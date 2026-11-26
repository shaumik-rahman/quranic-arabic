import { ALL_LINES, PATTERNS, STRUCTURES, UNITS, teachOf, WORDS, WORD_ORDER, linesWithWord, lessonById, unitById, type Line, type Token, type Word } from "./course";
import type { ProgressData } from "./store";
import { dueItems } from "./stats";

export type Exercise =
  | { kind: "intro"; word: string }
  | { kind: "pattern"; pattern: string }
  | { kind: "mcq"; mode: "ar2mean" | "mean2ar"; word: string; options: string[] }
  | { kind: "patternq"; pattern: string; token: Token; options: Token[] }
  | { kind: "spot"; lineId: string; word: string }
  | { kind: "fill"; lineId: string; blank: number; options: string[] }
  | { kind: "match"; words: string[] }
  | { kind: "build"; lineId: string; from: number; to: number; extras: Token[] }
  | { kind: "meaning"; lineId: string; options: string[] }
  | { kind: "structure"; structure: string }
  | { kind: "breakdown"; structure: string; lineIds: string[] }
  | { kind: "arrange"; lineId: string; extras: string[] }
  | { kind: "read"; lineId: string; highlight?: string[]; title?: "verse" | "chunk" }
  | { kind: "check"; ref: string; n: number; order: number[] };

export type Step = Exercise & { id: string; item?: string };

/** Lines from the first `n` units (what the learner has met so far). */
let poolLines: Line[] = ALL_LINES;
function setPool(unitIndex: number | null) {
  if (unitIndex === null) { poolLines = ALL_LINES; return; }
  const seen = new Set<string>();
  poolLines = [];
  for (const u of UNITS.slice(0, Math.max(unitIndex + 1, 2))) {
    for (const l of [...u.lines, ...(u.structures || []).flatMap((s) => s.everyday)]) if (!seen.has(l.id)) { seen.add(l.id); poolLines.push(l); }
  }
}

export const isGraded = (e: Exercise) => !["intro", "pattern", "structure", "read", "breakdown"].includes(e.kind);

// ---------- helpers ----------
const LINE_MAP: Record<string, Line> = {};
for (const u of UNITS) {
  for (const l of u.lines) LINE_MAP[l.id] = l;
  for (const l of u.newVerses || []) LINE_MAP[l.id] = l;
  for (const s of u.structures || []) {
    for (const l of [...s.quran, ...s.everyday, ...(s.chunkVerses || [])]) LINE_MAP[l.id] = l;
    if (s.chunk) LINE_MAP[s.chunk.id] = s.chunk;
  }
}
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

// ---------- similarity: what makes a good wrong answer ----------
const skeleton = (s: string) => s.split(" / ")[0].replace(/[^ء-يٱی]/g, "").replace(/^[اٱ]ل/, "").replace(/[أإآٱ]/g, "ا").replace(/ى/g, "ي");
function bigrams(s: string) { const o = new Set<string>(); for (let i = 0; i < s.length - 1; i++) o.add(s.slice(i, i + 2)); return o; }
function overlap(a: Set<string>, b: Set<string>) { let n = 0; a.forEach((x) => b.has(x) && n++); return n / Math.max(1, Math.min(a.size, b.size)); }
const mainWord = (en: string) => en.toLowerCase().replace(/\(.*?\)|the |a |an /g, "").split(/[,;/]/)[0].trim();

/** Higher = more tempting (same kind of word, shared root letters, looks alike) but still clearly different. */
function wordSimilarity(t: Word, o: Word) {
  let s = 0;
  if (t.pos === o.pos) s += 4;
  else if (["noun", "adj", "name"].includes(t.pos) && ["noun", "adj", "name"].includes(o.pos)) s += 2;
  if (t.root && o.root) s += 1.5 * [...t.root].filter((c) => o.root.includes(c)).length;
  s += 3 * overlap(bigrams(skeleton(t.ar)), bigrams(skeleton(o.ar)));
  if (t.emoji && o.emoji && t.emoji === o.emoji) s -= 10;
  return s;
}
function tooClose(t: Word, o: Word) {
  return o.key === t.key || o.en === t.en || o.ar === t.ar || mainWord(o.en) === mainWord(t.en) || o.bn === t.bn;
}

/** Candidate words the learner could plausibly know by now. */
function knownPool(target: string, progress: ProgressData | null) {
  const idx = WORD_ORDER.indexOf(target);
  const near = WORD_ORDER.slice(0, Math.max(idx + 4, 10));
  const known = progress ? Object.keys(progress.items).filter((k) => WORDS[k]) : [];
  return Array.from(new Set([...near, ...known]));
}
function rankPick<T>(items: T[], score: (x: T) => number, n: number, spread = 2): T[] {
  // take the most tempting few, with a little randomness so lessons don't repeat exactly
  const ranked = items.map((x) => ({ x, s: score(x) + Math.random() * 1.5 })).sort((a, b) => b.s - a.s);
  return shuffle(ranked.slice(0, n + spread)).sort((a, b) => b.s - a.s).slice(0, n).map((r) => r.x);
}
function wordOptions(target: string, progress: ProgressData | null, n = 4) {
  const tw = WORDS[target];
  const pool = knownPool(target, progress).map((k) => WORDS[k]).filter((o) => o && !tooClose(tw, o));
  const chosen = rankPick(pool, (o) => wordSimilarity(tw, o), n - 1);
  return shuffle([target, ...chosen.map((o) => o.key)]);
}

function mcq(word: string, mode: "ar2mean" | "mean2ar", progress: ProgressData | null): Step {
  return { id: sid(), kind: "mcq", mode, word, options: wordOptions(word, progress), item: word };
}

function spot(word: string, preferLines?: Line[]): Step | null {
  const inPref = (preferLines || []).filter((l) => l.tokens.some((t) => t.key === word) && l.tokens.length >= 2);
  const cands = inPref.length ? inPref : linesWithWord(word).map((x) => x.line).filter((l) => l.tokens.length >= 2);
  if (!cands.length) return null;
  const short = cands.filter((x) => x.tokens.length <= 14);
  const l = pick(short.length ? short : cands);
  return { id: sid(), kind: "spot", lineId: l.id, word, item: word };
}

const posOf = (t: Token) => WORDS[t.key]?.pos ?? "noun";
const hasAl = (t: Token) => t.pats.includes("al");

/** Fill the blank: wrong options are the same kind of word, with the same ٱلۡـ / ending, so you must know the meaning. */
function fill(line: Line, focusKey?: string): Step | null {
  if (line.tokens.length < 2) return null;
  let blank = focusKey ? line.tokens.findIndex((t) => t.key === focusKey) : -1;
  if (blank < 0) blank = Math.floor(Math.random() * line.tokens.length);
  const target = line.tokens[blank];
  const inLine = new Set(line.tokens.map((t) => t.ar));
  const cands = new Map<string, Token>();
  for (const t of [...poolLines, ...ALL_LINES].flatMap((l) => l.tokens)) {
    if (t.key === target.key || inLine.has(t.ar) || cands.has(t.ar)) continue;
    cands.set(t.ar, t);
  }
  const lastMark = (s: string) => s.replace(/[ۖ-ۭ]/g, "").slice(-1);
  const score = (t: Token) =>
    (posOf(t) === posOf(target) ? 4 : 0) + (hasAl(t) === hasAl(target) ? 2 : 0) + (lastMark(t.ar) === lastMark(target.ar) ? 1 : 0) +
    (poolLines.some((l) => l.tokens.includes(t)) ? 1.5 : 0) + (t.pats.join() === target.pats.join() ? 1 : 0);
  const opts = rankPick([...cands.values()], score, 3, 3).map((t) => t.ar);
  return { id: sid(), kind: "fill", lineId: line.id, blank, options: shuffle([target.ar, ...opts]), item: target.key };
}

/** Extra meaning tiles: other forms of the same words ("my Lord" vs "our Lord"), then same kind of word. */
function buildExtras(seg: Token[]): Token[] {
  const used = new Set(seg.map((t) => t.en));
  const keys = new Set(seg.map((t) => t.key));
  const all = [...poolLines, ...ALL_LINES].flatMap((l) => l.tokens).filter((t) => !used.has(t.en));
  const uniq = new Map<string, Token>();
  all.forEach((t) => uniq.has(t.en) || uniq.set(t.en, t));
  const segPos = new Set(seg.map(posOf));
  return rankPick([...uniq.values()], (t) => (keys.has(t.key) ? 6 : 0) + (segPos.has(posOf(t)) ? 2 : 0) + (poolLines.some((l) => l.tokens.includes(t)) ? 1 : 0), 2, 3);
}

function build(line: Line): Step {
  let from = 0, to = line.tokens.length - 1;
  if (line.tokens.length > 7) {
    from = Math.floor(Math.random() * (line.tokens.length - 6));
    to = from + 5;
  }
  return { id: sid(), kind: "build", lineId: line.id, from, to, extras: buildExtras(line.tokens.slice(from, to + 1)) };
}

/** Wrong translations come from lines that share words or the same sentence pattern, so you must read carefully. */
function meaningQ(line: Line): Step | null {
  const keys = new Set(line.tokens.map((t) => t.key));
  const verseOf = (l: Line) => (l.kind === "quran" ? l.id.split(":").slice(0, 2).join(":") : l.id);
  const sameStruct = Object.values(STRUCTURES).find((s) => s.everyday.some((l) => l.id === line.id));
  let cands = [...poolLines, ...ALL_LINES].filter((l, i, a) => a.findIndex((x) => x.id === l.id) === i)
    .filter((l) => l.id !== line.id && l.en && l.en !== line.en && l.bn !== line.bn && verseOf(l) !== verseOf(line));
  if (cands.length < 2) cands = ALL_LINES.filter((l) => l.id !== line.id && l.en && l.en !== line.en);
  const score = (l: Line) => {
    const shared = l.tokens.filter((t) => keys.has(t.key)).length;
    return shared * 2 + (sameStruct && sameStruct.everyday.some((x) => x.id === l.id) ? 3 : 0) + (l.kind === line.kind ? 1 : 0)
      - Math.abs(l.tokens.length - line.tokens.length) * 0.3;
  };
  const opts = rankPick(cands, score, 2, 2);
  if (opts.length < 2) return null;
  return { id: sid(), kind: "meaning", lineId: line.id, options: shuffle([line.id, ...opts.map((l) => l.id)]) };
}

function patternQ(pattern: string, preferLines: Line[]): Step | null {
  const toks = (lines: Line[]) => lines.flatMap((l) => l.tokens).filter((t) => t.pats.includes(pattern));
  let cands = toks(preferLines);
  if (!cands.length) cands = toks(ALL_LINES);
  if (!cands.length) return null;
  const token = pick(cands);
  const all = ALL_LINES.flatMap((l) => l.tokens);
  const near = poolLines.flatMap((l) => l.tokens);
  // best traps: the same word with a different piece (رَبِّ / رَبَّنَا / رَبِّكَ), then other words with this piece
  const sameWord = shuffle(all.filter((t) => t.key === token.key && t.en !== token.en && t.ar !== token.ar));
  const samePat = shuffle(near.filter((t) => t.key !== token.key && t.pats.includes(pattern) && t.en !== token.en));
  const samePos = shuffle(near.filter((t) => t.key !== token.key && posOf(t) === posOf(token) && t.en !== token.en));
  const opts: Token[] = [];
  for (const t of [...sameWord, ...samePos, ...samePat]) {
    if (opts.length >= 3) break;
    if (!opts.some((o) => o.en === t.en)) opts.push(t);
  }
  return { id: sid(), kind: "patternq", pattern, token, options: shuffle([token, ...opts]), item: "p:" + pattern };
}

/** Arrange tiles: extra tiles are look-alike words from the same pattern's sentences (هَٰذَا / ذَٰلِكَ, قَلَمٌ / كِتَابٌ). */
function arrange(line: Line): Step {
  const own = new Set(line.tokens.map((t) => t.ar));
  const st = Object.values(STRUCTURES).find((s) => s.everyday.some((l) => l.id === line.id));
  const sibling = (st?.everyday || []).filter((l) => l.id !== line.id).flatMap((l) => l.tokens);
  const linePos = new Set(line.tokens.map(posOf));
  const cands = new Map<string, Token>();
  [...sibling, ...poolLines.flatMap((l) => l.tokens)].forEach((t) => { if (!own.has(t.ar) && !cands.has(t.ar) && t.ar.length < 16) cands.set(t.ar, t); });
  const extras = rankPick([...cands.values()], (t) => (sibling.includes(t) ? 3 : 0) + (linePos.has(posOf(t)) ? 2 : 0), 2, 2).map((t) => t.ar);
  return { id: sid(), kind: "arrange", lineId: line.id, extras };
}

/** A written question that tests the idea just taught ("p:un", "s:of"). */
function checkStep(ref: string, n: number): Step | null {
  const c = teachOf(ref).checks[n];
  if (!c) return null;
  return { id: sid(), kind: "check", ref, n, order: shuffle(c.options.map((_, i) => i)), item: ref.startsWith("p:") ? ref : undefined };
}
const allChecks = (ref: string) => teachOf(ref).checks.map((_, n) => checkStep(ref, n)).filter((s): s is Step => !!s);

// ---------- lesson builders ----------
export function buildLesson(lessonId: string, progress: ProgressData): Step[] {
  const lesson = lessonById(lessonId);
  setPool(lesson.unitIndex);
  const unit = unitById(lesson.unitId);
  if (lesson.type === "structure") return structureLesson(lessonId, progress);
  if (lesson.type === "verses") return versesLesson(unit.id);
  return lesson.type === "final" ? finalLesson(unit.id) : learnLesson(lessonId, progress);
}

function introduce(words: string[], patterns: string[], lines: Line[], progress: ProgressData): Step[] {
  const steps: Step[] = [];
  for (let i = 0; i < words.length; i += 2) {
    const pair = words.slice(i, i + 2);
    pair.forEach((w) => steps.push({ id: sid(), kind: "intro", word: w }));
    pair.forEach((w, j) => steps.push(mcq(w, j === 0 ? "ar2mean" : "mean2ar", progress)));
  }
  for (const p of patterns) {
    steps.push({ id: sid(), kind: "pattern", pattern: p });
    steps.push(...allChecks("p:" + p));
    const q = patternQ(p, lines);
    if (q) steps.push(q);
  }
  return steps;
}

function learnLesson(lessonId: string, progress: ProgressData): Step[] {
  const lesson = lessonById(lessonId);
  const unit = unitById(lesson.unitId);
  const words = lesson.words;
  const steps = introduce(words, lesson.patterns, unit.lines, progress);
  const practice: Step[] = [];
  shuffle(words).slice(0, 3).forEach((w) => { const s = spot(w, unit.lines); if (s) practice.push(s); });
  shuffle(words).slice(0, 2).forEach((w) => practice.push(mcq(w, pick(["ar2mean", "mean2ar"] as const), progress)));
  const fillLine = unit.lines.find((l) => l.tokens.some((t) => words.includes(t.key)) && l.tokens.length >= 3);
  if (fillLine) {
    const f = fill(fillLine, pick(fillLine.tokens.filter((t) => words.includes(t.key))).key);
    if (f) practice.push(f);
  }
  const older = Object.keys(progress.items).filter((k) => WORDS[k] && !words.includes(k));
  const due = dueItems(progress).filter((k) => WORDS[k] && !words.includes(k));
  Array.from(new Set([...due, ...shuffle(older)])).slice(0, 2).forEach((w) => practice.push(mcq(w, pick(["ar2mean", "mean2ar"] as const), progress)));
  const matchWords = Array.from(new Set([...words, ...shuffle(older)])).slice(0, 5);
  if (matchWords.length >= 3) practice.push({ id: sid(), kind: "match", words: shuffle(matchWords) });
  return [...steps, ...shuffle(practice)];
}

function finalLesson(unitId: string): Step[] {
  const unit = unitById(unitId);
  const steps: Step[] = [];
  const lines = unit.lines.length > 6 ? shuffle(unit.lines).slice(0, 6) : unit.lines;
  for (const l of lines) steps.push(build(l));
  shuffle(unit.lines).slice(0, Math.min(3, unit.lines.length)).forEach((l) => { const m = meaningQ(l); if (m) steps.push(m); });
  const uw = shuffle(unit.newWords);
  if (uw.length >= 3) steps.push({ id: sid(), kind: "match", words: uw.slice(0, 5) });
  uw.slice(5, 7).forEach((w) => { const s = spot(w, unit.lines); if (s) steps.push(s); });
  const fl = pick(unit.lines.filter((l) => l.tokens.length >= 3));
  if (fl) { const f = fill(fl); if (f) steps.push(f); }
  return steps;
}

function structureLesson(lessonId: string, progress: ProgressData): Step[] {
  const lesson = lessonById(lessonId);
  const st = STRUCTURES[lesson.structure!];
  const part = lesson.part ?? 1;
  const words = lesson.words;
  const steps = introduce(words, lesson.patterns, [...st.everyday, ...poolLines], progress);

  // sentences the learner can build now (words known or introduced in this lesson)
  const later = new Set(
    (lesson.parts ?? 1) > part
      ? UNITS.flatMap((u) => u.lessons).filter((l) => l.structure === st.id && (l.part ?? 1) > part).flatMap((l) => l.words)
      : [],
  );
  const ready = st.everyday.filter((l) => l.tokens.every((t) => !later.has(t.key)));
  const withNew = ready.filter((l) => l.tokens.some((t) => words.includes(t.key)));
  const sentences = [...withNew, ...shuffle(ready.filter((l) => !withNew.includes(l)))].slice(0, 5);

  if (part === 1) {
    steps.push({ id: sid(), kind: "structure", structure: st.id });
    const shown = [...sentences.slice(0, 2).map((l) => l.id), st.quran[0].id];
    steps.push({ id: sid(), kind: "breakdown", structure: st.id, lineIds: shown });
    steps.push(...allChecks("s:" + st.id));
  } else if (sentences.length) {
    steps.push({ id: sid(), kind: "breakdown", structure: st.id, lineIds: sentences.slice(0, 2).map((l) => l.id) });
  }

  const practice: Step[] = [];
  sentences.forEach((l, i) => practice.push(i % 2 === 0 ? arrange(l) : build(l)));
  sentences.slice(0, 2).forEach((l) => { const m = meaningQ(l); if (m) practice.push(m); });
  const ql = st.quran[part === 1 ? 0 : st.quran.length - 1];
  const m = ql && meaningQ(ql);
  if (m) practice.splice(1, 0, m);
  const fl = sentences.find((l) => l.tokens.length >= 2);
  if (fl) { const f = fill(fl); if (f) practice.push(f); }
  if (st.chunk && part === 1) {
    const ck = st.chunk.tokens.map((t) => t.key);
    for (const v of (st.chunkVerses || []).slice(0, 2)) {
      practice.push({ id: sid(), kind: "read", lineId: v.id, highlight: ck, title: "chunk" });
      const mq = meaningQ(v);
      if (mq) practice.push(mq);
    }
  }
  const matchWords = Array.from(new Set([...words, ...sentences.flatMap((l) => l.tokens.map((t) => t.key))])).filter((k) => WORDS[k]).slice(0, 5);
  if (matchWords.length >= 3) practice.push({ id: sid(), kind: "match", words: shuffle(matchWords) });
  return [...steps, ...practice];
}

function versesLesson(unitId: string): Step[] {
  const u = unitById(unitId);
  const steps: Step[] = [];
  for (const v of u.newVerses) {
    steps.push({ id: sid(), kind: "read", lineId: v.id, title: "verse" });
    const m = meaningQ(v);
    if (m) steps.push(m);
    const known = v.tokens.filter((t) => WORDS[t.key] && t.known);
    if (known.length) { const sp = spot(pick(known).key, [v]); if (sp) steps.push(sp); }
  }
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
      // review a grammar idea: its own written question or a word that uses it
      const n = teachOf(id).checks.length;
      const q = n && (Math.random() < 0.5 || !PATTERNS[id.slice(2)].examples.length) ? checkStep(id, Math.floor(Math.random() * n)) : patternQ(id.slice(2), poolLines);
      if (q) steps.push(q);
      continue;
    }
    const m = pick(["ar2mean", "mean2ar", "spot"]);
    if (m === "spot") steps.push(spot(id) ?? mcq(id, "ar2mean", progress));
    else steps.push(mcq(id, m as "ar2mean", progress));
  }
  const wordsOnly = chosen.filter((k) => !k.startsWith("p:"));
  if (wordsOnly.length >= 4) steps.splice(Math.floor(steps.length / 2), 0, { id: sid(), kind: "match", words: shuffle(wordsOnly).slice(0, 5) });
  // practise a sentence too, once the learner has built some
  const sentences = Object.values(STRUCTURES).flatMap((s) => s.everyday).filter((l) => l.tokens.every((t) => progress.items[t.key]));
  if (sentences.length) steps.push(arrange(pick(sentences)));
  return steps;
}
