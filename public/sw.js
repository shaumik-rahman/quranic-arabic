/* Quranic Arabic service worker: offline app shell + cached Quran data. */
const VERSION = "qa-v3"; // v3: surah data now carries Bangla word glosses
const SHELL = `${VERSION}-shell`;
const STATIC = `${VERSION}-static`;
const DATA = `${VERSION}-data`;

const PRECACHE = ["/learn", "/review", "/quran", "/library", "/profile", "/icon-192.png", "/icon-512.png", "/manifest.webmanifest"];

self.addEventListener("install", (e) => {
  e.waitUntil(caches.open(SHELL).then((c) => c.addAll(PRECACHE).catch(() => {})).then(() => self.skipWaiting()));
});

self.addEventListener("activate", (e) => {
  e.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => !k.startsWith(VERSION)).map((k) => caches.delete(k))),
    ).then(() => self.clients.claim()),
  );
});

const cacheFirst = async (req, name) => {
  const hit = await caches.match(req);
  if (hit) return hit;
  const res = await fetch(req);
  if (res && (res.ok || res.type === "opaque")) (await caches.open(name)).put(req, res.clone());
  return res;
};
const staleWhileRevalidate = async (req, name) => {
  const cache = await caches.open(name);
  const hit = await cache.match(req);
  const net = fetch(req).then((res) => { if (res.ok) cache.put(req, res.clone()); return res; }).catch(() => hit);
  return hit || net;
};

self.addEventListener("fetch", (e) => {
  const req = e.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);

  // Audio and other sites (quran.com, everyayah, Supabase) go straight to the network:
  // Safari can't play audio that a service worker hands back.
  if (url.origin !== self.location.origin) return;

  if (url.pathname.startsWith("/_next/static/") || /\.(png|svg|woff2?|ttf|ico)$/.test(url.pathname)) {
    e.respondWith(cacheFirst(req, STATIC));
    return;
  }
  if (url.pathname.startsWith("/quran/") && url.pathname.endsWith(".json")) {
    e.respondWith(staleWhileRevalidate(req, DATA));
    return;
  }
  if (req.mode === "navigate") {
    e.respondWith(
      fetch(req)
        .then((res) => { const copy = res.clone(); caches.open(SHELL).then((c) => c.put(req, copy)); return res; })
        .catch(async () => (await caches.match(req)) || (await caches.match("/learn")) || Response.error()),
    );
    return;
  }
  e.respondWith(staleWhileRevalidate(req, STATIC));
});
