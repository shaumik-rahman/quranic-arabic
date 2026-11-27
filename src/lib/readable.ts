"use client";
import { useEffect, useMemo, useState } from "react";
import { useProgress } from "./store";
import { TEXTS } from "./course";

// verses the course already teaches: the daily verse should show something new
const COURSE_VERSES = new Set(TEXTS.flatMap((t) => t.lines).filter((l) => l.kind === "quran").map((l) => l.id.split(":").slice(0, 2).join(":")));

type VerseLemmas = [number, number, number[]][];
type Lemma = [string, string, string, number];
let cache: Promise<{ verses: VerseLemmas; lemmas: Lemma[] }> | null = null;
function load() {
  if (!cache) {
    cache = Promise.all([
      fetch("/quran/verse-lemmas.json").then((r) => r.json()),
      fetch("/quran/lemmas.json").then((r) => r.json()),
    ]).then(([verses, lemmas]) => ({ verses, lemmas }));
    cache.catch(() => { cache = null; });
  }
  return cache;
}

/** Verses in which the learner knows every word. */
export function useReadableVerses() {
  const items = useProgress((s) => s.items);
  const [data, setData] = useState<{ verses: VerseLemmas; lemmas: Lemma[] } | null>(null);
  useEffect(() => { load().then(setData).catch(() => {}); }, []);
  return useMemo(() => {
    if (!data) return null;
    const known = new Set<number>();
    data.lemmas.forEach((l, i) => { if (items[l[0]]) known.add(i); });
    const list = data.verses.filter(([, , ls]) => ls.every((i) => known.has(i))).map(([s, v]) => [s, v] as [number, number]);
    // nearly there: short verses where only one or two words are new
    const near = data.verses
      .filter(([, , ls]) => ls.length >= 3 && ls.length <= 12 && !ls.every((i) => known.has(i)))
      .map(([s, v, ls]) => ({ s, v, unknown: ls.filter((i) => !known.has(i)).length, n: ls.length }))
      .filter((x) => x.unknown <= 2 && x.unknown / x.n <= 0.3)
      .sort((a, b) => a.unknown - b.unknown || a.s - b.s || a.v - b.v)
      .map(({ s, v }) => [s, v] as [number, number]);
    return { count: list.length, total: data.verses.length, list, near, lemmas: data.lemmas };
  }, [data, items]);
}

/** Verses that read well on their own (duas, reminders, names of Allah), so a verse of the day is never a quote taken out of context. */
const DAILY = (
  "2:21 2:45 2:152 2:153 2:156 2:163 2:186 2:201 2:250 2:127 2:128 3:8 3:9 3:31 3:92 3:139 3:173 3:185 3:190 3:191 3:200 4:28 " +
  "6:162 6:163 7:23 7:205 8:2 9:51 9:129 10:62 11:6 12:86 12:87 13:28 14:7 14:40 14:41 15:9 15:49 16:18 16:97 16:128 17:24 17:80 17:81 " +
  "18:10 20:14 20:25 20:26 20:27 20:28 20:114 21:35 21:107 23:1 23:2 23:97 23:98 23:118 25:74 26:78 26:79 26:80 26:83 28:24 29:69 " +
  "33:41 33:42 33:56 35:15 39:53 40:44 40:60 49:10 49:13 50:16 51:56 55:13 55:26 55:27 55:60 59:18 62:10 64:16 67:1 67:2 70:5 73:8 73:9 " +
  "87:1 87:14 87:15 87:17 89:27 89:28 89:29 89:30 93:3 93:4 93:5 93:11 94:5 94:6 94:7 94:8 95:4 96:1 96:3 96:4 96:5 97:1 97:3 97:5 " +
  "99:7 99:8 109:6 2:255 112:1 112:2 113:1 114:1"
).split(" ");

/** Today's verse: one the learner fully understands if possible, otherwise one where only a few words are new. Changes daily. */
export function useDailyVerse() {
  const items = useProgress((s) => s.items);
  const [data, setData] = useState<{ verses: VerseLemmas; lemmas: Lemma[] } | null>(null);
  useEffect(() => { load().then(setData).catch(() => {}); }, []);
  return useMemo(() => {
    if (!data) return null;
    const byRef = new Map(data.verses.map(([s, v, ls]) => [`${s}:${v}`, ls]));
    const known = new Set<number>();
    data.lemmas.forEach((l, i) => { if (items[l[0]]) known.add(i); });
    const scored = DAILY.filter((r) => byRef.has(r)).map((r) => {
      const ls = byRef.get(r)!;
      return { r, unknown: ls.filter((i) => !known.has(i)).length, fresh: !COURSE_VERSES.has(r) };
    });
    const day = Math.floor((Date.now() - new Date().getTimezoneOffset() * 60000) / 86400000);
    const full = scored.filter((x) => x.unknown === 0);
    const fullFresh = full.filter((x) => x.fresh);
    let pool = fullFresh.length ? fullFresh : full;
    if (!fullFresh.length) {
      // nearly there: the verses with the fewest new words
      const fresh = scored.filter((x) => x.fresh).sort((a, b) => a.unknown - b.unknown);
      const best = fresh[0]?.unknown ?? 99;
      const near = fresh.filter((x) => x.unknown <= Math.max(2, best));
      if (near.length && (!full.length || best <= 2)) pool = near;
    }
    if (!pool.length) return null;
    const pickd = pool[(day * 7919) % pool.length];
    const [s, v] = pickd.r.split(":").map(Number);
    return { s, v, full: pickd.unknown === 0, lemmas: data.lemmas };
  }, [data, items]);
}
