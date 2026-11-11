// Logique pure : notation (type Sorbonne), note sur 20, tirage, bilan. Testée par tests/core.test.mjs.

export const KPRIM = 0, QCM = 1, QCS = 2;
export const FORMATS = { [KPRIM]: 'Kprim', [QCM]: 'QCM', [QCS]: 'QCS' };

/**
 * Points d'une question (0 à 1).
 * reponses : [1,0,0,1] (1 = vrai), dans l'ordre d'origine des propositions.
 * choix : null (passée) ou tableau de 4 dans le même ordre ;
 *   QCS/QCM : true = coché ; Kprim : true = « Vrai », false = « Faux », null = sans jugement.
 */
export function noter(mode, reponses, choix) {
  if (!choix) return 0;
  const vrai = reponses.map(r => r === 1);
  if (mode === KPRIM) return vrai.every((v, i) => choix[i] === v) ? 1 : 0;
  const coches = vrai.map((_, i) => choix[i] === true);
  if (mode === QCS) {
    const n = coches.filter(Boolean).length;
    return n === 1 && vrai[coches.indexOf(true)] ? 1 : 0;
  }
  if (coches.some((c, i) => c && !vrai[i])) return 0;
  const bonnesCochees = coches.filter(Boolean).length;
  const bonnes = vrai.filter(Boolean).length;
  if (bonnesCochees === 0) return 0;
  if (bonnesCochees === bonnes) return 1;
  return bonnesCochees === 1 ? 0.25 : 0.5;
}

/** Note sur 20 arrondie au centième ; null si aucune question. */
export function surVingt(points, n) {
  return n ? Math.round((points * 2000) / n) / 100 : null;
}

/** Copie mélangée (Fisher-Yates). */
export function melanger(liste, alea = Math.random) {
  const t = [...liste];
  for (let i = t.length - 1; i > 0; i--) {
    const j = Math.floor(alea() * (i + 1));
    [t[i], t[j]] = [t[j], t[i]];
  }
  return t;
}

/** n éléments tirés au hasard (tous si n est null ou dépasse la taille). */
export function tirer(liste, n, alea = Math.random) {
  const t = melanger(liste, alea);
  return n == null ? t : t.slice(0, n);
}

/**
 * Bilan d'une session.
 * lignes : [{ points, semestre, ue, ueIntitule, coursId, coursNom, importance, mode }]
 */
export function bilan(lignes) {
  const grouper = cle => {
    const m = new Map();
    for (const l of lignes) {
      const [k, nom] = cle(l);
      const g = m.get(k) ?? { cle: k, nom, points: 0, n: 0 };
      g.points += l.points;
      g.n += 1;
      m.set(k, g);
    }
    return [...m.values()]
      .map(g => ({ ...g, note: surVingt(g.points, g.n) }))
      .sort((a, b) => String(a.cle).localeCompare(String(b.cle), 'fr', { numeric: true }));
  };
  const points = lignes.reduce((s, l) => s + l.points, 0);
  const parCours = grouper(l => [l.coursId, l.coursNom]);
  const notes = parCours.map(c => c.note);
  return {
    points, n: lignes.length, note: surVingt(points, lignes.length),
    parSemestre: grouper(l => [l.semestre, `Semestre ${l.semestre}`]),
    parUE: grouper(l => [l.ue, `${l.ue} ${l.ueIntitule}`]),
    parCours,
    parImportance: grouper(l => [l.importance, l.importance]),
    parFormat: grouper(l => [l.mode, FORMATS[l.mode]]),
    // Plus faible / plus fort seulement si au moins deux cours se distinguent.
    plusFaible: parCours.length > 1 && Math.min(...notes) !== Math.max(...notes)
      ? parCours.filter(c => c.note === Math.min(...notes)).map(c => c.cle) : [],
    plusFort: parCours.length > 1 && Math.min(...notes) !== Math.max(...notes)
      ? parCours.filter(c => c.note === Math.max(...notes)).map(c => c.cle) : [],
  };
}
