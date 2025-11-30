# JavaScript Interview Questions

## Table of Contents
| No. | Question | Difficulty |
| --- | -------- | ---------- |
| 1 | [How do you implement a robust debounce function with immediate execution option?](#how-do-you-implement-a-robust-debounce-function-with-immediate-execution-option) | Intermediate |
| 2 | [How do you deeply clone an object handling circular references and special types (Date, RegExp)?](#how-do-you-deeply-clone-an-object-handling-circular-references-and-special-types-date-regexp) | Intermediate |
| 3 | [How do you implement a custom Promise.allSettled() polyfill?](#how-do-you-implement-a-custom-promise.allsettled-polyfill) | Intermediate |
| 4 | [How do you create a private variable in JavaScript without using the '#' private field syntax?](#how-do-you-create-a-private-variable-in-javascript-without-using-the-#-private-field-syntax) | Intermediate |
| 5 | [How do you efficiently flatten a deeply nested array without using `Array.prototype.flat`?](#how-do-you-efficiently-flatten-a-deeply-nested-array-without-using-array.prototype.flat) | Intermediate |
| 6 | [How do you implement function composition (pipe) from scratch?](#how-do-you-implement-function-composition-pipe-from-scratch) | Advanced |
| 7 | [How do you use Proxy to implement a validation schema for an object?](#how-do-you-use-proxy-to-implement-a-validation-schema-for-an-object) | Advanced |
| 8 | [How do you implement an event emitter (Pub/Sub pattern) from scratch?](#how-do-you-implement-an-event-emitter-pubsub-pattern-from-scratch) | Advanced |
| 9 | [How do you throttle a function to ensure it runs at most once every X milliseconds?](#how-do-you-throttle-a-function-to-ensure-it-runs-at-most-once-every-x-milliseconds) | Advanced |
| 10 | [How do you implement a memoization function to cache expensive calculation results?](#how-do-you-implement-a-memoization-function-to-cache-expensive-calculation-results) | Advanced |
| 11 | [How do you parallelize async tasks with a concurrency limit?](#how-do-you-parallelize-async-tasks-with-a-concurrency-limit) | Advanced |
| 12 | [How do you implement a custom `instanceof` operator?](#how-do-you-implement-a-custom-instanceof-operator) | Advanced |
| 13 | [How do you handle error boundaries in vanilla JavaScript (similar to React)?](#how-do-you-handle-error-boundaries-in-vanilla-javascript-similar-to-react) | Advanced |
| 14 | [How do you implement currying to transform a function?](#how-do-you-implement-currying-to-transform-a-function) | Advanced |
| 15 | [How do you safely access deeply nested properties (Optional Chaining polyfill)?](#how-do-you-safely-access-deeply-nested-properties-optional-chaining-polyfill) | Advanced |
| 16 | [How do you implement a custom Iterable using Symbol.iterator?](#how-do-you-implement-a-custom-iterable-using-symbol.iterator) | Intermediate |
| 17 | [How do you use Generators for asynchronous flow control (co-routine pattern)?](#how-do-you-use-generators-for-asynchronous-flow-control-co-routine-pattern) | Intermediate |
| 18 | [How do you detect and fix memory leaks in JavaScript applications?](#how-do-you-detect-and-fix-memory-leaks-in-javascript-applications) | Intermediate |
| 19 | [How do you optimize large array processing using Web Workers?](#how-do-you-optimize-large-array-processing-using-web-workers) | Intermediate |
| 20 | [How do you implement a basic Observable pattern?](#how-do-you-implement-a-basic-observable-pattern) | Beginner |
| 21 | [How do you use the IntersectionObserver API for lazy loading images?](#how-do-you-use-the-intersectionobserver-api-for-lazy-loading-images) | Intermediate |
| 22 | [How do you use the MutationObserver API to track DOM changes?](#how-do-you-use-the-mutationobserver-api-to-track-dom-changes) | Intermediate |
| 23 | [How do you implement a sticky header using pure JavaScript?](#how-do-you-implement-a-sticky-header-using-pure-javascript) | Intermediate |
| 24 | [How do you validate email using regex correctly?](#how-do-you-validate-email-using-regex-correctly) | Intermediate |
| 25 | [How do you format numbers as currency using Intl.NumberFormat?](#how-do-you-format-numbers-as-currency-using-intl.numberformat) | Intermediate |
| 26 | [How do you format dates using Intl.DateTimeFormat?](#how-do-you-format-dates-using-intl.datetimeformat) | Intermediate |
| 27 | [How do you implement drag and drop using the HTML5 Drag and Drop API?](#how-do-you-implement-drag-and-drop-using-the-html5-drag-and-drop-api) | Intermediate |
| 28 | [How do you read files using the FileReader API?](#how-do-you-read-files-using-the-filereader-api) | Intermediate |
| 29 | [How do you use the Clipboard API to copy text to clipboard?](#how-do-you-use-the-clipboard-api-to-copy-text-to-clipboard) | Intermediate |
| 30 | [How do you detect network status changes (online/offline)?](#how-do-you-detect-network-status-changes-onlineoffline) | Intermediate |
| 31 | [How do you use the Geolocation API to get user position?](#how-do-you-use-the-geolocation-api-to-get-user-position) | Intermediate |
| 32 | [How do you implement a virtual list (windowing) for large datasets?](#how-do-you-implement-a-virtual-list-windowing-for-large-datasets) | Intermediate |
| 33 | [How do you optimize event listeners using event delegation?](#how-do-you-optimize-event-listeners-using-event-delegation) | Intermediate |
| 34 | [How do you prevent prototype pollution attacks?](#how-do-you-prevent-prototype-pollution-attacks) | Intermediate |
| 35 | [How do you securely store tokens in the browser (HttpOnly vs LocalStorage)?](#how-do-you-securely-store-tokens-in-the-browser-httponly-vs-localstorage) | Intermediate |
| 36 | [How do you implement CSRF protection in AJAX requests?](#how-do-you-implement-csrf-protection-in-ajax-requests) | Intermediate |
| 37 | [How do you sanitize user input to prevent XSS?](#how-do-you-sanitize-user-input-to-prevent-xss) | Intermediate |
| 38 | [How do you use the BroadcastChannel API for tab communication?](#how-do-you-use-the-broadcastchannel-api-for-tab-communication) | Intermediate |
| 39 | [How do you use SharedWorkers for shared state between tabs?](#how-do-you-use-sharedworkers-for-shared-state-between-tabs) | Intermediate |
| 40 | [How do you implement a simple state management system (like Redux) from scratch?](#how-do-you-implement-a-simple-state-management-system-like-redux-from-scratch) | Intermediate |
| 41 | [How do you implement a router from scratch (Hash vs History API)?](#how-do-you-implement-a-router-from-scratch-hash-vs-history-api) | Intermediate |
| 42 | [How do you parse query string parameters without a library?](#how-do-you-parse-query-string-parameters-without-a-library) | Intermediate |
| 43 | [How do you implement a dark mode toggle using CSS variables and JS?](#how-do-you-implement-a-dark-mode-toggle-using-css-variables-and-js) | Intermediate |
| 44 | [How do you detect if an element is visible in the viewport?](#how-do-you-detect-if-an-element-is-visible-in-the-viewport) | Intermediate |
| 45 | [How do you implement infinite scrolling using JavaScript?](#how-do-you-implement-infinite-scrolling-using-javascript) | Intermediate |
| 46 | [How do you sort an array of objects by multiple keys?](#how-do-you-sort-an-array-of-objects-by-multiple-keys) | Intermediate |
| 47 | [How do you remove duplicates from an array of objects?](#how-do-you-remove-duplicates-from-an-array-of-objects) | Intermediate |
| 48 | [How do you find the intersection of two arrays?](#how-do-you-find-the-intersection-of-two-arrays) | Intermediate |
| 49 | [How do you shuffle an array (Fisher-Yates algorithm)?](#how-do-you-shuffle-an-array-fisher-yates-algorithm) | Intermediate |
| 50 | [How do you generate a random UUID in JavaScript?](#how-do-you-generate-a-random-uuid-in-javascript) | Intermediate |
| 51 | [How do you convert RGB to Hex using JavaScript?](#how-do-you-convert-rgb-to-hex-using-javascript) | Intermediate |
| 52 | [How do you detect mobile devices using JavaScript?](#how-do-you-detect-mobile-devices-using-javascript) | Intermediate |
| 53 | [How do you disable right-click context menu?](#how-do-you-disable-right-click-context-menu) | Intermediate |
| 54 | [How do you copy text to clipboard without the Clipboard API (fallback)?](#how-do-you-copy-text-to-clipboard-without-the-clipboard-api-fallback) | Intermediate |
| 55 | [How do you trigger a file download programmatically?](#how-do-you-trigger-a-file-download-programmatically) | Intermediate |
| 56 | [How do you use `requestAnimationFrame` for smooth animations?](#how-do-you-use-requestanimationframe-for-smooth-animations) | Intermediate |
| 57 | [How do you measure performance using `performance.now()`?](#how-do-you-measure-performance-using-performance.now) | Intermediate |
| 58 | [How do you use `console.time` and `console.timeEnd` for debugging?](#how-do-you-use-console.time-and-console.timeend-for-debugging) | Intermediate |
| 59 | [How do you debug memory leaks using Chrome DevTools?](#how-do-you-debug-memory-leaks-using-chrome-devtools) | Intermediate |
| 60 | [How do you use the `debugger` statement effectively?](#how-do-you-use-the-debugger-statement-effectively) | Intermediate |
| 61 | [How do you implement a simple template engine?](#how-do-you-implement-a-simple-template-engine) | Intermediate |
| 62 | [How do you parse JSON safely without throwing errors?](#how-do-you-parse-json-safely-without-throwing-errors) | Intermediate |
| 63 | [How do you stringify objects with circular references?](#how-do-you-stringify-objects-with-circular-references) | Intermediate |
| 64 | [How do you check if two objects are deeply equal?](#how-do-you-check-if-two-objects-are-deeply-equal) | Intermediate |
| 65 | [How do you get unique values from an array using Set?](#how-do-you-get-unique-values-from-an-array-using-set) | Intermediate |
| 66 | [How do you merge two objects deeply?](#how-do-you-merge-two-objects-deeply) | Intermediate |
| 67 | [How do you implement a `sleep` or `delay` function using Promises?](#how-do-you-implement-a-sleep-or-delay-function-using-promises) | Intermediate |
| 68 | [How do you cancel a fetch request using AbortController?](#how-do-you-cancel-a-fetch-request-using-abortcontroller) | Intermediate |
| 69 | [How do you set a timeout for a fetch request?](#how-do-you-set-a-timeout-for-a-fetch-request) | Intermediate |
| 70 | [How do you retry a failed API call with exponential backoff?](#how-do-you-retry-a-failed-api-call-with-exponential-backoff) | Intermediate |
| 71 | [How do you upload files using `FormData`?](#how-do-you-upload-files-using-formdata) | Intermediate |
| 72 | [How do you send JSON data using `fetch`?](#how-do-you-send-json-data-using-fetch) | Intermediate |
| 73 | [How do you handle HTTP errors in `fetch` (since it doesn't reject on 4xx/5xx)?](#how-do-you-handle-http-errors-in-fetch-since-it-doesnt-reject-on-4xx5xx) | Intermediate |
| 74 | [How do you use `navigator.sendBeacon` for analytics?](#how-do-you-use-navigator.sendbeacon-for-analytics) | Intermediate |
| 75 | [How do you preload images using JavaScript?](#how-do-you-preload-images-using-javascript) | Intermediate |
| 76 | [How do you check if a variable is an array?](#how-do-you-check-if-a-variable-is-an-array) | Intermediate |
| 77 | [How do you check if a variable is a number (and not NaN)?](#how-do-you-check-if-a-variable-is-a-number-and-not-nan) | Intermediate |
| 78 | [How do you convert a NodeList to an Array?](#how-do-you-convert-a-nodelist-to-an-array) | Intermediate |
| 79 | [How do you get the last element of an array?](#how-do-you-get-the-last-element-of-an-array) | Intermediate |
| 80 | [How do you clear an array efficiently?](#how-do-you-clear-an-array-efficiently) | Intermediate |
| 81 | [How do you loop over an object's properties?](#how-do-you-loop-over-an-objects-properties) | Intermediate |
| 82 | [How do you use `Object.entries()` and `Object.fromEntries()`?](#how-do-you-use-object.entries-and-object.fromentries) | Intermediate |
| 83 | [How do you freeze an object to prevent modifications?](#how-do-you-freeze-an-object-to-prevent-modifications) | Intermediate |
| 84 | [How do you seal an object?](#how-do-you-seal-an-object) | Intermediate |
| 85 | [How do you use `Object.create()` for inheritance?](#how-do-you-use-object.create-for-inheritance) | Intermediate |
| 86 | [How do you implement a mixin in JavaScript?](#how-do-you-implement-a-mixin-in-javascript) | Intermediate |
| 87 | [How do you use factory functions vs classes?](#how-do-you-use-factory-functions-vs-classes) | Intermediate |
| 88 | [How do you use private class fields (#)?](#how-do-you-use-private-class-fields-#) | Intermediate |
| 89 | [How do you use static class methods?](#how-do-you-use-static-class-methods) | Intermediate |
| 90 | [How do you implement a Singleton using a closure?](#how-do-you-implement-a-singleton-using-a-closure) | Intermediate |
| 91 | [How do you use default parameters in functions?](#how-do-you-use-default-parameters-in-functions) | Intermediate |
| 92 | [How do you use the rest operator `...`?](#how-do-you-use-the-rest-operator-...) | Intermediate |
| 93 | [How do you use the spread operator `...`?](#how-do-you-use-the-spread-operator-...) | Intermediate |
| 94 | [How do you destructure nested objects?](#how-do-you-destructure-nested-objects) | Intermediate |
| 95 | [How do you swap variables using destructuring?](#how-do-you-swap-variables-using-destructuring) | Intermediate |
| 96 | [How do you use template literals for multiline strings?](#how-do-you-use-template-literals-for-multiline-strings) | Intermediate |
| 97 | [How do you use tagged template literals?](#how-do-you-use-tagged-template-literals) | Intermediate |
| 98 | [How do you use `String.prototype.includes()` vs `indexOf()`?](#how-do-you-use-string.prototype.includes-vs-indexof) | Intermediate |
| 99 | [How do you pad a string using `padStart` and `padEnd`?](#how-do-you-pad-a-string-using-padstart-and-padend) | Intermediate |
| 100 | [How do you trim strings using `trim`, `trimStart`, `trimEnd`?](#how-do-you-trim-strings-using-trim-trimstart-trimend) | Intermediate |
| 101 | [How do you replace all occurrences of a string using `replaceAll`?](#how-do-you-replace-all-occurrences-of-a-string-using-replaceall) | Intermediate |
| 102 | [How do you use `Array.prototype.map()`?](#how-do-you-use-array.prototype.map) | Intermediate |
| 103 | [How do you use `Array.prototype.filter()`?](#how-do-you-use-array.prototype.filter) | Intermediate |
| 104 | [How do you use `Array.prototype.reduce()`?](#how-do-you-use-array.prototype.reduce) | Intermediate |
| 105 | [How do you use `Array.prototype.find()` and `findIndex()`?](#how-do-you-use-array.prototype.find-and-findindex) | Intermediate |
| 106 | [How do you use `Array.prototype.some()` and `every()`?](#how-do-you-use-array.prototype.some-and-every) | Intermediate |
| 107 | [How do you use `Array.prototype.flat()` and `flatMap()`?](#how-do-you-use-array.prototype.flat-and-flatmap) | Intermediate |
| 108 | [How do you sort numbers correctly (since default sort is lexicographical)?](#how-do-you-sort-numbers-correctly-since-default-sort-is-lexicographical) | Intermediate |
| 109 | [How do you create an array of a specific length filled with a value?](#how-do-you-create-an-array-of-a-specific-length-filled-with-a-value) | Intermediate |
| 110 | [How do you get query parameters from a URL object?](#how-do-you-get-query-parameters-from-a-url-object) | Intermediate |
| 111 | [How do you use `URLSearchParams`?](#how-do-you-use-urlsearchparams) | Intermediate |
| 112 | [How do you encode and decode URLs (`encodeURIComponent`)?](#how-do-you-encode-and-decode-urls-encodeuricomponent) | Intermediate |
| 113 | [How do you use `Math.random()` effectively?](#how-do-you-use-math.random-effectively) | Intermediate |
| 114 | [How do you round numbers using `Math.round`, `ceil`, `floor`?](#how-do-you-round-numbers-using-math.round-ceil-floor) | Intermediate |
| 115 | [How do you get the max/min value from an array?](#how-do-you-get-the-maxmin-value-from-an-array) | Intermediate |
| 116 | [How do you use the modulo operator `%`?](#how-do-you-use-the-modulo-operator-%) | Intermediate |
| 117 | [How do you check if a number is even or odd?](#how-do-you-check-if-a-number-is-even-or-odd) | Intermediate |
| 118 | [How do you use bitwise operators in JavaScript?](#how-do-you-use-bitwise-operators-in-javascript) | Intermediate |
| 119 | [How do you use `BigInt` for large integers?](#how-do-you-use-bigint-for-large-integers) | Intermediate |
| 120 | [How do you prevent default event behavior?](#how-do-you-prevent-default-event-behavior) | Intermediate |
| 121 | [How do you stop event propagation?](#how-do-you-stop-event-propagation) | Intermediate |
| 122 | [How do you check if an event target matches a selector?](#how-do-you-check-if-an-event-target-matches-a-selector) | Intermediate |
| 123 | [How do you get the mouse position in an event?](#how-do-you-get-the-mouse-position-in-an-event) | Intermediate |
| 124 | [How do you handle keyboard events?](#how-do-you-handle-keyboard-events) | Intermediate |
| 125 | [How do you detect which key was pressed?](#how-do-you-detect-which-key-was-pressed) | Intermediate |
| 126 | [How do you handle form submission?](#how-do-you-handle-form-submission) | Intermediate |
| 127 | [How do you access form values?](#how-do-you-access-form-values) | Intermediate |
| 128 | [How do you disable a button after click?](#how-do-you-disable-a-button-after-click) | Intermediate |
| 129 | [How do you toggle a class on an element?](#how-do-you-toggle-a-class-on-an-element) | Intermediate |
| 130 | [How do you get computed styles of an element?](#how-do-you-get-computed-styles-of-an-element) | Intermediate |
| 131 | [How do you get the size and position of an element (`getBoundingClientRect`)?](#how-do-you-get-the-size-and-position-of-an-element-getboundingclientrect) | Intermediate |
| 132 | [How do you scroll to a specific element?](#how-do-you-scroll-to-a-specific-element) | Intermediate |
| 133 | [How do you create elements dynamically?](#how-do-you-create-elements-dynamically) | Intermediate |
| 134 | [How do you insert elements at specific positions (`insertAdjacentHTML`)?](#how-do-you-insert-elements-at-specific-positions-insertadjacenthtml) | Intermediate |
| 135 | [How do you remove an element from the DOM?](#how-do-you-remove-an-element-from-the-dom) | Intermediate |
| 136 | [How do you replace an element in the DOM?](#how-do-you-replace-an-element-in-the-dom) | Intermediate |
| 137 | [How do you use `dataset` attributes?](#how-do-you-use-dataset-attributes) | Intermediate |
| 138 | [How do you set and get cookies in JavaScript?](#how-do-you-set-and-get-cookies-in-javascript) | Intermediate |
| 139 | [How do you use `sessionStorage`?](#how-do-you-use-sessionstorage) | Intermediate |
| 140 | [How do you use `localStorage`?](#how-do-you-use-localstorage) | Intermediate |
| 141 | [How do you clear storage?](#how-do-you-clear-storage) | Intermediate |
| 142 | [How do you listen for storage changes?](#how-do-you-listen-for-storage-changes) | Intermediate |
| 143 | [How do you use the History API (`pushState`, `replaceState`)?](#how-do-you-use-the-history-api-pushstate-replacestate) | Intermediate |
| 144 | [How do you handle browser back button?](#how-do-you-handle-browser-back-button) | Intermediate |
| 145 | [How do you reload the page using JavaScript?](#how-do-you-reload-the-page-using-javascript) | Intermediate |
| 146 | [How do you redirect to another page?](#how-do-you-redirect-to-another-page) | Intermediate |
| 147 | [How do you get the browser user agent?](#how-do-you-get-the-browser-user-agent) | Intermediate |
| 148 | [How do you check if cookies are enabled?](#how-do-you-check-if-cookies-are-enabled) | Intermediate |
| 149 | [How do you check if the browser supports a feature?](#how-do-you-check-if-the-browser-supports-a-feature) | Intermediate |
| 150 | [How do you use `typeof` operator?](#how-do-you-use-typeof-operator) | Intermediate |
| 151 | [How do you use `instanceof` operator?](#how-do-you-use-instanceof-operator) | Intermediate |
| 152 | [How do you use `void` operator?](#how-do-you-use-void-operator) | Intermediate |
| 153 | [How do you use the comma operator?](#how-do-you-use-the-comma-operator) | Intermediate |
| 154 | [How do you use the unary plus operator?](#how-do-you-use-the-unary-plus-operator) | Intermediate |
| 155 | [How do you use `!!` (double bang) to convert to boolean?](#how-do-you-use-!!-double-bang-to-convert-to-boolean) | Intermediate |
| 156 | [How do you use short-circuit evaluation (`&&`, `||`)?](#how-do-you-use-short-circuit-evaluation-&&-||) | Intermediate |
| 157 | [How do you use the nullish coalescing operator (`??`)?](#how-do-you-use-the-nullish-coalescing-operator-) | Intermediate |
| 158 | [How do you use the logical assignment operators (`&&=`, `||=`, `??=`)?](#how-do-you-use-the-logical-assignment-operators-&&=-||=-=) | Intermediate |

---

### 1. How do you implement a robust debounce function with immediate execution option?


**Strategy:**
A robust debounce function should:
1. Delay function execution until `wait` milliseconds have passed since the last invocation.
2. Support an `immediate` option to trigger the function on the leading edge instead of the trailing edge.
3. Preserve the `this` context and arguments.
4. Return a cancellation method to clear pending timers.

**Code Snippet:**

```javascript
function debounce(func, wait, immediate = false) {
  let timeout;

  const debounced = function(...args) {
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

  debounced.cancel = function() {
    clearTimeout(timeout);
    timeout = null;
  };

  return debounced;
}

// Usage
const handleResize = debounce((evt) => {
  console.log('Window resized:', evt);
}, 250);

window.addEventListener('resize', handleResize);

// Cleanup
// handleResize.cancel();
```
**[⬆ Back to Top](#table-of-contents)**

### 2. How do you deeply clone an object handling circular references and special types (Date, RegExp)?


**Strategy:**
While `JSON.parse(JSON.stringify(obj))` is common, it fails with Dates, functions, `undefined`, and circular references.
A robust solution uses recursion with a `WeakMap` to track visited objects (handling cycles) and handles specific constructors.
In modern environments, `structuredClone()` is the native solution.

**Code Snippet:**

```javascript
// Modern Native Approach
const original = { date: new Date(), items: [1, 2] };
const copyNative = structuredClone(original);

// Polyfill/Manual Implementation
function deepClone(obj, hash = new WeakMap()) {
  if (Object(obj) !== obj) return obj; // Primitive
  if (hash.has(obj)) return hash.get(obj); // Cyclic reference

  let result;
  
  // Handle specific types
  if (obj instanceof Date) result = new Date(obj);
  else if (obj instanceof RegExp) result = new RegExp(obj.source, obj.flags);
  else if (obj.constructor) result = new obj.constructor();
  else result = Object.create(null);

  hash.set(obj, result);

  if (obj instanceof Map) {
    Array.from(obj, ([key, val]) => result.set(key, deepClone(val, hash)));
  } else if (obj instanceof Set) {
    Array.from(obj, (val) => result.add(deepClone(val, hash)));
  } else {
    // Objects and Arrays
    Object.assign(result, ...Object.keys(obj).map(key => ({
      [key]: deepClone(obj[key], hash)
    })));
  }

  return result;
}
```
**[⬆ Back to Top](#table-of-contents)**

### 3. How do you implement a custom Promise.allSettled() polyfill?


**Strategy:**
`Promise.allSettled` waits for all promises to finish, regardless of whether they resolved or rejected.
We map each promise to a new promise that always resolves with an object describing the outcome (`{ status: 'fulfilled', value }` or `{ status: 'rejected', reason }`).

**Code Snippet:**

```javascript
if (!Promise.allSettled) {
  Promise.allSettled = function(promises) {
    return Promise.all(
      promises.map(p => 
        Promise.resolve(p)
          .then(value => ({
            status: 'fulfilled',
            value
          }))
          .catch(reason => ({
            status: 'rejected',
            reason
          }))
      )
    );
  };
}

// Usage
const p1 = Promise.resolve(42);
const p2 = Promise.reject('Error');

Promise.allSettled([p1, p2]).then(results => {
  console.log(results);
  // [
  //   { status: 'fulfilled', value: 42 },
  //   { status: 'rejected', reason: 'Error' }
  // ]
});
```
**[⬆ Back to Top](#table-of-contents)**

### 4. How do you create a private variable in JavaScript without using the '#' private field syntax?


**Strategy:**
Before ES2022 private fields (`#prop`), private variables were typically achieved using:
1. **Closures:** The most common pattern (Module pattern).
2. **WeakMap:** Associating private data with an instance without exposing it.
3. **Symbol:** pseudo-private (accessible via `Object.getOwnPropertySymbols`).

**Code Snippet (WeakMap Approach):**

```javascript
const privateData = new WeakMap();

class User {
  constructor(name, email) {
    privateData.set(this, {
      email: email,
      apiKey: 'secret_123'
    });
    this.name = name;
  }

  getEmail() {
    return privateData.get(this).email;
  }

  // apiKey is inaccessible directly
}

const user = new User('Alice', 'alice@example.com');
console.log(user.name); // Alice
console.log(user.getEmail()); // alice@example.com
// console.log(user.apiKey); // undefined
// console.log(privateData.get(user)); // Accessible if you have reference to privateData
```
**[⬆ Back to Top](#table-of-contents)**

### 5. How do you efficiently flatten a deeply nested array without using `Array.prototype.flat`?


**Strategy:**
We can use recursion or a stack-based iterative approach. The iterative approach is generally safer to avoid call stack overflow with very deep arrays.
Using a generator is also an elegant way to lazily flatten.

**Code Snippet (Generator Approach):**

```javascript
function* flatten(array) {
  for (const item of array) {
    if (Array.isArray(item)) {
      yield* flatten(item);
    } else {
      yield item;
    }
  }
}

const nested = [1, [2, [3, 4], 5], 6];
const flat = [...flatten(nested)];
console.log(flat); // [1, 2, 3, 4, 5, 6]

// Iterative Stack Approach (Faster for huge arrays)
function flattenIterative(arr) {
  const stack = [...arr];
  const res = [];
  while (stack.length) {
    const next = stack.pop();
    if (Array.isArray(next)) {
      stack.push(...next);
    } else {
      res.push(next);
    }
  }
  return res.reverse();
}
```
**[⬆ Back to Top](#table-of-contents)**

### 6. How do you implement function composition (pipe) from scratch?


**Strategy:**
Function composition combines multiple functions such that the output of one becomes the input of the next.
`pipe` executes left-to-right, while `compose` executes right-to-left.
We can use `Array.prototype.reduce` for this.

**Code Snippet:**

```javascript
const pipe = (...fns) => (initialValue) => 
  fns.reduce((acc, fn) => fn(acc), initialValue);

const compose = (...fns) => (initialValue) => 
  fns.reduceRight((acc, fn) => fn(acc), initialValue);

// Example functions
const add5 = x => x + 5;
const multiply2 = x => x * 2;
const toString = x => `Result: ${x}`;

// Execution order: add5 -> multiply2 -> toString
const process = pipe(add5, multiply2, toString);

console.log(process(10)); 
// (10 + 5) * 2 = 30 -> "Result: 30"
```
**[⬆ Back to Top](#table-of-contents)**

### 7. How do you use Proxy to implement a validation schema for an object?


**Strategy:**
A `Proxy` object allows you to intercept and customize operations performed on objects (like property lookup, assignment, etc.).
We can intercept the `set` trap to validate values before assignment.

**Code Snippet:**

```javascript
const validator = {
  set: function(obj, prop, value) {
    if (prop === 'age') {
      if (!Number.isInteger(value)) {
        throw new TypeError('Age must be an integer');
      }
      if (value < 0 || value > 120) {
        throw new RangeError('Age must be between 0 and 120');
      }
    }
    
    // Default behavior: store the value
    obj[prop] = value;
    return true; // Indicate success
  }
};

const person = new Proxy({}, validator);

person.age = 25; // OK
console.log(person.age); // 25

try {
  person.age = 'old'; // Throws TypeError
} catch (e) {
  console.error(e.message);
}
```
**[⬆ Back to Top](#table-of-contents)**

### 8. How do you implement an event emitter (Pub/Sub pattern) from scratch?


**Strategy:**
The Publish-Subscribe pattern allows loose coupling between components.
We need a structure to store listeners (callbacks) for each event name, and methods to `on` (subscribe), `off` (unsubscribe), and `emit` (publish).

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
    
    // Return unsubscribe function for convenience
    return () => this.off(event, listener);
  }

  off(event, listener) {
    if (!this.events[event]) return;
    this.events[event] = this.events[event].filter(l => l !== listener);
  }

  emit(event, ...args) {
    if (!this.events[event]) return;
    this.events[event].forEach(listener => {
      listener(...args);
    });
  }
  
  once(event, listener) {
    const remove = this.on(event, (...args) => {
      remove();
      listener(...args);
    });
  }
}

// Usage
const bus = new EventEmitter();
const logData = (data) => console.log('Received:', data);

bus.on('data', logData);
bus.emit('data', { id: 1 }); // Received: { id: 1 }
bus.off('data', logData);
```
**[⬆ Back to Top](#table-of-contents)**

### 9. How do you throttle a function to ensure it runs at most once every X milliseconds?


**Strategy:**
Throttling ensures a function is called at most once in a specified time period.
It differs from debouncing (which waits for a pause).
We need to track the last execution time.

**Code Snippet:**

```javascript
function throttle(func, limit) {
  let inThrottle;
  
  return function(...args) {
    const context = this;
    
    if (!inThrottle) {
      func.apply(context, args);
      inThrottle = true;
      
      setTimeout(() => {
        inThrottle = false;
      }, limit);
    }
  };
}

// Usage (e.g., scroll handler)
const logScroll = throttle(() => {
  console.log('Scroll event fired');
}, 1000);

window.addEventListener('scroll', logScroll);
```
**[⬆ Back to Top](#table-of-contents)**

### 10. How do you implement a memoization function to cache expensive calculation results?


**Strategy:**
Memoization caches the result of a function call based on its arguments.
If the function is called again with the same arguments, the cached result is returned.
We can use a `Map` or object to store the cache, using a stringified version of arguments as the key.

**Code Snippet:**

```javascript
function memoize(fn) {
  const cache = new Map();
  
  return function(...args) {
    // Create a unique key for arguments
    // Note: JSON.stringify works for simple args, but has limits with objects/functions
    const key = JSON.stringify(args);
    
    if (cache.has(key)) {
      console.log('Fetching from cache:', key);
      return cache.get(key);
    }
    
    const result = fn.apply(this, args);
    cache.set(key, result);
    return result;
  };
}

// Usage
const factorial = memoize((n) => {
  if (n <= 1) return 1;
  return n * factorial(n - 1); // Note: recursive calls won't use memoized version unless wrapper is used recursively
});

console.log(factorial(5)); // Calculates
console.log(factorial(5)); // Returns cached
```
**[⬆ Back to Top](#table-of-contents)**

### 11. How do you parallelize async tasks with a concurrency limit?


**Strategy:**
Sometimes `Promise.all` is too aggressive if you have thousands of requests.
We need a way to run a maximum of `N` tasks at a time. When one finishes, the next one starts.

**Code Snippet:**

```javascript
async function asyncPool(poolLimit, array, iteratorFn) {
  const ret = [];
  const executing = [];
  
  for (const item of array) {
    // Create promise
    const p = Promise.resolve().then(() => iteratorFn(item));
    ret.push(p);

    if (poolLimit <= array.length) {
      const e = p.then(() => executing.splice(executing.indexOf(e), 1));
      executing.push(e);
      
      if (executing.length >= poolLimit) {
        // Wait for the fastest one to finish
        await Promise.race(executing);
      }
    }
  }
  
  return Promise.all(ret);
}

// Usage
const urls = [/* 100 urls */];
const download = url => fetch(url).then(r => r.blob());

// Download max 5 at a time
// await asyncPool(5, urls, download);
```
**[⬆ Back to Top](#table-of-contents)**

### 12. How do you implement a custom `instanceof` operator?


**Strategy:**
The `instanceof` operator checks if the `prototype` property of a constructor appears anywhere in the prototype chain of an object.
We can traverse the prototype chain using `Object.getPrototypeOf()`.

**Code Snippet:**

```javascript
function myInstanceOf(obj, constructor) {
  // Primitives are not instances
  if (obj === null || typeof obj !== 'object') return false;
  
  let proto = Object.getPrototypeOf(obj);
  
  while (proto) {
    if (proto === constructor.prototype) {
      return true;
    }
    proto = Object.getPrototypeOf(proto);
  }
  
  return false;
}

// Usage
class Animal {}
class Dog extends Animal {}
const d = new Dog();

console.log(myInstanceOf(d, Dog));    // true
console.log(myInstanceOf(d, Animal)); // true
console.log(myInstanceOf(d, Array));  // false
```
**[⬆ Back to Top](#table-of-contents)**

### 13. How do you handle error boundaries in vanilla JavaScript (similar to React)?


**Strategy:**
In vanilla JS, global error handling is done via `window.onerror` or `window.addEventListener('error')`.
For unhandled promise rejections, use `unhandledrejection` event.
This acts as a global safety net.

**Code Snippet:**

```javascript
// Synchronous errors & DOM errors
window.addEventListener('error', (event) => {
  console.error('Global Error Caught:', event.message);
  // Prevent default browser error console logging
  // event.preventDefault();
  
  // Log to monitoring service
  // logError(event.error);
});

// Async Promise rejections
window.addEventListener('unhandledrejection', (event) => {
  console.error('Unhandled Promise Rejection:', event.reason);
  // event.preventDefault();
});

// Test
// setTimeout(() => { throw new Error('Oops'); }, 1000);
// Promise.reject('Failed request');
```
**[⬆ Back to Top](#table-of-contents)**

### 14. How do you implement currying to transform a function?


**Strategy:**
Currying transforms a function `f(a, b, c)` into `f(a)(b)(c)`.
It allows for partial application of arguments.
We implement this by checking if we have received enough arguments (`func.length`).

**Code Snippet:**

```javascript
function curry(func) {
  return function curried(...args) {
    if (args.length >= func.length) {
      // We have enough arguments, execute function
      return func.apply(this, args);
    } else {
      // Not enough arguments, return new function waiting for rest
      return function(...nextArgs) {
        return curried.apply(this, args.concat(nextArgs));
      };
    }
  };
}

// Usage
function sum(a, b, c) {
  return a + b + c;
}

const curriedSum = curry(sum);

console.log(curriedSum(1)(2)(3)); // 6
console.log(curriedSum(1, 2)(3)); // 6
console.log(curriedSum(1)(2, 3)); // 6
```
**[⬆ Back to Top](#table-of-contents)**

### 15. How do you safely access deeply nested properties (Optional Chaining polyfill)?


**Strategy:**
Before ES2020 `?.` operator, accessing `user.address.street` would throw if `address` was undefined.
We can use a utility function to safely traverse the path.

**Code Snippet:**

```javascript
// Modern Syntax
// const street = user?.address?.street;

// Functional Approach
const get = (obj, path, defaultValue) => {
  const keys = path.split('.');
  let result = obj;
  
  for (const key of keys) {
    if (result === null || result === undefined) {
      return defaultValue;
    }
    result = result[key];
  }
  
  return result === undefined ? defaultValue : result;
};

// Usage
const user = { profile: { name: 'John' } };
console.log(get(user, 'profile.name')); // 'John'
console.log(get(user, 'profile.address.city', 'Unknown')); // 'Unknown'
```
**[⬆ Back to Top](#table-of-contents)**

### 16. How do you implement a custom Iterable using Symbol.iterator?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you implement a custom Iterable using Symbol.iterator?
```

**[⬆ Back to Top](#table-of-contents)**

### 17. How do you use Generators for asynchronous flow control (co-routine pattern)?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use Generators for asynchronous flow control (co-routine pattern)?
```

**[⬆ Back to Top](#table-of-contents)**

### 18. How do you detect and fix memory leaks in JavaScript applications?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you detect and fix memory leaks in JavaScript applications?
```

**[⬆ Back to Top](#table-of-contents)**

### 19. How do you optimize large array processing using Web Workers?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you optimize large array processing using Web Workers?
```

**[⬆ Back to Top](#table-of-contents)**

### 20. How do you implement a basic Observable pattern?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you implement a basic Observable pattern?
```

**[⬆ Back to Top](#table-of-contents)**

### 21. How do you use the IntersectionObserver API for lazy loading images?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use the IntersectionObserver API for lazy loading images?
```

**[⬆ Back to Top](#table-of-contents)**

### 22. How do you use the MutationObserver API to track DOM changes?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use the MutationObserver API to track DOM changes?
```

**[⬆ Back to Top](#table-of-contents)**

### 23. How do you implement a sticky header using pure JavaScript?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you implement a sticky header using pure JavaScript?
```

**[⬆ Back to Top](#table-of-contents)**

### 24. How do you validate email using regex correctly?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you validate email using regex correctly?
```

**[⬆ Back to Top](#table-of-contents)**

### 25. How do you format numbers as currency using Intl.NumberFormat?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you format numbers as currency using Intl.NumberFormat?
```

**[⬆ Back to Top](#table-of-contents)**

### 26. How do you format dates using Intl.DateTimeFormat?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you format dates using Intl.DateTimeFormat?
```

**[⬆ Back to Top](#table-of-contents)**

### 27. How do you implement drag and drop using the HTML5 Drag and Drop API?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you implement drag and drop using the HTML5 Drag and Drop API?
```

**[⬆ Back to Top](#table-of-contents)**

### 28. How do you read files using the FileReader API?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you read files using the FileReader API?
```

**[⬆ Back to Top](#table-of-contents)**

### 29. How do you use the Clipboard API to copy text to clipboard?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use the Clipboard API to copy text to clipboard?
```

**[⬆ Back to Top](#table-of-contents)**

### 30. How do you detect network status changes (online/offline)?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you detect network status changes (online/offline)?
```

**[⬆ Back to Top](#table-of-contents)**

### 31. How do you use the Geolocation API to get user position?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use the Geolocation API to get user position?
```

**[⬆ Back to Top](#table-of-contents)**

### 32. How do you implement a virtual list (windowing) for large datasets?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you implement a virtual list (windowing) for large datasets?
```

**[⬆ Back to Top](#table-of-contents)**

### 33. How do you optimize event listeners using event delegation?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you optimize event listeners using event delegation?
```

**[⬆ Back to Top](#table-of-contents)**

### 34. How do you prevent prototype pollution attacks?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you prevent prototype pollution attacks?
```

**[⬆ Back to Top](#table-of-contents)**

### 35. How do you securely store tokens in the browser (HttpOnly vs LocalStorage)?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you securely store tokens in the browser (HttpOnly vs LocalStorage)?
```

**[⬆ Back to Top](#table-of-contents)**

### 36. How do you implement CSRF protection in AJAX requests?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you implement CSRF protection in AJAX requests?
```

**[⬆ Back to Top](#table-of-contents)**

### 37. How do you sanitize user input to prevent XSS?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you sanitize user input to prevent XSS?
```

**[⬆ Back to Top](#table-of-contents)**

### 38. How do you use the BroadcastChannel API for tab communication?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use the BroadcastChannel API for tab communication?
```

**[⬆ Back to Top](#table-of-contents)**

### 39. How do you use SharedWorkers for shared state between tabs?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use SharedWorkers for shared state between tabs?
```

**[⬆ Back to Top](#table-of-contents)**

### 40. How do you implement a simple state management system (like Redux) from scratch?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you implement a simple state management system (like Redux) from scratch?
```

**[⬆ Back to Top](#table-of-contents)**

### 41. How do you implement a router from scratch (Hash vs History API)?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you implement a router from scratch (Hash vs History API)?
```

**[⬆ Back to Top](#table-of-contents)**

### 42. How do you parse query string parameters without a library?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you parse query string parameters without a library?
```

**[⬆ Back to Top](#table-of-contents)**

### 43. How do you implement a dark mode toggle using CSS variables and JS?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you implement a dark mode toggle using CSS variables and JS?
```

**[⬆ Back to Top](#table-of-contents)**

### 44. How do you detect if an element is visible in the viewport?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you detect if an element is visible in the viewport?
```

**[⬆ Back to Top](#table-of-contents)**

### 45. How do you implement infinite scrolling using JavaScript?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you implement infinite scrolling using JavaScript?
```

**[⬆ Back to Top](#table-of-contents)**

### 46. How do you sort an array of objects by multiple keys?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you sort an array of objects by multiple keys?
```

**[⬆ Back to Top](#table-of-contents)**

### 47. How do you remove duplicates from an array of objects?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you remove duplicates from an array of objects?
```

**[⬆ Back to Top](#table-of-contents)**

### 48. How do you find the intersection of two arrays?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you find the intersection of two arrays?
```

**[⬆ Back to Top](#table-of-contents)**

### 49. How do you shuffle an array (Fisher-Yates algorithm)?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you shuffle an array (Fisher-Yates algorithm)?
```

**[⬆ Back to Top](#table-of-contents)**

### 50. How do you generate a random UUID in JavaScript?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you generate a random UUID in JavaScript?
```

**[⬆ Back to Top](#table-of-contents)**

### 51. How do you convert RGB to Hex using JavaScript?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you convert RGB to Hex using JavaScript?
```

**[⬆ Back to Top](#table-of-contents)**

### 52. How do you detect mobile devices using JavaScript?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you detect mobile devices using JavaScript?
```

**[⬆ Back to Top](#table-of-contents)**

### 53. How do you disable right-click context menu?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you disable right-click context menu?
```

**[⬆ Back to Top](#table-of-contents)**

### 54. How do you copy text to clipboard without the Clipboard API (fallback)?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you copy text to clipboard without the Clipboard API (fallback)?
```

**[⬆ Back to Top](#table-of-contents)**

### 55. How do you trigger a file download programmatically?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you trigger a file download programmatically?
```

**[⬆ Back to Top](#table-of-contents)**

### 56. How do you use `requestAnimationFrame` for smooth animations?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use `requestAnimationFrame` for smooth animations?
```

**[⬆ Back to Top](#table-of-contents)**

### 57. How do you measure performance using `performance.now()`?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you measure performance using `performance.now()`?
```

**[⬆ Back to Top](#table-of-contents)**

### 58. How do you use `console.time` and `console.timeEnd` for debugging?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use `console.time` and `console.timeEnd` for debugging?
```

**[⬆ Back to Top](#table-of-contents)**

### 59. How do you debug memory leaks using Chrome DevTools?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you debug memory leaks using Chrome DevTools?
```

**[⬆ Back to Top](#table-of-contents)**

### 60. How do you use the `debugger` statement effectively?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use the `debugger` statement effectively?
```

**[⬆ Back to Top](#table-of-contents)**

### 61. How do you implement a simple template engine?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you implement a simple template engine?
```

**[⬆ Back to Top](#table-of-contents)**

### 62. How do you parse JSON safely without throwing errors?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you parse JSON safely without throwing errors?
```

**[⬆ Back to Top](#table-of-contents)**

### 63. How do you stringify objects with circular references?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you stringify objects with circular references?
```

**[⬆ Back to Top](#table-of-contents)**

### 64. How do you check if two objects are deeply equal?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you check if two objects are deeply equal?
```

**[⬆ Back to Top](#table-of-contents)**

### 65. How do you get unique values from an array using Set?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you get unique values from an array using Set?
```

**[⬆ Back to Top](#table-of-contents)**

### 66. How do you merge two objects deeply?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you merge two objects deeply?
```

**[⬆ Back to Top](#table-of-contents)**

### 67. How do you implement a `sleep` or `delay` function using Promises?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you implement a `sleep` or `delay` function using Promises?
```

**[⬆ Back to Top](#table-of-contents)**

### 68. How do you cancel a fetch request using AbortController?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you cancel a fetch request using AbortController?
```

**[⬆ Back to Top](#table-of-contents)**

### 69. How do you set a timeout for a fetch request?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you set a timeout for a fetch request?
```

**[⬆ Back to Top](#table-of-contents)**

### 70. How do you retry a failed API call with exponential backoff?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you retry a failed API call with exponential backoff?
```

**[⬆ Back to Top](#table-of-contents)**

### 71. How do you upload files using `FormData`?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you upload files using `FormData`?
```

**[⬆ Back to Top](#table-of-contents)**

### 72. How do you send JSON data using `fetch`?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you send JSON data using `fetch`?
```

**[⬆ Back to Top](#table-of-contents)**

### 73. How do you handle HTTP errors in `fetch` (since it doesn't reject on 4xx/5xx)?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you handle HTTP errors in `fetch` (since it doesn't reject on 4xx/5xx)?
```

**[⬆ Back to Top](#table-of-contents)**

### 74. How do you use `navigator.sendBeacon` for analytics?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use `navigator.sendBeacon` for analytics?
```

**[⬆ Back to Top](#table-of-contents)**

### 75. How do you preload images using JavaScript?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you preload images using JavaScript?
```

**[⬆ Back to Top](#table-of-contents)**

### 76. How do you check if a variable is an array?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you check if a variable is an array?
```

**[⬆ Back to Top](#table-of-contents)**

### 77. How do you check if a variable is a number (and not NaN)?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you check if a variable is a number (and not NaN)?
```

**[⬆ Back to Top](#table-of-contents)**

### 78. How do you convert a NodeList to an Array?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you convert a NodeList to an Array?
```

**[⬆ Back to Top](#table-of-contents)**

### 79. How do you get the last element of an array?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you get the last element of an array?
```

**[⬆ Back to Top](#table-of-contents)**

### 80. How do you clear an array efficiently?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you clear an array efficiently?
```

**[⬆ Back to Top](#table-of-contents)**

### 81. How do you loop over an object's properties?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you loop over an object's properties?
```

**[⬆ Back to Top](#table-of-contents)**

### 82. How do you use `Object.entries()` and `Object.fromEntries()`?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use `Object.entries()` and `Object.fromEntries()`?
```

**[⬆ Back to Top](#table-of-contents)**

### 83. How do you freeze an object to prevent modifications?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you freeze an object to prevent modifications?
```

**[⬆ Back to Top](#table-of-contents)**

### 84. How do you seal an object?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you seal an object?
```

**[⬆ Back to Top](#table-of-contents)**

### 85. How do you use `Object.create()` for inheritance?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use `Object.create()` for inheritance?
```

**[⬆ Back to Top](#table-of-contents)**

### 86. How do you implement a mixin in JavaScript?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you implement a mixin in JavaScript?
```

**[⬆ Back to Top](#table-of-contents)**

### 87. How do you use factory functions vs classes?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use factory functions vs classes?
```

**[⬆ Back to Top](#table-of-contents)**

### 88. How do you use private class fields (#)?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use private class fields (#)?
```

**[⬆ Back to Top](#table-of-contents)**

### 89. How do you use static class methods?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use static class methods?
```

**[⬆ Back to Top](#table-of-contents)**

### 90. How do you implement a Singleton using a closure?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you implement a Singleton using a closure?
```

**[⬆ Back to Top](#table-of-contents)**

### 91. How do you use default parameters in functions?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use default parameters in functions?
```

**[⬆ Back to Top](#table-of-contents)**

### 92. How do you use the rest operator `...`?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use the rest operator `...`?
```

**[⬆ Back to Top](#table-of-contents)**

### 93. How do you use the spread operator `...`?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use the spread operator `...`?
```

**[⬆ Back to Top](#table-of-contents)**

### 94. How do you destructure nested objects?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you destructure nested objects?
```

**[⬆ Back to Top](#table-of-contents)**

### 95. How do you swap variables using destructuring?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you swap variables using destructuring?
```

**[⬆ Back to Top](#table-of-contents)**

### 96. How do you use template literals for multiline strings?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use template literals for multiline strings?
```

**[⬆ Back to Top](#table-of-contents)**

### 97. How do you use tagged template literals?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use tagged template literals?
```

**[⬆ Back to Top](#table-of-contents)**

### 98. How do you use `String.prototype.includes()` vs `indexOf()`?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use `String.prototype.includes()` vs `indexOf()`?
```

**[⬆ Back to Top](#table-of-contents)**

### 99. How do you pad a string using `padStart` and `padEnd`?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you pad a string using `padStart` and `padEnd`?
```

**[⬆ Back to Top](#table-of-contents)**

### 100. How do you trim strings using `trim`, `trimStart`, `trimEnd`?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you trim strings using `trim`, `trimStart`, `trimEnd`?
```

**[⬆ Back to Top](#table-of-contents)**

### 101. How do you replace all occurrences of a string using `replaceAll`?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you replace all occurrences of a string using `replaceAll`?
```

**[⬆ Back to Top](#table-of-contents)**

### 102. How do you use `Array.prototype.map()`?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use `Array.prototype.map()`?
```

**[⬆ Back to Top](#table-of-contents)**

### 103. How do you use `Array.prototype.filter()`?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use `Array.prototype.filter()`?
```

**[⬆ Back to Top](#table-of-contents)**

### 104. How do you use `Array.prototype.reduce()`?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use `Array.prototype.reduce()`?
```

**[⬆ Back to Top](#table-of-contents)**

### 105. How do you use `Array.prototype.find()` and `findIndex()`?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use `Array.prototype.find()` and `findIndex()`?
```

**[⬆ Back to Top](#table-of-contents)**

### 106. How do you use `Array.prototype.some()` and `every()`?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use `Array.prototype.some()` and `every()`?
```

**[⬆ Back to Top](#table-of-contents)**

### 107. How do you use `Array.prototype.flat()` and `flatMap()`?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use `Array.prototype.flat()` and `flatMap()`?
```

**[⬆ Back to Top](#table-of-contents)**

### 108. How do you sort numbers correctly (since default sort is lexicographical)?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you sort numbers correctly (since default sort is lexicographical)?
```

**[⬆ Back to Top](#table-of-contents)**

### 109. How do you create an array of a specific length filled with a value?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you create an array of a specific length filled with a value?
```

**[⬆ Back to Top](#table-of-contents)**

### 110. How do you get query parameters from a URL object?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you get query parameters from a URL object?
```

**[⬆ Back to Top](#table-of-contents)**

### 111. How do you use `URLSearchParams`?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use `URLSearchParams`?
```

**[⬆ Back to Top](#table-of-contents)**

### 112. How do you encode and decode URLs (`encodeURIComponent`)?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you encode and decode URLs (`encodeURIComponent`)?
```

**[⬆ Back to Top](#table-of-contents)**

### 113. How do you use `Math.random()` effectively?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use `Math.random()` effectively?
```

**[⬆ Back to Top](#table-of-contents)**

### 114. How do you round numbers using `Math.round`, `ceil`, `floor`?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you round numbers using `Math.round`, `ceil`, `floor`?
```

**[⬆ Back to Top](#table-of-contents)**

### 115. How do you get the max/min value from an array?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you get the max/min value from an array?
```

**[⬆ Back to Top](#table-of-contents)**

### 116. How do you use the modulo operator `%`?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use the modulo operator `%`?
```

**[⬆ Back to Top](#table-of-contents)**

### 117. How do you check if a number is even or odd?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you check if a number is even or odd?
```

**[⬆ Back to Top](#table-of-contents)**

### 118. How do you use bitwise operators in JavaScript?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use bitwise operators in JavaScript?
```

**[⬆ Back to Top](#table-of-contents)**

### 119. How do you use `BigInt` for large integers?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use `BigInt` for large integers?
```

**[⬆ Back to Top](#table-of-contents)**

### 120. How do you prevent default event behavior?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you prevent default event behavior?
```

**[⬆ Back to Top](#table-of-contents)**

### 121. How do you stop event propagation?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you stop event propagation?
```

**[⬆ Back to Top](#table-of-contents)**

### 122. How do you check if an event target matches a selector?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you check if an event target matches a selector?
```

**[⬆ Back to Top](#table-of-contents)**

### 123. How do you get the mouse position in an event?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you get the mouse position in an event?
```

**[⬆ Back to Top](#table-of-contents)**

### 124. How do you handle keyboard events?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you handle keyboard events?
```

**[⬆ Back to Top](#table-of-contents)**

### 125. How do you detect which key was pressed?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you detect which key was pressed?
```

**[⬆ Back to Top](#table-of-contents)**

### 126. How do you handle form submission?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you handle form submission?
```

**[⬆ Back to Top](#table-of-contents)**

### 127. How do you access form values?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you access form values?
```

**[⬆ Back to Top](#table-of-contents)**

### 128. How do you disable a button after click?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you disable a button after click?
```

**[⬆ Back to Top](#table-of-contents)**

### 129. How do you toggle a class on an element?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you toggle a class on an element?
```

**[⬆ Back to Top](#table-of-contents)**

### 130. How do you get computed styles of an element?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you get computed styles of an element?
```

**[⬆ Back to Top](#table-of-contents)**

### 131. How do you get the size and position of an element (`getBoundingClientRect`)?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you get the size and position of an element (`getBoundingClientRect`)?
```

**[⬆ Back to Top](#table-of-contents)**

### 132. How do you scroll to a specific element?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you scroll to a specific element?
```

**[⬆ Back to Top](#table-of-contents)**

### 133. How do you create elements dynamically?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you create elements dynamically?
```

**[⬆ Back to Top](#table-of-contents)**

### 134. How do you insert elements at specific positions (`insertAdjacentHTML`)?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you insert elements at specific positions (`insertAdjacentHTML`)?
```

**[⬆ Back to Top](#table-of-contents)**

### 135. How do you remove an element from the DOM?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you remove an element from the DOM?
```

**[⬆ Back to Top](#table-of-contents)**

### 136. How do you replace an element in the DOM?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you replace an element in the DOM?
```

**[⬆ Back to Top](#table-of-contents)**

### 137. How do you use `dataset` attributes?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use `dataset` attributes?
```

**[⬆ Back to Top](#table-of-contents)**

### 138. How do you set and get cookies in JavaScript?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you set and get cookies in JavaScript?
```

**[⬆ Back to Top](#table-of-contents)**

### 139. How do you use `sessionStorage`?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use `sessionStorage`?
```

**[⬆ Back to Top](#table-of-contents)**

### 140. How do you use `localStorage`?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use `localStorage`?
```

**[⬆ Back to Top](#table-of-contents)**

### 141. How do you clear storage?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you clear storage?
```

**[⬆ Back to Top](#table-of-contents)**

### 142. How do you listen for storage changes?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you listen for storage changes?
```

**[⬆ Back to Top](#table-of-contents)**

### 143. How do you use the History API (`pushState`, `replaceState`)?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use the History API (`pushState`, `replaceState`)?
```

**[⬆ Back to Top](#table-of-contents)**

### 144. How do you handle browser back button?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you handle browser back button?
```

**[⬆ Back to Top](#table-of-contents)**

### 145. How do you reload the page using JavaScript?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you reload the page using JavaScript?
```

**[⬆ Back to Top](#table-of-contents)**

### 146. How do you redirect to another page?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you redirect to another page?
```

**[⬆ Back to Top](#table-of-contents)**

### 147. How do you get the browser user agent?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you get the browser user agent?
```

**[⬆ Back to Top](#table-of-contents)**

### 148. How do you check if cookies are enabled?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you check if cookies are enabled?
```

**[⬆ Back to Top](#table-of-contents)**

### 149. How do you check if the browser supports a feature?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you check if the browser supports a feature?
```

**[⬆ Back to Top](#table-of-contents)**

### 150. How do you use `typeof` operator?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use `typeof` operator?
```

**[⬆ Back to Top](#table-of-contents)**

### 151. How do you use `instanceof` operator?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use `instanceof` operator?
```

**[⬆ Back to Top](#table-of-contents)**

### 152. How do you use `void` operator?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use `void` operator?
```

**[⬆ Back to Top](#table-of-contents)**

### 153. How do you use the comma operator?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use the comma operator?
```

**[⬆ Back to Top](#table-of-contents)**

### 154. How do you use the unary plus operator?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use the unary plus operator?
```

**[⬆ Back to Top](#table-of-contents)**

### 155. How do you use `!!` (double bang) to convert to boolean?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use `!!` (double bang) to convert to boolean?
```

**[⬆ Back to Top](#table-of-contents)**

### 156. How do you use short-circuit evaluation (`&&`, `||`)?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use short-circuit evaluation (`&&`, `||`)?
```

**[⬆ Back to Top](#table-of-contents)**

### 157. How do you use the nullish coalescing operator (`??`)?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use the nullish coalescing operator (`??`)?
```

**[⬆ Back to Top](#table-of-contents)**

### 158. How do you use the logical assignment operators (`&&=`, `||=`, `??=`)?

**Answer:**

This is a practical question that requires understanding of JavaScript fundamentals.

```javascript
// Implementation example
// How do you use the logical assignment operators (`&&=`, `||=`, `??=`)?
```

**[⬆ Back to Top](#table-of-contents)**

