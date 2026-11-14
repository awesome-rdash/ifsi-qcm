// Écrans du site : connexion, composition, question, correction, bilan, historique.
import { noter, surVingt, tirer, melanger, bilan, FORMATS, KPRIM, QCS } from './core.js';
import { EMPREINTE } from './config.js';

const app = document.getElementById('app');
const IMPORTANCES = { I0: 'à savoir par cœur', I1: 'important', I2: 'spécialité', I3: "spécifique à l'examen" };
const NOMBRE_DEFAUT = 20;
const HISTORIQUE_MAX = 100;
const CLES = { auth: 'ifsi.auth', session: 'ifsi.session', historique: 'ifsi.historique', prefs: 'ifsi.prefs' };

// ---------- Stockage local (peut être indisponible : navigation privée, quota) ----------
function lire(cle, defaut) {
  try { return JSON.parse(localStorage.getItem(cle)) ?? defaut; } catch { return defaut; }
}
function ecrire(cle, valeur) {
  try {
    if (valeur == null) localStorage.removeItem(cle);
    else localStorage.setItem(cle, JSON.stringify(valeur));
  } catch { /* stockage indisponible : le site marche sans mémoire */ }
}

// ---------- Utilitaires ----------
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => `&#${c.charCodeAt(0)};`);
const fr = (x, decimales = 0) => x == null ? '—'
  : x.toLocaleString('fr-FR', { minimumFractionDigits: decimales, maximumFractionDigits: 2 });
const note20 = x => `${fr(x, 2)} / 20`;

const BALISES = new Set(['B', 'I', 'U', 'BR', 'P', 'UL', 'OL', 'LI', 'TABLE', 'THEAD', 'TBODY', 'TR', 'TD', 'TH',
  'IMG', 'SPAN', 'DIV', 'SUP', 'SUB', 'A']);
const A_SUPPRIMER = new Set(['SCRIPT', 'STYLE', 'IFRAME', 'OBJECT', 'EMBED', 'NOSCRIPT', 'TEMPLATE', 'SVG', 'MATH',
  'FORM', 'INPUT', 'BUTTON', 'SELECT', 'TEXTAREA', 'VIDEO', 'AUDIO']);

/** Assainit un champ HTML (liste blanche). base : dossier du cours, pour les images media/…. */
export function assainir(html, base = '') {
  const t = document.createElement('template'); // document inerte : rien ne s'exécute ni ne se charge
  t.innerHTML = html ?? '';
  nettoyer(t.content, base);
  return t.innerHTML;
}
function nettoyer(parent, base) {
  for (const n of [...parent.childNodes]) {
    if (n.nodeType === Node.TEXT_NODE) continue;
    if (n.nodeType !== Node.ELEMENT_NODE) { n.remove(); continue; }
    const tag = n.tagName.toUpperCase();
    if (A_SUPPRIMER.has(tag)) { n.remove(); continue; }
    nettoyer(n, base);
    if (!BALISES.has(tag)) { n.replaceWith(...n.childNodes); continue; }
    for (const a of [...n.attributes]) {
      const v = a.value.trim();
      const ok = (tag === 'IMG' && a.name === 'src' && /^media\/[\w.-]+$/.test(v))
        || (tag === 'A' && a.name === 'href' && /^https?:\/\//i.test(v))
        || ((a.name === 'colspan' || a.name === 'rowspan') && /^\d+$/.test(v));
      if (!ok) n.removeAttribute(a.name);
    }
    if (tag === 'IMG') {
      if (!n.hasAttribute('src')) { n.remove(); continue; }
      n.setAttribute('src', base + n.getAttribute('src'));
      n.setAttribute('loading', 'lazy');
      n.setAttribute('alt', '');
    }
    if (tag === 'A') { n.setAttribute('target', '_blank'); n.setAttribute('rel', 'noopener noreferrer'); }
  }
}

/** Met en évidence les signalements ⛔ ✎ ⚠ (jusqu'à la balise suivante). */
const surligner = html => html.replace(/[⛔✎⚠][^<]*/g,
  m => `<mark class="${{ '⛔': 'danger', '✎': 'modif', '⚠': 'nonconf' }[m[0]]}">${m}</mark>`);

async function empreinte(texte) {
  const h = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(texte));
  return [...new Uint8Array(h)].map(b => b.toString(16).padStart(2, '0')).join('');
}

function afficher(html, entete = true) {
  app.innerHTML = (entete ? `<header class="entete">
      <a href="#" class="marque" data-action="accueil">Révisions QCM IFSI</a>
      <button type="button" class="lien" data-action="historique">Historique</button>
    </header>` : '') + html;
  window.scrollTo(0, 0);
  app.querySelector('[tabindex="-1"]')?.focus();
}

// ---------- Données ----------
let catalogue = null;            // index.json : liste des cours
const charges = new Map();       // id du cours -> { meta, base, parGuid }
let session = null;              // voir specs/001-site-revision-qcm/data-model.md

async function chargerCatalogue() {
  if (catalogue) return catalogue;
  const r = await fetch('data/index.json', { cache: 'no-cache' });
  if (!r.ok) throw new Error(`catalogue : HTTP ${r.status}`);
  catalogue = (await r.json()).cours;
  return catalogue;
}

async function chargerCours(id) {
  if (charges.has(id)) return charges.get(id);
  const entree = catalogue.find(c => c.id === id);
  if (!entree) return null;
  const r = await fetch(entree.fichier, { cache: 'no-cache' });
  if (!r.ok) throw new Error(`${entree.nom} : HTTP ${r.status}`);
  const d = await r.json();
  const c = { meta: d.cours, base: entree.fichier.replace(/questions\.json$/, ''),
    questions: d.questions, parGuid: new Map(d.questions.map(q => [q.guid, q])) };
  charges.set(id, c);
  return c;
}

const questionDe = it => charges.get(it.cours)?.parGuid.get(it.guid);
const sauver = () => ecrire(CLES.session, session);

// ---------- Connexion ----------
function ecranConnexion() {
  afficher(`<h1 tabindex="-1">Révisions QCM IFSI</h1>
    <form class="connexion" id="f-connexion">
      <label for="mdp">Mot de passe de la promotion</label>
      <input id="mdp" type="password" autocomplete="current-password" required>
      <p id="erreur" class="erreur" role="alert"></p>
      <button class="principal">Entrer</button>
    </form>`, false);
  const f = document.getElementById('f-connexion');
  f.addEventListener('submit', async e => {
    e.preventDefault();
    const err = document.getElementById('erreur');
    if (!crypto.subtle) { err.textContent = 'Navigateur trop ancien ou connexion non sécurisée (https requis).'; return; }
    if (await empreinte(f.mdp.value.trim()) === EMPREINTE) {
      ecrire(CLES.auth, EMPREINTE);
      ecranAccueil();
    } else {
      err.textContent = 'Mot de passe incorrect.';
      f.mdp.select();
    }
  });
  f.mdp.focus();
}

// ---------- Accueil : composition de la session ----------
function prefs() {
  return { importances: Object.keys(IMPORTANCES), correction: 'chaque', nombres: {}, coches: [],
    global: NOMBRE_DEFAUT, ...lire(CLES.prefs, {}) };
}

async function ecranAccueil() {
  afficher('<p class="info">Chargement des cours…</p>');
  try { await chargerCatalogue(); } catch (e) {
    afficher(`<p class="erreur" tabindex="-1">Impossible de charger la liste des cours (${esc(e.message)}).</p>
      <button data-action="accueil">Réessayer</button>`);
    return;
  }
  session = lire(CLES.session, null);
  const p = prefs();
  const nombre = id => (id in p.nombres ? p.nombres[id] : p.global) ?? '';

  // Arbre Semestre -> UE -> Cours
  const sems = new Map();
  for (const c of [...catalogue].sort((a, b) => a.semestre - b.semestre
    || a.ue.localeCompare(b.ue, 'fr', { numeric: true }) || a.nom.localeCompare(b.nom, 'fr', { numeric: true }))) {
    if (!sems.has(c.semestre)) sems.set(c.semestre, new Map());
    const ues = sems.get(c.semestre);
    if (!ues.has(c.ue)) ues.set(c.ue, { intitule: c.ue_intitule, cours: [] });
    ues.get(c.ue).cours.push(c);
  }
  const caseGroupe = libelle => `<label class="choix"><input type="checkbox" data-groupe-case>
    <span>${esc(libelle)} <span class="compte"></span></span></label>`;
  const arbre = [...sems].map(([s, ues]) => `<li data-groupe>${caseGroupe(`Semestre ${s}`)}<ul>${
    [...ues].map(([ue, u]) => `<li data-groupe>${caseGroupe(`${ue} ${u.intitule}`)}<ul>${
      u.cours.map(c => `<li class="cours" data-id="${esc(c.id)}">
        <label class="choix"><input type="checkbox" name="cours" value="${esc(c.id)}"
          ${p.coches.includes(c.id) ? 'checked' : ''}><span>${esc(c.nom)} <span class="compte"></span></span></label>
        <input type="number" min="1" inputmode="numeric" name="nb-${esc(c.id)}" value="${esc(nombre(c.id))}"
          placeholder="toutes" aria-label="Nombre de questions pour ${esc(c.nom)} (vide = toutes)">
      </li>`).join('')}</ul></li>`).join('')}</ul></li>`).join('');

  const reprise = session ? (() => {
    const fait = session.items.filter(i => i.statut).length;
    return `<section class="encart" aria-labelledby="t-reprise">
      <h2 id="t-reprise">Session en cours</h2>
      <p>${fait} / ${session.items.length} questions faites.</p>
      <div class="actions"><button class="principal" data-action="reprendre">Reprendre</button>
      <button data-action="abandonner">Abandonner</button></div></section>`;
  })() : '';

  afficher(`<h1 tabindex="-1">Composer une session</h1>${reprise}
    <form id="f-compo">
      <fieldset><legend>Importance</legend><div class="ligne">${Object.entries(IMPORTANCES).map(([k, v]) => `
        <label class="choix"><input type="checkbox" name="imp" value="${k}" ${p.importances.includes(k) ? 'checked' : ''}>
        <span>${k} — ${v}</span></label>`).join('')}</div></fieldset>
      <fieldset><legend>Correction</legend><div class="ligne">
        <label class="choix"><input type="radio" name="correction" value="chaque" ${p.correction !== 'fin' ? 'checked' : ''}>
          <span>Après chaque question</span></label>
        <label class="choix"><input type="radio" name="correction" value="fin" ${p.correction === 'fin' ? 'checked' : ''}>
          <span>À la fin seulement</span></label></div></fieldset>
      <fieldset class="arbre" data-groupe><legend>Cours</legend>
        ${catalogue.length ? caseGroupe('Tout') : '<p class="info">Aucun cours publié.</p>'}
        <ul>${arbre}</ul>
        <div class="global">
          <label for="nb-global">Nombre par cours</label>
          <input id="nb-global" type="number" min="1" inputmode="numeric" placeholder="toutes" value="${esc(p.global ?? '')}">
          <button type="button" id="appliquer">Appliquer aux cours cochés</button>
        </div>
      </fieldset>
      <p class="total" id="total" aria-live="polite"></p>
      <div class="actions"><button class="principal" id="commencer">Commencer</button></div>
    </form>`);

  const f = document.getElementById('f-compo');
  const importances = () => [...f.querySelectorAll('[name=imp]:checked')].map(i => i.value);
  const dispo = (c, imps) => imps.reduce((s, k) => s + (c.par_importance[k] ?? 0), 0);

  const lireChoix = () => {
    const imps = importances();
    return [...f.querySelectorAll('li.cours')].map(li => {
      const c = catalogue.find(x => x.id === li.dataset.id);
      const v = li.querySelector('input[type=number]').value;
      return { id: c.id, coche: li.querySelector('[name=cours]').checked, dispo: dispo(c, imps),
        nombre: v === '' ? null : Math.max(1, parseInt(v, 10) || 1) };
    });
  };

  const maj = () => {
    const choix = lireChoix();
    const parId = new Map(choix.map(c => [c.id, c]));
    for (const li of f.querySelectorAll('li.cours')) li.querySelector('.compte').textContent = `(${parId.get(li.dataset.id).dispo})`;
    for (const g of f.querySelectorAll('[data-groupe]')) {
      const cs = [...g.querySelectorAll('li.cours')].map(li => parId.get(li.dataset.id));
      const lab = g.querySelector(':scope > label');
      if (!lab) continue;
      lab.querySelector('.compte').textContent = `(${cs.reduce((s, c) => s + c.dispo, 0)})`;
      const k = cs.filter(c => c.coche).length;
      const box = lab.querySelector('input');
      box.checked = k > 0 && k === cs.length;
      box.indeterminate = k > 0 && k < cs.length;
    }
    const total = choix.filter(c => c.coche).reduce((s, c) => s + Math.min(c.nombre ?? Infinity, c.dispo), 0);
    document.getElementById('total').textContent = `Total : ${total} question${total > 1 ? 's' : ''}`;
    document.getElementById('commencer').disabled = total === 0;
    const g = document.getElementById('nb-global').value;
    ecrire(CLES.prefs, {
      importances: importances(), correction: f.correction.value,
      coches: choix.filter(c => c.coche).map(c => c.id),
      nombres: Object.fromEntries(choix.map(c => [c.id, c.nombre])),
      global: g === '' ? null : parseInt(g, 10) || NOMBRE_DEFAUT,
    });
    return choix;
  };

  f.addEventListener('change', e => {
    if (e.target.matches('[data-groupe-case]')) {
      const g = e.target.closest('[data-groupe]');
      for (const b of g.querySelectorAll('[name=cours]')) b.checked = e.target.checked;
    }
    maj();
  });
  f.addEventListener('input', e => { if (e.target.type === 'number') maj(); });
  document.getElementById('appliquer').addEventListener('click', () => {
    const v = document.getElementById('nb-global').value;
    for (const li of f.querySelectorAll('li.cours')) {
      if (li.querySelector('[name=cours]').checked) li.querySelector('input[type=number]').value = v;
    }
    maj();
  });
  f.addEventListener('submit', e => {
    e.preventDefault();
    const choix = maj().filter(c => c.coche && c.dispo > 0);
    commencer(choix, importances(), f.correction.value);
  });
  maj();
}

async function commencer(choix, imps, correction) {
  if (session && !confirm('Une session est en cours. La remplacer ?')) return;
  afficher('<p class="info" tabindex="-1">Préparation des questions…</p>');
  try {
    const tirees = [];
    for (const c of choix) {
      const cours = await chargerCours(c.id);
      tirees.push(...tirer(cours.questions.filter(q => imps.includes(q.importance)), c.nombre)
        .map(q => ({ cours: c.id, guid: q.guid })));
    }
    demarrer(tirees, correction);
  } catch (e) {
    afficher(`<p class="erreur" tabindex="-1">Impossible de charger les questions (${esc(e.message)}).
      Vérifiez la connexion.</p><button data-action="accueil">Retour</button>`);
  }
}

function demarrer(refs, correction) {
  session = { v: 1, correction, items: melanger(refs).map(r => ({
    cours: r.cours, guid: r.guid, ordre: melanger([0, 1, 2, 3]), choix: null, statut: null })) };
  sauver();
  ecranQuestion();
}

async function reprendre() {
  afficher('<p class="info" tabindex="-1">Chargement de la session…</p>');
  try {
    await chargerCatalogue();
    for (const id of new Set(session.items.map(i => i.cours))) await chargerCours(id);
  } catch (e) {
    afficher(`<p class="erreur" tabindex="-1">Impossible de charger les questions (${esc(e.message)}).</p>
      <button data-action="accueil">Retour</button>`);
    return;
  }
  session.items = session.items.filter(questionDe); // questions retirées depuis par une publication
  if (!session.items.length) { session = null; sauver(); return ecranAccueil(); }
  sauver();
  ecranQuestion();
}

// ---------- Question ----------
const LETTRES = 'ABCD';

function ecranQuestion() {
  const i = session.items.findIndex(it => !it.statut);
  if (i < 0) return terminer();
  const it = session.items[i];
  const q = questionDe(it);
  const c = charges.get(it.cours);
  const n = session.items.length;
  const prop = k => assainir(q.propositions[k], c.base);

  let corps;
  if (q.mode === KPRIM) {
    corps = it.ordre.map((k, j) => `<fieldset class="prop kprim"><legend>${LETTRES[j]}. ${prop(k)}</legend>
      <div class="vf">
        <label class="choix"><input type="radio" name="p${k}" value="V"><span>Vrai</span></label>
        <label class="choix"><input type="radio" name="p${k}" value="F"><span>Faux</span></label>
      </div></fieldset>`).join('');
  } else {
    const type = q.mode === QCS ? 'radio' : 'checkbox';
    corps = `<fieldset class="nu"><legend class="sr">Propositions</legend>${it.ordre.map((k, j) => `
      <label class="prop choix"><input type="${type}" name="p" value="${k}"><span>${LETTRES[j]}. ${prop(k)}</span></label>`).join('')}
      </fieldset>`;
  }

  afficher(`<div class="progres"><span>Question ${i + 1} / ${n}</span><span>${esc(c.meta.nom)}</span></div>
    <progress max="${n}" value="${i}" aria-hidden="true"></progress>
    ${enonce(q, c, true)}
    <form id="f-rep">${corps}
      <div class="actions"><button class="principal">Valider</button>
      <button type="button" id="passer">Passer</button></div>
    </form>`);

  const f = document.getElementById('f-rep');
  f.addEventListener('submit', e => {
    e.preventDefault();
    it.choix = q.mode === KPRIM
      ? [0, 1, 2, 3].map(k => ({ V: true, F: false })[f.querySelector(`[name=p${k}]:checked`)?.value] ?? null)
      : [0, 1, 2, 3].map(k => f.querySelector(`[name=p][value="${k}"]`).checked);
    it.statut = 'repondu';
    sauver();
    if (session.correction === 'chaque') ecranCorrection(it, i);
    else ecranQuestion();
  });
  document.getElementById('passer').addEventListener('click', () => {
    it.choix = null;
    it.statut = 'passe';
    sauver();
    ecranQuestion();
  });
}

function enonce(q, c, focus) {
  return `<p class="contexte">${esc(c.meta.contexte)}</p>
    <h2 ${focus ? 'tabindex="-1"' : ''}>${assainir(q.titre, c.base)}</h2>
    <div class="badges"><span class="badge">${FORMATS[q.mode]}</span>
      <span class="badge" title="${esc(IMPORTANCES[q.importance])}">${q.importance} — ${esc(IMPORTANCES[q.importance])}</span></div>
    <div class="enonce">${assainir(q.question, c.base)}</div>
    ${q.image ? `<img src="${esc(c.base + q.image)}" alt="Illustration de la question" loading="lazy">` : ''}`;
}

// ---------- Correction ----------
function correction(it) {
  const q = questionDe(it);
  const c = charges.get(it.cours);
  const pts = noter(q.mode, q.reponses, it.choix);
  // Couleur = vérité de la proposition (vraie en vert) ; erreur de l'étudiant = barre rouge + texte.
  const lignes = it.ordre.map((k, j) => {
    const bon = q.reponses[k] === 1;
    let donne, marque, juste, verdict;
    if (q.mode === KPRIM) {
      const v = it.choix?.[k] ?? null;
      donne = v == null ? 'sans réponse' : v ? 'Vrai' : 'Faux';
      marque = v == null ? '–' : v ? 'V' : 'F';
      juste = v === bon;
      verdict = juste ? 'Bien jugé' : v == null ? 'Pas de réponse' : `Vous avez répondu ${donne}`;
    } else {
      const coche = it.choix?.[k] === true;
      donne = coche ? 'cochée' : 'non cochée';
      marque = q.mode === QCS ? (coche ? '◉' : '○') : (coche ? '☑' : '☐');
      juste = coche === bon;
      verdict = juste ? (coche ? 'Bien cochée' : 'Bien laissée') : coche ? 'Cochée à tort' : 'Oubliée : il fallait la cocher';
    }
    return `<li class="${bon ? 'vraie' : 'fausse'}${juste ? '' : ' rate'}">
      <span class="marque-eleve" aria-hidden="true">${marque}</span>
      <span class="txt">${LETTRES[j]}. ${assainir(q.propositions[k], c.base)}</span>
      <span class="verite">${bon ? '✓ Vraie' : '✗ Fausse'}</span>
      <span class="verdict"><span class="sr">Votre réponse : ${donne}. </span>${juste ? '✓' : '✗'} ${verdict}</span></li>`;
  }).join('');
  return `<div class="correction">
    <p class="points">${it.statut === 'passe' ? 'Question passée — ' : ''}${fr(pts)} point${pts > 1 ? 's' : ''} sur 1</p>
    <ul class="props">${lignes}</ul>
    ${q.danger ? '<p class="alerte-danger">⛔ Erreur dangereuse signalée pour cette question (voir ci-dessous).</p>' : ''}
    ${q.infos ? `<div class="infos">${surligner(assainir(q.infos, c.base))}</div>` : ''}
    ${q.page_cours.length ? `<div class="pages"><h4>Page${q.page_cours.length > 1 ? 's' : ''} du cours</h4>${
      q.page_cours.map(p => `<a href="${esc(c.base + p)}" target="_blank" rel="noopener">
        <img src="${esc(c.base + p)}" alt="Page du cours (ouvrir en grand)" loading="lazy"></a>`).join('')}</div>` : ''}
    ${q.sources ? `<p class="sources"><b>Sources :</b> ${assainir(q.sources, c.base)}</p>` : ''}
  </div>`;
}

function ecranCorrection(it, i) {
  const q = questionDe(it);
  const c = charges.get(it.cours);
  const n = session.items.length;
  afficher(`<div class="progres"><span>Question ${i + 1} / ${n}</span><span>${esc(c.meta.nom)}</span></div>
    <progress max="${n}" value="${i + 1}" aria-hidden="true"></progress>
    ${enonce(q, c, false)}
    <h3 tabindex="-1">Correction</h3>${correction(it)}
    <div class="actions"><button class="principal" data-action="suivante">${i + 1 < n ? 'Question suivante' : 'Voir le bilan'}</button></div>`);
}

// ---------- Bilan ----------
function terminer() {
  const lignes = session.items.map(it => {
    const q = questionDe(it);
    const m = charges.get(it.cours).meta;
    return { points: noter(q.mode, q.reponses, it.choix), semestre: m.semestre, ue: m.ue, ueIntitule: m.ue_intitule,
      coursId: m.id, coursNom: m.nom, importance: q.importance, mode: q.mode };
  });
  const b = bilan(lignes);
  const garder = ({ cle, nom, points, n, note }) => ({ cle, nom, points, n, note });
  const hist = lire(CLES.historique, []);
  hist.push({ date: new Date().toISOString(), points: b.points, n: b.n, note: b.note,
    parCours: b.parCours.map(garder), parImportance: b.parImportance.map(garder), parFormat: b.parFormat.map(garder) });
  ecrire(CLES.historique, hist.slice(-HISTORIQUE_MAX));

  const fini = session;
  session = null;
  sauver();
  const erreurs = fini.items.filter((it, k) => lignes[k].points < 1);

  const tableau = (titre, groupes, marquer = false) => `<h3>${titre}</h3><div class="tableau"><table>
    <thead><tr><th scope="col">${titre.replace('Par ', '').replace(/^./, s => s.toUpperCase())}</th>
      <th scope="col" class="num">Questions</th><th scope="col" class="num">Note</th></tr></thead><tbody>${
    groupes.map(g => {
      const faible = marquer && b.plusFaible.includes(g.cle), fort = marquer && b.plusFort.includes(g.cle);
      return `<tr class="${faible ? 'faible' : fort ? 'fort' : ''}"><td>${esc(g.nom)}${
        faible ? ' <strong>▼ à retravailler</strong>' : fort ? ' <strong>▲ point fort</strong>' : ''}</td>
        <td class="num">${g.n}</td><td class="num">${note20(g.note)}</td></tr>`;
    }).join('')}</tbody></table></div>`;

  afficher(`<h1 tabindex="-1">Bilan</h1>
    <p class="note">${note20(b.note)}</p>
    <p>${fr(b.points)} / ${b.n} points</p>
    ${tableau('Par cours', b.parCours, true)}
    ${b.parUE.length > 1 ? tableau('Par UE', b.parUE) : ''}
    ${b.parSemestre.length > 1 ? tableau('Par semestre', b.parSemestre) : ''}
    ${tableau('Par importance', b.parImportance)}
    ${tableau('Par format', b.parFormat)}
    <h2>Questions ratées ou partielles (${erreurs.length})</h2>
    ${erreurs.length ? erreurs.map(it => {
      const q = questionDe(it), c = charges.get(it.cours);
      return `<details class="revoir"><summary>${fr(noter(q.mode, q.reponses, it.choix))} pt —
        ${esc(c.meta.nom)} — ${assainir(q.titre, c.base)}</summary>${enonce(q, c, false)}${correction(it)}</details>`;
    }).join('') : '<p>Aucune : bravo.</p>'}
    <div class="actions">
      ${erreurs.length ? `<button class="principal" id="refaire">Refaire mes erreurs (${erreurs.length})</button>` : ''}
      <button data-action="accueil">Retour à l'accueil</button>
    </div>`);
  document.getElementById('refaire')?.addEventListener('click',
    () => demarrer(erreurs.map(({ cours, guid }) => ({ cours, guid })), fini.correction));
}

// ---------- Historique ----------
function ecranHistorique() {
  const hist = lire(CLES.historique, []);
  const evolution = new Map();
  for (const h of hist) for (const c of h.parCours) {
    if (!evolution.has(c.cle)) evolution.set(c.cle, { nom: c.nom, notes: [] });
    evolution.get(c.cle).notes.push(c.note);
  }
  const date = iso => new Date(iso).toLocaleString('fr-FR', { dateStyle: 'short', timeStyle: 'short' });
  afficher(`<h1 tabindex="-1">Historique</h1>
    ${hist.length ? `<h2>Évolution par cours</h2><div class="tableau"><table>
      <thead><tr><th scope="col">Cours</th><th scope="col">Notes successives / 20</th></tr></thead><tbody>
      ${[...evolution.values()].map(e => `<tr><td>${esc(e.nom)}</td><td>${e.notes.map(x => fr(x, 2)).join(' → ')}</td></tr>`).join('')}
      </tbody></table></div>
      <h2>Sessions</h2><div class="tableau"><table>
      <thead><tr><th scope="col">Date</th><th scope="col">Cours</th><th scope="col" class="num">Questions</th><th scope="col" class="num">Note</th></tr></thead><tbody>
      ${[...hist].reverse().map(h => `<tr><td>${date(h.date)}</td><td>${h.parCours.map(c => esc(c.nom)).join(', ')}</td>
        <td class="num">${h.n}</td><td class="num">${note20(h.note)}</td></tr>`).join('')}
      </tbody></table></div>` : '<p>Aucune session terminée sur cet appareil.</p>'}
    <h2>Mes données</h2>
    <p>Historique, session en cours et préférences sont gardés uniquement sur cet appareil.</p>
    <div class="actions"><button data-action="effacer">Effacer mes données</button>
      <button data-action="deconnexion">Se déconnecter</button></div>`);
}

// ---------- Actions communes ----------
const ACTIONS = {
  accueil: ecranAccueil,
  historique: ecranHistorique,
  reprendre,
  suivante: ecranQuestion,
  abandonner() {
    if (!confirm('Abandonner la session en cours ?')) return;
    session = null; sauver(); ecranAccueil();
  },
  effacer() {
    if (!confirm('Effacer l’historique, la session en cours et les préférences de cet appareil ?')) return;
    for (const k of [CLES.session, CLES.historique, CLES.prefs]) ecrire(k, null);
    session = null;
    ecranHistorique();
  },
  deconnexion() { ecrire(CLES.auth, null); ecranConnexion(); },
};

app.addEventListener('click', e => {
  const b = e.target.closest('[data-action]');
  if (b) { e.preventDefault(); ACTIONS[b.dataset.action](); }
});

// Pied de page : version, date de mise à jour et changelog (site/data/version.json, produit à la publication).
const dateHeure = iso => {
  const d = new Date(iso), tz = { timeZone: 'Europe/Paris' };
  return `${d.toLocaleDateString('sv-SE', tz)} à ${d.toLocaleTimeString('fr-FR', { ...tz, hour: '2-digit', minute: '2-digit' })}`;
};
fetch('data/version.json', { cache: 'no-cache' }).then(r => r.ok ? r.json() : null).then(v => {
  if (!v) return;
  const maj = document.getElementById('maj'), ver = document.getElementById('version');
  maj.textContent = `Mis à jour le ${dateHeure(v.date)}`;
  ver.querySelector('summary span').textContent = v.version;
  for (const c of v.changelog) {
    const li = document.createElement('li');
    li.textContent = `Version ${c.version} (${dateHeure(c.date)}) : ${c.raison}`;
    ver.querySelector('ul').append(li);
  }
  maj.hidden = ver.hidden = false;
}).catch(() => {});

if (lire(CLES.auth, null) === EMPREINTE && EMPREINTE !== 'A_DEFINIR') ecranAccueil();
else ecranConnexion();
