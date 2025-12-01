# JavaScript Interview Questions & Answers

## Table of Contents

1. [Explain Hoisting with examples?](#q1) <span class="beginner">Beginner</span>
2. [Difference between `var`, `let`, and `const`?](#q2) <span class="beginner">Beginner</span>
3. [Explain Closures with a practical example?](#q3) <span class="intermediate">Intermediate</span>
4. [How does the Event Loop work?](#q4) <span class="advanced">Advanced</span>
5. [Explain `this` keyword behavior?](#q5) <span class="intermediate">Intermediate</span>
6. [Call vs Apply vs Bind?](#q6) <span class="intermediate">Intermediate</span>
7. [What is Prototypal Inheritance?](#q7) <span class="advanced">Advanced</span>
8. [Explain Promise and its states?](#q8) <span class="intermediate">Intermediate</span>
9. [Async/Await vs Promises?](#q9) <span class="beginner">Beginner</span>
10. [What is Event Bubbling vs Capturing?](#q10) <span class="intermediate">Intermediate</span>
11. [How does Event Delegation work?](#q11) <span class="intermediate">Intermediate</span>
12. [Deep Copy vs Shallow Copy?](#q12) <span class="intermediate">Intermediate</span>
13. [What is the difference between `==` and `===`?](#q13) <span class="beginner">Beginner</span>
14. [Explain Higher-Order Functions?](#q14) <span class="beginner">Beginner</span>
15. [What is Currying?](#q15) <span class="intermediate">Intermediate</span>
16. [What is Memoization?](#q16) <span class="intermediate">Intermediate</span>
17. [Explain Debounce vs Throttle?](#q17) <span class="intermediate">Intermediate</span>
18. [What are Generators?](#q18) <span class="advanced">Advanced</span>
19. [Map vs WeakMap?](#q19) <span class="advanced">Advanced</span>
20. [Set vs WeakSet?](#q20) <span class="advanced">Advanced</span>
21. [What is a Proxy object?](#q21) <span class="advanced">Advanced</span>
22. [Explain the Module System (ESM vs CommonJS)?](#q22) <span class="intermediate">Intermediate</span>
23. [What is the Temporal Dead Zone (TDZ)?](#q23) <span class="intermediate">Intermediate</span>
24. [How does Garbage Collection work in JS?](#q24) <span class="advanced">Advanced</span>
25. [What is strict mode (`'use strict'`)?](#q25) <span class="beginner">Beginner</span>
26. [Difference between `null` and `undefined`?](#q26) <span class="beginner">Beginner</span>
27. [What is Type Coercion?](#q27) <span class="intermediate">Intermediate</span>
28. [Explain `instanceof` operator?](#q28) <span class="intermediate">Intermediate</span>
29. [What are Arrow Functions?](#q29) <span class="beginner">Beginner</span>
30. [What is Destructuring Assignment?](#q30) <span class="beginner">Beginner</span>
31. [Rest Operator vs Spread Operator?](#q31) <span class="beginner">Beginner</span>
32. [What is a Polyfill?](#q32) <span class="beginner">Beginner</span>
33. [What is a Transpiler (Babel)?](#q33) <span class="beginner">Beginner</span>
34. [Explain `Symbol` primitive?](#q34) <span class="advanced">Advanced</span>
35. [What is an Iterator?](#q35) <span class="advanced">Advanced</span>
36. [Explain `Object.freeze()` vs `Object.seal()`?](#q36) <span class="intermediate">Intermediate</span>
37. [How to check if an object is an array?](#q37) <span class="beginner">Beginner</span>
38. [What is `NaN` and how to check for it?](#q38) <span class="beginner">Beginner</span>
39. [Explain `preventDefault()` vs `stopPropagation()`?](#q39) <span class="beginner">Beginner</span>
40. [What is the BOM (Browser Object Model)?](#q40) <span class="beginner">Beginner</span>
41. [LocalStorage vs SessionStorage vs Cookies?](#q41) <span class="intermediate">Intermediate</span>
42. [What is JSONP?](#q42) <span class="advanced">Advanced</span>
43. [What is CORS?](#q43) <span class="intermediate">Intermediate</span>
44. [Explain the Critical Rendering Path?](#q44) <span class="advanced">Advanced</span>
45. [What are Web Workers?](#q45) <span class="advanced">Advanced</span>
46. [Service Workers vs Web Workers?](#q46) <span class="advanced">Advanced</span>
47. [What is the Shadow DOM?](#q47) <span class="advanced">Advanced</span>
48. [Custom Elements (Web Components)?](#q48) <span class="advanced">Advanced</span>
49. [Explain `requestAnimationFrame`?](#q49) <span class="intermediate">Intermediate</span>
50. [MutationObserver API?](#q50) <span class="advanced">Advanced</span>
51. [IntersectionObserver API?](#q51) <span class="intermediate">Intermediate</span>
52. [What is the Fetch API?](#q52) <span class="beginner">Beginner</span>
53. [How to abort a Fetch request?](#q53) <span class="intermediate">Intermediate</span>
54. [Explain `Promise.all` vs `Promise.race`?](#q54) <span class="intermediate">Intermediate</span>
55. [Explain `Promise.allSettled` vs `Promise.any`?](#q55) <span class="intermediate">Intermediate</span>
56. [What is a Microtask vs Macrotask?](#q56) <span class="advanced">Advanced</span>
57. [How to implement a Sleep function?](#q57) <span class="beginner">Beginner</span>
58. [Flatten an array without flat()?](#q58) <span class="intermediate">Intermediate</span>
59. [Remove duplicates from array?](#q59) <span class="beginner">Beginner</span>
60. [Check for Anagrams?](#q60) <span class="beginner">Beginner</span>
61. [Check for Palindrome?](#q61) <span class="beginner">Beginner</span>
62. [Implement `map` polyfill?](#q62) <span class="intermediate">Intermediate</span>
63. [Implement `filter` polyfill?](#q63) <span class="intermediate">Intermediate</span>
64. [Implement `reduce` polyfill?](#q64) <span class="advanced">Advanced</span>
65. [What is a Pure Function?](#q65) <span class="intermediate">Intermediate</span>
66. [What is Side Effect?](#q66) <span class="beginner">Beginner</span>
67. [Declarative vs Imperative Programming?](#q67) <span class="intermediate">Intermediate</span>
68. [What is Tail Call Optimization (TCO)?](#q68) <span class="advanced">Advanced</span>
69. [What is a Thunk?](#q69) <span class="advanced">Advanced</span>
70. [Explain Function Composition?](#q70) <span class="intermediate">Intermediate</span>
71. [What is `eval()` and why avoid it?](#q71) <span class="beginner">Beginner</span>
72. [What is `void 0`?](#q72) <span class="advanced">Advanced</span>
73. [Difference between property and attribute?](#q73) <span class="intermediate">Intermediate</span>
74. [Data attributes (`data-*`)?](#q74) <span class="beginner">Beginner</span>
75. [How to detect browser/device?](#q75) <span class="beginner">Beginner</span>
76. [What is `document.createDocumentFragment()`?](#q76) <span class="intermediate">Intermediate</span>
77. [Explain Reflow vs Repaint?](#q77) <span class="advanced">Advanced</span>
78. [What is the Virtual DOM (concept)?](#q78) <span class="intermediate">Intermediate</span>
79. [Server-Side Rendering (SSR) vs CSR?](#q79) <span class="intermediate">Intermediate</span>
80. [What is a Single Page Application (SPA)?](#q80) <span class="beginner">Beginner</span>
81. [What is Progressive Web App (PWA)?](#q81) <span class="intermediate">Intermediate</span>
82. [Explain WebSocket Protocol?](#q82) <span class="advanced">Advanced</span>
83. [Server-Sent Events (SSE)?](#q83) <span class="advanced">Advanced</span>
84. [What is `Intl` API?](#q84) <span class="intermediate">Intermediate</span>
85. [How to format dates (Date vs Intl)?](#q85) <span class="beginner">Beginner</span>
86. [What is Regex?](#q86) <span class="intermediate">Intermediate</span>
87. [Error Handling (try/catch/finally)?](#q87) <span class="beginner">Beginner</span>
88. [Custom Error Classes?](#q88) <span class="intermediate">Intermediate</span>
89. [What is a Memory Leak?](#q89) <span class="advanced">Advanced</span>
90. [How to debug Memory Leaks?](#q90) <span class="advanced">Advanced</span>
91. [What is `console.time()`?](#q91) <span class="beginner">Beginner</span>
92. [What is `debugger` statement?](#q92) <span class="beginner">Beginner</span>
93. [Strict Equality of Objects?](#q93) <span class="intermediate">Intermediate</span>
94. [Chaining Optional Chaining (`?.`)?](#q94) <span class="beginner">Beginner</span>
95. [Nullish Coalescing Operator (`??`)?](#q95) <span class="beginner">Beginner</span>
96. [Dynamic Imports (`import()`)?](#q96) <span class="intermediate">Intermediate</span>
97. [Top-level Await?](#q97) <span class="intermediate">Intermediate</span>
98. [BigInt Type?](#q98) <span class="beginner">Beginner</span>
99. [Private Class Fields (`#`)?](#q99) <span class="intermediate">Intermediate</span>
100. [What is the TC39 Process?](#q100) <span class="advanced">Advanced</span>

---

<div id="q1" class="question">1. Explain Hoisting with examples? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Hoisting is JS's default behavior of moving declarations to the top. <code>var</code> is hoisted and initialized with <code>undefined</code>. <code>let</code>/<code>const</code> are hoisted but stay in the TDZ.</p>
<pre><code class="language-javascript">console.log(a); // undefined
var a = 5;

console.log(b); // ReferenceError
let b = 10;</code></pre>
</div>

<div id="q2" class="question">2. Difference between `var`, `let`, and `const`? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <ul>
    <li><strong>var:</strong> Function scoped, hoisted, re-declarable.</li>
    <li><strong>let:</strong> Block scoped, not re-declarable in same scope.</li>
    <li><strong>const:</strong> Block scoped, must be initialized, cannot be reassigned (but objects are mutable).</li>
  </ul>
</div>

<div id="q3" class="question">3. Explain Closures with a practical example? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>A closure is a function that remembers its outer variables even after the outer function has returned.</p>
<pre><code class="language-javascript">function createCounter() {
  let count = 0;
  return function() {
    count++;
    return count;
  };
}
const counter = createCounter();
console.log(counter()); // 1
console.log(counter()); // 2</code></pre>
</div>

<div id="q4" class="question">4. How does the Event Loop work? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>JS is single-threaded. The Event Loop checks if Call Stack is empty. If yes, it pushes tasks from Microtask Queue (Promises) first, then Macrotask Queue (setTimeout, I/O) to Call Stack.</p>
</div>

<div id="q5" class="question">5. Explain `this` keyword behavior? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Value depends on invocation:</p>
  <ul>
    <li><strong>Global:</strong> <code>window</code> (or undefined in strict).</li>
    <li><strong>Method:</strong> Object calling it.</li>
    <li><strong>Function:</strong> Global (or undefined).</li>
    <li><strong>Arrow Function:</strong> Inherits from lexical scope (parent).</li>
  </ul>
</div>

<div id="q6" class="question">6. Call vs Apply vs Bind? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <ul>
    <li><code>call(thisArg, arg1, arg2)</code>: Invokes immediately.</li>
    <li><code>apply(thisArg, [args])</code>: Invokes immediately with array.</li>
    <li><code>bind(thisArg)</code>: Returns new function with bound <code>this</code>.</li>
  </ul>
</div>

<div id="q7" class="question">7. What is Prototypal Inheritance? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Objects inherit properties from other objects via `__proto__` chain.</p>
<pre><code class="language-javascript">const animal = { eats: true };
const rabbit = Object.create(animal);
console.log(rabbit.eats); // true</code></pre>
</div>

<div id="q8" class="question">8. Explain Promise and its states? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Object representing async completion. States: <strong>Pending, Fulfilled, Rejected</strong>.</p>
<pre><code class="language-javascript">const p = new Promise((resolve, reject) => {
  if (true) resolve('Success');
});</code></pre>
</div>

<div id="q9" class="question">9. Async/Await vs Promises? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Async/Await is syntactic sugar over Promises. Makes code look synchronous and easier to read.</p>
</div>

<div id="q10" class="question">10. What is Event Bubbling vs Capturing? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <ul>
    <li><strong>Bubbling (Default):</strong> Event starts at target and goes up to window.</li>
    <li><strong>Capturing:</strong> Event goes down from window to target.</li>
  </ul>
</div>

<div id="q11" class="question">11. How does Event Delegation work? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Attaching a single listener to a parent to handle events for all children (using Bubbling).</p>
<pre><code class="language-javascript">document.getElementById('list').addEventListener('click', (e) => {
  if (e.target.tagName === 'LI') console.log('Item clicked');
});</code></pre>
</div>

<div id="q12" class="question">12. Deep Copy vs Shallow Copy? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <ul>
    <li><strong>Shallow:</strong> Copies references (e.g., <code>{...obj}</code>). Nested changes affect original.</li>
    <li><strong>Deep:</strong> Copies values recursively (e.g., <code>JSON.parse(JSON.stringify(obj))</code> or <code>structuredClone()</code>).</li>
  </ul>
</div>

<div id="q13" class="question">13. What is the difference between `==` and `===`? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p><code>==</code> performs type coercion. <code>===</code> checks value and type (Strict Equality).</p>
</div>

<div id="q14" class="question">14. Explain Higher-Order Functions? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Functions that take other functions as args or return them (e.g., <code>map</code>, <code>filter</code>).</p>
</div>

<div id="q15" class="question">15. What is Currying? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Transforming <code>f(a,b,c)</code> into <code>f(a)(b)(c)</code>.</p>
<pre><code class="language-javascript">const add = a => b => a + b;
add(2)(3); // 5</code></pre>
</div>

<div id="q16" class="question">16. What is Memoization? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Caching results of expensive function calls based on inputs.</p>
</div>

<div id="q17" class="question">17. Explain Debounce vs Throttle? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <ul>
    <li><strong>Debounce:</strong> Wait for pause in events before running (e.g., Search input).</li>
    <li><strong>Throttle:</strong> Run at most once every X ms (e.g., Scroll).</li>
  </ul>
</div>

<div id="q18" class="question">18. What are Generators? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Functions that can pause (`yield`) and resume.</p>
<pre><code class="language-javascript">function* gen() {
  yield 1;
  yield 2;
}
const g = gen();
g.next().value; // 1</code></pre>
</div>

<div id="q19" class="question">19. Map vs WeakMap? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p><strong>WeakMap</strong> keys must be objects and are weakly referenced (garbage collected if no other ref exists). Not iterable.</p>
</div>

<div id="q20" class="question">20. Set vs WeakSet? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Similar to WeakMap, but for Sets. Stores objects weakly.</p>
</div>

<div id="q21" class="question">21. What is a Proxy object? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Wraps an object to intercept operations (get, set, etc.).</p>
<pre><code class="language-javascript">const handler = {
  get: (obj, prop) => prop in obj ? obj[prop] : 'Not Found'
};</code></pre>
</div>

<div id="q22" class="question">22. Explain the Module System (ESM vs CommonJS)? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <ul>
    <li><strong>CommonJS:</strong> <code>require</code> / <code>module.exports</code>. Sync. Node.js default.</li>
    <li><strong>ESM:</strong> <code>import</code> / <code>export</code>. Async. Browser/Modern Node.</li>
  </ul>
</div>

<div id="q23" class="question">23. What is the Temporal Dead Zone (TDZ)? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Time between entering scope and variable declaration where accessing <code>let</code>/<code>const</code> throws ReferenceError.</p>
</div>

<div id="q24" class="question">24. How does Garbage Collection work in JS? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Mark-and-Sweep algorithm. Roots are marked, reachable objects marked. Unmarked memory is freed.</p>
</div>

<div id="q25" class="question">25. What is strict mode (`'use strict'`)? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Enforces stricter parsing. Catches silent errors. Disables global <code>this</code>.</p>
</div>

<div id="q26" class="question">26. Difference between `null` and `undefined`? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p><code>undefined</code>: Variable declared but not assigned.<br><code>null</code>: Assignment value representing "no value".</p>
</div>

<div id="q27" class="question">27. What is Type Coercion? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Automatic conversion of values from one type to another (e.g., <code>"5" - 1 = 4</code>).</p>
</div>

<div id="q28" class="question">28. Explain `instanceof` operator? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Checks if prototype property of constructor appears in object's prototype chain.</p>
</div>

<div id="q29" class="question">29. What are Arrow Functions? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Concise syntax. No own <code>this</code>, <code>arguments</code>, or <code>super</code>.</p>
</div>

<div id="q30" class="question">30. What is Destructuring Assignment? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
<pre><code class="language-javascript">const { name, age } = user;
const [first, second] = array;</code></pre>
</div>

<div id="q31" class="question">31. Rest Operator vs Spread Operator? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Both use `...`. <strong>Spread</strong> expands (unpacks). <strong>Rest</strong> collects (packs).</p>
</div>

<div id="q32" class="question">32. What is a Polyfill? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Code that implements a feature on browsers that don't support it.</p>
</div>

<div id="q33" class="question">33. What is a Transpiler (Babel)? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Converts modern JS (ES6+) into older JS (ES5) for compatibility.</p>
</div>

<div id="q34" class="question">34. Explain `Symbol` primitive? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Unique, immutable primitive. Used for object property keys to avoid collision.</p>
</div>

<div id="q35" class="question">35. What is an Iterator? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Object implementing `next()` method returning `{value, done}`. Used in `for..of`.</p>
</div>

<div id="q36" class="question">36. Explain `Object.freeze()` vs `Object.seal()`? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <ul>
    <li><strong>Freeze:</strong> Immutable. Cannot add/remove/change properties.</li>
    <li><strong>Seal:</strong> Cannot add/remove properties, but CAN change existing values.</li>
  </ul>
</div>

<div id="q37" class="question">37. How to check if an object is an array? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-javascript">Array.isArray(obj)</code></pre>
</div>

<div id="q38" class="question">38. What is `NaN` and how to check for it? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Not-a-Number. Check with <code>Number.isNaN(val)</code>.</p>
</div>

<div id="q39" class="question">39. Explain `preventDefault()` vs `stopPropagation()`? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <ul>
    <li><code>preventDefault()</code>: Stops default browser action (e.g., form submit).</li>
    <li><code>stopPropagation()</code>: Stops bubbling.</li>
  </ul>
</div>

<div id="q40" class="question">40. What is the BOM (Browser Object Model)? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Objects provided by browser to interact with window (location, history, screen).</p>
</div>

<div id="q41" class="question">41. LocalStorage vs SessionStorage vs Cookies? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <ul>
    <li><strong>Local:</strong> Persistent, ~5MB.</li>
    <li><strong>Session:</strong> Tab life, ~5MB.</li>
    <li><strong>Cookie:</strong> Sent to server, ~4KB.</li>
  </ul>
</div>

<div id="q42" class="question">42. What is JSONP? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Old hack for cross-domain requests using `&lt;script&gt;` tags. Insecure.</p>
</div>

<div id="q43" class="question">43. What is CORS? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Cross-Origin Resource Sharing. Browser mechanism allowing access to resources from different origins.</p>
</div>

<div id="q44" class="question">44. Explain the Critical Rendering Path? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>HTML -> DOM -> CSSOM -> Render Tree -> Layout -> Paint.</p>
</div>

<div id="q45" class="question">45. What are Web Workers? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Run JS in background thread. No DOM access. Used for heavy computation.</p>
</div>

<div id="q46" class="question">46. Service Workers vs Web Workers? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Service Workers act as network proxy (caching, offline). Web Workers do computation.</p>
</div>

<div id="q47" class="question">47. What is the Shadow DOM? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Encapsulated DOM tree attached to an element. Styles don't leak in/out. (Used in `&lt;video&gt;`).</p>
</div>

<div id="q48" class="question">48. Custom Elements (Web Components)? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Defining new HTML tags (`&lt;my-element&gt;`) with custom behavior.</p>
</div>

<div id="q49" class="question">49. Explain `requestAnimationFrame`? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Schedules function for next repaint (approx 60fps). More efficient than `setInterval` for animations.</p>
</div>

<div id="q50" class="question">50. MutationObserver API? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Watches for changes in the DOM tree (childList, attributes).</p>
</div>

<div id="q51" class="question">51. IntersectionObserver API? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Detects visibility of element (e.g., infinite scroll, lazy loading).</p>
</div>

<div id="q52" class="question">52. What is the Fetch API? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Modern promise-based replacement for XHR.</p>
</div>

<div id="q53" class="question">53. How to abort a Fetch request? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Use <code>AbortController</code>.</p>
<pre><code class="language-javascript">const controller = new AbortController();
fetch(url, { signal: controller.signal });
controller.abort();</code></pre>
</div>

<div id="q54" class="question">54. Explain `Promise.all` vs `Promise.race`? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <ul>
    <li><code>all</code>: Waits for all to resolve or one to reject.</li>
    <li><code>race</code>: Waits for first to settle (resolve or reject).</li>
  </ul>
</div>

<div id="q55" class="question">55. Explain `Promise.allSettled` vs `Promise.any`? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <ul>
    <li><code>allSettled</code>: Waits for all to finish (status for each).</li>
    <li><code>any</code>: Waits for first to fulfill.</li>
  </ul>
</div>

<div id="q56" class="question">56. What is a Microtask vs Macrotask? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p><strong>Microtask:</strong> Promises, queueMicrotask (Higher priority).<br><strong>Macrotask:</strong> setTimeout, I/O.</p>
</div>

<div id="q57" class="question">57. How to implement a Sleep function? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-javascript">const sleep = ms => new Promise(r => setTimeout(r, ms));</code></pre>
</div>

<div id="q58" class="question">58. Flatten an array without flat()? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-javascript">const flat = arr => arr.reduce((acc, val) => 
    Array.isArray(val) ? acc.concat(flat(val)) : acc.concat(val), []);</code></pre>
</div>

<div id="q59" class="question">59. Remove duplicates from array? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-javascript">[...new Set(arr)]</code></pre>
</div>

<div id="q60" class="question">60. Check for Anagrams? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-javascript">s1.split('').sort().join('') === s2.split('').sort().join('')</code></pre>
</div>

<div id="q61" class="question">61. Check for Palindrome? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-javascript">str === str.split('').reverse().join('')</code></pre>
</div>

<div id="q62" class="question">62. Implement `map` polyfill? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">Array.prototype.myMap = function(cb) {
  const res = [];
  for (let i = 0; i < this.length; i++) res.push(cb(this[i], i, this));
  return res;
};</code></pre>
</div>

<div id="q63" class="question">63. Implement `filter` polyfill? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
<pre><code class="language-javascript">Array.prototype.myFilter = function(cb) {
  const res = [];
  for (let i = 0; i < this.length; i++) if (cb(this[i])) res.push(this[i]);
  return res;
};</code></pre>
</div>

<div id="q64" class="question">64. Implement `reduce` polyfill? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
<pre><code class="language-javascript">Array.prototype.myReduce = function(cb, init) {
  let acc = init ?? this[0];
  let start = init === undefined ? 1 : 0;
  for (let i = start; i < this.length; i++) acc = cb(acc, this[i]);
  return acc;
};</code></pre>
</div>

<div id="q65" class="question">65. What is a Pure Function? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Function that always returns same output for same input and has no side effects.</p>
</div>

<div id="q66" class="question">66. What is Side Effect? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Modifying external state (DOM, global vars) or API calls.</p>
</div>

<div id="q67" class="question">67. Declarative vs Imperative Programming? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p><strong>Declarative:</strong> What to do (React, SQL).<br><strong>Imperative:</strong> How to do it (Loops, DOM manipulation).</p>
</div>

<div id="q68" class="question">68. What is Tail Call Optimization (TCO)? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Engine optimization where recursion doesn't grow stack if call is in tail position.</p>
</div>

<div id="q69" class="question">69. What is a Thunk? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Function that wraps an expression to delay its evaluation.</p>
</div>

<div id="q70" class="question">70. Explain Function Composition? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Combining functions: <code>f(g(x))</code>.</p>
</div>

<div id="q71" class="question">71. What is `eval()` and why avoid it? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Executes string as code. Security risk (XSS) and performance hit.</p>
</div>

<div id="q72" class="question">72. What is `void 0`? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Reliable way to get true `undefined` (since undefined variable can be overwritten in non-strict).</p>
</div>

<div id="q73" class="question">73. Difference between property and attribute? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p><strong>Attribute:</strong> HTML initial value.<br><strong>Property:</strong> DOM current value (e.g., input value).</p>
</div>

<div id="q74" class="question">74. Data attributes (`data-*`)? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Store custom data on HTML elements. Access via <code>dataset</code>.</p>
</div>

<div id="q75" class="question">75. How to detect browser/device? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p><code>navigator.userAgent</code> (though unreliable).</p>
</div>

<div id="q76" class="question">76. What is `document.createDocumentFragment()`? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Lightweight container. Appending to it doesn't trigger reflow. Appending fragment to DOM triggers one reflow.</p>
</div>

<div id="q77" class="question">77. Explain Reflow vs Repaint? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p><strong>Reflow:</strong> Layout calculation (Expensive).<br><strong>Repaint:</strong> Pixel update (Color change).</p>
</div>

<div id="q78" class="question">78. What is the Virtual DOM (concept)? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>In-memory representation of DOM. Diffs changes and updates real DOM efficiently.</p>
</div>

<div id="q79" class="question">79. Server-Side Rendering (SSR) vs CSR? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p><strong>SSR:</strong> Server sends HTML. Better SEO/First Paint.<br><strong>CSR:</strong> Browser builds HTML. Better interactivity.</p>
</div>

<div id="q80" class="question">80. What is a Single Page Application (SPA)? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Web app that loads one HTML page and dynamically updates content.</p>
</div>

<div id="q81" class="question">81. What is Progressive Web App (PWA)? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Web app behaving like native app (Offline, Installable, Push Notifications).</p>
</div>

<div id="q82" class="question">82. Explain WebSocket Protocol? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Full-duplex communication over single TCP connection.</p>
</div>

<div id="q83" class="question">83. Server-Sent Events (SSE)? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>One-way stream from Server to Client over HTTP.</p>
</div>

<div id="q84" class="question">84. What is `Intl` API? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Internationalization API for formatting numbers, dates, currencies.</p>
</div>

<div id="q85" class="question">85. How to format dates (Date vs Intl)? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-javascript">new Intl.DateTimeFormat('en-US').format(date)</code></pre>
</div>

<div id="q86" class="question">86. What is Regex? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Pattern matching for strings. <code>/pattern/.test(str)</code>.</p>
</div>

<div id="q87" class="question">87. Error Handling (try/catch/finally)? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Catch runtime errors. Finally runs always.</p>
</div>

<div id="q88" class="question">88. Custom Error Classes? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-javascript">class MyError extends Error { ... }</code></pre>
</div>

<div id="q89" class="question">89. What is a Memory Leak? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Memory allocated but not freed (e.g., Global vars, Detached DOM, Closures).</p>
</div>

<div id="q90" class="question">90. How to debug Memory Leaks? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Chrome DevTools > Memory > Heap Snapshot. Look for detached elements.</p>
</div>

<div id="q91" class="question">91. What is `console.time()`? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Measures time execution between <code>time()</code> and <code>timeEnd()</code>.</p>
</div>

<div id="q92" class="question">92. What is `debugger` statement? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Pauses execution if DevTools is open.</p>
</div>

<div id="q93" class="question">93. Strict Equality of Objects? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Compares references. Two identical objects are NOT equal.</p>
</div>

<div id="q94" class="question">94. Chaining Optional Chaining (`?.`)? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Safely access nested properties: <code>obj?.prop</code>.</p>
</div>

<div id="q95" class="question">95. Nullish Coalescing Operator (`??`)? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Returns right side if left is `null` or `undefined`. (Unlike `||` which handles all falsy).</p>
</div>

<div id="q96" class="question">96. Dynamic Imports (`import()`)? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Load modules on demand (Promise based). Good for Code Splitting.</p>
</div>

<div id="q97" class="question">97. Top-level Await? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Using <code>await</code> outside async function in modules.</p>
</div>

<div id="q98" class="question">98. BigInt Type? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Integer with arbitrary precision. <code>10n</code>.</p>
</div>

<div id="q99" class="question">99. Private Class Fields (`#`)? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-javascript">class A { #x = 1; }</code></pre>
</div>

<div id="q100" class="question">100. What is the TC39 Process? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Stages (0-4) for adding new features to ECMAScript standard.</p>
</div>
