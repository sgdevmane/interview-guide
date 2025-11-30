## Table of Contents

1. [How do you minimize unnecessary re-renders in a React component using Zustand?](#q1-how-do-you-minimize-unnecessary-re-renders-in-a-react-component-using-zustand) <span class="intermediate">Intermediate</span>
2. [How do you implement optimistic UI updates using Redux Toolkit (RTK)?](#q2-how-do-you-implement-optimistic-ui-updates-using-redux-toolkit-rtk) <span class="advanced">Advanced</span>
3. [How do you persist Zustand state to `localStorage` and rehydrate it on app start?](#q3-how-do-you-persist-zustand-state-to-localstorage-and-rehydrate-it-on-app-start) <span class="beginner">Beginner</span>
4. [How do you handle complex asynchronous logic (like debouncing or cancellation) in Redux Toolkit?](#q4-how-do-you-handle-complex-asynchronous-logic-like-debouncing-or-cancellation-in-redux-toolkit) <span class="advanced">Advanced</span>
5. [How do you normalize nested API data (e.g., Users with Posts) in a Redux store?](#q5-how-do-you-normalize-nested-api-data-eg-users-with-posts-in-a-redux-store) <span class="intermediate">Intermediate</span>
6. [How do you type a Redux Toolkit slice and dispatch correctly in TypeScript?](#q6-how-do-you-type-a-redux-toolkit-slice-and-dispatch-correctly-in-typescript) <span class="beginner">Beginner</span>
7. [How do you access the Zustand store state outside of a React component (e.g., in a utility function)?](#q7-how-do-you-access-the-zustand-store-state-outside-of-a-react-component-eg-in-a-utility-function) <span class="intermediate">Intermediate</span>
8. [How do you split a large Redux store into manageable chunks (Code Splitting)?](#q8-how-do-you-split-a-large-redux-store-into-manageable-chunks-code-splitting) <span class="advanced">Advanced</span>
9. [How do you unit test a Redux Toolkit slice logic?](#q9-how-do-you-unit-test-a-redux-toolkit-slice-logic) <span class="intermediate">Intermediate</span>
10. [How do you handle side effects in Zustand without middleware?](#q10-how-do-you-handle-side-effects-in-zustand-without-middleware) <span class="beginner">Beginner</span>
11. [How do you create a 'derived state' selector in Redux that is memoized?](#q11-how-do-you-create-a-derived-state-selector-in-redux-that-is-memoized) <span class="intermediate">Intermediate</span>
12. [How do you reset the entire Redux state (e.g., on user logout)?](#q12-how-do-you-reset-the-entire-redux-state-eg-on-user-logout) <span class="intermediate">Intermediate</span>
13. [How do you share state between multiple tabs/windows using Zustand?](#q13-how-do-you-share-state-between-multiple-tabswindows-using-zustand) <span class="advanced">Advanced</span>
14. [How do you prevent a specific Redux action from being logged in DevTools (e.g., sensitive data)?](#q14-how-do-you-prevent-a-specific-redux-action-from-being-logged-in-devtools-eg-sensitive-data) <span class="intermediate">Intermediate</span>
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

### Q1: How do you minimize unnecessary re-renders in a React component using Zustand?

**Difficulty**: Intermediate

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

### Q2: How do you implement optimistic UI updates using Redux Toolkit (RTK)?

**Difficulty**: Advanced

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

### Q3: How do you persist Zustand state to `localStorage` and rehydrate it on app start?

**Difficulty**: Beginner

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

### Q4: How do you handle complex asynchronous logic (like debouncing or cancellation) in Redux Toolkit?

**Difficulty**: Advanced

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

### Q5: How do you normalize nested API data (e.g., Users with Posts) in a Redux store?

**Difficulty**: Intermediate

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

### Q6: How do you type a Redux Toolkit slice and dispatch correctly in TypeScript?

**Difficulty**: Beginner

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

### Q7: How do you access the Zustand store state outside of a React component (e.g., in a utility function)?

**Difficulty**: Intermediate

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

### Q8: How do you split a large Redux store into manageable chunks (Code Splitting)?

**Difficulty**: Advanced

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

### Q9: How do you unit test a Redux Toolkit slice logic?

**Difficulty**: Intermediate

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

### Q10: How do you handle side effects in Zustand without middleware?

**Difficulty**: Beginner

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

### Q11: How do you create a 'derived state' selector in Redux that is memoized?

**Difficulty**: Intermediate

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

### Q12: How do you reset the entire Redux state (e.g., on user logout)?

**Difficulty**: Intermediate

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

### Q13: How do you share state between multiple tabs/windows using Zustand?

**Difficulty**: Advanced

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

### Q14: How do you prevent a specific Redux action from being logged in DevTools (e.g., sensitive data)?

**Difficulty**: Intermediate

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

### Q15: How do you implement undo/redo functionality in a Redux store?

**Difficulty**: Advanced

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

### Q16: How do you use the DevTools middleware in Zustand?

**Difficulty**: Beginner

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

### Q17: How do you create a parameterized selector in Redux?

**Difficulty**: Intermediate

**Strategy:**
Return a function from the selector or use a factory function if memoization is needed per instance.

**Code Example:**
const selectItemById = (state, itemId) => state.items[itemId];

// Usage
const item = useSelector(state => selectItemById(state, props.id));

[⬆️ Back to Top](#table-of-contents)

---

### Q18: How do you listen to transient state changes in Zustand without re-rendering?

**Difficulty**: Advanced

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

### Q19: How do you transform API responses in RTK Query?

**Difficulty**: Intermediate

**Strategy:**
Use `transformResponse` in the endpoint definition.

**Code Example:**
getPost: builder.query({
  query: (id) => `post/${id}`,
  transformResponse: (response: { data: Post }) => response.data,
});

[⬆️ Back to Top](#table-of-contents)

---

### Q20: How do you implement Cache Invalidation in RTK Query?

**Difficulty**: Intermediate

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

### Q21: How do you organize a large Zustand store using Slices?

**Difficulty**: Advanced

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

### Q22: What is the `prepare` callback in Redux Toolkit reducers?

**Difficulty**: Intermediate

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

### Q23: How do you implement polling in RTK Query?

**Difficulty**: Beginner

**Strategy:**
Pass `pollingInterval` (in ms) to the `useQuery` hook.

**Code Example:**
const { data } = useGetStatusQuery(undefined, {
  pollingInterval: 3000,
});

[⬆️ Back to Top](#table-of-contents)

---

### Q24: How do you inject an Authentication Token into RTK Query requests?

**Difficulty**: Intermediate

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

### Q25: How do you use Immer manually in Redux Toolkit?

**Difficulty**: Advanced

**Strategy:**
Use `createNextState` (exported as `produce` usually in Immer) if you need immutable updates outside of reducers.

**Code Example:**
import { createNextState } from '@reduxjs/toolkit';

const nextState = createNextState(baseState, draft => {
  draft.todo = 'done';
});

[⬆️ Back to Top](#table-of-contents)

---

### Q26: How do you handle multiple action types in one reducer (RTK)?

**Difficulty**: Intermediate

**Strategy:**
Use `builder.addMatcher` with `isAnyOf` in `extraReducers`.

**Code Example:**
builder.addMatcher(
  isAnyOf(action1, action2),
  (state, action) => { state.loading = false; }
);

[⬆️ Back to Top](#table-of-contents)

---

### Q27: How do you create a Component-Scoped Zustand Store?

**Difficulty**: Advanced

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

### Q28: How do you prefetch data with RTK Query?

**Difficulty**: Intermediate

**Strategy:**
Use the `usePrefetch` hook or dispatch `initiate` manually.

**Code Example:**
const prefetchUser = usePrefetch('getUser');

<button onMouseEnter={() => prefetchUser(id)}>Hover to load</button>

[⬆️ Back to Top](#table-of-contents)

---

### Q29: How do you code-split RTK Query endpoints?

**Difficulty**: Advanced

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

### Q30: How do you debug the current state in an RTK reducer?

**Difficulty**: Beginner

**Strategy:**
Use the `current` utility to unwrap the Immer draft proxy and log the plain JS object.

**Code Example:**
import { current } from '@reduxjs/toolkit';

// Inside reducer
console.log(current(state));

[⬆️ Back to Top](#table-of-contents)

---

### Q31: How do you skip a query in RTK Query?

**Difficulty**: Beginner

**Strategy:**
Use the `skip` option (boolean) or pass `skipToken`.

**Code Example:**
const { data } = useGetUserQuery(id, { skip: !id });

[⬆️ Back to Top](#table-of-contents)

---

### Q32: How do you automatically refetch data on window focus?

**Difficulty**: Beginner

**Strategy:**
Enable `refetchOnFocus: true` in `setupListeners` or individual query options.

**Code Example:**
setupListeners(store.dispatch); // Global setup

// or per hook
useQuery(id, { refetchOnFocus: true });

[⬆️ Back to Top](#table-of-contents)

---

### Q33: How do you use the Immer middleware in Zustand?

**Difficulty**: Intermediate

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

### Q34: How do you inject extra arguments (like an API client) into Thunks?

**Difficulty**: Intermediate

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

### Q35: How do you bypass `baseQuery` for a specific endpoint in RTK Query?

**Difficulty**: Advanced

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

### Q36: How do you optimize RTK Query selection performance?

**Difficulty**: Advanced

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

### Q37: How do you handle optimistic updates in Zustand?

**Difficulty**: Intermediate

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

### Q38: How do you reset the RTK Query cache?

**Difficulty**: Intermediate

**Strategy:**
Dispatch `api.util.resetApiState()`.

**Code Example:**
dispatch(api.util.resetApiState());

[⬆️ Back to Top](#table-of-contents)

---

### Q39: How do you use `combine` middleware in Zustand for type inference?

**Difficulty**: Advanced

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

### Q40: How do you ensure strict state immutability checks in Redux Toolkit?

**Difficulty**: Beginner

**Strategy:**
RTK enables `immutableStateInvariantMiddleware` by default in development. It throws errors if you mutate state outside of Immer reducers.

**Code Example:**
// Enabled by default.
// To disable (not recommended):
getDefaultMiddleware({ immutableCheck: false })

[⬆️ Back to Top](#table-of-contents)

---

### Q41: How do you perform Server-Side Rendering (SSR) with Redux Toolkit?

**Difficulty**: Advanced

**Strategy:**
Initialize the store on the server, dispatch actions, wait for completion, and serialize the state to `preloadedState` on the client.

**Code Example:**
// Server
await Promise.all(store.dispatch(api.util.getRunningQueriesThunk()));
const preloadedState = store.getState();

[⬆️ Back to Top](#table-of-contents)

---

### Q42: How do you perform Server-Side Rendering (SSR) with Zustand?

**Difficulty**: Advanced

**Strategy:**
Avoid using `persist` with `localStorage` directly on server. Use `skipHydration` or a custom storage adapter that handles SSR.

**Code Example:**
// Skip hydration on init, hydrate in useEffect

[⬆️ Back to Top](#table-of-contents)

---

### Q43: How do you use the `autoBatchEnhancer` in Redux Toolkit?

**Difficulty**: Advanced

**Strategy:**
It allows low-priority state updates to be batched together, reducing notify subscribers calls. Enabled via `enhancers`.

**Code Example:**
configureStore({
  enhancers: (defaultEnhancers) => defaultEnhancers.concat(autoBatchEnhancer()),
});

[⬆️ Back to Top](#table-of-contents)

---

### Q44: How do you test a Zustand store?

**Difficulty**: Intermediate

**Strategy:**
Since it's a hook, use `renderHook` from `@testing-library/react-hooks` or test the vanilla store via `useStore.getState()`.

**Code Example:**
const { result } = renderHook(() => useStore());
act(() => result.current.inc());
expect(result.current.count).toBe(1);

[⬆️ Back to Top](#table-of-contents)

---

### Q45: How do you wait for a specific action in Redux?

**Difficulty**: Advanced

**Strategy:**
Use `listenerMiddleware` with `condition` or `take` effect.

**Code Example:**
await listenerApi.condition((action) => action.type === 'Success');

[⬆️ Back to Top](#table-of-contents)

---

### Q46: How do you use `mutative` with Zustand?

**Difficulty**: Intermediate

**Strategy:**
Similar to Immer, wrap the setter. `mutative` is often faster.

**Code Example:**
// Implementation depends on middleware wrapper

[⬆️ Back to Top](#table-of-contents)

---

### Q47: How do you create a bidirectional sync between Redux and URL params?

**Difficulty**: Advanced

**Strategy:**
Use a listener that updates URL when state changes, and a router listener that dispatches actions when URL changes.

**Code Example:**
// Listener middleware
listenerApi.dispatch(updateUrl(action.payload));

[⬆️ Back to Top](#table-of-contents)

---

### Q48: How do you handle non-serializable data in Redux?

**Difficulty**: Intermediate

**Strategy:**
Avoid putting it in the store. If necessary, disable the `serializableCheck` middleware.

**Code Example:**
getDefaultMiddleware({ serializableCheck: false })

[⬆️ Back to Top](#table-of-contents)

---

### Q49: How do you implement a 'Draft' feature using Redux?

**Difficulty**: Intermediate

**Strategy:**
Keep a separate slice for the draft state. Sync it with the original data on 'Edit' and commit it on 'Save'.

**Code Example:**
// draftSlice

[⬆️ Back to Top](#table-of-contents)

---

### Q50: How do you use `createStore` (Vanilla) in Zustand?

**Difficulty**: Intermediate

**Strategy:**
Import `createStore` instead of `create`. Useful for non-React usage.

**Code Example:**
import { createStore } from 'zustand/vanilla';
const store = createStore(() => ({ count: 0 }));
store.subscribe(console.log);

[⬆️ Back to Top](#table-of-contents)

---

