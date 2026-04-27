<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>NgRx Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for developers</b></p>
</div>

---

## Table of Contents

1. [What is the difference between NgRx Global Store and NgRx ComponentStore?](#q1-what-is-the-difference-between-ngrx-global-store-and-ngrx-componentstore) <span class="beginner">Beginner</span>
2. [How do you prevent selector re-computation when using arguments (props)?](#q2-how-do-you-prevent-selector-re-computation-when-using-arguments-props) <span class="advanced">Advanced</span>
3. [How do you manage local component state using NgRx ComponentStore?](#q3-how-do-you-manage-local-component-state-using-ngrx-componentstore) <span class="intermediate">Intermediate</span>
4. [How do you implement the Facade pattern with NgRx to hide store complexity?](#q4-how-do-you-implement-the-facade-pattern-with-ngrx-to-hide-store-complexity) <span class="intermediate">Intermediate</span>
5. [How do you handle race conditions in NgRx Effects (e.g., typeahead search)?](#q5-how-do-you-handle-race-conditions-in-ngrx-effects-e.g.-typeahead-search) <span class="intermediate">Intermediate</span>
6. [How do you normalize deeply nested API data using NgRx Entity?](#q6-how-do-you-normalize-deeply-nested-api-data-using-ngrx-entity) <span class="advanced">Advanced</span>
7. [How do you implement runtime checks to ensure state immutability?](#q7-how-do-you-implement-runtime-checks-to-ensure-state-immutability) <span class="intermediate">Intermediate</span>
8. [How do you handle multiple actions triggering the same reducer logic?](#q8-how-do-you-handle-multiple-actions-triggering-the-same-reducer-logic) <span class="beginner">Beginner</span>
9. [How do you hydrate NgRx state from LocalStorage on app startup?](#q9-how-do-you-hydrate-ngrx-state-from-localstorage-on-app-startup) <span class="advanced">Advanced</span>
10. [How do you implement undo/redo functionality with NgRx?](#q10-how-do-you-implement-undoredo-functionality-with-ngrx) <span class="expert">Expert</span>
11. [How do you test an NgRx Effect that uses `debounceTime`?](#q11-how-do-you-test-an-ngrx-effect-that-uses-debouncetime) <span class="advanced">Advanced</span>
12. [How do you combine data from multiple feature stores in a single selector?](#q12-how-do-you-combine-data-from-multiple-feature-stores-in-a-single-selector) <span class="intermediate">Intermediate</span>
13. [How do you implement authentication flow (login/logout) using NgRx?](#q13-how-do-you-implement-authentication-flow-loginlogout-using-ngrx) <span class="intermediate">Intermediate</span>
14. [How do you optimize performance when dealing with large collections in NgRx?](#q14-how-do-you-optimize-performance-when-dealing-with-large-collections-in-ngrx) <span class="advanced">Advanced</span>
15. [How do you migrate a legacy service-based state to NgRx?](#q15-how-do-you-migrate-a-legacy-service-based-state-to-ngrx) <span class="expert">Expert</span>
16. [How do you test NgRx Effects using Marble Diagrams?](#q16-how-do-you-test-ngrx-effects-using-marble-diagrams) <span class="expert">Expert</span>
17. [How does NgRx interact with `OnPush` Change Detection?](#q17-how-does-ngrx-interact-with-onpush-change-detection) <span class="intermediate">Intermediate</span>
18. [How do you implement a Polling Effect (Start/Stop)?](#q18-how-do-you-implement-a-polling-effect-startstop) <span class="advanced">Advanced</span>
19. [How do you create a Meta-Reducer for logging actions?](#q19-how-do-you-create-a-meta-reducer-for-logging-actions) <span class="intermediate">Intermediate</span>
20. [How do you sort entities automatically using NgRx Entity?](#q20-how-do-you-sort-entities-automatically-using-ngrx-entity) <span class="intermediate">Intermediate</span>
21. [How do you use `tapResponse` in ComponentStore?](#q21-how-do-you-use-tapresponse-in-componentstore) <span class="intermediate">Intermediate</span>
22. [How do you define a SignalStore with state and methods?](#q22-how-do-you-define-a-signalstore-with-state-and-methods) <span class="advanced">Advanced</span>
23. [How do you connect an Observable to a SignalStore using `rxMethod`?](#q23-how-do-you-connect-an-observable-to-a-signalstore-using-rxmethod) <span class="advanced">Advanced</span>
24. [How do you group related actions using `createActionGroup`?](#q24-how-do-you-group-related-actions-using-createactiongroup) <span class="beginner">Beginner</span>
25. [How do you set up NgRx with Standalone APIs?](#q25-how-do-you-set-up-ngrx-with-standalone-apis) <span class="intermediate">Intermediate</span>
26. [How do you create Functional Effects?](#q26-how-do-you-create-functional-effects) <span class="intermediate">Intermediate</span>
27. [How do you enforce serializability checks for actions and state?](#q27-how-do-you-enforce-serializability-checks-for-actions-and-state) <span class="intermediate">Intermediate</span>
28. [How do you create a Custom Router Serializer?](#q28-how-do-you-create-a-custom-router-serializer) <span class="advanced">Advanced</span>
29. [How do you mock the Store in unit tests?](#q29-how-do-you-mock-the-store-in-unit-tests) <span class="intermediate">Intermediate</span>
30. [How do you use `createFeature` to reduce boilerplate?](#q30-how-do-you-use-createfeature-to-reduce-boilerplate) <span class="intermediate">Intermediate</span>
31. [How do you handle non-dispatching effects?](#q31-how-do-you-handle-non-dispatching-effects) <span class="beginner">Beginner</span>
32. [How do you select a Signal from the Store?](#q32-how-do-you-select-a-signal-from-the-store) <span class="intermediate">Intermediate</span>
33. [How do you handle global error reporting via Effects?](#q33-how-do-you-handle-global-error-reporting-via-effects) <span class="intermediate">Intermediate</span>
34. [How do you use Deep Signals in SignalStore?](#q34-how-do-you-use-deep-signals-in-signalstore) <span class="advanced">Advanced</span>
35. [How do you implement 'Load on Demand' (Lazy Loading) of state?](#q35-how-do-you-implement-load-on-demand-lazy-loading-of-state) <span class="advanced">Advanced</span>
36. [How do you use `concatLatestFrom` in Effects?](#q36-how-do-you-use-concatlatestfrom-in-effects) <span class="intermediate">Intermediate</span>
37. [How do you implement a 'Reset State' meta-reducer?](#q37-how-do-you-implement-a-reset-state-meta-reducer) <span class="intermediate">Intermediate</span>
38. [How do you test ComponentStore?](#q38-how-do-you-test-componentstore) <span class="intermediate">Intermediate</span>
39. [How do you manage loading/error states generically?](#q39-how-do-you-manage-loadingerror-states-generically) <span class="intermediate">Intermediate</span>
40. [How do you use the `routerNavigated` action?](#q40-how-do-you-use-the-routernavigated-action) <span class="intermediate">Intermediate</span>
41. [How do you implement Undo/Redo with SignalStore?](#q41-how-do-you-implement-undoredo-with-signalstore) <span class="advanced">Advanced</span>
42. [How do you select data based on route params?](#q42-how-do-you-select-data-based-on-route-params) <span class="advanced">Advanced</span>
43. [How do you optimize `OnPush` components with deep objects?](#q43-how-do-you-optimize-onpush-components-with-deep-objects) <span class="advanced">Advanced</span>
44. [How do you handle WebSocket messages in NgRx?](#q44-how-do-you-handle-websocket-messages-in-ngrx) <span class="advanced">Advanced</span>
45. [How do you use `provideStoreDevtools`?](#q45-how-do-you-use-providestoredevtools) <span class="beginner">Beginner</span>
46. [How do you implement Pagination with NgRx?](#q46-how-do-you-implement-pagination-with-ngrx) <span class="intermediate">Intermediate</span>
47. [How do you cancel an HTTP request when the component is destroyed?](#q47-how-do-you-cancel-an-http-request-when-the-component-is-destroyed) <span class="intermediate">Intermediate</span>
48. [How do you manage Forms with NgRx?](#q48-how-do-you-manage-forms-with-ngrx) <span class="intermediate">Intermediate</span>
49. [How do you use `ngrx-data`?](#q49-how-do-you-use-ngrx-data) <span class="advanced">Advanced</span>
50. [How do you migrate from NgRx Global Store to SignalStore?](#q50) <span class="advanced">Advanced</span>

---
<a id="q1"></a>
### Q1: What is the difference between NgRx Global Store and NgRx ComponentStore?

**Difficulty**: Beginner

**Strategy**: Understanding when to use global versus local state management is a fundamental architectural decision in Angular apps. The Global Store follows the Redux pattern with actions, reducers, and effects for app-wide shared state, while ComponentStore provides a lighter, service-based approach for component-scoped state without boilerplate. A common pitfall is overusing the Global Store for state that only lives within a single component, which adds unnecessary complexity.

**Strategy:**
*   **Global Store**: Single source of truth for the entire app. Used for shared state (Auth, Config). Dispatches actions, uses reducers/effects.
*   **ComponentStore**: Local state management for a specific component or feature. Service-based, no actions/reducers needed (uses `updater`/`effect`).

**Code Example:**
```typescript
// ComponentStore (Local)
@Injectable()
export class MoviesStore extends ComponentStore<MoviesState> { ... }

// Global Store
StoreModule.forRoot({ movies: moviesReducer })
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q2"></a>
### Q2: How do you prevent selector re-computation when using arguments (props)?

**Difficulty**: Advanced

**Strategy**: Selector memoization is critical for NgRx performance, and factory selectors that accept dynamic arguments can silently break memoization if not designed carefully. The key insight is that selectors cache based on input references, so passing new arguments on every call defeats the cache. Best practice is to keep selectors as simple as possible and move dynamic filtering logic into component-level computations or return dictionaries from selectors.

**Strategy:**
Use a "factory selector" function that returns the selector, or use the `props` argument carefully. Memoization breaks if arguments are dynamic. Ideally, filter data in the component or use `createSelector` to return a dictionary and pick from it.

**Code Example:**
```typescript
// Preferred: Select all entities, then pick by ID
export const selectTodoById = (id: string) => createSelector(
  selectTodoEntities,
  (entities) => entities[id]
);
```

---

<a id="q3"></a>
### Q3: How do you manage local component state using NgRx ComponentStore?

**Difficulty**: Intermediate

**Strategy**: ComponentStore is NgRx's answer to managing state that does not need to be shared across the entire application, reducing boilerplate compared to the full Global Store. It uses `updater` methods for synchronous state changes and `effect` methods for handling side effects like API calls, all within an injectable service. A common mistake is reaching for the Global Store when ComponentStore would be simpler and more maintainable for feature-local data.

**Strategy:**
Extend `ComponentStore`, define state interface, and use `updater` for state changes and `effect` for side effects.

**Code Example:**
```typescript
interface TodoState {
  todos: Todo[];
}

@Injectable()
export class TodoStore extends ComponentStore<TodoState> {
  constructor(private todoService: TodoService) {
    super({ todos: [] });
  }

  readonly addTodo = this.updater((state, todo: Todo) => ({
    ...state,
    todos: [...state.todos, todo],
  }));

  readonly loadTodos = this.effect((trigger$) => trigger$.pipe(
    switchMap(() => this.todoService.getAll().pipe(
      tapResponse({
        next: (todos) => this.patchState({ todos }),
        error: (e) => console.error(e),
      })
    ))
  ));
}
```

---

<a id="q4"></a>
### Q4: How do you implement the Facade pattern with NgRx to hide store complexity?

**Difficulty**: Intermediate

**Strategy**: The Facade pattern decouples components from the underlying state management implementation, making it easier to refactor or swap NgRx for another solution later. By exposing only Observables and methods through a service, components remain clean and unaware of actions, selectors, or store dispatching. This pattern is especially valuable in large teams where you want to enforce a consistent API boundary between UI and state layers.

**Strategy:**
Create an Injectable service that exposes Observables (selectors) and methods (dispatching actions). Components inject this facade instead of the Store directly.

**Code Example:**
```typescript
@Injectable({ providedIn: 'root' })
export class TodoFacade {
  todos$ = this.store.select(selectTodos);
  loading$ = this.store.select(selectLoading);

  constructor(private store: Store) {}

  loadTodos() {
    this.store.dispatch(loadTodos());
  }

  addTodo(todo: Todo) {
    this.store.dispatch(addTodo({ todo }));
  }
}
```

---

<a id="q5"></a>
### Q5: How do you handle race conditions in NgRx Effects (e.g., typeahead search)?

**Difficulty**: Intermediate

**Strategy**: Race conditions are one of the most common bugs in reactive applications, where multiple overlapping HTTP requests return results in an unpredictable order. The solution hinges on choosing the right RxJS flattening operator: `switchMap` cancels the previous request when a new one arrives, `concatMap` queues them, and `mergeMap` runs them all in parallel. For typeahead search, always use `switchMap` combined with `debounceTime` to avoid firing requests on every keystroke.

**Strategy:**
Use the `switchMap` operator. It cancels the previous inner observable (HTTP request) if a new action arrives before the previous one completes.

**Code Example:**
```typescript
search$ = createEffect(() => this.actions$.pipe(
  ofType(Actions.search),
  debounceTime(300),
  switchMap(({ query }) => this.service.search(query).pipe(
    map(results => Actions.searchSuccess({ results })),
    catchError(error => of(Actions.searchFailure({ error })))
  ))
));
```

---

<a id="q6"></a>
### Q6: How do you normalize deeply nested API data using NgRx Entity?

**Difficulty**: Advanced

**Strategy**: Storing denormalized nested objects in the store makes updates error-prone and leads to data duplication across state slices. Normalization flattens nested structures into separate entity collections keyed by ID, enabling O(1) lookups and consistent updates. A common pitfall is storing the raw API response directly without transformation, which makes reducer logic fragile when the API shape changes.

**Strategy:**
Flatten the data structure using `normalizr` or manual mapping before storing it. Use `EntityAdapter` to manage the flat collections.

**Code Example:**
```typescript
export const adapter: EntityAdapter<User> = createEntityAdapter<User>();

export const initialState: State = adapter.getInitialState();

const userReducer = createReducer(
  initialState,
  on(UserActions.loadUsersSuccess, (state, { users }) => {
    return adapter.setAll(users, state);
  })
);
```

---

<a id="q7"></a>
### Q7: How do you implement runtime checks to ensure state immutability?

**Difficulty**: Intermediate

**Strategy**: State immutability is a core Redux principle, and accidentally mutating state is one of the hardest bugs to track down because changes may not trigger re-renders. NgRx provides built-in runtime checks that throw clear errors whenever state or actions are mutated directly. Always enable these checks in development mode and disable them in production for performance, using the `runtimeChecks` configuration object.

**Strategy:**
Use `store-devtools` or `ngrx-store-freeze` (meta-reducer) in development mode to throw errors if state is mutated directly.

**Code Example:**
```typescript
@NgModule({
  imports: [
    StoreModule.forRoot(reducers, {
      runtimeChecks: {
        strictStateImmutability: true,
        strictActionImmutability: true,
      },
    }),
  ],
})
export class AppModule {}
```

---

<a id="q8"></a>
### Q8: How do you handle multiple actions triggering the same reducer logic?

**Difficulty**: Beginner

**Strategy**: Real-world reducers often need to handle the same state transition for different actions, such as resetting an error flag on both login and registration attempts. NgRx's `on()` function accepts multiple action creators as arguments, keeping the reducer DRY and maintainable. A common mistake is duplicating the same reducer logic in separate `on()` clauses, which increases maintenance burden and the risk of drift.

**Strategy:**
List multiple actions in the `on()` function of `createReducer`.

**Code Example:**
```typescript
export const reducer = createReducer(
  initialState,
  on(
    AuthActions.loginFailure,
    AuthActions.registerFailure,
    (state, { error }) => ({ ...state, error, loading: false })
  )
);
```

---

<a id="q9"></a>
### Q9: How do you hydrate NgRx state from LocalStorage on app startup?

**Difficulty**: Advanced

**Strategy**: State hydration allows the application to restore a previous session without re-fetching everything, improving perceived load time and offline resilience. The meta-reducer pattern intercepts the initial `INIT` action to merge persisted data into the store before any reducer runs. Be cautious about versioning your stored state and excluding sensitive or transient data to avoid stale or corrupted state on app updates.

**Strategy:**
Use a meta-reducer to intercept the `INIT` or `UPDATE` action and merge the state from LocalStorage.

**Code Example:**
```typescript
export function localStorageSyncReducer(reducer: ActionReducer<any>): ActionReducer<any> {
  return (state, action) => {
    if (action.type === INIT || action.type === UPDATE) {
      const storageValue = localStorage.getItem('appState');
      if (storageValue) {
        return JSON.parse(storageValue); // Merge logic might be needed
      }
    }
    const nextState = reducer(state, action);
    localStorage.setItem('appState', JSON.stringify(nextState));
    return nextState;
  };
}
```

---

<a id="q10"></a>
### Q10: How do you implement undo/redo functionality with NgRx?

**Difficulty**: Expert

**Strategy**: Undo/redo is a challenging feature that demonstrates deep understanding of reducer composition and state history management. The meta-reducer approach wraps the base reducer and maintains separate stacks for past and future states, swapping them on undo/redo actions. A common pitfall is storing the entire state on every action without limiting history size, which can cause memory leaks in long-running sessions.

**Strategy:**
Use a higher-order reducer (meta-reducer) that keeps a history of past and future states.

**Code Example:**
```typescript
export function undoRedo(reducer: ActionReducer<State>): ActionReducer<State> {
  let history = [];
  let future = [];
  
  return (state, action) => {
    switch (action.type) {
      case 'UNDO':
        const previous = history.pop();
        if (!previous) return state;
        future.push(state);
        return previous;
      case 'REDO':
        const next = future.pop();
        if (!next) return state;
        history.push(state);
        return next;
      default:
        if (state) history.push(state);
        return reducer(state, action);
    }
  };
}
```

---

<a id="q11"></a>
### Q11: How do you test an NgRx Effect that uses `debounceTime`?

**Difficulty**: Advanced

**Strategy**: Testing time-dependent RxJS operators like `debounceTime` requires controlling virtual time, otherwise tests become slow and flaky. The `TestScheduler` from `rxjs/testing` provides deterministic virtual time using marble notation, letting you verify debouncing behavior in milliseconds rather than waiting real time. A common mistake is using real delays with `setTimeout` in tests, which makes them non-deterministic and prone to timeout failures.

**Strategy:**
Use `TestScheduler` from `rxjs/testing` to control virtual time, or `fakeAsync` with `tick`.

**Code Example:**
```typescript
it('should debounce search', () => {
  testScheduler.run(({ hot, cold, expectObservable }) => {
    actions$ = hot('-a-b 300ms c', {
      a: search({ query: 'a' }),
      b: search({ query: 'ab' }),
      c: search({ query: 'abc' })
    });

    const expected = '- 300ms - 300ms r'; // Only 'abc' triggers result
    expectObservable(effects.search$).toBe(expected, { r: searchSuccess(...) });
  });
});
```

---

<a id="q12"></a>
### Q12: How do you combine data from multiple feature stores in a single selector?

**Difficulty**: Intermediate

**Strategy**: Cross-feature data composition is common in dashboards and detail pages that need information from different domain slices. `createSelector` accepts selectors from any number of feature stores, and NgRx re-runs the projector only when any input selector emits a new value. Keep in mind that combining selectors across features creates a coupling between those state slices, so use this sparingly and prefer keeping related data together when possible.

**Strategy:**
Import selectors from different feature slices and combine them using `createSelector`.

**Code Example:**
```typescript
export const selectUserOrders = createSelector(
  UserSelectors.selectCurrentUser,
  OrderSelectors.selectAllOrders,
  (user, orders) => orders.filter(o => o.userId === user.id)
);
```

---

<a id="q13"></a>
### Q13: How do you implement authentication flow (login/logout) using NgRx?

**Difficulty**: Intermediate

**Strategy**: Authentication is a canonical use case for NgRx because auth state is global, affects the entire UI, and involves side effects like API calls and navigation. The flow follows a clear pattern: actions trigger effects for async work, success actions update the store with tokens, and additional effects handle post-login navigation or post-logout cleanup. A common pitfall is forgetting to clear all auth-related state and cancel pending requests on logout, which can lead to stale data leaks.

**Strategy:**
1.  **Login:** Action -> Effect (API) -> Success Action (Store Token) -> Effect (Navigate).
2.  **Logout:** Action -> Reducer (Clear State) -> Effect (Clear Storage & Navigate).

**Code Example:**
```typescript
loginSuccess$ = createEffect(() => this.actions$.pipe(
  ofType(AuthActions.loginSuccess),
  tap(() => this.router.navigate(['/dashboard']))
), { dispatch: false });
```

---

<a id="q14"></a>
### Q14: How do you optimize performance when dealing with large collections in NgRx?

**Difficulty**: Advanced

**Strategy**: Performance degrades quickly when storing hundreds or thousands of entities in a plain JavaScript array, since lookups and updates are O(n). NgRx Entity replaces arrays with a normalized dictionary structure keyed by ID, enabling O(1) lookups and efficient CRUD operations through the EntityAdapter. A common mistake is storing large collections as arrays and using `Array.find` in selectors, which re-scans the entire list on every state change.

**Strategy:**
Use `@ngrx/entity`. It stores collections as a dictionary (map) `{ ids: [], entities: {} }` providing O(1) access and easy CRUD operations.

**Code Example:**
```typescript
const adapter = createEntityAdapter<Product>();
const initialState = adapter.getInitialState();

const reducer = createReducer(
  initialState,
  on(ProductActions.updateProduct, (state, { update }) => {
    return adapter.updateOne(update, state);
  })
);
```

---

<a id="q15"></a>
### Q15: How do you migrate a legacy service-based state to NgRx?

**Difficulty**: Expert

**Strategy**: Migrating from service-based state to NgRx is a common real-world scenario when Angular apps outgrow simple service patterns and need predictable state management. The key is an incremental approach: map each service property to a state slice, each service method to an action, and each API call to an effect. Avoid the "big bang" migration of all services at once; instead, migrate one feature module at a time, keeping the app functional throughout.

**Strategy:**
1.  Identify state properties in the service.
2.  Create Actions for each state mutation.
3.  Create Reducers to handle mutations.
4.  Move API calls to Effects.
5.  Replace service properties with Selectors in components.
6.  Replace service method calls with `store.dispatch()`.


---

<a id="q16"></a>
### Q16: How do you test NgRx Effects using Marble Diagrams?

**Difficulty**: Expert

**Strategy**: Marble testing provides a visual and precise way to verify complex async flows in Effects, including timing, ordering, and error handling. Hot observables simulate actions coming into the effect, cold observables simulate service responses, and `expectObservable` asserts the output stream. A common pitfall is confusing hot and cold observables: hot represents values already in flight, cold represents values that start on subscription.

**Strategy:**
Use `jasmine-marbles` or `rxjs/testing` to represent time and streams visually. Hot observables (`-a-`) simulate actions, cold (`-a|`) simulate service responses.

**Code Example:**
actions$ = hot('-a-', { a: load() });
const response = cold('-b|', { b: success() });
service.getAll.and.returnValue(response);

expectObservable(effects.load$).toBe('--c', { c: success() });

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q17"></a>
### Q17: How does NgRx interact with `OnPush` Change Detection?

**Difficulty**: Intermediate

**Strategy**: `OnPush` change detection is essential for Angular performance, and understanding how NgRx Observables trigger it correctly is a key interview topic. The `async` pipe subscribes to store selectors and automatically marks the component for checking when a new value emits, making NgRx and OnPush a natural fit. A common mistake is manually subscribing to selectors in the component and failing to trigger change detection, leading to stale UI.

**Strategy:**
NgRx streams (Observables) used with the `async` pipe automatically trigger change detection when a new value is emitted, making `OnPush` highly efficient.

**Code Example:**
@Component({
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `{{ count$ | async }}`
})

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q18"></a>
### Q18: How do you implement a Polling Effect (Start/Stop)?

**Difficulty**: Advanced

**Strategy**: Polling is needed for real-time dashboards and status monitors, and implementing it correctly with proper start/stop lifecycle management is a practical interview challenge. The pattern uses `switchMap` to start an `interval` on a trigger action and `takeUntil` to cancel it when a stop action fires. A common pitfall is forgetting the `takeUntil` guard, which leaves background HTTP requests running even after the component is destroyed.

**Strategy:**
Listen for a 'Start' action, switchMap to a timer/interval, and `takeUntil` a 'Stop' action.

**Code Example:**
startPolling$ = createEffect(() => actions$.pipe(
  ofType(start),
  switchMap(() => interval(5000).pipe(
    map(() => fetchUpdate()),
    takeUntil(actions$.pipe(ofType(stop)))
  ))
));

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q19"></a>
### Q19: How do you create a Meta-Reducer for logging actions?

**Difficulty**: Intermediate

**Strategy**: Meta-reducers are middleware-like functions that wrap the root reducer, making them ideal for cross-cutting concerns like logging, analytics, and state hydration. They receive every action before the actual reducer, allowing you to inspect, transform, or log the action and resulting state. A best practice is to keep meta-reducers focused on a single responsibility and to register them only in development mode when they are used for debugging.

**Strategy:**
A meta-reducer wraps the main reducer. It can inspect/log the action and state before/after the inner reducer runs.

**Code Example:**
export function logger(reducer: ActionReducer<any>): ActionReducer<any> {
  return (state, action) => {
    console.log('action', action);
    return reducer(state, action);
  };
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q20"></a>
### Q20: How do you sort entities automatically using NgRx Entity?

**Difficulty**: Intermediate

**Strategy**: Keeping entity collections sorted eliminates the need for repeated client-side sorting in selectors and ensures consistent display order. The `sortComparer` option in `createEntityAdapter` automatically maintains sort order whenever entities are added or updated. Be aware that sorting on every insertion has a performance cost for very large collections, so consider whether sorting in a selector instead would be more efficient.

**Strategy:**
Provide a `sortComparer` function to `createEntityAdapter`. The collection will maintain sort order on insertion/update.

**Code Example:**
export const adapter = createEntityAdapter<User>({
  sortComparer: (a, b) => a.name.localeCompare(b.name)
});

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q21"></a>
### Q21: How do you use `tapResponse` in ComponentStore?

**Difficulty**: Intermediate

**Strategy**: Error handling in Observable streams is tricky because an error tears down the entire subscription, breaking the effect permanently. `tapResponse` is NgRx's solution: it catches errors gracefully like `catchError` but does not tear down the stream, allowing the effect to continue handling future triggers. A common mistake is using a bare `tap` with a `catchError` inside `switchMap`, which can leave the effect in a dead state after an error.

**Strategy:**
`tapResponse` safely handles side effects (success/error) in an Effect without breaking the stream on error (unlike a simple `subscribe`).

**Code Example:**
this.effect(trigger$ => trigger$.pipe(
  switchMap(() => api.get().pipe(
    tapResponse(
      (data) => this.updateState(data),
      (error) => this.logError(error)
    )
  ))
));

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q22"></a>
### Q22: How do you define a SignalStore with state and methods?

**Difficulty**: Advanced

**Strategy**: SignalStore is NgRx's modern, signal-based state management approach that leverages Angular signals for fine-grained reactivity without Zone.js. It uses a composable API with `withState`, `withComputed`, and `withMethods` to build stores declaratively. Understanding SignalStore is important for interviews because it represents the direction Angular is heading, and developers should know when to adopt it over the traditional Global Store.

**Strategy:**
Use `signalStore` with `withState`, `withComputed`, and `withMethods`.

**Code Example:**
export const CounterStore = signalStore(
  withState({ count: 0 }),
  withComputed(({ count }) => ({ double: computed(() => count() * 2) })),
  withMethods((store) => ({
    increment: () => patchState(store, (state) => ({ count: state.count + 1 }))
  }))
);

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q23"></a>
### Q23: How do you connect an Observable to a SignalStore using `rxMethod`?

**Difficulty**: Advanced

**Strategy**: `rxMethod` bridges the reactive Observable world with Angular's signal-based SignalStore, enabling you to handle async operations like API calls within a signal context. It accepts a value, a Signal, or an Observable as input and runs the full RxJS pipeline you define. This is essential for real-world apps where most data comes from async sources, and knowing it shows you understand how to blend signals and Observables effectively.

**Strategy:**
`rxMethod` creates a reactive method that can accept a value, Signal, or Observable, and run a pipeline (like Effects).

**Code Example:**
load = rxMethod<void>(pipe(
  switchMap(() => service.load().pipe(
    tapResponse({ next: c => patchState(store, { c }), error: console.error })
  ))
));

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q24"></a>
### Q24: How do you group related actions using `createActionGroup`?

**Difficulty**: Beginner

**Strategy**: Organizing actions by source domain improves code discoverability and reduces the scattered `createAction` declarations across large codebases. `createActionGroup` lets you define all actions for a feature in one object with consistent naming conventions. A best practice is to group actions by the API or domain event they represent (e.g., `BooksApi`, `BooksPage`) rather than lumping everything into a single group.

**Strategy:**
Use `createActionGroup` to define a source and event dictionary. Reduces boilerplate and enforces consistent naming.

**Code Example:**
export const AuthActions = createActionGroup({
  source: 'Auth API',
  events: {
    'Login': props<{ user: string }>(),
    'Login Success': props<{ token: string }>(),
    'Login Failure': props<{ error: any }>()
  }
});

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q25"></a>
### Q25: How do you set up NgRx with Standalone APIs?

**Difficulty**: Intermediate

**Strategy**: Angular's move to standalone APIs means NgRx setup no longer requires `NgModule` boilerplate, and interviewers expect you to know the modern `provideStore` and `provideEffects` pattern. These providers go directly into `app.config.ts` or lazy-loaded route configurations. A common mistake is still wrapping NgRx setup in a feature module when the rest of the app has migrated to standalone components.

**Strategy:**
Use `provideStore` and `provideEffects` in the `app.config.ts` providers array.

**Code Example:**
bootstrapApplication(App, {
  providers: [
    provideStore(reducers),
    provideEffects(AppEffects),
    provideStoreDevtools()
  ]
});

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q26"></a>
### Q26: How do you create Functional Effects?

**Difficulty**: Intermediate

**Strategy**: Functional Effects eliminate the need for class-based Effect services, aligning with Angular's shift toward functional and tree-shakable patterns. They use `inject()` for dependency injection and the `functional: true` flag, resulting in less boilerplate. This is increasingly the preferred approach in modern NgRx codebases, and knowing it signals that you keep up with current Angular ecosystem trends.

**Strategy:**
Define effects as functions using `createEffect` with `inject`. No class needed.

**Code Example:**
export const loadUsers = createEffect(
  (actions$ = inject(Actions), service = inject(UserService)) => actions$.pipe(...)
, { functional: true });

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q27"></a>
### Q27: How do you enforce serializability checks for actions and state?

**Difficulty**: Intermediate

**Strategy**: Non-serializable values in the store (Date objects, class instances, functions) break time-travel debugging, state hydration, and can cause subtle bugs. Enabling `strictStateSerializability` and `strictActionSerializability` catches these violations at development time with clear error messages. A common pitfall is storing `Date` objects directly instead of ISO strings, which serializes correctly but loses the Date methods.

**Strategy:**
Enable `strictActionSerializability` and `strictStateSerializability` in store config. This prevents putting non-serializable objects (like Dates, Class instances) in the store.

**Code Example:**
provideStore(reducers, {
  runtimeChecks: {
    strictStateSerializability: true,
    strictActionSerializability: true
  }
})

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q28"></a>
### Q28: How do you create a Custom Router Serializer?

**Difficulty**: Advanced

**Strategy**: The default router store state includes the entire router snapshot tree, which is large and expensive to serialize and compare for changes. A custom `RouterStateSerializer` extracts only the specific fields your selectors need, dramatically reducing store size and improving performance. This optimization is particularly important in apps that react to route changes frequently, such as those with complex navigation or breadcrumb logic.

**Strategy:**
Implement `RouterStateSerializer` to extract only necessary router data (url, params, queryParams) into the store, keeping the state clean.

**Code Example:**
export class CustomSerializer implements RouterStateSerializer<MinimalRouterState> {
  serialize(routerState: RouterStateSnapshot): MinimalRouterState {
    // Extract logic
  }
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q29"></a>
### Q29: How do you mock the Store in unit tests?

**Difficulty**: Intermediate

**Strategy**: Properly mocking the NgRx Store is essential for writing fast, isolated unit tests for components and services without setting up the full store chain. `provideMockStore` gives you a `MockStore` instance where you can override any selector's return value with `overrideSelector`. A best practice is to use `MockStore` for component tests and reserve integration-level tests with the real store for testing reducer and effect logic.

**Strategy:**
Use `provideMockStore` and `MockStore`. You can override selectors to return specific test data.

**Code Example:**
TestBed.configureTestingModule({
  providers: [provideMockStore({ initialState })]
});
store.overrideSelector(selectUser, { name: 'Test' });

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q30"></a>
### Q30: How do you use `createFeature` to reduce boilerplate?

**Difficulty**: Intermediate

**Strategy**: NgRx is often criticized for its boilerplate, and `createFeature` is the primary API for reducing it by generating selectors, the feature name, and the reducer in a single call. This ensures consistent naming conventions and eliminates the need to manually write feature selectors. Adopting `createFeature` is considered a best practice in modern NgRx and demonstrates that you write concise, maintainable store code.

**Strategy:**
`createFeature` generates the reducer, selectors, and feature name in one go.

**Code Example:**
export const counterFeature = createFeature({
  name: 'counter',
  reducer: createReducer(...)
});

const { selectCount } = counterFeature;

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q31"></a>
### Q31: How do you handle non-dispatching effects?

**Difficulty**: Beginner

**Strategy**: Not every side effect needs to update the store; navigation, logging, and showing notifications are common examples that perform work without changing state. Non-dispatching effects use `{ dispatch: false }` to tell NgRx that the effect's output should not be treated as a new action. A common mistake is forgetting this flag and having the effect's return value accidentally dispatched as an action, causing errors.

**Strategy:**
Set `{ dispatch: false }`. Use this for side effects that don't update state (e.g., navigation, alerts, logging).

**Code Example:**
log$ = createEffect(() => actions$.pipe(
  tap(action => console.log(action))
), { dispatch: false });

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q32"></a>
### Q32: How do you select a Signal from the Store?

**Difficulty**: Intermediate

**Strategy**: Angular signals offer finer-grained reactivity than Observables, and `selectSignal` bridges NgRx with the signal ecosystem by returning a Signal instead of an Observable. This eliminates the need for the `async` pipe and works seamlessly with signal-based components and computed values. Knowing when to use `selectSignal` versus `store.select` demonstrates understanding of Angular's evolving reactivity model.

**Strategy:**
Use `store.selectSignal(selector)`. It returns a Signal instead of an Observable, useful for Angular 17+ signal-based components.

**Code Example:**
count = this.store.selectSignal(selectCount);
// In template: {{ count() }}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q33"></a>
### Q33: How do you handle global error reporting via Effects?

**Difficulty**: Intermediate

**Strategy**: Centralized error handling prevents scattered `console.error` calls and ensures users see consistent error feedback like toast notifications. The pattern involves catching errors in feature effects and dispatching a shared error action that a central effect listens to for UI notification. A best practice is to include enough context (source, error code, user message) in the error action so the central handler can make smart decisions about how to display it.

**Strategy:**
Catch errors in feature effects and dispatch a shared `GlobalActions.error` action. A central effect listens for this and shows a toast/snackbar.

**Code Example:**
catchError(error => of(GlobalActions.error({ message: error.message })))

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q34"></a>
### Q34: How do you use Deep Signals in SignalStore?

**Difficulty**: Advanced

**Strategy**: Deep signals automatically create granular signal references for nested state properties, enabling fine-grained change detection without manual decomposition. Accessing `store.user.address.city()` gives you a signal that only updates when the city value actually changes, not when unrelated parts of the user object change. This is a powerful optimization for complex state trees where only a small subset of data changes frequently.

**Strategy:**
SignalStore creates deep signals for nested state automatically. You can access nested properties directly as signals.

**Code Example:**
const store = inject(UserStore);
// If state is { user: { address: { city: 'NY' } } }
effect(() => console.log(store.user.address.city()));

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q35"></a>
### Q35: How do you implement 'Load on Demand' (Lazy Loading) of state?

**Difficulty**: Advanced

**Strategy**: Lazy-loaded feature states reduce the initial bundle size and avoid allocating memory for state slices that the user may never visit. By registering state with `provideState` or `StoreModule.forFeature` inside lazy-loaded routes, the state slice appears in the store only when that module loads. A common pitfall is referencing selectors for a lazy feature before it has been loaded, which returns `undefined` and can cause runtime errors.

**Strategy:**
Register the feature state (`StoreModule.forFeature`) in the lazy-loaded module/route. The state slice is created only when the module loads.

**Code Example:**
providers: [
  provideState(featureName, featureReducer)
]

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q36"></a>
### Q36: How do you use `concatLatestFrom` in Effects?

**Difficulty**: Intermediate

**Strategy**: Accessing current store state inside an effect is a common need, but using `store.select` directly creates a long-lived subscription that can cause memory leaks and unexpected behavior. `concatLatestFrom` lazily reads the current state value only when the effect pipeline reaches it, avoiding unnecessary subscriptions. It is the recommended replacement for the deprecated `withLatestFrom` pattern within NgRx effects.

**Strategy:**
`concatLatestFrom` (from `@ngrx/effects`) safely selects state within an effect without subscribing to the store manually. It's lazy and non-blocking.

**Code Example:**
concatLatestFrom(() => this.store.select(selectUser)),
tap(([action, user]) => ...)

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q37"></a>
### Q37: How do you implement a 'Reset State' meta-reducer?

**Difficulty**: Intermediate

**Strategy**: Resetting state on logout is critical for security, preventing a new user from seeing the previous user's cached data. The meta-reducer pattern intercepts a logout action and passes `undefined` as state to the inner reducer, which triggers the initial state default values. A common mistake is trying to manually reset each feature slice individually instead of using this centralized approach.

**Strategy:**
Listen for a `LOGOUT` action. If received, return `undefined` to the inner reducer, forcing it to re-initialize state.

**Code Example:**
if (action.type === 'LOGOUT') {
  return reducer(undefined, action);
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q38"></a>
### Q38: How do you test ComponentStore?

**Difficulty**: Intermediate

**Strategy**: ComponentStore is an injectable service, so testing it follows the same patterns as testing any Angular service with `TestBed`. You can call updater methods directly, trigger effects, and assert on the resulting state through selectors. A best practice is to mock external service dependencies rather than making real HTTP calls, keeping tests fast and deterministic.

**Strategy:**
Test it like a service. Subscribe to selectors or call effects and verify state changes or spy on dependencies.

**Code Example:**
store.addTodo(todo);
store.todos$.subscribe(t => expect(t).toContain(todo));

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q39"></a>
### Q39: How do you manage loading/error states generically?

**Difficulty**: Intermediate

**Strategy**: Every async operation needs loading and error tracking, and duplicating this logic across every feature creates maintenance headaches. The `CallState` pattern wraps entity data with a status enum (`init`, `loading`, `loaded`, `error`), providing a consistent API for the UI to show spinners and error messages. A common pitfall is using separate boolean flags (`isLoading`, `hasError`) which can reach invalid combinations like both being true simultaneously.

**Strategy:**
Use a higher-order state interface (e.g., `CallState` pattern) or a shared utility to wrap entity state with `loading` and `error` flags.

**Code Example:**
interface State<T> {
  data: T;
  status: 'init' | 'loading' | 'loaded' | 'error';
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q40"></a>
### Q40: How do you use the `routerNavigated` action?

**Difficulty**: Intermediate

**Strategy**: Reacting to navigation events is essential for features like analytics tracking, breadcrumb updates, and fetching data tied to route changes. The `routerNavigated` action from `@ngrx/router-store` fires after a successful navigation, giving you access to the full router state in an effect. A best practice is to use `routerNavigated` instead of subscribing to `Router.events` directly, keeping all side-effect logic centralized in NgRx effects.

**Strategy:**
Listen to `routerNavigated` from `@ngrx/router-store` in an effect to trigger actions based on successful navigation (e.g., analytics).

**Code Example:**
ofType(routerNavigated),
tap(action => trackPageView(action.payload.routerState.url))

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q41"></a>
### Q41: How do you implement Undo/Redo with SignalStore?

**Difficulty**: Advanced

**Strategy**: Implementing undo/redo with SignalStore demonstrates how to build custom store features using the composable `with*` pattern. The approach maintains a history stack signal alongside the current state, pushing snapshots on each mutation and popping them on undo. A key consideration is limiting the history depth to prevent memory issues and deciding which state properties should be tracked to avoid undoing trivial changes.

**Strategy:**
Use `withUndoRedo` custom feature (community or manual). Maintain a history stack signal and update current state on undo.

**Code Example:**
```typescript
import { signalStore, withState, patchState } from '@ngrx/signals';
import { withUndoRedo } from '@ngrx/signals/features'; // Hypothetical or custom

export const UserStore = signalStore(
  withState({ user: null }),
  withUndoRedo({
    maxHistory: 10,
    keys: ['user'] // Only track user changes
  })
);

// Usage
store.undo();
store.redo();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q42"></a>
### Q42: How do you select data based on route params?

**Difficulty**: Advanced

**Strategy**: Combining router state with entity data is a frequent requirement in detail pages, where the URL parameter determines which entity to display. Using `selectRouteParams` from RouterStore in a `createSelector` composition keeps the data derivation declarative and memoized. A common pitfall is subscribing to route params and the store separately in the component and combining them imperatively, which loses the benefits of selector memoization.

**Strategy:**
Use `selectRouteParams` from RouterStore selectors combined with entity selectors.

**Code Example:**
```typescript
import { getRouterSelectors } from '@ngrx/router-store';

const { selectRouteParams } = getRouterSelectors();

export const selectSelectedUser = createSelector(
  selectUserEntities,
  selectRouteParams,
  (users, params) => users[params['id']]
);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q43"></a>
### Q43: How do you optimize `OnPush` components with deep objects?

**Difficulty**: Advanced

**Strategy**: `OnPush` components only re-render when input references change, so selectors returning new object references on every call defeat change detection optimization. The solution is to ensure selectors return the same reference when the underlying data has not changed, leveraging memoization correctly. A common mistake is creating new objects or arrays inside selector projectors without checking if the output is actually different from the previous result.

**Strategy:**
Ensure selectors return new references only when data actually changes (memoization). Avoid returning new objects `{...}` in selectors if data is unchanged.

**Code Example:**
```typescript
// Bad: Returns new reference every time
export const selectBad = createSelector(
  selectItems,
  items => ({ count: items.length }) 
);

// Good: Returns same reference if length is same
export const selectGood = createSelector(
  selectItems,
  items => items.length
);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q44"></a>
### Q44: How do you handle WebSocket messages in NgRx?

**Difficulty**: Advanced

**Strategy**: Real-time features like chat, notifications, and live dashboards require WebSocket integration with the store, and NgRx Effects provide a natural bridge. The effect subscribes to the WebSocket stream and maps incoming messages to actions, keeping the store as the single source of truth for real-time data. A critical consideration is managing the connection lifecycle: open the socket on login or feature activation and close it on logout using `takeUntil`.

**Strategy:**
Create an effect that connects to the socket and maps incoming messages to Actions. Dispatch actions to update state.

**Code Example:**
```typescript
listenToMessages$ = createEffect(() => {
  return this.actions$.pipe(
    ofType(AuthActions.loginSuccess),
    switchMap(() => this.socketService.messages$.pipe(
      map(msg => ChatActions.messageReceived({ msg })),
      takeUntil(this.actions$.pipe(ofType(AuthActions.logout)))
    ))
  );
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q45"></a>
### Q45: How do you use `provideStoreDevtools`?

**Difficulty**: Beginner

**Strategy**: Redux DevTools is one of the most powerful debugging tools for state management, enabling time-travel debugging and action inspection. `provideStoreDevtools` configures it for standalone Angular apps with options like `maxAge` to limit action history and `logOnly` for production safety. A best practice is to never ship DevTools enabled in production with trace mode on, as it can expose sensitive state data and impact performance.

**Strategy:**
Add it to providers. Configure `maxAge` and `logOnly` for production.

**Code Example:**
```typescript
import { provideStoreDevtools } from '@ngrx/store-devtools';

bootstrapApplication(AppComponent, {
  providers: [
    provideStore(reducers),
    provideStoreDevtools({
      maxAge: 25,
      logOnly: !isDevMode(),
      autoPause: true,
      trace: false,
      traceLimit: 75,
    }),
  ],
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q46"></a>
### Q46: How do you implement Pagination with NgRx?

**Difficulty**: Intermediate

**Strategy**: Pagination is a standard feature in data-heavy applications, and implementing it with NgRx demonstrates proper state, effect, and selector composition. Store pagination parameters (`page`, `pageSize`) in the state, trigger API calls through effects with those params, and use selectors to derive the current page slice from the response. A common pitfall is storing the entire dataset client-side and slicing in a selector, rather than letting the server handle pagination.

**Strategy:**
Store `page`, `pageSize`, and `total` in state. Effects trigger API calls with these params. Selectors derive the current page slice.

**Code Example:**
```typescript
loadPage$ = createEffect(() => this.actions$.pipe(
  ofType(PageActions.changePage),
  concatLatestFrom(() => this.store.select(selectPaginationParams)),
  switchMap(([action, { page, pageSize }]) => 
    this.service.getItems(page, pageSize).pipe(
      map(items => PageActions.loadSuccess({ items }))
    )
  )
));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q47"></a>
### Q47: How do you cancel an HTTP request when the component is destroyed?

**Difficulty**: Intermediate

**Strategy**: Uncanceled HTTP requests create memory leaks and can cause state updates on destroyed components, leading to confusing errors. With ComponentStore, effects are tied to the component lifecycle and cancel automatically, but with the Global Store you must dispatch a destroy action and use `takeUntil` in the effect. A best practice is to always pair load actions with corresponding cancel/destroy actions to ensure clean teardown.

**Strategy:**
If using `ComponentStore`, the effect is tied to the lifecycle and cancels automatically. In global Effects, listen for a specific Cancel action dispatch in `ngOnDestroy`.

**Code Example:**
```typescript
// In Component
ngOnDestroy() {
  this.store.dispatch(PageActions.destroyed());
}

// In Effect
loadData$ = createEffect(() => this.actions$.pipe(
  ofType(PageActions.load),
  switchMap(() => this.service.getData().pipe(
    takeUntil(this.actions$.pipe(ofType(PageActions.destroyed))),
    map(data => PageActions.success({ data }))
  ))
));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q48"></a>
### Q48: How do you manage Forms with NgRx?

**Difficulty**: Intermediate

**Strategy**: Storing every keystroke in the NgRx store is an anti-pattern that creates excessive action dispatching and performance overhead. The recommended approach is to use Reactive Forms for local form state and dispatch a single action only on form submission. Reserve `ngrx-forms` for rare cases where form state genuinely needs to be shared across distant components or persisted across navigation.

**Strategy:**
Avoid storing every keystroke in Redux. Use local state for the form, and dispatch a single action on Submit. Or use Reactive Forms with `ngrx-forms` (if complex).

**Code Example:**
```typescript
@Component({...})
export class ContactComponent {
  form = this.fb.group({ name: [''], email: [''] });

  onSubmit() {
    if (this.form.valid) {
      this.store.dispatch(ContactActions.submit({ 
        data: this.form.value 
      }));
    }
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q49"></a>
### Q49: How do you use `ngrx-data`?

**Difficulty**: Advanced

**Strategy**: `ngrx-data` dramatically reduces CRUD boilerplate by generating actions, reducers, selectors, and effects automatically based on entity metadata. It is best suited for applications with many standard REST-backed entities where the CRUD pattern is repetitive and consistent. A key consideration is that while `ngrx-data` speeds up development for standard cases, customizing non-standard behavior can be more difficult than writing the NgRx code manually.

**Strategy:**
`ngrx-data` automates standard CRUD. Define `EntityMetadataMap`, register it, and inject `EntityCollectionService<T>`.

**Code Example:**
```typescript
const entityMetadata: EntityMetadataMap = {
  Hero: {
    selectId: (hero) => hero.uuid, // Custom ID
  }
};

@Injectable()
export class HeroService extends EntityCollectionServiceBase<Hero> {
  constructor(serviceElementsFactory: EntityCollectionServiceElementsFactory) {
    super('Hero', serviceElementsFactory);
  }
}
// Usage: this.heroService.getAll();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q50"></a>
### Q50: How do you migrate from NgRx Global Store to SignalStore?

**Difficulty**: Advanced

**Strategy**: Migrating to SignalStore is an increasingly relevant topic as Angular signals mature and become the default reactivity model. The migration maps reducers to `withMethods`, selectors to `withComputed`, and effects to `rxMethod`, adopting a more composable and less boilerplate-heavy pattern. A best practice is to migrate incrementally, keeping the Global Store for truly app-wide state like authentication while moving feature state to SignalStore.

**Strategy:**
Refactor Feature States to SignalStores. Replace Selectors with computed signals. Replace Actions/Effects with `rxMethod`. Keep Global Store for truly global data (Auth).

**Code Example:**
```typescript
// Before (Reducer)
on(increment, state => ({ count: state.count + 1 }))

// After (SignalStore)
withMethods((store) => ({
  increment: () => patchState(store, (state) => ({ count: state.count + 1 }))
}))
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---
