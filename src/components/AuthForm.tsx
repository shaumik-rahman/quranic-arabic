"use client";
import Link from "next/link";
import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { supabase } from "@/lib/supabase";
import { useAuth } from "@/lib/auth";

type Mode = "login" | "signup" | "forgot";

export function AuthForm({ mode }: { mode: Mode }) {
  const router = useRouter();
  const { status, demo } = useAuth();
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [busy, setBusy] = useState(false);
  const [err, setErr] = useState("");
  const [info, setInfo] = useState("");

  useEffect(() => { if (status === "signedIn") router.replace("/learn"); }, [status, router]);

  const origin = typeof window !== "undefined" ? window.location.origin : "";

  async function submit(e: React.FormEvent) {
    e.preventDefault();
    if (!supabase) return;
    setBusy(true); setErr(""); setInfo("");
    try {
      if (mode === "login") {
        const { error } = await supabase.auth.signInWithPassword({ email, password });
        if (error) throw error;
      } else if (mode === "signup") {
        const { data, error } = await supabase.auth.signUp({
          email, password, options: { data: { full_name: name }, emailRedirectTo: `${origin}/auth/callback` },
        });
        if (error) throw error;
        if (!data.session) setInfo("Check your email to confirm your account, then sign in.");
      } else {
        const { error } = await supabase.auth.resetPasswordForEmail(email, { redirectTo: `${origin}/auth/update-password` });
        if (error) throw error;
        setInfo("If that email has an account, a reset link is on its way.");
      }
    } catch (e: unknown) {
      setErr(e instanceof Error ? e.message : String(e));
    } finally {
      setBusy(false);
    }
  }

  async function google() {
    if (!supabase) return;
    setErr("");
    const { error } = await supabase.auth.signInWithOAuth({ provider: "google", options: { redirectTo: `${origin}/auth/callback` } });
    if (error) setErr(error.message);
  }

  const title = mode === "login" ? "Welcome back" : mode === "signup" ? "Create your account" : "Reset your password";
  return (
    <div className="pattern-soft flex min-h-dvh flex-col">
      <div className="pt-safe mx-auto w-full max-w-md flex-1 px-6 pt-10">
        <Link href="/" className="font-bold text-muted">← Quranic Arabic</Link>
        <h1 className="mt-6 text-3xl font-black">{title}</h1>
        {demo ? (
          <div className="card mt-6 p-5">
            <p className="font-bold">Demo mode</p>
            <p className="mt-1 text-sm text-muted">Accounts aren&apos;t connected yet (no Supabase keys). You can try everything now; progress is saved on this device.</p>
            <Link href="/learn" className="btn btn-primary mt-4 w-full">Start learning</Link>
          </div>
        ) : (
          <>
            {mode !== "forgot" && (
              <>
                <button onClick={google} className="btn btn-ghost mt-6 w-full">
                  <svg width="20" height="20" viewBox="0 0 48 48" aria-hidden><path fill="#FFC107" d="M43.6 20.5H42V20H24v8h11.3C33.7 32.7 29.2 36 24 36c-6.6 0-12-5.4-12-12s5.4-12 12-12c3.1 0 5.8 1.2 7.9 3.1l5.7-5.7C34 6.1 29.3 4 24 4 12.9 4 4 12.9 4 24s8.9 20 20 20 20-8.9 20-20c0-1.3-.1-2.4-.4-3.5z"/><path fill="#FF3D00" d="m6.3 14.7 6.6 4.8C14.7 15.1 19 12 24 12c3.1 0 5.8 1.2 7.9 3.1l5.7-5.7C34 6.1 29.3 4 24 4 16.3 4 9.7 8.3 6.3 14.7z"/><path fill="#4CAF50" d="M24 44c5.2 0 9.9-2 13.4-5.2l-6.2-5.2C29.2 35.1 26.7 36 24 36c-5.2 0-9.6-3.3-11.3-8l-6.5 5C9.5 39.6 16.2 44 24 44z"/><path fill="#1976D2" d="M43.6 20.5H42V20H24v8h11.3c-.8 2.2-2.2 4.2-4.1 5.6l6.2 5.2C37 39.2 44 34 44 24c0-1.3-.1-2.4-.4-3.5z"/></svg>
                  Continue with Google
                </button>
                <div className="my-5 flex items-center gap-3 text-sm font-bold text-muted"><div className="h-0.5 flex-1 bg-line" />or<div className="h-0.5 flex-1 bg-line" /></div>
              </>
            )}
            <form onSubmit={submit} className={`space-y-3 ${mode === "forgot" ? "mt-6" : ""}`}>
              {mode === "signup" && <Field label="Name" value={name} onChange={setName} autoComplete="name" />}
              <Field label="Email" type="email" value={email} onChange={setEmail} autoComplete="email" required />
              {mode !== "forgot" && (
                <Field label="Password" type="password" value={password} onChange={setPassword} required minLength={6}
                  autoComplete={mode === "login" ? "current-password" : "new-password"} />
              )}
              {err && <p className="rounded-xl bg-coral-light p-3 text-sm font-bold text-coral-dark">{err}</p>}
              {info && <p className="rounded-xl bg-emerald-light p-3 text-sm font-bold text-emerald-dark">{info}</p>}
              <button disabled={busy} className="btn btn-primary w-full text-lg">
                {busy ? "…" : mode === "login" ? "Sign in" : mode === "signup" ? "Create account" : "Send reset link"}
              </button>
            </form>
            <div className="mt-5 space-y-2 text-center text-sm font-bold">
              {mode === "login" && <>
                <Link href="/forgot" className="block text-muted">Forgot password?</Link>
                <Link href="/signup" className="block text-emerald">New here? Create an account</Link>
              </>}
              {mode === "signup" && <Link href="/login" className="block text-emerald">Already have an account? Sign in</Link>}
              {mode === "forgot" && <Link href="/login" className="block text-emerald">Back to sign in</Link>}
            </div>
          </>
        )}
      </div>
    </div>
  );
}

export function Field({ label, value, onChange, ...rest }: { label: string; value: string; onChange: (v: string) => void } & Omit<React.InputHTMLAttributes<HTMLInputElement>, "onChange" | "value">) {
  return (
    <label className="block">
      <span className="text-sm font-bold text-muted">{label}</span>
      <input {...rest} value={value} onChange={(e) => onChange(e.target.value)}
        className="mt-1 w-full rounded-2xl border-2 border-line bg-white px-4 py-3 text-lg outline-none focus:border-emerald" />
    </label>
  );
}
