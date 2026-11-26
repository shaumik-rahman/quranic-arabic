"use client";
import { verseAudioUrl, wordAudioUrl } from "./course";
import { useProgress } from "./store";

let el: HTMLAudioElement | null = null;
let queue: string[] = [];
let ctx: AudioContext | null = null;
let unlocked = false;
let pending: string[] | null = null; // a play that the browser blocked before the first tap

// A tiny silent WAV (50 ms), played on the first tap to "unlock" audio on iPhone/Safari.
const SILENT = "data:audio/wav;base64,UklGRrQBAABXQVZFZm10IBAAAAABAAEAQB8AAEAfAAABAAgAZGF0YZABAACAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA";

function player() {
  if (!el && typeof window !== "undefined") {
    el = new Audio();
    el.preload = "auto";
    el.setAttribute("playsinline", "");
    el.addEventListener("ended", () => {
      const next = queue.shift();
      if (next) start(next);
    });
    el.addEventListener("error", () => {
      console.warn("[audio] could not load", el?.src);
      const next = queue.shift();
      if (next) start(next);
    });
  }
  return el;
}

function start(url: string) {
  const p = player();
  if (!p) return;
  p.src = url;
  const pr = p.play();
  if (pr) pr.catch((err: DOMException) => {
    if (err?.name === "NotAllowedError") pending = [url, ...queue]; // retry on the next tap
    else console.warn("[audio]", err?.name, err?.message);
  });
}

/** Call once: unlocks audio on the first tap anywhere, and plays anything the browser blocked. */
export function initAudioUnlock() {
  if (typeof window === "undefined" || unlocked) return;
  const unlock = () => {
    if (unlocked) return;
    unlocked = true;
    try {
      ctx = ctx || new (window.AudioContext || (window as unknown as { webkitAudioContext: typeof AudioContext }).webkitAudioContext)();
      ctx.resume().catch(() => {});
    } catch {}
    const p = player();
    if (p && !pending && p.paused) {
      p.src = SILENT;
      p.play().catch(() => {});
    }
    if (pending) { const urls = pending; pending = null; playUrls(urls); }
  };
  window.addEventListener("pointerdown", unlock, { capture: true, passive: true });
  window.addEventListener("touchend", unlock, { capture: true, passive: true });
  window.addEventListener("keydown", unlock, { capture: true });
}

export function playUrls(urls: string[]) {
  const p = player();
  if (!p || !urls.length) return;
  queue = urls.slice(1);
  p.pause();
  start(urls[0]);
}
export const playWord = (id: string | null | undefined) => id && playUrls([wordAudioUrl(id)]);
export const playVerse = (id: string) => playUrls([verseAudioUrl(id)]);
export const playWordSequence = (ids: (string | null)[]) =>
  playUrls(ids.filter((x): x is string => !!x).map(wordAudioUrl));
export function stopAudio() { queue = []; pending = null; el?.pause(); }

/** Tiny synthesized feedback sounds (no files needed). */
export function sfx(kind: "correct" | "wrong" | "complete") {
  if (typeof window === "undefined" || !useProgress.getState().settings.sound) return;
  try {
    ctx = ctx || new (window.AudioContext || (window as unknown as { webkitAudioContext: typeof AudioContext }).webkitAudioContext)();
    if (ctx.state === "suspended") ctx.resume().catch(() => {});
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

/** Only complete verses are played (Mishary Alafasy). Word clips were cut from continuous recitation and sounded wrong. */
export const playLine = (line: { verseAudio: string | null }) => { if (line.verseAudio) playVerse(line.verseAudio); };
