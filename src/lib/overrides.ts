"use client";
/**
 * Content edits made by the superadmin in the app (stored in Supabase `content_overrides`).
 * They are applied on top of the built-in course data, so a fix shows up for everyone without a new release.
 *
 * A path is a JSON array saying what to change:
 *   ["word", key, field]                 field: en | bn | tip | emoji | cog.en | cog.bn | cog.hi
 *   ["pattern", id, field]               en | bn | expl_en | expl_bn
 *   ["struct", id, field]                en | bn | expl_en | expl_bn
 *   ["page", ref, i, field]              t_en | t_bn | x_en | x_bn          (ref = "p:al" or "s:is")
 *   ["pageex", ref, i, "ex"|"vs", j, en|bn]
 *   ["check", ref, n, field]             q_en | q_bn | why_en | why_bn
 *   ["checkopt", ref, n, j, en|bn]
 *   ["root", root, field]                idea_en | idea_bn | story_en | story_bn
 *   ["line", lineId, en|bn]              a sentence's translation (every copy of that line)
 *   ["tok", lineId, i, en|bn]            one word's meaning inside a line
 */
import { create } from "zustand";
import { course, PATTERNS, ROOTS, STRUCTURES, WORDS, teachOf, type Line } from "./course";
import { supabase } from "./supabase";

export type Path = (string | number)[];
const CACHE = "qa-overrides-v1";

// every line object in the course, by id (the same sentence can appear in several places)
let lineIndex: Map<string, Line[]> | null = null;
function linesById() {
  if (lineIndex) return lineIndex;
  lineIndex = new Map();
  const seen = new Set<object>();
  const walk = (o: unknown) => {
    if (!o || typeof o !== "object" || seen.has(o)) return;
    seen.add(o);
    if (Array.isArray(o)) { o.forEach(walk); return; }
    const r = o as Record<string, unknown>;
    if (typeof r.id === "string" && Array.isArray(r.tokens)) {
      const list = lineIndex!.get(r.id) ?? [];
      list.push(r as unknown as Line);
      lineIndex!.set(r.id, list);
    }
    Object.values(r).forEach(walk);
  };
  walk(course);
  return lineIndex;
}

/** the objects a path points into, and the final field name */
function targets(path: Path): [Record<string, unknown>[], string] {
  const [kind, a, b, c, d, e] = path as [string, string, number | string, number | string, number | string, string];
  const one = (o: unknown) => (o ? [o as Record<string, unknown>] : []);
  switch (kind) {
    case "word": {
      const w = WORDS[a];
      if (String(b).startsWith("cog.")) return [one(w?.cog), String(b).slice(4)];
      return [one(w), String(b)];
    }
    case "pattern": return [one(PATTERNS[a]), String(b)];
    case "struct": return [one(STRUCTURES[a]), String(b)];
    case "root": return [one(ROOTS[a]), String(b)];
    case "page": return [one(teachOf(a).pages[Number(b)]), String(c)];
    case "pageex": {
      const pg = teachOf(a).pages[Number(b)] as unknown as Record<string, Record<string, unknown>[]> | undefined;
      return [one(pg?.[String(c)]?.[Number(d)]), e];
    }
    case "check": return [one(teachOf(a).checks[Number(b)]), String(c)];
    case "checkopt": return [one(teachOf(a).checks[Number(b)]?.options[Number(c)]), String(d)];
    case "line": return [(linesById().get(a) ?? []) as unknown as Record<string, unknown>[], String(b)];
    case "tok": return [(linesById().get(a) ?? []).map((l) => l.tokens[Number(b)]).filter(Boolean) as unknown as Record<string, unknown>[], String(c)];
  }
  return [[], ""];
}

const originals = new Map<string, string>();
export function getValue(path: Path): string {
  const [objs, f] = targets(path);
  const v = objs[0]?.[f];
  return typeof v === "string" ? v : "";
}
/** the built-in text, before any edit */
export function originalValue(path: Path): string {
  return originals.get(JSON.stringify(path)) ?? getValue(path);
}
function apply(path: Path, value: string) {
  const k = JSON.stringify(path);
  if (!originals.has(k)) originals.set(k, getValue(path));
  const [objs, f] = targets(path);
  objs.forEach((o) => (o[f] = value));
}
function restore(path: Path) {
  const k = JSON.stringify(path);
  if (originals.has(k)) { const [objs, f] = targets(path); objs.forEach((o) => (o[f] = originals.get(k))); }
}

/** bumping `version` re-renders the app after edits arrive */
export const useContent = create<{ version: number; remount: number; edits: Record<string, string> }>(() => ({ version: 0, remount: 0, edits: {} }));

/** remount=true re-renders the whole app (used when edits arrive from the server, not for the editor's own saves) */
function setEdits(edits: Record<string, string>, remount = false) {
  // undo edits that disappeared, apply the current ones
  for (const k of Object.keys(useContent.getState().edits)) if (!(k in edits)) restore(JSON.parse(k));
  for (const [k, v] of Object.entries(edits)) { try { apply(JSON.parse(k), v); } catch { /* path no longer exists */ } }
  try { localStorage.setItem(CACHE, JSON.stringify(edits)); } catch { /* private mode */ }
  useContent.setState((s) => ({ version: s.version + 1, remount: s.remount + (remount ? 1 : 0), edits }));
}

/** apply cached edits at once, then fetch the latest */
export async function loadOverrides() {
  try {
    const cached = JSON.parse(localStorage.getItem(CACHE) || "{}");
    if (Object.keys(cached).length) setEdits(cached, true);
  } catch { /* ignore */ }
  if (!supabase) return;
  const { data, error } = await supabase.from("content_overrides").select("path, value");
  if (error || !data) return;
  const edits: Record<string, string> = {};
  for (const r of data as { path: string; value: string }[]) edits[r.path] = r.value;
  if (JSON.stringify(edits) !== JSON.stringify(useContent.getState().edits)) setEdits(edits, true);
}

export async function saveOverride(path: Path, value: string): Promise<string | null> {
  if (!supabase) return "Supabase is not connected.";
  const k = JSON.stringify(path);
  const orig = originalValue(path);
  if (value === orig) return revertOverride(path);
  const { data: u } = await supabase.auth.getUser();
  const { error } = await supabase.from("content_overrides").upsert({ path: k, value, updated_by: u.user?.id, updated_at: new Date().toISOString() });
  if (error) return error.message;
  setEdits({ ...useContent.getState().edits, [k]: value });
  return null;
}

export async function revertOverride(path: Path): Promise<string | null> {
  if (!supabase) return "Supabase is not connected.";
  const k = JSON.stringify(path);
  const { error } = await supabase.from("content_overrides").delete().eq("path", k);
  if (error) return error.message;
  const edits = { ...useContent.getState().edits };
  delete edits[k];
  setEdits(edits);
  return null;
}
