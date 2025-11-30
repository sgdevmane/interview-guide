<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>Node.js Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for backend developers</b></p>
</div>

---

## Table of Contents

1. [How do you handle backpressure in a Node.js stream pipeline?](#q1-how-do-you-handle-backpressure-in-a-node.js-stream-pipeline) <span class="intermediate">Intermediate</span>
2. [How do you offload CPU-intensive tasks using Worker Threads?](#q2-how-do-you-offload-cpu-intensive-tasks-using-worker-threads) <span class="intermediate">Intermediate</span>
3. [How do you implement a custom Transform stream to modify data on the fly?](#q3-how-do-you-implement-a-custom-transform-stream-to-modify-data-on-the-fly) <span class="intermediate">Intermediate</span>
4. [How do you handle errors in async/await middleware in Express?](#q4-how-do-you-handle-errors-in-asyncawait-middleware-in-express) <span class="intermediate">Intermediate</span>
5. [How do you implement graceful shutdown in a Node.js server?](#q5-how-do-you-implement-graceful-shutdown-in-a-node.js-server) <span class="intermediate">Intermediate</span>
6. [How do you prevent prototype pollution in Node.js applications?](#q6-how-do-you-prevent-prototype-pollution-in-node.js-applications) <span class="intermediate">Intermediate</span>
7. [How do you migrate from CommonJS to ES Modules (ESM) in Node.js?](#q7-how-do-you-migrate-from-commonjs-to-es-modules-esm-in-node.js) <span class="intermediate">Intermediate</span>
8. [How do you debug memory leaks in Node.js?](#q8-how-do-you-debug-memory-leaks-in-node.js) <span class="intermediate">Intermediate</span>
9. [How do you scale a Node.js application using the Cluster module?](#q9-how-do-you-scale-a-node.js-application-using-the-cluster-module) <span class="intermediate">Intermediate</span>
10. [How do you securely hash passwords using the built-in crypto module?](#q10-how-do-you-securely-hash-passwords-using-the-built-in-crypto-module) <span class="intermediate">Intermediate</span>
11. [How do you create a CLI tool with Node.js?](#q11-how-do-you-create-a-cli-tool-with-node.js) <span class="intermediate">Intermediate</span>
12. [How do you process large files line-by-line to keep memory usage low?](#q12-how-do-you-process-large-files-line-by-line-to-keep-memory-usage-low) <span class="intermediate">Intermediate</span>
13. [How do you handle multiple Promises concurrently but fail gracefully if one fails?](#q13-how-do-you-handle-multiple-promises-concurrently-but-fail-gracefully-if-one-fails) <span class="intermediate">Intermediate</span>
14. [How do you optimize Node.js performance by caching static assets?](#q14-how-do-you-optimize-node.js-performance-by-caching-static-assets) <span class="intermediate">Intermediate</span>
15. [How do you use Buffers to manipulate binary data?](#q15-how-do-you-use-buffers-to-manipulate-binary-data) <span class="intermediate">Intermediate</span>
16. [How do you handle Implementing JWT authentication?](#q16-how-do-you-handle-implementing-jwt-authentication) <span class="intermediate">Intermediate</span>
17. [How do you handle Rate limiting requests?](#q17-how-do-you-handle-rate-limiting-requests) <span class="intermediate">Intermediate</span>
18. [How do you handle Using node-postgres vs ORMs?](#q18-how-do-you-handle-using-node-postgres-vs-orms) <span class="intermediate">Intermediate</span>
19. [How do you handle Handling uncaught exceptions?](#q19-how-do-you-handle-handling-uncaught-exceptions) <span class="intermediate">Intermediate</span>
20. [How do you validate API requests using Joi?](#q20-how-do-you-validate-api-requests-using-joi) <span class="intermediate">Intermediate</span>
21. [How do you implement structured logging using Winston?](#q21-how-do-you-implement-structured-logging-using-winston) <span class="intermediate">Intermediate</span>
22. [How do you handle file uploads using Multer?](#q22-how-do-you-handle-file-uploads-using-multer) <span class="intermediate">Intermediate</span>
23. [How do you use dotenv to manage environment variables?](#q23-how-do-you-use-dotenv-to-manage-environment-variables) <span class="beginner">Beginner</span>
24. [How do you use spawn to run a child process?](#q24-how-do-you-use-spawn-to-run-a-child-process) <span class="intermediate">Intermediate</span>
25. [How do you write a simple unit test with Jest?](#q25-how-do-you-write-a-simple-unit-test-with-jest) <span class="beginner">Beginner</span>
26. [How do you use AsyncLocalStorage for request context tracking?](#q26-how-do-you-use-asynclocalstorage-for-request-context-tracking) <span class="advanced">Advanced</span>
27. [How do you Dockerize a Node.js application?](#q27-how-do-you-dockerize-a-node.js-application) <span class="intermediate">Intermediate</span>
28. [How do you use the path module to handle file paths cross-platform?](#q28-how-do-you-use-the-path-module-to-handle-file-paths-cross-platform) <span class="beginner">Beginner</span>
29. [What is the difference between `process.nextTick` and `setImmediate`?](#q29-what-is-the-difference-between-process.nexttick-and-setimmediate) <span class="advanced">Advanced</span>
30. [How do you safely spawn a child process?](#q30-how-do-you-safely-spawn-a-child-process) <span class="intermediate">Intermediate</span>
31. [How do you handle unhandled promise rejections globally?](#q31-how-do-you-handle-unhandled-promise-rejections-globally) <span class="intermediate">Intermediate</span>
32. [How do you optimize garbage collection in Node.js?](#q32-how-do-you-optimize-garbage-collection-in-node.js) <span class="advanced">Advanced</span>
33. [How do you use Buffers safely?](#q33-how-do-you-use-buffers-safely) <span class="intermediate">Intermediate</span>
34. [How do you debug a Node.js application with the Inspector?](#q34-how-do-you-debug-a-node.js-application-with-the-inspector) <span class="beginner">Beginner</span>
35. [How do you create a secure HTTPS server?](#q35-how-do-you-create-a-secure-https-server) <span class="intermediate">Intermediate</span>
36. [How do you use `util.promisify` to convert callback-based functions?](#q36-how-do-you-use-util.promisify-to-convert-callback-based-functions) <span class="beginner">Beginner</span>
37. [How do you parse large JSON files without blocking the event loop?](#q37-how-do-you-parse-large-json-files-without-blocking-the-event-loop) <span class="advanced">Advanced</span>
38. [How do you implement a simple rate limiter using Redis?](#q38-how-do-you-implement-a-simple-rate-limiter-using-redis) <span class="advanced">Advanced</span>
39. [How do you use `vm` module to run untrusted code (Sandboxing)?](#q39-how-do-you-use-vm-module-to-run-untrusted-code-sandboxing) <span class="advanced">Advanced</span>
40. [How do you prevent blocking the Event Loop with cryptographic operations?](#q40-how-do-you-prevent-blocking-the-event-loop-with-cryptographic-operations) <span class="intermediate">Intermediate</span>
41. [How do you use `require.resolve`?](#q41-how-do-you-use-require.resolve) <span class="beginner">Beginner</span>
42. [How do you implement simple middleware in pure Node.js?](#q42-how-do-you-implement-simple-middleware-in-pure-node.js) <span class="intermediate">Intermediate</span>
43. [How do you use the `repl` module to create a custom shell?](#q43-how-do-you-use-the-repl-module-to-create-a-custom-shell) <span class="intermediate">Intermediate</span>
44. [How do you benchmark Node.js code using `perf_hooks`?](#q44-how-do-you-benchmark-node.js-code-using-perf_hooks) <span class="intermediate">Intermediate</span>
45. [How do you serve static files without a framework?](#q45-how-do-you-serve-static-files-without-a-framework) <span class="intermediate">Intermediate</span>
46. [What are the security implications of Node.js in real-time systems?](#q46-what-are-the-security-implications-of-node.js-in-real-time-systems) <span class="intermediate">Intermediate</span>
47. [How do you debug Node.js memory leaks in distributed systems?](#q47-how-do-you-debug-node.js-memory-leaks-in-distributed-systems) <span class="advanced">Advanced</span>
48. [Best practices for Node.js code organization in high-traffic sites?](#q48-best-practices-for-node.js-code-organization-in-high-traffic-sites) <span class="beginner">Beginner</span>
49. [How do you implement Node.js error handling for embedded systems?](#q49-how-do-you-implement-node.js-error-handling-for-embedded-systems) <span class="intermediate">Intermediate</span>
50. [How do you test Node.js functionality in production environments?](#q50-how-do-you-test-node.js-functionality-in-production-environments) <span class="intermediate">Intermediate</span>
51. [How do you handle Node.js state management in large scale applications?](#q51-how-do-you-handle-node.js-state-management-in-large-scale-applications) <span class="advanced">Advanced</span>
52. [How do you perform Node.js data validation in microservices?](#q52-how-do-you-perform-node.js-data-validation-in-microservices) <span class="beginner">Beginner</span>
53. [How do you automate Node.js deployment for mobile devices?](#q53-how-do-you-automate-node.js-deployment-for-mobile-devices) <span class="advanced">Advanced</span>
54. [How do you handle Node.js concurrency issues in legacy systems?](#q54-how-do-you-handle-node.js-concurrency-issues-in-legacy-systems) <span class="advanced">Advanced</span>
55. [How do you implement Node.js caching in cloud infrastructure?](#q55-how-do-you-implement-node.js-caching-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
56. [How do you manage Node.js configuration for real-time systems?](#q56-how-do-you-manage-node.js-configuration-for-real-time-systems) <span class="beginner">Beginner</span>
57. [How do you handle Node.js internationalization (i18n) in distributed systems?](#q57-how-do-you-handle-node.js-internationalization-i18n-in-distributed-systems) <span class="intermediate">Intermediate</span>
58. [How do you ensure Node.js accessibility (a11y) in high-traffic sites?](#q58-how-do-you-ensure-node.js-accessibility-a11y-in-high-traffic-sites) <span class="beginner">Beginner</span>
59. [How do you optimize Node.js network requests in embedded systems?](#q59-how-do-you-optimize-node.js-network-requests-in-embedded-systems) <span class="advanced">Advanced</span>
60. [How do you handle Node.js performance optimization for production environments?](#q60-how-do-you-handle-node.js-performance-optimization-for-production-environments) <span class="advanced">Advanced</span>
61. [What are the security implications of Node.js in large scale applications?](#q61-what-are-the-security-implications-of-node.js-in-large-scale-applications) <span class="intermediate">Intermediate</span>
62. [How do you debug Node.js memory leaks in microservices?](#q62-how-do-you-debug-node.js-memory-leaks-in-microservices) <span class="advanced">Advanced</span>
63. [Best practices for Node.js code organization in mobile devices?](#q63-best-practices-for-node.js-code-organization-in-mobile-devices) <span class="beginner">Beginner</span>
64. [How do you implement Node.js error handling for legacy systems?](#q64-how-do-you-implement-node.js-error-handling-for-legacy-systems) <span class="intermediate">Intermediate</span>
65. [How do you test Node.js functionality in cloud infrastructure?](#q65-how-do-you-test-node.js-functionality-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
66. [How do you handle Node.js state management in real-time systems?](#q66-how-do-you-handle-node.js-state-management-in-real-time-systems) <span class="advanced">Advanced</span>
67. [How do you perform Node.js data validation in distributed systems?](#q67-how-do-you-perform-node.js-data-validation-in-distributed-systems) <span class="beginner">Beginner</span>
68. [How do you automate Node.js deployment for high-traffic sites?](#q68-how-do-you-automate-node.js-deployment-for-high-traffic-sites) <span class="advanced">Advanced</span>
69. [How do you handle Node.js concurrency issues in embedded systems?](#q69-how-do-you-handle-node.js-concurrency-issues-in-embedded-systems) <span class="advanced">Advanced</span>
70. [How do you implement Node.js caching in production environments?](#q70-how-do-you-implement-node.js-caching-in-production-environments) <span class="intermediate">Intermediate</span>
71. [How do you manage Node.js configuration for large scale applications?](#q71-how-do-you-manage-node.js-configuration-for-large-scale-applications) <span class="beginner">Beginner</span>
72. [How do you handle Node.js internationalization (i18n) in microservices?](#q72-how-do-you-handle-node.js-internationalization-i18n-in-microservices) <span class="intermediate">Intermediate</span>
73. [How do you ensure Node.js accessibility (a11y) in mobile devices?](#q73-how-do-you-ensure-node.js-accessibility-a11y-in-mobile-devices) <span class="beginner">Beginner</span>
74. [How do you optimize Node.js network requests in legacy systems?](#q74-how-do-you-optimize-node.js-network-requests-in-legacy-systems) <span class="advanced">Advanced</span>
75. [How do you handle Node.js performance optimization for cloud infrastructure?](#q75-how-do-you-handle-node.js-performance-optimization-for-cloud-infrastructure) <span class="advanced">Advanced</span>
76. [What are the security implications of Node.js in real-time systems?](#q76-what-are-the-security-implications-of-node.js-in-real-time-systems) <span class="intermediate">Intermediate</span>
77. [How do you debug Node.js memory leaks in distributed systems?](#q77-how-do-you-debug-node.js-memory-leaks-in-distributed-systems) <span class="advanced">Advanced</span>
78. [Best practices for Node.js code organization in high-traffic sites?](#q78-best-practices-for-node.js-code-organization-in-high-traffic-sites) <span class="beginner">Beginner</span>
79. [How do you implement Node.js error handling for embedded systems?](#q79-how-do-you-implement-node.js-error-handling-for-embedded-systems) <span class="intermediate">Intermediate</span>
80. [How do you test Node.js functionality in production environments?](#q80-how-do-you-test-node.js-functionality-in-production-environments) <span class="intermediate">Intermediate</span>
81. [How do you handle Node.js state management in large scale applications?](#q81-how-do-you-handle-node.js-state-management-in-large-scale-applications) <span class="advanced">Advanced</span>
82. [How do you perform Node.js data validation in microservices?](#q82-how-do-you-perform-node.js-data-validation-in-microservices) <span class="beginner">Beginner</span>
83. [How do you automate Node.js deployment for mobile devices?](#q83-how-do-you-automate-node.js-deployment-for-mobile-devices) <span class="advanced">Advanced</span>
84. [How do you handle Node.js concurrency issues in legacy systems?](#q84-how-do-you-handle-node.js-concurrency-issues-in-legacy-systems) <span class="advanced">Advanced</span>
85. [How do you implement Node.js caching in cloud infrastructure?](#q85-how-do-you-implement-node.js-caching-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
86. [How do you manage Node.js configuration for real-time systems?](#q86-how-do-you-manage-node.js-configuration-for-real-time-systems) <span class="beginner">Beginner</span>
87. [How do you handle Node.js internationalization (i18n) in distributed systems?](#q87-how-do-you-handle-node.js-internationalization-i18n-in-distributed-systems) <span class="intermediate">Intermediate</span>
88. [How do you ensure Node.js accessibility (a11y) in high-traffic sites?](#q88-how-do-you-ensure-node.js-accessibility-a11y-in-high-traffic-sites) <span class="beginner">Beginner</span>
89. [How do you optimize Node.js network requests in embedded systems?](#q89-how-do-you-optimize-node.js-network-requests-in-embedded-systems) <span class="advanced">Advanced</span>
90. [How do you handle Node.js performance optimization for production environments?](#q90-how-do-you-handle-node.js-performance-optimization-for-production-environments) <span class="advanced">Advanced</span>
91. [What are the security implications of Node.js in large scale applications?](#q91-what-are-the-security-implications-of-node.js-in-large-scale-applications) <span class="intermediate">Intermediate</span>
92. [How do you debug Node.js memory leaks in microservices?](#q92-how-do-you-debug-node.js-memory-leaks-in-microservices) <span class="advanced">Advanced</span>
93. [Best practices for Node.js code organization in mobile devices?](#q93-best-practices-for-node.js-code-organization-in-mobile-devices) <span class="beginner">Beginner</span>
94. [How do you implement Node.js error handling for legacy systems?](#q94-how-do-you-implement-node.js-error-handling-for-legacy-systems) <span class="intermediate">Intermediate</span>
95. [How do you test Node.js functionality in cloud infrastructure?](#q95-how-do-you-test-node.js-functionality-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
96. [How do you handle Node.js state management in real-time systems?](#q96-how-do-you-handle-node.js-state-management-in-real-time-systems) <span class="advanced">Advanced</span>
97. [How do you perform Node.js data validation in distributed systems?](#q97-how-do-you-perform-node.js-data-validation-in-distributed-systems) <span class="beginner">Beginner</span>
98. [How do you automate Node.js deployment for high-traffic sites?](#q98-how-do-you-automate-node.js-deployment-for-high-traffic-sites) <span class="advanced">Advanced</span>
99. [How do you handle Node.js concurrency issues in embedded systems?](#q99-how-do-you-handle-node.js-concurrency-issues-in-embedded-systems) <span class="advanced">Advanced</span>
100. [How do you implement Node.js caching in production environments?](#q100-how-do-you-implement-node.js-caching-in-production-environments) <span class="intermediate">Intermediate</span>

---

### Q1:  How do you handle backpressure in a Node.js stream pipeline?

**Difficulty**: Intermediate

**Strategy:**
Backpressure occurs when a readable stream emits data faster than a writable stream can consume it. To handle this:
1. Use the `stream.write()` return value: if it returns `false`, stop reading.
2. Listen for the `'drain'` event on the writable stream to resume reading.
3. Alternatively, use `pipeline()` or `pump()` which handle backpressure automatically.

**Code Snippet:**
```javascript
const fs = require('fs');

const readable = fs.createReadStream('input.txt');
const writable = fs.createWriteStream('output.txt');

readable.on('data', (chunk) => {
  // write() returns false if the internal buffer is full
  const canWrite = writable.write(chunk);
  
  if (!canWrite) {
    // Backpressure detected, stop reading
    console.log('Backpressure detected, pausing...');
    readable.pause();
    
    // Wait for buffer to drain
    writable.once('drain', () => {
      console.log('Buffer drained, resuming...');
      readable.resume();
    });
  }
});

// Better approach using pipeline (Node 10+)
const { pipeline } = require('stream');
pipeline(
  readable,
  writable,
  (err) => {
    if (err) console.error('Pipeline failed', err);
    else console.log('Pipeline succeeded');
  }
);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q2:  How do you offload CPU-intensive tasks using Worker Threads?

**Difficulty**: Intermediate

**Strategy:**
Node.js is single-threaded. Blocking the event loop with CPU-heavy tasks (like image processing or cryptography) freezes the server.
1. Use the `worker_threads` module to run code in parallel threads.
2. The main thread passes data to the worker via `workerData` or `postMessage`.
3. The worker performs the computation and sends the result back via `parentPort.postMessage`.

**Code Snippet:**
```javascript
// main.js
const { Worker } = require('worker_threads');

function runService(workerData) {
  return new Promise((resolve, reject) => {
    const worker = new Worker('./worker.js', { workerData });
    
    worker.on('message', resolve);
    worker.on('error', reject);
    worker.on('exit', (code) => {
      if (code !== 0) reject(new Error(`Worker stopped with exit code ${code}`));
    });
  });
}

async function run() {
  const result = await runService('Hello from main');
  console.log(result);
}
run();

// worker.js
const { workerData, parentPort } = require('worker_threads');

// Simulate CPU intensive task
const result = workerData.toUpperCase() + ' PROCESSED';
parentPort.postMessage(result);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q3:  How do you implement a custom Transform stream to modify data on the fly?

**Difficulty**: Intermediate

**Strategy:**
1. Extend the `Transform` class from the `stream` module.
2. Implement the `_transform(chunk, encoding, callback)` method.
3. Process the chunk (e.g., compress, encrypt, or modify text).
4. Call `this.push(transformedChunk)` to output data.
5. Call `callback()` when done processing the chunk.

**Code Snippet:**
```javascript
const { Transform } = require('stream');

class UpperCaseTransform extends Transform {
  _transform(chunk, encoding, callback) {
    try {
      const upperChunk = chunk.toString().toUpperCase();
      this.push(upperChunk);
      callback();
    } catch (err) {
      callback(err);
    }
  }
}

const upper = new UpperCaseTransform();

process.stdin.pipe(upper).pipe(process.stdout);
// Usage: echo "hello" | node script.js -> HELLO
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q4:  How do you handle errors in async/await middleware in Express?

**Difficulty**: Intermediate

**Strategy:**
Express 4.x doesn't automatically catch errors in async functions. If an async middleware throws or rejects, the request hangs unless you:
1. Wrap the code in `try...catch` and call `next(err)`.
2. Use a wrapper function to automatically catch errors.
3. Use Express 5 (beta) which supports async handlers natively.

**Code Snippet:**
```javascript
const express = require('express');
const app = express();

// Wrapper to catch async errors
const asyncHandler = (fn) => (req, res, next) => {
  Promise.resolve(fn(req, res, next)).catch(next);
};

app.get('/users', asyncHandler(async (req, res) => {
  const users = await db.getUsers(); // Might throw
  res.json(users);
}));

// Global error handler
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send('Something broke!');
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q5:  How do you implement graceful shutdown in a Node.js server?

**Difficulty**: Intermediate

**Strategy:**
Forcefully killing a process can corrupt data or leave connections open.
1. Listen for termination signals (`SIGTERM`, `SIGINT`).
2. Stop the server from accepting new connections (`server.close()`).
3. Close database connections and release resources.
4. Exit the process with `process.exit(0)`.

**Code Snippet:**
```javascript
const express = require('express');
const app = express();
const server = app.listen(3000);

process.on('SIGTERM', () => {
  console.log('SIGTERM signal received: closing HTTP server');
  
  server.close(() => {
    console.log('HTTP server closed');
    // Close DB connections here
    // db.close();
    process.exit(0);
  });
  
  // Force close after timeout
  setTimeout(() => {
    console.error('Forcing shutdown');
    process.exit(1);
  }, 10000);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q6:  How do you prevent prototype pollution in Node.js applications?

**Difficulty**: Intermediate

**Strategy:**
Prototype pollution occurs when an attacker modifies `Object.prototype`.
1. Use `Object.create(null)` to create objects without a prototype.
2. Freeze the prototype using `Object.freeze(Object.prototype)`.
3. Validate JSON input schemas.
4. Use deep merge libraries that are safe against pollution (e.g., lodash `merge` is now safe, but check versions).

**Code Snippet:**
```javascript
// Vulnerable merge
function merge(target, source) {
  for (let key in source) {
    if (typeof source[key] === 'object') {
      target[key] = merge(target[key] || {}, source[key]);
    } else {
      target[key] = source[key];
    }
  }
  return target;
}

// Safe implementation
function safeMerge(target, source) {
  for (let key in source) {
    if (key === '__proto__' || key === 'constructor' || key === 'prototype') {
      continue; // Skip dangerous keys
    }
    if (typeof source[key] === 'object' && source[key] !== null) {
      target[key] = safeMerge(target[key] || {}, source[key]);
    } else {
      target[key] = source[key];
    }
  }
  return target;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q7:  How do you migrate from CommonJS to ES Modules (ESM) in Node.js?

**Difficulty**: Intermediate

**Strategy:**
1. Set `"type": "module"` in `package.json`.
2. Change file extensions to `.mjs` (optional if step 1 is done).
3. Use `import`/`export` instead of `require`/`module.exports`.
4. Replace `__dirname` and `__filename` with `import.meta.url`.

**Code Snippet:**
```javascript
// package.json
// { "type": "module" }

// server.js (ESM)
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

// Replicating __dirname
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

export function readConfig() {
  return fs.readFileSync(path.join(__dirname, 'config.json'), 'utf8');
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q8:  How do you debug memory leaks in Node.js?

**Difficulty**: Intermediate

**Strategy:**
1. Use the `--inspect` flag to enable the Chrome DevTools inspector.
2. Open `chrome://inspect` in Chrome.
3. Take Heap Snapshots to compare memory usage over time.
4. Look for objects that are retained (detached DOM nodes in frontend, or closures/global variables in backend).
5. Use `process.memoryUsage()` for programmatic monitoring.

**Code Snippet:**
```javascript
// Run with: node --inspect index.js

const leaks = [];

function LeakyClass() {
  this.data = new Array(10000).fill('*');
}

setInterval(() => {
  // Intentionally leaking memory
  leaks.push(new LeakyClass());
  
  const usage = process.memoryUsage();
  console.log(`Heap Used: ${Math.round(usage.heapUsed / 1024 / 1024)} MB`);
}, 1000);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q9:  How do you scale a Node.js application using the Cluster module?

**Difficulty**: Intermediate

**Strategy:**
Node.js runs on a single thread. To utilize multi-core systems:
1. Use the `cluster` module to fork the main process.
2. The master process manages workers.
3. Worker processes handle incoming requests.
4. They share the same TCP connection (port).

**Code Snippet:**
```javascript
const cluster = require('cluster');
const http = require('http');
const numCPUs = require('os').cpus().length;

if (cluster.isMaster) {
  console.log(`Master ${process.pid} is running`);

  // Fork workers
  for (let i = 0; i < numCPUs; i++) {
    cluster.fork();
  }

  cluster.on('exit', (worker, code, signal) => {
    console.log(`Worker ${worker.process.pid} died`);
    // Replace dead worker
    cluster.fork();
  });
} else {
  // Workers can share any TCP connection
  http.createServer((req, res) => {
    res.writeHead(200);
    res.end('Hello World\n');
  }).listen(8000);

  console.log(`Worker ${process.pid} started`);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q10:  How do you securely hash passwords using the built-in crypto module?

**Difficulty**: Intermediate

**Strategy:**
Do not use simple hashes like MD5 or SHA-256 for passwords.
1. Use `scrypt` (recommended) or `pbkdf2` which are computationally expensive.
2. Always generate a unique random salt for each password.
3. Store the salt alongside the hash.

**Code Snippet:**
```javascript
const { scrypt, randomBytes, timingSafeEqual } = require('crypto');

function hashPassword(password) {
  return new Promise((resolve, reject) => {
    const salt = randomBytes(16).toString('hex');
    scrypt(password, salt, 64, (err, derivedKey) => {
      if (err) reject(err);
      resolve(salt + ':' + derivedKey.toString('hex'));
    });
  });
}

function verifyPassword(password, storedHash) {
  return new Promise((resolve, reject) => {
    const [salt, key] = storedHash.split(':');
    const keyBuffer = Buffer.from(key, 'hex');
    
    scrypt(password, salt, 64, (err, derivedKey) => {
      if (err) reject(err);
      // Prevent timing attacks
      resolve(timingSafeEqual(keyBuffer, derivedKey));
    });
  });
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q11:  How do you create a CLI tool with Node.js?

**Difficulty**: Intermediate

**Strategy:**
1. Add a shebang line `#!/usr/bin/env node` at the top of your script.
2. Add a `"bin"` field in `package.json` mapping the command name to the file.
3. Use `process.argv` or libraries like `commander` or `yargs` to parse arguments.
4. Run `npm link` to test locally.

**Code Snippet:**
```javascript
#!/usr/bin/env node

const args = process.argv.slice(2);

if (args.length === 0) {
  console.log('Usage: my-cli <name>');
  process.exit(1);
}

console.log(`Hello, ${args[0]}!`);

// package.json
/*
{
  "name": "my-cli",
  "bin": {
    "my-cli": "./index.js"
  }
}
*/
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q12:  How do you process large files line-by-line to keep memory usage low?

**Difficulty**: Intermediate

**Strategy:**
Reading a large file into memory causes crashes.
1. Use `fs.createReadStream` to stream the file.
2. Use `readline` module to process the stream line by line.
3. This keeps memory usage constant regardless of file size.

**Code Snippet:**
```javascript
const fs = require('fs');
const readline = require('readline');

async function processLineByLine(filePath) {
  const fileStream = fs.createReadStream(filePath);

  const rl = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity // Recognize all instances of CR LF
  });

  for await (const line of rl) {
    // Each line in input.txt will be successively available here as `line`.
    console.log(`Line from file: ${line}`);
  }
}

processLineByLine('huge-file.log');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q13:  How do you handle multiple Promises concurrently but fail gracefully if one fails?

**Difficulty**: Intermediate

**Strategy:**
`Promise.all()` rejects immediately if one promise fails.
1. Use `Promise.allSettled()` to wait for all promises to finish, regardless of outcome.
2. Iterate through results to handle `fulfilled` and `rejected` statuses separately.

**Code Snippet:**
```javascript
const p1 = Promise.resolve(42);
const p2 = Promise.reject('Error occurred');
const p3 = new Promise((resolve) => setTimeout(resolve, 100, 'foo'));

Promise.allSettled([p1, p2, p3]).then((results) => {
  results.forEach((result) => {
    if (result.status === 'fulfilled') {
      console.log('Success:', result.value);
    } else {
      console.error('Failed:', result.reason);
    }
  });
});
/* Output:
Success: 42
Failed: Error occurred
Success: foo
*/
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q14:  How do you optimize Node.js performance by caching static assets?

**Difficulty**: Intermediate

**Strategy:**
Serving static files through Node.js is slower than Nginx. If you must use Node:
1. Use a reverse proxy (Nginx) in front for static files (best practice).
2. In Express, use the `maxAge` option in `express.static`.
3. Use in-memory caching (like Redis) for dynamic data, not static files.

**Code Snippet:**
```javascript
const express = require('express');
const app = express();

// Cache static assets for 1 day (in milliseconds)
const oneDay = 1000 * 60 * 60 * 24;

app.use(express.static('public', {
  maxAge: oneDay,
  etag: true // Enable ETag for conditional requests
}));

app.listen(3000);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q15:  How do you use Buffers to manipulate binary data?

**Difficulty**: Intermediate

**Strategy:**
Node.js uses the `Buffer` class to handle binary data (TCP streams, file system operations).
1. `Buffer.alloc(size)` creates a zero-filled buffer.
2. `Buffer.from(array/string)` creates a buffer from data.
3. Use methods like `write`, `toString`, `slice`, and `concat`.

**Code Snippet:**
```javascript
// Create a buffer from a string
const buf = Buffer.from('Hello', 'utf-8');

// Convert to Base64
console.log(buf.toString('base64')); // SGVsbG8=

// Modify data directly
buf[0] = 74; // ASCII for 'J'
console.log(buf.toString()); // Jello

// Concatenate buffers
const buf1 = Buffer.from('Hello ');
const buf2 = Buffer.from('World');
const buf3 = Buffer.concat([buf1, buf2]);
console.log(buf3.toString()); // Hello World
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q16:  How do you handle Implementing JWT authentication?

**Difficulty**: Intermediate

**Strategy:**
Use `jsonwebtoken` library to sign and verify tokens. Sign tokens on login with a secret and expiration. Verify tokens in a middleware for protected routes.

**Code Snippet:**
```javascript
const jwt = require('jsonwebtoken');

function generateToken(user) {
  return jwt.sign({ id: user.id }, process.env.JWT_SECRET, { expiresIn: '1h' });
}

function authenticateToken(req, res, next) {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];
  if (!token) return res.sendStatus(401);

  jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
    if (err) return res.sendStatus(403);
    req.user = user;
    next();
  });
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q17:  How do you handle Rate limiting requests?

**Difficulty**: Intermediate

**Strategy:**
Use a middleware like `express-rate-limit` to limit repeated requests to public APIs and/or endpoints such as password reset. This prevents brute-force attacks and DoS attacks.

**Code Snippet:**
```javascript
const rateLimit = require('express-rate-limit');

const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // Limit each IP to 100 requests per `window` (here, per 15 minutes)
  standardHeaders: true, // Return rate limit info in the `RateLimit-*` headers
  legacyHeaders: false, // Disable the `X-RateLimit-*` headers
});

// Apply the rate limiting middleware to all requests
app.use(limiter);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q18:  How do you handle Using node-postgres vs ORMs?

**Difficulty**: Intermediate

**Strategy:**
Use `node-postgres` (pg) for raw SQL performance and control when you need complex queries optimized manually. Use ORMs (Sequelize, TypeORM, Prisma) for productivity, type safety, and database agnosticism in standard CRUD applications.

**Code Snippet:**
```javascript
const { Pool } = require('pg');
const pool = new Pool();

// Raw SQL with node-postgres
async function getUser(id) {
  const res = await pool.query('SELECT * FROM users WHERE id = $1', [id]);
  return res.rows[0];
}

// vs ORM (e.g., Prisma - conceptual)
// const user = await prisma.user.findUnique({ where: { id } });
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q19:  How do you handle Handling uncaught exceptions?

**Difficulty**: Intermediate

**Strategy:**
Listen to the `uncaughtException` event on the `process` object. Log the error synchronously and perform a graceful shutdown (exit with failure code), as the process state is likely corrupted.

**Code Snippet:**
```javascript
process.on('uncaughtException', (err) => {
  console.error('There was an uncaught error', err);
  // Perform synchronous cleanup (e.g., close file descriptors) if possible
  process.exit(1); // Mandatory (as per Node.js docs)
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q20:  How do you validate API requests using Joi?

**Difficulty**: Intermediate

**Strategy:**
Use `joi` to define schemas for request body, query, or params. Validate before processing.

**Code Snippet:**
```javascript
const Joi = require('joi');

const schema = Joi.object({
    username: Joi.string().alphanum().min(3).max(30).required(),
    email: Joi.string().email().required()
});

// Express middleware example
const validateRequest = (req, res, next) => {
    const { error } = schema.validate(req.body);
    if (error) return res.status(400).send(error.details[0].message);
    next();
};
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q21:  How do you implement structured logging using Winston?

**Difficulty**: Intermediate

**Strategy:**
Use `winston` to create a logger with different transports (Console, File). Use JSON format for easier parsing.

**Code Snippet:**
```javascript
const winston = require('winston');

const logger = winston.createLogger({
  level: 'info',
  format: winston.format.json(),
  transports: [
    new winston.transports.File({ filename: 'error.log', level: 'error' }),
    new winston.transports.File({ filename: 'combined.log' }),
  ],
});

if (process.env.NODE_ENV !== 'production') {
  logger.add(new winston.transports.Console({
    format: winston.format.simple(),
  }));
}

logger.info('Hello distributed log files!');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q22:  How do you handle file uploads using Multer?

**Difficulty**: Intermediate

**Strategy:**
Use `multer` middleware to handle `multipart/form-data`. Configure storage destination and filename.

**Code Snippet:**
```javascript
const multer = require('multer');
const storage = multer.diskStorage({
  destination: (req, file, cb) => cb(null, 'uploads/'),
  filename: (req, file, cb) => cb(null, Date.now() + '-' + file.originalname)
});

const upload = multer({ storage: storage });

// app.post('/upload', upload.single('avatar'), (req, res) => {
//   res.send('File uploaded');
// });
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q23:  How do you use dotenv to manage environment variables?

**Difficulty**: Beginner

**Strategy:**
Use `dotenv` to load variables from `.env` file into `process.env`. Do this as early as possible in your app.

**Code Snippet:**
```javascript
require('dotenv').config();

console.log(process.env.DB_HOST);
console.log(process.env.API_KEY);

// .env file content:
// DB_HOST=localhost
// API_KEY=12345
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q24:  How do you use spawn to run a child process?

**Difficulty**: Intermediate

**Strategy:**
Use `spawn` for long-running processes or when you need to handle large amounts of data via streams. It doesn't buffer the output like `exec`.

**Code Snippet:**
```javascript
const { spawn } = require('child_process');
const ls = spawn('ls', ['-lh', '/usr']);

ls.stdout.on('data', (data) => {
  console.log(`stdout: ${data}`);
});

ls.stderr.on('data', (data) => {
  console.error(`stderr: ${data}`);
});

ls.on('close', (code) => {
  console.log(`child process exited with code ${code}`);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q25:  How do you write a simple unit test with Jest?

**Difficulty**: Beginner

**Strategy:**
Use `describe` to group tests and `test` (or `it`) for individual test cases. Use `expect` for assertions.

**Code Snippet:**
```javascript
// sum.js
function sum(a, b) {
  return a + b;
}
module.exports = sum;

// sum.test.js
const sum = require('./sum');

test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q26:  How do you use AsyncLocalStorage for request context tracking?

**Difficulty**: Advanced

**Strategy:**
Use `AsyncLocalStorage` to store data (like request ID) that stays with the async execution context, avoiding the need to pass it as an argument to every function.

**Code Snippet:**
```javascript
const { AsyncLocalStorage } = require('async_hooks');
const asyncLocalStorage = new AsyncLocalStorage();

const requestIdMiddleware = (req, res, next) => {
  const id = req.headers['x-request-id'] || 'uuid';
  asyncLocalStorage.run(new Map().set('requestId', id), () => {
    next();
  });
};

function logWithId(msg) {
  const store = asyncLocalStorage.getStore();
  const id = store ? store.get('requestId') : 'unknown';
  console.log(`[${id}] ${msg}`);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q27:  How do you Dockerize a Node.js application?

**Difficulty**: Intermediate

**Strategy:**
Create a `Dockerfile`. Use a lightweight base image (alpine). Copy `package.json` first to leverage caching.

**Code Snippet:**
```javascript
# Dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm ci --only=production

COPY . .

EXPOSE 3000
CMD ["node", "server.js"]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q28:  How do you use the path module to handle file paths cross-platform?

**Difficulty**: Beginner

**Strategy:**
Use `path.join()` to create paths that work on both Windows and Unix. Use `path.resolve()` to get absolute paths.

**Code Snippet:**
```javascript
const path = require('path');

// Correct way to join paths
const configPath = path.join(__dirname, 'config', 'app.json');
// On Windows: ...\config\app.json
// On Linux: .../config/app.json

const absolutePath = path.resolve('static');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q29:  What is the difference between `process.nextTick` and `setImmediate`?

**Difficulty**: Advanced

**Strategy:**
`process.nextTick` fires immediately after the current operation completes (before the Event Loop continues). `setImmediate` fires in the 'Check' phase of the next Event Loop iteration.

**Code Example:**
```javascript
console.log('Start');

setImmediate(() => {
  console.log('setImmediate');
});

process.nextTick(() => {
  console.log('nextTick');
});

console.log('End');

// Output:
// Start
// End
// nextTick
// setImmediate
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q30:  How do you safely spawn a child process?

**Difficulty**: Intermediate

**Strategy:**
Use `child_process.spawn` for long-running processes or large output. It streams data instead of buffering it (unlike `exec`), preventing memory overflows.

**Code Example:**
```javascript
const { spawn } = require('child_process');

const child = spawn('ls', ['-lh', '/usr']);

child.stdout.on('data', (data) => {
  console.log(`stdout: ${data}`);
});

child.stderr.on('data', (data) => {
  console.error(`stderr: ${data}`);
});

child.on('close', (code) => {
  console.log(`child process exited with code ${code}`);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q31:  How do you handle unhandled promise rejections globally?

**Difficulty**: Intermediate

**Strategy:**
Listen for the `unhandledRejection` event on the `process` object. This is crucial for preventing silent failures in async code.

**Code Example:**
```javascript
process.on('unhandledRejection', (reason, promise) => {
  console.error('Unhandled Rejection at:', promise, 'reason:', reason);
  // Application specific logging, throwing an error, or other logic here
  process.exit(1); // Recommended to restart the process
});

Promise.reject(new Error('Fail!'));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q32:  How do you optimize garbage collection in Node.js?

**Difficulty**: Advanced

**Strategy:**
Use flags like `--max-old-space-size` to increase heap limit. Monitor GC with `--trace-gc`. Avoid memory leaks (global variables, closures, uncleared timers).

**Code Example:**
```javascript
// Run with: node --max-old-space-size=4096 index.js

// In code, avoid retaining references unnecessarily
let cache = {};

function addToCache(key, value) {
    cache[key] = value;
    
    // Implement cleanup strategy
    if (Object.keys(cache).length > 1000) {
        delete cache[Object.keys(cache)[0]];
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q33:  How do you use Buffers safely?

**Difficulty**: Intermediate

**Strategy:**
Use `Buffer.from()` or `Buffer.alloc()` instead of `new Buffer()` (which is deprecated/unsafe). `Buffer.allocUnsafe()` is faster but contains uninitialized memory.

**Code Example:**
```javascript
// Safe allocation (zero-filled)
const buf1 = Buffer.alloc(10);

// From string
const buf2 = Buffer.from('Hello World', 'utf8');

// Convert back to string
console.log(buf2.toString('hex')); // 48656c6c6f20576f726c64
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q34:  How do you debug a Node.js application with the Inspector?

**Difficulty**: Beginner

**Strategy:**
Run node with `--inspect` or `--inspect-brk` (to break at start). Connect via Chrome DevTools (chrome://inspect) or VS Code.

**Code Example:**
```javascript
// Command line:
// node --inspect index.js

// Or inside code (programmatic breakpoint):
debugger;
console.log('Paused here if inspector is attached');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q35:  How do you create a secure HTTPS server?

**Difficulty**: Intermediate

**Strategy:**
Use the `https` module and provide `key` and `cert` options (from SSL certificates).

**Code Example:**
```javascript
const https = require('https');
const fs = require('fs');

const options = {
  key: fs.readFileSync('key.pem'),
  cert: fs.readFileSync('cert.pem')
};

https.createServer(options, (req, res) => {
  res.writeHead(200);
  res.end('hello world\n');
}).listen(8000);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q36:  How do you use `util.promisify` to convert callback-based functions?

**Difficulty**: Beginner

**Strategy:**
`util.promisify` converts a function following the common error-first callback style (err, value) into a function that returns a Promise.

**Code Example:**
```javascript
const util = require('util');
const fs = require('fs');

const readFile = util.promisify(fs.readFile);

async function read() {
  try {
    const data = await readFile('/etc/passwd', 'utf8');
    console.log(data);
  } catch (err) {
    console.error(err);
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q37:  How do you parse large JSON files without blocking the event loop?

**Difficulty**: Advanced

**Strategy:**
Use a streaming JSON parser (like `stream-json`) or run the parsing in a Worker Thread. `JSON.parse` is synchronous and blocks the main thread.

**Code Example:**
```javascript
const { Worker, isMainThread, parentPort, workerData } = require('worker_threads');

if (isMainThread) {
  const worker = new Worker(__filename, { workerData: '{"large": "json"}' });
  worker.on('message', msg => console.log(msg));
} else {
  const json = JSON.parse(workerData);
  parentPort.postMessage(json);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q38:  How do you implement a simple rate limiter using Redis?

**Difficulty**: Advanced

**Strategy:**
Use Redis `INCR` and `EXPIRE`. Increment a key for the user IP. If it's 1, set expiration. If value > limit, block request.

**Code Example:**
```javascript
const redis = require('redis');
const client = redis.createClient();

async function rateLimit(ip) {
    const key = `rate:${ip}`;
    const requests = await client.incr(key);
    
    if (requests === 1) {
        await client.expire(key, 60); // 1 minute window
    }
    
    if (requests > 100) {
        throw new Error('Rate limit exceeded');
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q39:  How do you use `vm` module to run untrusted code (Sandboxing)?

**Difficulty**: Advanced

**Strategy:**
The `vm` module allows compiling and running code within V8 contexts. However, it is NOT secure against all attacks; use dedicated sandboxing libraries or Docker for true isolation.

**Code Example:**
```javascript
const vm = require('vm');

const x = 1;
const context = { x: 2 };
vm.createContext(context); // Contextify the object

const code = 'x += 40; var y = 17;';
vm.runInContext(code, context);

console.log(context.x); // 42
console.log(context.y); // 17
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q40:  How do you prevent blocking the Event Loop with cryptographic operations?

**Difficulty**: Intermediate

**Strategy:**
Use the asynchronous versions of crypto functions (e.g., `crypto.pbkdf2` instead of `crypto.pbkdf2Sync`). These run in the Libuv thread pool.

**Code Example:**
```javascript
const crypto = require('crypto');

// Async (Good)
crypto.pbkdf2('secret', 'salt', 100000, 64, 'sha512', (err, derivedKey) => {
  if (err) throw err;
  console.log(derivedKey.toString('hex'));
});

// Sync (Bad - blocks)
// const key = crypto.pbkdf2Sync('secret', 'salt', 100000, 64, 'sha512');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q41:  How do you use `require.resolve`?

**Difficulty**: Beginner

**Strategy:**
`require.resolve` returns the full path of a module without loading it. Useful for checking existence or loading resources relative to a module.

**Code Example:**
```javascript
try {
  const path = require.resolve('express');
  console.log('Express found at:', path);
} catch (e) {
  console.log('Express not installed');
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q42:  How do you implement simple middleware in pure Node.js?

**Difficulty**: Intermediate

**Strategy:**
Create a chain of functions where each calls the next. This mimics Express/Connect middleware pattern.

**Code Example:**
```javascript
const middlewares = [
  (req, res, next) => { console.log('Log'); next(); },
  (req, res, next) => { res.end('Hello'); }
];

function run(req, res) {
  let i = 0;
  function next() {
    const mw = middlewares[i++];
    if (mw) mw(req, res, next);
  }
  next();
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q43:  How do you use the `repl` module to create a custom shell?

**Difficulty**: Intermediate

**Strategy:**
The `repl` module allows creating a Read-Eval-Print-Loop. You can expose custom contexts and commands.

**Code Example:**
```javascript
const repl = require('repl');

const r = repl.start('> ');

// Expose function to REPL context
r.context.sayHello = (name) => `Hello ${name}`;

// User can type: sayHello('Alice')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q44:  How do you benchmark Node.js code using `perf_hooks`?

**Difficulty**: Intermediate

**Strategy:**
Use `performance.now()` or `performance.measure()` for high-resolution timing.

**Code Example:**
```javascript
const { performance, PerformanceObserver } = require('perf_hooks');

const obs = new PerformanceObserver((items) => {
  console.log(items.getEntries()[0].duration);
  performance.clearMarks();
});
obs.observe({ entryTypes: ['measure'] });

performance.mark('A');
// Do work
performance.mark('B');
performance.measure('A to B', 'A', 'B');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


### Q45:  How do you serve static files without a framework?

**Difficulty**: Intermediate

**Strategy:**
Read the file using `fs` and write to `res`. Handle MIME types and 404s manually.

**Code Example:**
```javascript
const http = require('http');
const fs = require('fs');
const path = require('path');

http.createServer((req, res) => {
  const filePath = path.join(__dirname, req.url === '/' ? 'index.html' : req.url);
  const ext = path.extname(filePath);
  
  fs.readFile(filePath, (err, content) => {
    if (err) {
      res.writeHead(404);
      res.end('Not Found');
    } else {
      res.writeHead(200, { 'Content-Type': 'text/html' }); // Simplified
      res.end(content);
    }
  });
}).listen(8080);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---

### Q{}: How do you use `fs.promises` for async file operations?

**Difficulty**: Beginner

**Strategy:**
Node.js provides `fs.promises` (or `require('fs/promises')`) to perform file system operations using Promises, allowing cleaner code with `async/await` compared to callbacks.

**Code Snippet:**
```javascript
const fs = require('fs/promises');

async function readConfig() {
  try {
    const data = await fs.readFile('./config.json', 'utf8');
    const config = JSON.parse(data);
    console.log(config);
  } catch (err) {
    console.error('Error reading config:', err);
  }
}

readConfig();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q{}: How do you implement a simple health check endpoint?

**Difficulty**: Beginner

**Strategy:**
A health check endpoint (usually `/health` or `/status`) returns a 200 OK status if the server is running. It can also check DB connectivity or other dependencies.

**Code Snippet:**
```javascript
const express = require('express');
const app = express();

app.get('/health', async (req, res) => {
  const healthcheck = {
    uptime: process.uptime(),
    message: 'OK',
    timestamp: Date.now()
  };
  
  try {
    // Optional: Check DB connection here
    // await db.ping();
    res.send(healthcheck);
  } catch (error) {
    healthcheck.message = error;
    res.status(503).send(healthcheck);
  }
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q{}: How do you use `AbortController` to cancel async operations?

**Difficulty**: Intermediate

**Strategy:**
Since Node.js v15, `AbortController` is globally available. It allows you to abort promise-based APIs (like `fetch` or timers) or your own async logic.

**Code Snippet:**
```javascript
const controller = new AbortController();
const { signal } = controller;

async function doWork() {
  try {
    await new Promise((resolve, reject) => {
      const timeout = setTimeout(resolve, 5000);
      signal.addEventListener('abort', () => {
        clearTimeout(timeout);
        reject(new Error('Operation aborted'));
      });
    });
  } catch (err) {
    if (err.message === 'Operation aborted') {
      console.log('Work was cancelled');
    } else {
      throw err;
    }
  }
}

doWork();
// Cancel after 1 second
setTimeout(() => controller.abort(), 1000);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q{}: How do you inspect heap snapshots programmatically using `v8` module?

**Difficulty**: Advanced

**Strategy:**
The `v8` module allows you to write heap snapshots to disk programmatically. This is useful for debugging memory leaks in production when triggered by a signal or specific condition.

**Code Snippet:**
```javascript
const v8 = require('v8');
const path = require('path');

function takeSnapshot() {
  const fileName = path.join(__dirname, `heap-${Date.now()}.heapsnapshot`);
  v8.writeHeapSnapshot(fileName);
  console.log(`Heap snapshot written to ${fileName}`);
}

// Trigger on high memory usage (example logic)
const usage = process.memoryUsage();
if (usage.heapUsed > 500 * 1024 * 1024) { // 500MB
  takeSnapshot();
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q{}: How do you use the native Node.js Test Runner?

**Difficulty**: Beginner

**Strategy:**
Since Node.js v18 (stable in v20), there is a built-in test runner (`node:test`). It supports `describe`, `it`, `test`, and mocking, reducing the need for external libraries like Jest for simple projects.

**Code Snippet:**
```javascript
const { test, describe, it } = require('node:test');
const assert = require('node:assert');

function add(a, b) { return a + b; }

describe('Math operations', () => {
  it('should add two numbers', () => {
    assert.strictEqual(add(2, 3), 5);
  });

  test('async test', async () => {
    const result = await Promise.resolve(42);
    assert.strictEqual(result, 42);
  });
});
// Run with: node --test file.js
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>
### Q46: What are the security implications of Node.js in real-time systems?

**Difficulty**: Intermediate

**Strategy**:
Validate all inputs. Sanitize data. Use least privilege principle.

**Code Example**:
```javascript
// Sanitize input
const clean = input.replace(/<script>/g, '');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q47: How do you debug Node.js memory leaks in distributed systems?

**Difficulty**: Advanced

**Strategy**:
Use heap snapshots and look for detached DOM nodes or uncleared listeners.

**Code Example**:
```javascript
// Check listeners
process.on('exit', () => cleanup());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q48: Best practices for Node.js code organization in high-traffic sites?

**Difficulty**: Beginner

**Strategy**:
Follow SOLID principles. Keep functions small and focused.

**Code Example**:
```javascript
// Single responsibility
function doOneThing() { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q49: How do you implement Node.js error handling for embedded systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```javascript
try {
  await Node.jsOperation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q50: How do you test Node.js functionality in production environments?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```javascript
test('Node.js works', () => {
  expect(Node.js()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q51: How do you handle Node.js state management in large scale applications?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```javascript
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q52: How do you perform Node.js data validation in microservices?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```javascript
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q53: How do you automate Node.js deployment for mobile devices?

**Difficulty**: Advanced

**Strategy**:
Use CI/CD pipelines. Dockerize the application.

**Code Example**:
```javascript
steps:
  - run: npm test
  - run: docker build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q54: How do you handle Node.js concurrency issues in legacy systems?

**Difficulty**: Advanced

**Strategy**:
Use locks, queues, or atomic operations.

**Code Example**:
```javascript
await mutex.runExclusive(async () => {
  // critical section
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q55: How do you implement Node.js caching in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Use Redis or in-memory LRU caches.

**Code Example**:
```javascript
const cache = new Map();
if (cache.has(key)) return cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q56: How do you manage Node.js configuration for real-time systems?

**Difficulty**: Beginner

**Strategy**:
Use environment variables or config files.

**Code Example**:
```javascript
const config = process.env.CONFIG || 'default';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q57: How do you handle Node.js internationalization (i18n) in distributed systems?

**Difficulty**: Intermediate

**Strategy**:
Use i18n libraries. Extract strings to resource files.

**Code Example**:
```javascript
t('welcome_message')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q58: How do you ensure Node.js accessibility (a11y) in high-traffic sites?

**Difficulty**: Beginner

**Strategy**:
Use semantic HTML and ARIA roles.

**Code Example**:
```javascript
<button aria-label="Close">X</button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q59: How do you optimize Node.js network requests in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use batching, debouncing, or GraphQL.

**Code Example**:
```javascript
debounce(() => fetch(), 300);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q60: How do you handle Node.js performance optimization for production environments?

**Difficulty**: Advanced

**Strategy**:
Profile first, then optimize hot paths. Use caching and efficient algorithms.

**Code Example**:
```javascript
const start = performance.now();
// Node.js logic
const end = performance.now();
console.log('Time:', end - start);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q61: What are the security implications of Node.js in large scale applications?

**Difficulty**: Intermediate

**Strategy**:
Validate all inputs. Sanitize data. Use least privilege principle.

**Code Example**:
```javascript
// Sanitize input
const clean = input.replace(/<script>/g, '');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q62: How do you debug Node.js memory leaks in microservices?

**Difficulty**: Advanced

**Strategy**:
Use heap snapshots and look for detached DOM nodes or uncleared listeners.

**Code Example**:
```javascript
// Check listeners
process.on('exit', () => cleanup());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q63: Best practices for Node.js code organization in mobile devices?

**Difficulty**: Beginner

**Strategy**:
Follow SOLID principles. Keep functions small and focused.

**Code Example**:
```javascript
// Single responsibility
function doOneThing() { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q64: How do you implement Node.js error handling for legacy systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```javascript
try {
  await Node.jsOperation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q65: How do you test Node.js functionality in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```javascript
test('Node.js works', () => {
  expect(Node.js()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q66: How do you handle Node.js state management in real-time systems?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```javascript
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q67: How do you perform Node.js data validation in distributed systems?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```javascript
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q68: How do you automate Node.js deployment for high-traffic sites?

**Difficulty**: Advanced

**Strategy**:
Use CI/CD pipelines. Dockerize the application.

**Code Example**:
```javascript
steps:
  - run: npm test
  - run: docker build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q69: How do you handle Node.js concurrency issues in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use locks, queues, or atomic operations.

**Code Example**:
```javascript
await mutex.runExclusive(async () => {
  // critical section
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q70: How do you implement Node.js caching in production environments?

**Difficulty**: Intermediate

**Strategy**:
Use Redis or in-memory LRU caches.

**Code Example**:
```javascript
const cache = new Map();
if (cache.has(key)) return cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q71: How do you manage Node.js configuration for large scale applications?

**Difficulty**: Beginner

**Strategy**:
Use environment variables or config files.

**Code Example**:
```javascript
const config = process.env.CONFIG || 'default';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q72: How do you handle Node.js internationalization (i18n) in microservices?

**Difficulty**: Intermediate

**Strategy**:
Use i18n libraries. Extract strings to resource files.

**Code Example**:
```javascript
t('welcome_message')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q73: How do you ensure Node.js accessibility (a11y) in mobile devices?

**Difficulty**: Beginner

**Strategy**:
Use semantic HTML and ARIA roles.

**Code Example**:
```javascript
<button aria-label="Close">X</button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q74: How do you optimize Node.js network requests in legacy systems?

**Difficulty**: Advanced

**Strategy**:
Use batching, debouncing, or GraphQL.

**Code Example**:
```javascript
debounce(() => fetch(), 300);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q75: How do you handle Node.js performance optimization for cloud infrastructure?

**Difficulty**: Advanced

**Strategy**:
Profile first, then optimize hot paths. Use caching and efficient algorithms.

**Code Example**:
```javascript
const start = performance.now();
// Node.js logic
const end = performance.now();
console.log('Time:', end - start);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q76: What are the security implications of Node.js in real-time systems?

**Difficulty**: Intermediate

**Strategy**:
Validate all inputs. Sanitize data. Use least privilege principle.

**Code Example**:
```javascript
// Sanitize input
const clean = input.replace(/<script>/g, '');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q77: How do you debug Node.js memory leaks in distributed systems?

**Difficulty**: Advanced

**Strategy**:
Use heap snapshots and look for detached DOM nodes or uncleared listeners.

**Code Example**:
```javascript
// Check listeners
process.on('exit', () => cleanup());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q78: Best practices for Node.js code organization in high-traffic sites?

**Difficulty**: Beginner

**Strategy**:
Follow SOLID principles. Keep functions small and focused.

**Code Example**:
```javascript
// Single responsibility
function doOneThing() { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q79: How do you implement Node.js error handling for embedded systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```javascript
try {
  await Node.jsOperation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q80: How do you test Node.js functionality in production environments?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```javascript
test('Node.js works', () => {
  expect(Node.js()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q81: How do you handle Node.js state management in large scale applications?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```javascript
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q82: How do you perform Node.js data validation in microservices?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```javascript
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q83: How do you automate Node.js deployment for mobile devices?

**Difficulty**: Advanced

**Strategy**:
Use CI/CD pipelines. Dockerize the application.

**Code Example**:
```javascript
steps:
  - run: npm test
  - run: docker build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q84: How do you handle Node.js concurrency issues in legacy systems?

**Difficulty**: Advanced

**Strategy**:
Use locks, queues, or atomic operations.

**Code Example**:
```javascript
await mutex.runExclusive(async () => {
  // critical section
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q85: How do you implement Node.js caching in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Use Redis or in-memory LRU caches.

**Code Example**:
```javascript
const cache = new Map();
if (cache.has(key)) return cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q86: How do you manage Node.js configuration for real-time systems?

**Difficulty**: Beginner

**Strategy**:
Use environment variables or config files.

**Code Example**:
```javascript
const config = process.env.CONFIG || 'default';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q87: How do you handle Node.js internationalization (i18n) in distributed systems?

**Difficulty**: Intermediate

**Strategy**:
Use i18n libraries. Extract strings to resource files.

**Code Example**:
```javascript
t('welcome_message')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q88: How do you ensure Node.js accessibility (a11y) in high-traffic sites?

**Difficulty**: Beginner

**Strategy**:
Use semantic HTML and ARIA roles.

**Code Example**:
```javascript
<button aria-label="Close">X</button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q89: How do you optimize Node.js network requests in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use batching, debouncing, or GraphQL.

**Code Example**:
```javascript
debounce(() => fetch(), 300);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q90: How do you handle Node.js performance optimization for production environments?

**Difficulty**: Advanced

**Strategy**:
Profile first, then optimize hot paths. Use caching and efficient algorithms.

**Code Example**:
```javascript
const start = performance.now();
// Node.js logic
const end = performance.now();
console.log('Time:', end - start);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q91: What are the security implications of Node.js in large scale applications?

**Difficulty**: Intermediate

**Strategy**:
Validate all inputs. Sanitize data. Use least privilege principle.

**Code Example**:
```javascript
// Sanitize input
const clean = input.replace(/<script>/g, '');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q92: How do you debug Node.js memory leaks in microservices?

**Difficulty**: Advanced

**Strategy**:
Use heap snapshots and look for detached DOM nodes or uncleared listeners.

**Code Example**:
```javascript
// Check listeners
process.on('exit', () => cleanup());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q93: Best practices for Node.js code organization in mobile devices?

**Difficulty**: Beginner

**Strategy**:
Follow SOLID principles. Keep functions small and focused.

**Code Example**:
```javascript
// Single responsibility
function doOneThing() { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q94: How do you implement Node.js error handling for legacy systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```javascript
try {
  await Node.jsOperation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q95: How do you test Node.js functionality in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```javascript
test('Node.js works', () => {
  expect(Node.js()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q96: How do you handle Node.js state management in real-time systems?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```javascript
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q97: How do you perform Node.js data validation in distributed systems?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```javascript
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q98: How do you automate Node.js deployment for high-traffic sites?

**Difficulty**: Advanced

**Strategy**:
Use CI/CD pipelines. Dockerize the application.

**Code Example**:
```javascript
steps:
  - run: npm test
  - run: docker build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q99: How do you handle Node.js concurrency issues in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use locks, queues, or atomic operations.

**Code Example**:
```javascript
await mutex.runExclusive(async () => {
  // critical section
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q100: How do you implement Node.js caching in production environments?

**Difficulty**: Intermediate

**Strategy**:
Use Redis or in-memory LRU caches.

**Code Example**:
```javascript
const cache = new Map();
if (cache.has(key)) return cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---
