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
