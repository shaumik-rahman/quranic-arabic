"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";
import { supabase } from "@/lib/supabase";
import { Field } from "@/components/AuthForm";

export default function UpdatePassword() {
  const router = useRouter();
  const [pw, setPw] = useState("");
  const [msg, setMsg] = useState("");
  const [busy, setBusy] = useState(false);
  async function submit(e: React.FormEvent) {
    e.preventDefault();
    if (!supabase) return;
    setBusy(true);
    const { error } = await supabase.auth.updateUser({ password: pw });
    setBusy(false);
    if (error) setMsg(error.message);
    else router.replace("/learn");
  }
  return (
    <div className="mx-auto max-w-md px-6 pt-16">
      <h1 className="text-3xl font-black">Choose a new password</h1>
      <form onSubmit={submit} className="mt-6 space-y-3">
        <Field label="New password" type="password" value={pw} onChange={setPw} minLength={6} required autoComplete="new-password" />
        {msg && <p className="rounded-xl bg-coral-light p-3 text-sm font-bold text-coral-dark">{msg}</p>}
        <button disabled={busy} className="btn btn-primary w-full">{busy ? "…" : "Save password"}</button>
      </form>
    </div>
  );
}
