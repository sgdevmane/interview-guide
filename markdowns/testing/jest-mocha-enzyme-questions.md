<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>Testing (Jest/Mocha) Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for developers</b></p>
</div>

---

## Table of Contents

1. [How do you mock a module in Jest?](#q1-how-do-you-mock-a-module-in-jest) <span class="beginner">Beginner</span>
2. [What is Snapshot Testing in Jest?](#q2-what-is-snapshot-testing-in-jest) <span class="beginner">Beginner</span>
3. [How do you test asynchronous code in Jest?](#q3-how-do-you-test-asynchronous-code-in-jest) <span class="intermediate">Intermediate</span>
4. [Difference between `shallow` and `mount` in Enzyme?](#q4-difference-between-shallow-and-mount-in-enzyme) <span class="intermediate">Intermediate</span>
5. [How do you spy on a method with Jest?](#q5-how-do-you-spy-on-a-method-with-jest) <span class="intermediate">Intermediate</span>
6. [How do you setup and teardown tests in Mocha?](#q6-how-do-you-setup-and-teardown-tests-in-mocha) <span class="beginner">Beginner</span>
7. [How do you mock a timer in Jest?](#q7-how-do-you-mock-a-timer-in-jest) <span class="advanced">Advanced</span>
8. [How do you test a React Hook?](#q8-how-do-you-test-a-react-hook) <span class="advanced">Advanced</span>
9. [How do you mock a default export in Jest?](#q9-how-do-you-mock-a-default-export-in-jest) <span class="advanced">Advanced</span>
10. [How do you test for an exception in Jest?](#q10-how-do-you-test-for-an-exception-in-jest) <span class="beginner">Beginner</span>
11. [What is the difference between `describe` and `test`?](#q11-what-is-the-difference-between-describe-and-test) <span class="beginner">Beginner</span>
12. [How do you access the DOM in Jest?](#q12-how-do-you-access-the-dom-in-jest) <span class="intermediate">Intermediate</span>
13. [What is `jest.fn()`?](#q13-what-is-jestfn) <span class="beginner">Beginner</span>
14. [How do you skip a test?](#q14-how-do-you-skip-a-test) <span class="beginner">Beginner</span>
15. [How do you run only one test?](#q15-how-do-you-run-only-one-test) <span class="beginner">Beginner</span>
16. [How do you test React components without Enzyme?](#q16-how-do-you-test-react-components-without-enzyme) <span class="intermediate">Intermediate</span>
17. [How do you mock global objects like `localStorage`?](#q17-how-do-you-mock-global-objects-like-localstorage) <span class="intermediate">Intermediate</span>
18. [What is Code Coverage?](#q18-what-is-code-coverage) <span class="intermediate">Intermediate</span>
19. [How do you parameterize tests in Jest?](#q19-how-do-you-parameterize-tests-in-jest) <span class="intermediate">Intermediate</span>
20. [How do you reset mocks between tests?](#q20-how-do-you-reset-mocks-between-tests) <span class="intermediate">Intermediate</span>
21. [What is a Spy in testing?](#q21-what-is-a-spy-in-testing) <span class="beginner">Beginner</span>
22. [How do you test Redux connected components?](#q22-how-do-you-test-redux-connected-components) <span class="advanced">Advanced</span>
23. [What is TDD?](#q23-what-is-tdd) <span class="beginner">Beginner</span>
24. [What is BDD?](#q24-what-is-bdd) <span class="beginner">Beginner</span>
25. [Difference between Unit and Integration tests?](#q25-difference-between-unit-and-integration-tests) <span class="beginner">Beginner</span>
26. [What is E2E testing?](#q26-what-is-e2e-testing) <span class="beginner">Beginner</span>
27. [What is Jest?](#q27-what-is-jest) <span class="beginner">Beginner</span>
28. [What is Mocha?](#q28-what-is-mocha) <span class="beginner">Beginner</span>
29. [What is Chai?](#q29-what-is-chai) <span class="beginner">Beginner</span>
30. [What is Enzyme?](#q30-what-is-enzyme) <span class="intermediate">Intermediate</span>
31. [What is React Testing Library (RTL)?](#q31-what-is-react-testing-library-rtl) <span class="intermediate">Intermediate</span>
32. [How do you mock a function?](#q32-how-do-you-mock-a-function) <span class="beginner">Beginner</span>
33. [How do you mock a module?](#q33-how-do-you-mock-a-module) <span class="intermediate">Intermediate</span>
34. [What is Snapshot testing?](#q34-what-is-snapshot-testing) <span class="beginner">Beginner</span>
35. [How do you update snapshots?](#q35-how-do-you-update-snapshots) <span class="beginner">Beginner</span>
36. [What is `beforeAll`?](#q36-what-is-beforeall) <span class="beginner">Beginner</span>
37. [What is `afterEach`?](#q37-what-is-aftereach) <span class="beginner">Beginner</span>
38. [How do you test async code?](#q38-how-do-you-test-async-code) <span class="intermediate">Intermediate</span>
39. [How do you mock timers?](#q39-how-do-you-mock-timers) <span class="advanced">Advanced</span>
40. [What is `spyOn`?](#q40-what-is-spyon) <span class="intermediate">Intermediate</span>
41. [How do you mock API calls?](#q41-how-do-you-mock-api-calls) <span class="intermediate">Intermediate</span>
42. [What is Coverage?](#q42-what-is-coverage) <span class="beginner">Beginner</span>
43. [How do you test hooks?](#q43-how-do-you-test-hooks) <span class="advanced">Advanced</span>
44. [How do you test context?](#q44-how-do-you-test-context) <span class="intermediate">Intermediate</span>
45. [What is `act`?](#q45-what-is-act) <span class="advanced">Advanced</span>
46. [How do you find elements in RTL?](#q46-how-do-you-find-elements-in-rtl) <span class="beginner">Beginner</span>
47. [Difference between `getBy` and `queryBy`?](#q47-difference-between-getby-and-queryby) <span class="intermediate">Intermediate</span>
48. [Difference between `getBy` and `findBy`?](#q48-difference-between-getby-and-findby) <span class="intermediate">Intermediate</span>
49. [How do you simulate events?](#q49-how-do-you-simulate-events) <span class="beginner">Beginner</span>
50. [What is `user-event`?](#q50-what-is-user-event) <span class="intermediate">Intermediate</span>
51. [How do you debug tests?](#q51-how-do-you-debug-tests) <span class="beginner">Beginner</span>
52. [How do you skip a test?](#q52-how-do-you-skip-a-test) <span class="beginner">Beginner</span>
53. [How do you focus a test?](#q53-how-do-you-focus-a-test) <span class="beginner">Beginner</span>
54. [What is `describe`?](#q54-what-is-describe) <span class="beginner">Beginner</span>
55. [How do you mock local storage?](#q55-how-do-you-mock-local-storage) <span class="intermediate">Intermediate</span>
56. [How do you test routing?](#q56-how-do-you-test-routing) <span class="intermediate">Intermediate</span>
57. [What is Cypress?](#q57-what-is-cypress) <span class="intermediate">Intermediate</span>
58. [What is Playwright?](#q58-what-is-playwright) <span class="intermediate">Intermediate</span>
59. [Difference between Mock and Stub?](#q59-difference-between-mock-and-stub) <span class="advanced">Advanced</span>
60. [What is Mutation Testing?](#q60-what-is-mutation-testing) <span class="advanced">Advanced</span>
61. [How do you test accessibility?](#q61-how-do-you-test-accessibility) <span class="intermediate">Intermediate</span>
62. [What is Visual Regression Testing?](#q62-what-is-visual-regression-testing) <span class="advanced">Advanced</span>
63. [How do you test Redux?](#q63-how-do-you-test-redux) <span class="intermediate">Intermediate</span>
64. [How do you mock Date?](#q64-how-do-you-mock-date) <span class="intermediate">Intermediate</span>
65. [What is `cleanup`?](#q65-what-is-cleanup) <span class="intermediate">Intermediate</span>
66. [How do you test portals?](#q66-how-do-you-test-portals) <span class="advanced">Advanced</span>
67. [What is Property Based Testing?](#q67-what-is-property-based-testing) <span class="advanced">Advanced</span>
68. [How do you setup global config?](#q68-how-do-you-setup-global-config) <span class="intermediate">Intermediate</span>
69. [What is the Pyramid of Testing?](#q69-what-is-the-pyramid-of-testing) <span class="beginner">Beginner</span>
70. [How do you test strict mode?](#q70-how-do-you-test-strict-mode) <span class="intermediate">Intermediate</span>
71. [How do you test error boundaries?](#q71-how-do-you-test-error-boundaries) <span class="advanced">Advanced</span>
72. [What is shallow rendering?](#q72-what-is-shallow-rendering) <span class="intermediate">Intermediate</span>
73. [Why prefer full rendering?](#q73-why-prefer-full-rendering) <span class="intermediate">Intermediate</span>
74. [How do you test observables?](#q74-how-do-you-test-observables) <span class="advanced">Advanced</span>
75. [What is CI/CD testing?](#q75-what-is-cicd-testing) <span class="intermediate">Intermediate</span>
76. [How do you parallelize tests?](#q76-how-do-you-parallelize-tests) <span class="intermediate">Intermediate</span>
77. [What is Flaky test?](#q77-what-is-flaky-test) <span class="beginner">Beginner</span>
78. [How do you fix flaky tests?](#q78-how-do-you-fix-flaky-tests) <span class="intermediate">Intermediate</span>
79. [What is Contract Testing?](#q79-what-is-contract-testing) <span class="advanced">Advanced</span>
80. [How do you test WebSockets?](#q80-how-do-you-test-websockets) <span class="advanced">Advanced</span>
81. [How do you test Service Workers?](#q81-how-do-you-test-service-workers) <span class="advanced">Advanced</span>
82. [What is `test.todo`?](#q82-what-is-testtodo) <span class="beginner">Beginner</span>
83. [How do you mock a module partially?](#q83-how-do-you-mock-a-module-partially) <span class="intermediate">Intermediate</span>
84. [What is `__mocks__` folder?](#q84-what-is-mocks-folder) <span class="intermediate">Intermediate</span>
85. [How do you test memory leaks?](#q85-how-do-you-test-memory-leaks) <span class="advanced">Advanced</span>
86. [What is Static Analysis?](#q86-what-is-static-analysis) <span class="beginner">Beginner</span>
87. [How do you test Canvas?](#q87-how-do-you-test-canvas) <span class="advanced">Advanced</span>
88. [What is Headless Browser?](#q88-what-is-headless-browser) <span class="beginner">Beginner</span>
89. [How do you test performance?](#q89-how-do-you-test-performance) <span class="advanced">Advanced</span>
90. [What is Chaos Engineering?](#q90-what-is-chaos-engineering) <span class="advanced">Advanced</span>
91. [How do you test i18n?](#q91-how-do-you-test-i18n) <span class="intermediate">Intermediate</span>
92. [What is Snapshot serialization?](#q92-what-is-snapshot-serialization) <span class="advanced">Advanced</span>

---

<a id="q1"></a>
### Q1: How do you mock a module in Jest?

**Difficulty**: Beginner

**Strategy**:
Use `jest.mock()`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Captures rendered output and compares to a reference file.

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
Use `async/await`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
`shallow` renders only the current component. `mount` renders full DOM tree.

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
Use `jest.spyOn`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Use `before`, `after`, `beforeEach`, `afterEach`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Use `jest.useFakeTimers()`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Use `renderHook` from testing-library. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Use `__esModule: true`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Use `toThrow()`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
`describe` groups tests. `test` (or `it`) runs the actual test case.

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
Jest uses jsdom to simulate a browser environment.

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
Creates a mock function that tracks calls and returns values.

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
Use `.skip`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Use `.only`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Use React Testing Library (RTL). It focuses on user interactions.

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
Mock the prototype or assign to window. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
A metric showing what percentage of your code is executed during tests.

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
Use `test.each`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Use `jest.clearAllMocks()` or configure `clearMocks: true`.

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
A test double that records information about how it is called.

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
Wrap the component in a `<Provider store={store}>`.

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
Test Driven Development. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Behavior Driven Development. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Unit: isolated. Integration: combined. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
End to End testing. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Test runner by Facebook. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Test framework. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Assertion library. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
React testing utility (older). This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Focus on user behavior. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
jest.fn() This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const mock = jest.fn() This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q33"></a>
### Q33: How do you mock a module?

**Difficulty**: Intermediate

**Strategy**:
jest.mock() This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Compare UI to saved file. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
jest -u This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Runs once before all tests. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Runs after every test. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
async/await. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
jest.useFakeTimers() This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Track calls to existing method. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Mock fetch or axios. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
% of code tested. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
renderHook from RTL. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Wrap in Provider. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Wrap state updates. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
getBy, queryBy, findBy. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
getBy throws if not found, queryBy returns null. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
findBy is async (waits). This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
fireEvent or userEvent. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Simulates real user interactions. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
screen.debug() This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
screen.debug() This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q52"></a>
### Q52: How do you skip a test?

**Difficulty**: Beginner

**Strategy**:
test.skip or xit. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
test.only or fit. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Group tests. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Mock window.localStorage. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Wrap in MemoryRouter. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
E2E testing tool. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
E2E tool by Microsoft. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Stub provides canned answer. Mock verifies behavior.

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
Modifies code to ensure tests fail. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
jest-axe. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Compare pixels. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Integration test with store. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
jest.setSystemTime() This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Unmounts trees after test. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Check `baseElement`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Test with random data inputs. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
jest.config.js setupFilesAfterEnv. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Unit > Integration > E2E. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Wrap in StrictMode. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Throw in component, check fallback. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Render one level deep. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Closer to real user usage. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Marble testing. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Run tests in pipeline. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Jest does it by default. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Fails randomly. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Isolate, fix async, mock time. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Verify API contracts. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Mock server. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Browser env needed. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Placeholder. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
requireActual. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Manual mocks location. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Heap snapshots. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Linting, Types. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
jest-canvas-mock. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Browser without UI. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Lighthouse CI. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Break things on purpose. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Mock translation function. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Format snapshot output. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
expect.addSnapshotSerializer(...) 
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>