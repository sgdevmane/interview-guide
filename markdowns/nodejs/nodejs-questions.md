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
46. [How do you use `fs.promises` for async file operations?](#q46) <span class="beginner">Beginner</span>
47. [How do you implement a simple health check endpoint?](#q47) <span class="beginner">Beginner</span>
48. [How do you use `AbortController` to cancel async operations?](#q48) <span class="intermediate">Intermediate</span>
49. [How do you inspect heap snapshots programmatically using `v8` module?](#q49) <span class="advanced">Advanced</span>
50. [How do you use the native Node.js Test Runner?](#q50) <span class="beginner">Beginner</span>
51. [Explain the Node.js Event Loop phases.](#q51-explain-the-node.js-event-loop-phases.) <span class="advanced">Advanced</span>
52. [Difference between `process.nextTick` and `setImmediate`?](#q52-difference-between-process.nexttick-and-setimmediate) <span class="intermediate">Intermediate</span>
53. [How do Worker Threads differ from Cluster module?](#q53-how-do-worker-threads-differ-from-cluster-module) <span class="advanced">Advanced</span>
54. [How do you handle Backpressure in Streams?](#q54-how-do-you-handle-backpressure-in-streams) <span class="advanced">Advanced</span>
55. [How do you debug a memory leak in Node.js?](#q55-how-do-you-debug-a-memory-leak-in-node.js) <span class="advanced">Advanced</span>
56. [What is the Buffer class?](#q56-what-is-the-buffer-class) <span class="beginner">Beginner</span>
57. [How do you implement a custom Transform stream?](#q57-how-do-you-implement-a-custom-transform-stream) <span class="advanced">Advanced</span>
58. [How do you handle uncaught exceptions?](#q58-how-do-you-handle-uncaught-exceptions) <span class="intermediate">Intermediate</span>
59. [What is libuv?](#q59-what-is-libuv) <span class="advanced">Advanced</span>
60. [How do you secure a Node.js app?](#q60-how-do-you-secure-a-node.js-app) <span class="intermediate">Intermediate</span>
61. [Difference between `spawn` and `exec`?](#q61-difference-between-spawn-and-exec) <span class="intermediate">Intermediate</span>
62. [How do you implement a graceful shutdown?](#q62-how-do-you-implement-a-graceful-shutdown) <span class="intermediate">Intermediate</span>
63. [How do you use `util.promisify`?](#q63-how-do-you-use-util.promisify) <span class="beginner">Beginner</span>
64. [What is middleware in Express?](#q64-what-is-middleware-in-express) <span class="beginner">Beginner</span>
65. [How do you handle file uploads in Node?](#q65-how-do-you-handle-file-uploads-in-node) <span class="intermediate">Intermediate</span>
66. [How do you implement JWT authentication?](#q66-how-do-you-implement-jwt-authentication) <span class="intermediate">Intermediate</span>
67. [How do you optimize Node.js performance?](#q67-how-do-you-optimize-node.js-performance) <span class="advanced">Advanced</span>
68. [What is the purpose of `package-lock.json`?](#q68-what-is-the-purpose-of-package-lock.json) <span class="beginner">Beginner</span>
69. [How do you implement logging?](#q69-how-do-you-implement-logging) <span class="intermediate">Intermediate</span>
70. [How do you use Environment Variables?](#q70-how-do-you-use-environment-variables) <span class="beginner">Beginner</span>
71. [How do you handle CORS?](#q71-how-do-you-handle-cors) <span class="beginner">Beginner</span>
72. [How do you make an HTTP request?](#q72-how-do-you-make-an-http-request) <span class="beginner">Beginner</span>
73. [What is the Cluster module?](#q73-what-is-the-cluster-module) <span class="advanced">Advanced</span>
74. [How do you implement API rate limiting?](#q74-how-do-you-implement-api-rate-limiting) <span class="intermediate">Intermediate</span>
75. [How do you parse JSON?](#q75-how-do-you-parse-json) <span class="beginner">Beginner</span>
76. [How do you implement a WebSocket server?](#q76-how-do-you-implement-a-websocket-server) <span class="intermediate">Intermediate</span>
77. [What is REPL?](#q77-what-is-repl) <span class="beginner">Beginner</span>
78. [How do you profile a Node app?](#q78-how-do-you-profile-a-node-app) <span class="advanced">Advanced</span>
79. [How do you manage configuration?](#q79-how-do-you-manage-configuration) <span class="intermediate">Intermediate</span>
80. [How do you schedule tasks?](#q80-how-do-you-schedule-tasks) <span class="intermediate">Intermediate</span>
81. [How do you write unit tests?](#q81-how-do-you-write-unit-tests) <span class="beginner">Beginner</span>
82. [How do you handle large JSON payloads?](#q82-how-do-you-handle-large-json-payloads) <span class="intermediate">Intermediate</span>
83. [How do you use async/await with callbacks?](#q83-how-do-you-use-asyncawait-with-callbacks) <span class="intermediate">Intermediate</span>
84. [What is `require.resolve`?](#q84-what-is-require.resolve) <span class="advanced">Advanced</span>
85. [How do you implement a health check endpoint?](#q85-how-do-you-implement-a-health-check-endpoint) <span class="beginner">Beginner</span>
86. [How do you compress HTTP responses?](#q86-how-do-you-compress-http-responses) <span class="beginner">Beginner</span>
87. [How do you protect against NoSQL Injection?](#q87-how-do-you-protect-against-nosql-injection) <span class="intermediate">Intermediate</span>
88. [How do you implement role-based access control?](#q88-how-do-you-implement-role-based-access-control) <span class="intermediate">Intermediate</span>
89. [How do you use `EventEmitter`?](#q89-how-do-you-use-eventemitter) <span class="beginner">Beginner</span>
90. [How do you debug async code?](#q90-how-do-you-debug-async-code) <span class="intermediate">Intermediate</span>
91. [How do you serve static files?](#q91-how-do-you-serve-static-files) <span class="beginner">Beginner</span>
92. [How do you implement request validation?](#q92-how-do-you-implement-request-validation) <span class="intermediate">Intermediate</span>
93. [How do you mock dependencies in tests?](#q93-how-do-you-mock-dependencies-in-tests) <span class="intermediate">Intermediate</span>
94. [How do you handle timezones?](#q94-how-do-you-handle-timezones) <span class="intermediate">Intermediate</span>
95. [How do you implement hot reload?](#q95-how-do-you-implement-hot-reload) <span class="beginner">Beginner</span>
96. [How do you use MongoDB with Node?](#q96-how-do-you-use-mongodb-with-node) <span class="beginner">Beginner</span>
97. [How do you implement redis caching?](#q97-how-do-you-implement-redis-caching) <span class="intermediate">Intermediate</span>
98. [How do you handle sticky sessions?](#q98-how-do-you-handle-sticky-sessions) <span class="advanced">Advanced</span>
99. [How do you implement OAuth?](#q99-how-do-you-implement-oauth) <span class="intermediate">Intermediate</span>
100. [How do you parse command line arguments?](#q100-how-do-you-parse-command-line-arguments) <span class="beginner">Beginner</span>

---

<a id="q1"></a>
### Q1: How do you handle backpressure in a Node.js stream pipeline?

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


<a id="q2"></a>
### Q2: How do you offload CPU-intensive tasks using Worker Threads?

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


<a id="q3"></a>
### Q3: How do you implement a custom Transform stream to modify data on the fly?

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


<a id="q4"></a>
### Q4: How do you handle errors in async/await middleware in Express?

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


<a id="q5"></a>
### Q5: How do you implement graceful shutdown in a Node.js server?

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


<a id="q6"></a>
### Q6: How do you prevent prototype pollution in Node.js applications?

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


<a id="q7"></a>
### Q7: How do you migrate from CommonJS to ES Modules (ESM) in Node.js?

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


<a id="q8"></a>
### Q8: How do you debug memory leaks in Node.js?

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


<a id="q9"></a>
### Q9: How do you scale a Node.js application using the Cluster module?

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


<a id="q10"></a>
### Q10: How do you securely hash passwords using the built-in crypto module?

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


<a id="q11"></a>
### Q11: How do you create a CLI tool with Node.js?

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


<a id="q12"></a>
### Q12: How do you process large files line-by-line to keep memory usage low?

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


<a id="q13"></a>
### Q13: How do you handle multiple Promises concurrently but fail gracefully if one fails?

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


<a id="q14"></a>
### Q14: How do you optimize Node.js performance by caching static assets?

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


<a id="q15"></a>
### Q15: How do you use Buffers to manipulate binary data?

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


<a id="q16"></a>
### Q16: How do you handle Implementing JWT authentication?

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


<a id="q17"></a>
### Q17: How do you handle Rate limiting requests?

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


<a id="q18"></a>
### Q18: How do you handle Using node-postgres vs ORMs?

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


<a id="q19"></a>
### Q19: How do you handle Handling uncaught exceptions?

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


<a id="q20"></a>
### Q20: How do you validate API requests using Joi?

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


<a id="q21"></a>
### Q21: How do you implement structured logging using Winston?

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


<a id="q22"></a>
### Q22: How do you handle file uploads using Multer?

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


<a id="q23"></a>
### Q23: How do you use dotenv to manage environment variables?

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


<a id="q24"></a>
### Q24: How do you use spawn to run a child process?

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


<a id="q25"></a>
### Q25: How do you write a simple unit test with Jest?

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


<a id="q26"></a>
### Q26: How do you use AsyncLocalStorage for request context tracking?

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


<a id="q27"></a>
### Q27: How do you Dockerize a Node.js application?

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


<a id="q28"></a>
### Q28: How do you use the path module to handle file paths cross-platform?

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


<a id="q29"></a>
### Q29: What is the difference between `process.nextTick` and `setImmediate`?

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


<a id="q30"></a>
### Q30: How do you safely spawn a child process?

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


<a id="q31"></a>
### Q31: How do you handle unhandled promise rejections globally?

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
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q32"></a>
### Q32: How do you optimize garbage collection in Node.js?

**Difficulty**: Advanced

**Strategy**:
Use flags like `--max-old-space-size` to increase heap limit. Use `--optimize_for_size` for smaller memory footprint. Avoid global variables and closures that retain large objects.

**Code Example**:
```bash
node --max-old-space-size=4096 server.js
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q33"></a>
### Q33: How do you use Buffers safely?

**Difficulty**: Intermediate

**Strategy**:
Use `Buffer.alloc()` (initializes with zeros) instead of `Buffer.allocUnsafe()` (contains old memory data) unless performance is critical and you immediately overwrite it.

**Code Example**:
```javascript
// Safe
const buf = Buffer.alloc(1024);

// Unsafe (faster, but potential security risk)
const unsafeBuf = Buffer.allocUnsafe(1024);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q34"></a>
### Q34: How do you debug a Node.js application with the Inspector?

**Difficulty**: Beginner

**Strategy**:
Start Node with `--inspect` or `--inspect-brk` (breaks on first line). Open Chrome and go to `chrome://inspect`.

**Code Example**:
```bash
node --inspect-brk server.js
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q35"></a>
### Q35: How do you create a secure HTTPS server?

**Difficulty**: Intermediate

**Strategy**:
Use the `https` module. You need an SSL certificate (key and cert files).

**Code Example**:
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
}).listen(443);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q36"></a>
### Q36: How do you use `util.promisify` to convert callback-based functions?

**Difficulty**: Beginner

**Strategy**:
`util.promisify` converts a function that accepts a callback (err, value) into a function that returns a Promise.

**Code Example**:
```javascript
const util = require('util');
const fs = require('fs');
const readFile = util.promisify(fs.readFile);

async function read() {
  const data = await readFile('test.txt', 'utf8');
  console.log(data);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q37"></a>
### Q37: How do you parse large JSON files without blocking the event loop?

**Difficulty**: Advanced

**Strategy**:
Use a streaming JSON parser like `stream-json` or `bfj` instead of `JSON.parse()` which is synchronous and blocks the loop for large strings.

**Code Example**:
```javascript
const { parser } = require('stream-json');
const fs = require('fs');

fs.createReadStream('large.json')
  .pipe(parser())
  .on('data', data => console.log(data));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q38"></a>
### Q38: How do you implement a simple rate limiter using Redis?

**Difficulty**: Advanced

**Strategy**:
Use Redis `INCR` and `EXPIRE`. Increment a counter for the user's IP. If it exceeds the limit, reject.

**Code Example**:
```javascript
const redis = require('redis');
const client = redis.createClient();

async function rateLimit(ip) {
  const requests = await client.incr(ip);
  if (requests === 1) await client.expire(ip, 60); // 60s window
  
  if (requests > 100) throw new Error('Too many requests');
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q39"></a>
### Q39: How do you use `vm` module to run untrusted code (Sandboxing)?

**Difficulty**: Advanced

**Strategy**:
The `vm` module allows compiling and running code in V8 contexts. However, it is **not secure** for untrusted code. Use `vm2` or isolated processes/containers for real security.

**Code Example**:
```javascript
const vm = require('vm');
const context = { x: 2 };
vm.createContext(context);
vm.runInContext('x += 40; var y = 17;', context);
console.log(context.x); // 42
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q40"></a>
### Q40: How do you prevent blocking the Event Loop with cryptographic operations?

**Difficulty**: Intermediate

**Strategy**:
Use the async versions of `crypto` methods (e.g., `crypto.pbkdf2` instead of `crypto.pbkdf2Sync`). These run in the libuv thread pool.

**Code Example**:
```javascript
const crypto = require('crypto');
// Async - Non-blocking
crypto.pbkdf2('secret', 'salt', 100000, 64, 'sha512', (err, key) => {
  console.log(key.toString('hex'));
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q41"></a>
### Q41: How do you use `require.resolve`?

**Difficulty**: Beginner

**Strategy**:
It returns the absolute filename of a module without loading it. Useful for checking existence or getting paths.

**Code Example**:
```javascript
const path = require.resolve('express');
console.log(path); // /node_modules/express/index.js
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q42"></a>
### Q42: How do you implement simple middleware in pure Node.js?

**Difficulty**: Intermediate

**Strategy**:
Wrap the request handler. Execute logic before calling the next handler.

**Code Example**:
```javascript
const logger = (req, res, next) => {
  console.log(req.method, req.url);
  next();
};

const server = http.createServer((req, res) => {
  logger(req, res, () => {
    res.end('Hello');
  });
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q43"></a>
### Q43: How do you use the `repl` module to create a custom shell?

**Difficulty**: Intermediate

**Strategy**:
Use `repl.start()` to create an interactive shell with custom context.

**Code Example**:
```javascript
const repl = require('repl');
const r = repl.start('> ');
r.context.myFunc = () => console.log('Custom function');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q44"></a>
### Q44: How do you benchmark Node.js code using `perf_hooks`?

**Difficulty**: Intermediate

**Strategy**:
Use `performance.now()` for high-resolution timestamps to measure execution time.

**Code Example**:
```javascript
const { performance } = require('perf_hooks');
const start = performance.now();
// ... operation ...
const end = performance.now();
console.log(`Time: ${end - start}ms`);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q45"></a>
### Q45: How do you serve static files without a framework?

**Difficulty**: Intermediate

**Strategy**:
Read the file using `fs` based on the URL path and write it to the response stream with the correct MIME type.

**Code Example**:
```javascript
const fs = require('fs');
const http = require('http');

http.createServer((req, res) => {
  if (req.url === '/style.css') {
    res.writeHead(200, { 'Content-Type': 'text/css' });
    fs.createReadStream('style.css').pipe(res);
  }
}).listen(3000);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q46"></a>
### Q46: What are the security implications of Node.js in real-time systems?

**Difficulty**: Intermediate

**Strategy**:
Real-time apps (WebSockets) maintain persistent connections. This increases exposure to DoS attacks (exhausting file descriptors). Use rate limiting and connection limits.

**Code Example**:
```javascript
// Pseudo-code for connection limit
if (activeConnections > MAX_CONNECTIONS) {
  socket.destroy();
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q47"></a>
### Q47: How do you debug Node.js memory leaks in distributed systems?

**Difficulty**: Advanced

**Strategy**:
Use APM tools (Datadog, New Relic) or remote heap profiling (e.g., `heapdump` module triggering a snapshot on signal).

**Code Example**:
```javascript
const heapdump = require('heapdump');
process.kill(process.pid, 'SIGUSR2'); // Triggers snapshot
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q48"></a>
### Q48: Best practices for Node.js code organization in high-traffic sites?

**Difficulty**: Beginner

**Strategy**:
Layered Architecture: Controllers (HTTP), Services (Business Logic), Data Access (DB). Keep controllers thin.

**Code Example**:
```javascript
// user.controller.js -> calls userService.js -> calls userRepository.js
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q49"></a>
### Q49: How do you implement Node.js error handling for embedded systems?

**Difficulty**: Intermediate

**Strategy**:
On embedded systems, you can't just crash. Use a supervisor (systemd/PM2) to restart, but also implement a "safe mode" or retry logic for hardware I/O errors.

**Code Example**:
```javascript
try {
  readSensor();
} catch (e) {
  logError(e);
  setTimeout(readSensor, 5000); // Retry
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q50"></a>
### Q50: How do you test Node.js functionality in production environments?

**Difficulty**: Intermediate

**Strategy**:
Use Canary Deployments or Feature Flags. Use "Synthetic Monitoring" (pings critical paths periodically).

**Code Example**:
```javascript
// Health check endpoint that checks DB connection
app.get('/health', async (req, res) => {
  const dbUp = await checkDb();
  res.status(dbUp ? 200 : 500).send();
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q51"></a>
### Q51: Explain the Node.js Event Loop phases.

**Difficulty**: Advanced

**Strategy**:
1. Timers (setTimeout)
2. Pending Callbacks (I/O)
3. Idle, Prepare
4. Poll (New I/O)
5. Check (setImmediate)
6. Close Callbacks

**Code Example**:
```javascript
// Understanding order
setTimeout(() => console.log('Timer'), 0);
setImmediate(() => console.log('Check'));
// 'Check' might run before 'Timer' depending on I/O cycle
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q52"></a>
### Q52: How does the `os` module help in scaling?

**Difficulty**: Intermediate

**Strategy**:
Use `os.cpus().length` to determine how many worker threads or cluster forks to create to maximize CPU usage.

**Code Example**:
```javascript
const os = require('os');
const numCPUs = os.cpus().length;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q53"></a>
### Q53: How do Worker Threads differ from Cluster module?

**Difficulty**: Advanced

**Strategy**:
Cluster: Separate processes (share port, separate memory). Good for HTTP scaling.
Worker Threads: Same process (share memory via SharedArrayBuffer). Good for CPU tasks within an app.

**Code Example**:
```javascript
// Worker Thread sharing memory
const { Worker, isMainThread } = require('worker_threads');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q54"></a>
### Q54: How do you handle Backpressure in Streams?

**Difficulty**: Advanced

**Strategy**:
Use `pipeline` which handles it automatically. If manual, check `write()` return value and wait for `drain`.

**Code Example**:
```javascript
readable.pipe(writable); // Auto-handles backpressure
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q55"></a>
### Q55: How do you use `heapdump`?

**Difficulty**: Advanced

**Strategy**:
Generate a heap snapshot file programmatically to analyze memory usage in Chrome DevTools.

**Code Example**:
```javascript
const heapdump = require('heapdump');
heapdump.writeSnapshot('/var/local/' + Date.now() + '.heapsnapshot');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q56"></a>
### Q56: What is the Buffer class?

**Difficulty**: Beginner

**Strategy**:
A global class to handle raw binary data. Node.js was designed for networking, which requires binary.

**Code Example**:
```javascript
Buffer.from('Hello');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q57"></a>
### Q57: How do you implement a custom Transform stream?

**Difficulty**: Advanced

**Strategy**:
Implement `_transform` and `_flush`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
class MyTransform extends Transform {
  _transform(chunk, enc, cb) {
    this.push(chunk);
    cb();
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q58"></a>
### Q58: How do you handle uncaught exceptions?

**Difficulty**: Intermediate

**Strategy**:
`process.on('uncaughtException')`. Log and exit. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
process.on('uncaughtException', (err) => process.exit(1));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q59"></a>
### Q59: What is libuv?

**Difficulty**: Advanced

**Strategy**:
The C library that provides the Event Loop and async I/O (file system, DNS, network) for Node.js.

**Code Example**:
```javascript
// libuv handles the thread pool for fs operations
fs.readFile(...); 
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q60"></a>
### Q60: How do you secure a Node.js app?

**Difficulty**: Intermediate

**Strategy**:
Helmet (headers), Rate Limit, Input Validation, CORS, no eval.

**Code Example**:
```javascript
app.use(helmet());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q61"></a>
### Q61: Difference between `spawn` and `exec`?

**Difficulty**: Intermediate

**Strategy**:
`spawn`: Returns a stream (good for large data).
`exec`: Buffers output (good for small output, simple commands).

**Code Example**:
```javascript
exec('ls', (err, stdout) => console.log(stdout));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q62"></a>
### Q62: How do you implement a graceful shutdown?

**Difficulty**: Intermediate

**Strategy**:
Handle `SIGTERM`. Close server and DB. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
process.on('SIGTERM', () => server.close());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q63"></a>
### Q63: How do you use `util.promisify`?

**Difficulty**: Beginner

**Strategy**:
Converts callback style to promise style. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const stat = util.promisify(fs.stat);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q64"></a>
### Q64: What is middleware in Express?

**Difficulty**: Beginner

**Strategy**:
Functions that access request/response objects and `next` function.

**Code Example**:
```javascript
app.use((req, res, next) => next());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q65"></a>
### Q65: How do you handle file uploads in Node?

**Difficulty**: Intermediate

**Strategy**:
Use `multer` or `formidable`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const upload = multer({ dest: 'uploads/' });
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q66"></a>
### Q66: How do you implement JWT authentication?

**Difficulty**: Intermediate

**Strategy**:
Sign payload with secret. Send token. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
jwt.sign({ id: 1 }, 'secret');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q67"></a>
### Q67: How do you optimize Node.js performance?

**Difficulty**: Advanced

**Strategy**:
Clustering, Caching, Gzip, Async I/O. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
compression();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q68"></a>
### Q68: What is the purpose of `package-lock.json`?

**Difficulty**: Beginner

**Strategy**:
Locks dependency versions to ensure consistent installs across environments.

**Code Example**:
```json
"dependencies": { "express": { "version": "4.17.1" } }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q69"></a>
### Q69: How do you implement logging?

**Difficulty**: Intermediate

**Strategy**:
Winston or Pino. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
logger.info('message');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q70"></a>
### Q70: How do you use Environment Variables?

**Difficulty**: Beginner

**Strategy**:
`process.env`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const db = process.env.DB_URI;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q71"></a>
### Q71: How do you handle CORS?

**Difficulty**: Beginner

**Strategy**:
`cors` middleware. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
app.use(cors());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q72"></a>
### Q72: How do you make an HTTP request?

**Difficulty**: Beginner

**Strategy**:
`fetch` (Node 18+), `axios`, or `http.request`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
await fetch('https://api.com');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q73"></a>
### Q73: What is the Cluster module?

**Difficulty**: Advanced

**Strategy**:
Multi-processing to use all cores. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
cluster.fork();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q74"></a>
### Q74: How do you implement API rate limiting?

**Difficulty**: Intermediate

**Strategy**:
`express-rate-limit`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
rateLimit({ windowMs: 60000, max: 10 });
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q75"></a>
### Q75: How do you parse JSON?

**Difficulty**: Beginner

**Strategy**:
`JSON.parse()` or `express.json()` middleware. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
app.use(express.json());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q76"></a>
### Q76: How do you implement a WebSocket server?

**Difficulty**: Intermediate

**Strategy**:
Use `ws` or `socket.io`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const wss = new WebSocket.Server({ port: 8080 });
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q77"></a>
### Q77: What is `console.dir`?

**Difficulty**: Beginner

**Strategy**:
Displays an interactive list of the properties of the specified JavaScript object.

**Code Example**:
```javascript
console.dir(obj, { depth: null, colors: true });
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q78"></a>
### Q78: How do you profile a Node app?

**Difficulty**: Advanced

**Strategy**:
`--prof` flag or `0x` tool. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```bash
node --prof app.js
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q79"></a>
### Q79: How do you manage configuration?

**Difficulty**: Intermediate

**Strategy**:
`dotenv` or `config` module. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const config = require('config');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q80"></a>
### Q80: How do you schedule tasks?

**Difficulty**: Intermediate

**Strategy**:
`node-cron` or `agenda`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
cron.schedule('* * * * *', () => console.log('Task'));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q81"></a>
### Q81: How do you write unit tests?

**Difficulty**: Beginner

**Strategy**:
Jest, Mocha, Chai. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
it('should return true', () => expect(true).toBe(true));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q82"></a>
### Q82: How do you handle large JSON payloads?

**Difficulty**: Intermediate

**Strategy**:
Increase limit in body parser. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
express.json({ limit: '50mb' });
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q83"></a>
### Q83: How do you use async/await with callbacks?

**Difficulty**: Intermediate

**Strategy**:
Wrap in Promise. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
await new Promise(resolve => cb(resolve));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q84"></a>
### Q84: What is `module.exports` vs `exports`?

**Difficulty**: Advanced

**Strategy**:
`exports` is a reference to `module.exports`. If you reassign `exports`, the link is broken.

**Code Example**:
```javascript
exports.foo = 'bar'; // Works
exports = { foo: 'bar' }; // Breaks
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q85"></a>
### Q85: How do you implement a health check endpoint?

**Difficulty**: Beginner

**Strategy**:
Simple GET route. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
app.get('/health', (req, res) => res.send('OK'));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q86"></a>
### Q86: How do you compress HTTP responses?

**Difficulty**: Beginner

**Strategy**:
`compression` middleware. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
app.use(compression());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q87"></a>
### Q87: How do you protect against NoSQL Injection?

**Difficulty**: Intermediate

**Strategy**:
Sanitize input (remove `$` signs). This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const clean = req.body.username.replace(/\$/g, '');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q88"></a>
### Q88: How do you implement role-based access control?

**Difficulty**: Intermediate

**Strategy**:
Middleware checking user role. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
if (req.user.role !== 'admin') return res.sendStatus(403);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q89"></a>
### Q89: How do you use `EventEmitter`?

**Difficulty**: Beginner

**Strategy**:
Pub/Sub pattern. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
emitter.on('event', () => {});
emitter.emit('event');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q90"></a>
### Q90: How do you debug async code?

**Difficulty**: Intermediate

**Strategy**:
`async_hooks` or long stack traces. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
require('longjohn');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q91"></a>
### Q91: How do you serve static files?

**Difficulty**: Beginner

**Strategy**:
`express.static`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
app.use(express.static('public'));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q92"></a>
### Q92: How do you implement request validation?

**Difficulty**: Intermediate

**Strategy**:
Joi or express-validator. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
check('email').isEmail();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q93"></a>
### Q93: How do you mock dependencies in tests?

**Difficulty**: Intermediate

**Strategy**:
`jest.mock()`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
jest.mock('fs');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q94"></a>
### Q94: How do you handle timezones?

**Difficulty**: Intermediate

**Strategy**:
Store as UTC, display as local using Moment/Luxon.

**Code Example**:
```javascript
moment().utc().format();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q95"></a>
### Q95: How do you implement hot reload?

**Difficulty**: Beginner

**Strategy**:
Nodemon. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```bash
nodemon app.js
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q96"></a>
### Q96: How do you use MongoDB with Node?

**Difficulty**: Beginner

**Strategy**:
Mongoose or native driver. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
mongoose.connect(uri);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q97"></a>
### Q97: How do you implement redis caching?

**Difficulty**: Intermediate

**Strategy**:
Check cache, if miss, fetch and set cache. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
client.get('key', (err, val) => {});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q98"></a>
### Q98: How do you handle sticky sessions?

**Difficulty**: Advanced

**Strategy**:
Use a store (Redis) for sessions instead of memory, or configure Load Balancer.

**Code Example**:
```javascript
const RedisStore = require('connect-redis')(session);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q99"></a>
### Q99: How do you implement OAuth?

**Difficulty**: Intermediate

**Strategy**:
Passport.js. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
passport.use(new GoogleStrategy(...));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q100"></a>
### Q100: How do you parse command line arguments?

**Difficulty**: Beginner

**Strategy**:
`process.argv` or `yargs`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const args = process.argv.slice(2);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


Promise.reject(new Error('Fail!'));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---


<a id="q32"></a>
### Q32: How do you optimize garbage collection in Node.js?

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


<a id="q33"></a>
### Q33: How do you use Buffers safely?

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


<a id="q34"></a>
### Q34: How do you debug a Node.js application with the Inspector?

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


<a id="q35"></a>
### Q35: How do you create a secure HTTPS server?

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


<a id="q36"></a>
### Q36: How do you use `util.promisify` to convert callback-based functions?

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


<a id="q37"></a>
### Q37: How do you parse large JSON files without blocking the event loop?

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


<a id="q38"></a>
### Q38: How do you implement a simple rate limiter using Redis?

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


<a id="q39"></a>
### Q39: How do you use `vm` module to run untrusted code (Sandboxing)?

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


<a id="q40"></a>
### Q40: How do you prevent blocking the Event Loop with cryptographic operations?

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


<a id="q41"></a>
### Q41: How do you use `require.resolve`?

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


<a id="q42"></a>
### Q42: How do you implement simple middleware in pure Node.js?

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


<a id="q43"></a>
### Q43: How do you use the `repl` module to create a custom shell?

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


<a id="q44"></a>
### Q44: How do you benchmark Node.js code using `perf_hooks`?

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


<a id="q45"></a>
### Q45: How do you serve static files without a framework?

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

<a id="q46"></a>
### Q46: How do you use `fs.promises` for async file operations?

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

<a id="q47"></a>
### Q47: How do you implement a simple health check endpoint?

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

<a id="q48"></a>
### Q48: How do you use `AbortController` to cancel async operations?

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

<a id="q49"></a>
### Q49: How do you inspect heap snapshots programmatically using `v8` module?

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

<a id="q50"></a>
### Q50: How do you use the native Node.js Test Runner?

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


---


<a id="q51"></a>
### Q51: Explain the Node.js Event Loop phases.

**Difficulty**: Advanced

**Strategy**:
Timers (setTimeout), Pending Callbacks (I/O), Idle/Prepare, Poll (new I/O), Check (setImmediate), Close Callbacks.

**Code Example**:
```javascript
// Phases execute in specific order, with NextTick queue processed between them.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q52"></a>
### Q52: Difference between `process.nextTick` and `setImmediate`?

**Difficulty**: Intermediate

**Strategy**:
`nextTick` fires immediately after current operation (before IO). `setImmediate` fires in the Check phase (after IO).

**Code Example**:
```javascript
process.nextTick(() => console.log('NextTick'));
setImmediate(() => console.log('Immediate'));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q53"></a>
### Q53: How do Worker Threads differ from Cluster module?

**Difficulty**: Advanced

**Strategy**:
Cluster uses processes (separate memory). Worker Threads use threads (shared memory instance). Threads are lighter.

**Code Example**:
```javascript
const { Worker } = require('worker_threads');
new Worker('./worker.js');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q54"></a>
### Q54: How do you handle Backpressure in Streams?

**Difficulty**: Advanced

**Strategy**:
Listen for 'drain' event or use `pipe()` which handles it automatically.

**Code Example**:
```javascript
if (!stream.write(chunk)) {
  stream.once('drain', writeMore);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q55"></a>
### Q55: How do you debug a memory leak in Node.js?

**Difficulty**: Advanced

**Strategy**:
Use `--inspect` and Chrome DevTools, or `heapdump`. Look for Retained Size.

**Code Example**:
```javascript
const heapdump = require('heapdump');
heapdump.writeSnapshot('/var/local/' + Date.now() + '.heapsnapshot');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q56"></a>
### Q56: What is the Buffer class?

**Difficulty**: Beginner

**Strategy**:
Used to handle binary data. Fixed-size chunk of memory.

**Code Example**:
```javascript
const buf = Buffer.from('Hello');
console.log(buf.toString('hex'));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q57"></a>
### Q57: How do you implement a custom Transform stream?

**Difficulty**: Advanced

**Strategy**:
Extend `Transform` class and implement `_transform` method.

**Code Example**:
```javascript
class MyTransform extends Transform {
  _transform(chunk, enc, cb) {
    this.push(chunk.toString().toUpperCase());
    cb();
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q58"></a>
### Q58: How do you handle uncaught exceptions?

**Difficulty**: Intermediate

**Strategy**:
Listen to `uncaughtException`. Note: Process is in unstable state, should restart.

**Code Example**:
```javascript
process.on('uncaughtException', (err) => {
  console.error(err);
  process.exit(1);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q59"></a>
### Q59: What is libuv?

**Difficulty**: Advanced

**Strategy**:
C library that provides asynchronous I/O (Event Loop, Thread Pool) for Node.js.

**Code Example**:
```javascript
// Handles file system, DNS, network, etc.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q60"></a>
### Q60: How do you secure a Node.js app?

**Difficulty**: Intermediate

**Strategy**:
Helmet (headers), Rate Limiting, Data Validation, CORS config.

**Code Example**:
```javascript
app.use(helmet());
app.use(rateLimit({ windowMs: 15*60*1000, max: 100 }));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q61"></a>
### Q61: Difference between `spawn` and `exec`?

**Difficulty**: Intermediate

**Strategy**:
`spawn` returns a stream (good for large data). `exec` buffers output (good for small output).

**Code Example**:
```javascript
const { spawn } = require('child_process');
const ls = spawn('ls', ['-lh', '/usr']);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q62"></a>
### Q62: How do you implement a graceful shutdown?

**Difficulty**: Intermediate

**Strategy**:
Listen for SIGTERM/SIGINT. Close server and DB connections.

**Code Example**:
```javascript
process.on('SIGTERM', () => {
  server.close(() => {
    db.disconnect();
  });
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q63"></a>
### Q63: How do you use `util.promisify`?

**Difficulty**: Beginner

**Strategy**:
Converts callback-based functions to Promise-based.

**Code Example**:
```javascript
const readFile = util.promisify(fs.readFile);
await readFile('file.txt');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q64"></a>
### Q64: What is middleware in Express?

**Difficulty**: Beginner

**Strategy**:
Function that has access to req, res, and next. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
app.use((req, res, next) => {
  console.log('Time:', Date.now());
  next();
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q65"></a>
### Q65: How do you handle file uploads in Node?

**Difficulty**: Intermediate

**Strategy**:
Use `multer` or `busboy` to parse multipart/form-data.

**Code Example**:
```javascript
const upload = multer({ dest: 'uploads/' });
app.post('/profile', upload.single('avatar'), ...);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q66"></a>
### Q66: How do you implement JWT authentication?

**Difficulty**: Intermediate

**Strategy**:
Sign token on login. Verify token in middleware. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const token = jwt.sign({ id: user.id }, 'secret');
const decoded = jwt.verify(token, 'secret');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q67"></a>
### Q67: How do you optimize Node.js performance?

**Difficulty**: Advanced

**Strategy**:
Use caching (Redis), clustering, gzip compression, efficient DB queries.

**Code Example**:
```javascript
app.use(compression());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q68"></a>
### Q68: What is the purpose of `package-lock.json`?

**Difficulty**: Beginner

**Strategy**:
Locks dependency versions to ensure consistent installs.

**Code Example**:
```javascript
// Committed to git
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q69"></a>
### Q69: How do you implement logging?

**Difficulty**: Intermediate

**Strategy**:
Use Winston or Bunyan. Log to stdout/file with levels.

**Code Example**:
```javascript
logger.info('User logged in', { userId });
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q70"></a>
### Q70: How do you use Environment Variables?

**Difficulty**: Beginner

**Strategy**:
Use `dotenv` package. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
require('dotenv').config();
console.log(process.env.DB_HOST);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q71"></a>
### Q71: How do you handle CORS?

**Difficulty**: Beginner

**Strategy**:
Use `cors` middleware. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
app.use(cors({ origin: 'http://example.com' }));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q72"></a>
### Q72: How do you make an HTTP request?

**Difficulty**: Beginner

**Strategy**:
Use `axios`, `node-fetch`, or built-in `http`/`https` module.

**Code Example**:
```javascript
const res = await axios.get('https://api.com');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q73"></a>
### Q73: What is the Cluster module?

**Difficulty**: Advanced

**Strategy**:
Allows creating child processes (workers) that share server ports to utilize multi-core systems.

**Code Example**:
```javascript
if (cluster.isMaster) { cluster.fork(); }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q74"></a>
### Q74: How do you implement API rate limiting?

**Difficulty**: Intermediate

**Strategy**:
Use `express-rate-limit` or Redis-based limiter. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const limiter = rateLimit({ windowMs: 15 * 60 * 1000, max: 100 });
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q75"></a>
### Q75: How do you parse JSON?

**Difficulty**: Beginner

**Strategy**:
Use `JSON.parse()` (try-catch for safety) or `express.json()` middleware.

**Code Example**:
```javascript
app.use(express.json());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q76"></a>
### Q76: How do you implement a WebSocket server?

**Difficulty**: Intermediate

**Strategy**:
Use `ws` or `socket.io`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const wss = new WebSocket.Server({ port: 8080 });
wss.on('connection', ws => ws.send('hello'));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q77"></a>
### Q77: What is REPL?

**Difficulty**: Beginner

**Strategy**:
Read-Eval-Print Loop. Interactive shell. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
$ node
> 1 + 1
2
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q78"></a>
### Q78: How do you profile a Node app?

**Difficulty**: Advanced

**Strategy**:
Use `node --prof` or `clinic.js`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
$ clinic doctor -- node server.js
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q79"></a>
### Q79: How do you manage configuration?

**Difficulty**: Intermediate

**Strategy**:
Use `config` module or `dotenv`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const dbConfig = config.get('Customer.dbConfig');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q80"></a>
### Q80: How do you schedule tasks?

**Difficulty**: Intermediate

**Strategy**:
Use `node-cron` or `agenda`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
cron.schedule('* * * * *', () => console.log('Running task'));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q81"></a>
### Q81: How do you write unit tests?

**Difficulty**: Beginner

**Strategy**:
Use Jest, Mocha, or Tape. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
test('adds 1 + 2', () => { expect(sum(1, 2)).toBe(3); });
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q82"></a>
### Q82: How do you handle large JSON payloads?

**Difficulty**: Intermediate

**Strategy**:
Stream parsing with `JSONStream`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
fs.createReadStream('big.json').pipe(JSONStream.parse('*'));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q83"></a>
### Q83: How do you use async/await with callbacks?

**Difficulty**: Intermediate

**Strategy**:
Wrap in Promise. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
await new Promise((resolve) => fn(resolve));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q84"></a>
### Q84: What is `require.resolve`?

**Difficulty**: Advanced

**Strategy**:
Returns the path of the module without loading it.

**Code Example**:
```javascript
const path = require.resolve('lodash');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q85"></a>
### Q85: How do you implement a health check endpoint?

**Difficulty**: Beginner

**Strategy**:
Return 200 OK. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
app.get('/health', (req, res) => res.status(200).send('OK'));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q86"></a>
### Q86: How do you compress HTTP responses?

**Difficulty**: Beginner

**Strategy**:
Use `compression` middleware. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
app.use(compression());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q87"></a>
### Q87: How do you protect against NoSQL Injection?

**Difficulty**: Intermediate

**Strategy**:
Sanitize inputs, avoid passing user input directly to query objects.

**Code Example**:
```javascript
// Bad: find({ $where: req.body.code })
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q88"></a>
### Q88: How do you implement role-based access control?

**Difficulty**: Intermediate

**Strategy**:
Middleware to check user role. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
if (!req.user.roles.includes('admin')) return res.sendStatus(403);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q89"></a>
### Q89: How do you use `EventEmitter`?

**Difficulty**: Beginner

**Strategy**:
Extend or instantiate `EventEmitter`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const myEmitter = new EventEmitter();
myEmitter.on('event', () => console.log('fired'));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q90"></a>
### Q90: How do you debug async code?

**Difficulty**: Intermediate

**Strategy**:
Use `async_hooks` or long stack traces. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Async hooks track lifetime of async resources
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q91"></a>
### Q91: How do you serve static files?

**Difficulty**: Beginner

**Strategy**:
Use `express.static`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
app.use(express.static('public'));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q92"></a>
### Q92: How do you implement request validation?

**Difficulty**: Intermediate

**Strategy**:
Use `express-validator` or `joi`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
body('email').isEmail()
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q93"></a>
### Q93: How do you mock dependencies in tests?

**Difficulty**: Intermediate

**Strategy**:
Use `proxyquire` or Jest mocks. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
jest.mock('axios');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q94"></a>
### Q94: How do you handle timezones?

**Difficulty**: Intermediate

**Strategy**:
Use `moment-timezone` or `luxon`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
DateTime.now().setZone('America/New_York');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q95"></a>
### Q95: How do you implement hot reload?

**Difficulty**: Beginner

**Strategy**:
Use `nodemon`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
$ nodemon server.js
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q96"></a>
### Q96: How do you use MongoDB with Node?

**Difficulty**: Beginner

**Strategy**:
Use `mongoose` or native driver. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
mongoose.connect(uri);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q97"></a>
### Q97: How do you implement redis caching?

**Difficulty**: Intermediate

**Strategy**:
Check cache, if miss, fetch DB and set cache. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const val = await redis.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q98"></a>
### Q98: How do you handle sticky sessions?

**Difficulty**: Advanced

**Strategy**:
Configure load balancer (Nginx) or use shared store (Redis).

**Code Example**:
```javascript
// ip_hash in nginx
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q99"></a>
### Q99: How do you implement OAuth?

**Difficulty**: Intermediate

**Strategy**:
Use `passport.js` strategies. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
passport.use(new GoogleStrategy(...));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q100"></a>
### Q100: How do you parse command line arguments?

**Difficulty**: Beginner

**Strategy**:
Use `yargs` or `commander`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const argv = yargs.argv;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---
