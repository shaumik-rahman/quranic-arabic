/** Simple SM-2–style spaced repetition. Intervals are in days. */
export interface ItemState {
  ease: number;
  interval: number;
  due: number; // ms epoch
  reps: number;
  lapses: number;
  seen: number; // first learned
  last: number;
}

const DAY = 86_400_000;

export function newItem(now = Date.now()): ItemState {
  return { ease: 2.4, interval: 0, due: now + DAY / 2, reps: 0, lapses: 0, seen: now, last: now };
}

export function grade(s: ItemState, correct: boolean, now = Date.now()): ItemState {
  if (correct) {
    const reps = s.reps + 1;
    let interval = reps === 1 ? 1 : reps === 2 ? 3 : Math.round(Math.max(s.interval, 1) * s.ease);
    interval = Math.min(interval, 365);
    return { ...s, reps, interval, ease: Math.min(2.8, s.ease + 0.05), due: now + interval * DAY, last: now };
  }
  return { ...s, reps: 0, interval: 0, lapses: s.lapses + 1, ease: Math.max(1.3, s.ease - 0.2), due: now + 10 * 60_000, last: now };
}

export type Strength = "new" | "learning" | "strong" | "mastered";
export function strength(s?: ItemState): Strength {
  if (!s) return "new";
  if (s.interval >= 21) return "mastered";
  if (s.interval >= 4) return "strong";
  return "learning";
}
export const strengthLevel = (s?: ItemState) => ({ new: 0, learning: 1, strong: 2, mastered: 3 })[strength(s)];
