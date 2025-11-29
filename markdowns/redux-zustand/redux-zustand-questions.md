# Redux + Zustand Interview Questions & Answers

## Table of Contents

- [Q1: What is Redux and what are its core principles?](#q1-what-is-redux-and-what-are-its-core-principles)
- [Q2: How do you handle complex state with multiple reducers?](#q2-how-do-you-handle-complex-state-with-multiple-reducers)
- [Q3: How does Redux Toolkit simplify Redux development?](#q3-how-does-redux-toolkit-simplify-redux-development)
- [Q4: How do you handle async operations with RTK Query?](#q4-how-do-you-handle-async-operations-with-rtk-query)
- [Q5: How do you create custom middleware in Redux?](#q5-how-do-you-create-custom-middleware-in-redux)
- [Q6: What is Zustand and how does it differ from Redux?](#q6-what-is-zustand-and-how-does-it-differ-from-redux)
- [Q7: How do you implement middleware and persistence in Zustand?](#q7-how-do-you-implement-middleware-and-persistence-in-zustand)
- [Q8: How do you implement complex state patterns with Zustand?](#q8-how-do-you-implement-complex-state-patterns-with-zustand)
- [Q9: When should you choose Redux over Zustand and vice versa?](#q9-when-should-you-choose-redux-over-zustand-and-vice-versa)
- [Q10: How do you migrate from Redux to Zustand?](#q10-how-do-you-migrate-from-redux-to-zustand)
- [Q11: How do you optimize performance in Redux and Zustand?](#q11-how-do-you-optimize-performance-in-redux-and-zustand)
- [Q12: What are the best practices for testing Redux and Zustand stores?](#q12-what-are-the-best-practices-for-testing-redux-and-zustand-stores)
- [Q13: What are the key differences between Redux and Zustand, and when should you use each?](#q13-what-are-the-key-differences-between-redux-and-zustand-and-when-should-you-use-each)
- [Q14: How do you implement middleware in Redux and Zustand?](#q14-how-do-you-implement-middleware-in-redux-and-zustand)
- [Q15: How do you handle complex state patterns and normalization in Redux vs Zustand?](#q15-how-do-you-handle-complex-state-patterns-and-normalization-in-redux-vs-zustand)
- [Q16: How do you migrate from Redux to Zustand or vice versa?](#q16-how-do-you-migrate-from-redux-to-zustand-or-vice-versa)
- [Q17: How do you optimize performance in Redux and Zustand applications?](#q17-how-do-you-optimize-performance-in-redux-and-zustand-applications)
- [Q18: How do you implement TypeScript with Redux and Zustand?](#q18-how-do-you-implement-typescript-with-redux-and-zustand)
- [Q19: How do you handle error boundaries and error handling in Redux vs Zustand?](#q19-how-do-you-handle-error-boundaries-and-error-handling-in-redux-vs-zustand)
- [Q20: What are the advanced patterns and real-world use cases for Redux vs Zustand?](#q20-what-are-the-advanced-patterns-and-real-world-use-cases-for-redux-vs-zustand)
- [Q23: What are Redux actions and action creators? How do you structure them?](#q23-what-are-redux-actions-and-action-creators-how-do-you-structure-them)
- [Q24: How do you handle form state management in Redux vs Zustand?](#q24-how-do-you-handle-form-state-management-in-redux-vs-zustand)
- [Q25: What are Redux selectors and how do you create reusable selectors?](#q25-what-are-redux-selectors-and-how-do-you-create-reusable-selectors)
- [Q26: How do you handle authentication state management in Redux vs Zustand?](#q26-how-do-you-handle-authentication-state-management-in-redux-vs-zustand)
- [Q27: How do you use Redux DevTools for debugging and what are its key features?](#q27-how-do-you-use-redux-devtools-for-debugging-and-what-are-its-key-features)
- [Q28: How do you handle loading states and error handling patterns in Redux vs Zustand?](#q28-how-do-you-handle-loading-states-and-error-handling-patterns-in-redux-vs-zustand)
- [Q29: What are the differences between Redux Thunk and Redux Saga? When would you use each?](#q29-what-are-the-differences-between-redux-thunk-and-redux-saga-when-would-you-use-each)
- [Q30: How do you implement optimistic updates in Redux vs Zustand?](#q30-how-do-you-implement-optimistic-updates-in-redux-vs-zustand)
- [Q31: What is Redux Observable and how does it compare to Redux Saga?](#q31-what-is-redux-observable-and-how-does-it-compare-to-redux-saga)
- [Q32: How do you implement advanced Zustand subscriptions and reactive patterns?](#q32-how-do-you-implement-advanced-zustand-subscriptions-and-reactive-patterns)
- [Q33: How do you implement caching strategies and data synchronization in Redux vs Zustand?](#q33-how-do-you-implement-caching-strategies-and-data-synchronization-in-redux-vs-zustand)
- [Q34: How do you handle concurrent updates and race conditions in Redux vs Zustand?](#q34-how-do-you-handle-concurrent-updates-and-race-conditions-in-redux-vs-zustand)
- [Q35: How do you implement internationalization (i18n) and localization patterns in Redux vs Zustand?](#q35-how-do-you-implement-internationalization-i18n-and-localization-patterns-in-redux-vs-zustand)
- [Q56: How do you implement advanced caching and memoization strategies in Redux vs Zustand?](#q56-how-do-you-implement-advanced-caching-and-memoization-strategies-in-redux-vs-zustand)
- [Q15: What is Redux Thunk?](#q15-what-is-redux-thunk)
- [Q16: What is Redux Saga?](#q16-what-is-redux-saga)
- [Q17: Redux Thunk vs Redux Saga.](#q17-redux-thunk-vs-redux-saga)
- [Q18: What is Immer?](#q18-what-is-immer)
- [Q19: What is `createSlice` in Redux Toolkit?](#q19-what-is-createslice-in-redux-toolkit)
- [Q20: What is the `connect` function?](#q20-what-is-the-connect-function)
- [Q21: `useSelector` vs `useDispatch`.](#q21-useselector-vs-usedispatch)
- [Q22: What is the Flux Architecture?](#q22-what-is-the-flux-architecture)
- [Q23: Explain "Single Source of Truth".](#q23-explain-single-source-of-truth)
- [Q24: What are "Selectors"?](#q24-what-are-selectors)
- [Q25: Zustand: `create` store.](#q25-zustand-create-store)
- [Q26: Zustand vs Redux: Boilerplate.](#q26-zustand-vs-redux-boilerplate)
- [Q27: How to handle async actions in Zustand?](#q27-how-to-handle-async-actions-in-zustand)
- [Q28: How to access Zustand store outside React components?](#q28-how-to-access-zustand-store-outside-react-components)
- [Q29: What is "Transient Updates" in Zustand?](#q29-what-is-transient-updates-in-zustand)
- [Q30: How to persist state in Zustand?](#q30-how-to-persist-state-in-zustand)
- [Q31: What is Redux DevTools Extension?](#q31-what-is-redux-devtools-extension)
- [Q32: MobX vs Redux.](#q32-mobx-vs-redux)
- [Q33: What is RTK Query?](#q33-what-is-rtk-query)
- [Q34: Explain `reselect` library.](#q34-explain-reselect-library)
- [Q35: What is the "Provider" component in Redux?](#q35-what-is-the-provider-component-in-redux)
- [Q36: How to reset state in Redux?](#q36-how-to-reset-state-in-redux)
- [Q37: Multiple Stores in Redux?](#q37-multiple-stores-in-redux)
- [Q38: Zustand: `set` function patterns.](#q38-zustand-set-function-patterns)
- [Q39: How to test Redux reducers?](#q39-how-to-test-redux-reducers)
- [Q40: How to test Redux async thunks?](#q40-how-to-test-redux-async-thunks)
- [Q41: Recoil vs Redux.](#q41-recoil-vs-redux)
- [Q42: Jotai vs Zustand.](#q42-jotai-vs-zustand)
- [Q43: What is "Optimistic UI"?](#q43-what-is-optimistic-ui)
- [Q44: How to structure Redux files?](#q44-how-to-structure-redux-files)
- [Q45: Why state immutability is important?](#q45-why-state-immutability-is-important)
- [Q46: `shallow` comparison in Zustand.](#q46-shallow-comparison-in-zustand)
- [Q47: Redux Middleware signature.](#q47-redux-middleware-signature)
- [Q48: How to handle side effects in Zustand?](#q48-how-to-handle-side-effects-in-zustand)
- [Q49: What is `combineReducers`?](#q49-what-is-combinereducers)
- [Q50: Context + useReducer vs Redux.](#q50-context--usereducer-vs-redux)
- [Q51: How to type Redux state (TypeScript)?](#q51-how-to-type-redux-state-typescript)
- [Q52: How to type Zustand store (TypeScript)?](#q52-how-to-type-zustand-store-typescript)
- [Q53: Dynamic Reducers in Redux?](#q53-dynamic-reducers-in-redux)
- [Q54: What is the "Container/Presentational" pattern?](#q54-what-is-the-containerpresentational-pattern)
- [Q55: Explain `bindActionCreators`.](#q55-explain-bindactioncreators)
- [Q56: Redux Toolkit `createAsyncThunk`.](#q56-redux-toolkit-createasyncthunk)
- [Q57: How `createEntityAdapter` helps?](#q57-how-createentityadapter-helps)
- [Q58: What is "Normalization" in State?](#q58-what-is-normalization-in-state)
- [Q59: Zustand vs Context Performance.](#q59-zustand-vs-context-performance)
- [Q60: Can you use Redux and Zustand together?](#q60-can-you-use-redux-and-zustand-together)
- [Q61: What is `store.subscribe`?](#q61-what-is-storesubscribe)
- [Q62: How to handle WebSocket data in Redux?](#q62-how-to-handle-websocket-data-in-redux)
- [Q63: What is "Action Creator"?](#q63-what-is-action-creator)
- [Q64: Pure Functions in Redux.](#q64-pure-functions-in-redux)
- [Q65: Explain "Time Travel Debugging".](#q65-explain-time-travel-debugging)
- [Q66: Why use `const` for Action Types?](#q66-why-use-const-for-action-types)
- [Q67: Zustand `subscribe` with selector.](#q67-zustand-subscribe-with-selector)
- [Q68: How to secure Redux state?](#q68-how-to-secure-redux-state)
- [Q69: Server-Side Rendering (SSR) with Redux.](#q69-server-side-rendering-ssr-with-redux)
- [Q70: Atomic State Management.](#q70-atomic-state-management)
- [Q71: What is "Prop Drilling"?](#q71-what-is-prop-drilling)
- [Q72: How to clear Redux cache?](#q72-how-to-clear-redux-cache)
- [Q73: Explain `redux-persist`.](#q73-explain-redux-persist)
- [Q74: `useStore` vs `useSelector` (Zustand vs Redux).](#q74-usestore-vs-useselector-zustand-vs-redux)
- [Q75: Why is Redux synchronous?](#q75-why-is-redux-synchronous)
- [Q76: What is "derived state"?](#q76-what-is-derived-state)
- [Q77: How to structure large Redux apps?](#q77-how-to-structure-large-redux-apps)
- [Q78: Zustand middlewares list.](#q78-zustand-middlewares-list)
- [Q79: What is `extraReducers`?](#q79-what-is-extrareducers)
- [Q80: Benefits of RTK over vanilla Redux.](#q80-benefits-of-rtk-over-vanilla-redux)
- [Q81: Zustand: How to reset store?](#q81-zustand-how-to-reset-store)
- [Q82: How to use Immer with Zustand?](#q82-how-to-use-immer-with-zustand)
- [Q83: Can Redux work without React?](#q83-can-redux-work-without-react)
- [Q84: What is "Enhancer" in Redux?](#q84-what-is-enhancer-in-redux)
- [Q85: How to handle error handling in Redux?](#q85-how-to-handle-error-handling-in-redux)
- [Q86: Zustand vs Context API for Global State.](#q86-zustand-vs-context-api-for-global-state)
- [Q87: What is a "Draft" state (Immer)?](#q87-what-is-a-draft-state-immer)
- [Q88: How to handle form state in Redux?](#q88-how-to-handle-form-state-in-redux)
- [Q89: Why Redux boilerplate was reduced?](#q89-why-redux-boilerplate-was-reduced)
- [Q90: Zustand: Multiple stores vs Single store.](#q90-zustand-multiple-stores-vs-single-store)
- [Q91: What is "Declarative" vs "Imperative" in State?](#q91-what-is-declarative-vs-imperative-in-state)
- [Q92: How to mock Redux for integration tests?](#q92-how-to-mock-redux-for-integration-tests)
- [Q93: Explain "Hydration" error.](#q93-explain-hydration-error)
- [Q94: Does Zustand use React Context?](#q94-does-zustand-use-react-context)
- [Q95: When to use `useLayoutEffect` with state?](#q95-when-to-use-uselayouteffect-with-state)
- [Q96: How to handle heavy computation in Redux?](#q96-how-to-handle-heavy-computation-in-redux)
- [Q97: Redux `compose`.](#q97-redux-compose)
- [Q98: State Management trends 2024.](#q98-state-management-trends-2024)
- [Q99: What are "Signals"?](#q99-what-are-signals)
- [Q100: Best library for simple global state?](#q100-best-library-for-simple-global-state)

---

### Q1: What is Redux and what are its core principles?

**Answer:**
Redux is a predictable state container for JavaScript applications, following three core principles:

**Core Principles:**

1. **Single Source of Truth**: The entire application state is stored in a single store
2. **State is Read-Only**: State can only be changed by dispatching actions
3. **Changes are Made with Pure Functions**: Reducers are pure functions that specify how state changes

```javascript
// Basic Redux setup
import { createStore } from "redux";

// Action Types
const INCREMENT = "INCREMENT";
const DECREMENT = "DECREMENT";
const SET_COUNT = "SET_COUNT";

// Action Creators
export const increment = () => ({ type: INCREMENT });
export const decrement = () => ({ type: DECREMENT });
export const setCount = (count) => ({ type: SET_COUNT, payload: count });

// Initial State
const initialState = {
  count: 0,
  history: [],
  lastUpdated: null,
};

// Reducer (Pure Function)
function counterReducer(state = initialState, action) {
  switch (action.type) {
    case INCREMENT:
      return {
        ...state,
        count: state.count + 1,
        history: [...state.history, "increment"],
        lastUpdated: new Date().toISOString(),
      };
    case DECREMENT:
      return {
        ...state,
        count: state.count - 1,
        history: [...state.history, "decrement"],
        lastUpdated: new Date().toISOString(),
      };
    case SET_COUNT:
      return {
        ...state,
        count: action.payload,
        history: [...state.history, `set to ${action.payload}`],
        lastUpdated: new Date().toISOString(),
      };
    default:
      return state;
  }
}

// Store
const store = createStore(counterReducer);

// Usage
store.dispatch(increment()); // { count: 1, history: ['increment'], lastUpdated: '...' }
store.dispatch(setCount(10)); // { count: 10, history: ['increment', 'set to 10'], lastUpdated: '...' }
console.log(store.getState());
```

### Q2: How do you handle complex state with multiple reducers?

**Answer:**
Use `combineReducers` to split state management into smaller, focused reducers.

```javascript
import { combineReducers, createStore } from "redux";

// User Reducer
const userInitialState = {
  currentUser: null,
  isAuthenticated: false,
  profile: null,
  preferences: {
    theme: "light",
    language: "en",
  },
};

function userReducer(state = userInitialState, action) {
  switch (action.type) {
    case "USER_LOGIN_SUCCESS":
      return {
        ...state,
        currentUser: action.payload.user,
        isAuthenticated: true,
        profile: action.payload.profile,
      };
    case "USER_LOGOUT":
      return {
        ...userInitialState,
      };
    case "UPDATE_PREFERENCES":
      return {
        ...state,
        preferences: {
          ...state.preferences,
          ...action.payload,
        },
      };
    default:
      return state;
  }
}

// Posts Reducer
const postsInitialState = {
  items: [],
  loading: false,
  error: null,
  pagination: {
    page: 1,
    limit: 10,
    total: 0,
  },
};

function postsReducer(state = postsInitialState, action) {
  switch (action.type) {
    case "FETCH_POSTS_START":
      return {
        ...state,
        loading: true,
        error: null,
      };
    case "FETCH_POSTS_SUCCESS":
      return {
        ...state,
        loading: false,
        items: action.payload.posts,
        pagination: {
          ...state.pagination,
          ...action.payload.pagination,
        },
      };
    case "FETCH_POSTS_ERROR":
      return {
        ...state,
        loading: false,
        error: action.payload.error,
      };
    case "ADD_POST":
      return {
        ...state,
        items: [action.payload, ...state.items],
      };
    case "UPDATE_POST":
      return {
        ...state,
        items: state.items.map((post) =>
          post.id === action.payload.id
            ? { ...post, ...action.payload.updates }
            : post
        ),
      };
    case "DELETE_POST":
      return {
        ...state,
        items: state.items.filter((post) => post.id !== action.payload.id),
      };
    default:
      return state;
  }
}

// UI Reducer
const uiInitialState = {
  sidebarOpen: false,
  modals: {
    createPost: false,
    editProfile: false,
    confirmDelete: false,
  },
  notifications: [],
  theme: "light",
};

function uiReducer(state = uiInitialState, action) {
  switch (action.type) {
    case "TOGGLE_SIDEBAR":
      return {
        ...state,
        sidebarOpen: !state.sidebarOpen,
      };
    case "OPEN_MODAL":
      return {
        ...state,
        modals: {
          ...state.modals,
          [action.payload.modalName]: true,
        },
      };
    case "CLOSE_MODAL":
      return {
        ...state,
        modals: {
          ...state.modals,
          [action.payload.modalName]: false,
        },
      };
    case "ADD_NOTIFICATION":
      return {
        ...state,
        notifications: [
          ...state.notifications,
          {
            id: Date.now(),
            ...action.payload,
          },
        ],
      };
    case "REMOVE_NOTIFICATION":
      return {
        ...state,
        notifications: state.notifications.filter(
          (notification) => notification.id !== action.payload.id
        ),
      };
    default:
      return state;
  }
}

// Combine Reducers
const rootReducer = combineReducers({
  user: userReducer,
  posts: postsReducer,
  ui: uiReducer,
});

// Store
const store = createStore(rootReducer);

// Selectors
export const selectUser = (state) => state.user.currentUser;
export const selectIsAuthenticated = (state) => state.user.isAuthenticated;
export const selectPosts = (state) => state.posts.items;
export const selectPostsLoading = (state) => state.posts.loading;
export const selectSidebarOpen = (state) => state.ui.sidebarOpen;
export const selectNotifications = (state) => state.ui.notifications;

// Action Creators
export const loginSuccess = (user, profile) => ({
  type: "USER_LOGIN_SUCCESS",
  payload: { user, profile },
});

export const logout = () => ({ type: "USER_LOGOUT" });

export const fetchPostsStart = () => ({ type: "FETCH_POSTS_START" });
export const fetchPostsSuccess = (posts, pagination) => ({
  type: "FETCH_POSTS_SUCCESS",
  payload: { posts, pagination },
});

export const addNotification = (message, type = "info") => ({
  type: "ADD_NOTIFICATION",
  payload: { message, type, timestamp: new Date().toISOString() },
});
```

---

### Q3: How does Redux Toolkit simplify Redux development?

**Answer:**
Redux Toolkit (RTK) provides utilities to simplify common Redux patterns and reduce boilerplate code.

```javascript
import {
  createSlice,
  configureStore,
  createAsyncThunk,
} from "@reduxjs/toolkit";

// Async Thunk for API calls
export const fetchPosts = createAsyncThunk(
  "posts/fetchPosts",
  async ({ page = 1, limit = 10 }, { rejectWithValue }) => {
    try {
      const response = await fetch(`/api/posts?page=${page}&limit=${limit}`);
      if (!response.ok) {
        throw new Error("Failed to fetch posts");
      }
      const data = await response.json();
      return data;
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);

export const createPost = createAsyncThunk(
  "posts/createPost",
  async (postData, { rejectWithValue }) => {
    try {
      const response = await fetch("/api/posts", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(postData),
      });
      if (!response.ok) {
        throw new Error("Failed to create post");
      }
      return await response.json();
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);

// Posts Slice
const postsSlice = createSlice({
  name: "posts",
  initialState: {
    items: [],
    loading: false,
    error: null,
    pagination: {
      page: 1,
      limit: 10,
      total: 0,
      totalPages: 0,
    },
    filters: {
      category: "all",
      search: "",
      sortBy: "createdAt",
      sortOrder: "desc",
    },
  },
  reducers: {
    // Synchronous actions
    updatePost: (state, action) => {
      const { id, updates } = action.payload;
      const existingPost = state.items.find((post) => post.id === id);
      if (existingPost) {
        Object.assign(existingPost, updates);
      }
    },
    deletePost: (state, action) => {
      state.items = state.items.filter((post) => post.id !== action.payload);
    },
    setFilters: (state, action) => {
      state.filters = { ...state.filters, ...action.payload };
    },
    clearError: (state) => {
      state.error = null;
    },
    resetPosts: (state) => {
      state.items = [];
      state.pagination = {
        page: 1,
        limit: 10,
        total: 0,
        totalPages: 0,
      };
    },
  },
  extraReducers: (builder) => {
    builder
      // Fetch Posts
      .addCase(fetchPosts.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchPosts.fulfilled, (state, action) => {
        state.loading = false;
        state.items = action.payload.posts;
        state.pagination = action.payload.pagination;
      })
      .addCase(fetchPosts.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      })
      // Create Post
      .addCase(createPost.pending, (state) => {
        state.loading = true;
      })
      .addCase(createPost.fulfilled, (state, action) => {
        state.loading = false;
        state.items.unshift(action.payload);
        state.pagination.total += 1;
      })
      .addCase(createPost.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      });
  },
});

// User Slice with authentication
const userSlice = createSlice({
  name: "user",
  initialState: {
    currentUser: null,
    isAuthenticated: false,
    profile: null,
    preferences: {
      theme: "light",
      language: "en",
      notifications: true,
    },
    loading: false,
    error: null,
  },
  reducers: {
    loginStart: (state) => {
      state.loading = true;
      state.error = null;
    },
    loginSuccess: (state, action) => {
      state.loading = false;
      state.currentUser = action.payload.user;
      state.profile = action.payload.profile;
      state.isAuthenticated = true;
    },
    loginFailure: (state, action) => {
      state.loading = false;
      state.error = action.payload;
      state.isAuthenticated = false;
    },
    logout: (state) => {
      state.currentUser = null;
      state.profile = null;
      state.isAuthenticated = false;
      state.preferences = {
        theme: "light",
        language: "en",
        notifications: true,
      };
    },
    updatePreferences: (state, action) => {
      state.preferences = { ...state.preferences, ...action.payload };
    },
    updateProfile: (state, action) => {
      if (state.profile) {
        state.profile = { ...state.profile, ...action.payload };
      }
    },
  },
});

// Configure Store
const store = configureStore({
  reducer: {
    posts: postsSlice.reducer,
    user: userSlice.reducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: {
        ignoredActions: ["persist/PERSIST", "persist/REHYDRATE"],
      },
    }),
  devTools: process.env.NODE_ENV !== "production",
});

// Export actions
export const { updatePost, deletePost, setFilters, clearError, resetPosts } =
  postsSlice.actions;
export const {
  loginStart,
  loginSuccess,
  loginFailure,
  logout,
  updatePreferences,
  updateProfile,
} = userSlice.actions;

// Selectors
export const selectPosts = (state) => state.posts.items;
export const selectPostsLoading = (state) => state.posts.loading;
export const selectPostsError = (state) => state.posts.error;
export const selectPostsPagination = (state) => state.posts.pagination;
export const selectPostsFilters = (state) => state.posts.filters;

export const selectCurrentUser = (state) => state.user.currentUser;
export const selectIsAuthenticated = (state) => state.user.isAuthenticated;
export const selectUserPreferences = (state) => state.user.preferences;

// Memoized selectors
import { createSelector } from "@reduxjs/toolkit";

export const selectFilteredPosts = createSelector(
  [selectPosts, selectPostsFilters],
  (posts, filters) => {
    let filtered = posts;

    if (filters.category !== "all") {
      filtered = filtered.filter((post) => post.category === filters.category);
    }

    if (filters.search) {
      const searchLower = filters.search.toLowerCase();
      filtered = filtered.filter(
        (post) =>
          post.title.toLowerCase().includes(searchLower) ||
          post.content.toLowerCase().includes(searchLower)
      );
    }

    // Sort posts
    filtered.sort((a, b) => {
      const aValue = a[filters.sortBy];
      const bValue = b[filters.sortBy];

      if (filters.sortOrder === "asc") {
        return aValue > bValue ? 1 : -1;
      } else {
        return aValue < bValue ? 1 : -1;
      }
    });

    return filtered;
  }
);

export default store;
```

### Q4: How do you handle async operations with RTK Query?

**Answer:**
RTK Query provides powerful data fetching and caching capabilities built on top of Redux Toolkit.

```javascript
import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

// Define API slice
export const apiSlice = createApi({
  reducerPath: "api",
  baseQuery: fetchBaseQuery({
    baseUrl: "/api",
    prepareHeaders: (headers, { getState }) => {
      const token = getState().user.token;
      if (token) {
        headers.set("authorization", `Bearer ${token}`);
      }
      return headers;
    },
  }),
  tagTypes: ["Post", "User", "Comment"],
  endpoints: (builder) => ({
    // Posts endpoints
    getPosts: builder.query({
      query: ({ page = 1, limit = 10, category, search } = {}) => {
        const params = new URLSearchParams({
          page: page.toString(),
          limit: limit.toString(),
          ...(category && { category }),
          ...(search && { search }),
        });
        return `posts?${params}`;
      },
      providesTags: (result) =>
        result
          ? [
              ...result.posts.map(({ id }) => ({ type: "Post", id })),
              { type: "Post", id: "LIST" },
            ]
          : [{ type: "Post", id: "LIST" }],
    }),

    getPost: builder.query({
      query: (id) => `posts/${id}`,
      providesTags: (result, error, id) => [{ type: "Post", id }],
    }),

    createPost: builder.mutation({
      query: (newPost) => ({
        url: "posts",
        method: "POST",
        body: newPost,
      }),
      invalidatesTags: [{ type: "Post", id: "LIST" }],
    }),

    updatePost: builder.mutation({
      query: ({ id, ...patch }) => ({
        url: `posts/${id}`,
        method: "PATCH",
        body: patch,
      }),
      invalidatesTags: (result, error, { id }) => [{ type: "Post", id }],
    }),

    deletePost: builder.mutation({
      query: (id) => ({
        url: `posts/${id}`,
        method: "DELETE",
      }),
      invalidatesTags: (result, error, id) => [
        { type: "Post", id },
        { type: "Post", id: "LIST" },
      ],
    }),

    // Comments endpoints
    getComments: builder.query({
      query: (postId) => `posts/${postId}/comments`,
      providesTags: (result, error, postId) =>
        result
          ? [
              ...result.map(({ id }) => ({ type: "Comment", id })),
              { type: "Comment", id: `LIST-${postId}` },
            ]
          : [{ type: "Comment", id: `LIST-${postId}` }],
    }),

    addComment: builder.mutation({
      query: ({ postId, content }) => ({
        url: `posts/${postId}/comments`,
        method: "POST",
        body: { content },
      }),
      invalidatesTags: (result, error, { postId }) => [
        { type: "Comment", id: `LIST-${postId}` },
      ],
    }),

    // User endpoints
    getProfile: builder.query({
      query: () => "user/profile",
      providesTags: ["User"],
    }),

    updateProfile: builder.mutation({
      query: (updates) => ({
        url: "user/profile",
        method: "PATCH",
        body: updates,
      }),
      invalidatesTags: ["User"],
    }),
  }),
});

// Export hooks for usage in components
export const {
  useGetPostsQuery,
  useGetPostQuery,
  useCreatePostMutation,
  useUpdatePostMutation,
  useDeletePostMutation,
  useGetCommentsQuery,
  useAddCommentMutation,
  useGetProfileQuery,
  useUpdateProfileMutation,
} = apiSlice;

// Usage in components
import React, { useState } from "react";
import {
  useGetPostsQuery,
  useCreatePostMutation,
  useDeletePostMutation,
} from "./apiSlice";

function PostsList() {
  const [page, setPage] = useState(1);
  const [filters, setFilters] = useState({ category: "", search: "" });

  const {
    data: postsData,
    error,
    isLoading,
    isFetching,
    refetch,
  } = useGetPostsQuery({ page, ...filters });

  const [createPost, { isLoading: isCreating }] = useCreatePostMutation();
  const [deletePost] = useDeletePostMutation();

  const handleCreatePost = async (postData) => {
    try {
      await createPost(postData).unwrap();
      // Post created successfully
    } catch (error) {
      console.error("Failed to create post:", error);
    }
  };

  const handleDeletePost = async (id) => {
    if (window.confirm("Are you sure?")) {
      try {
        await deletePost(id).unwrap();
        // Post deleted successfully
      } catch (error) {
        console.error("Failed to delete post:", error);
      }
    }
  };

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return (
    <div>
      <div className="mb-4">
        <input
          type="text"
          placeholder="Search posts..."
          value={filters.search}
          onChange={(e) => setFilters({ ...filters, search: e.target.value })}
          className="border p-2 mr-2"
        />
        <select
          value={filters.category}
          onChange={(e) => setFilters({ ...filters, category: e.target.value })}
          className="border p-2"
        >
          <option value="">All Categories</option>
          <option value="tech">Technology</option>
          <option value="lifestyle">Lifestyle</option>
        </select>
        <button
          onClick={refetch}
          className="ml-2 px-4 py-2 bg-blue-500 text-white"
        >
          Refresh
        </button>
      </div>

      {isFetching && <div>Updating...</div>}

      <div className="grid gap-4">
        {postsData?.posts.map((post) => (
          <div key={post.id} className="border p-4 rounded">
            <h3 className="text-xl font-bold">{post.title}</h3>
            <p className="text-gray-600">{post.excerpt}</p>
            <div className="mt-2">
              <button
                onClick={() => handleDeletePost(post.id)}
                className="px-3 py-1 bg-red-500 text-white rounded"
              >
                Delete
              </button>
            </div>
          </div>
        ))}
      </div>

      {/* Pagination */}
      <div className="mt-4 flex justify-center space-x-2">
        <button
          onClick={() => setPage(page - 1)}
          disabled={page === 1}
          className="px-3 py-1 border disabled:opacity-50"
        >
          Previous
        </button>
        <span className="px-3 py-1">Page {page}</span>
        <button
          onClick={() => setPage(page + 1)}
          disabled={!postsData?.pagination.hasNext}
          className="px-3 py-1 border disabled:opacity-50"
        >
          Next
        </button>
      </div>
    </div>
  );
}

export default PostsList;
```

---

### Q5: How do you create custom middleware in Redux?

**Answer:**
Middleware provides a way to extend Redux with custom functionality for logging, crash reporting, async actions, etc.

```javascript
// Custom logging middleware
const loggerMiddleware = (store) => (next) => (action) => {
  console.group(`Action: ${action.type}`);
  console.log("Previous State:", store.getState());
  console.log("Action:", action);

  const result = next(action);

  console.log("Next State:", store.getState());
  console.groupEnd();

  return result;
};

// Performance monitoring middleware
const performanceMiddleware = (store) => (next) => (action) => {
  const start = performance.now();

  const result = next(action);

  const end = performance.now();
  const duration = end - start;

  if (duration > 10) {
    // Log slow actions
    console.warn(
      `Slow action detected: ${action.type} took ${duration.toFixed(2)}ms`
    );
  }

  return result;
};

// Error handling middleware
const errorMiddleware = (store) => (next) => (action) => {
  try {
    return next(action);
  } catch (error) {
    console.error("Redux Error:", error);

    // Send error to monitoring service
    if (typeof window !== "undefined" && window.Sentry) {
      window.Sentry.captureException(error, {
        extra: {
          action,
          state: store.getState(),
        },
      });
    }

    // Dispatch error action
    store.dispatch({
      type: "GLOBAL_ERROR",
      payload: {
        message: error.message,
        stack: error.stack,
        action,
      },
    });

    throw error;
  }
};

// API middleware for handling async actions
const apiMiddleware = (store) => (next) => (action) => {
  // Pass through non-API actions
  if (!action.meta || !action.meta.api) {
    return next(action);
  }

  const { endpoint, method = "GET", body, headers = {} } = action.meta.api;
  const { type } = action;

  // Dispatch loading action
  store.dispatch({ type: `${type}_PENDING` });

  // Make API call
  return fetch(endpoint, {
    method,
    headers: {
      "Content-Type": "application/json",
      ...headers,
    },
    ...(body && { body: JSON.stringify(body) }),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`);
      }
      return response.json();
    })
    .then((data) => {
      // Dispatch success action
      store.dispatch({
        type: `${type}_FULFILLED`,
        payload: data,
      });
      return data;
    })
    .catch((error) => {
      // Dispatch error action
      store.dispatch({
        type: `${type}_REJECTED`,
        payload: error.message,
        error: true,
      });
      throw error;
    });
};

// Debounce middleware for search actions
const debounceMiddleware = (store) => {
  const debounceTimers = new Map();

  return (next) => (action) => {
    if (action.meta && action.meta.debounce) {
      const { delay = 300, key = action.type } = action.meta.debounce;

      // Clear existing timer
      if (debounceTimers.has(key)) {
        clearTimeout(debounceTimers.get(key));
      }

      // Set new timer
      const timer = setTimeout(() => {
        debounceTimers.delete(key);
        next(action);
      }, delay);

      debounceTimers.set(key, timer);

      return;
    }

    return next(action);
  };
};

// Local storage persistence middleware
const persistenceMiddleware = (store) => (next) => (action) => {
  const result = next(action);

  // Persist specific state slices
  const stateToPersist = {
    user: store.getState().user,
    preferences: store.getState().preferences,
  };

  try {
    localStorage.setItem("reduxState", JSON.stringify(stateToPersist));
  } catch (error) {
    console.warn("Failed to persist state:", error);
  }

  return result;
};

// Configure store with middleware
import { configureStore } from "@reduxjs/toolkit";

const store = configureStore({
  reducer: rootReducer,
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: {
        ignoredActions: ["persist/PERSIST"],
      },
    }).concat(
      loggerMiddleware,
      performanceMiddleware,
      errorMiddleware,
      apiMiddleware,
      debounceMiddleware,
      persistenceMiddleware
    ),
});

// Usage examples

// API action
const fetchUsers = () => ({
  type: "FETCH_USERS",
  meta: {
    api: {
      endpoint: "/api/users",
      method: "GET",
    },
  },
});

// Debounced search action
const searchPosts = (query) => ({
  type: "SEARCH_POSTS",
  payload: query,
  meta: {
    debounce: {
      delay: 500,
      key: "search",
    },
  },
});

// Usage in component
function SearchComponent() {
  const dispatch = useDispatch();

  const handleSearch = (query) => {
    dispatch(searchPosts(query));
  };

  const handleFetchUsers = () => {
    dispatch(fetchUsers());
  };

  return (
    <div>
      <input
        type="text"
        onChange={(e) => handleSearch(e.target.value)}
        placeholder="Search posts..."
      />
      <button onClick={handleFetchUsers}>Fetch Users</button>
    </div>
  );
}
```

---

### Q6: What is Zustand and how does it differ from Redux?

**Answer:**
Zustand is a lightweight state management library that provides a simpler alternative to Redux with less boilerplate and better TypeScript support.

**Key Differences:**

- **Less Boilerplate**: No actions, reducers, or providers needed
- **Simpler API**: Direct state mutations allowed
- **Better TypeScript**: Built-in TypeScript support
- **Smaller Bundle**: Much smaller than Redux
- **No Context**: Doesn't use React Context, avoiding re-render issues

```javascript
import { create } from "zustand";
import { devtools, persist, subscribeWithSelector } from "zustand/middleware";
import { immer } from "zustand/middleware/immer";

// Basic Zustand store
const useCounterStore = create((set, get) => ({
  count: 0,
  increment: () => set((state) => ({ count: state.count + 1 })),
  decrement: () => set((state) => ({ count: state.count - 1 })),
  reset: () => set({ count: 0 }),
  incrementBy: (value) => set((state) => ({ count: state.count + value })),
  // Computed values
  get doubled() {
    return get().count * 2;
  },
  get isEven() {
    return get().count % 2 === 0;
  },
}));

// Complex store with multiple slices
const useAppStore = create(
  devtools(
    persist(
      subscribeWithSelector(
        immer((set, get) => ({
          // User slice
          user: {
            currentUser: null,
            isAuthenticated: false,
            preferences: {
              theme: "light",
              language: "en",
            },
          },

          // Posts slice
          posts: {
            items: [],
            loading: false,
            error: null,
            filters: {
              category: "all",
              search: "",
            },
          },

          // UI slice
          ui: {
            sidebarOpen: false,
            modals: {
              createPost: false,
              editProfile: false,
            },
            notifications: [],
          },

          // User actions
          login: (user) =>
            set((state) => {
              state.user.currentUser = user;
              state.user.isAuthenticated = true;
            }),

          logout: () =>
            set((state) => {
              state.user.currentUser = null;
              state.user.isAuthenticated = false;
              state.user.preferences = {
                theme: "light",
                language: "en",
              };
            }),

          updatePreferences: (preferences) =>
            set((state) => {
              Object.assign(state.user.preferences, preferences);
            }),

          // Posts actions
          setPosts: (posts) =>
            set((state) => {
              state.posts.items = posts;
              state.posts.loading = false;
              state.posts.error = null;
            }),

          addPost: (post) =>
            set((state) => {
              state.posts.items.unshift(post);
            }),

          updatePost: (id, updates) =>
            set((state) => {
              const post = state.posts.items.find((p) => p.id === id);
              if (post) {
                Object.assign(post, updates);
              }
            }),

          deletePost: (id) =>
            set((state) => {
              state.posts.items = state.posts.items.filter((p) => p.id !== id);
            }),

          setPostsLoading: (loading) =>
            set((state) => {
              state.posts.loading = loading;
            }),

          setPostsError: (error) =>
            set((state) => {
              state.posts.error = error;
              state.posts.loading = false;
            }),

          setPostsFilters: (filters) =>
            set((state) => {
              Object.assign(state.posts.filters, filters);
            }),

          // Async actions
          fetchPosts: async () => {
            const { setPostsLoading, setPosts, setPostsError } = get();

            setPostsLoading(true);
            try {
              const response = await fetch("/api/posts");
              if (!response.ok) throw new Error("Failed to fetch posts");
              const posts = await response.json();
              setPosts(posts);
            } catch (error) {
              setPostsError(error.message);
            }
          },

          createPost: async (postData) => {
            const { addPost, setPostsError } = get();

            try {
              const response = await fetch("/api/posts", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(postData),
              });
              if (!response.ok) throw new Error("Failed to create post");
              const newPost = await response.json();
              addPost(newPost);
              return newPost;
            } catch (error) {
              setPostsError(error.message);
              throw error;
            }
          },

          // UI actions
          toggleSidebar: () =>
            set((state) => {
              state.ui.sidebarOpen = !state.ui.sidebarOpen;
            }),

          openModal: (modalName) =>
            set((state) => {
              state.ui.modals[modalName] = true;
            }),

          closeModal: (modalName) =>
            set((state) => {
              state.ui.modals[modalName] = false;
            }),

          addNotification: (notification) =>
            set((state) => {
              state.ui.notifications.push({
                id: Date.now(),
                timestamp: new Date().toISOString(),
                ...notification,
              });
            }),

          removeNotification: (id) =>
            set((state) => {
              state.ui.notifications = state.ui.notifications.filter(
                (n) => n.id !== id
              );
            }),

          // Computed selectors
          get filteredPosts() {
            const { posts } = get();
            let filtered = posts.items;

            if (posts.filters.category !== "all") {
              filtered = filtered.filter(
                (post) => post.category === posts.filters.category
              );
            }

            if (posts.filters.search) {
              const search = posts.filters.search.toLowerCase();
              filtered = filtered.filter(
                (post) =>
                  post.title.toLowerCase().includes(search) ||
                  post.content.toLowerCase().includes(search)
              );
            }

            return filtered;
          },
        }))
      ),
      {
        name: "app-storage",
        partialize: (state) => ({
          user: {
            preferences: state.user.preferences,
          },
        }),
      }
    ),
    {
      name: "app-store",
    }
  )
);

// Usage in components
function Counter() {
  const { count, increment, decrement, reset, doubled, isEven } =
    useCounterStore();

  return (
    <div>
      <p>Count: {count}</p>
      <p>Doubled: {doubled}</p>
      <p>Is Even: {isEven ? "Yes" : "No"}</p>
      <button onClick={increment}>+</button>
      <button onClick={decrement}>-</button>
      <button onClick={reset}>Reset</button>
    </div>
  );
}

function PostsList() {
  const { posts, filteredPosts, fetchPosts, deletePost, setPostsFilters } =
    useAppStore();

  useEffect(() => {
    fetchPosts();
  }, []);

  return (
    <div>
      <input
        type="text"
        placeholder="Search posts..."
        onChange={(e) => setPostsFilters({ search: e.target.value })}
      />

      {posts.loading && <div>Loading...</div>}
      {posts.error && <div>Error: {posts.error}</div>}

      <div>
        {filteredPosts.map((post) => (
          <div key={post.id}>
            <h3>{post.title}</h3>
            <p>{post.content}</p>
            <button onClick={() => deletePost(post.id)}>Delete</button>
          </div>
        ))}
      </div>
    </div>
  );
}

// Selective subscriptions to avoid unnecessary re-renders
function UserProfile() {
  const user = useAppStore((state) => state.user.currentUser);
  const updatePreferences = useAppStore((state) => state.updatePreferences);

  // This component only re-renders when user.currentUser changes
  return (
    <div>
      <h2>{user?.name}</h2>
      <button onClick={() => updatePreferences({ theme: "dark" })}>
        Switch to Dark Theme
      </button>
    </div>
  );
}

export { useCounterStore, useAppStore };
```

### Q7: How do you implement middleware and persistence in Zustand?

**Answer:**
Zustand provides several built-in middleware for common patterns like persistence, devtools, and subscriptions.

```javascript
import { create } from "zustand";
import {
  devtools,
  persist,
  subscribeWithSelector,
  createJSONStorage,
} from "zustand/middleware";
import { immer } from "zustand/middleware/immer";

// Custom middleware for logging
const logger = (config) => (set, get, api) =>
  config(
    (...args) => {
      console.log("Previous state:", get());
      set(...args);
      console.log("New state:", get());
    },
    get,
    api
  );

// Custom middleware for error handling
const errorHandler = (config) => (set, get, api) => {
  const wrappedSet = (...args) => {
    try {
      set(...args);
    } catch (error) {
      console.error("State update error:", error);
      // You could dispatch to an error store here
      api.setState({ error: error.message });
    }
  };

  return config(wrappedSet, get, api);
};

// Store with multiple middleware
const useAdvancedStore = create(
  logger(
    errorHandler(
      devtools(
        persist(
          subscribeWithSelector(
            immer((set, get) => ({
              // State
              user: null,
              posts: [],
              settings: {
                theme: "light",
                notifications: true,
                autoSave: false,
              },
              error: null,

              // Actions
              setUser: (user) =>
                set((state) => {
                  state.user = user;
                  state.error = null;
                }),

              addPost: (post) =>
                set((state) => {
                  state.posts.push({
                    ...post,
                    id: Date.now(),
                    createdAt: new Date().toISOString(),
                  });
                }),

              updateSettings: (newSettings) =>
                set((state) => {
                  Object.assign(state.settings, newSettings);
                }),

              clearError: () =>
                set((state) => {
                  state.error = null;
                }),
            }))
          ),
          {
            name: "advanced-storage",
            storage: createJSONStorage(() => localStorage),
            partialize: (state) => ({
              settings: state.settings,
              user: state.user
                ? { id: state.user.id, name: state.user.name }
                : null,
            }),
            onRehydrateStorage: () => (state) => {
              console.log("Hydration finished", state);
            },
          }
        ),
        {
          name: "advanced-store",
        }
      )
    )
  )
);

// Custom storage implementation
const customStorage = {
  getItem: async (name) => {
    try {
      const value = localStorage.getItem(name);
      return value ? JSON.parse(value) : null;
    } catch (error) {
      console.error("Failed to get item from storage:", error);
      return null;
    }
  },
  setItem: async (name, value) => {
    try {
      localStorage.setItem(name, JSON.stringify(value));
    } catch (error) {
      console.error("Failed to set item in storage:", error);
    }
  },
  removeItem: async (name) => {
    try {
      localStorage.removeItem(name);
    } catch (error) {
      console.error("Failed to remove item from storage:", error);
    }
  },
};

// Store with custom storage
const useCustomStorageStore = create(
  persist(
    (set, get) => ({
      data: [],
      addData: (item) => set((state) => ({ data: [...state.data, item] })),
      clearData: () => set({ data: [] }),
    }),
    {
      name: "custom-storage",
      storage: createJSONStorage(() => customStorage),
    }
  )
);

// Subscription example
const useSubscriptionStore = create(
  subscribeWithSelector((set, get) => ({
    count: 0,
    user: null,
    increment: () => set((state) => ({ count: state.count + 1 })),
    setUser: (user) => set({ user }),
  }))
);

// Subscribe to specific state changes
useSubscriptionStore.subscribe(
  (state) => state.count,
  (count, previousCount) => {
    console.log("Count changed from", previousCount, "to", count);

    // Trigger side effects
    if (count > 10) {
      console.log("Count exceeded 10!");
    }
  }
);

// Subscribe to user changes
useSubscriptionStore.subscribe(
  (state) => state.user,
  (user, previousUser) => {
    if (user && !previousUser) {
      console.log("User logged in:", user);
      // Track login event
    } else if (!user && previousUser) {
      console.log("User logged out");
      // Track logout event
    }
  }
);

// Async middleware for API calls
const asyncMiddleware = (config) => (set, get, api) => {
  const asyncActions = {
    async fetchUser(id) {
      set({ loading: true, error: null });
      try {
        const response = await fetch(`/api/users/${id}`);
        if (!response.ok) throw new Error("Failed to fetch user");
        const user = await response.json();
        set({ user, loading: false });
        return user;
      } catch (error) {
        set({ error: error.message, loading: false });
        throw error;
      }
    },

    async saveData(data) {
      set({ saving: true });
      try {
        const response = await fetch("/api/data", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(data),
        });
        if (!response.ok) throw new Error("Failed to save data");
        set({ saving: false, lastSaved: new Date().toISOString() });
      } catch (error) {
        set({ saving: false, error: error.message });
        throw error;
      }
    },
  };

  return {
    ...config(set, get, api),
    ...asyncActions,
  };
};

// Store with async middleware
const useAsyncStore = create(
  asyncMiddleware((set, get) => ({
    user: null,
    loading: false,
    saving: false,
    error: null,
    lastSaved: null,

    clearError: () => set({ error: null }),
  }))
);

// Usage in components
function AsyncComponent() {
  const { user, loading, error, fetchUser, saveData, clearError } =
    useAsyncStore();

  const handleFetchUser = async () => {
    try {
      await fetchUser(123);
    } catch (error) {
      console.error("Failed to fetch user:", error);
    }
  };

  return (
    <div>
      {loading && <div>Loading...</div>}
      {error && (
        <div>
          Error: {error}
          <button onClick={clearError}>Clear</button>
        </div>
      )}
      {user && <div>User: {user.name}</div>}
      <button onClick={handleFetchUser}>Fetch User</button>
    </div>
  );
}

export {
  useAdvancedStore,
  useCustomStorageStore,
  useSubscriptionStore,
  useAsyncStore,
};
```

---

### Q8: How do you implement complex state patterns with Zustand?

**Answer:**
Zustand supports advanced patterns like slices, computed values, and state machines for complex applications.

```javascript
import { create } from "zustand";
import { devtools, subscribeWithSelector } from "zustand/middleware";
import { immer } from "zustand/middleware/immer";

// Slice pattern for modular state management
const createUserSlice = (set, get) => ({
  user: {
    currentUser: null,
    profile: null,
    preferences: {
      theme: "light",
      language: "en",
      notifications: true,
    },
    isAuthenticated: false,
    loading: false,
    error: null,
  },

  // User actions
  loginUser: async (credentials) => {
    set((state) => {
      state.user.loading = true;
      state.user.error = null;
    });

    try {
      const response = await fetch("/api/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(credentials),
      });

      if (!response.ok) throw new Error("Login failed");

      const { user, profile } = await response.json();

      set((state) => {
        state.user.currentUser = user;
        state.user.profile = profile;
        state.user.isAuthenticated = true;
        state.user.loading = false;
      });

      return user;
    } catch (error) {
      set((state) => {
        state.user.error = error.message;
        state.user.loading = false;
      });
      throw error;
    }
  },

  logoutUser: () =>
    set((state) => {
      state.user.currentUser = null;
      state.user.profile = null;
      state.user.isAuthenticated = false;
      state.user.preferences = {
        theme: "light",
        language: "en",
        notifications: true,
      };
    }),

  updateUserPreferences: (preferences) =>
    set((state) => {
      Object.assign(state.user.preferences, preferences);
    }),

  updateUserProfile: (updates) =>
    set((state) => {
      if (state.user.profile) {
        Object.assign(state.user.profile, updates);
      }
    }),
});

const createPostsSlice = (set, get) => ({
  posts: {
    items: [],
    categories: [],
    loading: false,
    error: null,
    pagination: {
      page: 1,
      limit: 10,
      total: 0,
      hasNext: false,
    },
    filters: {
      category: "all",
      search: "",
      sortBy: "createdAt",
      sortOrder: "desc",
    },
    cache: new Map(),
  },

  // Posts actions
  fetchPosts: async (options = {}) => {
    const { posts } = get();
    const params = { ...posts.filters, ...options };
    const cacheKey = JSON.stringify(params);

    // Check cache first
    if (posts.cache.has(cacheKey)) {
      const cachedData = posts.cache.get(cacheKey);
      set((state) => {
        state.posts.items = cachedData.items;
        state.posts.pagination = cachedData.pagination;
      });
      return;
    }

    set((state) => {
      state.posts.loading = true;
      state.posts.error = null;
    });

    try {
      const queryParams = new URLSearchParams(params);
      const response = await fetch(`/api/posts?${queryParams}`);

      if (!response.ok) throw new Error("Failed to fetch posts");

      const data = await response.json();

      set((state) => {
        state.posts.items = data.posts;
        state.posts.pagination = data.pagination;
        state.posts.loading = false;

        // Cache the result
        state.posts.cache.set(cacheKey, {
          items: data.posts,
          pagination: data.pagination,
          timestamp: Date.now(),
        });
      });
    } catch (error) {
      set((state) => {
        state.posts.error = error.message;
        state.posts.loading = false;
      });
    }
  },

  createPost: async (postData) => {
    try {
      const response = await fetch("/api/posts", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(postData),
      });

      if (!response.ok) throw new Error("Failed to create post");

      const newPost = await response.json();

      set((state) => {
        state.posts.items.unshift(newPost);
        state.posts.cache.clear(); // Invalidate cache
      });

      return newPost;
    } catch (error) {
      set((state) => {
        state.posts.error = error.message;
      });
      throw error;
    }
  },

  updatePost: async (id, updates) => {
    try {
      const response = await fetch(`/api/posts/${id}`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(updates),
      });

      if (!response.ok) throw new Error("Failed to update post");

      const updatedPost = await response.json();

      set((state) => {
        const index = state.posts.items.findIndex((p) => p.id === id);
        if (index !== -1) {
          state.posts.items[index] = updatedPost;
        }
        state.posts.cache.clear(); // Invalidate cache
      });

      return updatedPost;
    } catch (error) {
      set((state) => {
        state.posts.error = error.message;
      });
      throw error;
    }
  },

  deletePost: async (id) => {
    try {
      const response = await fetch(`/api/posts/${id}`, {
        method: "DELETE",
      });

      if (!response.ok) throw new Error("Failed to delete post");

      set((state) => {
        state.posts.items = state.posts.items.filter((p) => p.id !== id);
        state.posts.cache.clear(); // Invalidate cache
      });
    } catch (error) {
      set((state) => {
        state.posts.error = error.message;
      });
      throw error;
    }
  },

  setPostsFilters: (filters) =>
    set((state) => {
      Object.assign(state.posts.filters, filters);
    }),

  clearPostsCache: () =>
    set((state) => {
      state.posts.cache.clear();
    }),
});

const createUISlice = (set, get) => ({
  ui: {
    theme: "light",
    sidebarOpen: false,
    modals: {
      createPost: false,
      editProfile: false,
      confirmDelete: false,
    },
    notifications: [],
    loading: {
      global: false,
      posts: false,
      user: false,
    },
    errors: [],
  },

  // UI actions
  setTheme: (theme) =>
    set((state) => {
      state.ui.theme = theme;
    }),

  toggleSidebar: () =>
    set((state) => {
      state.ui.sidebarOpen = !state.ui.sidebarOpen;
    }),

  openModal: (modalName) =>
    set((state) => {
      state.ui.modals[modalName] = true;
    }),

  closeModal: (modalName) =>
    set((state) => {
      state.ui.modals[modalName] = false;
    }),

  addNotification: (notification) =>
    set((state) => {
      state.ui.notifications.push({
        id: Date.now(),
        timestamp: new Date().toISOString(),
        type: "info",
        autoClose: true,
        duration: 5000,
        ...notification,
      });
    }),

  removeNotification: (id) =>
    set((state) => {
      state.ui.notifications = state.ui.notifications.filter(
        (n) => n.id !== id
      );
    }),

  setLoading: (key, loading) =>
    set((state) => {
      state.ui.loading[key] = loading;
    }),

  addError: (error) =>
    set((state) => {
      state.ui.errors.push({
        id: Date.now(),
        message: error.message || error,
        timestamp: new Date().toISOString(),
      });
    }),

  removeError: (id) =>
    set((state) => {
      state.ui.errors = state.ui.errors.filter((e) => e.id !== id);
    }),
});

// Computed values slice
const createComputedSlice = (set, get) => ({
  // Computed getters
  get filteredPosts() {
    const { posts } = get();
    let filtered = posts.items;

    if (posts.filters.category !== "all") {
      filtered = filtered.filter(
        (post) => post.category === posts.filters.category
      );
    }

    if (posts.filters.search) {
      const search = posts.filters.search.toLowerCase();
      filtered = filtered.filter(
        (post) =>
          post.title.toLowerCase().includes(search) ||
          post.content.toLowerCase().includes(search)
      );
    }

    // Sort posts
    filtered.sort((a, b) => {
      const aValue = a[posts.filters.sortBy];
      const bValue = b[posts.filters.sortBy];

      if (posts.filters.sortOrder === "asc") {
        return aValue > bValue ? 1 : -1;
      } else {
        return aValue < bValue ? 1 : -1;
      }
    });

    return filtered;
  },

  get userStats() {
    const { user, posts } = get();
    if (!user.currentUser) return null;

    const userPosts = posts.items.filter(
      (post) => post.authorId === user.currentUser.id
    );

    return {
      totalPosts: userPosts.length,
      totalViews: userPosts.reduce((sum, post) => sum + (post.views || 0), 0),
      totalLikes: userPosts.reduce((sum, post) => sum + (post.likes || 0), 0),
      averageViews:
        userPosts.length > 0
          ? userPosts.reduce((sum, post) => sum + (post.views || 0), 0) /
            userPosts.length
          : 0,
    };
  },

  get isLoading() {
    const { ui, user, posts } = get();
    return ui.loading.global || user.loading || posts.loading;
  },
});

// Main store combining all slices
const useAppStore = create(
  devtools(
    subscribeWithSelector(
      immer((set, get) => ({
        ...createUserSlice(set, get),
        ...createPostsSlice(set, get),
        ...createUISlice(set, get),
        ...createComputedSlice(set, get),
      }))
    ),
    { name: "app-store" }
  )
);

// State machine pattern for complex workflows
const createStateMachine = (initialState, transitions) => {
  return create((set, get) => ({
    currentState: initialState,
    context: {},

    transition: (event, payload = {}) => {
      const { currentState } = get();
      const stateConfig = transitions[currentState];

      if (!stateConfig || !stateConfig[event]) {
        console.warn(`Invalid transition: ${event} from ${currentState}`);
        return false;
      }

      const transition = stateConfig[event];
      const nextState =
        typeof transition.target === "function"
          ? transition.target(get().context, payload)
          : transition.target;

      set((state) => {
        state.currentState = nextState;

        // Update context if action provided
        if (transition.action) {
          state.context = transition.action(state.context, payload);
        }
      });

      return true;
    },

    can: (event) => {
      const { currentState } = get();
      const stateConfig = transitions[currentState];
      return stateConfig && stateConfig[event];
    },

    is: (state) => get().currentState === state,
  }));
};

// Example: Post creation workflow state machine
const usePostCreationMachine = createStateMachine("idle", {
  idle: {
    START_CREATION: {
      target: "editing",
      action: (context, payload) => ({
        ...context,
        draft: { title: "", content: "", category: "" },
      }),
    },
  },
  editing: {
    UPDATE_DRAFT: {
      target: "editing",
      action: (context, payload) => ({
        ...context,
        draft: { ...context.draft, ...payload },
      }),
    },
    VALIDATE: {
      target: (context) => {
        const { title, content } = context.draft;
        return title && content ? "valid" : "invalid";
      },
    },
    CANCEL: {
      target: "idle",
      action: () => ({}),
    },
  },
  valid: {
    SUBMIT: {
      target: "submitting",
      action: (context) => ({
        ...context,
        submittedAt: new Date().toISOString(),
      }),
    },
    EDIT: {
      target: "editing",
    },
  },
  invalid: {
    EDIT: {
      target: "editing",
    },
  },
  submitting: {
    SUCCESS: {
      target: "success",
      action: (context, payload) => ({ ...context, result: payload }),
    },
    ERROR: {
      target: "error",
      action: (context, payload) => ({ ...context, error: payload }),
    },
  },
  success: {
    RESET: {
      target: "idle",
      action: () => ({}),
    },
  },
  error: {
    RETRY: {
      target: "submitting",
    },
    EDIT: {
      target: "editing",
    },
    CANCEL: {
      target: "idle",
      action: () => ({}),
    },
  },
});

export { useAppStore, usePostCreationMachine, createStateMachine };
```

---

### Q9: When should you choose Redux over Zustand and vice versa?

**Answer:**
The choice between Redux and Zustand depends on project requirements, team preferences, and application complexity.

**Choose Redux when:**

- Large, complex applications with many developers
- Need for time-travel debugging and extensive DevTools
- Strict patterns and predictability are required
- Heavy use of middleware ecosystem
- Team is already familiar with Redux patterns

**Choose Zustand when:**

- Smaller to medium-sized applications
- Want minimal boilerplate and faster development
- TypeScript-first development
- Need flexible state management without strict patterns
- Bundle size is a concern

```javascript
// Redux approach - More verbose but structured
// actions/userActions.js
export const LOGIN_REQUEST = "LOGIN_REQUEST";
export const LOGIN_SUCCESS = "LOGIN_SUCCESS";
export const LOGIN_FAILURE = "LOGIN_FAILURE";

export const loginRequest = () => ({ type: LOGIN_REQUEST });
export const loginSuccess = (user) => ({ type: LOGIN_SUCCESS, payload: user });
export const loginFailure = (error) => ({
  type: LOGIN_FAILURE,
  payload: error,
});

export const login = (credentials) => async (dispatch) => {
  dispatch(loginRequest());
  try {
    const response = await fetch("/api/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(credentials),
    });
    const user = await response.json();
    dispatch(loginSuccess(user));
  } catch (error) {
    dispatch(loginFailure(error.message));
  }
};

// reducers/userReducer.js
const initialState = {
  user: null,
  loading: false,
  error: null,
};

export default function userReducer(state = initialState, action) {
  switch (action.type) {
    case LOGIN_REQUEST:
      return { ...state, loading: true, error: null };
    case LOGIN_SUCCESS:
      return { ...state, loading: false, user: action.payload };
    case LOGIN_FAILURE:
      return { ...state, loading: false, error: action.payload };
    default:
      return state;
  }
}

// store.js
import { configureStore } from "@reduxjs/toolkit";
import userReducer from "./reducers/userReducer";

export const store = configureStore({
  reducer: {
    user: userReducer,
  },
});

// Component usage
import { useSelector, useDispatch } from "react-redux";
import { login } from "./actions/userActions";

function LoginComponent() {
  const { user, loading, error } = useSelector((state) => state.user);
  const dispatch = useDispatch();

  const handleLogin = (credentials) => {
    dispatch(login(credentials));
  };

  return (
    <div>
      {loading && <div>Loading...</div>}
      {error && <div>Error: {error}</div>}
      {user && <div>Welcome, {user.name}!</div>}
    </div>
  );
}

// Zustand approach - More concise and direct
import { create } from "zustand";

const useUserStore = create((set, get) => ({
  user: null,
  loading: false,
  error: null,

  login: async (credentials) => {
    set({ loading: true, error: null });
    try {
      const response = await fetch("/api/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(credentials),
      });
      const user = await response.json();
      set({ loading: false, user });
    } catch (error) {
      set({ loading: false, error: error.message });
    }
  },

  logout: () => set({ user: null, error: null }),
}));

// Component usage
function LoginComponent() {
  const { user, loading, error, login } = useUserStore();

  const handleLogin = (credentials) => {
    login(credentials);
  };

  return (
    <div>
      {loading && <div>Loading...</div>}
      {error && <div>Error: {error}</div>}
      {user && <div>Welcome, {user.name}!</div>}
    </div>
  );
}
```

### Q10: How do you migrate from Redux to Zustand?

**Answer:**
Migrating from Redux to Zustand can be done incrementally by replacing Redux slices with Zustand stores.

```javascript
// Step 1: Create equivalent Zustand stores for Redux slices

// Original Redux slice
// userSlice.js (Redux Toolkit)
import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";

export const fetchUser = createAsyncThunk("user/fetchUser", async (userId) => {
  const response = await fetch(`/api/users/${userId}`);
  return response.json();
});

const userSlice = createSlice({
  name: "user",
  initialState: {
    currentUser: null,
    loading: false,
    error: null,
  },
  reducers: {
    logout: (state) => {
      state.currentUser = null;
    },
    clearError: (state) => {
      state.error = null;
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchUser.pending, (state) => {
        state.loading = true;
      })
      .addCase(fetchUser.fulfilled, (state, action) => {
        state.loading = false;
        state.currentUser = action.payload;
      })
      .addCase(fetchUser.rejected, (state, action) => {
        state.loading = false;
        state.error = action.error.message;
      });
  },
});

export const { logout, clearError } = userSlice.actions;
export default userSlice.reducer;

// Equivalent Zustand store
// userStore.js (Zustand)
import { create } from "zustand";
import { devtools } from "zustand/middleware";

export const useUserStore = create(
  devtools(
    (set, get) => ({
      currentUser: null,
      loading: false,
      error: null,

      fetchUser: async (userId) => {
        set({ loading: true, error: null });
        try {
          const response = await fetch(`/api/users/${userId}`);
          const user = await response.json();
          set({ loading: false, currentUser: user });
        } catch (error) {
          set({ loading: false, error: error.message });
        }
      },

      logout: () => set({ currentUser: null }),

      clearError: () => set({ error: null }),
    }),
    { name: "user-store" }
  )
);

// Step 2: Create a migration adapter for gradual transition
// migrationAdapter.js
import { useSelector, useDispatch } from "react-redux";
import { useUserStore } from "./userStore";
import { fetchUser, logout, clearError } from "./userSlice";

// Adapter hook that provides the same interface as Redux
export const useUserMigration = (useZustand = false) => {
  const reduxUser = useSelector((state) => state.user);
  const dispatch = useDispatch();

  const zustandUser = useUserStore();

  if (useZustand) {
    return {
      currentUser: zustandUser.currentUser,
      loading: zustandUser.loading,
      error: zustandUser.error,
      fetchUser: zustandUser.fetchUser,
      logout: zustandUser.logout,
      clearError: zustandUser.clearError,
    };
  }

  return {
    currentUser: reduxUser.currentUser,
    loading: reduxUser.loading,
    error: reduxUser.error,
    fetchUser: (userId) => dispatch(fetchUser(userId)),
    logout: () => dispatch(logout()),
    clearError: () => dispatch(clearError()),
  };
};

// Step 3: Update components gradually
// UserProfile.js - Before migration
import { useSelector, useDispatch } from "react-redux";
import { fetchUser, logout } from "./userSlice";

function UserProfile({ userId }) {
  const { currentUser, loading, error } = useSelector((state) => state.user);
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(fetchUser(userId));
  }, [userId, dispatch]);

  const handleLogout = () => {
    dispatch(logout());
  };

  return (
    <div>
      {loading && <div>Loading...</div>}
      {error && <div>Error: {error}</div>}
      {currentUser && (
        <div>
          <h2>{currentUser.name}</h2>
          <button onClick={handleLogout}>Logout</button>
        </div>
      )}
    </div>
  );
}

// UserProfile.js - During migration (using adapter)
import { useUserMigration } from "./migrationAdapter";

function UserProfile({ userId }) {
  // Toggle this flag to switch between Redux and Zustand
  const useZustand = process.env.REACT_APP_USE_ZUSTAND === "true";
  const { currentUser, loading, error, fetchUser, logout } =
    useUserMigration(useZustand);

  useEffect(() => {
    fetchUser(userId);
  }, [userId, fetchUser]);

  return (
    <div>
      {loading && <div>Loading...</div>}
      {error && <div>Error: {error}</div>}
      {currentUser && (
        <div>
          <h2>{currentUser.name}</h2>
          <button onClick={logout}>Logout</button>
        </div>
      )}
    </div>
  );
}

// UserProfile.js - After migration (pure Zustand)
import { useUserStore } from "./userStore";

function UserProfile({ userId }) {
  const { currentUser, loading, error, fetchUser, logout } = useUserStore();

  useEffect(() => {
    fetchUser(userId);
  }, [userId, fetchUser]);

  return (
    <div>
      {loading && <div>Loading...</div>}
      {error && <div>Error: {error}</div>}
      {currentUser && (
        <div>
          <h2>{currentUser.name}</h2>
          <button onClick={logout}>Logout</button>
        </div>
      )}
    </div>
  );
}

// Step 4: Migration utilities
// migrationUtils.js
export const createMigrationStore = (reduxSlice, zustandStore) => {
  return {
    // Sync Redux state to Zustand
    syncToZustand: (reduxState) => {
      zustandStore.setState(reduxState);
    },

    // Sync Zustand state to Redux
    syncToRedux: (dispatch) => {
      const zustandState = zustandStore.getState();
      dispatch(reduxSlice.actions.setState(zustandState));
    },

    // Compare states for debugging
    compareStates: (reduxState) => {
      const zustandState = zustandStore.getState();
      console.log("Redux state:", reduxState);
      console.log("Zustand state:", zustandState);
      console.log(
        "States match:",
        JSON.stringify(reduxState) === JSON.stringify(zustandState)
      );
    },
  };
};

// Step 5: Testing utilities
// testUtils.js
import { renderHook, act } from "@testing-library/react";
import { Provider } from "react-redux";
import { store } from "./store";
import { useUserStore } from "./userStore";

// Test both Redux and Zustand implementations
export const testBothImplementations = (testFn) => {
  describe("Redux implementation", () => {
    testFn("redux");
  });

  describe("Zustand implementation", () => {
    testFn("zustand");
  });
};

// Example test
testBothImplementations((implementation) => {
  it("should handle user login", async () => {
    if (implementation === "redux") {
      // Test Redux implementation
      const wrapper = ({ children }) => (
        <Provider store={store}>{children}</Provider>
      );

      const { result } = renderHook(() => useSelector((state) => state.user), {
        wrapper,
      });
      // ... Redux-specific test logic
    } else {
      // Test Zustand implementation
      const { result } = renderHook(() => useUserStore());
      // ... Zustand-specific test logic
    }
  });
});
```

---

### Q11: How do you optimize performance in Redux and Zustand?

**Answer:**
Both Redux and Zustand offer different approaches to performance optimization.

**Redux Performance Optimization:**

```javascript
import { createSelector } from "@reduxjs/toolkit";
import { shallowEqual, useSelector } from "react-redux";
import { memo, useMemo, useCallback } from "react";

// 1. Use memoized selectors
const selectPosts = (state) => state.posts.items;
const selectFilters = (state) => state.posts.filters;

const selectFilteredPosts = createSelector(
  [selectPosts, selectFilters],
  (posts, filters) => {
    console.log("Recomputing filtered posts"); // Only logs when inputs change

    let filtered = posts;

    if (filters.category !== "all") {
      filtered = filtered.filter((post) => post.category === filters.category);
    }

    if (filters.search) {
      const searchLower = filters.search.toLowerCase();
      filtered = filtered.filter((post) =>
        post.title.toLowerCase().includes(searchLower)
      );
    }

    return filtered.sort(
      (a, b) => new Date(b.createdAt) - new Date(a.createdAt)
    );
  }
);

// 2. Use shallow equality for object selections
function PostsList() {
  const { posts, loading, error } = useSelector(
    (state) => ({
      posts: selectFilteredPosts(state),
      loading: state.posts.loading,
      error: state.posts.error,
    }),
    shallowEqual // Prevents re-renders when object shape is the same
  );

  return (
    <div>
      {loading && <div>Loading...</div>}
      {error && <div>Error: {error}</div>}
      {posts.map((post) => (
        <PostItem key={post.id} post={post} />
      ))}
    </div>
  );
}

// 3. Memoize components
const PostItem = memo(({ post, onDelete, onEdit }) => {
  const handleDelete = useCallback(() => {
    onDelete(post.id);
  }, [post.id, onDelete]);

  const handleEdit = useCallback(() => {
    onEdit(post);
  }, [post, onEdit]);

  return (
    <div className="post-item">
      <h3>{post.title}</h3>
      <p>{post.excerpt}</p>
      <div>
        <button onClick={handleEdit}>Edit</button>
        <button onClick={handleDelete}>Delete</button>
      </div>
    </div>
  );
});

// 4. Normalize state structure
const postsAdapter = createEntityAdapter({
  selectId: (post) => post.id,
  sortComparer: (a, b) => b.createdAt.localeCompare(a.createdAt),
});

const postsSlice = createSlice({
  name: "posts",
  initialState: postsAdapter.getInitialState({
    loading: false,
    error: null,
  }),
  reducers: {
    addPost: postsAdapter.addOne,
    updatePost: postsAdapter.updateOne,
    removePost: postsAdapter.removeOne,
    setPosts: postsAdapter.setAll,
  },
});

// Optimized selectors
export const {
  selectAll: selectAllPosts,
  selectById: selectPostById,
  selectIds: selectPostIds,
} = postsAdapter.getSelectors((state) => state.posts);

// 5. Use RTK Query for automatic caching
import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

const apiSlice = createApi({
  reducerPath: "api",
  baseQuery: fetchBaseQuery({ baseUrl: "/api" }),
  tagTypes: ["Post"],
  endpoints: (builder) => ({
    getPosts: builder.query({
      query: (params) => `posts?${new URLSearchParams(params)}`,
      providesTags: (result) =>
        result
          ? [
              ...result.map(({ id }) => ({ type: "Post", id })),
              { type: "Post", id: "LIST" },
            ]
          : [{ type: "Post", id: "LIST" }],
      // Cache for 60 seconds
      keepUnusedDataFor: 60,
    }),
  }),
});
```

**Zustand Performance Optimization:**

```javascript
import { create } from "zustand";
import { subscribeWithSelector } from "zustand/middleware";
import { shallow } from "zustand/shallow";
import { memo, useMemo } from "react";

// 1. Use selective subscriptions
const useAppStore = create(
  subscribeWithSelector((set, get) => ({
    posts: [],
    filters: { category: "all", search: "" },
    user: null,
    ui: { theme: "light", sidebarOpen: false },

    setPosts: (posts) => set({ posts }),
    setFilters: (filters) =>
      set((state) => ({
        filters: { ...state.filters, ...filters },
      })),
    setUser: (user) => set({ user }),
    toggleSidebar: () =>
      set((state) => ({
        ui: { ...state.ui, sidebarOpen: !state.ui.sidebarOpen },
      })),
  }))
);

// 2. Selective subscriptions to prevent unnecessary re-renders
function PostsList() {
  // Only re-render when posts or filters change
  const { posts, filters } = useAppStore(
    (state) => ({ posts: state.posts, filters: state.filters }),
    shallow
  );

  const filteredPosts = useMemo(() => {
    let filtered = posts;

    if (filters.category !== "all") {
      filtered = filtered.filter((post) => post.category === filters.category);
    }

    if (filters.search) {
      const searchLower = filters.search.toLowerCase();
      filtered = filtered.filter((post) =>
        post.title.toLowerCase().includes(searchLower)
      );
    }

    return filtered;
  }, [posts, filters]);

  return (
    <div>
      {filteredPosts.map((post) => (
        <PostItem key={post.id} post={post} />
      ))}
    </div>
  );
}

// 3. Use specific selectors for individual values
function UserProfile() {
  // Only re-render when user changes, not when other state changes
  const user = useAppStore((state) => state.user);
  const setUser = useAppStore((state) => state.setUser);

  return (
    <div>
      {user ? (
        <div>
          <h2>{user.name}</h2>
          <p>{user.email}</p>
        </div>
      ) : (
        <div>Not logged in</div>
      )}
    </div>
  );
}

// 4. Optimize with computed values
const useOptimizedStore = create((set, get) => ({
  items: [],
  filters: { search: "", category: "all" },

  // Computed getter - only recalculates when accessed
  get filteredItems() {
    const { items, filters } = get();
    console.log("Computing filtered items"); // Only logs when accessed

    return items.filter((item) => {
      if (filters.category !== "all" && item.category !== filters.category) {
        return false;
      }
      if (
        filters.search &&
        !item.name.toLowerCase().includes(filters.search.toLowerCase())
      ) {
        return false;
      }
      return true;
    });
  },

  addItem: (item) =>
    set((state) => ({
      items: [...state.items, item],
    })),

  setFilters: (newFilters) =>
    set((state) => ({
      filters: { ...state.filters, ...newFilters },
    })),
}));

// 5. Use subscriptions for side effects
const useStoreWithEffects = create(
  subscribeWithSelector((set, get) => ({
    user: null,
    posts: [],
    analytics: { pageViews: 0, userActions: 0 },

    setUser: (user) => set({ user }),
    addPost: (post) =>
      set((state) => ({
        posts: [...state.posts, post],
        analytics: {
          ...state.analytics,
          userActions: state.analytics.userActions + 1,
        },
      })),
    incrementPageViews: () =>
      set((state) => ({
        analytics: {
          ...state.analytics,
          pageViews: state.analytics.pageViews + 1,
        },
      })),
  }))
);

// Subscribe to user changes for analytics
useStoreWithEffects.subscribe(
  (state) => state.user,
  (user, previousUser) => {
    if (user && !previousUser) {
      // User logged in
      console.log("User logged in, tracking event");
      // Track login event
    }
  }
);

// 6. Memoized components with Zustand
const OptimizedPostItem = memo(({ postId }) => {
  // Only subscribe to the specific post
  const post = useAppStore((state) => state.posts.find((p) => p.id === postId));

  const updatePost = useAppStore((state) => state.updatePost);

  if (!post) return null;

  return (
    <div>
      <h3>{post.title}</h3>
      <p>{post.content}</p>
      <button onClick={() => updatePost(postId, { views: post.views + 1 })}>
        View ({post.views})
      </button>
    </div>
  );
});

// 7. Batch updates for better performance
const useBatchedStore = create((set, get) => ({
  items: [],
  loading: false,
  error: null,

  fetchItems: async () => {
    // Batch multiple state updates
    set({ loading: true, error: null });

    try {
      const response = await fetch("/api/items");
      const items = await response.json();

      // Single state update instead of multiple
      set({
        items,
        loading: false,
        error: null,
      });
    } catch (error) {
      set({
        loading: false,
        error: error.message,
      });
    }
  },

  bulkUpdateItems: (updates) => {
    set((state) => ({
      items: state.items.map((item) => {
        const update = updates.find((u) => u.id === item.id);
        return update ? { ...item, ...update } : item;
      }),
    }));
  },
}));

export { useAppStore, useOptimizedStore, useStoreWithEffects, useBatchedStore };
```

### Q12: What are the best practices for testing Redux and Zustand stores?

**Answer:**
Testing state management requires different approaches for Redux and Zustand, focusing on actions, state changes, and component integration.

**Redux Testing:**

```javascript
// Redux testing with Jest and React Testing Library
import { configureStore } from "@reduxjs/toolkit";
import { renderHook, act } from "@testing-library/react";
import { Provider } from "react-redux";
import userSlice, { loginUser, logout } from "./userSlice";

// Test reducer directly
describe("userSlice reducer", () => {
  const initialState = {
    currentUser: null,
    loading: false,
    error: null,
  };

  it("should handle initial state", () => {
    expect(userSlice.reducer(undefined, { type: "unknown" })).toEqual(
      initialState
    );
  });

  it("should handle logout", () => {
    const previousState = {
      currentUser: { id: 1, name: "John" },
      loading: false,
      error: null,
    };

    expect(userSlice.reducer(previousState, logout())).toEqual(initialState);
  });
});

// Test async thunks
describe("loginUser async thunk", () => {
  let store;

  beforeEach(() => {
    store = configureStore({
      reducer: {
        user: userSlice.reducer,
      },
    });

    // Mock fetch
    global.fetch = jest.fn();
  });

  afterEach(() => {
    jest.resetAllMocks();
  });

  it("should handle successful login", async () => {
    const mockUser = { id: 1, name: "John", email: "john@example.com" };

    fetch.mockResolvedValueOnce({
      ok: true,
      json: async () => mockUser,
    });

    await store.dispatch(
      loginUser({ email: "john@example.com", password: "password" })
    );

    const state = store.getState().user;
    expect(state.currentUser).toEqual(mockUser);
    expect(state.loading).toBe(false);
    expect(state.error).toBe(null);
  });

  it("should handle login failure", async () => {
    fetch.mockRejectedValueOnce(new Error("Login failed"));

    await store.dispatch(
      loginUser({ email: "john@example.com", password: "wrong" })
    );

    const state = store.getState().user;
    expect(state.currentUser).toBe(null);
    expect(state.loading).toBe(false);
    expect(state.error).toBe("Login failed");
  });
});

// Test component integration
import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import LoginForm from "./LoginForm";

const renderWithProvider = (component, initialState = {}) => {
  const store = configureStore({
    reducer: {
      user: userSlice.reducer,
    },
    preloadedState: initialState,
  });

  return {
    ...render(<Provider store={store}>{component}</Provider>),
    store,
  };
};

describe("LoginForm component", () => {
  beforeEach(() => {
    global.fetch = jest.fn();
  });

  it("should display loading state during login", async () => {
    fetch.mockImplementation(
      () =>
        new Promise((resolve) => {
          setTimeout(
            () =>
              resolve({
                ok: true,
                json: () => Promise.resolve({ id: 1, name: "John" }),
              }),
            100
          );
        })
    );

    renderWithProvider(<LoginForm />);

    fireEvent.change(screen.getByLabelText(/email/i), {
      target: { value: "john@example.com" },
    });
    fireEvent.change(screen.getByLabelText(/password/i), {
      target: { value: "password" },
    });
    fireEvent.click(screen.getByRole("button", { name: /login/i }));

    expect(screen.getByText(/logging in/i)).toBeInTheDocument();

    await waitFor(() => {
      expect(screen.queryByText(/logging in/i)).not.toBeInTheDocument();
    });
  });
});
```

**Zustand Testing:**

```javascript
// Zustand testing
import { renderHook, act } from "@testing-library/react";
import { useUserStore } from "./userStore";

// Test store directly
describe("useUserStore", () => {
  beforeEach(() => {
    // Reset store before each test
    useUserStore.setState({
      currentUser: null,
      loading: false,
      error: null,
    });

    global.fetch = jest.fn();
  });

  afterEach(() => {
    jest.resetAllMocks();
  });

  it("should have initial state", () => {
    const { result } = renderHook(() => useUserStore());

    expect(result.current.currentUser).toBe(null);
    expect(result.current.loading).toBe(false);
    expect(result.current.error).toBe(null);
  });

  it("should handle logout", () => {
    const { result } = renderHook(() => useUserStore());

    // Set initial user
    act(() => {
      useUserStore.setState({ currentUser: { id: 1, name: "John" } });
    });

    expect(result.current.currentUser).toEqual({ id: 1, name: "John" });

    // Logout
    act(() => {
      result.current.logout();
    });

    expect(result.current.currentUser).toBe(null);
  });

  it("should handle successful login", async () => {
    const mockUser = { id: 1, name: "John", email: "john@example.com" };

    fetch.mockResolvedValueOnce({
      ok: true,
      json: async () => mockUser,
    });

    const { result } = renderHook(() => useUserStore());

    await act(async () => {
      await result.current.login({
        email: "john@example.com",
        password: "password",
      });
    });

    expect(result.current.currentUser).toEqual(mockUser);
    expect(result.current.loading).toBe(false);
    expect(result.current.error).toBe(null);
  });

  it("should handle login failure", async () => {
    fetch.mockRejectedValueOnce(new Error("Login failed"));

    const { result } = renderHook(() => useUserStore());

    await act(async () => {
      try {
        await result.current.login({
          email: "john@example.com",
          password: "wrong",
        });
      } catch (error) {
        // Expected to throw
      }
    });

    expect(result.current.currentUser).toBe(null);
    expect(result.current.loading).toBe(false);
    expect(result.current.error).toBe("Login failed");
  });
});

// Test store subscriptions
describe("useUserStore subscriptions", () => {
  it("should notify subscribers of state changes", () => {
    const subscriber = jest.fn();

    const unsubscribe = useUserStore.subscribe(subscriber);

    act(() => {
      useUserStore.setState({ currentUser: { id: 1, name: "John" } });
    });

    expect(subscriber).toHaveBeenCalledWith(
      expect.objectContaining({
        currentUser: { id: 1, name: "John" },
      }),
      expect.objectContaining({
        currentUser: null,
      })
    );

    unsubscribe();
  });
});

// Test component integration with Zustand
import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import LoginForm from "./LoginForm";

describe("LoginForm with Zustand", () => {
  beforeEach(() => {
    // Reset store
    useUserStore.setState({
      currentUser: null,
      loading: false,
      error: null,
    });

    global.fetch = jest.fn();
  });

  it("should display user after successful login", async () => {
    const mockUser = { id: 1, name: "John" };

    fetch.mockResolvedValueOnce({
      ok: true,
      json: async () => mockUser,
    });

    render(<LoginForm />);

    fireEvent.change(screen.getByLabelText(/email/i), {
      target: { value: "john@example.com" },
    });
    fireEvent.change(screen.getByLabelText(/password/i), {
      target: { value: "password" },
    });
    fireEvent.click(screen.getByRole("button", { name: /login/i }));

    await waitFor(() => {
      expect(screen.getByText(/welcome, john/i)).toBeInTheDocument();
    });
  });
});

// Test utilities for Zustand
export const createTestStore = (initialState = {}) => {
  const store = useUserStore;
  store.setState(initialState);
  return store;
};

export const mockStoreActions = () => {
  const originalLogin = useUserStore.getState().login;
  const originalLogout = useUserStore.getState().logout;

  const mockLogin = jest.fn();
  const mockLogout = jest.fn();

  useUserStore.setState({
    login: mockLogin,
    logout: mockLogout,
  });

  return {
    mockLogin,
    mockLogout,
    restore: () => {
      useUserStore.setState({
        login: originalLogin,
        logout: originalLogout,
      });
    },
  };
};

// Integration test helper
export const testStoreIntegration = (Component, initialState = {}) => {
  beforeEach(() => {
    useUserStore.setState({
      currentUser: null,
      loading: false,
      error: null,
      ...initialState,
    });
  });

  return render(<Component />);
};
```

These examples demonstrate comprehensive testing strategies for both Redux and Zustand, covering unit tests, integration tests, and testing utilities.

---

### Q13: What are the key differences between Redux and Zustand, and when should you use each?

**Answer:**
Redux and Zustand are both state management libraries, but they differ significantly in philosophy, complexity, and use cases.

**Key Differences:**

**1. Boilerplate and Setup:**

_Redux:_

```javascript
// Redux requires multiple files and setup
// actions/userActions.js
export const LOAD_USERS = "LOAD_USERS";
export const LOAD_USERS_SUCCESS = "LOAD_USERS_SUCCESS";
export const LOAD_USERS_FAILURE = "LOAD_USERS_FAILURE";

export const loadUsers = () => ({ type: LOAD_USERS });
export const loadUsersSuccess = (users) => ({
  type: LOAD_USERS_SUCCESS,
  payload: users,
});
export const loadUsersFailure = (error) => ({
  type: LOAD_USERS_FAILURE,
  payload: error,
});

// reducers/userReducer.js
import {
  LOAD_USERS,
  LOAD_USERS_SUCCESS,
  LOAD_USERS_FAILURE,
} from "../actions/userActions";

const initialState = {
  users: [],
  loading: false,
  error: null,
};

export const userReducer = (state = initialState, action) => {
  switch (action.type) {
    case LOAD_USERS:
      return {
        ...state,
        loading: true,
        error: null,
      };
    case LOAD_USERS_SUCCESS:
      return {
        ...state,
        loading: false,
        users: action.payload,
      };
    case LOAD_USERS_FAILURE:
      return {
        ...state,
        loading: false,
        error: action.payload,
      };
    default:
      return state;
  }
};

// store/index.js
import { createStore, combineReducers, applyMiddleware } from "redux";
import { userReducer } from "../reducers/userReducer";
import thunk from "redux-thunk";

const rootReducer = combineReducers({
  users: userReducer,
});

export const store = createStore(rootReducer, applyMiddleware(thunk));
```

_Zustand:_

```javascript
// Single file store definition
import { create } from "zustand";

export const useUserStore = create((set, get) => ({
  users: [],
  loading: false,
  error: null,

  loadUsers: async () => {
    set({ loading: true, error: null });
    try {
      const response = await fetch("/api/users");
      const users = await response.json();
      set({ users, loading: false });
    } catch (error) {
      set({ error: error.message, loading: false });
    }
  },

  addUser: (user) =>
    set((state) => ({
      users: [...state.users, user],
    })),

  updateUser: (id, updates) =>
    set((state) => ({
      users: state.users.map((user) =>
        user.id === id ? { ...user, ...updates } : user
      ),
    })),

  deleteUser: (id) =>
    set((state) => ({
      users: state.users.filter((user) => user.id !== id),
    })),

  clearError: () => set({ error: null }),
}));
```

**2. Component Usage:**

_Redux:_

```javascript
import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { loadUsers, addUser } from "../actions/userActions";

const UserList = () => {
  const { users, loading, error } = useSelector((state) => state.users);
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(loadUsers());
  }, [dispatch]);

  const handleAddUser = (userData) => {
    dispatch(addUser(userData));
  };

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      {users.map((user) => (
        <div key={user.id}>{user.name}</div>
      ))}
      <button onClick={() => handleAddUser({ name: "New User" })}>
        Add User
      </button>
    </div>
  );
};
```

_Zustand:_

```javascript
import React, { useEffect } from "react";
import { useUserStore } from "../stores/userStore";

const UserList = () => {
  const { users, loading, error, loadUsers, addUser } = useUserStore();

  useEffect(() => {
    loadUsers();
  }, [loadUsers]);

  const handleAddUser = () => {
    addUser({ id: Date.now(), name: "New User" });
  };

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      {users.map((user) => (
        <div key={user.id}>{user.name}</div>
      ))}
      <button onClick={handleAddUser}>Add User</button>
    </div>
  );
};
```

**When to Use Each:**

**Use Redux when:**

- Building large, complex applications with multiple teams
- Need predictable state updates with time-travel debugging
- Require extensive middleware ecosystem (sagas, observables)
- Need strict patterns and conventions across the team
- Building applications with complex async flows
- Need hot reloading and advanced debugging capabilities
- Working with legacy codebases already using Redux

**Use Zustand when:**

- Building small to medium-sized applications
- Want minimal boilerplate and faster development
- Need simple, intuitive API with TypeScript support
- Prefer co-locating state logic with business logic
- Want built-in async support without additional middleware
- Need selective subscriptions for performance optimization
- Building modern React applications with hooks-first approach
- Want easy integration with existing codebases

**Performance Comparison:**

Redux typically has more overhead due to its architecture, while Zustand offers better performance out of the box with selective subscriptions and minimal re-renders.

---

### Q14: How do you implement middleware in Redux and Zustand?

**Answer:**
Middleware in both Redux and Zustand allows you to intercept and modify actions or state changes, enabling features like logging, async handling, and persistence.

**Redux Middleware:**

**1. Custom Logging Middleware:**

```javascript
// Custom logging middleware
const loggerMiddleware = (store) => (next) => (action) => {
  console.group(`Action: ${action.type}`);
  console.log("Previous State:", store.getState());
  console.log("Action:", action);

  const result = next(action);

  console.log("Next State:", store.getState());
  console.groupEnd();

  return result;
};

// API middleware for handling async actions
const apiMiddleware = (store) => (next) => (action) => {
  if (action.type?.endsWith("_REQUEST")) {
    const {
      endpoint,
      method = "GET",
      body,
      onSuccess,
      onFailure,
    } = action.payload;

    fetch(endpoint, {
      method,
      headers: { "Content-Type": "application/json" },
      body: body ? JSON.stringify(body) : undefined,
    })
      .then((response) => response.json())
      .then((data) => {
        if (onSuccess) {
          store.dispatch(onSuccess(data));
        }
      })
      .catch((error) => {
        if (onFailure) {
          store.dispatch(onFailure(error.message));
        }
      });
  }

  return next(action);
};

// Store setup with middleware
import { createStore, applyMiddleware, compose } from "redux";
import thunk from "redux-thunk";

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

const store = createStore(
  rootReducer,
  composeEnhancers(applyMiddleware(thunk, loggerMiddleware, apiMiddleware))
);
```

**2. Redux Toolkit Middleware:**

```javascript
import { configureStore, createListenerMiddleware } from "@reduxjs/toolkit";
import { userSlice } from "./userSlice";

// Listener middleware for side effects
const listenerMiddleware = createListenerMiddleware();

// Listen for specific actions
listenerMiddleware.startListening({
  actionCreator: userSlice.actions.userLoggedIn,
  effect: async (action, listenerApi) => {
    // Perform side effects
    console.log("User logged in:", action.payload);

    // Dispatch other actions
    listenerApi.dispatch(userSlice.actions.loadUserPreferences());

    // Access current state
    const state = listenerApi.getState();
    console.log("Current state:", state);
  },
});

// Custom middleware for RTK
const customRTKMiddleware = (api) => (next) => (action) => {
  if (action.type.startsWith("user/")) {
    console.log("User action dispatched:", action);
  }
  return next(action);
};

const store = configureStore({
  reducer: {
    user: userSlice.reducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: {
        ignoredActions: ["persist/PERSIST"],
      },
    })
      .prepend(listenerMiddleware.middleware)
      .concat(customRTKMiddleware),
});
```

**Zustand Middleware:**

**1. Built-in Middleware:**

```javascript
import { create } from "zustand";
import { persist, createJSONStorage } from "zustand/middleware";
import { immer } from "zustand/middleware/immer";
import { devtools } from "zustand/middleware";
import { subscribeWithSelector } from "zustand/middleware";

// Combining multiple middleware
export const useUserStore = create(
  devtools(
    persist(
      subscribeWithSelector(
        immer((set, get) => ({
          users: [],
          currentUser: null,
          loading: false,

          // Using immer for immutable updates
          addUser: (user) =>
            set((state) => {
              state.users.push(user);
            }),

          updateUser: (id, updates) =>
            set((state) => {
              const userIndex = state.users.findIndex((u) => u.id === id);
              if (userIndex !== -1) {
                Object.assign(state.users[userIndex], updates);
              }
            }),

          setCurrentUser: (user) => set({ currentUser: user }),

          loadUsers: async () => {
            set({ loading: true });
            try {
              const response = await fetch("/api/users");
              const users = await response.json();
              set({ users, loading: false });
            } catch (error) {
              set({ loading: false });
              throw error;
            }
          },
        }))
      ),
      {
        name: "user-storage",
        storage: createJSONStorage(() => localStorage),
        partialize: (state) => ({
          currentUser: state.currentUser,
          users: state.users,
        }),
      }
    ),
    {
      name: "user-store",
    }
  )
);
```

**2. Custom Zustand Middleware:**

```javascript
// Custom logging middleware for Zustand
const logger = (config) => (set, get, api) =>
  config(
    (...args) => {
      console.log("Previous state:", get());
      set(...args);
      console.log("New state:", get());
    },
    get,
    api
  );

// Custom API middleware
const apiMiddleware = (config) => (set, get, api) => {
  const store = config(set, get, api);

  return {
    ...store,
    apiCall: async (endpoint, options = {}) => {
      set({ loading: true, error: null });

      try {
        const response = await fetch(endpoint, {
          headers: { "Content-Type": "application/json" },
          ...options,
        });

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        set({ loading: false });
        return data;
      } catch (error) {
        set({ loading: false, error: error.message });
        throw error;
      }
    },
  };
};

// Usage with custom middleware
export const useApiStore = create(
  logger(
    apiMiddleware((set, get) => ({
      data: null,
      loading: false,
      error: null,

      fetchData: async (endpoint) => {
        try {
          const data = await get().apiCall(endpoint);
          set({ data });
        } catch (error) {
          console.error("Failed to fetch data:", error);
        }
      },

      reset: () => set({ data: null, error: null }),
    }))
  )
);
```

**3. Middleware for State Synchronization:**

```javascript
// Sync middleware to keep stores in sync
const createSyncMiddleware = (stores) => (config) => (set, get, api) => {
  const store = config(set, get, api);

  // Subscribe to changes and sync with other stores
  api.subscribe((state, prevState) => {
    stores.forEach((otherStore) => {
      if (otherStore !== api) {
        // Sync specific state properties
        if (state.currentUser !== prevState.currentUser) {
          otherStore.getState().setCurrentUser?.(state.currentUser);
        }
      }
    });
  });

  return store;
};

// Usage
const stores = [];

export const useAuthStore = create(
  createSyncMiddleware(stores)((set) => ({
    currentUser: null,
    setCurrentUser: (user) => set({ currentUser: user }),
  }))
);

stores.push(useAuthStore);
```

**Key Differences:**

1. **Redux**: Middleware intercepts actions before they reach reducers
2. **Zustand**: Middleware wraps the store creation and can intercept state changes
3. **Redux**: More complex setup but powerful ecosystem
4. **Zustand**: Simpler API with built-in common middleware
5. **Redux**: Middleware runs in a specific order
6. **Zustand**: Middleware composition is more flexible

Both approaches provide powerful ways to extend functionality, with Redux offering more standardized patterns and Zustand providing more flexibility and simplicity.

---

### Q15: How do you handle complex state patterns and normalization in Redux vs Zustand?

**Answer:**
Both Redux and Zustand can handle complex state patterns, but they approach normalization and complex state management differently.

**Redux State Normalization:**

**1. Normalized State Structure:**

```javascript
// Normalized Redux state
const initialState = {
  users: {
    byId: {},
    allIds: [],
  },
  posts: {
    byId: {},
    allIds: [],
  },
  comments: {
    byId: {},
    allIds: [],
  },
  ui: {
    loading: false,
    selectedUserId: null,
    filters: {
      status: "all",
      category: "all",
    },
  },
};

// Selectors for denormalized data
import { createSelector } from "@reduxjs/toolkit";

const selectUsers = (state) => state.users;
const selectPosts = (state) => state.posts;
const selectComments = (state) => state.comments;

export const selectAllUsers = createSelector([selectUsers], (users) =>
  users.allIds.map((id) => users.byId[id])
);

export const selectUserById = createSelector(
  [selectUsers, (state, userId) => userId],
  (users, userId) => users.byId[userId]
);

export const selectPostsWithAuthors = createSelector(
  [selectPosts, selectUsers],
  (posts, users) => {
    return posts.allIds.map((postId) => {
      const post = posts.byId[postId];
      return {
        ...post,
        author: users.byId[post.authorId],
      };
    });
  }
);

export const selectPostsWithCommentsAndAuthors = createSelector(
  [selectPosts, selectComments, selectUsers],
  (posts, comments, users) => {
    return posts.allIds.map((postId) => {
      const post = posts.byId[postId];
      const postComments = comments.allIds
        .filter((commentId) => comments.byId[commentId].postId === postId)
        .map((commentId) => ({
          ...comments.byId[commentId],
          author: users.byId[comments.byId[commentId].authorId],
        }));

      return {
        ...post,
        author: users.byId[post.authorId],
        comments: postComments,
      };
    });
  }
);
```

**2. Redux Toolkit Entity Adapter:**

```javascript
import { createEntityAdapter, createSlice } from "@reduxjs/toolkit";

// Users entity adapter
const usersAdapter = createEntityAdapter({
  selectId: (user) => user.id,
  sortComparer: (a, b) => a.name.localeCompare(b.name),
});

const usersSlice = createSlice({
  name: "users",
  initialState: usersAdapter.getInitialState({
    loading: false,
    error: null,
  }),
  reducers: {
    addUser: usersAdapter.addOne,
    addUsers: usersAdapter.addMany,
    updateUser: usersAdapter.updateOne,
    removeUser: usersAdapter.removeOne,
    setUsers: usersAdapter.setAll,
  },
});

// Export selectors
export const {
  selectAll: selectAllUsers,
  selectById: selectUserById,
  selectIds: selectUserIds,
} = usersAdapter.getSelectors((state) => state.users);

// Posts with relationships
const postsAdapter = createEntityAdapter({
  sortComparer: (a, b) => b.createdAt.localeCompare(a.createdAt),
});

const postsSlice = createSlice({
  name: "posts",
  initialState: postsAdapter.getInitialState(),
  reducers: {
    addPost: postsAdapter.addOne,
    updatePost: postsAdapter.updateOne,
    removePost: postsAdapter.removeOne,
    setPosts: postsAdapter.setAll,
  },
});

export const { selectAll: selectAllPosts, selectById: selectPostById } =
  postsAdapter.getSelectors((state) => state.posts);
```

**Zustand Complex State Patterns:**

**1. Nested State with Immer:**

```javascript
import { create } from "zustand";
import { immer } from "zustand/middleware/immer";
import { subscribeWithSelector } from "zustand/middleware";

export const useAppStore = create(
  subscribeWithSelector(
    immer((set, get) => ({
      // Normalized-like structure in Zustand
      entities: {
        users: new Map(),
        posts: new Map(),
        comments: new Map(),
      },

      ui: {
        loading: false,
        selectedUserId: null,
        filters: {
          status: "all",
          category: "all",
        },
      },

      // Actions for users
      addUser: (user) =>
        set((state) => {
          state.entities.users.set(user.id, user);
        }),

      updateUser: (id, updates) =>
        set((state) => {
          const user = state.entities.users.get(id);
          if (user) {
            Object.assign(user, updates);
          }
        }),

      removeUser: (id) =>
        set((state) => {
          state.entities.users.delete(id);
          // Remove related posts and comments
          for (const [postId, post] of state.entities.posts) {
            if (post.authorId === id) {
              state.entities.posts.delete(postId);
            }
          }
          for (const [commentId, comment] of state.entities.comments) {
            if (comment.authorId === id) {
              state.entities.comments.delete(commentId);
            }
          }
        }),

      // Actions for posts
      addPost: (post) =>
        set((state) => {
          state.entities.posts.set(post.id, {
            ...post,
            createdAt: new Date().toISOString(),
          });
        }),

      updatePost: (id, updates) =>
        set((state) => {
          const post = state.entities.posts.get(id);
          if (post) {
            Object.assign(post, updates);
          }
        }),

      // Complex derived state getters
      getAllUsers: () => {
        return Array.from(get().entities.users.values()).sort((a, b) =>
          a.name.localeCompare(b.name)
        );
      },

      getUserById: (id) => {
        return get().entities.users.get(id);
      },

      getPostsWithAuthors: () => {
        const { entities } = get();
        return Array.from(entities.posts.values())
          .map((post) => ({
            ...post,
            author: entities.users.get(post.authorId),
          }))
          .sort((a, b) => b.createdAt.localeCompare(a.createdAt));
      },

      getPostsWithCommentsAndAuthors: () => {
        const { entities } = get();
        return Array.from(entities.posts.values()).map((post) => {
          const comments = Array.from(entities.comments.values())
            .filter((comment) => comment.postId === post.id)
            .map((comment) => ({
              ...comment,
              author: entities.users.get(comment.authorId),
            }));

          return {
            ...post,
            author: entities.users.get(post.authorId),
            comments,
          };
        });
      },

      // UI actions
      setLoading: (loading) =>
        set((state) => {
          state.ui.loading = loading;
        }),

      setSelectedUser: (userId) =>
        set((state) => {
          state.ui.selectedUserId = userId;
        }),

      updateFilters: (filters) =>
        set((state) => {
          Object.assign(state.ui.filters, filters);
        }),
    }))
  )
);
```

**2. Zustand with Slices Pattern:**

```javascript
// Separate slices for different domains
const createUserSlice = (set, get) => ({
  users: new Map(),

  addUser: (user) =>
    set((state) => {
      state.users.set(user.id, user);
    }),

  updateUser: (id, updates) =>
    set((state) => {
      const user = state.users.get(id);
      if (user) Object.assign(user, updates);
    }),

  getUserById: (id) => get().users.get(id),
  getAllUsers: () => Array.from(get().users.values()),
});

const createPostSlice = (set, get) => ({
  posts: new Map(),

  addPost: (post) =>
    set((state) => {
      state.posts.set(post.id, post);
    }),

  getPostsWithAuthors: () => {
    const posts = Array.from(get().posts.values());
    const users = get().users;
    return posts.map((post) => ({
      ...post,
      author: users.get(post.authorId),
    }));
  },
});

const createUISlice = (set, get) => ({
  ui: {
    loading: false,
    selectedUserId: null,
    filters: { status: "all" },
  },

  setLoading: (loading) =>
    set((state) => {
      state.ui.loading = loading;
    }),

  updateFilters: (filters) =>
    set((state) => {
      Object.assign(state.ui.filters, filters);
    }),
});

// Combine slices
export const useAppStore = create(
  immer((set, get) => ({
    ...createUserSlice(set, get),
    ...createPostSlice(set, get),
    ...createUISlice(set, get),
  }))
);
```

**Performance Considerations:**

**Redux:**

- Use `createSelector` for memoized derived state
- Entity adapters provide optimized CRUD operations
- Normalized state prevents deep nesting issues
- Selectors prevent unnecessary re-renders

**Zustand:**

- Use `subscribeWithSelector` for granular subscriptions
- Getter functions for computed state
- Map/Set for efficient lookups
- Selective subscriptions to prevent unnecessary updates

**Usage in Components:**

```javascript
// Redux usage
const PostList = () => {
  const posts = useSelector(selectPostsWithAuthors);
  const loading = useSelector((state) => state.ui.loading);

  return (
    <div>
      {loading
        ? "Loading..."
        : posts.map((post) => <PostItem key={post.id} post={post} />)}
    </div>
  );
};

// Zustand usage with selective subscription
const PostList = () => {
  const posts = useAppStore((state) => state.getPostsWithAuthors());
  const loading = useAppStore((state) => state.ui.loading);

  return (
    <div>
      {loading
        ? "Loading..."
        : posts.map((post) => <PostItem key={post.id} post={post} />)}
    </div>
  );
};
```

Both approaches can handle complex state effectively, with Redux providing more structured patterns and Zustand offering more flexibility in implementation.

---

### Q16: How do you migrate from Redux to Zustand or vice versa?

**Answer:**
Migrating between Redux and Zustand requires careful planning and can be done incrementally to minimize disruption.

**Migrating from Redux to Zustand:**

**1. Gradual Migration Strategy:**

```javascript
// Step 1: Create Zustand stores alongside Redux
// Original Redux store
const reduxUserSlice = createSlice({
  name: "users",
  initialState: { users: [], loading: false },
  reducers: {
    setUsers: (state, action) => {
      state.users = action.payload;
    },
    setLoading: (state, action) => {
      state.loading = action.payload;
    },
  },
});

// New Zustand store (parallel implementation)
import { create } from "zustand";

export const useUserStore = create((set, get) => ({
  users: [],
  loading: false,

  setUsers: (users) => set({ users }),
  setLoading: (loading) => set({ loading }),

  // Enhanced functionality in Zustand
  addUser: (user) =>
    set((state) => ({
      users: [...state.users, user],
    })),

  updateUser: (id, updates) =>
    set((state) => ({
      users: state.users.map((user) =>
        user.id === id ? { ...user, ...updates } : user
      ),
    })),

  // Async actions (simpler than Redux thunks)
  fetchUsers: async () => {
    set({ loading: true });
    try {
      const response = await fetch("/api/users");
      const users = await response.json();
      set({ users, loading: false });
    } catch (error) {
      set({ loading: false });
      throw error;
    }
  },
}));
```

**2. Component Migration:**

```javascript
// Original Redux component
import { useSelector, useDispatch } from "react-redux";
import { setUsers, setLoading } from "./userSlice";

const UserListRedux = () => {
  const { users, loading } = useSelector((state) => state.users);
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(setLoading(true));
    fetchUsersAPI().then((users) => {
      dispatch(setUsers(users));
      dispatch(setLoading(false));
    });
  }, [dispatch]);

  return (
    <div>
      {loading
        ? "Loading..."
        : users.map((user) => <div key={user.id}>{user.name}</div>)}
    </div>
  );
};

// Migrated Zustand component
import { useUserStore } from "./userStore";

const UserListZustand = () => {
  const { users, loading, fetchUsers } = useUserStore();

  useEffect(() => {
    fetchUsers();
  }, [fetchUsers]);

  return (
    <div>
      {loading
        ? "Loading..."
        : users.map((user) => <div key={user.id}>{user.name}</div>)}
    </div>
  );
};
```

**3. State Synchronization During Migration:**

```javascript
// Bridge component to sync Redux and Zustand during migration
import { useEffect } from "react";
import { useSelector } from "react-redux";
import { useUserStore } from "./userStore";

export const ReduxZustandBridge = () => {
  const reduxUsers = useSelector((state) => state.users.users);
  const reduxLoading = useSelector((state) => state.users.loading);
  const { setUsers, setLoading } = useUserStore();

  // Sync Redux state to Zustand
  useEffect(() => {
    setUsers(reduxUsers);
  }, [reduxUsers, setUsers]);

  useEffect(() => {
    setLoading(reduxLoading);
  }, [reduxLoading, setLoading]);

  return null; // This component only handles synchronization
};

// Usage in App component during migration
const App = () => {
  return (
    <Provider store={reduxStore}>
      <ReduxZustandBridge />
      <UserListZustand /> {/* Using Zustand */}
      <OtherReduxComponent /> {/* Still using Redux */}
    </Provider>
  );
};
```

**Migrating from Zustand to Redux:**

**1. Converting Zustand Store to Redux:**

```javascript
// Original Zustand store
const useUserStore = create((set, get) => ({
  users: [],
  loading: false,

  addUser: (user) =>
    set((state) => ({
      users: [...state.users, user],
    })),

  updateUser: (id, updates) =>
    set((state) => ({
      users: state.users.map((user) =>
        user.id === id ? { ...user, ...updates } : user
      ),
    })),

  fetchUsers: async () => {
    set({ loading: true });
    try {
      const response = await fetch("/api/users");
      const users = await response.json();
      set({ users, loading: false });
    } catch (error) {
      set({ loading: false });
      throw error;
    }
  },
}));

// Converted to Redux Toolkit
import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";

// Async thunk for fetching users
export const fetchUsers = createAsyncThunk("users/fetchUsers", async () => {
  const response = await fetch("/api/users");
  return response.json();
});

const userSlice = createSlice({
  name: "users",
  initialState: {
    users: [],
    loading: false,
    error: null,
  },
  reducers: {
    addUser: (state, action) => {
      state.users.push(action.payload);
    },
    updateUser: (state, action) => {
      const { id, updates } = action.payload;
      const userIndex = state.users.findIndex((user) => user.id === id);
      if (userIndex !== -1) {
        Object.assign(state.users[userIndex], updates);
      }
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchUsers.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchUsers.fulfilled, (state, action) => {
        state.loading = false;
        state.users = action.payload;
      })
      .addCase(fetchUsers.rejected, (state, action) => {
        state.loading = false;
        state.error = action.error.message;
      });
  },
});

export const { addUser, updateUser } = userSlice.actions;
export default userSlice.reducer;
```

**2. Component Migration from Zustand to Redux:**

```javascript
// Original Zustand component
const UserListZustand = () => {
  const { users, loading, addUser, updateUser, fetchUsers } = useUserStore();

  useEffect(() => {
    fetchUsers();
  }, [fetchUsers]);

  const handleAddUser = () => {
    addUser({ id: Date.now(), name: "New User" });
  };

  return (
    <div>
      {loading
        ? "Loading..."
        : users.map((user) => (
            <div key={user.id}>
              {user.name}
              <button onClick={() => updateUser(user.id, { name: "Updated" })}>
                Update
              </button>
            </div>
          ))}
      <button onClick={handleAddUser}>Add User</button>
    </div>
  );
};

// Migrated Redux component
import { useSelector, useDispatch } from "react-redux";
import { addUser, updateUser, fetchUsers } from "./userSlice";

const UserListRedux = () => {
  const { users, loading, error } = useSelector((state) => state.users);
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(fetchUsers());
  }, [dispatch]);

  const handleAddUser = () => {
    dispatch(addUser({ id: Date.now(), name: "New User" }));
  };

  const handleUpdateUser = (id) => {
    dispatch(updateUser({ id, updates: { name: "Updated" } }));
  };

  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      {loading
        ? "Loading..."
        : users.map((user) => (
            <div key={user.id}>
              {user.name}
              <button onClick={() => handleUpdateUser(user.id)}>Update</button>
            </div>
          ))}
      <button onClick={handleAddUser}>Add User</button>
    </div>
  );
};
```

**Migration Best Practices:**

1. **Incremental Migration**: Migrate one feature/component at a time
2. **Maintain Parallel Implementations**: Run both systems during transition
3. **State Synchronization**: Use bridge components to sync state
4. **Testing**: Ensure functionality remains consistent
5. **Team Training**: Educate team on new patterns and conventions
6. **Documentation**: Update documentation and coding standards
7. **Performance Monitoring**: Monitor performance during and after migration

**Migration Checklist:**

- [ ] Identify migration scope and priorities
- [ ] Set up new state management alongside existing
- [ ] Create bridge components for state synchronization
- [ ] Migrate components incrementally
- [ ] Update tests and documentation
- [ ] Remove old state management code
- [ ] Performance testing and optimization
- [ ] Team training and knowledge transfer

---

### Q17: How do you optimize performance in Redux and Zustand applications?

**Answer:**
Performance optimization in state management involves preventing unnecessary re-renders, optimizing selectors, and managing subscriptions efficiently.

**Redux Performance Optimization:**

**1. Memoized Selectors:**

```javascript
import { createSelector } from "@reduxjs/toolkit";

// Basic selectors
const selectUsers = (state) => state.users.items;
const selectFilters = (state) => state.users.filters;
const selectSearchTerm = (state) => state.users.searchTerm;

// Memoized selector to prevent unnecessary recalculations
export const selectFilteredUsers = createSelector(
  [selectUsers, selectFilters, selectSearchTerm],
  (users, filters, searchTerm) => {
    console.log("Filtering users..."); // This will only log when inputs change

    return users.filter((user) => {
      const matchesSearch = user.name
        .toLowerCase()
        .includes(searchTerm.toLowerCase());
      const matchesStatus =
        filters.status === "all" || user.status === filters.status;
      const matchesRole = filters.role === "all" || user.role === filters.role;

      return matchesSearch && matchesStatus && matchesRole;
    });
  }
);

// Parameterized selectors
export const selectUserById = createSelector(
  [selectUsers, (state, userId) => userId],
  (users, userId) => users.find((user) => user.id === userId)
);

// Complex derived state
export const selectUserStats = createSelector([selectUsers], (users) => ({
  total: users.length,
  active: users.filter((u) => u.status === "active").length,
  inactive: users.filter((u) => u.status === "inactive").length,
  byRole: users.reduce((acc, user) => {
    acc[user.role] = (acc[user.role] || 0) + 1;
    return acc;
  }, {}),
}));
```

**2. Component Optimization:**

```javascript
import React, { memo, useMemo } from "react";
import { useSelector, shallowEqual } from "react-redux";

// Optimized component with shallow equality check
const UserList = memo(() => {
  // Use shallowEqual to prevent unnecessary re-renders
  const { users, loading } = useSelector(
    (state) => ({
      users: selectFilteredUsers(state),
      loading: state.users.loading,
    }),
    shallowEqual
  );

  // Memoize expensive calculations
  const userStats = useMemo(() => {
    return users.reduce((stats, user) => {
      stats[user.role] = (stats[user.role] || 0) + 1;
      return stats;
    }, {});
  }, [users]);

  if (loading) return <div>Loading...</div>;

  return (
    <div>
      <div>Stats: {JSON.stringify(userStats)}</div>
      {users.map((user) => (
        <UserItem key={user.id} user={user} />
      ))}
    </div>
  );
});

// Optimized individual item component
const UserItem = memo(({ user }) => {
  const handleClick = useCallback(() => {
    // Handle user click
  }, [user.id]);

  return (
    <div onClick={handleClick}>
      {user.name} - {user.role}
    </div>
  );
});
```

**3. Redux Toolkit Query Optimization:**

```javascript
import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const usersApi = createApi({
  reducerPath: "usersApi",
  baseQuery: fetchBaseQuery({ baseUrl: "/api/" }),
  tagTypes: ["User"],
  endpoints: (builder) => ({
    getUsers: builder.query({
      query: (filters) => ({
        url: "users",
        params: filters,
      }),
      providesTags: ["User"],
      // Cache for 60 seconds
      keepUnusedDataFor: 60,
      // Transform response to normalize data
      transformResponse: (response) => {
        return response.users.map((user) => ({
          ...user,
          fullName: `${user.firstName} ${user.lastName}`,
        }));
      },
    }),

    getUserById: builder.query({
      query: (id) => `users/${id}`,
      providesTags: (result, error, id) => [{ type: "User", id }],
    }),
  }),
});

export const { useGetUsersQuery, useGetUserByIdQuery } = usersApi;
```

**Zustand Performance Optimization:**

**1. Selective Subscriptions:**

```javascript
import { create } from "zustand";
import { subscribeWithSelector } from "zustand/middleware";

export const useAppStore = create(
  subscribeWithSelector((set, get) => ({
    users: [],
    filters: { status: "all", role: "all" },
    searchTerm: "",
    loading: false,

    setUsers: (users) => set({ users }),
    setFilters: (filters) => set({ filters }),
    setSearchTerm: (searchTerm) => set({ searchTerm }),
    setLoading: (loading) => set({ loading }),

    // Computed getters (not reactive)
    getFilteredUsers: () => {
      const { users, filters, searchTerm } = get();
      return users.filter((user) => {
        const matchesSearch = user.name
          .toLowerCase()
          .includes(searchTerm.toLowerCase());
        const matchesStatus =
          filters.status === "all" || user.status === filters.status;
        const matchesRole =
          filters.role === "all" || user.role === filters.role;
        return matchesSearch && matchesStatus && matchesRole;
      });
    },

    getUserById: (id) => {
      return get().users.find((user) => user.id === id);
    },
  }))
);

// Optimized component with selective subscriptions
const UserList = () => {
  // Only subscribe to specific parts of the state
  const users = useAppStore((state) => state.getFilteredUsers());
  const loading = useAppStore((state) => state.loading);

  // Memoize the filtered users to prevent recalculation
  const memoizedUsers = useMemo(() => users, [users]);

  if (loading) return <div>Loading...</div>;

  return (
    <div>
      {memoizedUsers.map((user) => (
        <UserItem key={user.id} userId={user.id} />
      ))}
    </div>
  );
};

// Component that only subscribes to specific user
const UserItem = memo(({ userId }) => {
  const user = useAppStore((state) => state.getUserById(userId));

  return (
    <div>
      {user?.name} - {user?.role}
    </div>
  );
});
```

**2. Computed State with Subscriptions:**

```javascript
import { create } from "zustand";
import { subscribeWithSelector } from "zustand/middleware";

export const useOptimizedStore = create(
  subscribeWithSelector((set, get) => ({
    users: [],
    filters: { status: "all" },

    // Cached computed state
    _filteredUsers: [],
    _userStats: { total: 0, active: 0 },

    setUsers: (users) => {
      set({ users });
      // Trigger recomputation
      get()._recomputeFilteredUsers();
      get()._recomputeStats();
    },

    setFilters: (filters) => {
      set({ filters });
      get()._recomputeFilteredUsers();
    },

    _recomputeFilteredUsers: () => {
      const { users, filters } = get();
      const filtered = users.filter(
        (user) => filters.status === "all" || user.status === filters.status
      );
      set({ _filteredUsers: filtered });
    },

    _recomputeStats: () => {
      const { users } = get();
      const stats = {
        total: users.length,
        active: users.filter((u) => u.status === "active").length,
      };
      set({ _userStats: stats });
    },

    // Getters for cached computed state
    getFilteredUsers: () => get()._filteredUsers,
    getUserStats: () => get()._userStats,
  }))
);

// Usage with cached computed state
const OptimizedUserList = () => {
  const filteredUsers = useOptimizedStore((state) => state._filteredUsers);
  const stats = useOptimizedStore((state) => state._userStats);

  return (
    <div>
      <div>
        Total: {stats.total}, Active: {stats.active}
      </div>
      {filteredUsers.map((user) => (
        <div key={user.id}>{user.name}</div>
      ))}
    </div>
  );
};
```

**3. External Store Pattern for Heavy Computations:**

```javascript
import { useSyncExternalStore } from "react";

class UserStoreManager {
  constructor() {
    this.users = [];
    this.filters = { status: "all" };
    this.listeners = new Set();
    this._filteredUsers = [];
  }

  subscribe = (listener) => {
    this.listeners.add(listener);
    return () => this.listeners.delete(listener);
  };

  getSnapshot = () => {
    return {
      users: this.users,
      filteredUsers: this._filteredUsers,
      filters: this.filters,
    };
  };

  setUsers = (users) => {
    this.users = users;
    this._recomputeFilteredUsers();
    this._notify();
  };

  setFilters = (filters) => {
    this.filters = filters;
    this._recomputeFilteredUsers();
    this._notify();
  };

  _recomputeFilteredUsers = () => {
    this._filteredUsers = this.users.filter(
      (user) =>
        this.filters.status === "all" || user.status === this.filters.status
    );
  };

  _notify = () => {
    this.listeners.forEach((listener) => listener());
  };
}

const userStoreManager = new UserStoreManager();

// Hook to use the external store
const useUserStoreManager = () => {
  return useSyncExternalStore(
    userStoreManager.subscribe,
    userStoreManager.getSnapshot
  );
};

// Component using external store
const ExternalStoreUserList = () => {
  const { filteredUsers } = useUserStoreManager();

  return (
    <div>
      {filteredUsers.map((user) => (
        <div key={user.id}>{user.name}</div>
      ))}
    </div>
  );
};
```

**Performance Best Practices:**

**Redux:**

1. Use `createSelector` for memoized derived state
2. Implement `shallowEqual` for object comparisons
3. Normalize state structure to avoid deep nesting
4. Use RTK Query for efficient data fetching and caching
5. Split large reducers into smaller, focused ones

**Zustand:**

1. Use selective subscriptions to minimize re-renders
2. Implement computed getters for derived state
3. Use `subscribeWithSelector` for granular updates
4. Cache expensive computations in the store
5. Consider external stores for heavy computational logic

**Common Optimizations:**

1. Memoize components with `React.memo`
2. Use `useMemo` and `useCallback` appropriately
3. Implement virtualization for large lists
4. Debounce frequent state updates
5. Profile and measure performance regularly

---

### Q18: How do you implement TypeScript with Redux and Zustand?

**Answer:**
Both Redux and Zustand provide excellent TypeScript support, but with different approaches to type safety and inference.

**Redux with TypeScript:**

**1. Redux Toolkit with TypeScript:**

```typescript
import { createSlice, PayloadAction, configureStore } from "@reduxjs/toolkit";

// Define types for state
interface User {
  id: string;
  name: string;
  email: string;
  role: "admin" | "user" | "moderator";
  status: "active" | "inactive";
}

interface UserState {
  users: User[];
  loading: boolean;
  error: string | null;
  selectedUserId: string | null;
}

// Initial state with proper typing
const initialState: UserState = {
  users: [],
  loading: false,
  error: null,
  selectedUserId: null,
};

// Create slice with typed actions
const userSlice = createSlice({
  name: "users",
  initialState,
  reducers: {
    setLoading: (state, action: PayloadAction<boolean>) => {
      state.loading = action.payload;
    },
    setError: (state, action: PayloadAction<string | null>) => {
      state.error = action.payload;
    },
    setUsers: (state, action: PayloadAction<User[]>) => {
      state.users = action.payload;
    },
    addUser: (state, action: PayloadAction<User>) => {
      state.users.push(action.payload);
    },
    updateUser: (
      state,
      action: PayloadAction<{ id: string; updates: Partial<User> }>
    ) => {
      const { id, updates } = action.payload;
      const userIndex = state.users.findIndex((user) => user.id === id);
      if (userIndex !== -1) {
        Object.assign(state.users[userIndex], updates);
      }
    },
    removeUser: (state, action: PayloadAction<string>) => {
      state.users = state.users.filter((user) => user.id !== action.payload);
    },
    setSelectedUser: (state, action: PayloadAction<string | null>) => {
      state.selectedUserId = action.payload;
    },
  },
});

export const {
  setLoading,
  setError,
  setUsers,
  addUser,
  updateUser,
  removeUser,
  setSelectedUser,
} = userSlice.actions;

export default userSlice.reducer;

// Store configuration with proper typing
export const store = configureStore({
  reducer: {
    users: userSlice.reducer,
  },
});

// Infer types from store
export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
```

**2. Typed Hooks:**

```typescript
import { TypedUseSelectorHook, useDispatch, useSelector } from "react-redux";
import type { RootState, AppDispatch } from "./store";

// Typed hooks for better developer experience
export const useAppDispatch = () => useDispatch<AppDispatch>();
export const useAppSelector: TypedUseSelectorHook<RootState> = useSelector;

// Typed selectors
import { createSelector } from "@reduxjs/toolkit";

const selectUserState = (state: RootState) => state.users;

export const selectAllUsers = createSelector(
  [selectUserState],
  (userState) => userState.users
);

export const selectUserById = createSelector(
  [selectAllUsers, (state: RootState, userId: string) => userId],
  (users, userId) => users.find((user) => user.id === userId)
);

export const selectUsersByRole = createSelector(
  [selectAllUsers, (state: RootState, role: User["role"]) => role],
  (users, role) => users.filter((user) => user.role === role)
);

export const selectActiveUsers = createSelector([selectAllUsers], (users) =>
  users.filter((user) => user.status === "active")
);
```

**3. Async Thunks with TypeScript:**

```typescript
import { createAsyncThunk } from "@reduxjs/toolkit";

// API response types
interface ApiResponse<T> {
  data: T;
  message: string;
  success: boolean;
}

interface CreateUserRequest {
  name: string;
  email: string;
  role: User["role"];
}

// Typed async thunks
export const fetchUsers = createAsyncThunk<
  User[], // Return type
  void, // Argument type
  { rejectValue: string } // ThunkAPI config
>("users/fetchUsers", async (_, { rejectWithValue }) => {
  try {
    const response = await fetch("/api/users");
    if (!response.ok) {
      throw new Error("Failed to fetch users");
    }
    const result: ApiResponse<User[]> = await response.json();
    return result.data;
  } catch (error) {
    return rejectWithValue(
      error instanceof Error ? error.message : "Unknown error"
    );
  }
});

export const createUser = createAsyncThunk<
  User,
  CreateUserRequest,
  { rejectValue: string }
>("users/createUser", async (userData, { rejectWithValue }) => {
  try {
    const response = await fetch("/api/users", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(userData),
    });

    if (!response.ok) {
      throw new Error("Failed to create user");
    }

    const result: ApiResponse<User> = await response.json();
    return result.data;
  } catch (error) {
    return rejectWithValue(
      error instanceof Error ? error.message : "Unknown error"
    );
  }
});

// Add extra reducers to handle async actions
const userSliceWithAsync = createSlice({
  name: "users",
  initialState,
  reducers: {
    // ... existing reducers
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchUsers.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchUsers.fulfilled, (state, action) => {
        state.loading = false;
        state.users = action.payload;
      })
      .addCase(fetchUsers.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload || "Failed to fetch users";
      })
      .addCase(createUser.fulfilled, (state, action) => {
        state.users.push(action.payload);
      });
  },
});
```

**Zustand with TypeScript:**

**1. Basic Zustand Store with TypeScript:**

```typescript
import { create } from 'zustand';
import { devtools, persist } from 'zustand/middleware';
import { immer } from 'zustand/middleware/immer';

// Define the store state interface
interface UserState {
  users: User[];
  loading: boolean;
  error: string | null;
  selectedUserId: string | null;
}

// Define the store actions interface
interface UserActions {
  setLoading: (loading: boolean) => void;
  setError: (error: string | null) => void;
  setUsers: (users: User[]) => void;
  addUser: (user: User) => void;
  updateUser: (id: string, updates: Partial<User>) => void;
  removeUser: (id: string) => void;
  setSelectedUser: (userId: string | null) => void;
  fetchUsers: () => Promise<void>;
  createUser: (userData: CreateUserRequest) => Promise<User>;
  getUserById: (id: string) => User | undefined;
  getUsersByRole: (role: User['role']) => User[];
  getActiveUsers: () => User[];
  reset: () => void;
}

// Combine state and actions
type UserStore = UserState & UserActions;

// Create the store with full type safety
export const useUserStore = create<UserStore>()()
  devtools(
    persist(
      immer((set, get) => ({
        // Initial state
        users: [],
        loading: false,
        error: null,
        selectedUserId: null,

        // Actions
        setLoading: (loading) => set((state) => {
          state.loading = loading;
        }),

        setError: (error) => set((state) => {
          state.error = error;
        }),

        setUsers: (users) => set((state) => {
          state.users = users;
        }),

        addUser: (user) => set((state) => {
          state.users.push(user);
        }),

        updateUser: (id, updates) => set((state) => {
          const userIndex = state.users.findIndex(user => user.id === id);
          if (userIndex !== -1) {
            Object.assign(state.users[userIndex], updates);
          }
        }),

        removeUser: (id) => set((state) => {
          state.users = state.users.filter(user => user.id !== id);
        }),

        setSelectedUser: (userId) => set((state) => {
          state.selectedUserId = userId;
        }),

        // Async actions
        fetchUsers: async () => {
          set((state) => {
            state.loading = true;
            state.error = null;
          });

          try {
            const response = await fetch('/api/users');
            if (!response.ok) {
              throw new Error('Failed to fetch users');
            }
            const result: ApiResponse<User[]> = await response.json();

            set((state) => {
              state.users = result.data;
              state.loading = false;
            });
          } catch (error) {
            set((state) => {
              state.loading = false;
              state.error = error instanceof Error ? error.message : 'Unknown error';
            });
          }
        },

        createUser: async (userData) => {
          const response = await fetch('/api/users', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(userData)
          });

          if (!response.ok) {
            throw new Error('Failed to create user');
          }

          const result: ApiResponse<User> = await response.json();

          set((state) => {
            state.users.push(result.data);
          });

          return result.data;
        },

        // Computed getters
        getUserById: (id) => {
          return get().users.find(user => user.id === id);
        },

        getUsersByRole: (role) => {
          return get().users.filter(user => user.role === role);
        },

        getActiveUsers: () => {
          return get().users.filter(user => user.status === 'active');
        },

        reset: () => set((state) => {
          state.users = [];
          state.loading = false;
          state.error = null;
          state.selectedUserId = null;
        })
      })),
      {
        name: 'user-store',
        partialize: (state) => ({
          users: state.users,
          selectedUserId: state.selectedUserId
        })
      }
    ),
    { name: 'user-store' }
  )
);
```

**2. Zustand with Slices Pattern:**

```typescript
// Define slice interfaces
interface UserSlice {
  users: User[];
  addUser: (user: User) => void;
  updateUser: (id: string, updates: Partial<User>) => void;
  removeUser: (id: string) => void;
  getUserById: (id: string) => User | undefined;
}

interface UISlice {
  loading: boolean;
  error: string | null;
  selectedUserId: string | null;
  setLoading: (loading: boolean) => void;
  setError: (error: string | null) => void;
  setSelectedUser: (userId: string | null) => void;
}

// Create slice creators
const createUserSlice = (set: any, get: any): UserSlice => ({
  users: [],

  addUser: (user) => set((state: any) => {
    state.users.push(user);
  }),

  updateUser: (id, updates) => set((state: any) => {
    const userIndex = state.users.findIndex((user: User) => user.id === id);
    if (userIndex !== -1) {
      Object.assign(state.users[userIndex], updates);
    }
  }),

  removeUser: (id) => set((state: any) => {
    state.users = state.users.filter((user: User) => user.id !== id);
  }),

  getUserById: (id) => {
    return get().users.find((user: User) => user.id === id);
  }
});

const createUISlice = (set: any, get: any): UISlice => ({
  loading: false,
  error: null,
  selectedUserId: null,

  setLoading: (loading) => set((state: any) => {
    state.loading = loading;
  }),

  setError: (error) => set((state: any) => {
    state.error = error;
  }),

  setSelectedUser: (userId) => set((state: any) => {
    state.selectedUserId = userId;
  })
});

// Combine slices
type StoreState = UserSlice & UISlice;

export const useAppStore = create<StoreState>()()
  immer((set, get) => ({
    ...createUserSlice(set, get),
    ...createUISlice(set, get)
  }))
);
```

**3. Component Usage with TypeScript:**

```typescript
import React, { useEffect } from "react";
import { useUserStore } from "./store";

// Redux component
const ReduxUserList: React.FC = () => {
  const users = useAppSelector(selectAllUsers);
  const loading = useAppSelector((state) => state.users.loading);
  const error = useAppSelector((state) => state.users.error);
  const dispatch = useAppDispatch();

  useEffect(() => {
    dispatch(fetchUsers());
  }, [dispatch]);

  const handleCreateUser = async () => {
    try {
      await dispatch(
        createUser({
          name: "New User",
          email: "user@example.com",
          role: "user",
        })
      ).unwrap();
    } catch (error) {
      console.error("Failed to create user:", error);
    }
  };

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      {users.map((user) => (
        <div key={user.id}>
          {user.name} - {user.role}
        </div>
      ))}
      <button onClick={handleCreateUser}>Add User</button>
    </div>
  );
};

// Zustand component
const ZustandUserList: React.FC = () => {
  const { users, loading, error, fetchUsers, createUser } = useUserStore();

  useEffect(() => {
    fetchUsers();
  }, [fetchUsers]);

  const handleCreateUser = async () => {
    try {
      await createUser({
        name: "New User",
        email: "user@example.com",
        role: "user",
      });
    } catch (error) {
      console.error("Failed to create user:", error);
    }
  };

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      {users.map((user) => (
        <div key={user.id}>
          {user.name} - {user.role}
        </div>
      ))}
      <button onClick={handleCreateUser}>Add User</button>
    </div>
  );
};
```

**TypeScript Benefits:**

**Redux:**

- Strong typing for actions and state
- Excellent IDE support with autocompletion
- Type-safe selectors and thunks
- Compile-time error detection

**Zustand:**

- Simpler type definitions
- Better inference for store methods
- Less boilerplate for TypeScript setup
- Flexible typing for complex state patterns

Both approaches provide excellent TypeScript support, with Redux offering more structured typing patterns and Zustand providing more flexibility with less boilerplate.

---

### Q19: How do you handle error boundaries and error handling in Redux vs Zustand?

**Answer:**
Error handling strategies differ between Redux and Zustand, with each offering different approaches to manage and recover from errors.

**Redux Error Handling:**

**1. Error Handling in Async Thunks:**

```typescript
import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";

// Custom error types
interface ApiError {
  message: string;
  code: string;
  details?: any;
}

interface ErrorState {
  global: ApiError | null;
  user: ApiError | null;
  network: boolean;
}

interface AppState {
  users: User[];
  loading: boolean;
  errors: ErrorState;
}

const initialState: AppState = {
  users: [],
  loading: false,
  errors: {
    global: null,
    user: null,
    network: false,
  },
};

// Enhanced async thunk with comprehensive error handling
export const fetchUsersWithErrorHandling = createAsyncThunk<
  User[],
  void,
  { rejectValue: ApiError }
>(
  "users/fetchUsersWithErrorHandling",
  async (_, { rejectWithValue, dispatch }) => {
    try {
      const response = await fetch("/api/users", {
        timeout: 10000, // 10 second timeout
      });

      if (!response.ok) {
        // Handle different HTTP status codes
        switch (response.status) {
          case 401:
            dispatch(clearAuthToken());
            throw new Error("Authentication required");
          case 403:
            throw new Error("Access forbidden");
          case 404:
            throw new Error("Users not found");
          case 500:
            throw new Error("Server error");
          default:
            throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }
      }

      const data = await response.json();

      // Validate response data
      if (!Array.isArray(data.users)) {
        throw new Error("Invalid response format");
      }

      return data.users;
    } catch (error) {
      // Categorize errors
      if (error instanceof TypeError && error.message.includes("fetch")) {
        return rejectWithValue({
          message: "Network connection failed",
          code: "NETWORK_ERROR",
          details: error.message,
        });
      }

      if (error.name === "AbortError") {
        return rejectWithValue({
          message: "Request timeout",
          code: "TIMEOUT_ERROR",
        });
      }

      return rejectWithValue({
        message: error instanceof Error ? error.message : "Unknown error",
        code: "API_ERROR",
        details: error,
      });
    }
  }
);

// Error handling slice
const appSlice = createSlice({
  name: "app",
  initialState,
  reducers: {
    clearError: (state, action) => {
      const errorType = action.payload;
      if (errorType && state.errors[errorType]) {
        state.errors[errorType] = null;
      } else {
        // Clear all errors
        state.errors = {
          global: null,
          user: null,
          network: false,
        };
      }
    },
    setGlobalError: (state, action) => {
      state.errors.global = action.payload;
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchUsersWithErrorHandling.pending, (state) => {
        state.loading = true;
        state.errors.user = null;
        state.errors.network = false;
      })
      .addCase(fetchUsersWithErrorHandling.fulfilled, (state, action) => {
        state.loading = false;
        state.users = action.payload;
        state.errors.user = null;
      })
      .addCase(fetchUsersWithErrorHandling.rejected, (state, action) => {
        state.loading = false;

        if (action.payload) {
          if (action.payload.code === "NETWORK_ERROR") {
            state.errors.network = true;
          } else {
            state.errors.user = action.payload;
          }
        } else {
          state.errors.global = {
            message: "An unexpected error occurred",
            code: "UNKNOWN_ERROR",
          };
        }
      });
  },
});

export const { clearError, setGlobalError } = appSlice.actions;
```

**2. Redux Error Boundary Integration:**

```typescript
import React, { Component, ErrorInfo, ReactNode } from "react";
import { connect } from "react-redux";
import { setGlobalError } from "./store/appSlice";

interface Props {
  children: ReactNode;
  setGlobalError: (error: ApiError) => void;
}

interface State {
  hasError: boolean;
}

class ReduxErrorBoundary extends Component<Props, State> {
  constructor(props: Props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(_: Error): State {
    return { hasError: true };
  }

  componentDidCatch(error: Error, errorInfo: ErrorInfo) {
    console.error("Redux Error Boundary caught an error:", error, errorInfo);

    // Dispatch error to Redux store
    this.props.setGlobalError({
      message: error.message,
      code: "COMPONENT_ERROR",
      details: {
        stack: error.stack,
        componentStack: errorInfo.componentStack,
      },
    });
  }

  render() {
    if (this.state.hasError) {
      return (
        <div className="error-fallback">
          <h2>Something went wrong</h2>
          <button onClick={() => this.setState({ hasError: false })}>
            Try again
          </button>
        </div>
      );
    }

    return this.props.children;
  }
}

export default connect(null, { setGlobalError })(ReduxErrorBoundary);
```

**3. Redux Error Display Component:**

```typescript
import React from "react";
import { useSelector, useDispatch } from "react-redux";
import { clearError } from "./store/appSlice";

const ErrorDisplay: React.FC = () => {
  const errors = useSelector((state: RootState) => state.app.errors);
  const dispatch = useDispatch();

  const handleDismiss = (errorType: string) => {
    dispatch(clearError(errorType));
  };

  const handleRetry = () => {
    dispatch(clearError());
    // Retry failed operations
    dispatch(fetchUsersWithErrorHandling());
  };

  if (errors.network) {
    return (
      <div className="error-banner network-error">
        <span>Network connection lost</span>
        <button onClick={handleRetry}>Retry</button>
      </div>
    );
  }

  if (errors.global) {
    return (
      <div className="error-banner global-error">
        <span>{errors.global.message}</span>
        <button onClick={() => handleDismiss("global")}>Dismiss</button>
      </div>
    );
  }

  if (errors.user) {
    return (
      <div className="error-banner user-error">
        <span>{errors.user.message}</span>
        <button onClick={() => handleDismiss("user")}>Dismiss</button>
      </div>
    );
  }

  return null;
};

export default ErrorDisplay;
```

**Zustand Error Handling:**

**1. Zustand Store with Error Handling:**

```typescript
import { create } from 'zustand';
import { devtools } from 'zustand/middleware';
import { immer } from 'zustand/middleware/immer';

interface ErrorState {
  global: ApiError | null;
  user: ApiError | null;
  network: boolean;
}

interface AppState {
  users: User[];
  loading: boolean;
  errors: ErrorState;
}

interface AppActions {
  fetchUsers: () => Promise<void>;
  clearError: (errorType?: keyof ErrorState) => void;
  setGlobalError: (error: ApiError) => void;
  handleError: (error: unknown, context: string) => void;
  retryFailedOperations: () => Promise<void>;
}

type AppStore = AppState & AppActions;

export const useAppStore = create<AppStore>()()
  devtools(
    immer((set, get) => ({
      // Initial state
      users: [],
      loading: false,
      errors: {
        global: null,
        user: null,
        network: false
      },

      // Error handling utilities
      handleError: (error: unknown, context: string) => {
        console.error(`Error in ${context}:`, error);

        set((state) => {
          if (error instanceof TypeError && error.message.includes('fetch')) {
            state.errors.network = true;
          } else if (error instanceof Error) {
            if (context === 'user') {
              state.errors.user = {
                message: error.message,
                code: 'USER_ERROR',
                details: { context }
              };
            } else {
              state.errors.global = {
                message: error.message,
                code: 'GLOBAL_ERROR',
                details: { context }
              };
            }
          } else {
            state.errors.global = {
              message: 'An unexpected error occurred',
              code: 'UNKNOWN_ERROR',
              details: { context, error }
            };
          }
        });
      },

      clearError: (errorType) => set((state) => {
        if (errorType) {
          state.errors[errorType] = errorType === 'network' ? false : null;
        } else {
          state.errors = {
            global: null,
            user: null,
            network: false
          };
        }
      }),

      setGlobalError: (error) => set((state) => {
        state.errors.global = error;
      }),

      // Async operations with error handling
      fetchUsers: async () => {
        const { handleError } = get();

        set((state) => {
          state.loading = true;
          state.errors.user = null;
          state.errors.network = false;
        });

        try {
          const controller = new AbortController();
          const timeoutId = setTimeout(() => controller.abort(), 10000);

          const response = await fetch('/api/users', {
            signal: controller.signal
          });

          clearTimeout(timeoutId);

          if (!response.ok) {
            throw new Error(`HTTP ${response.status}: ${response.statusText}`);
          }

          const data = await response.json();

          if (!Array.isArray(data.users)) {
            throw new Error('Invalid response format');
          }

          set((state) => {
            state.users = data.users;
            state.loading = false;
          });
        } catch (error) {
          set((state) => {
            state.loading = false;
          });
          handleError(error, 'user');
        }
      },

      retryFailedOperations: async () => {
        const { fetchUsers, clearError } = get();
        clearError();
        await fetchUsers();
      }
    })),
    { name: 'app-store' }
  )
);
```

**2. Zustand Error Boundary:**

```typescript
import React, { Component, ErrorInfo, ReactNode } from "react";
import { useAppStore } from "./store";

interface Props {
  children: ReactNode;
}

interface State {
  hasError: boolean;
}

class ZustandErrorBoundary extends Component<Props, State> {
  constructor(props: Props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(_: Error): State {
    return { hasError: true };
  }

  componentDidCatch(error: Error, errorInfo: ErrorInfo) {
    console.error("Zustand Error Boundary caught an error:", error, errorInfo);

    // Access Zustand store directly
    const { setGlobalError } = useAppStore.getState();
    setGlobalError({
      message: error.message,
      code: "COMPONENT_ERROR",
      details: {
        stack: error.stack,
        componentStack: errorInfo.componentStack,
      },
    });
  }

  render() {
    if (this.state.hasError) {
      return (
        <div className="error-fallback">
          <h2>Something went wrong</h2>
          <button onClick={() => this.setState({ hasError: false })}>
            Try again
          </button>
        </div>
      );
    }

    return this.props.children;
  }
}

export default ZustandErrorBoundary;
```

**3. Zustand Error Display Hook:**

```typescript
import { useEffect } from "react";
import { useAppStore } from "./store";

export const useErrorHandler = () => {
  const { errors, clearError, retryFailedOperations } = useAppStore();

  // Auto-clear network errors after connection is restored
  useEffect(() => {
    if (errors.network) {
      const checkConnection = async () => {
        try {
          await fetch("/api/health", { method: "HEAD" });
          clearError("network");
        } catch {
          // Still offline, check again in 5 seconds
          setTimeout(checkConnection, 5000);
        }
      };

      const timeoutId = setTimeout(checkConnection, 2000);
      return () => clearTimeout(timeoutId);
    }
  }, [errors.network, clearError]);

  return {
    errors,
    clearError,
    retryFailedOperations,
    hasErrors: errors.global || errors.user || errors.network,
  };
};

// Error display component
const ZustandErrorDisplay: React.FC = () => {
  const { errors, clearError, retryFailedOperations } = useErrorHandler();

  if (errors.network) {
    return (
      <div className="error-banner network-error">
        <span>Network connection lost</span>
        <button onClick={retryFailedOperations}>Retry</button>
      </div>
    );
  }

  if (errors.global) {
    return (
      <div className="error-banner global-error">
        <span>{errors.global.message}</span>
        <button onClick={() => clearError("global")}>Dismiss</button>
      </div>
    );
  }

  if (errors.user) {
    return (
      <div className="error-banner user-error">
        <span>{errors.user.message}</span>
        <button onClick={() => clearError("user")}>Dismiss</button>
      </div>
    );
  }

  return null;
};

export default ZustandErrorDisplay;
```

**Error Handling Comparison:**

**Redux:**

- Structured error handling through reducers
- Centralized error state management
- Built-in support for async error handling
- Integration with Redux DevTools for debugging

**Zustand:**

- More flexible error handling patterns
- Direct store access from error boundaries
- Simpler error state updates
- Custom hooks for error management

**Best Practices:**

1. Categorize errors by type and severity
2. Provide user-friendly error messages
3. Implement retry mechanisms for transient errors
4. Log errors for debugging and monitoring
5. Use error boundaries to catch component errors
6. Handle network errors gracefully
7. Provide fallback UI for critical errors

---

### Q20: What are the advanced patterns and real-world use cases for Redux vs Zustand?

**Answer:**
Both Redux and Zustand support advanced patterns for complex applications, but they approach them differently.

**Redux Advanced Patterns:**

**1. Entity Normalization with RTK Query:**

```typescript
import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";
import { createEntityAdapter, createSlice } from "@reduxjs/toolkit";

// Entity adapter for normalized state
const usersAdapter = createEntityAdapter<User>({
  selectId: (user) => user.id,
  sortComparer: (a, b) => a.name.localeCompare(b.name),
});

// RTK Query API
export const apiSlice = createApi({
  reducerPath: "api",
  baseQuery: fetchBaseQuery({
    baseUrl: "/api",
    prepareHeaders: (headers, { getState }) => {
      const token = (getState() as RootState).auth.token;
      if (token) {
        headers.set("authorization", `Bearer ${token}`);
      }
      return headers;
    },
  }),
  tagTypes: ["User", "Post", "Comment"],
  endpoints: (builder) => ({
    getUsers: builder.query<User[], void>({
      query: () => "/users",
      providesTags: ["User"],
      transformResponse: (response: { users: User[] }) => response.users,
    }),
    getUserById: builder.query<User, string>({
      query: (id) => `/users/${id}`,
      providesTags: (result, error, id) => [{ type: "User", id }],
    }),
    updateUser: builder.mutation<User, { id: string; updates: Partial<User> }>({
      query: ({ id, updates }) => ({
        url: `/users/${id}`,
        method: "PATCH",
        body: updates,
      }),
      invalidatesTags: (result, error, { id }) => [{ type: "User", id }],
    }),
    getUserPosts: builder.query<Post[], string>({
      query: (userId) => `/users/${userId}/posts`,
      providesTags: (result, error, userId) =>
        result
          ? [...result.map(({ id }) => ({ type: "Post" as const, id })), "Post"]
          : ["Post"],
    }),
  }),
});

export const {
  useGetUsersQuery,
  useGetUserByIdQuery,
  useUpdateUserMutation,
  useGetUserPostsQuery,
} = apiSlice;
```

**2. Advanced Middleware Chain:**

```typescript
import { configureStore, createListenerMiddleware } from "@reduxjs/toolkit";
import { persistStore, persistReducer } from "redux-persist";
import storage from "redux-persist/lib/storage";

// Custom middleware for analytics
const analyticsMiddleware: Middleware = (store) => (next) => (action) => {
  // Track user actions
  if (action.type.startsWith("user/")) {
    analytics.track("User Action", {
      action: action.type,
      payload: action.payload,
      timestamp: Date.now(),
    });
  }
  return next(action);
};

// Listener middleware for side effects
const listenerMiddleware = createListenerMiddleware();

// Listen for user updates and sync with external services
listenerMiddleware.startListening({
  actionCreator: updateUser,
  effect: async (action, listenerApi) => {
    const { id, updates } = action.payload;

    // Sync with external CRM
    try {
      await syncWithCRM(id, updates);
    } catch (error) {
      console.error("Failed to sync with CRM:", error);
      // Optionally dispatch a compensation action
      listenerApi.dispatch(
        setCrmSyncError({ userId: id, error: error.message })
      );
    }

    // Update search index
    await updateSearchIndex(id, updates);
  },
});

// Persist configuration
const persistConfig = {
  key: "root",
  storage,
  whitelist: ["user", "preferences"],
  transforms: [
    // Custom transform to encrypt sensitive data
    createTransform(
      (inboundState: any) => {
        return {
          ...inboundState,
          sensitiveData: encrypt(inboundState.sensitiveData),
        };
      },
      (outboundState: any) => {
        return {
          ...outboundState,
          sensitiveData: decrypt(outboundState.sensitiveData),
        };
      },
      { whitelist: ["user"] }
    ),
  ],
};

const persistedReducer = persistReducer(persistConfig, rootReducer);

export const store = configureStore({
  reducer: persistedReducer,
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: {
        ignoredActions: [FLUSH, REHYDRATE, PAUSE, PERSIST, PURGE, REGISTER],
      },
    })
      .concat(apiSlice.middleware)
      .concat(analyticsMiddleware)
      .concat(listenerMiddleware.middleware),
  devTools: process.env.NODE_ENV !== "production",
});

export const persistor = persistStore(store);
```

**3. Feature-Based Architecture:**

```typescript
// features/user/userSlice.ts
export const userSlice = createSlice({
  name: "user",
  initialState: usersAdapter.getInitialState({
    loading: false,
    error: null,
    filters: {
      role: null,
      status: null,
      search: "",
    },
    pagination: {
      page: 1,
      limit: 10,
      total: 0,
    },
  }),
  reducers: {
    setFilters: (state, action) => {
      state.filters = { ...state.filters, ...action.payload };
      state.pagination.page = 1; // Reset to first page
    },
    setPagination: (state, action) => {
      state.pagination = { ...state.pagination, ...action.payload };
    },
  },
  extraReducers: (builder) => {
    builder
      .addMatcher(
        apiSlice.endpoints.getUsers.matchFulfilled,
        (state, action) => {
          usersAdapter.setAll(state, action.payload);
          state.loading = false;
        }
      )
      .addMatcher(
        apiSlice.endpoints.updateUser.matchFulfilled,
        (state, action) => {
          usersAdapter.updateOne(state, {
            id: action.payload.id,
            changes: action.payload,
          });
        }
      );
  },
});

// Selectors with memoization
export const {
  selectAll: selectAllUsers,
  selectById: selectUserById,
  selectIds: selectUserIds,
} = usersAdapter.getSelectors((state: RootState) => state.user);

export const selectFilteredUsers = createSelector(
  [selectAllUsers, (state: RootState) => state.user.filters],
  (users, filters) => {
    return users.filter((user) => {
      if (filters.role && user.role !== filters.role) return false;
      if (filters.status && user.status !== filters.status) return false;
      if (
        filters.search &&
        !user.name.toLowerCase().includes(filters.search.toLowerCase())
      )
        return false;
      return true;
    });
  }
);

export const selectPaginatedUsers = createSelector(
  [selectFilteredUsers, (state: RootState) => state.user.pagination],
  (users, pagination) => {
    const start = (pagination.page - 1) * pagination.limit;
    const end = start + pagination.limit;
    return users.slice(start, end);
  }
);
```

**Zustand Advanced Patterns:**

**1. Modular Store with Subscriptions:**

```typescript
import { create } from 'zustand';
import { subscribeWithSelector } from 'zustand/middleware';
import { immer } from 'zustand/middleware/immer';

// Modular store slices
interface UserSlice {
  users: Map<string, User>;
  userActions: {
    addUser: (user: User) => void;
    updateUser: (id: string, updates: Partial<User>) => void;
    removeUser: (id: string) => void;
    getUserById: (id: string) => User | undefined;
    getUsersByRole: (role: string) => User[];
  };
}

interface NotificationSlice {
  notifications: Notification[];
  notificationActions: {
    addNotification: (notification: Omit<Notification, 'id'>) => void;
    removeNotification: (id: string) => void;
    markAsRead: (id: string) => void;
    clearAll: () => void;
  };
}

interface AnalyticsSlice {
  events: AnalyticsEvent[];
  analyticsActions: {
    trackEvent: (event: Omit<AnalyticsEvent, 'id' | 'timestamp'>) => void;
    getEventsByType: (type: string) => AnalyticsEvent[];
    clearEvents: () => void;
  };
}

type AppStore = UserSlice & NotificationSlice & AnalyticsSlice;

// Create modular store with subscriptions
export const useAppStore = create<AppStore>()()
  subscribeWithSelector(
    immer((set, get) => ({
      // User slice
      users: new Map(),
      userActions: {
        addUser: (user) => set((state) => {
          state.users.set(user.id, user);
          // Trigger analytics
          state.analyticsActions.trackEvent({
            type: 'user_added',
            data: { userId: user.id, role: user.role }
          });
        }),

        updateUser: (id, updates) => set((state) => {
          const user = state.users.get(id);
          if (user) {
            state.users.set(id, { ...user, ...updates });
            // Trigger notification
            state.notificationActions.addNotification({
              type: 'success',
              message: `User ${user.name} updated successfully`,
              duration: 3000
            });
          }
        }),

        removeUser: (id) => set((state) => {
          const user = state.users.get(id);
          if (user) {
            state.users.delete(id);
            state.analyticsActions.trackEvent({
              type: 'user_removed',
              data: { userId: id, role: user.role }
            });
          }
        }),

        getUserById: (id) => get().users.get(id),

        getUsersByRole: (role) => {
          return Array.from(get().users.values()).filter(user => user.role === role);
        }
      },

      // Notification slice
      notifications: [],
      notificationActions: {
        addNotification: (notification) => set((state) => {
          const newNotification = {
            ...notification,
            id: crypto.randomUUID(),
            timestamp: Date.now(),
            read: false
          };
          state.notifications.push(newNotification);

          // Auto-remove after duration
          if (notification.duration) {
            setTimeout(() => {
              get().notificationActions.removeNotification(newNotification.id);
            }, notification.duration);
          }
        }),

        removeNotification: (id) => set((state) => {
          state.notifications = state.notifications.filter(n => n.id !== id);
        }),

        markAsRead: (id) => set((state) => {
          const notification = state.notifications.find(n => n.id === id);
          if (notification) {
            notification.read = true;
          }
        }),

        clearAll: () => set((state) => {
          state.notifications = [];
        })
      },

      // Analytics slice
      events: [],
      analyticsActions: {
        trackEvent: (event) => set((state) => {
          state.events.push({
            ...event,
            id: crypto.randomUUID(),
            timestamp: Date.now()
          });

          // Keep only last 1000 events
          if (state.events.length > 1000) {
            state.events = state.events.slice(-1000);
          }
        }),

        getEventsByType: (type) => {
          return get().events.filter(event => event.type === type);
        },

        clearEvents: () => set((state) => {
          state.events = [];
        })
      }
    }))
  )
);

// Subscribe to user changes for external sync
useAppStore.subscribe(
  (state) => state.users,
  (users, prevUsers) => {
    // Sync with external services when users change
    const changedUsers = Array.from(users.entries()).filter(
      ([id, user]) => {
        const prevUser = prevUsers.get(id);
        return !prevUser || JSON.stringify(user) !== JSON.stringify(prevUser);
      }
    );

    changedUsers.forEach(([id, user]) => {
      syncUserWithExternalService(user);
    });
  },
  { equalityFn: (a, b) => a.size === b.size }
);

// Subscribe to analytics events for batching
let eventBatch: AnalyticsEvent[] = [];
useAppStore.subscribe(
  (state) => state.events,
  (events) => {
    const newEvents = events.slice(eventBatch.length);
    eventBatch.push(...newEvents);

    // Batch send every 10 events or 30 seconds
    if (eventBatch.length >= 10) {
      sendAnalyticsBatch(eventBatch);
      eventBatch = [];
    }
  }
);

// Periodic batch send
setInterval(() => {
  if (eventBatch.length > 0) {
    sendAnalyticsBatch(eventBatch);
    eventBatch = [];
  }
}, 30000);
```

**2. Advanced Persistence and Hydration:**

```typescript
import { create } from 'zustand';
import { persist, createJSONStorage } from 'zustand/middleware';

// Custom storage with encryption
const encryptedStorage = {
  getItem: async (name: string) => {
    const encrypted = localStorage.getItem(name);
    if (!encrypted) return null;
    try {
      return decrypt(encrypted);
    } catch {
      return null;
    }
  },
  setItem: async (name: string, value: string) => {
    const encrypted = encrypt(value);
    localStorage.setItem(name, encrypted);
  },
  removeItem: async (name: string) => {
    localStorage.removeItem(name);
  }
};

// Store with advanced persistence
export const usePersistedStore = create<AppState>()()
  persist(
    (set, get) => ({
      // Store implementation
      user: null,
      preferences: defaultPreferences,
      cache: new Map(),

      setUser: (user) => set({ user }),
      updatePreferences: (updates) => set((state) => ({
        preferences: { ...state.preferences, ...updates }
      })),

      // Cache management
      setCache: (key, value, ttl = 300000) => set((state) => {
        const newCache = new Map(state.cache);
        newCache.set(key, {
          value,
          expires: Date.now() + ttl
        });
        return { cache: newCache };
      }),

      getCache: (key) => {
        const cached = get().cache.get(key);
        if (!cached || cached.expires < Date.now()) {
          return null;
        }
        return cached.value;
      },

      clearExpiredCache: () => set((state) => {
        const newCache = new Map();
        const now = Date.now();

        for (const [key, value] of state.cache) {
          if (value.expires > now) {
            newCache.set(key, value);
          }
        }

        return { cache: newCache };
      })
    }),
    {
      name: 'app-storage',
      storage: createJSONStorage(() => encryptedStorage),
      partialize: (state) => ({
        user: state.user,
        preferences: state.preferences
        // Exclude cache from persistence
      }),
      onRehydrateStorage: () => (state) => {
        if (state) {
          // Initialize cache as Map after rehydration
          state.cache = new Map();
          // Clear expired cache on startup
          state.clearExpiredCache();
        }
      },
      migrate: (persistedState: any, version: number) => {
        // Handle migration between versions
        if (version === 0) {
          // Migrate from version 0 to 1
          return {
            ...persistedState,
            preferences: {
              ...defaultPreferences,
              ...persistedState.preferences
            }
          };
        }
        return persistedState;
      },
      version: 1
    }
  )
);
```

**Real-World Use Cases:**

**Redux Best For:**

- Large enterprise applications with complex state
- Applications requiring strict state management patterns
- Teams needing predictable state updates
- Applications with extensive debugging requirements
- Complex async operations with caching
- Applications requiring time-travel debugging

**Zustand Best For:**

- Medium-sized applications with moderate complexity
- Rapid prototyping and development
- Applications requiring flexible state patterns
- Teams preferring minimal boilerplate
- Applications with simple to moderate async needs
- Projects requiring quick setup and iteration

**Performance Considerations:**

- Redux: Better for large datasets with normalization
- Zustand: Better for smaller, frequently updated state
- Both: Support selective subscriptions and memoization

**Team and Maintenance:**

- Redux: Steeper learning curve, more structured
- Zustand: Easier onboarding, more flexible
- Both: Strong TypeScript support and community

Choose based on your specific requirements, team expertise, and application complexity.

---

### Q23: What are Redux actions and action creators? How do you structure them?

**Answer:**
Actions are plain JavaScript objects that describe what happened in your application. Action creators are functions that return action objects.

**Basic Action Structure:**

```javascript
// Action Types
const ADD_TODO = "ADD_TODO";
const TOGGLE_TODO = "TOGGLE_TODO";
const SET_FILTER = "SET_FILTER";

// Action Creators
const addTodo = (text) => ({
  type: ADD_TODO,
  payload: {
    id: Date.now(),
    text,
    completed: false,
  },
});

const toggleTodo = (id) => ({
  type: TOGGLE_TODO,
  payload: { id },
});

const setFilter = (filter) => ({
  type: SET_FILTER,
  payload: { filter },
});
```

**Advanced Action Creators with Redux Toolkit:**

```javascript
import { createAction, createAsyncThunk } from "@reduxjs/toolkit";

// Simple action creators
export const addTodo = createAction("todos/add", (text) => ({
  payload: {
    id: Date.now(),
    text,
    completed: false,
  },
}));

export const toggleTodo = createAction("todos/toggle");

// Async action creators
export const fetchTodos = createAsyncThunk(
  "todos/fetchTodos",
  async (userId, { rejectWithValue }) => {
    try {
      const response = await fetch(`/api/todos/${userId}`);
      if (!response.ok) {
        throw new Error("Failed to fetch todos");
      }
      return await response.json();
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);

// Action creator with prepare callback
export const addTodoWithTimestamp = createAction(
  "todos/addWithTimestamp",
  (text) => {
    return {
      payload: {
        id: Date.now(),
        text,
        completed: false,
        createdAt: new Date().toISOString(),
      },
    };
  }
);
```

**Structured Action Organization:**

```javascript
// actions/todoActions.js
export const todoActions = {
  // Synchronous actions
  add: createAction("todos/add"),
  toggle: createAction("todos/toggle"),
  remove: createAction("todos/remove"),
  edit: createAction("todos/edit"),

  // Async actions
  fetch: createAsyncThunk("todos/fetch", async () => {
    const response = await api.getTodos();
    return response.data;
  }),

  create: createAsyncThunk("todos/create", async (todoData) => {
    const response = await api.createTodo(todoData);
    return response.data;
  }),

  update: createAsyncThunk("todos/update", async ({ id, updates }) => {
    const response = await api.updateTodo(id, updates);
    return response.data;
  }),

  delete: createAsyncThunk("todos/delete", async (id) => {
    await api.deleteTodo(id);
    return id;
  }),
};
```

**Action Creator Patterns:**

```javascript
// 1. FSA (Flux Standard Action) Pattern
const createFSAAction = (type) => (payload, meta) => ({
  type,
  payload,
  meta,
  error: payload instanceof Error,
});

// 2. Action Creator Factory
const createCRUDActions = (entityName) => {
  const upperName = entityName.toUpperCase();

  return {
    create: createAction(`${upperName}/CREATE`),
    read: createAction(`${upperName}/READ`),
    update: createAction(`${upperName}/UPDATE`),
    delete: createAction(`${upperName}/DELETE`),

    // Async versions
    fetchAll: createAsyncThunk(`${upperName}/FETCH_ALL`, async () => {
      const response = await api.getAll(entityName);
      return response.data;
    }),

    createAsync: createAsyncThunk(`${upperName}/CREATE_ASYNC`, async (data) => {
      const response = await api.create(entityName, data);
      return response.data;
    }),
  };
};

// Usage
const userActions = createCRUDActions("user");
const productActions = createCRUDActions("product");
```

**Best Practices:**

1. **Use Action Constants:**

```javascript
// constants/actionTypes.js
export const TODO_ACTIONS = {
  ADD: "todos/add",
  TOGGLE: "todos/toggle",
  REMOVE: "todos/remove",
  FETCH: "todos/fetch",
};
```

2. **Normalize Action Payloads:**

```javascript
const addUser = (userData) => ({
  type: "users/add",
  payload: {
    user: normalizeUser(userData),
    timestamp: Date.now(),
    source: "user_input",
  },
});
```

3. **Use TypeScript for Type Safety:**

```typescript
interface AddTodoAction {
  type: "todos/add";
  payload: {
    id: string;
    text: string;
    completed: boolean;
  };
}

interface ToggleTodoAction {
  type: "todos/toggle";
  payload: {
    id: string;
  };
}

type TodoAction = AddTodoAction | ToggleTodoAction;

const addTodo = (text: string): AddTodoAction => ({
  type: "todos/add",
  payload: {
    id: Date.now().toString(),
    text,
    completed: false,
  },
});
```

**Key Points:**

- Actions describe what happened, not how state should change
- Action creators provide a consistent API for creating actions
- Use Redux Toolkit's `createAction` for better DX and TypeScript support
- Organize actions by feature/domain for better maintainability
- Consider using action creator factories for repetitive patterns

---

### Q24: How do you handle form state management in Redux vs Zustand?

**Answer:**
Form state management can be handled differently in Redux and Zustand, each with their own advantages for different use cases.

**Redux Form State Management:**

```javascript
// Redux Toolkit slice for form state
import { createSlice } from "@reduxjs/toolkit";

const formSlice = createSlice({
  name: "form",
  initialState: {
    userForm: {
      values: {
        name: "",
        email: "",
        age: "",
      },
      errors: {},
      touched: {},
      isSubmitting: false,
      isValid: true,
    },
  },
  reducers: {
    updateField: (state, action) => {
      const { formName, field, value } = action.payload;
      state[formName].values[field] = value;
      state[formName].touched[field] = true;

      // Clear error when user starts typing
      if (state[formName].errors[field]) {
        delete state[formName].errors[field];
      }
    },

    setErrors: (state, action) => {
      const { formName, errors } = action.payload;
      state[formName].errors = errors;
      state[formName].isValid = Object.keys(errors).length === 0;
    },

    setSubmitting: (state, action) => {
      const { formName, isSubmitting } = action.payload;
      state[formName].isSubmitting = isSubmitting;
    },

    resetForm: (state, action) => {
      const { formName } = action.payload;
      state[formName] = {
        values: {},
        errors: {},
        touched: {},
        isSubmitting: false,
        isValid: true,
      };
    },
  },
});

export const { updateField, setErrors, setSubmitting, resetForm } =
  formSlice.actions;
export default formSlice.reducer;
```

**Redux Form Component:**

```javascript
import React from "react";
import { useSelector, useDispatch } from "react-redux";
import { updateField, setErrors, setSubmitting } from "./formSlice";

const UserForm = () => {
  const dispatch = useDispatch();
  const form = useSelector((state) => state.form.userForm);

  const handleChange = (field) => (e) => {
    dispatch(
      updateField({
        formName: "userForm",
        field,
        value: e.target.value,
      })
    );
  };

  const validateForm = () => {
    const errors = {};

    if (!form.values.name) errors.name = "Name is required";
    if (!form.values.email) errors.email = "Email is required";
    else if (!/\S+@\S+\.\S+/.test(form.values.email)) {
      errors.email = "Email is invalid";
    }

    dispatch(setErrors({ formName: "userForm", errors }));
    return Object.keys(errors).length === 0;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!validateForm()) return;

    dispatch(setSubmitting({ formName: "userForm", isSubmitting: true }));

    try {
      await submitUserData(form.values);
      dispatch(resetForm({ formName: "userForm" }));
    } catch (error) {
      dispatch(
        setErrors({
          formName: "userForm",
          errors: { submit: error.message },
        })
      );
    } finally {
      dispatch(setSubmitting({ formName: "userForm", isSubmitting: false }));
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={form.values.name || ""}
        onChange={handleChange("name")}
        placeholder="Name"
      />
      {form.errors.name && <span>{form.errors.name}</span>}

      <input
        type="email"
        value={form.values.email || ""}
        onChange={handleChange("email")}
        placeholder="Email"
      />
      {form.errors.email && <span>{form.errors.email}</span>}

      <button type="submit" disabled={form.isSubmitting}>
        {form.isSubmitting ? "Submitting..." : "Submit"}
      </button>
    </form>
  );
};
```

**Zustand Form State Management:**

```javascript
// Zustand form store
import { create } from "zustand";
import { immer } from "zustand/middleware/immer";

const useFormStore = create(
  immer((set, get) => ({
    forms: {},

    // Initialize form
    initForm: (formName, initialValues = {}) =>
      set((state) => {
        state.forms[formName] = {
          values: initialValues,
          errors: {},
          touched: {},
          isSubmitting: false,
          isValid: true,
        };
      }),

    // Update field value
    updateField: (formName, field, value) =>
      set((state) => {
        if (!state.forms[formName]) return;

        state.forms[formName].values[field] = value;
        state.forms[formName].touched[field] = true;

        // Clear error when user starts typing
        if (state.forms[formName].errors[field]) {
          delete state.forms[formName].errors[field];
        }
      }),

    // Set form errors
    setErrors: (formName, errors) =>
      set((state) => {
        if (!state.forms[formName]) return;

        state.forms[formName].errors = errors;
        state.forms[formName].isValid = Object.keys(errors).length === 0;
      }),

    // Set submitting state
    setSubmitting: (formName, isSubmitting) =>
      set((state) => {
        if (!state.forms[formName]) return;
        state.forms[formName].isSubmitting = isSubmitting;
      }),

    // Reset form
    resetForm: (formName) =>
      set((state) => {
        if (!state.forms[formName]) return;

        state.forms[formName] = {
          values: {},
          errors: {},
          touched: {},
          isSubmitting: false,
          isValid: true,
        };
      }),

    // Get form data
    getForm: (formName) => {
      const state = get();
      return state.forms[formName] || null;
    },
  }))
);

export default useFormStore;
```

**Zustand Form Component:**

```javascript
import React, { useEffect } from "react";
import useFormStore from "./formStore";

const UserForm = () => {
  const { forms, initForm, updateField, setErrors, setSubmitting, resetForm } =
    useFormStore();

  const form = forms.userForm;

  useEffect(() => {
    initForm("userForm", { name: "", email: "", age: "" });
  }, []);

  if (!form) return null;

  const handleChange = (field) => (e) => {
    updateField("userForm", field, e.target.value);
  };

  const validateForm = () => {
    const errors = {};

    if (!form.values.name) errors.name = "Name is required";
    if (!form.values.email) errors.email = "Email is required";
    else if (!/\S+@\S+\.\S+/.test(form.values.email)) {
      errors.email = "Email is invalid";
    }

    setErrors("userForm", errors);
    return Object.keys(errors).length === 0;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!validateForm()) return;

    setSubmitting("userForm", true);

    try {
      await submitUserData(form.values);
      resetForm("userForm");
    } catch (error) {
      setErrors("userForm", { submit: error.message });
    } finally {
      setSubmitting("userForm", false);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={form.values.name || ""}
        onChange={handleChange("name")}
        placeholder="Name"
      />
      {form.errors.name && <span>{form.errors.name}</span>}

      <input
        type="email"
        value={form.values.email || ""}
        onChange={handleChange("email")}
        placeholder="Email"
      />
      {form.errors.email && <span>{form.errors.email}</span>}

      <button type="submit" disabled={form.isSubmitting}>
        {form.isSubmitting ? "Submitting..." : "Submit"}
      </button>
    </form>
  );
};
```

**Advanced Form Patterns:**

**1. Form Validation Hook (Zustand):**

```javascript
const useFormValidation = (formName, validationRules) => {
  const { getForm, setErrors } = useFormStore();

  const validate = useCallback(() => {
    const form = getForm(formName);
    if (!form) return false;

    const errors = {};

    Object.entries(validationRules).forEach(([field, rules]) => {
      const value = form.values[field];

      rules.forEach((rule) => {
        if (rule.required && !value) {
          errors[field] = rule.message || `${field} is required`;
        } else if (rule.pattern && value && !rule.pattern.test(value)) {
          errors[field] = rule.message || `${field} is invalid`;
        } else if (rule.minLength && value && value.length < rule.minLength) {
          errors[field] =
            rule.message ||
            `${field} must be at least ${rule.minLength} characters`;
        }
      });
    });

    setErrors(formName, errors);
    return Object.keys(errors).length === 0;
  }, [formName, validationRules, getForm, setErrors]);

  return { validate };
};

// Usage
const validationRules = {
  name: [{ required: true, message: "Name is required" }],
  email: [
    { required: true, message: "Email is required" },
    { pattern: /\S+@\S+\.\S+/, message: "Email is invalid" },
  ],
};

const { validate } = useFormValidation("userForm", validationRules);
```

**2. Dynamic Form Fields:**

```javascript
// Redux approach
const dynamicFormSlice = createSlice({
  name: "dynamicForm",
  initialState: {
    fields: [],
    values: {},
  },
  reducers: {
    addField: (state, action) => {
      state.fields.push(action.payload);
    },
    removeField: (state, action) => {
      const fieldName = action.payload;
      state.fields = state.fields.filter((field) => field.name !== fieldName);
      delete state.values[fieldName];
    },
    updateValue: (state, action) => {
      const { field, value } = action.payload;
      state.values[field] = value;
    },
  },
});

// Zustand approach
const useDynamicFormStore = create((set) => ({
  fields: [],
  values: {},

  addField: (field) =>
    set((state) => ({
      fields: [...state.fields, field],
    })),

  removeField: (fieldName) =>
    set((state) => {
      const newValues = { ...state.values };
      delete newValues[fieldName];

      return {
        fields: state.fields.filter((field) => field.name !== fieldName),
        values: newValues,
      };
    }),

  updateValue: (field, value) =>
    set((state) => ({
      values: { ...state.values, [field]: value },
    })),
}));
```

**Comparison Summary:**

**Redux Advantages:**

- Centralized form state management
- Time-travel debugging for forms
- Predictable state updates
- Better for complex form workflows

**Zustand Advantages:**

- Less boilerplate code
- More flexible form structure
- Easier to implement dynamic forms
- Better performance for frequent updates

**When to Use Each:**

- **Redux**: Complex forms, multi-step wizards, form state needs to persist across routes
- **Zustand**: Simple forms, component-level form state, rapid prototyping

---

### Q25: What are Redux selectors and how do you create reusable selectors?

**Answer:**
Selectors are functions that extract specific pieces of state from the Redux store. They provide a clean API for accessing state and enable memoization for performance optimization.

**Basic Selectors:**

```javascript
// Basic selector functions
const selectTodos = (state) => state.todos.items;
const selectTodosLoading = (state) => state.todos.loading;
const selectTodosError = (state) => state.todos.error;
const selectCurrentUser = (state) => state.auth.user;

// Using selectors in components
import { useSelector } from "react-redux";

const TodoList = () => {
  const todos = useSelector(selectTodos);
  const loading = useSelector(selectTodosLoading);
  const error = useSelector(selectTodosError);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <ul>
      {todos.map((todo) => (
        <li key={todo.id}>{todo.text}</li>
      ))}
    </ul>
  );
};
```

**Memoized Selectors with Reselect:**

```javascript
import { createSelector } from "@reduxjs/toolkit";

// Input selectors
const selectTodos = (state) => state.todos.items;
const selectFilter = (state) => state.todos.filter;
const selectSearchTerm = (state) => state.todos.searchTerm;

// Memoized selectors
const selectFilteredTodos = createSelector(
  [selectTodos, selectFilter],
  (todos, filter) => {
    console.log("Computing filtered todos"); // Only runs when inputs change

    switch (filter) {
      case "completed":
        return todos.filter((todo) => todo.completed);
      case "active":
        return todos.filter((todo) => !todo.completed);
      default:
        return todos;
    }
  }
);

const selectSearchedTodos = createSelector(
  [selectFilteredTodos, selectSearchTerm],
  (filteredTodos, searchTerm) => {
    if (!searchTerm) return filteredTodos;

    return filteredTodos.filter((todo) =>
      todo.text.toLowerCase().includes(searchTerm.toLowerCase())
    );
  }
);

// Complex computed selectors
const selectTodoStats = createSelector([selectTodos], (todos) => ({
  total: todos.length,
  completed: todos.filter((todo) => todo.completed).length,
  active: todos.filter((todo) => !todo.completed).length,
  completionRate:
    todos.length > 0
      ? (todos.filter((todo) => todo.completed).length / todos.length) * 100
      : 0,
}));
```

**Parameterized Selectors:**

```javascript
// Selector factory for parameterized selectors
const makeSelectTodoById = () =>
  createSelector([selectTodos, (state, todoId) => todoId], (todos, todoId) =>
    todos.find((todo) => todo.id === todoId)
  );

// Usage in component
const TodoItem = ({ todoId }) => {
  const selectTodoById = useMemo(makeSelectTodoById, []);
  const todo = useSelector((state) => selectTodoById(state, todoId));

  return <div>{todo?.text}</div>;
};

// Alternative approach with createSelector
const selectTodoById = createSelector(
  [selectTodos, (state, id) => id],
  (todos, id) => todos.find((todo) => todo.id === id)
);

// Using with useSelector
const todo = useSelector((state) => selectTodoById(state, todoId));
```

**Advanced Selector Patterns:**

```javascript
// 1. Selector composition
const selectUserTodos = createSelector(
  [selectTodos, selectCurrentUser],
  (todos, user) => todos.filter((todo) => todo.userId === user?.id)
);

const selectUserCompletedTodos = createSelector(
  [selectUserTodos],
  (userTodos) => userTodos.filter((todo) => todo.completed)
);

// 2. Denormalized data selectors
const selectTodosWithCategories = createSelector(
  [selectTodos, (state) => state.categories.items],
  (todos, categories) => {
    const categoryMap = categories.reduce((acc, cat) => {
      acc[cat.id] = cat;
      return acc;
    }, {});

    return todos.map((todo) => ({
      ...todo,
      category: categoryMap[todo.categoryId],
    }));
  }
);

// 3. Aggregation selectors
const selectTodosByCategory = createSelector(
  [selectTodosWithCategories],
  (todosWithCategories) => {
    return todosWithCategories.reduce((acc, todo) => {
      const categoryName = todo.category?.name || "Uncategorized";
      if (!acc[categoryName]) {
        acc[categoryName] = [];
      }
      acc[categoryName].push(todo);
      return acc;
    }, {});
  }
);

// 4. Sorted selectors
const selectSortedTodos = createSelector(
  [
    selectTodos,
    (state) => state.todos.sortBy,
    (state) => state.todos.sortOrder,
  ],
  (todos, sortBy, sortOrder) => {
    const sorted = [...todos].sort((a, b) => {
      let aVal = a[sortBy];
      let bVal = b[sortBy];

      if (sortBy === "createdAt") {
        aVal = new Date(aVal);
        bVal = new Date(bVal);
      }

      if (aVal < bVal) return sortOrder === "asc" ? -1 : 1;
      if (aVal > bVal) return sortOrder === "asc" ? 1 : -1;
      return 0;
    });

    return sorted;
  }
);
```

**Selector Organization:**

```javascript
// selectors/todoSelectors.js
export const todoSelectors = {
  // Basic selectors
  selectTodos: (state) => state.todos.items,
  selectTodosLoading: (state) => state.todos.loading,
  selectTodosError: (state) => state.todos.error,
  selectFilter: (state) => state.todos.filter,
  selectSearchTerm: (state) => state.todos.searchTerm,

  // Computed selectors
  selectFilteredTodos: createSelector(
    [(state) => state.todos.items, (state) => state.todos.filter],
    (todos, filter) => {
      switch (filter) {
        case "completed":
          return todos.filter((todo) => todo.completed);
        case "active":
          return todos.filter((todo) => !todo.completed);
        default:
          return todos;
      }
    }
  ),

  selectTodoStats: createSelector([(state) => state.todos.items], (todos) => ({
    total: todos.length,
    completed: todos.filter((todo) => todo.completed).length,
    active: todos.filter((todo) => !todo.completed).length,
  })),
};

// Export individual selectors for convenience
export const {
  selectTodos,
  selectTodosLoading,
  selectFilteredTodos,
  selectTodoStats,
} = todoSelectors;
```

**Testing Selectors:**

```javascript
// selectors.test.js
import { selectFilteredTodos, selectTodoStats } from "./todoSelectors";

describe("Todo Selectors", () => {
  const mockState = {
    todos: {
      items: [
        { id: 1, text: "Learn Redux", completed: false },
        { id: 2, text: "Write tests", completed: true },
        { id: 3, text: "Deploy app", completed: false },
      ],
      filter: "all",
    },
  };

  describe("selectFilteredTodos", () => {
    it('should return all todos when filter is "all"', () => {
      const result = selectFilteredTodos(mockState);
      expect(result).toHaveLength(3);
    });

    it('should return only completed todos when filter is "completed"', () => {
      const stateWithFilter = {
        ...mockState,
        todos: { ...mockState.todos, filter: "completed" },
      };

      const result = selectFilteredTodos(stateWithFilter);
      expect(result).toHaveLength(1);
      expect(result[0].completed).toBe(true);
    });
  });

  describe("selectTodoStats", () => {
    it("should calculate correct statistics", () => {
      const result = selectTodoStats(mockState);

      expect(result).toEqual({
        total: 3,
        completed: 1,
        active: 2,
      });
    });
  });
});
```

**Performance Optimization with Selectors:**

```javascript
// 1. Avoid creating new objects in selectors
// BAD - creates new object every time
const badSelector = (state) => ({
  todos: state.todos,
  user: state.user,
});

// GOOD - use createSelector for object creation
const goodSelector = createSelector(
  [(state) => state.todos, (state) => state.user],
  (todos, user) => ({ todos, user })
);

// 2. Use shallow equality for arrays
const selectTodoIds = createSelector([selectTodos], (todos) =>
  todos.map((todo) => todo.id)
);

// 3. Memoize expensive computations
const selectExpensiveComputation = createSelector([selectTodos], (todos) => {
  // Expensive operation that should be memoized
  return todos.reduce((acc, todo) => {
    // Complex computation
    return acc + complexCalculation(todo);
  }, 0);
});
```

**Best Practices:**

1. **Keep selectors pure** - no side effects
2. **Use memoization** for expensive computations
3. **Organize selectors** by feature/domain
4. **Test selectors** independently
5. **Avoid deep nesting** in selector logic
6. **Use TypeScript** for better type safety
7. **Document complex selectors** with comments
8. **Prefer composition** over large monolithic selectors

**Key Benefits:**

- **Performance**: Memoization prevents unnecessary re-computations
- **Reusability**: Selectors can be shared across components
- **Testability**: Easy to unit test selector logic
- **Maintainability**: Centralized state access logic
- **Type Safety**: Better TypeScript integration

---

### Q26: How do you handle authentication state management in Redux vs Zustand?

**Answer:**
Authentication state management involves handling user login/logout, token storage, session persistence, and protecting routes. Both Redux and Zustand offer different approaches.

**Redux Authentication Implementation:**

```javascript
// authSlice.js
import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { authAPI } from "../api/authAPI";

// Async thunks
export const loginUser = createAsyncThunk(
  "auth/loginUser",
  async ({ email, password }, { rejectWithValue }) => {
    try {
      const response = await authAPI.login({ email, password });

      // Store token in localStorage
      localStorage.setItem("token", response.data.token);
      localStorage.setItem("refreshToken", response.data.refreshToken);

      return response.data;
    } catch (error) {
      return rejectWithValue(error.response?.data?.message || "Login failed");
    }
  }
);

export const logoutUser = createAsyncThunk(
  "auth/logoutUser",
  async (_, { getState }) => {
    const { auth } = getState();

    try {
      await authAPI.logout(auth.refreshToken);
    } catch (error) {
      console.error("Logout API call failed:", error);
    } finally {
      // Always clear local storage
      localStorage.removeItem("token");
      localStorage.removeItem("refreshToken");
    }
  }
);

export const refreshToken = createAsyncThunk(
  "auth/refreshToken",
  async (_, { getState, rejectWithValue }) => {
    const { auth } = getState();

    try {
      const response = await authAPI.refreshToken(auth.refreshToken);

      localStorage.setItem("token", response.data.token);

      return response.data;
    } catch (error) {
      localStorage.removeItem("token");
      localStorage.removeItem("refreshToken");
      return rejectWithValue("Token refresh failed");
    }
  }
);

export const loadUserFromToken = createAsyncThunk(
  "auth/loadUserFromToken",
  async (_, { rejectWithValue }) => {
    const token = localStorage.getItem("token");

    if (!token) {
      return rejectWithValue("No token found");
    }

    try {
      const response = await authAPI.getCurrentUser(token);
      return response.data;
    } catch (error) {
      localStorage.removeItem("token");
      localStorage.removeItem("refreshToken");
      return rejectWithValue("Invalid token");
    }
  }
);

// Auth slice
const authSlice = createSlice({
  name: "auth",
  initialState: {
    user: null,
    token: localStorage.getItem("token"),
    refreshToken: localStorage.getItem("refreshToken"),
    isAuthenticated: false,
    loading: false,
    error: null,
    lastActivity: Date.now(),
  },
  reducers: {
    clearError: (state) => {
      state.error = null;
    },
    updateLastActivity: (state) => {
      state.lastActivity = Date.now();
    },
    updateUser: (state, action) => {
      state.user = { ...state.user, ...action.payload };
    },
  },
  extraReducers: (builder) => {
    builder
      // Login
      .addCase(loginUser.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(loginUser.fulfilled, (state, action) => {
        state.loading = false;
        state.user = action.payload.user;
        state.token = action.payload.token;
        state.refreshToken = action.payload.refreshToken;
        state.isAuthenticated = true;
        state.lastActivity = Date.now();
      })
      .addCase(loginUser.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
        state.isAuthenticated = false;
      })

      // Logout
      .addCase(logoutUser.fulfilled, (state) => {
        state.user = null;
        state.token = null;
        state.refreshToken = null;
        state.isAuthenticated = false;
        state.error = null;
      })

      // Refresh token
      .addCase(refreshToken.fulfilled, (state, action) => {
        state.token = action.payload.token;
        state.lastActivity = Date.now();
      })
      .addCase(refreshToken.rejected, (state) => {
        state.user = null;
        state.token = null;
        state.refreshToken = null;
        state.isAuthenticated = false;
      })

      // Load user from token
      .addCase(loadUserFromToken.fulfilled, (state, action) => {
        state.user = action.payload.user;
        state.isAuthenticated = true;
        state.loading = false;
      })
      .addCase(loadUserFromToken.rejected, (state) => {
        state.token = null;
        state.refreshToken = null;
        state.isAuthenticated = false;
        state.loading = false;
      });
  },
});

export const { clearError, updateLastActivity, updateUser } = authSlice.actions;
export default authSlice.reducer;
```

**Redux Auth Selectors:**

```javascript
// authSelectors.js
import { createSelector } from "@reduxjs/toolkit";

export const selectAuth = (state) => state.auth;
export const selectUser = (state) => state.auth.user;
export const selectIsAuthenticated = (state) => state.auth.isAuthenticated;
export const selectAuthLoading = (state) => state.auth.loading;
export const selectAuthError = (state) => state.auth.error;
export const selectToken = (state) => state.auth.token;

export const selectUserRole = createSelector(
  [selectUser],
  (user) => user?.role || "guest"
);

export const selectUserPermissions = createSelector(
  [selectUser],
  (user) => user?.permissions || []
);

export const selectCanAccess = createSelector(
  [selectUserPermissions],
  (permissions) => (requiredPermission) =>
    permissions.includes(requiredPermission)
);

export const selectSessionExpiry = createSelector([selectAuth], (auth) => {
  if (!auth.token || !auth.lastActivity) return null;

  const sessionTimeout = 30 * 60 * 1000; // 30 minutes
  return auth.lastActivity + sessionTimeout;
});
```

**Zustand Authentication Implementation:**

```javascript
// authStore.js
import { create } from "zustand";
import { persist, subscribeWithSelector } from "zustand/middleware";
import { immer } from "zustand/middleware/immer";
import { authAPI } from "../api/authAPI";

const useAuthStore = create(
  subscribeWithSelector(
    persist(
      immer((set, get) => ({
        // State
        user: null,
        token: null,
        refreshToken: null,
        isAuthenticated: false,
        loading: false,
        error: null,
        lastActivity: Date.now(),

        // Actions
        login: async (credentials) => {
          set((state) => {
            state.loading = true;
            state.error = null;
          });

          try {
            const response = await authAPI.login(credentials);

            set((state) => {
              state.user = response.data.user;
              state.token = response.data.token;
              state.refreshToken = response.data.refreshToken;
              state.isAuthenticated = true;
              state.loading = false;
              state.lastActivity = Date.now();
            });

            return { success: true };
          } catch (error) {
            set((state) => {
              state.loading = false;
              state.error = error.response?.data?.message || "Login failed";
              state.isAuthenticated = false;
            });

            return { success: false, error: error.message };
          }
        },

        logout: async () => {
          const { refreshToken } = get();

          try {
            await authAPI.logout(refreshToken);
          } catch (error) {
            console.error("Logout API call failed:", error);
          }

          set((state) => {
            state.user = null;
            state.token = null;
            state.refreshToken = null;
            state.isAuthenticated = false;
            state.error = null;
          });
        },

        refreshToken: async () => {
          const { refreshToken } = get();

          if (!refreshToken) {
            get().logout();
            return false;
          }

          try {
            const response = await authAPI.refreshToken(refreshToken);

            set((state) => {
              state.token = response.data.token;
              state.lastActivity = Date.now();
            });

            return true;
          } catch (error) {
            get().logout();
            return false;
          }
        },

        loadUserFromToken: async () => {
          const { token } = get();

          if (!token) return false;

          set((state) => {
            state.loading = true;
          });

          try {
            const response = await authAPI.getCurrentUser(token);

            set((state) => {
              state.user = response.data.user;
              state.isAuthenticated = true;
              state.loading = false;
            });

            return true;
          } catch (error) {
            set((state) => {
              state.token = null;
              state.refreshToken = null;
              state.isAuthenticated = false;
              state.loading = false;
            });

            return false;
          }
        },

        updateUser: (userData) => {
          set((state) => {
            state.user = { ...state.user, ...userData };
          });
        },

        updateLastActivity: () => {
          set((state) => {
            state.lastActivity = Date.now();
          });
        },

        clearError: () => {
          set((state) => {
            state.error = null;
          });
        },

        // Computed values
        getUserRole: () => get().user?.role || "guest",
        getUserPermissions: () => get().user?.permissions || [],
        canAccess: (permission) => {
          const permissions = get().getUserPermissions();
          return permissions.includes(permission);
        },
        getSessionExpiry: () => {
          const { token, lastActivity } = get();
          if (!token || !lastActivity) return null;

          const sessionTimeout = 30 * 60 * 1000; // 30 minutes
          return lastActivity + sessionTimeout;
        },
      })),
      {
        name: "auth-storage",
        partialize: (state) => ({
          token: state.token,
          refreshToken: state.refreshToken,
          user: state.user,
          isAuthenticated: state.isAuthenticated,
        }),
      }
    )
  )
);

export default useAuthStore;
```

**Authentication Components:**

```javascript
// Redux Login Component
import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { loginUser, clearError } from "../store/authSlice";
import { selectAuthLoading, selectAuthError } from "../store/authSelectors";

const ReduxLoginForm = () => {
  const dispatch = useDispatch();
  const loading = useSelector(selectAuthLoading);
  const error = useSelector(selectAuthError);

  const [credentials, setCredentials] = useState({
    email: "",
    password: "",
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    dispatch(clearError());

    const result = await dispatch(loginUser(credentials));

    if (loginUser.fulfilled.match(result)) {
      // Handle successful login
      console.log("Login successful");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="email"
        value={credentials.email}
        onChange={(e) =>
          setCredentials((prev) => ({
            ...prev,
            email: e.target.value,
          }))
        }
        placeholder="Email"
        required
      />

      <input
        type="password"
        value={credentials.password}
        onChange={(e) =>
          setCredentials((prev) => ({
            ...prev,
            password: e.target.value,
          }))
        }
        placeholder="Password"
        required
      />

      {error && <div className="error">{error}</div>}

      <button type="submit" disabled={loading}>
        {loading ? "Logging in..." : "Login"}
      </button>
    </form>
  );
};

// Zustand Login Component
const ZustandLoginForm = () => {
  const { login, loading, error, clearError } = useAuthStore();

  const [credentials, setCredentials] = useState({
    email: "",
    password: "",
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    clearError();

    const result = await login(credentials);

    if (result.success) {
      console.log("Login successful");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="email"
        value={credentials.email}
        onChange={(e) =>
          setCredentials((prev) => ({
            ...prev,
            email: e.target.value,
          }))
        }
        placeholder="Email"
        required
      />

      <input
        type="password"
        value={credentials.password}
        onChange={(e) =>
          setCredentials((prev) => ({
            ...prev,
            password: e.target.value,
          }))
        }
        placeholder="Password"
        required
      />

      {error && <div className="error">{error}</div>}

      <button type="submit" disabled={loading}>
        {loading ? "Logging in..." : "Login"}
      </button>
    </form>
  );
};
```

**Protected Route Components:**

```javascript
// Redux Protected Route
import { useSelector } from "react-redux";
import {
  selectIsAuthenticated,
  selectAuthLoading,
} from "../store/authSelectors";

const ReduxProtectedRoute = ({ children, requiredPermission }) => {
  const isAuthenticated = useSelector(selectIsAuthenticated);
  const loading = useSelector(selectAuthLoading);
  const canAccess = useSelector(selectCanAccess);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (!isAuthenticated) {
    return <Navigate to="/login" replace />;
  }

  if (requiredPermission && !canAccess(requiredPermission)) {
    return <div>Access Denied</div>;
  }

  return children;
};

// Zustand Protected Route
const ZustandProtectedRoute = ({ children, requiredPermission }) => {
  const { isAuthenticated, loading, canAccess } = useAuthStore();

  if (loading) {
    return <div>Loading...</div>;
  }

  if (!isAuthenticated) {
    return <Navigate to="/login" replace />;
  }

  if (requiredPermission && !canAccess(requiredPermission)) {
    return <div>Access Denied</div>;
  }

  return children;
};
```

**Session Management:**

```javascript
// Redux Session Manager
import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import {
  refreshToken,
  logoutUser,
  updateLastActivity,
} from "../store/authSlice";
import {
  selectSessionExpiry,
  selectIsAuthenticated,
} from "../store/authSelectors";

const ReduxSessionManager = () => {
  const dispatch = useDispatch();
  const sessionExpiry = useSelector(selectSessionExpiry);
  const isAuthenticated = useSelector(selectIsAuthenticated);

  useEffect(() => {
    if (!isAuthenticated) return;

    const checkSession = () => {
      const now = Date.now();

      if (sessionExpiry && now > sessionExpiry) {
        dispatch(logoutUser());
        return;
      }

      // Refresh token if close to expiry
      if (sessionExpiry && now > sessionExpiry - 5 * 60 * 1000) {
        dispatch(refreshToken());
      }
    };

    const interval = setInterval(checkSession, 60000); // Check every minute

    // Update activity on user interaction
    const updateActivity = () => dispatch(updateLastActivity());

    window.addEventListener("click", updateActivity);
    window.addEventListener("keypress", updateActivity);

    return () => {
      clearInterval(interval);
      window.removeEventListener("click", updateActivity);
      window.removeEventListener("keypress", updateActivity);
    };
  }, [dispatch, sessionExpiry, isAuthenticated]);

  return null;
};

// Zustand Session Manager
const ZustandSessionManager = () => {
  const {
    isAuthenticated,
    getSessionExpiry,
    refreshToken,
    logout,
    updateLastActivity,
  } = useAuthStore();

  useEffect(() => {
    if (!isAuthenticated) return;

    const checkSession = () => {
      const sessionExpiry = getSessionExpiry();
      const now = Date.now();

      if (sessionExpiry && now > sessionExpiry) {
        logout();
        return;
      }

      // Refresh token if close to expiry
      if (sessionExpiry && now > sessionExpiry - 5 * 60 * 1000) {
        refreshToken();
      }
    };

    const interval = setInterval(checkSession, 60000);

    // Update activity on user interaction
    const updateActivity = () => updateLastActivity();

    window.addEventListener("click", updateActivity);
    window.addEventListener("keypress", updateActivity);

    return () => {
      clearInterval(interval);
      window.removeEventListener("click", updateActivity);
      window.removeEventListener("keypress", updateActivity);
    };
  }, [
    isAuthenticated,
    getSessionExpiry,
    refreshToken,
    logout,
    updateLastActivity,
  ]);

  return null;
};
```

**Comparison Summary:**

**Redux Advantages:**

- **Predictable state updates** with actions and reducers
- **Excellent DevTools** for debugging auth flows
- **Middleware support** for complex auth logic
- **Time-travel debugging** for auth state changes
- **Standardized patterns** for team consistency

**Zustand Advantages:**

- **Simpler setup** with less boilerplate
- **Built-in persistence** with middleware
- **Direct async actions** without thunks
- **Smaller bundle size** for auth-only needs
- **Flexible store structure** for auth data

**Best Practices:**

1. **Secure token storage** (consider httpOnly cookies for sensitive apps)
2. **Automatic token refresh** before expiration
3. **Session timeout** handling
4. **Activity tracking** for security
5. **Proper error handling** for auth failures
6. **Route protection** based on authentication state
7. **Logout on token expiry** or invalid tokens
8. **Persist auth state** across browser sessions

---

### Q27: How do you use Redux DevTools for debugging and what are its key features?

**Answer:**
Redux DevTools is a powerful debugging tool that provides time-travel debugging, action inspection, state monitoring, and performance analysis for Redux applications.

**Setting Up Redux DevTools:**

```javascript
// store.js - Basic setup
import { configureStore } from "@reduxjs/toolkit";
import { composeWithDevTools } from "@reduxjs/toolkit/query";

// With Redux Toolkit (DevTools enabled by default)
const store = configureStore({
  reducer: {
    todos: todosReducer,
    auth: authReducer,
    ui: uiReducer,
  },
  // DevTools configuration
  devTools: process.env.NODE_ENV !== "production" && {
    name: "My App",
    trace: true,
    traceLimit: 25,
    actionSanitizer: (action) => ({
      ...action,
      // Hide sensitive data
      ...(action.type === "auth/loginUser/fulfilled" && {
        payload: { ...action.payload, token: "[HIDDEN]" },
      }),
    }),
    stateSanitizer: (state) => ({
      ...state,
      // Hide sensitive state
      auth: {
        ...state.auth,
        token: state.auth.token ? "[HIDDEN]" : null,
        refreshToken: state.auth.refreshToken ? "[HIDDEN]" : null,
      },
    }),
  },
});

// Legacy Redux setup
import { createStore, applyMiddleware, compose } from "redux";
import thunk from "redux-thunk";

const composeEnhancers =
  (typeof window !== "undefined" &&
    window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__) ||
  compose;

const store = createStore(
  rootReducer,
  composeEnhancers(applyMiddleware(thunk))
);
```

**Advanced DevTools Configuration:**

```javascript
// Enhanced DevTools setup with custom options
const store = configureStore({
  reducer: rootReducer,
  devTools: process.env.NODE_ENV !== "production" && {
    // Custom instance name
    name: "TodoApp Redux Store",

    // Enable action stack traces
    trace: true,
    traceLimit: 25,

    // Custom serialization
    serialize: {
      options: {
        undefined: true,
        function: true,
        symbol: true,
      },
    },

    // Action filtering
    predicate: (state, action) => {
      // Don't log certain actions
      return !action.type.includes("@@redux-form");
    },

    // Action sanitization for security
    actionSanitizer: (action) => {
      const sensitiveActions = [
        "auth/loginUser/fulfilled",
        "auth/refreshToken/fulfilled",
      ];

      if (sensitiveActions.includes(action.type)) {
        return {
          ...action,
          payload: {
            ...action.payload,
            token: "[REDACTED]",
            refreshToken: "[REDACTED]",
          },
        };
      }

      return action;
    },

    // State sanitization
    stateSanitizer: (state) => ({
      ...state,
      auth: {
        ...state.auth,
        token: state.auth.token ? "[REDACTED]" : null,
        refreshToken: state.auth.refreshToken ? "[REDACTED]" : null,
      },
      // Hide large data sets in DevTools
      cache:
        Object.keys(state.cache || {}).length > 100
          ? "[LARGE_DATASET_HIDDEN]"
          : state.cache,
    }),

    // Maximum number of actions to keep
    maxAge: 50,

    // Auto-pause on errors
    pauseActionType: "@@PAUSED",
  },
});
```

**Key DevTools Features:**

**1. Action Inspection:**

```javascript
// Custom action creators with better DevTools integration
const addTodoWithMetadata = (text) => ({
  type: "todos/addTodo",
  payload: { text },
  meta: {
    timestamp: Date.now(),
    source: "user_input",
    // Custom metadata for debugging
    debugInfo: {
      component: "TodoForm",
      userAgent: navigator.userAgent,
    },
  },
});

// Enhanced async thunk with better DevTools info
export const fetchTodosWithDebugInfo = createAsyncThunk(
  "todos/fetchTodos",
  async (userId, { getState, requestId, signal, rejectWithValue }) => {
    const startTime = performance.now();

    try {
      const response = await todosAPI.fetchTodos(userId, { signal });

      // Add performance metadata
      const endTime = performance.now();

      return {
        todos: response.data,
        meta: {
          requestId,
          duration: endTime - startTime,
          timestamp: Date.now(),
          cacheHit: false,
        },
      };
    } catch (error) {
      return rejectWithValue({
        message: error.message,
        requestId,
        duration: performance.now() - startTime,
      });
    }
  }
);
```

**2. Time Travel Debugging:**

```javascript
// Middleware for enhanced time travel debugging
const timeTravelMiddleware = (store) => (next) => (action) => {
  // Log state before action
  const prevState = store.getState();

  // Execute action
  const result = next(action);

  // Log state after action
  const nextState = store.getState();

  // Custom logging for specific actions
  if (action.type.includes("todos/")) {
    console.group(`🔄 ${action.type}`);
    console.log("Previous State:", prevState.todos);
    console.log("Action:", action);
    console.log("Next State:", nextState.todos);
    console.groupEnd();
  }

  return result;
};

// Add to store
const store = configureStore({
  reducer: rootReducer,
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(timeTravelMiddleware),
});
```

**3. State Monitoring and Subscriptions:**

```javascript
// Custom DevTools monitoring
class ReduxDevToolsMonitor {
  constructor(store) {
    this.store = store;
    this.subscribers = new Set();
    this.previousState = store.getState();

    // Subscribe to store changes
    store.subscribe(() => {
      const currentState = store.getState();
      this.notifySubscribers(this.previousState, currentState);
      this.previousState = currentState;
    });
  }

  subscribe(callback) {
    this.subscribers.add(callback);

    return () => {
      this.subscribers.delete(callback);
    };
  }

  notifySubscribers(prevState, nextState) {
    this.subscribers.forEach((callback) => {
      callback(prevState, nextState);
    });
  }

  // Monitor specific state slices
  monitorSlice(sliceName, callback) {
    return this.subscribe((prevState, nextState) => {
      const prevSlice = prevState[sliceName];
      const nextSlice = nextState[sliceName];

      if (prevSlice !== nextSlice) {
        callback(prevSlice, nextSlice, sliceName);
      }
    });
  }
}

// Usage
const monitor = new ReduxDevToolsMonitor(store);

// Monitor todos slice
monitor.monitorSlice("todos", (prevTodos, nextTodos, sliceName) => {
  console.log(`${sliceName} changed:`, {
    previous: prevTodos,
    current: nextTodos,
    diff: {
      added: nextTodos.items.length - prevTodos.items.length,
      timestamp: Date.now(),
    },
  });
});
```

**4. Performance Analysis:**

```javascript
// Performance monitoring middleware
const performanceMiddleware = (store) => (next) => (action) => {
  const start = performance.now();

  // Mark the start of action processing
  performance.mark(`action-${action.type}-start`);

  const result = next(action);

  const end = performance.now();
  const duration = end - start;

  // Mark the end and measure
  performance.mark(`action-${action.type}-end`);
  performance.measure(
    `action-${action.type}`,
    `action-${action.type}-start`,
    `action-${action.type}-end`
  );

  // Log slow actions
  if (duration > 10) {
    console.warn(
      `🐌 Slow action detected: ${action.type} took ${duration.toFixed(2)}ms`
    );
  }

  // Send to DevTools with performance data
  if (window.__REDUX_DEVTOOLS_EXTENSION__) {
    window.__REDUX_DEVTOOLS_EXTENSION__.send(
      {
        ...action,
        meta: {
          ...action.meta,
          performance: {
            duration,
            timestamp: Date.now(),
          },
        },
      },
      store.getState()
    );
  }

  return result;
};
```

**5. Custom DevTools Integration:**

```javascript
// Custom DevTools extension integration
class CustomDevTools {
  constructor(store) {
    this.store = store;
    this.devTools = window.__REDUX_DEVTOOLS_EXTENSION__;
    this.actionHistory = [];
    this.stateHistory = [];

    if (this.devTools) {
      this.setupDevTools();
    }
  }

  setupDevTools() {
    // Connect to DevTools
    this.connection = this.devTools.connect({
      name: "Custom Redux Monitor",
      features: {
        pause: true,
        lock: true,
        persist: true,
        export: true,
        import: "custom",
        jump: true,
        skip: true,
        reorder: true,
        dispatch: true,
        test: true,
      },
    });

    // Listen to DevTools messages
    this.connection.subscribe((message) => {
      if (message.type === "DISPATCH") {
        this.handleDevToolsMessage(message);
      }
    });

    // Send initial state
    this.connection.init(this.store.getState());

    // Subscribe to store changes
    this.store.subscribe(() => {
      const state = this.store.getState();
      this.stateHistory.push(state);

      // Keep history limited
      if (this.stateHistory.length > 50) {
        this.stateHistory.shift();
      }
    });
  }

  handleDevToolsMessage(message) {
    switch (message.payload.type) {
      case "JUMP_TO_ACTION":
      case "JUMP_TO_STATE":
        // Handle time travel
        const targetState = this.stateHistory[message.payload.actionId];
        if (targetState) {
          this.store.dispatch({
            type: "@@RESTORE_STATE",
            payload: targetState,
          });
        }
        break;

      case "TOGGLE_ACTION":
        // Handle action toggling
        this.toggleAction(message.payload.id);
        break;

      case "RESET":
        // Reset to initial state
        this.store.dispatch({ type: "@@RESET" });
        break;

      case "COMMIT":
        // Commit current state as new initial state
        this.actionHistory = [];
        this.stateHistory = [this.store.getState()];
        break;
    }
  }

  logAction(action) {
    this.actionHistory.push({
      action,
      timestamp: Date.now(),
      state: this.store.getState(),
    });

    if (this.connection) {
      this.connection.send(action, this.store.getState());
    }
  }

  toggleAction(actionId) {
    // Implementation for toggling actions
    const targetAction = this.actionHistory[actionId];
    if (targetAction) {
      // Replay all actions except the toggled one
      this.replayActions(
        this.actionHistory.filter((_, index) => index !== actionId)
      );
    }
  }

  replayActions(actions) {
    // Reset to initial state and replay actions
    this.store.dispatch({ type: "@@RESET" });
    actions.forEach(({ action }) => {
      this.store.dispatch(action);
    });
  }
}

// Usage
const customDevTools = new CustomDevTools(store);

// Enhanced action logging
const devToolsMiddleware = (store) => (next) => (action) => {
  const result = next(action);
  customDevTools.logAction(action);
  return result;
};
```

**6. Testing with DevTools:**

```javascript
// DevTools testing utilities
class DevToolsTestHelper {
  constructor(store) {
    this.store = store;
    this.actionLog = [];
    this.stateSnapshots = [];
  }

  // Record actions for testing
  startRecording() {
    this.actionLog = [];
    this.stateSnapshots = [this.store.getState()];

    this.unsubscribe = this.store.subscribe(() => {
      this.stateSnapshots.push(this.store.getState());
    });
  }

  stopRecording() {
    if (this.unsubscribe) {
      this.unsubscribe();
    }

    return {
      actions: this.actionLog,
      states: this.stateSnapshots,
    };
  }

  // Export recorded session
  exportSession() {
    return {
      actions: this.actionLog,
      initialState: this.stateSnapshots[0],
      finalState: this.stateSnapshots[this.stateSnapshots.length - 1],
      timestamp: Date.now(),
    };
  }

  // Import and replay session
  importSession(session) {
    // Reset store to initial state
    this.store.dispatch({
      type: "@@RESTORE_STATE",
      payload: session.initialState,
    });

    // Replay actions
    session.actions.forEach((action) => {
      this.store.dispatch(action);
    });
  }

  // Generate test cases from recorded actions
  generateTests() {
    return this.actionLog.map((action, index) => ({
      description: `should handle ${action.type}`,
      action,
      expectedState: this.stateSnapshots[index + 1],
    }));
  }
}

// Usage in tests
const testHelper = new DevToolsTestHelper(store);

describe("Redux DevTools Integration", () => {
  it("should record and replay actions", () => {
    testHelper.startRecording();

    // Perform actions
    store.dispatch(addTodo("Test todo"));
    store.dispatch(toggleTodo(1));

    const session = testHelper.stopRecording();

    expect(session.actions).toHaveLength(2);
    expect(session.states).toHaveLength(3); // initial + 2 actions
  });

  it("should generate test cases from recorded session", () => {
    const tests = testHelper.generateTests();

    tests.forEach((test) => {
      const newStore = createStore(reducer, test.action.prevState);
      newStore.dispatch(test.action);

      expect(newStore.getState()).toEqual(test.expectedState);
    });
  });
});
```

**Best Practices for DevTools:**

1. **Sanitize sensitive data** in production builds
2. **Limit action history** to prevent memory issues
3. **Use meaningful action types** for better debugging
4. **Add metadata** to actions for context
5. **Configure trace limits** for performance
6. **Use action filtering** to reduce noise
7. **Implement custom monitors** for specific debugging needs
8. **Export/import state** for bug reproduction

**DevTools vs Zustand Debugging:**

```javascript
// Zustand DevTools integration
import { devtools } from "zustand/middleware";

const useStore = create(
  devtools(
    (set, get) => ({
      count: 0,
      increment: () =>
        set((state) => ({ count: state.count + 1 }), false, "increment"),
      decrement: () =>
        set((state) => ({ count: state.count - 1 }), false, "decrement"),
    }),
    {
      name: "counter-store",
      serialize: { options: true },
    }
  )
);
```

**Key Benefits:**

- **Time-travel debugging** for complex state changes
- **Action replay** for bug reproduction
- **Performance monitoring** and optimization
- **State inspection** at any point in time
- **Hot reloading** with state preservation
- **Export/import** for sharing debugging sessions
- **Custom monitoring** for specific use cases

---

### Q28: How do you handle loading states and error handling patterns in Redux vs Zustand?

**Answer:**
Proper loading states and error handling are crucial for good user experience. Both Redux and Zustand offer different approaches to manage these patterns effectively.

**Redux Loading States and Error Handling:**

```javascript
// Enhanced slice with comprehensive loading and error handling
import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";

// Async thunk with detailed error handling
export const fetchTodos = createAsyncThunk(
  "todos/fetchTodos",
  async (params, { rejectWithValue, signal, getState }) => {
    try {
      const response = await todosAPI.fetchTodos(params, { signal });
      return response.data;
    } catch (error) {
      // Handle different error types
      if (error.name === "AbortError") {
        return rejectWithValue({
          type: "CANCELLED",
          message: "Request cancelled",
        });
      }

      if (error.response?.status === 401) {
        return rejectWithValue({
          type: "UNAUTHORIZED",
          message: "Please log in again",
          shouldRedirect: true,
        });
      }

      if (error.response?.status >= 500) {
        return rejectWithValue({
          type: "SERVER_ERROR",
          message: "Server error. Please try again later.",
          retryable: true,
        });
      }

      return rejectWithValue({
        type: "UNKNOWN_ERROR",
        message: error.message || "An unexpected error occurred",
        retryable: false,
      });
    }
  }
);

export const createTodo = createAsyncThunk(
  "todos/createTodo",
  async (todoData, { rejectWithValue, dispatch }) => {
    try {
      const response = await todosAPI.createTodo(todoData);

      // Optimistic update success
      dispatch(todosSlice.actions.addTodoOptimistic(response.data));

      return response.data;
    } catch (error) {
      // Revert optimistic update
      dispatch(todosSlice.actions.revertOptimisticAdd(todoData.tempId));

      return rejectWithValue({
        type: "CREATE_FAILED",
        message: error.response?.data?.message || "Failed to create todo",
        originalData: todoData,
      });
    }
  }
);

// Enhanced todos slice with loading patterns
const todosSlice = createSlice({
  name: "todos",
  initialState: {
    items: [],
    // Multiple loading states for different operations
    loading: {
      fetch: false,
      create: false,
      update: false,
      delete: false,
    },
    // Structured error handling
    errors: {
      fetch: null,
      create: null,
      update: null,
      delete: null,
      global: null,
    },
    // Request metadata
    lastFetch: null,
    retryCount: 0,
    // Optimistic updates tracking
    optimisticUpdates: new Set(),
  },
  reducers: {
    clearError: (state, action) => {
      const { errorType } = action.payload;
      if (errorType) {
        state.errors[errorType] = null;
      } else {
        // Clear all errors
        Object.keys(state.errors).forEach((key) => {
          state.errors[key] = null;
        });
      }
    },

    setGlobalError: (state, action) => {
      state.errors.global = action.payload;
    },

    addTodoOptimistic: (state, action) => {
      const todo = { ...action.payload, optimistic: true };
      state.items.push(todo);
      state.optimisticUpdates.add(todo.id);
    },

    revertOptimisticAdd: (state, action) => {
      const tempId = action.payload;
      state.items = state.items.filter((todo) => todo.tempId !== tempId);
      state.optimisticUpdates.delete(tempId);
    },

    incrementRetryCount: (state) => {
      state.retryCount += 1;
    },

    resetRetryCount: (state) => {
      state.retryCount = 0;
    },
  },
  extraReducers: (builder) => {
    builder
      // Fetch todos
      .addCase(fetchTodos.pending, (state) => {
        state.loading.fetch = true;
        state.errors.fetch = null;
      })
      .addCase(fetchTodos.fulfilled, (state, action) => {
        state.loading.fetch = false;
        state.items = action.payload;
        state.lastFetch = Date.now();
        state.retryCount = 0;
      })
      .addCase(fetchTodos.rejected, (state, action) => {
        state.loading.fetch = false;
        state.errors.fetch = action.payload;

        // Auto-retry for retryable errors
        if (action.payload?.retryable && state.retryCount < 3) {
          state.retryCount += 1;
        }
      })

      // Create todo
      .addCase(createTodo.pending, (state) => {
        state.loading.create = true;
        state.errors.create = null;
      })
      .addCase(createTodo.fulfilled, (state, action) => {
        state.loading.create = false;
        // Remove optimistic update and add real data
        const optimisticIndex = state.items.findIndex(
          (item) => item.tempId === action.meta.arg.tempId
        );
        if (optimisticIndex !== -1) {
          state.items[optimisticIndex] = action.payload;
          state.optimisticUpdates.delete(action.payload.id);
        }
      })
      .addCase(createTodo.rejected, (state, action) => {
        state.loading.create = false;
        state.errors.create = action.payload;
      });
  },
});

export const {
  clearError,
  setGlobalError,
  addTodoOptimistic,
  revertOptimisticAdd,
  incrementRetryCount,
  resetRetryCount,
} = todosSlice.actions;

export default todosSlice.reducer;
```

**Redux Loading and Error Selectors:**

```javascript
// Enhanced selectors for loading and error states
import { createSelector } from "@reduxjs/toolkit";

// Basic selectors
export const selectTodos = (state) => state.todos.items;
export const selectTodosLoading = (state) => state.todos.loading;
export const selectTodosErrors = (state) => state.todos.errors;
export const selectRetryCount = (state) => state.todos.retryCount;

// Computed loading states
export const selectIsAnyLoading = createSelector(
  [selectTodosLoading],
  (loading) => Object.values(loading).some(Boolean)
);

export const selectLoadingByType = createSelector(
  [selectTodosLoading],
  (loading) => (type) => loading[type] || false
);

// Error selectors
export const selectHasAnyError = createSelector([selectTodosErrors], (errors) =>
  Object.values(errors).some((error) => error !== null)
);

export const selectErrorByType = createSelector(
  [selectTodosErrors],
  (errors) => (type) => errors[type]
);

export const selectRetryableErrors = createSelector(
  [selectTodosErrors],
  (errors) =>
    Object.entries(errors)
      .filter(([_, error]) => error?.retryable)
      .map(([type, error]) => ({ type, error }))
);

// Combined loading and error states
export const selectTodosStatus = createSelector(
  [selectTodosLoading, selectTodosErrors, selectRetryCount],
  (loading, errors, retryCount) => ({
    isLoading: Object.values(loading).some(Boolean),
    hasError: Object.values(errors).some((error) => error !== null),
    canRetry: retryCount < 3,
    retryCount,
    loadingStates: loading,
    errors,
  })
);
```

**Zustand Loading States and Error Handling:**

```javascript
// Comprehensive Zustand store with loading and error handling
import { create } from "zustand";
import { immer } from "zustand/middleware/immer";
import { subscribeWithSelector } from "zustand/middleware";

const useTodosStore = create(
  subscribeWithSelector(
    immer((set, get) => ({
      // State
      items: [],
      loading: {
        fetch: false,
        create: false,
        update: false,
        delete: false,
      },
      errors: {
        fetch: null,
        create: null,
        update: null,
        delete: null,
        global: null,
      },
      retryCount: 0,
      lastFetch: null,
      optimisticUpdates: new Set(),

      // Actions
      fetchTodos: async (params = {}) => {
        set((state) => {
          state.loading.fetch = true;
          state.errors.fetch = null;
        });

        try {
          const response = await todosAPI.fetchTodos(params);

          set((state) => {
            state.items = response.data;
            state.loading.fetch = false;
            state.lastFetch = Date.now();
            state.retryCount = 0;
          });

          return { success: true, data: response.data };
        } catch (error) {
          const errorInfo = get().handleError(error, "fetch");

          set((state) => {
            state.loading.fetch = false;
            state.errors.fetch = errorInfo;

            if (errorInfo.retryable && state.retryCount < 3) {
              state.retryCount += 1;
            }
          });

          return { success: false, error: errorInfo };
        }
      },

      createTodo: async (todoData) => {
        const tempId = `temp_${Date.now()}`;
        const optimisticTodo = { ...todoData, id: tempId, optimistic: true };

        // Optimistic update
        set((state) => {
          state.items.push(optimisticTodo);
          state.optimisticUpdates.add(tempId);
          state.loading.create = true;
          state.errors.create = null;
        });

        try {
          const response = await todosAPI.createTodo(todoData);

          set((state) => {
            // Replace optimistic todo with real one
            const index = state.items.findIndex((item) => item.id === tempId);
            if (index !== -1) {
              state.items[index] = response.data;
            }
            state.optimisticUpdates.delete(tempId);
            state.loading.create = false;
          });

          return { success: true, data: response.data };
        } catch (error) {
          // Revert optimistic update
          set((state) => {
            state.items = state.items.filter((item) => item.id !== tempId);
            state.optimisticUpdates.delete(tempId);
            state.loading.create = false;
            state.errors.create = get().handleError(error, "create");
          });

          return { success: false, error: error.message };
        }
      },

      updateTodo: async (id, updates) => {
        const originalTodo = get().items.find((item) => item.id === id);

        // Optimistic update
        set((state) => {
          const index = state.items.findIndex((item) => item.id === id);
          if (index !== -1) {
            state.items[index] = { ...state.items[index], ...updates };
          }
          state.loading.update = true;
          state.errors.update = null;
        });

        try {
          const response = await todosAPI.updateTodo(id, updates);

          set((state) => {
            const index = state.items.findIndex((item) => item.id === id);
            if (index !== -1) {
              state.items[index] = response.data;
            }
            state.loading.update = false;
          });

          return { success: true, data: response.data };
        } catch (error) {
          // Revert optimistic update
          set((state) => {
            const index = state.items.findIndex((item) => item.id === id);
            if (index !== -1 && originalTodo) {
              state.items[index] = originalTodo;
            }
            state.loading.update = false;
            state.errors.update = get().handleError(error, "update");
          });

          return { success: false, error: error.message };
        }
      },

      deleteTodo: async (id) => {
        const originalTodo = get().items.find((item) => item.id === id);

        // Optimistic removal
        set((state) => {
          state.items = state.items.filter((item) => item.id !== id);
          state.loading.delete = true;
          state.errors.delete = null;
        });

        try {
          await todosAPI.deleteTodo(id);

          set((state) => {
            state.loading.delete = false;
          });

          return { success: true };
        } catch (error) {
          // Revert optimistic removal
          set((state) => {
            if (originalTodo) {
              state.items.push(originalTodo);
              state.items.sort((a, b) => a.createdAt - b.createdAt);
            }
            state.loading.delete = false;
            state.errors.delete = get().handleError(error, "delete");
          });

          return { success: false, error: error.message };
        }
      },

      // Error handling utility
      handleError: (error, operation) => {
        if (error.name === "AbortError") {
          return {
            type: "CANCELLED",
            message: "Request cancelled",
            retryable: false,
          };
        }

        if (error.response?.status === 401) {
          return {
            type: "UNAUTHORIZED",
            message: "Please log in again",
            shouldRedirect: true,
            retryable: false,
          };
        }

        if (error.response?.status >= 500) {
          return {
            type: "SERVER_ERROR",
            message: "Server error. Please try again later.",
            retryable: true,
            operation,
          };
        }

        return {
          type: "UNKNOWN_ERROR",
          message: error.message || "An unexpected error occurred",
          retryable: false,
          operation,
        };
      },

      // Utility actions
      clearError: (errorType) => {
        set((state) => {
          if (errorType) {
            state.errors[errorType] = null;
          } else {
            Object.keys(state.errors).forEach((key) => {
              state.errors[key] = null;
            });
          }
        });
      },

      retry: async (operation, ...args) => {
        const { retryCount } = get();

        if (retryCount >= 3) {
          return { success: false, error: "Maximum retry attempts reached" };
        }

        // Clear previous error
        get().clearError(operation);

        // Retry the operation
        switch (operation) {
          case "fetch":
            return get().fetchTodos(...args);
          case "create":
            return get().createTodo(...args);
          case "update":
            return get().updateTodo(...args);
          case "delete":
            return get().deleteTodo(...args);
          default:
            return { success: false, error: "Unknown operation" };
        }
      },

      // Computed getters
      getLoadingState: () => {
        const { loading } = get();
        return {
          isAnyLoading: Object.values(loading).some(Boolean),
          loadingStates: loading,
        };
      },

      getErrorState: () => {
        const { errors } = get();
        return {
          hasAnyError: Object.values(errors).some((error) => error !== null),
          errors,
          retryableErrors: Object.entries(errors)
            .filter(([_, error]) => error?.retryable)
            .map(([type, error]) => ({ type, error })),
        };
      },
    }))
  )
);

export default useTodosStore;
```

**Loading and Error UI Components:**

```javascript
// Redux Loading Component
import React from "react";
import { useSelector, useDispatch } from "react-redux";
import {
  selectTodosStatus,
  selectRetryableErrors,
  clearError,
} from "../store/todosSlice";

const ReduxTodoList = () => {
  const dispatch = useDispatch();
  const todos = useSelector(selectTodos);
  const status = useSelector(selectTodosStatus);
  const retryableErrors = useSelector(selectRetryableErrors);

  const handleRetry = (errorType) => {
    dispatch(clearError({ errorType }));

    switch (errorType) {
      case "fetch":
        dispatch(fetchTodos());
        break;
      // Handle other retry cases
    }
  };

  if (status.loadingStates.fetch) {
    return (
      <div className="loading-container">
        <div className="spinner" />
        <p>Loading todos...</p>
      </div>
    );
  }

  if (status.errors.fetch) {
    return (
      <div className="error-container">
        <h3>Error Loading Todos</h3>
        <p>{status.errors.fetch.message}</p>
        {status.errors.fetch.retryable && status.canRetry && (
          <button onClick={() => handleRetry("fetch")}>
            Retry ({3 - status.retryCount} attempts left)
          </button>
        )}
      </div>
    );
  }

  return (
    <div>
      {/* Global error display */}
      {retryableErrors.length > 0 && (
        <div className="retry-banner">
          <p>Some operations failed. Would you like to retry?</p>
          {retryableErrors.map(({ type, error }) => (
            <button key={type} onClick={() => handleRetry(type)}>
              Retry {type}
            </button>
          ))}
        </div>
      )}

      {/* Todo list */}
      <ul>
        {todos.map((todo) => (
          <li key={todo.id} className={todo.optimistic ? "optimistic" : ""}>
            {todo.text}
            {status.loadingStates.update && (
              <span className="updating">Updating...</span>
            )}
          </li>
        ))}
      </ul>

      {/* Create todo loading */}
      {status.loadingStates.create && (
        <div className="creating-indicator">Creating new todo...</div>
      )}
    </div>
  );
};

// Zustand Loading Component
const ZustandTodoList = () => {
  const {
    items: todos,
    loading,
    errors,
    retry,
    clearError,
    getLoadingState,
    getErrorState,
  } = useTodosStore();

  const loadingState = getLoadingState();
  const errorState = getErrorState();

  const handleRetry = async (operation) => {
    const result = await retry(operation);
    if (!result.success) {
      console.error("Retry failed:", result.error);
    }
  };

  if (loading.fetch) {
    return (
      <div className="loading-container">
        <div className="spinner" />
        <p>Loading todos...</p>
      </div>
    );
  }

  if (errors.fetch) {
    return (
      <div className="error-container">
        <h3>Error Loading Todos</h3>
        <p>{errors.fetch.message}</p>
        {errors.fetch.retryable && (
          <button onClick={() => handleRetry("fetch")}>Retry</button>
        )}
      </div>
    );
  }

  return (
    <div>
      {/* Error notifications */}
      {errorState.retryableErrors.length > 0 && (
        <div className="error-notifications">
          {errorState.retryableErrors.map(({ type, error }) => (
            <div key={type} className="error-notification">
              <p>{error.message}</p>
              <button onClick={() => handleRetry(type)}>Retry {type}</button>
              <button onClick={() => clearError(type)}>×</button>
            </div>
          ))}
        </div>
      )}

      {/* Todo list */}
      <ul>
        {todos.map((todo) => (
          <li key={todo.id} className={todo.optimistic ? "optimistic" : ""}>
            {todo.text}
          </li>
        ))}
      </ul>

      {/* Loading indicators */}
      {loadingState.isAnyLoading && (
        <div className="loading-overlay">
          {loading.create && <p>Creating todo...</p>}
          {loading.update && <p>Updating todo...</p>}
          {loading.delete && <p>Deleting todo...</p>}
        </div>
      )}
    </div>
  );
};
```

**Advanced Error Boundary Integration:**

```javascript
// Error Boundary for Redux
class ReduxErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  componentDidCatch(error, errorInfo) {
    // Log error to Redux store
    this.props.dispatch(
      setGlobalError({
        type: "COMPONENT_ERROR",
        message: error.message,
        stack: error.stack,
        componentStack: errorInfo.componentStack,
      })
    );
  }

  render() {
    if (this.state.hasError) {
      return (
        <div className="error-boundary">
          <h2>Something went wrong</h2>
          <p>{this.state.error?.message}</p>
          <button onClick={() => window.location.reload()}>Reload Page</button>
        </div>
      );
    }

    return this.props.children;
  }
}

// Zustand Error Boundary
class ZustandErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  componentDidCatch(error, errorInfo) {
    // Log error to Zustand store
    useTodosStore.getState().setGlobalError({
      type: "COMPONENT_ERROR",
      message: error.message,
      stack: error.stack,
      componentStack: errorInfo.componentStack,
    });
  }

  render() {
    if (this.state.hasError) {
      return (
        <div className="error-boundary">
          <h2>Something went wrong</h2>
          <p>{this.state.error?.message}</p>
          <button
            onClick={() => this.setState({ hasError: false, error: null })}
          >
            Try Again
          </button>
        </div>
      );
    }

    return this.props.children;
  }
}
```

**Comparison Summary:**

**Redux Advantages:**

- **Structured error handling** with action types
- **Predictable loading states** through reducers
- **Time-travel debugging** for error scenarios
- **Middleware integration** for global error handling
- **Standardized patterns** for team consistency

**Zustand Advantages:**

- **Simpler error handling** with direct state updates
- **Flexible loading patterns** without boilerplate
- **Built-in optimistic updates** with easy rollback
- **Direct async actions** without thunk complexity
- **Smaller bundle size** for error handling logic

**Best Practices:**

1. **Separate loading states** for different operations
2. **Structured error objects** with type and metadata
3. **Optimistic updates** with rollback capability
4. **Retry mechanisms** for transient failures
5. **Error boundaries** for component-level errors
6. **User-friendly error messages** with actionable steps
7. **Loading indicators** for better UX
8. **Error persistence** across component re-renders

---

### Q29: What are the differences between Redux Thunk and Redux Saga? When would you use each?

**Answer:**
Redux Thunk and Redux Saga are both middleware solutions for handling side effects in Redux, but they use fundamentally different approaches and are suited for different use cases.

**Redux Thunk Overview:**

Redux Thunk is the simplest middleware that allows action creators to return functions instead of plain action objects.

```javascript
// Basic Redux Thunk setup
import { configureStore } from "@reduxjs/toolkit";
import thunk from "redux-thunk";
import rootReducer from "./reducers";

const store = configureStore({
  reducer: rootReducer,
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      thunk: {
        extraArgument: { api, logger },
      },
    }),
});

// Simple thunk action creator
const fetchUser = (userId) => {
  return async (dispatch, getState, { api }) => {
    dispatch({ type: "FETCH_USER_START" });

    try {
      const user = await api.fetchUser(userId);
      dispatch({ type: "FETCH_USER_SUCCESS", payload: user });
    } catch (error) {
      dispatch({ type: "FETCH_USER_ERROR", payload: error.message });
    }
  };
};

// Complex thunk with conditional logic
const fetchUserIfNeeded = (userId) => {
  return async (dispatch, getState) => {
    const state = getState();
    const user = state.users.byId[userId];

    // Only fetch if user doesn't exist or is stale
    if (!user || Date.now() - user.lastFetch > 300000) {
      return dispatch(fetchUser(userId));
    }

    return Promise.resolve(user);
  };
};

// Thunk with error handling and retry logic
const fetchUserWithRetry = (userId, retryCount = 0) => {
  return async (dispatch, getState, { api }) => {
    const maxRetries = 3;

    try {
      dispatch({ type: "FETCH_USER_START", payload: { userId, retryCount } });

      const user = await api.fetchUser(userId);
      dispatch({ type: "FETCH_USER_SUCCESS", payload: user });

      return user;
    } catch (error) {
      if (retryCount < maxRetries && error.status >= 500) {
        // Exponential backoff
        const delay = Math.pow(2, retryCount) * 1000;

        setTimeout(() => {
          dispatch(fetchUserWithRetry(userId, retryCount + 1));
        }, delay);
      } else {
        dispatch({
          type: "FETCH_USER_ERROR",
          payload: { error: error.message, userId, retryCount },
        });
      }

      throw error;
    }
  };
};

// Thunk with cancellation support
const createCancellableThunk = (userId) => {
  return (dispatch, getState, { api }) => {
    const abortController = new AbortController();

    const promise = api
      .fetchUser(userId, {
        signal: abortController.signal,
      })
      .then(
        (user) => dispatch({ type: "FETCH_USER_SUCCESS", payload: user }),
        (error) => {
          if (error.name !== "AbortError") {
            dispatch({ type: "FETCH_USER_ERROR", payload: error.message });
          }
        }
      );

    // Return both promise and cancel function
    return {
      promise,
      cancel: () => abortController.abort(),
    };
  };
};
```

**Redux Saga Overview:**

Redux Saga uses ES6 generator functions to create more powerful and testable side effects.

```javascript
// Redux Saga setup
import { configureStore } from "@reduxjs/toolkit";
import createSagaMiddleware from "redux-saga";
import { all, fork } from "redux-saga/effects";
import rootReducer from "./reducers";
import { userSagas } from "./sagas";

const sagaMiddleware = createSagaMiddleware({
  context: {
    api: apiService,
    logger: loggerService,
  },
});

const store = configureStore({
  reducer: rootReducer,
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({ thunk: false }).concat(sagaMiddleware),
});

// Root saga
function* rootSaga() {
  yield all([
    fork(userSagas),
    fork(notificationSagas),
    fork(backgroundSyncSagas),
  ]);
}

sagaMiddleware.run(rootSaga);

// Basic saga
import {
  call,
  put,
  takeEvery,
  takeLatest,
  select,
  race,
  delay,
  cancel,
  fork,
  cancelled,
} from "redux-saga/effects";

function* fetchUserSaga(action) {
  try {
    yield put({ type: "FETCH_USER_START" });

    const user = yield call(api.fetchUser, action.payload.userId);
    yield put({ type: "FETCH_USER_SUCCESS", payload: user });
  } catch (error) {
    yield put({ type: "FETCH_USER_ERROR", payload: error.message });
  }
}

// Advanced saga with race conditions and timeouts
function* fetchUserWithTimeoutSaga(action) {
  try {
    const { response, timeout } = yield race({
      response: call(api.fetchUser, action.payload.userId),
      timeout: delay(5000), // 5 second timeout
    });

    if (timeout) {
      yield put({
        type: "FETCH_USER_ERROR",
        payload: "Request timed out",
      });
    } else {
      yield put({ type: "FETCH_USER_SUCCESS", payload: response });
    }
  } catch (error) {
    yield put({ type: "FETCH_USER_ERROR", payload: error.message });
  }
}

// Saga with retry logic and exponential backoff
function* fetchUserWithRetrySaga(action) {
  const maxRetries = 3;
  let retryCount = 0;

  while (retryCount <= maxRetries) {
    try {
      yield put({
        type: "FETCH_USER_START",
        payload: { userId: action.payload.userId, retryCount },
      });

      const user = yield call(api.fetchUser, action.payload.userId);
      yield put({ type: "FETCH_USER_SUCCESS", payload: user });

      return; // Success, exit retry loop
    } catch (error) {
      retryCount++;

      if (retryCount > maxRetries || error.status < 500) {
        yield put({
          type: "FETCH_USER_ERROR",
          payload: { error: error.message, retryCount },
        });
        return;
      }

      // Exponential backoff
      const delayTime = Math.pow(2, retryCount - 1) * 1000;
      yield delay(delayTime);
    }
  }
}

// Saga with cancellation support
function* fetchUserCancellableSaga(action) {
  try {
    yield put({ type: "FETCH_USER_START" });

    const user = yield call(api.fetchUser, action.payload.userId);
    yield put({ type: "FETCH_USER_SUCCESS", payload: user });
  } catch (error) {
    if (yield cancelled()) {
      yield put({ type: "FETCH_USER_CANCELLED" });
    } else {
      yield put({ type: "FETCH_USER_ERROR", payload: error.message });
    }
  } finally {
    if (yield cancelled()) {
      // Cleanup logic
      console.log("Fetch user saga was cancelled");
    }
  }
}

// Background sync saga
function* backgroundSyncSaga() {
  while (true) {
    try {
      // Check if user is online
      const isOnline = yield select(getIsOnline);

      if (isOnline) {
        // Get pending sync items
        const pendingItems = yield select(getPendingSyncItems);

        if (pendingItems.length > 0) {
          yield put({ type: "SYNC_START" });

          // Process items in parallel with concurrency limit
          yield all(
            pendingItems.slice(0, 5).map((item) => fork(syncItemSaga, item))
          );

          yield put({ type: "SYNC_COMPLETE" });
        }
      }

      // Wait 30 seconds before next sync check
      yield delay(30000);
    } catch (error) {
      console.error("Background sync error:", error);
      yield delay(60000); // Wait longer on error
    }
  }
}

// Complex flow control saga
function* userRegistrationFlowSaga(action) {
  const { email, password, profile } = action.payload;

  try {
    // Step 1: Validate email
    yield put({ type: "VALIDATE_EMAIL_START" });
    const emailValid = yield call(api.validateEmail, email);

    if (!emailValid) {
      yield put({ type: "REGISTRATION_ERROR", payload: "Invalid email" });
      return;
    }

    // Step 2: Create user account
    yield put({ type: "CREATE_ACCOUNT_START" });
    const user = yield call(api.createUser, { email, password });

    // Step 3: Upload profile data
    yield put({ type: "UPLOAD_PROFILE_START" });
    const updatedUser = yield call(api.updateProfile, user.id, profile);

    // Step 4: Send welcome email
    yield fork(sendWelcomeEmailSaga, user.id);

    // Step 5: Initialize user preferences
    yield fork(initializeUserPreferencesSaga, user.id);

    yield put({
      type: "REGISTRATION_SUCCESS",
      payload: updatedUser,
    });

    // Navigate to dashboard
    yield put({ type: "NAVIGATE_TO_DASHBOARD" });
  } catch (error) {
    yield put({
      type: "REGISTRATION_ERROR",
      payload: error.message,
    });
  }
}

// Watcher sagas
function* userSagas() {
  yield takeEvery("FETCH_USER_REQUEST", fetchUserSaga);
  yield takeLatest("FETCH_USER_WITH_TIMEOUT", fetchUserWithTimeoutSaga);
  yield takeEvery("FETCH_USER_WITH_RETRY", fetchUserWithRetrySaga);
  yield takeLatest("REGISTER_USER", userRegistrationFlowSaga);

  // Cancellable saga pattern
  yield takeLatest("FETCH_USER_CANCELLABLE", function* (action) {
    const task = yield fork(fetchUserCancellableSaga, action);

    // Listen for cancel action
    yield take("CANCEL_FETCH_USER");
    yield cancel(task);
  });
}

export { userSagas };
```

**Testing Comparison:**

```javascript
// Testing Redux Thunk
import configureMockStore from "redux-mock-store";
import thunk from "redux-thunk";
import { fetchUser } from "./userActions";

const middlewares = [thunk];
const mockStore = configureMockStore(middlewares);

describe("fetchUser thunk", () => {
  it("should dispatch success action when API call succeeds", async () => {
    const mockApi = {
      fetchUser: jest.fn().mockResolvedValue({ id: 1, name: "John" }),
    };

    const store = mockStore({});

    await store.dispatch(fetchUser(1));

    const actions = store.getActions();
    expect(actions[0]).toEqual({ type: "FETCH_USER_START" });
    expect(actions[1]).toEqual({
      type: "FETCH_USER_SUCCESS",
      payload: { id: 1, name: "John" },
    });
  });
});

// Testing Redux Saga
import { runSaga } from "redux-saga";
import { fetchUserSaga } from "./userSagas";

describe("fetchUserSaga", () => {
  it("should dispatch success action when API call succeeds", async () => {
    const dispatched = [];
    const mockApi = {
      fetchUser: jest.fn().mockResolvedValue({ id: 1, name: "John" }),
    };

    await runSaga(
      {
        dispatch: (action) => dispatched.push(action),
        getState: () => ({}),
      },
      fetchUserSaga,
      { payload: { userId: 1 } }
    ).toPromise();

    expect(dispatched[0]).toEqual({ type: "FETCH_USER_START" });
    expect(dispatched[1]).toEqual({
      type: "FETCH_USER_SUCCESS",
      payload: { id: 1, name: "John" },
    });
  });

  // Testing generator step by step
  it("should handle API call step by step", () => {
    const generator = fetchUserSaga({ payload: { userId: 1 } });

    expect(generator.next().value).toEqual(put({ type: "FETCH_USER_START" }));

    expect(generator.next().value).toEqual(call(api.fetchUser, 1));

    expect(generator.next({ id: 1, name: "John" }).value).toEqual(
      put({ type: "FETCH_USER_SUCCESS", payload: { id: 1, name: "John" } })
    );

    expect(generator.next().done).toBe(true);
  });
});
```

**When to Use Redux Thunk:**

**Advantages:**

- **Simple learning curve** - easy to understand and implement
- **Lightweight** - minimal bundle size impact
- **Direct async/await support** - familiar JavaScript patterns
- **Good for simple side effects** - API calls, basic async logic
- **Less boilerplate** for straightforward use cases
- **Built into Redux Toolkit** by default

**Best for:**

- Simple applications with basic async needs
- Teams new to Redux
- Straightforward API calls and data fetching
- When bundle size is a primary concern
- Applications without complex flow control

**When to Use Redux Saga:**

**Advantages:**

- **Powerful flow control** - complex async workflows
- **Cancellation support** - built-in task cancellation
- **Racing and parallel execution** - advanced concurrency patterns
- **Excellent testing** - step-by-step generator testing
- **Background tasks** - long-running processes
- **Declarative effects** - more predictable side effects

**Best for:**

- Complex applications with intricate async flows
- Applications requiring background synchronization
- When you need advanced cancellation and racing
- Teams comfortable with generator functions
- Applications with complex business logic
- When testing is a high priority

**Comparison Summary:**

| Feature              | Redux Thunk              | Redux Saga           |
| -------------------- | ------------------------ | -------------------- |
| **Learning Curve**   | Easy                     | Moderate to Hard     |
| **Bundle Size**      | Small (~2KB)             | Larger (~25KB)       |
| **Async Patterns**   | Promises/async-await     | Generators           |
| **Cancellation**     | Manual (AbortController) | Built-in             |
| **Testing**          | Standard async testing   | Step-by-step testing |
| **Flow Control**     | Limited                  | Advanced             |
| **Background Tasks** | Difficult                | Excellent            |
| **Racing/Parallel**  | Manual Promise.race      | Built-in effects     |
| **Debugging**        | Standard debugging       | Redux-Saga dev tools |
| **Community**        | Large                    | Smaller but active   |

**Migration Considerations:**

You can use both Redux Thunk and Redux Saga in the same application:

```javascript
// Using both middlewares
const store = configureStore({
  reducer: rootReducer,
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(sagaMiddleware),
  // Thunk is included by default in getDefaultMiddleware
});

// Gradually migrate from thunks to sagas
const fetchUserThunk = (userId) => async (dispatch) => {
  // Simple thunk for basic cases
};

function* complexUserFlowSaga() {
  // Complex saga for advanced cases
}
```

**Recommendation:**

- Start with **Redux Thunk** for most applications
- Migrate to **Redux Saga** when you encounter limitations
- Use **Redux Saga** from the beginning for complex applications
- Consider **RTK Query** as an alternative for data fetching

---

### Q30: How do you implement optimistic updates in Redux vs Zustand?

**Answer:**
Optimistic updates improve user experience by immediately updating the UI before the server confirms the change, then handling success or failure accordingly.

**Redux Optimistic Updates:**

```javascript
// Enhanced Redux slice with optimistic updates
import { createSlice, createAsyncThunk, nanoid } from "@reduxjs/toolkit";

// Async thunk for optimistic todo creation
export const createTodoOptimistic = createAsyncThunk(
  "todos/createOptimistic",
  async (todoData, { dispatch, rejectWithValue }) => {
    const tempId = nanoid();
    const optimisticTodo = {
      ...todoData,
      id: tempId,
      createdAt: new Date().toISOString(),
      optimistic: true,
    };

    // Immediately add optimistic todo
    dispatch(todosSlice.actions.addOptimisticTodo(optimisticTodo));

    try {
      const response = await todosAPI.createTodo(todoData);

      // Replace optimistic todo with real one
      dispatch(
        todosSlice.actions.replaceOptimisticTodo({
          tempId,
          realTodo: response.data,
        })
      );

      return response.data;
    } catch (error) {
      // Remove optimistic todo on failure
      dispatch(todosSlice.actions.removeOptimisticTodo(tempId));

      return rejectWithValue({
        error: error.message,
        tempId,
        originalData: todoData,
      });
    }
  }
);

// Optimistic update thunk
export const updateTodoOptimistic = createAsyncThunk(
  "todos/updateOptimistic",
  async ({ id, updates }, { dispatch, getState, rejectWithValue }) => {
    const state = getState();
    const originalTodo = state.todos.items.find((todo) => todo.id === id);

    if (!originalTodo) {
      return rejectWithValue("Todo not found");
    }

    // Apply optimistic update
    dispatch(todosSlice.actions.applyOptimisticUpdate({ id, updates }));

    try {
      const response = await todosAPI.updateTodo(id, updates);

      // Confirm optimistic update with server data
      dispatch(
        todosSlice.actions.confirmOptimisticUpdate({
          id,
          serverData: response.data,
        })
      );

      return response.data;
    } catch (error) {
      // Revert optimistic update
      dispatch(
        todosSlice.actions.revertOptimisticUpdate({
          id,
          originalTodo,
        })
      );

      return rejectWithValue({
        error: error.message,
        id,
        originalTodo,
      });
    }
  }
);

// Optimistic delete thunk
export const deleteTodoOptimistic = createAsyncThunk(
  "todos/deleteOptimistic",
  async (id, { dispatch, getState, rejectWithValue }) => {
    const state = getState();
    const todoToDelete = state.todos.items.find((todo) => todo.id === id);

    if (!todoToDelete) {
      return rejectWithValue("Todo not found");
    }

    // Optimistically remove todo
    dispatch(todosSlice.actions.removeOptimisticTodo(id));

    try {
      await todosAPI.deleteTodo(id);

      // Confirm deletion
      dispatch(todosSlice.actions.confirmOptimisticDelete(id));

      return id;
    } catch (error) {
      // Restore deleted todo
      dispatch(todosSlice.actions.restoreOptimisticTodo(todoToDelete));

      return rejectWithValue({
        error: error.message,
        id,
        restoredTodo: todoToDelete,
      });
    }
  }
);

const todosSlice = createSlice({
  name: "todos",
  initialState: {
    items: [],
    optimisticOperations: new Map(), // Track optimistic operations
    loading: {
      create: false,
      update: false,
      delete: false,
    },
    errors: {
      create: null,
      update: null,
      delete: null,
    },
  },
  reducers: {
    // Optimistic todo creation
    addOptimisticTodo: (state, action) => {
      const todo = action.payload;
      state.items.push(todo);
      state.optimisticOperations.set(todo.id, {
        type: "CREATE",
        timestamp: Date.now(),
        data: todo,
      });
    },

    // Replace optimistic todo with real one
    replaceOptimisticTodo: (state, action) => {
      const { tempId, realTodo } = action.payload;
      const index = state.items.findIndex((todo) => todo.id === tempId);

      if (index !== -1) {
        state.items[index] = realTodo;
        state.optimisticOperations.delete(tempId);
      }
    },

    // Remove optimistic todo
    removeOptimisticTodo: (state, action) => {
      const id = action.payload;
      state.items = state.items.filter((todo) => todo.id !== id);
      state.optimisticOperations.delete(id);
    },

    // Apply optimistic update
    applyOptimisticUpdate: (state, action) => {
      const { id, updates } = action.payload;
      const index = state.items.findIndex((todo) => todo.id === id);

      if (index !== -1) {
        const originalTodo = state.items[index];
        state.items[index] = { ...originalTodo, ...updates };

        state.optimisticOperations.set(id, {
          type: "UPDATE",
          timestamp: Date.now(),
          originalData: originalTodo,
          updates,
        });
      }
    },

    // Confirm optimistic update
    confirmOptimisticUpdate: (state, action) => {
      const { id, serverData } = action.payload;
      const index = state.items.findIndex((todo) => todo.id === id);

      if (index !== -1) {
        state.items[index] = serverData;
        state.optimisticOperations.delete(id);
      }
    },

    // Revert optimistic update
    revertOptimisticUpdate: (state, action) => {
      const { id, originalTodo } = action.payload;
      const index = state.items.findIndex((todo) => todo.id === id);

      if (index !== -1) {
        state.items[index] = originalTodo;
        state.optimisticOperations.delete(id);
      }
    },

    // Confirm optimistic delete
    confirmOptimisticDelete: (state, action) => {
      const id = action.payload;
      state.optimisticOperations.delete(id);
    },

    // Restore optimistically deleted todo
    restoreOptimisticTodo: (state, action) => {
      const todo = action.payload;
      state.items.push(todo);
      state.items.sort((a, b) => new Date(a.createdAt) - new Date(b.createdAt));
      state.optimisticOperations.delete(todo.id);
    },

    // Clear all optimistic operations (for cleanup)
    clearOptimisticOperations: (state) => {
      state.optimisticOperations.clear();
      state.items = state.items.filter((todo) => !todo.optimistic);
    },
  },
  extraReducers: (builder) => {
    builder
      // Handle loading states for optimistic operations
      .addCase(createTodoOptimistic.pending, (state) => {
        state.loading.create = true;
        state.errors.create = null;
      })
      .addCase(createTodoOptimistic.fulfilled, (state) => {
        state.loading.create = false;
      })
      .addCase(createTodoOptimistic.rejected, (state, action) => {
        state.loading.create = false;
        state.errors.create = action.payload;
      })

      .addCase(updateTodoOptimistic.pending, (state) => {
        state.loading.update = true;
        state.errors.update = null;
      })
      .addCase(updateTodoOptimistic.fulfilled, (state) => {
        state.loading.update = false;
      })
      .addCase(updateTodoOptimistic.rejected, (state, action) => {
        state.loading.update = false;
        state.errors.update = action.payload;
      })

      .addCase(deleteTodoOptimistic.pending, (state) => {
        state.loading.delete = true;
        state.errors.delete = null;
      })
      .addCase(deleteTodoOptimistic.fulfilled, (state) => {
        state.loading.delete = false;
      })
      .addCase(deleteTodoOptimistic.rejected, (state, action) => {
        state.loading.delete = false;
        state.errors.delete = action.payload;
      });
  },
});

export const {
  addOptimisticTodo,
  replaceOptimisticTodo,
  removeOptimisticTodo,
  applyOptimisticUpdate,
  confirmOptimisticUpdate,
  revertOptimisticUpdate,
  confirmOptimisticDelete,
  restoreOptimisticTodo,
  clearOptimisticOperations,
} = todosSlice.actions;

export default todosSlice.reducer;
```

**Redux Optimistic Selectors:**

```javascript
// Selectors for optimistic updates
import { createSelector } from "@reduxjs/toolkit";

export const selectTodos = (state) => state.todos.items;
export const selectOptimisticOperations = (state) =>
  state.todos.optimisticOperations;

// Get todos with optimistic status
export const selectTodosWithOptimisticStatus = createSelector(
  [selectTodos, selectOptimisticOperations],
  (todos, operations) => {
    return todos.map((todo) => ({
      ...todo,
      isOptimistic: operations.has(todo.id),
      optimisticOperation: operations.get(todo.id),
    }));
  }
);

// Get only confirmed (non-optimistic) todos
export const selectConfirmedTodos = createSelector(
  [selectTodos, selectOptimisticOperations],
  (todos, operations) => {
    return todos.filter((todo) => !operations.has(todo.id));
  }
);

// Get pending optimistic operations
export const selectPendingOptimisticOperations = createSelector(
  [selectOptimisticOperations],
  (operations) => {
    return Array.from(operations.entries()).map(([id, operation]) => ({
      id,
      ...operation,
    }));
  }
);
```

**Zustand Optimistic Updates:**

```javascript
// Zustand store with optimistic updates
import { create } from "zustand";
import { immer } from "zustand/middleware/immer";
import { nanoid } from "nanoid";

const useTodosStore = create(
  immer((set, get) => ({
    items: [],
    optimisticOperations: new Map(),
    loading: {
      create: false,
      update: false,
      delete: false,
    },
    errors: {
      create: null,
      update: null,
      delete: null,
    },

    // Optimistic create
    createTodoOptimistic: async (todoData) => {
      const tempId = nanoid();
      const optimisticTodo = {
        ...todoData,
        id: tempId,
        createdAt: new Date().toISOString(),
        optimistic: true,
      };

      // Immediately add optimistic todo
      set((state) => {
        state.items.push(optimisticTodo);
        state.optimisticOperations.set(tempId, {
          type: "CREATE",
          timestamp: Date.now(),
          data: optimisticTodo,
        });
        state.loading.create = true;
        state.errors.create = null;
      });

      try {
        const response = await todosAPI.createTodo(todoData);

        // Replace optimistic todo with real one
        set((state) => {
          const index = state.items.findIndex((todo) => todo.id === tempId);
          if (index !== -1) {
            state.items[index] = response.data;
          }
          state.optimisticOperations.delete(tempId);
          state.loading.create = false;
        });

        return { success: true, data: response.data };
      } catch (error) {
        // Remove optimistic todo on failure
        set((state) => {
          state.items = state.items.filter((todo) => todo.id !== tempId);
          state.optimisticOperations.delete(tempId);
          state.loading.create = false;
          state.errors.create = error.message;
        });

        return { success: false, error: error.message };
      }
    },

    // Optimistic update
    updateTodoOptimistic: async (id, updates) => {
      const originalTodo = get().items.find((todo) => todo.id === id);

      if (!originalTodo) {
        return { success: false, error: "Todo not found" };
      }

      // Apply optimistic update
      set((state) => {
        const index = state.items.findIndex((todo) => todo.id === id);
        if (index !== -1) {
          state.items[index] = { ...state.items[index], ...updates };
          state.optimisticOperations.set(id, {
            type: "UPDATE",
            timestamp: Date.now(),
            originalData: originalTodo,
            updates,
          });
        }
        state.loading.update = true;
        state.errors.update = null;
      });

      try {
        const response = await todosAPI.updateTodo(id, updates);

        // Confirm optimistic update with server data
        set((state) => {
          const index = state.items.findIndex((todo) => todo.id === id);
          if (index !== -1) {
            state.items[index] = response.data;
          }
          state.optimisticOperations.delete(id);
          state.loading.update = false;
        });

        return { success: true, data: response.data };
      } catch (error) {
        // Revert optimistic update
        set((state) => {
          const index = state.items.findIndex((todo) => todo.id === id);
          if (index !== -1) {
            state.items[index] = originalTodo;
          }
          state.optimisticOperations.delete(id);
          state.loading.update = false;
          state.errors.update = error.message;
        });

        return { success: false, error: error.message };
      }
    },

    // Optimistic delete
    deleteTodoOptimistic: async (id) => {
      const todoToDelete = get().items.find((todo) => todo.id === id);

      if (!todoToDelete) {
        return { success: false, error: "Todo not found" };
      }

      // Optimistically remove todo
      set((state) => {
        state.items = state.items.filter((todo) => todo.id !== id);
        state.optimisticOperations.set(id, {
          type: "DELETE",
          timestamp: Date.now(),
          data: todoToDelete,
        });
        state.loading.delete = true;
        state.errors.delete = null;
      });

      try {
        await todosAPI.deleteTodo(id);

        // Confirm deletion
        set((state) => {
          state.optimisticOperations.delete(id);
          state.loading.delete = false;
        });

        return { success: true };
      } catch (error) {
        // Restore deleted todo
        set((state) => {
          state.items.push(todoToDelete);
          state.items.sort(
            (a, b) => new Date(a.createdAt) - new Date(b.createdAt)
          );
          state.optimisticOperations.delete(id);
          state.loading.delete = false;
          state.errors.delete = error.message;
        });

        return { success: false, error: error.message };
      }
    },

    // Batch optimistic operations
    batchOptimisticUpdates: async (operations) => {
      const rollbackData = [];

      // Apply all optimistic updates
      operations.forEach(({ type, id, data }) => {
        const currentState = get();

        switch (type) {
          case "UPDATE":
            const originalTodo = currentState.items.find(
              (todo) => todo.id === id
            );
            if (originalTodo) {
              rollbackData.push({
                type: "UPDATE",
                id,
                originalData: originalTodo,
              });
              get().updateTodoOptimistic(id, data);
            }
            break;
          case "DELETE":
            const todoToDelete = currentState.items.find(
              (todo) => todo.id === id
            );
            if (todoToDelete) {
              rollbackData.push({
                type: "DELETE",
                id,
                originalData: todoToDelete,
              });
              get().deleteTodoOptimistic(id);
            }
            break;
        }
      });

      try {
        // Execute all operations on server
        const promises = operations.map(({ type, id, data }) => {
          switch (type) {
            case "UPDATE":
              return todosAPI.updateTodo(id, data);
            case "DELETE":
              return todosAPI.deleteTodo(id);
            default:
              return Promise.resolve();
          }
        });

        await Promise.all(promises);

        return { success: true };
      } catch (error) {
        // Rollback all optimistic updates
        rollbackData.forEach(({ type, id, originalData }) => {
          set((state) => {
            switch (type) {
              case "UPDATE":
                const updateIndex = state.items.findIndex(
                  (todo) => todo.id === id
                );
                if (updateIndex !== -1) {
                  state.items[updateIndex] = originalData;
                }
                break;
              case "DELETE":
                state.items.push(originalData);
                state.items.sort(
                  (a, b) => new Date(a.createdAt) - new Date(b.createdAt)
                );
                break;
            }
            state.optimisticOperations.delete(id);
          });
        });

        return { success: false, error: error.message };
      }
    },

    // Utility functions
    getOptimisticStatus: (id) => {
      const operations = get().optimisticOperations;
      return operations.has(id) ? operations.get(id) : null;
    },

    getTodosWithOptimisticStatus: () => {
      const { items, optimisticOperations } = get();
      return items.map((todo) => ({
        ...todo,
        isOptimistic: optimisticOperations.has(todo.id),
        optimisticOperation: optimisticOperations.get(todo.id),
      }));
    },

    getPendingOptimisticOperations: () => {
      const operations = get().optimisticOperations;
      return Array.from(operations.entries()).map(([id, operation]) => ({
        id,
        ...operation,
      }));
    },

    clearOptimisticOperations: () => {
      set((state) => {
        state.optimisticOperations.clear();
        state.items = state.items.filter((todo) => !todo.optimistic);
      });
    },
  }))
);

export default useTodosStore;
```

**Optimistic Updates UI Components:**

```javascript
// Redux Optimistic Todo Component
import React from "react";
import { useSelector, useDispatch } from "react-redux";
import {
  createTodoOptimistic,
  updateTodoOptimistic,
  deleteTodoOptimistic,
  selectTodosWithOptimisticStatus,
} from "../store/todosSlice";

const ReduxOptimisticTodoList = () => {
  const dispatch = useDispatch();
  const todosWithStatus = useSelector(selectTodosWithOptimisticStatus);

  const handleCreate = async (todoData) => {
    const result = await dispatch(createTodoOptimistic(todoData));

    if (createTodoOptimistic.rejected.match(result)) {
      // Handle creation failure
      console.error("Failed to create todo:", result.payload);
    }
  };

  const handleUpdate = async (id, updates) => {
    const result = await dispatch(updateTodoOptimistic({ id, updates }));

    if (updateTodoOptimistic.rejected.match(result)) {
      // Handle update failure
      console.error("Failed to update todo:", result.payload);
    }
  };

  const handleDelete = async (id) => {
    const result = await dispatch(deleteTodoOptimistic(id));

    if (deleteTodoOptimistic.rejected.match(result)) {
      // Handle deletion failure
      console.error("Failed to delete todo:", result.payload);
    }
  };

  return (
    <div className="todo-list">
      {todosWithStatus.map((todo) => (
        <div
          key={todo.id}
          className={`todo-item ${
            todo.isOptimistic ? "optimistic" : "confirmed"
          }`}
        >
          <span className="todo-text">{todo.text}</span>

          {todo.isOptimistic && (
            <div className="optimistic-indicator">
              <span className="spinner" />
              <span className="status">
                {todo.optimisticOperation?.type === "CREATE" && "Creating..."}
                {todo.optimisticOperation?.type === "UPDATE" && "Updating..."}
                {todo.optimisticOperation?.type === "DELETE" && "Deleting..."}
              </span>
            </div>
          )}

          <div className="todo-actions">
            <button
              onClick={() =>
                handleUpdate(todo.id, { completed: !todo.completed })
              }
              disabled={todo.isOptimistic}
            >
              {todo.completed ? "Undo" : "Complete"}
            </button>

            <button
              onClick={() => handleDelete(todo.id)}
              disabled={todo.isOptimistic}
              className="delete-btn"
            >
              Delete
            </button>
          </div>
        </div>
      ))}
    </div>
  );
};

// Zustand Optimistic Todo Component
const ZustandOptimisticTodoList = () => {
  const {
    items: todos,
    createTodoOptimistic,
    updateTodoOptimistic,
    deleteTodoOptimistic,
    getTodosWithOptimisticStatus,
  } = useTodosStore();

  const todosWithStatus = getTodosWithOptimisticStatus();

  const handleCreate = async (todoData) => {
    const result = await createTodoOptimistic(todoData);

    if (!result.success) {
      console.error("Failed to create todo:", result.error);
    }
  };

  const handleUpdate = async (id, updates) => {
    const result = await updateTodoOptimistic(id, updates);

    if (!result.success) {
      console.error("Failed to update todo:", result.error);
    }
  };

  const handleDelete = async (id) => {
    const result = await deleteTodoOptimistic(id);

    if (!result.success) {
      console.error("Failed to delete todo:", result.error);
    }
  };

  return (
    <div className="todo-list">
      {todosWithStatus.map((todo) => (
        <div
          key={todo.id}
          className={`todo-item ${
            todo.isOptimistic ? "optimistic" : "confirmed"
          }`}
        >
          <span className="todo-text">{todo.text}</span>

          {todo.isOptimistic && (
            <div className="optimistic-indicator">
              <span className="spinner" />
              <span className="status">
                {todo.optimisticOperation?.type === "CREATE" && "Creating..."}
                {todo.optimisticOperation?.type === "UPDATE" && "Updating..."}
                {todo.optimisticOperation?.type === "DELETE" && "Deleting..."}
              </span>
            </div>
          )}

          <div className="todo-actions">
            <button
              onClick={() =>
                handleUpdate(todo.id, { completed: !todo.completed })
              }
              disabled={todo.isOptimistic}
            >
              {todo.completed ? "Undo" : "Complete"}
            </button>

            <button
              onClick={() => handleDelete(todo.id)}
              disabled={todo.isOptimistic}
              className="delete-btn"
            >
              Delete
            </button>
          </div>
        </div>
      ))}
    </div>
  );
};
```

**Optimistic Updates CSS:**

```css
/* Optimistic updates styling */
.todo-item {
  display: flex;
  align-items: center;
  padding: 12px;
  border: 1px solid #e1e5e9;
  border-radius: 6px;
  margin-bottom: 8px;
  transition: all 0.2s ease;
}

.todo-item.optimistic {
  opacity: 0.7;
  border-color: #fbbf24;
  background-color: #fffbeb;
}

.todo-item.confirmed {
  opacity: 1;
  border-color: #10b981;
  background-color: #f0fdf4;
}

.optimistic-indicator {
  display: flex;
  align-items: center;
  margin-left: auto;
  margin-right: 12px;
  color: #f59e0b;
  font-size: 12px;
}

.spinner {
  width: 12px;
  height: 12px;
  border: 2px solid #f3f4f6;
  border-top: 2px solid #f59e0b;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-right: 6px;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.todo-actions button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
```

**Best Practices for Optimistic Updates:**

1. **Clear Visual Feedback:**

   - Show loading indicators for optimistic operations
   - Use different styling for optimistic vs confirmed items
   - Provide clear error messages when operations fail

2. **Proper Error Handling:**

   - Always revert optimistic changes on failure
   - Preserve original data for rollback
   - Show meaningful error messages to users

3. **Conflict Resolution:**

   - Handle concurrent modifications gracefully
   - Consider server timestamps for conflict detection
   - Implement merge strategies for conflicting updates

4. **Performance Considerations:**

   - Limit the number of concurrent optimistic operations
   - Clean up completed operations to prevent memory leaks
   - Use efficient data structures for tracking operations

5. **User Experience:**
   - Disable actions on items with pending operations
   - Provide undo functionality where appropriate
   - Show progress indicators for long-running operations

**Comparison Summary:**

**Redux Advantages:**

- **Structured approach** with clear action types
- **Time-travel debugging** for optimistic operations
- **Predictable state updates** through reducers
- **Middleware integration** for global optimistic handling

**Zustand Advantages:**

- **Simpler implementation** with direct state updates
- **Flexible rollback logic** without action complexity
- **Built-in async support** without thunk boilerplate
- **Smaller bundle size** for optimistic update logic

Both approaches provide robust optimistic update capabilities, with Redux offering more structure and debugging tools, while Zustand provides simplicity and flexibility.

---

### Q31: What is Redux Observable and how does it compare to Redux Saga?

**Answer:**
Redux Observable is a middleware for Redux that uses RxJS observables to handle complex asynchronous operations and side effects. It provides a reactive programming approach to managing async flows in Redux applications.

**Redux Observable Setup:**

```javascript
// Installation: npm install redux-observable rxjs

import { createStore, applyMiddleware } from "redux";
import { createEpicMiddleware, combineEpics } from "redux-observable";
import { ajax } from "rxjs/ajax";
import {
  map,
  mergeMap,
  catchError,
  debounceTime,
  switchMap,
  takeUntil,
  retry,
  delay,
  filter,
  withLatestFrom,
} from "rxjs/operators";
import { of, timer, race, merge } from "rxjs";
import { ofType } from "redux-observable";

// Action types
const FETCH_USER = "FETCH_USER";
const FETCH_USER_SUCCESS = "FETCH_USER_SUCCESS";
const FETCH_USER_FAILURE = "FETCH_USER_FAILURE";
const SEARCH_USERS = "SEARCH_USERS";
const SEARCH_USERS_SUCCESS = "SEARCH_USERS_SUCCESS";
const SEARCH_USERS_FAILURE = "SEARCH_USERS_FAILURE";
const CANCEL_SEARCH = "CANCEL_SEARCH";
const WEBSOCKET_CONNECT = "WEBSOCKET_CONNECT";
const WEBSOCKET_MESSAGE = "WEBSOCKET_MESSAGE";
const WEBSOCKET_DISCONNECT = "WEBSOCKET_DISCONNECT";

// Action creators
const fetchUser = (userId) => ({ type: FETCH_USER, payload: userId });
const fetchUserSuccess = (user) => ({
  type: FETCH_USER_SUCCESS,
  payload: user,
});
const fetchUserFailure = (error) => ({
  type: FETCH_USER_FAILURE,
  payload: error,
});

const searchUsers = (query) => ({ type: SEARCH_USERS, payload: query });
const searchUsersSuccess = (users) => ({
  type: SEARCH_USERS_SUCCESS,
  payload: users,
});
const searchUsersFailure = (error) => ({
  type: SEARCH_USERS_FAILURE,
  payload: error,
});
const cancelSearch = () => ({ type: CANCEL_SEARCH });

const websocketConnect = () => ({ type: WEBSOCKET_CONNECT });
const websocketMessage = (message) => ({
  type: WEBSOCKET_MESSAGE,
  payload: message,
});
const websocketDisconnect = () => ({ type: WEBSOCKET_DISCONNECT });

// Basic Epic - Fetch User
const fetchUserEpic = (action$) =>
  action$.pipe(
    ofType(FETCH_USER),
    mergeMap((action) =>
      ajax.getJSON(`/api/users/${action.payload}`).pipe(
        map((response) => fetchUserSuccess(response)),
        catchError((error) => of(fetchUserFailure(error.message)))
      )
    )
  );

// Advanced Epic - Debounced Search with Cancellation
const searchUsersEpic = (action$) =>
  action$.pipe(
    ofType(SEARCH_USERS),
    debounceTime(300), // Debounce user input
    switchMap(
      (
        action // switchMap cancels previous requests
      ) =>
        ajax.getJSON(`/api/users/search?q=${action.payload}`).pipe(
          map((response) => searchUsersSuccess(response.users)),
          catchError((error) => of(searchUsersFailure(error.message))),
          takeUntil(action$.pipe(ofType(CANCEL_SEARCH))) // Manual cancellation
        )
    )
  );

// Epic with Retry Logic
const fetchUserWithRetryEpic = (action$) =>
  action$.pipe(
    ofType(FETCH_USER),
    mergeMap((action) =>
      ajax.getJSON(`/api/users/${action.payload}`).pipe(
        retry(3), // Retry up to 3 times
        map((response) => fetchUserSuccess(response)),
        catchError((error) => {
          console.error("Failed after 3 retries:", error);
          return of(fetchUserFailure(error.message));
        })
      )
    )
  );

// Epic with Exponential Backoff
const fetchUserWithBackoffEpic = (action$) =>
  action$.pipe(
    ofType(FETCH_USER),
    mergeMap((action) =>
      ajax.getJSON(`/api/users/${action.payload}`).pipe(
        retryWhen((errors) =>
          errors.pipe(
            mergeMap((error, index) => {
              const retryAttempt = index + 1;
              if (retryAttempt > 3) {
                throw error;
              }
              const delayTime = Math.pow(2, retryAttempt) * 1000; // Exponential backoff
              console.log(`Retry attempt ${retryAttempt} after ${delayTime}ms`);
              return timer(delayTime);
            })
          )
        ),
        map((response) => fetchUserSuccess(response)),
        catchError((error) => of(fetchUserFailure(error.message)))
      )
    )
  );

// WebSocket Epic
const websocketEpic = (action$, state$) =>
  action$.pipe(
    ofType(WEBSOCKET_CONNECT),
    switchMap(() => {
      const websocket$ = new Observable((observer) => {
        const ws = new WebSocket("ws://localhost:8080");

        ws.onopen = () => {
          console.log("WebSocket connected");
          observer.next(websocketMessage({ type: "CONNECTED" }));
        };

        ws.onmessage = (event) => {
          const data = JSON.parse(event.data);
          observer.next(websocketMessage(data));
        };

        ws.onerror = (error) => {
          observer.error(error);
        };

        ws.onclose = () => {
          console.log("WebSocket disconnected");
          observer.complete();
        };

        // Cleanup function
        return () => {
          if (ws.readyState === WebSocket.OPEN) {
            ws.close();
          }
        };
      });

      return websocket$.pipe(
        takeUntil(action$.pipe(ofType(WEBSOCKET_DISCONNECT)))
      );
    })
  );

// Polling Epic
const pollingEpic = (action$, state$) =>
  action$.pipe(
    ofType("START_POLLING"),
    switchMap(() =>
      timer(0, 5000).pipe(
        // Poll every 5 seconds
        mergeMap(() =>
          ajax.getJSON("/api/status").pipe(
            map((response) => ({ type: "POLLING_SUCCESS", payload: response })),
            catchError((error) =>
              of({ type: "POLLING_FAILURE", payload: error.message })
            )
          )
        ),
        takeUntil(action$.pipe(ofType("STOP_POLLING")))
      )
    )
  );

// Complex Flow Epic - Race Conditions
const raceConditionEpic = (action$) =>
  action$.pipe(
    ofType("FETCH_DATA_WITH_TIMEOUT"),
    switchMap((action) => {
      const dataRequest$ = ajax
        .getJSON(`/api/data/${action.payload}`)
        .pipe(
          map((response) => ({ type: "FETCH_DATA_SUCCESS", payload: response }))
        );

      const timeout$ = timer(5000).pipe(
        map(() => ({ type: "FETCH_DATA_TIMEOUT" }))
      );

      return race(dataRequest$, timeout$).pipe(
        catchError((error) =>
          of({ type: "FETCH_DATA_FAILURE", payload: error.message })
        )
      );
    })
  );

// Epic with State Access
const conditionalEpic = (action$, state$) =>
  action$.pipe(
    ofType("CONDITIONAL_ACTION"),
    withLatestFrom(state$),
    filter(([action, state]) => state.user.isAuthenticated), // Only proceed if authenticated
    mergeMap(([action, state]) =>
      ajax
        .getJSON("/api/protected-data", {
          Authorization: `Bearer ${state.user.token}`,
        })
        .pipe(
          map((response) => ({
            type: "PROTECTED_DATA_SUCCESS",
            payload: response,
          })),
          catchError((error) =>
            of({ type: "PROTECTED_DATA_FAILURE", payload: error.message })
          )
        )
    )
  );

// Combine all epics
const rootEpic = combineEpics(
  fetchUserEpic,
  searchUsersEpic,
  fetchUserWithRetryEpic,
  fetchUserWithBackoffEpic,
  websocketEpic,
  pollingEpic,
  raceConditionEpic,
  conditionalEpic
);

// Create epic middleware
const epicMiddleware = createEpicMiddleware();

// Create store
const store = createStore(rootReducer, applyMiddleware(epicMiddleware));

// Run the root epic
epicMiddleware.run(rootEpic);
```

**Advanced Redux Observable Patterns:**

```javascript
// Hot Observable Epic - Share expensive operations
const sharedDataEpic = (action$) => {
  const sharedRequest$ = ajax.getJSON("/api/expensive-data").pipe(
    shareReplay(1) // Cache the result for multiple subscribers
  );

  return action$.pipe(
    ofType("REQUEST_SHARED_DATA"),
    switchMap(() =>
      sharedRequest$.pipe(
        map((response) => ({ type: "SHARED_DATA_SUCCESS", payload: response })),
        catchError((error) =>
          of({ type: "SHARED_DATA_FAILURE", payload: error.message })
        )
      )
    )
  );
};

// Buffer and Batch Epic
const batchEpic = (action$) =>
  action$.pipe(
    ofType("BATCH_ACTION"),
    bufferTime(1000), // Collect actions for 1 second
    filter((actions) => actions.length > 0),
    mergeMap((actions) => {
      const batchData = actions.map((action) => action.payload);
      return ajax.post("/api/batch", batchData).pipe(
        map((response) => ({ type: "BATCH_SUCCESS", payload: response })),
        catchError((error) =>
          of({ type: "BATCH_FAILURE", payload: error.message })
        )
      );
    })
  );

// Dependency Injection Epic
const createApiEpic = (dependencies) => (action$, state$) =>
  action$.pipe(
    ofType("API_CALL"),
    mergeMap((action) =>
      dependencies.apiService.getData(action.payload).pipe(
        map((response) => ({ type: "API_SUCCESS", payload: response })),
        catchError((error) =>
          of({ type: "API_FAILURE", payload: error.message })
        )
      )
    )
  );

// Epic with dependencies
const epicMiddleware = createEpicMiddleware({
  dependencies: {
    apiService: new ApiService(),
    logger: new Logger(),
  },
});

// Testing Epic
const testEpic = (action$, state$, dependencies) => {
  const { scheduler } = dependencies;

  return action$.pipe(
    ofType("TEST_ACTION"),
    delay(1000, scheduler), // Use scheduler for testing
    map(() => ({ type: "TEST_SUCCESS" }))
  );
};
```

**Redux Observable vs Redux Saga Comparison:**

```javascript
// Redux Observable - Reactive approach
const fetchUserEpic = (action$) =>
  action$.pipe(
    ofType(FETCH_USER),
    mergeMap((action) =>
      ajax.getJSON(`/api/users/${action.payload}`).pipe(
        map((response) => fetchUserSuccess(response)),
        catchError((error) => of(fetchUserFailure(error.message)))
      )
    )
  );

// Redux Saga - Generator approach
function* fetchUserSaga() {
  try {
    const action = yield take(FETCH_USER);
    const response = yield call(api.getUser, action.payload);
    yield put(fetchUserSuccess(response));
  } catch (error) {
    yield put(fetchUserFailure(error.message));
  }
}

// Complex flow comparison

// Redux Observable - Declarative stream composition
const complexFlowEpic = (action$, state$) =>
  action$.pipe(
    ofType("START_COMPLEX_FLOW"),
    withLatestFrom(state$),
    filter(([action, state]) => state.user.isAuthenticated),
    debounceTime(300),
    switchMap(([action, state]) =>
      merge(
        ajax
          .getJSON("/api/data1")
          .pipe(
            map((response) => ({ type: "DATA1_SUCCESS", payload: response }))
          ),
        ajax
          .getJSON("/api/data2")
          .pipe(
            map((response) => ({ type: "DATA2_SUCCESS", payload: response }))
          )
      ).pipe(
        takeUntil(action$.pipe(ofType("CANCEL_FLOW"))),
        catchError((error) =>
          of({ type: "FLOW_FAILURE", payload: error.message })
        )
      )
    )
  );

// Redux Saga - Imperative step-by-step approach
function* complexFlowSaga() {
  try {
    const action = yield take("START_COMPLEX_FLOW");
    const state = yield select();

    if (!state.user.isAuthenticated) {
      return;
    }

    yield delay(300); // Debounce

    const { data1, data2 } = yield race({
      data1: call(api.getData1),
      data2: call(api.getData2),
      cancel: take("CANCEL_FLOW"),
    });

    if (data1) {
      yield put({ type: "DATA1_SUCCESS", payload: data1 });
    }

    if (data2) {
      yield put({ type: "DATA2_SUCCESS", payload: data2 });
    }
  } catch (error) {
    yield put({ type: "FLOW_FAILURE", payload: error.message });
  }
}
```

**Testing Redux Observable:**

```javascript
import { TestScheduler } from "rxjs/testing";
import { fetchUserEpic } from "./epics";

describe("fetchUserEpic", () => {
  let testScheduler;

  beforeEach(() => {
    testScheduler = new TestScheduler((actual, expected) => {
      expect(actual).toEqual(expected);
    });
  });

  it("should fetch user successfully", () => {
    testScheduler.run(({ hot, cold, expectObservable }) => {
      const action$ = hot("-a", {
        a: { type: FETCH_USER, payload: "123" },
      });

      const dependencies = {
        ajax: {
          getJSON: () =>
            cold("--a|", {
              a: { id: "123", name: "John" },
            }),
        },
      };

      const output$ = fetchUserEpic(action$, null, dependencies);

      expectObservable(output$).toBe("---a", {
        a: {
          type: FETCH_USER_SUCCESS,
          payload: { id: "123", name: "John" },
        },
      });
    });
  });

  it("should handle errors", () => {
    testScheduler.run(({ hot, cold, expectObservable }) => {
      const action$ = hot("-a", {
        a: { type: FETCH_USER, payload: "123" },
      });

      const dependencies = {
        ajax: {
          getJSON: () => cold("--#", null, new Error("Network error")),
        },
      };

      const output$ = fetchUserEpic(action$, null, dependencies);

      expectObservable(output$).toBe("---a", {
        a: {
          type: FETCH_USER_FAILURE,
          payload: "Network error",
        },
      });
    });
  });
});
```

**Comparison Summary:**

| Feature                   | Redux Observable                  | Redux Saga                       |
| ------------------------- | --------------------------------- | -------------------------------- |
| **Learning Curve**        | Steep (RxJS knowledge required)   | Moderate (Generator functions)   |
| **Async Handling**        | Reactive streams                  | Imperative generators            |
| **Cancellation**          | Built-in with operators           | Manual with `cancel()`           |
| **Testing**               | Marble testing with TestScheduler | Easy with step-by-step execution |
| **Debugging**             | Stream visualization tools        | Step-through debugging           |
| **Bundle Size**           | Larger (includes RxJS)            | Smaller                          |
| **Complex Flows**         | Declarative composition           | Imperative control flow          |
| **Error Handling**        | Stream-based with operators       | Try-catch blocks                 |
| **Concurrency**           | Built-in operators (merge, race)  | Manual coordination              |
| **Time-based Operations** | Rich set of operators             | Basic delay/timeout              |

**When to Choose Redux Observable:**

- **Complex async flows** with multiple data streams
- **Real-time applications** with WebSockets or SSE
- **Heavy data transformation** and filtering
- **Time-based operations** (debouncing, throttling, polling)
- **Team familiar with RxJS** and reactive programming
- **Applications requiring advanced cancellation** and backpressure handling

**When to Choose Redux Saga:**

- **Simpler async flows** with clear step-by-step logic
- **Teams new to reactive programming**
- **Applications requiring easy debugging** and testing
- **Background tasks** and long-running processes
- **Complex business logic** with conditional flows
- **Smaller bundle size** requirements

Both Redux Observable and Redux Saga are powerful tools for handling side effects, with Redux Observable excelling in reactive scenarios and Redux Saga providing more straightforward imperative control flow.

---

### Q32: How do you implement advanced Zustand subscriptions and reactive patterns?

**Answer:**
Zustand provides powerful subscription mechanisms that allow you to react to state changes in sophisticated ways. These patterns enable reactive programming similar to observables but with a simpler API.

**Basic Zustand Subscriptions:**

```javascript
import { create } from "zustand";
import { subscribeWithSelector } from "zustand/middleware";

// Store with subscription middleware
const useStore = create(
  subscribeWithSelector((set, get) => ({
    user: null,
    posts: [],
    notifications: [],
    settings: {
      theme: "light",
      language: "en",
      notifications: true,
    },

    // Actions
    setUser: (user) => set({ user }),
    addPost: (post) =>
      set((state) => ({
        posts: [...state.posts, post],
      })),
    updateSettings: (newSettings) =>
      set((state) => ({
        settings: { ...state.settings, ...newSettings },
      })),
    addNotification: (notification) =>
      set((state) => ({
        notifications: [...state.notifications, notification],
      })),
  }))
);

// Basic subscription to user changes
const unsubscribeUser = useStore.subscribe(
  (state) => state.user,
  (user, previousUser) => {
    console.log("User changed:", { user, previousUser });

    if (user && !previousUser) {
      console.log("User logged in");
      // Trigger side effects for login
    } else if (!user && previousUser) {
      console.log("User logged out");
      // Trigger side effects for logout
    }
  },
  {
    equalityFn: (a, b) => a?.id === b?.id, // Custom equality check
    fireImmediately: false, // Don't fire on subscription
  }
);

// Subscription to nested state changes
const unsubscribeTheme = useStore.subscribe(
  (state) => state.settings.theme,
  (theme) => {
    document.documentElement.setAttribute("data-theme", theme);
    localStorage.setItem("theme", theme);
  }
);

// Multiple state subscription
const unsubscribeMultiple = useStore.subscribe(
  (state) => [state.user, state.settings.notifications],
  ([user, notificationsEnabled]) => {
    if (user && notificationsEnabled) {
      // Setup notification listeners
      console.log("Setting up notifications for user:", user.id);
    } else {
      // Cleanup notification listeners
      console.log("Cleaning up notifications");
    }
  }
);
```

**Advanced Subscription Patterns:**

```javascript
// Debounced subscriptions
const createDebouncedSubscription = (
  store,
  selector,
  callback,
  delay = 300
) => {
  let timeoutId;

  return store.subscribe(selector, (...args) => {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => callback(...args), delay);
  });
};

// Usage: Debounced search
const unsubscribeSearch = createDebouncedSubscription(
  useStore,
  (state) => state.searchQuery,
  (query) => {
    if (query.length > 2) {
      performSearch(query);
    }
  },
  500
);

// Throttled subscriptions
const createThrottledSubscription = (
  store,
  selector,
  callback,
  delay = 100
) => {
  let lastCall = 0;

  return store.subscribe(selector, (...args) => {
    const now = Date.now();
    if (now - lastCall >= delay) {
      lastCall = now;
      callback(...args);
    }
  });
};

// Usage: Throttled scroll position tracking
const unsubscribeScroll = createThrottledSubscription(
  useStore,
  (state) => state.scrollPosition,
  (position) => {
    updateScrollIndicator(position);
  },
  16 // ~60fps
);

// Conditional subscriptions
const createConditionalSubscription = (
  store,
  selector,
  condition,
  callback
) => {
  return store.subscribe(selector, (value, previousValue) => {
    if (condition(value, previousValue)) {
      callback(value, previousValue);
    }
  });
};

// Usage: Only react to increases
const unsubscribeScore = createConditionalSubscription(
  useStore,
  (state) => state.gameScore,
  (current, previous) => current > previous,
  (score) => {
    showScoreAnimation(score);
    playSound("score-increase");
  }
);

// Batch subscriptions
const createBatchSubscription = (
  store,
  selectors,
  callback,
  batchDelay = 0
) => {
  const values = new Map();
  let timeoutId;

  const unsubscribers = selectors.map((selector, index) => {
    return store.subscribe(selector, (value) => {
      values.set(index, value);

      if (batchDelay > 0) {
        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => {
          callback(Array.from(values.values()));
        }, batchDelay);
      } else {
        callback(Array.from(values.values()));
      }
    });
  });

  return () => unsubscribers.forEach((unsub) => unsub());
};

// Usage: Batch multiple state changes
const unsubscribeBatch = createBatchSubscription(
  useStore,
  [
    (state) => state.user,
    (state) => state.settings,
    (state) => state.preferences,
  ],
  ([user, settings, preferences]) => {
    updateUserProfile({ user, settings, preferences });
  },
  100 // Batch changes within 100ms
);
```

**Reactive Store with Computed Values:**

```javascript
import { create } from "zustand";
import { subscribeWithSelector } from "zustand/middleware";

const useReactiveStore = create(
  subscribeWithSelector((set, get) => {
    const store = {
      // Base state
      todos: [],
      filter: "all", // 'all', 'active', 'completed'
      searchQuery: "",

      // Computed values (will be updated reactively)
      filteredTodos: [],
      todoStats: {
        total: 0,
        active: 0,
        completed: 0,
      },

      // Actions
      addTodo: (text) => {
        const newTodo = {
          id: Date.now(),
          text,
          completed: false,
          createdAt: new Date(),
        };
        set((state) => ({ todos: [...state.todos, newTodo] }));
      },

      toggleTodo: (id) => {
        set((state) => ({
          todos: state.todos.map((todo) =>
            todo.id === id ? { ...todo, completed: !todo.completed } : todo
          ),
        }));
      },

      setFilter: (filter) => set({ filter }),
      setSearchQuery: (searchQuery) => set({ searchQuery }),

      // Reactive computations
      computeFilteredTodos: () => {
        const { todos, filter, searchQuery } = get();

        let filtered = todos;

        // Apply search filter
        if (searchQuery) {
          filtered = filtered.filter((todo) =>
            todo.text.toLowerCase().includes(searchQuery.toLowerCase())
          );
        }

        // Apply status filter
        switch (filter) {
          case "active":
            filtered = filtered.filter((todo) => !todo.completed);
            break;
          case "completed":
            filtered = filtered.filter((todo) => todo.completed);
            break;
          default:
            // 'all' - no additional filtering
            break;
        }

        set({ filteredTodos: filtered });
      },

      computeTodoStats: () => {
        const { todos } = get();

        const stats = {
          total: todos.length,
          active: todos.filter((todo) => !todo.completed).length,
          completed: todos.filter((todo) => todo.completed).length,
        };

        set({ todoStats: stats });
      },
    };

    return store;
  })
);

// Setup reactive subscriptions
const setupReactiveSubscriptions = () => {
  // Recompute filtered todos when todos, filter, or search query changes
  const unsubscribeFiltered = useReactiveStore.subscribe(
    (state) => [state.todos, state.filter, state.searchQuery],
    () => {
      useReactiveStore.getState().computeFilteredTodos();
    },
    { equalityFn: (a, b) => JSON.stringify(a) === JSON.stringify(b) }
  );

  // Recompute stats when todos change
  const unsubscribeStats = useReactiveStore.subscribe(
    (state) => state.todos,
    () => {
      useReactiveStore.getState().computeTodoStats();
    }
  );

  // Cleanup function
  return () => {
    unsubscribeFiltered();
    unsubscribeStats();
  };
};

// Initialize reactive subscriptions
const cleanupReactive = setupReactiveSubscriptions();
```

**Subscription Manager for Complex Applications:**

```javascript
class SubscriptionManager {
  constructor() {
    this.subscriptions = new Map();
    this.groups = new Map();
  }

  // Add a named subscription
  add(name, unsubscriber, group = "default") {
    // Cleanup existing subscription with same name
    if (this.subscriptions.has(name)) {
      this.subscriptions.get(name)();
    }

    this.subscriptions.set(name, unsubscriber);

    // Add to group
    if (!this.groups.has(group)) {
      this.groups.set(group, new Set());
    }
    this.groups.get(group).add(name);
  }

  // Remove a specific subscription
  remove(name) {
    if (this.subscriptions.has(name)) {
      this.subscriptions.get(name)();
      this.subscriptions.delete(name);

      // Remove from groups
      for (const [groupName, groupSubs] of this.groups) {
        groupSubs.delete(name);
        if (groupSubs.size === 0) {
          this.groups.delete(groupName);
        }
      }
    }
  }

  // Remove all subscriptions in a group
  removeGroup(groupName) {
    if (this.groups.has(groupName)) {
      const groupSubs = this.groups.get(groupName);
      for (const name of groupSubs) {
        if (this.subscriptions.has(name)) {
          this.subscriptions.get(name)();
          this.subscriptions.delete(name);
        }
      }
      this.groups.delete(groupName);
    }
  }

  // Remove all subscriptions
  removeAll() {
    for (const unsubscriber of this.subscriptions.values()) {
      unsubscriber();
    }
    this.subscriptions.clear();
    this.groups.clear();
  }

  // Get subscription info
  getInfo() {
    return {
      totalSubscriptions: this.subscriptions.size,
      groups: Array.from(this.groups.entries()).map(([name, subs]) => ({
        name,
        count: subs.size,
        subscriptions: Array.from(subs),
      })),
    };
  }
}

// Usage with subscription manager
const subscriptionManager = new SubscriptionManager();

// Add subscriptions with groups
subscriptionManager.add(
  "userAuth",
  useStore.subscribe(
    (state) => state.user,
    (user) => {
      if (user) {
        initializeUserSession(user);
      } else {
        cleanupUserSession();
      }
    }
  ),
  "authentication"
);

subscriptionManager.add(
  "themeSync",
  useStore.subscribe(
    (state) => state.settings.theme,
    (theme) => {
      document.documentElement.setAttribute("data-theme", theme);
    }
  ),
  "ui"
);

subscriptionManager.add(
  "notificationSettings",
  useStore.subscribe(
    (state) => [state.user, state.settings.notifications],
    ([user, enabled]) => {
      if (user && enabled) {
        enableNotifications(user.id);
      } else {
        disableNotifications();
      }
    }
  ),
  "notifications"
);

// React hook for managing subscriptions
const useSubscriptionManager = () => {
  const managerRef = useRef(new SubscriptionManager());

  useEffect(() => {
    return () => {
      // Cleanup all subscriptions on unmount
      managerRef.current.removeAll();
    };
  }, []);

  return managerRef.current;
};

// Component using subscription manager
const App = () => {
  const subscriptionManager = useSubscriptionManager();

  useEffect(() => {
    // Setup application-level subscriptions
    subscriptionManager.add(
      "appInit",
      useStore.subscribe(
        (state) => state.isInitialized,
        (isInitialized) => {
          if (isInitialized) {
            console.log("App initialized");
            // Setup additional subscriptions
            setupFeatureSubscriptions(subscriptionManager);
          }
        }
      ),
      "app"
    );
  }, []);

  return <div className="app">{/* App content */}</div>;
};
```

**Performance Optimization for Subscriptions:**

```javascript
// Memoized selectors for better performance
const createMemoizedSelector = (selector) => {
  let lastResult;
  let lastArgs;

  return (state) => {
    const args = selector(state);

    if (!lastArgs || !shallowEqual(args, lastArgs)) {
      lastArgs = args;
      lastResult = args;
    }

    return lastResult;
  };
};

// Shallow equality check
const shallowEqual = (a, b) => {
  if (a === b) return true;

  if (Array.isArray(a) && Array.isArray(b)) {
    if (a.length !== b.length) return false;
    return a.every((item, index) => item === b[index]);
  }

  if (typeof a === "object" && typeof b === "object") {
    const keysA = Object.keys(a);
    const keysB = Object.keys(b);

    if (keysA.length !== keysB.length) return false;

    return keysA.every((key) => a[key] === b[key]);
  }

  return false;
};

// Usage with memoized selector
const memoizedUserSelector = createMemoizedSelector((state) => ({
  id: state.user?.id,
  name: state.user?.name,
  email: state.user?.email,
}));

const unsubscribeUser = useStore.subscribe(
  memoizedUserSelector,
  (userData) => {
    updateUserProfile(userData);
  },
  { equalityFn: shallowEqual }
);
```

**Best Practices for Zustand Subscriptions:**

1. **Use subscribeWithSelector middleware** for advanced subscription features
2. **Implement proper cleanup** to prevent memory leaks
3. **Use custom equality functions** for complex state comparisons
4. **Debounce/throttle subscriptions** for performance-sensitive operations
5. **Group related subscriptions** for easier management
6. **Memoize selectors** to prevent unnecessary re-computations
7. **Use subscription managers** for complex applications
8. **Avoid subscribing to entire state** - be specific with selectors
9. **Consider using React hooks** for component-level subscriptions
10. **Test subscription behavior** thoroughly, especially cleanup logic

Zustand's subscription system provides a powerful foundation for reactive programming patterns while maintaining simplicity and performance.

---

### Q33: How do you implement caching strategies and data synchronization in Redux vs Zustand?

**Answer:**
Effective caching and data synchronization are crucial for building performant applications. Both Redux and Zustand offer different approaches to handle data caching, invalidation, and synchronization with external sources.

**Redux Caching with RTK Query:**

```javascript
// RTK Query API slice with advanced caching
import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

const api = createApi({
  reducerPath: "api",
  baseQuery: fetchBaseQuery({
    baseUrl: "/api",
    prepareHeaders: (headers, { getState }) => {
      const token = getState().auth.token;
      if (token) {
        headers.set("authorization", `Bearer ${token}`);
      }
      return headers;
    },
  }),
  tagTypes: ["User", "Post", "Comment"],
  endpoints: (builder) => ({
    // Users
    getUsers: builder.query({
      query: (params) => ({
        url: "users",
        params: {
          page: params?.page || 1,
          limit: params?.limit || 10,
          search: params?.search,
        },
      }),
      providesTags: (result) =>
        result
          ? [
              ...result.data.map(({ id }) => ({ type: "User", id })),
              { type: "User", id: "LIST" },
            ]
          : [{ type: "User", id: "LIST" }],
      // Cache for 5 minutes
      keepUnusedDataFor: 300,
      // Transform response
      transformResponse: (response) => ({
        data: response.users,
        total: response.total,
        hasMore: response.hasMore,
      }),
    }),

    getUser: builder.query({
      query: (id) => `users/${id}`,
      providesTags: (result, error, id) => [{ type: "User", id }],
      // Cache indefinitely until invalidated
      keepUnusedDataFor: Infinity,
    }),

    updateUser: builder.mutation({
      query: ({ id, ...patch }) => ({
        url: `users/${id}`,
        method: "PATCH",
        body: patch,
      }),
      invalidatesTags: (result, error, { id }) => [
        { type: "User", id },
        { type: "User", id: "LIST" },
      ],
      // Optimistic update
      async onQueryStarted({ id, ...patch }, { dispatch, queryFulfilled }) {
        const patchResult = dispatch(
          api.util.updateQueryData("getUser", id, (draft) => {
            Object.assign(draft, patch);
          })
        );

        try {
          await queryFulfilled;
        } catch {
          patchResult.undo();
        }
      },
    }),

    // Posts with relationship caching
    getPosts: builder.query({
      query: (userId) => `users/${userId}/posts`,
      providesTags: (result, error, userId) =>
        result
          ? [
              ...result.map(({ id }) => ({ type: "Post", id })),
              { type: "Post", id: `USER_${userId}` },
            ]
          : [{ type: "Post", id: `USER_${userId}` }],
    }),

    createPost: builder.mutation({
      query: ({ userId, ...post }) => ({
        url: `users/${userId}/posts`,
        method: "POST",
        body: post,
      }),
      invalidatesTags: (result, error, { userId }) => [
        { type: "Post", id: `USER_${userId}` },
      ],
      // Optimistic update for posts list
      async onQueryStarted({ userId, ...post }, { dispatch, queryFulfilled }) {
        const optimisticPost = {
          id: `temp-${Date.now()}`,
          ...post,
          userId,
          createdAt: new Date().toISOString(),
          isOptimistic: true,
        };

        const patchResult = dispatch(
          api.util.updateQueryData("getPosts", userId, (draft) => {
            draft.unshift(optimisticPost);
          })
        );

        try {
          const { data: newPost } = await queryFulfilled;

          // Replace optimistic post with real post
          dispatch(
            api.util.updateQueryData("getPosts", userId, (draft) => {
              const index = draft.findIndex((p) => p.id === optimisticPost.id);
              if (index !== -1) {
                draft[index] = newPost;
              }
            })
          );
        } catch {
          patchResult.undo();
        }
      },
    }),
  }),
});

export const {
  useGetUsersQuery,
  useGetUserQuery,
  useUpdateUserMutation,
  useGetPostsQuery,
  useCreatePostMutation,
} = api;

// Manual cache management
export const cacheUtils = {
  // Prefetch data
  prefetchUser: (id) => (dispatch) => {
    dispatch(api.util.prefetch("getUser", id, { force: false }));
  },

  // Invalidate specific cache
  invalidateUser: (id) => (dispatch) => {
    dispatch(api.util.invalidateTags([{ type: "User", id }]));
  },

  // Update cache manually
  updateUserCache: (id, updates) => (dispatch) => {
    dispatch(
      api.util.updateQueryData("getUser", id, (draft) => {
        Object.assign(draft, updates);
      })
    );
  },

  // Reset all cache
  resetCache: () => (dispatch) => {
    dispatch(api.util.resetApiState());
  },
};
```

**Custom Redux Caching Layer:**

```javascript
// Custom caching slice
import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";

const createCacheSlice = (name, fetchFn) => {
  const fetchData = createAsyncThunk(
    `${name}/fetchData`,
    async (key, { getState, rejectWithValue }) => {
      const state = getState()[name];
      const cached = state.cache[key];

      // Check if cache is still valid
      if (cached && Date.now() - cached.timestamp < cached.ttl) {
        return { key, data: cached.data, fromCache: true };
      }

      try {
        const data = await fetchFn(key);
        return { key, data, fromCache: false };
      } catch (error) {
        return rejectWithValue(error.message);
      }
    }
  );

  const slice = createSlice({
    name,
    initialState: {
      cache: {},
      loading: {},
      errors: {},
      lastFetch: {},
    },
    reducers: {
      setCacheData: (state, action) => {
        const { key, data, ttl = 300000 } = action.payload; // 5 min default TTL
        state.cache[key] = {
          data,
          timestamp: Date.now(),
          ttl,
        };
        delete state.errors[key];
      },

      invalidateCache: (state, action) => {
        const { keys } = action.payload;
        if (keys) {
          keys.forEach((key) => {
            delete state.cache[key];
            delete state.lastFetch[key];
          });
        } else {
          // Clear all cache
          state.cache = {};
          state.lastFetch = {};
        }
      },

      updateCacheData: (state, action) => {
        const { key, updates } = action.payload;
        if (state.cache[key]) {
          state.cache[key].data = {
            ...state.cache[key].data,
            ...updates,
          };
        }
      },

      removeCacheEntry: (state, action) => {
        const { key } = action.payload;
        delete state.cache[key];
        delete state.loading[key];
        delete state.errors[key];
        delete state.lastFetch[key];
      },
    },
    extraReducers: (builder) => {
      builder
        .addCase(fetchData.pending, (state, action) => {
          const key = action.meta.arg;
          state.loading[key] = true;
          delete state.errors[key];
        })
        .addCase(fetchData.fulfilled, (state, action) => {
          const { key, data, fromCache } = action.payload;
          state.loading[key] = false;

          if (!fromCache) {
            state.cache[key] = {
              data,
              timestamp: Date.now(),
              ttl: 300000, // 5 minutes
            };
            state.lastFetch[key] = Date.now();
          }
        })
        .addCase(fetchData.rejected, (state, action) => {
          const key = action.meta.arg;
          state.loading[key] = false;
          state.errors[key] = action.payload;
        });
    },
  });

  return {
    slice,
    actions: { ...slice.actions, fetchData },
    selectors: {
      selectCacheData: (key) => (state) => state[name].cache[key]?.data,
      selectIsLoading: (key) => (state) => state[name].loading[key] || false,
      selectError: (key) => (state) => state[name].errors[key],
      selectCacheInfo: (key) => (state) => {
        const cached = state[name].cache[key];
        return cached
          ? {
              hasData: true,
              isStale: Date.now() - cached.timestamp > cached.ttl,
              age: Date.now() - cached.timestamp,
            }
          : { hasData: false };
      },
    },
  };
};

// Usage
const userCache = createCacheSlice("userCache", async (userId) => {
  const response = await fetch(`/api/users/${userId}`);
  return response.json();
});

const postCache = createCacheSlice("postCache", async (postId) => {
  const response = await fetch(`/api/posts/${postId}`);
  return response.json();
});
```

**Zustand Caching Implementation:**

```javascript
import { create } from "zustand";
import { persist, subscribeWithSelector } from "zustand/middleware";
import { immer } from "zustand/middleware/immer";

// Cache store with advanced features
const useCacheStore = create(
  persist(
    subscribeWithSelector(
      immer((set, get) => ({
        // Cache data structure
        cache: new Map(),
        loading: new Set(),
        errors: new Map(),
        subscriptions: new Map(),

        // Cache configuration
        config: {
          defaultTTL: 5 * 60 * 1000, // 5 minutes
          maxCacheSize: 1000,
          staleWhileRevalidate: true,
        },

        // Core cache operations
        get: async (key, fetchFn, options = {}) => {
          const state = get();
          const cached = state.cache.get(key);
          const now = Date.now();

          // Return cached data if valid
          if (
            cached &&
            now - cached.timestamp < (options.ttl || state.config.defaultTTL)
          ) {
            return cached.data;
          }

          // Return stale data while revalidating
          if (
            cached &&
            state.config.staleWhileRevalidate &&
            !state.loading.has(key)
          ) {
            // Start background revalidation
            state.revalidate(key, fetchFn, options);
            return cached.data;
          }

          // Fetch fresh data
          return state.fetch(key, fetchFn, options);
        },

        fetch: async (key, fetchFn, options = {}) => {
          const state = get();

          // Prevent duplicate requests
          if (state.loading.has(key)) {
            return new Promise((resolve, reject) => {
              const unsubscribe = useCacheStore.subscribe(
                (state) => state.loading.has(key),
                (isLoading) => {
                  if (!isLoading) {
                    unsubscribe();
                    const cached = state.cache.get(key);
                    if (cached) {
                      resolve(cached.data);
                    } else {
                      const error = state.errors.get(key);
                      reject(error || new Error("Fetch failed"));
                    }
                  }
                }
              );
            });
          }

          set((draft) => {
            draft.loading.add(key);
            draft.errors.delete(key);
          });

          try {
            const data = await fetchFn(key);

            set((draft) => {
              // Implement LRU eviction if cache is full
              if (draft.cache.size >= draft.config.maxCacheSize) {
                const oldestKey = draft.cache.keys().next().value;
                draft.cache.delete(oldestKey);
              }

              draft.cache.set(key, {
                data,
                timestamp: Date.now(),
                ttl: options.ttl || draft.config.defaultTTL,
              });
              draft.loading.delete(key);
            });

            return data;
          } catch (error) {
            set((draft) => {
              draft.loading.delete(key);
              draft.errors.set(key, error);
            });
            throw error;
          }
        },

        revalidate: async (key, fetchFn, options = {}) => {
          try {
            const data = await fetchFn(key);
            set((draft) => {
              draft.cache.set(key, {
                data,
                timestamp: Date.now(),
                ttl: options.ttl || draft.config.defaultTTL,
              });
            });
            return data;
          } catch (error) {
            console.warn(`Revalidation failed for ${key}:`, error);
            return null;
          }
        },

        set: (key, data, options = {}) => {
          set((draft) => {
            draft.cache.set(key, {
              data,
              timestamp: Date.now(),
              ttl: options.ttl || draft.config.defaultTTL,
            });
            draft.errors.delete(key);
          });
        },

        update: (key, updater) => {
          set((draft) => {
            const cached = draft.cache.get(key);
            if (cached) {
              const updatedData =
                typeof updater === "function"
                  ? updater(cached.data)
                  : { ...cached.data, ...updater };

              draft.cache.set(key, {
                ...cached,
                data: updatedData,
              });
            }
          });
        },

        invalidate: (keys) => {
          set((draft) => {
            if (Array.isArray(keys)) {
              keys.forEach((key) => {
                draft.cache.delete(key);
                draft.errors.delete(key);
              });
            } else if (keys) {
              draft.cache.delete(keys);
              draft.errors.delete(keys);
            } else {
              // Clear all cache
              draft.cache.clear();
              draft.errors.clear();
            }
          });
        },

        // Subscription management
        subscribe: (key, callback) => {
          const state = get();
          const subscribers = state.subscriptions.get(key) || new Set();
          subscribers.add(callback);

          set((draft) => {
            draft.subscriptions.set(key, subscribers);
          });

          // Return unsubscribe function
          return () => {
            const currentSubscribers = get().subscriptions.get(key);
            if (currentSubscribers) {
              currentSubscribers.delete(callback);
              if (currentSubscribers.size === 0) {
                set((draft) => {
                  draft.subscriptions.delete(key);
                });
              }
            }
          };
        },

        // Utility methods
        getCacheInfo: (key) => {
          const state = get();
          const cached = state.cache.get(key);
          const now = Date.now();

          if (!cached) {
            return { exists: false };
          }

          return {
            exists: true,
            age: now - cached.timestamp,
            isStale: now - cached.timestamp > cached.ttl,
            size: JSON.stringify(cached.data).length,
          };
        },

        getStats: () => {
          const state = get();
          return {
            cacheSize: state.cache.size,
            loadingCount: state.loading.size,
            errorCount: state.errors.size,
            subscriptionCount: state.subscriptions.size,
            totalMemory: Array.from(state.cache.values()).reduce(
              (total, item) => total + JSON.stringify(item.data).length,
              0
            ),
          };
        },

        cleanup: () => {
          const state = get();
          const now = Date.now();

          set((draft) => {
            // Remove expired entries
            for (const [key, cached] of draft.cache) {
              if (now - cached.timestamp > cached.ttl) {
                draft.cache.delete(key);
                draft.errors.delete(key);
              }
            }
          });
        },
      }))
    ),
    {
      name: "cache-store",
      // Only persist cache data, not loading/error states
      partialize: (state) => ({ cache: state.cache }),
      // Custom serialization for Map
      serialize: (state) =>
        JSON.stringify({
          ...state,
          cache: Array.from(state.cache.entries()),
        }),
      deserialize: (str) => {
        const parsed = JSON.parse(str);
        return {
          ...parsed,
          cache: new Map(parsed.cache || []),
        };
      },
    }
  )
);

// Higher-order hook for cached data fetching
const useCachedData = (key, fetchFn, options = {}) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const cacheStore = useCacheStore();

  const fetchData = useCallback(async () => {
    setLoading(true);
    setError(null);

    try {
      const result = await cacheStore.get(key, fetchFn, options);
      setData(result);
    } catch (err) {
      setError(err);
    } finally {
      setLoading(false);
    }
  }, [key, fetchFn, options, cacheStore]);

  useEffect(() => {
    fetchData();
  }, [fetchData]);

  // Subscribe to cache changes
  useEffect(() => {
    const unsubscribe = cacheStore.subscribe(key, (newData) => {
      setData(newData);
    });

    return unsubscribe;
  }, [key, cacheStore]);

  const refetch = useCallback(() => {
    cacheStore.invalidate(key);
    fetchData();
  }, [key, cacheStore, fetchData]);

  const updateData = useCallback(
    (updater) => {
      cacheStore.update(key, updater);
    },
    [key, cacheStore]
  );

  return {
    data,
    loading,
    error,
    refetch,
    updateData,
    cacheInfo: cacheStore.getCacheInfo(key),
  };
};

// Usage examples
const UserProfile = ({ userId }) => {
  const {
    data: user,
    loading,
    error,
    refetch,
    updateData,
  } = useCachedData(
    `user-${userId}`,
    async () => {
      const response = await fetch(`/api/users/${userId}`);
      return response.json();
    },
    { ttl: 10 * 60 * 1000 } // 10 minutes
  );

  const handleUpdateName = (newName) => {
    updateData((currentUser) => ({
      ...currentUser,
      name: newName,
    }));
  };

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;
  if (!user) return <div>No user found</div>;

  return (
    <div>
      <h1>{user.name}</h1>
      <p>{user.email}</p>
      <button onClick={refetch}>Refresh</button>
      <button onClick={() => handleUpdateName("New Name")}>Update Name</button>
    </div>
  );
};
```

**Data Synchronization Patterns:**

```javascript
// Real-time synchronization with WebSocket
const useRealtimeSync = () => {
  const cacheStore = useCacheStore();

  useEffect(() => {
    const ws = new WebSocket("ws://localhost:8080");

    ws.onmessage = (event) => {
      const { type, key, data } = JSON.parse(event.data);

      switch (type) {
        case "UPDATE":
          cacheStore.set(key, data);
          break;
        case "DELETE":
          cacheStore.invalidate(key);
          break;
        case "INVALIDATE":
          cacheStore.invalidate(key);
          break;
      }
    };

    return () => ws.close();
  }, [cacheStore]);
};

// Periodic background sync
const useBackgroundSync = (keys, fetchFunctions, interval = 60000) => {
  const cacheStore = useCacheStore();

  useEffect(() => {
    const syncData = async () => {
      for (let i = 0; i < keys.length; i++) {
        const key = keys[i];
        const fetchFn = fetchFunctions[i];

        try {
          await cacheStore.revalidate(key, fetchFn);
        } catch (error) {
          console.warn(`Background sync failed for ${key}:`, error);
        }
      }
    };

    const intervalId = setInterval(syncData, interval);

    return () => clearInterval(intervalId);
  }, [keys, fetchFunctions, interval, cacheStore]);
};

// Optimistic updates with rollback
const useOptimisticUpdate = () => {
  const cacheStore = useCacheStore();

  const performOptimisticUpdate = async (key, optimisticData, updateFn) => {
    // Store original data for rollback
    const originalData = cacheStore.cache.get(key)?.data;

    // Apply optimistic update
    cacheStore.set(key, optimisticData);

    try {
      // Perform actual update
      const result = await updateFn();

      // Update with real data
      cacheStore.set(key, result);

      return result;
    } catch (error) {
      // Rollback on error
      if (originalData) {
        cacheStore.set(key, originalData);
      } else {
        cacheStore.invalidate(key);
      }

      throw error;
    }
  };

  return { performOptimisticUpdate };
};
```

**Comparison Summary:**

| Feature                | Redux (RTK Query)                                      | Zustand Custom Cache               |
| ---------------------- | ------------------------------------------------------ | ---------------------------------- |
| **Setup Complexity**   | Medium (requires RTK setup)                            | Low (simple store creation)        |
| **Built-in Features**  | Comprehensive (tags, invalidation, optimistic updates) | Custom implementation needed       |
| **Bundle Size**        | Larger (RTK Query + Redux)                             | Smaller (minimal dependencies)     |
| **TypeScript Support** | Excellent (auto-generated types)                       | Good (manual typing)               |
| **DevTools**           | Excellent Redux DevTools integration                   | Basic Zustand DevTools             |
| **Caching Strategy**   | Tag-based invalidation                                 | TTL-based with manual invalidation |
| **Real-time Updates**  | Manual implementation                                  | Easy WebSocket integration         |
| **Persistence**        | Requires additional setup                              | Built-in with persist middleware   |
| **Learning Curve**     | Steeper (RTK Query concepts)                           | Gentler (straightforward API)      |
| **Flexibility**        | Structured approach                                    | Highly customizable                |

**Best Practices:**

1. **Choose the right strategy** based on your application's complexity and requirements
2. **Implement proper cache invalidation** to prevent stale data issues
3. **Use optimistic updates** for better user experience
4. **Monitor cache performance** and implement cleanup strategies
5. **Handle offline scenarios** with appropriate fallback mechanisms
6. **Implement proper error handling** and retry logic
7. **Use background synchronization** for critical data
8. **Consider memory usage** and implement cache size limits
9. **Test caching behavior** thoroughly, especially edge cases
10. **Document your caching strategy** for team understanding

Both approaches offer powerful caching capabilities, with Redux providing more structure and Zustand offering more flexibility for custom implementations.

---

### Q34: How do you handle concurrent updates and race conditions in Redux vs Zustand?

**Answer:**
Concurrent updates and race conditions are common challenges in modern applications, especially when dealing with asynchronous operations, real-time updates, and multiple user interactions. Both Redux and Zustand provide different approaches to handle these scenarios.

**Redux Race Condition Handling:**

```javascript
// Redux Toolkit with race condition handling
import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";

// Async thunk with race condition protection
const fetchUserWithRaceProtection = createAsyncThunk(
  "user/fetchUser",
  async (userId, { getState, signal, rejectWithValue }) => {
    // Check if request is already in progress
    const state = getState();
    if (state.user.loading[userId]) {
      return rejectWithValue("Request already in progress");
    }

    try {
      const response = await fetch(`/api/users/${userId}`, {
        signal, // AbortController signal for cancellation
      });

      if (!response.ok) {
        throw new Error("Failed to fetch user");
      }

      return await response.json();
    } catch (error) {
      if (error.name === "AbortError") {
        return rejectWithValue("Request was cancelled");
      }
      throw error;
    }
  },
  {
    condition: (userId, { getState }) => {
      // Prevent duplicate requests
      const state = getState();
      return !state.user.loading[userId];
    },
  }
);

// Advanced async thunk with request deduplication
const createDedupedAsyncThunk = (typePrefix, payloadCreator) => {
  const pendingRequests = new Map();

  return createAsyncThunk(typePrefix, async (arg, thunkAPI) => {
    const key = JSON.stringify(arg);

    // Return existing promise if request is already pending
    if (pendingRequests.has(key)) {
      return pendingRequests.get(key);
    }

    const promise = payloadCreator(arg, thunkAPI);
    pendingRequests.set(key, promise);

    try {
      const result = await promise;
      pendingRequests.delete(key);
      return result;
    } catch (error) {
      pendingRequests.delete(key);
      throw error;
    }
  });
};

// Usage of deduped async thunk
const fetchUserDeduped = createDedupedAsyncThunk(
  "user/fetchUserDeduped",
  async (userId, { signal }) => {
    const response = await fetch(`/api/users/${userId}`, { signal });
    return response.json();
  }
);

// User slice with concurrent update handling
const userSlice = createSlice({
  name: "user",
  initialState: {
    entities: {},
    loading: {},
    errors: {},
    lastUpdated: {},
    optimisticUpdates: {},
    requestIds: {}, // Track request IDs for cancellation
  },
  reducers: {
    // Optimistic update with conflict resolution
    updateUserOptimistic: (state, action) => {
      const { userId, updates, requestId } = action.payload;
      const timestamp = Date.now();

      // Store optimistic update
      state.optimisticUpdates[userId] = {
        updates,
        timestamp,
        requestId,
      };

      // Apply optimistic update
      if (state.entities[userId]) {
        state.entities[userId] = {
          ...state.entities[userId],
          ...updates,
          _optimistic: true,
          _optimisticTimestamp: timestamp,
        };
      }
    },

    // Resolve optimistic update
    resolveOptimisticUpdate: (state, action) => {
      const { userId, serverData, requestId } = action.payload;
      const optimistic = state.optimisticUpdates[userId];

      if (optimistic && optimistic.requestId === requestId) {
        // Remove optimistic flag and apply server data
        state.entities[userId] = {
          ...serverData,
          _optimistic: false,
        };
        delete state.optimisticUpdates[userId];
        state.lastUpdated[userId] = Date.now();
      }
    },

    // Handle conflicting updates
    handleUpdateConflict: (state, action) => {
      const {
        userId,
        localUpdates,
        serverData,
        strategy = "server-wins",
      } = action.payload;

      switch (strategy) {
        case "server-wins":
          state.entities[userId] = serverData;
          break;

        case "client-wins":
          state.entities[userId] = {
            ...serverData,
            ...localUpdates,
          };
          break;

        case "merge":
          // Custom merge logic
          state.entities[userId] = mergeUpdates(serverData, localUpdates);
          break;

        case "manual":
          // Store conflict for manual resolution
          state.entities[userId] = {
            ...serverData,
            _conflict: {
              local: localUpdates,
              server: serverData,
              timestamp: Date.now(),
            },
          };
          break;
      }

      delete state.optimisticUpdates[userId];
    },

    // Cancel pending request
    cancelRequest: (state, action) => {
      const { userId } = action.payload;
      delete state.loading[userId];
      delete state.requestIds[userId];
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchUserWithRaceProtection.pending, (state, action) => {
        const userId = action.meta.arg;
        state.loading[userId] = true;
        state.requestIds[userId] = action.meta.requestId;
        delete state.errors[userId];
      })
      .addCase(fetchUserWithRaceProtection.fulfilled, (state, action) => {
        const userId = action.meta.arg;
        const requestId = action.meta.requestId;

        // Only update if this is the latest request
        if (state.requestIds[userId] === requestId) {
          state.entities[userId] = action.payload;
          state.loading[userId] = false;
          state.lastUpdated[userId] = Date.now();
          delete state.requestIds[userId];
        }
      })
      .addCase(fetchUserWithRaceProtection.rejected, (state, action) => {
        const userId = action.meta.arg;
        const requestId = action.meta.requestId;

        // Only update error if this is the latest request
        if (state.requestIds[userId] === requestId) {
          state.loading[userId] = false;
          state.errors[userId] = action.payload;
          delete state.requestIds[userId];
        }
      });
  },
});

// Custom merge function for conflict resolution
const mergeUpdates = (serverData, localUpdates) => {
  const merged = { ...serverData };

  // Custom merge logic based on field types
  Object.keys(localUpdates).forEach((key) => {
    if (key === "name" || key === "email") {
      // Client wins for user-editable fields
      merged[key] = localUpdates[key];
    } else if (key === "lastLogin" || key === "createdAt") {
      // Server wins for system fields
      merged[key] = serverData[key];
    } else if (
      typeof localUpdates[key] === "number" &&
      typeof serverData[key] === "number"
    ) {
      // Take the maximum for numeric fields
      merged[key] = Math.max(localUpdates[key], serverData[key]);
    } else {
      // Default to local updates
      merged[key] = localUpdates[key];
    }
  });

  return merged;
};

// Middleware for handling concurrent updates
const concurrentUpdateMiddleware = (store) => (next) => (action) => {
  if (action.type.endsWith("/pending")) {
    const state = store.getState();
    const userId = action.meta?.arg;

    // Cancel previous request if exists
    if (userId && state.user.requestIds[userId]) {
      // Dispatch cancel action for previous request
      store.dispatch(userSlice.actions.cancelRequest({ userId }));
    }
  }

  return next(action);
};

export const {
  updateUserOptimistic,
  resolveOptimisticUpdate,
  handleUpdateConflict,
} = userSlice.actions;
```

**Zustand Concurrent Update Handling:**

```javascript
import { create } from "zustand";
import { subscribeWithSelector } from "zustand/middleware";
import { immer } from "zustand/middleware/immer";

// Zustand store with race condition protection
const useUserStore = create(
  subscribeWithSelector(
    immer((set, get) => ({
      users: new Map(),
      loading: new Set(),
      errors: new Map(),
      pendingRequests: new Map(),
      optimisticUpdates: new Map(),
      lastUpdated: new Map(),

      // Fetch user with race protection
      fetchUser: async (userId) => {
        const state = get();

        // Check if request is already pending
        if (state.loading.has(userId)) {
          return state.pendingRequests.get(userId);
        }

        // Create abort controller for cancellation
        const abortController = new AbortController();

        const fetchPromise = (async () => {
          set((draft) => {
            draft.loading.add(userId);
            draft.errors.delete(userId);
          });

          try {
            const response = await fetch(`/api/users/${userId}`, {
              signal: abortController.signal,
            });

            if (!response.ok) {
              throw new Error("Failed to fetch user");
            }

            const userData = await response.json();

            set((draft) => {
              // Only update if request wasn't cancelled
              if (draft.loading.has(userId)) {
                draft.users.set(userId, userData);
                draft.loading.delete(userId);
                draft.lastUpdated.set(userId, Date.now());
                draft.pendingRequests.delete(userId);
              }
            });

            return userData;
          } catch (error) {
            if (error.name !== "AbortError") {
              set((draft) => {
                draft.loading.delete(userId);
                draft.errors.set(userId, error.message);
                draft.pendingRequests.delete(userId);
              });
            }
            throw error;
          }
        })();

        // Store promise and abort controller
        set((draft) => {
          draft.pendingRequests.set(userId, {
            promise: fetchPromise,
            abortController,
          });
        });

        return fetchPromise;
      },

      // Cancel pending request
      cancelRequest: (userId) => {
        const state = get();
        const pending = state.pendingRequests.get(userId);

        if (pending) {
          pending.abortController.abort();

          set((draft) => {
            draft.loading.delete(userId);
            draft.pendingRequests.delete(userId);
          });
        }
      },

      // Optimistic update with conflict resolution
      updateUserOptimistic: async (userId, updates, updateFn) => {
        const state = get();
        const originalUser = state.users.get(userId);
        const requestId = `${userId}-${Date.now()}`;

        // Apply optimistic update
        set((draft) => {
          const currentUser = draft.users.get(userId);
          if (currentUser) {
            const optimisticUser = { ...currentUser, ...updates };
            draft.users.set(userId, optimisticUser);
            draft.optimisticUpdates.set(userId, {
              original: originalUser,
              updates,
              requestId,
              timestamp: Date.now(),
            });
          }
        });

        try {
          // Perform actual update
          const serverData = await updateFn(userId, updates);

          set((draft) => {
            const optimistic = draft.optimisticUpdates.get(userId);

            // Only apply if this is the latest optimistic update
            if (optimistic && optimistic.requestId === requestId) {
              draft.users.set(userId, serverData);
              draft.optimisticUpdates.delete(userId);
              draft.lastUpdated.set(userId, Date.now());
            }
          });

          return serverData;
        } catch (error) {
          // Rollback optimistic update
          set((draft) => {
            const optimistic = draft.optimisticUpdates.get(userId);

            if (optimistic && optimistic.requestId === requestId) {
              if (optimistic.original) {
                draft.users.set(userId, optimistic.original);
              } else {
                draft.users.delete(userId);
              }
              draft.optimisticUpdates.delete(userId);
            }
          });

          throw error;
        }
      },

      // Handle concurrent updates with different strategies
      handleConcurrentUpdate: (
        userId,
        localUpdates,
        serverData,
        strategy = "server-wins"
      ) => {
        set((draft) => {
          switch (strategy) {
            case "server-wins":
              draft.users.set(userId, serverData);
              break;

            case "client-wins":
              draft.users.set(userId, { ...serverData, ...localUpdates });
              break;

            case "merge":
              const merged = mergeUserData(serverData, localUpdates);
              draft.users.set(userId, merged);
              break;

            case "timestamp":
              // Use timestamps to determine winner
              const localTimestamp = localUpdates._timestamp || 0;
              const serverTimestamp = serverData._timestamp || 0;

              if (localTimestamp > serverTimestamp) {
                draft.users.set(userId, { ...serverData, ...localUpdates });
              } else {
                draft.users.set(userId, serverData);
              }
              break;

            case "field-level":
              // Merge at field level based on timestamps
              const fieldMerged = mergeByFieldTimestamps(
                serverData,
                localUpdates
              );
              draft.users.set(userId, fieldMerged);
              break;
          }

          draft.optimisticUpdates.delete(userId);
          draft.lastUpdated.set(userId, Date.now());
        });
      },

      // Batch updates to prevent race conditions
      batchUpdate: (updates) => {
        set((draft) => {
          updates.forEach(({ userId, data }) => {
            draft.users.set(userId, data);
            draft.lastUpdated.set(userId, Date.now());
          });
        });
      },

      // Debounced update to prevent excessive API calls
      debouncedUpdate: (() => {
        const debounceMap = new Map();

        return (userId, updates, delay = 500) => {
          // Clear existing timeout
          if (debounceMap.has(userId)) {
            clearTimeout(debounceMap.get(userId));
          }

          // Apply immediate optimistic update
          set((draft) => {
            const currentUser = draft.users.get(userId);
            if (currentUser) {
              draft.users.set(userId, { ...currentUser, ...updates });
            }
          });

          // Set new timeout for actual update
          const timeoutId = setTimeout(async () => {
            try {
              const response = await fetch(`/api/users/${userId}`, {
                method: "PATCH",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(updates),
              });

              const serverData = await response.json();

              set((draft) => {
                draft.users.set(userId, serverData);
                draft.lastUpdated.set(userId, Date.now());
              });
            } catch (error) {
              console.error("Debounced update failed:", error);
              // Could implement retry logic here
            } finally {
              debounceMap.delete(userId);
            }
          }, delay);

          debounceMap.set(userId, timeoutId);
        };
      })(),
    }))
  )
);

// Helper functions for merging data
const mergeUserData = (serverData, localUpdates) => {
  const merged = { ...serverData };

  // Custom merge logic
  Object.keys(localUpdates).forEach((key) => {
    if (key.startsWith("_")) {
      // Skip internal fields
      return;
    }

    if (key === "preferences" && typeof localUpdates[key] === "object") {
      // Deep merge for preferences
      merged[key] = { ...serverData[key], ...localUpdates[key] };
    } else {
      merged[key] = localUpdates[key];
    }
  });

  return merged;
};

const mergeByFieldTimestamps = (serverData, localUpdates) => {
  const merged = { ...serverData };

  Object.keys(localUpdates).forEach((key) => {
    const localTimestamp = localUpdates[`${key}_timestamp`] || 0;
    const serverTimestamp = serverData[`${key}_timestamp`] || 0;

    if (localTimestamp >= serverTimestamp) {
      merged[key] = localUpdates[key];
      merged[`${key}_timestamp`] = localTimestamp;
    }
  });

  return merged;
};

// React hook for handling concurrent updates
const useUserWithConcurrency = (userId) => {
  const store = useUserStore();
  const [localUpdates, setLocalUpdates] = useState({});
  const [isConflicted, setIsConflicted] = useState(false);

  const user = store.users.get(userId);
  const loading = store.loading.has(userId);
  const error = store.errors.get(userId);

  // Fetch user on mount
  useEffect(() => {
    if (userId && !user && !loading) {
      store.fetchUser(userId);
    }
  }, [userId, user, loading, store]);

  // Handle optimistic updates
  const updateUser = useCallback(
    async (updates) => {
      setLocalUpdates((prev) => ({ ...prev, ...updates }));

      try {
        await store.updateUserOptimistic(userId, updates, async (id, data) => {
          const response = await fetch(`/api/users/${id}`, {
            method: "PATCH",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data),
          });
          return response.json();
        });

        setLocalUpdates({});
        setIsConflicted(false);
      } catch (error) {
        console.error("Update failed:", error);
        setIsConflicted(true);
      }
    },
    [userId, store]
  );

  // Resolve conflicts
  const resolveConflict = useCallback(
    (strategy) => {
      if (isConflicted && user) {
        store.handleConcurrentUpdate(userId, localUpdates, user, strategy);
        setLocalUpdates({});
        setIsConflicted(false);
      }
    },
    [userId, localUpdates, user, isConflicted, store]
  );

  return {
    user,
    loading,
    error,
    updateUser,
    localUpdates,
    isConflicted,
    resolveConflict,
  };
};
```

**Advanced Race Condition Patterns:**

```javascript
// Request deduplication utility
class RequestDeduplicator {
  constructor() {
    this.pendingRequests = new Map();
  }

  async dedupe(key, requestFn) {
    if (this.pendingRequests.has(key)) {
      return this.pendingRequests.get(key);
    }

    const promise = requestFn().finally(() => {
      this.pendingRequests.delete(key);
    });

    this.pendingRequests.set(key, promise);
    return promise;
  }

  cancel(key) {
    this.pendingRequests.delete(key);
  }

  cancelAll() {
    this.pendingRequests.clear();
  }
}

// Optimistic update manager
class OptimisticUpdateManager {
  constructor() {
    this.updates = new Map();
    this.conflicts = new Map();
  }

  apply(key, optimisticData, originalData) {
    this.updates.set(key, {
      optimistic: optimisticData,
      original: originalData,
      timestamp: Date.now(),
    });
  }

  resolve(key, serverData) {
    const update = this.updates.get(key);
    if (!update) return serverData;

    // Check for conflicts
    const hasConflict = this.detectConflict(update.optimistic, serverData);

    if (hasConflict) {
      this.conflicts.set(key, {
        local: update.optimistic,
        server: serverData,
        original: update.original,
        timestamp: Date.now(),
      });
      return update.optimistic; // Keep optimistic data for manual resolution
    }

    this.updates.delete(key);
    return serverData;
  }

  rollback(key) {
    const update = this.updates.get(key);
    if (update) {
      this.updates.delete(key);
      return update.original;
    }
    return null;
  }

  detectConflict(optimisticData, serverData) {
    // Simple conflict detection - can be customized
    return JSON.stringify(optimisticData) !== JSON.stringify(serverData);
  }

  getConflicts() {
    return Array.from(this.conflicts.entries());
  }

  resolveConflict(key, strategy = "server-wins") {
    const conflict = this.conflicts.get(key);
    if (!conflict) return null;

    let resolved;
    switch (strategy) {
      case "server-wins":
        resolved = conflict.server;
        break;
      case "client-wins":
        resolved = conflict.local;
        break;
      case "merge":
        resolved = { ...conflict.server, ...conflict.local };
        break;
      default:
        resolved = conflict.server;
    }

    this.conflicts.delete(key);
    return resolved;
  }
}

// Usage in components
const UserEditor = ({ userId }) => {
  const { user, updateUser, isConflicted, resolveConflict } =
    useUserWithConcurrency(userId);
  const [formData, setFormData] = useState({});

  useEffect(() => {
    if (user) {
      setFormData(user);
    }
  }, [user]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await updateUser(formData);
    } catch (error) {
      console.error("Update failed:", error);
    }
  };

  if (isConflicted) {
    return (
      <div className="conflict-resolution">
        <h3>Conflict Detected</h3>
        <p>
          The data has been modified by another user. How would you like to
          resolve this?
        </p>

        <button onClick={() => resolveConflict("server-wins")}>
          Use Server Version
        </button>
        <button onClick={() => resolveConflict("client-wins")}>
          Keep My Changes
        </button>
        <button onClick={() => resolveConflict("merge")}>Merge Changes</button>
      </div>
    );
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        value={formData.name || ""}
        onChange={(e) =>
          setFormData((prev) => ({ ...prev, name: e.target.value }))
        }
        placeholder="Name"
      />
      <input
        value={formData.email || ""}
        onChange={(e) =>
          setFormData((prev) => ({ ...prev, email: e.target.value }))
        }
        placeholder="Email"
      />
      <button type="submit">Update User</button>
    </form>
  );
};
```

**Comparison Summary:**

| Feature                      | Redux                                     | Zustand                               |
| ---------------------------- | ----------------------------------------- | ------------------------------------- |
| **Built-in Race Protection** | Limited (requires custom implementation)  | Flexible (easy to implement)          |
| **Request Deduplication**    | Manual with middleware                    | Simple with Map-based tracking        |
| **Optimistic Updates**       | RTK Query provides built-in support       | Custom implementation needed          |
| **Conflict Resolution**      | Requires custom logic                     | Highly customizable strategies        |
| **Cancellation Support**     | AbortController with thunks               | Easy integration with AbortController |
| **Debugging**                | Excellent with Redux DevTools             | Basic debugging capabilities          |
| **Performance**              | Can be heavy with many concurrent updates | Lightweight and efficient             |
| **Learning Curve**           | Steeper (RTK patterns)                    | Gentler (straightforward API)         |

**Best Practices:**

1. **Always handle request cancellation** to prevent memory leaks
2. **Implement request deduplication** for expensive operations
3. **Use optimistic updates** for better user experience
4. **Provide conflict resolution strategies** for concurrent modifications
5. **Debounce rapid updates** to reduce server load
6. **Use timestamps** for conflict detection and resolution
7. **Implement proper error handling** and rollback mechanisms
8. **Test concurrent scenarios** thoroughly
9. **Monitor and log** race conditions for debugging
10. **Document your concurrency strategy** for team understanding

Both Redux and Zustand can effectively handle concurrent updates, with Redux providing more structured patterns through RTK Query and Zustand offering more flexibility for custom implementations.

---

### Q35: How do you implement internationalization (i18n) and localization patterns in Redux vs Zustand?

**Answer:**
Internationalization (i18n) and localization (l10n) are crucial for building applications that serve global audiences. Both Redux and Zustand can effectively manage language preferences, translations, and locale-specific data.

**Redux i18n Implementation:**

```javascript
// Redux Toolkit i18n slice
import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";

// Async thunk for loading translations
const loadTranslations = createAsyncThunk(
  "i18n/loadTranslations",
  async ({ locale, namespace = "common" }, { rejectWithValue }) => {
    try {
      const response = await fetch(
        `/api/translations/${locale}/${namespace}.json`
      );

      if (!response.ok) {
        throw new Error(
          `Failed to load translations for ${locale}/${namespace}`
        );
      }

      const translations = await response.json();
      return { locale, namespace, translations };
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);

// Async thunk for loading locale data
const loadLocaleData = createAsyncThunk(
  "i18n/loadLocaleData",
  async (locale, { rejectWithValue }) => {
    try {
      const [dateFormats, numberFormats, currencyData] = await Promise.all([
        fetch(`/api/locales/${locale}/date-formats.json`).then((r) => r.json()),
        fetch(`/api/locales/${locale}/number-formats.json`).then((r) =>
          r.json()
        ),
        fetch(`/api/locales/${locale}/currency.json`).then((r) => r.json()),
      ]);

      return {
        locale,
        dateFormats,
        numberFormats,
        currencyData,
      };
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);

// i18n slice
const i18nSlice = createSlice({
  name: "i18n",
  initialState: {
    currentLocale: "en-US",
    fallbackLocale: "en-US",
    supportedLocales: ["en-US", "es-ES", "fr-FR", "de-DE", "ja-JP", "zh-CN"],
    translations: {},
    localeData: {},
    loading: {},
    errors: {},
    direction: "ltr", // or 'rtl'
    loadedNamespaces: new Set(),
    pluralRules: {},
    interpolationOptions: {
      prefix: "{{",
      suffix: "}}",
      escapeValue: true,
    },
  },
  reducers: {
    // Set current locale
    setLocale: (state, action) => {
      const { locale, direction = "ltr" } = action.payload;

      if (state.supportedLocales.includes(locale)) {
        state.currentLocale = locale;
        state.direction = direction;

        // Update document attributes
        if (typeof document !== "undefined") {
          document.documentElement.lang = locale;
          document.documentElement.dir = direction;
        }
      }
    },

    // Add translations manually
    addTranslations: (state, action) => {
      const { locale, namespace, translations } = action.payload;

      if (!state.translations[locale]) {
        state.translations[locale] = {};
      }

      state.translations[locale][namespace] = {
        ...state.translations[locale][namespace],
        ...translations,
      };

      state.loadedNamespaces.add(`${locale}:${namespace}`);
    },

    // Set plural rules for a locale
    setPluralRules: (state, action) => {
      const { locale, rules } = action.payload;
      state.pluralRules[locale] = rules;
    },

    // Update interpolation options
    setInterpolationOptions: (state, action) => {
      state.interpolationOptions = {
        ...state.interpolationOptions,
        ...action.payload,
      };
    },

    // Clear translations for a locale
    clearTranslations: (state, action) => {
      const { locale, namespace } = action.payload;

      if (namespace) {
        delete state.translations[locale]?.[namespace];
        state.loadedNamespaces.delete(`${locale}:${namespace}`);
      } else {
        delete state.translations[locale];
        // Remove all namespaces for this locale
        state.loadedNamespaces.forEach((ns) => {
          if (ns.startsWith(`${locale}:`)) {
            state.loadedNamespaces.delete(ns);
          }
        });
      }
    },
  },
  extraReducers: (builder) => {
    builder
      // Load translations
      .addCase(loadTranslations.pending, (state, action) => {
        const { locale, namespace } = action.meta.arg;
        const key = `${locale}:${namespace}`;
        state.loading[key] = true;
        delete state.errors[key];
      })
      .addCase(loadTranslations.fulfilled, (state, action) => {
        const { locale, namespace, translations } = action.payload;
        const key = `${locale}:${namespace}`;

        if (!state.translations[locale]) {
          state.translations[locale] = {};
        }

        state.translations[locale][namespace] = translations;
        state.loading[key] = false;
        state.loadedNamespaces.add(key);
      })
      .addCase(loadTranslations.rejected, (state, action) => {
        const { locale, namespace } = action.meta.arg;
        const key = `${locale}:${namespace}`;
        state.loading[key] = false;
        state.errors[key] = action.payload;
      })

      // Load locale data
      .addCase(loadLocaleData.pending, (state, action) => {
        const locale = action.meta.arg;
        state.loading[`locale:${locale}`] = true;
        delete state.errors[`locale:${locale}`];
      })
      .addCase(loadLocaleData.fulfilled, (state, action) => {
        const { locale, dateFormats, numberFormats, currencyData } =
          action.payload;

        state.localeData[locale] = {
          dateFormats,
          numberFormats,
          currencyData,
        };

        state.loading[`locale:${locale}`] = false;
      })
      .addCase(loadLocaleData.rejected, (state, action) => {
        const locale = action.meta.arg;
        state.loading[`locale:${locale}`] = false;
        state.errors[`locale:${locale}`] = action.payload;
      });
  },
});

// Selectors
const selectCurrentLocale = (state) => state.i18n.currentLocale;
const selectDirection = (state) => state.i18n.direction;
const selectSupportedLocales = (state) => state.i18n.supportedLocales;

const selectTranslations = (state, locale, namespace = "common") => {
  return state.i18n.translations[locale]?.[namespace] || {};
};

const selectCurrentTranslations = (state, namespace = "common") => {
  const locale = selectCurrentLocale(state);
  return selectTranslations(state, locale, namespace);
};

const selectLocaleData = (state, locale) => {
  return state.i18n.localeData[locale];
};

const selectIsLoading = (state, locale, namespace) => {
  const key = namespace ? `${locale}:${namespace}` : `locale:${locale}`;
  return state.i18n.loading[key] || false;
};

// Translation function selector
const selectTranslationFunction = (state) => {
  const currentLocale = selectCurrentLocale(state);
  const fallbackLocale = state.i18n.fallbackLocale;
  const translations = state.i18n.translations;
  const interpolationOptions = state.i18n.interpolationOptions;

  return (key, options = {}) => {
    const { namespace = "common", values = {}, count, defaultValue } = options;

    // Get translation from current locale
    let translation = translations[currentLocale]?.[namespace]?.[key];

    // Fallback to fallback locale
    if (!translation && currentLocale !== fallbackLocale) {
      translation = translations[fallbackLocale]?.[namespace]?.[key];
    }

    // Use default value if no translation found
    if (!translation) {
      translation = defaultValue || key;
    }

    // Handle pluralization
    if (typeof count === "number" && typeof translation === "object") {
      const pluralRule = getPluralRule(currentLocale, count);
      translation =
        translation[pluralRule] || translation.other || translation.one;
    }

    // Interpolate values
    if (typeof translation === "string" && Object.keys(values).length > 0) {
      translation = interpolateString(
        translation,
        values,
        interpolationOptions
      );
    }

    return translation;
  };
};

// Helper functions
const getPluralRule = (locale, count) => {
  try {
    const pr = new Intl.PluralRules(locale);
    return pr.select(count);
  } catch {
    // Fallback for unsupported locales
    return count === 1 ? "one" : "other";
  }
};

const interpolateString = (str, values, options) => {
  const { prefix, suffix, escapeValue } = options;

  return str.replace(
    new RegExp(
      `${escapeRegExp(prefix)}([^${escapeRegExp(suffix)}]+)${escapeRegExp(
        suffix
      )}`,
      "g"
    ),
    (match, key) => {
      const value = values[key.trim()];
      if (value === undefined) return match;

      return escapeValue ? escapeHtml(String(value)) : String(value);
    }
  );
};

const escapeRegExp = (string) => {
  return string.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
};

const escapeHtml = (unsafe) => {
  return unsafe
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
};

// React hooks
const useTranslation = (namespace = "common") => {
  const dispatch = useDispatch();
  const currentLocale = useSelector(selectCurrentLocale);
  const t = useSelector(selectTranslationFunction);
  const isLoading = useSelector((state) =>
    selectIsLoading(state, currentLocale, namespace)
  );

  // Auto-load translations if not loaded
  useEffect(() => {
    const key = `${currentLocale}:${namespace}`;
    const loadedNamespaces = useSelector(
      (state) => state.i18n.loadedNamespaces
    );

    if (!loadedNamespaces.has(key) && !isLoading) {
      dispatch(loadTranslations({ locale: currentLocale, namespace }));
    }
  }, [currentLocale, namespace, dispatch, isLoading]);

  return {
    t: (key, options) => t(key, { ...options, namespace }),
    locale: currentLocale,
    isLoading,
  };
};

const useLocale = () => {
  const dispatch = useDispatch();
  const currentLocale = useSelector(selectCurrentLocale);
  const direction = useSelector(selectDirection);
  const supportedLocales = useSelector(selectSupportedLocales);

  const changeLocale = useCallback(
    (locale, dir) => {
      dispatch(i18nSlice.actions.setLocale({ locale, direction: dir }));
      dispatch(loadLocaleData(locale));
    },
    [dispatch]
  );

  return {
    locale: currentLocale,
    direction,
    supportedLocales,
    changeLocale,
  };
};

export const { setLocale, addTranslations, setPluralRules } = i18nSlice.actions;
export { loadTranslations, loadLocaleData };
export { useTranslation, useLocale };
```

**Zustand i18n Implementation:**

```javascript
import { create } from "zustand";
import { persist, subscribeWithSelector } from "zustand/middleware";
import { immer } from "zustand/middleware/immer";

// Zustand i18n store
const useI18nStore = create(
  persist(
    subscribeWithSelector(
      immer((set, get) => ({
        // State
        currentLocale: "en-US",
        fallbackLocale: "en-US",
        supportedLocales: [
          "en-US",
          "es-ES",
          "fr-FR",
          "de-DE",
          "ja-JP",
          "zh-CN",
        ],
        direction: "ltr",
        translations: new Map(),
        localeData: new Map(),
        loadingStates: new Map(),
        errors: new Map(),
        loadedNamespaces: new Set(),

        // Configuration
        interpolationOptions: {
          prefix: "{{",
          suffix: "}}",
          escapeValue: true,
        },

        // Actions
        setLocale: (locale, direction = "ltr") => {
          const state = get();

          if (state.supportedLocales.includes(locale)) {
            set((draft) => {
              draft.currentLocale = locale;
              draft.direction = direction;
            });

            // Update document attributes
            if (typeof document !== "undefined") {
              document.documentElement.lang = locale;
              document.documentElement.dir = direction;
            }

            // Auto-load locale data
            get().loadLocaleData(locale);
          }
        },

        // Load translations for a specific namespace
        loadTranslations: async (locale, namespace = "common") => {
          const state = get();
          const key = `${locale}:${namespace}`;

          // Check if already loaded or loading
          if (state.loadedNamespaces.has(key) || state.loadingStates.get(key)) {
            return;
          }

          set((draft) => {
            draft.loadingStates.set(key, true);
            draft.errors.delete(key);
          });

          try {
            const response = await fetch(
              `/api/translations/${locale}/${namespace}.json`
            );

            if (!response.ok) {
              throw new Error(
                `Failed to load translations for ${locale}/${namespace}`
              );
            }

            const translations = await response.json();

            set((draft) => {
              if (!draft.translations.has(locale)) {
                draft.translations.set(locale, new Map());
              }

              draft.translations.get(locale).set(namespace, translations);
              draft.loadedNamespaces.add(key);
              draft.loadingStates.set(key, false);
            });
          } catch (error) {
            set((draft) => {
              draft.loadingStates.set(key, false);
              draft.errors.set(key, error.message);
            });

            throw error;
          }
        },

        // Load locale-specific data (date formats, number formats, etc.)
        loadLocaleData: async (locale) => {
          const state = get();
          const key = `locale:${locale}`;

          if (state.localeData.has(locale) || state.loadingStates.get(key)) {
            return;
          }

          set((draft) => {
            draft.loadingStates.set(key, true);
            draft.errors.delete(key);
          });

          try {
            const [dateFormats, numberFormats, currencyData] =
              await Promise.all([
                fetch(`/api/locales/${locale}/date-formats.json`).then((r) =>
                  r.json()
                ),
                fetch(`/api/locales/${locale}/number-formats.json`).then((r) =>
                  r.json()
                ),
                fetch(`/api/locales/${locale}/currency.json`).then((r) =>
                  r.json()
                ),
              ]);

            set((draft) => {
              draft.localeData.set(locale, {
                dateFormats,
                numberFormats,
                currencyData,
              });
              draft.loadingStates.set(key, false);
            });
          } catch (error) {
            set((draft) => {
              draft.loadingStates.set(key, false);
              draft.errors.set(key, error.message);
            });
          }
        },

        // Add translations manually
        addTranslations: (locale, namespace, translations) => {
          set((draft) => {
            if (!draft.translations.has(locale)) {
              draft.translations.set(locale, new Map());
            }

            const existing =
              draft.translations.get(locale).get(namespace) || {};
            draft.translations.get(locale).set(namespace, {
              ...existing,
              ...translations,
            });

            draft.loadedNamespaces.add(`${locale}:${namespace}`);
          });
        },

        // Translation function
        t: (key, options = {}) => {
          const state = get();
          const {
            namespace = "common",
            values = {},
            count,
            defaultValue,
            locale = state.currentLocale,
          } = options;

          // Get translation from current locale
          let translation = state.translations.get(locale)?.get(namespace)?.[
            key
          ];

          // Fallback to fallback locale
          if (!translation && locale !== state.fallbackLocale) {
            translation = state.translations
              .get(state.fallbackLocale)
              ?.get(namespace)?.[key];
          }

          // Use default value if no translation found
          if (!translation) {
            translation = defaultValue || key;
          }

          // Handle pluralization
          if (typeof count === "number" && typeof translation === "object") {
            const pluralRule = getPluralRule(locale, count);
            translation =
              translation[pluralRule] || translation.other || translation.one;
          }

          // Interpolate values
          if (
            typeof translation === "string" &&
            Object.keys(values).length > 0
          ) {
            translation = interpolateString(
              translation,
              values,
              state.interpolationOptions
            );
          }

          return translation;
        },

        // Format date according to locale
        formatDate: (date, options = {}) => {
          const state = get();
          const locale = options.locale || state.currentLocale;
          const localeData = state.localeData.get(locale);

          try {
            const formatOptions = {
              ...localeData?.dateFormats?.default,
              ...options,
            };

            return new Intl.DateTimeFormat(locale, formatOptions).format(
              new Date(date)
            );
          } catch {
            return new Date(date).toLocaleDateString(locale);
          }
        },

        // Format number according to locale
        formatNumber: (number, options = {}) => {
          const state = get();
          const locale = options.locale || state.currentLocale;
          const localeData = state.localeData.get(locale);

          try {
            const formatOptions = {
              ...localeData?.numberFormats?.default,
              ...options,
            };

            return new Intl.NumberFormat(locale, formatOptions).format(number);
          } catch {
            return number.toLocaleString(locale);
          }
        },

        // Format currency according to locale
        formatCurrency: (amount, currency, options = {}) => {
          const state = get();
          const locale = options.locale || state.currentLocale;
          const localeData = state.localeData.get(locale);

          try {
            const formatOptions = {
              style: "currency",
              currency,
              ...localeData?.currencyData?.formats?.[currency],
              ...options,
            };

            return new Intl.NumberFormat(locale, formatOptions).format(amount);
          } catch {
            return `${currency} ${amount}`;
          }
        },

        // Get relative time formatting
        formatRelativeTime: (value, unit, options = {}) => {
          const state = get();
          const locale = options.locale || state.currentLocale;

          try {
            return new Intl.RelativeTimeFormat(locale, options).format(
              value,
              unit
            );
          } catch {
            return `${value} ${unit}${Math.abs(value) !== 1 ? "s" : ""} ago`;
          }
        },

        // Clear translations
        clearTranslations: (locale, namespace) => {
          set((draft) => {
            if (namespace) {
              draft.translations.get(locale)?.delete(namespace);
              draft.loadedNamespaces.delete(`${locale}:${namespace}`);
            } else {
              draft.translations.delete(locale);
              // Remove all namespaces for this locale
              draft.loadedNamespaces.forEach((ns) => {
                if (ns.startsWith(`${locale}:`)) {
                  draft.loadedNamespaces.delete(ns);
                }
              });
            }
          });
        },

        // Preload translations for multiple locales
        preloadTranslations: async (locales, namespaces = ["common"]) => {
          const promises = [];

          for (const locale of locales) {
            for (const namespace of namespaces) {
              promises.push(get().loadTranslations(locale, namespace));
            }
          }

          await Promise.allSettled(promises);
        },

        // Get loading state
        isLoading: (locale, namespace) => {
          const state = get();
          const key = namespace ? `${locale}:${namespace}` : `locale:${locale}`;
          return state.loadingStates.get(key) || false;
        },

        // Get error state
        getError: (locale, namespace) => {
          const state = get();
          const key = namespace ? `${locale}:${namespace}` : `locale:${locale}`;
          return state.errors.get(key);
        },
      }))
    ),
    {
      name: "i18n-store",
      partialize: (state) => ({
        currentLocale: state.currentLocale,
        direction: state.direction,
        // Don't persist translations and loading states
      }),
    }
  )
);

// React hooks for Zustand
const useTranslation = (namespace = "common") => {
  const store = useI18nStore();
  const currentLocale = store.currentLocale;
  const isLoading = store.isLoading(currentLocale, namespace);

  // Auto-load translations
  useEffect(() => {
    const key = `${currentLocale}:${namespace}`;
    if (!store.loadedNamespaces.has(key) && !isLoading) {
      store.loadTranslations(currentLocale, namespace);
    }
  }, [currentLocale, namespace, store, isLoading]);

  return {
    t: (key, options) => store.t(key, { ...options, namespace }),
    locale: currentLocale,
    isLoading,
  };
};

const useLocale = () => {
  const store = useI18nStore();

  return {
    locale: store.currentLocale,
    direction: store.direction,
    supportedLocales: store.supportedLocales,
    changeLocale: store.setLocale,
    formatDate: store.formatDate,
    formatNumber: store.formatNumber,
    formatCurrency: store.formatCurrency,
    formatRelativeTime: store.formatRelativeTime,
  };
};

// Language detector utility
const detectLanguage = () => {
  // Check URL parameter
  const urlParams = new URLSearchParams(window.location.search);
  const urlLang = urlParams.get("lang");
  if (urlLang) return urlLang;

  // Check localStorage
  const storedLang = localStorage.getItem("preferred-language");
  if (storedLang) return storedLang;

  // Check browser language
  const browserLang = navigator.language || navigator.languages[0];
  return browserLang;
};

// Initialize i18n
const initializeI18n = async () => {
  const detectedLanguage = detectLanguage();
  const store = useI18nStore.getState();

  // Set detected language if supported
  const supportedLanguage = store.supportedLocales.find((locale) =>
    locale.startsWith(detectedLanguage.split("-")[0])
  );

  if (supportedLanguage) {
    store.setLocale(supportedLanguage);
  }

  // Preload common translations
  await store.preloadTranslations(
    [store.currentLocale],
    ["common", "navigation"]
  );
};

export { useI18nStore, useTranslation, useLocale, initializeI18n };
```

**Advanced i18n Patterns:**

```javascript
// Lazy loading translation component
const LazyTranslation = ({ namespace, children }) => {
  const { t, isLoading } = useTranslation(namespace);

  if (isLoading) {
    return <div className="translation-loading">Loading translations...</div>;
  }

  return children({ t });
};

// Translation provider with context
const TranslationContext = createContext();

const TranslationProvider = ({ children, defaultNamespace = "common" }) => {
  const { t, locale, isLoading } = useTranslation(defaultNamespace);
  const { formatDate, formatNumber, formatCurrency } = useLocale();

  const contextValue = {
    t,
    locale,
    isLoading,
    formatDate,
    formatNumber,
    formatCurrency,
    // Enhanced translation function with automatic namespace detection
    translate: (key, options = {}) => {
      // Auto-detect namespace from key (e.g., 'navigation.home' -> namespace: 'navigation')
      if (key.includes(".") && !options.namespace) {
        const [detectedNamespace, ...keyParts] = key.split(".");
        return t(keyParts.join("."), {
          ...options,
          namespace: detectedNamespace,
        });
      }
      return t(key, options);
    },
  };

  return (
    <TranslationContext.Provider value={contextValue}>
      {children}
    </TranslationContext.Provider>
  );
};

// Higher-order component for translations
const withTranslation = (namespace) => (Component) => {
  return function TranslatedComponent(props) {
    const { t, locale, isLoading } = useTranslation(namespace);

    return (
      <Component
        {...props}
        t={t}
        locale={locale}
        isTranslationLoading={isLoading}
      />
    );
  };
};

// Translation component with interpolation
const Trans = ({ i18nKey, values = {}, components = {}, namespace }) => {
  const { t } = useTranslation(namespace);
  const translation = t(i18nKey, { values });

  // Handle component interpolation (e.g., "Click <link>here</link>")
  if (Object.keys(components).length > 0) {
    return (
      <span
        dangerouslySetInnerHTML={{
          __html: interpolateComponents(translation, components),
        }}
      />
    );
  }

  return <span>{translation}</span>;
};

// Utility for component interpolation
const interpolateComponents = (text, components) => {
  return text.replace(/<(\w+)>(.*?)<\/\1>/g, (match, tag, content) => {
    const Component = components[tag];
    if (Component) {
      return ReactDOMServer.renderToString(
        React.createElement(Component, {}, content)
      );
    }
    return match;
  });
};

// Locale switcher component
const LocaleSwitcher = ({ className }) => {
  const { locale, supportedLocales, changeLocale } = useLocale();
  const { t } = useTranslation("common");

  return (
    <select
      className={className}
      value={locale}
      onChange={(e) => changeLocale(e.target.value)}
      aria-label={t("language.select")}
    >
      {supportedLocales.map((loc) => (
        <option key={loc} value={loc}>
          {t(`language.${loc}`, { defaultValue: loc })}
        </option>
      ))}
    </select>
  );
};

// RTL support component
const RTLProvider = ({ children }) => {
  const { direction } = useLocale();

  useEffect(() => {
    document.documentElement.dir = direction;
    document.body.className = direction === "rtl" ? "rtl" : "ltr";
  }, [direction]);

  return <div className={`app-container ${direction}`}>{children}</div>;
};

// Usage examples
const App = () => {
  useEffect(() => {
    initializeI18n();
  }, []);

  return (
    <TranslationProvider>
      <RTLProvider>
        <Header />
        <Main />
        <Footer />
      </RTLProvider>
    </TranslationProvider>
  );
};

const Header = withTranslation("navigation")(({ t }) => (
  <header>
    <nav>
      <a href="/">{t("home")}</a>
      <a href="/about">{t("about")}</a>
      <a href="/contact">{t("contact")}</a>
    </nav>
    <LocaleSwitcher className="locale-switcher" />
  </header>
));

const WelcomeMessage = () => {
  const { t, formatDate } = useLocale();
  const currentDate = new Date();

  return (
    <div>
      <Trans
        i18nKey="welcome.message"
        values={{
          name: "John",
          date: formatDate(currentDate, { dateStyle: "long" }),
        }}
        components={{
          strong: <strong />,
          link: <a href="/profile" />,
        }}
      />
    </div>
  );
};
```

**Comparison Summary:**

| Feature                | Redux                                  | Zustand                             |
| ---------------------- | -------------------------------------- | ----------------------------------- |
| **Setup Complexity**   | More complex (slice, selectors, hooks) | Simpler (single store)              |
| **Type Safety**        | Excellent with TypeScript              | Good with TypeScript                |
| **Performance**        | Good (with proper selectors)           | Excellent (fine-grained reactivity) |
| **DevTools**           | Excellent debugging                    | Basic debugging                     |
| **Persistence**        | Requires additional setup              | Built-in persist middleware         |
| **Bundle Size**        | Larger (RTK + dependencies)            | Smaller footprint                   |
| **Learning Curve**     | Steeper                                | Gentler                             |
| **Async Loading**      | Built-in with RTK Query                | Custom implementation               |
| **Middleware Support** | Extensive ecosystem                    | Limited but sufficient              |
| **SSR Support**        | Good with proper setup                 | Good with hydration                 |

**Best Practices:**

1. **Lazy load translations** to reduce initial bundle size
2. **Use namespaces** to organize translations logically
3. **Implement fallback mechanisms** for missing translations
4. **Cache translations** to avoid repeated network requests
5. **Support pluralization** for languages with complex plural rules
6. **Handle RTL languages** properly with CSS and layout adjustments
7. **Use interpolation** for dynamic content in translations
8. **Implement proper error handling** for failed translation loads
9. **Test with different locales** to ensure proper functionality
10. **Consider SEO implications** for multi-language content

Both Redux and Zustand can effectively handle internationalization, with Redux providing more structure and tooling, while Zustand offers simplicity and flexibility for custom i18n implementations.

### Q56: How do you implement advanced caching and memoization strategies in Redux vs Zustand?

**Answer:**

Both Redux and Zustand can implement sophisticated caching and memoization strategies to optimize performance and reduce unnecessary computations.

#### Redux Implementation:

```javascript
// store/slices/cacheSlice.js
import { createSlice, createAsyncThunk, createSelector } from '@reduxjs/toolkit';
import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

// RTK Query API for advanced caching
export const apiSlice = createApi({
  reducerPath: 'api',
  baseQuery: fetchBaseQuery({
    baseUrl: '/api',
    prepareHeaders: (headers, { getState }) => {
      const token = getState().auth.token;
      if (token) {
        headers.set('authorization', `Bearer ${token}`);
      }
      return headers;
    },
  }),
  tagTypes: ['User', 'Post', 'Comment'],
  endpoints: (builder) => ({
    getUsers: builder.query({
      query: (params) => ({
        url: '/users',
        params,
      }),
      providesTags: ['User'],
      // Advanced caching configuration
      keepUnusedDataFor: 60, // seconds
      transformResponse: (response) => {
        // Transform and normalize data
        return response.data.map(user => ({
          ...user,
          fullName: `${user.firstName} ${user.lastName}`,
        }));
      },
    }),
    getUserById: builder.query({
      query: (id) => `/users/${id}`,
      providesTags: (result, error, id) => [{ type: 'User', id }],
    }),
    updateUser: builder.mutation({
      query: ({ id, ...patch }) => ({
        url: `/users/${id}`,
        method: 'PATCH',
        body: patch,
      }),
      invalidatesTags: (result, error, { id }) => [{ type: 'User', id }],
      // Optimistic updates
      onQueryStarted: async ({ id, ...patch }, { dispatch, queryFulfilled }) => {
        const patchResult = dispatch(
          apiSlice.util.updateQueryData('getUserById', id, (draft) => {
            Object.assign(draft, patch);
          })
        );
        try {
          await queryFulfilled;
        } catch {
          patchResult.undo();
        }
      },
    }),
  }),
});

// Manual cache slice for custom caching logic
const cacheSlice = createSlice({
  name: 'cache',
  initialState: {
    computedValues: {},
    timestamps: {},
    dependencies: {},
    ttl: 300000, // 5 minutes
  },
  reducers: {
    setCachedValue: (state, action) => {
      const { key, value, dependencies = [] } = action.payload;
      state.computedValues[key] = value;
      state.timestamps[key] = Date.now();
      state.dependencies[key] = dependencies;
    },
    invalidateCache: (state, action) => {
      const { keys } = action.payload;
      keys.forEach(key => {
        delete state.computedValues[key];
        delete state.timestamps[key];
        delete state.dependencies[key];
      });
    },
    invalidateDependentCache: (state, action) => {
      const { dependency } = action.payload;
      Object.entries(state.dependencies).forEach(([key, deps]) => {
        if (deps.includes(dependency)) {
          delete state.computedValues[key];
          delete state.timestamps[key];
          delete state.dependencies[key];
        }
      });
    },
    clearExpiredCache: (state) => {
      const now = Date.now();
      Object.entries(state.timestamps).forEach(([key, timestamp]) => {
        if (now - timestamp > state.ttl) {
          delete state.computedValues[key];
          delete state.timestamps[key];
          delete state.dependencies[key];
        }
      });
    },
  },
});

// Memoized selectors
export const selectUserById = createSelector(
  [(state) => state.users.entities, (state, userId) => userId],
  (entities, userId) => entities[userId]
);

export const selectUsersByRole = createSelector(
  [(state) => state.users.entities, (state, role) => role],
  (entities, role) => {
    return Object.values(entities).filter(user => user.role === role);
  }
);

// Complex memoized selector with multiple dependencies
export const selectUserStatistics = createSelector(
  [
    (state) => state.users.entities,
    (state) => state.posts.entities,
    (state) => state.comments.entities,
  ],
  (users, posts, comments) => {
    // Expensive computation
    return Object.values(users).map(user => {
      const userPosts = Object.values(posts).filter(post => post.authorId === user.id);
      const userComments = Object.values(comments).filter(comment => comment.authorId === user.id);
      
      return {
        ...user,
        postsCount: userPosts.length,
        commentsCount: userComments.length,
        avgPostLength: userPosts.reduce((sum, post) => sum + post.content.length, 0) / userPosts.length || 0,
        lastActivity: Math.max(
          ...userPosts.map(p => new Date(p.createdAt).getTime()),
          ...userComments.map(c => new Date(c.createdAt).getTime())
        ),
      };
    });
  }
);

export const { setCachedValue, invalidateCache, invalidateDependentCache, clearExpiredCache } = cacheSlice.actions;
export default cacheSlice.reducer;
```

```javascript
// hooks/useReduxCache.js
import { useSelector, useDispatch } from 'react-redux';
import { useCallback, useEffect, useMemo } from 'react';
import { setCachedValue, invalidateCache, clearExpiredCache } from '../store/slices/cacheSlice';

export const useReduxCache = () => {
  const dispatch = useDispatch();
  const cache = useSelector(state => state.cache);

  // Memoized cache operations
  const getCachedValue = useCallback((key) => {
    const value = cache.computedValues[key];
    const timestamp = cache.timestamps[key];
    
    if (!value || !timestamp) return null;
    
    // Check if cache is expired
    if (Date.now() - timestamp > cache.ttl) {
      dispatch(invalidateCache({ keys: [key] }));
      return null;
    }
    
    return value;
  }, [cache, dispatch]);

  const setCachedValue = useCallback((key, value, dependencies = []) => {
    dispatch(setCachedValue({ key, value, dependencies }));
  }, [dispatch]);

  const invalidateByDependency = useCallback((dependency) => {
    dispatch(invalidateDependentCache({ dependency }));
  }, [dispatch]);

  // Auto cleanup expired cache
  useEffect(() => {
    const interval = setInterval(() => {
      dispatch(clearExpiredCache());
    }, 60000); // Check every minute

    return () => clearInterval(interval);
  }, [dispatch]);

  return {
    getCachedValue,
    setCachedValue,
    invalidateByDependency,
  };
};

// Hook for memoized computations
export const useMemoizedComputation = (computeFn, dependencies, cacheKey) => {
  const { getCachedValue, setCachedValue } = useReduxCache();
  
  return useMemo(() => {
    // Try to get from cache first
    const cached = getCachedValue(cacheKey);
    if (cached !== null) {
      return cached;
    }
    
    // Compute and cache the result
    const result = computeFn();
    setCachedValue(cacheKey, result, dependencies);
    return result;
  }, [computeFn, dependencies, cacheKey, getCachedValue, setCachedValue]);
};
```

#### Zustand Implementation:

```javascript
// stores/cacheStore.js
import { create } from 'zustand';
import { subscribeWithSelector } from 'zustand/middleware';
import { immer } from 'zustand/middleware/immer';
import { persist } from 'zustand/middleware';

// Cache store with advanced memoization
export const useCacheStore = create(
  subscribeWithSelector(
    immer(
      persist(
        (set, get) => ({
          // Cache state
          computedValues: new Map(),
          timestamps: new Map(),
          dependencies: new Map(),
          memoizedSelectors: new Map(),
          ttl: 300000, // 5 minutes
          
          // Cache actions
          setCachedValue: (key, value, dependencies = []) => {
            set((state) => {
              state.computedValues.set(key, value);
              state.timestamps.set(key, Date.now());
              state.dependencies.set(key, dependencies);
            });
          },
          
          getCachedValue: (key) => {
            const state = get();
            const value = state.computedValues.get(key);
            const timestamp = state.timestamps.get(key);
            
            if (!value || !timestamp) return null;
            
            // Check if cache is expired
            if (Date.now() - timestamp > state.ttl) {
              get().invalidateCache([key]);
              return null;
            }
            
            return value;
          },
          
          invalidateCache: (keys) => {
            set((state) => {
              keys.forEach(key => {
                state.computedValues.delete(key);
                state.timestamps.delete(key);
                state.dependencies.delete(key);
              });
            });
          },
          
          invalidateDependentCache: (dependency) => {
            set((state) => {
              const keysToInvalidate = [];
              state.dependencies.forEach((deps, key) => {
                if (deps.includes(dependency)) {
                  keysToInvalidate.push(key);
                }
              });
              
              keysToInvalidate.forEach(key => {
                state.computedValues.delete(key);
                state.timestamps.delete(key);
                state.dependencies.delete(key);
              });
            });
          },
          
          clearExpiredCache: () => {
            set((state) => {
              const now = Date.now();
              const keysToDelete = [];
              
              state.timestamps.forEach((timestamp, key) => {
                if (now - timestamp > state.ttl) {
                  keysToDelete.push(key);
                }
              });
              
              keysToDelete.forEach(key => {
                state.computedValues.delete(key);
                state.timestamps.delete(key);
                state.dependencies.delete(key);
              });
            });
          },
          
          // Memoized selector factory
          createMemoizedSelector: (selectorFn, dependencies = []) => {
            const selectorKey = JSON.stringify({ fn: selectorFn.toString(), deps: dependencies });
            
            return (state) => {
              const cached = get().getCachedValue(selectorKey);
              if (cached !== null) {
                return cached;
              }
              
              const result = selectorFn(state);
              get().setCachedValue(selectorKey, result, dependencies);
              return result;
            };
          },
          
          // Advanced memoization with weak references
          memoize: (fn, keyFn = (...args) => JSON.stringify(args)) => {
            const cache = new Map();
            const weakCache = new WeakMap();
            
            return (...args) => {
              const key = keyFn(...args);
              
              // Try weak cache first for object references
              if (args.length === 1 && typeof args[0] === 'object' && args[0] !== null) {
                if (weakCache.has(args[0])) {
                  return weakCache.get(args[0]);
                }
              }
              
              // Try regular cache
              if (cache.has(key)) {
                const { value, timestamp } = cache.get(key);
                if (Date.now() - timestamp < get().ttl) {
                  return value;
                }
                cache.delete(key);
              }
              
              // Compute new value
              const result = fn(...args);
              const cacheEntry = { value: result, timestamp: Date.now() };
              
              cache.set(key, cacheEntry);
              
              // Store in weak cache if applicable
              if (args.length === 1 && typeof args[0] === 'object' && args[0] !== null) {
                weakCache.set(args[0], result);
              }
              
              return result;
            };
          },
        }),
        {
          name: 'cache-store',
          partialize: (state) => ({
            // Only persist non-function values
            computedValues: Array.from(state.computedValues.entries()),
            timestamps: Array.from(state.timestamps.entries()),
            dependencies: Array.from(state.dependencies.entries()),
            ttl: state.ttl,
          }),
          onRehydrateStorage: () => (state) => {
            if (state) {
              // Restore Maps from arrays
              state.computedValues = new Map(state.computedValues || []);
              state.timestamps = new Map(state.timestamps || []);
              state.dependencies = new Map(state.dependencies || []);
              state.memoizedSelectors = new Map();
            }
          },
        }
      )
    )
  )
);

// Data store with caching integration
export const useDataStore = create(
  subscribeWithSelector(
    immer((set, get) => ({
      users: new Map(),
      posts: new Map(),
      comments: new Map(),
      loading: false,
      error: null,
      
      // Memoized selectors
      getUserById: useCacheStore.getState().memoize(
        (id) => get().users.get(id),
        (id) => `user-${id}`
      ),
      
      getUsersByRole: useCacheStore.getState().memoize(
        (role) => {
          return Array.from(get().users.values()).filter(user => user.role === role);
        },
        (role) => `users-by-role-${role}`
      ),
      
      getUserStatistics: useCacheStore.getState().memoize(
        () => {
          const { users, posts, comments } = get();
          
          return Array.from(users.values()).map(user => {
            const userPosts = Array.from(posts.values()).filter(post => post.authorId === user.id);
            const userComments = Array.from(comments.values()).filter(comment => comment.authorId === user.id);
            
            return {
              ...user,
              postsCount: userPosts.length,
              commentsCount: userComments.length,
              avgPostLength: userPosts.reduce((sum, post) => sum + post.content.length, 0) / userPosts.length || 0,
              lastActivity: Math.max(
                ...userPosts.map(p => new Date(p.createdAt).getTime()),
                ...userComments.map(c => new Date(c.createdAt).getTime())
              ),
            };
          });
        },
        () => 'user-statistics'
      ),
      
      // Actions that invalidate cache
      addUser: (user) => {
        set((state) => {
          state.users.set(user.id, user);
        });
        useCacheStore.getState().invalidateDependentCache('users');
      },
      
      updateUser: (id, updates) => {
        set((state) => {
          const user = state.users.get(id);
          if (user) {
            state.users.set(id, { ...user, ...updates });
          }
        });
        useCacheStore.getState().invalidateDependentCache('users');
        useCacheStore.getState().invalidateCache([`user-${id}`]);
      },
      
      deleteUser: (id) => {
        set((state) => {
          state.users.delete(id);
        });
        useCacheStore.getState().invalidateDependentCache('users');
        useCacheStore.getState().invalidateCache([`user-${id}`]);
      },
    }))
  )
);
```

```javascript
// hooks/useZustandCache.js
import { useCallback, useEffect, useMemo } from 'react';
import { useCacheStore } from '../stores/cacheStore';

export const useZustandCache = () => {
  const {
    getCachedValue,
    setCachedValue,
    invalidateCache,
    invalidateDependentCache,
    clearExpiredCache,
    memoize,
  } = useCacheStore();

  // Auto cleanup expired cache
  useEffect(() => {
    const interval = setInterval(() => {
      clearExpiredCache();
    }, 60000); // Check every minute

    return () => clearInterval(interval);
  }, [clearExpiredCache]);

  return {
    getCachedValue,
    setCachedValue,
    invalidateCache,
    invalidateDependentCache,
    memoize,
  };
};

// Hook for memoized computations
export const useMemoizedComputation = (computeFn, dependencies, cacheKey) => {
  const { getCachedValue, setCachedValue } = useZustandCache();
  
  return useMemo(() => {
    // Try to get from cache first
    const cached = getCachedValue(cacheKey);
    if (cached !== null) {
      return cached;
    }
    
    // Compute and cache the result
    const result = computeFn();
    setCachedValue(cacheKey, result, dependencies);
    return result;
  }, [computeFn, dependencies, cacheKey, getCachedValue, setCachedValue]);
};

// Hook for creating memoized selectors
export const useMemoizedSelector = (selector, dependencies = []) => {
  const { memoize } = useZustandCache();
  
  return useMemo(() => {
    return memoize(selector, (...args) => {
      return JSON.stringify({ args, deps: dependencies });
    });
  }, [selector, dependencies, memoize]);
};
```

#### React Components:

```jsx
// components/UserList.jsx
import React, { useMemo } from 'react';
import { useSelector } from 'react-redux';
import { selectUsersByRole, selectUserStatistics } from '../store/slices/cacheSlice';
import { useDataStore } from '../stores/cacheStore';
import { useMemoizedComputation } from '../hooks/useZustandCache';

// Redux version
const ReduxUserList = ({ role, showStatistics }) => {
  // Memoized selectors automatically cache results
  const usersByRole = useSelector(state => selectUsersByRole(state, role));
  const userStatistics = useSelector(selectUserStatistics);
  
  // Additional memoized computation
  const processedUsers = useMemoizedComputation(
    () => {
      return usersByRole.map(user => ({
        ...user,
        displayName: `${user.firstName} ${user.lastName} (${user.role})`,
        isActive: user.lastLogin && new Date(user.lastLogin) > new Date(Date.now() - 30 * 24 * 60 * 60 * 1000),
      }));
    },
    [role],
    `processed-users-${role}`
  );
  
  return (
    <div className="user-list">
      <h2>Users - {role}</h2>
      {processedUsers.map(user => (
        <div key={user.id} className="user-item">
          <h3>{user.displayName}</h3>
          <span className={`status ${user.isActive ? 'active' : 'inactive'}`}>
            {user.isActive ? 'Active' : 'Inactive'}
          </span>
          {showStatistics && (
            <div className="user-stats">
              <span>Posts: {userStatistics.find(s => s.id === user.id)?.postsCount || 0}</span>
              <span>Comments: {userStatistics.find(s => s.id === user.id)?.commentsCount || 0}</span>
            </div>
          )}
        </div>
      ))}
    </div>
  );
};

// Zustand version
const ZustandUserList = ({ role, showStatistics }) => {
  const getUsersByRole = useDataStore(state => state.getUsersByRole);
  const getUserStatistics = useDataStore(state => state.getUserStatistics);
  
  // Memoized data fetching
  const usersByRole = useMemo(() => getUsersByRole(role), [getUsersByRole, role]);
  const userStatistics = useMemo(() => getUserStatistics(), [getUserStatistics]);
  
  // Additional memoized computation
  const processedUsers = useMemoizedComputation(
    () => {
      return usersByRole.map(user => ({
        ...user,
        displayName: `${user.firstName} ${user.lastName} (${user.role})`,
        isActive: user.lastLogin && new Date(user.lastLogin) > new Date(Date.now() - 30 * 24 * 60 * 60 * 1000),
      }));
    },
    [role],
    `processed-users-${role}`
  );
  
  return (
    <div className="user-list">
      <h2>Users - {role}</h2>
      {processedUsers.map(user => (
        <div key={user.id} className="user-item">
          <h3>{user.displayName}</h3>
          <span className={`status ${user.isActive ? 'active' : 'inactive'}`}>
            {user.isActive ? 'Active' : 'Inactive'}
          </span>
          {showStatistics && (
            <div className="user-stats">
              <span>Posts: {userStatistics.find(s => s.id === user.id)?.postsCount || 0}</span>
              <span>Comments: {userStatistics.find(s => s.id === user.id)?.commentsCount || 0}</span>
            </div>
          )}
        </div>
      ))}
    </div>
  );
};
```

#### Best Practices:

**Performance Optimization:**
- Use RTK Query for API caching in Redux
- Implement proper cache invalidation strategies
- Use weak references for object-based caching
- Implement cache size limits and LRU eviction

**Memory Management:**
- Clear expired cache entries regularly
- Use weak maps for temporary object references
- Implement cache size monitoring
- Avoid memory leaks in long-running applications

**Cache Strategy:**
- Choose appropriate TTL values
- Implement dependency-based invalidation
- Use optimistic updates for better UX
- Consider cache warming for critical data

**Development Experience:**
- Provide cache debugging tools
- Implement cache hit/miss metrics
- Use proper TypeScript types for cache keys
- Document cache dependencies clearly

#### Comparison Summary:

| Feature | Redux | Zustand |
|---------|-------|----------|
| **Built-in Caching** | RTK Query | Custom implementation |
| **Memoized Selectors** | createSelector | Custom memoization |
| **Cache Invalidation** | Tag-based system | Dependency tracking |
| **Persistence** | Additional middleware | Built-in persist |
| **Memory Management** | Manual cleanup | WeakMap support |
| **Performance** | Excellent with RTK Query | Good with custom logic |
| **Complexity** | Medium (RTK Query) | High (custom) |
| **Flexibility** | Structured approach | Highly customizable |

Both approaches provide powerful caching and memoization capabilities, with Redux offering more built-in solutions through RTK Query, while Zustand provides maximum flexibility for custom implementations.

---

### Redux Implementation

**Error Slice with RTK:**
```javascript
// store/errorSlice.js
import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';

const errorSlice = createSlice({
  name: 'error',
  initialState: {
    errors: {},
    globalError: null,
    retryAttempts: {},
    errorHistory: [],
    isRecovering: false
  },
  reducers: {
    addError: (state, action) => {
      const { id, error, context } = action.payload;
      state.errors[id] = {
        ...error,
        context,
        timestamp: Date.now(),
        id
      };
      state.errorHistory.push({
        id,
        error,
        context,
        timestamp: Date.now()
      });
    },
    removeError: (state, action) => {
      delete state.errors[action.payload];
    },
    setGlobalError: (state, action) => {
      state.globalError = action.payload;
    },
    clearGlobalError: (state) => {
      state.globalError = null;
    },
    incrementRetry: (state, action) => {
      const { id } = action.payload;
      state.retryAttempts[id] = (state.retryAttempts[id] || 0) + 1;
    },
    resetRetry: (state, action) => {
      delete state.retryAttempts[action.payload];
    },
    setRecovering: (state, action) => {
      state.isRecovering = action.payload;
    },
    clearErrorHistory: (state) => {
      state.errorHistory = [];
    }
  }
});

export const {
  addError,
  removeError,
  setGlobalError,
  clearGlobalError,
  incrementRetry,
  resetRetry,
  setRecovering,
  clearErrorHistory
} = errorSlice.actions;

export default errorSlice.reducer;
```

**Error Recovery Thunks:**
```javascript
// store/errorThunks.js
import { createAsyncThunk } from '@reduxjs/toolkit';
import { addError, incrementRetry, resetRetry, setRecovering } from './errorSlice';

export const retryOperation = createAsyncThunk(
  'error/retryOperation',
  async ({ operation, maxRetries = 3, delay = 1000 }, { dispatch, getState }) => {
    const { error } = getState();
    const operationId = operation.id;
    const currentRetries = error.retryAttempts[operationId] || 0;

    if (currentRetries >= maxRetries) {
      throw new Error(`Max retries (${maxRetries}) exceeded for operation ${operationId}`);
    }

    dispatch(incrementRetry({ id: operationId }));
    dispatch(setRecovering(true));

    try {
      // Exponential backoff
      const backoffDelay = delay * Math.pow(2, currentRetries);
      await new Promise(resolve => setTimeout(resolve, backoffDelay));

      const result = await operation.execute();
      dispatch(resetRetry(operationId));
      dispatch(setRecovering(false));
      return result;
    } catch (error) {
      dispatch(addError({
        id: operationId,
        error: {
          message: error.message,
          code: error.code,
          type: 'RETRY_FAILED',
          retryCount: currentRetries + 1
        },
        context: operation.context
      }));
      dispatch(setRecovering(false));
      throw error;
    }
  }
);

export const recoverFromError = createAsyncThunk(
  'error/recoverFromError',
  async ({ errorId, recoveryStrategy }, { dispatch, getState }) => {
    const { error } = getState();
    const errorInfo = error.errors[errorId];

    if (!errorInfo) {
      throw new Error(`Error ${errorId} not found`);
    }

    dispatch(setRecovering(true));

    try {
      switch (recoveryStrategy.type) {
        case 'RETRY':
          await dispatch(retryOperation({
            operation: recoveryStrategy.operation,
            maxRetries: recoveryStrategy.maxRetries
          })).unwrap();
          break;

        case 'FALLBACK':
          await recoveryStrategy.fallbackAction();
          break;

        case 'RESET_STATE':
          await recoveryStrategy.resetAction();
          break;

        case 'REDIRECT':
          window.location.href = recoveryStrategy.redirectUrl;
          break;

        default:
          throw new Error(`Unknown recovery strategy: ${recoveryStrategy.type}`);
      }

      dispatch(removeError(errorId));
      dispatch(setRecovering(false));
    } catch (recoveryError) {
      dispatch(addError({
        id: `recovery_${errorId}`,
        error: {
          message: recoveryError.message,
          type: 'RECOVERY_FAILED',
          originalError: errorInfo
        },
        context: { recoveryStrategy }
      }));
      dispatch(setRecovering(false));
      throw recoveryError;
    }
  }
);
```

**Redux Error Hook:**
```javascript
// hooks/useReduxError.js
import { useSelector, useDispatch } from 'react-redux';
import { useCallback, useEffect } from 'react';
import { removeError, recoverFromError } from '../store/errorThunks';

export const useReduxError = () => {
  const dispatch = useDispatch();
  const {
    errors,
    globalError,
    retryAttempts,
    errorHistory,
    isRecovering
  } = useSelector(state => state.error);

  const handleError = useCallback((error, context = {}) => {
    const errorId = `error_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
    
    dispatch(addError({
      id: errorId,
      error: {
        message: error.message,
        code: error.code,
        type: error.type || 'UNKNOWN'
      },
      context
    }));

    return errorId;
  }, [dispatch]);

  const dismissError = useCallback((errorId) => {
    dispatch(removeError(errorId));
  }, [dispatch]);

  const recoverError = useCallback((errorId, recoveryStrategy) => {
    return dispatch(recoverFromError({ errorId, recoveryStrategy }));
  }, [dispatch]);

  const getErrorsByType = useCallback((type) => {
    return Object.values(errors).filter(error => error.type === type);
  }, [errors]);

  const hasErrors = Object.keys(errors).length > 0;
  const criticalErrors = getErrorsByType('CRITICAL');
  const hasCriticalErrors = criticalErrors.length > 0;

  return {
    errors,
    globalError,
    retryAttempts,
    errorHistory,
    isRecovering,
    hasErrors,
    hasCriticalErrors,
    criticalErrors,
    handleError,
    dismissError,
    recoverError,
    getErrorsByType
  };
};
```

### Zustand Implementation

**Error Store with Advanced Recovery:**
```javascript
// stores/errorStore.js
import { create } from 'zustand';
import { subscribeWithSelector } from 'zustand/middleware';
import { immer } from 'zustand/middleware/immer';
import { persist } from 'zustand/middleware/persist';

const useErrorStore = create(
  subscribeWithSelector(
    immer(
      persist(
        (set, get) => ({
          errors: {},
          globalError: null,
          retryAttempts: {},
          errorHistory: [],
          isRecovering: false,
          recoveryStrategies: {},
          errorListeners: new Map(),

          // Actions
          addError: (id, error, context = {}) => {
            set((state) => {
              state.errors[id] = {
                ...error,
                context,
                timestamp: Date.now(),
                id
              };
              state.errorHistory.push({
                id,
                error,
                context,
                timestamp: Date.now()
              });
            });

            // Trigger error listeners
            const listeners = get().errorListeners.get(error.type) || [];
            listeners.forEach(listener => listener(id, error, context));
          },

          removeError: (id) => {
            set((state) => {
              delete state.errors[id];
            });
          },

          setGlobalError: (error) => {
            set((state) => {
              state.globalError = error;
            });
          },

          clearGlobalError: () => {
            set((state) => {
              state.globalError = null;
            });
          },

          incrementRetry: (id) => {
            set((state) => {
              state.retryAttempts[id] = (state.retryAttempts[id] || 0) + 1;
            });
          },

          resetRetry: (id) => {
            set((state) => {
              delete state.retryAttempts[id];
            });
          },

          setRecovering: (isRecovering) => {
            set((state) => {
              state.isRecovering = isRecovering;
            });
          },

          clearErrorHistory: () => {
            set((state) => {
              state.errorHistory = [];
            });
          },

          // Advanced recovery methods
          retryOperation: async (operation, maxRetries = 3, delay = 1000) => {
            const { retryAttempts, incrementRetry, resetRetry, setRecovering, addError } = get();
            const operationId = operation.id;
            const currentRetries = retryAttempts[operationId] || 0;

            if (currentRetries >= maxRetries) {
              throw new Error(`Max retries (${maxRetries}) exceeded for operation ${operationId}`);
            }

            incrementRetry(operationId);
            setRecovering(true);

            try {
              // Exponential backoff
              const backoffDelay = delay * Math.pow(2, currentRetries);
              await new Promise(resolve => setTimeout(resolve, backoffDelay));

              const result = await operation.execute();
              resetRetry(operationId);
              setRecovering(false);
              return result;
            } catch (error) {
              addError(operationId, {
                message: error.message,
                code: error.code,
                type: 'RETRY_FAILED',
                retryCount: currentRetries + 1
              }, operation.context);
              setRecovering(false);
              throw error;
            }
          },

          recoverFromError: async (errorId, recoveryStrategy) => {
            const { errors, setRecovering, removeError, addError } = get();
            const errorInfo = errors[errorId];

            if (!errorInfo) {
              throw new Error(`Error ${errorId} not found`);
            }

            setRecovering(true);

            try {
              switch (recoveryStrategy.type) {
                case 'RETRY':
                  await get().retryOperation(
                    recoveryStrategy.operation,
                    recoveryStrategy.maxRetries
                  );
                  break;

                case 'FALLBACK':
                  await recoveryStrategy.fallbackAction();
                  break;

                case 'RESET_STATE':
                  await recoveryStrategy.resetAction();
                  break;

                case 'REDIRECT':
                  window.location.href = recoveryStrategy.redirectUrl;
                  break;

                default:
                  throw new Error(`Unknown recovery strategy: ${recoveryStrategy.type}`);
              }

              removeError(errorId);
              setRecovering(false);
            } catch (recoveryError) {
              addError(`recovery_${errorId}`, {
                message: recoveryError.message,
                type: 'RECOVERY_FAILED',
                originalError: errorInfo
              }, { recoveryStrategy });
              setRecovering(false);
              throw recoveryError;
            }
          },

          // Error listener management
          addErrorListener: (errorType, listener) => {
            set((state) => {
              const listeners = state.errorListeners.get(errorType) || [];
              listeners.push(listener);
              state.errorListeners.set(errorType, listeners);
            });
          },

          removeErrorListener: (errorType, listener) => {
            set((state) => {
              const listeners = state.errorListeners.get(errorType) || [];
              const filteredListeners = listeners.filter(l => l !== listener);
              state.errorListeners.set(errorType, filteredListeners);
            });
          },

          // Helper methods
          getErrorsByType: (type) => {
            const { errors } = get();
            return Object.values(errors).filter(error => error.type === type);
          },

          hasErrors: () => {
            const { errors } = get();
            return Object.keys(errors).length > 0;
          },

          hasCriticalErrors: () => {
            return get().getErrorsByType('CRITICAL').length > 0;
          },

          registerRecoveryStrategy: (errorType, strategy) => {
            set((state) => {
              state.recoveryStrategies[errorType] = strategy;
            });
          },

          autoRecover: async (errorId) => {
            const { errors, recoveryStrategies, recoverFromError } = get();
            const error = errors[errorId];
            
            if (!error) return;
            
            const strategy = recoveryStrategies[error.type];
            if (strategy) {
              try {
                await recoverFromError(errorId, strategy);
              } catch (recoveryError) {
                console.error('Auto-recovery failed:', recoveryError);
              }
            }
          }
        }),
        {
          name: 'error-store',
          partialize: (state) => ({
            errorHistory: state.errorHistory.slice(-50), // Keep last 50 errors
            recoveryStrategies: state.recoveryStrategies
          })
        }
      )
    )
  )
);

export default useErrorStore;
```

**Zustand Error Hook:**
```javascript
// hooks/useZustandError.js
import { useCallback, useEffect } from 'react';
import useErrorStore from '../stores/errorStore';

export const useZustandError = () => {
  const {
    errors,
    globalError,
    retryAttempts,
    errorHistory,
    isRecovering,
    addError,
    removeError,
    recoverFromError,
    getErrorsByType,
    hasErrors,
    hasCriticalErrors,
    addErrorListener,
    removeErrorListener,
    autoRecover
  } = useErrorStore();

  const handleError = useCallback((error, context = {}) => {
    const errorId = `error_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
    
    addError(errorId, {
      message: error.message,
      code: error.code,
      type: error.type || 'UNKNOWN'
    }, context);

    // Auto-recover if strategy exists
    setTimeout(() => autoRecover(errorId), 100);

    return errorId;
  }, [addError, autoRecover]);

  const dismissError = useCallback((errorId) => {
    removeError(errorId);
  }, [removeError]);

  const recoverError = useCallback((errorId, recoveryStrategy) => {
    return recoverFromError(errorId, recoveryStrategy);
  }, [recoverFromError]);

  // Auto-dismiss non-critical errors after timeout
  useEffect(() => {
    const nonCriticalErrors = Object.entries(errors).filter(
      ([_, error]) => error.type !== 'CRITICAL'
    );

    nonCriticalErrors.forEach(([errorId, error]) => {
      const age = Date.now() - error.timestamp;
      if (age > 30000) { // 30 seconds
        removeError(errorId);
      }
    });
  }, [errors, removeError]);

  const criticalErrors = getErrorsByType('CRITICAL');

  return {
    errors,
    globalError,
    retryAttempts,
    errorHistory,
    isRecovering,
    hasErrors: hasErrors(),
    hasCriticalErrors: hasCriticalErrors(),
    criticalErrors,
    handleError,
    dismissError,
    recoverError,
    getErrorsByType,
    addErrorListener,
    removeErrorListener
  };
};
```

### Best Practices

**Error Classification:**
```javascript
// utils/errorClassification.js
export const ErrorTypes = {
  NETWORK: 'NETWORK',
  VALIDATION: 'VALIDATION',
  AUTHENTICATION: 'AUTHENTICATION',
  AUTHORIZATION: 'AUTHORIZATION',
  SERVER: 'SERVER',
  CLIENT: 'CLIENT',
  CRITICAL: 'CRITICAL',
  RECOVERABLE: 'RECOVERABLE'
};

export const classifyError = (error) => {
  if (error.code >= 500) return ErrorTypes.SERVER;
  if (error.code === 401) return ErrorTypes.AUTHENTICATION;
  if (error.code === 403) return ErrorTypes.AUTHORIZATION;
  if (error.code >= 400) return ErrorTypes.CLIENT;
  if (error.name === 'NetworkError') return ErrorTypes.NETWORK;
  if (error.name === 'ValidationError') return ErrorTypes.VALIDATION;
  
  return ErrorTypes.CLIENT;
};

export const isCriticalError = (error) => {
  return [
    ErrorTypes.CRITICAL,
    ErrorTypes.AUTHENTICATION,
    ErrorTypes.SERVER
  ].includes(error.type);
};
```

**Recovery Strategies:**
```javascript
// utils/recoveryStrategies.js
export const createRetryStrategy = (operation, maxRetries = 3) => ({
  type: 'RETRY',
  operation,
  maxRetries
});

export const createFallbackStrategy = (fallbackAction) => ({
  type: 'FALLBACK',
  fallbackAction
});

export const createResetStrategy = (resetAction) => ({
  type: 'RESET_STATE',
  resetAction
});

export const createRedirectStrategy = (redirectUrl) => ({
  type: 'REDIRECT',
  redirectUrl
});
```

### Comparison Summary

| Feature | Redux | Zustand |
|---------|-------|----------|
| **Error State Management** | Structured with slices and reducers | Flexible store with immer |
| **Recovery Mechanisms** | Async thunks with middleware | Direct async methods |
| **Error Listeners** | Redux middleware and selectors | Built-in listener system |
| **Persistence** | Requires additional setup | Built-in persist middleware |
| **DevTools** | Excellent debugging support | Basic debugging |
| **Type Safety** | Strong with TypeScript | Good with TypeScript |
| **Bundle Size** | Larger with dependencies | Smaller and lightweight |
| **Learning Curve** | Steeper with concepts | Gentler and intuitive |
| **Error Boundaries** | Requires integration setup | Direct store integration |
| **Auto-Recovery** | Manual implementation | Built-in support |

**Best Practices:**
- **Error Classification**: Categorize errors by type and severity for appropriate handling
- **Recovery Strategies**: Implement multiple recovery patterns (retry, fallback, reset, redirect)
- **User Experience**: Provide clear error messages and recovery options
- **Monitoring**: Track error patterns and recovery success rates
- **Performance**: Avoid memory leaks with proper error cleanup
- **Testing**: Test error scenarios and recovery mechanisms thoroughly
- **Logging**: Implement comprehensive error logging for debugging
- **Graceful Degradation**: Ensure app remains functional during errors

---

### Redux Testing Strategies

#### 1. Redux Toolkit Testing Setup

```javascript
// store/testUtils.js
import { configureStore } from '@reduxjs/toolkit';
import { render } from '@testing-library/react';
import { Provider } from 'react-redux';
import userSlice from './slices/userSlice';
import postsSlice from './slices/postsSlice';
import { api } from './api/apiSlice';

// Test store factory
export const createTestStore = (preloadedState = {}) => {
  return configureStore({
    reducer: {
      user: userSlice,
      posts: postsSlice,
      api: api.reducer,
    },
    preloadedState,
    middleware: (getDefaultMiddleware) =>
      getDefaultMiddleware({
        serializableCheck: false,
        immutableCheck: false,
      }).concat(api.middleware),
  });
};

// Custom render with Redux provider
export const renderWithRedux = (
  ui,
  {
    preloadedState = {},
    store = createTestStore(preloadedState),
    ...renderOptions
  } = {}
) => {
  const Wrapper = ({ children }) => (
    <Provider store={store}>{children}</Provider>
  );
  
  return {
    ...render(ui, { wrapper: Wrapper, ...renderOptions }),
    store,
  };
};

// Mock API responses
export const createMockApiResponse = (data, status = 200) => ({
  data,
  status,
  headers: {},
  config: {},
  statusText: 'OK',
});
```

#### 2. Slice Testing

```javascript
// __tests__/userSlice.test.js
import userSlice, {
  setUser,
  updateProfile,
  fetchUserProfile,
  selectUser,
  selectUserStatus,
} from '../slices/userSlice';
import { createTestStore } from '../testUtils';

describe('userSlice', () => {
  let store;
  
  beforeEach(() => {
    store = createTestStore();
  });
  
  describe('reducers', () => {
    it('should handle setUser', () => {
      const user = { id: 1, name: 'John Doe', email: 'john@example.com' };
      
      store.dispatch(setUser(user));
      
      expect(selectUser(store.getState())).toEqual(user);
      expect(selectUserStatus(store.getState())).toBe('idle');
    });
    
    it('should handle updateProfile', () => {
      const initialUser = { id: 1, name: 'John', email: 'john@example.com' };
      const updates = { name: 'John Doe', bio: 'Software Developer' };
      
      store.dispatch(setUser(initialUser));
      store.dispatch(updateProfile(updates));
      
      const updatedUser = selectUser(store.getState());
      expect(updatedUser).toEqual({ ...initialUser, ...updates });
    });
  });
  
  describe('async thunks', () => {
    it('should handle fetchUserProfile success', async () => {
      const mockUser = { id: 1, name: 'John Doe' };
      
      // Mock the API call
      jest.spyOn(global, 'fetch').mockResolvedValueOnce({
        ok: true,
        json: async () => mockUser,
      });
      
      await store.dispatch(fetchUserProfile(1));
      
      expect(selectUser(store.getState())).toEqual(mockUser);
      expect(selectUserStatus(store.getState())).toBe('succeeded');
    });
    
    it('should handle fetchUserProfile failure', async () => {
      jest.spyOn(global, 'fetch').mockRejectedValueOnce(
        new Error('Network error')
      );
      
      await store.dispatch(fetchUserProfile(1));
      
      expect(selectUserStatus(store.getState())).toBe('failed');
    });
  });
});
```

#### 3. Component Integration Testing

```javascript
// __tests__/UserProfile.test.js
import React from 'react';
import { screen, fireEvent, waitFor } from '@testing-library/react';
import { renderWithRedux } from '../store/testUtils';
import UserProfile from '../components/UserProfile';
import { server } from '../mocks/server';
import { rest } from 'msw';

describe('UserProfile Component', () => {
  it('should display user information', () => {
    const preloadedState = {
      user: {
        data: { id: 1, name: 'John Doe', email: 'john@example.com' },
        status: 'idle',
        error: null,
      },
    };
    
    renderWithRedux(<UserProfile />, { preloadedState });
    
    expect(screen.getByText('John Doe')).toBeInTheDocument();
    expect(screen.getByText('john@example.com')).toBeInTheDocument();
  });
  
  it('should handle profile update', async () => {
    const preloadedState = {
      user: {
        data: { id: 1, name: 'John', email: 'john@example.com' },
        status: 'idle',
        error: null,
      },
    };
    
    const { store } = renderWithRedux(<UserProfile />, { preloadedState });
    
    // Mock successful API response
    server.use(
      rest.put('/api/users/1', (req, res, ctx) => {
        return res(ctx.json({ id: 1, name: 'John Doe', email: 'john@example.com' }));
      })
    );
    
    fireEvent.click(screen.getByText('Edit Profile'));
    fireEvent.change(screen.getByLabelText('Name'), {
      target: { value: 'John Doe' },
    });
    fireEvent.click(screen.getByText('Save'));
    
    await waitFor(() => {
      expect(store.getState().user.data.name).toBe('John Doe');
    });
  });
});
```

### Zustand Testing Strategies

#### 1. Zustand Store Testing Setup

```javascript
// stores/testUtils.js
import { act, renderHook } from '@testing-library/react';
import { createUserStore } from './userStore';
import { createPostsStore } from './postsStore';

// Store factory for testing
export const createTestUserStore = (initialState = {}) => {
  const store = createUserStore();
  
  if (Object.keys(initialState).length > 0) {
    act(() => {
      store.setState(initialState);
    });
  }
  
  return store;
};

// Custom hook for testing stores
export const renderStoreHook = (store, selector) => {
  return renderHook(() => store(selector));
};

// Mock API utilities
export const mockApiCall = (response, delay = 0) => {
  return jest.fn().mockImplementation(
    () => new Promise((resolve) => {
      setTimeout(() => resolve(response), delay);
    })
  );
};

// Store state assertions
export const expectStoreState = (store, expectedState) => {
  expect(store.getState()).toMatchObject(expectedState);
};
```

#### 2. Store Unit Testing

```javascript
// __tests__/userStore.test.js
import { act } from '@testing-library/react';
import { createTestUserStore, expectStoreState } from '../testUtils';
import * as api from '../api/userApi';

// Mock the API module
jest.mock('../api/userApi');
const mockedApi = api as jest.Mocked<typeof api>;

describe('userStore', () => {
  let store;
  
  beforeEach(() => {
    store = createTestUserStore();
    jest.clearAllMocks();
  });
  
  describe('synchronous actions', () => {
    it('should set user data', () => {
      const userData = { id: 1, name: 'John Doe', email: 'john@example.com' };
      
      act(() => {
        store.getState().setUser(userData);
      });
      
      expectStoreState(store, {
        user: userData,
        loading: false,
        error: null,
      });
    });
    
    it('should update user profile', () => {
      const initialUser = { id: 1, name: 'John', email: 'john@example.com' };
      const updates = { name: 'John Doe', bio: 'Developer' };
      
      act(() => {
        store.getState().setUser(initialUser);
        store.getState().updateProfile(updates);
      });
      
      expectStoreState(store, {
        user: { ...initialUser, ...updates },
      });
    });
    
    it('should clear user data', () => {
      const userData = { id: 1, name: 'John Doe' };
      
      act(() => {
        store.getState().setUser(userData);
        store.getState().clearUser();
      });
      
      expectStoreState(store, {
        user: null,
        loading: false,
        error: null,
      });
    });
  });
  
  describe('asynchronous actions', () => {
    it('should fetch user successfully', async () => {
      const mockUser = { id: 1, name: 'John Doe', email: 'john@example.com' };
      mockedApi.fetchUser.mockResolvedValueOnce(mockUser);
      
      await act(async () => {
        await store.getState().fetchUser(1);
      });
      
      expect(mockedApi.fetchUser).toHaveBeenCalledWith(1);
      expectStoreState(store, {
        user: mockUser,
        loading: false,
        error: null,
      });
    });
    
    it('should handle fetch user error', async () => {
      const errorMessage = 'User not found';
      mockedApi.fetchUser.mockRejectedValueOnce(new Error(errorMessage));
      
      await act(async () => {
        await store.getState().fetchUser(999);
      });
      
      expectStoreState(store, {
        user: null,
        loading: false,
        error: errorMessage,
      });
    });
    
    it('should set loading state during async operations', async () => {
      let resolvePromise;
      const promise = new Promise((resolve) => {
        resolvePromise = resolve;
      });
      
      mockedApi.fetchUser.mockReturnValueOnce(promise);
      
      // Start async operation
      act(() => {
        store.getState().fetchUser(1);
      });
      
      // Check loading state
      expectStoreState(store, {
        loading: true,
        error: null,
      });
      
      // Resolve promise
      await act(async () => {
        resolvePromise({ id: 1, name: 'John' });
        await promise;
      });
      
      expectStoreState(store, {
        loading: false,
      });
    });
  });
});
```

#### 3. Hook Integration Testing

```javascript
// __tests__/useUserProfile.test.js
import { renderHook, act } from '@testing-library/react';
import { useUserProfile } from '../hooks/useUserProfile';
import { createTestUserStore } from '../testUtils';
import * as api from '../api/userApi';

jest.mock('../api/userApi');
const mockedApi = api as jest.Mocked<typeof api>;

describe('useUserProfile hook', () => {
  let store;
  
  beforeEach(() => {
    store = createTestUserStore();
    jest.clearAllMocks();
  });
  
  it('should return user profile data', () => {
    const userData = { id: 1, name: 'John Doe', email: 'john@example.com' };
    
    act(() => {
      store.getState().setUser(userData);
    });
    
    const { result } = renderHook(() => useUserProfile(store));
    
    expect(result.current.user).toEqual(userData);
    expect(result.current.loading).toBe(false);
    expect(result.current.error).toBeNull();
  });
  
  it('should handle profile updates', async () => {
    const initialUser = { id: 1, name: 'John', email: 'john@example.com' };
    const updatedUser = { ...initialUser, name: 'John Doe' };
    
    mockedApi.updateUser.mockResolvedValueOnce(updatedUser);
    
    act(() => {
      store.getState().setUser(initialUser);
    });
    
    const { result } = renderHook(() => useUserProfile(store));
    
    await act(async () => {
      await result.current.updateProfile({ name: 'John Doe' });
    });
    
    expect(result.current.user.name).toBe('John Doe');
  });
});
```

#### 4. Component Testing with Zustand

```javascript
// __tests__/UserProfileZustand.test.js
import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import UserProfile from '../components/UserProfile';
import { createTestUserStore } from '../testUtils';
import { UserStoreProvider } from '../providers/UserStoreProvider';
import * as api from '../api/userApi';

jest.mock('../api/userApi');
const mockedApi = api as jest.Mocked<typeof api>;

const renderWithStore = (component, store) => {
  return render(
    <UserStoreProvider store={store}>
      {component}
    </UserStoreProvider>
  );
};

describe('UserProfile with Zustand', () => {
  let store;
  
  beforeEach(() => {
    store = createTestUserStore();
    jest.clearAllMocks();
  });
  
  it('should display user information', () => {
    const userData = { id: 1, name: 'John Doe', email: 'john@example.com' };
    
    store.getState().setUser(userData);
    
    renderWithStore(<UserProfile />, store);
    
    expect(screen.getByText('John Doe')).toBeInTheDocument();
    expect(screen.getByText('john@example.com')).toBeInTheDocument();
  });
  
  it('should handle loading state', () => {
    store.getState().setLoading(true);
    
    renderWithStore(<UserProfile />, store);
    
    expect(screen.getByText('Loading...')).toBeInTheDocument();
  });
  
  it('should handle error state', () => {
    store.getState().setError('Failed to load user');
    
    renderWithStore(<UserProfile />, store);
    
    expect(screen.getByText('Failed to load user')).toBeInTheDocument();
  });
});
```

### Advanced Testing Patterns

#### 1. Time-Travel Testing

```javascript
// __tests__/timeTravel.test.js
import { createTestStore } from '../testUtils';
import { addTodo, toggleTodo, removeTodo } from '../slices/todosSlice';

describe('Time-travel testing', () => {
  it('should support undo/redo operations', () => {
    const store = createTestStore();
    const actions = [];
    
    // Record actions
    const originalDispatch = store.dispatch;
    store.dispatch = (action) => {
      actions.push(action);
      return originalDispatch(action);
    };
    
    // Perform actions
    store.dispatch(addTodo({ id: 1, text: 'Learn Redux', completed: false }));
    store.dispatch(addTodo({ id: 2, text: 'Learn Testing', completed: false }));
    store.dispatch(toggleTodo(1));
    
    const finalState = store.getState();
    
    // Replay actions
    const replayStore = createTestStore();
    actions.forEach(action => replayStore.dispatch(action));
    
    expect(replayStore.getState()).toEqual(finalState);
  });
});
```

#### 2. Performance Testing

```javascript
// __tests__/performance.test.js
import { renderHook } from '@testing-library/react';
import { useSelector } from 'react-redux';
import { createTestStore } from '../testUtils';
import { selectExpensiveComputation } from '../selectors';

describe('Performance testing', () => {
  it('should memoize expensive selectors', () => {
    const store = createTestStore();
    const mockComputation = jest.fn(() => 'computed value');
    
    // Mock the expensive computation
    jest.spyOn(require('../selectors'), 'expensiveComputation')
      .mockImplementation(mockComputation);
    
    const { result, rerender } = renderHook(
      () => useSelector(selectExpensiveComputation),
      {
        wrapper: ({ children }) => (
          <Provider store={store}>{children}</Provider>
        ),
      }
    );
    
    // First render
    expect(result.current).toBe('computed value');
    expect(mockComputation).toHaveBeenCalledTimes(1);
    
    // Re-render without state change
    rerender();
    expect(mockComputation).toHaveBeenCalledTimes(1); // Should not recompute
  });
});
```

### Best Practices

#### Testing Strategy
- **Unit Tests**: Test individual reducers, actions, and selectors
- **Integration Tests**: Test component-store interactions
- **E2E Tests**: Test complete user workflows
- **Performance Tests**: Verify memoization and optimization

#### Test Organization
- **Arrange-Act-Assert**: Structure tests clearly
- **Test Isolation**: Each test should be independent
- **Mock External Dependencies**: API calls, timers, etc.
- **Test Edge Cases**: Error states, loading states, empty data

#### Redux-Specific Testing
- **Pure Functions**: Reducers are easy to test
- **Action Creators**: Test both sync and async actions
- **Selectors**: Test memoization and computation
- **Middleware**: Test side effects and async flows

#### Zustand-Specific Testing
- **Store Isolation**: Create fresh stores for each test
- **State Mutations**: Test immer-based updates
- **Subscriptions**: Test reactive updates
- **Persistence**: Test hydration and serialization

### Comparison Summary

| Feature | Redux | Zustand |
|---------|-------|----------|
| **Test Setup** | More complex, requires providers | Simpler, direct store usage |
| **Mocking** | Mock actions and reducers | Mock store methods |
| **Time Travel** | Built-in with DevTools | Manual implementation |
| **Async Testing** | Thunk/Saga testing patterns | Promise-based testing |
| **Performance Testing** | Selector memoization testing | Subscription testing |
| **Integration Testing** | Provider wrapper required | Direct store injection |
| **Test Utilities** | Rich ecosystem (RTL, etc.) | Custom utilities needed |
| **Debugging** | Excellent DevTools support | Manual debugging tools |

---

Micro-frontends require sophisticated state management strategies to handle isolation, communication, and shared state across independent applications.

### Redux Implementation

#### Federated Store Architecture

```javascript
// shared/store-registry.js
class StoreRegistry {
  constructor() {
    this.stores = new Map();
    this.globalStore = null;
    this.eventBus = new EventTarget();
  }

  registerStore(appName, store) {
    this.stores.set(appName, store);
    this.eventBus.dispatchEvent(new CustomEvent('store-registered', {
      detail: { appName, store }
    }));
  }

  getStore(appName) {
    return this.stores.get(appName);
  }

  setGlobalStore(store) {
    this.globalStore = store;
  }

  broadcastAction(action, excludeApp = null) {
    this.stores.forEach((store, appName) => {
      if (appName !== excludeApp) {
        store.dispatch(action);
      }
    });
  }
}

export const storeRegistry = new StoreRegistry();
```

#### Shared State Slice

```javascript
// shared/shared-slice.js
import { createSlice } from '@reduxjs/toolkit';

const sharedSlice = createSlice({
  name: 'shared',
  initialState: {
    user: null,
    theme: 'light',
    notifications: [],
    crossAppData: {},
    eventHistory: []
  },
  reducers: {
    setUser: (state, action) => {
      state.user = action.payload;
      state.eventHistory.push({
        type: 'USER_UPDATED',
        timestamp: Date.now(),
        data: action.payload
      });
    },
    setTheme: (state, action) => {
      state.theme = action.payload;
    },
    addNotification: (state, action) => {
      state.notifications.push({
        id: Date.now(),
        ...action.payload
      });
    },
    setCrossAppData: (state, action) => {
      const { appName, data } = action.payload;
      state.crossAppData[appName] = data;
    },
    syncFromExternal: (state, action) => {
      const { source, data } = action.payload;
      Object.assign(state, data);
      state.eventHistory.push({
        type: 'EXTERNAL_SYNC',
        source,
        timestamp: Date.now()
      });
    }
  }
});

export const {
  setUser,
  setTheme,
  addNotification,
  setCrossAppData,
  syncFromExternal
} = sharedSlice.actions;

export default sharedSlice.reducer;
```

#### Cross-App Communication Middleware

```javascript
// shared/cross-app-middleware.js
import { storeRegistry } from './store-registry';

const crossAppMiddleware = (store) => (next) => (action) => {
  const result = next(action);
  
  // Handle cross-app actions
  if (action.meta?.crossApp) {
    const { targetApps, excludeCurrent } = action.meta.crossApp;
    
    if (targetApps) {
      targetApps.forEach(appName => {
        const targetStore = storeRegistry.getStore(appName);
        if (targetStore) {
          targetStore.dispatch({
            ...action,
            meta: { ...action.meta, fromApp: store.appName }
          });
        }
      });
    } else if (excludeCurrent) {
      storeRegistry.broadcastAction(action, store.appName);
    }
  }
  
  // Handle shared state synchronization
  if (action.type.startsWith('shared/')) {
    window.postMessage({
      type: 'REDUX_SHARED_ACTION',
      action,
      source: store.appName
    }, '*');
  }
  
  return result;
};

export default crossAppMiddleware;
```

#### Micro-Frontend Store Setup

```javascript
// app1/store.js
import { configureStore } from '@reduxjs/toolkit';
import { storeRegistry } from '../shared/store-registry';
import crossAppMiddleware from '../shared/cross-app-middleware';
import sharedReducer from '../shared/shared-slice';
import app1Reducer from './app1-slice';

const store = configureStore({
  reducer: {
    shared: sharedReducer,
    app1: app1Reducer
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: {
        ignoredActions: ['persist/PERSIST']
      }
    }).concat(crossAppMiddleware)
});

store.appName = 'app1';
storeRegistry.registerStore('app1', store);

// Listen for external state changes
window.addEventListener('message', (event) => {
  if (event.data.type === 'REDUX_SHARED_ACTION' && 
      event.data.source !== 'app1') {
    store.dispatch(event.data.action);
  }
});

export default store;
```

### Zustand Implementation

#### Federated Store Manager

```javascript
// shared/store-manager.js
import { subscribeWithSelector } from 'zustand/middleware';
import { createWithEqualityFn } from 'zustand/traditional';
import { shallow } from 'zustand/shallow';

class MicroFrontendStoreManager {
  constructor() {
    this.stores = new Map();
    this.sharedStore = null;
    this.eventBus = new EventTarget();
    this.subscriptions = new Map();
  }

  createSharedStore() {
    this.sharedStore = createWithEqualityFn(
      subscribeWithSelector((set, get) => ({
        user: null,
        theme: 'light',
        notifications: [],
        crossAppData: {},
        eventHistory: [],
        
        setUser: (user) => set((state) => {
          const newState = { ...state, user };
          newState.eventHistory.push({
            type: 'USER_UPDATED',
            timestamp: Date.now(),
            data: user
          });
          return newState;
        }),
        
        setTheme: (theme) => set({ theme }),
        
        addNotification: (notification) => set((state) => ({
          notifications: [...state.notifications, {
            id: Date.now(),
            ...notification
          }]
        })),
        
        setCrossAppData: (appName, data) => set((state) => ({
          crossAppData: {
            ...state.crossAppData,
            [appName]: data
          }
        })),
        
        syncFromExternal: (source, data) => set((state) => {
          const newState = { ...state, ...data };
          newState.eventHistory.push({
            type: 'EXTERNAL_SYNC',
            source,
            timestamp: Date.now()
          });
          return newState;
        })
      })),
      shallow
    );
    
    return this.sharedStore;
  }

  registerStore(appName, store) {
    this.stores.set(appName, store);
    
    // Set up cross-app communication
    const unsubscribe = store.subscribe(
      (state) => state,
      (state, prevState) => {
        this.eventBus.dispatchEvent(new CustomEvent('state-change', {
          detail: { appName, state, prevState }
        }));
      }
    );
    
    this.subscriptions.set(appName, unsubscribe);
  }

  broadcastAction(action, excludeApp = null) {
    this.stores.forEach((store, appName) => {
      if (appName !== excludeApp && store.actions) {
        const actionMethod = store.actions[action.type];
        if (actionMethod) {
          actionMethod(action.payload);
        }
      }
    });
  }
}

export const storeManager = new MicroFrontendStoreManager();
```

#### App-Specific Store with Cross-App Features

```javascript
// app1/store.js
import { createWithEqualityFn } from 'zustand/traditional';
import { subscribeWithSelector, persist } from 'zustand/middleware';
import { immer } from 'zustand/middleware/immer';
import { storeManager } from '../shared/store-manager';

const useApp1Store = createWithEqualityFn(
  persist(
    subscribeWithSelector(
      immer((set, get) => ({
        // App-specific state
        products: [],
        cart: [],
        filters: {},
        loading: false,
        
        // Actions
        actions: {
          addProduct: (product) => set((state) => {
            state.products.push(product);
          }),
          
          addToCart: (productId) => set((state) => {
            const product = state.products.find(p => p.id === productId);
            if (product) {
              state.cart.push(product);
              
              // Notify other apps
              const sharedStore = storeManager.getSharedStore();
              if (sharedStore) {
                sharedStore.getState().setCrossAppData('app1', {
                  cartCount: state.cart.length
                });
              }
            }
          }),
          
          broadcastCartUpdate: () => {
            const state = get();
            storeManager.broadcastAction({
              type: 'updateCartCount',
              payload: state.cart.length
            }, 'app1');
          }
        },
        
        // Computed values
        get cartTotal() {
          return get().cart.reduce((sum, item) => sum + item.price, 0);
        }
      }))
    ),
    { name: 'app1-store' }
  )
);

storeManager.registerStore('app1', useApp1Store);
export default useApp1Store;
```

#### Cross-App Communication Hook

```javascript
// shared/use-micro-frontend.js
import { useEffect, useCallback } from 'react';
import { storeManager } from './store-manager';

export const useMicroFrontend = (appName) => {
  const sharedStore = storeManager.getSharedStore();
  const appStore = storeManager.getStore(appName);
  
  const sharedState = sharedStore?.();
  const appState = appStore?.();
  
  const communicateWithApp = useCallback((targetApp, action) => {
    const targetStore = storeManager.getStore(targetApp);
    if (targetStore && targetStore.actions) {
      const actionMethod = targetStore.actions[action.type];
      if (actionMethod) {
        actionMethod(action.payload);
      }
    }
  }, []);
  
  const broadcastToAll = useCallback((action) => {
    storeManager.broadcastAction(action, appName);
  }, [appName]);
  
  // Set up cross-app event listeners
  useEffect(() => {
    const handleStateChange = (event) => {
      const { appName: sourceApp, state } = event.detail;
      if (sourceApp !== appName && sharedStore) {
        sharedStore.getState().setCrossAppData(sourceApp, {
          lastUpdate: Date.now(),
          summary: { hasData: Object.keys(state).length > 0 }
        });
      }
    };
    
    storeManager.eventBus.addEventListener('state-change', handleStateChange);
    
    return () => {
      storeManager.eventBus.removeEventListener('state-change', handleStateChange);
    };
  }, [appName, sharedStore]);
  
  return {
    sharedState,
    appState,
    communicateWithApp,
    broadcastToAll
  };
};
```

### Best Practices

#### Architecture
- **Isolation**: Keep app-specific state separate from shared state
- **Communication**: Use event-driven architecture for loose coupling
- **Versioning**: Version shared state schemas for backward compatibility
- **Boundaries**: Define clear boundaries between micro-frontends

#### Performance
- **Lazy Loading**: Load stores only when micro-frontends are mounted
- **Selective Sync**: Only sync necessary state between apps
- **Debouncing**: Debounce cross-app communications to avoid spam
- **Memory Management**: Clean up subscriptions when apps unmount

#### Security
- **Validation**: Validate all cross-app communications
- **Sanitization**: Sanitize data before sharing between apps
- **Access Control**: Implement proper access controls for shared state
- **Audit Trail**: Log all cross-app state changes

### Comparison Summary

| Feature | Redux | Zustand |
|---------|-------|----------|
| **Setup Complexity** | High (multiple stores, middleware) | Medium (store manager) |
| **Cross-App Communication** | Middleware-based | Event-driven |
| **State Isolation** | Provider boundaries | Store boundaries |
| **Shared State** | Federated reducers | Shared store instance |
| **DevTools** | Excellent (Redux DevTools) | Custom implementation |
| **Performance** | Good (with optimization) | Excellent (minimal overhead) |
| **Type Safety** | Good (with TypeScript) | Excellent (TypeScript-first) |
| **Learning Curve** | Steep (complex patterns) | Moderate (simpler concepts) |

### Q15: What is Redux Thunk?
**Difficulty: Intermediate**

**Answer:**
Redux Thunk is a middleware that allows you to write action creators that return a function instead of an action.
*   **Purpose:** To handle asynchronous logic (like API calls) or complex synchronous logic.
*   **Mechanism:** The thunk function receives `dispatch` and `getState` as arguments.
```javascript
const fetchUser = (id) => async (dispatch, getState) => {
  dispatch({ type: 'FETCH_START' });
  const response = await api.getUser(id);
  dispatch({ type: 'FETCH_SUCCESS', payload: response.data });
};
```

### Q16: What is Redux Saga?
**Difficulty: Advanced**

**Answer:**
A middleware for handling side effects in Redux using **Generator Functions**.
*   **Concept:** Uses an ES6 feature called Generators (`function*`) to make async code look synchronous.
*   **Pros:** easier to test, powerful effects (race, call, put, takeLatest).
*   **Cons:** steeper learning curve than Thunk.

### Q17: Redux Thunk vs Redux Saga.
**Difficulty: Advanced**

**Answer:**
*   **Thunk:**
    *   Simple functions.
    *   Easy to learn.
    *   Good for simple async logic.
    *   Harder to test complex flows (callbacks/promises).
*   **Saga:**
    *   Generator functions.
    *   Steeper learning curve.
    *   Great for complex flows (retries, cancellation, race conditions).
    *   Declarative style (easy to test).

### Q18: What is Immer?
**Difficulty: Intermediate**

**Answer:**
A library to work with immutable state in a more convenient way.
*   **Mechanism:** You write code that "mutates" a draft state, and Immer produces the next immutable state based on those changes.
*   **Usage in Redux Toolkit:** RTK uses Immer internally in `createSlice`, allowing you to write "mutating" logic in reducers:
    ```javascript
    reducer: (state, action) => {
      state.value += 1; // Looks mutating, but is safe thanks to Immer
    }
    ```

### Q19: What is `createSlice` in Redux Toolkit?
**Difficulty: Beginner**

**Answer:**
A function that accepts an initial state, an object of reducer functions, and a slice name.
*   **Generates:** Action creators and action types automatically.
*   **Reduces Boilerplate:** No need to manually write switch statements or define action type constants.

### Q20: What is the `connect` function?
**Difficulty: Intermediate**

**Answer:**
A Higher-Order Component (HOC) from `react-redux` used to connect a React component to the Redux store.
*   **Arguments:**
    1.  `mapStateToProps`: Select data from store.
    2.  `mapDispatchToProps`: Dispatch actions.
*   *Note:* In modern React with Hooks, `useSelector` and `useDispatch` are preferred over `connect`.

### Q21: `useSelector` vs `useDispatch`.
**Difficulty: Beginner**

**Answer:**
Hooks provided by `react-redux`.
*   **`useSelector`:** Reads a value from the store state and subscribes to updates.
    *   `const count = useSelector(state => state.counter.value)`
*   **`useDispatch`:** Returns the dispatch function to send actions.
    *   `const dispatch = useDispatch(); dispatch(increment())`

### Q22: What is the Flux Architecture?
**Difficulty: Intermediate**

**Answer:**
An application architecture pattern created by Facebook for building client-side web apps. Redux is inspired by Flux.
*   **Unidirectional Data Flow:** Action -> Dispatcher -> Store -> View.
*   **Single Direction:** Data flows in one direction, making it easier to reason about state changes.

### Q23: Explain "Single Source of Truth".
**Difficulty: Beginner**

**Answer:**
A fundamental principle of Redux.
*   The entire state of the application is stored in an object tree within a single **Store**.
*   Makes it easier to debug/inspect the application state.
*   Enables features like "Time Travel Debugging".

### Q24: What are "Selectors"?
**Difficulty: Intermediate**

**Answer:**
Functions that extract specific pieces of data from the Redux store state.
*   **Basic:** `state => state.users.list`
*   **Memoized (Reselect):** Library to create selectors that only recompute when inputs change.
    *   Prevents unnecessary re-renders and expensive recalculations.

### Q25: Zustand: `create` store.
**Difficulty: Beginner**

**Answer:**
How to create a store in Zustand.
```javascript
import { create } from 'zustand'

const useStore = create((set) => ({
  bears: 0,
  increasePopulation: () => set((state) => ({ bears: state.bears + 1 })),
  removeAllBears: () => set({ bears: 0 }),
}))
```
*   Returns a hook `useStore` to be used in components.

### Q26: Zustand vs Redux: Boilerplate.
**Difficulty: Beginner**

**Answer:**
*   **Redux:** Traditionally high boilerplate (actions, types, reducers, store setup). Redux Toolkit reduced this significantly.
*   **Zustand:** Very low boilerplate. No providers (context-less), no reducers required (just setter functions).

### Q27: How to handle async actions in Zustand?
**Difficulty: Intermediate**

**Answer:**
Just use async/await inside the store actions.
```javascript
const useStore = create((set) => ({
  fish: 0,
  fetchFish: async () => {
    const response = await fetch('/pond');
    set({ fish: await response.json() });
  },
}))
```
No middleware needed (unlike Redux).

### Q28: How to access Zustand store outside React components?
**Difficulty: Advanced**

**Answer:**
The hook created by `create` has utility methods attached to it.
*   `useStore.getState()`: Get current state.
*   `useStore.setState({ ... })`: Update state.
*   `useStore.subscribe(callback)`: Listen to changes.
Useful for using state in vanilla JS files or utility functions.

### Q29: What is "Transient Updates" in Zustand?
**Difficulty: Advanced**

**Answer:**
Updating state without causing a re-render of the component.
*   Useful for high-frequency updates (e.g., scroll position, animation).
*   Can be achieved using `subscribe` directly in `useEffect` refs instead of selecting state.

### Q30: How to persist state in Zustand?
**Difficulty: Intermediate**

**Answer:**
Use the `persist` middleware.
```javascript
import { persist } from 'zustand/middleware'

const useStore = create(
  persist(
    (set) => ({ ... }),
    { name: 'food-storage' } // stores in localStorage by default
  )
)
```

### Q31: What is Redux DevTools Extension?
**Difficulty: Beginner**

**Answer:**
A browser extension that provides a UI to inspect Redux state and actions.
*   **Features:**
    *   View action history log.
    *   Inspect state diffs.
    *   Time Travel (jump back to previous state).
    *   Dispatch actions manually.
*   Zustand can also connect to Redux DevTools via middleware.

### Q32: MobX vs Redux.
**Difficulty: Intermediate**

**Answer:**
*   **Redux:**
    *   Functional, Immutable.
    *   Explicit updates via actions/reducers.
    *   More boilerplate.
*   **MobX:**
    *   OOP, Mutable.
    *   "Magical" automatic tracking of observables (using Proxy).
    *   Less boilerplate.
    *   Harder to debug (updates happen automatically).

### Q33: What is RTK Query?
**Difficulty: Advanced**

**Answer:**
A powerful data fetching and caching tool included in Redux Toolkit.
*   **Features:**
    *   Automatic caching and deduplication of requests.
    *   Polling / Auto-refetching.
    *   Optimistic Updates.
    *   Generates hooks (`useGetPokemonQuery`).
*   Eliminates the need to write thunks/reducers for data fetching.

### Q34: Explain `reselect` library.
**Difficulty: Advanced**

**Answer:**
A library for creating memoized, composable selector functions.
*   `createSelector(...inputSelectors, resultFunc)`
*   If input selectors return the same values as last time, `resultFunc` is skipped and cached result is returned.
*   Essential for performance when deriving complex data from state.

### Q35: What is the "Provider" component in Redux?
**Difficulty: Beginner**

**Answer:**
`<Provider store={store}>`
*   Wraps the React application (usually at the root).
*   Makes the Redux store available to any nested components that need to connect to it (via hooks or connect).
*   Uses React Context internally.

### Q36: How to reset state in Redux?
**Difficulty: Intermediate**

**Answer:**
Handle a specific action (e.g., `LOGOUT`) in the root reducer.
```javascript
const rootReducer = (state, action) => {
  if (action.type === 'LOGOUT') {
    state = undefined; // Resets all reducers to initial state
  }
  return appReducer(state, action);
}
```

### Q37: Multiple Stores in Redux?
**Difficulty: Advanced**

**Answer:**
*   **Standard Redux:** Recommends a **Single Store**.
*   **Why?** Easier debugging, single source of truth, easy state hydration/persistence.
*   **Multiple Stores:** Possible but discouraged. Makes it hard to share data between different parts of the app and breaks DevTools integration.

### Q38: Zustand: `set` function patterns.
**Difficulty: Intermediate**

**Answer:**
*   **Merge:** `set({ count: 1 })` (merges with existing state, shallowly).
*   **Replace:** `set({ count: 1 }, true)` (replaces entire state object).
*   **Functional:** `set(state => ({ count: state.count + 1 }))` (depends on previous state).

### Q39: How to test Redux reducers?
**Difficulty: Beginner**

**Answer:**
Reducers are pure functions, so they are easy to test.
```javascript
test('should handle increment', () => {
  const startState = { value: 0 };
  const action = { type: 'counter/increment' };
  const endState = reducer(startState, action);
  expect(endState).toEqual({ value: 1 });
});
```

### Q40: How to test Redux async thunks?
**Difficulty: Advanced**

**Answer:**
1.  Mock the store (`redux-mock-store`).
2.  Mock the API calls (using `jest.spyOn` or `msw`).
3.  Dispatch the thunk.
4.  Assert that the expected actions (START, SUCCESS) were dispatched.

### Q41: Recoil vs Redux.
**Difficulty: Intermediate**

**Answer:**
*   **Recoil:**
    *   Created by Facebook (experimental).
    *   **Atoms** (state units) and **Selectors** (derived state).
    *   Designed for highly granular updates (performance in massive apps).
    *   React-ish API.
*   **Redux:**
    *   Centralized store.
    *   Strict patterns.

### Q42: Jotai vs Zustand.
**Difficulty: Intermediate**

**Answer:**
Both are from the Poimandres group.
*   **Jotai:** Atomic model (like Recoil). State is split into tiny atoms. Good for derived state and frequent granular updates.
*   **Zustand:** Store model (like Redux but simplified). One or few big stores. Good for global client state.

### Q43: What is "Optimistic UI"?
**Difficulty: Advanced**

**Answer:**
Updating the UI *immediately* after a user action, assuming the server request will succeed, instead of waiting for the server response.
*   **Failure:** If server fails, rollback the change.
*   **Benefit:** App feels instant/snappy.
*   **Implementation:** Supported natively in RTK Query and React Query.

### Q44: How to structure Redux files?
**Difficulty: Beginner**

**Answer:**
1.  **Rails-style:** Folders for `actions`, `reducers`, `constants`. (Old way).
2.  **Ducks pattern:** Bundle action types, actions, and reducers for a feature in one file (module).
3.  **Feature Folder (Slice):** Modern RTK way. `features/users/userSlice.js`.

### Q45: Why state immutability is important?
**Difficulty: Intermediate**

**Answer:**
1.  **Predictability:** State history is preserved.
2.  **Performance:** Shallow equality checking (`oldState === newState`) is fast. If references are different, component re-renders. Deep comparison is slow.
3.  **Debugging:** Enables Time Travel.

### Q46: `shallow` comparison in Zustand.
**Difficulty: Intermediate**

**Answer:**
By default, Zustand uses strict equality `===` to detect changes.
If you select an object `state => ({ a: state.a, b: state.b })`, it creates a new object every time, causing re-renders.
**Solution:**
```javascript
import { shallow } from 'zustand/shallow'
const { a, b } = useStore(state => ({ a: state.a, b: state.b }), shallow)
```

### Q47: Redux Middleware signature.
**Difficulty: Expert**

**Answer:**
Curried function signature:
`store => next => action => { ... }`
```javascript
const logger = store => next => action => {
  console.log('dispatching', action);
  let result = next(action);
  console.log('next state', store.getState());
  return result;
}
```

### Q48: How to handle side effects in Zustand?
**Difficulty: Beginner**

**Answer:**
Zustand does not have a specific "middleware" for side effects like Redux Saga.
Side effects are handled simply inside the **actions** (functions in the store).
You can call APIs, set timeouts, etc., directly before calling `set()`.

### Q49: What is `combineReducers`?
**Difficulty: Beginner**

**Answer:**
Helper function in Redux to split the root reducer into smaller reducers based on state slice.
```javascript
const rootReducer = combineReducers({
  users: usersReducer,
  posts: postsReducer
});
```

### Q50: Context + useReducer vs Redux.
**Difficulty: Intermediate**

**Answer:**
You can mimic Redux with `useContext` + `useReducer`.
*   **Pros:** Built-in, no extra libraries.
*   **Cons:** No DevTools, no middleware ecosystem, performance issues (Context updates re-render all consumers unless optimized carefully), manual setup of boilerplate.
*   **Use Redux** if you need the ecosystem/performance for complex apps.

### Q51: How to type Redux state (TypeScript)?
**Difficulty: Intermediate**

**Answer:**
With RTK:
```typescript
// store.ts
export type RootState = ReturnType<typeof store.getState>
export type AppDispatch = typeof store.dispatch
```
Use typed hooks: `useAppSelector` and `useAppDispatch`.

### Q52: How to type Zustand store (TypeScript)?
**Difficulty: Intermediate**

**Answer:**
```typescript
interface BearState {
  bears: number
  increase: (by: number) => void
}
const useStore = create<BearState>((set) => ({
  bears: 0,
  increase: (by) => set((state) => ({ bears: state.bears + by })),
}))
```

### Q53: Dynamic Reducers in Redux?
**Difficulty: Advanced**

**Answer:**
Loading reducers on the fly (Code Splitting).
*   Useful for large apps where you don't want to load all reducers at startup.
*   Requires a `store.injectReducer` helper method to replace the root reducer using `store.replaceReducer()`.

### Q54: What is the "Container/Presentational" pattern?
**Difficulty: Intermediate**

**Answer:**
*   **Presentational (Dumb):** Concerned with how things *look*. Receive data via props. No dependency on Redux.
*   **Container (Smart):** Concerned with how things *work*. Connect to Redux, fetch data, pass props to Presentational components.
*   *Note:* Hooks (`useSelector`) have made this pattern less strict/necessary.

### Q55: Explain `bindActionCreators`.
**Difficulty: Advanced**

**Answer:**
Redux utility.
*   Wraps action creators in `dispatch` calls.
*   `bindActionCreators({ add }, dispatch)` returns `{ add: (...args) => dispatch(add(...args)) }`.
*   Mostly used in `mapDispatchToProps` (legacy connect API).

### Q56: Redux Toolkit `createAsyncThunk`.
**Difficulty: Intermediate**

**Answer:**
A helper to generate thunks that dispatch `pending`, `fulfilled`, and `rejected` action types automatically.
```javascript
const fetchUser = createAsyncThunk(
  'users/fetch',
  async (userId, thunkAPI) => {
    const response = await api.get(userId);
    return response.data;
  }
)
```

### Q57: How `createEntityAdapter` helps?
**Difficulty: Advanced**

**Answer:**
RTK helper to manage normalized data (IDs and Entities).
*   Provides reducers: `addOne`, `removeOne`, `updateMany`.
*   Provides selectors: `selectAll`, `selectById`.
*   Simplifies CRUD operations in state.

### Q58: What is "Normalization" in State?
**Difficulty: Advanced**

**Answer:**
Structuring state like a database.
*   Store data in objects indexed by ID: `{ ids: [1, 2], entities: { 1: { ... }, 2: { ... } } }`.
*   Avoids duplication.
*   Makes updates easier (update in one place).
*   Libraries: `normalizr`, RTK `createEntityAdapter`.

### Q59: Zustand vs Context Performance.
**Difficulty: Intermediate**

**Answer:**
*   **Context:** Changing a value in Provider re-renders **all** consumers. Requires splitting context or `useMemo` to optimize.
*   **Zustand:** Consumers rely on **selectors**. A component only re-renders if the *selected* slice of state changes. Better default performance.

### Q60: Can you use Redux and Zustand together?
**Difficulty: Beginner**

**Answer:**
Yes.
*   They are just libraries.
*   You might use Redux for legacy global state and Zustand for new modules or UI state.
*   However, having two sources of truth is generally discouraged for maintainability.

### Q61: What is `store.subscribe`?
**Difficulty: Beginner**

**Answer:**
Low-level listener to store changes.
*   Called whenever an action is dispatched.
*   `const unsubscribe = store.subscribe(() => console.log(store.getState()))`.
*   UI bindings (react-redux) use this internally.

### Q62: How to handle WebSocket data in Redux?
**Difficulty: Advanced**

**Answer:**
Use a middleware.
*   Middleware opens socket connection on startup (`init` action).
*   Listens to socket messages and dispatches Redux actions (`SOCKET_MESSAGE`).
*   Listens to Redux actions (`SEND_MESSAGE`) and emits to socket.

### Q63: What is "Action Creator"?
**Difficulty: Beginner**

**Answer:**
A function that creates and returns an action object.
```javascript
function addTodo(text) {
  return { type: 'ADD_TODO', text }
}
```

### Q64: Pure Functions in Redux.
**Difficulty: Beginner**

**Answer:**
Reducers must be pure functions.
1.  Return value depends ONLY on arguments.
2.  No side effects (no API calls, no mutation).
3.  Given same input, always return same output.

### Q65: Explain "Time Travel Debugging".
**Difficulty: Intermediate**

**Answer:**
Ability to move back and forth among the past states of the application.
*   Possible because Redux state is immutable and actions are recorded.
*   DevTools can "replay" actions or "jump" to a specific state snapshot.

### Q66: Why use `const` for Action Types?
**Difficulty: Beginner**

**Answer:**
`const ADD_TODO = 'ADD_TODO'`
*   Prevents typos (string literals don't throw errors, undefined variables do).
*   Better IDE autocompletion.
*   Easier to refactor.

### Q67: Zustand `subscribe` with selector.
**Difficulty: Advanced**

**Answer:**
Zustand allows subscribing to a specific slice of state.
```javascript
const unsub = useStore.subscribe(
  (state) => state.paw,
  (paw) => console.log('paw changed', paw)
)
```

### Q68: How to secure Redux state?
**Difficulty: Intermediate**

**Answer:**
State is in memory (JS variables), so it's accessible via console/debugger.
*   Don't store highly sensitive data (plain text passwords, full credit card numbers) in state if possible.
*   Clear state on logout.
*   Encrypt data if persisting to localStorage.

### Q69: Server-Side Rendering (SSR) with Redux.
**Difficulty: Advanced**

**Answer:**
1.  Create a store instance on the server for every request.
2.  Dispatch actions to fetch initial data.
3.  Get state (`store.getState()`).
4.  Embed state in HTML (`window.__PRELOADED_STATE__`).
5.  On client, create store using preloaded state (Hydration).

### Q70: Atomic State Management.
**Difficulty: Intermediate**

**Answer:**
Approach used by Recoil/Jotai.
*   State is distributed in small "atoms".
*   Components subscribe to specific atoms.
*   Contrasts with Redux's "Single State Tree".

### Q71: What is "Prop Drilling"?
**Difficulty: Beginner**

**Answer:**
Passing props through multiple levels of components.
*   Component A -> B -> C -> D. Only D needs the prop.
*   Redux/Zustand solves this by allowing D to access store directly.

### Q72: How to clear Redux cache?
**Difficulty: Intermediate**

**Answer:**
*   If using `redux-persist`: `persistor.purge()`.
*   If using RTK Query: `dispatch(api.util.resetApiState())`.

### Q73: Explain `redux-persist`.
**Difficulty: Intermediate**

**Answer:**
Library to save Redux state to persistent storage (localStorage, AsyncStorage) and rehydrate it on app launch.
*   Prevents data loss on page refresh.
*   Configurable (whitelist/blacklist specific reducers).

### Q74: `useStore` vs `useSelector` (Zustand vs Redux).
**Difficulty: Beginner**

**Answer:**
*   **Redux:** `useSelector` is the standard hook.
*   **Zustand:** The store itself is a hook. `useStore(selector)`.

### Q75: Why is Redux synchronous?
**Difficulty: Intermediate**

**Answer:**
Reducers are synchronous pure functions to calculate the next state immediately.
This guarantees order and predictability.
Async operations are handled *before* reaching the reducer (in middleware).

### Q76: What is "derived state"?
**Difficulty: Beginner**

**Answer:**
State that can be calculated from other state.
*   Example: `fullName` derived from `firstName` and `lastName`.
*   Should NOT be stored in state (redundant). Calculate it in render or use Selectors.

### Q77: How to structure large Redux apps?
**Difficulty: Advanced**

**Answer:**
*   **Feature-based folders:** Group logic by feature (Auth, Feed, Profile).
*   **Ducks/Slices:** Keep logic together.
*   **Normalized State:** Flatten nested data.
*   **Reselect:** Heavily use selectors for data access.

### Q78: Zustand middlewares list.
**Difficulty: Intermediate**

**Answer:**
Common middlewares:
*   `persist`: Storage persistence.
*   `devtools`: Redux DevTools connection.
*   `subscribeWithSelector`: Enhanced subscription.
*   `immer`: Use Immer for updates.

### Q79: What is `extraReducers`?
**Difficulty: Intermediate**

**Answer:**
Field in `createSlice` (RTK).
*   Allows the slice to respond to actions defined *outside* of the slice (e.g., async thunks, or actions from other slices).
*   Uses a builder pattern: `builder.addCase(otherAction, ...)`

### Q80: Benefits of RTK over vanilla Redux.
**Difficulty: Beginner**

**Answer:**
1.  Simple store setup (`configureStore`).
2.  Immer built-in (write mutable code).
3.  No switch statements (createSlice).
4.  Thunk built-in.
5.  DevTools enabled by default.

### Q81: Zustand: How to reset store?
**Difficulty: Intermediate**

**Answer:**
Zustand doesn't have a built-in reset. Pattern:
```javascript
const initialState = { count: 0 }
const useStore = create(set => ({
  ...initialState,
  reset: () => set(initialState)
}))
```

### Q82: How to use Immer with Zustand?
**Difficulty: Intermediate**

**Answer:**
Wrap the state creator with `immer` middleware.
```javascript
import { immer } from 'zustand/middleware/immer'
const useStore = create(immer((set) => ({
  bees: 0,
  addBee: () => set((state) => { state.bees += 1 }) // Mutation allowed
})))
```

### Q83: Can Redux work without React?
**Difficulty: Beginner**

**Answer:**
Yes. Redux is a standalone JS library.
*   Can be used with Vanilla JS, Angular, Vue, Ember.
*   `react-redux` is the binding library for React.

### Q84: What is "Enhancer" in Redux?
**Difficulty: Advanced**

**Answer:**
Higher-order function that adds capabilities to the store.
*   `applyMiddleware` is the most common enhancer.
*   DevTools is an enhancer.
*   It wraps `createStore` to override its methods (dispatch, getState, subscribe).

### Q85: How to handle error handling in Redux?
**Difficulty: Intermediate**

**Answer:**
*   Dispatch `FAILURE` actions with error payload.
*   Store `error` state in reducer (`loading`, `data`, `error`).
*   Display error in UI based on state.
*   Global error handling: Custom middleware to catch rejected actions and show toasts.

### Q86: Zustand vs Context API for Global State.
**Difficulty: Intermediate**

**Answer:**
Zustand is often better for global state because:
1.  **Performance:** Fixes the re-render issue of Context without complex workarounds.
2.  **Usage:** Can be used outside components.
3.  **Features:** Middleware support (persist, devtools).

### Q87: What is a "Draft" state (Immer)?
**Difficulty: Intermediate**

**Answer:**
A proxy object provided by Immer.
*   You modify the draft.
*   Immer records changes.
*   Immer generates the new immutable state tree.

### Q88: How to handle form state in Redux?
**Difficulty: Intermediate**

**Answer:**
*   Generally discouraged to put *every* keystroke in Redux (performance).
*   Use local state (`useState`) or form libraries (`React Hook Form`, `Formik`) for transient form state.
*   Dispatch to Redux only on Submit.

### Q89: Why Redux boilerplate was reduced?
**Difficulty: General**

**Answer:**
Community complaint was "too much code for simple things".
*   Redux Toolkit was created to standardize best practices and hide configuration.

### Q90: Zustand: Multiple stores vs Single store.
**Difficulty: Advanced**

**Answer:**
*   Zustand allows creating multiple isolated stores (`useAuthStore`, `useCartStore`).
*   **Pros:** Modular, code splitting.
*   **Cons:** Harder to interact between stores (need to import both).
*   Redux enforces single store.

### Q91: What is "Declarative" vs "Imperative" in State?
**Difficulty: General**

**Answer:**
*   **Imperative:** "Change X to Y" (jQuery).
*   **Declarative:** "State is Y, render UI accordingly" (React/Redux).
*   Redux is declarative: You describe the *state*, UI updates automatically.

### Q92: How to mock Redux for integration tests?
**Difficulty: Advanced**

**Answer:**
Wrap the test component in a `<Provider store={customStore}>`.
*   Create a real store instance for the test (integration test).
*   Or use `redux-mock-store` for unit testing actions/reducers specifically.

### Q93: Explain "Hydration" error.
**Difficulty: Advanced**

**Answer:**
Occurs in SSR (Next.js) when the server-rendered HTML (based on initial state) differs from the client-side rendered HTML (after hydration).
*   Common cause: Random values, dates, or state mismatch between server and client store.

### Q94: Does Zustand use React Context?
**Difficulty: Intermediate**

**Answer:**
No.
*   Zustand uses module scope for the store and custom listeners for updates.
*   This is why it doesn't require a `<Provider>` wrapper.

### Q95: When to use `useLayoutEffect` with state?
**Difficulty: Advanced**

**Answer:**
Rarely.
*   Use if you need to synchronously re-render based on state change *before* browser paints (to avoid flicker).
*   Standard state updates usually work fine with `useEffect`.

### Q96: How to handle heavy computation in Redux?
**Difficulty: Intermediate**

**Answer:**
*   Don't do it in the reducer (blocks UI).
*   Do it in a Web Worker.
*   Or use memoized selectors (Reselect) to avoid re-computing.

### Q97: Redux `compose`.
**Difficulty: Advanced**

**Answer:**
Functional programming utility.
*   `compose(f, g, h)(x)` is `f(g(h(x)))`.
*   Used to apply multiple store enhancers/middlewares.

### Q98: State Management trends 2024.
**Difficulty: General**

**Answer:**
*   **Server State:** React Query / RTK Query / SWR (handling API data).
*   **Client State:** Zustand / Jotai / Signals (handling UI state).
*   **Redux:** Still huge, but RTK is the standard way.

### Q99: What are "Signals"?
**Difficulty: Advanced**

**Answer:**
A reactive state primitive (popularized by SolidJS, Preact, Angular).
*   Fine-grained reactivity.
*   Update values, and only the DOM text node bound to it updates (bypassing VDOM diffing in some frameworks).
*   Different model than Redux/Zustand.

### Q100: Best library for simple global state?
**Difficulty: General**

**Answer:**
**Zustand**.
*   Small bundle size.
*   Simple API.
*   No provider hell.
*   Performance is great by default.
