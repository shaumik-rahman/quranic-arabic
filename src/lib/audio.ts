"use client";
import { verseAudioUrl, wordAudioUrl } from "./course";
import { useProgress } from "./store";

let el: HTMLAudioElement | null = null;
let queue: string[] = [];
let ctx: AudioContext | null = null;

function player() {
  if (!el && typeof window !== "undefined") {
    el = new Audio();
    el.preload = "auto";
    el.addEventListener("ended", () => {
      const next = queue.shift();
      if (next && el) { el.src = next; el.play().catch(() => {}); }
    });
  }
  return el;
}

export function playUrls(urls: string[]) {
  const p = player();
  if (!p || !urls.length) return;
  queue = urls.slice(1);
  p.pause();
  p.src = urls[0];
  p.currentTime = 0;
  p.play().catch(() => {});
}
export const playWord = (id: string | null | undefined) => id && playUrls([wordAudioUrl(id)]);
export const playVerse = (id: string) => playUrls([verseAudioUrl(id)]);
export const playWordSequence = (ids: (string | null)[]) =>
  playUrls(ids.filter((x): x is string => !!x).map(wordAudioUrl));
export function stopAudio() { queue = []; el?.pause(); }

/** Tiny synthesized feedback sounds (no files needed). */
export function sfx(kind: "correct" | "wrong" | "complete") {
  if (typeof window === "undefined" || !useProgress.getState().settings.sound) return;
  try {
    ctx = ctx || new (window.AudioContext || (window as unknown as { webkitAudioContext: typeof AudioContext }).webkitAudioContext)();
    const notes = kind === "correct" ? [660, 880] : kind === "wrong" ? [220, 180] : [523, 659, 784, 1046];
    notes.forEach((f, i) => {
      const o = ctx!.createOscillator();
      const g = ctx!.createGain();
      o.type = kind === "wrong" ? "sawtooth" : "sine";
      o.frequency.value = f;
      const t0 = ctx!.currentTime + i * 0.09;
      g.gain.setValueAtTime(0.0001, t0);
      g.gain.exponentialRampToValueAtTime(kind === "wrong" ? 0.05 : 0.12, t0 + 0.02);
      g.gain.exponentialRampToValueAtTime(0.0001, t0 + 0.18);
      o.connect(g).connect(ctx!.destination);
      o.start(t0);
      o.stop(t0 + 0.2);
    });
  } catch {}
}
