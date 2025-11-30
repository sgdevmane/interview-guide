<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>JavaScript Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for frontend developers</b></p>
</div>

---

## Table of Contents

1. [How do you implement a robust debounce function with immediate execution option?](#q1-how-do-you-implement-a-robust-debounce-function-with-immediate-execution-option) <span class="beginner">Beginner</span>
2. [How do you deeply clone an object handling circular references and special types?](#q2-how-do-you-deeply-clone-an-object-handling-circular-references-and-special-types) <span class="beginner">Beginner</span>
3. [How do you implement a custom Promise.allSettled() polyfill?](#q3-how-do-you-implement-a-custom-promise.allsettled-polyfill) <span class="beginner">Beginner</span>
4. [How do you efficiently flatten a deeply nested array without using `Array.prototype.flat`?](#q4-how-do-you-efficiently-flatten-a-deeply-nested-array-without-using-array.prototype.flat) <span class="beginner">Beginner</span>
5. [How do you implement function composition (pipe) from scratch?](#q5-how-do-you-implement-function-composition-pipe-from-scratch) <span class="beginner">Beginner</span>
6. [How do you implement an event emitter (Pub/Sub pattern) from scratch?](#q6-how-do-you-implement-an-event-emitter-pubsub-pattern-from-scratch) <span class="beginner">Beginner</span>
7. [How do you throttle a function to ensure it runs at most once every X milliseconds?](#q7-how-do-you-throttle-a-function-to-ensure-it-runs-at-most-once-every-x-milliseconds) <span class="beginner">Beginner</span>
8. [How do you implement a memoization function to cache expensive calculation results?](#q8-how-do-you-implement-a-memoization-function-to-cache-expensive-calculation-results) <span class="beginner">Beginner</span>
9. [How do you parallelize async tasks with a concurrency limit?](#q9-how-do-you-parallelize-async-tasks-with-a-concurrency-limit) <span class="beginner">Beginner</span>
10. [How do you implement a custom `instanceof` operator?](#q10-how-do-you-implement-a-custom-instanceof-operator) <span class="beginner">Beginner</span>
11. [How do you implement currying to transform a function?](#q11-how-do-you-implement-currying-to-transform-a-function) <span class="beginner">Beginner</span>
12. [How do you implement a custom Iterable using Symbol.iterator?](#q12-how-do-you-implement-a-custom-iterable-using-symbol.iterator) <span class="beginner">Beginner</span>
13. [How do you use Generators for asynchronous flow control?](#q13-how-do-you-use-generators-for-asynchronous-flow-control) <span class="beginner">Beginner</span>
14. [How do you use the IntersectionObserver API for lazy loading images?](#q14-how-do-you-use-the-intersectionobserver-api-for-lazy-loading-images) <span class="beginner">Beginner</span>
15. [How do you use the MutationObserver API to track DOM changes?](#q15-how-do-you-use-the-mutationobserver-api-to-track-dom-changes) <span class="beginner">Beginner</span>
16. [How do you implement a virtual list (windowing) for large datasets?](#q16-how-do-you-implement-a-virtual-list-windowing-for-large-datasets) <span class="beginner">Beginner</span>
17. [How do you optimize event listeners using event delegation?](#q17-how-do-you-optimize-event-listeners-using-event-delegation) <span class="beginner">Beginner</span>
18. [How do you prevent prototype pollution attacks?](#q18-how-do-you-prevent-prototype-pollution-attacks) <span class="beginner">Beginner</span>
19. [How do you securely store tokens in the browser?](#q19-how-do-you-securely-store-tokens-in-the-browser) <span class="beginner">Beginner</span>
20. [How do you implement CSRF protection in AJAX requests?](#q20-how-do-you-implement-csrf-protection-in-ajax-requests) <span class="beginner">Beginner</span>
21. [How do you sanitize user input to prevent XSS?](#q21-how-do-you-sanitize-user-input-to-prevent-xss) <span class="beginner">Beginner</span>
22. [How do you use the BroadcastChannel API for tab communication?](#q22-how-do-you-use-the-broadcastchannel-api-for-tab-communication) <span class="beginner">Beginner</span>
23. [How do you use SharedWorkers for shared state between tabs?](#q23-how-do-you-use-sharedworkers-for-shared-state-between-tabs) <span class="beginner">Beginner</span>
24. [How do you implement a simple state management system from scratch?](#q24-how-do-you-implement-a-simple-state-management-system-from-scratch) <span class="beginner">Beginner</span>
25. [How do you implement a client-side router from scratch?](#q25-how-do-you-implement-a-client-side-router-from-scratch) <span class="beginner">Beginner</span>
26. [How do you parse query string parameters without a library?](#q26-how-do-you-parse-query-string-parameters-without-a-library) <span class="beginner">Beginner</span>
27. [How do you check if two objects are deeply equal?](#q27-how-do-you-check-if-two-objects-are-deeply-equal) <span class="beginner">Beginner</span>
28. [How do you retry a failed API call with exponential backoff?](#q28-how-do-you-retry-a-failed-api-call-with-exponential-backoff) <span class="beginner">Beginner</span>
29. [How do you cancel a fetch request using AbortController?](#q29-how-do-you-cancel-a-fetch-request-using-abortcontroller) <span class="beginner">Beginner</span>
30. [How do you implement a custom `bind` function?](#q30-how-do-you-implement-a-custom-bind-function) <span class="beginner">Beginner</span>
31. [How do you use the Proxy API to validate object property assignments?](#q31-how-do-you-use-the-proxy-api-to-validate-object-property-assignments) <span class="advanced">Advanced</span>
32. [What is the Reflect API and how does it relate to Proxy?](#q32-what-is-the-reflect-api-and-how-does-it-relate-to-proxy) <span class="advanced">Advanced</span>
33. [When should you use a Map over a plain Object?](#q33-when-should-you-use-a-map-over-a-plain-object) <span class="intermediate">Intermediate</span>
34. [How do you efficiently remove duplicates from an array using Set?](#q34-how-do-you-efficiently-remove-duplicates-from-an-array-using-set) <span class="beginner">Beginner</span>
35. [What is a WeakMap and why is it useful for memory management?](#q35-what-is-a-weakmap-and-why-is-it-useful-for-memory-management) <span class="advanced">Advanced</span>
36. [How do you implement an ID generator using Generators?](#q36-how-do-you-implement-an-id-generator-using-generators) <span class="intermediate">Intermediate</span>
37. [Why is `requestAnimationFrame` better than `setTimeout` for animations?](#q37-why-is-requestanimationframe-better-than-settimeout-for-animations) <span class="intermediate">Intermediate</span>
38. [How do you offload heavy CPU tasks using Web Workers?](#q38-how-do-you-offload-heavy-cpu-tasks-using-web-workers) <span class="advanced">Advanced</span>
39. [What is the difference between `null` and `undefined`?](#q39-what-is-the-difference-between-null-and-undefined) <span class="beginner">Beginner</span>
40. [How do you use the `Intl` API for language-sensitive formatting?](#q40-how-do-you-use-the-intl-api-for-language-sensitive-formatting) <span class="intermediate">Intermediate</span>
41. [What is `BigInt` and when should you use it?](#q41-what-is-bigint-and-when-should-you-use-it) <span class="intermediate">Intermediate</span>
42. [What is the difference between Nullish Coalescing (`??`) and Logical OR (`||`)?](#q42-what-is-the-difference-between-nullish-coalescing--and-logical-or-||) <span class="intermediate">Intermediate</span>
43. [How does Optional Chaining (`?.`) simplify object access?](#q43-how-does-optional-chaining-.-simplify-object-access) <span class="beginner">Beginner</span>
44. [What is `globalThis`?](#q44-what-is-globalthis) <span class="intermediate">Intermediate</span>
45. [Explain the 'Classic Closure Loop' problem and how to fix it.](#q45-explain-the-classic-closure-loop-problem-and-how-to-fix-it.) <span class="intermediate">Intermediate</span>
46. [What is the difference between Function Declaration and Function Expression regarding Hoisting?](#q46-what-is-the-difference-between-function-declaration-and-function-expression-regarding-hoisting) <span class="beginner">Beginner</span>
47. [How do you perform a deep equality check manually?](#q47-how-do-you-perform-a-deep-equality-check-manually) <span class="intermediate">Intermediate</span>
48. [How do you use `Array.prototype.reduce` to group objects by a property?](#q48-how-do-you-use-array.prototype.reduce-to-group-objects-by-a-property) <span class="intermediate">Intermediate</span>
49. [How do you implement a custom `Promise.race`?](#q49-how-do-you-implement-a-custom-promise.race) <span class="advanced">Advanced</span>
50. [How do you use `Symbol.iterator` to make an object iterable?](#q50-how-do-you-use-symbol.iterator-to-make-an-object-iterable) <span class="advanced">Advanced</span>
31. [How do you use the Proxy API to validate object property assignments?](#q31-how-do-you-use-the-proxy-api-to-validate-object-property-assignments) <span class="advanced">Advanced</span>
32. [What is the Reflect API and how does it differ from Proxy?](#q32-what-is-the-reflect-api-and-how-does-it-differ-from-proxy) <span class="advanced">Advanced</span>
33. [How do you implement a deep equality check for two objects?](#q33-how-do-you-implement-a-deep-equality-check-for-two-objects) <span class="advanced">Advanced</span>
34. [How can you use Set to remove duplicates from an array?](#q34-how-can-you-use-set-to-remove-duplicates-from-an-array) <span class="intermediate">Intermediate</span>
35. [What is a WeakMap and why is it useful for memory management?](#q35-what-is-a-weakmap-and-why-is-it-useful-for-memory-management) <span class="advanced">Advanced</span>
36. [How do you implement an ID generator using Generators?](#q36-how-do-you-implement-an-id-generator-using-generators) <span class="intermediate">Intermediate</span>
37. [How does requestAnimationFrame differ from setTimeout for animations?](#q37-how-does-requestanimationframe-differ-from-settimeout-for-animations) <span class="intermediate">Intermediate</span>
38. [How do you use Web Workers to offload CPU-intensive tasks?](#q38-how-do-you-use-web-workers-to-offload-cpu-intensive-tasks) <span class="advanced">Advanced</span>
39. [Explain the difference between null and undefined with a practical example.](#q39-explain-the-difference-between-null-and-undefined-with-a-practical-example.) <span class="beginner">Beginner</span>
40. [How do you use the Intl API for language-sensitive number formatting?](#q40-how-do-you-use-the-intl-api-for-language-sensitive-number-formatting) <span class="intermediate">Intermediate</span>
41. [What is BigInt and when should you use it?](#q41-what-is-bigint-and-when-should-you-use-it) <span class="intermediate">Intermediate</span>
42. [Explain the Nullish Coalescing Operator (??) vs Logical OR (||).](#q42-explain-the-nullish-coalescing-operator--vs-logical-or-||.) <span class="intermediate">Intermediate</span>
43. [How does Optional Chaining (?.) simplify accessing nested properties?](#q43-how-does-optional-chaining-.-simplify-accessing-nested-properties) <span class="beginner">Beginner</span>
44. [What is globalThis and why is it needed?](#q44-what-is-globalthis-and-why-is-it-needed) <span class="intermediate">Intermediate</span>
45. [Explain the 'Classic Closure Loop' problem and how to fix it.](#q45-explain-the-classic-closure-loop-problem-and-how-to-fix-it.) <span class="intermediate">Intermediate</span>
46. [Function Declaration vs Function Expression: What is the difference?](#q46-function-declaration-vs-function-expression:-what-is-the-difference) <span class="beginner">Beginner</span>
47. [How do you implement a GroupBy function using Array.reduce?](#q47-how-do-you-implement-a-groupby-function-using-array.reduce) <span class="advanced">Advanced</span>
48. [How do you implement Promise.race from scratch?](#q48-how-do-you-implement-promise.race-from-scratch) <span class="advanced">Advanced</span>
49. [How do you make an object iterable (usable in for...of)?](#q49-how-do-you-make-an-object-iterable-usable-in-for...of) <span class="advanced">Advanced</span>
50. [How can you flatten a nested array of arbitrary depth?](#q50-how-can-you-flatten-a-nested-array-of-arbitrary-depth) <span class="intermediate">Intermediate</span>
51. [How does the Event Loop work?](#q51-how-does-the-event-loop-work) <span class="advanced">Advanced</span>
52. [What is a Closure?](#q52-what-is-a-closure) <span class="intermediate">Intermediate</span>
53. [Difference between `var`, `let`, and `const`?](#q53-difference-between-var-let-and-const) <span class="beginner">Beginner</span>
54. [What is `this` keyword?](#q54-what-is-this-keyword) <span class="intermediate">Intermediate</span>
55. [How does Prototypal Inheritance work?](#q55-how-does-prototypal-inheritance-work) <span class="advanced">Advanced</span>
56. [What is a Promise?](#q56-what-is-a-promise) <span class="beginner">Beginner</span>
57. [How does `async/await` work?](#q57-how-does-asyncawait-work) <span class="intermediate">Intermediate</span>
58. [What is Hoisting?](#q58-what-is-hoisting) <span class="intermediate">Intermediate</span>
59. [Difference between `null` and `undefined`?](#q59-difference-between-null-and-undefined) <span class="beginner">Beginner</span>
60. [What is Event Bubbling vs Capturing?](#q60-what-is-event-bubbling-vs-capturing) <span class="intermediate">Intermediate</span>
61. [How do you implement a deep clone?](#q61-how-do-you-implement-a-deep-clone) <span class="intermediate">Intermediate</span>
62. [What is a Generator function?](#q62-what-is-a-generator-function) <span class="advanced">Advanced</span>
63. [What is the Proxy object?](#q63-what-is-the-proxy-object) <span class="advanced">Advanced</span>
64. [Difference between `==` and `===`?](#q64-difference-between-==-and-===) <span class="beginner">Beginner</span>
65. [What is `bind`, `call`, and `apply`?](#q65-what-is-bind-call-and-apply) <span class="intermediate">Intermediate</span>
66. [What is a WeakMap?](#q66-what-is-a-weakmap) <span class="advanced">Advanced</span>
67. [How do you handle errors in Promises?](#q67-how-do-you-handle-errors-in-promises) <span class="intermediate">Intermediate</span>
68. [What is Currying?](#q68-what-is-currying) <span class="intermediate">Intermediate</span>
69. [What is the Temporal Dead Zone (TDZ)?](#q69-what-is-the-temporal-dead-zone-tdz) <span class="advanced">Advanced</span>
70. [What is a Polyfill?](#q70-what-is-a-polyfill) <span class="beginner">Beginner</span>
71. [How do you debounce a function?](#q71-how-do-you-debounce-a-function) <span class="intermediate">Intermediate</span>
72. [How do you throttle a function?](#q72-how-do-you-throttle-a-function) <span class="intermediate">Intermediate</span>
73. [What is the `module` pattern?](#q73-what-is-the-module-pattern) <span class="intermediate">Intermediate</span>
74. [What is `localStorage` vs `sessionStorage`?](#q74-what-is-localstorage-vs-sessionstorage) <span class="beginner">Beginner</span>
75. [How do you check array equality?](#q75-how-do-you-check-array-equality) <span class="intermediate">Intermediate</span>
76. [What is `Symbol`?](#q76-what-is-symbol) <span class="intermediate">Intermediate</span>
77. [What is `Reflect` API?](#q77-what-is-reflect-api) <span class="advanced">Advanced</span>
78. [How do you flatten an array?](#q78-how-do-you-flatten-an-array) <span class="beginner">Beginner</span>
79. [What is strict mode?](#q79-what-is-strict-mode) <span class="beginner">Beginner</span>
80. [How do you implement a Set?](#q80-how-do-you-implement-a-set) <span class="beginner">Beginner</span>
81. [What is `Intl` API?](#q81-what-is-intl-api) <span class="intermediate">Intermediate</span>
82. [How do you detect browser vs node?](#q82-how-do-you-detect-browser-vs-node) <span class="beginner">Beginner</span>
83. [What is an IIFE?](#q83-what-is-an-iife) <span class="beginner">Beginner</span>
84. [How do you remove duplicates from array?](#q84-how-do-you-remove-duplicates-from-array) <span class="beginner">Beginner</span>
85. [What is Object.freeze?](#q85-what-is-object.freeze) <span class="intermediate">Intermediate</span>
86. [What is `requestAnimationFrame`?](#q86-what-is-requestanimationframe) <span class="intermediate">Intermediate</span>
87. [How do you stop event propagation?](#q87-how-do-you-stop-event-propagation) <span class="beginner">Beginner</span>
88. [What is `Promise.all`?](#q88-what-is-promise.all) <span class="intermediate">Intermediate</span>
89. [What is `Promise.race`?](#q89-what-is-promise.race) <span class="intermediate">Intermediate</span>
90. [What is `BigInt`?](#q90-what-is-bigint) <span class="beginner">Beginner</span>
91. [How do you merge objects?](#q91-how-do-you-merge-objects) <span class="beginner">Beginner</span>
92. [What is Optional Chaining?](#q92-what-is-optional-chaining) <span class="beginner">Beginner</span>
93. [What is Nullish Coalescing?](#q93-what-is-nullish-coalescing) <span class="beginner">Beginner</span>
94. [How do you iterate object keys?](#q94-how-do-you-iterate-object-keys) <span class="beginner">Beginner</span>
95. [What is `globalThis`?](#q95-what-is-globalthis) <span class="beginner">Beginner</span>
96. [How do you parse URL parameters?](#q96-how-do-you-parse-url-parameters) <span class="beginner">Beginner</span>
97. [What is the difference between `slice` and `splice`?](#q97-what-is-the-difference-between-slice-and-splice) <span class="beginner">Beginner</span>
98. [How do you copy to clipboard?](#q98-how-do-you-copy-to-clipboard) <span class="intermediate">Intermediate</span>
99. [What is a service worker?](#q99-what-is-a-service-worker) <span class="advanced">Advanced</span>
100. [How do you check for NaN?](#q100-how-do-you-check-for-nan) <span class="beginner">Beginner</span>

---

### Q1: How do you implement a robust debounce function with immediate execution option?

**Difficulty:** Intermediate

**Strategy:**
Debouncing forces a function to wait a certain amount of time before running again. The function is built by using a timer variable that is cleared and reset on every call. If `immediate` is passed, the function triggers on the leading edge instead of the trailing edge.

**Code Snippet:**
```javascript
function debounce(func, wait, immediate) {
  let timeout;
  return function(...args) {
    const context = this;
    const later = function() {
      timeout = null;
      if (!immediate) func.apply(context, args);
    };
    const callNow = immediate && !timeout;
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
    if (callNow) func.apply(context, args);
  };
}

// Usage
const myEfficientFn = debounce(function() {
  // All the heavy lifting
  console.log('Function executed');
}, 250);

window.addEventListener('resize', myEfficientFn);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q2: How do you deeply clone an object handling circular references and special types?

**Difficulty:** Intermediate

**Strategy:**
`JSON.parse(JSON.stringify(obj))` is simple but fails on Dates, RegExps, functions, and circular references. A robust solution involves recursion and a `WeakMap` to track visited objects to handle circular references.

**Code Snippet:**
```javascript
function deepClone(obj, hash = new WeakMap()) {
  if (Object(obj) !== obj) return obj; // primitives
  if (hash.has(obj)) return hash.get(obj); // cyclic reference

  let result;
  if (obj instanceof Set) {
    result = new Set(obj); // See note below
  } else if (obj instanceof Map) {
    result = new Map(Array.from(obj, ([key, val]) => 
      [key, deepClone(val, hash)]));
  } else if (obj instanceof Date) {
    result = new Date(obj);
  } else if (obj instanceof RegExp) {
    result = new RegExp(obj.source, obj.flags);
  } else if (typeof obj === 'function') {
    return obj; // functions are typically not cloned
  } else {
    result = Array.isArray(obj) ? [] : {};
    hash.set(obj, result);
    for (let key in obj) {
      if (Object.prototype.hasOwnProperty.call(obj, key)) {
        result[key] = deepClone(obj[key], hash);
      }
    }
  }
  return result;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q3: How do you implement a custom Promise.allSettled() polyfill?

**Difficulty:** Intermediate

**Strategy:**
`Promise.allSettled` waits for all promises to finish, regardless of success or failure. We can map over the input array and transform each promise into one that always resolves with a status object.

**Code Snippet:**
```javascript
function allSettled(promises) {
  return Promise.all(
    promises.map(promise =>
      Promise.resolve(promise)
        .then(value => ({ status: 'fulfilled', value }))
        .catch(reason => ({ status: 'rejected', reason }))
    )
  );
}

// Usage
allSettled([
  Promise.resolve(1),
  Promise.reject('error'),
  Promise.resolve(3)
]).then(console.log);
// [{status: 'fulfilled', value: 1}, {status: 'rejected', reason: 'error'}, ...]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q4: How do you efficiently flatten a deeply nested array without using `Array.prototype.flat`?

**Difficulty:** Intermediate

**Strategy:**
We can use recursion or a stack-based iterative approach. The iterative approach (using a stack) is safer for very deep arrays to avoid stack overflow errors.

**Code Snippet:**
```javascript
function flatten(arr) {
  const result = [];
  const stack = [...arr];
  
  while (stack.length) {
    const next = stack.pop();
    if (Array.isArray(next)) {
      stack.push(...next);
    } else {
      result.push(next);
    }
  }
  // The stack approach reverses order, so we reverse back
  return result.reverse();
}

// Recursive one-liner (simpler but risk of stack overflow)
const flattenRecursive = (arr) => 
  arr.reduce((acc, val) => 
    Array.isArray(val) ? acc.concat(flattenRecursive(val)) : acc.concat(val), 
  []);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q5: How do you implement function composition (pipe) from scratch?

**Difficulty:** Advanced

**Strategy:**
Composition combines multiple functions where the output of one becomes the input of the next. `pipe` goes left-to-right, while `compose` goes right-to-left.

**Code Snippet:**
```javascript
const pipe = (...fns) => (x) => fns.reduce((v, f) => f(v), x);

const compose = (...fns) => (x) => fns.reduceRight((v, f) => f(v), x);

// Usage
const add5 = x => x + 5;
const multiply2 = x => x * 2;
const toString = x => `Result: ${x}`;

const process = pipe(add5, multiply2, toString);
console.log(process(5)); // (5+5)*2 = 20 -> "Result: 20"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q6: How do you implement an event emitter (Pub/Sub pattern) from scratch?

**Difficulty:** Advanced

**Strategy:**
Create a class with a storage object for events. Methods needed: `on` (subscribe), `off` (unsubscribe), `emit` (publish), and optionally `once`.

**Code Snippet:**
```javascript
class EventEmitter {
  constructor() {
    this.events = {};
  }

  on(event, listener) {
    if (!this.events[event]) {
      this.events[event] = [];
    }
    this.events[event].push(listener);
    return () => this.off(event, listener); // Return unsubscribe function
  }

  off(event, listenerToRemove) {
    if (!this.events[event]) return;
    this.events[event] = this.events[event].filter(l => l !== listenerToRemove);
  }

  emit(event, ...args) {
    if (!this.events[event]) return;
    this.events[event].forEach(listener => listener(...args));
  }

  once(event, listener) {
    const remove = this.on(event, (...args) => {
      remove();
      listener(...args);
    });
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q7: How do you throttle a function to ensure it runs at most once every X milliseconds?

**Difficulty:** Advanced

**Strategy:**
Throttling ensures a function is called at most once in a specified time period. It's useful for scrolling events or window resizing where you don't want to block the UI.

**Code Snippet:**
```javascript
function throttle(func, limit) {
  let inThrottle;
  return function(...args) {
    const context = this;
    if (!inThrottle) {
      func.apply(context, args);
      inThrottle = true;
      setTimeout(() => inThrottle = false, limit);
    }
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q8: How do you implement a memoization function to cache expensive calculation results?

**Difficulty:** Advanced

**Strategy:**
Create a higher-order function that stores results in a cache (object or Map) keyed by the arguments. If called again with same args, return cached result.

**Code Snippet:**
```javascript
function memoize(fn) {
  const cache = new Map();
  return function(...args) {
    const key = JSON.stringify(args); // Simple key generation
    if (cache.has(key)) {
      return cache.get(key);
    }
    const result = fn.apply(this, args);
    cache.set(key, result);
    return result;
  }
}

// Usage
const factorial = memoize(n => (n <= 1 ? 1 : n * factorial(n - 1)));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q9: How do you parallelize async tasks with a concurrency limit?

**Difficulty:** Advanced

**Strategy:**
Use a queue or a recursive function that starts new tasks as old ones finish. This is crucial when scraping or making API calls to avoid rate limits.

**Code Snippet:**
```javascript
async function asyncPool(poolLimit, array, iteratorFn) {
  const ret = [];
  const executing = [];
  for (const item of array) {
    const p = Promise.resolve().then(() => iteratorFn(item));
    ret.push(p);

    if (poolLimit <= array.length) {
      const e = p.then(() => executing.splice(executing.indexOf(e), 1));
      executing.push(e);
      if (executing.length >= poolLimit) {
        await Promise.race(executing);
      }
    }
  }
  return Promise.all(ret);
}

// Usage
const timeout = i => new Promise(resolve => setTimeout(() => resolve(i), i));
asyncPool(2, [1000, 5000, 3000, 2000], timeout).then(console.log);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q10: How do you implement a custom `instanceof` operator?

**Difficulty:** Advanced

**Strategy:**
`instanceof` checks if the prototype property of a constructor appears anywhere in the prototype chain of an object.

**Code Snippet:**
```javascript
function myInstanceOf(obj, constructor) {
  if (obj == null) return false;
  
  let proto = Object.getPrototypeOf(obj);
  while (proto) {
    if (proto === constructor.prototype) {
      return true;
    }
    proto = Object.getPrototypeOf(proto);
  }
  return false;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q11: How do you implement currying to transform a function?

**Difficulty:** Advanced

**Strategy:**
Currying transforms `f(a, b, c)` into `f(a)(b)(c)`. It allows partial application of functions.

**Code Snippet:**
```javascript
function curry(fn) {
  return function curried(...args) {
    if (args.length >= fn.length) {
      return fn.apply(this, args);
    } else {
      return function(...args2) {
        return curried.apply(this, args.concat(args2));
      }
    }
  }
}

// Usage
const sum = (a, b, c) => a + b + c;
const curriedSum = curry(sum);
console.log(curriedSum(1)(2)(3)); // 6
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q12: How do you implement a custom Iterable using Symbol.iterator?

**Difficulty:** Intermediate

**Strategy:**
Any object can be made iterable by implementing a method keyed by `Symbol.iterator` that returns an object with a `next()` method.

**Code Snippet:**
```javascript
const range = {
  from: 1,
  to: 5,
  [Symbol.iterator]() {
    this.current = this.from;
    return this;
  },
  next() {
    if (this.current <= this.to) {
      return { done: false, value: this.current++ };
    } else {
      return { done: true };
    }
  }
};

for (let num of range) {
  console.log(num); // 1, 2, 3, 4, 5
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q13: How do you use Generators for asynchronous flow control?

**Difficulty:** Intermediate

**Strategy:**
Generators can pause execution with `yield`. When combined with Promises (async/await pattern precursor), they allow writing async code that looks synchronous.

**Code Snippet:**
```javascript
function* fetchUserFlow() {
  const user = yield fetch('/api/user').then(r => r.json());
  const posts = yield fetch(`/api/posts/${user.id}`).then(r => r.json());
  return posts;
}

function run(generator) {
  const iterator = generator();
  function iterate(iteration) {
    if (iteration.done) return iteration.value;
    const promise = iteration.value;
    return promise.then(x => iterate(iterator.next(x)));
  }
  return iterate(iterator.next());
}

run(fetchUserFlow).then(posts => console.log(posts));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q14: How do you use the IntersectionObserver API for lazy loading images?

**Difficulty:** Intermediate

**Strategy:**
The IntersectionObserver API asynchronously observes changes in the intersection of a target element with an ancestor element or the viewport.

**Code Snippet:**
```javascript
const observer = new IntersectionObserver((entries, observer) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const img = entry.target;
      img.src = img.dataset.src;
      img.classList.remove('lazy');
      observer.unobserve(img);
    }
  });
});

document.querySelectorAll('img.lazy').forEach(img => {
  observer.observe(img);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q15: How do you use the MutationObserver API to track DOM changes?

**Difficulty:** Intermediate

**Strategy:**
MutationObserver allows you to watch for changes being made to the DOM tree (attributes, child list, subtree).

**Code Snippet:**
```javascript
const targetNode = document.getElementById('content');
const config = { attributes: true, childList: true, subtree: true };

const callback = function(mutationsList, observer) {
  for(const mutation of mutationsList) {
    if (mutation.type === 'childList') {
      console.log('A child node has been added or removed.');
    } else if (mutation.type === 'attributes') {
      console.log('The ' + mutation.attributeName + ' attribute was modified.');
    }
  }
};

const observer = new MutationObserver(callback);
observer.observe(targetNode, config);

// Later: observer.disconnect();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q16: How do you implement a virtual list (windowing) for large datasets?

**Difficulty:** Intermediate

**Strategy:**
Only render the items that are currently visible in the viewport plus a small buffer. Calculate the total height to maintain scrollbar size.

**Code Snippet:**
```javascript
// Conceptual implementation
class VirtualList {
  constructor(container, itemHeight, totalItems) {
    this.container = container;
    this.itemHeight = itemHeight;
    this.totalItems = totalItems;
    this.render();
    this.container.addEventListener('scroll', () => this.render());
  }

  render() {
    const scrollTop = this.container.scrollTop;
    const viewportHeight = this.container.clientHeight;
    
    const startIndex = Math.floor(scrollTop / this.itemHeight);
    const endIndex = Math.min(
      this.totalItems, 
      Math.floor((scrollTop + viewportHeight) / this.itemHeight) + 5 // buffer
    );
    
    // Clear and re-render visible items
    this.container.innerHTML = '';
    // Add padding top
    const paddingTop = document.createElement('div');
    paddingTop.style.height = `${startIndex * this.itemHeight}px`;
    this.container.appendChild(paddingTop);
    
    for (let i = startIndex; i < endIndex; i++) {
      const item = document.createElement('div');
      item.innerText = `Item ${i}`;
      item.style.height = `${this.itemHeight}px`;
      this.container.appendChild(item);
    }
    
    // Add padding bottom
    const paddingBottom = document.createElement('div');
    paddingBottom.style.height = `${(this.totalItems - endIndex) * this.itemHeight}px`;
    this.container.appendChild(paddingBottom);
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q17: How do you optimize event listeners using event delegation?

**Difficulty:** Intermediate

**Strategy:**
Instead of attaching an event listener to every child element, attach a single listener to a common parent. Use `event.target` to identify which child was clicked.

**Code Snippet:**
```javascript
document.getElementById('parent-list').addEventListener('click', function(e) {
  // Check if the clicked element matches our target selector
  if (e.target && e.target.matches('li.item')) {
    console.log('List item clicked!', e.target.dataset.id);
  }
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q18: How do you prevent prototype pollution attacks?

**Difficulty:** Intermediate

**Strategy:**
Prototype pollution occurs when attackers merge properties into `Object.prototype`. Prevent it by using `Object.create(null)`, freezing the prototype, or carefully validating keys during merge operations.

**Code Snippet:**
```javascript
function safeMerge(target, source) {
  for (let key in source) {
    if (key === '__proto__' || key === 'constructor' || key === 'prototype') {
      continue; // Skip dangerous keys
    }
    if (typeof target[key] === 'object' && target[key] !== null) {
      safeMerge(target[key], source[key]);
    } else {
      target[key] = source[key];
    }
  }
  return target;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q19: How do you securely store tokens in the browser?

**Difficulty:** Intermediate

**Strategy:**
Do NOT store sensitive tokens (like JWTs giving access to sensitive data) in `localStorage` or `sessionStorage` due to XSS risks. Use **HttpOnly cookies** which are not accessible via JavaScript.

**Code Snippet:**
```javascript
// Server-side (Node/Express example)
res.cookie('token', jwt, {
  httpOnly: true,
  secure: true, // HTTPS only
  sameSite: 'Strict', // CSRF protection
  maxAge: 3600000
});

// Client-side: Browser handles sending the cookie automatically with requests.
// No JavaScript code needed to read/write the token.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q20: How do you implement CSRF protection in AJAX requests?

**Difficulty:** Intermediate

**Strategy:**
For non-GET requests, the server should provide a CSRF token (e.g., in a meta tag or cookie). The client must read this token and send it in a custom HTTP header (e.g., `X-CSRF-Token`).

**Code Snippet:**
```javascript
// 1. Get the token from meta tag (rendered by server)
const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

// 2. Send it in headers
fetch('/api/update', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'X-CSRF-Token': csrfToken
  },
  body: JSON.stringify({ data: 'value' })
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q21: How do you sanitize user input to prevent XSS?

**Difficulty:** Intermediate

**Strategy:**
Never trust user input. When rendering HTML, encode special characters. Libraries like DOMPurify are recommended.

**Code Snippet:**
```javascript
function escapeHTML(str) {
  return str.replace(/[&<>'"]/g, 
    tag => ({
      '&': '&amp;',
      '<': '&lt;',
      '>': '&gt;',
      "'": '&#39;',
      '"': '&quot;'
    }[tag])
  );
}

const userInput = "<script>alert('xss')</script>";
const safeOutput = escapeHTML(userInput);
document.body.innerHTML = safeOutput; // &lt;script&gt;alert('xss')&lt;/script&gt;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q22: How do you use the BroadcastChannel API for tab communication?

**Difficulty:** Intermediate

**Strategy:**
`BroadcastChannel` allows simple communication between browsing contexts (windows, tabs, frames, or iframes) of the same origin.

**Code Snippet:**
```javascript
// Tab 1: Sender
const channel = new BroadcastChannel('my_channel');
channel.postMessage('Hello from Tab 1');

// Tab 2: Receiver
const channel = new BroadcastChannel('my_channel');
channel.onmessage = (event) => {
  console.log('Received:', event.data);
};
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q23: How do you use SharedWorkers for shared state between tabs?

**Difficulty:** Intermediate

**Strategy:**
`SharedWorker` is a script that can be accessed by multiple windows, iframes or even workers.

**Code Snippet:**
```javascript
// worker.js
let connections = 0;
onconnect = function(e) {
  const port = e.ports[0];
  connections++;
  port.postMessage('Connection count: ' + connections);
  
  port.onmessage = function(e) {
    // Broadcast to logic would be more complex here
    port.postMessage('You said: ' + e.data);
  }
}

// main.js
const myWorker = new SharedWorker('worker.js');
myWorker.port.start();
myWorker.port.onmessage = function(e) {
  console.log('Worker said: ' + e.data);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q24: How do you implement a simple state management system from scratch?

**Difficulty:** Intermediate

**Strategy:**
Use the Pub/Sub pattern combined with a central store object.

**Code Snippet:**
```javascript
class Store {
  constructor(initialState = {}, reducer) {
    this.state = initialState;
    this.reducer = reducer;
    this.listeners = [];
  }

  getState() {
    return this.state;
  }

  dispatch(action) {
    this.state = this.reducer(this.state, action);
    this.listeners.forEach(listener => listener());
  }

  subscribe(listener) {
    this.listeners.push(listener);
    return () => {
      this.listeners = this.listeners.filter(l => l !== listener);
    };
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q25: How do you implement a client-side router from scratch?

**Difficulty:** Intermediate

**Strategy:**
Listen to `popstate` events for history changes and intercept link clicks to prevent page reload, using `history.pushState`.

**Code Snippet:**
```javascript
class Router {
  constructor(routes) {
    this.routes = routes;
    this.root = document.getElementById('app');
    window.addEventListener('popstate', () => this.loadRoute());
    document.body.addEventListener('click', e => {
      if (e.target.matches('[data-link]')) {
        e.preventDefault();
        history.pushState(null, null, e.target.href);
        this.loadRoute();
      }
    });
    this.loadRoute();
  }

  loadRoute() {
    const path = window.location.pathname;
    const view = this.routes[path] || this.routes['/404'];
    this.root.innerHTML = view;
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q26: How do you parse query string parameters without a library?

**Difficulty:** Intermediate

**Strategy:**
Use `URLSearchParams` (modern) or regex (legacy).

**Code Snippet:**
```javascript
// Modern approach
const params = new URLSearchParams(window.location.search);
const name = params.get('name');

// Legacy / Manual implementation
function getQueryParams(url) {
  const paramArr = url.slice(url.indexOf('?') + 1).split('&');
  const params = {};
  paramArr.map(param => {
    const [key, val] = param.split('=');
    params[key] = decodeURIComponent(val);
  });
  return params;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q27: How do you check if two objects are deeply equal?

**Difficulty:** Intermediate

**Strategy:**
Recursively compare keys and values.

**Code Snippet:**
```javascript
function deepEqual(obj1, obj2) {
  if (obj1 === obj2) return true;
  
  if (typeof obj1 !== 'object' || obj1 === null ||
      typeof obj2 !== 'object' || obj2 === null) {
    return false;
  }
  
  const keys1 = Object.keys(obj1);
  const keys2 = Object.keys(obj2);
  
  if (keys1.length !== keys2.length) return false;
  
  for (let key of keys1) {
    if (!keys2.includes(key) || !deepEqual(obj1[key], obj2[key])) {
      return false;
    }
  }
  
  return true;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q28: How do you retry a failed API call with exponential backoff?

**Difficulty:** Intermediate

**Strategy:**
Recursively call the fetch function, increasing the delay on each failure.

**Code Snippet:**
```javascript
async function fetchWithRetry(url, options = {}, retries = 3, delay = 1000) {
  try {
    const response = await fetch(url, options);
    if (!response.ok) throw new Error('Request failed');
    return response;
  } catch (error) {
    if (retries === 0) throw error;
    await new Promise(resolve => setTimeout(resolve, delay));
    return fetchWithRetry(url, options, retries - 1, delay * 2);
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q29: How do you cancel a fetch request using AbortController?

**Difficulty:** Intermediate

**Strategy:**
Pass the `signal` from an `AbortController` to the fetch request. Call `controller.abort()` to cancel.

**Code Snippet:**
```javascript
const controller = new AbortController();
const signal = controller.signal;

fetch('/api/data', { signal })
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(err => {
    if (err.name === 'AbortError') {
      console.log('Fetch aborted');
    } else {
      console.error('Fetch error:', err);
    }
  });

// Cancel request
controller.abort();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q30: How do you implement a custom `bind` function?

**Difficulty:** Advanced

**Strategy:**
`bind` returns a new function with `this` fixed to the passed context. It also needs to handle partial application of arguments.

**Code Snippet:**
```javascript
Function.prototype.myBind = function(context, ...args) {
  const fn = this;
  return function(...newArgs) {
    return fn.apply(context, [...args, ...newArgs]);
  }
}

// Usage
const person = { name: 'Alice' };
function greet(greeting) { console.log(`${greeting}, ${this.name}`); }
const greetAlice = greet.myBind(person, 'Hello');
greetAlice(); // Hello, Alice
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

### Q31: How do you use the Proxy API to validate object property assignments?

**Difficulty**: Advanced

**Strategy:**
Proxies allow you to intercept and redefine fundamental operations for an object. A `set` trap can be used to validate data before it is written to the object.

**Code Example:**
const validator = {
  set: function(obj, prop, value) {
    if (prop === 'age') {
      if (!Number.isInteger(value)) {
        throw new TypeError('The age must be an integer');
      }
      if (value < 0 || value > 200) {
        throw new RangeError('The age seems invalid');
      }
    }
    // The default behavior to store the value
    obj[prop] = value;
    return true;
  }
};

const person = new Proxy({}, validator);

person.age = 100; // OK
// person.age = 'young'; // Throws TypeError
// person.age = 300; // Throws RangeError

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q32: What is the Reflect API and how does it relate to Proxy?

**Difficulty**: Advanced

**Strategy:**
`Reflect` is a built-in object that provides methods for interceptable JavaScript operations. It is often used inside Proxy handlers to forward the default behavior safely.

**Code Example:**
const handler = {
  get(target, prop, receiver) {
    console.log(`Getting ${prop}`);
    // Reflect.get ensures correct 'this' binding (receiver)
    return Reflect.get(target, prop, receiver);
  }
};

const obj = new Proxy({ x: 1, get y() { return this.x; } }, handler);

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q33: When should you use a Map over a plain Object?

**Difficulty**: Intermediate

**Strategy:**
Use `Map` when: keys are not strings (e.g., objects), key order matters (insertion order is preserved), or you need frequent size checks (`.size`). Use `Object` for simple key-value pairs where keys are strings/symbols.

**Code Example:**
const map = new Map();
const keyObj = { id: 1 };

map.set(keyObj, 'Metadata for object');
console.log(map.get(keyObj)); // 'Metadata for object'

console.log(map.size); // 1

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q34: How do you efficiently remove duplicates from an array using Set?

**Difficulty**: Beginner

**Strategy:**
`Set` only stores unique values. You can convert an array to a Set and back to an array to remove duplicates.

**Code Example:**
const numbers = [1, 2, 2, 3, 4, 4, 5];
const uniqueNumbers = [...new Set(numbers)];
// [1, 2, 3, 4, 5]

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q35: What is a WeakMap and why is it useful for memory management?

**Difficulty**: Advanced

**Strategy:**
`WeakMap` holds 'weak' references to key objects, meaning if the key object is no longer referenced elsewhere, it can be garbage collected. This prevents memory leaks when associating data with DOM elements or objects.

**Code Example:**
let user = { name: "Alice" };

const weakMap = new WeakMap();
weakMap.set(user, "Secret Data");

user = null; 
// The entry in weakMap is now eligible for garbage collection automatically.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q36: How do you implement an ID generator using Generators?

**Difficulty**: Intermediate

**Strategy:**
Generators (`function*`) can maintain internal state and yield values one at a time, making them perfect for infinite sequences like IDs.

**Code Example:**
function* idGenerator() {
  let id = 1;
  while (true) {
    yield id++;
  }
}

const gen = idGenerator();
console.log(gen.next().value); // 1
console.log(gen.next().value); // 2

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q37: Why is `requestAnimationFrame` better than `setTimeout` for animations?

**Difficulty**: Intermediate

**Strategy:**
`requestAnimationFrame` syncs with the browser's refresh rate (usually 60fps), pausing when the tab is inactive to save battery, whereas `setTimeout` runs blindly and can cause jank.

**Code Example:**
function animate() {
  // Update animation state
  element.style.left = parseInt(element.style.left || 0) + 1 + 'px';
  
  // Schedule next frame
  requestAnimationFrame(animate);
}

requestAnimationFrame(animate);

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q38: How do you offload heavy CPU tasks using Web Workers?

**Difficulty**: Advanced

**Strategy:**
Web Workers run scripts in background threads, preventing the main UI thread from blocking.

**Code Example:**
// worker.js
self.onmessage = function(e) {
  // Heavy computation
  let result = 0;
  for (let i = 0; i < 1000000000; i++) result += i;
  self.postMessage(result);
};

// main.js
const worker = new Worker('worker.js');
worker.onmessage = function(e) {
  console.log('Result:', e.data);
};
worker.postMessage('start');

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q39: What is the difference between `null` and `undefined`?

**Difficulty**: Beginner

**Strategy:**
`undefined` means a variable has been declared but not assigned a value. `null` is an assignment value that represents no value or no object.

**Code Example:**
let a; 
console.log(a); // undefined

let b = null;
console.log(b); // null

console.log(typeof undefined); // 'undefined'
console.log(typeof null); // 'object' (legacy bug)

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q40: How do you use the `Intl` API for language-sensitive formatting?

**Difficulty**: Intermediate

**Strategy:**
`Intl` provides standard APIs for formatting dates, numbers, and currencies across different locales.

**Code Example:**
const number = 123456.789;

console.log(new Intl.NumberFormat('de-DE', { style: 'currency', currency: 'EUR' }).format(number));
// 123.456,79 €

console.log(new Intl.NumberFormat('ja-JP', { style: 'currency', currency: 'JPY' }).format(number));
// ￥123,457

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q41: What is `BigInt` and when should you use it?

**Difficulty**: Intermediate

**Strategy:**
`BigInt` is a primitive wrapper for whole numbers larger than `2^53 - 1` (Number.MAX_SAFE_INTEGER).

**Code Example:**
const max = Number.MAX_SAFE_INTEGER;
console.log(max + 1 === max + 2); // true (Precision lost)

const big = 9007199254740991n;
console.log(big + 1n === big + 2n); // false (Precision kept)

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q42: What is the difference between Nullish Coalescing (`??`) and Logical OR (`||`)?

**Difficulty**: Intermediate

**Strategy:**
`||` returns the right side if the left is *falsy* (null, undefined, 0, '', false). `??` returns the right side only if the left is *null* or *undefined*.

**Code Example:**
const count = 0;

const a = count || 10; // 10 (0 is falsy)
const b = count ?? 10; // 0 (0 is defined)

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q43: How does Optional Chaining (`?.`) simplify object access?

**Difficulty**: Beginner

**Strategy:**
It allows you to read the value of a property located deep within a chain of connected objects without having to check that each reference in the chain is valid.

**Code Example:**
const user = { address: null };

// Old way
const zip = user && user.address && user.address.zip;

// New way
const zipNew = user?.address?.zip; // undefined (no error thrown)

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q44: What is `globalThis`?

**Difficulty**: Intermediate

**Strategy:**
`globalThis` provides a standard way to access the global `this` value (window in browser, global in Node.js) across environments.

**Code Example:**
// Works in Browser, Node, and Workers
console.log(globalThis); 

if (typeof globalThis.setTimeout !== 'function') {
  // ...
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q45: Explain the 'Classic Closure Loop' problem and how to fix it.

**Difficulty**: Intermediate

**Strategy:**
Using `var` in a loop creates a single shared binding. Using `let` creates a new binding for each iteration.

**Code Example:**
// Problem (var)
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);
}
// Output: 3, 3, 3

// Fix (let)
for (let i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);
}
// Output: 0, 1, 2

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q46: What is the difference between Function Declaration and Function Expression regarding Hoisting?

**Difficulty**: Beginner

**Strategy:**
Function declarations are hoisted completely (can be called before definition). Function expressions (assigned to variables) are not hoisted (variable is hoisted but undefined).

**Code Example:**
sayHello(); // Works
function sayHello() { console.log("Hello"); }

// sayHi(); // Error: sayHi is not a function
var sayHi = function() { console.log("Hi"); };

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q47: How do you perform a deep equality check manually?

**Difficulty**: Intermediate

**Strategy:**
Recursively compare keys and values. Handle primitives, arrays, and objects.

**Code Example:**
function deepEqual(obj1, obj2) {
  if (obj1 === obj2) return true;
  
  if (typeof obj1 !== 'object' || obj1 === null ||
      typeof obj2 !== 'object' || obj2 === null) {
    return false;
  }

  const keys1 = Object.keys(obj1);
  const keys2 = Object.keys(obj2);

  if (keys1.length !== keys2.length) return false;

  for (let key of keys1) {
    if (!keys2.includes(key) || !deepEqual(obj1[key], obj2[key])) {
      return false;
    }
  }
  return true;
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q48: How do you use `Array.prototype.reduce` to group objects by a property?

**Difficulty**: Intermediate

**Strategy:**
Use `reduce` to accumulate an object where keys are the group names and values are arrays of items.

**Code Example:**
const people = [
  { name: 'Alice', age: 20 },
  { name: 'Bob', age: 20 },
  { name: 'Charlie', age: 25 }
];

const grouped = people.reduce((acc, person) => {
  const key = person.age;
  if (!acc[key]) {
    acc[key] = [];
  }
  acc[key].push(person);
  return acc;
}, {});

// { '20': [{...}, {...}], '25': [{...}] }

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q49: How do you implement a custom `Promise.race`?

**Difficulty**: Advanced

**Strategy:**
Return a new Promise that resolves or rejects as soon as the first promise in the iterable resolves or rejects.

**Code Example:**
function race(promises) {
  return new Promise((resolve, reject) => {
    promises.forEach(promise => {
      Promise.resolve(promise)
        .then(resolve)
        .catch(reject);
    });
  });
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q50: How do you use `Symbol.iterator` to make an object iterable?

**Difficulty**: Advanced

**Strategy:**
Define a method with key `[Symbol.iterator]` that returns an iterator object (with a `next` method).

**Code Example:**
const range = {
  from: 1,
  to: 5,
  [Symbol.iterator]() {
    let current = this.from;
    let last = this.to;
    return {
      next() {
        if (current <= last) {
          return { done: false, value: current++ };
        } else {
          return { done: true };
        }
      }
    };
  }
};

for (let num of range) {
  console.log(num); // 1, 2, 3, 4, 5
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---


### Q31: How do you use the Proxy API to validate object property assignments?

**Difficulty**: Advanced

**Strategy:**
Proxies allow you to intercept and redefine fundamental operations for an object. A `set` trap can be used to validate data before it is written to the object.

**Code Example:**
const validator = {
  set: function(obj, prop, value) {
    if (prop === 'age') {
      if (!Number.isInteger(value)) {
        throw new TypeError('The age must be an integer');
      }
      if (value < 0 || value > 200) {
        throw new RangeError('The age seems invalid');
      }
    }
    // The default behavior to store the value
    obj[prop] = value;
    return true;
  }
};

const person = new Proxy({}, validator);

person.age = 100; // OK
// person.age = 'young'; // Throws TypeError
// person.age = 300; // Throws RangeError

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q32: What is the Reflect API and how does it differ from Proxy?

**Difficulty**: Advanced

**Strategy:**
Reflect is a built-in object that provides methods for interceptable JavaScript operations. It is often used within Proxy traps to forward the default behavior to the target object safely.

**Code Example:**
const handler = {
  get(target, prop, receiver) {
    console.log(`Getting ${prop}`);
    // Reflect.get forwards the operation to the original object
    return Reflect.get(target, prop, receiver);
  }
};

const obj = { name: "Alice" };
const proxy = new Proxy(obj, handler);

console.log(proxy.name); 
// Output:
// Getting name
// Alice

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q33: How do you implement a deep equality check for two objects?

**Difficulty**: Advanced

**Strategy:**
A deep equality check recursively compares properties of objects. For simple cases, `JSON.stringify` works, but it handles dates and circular references poorly. A recursive function is more robust.

**Code Example:**
function deepEqual(obj1, obj2) {
  if (obj1 === obj2) return true;

  if (typeof obj1 !== 'object' || obj1 === null || 
      typeof obj2 !== 'object' || obj2 === null) {
    return false;
  }

  const keys1 = Object.keys(obj1);
  const keys2 = Object.keys(obj2);

  if (keys1.length !== keys2.length) return false;

  for (let key of keys1) {
    if (!keys2.includes(key) || !deepEqual(obj1[key], obj2[key])) {
      return false;
    }
  }
  return true;
}

const a = { x: 1, y: { z: 2 } };
const b = { x: 1, y: { z: 2 } };
console.log(deepEqual(a, b)); // true

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q34: How can you use Set to remove duplicates from an array?

**Difficulty**: Intermediate

**Strategy:**
`Set` objects are collections of values where each value must be unique. Converting an array to a Set and back to an array is a concise way to remove duplicates.

**Code Example:**
const numbers = [1, 2, 2, 3, 4, 4, 5];
const uniqueNumbers = [...new Set(numbers)];

console.log(uniqueNumbers); // [1, 2, 3, 4, 5]

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q35: What is a WeakMap and why is it useful for memory management?

**Difficulty**: Advanced

**Strategy:**
`WeakMap` holds 'weak' references to key objects, meaning if the key object is no longer referenced elsewhere, it can be garbage collected. This prevents memory leaks when associating data with DOM elements or objects.

**Code Example:**
let user = { name: "Alice" };

const weakMap = new WeakMap();
weakMap.set(user, "Secret Data");

// If we remove the reference to user...
user = null; 

// The entry in weakMap is now eligible for garbage collection automatically.
// Unlike Map, you cannot iterate over keys in WeakMap.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q36: How do you implement an ID generator using Generators?

**Difficulty**: Intermediate

**Strategy:**
Generators can maintain internal state and yield values on demand, making them perfect for creating infinite sequences like unique IDs.

**Code Example:**
function* idGenerator() {
  let id = 1;
  while (true) {
    yield id++;
  }
}

const gen = idGenerator();

console.log(gen.next().value); // 1
console.log(gen.next().value); // 2
console.log(gen.next().value); // 3

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q37: How does requestAnimationFrame differ from setTimeout for animations?

**Difficulty**: Intermediate

**Strategy:**
`requestAnimationFrame` tells the browser that you wish to perform an animation and requests that the browser call a specified function to update an animation before the next repaint. It is more efficient than `setTimeout` because it pauses when the tab is inactive and syncs with the monitor's refresh rate.

**Code Example:**
function animate() {
  const element = document.getElementById('box');
  let pos = 0;

  function step() {
    pos++;
    element.style.left = pos + 'px';
    if (pos < 300) {
      requestAnimationFrame(step);
    }
  }

  requestAnimationFrame(step);
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q38: How do you use Web Workers to offload CPU-intensive tasks?

**Difficulty**: Advanced

**Strategy:**
Web Workers run a script in the background, separate from the main execution thread of a web application. This allows the main thread (usually the UI) to run without being blocked/frozen.

**Code Example:**
// main.js
const worker = new Worker('worker.js');

worker.postMessage(1000000000); // Send data to worker

worker.onmessage = function(e) {
  console.log('Result from worker:', e.data);
};

// worker.js
onmessage = function(e) {
  let sum = 0;
  for (let i = 0; i < e.data; i++) {
    sum += i;
  }
  postMessage(sum); // Send result back to main thread
};

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q39: Explain the difference between null and undefined with a practical example.

**Difficulty**: Beginner

**Strategy:**
`undefined` means a variable has been declared but not defined. `null` is an assignment value that represents no value or no object. `null` is an object, `undefined` is a type.

**Code Example:**
let a;
console.log(a); // undefined (automatically assigned)

let b = null;
console.log(b); // null (intentionally assigned)

console.log(typeof a); // "undefined"
console.log(typeof b); // "object" (a known JS quirk)

// Practical difference in default parameters
function greet(name = 'Guest') {
  return `Hello, ${name}`;
}

console.log(greet(undefined)); // "Hello, Guest"
console.log(greet(null));      // "Hello, null" 

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q40: How do you use the Intl API for language-sensitive number formatting?

**Difficulty**: Intermediate

**Strategy:**
The `Intl.NumberFormat` object enables language-sensitive number formatting.

**Code Example:**
const number = 123456.789;

// US English
console.log(new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(number));
// "$123,456.79"

// German
console.log(new Intl.NumberFormat('de-DE', { style: 'currency', currency: 'EUR' }).format(number));
// "123.456,79 €" 

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q41: What is BigInt and when should you use it?

**Difficulty**: Intermediate

**Strategy:**
`BigInt` is a built-in object that provides a way to represent whole numbers larger than 2^53 - 1, which is the largest number JavaScript can reliably represent with the Number primitive.

**Code Example:**
const maxSafe = Number.MAX_SAFE_INTEGER;
console.log(maxSafe + 1); // 9007199254740992
console.log(maxSafe + 2); // 9007199254740992 (Error!)

const bigInt = 9007199254740991n;
console.log(bigInt + 2n); // 9007199254740993n (Correct)

// Note: You cannot mix BigInt and other types
// console.log(1n + 2); // TypeError

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q42: Explain the Nullish Coalescing Operator (??) vs Logical OR (||).

**Difficulty**: Intermediate

**Strategy:**
The logical OR (`||`) operator returns the right-hand side operand if the left-hand side is *falsy* (including 0, '', false). The nullish coalescing operator (`??`) returns the right-hand side only if the left-hand side is `null` or `undefined`.

**Code Example:**
const count = 0;
const text = "";

const qty = count || 42;
const message = text || "Hello";

console.log(qty);     // 42 (because 0 is falsy)
console.log(message); // "Hello" (because "" is falsy)

const qty2 = count ?? 42;
const message2 = text ?? "Hello";

console.log(qty2);     // 0 (0 is not null/undefined)
console.log(message2); // "" ("" is not null/undefined)

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q43: How does Optional Chaining (?.) simplify accessing nested properties?

**Difficulty**: Beginner

**Strategy:**
Optional chaining (`?.`) permits reading the value of a property located deep within a chain of connected objects without having to expressly validate that each reference in the chain is valid.

**Code Example:**
const user = {
  profile: {
    // address is missing
  }
};

// Old way
const street = user && user.profile && user.profile.address && user.profile.address.street;

// New way with Optional Chaining
const street2 = user?.profile?.address?.street;

console.log(street2); // undefined (no error thrown)

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q44: What is globalThis and why is it needed?

**Difficulty**: Intermediate

**Strategy:**
`globalThis` provides a standard way to access the global `this` value (and hence the global object) across environments (window in browser, global in Node.js, self in Workers).

**Code Example:**
// Before globalThis, accessing the global object was environment-specific:
const getGlobal = () => {
  if (typeof self !== 'undefined') { return self; }
  if (typeof window !== 'undefined') { return window; }
  if (typeof global !== 'undefined') { return global; }
  throw new Error('unable to locate global object');
};

// With globalThis
console.log(globalThis); // Works everywhere

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q45: Explain the 'Classic Closure Loop' problem and how to fix it.

**Difficulty**: Intermediate

**Strategy:**
Using `var` in a loop with an asynchronous callback often leads to the same final value being used for all iterations because `var` is function-scoped. Using `let` (block-scoped) fixes this.

**Code Example:**
// Problematic code
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);
}
// Output: 3, 3, 3

// Fix with let
for (let j = 0; j < 3; j++) {
  setTimeout(() => console.log(j), 100);
}
// Output: 0, 1, 2

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q46: Function Declaration vs Function Expression: What is the difference?

**Difficulty**: Beginner

**Strategy:**
Function declarations are hoisted, meaning they can be called before they are defined. Function expressions (assigned to variables) are not hoisted.

**Code Example:**
console.log(hoistedFunc()); // Works: "I am hoisted"
// console.log(notHoisted()); // Error: notHoisted is not a function

function hoistedFunc() {
  return "I am hoisted";
}

var notHoisted = function() {
  return "I am not hoisted";
};

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q47: How do you implement a GroupBy function using Array.reduce?

**Difficulty**: Advanced

**Strategy:**
`Array.reduce` is a powerful method that can transform an array into any structure, including an object grouping elements by a key.

**Code Example:**
const people = [
  { name: 'Alice', age: 21 },
  { name: 'Bob', age: 25 },
  { name: 'Charlie', age: 21 }
];

const groupedByAge = people.reduce((acc, person) => {
  const key = person.age;
  if (!acc[key]) {
    acc[key] = [];
  }
  acc[key].push(person);
  return acc;
}, {});

console.log(groupedByAge);
/*
{
  '21': [ { name: 'Alice', age: 21 }, { name: 'Charlie', age: 21 } ],
  '25': [ { name: 'Bob', age: 25 } ]
}
*/

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q48: How do you implement Promise.race from scratch?

**Difficulty**: Advanced

**Strategy:**
`Promise.race` returns a promise that fulfills or rejects as soon as one of the promises in an iterable fulfills or rejects.

**Code Example:**
function myPromiseRace(promises) {
  return new Promise((resolve, reject) => {
    for (const p of promises) {
      Promise.resolve(p)
        .then(resolve)
        .catch(reject);
    }
  });
}

const p1 = new Promise(r => setTimeout(r, 500, 'one'));
const p2 = new Promise(r => setTimeout(r, 100, 'two'));

myPromiseRace([p1, p2]).then(value => {
  console.log(value); // "two"
});

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q49: How do you make an object iterable (usable in for...of)?

**Difficulty**: Advanced

**Strategy:**
To make an object iterable, you must implement the `[Symbol.iterator]` method, which returns an iterator (an object with a `next()` method).

**Code Example:**
const range = {
  from: 1,
  to: 5,
  
  [Symbol.iterator]() {
    this.current = this.from;
    return this;
  },
  
  next() {
    if (this.current <= this.to) {
      return { done: false, value: this.current++ };
    } else {
      return { done: true };
    }
  }
};

for (let num of range) {
  console.log(num); // 1, 2, 3, 4, 5
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q50: How can you flatten a nested array of arbitrary depth?

**Difficulty**: Intermediate

**Strategy:**
Modern JS has `Array.prototype.flat(Infinity)`, but implementing it recursively demonstrates understanding of recursion and array manipulation.

**Code Example:**
const nested = [1, [2, [3, [4]], 5]];

// Modern way
console.log(nested.flat(Infinity)); // [1, 2, 3, 4, 5]

// Recursive implementation
function flatten(arr) {
  return arr.reduce((acc, val) => 
    Array.isArray(val) ? acc.concat(flatten(val)) : acc.concat(val), 
  []);
}

console.log(flatten(nested)); // [1, 2, 3, 4, 5]

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---



### Q51: How does the Event Loop work?

**Difficulty**: Advanced

**Strategy**:
Call Stack -> Microtasks (Promises) -> Macrotasks (setTimeout) -> Render.

**Code Example**:
```javascript
Promise.resolve().then(() => console.log('Micro'));
setTimeout(() => console.log('Macro'), 0);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q52: What is a Closure?

**Difficulty**: Intermediate

**Strategy**:
Function bundled with its lexical environment. Accesses outer variables.

**Code Example**:
```javascript
function outer() { let x = 10; return () => x; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q53: Difference between `var`, `let`, and `const`?

**Difficulty**: Beginner

**Strategy**:
`var`: function scope, hoisted. `let`/`const`: block scope, TDZ. `const`: immutable reference.

**Code Example**:
```javascript
const x = 1;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q54: What is `this` keyword?

**Difficulty**: Intermediate

**Strategy**:
Refers to the object executing the function. Depends on call site.

**Code Example**:
```javascript
obj.method() // this = obj
func() // this = global/undefined
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q55: How does Prototypal Inheritance work?

**Difficulty**: Advanced

**Strategy**:
Objects inherit from other objects via `__proto__` chain.

**Code Example**:
```javascript
function Dog() {}; Dog.prototype = Object.create(Animal.prototype);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q56: What is a Promise?

**Difficulty**: Beginner

**Strategy**:
Object representing eventual completion of async operation.

**Code Example**:
```javascript
new Promise((res, rej) => { ... })
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q57: How does `async/await` work?

**Difficulty**: Intermediate

**Strategy**:
Syntactic sugar over Promises/Generators.

**Code Example**:
```javascript
async function() { await promise; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q58: What is Hoisting?

**Difficulty**: Intermediate

**Strategy**:
Declarations moved to top of scope. `var` initialized undefined, `let`/`const` uninitialized.

**Code Example**:
```javascript
console.log(a); var a = 1;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q59: Difference between `null` and `undefined`?

**Difficulty**: Beginner

**Strategy**:
`undefined`: variable declared but no value. `null`: intentional absence of value.

**Code Example**:
```javascript
typeof null // 'object'
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q60: What is Event Bubbling vs Capturing?

**Difficulty**: Intermediate

**Strategy**:
Bubbling: Target -> Root. Capturing: Root -> Target.

**Code Example**:
```javascript
elem.addEventListener('click', fn, { capture: true })
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q61: How do you implement a deep clone?

**Difficulty**: Intermediate

**Strategy**:
Use `structuredClone()` or recursion.

**Code Example**:
```javascript
const copy = structuredClone(original);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q62: What is a Generator function?

**Difficulty**: Advanced

**Strategy**:
Function that can be paused and resumed (`yield`).

**Code Example**:
```javascript
function* gen() { yield 1; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q63: What is the Proxy object?

**Difficulty**: Advanced

**Strategy**:
Intercepts operations on objects (get, set).

**Code Example**:
```javascript
new Proxy(target, { get: (obj, prop) => ... })
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q64: Difference between `==` and `===`?

**Difficulty**: Beginner

**Strategy**:
`===` checks type and value. `==` does type coercion.

**Code Example**:
```javascript
1 == '1' // true
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q65: What is `bind`, `call`, and `apply`?

**Difficulty**: Intermediate

**Strategy**:
Methods to set `this` context explicitly.

**Code Example**:
```javascript
fn.call(ctx, arg1); fn.apply(ctx, [args]); fn.bind(ctx);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q66: What is a WeakMap?

**Difficulty**: Advanced

**Strategy**:
Map with weak keys (objects only). Garbage collected if key is unreachable.

**Code Example**:
```javascript
const wm = new WeakMap();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q67: How do you handle errors in Promises?

**Difficulty**: Intermediate

**Strategy**:
Use `.catch()` or `try/catch` in async/await.

**Code Example**:
```javascript
p.then().catch(err => ...);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q68: What is Currying?

**Difficulty**: Intermediate

**Strategy**:
Transforming function `f(a,b)` into `f(a)(b)`.

**Code Example**:
```javascript
const add = a => b => a + b;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q69: What is the Temporal Dead Zone (TDZ)?

**Difficulty**: Advanced

**Strategy**:
Time between entering scope and `let`/`const` declaration.

**Code Example**:
```javascript
{ console.log(x); let x; } // ReferenceError
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q70: What is a Polyfill?

**Difficulty**: Beginner

**Strategy**:
Code to provide modern functionality on older browsers.

**Code Example**:
```javascript
if (!Array.prototype.map) { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q71: How do you debounce a function?

**Difficulty**: Intermediate

**Strategy**:
Delay execution until time elapses since last call.

**Code Example**:
```javascript
function debounce(fn, delay) { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q72: How do you throttle a function?

**Difficulty**: Intermediate

**Strategy**:
Limit execution to once per time interval.

**Code Example**:
```javascript
function throttle(fn, limit) { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q73: What is the `module` pattern?

**Difficulty**: Intermediate

**Strategy**:
Encapsulating private members using closures (IIFE).

**Code Example**:
```javascript
const mod = (() => { let p = 1; return { get: () => p }; })();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q74: What is `localStorage` vs `sessionStorage`?

**Difficulty**: Beginner

**Strategy**:
Local: persists. Session: clears on tab close.

**Code Example**:
```javascript
localStorage.setItem('key', 'val');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q75: How do you check array equality?

**Difficulty**: Intermediate

**Strategy**:
Loop or JSON.stringify (simple cases).

**Code Example**:
```javascript
JSON.stringify(a) === JSON.stringify(b)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q76: What is `Symbol`?

**Difficulty**: Intermediate

**Strategy**:
Unique primitive type. Used for object keys.

**Code Example**:
```javascript
const sym = Symbol('desc');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q77: What is `Reflect` API?

**Difficulty**: Advanced

**Strategy**:
Methods for interceptable JavaScript operations.

**Code Example**:
```javascript
Reflect.get(target, prop)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q78: How do you flatten an array?

**Difficulty**: Beginner

**Strategy**:
Use `flat()`.

**Code Example**:
```javascript
arr.flat(Infinity)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q79: What is strict mode?

**Difficulty**: Beginner

**Strategy**:
Enforces stricter parsing and error handling.

**Code Example**:
```javascript
'use strict';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q80: How do you implement a Set?

**Difficulty**: Beginner

**Strategy**:
Use `Set` object for unique values.

**Code Example**:
```javascript
new Set([1, 2, 2])
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q81: What is `Intl` API?

**Difficulty**: Intermediate

**Strategy**:
Internationalization helper.

**Code Example**:
```javascript
new Intl.NumberFormat().format(1000)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q82: How do you detect browser vs node?

**Difficulty**: Beginner

**Strategy**:
Check `typeof window` or `typeof process`.

**Code Example**:
```javascript
typeof window !== 'undefined'
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q83: What is an IIFE?

**Difficulty**: Beginner

**Strategy**:
Immediately Invoked Function Expression.

**Code Example**:
```javascript
(() => { ... })()
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q84: How do you remove duplicates from array?

**Difficulty**: Beginner

**Strategy**:
Use Set.

**Code Example**:
```javascript
[...new Set(arr)]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q85: What is Object.freeze?

**Difficulty**: Intermediate

**Strategy**:
Prevents modification of object.

**Code Example**:
```javascript
Object.freeze(obj)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q86: What is `requestAnimationFrame`?

**Difficulty**: Intermediate

**Strategy**:
Schedule function for next repaint.

**Code Example**:
```javascript
requestAnimationFrame(draw)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q87: How do you stop event propagation?

**Difficulty**: Beginner

**Strategy**:
`e.stopPropagation()`.

**Code Example**:
```javascript
elem.onclick = e => e.stopPropagation()
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q88: What is `Promise.all`?

**Difficulty**: Intermediate

**Strategy**:
Wait for all promises to resolve.

**Code Example**:
```javascript
Promise.all([p1, p2])
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q89: What is `Promise.race`?

**Difficulty**: Intermediate

**Strategy**:
Wait for first promise to settle.

**Code Example**:
```javascript
Promise.race([p1, p2])
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q90: What is `BigInt`?

**Difficulty**: Beginner

**Strategy**:
Arbitrary precision integers.

**Code Example**:
```javascript
const n = 123n;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q91: How do you merge objects?

**Difficulty**: Beginner

**Strategy**:
Spread operator or `Object.assign`.

**Code Example**:
```javascript
{ ...obj1, ...obj2 }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q92: What is Optional Chaining?

**Difficulty**: Beginner

**Strategy**:
Safe property access.

**Code Example**:
```javascript
obj?.prop
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q93: What is Nullish Coalescing?

**Difficulty**: Beginner

**Strategy**:
Default value for null/undefined.

**Code Example**:
```javascript
x ?? 'default'
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q94: How do you iterate object keys?

**Difficulty**: Beginner

**Strategy**:
`Object.keys`, `Object.values`, `for...in`.

**Code Example**:
```javascript
for (let k in obj) ...
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q95: What is `globalThis`?

**Difficulty**: Beginner

**Strategy**:
Universal global scope.

**Code Example**:
```javascript
console.log(globalThis)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q96: How do you parse URL parameters?

**Difficulty**: Beginner

**Strategy**:
Use `URLSearchParams`.

**Code Example**:
```javascript
new URLSearchParams(window.location.search)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q97: What is the difference between `slice` and `splice`?

**Difficulty**: Beginner

**Strategy**:
`slice` returns new array. `splice` modifies in-place.

**Code Example**:
```javascript
arr.slice(0, 1)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q98: How do you copy to clipboard?

**Difficulty**: Intermediate

**Strategy**:
Use Clipboard API.

**Code Example**:
```javascript
navigator.clipboard.writeText('text')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q99: What is a service worker?

**Difficulty**: Advanced

**Strategy**:
Script running in background (PWA).

**Code Example**:
```javascript
navigator.serviceWorker.register('sw.js')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q100: How do you check for NaN?

**Difficulty**: Beginner

**Strategy**:
`Number.isNaN()`.

**Code Example**:
```javascript
Number.isNaN(NaN)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---
