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

// ==============================================================================
// 4. Web Push Notification Handling (Item #15)
// ==============================================================================
self.addEventListener('push', (event) => {
  let data = { title: 'Tech Interview Guide', body: 'Time for your daily interview review!' };
  if (event.data) {
    try {
      data = event.data.json();
    } catch (e) {
      data.body = event.data.text();
    }
  }

  const options = {
    body: data.body,
    icon: './assets/icons/icon-192x192.png',
    badge: './assets/icons/icon-192x192.png',
    data: {
      url: data.url || './dashboard.html'
    },
    vibrate: [100, 50, 100],
    actions: [
      { action: 'review', title: 'Review Now' },
      { action: 'dismiss', title: 'Later' }
    ]
  };

  event.waitUntil(
    self.registration.showNotification(data.title || 'Tech Interview Guide', options)
  );
});

self.addEventListener('notificationclick', (event) => {
  event.notification.close();
  const urlToOpen = event.notification.data?.url || './dashboard.html';
  event.waitUntil(
    clients.matchAll({ type: 'window', includeUncontrolled: true }).then((windowClients) => {
      for (let client of windowClients) {
        if (client.url.includes('interview') && 'focus' in client) {
          return client.focus();
        }
      }
      if (clients.openWindow) {
        return clients.openWindow(urlToOpen);
      }
    })
  );
});

// ==============================================================================
// 5. Offline Background Sync (Item #50)
// ==============================================================================
self.addEventListener('sync', (event) => {
  if (event.tag === 'sync-study-progress') {
    event.waitUntil(
      clients.matchAll().then((clientsList) => {
        clientsList.forEach((client) => {
          client.postMessage({ type: 'SYNC_OFFLINE_QUEUE' });
        });
      })
    );
  }
});

