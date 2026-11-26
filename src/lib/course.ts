import courseJson from "@/data/course.json";
import coverageJson from "@/data/coverage.json";

export type Lang = "en" | "bn";

export interface FamilyMember { key: string; ar: string; count: number; ex: string; exIp?: string | null; gloss: string; ref: string; self: boolean }
export interface Word {
  key: string; pos: string; ar: string; en: string; bn: string; emoji: string;
  cog: { en?: string; bn?: string; hi?: string }; tip: string;
  lemma: string; root: string; rootSpaced: string; count: number; rank: number | null;
  audio: string | null; family: FamilyMember[];
}
export interface Token { ar: string; ip?: string | null; en: string; bn: string; key: string; pats: string[]; audio: string | null; tr: string; loc: string | null; known?: boolean }
export interface Line {
  id: string; ref: string; kind: "quran" | "hand" | "everyday"; verseAudio: string | null;
  en: string; bn: string; tokens: Token[]; ar: string; note_en?: string; note_bn?: string; newVerse?: boolean;
}
export interface TeachEx { ar: string; en: string; bn: string }
/** one swipeable teaching page */
export interface TeachPage { t_en: string; t_bn: string; x_en: string; x_bn: string; ex: TeachEx[]; vs: TeachEx[] }
/** an understanding check; options[0] is the right answer */
export interface Check {
  q_en: string; q_bn: string; ar: string | null; ar_opts: boolean;
  options: (string | { en: string; bn: string })[]; why_en: string; why_bn: string;
}
export interface Structure {
  id: string; en: string; bn: string; emoji: string;
  shape: { ar: string; en: string; bn: string; role: string }[];
  expl_en: string; expl_bn: string; notes: { en: string; bn: string }[]; quran: Line[]; everyday: Line[];
  chunk: Line | null; chunkVerses?: Line[]; chunkCount?: number;
  pages: TeachPage[]; checks: Check[];
}
export interface Text { id: string; en: string; bn: string; ar: string; emoji: string; desc_en: string; desc_bn: string; lines: Line[] }
export interface Lesson { id: string; type: "learn" | "final" | "structure" | "verses"; words: string[]; patterns: string[]; structure?: string; part?: number; parts?: number }
export interface Unit {
  id: string; text: string; en: string; bn: string; completes: string | null; emoji: string;
  lines: Line[]; lessons: Lesson[]; newWords: string[]; newPatterns: string[];
  structures: Structure[]; newVerses: Line[];
}
export interface Pattern {
  id: string; ar: string; en: string; bn: string; emoji: string; expl_en: string; expl_bn: string;
  more_en?: string; more_bn?: string; pages: TeachPage[]; checks: Check[];
  examples: { ar: string; ip?: string | null; en: string; bn: string; key?: string; audio: string | null }[];
}
export interface Course { totalTokens: number; words: Record<string, Word>; patterns: Record<string, Pattern>; texts: Text[]; units: Unit[] }

export const course = courseJson as unknown as Course;
export const coverage = coverageJson as unknown as {
  totalTokens: number;
  surahs: { n: number; ar: string; tr: string; en: string; bn: string; verses: number; total: number }[];
  lemmaSurah: Record<string, [number, number][]>;
};

export const WORDS = course.words;
export const PATTERNS = course.patterns;
export const UNITS = course.units;
export const TEXTS = course.texts;
export const TOTAL_TOKENS = course.totalTokens;

export const ALL_LESSONS: (Lesson & { unitId: string; unitIndex: number; indexInUnit: number })[] = [];
UNITS.forEach((u, ui) => u.lessons.forEach((l, li) => ALL_LESSONS.push({ ...l, unitId: u.id, unitIndex: ui, indexInUnit: li })));
export const LESSON_INDEX: Record<string, number> = Object.fromEntries(ALL_LESSONS.map((l, i) => [l.id, i]));

export const unitById = (id: string) => UNITS.find((u) => u.id === id)!;
export const textById = (id: string) => TEXTS.find((t) => t.id === id);
export const lessonById = (id: string) => ALL_LESSONS[LESSON_INDEX[id]];

/** The word list in curriculum order (for library sorting). */
export const WORD_ORDER: string[] = UNITS.flatMap((u) => u.newWords);
export const WORD_UNIT: Record<string, string> = {};
UNITS.forEach((u) => u.newWords.forEach((k) => (WORD_UNIT[k] = u.id)));
export const PATTERN_UNIT: Record<string, string> = {};
UNITS.forEach((u) => u.newPatterns.forEach((p) => (PATTERN_UNIT[p] = u.id)));

/** All curriculum lines incl. everyday sentences (for finding a word in context, distractors). */
export const ALL_LINES: Line[] = (() => {
  const seen = new Set<string>();
  const out: Line[] = [];
  for (const u of UNITS) {
    for (const l of u.lines) if (!seen.has(l.id)) { seen.add(l.id); out.push(l); }
    for (const s of u.structures || []) for (const l of s.everyday) if (!seen.has(l.id)) { seen.add(l.id); out.push(l); }
  }
  return out;
})();
export const STRUCTURES: Record<string, Structure & { unitId: string }> = {};
UNITS.forEach((u) => (u.structures || []).forEach((s) => (STRUCTURES[s.id] = { ...s, unitId: u.id })));

export const meaning = (w: { en: string; bn: string }, lang: Lang) => (lang === "bn" && w.bn ? w.bn : w.en);

export const WORD_AUDIO_BASE = "https://audio.qurancdn.com/wbw/";
export const VERSE_AUDIO_BASE = "https://everyayah.com/data/Alafasy_128kbps/";
export const wordAudioUrl = (id: string) => `${WORD_AUDIO_BASE}${id}.mp3`;
export const verseAudioUrl = (id: string) => `${VERSE_AUDIO_BASE}${id}.mp3`;

/** Glyph "emojis" that should render in the Quran font (no pictures for Allah / the Prophet ﷺ). */
export const isGlyph = (e: string) => e === "ﷲ" || e === "ﷺ";

export function linesWithWord(key: string): { line: Line; index: number }[] {
  const out: { line: Line; index: number }[] = [];
  for (const line of ALL_LINES) {
    const i = line.tokens.findIndex((t) => t.key === key);
    if (i >= 0) out.push({ line, index: i });
  }
  return out;
}

/** teaching material for "p:<pattern>" or "s:<structure>" */
export function teachOf(ref: string): { pages: TeachPage[]; checks: Check[] } {
  const [kind, id] = [ref.slice(0, 1), ref.slice(2)];
  const src = kind === "p" ? PATTERNS[id] : STRUCTURES[id];
  return { pages: src?.pages ?? [], checks: src?.checks ?? [] };
}
