<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>Javascript Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for developers</b></p>
</div>

---

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

---

<a id="q1"></a>
### Q1: Explain Hoisting with examples?

**Difficulty**: Beginner

**Strategy**:
Hoisting is JS's default behavior of moving declarations to the top. <code>var</code> is hoisted and initialized with <code>undefined</code>. <code>let</code>/<code>const</code> are hoisted but stay in the TDZ.

**Code Example**:
```javascript
console.log(a); // undefined
var a = 5;

console.log(b); // ReferenceError
let b = 10;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q2"></a>
### Q2: Difference between `var`, `let`, and `const`?

**Difficulty**: Beginner

**Strategy**:
- **var:** Function scoped, hoisted, re-declarable.

    - **let:** Block scoped, not re-declarable in same scope.

    - **const:** Block scoped, must be initialized, cannot be reassigned (but objects are mutable).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q3"></a>
### Q3: Explain Closures with a practical example?

**Difficulty**: Intermediate

**Strategy**:
A closure is a function that remembers its outer variables even after the outer function has returned.

**Code Example**:
```javascript
function createCounter() {
  let count = 0;
  return function() {
    count++;
    return count;
  };
}
const counter = createCounter();
console.log(counter()); // 1
console.log(counter()); // 2
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q4"></a>
### Q4: How does the Event Loop work?

**Difficulty**: Advanced

**Strategy**:
JS is single-threaded. The Event Loop checks if Call Stack is empty. If yes, it pushes tasks from Microtask Queue (Promises) first, then Macrotask Queue (setTimeout, I/O) to Call Stack.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q5"></a>
### Q5: Explain `this` keyword behavior?

**Difficulty**: Intermediate

**Strategy**:
Value depends on invocation:


  
    - **Global:** <code>window</code> (or undefined in strict).

    - **Method:** Object calling it.

    - **Function:** Global (or undefined).

    - **Arrow Function:** Inherits from lexical scope (parent).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q6"></a>
### Q6: Call vs Apply vs Bind?

**Difficulty**: Intermediate

**Strategy**:
- <code>call(thisArg, arg1, arg2)</code>: Invokes immediately.

    - <code>apply(thisArg, [args])</code>: Invokes immediately with array.

    - <code>bind(thisArg)</code>: Returns new function with bound <code>this</code>.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q7"></a>
### Q7: What is Prototypal Inheritance?

**Difficulty**: Advanced

**Strategy**:
Objects inherit properties from other objects via `__proto__` chain.

**Code Example**:
```javascript
const animal = { eats: true };
const rabbit = Object.create(animal);
console.log(rabbit.eats); // true
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q8"></a>
### Q8: Explain Promise and its states?

**Difficulty**: Intermediate

**Strategy**:
Object representing async completion. States: **Pending, Fulfilled, Rejected**.

**Code Example**:
```javascript
const p = new Promise((resolve, reject) => {
  if (true) resolve('Success');
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q9"></a>
### Q9: Async/Await vs Promises?

**Difficulty**: Beginner

**Strategy**:
Async/Await is syntactic sugar over Promises. Makes code look synchronous and easier to read.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q10"></a>
### Q10: What is Event Bubbling vs Capturing?

**Difficulty**: Intermediate

**Strategy**:
- **Bubbling (Default):** Event starts at target and goes up to window.

    - **Capturing:** Event goes down from window to target.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q11"></a>
### Q11: How does Event Delegation work?

**Difficulty**: Intermediate

**Strategy**:
Attaching a single listener to a parent to handle events for all children (using Bubbling).

**Code Example**:
```javascript
document.getElementById('list').addEventListener('click', (e) => {
  if (e.target.tagName === 'LI') console.log('Item clicked');
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q12"></a>
### Q12: Deep Copy vs Shallow Copy?

**Difficulty**: Intermediate

**Strategy**:
- **Shallow:** Copies references (e.g., <code>{...obj}</code>). Nested changes affect original.

    - **Deep:** Copies values recursively (e.g., <code>JSON.parse(JSON.stringify(obj))</code> or <code>structuredClone()</code>).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q13"></a>
### Q13: What is the difference between `==` and `===`?

**Difficulty**: Beginner

**Strategy**:
<code>==</code> performs type coercion. <code>===</code> checks value and type (Strict Equality).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q14"></a>
### Q14: Explain Higher-Order Functions?

**Difficulty**: Beginner

**Strategy**:
Functions that take other functions as args or return them (e.g., <code>map</code>, <code>filter</code>).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q15"></a>
### Q15: What is Currying?

**Difficulty**: Intermediate

**Strategy**:
Transforming <code>f(a,b,c)</code> into <code>f(a)(b)(c)</code>.

**Code Example**:
```javascript
const add = a => b => a + b;
add(2)(3); // 5
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q16"></a>
### Q16: What is Memoization?

**Difficulty**: Intermediate

**Strategy**:
Caching results of expensive function calls based on inputs.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q17"></a>
### Q17: Explain Debounce vs Throttle?

**Difficulty**: Intermediate

**Strategy**:
- **Debounce:** Wait for pause in events before running (e.g., Search input).

    - **Throttle:** Run at most once every X ms (e.g., Scroll).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q18"></a>
### Q18: What are Generators?

**Difficulty**: Advanced

**Strategy**:
Functions that can pause (`yield`) and resume.

**Code Example**:
```javascript
function* gen() {
  yield 1;
  yield 2;
}
const g = gen();
g.next().value; // 1
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q19"></a>
### Q19: Map vs WeakMap?

**Difficulty**: Advanced

**Strategy**:
**WeakMap** keys must be objects and are weakly referenced (garbage collected if no other ref exists). Not iterable.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q20"></a>
### Q20: Set vs WeakSet?

**Difficulty**: Advanced

**Strategy**:
Similar to WeakMap, but for Sets. Stores objects weakly.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q21"></a>
### Q21: What is a Proxy object?

**Difficulty**: Advanced

**Strategy**:
Wraps an object to intercept operations (get, set, etc.).

**Code Example**:
```javascript
const handler = {
  get: (obj, prop) => prop in obj ? obj[prop] : 'Not Found'
};
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q22"></a>
### Q22: Explain the Module System (ESM vs CommonJS)?

**Difficulty**: Intermediate

**Strategy**:
- **CommonJS:** <code>require</code> / <code>module.exports</code>. Sync. Node.js default.

    - **ESM:** <code>import</code> / <code>export</code>. Async. Browser/Modern Node.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q23"></a>
### Q23: What is the Temporal Dead Zone (TDZ)?

**Difficulty**: Intermediate

**Strategy**:
Time between entering scope and variable declaration where accessing <code>let</code>/<code>const</code> throws ReferenceError.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q24"></a>
### Q24: How does Garbage Collection work in JS?

**Difficulty**: Advanced

**Strategy**:
Mark-and-Sweep algorithm. Roots are marked, reachable objects marked. Unmarked memory is freed.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q25"></a>
### Q25: What is strict mode (`'use strict'`)?

**Difficulty**: Beginner

**Strategy**:
Enforces stricter parsing. Catches silent errors. Disables global <code>this</code>.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q26"></a>
### Q26: Difference between `null` and `undefined`?

**Difficulty**: Beginner

**Strategy**:
<code>undefined</code>: Variable declared but not assigned.
<code>null</code>: Assignment value representing "no value".

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q27"></a>
### Q27: What is Type Coercion?

**Difficulty**: Intermediate

**Strategy**:
Automatic conversion of values from one type to another (e.g., <code>"5" - 1 = 4</code>).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q28"></a>
### Q28: Explain `instanceof` operator?

**Difficulty**: Intermediate

**Strategy**:
Checks if prototype property of constructor appears in object's prototype chain.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q29"></a>
### Q29: What are Arrow Functions?

**Difficulty**: Beginner

**Strategy**:
Concise syntax. No own <code>this</code>, <code>arguments</code>, or <code>super</code>.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q30"></a>
### Q30: What is Destructuring Assignment?

**Difficulty**: Beginner

**Strategy**:


**Code Example**:
```javascript
const { name, age } = user;
const [first, second] = array;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q31"></a>
### Q31: Rest Operator vs Spread Operator?

**Difficulty**: Beginner

**Strategy**:
Both use `...`. **Spread** expands (unpacks). **Rest** collects (packs).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q32"></a>
### Q32: What is a Polyfill?

**Difficulty**: Beginner

**Strategy**:
Code that implements a feature on browsers that don't support it.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q33"></a>
### Q33: What is a Transpiler (Babel)?

**Difficulty**: Beginner

**Strategy**:
Converts modern JS (ES6+) into older JS (ES5) for compatibility.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q34"></a>
### Q34: Explain `Symbol` primitive?

**Difficulty**: Advanced

**Strategy**:
Unique, immutable primitive. Used for object property keys to avoid collision.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q35"></a>
### Q35: What is an Iterator?

**Difficulty**: Advanced

**Strategy**:
Object implementing `next()` method returning `{value, done}`. Used in `for..of`.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q36"></a>
### Q36: Explain `Object.freeze()` vs `Object.seal()`?

**Difficulty**: Intermediate

**Strategy**:
- **Freeze:** Immutable. Cannot add/remove/change properties.

    - **Seal:** Cannot add/remove properties, but CAN change existing values.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q37"></a>
### Q37: How to check if an object is an array?

**Difficulty**: Beginner

**Strategy**:


**Code Example**:
```javascript
Array.isArray(obj)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q38"></a>
### Q38: What is `NaN` and how to check for it?

**Difficulty**: Beginner

**Strategy**:
Not-a-Number. Check with <code>Number.isNaN(val)</code>.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q39"></a>
### Q39: Explain `preventDefault()` vs `stopPropagation()`?

**Difficulty**: Beginner

**Strategy**:
- <code>preventDefault()</code>: Stops default browser action (e.g., form submit).

    - <code>stopPropagation()</code>: Stops bubbling.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q40"></a>
### Q40: What is the BOM (Browser Object Model)?

**Difficulty**: Beginner

**Strategy**:
Objects provided by browser to interact with window (location, history, screen).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q41"></a>
### Q41: LocalStorage vs SessionStorage vs Cookies?

**Difficulty**: Intermediate

**Strategy**:
- **Local:** Persistent, ~5MB.

    - **Session:** Tab life, ~5MB.

    - **Cookie:** Sent to server, ~4KB.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q42"></a>
### Q42: What is JSONP?

**Difficulty**: Advanced

**Strategy**:
Old hack for cross-domain requests using `&lt;script&gt;` tags. Insecure.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q43"></a>
### Q43: What is CORS?

**Difficulty**: Intermediate

**Strategy**:
Cross-Origin Resource Sharing. Browser mechanism allowing access to resources from different origins.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q44"></a>
### Q44: Explain the Critical Rendering Path?

**Difficulty**: Advanced

**Strategy**:
HTML -> DOM -> CSSOM -> Render Tree -> Layout -> Paint.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q45"></a>
### Q45: What are Web Workers?

**Difficulty**: Advanced

**Strategy**:
Run JS in background thread. No DOM access. Used for heavy computation.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q46"></a>
### Q46: Service Workers vs Web Workers?

**Difficulty**: Advanced

**Strategy**:
Service Workers act as network proxy (caching, offline). Web Workers do computation.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q47"></a>
### Q47: What is the Shadow DOM?

**Difficulty**: Advanced

**Strategy**:
Encapsulated DOM tree attached to an element. Styles don't leak in/out. (Used in `&lt;video&gt;`).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q48"></a>
### Q48: Custom Elements (Web Components)?

**Difficulty**: Advanced

**Strategy**:
Defining new HTML tags (`&lt;my-element&gt;`) with custom behavior.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q49"></a>
### Q49: Explain `requestAnimationFrame`?

**Difficulty**: Intermediate

**Strategy**:
Schedules function for next repaint (approx 60fps). More efficient than `setInterval` for animations.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q50"></a>
### Q50: MutationObserver API?

**Difficulty**: Advanced

**Strategy**:
Watches for changes in the DOM tree (childList, attributes).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q51"></a>
### Q51: IntersectionObserver API?

**Difficulty**: Intermediate

**Strategy**:
Detects visibility of element (e.g., infinite scroll, lazy loading).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q52"></a>
### Q52: What is the Fetch API?

**Difficulty**: Beginner

**Strategy**:
Modern promise-based replacement for XHR.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q53"></a>
### Q53: How to abort a Fetch request?

**Difficulty**: Intermediate

**Strategy**:
Use <code>AbortController</code>.

**Code Example**:
```javascript
const controller = new AbortController();
fetch(url, { signal: controller.signal });
controller.abort();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q54"></a>
### Q54: Explain `Promise.all` vs `Promise.race`?

**Difficulty**: Intermediate

**Strategy**:
- <code>all</code>: Waits for all to resolve or one to reject.

    - <code>race</code>: Waits for first to settle (resolve or reject).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q55"></a>
### Q55: Explain `Promise.allSettled` vs `Promise.any`?

**Difficulty**: Intermediate

**Strategy**:
- <code>allSettled</code>: Waits for all to finish (status for each).

    - <code>any</code>: Waits for first to fulfill.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q56"></a>
### Q56: What is a Microtask vs Macrotask?

**Difficulty**: Advanced

**Strategy**:
**Microtask:** Promises, queueMicrotask (Higher priority).
**Macrotask:** setTimeout, I/O.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q57"></a>
### Q57: How to implement a Sleep function?

**Difficulty**: Beginner

**Strategy**:


**Code Example**:
```javascript
const sleep = ms => new Promise(r => setTimeout(r, ms));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q58"></a>
### Q58: Flatten an array without flat()?

**Difficulty**: Intermediate

**Strategy**:


**Code Example**:
```javascript
const flat = arr => arr.reduce((acc, val) => 
    Array.isArray(val) ? acc.concat(flat(val)) : acc.concat(val), []);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q59"></a>
### Q59: Remove duplicates from array?

**Difficulty**: Beginner

**Strategy**:


**Code Example**:
```javascript
[...new Set(arr)]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q60"></a>
### Q60: Check for Anagrams?

**Difficulty**: Beginner

**Strategy**:


**Code Example**:
```javascript
s1.split('').sort().join('') === s2.split('').sort().join('')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q61"></a>
### Q61: Check for Palindrome?

**Difficulty**: Beginner

**Strategy**:


**Code Example**:
```javascript
str === str.split('').reverse().join('')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q62"></a>
### Q62: Implement `map` polyfill?

**Difficulty**: Intermediate

**Strategy**:


**Code Example**:
```javascript
Array.prototype.myMap = function(cb) {
  const res = [];
  for (let i = 0; i < this.length; i++) res.push(cb(this[i], i, this));
  return res;
};
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q63"></a>
### Q63: Implement `filter` polyfill?

**Difficulty**: Intermediate

**Strategy**:


**Code Example**:
```javascript
Array.prototype.myFilter = function(cb) {
  const res = [];
  for (let i = 0; i < this.length; i++) if (cb(this[i])) res.push(this[i]);
  return res;
};
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q64"></a>
### Q64: Implement `reduce` polyfill?

**Difficulty**: Advanced

**Strategy**:


**Code Example**:
```javascript
Array.prototype.myReduce = function(cb, init) {
  let acc = init ?? this[0];
  let start = init === undefined ? 1 : 0;
  for (let i = start; i < this.length; i++) acc = cb(acc, this[i]);
  return acc;
};
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q65"></a>
### Q65: What is a Pure Function?

**Difficulty**: Intermediate

**Strategy**:
Function that always returns same output for same input and has no side effects.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q66"></a>
### Q66: What is Side Effect?

**Difficulty**: Beginner

**Strategy**:
Modifying external state (DOM, global vars) or API calls.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q67"></a>
### Q67: Declarative vs Imperative Programming?

**Difficulty**: Intermediate

**Strategy**:
**Declarative:** What to do (React, SQL).
**Imperative:** How to do it (Loops, DOM manipulation).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q68"></a>
### Q68: What is Tail Call Optimization (TCO)?

**Difficulty**: Advanced

**Strategy**:
Engine optimization where recursion doesn't grow stack if call is in tail position.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q69"></a>
### Q69: What is a Thunk?

**Difficulty**: Advanced

**Strategy**:
Function that wraps an expression to delay its evaluation.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q70"></a>
### Q70: Explain Function Composition?

**Difficulty**: Intermediate

**Strategy**:
Combining functions: <code>f(g(x))</code>.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q71"></a>
### Q71: What is `eval()` and why avoid it?

**Difficulty**: Beginner

**Strategy**:
Executes string as code. Security risk (XSS) and performance hit.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q72"></a>
### Q72: What is `void 0`?

**Difficulty**: Advanced

**Strategy**:
Reliable way to get true `undefined` (since undefined variable can be overwritten in non-strict).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q73"></a>
### Q73: Difference between property and attribute?

**Difficulty**: Intermediate

**Strategy**:
**Attribute:** HTML initial value.
**Property:** DOM current value (e.g., input value).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q74"></a>
### Q74: Data attributes (`data-*`)?

**Difficulty**: Beginner

**Strategy**:
Store custom data on HTML elements. Access via <code>dataset</code>.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q75"></a>
### Q75: How to detect browser/device?

**Difficulty**: Beginner

**Strategy**:
<code>navigator.userAgent</code> (though unreliable).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q76"></a>
### Q76: What is `document.createDocumentFragment()`?

**Difficulty**: Intermediate

**Strategy**:
Lightweight container. Appending to it doesn't trigger reflow. Appending fragment to DOM triggers one reflow.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q77"></a>
### Q77: Explain Reflow vs Repaint?

**Difficulty**: Advanced

**Strategy**:
**Reflow:** Layout calculation (Expensive).
**Repaint:** Pixel update (Color change).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q78"></a>
### Q78: What is the Virtual DOM (concept)?

**Difficulty**: Intermediate

**Strategy**:
In-memory representation of DOM. Diffs changes and updates real DOM efficiently.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q79"></a>
### Q79: Server-Side Rendering (SSR) vs CSR?

**Difficulty**: Intermediate

**Strategy**:
**SSR:** Server sends HTML. Better SEO/First Paint.
**CSR:** Browser builds HTML. Better interactivity.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q80"></a>
### Q80: What is a Single Page Application (SPA)?

**Difficulty**: Beginner

**Strategy**:
Web app that loads one HTML page and dynamically updates content.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q81"></a>
### Q81: What is Progressive Web App (PWA)?

**Difficulty**: Intermediate

**Strategy**:
Web app behaving like native app (Offline, Installable, Push Notifications).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q82"></a>
### Q82: Explain WebSocket Protocol?

**Difficulty**: Advanced

**Strategy**:
Full-duplex communication over single TCP connection.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q83"></a>
### Q83: Server-Sent Events (SSE)?

**Difficulty**: Advanced

**Strategy**:
One-way stream from Server to Client over HTTP.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q84"></a>
### Q84: What is `Intl` API?

**Difficulty**: Intermediate

**Strategy**:
Internationalization API for formatting numbers, dates, currencies.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q85"></a>
### Q85: How to format dates (Date vs Intl)?

**Difficulty**: Beginner

**Strategy**:


**Code Example**:
```javascript
new Intl.DateTimeFormat('en-US').format(date)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q86"></a>
### Q86: What is Regex?

**Difficulty**: Intermediate

**Strategy**:
Pattern matching for strings. <code>/pattern/.test(str)</code>.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q87"></a>
### Q87: Error Handling (try/catch/finally)?

**Difficulty**: Beginner

**Strategy**:
Catch runtime errors. Finally runs always.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q88"></a>
### Q88: Custom Error Classes?

**Difficulty**: Intermediate

**Strategy**:


**Code Example**:
```javascript
class MyError extends Error { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q89"></a>
### Q89: What is a Memory Leak?

**Difficulty**: Advanced

**Strategy**:
Memory allocated but not freed (e.g., Global vars, Detached DOM, Closures).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q90"></a>
### Q90: How to debug Memory Leaks?

**Difficulty**: Advanced

**Strategy**:
Chrome DevTools > Memory > Heap Snapshot. Look for detached elements.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q91"></a>
### Q91: What is `console.time()`?

**Difficulty**: Beginner

**Strategy**:
Measures time execution between <code>time()</code> and <code>timeEnd()</code>.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q92"></a>
### Q92: What is `debugger` statement?

**Difficulty**: Beginner

**Strategy**:
Pauses execution if DevTools is open.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q93"></a>
### Q93: Strict Equality of Objects?

**Difficulty**: Intermediate

**Strategy**:
Compares references. Two identical objects are NOT equal.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q94"></a>
### Q94: Chaining Optional Chaining (`?.`)?

**Difficulty**: Beginner

**Strategy**:
Safely access nested properties: <code>obj?.prop</code>.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q95"></a>
### Q95: Nullish Coalescing Operator (`??`)?

**Difficulty**: Beginner

**Strategy**:
Returns right side if left is `null` or `undefined`. (Unlike `||` which handles all falsy).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q96"></a>
### Q96: Dynamic Imports (`import()`)?

**Difficulty**: Intermediate

**Strategy**:
Load modules on demand (Promise based). Good for Code Splitting.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q97"></a>
### Q97: Top-level Await?

**Difficulty**: Intermediate

**Strategy**:
Using <code>await</code> outside async function in modules.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q98"></a>
### Q98: BigInt Type?

**Difficulty**: Beginner

**Strategy**:
Integer with arbitrary precision. <code>10n</code>.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q99"></a>
### Q99: Private Class Fields (`#`)?

**Difficulty**: Intermediate

**Strategy**:


**Code Example**:
```javascript
class A { #x = 1; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q100"></a>
### Q100: What is the TC39 Process?

**Difficulty**: Advanced

**Strategy**:
Stages (0-4) for adding new features to ECMAScript standard.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---
