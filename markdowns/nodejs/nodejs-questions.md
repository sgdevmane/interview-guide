# Node.js Interview Questions

## Table of Contents
1. [You have a readable stream producing data faster than a writable stream can consume it (Backpressure). How do you handle this manually without `pipe()`?](#q1-you-have-a-readable-stream-producing-data-faster-than-a-writable-stream-can-c)
2. [How do you use `Worker Threads` to offload a CPU-intensive task (like image processing) so it doesn't block the main Event Loop?](#q2-how-do-you-use-worker-threads-to-offload-a-cpu-intensive-task-like-image-proc)
3. [How do you implement a custom `Transform` stream to compress chunks of data on the fly?](#q3-how-do-you-implement-a-custom-transform-stream-to-compress-chunks-of-data-on-)
4. [You are migrating a CommonJS project to ESM (ECMAScript Modules). How do you handle `__dirname` and `__filename` which are not available in ESM?](#q4-you-are-migrating-a-commonjs-project-to-esm-ecmascript-modules-how-do-you-han)
5. [How do you properly handle errors in an `async` Express middleware to prevent the app from hanging?](#q5-how-do-you-properly-handle-errors-in-an-async-express-middleware-to-prevent-t)
6. [How do you use `setImmediate` vs `process.nextTick`? Provide a scenario where `nextTick` is dangerous.](#q6-how-do-you-use-setimmediate-vs-process-nexttick-provide-a-scenario-where-next)
7. [How do you debug a memory leak in a production Node.js app without stopping the process?](#q7-how-do-you-debug-a-memory-leak-in-a-production-node-js-app-without-stopping-t)
8. [How do you use the `cluster` module to scale a Node.js server across multiple CPU cores?](#q8-how-do-you-use-the-cluster-module-to-scale-a-node-js-server-across-multiple-c)
9. [How do you prevent 'Prototype Pollution' vulnerabilities when merging objects?](#q9-how-do-you-prevent-prototype-pollution-vulnerabilities-when-merging-objects)
10. [How do you implement a graceful shutdown to ensure all active database connections are closed before exiting?](#q10-how-do-you-implement-a-graceful-shutdown-to-ensure-all-active-database-conne)
11. [How do you use `Buffer.allocUnsafe` correctly versus `Buffer.alloc`?](#q11-how-do-you-use-buffer-allocunsafe-correctly-versus-buffer-alloc)
12. [How do you read a large file line-by-line without loading the entire file into memory?](#q12-how-do-you-read-a-large-file-line-by-line-without-loading-the-entire-file-in)
13. [How do you make a Node.js script executable from the command line (CLI tool)?](#q13-how-do-you-make-a-node-js-script-executable-from-the-command-line-cli-tool)
14. [How do you securely store user passwords using the `crypto` module (scrypt)?](#q14-how-do-you-securely-store-user-passwords-using-the-crypto-module-scrypt)
15. [How do you use `Promise.allSettled` to handle multiple async requests where some might fail?](#q15-how-do-you-use-promise-allsettled-to-handle-multiple-async-requests-where-so)
16. [How do you handle unhandled promise rejections globally?](#q16-how-do-you-handle-unhandled-promise-rejections-globally)
17. [How do you handle uncaught exceptions globally (and why you should exit)?](#q17-how-do-you-handle-uncaught-exceptions-globally-and-why-you-should-exit)
18. [How do you use `util.promisify` to convert callback-based functions to promises?](#q18-how-do-you-use-util-promisify-to-convert-callback-based-functions-to-promise)
19. [How do you use `fs.promises` for async file operations?](#q19-how-do-you-use-fs-promises-for-async-file-operations)
20. [How do you watch for file changes using `fs.watch` (and its caveats)?](#q20-how-do-you-watch-for-file-changes-using-fs-watch-and-its-caveats)
21. [How do you manage environment variables with `dotenv`?](#q21-how-do-you-manage-environment-variables-with-dotenv)
22. [How do you validate environment variables at startup (e.g., with Joi/Zod)?](#q22-how-do-you-validate-environment-variables-at-startup-e-g-with-joi-zod)
23. [How do you implement a structured logger using Winston or Pino?](#q23-how-do-you-implement-a-structured-logger-using-winston-or-pino)
24. [How do you trace requests across microservices using a Correlation ID?](#q24-how-do-you-trace-requests-across-microservices-using-a-correlation-id)
25. [How do you use `async_hooks` to track context across async calls?](#q25-how-do-you-use-async_hooks-to-track-context-across-async-calls)
26. [How do you debug performance issues with `perf_hooks`?](#q26-how-do-you-debug-performance-issues-with-perf_hooks)
27. [How do you measure event loop lag?](#q27-how-do-you-measure-event-loop-lag)
28. [How do you optimize garbage collection (flags like --max-old-space-size)?](#q28-how-do-you-optimize-garbage-collection-flags-like-max-old-space-size)
29. [How do you use `node --inspect-brk` for debugging at startup?](#q29-how-do-you-use-node-inspect-brk-for-debugging-at-startup)
30. [How do you profile CPU usage with the Profiler?](#q30-how-do-you-profile-cpu-usage-with-the-profiler)
31. [How do you generate a flame graph for Node.js?](#q31-how-do-you-generate-a-flame-graph-for-node-js)
32. [How do you secure HTTP headers using Helmet?](#q32-how-do-you-secure-http-headers-using-helmet)
33. [How do you prevent Rate Limiting attacks (e.g., express-rate-limit)?](#q33-how-do-you-prevent-rate-limiting-attacks-e-g-express-rate-limit)
34. [How do you sanitize user input to prevent XSS?](#q34-how-do-you-sanitize-user-input-to-prevent-xss)
35. [How do you prevent SQL Injection (Parameterization)?](#q35-how-do-you-prevent-sql-injection-parameterization)
36. [How do you prevent NoSQL Injection?](#q36-how-do-you-prevent-nosql-injection)
37. [How do you manage dependencies safely (npm audit, snyk)?](#q37-how-do-you-manage-dependencies-safely-npm-audit-snyk)
38. [How do you use `npm ci` for deterministic builds?](#q38-how-do-you-use-npm-ci-for-deterministic-builds)
39. [How do you create a lockfile (package-lock.json) and why it matters?](#q39-how-do-you-create-a-lockfile-package-lock-json-and-why-it-matters)
40. [How do you use `npm link` for local package development?](#q40-how-do-you-use-npm-link-for-local-package-development)
41. [How do you publish a private package to a registry?](#q41-how-do-you-publish-a-private-package-to-a-registry)
42. [How do you version an API using URL or Headers?](#q42-how-do-you-version-an-api-using-url-or-headers)
43. [How do you document an API using Swagger/OpenAPI?](#q43-how-do-you-document-an-api-using-swagger-openapi)
44. [How do you validate API request bodies (e.g., with Joi/Zod)?](#q44-how-do-you-validate-api-request-bodies-e-g-with-joi-zod)
45. [How do you handle file uploads using `multer` or `busboy`?](#q45-how-do-you-handle-file-uploads-using-multer-or-busboy)
46. [How do you stream a file upload directly to S3?](#q46-how-do-you-stream-a-file-upload-directly-to-s3)
47. [How do you serve static files efficiently?](#q47-how-do-you-serve-static-files-efficiently)
48. [How do you implement a reverse proxy with Node.js?](#q48-how-do-you-implement-a-reverse-proxy-with-node-js)
49. [How do you setup a load balancer with Nginx in front of Node?](#q49-how-do-you-setup-a-load-balancer-with-nginx-in-front-of-node)
50. [How do you keep a Node process alive with PM2 or Systemd?](#q50-how-do-you-keep-a-node-process-alive-with-pm2-or-systemd)
51. [How do you monitor a Node app with Prometheus metrics?](#q51-how-do-you-monitor-a-node-app-with-prometheus-metrics)
52. [How do you containerize a Node app with Docker (best practices)?](#q52-how-do-you-containerize-a-node-app-with-docker-best-practices)
53. [How do you optimize Docker image size for Node (multi-stage builds)?](#q53-how-do-you-optimize-docker-image-size-for-node-multi-stage-builds)
54. [How do you handle 'Zombie Processes' in Docker?](#q54-how-do-you-handle-zombie-processes-in-docker)
55. [How do you use `tini` as an init process in Docker?](#q55-how-do-you-use-tini-as-an-init-process-in-docker)
56. [How do you implement JWT authentication?](#q56-how-do-you-implement-jwt-authentication)
57. [How do you implement OAuth2/OpenID Connect?](#q57-how-do-you-implement-oauth2-openid-connect)
58. [How do you implement Role-Based Access Control (RBAC)?](#q58-how-do-you-implement-role-based-access-control-rbac)
59. [How do you hash passwords with Argon2?](#q59-how-do-you-hash-passwords-with-argon2)
60. [How do you implement 2FA (Two-Factor Authentication)?](#q60-how-do-you-implement-2fa-two-factor-authentication)
61. [How do you schedule recurring tasks (Cron jobs)?](#q61-how-do-you-schedule-recurring-tasks-cron-jobs)
62. [How do you process jobs in a queue (Bull/Redis)?](#q62-how-do-you-process-jobs-in-a-queue-bull-redis)
63. [How do you handle distributed locks with Redis?](#q63-how-do-you-handle-distributed-locks-with-redis)
64. [How do you cache API responses with Redis?](#q64-how-do-you-cache-api-responses-with-redis)
65. [How do you implement a WebSocket server (ws or socket.io)?](#q65-how-do-you-implement-a-websocket-server-ws-or-socket-io)
66. [How do you scale WebSockets across multiple nodes (Redis Adapter)?](#q66-how-do-you-scale-websockets-across-multiple-nodes-redis-adapter)
67. [How do you broadcast messages to specific WebSocket rooms?](#q67-how-do-you-broadcast-messages-to-specific-websocket-rooms)
68. [How do you handle WebSocket reconnection logic?](#q68-how-do-you-handle-websocket-reconnection-logic)
69. [How do you serialize data with Protocol Buffers for performance?](#q69-how-do-you-serialize-data-with-protocol-buffers-for-performance)
70. [How do you interact with a C++ library using N-API?](#q70-how-do-you-interact-with-a-c++-library-using-n-api)
71. [How do you run WebAssembly modules in Node.js?](#q71-how-do-you-run-webassembly-modules-in-node-js)
72. [How do you use the `vm` module to run untrusted code (sandbox)?](#q72-how-do-you-use-the-vm-module-to-run-untrusted-code-sandbox)
73. [How do you execute system commands with `child_process.spawn`?](#q73-how-do-you-execute-system-commands-with-child_process-spawn)
74. [How do you pipe output from one child process to another?](#q74-how-do-you-pipe-output-from-one-child-process-to-another)
75. [How do you handle `SIGKILL` vs `SIGTERM`?](#q75-how-do-you-handle-sigkill-vs-sigterm)
76. [How do you use `process.cwd()` vs `__dirname`?](#q76-how-do-you-use-process-cwd-vs-__dirname)
77. [How do you mock dependencies in unit tests (Jest/Sinon)?](#q77-how-do-you-mock-dependencies-in-unit-tests-jest-sinon)
78. [How do you test async code properly?](#q78-how-do-you-test-async-code-properly)
79. [How do you measure code coverage?](#q79-how-do-you-measure-code-coverage)
80. [How do you run tests in parallel?](#q80-how-do-you-run-tests-in-parallel)
81. [How do you setup a CI/CD pipeline for Node.js?](#q81-how-do-you-setup-a-ci-cd-pipeline-for-node-js)
82. [How do you lint code with ESLint and Prettier?](#q82-how-do-you-lint-code-with-eslint-and-prettier)
83. [How do you enforce commit message conventions (husky, commitlint)?](#q83-how-do-you-enforce-commit-message-conventions-husky-commitlint)
84. [How do you automate releases with Semantic Release?](#q84-how-do-you-automate-releases-with-semantic-release)
85. [How do you transpile TypeScript code for Node.js?](#q85-how-do-you-transpile-typescript-code-for-node-js)
86. [How do you run TypeScript directly with `ts-node` or `tsx`?](#q86-how-do-you-run-typescript-directly-with-ts-node-or-tsx)
87. [How do you configure path aliases in Node.js?](#q87-how-do-you-configure-path-aliases-in-node-js)
88. [How do you use `module-alias` for legacy projects?](#q88-how-do-you-use-module-alias-for-legacy-projects)
89. [How do you implement 'Hot Module Replacement' (HMR) on the server?](#q89-how-do-you-implement-hot-module-replacement-hmr-on-the-server)
90. [How do you restart the server on file changes (nodemon)?](#q90-how-do-you-restart-the-server-on-file-changes-nodemon)
91. [How do you load config based on `NODE_ENV`?](#q91-how-do-you-load-config-based-on-node_env)
92. [How do you access command line arguments (`process.argv`)?](#q92-how-do-you-access-command-line-arguments-process-argv)
93. [How do you parse command line args with `yargs` or `commander`?](#q93-how-do-you-parse-command-line-args-with-yargs-or-commander)
94. [How do you create an interactive CLI prompt (Inquirer.js)?](#q94-how-do-you-create-an-interactive-cli-prompt-inquirer-js)
95. [How do you display a progress bar in the terminal?](#q95-how-do-you-display-a-progress-bar-in-the-terminal)
96. [How do you colorize terminal output (chalk)?](#q96-how-do-you-colorize-terminal-output-chalk)
97. [How do you detect if stdout is a TTY?](#q97-how-do-you-detect-if-stdout-is-a-tty)
98. [How do you handle circular dependencies in modules?](#q98-how-do-you-handle-circular-dependencies-in-modules)
99. [How do you debug 'Module not found' errors?](#q99-how-do-you-debug-module-not-found-errors)
100. [How do you use `require.resolve` to find module paths?](#q100-how-do-you-use-require-resolve-to-find-module-paths)
101. [How do you monkey-patch a module for debugging (and why avoid it)?](#q101-how-do-you-monkey-patch-a-module-for-debugging-and-why-avoid-it)
102. [How do you implement the Singleton pattern in Node modules?](#q102-how-do-you-implement-the-singleton-pattern-in-node-modules)
103. [How do you share state across modules safely?](#q103-how-do-you-share-state-across-modules-safely)
104. [How do you implement a Plugin architecture?](#q104-how-do-you-implement-a-plugin-architecture)

---

### Q1: You have a readable stream producing data faster than a writable stream can consume it (Backpressure). How do you handle this manually without `pipe()`?

**Difficulty: Advanced**

**Solution: Listen for `drain` event**

Pause the readable stream when `write()` returns `false`, and resume when `drain` is emitted.

```javascript
readable.on('data', (chunk) => {
  const canWrite = writable.write(chunk);
  
  if (!canWrite) {
    // Backpressure detected, stop reading
    readable.pause();
    
    // Wait for buffer to drain
    writable.once('drain', () => {
      readable.resume();
    });
  }
});
```

[Back to Top](#table-of-contents)

---

### Q2: How do you use `Worker Threads` to offload a CPU-intensive task (like image processing) so it doesn't block the main Event Loop?

**Difficulty: Intermediate**

**Solution: `worker_threads` module**

Unlike `cluster` (which spawns processes), Workers share memory and are lightweight.

**worker.js**
```javascript
const { parentPort, workerData } = require('worker_threads');
// Heavy CPU task
const result = heavyTask(workerData);
parentPort.postMessage(result);
```

**main.js**
```javascript
const { Worker } = require('worker_threads');

function runTask(data) {
  return new Promise((resolve, reject) => {
    const worker = new Worker('./worker.js', { workerData: data });
    worker.on('message', resolve);
    worker.on('error', reject);
  });
}
```

[Back to Top](#table-of-contents)

---

### Q3: How do you implement a custom `Transform` stream to compress chunks of data on the fly?

**Difficulty: Intermediate**

**Solution: Extend `Transform` class**

Implement the `_transform` method.

```javascript
const { Transform } = require('stream');
const zlib = require('zlib');

const gzip = zlib.createGzip(); // Built-in Transform

// Custom Transform
class UpperCaseTransform extends Transform {
  _transform(chunk, encoding, callback) {
    // Push transformed data
    this.push(chunk.toString().toUpperCase());
    callback();
  }
}

process.stdin.pipe(new UpperCaseTransform()).pipe(process.stdout);
```

[Back to Top](#table-of-contents)

---

### Q4: You are migrating a CommonJS project to ESM (ECMAScript Modules). How do you handle `__dirname` and `__filename` which are not available in ESM?

**Difficulty: Intermediate**

**Solution: `import.meta.url`**

Use `fileURLToPath` and `dirname` from the `url` and `path` modules.

```javascript
import { fileURLToPath } from 'url';
import { dirname } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

console.log('Current Dir:', __dirname);
```

[Back to Top](#table-of-contents)

---

### Q5: How do you properly handle errors in an `async` Express middleware to prevent the app from hanging?

**Difficulty: Intermediate**

**Solution: `try-catch` and `next(err)`**

Async errors aren't caught automatically in Express 4 (Express 5 handles them).

```javascript
app.get('/users', async (req, res, next) => {
  try {
    const users = await db.getUsers();
    res.json(users);
  } catch (err) {
    // Pass error to global error handler
    next(err); 
  }
});
```

[Back to Top](#table-of-contents)

---

### Q6: How do you use `setImmediate` vs `process.nextTick`? Provide a scenario where `nextTick` is dangerous.

**Difficulty: Advanced**

**Solution: Execution Phases**

*   `nextTick`: Runs **immediately** after current code, before IO. Recursive calls starve the Event Loop.
*   `setImmediate`: Runs in the **Check** phase (after IO).

**Dangerous `nextTick`:**
```javascript
function loop() {
  process.nextTick(loop); // Blocks IO indefinitely (starvation)
}
// loop(); 
```

**Safe Recursive Loop:**
```javascript
function loop() {
  setImmediate(loop); // Allows IO to run in between
}
```

[Back to Top](#table-of-contents)

---

### Q7: How do you debug a memory leak in a production Node.js app without stopping the process?

**Difficulty: Expert**

**Solution: `heapdump` or Inspector Protocol**

Trigger a heap snapshot and analyze it in Chrome DevTools.

```javascript
const heapdump = require('heapdump');

// Manually trigger via signal
process.on('SIGUSR2', () => {
  heapdump.writeSnapshot('./heap-' + Date.now() + '.heapsnapshot');
});
```

[Back to Top](#table-of-contents)

---

### Q8: How do you use the `cluster` module to scale a Node.js server across multiple CPU cores?

**Difficulty: Intermediate**

**Solution: Fork Workers**

The master process forks workers, which share the same TCP port.

```javascript
const cluster = require('cluster');
const http = require('http');
const numCPUs = require('os').cpus().length;

if (cluster.isMaster) {
  for (let i = 0; i < numCPUs; i++) {
    cluster.fork();
  }
} else {
  http.createServer((req, res) => {
    res.writeHead(200);
    res.end('Hello World');
  }).listen(8000);
}
```

[Back to Top](#table-of-contents)

---

### Q9: How do you prevent 'Prototype Pollution' vulnerabilities when merging objects?

**Difficulty: Advanced**

**Solution: Freeze prototype or use `Map`**

Avoid unsafe recursive merges that modify `__proto__`.

```javascript
// Vulnerable Merge
function merge(target, source) {
  for (let key in source) {
    if (typeof target[key] === 'object') {
      merge(target[key], source[key]);
    } else {
      target[key] = source[key];
    }
  }
  return target;
}

// Fix: Prevent access to __proto__
const safeMerge = (target, source) => {
  // Implementation that checks for __proto__, constructor, prototype keys
};
```

[Back to Top](#table-of-contents)

---

### Q10: How do you implement a graceful shutdown to ensure all active database connections are closed before exiting?

**Difficulty: Intermediate**

**Solution: Listen for `SIGTERM`/`SIGINT`**

Stop accepting new requests, wait for existing ones, then close DB.

```javascript
const server = app.listen(3000);

process.on('SIGTERM', async () => {
  console.log('SIGTERM received');
  
  server.close(() => {
    console.log('HTTP server closed');
  });

  await db.disconnect();
  process.exit(0);
});
```

[Back to Top](#table-of-contents)

---

### Q11: How do you use `Buffer.allocUnsafe` correctly versus `Buffer.alloc`?

**Difficulty: Advanced**

**Solution: Initialize if Unsafe**

*   `Buffer.alloc(size)`: Zero-fills memory (Slower, Safe).
*   `Buffer.allocUnsafe(size)`: Uninitialized memory (Faster, Potentially contains sensitive old data).

**Usage:** Always `fill()` if using `allocUnsafe`.
```javascript
const buf = Buffer.allocUnsafe(10);
buf.fill(0); // Now safe
```

[Back to Top](#table-of-contents)

---

### Q12: How do you read a large file line-by-line without loading the entire file into memory?

**Difficulty: Intermediate**

**Solution: `readline` module**

Streams the file content line by line.

```javascript
const fs = require('fs');
const readline = require('readline');

const rl = readline.createInterface({
  input: fs.createReadStream('large-file.txt'),
  crlfDelay: Infinity
});

rl.on('line', (line) => {
  console.log(`Line: ${line}`);
});
```

[Back to Top](#table-of-contents)

---

### Q13: How do you make a Node.js script executable from the command line (CLI tool)?

**Difficulty: Beginner**

**Solution: Shebang + `bin` in package.json**

1.  Add Shebang:
    ```javascript
    #!/usr/bin/env node
    console.log("Hello CLI");
    ```
2.  Update `package.json`:
    ```json
    "bin": {
      "my-tool": "./index.js"
    }
    ```
3.  Link: `npm link`

[Back to Top](#table-of-contents)

---

### Q14: How do you securely store user passwords using the `crypto` module (scrypt)?

**Difficulty: Intermediate**

**Solution: `scrypt` (Salt + Hash)**

Do not use simple SHA-256. Use a slow algorithm like scrypt or Argon2.

```javascript
const { scrypt, randomBytes } = require('crypto');

const salt = randomBytes(16).toString('hex');
const password = 'super-secret';

scrypt(password, salt, 64, (err, derivedKey) => {
  if (err) throw err;
  console.log(derivedKey.toString('hex'));
});
```

[Back to Top](#table-of-contents)

---

### Q15: How do you use `Promise.allSettled` to handle multiple async requests where some might fail?

**Difficulty: Intermediate**

**Solution: `Promise.allSettled`**

Unlike `Promise.all`, it doesn't reject if one promise fails.

```javascript
const p1 = Promise.resolve(1);
const p2 = Promise.reject('error');

const results = await Promise.allSettled([p1, p2]);

results.forEach((result) => {
  if (result.status === 'fulfilled') {
    console.log('Success:', result.value);
  } else {
    console.error('Failed:', result.reason);
  }
});
```

[Back to Top](#table-of-contents)

---

### Q16: How do you handle unhandled promise rejections globally?

**Difficulty: Intermediate**

**Answer:**

To handle unhandled promise rejections globally, you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q17: How do you handle uncaught exceptions globally (and why you should exit)?

**Difficulty: Intermediate**

**Answer:**

To handle uncaught exceptions globally (and why you should exit), you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q18: How do you use `util.promisify` to convert callback-based functions to promises?

**Difficulty: Beginner**

**Answer:**

To use `util.promisify` to convert callback-based functions to promises, you should use standard Node.js modules or popular libraries suitable for beginner scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q19: How do you use `fs.promises` for async file operations?

**Difficulty: Beginner**

**Answer:**

To use `fs.promises` for async file operations, you should use standard Node.js modules or popular libraries suitable for beginner scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q20: How do you watch for file changes using `fs.watch` (and its caveats)?

**Difficulty: Intermediate**

**Answer:**

To watch for file changes using `fs.watch` (and its caveats), you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q21: How do you manage environment variables with `dotenv`?

**Difficulty: Beginner**

**Answer:**

To manage environment variables with `dotenv`, you should use standard Node.js modules or popular libraries suitable for beginner scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q22: How do you validate environment variables at startup (e.g., with Joi/Zod)?

**Difficulty: Intermediate**

**Answer:**

To validate environment variables at startup (e.g., with Joi/Zod), you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q23: How do you implement a structured logger using Winston or Pino?

**Difficulty: Intermediate**

**Answer:**

To implement a structured logger using Winston or Pino, you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q24: How do you trace requests across microservices using a Correlation ID?

**Difficulty: Advanced**

**Answer:**

To trace requests across microservices using a Correlation ID, you should use standard Node.js modules or popular libraries suitable for advanced scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q25: How do you use `async_hooks` to track context across async calls?

**Difficulty: Expert**

**Answer:**

To use `async_hooks` to track context across async calls, you should use standard Node.js modules or popular libraries suitable for expert scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q26: How do you debug performance issues with `perf_hooks`?

**Difficulty: Advanced**

**Answer:**

To debug performance issues with `perf_hooks`, you should use standard Node.js modules or popular libraries suitable for advanced scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q27: How do you measure event loop lag?

**Difficulty: Advanced**

**Answer:**

To measure event loop lag, you should use standard Node.js modules or popular libraries suitable for advanced scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q28: How do you optimize garbage collection (flags like --max-old-space-size)?

**Difficulty: Advanced**

**Answer:**

To optimize garbage collection (flags like --max-old-space-size), you should use standard Node.js modules or popular libraries suitable for advanced scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q29: How do you use `node --inspect-brk` for debugging at startup?

**Difficulty: Beginner**

**Answer:**

To use `node --inspect-brk` for debugging at startup, you should use standard Node.js modules or popular libraries suitable for beginner scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q30: How do you profile CPU usage with the Profiler?

**Difficulty: Advanced**

**Answer:**

To profile CPU usage with the Profiler, you should use standard Node.js modules or popular libraries suitable for advanced scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q31: How do you generate a flame graph for Node.js?

**Difficulty: Expert**

**Answer:**

To generate a flame graph for Node.js, you should use standard Node.js modules or popular libraries suitable for expert scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q32: How do you secure HTTP headers using Helmet?

**Difficulty: Beginner**

**Answer:**

To secure HTTP headers using Helmet, you should use standard Node.js modules or popular libraries suitable for beginner scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q33: How do you prevent Rate Limiting attacks (e.g., express-rate-limit)?

**Difficulty: Intermediate**

**Answer:**

To prevent Rate Limiting attacks (e.g., express-rate-limit), you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q34: How do you sanitize user input to prevent XSS?

**Difficulty: Intermediate**

**Answer:**

To sanitize user input to prevent XSS, you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q35: How do you prevent SQL Injection (Parameterization)?

**Difficulty: Beginner**

**Answer:**

To prevent SQL Injection (Parameterization), you should use standard Node.js modules or popular libraries suitable for beginner scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q36: How do you prevent NoSQL Injection?

**Difficulty: Intermediate**

**Answer:**

To prevent NoSQL Injection, you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q37: How do you manage dependencies safely (npm audit, snyk)?

**Difficulty: Beginner**

**Answer:**

To manage dependencies safely (npm audit, snyk), you should use standard Node.js modules or popular libraries suitable for beginner scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q38: How do you use `npm ci` for deterministic builds?

**Difficulty: Beginner**

**Answer:**

To use `npm ci` for deterministic builds, you should use standard Node.js modules or popular libraries suitable for beginner scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q39: How do you create a lockfile (package-lock.json) and why it matters?

**Difficulty: Beginner**

**Answer:**

To create a lockfile (package-lock.json) and why it matters, you should use standard Node.js modules or popular libraries suitable for beginner scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q40: How do you use `npm link` for local package development?

**Difficulty: Intermediate**

**Answer:**

To use `npm link` for local package development, you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q41: How do you publish a private package to a registry?

**Difficulty: Intermediate**

**Answer:**

To publish a private package to a registry, you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q42: How do you version an API using URL or Headers?

**Difficulty: Intermediate**

**Answer:**

To version an API using URL or Headers, you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q43: How do you document an API using Swagger/OpenAPI?

**Difficulty: Intermediate**

**Answer:**

To document an API using Swagger/OpenAPI, you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q44: How do you validate API request bodies (e.g., with Joi/Zod)?

**Difficulty: Beginner**

**Answer:**

To validate API request bodies (e.g., with Joi/Zod), you should use standard Node.js modules or popular libraries suitable for beginner scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q45: How do you handle file uploads using `multer` or `busboy`?

**Difficulty: Intermediate**

**Answer:**

To handle file uploads using `multer` or `busboy`, you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q46: How do you stream a file upload directly to S3?

**Difficulty: Advanced**

**Answer:**

To stream a file upload directly to S3, you should use standard Node.js modules or popular libraries suitable for advanced scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q47: How do you serve static files efficiently?

**Difficulty: Beginner**

**Answer:**

To serve static files efficiently, you should use standard Node.js modules or popular libraries suitable for beginner scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q48: How do you implement a reverse proxy with Node.js?

**Difficulty: Advanced**

**Answer:**

To implement a reverse proxy with Node.js, you should use standard Node.js modules or popular libraries suitable for advanced scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q49: How do you setup a load balancer with Nginx in front of Node?

**Difficulty: Intermediate**

**Answer:**

To setup a load balancer with Nginx in front of Node, you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q50: How do you keep a Node process alive with PM2 or Systemd?

**Difficulty: Intermediate**

**Answer:**

To keep a Node process alive with PM2 or Systemd, you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q51: How do you monitor a Node app with Prometheus metrics?

**Difficulty: Advanced**

**Answer:**

To monitor a Node app with Prometheus metrics, you should use standard Node.js modules or popular libraries suitable for advanced scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q52: How do you containerize a Node app with Docker (best practices)?

**Difficulty: Intermediate**

**Answer:**

To containerize a Node app with Docker (best practices), you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q53: How do you optimize Docker image size for Node (multi-stage builds)?

**Difficulty: Intermediate**

**Answer:**

To optimize Docker image size for Node (multi-stage builds), you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q54: How do you handle 'Zombie Processes' in Docker?

**Difficulty: Advanced**

**Answer:**

To handle 'Zombie Processes' in Docker, you should use standard Node.js modules or popular libraries suitable for advanced scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q55: How do you use `tini` as an init process in Docker?

**Difficulty: Intermediate**

**Answer:**

To use `tini` as an init process in Docker, you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q56: How do you implement JWT authentication?

**Difficulty: Intermediate**

**Answer:**

To implement JWT authentication, you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q57: How do you implement OAuth2/OpenID Connect?

**Difficulty: Advanced**

**Answer:**

To implement OAuth2/OpenID Connect, you should use standard Node.js modules or popular libraries suitable for advanced scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q58: How do you implement Role-Based Access Control (RBAC)?

**Difficulty: Intermediate**

**Answer:**

To implement Role-Based Access Control (RBAC), you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q59: How do you hash passwords with Argon2?

**Difficulty: Intermediate**

**Answer:**

To hash passwords with Argon2, you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q60: How do you implement 2FA (Two-Factor Authentication)?

**Difficulty: Advanced**

**Answer:**

To implement 2FA (Two-Factor Authentication), you should use standard Node.js modules or popular libraries suitable for advanced scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q61: How do you schedule recurring tasks (Cron jobs)?

**Difficulty: Intermediate**

**Answer:**

To schedule recurring tasks (Cron jobs), you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q62: How do you process jobs in a queue (Bull/Redis)?

**Difficulty: Advanced**

**Answer:**

To process jobs in a queue (Bull/Redis), you should use standard Node.js modules or popular libraries suitable for advanced scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q63: How do you handle distributed locks with Redis?

**Difficulty: Expert**

**Answer:**

To handle distributed locks with Redis, you should use standard Node.js modules or popular libraries suitable for expert scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q64: How do you cache API responses with Redis?

**Difficulty: Intermediate**

**Answer:**

To cache API responses with Redis, you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q65: How do you implement a WebSocket server (ws or socket.io)?

**Difficulty: Intermediate**

**Answer:**

To implement a WebSocket server (ws or socket.io), you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q66: How do you scale WebSockets across multiple nodes (Redis Adapter)?

**Difficulty: Advanced**

**Answer:**

To scale WebSockets across multiple nodes (Redis Adapter), you should use standard Node.js modules or popular libraries suitable for advanced scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q67: How do you broadcast messages to specific WebSocket rooms?

**Difficulty: Intermediate**

**Answer:**

To broadcast messages to specific WebSocket rooms, you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q68: How do you handle WebSocket reconnection logic?

**Difficulty: Intermediate**

**Answer:**

To handle WebSocket reconnection logic, you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q69: How do you serialize data with Protocol Buffers for performance?

**Difficulty: Expert**

**Answer:**

To serialize data with Protocol Buffers for performance, you should use standard Node.js modules or popular libraries suitable for expert scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q70: How do you interact with a C++ library using N-API?

**Difficulty: Expert**

**Answer:**

To interact with a C++ library using N-API, you should use standard Node.js modules or popular libraries suitable for expert scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q71: How do you run WebAssembly modules in Node.js?

**Difficulty: Advanced**

**Answer:**

To run WebAssembly modules in Node.js, you should use standard Node.js modules or popular libraries suitable for advanced scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q72: How do you use the `vm` module to run untrusted code (sandbox)?

**Difficulty: Expert**

**Answer:**

To use the `vm` module to run untrusted code (sandbox), you should use standard Node.js modules or popular libraries suitable for expert scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q73: How do you execute system commands with `child_process.spawn`?

**Difficulty: Intermediate**

**Answer:**

To execute system commands with `child_process.spawn`, you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q74: How do you pipe output from one child process to another?

**Difficulty: Intermediate**

**Answer:**

To pipe output from one child process to another, you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q75: How do you handle `SIGKILL` vs `SIGTERM`?

**Difficulty: Intermediate**

**Answer:**

To handle `SIGKILL` vs `SIGTERM`, you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q76: How do you use `process.cwd()` vs `__dirname`?

**Difficulty: Beginner**

**Answer:**

To use `process.cwd()` vs `__dirname`, you should use standard Node.js modules or popular libraries suitable for beginner scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q77: How do you mock dependencies in unit tests (Jest/Sinon)?

**Difficulty: Intermediate**

**Answer:**

To mock dependencies in unit tests (Jest/Sinon), you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q78: How do you test async code properly?

**Difficulty: Beginner**

**Answer:**

To test async code properly, you should use standard Node.js modules or popular libraries suitable for beginner scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q79: How do you measure code coverage?

**Difficulty: Beginner**

**Answer:**

To measure code coverage, you should use standard Node.js modules or popular libraries suitable for beginner scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q80: How do you run tests in parallel?

**Difficulty: Intermediate**

**Answer:**

To run tests in parallel, you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q81: How do you setup a CI/CD pipeline for Node.js?

**Difficulty: Intermediate**

**Answer:**

To setup a CI/CD pipeline for Node.js, you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q82: How do you lint code with ESLint and Prettier?

**Difficulty: Beginner**

**Answer:**

To lint code with ESLint and Prettier, you should use standard Node.js modules or popular libraries suitable for beginner scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q83: How do you enforce commit message conventions (husky, commitlint)?

**Difficulty: Intermediate**

**Answer:**

To enforce commit message conventions (husky, commitlint), you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q84: How do you automate releases with Semantic Release?

**Difficulty: Advanced**

**Answer:**

To automate releases with Semantic Release, you should use standard Node.js modules or popular libraries suitable for advanced scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q85: How do you transpile TypeScript code for Node.js?

**Difficulty: Intermediate**

**Answer:**

To transpile TypeScript code for Node.js, you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q86: How do you run TypeScript directly with `ts-node` or `tsx`?

**Difficulty: Beginner**

**Answer:**

To run TypeScript directly with `ts-node` or `tsx`, you should use standard Node.js modules or popular libraries suitable for beginner scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q87: How do you configure path aliases in Node.js?

**Difficulty: Intermediate**

**Answer:**

To configure path aliases in Node.js, you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q88: How do you use `module-alias` for legacy projects?

**Difficulty: Intermediate**

**Answer:**

To use `module-alias` for legacy projects, you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q89: How do you implement 'Hot Module Replacement' (HMR) on the server?

**Difficulty: Advanced**

**Answer:**

To implement 'Hot Module Replacement' (HMR) on the server, you should use standard Node.js modules or popular libraries suitable for advanced scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q90: How do you restart the server on file changes (nodemon)?

**Difficulty: Beginner**

**Answer:**

To restart the server on file changes (nodemon), you should use standard Node.js modules or popular libraries suitable for beginner scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q91: How do you load config based on `NODE_ENV`?

**Difficulty: Beginner**

**Answer:**

To load config based on `NODE_ENV`, you should use standard Node.js modules or popular libraries suitable for beginner scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q92: How do you access command line arguments (`process.argv`)?

**Difficulty: Beginner**

**Answer:**

To access command line arguments (`process.argv`), you should use standard Node.js modules or popular libraries suitable for beginner scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q93: How do you parse command line args with `yargs` or `commander`?

**Difficulty: Intermediate**

**Answer:**

To parse command line args with `yargs` or `commander`, you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q94: How do you create an interactive CLI prompt (Inquirer.js)?

**Difficulty: Intermediate**

**Answer:**

To create an interactive CLI prompt (Inquirer.js), you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q95: How do you display a progress bar in the terminal?

**Difficulty: Intermediate**

**Answer:**

To display a progress bar in the terminal, you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q96: How do you colorize terminal output (chalk)?

**Difficulty: Beginner**

**Answer:**

To colorize terminal output (chalk), you should use standard Node.js modules or popular libraries suitable for beginner scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q97: How do you detect if stdout is a TTY?

**Difficulty: Intermediate**

**Answer:**

To detect if stdout is a TTY, you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q98: How do you handle circular dependencies in modules?

**Difficulty: Intermediate**

**Answer:**

To handle circular dependencies in modules, you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q99: How do you debug 'Module not found' errors?

**Difficulty: Beginner**

**Answer:**

To debug 'Module not found' errors, you should use standard Node.js modules or popular libraries suitable for beginner scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q100: How do you use `require.resolve` to find module paths?

**Difficulty: Intermediate**

**Answer:**

To use `require.resolve` to find module paths, you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q101: How do you monkey-patch a module for debugging (and why avoid it)?

**Difficulty: Advanced**

**Answer:**

To monkey-patch a module for debugging (and why avoid it), you should use standard Node.js modules or popular libraries suitable for advanced scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q102: How do you implement the Singleton pattern in Node modules?

**Difficulty: Intermediate**

**Answer:**

To implement the Singleton pattern in Node modules, you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q103: How do you share state across modules safely?

**Difficulty: Intermediate**

**Answer:**

To share state across modules safely, you should use standard Node.js modules or popular libraries suitable for intermediate scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

### Q104: How do you implement a Plugin architecture?

**Difficulty: Advanced**

**Answer:**

To implement a Plugin architecture, you should use standard Node.js modules or popular libraries suitable for advanced scenarios. Provide a code snippet demonstrating the implementation.

[Back to Top](#table-of-contents)

---

