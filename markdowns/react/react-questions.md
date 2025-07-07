# React.js Interview Questions

## Table of Contents
1. [Q1: What is React and what are its key features?](#q1-what-is-react-and-what-are-its-key-features)
2. [Q2: Explain the difference between functional and class components.](#q2-explain-the-difference-between-functional-and-class-components)
3. [Q3: What is JSX and how does it work?](#q3-what-is-jsx-and-how-does-it-work)
4. [Q4: How do you pass data between components?](#q4-how-do-you-pass-data-between-components)
5. [Q5: Explain useState and how to manage state in functional components.](#q5-explain-usestate-and-how-to-manage-state-in-functional-components)
6. [Q6: Explain useEffect and its use cases.](#q6-explain-useeffect-and-its-use-cases)
7. [Q7: Explain React Server Components and how they differ from traditional React components.](#q7-explain-react-server-components-and-how-they-differ-from-traditional-react-components)
8. [Q8: How do you optimize React application performance using React.memo, useMemo, and useCallback?](#q8-how-do-you-optimize-react-application-performance-using-reactmemo-usememo-and-usecallback)
9. [Q9: How do you implement error boundaries and error handling in React applications?](#q9-how-do-you-implement-error-boundaries-and-error-handling-in-react-applications)
10. [Q10: Explain React Context API and when to use it over prop drilling.](#q10-explain-react-context-api-and-when-to-use-it-over-prop-drilling)
11. [Q11: What are Higher-Order Components (HOCs) and how do you implement them?](#q11-what-are-higher-order-components-hocs-and-how-do-you-implement-them)
12. [Q12: How do you test React components using Jest and React Testing Library?](#q12-how-do-you-test-react-components-using-jest-and-react-testing-library)
13. [Q13: How do you implement and test React Router navigation?](#q13-how-do-you-implement-and-test-react-router-navigation)
14. [Q14: How do you implement React Suspense and Concurrent Features?](#q14-how-do-you-implement-react-suspense-and-concurrent-features)
15. [Q15: How do you implement custom React hooks for complex state management?](#q15-how-do-you-implement-custom-react-hooks-for-complex-state-management)
16. [Q16: How do you implement React Server Components and streaming SSR?](#q16-how-do-you-implement-react-server-components-and-streaming-ssr)
17. [Q17: How do you implement advanced React patterns like Compound Components and Render Props?](#q17-how-do-you-implement-advanced-react-patterns-like-compound-components-and-render-props)
18. [Q18: How do you implement micro-frontends with React and Module Federation?](#q18-how-do-you-implement-micro-frontends-with-react-and-module-federation)
19. [Q19: How do you implement advanced React performance optimization techniques?](#q19-how-do-you-implement-advanced-react-performance-optimization-techniques)
20. [Q20: How do you implement React 18+ concurrent features and automatic batching?](#q20-how-do-you-implement-react-18-concurrent-features-and-automatic-batching)
21. [Q21: How do you implement React Server Components and modern full-stack React architecture?](#q21-how-do-you-implement-react-server-components-and-modern-full-stack-react-architecture)
22. [Q22: What is the difference between controlled and uncontrolled components in React?](#q22-what-is-the-difference-between-controlled-and-uncontrolled-components-in-react)
23. [Q23: What does it mean to "lift state up" in React?](#q23-what-does-it-mean-to-lift-state-up-in-react)
24. [Q24: What are keys in React and why are they important?](#q24-what-are-keys-in-react-and-why-are-they-important)
25. [Q25: Explain the component lifecycle in React.](#q25-explain-the-component-lifecycle-in-react)
26. [Q26: How do you handle conditional rendering in React?](#q26-how-do-you-handle-conditional-rendering-in-react)
27. [Q27: What is the difference between `useEffect` and `useLayoutEffect`?](#q27-what-is-the-difference-between-useeffect-and-uselayouteffect)
28. [Q28: What are `useMemo` and `useCallback` used for?](#q28-what-are-usememo-and-usecallback-used-for)
29. [Q29: What is `React.memo()` and how does it work?](#q29-what-is-reactmemo-and-how-does-it-work)
30. [Q30: What are Portals in React and what are they used for?](#q30-what-are-portals-in-react-and-what-are-they-used-for)
31. [Q31: What are Error Boundaries in React?](#q31-what-are-error-boundaries-in-react)
32. [Q32: What are Fragments in React?](#q32-what-are-fragments-in-react)
33. [Q33: What is Strict Mode in React?](#q33-what-is-strict-mode-in-react)
34. [Q34: What are the main differences between JSX and HTML?](#q34-what-are-the-main-differences-between-jsx-and-html)
35. [Q35: What are refs in React and what are they used for?](#q35-what-are-refs-in-react-and-what-are-they-used-for)
36. [Q36: What is `forwardRef` in React?](#q36-what-is-forwardref-in-react)
37. [Q37: What is the difference between the Shadow DOM and the Virtual DOM?](#q37-what-is-the-difference-between-the-shadow-dom-and-the-virtual-dom)
38. [Q38: What are Synthetic Events in React?](#q38-what-are-synthetic-events-in-react)
39. [Q39: What is reconciliation in React?](#q39-what-is-reconciliation-in-react)
40. [Q40: What is prop drilling and how can you avoid it?](#q40-what-is-prop-drilling-and-how-can-you-avoid-it)
41. [Q41: What are the differences between class and functional components?](#q41-what-are-the-differences-between-class-and-functional-components)
42. [Q42: What is the `children` prop in React?](#q42-what-is-the-children-prop-in-react)
43. [Q43: What is the difference between `React.Component` and `React.PureComponent`?](#q43-what-is-the-difference-between-reactcomponent-and-reactpurecomponent)
44. [Q44: What is the difference between stateful and stateless components?](#q44-what-is-the-difference-between-stateful-and-stateless-components)
45. [Q45: How do you make an AJAX request in React?](#q45-how-do-you-make-an-ajax-request-in-react)
46. [Q46: What are the Rules of Hooks?](#q46-what-are-the-rules-of-hooks)
47. [Q47: What is the `useReducer` hook and when should you use it?](#q47-what-is-the-usereducer-hook-and-when-should-you-use-it)
48. [Q48: What is the `useImperativeHandle` hook?](#q48-what-is-the-useimperativehandle-hook)
49. [Q49: What is `useLayoutEffect` and how is it different from `useEffect`?](#q49-what-is-uselayouteffect-and-how-is-it-different-from-useeffect)
50. [Q50: What is the `useCallback` hook and why is it useful?](#q50-what-is-the-usecallback-hook-and-why-is-it-useful)
51. [Q51: What is the `useMemo` hook and how is it different from `useCallback`?](#q51-what-is-the-usememo-hook-and-how-is-it-different-from-usecallback)
52. [Q52: What are custom Hooks and why are they useful?](#q52-what-are-custom-hooks-and-why-are-they-useful)
53. [Q53: What is React Router and what are its main components?](#q53-what-is-react-router-and-what-are-its-main-components)
54. [Q54: What is the difference between `<Link>` and `<NavLink>` in React Router?](#q54-what-is-the-difference-between-link-and-navlink-in-react-router)
55. [Q55: How do you handle 404 (Not Found) pages in React Router?](#q55-how-do-you-handle-404-not-found-pages-in-react-router)
56. [Q56: How do you pass data through routes in React Router?](#q56-how-do-you-pass-data-through-routes-in-react-router)
57. [Q57: How do you perform programmatic navigation in React Router?](#q57-how-do-you-perform-programmatic-navigation-in-react-router)
58. [Q58: What are nested routes and how do you implement them in React Router?](#q58-what-are-nested-routes-and-how-do-you-implement-them-in-react-router)
59. [Q59: How do you create protected routes in React Router?](#q59-how-do-you-create-protected-routes-in-react-router)
60. [Q60: What is lazy loading and how do you implement it in React?](#q60-what-is-lazy-loading-and-how-do-you-implement-it-in-react)
61. [Q61: What is Redux and what are its core principles?](#q61-what-is-redux-and-what-are-its-core-principles)
62. [Q62: What is the difference between `connect()` and React Redux hooks like `useSelector` and `useDispatch`?](#q62-what-is-the-difference-between-connect-and-react-redux-hooks-like-useselector-and-usedispatch)
63. [Q63: What is Redux middleware and what is it used for?](#q63-what-is-redux-middleware-and-what-is-it-used-for)
64. [Q64: What is the difference between Redux Thunk and Redux Saga?](#q64-what-is-the-difference-between-redux-thunk-and-redux-saga)
65. [Q65: What is Redux Toolkit and why is it recommended for Redux development?](#q65-what-is-redux-toolkit-and-why-is-it-recommended-for-redux-development)
66. [Q66: How do you test React components?](#q66-how-do-you-test-react-components)
67. [Q67: How do you mock functions, modules, and components in Jest?](#q67-how-do-you-mock-functions-modules-and-components-in-jest)
68. [Q68: What is the difference between `getBy`, `queryBy`, and `findBy` queries in React Testing Library?](#q68-what-is-the-difference-between-getby-queryby-and-findby-queries-in-react-testing-library)
69. [Q69: What is the difference between `fireEvent` and `user-event` in React Testing Library?](#q69-what-is-the-difference-between-fireevent-and-user-event-in-react-testing-library)
70. [Q70: What is the `act()` function in React Testing Library, and when should you use it?](#q70-what-is-the-act-function-in-react-testing-library-and-when-should-you-use-it)

---

## React Fundamentals

### Q1: What is React and what are its key features?
**Difficulty: Easy**

**Answer:**
React is a JavaScript library for building user interfaces, particularly web applications. It was developed by Facebook and is now maintained by Meta and the open-source community.

**Key Features:**

1. **Virtual DOM**: React creates a virtual representation of the DOM in memory, which allows for efficient updates by comparing (diffing) the virtual DOM with the actual DOM and updating only the parts that have changed.

2. **Component-Based Architecture**: React applications are built using reusable components that encapsulate their own state and logic.

3. **Unidirectional Data Flow**: Data flows down from parent to child components through props, making the application predictable and easier to debug.

4. **JSX Syntax**: JavaScript XML allows you to write HTML-like syntax within JavaScript, making component creation more intuitive.

5. **Declarative Programming**: You describe what the UI should look like for any given state, and React handles the how.

```jsx
// Example of a simple React component
import React, { useState }
```

```jsx
// components/InteractiveButton.js (Client Component)
'use client';

import { useState, useTransition } from 'react';
import { followUser, unfollowUser } from '@/lib/actions';

export function InteractiveButton({ userId }) {
  const [isFollowing, setIsFollowing] = useState(false);
  const [isPending, startTransition] = useTransition();
  
  const handleFollow = () => {
    startTransition(async () => {
      if (isFollowing) {
        await unfollowUser(userId);
        setIsFollowing(false);
      } else {
        await followUser(userId);
        setIsFollowing(true);
      }
    });
  };
  
  return (
    <button 
      onClick={handleFollow}
      disabled={isPending}
      className={`follow-btn ${isFollowing ? 'following' : ''}`}
    >
      {isPending ? 'Loading...' : isFollowing ? 'Unfollow' : 'Follow'}
    </button>
  );
}
```

```jsx
// components/InteractiveButton.js (Client Component)
'use client';

import { useState, useTransition } from 'react';
import { followUser, unfollowUser } from '@/lib/actions';

export function InteractiveButton({ userId }) {
  const [isFollowing, setIsFollowing] = useState(false);
  const [isPending, startTransition] = useTransition();
  
  const handleFollow = () => {
    startTransition(async () => {
      if (isFollowing) {
        await unfollowUser(userId);
        setIsFollowing(false);
      } else {
        await followUser(userId);
        setIsFollowing(true);
      }
    });
  };
  
  return (
    <button 
      onClick={handleFollow}
      disabled={isPending}
      className={`follow-btn ${isFollowing ? 'following' : ''}`}
    >
      {isPending ? 'Loading...' : isFollowing ? 'Unfollow' : 'Follow'}
    </button>
  );
}
```

**3. Server Actions for Form Handling:**

```jsx
// lib/actions.js (Server Actions)
'use server';

import { db } from './database';
import { revalidatePath } from 'next/cache';
import { redirect } from 'next/navigation';

export async function createPost(formData) {
  const title = formData.get('title');
  const content = formData.get('content');
  const userId = formData.get('userId');
  
  // Validation
  if (!title || !content) {
    return { error: 'Title and content are required' };
  }
  
  try {
    const result = await db.query(
      'INSERT INTO posts (title, content, user_id, created_at) VALUES (?, ?, ?, NOW())',
      [title, content, userId]
    );
    
    // Revalidate the posts page to show new post
    revalidatePath('/posts');
    
    // Redirect to the new post
    redirect(`/posts/${result.insertId}`);
  } catch (error) {
    console.error('Failed to create post:', error);
    return { error: 'Failed to create post' };
  }
}

export async function updatePost(postId, formData) {
  const title = formData.get('title');
  const content = formData.get('content');
  
  try {
    await db.query(
      'UPDATE posts SET title = ?, content = ?, updated_at = NOW() WHERE id = ?',
      [title, content, postId]
    );
    
    revalidatePath(`/posts/${postId}`);
    return { success: true };
  } catch (error) {
    return { error: 'Failed to update post' };
  }
}
```

**4. Data Fetching and Caching Patterns:**

```jsx
// lib/data.js
import { cache } from 'react';
import { db } from './database';

// Cache function calls across the request
export const getUser = cache(async (userId) => {
  console.log('Fetching user:', userId); // Only logs once per request
  
  const user = await db.query(
    'SELECT * FROM users WHERE id = ?',
    [userId]
  );
  
  return user[0];
});

export const getUserPosts = cache(async (userId, limit = 10) => {
  const posts = await db.query(
    'SELECT * FROM posts WHERE user_id = ? ORDER BY created_at DESC LIMIT ?',
    [userId, limit]

---

### Q22: What is the difference between controlled and uncontrolled components in React?

**Answer:**
The distinction between controlled and uncontrolled components in React revolves around who manages the state of form elements (like `<input>`, `<textarea>`, and `<select>`).

#### Controlled Components

In a controlled component, the state of the form element is managed by the React component itself, typically using the `useState` hook. The value of the input is driven by the component's state, and any changes to the input are handled by an `onChange` event handler that updates the state.

**Key Characteristics:**

1.  **State Management:** The component's state is the single source of truth for the input's value.
2.  **Data Flow:** The value flows from the component's state to the input (`value` prop), and changes flow back from the input to the component's state (`onChange` handler).
3.  **Predictable:** Since the state is managed by React, the component's behavior is more predictable and easier to debug.

**Example:**

```jsx
import React, { useState } from 'react';

function ControlledForm() {
  const [name, setName] = useState('');

  const handleChange = (event) => {
    setName(event.target.value);
  };

  const handleSubmit = (event) => {
    alert('A name was submitted: ' + name);
    event.preventDefault();
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Name:
        <input type="text" value={name} onChange={handleChange} />
      </label>
      <input type="submit" value="Submit" />
    </form>
  );
}
```

#### Uncontrolled Components

In an uncontrolled component, the state of the form element is managed by the DOM itself. Instead of using state to manage the value, you use a **ref** to get the value from the DOM when you need it (e.g., when the form is submitted).

**Key Characteristics:**

1.  **State Management:** The DOM is the source of truth for the input's value.
2.  **Data Flow:** Data is pulled from the DOM when needed, typically using a ref.
3.  **Simpler for Simple Forms:** Can be less code for simple forms, as you don't need to write an event handler for every state change.

**Example:**

```jsx
import React, { useRef } from 'react';

function UncontrolledForm() {
  const inputRef = useRef(null);

  const handleSubmit = (event) => {
    alert('A name was submitted: ' + inputRef.current.value);
    event.preventDefault();
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Name:
        <input type="text" ref={inputRef} />
      </label>
      <input type="submit" value="Submit" />
    </form>
  );
}
```

#### Summary Table

| Feature             | Controlled Component                         | Uncontrolled Component                       |
| :------------------ | :------------------------------------------- | :------------------------------------------- |
| **Source of Truth** | React component state (`useState`)           | The DOM itself                               |
| **Data Flow**       | Two-way binding (value prop and `onChange`)  | One-way (pull data from DOM with a ref)      |
| **Use Case**        | Complex forms, validation, dynamic inputs    | Simple forms, integrating with non-React code |
| **Predictability**  | High                                         | Lower, as state is not managed by React      |

**When to Use Which:**
-   Use **controlled components** for most cases, as they provide more control and predictability.
-   Use **uncontrolled components** for simple forms, or when integrating with non-React libraries that manage their own DOM.

---

### Q23: What does it mean to "lift state up" in React?

**Answer:**
"Lifting state up" is a common pattern in React for sharing state between components. It involves moving the state from a child component to its closest common ancestor component. The ancestor then passes the state down to the children that need it via props, and provides functions to the children to update that state.

This pattern is used when multiple components need to reflect the same changing data. By centralizing the state in a parent component, you create a **single source of truth**, which helps to avoid inconsistencies and makes the application easier to manage.

#### How It Works:

1.  **Identify Shared State:** Find the state that needs to be accessed by multiple sibling components.
2.  **Find a Common Ancestor:** Locate the closest common parent component of the siblings.
3.  **Lift the State:** Move the `useState` declaration from the child component to the common ancestor.
4.  **Pass State Down:** Pass the state value down to the child components as props.
5.  **Pass Handlers Down:** Pass functions (event handlers) down to the child components as props. These functions will allow the children to update the state in the parent.

#### Example:

Imagine a temperature calculator where you have two inputs, one for Celsius and one for Fahrenheit. When you type in one input, the other should update accordingly. Both inputs need to share the temperature state.

```jsx
import React, { useState } from 'react';

// Child component for temperature input
function TemperatureInput({ scale, temperature, onTemperatureChange }) {
  const scaleNames = { c: 'Celsius', f: 'Fahrenheit' };

  return (
    <fieldset>
      <legend>Enter temperature in {scaleNames[scale]}:</legend>
      <input 
        value={temperature} 
        onChange={(e) => onTemperatureChange(e.target.value)} 
      />
    </fieldset>
  );
}

// Parent component that lifts state up
function Calculator() {
  const [temperature, setTemperature] = useState('');
  const [scale, setScale] = useState('c');

  const handleCelsiusChange = (temp) => {
    setTemperature(temp);
    setScale('c');
  };

  const handleFahrenheitChange = (temp) => {
    setTemperature(temp);
    setScale('f');
  };

  // Convert temperature based on the current scale
  const celsius = scale === 'f' ? (temperature - 32) * 5 / 9 : temperature;
  const fahrenheit = scale === 'c' ? (temperature * 9 / 5) + 32 : temperature;

  return (
    <div>
      <TemperatureInput 
        scale="c" 
        temperature={celsius} 
        onTemperatureChange={handleCelsiusChange} 
      />
      <TemperatureInput 
        scale="f" 
        temperature={fahrenheit} 
        onTemperatureChange={handleFahrenheitChange} 
      />
      <p>
        {celsius >= 100 ? 'The water would boil.' : 'The water would not boil.'}
      </p>
    </div>
  );
}
```

**Explanation:**
-   The `Calculator` component is the common ancestor that **owns the state** (`temperature` and `scale`).
-   It passes the current temperature and a callback function (`onTemperatureChange`) down to each `TemperatureInput`.
-   When an input value changes, it calls the function passed from the parent, which updates the parent's state. This triggers a re-render, and both inputs receive the new, converted values.

---

### Q24: What are keys in React and why are they important?

**Answer:**
Keys are a special string attribute you need to include when creating lists of elements in React. They help React identify which items have changed, are added, or are removed, making the process of updating the UI much more efficient.

#### Why are Keys Important?

When you render a list of components, React's reconciliation algorithm uses the keys to match the children in the original tree with the children in the subsequent tree. A stable and unique key for each item allows React to:

1.  **Efficiently Update the DOM:** Without keys, React would have to re-render the entire list if it changes. With keys, React can quickly identify which specific items were added, removed, or reordered, and only apply the necessary DOM mutations.

2.  **Preserve Component State:** If you have a list of stateful components, keys ensure that the state is preserved correctly when the list is updated. For example, if you reorder a list, React will move the component instance associated with a specific key, along with its state, to the new position.

3.  **Avoid Bugs:** Using the index of an array as a key is an anti-pattern, especially if the list can be reordered, filtered, or have items added/removed from the beginning. This can lead to incorrect state being displayed and performance issues, as React may end up updating the wrong component.

#### How to Use Keys:

-   **Keys must be unique** among siblings in a list. They don't need to be globally unique.
-   The best keys are **stable, predictable, and unique** identifiers from your data, such as a database ID.
-   Keys are an internal hint for React and are not passed down to the component as a prop.

**Example:**

```jsx
import React from 'react';

function TodoList({ todos }) {
  return (
    <ul>
      {todos.map((todo) => (
        // `todo.id` is a stable and unique identifier from the data
        <li key={todo.id}>
          {todo.text}
        </li>
      ))}
    </ul>
  );
}

const myTodos = [
  { id: 'a', text: 'Learn React' },
  { id: 'b', text: 'Build a project' },
  { id: 'c', text: 'Deploy the project' },
];

function App() {
  return <TodoList todos={myTodos} />;
}
```

**What happens if you don't use keys?**

React will log a warning in the console. While the application might still render, it can lead to the issues mentioned above, especially with dynamic lists. It's a fundamental best practice to always provide proper keys when rendering lists.

---

### Q25: Explain the component lifecycle in React.

**Answer:**
The component lifecycle in React refers to the sequence of phases a component goes through from its creation to its destruction. Understanding the lifecycle allows you to perform specific actions at different stages, such as fetching data, setting up subscriptions, or cleaning up resources.

The lifecycle differs between class components and functional components with hooks.

#### Class Component Lifecycle

The lifecycle of a class component is divided into three main phases:

1.  **Mounting:** Putting elements into the DOM.
    -   `constructor()`: Initializes state and binds event handlers.
    -   `static getDerivedStateFromProps()`: Used to update state in response to a prop change before rendering.
    -   `render()`: The only required method. It returns the JSX for the component.
    -   `componentDidMount()`: Called immediately after the component is mounted. Ideal for network requests, subscriptions, or DOM manipulations.

2.  **Updating:** Re-rendering the component when props or state change.
    -   `static getDerivedStateFromProps()`: Called on every re-render.
    -   `shouldComponentUpdate()`: A performance optimization that determines if a re-render is necessary.
    -   `render()`: Re-renders the component.
    -   `getSnapshotBeforeUpdate()`: Captures information from the DOM (e.g., scroll position) before it's updated.
    -   `componentDidUpdate()`: Called after the component is updated. Ideal for side effects that depend on the new props or state.

3.  **Unmounting:** Removing the component from the DOM.
    -   `componentWillUnmount()`: Called just before the component is unmounted and destroyed. Ideal for cleanup, such as invalidating timers, canceling network requests, or removing event listeners.

**Example (Class Component):**

```jsx
import React, { Component } from 'react';

class LifecycleDemo extends Component {
  constructor(props) {
    super(props);
    this.state = { count: 0 };
    console.log('Constructor');
  }

  componentDidMount() {
    console.log('Component Did Mount');
    // Example: Fetch data
  }

  componentDidUpdate(prevProps, prevState) {
    console.log('Component Did Update');
    if (prevState.count !== this.state.count) {
      console.log('Count has changed.');
    }
  }

  componentWillUnmount() {
    console.log('Component Will Unmount');
    // Example: Clean up subscriptions
  }

  render() {
    console.log('Render');
    return (
      <div>
        <p>Count: {this.state.count}</p>
        <button onClick={() => this.setState({ count: this.state.count + 1 })}>
          Increment
        </button>
      </div>
    );
  }
}
```

#### Functional Component Lifecycle (with Hooks)

Functional components use hooks to replicate and manage lifecycle events. The `useEffect` hook is the primary tool for this.

-   **Mounting:** A `useEffect` with an empty dependency array `[]` runs only once, after the initial render, simulating `componentDidMount()`.

-   **Updating:** A `useEffect` with dependencies in its array `[prop, state]` runs after the initial render and whenever any of the specified dependencies change, simulating `componentDidUpdate()`.

-   **Unmounting:** The cleanup function returned from a `useEffect` hook simulates `componentWillUnmount()`. It runs when the component is unmounted or before the effect runs again.

**Example (Functional Component):**

```jsx
import React, { useState, useEffect } from 'react';

function LifecycleDemoFunc() {
  const [count, setCount] = useState(0);

  // Simulates componentDidMount
  useEffect(() => {
    console.log('Component Did Mount (Functional)');
  }, []);

  // Simulates componentDidUpdate for `count`
  useEffect(() => {
    console.log('Component Did Update (Functional) - count changed');
  }, [count]);

  // Simulates componentWillUnmount
  useEffect(() => {
    return () => {
      console.log('Component Will Unmount (Functional)');
    };
  }, []);

  console.log('Render (Functional)');
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}
```

---

### Q26: How do you handle conditional rendering in React?

**Answer:**
Conditional rendering in React is the process of displaying different UI elements or components based on certain conditions. It works the same way conditions work in JavaScript. There are several ways to achieve this.

#### 1. `if-else` Statement

This is the most basic way to conditionally render a component. You can use an `if` statement to return different JSX from your component based on a condition. This is often used for rendering entirely different components or layouts.

**Example:**

```jsx
import React from 'react';

function UserGreeting() {
  return <h1>Welcome back!</h1>;
}

function GuestGreeting() {
  return <h1>Please sign up.</h1>;
}

function Greeting({ isLoggedIn }) {
  if (isLoggedIn) {
    return <UserGreeting />;
  }
  return <GuestGreeting />;
}
```

#### 2. Ternary Operator

The conditional (ternary) operator (`condition ? trueValue : falseValue`) is a concise way to handle simple conditional rendering directly within your JSX. It's perfect for toggling between two options.

**Example:**

```jsx
import React from 'react';

function LoginStatus({ isLoggedIn }) {
  return (
    <div>
      The user is <b>{isLoggedIn ? 'currently' : 'not'}</b> logged in.
    </div>
  );
}
```

#### 3. Logical `&&` Operator (Short-Circuiting)

When you want to render something only if a condition is true (and render nothing otherwise), the logical `&&` operator is a clean and common pattern. If the condition is `true`, the element right after `&&` will appear in the output. If it is `false`, React will ignore and skip it.

**Example:**

```jsx
import React from 'react';

function Mailbox({ unreadMessages }) {
  return (
    <div>
      <h1>Hello!</h1>
      {unreadMessages.length > 0 &&
        <h2>
          You have {unreadMessages.length} unread messages.
        </h2>
      }
    </div>
  );
}
```

#### 4. Using Variables to Store Elements

You can use a variable to store a JSX element, and then conditionally assign a different element to it before rendering. This is useful when a part of the component needs to change based on a condition, while the rest remains the same.

**Example:**

```jsx
import React from 'react';

function LoginButton({ onClick }) {
  return <button onClick={onClick}>Login</button>;
}

function LogoutButton({ onClick }) {
  return <button onClick={onClick}>Logout</button>;
}

class LoginControl extends React.Component {
  constructor(props) {
    super(props);
    this.state = { isLoggedIn: false };
  }

  // ... event handlers

  render() {
    const { isLoggedIn } = this.state;
    let button;

    if (isLoggedIn) {
      button = <LogoutButton onClick={this.handleLogoutClick} />;
    } else {
      button = <LoginButton onClick={this.handleLoginClick} />;
    }

    return (
      <div>
        <Greeting isLoggedIn={isLoggedIn} />
        {button}
      </div>
    );
  }
}
```

By choosing the right method for each situation, you can create dynamic and responsive user interfaces that adapt to the application's state.

---

### Q27: What is the difference between `useEffect` and `useLayoutEffect`?

**Answer:**

Both `useEffect` and `useLayoutEffect` are hooks in React that allow you to perform side effects in function components. They share the same signature but differ in when they are fired. The key difference lies in their timing relative to the browser painting the screen.

#### `useEffect`

- **Timing**: Runs **asynchronously** *after* React has rendered the component and the browser has painted the changes to the screen.
- **Behavior**: It does not block the browser from painting. This means the user will see the updated UI before the effect runs.
- **Use Case**: This is the most common hook for side effects. It's suitable for data fetching, setting up subscriptions, and manually changing the DOM in ways that don't need to be synchronous. Using `useEffect` prevents the effect logic from blocking the visual updates, leading to a more responsive UI.

#### `useLayoutEffect`

- **Timing**: Runs **synchronously** *after* React has performed all DOM mutations but *before* the browser has painted the changes to the screen.
- **Behavior**: It blocks the browser's painting process. The browser will not paint the updated component until the `useLayoutEffect` code has finished running.
- **Use Case**: This is useful for side effects that need to read from the DOM and then synchronously re-render. For example, measuring the size or position of a DOM element and then updating the component's state based on that measurement. Using it prevents the user from seeing a flicker where the component first renders in one state and then quickly re-renders to another state after a measurement.

#### Summary Table

| Feature           | `useEffect`                                       | `useLayoutEffect`                                       |
| ----------------- | ------------------------------------------------- | ------------------------------------------------------- |
| **Timing**        | Asynchronous, after render and browser paint      | Synchronous, after render but before browser paint      |
| **Blocking**      | No, does not block browser painting               | Yes, blocks browser painting                            |
| **Common Use**    | Data fetching, subscriptions, non-urgent DOM updates | Reading DOM layout, synchronous DOM updates, animations |
| **Performance**   | Better for perceived performance (non-blocking)   | Can cause lag if the effect is slow (blocking)          |

#### Example: When to use `useLayoutEffect`

Imagine you have a tooltip that needs to be positioned next to an element. If you use `useEffect`, you might see the tooltip briefly appear at a default position before it's moved to the correct one, causing a flicker. `useLayoutEffect` solves this.

```jsx
import React, { useState, useLayoutEffect, useRef } from 'react';

function Tooltip() {
  const [show, setShow] = useState(false);
  const buttonRef = useRef(null);
  const tooltipRef = useRef(null);

  useLayoutEffect(() => {
    if (buttonRef.current && tooltipRef.current) {
      const { bottom } = buttonRef.current.getBoundingClientRect();
      tooltipRef.current.style.top = `${bottom + 10}px`;
    }
  }, [show]);

  return (
    <div>
      <button ref={buttonRef} onClick={() => setShow(s => !s)}>
        Hover me
      </button>
      {show && (
        <div ref={tooltipRef} style={{ position: 'absolute' }}>
          This is a tooltip!
        </div>
      )}
    </div>
  );
}
```

In this example, `useLayoutEffect` ensures that before the browser paints the tooltip, its position is already calculated and set, so the user never sees the flicker.

**Rule of Thumb**: Always start with `useEffect`. If you notice a visual flicker or need to perform DOM measurements, switch to `useLayoutEffect`.

---

### Q28: What are `useMemo` and `useCallback` used for?

**Answer:**

`useMemo` and `useCallback` are React hooks designed to optimize performance by memoizing values and functions. Memoization is a caching technique where the result of an expensive computation is stored and returned on subsequent calls with the same input, avoiding re-computation.

#### `useMemo`

`useMemo` memoizes the **result** of a function. It re-runs the function only when one of its dependencies has changed. This is useful for avoiding expensive calculations on every render.

- **Syntax**: `const memoizedValue = useMemo(() => computeExpensiveValue(a, b), [a, b]);`
- **Returns**: A memoized **value**.
- **Use Case**: When you have a computationally expensive function that is called in your component, and you want to avoid re-running it on every render unless its inputs change.

**Example:**

```jsx
import React, { useState, useMemo } from 'react';

function ExpensiveComponent({ num }) {
  const expensiveCalculation = (number) => {
    console.log('Performing expensive calculation...');
    // Simulate a delay
    for (let i = 0; i < 1000000000; i++) {}
    return number * 2;
  };

  const calculatedValue = useMemo(() => expensiveCalculation(num), [num]);

  return (
    <div>
      <p>Calculated Value: {calculatedValue}</p>
    </div>
  );
}
```

Without `useMemo`, `expensiveCalculation` would run every time the parent component re-renders, even if the `num` prop hasn't changed. With `useMemo`, it only runs when `num` changes.

#### `useCallback`

`useCallback` memoizes a **function definition**. It returns a memoized version of the callback that only changes if one of the dependencies has changed. This is particularly useful when passing callbacks to optimized child components that rely on reference equality to prevent unnecessary renders (e.g., components wrapped in `React.memo`).

- **Syntax**: `const memoizedCallback = useCallback(() => { doSomething(a, b); }, [a, b]);`
- **Returns**: A memoized **function**.
- **Use Case**: To prevent the re-creation of a function on every render. This is important when that function is a dependency of another hook (like `useEffect`) or is passed as a prop to a memoized component.

**Example:**

```jsx
import React, { useState, useCallback } from 'react';

const Button = React.memo(({ onClick }) => {
  console.log('Button rendered');
  return <button onClick={onClick}>Click Me</button>;
});

function ParentComponent() {
  const [count, setCount] = useState(0);

  const handleClick = useCallback(() => {
    console.log('Button clicked!');
  }, []); // Empty dependency array means the function is created only once

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment Count</button>
      <Button onClick={handleClick} />
    </div>
  );
}
```

In this example, because `handleClick` is wrapped in `useCallback`, its reference remains stable across re-renders of `ParentComponent`. As a result, the `Button` component (wrapped in `React.memo`) does not re-render when the `count` state changes, because its `onClick` prop has not changed.

#### Summary

| Hook          | What it Memoizes      | Returns          | Primary Use Case                                               |
| ------------- | --------------------- | ---------------- | -------------------------------------------------------------- |
| `useMemo`     | A function's **result** | A memoized value | Avoiding expensive calculations on every render.               |
| `useCallback` | A **function itself**   | A memoized function | Preventing re-renders of child components that rely on reference equality. |

In short: `useCallback(fn, deps)` is equivalent to `useMemo(() => fn, deps)`.

---

### Q29: What is `React.memo()` and how does it work?

**Answer:**

`React.memo()` is a higher-order component (HOC) that memoizes a functional component, preventing it from re-rendering if its props have not changed. It's a performance optimization tool that helps to avoid unnecessary render cycles.

#### How It Works

When you wrap a component in `React.memo()`, React will render the component and memoize (store) the result. Before the next render, React will do a shallow comparison of the new props with the old props. If the props are the same, React will reuse the memoized result, skipping the re-render. If the props are different, the component will re-render.

- **Shallow Comparison**: By default, `React.memo()` only performs a shallow comparison of props. This means it checks for equality on the top-level properties of the props object. If you pass complex objects or functions as props, their references will be compared, not their contents. This is why it's often used with `useCallback` for function props.

#### When to Use `React.memo()`

`React.memo()` is most effective when:

1.  **The component renders often**: If a component is part of a frequently updating UI, memoization can provide significant benefits.
2.  **The component has the same props for most re-renders**: If the props rarely change, you can save a lot of rendering work.
3.  **The component is reasonably complex**: The performance gain from skipping a render should outweigh the cost of comparing props. For very simple components, the overhead of memoization might not be worth it.

#### Example

Consider a parent component that re-renders frequently, passing props to a child component.

```jsx
import React, { useState } from 'react';

// A child component that we want to optimize
const Greeting = React.memo(function Greeting({ name }) {
  console.log(`Rendering Greeting for ${name}`);
  return <p>Hello, {name}!</p>;
});

function App() {
  const [count, setCount] = useState(0);
  const [name, setName] = useState('Alice');

  return (
    <div>
      <button onClick={() => setCount(count + 1)}>Increment Count: {count}</button>
      <input value={name} onChange={(e) => setName(e.target.value)} />
      <Greeting name={name} />
      <Greeting name="Bob" />
    </div>
  );
}
```

In this example:

- When you click the "Increment Count" button, the `App` component re-renders.
- The `Greeting` component with `name="Alice"` will re-render because its `name` prop might change (if you type in the input).
- However, the `Greeting` component with `name="Bob"` will **not** re-render. `React.memo()` compares its old prop (`{ name: 'Bob' }`) with the new prop (`{ name: 'Bob' }`), finds they are shallowly equal, and skips the render. You will not see "Rendering Greeting for Bob" in the console.

#### Custom Comparison Function

For more control, you can provide a custom comparison function as the second argument to `React.memo()`. This function receives the old and new props and should return `true` if the props are equal (preventing a re-render) and `false` otherwise.

```jsx
function areEqual(prevProps, nextProps) {
  // Custom logic to compare props
  // Return true if nextProps would result in the same output as prevProps
  return prevProps.user.id === nextProps.user.id;
}

const UserProfile = React.memo(MyComponent, areEqual);
```

This is useful when a shallow comparison is not sufficient, for example, when dealing with deeply nested objects.

---

### Q30: What are Portals in React and what are they used for?

**Answer:**

React Portals provide a first-class way to render children into a DOM node that exists outside the DOM hierarchy of the parent component. This allows a component's rendered output to "escape" its container in the DOM tree.

#### How It Works

You create a portal using `ReactDOM.createPortal(child, container)`:

-   `child`: Any renderable React child, such as an element, string, or fragment.
-   `container`: A DOM element that exists in the DOM, which will serve as the container for the `child`.

Even though a portal can be anywhere in the DOM tree, it behaves like a normal React child in every other way. It can access the props and context of the React tree it is defined in. This includes event bubbling—an event fired from inside a portal will propagate to ancestors in the React tree, even if those ancestors are not its ancestors in the DOM tree.

#### Why Use Portals?

Portals are ideal for UI elements that need to break out of their parent container's styling, such as:

1.  **Modals and Dialogs**: To ensure a modal overlay covers the entire viewport, it's best to render it as a direct child of `<body>`, avoiding `z-index` or `overflow: hidden` issues from parent components.
2.  **Tooltips and Popovers**: To position a tooltip correctly relative to the viewport without being clipped by a parent's boundaries.
3.  **Notifications**: To display global notifications at the top or bottom of the screen.

#### Example: Creating a Modal

First, you need a container in your main HTML file, typically a `<div>` right inside the `<body>`.

**`public/index.html`**
```html
<div id="root"></div>
<div id="modal-root"></div>
```

Next, create a `Modal` component that uses `ReactDOM.createPortal` to render its children into the `#modal-root` element.

**`Modal.js`**
```jsx
import React, { useEffect } from 'react';
import ReactDOM from 'react-dom';

// Get the DOM node to render the modal into
const modalRoot = document.getElementById('modal-root');

function Modal({ children }) {
  // Create a div element to append to the modal root
  const el = document.createElement('div');

  useEffect(() => {
    // Append the element to the modal root on mount
    modalRoot.appendChild(el);

    // Clean up by removing the element on unmount
    return () => {
      modalRoot.removeChild(el);
    };
  }, [el]);

  return ReactDOM.createPortal(children, el);
}

export default Modal;
```

Now, you can use the `Modal` component from anywhere in your application.

**`App.js`**
```jsx
import React, { useState } from 'react';
import Modal from './Modal';

function App() {
  const [showModal, setShowModal] = useState(false);

  return (
    <div>
      <button onClick={() => setShowModal(true)}>Show Modal</button>
      {showModal && (
        <Modal>
          <div className="modal-content">
            <h2>This is a Modal!</h2>
            <p>It is rendered outside the main #root div.</p>
            <button onClick={() => setShowModal(false)}>Close</button>
          </div>
        </Modal>
      )}
    </div>
  );
}
```

Even though the `Modal` is rendered inside the `App` component in the React tree, its DOM output appears in `#modal-root`. Clicking the "Close" button inside the modal will correctly update the `App` component's state because the event bubbles up through the React tree, not the DOM tree.

---

### Q31: What are Error Boundaries in React?

**Answer:**

Error Boundaries are React components that catch JavaScript errors anywhere in their child component tree, log those errors, and display a fallback UI instead of the component tree that crashed. They are a key part of making a React application resilient.

#### Key Concepts

-   **Catching Errors**: Error boundaries catch errors during rendering, in lifecycle methods, and in constructors of the whole tree below them.
-   **Limitations**: They do **not** catch errors for:
    -   Event handlers (use standard `try...catch` blocks for these).
    -   Asynchronous code (e.g., `setTimeout` or `requestAnimationFrame` callbacks).
    -   Server-side rendering.
    -   Errors thrown in the error boundary itself (rather than its children).
-   **Class Components**: As of React 18, error boundaries can only be implemented as class components. You need to define either (or both) of the static `getDerivedStateFromError()` or `componentDidCatch()` lifecycle methods.

#### How to Create an Error Boundary

You create an error boundary by making a class component with specific lifecycle methods.

1.  **`static getDerivedStateFromError(error)`**: This method is called during the "render" phase when a descendant component throws an error. It should return an object to update the component's state, which allows you to render a fallback UI on the next render. It is used to handle the fallback UI.

2.  **`componentDidCatch(error, errorInfo)`**: This method is called during the "commit" phase after an error has been thrown by a descendant component. It is used for side effects like logging the error to an external service.

**Example:**

```jsx
import React, { Component } from 'react';

class ErrorBoundary extends Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    // Update state so the next render will show the fallback UI.
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    // You can also log the error to an error reporting service
    console.error("Uncaught error:", error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      // You can render any custom fallback UI
      return <h1>Something went wrong.</h1>;
    }

    return this.props.children;
  }
}

export default ErrorBoundary;
```

#### How to Use an Error Boundary

You use an error boundary by wrapping it around any part of your component tree that you want to protect.

```jsx
import React from 'react';
import ErrorBoundary from './ErrorBoundary';

// A component that will throw an error
function BuggyCounter() {
  const [counter, setCounter] = React.useState(0);

  if (counter === 3) {
    // Simulate a JS error
    throw new Error('I crashed!');
  }

  return <h1 onClick={() => setCounter(counter + 1)}>{counter}</h1>;
}

function App() {
  return (
    <div>
      <p>Click on the numbers to increase the counter. It will crash at 3.</p>
      <hr />
      <ErrorBoundary>
        <p><b>This first counter is inside an error boundary.</b></p>
        <BuggyCounter />
      </ErrorBoundary>
      <hr />
      <p><b>This second counter is not, so it will crash the whole app.</b></p>
      <BuggyCounter />
    </div>
  );
}
```

In this example:

-   The first `BuggyCounter` is wrapped in an `ErrorBoundary`. When it crashes, the `ErrorBoundary` will catch the error and display the "Something went wrong" message. The rest of the application will remain functional.
-   The second `BuggyCounter` is not wrapped. When it crashes, the entire React application will unmount.

---

### Q32: What are Fragments in React?

**Answer:**

Fragments are a feature in React that let you group a list of children elements without adding extra nodes to the DOM. They provide a way to return multiple elements from a component's `render` method without having to wrap them in a parent `div` or another container element.

#### The Problem Fragments Solve

In React, a component's `render` method must return a single root element. Before Fragments, the common solution was to wrap the list of children in a `div`:

```jsx
// Before Fragments
render() {
  return (
    <div>
      <ChildA />
      <ChildB />
      <ChildC />
    </div>
  );
}
```

This approach works, but it introduces an unnecessary `<div>` into the DOM. This can lead to issues with invalid HTML (e.g., a `<td>` must be a child of a `<tr>`, but the extra `div` breaks this structure) and can add unnecessary nesting to the DOM tree, making styling and debugging more complex.

#### The Solution: Fragments

Fragments solve this by allowing you to group elements without creating an extra DOM node.

There are two main syntaxes for Fragments:

**1. The Long Syntax: `<React.Fragment>`**

This is the explicit syntax. It's useful when you need to pass a `key` prop to the fragment, which is common when rendering a list of fragments.

**Example:**

```jsx
function Columns() {
  return (
    <React.Fragment>
      <td>Hello</td>
      <td>World</td>
    </React.Fragment>
  );
}

// In a table
<table>
  <tr>
    <Columns />
  </tr>
</table>
```

**2. The Short Syntax: `<>` and `</>`**

This is a more concise and common way to use fragments. It looks like empty XML tags.

**Example:**

```jsx
function App() {
  return (
    <>
      <h1>Title</h1>
      <p>Some text.</p>
    </>
  );
}
```

**Important Note**: The short syntax (`<>`) does not support the `key` attribute. If you need to provide a key for a fragment in a list, you must use the `<React.Fragment key={...}>` syntax.

**Example with Keys:**

```jsx
function Glossary(props) {
  return (
    <dl>
      {props.items.map(item => (
        // Without the `key` prop, React will give a warning.
        // The short syntax <> does not support keys.
        <React.Fragment key={item.id}>
          <dt>{item.term}</dt>
          <dd>{item.description}</dd>
        </React.Fragment>
      ))}
    </dl>
  );
}
```

By using Fragments, you can write cleaner components and produce a more minimal and valid DOM structure.

---

### Q33: What is Strict Mode in React?

**Answer:**

`React.StrictMode` is a tool for highlighting potential problems in an application. Like `Fragment`, `StrictMode` does not render any visible UI. It activates additional checks and warnings for its descendants.

#### Key Characteristics

-   **Development Only**: Strict Mode checks only run in development mode; they do **not** impact the production build.
-   **No Visible UI**: It does not render any actual UI elements in the DOM.
-   **Proactive Problem Finding**: It helps developers find common mistakes and deprecated features before they become bugs in production.

#### How to Use Strict Mode

You can enable Strict Mode for any part of your application by wrapping a component or a group of components with `<React.StrictMode>`.

**Example:**

```jsx
import React from 'react';

function App() {
  return (
    <div>
      <Header />
      <React.StrictMode>
        <div>
          <ComponentOne />
          <ComponentTwo />
        </div>
      </React.StrictMode>
      <Footer />
    </div>
  );
}
```

In this example, the `Header` and `Footer` components will not be checked by Strict Mode, but `ComponentOne` and `ComponentTwo`, along with all of their descendants, will be.

It's common to wrap the entire application in `StrictMode` in the root `index.js` file:

```jsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

#### What Does Strict Mode Do?

`StrictMode` helps with:

1.  **Identifying components with unsafe lifecycles**: It provides warnings about legacy lifecycle methods like `componentWillMount` that are considered unsafe for asynchronous rendering.

2.  **Warning about legacy string ref API usage**: It warns if you are using the older string ref API, which is being deprecated in favor of callback refs and `React.createRef()`.

3.  **Warning about deprecated `findDOMNode` usage**: It warns against the use of `findDOMNode`, which is being phased out.

4.  **Detecting unexpected side effects**: This is one of its most powerful features. Strict Mode intentionally double-invokes certain functions (like component constructors, `render` methods, and state updates) to help you find side effects that were not cleaned up properly. If your component has side effects in these methods, the double invocation can help expose them.

5.  **Detecting legacy context API**: It warns about the use of the old context API, which has been replaced by the new, more efficient Context API.

By catching these issues early, `StrictMode` encourages developers to write more robust and maintainable React code that is better prepared for future updates to the library.

---

### Q34: What are the main differences between JSX and HTML?

**Answer:**

JSX (JavaScript XML) is a syntax extension for JavaScript that allows you to write HTML-like code inside your JavaScript files. While it looks very similar to HTML, there are several key differences that are important to understand when working with React.

#### 1. Attribute Naming Convention

-   **HTML**: Uses kebab-case for attributes (e.g., `class`, `onclick`).
-   **JSX**: Uses camelCase for most attributes because they are converted into properties of JavaScript objects. For example, `onclick` becomes `onClick`, and `tabindex` becomes `tabIndex`.

-   **`class` vs. `className`**: Since `class` is a reserved keyword in JavaScript, JSX uses `className` to specify CSS classes.
-   **`for` vs. `htmlFor`**: Similarly, `for` is a reserved keyword, so JSX uses `htmlFor` for the `for` attribute on `<label>` elements.

#### 2. Inline Styles

-   **HTML**: Inline styles are written as a string.
    ```html
    <div style="color: blue; font-size: 16px;"></div>
    ```
-   **JSX**: Inline styles are specified as a JavaScript object. The keys are camelCased versions of CSS property names, and the values are typically strings.
    ```jsx
    <div style={{ color: 'blue', fontSize: '16px' }}></div>
    ```

#### 3. JavaScript Expressions

-   **HTML**: Is static and cannot directly embed dynamic logic.
-   **JSX**: You can embed any JavaScript expression inside JSX by wrapping it in curly braces `{}`. This allows you to render dynamic content, perform calculations, or call functions directly within your markup.
    ```jsx
    <h1>{user.name}'s Profile</h1>
    <p>2 + 2 = {2 + 2}</p>
    ```

#### 4. Self-Closing Tags

-   **HTML**: Some tags can be self-closing (e.g., `<img>`, `<br>`), while others are not.
-   **JSX**: Any tag can be self-closing. If a tag has no children, you **must** close it with a trailing slash, like in XML. For example, `<div />` is valid JSX.

#### 5. Comments

-   **HTML**: Uses `<!-- comment -->`.
-   **JSX**: Uses JavaScript comments wrapped in curly braces.
    ```jsx
    {/* This is a comment in JSX */}
    ```

#### Summary Table

| Feature             | HTML                                | JSX                                                     |
| ------------------- | ----------------------------------- | ------------------------------------------------------- |
| **Attribute Naming**| `kebab-case` (e.g., `onclick`)      | `camelCase` (e.g., `onClick`)                           |
| **Class Attribute** | `class="my-class"`                  | `className="my-class"`                                  |
| **Inline Styles**   | A string: `style="color: red;"`     | An object: `style={{ color: 'red' }}`                   |
| **Expressions**     | Static, no dynamic expressions      | Embed JS with `{}`: `<h1>{title}</h1>`                  |
| **Self-Closing**    | Only for certain tags (e.g., `<img>`) | Any tag can be self-closing: `<div />`                  |
| **Comments**        | `<!-- comment -->`                  | `{/* comment */}`                                       |

These differences are due to the fact that JSX is ultimately compiled into regular JavaScript by a transpiler like Babel, which creates React elements (JavaScript objects) from the JSX syntax.

---

### Q35: What are refs in React and what are they used for?

**Answer:**

Refs (short for "references") provide a way to access DOM nodes or React elements created in the `render` method. They are used for cases where you need to imperatively modify a child outside of the typical dataflow.

#### When to Use Refs

Refs are an escape hatch from the declarative, props-based nature of React. They should be used sparingly, but they are necessary for certain tasks:

1.  **Managing focus, text selection, or media playback**: For example, programmatically focusing an input field when a component mounts.
2.  **Triggering imperative animations**: Directly manipulating an element's style to trigger an animation.
3.  **Integrating with third-party DOM libraries**: If you are using a library that needs direct access to a DOM node (like a jQuery plugin), you can use a ref to provide it.

Avoid using refs for anything that can be done declaratively. For example, instead of using a ref to show or hide a component, use conditional rendering.

#### Creating and Using Refs

There are two main ways to create refs:

**1. `React.createRef()` (for class components)**

In class components, you can create a ref in the constructor and attach it to a React element via the `ref` attribute.

**Example:**

```jsx
import React, { Component } from 'react';

class MyComponent extends Component {
  constructor(props) {
    super(props);
    this.myInput = React.createRef();
  }

  componentDidMount() {
    // Access the DOM node via the .current property
    this.myInput.current.focus();
  }

  render() {
    return <input type="text" ref={this.myInput} />;
  }
}
```

**2. `useRef()` Hook (for functional components)**

The `useRef` hook is the modern way to create refs in functional components. It returns a mutable ref object whose `.current` property is initialized to the passed argument (`initialValue`). The returned object will persist for the full lifetime of the component.

**Example:**

```jsx
import React, { useRef, useEffect } from 'react';

function MyFunctionalComponent() {
  const inputEl = useRef(null);

  useEffect(() => {
    // The .current property holds the DOM node
    inputEl.current.focus();
  }, []);

  return <input ref={inputEl} type="text" />;
}
```

#### Refs for Storing Mutable Values

A less common but powerful use of `useRef` is to hold a mutable value that does not cause a re-render when it changes. This is like having an instance variable in a class component.

**Example:**

```jsx
import React, { useRef, useEffect } from 'react';

function Timer() {
  const intervalRef = useRef();

  useEffect(() => {
    const id = setInterval(() => {
      console.log('Timer tick');
    }, 1000);

    intervalRef.current = id;

    return () => {
      clearInterval(intervalRef.current);
    };
  }, []);

  return <div>Timer is running...</div>;
}
```

In this case, `intervalRef` stores the interval ID. Updating `intervalRef.current` does not trigger a re-render, which is exactly what we want. It allows us to persist the ID across renders and access it in the cleanup function.

---

### Q36: What is `forwardRef` in React?

**Answer:**

`React.forwardRef` is a function that lets a component expose a DOM ref from one of its children to its parent. It provides a way to pass a ref through a component to one of its children, which is something you can't do with the standard `ref` attribute.

#### The Problem `forwardRef` Solves

By default, you cannot pass a `ref` prop to a functional component. If you try to do so, React will give you a warning because `ref` is not a normal prop and is handled differently by React, just like the `key` prop.

This becomes a problem when you have a reusable component (e.g., a custom `FancyButton`) and the parent component needs a ref to the underlying DOM element (e.g., the `<button>`) for reasons like managing focus.

#### How to Use `forwardRef`

`React.forwardRef` creates a React component that forwards the `ref` attribute it receives to another component below in the tree.

-   **Syntax**: `const MyComponent = React.forwardRef((props, ref) => { ... });`

    -   The component function receives `props` as the first argument and `ref` as the second argument.
    -   You can then forward this `ref` down to a specific DOM element or class component.

**Example:**

Let's create a `FancyButton` component that forwards its ref to the underlying DOM `<button>` element.

```jsx
import React, { forwardRef } from 'react';

// 1. Create a component with React.forwardRef
const FancyButton = forwardRef((props, ref) => (
  <button ref={ref} className="FancyButton">
    {props.children}
  </button>
));

export default FancyButton;
```

Now, a parent component can get a ref to the `<button>` DOM node.

```jsx
import React, { useRef, useEffect } from 'react';
import FancyButton from './FancyButton';

function App() {
  // 2. Create a ref in the parent component
  const buttonRef = useRef(null);

  useEffect(() => {
    // 4. The ref now points to the <button> DOM element
    if (buttonRef.current) {
      buttonRef.current.focus();
    }
  }, []);

  return (
    <div>
      {/* 3. Pass the ref to the child component */}
      <FancyButton ref={buttonRef}>Click me</FancyButton>
    </div>
  );
}
```

In this example:

1.  We wrap our `FancyButton` component in `React.forwardRef`.
2.  The `ref` passed by the `App` component is received as the second argument in our `FancyButton`'s render function.
3.  We forward this `ref` to the `<button>` element by passing it as its `ref` attribute.
4.  This allows the `App` component's `buttonRef` to get direct access to the `<button>` DOM node, and we can call `.focus()` on it.

#### Use with Higher-Order Components (HOCs)

`forwardRef` is also particularly useful when working with Higher-Order Components (HOCs). If an HOC wraps a component, it can hide the original component's refs. `forwardRef` can be used in the HOC to pass the ref through to the wrapped component, preserving the ability to get a ref to it.

---

### Q37: What is the difference between the Shadow DOM and the Virtual DOM?

**Answer:**

Shadow DOM and Virtual DOM are two different concepts that help solve different problems in web development. Although they both involve the "DOM," they are not related and serve distinct purposes.

#### Virtual DOM (V-DOM)

The Virtual DOM is a programming concept where a virtual representation of a UI is kept in memory and synced with the "real" DOM. It's a core part of libraries like React and Vue.

-   **Purpose**: To improve performance by minimizing direct manipulation of the real DOM. DOM operations are slow and expensive. The V-DOM provides a way to batch updates efficiently.
-   **How it Works**:
    1.  When the state of a component changes, a new Virtual DOM tree is created.
    2.  This new V-DOM tree is compared (or "diffed") with the previous V-DOM tree.
    3.  React calculates the most efficient way to apply these changes to the real DOM.
    4.  Only the necessary changes are batched and applied to the real DOM, reducing the number of costly DOM operations.
-   **Key Feature**: It's a performance optimization technique. It's a JavaScript object that models the DOM, not a browser feature.

#### Shadow DOM

The Shadow DOM is a browser technology designed for encapsulation. It allows you to attach a hidden, separated DOM tree to an element—the "shadow host." This shadow tree is rendered separately from the main document's DOM.

-   **Purpose**: To encapsulate the structure, style, and behavior of a component, keeping it isolated from the rest of the document. This is a cornerstone of Web Components.
-   **How it Works**:
    1.  You attach a shadow root to a host element using `element.attachShadow({ mode: 'open' })`.
    2.  You can then append elements to this shadow root.
    3.  The styles defined inside the shadow root are scoped to it and don't leak out. External styles don't affect the elements inside it (unless explicitly designed to).
-   **Key Feature**: It's an encapsulation and scoping mechanism. It's a native browser feature.

#### Summary Table

| Feature             | Virtual DOM                                                              | Shadow DOM                                                               |
| ------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| **Primary Goal**    | Performance Optimization                                                 | Encapsulation and Scoping                                                |
| **Nature**          | A concept/pattern implemented by JavaScript libraries (e.g., React)      | A native browser technology (part of the Web Components standard)        |
| **How it Works**    | Creates a copy of the DOM in memory, computes diffs, and batches updates. | Creates an isolated DOM tree attached to an element.                     |
| **Main Benefit**    | Reduces expensive DOM manipulations, leading to faster UI updates.       | Prevents styles and scripts from leaking in or out, creating reusable components. |
| **Relation to DOM** | An abstraction on top of the real DOM.                                   | A separate, hidden DOM tree attached to a real DOM element.              |

In short, the **Virtual DOM** is about **when** and **how** to update the DOM for performance, while the **Shadow DOM** is about **where** to render the DOM for encapsulation.

---

### Q38: What are Synthetic Events in React?

**Answer:**

Synthetic Events are React's cross-browser wrapper around the browser's native event system. They provide a consistent and reliable event interface, normalizing browser inconsistencies and ensuring that events work identically across all browsers.

#### Key Characteristics

1.  **Cross-Browser Consistency**: Native browser events can have different property names and behaviors. For example, `event.target` might behave differently in older browsers. React's `SyntheticEvent` normalizes these differences, so you can rely on a consistent API (e.g., `e.target`, `e.preventDefault()`, `e.stopPropagation()`).

2.  **Performance**: React uses a technique called **event delegation**. Instead of attaching an event listener to every single DOM element, React attaches a single event listener at the root of the document for each event type. When an event is fired, it bubbles up to the root, where React's listener catches it and determines which component triggered it.

3.  **Event Pooling**: To improve performance, React pools `SyntheticEvent` objects. This means that after an event handler is executed, the event object's properties are nullified, and the object is released back into a pool. You cannot access the event asynchronously (e.g., in a `setTimeout`) because it will have been reset.

    If you need to access the event properties asynchronously, you must call `e.persist()` on the event.

#### How to Use Them

Using Synthetic Events is straightforward and looks just like handling native DOM events.

```javascript:src/EventComponent.js
import React from 'react';

function EventComponent() {
  const handleClick = (e) => {
    // e is a SyntheticEvent
    console.log('Button clicked!');

    // You can prevent the default browser action
    e.preventDefault();

    // You cannot access the event asynchronously without e.persist()
    setTimeout(() => {
      // This will log null, because the event is pooled
      console.log(e.type); // Logs 'click' if e.persist() was called, otherwise error/null
    }, 500);

    // To use it asynchronously, you must opt-in
    // e.persist();
  };

  return (
    <a href="#" onClick={handleClick}>
      Click Me
    </a>
  );
}

export default EventComponent;
```

#### Accessing the Native Event

If you need to access the underlying native browser event for any reason, you can do so via the `nativeEvent` property on the `SyntheticEvent` object.

```javascript
const handleChange = (e) => {
  console.log(e.nativeEvent); // The original browser event
};
```

In summary, `SyntheticEvent` is an essential abstraction in React that provides a consistent, high-performance event system, freeing developers from worrying about cross-browser quirks.

---

### Q39: What is reconciliation in React?

**Answer:**

Reconciliation is the process through which React updates the browser's DOM. When a component's state or props change, React decides whether an actual DOM update is necessary by comparing the newly returned element with the previously rendered one. If they are not equal, React will update the DOM.

This process is powered by React's **diffing algorithm**, which makes reconciliation highly efficient. Instead of re-rendering the entire application on every change, React uses the **Virtual DOM** to find the minimum number of operations required to update the UI.

#### The Diffing Algorithm

React's diffing algorithm is built on a set of heuristics that allow it to compare two Virtual DOM trees in O(n) time complexity.

1.  **Different Element Types**: If the root elements of the two trees have different types (e.g., `<div>` changes to `<span>`), React will tear down the old tree and build the new tree from scratch. This includes destroying all old components and their state.

    ```javascript
    // Before update
    <div>
      <Counter />
    </div>

    // After update
    <span>
      <Counter />
    </span>
    ```

    In this case, the original `<Counter />` component will be unmounted, and a new one will be mounted.

2.  **Same Element Types**: If the root elements have the same type, React will look at the attributes of both, keep the same underlying DOM node, and only update the changed attributes.

    ```javascript
    // Before update
    <div className="before" title="stuff" />

    // After update
    <div className="after" title="stuff" />
    ```

    React will only modify the `className` on the underlying DOM node.

3.  **Lists of Elements (Keys)**: When rendering a list of elements, React needs a way to identify which items have changed, been added, or been removed. This is where the `key` prop is crucial.

    -   **Without Keys**: If you don't provide keys, React will compare items by their index. If an item is added to the beginning of the list, React will think every item has changed, leading to inefficient re-renders and potential state management bugs.

    -   **With Keys**: Keys should be stable, predictable, and unique strings that identify an item among its siblings. With keys, React can correctly identify which items were moved, added, or removed, and only perform the necessary mutations.

    ```javascript:src/TodoList.js
    import React from 'react';

    function TodoList({ todos }) {
      return (
        <ul>
          {todos.map(todo => (
            // The key helps React identify each item
            <li key={todo.id}>
              {todo.text}
            </li>
          ))}
        </ul>
      );
    }
    ```

In summary, reconciliation is the mechanism that makes React fast. By using a Virtual DOM and an efficient diffing algorithm, React minimizes direct manipulation of the real DOM, resulting in a smoother and more performant user experience.

---

### Q40: What is prop drilling and how can you avoid it?

**Answer:**

**Prop drilling** is the process of passing data from a parent component down to a deeply nested child component through intermediate components that don't need the data themselves. This can make the codebase harder to maintain and refactor.

#### The Problem

Imagine a component tree where a top-level component holds some state, but a child component several levels down needs that state.

```
<App>
  <HomePage user={user}>
    <UserProfile user={user}>
      <Avatar user={user} />
    </UserProfile>
  </HomePage>
</App>
```

In this example, `HomePage` and `UserProfile` don't use the `user` prop. They just pass it along so that `<Avatar />` can use it. This is prop drilling.

**Why is it a problem?**

-   **Maintenance Hell**: If the shape of the `user` object changes, you might have to update the prop types or interfaces in every intermediate component.
-   **Reduced Reusability**: The intermediate components (`HomePage`, `UserProfile`) are now less reusable because they are coupled to the `user` prop.
-   **Code Clutter**: It adds unnecessary code to components that don't care about the data.

#### How to Avoid It

There are several strategies to avoid prop drilling.

1.  **React Context API**: The Context API is React's built-in solution for sharing state across the entire component tree without having to pass props down manually at every level.

    -   **How it works**: You create a `Context` object. Then, you use a `Provider` to make the data available to all components inside it. Any component that needs the data can subscribe to it using a `Consumer` or the `useContext` hook.

    ```javascript:src/UserContext.js
    import React, { createContext, useContext } from 'react';

    const UserContext = createContext(null);

    export function App() {
      const user = { name: 'John Doe' };
      return (
        <UserContext.Provider value={user}>
          <HomePage />
        </UserContext.Provider>
      );
    }

    export function Avatar() {
      const user = useContext(UserContext);
      return <div>{user.name}</div>;
    }
    ```

2.  **State Management Libraries (Redux, Zustand, etc.)**: For large-scale applications, a dedicated state management library can provide a centralized store for your application's state. Components can then connect to this store to access the data they need directly.

    -   **How it works**: State is held in a global "store." Components can dispatch "actions" to update the state and subscribe to changes to re-render when the state they care about is updated.

3.  **Component Composition**: Sometimes, you can solve prop drilling by restructuring your components. Instead of passing data down, you can pass the component that needs the data as a prop.

    ```javascript
    // Instead of this:
    <HomePage user={user} />

    // You can do this:
    <HomePage avatar={<Avatar user={user} />} />

    // HomePage then renders the avatar prop directly:
    function HomePage({ avatar }) {
      return <div>{avatar}</div>;
    }
    ```

By using these techniques, you can write cleaner, more maintainable, and more reusable React components.

---

### Q41: What are the differences between class and functional components?

**Answer:**

Class and functional components are two ways to define components in React. While they can achieve the same results, they have fundamental differences in syntax, state management, and lifecycle features. Since the introduction of Hooks, functional components have become the modern standard for writing React applications.

#### Class Components

Class components are ES6 classes that extend `React.Component`. They have a `render` method that returns JSX and can manage state and side effects using lifecycle methods.

-   **Syntax**: Uses ES6 class syntax.
-   **State**: Managed with `this.state` and updated with `this.setState()`.
-   **Lifecycle**: Uses lifecycle methods like `componentDidMount`, `componentDidUpdate`, and `componentWillUnmount`.
-   **`this` Keyword**: The meaning of `this` can be tricky and often requires binding in the constructor.

```javascript:src/ClassCounter.js
import React from 'react';

class ClassCounter extends React.Component {
  constructor(props) {
    super(props);
    this.state = { count: 0 };
  }

  componentDidMount() {
    document.title = `You clicked ${this.state.count} times`;
  }

  componentDidUpdate() {
    document.title = `You clicked ${this.state.count} times`;
  }

  render() {
    return (
      <div>
        <p>You clicked {this.state.count} times</p>
        <button onClick={() => this.setState({ count: this.state.count + 1 })}>
          Click me
        </button>
      </div>
    );
  }
}
```

#### Functional Components

Functional components are JavaScript functions that accept props and return JSX. Originally, they were stateless, but with the introduction of Hooks, they can now manage state, handle side effects, and more.

-   **Syntax**: Simple JavaScript functions.
-   **State**: Managed with the `useState` Hook.
-   **Lifecycle**: Side effects are handled with the `useEffect` Hook, which can replicate the behavior of `componentDidMount`, `componentDidUpdate`, and `componentWillUnmount`.
-   **`this` Keyword**: No `this` keyword to worry about.

```javascript:src/FunctionalCounter.js
import React, { useState, useEffect } from 'react';

function FunctionalCounter() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    document.title = `You clicked ${count} times`;
  });

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>
        Click me
      </button>
    </div>
  );
}
```

#### Summary Table

| Feature         | Class Components                                       | Functional Components (with Hooks)                     |
| --------------- | ------------------------------------------------------ | ------------------------------------------------------ |
| **Syntax**      | ES6 Class extending `React.Component`                  | JavaScript function                                    |
| **State**       | `this.state`, updated with `this.setState()`           | `useState` Hook                                        |
| **Side Effects**| Lifecycle methods (`componentDidMount`, etc.)          | `useEffect` Hook                                       |
| **Props**       | Accessed via `this.props`                              | Passed as function arguments                           |
| **`this`**      | Required, context can be confusing                     | Not used                                               |
| **Code Size**   | Generally more verbose                                 | More concise and easier to read                        |
| **Modern React**| Legacy approach, though still fully supported          | The recommended and modern approach                    |

Functional components with Hooks are now preferred because they lead to more readable, reusable, and less boilerplate-heavy code.

---

### Q42: What is the `children` prop in React?

**Answer:**

`props.children` is a special prop, automatically passed to every component, that can be used to render whatever you include between the opening and closing tags when invoking a component. It allows for component composition and creating flexible, reusable container components.

#### What can `props.children` be?

The `children` prop can be anything: a single element, an array of elements, a string, a number, or even a function.

-   **A String**:

    ```jsx
    <MyComponent>Hello world!</MyComponent>
    ```

-   **JSX Elements**:

    ```jsx
    <Card>
      <h1>About Me</h1>
      <p>I am a React developer.</p>
    </Card>
    ```

-   **A Mix of Both**:

    ```jsx
    <p>Here is a list: <ul>...</ul></p>
    ```

#### How to Use It

You can access the children in your component via `props.children`.

Here is an example of a generic `Card` component that can wrap any content:

```javascript:src/Card.js
import React from 'react';

// The Card component doesn't need to know what it will render.
// It just provides a container with some styles.
function Card({ children }) {
  const cardStyle = {
    border: '1px solid #ccc',
    borderRadius: '8px',
    padding: '16px',
    margin: '16px',
    boxShadow: '0 2px 4px rgba(0,0,0,0.1)',
  };

  return (
    <div style={cardStyle}>
      {children}  // Render whatever is passed inside
    </div>
  );
}

export default Card;
```

Now you can use the `Card` component to wrap different content:

```javascript:src/App.js
import React from 'react';
import Card from './Card';

function App() {
  return (
    <div>
      <Card>
        <h2>Welcome!</h2>
        <p>This is some content inside a card.</p>
      </Card>

      <Card>
        <article>
          <h3>Another Card</h3>
          <button>Click Me</button>
        </article>
      </Card>
    </div>
  );
}
```

#### `React.Children` Utility

React provides a utility API, `React.Children`, for working with `props.children`. This is useful because `props.children` can be an opaque data structure. You shouldn't just assume it's an array.

`React.Children` provides methods like:

-   `React.Children.map(children, fn)`: Invokes a function on every immediate child contained within `children`.
-   `React.Children.forEach(children, fn)`: Like `map` but doesn't return an array.
-   `React.Children.count(children)`: Returns the total number of components in `children`.
-   `React.Children.only(children)`: Verifies that `children` has only one child and returns it. Otherwise, it throws an error.
-   `React.Children.toArray(children)`: Returns the `children` data structure as a flat array.

Using `React.Children.map` is safer than `props.children.map` because it handles cases where `children` is a single element or null/undefined.

In summary, `props.children` is a fundamental concept in React for creating composable and reusable UIs.

---

### Q43: What is the difference between `React.Component` and `React.PureComponent`?

**Answer:**

`React.PureComponent` is a base class that is very similar to `React.Component`. The key difference lies in how they handle re-rendering. `PureComponent` provides a performance optimization out of the box by preventing unnecessary re-renders.

#### `React.Component`

A component that extends `React.Component` will re-render whenever its parent re-renders, or whenever `this.setState()` is called, regardless of whether its props or state have actually changed.

#### `React.PureComponent`

A `PureComponent` implements a `shouldComponentUpdate()` lifecycle method with a **shallow comparison** of its current and next props and state.

-   **Shallow Comparison**: It checks for equality on the top-level properties. If the new props and state are shallowly equal to the previous ones, the component will **not** re-render.
-   **Performance**: This can provide a significant performance boost by skipping the render (and subsequent diffing) of an entire component subtree.

#### How it Works

Let's look at an example.

```javascript:src/Title.js
import React from 'react';

// This component will re-render every time its parent re-renders
class Title extends React.Component {
  render() {
    console.log('Title component rendered');
    return <h1>{this.props.text}</h1>;
  }
}

// This component will only re-render if its props change
class PureTitle extends React.PureComponent {
  render() {
    console.log('PureTitle component rendered');
    return <h1>{this.props.text}</h1>;
  }
}
```

If a parent component managing both of these re-renders without changing the `text` prop, you would see "Title component rendered" in the console every time, but "PureTitle component rendered" only on the first render.

#### When to Use `PureComponent`

`PureComponent` is ideal when:

1.  Your component's props and state are simple primitive values (strings, numbers, booleans).
2.  Your props and state are complex objects or arrays, but you ensure you are passing **new objects or arrays** when they change, rather than mutating them.

#### Potential Pitfalls

The shallow comparison can cause problems if you mutate data structures. For example, if a prop is an array and you just push a new item to it, the reference to the array remains the same, so `PureComponent` won't detect the change and won't re-render.

```javascript
// Bad: Mutating the array
const list = this.state.list;
list.push('new-item');
this.setState({ list: list }); // PureComponent will not re-render

// Good: Creating a new array
this.setState(prevState => ({
  list: [...prevState.list, 'new-item'],
})); // PureComponent will re-render
```

For functional components, `React.memo()` provides the same functionality as `PureComponent`.

In summary, use `PureComponent` (or `React.memo`) for a free performance win, but be mindful that it relies on a shallow comparison and requires you to work with immutable data structures for props and state.

---

### Q44: What is the difference between stateful and stateless components?

**Answer:**

In React, components are often categorized as either "stateful" or "stateless" based on whether they manage their own internal state.

#### Stateless Components

Stateless components (also known as "dumb" or "presentational" components) do not have their own internal state. They receive data via props and render UI based on that data. They are typically simple functions.

-   **Purpose**: To display information. They are concerned with *how things look*.
-   **Characteristics**:
    -   They don't manage state.
    -   They receive data only through props.
    -   They are highly reusable and predictable. Given the same props, they will always render the same output.
    -   They are easy to test.

**Example:**

```javascript:src/Greeting.js
import React from 'react';

// This component just displays the name it receives.
function Greeting({ name }) {
  return <h1>Hello, {name}!</h1>;
}

export default Greeting;
```

#### Stateful Components

Stateful components (also known as "smart" or "container" components) are components that hold and manage their own internal state. They are responsible for application logic and passing data down to stateless components.

-   **Purpose**: To manage data and application logic. They are concerned with *how things work*.
-   **Characteristics**:
    -   They manage their own state using `this.state` (in class components) or the `useState` hook (in functional components).
    -   They often contain side effects (e.g., data fetching).
    -   They act as a source of data for other components.

**Example:**

```javascript:src/NameInput.js
import React, { useState } from 'react';
import Greeting from './Greeting';

// This component manages the 'name' state.
function NameInput() {
  const [name, setName] = useState('World');

  const handleChange = (e) => {
    setName(e.target.value);
  };

  return (
    <div>
      <input type="text" value={name} onChange={handleChange} />
      <Greeting name={name} />
    </div>
  );
}

export default NameInput;
```

#### Summary Table

| Feature          | Stateless Components                               | Stateful Components                                |
| ---------------- | -------------------------------------------------- | -------------------------------------------------- |
| **State**        | Do not have internal state.                        | Manage their own internal state.                   |
| **Primary Role** | Presentation (UI).                                 | Logic and Data Management.                         |
| **Data Source**  | Receives data via props.                           | Can have its own state as a data source.           |
| **Implementation**| Usually functional components.                     | Can be class components or functional components with Hooks. |
| **Reusability**  | Highly reusable.                                   | Less reusable, often specific to an application's logic. |

This separation of concerns—having stateful components manage the logic and stateless components handle the UI—is a common pattern in React that leads to a more organized and maintainable codebase.

---

### Q45: How do you make an AJAX request in React?

**Answer:**

AJAX requests in React are typically made inside the `useEffect` hook to fetch data from an external API. This ensures that the data fetching logic runs as a side effect, separate from the rendering process. You can use the browser's built-in **Fetch API** or a third-party library like **Axios**.

#### Using the Fetch API

The Fetch API is a modern, promise-based interface for making network requests. It's available in all modern browsers.

**Steps:**

1.  Use the `useEffect` hook to run the fetch call when the component mounts.
2.  Use the `useState` hook to store the fetched data, loading status, and any potential errors.
3.  Make the request using `fetch()`.
4.  Handle the response by converting it to JSON and updating the state.
5.  Include a cleanup function in `useEffect` if you need to cancel the request on unmount.

**Example:**

```javascript:src/DataFetcher.js
import React, { useState, useEffect } from 'react';

function DataFetcher() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('https://api.example.com/data');
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const result = await response.json();
        setData(result);
      } catch (e) {
        setError(e.message);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []); // The empty dependency array ensures this effect runs only once

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      <h1>Fetched Data</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}

export default DataFetcher;
```

#### Using Axios

Axios is a popular third-party library that provides a more convenient API for making HTTP requests. It offers features like automatic JSON transformation and better error handling.

First, you need to install it:
`npm install axios`

**Example with Axios:**

The code structure is very similar to the Fetch example.

```javascript:src/AxiosDataFetcher.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function AxiosDataFetcher() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('https://api.example.com/data');
        setData(response.data);
      } catch (e) {
        setError(e.message);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      <h1>Fetched Data with Axios</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}
```

Both methods are excellent choices. **Fetch** is great for simple requests with no external dependencies, while **Axios** provides a more powerful and flexible API for complex applications.

---

### Q46: What are the Rules of Hooks?

**Answer:**

React Hooks have two fundamental rules that you must follow to ensure they work correctly and predictably. These rules are enforced by the `eslint-plugin-react-hooks` ESLint plugin.

#### 1. Only Call Hooks at the Top Level

**Don't call Hooks inside loops, conditions, or nested functions.** Instead, always use Hooks at the top level of your React function, before any early returns.

**Why?**

React relies on the **call order** of Hooks to associate state with the correct component. On every render, the call order of Hooks must be identical. If you put a Hook inside a condition, the call order could change between renders, leading to bugs.

**Incorrect ❌**

```javascript
function MyComponent({ hasName }) {
  if (hasName) {
    // Don't do this! The call order changes based on the prop.
    const [name, setName] = useState('John');
  }

  const [age, setAge] = useState(30);
  // ...
}
```

If `hasName` is false on the first render and true on the second, the Hook call order will be different, and React will be confused.

**Correct ✅**

```javascript
function MyComponent({ hasName }) {
  // Call Hooks at the top level, in the same order every time.
  const [name, setName] = useState(hasName ? 'John' : '');
  const [age, setAge] = useState(30);

  // You can have conditional logic *inside* your Hook if needed.
  useEffect(() => {
    if (hasName) {
      // ...
    }
  });

  // ...
}
```

#### 2. Only Call Hooks from React Functions

**Don't call Hooks from regular JavaScript functions.** You should only call Hooks from:

1.  **React functional components.**
2.  **Custom Hooks.**

**Why?**

Hooks are designed to be used in the context of a React component. They need access to the component's state and lifecycle features. Calling them from a regular JavaScript function doesn't make sense because there is no component context for them to hook into.

**Incorrect ❌**

```javascript
function getFormState() {
  // This is not a React component or a custom Hook.
  const [name, setName] = useState(''); // This will not work.
  return { name, setName };
}
```

**Correct ✅**

You can, however, create **custom Hooks**, which are reusable functions that contain other Hooks. By convention, custom Hooks must start with the word `use`.

```javascript
// This is a custom Hook because its name starts with 'use'.
function useFormInput(initialValue) {
  const [value, setValue] = useState(initialValue);

  function handleChange(e) {
    setValue(e.target.value);
  }

  return {
    value,
    onChange: handleChange,
  };
}

// Now you can use your custom Hook in a component.
function MyForm() {
  const name = useFormInput('John');
  return <input {...name} />;
}
```

Following these two rules ensures that all stateful logic in a component is clearly visible from its source code and that the component will behave correctly on every render.

---

### Q47: What is the `useReducer` hook and when should you use it?

**Answer:**

`useReducer` is a hook that is used for state management in React. It is an alternative to `useState` and is generally preferred when you have complex state logic that involves multiple sub-values or when the next state depends on the previous one.

It accepts a **reducer function** and an **initial state**, and it returns the current state and a **dispatch** function.

`const [state, dispatch] = useReducer(reducer, initialState);`

-   **`state`**: The current state value.
-   **`dispatch`**: A function that you call to update the state. It sends an "action" object to the reducer.
-   **`reducer`**: A pure function that takes the current state and an action object and returns the new state.
-   **`initialState`**: The initial state value.

#### When to use `useReducer` over `useState`

1.  **Complex State Logic**: When your state is an object or array with multiple properties that often change together, `useReducer` can make the state transitions more predictable and maintainable.

2.  **When Next State Depends on Previous State**: The reducer function receives the current state, making it easy to compute the next state based on the previous one.

3.  **Optimizing Performance**: When dealing with deep updates, `useReducer` allows you to pass down a `dispatch` function instead of callbacks to child components. This can prevent unnecessary re-renders of child components that don't need the state itself, only the ability to update it.

#### Example: A Complex Counter

Here is a counter that can be incremented, decremented, reset, and have a value added to it.

```javascript:src/Counter.js
import React, { useReducer } from 'react';

// 1. Define the initial state
const initialState = { count: 0 };

// 2. Create the reducer function
function reducer(state, action) {
  switch (action.type) {
    case 'increment':
      return { count: state.count + 1 };
    case 'decrement':
      return { count: state.count - 1 };
    case 'add':
      return { count: state.count + action.payload };
    case 'reset':
      return initialState;
    default:
      throw new Error();
  }
}

function Counter() {
  // 3. Use the useReducer hook
  const [state, dispatch] = useReducer(reducer, initialState);

  return (
    <div>
      <h2>Count: {state.count}</h2>
      {/* 4. Dispatch actions on user events */}
      <button onClick={() => dispatch({ type: 'increment' })}>+</button>
      <button onClick={() => dispatch({ type: 'decrement' })}>-</button>
      <button onClick={() => dispatch({ type: 'add', payload: 10 })}>+10</button>
      <button onClick={() => dispatch({ type: 'reset' })}>Reset</button>
    </div>
  );
}

export default Counter;
```

In this example, all the state transition logic is consolidated in the `reducer` function, making the `Counter` component cleaner and the state updates more explicit and predictable.

---

### Q48: What is the `useImperativeHandle` hook?

**Answer:**

`useImperativeHandle` is a React Hook that customizes the instance value that is exposed to parent components when using `ref`. In other words, it allows a child component to expose a specific, limited set of functions to a parent component, rather than exposing the entire component instance.

This hook should be used in combination with `forwardRef`.

`useImperativeHandle(ref, createHandle, [deps])`

-   **`ref`**: The ref passed down from the parent.
-   **`createHandle`**: A function that returns an object containing the properties you want to expose. This object will become the value of `ref.current` in the parent component.
-   **`[deps]`**: An optional dependency array. The handle will be re-created only if the dependencies change.

#### Why Use It?

Normally, you want to avoid using refs for imperative actions, but sometimes they are necessary (e.g., to trigger focus or an animation). `useImperativeHandle` is useful for:

1.  **Encapsulation**: It hides the implementation details of the child component and exposes a minimal, clean API to the parent.
2.  **Control**: It prevents the parent component from having to reach into the child's DOM nodes or call methods on its instance directly.

#### Example: A Custom Input with a Focus Method

Imagine you have a custom input component, and you want the parent to be able to call `focus()` on it.

```javascript:src/FancyInput.js
import React, { useRef, useImperativeHandle, forwardRef } from 'react';

// 1. Wrap the component with forwardRef to receive the ref
const FancyInput = forwardRef((props, ref) => {
  const inputRef = useRef();

  // 2. Use useImperativeHandle to expose a custom handle
  useImperativeHandle(ref, () => ({
    // Expose a 'focus' method
    focus: () => {
      console.log('Focusing input!');
      inputRef.current.focus();
    },
    // You could expose other methods here too
    clear: () => {
      inputRef.current.value = '';
    }
  }));

  return <input ref={inputRef} type="text" />;
});

export default FancyInput;
```

Now, the parent component can use this `FancyInput` and call the exposed `focus` method.

```javascript:src/App.js
import React, { useRef } from 'react';
import FancyInput from './FancyInput';

function App() {
  const fancyInputRef = useRef();

  const handleFocusClick = () => {
    // 3. Call the exposed method via the ref's current value
    fancyInputRef.current.focus();
  };

  const handleClearClick = () => {
    fancyInputRef.current.clear();
  };

  return (
    <div>
      <FancyInput ref={fancyInputRef} />
      <button onClick={handleFocusClick}>Focus Input</button>
      <button onClick={handleClearClick}>Clear Input</button>
    </div>
  );
}

export default App;
```

In this setup, the parent component doesn't have direct access to the `<input>` DOM node inside `FancyInput`. It can only interact with the methods explicitly exposed by `useImperativeHandle`, which makes the component's public API clear and controlled.

---

### Q49: What is `useLayoutEffect` and how is it different from `useEffect`?

**Answer:**

`useLayoutEffect` is a version of `useEffect` that fires **synchronously** after all DOM mutations, but **before** the browser has a chance to paint the changes. This is in contrast to `useEffect`, which runs **asynchronously** after the render is committed to the screen.

#### Key Differences

| Feature           | `useEffect`                                                                 | `useLayoutEffect`                                                              | 
| ----------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | 
| **Timing**        | Asynchronous. Fires *after* the browser has painted the DOM updates.        | Synchronous. Fires *before* the browser has painted the DOM updates.           | 
| **Blocking**      | Does not block the browser paint. The user sees the UI update first.        | Blocks the browser paint. The user has to wait for it to complete.             | 
| **Common Use Case** | Data fetching, setting subscriptions, manually changing the DOM (non-layout). | Reading DOM layout (e.g., getting an element's size or position) and synchronously re-rendering. | 

#### When to use `useLayoutEffect`?

You should almost always use `useEffect`. The synchronous nature of `useLayoutEffect` can block visual updates and hurt performance if used improperly.

Use `useLayoutEffect` only when your effect needs to perform DOM measurements and then trigger a synchronous re-render to prevent the user from seeing a visual inconsistency or flicker. For example, if you need to get the height of an element to set the height of another element, using `useEffect` might cause a flicker: the component renders, then the effect runs, then the component re-renders with the correct height. `useLayoutEffect` avoids this by doing it all before the browser paints.

#### Example: Tooltip Positioning

Imagine you want to display a tooltip, but its position depends on the size of the button that triggers it. You need to measure the button's position *after* it has been rendered but *before* the user sees it.

```javascript
import React, { useState, useLayoutEffect, useRef } from 'react';

function TooltipExample() {
  const [show, setShow] = useState(false);
  const [position, setPosition] = useState({ top: 0, left: 0 });
  const buttonRef = useRef();

  // Use useLayoutEffect to measure the button and position the tooltip
  useLayoutEffect(() => {
    if (show && buttonRef.current) {
      const rect = buttonRef.current.getBoundingClientRect();
      setPosition({
        top: rect.bottom + 5, // Position below the button
        left: rect.left
      });
    }
  }, [show]);

  return (
    <div>
      <button ref={buttonRef} onClick={() => setShow(s => !s)}>
        Hover me
      </button>
      {show && (
        <div style={{
          position: 'absolute',
          top: position.top,
          left: position.left,
          border: '1px solid black',
          padding: '5px',
          backgroundColor: 'white'
        }}>
          I'm a tooltip!
        </div>
      )}
    </div>
  );
}

export default TooltipExample;
```

If you were to use `useEffect` here, you might see the tooltip briefly appear at `(0, 0)` before jumping to its correct position, causing a flicker. `useLayoutEffect` ensures the measurement and state update happen synchronously before the paint, so the tooltip appears in the correct place from the start.

---

### Q50: What is the `useCallback` hook and why is it useful?

**Answer:**

`useCallback` is a React Hook that returns a **memoized** version of a callback function. This means that the callback function will only be re-created if one of its dependencies has changed. It's a tool for performance optimization.

`const memoizedCallback = useCallback(callback, [dependencies]);`

-   **`callback`**: The function to memoize.
-   **`[dependencies]`**: An array of dependencies. The callback will be re-created only if a value in this array changes.

#### Why is it useful?

In JavaScript, functions are objects. Every time a component re-renders, any functions defined inside it are re-created. This is usually not a problem.

However, it becomes an issue when you pass these functions as props to child components that are optimized with `React.memo`. Since the function is a new object on every render, the child component will see it as a new prop and re-render, even if its behavior is identical. This defeats the purpose of `React.memo`.

`useCallback` solves this by providing the *same* function instance across re-renders, as long as its dependencies don't change. This allows `React.memo` to correctly skip re-rendering the child component.

**Use `useCallback` when:**

1.  You are passing a callback to a child component that is wrapped in `React.memo`.
2.  The callback is a dependency of another hook, like `useEffect`.

#### Example: Preventing Unnecessary Re-renders

Consider a parent component that renders a list of items and a button to add a new item.

```javascript
import React, { useState, useCallback } from 'react';

// A child component that is expensive to render
const ExpensiveButton = React.memo(({ onClick, children }) => {
  console.log(`Rendering button: ${children}`);
  return <button onClick={onClick}>{children}</button>;
});

function ParentComponent() {
  const [count, setCount] = useState(0);
  const [items, setItems] = useState([]);

  // Without useCallback, this function is re-created on every render
  // const handleAddItem = () => {
  //   setItems([...items, 'New Item']);
  // };

  // With useCallback, this function is only re-created if 'items' changes
  const handleAddItem = useCallback(() => {
    setItems(prevItems => [...prevItems, 'New Item']);
  }, []); // Dependency array is empty if we use the functional update form of setState

  return (
    <div>
      <h2>Count: {count}</h2>
      <button onClick={() => setCount(count + 1)}>Increment Count</button>

      <hr />

      <ExpensiveButton onClick={handleAddItem}>
        Add Item
      </ExpensiveButton>

      <ul>
        {items.map((item, index) => <li key={index}>{item}</li>)}
      </ul>
    </div>
  );
}

export default ParentComponent;
```

**Behavior:**

-   **Without `useCallback`**: Every time you click "Increment Count", the `ParentComponent` re-renders. A new `handleAddItem` function is created, and `ExpensiveButton` re-renders because its `onClick` prop has changed (it's a new function object).
-   **With `useCallback`**: When you click "Increment Count", `ParentComponent` re-renders, but `useCallback` returns the *same* `handleAddItem` function because its dependency array is empty. `React.memo` sees that the `onClick` prop is the same and skips re-rendering `ExpensiveButton`.

This optimization prevents unnecessary renders and can significantly improve performance in complex applications.

---

### Q51: What is the `useMemo` hook and how is it different from `useCallback`?

**Answer:**

`useMemo` is a React Hook that memoizes the **result** of a function call. It re-runs the function and re-computes the value only when one of its dependencies has changed. This is useful for avoiding expensive calculations on every render.

`const memoizedValue = useMemo(() => computeExpensiveValue(a, b), [a, b]);`

-   The first argument is a function that computes and **returns a value**.
-   The second argument is a dependency array. `useMemo` will only re-evaluate the function if a dependency changes.

#### How is it different from `useCallback`?

The key difference lies in what they memoize:

-   **`useCallback` memoizes a function instance.**
    -   `useCallback(fn, deps)` is equivalent to `useMemo(() => fn, deps)`.
    -   It returns the *function itself*, which you can then call later.
    -   Its primary use case is to maintain referential equality for callbacks passed to optimized child components.

-   **`useMemo` memoizes the return value of a function.**
    -   It **calls** the function and returns its result.
    -   Its primary use case is to avoid re-computing expensive values on every render.

| Hook          | What it Memoizes        | What it Returns      | Primary Use Case                                    |
|---------------|-------------------------|----------------------|-----------------------------------------------------|
| `useCallback` | The function itself     | A memoized function  | Passing stable callbacks to optimized components.   |
| `useMemo`     | The result of a function| A memoized value     | Avoiding expensive calculations on every render.    |

#### Example: Memoizing an Expensive Calculation

Imagine a component where you perform a complex calculation based on a prop. If the component re-renders for other reasons (e.g., unrelated state changes), you don't want to re-run this expensive calculation unnecessarily.

```javascript
import React, { useState, useMemo } from 'react';

// An expensive function that we want to avoid re-running
const expensiveCalculation = (num) => {
  console.log('Performing expensive calculation...');
  let result = 0;
  for (let i = 0; i < 1000000000; i++) {
    result += num;
  }
  return result;
};

function Calculator({ number }) {
  const [unrelatedState, setUnrelatedState] = useState(0);

  // Use useMemo to memoize the result of the expensive calculation.
  // It will only re-run if the 'number' prop changes.
  const calculationResult = useMemo(() => expensiveCalculation(number), [number]);

  return (
    <div>
      <h2>Calculation Result: {calculationResult}</h2>
      <p>This button updates unrelated state, which would normally cause a re-render and re-calculation.</p>
      <button onClick={() => setUnrelatedState(c => c + 1)}>
        Re-render Component ({unrelatedState})
      </button>
    </div>
  );
}

export default Calculator;
```

**Behavior:**

1.  When the `Calculator` component first renders, `expensiveCalculation` is called, and the result is stored in `calculationResult`.
2.  When you click the "Re-render Component" button, the `unrelatedState` changes, and the component re-renders.
3.  Because `number` (the dependency of `useMemo`) has not changed, `useMemo` does **not** re-run `expensiveCalculation`. It returns the previously memoized value.
4.  The "Performing expensive calculation..." message will only appear in the console when the `number` prop itself changes, proving that the expensive work is being skipped on other re-renders.

---

### Q52: What are custom Hooks and why are they useful?

**Answer:**

A custom Hook is a **JavaScript function** whose name starts with `"use"` and that can call other Hooks. They are a core feature of React that lets you extract component logic into reusable functions.

Before Hooks, the primary ways to share stateful logic between components were render props and higher-order components (HOCs), which often led to complex component hierarchies ("wrapper hell"). Custom Hooks solve this problem more elegantly.

#### Why are they useful?

1.  **Reusability**: You can write a piece of logic once and use it in multiple components.
2.  **Clean Components**: They help keep your components clean and focused on rendering UI, as the complex logic is abstracted away.
3.  **Composition**: You can compose custom Hooks together, just like you compose components.
4.  **No Wrapper Hell**: Unlike HOCs or Render Props, custom Hooks don't add extra nodes to the component tree.

#### Rules for Creating Custom Hooks

1.  **Name must start with `use`**: This is a convention that allows React's linter to check for violations of the Rules of Hooks.
2.  **Call other Hooks**: A custom Hook's purpose is to reuse stateful logic, so it will almost always use built-in Hooks like `useState`, `useEffect`, or `useContext`.

#### Example: A `useFetch` Custom Hook

A very common use case is fetching data. Instead of writing the same `useState` and `useEffect` logic in every component that needs to fetch data, you can create a `useFetch` hook.

```javascript:src/hooks/useFetch.js
import { useState, useEffect } from 'react';

function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);
      try {
        const response = await fetch(url);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const result = await response.json();
        setData(result);
      } catch (e) {
        setError(e);
      } finally {
        setLoading(false);
      }
    };

    fetchData();

    // Cleanup function to cancel any pending request if the component unmounts
    // This is a simplified example; a real-world useFetch might use AbortController
  }, [url]); // Re-run the effect if the URL changes

  // Return the stateful values for the component to use
  return { data, loading, error };
}

export default useFetch;
```

Now, any component can use this hook to fetch data with minimal boilerplate:

```javascript:src/components/MyComponent.js
import React from 'react';
import useFetch from '../hooks/useFetch';

function MyComponent() {
  const { data, loading, error } = useFetch('https://api.example.com/data');

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return (
    <div>
      <h1>Data</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}

export default MyComponent;
```

This approach makes the component logic much simpler and allows the data-fetching logic to be easily tested and reused across the application.

---

### Q53: What is React Router and what are its main components?

**Answer:**

React Router is the standard library for routing in React. It enables navigation among views of various components in a React Application, allows changing the browser URL, and keeps the UI in sync with the URL.

In essence, it allows you to build a single-page application (SPA) with navigation without the page refreshing as the user navigates. React Router uses a component-based structure to handle routing.

#### Main Components of React Router (v6)

1.  **`<BrowserRouter>`**: This is the parent component that should wrap your entire application (or at least the part of it that needs routing). It uses the HTML5 History API (pushState, replaceState, and the popstate event) to keep your UI in sync with the URL.

2.  **`<Routes>`**: A container for a collection of `<Route>` elements. It's responsible for looking through all its child `<Route>`s to find the best match for the current URL and rendering that branch of the UI. When a match is found, it stops searching and renders.

3.  **`<Route>`**: The core of React Router. A route has two main props:
    *   `path`: A string that describes the URL path the route should match (e.g., `/about`, `/users/:id`).
    *   `element`: The React element (component) to render when the URL matches the path.

4.  **`<Link>`**: The primary way to allow users to navigate around your application. It's an element that renders an `<a>` tag but with a key difference: clicking a `<Link>` will update the URL and render the corresponding `<Route>` without triggering a full page reload.
    *   It uses the `to` prop to specify the destination path (e.g., `<Link to="/about">About</Link>`).

#### Example: Basic Routing Setup

Here is a complete example of how to set up a basic navigation structure.

First, install React Router:
`npm install react-router-dom`

Then, set up the components and routes:

```javascript:src/App.js
import React from 'react';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';

// Define some simple components to act as pages
const Home = () => <h2>Home</h2>;
const About = () => <h2>About</h2>;
const Dashboard = () => <h2>Dashboard</h2>;

function App() {
  return (
    // 1. Wrap the application with BrowserRouter
    <BrowserRouter>
      <div>
        {/* 2. Create navigation links */}
        <nav>
          <ul>
            <li><Link to="/">Home</Link></li>
            <li><Link to="/about">About</Link></li>
            <li><Link to="/dashboard">Dashboard</Link></li>
          </ul>
        </nav>

        <hr />

        {/* 3. Define the routes */}
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/dashboard" element={<Dashboard />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
```

**How it works:**

-   When the user is at the root URL (`/`), the `<Home />` component is rendered.
-   When the user clicks the "About" link, the URL changes to `/about`, and the `<About />` component is rendered.
-   The page content changes dynamically without a browser refresh, providing a smooth user experience typical of a SPA.

---

### Q54: What is the difference between `<Link>` and `<NavLink>` in React Router?

**Answer:**

Both `<Link>` and `<NavLink>` are components provided by React Router to create navigation links. The fundamental difference is that **`<NavLink>` is a special version of `<Link>` that knows whether or not it is "active"**.

This "active" awareness makes `<NavLink>` ideal for building navigation menus (like breadcrumbs or a main navigation bar) where you want to visually distinguish the link corresponding to the current page.

#### Key Differences

| Feature         | `<Link>`                                      | `<NavLink>`                                                                                                 |
|-----------------|-----------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| **Purpose**     | Basic navigation from one route to another.   | Navigation where the link needs to be styled differently when it's active (i.e., its `to` prop matches the current URL). |
| **Styling**     | No special props for active styling.          | Provides props like `className` and `style` that can be functions to apply styles conditionally.            |
| **Functionality** | Renders an `<a>` tag for navigation.          | Renders an `<a>` tag and automatically adds an `active` class by default when the link is active.           |

#### How to Use `NavLink` for Active Styling

`NavLink` allows you to determine if the link is active by passing a function to its `style` or `className` props. This function receives an object with an `isActive` boolean property.

**Example:**

```javascript
import { NavLink } from 'react-router-dom';

const Navigation = () => {
  const activeStyle = {
    textDecoration: 'underline',
    color: 'red'
  };

  return (
    <nav>
      <ul>
        <li>
          <NavLink 
            to="/"
            style={({ isActive }) => isActive ? activeStyle : undefined}
          >
            Home
          </NavLink>
        </li>
        <li>
          <NavLink 
            to="/about"
            className={({ isActive }) => isActive ? 'active-link' : 'inactive-link'}
          >
            About
          </NavLink>
        </li>
      </ul>
    </nav>
  );
};

export default Navigation;
```

In this example:

1.  **Home Link**: Uses the `style` prop. When the user is at the homepage (`/`), the `isActive` boolean will be `true`, and the `activeStyle` object will be applied, making the link underlined and red.
2.  **About Link**: Uses the `className` prop. When the user is on the `/about` page, the link will be rendered with the CSS class `active-link`, which you can then style in your CSS file (e.g., `.active-link { font-weight: bold; }`).

**Conclusion:**

-   Use **`<Link>`** for standard links where no special styling is needed for the active state.
-   Use **`<NavLink>`** when you need to apply styles or classes to a link to indicate that it is the currently active page.

---

### Q55: How do you handle 404 (Not Found) pages in React Router?

**Answer:**

In React Router, you can handle 404 (Not Found) errors by defining a "catch-all" route. This is a route that will match any URL that hasn't been matched by any of the other routes defined in your application.

This is achieved by creating a `<Route>` with its `path` prop set to `"*"`.

#### Implementation

The key is to place this catch-all route at the **end** of your `<Routes>` definition. React Router's `<Routes>` component searches through its children `<Route>`s from top to bottom and renders the *first* one that matches the current URL. By putting the `path="*"` route last, you ensure that it only matches if no other more specific routes have matched first.

**Example:**

```javascript
import React from 'react';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';

// Page components
const Home = () => <h2>Home</h2>;
const About = () => <h2>About</h2>;

// 404 Not Found component
const NotFound = () => (
  <div>
    <h2>404 - Page Not Found</h2>
    <p>The page you are looking for does not exist.</p>
    <Link to="/">Go to Homepage</Link>
  </div>
);

function App() {
  return (
    <BrowserRouter>
      <nav>
        <Link to="/">Home</Link> | <Link to="/about">About</Link>
      </nav>
      <hr />
      <Routes>
        {/* Specific routes first */}
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />

        {/* Catch-all 404 route last */}
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
```

**How it works:**

1.  If the user navigates to `/`, the first `<Route>` matches, and the `Home` component is rendered.
2.  If the user navigates to `/about`, the second `<Route>` matches, and the `About` component is rendered.
3.  If the user navigates to any other URL (e.g., `/contact`, `/products/123`, or `/some-random-text`), React Router will fail to match the first two routes.
4.  It will then fall through to the last route, `path="*"`, which acts as a wildcard and matches anything. The `NotFound` component is then rendered, displaying the 404 message.

---

### Q56: How do you pass data through routes in React Router?

**Answer:**

There are several ways to pass data between routes in React Router, each suited for different use cases. The most common methods are URL Parameters and Query Parameters.

#### 1. URL Parameters

URL parameters are used to capture dynamic segments of a URL. They are ideal for passing required data that identifies a specific resource, like a user ID or a product slug.

**How to use:**

1.  **Define the route path** with a colon (`:`) to mark a parameter (e.g., `/users/:userId`).
2.  **Create a link** to that path with a specific value (e.g., `/users/123`).
3.  **Access the parameter** in the destination component using the `useParams` hook.

**Example:**

```javascript
import { Routes, Route, Link, useParams } from 'react-router-dom';

// Component to display user profile
const UserProfile = () => {
  // 3. Access the userId from the URL
  const { userId } = useParams();
  return <h2>User Profile for ID: {userId}</h2>;
};

function App() {
  return (
    <div>
      <nav>
        {/* 2. Link to a specific user */}
        <Link to="/users/123">User 123</Link> | <Link to="/users/456">User 456</Link>
      </nav>
      <Routes>
        {/* 1. Define the route with a URL parameter */}
        <Route path="/users/:userId" element={<UserProfile />} />
      </Routes>
    </div>
  );
}
```

#### 2. Query Parameters (Search Params)

Query parameters are used for optional data, such as filtering, sorting, or search queries. They appear at the end of the URL after a `?` and are formatted as key-value pairs (e.g., `/search?query=react&sort=asc`).

**How to use:**

1.  **Create a link** with a search string (e.g., `/search?query=hooks`).
2.  **Access the parameters** in the destination component using the `useSearchParams` hook.

**Example:**

```javascript
import { Routes, Route, Link, useSearchParams } from 'react-router-dom';

const SearchResults = () => {
  // 2. Access the search params
  const [searchParams] = useSearchParams();
  const query = searchParams.get('query'); // Get a specific param
  const sort = searchParams.get('sort');

  return (
    <div>
      <h2>Search Results</h2>
      <p>Query: {query}</p>
      <p>Sort by: {sort}</p>
    </div>
  );
};

function App() {
  return (
    <div>
      <nav>
        {/* 1. Link with query parameters */}
        <Link to="/search?query=react-router&sort=popular">Search for React Router</Link>
      </nav>
      <Routes>
        <Route path="/search" element={<SearchResults />} />
      </Routes>
    </div>
  );
}
```

| Method            | Use Case                                    | URL Appearance              | How to Access        |
|-------------------|---------------------------------------------|-----------------------------|----------------------|
| **URL Parameters**  | Required data, resource identifiers (e.g., ID) | `/users/123`                | `useParams`          |
| **Query Parameters**| Optional data, filtering, sorting           | `/products?color=blue`      | `useSearchParams`    |

---

### Q57: How do you perform programmatic navigation in React Router?

**Answer:**

Programmatic navigation refers to changing routes imperatively (i.e., from within your component's logic, like after a form submission or a timeout) rather than declaratively through a `<Link>` or `<NavLink>` component.

In React Router (v6 and later), this is primarily done using the **`useNavigate`** hook.

#### The `useNavigate` Hook

The `useNavigate` hook returns a function that lets you navigate to a different route. You can call this function with a path to navigate to.

`const navigate = useNavigate();`

-   `navigate('/some/path')`: Navigates to the specified path.
-   `navigate(-1)`: Navigates back to the previous entry in the history stack (equivalent to clicking the browser's back button).
-   `navigate(1)`: Navigates forward.
-   `navigate('/some/path', { replace: true })`: Navigates to the path but replaces the current entry in the history stack instead of pushing a new one. This is useful for login flows where you don't want the user to be able to go back to the login page after successfully logging in.

#### Example: Redirecting After a Form Submission

A common use case is redirecting the user to a different page after they successfully submit a form.

```javascript
import { useNavigate, Routes, Route } from 'react-router-dom';

const LoginSuccess = () => <h2>Login Successful! Welcome to the dashboard.</h2>;

const LoginForm = () => {
  const navigate = useNavigate();

  const handleLogin = (event) => {
    event.preventDefault();
    // In a real app, you would perform authentication here
    console.log('Simulating successful login...');

    // Redirect to the dashboard page, replacing the login page in history
    navigate('/dashboard', { replace: true });
  };

  return (
    <form onSubmit={handleLogin}>
      <h2>Login</h2>
      <button type="submit">Log In</button>
    </form>
  );
};

function App() {
  return (
    <Routes>
      <Route path="/" element={<LoginForm />} />
      <Route path="/dashboard" element={<LoginSuccess />} />
    </Routes>
  );
}
```

**How it works:**

1.  The `LoginForm` component gets the `navigate` function by calling `useNavigate()`.
2.  When the user submits the form, the `handleLogin` function is executed.
3.  After the simulated login logic, `navigate('/dashboard', { replace: true })` is called.
4.  React Router changes the URL to `/dashboard`, and the `LoginSuccess` component is rendered.
5.  Because `{ replace: true }` was used, the `/` route (the login form) is removed from the browser's history stack. If the user clicks the back button, they won't be taken back to the login form.

---

### Q58: What are nested routes and how do you implement them in React Router?

**Answer:**

Nested routes are a powerful feature of React Router that allow you to build complex layouts where a part of the UI is shared across a set of routes. For example, a user dashboard might have a consistent sidebar and header, while the main content area changes.

This is achieved by nesting `<Route>` components inside one another. The parent route defines a layout, and the child routes render their components within that layout.

#### The `<Outlet>` Component

The key to nested routing is the **`<Outlet>`** component. A parent route's element should render an `<Outlet>`. This component acts as a placeholder, marking the spot where the matched child route's element should be rendered.

#### How to Implement Nested Routes

1.  **Structure your routes** by nesting `<Route>` components. The parent `<Route>` will have a path, and its children will have paths relative to the parent.
2.  **Create a layout component** for the parent route. This component will contain the shared UI (like a navbar or sidebar) and an `<Outlet />` component to render the children.

**Example: A Dashboard Layout**

Imagine a dashboard at `/dashboard` with two sub-pages: `/dashboard/profile` and `/dashboard/settings`.

```javascript
import { Routes, Route, Link, Outlet } from 'react-router-dom';

// 1. Create the layout component for the parent route
const DashboardLayout = () => (
  <div>
    <h1>Dashboard</h1>
    <nav>
      <Link to="profile">Profile</Link> | <Link to="settings">Settings</Link>
    </nav>
    <hr />
    {/* 2. Use Outlet to render the child route's element */}
    <main>
      <Outlet />
    </main>
  </div>
);

// Child route components
const DashboardHome = () => <h3>Welcome to your dashboard!</h3>;
const Profile = () => <h3>Your Profile</h3>;
const Settings = () => <h3>Your Settings</h3>;

function App() {
  return (
    <Routes>
      {/* 3. Define the nested routes */}
      <Route path="/dashboard" element={<DashboardLayout />}>
        {/* Index route: rendered when the parent's path matches exactly */}
        <Route index element={<DashboardHome />} />
        
        {/* Child routes: paths are relative to the parent */}
        <Route path="profile" element={<Profile />} />
        <Route path="settings" element={<Settings />} />
      </Route>
      {/* Other top-level routes can go here */}
      <Route path="/" element={<h2>Home Page</h2>} />
    </Routes>
  );
}
```

**How it works:**

-   When the URL is `/dashboard`, the `DashboardLayout` is rendered. Because the `index` route is present, the `DashboardHome` component is rendered inside the `<Outlet>`.
-   When the URL is `/dashboard/profile`, the `DashboardLayout` is still the parent. The `Profile` component is rendered inside the `<Outlet>` because its path (`profile`) matches the remaining part of the URL.
-   When the URL is `/dashboard/settings`, the `Settings` component is rendered inside the `<Outlet>`.

This pattern is extremely useful for creating clean, hierarchical UI structures where common layouts are shared across multiple pages.

---

### Q59: How do you create protected routes in React Router?

**Answer:**

Protected routes are used to restrict access to certain parts of an application, such as a user dashboard, to authenticated users only. If an unauthenticated user tries to access a protected route, they are typically redirected to a login page.

In React Router v6, this is commonly implemented by creating a wrapper component that conditionally renders its children or redirects.

#### Key Components

1.  **A Wrapper Component (`ProtectedRoute`)**: This component checks for an authentication condition.
    *   If the user is authenticated, it renders the `<Outlet />` component, which in turn renders the actual route's component.
    *   If the user is not authenticated, it uses the `<Navigate>` component to redirect them to a login page.
2.  **Authentication Logic**: A way to determine if the user is logged in. This could be a simple boolean flag in state, a token in local storage, or a value from a context provider.

#### How to Implement Protected Routes

**Example: Protecting a Dashboard**

Let's assume we have a simple `useAuth` hook that tells us if a user is logged in.

```javascript
import { Routes, Route, Navigate, Outlet } from 'react-router-dom';

// A mock authentication hook
const useAuth = () => {
  // In a real app, you'd have logic to check for a token, user session, etc.
  const user = { loggedIn: true }; // Change to false to test the redirect
  return user && user.loggedIn;
};

// 1. Create the ProtectedRoute component
const ProtectedRoute = () => {
  const isAuth = useAuth();
  // If authorized, return an outlet that will render child elements
  // If not, return element that will navigate to login page
  return isAuth ? <Outlet /> : <Navigate to="/login" />;
};

// Components for our routes
const HomePage = () => <h2>Home Page (Public)</h2>;
const LoginPage = () => <h2>Login Page (Public)</h2>;
const Dashboard = () => <h2>Dashboard (Protected)</h2>;

function App() {
  return (
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/login" element={<LoginPage />} />

      {/* 2. Wrap protected routes in the ProtectedRoute component */}
      <Route element={<ProtectedRoute />}>
        {/* Routes that require authentication go here */}
        <Route path="/dashboard" element={<Dashboard />} />
        {/* You can add more protected routes here */}
        {/* e.g., <Route path="/settings" element={<Settings />} /> */}
      </Route>
    </Routes>
  );
}
```

**How it works:**

1.  The routes are structured so that any route nested inside `<Route element={<ProtectedRoute />}>` becomes a protected route.
2.  When a user navigates to `/dashboard`:
    *   React Router matches the parent route, which renders the `ProtectedRoute` component.
    *   The `ProtectedRoute` component calls `useAuth()`.
    *   **If `useAuth()` returns `true`**: The component returns `<Outlet />`. React Router then proceeds to render the matched child route's element, which is `<Dashboard />`.
    *   **If `useAuth()` returns `false`**: The component returns `<Navigate to="/login" />`. This declaratively redirects the user to the `/login` page. The `<Dashboard />` component is never rendered.

This approach is clean, declarative, and leverages the composition model of React Router v6 effectively.

---

### Q60: What is lazy loading and how do you implement it in React?

**Answer:**

**Lazy loading** (or code-splitting) is a performance optimization technique where you delay the loading of certain parts of your application until they are actually needed. In React, this typically means loading components only when they are about to be rendered.

By default, bundlers like Webpack or Vite create a single JavaScript file (a "bundle") containing all the application code. As the application grows, this bundle can become very large, increasing the initial load time. Lazy loading splits this bundle into smaller chunks, which are loaded on demand.

#### How to Implement Lazy Loading in React

React provides two core features to make lazy loading simple:

1.  **`React.lazy()`**: A function that lets you render a dynamic `import()` as a regular component. It takes a function that must call a dynamic `import()`. This returns a Promise which resolves to a module with a `default` export containing a React component.

2.  **`React.Suspense`**: A component that lets you specify a loading indicator (a "fallback") if the component in its tree is not yet ready to render.

**Example: Lazy Loading a Component**

Imagine you have a large `ChartComponent` that you only want to load when the user clicks a button.

```javascript
import React, { useState, Suspense } from 'react';

// 1. Use React.lazy to create a lazy-loaded component
// The import() function returns a Promise.
const ChartComponent = React.lazy(() => import('./ChartComponent'));

// A simple fallback component to show while loading
const LoadingIndicator = () => <p>Loading chart...</p>;

function App() {
  const [showChart, setShowChart] = useState(false);

  return (
    <div>
      <h1>My Dashboard</h1>
      <button onClick={() => setShowChart(true)}>Show Chart</button>

      {/* 3. Wrap the lazy component in Suspense */}
      {showChart && (
        <Suspense fallback={<LoadingIndicator />}>
          <ChartComponent />
        </Suspense>
      )}
    </div>
  );
}

// In a separate file: ./ChartComponent.js
// const ChartComponent = () => {
//   // Imagine this is a large component with heavy dependencies
//   return <h2>Here is the very large chart!</h2>;
// };
// export default ChartComponent;
```

**How it works:**

1.  When `App` first renders, the code for `ChartComponent` is **not** included in the main bundle. The `ChartComponent` variable holds a special "lazy" component object.
2.  The user sees the "Show Chart" button.
3.  When the button is clicked, `showChart` becomes `true`.
4.  React attempts to render `<ChartComponent />`.
5.  Since the component's code hasn't been loaded yet, React triggers the nearest `<Suspense>` boundary's `fallback`. The user sees "Loading chart...".
6.  In the background, React triggers the dynamic `import('./ChartComponent')` call. The browser fetches this new JavaScript chunk.
7.  Once the chunk is loaded and the `ChartComponent` is ready, `Suspense` automatically swaps the fallback UI with the actual `ChartComponent`.

#### Best Practices

*   **Route-based code-splitting**: The most common and effective use case for lazy loading is to split code by routes. You can lazy-load the components associated with each route.
*   **Use a meaningful fallback**: Provide a good loading experience (e.g., a skeleton screen) so the user understands that content is on its way.
*   **Error Boundaries**: Wrap your `Suspense` component with an [Error Boundary](https://reactjs.org/docs/error-boundaries.html) to gracefully handle cases where the dynamic import fails (e.g., due to a network error).

---

### Q61: What is Redux and what are its core principles?

**Answer:**

**Redux** is a predictable state container for JavaScript applications, most commonly used with React. It helps you manage the application's state in a single, centralized location, making state management more predictable and easier to debug, especially in large and complex applications.

While React's built-in state management (like `useState` and `useContext`) is sufficient for many applications, Redux provides a more robust solution for handling global state that is accessed by many components.

#### The Three Core Principles of Redux

Redux is built on three fundamental principles:

1.  **Single Source of Truth**: The entire state of your application is stored in a single object tree within a single **store**. This makes it easy to debug, inspect, and persist the application state.

2.  **State is Read-Only**: The only way to change the state is to dispatch an **action**, which is a plain JavaScript object describing what happened. You cannot directly modify the state object. This ensures that neither the views nor network callbacks will ever write to the state directly, preventing race conditions and making changes predictable.

3.  **Changes are Made with Pure Functions**: To specify how the state tree is transformed by actions, you write pure **reducers**. A reducer is a function that takes the previous state and an action, and returns the next state. Because reducers are pure functions, they produce the same output for the same input, making them easy to test and reason about.

#### Core Concepts

*   **Store**: The single object that holds the application state. It is created using the `createStore` function (or `configureStore` from Redux Toolkit).
*   **Actions**: Plain JavaScript objects that represent an intention to change the state. They must have a `type` property. Example: `{ type: 'INCREMENT_COUNTER' }`.
*   **Reducers**: Pure functions that take the current state and an action and return a new state. Example: `(state, action) => newState`.

**Simple Example (Conceptual)**

```javascript
// 1. Action: An object describing the change
const incrementAction = { type: 'INCREMENT' };

// 2. Reducer: A pure function to handle the action
const counterReducer = (state = { value: 0 }, action) => {
  switch (action.type) {
    case 'INCREMENT':
      return { value: state.value + 1 };
    default:
      return state; // Always return the existing state for unhandled actions
  }
};

// 3. Store: Holds the state and is created with the reducer
import { createStore } from 'redux';
const store = createStore(counterReducer);

// To change the state, you dispatch an action
console.log('Initial state:', store.getState()); // { value: 0 }
store.dispatch(incrementAction);
console.log('State after increment:', store.getState()); // { value: 1 }
```

While this is a basic example, modern Redux development almost always uses **Redux Toolkit**, which simplifies these patterns and reduces boilerplate code significantly.

---

### Q62: What is the difference between `connect()` and React Redux hooks like `useSelector` and `useDispatch`?

**Answer:**

Both `connect()` and the React Redux hooks (`useSelector`, `useDispatch`) serve the same purpose: to connect React components to the Redux store. However, they represent two different APIs for doing so—the older higher-order component (HOC) pattern and the modern hooks-based approach.

#### `connect()` Higher-Order Component (HOC)

`connect()` is a higher-order component provided by the `react-redux` library. It wraps your component and injects props into it.

*   **`mapStateToProps(state, [ownProps])`**: This function subscribes your component to store updates. It takes the entire Redux state and returns an object of data that your component needs. This object is then merged into the component's props.
*   **`mapDispatchToProps(dispatch, [ownProps])`**: This function gives your component access to the `dispatch` function. You can return an object where each key is a prop name and each value is a function that dispatches an action.

**Example with `connect()`:**

```javascript
import React from 'react';
import { connect } from 'react-redux';

class Counter extends React.Component {
  render() {
    return (
      <div>
        <p>Count: {this.props.count}</p>
        <button onClick={this.props.increment}>Increment</button>
      </div>
    );
  }
}

// Maps state to props
const mapStateToProps = (state) => ({
  count: state.counter.value,
});

// Maps dispatch to props
const mapDispatchToProps = (dispatch) => ({
  increment: () => dispatch({ type: 'INCREMENT' }),
});

// connect() returns a new, wrapped component
export default connect(mapStateToProps, mapDispatchToProps)(Counter);
```

#### React Redux Hooks (`useSelector` and `useDispatch`)

The hooks API was introduced in `react-redux` v7.1 and is now the recommended way to interact with the Redux store in functional components.

*   **`useSelector()`**: Allows you to extract data from the Redux store state. It takes a selector function as an argument, which receives the entire state and returns the specific piece of data you need. It's analogous to `mapStateToProps`.
*   **`useDispatch()`**: Returns a reference to the `dispatch` function from the Redux store. You can use it to dispatch actions as needed. It's analogous to `mapDispatchToProps`.

**Example with Hooks:**

```javascript
import React from 'react';
import { useSelector, useDispatch } from 'react-redux';

const Counter = () => {
  // Get the specific state value you need
  const count = useSelector((state) => state.counter.value);
  
  // Get the dispatch function
  const dispatch = useDispatch();

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => dispatch({ type: 'INCREMENT' })}>Increment</button>
    </div>
  );
};

export default Counter;
```

#### Comparison

| Feature             | `connect()` HOC                                       | `useSelector` / `useDispatch` Hooks                     |
| ------------------- | ----------------------------------------------------- | ------------------------------------------------------- |
| **Component Type**  | Works with both class and functional components.      | **Only works in functional components.**                |
| **Code Verbosity**  | More boilerplate (requires `mapStateToProps`, etc.).  | More concise and easier to read.                        |
| **Data Fetching**   | `mapStateToProps` typically returns an object of props. | `useSelector` can return any value, not just an object. |
| **Typing (TypeScript)** | Can be complex to type correctly.                     | Simpler and more direct to type with modern TypeScript. |
| **Composition**     | Wraps components, which can lead to "wrapper hell."   | No extra component in the tree. Cleaner composition.    |

**Conclusion:**

The hooks API (`useSelector`, `useDispatch`) is the modern, recommended standard for new React-Redux applications. It is more concise, easier to use with TypeScript, and fits better with the functional programming paradigm of modern React. The `connect()` HOC is still supported for legacy codebases and class components.

---

### Q63: What is Redux middleware and what is it used for?

**Answer:**

**Redux middleware** provides a third-party extension point between dispatching an action and the moment it reaches the reducer. It allows you to write custom logic that intercepts every action before it is passed to the reducer.

In essence, middleware acts as a layer between `dispatch()` and the reducers. When you dispatch an action, it first goes through the middleware chain, and each middleware can inspect the action, modify it, dispatch other actions, or even stop the action from reaching the reducer.

#### What is it Used For?

Middleware is the right place to put logic that needs to interact with the outside world or perform asynchronous tasks. Common use cases include:

*   **Asynchronous API Calls**: The most common use case. Middleware like **Redux Thunk** or **Redux Saga** allows you to write action creators that can make API calls and dispatch new actions based on the results (e.g., `FETCH_DATA_SUCCESS` or `FETCH_DATA_FAILURE`).
*   **Logging**: Creating a logger to `console.log` every action that is dispatched and the resulting state changes. This is great for debugging.
*   **Routing**: Dispatching routing actions to navigate between pages.
*   **Error Reporting**: Catching errors from actions and sending them to a reporting service.

#### How Middleware Works

A middleware is a higher-order function with the signature `store => next => action => ...`.

1.  It receives the `store` instance, giving it access to `getState()` and `dispatch()`.
2.  It receives `next`, which is a function that, when called, passes the action to the *next* middleware in the chain. The last middleware's `next` is the original `dispatch()` to the reducers.
3.  It receives the `action` that was dispatched.

**Example: A Simple Logger Middleware**

Here is a basic middleware that logs the action type and the state before and after the action is processed.

```javascript
// loggerMiddleware.js
const loggerMiddleware = store => next => action => {
  console.log('Dispatching:', action.type);
  
  // Call the next middleware in the chain (or the reducer)
  const result = next(action);
  
  console.log('Next state:', store.getState());
  
  // Return the result of the next middleware
  return result;
};

// To use it, you apply it when creating the store:
import { createStore, applyMiddleware } from 'redux';
import rootReducer from './reducers';

const store = createStore(
  rootReducer,
  applyMiddleware(loggerMiddleware)
);
```

**Explanation:**

1.  When an action is dispatched (e.g., `store.dispatch({ type: 'INCREMENT' })`), it first hits `loggerMiddleware`.
2.  The middleware logs "Dispatching: INCREMENT".
3.  It then calls `next(action)`, passing the action along. If there were other middlewares, it would go to the next one. If not, the action goes to the reducers.
4.  The reducers update the state.
5.  After the reducers have finished, the `next(action)` call returns, and the middleware logs the new state by calling `store.getState()`.

This powerful pattern allows for clean separation of concerns, keeping reducers pure while handling complex side effects in a predictable, centralized way.

---

### Q64: What is the difference between Redux Thunk and Redux Saga?

**Answer:**

Both **Redux Thunk** and **Redux Saga** are middleware libraries for Redux that help manage asynchronous operations (side effects), like fetching data from an API. They solve the same problem but use fundamentally different approaches.

#### Redux Thunk

Redux Thunk is the simpler of the two. It allows you to write action creators that return a **function** instead of a plain action object. This function, called a "thunk," receives the store's `dispatch` and `getState` methods as arguments.

**Core Idea**: Delay the dispatch of an action, or dispatch only if a certain condition is met. Inside the thunk, you can perform asynchronous logic and dispatch actions.

**Example: Fetching Data with Thunk**

```javascript
// Action creator returning a function (a thunk)
const fetchUser = (id) => {
  // The thunk receives dispatch and getState
  return async (dispatch, getState) => {
    dispatch({ type: 'FETCH_USER_REQUEST' });
    try {
      const response = await fetch(`https://api.example.com/users/${id}`);
      const user = await response.json();
      dispatch({ type: 'FETCH_USER_SUCCESS', payload: user });
    } catch (error) {
      dispatch({ type: 'FETCH_USER_FAILURE', error: error.message });
    }
  };
};

// In your component, you would dispatch this thunk:
// dispatch(fetchUser(123));
```

#### Redux Saga

Redux Saga uses **ES6 Generators** to make asynchronous flows easy to read, write, and test. Instead of dispatching functions, sagas listen for dispatched actions and trigger generator functions ("sagas") to run.

**Core Idea**: Sagas run in the background, like a separate thread in your application, listening for actions. They are implemented as generator functions that `yield` plain JavaScript objects called **Effects**. These Effects are instructions for the saga middleware to perform some operation (e.g., make an API call, dispatch an action).

**Example: Fetching Data with Saga**

```javascript
import { call, put, takeEvery } from 'redux-saga/effects';

// Worker Saga: performs the async task
function* fetchUserSaga(action) {
  try {
    // `call` is an Effect that tells the middleware to call a function
    const user = yield call(fetch, `https://api.example.com/users/${action.payload.id}`);
    const userData = yield user.json();
    
    // `put` is an Effect that tells the middleware to dispatch an action
    yield put({ type: 'FETCH_USER_SUCCESS', payload: userData });
  } catch (error) {
    yield put({ type: 'FETCH_USER_FAILURE', error: error.message });
  }
}

// Watcher Saga: listens for actions and starts the worker saga
function* mySaga() {
  // `takeEvery` listens for every 'FETCH_USER_REQUEST' action
  yield takeEvery('FETCH_USER_REQUEST', fetchUserSaga);
}

// In your component, you would dispatch a plain action object:
// dispatch({ type: 'FETCH_USER_REQUEST', payload: { id: 123 } });
```

#### Comparison

| Feature          | Redux Thunk                                                              | Redux Saga                                                                      |
| ---------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------- |
| **Concept**      | Action creators can return functions (thunks).                           | Uses ES6 Generators to run tasks in the background, listening for actions.      |
| **Complexity**   | **Simple**. Easy to learn and has a minimal API.                         | **Complex**. Requires understanding generators and the saga effect creators API. |
| **Control Flow** | Logic is inside the action creator. Can lead to callback-hell style code. | Logic is centralized in sagas. Easier to manage complex, long-running tasks.    |
| **Testability**  | Can be harder to test, as thunks are not pure functions.                 | **Highly testable**. Generators yield plain objects (Effects), which can be easily tested. |
| **Use Case**     | Good for simple to moderately complex asynchronous logic.                | Excellent for complex scenarios like concurrent tasks, debouncing, or cancellation. |

**Conclusion:**

*   Choose **Redux Thunk** for smaller projects or if you prefer simplicity.
*   Choose **Redux Saga** for larger applications with complex asynchronous workflows that require fine-grained control and high testability.

---

### Q65: What is Redux Toolkit and why is it recommended for Redux development?

**Answer:**

**Redux Toolkit (RTK)** is the official, opinionated, batteries-included toolset for efficient Redux development. It was created by the Redux team to address common complaints about Redux, such as too much boilerplate code, the need to add many packages to get a basic setup, and the complexity of configuring the store.

RTK is now the **standard and recommended way** to write Redux logic. It simplifies and standardizes the process, making the code more maintainable and easier to write.

#### Key Features and Benefits

Redux Toolkit includes several key utilities that simplify the most common Redux tasks:

1.  **`configureStore()`**: A wrapper around the original `createStore` function that simplifies store setup. It automatically:
    *   Combines your slice reducers.
    *   Adds the Redux Thunk middleware by default.
    *   Enables the Redux DevTools Extension in development mode.

2.  **`createSlice()`**: This is the most powerful feature. It lets you define a "slice" of the Redux state, and it automatically generates action creators and action types from your reducer functions. It also uses the **Immer** library internally, which allows you to write "mutating" immutable update logic.

3.  **`createAsyncThunk()`**: A utility for creating thunks to handle asynchronous logic like API requests. It standardizes the process by automatically dispatching pending, fulfilled, and rejected actions, which you can handle in your reducers.

#### Why is it Recommended?

*   **Reduces Boilerplate**: `createSlice` eliminates the need to write action type constants and action creator functions by hand. This is the biggest source of boilerplate in traditional Redux.
*   **Simplifies Immutable Updates**: By using Immer, you can write simple, direct mutation logic (e.g., `state.value += 1`) in your reducers, and RTK will handle the complex immutable updates behind the scenes. This prevents common bugs related to accidental state mutation.
*   **Opinionated and Standardized**: It provides a standard way of structuring Redux logic, making it easier for developers to switch between projects and understand the codebase.
*   **Batteries-Included**: It includes Redux Thunk and Reselect (for creating memoized selectors) out of the box, which are essential for most Redux applications.

**Example: A Counter Slice with Redux Toolkit**

```javascript
import { createSlice, configureStore } from '@reduxjs/toolkit';

// 1. Create a slice of the state with createSlice
const counterSlice = createSlice({
  name: 'counter', // The name of the slice
  initialState: {
    value: 0,
  },
  // Reducers are defined as an object of functions
  reducers: {
    // The key 'increment' becomes the action type
    increment: (state) => {
      // Immer lets you write "mutating" logic here
      state.value += 1;
    },
    decrement: (state) => {
      state.value -= 1;
    },
    // Action with a payload
    incrementByAmount: (state, action) => {
      state.value += action.payload;
    },
  },
});

// 2. Export the auto-generated action creators
export const { increment, decrement, incrementByAmount } = counterSlice.actions;

// 3. Configure the store
const store = configureStore({
  reducer: {
    // Add the slice reducer to the store
    counter: counterSlice.reducer,
  },
});

// 4. Using it in a component (with hooks)
import { useSelector, useDispatch } from 'react-redux';

function Counter() {
  const count = useSelector((state) => state.counter.value);
  const dispatch = useDispatch();

  return (
    <div>
      <button onClick={() => dispatch(increment())}>Increment</button>
      <span>{count}</span>
      <button onClick={() => dispatch(decrement())}>Decrement</button>
    </div>
  );
}
```

In summary, Redux Toolkit is not a different version of Redux—it **is** Redux, but with a simpler, more efficient, and less error-prone API. It is the modern standard for all new Redux applications.

---

### Q66: How do you test React components?

**Answer:**

Testing React components is crucial for building reliable and maintainable applications. The modern approach to testing focuses on user-centric testing, which means you test components from the user's perspective rather than testing implementation details.

The most popular and recommended toolset for this is **Jest** and **React Testing Library (RTL)**.

*   **Jest**: A JavaScript testing framework that provides a test runner, assertion library, and mocking capabilities.
*   **React Testing Library (RTL)**: A library that provides utilities to test React components in a way that resembles how a user would interact with them. It encourages you to write tests that are more resilient to code refactoring.

#### Types of Component Tests

1.  **Unit Testing**: Testing a single component in isolation. You provide props and mock any dependencies to verify that the component renders correctly and that its individual logic works as expected.

2.  **Integration Testing**: Testing multiple components together to ensure they interact correctly. This often involves rendering a larger part of your application tree.

#### The React Testing Library Philosophy

RTL's guiding principle is:

> "The more your tests resemble the way your software is used, the more confidence they can give you."

This means you should:

*   **Query the DOM like a user**: Find elements by their text content, label, role, or other user-facing attributes, not by their CSS class, ID, or component name.
*   **Interact with the component**: Simulate user events like clicks, typing, and form submissions.
*   **Assert the result**: Check if the component's output matches what the user would see.

#### Example: Testing a Simple Counter Component

Let's say we have a `Counter` component:

```javascript
// Counter.js
import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}

export default Counter;
```

Here's how you would test it with Jest and React Testing Library:

```javascript
// Counter.test.js
import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom'; // for extra matchers like .toBeInTheDocument()
import Counter from './Counter';

describe('Counter component', () => {
  test('it renders the initial count and the increment button', () => {
    // 1. Render the component
    render(<Counter />);

    // 2. Query for elements a user would see
    // `getByText` finds an element by its text content.
    const countElement = screen.getByText(/count: 0/i);
    const buttonElement = screen.getByRole('button', { name: /increment/i });

    // 3. Assert that the elements are in the document
    expect(countElement).toBeInTheDocument();
    expect(buttonElement).toBeInTheDocument();
  });

  test('it increments the count when the button is clicked', () => {
    render(<Counter />);

    // Find the button
    const buttonElement = screen.getByRole('button', { name: /increment/i });

    // Simulate a user click
    fireEvent.click(buttonElement);

    // Assert that the count has updated
    // The count element now displays '1'
    const countElement = screen.getByText(/count: 1/i);
    expect(countElement).toBeInTheDocument();

    // Click again to be sure
    fireEvent.click(buttonElement);
    expect(screen.getByText(/count: 2/i)).toBeInTheDocument();
  });
});
```

**Key Steps in the Test:**

1.  **`render()`**: Renders the component into a virtual DOM.
2.  **`screen`**: An object that provides query methods to find elements in the rendered component.
3.  **Queries (`getBy...`, `findBy...`, `queryBy...`)**: Functions to find elements. `getByRole` and `getByText` are preferred because they reflect how users and assistive technologies find elements.
4.  **`fireEvent`**: An object with methods to simulate user interactions.
5.  **`expect()`**: The Jest assertion function, used with matchers (like `.toBeInTheDocument()`) to verify outcomes.

---

### Q67: How do you mock functions, modules, and components in Jest?

**Answer:**

Mocking is a fundamental technique in testing that involves replacing parts of your application with controlled, fake versions. In Jest, mocking is used to isolate the code you are testing from its dependencies (like API calls, helper functions, or child components).

Jest provides a powerful mocking library that can be used in several ways.

#### 1. Mocking Functions with `jest.fn()`

`jest.fn()` allows you to create a "spy" or a mock function. You can track how this function is called, what it's called with, and control its return value.

**Use Case**: Mocking a callback function passed as a prop.

```javascript
// Test if a button's onClick handler is called
test('calls the onClick prop when clicked', () => {
  const handleClick = jest.fn(); // Create a mock function
  render(<Button onClick={handleClick}>Click Me</Button>);
  
  fireEvent.click(screen.getByText(/click me/i));
  
  expect(handleClick).toHaveBeenCalledTimes(1); // Assert it was called once
});
```

#### 2. Mocking Modules with `jest.mock()`

`jest.mock()` is used to automatically mock an entire module. This is extremely useful for mocking API clients, third-party libraries, or internal utility modules.

**Use Case**: Mocking an API client module to avoid making real network requests.

Let's say you have an `api.js` module:

```javascript
// src/api.js
export const fetchUserProfile = async (userId) => {
  const response = await fetch(`/api/users/${userId}`);
  return response.json();
};
```

And a component that uses it:

```javascript
// UserProfile.js
import React, { useState, useEffect } from 'react';
import { fetchUserProfile } from './api';

function UserProfile({ userId }) {
  const [user, setUser] = useState(null);
  useEffect(() => {
    fetchUserProfile(userId).then(data => setUser(data));
  }, [userId]);

  if (!user) return <div>Loading...</div>;
  return <h1>{user.name}</h1>;
}
```

Here's how to test it by mocking the `api.js` module:

```javascript
// UserProfile.test.js
import { render, screen, waitFor } from '@testing-library/react';
import { fetchUserProfile } from './api';
import UserProfile from './UserProfile';

// 1. Mock the entire module
jest.mock('./api');

test('displays the user name after fetching', async () => {
  const mockUser = { name: 'John Doe' };
  // 2. Provide a mock implementation for the specific function
  fetchUserProfile.mockResolvedValue(mockUser);

  render(<UserProfile userId="123" />);

  // 3. Assert that the component displays the mocked data
  // `findBy` is async and waits for the element to appear
  const userName = await screen.findByText('John Doe');
  expect(userName).toBeInTheDocument();
});
```

#### 3. Mocking Components

Sometimes you want to prevent a child component from rendering its entire tree, especially if it's complex or has its own side effects. You can mock a component just like any other module.

**Use Case**: Mocking a heavy `ChartComponent` inside a `Dashboard` component.

```javascript
// Dashboard.test.js
import { render, screen } from '@testing-library/react';
import Dashboard from './Dashboard';

// Mock the ChartComponent. Jest replaces it with a simple mock.
jest.mock('./ChartComponent', () => () => <div data-testid="mock-chart">Mock Chart</div>);

test('renders the dashboard with a mock chart', () => {
  render(<Dashboard />);
  
  // The real ChartComponent is not rendered.
  // Instead, our mock version is.
  expect(screen.getByTestId('mock-chart')).toBeInTheDocument();
  expect(screen.getByText('Mock Chart')).toBeInTheDocument();
});
```

This approach is powerful because it keeps your tests fast and focused on the unit under test, preventing tests from breaking due to unrelated changes in dependencies.

---

### Q68: What is the difference between `getBy`, `queryBy`, and `findBy` queries in React Testing Library?

**Answer:**

React Testing Library provides three main types of queries to find elements on the page: `getBy`, `queryBy`, and `findBy`. The key difference between them is whether they throw an error when no element is found and whether they handle asynchronous elements.

Understanding which one to use is crucial for writing effective, non-brittle tests.

#### `getBy...`

*   **Behavior**: Returns the first matching node for a query. If **no elements** are found, it **throws an error**, which will fail your test immediately.
*   **When to use**: Use `getBy` for elements that you **expect to be present** in the DOM when the query is run. This is the most common type of query. If the element isn't there, your test should fail, and `getBy` ensures that it does.

**Example**:

```javascript
// Fails the test if the button is not found
const submitButton = screen.getByRole('button', { name: /submit/i });
expect(submitButton).toBeInTheDocument();
```

#### `queryBy...`

*   **Behavior**: Returns the first matching node for a query. If **no elements** are found, it returns **`null`** instead of throwing an error.
*   **When to use**: Use `queryBy` when you want to **assert that an element is not present**. Because it doesn't throw an error, it's perfect for verifying that something has been removed from the DOM.

**Example**:

```javascript
// After deleting an item
fireEvent.click(screen.getByRole('button', { name: /delete/i }));

// Assert that the item is no longer in the DOM
const deletedItem = screen.queryByText(/item to delete/i);
expect(deletedItem).not.toBeInTheDocument(); // or expect(deletedItem).toBeNull();
```

Using `getBy` here would throw an error and give a false negative, as the test would fail for the right reason (the element is gone).

#### `findBy...`

*   **Behavior**: Returns a **Promise** which resolves when an element is found. The promise is rejected if no element is found after a default timeout (usually 1000ms).
*   **When to use**: Use `findBy` for elements that will appear **asynchronously**. This is essential for testing components that fetch data, have timers, or wait for some other async operation to complete before rendering an element.

**Example**:

```javascript
// Test a component that fetches and displays data
test('it displays the user name after an API call', async () => {
  render(<UserProfile />);
  
  // `findBy` will wait for the 'Loading...' text to be replaced by the user's name
  const userName = await screen.findByText(/john doe/i);
  expect(userName).toBeInTheDocument();
});
```

`findBy` is essentially a combination of `getBy` and `waitFor`.

#### Summary Table

| Query Type | No Element Found      | Asynchronous | Use Case                                    |
| ---------- | --------------------- | ------------ | ------------------------------------------- |
| **`getBy`**  | Throws an error       | No           | Asserting an element **is** present.        |
| **`queryBy`**| Returns `null`        | No           | Asserting an element **is not** present.    |
| **`findBy`** | Rejects the promise   | **Yes**      | Asserting an element appears **asynchronously**. |

Choosing the right query type makes your tests more readable and robust.

---

### Q69: What is the difference between `fireEvent` and `user-event` in React Testing Library?

**Answer:**

Both `fireEvent` and `user-event` are libraries used to simulate events in React Testing Library, but they operate at different levels of abstraction. The `user-event` library is generally recommended because it simulates user interactions more realistically than `fireEvent`.

#### `fireEvent`

`fireEvent` dispatches DOM events directly. When you call `fireEvent.click(button)`, it dispatches a single `click` event to that button. This is a low-level implementation that doesn't always capture the full scope of a user's action.

For example, `fireEvent.change(input, { target: { value: 'hello' } })` only dispatches a single `change` event. A real user typing into an input would also trigger `keyDown`, `keyUp`, and `input` events for each character.

**Key Characteristics of `fireEvent`**:
*   **Low-Level**: Dispatches only the specified DOM event.
*   **Implementation-Focused**: Tests how the component responds to a specific event.
*   **Less Realistic**: Does not mimic the full sequence of events a user would trigger.

#### `user-event`

`user-event` is a companion library that simulates the full sequence of events that happen when a user interacts with the page. It's built on top of `fireEvent` but provides a higher-level, more user-centric API.

For example, `await userEvent.type(input, 'hello')` will dispatch `keyDown`, `keyPress`, `keyUp`, `input`, and `change` events for each character, just as if a real user were typing. Similarly, `await userEvent.click(button)` will trigger `focus`, `hover`, `mousedown`, `mouseup`, and `click` events.

**Key Characteristics of `user-event`**:
*   **High-Level**: Simulates the full interaction, including multiple related events.
*   **User-Focused**: Tests how the component behaves from a user's perspective.
*   **More Realistic**: Leads to more robust tests that are less likely to break with implementation changes.
*   **Asynchronous**: Most `user-event` APIs return a promise, so you should always use `await`.

#### Comparison and Example

Let's compare typing into an input field.

**Component:**

```jsx
import React, { useState } from 'react';

function TextInput() {
  const [value, setValue] = useState('');

  return (
    <input
      type="text"
      value={value}
      onChange={(e) => setValue(e.target.value)}
      placeholder="Enter text"
    />
  );
}
```

**Test with `fireEvent`:**

```javascript
import { render, screen, fireEvent } from '@testing-library/react';

// ...

test('updates on change with fireEvent', () => {
  render(<TextInput />);
  const input = screen.getByPlaceholderText('Enter text');

  fireEvent.change(input, { target: { value: 'Hello' } });

  expect(input.value).toBe('Hello');
});
```

**Test with `user-event`:**

```javascript
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';

// ...

test('updates on type with user-event', async () => {
  render(<TextInput />);
  const input = screen.getByPlaceholderText('Enter text');

  await userEvent.type(input, 'Hello');

  expect(input.value).toBe('Hello');
});
```

#### Recommendation

**Always prefer `user-event` over `fireEvent`**. It makes your tests more aligned with how users actually interact with your application. This leads to higher confidence in your tests and makes them less brittle, as they are less coupled to the specific DOM events being fired.

---

### Q70: What is the `act()` function in React Testing Library, and when should you use it?

**Answer:**

The `act()` function, provided by `react-dom/test-utils`, ensures that all updates related to a component (like state changes, effects, and re-renders) are processed and applied to the DOM before you make any assertions in your tests.

#### Why is `act()` Necessary?

React's rendering process is asynchronous. When you update a component's state, React doesn't immediately update the DOM. Instead, it batches updates and processes them in a separate, non-blocking step.

In a test environment, this can lead to problems. If you update state and immediately try to assert something about the resulting DOM, the update might not have happened yet, causing your test to fail incorrectly.

`act()` solves this by creating an execution scope for your test. Any React updates triggered inside an `act()` call are guaranteed to be flushed before `act()` exits.

#### Do You Need to Use `act()` with React Testing Library?

**Usually, no.**

React Testing Library's APIs, such as `render`, `fireEvent`, and `user-event`, are already wrapped in `act()` internally. This is a major reason why RTL is so popular—it handles this complexity for you.

When you use these APIs, you can be confident that the component has finished re-rendering before the next line of your test runs.

```javascript
// No `act()` needed here because `fireEvent` and `user-event` are wrapped in it.

test('should increment counter', async () => {
  render(<Counter />);
  
  // fireEvent is wrapped in act()
  fireEvent.click(screen.getByText('+'));
  expect(screen.getByText('1')).toBeInTheDocument();

  // user-event is also wrapped in act()
  await userEvent.click(screen.getByText('+'));
  expect(screen.getByText('2')).toBeInTheDocument();
});
```

#### When *Should* You Use `act()`?

You only need to manually use `act()` when you trigger a state update that is **not** caused by a user interaction simulated by RTL. This is rare but can happen in specific scenarios, such as:

1.  **Testing custom hooks directly**: When testing a custom hook, you might call a function returned by the hook that updates state. Since this isn't a DOM event, you need to wrap it in `act()`.
2.  **Mocked asynchronous calls**: If you have a mocked function (e.g., a WebSocket `onmessage` handler) that triggers a state update, you must wrap that state update in `act()`.

**Example: Testing a Custom Hook**

Let's say you have a `useCounter` hook:

```javascript
// useCounter.js
import { useState, useCallback } from 'react';

export function useCounter() {
  const [count, setCount] = useState(0);
  const increment = useCallback(() => setCount((c) => c + 1), []);
  return { count, increment };
}
```

When testing it with `@testing-library/react-hooks` (or `@testing-library/react` for React 18+), you need `act()`:

```javascript
import { renderHook, act } from '@testing-library/react';
import { useCounter } from './useCounter';

test('should increment the counter', () => {
  const { result } = renderHook(() => useCounter());

  // The state update is not caused by a DOM event, so we need act()
  act(() => {
    result.current.increment();
  });

  expect(result.current.count).toBe(1);
});
```

#### The `act` Warning

If you see this warning in your test console:

> `Warning: An update to MyComponent was not wrapped in act(...).`

It's a clear sign that a state update happened somewhere in your test without being wrapped in `act()`. The most common cause is an asynchronous operation (like a `fetch` call in a `useEffect`) that resolves and updates state *after* your test has already finished its assertions. To fix this, you typically need to use `findBy` queries and `await` the appearance of the resulting UI change.

  );
  
  return posts;
});

// Parallel data fetching
export async function getUserDashboardData(userId) {
  const [user, posts, analytics] = await Promise.all([
    getUser(userId),
    getUserPosts(userId, 5),
    getUserAnalytics(userId)
  ]);
  
  return { user, posts, analytics };
}
```

**Best Practices:**

1. **Server vs Client Components**: Use Server Components by default, Client Components only when needed for interactivity
2. **Data Fetching**: Fetch data as close to where it's needed as possible
3. **Caching**: Use React's `cache` function to deduplicate requests
4. **Streaming**: Use Suspense boundaries to stream content progressively
5. **Error Handling**: Implement proper error boundaries and not-found pages
6. **Performance**: Optimize bundle size by keeping client components minimal
7. **SEO**: Leverage server-side rendering for better search engine optimization
8. **Security**: Never expose sensitive data in Client Components

React Server Components represent the future of React development, enabling better performance, SEO, and developer experience while maintaining the component-based architecture that makes React powerful.

**3. Server Actions for Form Handling:**

```jsx
// lib/actions.js (Server Actions)
'use server';

import { db } from './database';
import { revalidatePath } from 'next/cache';
import { redirect } from 'next/navigation';

export async function createPost(formData) {
  const title = formData.get('title');
  const content = formData.get('content');
  const userId = formData.get('userId');
  
  // Validation
  if (!title || !content) {
    return { error: 'Title and content are required' };
  }
  
  try {
    const result = await db.query(
      'INSERT INTO posts (title, content, user_id, created_at) VALUES (?, ?, ?, NOW())',
      [title, content, userId]
    );
    
    // Revalidate the posts page to show new post
    revalidatePath('/posts');
    
    // Redirect to the new post
    redirect(`/posts/${result.insertId}`);
  } catch (error) {
    console.error('Failed to create post:', error);
    return { error: 'Failed to create post' };
  }
}

export async function updatePost(postId, formData) {
  const title = formData.get('title');
  const content = formData.get('content');
  
  try {
    await db.query(
      'UPDATE posts SET title = ?, content = ?, updated_at = NOW() WHERE id = ?',
      [title, content, postId]
    );
    
    revalidatePath(`/posts/${postId}`);
    return { success: true };
  } catch (error) {
    return { error: 'Failed to update post' };
  }
}
```

**Best Practices:**

1. **Server vs Client Components**: Use Server Components by default, Client Components only when needed for interactivity
2. **Data Fetching**: Fetch data as close to where it's needed as possible
3. **Caching**: Use React's `cache` function to deduplicate requests
4. **Streaming**: Use Suspense boundaries to stream content progressively
5. **Error Handling**: Implement proper error boundaries and not-found pages
6. **Performance**: Optimize bundle size by keeping client components minimal
7. **SEO**: Leverage server-side rendering for better search engine optimization
8. **Security**: Never expose sensitive data in Client Components

React Server Components represent the future of React development, enabling better performance, SEO, and developer experience while maintaining the component-based architecture that makes React powerful. from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <h2>Counter: {count}</h2>
      <button onClick={() => setCount(count + 1)}>
        Increment
      </button>
      <button onClick={() => setCount(count - 1)}>
        Decrement
      </button>
    </div>
  );
}

export default Counter;
```

**Benefits:**
- **Reusability**: Components can be reused across different parts of the application
- **Maintainability**: Clear separation of concerns and modular structure
- **Performance**: Virtual DOM and efficient reconciliation algorithm
- **Developer Experience**: Rich ecosystem, excellent tooling, and strong community support
- **SEO-Friendly**: Server-side rendering capabilities with Next.js

---

### Q2: Explain the difference between functional and class components.
**Difficulty: Medium**

**Answer:**
React components can be written as either functional components or class components, each with their own characteristics and use cases.

**Functional Components:**
Functional components are JavaScript functions that return JSX. With the introduction of Hooks in React 16.8, they can now manage state and lifecycle methods.

```jsx
// Functional Component with Hooks
import React, { useState, useEffect } from 'react';

function UserProfile({ userId }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchUser() {
      try {
        const response = await fetch(`/api/users/${userId}`);
        const userData = await response.json();
        setUser(userData);
      } catch (error) {
        console.error('Error fetching user:', error);
      } finally {
        setLoading(false);
      }
    }

    fetchUser();
  }, [userId]);

  if (loading) return <div>Loading...</div>;
  if (!user) return <div>User not found</div>;

  return (
    <div className="user-profile">
      <h2>{user.name}</h2>
      <p>Email: {user.email}</p>
      <p>Role: {user.role}</p>
    </div>
  );
}

export default UserProfile;
```

**Class Components:**
Class components are ES6 classes that extend React.Component and must have a render method.

```jsx
// Class Component
import React, { Component } from 'react';

class UserProfile extends Component {
  constructor(props) {
    super(props);
    this.state = {
      user: null,
      loading: true
    };
  }

  async componentDidMount() {
    try {
      const response = await fetch(`/api/users/${this.props.userId}`);
      const userData = await response.json();
      this.setState({ user: userData, loading: false });
    } catch (error) {
      console.error('Error fetching user:', error);
      this.setState({ loading: false });
    }
  }

  async componentDidUpdate(prevProps) {
    if (prevProps.userId !== this.props.userId) {
      this.setState({ loading: true });
      try {
        const response = await fetch(`/api/users/${this.props.userId}`);
        const userData = await response.json();
        this.setState({ user: userData, loading: false });
      } catch (error) {
        console.error('Error fetching user:', error);
        this.setState({ loading: false });
      }
    }
  }

  render() {
    const { user, loading } = this.state;

    if (loading) return <div>Loading...</div>;
    if (!user) return <div>User not found</div>;

    return (
      <div className="user-profile">
        <h2>{user.name}</h2>
        <p>Email: {user.email}</p>
        <p>Role: {user.role}</p>
      </div>
    );
  }
}

export default UserProfile;
```

**Key Differences:**

| Aspect | Functional Components | Class Components |
|--------|----------------------|------------------|
| **Syntax** | Function declaration | ES6 Class |
| **State Management** | useState Hook | this.state |
| **Lifecycle Methods** | useEffect Hook | componentDidMount, etc. |
| **Performance** | Generally better (less overhead) | Slightly more overhead |
| **Code Length** | More concise | More verbose |
| **Learning Curve** | Easier for beginners | Requires understanding of classes |
| **Modern Preference** | Recommended approach | Legacy approach |

**When to Use:**
- **Functional Components**: Preferred for new development, simpler syntax, better performance
- **Class Components**: Legacy codebases, when you need error boundaries (though functional error boundaries are coming)

---

### Q3: What is JSX and how does it work?
**Difficulty: Easy**

**Answer:**
JSX (JavaScript XML) is a syntax extension for JavaScript that allows you to write HTML-like code within JavaScript. It makes React components more readable and easier to write.

**How JSX Works:**
JSX is not valid JavaScript by itself. It gets transpiled by tools like Babel into regular JavaScript function calls.

```jsx
// JSX Code
const element = (
  <div className="greeting">
    <h1>Hello, {name}!</h1>
    <p>Welcome to our application.</p>
  </div>
);

// Transpiled JavaScript (what Babel produces)
const element = React.createElement(
  'div',
  { className: 'greeting' },
  React.createElement('h1', null, 'Hello, ', name, '!'),
  React.createElement('p', null, 'Welcome to our application.')
);
```

**JSX Rules and Best Practices:**

1. **Single Parent Element**: JSX expressions must have one parent element
```jsx
// ❌ Invalid - Multiple parent elements
return (
  <h1>Title</h1>
  <p>Content</p>
);

// ✅ Valid - Single parent element
return (
  <div>
    <h1>Title</h1>
    <p>Content</p>
  </div>
);

// ✅ Valid - React Fragment
return (
  <>
    <h1>Title</h1>
    <p>Content</p>
  </>
);
```

2. **JavaScript Expressions**: Use curly braces for JavaScript expressions
```jsx
function WelcomeMessage({ user, isLoggedIn }) {
  const currentTime = new Date().toLocaleTimeString();
  
  return (
    <div>
      {isLoggedIn ? (
        <h1>Welcome back, {user.name}!</h1>
      ) : (
        <h1>Please log in</h1>
      )}
      <p>Current time: {currentTime}</p>
      <p>You have {user.notifications?.length || 0} notifications</p>
    </div>
  );
}
```

3. **Attribute Naming**: Use camelCase for attributes
```jsx
// ❌ HTML attributes
<div class="container" onclick="handleClick()">

// ✅ JSX attributes
<div className="container" onClick={handleClick}>
```

4. **Self-Closing Tags**: All tags must be properly closed
```jsx
// ❌ Invalid
<img src="image.jpg">
<input type="text">

// ✅ Valid
<img src="image.jpg" />
<input type="text" />
```

**Advanced JSX Patterns:**

```jsx
function ProductList({ products, onProductSelect }) {
  return (
    <div className="product-list">
      {products.length > 0 ? (
        products.map(product => (
          <div 
            key={product.id} 
            className={`product-item ${product.featured ? 'featured' : ''}`}
            onClick={() => onProductSelect(product)}
          >
            <img 
              src={product.image} 
              alt={product.name}
              loading="lazy"
            />
            <h3>{product.name}</h3>
            <p className="price">${product.price.toFixed(2)}</p>
            {product.discount && (
              <span className="discount">-{product.discount}%</span>
            )}
          </div>
        ))
      ) : (
        <div className="empty-state">
          <p>No products available</p>
        </div>
      )}
    </div>
  );
}
```

**Benefits of JSX:**
- **Familiar Syntax**: HTML-like syntax is familiar to web developers
- **Type Safety**: When used with TypeScript, provides compile-time type checking
- **Developer Experience**: Better IDE support with syntax highlighting and autocomplete
- **Expressiveness**: Allows embedding JavaScript expressions seamlessly

---

## Components and JSX

### Q4: How do you pass data between components?
**Difficulty: Medium**

**Answer:**
React provides several ways to pass data between components, each suitable for different scenarios.

**1. Props (Parent to Child)**
Props are the primary way to pass data from parent to child components.

```jsx
// Parent Component
function App() {
  const user = {
    id: 1,
    name: 'John Doe',
    email: 'john@example.com',
    avatar: '/avatars/john.jpg'
  };

  const handleUserUpdate = (updatedUser) => {
    console.log('User updated:', updatedUser);
    // Update user in state or send to API
  };

  return (
    <div>
      <Header title="User Dashboard" />
      <UserProfile 
        user={user}
        onUserUpdate={handleUserUpdate}
        isEditable={true}
      />
    </div>
  );
}

// Child Component
function UserProfile({ user, onUserUpdate, isEditable }) {
  const [isEditing, setIsEditing] = useState(false);
  const [formData, setFormData] = useState(user);

  const handleSubmit = (e) => {
    e.preventDefault();
    onUserUpdate(formData);
    setIsEditing(false);
  };

  return (
    <div className="user-profile">
      <img src={user.avatar} alt={user.name} />
      {isEditing ? (
        <form onSubmit={handleSubmit}>
          <input
            value={formData.name}
            onChange={(e) => setFormData({...formData, name: e.target.value})}
          />
          <input
            value={formData.email}
            onChange={(e) => setFormData({...formData, email: e.target.value})}
          />
          <button type="submit">Save</button>
          <button type="button" onClick={() => setIsEditing(false)}>Cancel</button>
        </form>
      ) : (
        <div>
          <h2>{user.name}</h2>
          <p>{user.email}</p>
          {isEditable && (
            <button onClick={() => setIsEditing(true)}>Edit</button>
          )}
        </div>
      )}
    </div>
  );
}
```

**2. Callback Functions (Child to Parent)**
Pass functions as props to allow child components to communicate back to parents.

```jsx
// Parent Component
function TodoApp() {
  const [todos, setTodos] = useState([]);

  const addTodo = (text) => {
    const newTodo = {
      id: Date.now(),
      text,
      completed: false,
      createdAt: new Date()
    };
    setTodos([...todos, newTodo]);
  };

  const toggleTodo = (id) => {
    setTodos(todos.map(todo => 
      todo.id === id ? { ...todo, completed: !todo.completed } : todo
    ));
  };

  const deleteTodo = (id) => {
    setTodos(todos.filter(todo => todo.id !== id));
  };

  return (
    <div>
      <TodoForm onAddTodo={addTodo} />
      <TodoList 
        todos={todos}
        onToggleTodo={toggleTodo}
        onDeleteTodo={deleteTodo}
      />
    </div>
  );
}

// Child Components
function TodoForm({ onAddTodo }) {
  const [text, setText] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (text.trim()) {
      onAddTodo(text.trim());
      setText('');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Add a new todo..."
      />
      <button type="submit">Add Todo</button>
    </form>
  );
}

function TodoList({ todos, onToggleTodo, onDeleteTodo }) {
  return (
    <ul>
      {todos.map(todo => (
        <TodoItem
          key={todo.id}
          todo={todo}
          onToggle={() => onToggleTodo(todo.id)}
          onDelete={() => onDeleteTodo(todo.id)}
        />
      ))}
    </ul>
  );
}
```

**3. Context API (Global State)**
For data that needs to be accessed by many components at different nesting levels.

```jsx
// Create Context
const ThemeContext = createContext();
const UserContext = createContext();

// Context Provider
function AppProvider({ children }) {
  const [theme, setTheme] = useState('light');
  const [user, setUser] = useState(null);

  const toggleTheme = () => {
    setTheme(prev => prev === 'light' ? 'dark' : 'light');
  };

  const login = async (credentials) => {
    try {
      const response = await fetch('/api/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(credentials)
      });
      const userData = await response.json();
      setUser(userData);
    } catch (error) {
      console.error('Login failed:', error);
    }
  };

  const logout = () => {
    setUser(null);
    localStorage.removeItem('token');
  };

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      <UserContext.Provider value={{ user, login, logout }}>
        {children}
      </UserContext.Provider>
    </ThemeContext.Provider>
  );
}

// Custom Hooks for Context
function useTheme() {
  const context = useContext(ThemeContext);
  if (!context) {
    throw new Error('useTheme must be used within AppProvider');
  }
  return context;
}

function useUser() {
  const context = useContext(UserContext);
  if (!context) {
    throw new Error('useUser must be used within AppProvider');
  }
  return context;
}

// Using Context in Components
function Header() {
  const { theme, toggleTheme } = useTheme();
  const { user, logout } = useUser();

  return (
    <header className={`header ${theme}`}>
      <h1>My App</h1>
      <div>
        <button onClick={toggleTheme}>
          Switch to {theme === 'light' ? 'dark' : 'light'} mode
        </button>
        {user ? (
          <div>
            <span>Welcome, {user.name}</span>
            <button onClick={logout}>Logout</button>
          </div>
        ) : (
          <LoginButton />
        )}
      </div>
    </header>
  );
}
```

**4. State Management Libraries**
For complex applications, consider using Redux, Zustand, or Jotai.

```jsx
// Using Zustand for state management
import { create } from 'zustand';

const useStore = create((set, get) => ({
  // State
  user: null,
  todos: [],
  loading: false,
  
  // Actions
  setUser: (user) => set({ user }),
  addTodo: (text) => set((state) => ({
    todos: [...state.todos, {
      id: Date.now(),
      text,
      completed: false
    }]
  })),
  toggleTodo: (id) => set((state) => ({
    todos: state.todos.map(todo =>
      todo.id === id ? { ...todo, completed: !todo.completed } : todo
    )
  })),
  fetchTodos: async () => {
    set({ loading: true });
    try {
      const response = await fetch('/api/todos');
      const todos = await response.json();
      set({ todos, loading: false });
    } catch (error) {
      console.error('Failed to fetch todos:', error);
      set({ loading: false });
    }
  }
}));

// Using the store in components
function TodoComponent() {
  const { todos, addTodo, toggleTodo, fetchTodos, loading } = useStore();
  
  useEffect(() => {
    fetchTodos();
  }, [fetchTodos]);

  if (loading) return <div>Loading...</div>;

  return (
    <div>
      {todos.map(todo => (
        <div key={todo.id}>
          <input
            type="checkbox"
            checked={todo.completed}
            onChange={() => toggleTodo(todo.id)}
          />
          <span>{todo.text}</span>
        </div>
      ))}
    </div>
  );
}
```

**Best Practices:**
- Use props for direct parent-child communication
- Use callback functions for child-to-parent communication
- Use Context for global state that many components need
- Consider state management libraries for complex applications
- Keep state as close to where it's needed as possible
- Avoid prop drilling by using Context or state management libraries

---

## State Management

### Q5: Explain useState and how to manage state in functional components.
**Difficulty: Medium**

**Answer:**
The `useState` hook is the primary way to manage state in functional components. It allows you to add state variables to functional components and provides a way to update them.

**Basic useState Syntax:**
```jsx
const [state, setState] = useState(initialValue);
```

**Simple State Management:**
```jsx
import React, { useState } from 'react';

function Counter() {
  // Simple state with primitive value
  const [count, setCount] = useState(0);
  const [name, setName] = useState('');
  const [isVisible, setIsVisible] = useState(true);

  return (
    <div>
      <h2>Count: {count}</h2>
      <button onClick={() => setCount(count + 1)}>Increment</button>
      <button onClick={() => setCount(count - 1)}>Decrement</button>
      <button onClick={() => setCount(0)}>Reset</button>
      
      <input
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Enter your name"
      />
      
      <button onClick={() => setIsVisible(!isVisible)}>
        {isVisible ? 'Hide' : 'Show'} Content
      </button>
      
      {isVisible && <p>Hello, {name || 'Anonymous'}!</p>}
    </div>
  );
}
```

**Complex State Management:**
```jsx
function UserForm() {
  // Object state
  const [user, setUser] = useState({
    firstName: '',
    lastName: '',
    email: '',
    age: '',
    preferences: {
      newsletter: false,
      notifications: true
    }
  });

  // Array state
  const [hobbies, setHobbies] = useState([]);
  const [errors, setErrors] = useState({});

  // Update object state - always create new object
  const updateUser = (field, value) => {
    setUser(prevUser => ({
      ...prevUser,
      [field]: value
    }));
  };

  // Update nested object state
  const updatePreference = (preference, value) => {
    setUser(prevUser => ({
      ...prevUser,
      preferences: {
        ...prevUser.preferences,
        [preference]: value
      }
    }));
  };

  // Add to array
  const addHobby = (hobby) => {
    if (hobby && !hobbies.includes(hobby)) {
      setHobbies(prevHobbies => [...prevHobbies, hobby]);
    }
  };

  // Remove from array
  const removeHobby = (hobbyToRemove) => {
    setHobbies(prevHobbies => 
      prevHobbies.filter(hobby => hobby !== hobbyToRemove)
    );
  };

  // Form validation
  const validateForm = () => {
    const newErrors = {};
    
    if (!user.firstName.trim()) {
      newErrors.firstName = 'First name is required';
    }
    
    if (!user.email.trim()) {
      newErrors.email = 'Email is required';
    } else if (!/\S+@\S+\.\S+/.test(user.email)) {
      newErrors.email = 'Email is invalid';
    }
    
    if (!user.age || user.age < 18) {
      newErrors.age = 'Must be 18 or older';
    }
    
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (validateForm()) {
      console.log('Form submitted:', { user, hobbies });
      // Reset form
      setUser({
        firstName: '',
        lastName: '',
        email: '',
        age: '',
        preferences: {
          newsletter: false,
          notifications: true
        }
      });
      setHobbies([]);
      setErrors({});
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <input
          value={user.firstName}
          onChange={(e) => updateUser('firstName', e.target.value)}
          placeholder="First Name"
        />
        {errors.firstName && <span className="error">{errors.firstName}</span>}
      </div>
      
      <div>
        <input
          value={user.lastName}
          onChange={(e) => updateUser('lastName', e.target.value)}
          placeholder="Last Name"
        />
      </div>
      
      <div>
        <input
          type="email"
          value={user.email}
          onChange={(e) => updateUser('email', e.target.value)}
          placeholder="Email"
        />
        {errors.email && <span className="error">{errors.email}</span>}
      </div>
      
      <div>
        <input
          type="number"
          value={user.age}
          onChange={(e) => updateUser('age', parseInt(e.target.value))}
          placeholder="Age"
        />
        {errors.age && <span className="error">{errors.age}</span>}
      </div>
      
      <div>
        <label>
          <input
            type="checkbox"
            checked={user.preferences.newsletter}
            onChange={(e) => updatePreference('newsletter', e.target.checked)}
          />
          Subscribe to newsletter
        </label>
      </div>
      
      <div>
        <label>
          <input
            type="checkbox"
            checked={user.preferences.notifications}
            onChange={(e) => updatePreference('notifications', e.target.checked)}
          />
          Enable notifications
        </label>
      </div>
      
      <div>
        <h3>Hobbies:</h3>
        {hobbies.map(hobby => (
          <span key={hobby} className="hobby-tag">
            {hobby}
            <button type="button" onClick={() => removeHobby(hobby)}>×</button>
          </span>
        ))}
        <input
          type="text"
          placeholder="Add hobby"
          onKeyPress={(e) => {
            if (e.key === 'Enter') {
              e.preventDefault();
              addHobby(e.target.value);
              e.target.value = '';
            }
          }}
        />
      </div>
      
      <button type="submit">Submit</button>
    </form>
  );
}
```

**Advanced State Patterns:**

1. **Functional Updates:**
```jsx
function TodoList() {
  const [todos, setTodos] = useState([]);
  
  // When new state depends on previous state, use functional update
  const addTodo = (text) => {
    setTodos(prevTodos => [
      ...prevTodos,
      {
        id: Date.now(),
        text,
        completed: false,
        createdAt: new Date()
      }
    ]);
  };
  
  const toggleTodo = (id) => {
    setTodos(prevTodos =>
      prevTodos.map(todo =>
        todo.id === id
          ? { ...todo, completed: !todo.completed }
          : todo
      )
    );
  };
  
  const deleteTodo = (id) => {
    setTodos(prevTodos => prevTodos.filter(todo => todo.id !== id));
  };
  
  // Batch multiple state updates
  const clearCompleted = () => {
    setTodos(prevTodos => prevTodos.filter(todo => !todo.completed));
  };
  
  return (
    <div>
      {/* Component JSX */}
    </div>
  );
}
```

2. **Lazy Initial State:**
```jsx
function ExpensiveComponent() {
  // Expensive computation only runs once
  const [data, setData] = useState(() => {
    console.log('Computing initial state...');
    return processLargeDataSet();
  });
  
  // Alternative: using useEffect for async initialization
  const [asyncData, setAsyncData] = useState(null);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    async function loadData() {
      try {
        const result = await fetchDataFromAPI();
        setAsyncData(result);
      } catch (error) {
        console.error('Failed to load data:', error);
      } finally {
        setLoading(false);
      }
    }
    
    loadData();
  }, []);
  
  if (loading) return <div>Loading...</div>;
  
  return (
    <div>
      {/* Render data */}
    </div>
  );
}
```

3. **Custom Hooks for State Logic:**
```jsx
// Custom hook for form handling
function useForm(initialValues, validationRules) {
  const [values, setValues] = useState(initialValues);
  const [errors, setErrors] = useState({});
  const [touched, setTouched] = useState({});
  
  const setValue = (name, value) => {
    setValues(prev => ({ ...prev, [name]: value }));
    
    // Clear error when user starts typing
    if (errors[name]) {
      setErrors(prev => ({ ...prev, [name]: '' }));
    }
  };
  
  const setTouched = (name) => {
    setTouched(prev => ({ ...prev, [name]: true }));
  };
  
  const validate = () => {
    const newErrors = {};
    
    Object.keys(validationRules).forEach(field => {
      const rule = validationRules[field];
      const value = values[field];
      
      if (rule.required && !value) {
        newErrors[field] = `${field} is required`;
      } else if (rule.pattern && !rule.pattern.test(value)) {
        newErrors[field] = rule.message;
      }
    });
    
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };
  
  const reset = () => {
    setValues(initialValues);
    setErrors({});
    setTouched({});
  };
  
  return {
    values,
    errors,
    touched,
    setValue,
    setTouched,
    validate,
    reset
  };
}

// Using the custom hook
function LoginForm() {
  const {
    values,
    errors,
    touched,
    setValue,
    setTouched,
    validate,
    reset
  } = useForm(
    { email: '', password: '' },
    {
      email: {
        required: true,
        pattern: /\S+@\S+\.\S+/,
        message: 'Please enter a valid email'
      },
      password: {
        required: true,
        pattern: /.{6,}/,
        message: 'Password must be at least 6 characters'
      }
    }
  );
  
  const handleSubmit = (e) => {
    e.preventDefault();
    if (validate()) {
      console.log('Login:', values);
      reset();
    }
  };
  
  return (
    <form onSubmit={handleSubmit}>
      <input
        type="email"
        value={values.email}
        onChange={(e) => setValue('email', e.target.value)}
        onBlur={() => setTouched('email')}
        placeholder="Email"
      />
      {touched.email && errors.email && (
        <span className="error">{errors.email}</span>
      )}
      
      <input
        type="password"
        value={values.password}
        onChange={(e) => setValue('password', e.target.value)}
        onBlur={() => setTouched('password')}
        placeholder="Password"
      />
      {touched.password && errors.password && (
        <span className="error">{errors.password}</span>
      )}
      
      <button type="submit">Login</button>
    </form>
  );
}
```

**Best Practices:**
- Always use functional updates when new state depends on previous state
- Don't mutate state directly - always create new objects/arrays
- Use lazy initial state for expensive computations
- Consider custom hooks for reusable state logic
- Keep state as local as possible
- Use multiple useState calls for unrelated state variables
- Validate and sanitize user input
- Handle loading and error states appropriately

---

## Hooks

### Q6: Explain useEffect and its use cases.
**Difficulty: Medium**

**Answer:**
The `useEffect` hook allows you to perform side effects in functional components. It serves the same purpose as `componentDidMount`, `componentDidUpdate`, and `componentWillUnmount` combined in class components.

**Basic useEffect Syntax:**
```jsx
useEffect(() => {
  // Side effect code
  return () => {
    // Cleanup code (optional)
  };
}, [dependencies]); // Dependencies array (optional)
```

**1. Component Mount (componentDidMount equivalent):**
```jsx
import React, { useState, useEffect } from 'react';

function UserProfile({ userId }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Runs once after component mounts
  useEffect(() => {
    async function fetchUser() {
      try {
        setLoading(true);
        setError(null);
        
        const response = await fetch(`/api/users/${userId}`);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const userData = await response.json();
        setUser(userData);
      } catch (err) {
        setError(err.message);
        console.error('Error fetching user:', err);
      } finally {
        setLoading(false);
      }
    }

    fetchUser();
  }, []); // Empty dependency array = run once on mount

  if (loading) return <div className="loading">Loading user...</div>;
  if (error) return <div className="error">Error: {error}</div>;
  if (!user) return <div>User not found</div>;

  return (
    <div className="user-profile">
      <img src={user.avatar} alt={user.name} />
      <h2>{user.name}</h2>
      <p>{user.email}</p>
      <p>Joined: {new Date(user.joinDate).toLocaleDateString()}</p>
    </div>
  );
}
```

**2. Dependency-based Updates (componentDidUpdate equivalent):**
```jsx
function SearchResults({ query, filters }) {
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [page, setPage] = useState(1);

  // Runs when query or filters change
  useEffect(() => {
    if (!query.trim()) {
      setResults([]);
      return;
    }

    async function searchProducts() {
      setLoading(true);
      try {
        const params = new URLSearchParams({
          q: query,
          page: 1,
          ...filters
        });
        
        const response = await fetch(`/api/search?${params}`);
        const data = await response.json();
        
        setResults(data.results);
        setPage(1);
      } catch (error) {
        console.error('Search failed:', error);
        setResults([]);
      } finally {
        setLoading(false);
      }
    }

    // Debounce search to avoid too many API calls
    const timeoutId = setTimeout(searchProducts, 300);
    
    return () => clearTimeout(timeoutId);
  }, [query, filters]); // Runs when query or filters change

  // Load more results when page changes
  useEffect(() => {
    if (page === 1) return; // Skip first page (already loaded)

    async function loadMoreResults() {
      setLoading(true);
      try {
        const params = new URLSearchParams({
          q: query,
          page,
          ...filters
        });
        
        const response = await fetch(`/api/search?${params}`);
        const data = await response.json();
        
        setResults(prev => [...prev, ...data.results]);
      } catch (error) {
        console.error('Failed to load more results:', error);
      } finally {
        setLoading(false);
      }
    }

    loadMoreResults();
  }, [page, query, filters]);

  return (
    <div>
      {loading && <div>Searching...</div>}
      <div className="results">
        {results.map(product => (
          <ProductCard key={product.id} product={product} />
        ))}
      </div>
      {results.length > 0 && (
        <button onClick={() => setPage(prev => prev + 1)}>
          Load More
        </button>
      )}
    </div>
  );
}
```

**3. Cleanup (componentWillUnmount equivalent):**
```jsx
function Timer() {
  const [seconds, setSeconds] = useState(0);
  const [isRunning, setIsRunning] = useState(false);

  useEffect(() => {
    let intervalId;

    if (isRunning) {
      intervalId = setInterval(() => {
        setSeconds(prev => prev + 1);
      }, 1000);
    }

    // Cleanup function - runs when component unmounts or dependencies change
    return () => {
      if (intervalId) {
        clearInterval(intervalId);
      }
    };
  }, [isRunning]); // Runs when isRunning changes

  return (
    <div>
      <h2>Timer: {seconds}s</h2>
      <button onClick={() => setIsRunning(!isRunning)}>
        {isRunning ? 'Pause' : 'Start'}
      </button>
      <button onClick={() => {
        setSeconds(0);
        setIsRunning(false);
      }}>
        Reset
      </button>
    </div>
  );
}
```

**4. Event Listeners and DOM Manipulation:**
```jsx
function WindowSize() {
  const [windowSize, setWindowSize] = useState({
    width: window.innerWidth,
    height: window.innerHeight
  });

  useEffect(() => {
    function handleResize() {
      setWindowSize({
        width: window.innerWidth,
        height: window.innerHeight
      });
    }

    // Add event listener
    window.addEventListener('resize', handleResize);

    // Cleanup: remove event listener
    return () => {
      window.removeEventListener('resize', handleResize);
    };
  }, []); // Empty dependency array = setup once, cleanup on unmount

  return (
    <div>
      <p>Window size: {windowSize.width} x {windowSize.height}</p>
    </div>
  );
}

function ScrollToTop() {
  const [showButton, setShowButton] = useState(false);

  useEffect(() => {
    function handleScroll() {
      setShowButton(window.pageYOffset > 300);
    }

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const scrollToTop = () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  };

  return (
    showButton && (
      <button 
        className="scroll-to-top"
        onClick={scrollToTop}
        aria-label="Scroll to top"
      >
        ↑
      </button>
    )
  );
}
```

**5. Multiple useEffect Hooks:**
```jsx
function BlogPost({ postId }) {
  const [post, setPost] = useState(null);
  const [comments, setComments] = useState([]);
  const [relatedPosts, setRelatedPosts] = useState([]);
  const [loading, setLoading] = useState(true);

  // Fetch main post
  useEffect(() => {
    async function fetchPost() {
      try {
        const response = await fetch(`/api/posts/${postId}`);
        const postData = await response.json();
        setPost(postData);
      } catch (error) {
        console.error('Error fetching post:', error);
      }
    }

    fetchPost();
  }, [postId]);

  // Fetch comments
  useEffect(() => {
    async function fetchComments() {
      try {
        const response = await fetch(`/api/posts/${postId}/comments`);
        const commentsData = await response.json();
        setComments(commentsData);
      } catch (error) {
        console.error('Error fetching comments:', error);
      }
    }

    fetchComments();
  }, [postId]);

  // Fetch related posts (depends on post category)
  useEffect(() => {
    if (!post?.category) return;

    async function fetchRelatedPosts() {
      try {
        const response = await fetch(`/api/posts?category=${post.category}&exclude=${postId}`);
        const relatedData = await response.json();
        setRelatedPosts(relatedData.slice(0, 5)); // Limit to 5 related posts
      } catch (error) {
        console.error('Error fetching related posts:', error);
      }
    }

    fetchRelatedPosts();
  }, [post?.category, postId]);

  // Update document title
  useEffect(() => {
    if (post) {
      document.title = `${post.title} - My Blog`;
    }

    // Cleanup: reset title when component unmounts
    return () => {
      document.title = 'My Blog';
    };
  }, [post?.title]);

  // Track page view analytics
  useEffect(() => {
    if (post) {
      // Analytics tracking
      analytics.track('Page View', {
        page: 'Blog Post',
        postId: post.id,
        title: post.title,
        category: post.category
      });
    }
  }, [post]);

  if (loading && !post) {
    return <div>Loading...</div>;
  }

  return (
    <article>
      <h1>{post.title}</h1>
      <div dangerouslySetInnerHTML={{ __html: post.content }} />
      
      <section>
        <h3>Comments ({comments.length})</h3>
        {comments.map(comment => (
          <div key={comment.id}>
            <strong>{comment.author}</strong>
            <p>{comment.content}</p>
          </div>
        ))}
      </section>
      
      {relatedPosts.length > 0 && (
        <section>
          <h3>Related Posts</h3>
          {relatedPosts.map(relatedPost => (
            <a key={relatedPost.id} href={`/posts/${relatedPost.id}`}>
              {relatedPost.title}
            </a>
          ))}
        </section>
      )}
    </article>
  );
}
```

**6. Custom Hooks with useEffect:**
```jsx
// Custom hook for API calls
function useApi(url, dependencies = []) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    let cancelled = false;

    async function fetchData() {
      try {
        setLoading(true);
        setError(null);
        
        const response = await fetch(url);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const result = await response.json();
        
        if (!cancelled) {
          setData(result);
        }
      } catch (err) {
        if (!cancelled) {
          setError(err.message);
        }
      } finally {
        if (!cancelled) {
          setLoading(false);
        }
      }
    }

    fetchData();

    return () => {
      cancelled = true;
    };
  }, [url, ...dependencies]);

  return { data, loading, error };
}

// Custom hook for local storage
function useLocalStorage(key, initialValue) {
  const [storedValue, setStoredValue] = useState(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      console.error(`Error reading localStorage key "${key}":`, error);
      return initialValue;
    }
  });

  const setValue = (value) => {
    try {
      setStoredValue(value);
      window.localStorage.setItem(key, JSON.stringify(value));
    } catch (error) {
      console.error(`Error setting localStorage key "${key}":`, error);
    }
  };

  // Listen for changes in other tabs
  useEffect(() => {
    function handleStorageChange(e) {
      if (e.key === key && e.newValue !== null) {
        try {
          setStoredValue(JSON.parse(e.newValue));
        } catch (error) {
          console.error(`Error parsing localStorage key "${key}":`, error);
        }
      }
    }

    window.addEventListener('storage', handleStorageChange);
    return () => window.removeEventListener('storage', handleStorageChange);
  }, [key]);

  return [storedValue, setValue];
}

// Using custom hooks
function UserDashboard() {
  const { data: user, loading, error } = useApi('/api/user/profile');
  const [preferences, setPreferences] = useLocalStorage('userPreferences', {
    theme: 'light',
    language: 'en'
  });

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div className={`dashboard ${preferences.theme}`}>
      <h1>Welcome, {user.name}!</h1>
      <button 
        onClick={() => setPreferences({
          ...preferences,
          theme: preferences.theme === 'light' ? 'dark' : 'light'
        })}
      >
        Toggle Theme
      </button>
    </div>
  );
}
```

**Common useEffect Patterns and Best Practices:**

1. **Dependency Array Guidelines:**
   - No dependency array: runs after every render
   - Empty array `[]`: runs once after mount
   - With dependencies `[dep1, dep2]`: runs when dependencies change

2. **Cleanup is Important:**
   - Always cleanup subscriptions, timers, and event listeners
   - Prevent memory leaks and unexpected behavior

3. **Avoid Infinite Loops:**
   - Be careful with object/array dependencies
   - Use useCallback and useMemo when necessary

4. **Separate Concerns:**
   - Use multiple useEffect hooks for different concerns
   - Each effect should have a single responsibility

5. **Handle Race Conditions:**
   - Use cleanup functions to cancel ongoing requests
   - Check if component is still mounted before setting state

**Common Mistakes to Avoid:**
- Missing dependencies in the dependency array
- Not cleaning up side effects
- Putting objects/arrays directly in dependency arrays without memoization
- Using useEffect for derived state (use useMemo instead)
- Not handling loading and error states properly

---

This comprehensive guide covers the fundamental concepts of React.js with detailed explanations and practical examples. Each answer includes real-world scenarios and best practices to help developers understand not just the "how" but also the "why" behind React patterns.

### Q7: Explain React Server Components and how they differ from traditional React components.
**Difficulty: Hard**

**Answer:**
React Server Components (RSC) represent a paradigm shift in how React applications are built, allowing components to render on the server without requiring JavaScript to be sent to the client. This feature was introduced as part of React 18 and is a key part of the React architecture moving forward, especially in frameworks like Next.js 13+ and Remix.

**Key Characteristics of Server Components:**

1. **Server-Only Rendering**: Server Components execute and render entirely on the server, with only their output HTML sent to the client.

2. **Zero JavaScript Footprint**: They don't increase your client-side JavaScript bundle size because they don't get shipped to the client.

3. **Direct Backend Access**: They can directly access backend resources like databases, file systems, and internal services without API layers.

4. **Automatic Code Splitting**: They naturally split your application code between server and client.

5. **Progressive Enhancement**: They work well with traditional client components for interactive features.

**Server Components vs. Client Components:**

```jsx
// Server Component (saved as Page.server.jsx in some implementations)
// or using the 'use server' directive in Next.js
import db from '../database'; // Direct database access

async function UserProfile({ userId }) {
  // Direct database query without an API layer
  const user = await db.users.findById(userId);
  const userPosts = await db.posts.findByAuthor(userId);
  
  return (
    <div className="profile">
      <h1>{user.name}</h1>
      <ProfileDetails user={user} />
      <PostList posts={userPosts} />
    </div>
  );
}

// Client Component (saved as Counter.client.jsx in some implementations)
// or using the 'use client' directive in Next.js
'use client';

import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);
  
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}
```

**How Server Components Work:**

1. **Initial Request**: When a user visits a page, the server renders the Server Components.

2. **Streaming HTML**: The server streams HTML to the client, which can be displayed immediately.

3. **Hydration**: Any Client Components within the page are then hydrated, making them interactive.

4. **Subsequent Updates**: When data changes, only the affected components are re-rendered, not the entire page.

**Benefits of Server Components:**

1. **Improved Performance**:
   - Reduced JavaScript bundle size
   - Faster initial page load
   - Improved Time to First Byte (TTFB)
   - Better Core Web Vitals scores

2. **Enhanced Developer Experience**:
   - Simplified data fetching
   - No need for separate API endpoints
   - Automatic code splitting
   - Reduced prop drilling

3. **Better Security**:
   - Sensitive code and data stays on the server
   - API keys and secrets never exposed to the client
   - Reduced attack surface

**Implementation in Next.js 13+:**

```jsx
// app/page.js - Server Component by default
async function HomePage() {
  const products = await fetchProducts(); // Direct server-side data fetching
  
  return (
    <main>
      <h1>Welcome to our store</h1>
      <ProductGrid products={products} />
      <ClientSideCart /> {/* This is a Client Component */}
    </main>
  );
}

export default HomePage;

// app/components/client-side-cart.js
'use client'; // This directive marks it as a Client Component

import { useState } from 'react';

export default function ClientSideCart() {
  const [isOpen, setIsOpen] = useState(false);
  
  return (
    <div className="cart">
      <button onClick={() => setIsOpen(!isOpen)}>
        {isOpen ? 'Close' : 'Open'} Cart
      </button>
      {isOpen && <CartContents />}
    </div>
  );
}
```

**Patterns and Best Practices:**

1. **Component Splitting Strategy**:
   - Use Server Components for data fetching, access control, and static content
   - Use Client Components for interactive elements, state management, and event handling

2. **Data Fetching Pattern**:
```jsx
// Server Component with parallel data fetching
async function Dashboard() {
  // These requests run in parallel
  const userPromise = fetchUser();
  const postsPromise = fetchPosts();
  const analyticsPromise = fetchAnalytics();
  
  // Wait for all data to be available
  const [user, posts, analytics] = await Promise.all([
    userPromise,
    postsPromise,
    analyticsPromise
  ]);
  
  return (
    <div>
      <UserHeader user={user} />
      <PostList posts={posts} />
      <AnalyticsDashboard data={analytics} />
    </div>
  );
}
```

3. **Interleaving Server and Client Components**:
```jsx
// Server Component
async function ProductPage({ productId }) {
  const product = await fetchProduct(productId);
  
  return (
    <div>
      <h1>{product.name}</h1>
      <ProductDetails product={product} />
      {/* Client Component embedded within Server Component */}
      <AddToCartButton productId={product.id} /> 
      {/* Another Server Component */}
      <RelatedProducts categoryId={product.categoryId} />
    </div>
  );
}

// Client Component
'use client';
function AddToCartButton({ productId }) {
  const [isAdded, setIsAdded] = useState(false);
  
  const handleAddToCart = async () => {
    await addToCart(productId);
    setIsAdded(true);
  };
  
  return (
    <button 
      onClick={handleAddToCart}
      disabled={isAdded}
    >
      {isAdded ? 'Added to Cart' : 'Add to Cart'}
    </button>
  );
}
```

4. **Progressive Loading with Suspense**:
```jsx
import { Suspense } from 'react';

function ProductPage({ productId }) {
  return (
    <div>
      <ProductHeader productId={productId} />
      <Suspense fallback={<p>Loading details...</p>}>
        <ProductDetails productId={productId} />
      </Suspense>
      <Suspense fallback={<p>Loading reviews...</p>}>
        <ProductReviews productId={productId} />
      </Suspense>
    </div>
  );
}
```

**Limitations and Considerations:**

1. **No Browser APIs**: Server Components cannot access browser-specific APIs like `window`, `document`, or browser events.

2. **No React Hooks**: Server Components cannot use React hooks like `useState` or `useEffect`.

3. **No Event Handlers**: Server Components cannot include event handlers like `onClick` or `onChange`.

4. **Framework Dependency**: Full RSC implementation currently requires a framework like Next.js or a specialized bundler setup.

5. **Learning Curve**: Developers need to understand the mental model of which code runs where and how to structure applications accordingly.

Server Components represent a significant evolution in React's architecture, enabling developers to build more performant applications with simplified data access patterns while maintaining React's component model and composition benefits.

---

## Performance Optimization

### Q8: How do you optimize React application performance using React.memo, useMemo, and useCallback?

**Difficulty: Medium**

**Answer:**
React provides several built-in optimization techniques to prevent unnecessary re-renders and expensive calculations. Understanding when and how to use these tools is crucial for building performant applications.

**1. React.memo - Component Memoization:**

React.memo is a higher-order component that memoizes the result of a component and only re-renders if its props change.

```jsx
import React, { memo, useState, useCallback } from 'react';

// Without memo - re-renders on every parent update
function ExpensiveChild({ name, count }) {
  console.log('ExpensiveChild rendered');
  
  // Simulate expensive calculation
  const expensiveValue = React.useMemo(() => {
    let result = 0;
    for (let i = 0; i < 1000000; i++) {
      result += i;
    }
    return result + count;
  }, [count]);
  
  return (
    <div>
      <h3>{name}</h3>
      <p>Expensive calculation result: {expensiveValue}</p>
    </div>
  );
}

// With memo - only re-renders when props change
const MemoizedChild = memo(ExpensiveChild);

// Custom comparison function for complex props
const MemoizedChildWithCustomComparison = memo(ExpensiveChild, (prevProps, nextProps) => {
  return prevProps.name === nextProps.name && prevProps.count === nextProps.count;
});
```

**2. useMemo - Value Memoization:**

useMemo memoizes expensive calculations and only recalculates when dependencies change.

```jsx
import React, { useState, useMemo } from 'react';

function ProductList({ products, searchTerm, sortBy }) {
  // Expensive filtering and sorting operation
  const processedProducts = useMemo(() => {
    console.log('Processing products...');
    
    let filtered = products.filter(product => 
      product.name.toLowerCase().includes(searchTerm.toLowerCase())
    );
    
    return filtered.sort((a, b) => {
      switch (sortBy) {
        case 'price':
          return a.price - b.price;
        case 'name':
          return a.name.localeCompare(b.name);
        case 'rating':
          return b.rating - a.rating;
        default:
          return 0;
      }
    });
  }, [products, searchTerm, sortBy]);
  
  // Memoize derived statistics
  const statistics = useMemo(() => {
    return {
      totalProducts: processedProducts.length,
      averagePrice: processedProducts.reduce((sum, p) => sum + p.price, 0) / processedProducts.length,
      averageRating: processedProducts.reduce((sum, p) => sum + p.rating, 0) / processedProducts.length
    };
  }, [processedProducts]);
  
  return (
    <div>
      <div className="statistics">
        <p>Total: {statistics.totalProducts}</p>
        <p>Avg Price: ${statistics.averagePrice.toFixed(2)}</p>
        <p>Avg Rating: {statistics.averageRating.toFixed(1)}</p>
      </div>
      
      <div className="products">
        {processedProducts.map(product => (
          <ProductCard key={product.id} product={product} />
        ))}
      </div>
    </div>
  );
}
```

**3. useCallback - Function Memoization:**

useCallback memoizes functions to prevent unnecessary re-renders of child components that depend on function props.

```jsx
import React, { useState, useCallback, memo } from 'react';

// Child component that receives callback props
const TodoItem = memo(({ todo, onToggle, onDelete, onEdit }) => {
  console.log(`TodoItem ${todo.id} rendered`);
  
  return (
    <div className="todo-item">
      <input 
        type="checkbox" 
        checked={todo.completed}
        onChange={() => onToggle(todo.id)}
      />
      <span 
        style={{ textDecoration: todo.completed ? 'line-through' : 'none' }}
        onClick={() => onEdit(todo.id)}
      >
        {todo.text}
      </span>
      <button onClick={() => onDelete(todo.id)}>Delete</button>
    </div>
  );
});

function TodoApp() {
  const [todos, setTodos] = useState([
    { id: 1, text: 'Learn React', completed: false },
    { id: 2, text: 'Build an app', completed: false }
  ]);
  const [filter, setFilter] = useState('all');
  
  // Without useCallback - new function on every render
  // const handleToggle = (id) => {
  //   setTodos(todos => todos.map(todo => 
  //     todo.id === id ? { ...todo, completed: !todo.completed } : todo
  //   ));
  // };
  
  // With useCallback - function only changes when dependencies change
  const handleToggle = useCallback((id) => {
    setTodos(todos => todos.map(todo => 
      todo.id === id ? { ...todo, completed: !todo.completed } : todo
    ));
  }, []); // Empty dependency array since we use functional update
  
  const handleDelete = useCallback((id) => {
    setTodos(todos => todos.filter(todo => todo.id !== id));
  }, []);
  
  const handleEdit = useCallback((id) => {
    const newText = prompt('Edit todo:');
    if (newText) {
      setTodos(todos => todos.map(todo => 
        todo.id === id ? { ...todo, text: newText } : todo
      ));
    }
  }, []);
  
  // Memoize filtered todos
  const filteredTodos = useMemo(() => {
    switch (filter) {
      case 'active':
        return todos.filter(todo => !todo.completed);
      case 'completed':
        return todos.filter(todo => todo.completed);
      default:
        return todos;
    }
  }, [todos, filter]);
  
  return (
    <div>
      <div className="filters">
        <button onClick={() => setFilter('all')}>All</button>
        <button onClick={() => setFilter('active')}>Active</button>
        <button onClick={() => setFilter('completed')}>Completed</button>
      </div>
      
      <div className="todos">
        {filteredTodos.map(todo => (
          <TodoItem 
            key={todo.id}
            todo={todo}
            onToggle={handleToggle}
            onDelete={handleDelete}
            onEdit={handleEdit}
          />
        ))}
      </div>
    </div>
  );
}
```

**4. Advanced Performance Optimization Patterns:**

```jsx
import React, { useState, useMemo, useCallback, memo, useRef } from 'react';

// Custom hook for debounced values
function useDebounce(value, delay) {
  const [debouncedValue, setDebouncedValue] = useState(value);
  
  React.useEffect(() => {
    const handler = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);
    
    return () => {
      clearTimeout(handler);
    };
  }, [value, delay]);
  
  return debouncedValue;
}

// Virtualized list component for large datasets
const VirtualizedList = memo(({ items, itemHeight = 50, containerHeight = 400 }) => {
  const [scrollTop, setScrollTop] = useState(0);
  const containerRef = useRef();
  
  const visibleItems = useMemo(() => {
    const startIndex = Math.floor(scrollTop / itemHeight);
    const endIndex = Math.min(
      startIndex + Math.ceil(containerHeight / itemHeight) + 1,
      items.length
    );
    
    return items.slice(startIndex, endIndex).map((item, index) => ({
      ...item,
      index: startIndex + index
    }));
  }, [items, scrollTop, itemHeight, containerHeight]);
  
  const handleScroll = useCallback((e) => {
    setScrollTop(e.target.scrollTop);
  }, []);
  
  return (
    <div 
      ref={containerRef}
      style={{ height: containerHeight, overflow: 'auto' }}
      onScroll={handleScroll}
    >
      <div style={{ height: items.length * itemHeight, position: 'relative' }}>
        {visibleItems.map(item => (
          <div 
            key={item.id}
            style={{
              position: 'absolute',
              top: item.index * itemHeight,
              height: itemHeight,
              width: '100%'
            }}
          >
            {item.content}
          </div>
        ))}
      </div>
    </div>
  );
});

// Performance monitoring component
function PerformanceMonitor({ children }) {
  const renderCount = useRef(0);
  const startTime = useRef(performance.now());
  
  React.useEffect(() => {
    renderCount.current += 1;
    const endTime = performance.now();
    console.log(`Render #${renderCount.current} took ${endTime - startTime.current}ms`);
    startTime.current = endTime;
  });
  
  return children;
}
```

**Best Practices:**

1. **Use React.memo sparingly**: Only memoize components that actually have performance issues
2. **Avoid inline objects and functions**: They break memoization
3. **Use useCallback for event handlers**: Especially when passing to memoized child components
4. **Use useMemo for expensive calculations**: Not for simple operations
5. **Profile before optimizing**: Use React DevTools Profiler to identify actual bottlenecks
6. **Consider code splitting**: Use React.lazy and Suspense for large components
7. **Optimize bundle size**: Use tree shaking and analyze bundle composition

**Common Mistakes to Avoid:**
- Over-memoizing everything (can actually hurt performance)
- Forgetting dependencies in useMemo/useCallback
- Using useMemo for values that change frequently
- Not measuring performance impact of optimizations

---

### Q9: How do you implement error boundaries and error handling in React applications?

**Difficulty: Medium**

**Answer:**
Error boundaries are React components that catch JavaScript errors anywhere in their child component tree, log those errors, and display a fallback UI instead of the component tree that crashed. They're essential for building robust React applications.

**1. Basic Error Boundary Implementation:**

```jsx
import React from 'react';

class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { 
      hasError: false, 
      error: null, 
      errorInfo: null 
    };
  }
  
  static getDerivedStateFromError(error) {
    // Update state so the next render will show the fallback UI
    return { hasError: true };
  }
  
  componentDidCatch(error, errorInfo) {
    // Log error details
    console.error('Error caught by boundary:', error, errorInfo);
    
    // Update state with error details
    this.setState({
      error: error,
      errorInfo: errorInfo
    });
    
    // Report error to monitoring service
    this.reportError(error, errorInfo);
  }
  
  reportError = (error, errorInfo) => {
    // Example: Send to error reporting service
    if (process.env.NODE_ENV === 'production') {
      // Sentry, LogRocket, Bugsnag, etc.
      console.log('Reporting error to monitoring service:', {
        message: error.message,
        stack: error.stack,
        componentStack: errorInfo.componentStack
      });
    }
  }
  
  handleRetry = () => {
    this.setState({ 
      hasError: false, 
      error: null, 
      errorInfo: null 
    });
  }
  
  render() {
    if (this.state.hasError) {
      return (
        <div className="error-boundary">
          <h2>Something went wrong</h2>
          <details style={{ whiteSpace: 'pre-wrap' }}>
            <summary>Error details (click to expand)</summary>
            <p><strong>Error:</strong> {this.state.error && this.state.error.toString()}</p>
            <p><strong>Component Stack:</strong></p>
            <pre>{this.state.errorInfo.componentStack}</pre>
          </details>
          <button onClick={this.handleRetry}>Try Again</button>
        </div>
      );
    }
    
    return this.props.children;
  }
}
```

**2. Advanced Error Boundary with Different Fallback UIs:**

```jsx
import React, { Component } from 'react';

class AdvancedErrorBoundary extends Component {
  constructor(props) {
    super(props);
    this.state = {
      hasError: false,
      error: null,
      errorId: null,
      retryCount: 0
    };
  }
  
  static getDerivedStateFromError(error) {
    return {
      hasError: true,
      errorId: Date.now().toString(36) + Math.random().toString(36).substr(2)
    };
  }
  
  componentDidCatch(error, errorInfo) {
    const { onError, level = 'error' } = this.props;
    
    this.setState({ error });
    
    // Custom error handler
    if (onError) {
      onError(error, errorInfo, this.state.errorId);
    }
    
    // Log based on level
    this.logError(error, errorInfo, level);
  }
  
  logError = (error, errorInfo, level) => {
    const errorData = {
      message: error.message,
      stack: error.stack,
      componentStack: errorInfo.componentStack,
      errorId: this.state.errorId,
      timestamp: new Date().toISOString(),
      userAgent: navigator.userAgent,
      url: window.location.href
    };
    
    switch (level) {
      case 'warning':
        console.warn('Warning caught by boundary:', errorData);
        break;
      case 'error':
        console.error('Error caught by boundary:', errorData);
        break;
      case 'critical':
        console.error('Critical error caught by boundary:', errorData);
        // Send to monitoring service immediately
        this.sendToMonitoring(errorData);
        break;
      default:
        console.log('Info caught by boundary:', errorData);
    }
  }
  
  sendToMonitoring = (errorData) => {
    // Example integration with monitoring service
    fetch('/api/errors', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(errorData)
    }).catch(err => console.error('Failed to send error to monitoring:', err));
  }
  
  handleRetry = () => {
    this.setState(prevState => ({
      hasError: false,
      error: null,
      errorId: null,
      retryCount: prevState.retryCount + 1
    }));
  }
  
  render() {
    const { hasError, retryCount } = this.state;
    const { fallback: Fallback, level = 'error' } = this.props;
    
    if (hasError) {
      // Custom fallback component
      if (Fallback) {
        return (
          <Fallback 
            error={this.state.error}
            errorId={this.state.errorId}
            onRetry={this.handleRetry}
            retryCount={retryCount}
          />
        );
      }
      
      // Default fallback based on level
      switch (level) {
        case 'warning':
          return (
            <div className="error-warning">
              <p>⚠️ Something's not quite right, but you can continue.</p>
              <button onClick={this.handleRetry}>Refresh</button>
            </div>
          );
        case 'critical':
          return (
            <div className="error-critical">
              <h1>🚨 Critical Error</h1>
              <p>We're sorry, but something went seriously wrong.</p>
              <p>Error ID: {this.state.errorId}</p>
              <button onClick={() => window.location.reload()}>Reload Page</button>
            </div>
          );
        default:
          return (
            <div className="error-default">
              <h2>😕 Oops! Something went wrong</h2>
              <p>Don't worry, it's not your fault. Please try again.</p>
              <button onClick={this.handleRetry}>Try Again</button>
              {retryCount > 2 && (
                <button onClick={() => window.location.reload()}>Reload Page</button>
              )}
            </div>
          );
      }
    }
    
    return this.props.children;
  }
}
```

**3. Functional Error Boundary Hook (React 18+):**

```jsx
import React, { useState, useEffect } from 'react';

// Custom hook for error handling
function useErrorHandler() {
  const [error, setError] = useState(null);
  
  const resetError = () => setError(null);
  
  const captureError = (error, errorInfo) => {
    setError({ error, errorInfo });
    
    // Log error
    console.error('Error captured:', error, errorInfo);
    
    // Report to monitoring service
    if (process.env.NODE_ENV === 'production') {
      // Send to error reporting service
    }
  };
  
  return { error, resetError, captureError };
}

// Functional component with error handling
function FunctionalErrorBoundary({ children, fallback }) {
  const { error, resetError, captureError } = useErrorHandler();
  
  useEffect(() => {
    const handleError = (event) => {
      captureError(event.error, { componentStack: 'Unknown' });
    };
    
    const handleUnhandledRejection = (event) => {
      captureError(new Error(event.reason), { componentStack: 'Promise rejection' });
    };
    
    window.addEventListener('error', handleError);
    window.addEventListener('unhandledrejection', handleUnhandledRejection);
    
    return () => {
      window.removeEventListener('error', handleError);
      window.removeEventListener('unhandledrejection', handleUnhandledRejection);
    };
  }, [captureError]);
  
  if (error) {
    if (fallback) {
      return fallback(error, resetError);
    }
    
    return (
      <div className="error-boundary">
        <h2>Something went wrong</h2>
        <button onClick={resetError}>Try Again</button>
      </div>
    );
  }
  
  return children;
}
```

**4. Async Error Handling:**

```jsx
import React, { useState, useEffect } from 'react';

// Custom hook for async operations with error handling
function useAsyncOperation() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [data, setData] = useState(null);
  
  const execute = async (asyncFunction) => {
    try {
      setLoading(true);
      setError(null);
      const result = await asyncFunction();
      setData(result);
      return result;
    } catch (err) {
      setError(err);
      throw err;
    } finally {
      setLoading(false);
    }
  };
  
  const reset = () => {
    setLoading(false);
    setError(null);
    setData(null);
  };
  
  return { loading, error, data, execute, reset };
}

// Component using async error handling
function DataFetcher({ userId }) {
  const { loading, error, data, execute, reset } = useAsyncOperation();
  
  const fetchUserData = async () => {
    const response = await fetch(`/api/users/${userId}`);
    if (!response.ok) {
      throw new Error(`Failed to fetch user: ${response.statusText}`);
    }
    return response.json();
  };
  
  useEffect(() => {
    execute(fetchUserData);
  }, [userId]);
  
  if (loading) return <div>Loading...</div>;
  
  if (error) {
    return (
      <div className="error-state">
        <h3>Failed to load user data</h3>
        <p>{error.message}</p>
        <button onClick={() => execute(fetchUserData)}>Retry</button>
        <button onClick={reset}>Reset</button>
      </div>
    );
  }
  
  return (
    <div>
      <h2>{data?.name}</h2>
      <p>{data?.email}</p>
    </div>
  );
}
```

**5. Usage Examples:**

```jsx
// App-level error boundary
function App() {
  return (
    <AdvancedErrorBoundary 
      level="critical"
      onError={(error, errorInfo, errorId) => {
        // Send to analytics
        analytics.track('Error Occurred', {
          errorId,
          message: error.message,
          component: errorInfo.componentStack
        });
      }}
    >
      <Router>
        <Routes>
          <Route path="/" element={
            <AdvancedErrorBoundary level="error">
              <HomePage />
            </AdvancedErrorBoundary>
          } />
          <Route path="/profile" element={
            <AdvancedErrorBoundary 
              level="warning"
              fallback={({ error, onRetry }) => (
                <div>
                  <p>Profile couldn't load: {error.message}</p>
                  <button onClick={onRetry}>Try Again</button>
                </div>
              )}
            >
              <ProfilePage />
            </AdvancedErrorBoundary>
          } />
        </Routes>
      </Router>
    </AdvancedErrorBoundary>
  );
}
```

**Best Practices:**

1. **Strategic Placement**: Place error boundaries at different levels of your component tree
2. **Granular Error Handling**: Use different error boundaries for different parts of your app
3. **User-Friendly Messages**: Provide clear, actionable error messages
4. **Error Reporting**: Always log errors to monitoring services in production
5. **Recovery Options**: Provide retry mechanisms and fallback UIs
6. **Testing**: Test error scenarios and error boundary behavior
7. **Performance**: Don't let error handling impact normal app performance

**What Error Boundaries Don't Catch:**
- Errors inside event handlers
- Errors in asynchronous code (setTimeout, promises)
- Errors during server-side rendering
- Errors thrown in the error boundary itself

For these cases, use try-catch blocks, promise .catch() methods, and proper async error handling patterns.

---

## Advanced React Patterns

### Q10: Explain React Context API and when to use it over prop drilling.

**Difficulty: Medium**

**Answer:**
The React Context API provides a way to share data between components without having to pass props down manually at every level. It's designed to solve the "prop drilling" problem where you need to pass data through many intermediate components.

**1. Basic Context Implementation:**

```jsx
import React, { createContext, useContext, useState, useReducer } from 'react';

// Create Context
const ThemeContext = createContext();
const UserContext = createContext();

// Theme Provider Component
function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light');
  
  const toggleTheme = () => {
    setTheme(prevTheme => prevTheme === 'light' ? 'dark' : 'light');
  };
  
  const value = {
    theme,
    toggleTheme
  };
  
  return (
    <ThemeContext.Provider value={value}>
      {children}
    </ThemeContext.Provider>
  );
}

// Custom hook for using theme context
function useTheme() {
  const context = useContext(ThemeContext);
  if (!context) {
    throw new Error('useTheme must be used within a ThemeProvider');
  }
  return context;
}

// Component using the context
function Header() {
  const { theme, toggleTheme } = useTheme();
  
  return (
    <header className={`header ${theme}`}>
      <h1>My App</h1>
      <button onClick={toggleTheme}>
        Switch to {theme === 'light' ? 'dark' : 'light'} mode
      </button>
    </header>
  );
}

// Deeply nested component that needs theme
function Button({ children, onClick }) {
  const { theme } = useTheme();
  
  return (
    <button 
      className={`btn btn-${theme}`}
      onClick={onClick}
    >
      {children}
    </button>
  );
}
```

**2. Advanced Context with useReducer:**

```jsx
import React, { createContext, useContext, useReducer } from 'react';

// User state management with reducer
const initialUserState = {
  user: null,
  loading: false,
  error: null,
  preferences: {
    notifications: true,
    theme: 'light',
    language: 'en'
  }
};

function userReducer(state, action) {
  switch (action.type) {
    case 'LOGIN_START':
      return {
        ...state,
        loading: true,
        error: null
      };
    case 'LOGIN_SUCCESS':
      return {
        ...state,
        loading: false,
        user: action.payload,
        error: null
      };
    case 'LOGIN_ERROR':
      return {
        ...state,
        loading: false,
        error: action.payload
      };
    case 'LOGOUT':
      return {
        ...initialUserState
      };
    case 'UPDATE_PREFERENCES':
      return {
        ...state,
        preferences: {
          ...state.preferences,
          ...action.payload
        }
      };
    case 'UPDATE_PROFILE':
      return {
        ...state,
        user: {
          ...state.user,
          ...action.payload
        }
      };
    default:
      return state;
  }
}

// User Context Provider
function UserProvider({ children }) {
  const [state, dispatch] = useReducer(userReducer, initialUserState);
  
  const login = async (credentials) => {
    dispatch({ type: 'LOGIN_START' });
    try {
      const response = await fetch('/api/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(credentials)
      });
      
      if (!response.ok) {
        throw new Error('Login failed');
      }
      
      const user = await response.json();
      dispatch({ type: 'LOGIN_SUCCESS', payload: user });
    } catch (error) {
      dispatch({ type: 'LOGIN_ERROR', payload: error.message });
    }
  };
  
  const logout = () => {
    dispatch({ type: 'LOGOUT' });
  };
  
  const updatePreferences = (preferences) => {
    dispatch({ type: 'UPDATE_PREFERENCES', payload: preferences });
  };
  
  const updateProfile = (profileData) => {
    dispatch({ type: 'UPDATE_PROFILE', payload: profileData });
  };
  
  const value = {
    ...state,
    login,
    logout,
    updatePreferences,
    updateProfile
  };
  
  return (
    <UserContext.Provider value={value}>
      {children}
    </UserContext.Provider>
  );
}

// Custom hook for user context
function useUser() {
  const context = useContext(UserContext);
  if (!context) {
    throw new Error('useUser must be used within a UserProvider');
  }
  return context;
}
```

**3. Multiple Context Providers Pattern:**

```jsx
// App Providers Composition
function AppProviders({ children }) {
  return (
    <ThemeProvider>
      <UserProvider>
        <NotificationProvider>
          <LanguageProvider>
            {children}
          </LanguageProvider>
        </NotificationProvider>
      </UserProvider>
    </ThemeProvider>
  );
}

// Main App Component
function App() {
  return (
    <AppProviders>
      <Router>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/profile" element={<ProfilePage />} />
          <Route path="/settings" element={<SettingsPage />} />
        </Routes>
      </Router>
    </AppProviders>
  );
}
```

**4. Context with Performance Optimization:**

```jsx
import React, { createContext, useContext, useMemo, useCallback } from 'react';

// Separate contexts for different concerns to prevent unnecessary re-renders
const CartStateContext = createContext();
const CartActionsContext = createContext();

function CartProvider({ children }) {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(false);
  
  // Memoize state to prevent unnecessary re-renders
  const state = useMemo(() => ({
    items,
    loading,
    totalItems: items.reduce((sum, item) => sum + item.quantity, 0),
    totalPrice: items.reduce((sum, item) => sum + (item.price * item.quantity), 0)
  }), [items, loading]);
  
  // Memoize actions to prevent unnecessary re-renders
  const actions = useMemo(() => ({
    addItem: useCallback((product) => {
      setItems(prevItems => {
        const existingItem = prevItems.find(item => item.id === product.id);
        if (existingItem) {
          return prevItems.map(item =>
            item.id === product.id
              ? { ...item, quantity: item.quantity + 1 }
              : item
          );
        }
        return [...prevItems, { ...product, quantity: 1 }];
      });
    }, []),
    
    removeItem: useCallback((productId) => {
      setItems(prevItems => prevItems.filter(item => item.id !== productId));
    }, []),
    
    updateQuantity: useCallback((productId, quantity) => {
      if (quantity <= 0) {
        setItems(prevItems => prevItems.filter(item => item.id !== productId));
      } else {
        setItems(prevItems =>
          prevItems.map(item =>
            item.id === productId ? { ...item, quantity } : item
          )
        );
      }
    }, []),
    
    clearCart: useCallback(() => {
      setItems([]);
    }, [])
  }), []);
  
  return (
    <CartStateContext.Provider value={state}>
      <CartActionsContext.Provider value={actions}>
        {children}
      </CartActionsContext.Provider>
    </CartStateContext.Provider>
  );
}

// Separate hooks for state and actions
function useCartState() {
  const context = useContext(CartStateContext);
  if (!context) {
    throw new Error('useCartState must be used within a CartProvider');
  }
  return context;
}

function useCartActions() {
  const context = useContext(CartActionsContext);
  if (!context) {
    throw new Error('useCartActions must be used within a CartProvider');
  }
  return context;
}
```

**When to Use Context vs Prop Drilling:**

**Use Context When:**
- Data is needed by many components at different nesting levels
- You have global application state (user authentication, theme, language)
- Prop drilling becomes cumbersome (passing through 3+ levels)
- You need to avoid "threading" props through components that don't use them

**Use Prop Drilling When:**
- Data is only needed by a few closely related components
- The component tree is shallow (1-2 levels)
- You want explicit data flow that's easy to trace
- Performance is critical and you want to avoid context re-renders

**Best Practices:**
1. **Split contexts by concern**: Don't put everything in one context
2. **Use custom hooks**: Encapsulate context logic in custom hooks
3. **Optimize for performance**: Separate state and actions, use useMemo/useCallback
4. **Provide default values**: Always provide meaningful default values
5. **Error boundaries**: Wrap context providers with error boundaries
6. **TypeScript**: Use TypeScript for better type safety with contexts

---

### Q11: What are Higher-Order Components (HOCs) and how do you implement them?

**Difficulty: Medium-Hard**

**Answer:**
Higher-Order Components (HOCs) are a pattern in React for reusing component logic. An HOC is a function that takes a component and returns a new component with additional props or behavior. It's a way to share common functionality between components.

**1. Basic HOC Implementation:**

```jsx
import React, { useState, useEffect } from 'react';

// Basic HOC that adds loading state
function withLoading(WrappedComponent) {
  return function WithLoadingComponent(props) {
    const [loading, setLoading] = useState(true);
    
    useEffect(() => {
      // Simulate loading
      const timer = setTimeout(() => {
        setLoading(false);
      }, 2000);
      
      return () => clearTimeout(timer);
    }, []);
    
    if (loading) {
      return (
        <div className="loading-spinner">
          <div className="spinner"></div>
          <p>Loading...</p>
        </div>
      );
    }
    
    return <WrappedComponent {...props} />;
  };
}

// Usage
function UserProfile({ user }) {
  return (
    <div>
      <h2>{user.name}</h2>
      <p>{user.email}</p>
    </div>
  );
}

const UserProfileWithLoading = withLoading(UserProfile);
```

**2. HOC with Authentication:**

```jsx
import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

// HOC for authentication
function withAuth(WrappedComponent, options = {}) {
  return function WithAuthComponent(props) {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);
    const navigate = useNavigate();
    const { redirectTo = '/login', requiredRoles = [] } = options;
    
    useEffect(() => {
      async function checkAuth() {
        try {
          const token = localStorage.getItem('authToken');
          if (!token) {
            throw new Error('No token found');
          }
          
          const response = await fetch('/api/auth/verify', {
            headers: {
              'Authorization': `Bearer ${token}`
            }
          });
          
          if (!response.ok) {
            throw new Error('Token invalid');
          }
          
          const userData = await response.json();
          
          // Check if user has required roles
          if (requiredRoles.length > 0) {
            const hasRequiredRole = requiredRoles.some(role => 
              userData.roles.includes(role)
            );
            
            if (!hasRequiredRole) {
              throw new Error('Insufficient permissions');
            }
          }
          
          setUser(userData);
        } catch (error) {
          console.error('Authentication failed:', error);
          localStorage.removeItem('authToken');
          navigate(redirectTo);
        } finally {
          setLoading(false);
        }
      }
      
      checkAuth();
    }, [navigate, redirectTo]);
    
    if (loading) {
      return <div>Authenticating...</div>;
    }
    
    if (!user) {
      return null; // Will redirect
    }
    
    return <WrappedComponent {...props} user={user} />;
  };
}

// Usage
function AdminDashboard({ user }) {
  return (
    <div>
      <h1>Admin Dashboard</h1>
      <p>Welcome, {user.name}!</p>
    </div>
  );
}

const ProtectedAdminDashboard = withAuth(AdminDashboard, {
  redirectTo: '/login',
  requiredRoles: ['admin']
});
```

**3. HOC for Data Fetching:**

```jsx
import React, { useState, useEffect } from 'react';

// Generic data fetching HOC
function withDataFetching(WrappedComponent, config) {
  return function WithDataFetchingComponent(props) {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    
    const { 
      url, 
      propName = 'data',
      dependencies = [],
      transform = (data) => data,
      onError = (error) => console.error(error)
    } = typeof config === 'function' ? config(props) : config;
    
    useEffect(() => {
      async function fetchData() {
        try {
          setLoading(true);
          setError(null);
          
          const response = await fetch(url);
          if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
          }
          
          const result = await response.json();
          const transformedData = transform(result);
          setData(transformedData);
        } catch (err) {
          setError(err);
          onError(err);
        } finally {
          setLoading(false);
        }
      }
      
      fetchData();
    }, dependencies);
    
    const enhancedProps = {
      ...props,
      [propName]: data,
      [`${propName}Loading`]: loading,
      [`${propName}Error`]: error
    };
    
    return <WrappedComponent {...enhancedProps} />;
  };
}

// Usage
function UserList({ users, usersLoading, usersError }) {
  if (usersLoading) return <div>Loading users...</div>;
  if (usersError) return <div>Error: {usersError.message}</div>;
  
  return (
    <ul>
      {users.map(user => (
        <li key={user.id}>{user.name} - {user.email}</li>
      ))}
    </ul>
  );
}

const UserListWithData = withDataFetching(UserList, {
  url: '/api/users',
  propName: 'users',
  transform: (data) => data.users || [],
  onError: (error) => {
    console.error('Failed to fetch users:', error);
    // Could also send to error reporting service
  }
});

// Dynamic configuration based on props
function PostList({ posts, postsLoading, postsError }) {
  if (postsLoading) return <div>Loading posts...</div>;
  if (postsError) return <div>Error: {postsError.message}</div>;
  
  return (
    <div>
      {posts.map(post => (
        <article key={post.id}>
          <h3>{post.title}</h3>
          <p>{post.excerpt}</p>
        </article>
      ))}
    </div>
  );
}

const PostListWithData = withDataFetching(PostList, (props) => ({
  url: `/api/users/${props.userId}/posts`,
  propName: 'posts',
  dependencies: [props.userId],
  transform: (data) => data.posts || []
}));
```

**4. Composing Multiple HOCs:**

```jsx
import { compose } from 'redux'; // or create your own compose function

// Utility function to compose HOCs
function compose(...funcs) {
  if (funcs.length === 0) {
    return arg => arg;
  }
  
  if (funcs.length === 1) {
    return funcs[0];
  }
  
  return funcs.reduce((a, b) => (...args) => a(b(...args)));
}

// HOC for error boundary
function withErrorBoundary(WrappedComponent) {
  return class WithErrorBoundary extends React.Component {
    constructor(props) {
      super(props);
      this.state = { hasError: false };
    }
    
    static getDerivedStateFromError(error) {
      return { hasError: true };
    }
    
    componentDidCatch(error, errorInfo) {
      console.error('Error caught by HOC:', error, errorInfo);
    }
    
    render() {
      if (this.state.hasError) {
        return <div>Something went wrong.</div>;
      }
      
      return <WrappedComponent {...this.props} />;
    }
  };
}

// HOC for analytics tracking
function withAnalytics(WrappedComponent, eventName) {
  return function WithAnalyticsComponent(props) {
    useEffect(() => {
      // Track component mount
      analytics.track(`${eventName}_viewed`, {
        timestamp: new Date().toISOString(),
        props: Object.keys(props)
      });
      
      return () => {
        // Track component unmount
        analytics.track(`${eventName}_left`, {
          timestamp: new Date().toISOString()
        });
      };
    }, []);
    
    return <WrappedComponent {...props} />;
  };
}

// Compose multiple HOCs
const enhance = compose(
  withAuth({ requiredRoles: ['user'] }),
  withErrorBoundary,
  withLoading,
  withAnalytics('dashboard')
);

const EnhancedDashboard = enhance(Dashboard);
```

**5. Modern Alternative - Custom Hooks:**

```jsx
// Modern approach using custom hooks instead of HOCs
function useAuth(options = {}) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();
  
  useEffect(() => {
    // Authentication logic here
  }, []);
  
  return { user, loading };
}

function useDataFetching(url, dependencies = []) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  
  useEffect(() => {
    // Data fetching logic here
  }, dependencies);
  
  return { data, loading, error };
}

// Usage with hooks (preferred modern approach)
function Dashboard() {
  const { user, loading: authLoading } = useAuth({ requiredRoles: ['user'] });
  const { data: posts, loading: postsLoading } = useDataFetching('/api/posts');
  
  if (authLoading || postsLoading) return <div>Loading...</div>;
  
  return (
    <div>
      <h1>Welcome, {user.name}!</h1>
      {/* Render posts */}
    </div>
  );
}
```

**When to Use HOCs vs Hooks:**

**Use HOCs when:**
- You need to wrap components with additional JSX (error boundaries, providers)
- Working with class components
- You need to modify component behavior at the component level
- Legacy codebase that already uses HOCs

**Use Hooks when:**
- You want to share stateful logic between components
- Working with functional components
- You need more flexibility and composability
- Building new applications (modern React approach)

**Best Practices:**
1. **Don't mutate the original component**: Always return a new component
2. **Copy static methods**: Use `hoist-non-react-statics` library
3. **Pass through props**: Always spread props to the wrapped component
4. **Use display names**: Set meaningful display names for debugging
5. **Don't use HOCs inside render**: Create enhanced components outside render
6. **Consider hooks first**: For new code, prefer custom hooks over HOCs

---

## Testing

### Q12: How do you test React components using Jest and React Testing Library?

**Difficulty: Medium**

**Answer:**
Testing React components is crucial for maintaining code quality and preventing regressions. Jest and React Testing Library provide a powerful combination for testing React applications with a focus on testing behavior rather than implementation details.

**1. Basic Component Testing:**

```jsx
// Button.jsx
import React from 'react';

function Button({ children, onClick, disabled = false, variant = 'primary' }) {
  return (
    <button 
      onClick={onClick}
      disabled={disabled}
      className={`btn btn-${variant}`}
      data-testid="button"
    >
      {children}
    </button>
  );
}

export default Button;
```

```jsx
// Button.test.jsx
import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import Button from './Button';

describe('Button Component', () => {
  test('renders button with text', () => {
    render(<Button>Click me</Button>);
    
    const button = screen.getByRole('button', { name: /click me/i });
    expect(button).toBeInTheDocument();
  });
  
  test('calls onClick handler when clicked', async () => {
    const handleClick = jest.fn();
    const user = userEvent.setup();
    
    render(<Button onClick={handleClick}>Click me</Button>);
    
    const button = screen.getByRole('button');
    await user.click(button);
    
    expect(handleClick).toHaveBeenCalledTimes(1);
  });
  
  test('is disabled when disabled prop is true', () => {
    render(<Button disabled>Click me</Button>);
    
    const button = screen.getByRole('button');
    expect(button).toBeDisabled();
  });
  
  test('applies correct CSS class based on variant', () => {
    render(<Button variant="secondary">Click me</Button>);
    
    const button = screen.getByRole('button');
    expect(button).toHaveClass('btn-secondary');
  });
});
```

**2. Testing Components with State:**

```jsx
// Counter.jsx
import React, { useState } from 'react';

function Counter({ initialValue = 0, step = 1 }) {
  const [count, setCount] = useState(initialValue);
  
  const increment = () => setCount(prev => prev + step);
  const decrement = () => setCount(prev => prev - step);
  const reset = () => setCount(initialValue);
  
  return (
    <div>
      <h2 data-testid="count-display">Count: {count}</h2>
      <button onClick={increment}>Increment</button>
      <button onClick={decrement}>Decrement</button>
      <button onClick={reset}>Reset</button>
    </div>
  );
}

export default Counter;
```

```jsx
// Counter.test.jsx
import React from 'react';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import Counter from './Counter';

describe('Counter Component', () => {
  test('displays initial count', () => {
    render(<Counter initialValue={5} />);
    
    expect(screen.getByTestId('count-display')).toHaveTextContent('Count: 5');
  });
  
  test('increments count when increment button is clicked', async () => {
    const user = userEvent.setup();
    render(<Counter initialValue={0} step={2} />);
    
    const incrementButton = screen.getByRole('button', { name: /increment/i });
    await user.click(incrementButton);
    
    expect(screen.getByTestId('count-display')).toHaveTextContent('Count: 2');
  });
  
  test('decrements count when decrement button is clicked', async () => {
    const user = userEvent.setup();
    render(<Counter initialValue={10} />);
    
    const decrementButton = screen.getByRole('button', { name: /decrement/i });
    await user.click(decrementButton);
    
    expect(screen.getByTestId('count-display')).toHaveTextContent('Count: 9');
  });
  
  test('resets count to initial value when reset button is clicked', async () => {
    const user = userEvent.setup();
    render(<Counter initialValue={5} />);
    
    // First increment the counter
    const incrementButton = screen.getByRole('button', { name: /increment/i });
    await user.click(incrementButton);
    expect(screen.getByTestId('count-display')).toHaveTextContent('Count: 6');
    
    // Then reset
    const resetButton = screen.getByRole('button', { name: /reset/i });
    await user.click(resetButton);
    expect(screen.getByTestId('count-display')).toHaveTextContent('Count: 5');
  });
});
```

**3. Testing Components with API Calls:**

```jsx
// UserProfile.jsx
import React, { useState, useEffect } from 'react';

function UserProfile({ userId }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  
  useEffect(() => {
    async function fetchUser() {
      try {
        setLoading(true);
        const response = await fetch(`/api/users/${userId}`);
        
        if (!response.ok) {
          throw new Error('Failed to fetch user');
        }
        
        const userData = await response.json();
        setUser(userData);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }
    
    if (userId) {
      fetchUser();
    }
  }, [userId]);
  
  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;
  if (!user) return <div>No user found</div>;
  
  return (
    <div>
      <h2>{user.name}</h2>
      <p>Email: {user.email}</p>
      <p>Role: {user.role}</p>
    </div>
  );
}

export default UserProfile;
```

```jsx
// UserProfile.test.jsx
import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import UserProfile from './UserProfile';

// Mock fetch globally
global.fetch = jest.fn();

describe('UserProfile Component', () => {
  beforeEach(() => {
    fetch.mockClear();
  });
  
  test('displays loading state initially', () => {
    fetch.mockResolvedValueOnce({
      ok: true,
      json: async () => ({ id: 1, name: 'John Doe', email: 'john@example.com', role: 'user' })
    });
    
    render(<UserProfile userId={1} />);
    
    expect(screen.getByText('Loading...')).toBeInTheDocument();
  });
  
  test('displays user data after successful fetch', async () => {
    const mockUser = {
      id: 1,
      name: 'John Doe',
      email: 'john@example.com',
      role: 'admin'
    };
    
    fetch.mockResolvedValueOnce({
      ok: true,
      json: async () => mockUser
    });
    
    render(<UserProfile userId={1} />);
    
    await waitFor(() => {
      expect(screen.getByText('John Doe')).toBeInTheDocument();
    });
    
    expect(screen.getByText('Email: john@example.com')).toBeInTheDocument();
    expect(screen.getByText('Role: admin')).toBeInTheDocument();
  });
  
  test('displays error message when fetch fails', async () => {
    fetch.mockRejectedValueOnce(new Error('Network error'));
    
    render(<UserProfile userId={1} />);
    
    await waitFor(() => {
      expect(screen.getByText('Error: Network error')).toBeInTheDocument();
    });
  });
  
  test('displays error when API returns non-ok response', async () => {
    fetch.mockResolvedValueOnce({
      ok: false,
      status: 404
    });
    
    render(<UserProfile userId={1} />);
    
    await waitFor(() => {
      expect(screen.getByText('Error: Failed to fetch user')).toBeInTheDocument();
    });
  });
  
  test('makes correct API call with userId', () => {
    fetch.mockResolvedValueOnce({
      ok: true,
      json: async () => ({})
    });
    
    render(<UserProfile userId={123} />);
    
    expect(fetch).toHaveBeenCalledWith('/api/users/123');
  });
});
```

**4. Testing Custom Hooks:**

```jsx
// useCounter.js
import { useState, useCallback } from 'react';

function useCounter(initialValue = 0) {
  const [count, setCount] = useState(initialValue);
  
  const increment = useCallback(() => {
    setCount(prev => prev + 1);
  }, []);
  
  const decrement = useCallback(() => {
    setCount(prev => prev - 1);
  }, []);
  
  const reset = useCallback(() => {
    setCount(initialValue);
  }, [initialValue]);
  
  return { count, increment, decrement, reset };
}

export default useCounter;
```

```jsx
// useCounter.test.js
import { renderHook, act } from '@testing-library/react';
import useCounter from './useCounter';

describe('useCounter Hook', () => {
  test('initializes with default value', () => {
    const { result } = renderHook(() => useCounter());
    
    expect(result.current.count).toBe(0);
  });
  
  test('initializes with custom value', () => {
    const { result } = renderHook(() => useCounter(10));
    
    expect(result.current.count).toBe(10);
  });
  
  test('increments count', () => {
    const { result } = renderHook(() => useCounter(0));
    
    act(() => {
      result.current.increment();
    });
    
    expect(result.current.count).toBe(1);
  });
  
  test('decrements count', () => {
    const { result } = renderHook(() => useCounter(5));
    
    act(() => {
      result.current.decrement();
    });
    
    expect(result.current.count).toBe(4);
  });
  
  test('resets count to initial value', () => {
    const { result } = renderHook(() => useCounter(10));
    
    act(() => {
      result.current.increment();
      result.current.increment();
    });
    
    expect(result.current.count).toBe(12);
    
    act(() => {
      result.current.reset();
    });
    
    expect(result.current.count).toBe(10);
  });
});
```

**5. Testing Context Providers:**

```jsx
// ThemeContext.test.jsx
import React from 'react';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { ThemeProvider, useTheme } from './ThemeContext';

// Test component that uses the theme context
function TestComponent() {
  const { theme, toggleTheme } = useTheme();
  
  return (
    <div>
      <span data-testid="current-theme">{theme}</span>
      <button onClick={toggleTheme}>Toggle Theme</button>
    </div>
  );
}

describe('ThemeProvider', () => {
  test('provides default theme', () => {
    render(
      <ThemeProvider>
        <TestComponent />
      </ThemeProvider>
    );
    
    expect(screen.getByTestId('current-theme')).toHaveTextContent('light');
  });
  
  test('toggles theme when button is clicked', async () => {
    const user = userEvent.setup();
    
    render(
      <ThemeProvider>
        <TestComponent />
      </ThemeProvider>
    );
    
    const toggleButton = screen.getByRole('button', { name: /toggle theme/i });
    
    // Initial theme should be light
    expect(screen.getByTestId('current-theme')).toHaveTextContent('light');
    
    // Click to toggle to dark
    await user.click(toggleButton);
    expect(screen.getByTestId('current-theme')).toHaveTextContent('dark');
    
    // Click again to toggle back to light
    await user.click(toggleButton);
    expect(screen.getByTestId('current-theme')).toHaveTextContent('light');
  });
});
```

**6. Setup and Configuration:**

```javascript
// jest.config.js
module.exports = {
  testEnvironment: 'jsdom',
  setupFilesAfterEnv: ['<rootDir>/src/setupTests.js'],
  moduleNameMapping: {
    '\\.(css|less|scss|sass)$': 'identity-obj-proxy'
  },
  collectCoverageFrom: [
    'src/**/*.{js,jsx}',
    '!src/index.js',
    '!src/reportWebVitals.js'
  ],
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80
    }
  }
};
```

```javascript
// src/setupTests.js
import '@testing-library/jest-dom';

// Mock IntersectionObserver
global.IntersectionObserver = class IntersectionObserver {
  constructor() {}
  observe() { return null; }
  disconnect() { return null; }
  unobserve() { return null; }
};

// Mock window.matchMedia
Object.defineProperty(window, 'matchMedia', {
  writable: true,
  value: jest.fn().mockImplementation(query => ({
    matches: false,
    media: query,
    onchange: null,
    addListener: jest.fn(),
    removeListener: jest.fn(),
    addEventListener: jest.fn(),
    removeEventListener: jest.fn(),
    dispatchEvent: jest.fn(),
  })),
});
```

**Best Practices:**

1. **Test behavior, not implementation**: Focus on what the user sees and does
2. **Use semantic queries**: Prefer `getByRole`, `getByLabelText` over `getByTestId`
3. **Test user interactions**: Use `userEvent` for realistic user interactions
4. **Mock external dependencies**: Mock API calls, third-party libraries
5. **Test error states**: Don't forget to test error scenarios
6. **Keep tests isolated**: Each test should be independent
7. **Use descriptive test names**: Make it clear what each test is verifying
8. **Test accessibility**: Ensure your components are accessible

---

### Q13: How do you implement and test React Router navigation?

**Difficulty: Medium**

**Answer:**
React Router is the standard library for routing in React applications. Testing routing involves verifying navigation behavior, route parameters, and protected routes.

**1. Basic Router Setup:**

```jsx
// App.jsx
import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import HomePage from './pages/HomePage';
import AboutPage from './pages/AboutPage';
import UserProfile from './pages/UserProfile';
import NotFound from './pages/NotFound';
import Navigation from './components/Navigation';

function App() {
  return (
    <Router>
      <div className="app">
        <Navigation />
        <main>
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/about" element={<AboutPage />} />
            <Route path="/users/:userId" element={<UserProfile />} />
            <Route path="/404" element={<NotFound />} />
            <Route path="*" element={<Navigate to="/404" replace />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
```

```jsx
// components/Navigation.jsx
import React from 'react';
import { Link, useLocation } from 'react-router-dom';

function Navigation() {
  const location = useLocation();
  
  const isActive = (path) => location.pathname === path;
  
  return (
    <nav>
      <ul>
        <li>
          <Link 
            to="/" 
            className={isActive('/') ? 'active' : ''}
          >
            Home
          </Link>
        </li>
        <li>
          <Link 
            to="/about" 
            className={isActive('/about') ? 'active' : ''}
          >
            About
          </Link>
        </li>
        <li>
          <Link to="/users/123">User Profile</Link>
        </li>
      </ul>
    </nav>
  );
}

export default Navigation;
```

**2. Testing Router Components:**

```jsx
// App.test.jsx
import React from 'react';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { MemoryRouter } from 'react-router-dom';
import App from './App';

// Helper function to render with router
function renderWithRouter(ui, { initialEntries = ['/'] } = {}) {
  return render(
    <MemoryRouter initialEntries={initialEntries}>
      {ui}
    </MemoryRouter>
  );
}

describe('App Routing', () => {
  test('renders home page by default', () => {
    renderWithRouter(<App />);
    
    expect(screen.getByText('Welcome to Home Page')).toBeInTheDocument();
  });
  
  test('navigates to about page when about link is clicked', async () => {
    const user = userEvent.setup();
    renderWithRouter(<App />);
    
    const aboutLink = screen.getByRole('link', { name: /about/i });
    await user.click(aboutLink);
    
    expect(screen.getByText('About Us')).toBeInTheDocument();
  });
  
  test('renders user profile with correct user ID', () => {
    renderWithRouter(<App />, { initialEntries: ['/users/456'] });
    
    expect(screen.getByText('User ID: 456')).toBeInTheDocument();
  });
  
  test('redirects to 404 page for unknown routes', () => {
    renderWithRouter(<App />, { initialEntries: ['/unknown-route'] });
    
    expect(screen.getByText('Page Not Found')).toBeInTheDocument();
  });
  
  test('highlights active navigation link', () => {
    renderWithRouter(<App />, { initialEntries: ['/about'] });
    
    const aboutLink = screen.getByRole('link', { name: /about/i });
    expect(aboutLink).toHaveClass('active');
  });
});
```

**3. Testing Components with useNavigate:**

```jsx
// components/LoginForm.jsx
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function LoginForm() {
  const [credentials, setCredentials] = useState({ username: '', password: '' });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const navigate = useNavigate();
  
  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    
    try {
      const response = await fetch('/api/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(credentials)
      });
      
      if (!response.ok) {
        throw new Error('Invalid credentials');
      }
      
      const { token } = await response.json();
      localStorage.setItem('authToken', token);
      
      // Navigate to dashboard after successful login
      navigate('/dashboard');
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };
  
  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="username">Username:</label>
        <input
          id="username"
          type="text"
          value={credentials.username}
          onChange={(e) => setCredentials(prev => ({ ...prev, username: e.target.value }))}
          required
        />
      </div>
      <div>
        <label htmlFor="password">Password:</label>
        <input
          id="password"
          type="password"
          value={credentials.password}
          onChange={(e) => setCredentials(prev => ({ ...prev, password: e.target.value }))}
          required
        />
      </div>
      {error && <div role="alert">{error}</div>}
      <button type="submit" disabled={loading}>
        {loading ? 'Logging in...' : 'Login'}
      </button>
    </form>
  );
}

export default LoginForm;
```

```jsx
// LoginForm.test.jsx
import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { MemoryRouter } from 'react-router-dom';
import LoginForm from './LoginForm';

// Mock useNavigate
const mockNavigate = jest.fn();
jest.mock('react-router-dom', () => ({
  ...jest.requireActual('react-router-dom'),
  useNavigate: () => mockNavigate
}));

// Mock fetch
global.fetch = jest.fn();

function renderWithRouter(ui) {
  return render(
    <MemoryRouter>
      {ui}
    </MemoryRouter>
  );
}

describe('LoginForm', () => {
  beforeEach(() => {
    fetch.mockClear();
    mockNavigate.mockClear();
    localStorage.clear();
  });
  
  test('navigates to dashboard after successful login', async () => {
    const user = userEvent.setup();
    
    fetch.mockResolvedValueOnce({
      ok: true,
      json: async () => ({ token: 'fake-token' })
    });
    
    renderWithRouter(<LoginForm />);
    
    // Fill in the form
    await user.type(screen.getByLabelText(/username/i), 'testuser');
    await user.type(screen.getByLabelText(/password/i), 'password123');
    
    // Submit the form
    await user.click(screen.getByRole('button', { name: /login/i }));
    
    // Wait for navigation
    await waitFor(() => {
      expect(mockNavigate).toHaveBeenCalledWith('/dashboard');
    });
    
    // Check that token was stored
    expect(localStorage.getItem('authToken')).toBe('fake-token');
  });
  
  test('displays error message on failed login', async () => {
    const user = userEvent.setup();
    
    fetch.mockResolvedValueOnce({
      ok: false,
      status: 401
    });
    
    renderWithRouter(<LoginForm />);
    
    await user.type(screen.getByLabelText(/username/i), 'testuser');
    await user.type(screen.getByLabelText(/password/i), 'wrongpassword');
    await user.click(screen.getByRole('button', { name: /login/i }));
    
    await waitFor(() => {
      expect(screen.getByRole('alert')).toHaveTextContent('Invalid credentials');
    });
    
    // Should not navigate on error
    expect(mockNavigate).not.toHaveBeenCalled();
  });
});
```

**4. Testing Protected Routes:**

```jsx
// components/ProtectedRoute.jsx
import React from 'react';
import { Navigate, useLocation } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';

function ProtectedRoute({ children, requiredRole }) {
  const { user, loading } = useAuth();
  const location = useLocation();
  
  if (loading) {
    return <div>Loading...</div>;
  }
  
  if (!user) {
    // Redirect to login with return URL
    return <Navigate to="/login" state={{ from: location }} replace />;
  }
  
  if (requiredRole && !user.roles.includes(requiredRole)) {
    return <Navigate to="/unauthorized" replace />;
  }
  
  return children;
}

export default ProtectedRoute;
```

```jsx
// ProtectedRoute.test.jsx
import React from 'react';
import { render, screen } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import ProtectedRoute from './ProtectedRoute';
import { AuthProvider } from '../contexts/AuthContext';

// Mock the auth context
const mockAuthContext = {
  user: null,
  loading: false
};

jest.mock('../contexts/AuthContext', () => ({
  useAuth: () => mockAuthContext,
  AuthProvider: ({ children }) => children
}));

function TestComponent() {
  return <div>Protected Content</div>;
}

function renderWithRouter(ui, { initialEntries = ['/'] } = {}) {
  return render(
    <MemoryRouter initialEntries={initialEntries}>
      <AuthProvider>
        {ui}
      </AuthProvider>
    </MemoryRouter>
  );
}

describe('ProtectedRoute', () => {
  test('redirects to login when user is not authenticated', () => {
    mockAuthContext.user = null;
    mockAuthContext.loading = false;
    
    renderWithRouter(
      <ProtectedRoute>
        <TestComponent />
      </ProtectedRoute>
    );
    
    // Should not render protected content
    expect(screen.queryByText('Protected Content')).not.toBeInTheDocument();
  });
  
  test('renders children when user is authenticated', () => {
    mockAuthContext.user = { id: 1, name: 'John', roles: ['user'] };
    mockAuthContext.loading = false;
    
    renderWithRouter(
      <ProtectedRoute>
        <TestComponent />
      </ProtectedRoute>
    );
    
    expect(screen.getByText('Protected Content')).toBeInTheDocument();
  });
  
  test('redirects to unauthorized when user lacks required role', () => {
    mockAuthContext.user = { id: 1, name: 'John', roles: ['user'] };
    mockAuthContext.loading = false;
    
    renderWithRouter(
      <ProtectedRoute requiredRole="admin">
        <TestComponent />
      </ProtectedRoute>
    );
    
    expect(screen.queryByText('Protected Content')).not.toBeInTheDocument();
  });
  
  test('shows loading state while authentication is in progress', () => {
    mockAuthContext.user = null;
    mockAuthContext.loading = true;
    
    renderWithRouter(
      <ProtectedRoute>
        <TestComponent />
      </ProtectedRoute>
    );
    
    expect(screen.getByText('Loading...')).toBeInTheDocument();
    expect(screen.queryByText('Protected Content')).not.toBeInTheDocument();
  });
});
```

**5. Testing Route Parameters:**

```jsx
// pages/UserProfile.jsx
import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';

function UserProfile() {
  const { userId } = useParams();
  const navigate = useNavigate();
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    async function fetchUser() {
      try {
        const response = await fetch(`/api/users/${userId}`);
        if (!response.ok) {
          throw new Error('User not found');
        }
        const userData = await response.json();
        setUser(userData);
      } catch (error) {
        navigate('/404');
      } finally {
        setLoading(false);
      }
    }
    
    fetchUser();
  }, [userId, navigate]);
  
  if (loading) return <div>Loading user...</div>;
  
  return (
    <div>
      <h1>{user.name}</h1>
      <p>User ID: {userId}</p>
      <p>Email: {user.email}</p>
      <button onClick={() => navigate('/users')}>Back to Users</button>
    </div>
  );
}

export default UserProfile;
```

```jsx
// UserProfile.test.jsx
import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { MemoryRouter } from 'react-router-dom';
import UserProfile from './UserProfile';

const mockNavigate = jest.fn();
jest.mock('react-router-dom', () => ({
  ...jest.requireActual('react-router-dom'),
  useNavigate: () => mockNavigate
}));

global.fetch = jest.fn();

function renderWithRouter(ui, { route = '/users/123' } = {}) {
  return render(
    <MemoryRouter initialEntries={[route]}>
      {ui}
    </MemoryRouter>
  );
}

describe('UserProfile', () => {
  beforeEach(() => {
    fetch.mockClear();
    mockNavigate.mockClear();
  });
  
  test('displays user information with correct user ID', async () => {
    const mockUser = {
      id: 123,
      name: 'John Doe',
      email: 'john@example.com'
    };
    
    fetch.mockResolvedValueOnce({
      ok: true,
      json: async () => mockUser
    });
    
    renderWithRouter(<UserProfile />, { route: '/users/123' });
    
    await waitFor(() => {
      expect(screen.getByText('John Doe')).toBeInTheDocument();
    });
    
    expect(screen.getByText('User ID: 123')).toBeInTheDocument();
    expect(screen.getByText('Email: john@example.com')).toBeInTheDocument();
  });
  
  test('navigates to 404 when user is not found', async () => {
    fetch.mockResolvedValueOnce({
      ok: false,
      status: 404
    });
    
    renderWithRouter(<UserProfile />, { route: '/users/999' });
    
    await waitFor(() => {
      expect(mockNavigate).toHaveBeenCalledWith('/404');
    });
  });
  
  test('navigates back to users list when back button is clicked', async () => {
    const user = userEvent.setup();
    const mockUser = { id: 123, name: 'John Doe', email: 'john@example.com' };
    
    fetch.mockResolvedValueOnce({
      ok: true,
      json: async () => mockUser
    });
    
    renderWithRouter(<UserProfile />);
    
    await waitFor(() => {
      expect(screen.getByText('John Doe')).toBeInTheDocument();
    });
    
    const backButton = screen.getByRole('button', { name: /back to users/i });
    await user.click(backButton);
    
    expect(mockNavigate).toHaveBeenCalledWith('/users');
  });
});
```

**Best Practices for Testing React Router:**

1. **Use MemoryRouter for tests**: More predictable than BrowserRouter
2. **Test navigation behavior**: Verify that navigation happens correctly
3. **Test route parameters**: Ensure components handle params properly
4. **Mock useNavigate**: Control navigation in tests
5. **Test protected routes**: Verify authentication and authorization
6. **Test error scenarios**: Handle 404s and navigation errors
7. **Use helper functions**: Create reusable render functions with router
8. **Test active states**: Verify navigation highlighting works correctly

---

## Modern React Features

### Q14: How do you implement React Suspense and Concurrent Features?

**Difficulty: Advanced**

**Answer:**
React Suspense and Concurrent Features enable better user experiences through progressive loading, time slicing, and priority-based rendering. These features help create more responsive applications.

**1. Basic Suspense for Code Splitting:**

```jsx
// App.jsx
import React, { Suspense, lazy } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LoadingSpinner from './components/LoadingSpinner';
import ErrorBoundary from './components/ErrorBoundary';

// Lazy load components
const HomePage = lazy(() => import('./pages/HomePage'));
const AboutPage = lazy(() => import('./pages/AboutPage'));
const UserDashboard = lazy(() => import('./pages/UserDashboard'));
const AdminPanel = lazy(() => import('./pages/AdminPanel'));

function App() {
  return (
    <Router>
      <div className="app">
        <ErrorBoundary>
          <Suspense fallback={<LoadingSpinner />}>
            <Routes>
              <Route path="/" element={<HomePage />} />
              <Route path="/about" element={<AboutPage />} />
              <Route path="/dashboard" element={<UserDashboard />} />
              <Route path="/admin" element={<AdminPanel />} />
            </Routes>
          </Suspense>
        </ErrorBoundary>
      </div>
    </Router>
  );
}

export default App;
```

```jsx
// components/LoadingSpinner.jsx
import React from 'react';

function LoadingSpinner({ message = 'Loading...' }) {
  return (
    <div className="loading-container">
      <div className="spinner" />
      <p>{message}</p>
    </div>
  );
}

export default LoadingSpinner;
```

**2. Suspense for Data Fetching:**

```jsx
// hooks/useSuspenseQuery.js
import { useMemo } from 'react';

// Simple cache for demonstration
const cache = new Map();

function createSuspenseResource(promise, key) {
  let status = 'pending';
  let result;
  
  const suspender = promise.then(
    (data) => {
      status = 'success';
      result = data;
    },
    (error) => {
      status = 'error';
      result = error;
    }
  );
  
  return {
    read() {
      if (status === 'pending') {
        throw suspender;
      } else if (status === 'error') {
        throw result;
      } else if (status === 'success') {
        return result;
      }
    }
  };
}

export function useSuspenseQuery(url, options = {}) {
  const resource = useMemo(() => {
    const cacheKey = `${url}-${JSON.stringify(options)}`;
    
    if (cache.has(cacheKey)) {
      return cache.get(cacheKey);
    }
    
    const promise = fetch(url, options)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }
        return response.json();
      });
    
    const resource = createSuspenseResource(promise, cacheKey);
    cache.set(cacheKey, resource);
    
    return resource;
  }, [url, options]);
  
  return resource.read();
}
```

```jsx
// components/UserProfile.jsx
import React, { Suspense } from 'react';
import { useSuspenseQuery } from '../hooks/useSuspenseQuery';
import LoadingSpinner from './LoadingSpinner';
import ErrorBoundary from './ErrorBoundary';

function UserProfileData({ userId }) {
  const user = useSuspenseQuery(`/api/users/${userId}`);
  const posts = useSuspenseQuery(`/api/users/${userId}/posts`);
  
  return (
    <div className="user-profile">
      <div className="user-info">
        <img src={user.avatar} alt={`${user.name}'s avatar`} />
        <h1>{user.name}</h1>
        <p>{user.email}</p>
        <p>Joined: {new Date(user.createdAt).toLocaleDateString()}</p>
      </div>
      
      <div className="user-posts">
        <h2>Recent Posts ({posts.length})</h2>
        {posts.map(post => (
          <article key={post.id} className="post">
            <h3>{post.title}</h3>
            <p>{post.excerpt}</p>
            <time>{new Date(post.createdAt).toLocaleDateString()}</time>
          </article>
        ))}
      </div>
    </div>
  );
}

function UserProfile({ userId }) {
  return (
    <ErrorBoundary>
      <Suspense fallback={<LoadingSpinner message="Loading user profile..." />}>
        <UserProfileData userId={userId} />
      </Suspense>
    </ErrorBoundary>
  );
}

export default UserProfile;
```

**3. Nested Suspense Boundaries:**

```jsx
// components/Dashboard.jsx
import React, { Suspense } from 'react';
import { useSuspenseQuery } from '../hooks/useSuspenseQuery';
import LoadingSpinner from './LoadingSpinner';
import ErrorBoundary from './ErrorBoundary';

function UserStats({ userId }) {
  const stats = useSuspenseQuery(`/api/users/${userId}/stats`);
  
  return (
    <div className="user-stats">
      <div className="stat">
        <h3>Posts</h3>
        <span>{stats.postsCount}</span>
      </div>
      <div className="stat">
        <h3>Followers</h3>
        <span>{stats.followersCount}</span>
      </div>
      <div className="stat">
        <h3>Following</h3>
        <span>{stats.followingCount}</span>
      </div>
    </div>
  );
}

function RecentActivity({ userId }) {
  const activities = useSuspenseQuery(`/api/users/${userId}/activities`);
  
  return (
    <div className="recent-activity">
      <h3>Recent Activity</h3>
      <ul>
        {activities.map(activity => (
          <li key={activity.id}>
            <span className="activity-type">{activity.type}</span>
            <span className="activity-description">{activity.description}</span>
            <time>{new Date(activity.timestamp).toLocaleString()}</time>
          </li>
        ))}
      </ul>
    </div>
  );
}

function Notifications({ userId }) {
  const notifications = useSuspenseQuery(`/api/users/${userId}/notifications`);
  
  return (
    <div className="notifications">
      <h3>Notifications ({notifications.unreadCount})</h3>
      <ul>
        {notifications.items.map(notification => (
          <li key={notification.id} className={notification.read ? 'read' : 'unread'}>
            <p>{notification.message}</p>
            <time>{new Date(notification.createdAt).toLocaleString()}</time>
          </li>
        ))}
      </ul>
    </div>
  );
}

function Dashboard({ userId }) {
  return (
    <div className="dashboard">
      <h1>Dashboard</h1>
      
      {/* Fast-loading stats */}
      <ErrorBoundary>
        <Suspense fallback={<div className="stats-skeleton">Loading stats...</div>}>
          <UserStats userId={userId} />
        </Suspense>
      </ErrorBoundary>
      
      <div className="dashboard-content">
        {/* Medium-loading activity */}
        <ErrorBoundary>
          <Suspense fallback={<div className="activity-skeleton">Loading activity...</div>}>
            <RecentActivity userId={userId} />
          </Suspense>
        </ErrorBoundary>
        
        {/* Slow-loading notifications */}
        <ErrorBoundary>
          <Suspense fallback={<div className="notifications-skeleton">Loading notifications...</div>}>
            <Notifications userId={userId} />
          </Suspense>
        </ErrorBoundary>
      </div>
    </div>
  );
}

export default Dashboard;
```

**4. Concurrent Features with useTransition:**

```jsx
// components/SearchableList.jsx
import React, { useState, useTransition, useDeferredValue, useMemo } from 'react';

function SearchableList({ items, searchFields = ['name'] }) {
  const [query, setQuery] = useState('');
  const [isPending, startTransition] = useTransition();
  const deferredQuery = useDeferredValue(query);
  
  // Expensive filtering operation
  const filteredItems = useMemo(() => {
    if (!deferredQuery) return items;
    
    return items.filter(item => 
      searchFields.some(field => 
        item[field]?.toLowerCase().includes(deferredQuery.toLowerCase())
      )
    );
  }, [items, deferredQuery, searchFields]);
  
  const handleSearchChange = (e) => {
    const value = e.target.value;
    
    // Update input immediately for responsiveness
    setQuery(value);
    
    // Defer the expensive filtering operation
    startTransition(() => {
      // This will trigger the useMemo recalculation
      // but won't block the input update
    });
  };
  
  return (
    <div className="searchable-list">
      <div className="search-container">
        <input
          type="text"
          placeholder="Search items..."
          value={query}
          onChange={handleSearchChange}
          className="search-input"
        />
        {isPending && <span className="search-loading">Searching...</span>}
      </div>
      
      <div className="results-container">
        <p className="results-count">
          {filteredItems.length} of {items.length} items
          {isPending && ' (updating...)'}
        </p>
        
        <ul className={`items-list ${isPending ? 'updating' : ''}`}>
          {filteredItems.map(item => (
            <li key={item.id} className="item">
              <h3>{item.name}</h3>
              <p>{item.description}</p>
              <span className="item-category">{item.category}</span>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default SearchableList;
```

**5. Advanced Concurrent Patterns:**

```jsx
// hooks/useConcurrentState.js
import { useState, useTransition, useCallback } from 'react';

export function useConcurrentState(initialState) {
  const [state, setState] = useState(initialState);
  const [isPending, startTransition] = useTransition();
  
  const setConcurrentState = useCallback((newState) => {
    startTransition(() => {
      setState(newState);
    });
  }, []);
  
  return [state, setConcurrentState, isPending];
}
```

```jsx
// components/DataVisualization.jsx
import React, { useState, useMemo, useTransition } from 'react';
import { useConcurrentState } from '../hooks/useConcurrentState';

function DataVisualization({ data }) {
  const [viewType, setViewType] = useState('chart');
  const [filters, setFilters, isFiltersPending] = useConcurrentState({
    category: 'all',
    dateRange: 'last30days',
    sortBy: 'date'
  });
  const [isPending, startTransition] = useTransition();
  
  // Expensive data processing
  const processedData = useMemo(() => {
    console.log('Processing data...'); // This is expensive
    
    let filtered = data;
    
    if (filters.category !== 'all') {
      filtered = filtered.filter(item => item.category === filters.category);
    }
    
    if (filters.dateRange !== 'all') {
      const days = parseInt(filters.dateRange.replace('last', '').replace('days', ''));
      const cutoff = new Date(Date.now() - days * 24 * 60 * 60 * 1000);
      filtered = filtered.filter(item => new Date(item.date) >= cutoff);
    }
    
    // Sort data
    filtered.sort((a, b) => {
      if (filters.sortBy === 'date') {
        return new Date(b.date) - new Date(a.date);
      }
      return b.value - a.value;
    });
    
    return filtered;
  }, [data, filters]);
  
  const handleViewChange = (newViewType) => {
    startTransition(() => {
      setViewType(newViewType);
    });
  };
  
  const handleFilterChange = (filterKey, value) => {
    setFilters(prev => ({
      ...prev,
      [filterKey]: value
    }));
  };
  
  return (
    <div className="data-visualization">
      <div className="controls">
        <div className="view-controls">
          <button 
            onClick={() => handleViewChange('chart')}
            className={viewType === 'chart' ? 'active' : ''}
            disabled={isPending}
          >
            Chart View
          </button>
          <button 
            onClick={() => handleViewChange('table')}
            className={viewType === 'table' ? 'active' : ''}
            disabled={isPending}
          >
            Table View
          </button>
          <button 
            onClick={() => handleViewChange('grid')}
            className={viewType === 'grid' ? 'active' : ''}
            disabled={isPending}
          >
            Grid View
          </button>
        </div>
        
        <div className="filter-controls">
          <select 
            value={filters.category}
            onChange={(e) => handleFilterChange('category', e.target.value)}
            disabled={isFiltersPending}
          >
            <option value="all">All Categories</option>
            <option value="sales">Sales</option>
            <option value="marketing">Marketing</option>
            <option value="support">Support</option>
          </select>
          
          <select 
            value={filters.dateRange}
            onChange={(e) => handleFilterChange('dateRange', e.target.value)}
            disabled={isFiltersPending}
          >
            <option value="last7days">Last 7 Days</option>
            <option value="last30days">Last 30 Days</option>
            <option value="last90days">Last 90 Days</option>
            <option value="all">All Time</option>
          </select>
          
          <select 
            value={filters.sortBy}
            onChange={(e) => handleFilterChange('sortBy', e.target.value)}
            disabled={isFiltersPending}
          >
            <option value="date">Sort by Date</option>
            <option value="value">Sort by Value</option>
          </select>
        </div>
        
        {(isPending || isFiltersPending) && (
          <div className="loading-indicator">Updating...</div>
        )}
      </div>
      
      <div className={`visualization-content ${isPending ? 'updating' : ''}`}>
        {viewType === 'chart' && <ChartView data={processedData} />}
        {viewType === 'table' && <TableView data={processedData} />}
        {viewType === 'grid' && <GridView data={processedData} />}
      </div>
      
      <div className="data-summary">
        <p>Showing {processedData.length} items</p>
        {isFiltersPending && <span>(filters updating...)</span>}
      </div>
    </div>
  );
}

// Placeholder components
function ChartView({ data }) {
  return <div className="chart-view">Chart with {data.length} items</div>;
}

function TableView({ data }) {
  return <div className="table-view">Table with {data.length} items</div>;
}

function GridView({ data }) {
  return <div className="grid-view">Grid with {data.length} items</div>;
}

export default DataVisualization;
```

**6. Suspense with Error Boundaries:**

```jsx
// components/SuspenseErrorBoundary.jsx
import React from 'react';

class SuspenseErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }
  
  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }
  
  componentDidCatch(error, errorInfo) {
    console.error('Suspense Error Boundary caught an error:', error, errorInfo);
    
    // Log to error reporting service
    if (this.props.onError) {
      this.props.onError(error, errorInfo);
    }
  }
  
  render() {
    if (this.state.hasError) {
      if (this.props.fallback) {
        return this.props.fallback(this.state.error);
      }
      
      return (
        <div className="error-boundary">
          <h2>Something went wrong</h2>
          <p>{this.state.error?.message}</p>
          <button onClick={() => this.setState({ hasError: false, error: null })}>
            Try Again
          </button>
        </div>
      );
    }
    
    return this.props.children;
  }
}

export default SuspenseErrorBoundary;
```

**Best Practices:**

1. **Use Suspense boundaries strategically**: Place them where loading states make sense
2. **Combine with Error Boundaries**: Always wrap Suspense in error boundaries
3. **Optimize with useTransition**: Use for non-urgent updates
4. **Leverage useDeferredValue**: For expensive computations that can be delayed
5. **Progressive loading**: Load critical content first, defer secondary content
6. **Cache resources**: Implement proper caching to avoid redundant requests
7. **Provide meaningful fallbacks**: Show relevant loading states
8. **Test concurrent behavior**: Ensure your app works correctly with time slicing

---

### Q15: How do you implement custom React hooks for complex state management?

**Difficulty: Advanced**

**Answer:**
Custom hooks allow you to extract and reuse stateful logic across components. They're essential for managing complex state patterns, side effects, and creating reusable abstractions.

**1. Advanced State Management Hook:**

```jsx
// hooks/useAdvancedState.js
import { useReducer, useCallback, useMemo } from 'react';

// Action types
const ACTIONS = {
  SET: 'SET',
  UPDATE: 'UPDATE',
  RESET: 'RESET',
  MERGE: 'MERGE',
  DELETE_KEY: 'DELETE_KEY',
  UNDO: 'UNDO',
  REDO: 'REDO'
};

// Reducer function
function advancedStateReducer(state, action) {
  switch (action.type) {
    case ACTIONS.SET:
      return {
        ...state,
        present: action.payload,
        past: [...state.past, state.present],
        future: []
      };
      
    case ACTIONS.UPDATE:
      const newState = typeof action.payload === 'function' 
        ? action.payload(state.present)
        : action.payload;
      return {
        ...state,
        present: newState,
        past: [...state.past, state.present],
        future: []
      };
      
    case ACTIONS.MERGE:
      return {
        ...state,
        present: { ...state.present, ...action.payload },
        past: [...state.past, state.present],
        future: []
      };
      
    case ACTIONS.DELETE_KEY:
      const { [action.payload]: deleted, ...rest } = state.present;
      return {
        ...state,
        present: rest,
        past: [...state.past, state.present],
        future: []
      };
      
    case ACTIONS.RESET:
      return {
        present: action.payload || state.initial,
        past: [],
        future: [],
        initial: state.initial
      };
      
    case ACTIONS.UNDO:
      if (state.past.length === 0) return state;
      const previous = state.past[state.past.length - 1];
      const newPast = state.past.slice(0, state.past.length - 1);
      return {
        ...state,
        present: previous,
        past: newPast,
        future: [state.present, ...state.future]
      };
      
    case ACTIONS.REDO:
      if (state.future.length === 0) return state;
      const next = state.future[0];
      const newFuture = state.future.slice(1);
      return {
        ...state,
        present: next,
        past: [...state.past, state.present],
        future: newFuture
      };
      
    default:
      return state;
  }
}

export function useAdvancedState(initialState) {
  const [state, dispatch] = useReducer(advancedStateReducer, {
    present: initialState,
    past: [],
    future: [],
    initial: initialState
  });
  
  const actions = useMemo(() => ({
    set: (value) => dispatch({ type: ACTIONS.SET, payload: value }),
    update: (updater) => dispatch({ type: ACTIONS.UPDATE, payload: updater }),
    merge: (partial) => dispatch({ type: ACTIONS.MERGE, payload: partial }),
    deleteKey: (key) => dispatch({ type: ACTIONS.DELETE_KEY, payload: key }),
    reset: (newInitial) => dispatch({ type: ACTIONS.RESET, payload: newInitial }),
    undo: () => dispatch({ type: ACTIONS.UNDO }),
    redo: () => dispatch({ type: ACTIONS.REDO })
  }), []);
  
  const canUndo = state.past.length > 0;
  const canRedo = state.future.length > 0;
  
  return {
    state: state.present,
    actions,
    canUndo,
    canRedo,
    history: {
      past: state.past,
      future: state.future
    }
  };
}
```

**2. Async State Management Hook:**

```jsx
// hooks/useAsyncState.js
import { useReducer, useCallback, useRef, useEffect } from 'react';

const ASYNC_ACTIONS = {
  LOADING: 'LOADING',
  SUCCESS: 'SUCCESS',
  ERROR: 'ERROR',
  RESET: 'RESET'
};

function asyncStateReducer(state, action) {
  switch (action.type) {
    case ASYNC_ACTIONS.LOADING:
      return {
        ...state,
        loading: true,
        error: null
      };
      
    case ASYNC_ACTIONS.SUCCESS:
      return {
        ...state,
        loading: false,
        data: action.payload,
        error: null,
        lastFetch: Date.now()
      };
      
    case ASYNC_ACTIONS.ERROR:
      return {
        ...state,
        loading: false,
        error: action.payload,
        data: state.keepDataOnError ? state.data : null
      };
      
    case ASYNC_ACTIONS.RESET:
      return {
        data: null,
        loading: false,
        error: null,
        lastFetch: null,
        keepDataOnError: state.keepDataOnError
      };
      
    default:
      return state;
  }
}

export function useAsyncState(options = {}) {
  const {
    keepDataOnError = false,
    retryAttempts = 3,
    retryDelay = 1000,
    cacheTime = 5 * 60 * 1000 // 5 minutes
  } = options;
  
  const [state, dispatch] = useReducer(asyncStateReducer, {
    data: null,
    loading: false,
    error: null,
    lastFetch: null,
    keepDataOnError
  });
  
  const abortControllerRef = useRef(null);
  const retryCountRef = useRef(0);
  
  const execute = useCallback(async (asyncFunction, ...args) => {
    // Cancel previous request
    if (abortControllerRef.current) {
      abortControllerRef.current.abort();
    }
    
    // Create new abort controller
    abortControllerRef.current = new AbortController();
    const { signal } = abortControllerRef.current;
    
    dispatch({ type: ASYNC_ACTIONS.LOADING });
    
    const attemptRequest = async (attempt = 0) => {
      try {
        const result = await asyncFunction(signal, ...args);
        
        if (!signal.aborted) {
          dispatch({ type: ASYNC_ACTIONS.SUCCESS, payload: result });
          retryCountRef.current = 0;
        }
        
        return result;
      } catch (error) {
        if (signal.aborted) {
          return;
        }
        
        if (attempt < retryAttempts && !error.name === 'AbortError') {
          retryCountRef.current = attempt + 1;
          
          // Wait before retrying
          await new Promise(resolve => 
            setTimeout(resolve, retryDelay * Math.pow(2, attempt))
          );
          
          if (!signal.aborted) {
            return attemptRequest(attempt + 1);
          }
        } else {
          dispatch({ type: ASYNC_ACTIONS.ERROR, payload: error });
          retryCountRef.current = 0;
          throw error;
        }
      }
    };
    
    return attemptRequest();
  }, [retryAttempts, retryDelay]);
  
  const reset = useCallback(() => {
    if (abortControllerRef.current) {
      abortControllerRef.current.abort();
    }
    dispatch({ type: ASYNC_ACTIONS.RESET });
    retryCountRef.current = 0;
  }, []);
  
  const isStale = useCallback(() => {
    if (!state.lastFetch) return true;
    return Date.now() - state.lastFetch > cacheTime;
  }, [state.lastFetch, cacheTime]);
  
  // Cleanup on unmount
  useEffect(() => {
    return () => {
      if (abortControllerRef.current) {
        abortControllerRef.current.abort();
      }
    };
  }, []);
  
  return {
    ...state,
    execute,
    reset,
    isStale,
    retryCount: retryCountRef.current
  };
}
```

**3. Form Management Hook:**

```jsx
// hooks/useForm.js
import { useState, useCallback, useMemo } from 'react';

export function useForm(initialValues = {}, validationSchema = {}) {
  const [values, setValues] = useState(initialValues);
  const [errors, setErrors] = useState({});
  const [touched, setTouched] = useState({});
  const [isSubmitting, setIsSubmitting] = useState(false);
  
  // Validation function
  const validateField = useCallback((name, value) => {
    const validator = validationSchema[name];
    if (!validator) return null;
    
    if (typeof validator === 'function') {
      return validator(value, values);
    }
    
    if (validator.required && (!value || value.toString().trim() === '')) {
      return validator.message || `${name} is required`;
    }
    
    if (validator.minLength && value.length < validator.minLength) {
      return validator.message || `${name} must be at least ${validator.minLength} characters`;
    }
    
    if (validator.maxLength && value.length > validator.maxLength) {
      return validator.message || `${name} must be no more than ${validator.maxLength} characters`;
    }
    
    if (validator.pattern && !validator.pattern.test(value)) {
      return validator.message || `${name} format is invalid`;
    }
    
    if (validator.custom) {
      return validator.custom(value, values);
    }
    
    return null;
  }, [validationSchema, values]);
  
  // Validate all fields
  const validateAll = useCallback(() => {
    const newErrors = {};
    
    Object.keys(validationSchema).forEach(name => {
      const error = validateField(name, values[name]);
      if (error) {
        newErrors[name] = error;
      }
    });
    
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  }, [validateField, values, validationSchema]);
  
  // Handle field change
  const handleChange = useCallback((name, value) => {
    setValues(prev => ({ ...prev, [name]: value }));
    
    // Validate field if it's been touched
    if (touched[name]) {
      const error = validateField(name, value);
      setErrors(prev => ({
        ...prev,
        [name]: error
      }));
    }
  }, [validateField, touched]);
  
  // Handle field blur
  const handleBlur = useCallback((name) => {
    setTouched(prev => ({ ...prev, [name]: true }));
    
    const error = validateField(name, values[name]);
    setErrors(prev => ({
      ...prev,
      [name]: error
    }));
  }, [validateField, values]);
  
  // Handle form submission
  const handleSubmit = useCallback(async (onSubmit) => {
    setIsSubmitting(true);
    
    // Mark all fields as touched
    const allTouched = Object.keys(validationSchema).reduce((acc, key) => {
      acc[key] = true;
      return acc;
    }, {});
    setTouched(allTouched);
    
    // Validate all fields
    const isValid = validateAll();
    
    if (isValid) {
      try {
        await onSubmit(values);
      } catch (error) {
        console.error('Form submission error:', error);
      }
    }
    
    setIsSubmitting(false);
    return isValid;
  }, [values, validateAll, validationSchema]);
  
  // Reset form
  const reset = useCallback((newValues = initialValues) => {
    setValues(newValues);
    setErrors({});
    setTouched({});
    setIsSubmitting(false);
  }, [initialValues]);
  
  // Set field error manually
  const setFieldError = useCallback((name, error) => {
    setErrors(prev => ({ ...prev, [name]: error }));
  }, []);
  
  // Set multiple field errors
  const setFieldErrors = useCallback((errorObj) => {
    setErrors(prev => ({ ...prev, ...errorObj }));
  }, []);
  
  // Get field props for easy integration
  const getFieldProps = useCallback((name) => ({
    value: values[name] || '',
    onChange: (e) => handleChange(name, e.target.value),
    onBlur: () => handleBlur(name),
    error: errors[name],
    touched: touched[name]
  }), [values, handleChange, handleBlur, errors, touched]);
  
  // Computed properties
  const isValid = useMemo(() => Object.keys(errors).length === 0, [errors]);
  const isDirty = useMemo(() => 
    JSON.stringify(values) !== JSON.stringify(initialValues), 
    [values, initialValues]
  );
  
  return {
    values,
    errors,
    touched,
    isSubmitting,
    isValid,
    isDirty,
    handleChange,
    handleBlur,
    handleSubmit,
    reset,
    setFieldError,
    setFieldErrors,
    getFieldProps,
    validateAll
  };
}
```

**4. Local Storage Sync Hook:**

```jsx
// hooks/useLocalStorage.js
import { useState, useEffect, useCallback } from 'react';

export function useLocalStorage(key, initialValue, options = {}) {
  const {
    serialize = JSON.stringify,
    deserialize = JSON.parse,
    syncAcrossTabs = true
  } = options;
  
  // Get initial value from localStorage or use provided initial value
  const [storedValue, setStoredValue] = useState(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? deserialize(item) : initialValue;
    } catch (error) {
      console.warn(`Error reading localStorage key "${key}":`, error);
      return initialValue;
    }
  });
  
  // Update localStorage when state changes
  const setValue = useCallback((value) => {
    try {
      // Allow value to be a function so we have the same API as useState
      const valueToStore = value instanceof Function ? value(storedValue) : value;
      
      setStoredValue(valueToStore);
      
      if (valueToStore === undefined) {
        window.localStorage.removeItem(key);
      } else {
        window.localStorage.setItem(key, serialize(valueToStore));
      }
      
      // Dispatch custom event for cross-tab synchronization
      if (syncAcrossTabs) {
        window.dispatchEvent(new CustomEvent('local-storage-change', {
          detail: { key, value: valueToStore }
        }));
      }
    } catch (error) {
      console.warn(`Error setting localStorage key "${key}":`, error);
    }
  }, [key, serialize, storedValue, syncAcrossTabs]);
  
  // Listen for changes in localStorage (for cross-tab synchronization)
  useEffect(() => {
    if (!syncAcrossTabs) return;
    
    const handleStorageChange = (e) => {
      if (e.key === key && e.newValue !== null) {
        try {
          setStoredValue(deserialize(e.newValue));
        } catch (error) {
          console.warn(`Error deserializing localStorage key "${key}":`, error);
        }
      }
    };
    
    const handleCustomStorageChange = (e) => {
      if (e.detail.key === key) {
        setStoredValue(e.detail.value);
      }
    };
    
    window.addEventListener('storage', handleStorageChange);
    window.addEventListener('local-storage-change', handleCustomStorageChange);
    
    return () => {
      window.removeEventListener('storage', handleStorageChange);
      window.removeEventListener('local-storage-change', handleCustomStorageChange);
    };
  }, [key, deserialize, syncAcrossTabs]);
  
  // Remove item from localStorage
  const removeValue = useCallback(() => {
    setValue(undefined);
  }, [setValue]);
  
  return [storedValue, setValue, removeValue];
}
```

**5. Debounced State Hook:**

```jsx
// hooks/useDebounce.js
import { useState, useEffect, useRef, useCallback } from 'react';

export function useDebounce(value, delay, options = {}) {
  const { leading = false, trailing = true, maxWait } = options;
  const [debouncedValue, setDebouncedValue] = useState(value);
  const timeoutRef = useRef(null);
  const maxTimeoutRef = useRef(null);
  const lastCallTimeRef = useRef(null);
  const lastInvokeTimeRef = useRef(0);
  
  const invokeFunc = useCallback(() => {
    setDebouncedValue(value);
    lastInvokeTimeRef.current = Date.now();
  }, [value]);
  
  const leadingEdge = useCallback(() => {
    lastInvokeTimeRef.current = Date.now();
    if (leading) {
      invokeFunc();
    }
  }, [leading, invokeFunc]);
  
  const trailingEdge = useCallback(() => {
    timeoutRef.current = null;
    if (trailing && lastCallTimeRef.current) {
      invokeFunc();
    }
  }, [trailing, invokeFunc]);
  
  const timedOut = useCallback(() => {
    const timeSinceLastCall = Date.now() - lastCallTimeRef.current;
    
    if (timeSinceLastCall < delay) {
      timeoutRef.current = setTimeout(timedOut, delay - timeSinceLastCall);
    } else {
      trailingEdge();
    }
  }, [delay, trailingEdge]);
  
  useEffect(() => {
    lastCallTimeRef.current = Date.now();
    
    const timeSinceLastInvoke = lastCallTimeRef.current - lastInvokeTimeRef.current;
    
    if (!timeoutRef.current) {
      leadingEdge();
    }
    
    // Clear existing timeout
    if (timeoutRef.current) {
      clearTimeout(timeoutRef.current);
    }
    
    // Clear max timeout
    if (maxTimeoutRef.current) {
      clearTimeout(maxTimeoutRef.current);
    }
    
    // Set new timeout
    timeoutRef.current = setTimeout(timedOut, delay);
    
    // Set max wait timeout if specified
    if (maxWait && timeSinceLastInvoke >= maxWait) {
      invokeFunc();
    } else if (maxWait) {
      maxTimeoutRef.current = setTimeout(invokeFunc, maxWait - timeSinceLastInvoke);
    }
    
    return () => {
      if (timeoutRef.current) {
        clearTimeout(timeoutRef.current);
      }
      if (maxTimeoutRef.current) {
        clearTimeout(maxTimeoutRef.current);
      }
    };
  }, [value, delay, maxWait, leadingEdge, timedOut, invokeFunc]);
  
  const cancel = useCallback(() => {
    if (timeoutRef.current) {
      clearTimeout(timeoutRef.current);
      timeoutRef.current = null;
    }
    if (maxTimeoutRef.current) {
      clearTimeout(maxTimeoutRef.current);
      maxTimeoutRef.current = null;
    }
    lastCallTimeRef.current = null;
  }, []);
  
  const flush = useCallback(() => {
    if (timeoutRef.current) {
      clearTimeout(timeoutRef.current);
      trailingEdge();
    }
  }, [trailingEdge]);
  
  return {
    debouncedValue,
    cancel,
    flush
  };
}

// Simpler version for basic use cases
export function useSimpleDebounce(value, delay) {
  const [debouncedValue, setDebouncedValue] = useState(value);
  
  useEffect(() => {
    const handler = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);
    
    return () => {
      clearTimeout(handler);
    };
  }, [value, delay]);
  
  return debouncedValue;
}
```

**6. Usage Examples:**

```jsx
// Example: Using the advanced state hook
function TodoApp() {
  const { state: todos, actions, canUndo, canRedo } = useAdvancedState([]);
  
  const addTodo = (text) => {
    actions.update(prev => [...prev, {
      id: Date.now(),
      text,
      completed: false
    }]);
  };
  
  const toggleTodo = (id) => {
    actions.update(prev => prev.map(todo => 
      todo.id === id ? { ...todo, completed: !todo.completed } : todo
    ));
  };
  
  return (
    <div>
      <div>
        <button onClick={actions.undo} disabled={!canUndo}>Undo</button>
        <button onClick={actions.redo} disabled={!canRedo}>Redo</button>
        <button onClick={() => actions.reset([])}>Clear All</button>
      </div>
      {/* Todo list implementation */}
    </div>
  );
}

// Example: Using the form hook
function ContactForm() {
  const form = useForm(
    { name: '', email: '', message: '' },
    {
      name: { required: true, minLength: 2 },
      email: { 
        required: true, 
        pattern: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
        message: 'Please enter a valid email'
      },
      message: { required: true, minLength: 10 }
    }
  );
  
  const handleSubmit = async (values) => {
    await fetch('/api/contact', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(values)
    });
  };
  
  return (
    <form onSubmit={(e) => {
      e.preventDefault();
      form.handleSubmit(handleSubmit);
    }}>
      <input {...form.getFieldProps('name')} placeholder="Name" />
      <input {...form.getFieldProps('email')} placeholder="Email" />
      <textarea {...form.getFieldProps('message')} placeholder="Message" />
      <button type="submit" disabled={!form.isValid || form.isSubmitting}>
        {form.isSubmitting ? 'Sending...' : 'Send'}
      </button>
    </form>
  );
}
```

**Best Practices:**

1. **Keep hooks focused**: Each hook should have a single responsibility
2. **Use useCallback and useMemo**: Optimize performance for complex hooks
3. **Handle cleanup**: Always clean up side effects in useEffect
4. **Provide good APIs**: Make hooks easy to use with clear return values
5. **Add TypeScript**: Type your hooks for better developer experience
6. **Test thoroughly**: Write comprehensive tests for custom hooks
7. **Document well**: Provide clear documentation and examples
8. **Consider composition**: Build complex hooks from simpler ones

---

### Q16: How do you implement React Server Components and streaming SSR?

**Difficulty: Expert**

**Answer:**
React Server Components (RSC) and streaming SSR represent the cutting edge of React performance optimization, enabling server-side rendering with component-level granularity and progressive hydration.

**1. Basic Server Component Setup:**

```jsx
// app/layout.js (App Router)
import { Inter } from 'next/font/google';
import './globals.css';

const inter = Inter({ subsets: ['latin'] });

export const metadata = {
  title: 'React Server Components Demo',
  description: 'Advanced SSR with streaming'
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <nav className="navbar">
          <h1>My App</h1>
        </nav>
        <main>{children}</main>
      </body>
    </html>
  );
}
```

```jsx
// app/page.js (Server Component)
import { Suspense } from 'react';
import UserProfile from './components/UserProfile';
import PostsList from './components/PostsList';
import Sidebar from './components/Sidebar';
import LoadingSpinner from './components/LoadingSpinner';

// This is a Server Component by default
export default async function HomePage() {
  // Server-side data fetching
  const initialData = await fetch('https://api.example.com/initial-data', {
    cache: 'force-cache' // Next.js caching
  }).then(res => res.json());

  return (
    <div className="home-page">
      <div className="main-content">
        <h1>Welcome to {initialData.siteName}</h1>
        
        {/* Streaming different components */}
        <Suspense fallback={<LoadingSpinner message="Loading user profile..." />}>
          <UserProfile userId={initialData.userId} />
        </Suspense>
        
        <Suspense fallback={<div className="posts-skeleton">Loading posts...</div>}>
          <PostsList category={initialData.defaultCategory} />
        </Suspense>
      </div>
      
      <aside className="sidebar">
        <Suspense fallback={<div className="sidebar-skeleton">Loading sidebar...</div>}>
          <Sidebar userId={initialData.userId} />
        </Suspense>
      </aside>
    </div>
  );
}
```

**2. Server Components with Database Integration:**

```jsx
// app/components/UserProfile.js (Server Component)
import { db } from '../lib/database';
import { cache } from 'react';
import Image from 'next/image';

// Cache the database query
const getUser = cache(async (userId) => {
  const user = await db.user.findUnique({
    where: { id: userId },
    include: {
      profile: true,
      _count: {
        select: {
          posts: true,
          followers: true,
          following: true
        }
      }
    }
  });
  
  return user;
});

const getUserStats = cache(async (userId) => {
  const stats = await db.userStats.findUnique({
    where: { userId },
    select: {
      totalViews: true,
      totalLikes: true,
      joinedAt: true,
      lastActive: true
    }
  });
  
  return stats;
});

export default async function UserProfile({ userId }) {
  // These run in parallel on the server
  const [user, stats] = await Promise.all([
    getUser(userId),
    getUserStats(userId)
  ]);
  
  if (!user) {
    return (
      <div className="user-profile-error">
        <h2>User not found</h2>
        <p>The requested user profile could not be loaded.</p>
      </div>
    );
  }
  
  return (
    <div className="user-profile">
      <div className="profile-header">
        <Image
          src={user.profile?.avatar || '/default-avatar.png'}
          alt={`${user.name}'s avatar`}
          width={120}
          height={120}
          className="avatar"
          priority
        />
        <div className="profile-info">
          <h2>{user.name}</h2>
          <p className="username">@{user.username}</p>
          <p className="bio">{user.profile?.bio}</p>
          <div className="profile-stats">
            <span>{user._count.posts} posts</span>
            <span>{user._count.followers} followers</span>
            <span>{user._count.following} following</span>
          </div>
        </div>
      </div>
      
      {stats && (
        <div className="user-stats">
          <div className="stat">
            <span className="stat-value">{stats.totalViews.toLocaleString()}</span>
            <span className="stat-label">Total Views</span>
          </div>
          <div className="stat">
            <span className="stat-value">{stats.totalLikes.toLocaleString()}</span>
            <span className="stat-label">Total Likes</span>
          </div>
          <div className="stat">
            <span className="stat-value">{new Date(stats.joinedAt).getFullYear()}</span>
            <span className="stat-label">Member Since</span>
          </div>
          <div className="stat">
            <span className="stat-value">
              {new Date(stats.lastActive).toLocaleDateString()}
            </span>
            <span className="stat-label">Last Active</span>
          </div>
        </div>
      )}
    </div>
  );
}
```

**3. Client Components for Interactivity:**

```jsx
// app/components/InteractiveButton.js (Client Component)
'use client';

import { useState, useTransition } from 'react';
import { followUser, unfollowUser } from '../actions/userActions';

export default function FollowButton({ userId, initialFollowState, currentUserId }) {
  const [isFollowing, setIsFollowing] = useState(initialFollowState);
  const [isPending, startTransition] = useTransition();
  
  const handleFollowToggle = () => {
    startTransition(async () => {
      try {
        if (isFollowing) {
          await unfollowUser(userId, currentUserId);
          setIsFollowing(false);
        } else {
          await followUser(userId, currentUserId);
          setIsFollowing(true);
        }
      } catch (error) {
        console.error('Follow action failed:', error);
        // Revert optimistic update
        setIsFollowing(!isFollowing);
      }
    });
  };
  
  return (
    <button
      onClick={handleFollowToggle}
      disabled={isPending}
      className={`follow-button ${
        isFollowing ? 'following' : 'not-following'
      } ${isPending ? 'pending' : ''}`}
    >
      {isPending ? (
        <span className="loading-spinner" />
      ) : isFollowing ? (
        'Unfollow'
      ) : (
        'Follow'
      )}
    </button>
  );
}
```

**4. Server Actions for Data Mutations:**

```jsx
// app/actions/userActions.js
'use server';

import { db } from '../lib/database';
import { revalidatePath, revalidateTag } from 'next/cache';
import { redirect } from 'next/navigation';
import { auth } from '../lib/auth';

export async function followUser(targetUserId, currentUserId) {
  const session = await auth();
  
  if (!session || session.user.id !== currentUserId) {
    throw new Error('Unauthorized');
  }
  
  try {
    await db.follow.create({
      data: {
        followerId: currentUserId,
        followingId: targetUserId
      }
    });
    
    // Revalidate relevant pages
    revalidateTag(`user-${targetUserId}`);
    revalidateTag(`user-${currentUserId}`);
    revalidatePath(`/users/${targetUserId}`);
    
    return { success: true };
  } catch (error) {
    console.error('Follow user error:', error);
    throw new Error('Failed to follow user');
  }
}

export async function unfollowUser(targetUserId, currentUserId) {
  const session = await auth();
  
  if (!session || session.user.id !== currentUserId) {
    throw new Error('Unauthorized');
  }
  
  try {
    await db.follow.delete({
      where: {
        followerId_followingId: {
          followerId: currentUserId,
          followingId: targetUserId
        }
      }
    });
    
    // Revalidate relevant pages
    revalidateTag(`user-${targetUserId}`);
    revalidateTag(`user-${currentUserId}`);
    revalidatePath(`/users/${targetUserId}`);
    
    return { success: true };
  } catch (error) {
    console.error('Unfollow user error:', error);
    throw new Error('Failed to unfollow user');
  }
}

export async function createPost(formData) {
  const session = await auth();
  
  if (!session) {
    redirect('/login');
  }
  
  const title = formData.get('title');
  const content = formData.get('content');
  const category = formData.get('category');
  
  if (!title || !content) {
    throw new Error('Title and content are required');
  }
  
  try {
    const post = await db.post.create({
      data: {
        title,
        content,
        category,
        authorId: session.user.id,
        published: true
      }
    });
    
    // Revalidate relevant pages
    revalidateTag('posts');
    revalidateTag(`user-${session.user.id}`);
    revalidatePath('/');
    revalidatePath('/posts');
    
    redirect(`/posts/${post.id}`);
  } catch (error) {
    console.error('Create post error:', error);
    throw new Error('Failed to create post');
  }
}
```

**5. Streaming with Loading UI:**

```jsx
// app/posts/loading.js
export default function PostsLoading() {
  return (
    <div className="posts-loading">
      <div className="posts-skeleton">
        {Array.from({ length: 6 }).map((_, i) => (
          <div key={i} className="post-skeleton">
            <div className="skeleton-avatar" />
            <div className="skeleton-content">
              <div className="skeleton-title" />
              <div className="skeleton-text" />
              <div className="skeleton-text short" />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
```

```jsx
// app/posts/page.js
import { Suspense } from 'react';
import PostsList from '../components/PostsList';
import PostsFilter from '../components/PostsFilter';
import CreatePostForm from '../components/CreatePostForm';
import PostsLoading from './loading';

export default function PostsPage({ searchParams }) {
  const category = searchParams.category || 'all';
  const sort = searchParams.sort || 'recent';
  
  return (
    <div className="posts-page">
      <div className="posts-header">
        <h1>Posts</h1>
        <CreatePostForm />
      </div>
      
      <PostsFilter currentCategory={category} currentSort={sort} />
      
      <Suspense fallback={<PostsLoading />}>
        <PostsList category={category} sort={sort} />
      </Suspense>
    </div>
  );
}
```

**6. Advanced Caching and Revalidation:**

```jsx
// app/lib/cache.js
import { unstable_cache } from 'next/cache';

// Cache with tags for selective revalidation
export const getCachedPosts = unstable_cache(
  async (category, sort, limit = 20) => {
    const posts = await db.post.findMany({
      where: category !== 'all' ? { category } : {},
      orderBy: sort === 'recent' ? { createdAt: 'desc' } : { likes: 'desc' },
      take: limit,
      include: {
        author: {
          select: {
            id: true,
            name: true,
            username: true,
            profile: {
              select: { avatar: true }
            }
          }
        },
        _count: {
          select: {
            likes: true,
            comments: true
          }
        }
      }
    });
    
    return posts;
  },
  ['posts'],
  {
    tags: ['posts'],
    revalidate: 60 // Revalidate every 60 seconds
  }
);

export const getCachedUser = unstable_cache(
  async (userId) => {
    const user = await db.user.findUnique({
      where: { id: userId },
      include: {
        profile: true,
        _count: {
          select: {
            posts: true,
            followers: true,
            following: true
          }
        }
      }
    });
    
    return user;
  },
  ['user'],
  {
    tags: (userId) => [`user-${userId}`],
    revalidate: 300 // Revalidate every 5 minutes
  }
);
```

**7. Error Boundaries for Server Components:**

```jsx
// app/error.js
'use client';

import { useEffect } from 'react';

export default function Error({ error, reset }) {
  useEffect(() => {
    // Log the error to an error reporting service
    console.error('Page error:', error);
  }, [error]);
  
  return (
    <div className="error-page">
      <div className="error-content">
        <h2>Something went wrong!</h2>
        <p>We encountered an error while loading this page.</p>
        <details className="error-details">
          <summary>Error details</summary>
          <pre>{error.message}</pre>
        </details>
        <div className="error-actions">
          <button onClick={reset} className="retry-button">
            Try again
          </button>
          <a href="/" className="home-link">
            Go home
          </a>
        </div>
      </div>
    </div>
  );
}
```

**8. Performance Monitoring:**

```jsx
// app/lib/performance.js
export function measureServerComponentPerformance(componentName) {
  return function decorator(target, propertyKey, descriptor) {
    const originalMethod = descriptor.value;
    
    descriptor.value = async function (...args) {
      const start = performance.now();
      
      try {
        const result = await originalMethod.apply(this, args);
        const end = performance.now();
        
        console.log(`${componentName} rendered in ${end - start}ms`);
        
        // Send to analytics
        if (typeof window === 'undefined') {
          // Server-side logging
          console.log(`Server Component ${componentName}: ${end - start}ms`);
        }
        
        return result;
      } catch (error) {
        const end = performance.now();
        console.error(`${componentName} failed after ${end - start}ms:`, error);
        throw error;
      }
    };
    
    return descriptor;
  };
}
```

**Best Practices:**

1. **Minimize Client Components**: Use server components by default, client components only for interactivity
2. **Optimize Data Fetching**: Use parallel fetching and caching strategies
3. **Strategic Suspense Boundaries**: Place them where loading states make sense
4. **Cache Appropriately**: Use Next.js caching features for performance
5. **Handle Errors Gracefully**: Implement proper error boundaries
6. **Monitor Performance**: Track server component render times
7. **Progressive Enhancement**: Ensure basic functionality works without JavaScript
8. **Security First**: Validate all server actions and protect sensitive operations

---

### Q17: How do you implement advanced React patterns like Compound Components and Render Props?

**Difficulty: Expert**

**Answer:**
Advanced React patterns provide powerful abstractions for building flexible, reusable components. These patterns help manage complex component relationships and provide elegant APIs for component composition.

**1. Compound Components Pattern:**

```jsx
// components/Tabs/Tabs.jsx
import React, { createContext, useContext, useState, Children, cloneElement } from 'react';

// Context for sharing state between compound components
const TabsContext = createContext();

function useTabsContext() {
  const context = useContext(TabsContext);
  if (!context) {
    throw new Error('Tabs compound components must be used within Tabs');
  }
  return context;
}

// Main Tabs component
function Tabs({ children, defaultTab = 0, onChange, className = '' }) {
  const [activeTab, setActiveTab] = useState(defaultTab);
  
  const handleTabChange = (index) => {
    setActiveTab(index);
    onChange?.(index);
  };
  
  const contextValue = {
    activeTab,
    setActiveTab: handleTabChange
  };
  
  return (
    <TabsContext.Provider value={contextValue}>
      <div className={`tabs ${className}`}>
        {children}
      </div>
    </TabsContext.Provider>
  );
}

// Tab List component
function TabList({ children, className = '' }) {
  const { activeTab, setActiveTab } = useTabsContext();
  
  const tabElements = Children.map(children, (child, index) => {
    if (React.isValidElement(child)) {
      return cloneElement(child, {
        index,
        isActive: index === activeTab,
        onClick: () => setActiveTab(index)
      });
    }
    return child;
  });
  
  return (
    <div className={`tab-list ${className}`} role="tablist">
      {tabElements}
    </div>
  );
}

// Individual Tab component
function Tab({ children, index, isActive, onClick, disabled = false, className = '' }) {
  const handleClick = () => {
    if (!disabled) {
      onClick();
    }
  };
  
  const handleKeyDown = (e) => {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      handleClick();
    }
  };
  
  return (
    <button
      className={`tab ${
        isActive ? 'active' : ''
      } ${disabled ? 'disabled' : ''} ${className}`}
      onClick={handleClick}
      onKeyDown={handleKeyDown}
      disabled={disabled}
      role="tab"
      aria-selected={isActive}
      aria-controls={`tabpanel-${index}`}
      id={`tab-${index}`}
      tabIndex={isActive ? 0 : -1}
    >
      {children}
    </button>
  );
}

// Tab Panels container
function TabPanels({ children, className = '' }) {
  const { activeTab } = useTabsContext();
  
  const panelElements = Children.map(children, (child, index) => {
    if (React.isValidElement(child)) {
      return cloneElement(child, {
        index,
        isActive: index === activeTab
      });
    }
    return child;
  });
  
  return (
    <div className={`tab-panels ${className}`}>
      {panelElements}
    </div>
  );
}

// Individual Tab Panel
function TabPanel({ children, index, isActive, className = '' }) {
  if (!isActive) return null;
  
  return (
    <div
      className={`tab-panel ${className}`}
      role="tabpanel"
      aria-labelledby={`tab-${index}`}
      id={`tabpanel-${index}`}
      tabIndex={0}
    >
      {children}
    </div>
  );
}

// Attach compound components as static properties
Tabs.TabList = TabList;
Tabs.Tab = Tab;
Tabs.TabPanels = TabPanels;
Tabs.TabPanel = TabPanel;

export default Tabs;
```

**2. Advanced Compound Component with Flexible API:**

```jsx
// components/Modal/Modal.jsx
import React, { createContext, useContext, useState, useEffect, useRef } from 'react';
import { createPortal } from 'react-dom';

const ModalContext = createContext();

function useModalContext() {
  const context = useContext(ModalContext);
  if (!context) {
    throw new Error('Modal compound components must be used within Modal');
  }
  return context;
}

// Main Modal component
function Modal({ children, isOpen: controlledIsOpen, onClose, closeOnOverlayClick = true, closeOnEscape = true }) {
  const [internalIsOpen, setInternalIsOpen] = useState(false);
  const isControlled = controlledIsOpen !== undefined;
  const isOpen = isControlled ? controlledIsOpen : internalIsOpen;
  
  const modalRef = useRef(null);
  const previousFocusRef = useRef(null);
  
  const openModal = () => {
    if (!isControlled) {
      setInternalIsOpen(true);
    }
  };
  
  const closeModal = () => {
    if (isControlled) {
      onClose?.();
    } else {
      setInternalIsOpen(false);
    }
  };
  
  // Focus management
  useEffect(() => {
    if (isOpen) {
      previousFocusRef.current = document.activeElement;
      modalRef.current?.focus();
    } else {
      previousFocusRef.current?.focus();
    }
  }, [isOpen]);
  
  // Escape key handler
  useEffect(() => {
    if (!closeOnEscape) return;
    
    const handleEscape = (e) => {
      if (e.key === 'Escape' && isOpen) {
        closeModal();
      }
    };
    
    document.addEventListener('keydown', handleEscape);
    return () => document.removeEventListener('keydown', handleEscape);
  }, [isOpen, closeOnEscape]);
  
  // Prevent body scroll when modal is open
  useEffect(() => {
    if (isOpen) {
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = 'unset';
    }
    
    return () => {
      document.body.style.overflow = 'unset';
    };
  }, [isOpen]);
  
  const contextValue = {
    isOpen,
    openModal,
    closeModal,
    closeOnOverlayClick,
    modalRef
  };
  
  return (
    <ModalContext.Provider value={contextValue}>
      {children}
    </ModalContext.Provider>
  );
}

// Modal Trigger
function ModalTrigger({ children, asChild = false }) {
  const { openModal } = useModalContext();
  
  if (asChild && React.isValidElement(children)) {
    return React.cloneElement(children, {
      onClick: (e) => {
        children.props.onClick?.(e);
        openModal();
      }
    });
  }
  
  return (
    <button onClick={openModal} className="modal-trigger">
      {children}
    </button>
  );
}

// Modal Content
function ModalContent({ children, className = '' }) {
  const { isOpen, closeModal, closeOnOverlayClick, modalRef } = useModalContext();
  
  if (!isOpen) return null;
  
  const handleOverlayClick = (e) => {
    if (closeOnOverlayClick && e.target === e.currentTarget) {
      closeModal();
    }
  };
  
  const handleContentClick = (e) => {
    e.stopPropagation();
  };
  
  return createPortal(
    <div 
      className="modal-overlay"
      onClick={handleOverlayClick}
      role="dialog"
      aria-modal="true"
    >
      <div 
        ref={modalRef}
        className={`modal-content ${className}`}
        onClick={handleContentClick}
        tabIndex={-1}
      >
        {children}
      </div>
    </div>,
    document.body
  );
}

// Modal Header
function ModalHeader({ children, className = '' }) {
  return (
    <div className={`modal-header ${className}`}>
      {children}
    </div>
  );
}

// Modal Title
function ModalTitle({ children, className = '' }) {
  return (
    <h2 className={`modal-title ${className}`}>
      {children}
    </h2>
  );
}

// Modal Body
function ModalBody({ children, className = '' }) {
  return (
    <div className={`modal-body ${className}`}>
      {children}
    </div>
  );
}

// Modal Footer
function ModalFooter({ children, className = '' }) {
  return (
    <div className={`modal-footer ${className}`}>
      {children}
    </div>
  );
}

// Modal Close Button
function ModalClose({ children, asChild = false }) {
  const { closeModal } = useModalContext();
  
  if (asChild && React.isValidElement(children)) {
    return React.cloneElement(children, {
      onClick: (e) => {
        children.props.onClick?.(e);
        closeModal();
      }
    });
  }
  
  return (
    <button onClick={closeModal} className="modal-close">
      {children || '×'}
    </button>
  );
}

// Attach compound components
Modal.Trigger = ModalTrigger;
Modal.Content = ModalContent;
Modal.Header = ModalHeader;
Modal.Title = ModalTitle;
Modal.Body = ModalBody;
Modal.Footer = ModalFooter;
Modal.Close = ModalClose;

export default Modal;
```

**3. Render Props Pattern:**

```jsx
// components/DataFetcher/DataFetcher.jsx
import { useState, useEffect, useRef } from 'react';

function DataFetcher({ 
  url, 
  options = {}, 
  children, 
  onSuccess, 
  onError,
  retryAttempts = 3,
  retryDelay = 1000,
  cacheTime = 5 * 60 * 1000 // 5 minutes
}) {
  const [state, setState] = useState({
    data: null,
    loading: false,
    error: null,
    lastFetch: null
  });
  
  const abortControllerRef = useRef(null);
  const retryCountRef = useRef(0);
  const cacheRef = useRef(new Map());
  
  const fetchData = async (forceRefresh = false) => {
    const cacheKey = `${url}-${JSON.stringify(options)}`;
    const cachedData = cacheRef.current.get(cacheKey);
    
    // Return cached data if available and not stale
    if (!forceRefresh && cachedData && Date.now() - cachedData.timestamp < cacheTime) {
      setState({
        data: cachedData.data,
        loading: false,
        error: null,
        lastFetch: cachedData.timestamp
      });
      return;
    }
    
    // Cancel previous request
    if (abortControllerRef.current) {
      abortControllerRef.current.abort();
    }
    
    abortControllerRef.current = new AbortController();
    const { signal } = abortControllerRef.current;
    
    setState(prev => ({ ...prev, loading: true, error: null }));
    
    const attemptFetch = async (attempt = 0) => {
      try {
        const response = await fetch(url, {
          ...options,
          signal
        });
        
        if (!response.ok) {
          throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }
        
        const data = await response.json();
        
        if (!signal.aborted) {
          const timestamp = Date.now();
          
          // Cache the data
          cacheRef.current.set(cacheKey, { data, timestamp });
          
          setState({
            data,
            loading: false,
            error: null,
            lastFetch: timestamp
          });
          
          onSuccess?.(data);
          retryCountRef.current = 0;
        }
        
        return data;
      } catch (error) {
        if (signal.aborted) return;
        
        if (attempt < retryAttempts && error.name !== 'AbortError') {
          retryCountRef.current = attempt + 1;
          
          // Exponential backoff
          await new Promise(resolve => 
            setTimeout(resolve, retryDelay * Math.pow(2, attempt))
          );
          
          if (!signal.aborted) {
            return attemptFetch(attempt + 1);
          }
        } else {
          setState(prev => ({
            ...prev,
            loading: false,
            error
          }));
          
          onError?.(error);
          retryCountRef.current = 0;
        }
      }
    };
    
    return attemptFetch();
  };
  
  const refetch = () => fetchData(true);
  
  const reset = () => {
    if (abortControllerRef.current) {
      abortControllerRef.current.abort();
    }
    setState({
      data: null,
      loading: false,
      error: null,
      lastFetch: null
    });
    retryCountRef.current = 0;
  };
  
  // Initial fetch
  useEffect(() => {
    fetchData();
    
    return () => {
      if (abortControllerRef.current) {
        abortControllerRef.current.abort();
      }
    };
  }, [url, JSON.stringify(options)]);
  
  // Cleanup on unmount
  useEffect(() => {
    return () => {
      if (abortControllerRef.current) {
        abortControllerRef.current.abort();
      }
    };
  }, []);
  
  const isStale = state.lastFetch && Date.now() - state.lastFetch > cacheTime;
  
  return children({
    ...state,
    refetch,
    reset,
    isStale,
    retryCount: retryCountRef.current
  });
}

export default DataFetcher;
```

**4. Function as Children Pattern (Advanced Render Props):**

```jsx
// components/VirtualList/VirtualList.jsx
import { useState, useEffect, useRef, useMemo } from 'react';

function VirtualList({ 
  items, 
  itemHeight, 
  containerHeight, 
  overscan = 5,
  children 
}) {
  const [scrollTop, setScrollTop] = useState(0);
  const containerRef = useRef(null);
  
  const { visibleItems, totalHeight } = useMemo(() => {
    const startIndex = Math.floor(scrollTop / itemHeight);
    const endIndex = Math.min(
      startIndex + Math.ceil(containerHeight / itemHeight) + overscan,
      items.length
    );
    
    const visibleItems = [];
    for (let i = Math.max(0, startIndex - overscan); i < endIndex; i++) {
      visibleItems.push({
        index: i,
        item: items[i],
        style: {
          position: 'absolute',
          top: i * itemHeight,
          height: itemHeight,
          width: '100%'
        }
      });
    }
    
    return {
      visibleItems,
      totalHeight: items.length * itemHeight
    };
  }, [items, itemHeight, containerHeight, scrollTop, overscan]);
  
  const handleScroll = (e) => {
    setScrollTop(e.target.scrollTop);
  };
  
  const scrollToIndex = (index) => {
    if (containerRef.current) {
      containerRef.current.scrollTop = index * itemHeight;
    }
  };
  
  const scrollToTop = () => scrollToIndex(0);
  const scrollToBottom = () => scrollToIndex(items.length - 1);
  
  return (
    <div
      ref={containerRef}
      style={{
        height: containerHeight,
        overflow: 'auto',
        position: 'relative'
      }}
      onScroll={handleScroll}
    >
      <div style={{ height: totalHeight, position: 'relative' }}>
        {children({
          visibleItems,
          scrollToIndex,
          scrollToTop,
          scrollToBottom,
          totalHeight,
          scrollTop
        })}
      </div>
    </div>
  );
}

export default VirtualList;
```

**5. Usage Examples:**

```jsx
// Using Compound Components
function TabsExample() {
  return (
    <Tabs defaultTab={0} onChange={(index) => console.log('Tab changed:', index)}>
      <Tabs.TabList>
        <Tabs.Tab>Profile</Tabs.Tab>
        <Tabs.Tab>Settings</Tabs.Tab>
        <Tabs.Tab disabled>Billing</Tabs.Tab>
      </Tabs.TabList>
      
      <Tabs.TabPanels>
        <Tabs.TabPanel>
          <h3>Profile Information</h3>
          <p>Manage your profile details here.</p>
        </Tabs.TabPanel>
        <Tabs.TabPanel>
          <h3>Account Settings</h3>
          <p>Configure your account preferences.</p>
        </Tabs.TabPanel>
        <Tabs.TabPanel>
          <h3>Billing Information</h3>
          <p>View and manage your billing details.</p>
        </Tabs.TabPanel>
      </Tabs.TabPanels>
    </Tabs>
  );
}

// Using Modal Compound Components
function ModalExample() {
  return (
    <Modal>
      <Modal.Trigger>
        Open Modal
      </Modal.Trigger>
      
      <Modal.Content>
        <Modal.Header>
          <Modal.Title>Confirm Action</Modal.Title>
          <Modal.Close asChild>
            <button aria-label="Close">×</button>
          </Modal.Close>
        </Modal.Header>
        
        <Modal.Body>
          <p>Are you sure you want to perform this action?</p>
        </Modal.Body>
        
        <Modal.Footer>
          <Modal.Close asChild>
            <button>Cancel</button>
          </Modal.Close>
          <button>Confirm</button>
        </Modal.Footer>
      </Modal.Content>
    </Modal>
  );
}

// Using Render Props
function DataExample() {
  return (
    <DataFetcher 
      url="/api/users" 
      onSuccess={(data) => console.log('Data loaded:', data)}
      onError={(error) => console.error('Error:', error)}
    >
      {({ data, loading, error, refetch, isStale }) => {
        if (loading) return <div>Loading...</div>;
        if (error) return <div>Error: {error.message} <button onClick={refetch}>Retry</button></div>;
        
        return (
          <div>
            {isStale && <div>Data is stale <button onClick={refetch}>Refresh</button></div>}
            <ul>
              {data?.map(user => (
                <li key={user.id}>{user.name}</li>
              ))}
            </ul>
          </div>
        );
      }}
    </DataFetcher>
  );
}

// Using Virtual List
function VirtualListExample() {
  const items = Array.from({ length: 10000 }, (_, i) => `Item ${i + 1}`);
  
  return (
    <VirtualList 
      items={items} 
      itemHeight={50} 
      containerHeight={400}
    >
      {({ visibleItems, scrollToTop, scrollToBottom }) => (
        <>
          <div style={{ position: 'fixed', top: 0, right: 0, zIndex: 1000 }}>
            <button onClick={scrollToTop}>Top</button>
            <button onClick={scrollToBottom}>Bottom</button>
          </div>
          {visibleItems.map(({ index, item, style }) => (
            <div key={index} style={style}>
              {item}
            </div>
          ))}
        </>
      )}
    </VirtualList>
  );
}
```

**Best Practices:**

1. **Use Compound Components for related UI elements**: Perfect for tabs, modals, accordions
2. **Render Props for data logic**: Great for sharing stateful logic without UI assumptions
3. **Provide flexible APIs**: Support both controlled and uncontrolled modes
4. **Handle accessibility**: Include proper ARIA attributes and keyboard navigation
5. **Optimize performance**: Use React.memo, useMemo, and useCallback appropriately
6. **Error boundaries**: Wrap complex patterns in error boundaries
7. **TypeScript support**: Provide proper type definitions for better DX
8. **Documentation**: Provide clear examples and API documentation

---

### Q18: How do you implement micro-frontends with React and Module Federation?

**Difficulty: Expert**

**Answer:**
Micro-frontends enable teams to develop, deploy, and scale frontend applications independently. Module Federation in Webpack 5 provides a powerful way to implement micro-frontends with React.

**1. Shell Application (Host) Setup:**

```javascript
// webpack.config.js (Shell/Host)
const ModuleFederationPlugin = require('@module-federation/webpack');
const path = require('path');

module.exports = {
  mode: 'development',
  entry: './src/index.js',
  devServer: {
    port: 3000,
    historyApiFallback: true,
    hot: true,
    headers: {
      'Access-Control-Allow-Origin': '*',
    },
  },
  resolve: {
    extensions: ['.js', '.jsx', '.ts', '.tsx'],
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx|ts|tsx)$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: [
              '@babel/preset-env',
              '@babel/preset-react',
              '@babel/preset-typescript'
            ],
          },
        },
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader'],
      },
    ],
  },
  plugins: [
    new ModuleFederationPlugin({
      name: 'shell',
      remotes: {
        'user-management': 'userManagement@http://localhost:3001/remoteEntry.js',
        'product-catalog': 'productCatalog@http://localhost:3002/remoteEntry.js',
        'shopping-cart': 'shoppingCart@http://localhost:3003/remoteEntry.js',
        'analytics': 'analytics@http://localhost:3004/remoteEntry.js',
      },
      shared: {
        react: {
          singleton: true,
          requiredVersion: '^18.0.0',
          eager: true,
        },
        'react-dom': {
          singleton: true,
          requiredVersion: '^18.0.0',
          eager: true,
        },
        'react-router-dom': {
          singleton: true,
          requiredVersion: '^6.0.0',
        },
        '@emotion/react': {
          singleton: true,
        },
        '@emotion/styled': {
          singleton: true,
        },
      },
    }),
  ],
};
```

```jsx
// src/App.jsx (Shell Application)
import React, { Suspense, lazy, useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { ErrorBoundary } from 'react-error-boundary';
import { ThemeProvider } from '@emotion/react';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { ReactQueryDevtools } from '@tanstack/react-query-devtools';

// Lazy load micro-frontends
const UserManagement = lazy(() => import('user-management/UserApp'));
const ProductCatalog = lazy(() => import('product-catalog/ProductApp'));
const ShoppingCart = lazy(() => import('shopping-cart/CartApp'));
const Analytics = lazy(() => import('analytics/AnalyticsApp'));

// Shared components
import Header from './components/Header';
import Sidebar from './components/Sidebar';
import LoadingSpinner from './components/LoadingSpinner';
import ErrorFallback from './components/ErrorFallback';
import { useAuth } from './hooks/useAuth';
import { useTheme } from './hooks/useTheme';
import { GlobalStyles } from './styles/GlobalStyles';

// Create a single QueryClient instance
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      retry: 3,
      staleTime: 5 * 60 * 1000, // 5 minutes
      cacheTime: 10 * 60 * 1000, // 10 minutes
    },
  },
});

function App() {
  const { user, isAuthenticated, login, logout } = useAuth();
  const { theme, toggleTheme } = useTheme();
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [microfrontendErrors, setMicrofrontendErrors] = useState({});

  // Global error handler for micro-frontends
  const handleMicrofrontendError = (microfrontendName, error) => {
    console.error(`Error in ${microfrontendName}:`, error);
    setMicrofrontendErrors(prev => ({
      ...prev,
      [microfrontendName]: error
    }));
  };

  // Clear error when navigating away
  const clearMicrofrontendError = (microfrontendName) => {
    setMicrofrontendErrors(prev => {
      const newErrors = { ...prev };
      delete newErrors[microfrontendName];
      return newErrors;
    });
  };

  return (
    <QueryClientProvider client={queryClient}>
      <ThemeProvider theme={theme}>
        <Router>
          <GlobalStyles />
          <div className="app">
            <Header 
              user={user}
              onToggleSidebar={() => setSidebarOpen(!sidebarOpen)}
              onToggleTheme={toggleTheme}
              onLogout={logout}
            />
            
            <div className="app-body">
              <Sidebar 
                isOpen={sidebarOpen}
                onClose={() => setSidebarOpen(false)}
                user={user}
              />
              
              <main className="main-content">
                <Routes>
                  <Route path="/" element={<Navigate to="/dashboard" replace />} />
                  
                  {/* User Management Micro-frontend */}
                  <Route 
                    path="/users/*" 
                    element={
                      <ErrorBoundary
                        FallbackComponent={ErrorFallback}
                        onError={(error) => handleMicrofrontendError('user-management', error)}
                        onReset={() => clearMicrofrontendError('user-management')}
                      >
                        <Suspense fallback={<LoadingSpinner message="Loading User Management..." />}>
                          <UserManagement 
                            user={user}
                            theme={theme}
                            onError={(error) => handleMicrofrontendError('user-management', error)}
                          />
                        </Suspense>
                      </ErrorBoundary>
                    } 
                  />
                  
                  {/* Product Catalog Micro-frontend */}
                  <Route 
                    path="/products/*" 
                    element={
                      <ErrorBoundary
                        FallbackComponent={ErrorFallback}
                        onError={(error) => handleMicrofrontendError('product-catalog', error)}
                        onReset={() => clearMicrofrontendError('product-catalog')}
                      >
                        <Suspense fallback={<LoadingSpinner message="Loading Product Catalog..." />}>
                          <ProductCatalog 
                            user={user}
                            theme={theme}
                            onError={(error) => handleMicrofrontendError('product-catalog', error)}
                          />
                        </Suspense>
                      </ErrorBoundary>
                    } 
                  />
                  
                  {/* Shopping Cart Micro-frontend */}
                  <Route 
                    path="/cart/*" 
                    element={
                      <ErrorBoundary
                        FallbackComponent={ErrorFallback}
                        onError={(error) => handleMicrofrontendError('shopping-cart', error)}
                        onReset={() => clearMicrofrontendError('shopping-cart')}
                      >
                        <Suspense fallback={<LoadingSpinner message="Loading Shopping Cart..." />}>
                          <ShoppingCart 
                            user={user}
                            theme={theme}
                            onError={(error) => handleMicrofrontendError('shopping-cart', error)}
                          />
                        </Suspense>
                      </ErrorBoundary>
                    } 
                  />
                  
                  {/* Analytics Micro-frontend */}
                  <Route 
                    path="/analytics/*" 
                    element={
                      isAuthenticated && user?.role === 'admin' ? (
                        <ErrorBoundary
                          FallbackComponent={ErrorFallback}
                          onError={(error) => handleMicrofrontendError('analytics', error)}
                          onReset={() => clearMicrofrontendError('analytics')}
                        >
                          <Suspense fallback={<LoadingSpinner message="Loading Analytics..." />}>
                            <Analytics 
                              user={user}
                              theme={theme}
                              onError={(error) => handleMicrofrontendError('analytics', error)}
                            />
                          </Suspense>
                        </ErrorBoundary>
                      ) : (
                        <Navigate to="/unauthorized" replace />
                      )
                    } 
                  />
                  
                  <Route path="/unauthorized" element={<div>Unauthorized Access</div>} />
                  <Route path="*" element={<div>Page Not Found</div>} />
                </Routes>
              </main>
            </div>
          </div>
        </Router>
        <ReactQueryDevtools initialIsOpen={false} />
      </ThemeProvider>
    </QueryClientProvider>
  );
}

export default App;
```

**2. Micro-frontend (Remote) Setup:**

```javascript
// webpack.config.js (Product Catalog Micro-frontend)
const ModuleFederationPlugin = require('@module-federation/webpack');

module.exports = {
  mode: 'development',
  entry: './src/index.js',
  devServer: {
    port: 3002,
    historyApiFallback: true,
    hot: true,
    headers: {
      'Access-Control-Allow-Origin': '*',
    },
  },
  resolve: {
    extensions: ['.js', '.jsx', '.ts', '.tsx'],
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx|ts|tsx)$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: [
              '@babel/preset-env',
              '@babel/preset-react',
              '@babel/preset-typescript'
            ],
          },
        },
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader'],
      },
    ],
  },
  plugins: [
    new ModuleFederationPlugin({
      name: 'productCatalog',
      filename: 'remoteEntry.js',
      exposes: {
        './ProductApp': './src/ProductApp',
        './ProductList': './src/components/ProductList',
        './ProductDetail': './src/components/ProductDetail',
        './ProductSearch': './src/components/ProductSearch',
      },
      shared: {
        react: {
          singleton: true,
          requiredVersion: '^18.0.0',
        },
        'react-dom': {
          singleton: true,
          requiredVersion: '^18.0.0',
        },
        'react-router-dom': {
          singleton: true,
          requiredVersion: '^6.0.0',
        },
        '@emotion/react': {
          singleton: true,
        },
        '@emotion/styled': {
          singleton: true,
        },
      },
    }),
  ],
};
```

```jsx
// src/ProductApp.jsx (Product Catalog Micro-frontend)
import React, { useEffect, useState } from 'react';
import { Routes, Route, useNavigate, useLocation } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { ThemeProvider } from '@emotion/react';

import ProductList from './components/ProductList';
import ProductDetail from './components/ProductDetail';
import ProductSearch from './components/ProductSearch';
import ProductCategories from './components/ProductCategories';
import { ProductProvider } from './context/ProductContext';
import { useProductAnalytics } from './hooks/useProductAnalytics';
import { productApi } from './api/productApi';

// Create isolated QueryClient for this micro-frontend
const productQueryClient = new QueryClient({
  defaultOptions: {
    queries: {
      retry: 2,
      staleTime: 2 * 60 * 1000, // 2 minutes
      cacheTime: 5 * 60 * 1000, // 5 minutes
    },
  },
});

function ProductApp({ user, theme, onError }) {
  const navigate = useNavigate();
  const location = useLocation();
  const { trackPageView, trackProductView } = useProductAnalytics();
  const [isInitialized, setIsInitialized] = useState(false);

  // Initialize micro-frontend
  useEffect(() => {
    const initializeApp = async () => {
      try {
        // Initialize product API with user context
        await productApi.initialize(user?.token);
        
        // Track initial page view
        trackPageView(location.pathname);
        
        setIsInitialized(true);
      } catch (error) {
        console.error('Failed to initialize Product Catalog:', error);
        onError?.(error);
      }
    };

    initializeApp();
  }, [user, onError]);

  // Track navigation changes
  useEffect(() => {
    if (isInitialized) {
      trackPageView(location.pathname);
    }
  }, [location.pathname, isInitialized]);

  // Error boundary for this micro-frontend
  const handleError = (error, errorInfo) => {
    console.error('Product Catalog Error:', error, errorInfo);
    onError?.(error);
  };

  if (!isInitialized) {
    return (
      <div className="product-app-loading">
        <div className="loading-spinner" />
        <p>Initializing Product Catalog...</p>
      </div>
    );
  }

  return (
    <QueryClientProvider client={productQueryClient}>
      <ThemeProvider theme={theme}>
        <ProductProvider user={user} onError={handleError}>
          <div className="product-app">
            <Routes>
              <Route path="/" element={<ProductList />} />
              <Route path="/search" element={<ProductSearch />} />
              <Route path="/categories" element={<ProductCategories />} />
              <Route path="/categories/:categoryId" element={<ProductList />} />
              <Route path="/:productId" element={<ProductDetail />} />
            </Routes>
          </div>
        </ProductProvider>
      </ThemeProvider>
    </QueryClientProvider>
  );
}

export default ProductApp;
```

**3. Cross-Micro-frontend Communication:**

```jsx
// src/utils/eventBus.js (Shared Event System)
class EventBus {
  constructor() {
    this.events = {};
  }

  subscribe(eventName, callback) {
    if (!this.events[eventName]) {
      this.events[eventName] = [];
    }
    this.events[eventName].push(callback);

    // Return unsubscribe function
    return () => {
      this.events[eventName] = this.events[eventName].filter(
        cb => cb !== callback
      );
    };
  }

  emit(eventName, data) {
    if (this.events[eventName]) {
      this.events[eventName].forEach(callback => {
        try {
          callback(data);
        } catch (error) {
          console.error(`Error in event handler for ${eventName}:`, error);
        }
      });
    }
  }

  once(eventName, callback) {
    const unsubscribe = this.subscribe(eventName, (data) => {
      callback(data);
      unsubscribe();
    });
    return unsubscribe;
  }

  clear(eventName) {
    if (eventName) {
      delete this.events[eventName];
    } else {
      this.events = {};
    }
  }
}

// Global event bus instance
window.__MICRO_FRONTEND_EVENT_BUS__ = window.__MICRO_FRONTEND_EVENT_BUS__ || new EventBus();

export const eventBus = window.__MICRO_FRONTEND_EVENT_BUS__;

// Predefined event types
export const EVENTS = {
  USER_LOGGED_IN: 'user:logged-in',
  USER_LOGGED_OUT: 'user:logged-out',
  CART_ITEM_ADDED: 'cart:item-added',
  CART_ITEM_REMOVED: 'cart:item-removed',
  CART_UPDATED: 'cart:updated',
  PRODUCT_VIEWED: 'product:viewed',
  PRODUCT_PURCHASED: 'product:purchased',
  THEME_CHANGED: 'theme:changed',
  NAVIGATION_CHANGED: 'navigation:changed',
};
```

```jsx
// src/hooks/useEventBus.js (React Hook for Event Bus)
import { useEffect, useRef, useCallback } from 'react';
import { eventBus } from '../utils/eventBus';

export function useEventBus() {
  const unsubscribersRef = useRef([]);

  const subscribe = useCallback((eventName, callback) => {
    const unsubscribe = eventBus.subscribe(eventName, callback);
    unsubscribersRef.current.push(unsubscribe);
    return unsubscribe;
  }, []);

  const emit = useCallback((eventName, data) => {
    eventBus.emit(eventName, data);
  }, []);

  const once = useCallback((eventName, callback) => {
    const unsubscribe = eventBus.once(eventName, callback);
    unsubscribersRef.current.push(unsubscribe);
    return unsubscribe;
  }, []);

  // Cleanup on unmount
  useEffect(() => {
    return () => {
      unsubscribersRef.current.forEach(unsubscribe => unsubscribe());
      unsubscribersRef.current = [];
    };
  }, []);

  return { subscribe, emit, once };
}

// Specific hooks for common events
export function useCartEvents() {
  const { subscribe, emit } = useEventBus();

  const onCartUpdated = useCallback((callback) => {
    return subscribe(EVENTS.CART_UPDATED, callback);
  }, [subscribe]);

  const emitCartUpdated = useCallback((cartData) => {
    emit(EVENTS.CART_UPDATED, cartData);
  }, [emit]);

  const onItemAdded = useCallback((callback) => {
    return subscribe(EVENTS.CART_ITEM_ADDED, callback);
  }, [subscribe]);

  const emitItemAdded = useCallback((item) => {
    emit(EVENTS.CART_ITEM_ADDED, item);
  }, [emit]);

  return {
    onCartUpdated,
    emitCartUpdated,
    onItemAdded,
    emitItemAdded,
  };
}
```

**4. Shared State Management:**

```jsx
// src/store/globalStore.js (Shared State)
import { create } from 'zustand';
import { subscribeWithSelector } from 'zustand/middleware';
import { eventBus, EVENTS } from '../utils/eventBus';

// Global store shared across micro-frontends
const useGlobalStore = create(
  subscribeWithSelector((set, get) => ({
    // User state
    user: null,
    isAuthenticated: false,
    
    // Theme state
    theme: 'light',
    
    // Cart state
    cart: {
      items: [],
      total: 0,
      itemCount: 0,
    },
    
    // Notification state
    notifications: [],
    
    // Actions
    setUser: (user) => {
      set({ user, isAuthenticated: !!user });
      eventBus.emit(EVENTS.USER_LOGGED_IN, user);
    },
    
    clearUser: () => {
      set({ user: null, isAuthenticated: false });
      eventBus.emit(EVENTS.USER_LOGGED_OUT);
    },
    
    setTheme: (theme) => {
      set({ theme });
      eventBus.emit(EVENTS.THEME_CHANGED, theme);
    },
    
    updateCart: (cartData) => {
      set({ cart: cartData });
      eventBus.emit(EVENTS.CART_UPDATED, cartData);
    },
    
    addToCart: (item) => {
      const currentCart = get().cart;
      const existingItem = currentCart.items.find(i => i.id === item.id);
      
      let updatedItems;
      if (existingItem) {
        updatedItems = currentCart.items.map(i => 
          i.id === item.id 
            ? { ...i, quantity: i.quantity + (item.quantity || 1) }
            : i
        );
      } else {
        updatedItems = [...currentCart.items, { ...item, quantity: item.quantity || 1 }];
      }
      
      const updatedCart = {
        items: updatedItems,
        total: updatedItems.reduce((sum, i) => sum + (i.price * i.quantity), 0),
        itemCount: updatedItems.reduce((sum, i) => sum + i.quantity, 0),
      };
      
      set({ cart: updatedCart });
      eventBus.emit(EVENTS.CART_ITEM_ADDED, item);
      eventBus.emit(EVENTS.CART_UPDATED, updatedCart);
    },
    
    removeFromCart: (itemId) => {
      const currentCart = get().cart;
      const updatedItems = currentCart.items.filter(i => i.id !== itemId);
      
      const updatedCart = {
        items: updatedItems,
        total: updatedItems.reduce((sum, i) => sum + (i.price * i.quantity), 0),
        itemCount: updatedItems.reduce((sum, i) => sum + i.quantity, 0),
      };
      
      set({ cart: updatedCart });
      eventBus.emit(EVENTS.CART_ITEM_REMOVED, itemId);
      eventBus.emit(EVENTS.CART_UPDATED, updatedCart);
    },
    
    addNotification: (notification) => {
      const id = Date.now().toString();
      const newNotification = { ...notification, id, timestamp: Date.now() };
      set(state => ({
        notifications: [...state.notifications, newNotification]
      }));
      
      // Auto-remove after 5 seconds
      setTimeout(() => {
        set(state => ({
          notifications: state.notifications.filter(n => n.id !== id)
        }));
      }, 5000);
    },
    
    removeNotification: (id) => {
      set(state => ({
        notifications: state.notifications.filter(n => n.id !== id)
      }));
    },
  }))
);

// Make store globally available
window.__GLOBAL_STORE__ = useGlobalStore;

export default useGlobalStore;
```

**5. Dynamic Module Loading:**

```jsx
// src/components/DynamicMicrofrontend.jsx
import React, { Suspense, useState, useEffect } from 'react';
import { ErrorBoundary } from 'react-error-boundary';
import LoadingSpinner from './LoadingSpinner';
import ErrorFallback from './ErrorFallback';

const DynamicMicrofrontend = ({ 
  remoteName, 
  moduleName, 
  fallback, 
  props = {},
  onError,
  retryAttempts = 3 
}) => {
  const [Component, setComponent] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [retryCount, setRetryCount] = useState(0);

  const loadComponent = async () => {
    try {
      setLoading(true);
      setError(null);
      
      // Dynamic import with retry logic
      const module = await import(`${remoteName}/${moduleName}`);
      const LoadedComponent = module.default || module;
      
      setComponent(() => LoadedComponent);
      setRetryCount(0);
    } catch (err) {
      console.error(`Failed to load ${remoteName}/${moduleName}:`, err);
      
      if (retryCount < retryAttempts) {
        // Exponential backoff retry
        setTimeout(() => {
          setRetryCount(prev => prev + 1);
          loadComponent();
        }, Math.pow(2, retryCount) * 1000);
      } else {
        setError(err);
        onError?.(err);
      }
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadComponent();
  }, [remoteName, moduleName]);

  if (loading) {
    return fallback || <LoadingSpinner message={`Loading ${remoteName}...`} />;
  }

  if (error) {
    return (
      <ErrorFallback 
        error={error} 
        resetErrorBoundary={() => {
          setRetryCount(0);
          loadComponent();
        }}
      />
    );
  }

  if (!Component) {
    return <div>Failed to load component</div>;
  }

  return (
    <ErrorBoundary
      FallbackComponent={ErrorFallback}
      onError={onError}
      onReset={() => {
        setComponent(null);
        setRetryCount(0);
        loadComponent();
      }}
    >
      <Suspense fallback={fallback || <LoadingSpinner />}>
        <Component {...props} />
      </Suspense>
    </ErrorBoundary>
  );
};

export default DynamicMicrofrontend;
```

**6. Testing Micro-frontends:**

```javascript
// tests/microfrontend.test.js
import { render, screen, waitFor } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import DynamicMicrofrontend from '../components/DynamicMicrofrontend';

// Mock the module federation
jest.mock('user-management/UserApp', () => {
  return function MockUserApp(props) {
    return <div data-testid="user-app">User Management App {JSON.stringify(props)}</div>;
  };
});

describe('DynamicMicrofrontend', () => {
  it('should load and render micro-frontend successfully', async () => {
    const mockProps = { user: { id: 1, name: 'Test User' } };
    
    render(
      <BrowserRouter>
        <DynamicMicrofrontend
          remoteName="user-management"
          moduleName="UserApp"
          props={mockProps}
        />
      </BrowserRouter>
    );

    // Should show loading initially
    expect(screen.getByText(/loading/i)).toBeInTheDocument();

    // Should load the component
    await waitFor(() => {
      expect(screen.getByTestId('user-app')).toBeInTheDocument();
    });

    // Should pass props correctly
    expect(screen.getByText(/Test User/)).toBeInTheDocument();
  });

  it('should handle loading errors gracefully', async () => {
    const onError = jest.fn();
    
    render(
      <DynamicMicrofrontend
        remoteName="non-existent"
        moduleName="NonExistentApp"
        onError={onError}
        retryAttempts={1}
      />
    );

    await waitFor(() => {
      expect(onError).toHaveBeenCalled();
    });
  });
});
```

**Best Practices:**

1. **Independent Deployments**: Each micro-frontend should be deployable independently
2. **Shared Dependencies**: Use Module Federation's shared dependencies to avoid duplication
3. **Error Isolation**: Implement proper error boundaries to prevent cascading failures
4. **Communication Patterns**: Use event bus or shared state for cross-micro-frontend communication
5. **Performance**: Lazy load micro-frontends and implement proper caching strategies
6. **Testing**: Test micro-frontends both in isolation and integration
7. **Monitoring**: Implement comprehensive logging and monitoring for each micro-frontend
8. **Version Management**: Maintain compatibility between shell and micro-frontends

---

### Q19: How do you implement advanced React performance optimization techniques?

**Difficulty: Expert**

**Answer:**
Advanced React performance optimization involves multiple strategies including bundle optimization, runtime performance, memory management, and rendering optimization.

**1. Bundle Optimization and Code Splitting:**

```jsx
// src/utils/lazyWithRetry.js - Enhanced lazy loading with retry
import { lazy } from 'react';

const lazyWithRetry = (componentImport, retries = 3, delay = 1000) => {
  return lazy(async () => {
    let lastError;
    
    for (let i = 0; i <= retries; i++) {
      try {
        const component = await componentImport();
        return component;
      } catch (error) {
        lastError = error;
        
        if (i < retries) {
          // Exponential backoff
          await new Promise(resolve => 
            setTimeout(resolve, delay * Math.pow(2, i))
          );
        }
      }
    }
    
    throw lastError;
  });
};

export default lazyWithRetry;
```

```jsx
// src/components/RouteBasedSplitting.jsx
import React, { Suspense } from 'react';
import { Routes, Route } from 'react-router-dom';
import { ErrorBoundary } from 'react-error-boundary';
import lazyWithRetry from '../utils/lazyWithRetry';
import LoadingSpinner from './LoadingSpinner';
import ErrorFallback from './ErrorFallback';

// Route-based code splitting with retry logic
const Dashboard = lazyWithRetry(() => import('../pages/Dashboard'));
const UserProfile = lazyWithRetry(() => import('../pages/UserProfile'));
const Settings = lazyWithRetry(() => import('../pages/Settings'));
const Analytics = lazyWithRetry(() => import('../pages/Analytics'));
const Reports = lazyWithRetry(() => import('../pages/Reports'));

// Component-based splitting for heavy components
const DataVisualization = lazyWithRetry(() => import('../components/DataVisualization'));
const AdvancedChart = lazyWithRetry(() => import('../components/AdvancedChart'));

function AppRoutes() {
  return (
    <ErrorBoundary FallbackComponent={ErrorFallback}>
      <Suspense fallback={<LoadingSpinner />}>
        <Routes>
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/profile" element={<UserProfile />} />
          <Route path="/settings" element={<Settings />} />
          <Route 
            path="/analytics" 
            element={
              <Suspense fallback={<LoadingSpinner message="Loading Analytics..." />}>
                <Analytics />
              </Suspense>
            } 
          />
          <Route 
            path="/reports" 
            element={
              <Suspense fallback={<LoadingSpinner message="Loading Reports..." />}>
                <Reports />
              </Suspense>
            } 
          />
        </Routes>
      </Suspense>
    </ErrorBoundary>
  );
}

export default AppRoutes;
```

**2. Advanced Memoization Strategies:**

```jsx
// src/hooks/useAdvancedMemo.js
import { useMemo, useRef, useCallback } from 'react';

// Deep comparison memoization
export function useDeepMemo(factory, deps) {
  const ref = useRef();
  
  if (!ref.current || !deepEqual(ref.current.deps, deps)) {
    ref.current = {
      deps,
      value: factory()
    };
  }
  
  return ref.current.value;
}

// Memoization with custom equality function
export function useMemoWithCustomEquality(factory, deps, equalityFn) {
  const ref = useRef();
  
  if (!ref.current || !equalityFn(ref.current.deps, deps)) {
    ref.current = {
      deps,
      value: factory()
    };
  }
  
  return ref.current.value;
}

// Stable callback with dependency tracking
export function useStableCallback(callback, deps) {
  const callbackRef = useRef(callback);
  const depsRef = useRef(deps);
  
  // Update callback if dependencies changed
  if (!shallowEqual(depsRef.current, deps)) {
    callbackRef.current = callback;
    depsRef.current = deps;
  }
  
  return useCallback((...args) => {
    return callbackRef.current(...args);
  }, []);
}

// Memoization with size limit (LRU cache)
export function useLRUMemo(factory, deps, maxSize = 10) {
  const cacheRef = useRef(new Map());
  const keysRef = useRef([]);
  
  return useMemo(() => {
    const key = JSON.stringify(deps);
    const cache = cacheRef.current;
    const keys = keysRef.current;
    
    if (cache.has(key)) {
      // Move to end (most recently used)
      const index = keys.indexOf(key);
      keys.splice(index, 1);
      keys.push(key);
      return cache.get(key);
    }
    
    const value = factory();
    
    // Add to cache
    cache.set(key, value);
    keys.push(key);
    
    // Remove oldest if over limit
    if (keys.length > maxSize) {
      const oldestKey = keys.shift();
      cache.delete(oldestKey);
    }
    
    return value;
  }, deps);
}

// Utility functions
function deepEqual(a, b) {
  if (a === b) return true;
  if (a == null || b == null) return false;
  if (typeof a !== typeof b) return false;
  
  if (typeof a === 'object') {
    const keysA = Object.keys(a);
    const keysB = Object.keys(b);
    
    if (keysA.length !== keysB.length) return false;
    
    for (let key of keysA) {
      if (!keysB.includes(key) || !deepEqual(a[key], b[key])) {
        return false;
      }
    }
    
    return true;
  }
  
  return false;
}

function shallowEqual(a, b) {
  if (a === b) return true;
  if (!a || !b) return false;
  
  const keysA = Object.keys(a);
  const keysB = Object.keys(b);
  
  if (keysA.length !== keysB.length) return false;
  
  for (let key of keysA) {
    if (a[key] !== b[key]) return false;
  }
  
  return true;
}
```

**3. Virtual Scrolling and Windowing:**

```jsx
// src/components/VirtualizedList.jsx
import React, { useState, useEffect, useRef, useMemo, useCallback } from 'react';
import { FixedSizeList as List, VariableSizeList } from 'react-window';
import { areEqual } from 'react-window';
import memoize from 'memoize-one';

// Fixed height virtual list
const VirtualizedFixedList = React.memo(({ 
  items, 
  itemHeight = 50, 
  containerHeight = 400,
  renderItem,
  onItemsRendered,
  overscanCount = 5
}) => {
  const listRef = useRef();
  
  const ItemRenderer = useCallback(({ index, style }) => {
    const item = items[index];
    return (
      <div style={style}>
        {renderItem({ item, index })}
      </div>
    );
  }, [items, renderItem]);
  
  const handleItemsRendered = useCallback(({ visibleStartIndex, visibleStopIndex }) => {
    onItemsRendered?.({ 
      startIndex: visibleStartIndex, 
      stopIndex: visibleStopIndex 
    });
  }, [onItemsRendered]);
  
  return (
    <List
      ref={listRef}
      height={containerHeight}
      itemCount={items.length}
      itemSize={itemHeight}
      onItemsRendered={handleItemsRendered}
      overscanCount={overscanCount}
    >
      {ItemRenderer}
    </List>
  );
});

// Variable height virtual list
const VirtualizedVariableList = React.memo(({ 
  items, 
  getItemHeight, 
  containerHeight = 400,
  renderItem,
  estimatedItemSize = 50,
  onItemsRendered
}) => {
  const listRef = useRef();
  const itemHeightCache = useRef(new Map());
  
  // Memoized height getter
  const getHeight = useMemo(() => 
    memoize((index) => {
      if (itemHeightCache.current.has(index)) {
        return itemHeightCache.current.get(index);
      }
      
      const height = getItemHeight(items[index], index);
      itemHeightCache.current.set(index, height);
      return height;
    }),
    [items, getItemHeight]
  );
  
  // Clear cache when items change
  useEffect(() => {
    itemHeightCache.current.clear();
    listRef.current?.resetAfterIndex(0);
  }, [items]);
  
  const ItemRenderer = useCallback(({ index, style }) => {
    const item = items[index];
    return (
      <div style={style}>
        {renderItem({ item, index })}
      </div>
    );
  }, [items, renderItem]);
  
  return (
    <VariableSizeList
      ref={listRef}
      height={containerHeight}
      itemCount={items.length}
      itemSize={getHeight}
      estimatedItemSize={estimatedItemSize}
      onItemsRendered={onItemsRendered}
    >
      {ItemRenderer}
    </VariableSizeList>
  );
});

// Grid virtualization for 2D data
const VirtualizedGrid = React.memo(({ 
  data, 
  columnCount,
  rowCount,
  columnWidth = 200,
  rowHeight = 50,
  containerWidth = 800,
  containerHeight = 400,
  renderCell
}) => {
  const gridRef = useRef();
  
  const CellRenderer = useCallback(({ columnIndex, rowIndex, style }) => {
    const cellData = data[rowIndex]?.[columnIndex];
    return (
      <div style={style}>
        {renderCell({ cellData, columnIndex, rowIndex })}
      </div>
    );
  }, [data, renderCell]);
  
  return (
    <FixedSizeGrid
      ref={gridRef}
      columnCount={columnCount}
      columnWidth={columnWidth}
      height={containerHeight}
      rowCount={rowCount}
      rowHeight={rowHeight}
      width={containerWidth}
    >
      {CellRenderer}
    </FixedSizeGrid>
  );
});

export { VirtualizedFixedList, VirtualizedVariableList, VirtualizedGrid };
```

**4. Memory Management and Cleanup:**

```jsx
// src/hooks/useMemoryOptimization.js
import { useEffect, useRef, useCallback } from 'react';

// Automatic cleanup for event listeners
export function useEventListener(eventName, handler, element = window) {
  const savedHandler = useRef();
  
  useEffect(() => {
    savedHandler.current = handler;
  }, [handler]);
  
  useEffect(() => {
    const isSupported = element && element.addEventListener;
    if (!isSupported) return;
    
    const eventListener = (event) => savedHandler.current(event);
    element.addEventListener(eventName, eventListener);
    
    return () => {
      element.removeEventListener(eventName, eventListener);
    };
  }, [eventName, element]);
}

// Intersection Observer with cleanup
export function useIntersectionObserver(callback, options = {}) {
  const observerRef = useRef();
  
  const observe = useCallback((element) => {
    if (observerRef.current) {
      observerRef.current.disconnect();
    }
    
    if (element) {
      observerRef.current = new IntersectionObserver(callback, options);
      observerRef.current.observe(element);
    }
  }, [callback, options]);
  
  const unobserve = useCallback((element) => {
    if (observerRef.current && element) {
      observerRef.current.unobserve(element);
    }
  }, []);
  
  useEffect(() => {
    return () => {
      if (observerRef.current) {
        observerRef.current.disconnect();
      }
    };
  }, []);
  
  return { observe, unobserve };
}

// Memory-efficient image loading
export function useImagePreloader(imageSrcs, options = {}) {
  const [loadedImages, setLoadedImages] = useState(new Set());
  const [failedImages, setFailedImages] = useState(new Set());
  const imageCache = useRef(new Map());
  
  const preloadImage = useCallback((src) => {
    if (imageCache.current.has(src)) {
      return imageCache.current.get(src);
    }
    
    const promise = new Promise((resolve, reject) => {
      const img = new Image();
      
      img.onload = () => {
        setLoadedImages(prev => new Set([...prev, src]));
        resolve(img);
      };
      
      img.onerror = () => {
        setFailedImages(prev => new Set([...prev, src]));
        reject(new Error(`Failed to load image: ${src}`));
      };
      
      img.src = src;
      
      // Set loading timeout
      if (options.timeout) {
        setTimeout(() => {
          if (!loadedImages.has(src) && !failedImages.has(src)) {
            img.src = ''; // Cancel loading
            reject(new Error(`Image loading timeout: ${src}`));
          }
        }, options.timeout);
      }
    });
    
    imageCache.current.set(src, promise);
    return promise;
  }, [loadedImages, failedImages, options.timeout]);
  
  useEffect(() => {
    imageSrcs.forEach(src => {
      if (!loadedImages.has(src) && !failedImages.has(src)) {
        preloadImage(src).catch(() => {});
      }
    });
  }, [imageSrcs, preloadImage, loadedImages, failedImages]);
  
  // Cleanup cache on unmount
  useEffect(() => {
    return () => {
      imageCache.current.clear();
    };
  }, []);
  
  return {
    loadedImages,
    failedImages,
    preloadImage,
    isLoaded: (src) => loadedImages.has(src),
    isFailed: (src) => failedImages.has(src)
  };
}

// Debounced state updates
export function useDebouncedState(initialValue, delay = 300) {
  const [value, setValue] = useState(initialValue);
  const [debouncedValue, setDebouncedValue] = useState(initialValue);
  const timeoutRef = useRef();
  
  useEffect(() => {
    if (timeoutRef.current) {
      clearTimeout(timeoutRef.current);
    }
    
    timeoutRef.current = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);
    
    return () => {
      if (timeoutRef.current) {
        clearTimeout(timeoutRef.current);
      }
    };
  }, [value, delay]);
  
  return [debouncedValue, setValue];
}
```

**5. Performance Monitoring and Profiling:**

```jsx
// src/utils/performanceMonitor.js
class PerformanceMonitor {
  constructor() {
    this.metrics = new Map();
    this.observers = [];
  }
  
  // Measure component render time
  measureRender(componentName, renderFn) {
    const start = performance.now();
    const result = renderFn();
    const end = performance.now();
    
    this.recordMetric('render', componentName, end - start);
    return result;
  }
  
  // Measure async operations
  async measureAsync(operationName, asyncFn) {
    const start = performance.now();
    try {
      const result = await asyncFn();
      const end = performance.now();
      this.recordMetric('async', operationName, end - start);
      return result;
    } catch (error) {
      const end = performance.now();
      this.recordMetric('async-error', operationName, end - start);
      throw error;
    }
  }
  
  // Record custom metrics
  recordMetric(type, name, value, metadata = {}) {
    const key = `${type}:${name}`;
    if (!this.metrics.has(key)) {
      this.metrics.set(key, []);
    }
    
    this.metrics.get(key).push({
      value,
      timestamp: Date.now(),
      metadata
    });
    
    // Notify observers
    this.observers.forEach(observer => {
      observer({ type, name, value, metadata });
    });
    
    // Keep only last 100 measurements
    const measurements = this.metrics.get(key);
    if (measurements.length > 100) {
      measurements.splice(0, measurements.length - 100);
    }
  }
  
  // Get performance statistics
  getStats(type, name) {
    const key = `${type}:${name}`;
    const measurements = this.metrics.get(key) || [];
    
    if (measurements.length === 0) {
      return null;
    }
    
    const values = measurements.map(m => m.value);
    const sum = values.reduce((a, b) => a + b, 0);
    const avg = sum / values.length;
    const min = Math.min(...values);
    const max = Math.max(...values);
    
    // Calculate percentiles
    const sorted = [...values].sort((a, b) => a - b);
    const p50 = sorted[Math.floor(sorted.length * 0.5)];
    const p90 = sorted[Math.floor(sorted.length * 0.9)];
    const p95 = sorted[Math.floor(sorted.length * 0.95)];
    
    return {
      count: measurements.length,
      avg,
      min,
      max,
      p50,
      p90,
      p95,
      recent: measurements.slice(-10).map(m => m.value)
    };
  }
  
  // Subscribe to metrics
  subscribe(observer) {
    this.observers.push(observer);
    return () => {
      const index = this.observers.indexOf(observer);
      if (index > -1) {
        this.observers.splice(index, 1);
      }
    };
  }
  
  // Clear all metrics
  clear() {
    this.metrics.clear();
  }
}

export const performanceMonitor = new PerformanceMonitor();

// React hook for performance monitoring
export function usePerformanceMonitor() {
  const [metrics, setMetrics] = useState({});
  
  useEffect(() => {
    const unsubscribe = performanceMonitor.subscribe((metric) => {
      setMetrics(prev => ({
        ...prev,
        [`${metric.type}:${metric.name}`]: performanceMonitor.getStats(metric.type, metric.name)
      }));
    });
    
    return unsubscribe;
  }, []);
  
  return {
    metrics,
    measureRender: performanceMonitor.measureRender.bind(performanceMonitor),
    measureAsync: performanceMonitor.measureAsync.bind(performanceMonitor),
    recordMetric: performanceMonitor.recordMetric.bind(performanceMonitor)
  };
}
```

**Best Practices:**

1. **Bundle Analysis**: Regularly analyze bundle size and eliminate unused code
2. **Lazy Loading**: Implement strategic code splitting and lazy loading
3. **Memoization**: Use React.memo, useMemo, and useCallback judiciously
4. **Virtual Scrolling**: Implement for large lists and grids
5. **Memory Management**: Clean up event listeners, timers, and subscriptions
6. **Performance Monitoring**: Track key metrics and identify bottlenecks
7. **Image Optimization**: Implement lazy loading and proper image formats
8. **State Management**: Optimize state updates and avoid unnecessary re-renders

### Q20: How do you implement React 18+ concurrent features and automatic batching?

**Answer:**

React 18 introduced several concurrent features that improve performance and user experience through automatic batching, concurrent rendering, and new APIs.

**1. Automatic Batching:**

```jsx
// Before React 18 - only batched in React event handlers
function App() {
  const [count, setCount] = useState(0);
  const [flag, setFlag] = useState(false);

  function handleClick() {
    // React 17: Only batched in React events
    setCount(c => c + 1);
    setFlag(f => !f);
    // Only one re-render
  }

  function handleTimeout() {
    // React 17: Not batched - causes two re-renders
    setTimeout(() => {
      setCount(c => c + 1);
      setFlag(f => !f);
    }, 1000);
  }

  function handlePromise() {
    // React 17: Not batched - causes two re-renders
    fetch('/api/data').then(() => {
      setCount(c => c + 1);
      setFlag(f => !f);
    });
  }

  return (
    <div>
      <button onClick={handleClick}>Sync Update</button>
      <button onClick={handleTimeout}>Async Update</button>
      <button onClick={handlePromise}>Promise Update</button>
      <p>Count: {count}, Flag: {flag.toString()}</p>
    </div>
  );
}

// React 18: All updates are automatically batched
// createRoot enables automatic batching
import { createRoot } from 'react-dom/client';

const container = document.getElementById('root');
const root = createRoot(container);
root.render(<App />);
```

**2. Opt-out of Batching with flushSync:**

```jsx
import { flushSync } from 'react-dom';

function App() {
  const [count, setCount] = useState(0);
  const [flag, setFlag] = useState(false);

  function handleClick() {
    // Force immediate update (opt-out of batching)
    flushSync(() => {
      setCount(c => c + 1);
    });
    // This will cause a separate re-render
    setFlag(f => !f);
  }

  return (
    <div>
      <button onClick={handleClick}>Force Separate Renders</button>
      <p>Count: {count}, Flag: {flag.toString()}</p>
    </div>
  );
}
```

**3. useTransition for Non-Urgent Updates:**

```jsx
import { useState, useTransition, useDeferredValue } from 'react';

function SearchApp() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [isPending, startTransition] = useTransition();
  
  // Defer expensive computations
  const deferredQuery = useDeferredValue(query);

  function handleSearch(value) {
    // Urgent: Update input immediately
    setQuery(value);
    
    // Non-urgent: Update results with lower priority
    startTransition(() => {
      // Expensive search operation
      const searchResults = performExpensiveSearch(value);
      setResults(searchResults);
    });
  }

  return (
    <div>
      <input
        value={query}
        onChange={(e) => handleSearch(e.target.value)}
        placeholder="Search..."
      />
      {isPending && <div>Searching...</div>}
      <SearchResults query={deferredQuery} results={results} />
    </div>
  );
}

function SearchResults({ query, results }) {
  // This component will re-render with lower priority
  return (
    <div>
      <h3>Results for: {query}</h3>
      {results.map(result => (
        <div key={result.id}>{result.title}</div>
      ))}
    </div>
  );
}

function performExpensiveSearch(query) {
  // Simulate expensive operation
  const results = [];
  for (let i = 0; i < 10000; i++) {
    if (Math.random() > 0.7) {
      results.push({ id: i, title: `Result ${i} for ${query}` });
    }
  }
  return results.slice(0, 50);
}
```

**4. useDeferredValue for Expensive Renders:**

```jsx
import { useState, useDeferredValue, memo } from 'react';

function App() {
  const [text, setText] = useState('');
  const deferredText = useDeferredValue(text);

  return (
    <div>
      <input
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Type to filter..."
      />
      {/* This component updates immediately */}
      <p>Typing: {text}</p>
      
      {/* This component updates with lower priority */}
      <ExpensiveList query={deferredText} />
    </div>
  );
}

const ExpensiveList = memo(function ExpensiveList({ query }) {
  const items = generateLargeList(query);
  
  return (
    <ul>
      {items.map(item => (
        <li key={item.id}>
          <ExpensiveItem item={item} />
        </li>
      ))}
    </ul>
  );
});

const ExpensiveItem = memo(function ExpensiveItem({ item }) {
  // Simulate expensive rendering
  let result = 0;
  for (let i = 0; i < 1000; i++) {
    result += Math.random();
  }
  
  return <div>{item.name} - {result.toFixed(2)}</div>;
});

function generateLargeList(query) {
  const items = [];
  for (let i = 0; i < 1000; i++) {
    const name = `Item ${i}`;
    if (!query || name.toLowerCase().includes(query.toLowerCase())) {
      items.push({ id: i, name });
    }
  }
  return items;
}
```

**5. Concurrent Rendering with Suspense:**

```jsx
import { Suspense, lazy, useState, useTransition } from 'react';

// Lazy load components
const HeavyComponent = lazy(() => import('./HeavyComponent'));
const AnotherComponent = lazy(() => import('./AnotherComponent'));

function App() {
  const [activeTab, setActiveTab] = useState('tab1');
  const [isPending, startTransition] = useTransition();

  function handleTabChange(tab) {
    startTransition(() => {
      setActiveTab(tab);
    });
  }

  return (
    <div>
      <nav>
        <button
          onClick={() => handleTabChange('tab1')}
          disabled={isPending && activeTab !== 'tab1'}
        >
          Tab 1 {isPending && activeTab === 'tab1' && '(Loading...)'}
        </button>
        <button
          onClick={() => handleTabChange('tab2')}
          disabled={isPending && activeTab !== 'tab2'}
        >
          Tab 2 {isPending && activeTab === 'tab2' && '(Loading...)'}
        </button>
      </nav>
      
      <Suspense fallback={<div>Loading tab content...</div>}>
        {activeTab === 'tab1' && <HeavyComponent />}
        {activeTab === 'tab2' && <AnotherComponent />}
      </Suspense>
    </div>
  );
}
```

**6. useId for Stable IDs:**

```jsx
import { useId } from 'react';

function FormField({ label, type = 'text' }) {
  const id = useId();
  
  return (
    <div>
      <label htmlFor={id}>{label}</label>
      <input id={id} type={type} />
    </div>
  );
}

function ContactForm() {
  return (
    <form>
      <FormField label="Name" />
      <FormField label="Email" type="email" />
      <FormField label="Phone" type="tel" />
    </form>
  );
}
```

**7. useSyncExternalStore for External State:**

```jsx
import { useSyncExternalStore } from 'react';

// External store
class ThemeStore {
  constructor() {
    this.theme = 'light';
    this.listeners = new Set();
  }
  
  getSnapshot = () => {
    return this.theme;
  };
  
  subscribe = (listener) => {
    this.listeners.add(listener);
    return () => this.listeners.delete(listener);
  };
  
  setTheme = (theme) => {
    this.theme = theme;
    this.listeners.forEach(listener => listener());
  };
}

const themeStore = new ThemeStore();

function useTheme() {
  const theme = useSyncExternalStore(
    themeStore.subscribe,
    themeStore.getSnapshot,
    () => 'light' // Server snapshot
  );
  
  return [theme, themeStore.setTheme];
}

function App() {
  const [theme, setTheme] = useTheme();
  
  return (
    <div className={`app ${theme}`}>
      <button onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>
        Toggle Theme (Current: {theme})
      </button>
    </div>
  );
}
```

**8. Performance Monitoring with Concurrent Features:**

```jsx
import { Profiler } from 'react';

function onRenderCallback(id, phase, actualDuration, baseDuration, startTime, commitTime) {
  console.log('Profiler:', {
    id,
    phase, // 'mount' or 'update'
    actualDuration, // Time spent rendering
    baseDuration, // Estimated time without memoization
    startTime,
    commitTime
  });
  
  // Send to analytics
  if (actualDuration > 16) { // More than one frame
    analytics.track('slow-render', {
      component: id,
      duration: actualDuration,
      phase
    });
  }
}

function App() {
  return (
    <Profiler id="App" onRender={onRenderCallback}>
      <Header />
      <Profiler id="MainContent" onRender={onRenderCallback}>
        <MainContent />
      </Profiler>
      <Footer />
    </Profiler>
  );
}
```

**Best Practices:**

1. **Use createRoot**: Always use `createRoot` instead of `ReactDOM.render` for React 18 features
2. **Embrace Automatic Batching**: Let React batch updates automatically, only use `flushSync` when necessary
3. **Use Transitions Wisely**: Mark non-urgent updates with `startTransition` to keep UI responsive
4. **Defer Expensive Operations**: Use `useDeferredValue` for expensive computations that can be delayed
5. **Combine with Suspense**: Use concurrent features with Suspense for better loading states
6. **Monitor Performance**: Use Profiler to identify performance bottlenecks
7. **Gradual Adoption**: You can adopt these features incrementally in existing applications
8. **Test Thoroughly**: Concurrent features can change timing, so test edge cases carefully

---

### Q21: How do you implement React Server Components and modern full-stack React architecture?
**Difficulty: Expert**

**Answer:**
React Server Components (RSC) represent a paradigm shift in React development, allowing components to run on the server and stream HTML to the client. This enables better performance, SEO, and developer experience.

**1. Basic Server Component Structure:**

```jsx
// app/page.js (Server Component by default in Next.js 13+)
import { Suspense } from 'react';
import { UserProfile } from './components/UserProfile';
import { PostsList } from './components/PostsList';
import { Sidebar } from './components/Sidebar';

// This runs on the server
export default async function HomePage() {
  // Direct database/API calls in Server Components
  const user = await fetch('https://api.example.com/user/1').then(res => res.json());
  const posts = await fetch('https://api.example.com/posts').then(res => res.json());
  
  return (
    <div className="homepage">
      <header>
        <h1>Welcome, {user.name}</h1>
      </header>
      
      <main className="main-content">
        <Suspense fallback={<div>Loading profile...</div>}>
          <UserProfile user={user} />
        </Suspense>
        
        <Suspense fallback={<div>Loading posts...</div>}>
          <PostsList posts={posts} />
        </Suspense>
      </main>
      
      <aside>
        <Suspense fallback={<div>Loading sidebar...</div>}>
          <Sidebar userId={user.id} />
        </Suspense>
      </aside>
    </div>
  );
}
```

**2. Server vs Client Component Patterns:**

```jsx
// components/UserProfile.js (Server Component)
import { db } from '@/lib/database';
import { InteractiveButton } from './InteractiveButton';

export async function UserProfile({ user }) {
  // Server-side data fetching
  const userStats = await db.query(
    'SELECT post_count, follower_count FROM user_stats WHERE user_id = ?',
    [user.id]
  );
  
  const recentActivity = await db.query(
    'SELECT * FROM activities WHERE user_id = ? ORDER BY created_at DESC LIMIT 5',
    [user.id]
  );
  
  return (
    <div className="user-profile">
      <div className="user-info">
        <img src={user.avatar} alt={user.name} />
        <h2>{user.name}</h2>
        <p>{user.bio}</p>
        
        <div className="stats">
          <span>{userStats.post_count} Posts</span>
          <span>{userStats.follower_count} Followers</span>
        </div>
      </div>
      
      {/* Client Component for interactivity */}
      <InteractiveButton userId={user.id} />
      
      <div className="recent-activity">
        <h3>Recent Activity</h3>
        {recentActivity.map(activity => (
          <div key={activity.id} className="activity-item">
            <span>{activity.type}</span>
            <time>{new Date(activity.created_at).toLocaleDateString()}</time>
          </div>
        ))}
      </div>
    </div>
  );
}
```