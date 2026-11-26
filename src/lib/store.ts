"use client";
import { create } from "zustand";
import { persist } from "zustand/middleware";
import { grade, newItem, type ItemState } from "./srs";
import type { Lang } from "./course";

export const MAX_HEARTS = 5;
export const HEART_REFILL_MS = 3 * 60 * 60 * 1000; // one heart every 3 hours

export interface Settings {
  lang: Lang;
  translit: boolean;
  dailyGoal: number;
  sound: boolean;
  leaderboard: boolean;
  displayName: string;
}

export interface ProgressData {
  v: 1;
  userId: string | null;
  updatedAt: number;
  xp: number;
  xpByDay: Record<string, number>;
  streak: number;
  longestStreak: number;
  lastActiveDay: string | null;
  hearts: number;
  heartsUpdatedAt: number;
  completed: Record<string, { at: number; perfect: boolean }>;
  items: Record<string, ItemState>; // word keys, and "p:<pattern>" for patterns
  settings: Settings;
}

export const dayKey = (d = new Date()) =>
  `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`;
const yesterdayKey = () => dayKey(new Date(Date.now() - 86_400_000));

export const emptyProgress = (userId: string | null = null): ProgressData => ({
  v: 1,
  userId,
  updatedAt: 0,
  xp: 0,
  xpByDay: {},
  streak: 0,
  longestStreak: 0,
  lastActiveDay: null,
  hearts: MAX_HEARTS,
  heartsUpdatedAt: Date.now(),
  completed: {},
  items: {},
  settings: { lang: "en", translit: false, dailyGoal: 20, sound: true, leaderboard: false, displayName: "" },
});

interface Actions {
  setSettings: (s: Partial<Settings>) => void;
  refillHearts: () => void;
  loseHeart: () => void;
  gainHearts: (n: number) => void;
  addXp: (n: number) => void;
  learn: (ids: string[]) => void;
  answer: (id: string, correct: boolean) => void;
  completeLesson: (id: string, perfect: boolean) => void;
  replaceAll: (p: ProgressData) => void;
  resetFor: (userId: string | null) => void;
}

export const useProgress = create<ProgressData & Actions>()(
  persist(
    (set, get) => {
      const touch = (patch: Partial<ProgressData>) => set({ ...patch, updatedAt: Date.now() });
      return {
        ...emptyProgress(),
        setSettings: (s) => touch({ settings: { ...get().settings, ...s } }),
        refillHearts: () => {
          const { hearts, heartsUpdatedAt } = get();
          if (hearts >= MAX_HEARTS) {
            if (Date.now() - heartsUpdatedAt > HEART_REFILL_MS) set({ heartsUpdatedAt: Date.now() });
            return;
          }
          const gained = Math.floor((Date.now() - heartsUpdatedAt) / HEART_REFILL_MS);
          if (gained > 0) {
            const h = Math.min(MAX_HEARTS, hearts + gained);
            touch({ hearts: h, heartsUpdatedAt: h >= MAX_HEARTS ? Date.now() : heartsUpdatedAt + gained * HEART_REFILL_MS });
          }
        },
        loseHeart: () => {
          const { hearts, heartsUpdatedAt } = get();
          touch({ hearts: Math.max(0, hearts - 1), heartsUpdatedAt: hearts >= MAX_HEARTS ? Date.now() : heartsUpdatedAt });
        },
        gainHearts: (n) => touch({ hearts: Math.min(MAX_HEARTS, get().hearts + n) }),
        addXp: (n) => {
          const today = dayKey();
          const s = get();
          let streak = s.streak;
          if (s.lastActiveDay !== today) streak = s.lastActiveDay === yesterdayKey() ? s.streak + 1 : 1;
          touch({
            xp: s.xp + n,
            xpByDay: { ...s.xpByDay, [today]: (s.xpByDay[today] || 0) + n },
            streak,
            longestStreak: Math.max(s.longestStreak, streak),
            lastActiveDay: today,
          });
        },
        learn: (ids) => {
          const items = { ...get().items };
          let changed = false;
          for (const id of ids) if (!items[id]) { items[id] = newItem(); changed = true; }
          if (changed) touch({ items });
        },
        answer: (id, correct) => {
          const cur = get().items[id];
          if (!cur) return;
          touch({ items: { ...get().items, [id]: grade(cur, correct) } });
        },
        completeLesson: (id, perfect) => {
          const prev = get().completed[id];
          touch({ completed: { ...get().completed, [id]: { at: Date.now(), perfect: perfect || !!prev?.perfect } } });
        },
        replaceAll: (p) => set({ ...p }),
        resetFor: (userId) => set({ ...emptyProgress(userId), updatedAt: 0 }),
      };
    },
    {
      name: "qa-progress-v1",
      partialize: (s) => {
        // eslint-disable-next-line @typescript-eslint/no-unused-vars
        const { setSettings, refillHearts, loseHeart, gainHearts, addXp, learn, answer, completeLesson, replaceAll, resetFor, ...data } = s;
        return data;
      },
    },
  ),
);

export function snapshot(): ProgressData {
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const { setSettings, refillHearts, loseHeart, gainHearts, addXp, learn, answer, completeLesson, replaceAll, resetFor, ...data } =
    useProgress.getState();
  return data;
}
