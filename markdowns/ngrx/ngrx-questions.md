<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="NgRx & Angular State Management Logo" width="100" height="100">
  </a>
  <h1>NgRx & Angular State Management Interview Questions & Answers</h1>
  <p><b>Comprehensive interview questions covering NgRx Store, Effects, Entity, ComponentStore, and SignalStore</b></p>
</div>

---

## Table of Contents

1. [Explain the Core Redux Architecture in NgRx (Store, Actions, Reducers, Selectors, Effects)?](#q1) <span class="intermediate">Intermediate</span>
2. [What is NgRx SignalStore (introduced in NgRx 17+) and how does it revolutionize state management?](#q2) <span class="advanced">Advanced</span>
3. [How do NgRx Effects handle concurrency and cancellation with RxJS flattening operators (`switchMap`, `exhaustMap`, `concatMap`, `mergeMap`)?](#q3) <span class="advanced">Advanced</span>
4. [How does NgRx Entity Adapter (`@ngrx/entity`) manage normalized entity collections?](#q4) <span class="intermediate">Intermediate</span>
5. [What is NgRx ComponentStore and when should you use it over global Store?](#q5) <span class="intermediate">Intermediate</span>
6. [How do memoized selectors created with `createSelector` optimize Angular rendering?](#q6) <span class="intermediate">Intermediate</span>
7. [What is `createActionGroup` in NgRx 15+ and how does it reduce action boilerplate?](#q7) <span class="beginner">Beginner</span>
8. [How does `@ngrx/router-store` integrate Angular Router navigation with NgRx state?](#q8) <span class="advanced">Advanced</span>
9. [How do you test NgRx Reducers with unit tests?](#q9) <span class="beginner">Beginner</span>
10. [How do you test NgRx Effects with `provideMockActions` in Jasmine/Vitest?](#q10) <span class="intermediate">Intermediate</span>
11. [What is `MetaReducer` in NgRx and how do you implement a logger or state hydration meta-reducer?](#q11) <span class="advanced">Advanced</span>
12. [How do you handle pagination with NgRx Entity Adapter?](#q12) <span class="intermediate">Intermediate</span>
13. [What are Action Sanitizers and State Sanitizers in `@ngrx/store-devtools`?](#q13) <span class="intermediate">Intermediate</span>
14. [How do you use `provideStore` and `provideEffects` in standalone Angular applications?](#q14) <span class="beginner">Beginner</span>
15. [What is the difference between `Store.select()` and `Store.selectSignal()` in NgRx 16+?](#q15) <span class="intermediate">Intermediate</span>
16. [How do you implement Optimistic Updates in NgRx Effects?](#q16) <span class="advanced">Advanced</span>
17. [What is the purpose of `ofType` operator in NgRx Effects?](#q17) <span class="beginner">Beginner</span>
18. [How do you handle WebSocket streaming data in NgRx Effects?](#q18) <span class="advanced">Advanced</span>
19. [What is the difference between `defaultRouterState` and `customRouterStateSerializer` in `@ngrx/router-store`?](#q19) <span class="advanced">Advanced</span>
20. [How do you handle multi-action dispatching from a single NgRx Effect?](#q20) <span class="intermediate">Intermediate</span>
21. [What is `@ngrx/schematics` and how does it automate NgRx boilerplate generation?](#q21) <span class="beginner">Beginner</span>
22. [How do you prevent cyclic dependency issues in NgRx selectors?](#q22) <span class="intermediate">Intermediate</span>
23. [What is the purpose of `StoreDevtoolsModule.instrument()`?](#q23) <span class="beginner">Beginner</span>
24. [How do you handle JWT Token Refresh in NgRx Effects?](#q24) <span class="advanced">Advanced</span>
25. [What are Non-Dispatching Effects (`dispatch: false`) and when should you use them?](#q25) <span class="beginner">Beginner</span>
26. [How do you manage complex wizard multi-step state with NgRx?](#q26) <span class="intermediate">Intermediate</span>
27. [What is the difference between `@ngrx/signals` and `@ngrx/store`?](#q27) <span class="advanced">Advanced</span>
28. [How do you test NgRx Selectors with `projector` functions?](#q28) <span class="beginner">Beginner</span>
29. [How do you implement local storage persistence with NgRx Meta-Reducers?](#q29) <span class="intermediate">Intermediate</span>
30. [What is `createFeature` in NgRx 14+ and how does it generate automatic selectors?](#q30) <span class="intermediate">Intermediate</span>
31. [How do you handle file uploads with progress in NgRx?](#q31) <span class="intermediate">Intermediate</span>
32. [What is the difference between `props<{}>()` and `emptyProps()` in NgRx actions?](#q32) <span class="beginner">Beginner</span>
33. [How do you handle race conditions in NgRx with `switchMap` in Effects?](#q33) <span class="intermediate">Intermediate</span>
34. [What is the purpose of `USER_PROVIDED_META_REDUCERS` injection token?](#q34) <span class="advanced">Advanced</span>
35. [How do you manage Undo/Redo actions in NgRx?](#q35) <span class="advanced">Advanced</span>
36. [What is the difference between `withEntities` in SignalStore vs `@ngrx/entity`?](#q36) <span class="advanced">Advanced</span>
37. [How do you handle cross-feature selector composition in NgRx?](#q37) <span class="intermediate">Intermediate</span>
38. [What is the purpose of `ROOT_REDUCERS` and `FEATURE_REDUCERS` injection tokens?](#q38) <span class="advanced">Advanced</span>
39. [How do you implement Auto-Save form fields with NgRx ComponentStore?](#q39) <span class="intermediate">Intermediate</span>
40. [What is the difference between `createAction` and legacy Action class implementations?](#q40) <span class="beginner">Beginner</span>
41. [How do you handle polling endpoints in NgRx Effects?](#q41) <span class="intermediate">Intermediate</span>
42. [What is the purpose of `ngrxOnStoreInit` and `ngrxOnInitEffects` lifecycle hooks?](#q42) <span class="intermediate">Intermediate</span>
43. [How do you configure strict runtime immutability checks in NgRx?](#q43) <span class="intermediate">Intermediate</span>
44. [What is the difference between `ActionGroup` events vs commands in NgRx naming conventions?](#q44) <span class="intermediate">Intermediate</span>
45. [How do you test SignalStore methods and computed signals?](#q45) <span class="intermediate">Intermediate</span>
46. [What are the best practices for structuring enterprise NgRx codebases?](#q46) <span class="advanced">Advanced</span>
47. [How do you handle error states with retry logic in NgRx Effects?](#q47) <span class="intermediate">Intermediate</span>
48. [What is the difference between `provideState` and `StoreModule.forFeature` in Angular 15+?](#q48) <span class="beginner">Beginner</span>
49. [How do you implement debounce filtering with NgRx SignalStore?](#q49) <span class="intermediate">Intermediate</span>
50. [What is the difference between `selectEntities` and `selectAll` in NgRx Entity?](#q50) <span class="beginner">Beginner</span>
51. [How do you handle cross-tab logout synchronization with NgRx?](#q51) <span class="advanced">Advanced</span>
52. [What is the purpose of `withHooks` in NgRx SignalStore (`onInit`, `onDestroy`)?](#q52) <span class="intermediate">Intermediate</span>
53. [How do you manage modal dialog state with NgRx Store vs local ComponentStore?](#q53) <span class="intermediate">Intermediate</span>
54. [What is the difference between `patchState` and updating state manually in SignalStore?](#q54) <span class="beginner">Beginner</span>
55. [How do you test NgRx SignalStore computed values with mock state?](#q55) <span class="intermediate">Intermediate</span>
56. [What is the purpose of `StoreConfig` in NgRx Store configuration?](#q56) <span class="intermediate">Intermediate</span>
57. [How do you implement pagination cursor fetching in NgRx?](#q57) <span class="intermediate">Intermediate</span>
58. [What is the difference between `createReducerFactory` and standard `createReducer`?](#q58) <span class="advanced">Advanced</span>
59. [How do you cancel long-polling requests in NgRx Effects?](#q59) <span class="intermediate">Intermediate</span>
60. [What is the purpose of `ngrx-forms` library?](#q60) <span class="intermediate">Intermediate</span>
61. [How do you implement multi-tenant state isolation in NgRx?](#q61) <span class="advanced">Advanced</span>
62. [What is the difference between `selectSignal` and subscribing to `select` observable in template?](#q62) <span class="beginner">Beginner</span>
63. [How do you handle offline sync queue with NgRx and IndexedDB?](#q63) <span class="advanced">Advanced</span>
64. [What is the difference between `@ngrx/effects` and Angular service methods?](#q64) <span class="intermediate">Intermediate</span>
65. [How do you profile NgRx state transitions in Chrome DevTools performance tab?](#q65) <span class="advanced">Advanced</span>
66. [What is the purpose of `deepComputed` in NgRx SignalStore?](#q66) <span class="advanced">Advanced</span>
67. [How do you test Effect error handling streams with marble testing?](#q67) <span class="advanced">Advanced</span>
68. [What is the difference between `ngrxOnInitEffects` and effect constructor dispatch?](#q68) <span class="intermediate">Intermediate</span>
69. [How do you handle router query params synchronization with NgRx store selectors?](#q69) <span class="intermediate">Intermediate</span>
70. [What is the purpose of `strictActionSerializability` check in NgRx?](#q70) <span class="intermediate">Intermediate</span>
71. [How do you build a shopping cart with NgRx Entity Adapter?](#q71) <span class="intermediate">Intermediate</span>
72. [What is the difference between `select` operator in RxJS and `Store.select()`?](#q72) <span class="beginner">Beginner</span>
73. [How do you implement batch action dispatching with NgRx?](#q73) <span class="intermediate">Intermediate</span>
74. [What is the purpose of `withEntities` in NgRx Signals?](#q74) <span class="advanced">Advanced</span>
75. [How do you handle server-sent events (SSE) with NgRx Effects?](#q75) <span class="advanced">Advanced</span>
76. [What is the difference between `@ngrx/component` (`*ngrxLet`, `ngrxPush`) and standard Angular pipes?](#q76) <span class="intermediate">Intermediate</span>
77. [How do you test ComponentStore `updater` methods with unit tests?](#q77) <span class="beginner">Beginner</span>
78. [What is the purpose of `provideStoreDevtools` in standalone Angular?](#q78) <span class="beginner">Beginner</span>
79. [How do you implement optimistic deletes with undo toast in NgRx?](#q79) <span class="advanced">Advanced</span>
80. [What is the difference between `createEffect` and creating an observable property in service?](#q80) <span class="intermediate">Intermediate</span>
81. [How do you configure strict state serializability in NgRx?](#q81) <span class="intermediate">Intermediate</span>
82. [What is the purpose of `resettable` meta-reducer in NgRx for user logout?](#q82) <span class="intermediate">Intermediate</span>
83. [How do you handle multi-step form validation state in NgRx?](#q83) <span class="intermediate">Intermediate</span>
84. [What is the difference between NgRx SignalStore and custom Signal Service?](#q84) <span class="intermediate">Intermediate</span>
85. [How do you build accessible data table filters with NgRx selectors?](#q85) <span class="intermediate">Intermediate</span>
86. [What is the purpose of `USER_PROVIDED_EFFECTS` token?](#q86) <span class="advanced">Advanced</span>
87. [How do you manage WebSocket connection lifecycle in NgRx Effects?](#q87) <span class="advanced">Advanced</span>
88. [What is the difference between `createFeatureSelector` and `createSelector`?](#q88) <span class="beginner">Beginner</span>
89. [How do you mock Store in Angular component unit tests with `provideMockStore`?](#q89) <span class="intermediate">Intermediate</span>
90. [What is the purpose of `withMethods` in SignalStore?](#q90) <span class="intermediate">Intermediate</span>
91. [How do you handle infinite scrolling data append with NgRx Entity?](#q91) <span class="intermediate">Intermediate</span>
92. [What is the difference between `exhaustMap` and `switchMap` in login buttons?](#q92) <span class="beginner">Beginner</span>
93. [How do you implement dark mode theme state with NgRx Store and localStorage?](#q93) <span class="beginner">Beginner</span>
94. [What is the purpose of `selectRouteParams` from `@ngrx/router-store`?](#q94) <span class="intermediate">Intermediate</span>
95. [How do you implement auto-refresh polling with NgRx Effects?](#q95) <span class="intermediate">Intermediate</span>
96. [What is the difference between `EntityAdapter.selectId` and `sortComparer`?](#q96) <span class="intermediate">Intermediate</span>
97. [How do you test ComponentStore `effect` methods?](#q97) <span class="intermediate">Intermediate</span>
98. [What is the purpose of `withComputed` in NgRx SignalStore?](#q98) <span class="intermediate">Intermediate</span>
99. [How do you prevent state pollution between unit tests in NgRx?](#q99) <span class="intermediate">Intermediate</span>
100. [What is the difference between `Action` interface and `createAction` creator?](#q100) <span class="beginner">Beginner</span>

---

<a id="q1"></a>
### Q1: Explain the Core Redux Architecture in NgRx (Store, Actions, Reducers, Selectors, Effects)?

**Difficulty**: Intermediate

**Strategy**:
NgRx implements the Redux pattern for Angular:
1. **Actions**: Plain objects with a unique `type` describing events.
2. **Reducers**: Pure functions that take current state and action, producing the new immutable state.
3. **Selectors**: Pure functions using `createSelector` with memoization to slice and transform store state.
4. **Effects**: RxJS-based side-effect managers that isolate asynchronous operations (HTTP calls, storage) from components.
5. **Store**: Single-source-of-truth reactive state accessible as an Observable.

**Code Example**:
```typescript
// 1. Action
export const loadUsers = createAction('[User List] Load Users');
export const loadUsersSuccess = createAction('[User API] Load Users Success', props<{ users: User[] }>());

// 2. Reducer
export const userReducer = createReducer(
  initialState,
  on(loadUsersSuccess, (state, { users }) => ({ ...state, users, loading: false }))
);

// 3. Selector
export const selectUserState = createFeatureSelector<UserState>('users');
export const selectAllUsers = createSelector(selectUserState, (state) => state.users);
```

---

<a id="q2"></a>
### Q2: What is NgRx SignalStore (introduced in NgRx 17+) and how does it revolutionize state management?

**Difficulty**: Advanced

**Strategy**:
`@ngrx/signals` SignalStore is a standalone, lightweight, signal-based reactive state management solution that eliminates RxJS boilerplate for component and feature state. It features a composable architecture using signal store features (`withState`, `withComputed`, `withMethods`, `withHooks`, `withEntities`).

**Code Example**:
```typescript
import { signalStore, withState, withComputed, withMethods, patchState } from '@ngrx/signals';
import { computed, inject } from '@angular/core';
import { UserService } from './user.service';

export const UserStore = signalStore(
  { providedIn: 'root' },
  withState({ users: [] as User[], loading: false }),
  withComputed(({ users }) => ({
    userCount: computed(() => users().length),
  })),
  withMethods((store, userService = inject(UserService)) => ({
    async loadAll() {
      patchState(store, { loading: true });
      const users = await userService.getAll();
      patchState(store, { users, loading: false });
    }
  }))
);
```

---

<a id="q3"></a>
### Q3: How do NgRx Effects handle concurrency and cancellation with RxJS flattening operators (`switchMap`, `exhaustMap`, `concatMap`, `mergeMap`)?

**Difficulty**: Advanced

**Strategy**:
Choosing the right operator in Effects is critical to prevent data corruption:
- `switchMap`: Cancels pending HTTP request when a new action arrives (ideal for search inputs).
- `exhaustMap`: Ignores new actions until the current async request finishes (ideal for non-duplicate Login submissions).
- `concatMap`: Queues requests in strict FIFO order (ideal for sequential DB updates).
- `mergeMap`: Executes all requests concurrently without cancellation or queuing (ideal for parallel file uploads).

**Code Example**:
```typescript
import { Injectable, inject } from '@angular/core';
import { Actions, createEffect, ofType } from '@ngrx/effects';
import { exhaustMap, map, catchError, of } from 'rxjs';
import * as AuthActions from './auth.actions';
import { AuthService } from './auth.service';

@Injectable()
export class AuthEffects {
  private actions$ = inject(Actions);
  private auth = inject(AuthService);

  login$ = createEffect(() =>
    this.actions$.pipe(
      ofType(AuthActions.login),
      exhaustMap(action =>
        this.auth.login(action.credentials).pipe(
          map(user => AuthActions.loginSuccess({ user })),
          catchError(error => of(AuthActions.loginFailure({ error })))
        )
      )
    )
  );
}
```

---

<a id="q4"></a>
### Q4: How does NgRx Entity Adapter (`@ngrx/entity`) manage normalized entity collections?

**Difficulty**: Intermediate

**Strategy**:
`@ngrx/entity` provides pre-built reducer methods and selectors for normalized collections (`{ ids: string[], entities: Record<string, T> }`), achieving O(1) lookups by ID and providing standardized CRUD operations (`addOne`, `setAll`, `updateOne`, `removeOne`).

**Code Example**:
```typescript
import { createEntityAdapter, EntityState } from '@ngrx/entity';

export interface Product { id: string; name: string; price: number; }
export interface ProductState extends EntityState<Product> { selectedId: string | null; }

export const adapter = createEntityAdapter<Product>();
export const initialProductState: ProductState = adapter.getInitialState({ selectedId: null });

export const productReducer = createReducer(
  initialProductState,
  on(ProductActions.setProducts, (state, { products }) => adapter.setAll(products, state)),
  on(ProductActions.updateProduct, (state, { update }) => adapter.updateOne(update, state))
);

export const { selectAll, selectEntities, selectIds, selectTotal } = adapter.getSelectors();
```

---

<a id="q5"></a>
### Q5: What is NgRx ComponentStore and when should you use it over global Store?

**Difficulty**: Intermediate

**Strategy**:
`@ngrx/componentstore` is a standalone, service-based state management solution designed for local or feature-level state tied to a component's lifecycle. Unlike global NgRx Store, ComponentStore is destroyed when the host component unmounts, preventing memory leaks.

**Code Example**:
```typescript
import { Injectable } from '@angular/core';
import { ComponentStore } from '@ngrx/component-store';
import { Observable, switchMap, tap } from 'rxjs';

interface FilterState { query: string; category: string; }

@Injectable()
export class FilterStore extends ComponentStore<FilterState> {
  constructor() { super({ query: '', category: 'all' }); }

  readonly query$ = this.select(state => state.query);
  readonly setQuery = this.updater((state, query: string) => ({ ...state, query }));
}
```

---

<a id="q6"></a>
### Q6: How do memoized selectors created with `createSelector` optimize Angular rendering?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of How do memoized selectors created with `createSelector` optimize Angular rendering?. Memoized selectors only re-evaluate when their input selector slices emit new reference values, preventing redundant calculation overhead. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do memoized selectors created with `createSelector` optimize Angular rendering?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q7"></a>
### Q7: What is `createActionGroup` in NgRx 15+ and how does it reduce action boilerplate?

**Difficulty**: Beginner

**Strategy**:
Comprehensive explanation of What is `createActionGroup` in NgRx 15+ and how does it reduce action boilerplate?. Groups related actions for a single source (e.g. `User API`) into a concise, unified declaration. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is `createActionGroup` in NgRx 15+ and how does it reduce action boilerplate?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q8"></a>
### Q8: How does `@ngrx/router-store` integrate Angular Router navigation with NgRx state?

**Difficulty**: Advanced

**Strategy**:
Comprehensive explanation of How does `@ngrx/router-store` integrate Angular Router navigation with NgRx state?. Dispatches actions on router navigation (`ROUTER_NAVIGATION`, `ROUTER_CANCELLED`), allowing time-travel debugging of URL changes. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How does `@ngrx/router-store` integrate Angular Router navigation with NgRx state?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q9"></a>
### Q9: How do you test NgRx Reducers with unit tests?

**Difficulty**: Beginner

**Strategy**:
Comprehensive explanation of How do you test NgRx Reducers with unit tests?. Call the reducer function directly with initial state and action, asserting the returned state immutably matches expectation. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you test NgRx Reducers with unit tests?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q10"></a>
### Q10: How do you test NgRx Effects with `provideMockActions` in Jasmine/Vitest?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of How do you test NgRx Effects with `provideMockActions` in Jasmine/Vitest?. Supply a mock actions ReplaySubject to simulate action emissions and assert effect stream outputs. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you test NgRx Effects with `provideMockActions` in Jasmine/Vitest?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q11"></a>
### Q11: What is `MetaReducer` in NgRx and how do you implement a logger or state hydration meta-reducer?

**Difficulty**: Advanced

**Strategy**:
Comprehensive explanation of What is `MetaReducer` in NgRx and how do you implement a logger or state hydration meta-reducer?. Higher-order reducer that wraps the root reducer to intercept all actions and state transitions globally. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is `MetaReducer` in NgRx and how do you implement a logger or state hydration meta-reducer?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q12"></a>
### Q12: How do you handle pagination with NgRx Entity Adapter?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of How do you handle pagination with NgRx Entity Adapter?. Track `pageIndex`, `pageSize`, and `totalCount` in feature state alongside normalized entity dictionary. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you handle pagination with NgRx Entity Adapter?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q13"></a>
### Q13: What are Action Sanitizers and State Sanitizers in `@ngrx/store-devtools`?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of What are Action Sanitizers and State Sanitizers in `@ngrx/store-devtools`?. Sanitizes sensitive data (passwords, tokens) before sending state snapshots to Redux DevTools extension. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What are Action Sanitizers and State Sanitizers in `@ngrx/store-devtools`?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q14"></a>
### Q14: How do you use `provideStore` and `provideEffects` in standalone Angular applications?

**Difficulty**: Beginner

**Strategy**:
Comprehensive explanation of How do you use `provideStore` and `provideEffects` in standalone Angular applications?. Registers NgRx root store and effects directly in `ApplicationConfig.providers`. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you use `provideStore` and `provideEffects` in standalone Angular applications?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q15"></a>
### Q15: What is the difference between `Store.select()` and `Store.selectSignal()` in NgRx 16+?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of What is the difference between `Store.select()` and `Store.selectSignal()` in NgRx 16+?. `select()` returns an RxJS Observable; `selectSignal()` returns an Angular Signal directly. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is the difference between `Store.select()` and `Store.selectSignal()` in NgRx 16+?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q16"></a>
### Q16: How do you implement Optimistic Updates in NgRx Effects?

**Difficulty**: Advanced

**Strategy**:
Comprehensive explanation of How do you implement Optimistic Updates in NgRx Effects?. Dispatch success/update action immediately in component or effect, and dispatch revert action on HTTP catchError. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you implement Optimistic Updates in NgRx Effects?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q17"></a>
### Q17: What is the purpose of `ofType` operator in NgRx Effects?

**Difficulty**: Beginner

**Strategy**:
Comprehensive explanation of What is the purpose of `ofType` operator in NgRx Effects?. Filters the actions stream to only pass actions matching the specified action creators. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is the purpose of `ofType` operator in NgRx Effects?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q18"></a>
### Q18: How do you handle WebSocket streaming data in NgRx Effects?

**Difficulty**: Advanced

**Strategy**:
Comprehensive explanation of How do you handle WebSocket streaming data in NgRx Effects?. Use an effect that subscribes to a WebSocket service stream and dispatches update actions on incoming messages. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you handle WebSocket streaming data in NgRx Effects?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q19"></a>
### Q19: What is the difference between `defaultRouterState` and `customRouterStateSerializer` in `@ngrx/router-store`?

**Difficulty**: Advanced

**Strategy**:
Comprehensive explanation of What is the difference between `defaultRouterState` and `customRouterStateSerializer` in `@ngrx/router-store`?. Custom serializer extracts only minimal route params, queryParams, and data to prevent serializing circular router objects. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is the difference between `defaultRouterState` and `customRouterStateSerializer` in `@ngrx/router-store`?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q20"></a>
### Q20: How do you handle multi-action dispatching from a single NgRx Effect?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of How do you handle multi-action dispatching from a single NgRx Effect?. Use `concatMap` returning `of(actionA, actionB)` inside the effect pipeline. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you handle multi-action dispatching from a single NgRx Effect?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q21"></a>
### Q21: What is `@ngrx/schematics` and how does it automate NgRx boilerplate generation?

**Difficulty**: Beginner

**Strategy**:
Comprehensive explanation of What is `@ngrx/schematics` and how does it automate NgRx boilerplate generation?. Angular CLI schematics to generate actions, reducers, effects, and selectors with best practices (`ng g @ngrx/schematics:store`). Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is `@ngrx/schematics` and how does it automate NgRx boilerplate generation?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q22"></a>
### Q22: How do you prevent cyclic dependency issues in NgRx selectors?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of How do you prevent cyclic dependency issues in NgRx selectors?. Organize selectors strictly by feature domains and avoid importing parent selectors into child feature modules. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you prevent cyclic dependency issues in NgRx selectors?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q23"></a>
### Q23: What is the purpose of `StoreDevtoolsModule.instrument()`?

**Difficulty**: Beginner

**Strategy**:
Comprehensive explanation of What is the purpose of `StoreDevtoolsModule.instrument()`?. Connects Angular application state to the Redux DevTools Chrome/Firefox browser extension. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is the purpose of `StoreDevtoolsModule.instrument()`?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q24"></a>
### Q24: How do you handle JWT Token Refresh in NgRx Effects?

**Difficulty**: Advanced

**Strategy**:
Comprehensive explanation of How do you handle JWT Token Refresh in NgRx Effects?. Catch 401 errors in effect, dispatch `refreshToken` action, pause original request stream with switchMap, and retry on token success. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you handle JWT Token Refresh in NgRx Effects?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q25"></a>
### Q25: What are Non-Dispatching Effects (`dispatch: false`) and when should you use them?

**Difficulty**: Beginner

**Strategy**:
Comprehensive explanation of What are Non-Dispatching Effects (`dispatch: false`) and when should you use them?. Used for analytics tracking, external navigation (`router.navigate`), or notifications where no new action is emitted. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What are Non-Dispatching Effects (`dispatch: false`) and when should you use them?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q26"></a>
### Q26: How do you manage complex wizard multi-step state with NgRx?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of How do you manage complex wizard multi-step state with NgRx?. Maintain step index, form slice data, and validation flags in a dedicated feature store slice. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you manage complex wizard multi-step state with NgRx?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q27"></a>
### Q27: What is the difference between `@ngrx/signals` and `@ngrx/store`?

**Difficulty**: Advanced

**Strategy**:
Comprehensive explanation of What is the difference between `@ngrx/signals` and `@ngrx/store`?. SignalStore is lightweight, signal-native, and zero-boilerplate; NgRx Store is centralized, global, and RxJS Observable-driven. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is the difference between `@ngrx/signals` and `@ngrx/store`?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q28"></a>
### Q28: How do you test NgRx Selectors with `projector` functions?

**Difficulty**: Beginner

**Strategy**:
Comprehensive explanation of How do you test NgRx Selectors with `projector` functions?. Selectors expose a `.projector` function that can be tested directly with mock slice arguments without instantiating the entire Store. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you test NgRx Selectors with `projector` functions?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q29"></a>
### Q29: How do you implement local storage persistence with NgRx Meta-Reducers?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of How do you implement local storage persistence with NgRx Meta-Reducers?. Wrap root reducer with meta-reducer that saves state to `localStorage` on action changes and initializes state on boot. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you implement local storage persistence with NgRx Meta-Reducers?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q30"></a>
### Q30: What is `createFeature` in NgRx 14+ and how does it generate automatic selectors?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of What is `createFeature` in NgRx 14+ and how does it generate automatic selectors?. Automatically generates named selectors (`selectUserState`, `selectUsers`, `selectLoading`) based on reducer state properties. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is `createFeature` in NgRx 14+ and how does it generate automatic selectors?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q31"></a>
### Q31: How do you handle file uploads with progress in NgRx?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of How do you handle file uploads with progress in NgRx?. HttpClient returns `HttpEventType.UploadProgress` events mapped to progress action dispatches. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you handle file uploads with progress in NgRx?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q32"></a>
### Q32: What is the difference between `props<{}>()` and `emptyProps()` in NgRx actions?

**Difficulty**: Beginner

**Strategy**:
Comprehensive explanation of What is the difference between `props<{}>()` and `emptyProps()` in NgRx actions?. `props<Payload>()` defines structured action payload; `emptyProps()` defines actions without payloads. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is the difference between `props<{}>()` and `emptyProps()` in NgRx actions?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q33"></a>
### Q33: How do you handle race conditions in NgRx with `switchMap` in Effects?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of How do you handle race conditions in NgRx with `switchMap` in Effects?. Automatic cancellation of previous in-flight HTTP requests when new action is dispatched. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you handle race conditions in NgRx with `switchMap` in Effects?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q34"></a>
### Q34: What is the purpose of `USER_PROVIDED_META_REDUCERS` injection token?

**Difficulty**: Advanced

**Strategy**:
Comprehensive explanation of What is the purpose of `USER_PROVIDED_META_REDUCERS` injection token?. Allows injecting dynamic meta-reducers at runtime via Angular DI. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is the purpose of `USER_PROVIDED_META_REDUCERS` injection token?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q35"></a>
### Q35: How do you manage Undo/Redo actions in NgRx?

**Difficulty**: Advanced

**Strategy**:
Comprehensive explanation of How do you manage Undo/Redo actions in NgRx?. Implement a meta-reducer that maintains past and future state snapshot arrays. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you manage Undo/Redo actions in NgRx?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q36"></a>
### Q36: What is the difference between `withEntities` in SignalStore vs `@ngrx/entity`?

**Difficulty**: Advanced

**Strategy**:
Comprehensive explanation of What is the difference between `withEntities` in SignalStore vs `@ngrx/entity`?. SignalStore `withEntities` manages entities as Angular Signals with built-in signal entity selectors. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is the difference between `withEntities` in SignalStore vs `@ngrx/entity`?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q37"></a>
### Q37: How do you handle cross-feature selector composition in NgRx?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of How do you handle cross-feature selector composition in NgRx?. Combine feature selectors using `createSelector(selectCart, selectUser, (cart, user) => ...)`. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you handle cross-feature selector composition in NgRx?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q38"></a>
### Q38: What is the purpose of `ROOT_REDUCERS` and `FEATURE_REDUCERS` injection tokens?

**Difficulty**: Advanced

**Strategy**:
Comprehensive explanation of What is the purpose of `ROOT_REDUCERS` and `FEATURE_REDUCERS` injection tokens?. Allows lazy-loading and dynamic registration of reducer maps. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is the purpose of `ROOT_REDUCERS` and `FEATURE_REDUCERS` injection tokens?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q39"></a>
### Q39: How do you implement Auto-Save form fields with NgRx ComponentStore?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of How do you implement Auto-Save form fields with NgRx ComponentStore?. Use `this.effect` with `debounceTime(500)` and `switchMap` triggering save API. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you implement Auto-Save form fields with NgRx ComponentStore?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q40"></a>
### Q40: What is the difference between `createAction` and legacy Action class implementations?

**Difficulty**: Beginner

**Strategy**:
Comprehensive explanation of What is the difference between `createAction` and legacy Action class implementations?. `createAction` is type-safe and eliminates string constant action type boilerplate. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is the difference between `createAction` and legacy Action class implementations?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q41"></a>
### Q41: How do you handle polling endpoints in NgRx Effects?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of How do you handle polling endpoints in NgRx Effects?. Use `timer(0, 5000)` inside effect piped to HTTP request with `takeUntil` cancel action. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you handle polling endpoints in NgRx Effects?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q42"></a>
### Q42: What is the purpose of `ngrxOnStoreInit` and `ngrxOnInitEffects` lifecycle hooks?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of What is the purpose of `ngrxOnStoreInit` and `ngrxOnInitEffects` lifecycle hooks?. Executes initialization actions when feature stores or effects are lazily registered. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is the purpose of `ngrxOnStoreInit` and `ngrxOnInitEffects` lifecycle hooks?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q43"></a>
### Q43: How do you configure strict runtime immutability checks in NgRx?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of How do you configure strict runtime immutability checks in NgRx?. Enable `strictStateImmutability` and `strictActionImmutability` to catch accidental state mutations in development. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you configure strict runtime immutability checks in NgRx?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q44"></a>
### Q44: What is the difference between `ActionGroup` events vs commands in NgRx naming conventions?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of What is the difference between `ActionGroup` events vs commands in NgRx naming conventions?. Events describe what happened (`[User Page] User Clicked Save`); commands describe intent (`[User API] Save User`). Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is the difference between `ActionGroup` events vs commands in NgRx naming conventions?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q45"></a>
### Q45: How do you test SignalStore methods and computed signals?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of How do you test SignalStore methods and computed signals?. Instantiate the SignalStore in TestBed and assert signal values and async method outcomes. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you test SignalStore methods and computed signals?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q46"></a>
### Q46: What are the best practices for structuring enterprise NgRx codebases?

**Difficulty**: Advanced

**Strategy**:
Comprehensive explanation of What are the best practices for structuring enterprise NgRx codebases?. Feature-driven state organization, normalized entity dictionaries, strict immutability checks, and clean separation between smart components and dumb UI presentations. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What are the best practices for structuring enterprise NgRx codebases?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q47"></a>
### Q47: How do you handle error states with retry logic in NgRx Effects?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of How do you handle error states with retry logic in NgRx Effects?. Use RxJS `retry({ count: 3, delay: 1000 })` before the `catchError` block inside effects. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you handle error states with retry logic in NgRx Effects?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q48"></a>
### Q48: What is the difference between `provideState` and `StoreModule.forFeature` in Angular 15+?

**Difficulty**: Beginner

**Strategy**:
Comprehensive explanation of What is the difference between `provideState` and `StoreModule.forFeature` in Angular 15+?. `provideState` is the standalone API alternative to `StoreModule.forFeature`. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is the difference between `provideState` and `StoreModule.forFeature` in Angular 15+?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q49"></a>
### Q49: How do you implement debounce filtering with NgRx SignalStore?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of How do you implement debounce filtering with NgRx SignalStore?. Combine `rxMethod` with `debounceTime(300)` and `distinctUntilChanged()`. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you implement debounce filtering with NgRx SignalStore?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q50"></a>
### Q50: What is the difference between `selectEntities` and `selectAll` in NgRx Entity?

**Difficulty**: Beginner

**Strategy**:
Comprehensive explanation of What is the difference between `selectEntities` and `selectAll` in NgRx Entity?. `selectEntities` returns dictionary mapping ID to entity; `selectAll` returns flat array of all entities. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is the difference between `selectEntities` and `selectAll` in NgRx Entity?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q51"></a>
### Q51: How do you handle cross-tab logout synchronization with NgRx?

**Difficulty**: Advanced

**Strategy**:
Comprehensive explanation of How do you handle cross-tab logout synchronization with NgRx?. Meta-reducer listens to `storage` events and dispatches global logout action. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you handle cross-tab logout synchronization with NgRx?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q52"></a>
### Q52: What is the purpose of `withHooks` in NgRx SignalStore (`onInit`, `onDestroy`)?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of What is the purpose of `withHooks` in NgRx SignalStore (`onInit`, `onDestroy`)?. Executes initialization logic (like loading data) and cleanup when the store is instantiated and destroyed. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is the purpose of `withHooks` in NgRx SignalStore (`onInit`, `onDestroy`)?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q53"></a>
### Q53: How do you manage modal dialog state with NgRx Store vs local ComponentStore?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of How do you manage modal dialog state with NgRx Store vs local ComponentStore?. Global app-wide modals use global store; single-view dialogs use local ComponentStore. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you manage modal dialog state with NgRx Store vs local ComponentStore?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q54"></a>
### Q54: What is the difference between `patchState` and updating state manually in SignalStore?

**Difficulty**: Beginner

**Strategy**:
Comprehensive explanation of What is the difference between `patchState` and updating state manually in SignalStore?. `patchState` performs type-safe shallow merges on signal store state slices. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is the difference between `patchState` and updating state manually in SignalStore?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q55"></a>
### Q55: How do you test NgRx SignalStore computed values with mock state?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of How do you test NgRx SignalStore computed values with mock state?. Instantiate store with initial state and assert computed signal values. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you test NgRx SignalStore computed values with mock state?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q56"></a>
### Q56: What is the purpose of `StoreConfig` in NgRx Store configuration?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of What is the purpose of `StoreConfig` in NgRx Store configuration?. Configures runtime checks, initial state, and meta-reducers. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is the purpose of `StoreConfig` in NgRx Store configuration?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q57"></a>
### Q57: How do you implement pagination cursor fetching in NgRx?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of How do you implement pagination cursor fetching in NgRx?. Store `nextCursor` token in state and pass it to subsequent API action payloads. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you implement pagination cursor fetching in NgRx?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q58"></a>
### Q58: What is the difference between `createReducerFactory` and standard `createReducer`?

**Difficulty**: Advanced

**Strategy**:
Comprehensive explanation of What is the difference between `createReducerFactory` and standard `createReducer`?. Allows customizing reducer creation behavior across feature slices. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is the difference between `createReducerFactory` and standard `createReducer`?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q59"></a>
### Q59: How do you cancel long-polling requests in NgRx Effects?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of How do you cancel long-polling requests in NgRx Effects?. Use `takeUntil` listening for route change or explicit cancel action. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you cancel long-polling requests in NgRx Effects?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q60"></a>
### Q60: What is the purpose of `ngrx-forms` library?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of What is the purpose of `ngrx-forms` library?. Integrates Angular form state directly into NgRx store for centralized validation and undo history. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is the purpose of `ngrx-forms` library?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q61"></a>
### Q61: How do you implement multi-tenant state isolation in NgRx?

**Difficulty**: Advanced

**Strategy**:
Comprehensive explanation of How do you implement multi-tenant state isolation in NgRx?. Scope entity adapters with tenantId prefix or dynamic feature keys. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you implement multi-tenant state isolation in NgRx?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q62"></a>
### Q62: What is the difference between `selectSignal` and subscribing to `select` observable in template?

**Difficulty**: Beginner

**Strategy**:
Comprehensive explanation of What is the difference between `selectSignal` and subscribing to `select` observable in template?. `selectSignal` integrates natively with Angular change detection without `async` pipe. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is the difference between `selectSignal` and subscribing to `select` observable in template?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q63"></a>
### Q63: How do you handle offline sync queue with NgRx and IndexedDB?

**Difficulty**: Advanced

**Strategy**:
Comprehensive explanation of How do you handle offline sync queue with NgRx and IndexedDB?. Meta-reducer buffers mutating actions when offline and replays them when `online` event triggers. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you handle offline sync queue with NgRx and IndexedDB?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q64"></a>
### Q64: What is the difference between `@ngrx/effects` and Angular service methods?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of What is the difference between `@ngrx/effects` and Angular service methods?. Effects isolate side effects into declarative reactive streams, keeping components purely presentational. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is the difference between `@ngrx/effects` and Angular service methods?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q65"></a>
### Q65: How do you profile NgRx state transitions in Chrome DevTools performance tab?

**Difficulty**: Advanced

**Strategy**:
Comprehensive explanation of How do you profile NgRx state transitions in Chrome DevTools performance tab?. Enable `trackActionPerformance` to see time spent in reducers and effects. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you profile NgRx state transitions in Chrome DevTools performance tab?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q66"></a>
### Q66: What is the purpose of `deepComputed` in NgRx SignalStore?

**Difficulty**: Advanced

**Strategy**:
Comprehensive explanation of What is the purpose of `deepComputed` in NgRx SignalStore?. Creates nested computed signal proxies for fine-grained sub-property reactivity. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is the purpose of `deepComputed` in NgRx SignalStore?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q67"></a>
### Q67: How do you test Effect error handling streams with marble testing?

**Difficulty**: Advanced

**Strategy**:
Comprehensive explanation of How do you test Effect error handling streams with marble testing?. Use Jasmine marbles (`hot` and `cold` observables) to assert emissions and error completions. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you test Effect error handling streams with marble testing?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q68"></a>
### Q68: What is the difference between `ngrxOnInitEffects` and effect constructor dispatch?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of What is the difference between `ngrxOnInitEffects` and effect constructor dispatch?. `ngrxOnInitEffects` dispatches actions automatically after all effects are initialized. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is the difference between `ngrxOnInitEffects` and effect constructor dispatch?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q69"></a>
### Q69: How do you handle router query params synchronization with NgRx store selectors?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of How do you handle router query params synchronization with NgRx store selectors?. Use `getRouterSelectors()` from `@ngrx/router-store` to read route params directly in selectors. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you handle router query params synchronization with NgRx store selectors?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q70"></a>
### Q70: What is the purpose of `strictActionSerializability` check in NgRx?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of What is the purpose of `strictActionSerializability` check in NgRx?. Throws runtime error if non-serializable values (functions, promises, symbols) are passed in action payloads. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is the purpose of `strictActionSerializability` check in NgRx?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q71"></a>
### Q71: How do you build a shopping cart with NgRx Entity Adapter?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of How do you build a shopping cart with NgRx Entity Adapter?. Use `EntityState<CartItem>` with `addOne`, `updateOne`, and `removeOne` reducers and total price selector. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you build a shopping cart with NgRx Entity Adapter?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q72"></a>
### Q72: What is the difference between `select` operator in RxJS and `Store.select()`?

**Difficulty**: Beginner

**Strategy**:
Comprehensive explanation of What is the difference between `select` operator in RxJS and `Store.select()`?. `Store.select` applies automatic `distinctUntilChanged` memoization. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is the difference between `select` operator in RxJS and `Store.select()`?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q73"></a>
### Q73: How do you implement batch action dispatching with NgRx?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of How do you implement batch action dispatching with NgRx?. Create a batch action creator taking an array of actions and process them sequentially in a meta-reducer. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you implement batch action dispatching with NgRx?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q74"></a>
### Q74: What is the purpose of `withEntities` in NgRx Signals?

**Difficulty**: Advanced

**Strategy**:
Comprehensive explanation of What is the purpose of `withEntities` in NgRx Signals?. Adds normalized entity management methods (`addEntity`, `setAllEntities`) to SignalStore. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is the purpose of `withEntities` in NgRx Signals?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q75"></a>
### Q75: How do you handle server-sent events (SSE) with NgRx Effects?

**Difficulty**: Advanced

**Strategy**:
Comprehensive explanation of How do you handle server-sent events (SSE) with NgRx Effects?. Effect wraps `EventSource` and dispatches action for each event message emitted. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you handle server-sent events (SSE) with NgRx Effects?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q76"></a>
### Q76: What is the difference between `@ngrx/component` (`*ngrxLet`, `ngrxPush`) and standard Angular pipes?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of What is the difference between `@ngrx/component` (`*ngrxLet`, `ngrxPush`) and standard Angular pipes?. `*ngrxLet` and `ngrxPush` trigger CD concurrently and render without zone.js overhead. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is the difference between `@ngrx/component` (`*ngrxLet`, `ngrxPush`) and standard Angular pipes?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q77"></a>
### Q77: How do you test ComponentStore `updater` methods with unit tests?

**Difficulty**: Beginner

**Strategy**:
Comprehensive explanation of How do you test ComponentStore `updater` methods with unit tests?. Call updater method directly and assert state observable emission. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you test ComponentStore `updater` methods with unit tests?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q78"></a>
### Q78: What is the purpose of `provideStoreDevtools` in standalone Angular?

**Difficulty**: Beginner

**Strategy**:
Comprehensive explanation of What is the purpose of `provideStoreDevtools` in standalone Angular?. Standalone provider function to configure Redux DevTools extension. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is the purpose of `provideStoreDevtools` in standalone Angular?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q79"></a>
### Q79: How do you implement optimistic deletes with undo toast in NgRx?

**Difficulty**: Advanced

**Strategy**:
Comprehensive explanation of How do you implement optimistic deletes with undo toast in NgRx?. Remove entity from state immediately, show toast with 'Undo' button, and dispatch API call after 5-second delay if not cancelled. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you implement optimistic deletes with undo toast in NgRx?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q80"></a>
### Q80: What is the difference between `createEffect` and creating an observable property in service?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of What is the difference between `createEffect` and creating an observable property in service?. `createEffect` registers the effect with the NgRx lifecycle and handles error recovery. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is the difference between `createEffect` and creating an observable property in service?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q81"></a>
### Q81: How do you configure strict state serializability in NgRx?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of How do you configure strict state serializability in NgRx?. Enable `strictStateSerializability: true` to prevent storing class instances in state. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you configure strict state serializability in NgRx?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q82"></a>
### Q82: What is the purpose of `resettable` meta-reducer in NgRx for user logout?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of What is the purpose of `resettable` meta-reducer in NgRx for user logout?. Clears entire application store back to `initialState` when `logout` action is intercepted. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is the purpose of `resettable` meta-reducer in NgRx for user logout?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q83"></a>
### Q83: How do you handle multi-step form validation state in NgRx?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of How do you handle multi-step form validation state in NgRx?. Selector computes overall validity by combining slice validity flags. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you handle multi-step form validation state in NgRx?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q84"></a>
### Q84: What is the difference between NgRx SignalStore and custom Signal Service?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of What is the difference between NgRx SignalStore and custom Signal Service?. SignalStore provides standardized patterns (state, computed, methods, hooks, entities) and plugin ecosystem. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is the difference between NgRx SignalStore and custom Signal Service?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q85"></a>
### Q85: How do you build accessible data table filters with NgRx selectors?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of How do you build accessible data table filters with NgRx selectors?. Selectors filter and sort normalized entities in memory with O(1) efficiency. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you build accessible data table filters with NgRx selectors?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q86"></a>
### Q86: What is the purpose of `USER_PROVIDED_EFFECTS` token?

**Difficulty**: Advanced

**Strategy**:
Comprehensive explanation of What is the purpose of `USER_PROVIDED_EFFECTS` token?. Allows dynamic injection of effects via Angular DI. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is the purpose of `USER_PROVIDED_EFFECTS` token?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q87"></a>
### Q87: How do you manage WebSocket connection lifecycle in NgRx Effects?

**Difficulty**: Advanced

**Strategy**:
Comprehensive explanation of How do you manage WebSocket connection lifecycle in NgRx Effects?. Open connection on login action, dispatch actions on messages, and close socket on logout action. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you manage WebSocket connection lifecycle in NgRx Effects?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q88"></a>
### Q88: What is the difference between `createFeatureSelector` and `createSelector`?

**Difficulty**: Beginner

**Strategy**:
Comprehensive explanation of What is the difference between `createFeatureSelector` and `createSelector`?. `createFeatureSelector` selects top-level feature state slice; `createSelector` derives nested values. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is the difference between `createFeatureSelector` and `createSelector`?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q89"></a>
### Q89: How do you mock Store in Angular component unit tests with `provideMockStore`?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of How do you mock Store in Angular component unit tests with `provideMockStore`?. Use `provideMockStore({ initialState, selectors: [...] })`. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you mock Store in Angular component unit tests with `provideMockStore`?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q90"></a>
### Q90: What is the purpose of `withMethods` in SignalStore?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of What is the purpose of `withMethods` in SignalStore?. Defines methods that mutate state using `patchState` or call async services. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is the purpose of `withMethods` in SignalStore?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q91"></a>
### Q91: How do you handle infinite scrolling data append with NgRx Entity?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of How do you handle infinite scrolling data append with NgRx Entity?. Use `adapter.addMany(newItems, state)` to append items without duplicates. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you handle infinite scrolling data append with NgRx Entity?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q92"></a>
### Q92: What is the difference between `exhaustMap` and `switchMap` in login buttons?

**Difficulty**: Beginner

**Strategy**:
Comprehensive explanation of What is the difference between `exhaustMap` and `switchMap` in login buttons?. `exhaustMap` prevents duplicate submits while pending; `switchMap` would cancel and restart request. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is the difference between `exhaustMap` and `switchMap` in login buttons?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q93"></a>
### Q93: How do you implement dark mode theme state with NgRx Store and localStorage?

**Difficulty**: Beginner

**Strategy**:
Comprehensive explanation of How do you implement dark mode theme state with NgRx Store and localStorage?. Store theme state and persist via meta-reducer or effect syncing `document.body` class. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you implement dark mode theme state with NgRx Store and localStorage?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q94"></a>
### Q94: What is the purpose of `selectRouteParams` from `@ngrx/router-store`?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of What is the purpose of `selectRouteParams` from `@ngrx/router-store`?. Selector returning route parameters directly from current router state. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is the purpose of `selectRouteParams` from `@ngrx/router-store`?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q95"></a>
### Q95: How do you implement auto-refresh polling with NgRx Effects?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of How do you implement auto-refresh polling with NgRx Effects?. Effect uses `timer(0, 30000)` piped to API request with takeUntil cancellation. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you implement auto-refresh polling with NgRx Effects?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q96"></a>
### Q96: What is the difference between `EntityAdapter.selectId` and `sortComparer`?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of What is the difference between `EntityAdapter.selectId` and `sortComparer`?. `selectId` specifies unique key property; `sortComparer` maintains sorted order in `ids` array. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is the difference between `EntityAdapter.selectId` and `sortComparer`?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q97"></a>
### Q97: How do you test ComponentStore `effect` methods?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of How do you test ComponentStore `effect` methods?. Trigger effect method with test value and assert expected service call or state change. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you test ComponentStore `effect` methods?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q98"></a>
### Q98: What is the purpose of `withComputed` in NgRx SignalStore?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of What is the purpose of `withComputed` in NgRx SignalStore?. Derives reactive computed signals based on store state slices with automatic memoization. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is the purpose of `withComputed` in NgRx SignalStore?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q99"></a>
### Q99: How do you prevent state pollution between unit tests in NgRx?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive explanation of How do you prevent state pollution between unit tests in NgRx?. Always provide fresh initial state or use `mockStore.resetSelectors()` before each test spec. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for How do you prevent state pollution between unit tests in NgRx?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---

<a id="q100"></a>
### Q100: What is the difference between `Action` interface and `createAction` creator?

**Difficulty**: Beginner

**Strategy**:
Comprehensive explanation of What is the difference between `Action` interface and `createAction` creator?. `Action` interface requires manual `type` string; `createAction` returns typed callable creator function. Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.

**Code Example**:
```typescript
// Implementation for What is the difference between `Action` interface and `createAction` creator?
import { createAction, createReducer, on } from '@ngrx/store';

export const exampleAction = createAction('[Example] Action');
export const exampleReducer = createReducer({}, on(exampleAction, state => ({ ...state })));
```

---
