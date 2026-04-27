<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>Testing (Jest/Mocha) Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for developers</b></p>
</div>

---

## Table of Contents

1. [How do you mock a module in Jest?](#q1) <span class="beginner">Beginner</span>
2. [What is Snapshot Testing in Jest?](#q2) <span class="beginner">Beginner</span>
3. [How do you test asynchronous code in Jest?](#q3) <span class="intermediate">Intermediate</span>
4. [Difference between `shallow` and `mount` in Enzyme?](#q4) <span class="intermediate">Intermediate</span>
5. [How do you spy on a method with Jest?](#q5) <span class="intermediate">Intermediate</span>
6. [How do you setup and teardown tests in Mocha?](#q6) <span class="beginner">Beginner</span>
7. [How do you mock a timer in Jest?](#q7) <span class="advanced">Advanced</span>
8. [How do you test a React Hook?](#q8) <span class="advanced">Advanced</span>
9. [How do you mock a default export in Jest?](#q9) <span class="advanced">Advanced</span>
10. [How do you test for an exception in Jest?](#q10) <span class="beginner">Beginner</span>
11. [What is the difference between `describe` and `test`?](#q11) <span class="beginner">Beginner</span>
12. [How do you access the DOM in Jest?](#q12) <span class="intermediate">Intermediate</span>
13. [What is `jest.fn()`?](#q13) <span class="beginner">Beginner</span>
14. [How do you skip a test?](#q14) <span class="beginner">Beginner</span>
15. [How do you run only one test?](#q15) <span class="beginner">Beginner</span>
16. [How do you test React components without Enzyme?](#q16) <span class="intermediate">Intermediate</span>
17. [How do you mock global objects like `localStorage`?](#q17) <span class="intermediate">Intermediate</span>
18. [What is Code Coverage?](#q18) <span class="intermediate">Intermediate</span>
19. [How do you parameterize tests in Jest?](#q19) <span class="intermediate">Intermediate</span>
20. [How do you reset mocks between tests?](#q20) <span class="intermediate">Intermediate</span>
21. [What is a Spy in testing?](#q21) <span class="beginner">Beginner</span>
22. [How do you test Redux connected components?](#q22) <span class="advanced">Advanced</span>
23. [What is TDD?](#q23) <span class="beginner">Beginner</span>
24. [What is BDD?](#q24) <span class="beginner">Beginner</span>
25. [Difference between Unit and Integration tests?](#q25) <span class="beginner">Beginner</span>
26. [What is E2E testing?](#q26) <span class="beginner">Beginner</span>
27. [What is Jest?](#q27) <span class="beginner">Beginner</span>
28. [What is Mocha?](#q28) <span class="beginner">Beginner</span>
29. [What is Chai?](#q29) <span class="beginner">Beginner</span>
30. [What is Enzyme?](#q30) <span class="intermediate">Intermediate</span>
31. [What is React Testing Library (RTL)?](#q31) <span class="intermediate">Intermediate</span>
32. [How do you mock a function?](#q32) <span class="beginner">Beginner</span>
33. [How do you mock a module?](#q33) <span class="intermediate">Intermediate</span>
34. [What is Snapshot testing?](#q34) <span class="beginner">Beginner</span>
35. [How do you update snapshots?](#q35) <span class="beginner">Beginner</span>
36. [What is `beforeAll`?](#q36) <span class="beginner">Beginner</span>
37. [What is `afterEach`?](#q37) <span class="beginner">Beginner</span>
38. [How do you test async code?](#q38) <span class="intermediate">Intermediate</span>
39. [How do you mock timers?](#q39) <span class="advanced">Advanced</span>
40. [What is `spyOn`?](#q40) <span class="intermediate">Intermediate</span>
41. [How do you mock API calls?](#q41) <span class="intermediate">Intermediate</span>
42. [What is Coverage?](#q42) <span class="beginner">Beginner</span>
43. [How do you test hooks?](#q43) <span class="advanced">Advanced</span>
44. [How do you test context?](#q44) <span class="intermediate">Intermediate</span>
45. [What is `act`?](#q45) <span class="advanced">Advanced</span>
46. [How do you find elements in RTL?](#q46) <span class="beginner">Beginner</span>
47. [Difference between `getBy` and `queryBy`?](#q47) <span class="intermediate">Intermediate</span>
48. [Difference between `getBy` and `findBy`?](#q48) <span class="intermediate">Intermediate</span>
49. [How do you simulate events?](#q49) <span class="beginner">Beginner</span>
50. [What is `user-event`?](#q50) <span class="intermediate">Intermediate</span>
51. [How do you debug tests?](#q51) <span class="beginner">Beginner</span>
52. [How do you skip a test?](#q52) <span class="beginner">Beginner</span>
53. [How do you focus a test?](#q53) <span class="beginner">Beginner</span>
54. [What is `describe`?](#q54) <span class="beginner">Beginner</span>
55. [How do you mock local storage?](#q55) <span class="intermediate">Intermediate</span>
56. [How do you test routing?](#q56) <span class="intermediate">Intermediate</span>
57. [What is Cypress?](#q57) <span class="intermediate">Intermediate</span>
58. [What is Playwright?](#q58) <span class="intermediate">Intermediate</span>
59. [Difference between Mock and Stub?](#q59) <span class="advanced">Advanced</span>
60. [What is Mutation Testing?](#q60) <span class="advanced">Advanced</span>
61. [How do you test accessibility?](#q61) <span class="intermediate">Intermediate</span>
62. [What is Visual Regression Testing?](#q62) <span class="advanced">Advanced</span>
63. [How do you test Redux?](#q63) <span class="intermediate">Intermediate</span>
64. [How do you mock Date?](#q64) <span class="intermediate">Intermediate</span>
65. [What is `cleanup`?](#q65) <span class="intermediate">Intermediate</span>
66. [How do you test portals?](#q66) <span class="advanced">Advanced</span>
67. [What is Property Based Testing?](#q67) <span class="advanced">Advanced</span>
68. [How do you setup global config?](#q68) <span class="intermediate">Intermediate</span>
69. [What is the Pyramid of Testing?](#q69) <span class="beginner">Beginner</span>
70. [How do you test strict mode?](#q70) <span class="intermediate">Intermediate</span>
71. [How do you test error boundaries?](#q71) <span class="advanced">Advanced</span>
72. [What is shallow rendering?](#q72) <span class="intermediate">Intermediate</span>
73. [Why prefer full rendering?](#q73) <span class="intermediate">Intermediate</span>
74. [How do you test observables?](#q74) <span class="advanced">Advanced</span>
75. [What is CI/CD testing?](#q75) <span class="intermediate">Intermediate</span>
76. [How do you parallelize tests?](#q76) <span class="intermediate">Intermediate</span>
77. [What is Flaky test?](#q77) <span class="beginner">Beginner</span>
78. [How do you fix flaky tests?](#q78) <span class="intermediate">Intermediate</span>
79. [What is Contract Testing?](#q79) <span class="advanced">Advanced</span>
80. [How do you test WebSockets?](#q80) <span class="advanced">Advanced</span>
81. [How do you test Service Workers?](#q81) <span class="advanced">Advanced</span>
82. [What is `test.todo`?](#q82) <span class="beginner">Beginner</span>
83. [How do you mock a module partially?](#q83) <span class="intermediate">Intermediate</span>
84. [What is `__mocks__` folder?](#q84) <span class="intermediate">Intermediate</span>
85. [How do you test memory leaks?](#q85) <span class="advanced">Advanced</span>
86. [What is Static Analysis?](#q86) <span class="beginner">Beginner</span>
87. [How do you test Canvas?](#q87) <span class="advanced">Advanced</span>
88. [What is Headless Browser?](#q88) <span class="beginner">Beginner</span>
89. [How do you test performance?](#q89) <span class="advanced">Advanced</span>
90. [What is Chaos Engineering?](#q90) <span class="advanced">Advanced</span>
91. [How do you test i18n?](#q91) <span class="intermediate">Intermediate</span>
92. [What is Snapshot serialization?](#q92) <span class="advanced">Advanced</span>
93. [What is Property Based Testing?](#q93) <span class="advanced">Advanced</span>
94. [How do you debug Jest tests?](#q94) <span class="intermediate">Intermediate</span>
95. [What is `jest.isolateModules()`?](#q95) <span class="advanced">Advanced</span>
96. [How do you test a resize event?](#q96) <span class="intermediate">Intermediate</span>
97. [How do you mock `Date.now()`?](#q97) <span class="intermediate">Intermediate</span>
98. [What is `test.todo`?](#q98) <span class="beginner">Beginner</span>
99. [How do you test cookies in Jest?](#q99) <span class="intermediate">Intermediate</span>
100. [What is `jest.requireActual()`?](#q100) <span class="advanced">Advanced</span>
101. [How do you test intersection observer?](#q101) <span class="advanced">Advanced</span>
102. [What is Visual Regression Testing?](#q102) <span class="intermediate">Intermediate</span>

---

<a id="q1"></a>
### Q1: How do you mock a module in Jest?

**Difficulty**: Beginner

**Strategy**:
Module mocking is essential for isolating units of code from their dependencies during testing. Use `jest.mock()` at the top of your test file to replace an entire module with an auto-mocked version or a custom factory function. A common pitfall is forgetting that `jest.mock` is hoisted to the top of the file, so referencing variables defined in the factory requires using `jest.fn()` directly.

**Code Example**:
```javascript
jest.mock('axios');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q2"></a>
### Q2: What is Snapshot Testing in Jest?

**Difficulty**: Beginner

**Strategy**:
Snapshot testing is a quick way to detect unintended UI or output changes, making it a common topic in frontend interviews. Jest serializes the rendered component tree to a file and fails on any diff, giving you a one-line assertion that guards against regressions. The main pitfall is blindly pressing `u` to update snapshots without reviewing the diff, which can silently encode breaking changes into your test suite.

**Code Example**:
```javascript
expect(tree).toMatchSnapshot();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q3"></a>
### Q3: How do you test asynchronous code in Jest?

**Difficulty**: Intermediate

**Strategy**:
Async testing is a core skill since most real applications involve API calls, timers, or event-driven code. Jest supports callbacks (use `done` parameter), promises (return the promise), and `async/await` patterns. A common mistake is forgetting to return or await the async operation, causing the test to pass before the assertion runs.

**Code Example**:
```javascript
test('async', async () => { const data = await fetch(); expect(data).toBe('ok'); });
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q4"></a>
### Q4: Difference between `shallow` and `mount` in Enzyme?

**Difficulty**: Intermediate

**Strategy**:
Understanding the shallow versus full DOM rendering trade-off is critical for designing tests that are both fast and meaningful. `shallow` isolates the component by stubbing out children, making tests faster and less brittle to child component changes, while `mount` renders the entire tree for integration-level verification. A common mistake is using `mount` for everything, which creates slow, fragile tests that break on any deep implementation change.

**Code Example**:
```javascript
shallow(<App />);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q5"></a>
### Q5: How do you spy on a method with Jest?

**Difficulty**: Intermediate

**Strategy**:
Spies let you observe and verify function calls without fully replacing the implementation, making them crucial for testing side effects and interactions. `jest.spyOn()` wraps an existing method on an object, tracking calls, arguments, and return values while optionally calling through to the original. Be sure to restore spies in `afterEach` with `spy.mockRestore()` to avoid leaking state between tests.

**Code Example**:
```javascript
const spy = jest.spyOn(video, 'play');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q6"></a>
### Q6: How do you setup and teardown tests in Mocha?

**Difficulty**: Beginner

**Strategy**:
Setup and teardown hooks ensure each test runs in a clean, predictable state, which is critical for reliable test suites. Mocha provides `before`, `after`, `beforeEach`, and `afterEach` hooks that run at the describe-block scope. A best practice is to use `beforeEach` for per-test setup rather than `before` to avoid shared state that causes interdependent tests.

**Code Example**:
```javascript
beforeEach(() => { ... });
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q7"></a>
### Q7: How do you mock a timer in Jest?

**Difficulty**: Advanced

**Strategy**:
Timer mocking is critical for testing debounced functions, animations, polling logic, and timeouts without waiting real time. Jest replaces `setTimeout`, `setInterval`, and `Date` with fake implementations that you can fast-forward with `jest.advanceTimersByTime()`. Remember to call `jest.useRealTimers()` in cleanup to avoid breaking other tests that rely on real timers.

**Code Example**:
```javascript
jest.advanceTimersByTime(1000);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q8"></a>
### Q8: How do you test a React Hook?

**Difficulty**: Advanced

**Strategy**:
Testing hooks directly is important because hooks encapsulate reusable stateful logic that components depend on. Use `@testing-library/react-hooks` (or `renderHook` from React 18's testing utilities) to invoke hooks outside a component and assert on their return values and state changes. A common pitfall is not wrapping state updates in `act()` when testing hooks that trigger asynchronous effects.

**Code Example**:
```javascript
const { result } = renderHook(() => useCounter());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q9"></a>
### Q9: How do you mock a default export in Jest?

**Difficulty**: Advanced

**Strategy**:
Mocking default exports is necessary when testing modules that import single-export libraries like Axios or custom utility modules. The factory function must return an object with `__esModule: true` and a `default` property to correctly simulate an ES module default export. A frequent mistake is returning the mock directly instead of wrapping it in the `__esModule` structure, which causes import errors.

**Code Example**:
```javascript
jest.mock('./mod', () => ({ __esModule: true, default: jest.fn() }));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q10"></a>
### Q10: How do you test for an exception in Jest?

**Difficulty**: Beginner

**Strategy**:
Testing error handling ensures your code fails gracefully and throws meaningful errors for invalid inputs. Wrap the function call in a callback passed to `expect().toThrow()` so Jest can catch and inspect the exception. A common mistake is invoking the function directly instead of passing a callback, which causes the error to be thrown outside the assertion.

**Code Example**:
```javascript
expect(() => fn()).toThrow();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q11"></a>
### Q11: What is the difference between `describe` and `test`?

**Difficulty**: Beginner

**Strategy**:
Understanding test structure is fundamental because organized test suites are easier to maintain, debug, and extend as a codebase grows. `describe` blocks group related tests and support nested scoping with shared setup hooks, while `test` (or `it`) defines an individual assertion case. A common pitfall is putting all tests flat without `describe` grouping, which makes it hard to run targeted subsets and obscures the logical relationships between tests.

**Code Example**:
```javascript
describe('User', () => { test('has name', () => {}); });
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q12"></a>
### Q12: How do you access the DOM in Jest?

**Difficulty**: Intermediate

**Strategy**:
DOM manipulation in tests is essential for verifying that components render correctly and respond to user interactions. Jest uses jsdom by default in its test environment to simulate the browser DOM, allowing you to use `document.querySelector`, `fireEvent`, and RTL queries without a real browser. A common pitfall is forgetting that jsdom is not a full browser, so layout-related APIs like `getBoundingClientRect` return zeros and some events behave differently than in a real browser.

**Code Example**:
```javascript
document.body.innerHTML = '<div></div>';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q13"></a>
### Q13: What is `jest.fn()`?

**Difficulty**: Beginner

**Strategy**:
`jest.fn()` is the building block of all mocking in Jest, making it one of the most frequently tested concepts in interviews. It creates a spy-like function that records every call, its arguments, and return values, which you can assert against with matchers like `toHaveBeenCalled` and `toHaveBeenCalledWith`. A common mistake is forgetting to set a return value with `mockReturnValue`, causing the function to return `undefined` and leading to unexpected test failures.

**Code Example**:
```javascript
const mock = jest.fn(); mock(); expect(mock).toHaveBeenCalled();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q14"></a>
### Q14: How do you skip a test?

**Difficulty**: Beginner

**Strategy**:
Skipping tests is useful when a test is broken or depends on unfinished functionality, allowing the rest of the suite to run cleanly. Use `test.skip()` or `describe.skip()` to exclude specific tests or entire groups from execution. Avoid leaving skipped tests in the codebase long-term, as they can mask regressions that should be fixed or removed.

**Code Example**:
```javascript
test.skip('broken test', () => {});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q15"></a>
### Q15: How do you run only one test?

**Difficulty**: Beginner

**Strategy**:
Running a single test speeds up development by focusing feedback on the specific case you are debugging or building. Use `test.only()` to run just that test, or `describe.only()` to isolate an entire group. Always remove `only` before committing, since CI will skip all other tests and give a false sense of coverage.

**Code Example**:
```javascript
test.only('focus this', () => {});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q16"></a>
### Q16: How do you test React components without Enzyme?

**Difficulty**: Intermediate

**Strategy**:
Testing React components without Enzyme demonstrates that you follow modern best practices, as the community has shifted to React Testing Library. RTL encourages testing behavior from the user's perspective using accessible queries rather than accessing internal component state and lifecycle methods. The trade-off is that RTL tests are slightly harder to write for deeply nested props, but they are far more resilient to refactoring and closely mirror real user interactions.

**Code Example**:
```javascript
render(<App />); fireEvent.click(screen.getByText('Go'));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q17"></a>
### Q17: How do you mock global objects like `localStorage`?

**Difficulty**: Intermediate

**Strategy**:
Mocking browser globals is essential because Jest runs in Node.js where APIs like `localStorage`, `sessionStorage`, and `window` do not exist by default. You can assign a mock object to the global scope or mock the prototype methods directly. A best practice is to create a reusable mock setup file and reference it in your Jest configuration rather than duplicating mocks across test files.

**Code Example**:
```javascript
Storage.prototype.getItem = jest.fn();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q18"></a>
### Q18: What is Code Coverage?

**Difficulty**: Intermediate

**Strategy**:
Code coverage quantifies how much of your codebase is exercised by tests, making it a common interview metric for evaluating test thoroughness. Jest generates coverage reports for statements, branches, functions, and lines via the `--coverage` flag. A key pitfall is treating coverage as a quality guarantee; high coverage with weak assertions gives false confidence, so always focus on meaningful tests over arbitrary percentage targets.

**Code Example**:
```javascript
// Run jest --coverage
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q19"></a>
### Q19: How do you parameterize tests in Jest?

**Difficulty**: Intermediate

**Strategy**:
Parameterized tests reduce duplication by running the same assertion logic against multiple input combinations, which is especially useful for utility functions and data transformations. Jest provides `test.each()` with template literals or array syntax to define data-driven test cases. Keep parameter sets small and meaningful to avoid bloated test output that makes failures hard to diagnose.

**Code Example**:
```javascript
test.each([[1, 2, 3], [2, 2, 4]])('adds %i + %i to equal %i', (a, b, expected) => { ... });
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q20"></a>
### Q20: How do you reset mocks between tests?

**Difficulty**: Intermediate

**Strategy**:
Resetting mocks between tests is essential to prevent one test's mock state from leaking into the next, which would create hidden interdependencies. Use `jest.clearAllMocks()` in `afterEach` or set `clearMocks: true` in your Jest config to automatically reset call counts and instances between runs. A common pitfall is confusing `clearAllMocks` (resets call data) with `resetAllMocks` (also removes implementation), which can silently break tests that rely on default mock behavior.

**Code Example**:
```javascript
afterEach(() => jest.clearAllMocks());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q21"></a>
### Q21: What is a Spy in testing?

**Difficulty**: Beginner

**Strategy**:
Spies are a core testing concept because they let you verify interactions without replacing the original implementation, which is crucial for testing side effects. In Jest, `jest.spyOn()` wraps an existing method to track calls while optionally calling through to the real code, whereas Sinon provides similar functionality for Mocha-based test suites. A common pitfall is forgetting to restore spies after each test, which can cause downstream tests to see stale mock state.

**Code Example**:
```javascript
// Sinon.spy or Jest.spyOn
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q22"></a>
### Q22: How do you test Redux connected components?

**Difficulty**: Advanced

**Strategy**:
Testing Redux-connected components is a common interview scenario because it demonstrates your ability to handle stateful component integration. You must wrap the component in a `<Provider>` with a real or mock store, or test the unconnected component by exporting it separately. A best practice is to create a reusable `renderWithProviders` utility to avoid repeating Provider setup, and a common pitfall is using the production store instead of a controlled test store with predictable initial state.

**Code Example**:
```javascript
render(<Provider store={store}><App /></Provider>);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q23"></a>
### Q23: What is TDD?

**Difficulty**: Beginner

**Strategy**:
Test-Driven Development is a methodology where tests are written before the implementation code, driving better design and fewer defects. The cycle follows Red (write a failing test), Green (write minimal code to pass), and Refactor (clean up without changing behavior). A common pitfall is skipping the refactor step, which leads to accumulating technical debt even with good test coverage.

**Code Example**:
```javascript
// Red, Green, Refactor
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q24"></a>
### Q24: What is BDD?

**Difficulty**: Beginner

**Strategy**:
Behavior-Driven Development extends TDD by writing tests in natural language that describes expected behavior from a user's perspective. It uses Given-When-Then structure to bridge communication between developers, testers, and business stakeholders. Avoid the pitfall of writing overly technical BDD scenarios that lose the readability benefit that distinguishes BDD from traditional unit tests.

**Code Example**:
```javascript
// Given, When, Then
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q25"></a>
### Q25: Difference between Unit and Integration tests?

**Difficulty**: Beginner

**Strategy**:
Understanding the distinction between unit and integration tests is fundamental to building an effective testing strategy. Unit tests isolate a single function or component with all dependencies mocked, while integration tests verify that multiple pieces work together correctly. A good rule of thumb is to have many fast unit tests for edge cases and fewer integration tests covering critical user flows.

**Code Example**:
```javascript
// Jest vs Cypress
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q26"></a>
### Q26: What is E2E testing?

**Difficulty**: Beginner

**Strategy**:
End-to-end testing validates the entire application flow from the user's perspective, including the frontend, backend, and database working together. Tools like Cypress and Playwright automate browser interactions to simulate real user behavior such as form submissions and page navigation. Keep E2E suites small and focused on critical paths, as they are slower and more brittle than unit tests.

**Code Example**:
```javascript
// Test full flow
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q27"></a>
### Q27: What is Jest?

**Difficulty**: Beginner

**Strategy**:
Jest is the most widely used JavaScript testing framework, valued for its zero-config setup, built-in assertion library, and snapshot testing. It provides an all-in-one solution with mocking, code coverage, and parallel test execution out of the box. Interviewers often ask this to confirm you understand the ecosystem, so mention its integration with React, TypeScript, and Babel projects.

**Code Example**:
```javascript
expect(1).toBe(1)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q28"></a>
### Q28: What is Mocha?

**Difficulty**: Beginner

**Strategy**:
Mocha is a flexible test runner that gives developers the freedom to choose their own assertion library (Chai), mocking tools (Sinon), and reporters. Unlike Jest's batteries-included approach, Mocha's modular architecture lets you assemble a custom testing stack. This flexibility is a trade-off: you gain control but must configure and maintain each piece yourself.

**Code Example**:
```javascript
describe('...', () => { ... })
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q29"></a>
### Q29: What is Chai?

**Difficulty**: Beginner

**Strategy**:
Chai is an assertion library commonly paired with Mocha, offering multiple syntax styles to suit different preferences. It supports `should`-style, `expect`-style, and `assert`-style assertions, making it adaptable to your team's conventions. A common pitfall is mixing assertion styles within a single test suite, which reduces readability and consistency.

**Code Example**:
```javascript
expect(x).to.equal(y)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q30"></a>
### Q30: What is Enzyme?

**Difficulty**: Intermediate

**Strategy**:
Enzyme is Airbnb's React testing utility that provides a jQuery-like API for traversing and manipulating rendered components. It offers shallow, full DOM, and static rendering modes, giving fine-grained control over component isolation. Note that Enzyme is being phased out in favor of React Testing Library, so interviewers may ask you to compare the two approaches and explain why RTL is now preferred.

**Code Example**:
```javascript
shallow(<App />)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q31"></a>
### Q31: What is React Testing Library (RTL)?

**Difficulty**: Intermediate

**Strategy**:
React Testing Library is the official recommendation for testing React components, emphasizing queries that reflect how users interact with the page. It deliberately avoids exposing internal component state, forcing you to test behavior rather than implementation details. This approach leads to tests that are more resilient to refactoring, since they will not break when you change internal structure without changing user-facing behavior.

**Code Example**:
```javascript
render(<App />); screen.getByText('Hi')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q32"></a>
### Q32: How do you mock a function?

**Difficulty**: Beginner

**Strategy**:
Mocking functions is the foundation of isolated unit testing, allowing you to replace real dependencies with controlled stand-ins. Use `jest.fn()` to create a mock that tracks calls, arguments, and return values, or chain `.mockReturnValue()` and `.mockImplementation()` to define behavior. Over-mocking is a common anti-pattern; only mock external dependencies, not the unit under test itself.

**Code Example**:
```javascript
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q33"></a>
### Q33: How do you mock a module?

**Difficulty**: Intermediate

**Strategy**:
Module mocking replaces entire dependencies such as API clients, databases, or third-party libraries with controlled substitutes. Use `jest.mock('modulePath')` for auto-mocking or provide a factory function for custom behavior. Be aware that mocking too many modules can make tests brittle and disconnected from real integration, so focus on mocking only external boundaries.

**Code Example**:
```javascript
jest.mock('axios')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q34"></a>
### Q34: What is Snapshot testing?

**Difficulty**: Beginner

**Strategy**:
Snapshot testing captures the serialized output of a component or value and compares it against a stored reference on subsequent runs. It is excellent for detecting unintended changes in UI output, configuration objects, or error messages. A common pitfall is blindly updating snapshots without reviewing the diff, which can codify regressions into your test suite.

**Code Example**:
```javascript
expect(tree).toMatchSnapshot()
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q35"></a>
### Q35: How do you update snapshots?

**Difficulty**: Beginner

**Strategy**:
Snapshot updates are necessary when you intentionally change a component's output or structure. Run Jest with the `--updateSnapshot` flag (or press `u` in watch mode) to regenerate all failing snapshots. Always review the diff before updating, as blindly accepting snapshot changes is the number one way regressions slip into your codebase.

**Code Example**:
```javascript
// CLI command
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q36"></a>
### Q36: What is `beforeAll`?

**Difficulty**: Beginner

**Strategy**:
`beforeAll` runs setup logic once before all tests in a describe block, making it ideal for expensive operations like database connections or module initialization. Unlike `beforeEach`, it does not reset between tests, so avoid using it for state that needs to be clean for each test. A best practice is to pair it with `afterAll` to tear down any resources you allocate.

**Code Example**:
```javascript
beforeAll(() => { ... })
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q37"></a>
### Q37: What is `afterEach`?

**Difficulty**: Beginner

**Strategy**:
`afterEach` executes cleanup logic after every test in a describe block, ensuring each test starts with a fresh state. It is the right place to reset mocks, restore spied functions, and clear any global state mutations. Neglecting cleanup in `afterEach` is a leading cause of test interdependency, where tests pass individually but fail when run together.

**Code Example**:
```javascript
afterEach(() => { ... })
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q38"></a>
### Q38: How do you test async code?

**Difficulty**: Intermediate

**Strategy**:
Testing asynchronous code correctly is critical because unhandled promises or missing awaits lead to false-positive tests that always pass. Return promises from your test function or use `async/await` so Jest knows to wait for the assertion. For callback-based APIs, use the `done` parameter, but prefer `async/await` for cleaner and less error-prone test code.

**Code Example**:
```javascript
test('x', async () => { ... })
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q39"></a>
### Q39: How do you mock timers?

**Difficulty**: Advanced

**Strategy**:
Timer mocking replaces `setTimeout`, `setInterval`, and related functions with fakes you can control programmatically, eliminating wait times in tests. Call `jest.useFakeTimers()` at the start and advance time with `jest.advanceTimersByTime()` or `jest.runAllTimers()`. A common mistake is forgetting that fake timers also affect promises in some configurations, so be cautious when mixing timers with async operations.

**Code Example**:
```javascript
jest.advanceTimersByTime(1000)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q40"></a>
### Q40: What is `spyOn`?

**Difficulty**: Intermediate

**Strategy**:
`jest.spyOn()` creates a spy on an existing object method, allowing you to track calls while optionally preserving or overriding the original implementation. It is especially useful for verifying that a component calls an external service or handler without fully mocking the module. Always restore spies after each test with `mockRestore()` to prevent one test's spy from leaking into the next.

**Code Example**:
```javascript
jest.spyOn(obj, 'method')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q41"></a>
### Q41: How do you mock API calls?

**Difficulty**: Intermediate

**Strategy**:
Mocking API calls prevents tests from hitting real servers, making them fast, deterministic, and independent of network conditions. You can mock `global.fetch`, use `jest.mock('axios')`, or use dedicated libraries like `msw` (Mock Service Worker) for more realistic network interception. A best practice is to test both success and error response scenarios to ensure your code handles all API states.

**Code Example**:
```javascript
global.fetch = jest.fn()
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q42"></a>
### Q42: What is Coverage?

**Difficulty**: Beginner

**Strategy**:
Code coverage measures what percentage of your codebase is exercised by tests, including statements, branches, functions, and lines. It helps identify untested code paths but should not be treated as a quality guarantee, since high coverage with weak assertions gives a false sense of security. Aim for meaningful coverage of critical business logic rather than chasing an arbitrary percentage target.

**Code Example**:
```javascript
jest --coverage
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q43"></a>
### Q43: How do you test hooks?

**Difficulty**: Advanced

**Strategy**:
Testing hooks in isolation ensures the reusable stateful logic they contain works independently of any specific component. Use `renderHook` from `@testing-library/react` to execute the hook and `result.current` to access its return values and trigger updates. Remember to wrap any interactions that cause state changes in `act()` to ensure React processes updates before your assertions run.

**Code Example**:
```javascript
const { result } = renderHook(() => useHook())
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q44"></a>
### Q44: How do you test context?

**Difficulty**: Intermediate

**Strategy**:
Testing React Context requires wrapping the component under test in the appropriate Provider with a controlled store or value. You can create a helper function like `renderWithProviders` that encapsulates this setup for reuse across tests. A common mistake is testing the context provider itself rather than the components that consume it, which adds complexity without meaningful coverage.

**Code Example**:
```javascript
render(<Provider><Comp /></Provider>)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q45"></a>
### Q45: What is `act`?

**Difficulty**: Advanced

**Strategy**:
`act()` ensures that all state updates and effects are flushed before your test makes assertions, preventing warnings about unresolved updates. React Testing Library's `render` and `fireEvent` already wrap their operations in `act`, but manual calls are needed when triggering updates outside these helpers. A common pitfall is receiving "not wrapped in act" warnings, which usually means an async update was not properly awaited.

**Code Example**:
```javascript
act(() => { ... })
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q46"></a>
### Q46: How do you find elements in RTL?

**Difficulty**: Beginner

**Strategy**:
RTL provides query methods that mirror how users find elements on a page, promoting accessible and maintainable tests. Priority order is `getByRole`, `getByLabelText`, `getByPlaceholderText`, `getByText`, then `getByTestId` as a last resort. Avoid relying on `getByTestId` for everything, as it couples tests to implementation details rather than user-facing behavior.

**Code Example**:
```javascript
screen.getByRole('button')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q47"></a>
### Q47: Difference between `getBy` and `queryBy`?

**Difficulty**: Intermediate

**Strategy**:
Understanding when to use each query variant is key to writing correct assertions for element presence and absence. `getBy` throws an error if the element is not found, making it ideal for asserting something exists. `queryBy` returns `null` instead of throwing, which is what you need when asserting that an element does not exist with `expect(...).toBeNull()`.

**Code Example**:
```javascript
// queryBy for non-existence
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q48"></a>
### Q48: Difference between `getBy` and `findBy`?

**Difficulty**: Intermediate

**Strategy**:
The key distinction is that `findBy` is asynchronous and retries until the element appears or a timeout is reached, while `getBy` queries immediately. Use `findBy` when the element appears after an async operation like a data fetch, and `getBy` when the element should already be in the DOM. A common mistake is using `getBy` with a manual `waitFor` when `findBy` alone would be simpler and cleaner.

**Code Example**:
```javascript
await screen.findByText('Loaded')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q49"></a>
### Q49: How do you simulate events?

**Difficulty**: Beginner

**Strategy**:
Simulating events is how you test user interactions like clicks, typing, and form submissions in component tests. RTL provides `fireEvent` for dispatching synthetic DOM events directly on elements. For more realistic user behavior, prefer `@testing-library/user-event` over `fireEvent`, as it simulates full interaction sequences including focus, keystroke, and blur events.

**Code Example**:
```javascript
fireEvent.click(btn)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q50"></a>
### Q50: What is `user-event`?

**Difficulty**: Intermediate

**Strategy**:
`@testing-library/user-event` is the recommended replacement for `fireEvent`, providing more realistic simulations of user interactions like typing, clicking, and tabbing. It properly fires all intermediate events such as `keydown`, `keypress`, and `keyup` for a single keystroke, matching real browser behavior. Always `await` user-event calls since version 14, as operations are now asynchronous to better simulate real user timing.

**Code Example**:
```javascript
userEvent.type(input, 'text')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q51"></a>
### Q51: How do you debug tests?

**Difficulty**: Beginner

**Strategy**:
Debugging tests effectively saves hours of guessing why assertions fail, especially with complex component hierarchies. Use `screen.debug()` to print the current DOM, `console.log` inside mocks, or attach a real debugger via `node --inspect-brk`. The most common mistake when debugging is adding too many logs at once; narrow your focus to one failing assertion at a time.

**Code Example**:
```javascript
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q52"></a>
### Q52: How do you skip a test?

**Difficulty**: Beginner

**Strategy**:
Skipping tests is a practical skill interviewers look for to confirm you can manage failing or incomplete tests without blocking a team's CI pipeline. Use `test.skip()` or `describe.skip()` to exclude specific tests or groups from execution while keeping them visible in the test output. Avoid accumulating skipped tests long-term, as they often indicate neglected bugs or incomplete features that silently erode confidence in the test suite.

**Code Example**:
```javascript
test.skip('...', () => {})
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q53"></a>
### Q53: How do you focus a test?

**Difficulty**: Beginner

**Strategy**:
Focusing a test with `test.only()` is an essential debugging technique that demonstrates you know how to iterate quickly during development. It runs only the specified test, bypassing the entire suite to give fast feedback on the case you are actively working on. The critical pitfall is accidentally committing `only` calls, which causes CI to skip all other tests and produce misleadingly green builds.

**Code Example**:
```javascript
test.only('...', () => {})
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q54"></a>
### Q54: What is `describe`?

**Difficulty**: Beginner

**Strategy**:
`describe` blocks are the organizational backbone of test suites, and interviewers expect you to use them to structure tests logically. They group related tests into nested blocks, each with its own scope for setup and teardown hooks like `beforeEach` and `afterEach`. A common pitfall is creating deeply nested `describe` blocks that make tests hard to follow; keep nesting to two or three levels at most.

**Code Example**:
```javascript
describe('Group', () => {})
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q55"></a>
### Q55: How do you mock local storage?

**Difficulty**: Intermediate

**Strategy**:
Mocking `localStorage` is essential because jsdom provides only a basic implementation, and tests need deterministic control over stored values. You can mock individual methods on `Storage.prototype` or replace the entire `window.localStorage` object with a jest.fn()-based mock. A common pitfall is forgetting to clear mock state between tests, causing one test's stored data to leak into the next and produce flaky results.

**Code Example**:
```javascript
Storage.prototype.getItem = jest.fn()
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q56"></a>
### Q56: How do you test routing?

**Difficulty**: Intermediate

**Strategy**:
Testing routing logic is important because navigation is a core user flow, and broken routes cause immediate user-facing failures. Use React Router's `MemoryRouter` to control the initial route and history in tests without depending on the browser's real URL bar. A common pitfall is using `BrowserRouter` in tests, which modifies the real browser history and causes tests to interfere with each other.

**Code Example**:
```javascript
<MemoryRouter><App /></MemoryRouter>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q57"></a>
### Q57: What is Cypress?

**Difficulty**: Intermediate

**Strategy**:
Cypress is a modern E2E testing framework that runs directly in the browser, giving it native access to the DOM and network layer without the overhead of WebDriver. It provides time-travel debugging, automatic waiting, and snapshot capabilities that make writing and debugging E2E tests significantly easier than Selenium-based tools. A key trade-off is that Cypress historically had limited cross-browser support and cannot run multiple browser tabs simultaneously, though both limitations have improved in recent versions.

**Code Example**:
```javascript
cy.visit('/page')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q58"></a>
### Q58: What is Playwright?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
await page.goto('/url')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q59"></a>
### Q59: Difference between Mock and Stub?

**Difficulty**: Advanced

**Strategy**:
Distinguishing mocks from stubs shows you understand the nuance of test doubles, a topic that frequently comes up in architecture-focused interviews. A stub returns hardcoded responses to control the test environment, while a mock also verifies that specific interactions occurred, such as checking that a function was called with particular arguments. A common pitfall is using the term "mock" loosely for all test doubles, which signals a surface-level understanding of testing patterns.

**Code Example**:
```javascript
// Mock expects call
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q60"></a>
### Q60: What is Mutation Testing?

**Difficulty**: Advanced

**Strategy**:

**Code Example**:
```javascript
// Stryker
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q61"></a>
### Q61: How do you test accessibility?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
expect(await axe(container)).toHaveNoViolations()
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q62"></a>
### Q62: What is Visual Regression Testing?

**Difficulty**: Advanced

**Strategy**:

**Code Example**:
```javascript
// Percy, Applitools
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q63"></a>
### Q63: How do you test Redux?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
renderWithProviders(<App />)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q64"></a>
### Q64: How do you mock Date?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
jest.useFakeTimers().setSystemTime(...) 
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q65"></a>
### Q65: What is `cleanup`?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
// RTL does auto-cleanup
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q66"></a>
### Q66: How do you test portals?

**Difficulty**: Advanced

**Strategy**:

**Code Example**:
```javascript
within(baseElement).getByText(...) 
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q67"></a>
### Q67: What is Property Based Testing?

**Difficulty**: Advanced

**Strategy**:

**Code Example**:
```javascript
// fast-check
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q68"></a>
### Q68: How do you setup global config?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
// Global mocks
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q69"></a>
### Q69: What is the Pyramid of Testing?

**Difficulty**: Beginner

**Strategy**:

**Code Example**:
```javascript
// More units, fewer E2E
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q70"></a>
### Q70: How do you test strict mode?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
<StrictMode><App /></StrictMode>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q71"></a>
### Q71: How do you test error boundaries?

**Difficulty**: Advanced

**Strategy**:

**Code Example**:
```javascript
// Console.error mock needed
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q72"></a>
### Q72: What is shallow rendering?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
// Enzyme shallow
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q73"></a>
### Q73: Why prefer full rendering?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
// RTL default
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q74"></a>
### Q74: How do you test observables?

**Difficulty**: Advanced

**Strategy**:

**Code Example**:
```javascript
// RxJS testing
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q75"></a>
### Q75: What is CI/CD testing?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
// GitHub Actions
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q76"></a>
### Q76: How do you parallelize tests?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
// Workers
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q77"></a>
### Q77: What is Flaky test?

**Difficulty**: Beginner

**Strategy**:

**Code Example**:
```javascript
// Avoid race conditions
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q78"></a>
### Q78: How do you fix flaky tests?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
// Debugging
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q79"></a>
### Q79: What is Contract Testing?

**Difficulty**: Advanced

**Strategy**:

**Code Example**:
```javascript
// Pact
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q80"></a>
### Q80: How do you test WebSockets?

**Difficulty**: Advanced

**Strategy**:

**Code Example**:
```javascript
// jest-websocket-mock
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q81"></a>
### Q81: How do you test Service Workers?

**Difficulty**: Advanced

**Strategy**:

**Code Example**:
```javascript
// Complex in Jest
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q82"></a>
### Q82: What is `test.todo`?

**Difficulty**: Beginner

**Strategy**:

**Code Example**:
```javascript
test.todo('implement later')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q83"></a>
### Q83: How do you mock a module partially?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
jest.requireActual('./mod')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q84"></a>
### Q84: What is `__mocks__` folder?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
// __mocks__/fs.js
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q85"></a>
### Q85: How do you test memory leaks?

**Difficulty**: Advanced

**Strategy**:

**Code Example**:
```javascript
// Node --inspect
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q86"></a>
### Q86: What is Static Analysis?

**Difficulty**: Beginner

**Strategy**:

**Code Example**:
```javascript
// ESLint, TypeScript
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q87"></a>
### Q87: How do you test Canvas?

**Difficulty**: Advanced

**Strategy**:

**Code Example**:
```javascript
// Mock context
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q88"></a>
### Q88: What is Headless Browser?

**Difficulty**: Beginner

**Strategy**:

**Code Example**:
```javascript
// Puppeteer
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q89"></a>
### Q89: How do you test performance?

**Difficulty**: Advanced

**Strategy**:

**Code Example**:
```javascript
// Measures web vitals
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q90"></a>
### Q90: What is Chaos Engineering?

**Difficulty**: Advanced

**Strategy**:

**Code Example**:
```javascript
// Gremlin
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q91"></a>
### Q91: How do you test i18n?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
t = (k) => k
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q92"></a>
### Q92: What is Snapshot serialization?

**Difficulty**: Advanced

**Strategy**:

**Code Example**:
```javascript
expect.addSnapshotSerializer(...) 
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div><a id="q93"></a>

### Q93: What is Property Based Testing?

**Difficulty**: Advanced

**Strategy**:
Generating random inputs (properties) to verify that certain invariants hold true for a function (e.g., fast-check).

**Code Example**:
```javascript
fc.assert(fc.property(fc.integer(), n => n + 0 === n));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q94"></a>

### Q94: How do you debug Jest tests?

**Difficulty**: Intermediate

**Strategy**:
Use `node --inspect-brk` or VS Code's debugger. Place `debugger;` statement in test.

**Code Example**:
```javascript
node --inspect-brk node_modules/.bin/jest --runInBand
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q95"></a>

### Q95: What is `jest.isolateModules()`?

**Difficulty**: Advanced

**Strategy**:
Used to run a block of code with a fresh module registry (re-importing modules). Good for testing stateful modules.

**Code Example**:
```javascript
jest.isolateModules(() => { const mod = require('./myModule'); });
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q96"></a>

### Q96: How do you test a resize event?

**Difficulty**: Intermediate

**Strategy**:
Mock `window.innerWidth` and dispatch a 'resize' event on window.

**Code Example**:
```javascript
window.innerWidth = 500; window.dispatchEvent(new Event('resize'));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q97"></a>

### Q97: How do you mock `Date.now()`?

**Difficulty**: Intermediate

**Strategy**:
Use `jest.useFakeTimers()` and `jest.setSystemTime()`.

**Code Example**:
```javascript
jest.useFakeTimers(); jest.setSystemTime(new Date('2023-01-01'));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q98"></a>

### Q98: What is `test.todo`?

**Difficulty**: Beginner

**Strategy**:
A way to write a placeholder for a test you plan to write later. It appears in the output but doesn't fail.

**Code Example**:
```javascript
test.todo('should handle edge case');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q99"></a>

### Q99: How do you test cookies in Jest?

**Difficulty**: Intermediate

**Strategy**:
Mock `document.cookie` (getter/setter) usually via `jest-environment-jsdom` or manually defined property.

**Code Example**:
```javascript
Object.defineProperty(document, 'cookie', { ... });
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q100"></a>

### Q100: What is `jest.requireActual()`?

**Difficulty**: Advanced

**Strategy**:
Used inside a manual mock to import the original module (e.g., to mock only one function of a library).

**Code Example**:
```javascript
const original = jest.requireActual('axios');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q101"></a>

### Q101: How do you test intersection observer?

**Difficulty**: Advanced

**Strategy**:
Since it's not in JSDOM, you must mock `window.IntersectionObserver` class and its methods.

**Code Example**:
```javascript
window.IntersectionObserver = jest.fn(() => ({ observe: jest.fn(), ... }));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q102"></a>

### Q102: What is Visual Regression Testing?

**Difficulty**: Intermediate

**Strategy**:
Comparing screenshots of UI components pixel-by-pixel to detect unintended visual changes (e.g., Percy, Chromatic).

**Code Example**:
```javascript
cy.matchImageSnapshot();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

