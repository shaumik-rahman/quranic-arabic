"use client";
import { useEffect } from "react";
import { AuthProvider } from "@/lib/auth";
import { useProgress } from "@/lib/store";
import { WordSheetProvider } from "./WordSheet";

export function Providers({ children }: { children: React.ReactNode }) {
  const lang = useProgress((s) => s.settings.lang);
  useEffect(() => {
    document.documentElement.lang = lang;
  }, [lang]);
  useEffect(() => {
    const refill = () => useProgress.getState().refillHearts();
    refill();
    const id = setInterval(refill, 60_000);
    if ("serviceWorker" in navigator && process.env.NODE_ENV === "production") {
      navigator.serviceWorker.register("/sw.js").catch(() => {});
    }
    return () => clearInterval(id);
  }, []);
  return (
    <AuthProvider>
      <WordSheetProvider>{children}</WordSheetProvider>
    </AuthProvider>
  );
}
