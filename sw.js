// ==============================================================================
// Service Worker - Offline Caching Engine for Interview Guide Platform
// ==============================================================================

const CACHE_NAME = 'interview-guide-v3';
const STATIC_ASSETS = [
  './',
  './index.html',
  './dashboard.html',
  './login.html',
  './signup.html',
  './assets/css/inline-styles.css',
  './assets/css/interview-styles.css',
  './assets/js/app-main.js',
  './assets/js/platform-features.js',
  './manifest.json',
  './favicon.ico',
  './assets/icons/interview_guide_logo.png',
  './assets/icons/icon-192x192.png',
  './assets/icons/icon-512x512.png',
  './assets/icons/html-css-js-icon.svg'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log('[ServiceWorker] Pre-caching offline static assets');
      // Resilient caching: cache available assets even if one fails
      return Promise.allSettled(
        STATIC_ASSETS.map((url) =>
          cache.add(url).catch((err) => {
            console.warn('[ServiceWorker] Could not pre-cache:', url, err);
          })
        )
      );
    })
  );
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keyList) => {
      return Promise.all(
        keyList.map((key) => {
          if (key !== CACHE_NAME) {
            console.log('[ServiceWorker] Removing obsolete cache:', key);
            return caches.delete(key);
          }
        })
      );
    })
  );
  self.clients.claim();
});

self.addEventListener('fetch', (event) => {
  // Only handle GET requests
  if (event.request.method !== 'GET') return;

  const url = new URL(event.request.url);

  // Skip browser extensions and chrome-extension schemes
  if (url.protocol !== 'http:' && url.protocol !== 'https:') return;

  // Stale-while-revalidate strategy for maximum speed and offline availability
  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      const fetchPromise = fetch(event.request)
        .then((networkResponse) => {
          if (networkResponse && networkResponse.status === 200 && networkResponse.type === 'basic') {
            const responseClone = networkResponse.clone();
            caches.open(CACHE_NAME).then((cache) => {
              cache.put(event.request, responseClone);
            });
          }
          return networkResponse;
        })
        .catch(() => {
          // If offline and request is for navigation/HTML, return index.html
          if (event.request.mode === 'navigate') {
            return caches.match('./index.html') || caches.match('./dashboard.html');
          }
          return cachedResponse;
        });

      return cachedResponse || fetchPromise;
    })
  );
});
