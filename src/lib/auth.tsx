"use client";
import { createContext, useCallback, useContext, useEffect, useRef, useState } from "react";
import type { User } from "@supabase/supabase-js";
import { DEMO_MODE, supabase } from "./supabase";
import { snapshot, useProgress, type ProgressData } from "./store";
import { weekStart, weeklyXp } from "./stats";

export type Role = "learner" | "teacher" | "superadmin";
export interface Profile { id: string; email: string; display_name: string | null; role: Role; leaderboard_opt_in: boolean }

interface AuthState {
  status: "loading" | "signedOut" | "signedIn";
  user: { id: string; email: string } | null;
  profile: Profile | null;
  role: Role;
  isTeacher: boolean; // unlocks everything + unlimited hearts
  isAdmin: boolean;
  demo: boolean;
  signOut: () => Promise<void>;
  setDemoRole: (r: Role) => void;
  syncNow: () => Promise<void>;
  syncState: "idle" | "saving" | "saved" | "error";
}

const Ctx = createContext<AuthState | null>(null);
export const useAuth = () => useContext(Ctx)!;

const DEMO_ROLE_KEY = "qa-demo-role";

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [status, setStatus] = useState<AuthState["status"]>("loading");
  const [user, setUser] = useState<AuthState["user"]>(null);
  const [profile, setProfile] = useState<Profile | null>(null);
  const [demoRole, setDemoRoleState] = useState<Role>("learner");
  const [syncState, setSyncState] = useState<AuthState["syncState"]>("idle");
  const timer = useRef<ReturnType<typeof setTimeout> | null>(null);
  const ready = useRef(false);

  // ---------- push local progress to Supabase ----------
  const push = useCallback(async () => {
    if (!supabase || !user || !ready.current) return;
    const s = snapshot();
    if (s.userId !== user.id) return;
    setSyncState("saving");
    const { error } = await supabase.from("progress").upsert({ user_id: user.id, state: s, updated_at: new Date(s.updatedAt || Date.now()).toISOString() });
    await supabase.from("profiles").update({
      display_name: s.settings.displayName || null,
      total_xp: s.xp,
      weekly_xp: weeklyXp(s),
      week_start: weekStart(),
      leaderboard_opt_in: s.settings.leaderboard,
      words_learned: Object.keys(s.items).filter((k) => !k.startsWith("p:")).length,
    }).eq("id", user.id);
    setSyncState(error ? "error" : "saved");
  }, [user]);

  // ---------- initial load + auth listener ----------
  useEffect(() => {
    if (DEMO_MODE) {
      const r = (localStorage.getItem(DEMO_ROLE_KEY) as Role) || "learner";
      setDemoRoleState(r);
      setUser({ id: "demo", email: "demo@device" });
      const s = snapshot();
      if (s.userId !== "demo") useProgress.setState({ userId: "demo" });
      ready.current = true;
      setStatus("signedIn");
      return;
    }
    const sb = supabase!;
    sb.auth.getSession().then(({ data }) => applyUser(data.session?.user ?? null));
    const { data: sub } = sb.auth.onAuthStateChange((_e, session) => applyUser(session?.user ?? null));
    return () => sub.subscription.unsubscribe();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const lastUid = useRef<string | null>(null);
  async function applyUser(u: User | null) {
    if (!u) { lastUid.current = null; ready.current = false; setUser(null); setProfile(null); setStatus("signedOut"); return; }
    if (lastUid.current === u.id) return;
    lastUid.current = u.id;
    setUser({ id: u.id, email: u.email || "" });
    const sb = supabase!;
    const [{ data: prof }, { data: prog }] = await Promise.all([
      sb.from("profiles").select("id,email,display_name,role,leaderboard_opt_in").eq("id", u.id).maybeSingle(),
      sb.from("progress").select("state,updated_at").eq("user_id", u.id).maybeSingle(),
    ]);
    setProfile(prof as Profile | null);
    const local = snapshot();
    const remote = prog?.state as ProgressData | undefined;
    if (local.userId !== u.id) {
      if (remote) useProgress.getState().replaceAll({ ...remote, userId: u.id });
      else if (local.userId === null && local.updatedAt > 0) useProgress.setState({ userId: u.id });
      else useProgress.getState().resetFor(u.id);
    } else if (remote && (remote.updatedAt || 0) > (local.updatedAt || 0)) {
      useProgress.getState().replaceAll({ ...remote, userId: u.id });
    }
    const s = snapshot();
    if (!s.settings.displayName) {
      const name = (prof as Profile | null)?.display_name || (u.user_metadata?.full_name as string) || (u.user_metadata?.name as string) || (u.email || "").split("@")[0];
      useProgress.getState().setSettings({ displayName: name });
    }
    ready.current = true;
    setStatus("signedIn");
  }

  // ---------- debounced sync on every change ----------
  useEffect(() => {
    if (DEMO_MODE || !user) return;
    const unsub = useProgress.subscribe((s, prev) => {
      if (s.updatedAt === prev.updatedAt) return;
      if (timer.current) clearTimeout(timer.current);
      timer.current = setTimeout(push, 2500);
    });
    const onHide = () => { if (document.visibilityState === "hidden") push(); };
    document.addEventListener("visibilitychange", onHide);
    push();
    return () => { unsub(); document.removeEventListener("visibilitychange", onHide); };
  }, [user, push]);

  const role: Role = DEMO_MODE ? demoRole : profile?.role || "learner";
  const value: AuthState = {
    status, user, profile, role,
    isTeacher: role === "teacher" || role === "superadmin",
    isAdmin: role === "superadmin",
    demo: DEMO_MODE,
    syncState,
    syncNow: push,
    setDemoRole: (r) => { localStorage.setItem(DEMO_ROLE_KEY, r); setDemoRoleState(r); },
    signOut: async () => {
      if (supabase) { await push(); await supabase.auth.signOut(); }
    },
  };
  return <Ctx.Provider value={value}>{children}</Ctx.Provider>;
}
