import { AuthGate, BottomNav, TopBar } from "@/components/AppShell";

export default function MainLayout({ children }: { children: React.ReactNode }) {
  return (
    <AuthGate>
      <TopBar />
      <main className="mx-auto max-w-lg px-4 pb-28 pt-4">{children}</main>
      <BottomNav />
    </AuthGate>
  );
}
