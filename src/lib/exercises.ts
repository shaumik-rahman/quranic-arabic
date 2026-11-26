import { ALL_LINES, PATTERNS, UNITS, WORDS, WORD_ORDER, linesWithWord, lessonById, unitById, type Line, type Token } from "./course";
import type { ProgressData } from "./store";
import { dueItems } from "./stats";

export type Exercise =
  | { kind: "intro"; word: string }
  | { kind: "pattern"; pattern: string }
  | { kind: "mcq"; mode: "ar2mean" | "mean2ar" | "listen"; word: string; options: string[] }
  | { kind: "patternq"; pattern: string; token: Token; options: Token[] }
  | { kind: "spot"; lineId: string; word: string }
  | { kind: "fill"; lineId: string; blank: number; options: string[] }
  | { kind: "match"; words: string[] }
  | { kind: "build"; lineId: string; from: number; to: number; extras: Token[] }
  | { kind: "meaning"; lineId: string; options: string[] };

export type Step = Exercise & { id: string; item?: string };

/** Lines from the first `n` units (what the learner has met so far). */
let poolLines: Line[] = ALL_LINES;
function setPool(unitIndex: number | null) {
  if (unitIndex === null) { poolLines = ALL_LINES; return; }
  const seen = new Set<string>();
  poolLines = [];
  for (const u of UNITS.slice(0, Math.max(unitIndex + 1, 2))) for (const l of u.lines) if (!seen.has(l.id)) { seen.add(l.id); poolLines.push(l); }
}

export const isGraded = (e: Exercise) => e.kind !== "intro" && e.kind !== "pattern";

// ---------- helpers ----------
const LINE_MAP: Record<string, Line> = {};
for (const u of UNITS) for (const l of u.lines) LINE_MAP[l.id] = l;
for (const l of ALL_LINES) LINE_MAP[l.id] = l;
export const lineById = (id: string) => LINE_MAP[id];

function shuffle<T>(a: T[]): T[] {
  const b = [...a];
  for (let i = b.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [b[i], b[j]] = [b[j], b[i]];
  }
  return b;
}
const pick = <T,>(a: T[]) => a[Math.floor(Math.random() * a.length)];
let counter = 0;
const sid = () => `s${++counter}`;

/** Words the learner could plausibly know by this point, for distractors. */
function distractorPool(target: string, progress: ProgressData | null) {
  const idx = WORD_ORDER.indexOf(target);
  const near = WORD_ORDER.slice(0, Math.max(idx + 6, 12));
  const known = progress ? Object.keys(progress.items).filter((k) => WORDS[k]) : [];
  return Array.from(new Set([...near, ...known]));
}
function wordOptions(target: string, progress: ProgressData | null, n = 4) {
  const tw = WORDS[target];
  const pool = shuffle(distractorPool(target, progress)).filter(
    (k) => k !== target && WORDS[k].en !== tw.en && WORDS[k].emoji !== tw.emoji && WORDS[k].ar !== tw.ar,
  );
  return shuffle([target, ...pool.slice(0, n - 1)]);
}

function mcq(word: string, mode: "ar2mean" | "mean2ar" | "listen", progress: ProgressData | null): Step {
  return { id: sid(), kind: "mcq", mode, word, options: wordOptions(word, progress), item: word };
}

function spot(word: string, preferLines?: Line[]): Step | null {
  const inPref = (preferLines || []).filter((l) => l.tokens.some((t) => t.key === word) && l.tokens.length >= 2);
  const cands = inPref.length ? inPref : linesWithWord(word).map((x) => x.line).filter((l) => l.tokens.length >= 2);
  if (!cands.length) return null;
  const l = pick(cands.filter((x) => x.tokens.length <= 14).length ? cands.filter((x) => x.tokens.length <= 14) : cands);
  return { id: sid(), kind: "spot", lineId: l.id, word, item: word };
}

function fill(line: Line, focusKey?: string): Step | null {
  if (line.tokens.length < 2) return null;
  let blank = focusKey ? line.tokens.findIndex((t) => t.key === focusKey) : -1;
  if (blank < 0) blank = Math.floor(Math.random() * line.tokens.length);
  const answer = line.tokens[blank].ar;
  const others = shuffle(
    poolLines.flatMap((l) => l.tokens).filter((t) => t.key !== line.tokens[blank].key && !line.tokens.some((x) => x.ar === t.ar)).map((t) => t.ar),
  );
  const opts = Array.from(new Set(others)).slice(0, 3);
  return { id: sid(), kind: "fill", lineId: line.id, blank, options: shuffle([answer, ...opts]), item: line.tokens[blank].key };
}

function build(line: Line): Step {
  let from = 0, to = line.tokens.length - 1;
  if (line.tokens.length > 7) {
    from = Math.floor(Math.random() * (line.tokens.length - 6));
    to = from + 5;
  }
  const used = new Set(line.tokens.slice(from, to + 1).map((t) => t.en));
  const extras = shuffle(poolLines.flatMap((l) => l.tokens).filter((t) => !used.has(t.en))).slice(0, 2);
  return { id: sid(), kind: "build", lineId: line.id, from, to, extras };
}

function meaningQ(line: Line): Step | null {
  let cands = poolLines.filter((l) => l.id !== line.id && l.en && l.en !== line.en);
  if (cands.length < 2) cands = ALL_LINES.filter((l) => l.id !== line.id && l.en && l.en !== line.en);
  const pool = shuffle(cands).slice(0, 2);
  if (pool.length < 2) return null;
  return { id: sid(), kind: "meaning", lineId: line.id, options: shuffle([line.id, ...pool.map((l) => l.id)]) };
}

function patternQ(pattern: string, preferLines: Line[]): Step | null {
  const toks = (lines: Line[]) => lines.flatMap((l) => l.tokens).filter((t) => t.pats.includes(pattern));
  let cands = toks(preferLines);
  if (!cands.length) cands = toks(ALL_LINES);
  if (!cands.length) return null;
  const token = pick(cands);
  const all = ALL_LINES.flatMap((l) => l.tokens);
  const near = poolLines.flatMap((l) => l.tokens);
  const sameWord = shuffle(all.filter((t) => t.key === token.key && t.en !== token.en && t.ar !== token.ar));
  const samePat = shuffle(near.filter((t) => t.key !== token.key && t.pats.includes(pattern) && t.en !== token.en));
  const rest = shuffle(near.filter((t) => t.key !== token.key && t.en !== token.en));
  const opts: Token[] = [];
  for (const t of [...sameWord, ...samePat, ...rest]) {
    if (opts.length >= 3) break;
    if (!opts.some((o) => o.en === t.en)) opts.push(t);
  }
  return { id: sid(), kind: "patternq", pattern, token, options: shuffle([token, ...opts]), item: "p:" + pattern };
}

// ---------- lesson builders ----------
export function buildLesson(lessonId: string, progress: ProgressData): Step[] {
  const lesson = lessonById(lessonId);
  setPool(lesson.unitIndex);
  const unit = unitById(lesson.unitId);
  return lesson.type === "final" ? finalLesson(unit.id, progress) : learnLesson(lessonId, progress);
}

function learnLesson(lessonId: string, progress: ProgressData): Step[] {
  const lesson = lessonById(lessonId);
  const unit = unitById(lesson.unitId);
  const words = lesson.words;
  const steps: Step[] = [];
  for (let i = 0; i < words.length; i += 2) {
    const pair = words.slice(i, i + 2);
    pair.forEach((w) => steps.push({ id: sid(), kind: "intro", word: w }));
    pair.forEach((w, j) => steps.push(mcq(w, j === 0 ? "ar2mean" : "mean2ar", progress)));
  }
  for (const p of lesson.patterns) {
    steps.push({ id: sid(), kind: "pattern", pattern: p });
    const q = patternQ(p, unit.lines);
    if (q) steps.push(q);
  }
  const practice: Step[] = [];
  shuffle(words).slice(0, 3).forEach((w) => { const s = spot(w, unit.lines); if (s) practice.push(s); });
  const withAudio = words.filter((w) => WORDS[w].audio);
  shuffle(withAudio).slice(0, 2).forEach((w) => practice.push(mcq(w, "listen", progress)));
  const fillLine = unit.lines.find((l) => l.tokens.some((t) => words.includes(t.key)) && l.tokens.length >= 3);
  if (fillLine) {
    const f = fill(fillLine, pick(fillLine.tokens.filter((t) => words.includes(t.key))).key);
    if (f) practice.push(f);
  }
  // older words to keep them fresh
  const older = Object.keys(progress.items).filter((k) => WORDS[k] && !words.includes(k));
  const due = dueItems(progress).filter((k) => WORDS[k] && !words.includes(k));
  const review = Array.from(new Set([...due, ...shuffle(older)])).slice(0, 2);
  review.forEach((w) => practice.push(mcq(w, pick(["ar2mean", "mean2ar"] as const), progress)));
  const matchWords = Array.from(new Set([...words, ...shuffle(older)])).slice(0, 5);
  if (matchWords.length >= 3) practice.push({ id: sid(), kind: "match", words: shuffle(matchWords) });
  return [...steps, ...shuffle(practice)];
}

function finalLesson(unitId: string, progress: ProgressData): Step[] {
  const unit = unitById(unitId);
  const steps: Step[] = [];
  const lines = unit.lines.length > 6 ? shuffle(unit.lines).slice(0, 6) : unit.lines;
  for (const l of lines) steps.push(build(l));
  const meaningLines = shuffle(unit.lines).slice(0, Math.min(3, unit.lines.length));
  meaningLines.forEach((l) => { const m = meaningQ(l); if (m) steps.push(m); });
  const uw = shuffle(unit.newWords);
  if (uw.length >= 3) steps.push({ id: sid(), kind: "match", words: uw.slice(0, 5) });
  uw.slice(5, 7).forEach((w) => { const s = spot(w, unit.lines); if (s) steps.push(s); });
  const fl = pick(unit.lines.filter((l) => l.tokens.length >= 3));
  if (fl) { const f = fill(fl); if (f) steps.push(f); }
  void progress;
  return steps;
}

export function buildPractice(progress: ProgressData, size = 10): Step[] {
  const maxUnit = Math.max(0, ...Object.keys(progress.completed).map((id) => UNITS.findIndex((u) => u.lessons.some((l) => l.id === id))));
  setPool(maxUnit);
  const learned = Object.keys(progress.items).filter((k) => (k.startsWith("p:") ? PATTERNS[k.slice(2)] : WORDS[k]));
  if (!learned.length) return [];
  const due = dueItems(progress).filter((k) => learned.includes(k));
  const weakest = [...learned].sort((a, b) => progress.items[a].interval - progress.items[b].interval || progress.items[a].due - progress.items[b].due);
  const chosen = Array.from(new Set([...due, ...weakest])).slice(0, size);
  const steps: Step[] = [];
  for (const id of shuffle(chosen)) {
    if (id.startsWith("p:")) {
      const q = patternQ(id.slice(2), ALL_LINES);
      if (q) steps.push(q);
      continue;
    }
    const modes: string[] = ["ar2mean", "mean2ar", "spot"];
    if (WORDS[id].audio) modes.push("listen");
    const m = pick(modes);
    if (m === "spot") {
      const s = spot(id);
      steps.push(s ?? mcq(id, "ar2mean", progress));
    } else steps.push(mcq(id, m as "ar2mean", progress));
  }
  const wordsOnly = chosen.filter((k) => !k.startsWith("p:"));
  if (wordsOnly.length >= 4) steps.splice(Math.floor(steps.length / 2), 0, { id: sid(), kind: "match", words: shuffle(wordsOnly).slice(0, 5) });
  return steps;
}
