"use client";
import { Fragment, useEffect } from "react";
import { AuthProvider } from "@/lib/auth";
import { useProgress } from "@/lib/store";
import { WordSheetProvider } from "./WordSheet";
import { initAudioUnlock } from "@/lib/audio";
import { loadOverrides, useContent } from "@/lib/overrides";

export function Providers({ children }: { children: React.ReactNode }) {
  const lang = useProgress((s) => s.settings.lang);
  const script = useProgress((s) => s.settings.script) ?? "indopak";
  const remount = useContent((s) => s.remount);
  useEffect(() => {
    document.documentElement.lang = lang;
  }, [lang]);
  useEffect(() => {
    document.documentElement.dataset.script = script;
  }, [script]);
  useEffect(() => {
    const refill = () => useProgress.getState().refillHearts();
    refill();
    initAudioUnlock();
    loadOverrides();
    const id = setInterval(refill, 60_000);
    if ("serviceWorker" in navigator && process.env.NODE_ENV === "production") {
      navigator.serviceWorker.register("/sw.js").catch(() => {});
    }
    return () => clearInterval(id);
  }, []);
  return (
    <AuthProvider>
      {/* content edits from the superadmin: re-render with the new text when they arrive */}
      <WordSheetProvider><Fragment key={remount}>{children}</Fragment></WordSheetProvider>
    </AuthProvider>
  );
}
