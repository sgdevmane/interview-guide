# NgRx Interview Questions

## Table of Contents

1. [How do you handle optimistic UI updates using NgRx Effects?](#q1-how-do-you-handle-optimistic-ui-updates-using-ngrx-effects) <span class="advanced">Advanced</span>
2. [How do you prevent selector re-computation when using arguments (props)?](#q2-how-do-you-prevent-selector-re-computation-when-using-arguments-props) <span class="advanced">Advanced</span>
3. [How do you manage local component state using NgRx ComponentStore?](#q3-how-do-you-manage-local-component-state-using-ngrx-componentstore) <span class="intermediate">Intermediate</span>
4. [How do you implement the Facade pattern with NgRx to hide store complexity?](#q4-how-do-you-implement-the-facade-pattern-with-ngrx-to-hide-store-complexity) <span class="intermediate">Intermediate</span>
5. [How do you handle race conditions in NgRx Effects (e.g., typeahead search)?](#q5-how-do-you-handle-race-conditions-in-ngrx-effects-eg-typeahead-search) <span class="intermediate">Intermediate</span>
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
50. [How do you migrate from NgRx Global Store to SignalStore?](#q50-how-do-you-migrate-from-ngrx-global-store-to-signalstore) <span class="advanced">Advanced</span>

---

### Q2: How do you prevent selector re-computation when using arguments (props)?

**Difficulty**: Advanced

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

### Q3: How do you manage local component state using NgRx ComponentStore?

**Difficulty**: Intermediate

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

### Q4: How do you implement the Facade pattern with NgRx to hide store complexity?

**Difficulty**: Intermediate

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

### Q5: How do you handle race conditions in NgRx Effects (e.g., typeahead search)?

**Difficulty**: Intermediate

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

### Q6: How do you normalize deeply nested API data using NgRx Entity?

**Difficulty**: Advanced

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

### Q7: How do you implement runtime checks to ensure state immutability?

**Difficulty**: Intermediate

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

### Q8: How do you handle multiple actions triggering the same reducer logic?

**Difficulty**: Beginner

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

### Q9: How do you hydrate NgRx state from LocalStorage on app startup?

**Difficulty**: Advanced

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

### Q10: How do you implement undo/redo functionality with NgRx?

**Difficulty**: Expert

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

### Q11: How do you test an NgRx Effect that uses `debounceTime`?

**Difficulty**: Advanced

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

### Q12: How do you combine data from multiple feature stores in a single selector?

**Difficulty**: Intermediate

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

### Q13: How do you implement authentication flow (login/logout) using NgRx?

**Difficulty**: Intermediate

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

### Q14: How do you optimize performance when dealing with large collections in NgRx?

**Difficulty**: Advanced

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

### Q15: How do you migrate a legacy service-based state to NgRx?

**Difficulty**: Expert

**Strategy:**
1.  Identify state properties in the service.
2.  Create Actions for each state mutation.
3.  Create Reducers to handle mutations.
4.  Move API calls to Effects.
5.  Replace service properties with Selectors in components.
6.  Replace service method calls with `store.dispatch()`.


---

### Q16: How do you test NgRx Effects using Marble Diagrams?

**Difficulty**: Expert

**Strategy:**
Use `jasmine-marbles` or `rxjs/testing` to represent time and streams visually. Hot observables (`-a-`) simulate actions, cold (`-a|`) simulate service responses.

**Code Example:**
actions$ = hot('-a-', { a: load() });
const response = cold('-b|', { b: success() });
service.getAll.and.returnValue(response);

expectObservable(effects.load$).toBe('--c', { c: success() });

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q17: How does NgRx interact with `OnPush` Change Detection?

**Difficulty**: Intermediate

**Strategy:**
NgRx streams (Observables) used with the `async` pipe automatically trigger change detection when a new value is emitted, making `OnPush` highly efficient.

**Code Example:**
@Component({
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `{{ count$ | async }}`
})

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q18: How do you implement a Polling Effect (Start/Stop)?

**Difficulty**: Advanced

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

### Q19: How do you create a Meta-Reducer for logging actions?

**Difficulty**: Intermediate

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

### Q20: How do you sort entities automatically using NgRx Entity?

**Difficulty**: Intermediate

**Strategy:**
Provide a `sortComparer` function to `createEntityAdapter`. The collection will maintain sort order on insertion/update.

**Code Example:**
export const adapter = createEntityAdapter<User>({
  sortComparer: (a, b) => a.name.localeCompare(b.name)
});

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q21: How do you use `tapResponse` in ComponentStore?

**Difficulty**: Intermediate

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

### Q22: How do you define a SignalStore with state and methods?

**Difficulty**: Advanced

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

### Q23: How do you connect an Observable to a SignalStore using `rxMethod`?

**Difficulty**: Advanced

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

### Q24: How do you group related actions using `createActionGroup`?

**Difficulty**: Beginner

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

### Q25: How do you set up NgRx with Standalone APIs?

**Difficulty**: Intermediate

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

### Q26: How do you create Functional Effects?

**Difficulty**: Intermediate

**Strategy:**
Define effects as functions using `createEffect` with `inject`. No class needed.

**Code Example:**
export const loadUsers = createEffect(
  (actions$ = inject(Actions), service = inject(UserService)) => actions$.pipe(...)
, { functional: true });

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q27: How do you enforce serializability checks for actions and state?

**Difficulty**: Intermediate

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

### Q28: How do you create a Custom Router Serializer?

**Difficulty**: Advanced

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

### Q29: How do you mock the Store in unit tests?

**Difficulty**: Intermediate

**Strategy:**
Use `provideMockStore` and `MockStore`. You can override selectors to return specific test data.

**Code Example:**
TestBed.configureTestingModule({
  providers: [provideMockStore({ initialState })]
});
store.overrideSelector(selectUser, { name: 'Test' });

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q30: How do you use `createFeature` to reduce boilerplate?

**Difficulty**: Intermediate

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

### Q31: How do you handle non-dispatching effects?

**Difficulty**: Beginner

**Strategy:**
Set `{ dispatch: false }`. Use this for side effects that don't update state (e.g., navigation, alerts, logging).

**Code Example:**
log$ = createEffect(() => actions$.pipe(
  tap(action => console.log(action))
), { dispatch: false });

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q32: How do you select a Signal from the Store?

**Difficulty**: Intermediate

**Strategy:**
Use `store.selectSignal(selector)`. It returns a Signal instead of an Observable, useful for Angular 17+ signal-based components.

**Code Example:**
count = this.store.selectSignal(selectCount);
// In template: {{ count() }}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q33: How do you handle global error reporting via Effects?

**Difficulty**: Intermediate

**Strategy:**
Catch errors in feature effects and dispatch a shared `GlobalActions.error` action. A central effect listens for this and shows a toast/snackbar.

**Code Example:**
catchError(error => of(GlobalActions.error({ message: error.message })))

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q34: How do you use Deep Signals in SignalStore?

**Difficulty**: Advanced

**Strategy:**
SignalStore creates deep signals for nested state automatically. You can access nested properties directly as signals.

**Code Example:**
const store = inject(UserStore);
// If state is { user: { address: { city: 'NY' } } }
effect(() => console.log(store.user.address.city()));

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q35: How do you implement 'Load on Demand' (Lazy Loading) of state?

**Difficulty**: Advanced

**Strategy:**
Register the feature state (`StoreModule.forFeature`) in the lazy-loaded module/route. The state slice is created only when the module loads.

**Code Example:**
providers: [
  provideState(featureName, featureReducer)
]

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q36: How do you use `concatLatestFrom` in Effects?

**Difficulty**: Intermediate

**Strategy:**
`concatLatestFrom` (from `@ngrx/effects`) safely selects state within an effect without subscribing to the store manually. It's lazy and non-blocking.

**Code Example:**
concatLatestFrom(() => this.store.select(selectUser)),
tap(([action, user]) => ...)

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q37: How do you implement a 'Reset State' meta-reducer?

**Difficulty**: Intermediate

**Strategy:**
Listen for a `LOGOUT` action. If received, return `undefined` to the inner reducer, forcing it to re-initialize state.

**Code Example:**
if (action.type === 'LOGOUT') {
  return reducer(undefined, action);
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q38: How do you test ComponentStore?

**Difficulty**: Intermediate

**Strategy:**
Test it like a service. Subscribe to selectors or call effects and verify state changes or spy on dependencies.

**Code Example:**
store.addTodo(todo);
store.todos$.subscribe(t => expect(t).toContain(todo));

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q39: How do you manage loading/error states generically?

**Difficulty**: Intermediate

**Strategy:**
Use a higher-order state interface (e.g., `CallState` pattern) or a shared utility to wrap entity state with `loading` and `error` flags.

**Code Example:**
interface State<T> {
  data: T;
  status: 'init' | 'loading' | 'loaded' | 'error';
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q40: How do you use the `routerNavigated` action?

**Difficulty**: Intermediate

**Strategy:**
Listen to `routerNavigated` from `@ngrx/router-store` in an effect to trigger actions based on successful navigation (e.g., analytics).

**Code Example:**
ofType(routerNavigated),
tap(action => trackPageView(action.payload.routerState.url))

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q41: How do you implement Undo/Redo with SignalStore?

**Difficulty**: Advanced

**Strategy:**
Use `withUndoRedo` custom feature (community or manual). Maintain a history stack signal and update current state on undo.

**Code Example:**
// Custom feature implementation

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q42: How do you select data based on route params?

**Difficulty**: Advanced

**Strategy:**
Use `selectRouteParams` from RouterStore selectors combined with entity selectors.

**Code Example:**
export const selectSelectedUser = createSelector(
  selectUserEntities,
  selectRouteParam('id'),
  (users, id) => users[id]
);

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q43: How do you optimize `OnPush` components with deep objects?

**Difficulty**: Advanced

**Strategy:**
Ensure selectors return new references only when data actually changes (memoization). Avoid returning new objects `{...}` in selectors if data is unchanged.

**Code Example:**
// Good
createSelector(s1, s2, (a, b) => a.id === b.id ? a : { ...a, ...b })

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q44: How do you handle WebSocket messages in NgRx?

**Difficulty**: Advanced

**Strategy:**
Create an effect that connects to the socket and maps incoming messages to Actions. Dispatch actions to update state.

**Code Example:**
return socket.messages$.pipe(
  map(msg => Actions.messageReceived({ msg }))
);

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q45: How do you use `provideStoreDevtools`?

**Difficulty**: Beginner

**Strategy:**
Add it to providers. Configure `maxAge` and `logOnly` for production.

**Code Example:**
provideStoreDevtools({
  maxAge: 25,
  logOnly: environment.production
})

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q46: How do you implement Pagination with NgRx?

**Difficulty**: Intermediate

**Strategy:**
Store `page`, `pageSize`, and `total` in state. Effects trigger API calls with these params. Selectors derive the current page slice.

**Code Example:**
loadPage$ = createEffect(() => this.actions$.pipe(
  ofType(PageActions.next),
  withLatestFrom(this.store.select(selectPageParams)),
  switchMap(([_, params]) => api.get(params))
));

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q47: How do you cancel an HTTP request when the component is destroyed?

**Difficulty**: Intermediate

**Strategy:**
If using `ComponentStore`, the effect is tied to the lifecycle and cancels automatically. In global Effects, listen for a specific Cancel action dispatch in `ngOnDestroy`.

**Code Example:**
takeUntil(this.actions$.pipe(ofType(PageActions.destroyed)))

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q48: How do you manage Forms with NgRx?

**Difficulty**: Intermediate

**Strategy:**
Avoid storing every keystroke in Redux. Use local state for the form, and dispatch a single action on Submit. Or use Reactive Forms with `ngrx-forms` (if complex).

**Code Example:**
onSubmit() {
  if (form.valid) this.store.dispatch(save({ data: form.value }));
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q49: How do you use `ngrx-data`?

**Difficulty**: Advanced

**Strategy:**
`ngrx-data` automates standard CRUD. Define `EntityMetadataMap`, register it, and inject `EntityCollectionService<T>`.

**Code Example:**
const entityMetadata: EntityMetadataMap = { Hero: {} };
// Service
constructor(service: EntityCollectionService<Hero>) {
  service.getAll(); // Auto-dispatches, effects, reducer
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q50: How do you migrate from NgRx Global Store to SignalStore?

**Difficulty**: Advanced

**Strategy:**
Refactor Feature States to SignalStores. Replace Selectors with computed signals. Replace Actions/Effects with `rxMethod`. Keep Global Store for truly global data (Auth).

**Code Example:**
// Incremental adoption allowed

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

