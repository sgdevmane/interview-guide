<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>React Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for frontend developers</b></p>
</div>

---

## Table of Contents

1. [How do you implement a custom hook `useFetch` with caching and cancellation?](#q1-how-do-you-implement-a-custom-hook-usefetch-with-caching-and-cancellation) <span class="advanced">Advanced</span>
2. [How do you optimize a React application using `useMemo` and `useCallback` correctly?](#q2-how-do-you-optimize-a-react-application-using-usememo-and-usecallback-correctly) <span class="advanced">Advanced</span>
3. [How do you manage global state using React Context without triggering unnecessary re-renders?](#q3-how-do-you-manage-global-state-using-react-context-without-triggering-unnecessary-re-renders) <span class="advanced">Advanced</span>
4. [How do you implement a Compound Component pattern (e.g., Tabs)?](#q4-how-do-you-implement-a-compound-component-pattern-eg-tabs) <span class="advanced">Advanced</span>
5. [How do you create a Higher-Order Component (HOC) for authentication?](#q5-how-do-you-create-a-higher-order-component-hoc-for-authentication) <span class="advanced">Advanced</span>
6. [How do you implement the Render Props pattern for code reuse?](#q6-how-do-you-implement-the-render-props-pattern-for-code-reuse) <span class="intermediate">Intermediate</span>
7. [How do you implement an Error Boundary to catch crashes in child components?](#q7-how-do-you-implement-an-error-boundary-to-catch-crashes-in-child-components) <span class="intermediate">Intermediate</span>
8. [How do you use `useImperativeHandle` to expose child methods to a parent?](#q8-how-do-you-use-useimperativehandle-to-expose-child-methods-to-a-parent) <span class="advanced">Advanced</span>
9. [How do you implement a Portal to render children into a different part of the DOM?](#q9-how-do-you-implement-a-portal-to-render-children-into-a-different-part-of-the-dom) <span class="intermediate">Intermediate</span>
10. [How do you optimize large lists using Virtualization (Windowing)?](#q10-how-do-you-optimize-large-lists-using-virtualization-windowing) <span class="advanced">Advanced</span>
11. [How do you implement a custom `useDebounce` hook?](#q11-how-do-you-implement-a-custom-usedebounce-hook) <span class="intermediate">Intermediate</span>
12. [How do you implement a custom `useLocalStorage` hook?](#q12-how-do-you-implement-a-custom-uselocalstorage-hook) <span class="intermediate">Intermediate</span>
13. [How do you implement a custom `usePrevious` hook?](#q13-how-do-you-implement-a-custom-useprevious-hook) <span class="intermediate">Intermediate</span>
14. [What is the difference between `useEffect` and `useLayoutEffect`?](#q14-what-is-the-difference-between-useeffect-and-uselayouteffect) <span class="intermediate">Intermediate</span>
15. [How do you use `forwardRef` to pass refs to child components?](#q15-how-do-you-use-forwardref-to-pass-refs-to-child-components) <span class="intermediate">Intermediate</span>
16. [Controlled vs Uncontrolled Components: When to use which?](#q16-controlled-vs-uncontrolled-components-when-to-use-which) <span class="beginner">Beginner</span>
17. [How do you use `React.memo` to prevent re-renders?](#q17-how-do-you-use-reactmemo-to-prevent-re-renders) <span class="intermediate">Intermediate</span>
18. [How do you implement Code Splitting using `React.lazy` and `Suspense`?](#q18-how-do-you-implement-code-splitting-using-reactlazy-and-suspense) <span class="intermediate">Intermediate</span>
19. [How do you handle forms efficiently using React Hook Form?](#q19-how-do-you-handle-forms-efficiently-using-react-hook-form) <span class="intermediate">Intermediate</span>
20. [How do you manage state with Redux Toolkit (Slice + Thunk)?](#q20-how-do-you-manage-state-with-redux-toolkit-slice--thunk) <span class="advanced">Advanced</span>
21. [How do you create a simple store using Zustand?](#q21-how-do-you-create-a-simple-store-using-zustand) <span class="intermediate">Intermediate</span>
22. [How do you implement Private Routes for authentication?](#q22-how-do-you-implement-private-routes-for-authentication) <span class="intermediate">Intermediate</span>
23. [How do you handle JWT Authentication (Login/Logout)?](#q23-how-do-you-handle-jwt-authentication-loginlogout) <span class="intermediate">Intermediate</span>
24. [How do you unit test a React component using Jest and React Testing Library?](#q24-how-do-you-unit-test-a-react-component-using-jest-and-react-testing-library) <span class="intermediate">Intermediate</span>
25. [How do you mock API calls in Jest tests?](#q25-how-do-you-mock-api-calls-in-jest-tests) <span class="intermediate">Intermediate</span>
26. [How do you prevent XSS attacks in React?](#q26-how-do-you-prevent-xss-attacks-in-react) <span class="intermediate">Intermediate</span>
27. [How do you fix "Can't perform a React state update on an unmounted component"?](#q27-how-do-you-fix-cant-perform-a-react-state-update-on-an-unmounted-component) <span class="intermediate">Intermediate</span>
28. [How do you manage focus for accessibility (A11y)?](#q28-how-do-you-manage-focus-for-accessibility-a11y) <span class="intermediate">Intermediate</span>
29. [SSR vs CSR vs SSG: When to use what?](#q29-ssr-vs-csr-vs-ssg-when-to-use-what) <span class="intermediate">Intermediate</span>
30. [What is React Fiber and how does it improve performance?](#q30-what-is-react-fiber-and-how-does-it-improve-performance) <span class="expert">Expert</span>
31. [`useState` vs `useReducer`: When should you choose one over the other?](#q31-usestate-vs-usereducer:-when-should-you-choose-one-over-the-other) <span class="intermediate">Intermediate</span>
32. [How do you implement a custom hook `useOnClickOutside` to close modals?](#q32-how-do-you-implement-a-custom-hook-useonclickoutside-to-close-modals) <span class="intermediate">Intermediate</span>
33. [How do you implement a `useMediaQuery` hook for responsive designs?](#q33-how-do-you-implement-a-usemediaquery-hook-for-responsive-designs) <span class="intermediate">Intermediate</span>
34. [How do you make a custom button accessible using ARIA attributes?](#q34-how-do-you-make-a-custom-button-accessible-using-aria-attributes) <span class="intermediate">Intermediate</span>
35. [How do you profile a React application to identify performance bottlenecks?](#q35-how-do-you-profile-a-react-application-to-identify-performance-bottlenecks) <span class="advanced">Advanced</span>
36. [How do you safely render HTML content to prevent XSS attacks?](#q36-how-do-you-safely-render-html-content-to-prevent-xss-attacks) <span class="intermediate">Intermediate</span>
37. [What is the difference between `fireEvent` and `userEvent` in React Testing Library?](#q37-what-is-the-difference-between-fireevent-and-userevent-in-react-testing-library) <span class="intermediate">Intermediate</span>
38. [How do you handle errors in Functional Components (since they lack `componentDidCatch`)?](#q38-how-do-you-handle-errors-in-functional-components-since-they-lack-componentdidcatch) <span class="intermediate">Intermediate</span>
39. [What is Automatic Batching in React 18?](#q39-what-is-automatic-batching-in-react-18) <span class="advanced">Advanced</span>
40. [How do you use `useTransition` to keep the UI responsive during heavy state updates?](#q40-how-do-you-use-usetransition-to-keep-the-ui-responsive-during-heavy-state-updates) <span class="advanced">Advanced</span>
41. [What is `useDeferredValue` and when should you use it?](#q41-what-is-usedeferredvalue-and-when-should-you-use-it) <span class="advanced">Advanced</span>
42. [How does Suspense for Data Fetching work?](#q42-how-does-suspense-for-data-fetching-work) <span class="advanced">Advanced</span>
43. [Why is using the array index as a key an anti-pattern?](#q43-why-is-using-the-array-index-as-a-key-an-anti-pattern) <span class="beginner">Beginner</span>
44. [How do you solve Props Drilling without Context?](#q44-how-do-you-solve-props-drilling-without-context) <span class="intermediate">Intermediate</span>
45. [What are Micro-frontends and how does Module Federation help?](#q45-what-are-micro-frontends-and-how-does-module-federation-help) <span class="expert">Expert</span>
46. [How do you use Generics in TypeScript with React Props?](#q46-how-do-you-use-generics-in-typescript-with-react-props) <span class="intermediate">Intermediate</span>
47. [How do you create Discriminated Unions for mutually exclusive props?](#q47-how-do-you-create-discriminated-unions-for-mutually-exclusive-props) <span class="advanced">Advanced</span>
48. [What does React Strict Mode do?](#q48-what-does-react-strict-mode-do) <span class="beginner">Beginner</span>
49. [How does Event Delegation work in React?](#q49-how-does-event-delegation-work-in-react) <span class="advanced">Advanced</span>
50. [What is the React Reconciler?](#q50-what-is-the-react-reconciler) <span class="expert">Expert</span>
51. [How does React Fiber improve performance?](#q51-how-does-react-fiber-improve-performance) <span class="advanced">Advanced</span>
52. [What is the difference between `useMemo` and `useCallback`?](#q52-what-is-the-difference-between-usememo-and-usecallback) <span class="intermediate">Intermediate</span>
53. [How do you implement an Error Boundary?](#q53-how-do-you-implement-an-error-boundary) <span class="intermediate">Intermediate</span>
54. [What is the purpose of `useLayoutEffect`?](#q54-what-is-the-purpose-of-uselayouteffect) <span class="advanced">Advanced</span>
55. [How do you use React Portals?](#q55-how-do-you-use-react-portals) <span class="intermediate">Intermediate</span>
56. [What is Suspense for Data Fetching?](#q56-what-is-suspense-for-data-fetching) <span class="advanced">Advanced</span>
57. [How do you prevent prop drilling?](#q57-how-do-you-prevent-prop-drilling) <span class="beginner">Beginner</span>
58. [What is `forwardRef` used for?](#q58-what-is-forwardref-used-for) <span class="intermediate">Intermediate</span>
59. [How do Custom Hooks share logic?](#q59-how-do-custom-hooks-share-logic) <span class="beginner">Beginner</span>
60. [Difference between Controlled and Uncontrolled inputs?](#q60-difference-between-controlled-and-uncontrolled-inputs) <span class="beginner">Beginner</span>
61. [How do you optimize a large list in React?](#q61-how-do-you-optimize-a-large-list-in-react) <span class="intermediate">Intermediate</span>
62. [What is the key prop and why is it important?](#q62-what-is-the-key-prop-and-why-is-it-important) <span class="beginner">Beginner</span>
63. [How do you handle side effects in React?](#q63-how-do-you-handle-side-effects-in-react) <span class="beginner">Beginner</span>
64. [What is Higher-Order Component (HOC)?](#q64-what-is-higher-order-component-hoc) <span class="advanced">Advanced</span>
65. [How does `setState` batch updates?](#q65-how-does-setstate-batch-updates) <span class="advanced">Advanced</span>
66. [What is the Rules of Hooks?](#q66-what-is-the-rules-of-hooks) <span class="beginner">Beginner</span>
67. [How do you test a React component?](#q67-how-do-you-test-a-react-component) <span class="intermediate">Intermediate</span>
68. [What is Code Splitting?](#q68-what-is-code-splitting) <span class="intermediate">Intermediate</span>
69. [How do you handle forms in React?](#q69-how-do-you-handle-forms-in-react) <span class="beginner">Beginner</span>
70. [What is Reconciliation?](#q70-what-is-reconciliation) <span class="advanced">Advanced</span>
71. [How do you force a re-render?](#q71-how-do-you-force-a-re-render) <span class="intermediate">Intermediate</span>
72. [What is Strict Mode?](#q72-what-is-strict-mode) <span class="beginner">Beginner</span>
73. [How do you use Context API effectively?](#q73-how-do-you-use-context-api-effectively) <span class="intermediate">Intermediate</span>
74. [What is Hydration?](#q74-what-is-hydration) <span class="advanced">Advanced</span>
75. [How do you implement dark mode?](#q75-how-do-you-implement-dark-mode) <span class="intermediate">Intermediate</span>
76. [What is prop types?](#q76-what-is-prop-types) <span class="beginner">Beginner</span>
77. [How do you optimize Context re-renders?](#q77-how-do-you-optimize-context-re-renders) <span class="advanced">Advanced</span>
78. [React Server Components vs Client Components?](#q78-react-server-components-vs-client-components) <span class="advanced">Advanced</span>
79. [How do you handle images in React?](#q79-how-do-you-handle-images-in-react) <span class="beginner">Beginner</span>
80. [What is the Virtual DOM?](#q80-what-is-the-virtual-dom) <span class="beginner">Beginner</span>
81. [How do you implement authentication in React?](#q81-how-do-you-implement-authentication-in-react) <span class="intermediate">Intermediate</span>
82. [How do you handle multiple environments?](#q82-how-do-you-handle-multiple-environments) <span class="intermediate">Intermediate</span>
83. [How do you debug performance issues?](#q83-how-do-you-debug-performance-issues) <span class="intermediate">Intermediate</span>
84. [What is Render Props pattern?](#q84-what-is-render-props-pattern) <span class="intermediate">Intermediate</span>
85. [How do you create a compound component?](#q85-how-do-you-create-a-compound-component) <span class="advanced">Advanced</span>
86. [How do you manage global state without Redux?](#q86-how-do-you-manage-global-state-without-redux) <span class="intermediate">Intermediate</span>
87. [How do you implement infinite scroll?](#q87-how-do-you-implement-infinite-scroll) <span class="intermediate">Intermediate</span>
88. [How do you secure React apps?](#q88-how-do-you-secure-react-apps) <span class="intermediate">Intermediate</span>
89. [How do you unit test hooks?](#q89-how-do-you-unit-test-hooks) <span class="intermediate">Intermediate</span>
90. [What is `flushSync`?](#q90-what-is-flushsync) <span class="advanced">Advanced</span>
91. [How do you handle race conditions in useEffect?](#q91-how-do-you-handle-race-conditions-in-useeffect) <span class="advanced">Advanced</span>
92. [What is `dangerouslySetInnerHTML`?](#q92-what-is-dangerouslysetinnerhtml) <span class="beginner">Beginner</span>
93. [How do you implement drag and drop?](#q93-how-do-you-implement-drag-and-drop) <span class="intermediate">Intermediate</span>
94. [How do you handle file uploads in React?](#q94-how-do-you-handle-file-uploads-in-react) <span class="intermediate">Intermediate</span>
95. [How do you implement a carousel?](#q95-how-do-you-implement-a-carousel) <span class="intermediate">Intermediate</span>
96. [How do you mock API calls in tests?](#q96-how-do-you-mock-api-calls-in-tests) <span class="intermediate">Intermediate</span>
97. [What is `React.memo`?](#q97-what-is-react.memo) <span class="beginner">Beginner</span>
98. [How do you implement a tooltip?](#q98-how-do-you-implement-a-tooltip) <span class="intermediate">Intermediate</span>
99. [How do you handle window resize events?](#q99-how-do-you-handle-window-resize-events) <span class="intermediate">Intermediate</span>
100. [How do you implement A/B testing?](#q100-how-do-you-implement-ab-testing) <span class="intermediate">Intermediate</span>

---

### Q1: How do you implement a custom hook `useFetch` with caching and cancellation?

**Difficulty**: Intermediate

**Strategy:**
Creating a robust `useFetch` hook involves handling loading states, errors, data caching to avoid redundant requests, and request cancellation to prevent memory leaks or state updates on unmounted components.

**Key Features:**
1.  **Loading & Error States:** Standard state management for async operations.
2.  **Caching:** Using `useRef` to store responses keyed by URL.
3.  **Cancellation:** Using `AbortController` to cancel pending requests if the component unmounts or the URL changes.


**Code Example**:
```javascript
import { useState, useEffect, useRef } from 'react';

function useFetch(url, options = {}) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  
  // Use useRef for cache to persist data across renders without causing re-renders
  const cache = useRef({});

  useEffect(() => {
    if (!url) return;

    // Check cache first
    if (cache.current[url]) {
      setData(cache.current[url]);
      return;
    }

    const abortController = new AbortController();
    const signal = abortController.signal;

    const fetchData = async () => {
      setLoading(true);
      setError(null);
      
      try {
        const response = await fetch(url, { ...options, signal });
        
        if (!response.ok) {
          throw new Error(`Error: ${response.statusText}`);
        }
        
        const result = await response.json();
        
        // Update cache
        cache.current[url] = result;
        
        // Only update state if not aborted
        if (!signal.aborted) {
          setData(result);
        }
      } catch (err) {
        if (!signal.aborted) {
          setError(err.message);
        }
      } finally {
        if (!signal.aborted) {
          setLoading(false);
        }
      }
    };

    fetchData();

    // Cleanup function to abort fetch on unmount or dependency change
    return () => {
      abortController.abort();
    };
  }, [url]); // Re-run effect if URL changes

  return { data, loading, error };
}
```

---

### Q2: How do you optimize a React application using `useMemo` and `useCallback` correctly?

**Difficulty**: Intermediate

**Strategy:**
`useMemo` and `useCallback` are hooks for memoization, but they should be used judiciously. Overusing them can add overhead. They are most effective when performing expensive calculations or preserving referential equality for child components wrapped in `React.memo`.

**Usage:**
*   **`useMemo`**: Memoizes a *value*. Use it for expensive calculations (e.g., filtering large arrays) or to ensure an object/array dependency in `useEffect` remains stable.
*   **`useCallback`**: Memoizes a *function*. Use it when passing functions to optimized child components (`React.memo`) to prevent them from re-rendering due to a new function reference.


**Code Example**:
```javascript
import React, { useState, useMemo, useCallback } from 'react';

// A child component optimized with React.memo
const Child = React.memo(({ onClick, data }) => {
  console.log('Child rendered');
  return <button onClick={onClick}>{data.label}</button>;
});

function Parent() {
  const [count, setCount] = useState(0);
  const [text, setText] = useState('');

  // Expensive calculation: only re-runs if 'count' changes
  const expensiveValue = useMemo(() => {
    console.log('Computing expensive value...');
    return count * 2; // Imagine a heavy loop here
  }, [count]);

  // Function memoization: 'handleClick' reference stays the same unless dependencies change
  // Essential for passing to React.memo components
  const handleClick = useCallback(() => {
    console.log('Button clicked:', count);
  }, [count]);

  // Object memoization: prevents 'childData' from being a new reference on every render
  const childData = useMemo(() => ({ label: 'Click Me' }), []);

  return (
    <div>
      <h1>Count: {count}</h1>
      <h2>Double: {expensiveValue}</h2>
      <button onClick={() => setCount(c => c + 1)}>Increment</button>
      
      <input value={text} onChange={e => setText(e.target.value)} placeholder="Type something..." />
      
      {/* Child won't re-render when 'text' changes, thanks to memo/useCallback */}
      <Child onClick={handleClick} data={childData} />
    </div>
  );
}
```

---

### Q3: How do you manage global state using React Context without triggering unnecessary re-renders?

**Difficulty**: Intermediate

**Strategy:**
A common pitfall with React Context is that updating the context value causes *all* consuming components to re-render, even if they only use a part of the data.

**Strategies to avoid re-renders:**
1.  **Split Contexts:** Separate state into different contexts (e.g., `AuthContext`, `ThemeContext`) so updates in one don't affect consumers of the other.
2.  **Memoize the Value:** Wrap the context value object in `useMemo` so the reference remains stable unless state changes.
3.  **Context Selectors (Third-party):** Libraries like `use-context-selector` allow components to listen to only slices of the context.


**Code Example**:
```javascript
import React, { createContext, useContext, useState, useMemo } from 'react';

const AuthContext = createContext();
const ThemeContext = createContext();

export function AppProvider({ children }) {
  const [user, setUser] = useState(null);
  const [theme, setTheme] = useState('light');

  // Memoize auth value to prevent unnecessary re-renders if only theme changes
  const authValue = useMemo(() => ({ user, setUser }), [user]);
  
  // Memoize theme value
  const themeValue = useMemo(() => ({ theme, setTheme }), [theme]);

  return (
    <AuthContext.Provider value={authValue}>
      <ThemeContext.Provider value={themeValue}>
        {children}
      </ThemeContext.Provider>
    </AuthContext.Provider>
  );
}

// Custom hooks for consumption
export const useAuth = () => useContext(AuthContext);
export const useTheme = () => useContext(ThemeContext);
```

---

### Q4: How do you implement a Compound Component pattern (e.g., Tabs)?

**Difficulty**: Intermediate

**Strategy:**
Compound Components allow you to create flexible components where the parent manages the state, and children communicate with the parent implicitly. This avoids "prop explosion" where the parent needs dozens of props to configure internal children.

**Implementation:**
Use `React.Children.map` or `React.Context` to share state between the parent (`Tabs`) and children (`Tab`, `TabPanel`). Context is the modern and more flexible approach.


**Code Example**:
```javascript
import React, { createContext, useContext, useState } from 'react';

const TabsContext = createContext();

function Tabs({ children, defaultIndex = 0 }) {
  const [activeIndex, setActiveIndex] = useState(defaultIndex);

  return (
    <TabsContext.Provider value={{ activeIndex, setActiveIndex }}>
      <div className="tabs">{children}</div>
    </TabsContext.Provider>
  );
}

function TabList({ children }) {
  return <div className="tab-list">{children}</div>;
}

function Tab({ index, children }) {
  const { activeIndex, setActiveIndex } = useContext(TabsContext);
  const isActive = activeIndex === index;

  return (
    <button
      className={`tab ${isActive ? 'active' : ''}`}
      onClick={() => setActiveIndex(index)}
    >
      {children}
    </button>
  );
}

function TabPanel({ index, children }) {
  const { activeIndex } = useContext(TabsContext);
  return activeIndex === index ? <div className="tab-panel">{children}</div> : null;
}

// Usage
function App() {
  return (
    <Tabs defaultIndex={0}>
      <TabList>
        <Tab index={0}>Profile</Tab>
        <Tab index={1}>Settings</Tab>
      </TabList>
      <TabPanel index={0}>User Profile Content</TabPanel>
      <TabPanel index={1}>User Settings Content</TabPanel>
    </Tabs>
  );
}
```

---

### Q5: How do you create a Higher-Order Component (HOC) for authentication?

**Difficulty**: Intermediate

**Strategy:**
A Higher-Order Component (HOC) is a function that takes a component and returns a new component. It's a pattern for reusing component logic. While Hooks have replaced HOCs for many use cases (like data fetching), HOCs are still useful for wrapping components with cross-cutting concerns like authentication or layout injection.


**Code Example**:
```javascript
import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom'; // Assuming react-router

// HOC definition
function withAuth(WrappedComponent) {
  return function AuthComponent(props) {
    const navigate = useNavigate();
    // In a real app, check from context or localStorage
    const isAuthenticated = localStorage.getItem('token');

    useEffect(() => {
      if (!isAuthenticated) {
        navigate('/login');
      }
    }, [isAuthenticated, navigate]);

    if (!isAuthenticated) {
      return null; // Or a loading spinner
    }

    // Pass through props
    return <WrappedComponent {...props} />;
  };
}

// Usage
function Dashboard() {
  return <h1>Private Dashboard</h1>;
}

const ProtectedDashboard = withAuth(Dashboard);

export default ProtectedDashboard;
```

---

### Q6: How do you implement the Render Props pattern for code reuse?

**Difficulty**: Intermediate

**Strategy:**
Render Props refers to a technique for sharing code between React components using a prop whose value is a function. This function returns a React element. It allows the internal state of a component to be exposed to the parent, giving the parent full control over the UI.


**Code Example**:
```javascript
import React, { useState } from 'react';

// Reusable logic component
function MouseTracker({ render }) {
  const [position, setPosition] = useState({ x: 0, y: 0 });

  const handleMouseMove = (event) => {
    setPosition({
      x: event.clientX,
      y: event.clientY
    });
  };

  return (
    <div style={{ height: '100vh' }} onMouseMove={handleMouseMove}>
      {/* Call the render prop with the state */}
      {render(position)}
    </div>
  );
}

// Usage
function App() {
  return (
    <MouseTracker
      render={({ x, y }) => (
        <h1>
          The mouse position is ({x}, {y})
        </h1>
      )}
    />
  );
}
```

---

### Q7: How do you implement an Error Boundary to catch crashes in child components?

**Difficulty**: Intermediate

**Strategy:**
Error Boundaries are React components that catch JavaScript errors anywhere in their child component tree, log those errors, and display a fallback UI instead of the component tree that crashed. They must be implemented as **Class Components** because functional components do not yet support `getDerivedStateFromError` or `componentDidCatch`.


**Code Example**:
```javascript
import React from 'react';

class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  // Update state so the next render shows the fallback UI
  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  // You can also log the error to an error reporting service
  componentDidCatch(error, errorInfo) {
    console.error("Uncaught error:", error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return this.props.fallback || <h1>Something went wrong.</h1>;
    }

    return this.props.children;
  }
}

// Usage
function BuggyComponent() {
  throw new Error("I crashed!");
}

function App() {
  return (
    <ErrorBoundary fallback={<h1>Sorry, the widget crashed!</h1>}>
      <BuggyComponent />
    </ErrorBoundary>
  );
}
```

---

### Q8: How do you use `useImperativeHandle` to expose child methods to a parent?

**Difficulty**: Intermediate

**Strategy:**
`useImperativeHandle` customizes the instance value that is exposed to parent components when using `ref`. It is rarely used but helpful when you need to imperatively control a child (e.g., focus an input, scroll to a node, or trigger a child method) from the parent. It must be used with `forwardRef`.


**Code Example**:
```javascript
import React, { useRef, useImperativeHandle, forwardRef } from 'react';

const CustomInput = forwardRef((props, ref) => {
  const inputRef = useRef();

  useImperativeHandle(ref, () => ({
    focus: () => {
      inputRef.current.focus();
    },
    clear: () => {
      inputRef.current.value = '';
    }
  }));

  return <input ref={inputRef} {...props} />;
});

function App() {
  const childRef = useRef();

  return (
    <div>
      <CustomInput ref={childRef} />
      <button onClick={() => childRef.current.focus()}>Focus Input</button>
      <button onClick={() => childRef.current.clear()}>Clear Input</button>
    </div>
  );
}
```

---

### Q9: How do you implement a Portal to render children into a different part of the DOM?

**Difficulty**: Intermediate

**Strategy:**
Portals provide a way to render children into a DOM node that exists outside the DOM hierarchy of the parent component. This is commonly used for Modals, Tooltips, and Popovers to ensure they appear visually "on top" of other elements and aren't affected by parent CSS (like `overflow: hidden` or `z-index`).


**Code Example**:
```javascript
import React from 'react';
import ReactDOM from 'react-dom';

function Modal({ children, onClose }) {
  // Ensure this element exists in your index.html (e.g., <div id="modal-root"></div>)
  const modalRoot = document.getElementById('modal-root') || document.body;

  return ReactDOM.createPortal(
    <div style={overlayStyle}>
      <div style={modalStyle}>
        {children}
        <button onClick={onClose}>Close</button>
      </div>
    </div>,
    modalRoot
  );
}

// Styles
const overlayStyle = {
  position: 'fixed', top: 0, left: 0, right: 0, bottom: 0,
  backgroundColor: 'rgba(0,0,0,0.7)', zIndex: 1000
};

const modalStyle = {
  padding: '20px', background: '#fff', margin: '100px auto',
  width: '300px', borderRadius: '8px'
};

// Usage
function App() {
  const [isOpen, setIsOpen] = React.useState(false);
  return (
    <div style={{ overflow: 'hidden' }}>
      <button onClick={() => setIsOpen(true)}>Open Modal</button>
      {isOpen && (
        <Modal onClose={() => setIsOpen(false)}>
          <h2>I am a Portal!</h2>
        </Modal>
      )}
    </div>
  );
}
```

---

### Q10: How do you optimize large lists using Virtualization (Windowing)?

**Difficulty**: Intermediate

**Strategy:**
Virtualization (or Windowing) renders only the items currently visible in the viewport (plus a small buffer), rather than the entire list of thousands of items. This drastically reduces the number of DOM nodes and improves performance. Libraries like `react-window` or `react-virtualized` are standard.

**Implementation (Manual Concept):**
To implement it manually, you need to calculate which items overlap with the scroll container's viewport.


**Code Example**:
```javascript
import React, { useState } from 'react';

// Simple Fixed Height Virtual List
const VirtualList = ({ items, itemHeight, windowHeight }) => {
  const [scrollTop, setScrollTop] = useState(0);

  const totalHeight = items.length * itemHeight;
  
  // Calculate start and end indices
  const startIndex = Math.floor(scrollTop / itemHeight);
  const endIndex = Math.min(
    items.length - 1,
    Math.floor((scrollTop + windowHeight) / itemHeight)
  );

  const visibleItems = [];
  for (let i = startIndex; i <= endIndex; i++) {
    visibleItems.push(
      <div
        key={i}
        style={{
          position: 'absolute',
          top: `${i * itemHeight}px`,
          height: `${itemHeight}px`,
          width: '100%'
        }}
      >
        {items[i]}
      </div>
    );
  }

  return (
    <div
      onScroll={(e) => setScrollTop(e.target.scrollTop)}
      style={{ height: `${windowHeight}px`, overflowY: 'auto', position: 'relative' }}
    >
      <div style={{ height: `${totalHeight}px` }}>
        {visibleItems}
      </div>
    </div>
  );
};

// Usage
const items = Array.from({ length: 1000 }, (_, i) => `Item ${i + 1}`);

function App() {
  return <VirtualList items={items} itemHeight={35} windowHeight={300} />;
}
```

---

### Q11: How do you implement a custom `useDebounce` hook?

**Difficulty**: Intermediate

**Strategy:**
A `useDebounce` hook is useful for delaying a value update until a specified time has passed since the last change. It's commonly used for search inputs to avoid making an API call on every keystroke.


**Code Example**:
```javascript
import { useState, useEffect } from 'react';

function useDebounce(value, delay) {
  const [debouncedValue, setDebouncedValue] = useState(value);

  useEffect(() => {
    // Set a timeout to update the debounced value after the delay
    const handler = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);

    // Cleanup: Clear the timeout if value changes (resetting the timer)
    // or if the component unmounts
    return () => {
      clearTimeout(handler);
    };
  }, [value, delay]);

  return debouncedValue;
}

// Usage
function SearchComponent() {
  const [text, setText] = useState('');
  const debouncedText = useDebounce(text, 500);

  useEffect(() => {
    if (debouncedText) {
      console.log('API Call for:', debouncedText);
    }
  }, [debouncedText]);

  return <input value={text} onChange={(e) => setText(e.target.value)} />;
}
```

---

### Q12: How do you implement a custom `useLocalStorage` hook?

**Difficulty**: Intermediate

**Strategy:**
This hook syncs a state variable with `localStorage` so that data persists across browser refreshes. It also listens for changes to keep the state in sync.


**Code Example**:
```javascript
import { useState, useEffect } from 'react';

function useLocalStorage(key, initialValue) {
  // Initialize state function to run only once
  const [storedValue, setStoredValue] = useState(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      console.error(error);
      return initialValue;
    }
  });

  // Return a wrapped version of useState's setter function that persists data
  const setValue = (value) => {
    try {
      // Allow value to be a function so we have same API as useState
      const valueToStore = value instanceof Function ? value(storedValue) : value;
      setStoredValue(valueToStore);
      window.localStorage.setItem(key, JSON.stringify(valueToStore));
    } catch (error) {
      console.error(error);
    }
  };

  return [storedValue, setValue];
}
```

---

### Q13: How do you implement a custom `usePrevious` hook?

**Difficulty**: Intermediate

**Strategy:**
`usePrevious` is used to hold the value of a prop or state from the *previous* render. This is useful for comparing old and new values in effects.


**Code Example**:
```javascript
import { useRef, useEffect } from 'react';

function usePrevious(value) {
  const ref = useRef();

  // Store current value in ref
  useEffect(() => {
    ref.current = value;
  }, [value]); // Runs AFTER render

  // Return previous value (happens before update in useEffect)
  return ref.current;
}

// Usage
function Counter() {
  const [count, setCount] = useState(0);
  const prevCount = usePrevious(count);

  return (
    <h1>
      Now: {count}, Before: {prevCount}
    </h1>
  );
}
```

---

### Q14: What is the difference between `useEffect` and `useLayoutEffect`?

**Difficulty**: Intermediate

**Strategy:**
Both hooks run side effects, but the timing differs:
*   **`useEffect`**: Runs **asynchronously** *after* the browser has painted the screen. This is good for data fetching, subscriptions, and non-blocking updates. It doesn't block the UI.
*   **`useLayoutEffect`**: Runs **synchronously** *after* DOM mutations but *before* the browser paints. Use this if you need to measure DOM elements (width, height) and update state immediately to prevent a visual flicker.

**Visual Example:**
If you set state in `useEffect` that changes layout, the user might see the initial layout, then a flicker as it updates. With `useLayoutEffect`, the update happens before the paint, so no flicker occurs.


**Code Example**:
```javascript
import React, { useLayoutEffect, useRef, useState } from 'react';

function Tooltip() {
  const [height, setHeight] = useState(0);
  const ref = useRef(null);

  useLayoutEffect(() => {
    if (ref.current) {
      const { height } = ref.current.getBoundingClientRect();
      setHeight(height);
    }
  }, []); // Runs before paint

  return (
    <div>
      <div ref={ref}>Content that determines height</div>
      <p>Height is: {height}px</p>
    </div>
  );
}
```

---

### Q15: How do you use `forwardRef` to pass refs to child components?

**Difficulty**: Intermediate

**Strategy:**
By default, `ref`s are not passed to functional components. `forwardRef` allows a component to take a `ref` attribute and "forward" it to one of its children (usually a DOM element).


**Code Example**:
```javascript
import React, { forwardRef, useRef } from 'react';

// Child component capable of receiving a ref
const CustomButton = forwardRef((props, ref) => (
  <button ref={ref} className="btn">
    {props.children}
  </button>
));

function App() {
  const buttonRef = useRef(null);

  const clickHandler = () => {
    buttonRef.current.focus();
    buttonRef.current.innerText = "Clicked!";
  };

  return (
    <div>
      <CustomButton ref={buttonRef}>Click Me</CustomButton>
      <button onClick={clickHandler}>Focus the Custom Button</button>
    </div>
  );
}
```

---

### Q16: Controlled vs Uncontrolled Components: When to use which?

**Difficulty**: Intermediate

**Strategy:**
*   **Controlled Components:** React manages the state. The input value is driven by state (`value={state}`) and changes via `onChange`.
    *   *Pros:* Instant validation, conditional disabling, consistent state.
    *   *Cons:* More boilerplate, re-renders on every keystroke.
*   **Uncontrolled Components:** The DOM manages the state. You access the value using a `ref`.
    *   *Pros:* Easier to integrate with non-React code, less re-rendering.
    *   *Cons:* Harder to validate conditionally as you type.

**Recommendation:** Use Controlled for most forms. Use Uncontrolled for simple inputs or file uploads where React doesn't need to know the value instantly.


**Code Example**:
```javascript
// Controlled
function ControlledInput() {
  const [val, setVal] = useState("");
  return <input value={val} onChange={e => setVal(e.target.value)} />;
}

// Uncontrolled
function UncontrolledInput() {
  const inputRef = useRef();
  const handleSubmit = () => alert(inputRef.current.value);
  return (
    <div>
      <input ref={inputRef} />
      <button onClick={handleSubmit}>Submit</button>
    </div>
  );
}
```

---

### Q17: How do you use `React.memo` to prevent re-renders?

**Difficulty**: Intermediate

**Strategy:**
`React.memo` is a higher-order component that memoizes a functional component. It checks if the *props* have changed. If props are the same (shallow comparison), it skips re-rendering the component.

**Warning:** Don't wrap everything in `memo`. Use it only for pure components that render often with the same props.


**Code Example**:
```javascript
import React, { useState } from 'react';

const Movie = React.memo(({ title, releaseDate }) => {
  console.log(`Rendering Movie: ${title}`);
  return (
    <div>
      <h3>{title}</h3>
      <p>Release: {releaseDate}</p>
    </div>
  );
});

function App() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <button onClick={() => setCount(c => c + 1)}>Count: {count}</button>
      {/* Movie will NOT re-render when count changes */}
      <Movie title="Inception" releaseDate="2010" />
    </div>
  );
}
```

---

### Q18: How do you implement Code Splitting using `React.lazy` and `Suspense`?

**Difficulty**: Intermediate

**Strategy:**
Code splitting allows you to split your bundle into smaller chunks which can then be loaded on demand. This improves the initial load time. `React.lazy` lets you define a component that is loaded dynamically, and `Suspense` lets you show a fallback (like a spinner) while it's loading.


**Code Example**:
```javascript
import React, { Suspense } from 'react';

// Lazy load the component
const HeavyWidget = React.lazy(() => import('./HeavyWidget'));

function App() {
  return (
    <div>
      <h1>Dashboard</h1>
      
      {/* Show "Loading..." while HeavyWidget bundle is fetched */}
      <Suspense fallback={<div>Loading widget...</div>}>
        <HeavyWidget />
      </Suspense>
    </div>
  );
}
```

---

### Q19: How do you handle forms efficiently using React Hook Form?

**Difficulty**: Intermediate

**Strategy:**
`React Hook Form` is a popular library that uses *uncontrolled components* (refs) to handle form state, resulting in significantly fewer re-renders compared to controlled components. It provides easy validation and error handling.


**Code Example**:
```javascript
import React from 'react';
import { useForm } from 'react-hook-form';

function LoginForm() {
  const { register, handleSubmit, formState: { errors } } = useForm();

  const onSubmit = (data) => {
    console.log("Form Data:", data);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <div>
        <label>Username</label>
        {/* Register the input with validation rules */}
        <input {...register("username", { required: "Username is required" })} />
        {errors.username && <p>{errors.username.message}</p>}
      </div>

      <div>
        <label>Email</label>
        <input 
          {...register("email", { 
            required: "Email is required",
            pattern: { value: /^\S+@\S+$/i, message: "Invalid email" }
          })} 
        />
        {errors.email && <p>{errors.email.message}</p>}
      </div>

      <button type="submit">Login</button>
    </form>
  );
}
```

---

### Q20: How do you manage state with Redux Toolkit (Slice + Thunk)?

**Difficulty**: Intermediate

**Strategy:**
Redux Toolkit (RTK) simplifies Redux. A "Slice" contains the reducer logic and actions. `createAsyncThunk` handles async logic.


**Code Example**:
```javascript
// features/userSlice.js
import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';

// Async Thunk
export const fetchUser = createAsyncThunk('user/fetch', async (userId) => {
  const response = await fetch(`/api/user/${userId}`);
  return await response.json();
});

const userSlice = createSlice({
  name: 'user',
  initialState: { data: null, status: 'idle' },
  reducers: {
    logout: (state) => { state.data = null; }
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchUser.pending, (state) => { state.status = 'loading'; })
      .addCase(fetchUser.fulfilled, (state, action) => {
        state.status = 'succeeded';
        state.data = action.payload;
      });
  }
});

export const { logout } = userSlice.actions;
export default userSlice.reducer;

// Component
import { useDispatch, useSelector } from 'react-redux';
import { useEffect } from 'react';

function UserProfile({ id }) {
  const dispatch = useDispatch();
  const { data, status } = useSelector((state) => state.user);

  useEffect(() => {
    dispatch(fetchUser(id));
  }, [dispatch, id]);

  if (status === 'loading') return <p>Loading...</p>;
  return <div>{data?.name}</div>;
}
```

---

### Q21: How do you create a simple store using Zustand?

**Difficulty**: Intermediate

**Strategy:**
Zustand is a minimalistic state management library. It uses hooks and doesn't require a provider wrapper (unlike Context or Redux). It's great for avoiding boilerplate.


**Code Example**:
```javascript
import create from 'zustand';

// Create store
const useStore = create((set) => ({
  bears: 0,
  increasePopulation: () => set((state) => ({ bears: state.bears + 1 })),
  removeAllBears: () => set({ bears: 0 }),
}));

// Component
function BearCounter() {
  // Select state
  const bears = useStore((state) => state.bears);
  return <h1>{bears} around here...</h1>;
}

function Controls() {
  // Select actions
  const increase = useStore((state) => state.increasePopulation);
  return <button onClick={increase}>One up</button>;
}
```

---

### Q22: How do you implement Private Routes for authentication?

**Difficulty**: Intermediate

**Strategy:**
Private routes prevent unauthenticated users from accessing certain pages. In React Router v6, this is done by creating a wrapper component that checks for a token/user and redirects if missing.


**Code Example**:
```javascript
import { Navigate, Outlet } from 'react-router-dom';

const useAuth = () => {
  const user = localStorage.getItem('user');
  return user ? true : false;
};

function PrivateRoutes() {
  const isAuth = useAuth();
  // If authorized, render child routes (Outlet), else redirect to login
  return isAuth ? <Outlet /> : <Navigate to="/login" />;
}

// App.js
import { BrowserRouter, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />} />
        
        {/* Protected Routes */}
        <Route element={<PrivateRoutes />}>
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/settings" element={<Settings />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}
```

---

### Q23: How do you handle JWT Authentication (Login/Logout)?

**Difficulty**: Intermediate

**Strategy:**
Handling JWT involves sending credentials, storing the received token (usually `localStorage` or HttpOnly cookies), and attaching it to subsequent requests.


**Code Example**:
```javascript
// api.js
export const login = async (credentials) => {
  const res = await fetch('/api/login', {
    method: 'POST',
    body: JSON.stringify(credentials),
    headers: { 'Content-Type': 'application/json' }
  });
  const data = await res.json();
  if (data.token) {
    localStorage.setItem('token', data.token);
  }
  return data;
};

export const getProtectedData = async () => {
  const token = localStorage.getItem('token');
  const res = await fetch('/api/protected', {
    headers: {
      'Authorization': `Bearer ${token}`
    }
  });
  return res.json();
};

export const logout = () => {
  localStorage.removeItem('token');
  window.location.href = '/login';
};
```

---

### Q24: How do you unit test a React component using Jest and React Testing Library?

**Difficulty**: Intermediate

**Strategy:**
React Testing Library focuses on testing behavior from the user's perspective (clicking, seeing text) rather than implementation details (state, props).


**Code Example**:
```javascript
// Counter.js
import { useState } from 'react';
export default function Counter() {
  const [count, setCount] = useState(0);
  return (
    <div>
      <p data-testid="count-value">{count}</p>
      <button onClick={() => setCount(c => c + 1)}>Increment</button>
    </div>
  );
}

// Counter.test.js
import { render, screen, fireEvent } from '@testing-library/react';
import Counter from './Counter';

test('increments counter on click', () => {
  render(<Counter />);
  
  // Check initial state
  const countValue = screen.getByTestId('count-value');
  expect(countValue).toHaveTextContent('0');
  
  // Simulate click
  const button = screen.getByText('Increment');
  fireEvent.click(button);
  
  // Check updated state
  expect(countValue).toHaveTextContent('1');
});
```

---

### Q25: How do you mock API calls in Jest tests?

**Difficulty**: Intermediate

**Strategy:**
You should not make real network requests in tests. Instead, mock the `fetch` function or the module that makes the request.


**Code Example**:
```javascript
// UserList.js
import { useEffect, useState } from 'react';

export default function UserList() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch('/api/users')
      .then(res => res.json())
      .then(data => setUsers(data));
  }, []);

  return (
    <ul>
      {users.map(u => <li key={u.id}>{u.name}</li>)}
    </ul>
  );
}

// UserList.test.js
import { render, screen, waitFor } from '@testing-library/react';
import UserList from './UserList';

// Mock global fetch
global.fetch = jest.fn(() =>
  Promise.resolve({
    json: () => Promise.resolve([{ id: 1, name: 'John Doe' }]),
  })
);

test('renders users from API', async () => {
  render(<UserList />);

  // Wait for the element to appear
  const userItem = await waitFor(() => screen.getByText('John Doe'));
  
  expect(userItem).toBeInTheDocument();
  expect(fetch).toHaveBeenCalledTimes(1);
});
```

---

### Q26: How do you prevent XSS attacks in React?

**Difficulty**: Intermediate

**Strategy:**
Cross-Site Scripting (XSS) occurs when an attacker injects malicious scripts. React protects against XSS by default because it escapes data before rendering it. However, you are vulnerable if you use `dangerouslySetInnerHTML` or user-controlled `href` attributes.

**Best Practices:**
1.  Avoid `dangerouslySetInnerHTML`. If necessary, use a sanitization library like `dompurify`.
2.  Validate URLs in `<a>` tags (avoid `javascript:alert(1)`).


**Code Example**:
```javascript
import DOMPurify from 'dompurify';

function SafeContent({ htmlContent }) {
  // BAD: Vulnerable if htmlContent contains <script>
  // return <div dangerouslySetInnerHTML={{ __html: htmlContent }} />;

  // GOOD: Sanitize first
  const cleanHTML = DOMPurify.sanitize(htmlContent);
  
  return <div dangerouslySetInnerHTML={{ __html: cleanHTML }} />;
}
```

---

### Q27: How do you fix "Can't perform a React state update on an unmounted component"?

**Difficulty**: Intermediate

**Strategy:**
This warning occurs when an async operation (like `fetch` or `setTimeout`) completes and tries to call `setState` after the component has already unmounted.

**Fix:** Use a cleanup function in `useEffect` to cancel the operation or set a flag.


**Code Example**:
```javascript
useEffect(() => {
  let isMounted = true;

  fetchData().then(data => {
    if (isMounted) {
      setData(data);
    }
  });

  return () => {
    isMounted = false;
  };
}, []);
```
*Note: In modern React, strict mode often helps detect this, and using proper cancellation (like AbortController) is preferred over the `isMounted` flag.*

---

### Q28: How do you manage focus for accessibility (A11y)?

**Difficulty**: Intermediate

**Strategy:**
Managing focus is critical for keyboard navigation.
1.  **Auto-focus:** Use `ref.current.focus()` to move focus to a modal when it opens.
2.  **Focus Trap:** Keep focus inside a modal so Tab doesn't exit it.
3.  **Skip Links:** Allow users to skip navigation to main content.


**Code Example**:
```javascript
import { useEffect, useRef } from 'react';

function Modal({ isOpen, onClose, children }) {
  const modalRef = useRef();

  useEffect(() => {
    if (isOpen) {
      modalRef.current?.focus();
    }
  }, [isOpen]);

  if (!isOpen) return null;

  return (
    <div role="dialog" aria-modal="true">
      <div tabIndex={-1} ref={modalRef}>
        {children}
        <button onClick={onClose}>Close</button>
      </div>
    </div>
  );
}
```

---

### Q29: SSR vs CSR vs SSG: When to use what?

**Difficulty**: Intermediate

**Strategy:**
*   **CSR (Client-Side Rendering):** Standard React. Browser downloads empty HTML + JS bundle, then renders.
    *   *Use:* Dashboards, private apps behind login.
*   **SSR (Server-Side Rendering):** Server renders HTML on every request. (Next.js `getServerSideProps`).
    *   *Use:* Dynamic content needing SEO (e.g., Social Media feed).
*   **SSG (Static Site Generation):** HTML is built at **build time**. (Next.js `getStaticProps`).
    *   *Use:* Blogs, Marketing pages, Docs (Fastest performance).

---

### Q30: What is React Fiber and how does it improve performance?

**Difficulty**: Intermediate

**Strategy:**
React Fiber is the reimplementation of React's core reconciliation algorithm (introduced in React 16).
*   **Key Goal:** Incremental rendering. It can split rendering work into chunks and spread it out over multiple frames.
*   **Impact:** It allows React to pause work, reuse it, or abort it to prioritize higher-priority updates (like user input) over low-priority ones (like data fetching). This results in smoother animations and responsiveness.
*   **Features enabled by Fiber:** `Suspense`, `useTransition`, `Concurrency`.

### Q31: `useState` vs `useReducer`: When should you choose one over the other?

**Difficulty**: Intermediate

**Strategy:**
Use `useState` for simple, independent state values (strings, booleans). Use `useReducer` for complex state logic that involves multiple sub-values or when the next state depends on the previous one.

**Code Example:**
import React, { useReducer } from 'react';

const initialState = { count: 0 };

function reducer(state, action) {
  switch (action.type) {
    case 'increment':
      return { count: state.count + 1 };
    case 'decrement':
      return { count: state.count - 1 };
    default:
      throw new Error();
  }
}

function Counter() {
  const [state, dispatch] = useReducer(reducer, initialState);
  return (
    <>
      Count: {state.count}
      <button onClick={() => dispatch({ type: 'decrement' })}>-</button>
      <button onClick={() => dispatch({ type: 'increment' })}>+</button>
    </>
  );
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q32: How do you implement a custom hook `useOnClickOutside` to close modals?

**Difficulty**: Intermediate

**Strategy:**
This hook detects clicks outside a specified element (ref). It binds a `mousedown` or `touchstart` listener to the document and checks if the event target is contained within the ref element.

**Code Example:**
import { useEffect } from 'react';

function useOnClickOutside(ref, handler) {
  useEffect(() => {
    const listener = (event) => {
      // Do nothing if clicking ref's element or descendent elements
      if (!ref.current || ref.current.contains(event.target)) {
        return;
      }
      handler(event);
    };

    document.addEventListener('mousedown', listener);
    document.addEventListener('touchstart', listener);

    return () => {
      document.removeEventListener('mousedown', listener);
      document.removeEventListener('touchstart', listener);
    };
  }, [ref, handler]);
}

// Usage
// const ref = useRef();
// useOnClickOutside(ref, () => setModalOpen(false));
// <div ref={ref}>Modal Content</div>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q33: How do you implement a `useMediaQuery` hook for responsive designs?

**Difficulty**: Intermediate

**Strategy:**
This hook uses `window.matchMedia` to listen for media query changes and updates state accordingly.

**Code Example:**
import { useState, useEffect } from 'react';

function useMediaQuery(query) {
  const [matches, setMatches] = useState(false);

  useEffect(() => {
    const media = window.matchMedia(query);
    if (media.matches !== matches) {
      setMatches(media.matches);
    }

    const listener = () => setMatches(media.matches);
    media.addEventListener('change', listener);

    return () => media.removeEventListener('change', listener);
  }, [query]);

  return matches;
}

// Usage
// const isMobile = useMediaQuery('(max-width: 768px)');
// return <div>{isMobile ? 'Mobile View' : 'Desktop View'}</div>;

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q34: How do you make a custom button accessible using ARIA attributes?

**Difficulty**: Intermediate

**Strategy:**
When creating a non-native button (e.g., using a `div`), you must add `role='button'`, `tabIndex={0}` for keyboard focus, and handle `onKeyDown` for Enter/Space keys.

**Code Example:**
function AccessibleButton({ onClick, label }) {
  return (
    <div
      role="button"
      tabIndex={0}
      aria-label={label}
      onClick={onClick}
      onKeyDown={(e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault(); // Prevent scrolling for Space
          onClick();
        }
      }}
      style={{ cursor: 'pointer' }}
    >
      {label}
    </div>
  );
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q35: How do you profile a React application to identify performance bottlenecks?

**Difficulty**: Advanced

**Strategy:**
Use the React DevTools Profiler tab. It records rendering information, showing which components rendered, why they rendered (changed props/state), and how long it took.

**Code Example:**
// 1. Install React DevTools extension.
// 2. Open the 'Profiler' tab in Chrome DevTools.
// 3. Click 'Record' (blue circle).
// 4. Interact with your app.
// 5. Stop recording.

// Analysis:
// - Flamegraph: Shows the component tree. Width of bar = time taken to render. Color (yellow/red) = slow.
// - Ranked chart: Lists components by render time.
// - Why did this render?: Hover over a component to see changed props or hooks.

// Programmatic Profiling:
<Profiler id="Navigation" onRender={(id, phase, actualDuration) => {
  console.log({ id, phase, actualDuration });
}}>
  <Navigation />
</Profiler>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q36: How do you safely render HTML content to prevent XSS attacks?

**Difficulty**: Intermediate

**Strategy:**
React escapes content by default. If you must render raw HTML, use `dangerouslySetInnerHTML` but sanitize the content first using a library like `dompurify`.

**Code Example:**
import DOMPurify from 'dompurify';

function SafeHTML({ htmlContent }) {
  const sanitizedHTML = DOMPurify.sanitize(htmlContent);

  return (
    <div
      dangerouslySetInnerHTML={{ __html: sanitizedHTML }}
    />
  );
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q37: What is the difference between `fireEvent` and `userEvent` in React Testing Library?

**Difficulty**: Intermediate

**Strategy:**
`fireEvent` dispatches DOM events directly. `userEvent` simulates full user interactions (e.g., typing triggers focus, keydown, input, keyup, blur), making tests more realistic.

**Code Example:**
// fireEvent (Low-level)
fireEvent.change(input, { target: { value: 'hello' } });

// userEvent (Recommended - mimics real user behavior)
import userEvent from '@testing-library/user-event';

const user = userEvent.setup();
await user.type(input, 'hello'); // Triggers focus, keydown, input...
await user.click(button);

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q38: How do you handle errors in Functional Components (since they lack `componentDidCatch`)?

**Difficulty**: Intermediate

**Strategy:**
Use the `react-error-boundary` library, which provides a reusable `ErrorBoundary` component that works with functional components and hooks.

**Code Example:**
import { ErrorBoundary } from 'react-error-boundary';

function ErrorFallback({ error, resetErrorBoundary }) {
  return (
    <div role="alert">
      <p>Something went wrong:</p>
      <pre>{error.message}</pre>
      <button onClick={resetErrorBoundary}>Try again</button>
    </div>
  );
}

function App() {
  return (
    <ErrorBoundary
      FallbackComponent={ErrorFallback}
      onReset={() => {
        // Reset the state of your app so the error doesn't happen again
      }}
    >
      <MyComponent />
    </ErrorBoundary>
  );
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q39: What is Automatic Batching in React 18?

**Difficulty**: Advanced

**Strategy:**
Before React 18, updates inside promises, timeouts, or native event handlers were not batched. React 18 batches *all* state updates automatically, reducing re-renders.

**Code Example:**
// React 17: Renders twice
setTimeout(() => {
  setCount(c => c + 1);
  setFlag(f => !f);
}, 1000);

// React 18: Renders once (Automatic Batching)
setTimeout(() => {
  setCount(c => c + 1);
  setFlag(f => !f);
}, 1000);

// Opt-out (rarely needed):
import { flushSync } from 'react-dom';
flushSync(() => {
  setCount(c => c + 1); // Forces re-render immediately
});

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q40: How do you use `useTransition` to keep the UI responsive during heavy state updates?

**Difficulty**: Advanced

**Strategy:**
`useTransition` marks a state update as 'non-urgent' (transition). This allows the UI to remain responsive (e.g., typing in an input) while the heavy update (e.g., filtering a list) calculates in the background.

**Code Example:**
import { useState, useTransition } from 'react';

function App() {
  const [isPending, startTransition] = useTransition();
  const [input, setInput] = useState('');
  const [list, setList] = useState([]);

  const handleChange = (e) => {
    // Urgent: Update input immediately
    setInput(e.target.value);

    // Non-urgent: Filter list (can lag slightly)
    startTransition(() => {
      const filtered = largeList.filter(item => item.includes(e.target.value));
      setList(filtered);
    });
  };

  return (
    <div>
      <input value={input} onChange={handleChange} />
      {isPending ? <p>Loading list...</p> : <List items={list} />}
    </div>
  );
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q41: What is `useDeferredValue` and when should you use it?

**Difficulty**: Advanced

**Strategy:**
`useDeferredValue` accepts a value and returns a new copy of the value that will defer to more urgent updates. It's like debouncing but integrated with React's rendering cycle.

**Code Example:**
import { useState, useDeferredValue, useMemo } from 'react';

function App() {
  const [query, setQuery] = useState('');
  // The deferred query will lag behind the actual query if the UI is busy
  const deferredQuery = useDeferredValue(query);

  // Expensive list calculation only runs when deferredQuery catches up
  const list = useMemo(() => {
    return largeList.filter(item => item.includes(deferredQuery));
  }, [deferredQuery]);

  return (
    <>
      <input value={query} onChange={e => setQuery(e.target.value)} />
      <List items={list} />
    </>
  );
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q42: How does Suspense for Data Fetching work?

**Difficulty**: Advanced

**Strategy:**
Suspense allows components to 'suspend' rendering while waiting for an async operation (like fetching data) to complete. It requires a Suspense-enabled data fetching library (like Relay, SWR, or React Query's suspense mode).

**Code Example:**
import { Suspense } from 'react';

// Assume 'ProfileData' is a component that throws a promise while fetching
// This requires a library that supports Suspense for data fetching
function ProfilePage() {
  return (
    <Suspense fallback={<h1>Loading profile...</h1>}>
      <ProfileData />
      <Suspense fallback={<h1>Loading posts...</h1>}>
        <ProfilePosts />
      </Suspense>
    </Suspense>
  );
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q43: Why is using the array index as a key an anti-pattern?

**Difficulty**: Beginner

**Strategy:**
Using the index as a key can break your application and cause wrong data to be displayed if the list order changes (sorting, filtering, inserting). React uses keys to identify elements. If the index changes, React may reuse component state incorrectly.

**Code Example:**
// ❌ Bad: Index as key
{items.map((item, index) => (
  <li key={index}>{item.name}</li>
))}

// ✅ Good: Unique ID as key
{items.map((item) => (
  <li key={item.id}>{item.name}</li>
))}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q44: How do you solve Props Drilling without Context?

**Difficulty**: Intermediate

**Strategy:**
Use **Component Composition**. Instead of passing data down through intermediate components, pass the components themselves as `children` or props.

**Code Example:**
// ❌ Props Drilling
function App() {
  const user = { name: 'Alice' };
  return <Layout user={user} />;
}
function Layout({ user }) {
  return <Header user={user} />; // Layout doesn't need user
}
function Header({ user }) {
  return <div>Hello {user.name}</div>;
}

// ✅ Composition
function App() {
  const user = { name: 'Alice' };
  return (
    <Layout>
      <Header user={user} />
    </Layout>
  );
}
function Layout({ children }) {
  return <div>{children}</div>; // Layout is agnostic
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q45: What are Micro-frontends and how does Module Federation help?

**Difficulty**: Expert

**Strategy:**
Micro-frontends split a monolithic frontend into smaller, independently deployable apps. Webpack 5 Module Federation allows a JavaScript application to dynamically load code from another application at runtime.

**Code Example:**
// webpack.config.js (Host App)
const ModuleFederationPlugin = require("webpack/lib/container/ModuleFederationPlugin");

module.exports = {
  plugins: [
    new ModuleFederationPlugin({
      name: "host",
      remotes: {
        app1: "app1@http://localhost:3001/remoteEntry.js",
      },
    }),
  ],
};

// Usage in Host App
const RemoteApp1 = React.lazy(() => import("app1/App"));

function App() {
  return (
    <Suspense fallback="Loading App1...">
      <RemoteApp1 />
    </Suspense>
  );
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q46: How do you use Generics in TypeScript with React Props?

**Difficulty**: Intermediate

**Strategy:**
Generics allow you to create reusable components that work with different data types while maintaining type safety.

**Code Example:**
interface ListProps<T> {
  items: T[];
  renderItem: (item: T) => React.ReactNode;
}

function List<T>({ items, renderItem }: ListProps<T>) {
  return <ul>{items.map((item, i) => <li key={i}>{renderItem(item)}</li>)}</ul>;
}

// Usage
// <List<string> items={['a', 'b']} renderItem={(item) => <span>{item}</span>} />
// <List<number> items={[1, 2]} renderItem={(item) => <span>{item}</span>} />

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q47: How do you create Discriminated Unions for mutually exclusive props?

**Difficulty**: Advanced

**Strategy:**
Use a common literal type property (the discriminant) to distinguish between object types.

**Code Example:**
type ButtonProps = 
  | { variant: 'text'; text: string; icon?: never }
  | { variant: 'icon'; icon: string; text?: never };

function Button(props: ButtonProps) {
  if (props.variant === 'text') {
    return <button>{props.text}</button>;
  }
  return <button className="icon">{props.icon}</button>;
}

// Usage
// <Button variant="text" text="Click me" /> // ✅ Valid
// <Button variant="icon" icon="star" />     // ✅ Valid
// <Button variant="text" icon="star" />     // ❌ Error: Property 'icon' does not exist...

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q48: What does React Strict Mode do?

**Difficulty**: Beginner

**Strategy:**
`React.StrictMode` is a development-only tool that highlights potential problems. It intentionally double-invokes effects (mount -> unmount -> mount) to help find side effects and unsafe lifecycle methods.

**Code Example:**
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// In Dev:
// useEffect(() => console.log('mount'), []) 
// Logs: 'mount', 'mount' (to ensure your cleanup logic is correct)

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q49: How does Event Delegation work in React?

**Difficulty**: Advanced

**Strategy:**
React doesn't attach event handlers to the DOM nodes you create. Instead, it attaches a single event listener to the root element. When an event occurs, React maps it back to the correct component instance (Synthetic Events). This improves memory usage.

**Code Example:**
// JSX
<button onClick={handleClick}>Click</button>

// Real DOM (Simplified)
// <div id="root"></div> (Event Listener attached here)
//   <button>Click</button> (No individual listener)

// Event Bubble:
// Button Click -> Bubbles up to #root -> React catches it -> Calls handleClick

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q50: What is the React Reconciler?

**Difficulty**: Expert

**Strategy:**
The Reconciler is the engine that diffs the Virtual DOM. React Fiber is the current reconciliation engine (since v16). It enables features like pausing/aborting work, assigning priority to different updates, and reusing DOM elements.

**Code Example:**
// Reconciliation Process:
// 1. Render Phase: React calls your components and creates a Virtual DOM tree.
//    - This phase can be interrupted/paused (Fiber).
//    - Calculates changes (diffing).

// 2. Commit Phase: React applies the changes to the real DOM.
//    - This phase is synchronous and cannot be interrupted.
//    - Lifecycle methods like componentDidMount / useLayoutEffect run here.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---



### Q51: How does React Fiber improve performance?

**Difficulty**: Advanced

**Strategy**:
Fiber allows React to split rendering work into chunks and pause it to prioritize updates like user input. It uses a linked list tree traversal.

**Code Example**:
```javascript
// Conceptual Fiber Node
{
  stateNode: {},
  child: FiberNode,
  sibling: FiberNode,
  return: FiberNode
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q52: What is the difference between `useMemo` and `useCallback`?

**Difficulty**: Intermediate

**Strategy**:
`useMemo` caches the *result* of a function. `useCallback` caches the *function definition* itself.

**Code Example**:
```javascript
const memoizedValue = useMemo(() => compute(a, b), [a, b]);
const memoizedCallback = useCallback(() => doSomething(a, b), [a, b]);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q53: How do you implement an Error Boundary?

**Difficulty**: Intermediate

**Strategy**:
Class component with `static getDerivedStateFromError` and `componentDidCatch`. Hooks don't support this yet.

**Code Example**:
```javascript
class ErrorBoundary extends React.Component {
  static getDerivedStateFromError(error) { return { hasError: true }; }
  componentDidCatch(error, info) { logError(error, info); }
  render() { return this.state.hasError ? <h1>Error</h1> : this.props.children; }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q54: What is the purpose of `useLayoutEffect`?

**Difficulty**: Advanced

**Strategy**:
Fires synchronously after all DOM mutations. Use it to read layout from the DOM and re-render synchronously (prevent flickering).

**Code Example**:
```javascript
useLayoutEffect(() => {
  const rect = ref.current.getBoundingClientRect();
  setHeight(rect.height);
}, []);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q55: How do you use React Portals?

**Difficulty**: Intermediate

**Strategy**:
Render children into a DOM node that exists outside the DOM hierarchy of the parent component (e.g., Modals).

**Code Example**:
```javascript
return ReactDOM.createPortal(
  <div className="modal">{children}</div>,
  document.getElementById('modal-root')
);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q56: What is Suspense for Data Fetching?

**Difficulty**: Advanced

**Strategy**:
Allows components to 'wait' for something before rendering. Used with `React.lazy` or concurrent data fetching.

**Code Example**:
```javascript
<Suspense fallback={<Spinner />}>
  <ProfileDetails />
</Suspense>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q57: How do you prevent prop drilling?

**Difficulty**: Beginner

**Strategy**:
Use Context API, Composition (passing components as props), or State Management libraries.

**Code Example**:
```javascript
// Context approach
const UserContext = createContext();
<UserContext.Provider value={user}><App /></UserContext.Provider>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q58: What is `forwardRef` used for?

**Difficulty**: Intermediate

**Strategy**:
Forwarding a ref through a component to one of its children. Useful for reusable UI components.

**Code Example**:
```javascript
const FancyButton = React.forwardRef((props, ref) => (
  <button ref={ref} className="fancy-button">
    {props.children}
  </button>
));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q59: How do Custom Hooks share logic?

**Difficulty**: Beginner

**Strategy**:
They extract component logic into reusable functions. They can call other hooks.

**Code Example**:
```javascript
function useWindowSize() {
  const [size, setSize] = useState(window.innerWidth);
  useEffect(() => { /* listener */ }, []);
  return size;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q60: Difference between Controlled and Uncontrolled inputs?

**Difficulty**: Beginner

**Strategy**:
Controlled: React state drives the input value. Uncontrolled: DOM drives the value, accessed via ref.

**Code Example**:
```javascript
// Controlled
<input value={val} onChange={e => setVal(e.target.value)} />
// Uncontrolled
<input ref={inputRef} />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q61: How do you optimize a large list in React?

**Difficulty**: Intermediate

**Strategy**:
Virtualization (Windowing). Only render items currently in view.

**Code Example**:
```javascript
import { FixedSizeList } from 'react-window';
<FixedSizeList height={500} itemCount={1000} itemSize={35} ... />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q62: What is the key prop and why is it important?

**Difficulty**: Beginner

**Strategy**:
Helps React identify which items have changed, are added, or are removed. Must be unique among siblings.

**Code Example**:
```javascript
items.map(item => <li key={item.id}>{item.name}</li>)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q63: How do you handle side effects in React?

**Difficulty**: Beginner

**Strategy**:
Use `useEffect` hook. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
useEffect(() => {
  const id = setInterval(tick, 1000);
  return () => clearInterval(id);
}, []);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q64: What is Higher-Order Component (HOC)?

**Difficulty**: Advanced

**Strategy**:
A function that takes a component and returns a new component. Used for reusing component logic (e.g., authentication, logging).

**Code Example**:
```javascript
function withAuth(WrappedComponent) {
  return function(props) {
    return isAuthenticated ? <WrappedComponent {...props} /> : <Login />;
  };
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q65: How does `setState` batch updates?

**Difficulty**: Advanced

**Strategy**:
React groups multiple state updates into a single re-render for better performance. React 18 introduced Automatic Batching for promises and timeouts too.

**Code Example**:
```javascript
function handleClick() {
  setCount(c => c + 1);
  setFlag(f => !f);
  // Re-renders once, not twice
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q66: What is the Rules of Hooks?

**Difficulty**: Beginner

**Strategy**:
1. Only call Hooks at the top level (no loops, conditions, or nested functions).
2. Only call Hooks from React function components or custom Hooks.

**Code Example**:
```javascript
// ❌ Bad
if (condition) { useEffect(...) }

// ✅ Good
useEffect(() => {
  if (condition) { ... }
}, []);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q67: How do you test a React component?

**Difficulty**: Intermediate

**Strategy**:
Use **React Testing Library** to test interaction and **Jest** for assertions. Focus on user-centric testing (what user sees), not implementation details.

**Code Example**:
```javascript
test('renders button', () => {
  render(<Button />);
  expect(screen.getByRole('button')).toBeInTheDocument();
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q68: What is Code Splitting?

**Difficulty**: Intermediate

**Strategy**:
Splitting code into smaller bundles to load on demand. Implemented using `React.lazy()` and `Suspense` or dynamic imports in Webpack/Vite.

**Code Example**:
```javascript
const OtherComponent = React.lazy(() => import('./OtherComponent'));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q69: How do you handle forms in React?

**Difficulty**: Beginner

**Strategy**:
Use Controlled components (state) for simple forms, or `react-hook-form` (uncontrolled) for performance and complex validation.

**Code Example**:
```javascript
const { register, handleSubmit } = useForm();
<input {...register("firstName")} />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q70: What is Reconciliation?

**Difficulty**: Advanced

**Strategy**:
The process by which React updates the DOM. It compares the new Virtual DOM with the old one (diffing) and applies the minimal set of changes to the real DOM.

**Code Example**:
```javascript
// React compares element types.
// <div> -> <span> : Full rebuild.
// <div className="a"> -> <div className="b"> : Update attribute only.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q71: How do you force a re-render?

**Difficulty**: Intermediate

**Strategy**:
Ideally, you shouldn't. If needed, update a dummy state or use `useReducer`.

**Code Example**:
```javascript
const [, forceUpdate] = useReducer(x => x + 1, 0);
// Call forceUpdate() to re-render
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q72: What is Strict Mode?

**Difficulty**: Beginner

**Strategy**:
A tool for highlighting potential problems in an application. It activates additional checks and warnings for its descendants (e.g., double-invoking effects in dev).

**Code Example**:
```javascript
<React.StrictMode>
  <App />
</React.StrictMode>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q73: How do you use Context API effectively?

**Difficulty**: Intermediate

**Strategy**:
Use it for global data (theme, user, language). Avoid using it for high-frequency updates as it triggers re-renders in all consumers. Split contexts to optimize.

**Code Example**:
```javascript
const ThemeContext = createContext('light');
const theme = useContext(ThemeContext);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q74: What is Hydration?

**Difficulty**: Advanced

**Strategy**:
The process where React attaches event listeners to the HTML rendered by the server (SSR) to make it interactive.

**Code Example**:
```javascript
// Client-side
hydrateRoot(document.getElementById('root'), <App />);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q75: How do you implement dark mode?

**Difficulty**: Intermediate

**Strategy**:
Use a Context to hold the theme state. Toggle a CSS class on the `body` or root element, or use a `ThemeProvider` (Styled Components/Emotion).

**Code Example**:
```javascript
// In Context Provider
useEffect(() => {
  document.body.className = theme;
}, [theme]);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q76: What is prop types?

**Difficulty**: Beginner

**Strategy**:
Runtime type checking for React props. Less common now with TypeScript, but useful in JS projects.

**Code Example**:
```javascript
import PropTypes from 'prop-types';
MyComponent.propTypes = {
  name: PropTypes.string.isRequired
};
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q77: How do you optimize Context re-renders?

**Difficulty**: Advanced

**Strategy**:
Split context into State and Dispatch. Memoize the value passed to `Provider`.

**Code Example**:
```javascript
const value = useMemo(() => ({ state, dispatch }), [state]);
<Ctx.Provider value={value}>...</Ctx.Provider>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q78: React Server Components vs Client Components?

**Difficulty**: Advanced

**Strategy**:
Server Components run on the server (zero bundle size). Client Components run in the browser (interactivity).

**Code Example**:
```javascript
// Server Component (default in Next.js app dir)
async function getData() { ... }
export default async function Page() {
  const data = await getData();
  return <div>{data.title}</div>;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q79: How do you handle images in React?

**Difficulty**: Beginner

**Strategy**:
Import them or use the `public` folder. For optimization, use `<img loading="lazy" />` or Next.js `<Image />`.

**Code Example**:
```javascript
import logo from './logo.png';
<img src={logo} alt="Logo" />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q80: What is the Virtual DOM?

**Difficulty**: Beginner

**Strategy**:
A lightweight copy of the DOM in memory. React modifies this first, diffs it, and then updates the real DOM efficiently.

**Code Example**:
```javascript
// Conceptual Object
const vNode = {
  type: 'div',
  props: { className: 'container', children: 'Hello' }
};
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q81: How do you implement authentication in React?

**Difficulty**: Intermediate

**Strategy**:
Store JWT in localStorage/cookies. Use a Context to provide user state. specific `PrivateRoute` component to protect routes.

**Code Example**:
```javascript
const { user } = useAuth();
return user ? <Dashboard /> : <Navigate to="/login" />;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q82: How do you handle multiple environments?

**Difficulty**: Intermediate

**Strategy**:
Use `.env` files (`.env.development`, `.env.production`). Access via `process.env.REACT_APP_*` or `import.meta.env.VITE_*`.

**Code Example**:
```javascript
const apiUrl = import.meta.env.VITE_API_URL;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q83: How do you debug performance issues?

**Difficulty**: Intermediate

**Strategy**:
Use React DevTools **Profiler**. Look for unnecessary re-renders. Use `why-did-you-render` library.

**Code Example**:
```javascript
// wdyr.js
import React from 'react';
if (process.env.NODE_ENV === 'development') {
  const whyDidYouRender = require('@welldone-software/why-did-you-render');
  whyDidYouRender(React, { trackAllPureComponents: true });
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q84: What is Render Props pattern?

**Difficulty**: Intermediate

**Strategy**:
Passing a function as a prop to share code. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
<Mouse render={mouse => (
  <p>Mouse: {mouse.x}, {mouse.y}</p>
)}/>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q85: How do you create a compound component?

**Difficulty**: Advanced

**Strategy**:
Components that work together (like `<select>` and `<option>`). Use Context to share state implicitly.

**Code Example**:
```javascript
<Menu>
  <Menu.Button>Open</Menu.Button>
  <Menu.List>
    <Menu.Item>Copy</Menu.Item>
  </Menu.List>
</Menu>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q86: How do you manage global state without Redux?

**Difficulty**: Intermediate

**Strategy**:
Context API + `useReducer` for medium complexity. Zustand or Jotai for simpler, atomic state.

**Code Example**:
```javascript
// Zustand
const useStore = create(set => ({ count: 0, inc: () => set(s => ({ count: s.count + 1 })) }));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q87: How do you implement infinite scroll?

**Difficulty**: Intermediate

**Strategy**:
Use `IntersectionObserver` to detect when the user scrolls to the bottom, then fetch the next page.

**Code Example**:
```javascript
const { ref, inView } = useInView();
useEffect(() => {
  if (inView) loadMore();
}, [inView]);
return <div ref={ref}>Loading...</div>;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q88: How do you secure React apps?

**Difficulty**: Intermediate

**Strategy**:
1. Validate all inputs.
2. Sanitize HTML (`dompurify`).
3. Use HttpOnly cookies for tokens.
4. Implement CSP (Content Security Policy).

**Code Example**:
```javascript
// CSP Header in index.html meta tag
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; img-src https://*;" />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q89: How do you unit test hooks?

**Difficulty**: Intermediate

**Strategy**:
Use `renderHook` from `@testing-library/react`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const { result } = renderHook(() => useCounter());
act(() => result.current.increment());
expect(result.current.count).toBe(1);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q90: What is `flushSync`?

**Difficulty**: Advanced

**Strategy**:
Forces React to flush updates synchronously. Use sparingly, e.g., when you need to measure the DOM immediately after an update.

**Code Example**:
```javascript
flushSync(() => {
  setCount(c => c + 1);
});
// DOM is updated here
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q91: How do you handle race conditions in useEffect?

**Difficulty**: Advanced

**Strategy**:
Use a cleanup flag or AbortController to ignore results from stale requests.

**Code Example**:
```javascript
useEffect(() => {
  let active = true;
  fetch(url).then(data => {
    if (active) setData(data);
  });
  return () => { active = false; };
}, [url]);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q92: What is `dangerouslySetInnerHTML`?

**Difficulty**: Beginner

**Strategy**:
React's replacement for `innerHTML`. It reminds you that setting HTML directly is dangerous (XSS).

**Code Example**:
```javascript
<div dangerouslySetInnerHTML={{ __html: '<p>Hello</p>' }} />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q93: How do you implement drag and drop?

**Difficulty**: Intermediate

**Strategy**:
Use HTML5 Drag and Drop API or libraries like `dnd-kit` or `react-beautiful-dnd`.

**Code Example**:
```javascript
<div draggable onDragStart={e => e.dataTransfer.setData('text', 'id')} />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q94: How do you handle file uploads in React?

**Difficulty**: Intermediate

**Strategy**:
Use `input type="file"`. Access the file via `e.target.files[0]`. Use `FormData` to send it to the server.

**Code Example**:
```javascript
const handleUpload = (e) => {
  const file = e.target.files[0];
  const formData = new FormData();
  formData.append('file', file);
  fetch('/upload', { method: 'POST', body: formData });
};
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q95: How do you implement a carousel?

**Difficulty**: Intermediate

**Strategy**:
State tracks current index. `setInterval` for auto-play. CSS transform to slide.

**Code Example**:
```javascript
const [index, setIndex] = useState(0);
const next = () => setIndex((i + 1) % images.length);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q96: How do you mock API calls in tests?

**Difficulty**: Intermediate

**Strategy**:
Use `jest.spyOn(global, 'fetch')` or `msw` (Mock Service Worker) to intercept network requests.

**Code Example**:
```javascript
server.use(
  rest.get('/api/user', (req, res, ctx) => {
    return res(ctx.json({ name: 'John' }));
  })
);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q97: What is `React.memo`?

**Difficulty**: Beginner

**Strategy**:
Memoizes a component to prevent re-renders if props haven't changed.

**Code Example**:
```javascript
const MyComponent = React.memo(function MyComponent(props) {
  /* render using props */
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q98: How do you implement a tooltip?

**Difficulty**: Intermediate

**Strategy**:
Track hover state (`onMouseEnter`, `onMouseLeave`). Render a positioned div.

**Code Example**:
```javascript
{isHovered && <div className="tooltip">Info</div>}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q99: How do you handle window resize events?

**Difficulty**: Intermediate

**Strategy**:
`useEffect` to add `resize` listener. Update state. Debounce for performance.

**Code Example**:
```javascript
useEffect(() => {
  const handleResize = () => setWidth(window.innerWidth);
  window.addEventListener('resize', handleResize);
  return () => window.removeEventListener('resize', handleResize);
}, []);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q100: How do you implement A/B testing?

**Difficulty**: Intermediate

**Strategy**:
Use a Feature Flag service (LaunchDarkly) or random logic. Render different components based on the flag.

**Code Example**:
```javascript
const variant = useExperiment('new-signup-flow');
return variant === 'B' ? <SignupB /> : <SignupA />;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


**Strategy**:
A function that takes a component and returns a new component. Used for cross-cutting concerns.

**Code Example**:
```javascript
function withLogging(WrappedComponent) {
  return (props) => {
    useEffect(() => console.log('Mounted'), []);
    return <WrappedComponent {...props} />;
  };
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q65: How does `setState` batch updates?

**Difficulty**: Advanced

**Strategy**:
React batches multiple state updates into a single re-render for performance. In React 18, this is automatic even in promises/timeouts.

**Code Example**:
```javascript
handleClick() {
  setCount(c => c + 1);
  setFlag(f => !f);
  // Re-renders once
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q66: What is the Rules of Hooks?

**Difficulty**: Beginner

**Strategy**:
Only call Hooks at the top level. Only call Hooks from React functions.

**Code Example**:
```javascript
// ❌ Bad: inside condition
if (condition) useEffect(...)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q67: How do you test a React component?

**Difficulty**: Intermediate

**Strategy**:
Use React Testing Library (RTL). Test behavior, not implementation.

**Code Example**:
```javascript
render(<App />);
fireEvent.click(screen.getByText('Submit'));
expect(screen.getByText('Success')).toBeInTheDocument();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q68: What is Code Splitting?

**Difficulty**: Intermediate

**Strategy**:
Splitting bundle into smaller chunks to load on demand. Use `React.lazy` and dynamic `import()`.

**Code Example**:
```javascript
const OtherComponent = React.lazy(() => import('./OtherComponent'));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q69: How do you handle forms in React?

**Difficulty**: Beginner

**Strategy**:
Use local state or libraries like React Hook Form or Formik.

**Code Example**:
```javascript
const { register, handleSubmit } = useForm();
<form onSubmit={handleSubmit(onSubmit)}>
  <input {...register("firstName")} />
</form>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q70: What is Reconciliation?

**Difficulty**: Advanced

**Strategy**:
The process through which React updates the DOM. It compares the new element tree with the most recent one.

**Code Example**:
```javascript
// Diffing algorithm uses heuristics (type check, key check) to be O(n)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q71: How do you force a re-render?

**Difficulty**: Intermediate

**Strategy**:
Update state (dummy state) or use `useReducer`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const [, forceUpdate] = useReducer(x => x + 1, 0);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q72: What is Strict Mode?

**Difficulty**: Beginner

**Strategy**:
A tool for highlighting potential problems in an application. It activates additional checks and warnings.

**Code Example**:
```javascript
<React.StrictMode><App /></React.StrictMode>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q73: How do you use Context API effectively?

**Difficulty**: Intermediate

**Strategy**:
Split contexts to avoid unnecessary re-renders. Place providers close to where they are needed.

**Code Example**:
```javascript
const DispatchContext = createContext(null);
const StateContext = createContext(null);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q74: What is Hydration?

**Difficulty**: Advanced

**Strategy**:
Attaching event listeners to the server-rendered HTML on the client side.

**Code Example**:
```javascript
hydrateRoot(document.getElementById('root'), <App />);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q75: How do you implement dark mode?

**Difficulty**: Intermediate

**Strategy**:
Use Context to store theme state and a ThemeProvider (styled-components or MUI).

**Code Example**:
```javascript
const theme = isDark ? darkTheme : lightTheme;
<ThemeProvider theme={theme}>...</ThemeProvider>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q76: What is prop types?

**Difficulty**: Beginner

**Strategy**:
Runtime type checking for React props. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
MyComponent.propTypes = { name: PropTypes.string.isRequired };
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q77: How do you optimize Context re-renders?

**Difficulty**: Advanced

**Strategy**:
Memoize the value passed to the Provider. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const value = useMemo(() => ({ state, dispatch }), [state]);
<Ctx.Provider value={value}>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q78: React Server Components vs Client Components?

**Difficulty**: Advanced

**Strategy**:
Server Components render on server, zero bundle size. Client Components render on client, have interactivity.

**Code Example**:
```javascript
// Server Component (default in Next.js app dir)
async function Page() { const data = await db.query(); return <div>{data}</div> }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q79: How do you handle images in React?

**Difficulty**: Beginner

**Strategy**:
Import them or use `img` tag. In frameworks like Next.js, use `Image` component for optimization.

**Code Example**:
```javascript
<img src={logo} alt="Logo" />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q80: What is the Virtual DOM?

**Difficulty**: Beginner

**Strategy**:
A lightweight copy of the actual DOM in memory. React syncs VDOM with Real DOM.

**Code Example**:
```javascript
// VDOM is a JavaScript object representation
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q81: How do you implement authentication in React?

**Difficulty**: Intermediate

**Strategy**:
Store token (localStorage/cookie), use Context for auth state, and Protected Routes.

**Code Example**:
```javascript
const PrivateRoute = ({ children }) => auth ? children : <Navigate to="/login" />;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q82: How do you handle multiple environments?

**Difficulty**: Intermediate

**Strategy**:
Use `.env` files (`REACT_APP_` or `VITE_`). This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const apiUrl = process.env.REACT_APP_API_URL;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q83: How do you debug performance issues?

**Difficulty**: Intermediate

**Strategy**:
Use React DevTools Profiler tab. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Record interaction, view commit chart
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q84: What is Render Props pattern?

**Difficulty**: Intermediate

**Strategy**:
Sharing code between components using a prop whose value is a function.

**Code Example**:
```javascript
<DataProvider render={data => <h1>{data.title}</h1>} />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q85: How do you create a compound component?

**Difficulty**: Advanced

**Strategy**:
Components that work together (e.g., Select, Select.Option).

**Code Example**:
```javascript
const Select = ({ children }) => <Provider>{children}</Provider>;
Select.Option = Option;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q86: How do you manage global state without Redux?

**Difficulty**: Intermediate

**Strategy**:
Context API + useReducer, or libraries like Zustand/Recoil.

**Code Example**:
```javascript
const useStore = create(set => ({ count: 0, inc: () => set(s => ({ count: s.count + 1 })) }));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q87: How do you implement infinite scroll?

**Difficulty**: Intermediate

**Strategy**:
Intersection Observer API to detect when bottom is reached.

**Code Example**:
```javascript
const observer = new IntersectionObserver(entries => { if(entries[0].isIntersecting) loadMore(); });
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q88: How do you secure React apps?

**Difficulty**: Intermediate

**Strategy**:
Prevent XSS (React escapes by default), avoid `dangerouslySetInnerHTML`, secure headers.

**Code Example**:
```javascript
// Don't do this unless sanitized
<div dangerouslySetInnerHTML={{__html: userContent}} />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q89: How do you unit test hooks?

**Difficulty**: Intermediate

**Strategy**:
Use `renderHook` from testing library. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const { result } = renderHook(() => useCounter());
act(() => result.current.increment());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q90: What is `flushSync`?

**Difficulty**: Advanced

**Strategy**:
Forces React to flush pending updates synchronously.

**Code Example**:
```javascript
flushSync(() => { setCount(count + 1); });
// DOM is updated immediately here
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q91: How do you handle race conditions in useEffect?

**Difficulty**: Advanced

**Strategy**:
Use a boolean flag or AbortController. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
useEffect(() => {
  let ignore = false;
  fetchData().then(res => { if (!ignore) setData(res); });
  return () => { ignore = true; };
}, []);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q92: What is `dangerouslySetInnerHTML`?

**Difficulty**: Beginner

**Strategy**:
React's replacement for `innerHTML`. Risky for XSS.

**Code Example**:
```javascript
<div dangerouslySetInnerHTML={{ __html: '<b>Bold</b>' }} />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q93: How do you implement drag and drop?

**Difficulty**: Intermediate

**Strategy**:
Use HTML5 Drag and Drop API or libraries like `dnd-kit` or `react-beautiful-dnd`.

**Code Example**:
```javascript
<div draggable onDragStart={...}>Item</div>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q94: How do you handle file uploads in React?

**Difficulty**: Intermediate

**Strategy**:
Use `input type='file'` and `FormData`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const formData = new FormData();
formData.append('file', fileInput.files[0]);
fetch('/upload', { method: 'POST', body: formData });
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q95: How do you implement a carousel?

**Difficulty**: Intermediate

**Strategy**:
Manage active index state and transform styles. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
<div style={{ transform: `translateX(-${activeIndex * 100}%)` }}>...</div>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q96: How do you mock API calls in tests?

**Difficulty**: Intermediate

**Strategy**:
Use `jest.mock` or `msw` (Mock Service Worker). This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
server.use(rest.get('/api/user', (req, res, ctx) => res(ctx.json({ name: 'John' }))));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q97: What is `React.memo`?

**Difficulty**: Beginner

**Strategy**:
HOC to memoize functional components based on props comparison.

**Code Example**:
```javascript
const MyComponent = React.memo(function MyComponent(props) { ... });
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q98: How do you implement a tooltip?

**Difficulty**: Intermediate

**Strategy**:
State for visibility and position calculation (or use libraries like Tippy.js).

**Code Example**:
```javascript
{show && <div style={{ top, left }}>Tooltip</div>}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q99: How do you handle window resize events?

**Difficulty**: Intermediate

**Strategy**:
Add event listener in `useEffect`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
useEffect(() => {
  window.addEventListener('resize', handleResize);
  return () => window.removeEventListener('resize', handleResize);
}, []);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q100: How do you implement A/B testing?

**Difficulty**: Intermediate

**Strategy**:
Conditionally render components based on user bucket/flag.

**Code Example**:
```javascript
{variant === 'A' ? <NewFeature /> : <OldFeature />}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>
