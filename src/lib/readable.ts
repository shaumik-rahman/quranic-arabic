"use client";
import { useEffect, useMemo, useState } from "react";
import { useProgress } from "./store";

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
    return { count: list.length, total: data.verses.length, list };
  }, [data, items]);
}
