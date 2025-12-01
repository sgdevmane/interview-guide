<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/javascript-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>JavaScript Interview Questions & Answers</h1>
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
17. [What is a Generator Function?](#q17) <span class="advanced">Advanced</span>
18. [What is the Temporal Dead Zone (TDZ)?](#q18) <span class="intermediate">Intermediate</span>
19. [Map vs WeakMap?](#q19) <span class="advanced">Advanced</span>
20. [What is Destructuring Assignment?](#q20) <span class="beginner">Beginner</span>
21. [Explain the Spread and Rest Operator?](#q21) <span class="beginner">Beginner</span>
22. [What is Functional Programming in JS?](#q22) <span class="advanced">Advanced</span>
23. [What are Pure Functions?](#q23) <span class="intermediate">Intermediate</span>
24. [What is Type Coercion?](#q24) <span class="beginner">Beginner</span>
25. [What is a Proxy Object?](#q25) <span class="advanced">Advanced</span>
26. [What is the difference between `null` and `undefined`?](#q26) <span class="beginner">Beginner</span>
27. [How does `Array.prototype.reduce()` work?](#q27) <span class="intermediate">Intermediate</span>
28. [What are ES6 Modules (Import/Export)?](#q28) <span class="beginner">Beginner</span>
29. [What is the difference between `Object.freeze()` and `Object.seal()`?](#q29) <span class="intermediate">Intermediate</span>
30. [What is an IIFE (Immediately Invoked Function Expression)?](#q30) <span class="intermediate">Intermediate</span>
31. [What is the difference between `map()` and `forEach()`?](#q31) <span class="beginner">Beginner</span>
32. [What is `Strict Mode` in JavaScript?](#q32) <span class="beginner">Beginner</span>
33. [How does `NaN` behave and how to check for it?](#q33) <span class="beginner">Beginner</span>
34. [What are `Set` and `WeakSet`?](#q34) <span class="intermediate">Intermediate</span>
35. [What is the `Symbol` data type?](#q35) <span class="advanced">Advanced</span>
36. [How does `requestAnimationFrame` work?](#q36) <span class="intermediate">Intermediate</span>
37. [What is the difference between `localStorage`, `sessionStorage`, and Cookies?](#q37) <span class="intermediate">Intermediate</span>
38. [How does the `fetch` API work?](#q38) <span class="beginner">Beginner</span>
39. [What is the difference between `async` and `defer` attributes in script tags?](#q39) <span class="intermediate">Intermediate</span>
40. [What is the History API?](#q40) <span class="intermediate">Intermediate</span>
41. [What is `innerHTML` vs `textContent`?](#q41) <span class="beginner">Beginner</span>
42. [How do you handle errors with `try...catch...finally`?](#q42) <span class="beginner">Beginner</span>
43. [What is `JSON.parse` and `JSON.stringify`?](#q43) <span class="beginner">Beginner</span>
44. [What is the difference between `typeof` and `instanceof`?](#q44) <span class="beginner">Beginner</span>
45. [What are Template Literals?](#q45) <span class="beginner">Beginner</span>
46. [What is `Object.entries()`?](#q46) <span class="beginner">Beginner</span>
47. [What is the purpose of `Array.from()`?](#q47) <span class="intermediate">Intermediate</span>
48. [How do you detect if a property exists in an object?](#q48) <span class="beginner">Beginner</span>
49. [What is the `arguments` object?](#q49) <span class="beginner">Beginner</span>
50. [What is the difference between `slice()` and `splice()`?](#q50) <span class="beginner">Beginner</span>
51. [What are Service Workers?](#q51) <span class="advanced">Advanced</span>
52. [What is a Web Worker?](#q52) <span class="intermediate">Intermediate</span>
53. [What is the `Intl` API?](#q53) <span class="intermediate">Intermediate</span>
54. [What is `ResizeObserver`?](#q54) <span class="advanced">Advanced</span>
55. [What is `MutationObserver`?](#q55) <span class="advanced">Advanced</span>
56. [What is `navigator.sendBeacon`?](#q56) <span class="intermediate">Intermediate</span>
57. [What is `BigInt`?](#q57) <span class="beginner">Beginner</span>
58. [What is the Nullish Coalescing Operator (`??`)?](#q58) <span class="beginner">Beginner</span>
59. [What is Optional Chaining (`?.`)?](#q59) <span class="beginner">Beginner</span>
60. [What are Logical Assignment Operators?](#q60) <span class="intermediate">Intermediate</span>
61. [Explain `Promise.all` vs `Promise.allSettled`.](#q61) <span class="intermediate">Intermediate</span>
62. [What is `globalThis`?](#q62) <span class="beginner">Beginner</span>
63. [How does Garbage Collection work in JS?](#q63) <span class="advanced">Advanced</span>
64. [What causes Memory Leaks in JS?](#q64) <span class="intermediate">Intermediate</span>
65. [Debounce vs Throttle?](#q65) <span class="intermediate">Intermediate</span>
66. [What is a Polyfill?](#q66) <span class="beginner">Beginner</span>
67. [What is Tree Shaking?](#q67) <span class="intermediate">Intermediate</span>
68. [What is the `delete` operator?](#q68) <span class="beginner">Beginner</span>
69. [What is `void 0`?](#q69) <span class="beginner">Beginner</span>
70. [How do you create a Custom Event?](#q70) <span class="intermediate">Intermediate</span>
71. [What is `Object.create()`?](#q71) <span class="intermediate">Intermediate</span>
72. [What are Private Class Fields?](#q72) <span class="intermediate">Intermediate</span>
73. [What is the `Reflect` API?](#q73) <span class="advanced">Advanced</span>
74. [What is the Singleton Pattern in JS?](#q74) <span class="intermediate">Intermediate</span>
75. [What is Functional Programming?](#q75) <span class="advanced">Advanced</span>
76. [What is the Observer Pattern?](#q76) <span class="advanced">Advanced</span>
77. [What is a Factory Pattern?](#q77) <span class="intermediate">Intermediate</span>
78. [What is Currying (Advanced)?](#q78) <span class="advanced">Advanced</span>
79. [What are Typed Arrays?](#q79) <span class="advanced">Advanced</span>
80. [What is `ArrayBuffer`?](#q80) <span class="advanced">Advanced</span>
81. [What is `DataView`?](#q81) <span class="advanced">Advanced</span>
82. [What is a `Blob`?](#q82) <span class="intermediate">Intermediate</span>
83. [How does `FileReader` work?](#q83) <span class="intermediate">Intermediate</span>
84. [What is `URL` and `URLSearchParams`?](#q84) <span class="beginner">Beginner</span>
85. [What are Web Components?](#q85) <span class="advanced">Advanced</span>
86. [What is Shadow DOM?](#q86) <span class="advanced">Advanced</span>
87. [What is the difference between `Map` and Object?](#q87) <span class="intermediate">Intermediate</span>
88. [What is `Promise.race()`?](#q88) <span class="intermediate">Intermediate</span>
89. [What is `Promise.any()`?](#q89) <span class="intermediate">Intermediate</span>
90. [What is the `in` operator?](#q90) <span class="beginner">Beginner</span>
91. [What is the `static` keyword in Classes?](#q91) <span class="beginner">Beginner</span>
92. [What is `super` keyword?](#q92) <span class="beginner">Beginner</span>
93. [How do you flatten an array?](#q93) <span class="beginner">Beginner</span>
94. [What is `Function.prototype.call()`?](#q94) <span class="intermediate">Intermediate</span>
95. [What is `Function.prototype.apply()`?](#q95) <span class="intermediate">Intermediate</span>
96. [What is `Function.prototype.bind()`?](#q96) <span class="intermediate">Intermediate</span>
97. [What are Generators?](#q97) <span class="advanced">Advanced</span>
98. [What is the `Proxy` object?](#q98) <span class="advanced">Advanced</span>
99. [What is the Temporal Dead Zone (TDZ)?](#q99) <span class="intermediate">Intermediate</span>
100. [What is Coercion?](#q100) <span class="beginner">Beginner</span>

---

<a id="q1"></a>
### Q1: Explain Hoisting with examples?

**Difficulty**: Beginner

**Strategy**:
Hoisting is JavaScript's behavior of moving variable and function declarations to the top of their scope before code execution.
*   **`var`**: Hoisted and initialized with `undefined`. You can access it before declaration (result: undefined).
*   **Function Declaration**: Hoisted completely. You can call it before declaration.
*   **`let` / `const`**: Hoisted but NOT initialized. They are in the **Temporal Dead Zone (TDZ)** until the execution reaches the declaration. Accessing them early throws `ReferenceError`.

**Code Example**:
```javascript
// 1. var hoisting
console.log(a); // undefined
var a = 5;

// 2. function hoisting
greet(); // "Hello"
function greet() { console.log("Hello"); }

// 3. let/const hoisting (TDZ)
try {
  console.log(b);
} catch(e) {
  console.log(e); // ReferenceError: Cannot access 'b' before initialization
}
let b = 10;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q2"></a>
### Q2: Difference between `var`, `let`, and `const`?

**Difficulty**: Beginner

**Strategy**:
*   **`var`**:
    *   **Scope**: Function scoped.
    *   **Re-declaration**: Allowed.
    *   **Hoisting**: Initialized with `undefined`.
*   **`let`**:
    *   **Scope**: Block scoped `{ }`.
    *   **Re-declaration**: Not allowed in same scope.
    *   **Hoisting**: TDZ (ReferenceError).
*   **`const`**:
    *   **Scope**: Block scoped.
    *   **Re-assignment**: Not allowed (must initialize immediately). Note: Object properties *can* be mutated.

**Code Example**:
```javascript
if (true) {
  var x = 1;
  let y = 2;
}
console.log(x); // 1
// console.log(y); // ReferenceError: y is not defined

const obj = { name: 'Alice' };
obj.name = 'Bob'; // Allowed (Mutation)
// obj = {}; // Error (Reassignment)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q3"></a>
### Q3: Explain Closures with a practical example?

**Difficulty**: Intermediate

**Strategy**:
A **Closure** is a function that remembers its lexical scope (the variables around it) even when that function is executed outside that scope.
*   **Mechanism**: Inner functions have access to outer function variables.
*   **Use Cases**: Data privacy (encapsulation), Function factories, Memoization.

**Code Example**:
```javascript
function createCounter() {
  let count = 0; // Private variable
  
  return {
    increment: () => {
      count++;
      return count;
    },
    getCount: () => count
  };
}

const counter = createCounter();
console.log(counter.increment()); // 1
console.log(counter.increment()); // 2
// console.log(counter.count); // undefined (inaccessible)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q4"></a>
### Q4: How does the Event Loop work?

**Difficulty**: Advanced

**Strategy**:
JavaScript is single-threaded (one Call Stack). The Event Loop coordinates execution.
1.  **Call Stack**: Executes synchronous code.
2.  **Web APIs**: Browser handles async tasks (setTimeout, fetch, DOM events).
3.  **Task Queues**:
    *   **Microtask Queue**: High priority (Promises/then, queueMicrotask, MutationObserver).
    *   **Macrotask Queue (Task Queue)**: Low priority (setTimeout, setInterval, I/O).
4.  **Loop**: If Stack is empty -> Run ALL Microtasks -> Run ONE Macrotask -> Render UI -> Repeat.

**Code Example**:
```javascript
console.log('1: Start');

setTimeout(() => console.log('2: Timeout'), 0); // Macrotask

Promise.resolve().then(() => console.log('3: Promise')); // Microtask

console.log('4: End');

// Output:
// 1: Start
// 4: End
// 3: Promise (Microtasks run before Macrotasks)
// 2: Timeout
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q5"></a>
### Q5: Explain `this` keyword behavior?

**Difficulty**: Intermediate

**Strategy**:
The value of `this` depends on **how the function is called**, not where it is defined.
1.  **Global Context**: `window` (browser) or `global` (node). Undefined in strict mode.
2.  **Object Method**: The object before the dot (`obj.method()`).
3.  **Constructor**: The new instance (`new Foo()`).
4.  **Explicit Binding**: Specified via `call`, `apply`, `bind`.
5.  **Arrow Functions**: Lexical `this`. They inherit `this` from the parent scope at definition time. They do *not* have their own `this`.

**Code Example**:
```javascript
const obj = {
  name: 'Alice',
  regular() { console.log(this.name); },
  arrow: () => { console.log(this.name); }
};

obj.regular(); // "Alice"
obj.arrow();   // undefined (inherits from window/global)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q6"></a>
### Q6: Call vs Apply vs Bind?

**Difficulty**: Intermediate

**Strategy**:
All three allow you to explicitly set the value of `this`.
*   **`call(thisArg, arg1, arg2)`**: Invokes function immediately. Arguments passed individually.
*   **`apply(thisArg, [args])`**: Invokes function immediately. Arguments passed as an array.
*   **`bind(thisArg, arg1)`**: Returns a **new function** with `this` permanently bound. Does not invoke immediately.

**Code Example**:
```javascript
function greet(greeting, punctuation) {
  console.log(`${greeting}, ${this.name}${punctuation}`);
}

const user = { name: 'Bob' };

greet.call(user, 'Hello', '!');        // "Hello, Bob!"
greet.apply(user, ['Hi', '.']);        // "Hi, Bob."

const boundGreet = greet.bind(user, 'Hey');
boundGreet('?');                       // "Hey, Bob?"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q7"></a>
### Q7: What is Prototypal Inheritance?

**Difficulty**: Advanced

**Strategy**:
In JS, objects inherit directly from other objects. Every object has a hidden property `[[Prototype]]` (accessible via `__proto__`) that points to another object.
*   When you access a property, JS looks on the object itself.
*   If not found, it looks at the prototype.
*   If not found, it looks at the prototype's prototype (Prototype Chain).
*   Ends at `Object.prototype` (whose prototype is null).

**Code Example**:
```javascript
const animal = { eats: true };
const rabbit = { jumps: true };

// Inherit
Object.setPrototypeOf(rabbit, animal); 
// Or: rabbit.__proto__ = animal;

console.log(rabbit.jumps); // true (Own)
console.log(rabbit.eats);  // true (Inherited)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q8"></a>
### Q8: Explain Promise and its states?

**Difficulty**: Intermediate

**Strategy**:
A **Promise** is an object representing the eventual completion (or failure) of an asynchronous operation. It eliminates "Callback Hell".
*   **States**:
    1.  **Pending**: Initial state.
    2.  **Fulfilled (Resolved)**: Operation successful (calls `.then()`).
    3.  **Rejected**: Operation failed (calls `.catch()`).
*   Once settled (fulfilled/rejected), it cannot change state.

**Code Example**:
```javascript
const fetchData = new Promise((resolve, reject) => {
  setTimeout(() => {
    const success = true;
    if (success) resolve('Data loaded');
    else reject('Error');
  }, 1000);
});

fetchData
  .then(data => console.log(data))
  .catch(err => console.error(err))
  .finally(() => console.log('Done'));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q9"></a>
### Q9: Async/Await vs Promises?

**Difficulty**: Beginner

**Strategy**:
*   **Promises**: Use chaining (`.then().then()`). Can become messy with complex logic.
*   **Async/Await**: Syntactic sugar over Promises (ES2017). Makes async code look synchronous. Easier error handling with `try/catch`.
*   `async` function always returns a Promise. `await` pauses execution until Promise resolves.

**Code Example**:
```javascript
// Promise Chain
function getData() {
  fetch('/api')
    .then(res => res.json())
    .then(data => console.log(data))
    .catch(err => console.error(err));
}

// Async/Await
async function getDataAsync() {
  try {
    const res = await fetch('/api');
    const data = await res.json();
    console.log(data);
  } catch (err) {
    console.error(err);
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q10"></a>
### Q10: What is Event Bubbling vs Capturing?

**Difficulty**: Intermediate

**Strategy**:
When an event occurs on a DOM element (e.g., click on button inside div):
1.  **Capturing Phase (Trickling)**: Event goes down from Window -> Document -> Parent -> Target.
2.  **Target Phase**: Event reaches the target element.
3.  **Bubbling Phase**: Event bubbles up from Target -> Parent -> Document -> Window.
*   Default `addEventListener` listens to **Bubbling**.
*   Use `{ capture: true }` to listen to Capturing.
*   `event.stopPropagation()` stops the flow.

**Code Example**:
```javascript
// Bubbling (Default)
div.addEventListener('click', () => console.log('Div Clicked'));
btn.addEventListener('click', (e) => {
  console.log('Btn Clicked');
  e.stopPropagation(); // Stops div from seeing the click
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q11"></a>
### Q11: How does Event Delegation work?

**Difficulty**: Intermediate

**Strategy**:
Instead of attaching event listeners to individual child elements (which is memory expensive and doesn't work for dynamic elements), you attach **one** listener to a common parent.
*   Uses **Event Bubbling** to catch events from children.
*   Check `event.target` to see which child was clicked.

**Code Example**:
```javascript
document.getElementById('list').addEventListener('click', (e) => {
  // Check if the clicked element is an LI
  if (e.target && e.target.nodeName === 'LI') {
    console.log('List item clicked:', e.target.textContent);
  }
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q12"></a>
### Q12: Deep Copy vs Shallow Copy?

**Difficulty**: Intermediate

**Strategy**:
*   **Shallow Copy**: Copies the object's top-level properties. Nested objects are copied by *reference*. Changing a nested object in copy affects original.
    *   Methods: `Object.assign()`, Spread `...`.
*   **Deep Copy**: Recursively copies all levels. No references shared.
    *   Methods: `JSON.parse(JSON.stringify())` (fails on Functions/Dates), `structuredClone()` (modern standard), Lodash `_.cloneDeep`.

**Code Example**:
```javascript
const original = { a: 1, b: { c: 2 } };

// Shallow
const shallow = { ...original };
shallow.b.c = 99;
console.log(original.b.c); // 99 (Affected!)

// Deep
const deep = structuredClone(original);
deep.b.c = 500;
console.log(original.b.c); // 99 (Unaffected)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q13"></a>
### Q13: What is the difference between `==` and `===`?

**Difficulty**: Beginner

**Strategy**:
*   **`==` (Loose Equality)**: Performs **Type Coercion** before comparison. Converts operands to same type.
*   **`===` (Strict Equality)**: Checks both **Value** and **Type**. No coercion. Always prefer this.

**Code Example**:
```javascript
console.log(5 == '5');  // true (String '5' becomes Number 5)
console.log(5 === '5'); // false (Number vs String)

console.log(null == undefined); // true
console.log(null === undefined); // false
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q14"></a>
### Q14: Explain Higher-Order Functions?

**Difficulty**: Beginner

**Strategy**:
A Higher-Order Function (HOF) is a function that either:
1.  Takes one or more functions as **arguments** (callbacks).
2.  Returns a **function** as a result.
*   Common Examples: `map`, `filter`, `reduce`, `setTimeout`.

**Code Example**:
```javascript
// Takes a function
const numbers = [1, 2, 3];
const doubled = numbers.map(num => num * 2);

// Returns a function
function multiplier(factor) {
  return (number) => number * factor;
}
const double = multiplier(2);
console.log(double(5)); // 10
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q15"></a>
### Q15: What is Currying?

**Difficulty**: Intermediate

**Strategy**:
Currying is the process of transforming a function that takes multiple arguments `f(a, b, c)` into a sequence of functions that each take a single argument `f(a)(b)(c)`.
*   Useful for creating specialized functions (partial application).

**Code Example**:
```javascript
// Normal
const add = (a, b) => a + b;

// Curried
const curriedAdd = a => b => a + b;

const addFive = curriedAdd(5); // Partial application
console.log(addFive(10)); // 15
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q16"></a>
### Q16: What is Memoization?

**Difficulty**: Intermediate

**Strategy**:
Memoization is an optimization technique to speed up functions by **caching** the results of expensive function calls and returning the cached result when the same inputs occur again.

**Code Example**:
```javascript
function memoize(fn) {
  const cache = {};
  return function(...args) {
    const key = JSON.stringify(args);
    if (cache[key]) {
      return cache[key];
    }
    const result = fn.apply(this, args);
    cache[key] = result;
    return result;
  };
}

const slowSquare = n => { /* loop */ return n * n; };
const fastSquare = memoize(slowSquare);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q17"></a>
### Q17: What is a Generator Function?

**Difficulty**: Advanced

**Strategy**:
A Generator is a function that can be paused and resumed. It is declared with `function*`.
*   **`yield`**: Pauses execution and returns a value.
*   **`.next()`**: Resumes execution until the next `yield`.
*   Useful for iterators, infinite streams, and async flow control.

**Code Example**:
```javascript
function* idMaker() {
  let index = 0;
  while (true) {
    yield index++;
  }
}

const gen = idMaker();
console.log(gen.next().value); // 0
console.log(gen.next().value); // 1
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q18"></a>
### Q18: What is the Temporal Dead Zone (TDZ)?

**Difficulty**: Intermediate

**Strategy**:
The TDZ is the period between the start of a scope and the actual declaration of a variable (with `let` or `const`). Accessing the variable in this zone throws a `ReferenceError`. It prevents accessing variables before they are initialized.

**Code Example**:
```javascript
{
  // TDZ starts here
  // console.log(x); // ReferenceError
  
  let x = 10; // TDZ ends here
  console.log(x); // 10
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q19"></a>
### Q19: Map vs WeakMap?

**Difficulty**: Advanced

**Strategy**:
*   **Map**: Keys can be any type. Strong references to keys (prevents garbage collection). Iterable. Size property.
*   **WeakMap**: Keys must be **Objects**. Weak references (if key object is deleted elsewhere, entry is GC'd). Not iterable. No size property.
*   Use WeakMap for caching metadata about objects without causing memory leaks.

**Code Example**:
```javascript
let obj = { id: 1 };
const weakMap = new WeakMap();
weakMap.set(obj, 'metadata');

obj = null; // The entry in WeakMap is now eligible for GC
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q20"></a>
### Q20: What is Destructuring Assignment?

**Difficulty**: Beginner

**Strategy**:
Syntax that allows unpacking values from arrays, or properties from objects, into distinct variables.

**Code Example**:
```javascript
// Object
const user = { name: 'John', age: 30 };
const { name, age } = user;

// Array
const coords = [10, 20];
const [x, y] = coords;

// Renaming
const { name: userName } = user;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q21"></a>
### Q21: Explain the Spread and Rest Operator?

**Difficulty**: Beginner

**Strategy**:
Both use `...` syntax.
*   **Spread**: Expands an iterable into individual elements. Used in function calls `func(...args)` or array/object literals `[...arr]`.
*   **Rest**: Collects multiple elements into a single array. Used in function params `function(...args)` or destructuring.

**Code Example**:
```javascript
// Spread
const arr = [1, 2, 3];
const newArr = [...arr, 4]; // [1, 2, 3, 4]

// Rest
function sum(...numbers) {
  return numbers.reduce((a, b) => a + b);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q22"></a>
### Q22: What is Functional Programming in JS?

**Difficulty**: Advanced

**Strategy**:
Programming paradigm based on:
1.  **Pure Functions**: No side effects, same input = same output.
2.  **Immutability**: Don't change data, create new data.
3.  **First-Class Functions**: Functions are values.
4.  **Higher-Order Functions**: map, filter, reduce.

**Code Example**:
```javascript
// Impure
let total = 0;
const addToTotal = (n) => total += n;

// Pure
const add = (a, b) => a + b;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q23"></a>
### Q23: What are Pure Functions?

**Difficulty**: Intermediate

**Strategy**:
A function is pure if:
1.  It relies only on its inputs (no external state).
2.  It produces no side effects (doesn't modify DOM, API calls, global vars).
3.  Deterministic (Same input always gives same output).
*   Essential for Redux reducers and testing.

**Code Example**:
```javascript
// Pure
const square = x => x * x;

// Impure (depends on random)
const random = () => Math.random();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q24"></a>
### Q24: What is Type Coercion?

**Difficulty**: Beginner

**Strategy**:
Automatic conversion of values from one data type to another (e.g., String to Number).
*   **Implicit**: `5 + '5' = '55'` (Number coerced to String).
*   **Explicit**: `Number('5')`.
*   Tricky cases: `[] + [] = ""`, `true + 1 = 2`.

**Code Example**:
```javascript
console.log(1 + "2"); // "12"
console.log(1 - "2"); // -1 (String coerced to Number)
console.log(Boolean("hello")); // true
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q25"></a>
### Q25: What is a Proxy Object?

**Difficulty**: Advanced

**Strategy**:
A Proxy object wraps another object and intercepts operations (like reading/writing properties).
*   Used for validation, logging, data binding (Vue 3 reactivity), and magic APIs.

**Code Example**:
```javascript
const target = { message: "hello" };
const handler = {
  get: function(obj, prop) {
    return prop in obj ? obj[prop] : "Not found";
  }
};

const proxy = new Proxy(target, handler);
console.log(proxy.message); // "hello"
console.log(proxy.age);     // "Not found"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>
<a id="q26"></a>

### Q26: What is the difference between `null` and `undefined`?

**Difficulty**: Beginner

**Strategy:**
`undefined` means a variable has been declared but not yet assigned a value. `null` is an assignment value that represents "no value" or "empty". `typeof undefined` is `'undefined'`, while `typeof null` is `'object'` (a historical bug).

**Code Example:**

```javascript
let x;
console.log(x); // undefined

let y = null;
console.log(y); // null

console.log(x == y); // true (coercion)
console.log(x === y); // false
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q27"></a>

### Q27: How does `Array.prototype.reduce()` work?

**Difficulty**: Intermediate

**Strategy:**
`reduce()` executes a reducer function on each element of the array, passing in the return value from the calculation on the preceding element. The final result is a single value.

**Code Example:**

```javascript
const nums = [1, 2, 3, 4];
const sum = nums.reduce((acc, curr) => acc + curr, 0);
console.log(sum); // 10

// Grouping objects
const people = [{ age: 20 }, { age: 25 }, { age: 20 }];
const grouped = people.reduce((acc, person) => {
  acc[person.age] = (acc[person.age] || 0) + 1;
  return acc;
}, {});
// { '20': 2, '25': 1 }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q28"></a>

### Q28: What are ES6 Modules (Import/Export)?

**Difficulty**: Beginner

**Strategy:**
ES6 Modules allow sharing code between files. `export` exposes variables/functions, and `import` consumes them. Modules automatically run in strict mode and `this` is undefined at the top level.

**Code Example:**

```javascript
// lib.js
export const PI = 3.14;
export default function add(a, b) {
  return a + b;
}

// main.js
import add, { PI } from "./lib.js";
console.log(add(2, PI));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q29"></a>

### Q29: What is the difference between `Object.freeze()` and `Object.seal()`?

**Difficulty**: Intermediate

**Strategy:**
`Object.freeze()` makes an object immutable: no adding, removing, or changing properties. `Object.seal()` prevents adding/removing properties but allows modifying existing property values.

**Code Example:**

```javascript
const obj = { val: 10 };
Object.freeze(obj);
obj.val = 20; // Fails silently or error in strict mode
console.log(obj.val); // 10

const sealed = { val: 10 };
Object.seal(sealed);
sealed.val = 20; // Allowed
delete sealed.val; // Fails
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q30"></a>

### Q30: What is an IIFE (Immediately Invoked Function Expression)?

**Difficulty**: Intermediate

**Strategy:**
An IIFE is a function that runs as soon as it is defined. It is used to create a private scope and avoid polluting the global namespace.

**Code Example:**

```javascript
(function () {
  const secret = "I am hidden";
  console.log("Running immediately");
})();

// console.log(secret); // ReferenceError
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q31"></a>

### Q31: What is the difference between `map()` and `forEach()`?

**Difficulty**: Beginner

**Strategy:**
`map()` returns a **new array** with the results of calling a function on every element. `forEach()` executes a function for each array element but returns `undefined` (it mutates or performs side effects).

**Code Example:**

```javascript
const arr = [1, 2, 3];
const doubled = arr.map((x) => x * 2); // [2, 4, 6]

arr.forEach((x) => console.log(x)); // Logs 1, 2, 3
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q32"></a>

### Q32: What is `Strict Mode` in JavaScript?

**Difficulty**: Beginner

**Strategy:**
`"use strict";` enables strict mode. It catches common coding bloopers (like undeclared variables), prevents usage of unsafe features (like `with`), and makes `this` undefined in global functions.

**Code Example:**

```javascript
"use strict";
x = 3.14; // ReferenceError: x is not defined

function strictFunc() {
  return this;
}
console.log(strictFunc()); // undefined
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q33"></a>

### Q33: How does `NaN` behave and how to check for it?

**Difficulty**: Beginner

**Strategy:**
`NaN` stands for "Not-a-Number". It is the only value in JS that is not equal to itself (`NaN !== NaN`). Use `Number.isNaN()` to check strictly for `NaN`.

**Code Example:**

```javascript
console.log(NaN === NaN); // false
console.log(Number.isNaN(NaN)); // true
console.log(Number.isNaN("hello")); // false

// Global isNaN coerces argument
console.log(isNaN("hello")); // true
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q34"></a>

### Q34: What are `Set` and `WeakSet`?

**Difficulty**: Intermediate

**Strategy:**
`Set` is a collection of unique values (any type). `WeakSet` is a collection of objects only, where references are "weak" (if no other references exist, the object can be garbage collected). `WeakSet` is not iterable.

**Code Example:**

```javascript
const set = new Set([1, 1, 2]);
console.log(set.size); // 2

let obj = { a: 1 };
const weakSet = new WeakSet([obj]);
obj = null; // Object is now eligible for GC, removed from WeakSet
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q35"></a>

### Q35: What is the `Symbol` data type?

**Difficulty**: Advanced

**Strategy:**
`Symbol` is a primitive type used to create unique identifiers. They are often used as object keys to create "hidden" properties that don't show up in standard loops.

**Code Example:**

```javascript
const sym1 = Symbol("id");
const sym2 = Symbol("id");
console.log(sym1 === sym2); // false

const user = {
  [sym1]: 123,
};
console.log(Object.keys(user)); // []
console.log(user[sym1]); // 123
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q36"></a>

### Q36: How does `requestAnimationFrame` work?

**Difficulty**: Intermediate

**Strategy:**
It tells the browser that you wish to perform an animation and requests that the browser call a specified function before the next repaint. It's more efficient than `setTimeout` or `setInterval` for animations.

**Code Example:**

```javascript
function animate() {
  // update animation state
  console.log("Frame");
  requestAnimationFrame(animate);
}
requestAnimationFrame(animate);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q37"></a>

### Q37: What is the difference between `localStorage`, `sessionStorage`, and Cookies?

**Difficulty**: Intermediate

**Strategy:**

- **localStorage**: Persists until cleared manually (5-10MB).
- **sessionStorage**: Persists for the session (tab close clears it).
- **Cookies**: Sent with every HTTP request, small size (4KB), can have expiry.

**Code Example:**

```javascript
localStorage.setItem("theme", "dark");
sessionStorage.setItem("isLoggedIn", "true");
document.cookie = "user=Alice; expires=Thu, 18 Dec 2025 12:00:00 UTC";
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q38"></a>

### Q38: How does the `fetch` API work?

**Difficulty**: Beginner

**Strategy:**
`fetch` provides a modern interface for making network requests. It returns a Promise that resolves to the `Response` object. Unlike XHR, it doesn't reject on HTTP errors (like 404 or 500).

**Code Example:**

```javascript
fetch("https://api.example.com/data")
  .then((response) => {
    if (!response.ok) throw new Error("Network response was not ok");
    return response.json();
  })
  .then((data) => console.log(data))
  .catch((error) => console.error("Error:", error));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q39"></a>

### Q39: What is the difference between `async` and `defer` attributes in script tags?

**Difficulty**: Intermediate

**Strategy:**

- **Normal**: Parses HTML, pauses to download/execute script, resumes HTML.
- **async**: Downloads script in parallel, pauses HTML to execute immediately when downloaded. Order not guaranteed.
- **defer**: Downloads in parallel, executes **after** HTML parsing is complete. Preserves order.

**Code Example:**

```html
<script src="app.js" defer></script>
<!-- Best for dependencies -->
<script src="analytics.js" async></script>
<!-- Best for independent scripts -->
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q40"></a>

### Q40: What is the History API?

**Difficulty**: Intermediate

**Strategy:**
It allows manipulation of the browser session history (back/forward buttons) without reloading the page. Core to Single Page Applications (SPAs). Methods: `pushState`, `replaceState`.

**Code Example:**

```javascript
// Add entry to history stack
history.pushState({ page: 1 }, "title 1", "?page=1");

// Listen for back/forward navigation
window.onpopstate = function (event) {
  console.log(
    "location: " + document.location + ", state: " + JSON.stringify(event.state)
  );
};
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q41"></a>

### Q41: What is `innerHTML` vs `textContent`?

**Difficulty**: Beginner

**Strategy:**

- **`innerHTML`**: Parses content as HTML. Can be slow and unsafe (XSS risk).
- **`textContent`**: Sets raw text. Safer and faster.
- **`innerText`**: Similar to `textContent` but respects CSS styling (e.g., won't return text of hidden elements).

**Code Example:**

```javascript
const div = document.createElement("div");
div.innerHTML = "<strong>Hello</strong>"; // Bold Hello
div.textContent = "<strong>Hello</strong>"; // Literal string <strong>Hello</strong>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q42"></a>

### Q42: How do you handle errors with `try...catch...finally`?

**Difficulty**: Beginner

**Strategy:**
Code that might throw an error goes in `try`. Error handling goes in `catch`. Cleanup code (always runs) goes in `finally`.

**Code Example:**

```javascript
try {
  throw new Error("Something went wrong");
} catch (error) {
  console.error(error.message);
} finally {
  console.log("Cleanup operations");
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q43"></a>

### Q43: What is `JSON.parse` and `JSON.stringify`?

**Difficulty**: Beginner

**Strategy:**
`JSON.stringify` converts a JavaScript object/value to a JSON string. `JSON.parse` parses a JSON string into a JavaScript object. Note: `stringify` ignores functions and `undefined`.

**Code Example:**

```javascript
const obj = { name: "Alice", age: 25 };
const json = JSON.stringify(obj); // '{"name":"Alice","age":25}'
const parsed = JSON.parse(json); // { name: "Alice", age: 25 }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q44"></a>

### Q44: What is the difference between `typeof` and `instanceof`?

**Difficulty**: Beginner

**Strategy:**

- **`typeof`**: Returns a string indicating the primitive type (or 'object'/'function').
- **`instanceof`**: Checks if an object is an instance of a class/constructor (checks prototype chain).

**Code Example:**

```javascript
console.log(typeof "hello"); // "string"
console.log(typeof []); // "object"

console.log([] instanceof Array); // true
console.log([] instanceof Object); // true
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q45"></a>

### Q45: What are Template Literals?

**Difficulty**: Beginner

**Strategy:**
Enclosed by backticks (`` ` ``), they allow embedded expressions `${var}`, multi-line strings, and string interpolation.

**Code Example:**

```javascript
const name = "World";
const greeting = `Hello,
${name}!`;
console.log(greeting);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q46"></a>

### Q46: What is `Object.entries()`?

**Difficulty**: Beginner

**Strategy:**
It returns an array of a given object's own enumerable string-keyed property `[key, value]` pairs. Useful for iterating over objects.

**Code Example:**

```javascript
const obj = { a: 1, b: 2 };
for (const [key, value] of Object.entries(obj)) {
  console.log(`${key}: ${value}`);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q47"></a>

### Q47: What is the purpose of `Array.from()`?

**Difficulty**: Intermediate

**Strategy:**
It creates a new, shallow-copied Array instance from an array-like (e.g., `arguments`, `NodeList`) or iterable object (e.g., `Set`, `Map`). It also takes a map function as a second argument.

**Code Example:**

```javascript
const set = new Set([1, 2, 3]);
const arr = Array.from(set, (x) => x * 2); // [2, 4, 6]

// Create range
const range = Array.from({ length: 3 }, (_, i) => i); // [0, 1, 2]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q48"></a>

### Q48: How do you detect if a property exists in an object?

**Difficulty**: Beginner

**Strategy:**

1.  `in` operator (checks prototype chain too).
2.  `hasOwnProperty()` (checks own properties only).
3.  `Object.hasOwn()` (modern replacement for `hasOwnProperty`).
4.  Accessing property `obj.prop !== undefined` (fails if value is actually `undefined`).

**Code Example:**

```javascript
const obj = { a: 1 };
console.log("a" in obj); // true
console.log(Object.hasOwn(obj, "a")); // true
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q49"></a>

### Q49: What is the `arguments` object?

**Difficulty**: Beginner

**Strategy:**
It is an array-like object accessible inside functions (non-arrow) that contains the values of the arguments passed to that function. Modern JS prefers Rest parameters (`...args`).

**Code Example:**

```javascript
function sum() {
  let total = 0;
  for (let i = 0; i < arguments.length; i++) {
    total += arguments[i];
  }
  return total;
}
console.log(sum(1, 2, 3)); // 6
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q50"></a>

### Q50: What is the difference between `slice()` and `splice()`?

**Difficulty**: Beginner

**Strategy:**

- **`slice(start, end)`**: Returns a **new** array containing a portion of the array. Does **not** modify original.
- **`splice(start, count, ...items)`**: **Modifies** the original array by removing/replacing/adding elements. Returns removed elements.

**Code Example:**

```javascript
const arr = [1, 2, 3, 4];

const sliced = arr.slice(1, 3); // [2, 3]
console.log(arr); // [1, 2, 3, 4]

const spliced = arr.splice(1, 2); // [2, 3]
console.log(arr); // [1, 4]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q51"></a>

### Q51: What are Service Workers?

**Difficulty**: Advanced

**Strategy:**
Service Workers are scripts that run in the background, separate from a web page. They enable features like offline support (caching assets), push notifications, and background sync. They act as a proxy between the web app and the network.

**Code Example:**

```javascript
// Registering a Service Worker
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/sw.js')
    .then(reg => console.log('SW registered!', reg))
    .catch(err => console.log('SW failed', err));
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q52"></a>

### Q52: What is a Web Worker?

**Difficulty**: Intermediate

**Strategy:**
Web Workers allow running scripts in background threads. They can perform expensive calculations without blocking the UI thread (main thread). They communicate with the main thread via messages.

**Code Example:**

```javascript
// main.js
const worker = new Worker('worker.js');
worker.postMessage('Start');
worker.onmessage = (e) => console.log(e.data);

// worker.js
onmessage = (e) => {
  // Heavy computation
  postMessage('Done');
};
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q53"></a>

### Q53: What is the `Intl` API?

**Difficulty**: Intermediate

**Strategy:**
The `Intl` object provides language-sensitive string comparison, number formatting, and date/time formatting. It is the standard way to handle i18n in JS.

**Code Example:**

```javascript
const date = new Date();
const formatter = new Intl.DateTimeFormat('en-US', { month: 'long' });
console.log(formatter.format(date)); // December

const currency = new Intl.NumberFormat('ja-JP', { style: 'currency', currency: 'JPY' });
console.log(currency.format(1000)); // ￥1,000
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q54"></a>

### Q54: What is `ResizeObserver`?

**Difficulty**: Advanced

**Strategy:**
It observes changes to the dimensions of an Element's content box or border box. Useful for responsive components that need to react to their own size changes, not just the window size.

**Code Example:**

```javascript
const observer = new ResizeObserver(entries => {
  for (let entry of entries) {
    console.log(entry.contentRect.width);
  }
});
observer.observe(document.querySelector('.box'));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q55"></a>

### Q55: What is `MutationObserver`?

**Difficulty**: Advanced

**Strategy:**
It provides the ability to watch for changes being made to the DOM tree (attributes, child list, subtree). It replaces the old Mutation Events.

**Code Example:**

```javascript
const observer = new MutationObserver(mutations => {
  console.log("DOM changed!");
});
observer.observe(document.body, { childList: true, subtree: true });
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q56"></a>

### Q56: What is `navigator.sendBeacon`?

**Difficulty**: Intermediate

**Strategy:**
It allows asynchronously sending a small amount of data to a web server (usually analytics) when the user is navigating away from the page (unload/visibilitychange). Unlike XHR/fetch, it guarantees the request is sent even if the page closes.

**Code Example:**

```javascript
window.addEventListener('visibilitychange', () => {
  if (document.visibilityState === 'hidden') {
    navigator.sendBeacon('/log', JSON.stringify({ event: 'leave' }));
  }
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q57"></a>

### Q57: What is `BigInt`?

**Difficulty**: Beginner

**Strategy:**
`BigInt` is a primitive type used to represent integers larger than `2^53 - 1` (MAX_SAFE_INTEGER). Created by appending `n` to an integer or calling `BigInt()`.

**Code Example:**

```javascript
const huge = 9007199254740991n;
const big = BigInt(9007199254740991);
console.log(huge + 1n); // 9007199254740992n
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q58"></a>

### Q58: What is the Nullish Coalescing Operator (`??`)?

**Difficulty**: Beginner

**Strategy:**
It returns the right-hand side operand when the left-hand side operand is `null` or `undefined`. Unlike `||`, it does not fall back for falsy values like `0`, `""`, or `false`.

**Code Example:**

```javascript
const count = 0;
console.log(count || 10); // 10 (0 is falsy)
console.log(count ?? 10); // 0 (0 is not null/undefined)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q59"></a>

### Q59: What is Optional Chaining (`?.`)?

**Difficulty**: Beginner

**Strategy:**
It permits reading the value of a property located deep within a chain of connected objects without explicitly checking that each reference in the chain is valid. Short-circuits to `undefined` if a reference is nullish.

**Code Example:**

```javascript
const user = {};
console.log(user.address?.street); // undefined (no error)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q60"></a>

### Q60: What are Logical Assignment Operators?

**Difficulty**: Intermediate

**Strategy:**
They combine logical operations with assignment: `||=` (assign if falsy), `&&=` (assign if truthy), `??=` (assign if nullish).

**Code Example:**

```javascript
let a = null;
a ??= 10; // a becomes 10

let b = 5;
b &&= 2; // b becomes 2 (because 5 is truthy)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q61"></a>

### Q61: Explain `Promise.all` vs `Promise.allSettled`.

**Difficulty**: Intermediate

**Strategy:**
*   **`Promise.all`**: Waits for all promises to resolve. Rejects immediately if **any** promise rejects (fail-fast).
*   **`Promise.allSettled`**: Waits for all promises to finish (resolve or reject). Returns an array of status objects.

**Code Example:**

```javascript
const p1 = Promise.resolve(1);
const p2 = Promise.reject('error');

Promise.all([p1, p2]).catch(console.log); // 'error'
Promise.allSettled([p1, p2]).then(console.log);
// [{status: 'fulfilled', value: 1}, {status: 'rejected', reason: 'error'}]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q62"></a>

### Q62: What is `globalThis`?

**Difficulty**: Beginner

**Strategy:**
A standard global property that contains the global `this` value across environments (window in browser, global in Node.js, self in workers).

**Code Example:**

```javascript
console.log(globalThis === window); // true (in browser)
console.log(globalThis === global); // true (in Node)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q63"></a>

### Q63: How does Garbage Collection work in JS?

**Difficulty**: Advanced

**Strategy:**
JS engines (like V8) use "Mark-and-Sweep". They start from roots (global objects, stack) and mark all reachable objects. Any object not marked is unreachable and swept (memory reclaimed).

**Code Example:**

```javascript
let obj = { a: 1 }; // Referenced by 'obj'
obj = null; // { a: 1 } is now unreachable -> GC will clean it
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q64"></a>

### Q64: What causes Memory Leaks in JS?

**Difficulty**: Intermediate

**Strategy:**
Common causes:
1.  Unintentional Global Variables.
2.  Forgotten Timers/Intervals.
3.  Closures holding references.
4.  Detached DOM elements (JS holds ref, but element removed from document).

**Code Example:**

```javascript
// Detached DOM
let detached = document.createElement('div'); // Created but not appended
// If 'detached' is never nulled, it stays in memory.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q65"></a>

### Q65: Debounce vs Throttle?

**Difficulty**: Intermediate

**Strategy:**
*   **Debounce**: Delays execution until a certain time has passed since the *last* event (e.g., wait for typing to stop).
*   **Throttle**: Ensures execution happens at most once every specified interval (e.g., scroll handler runs every 100ms).

**Code Example:**

```javascript
// Debounce concept
function debounce(func, delay) {
  let timeout;
  return (...args) => {
    clearTimeout(timeout);
    timeout = setTimeout(() => func(...args), delay);
  };
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q66"></a>

### Q66: What is a Polyfill?

**Difficulty**: Beginner

**Strategy:**
A piece of code (usually JS) used to provide modern functionality on older browsers that do not natively support it (e.g., adding `Array.prototype.includes` to IE11).

**Code Example:**

```javascript
if (!String.prototype.startsWith) {
  String.prototype.startsWith = function(search, pos) {
    return this.substr(!pos || pos < 0 ? 0 : +pos, search.length) === search;
  };
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q67"></a>

### Q67: What is Tree Shaking?

**Difficulty**: Intermediate

**Strategy:**
A term used in bundlers (Webpack, Rollup) to remove "dead code" (unused exports) from the final bundle. It relies on ES6 static module structure (`import`/`export`).

**Code Example:**

```javascript
// utils.js
export const a = 1;
export const b = 2;

// main.js
import { a } from './utils';
// 'b' is not used, so Tree Shaking removes it from bundle.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q68"></a>

### Q68: What is the `delete` operator?

**Difficulty**: Beginner

**Strategy:**
It removes a property from an object. It returns `true` if successful. Note: It does not free memory immediately (GC handles that) and can affect optimization (makes objects "slow" in V8).

**Code Example:**

```javascript
const obj = { a: 1 };
delete obj.a;
console.log(obj.a); // undefined
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q69"></a>

### Q69: What is `void 0`?

**Difficulty**: Beginner

**Strategy:**
The `void` operator evaluates an expression and returns `undefined`. `void 0` is a safe way to get `undefined` because `undefined` could technically be shadowed (though strict mode prevents this).

**Code Example:**

```javascript
// <a href="javascript:void(0)">Click me</a>
// Prevents navigation
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q70"></a>

### Q70: How do you create a Custom Event?

**Difficulty**: Intermediate

**Strategy:**
Use the `CustomEvent` constructor. You can pass a name and a `detail` object with data. Dispatch it using `dispatchEvent`.

**Code Example:**

```javascript
const event = new CustomEvent('hello', { detail: { name: 'World' } });
window.addEventListener('hello', e => console.log(e.detail.name));
window.dispatchEvent(event);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q71"></a>

### Q71: What is `Object.create()`?

**Difficulty**: Intermediate

**Strategy:**
It creates a new object, using an existing object as the prototype of the newly created object. It's a direct way to implement inheritance without constructor functions or classes.

**Code Example:**

```javascript
const proto = { greet() { return "Hello"; } };
const obj = Object.create(proto);
console.log(obj.greet()); // Hello
console.log(Object.getPrototypeOf(obj) === proto); // true
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q72"></a>

### Q72: What are Private Class Fields?

**Difficulty**: Intermediate

**Strategy:**
Declared with a `#` prefix. They are only accessible within the class body and cannot be accessed or modified from outside (true privacy).

**Code Example:**

```javascript
class Counter {
  #count = 0;
  increment() { this.#count++; }
  getCount() { return this.#count; }
}
const c = new Counter();
// c.#count // SyntaxError
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q73"></a>

### Q73: What is the `Reflect` API?

**Difficulty**: Advanced

**Strategy:**
It provides methods for intercepting JavaScript operations. It works closely with Proxies. It has methods corresponding to Proxy traps (`Reflect.get`, `Reflect.set`, etc.).

**Code Example:**

```javascript
const obj = { a: 1 };
Reflect.set(obj, 'a', 2);
console.log(Reflect.get(obj, 'a')); // 2
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q74"></a>

### Q74: What is the Singleton Pattern in JS?

**Difficulty**: Intermediate

**Strategy:**
A design pattern that ensures a class has only one instance and provides a global point of access to it. In JS, object literals are singletons by default, but modules are the modern way.

**Code Example:**

```javascript
// Module Singleton
let instance;
class DB {
  constructor() {
    if (instance) return instance;
    instance = this;
  }
}
export default new DB();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q75"></a>

### Q75: What is Functional Programming?

**Difficulty**: Advanced

**Strategy:**
A paradigm where programs are constructed by applying and composing functions. Key concepts: Pure functions, Immutability, Higher-order functions, and avoiding side effects.

**Code Example:**

```javascript
// Imperative
let sum = 0;
for (let i = 0; i < arr.length; i++) sum += arr[i];

// Functional
const sum = arr.reduce((a, b) => a + b, 0);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q76"></a>

### Q76: What is the Observer Pattern?

**Difficulty**: Advanced

**Strategy:**
A design pattern where an object (Subject) maintains a list of dependents (Observers) and notifies them of state changes. The basis of event listeners and RxJS.

**Code Example:**

```javascript
class Subject {
  constructor() { this.observers = []; }
  subscribe(fn) { this.observers.push(fn); }
  notify(data) { this.observers.forEach(fn => fn(data)); }
}

const subj = new Subject();
subj.subscribe(data => console.log(data));
subj.notify("Event fired!");
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q77"></a>

### Q77: What is a Factory Pattern?

**Difficulty**: Intermediate

**Strategy:**
A pattern to create objects without specifying the exact class of object that will be created. It separates object creation logic from usage.

**Code Example:**

```javascript
function createUser(role) {
  if (role === 'admin') return new Admin();
  if (role === 'user') return new User();
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q78"></a>

### Q78: What is Currying (Advanced)?

**Difficulty**: Advanced

**Strategy:**
Transforming a function with multiple arguments into a sequence of functions each taking a single argument. Useful for composition and partial application.

**Code Example:**

```javascript
const multiply = a => b => a * b;
const double = multiply(2); // Partial application
console.log(double(5)); // 10
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q79"></a>

### Q79: What are Typed Arrays?

**Difficulty**: Advanced

**Strategy:**
Array-like objects that provide a mechanism for reading and writing raw binary data in memory buffers. E.g., `Uint8Array`, `Float32Array`. Used in WebGL, Canvas, and File APIs.

**Code Example:**

```javascript
const buffer = new ArrayBuffer(16);
const int32View = new Int32Array(buffer);
int32View[0] = 42;
console.log(int32View[0]); // 42
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q80"></a>

### Q80: What is `ArrayBuffer`?

**Difficulty**: Advanced

**Strategy:**
It represents a generic, fixed-length raw binary data buffer. You cannot manipulate it directly; you need a "view" (like `DataView` or Typed Array) to read/write.

**Code Example:**

```javascript
const buffer = new ArrayBuffer(8); // 8 bytes
console.log(buffer.byteLength); // 8
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q81"></a>

### Q81: What is `DataView`?

**Difficulty**: Advanced

**Strategy:**
A low-level interface for reading and writing multiple number types in an `ArrayBuffer`, regardless of the platform's endianness.

**Code Example:**

```javascript
const buffer = new ArrayBuffer(4);
const view = new DataView(buffer);
view.setInt8(0, 127);
console.log(view.getInt8(0)); // 127
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q82"></a>

### Q82: What is a `Blob`?

**Difficulty**: Intermediate

**Strategy:**
Binary Large Object. It represents data that isn't necessarily in a JavaScript-native format. File objects are a specific kind of Blob. Used for file uploads or creating object URLs.

**Code Example:**

```javascript
const blob = new Blob(["Hello, world!"], { type: "text/plain" });
const url = URL.createObjectURL(blob);
// url can be used in <a href="..."> or <img>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q83"></a>

### Q83: How does `FileReader` work?

**Difficulty**: Intermediate

**Strategy:**
It lets web applications asynchronously read the contents of files (or raw data buffers) stored on the user's computer, using `File` or `Blob` objects.

**Code Example:**

```javascript
const reader = new FileReader();
reader.onload = function(e) {
  console.log(e.target.result); // File content
};
// reader.readAsText(fileInput.files[0]);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q84"></a>

### Q84: What is `URL` and `URLSearchParams`?

**Difficulty**: Beginner

**Strategy:**
The `URL` interface represents an object providing static methods used for creating object URLs. `URLSearchParams` defines utility methods to work with the query string of a URL.

**Code Example:**

```javascript
const url = new URL('https://example.com?foo=1&bar=2');
const params = new URLSearchParams(url.search);
console.log(params.get('foo')); // "1"
params.set('baz', '3');
console.log(params.toString()); // "foo=1&bar=2&baz=3"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q85"></a>

### Q85: What are Web Components?

**Difficulty**: Advanced

**Strategy:**
A suite of technologies (Custom Elements, Shadow DOM, HTML Templates) allowing you to create reusable custom elements with their own functionality and isolated styles.

**Code Example:**

```javascript
class MyElement extends HTMLElement {
  connectedCallback() {
    this.innerHTML = `<p>Hello Web Components!</p>`;
  }
}
customElements.define('my-element', MyElement);
// <my-element></my-element>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q86"></a>

### Q86: What is Shadow DOM?

**Difficulty**: Advanced

**Strategy:**
It allows you to attach a hidden DOM tree to an element. The shadow DOM is encapsulated, meaning styles inside don't leak out and global styles don't leak in.

**Code Example:**

```javascript
const host = document.querySelector('#host');
const shadow = host.attachShadow({ mode: 'open' });
shadow.innerHTML = `<style>p { color: red; }</style><p>I am red!</p>`;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q87"></a>

### Q87: What is the difference between `Map` and Object?

**Difficulty**: Intermediate

**Strategy:**
*   **Keys**: Object keys are Strings/Symbols. Map keys can be **any** value (objects, functions).
*   **Order**: Map preserves insertion order. Object keys are not guaranteed (though mostly predictable now).
*   **Size**: `map.size` is O(1). Object size needs manual calculation.

**Code Example:**

```javascript
const map = new Map();
const keyObj = {};
map.set(keyObj, 'value');
console.log(map.get(keyObj)); // 'value'
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q88"></a>

### Q88: What is `Promise.race()`?

**Difficulty**: Intermediate

**Strategy:**
It returns a promise that fulfills or rejects as soon as one of the promises in the iterable fulfills or rejects, with the value or reason from that promise.

**Code Example:**

```javascript
const p1 = new Promise(r => setTimeout(r, 500, 'one'));
const p2 = new Promise(r => setTimeout(r, 100, 'two'));

Promise.race([p1, p2]).then(console.log); // "two"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q89"></a>

### Q89: What is `Promise.any()`?

**Difficulty**: Intermediate

**Strategy:**
It takes an iterable of Promise objects and, as soon as one of the promises fulfills, returns a single promise that resolves with the value from that promise. If no promises fulfill, it rejects with an `AggregateError`.

**Code Example:**

```javascript
const p1 = Promise.reject('error');
const p2 = Promise.resolve('success');
Promise.any([p1, p2]).then(console.log); // "success"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q90"></a>

### Q90: What is the `in` operator?

**Difficulty**: Beginner

**Strategy:**
The `in` operator returns `true` if the specified property is in the specified object or its prototype chain.

**Code Example:**

```javascript
const car = { make: 'Honda', model: 'Accord' };
console.log('make' in car); // true
console.log('toString' in car); // true (from Object.prototype)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q91"></a>

### Q91: What is the `static` keyword in Classes?

**Difficulty**: Beginner

**Strategy:**
Static methods or properties are defined on the class itself, not on instances of the class. They are often used for utility functions.

**Code Example:**

```javascript
class MathUtil {
  static add(a, b) { return a + b; }
}
console.log(MathUtil.add(1, 2)); // 3
// const m = new MathUtil(); m.add(1, 2); // Error
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q92"></a>

### Q92: What is `super` keyword?

**Difficulty**: Beginner

**Strategy:**
It is used to access and call functions on an object's parent. In classes, `super()` calls the parent constructor, and `super.method()` calls a parent method.

**Code Example:**

```javascript
class Animal {
  constructor(name) { this.name = name; }
}
class Dog extends Animal {
  constructor(name) {
    super(name); // Must call super before accessing 'this'
    this.type = 'dog';
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q93"></a>

### Q93: How do you flatten an array?

**Difficulty**: Beginner

**Strategy:**
Use `Array.prototype.flat(depth)`. The depth specifies how deep a nested array structure should be flattened. Default is 1. Use `Infinity` for deep flattening.

**Code Example:**

```javascript
const arr = [1, [2, [3, [4]]]];
console.log(arr.flat(2)); // [1, 2, 3, [4]]
console.log(arr.flat(Infinity)); // [1, 2, 3, 4]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q94"></a>

### Q94: What is `Function.prototype.call()`?

**Difficulty**: Intermediate

**Strategy:**
It calls a function with a given `this` value and arguments provided individually.

**Code Example:**

```javascript
function greet() { console.log(this.name); }
const person = { name: 'Alice' };
greet.call(person); // Alice
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q95"></a>

### Q95: What is `Function.prototype.apply()`?

**Difficulty**: Intermediate

**Strategy:**
Similar to `call()`, but arguments are provided as an array (or array-like object).

**Code Example:**

```javascript
const nums = [1, 2, 3];
console.log(Math.max.apply(null, nums)); // 3
// Modern equivalent: Math.max(...nums)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q96"></a>

### Q96: What is `Function.prototype.bind()`?

**Difficulty**: Intermediate

**Strategy:**
It creates a **new function** that, when called, has its `this` keyword set to the provided value. It does not execute immediately.

**Code Example:**

```javascript
const module = {
  x: 42,
  getX: function() { return this.x; }
};
const unbound = module.getX;
console.log(unbound()); // undefined (global scope)

const bound = unbound.bind(module);
console.log(bound()); // 42
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q97"></a>

### Q97: What are Generators?

**Difficulty**: Advanced

**Strategy:**
Functions that can be exited and later re-entered. Their context (variable bindings) remains saved across re-entrances. Defined with `function*`. Use `yield` to return values.

**Code Example:**

```javascript
function* idMaker() {
  let index = 0;
  while (true) yield index++;
}
const gen = idMaker();
console.log(gen.next().value); // 0
console.log(gen.next().value); // 1
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q98"></a>

### Q98: What is the `Proxy` object?

**Difficulty**: Advanced

**Strategy:**
It allows you to create an object that can be used in place of the original object, but which may redefine fundamental Object operations like getting, setting, and defining properties.

**Code Example:**

```javascript
const target = {};
const proxy = new Proxy(target, {
  get: (obj, prop) => prop in obj ? obj[prop] : 37
});
console.log(proxy.a); // 37
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q99"></a>

### Q99: What is the Temporal Dead Zone (TDZ)?

**Difficulty**: Intermediate

**Strategy:**
The time between the entering of a scope (where the variable is hoisted) and the actual declaration of the variable. Accessing `let` or `const` variables in TDZ throws a `ReferenceError`.

**Code Example:**

```javascript
{
  // TDZ starts here
  // console.log(bestFood); // ReferenceError
  let bestFood = "Pizza"; // TDZ ends here
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q100"></a>

### Q100: What is Coercion?

**Difficulty**: Beginner

**Strategy:**
The automatic or implicit conversion of values from one data type to another (e.g., strings to numbers). "Type casting" is explicit.

**Code Example:**

```javascript
const val = 1 + "2"; // "12" (number coerced to string)
const bool = !!"text"; // true (string coerced to boolean)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>
