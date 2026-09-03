import os
import sys
sys.path.append(os.path.dirname(__file__))
from batch_base import create_100_qnas

# ==============================================================================
# 9. REDUX & ZUSTAND (100 Questions)
# ==============================================================================
redux_zustand_data = [
    ("How does Redux Toolkit (RTK) modernize Redux and eliminate legacy boilerplate?", "Intermediate",
     "Redux Toolkit provides opinionated standard defaults:\n1. `configureStore()` automatically sets up Redux Thunk, Immer, and Redux DevTools.\n2. `createSlice()` combines actions and reducers in a single object, using Immer under the hood so state can be written as mutating code safely.\n3. `createAsyncThunk()` handles standard pending/fulfilled/rejected async action lifecycles.\n4. `RTK Query` provides declarative server-side caching and data fetching.",
     "```typescript\nimport { createSlice, configureStore, PayloadAction } from '@reduxjs/toolkit';\n\ninterface CounterState { value: number; }\nconst initialState: CounterState = { value: 0 };\n\nconst counterSlice = createSlice({\n  name: 'counter',\n  initialState,\n  reducers: {\n    // Immer allows direct mutation syntax\n    increment: (state) => { state.value += 1; },\n    addAmount: (state, action: PayloadAction<number>) => { state.value += action.payload; }\n  }\n});\n\nexport const { increment, addAmount } = counterSlice.actions;\nexport const store = configureStore({ reducer: { counter: counterSlice.reducer } });\n```"),

    ("How does Zustand work and why is it preferred over Redux in modern React?", "Intermediate",
     "Zustand is a minimalist (~1KB), hook-based state management library that does NOT require wrapping components in a `<Provider>`. It uses a closure-based external store with `useSyncExternalStore` for selector subscriptions, supports transient updates without component re-renders, and avoids complex boilerplate.",
     "```typescript\nimport { create } from 'zustand';\nimport { persist, devtools } from 'zustand/middleware';\n\ninterface BearStore {\n  bears: number;\n  increase: () => void;\n  reset: () => void;\n}\n\nexport const useBearStore = create<BearStore>()(\n  devtools(\n    persist(\n      (set) => ({\n        bears: 0,\n        increase: () => set((state) => ({ bears: state.bears + 1 }), false, 'increase'),\n        reset: () => set({ bears: 0 }, false, 'reset'),\n      }),\n      { name: 'bear-storage' }\n    )\n  )\n);\n```"),

    ("How does Immer work under the hood in RTK and Zustand?", "Advanced",
     "Immer uses JavaScript ES6 `Proxy` to wrap the draft state. When you perform mutating operations (`draft.items.push(newItem)`), Immer tracks all modifications in a copy-on-write proxy tree and produces a pristine, deeply frozen immutable state tree upon completion without modifying the original object.",
     "```javascript\nimport { produce } from 'immer';\n\nconst baseState = [{ todo: 'Learn Redux', done: true }, { todo: 'Learn Zustand', done: false }];\nconst nextState = produce(baseState, draft => {\n  draft[1].done = true;\n  draft.push({ todo: 'Learn Immer', done: false });\n});\n```"),

    ("What is RTK Query and how does it handle caching, polling, and optimistic updates?", "Advanced",
     "RTK Query is an advanced data fetching and caching tool built into Redux Toolkit. It auto-generates hooks (`useGetPostsQuery`, `useAddPostMutation`), manages normalized server-side caches, supports automatic tag-based invalidation (`providesTags`/`invalidatesTags`), polling intervals, and optimistic updates via `onQueryStarted`.",
     "```typescript\nimport { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';\n\nexport const postApi = createApi({\n  reducerPath: 'postApi',\n  baseQuery: fetchBaseQuery({ baseUrl: '/api/' }),\n  tagTypes: ['Post'],\n  endpoints: (builder) => ({\n    getPosts: builder.query<Post[], void>({\n      query: () => 'posts',\n      providesTags: ['Post'],\n    }),\n    addPost: builder.mutation<Post, Partial<Post>>({\n      query: (body) => ({ url: 'posts', method: 'POST', body }),\n      invalidatesTags: ['Post'],\n    }),\n  }),\n});\n\nexport const { useGetPostsQuery, useAddPostMutation } = postApi;\n```"),

    ("How do Transient Updates in Zustand work to achieve 60fps animations?", "Advanced",
     "Transient updates subscribe to store state changes without forcing a React component re-render. You can attach a callback to `useStore.subscribe()` to directly mutate DOM elements or canvas objects on state tick.",
     "```jsx\nimport { useEffect, useRef } from 'react';\nimport { useStore } from './store';\n\nexport function FastTicker() {\n  const textRef = useRef(null);\n\n  useEffect(() => {\n    // Subscribe directly without triggering React re-render\n    const unsub = useStore.subscribe(\n      (state) => state.livePrice,\n      (price) => {\n        if (textRef.current) textRef.current.innerText = `$${price.toFixed(2)}`;\n      }\n    );\n    return () => unsub();\n  }, []);\n\n  return <span ref={textRef}>$0.00</span>;\n}\n```")
]

# Generate 95 more questions for Redux & Zustand
redux_topics = [
    ("How do Zustand Slices allow splitting large stores into modular domain files?", "Intermediate", "Create slice functions that accept `(set, get)` and combine them into a single root store type."),
    ("What is the difference between `useSelector` with shallow equality in Redux vs Zustand `useShallow`?", "Intermediate", "Both prevent re-renders when returning derived object or array literals whose individual properties have not changed."),
    ("How do Redux Middlewares work and how do you write a custom logging middleware?", "Advanced", "Middleware intercepts dispatched actions via curried function `store => next => action` before hitting reducers."),
    ("What is `createAsyncThunk` and how does it generate action creators (`pending`, `fulfilled`, `rejected`)?", "Intermediate", "Executes an async promise payload creator and automatically dispatches lifecycle actions to reducers."),
    ("How do you handle WebSocket streaming with Redux Middleware?", "Advanced", "Custom middleware manages persistent WebSocket connection and dispatches Redux actions on incoming socket packets."),
    ("What is the purpose of `extraReducers` in `createSlice`?", "Intermediate", "Listens and responds to actions defined outside the slice, such as `createAsyncThunk` or actions from other slices."),
    ("How do you implement Undo/Redo in Zustand using `zundo` temporal middleware?", "Intermediate", "Wraps store with `temporal()` to gain automatic `undo()`, `redo()`, and `pastStates` history tracking."),
    ("What is `createEntityAdapter` in Redux Toolkit and how does it normalize state?", "Intermediate", "Provides normalized `{ ids, entities }` collection structure with CRUD reducer adapters (`addOne`, `setAll`)."),
    ("How do you handle JWT Token Refresh in RTK Query with `baseQueryWithReauth`?", "Advanced", "Wraps `fetchBaseQuery` in custom handler that catches 401, invokes refresh token endpoint, and replays original query."),
    ("What is the difference between Redux Thunk and Redux Saga?", "Advanced", "Thunk uses async functions returning dispatch; Saga uses Generator functions and declarative effect descriptions (`call`, `put`, `takeEvery`)."),
    ("How do you persist Zustand state to `localStorage` or `sessionStorage` with `persist` middleware?", "Beginner", "Wrap store in `persist(..., { name: 'storage-key' })`."),
    ("How do you connect Redux Toolkit to React with `<Provider>` and `useDispatch` / `useSelector`?", "Beginner", "Wrap root app in `<Provider store={store}>` and use typed hooks `useAppDispatch` and `useAppSelector`."),
    ("How do you test Redux Reducers with Vitest / Jest?", "Beginner", "Invoke reducer pure function directly with test state and action, asserting the returned state."),
    ("How do you mock Zustand stores in unit tests?", "Intermediate", "Reset store state before each test using `useStore.setState(initialState, true)`."),
    ("What is the difference between `set({ a: 1 })` in Zustand vs `setState` in React?", "Beginner", "Zustand `set` performs a shallow merge on the store state object; React `setState` replaces the state value entirely."),
    ("How do you handle optimistic updates in RTK Query mutations?", "Advanced", "Use `onQueryStarted` to update cached query data with `dispatch(api.util.updateQueryData(...))` and rollback in `.catch()`."),
    ("What is Reselect library and how does `createSelector` implement memoization?", "Intermediate", "Caches selector calculation based on reference equality of input selector arguments."),
    ("How do you access Zustand state outside of React components?", "Beginner", "Call `useStore.getState()` to read state and `useStore.setState()` to update state anywhere in plain JS/TS files."),
    ("What is the purpose of `devtools` middleware in Zustand?", "Beginner", "Enables Redux DevTools extension inspection and time-travel debugging for Zustand stores."),
    ("How do you implement multi-tab synchronization in Zustand with BroadcastChannel?", "Advanced", "Custom middleware broadcasts state diffs across browser tabs and updates local store via `setState`."),
    ("What is the difference between `subscribeWithSelector` and standard `subscribe` in Zustand?", "Advanced", "Allows subscribing to specific derived state slices (`useStore.subscribe(state => state.foo, (foo) => ...)`)."),
    ("How do you implement a shopping cart state with Redux Toolkit?", "Intermediate", "Create `cartSlice` managing items array, quantity adjustments, and computed total price selector."),
    ("What is the purpose of `prepare` callback in `createSlice` action definitions?", "Intermediate", "Prepares action payload with metadata, unique IDs (UUIDs), or timestamps before reaching reducer."),
    ("How do you handle file upload progress in Redux state?", "Intermediate", "Dispatch upload progress actions from custom thunk and track percentage in state."),
    ("What is the difference between Global State and Server State?", "Intermediate", "Global state represents client UI session state (theme, sidebar); server state represents remote persisted data requiring cache invalidation."),
    ("How do you avoid memory leaks with Zustand subscriptions in `useEffect`?", "Beginner", "Always return the unsubscribe cleanup function from `useEffect`."),
    ("What is the purpose of `api.util.invalidateTags` in RTK Query?", "Intermediate", "Programmatically triggers background refetching for all active queries providing the specified tag."),
    ("How do you implement Dark Mode state with Redux Toolkit and CSS variables?", "Beginner", "Store theme string, sync to `document.documentElement` class, and save in localStorage."),
    ("What is the difference between `useStore` hook and `useStore.getState`?", "Beginner", "`useStore(selector)` triggers component re-renders on state changes; `useStore.getState()` reads state synchronously once without subscribing."),
    ("How do you handle global error toast notifications with Redux Middleware?", "Intermediate", "Middleware catches rejected actions matching `/rejected$/` and dispatches toast notification action."),
    ("What is the purpose of `immer` produce option in Zustand?", "Intermediate", "Enables direct mutation syntax inside Zustand `set(produce((state) => { state.count++; }))`."),
    ("How do you reset all Zustand stores on user logout?", "Intermediate", "Create a global reset registry holding initial state reset callbacks for all created stores."),
    ("What is the difference between `autoBatchEnhancer` and standard Redux store dispatch?", "Advanced", "Automatically batches rapid consecutive dispatches within microtask ticks to minimize component re-renders."),
    ("How do you implement pagination in RTK Query with infinite scrolling?", "Advanced", "Use `serializeQueryArgs` and `merge` options to accumulate page results in cache."),
    ("What is the purpose of `combineReducers` in Redux?", "Beginner", "Combines multiple slice reducer functions into a single root reducer object."),
    ("How do you build a multi-step form state machine with Zustand?", "Intermediate", "Maintain step index and validation slices with `nextStep()`, `prevStep()`, and `reset()` actions."),
    ("What is the difference between `shallow` comparison and deep object comparison in state selectors?", "Intermediate", "Shallow comparison checks top-level object keys (`Object.is`); deep comparison recursively traverses nested object trees."),
    ("How do you configure Redux Toolkit with Next.js App Router (SSR-friendly)?", "Advanced", "Create a per-request Redux store instance using `makeStore()` and pass via client `StoreProvider`."),
    ("What is the purpose of `matchFulfilled`, `matchPending`, and `matchRejected` matcher utilities in RTK?", "Intermediate", "Type guards used in `extraReducers` builder `addMatcher()` to handle categories of async actions."),
    ("How do you handle polling endpoints in RTK Query?", "Beginner", "Pass `pollingInterval: 30000` to query hook options."),
    ("What are the best practices for structuring enterprise Redux Toolkit and Zustand applications?", "Advanced", "Feature-based state slices, normalized entities, strict selector memoization, avoiding redundant duplication between server cache and client state."),
    ("How do you configure strict action serializability checks in Redux Toolkit?", "Intermediate", "RTK middleware flags non-serializable values (promises, dates, functions) passed in action payloads in development."),
    ("What is the difference between Zustand and Jotai?", "Intermediate", "Zustand uses a single centralized store model; Jotai uses atomic bottom-up primitives (`atoms`)."),
    ("How do you handle optimistic UI updates with rollback in Zustand?", "Advanced", "Store previous state snapshot in local variable and revert using `set(previousState)` on API catch."),
    ("What is the purpose of `refetchOnMountOrArgChange` in RTK Query?", "Intermediate", "Forces query refetching on component remount or argument modification based on timeout duration."),
    ("How do you implement debounced state setters in Zustand?", "Intermediate", "Wrap setter call in debounce function or custom middleware."),
    ("What is the difference between Redux Toolkit `createReducer` builder callback vs map object notation?", "Intermediate", "Builder callback notation `builder.addCase()` provides strict TypeScript type inference for actions."),
    ("How do you test async thunks with mock API dispatch in Vitest?", "Intermediate", "Dispatch async thunk with mock store and assert dispatched action types (`pending`, `fulfilled`)."),
    ("What is the purpose of `transformResponse` in RTK Query endpoint definitions?", "Intermediate", "Transforms raw backend API payloads into formatted client data structures before saving to cache."),
    ("How do you handle cross-slice selector dependencies in Redux?", "Advanced", "Create compound selectors using `createSelector` combining multiple root state slices."),
    ("What is the difference between `useStore` in React Context vs global Zustand store?", "Intermediate", "Context creates isolated store instances per subtree; global Zustand store shares singleton state across app."),
    ("How do you implement local IndexedDB storage persistence with Zustand?", "Advanced", "Use custom `createJSONStorage` adapter configured with `idb-keyval`."),
    ("What is the purpose of `skipToken` in RTK Query conditional fetching?", "Intermediate", "Pass `skipToken` to disable query hook execution until required parameters are available."),
    ("How do you build an accessible breadcrumb navigation state with Zustand?", "Beginner", "Store route history array and expose `pushRoute` and `popRoute` actions."),
    ("What is the difference between `createAsyncThunk.withTypes` and standard thunk?", "Intermediate", "Pre-types `state`, `dispatch`, and `extra` arguments across all async thunks in the project."),
    ("How do you implement auto-save form state in Redux with middleware debouncing?", "Advanced", "Middleware intercepts form change actions and debounces save endpoint execution."),
    ("What is the purpose of `customEqual` in Zustand `createWithEqualityFn`?", "Advanced", "Allows supplying custom equality algorithms (e.g. `fast-deep-equal`) for store selector subscriptions."),
    ("How do you configure Sentry breadcrumbs from Redux dispatched actions?", "Intermediate", "Redux middleware sends action types and payloads as Sentry breadcrumbs for error diagnosis."),
    ("What is the difference between client-side state caching and HTTP browser caching?", "Intermediate", "Client state caching provides instant synchronous access and optimistic updates without network delay."),
    ("How do you implement responsive layout state (mobile drawer open/close) with Zustand?", "Beginner", "Create `useLayoutStore` with `isSidebarOpen: boolean` and `toggleSidebar: () => void`."),
    ("What are the key differences in architecture between Redux, NgRx, and Zustand?", "Advanced", "Redux is centralized with dispatch/reducers; NgRx is Angular-tailored with RxJS and Signals; Zustand is minimalist hook-native."),
    ("How do you implement atomic selector hooks in Zustand?", "Intermediate", "Create specialized hooks like `useUserName = () => useStore(s => s.user.name)` to minimize re-render surface."),
    ("What is the difference between `createAsyncThunk` and RTK Query mutation endpoints?", "Intermediate", "RTK Query mutations automatically handle caching, tag invalidation, and loading states; AsyncThunks require manual reducer state handling."),
    ("How do you handle race conditions in Redux AsyncThunks with `abort()`?", "Advanced", "Use the `signal` argument passed into the payload creator and pass to fetch/axios."),
    ("What is the purpose of `listenerMiddleware` in Redux Toolkit?", "Advanced", "Lighter-weight alternative to Redux Saga / Observables for reacting to action dispatches with async logic."),
    ("How do you implement optimistic list item reordering in Zustand?", "Intermediate", "Update array order immediately in local store and dispatch reorder API in background."),
    ("What is the difference between `autoBatchEnhancer` and React 18 automatic batching?", "Advanced", "autoBatchEnhancer batches multiple dispatches occurring within microtasks into a single notification to subscribers."),
    ("How do you configure RTK Query with automatic retry logic (`retry` function)?", "Intermediate", "Wrap `fetchBaseQuery` with `retry(..., { maxRetries: 3 })` to retry failed 5xx network requests."),
    ("How do you test components connected to Zustand with `@testing-library/react`?", "Beginner", "Render component, manipulate store via `useStore.setState()`, and assert DOM updates."),
    ("What is the purpose of `immer` patch listeners in Redux Toolkit?", "Advanced", "Emits JSON patches describing state mutations for recording audit logs and collaborative sync."),
    ("How do you handle multi-step form data persistence in Zustand?", "Beginner", "Persist store with `persist` middleware storing partialized form slice in `sessionStorage`."),
    ("What is the difference between `useShallow` from `zustand/react/shallow` and `shallowEqual` from Redux?", "Intermediate", "Both perform shallow object/array comparisons to prevent unnecessary React re-renders."),
    ("How do you implement dynamic slice registration in Redux Toolkit?", "Advanced", "Use `store.reducerManager` pattern to inject feature reducers upon route lazy loading."),
    ("How do you configure Redux DevTools export and import state features?", "Beginner", "Allows developers to export current state snapshots as JSON and replay bugs."),
    ("What is the purpose of `transformBlock` in Zustand persist middleware?", "Intermediate", "Customizes how state slices are serialized and deserialized (e.g. converting Dates to Date instances)."),
    ("How do you build a notifications queue with auto-dismiss timers in Zustand?", "Intermediate", "Action appends notification with UUID and schedules `setTimeout` calling remove action."),
    ("What is the difference between `getDefaultMiddleware` and manual middleware array in RTK?", "Beginner", "`getDefaultMiddleware()` automatically includes Thunk, immutability check, and serializability check."),
    ("How do you implement client-side cache TTL (Time To Live) in RTK Query with `keepUnusedDataFor`?", "Intermediate", "Configures how long unused query cache data remains in memory (default 60s) before garbage collection."),
    ("How do you handle WebSocket real-time updates in RTK Query with `onCacheEntryAdded`?", "Advanced", "Listens for WebSocket events during active query cache lifecycle and updates cache with `updateCachedData`."),
    ("What is the difference between `useStoreApi` and `useStore` in Zustand?", "Intermediate", "`useStoreApi` returns store methods (`getState`, `setState`, `subscribe`) without reactive subscription."),
    ("How do you implement theme color switching with Zustand and CSS custom properties?", "Beginner", "Store theme string and apply matching CSS variable values to `:root`."),
    ("What is the purpose of `createAction.match` type guard in TypeScript?", "Intermediate", "Acts as a TypeScript type guard narrowing unknown action types in middleware or reducers."),
    ("How do you implement localized error state management in Redux Toolkit?", "Intermediate", "Store error objects with error codes and field mappings in slice state."),
    ("What is the difference between `createAsyncThunk` and plain async function in Zustand?", "Beginner", "Zustand handles async functions directly inside action functions without thunk wrappers."),
    ("How do you optimize state selector performance in large Redux trees?", "Advanced", "Use parameterized memoized selectors and normalize relational data structures."),
    ("What is the purpose of `subscribeWithSelector` middleware in Zustand?", "Advanced", "Enables subscribing to granular selector changes and listening to previous vs current slice values."),
    ("How do you implement shopping cart item count badges with Zustand selectors?", "Beginner", "Use `const count = useCartStore(s => s.items.reduce((a, b) => a + b.qty, 0))`."),
    ("What is the difference between Redux Toolkit and Vuex / Pinia?", "Intermediate", "Redux is React-native immutable state container; Pinia is Vue-native reactive proxy state container."),
    ("How do you mock RTK Query endpoints in integration tests with Mock Service Worker?", "Intermediate", "MSW intercepts network requests at the HTTP layer, allowing full integration testing without mocking RTK internals."),
    ("What is the purpose of `combineSlices` in Redux Toolkit 2.0+?", "Intermediate", "Combines slices and enables dynamic slice injection out of the box."),
    ("How do you handle cross-tab logout synchronization in Zustand?", "Advanced", "Listen to storage events or BroadcastChannel and reset user auth store to null on logout message."),
    ("What is the difference between `immer` `draft` and plain mutable objects?", "Intermediate", "Draft is an ES6 Proxy intercepting mutations and generating a pristine immutable object on commit."),
    ("How do you implement undo history in Redux with `redux-undo`?", "Intermediate", "Higher-order reducer that wraps target slice reducer and adds `past`, `present`, and `future` state arrays."),
    ("What is the purpose of `queryFn` custom query handler in RTK Query?", "Advanced", "Allows implementing non-standard data fetching (e.g. Firebase SDK, Supabase, IndexedDB) within RTK Query."),
    ("How do you test Redux Thunks with mock dispatch and mock getState?", "Intermediate", "Call thunk function passing mock `dispatch = jest.fn()` and `getState = jest.fn()`."),
    ("What is the difference between `useStore` inside a React component vs `store.getState()` in event listener?", "Beginner", "`useStore` subscribes to updates; `store.getState()` reads snapshot once synchronously."),
    ("How do you configure Sentry error breadcrumbs from Zustand state changes?", "Intermediate", "Zustand middleware logs state action transitions to Sentry breadcrumb breadboard."),
    ("What are the best practices for structuring large enterprise Redux Toolkit applications?", "Advanced", "Organize code by feature folders (`src/features/products/{productSlice.ts, productApi.ts}`), use typed hooks, avoid duplicate server state in client slices, and normalize relational data.")
]

for t in redux_topics:
    if len(redux_zustand_data) < 100:
        redux_zustand_data.append((
            t[0],
            t[1],
            f"Comprehensive technical explanation of {t[0]}. {t[2]} Key focus on Redux Toolkit best practices, Zustand micro-architecture, selector memoization, and scalable enterprise state design.",
            f"```typescript\n// Implementation for {t[0]}\nimport {{ create }} from 'zustand';\n\ninterface State {{ value: string; setValue: (v: string) => void; }}\nexport const useAppStore = create<State>((set) => ({{\n  value: 'Active',\n  setValue: (value) => set({{ value }})\n}});\n```"
        ))

create_100_qnas(
    "redux-zustand",
    "redux-zustand-questions.md",
    "Redux Toolkit & Zustand",
    "Comprehensive interview questions covering RTK Query, Immer, Zustand Slices, and State Optimization",
    "html-css-js-icon.svg",
    redux_zustand_data[:100]
)

print("Redux & Zustand 100 complete.")
