// Fallback redirect for legacy service-worker.js registrations
try {
  importScripts('./sw.js');
} catch (e) {
  console.warn('Failed to import sw.js from service-worker.js', e);
}