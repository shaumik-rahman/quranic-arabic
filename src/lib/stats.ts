import { ALL_LESSONS, LESSON_INDEX, PATTERNS, TEXTS, TOTAL_TOKENS, UNITS, WORDS, coverage } from "./course";
import { strength } from "./srs";
import { dayKey, type ProgressData } from "./store";

export const wordKeysLearned = (p: ProgressData) => Object.keys(p.items).filter((k) => !k.startsWith("p:") && WORDS[k]);
export const patternsLearned = (p: ProgressData) => Object.keys(p.items).filter((k) => k.startsWith("p:") && PATTERNS[k.slice(2)]).map((k) => k.slice(2));

export function quranCoverage(p: ProgressData) {
  let learned = 0, mastered = 0, nLearned = 0, nMastered = 0, nStrong = 0;
  for (const k of wordKeysLearned(p)) {
    const c = WORDS[k].count;
    learned += c; nLearned++;
    const st = strength(p.items[k]);
    if (st === "mastered") { mastered += c; nMastered++; }
    if (st === "strong") nStrong++;
  }
  return {
    wordsLearned: nLearned,
    wordsMastered: nMastered,
    wordsStrong: nStrong,
    occurrencesLearned: learned,
    pctLearned: (100 * learned) / TOTAL_TOKENS,
    pctMastered: (100 * mastered) / TOTAL_TOKENS,
    totalCurriculumWords: Object.keys(WORDS).length,
  };
}

/** % of a curriculum text's words the learner knows */
export function textUnderstanding(p: ProgressData, textId: string) {
  const t = TEXTS.find((x) => x.id === textId);
  if (!t) return 0;
  let n = 0, k = 0;
  for (const l of t.lines) for (const tok of l.tokens) { n++; if (p.items[tok.key]) k++; }
  return n ? (100 * k) / n : 0;
}

export function surahCoverage(p: ProgressData) {
  const learnedBySurah: Record<number, number> = {};
  for (const k of wordKeysLearned(p)) {
    for (const [s, c] of coverage.lemmaSurah[k] || []) learnedBySurah[s] = (learnedBySurah[s] || 0) + c;
  }
  return coverage.surahs.map((s) => ({ ...s, known: learnedBySurah[s.n] || 0, pct: (100 * (learnedBySurah[s.n] || 0)) / s.total }));
}

export function weekStart(d = new Date()) {
  const x = new Date(d);
  const day = (x.getDay() + 6) % 7; // Monday = 0
  x.setDate(x.getDate() - day);
  return dayKey(x);
}
export function weeklyXp(p: ProgressData) {
  const ws = weekStart();
  return Object.entries(p.xpByDay).filter(([d]) => d >= ws).reduce((a, [, v]) => a + v, 0);
}
export const todayXp = (p: ProgressData) => p.xpByDay[dayKey()] || 0;
export function liveStreak(p: ProgressData) {
  if (!p.lastActiveDay) return 0;
  const today = dayKey();
  const yest = dayKey(new Date(Date.now() - 86_400_000));
  return p.lastActiveDay === today || p.lastActiveDay === yest ? p.streak : 0;
}

export function dueItems(p: ProgressData, now = Date.now()) {
  return Object.entries(p.items).filter(([, s]) => s.due <= now).sort((a, b) => a[1].due - b[1].due).map(([k]) => k);
}

export function isLessonUnlocked(p: ProgressData, lessonId: string, teacher: boolean) {
  if (teacher) return true;
  const i = LESSON_INDEX[lessonId];
  if (i === 0) return true;
  return !!p.completed[ALL_LESSONS[i - 1].id];
}
export function currentLessonId(p: ProgressData) {
  return ALL_LESSONS.find((l) => !p.completed[l.id])?.id ?? null;
}
export function unitProgress(p: ProgressData, unitId: string) {
  const u = UNITS.find((x) => x.id === unitId)!;
  const done = u.lessons.filter((l) => p.completed[l.id]).length;
  return { done, total: u.lessons.length };
}

export interface Badge { id: string; emoji: string; en: string; bn: string; earned: boolean; hint_en: string; hint_bn: string }
export function badges(p: ProgressData): Badge[] {
  const cov = quranCoverage(p);
  const out: Badge[] = [];
  for (const u of UNITS) {
    if (!u.completes) continue;
    const t = TEXTS.find((x) => x.id === u.completes)!;
    out.push({
      id: "text-" + t.id, emoji: t.emoji, en: t.en, bn: t.bn,
      earned: !!p.completed[u.lessons[u.lessons.length - 1].id],
      hint_en: "Understand every word", hint_bn: "প্রতিটি শব্দ বুঝুন",
    });
  }
  for (const n of [10, 50, 100, 150]) {
    out.push({ id: "words-" + n, emoji: "📚", en: `${n} words`, bn: `${n}টি শব্দ`, earned: cov.wordsLearned >= n, hint_en: `Learn ${n} Quranic words`, hint_bn: `${n}টি কুরআনি শব্দ শিখুন` });
  }
  for (const n of [10, 25, 40]) {
    out.push({ id: "cov-" + n, emoji: "📖", en: `${n}% of the Quran`, bn: `কুরআনের ${n}%`, earned: cov.pctLearned >= n, hint_en: `Know words making up ${n}% of the Quran`, hint_bn: `কুরআনের ${n}% শব্দ চিনুন` });
  }
  for (const n of [3, 7, 30]) {
    out.push({ id: "streak-" + n, emoji: "🔥", en: `${n}-day streak`, bn: `${n} দিনের ধারা`, earned: p.longestStreak >= n, hint_en: `Learn ${n} days in a row`, hint_bn: `টানা ${n} দিন শিখুন` });
  }
  return out;
}
