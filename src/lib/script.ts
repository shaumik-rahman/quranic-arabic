"use client";
import courseJson from "@/data/course.json";
import { useProgress } from "./store";

/** Quran script: IndoPak (Nastaleeq, as printed in South Asia) or Uthmani (Madinah). */
export type Script = "indopak" | "uthmani";

const IP: Record<string, string> = (courseJson as unknown as { ip: Record<string, string> }).ip || {};
const RUN = /[؀-ۿݐ-ݿࢠ-ࣿ]+/g;
const strip = (s: string) => s.split(" ")[0]; // drop pause / verse-end marks that follow a word

/** Convert any Uthmani string the app shows (teaching forms, options, inline examples) to the chosen script. */
const MARKS = /[\u06D6-\u06ED\uF500-\uF5FF]/g;
const tidy = (s: string) => s.replace(MARKS, "").replace(/\s+/g, " ").trim();
export function toScript(s: string | null | undefined, script: Script): string {
  if (!s) return s ?? "";
  if (script !== "indopak") return s;
  if (IP[s]) return tidy(IP[s]);
  if (s.includes(" / ")) return s.split(" / ").map((p) => tidy(IP[p.trim()] ?? p)).join(" / ");
  return s.replace(RUN, (m) => (IP[m] ? tidy(strip(IP[m])) : m));
}

export function useScript() {
  const script: Script = useProgress((s) => s.settings.script) ?? "indopak";
  return {
    script,
    /** any Uthmani string -> current script */
    A: (s: string | null | undefined) => toScript(s, script),
    /** a token: uses its own IndoPak text; `clean` drops pause marks (for exercise options) */
    T: (t: { ar: string; ip?: string | null }, clean = false) => {
      if (script === "indopak" && t.ip) return clean ? strip(t.ip) : t.ip;
      return t.ar;
    },
  };
}
