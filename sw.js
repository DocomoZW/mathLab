const CACHE_NAME = 'mathslms-v1';

const APP_SHELL = [
  '/learn',
  '/learn/',
];

// Content files we want to cache on access
const CONTENT_PATTERNS = [
  '/api/content-file?path=curriculum/',
  '/api/content-file?path=problems/',
  '/gifs/',
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      return cache.addAll(APP_SHELL);
    })
  );
  self.skipWaiting();
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys => {
      return Promise.all(
        keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k))
      );
    })
  );
  self.clients.claim();
});

self.addEventListener('fetch', event => {
  const url = new URL(event.request.url);

  // App shell: network first, fall back to cache
  if (url.pathname === '/learn' || url.pathname === '/learn/') {
    event.respondWith(
      fetch(event.request)
        .then(response => {
          const clone = response.clone();
          caches.open(CACHE_NAME).then(cache => cache.put(event.request, clone));
          return response;
        })
        .catch(() => caches.match(event.request))
    );
    return;
  }

  // Content API: cache first, network update
  if (url.pathname === '/api/content-file' || url.pathname.startsWith('/gifs/')) {
    event.respondWith(
      caches.match(event.request).then(cached => {
        if (cached) return cached;
        return fetch(event.request).then(response => {
          const clone = response.clone();
          caches.open(CACHE_NAME).then(cache => cache.put(event.request, clone));
          return response;
        });
      })
    );
    return;
  }

  // Dashboard API calls: network only
  if (url.pathname.startsWith('/api/')) {
    event.respondWith(fetch(event.request));
    return;
  }

  // Everything else: network first
  event.respondWith(
    fetch(event.request)
      .then(response => {
        const clone = response.clone();
        caches.open(CACHE_NAME).then(cache => cache.put(event.request, clone));
        return response;
      })
      .catch(() => caches.match(event.request).then(cached => {
        if (cached) return cached;
        // Offline fallback
        if (url.pathname === '/learn' || url.pathname === '/') {
          return caches.match('/learn');
        }
        return new Response('Offline', { status: 503 });
      }))
  );
});
