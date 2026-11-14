import { test } from 'node:test';
import assert from 'node:assert/strict';
import { noter, surVingt, tirer, melanger, bilan, KPRIM, QCM, QCS } from '../site/js/core.js';

const C = s => [...s].map(c => c === 'x');            // 'x..x' -> cases cochées
const K = s => [...s].map(c => ({ V: true, F: false })[c] ?? null); // 'VF?V' -> jugements

test('QCS', () => {
  assert.equal(noter(QCS, [0, 1, 0, 0], C('.x..')), 1);
  assert.equal(noter(QCS, [0, 1, 0, 0], C('x...')), 0);
  assert.equal(noter(QCS, [0, 1, 0, 0], C('....')), 0);
  assert.equal(noter(QCS, [0, 1, 0, 0], C('xx..')), 0, 'deux choix = pas « la » bonne réponse');
  assert.equal(noter(QCS, [0, 1, 0, 0], null), 0, 'passée');
});

test('QCM : réponse exacte', () => {
  assert.equal(noter(QCM, [1, 0, 0, 1], C('x..x')), 1);
  assert.equal(noter(QCM, [1, 1, 1, 1], C('xxxx')), 1);
  assert.equal(noter(QCM, [0, 0, 1, 0], C('..x.')), 1);
});

test('QCM : une proposition fausse cochée → 0, quoi qu’il y ait d’autre', () => {
  assert.equal(noter(QCM, [1, 0, 0, 1], C('xx.x')), 0);
  assert.equal(noter(QCM, [1, 0, 0, 1], C('.x..')), 0);
  assert.equal(noter(QCM, [1, 0, 0, 1], C('xxxx')), 0);
  assert.equal(noter(QCM, [1, 1, 1, 0], C('xxxx')), 0);
});

test('QCM : incomplète sans fausse cochée', () => {
  assert.equal(noter(QCM, [1, 0, 0, 1], C('x...')), 0.25, 'une bonne sur deux');
  assert.equal(noter(QCM, [1, 1, 1, 0], C('x...')), 0.25, 'une bonne sur trois');
  assert.equal(noter(QCM, [1, 1, 1, 0], C('xx..')), 0.5, 'deux bonnes sur trois');
  assert.equal(noter(QCM, [1, 1, 1, 1], C('xxx.')), 0.5, 'jamais plus de 0,5 si incomplète');
  assert.equal(noter(QCM, [1, 1, 1, 1], C('x...')), 0.25);
});

test('QCM : rien coché ou passée → 0', () => {
  assert.equal(noter(QCM, [1, 0, 0, 1], C('....')), 0);
  assert.equal(noter(QCM, [1, 0, 0, 1], null), 0);
});

test('Kprim', () => {
  assert.equal(noter(KPRIM, [1, 1, 1, 0], K('VVVF')), 1);
  assert.equal(noter(KPRIM, [0, 0, 0, 0], K('FFFF')), 1);
  assert.equal(noter(KPRIM, [1, 1, 1, 0], K('VVVV')), 0, 'un jugement faux');
  assert.equal(noter(KPRIM, [1, 1, 1, 0], K('VVV?')), 0, 'un jugement manquant');
  assert.equal(noter(KPRIM, [1, 1, 1, 0], K('????')), 0);
  assert.equal(noter(KPRIM, [1, 1, 1, 0], null), 0);
});

test('note sur 20 arrondie au centième', () => {
  assert.equal(surVingt(4, 5), 16);
  assert.equal(surVingt(1.25, 3), 8.33);
  assert.equal(surVingt(2, 3), 13.33);
  assert.equal(surVingt(0.25, 8), 0.63, 'arrondi du demi vers le haut (0,625)');
  assert.equal(surVingt(0, 7), 0);
  assert.equal(surVingt(7, 7), 20);
  assert.equal(surVingt(0, 0), null);
});

test('tirage', () => {
  const l = [...Array(10).keys()];
  assert.equal(tirer(l, 3).length, 3);
  assert.equal(tirer(l, 50).length, 10, 'plus que disponible → tout');
  assert.equal(tirer(l, null).length, 10, 'toutes');
  assert.deepEqual([...tirer(l, 10)].sort((a, b) => a - b), l, 'sans doublon');
  assert.deepEqual([...melanger(l)].sort((a, b) => a - b), l);
  assert.deepEqual(l, [...Array(10).keys()], 'liste d’origine intacte');
});

test('bilan', () => {
  const L = (coursId, points, extra = {}) => ({
    points, semestre: 3, ue: 'UE 2.8', ueIntitule: 'Processus obstructifs', coursId,
    coursNom: coursId, importance: 'I0', mode: QCM, ...extra,
  });
  const b = bilan([L('a', 1), L('a', 1), L('a', 1), L('b', 1, { mode: QCS, importance: 'I2' }), L('b', 0)]);
  assert.equal(b.note, 16);
  assert.equal(b.points, 4);
  assert.equal(b.n, 5);
  assert.deepEqual(b.parCours.map(c => [c.cle, c.n, c.note]), [['a', 3, 20], ['b', 2, 10]]);
  assert.deepEqual(b.plusFaible, ['b']);
  assert.deepEqual(b.plusFort, ['a']);
  assert.deepEqual(b.parFormat.map(f => [f.nom, f.n]), [['QCM', 4], ['QCS', 1]]);
  assert.deepEqual(b.parImportance.map(f => [f.cle, f.note]), [['I0', 15], ['I2', 20]]);
  assert.deepEqual(bilan([L('a', 1)]).plusFaible, [], 'un seul cours : rien à signaler');
});
