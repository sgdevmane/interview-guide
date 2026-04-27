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
16. [How do you implement JWT authentication in Node.js?](#q16-how-do-you-implement-jwt-authentication-in-nodejs) <span class="intermediate">Intermediate</span>
17. [How do you implement rate limiting in a Node.js API?](#q17-how-do-you-implement-rate-limiting-in-a-nodejs-api) <span class="intermediate">Intermediate</span>
18. [When should you use node-postgres vs an ORM?](#q18-when-should-you-use-node-postgres-vs-an-orm) <span class="intermediate">Intermediate</span>
19. [How do you handle uncaught exceptions in Node.js?](#q19-how-do-you-handle-uncaught-exceptions-in-nodejs) <span class="intermediate">Intermediate</span>
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
### Q16: How do you implement JWT authentication in Node.js?

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
### Q17: How do you implement rate limiting in a Node.js API?

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
### Q18: When should you use node-postgres vs an ORM?

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
### Q19: How do you handle uncaught exceptions in Node.js?

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

