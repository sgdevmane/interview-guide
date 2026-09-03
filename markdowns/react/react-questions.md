<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="React.js Logo" width="100" height="100">
  </a>
  <h1>React.js Interview Questions & Answers</h1>
  <p><b>Comprehensive, practical interview questions covering React 18/19, Hooks, Fiber, and Performance</b></p>
</div>

---

## Table of Contents

1. [Explain the Virtual DOM and React's Reconciliation algorithm?](#q1) <span class="intermediate">Intermediate</span>
2. [What is React Fiber and how does it enable concurrent rendering?](#q2) <span class="advanced">Advanced</span>
3. [Difference between `useState` and `useReducer` and when to use each?](#q3) <span class="intermediate">Intermediate</span>
4. [How does `useEffect` differ from `useLayoutEffect` and `useInsertionEffect`?](#q4) <span class="advanced">Advanced</span>
5. [Explain `useCallback` vs `useMemo`: Rules, cost of memoization, and anti-patterns?](#q5) <span class="intermediate">Intermediate</span>
6. [How do you implement a custom `useFetch` hook with caching and AbortController?](#q6) <span class="advanced">Advanced</span>
7. [What is `useTransition` and how does it differ from `useDeferredValue`?](#q7) <span class="advanced">Advanced</span>
8. [What are React Server Components (RSC) and how do they differ from SSR?](#q8) <span class="advanced">Advanced</span>
9. [How does Automatic Batching in React 18 work and how do you opt out?](#q9) <span class="intermediate">Intermediate</span>
10. [How do you implement an Error Boundary with fallback UI in React?](#q10) <span class="intermediate">Intermediate</span>
11. [How do you split Context to avoid unnecessary re-renders?](#q11) <span class="advanced">Advanced</span>
12. [How do you implement Compound Components pattern in React?](#q12) <span class="advanced">Advanced</span>
13. [How do you use `forwardRef` and `useImperativeHandle`?](#q13) <span class="advanced">Advanced</span>
14. [How do you render Portals in React and handle event bubbling?](#q14) <span class="intermediate">Intermediate</span>
15. [How do you virtualize large lists (10,000+ items) in React?](#q15) <span class="advanced">Advanced</span>
16. [How do you implement a custom `useDebounce` hook?](#q16) <span class="intermediate">Intermediate</span>
17. [What is the difference between Controlled and Uncontrolled components?](#q17) <span class="beginner">Beginner</span>
18. [What is React StrictMode and why does it double-invoke effects in development?](#q18) <span class="beginner">Beginner</span>
19. [How do you implement custom `usePrevious` hook using `useRef`?](#q19) <span class="intermediate">Intermediate</span>
20. [How do you implement custom `useLocalStorage` hook with multi-tab synchronization?](#q20) <span class="intermediate">Intermediate</span>
21. [How do you implement custom hook `useOnClickOutside` for dropdowns?](#q21) <span class="intermediate">Intermediate</span>
22. [What is `useSyncExternalStore` and when should you use it?](#q22) <span class="advanced">Advanced</span>
23. [What is `useOptimistic` in React 19 and how does it improve UX?](#q23) <span class="advanced">Advanced</span>
24. [What is `useActionState` in React 19?](#q24) <span class="advanced">Advanced</span>
25. [What is the difference between shallow and deep comparison in React memoization?](#q25) <span class="intermediate">Intermediate</span>
26. [Why should you avoid using array index as `key` prop in React lists?](#q26) <span class="beginner">Beginner</span>
27. [How do you manage Focus for accessibility (a11y) inside React Modals?](#q27) <span class="intermediate">Intermediate</span>
28. [How do you implement Polymorphic components in React with TypeScript (`as` prop)?](#q28) <span class="advanced">Advanced</span>
29. [How do you implement code splitting with `React.lazy` and `Suspense`?](#q29) <span class="intermediate">Intermediate</span>
30. [How do you test React components with Jest and React Testing Library?](#q30) <span class="intermediate">Intermediate</span>
31. [What causes memory leaks in React and how do you diagnose them?](#q31) <span class="advanced">Advanced</span>
32. [How does React protect against XSS attacks in JSX?](#q32) <span class="intermediate">Intermediate</span>
33. [How do you safely render HTML in React with DOMPurify?](#q33) <span class="intermediate">Intermediate</span>
34. [How do you implement custom `useInterval` hook?](#q34) <span class="intermediate">Intermediate</span>
35. [How do you implement Infinite Scroll using `IntersectionObserver`?](#q35) <span class="intermediate">Intermediate</span>
36. [How do you build an accessible Accordion component?](#q36) <span class="intermediate">Intermediate</span>
37. [How does React Profiler API work in production?](#q37) <span class="advanced">Advanced</span>
38. [What is Prop Drilling and how does Component Composition resolve it?](#q38) <span class="beginner">Beginner</span>
39. [How do you handle JWT authentication refresh flow in React?](#q39) <span class="advanced">Advanced</span>
40. [What is the difference between `React.createElement` and JSX?](#q40) <span class="beginner">Beginner</span>
41. [How do you handle multi-step forms in React?](#q41) <span class="intermediate">Intermediate</span>
42. [How do you optimize SVG icons in React?](#q42) <span class="beginner">Beginner</span>
43. [What is client-side routing vs server-side routing?](#q43) <span class="beginner">Beginner</span>
44. [How do you create a custom `useMediaQuery` hook?](#q44) <span class="intermediate">Intermediate</span>
45. [How do you cancel pending Axios requests on unmount?](#q45) <span class="intermediate">Intermediate</span>
46. [What are Render Props and why did Hooks replace them?](#q46) <span class="intermediate">Intermediate</span>
47. [How do you implement Dark Mode with CSS Variables?](#q47) <span class="beginner">Beginner</span>
48. [How do you handle Hydration mismatch errors in React SSR?](#q48) <span class="advanced">Advanced</span>
49. [What is `useId` and why is it important for accessibility?](#q49) <span class="beginner">Beginner</span>
50. [How do you implement Drag and Drop in React?](#q50) <span class="intermediate">Intermediate</span>
51. [What is the purpose of `React.Children.map`?](#q51) <span class="intermediate">Intermediate</span>
52. [How do you prevent unnecessary re-renders with Context objects?](#q52) <span class="intermediate">Intermediate</span>
53. [What are Higher-Order Components and what are their limitations?](#q53) <span class="intermediate">Intermediate</span>
54. [How do you implement Undo/Redo history in React state?](#q54) <span class="advanced">Advanced</span>
55. [What is the purpose of `useImperativeHandle`?](#q55) <span class="advanced">Advanced</span>
56. [How do you debounce API validation in React Hook Form?](#q56) <span class="intermediate">Intermediate</span>
57. [What is the difference in event delegation between React 16 and 17+?](#q57) <span class="advanced">Advanced</span>
58. [How do you implement Skeleton Loaders during data fetching?](#q58) <span class="beginner">Beginner</span>
59. [How do you control HTML `<dialog>` element in React?](#q59) <span class="intermediate">Intermediate</span>
60. [How does Server-Side Rendering (SSR) improve SEO?](#q60) <span class="intermediate">Intermediate</span>
61. [What is Static Site Generation (SSG)?](#q61) <span class="beginner">Beginner</span>
62. [What is Incremental Static Regeneration (ISR)?](#q62) <span class="advanced">Advanced</span>
63. [What is `React.cloneElement` and why is it discouraged in modern React?](#q63) <span class="intermediate">Intermediate</span>
64. [How do you build a Global Toast Notification system in React?](#q64) <span class="intermediate">Intermediate</span>
65. [How do you memoize recursive components in React?](#q65) <span class="advanced">Advanced</span>
66. [What is State Hoisting (Lifting State Up)?](#q66) <span class="beginner">Beginner</span>
67. [How do you build dynamic breadcrumb navigation in React?](#q67) <span class="intermediate">Intermediate</span>
68. [What is the difference between `PureComponent` and `Component`?](#q68) <span class="beginner">Beginner</span>
69. [How do you track file upload progress in React?](#q69) <span class="intermediate">Intermediate</span>
70. [How do you implement responsive table card layouts in React?](#q70) <span class="intermediate">Intermediate</span>
71. [What is the difference between `<React.Fragment>` and `<>` shorthand?](#q71) <span class="beginner">Beginner</span>
72. [How do you handle keyboard arrow navigation in Tabs?](#q72) <span class="intermediate">Intermediate</span>
73. [What is the difference between `window.location.href` and React Router `navigate`?](#q73) <span class="beginner">Beginner</span>
74. [How do you mock API calls in Jest without extra libraries?](#q74) <span class="intermediate">Intermediate</span>
75. [How do you test custom hooks using `renderHook`?](#q75) <span class="intermediate">Intermediate</span>
76. [What is Micro-frontend Module Federation with React?](#q76) <span class="advanced">Advanced</span>
77. [How do you optimize Core Web Vitals (LCP, INP, CLS) in React?](#q77) <span class="advanced">Advanced</span>
78. [How do you implement Copy to Clipboard with temporary tooltip?](#q78) <span class="beginner">Beginner</span>
79. [What is the difference between dependencies and peerDependencies in React packages?](#q79) <span class="intermediate">Intermediate</span>
80. [How do you build an accessible Dropdown menu in React?](#q80) <span class="intermediate">Intermediate</span>
81. [How do you test Error Boundary components with React Testing Library?](#q81) <span class="intermediate">Intermediate</span>
82. [What was SyntheticEvent pooling in React 16 and why was it removed in React 17?](#q82) <span class="advanced">Advanced</span>
83. [How do you implement custom `useHover` hook?](#q83) <span class="intermediate">Intermediate</span>
84. [How do you handle i18n localization in React?](#q84) <span class="intermediate">Intermediate</span>
85. [What are the advantages of `pnpm` in React monorepos?](#q85) <span class="intermediate">Intermediate</span>
86. [How do you implement pagination with ellipsis in React?](#q86) <span class="intermediate">Intermediate</span>
87. [What is client state vs server state in React applications?](#q87) <span class="intermediate">Intermediate</span>
88. [How do you implement auto-saving forms in React?](#q88) <span class="intermediate">Intermediate</span>
89. [How do you build a custom Range Slider in React?](#q89) <span class="intermediate">Intermediate</span>
90. [What are React Server Actions and how do they replace API routes?](#q90) <span class="advanced">Advanced</span>
91. [How do you implement WebAuthn biometric login in React?](#q91) <span class="advanced">Advanced</span>
92. [How do you create animated notification badges in React?](#q92) <span class="beginner">Beginner</span>
93. [What is the difference between `useCallback` and regular inline functions?](#q93) <span class="beginner">Beginner</span>
94. [How do you implement sticky headers in React?](#q94) <span class="beginner">Beginner</span>
95. [How do you structure enterprise React codebases?](#q95) <span class="advanced">Advanced</span>
96. [How do you test accessibility with `@axe-core/react`?](#q96) <span class="intermediate">Intermediate</span>
97. [What is the difference between SPA and MPA?](#q97) <span class="beginner">Beginner</span>
98. [How do you handle multi-tab session expiration in React?](#q98) <span class="advanced">Advanced</span>
99. [How do you implement custom `useCountdown` hook?](#q99) <span class="intermediate">Intermediate</span>
100. [What is shallow routing in React Router?](#q100) <span class="intermediate">Intermediate</span>

---

<a id="q1"></a>
### Q1: Explain the Virtual DOM and React's Reconciliation algorithm?

**Difficulty**: Intermediate

**Strategy**:
The Virtual DOM (VDOM) is an in-memory representation of real DOM elements. React uses an O(n) heuristic diffing algorithm: 1) Elements of different types tear down and recreate the tree, 2) Keys identify stable list items across renders. In React 16+, Reconciliation is executed incrementally via the Fiber architecture.

**Code Example**:
```jsx
// Stable keys prevent unnecessary DOM node recreations during diffing
function UserList({ users }) {
  return (
    <ul>
      {users.map(user => (
        <li key={user.id}>{user.name} ({user.role})</li>
      ))}
    </ul>
  );
}
```

---

<a id="q2"></a>
### Q2: What is React Fiber and how does it enable concurrent rendering?

**Difficulty**: Advanced

**Strategy**:
React Fiber is a rewrite of React core reconciler. It models units of work as a linked list of Fiber nodes with child, sibling, and return pointers. This enables cooperative multitasking: React can pause, resume, prioritize (via Lanes), or abort rendering work across animation frames.

**Code Example**:
```javascript
// Fiber node conceptual structure
const fiber = {
  type: 'div',
  key: null,
  stateNode: domElement,
  child: firstChildFiber,
  sibling: nextSiblingFiber,
  return: parentFiber,
  memoizedProps: prevProps,
  pendingProps: nextProps,
  lanes: 0b0001000 // Priority lane
};
```

---

<a id="q3"></a>
### Q3: Difference between `useState` and `useReducer` and when to use each?

**Difficulty**: Intermediate

**Strategy**:
`useState` is suited for independent, simple state. `useReducer` is best when: 1) State logic is complex with multiple transitions, 2) The next state depends on prior state in multiple ways, 3) Passing a stable `dispatch` function down avoids prop-drilling callbacks and prevents child re-renders.

**Code Example**:
```jsx
import React, { useReducer } from 'react';

const initialState = { count: 0, step: 1 };
function reducer(state, action) {
  switch (action.type) {
    case 'inc': return { ...state, count: state.count + state.step };
    case 'setStep': return { ...state, step: action.payload };
    case 'reset': return initialState;
    default: return state;
  }
}
export function Counter() {
  const [state, dispatch] = useReducer(reducer, initialState);
  return <button onClick={() => dispatch({ type: 'inc' })}>Count: {state.count}</button>;
}
```

---

<a id="q4"></a>
### Q4: How does `useEffect` differ from `useLayoutEffect` and `useInsertionEffect`?

**Difficulty**: Advanced

**Strategy**:
- `useInsertionEffect`: Fires synchronously BEFORE any DOM mutations. Used by CSS-in-JS libraries to inject `<style>` tags.
- `useLayoutEffect`: Fires synchronously AFTER DOM mutations but BEFORE browser repaint. Used to measure layout or mutate DOM without flickering.
- `useEffect`: Fires asynchronously AFTER browser paint. Used for data fetching, timers, and subscriptions.

**Code Example**:
```jsx
import { useState, useLayoutEffect, useRef } from 'react';

export function Tooltip({ targetRect }) {
  const [pos, setPos] = useState({ top: 0, left: 0 });
  const ref = useRef(null);

  useLayoutEffect(() => {
    if (ref.current) {
      const height = ref.current.offsetHeight;
      setPos({ top: targetRect.top - height - 8, left: targetRect.left });
    }
  }, [targetRect]);

  return <div ref={ref} style={{ position: 'fixed', top: pos.top, left: pos.left }}>Tooltip</div>;
}
```

---

<a id="q5"></a>
### Q5: Explain `useCallback` vs `useMemo`: Rules, cost of memoization, and anti-patterns?

**Difficulty**: Intermediate

**Strategy**:
- `useMemo` caches calculation results; `useCallback` caches function definitions.
- Anti-pattern: Memoizing trivial calculations or callbacks passed to plain DOM tags. Memoization incurs memory for dependency arrays and comparison overhead. Use only when passing to `React.memo` components, preserving object references for hook dependencies, or heavy calculations.

**Code Example**:
```jsx
import React, { useState, useMemo, useCallback } from 'react';

const MemoRow = React.memo(({ item, onDelete }) => {
  return <div>{item.name} <button onClick={() => onDelete(item.id)}>Delete</button></div>;
});

export function Table({ items }) {
  const [search, setSearch] = useState('');
  const filtered = useMemo(() => items.filter(i => i.name.includes(search)), [items, search]);
  const handleDelete = useCallback((id) => console.log('Delete', id), []);
  return <div>{filtered.map(i => <MemoRow key={i.id} item={i} onDelete={handleDelete} />)}</div>;
}
```

---

<a id="q6"></a>
### Q6: How do you implement a custom `useFetch` hook with caching and AbortController?

**Difficulty**: Advanced

**Strategy**:
A robust `useFetch` cancels in-flight requests via `AbortController` on unmount/URL change to avoid race conditions and uses a cache Map to avoid duplicate requests.

**Code Example**:
```typescript
import { useState, useEffect } from 'react';

const cache = new Map<string, any>();
export function useFetch<T>(url: string) {
  const [data, setData] = useState<T | null>(cache.get(url) || null);
  const [loading, setLoading] = useState(!cache.has(url));
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    if (!url) return;
    if (cache.has(url)) { setData(cache.get(url)); setLoading(false); return; }
    const controller = new AbortController();
    setLoading(true);
    fetch(url, { signal: controller.signal })
      .then(res => res.json())
      .then(d => { cache.set(url, d); setData(d); setLoading(false); })
      .catch(err => { if (err.name !== 'AbortError') { setError(err); setLoading(false); } });
    return () => controller.abort();
  }, [url]);

  return { data, loading, error };
}
```

---

<a id="q7"></a>
### Q7: What is `useTransition` and how does it differ from `useDeferredValue`?

**Difficulty**: Advanced

**Strategy**:
`useTransition` wraps a state setter to mark it as low-priority (transition) with an `isPending` indicator. `useDeferredValue` wraps a value itself (props or state) and defers updating it until high-priority work (like typing) finishes.

**Code Example**:
```jsx
import { useState, useTransition } from 'react';

export function SearchFilter({ list }) {
  const [input, setInput] = useState('');
  const [query, setQuery] = useState('');
  const [isPending, startTransition] = useTransition();

  const onChange = (e) => {
    setInput(e.target.value); // Urgent
    startTransition(() => {
      setQuery(e.target.value); // Transition
    });
  };

  return (
    <div>
      <input value={input} onChange={onChange} />
      {isPending && <span>Filtering...</span>}
      <ItemList query={query} list={list} />
    </div>
  );
}
```

---

<a id="q8"></a>
### Q8: What are React Server Components (RSC) and how do they differ from SSR?

**Difficulty**: Advanced

**Strategy**:
SSR renders static HTML on the server and still delivers the entire component JavaScript bundle for hydration. RSC execute exclusively on the server, streaming a JSON UI format to the client, never adding their dependencies to the browser bundle.

**Code Example**:
```jsx
// app/products/page.tsx - Server Component
import db from '@/lib/db';
import LikeButton from './LikeButton';

export default async function Products() {
  const products = await db.query('SELECT * FROM products');
  return (
    <div>
      {products.map(p => (
        <div key={p.id}>
          <h3>{p.name}</h3>
          <LikeButton id={p.id} />
        </div>
      ))}
    </div>
  );
}
```

---

<a id="q9"></a>
### Q9: How does Automatic Batching in React 18 work and how do you opt out?

**Difficulty**: Intermediate

**Strategy**:
React 18 batches all state updates across promises, `setTimeout`, native events, and fetch calls into one render. Use `ReactDOM.flushSync` if you need immediate synchronous DOM updates.

**Code Example**:
```jsx
import { useState } from 'react';
import { flushSync } from 'react-dom';

export function BatchDemo() {
  const [count, setCount] = useState(0);
  const [flag, setFlag] = useState(false);

  const handleAsync = async () => {
    await fetch('/api/data');
    // Automatically batched in React 18
    setCount(c => c + 1);
    setFlag(f => !f);
  };

  const handleForceSync = () => {
    flushSync(() => setCount(c => c + 1)); // Synchronous commit
  };

  return <button onClick={handleAsync}>Async Click</button>;
}
```

---

<a id="q10"></a>
### Q10: How do you implement an Error Boundary with fallback UI in React?

**Difficulty**: Intermediate

**Strategy**:
Error Boundaries are class components using `static getDerivedStateFromError` (to set error state) and `componentDidCatch` (to log errors). They catch rendering, lifecycle, and constructor errors in child subtrees.

**Code Example**:
```jsx
import React, { Component } from 'react';

export class ErrorBoundary extends Component {
  state = { hasError: false, error: null };
  static getDerivedStateFromError(error) { return { hasError: true, error }; }
  componentDidCatch(err, info) { console.error('Caught:', err, info); }
  render() {
    if (this.state.hasError) {
      return (
        <div role="alert">
          <h2>Error encountered</h2>
          <button onClick={() => this.setState({ hasError: false })}>Retry</button>
        </div>
      );
    }
    return this.props.children;
  }
}
```

---

<a id="q11"></a>
### Q11: How do you split Context to avoid unnecessary re-renders?

**Difficulty**: Advanced

**Strategy**:
Context consumers re-render on any value change. Split state and dispatch into separate contexts to prevent components that only dispatch actions from re-rendering.

**Code Example**:
```jsx
const StateCtx = createContext();
const DispatchCtx = createContext();
export function Provider({ children }) {
  const [state, dispatch] = useReducer(reducer, init);
  return (
    <StateCtx.Provider value={state}>
      <DispatchCtx.Provider value={dispatch}>{children}</DispatchCtx.Provider>
    </StateCtx.Provider>
  );
}
```

---

<a id="q12"></a>
### Q12: How do you implement Compound Components pattern in React?

**Difficulty**: Advanced

**Strategy**:
Compound components share implicit state via Context, creating clean JSX composition (e.g. `<Tabs>`, `<Tabs.Tab>`).

**Code Example**:
```jsx
const TabCtx = createContext();
export function Tabs({ children, defaultTab }) {
  const [active, setActive] = useState(defaultTab);
  return <TabCtx.Provider value={{ active, setActive }}>{children}</TabCtx.Provider>;
}
Tabs.Tab = ({ id, children }) => {
  const { active, setActive } = useContext(TabCtx);
  return <button className={active === id ? 'active' : ''} onClick={() => setActive(id)}>{children}</button>;
};
```

---

<a id="q13"></a>
### Q13: How do you use `forwardRef` and `useImperativeHandle`?

**Difficulty**: Advanced

**Strategy**:
Forward DOM references and expose explicit imperative API methods to parents.

**Code Example**:
```jsx
export const CustomInput = forwardRef((props, ref) => {
  const inputRef = useRef();
  useImperativeHandle(ref, () => ({
    focus: () => inputRef.current.focus(),
    clear: () => { inputRef.current.value = ''; }
  }));
  return <input ref={inputRef} {...props} />;
});
```

---

<a id="q14"></a>
### Q14: How do you render Portals in React and handle event bubbling?

**Difficulty**: Intermediate

**Strategy**:
`createPortal` mounts children into an external DOM node while preserving React synthetic event bubbling up the virtual tree.

**Code Example**:
```jsx
import { createPortal } from 'react-dom';
export function Modal({ isOpen, children, onClose }) {
  if (!isOpen) return null;
  return createPortal(
    <div className="overlay" onClick={onClose}>
      <div className="modal" onClick={e => e.stopPropagation()}>{children}</div>
    </div>,
    document.body
  );
}
```

---

<a id="q15"></a>
### Q15: How do you virtualize large lists (10,000+ items) in React?

**Difficulty**: Advanced

**Strategy**:
Virtual windowing computes visible items based on scroll offset and only renders DOM elements in view.

**Code Example**:
```jsx
export function VirtualList({ items, itemHeight = 40, height = 400 }) {
  const [scroll, setScroll] = useState(0);
  const start = Math.floor(scroll / itemHeight);
  const count = Math.ceil(height / itemHeight) + 2;
  const visible = items.slice(start, start + count);
  return (
    <div style={{ height, overflowY: 'auto' }} onScroll={e => setScroll(e.target.scrollTop)}>
      <div style={{ height: items.length * itemHeight, position: 'relative' }}>
        {visible.map((item, idx) => (
          <div key={item.id} style={{ position: 'absolute', top: (start + idx) * itemHeight }}>{item.title}</div>
        ))}
      </div>
    </div>
  );
}
```

---

<a id="q16"></a>
### Q16: How do you implement a custom `useDebounce` hook?

**Difficulty**: Intermediate

**Strategy**:
Delay updating state until delay period passes without new changes.

**Code Example**:
```typescript
export function useDebounce<T>(value: T, delay: number): T {
  const [debounced, setDebounced] = useState(value);
  useEffect(() => {
    const timer = setTimeout(() => setDebounced(value), delay);
    return () => clearTimeout(timer);
  }, [value, delay]);
  return debounced;
}
```

---

<a id="q17"></a>
### Q17: What is the difference between Controlled and Uncontrolled components?

**Difficulty**: Beginner

**Strategy**:
Controlled components have value driven by React state; uncontrolled components rely on native DOM state via `ref`.

**Code Example**:
```jsx
// Controlled
<input value={val} onChange={e => setVal(e.target.value)} />
// Uncontrolled
<input ref={inputRef} defaultValue="Initial" />
```

---

<a id="q18"></a>
### Q18: What is React StrictMode and why does it double-invoke effects in development?

**Difficulty**: Beginner

**Strategy**:
StrictMode checks for purity and missing cleanup by mounting, unmounting, and re-mounting components in dev mode.

**Code Example**:
```jsx
<React.StrictMode><App /></React.StrictMode>
```

---

<a id="q19"></a>
### Q19: How do you implement custom `usePrevious` hook using `useRef`?

**Difficulty**: Intermediate

**Strategy**:
Updating `useRef` inside `useEffect` captures the previous render's value without triggering a re-render.

**Code Example**:
```typescript
export function usePrevious<T>(value: T): T | undefined {
  const ref = useRef<T>();
  useEffect(() => { ref.current = value; }, [value]);
  return ref.current;
}
```

---

<a id="q20"></a>
### Q20: How do you implement custom `useLocalStorage` hook with multi-tab synchronization?

**Difficulty**: Intermediate

**Strategy**:
Sync state with localStorage and subscribe to the `storage` event for cross-tab updates.

**Code Example**:
```typescript
export function useLocalStorage<T>(key: string, initial: T) {
  const [val, setVal] = useState<T>(() => {
    try { const item = localStorage.getItem(key); return item ? JSON.parse(item) : initial; } catch { return initial; }
  });
  const update = (newVal: T) => {
    setVal(newVal);
    localStorage.setItem(key, JSON.stringify(newVal));
  };
  return [val, update] as const;
}
```

---

<a id="q21"></a>
### Q21: How do you implement custom hook `useOnClickOutside` for dropdowns?

**Difficulty**: Intermediate

**Strategy**:
Listen to document mousedown and check if ref contains target.

**Code Example**:
```typescript
export function useOnClickOutside(ref: any, handler: () => void) {
  useEffect(() => {
    const listener = (e: any) => { if (!ref.current?.contains(e.target)) handler(); };
    document.addEventListener('mousedown', listener);
    return () => document.removeEventListener('mousedown', listener);
  }, [ref, handler]);
}
```

---

<a id="q22"></a>
### Q22: What is `useSyncExternalStore` and when should you use it?

**Difficulty**: Advanced

**Strategy**:
Subscribes to external stores safely avoiding tearing in concurrent mode.

**Code Example**:
```typescript
import { useSyncExternalStore } from 'react';
function subscribe(cb: () => void) {
  window.addEventListener('online', cb);
  return () => window.removeEventListener('online', cb);
}
export const useOnline = () => useSyncExternalStore(subscribe, () => navigator.onLine, () => true);
```

---

<a id="q23"></a>
### Q23: What is `useOptimistic` in React 19 and how does it improve UX?

**Difficulty**: Advanced

**Strategy**:
Provides immediate optimistic UI state while an async server action executes.

**Code Example**:
```jsx
import { useOptimistic } from 'react';
export function LikeButton({ likes, onLike }) {
  const [opt, setOpt] = useOptimistic(likes, (prev) => prev + 1);
  return <button onClick={async () => { setOpt(likes + 1); await onLike(); }}>❤️ {opt}</button>;
}
```

---

<a id="q24"></a>
### Q24: What is `useActionState` in React 19?

**Difficulty**: Advanced

**Strategy**:
Integrates server actions with component state and pending status.

**Code Example**:
```jsx
import { useActionState } from 'react';
async function action(prev, formData) { return { count: prev.count + 1 }; }
export function Form() {
  const [state, formAction, isPending] = useActionState(action, { count: 0 });
  return <form action={formAction}><button disabled={isPending}>Count: {state.count}</button></form>;
}
```

---

<a id="q25"></a>
### Q25: What is the difference between shallow and deep comparison in React memoization?

**Difficulty**: Intermediate

**Strategy**:
Shallow checks references; deep recursively checks all properties.

**Code Example**:
```javascript
function arePropsEqual(prev, next) { return prev.id === next.id; }
export const MemoCard = React.memo(Card, arePropsEqual);
```

---

<a id="q26"></a>
### Q26: Why should you avoid using array index as `key` prop in React lists?

**Difficulty**: Beginner

**Strategy**:
Index keys break component state association during re-ordering or deletions.

**Code Example**:
```jsx
// Good
{items.map(item => <Item key={item.id} data={item} />)}
```

---

<a id="q27"></a>
### Q27: How do you manage Focus for accessibility (a11y) inside React Modals?

**Difficulty**: Intermediate

**Strategy**:
Trap tab focus inside the modal and return focus to trigger on close.

**Code Example**:
```jsx
useEffect(() => { if (isOpen) ref.current?.focus(); }, [isOpen]);
```

---

<a id="q28"></a>
### Q28: How do you implement Polymorphic components in React with TypeScript (`as` prop)?

**Difficulty**: Advanced

**Strategy**:
Use generic props extending `React.ElementType`.

**Code Example**:
```tsx
type ButtonProps<T extends React.ElementType> = { as?: T; children: React.ReactNode; } & React.ComponentPropsWithoutRef<T>;
export function Button<T extends React.ElementType = 'button'>({ as, children, ...props }: ButtonProps<T>) {
  const Component = as || 'button';
  return <Component {...props}>{children}</Component>;
}
```

---

<a id="q29"></a>
### Q29: How do you implement code splitting with `React.lazy` and `Suspense`?

**Difficulty**: Intermediate

**Strategy**:
Dynamically import components to create separate chunks.

**Code Example**:
```jsx
const Admin = React.lazy(() => import('./Admin'));
<React.Suspense fallback={<div>Loading...</div>}><Admin /></React.Suspense>
```

---

<a id="q30"></a>
### Q30: How do you test React components with Jest and React Testing Library?

**Difficulty**: Intermediate

**Strategy**:
Test behavior with `screen.getByRole` and `userEvent`.

**Code Example**:
```tsx
test('increments', async () => {
  render(<Counter />);
  await userEvent.click(screen.getByRole('button', { name: /inc/i }));
  expect(screen.getByText('1')).toBeInTheDocument();
});
```

---

<a id="q31"></a>
### Q31: What causes memory leaks in React and how do you diagnose them?

**Difficulty**: Advanced

**Strategy**:
Uncleaned subscriptions, timers, and closures retaining DOM nodes.

**Code Example**:
```javascript
useEffect(() => {
  const sub = eventBus.subscribe(handler);
  return () => sub.unsubscribe(); // Must cleanup
}, []);
```

---

<a id="q32"></a>
### Q32: How does React protect against XSS attacks in JSX?

**Difficulty**: Intermediate

**Strategy**:
React escapes all strings embedded in JSX before rendering.

**Code Example**:
```jsx
// React escapes malicious strings automatically
const dangerous = '<script>alert("XSS")</script>';
return <div>{dangerous}</div>;
```

---

<a id="q33"></a>
### Q33: How do you safely render HTML in React with DOMPurify?

**Difficulty**: Intermediate

**Strategy**:
Sanitize the string before using `dangerouslySetInnerHTML`.

**Code Example**:
```jsx
import DOMPurify from 'dompurify';
export function SafeHTML({ content }) {
  const clean = DOMPurify.sanitize(content);
  return <div dangerouslySetInnerHTML={{ __html: clean }} />;
}
```

---

<a id="q34"></a>
### Q34: How do you implement custom `useInterval` hook?

**Difficulty**: Intermediate

**Strategy**:
Store latest callback in ref to prevent stale closures while keeping interval active.

**Code Example**:
```javascript
export function useInterval(cb, delay) {
  const ref = useRef(cb);
  useEffect(() => { ref.current = cb; }, [cb]);
  useEffect(() => {
    if (delay !== null) {
      const id = setInterval(() => ref.current(), delay);
      return () => clearInterval(id);
    }
  }, [delay]);
}
```

---

<a id="q35"></a>
### Q35: How do you implement Infinite Scroll using `IntersectionObserver`?

**Difficulty**: Intermediate

**Strategy**:
Attach observer to sentinel element at list bottom.

**Code Example**:
```jsx
useEffect(() => {
  const observer = new IntersectionObserver(([e]) => { if (e.isIntersecting) loadMore(); });
  if (ref.current) observer.observe(ref.current);
  return () => observer.disconnect();
}, [loadMore]);
```

---

<a id="q36"></a>
### Q36: How do you build an accessible Accordion component?

**Difficulty**: Intermediate

**Strategy**:
Use `aria-expanded`, `aria-controls`, and `role="region"`.

**Code Example**:
```jsx
<button aria-expanded={isOpen} aria-controls="panel-1" onClick={toggle}>Header</button>
{isOpen && <div id="panel-1" role="region">Content</div>}
```

---

<a id="q37"></a>
### Q37: How does React Profiler API work in production?

**Difficulty**: Advanced

**Strategy**:
Measure render phase durations with `<Profiler onRender={callback}>`.

**Code Example**:
```jsx
<Profiler id="App" onRender={(id, phase, time) => console.log(id, phase, time)}><App /></Profiler>
```

---

<a id="q38"></a>
### Q38: What is Prop Drilling and how does Component Composition resolve it?

**Difficulty**: Beginner

**Strategy**:
Pass JSX components as children or props rather than drilling state down many levels.

**Code Example**:
```jsx
<Page header={<UserAvatar user={user} />} />
```

---

<a id="q39"></a>
### Q39: How do you handle JWT authentication refresh flow in React?

**Difficulty**: Advanced

**Strategy**:
Use Axios response interceptors to refresh access token on 401 error.

**Code Example**:
```javascript
axios.interceptors.response.use(res => res, async err => {
  if (err.response?.status === 401) { await refreshToken(); return axios(err.config); }
  return Promise.reject(err);
});
```

---

<a id="q40"></a>
### Q40: What is the difference between `React.createElement` and JSX?

**Difficulty**: Beginner

**Strategy**:
JSX is syntactic sugar compiled into `React.createElement` or JSX runtime `jsx()` calls.

**Code Example**:
```javascript
// JSX: <div className="box">Hi</div>
React.createElement('div', { className: 'box' }, 'Hi');
```

---

<a id="q41"></a>
### Q41: How do you handle multi-step forms in React?

**Difficulty**: Intermediate

**Strategy**:
Manage a step state index and collect accumulated form data at each step.

**Code Example**:
```jsx
const [step, setStep] = useState(1);
const [data, setData] = useState({});
```

---

<a id="q42"></a>
### Q42: How do you optimize SVG icons in React?

**Difficulty**: Beginner

**Strategy**:
Use SVGR to bundle SVGs as reusable vector components.

**Code Example**:
```jsx
export const Icon = ({ size = 24 }) => <svg width={size} height={size} viewBox="0 0 24 24"><path d="M12 2L2 22h20L12 2z"/></svg>;
```

---

<a id="q43"></a>
### Q43: What is client-side routing vs server-side routing?

**Difficulty**: Beginner

**Strategy**:
Client routing updates the DOM and History API without requesting a new HTML document.

**Code Example**:
```jsx
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
```

---

<a id="q44"></a>
### Q44: How do you create a custom `useMediaQuery` hook?

**Difficulty**: Intermediate

**Strategy**:
Listen to `window.matchMedia` change events.

**Code Example**:
```typescript
export function useMediaQuery(query: string) {
  const [matches, setMatches] = useState(() => window.matchMedia(query).matches);
  useEffect(() => {
    const media = window.matchMedia(query);
    const listener = (e: MediaQueryListEvent) => setMatches(e.matches);
    media.addEventListener('change', listener);
    return () => media.removeEventListener('change', listener);
  }, [query]);
  return matches;
}
```

---

<a id="q45"></a>
### Q45: How do you cancel pending Axios requests on unmount?

**Difficulty**: Intermediate

**Strategy**:
Pass `AbortController.signal` into Axios config.

**Code Example**:
```javascript
useEffect(() => {
  const ctrl = new AbortController();
  axios.get('/api', { signal: ctrl.signal });
  return () => ctrl.abort();
}, []);
```

---

<a id="q46"></a>
### Q46: What are Render Props and why did Hooks replace them?

**Difficulty**: Intermediate

**Strategy**:
Render props pass a rendering function as prop; hooks eliminate JSX wrapper nesting.

**Code Example**:
```jsx
<DataProvider render={data => <div>{data.title}</div>} />
```

---

<a id="q47"></a>
### Q47: How do you implement Dark Mode with CSS Variables?

**Difficulty**: Beginner

**Strategy**:
Toggle `data-theme` on documentElement and persist in localStorage.

**Code Example**:
```javascript
document.documentElement.setAttribute('data-theme', 'dark');
```

---

<a id="q48"></a>
### Q48: How do you handle Hydration mismatch errors in React SSR?

**Difficulty**: Advanced

**Strategy**:
Ensure server and initial client render outputs match, or use `suppressHydrationWarning`.

**Code Example**:
```jsx
<span suppressHydrationWarning>{new Date().toLocaleTimeString()}</span>
```

---

<a id="q49"></a>
### Q49: What is `useId` and why is it important for accessibility?

**Difficulty**: Beginner

**Strategy**:
Generates stable, unique IDs across client and server rendering.

**Code Example**:
```jsx
const id = useId();
return <><label htmlFor={id}>Email</label><input id={id}/></>;
```

---

<a id="q50"></a>
### Q50: How do you implement Drag and Drop in React?

**Difficulty**: Intermediate

**Strategy**:
Use native HTML Drag and Drop events or `dnd-kit` library.

**Code Example**:
```jsx
<div draggable onDragStart={e => e.dataTransfer.setData('text', 'id')}>Item</div>
```

---

<a id="q51"></a>
### Q51: What is the purpose of `React.Children.map`?

**Difficulty**: Intermediate

**Strategy**:
Safely iterates over opaque `props.children` elements.

**Code Example**:
```jsx
React.Children.map(children, child => React.cloneElement(child, { extra: true }))
```

---

<a id="q52"></a>
### Q52: How do you prevent unnecessary re-renders with Context objects?

**Difficulty**: Intermediate

**Strategy**:
Wrap context values inside `useMemo`.

**Code Example**:
```jsx
const value = useMemo(() => ({ user, theme }), [user, theme]);
return <Ctx.Provider value={value}>{children}</Ctx.Provider>;
```

---

<a id="q53"></a>
### Q53: What are Higher-Order Components and what are their limitations?

**Difficulty**: Intermediate

**Strategy**:
Functions returning enhanced components; limitations include prop collisions and wrapper hell.

**Code Example**:
```jsx
export const withLogger = (Comp) => (props) => { console.log('Render', props); return <Comp {...props}/>; };
```

---

<a id="q54"></a>
### Q54: How do you implement Undo/Redo history in React state?

**Difficulty**: Advanced

**Strategy**:
Maintain past, present, and future state arrays in a reducer.

**Code Example**:
```javascript
function undoReducer(state, action) {
  if (action.type === 'UNDO') return { past: state.past.slice(0, -1), present: state.past[state.past.length - 1], future: [state.present, ...state.future] };
  return state;
}
```

---

<a id="q55"></a>
### Q55: What is the purpose of `useImperativeHandle`?

**Difficulty**: Advanced

**Strategy**:
Exposes imperative methods when parent component accesses ref.

**Code Example**:
```jsx
useImperativeHandle(ref, () => ({ scroll: () => ref.current.scrollIntoView() }));
```

---

<a id="q56"></a>
### Q56: How do you debounce API validation in React Hook Form?

**Difficulty**: Intermediate

**Strategy**:
Debounce validation handler with lodash or custom timer.

**Code Example**:
```jsx
const debouncedValidate = debounce(checkUsername, 500);
```

---

<a id="q57"></a>
### Q57: What is the difference in event delegation between React 16 and 17+?

**Difficulty**: Advanced

**Strategy**:
React 17+ attaches event listeners to root container rather than `document`.

**Code Example**:
```javascript
// In React 17+, document.addEventListener runs before React synthetic events
```

---

<a id="q58"></a>
### Q58: How do you implement Skeleton Loaders during data fetching?

**Difficulty**: Beginner

**Strategy**:
Render placeholder pulse shapes while `loading` state is true.

**Code Example**:
```jsx
{loading ? <div className="skeleton" /> : <Content data={data} />}
```

---

<a id="q59"></a>
### Q59: How do you control HTML `<dialog>` element in React?

**Difficulty**: Intermediate

**Strategy**:
Use `ref.current.showModal()` and `ref.current.close()`.

**Code Example**:
```jsx
const ref = useRef();
<dialog ref={ref}><button onClick={() => ref.current.close()}>Close</button></dialog>
```

---

<a id="q60"></a>
### Q60: How does Server-Side Rendering (SSR) improve SEO?

**Difficulty**: Intermediate

**Strategy**:
Search engines receive pre-rendered HTML content on first response.

**Code Example**:
```javascript
// Full HTML content available immediately for search crawlers
```

---

<a id="q61"></a>
### Q61: What is Static Site Generation (SSG)?

**Difficulty**: Beginner

**Strategy**:
Pre-generates static HTML pages at build time.

**Code Example**:
```javascript
// Pages generated once at build time for instant CDN delivery
```

---

<a id="q62"></a>
### Q62: What is Incremental Static Regeneration (ISR)?

**Difficulty**: Advanced

**Strategy**:
Regenerates static pages in background on incoming requests after revalidation period.

**Code Example**:
```javascript
// export const revalidate = 60;
```

---

<a id="q63"></a>
### Q63: What is `React.cloneElement` and why is it discouraged in modern React?

**Difficulty**: Intermediate

**Strategy**:
Clones element and injects props; discouraged because it obscures data flow compared to Context or Render Props.

**Code Example**:
```jsx
React.cloneElement(child, { isActive: true })
```

---

<a id="q64"></a>
### Q64: How do you build a Global Toast Notification system in React?

**Difficulty**: Intermediate

**Strategy**:
Use Context Provider with reducer queue and auto-dismiss timer.

**Code Example**:
```jsx
const { addToast } = useToast();
addToast('Saved successfully', 'success');
```

---

<a id="q65"></a>
### Q65: How do you memoize recursive components in React?

**Difficulty**: Advanced

**Strategy**:
Wrap recursive component in `React.memo` with stable parent callbacks.

**Code Example**:
```jsx
const TreeNode = React.memo(({ node }) => (
  <div>{node.name}{node.children?.map(c => <TreeNode key={c.id} node={c}/>)}</div>
));
```

---

<a id="q66"></a>
### Q66: What is State Hoisting (Lifting State Up)?

**Difficulty**: Beginner

**Strategy**:
Moving state to nearest common ancestor so sibling components can share it.

**Code Example**:
```jsx
function Parent() {
  const [val, setVal] = useState('');
  return <><Input val={val} setVal={setVal}/><Display val={val}/></>;
}
```

---

<a id="q67"></a>
### Q67: How do you build dynamic breadcrumb navigation in React?

**Difficulty**: Intermediate

**Strategy**:
Parse current pathname and map segments to links.

**Code Example**:
```jsx
const paths = location.pathname.split('/').filter(Boolean);
```

---

<a id="q68"></a>
### Q68: What is the difference between `PureComponent` and `Component`?

**Difficulty**: Beginner

**Strategy**:
`PureComponent` automatically implements `shouldComponentUpdate` with shallow prop/state comparison.

**Code Example**:
```jsx
class Card extends React.PureComponent { render() { return <div>{this.props.title}</div>; } }
```

---

<a id="q69"></a>
### Q69: How do you track file upload progress in React?

**Difficulty**: Intermediate

**Strategy**:
Use Axios `onUploadProgress` or XMLHttpRequest upload listener.

**Code Example**:
```javascript
axios.post('/upload', formData, { onUploadProgress: e => setProgress(Math.round((e.loaded * 100) / e.total)) });
```

---

<a id="q70"></a>
### Q70: How do you implement responsive table card layouts in React?

**Difficulty**: Intermediate

**Strategy**:
Use CSS Grid and media queries to convert table rows into card elements on mobile.

**Code Example**:
```css
@media (max-width: 600px) { tr { display: flex; flex-direction: column; } }
```

---

<a id="q71"></a>
### Q71: What is the difference between `<React.Fragment>` and `<>` shorthand?

**Difficulty**: Beginner

**Strategy**:
`<React.Fragment>` accepts `key` attribute; `<>` shorthand does not.

**Code Example**:
```jsx
<React.Fragment key={id}><div>1</div><div>2</div></React.Fragment>
```

---

<a id="q72"></a>
### Q72: How do you handle keyboard arrow navigation in Tabs?

**Difficulty**: Intermediate

**Strategy**:
Listen for ArrowLeft / ArrowRight keydown events and shift active tab focus.

**Code Example**:
```jsx
onKeyDown={e => { if (e.key === 'ArrowRight') nextTab(); }}
```

---

<a id="q73"></a>
### Q73: What is the difference between `window.location.href` and React Router `navigate`?

**Difficulty**: Beginner

**Strategy**:
`window.location.href` triggers full page reload; `navigate` performs fast client-side transition.

**Code Example**:
```jsx
navigate('/dashboard');
```

---

<a id="q74"></a>
### Q74: How do you mock API calls in Jest without extra libraries?

**Difficulty**: Intermediate

**Strategy**:
Mock `global.fetch` with `jest.fn()` returning a resolved Promise.

**Code Example**:
```javascript
global.fetch = jest.fn(() => Promise.resolve({ json: () => Promise.resolve({ data: 123 }) }));
```

---

<a id="q75"></a>
### Q75: How do you test custom hooks using `renderHook`?

**Difficulty**: Intermediate

**Strategy**:
Use `renderHook` from `@testing-library/react` and wrap state changes in `act`.

**Code Example**:
```tsx
const { result } = renderHook(() => useCounter());
act(() => result.current.inc());
expect(result.current.count).toBe(1);
```

---

<a id="q76"></a>
### Q76: What is Micro-frontend Module Federation with React?

**Difficulty**: Advanced

**Strategy**:
Dynamically imports independent React builds at runtime across multiple domains.

**Code Example**:
```javascript
// ModuleFederationPlugin config
```

---

<a id="q77"></a>
### Q77: How do you optimize Core Web Vitals (LCP, INP, CLS) in React?

**Difficulty**: Advanced

**Strategy**:
Preload hero images, split heavy bundles, reserve aspect-ratio boxes, and defer non-critical JS.

**Code Example**:
```jsx
<img src="/hero.webp" fetchPriority="high" />
```

---

<a id="q78"></a>
### Q78: How do you implement Copy to Clipboard with temporary tooltip?

**Difficulty**: Beginner

**Strategy**:
Use `navigator.clipboard.writeText` and timeout state.

**Code Example**:
```jsx
const copy = () => { navigator.clipboard.writeText(text); setCopied(true); setTimeout(() => setCopied(false), 2000); };
```

---

<a id="q79"></a>
### Q79: What is the difference between dependencies and peerDependencies in React packages?

**Difficulty**: Intermediate

**Strategy**:
`dependencies` are installed by the package; `peerDependencies` must be installed by host application.

**Code Example**:
```json
"peerDependencies": { "react": ">=18.0.0" }
```

---

<a id="q80"></a>
### Q80: How do you build an accessible Dropdown menu in React?

**Difficulty**: Intermediate

**Strategy**:
Use `aria-haspopup="true"`, `aria-expanded`, and Escape key to close.

**Code Example**:
```jsx
<button aria-haspopup="true" aria-expanded={open} onClick={toggle}>Menu</button>
```

---

<a id="q81"></a>
### Q81: How do you test Error Boundary components with React Testing Library?

**Difficulty**: Intermediate

**Strategy**:
Spy on `console.error` and assert fallback UI is visible when child throws.

**Code Example**:
```jsx
render(<ErrorBoundary><Bomb /></ErrorBoundary>);
expect(screen.getByRole('alert')).toBeInTheDocument();
```

---

<a id="q82"></a>
### Q82: What was SyntheticEvent pooling in React 16 and why was it removed in React 17?

**Difficulty**: Advanced

**Strategy**:
React 16 reused event objects across ticks for memory efficiency; React 17 removed it so events can be accessed asynchronously without `e.persist()`.

**Code Example**:
```javascript
// In React 17+, event properties can be accessed in async callbacks safely
```

---

<a id="q83"></a>
### Q83: How do you implement custom `useHover` hook?

**Difficulty**: Intermediate

**Strategy**:
Listen for `mouseenter` and `mouseleave` events.

**Code Example**:
```typescript
export function useHover(ref: any) {
  const [hovered, setHovered] = useState(false);
  useEffect(() => {
    const on = () => setHovered(true), off = () => setHovered(false);
    const el = ref.current;
    el?.addEventListener('mouseenter', on);
    el?.addEventListener('mouseleave', off);
    return () => { el?.removeEventListener('mouseenter', on); el?.removeEventListener('mouseleave', off); };
  }, [ref]);
  return hovered;
}
```

---

<a id="q84"></a>
### Q84: How do you handle i18n localization in React?

**Difficulty**: Intermediate

**Strategy**:
Use `react-i18next` with JSON translation resources.

**Code Example**:
```jsx
const { t } = useTranslation();
return <h1>{t('welcome_message')}</h1>;
```

---

<a id="q85"></a>
### Q85: What are the advantages of `pnpm` in React monorepos?

**Difficulty**: Intermediate

**Strategy**:
Content-addressable store hard-links packages, preventing phantom dependencies and saving disk space.

**Code Example**:
```bash
pnpm install
```

---

<a id="q86"></a>
### Q86: How do you implement pagination with ellipsis in React?

**Difficulty**: Intermediate

**Strategy**:
Generate page array `[1, '...', curr-1, curr, curr+1, '...', total]`.

**Code Example**:
```jsx
const pages = getPaginationRange(current, total);
```

---

<a id="q87"></a>
### Q87: What is client state vs server state in React applications?

**Difficulty**: Intermediate

**Strategy**:
Client state handles local UI controls; server state handles remote persisted data requiring caching/invalidation.

**Code Example**:
```javascript
// Client: const [isOpen, setOpen] = useState(false);
// Server: const { data } = useQuery(['user'], fetchUser);
```

---

<a id="q88"></a>
### Q88: How do you implement auto-saving forms in React?

**Difficulty**: Intermediate

**Strategy**:
Debounce changes and fire background PATCH requests with save indicators.

**Code Example**:
```jsx
useDebounceEffect(() => { api.save(formData); }, 1000, [formData]);
```

---

<a id="q89"></a>
### Q89: How do you build a custom Range Slider in React?

**Difficulty**: Intermediate

**Strategy**:
Control `<input type="range">` and compute CSS gradient progress fill.

**Code Example**:
```jsx
<input type="range" min="0" max="100" value={val} onChange={e => setVal(e.target.value)} />
```

---

<a id="q90"></a>
### Q90: What are React Server Actions and how do they replace API routes?

**Difficulty**: Advanced

**Strategy**:
Async server functions called directly from client forms with automatic serialization.

**Code Example**:
```jsx
async function create(formData) { 'use server'; await db.insert(formData); }
```

---

<a id="q91"></a>
### Q91: How do you implement WebAuthn biometric login in React?

**Difficulty**: Advanced

**Strategy**:
Call `navigator.credentials.get()` for biometric passkey authentication.

**Code Example**:
```javascript
const cred = await navigator.credentials.get({ publicKey: options });
```

---

<a id="q92"></a>
### Q92: How do you create animated notification badges in React?

**Difficulty**: Beginner

**Strategy**:
Trigger CSS keyframe bounce animation whenever count changes.

**Code Example**:
```css
@keyframes bounce { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.3); } }
```

---

<a id="q93"></a>
### Q93: What is the difference between `useCallback` and regular inline functions?

**Difficulty**: Beginner

**Strategy**:
Inline functions create new references every render; `useCallback` returns cached function identity.

**Code Example**:
```jsx
const fn = useCallback(() => doWork(id), [id]);
```

---

<a id="q94"></a>
### Q94: How do you implement sticky headers in React?

**Difficulty**: Beginner

**Strategy**:
Use CSS `position: sticky; top: 0; z-index: 10;`.

**Code Example**:
```css
.header { position: sticky; top: 0; z-index: 100; }
```

---

<a id="q95"></a>
### Q95: How do you structure enterprise React codebases?

**Difficulty**: Advanced

**Strategy**:
Feature-based architecture with modules containing UI, hooks, api, and tests.

**Code Example**:
```
src/features/auth/{components, hooks, api, authSlice.ts}
```

---

<a id="q96"></a>
### Q96: How do you test accessibility with `@axe-core/react`?

**Difficulty**: Intermediate

**Strategy**:
Log WCAG violations directly to developer console.

**Code Example**:
```javascript
if (process.env.NODE_ENV !== 'production') { axe(React, ReactDOM, 1000); }
```

---

<a id="q97"></a>
### Q97: What is the difference between SPA and MPA?

**Difficulty**: Beginner

**Strategy**:
SPA renders client-side without full reloads; MPA requests full HTML documents per route.

**Code Example**:
```javascript
// SPA provides app-like fluid navigation
```

---

<a id="q98"></a>
### Q98: How do you handle multi-tab session expiration in React?

**Difficulty**: Advanced

**Strategy**:
Broadcast logout messages via `BroadcastChannel` or `localStorage` events.

**Code Example**:
```javascript
const bc = new BroadcastChannel('auth');
bc.onmessage = (e) => { if (e.data === 'logout') logout(); };
```

---

<a id="q99"></a>
### Q99: How do you implement custom `useCountdown` hook?

**Difficulty**: Intermediate

**Strategy**:
Decrement seconds using `setInterval` until reaching zero.

**Code Example**:
```typescript
export function useCountdown(initialSec: number) {
  const [sec, setSec] = useState(initialSec);
  useEffect(() => {
    if (sec <= 0) return;
    const id = setInterval(() => setSec(s => s - 1), 1000);
    return () => clearInterval(id);
  }, [sec]);
  return sec;
}
```

---

<a id="q100"></a>
### Q100: What is shallow routing in React Router?

**Difficulty**: Intermediate

**Strategy**:
Updates URL query params without reloading route data loaders.

**Code Example**:
```jsx
setSearchParams({ filter: 'active' });
```

---
