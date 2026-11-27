"use client";
import { useMemo } from "react";
import { SALAH } from "./course";
import { useProgress } from "./store";

/** The whole prayer in order, lighting up as the learner learns its words. */
export function useSalahUnderstanding() {
  const items = useProgress((s) => s.items);
  return useMemo(() => {
    const parts = SALAH.map((g) => {
      const toks = g.lines.flatMap((l) => l.tokens);
      const known = toks.filter((t) => items[t.key]).length;
      return { g, known, total: toks.length, pct: (100 * known) / Math.max(1, toks.length) };
    });
    const known = parts.reduce((a, p) => a + p.known, 0), total = parts.reduce((a, p) => a + p.total, 0);
    return { parts, known, total, pct: (100 * known) / Math.max(1, total) };
  }, [items]);
}

