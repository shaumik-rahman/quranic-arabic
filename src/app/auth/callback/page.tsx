"use client";
import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { useAuth } from "@/lib/auth";

/** Supabase redirects here after Google sign-in / email confirmation; the client exchanges the code automatically. */
export default function AuthCallback() {
  const { status } = useAuth();
  const router = useRouter();
  const [slow, setSlow] = useState(false);
  useEffect(() => {
    if (status === "signedIn") router.replace("/learn");
    const id = setTimeout(() => setSlow(true), 6000);
    return () => clearTimeout(id);
  }, [status, router]);
  return (
    <div className="flex min-h-dvh flex-col items-center justify-center gap-4 p-8 text-center">
      <div className="h-12 w-12 animate-spin rounded-full border-4 border-line border-t-emerald" />
      <p className="font-bold text-muted">Signing you in…</p>
      {slow && <a href="/login" className="text-sm font-bold text-emerald underline">Taking too long? Back to sign in</a>}
    </div>
  );
}
