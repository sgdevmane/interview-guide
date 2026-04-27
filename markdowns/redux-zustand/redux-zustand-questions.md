<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>Redux & Zustand Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for developers</b></p>
</div>

---

## Table of Contents

1. [How do you minimize unnecessary re-renders in a React component using Zustand?](#q1-how-do-you-minimize-unnecessary-re-renders-in-a-react-component-using-zustand) <span class="intermediate">Intermediate</span>
2. [How do you implement optimistic UI updates using Redux Toolkit (RTK)?](#q2-how-do-you-implement-optimistic-ui-updates-using-redux-toolkit-rtk) <span class="advanced">Advanced</span>
3. [How do you persist Zustand state to `localStorage` and rehydrate it on app start?](#q3-how-do-you-persist-zustand-state-to-localstorage-and-rehydrate-it-on-app-start) <span class="beginner">Beginner</span>
4. [How do you handle complex asynchronous logic (like debouncing or cancellation) in Redux Toolkit?](#q4-how-do-you-handle-complex-asynchronous-logic-like-debouncing-or-cancellation-in-redux-toolkit) <span class="advanced">Advanced</span>
5. [How do you normalize nested API data (e.g., Users with Posts) in a Redux store?](#q5-how-do-you-normalize-nested-api-data-e.g.-users-with-posts-in-a-redux-store) <span class="intermediate">Intermediate</span>
6. [How do you type a Redux Toolkit slice and dispatch correctly in TypeScript?](#q6-how-do-you-type-a-redux-toolkit-slice-and-dispatch-correctly-in-typescript) <span class="beginner">Beginner</span>
7. [How do you access the Zustand store state outside of a React component (e.g., in a utility function)?](#q7-how-do-you-access-the-zustand-store-state-outside-of-a-react-component-e.g.-in-a-utility-function) <span class="intermediate">Intermediate</span>
8. [How do you split a large Redux store into manageable chunks (Code Splitting)?](#q8-how-do-you-split-a-large-redux-store-into-manageable-chunks-code-splitting) <span class="advanced">Advanced</span>
9. [How do you unit test a Redux Toolkit slice logic?](#q9-how-do-you-unit-test-a-redux-toolkit-slice-logic) <span class="intermediate">Intermediate</span>
10. [How do you handle side effects in Zustand without middleware?](#q10-how-do-you-handle-side-effects-in-zustand-without-middleware) <span class="beginner">Beginner</span>
11. [How do you create a 'derived state' selector in Redux that is memoized?](#q11-how-do-you-create-a-derived-state-selector-in-redux-that-is-memoized) <span class="intermediate">Intermediate</span>
12. [How do you reset the entire Redux state (e.g., on user logout)?](#q12-how-do-you-reset-the-entire-redux-state-e.g.-on-user-logout) <span class="intermediate">Intermediate</span>
13. [How do you share state between multiple tabs/windows using Zustand?](#q13-how-do-you-share-state-between-multiple-tabswindows-using-zustand) <span class="advanced">Advanced</span>
14. [How do you prevent a specific Redux action from being logged in DevTools (e.g., sensitive data)?](#q14-how-do-you-prevent-a-specific-redux-action-from-being-logged-in-devtools-e.g.-sensitive-data) <span class="intermediate">Intermediate</span>
15. [How do you implement undo/redo functionality in a Redux store?](#q15-how-do-you-implement-undoredo-functionality-in-a-redux-store) <span class="advanced">Advanced</span>
16. [How do you use the DevTools middleware in Zustand?](#q16-how-do-you-use-the-devtools-middleware-in-zustand) <span class="beginner">Beginner</span>
17. [How do you create a parameterized selector in Redux?](#q17-how-do-you-create-a-parameterized-selector-in-redux) <span class="intermediate">Intermediate</span>
18. [How do you listen to transient state changes in Zustand without re-rendering?](#q18-how-do-you-listen-to-transient-state-changes-in-zustand-without-re-rendering) <span class="advanced">Advanced</span>
19. [How do you transform API responses in RTK Query?](#q19-how-do-you-transform-api-responses-in-rtk-query) <span class="intermediate">Intermediate</span>
20. [How do you implement Cache Invalidation in RTK Query?](#q20-how-do-you-implement-cache-invalidation-in-rtk-query) <span class="intermediate">Intermediate</span>
21. [How do you organize a large Zustand store using Slices?](#q21-how-do-you-organize-a-large-zustand-store-using-slices) <span class="advanced">Advanced</span>
22. [What is the `prepare` callback in Redux Toolkit reducers?](#q22-what-is-the-prepare-callback-in-redux-toolkit-reducers) <span class="intermediate">Intermediate</span>
23. [How do you implement polling in RTK Query?](#q23-how-do-you-implement-polling-in-rtk-query) <span class="beginner">Beginner</span>
24. [How do you inject an Authentication Token into RTK Query requests?](#q24-how-do-you-inject-an-authentication-token-into-rtk-query-requests) <span class="intermediate">Intermediate</span>
25. [How do you use Immer manually in Redux Toolkit?](#q25-how-do-you-use-immer-manually-in-redux-toolkit) <span class="advanced">Advanced</span>
26. [How do you handle multiple action types in one reducer (RTK)?](#q26-how-do-you-handle-multiple-action-types-in-one-reducer-rtk) <span class="intermediate">Intermediate</span>
27. [How do you create a Component-Scoped Zustand Store?](#q27-how-do-you-create-a-component-scoped-zustand-store) <span class="advanced">Advanced</span>
28. [How do you prefetch data with RTK Query?](#q28-how-do-you-prefetch-data-with-rtk-query) <span class="intermediate">Intermediate</span>
29. [How do you code-split RTK Query endpoints?](#q29-how-do-you-code-split-rtk-query-endpoints) <span class="advanced">Advanced</span>
30. [How do you debug the current state in an RTK reducer?](#q30-how-do-you-debug-the-current-state-in-an-rtk-reducer) <span class="beginner">Beginner</span>
31. [How do you skip a query in RTK Query?](#q31-how-do-you-skip-a-query-in-rtk-query) <span class="beginner">Beginner</span>
32. [How do you automatically refetch data on window focus?](#q32-how-do-you-automatically-refetch-data-on-window-focus) <span class="beginner">Beginner</span>
33. [How do you use the Immer middleware in Zustand?](#q33-how-do-you-use-the-immer-middleware-in-zustand) <span class="intermediate">Intermediate</span>
34. [How do you inject extra arguments (like an API client) into Thunks?](#q34-how-do-you-inject-extra-arguments-like-an-api-client-into-thunks) <span class="intermediate">Intermediate</span>
35. [How do you bypass `baseQuery` for a specific endpoint in RTK Query?](#q35-how-do-you-bypass-basequery-for-a-specific-endpoint-in-rtk-query) <span class="advanced">Advanced</span>
36. [How do you optimize RTK Query selection performance?](#q36-how-do-you-optimize-rtk-query-selection-performance) <span class="advanced">Advanced</span>
37. [How do you handle optimistic updates in Zustand?](#q37-how-do-you-handle-optimistic-updates-in-zustand) <span class="intermediate">Intermediate</span>
38. [How do you reset the RTK Query cache?](#q38-how-do-you-reset-the-rtk-query-cache) <span class="intermediate">Intermediate</span>
39. [How do you use `combine` middleware in Zustand for type inference?](#q39-how-do-you-use-combine-middleware-in-zustand-for-type-inference) <span class="advanced">Advanced</span>
40. [How do you ensure strict state immutability checks in Redux Toolkit?](#q40-how-do-you-ensure-strict-state-immutability-checks-in-redux-toolkit) <span class="beginner">Beginner</span>
41. [How do you perform Server-Side Rendering (SSR) with Redux Toolkit?](#q41-how-do-you-perform-server-side-rendering-ssr-with-redux-toolkit) <span class="advanced">Advanced</span>
42. [How do you perform Server-Side Rendering (SSR) with Zustand?](#q42-how-do-you-perform-server-side-rendering-ssr-with-zustand) <span class="advanced">Advanced</span>
43. [How do you use the `autoBatchEnhancer` in Redux Toolkit?](#q43-how-do-you-use-the-autobatchenhancer-in-redux-toolkit) <span class="advanced">Advanced</span>
44. [How do you test a Zustand store?](#q44-how-do-you-test-a-zustand-store) <span class="intermediate">Intermediate</span>
45. [How do you wait for a specific action in Redux?](#q45-how-do-you-wait-for-a-specific-action-in-redux) <span class="advanced">Advanced</span>
46. [How do you use `mutative` with Zustand?](#q46-how-do-you-use-mutative-with-zustand) <span class="intermediate">Intermediate</span>
47. [How do you create a bidirectional sync between Redux and URL params?](#q47-how-do-you-create-a-bidirectional-sync-between-redux-and-url-params) <span class="advanced">Advanced</span>
48. [How do you handle non-serializable data in Redux?](#q48-how-do-you-handle-non-serializable-data-in-redux) <span class="intermediate">Intermediate</span>
49. [How do you implement a 'Draft' feature using Redux?](#q49-how-do-you-implement-a-draft-feature-using-redux) <span class="intermediate">Intermediate</span>
50. [How do you use `createStore` (Vanilla) in Zustand?](#q50-how-do-you-use-createstore-vanilla-in-zustand) <span class="intermediate">Intermediate</span>

---

<a id="q1"></a>
### Q1: How do you minimize unnecessary re-renders in a React component using Zustand?

**Difficulty**: Intermediate

**Strategy**: Re-render optimization is critical for app performance, especially in large component trees. Zustand's default `===` comparison triggers re-renders on every reference change, even when the actual data hasn't changed meaningfully. Use selectors to subscribe only to the specific slice of state a component needs, and apply `useShallow` for object returns to avoid unnecessary re-renders caused by new object references on each call.

**Strategy:**
Use "selectors" when subscribing to the store. Zustand compares the result of the selector (by default using strict equality `===`). For objects, use `useShallow` or a custom equality function to avoid re-renders when nested properties haven't changed.

**Code Example:**
```tsx
import { create } from 'zustand';
import { useShallow } from 'zustand/react/shallow';

const useStore = create((set) => ({
  bears: 0,
  fish: 0,
  increaseBears: () => set((state) => ({ bears: state.bears + 1 })),
}));

// Component only re-renders when `bears` changes, ignoring `fish`
const Component = () => {
  const bears = useStore(useShallow((state) => state.bears));
  return <div>{bears}</div>;
};
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q2"></a>
### Q2: How do you implement optimistic UI updates using Redux Toolkit (RTK)?

**Difficulty**: Advanced

**Strategy**: Optimistic updates make apps feel instantaneous by updating the UI before the server responds, then rolling back if the request fails. This is essential for real-world features like toggling likes, editing posts, or reordering lists. The key pitfall is ensuring the rollback logic correctly restores the previous state on failure, including handling race conditions where multiple optimistic updates overlap.

**Strategy:**
In `createAsyncThunk`, use the `onQueryStarted` lifecycle method. Manually update the cache (via `updateQueryData` if using RTK Query) immediately, and rollback if the promise fails.

**Code Example:**
```typescript
const updatePost = createAsyncThunk(
  'posts/update',
  async (post: Post, { dispatch, getState }) => {
    // 1. Optimistic update logic here (manual dispatch if not using RTK Query)
    // ...
    const response = await api.updatePost(post);
    return response.data;
  }
);
// Note: RTK Query handles this much more elegantly with onQueryStarted
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q3"></a>
### Q3: How do you persist Zustand state to `localStorage` and rehydrate it on app start?

**Difficulty**: Beginner

**Strategy**: State persistence is a common requirement for preserving user preferences, cart data, or authentication tokens across page reloads. Zustand's `persist` middleware handles serialization and rehydration automatically. A common pitfall is storing too much data in localStorage (it has a ~5MB limit), so use `partialize` to selectively persist only the necessary slices.

**Strategy:**
Use the `persist` middleware provided by Zustand. Wrap your store creator with `persist` and provide a unique `name` for the storage key.

**Code Example:**
```typescript
import { create } from 'zustand';
import { persist, createJSONStorage } from 'zustand/middleware';

const useStore = create(
  persist(
    (set) => ({
      fishes: 0,
      addFish: () => set({ fishes: 1 }),
    }),
    {
      name: 'food-storage', // unique name
      storage: createJSONStorage(() => localStorage), // default is localStorage
    }
  )
);
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q4"></a>
### Q4: How do you handle complex asynchronous logic (like debouncing or cancellation) in Redux Toolkit?

**Difficulty**: Advanced

**Strategy**: Real-world apps need fine-grained control over async flows such as search-as-you-type (debounce), cancelling in-flight requests on navigation, or sequencing dependent API calls. While `createAsyncThunk` handles basic async, the `createListenerMiddleware` in RTK provides a lightweight, built-in alternative to redux-saga for debouncing, throttling, and conditional logic. Avoid rolling custom middleware when the listener API covers the same ground with less boilerplate.

**Strategy:**
Use `createAsyncThunk` which provides an `AbortSignal`. You can pass this signal to your API call (e.g., `fetch` or `axios`) to cancel requests automatically when the thunk is cancelled or a component unmounts (if using RTK Query). For more complex flows (debounce/takeLatest), `redux-saga` or `redux-observable` might be needed, but `createListenerMiddleware` is the modern RTK replacement.

**Code Example (Listener Middleware):**
```typescript
listenerMiddleware.startListening({
  actionCreator: searchUser,
  effect: async (action, listenerApi) => {
    // Cancel previous running instances of this effect
    listenerApi.cancelActiveListeners();
    
    // Debounce
    await listenerApi.delay(500);
    
    // Fetch data...
  },
});
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q5"></a>
### Q5: How do you normalize nested API data (e.g., Users with Posts) in a Redux store?

**Difficulty**: Intermediate

**Strategy**: Normalized state prevents data duplication and keeps updates predictable -- when a user's name changes, you update it in one place rather than searching through nested arrays. `createEntityAdapter` gives you CRUD methods and auto-generated selectors out of the box. The key interview point is explaining why flat `{ ids, entities }` structure scales better than storing nested API responses directly.

**Strategy:**
Use `createEntityAdapter` to manage collections as normalized structures (`{ ids: [], entities: {} }`). This simplifies CRUD operations and prevents deeply nested updates.

**Code Example:**
```typescript
const usersAdapter = createEntityAdapter<User>();

const usersSlice = createSlice({
  name: 'users',
  initialState: usersAdapter.getInitialState(),
  reducers: {
    userAdded: usersAdapter.addOne,
    usersReceived: usersAdapter.setAll,
  },
});

// Selectors are automatically generated
export const { selectAll: selectAllUsers } = usersAdapter.getSelectors();
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q6"></a>
### Q6: How do you type a Redux Toolkit slice and dispatch correctly in TypeScript?

**Difficulty**: Beginner

**Strategy**: Proper TypeScript integration eliminates an entire class of runtime bugs in Redux code, from typos in action types to accessing nonexistent state properties. The best practice is to infer types from the store itself rather than defining them manually, which keeps types in sync as the store evolves. Always create typed hooks to prevent accidentally using the untyped versions from `react-redux`.

**Strategy:**
Infer `RootState` and `AppDispatch` from the store instance. create typed hooks (`useAppDispatch`, `useAppSelector`) to avoid repeating types in every component.

**Code Example:**
```typescript
// store.ts
export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;

// hooks.ts
export const useAppDispatch: () => AppDispatch = useDispatch;
export const useAppSelector: TypedUseSelectorHook<RootState> = useSelector;
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q7"></a>
### Q7: How do you access the Zustand store state outside of a React component (e.g., in a utility function)?

**Difficulty**: Intermediate

**Strategy**: Unlike Redux, Zustand stores are plain JavaScript objects that don't depend on a React context provider. This makes them invaluable for reading or writing state from axios interceptors, WebSocket handlers, or analytics utilities. The key insight is that `.getState()` returns a snapshot (not a reactive subscription), so it is safe to call anywhere without triggering re-renders.

**Strategy:**
You can import the store hook and call `.getState()` or `.setState()` directly on it. This works because Zustand stores are vanilla JavaScript objects.

**Code Example:**
```typescript
import { useStore } from './store';

export const logCurrentBears = () => {
  const bears = useStore.getState().bears;
  console.log(`Current bears: ${bears}`);
};

export const resetBears = () => {
  useStore.setState({ bears: 0 });
};
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q8"></a>
### Q8: How do you split a large Redux store into manageable chunks (Code Splitting)?

**Difficulty**: Advanced

**Strategy**: In large applications, shipping all reducers upfront increases the initial bundle size. Code splitting allows you to load reducer logic on demand when a route or feature is first accessed. The `replaceReducer` API is the foundation, but be cautious of TypeScript type safety -- dynamically added reducers can weaken your `RootState` inference if not handled carefully.

**Strategy:**
Use the `injectReducer` pattern or `redux-dynamic-modules`. In modern RTK, you can add reducers to the store dynamically, but it's often cleaner to keep the store static and code-split at the *component* level while importing slices.

**Code Example:**
```typescript
// Dynamic injection helper
export function injectReducer(key, reducer) {
  store.asyncReducers[key] = reducer;
  store.replaceReducer(createRootReducer(store.asyncReducers));
}
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q9"></a>
### Q9: How do you unit test a Redux Toolkit slice logic?

**Difficulty**: Intermediate

**Strategy**: Testing reducers as pure functions is one of Redux's core advantages -- given the same state and action, the output is always deterministic. This makes tests fast, reliable, and free of mocking overhead. Focus tests on edge cases like undefined initial state, concurrent actions, and boundary values rather than just the happy path.

**Strategy:**
Test the reducer as a pure function. Pass an initial state and an action, then assert the expected new state.

**Code Example:**
```typescript
test('should handle increment', () => {
  const previousState = { value: 0 };
  const nextState = counterReducer(previousState, increment());
  expect(nextState).toEqual({ value: 1 });
});
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q10"></a>
### Q10: How do you handle side effects in Zustand without middleware?

**Difficulty**: Beginner

**Strategy**: One of Zustand's biggest advantages over Redux is that store actions are plain functions, so async logic goes directly inside them without thunks, sagas, or special middleware. This drastically reduces boilerplate. The pitfall to watch for is forgetting error handling -- always wrap async calls in try/catch and set error state so the UI can react to failures.

**Strategy:**
Since Zustand actions are just functions, you can write async logic directly inside them. No thunks or sagas required.

**Code Example:**
```typescript
const useStore = create((set) => ({
  data: null,
  fetchData: async (id) => {
    set({ loading: true });
    const response = await fetch(`/api/${id}`);
    const json = await response.json();
    set({ data: json, loading: false });
  },
}));
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q11"></a>
### Q11: How do you create a 'derived state' selector in Redux that is memoized?

**Difficulty**: Intermediate

**Strategy**: Derived state -- like a filtered list or computed total -- recalculating on every render is a common source of performance bugs. `createSelector` from Reselect solves this by caching the result until its input selectors return new values. A key pitfall is that Reselect only has a cache size of 1 by default, so sharing a selector across components with different arguments will break memoization unless you use selector factories.

**Strategy:**
Use `createSelector` from Reselect (re-exported by RTK). It memoizes the result and only re-calculates if input selectors change.

**Code Example:**
```typescript
const selectItems = (state) => state.items;
const selectFilter = (state) => state.filter;

export const selectFilteredItems = createSelector(
  [selectItems, selectFilter],
  (items, filter) => items.filter(item => item.includes(filter))
);
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q12"></a>
### Q12: How do you reset the entire Redux state (e.g., on user logout)?

**Difficulty**: Intermediate

**Strategy**: Security-sensitive applications must clear all client-side state on logout to prevent data leakage between user sessions. The root reducer wrapper pattern intercepts a logout action and forces every slice back to its initial state by passing `undefined`. Be careful not to accidentally reset state that should persist across sessions, like feature flags or app-wide configuration.

**Strategy:**
Wrap the root reducer. Check for a specific action (e.g., `LOGOUT`), and if matched, return `undefined` as the state to the root reducer, forcing it to re-initialize.

**Code Example:**
```typescript
const rootReducer = combineReducers({ /* ... */ });

const appReducer = (state, action) => {
  if (action.type === 'auth/logout') {
    state = undefined;
  }
  return rootReducer(state, action);
};
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q13"></a>
### Q13: How do you share state between multiple tabs/windows using Zustand?

**Difficulty**: Advanced

**Strategy**: Multi-tab state sync is important for apps where actions in one tab should reflect immediately in another, such as updating a shopping cart or logging out. The `BroadcastChannel` API provides a clean, cross-tab messaging mechanism, while the `storage` event on localStorage fires when another tab modifies the same key. A common pitfall is creating infinite sync loops -- always guard state listeners with a comparison check before updating.

**Strategy:**
Use a middleware that listens to the `storage` event (if using localStorage) or use `BroadcastChannel` API to sync state updates across tabs.

**Code Example:**
```typescript
// Simple sync via localStorage listener
window.addEventListener('storage', (e) => {
  if (e.key === 'my-app-storage') {
    useStore.setState(JSON.parse(e.newValue).state);
  }
});
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q14"></a>
### Q14: How do you prevent a specific Redux action from being logged in DevTools (e.g., sensitive data)?

**Difficulty**: Intermediate

**Strategy**: DevTools captures every dispatched action with its full payload, which can accidentally expose tokens, passwords, or personal data in development. The `actionSanitizer` and `actionsDenylist` options let you redact or filter sensitive actions at the store configuration level. Remember that DevTools configuration only applies in development builds -- ensure it does not leak into production.

**Strategy:**
Configure the `devTools` option in `configureStore`. You can use the `actionsDenylist` or `sanitizer` function to filter or mask data.

**Code Example:**
```typescript
const store = configureStore({
  reducer: rootReducer,
  devTools: {
    actionSanitizer: (action) => {
      return action.type === 'LOGIN_SUCCESS' 
        ? { ...action, payload: '<<REDACTED>>' } 
        : action;
    },
  },
});
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q15"></a>
### Q15: How do you implement undo/redo functionality in a Redux store?

**Difficulty**: Advanced

**Strategy**: Undo/redo is a hallmark feature of editing applications (text editors, drawing tools, form builders) and Redux's immutable architecture makes it naturally suited for this. Libraries like `redux-undo` manage a history stack of past, present, and future states. The key consideration is memory -- limit the history depth to avoid storing unbounded state snapshots, and decide which actions should be recorded versus ignored.

**Strategy:**
Use a higher-order reducer (like `redux-undo`). It wraps your reducer and maintains `past`, `present`, and `future` states.

**Code Example:**
```typescript
import undoable from 'redux-undo';

const store = configureStore({
  reducer: {
    counter: undoable(counterReducer),
  },
});

// Dispatch actions
dispatch(ActionCreators.undo());
dispatch(ActionCreators.redo());
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q16"></a>
### Q16: How do you use the DevTools middleware in Zustand?

**Difficulty**: Beginner

**Strategy**: Debugging state changes without visibility into action history is like working blindfolded. Zustand's `devtools` middleware bridges to the familiar Redux DevTools extension, enabling time-travel debugging and action inspection. Pass a descriptive `name` option to identify the store when multiple stores are active. Note that DevTools should only be enabled in development to avoid performance overhead in production.

**Strategy:**
Wrap the store creator with `devtools`. It connects to the Redux DevTools extension.

**Code Example:**
import { devtools } from 'zustand/middleware';

const useStore = create(devtools((set) => ({
  bears: 0,
  increase: () => set((state) => ({ bears: state.bears + 1 }))
}), { name: 'MyStore' }));

[⬆️ Back to Top](#table-of-contents)

---

<a id="q17"></a>
### Q17: How do you create a parameterized selector in Redux?

**Difficulty**: Intermediate

**Strategy**: Components often need to look up data by ID or filter by a dynamic value, so selectors must accept parameters beyond just the state. The straightforward approach passes extra arguments through the second parameter of `useSelector`, but this breaks memoization because the inline arrow function creates a new reference every render. For memoized parameterized selectors, use a selector factory or `createSelector` with the parameter baked into an input selector.

**Strategy:**
Return a function from the selector or use a factory function if memoization is needed per instance.

**Code Example:**
const selectItemById = (state, itemId) => state.items[itemId];

// Usage
const item = useSelector(state => selectItemById(state, props.id));

[⬆️ Back to Top](#table-of-contents)

---

<a id="q18"></a>
### Q18: How do you listen to transient state changes in Zustand without re-rendering?

**Difficulty**: Advanced

**Strategy**: Some state changes need to trigger side effects (logging, analytics, triggering sounds) without re-rendering any UI. Zustand's `subscribe` method runs a callback on every state change independently of React's render cycle. This is useful for analytics tracking or syncing to external systems. Always remember to call the returned unsubscribe function on cleanup to prevent memory leaks.

**Strategy:**
Use `useStore.subscribe`. It allows running logic on state change without causing a component render.

**Code Example:**
useEffect(() => {
  const unsub = useStore.subscribe((state, prevState) => {
    console.log('State changed:', state);
  });
  return unsub;
}, []);

[⬆️ Back to Top](#table-of-contents)

---

<a id="q19"></a>
### Q19: How do you transform API responses in RTK Query?

**Difficulty**: Intermediate

**Strategy**: Backend APIs rarely return data in the exact shape your frontend needs -- they may wrap responses in `{ data, meta }` envelopes or use different naming conventions. The `transformResponse` hook in RTK Query lets you normalize and reshape data at the API layer before it reaches the cache, keeping your components clean. A best practice is to keep transformations lightweight and move heavy computations into memoized selectors.

**Strategy:**
Use `transformResponse` in the endpoint definition.

**Code Example:**
getPost: builder.query({
  query: (id) => `post/${id}`,
  transformResponse: (response: { data: Post }) => response.data,
});

[⬆️ Back to Top](#table-of-contents)

---

<a id="q20"></a>
### Q20: How do you implement Cache Invalidation in RTK Query?

**Difficulty**: Intermediate

**Strategy**: Cache invalidation ensures users see fresh data after mutations without manually refetching everywhere. RTK Query's tag-based system declaratively links queries to data types and automatically refetches affected queries when a mutation invalidates their tag. A common mistake is using overly broad tags (e.g., just `'Post'`) when granular tags (e.g., `{ type: 'Post', id: 5 }`) would avoid unnecessary refetches of unrelated data.

**Strategy:**
Use `providesTags` on queries and `invalidatesTags` on mutations.

**Code Example:**
getPosts: builder.query({
  providesTags: ['Post'],
  query: () => '/posts',
}),
addPost: builder.mutation({
  invalidatesTags: ['Post'],
  query: (body) => ({ url: '/posts', method: 'POST', body }),
});

[⬆️ Back to Top](#table-of-contents)

---

<a id="q21"></a>
### Q21: How do you organize a large Zustand store using Slices?

**Difficulty**: Advanced

**Strategy**: As applications grow, a single monolithic store becomes difficult to maintain. The slice pattern in Zustand splits concerns into independent creator functions that each manage their own state and actions, then combines them at store creation time. This mirrors Redux's slice pattern but with less boilerplate. Keep slices focused on a single domain to avoid tangled cross-slice dependencies.

**Strategy:**
Create separate slice creators and combine them in the main store creation.

**Code Example:**
const createBearSlice = (set) => ({
  bears: 0,
  addBear: () => set((state) => ({ bears: state.bears + 1 })),
});

const createFishSlice = (set) => ({
  fishes: 0,
  addFish: () => set((state) => ({ fishes: state.fishes + 1 })),
});

const useStore = create((...a) => ({
  ...createBearSlice(...a),
  ...createFishSlice(...a),
}));

[⬆️ Back to Top](#table-of-contents)

---

<a id="q22"></a>
### Q22: What is the `prepare` callback in Redux Toolkit reducers?

**Difficulty**: Intermediate

**Strategy**: Action payloads often need preprocessing before reaching the reducer -- generating unique IDs, adding timestamps, or normalizing input. The `prepare` callback separates this concern from the reducer logic, keeping reducers focused solely on state transitions. This is a best practice because it prevents side-effect-like logic from leaking into reducers, which should remain pure and predictable for testing.

**Strategy:**
It allows customizing the payload (e.g., generating IDs, formatting dates) before the action is dispatched.

**Code Example:**
reducers: {
  addPost: {
    reducer: (state, action) => { state.push(action.payload) },
    prepare: (text) => ({
      payload: { id: nanoid(), text, date: new Date().toISOString() }
    }),
  },
}

[⬆️ Back to Top](#table-of-contents)

---

<a id="q23"></a>
### Q23: How do you implement polling in RTK Query?

**Difficulty**: Beginner

**Strategy**: Polling keeps data fresh for real-time-ish features like dashboards, notifications, or job status monitors without requiring WebSocket infrastructure. RTK Query makes this trivial with the `pollingInterval` option. Be mindful of the trade-off: shorter intervals give fresher data but increase server load and battery drain on mobile. Always pair polling with a `skip` condition to stop requests when the component is hidden or data is unchanged.

**Strategy:**
Pass `pollingInterval` (in ms) to the `useQuery` hook.

**Code Example:**
const { data } = useGetStatusQuery(undefined, {
  pollingInterval: 3000,
});

[⬆️ Back to Top](#table-of-contents)

---

<a id="q24"></a>
### Q24: How do you inject an Authentication Token into RTK Query requests?

**Difficulty**: Intermediate

**Strategy**: Almost every production API requires authentication, and manually attaching tokens to every fetch call is error-prone and repetitive. The `prepareHeaders` callback in `fetchBaseQuery` centralizes header injection by reading the token from the Redux store itself. This ensures every request automatically includes the current token, and handles the common case where the token refreshes mid-session.

**Strategy:**
Wrap `fetchBaseQuery` and add the `Authorization` header in the `prepareHeaders` callback.

**Code Example:**
fetchBaseQuery({
  baseUrl: '/api',
  prepareHeaders: (headers, { getState }) => {
    const token = (getState() as RootState).auth.token;
    if (token) headers.set('authorization', `Bearer ${token}`);
    return headers;
  },
});

[⬆️ Back to Top](#table-of-contents)

---

<a id="q25"></a>
### Q25: How do you use Immer manually in Redux Toolkit?

**Difficulty**: Advanced

**Strategy**: While RTK uses Immer internally inside `createSlice` reducers, there are cases where you need immutable updates outside reducers -- in thunks, event handlers, or utility functions. The `createNextState` utility exported by RTK is a re-export of Immer's `produce` function, letting you write mutable-looking code that produces immutable results. Avoid importing Immer separately since RTK already includes it.

**Strategy:**
Use `createNextState` (exported as `produce` usually in Immer) if you need immutable updates outside of reducers.

**Code Example:**
import { createNextState } from '@reduxjs/toolkit';

const nextState = createNextState(baseState, draft => {
  draft.todo = 'done';
});

[⬆️ Back to Top](#table-of-contents)

---

<a id="q26"></a>
### Q26: How do you handle multiple action types in one reducer (RTK)?

**Difficulty**: Intermediate

**Strategy**: Multiple async thunks often share the same loading or error handling logic -- for example, several API calls all need to set `loading = false` on completion. Using `builder.addMatcher` with `isAnyOf` lets a single handler respond to several action types, reducing duplicated reducer code. Keep these shared handlers focused on cross-cutting concerns like loading flags and error state rather than domain-specific logic.

**Strategy:**
Use `builder.addMatcher` with `isAnyOf` in `extraReducers`.

**Code Example:**
builder.addMatcher(
  isAnyOf(action1, action2),
  (state, action) => { state.loading = false; }
);

[⬆️ Back to Top](#table-of-contents)

---

<a id="q27"></a>
### Q27: How do you create a Component-Scoped Zustand Store?

**Difficulty**: Advanced

**Strategy**: Most Zustand stores are global singletons, but some components need their own isolated state -- think of a reusable modal, a rich text editor, or a map widget used multiple times on a page. Creating the store inside the component and distributing it via React Context gives each instance its own independent state. Use `useRef` to ensure the store is created only once per component mount, not on every render.

**Strategy:**
Create the store inside a component (or factory) and pass it via React Context. This prevents sharing state across all instances of the component.

**Code Example:**
const StoreContext = createContext(null);

const Provider = ({ children }) => {
  const storeRef = useRef(createStore(...));
  return <StoreContext.Provider value={storeRef.current}>{children}</StoreContext.Provider>;
};

[⬆️ Back to Top](#table-of-contents)

---

<a id="q28"></a>
### Q28: How do you prefetch data with RTK Query?

**Difficulty**: Intermediate

**Strategy**: Prefetching eliminates perceived loading time by fetching data before the user navigates to a page -- for example, on link hover or button focus. The `usePrefetch` hook triggers a query and caches the result so it is instantly available when the target component mounts. Be judicious with prefetching; fetching too aggressively wastes bandwidth and can overload the server on data-heavy pages with many interactive elements.

**Strategy:**
Use the `usePrefetch` hook or dispatch `initiate` manually.

**Code Example:**
const prefetchUser = usePrefetch('getUser');

<button onMouseEnter={() => prefetchUser(id)}>Hover to load</button>

[⬆️ Back to Top](#table-of-contents)

---

<a id="q29"></a>
### Q29: How do you code-split RTK Query endpoints?

**Difficulty**: Advanced

**Strategy**: In large applications, defining all API endpoints in one file creates a massive bundle and forces unrelated teams to share a single file. The `injectEndpoints` method lets you define an empty base API and extend it from feature-specific modules. This aligns endpoint definitions with the features that use them and enables lazy-loading of API definitions alongside route-based code splitting.

**Strategy:**
Use `injectEndpoints`. Create an empty API slice first, then inject endpoints in separate files.

**Code Example:**
// emptyApi.ts
export const api = createApi({ endpoints: () => ({}) });

// extendedApi.ts
const extendedApi = api.injectEndpoints({
  endpoints: (build) => ({
    getPosts: build.query(...)
  }),
});

[⬆️ Back to Top](#table-of-contents)

---

<a id="q30"></a>
### Q30: How do you debug the current state in an RTK reducer?

**Difficulty**: Beginner

**Strategy**: RTK uses Immer under the hood, which wraps state in Proxy objects that cannot be inspected with a simple `console.log`. Using `console.log(state)` shows `{[Proxy object]}` instead of actual values. The `current` utility from RTK unwraps the proxy into a plain snapshot you can inspect. This is a development-only tool -- never use `current` in production logic since it creates a deep copy on every call.

**Strategy:**
Use the `current` utility to unwrap the Immer draft proxy and log the plain JS object.

**Code Example:**
import { current } from '@reduxjs/toolkit';

// Inside reducer
console.log(current(state));

[⬆️ Back to Top](#table-of-contents)

---

<a id="q31"></a>
### Q31: How do you skip a query in RTK Query?

**Difficulty**: Beginner

**Strategy**: Queries should not fire until their required parameters are available -- calling `useGetUserQuery(undefined)` would fetch with an invalid URL. The `skip` option (or `skipToken`) conditionally pauses the query, returning `isUninitialized` status without making a network request. This is especially important for dependent queries where one API call's response provides the parameter for the next.

**Strategy:**
Use the `skip` option (boolean) or pass `skipToken`.

**Code Example:**
const { data } = useGetUserQuery(id, { skip: !id });

[⬆️ Back to Top](#table-of-contents)

---

<a id="q32"></a>
### Q32: How do you automatically refetch data on window focus?

**Difficulty**: Beginner

**Strategy**: Users often switch between tabs while working, and stale data on return can cause confusion -- think of a dashboard where a colleague updated a record. RTK Query's `refetchOnFocus` detects when the browser tab regains focus and refetches active queries automatically. Call `setupListeners(store.dispatch)` once during store setup to enable this globally, or set it per-hook for granular control.

**Strategy:**
Enable `refetchOnFocus: true` in `setupListeners` or individual query options.

**Code Example:**
setupListeners(store.dispatch); // Global setup

// or per hook
useQuery(id, { refetchOnFocus: true });

[⬆️ Back to Top](#table-of-contents)

---

<a id="q33"></a>
### Q33: How do you use the Immer middleware in Zustand?

**Difficulty**: Intermediate

**Strategy**: Deeply nested state updates in vanilla JavaScript require verbose spread operators that are error-prone and hard to read. Zustand's `immer` middleware lets you mutate the draft directly, and Immer produces an immutable update behind the scenes. This drastically simplifies nested object updates. Keep in mind that Immer has restrictions on what can be mutated -- never return a mix of draft mutations and new objects from the same `set` call.

**Strategy:**
Wrap the setter with `immer`. It allows mutating state directly.

**Code Example:**
import { immer } from 'zustand/middleware/immer';

const useStore = create(immer((set) => ({
  nested: { count: 0 },
  inc: () => set((state) => { state.nested.count += 1 }),
})));

[⬆️ Back to Top](#table-of-contents)

---

<a id="q34"></a>
### Q34: How do you inject extra arguments (like an API client) into Thunks?

**Difficulty**: Intermediate

**Strategy**: Hard-coding API calls inside thunks makes them difficult to test and couples business logic to a specific HTTP client. The `extraArgument` configuration in RTK's thunk middleware lets you inject a shared API client, allowing thunks to access it via `thunkAPI.extra`. This pattern enables dependency injection, making thunks testable by passing mock clients without modifying module-level imports.

**Strategy:**
Use `thunk.extraArgument` in `configureStore`.

**Code Example:**
const store = configureStore({
  middleware: (getDefault) => getDefault({
    thunk: { extraArgument: myApiClient }
  })
});

[⬆️ Back to Top](#table-of-contents)

---

<a id="q35"></a>
### Q35: How do you bypass `baseQuery` for a specific endpoint in RTK Query?

**Difficulty**: Advanced

**Strategy**: Not every API call fits the standard REST pattern your `baseQuery` is configured for -- you may need to call a GraphQL endpoint, use a Firebase SDK, or read from IndexedDB. The `queryFn` option replaces the standard `query` + `baseQuery` pipeline entirely for that endpoint, giving you full control over the data fetching logic while still benefiting from RTK Query's caching and loading state management.

**Strategy:**
Provide a `queryFn` instead of `query`. Useful for one-off logic or Firebase SDK calls.

**Code Example:**
getCustomData: builder.query({
  queryFn: async (arg) => {
    const data = await someSdkFunction(arg);
    return { data };
  },
});

[⬆️ Back to Top](#table-of-contents)

---

<a id="q36"></a>
### Q36: How do you optimize RTK Query selection performance?

**Difficulty**: Advanced

**Strategy**: By default, `useQuery` hooks return the entire cached result object including metadata like `isLoading` and `isFetching`. When a component only needs a single field (e.g., one post from a list), any change to the cache triggers a re-render even if that specific field is unchanged. The `selectFromResult` option narrows what the component subscribes to, preventing re-renders from unrelated cache updates. Combine this with memoization for the best performance.

**Strategy:**
Use `selectFromResult` to return a specific subset of data and prevent re-renders if other fields change.

**Code Example:**
useGetPostsQuery(undefined, {
  selectFromResult: ({ data }) => ({
    post: data?.find(p => p.id === id)
  }),
});

[⬆️ Back to Top](#table-of-contents)

---

<a id="q37"></a>
### Q37: How do you handle optimistic updates in Zustand?

**Difficulty**: Intermediate

**Strategy**: Zustand makes optimistic updates straightforward since you can call `set` synchronously and then revert in a `catch` block -- no middleware required. The critical pattern is always capturing the previous state before the optimistic update so you have a guaranteed rollback path. For concurrent updates, consider using a queue or version counter to prevent a stale rollback from overwriting a newer successful update.

**Strategy:**
Update state immediately, try the async action, and revert if it fails.

**Code Example:**
update: async (val) => {
  const old = get().val;
  set({ val }); // Optimistic
  try {
    await api.update(val);
  } catch {
    set({ val: old }); // Rollback
  }
}

[⬆️ Back to Top](#table-of-contents)

---

<a id="q38"></a>
### Q38: How do you reset the RTK Query cache?

**Difficulty**: Intermediate

**Strategy**: After a user logs out or switches accounts, cached API data from the previous session must be cleared to prevent cross-contamination. The `resetApiState` utility clears all cached data and unsubscribes from ongoing queries in one dispatch. Combine this with the root state reset pattern (Q12) for a complete logout flow that clears both local state and API cache.

**Strategy:**
Dispatch `api.util.resetApiState()`.

**Code Example:**
dispatch(api.util.resetApiState());

[⬆️ Back to Top](#table-of-contents)

---

<a id="q39"></a>
### Q39: How do you use `combine` middleware in Zustand for type inference?

**Difficulty**: Advanced

**Strategy**: Zustand's TypeScript inference can struggle with stores that mix state and action properties, often requiring explicit type annotations. The `combine` middleware solves this by separating the initial state object from the action creators, allowing TypeScript to infer the full store type automatically. This eliminates the need for manual interface definitions and keeps the type in sync with the store definition by construction.

**Strategy:**
`combine` merges an initial state object with actions, allowing TypeScript to infer types automatically without explicit interface definitions.

**Code Example:**
import { combine } from 'zustand/middleware';

const useStore = create(combine(
  { count: 0 },
  (set) => ({ inc: () => set(s => ({ count: s.count + 1 })) })
));

[⬆️ Back to Top](#table-of-contents)

---

<a id="q40"></a>
### Q40: How do you ensure strict state immutability checks in Redux Toolkit?

**Difficulty**: Beginner

**Strategy**: Accidental state mutations are one of the most common and hardest-to-debug Redux issues -- mutating state directly can cause components not to re-render or re-render with stale data. RTK's `immutableStateInvariantMiddleware` runs in development and throws immediately if it detects a mutation outside of an Immer-powered reducer. Never disable this in development; the runtime cost is negligible compared to the debugging time it saves.

**Strategy:**
RTK enables `immutableStateInvariantMiddleware` by default in development. It throws errors if you mutate state outside of Immer reducers.

**Code Example:**
// Enabled by default.
// To disable (not recommended):
getDefaultMiddleware({ immutableCheck: false })

[⬆️ Back to Top](#table-of-contents)

---

<a id="q41"></a>
### Q41: How do you perform Server-Side Rendering (SSR) with Redux Toolkit?

**Difficulty**: Advanced

**Strategy**: SSR with Redux requires creating a fresh store per request to prevent data leakage between users, dispatching all necessary async actions, waiting for them to resolve, then serializing the state into the HTML for client-side rehydration. RTK Query simplifies this with `getRunningQueriesThunk` to await all in-flight queries. The most common pitfall is sharing a single store instance across requests, which causes cross-user state contamination.

**Strategy:**
Initialize the store on the server, dispatch actions, wait for completion, and serialize the state to `preloadedState` on the client.

**Code Example:**
// Server
await Promise.all(store.dispatch(api.util.getRunningQueriesThunk()));
const preloadedState = store.getState();

[⬆️ Back to Top](#table-of-contents)

---

<a id="q42"></a>
### Q42: How do you perform Server-Side Rendering (SSR) with Zustand?

**Difficulty**: Advanced

**Strategy**: Zustand's simplicity makes SSR straightforward since stores are plain objects without provider wrappers, but the `persist` middleware with `localStorage` will crash on the server where `localStorage` does not exist. Use `skipHydration` to defer rehydration to a `useEffect` on the client, or provide a custom storage adapter that returns an in-memory object on the server. Always create a new store instance per server request.

**Strategy:**
Avoid using `persist` with `localStorage` directly on server. Use `skipHydration` or a custom storage adapter that handles SSR.

**Code Example:**
// Skip hydration on init, hydrate in useEffect

[⬆️ Back to Top](#table-of-contents)

---

<a id="q43"></a>
### Q43: How do you use the `autoBatchEnhancer` in Redux Toolkit?

**Difficulty**: Advanced

**Strategy**: When multiple dispatches fire in quick succession (e.g., receiving a WebSocket message that updates several slices), each dispatch triggers a separate React re-render, causing unnecessary layout thrashing. The `autoBatchEnhancer` batches low-priority notifications so React processes them in a single render pass. This is particularly valuable for high-frequency updates like real-time dashboards, where reducing render count directly improves frame rate.

**Strategy:**
It allows low-priority state updates to be batched together, reducing notify subscribers calls. Enabled via `enhancers`.

**Code Example:**
configureStore({
  enhancers: (defaultEnhancers) => defaultEnhancers.concat(autoBatchEnhancer()),
});

[⬆️ Back to Top](#table-of-contents)

---

<a id="q44"></a>
### Q44: How do you test a Zustand store?

**Difficulty**: Intermediate

**Strategy**: Zustand stores can be tested two ways: via `getState()`/`setState()` as plain objects (fastest, no React needed), or through `renderHook` to test the hook integration. For unit tests of store logic, the vanilla approach is preferred because it avoids React rendering overhead entirely. When tests share a module-level store, always reset state between tests to prevent leakage -- use `setState` with initial values in an `afterEach` block.

**Strategy:**
Since it's a hook, use `renderHook` from `@testing-library/react-hooks` or test the vanilla store via `useStore.getState()`.

**Code Example:**
const { result } = renderHook(() => useStore());
act(() => result.current.inc());
expect(result.current.count).toBe(1);

[⬆️ Back to Top](#table-of-contents)

---

<a id="q45"></a>
### Q45: How do you wait for a specific action in Redux?

**Difficulty**: Advanced

**Strategy**: Complex workflows often need to pause until another action completes -- for example, waiting for an authentication success before fetching user data. The `createListenerMiddleware` provides a `condition` method that returns a promise resolving when the matching action is dispatched, enabling sequential async flows without chaining thunks manually. This replaces older patterns like redux-saga's `take` with a built-in RTK solution.

**Strategy:**
Use `listenerMiddleware` with `condition` or `take` effect.

**Code Example:**
await listenerApi.condition((action) => action.type === 'Success');

[⬆️ Back to Top](#table-of-contents)

---

<a id="q46"></a>
### Q46: How do you use `mutative` with Zustand?

**Difficulty**: Intermediate

**Strategy**: `mutative` is an alternative to Immer that provides the same mutable-draft API but with significantly better performance for large state objects. It is particularly useful in Zustand stores with deep or complex state where Immer's proxy overhead becomes noticeable. The API surface is nearly identical, making it a drop-in replacement in most cases, though you should benchmark your specific use case before switching.

**Strategy:**
Similar to Immer, wrap the setter. `mutative` is often faster.

**Code Example:**
// Implementation depends on middleware wrapper

[⬆️ Back to Top](#table-of-contents)

---

<a id="q47"></a>
### Q47: How do you create a bidirectional sync between Redux and URL params?

**Difficulty**: Advanced

**Strategy**: URL parameters serve as shareable, bookmarkable state -- filters, pagination, and sort order should survive page reloads and be shareable via link. Bidirectional sync means dispatching a Redux action updates the URL, and a browser back/forward navigation updates Redux. The main challenge is preventing infinite loops where a URL change triggers a Redux action that tries to update the URL again. Use a guard flag or compare values before syncing.

**Strategy:**
Use a listener that updates URL when state changes, and a router listener that dispatches actions when URL changes.

**Code Example:**
// Listener middleware
listenerApi.dispatch(updateUrl(action.payload));

[⬆️ Back to Top](#table-of-contents)

---

<a id="q48"></a>
### Q48: How do you handle non-serializable data in Redux?

**Difficulty**: Intermediate

**Strategy**: Redux requires serializable state for features like time-travel debugging, persistence, and hydration to work correctly. Non-serializable values like `Date` objects, `Map`/`Set`, functions, or class instances will cause warnings and break DevTools. The best practice is to store serializable representations (ISO strings instead of Date objects, plain objects instead of Maps) and convert at the boundary. Only disable `serializableCheck` as a last resort.

**Strategy:**
Avoid putting it in the store. If necessary, disable the `serializableCheck` middleware.

**Code Example:**
getDefaultMiddleware({ serializableCheck: false })

[⬆️ Back to Top](#table-of-contents)

---

<a id="q49"></a>
### Q49: How do you implement a 'Draft' feature using Redux?

**Difficulty**: Intermediate

**Strategy**: Draft patterns are used in forms and editors where users edit a copy of existing data without modifying the canonical state until they explicitly save. Maintaining a separate draft slice isolates temporary edits from the main data, preventing partial updates from being visible to other components. On cancel, simply discard the draft; on save, copy the draft to the main slice and clear it. This avoids complex undo logic for form workflows.

**Strategy:**
Keep a separate slice for the draft state. Sync it with the original data on 'Edit' and commit it on 'Save'.

**Code Example:**
// draftSlice

[⬆️ Back to Top](#table-of-contents)

---

<a id="q50"></a>
### Q50: How do you use `createStore` (Vanilla) in Zustand?

**Difficulty**: Intermediate

**Strategy**: Not every state management scenario involves React -- you might need shared state in a service worker, a Node.js backend, or a non-React UI library. Zustand's `createStore` (from `zustand/vanilla`) creates a standalone store with `getState`, `setState`, and `subscribe` but no React hook binding. You can later wrap it with `useStore` from `zustand` if React integration is needed, making it a flexible choice for library code that may be consumed by different frameworks.

**Strategy:**
Import `createStore` instead of `create`. Useful for non-React usage.

**Code Example:**
import { createStore } from 'zustand/vanilla';
const store = createStore(() => ({ count: 0 }));
store.subscribe(console.log);

[⬆️ Back to Top](#table-of-contents)
