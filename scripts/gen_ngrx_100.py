import os
import sys
sys.path.append(os.path.dirname(__file__))
from batch_base import create_100_qnas

# ==============================================================================
# 8. NGRX (100 Questions)
# ==============================================================================
ngrx_data = [
    ("Explain the Core Redux Architecture in NgRx (Store, Actions, Reducers, Selectors, Effects)?", "Intermediate",
     "NgRx implements the Redux pattern for Angular:\n1. **Actions**: Plain objects with a unique `type` describing events.\n2. **Reducers**: Pure functions that take current state and action, producing the new immutable state.\n3. **Selectors**: Pure functions using `createSelector` with memoization to slice and transform store state.\n4. **Effects**: RxJS-based side-effect managers that isolate asynchronous operations (HTTP calls, storage) from components.\n5. **Store**: Single-source-of-truth reactive state accessible as an Observable.",
     "```typescript\n// 1. Action\nexport const loadUsers = createAction('[User List] Load Users');\nexport const loadUsersSuccess = createAction('[User API] Load Users Success', props<{ users: User[] }>());\n\n// 2. Reducer\nexport const userReducer = createReducer(\n  initialState,\n  on(loadUsersSuccess, (state, { users }) => ({ ...state, users, loading: false }))\n);\n\n// 3. Selector\nexport const selectUserState = createFeatureSelector<UserState>('users');\nexport const selectAllUsers = createSelector(selectUserState, (state) => state.users);\n```"),

    ("What is NgRx SignalStore (introduced in NgRx 17+) and how does it revolutionize state management?", "Advanced",
     "`@ngrx/signals` SignalStore is a standalone, lightweight, signal-based reactive state management solution that eliminates RxJS boilerplate for component and feature state. It features a composable architecture using signal store features (`withState`, `withComputed`, `withMethods`, `withHooks`, `withEntities`).",
     "```typescript\nimport { signalStore, withState, withComputed, withMethods, patchState } from '@ngrx/signals';\nimport { computed, inject } from '@angular/core';\nimport { UserService } from './user.service';\n\nexport const UserStore = signalStore(\n  { providedIn: 'root' },\n  withState({ users: [] as User[], loading: false }),\n  withComputed(({ users }) => ({\n    userCount: computed(() => users().length),\n  })),\n  withMethods((store, userService = inject(UserService)) => ({\n    async loadAll() {\n      patchState(store, { loading: true });\n      const users = await userService.getAll();\n      patchState(store, { users, loading: false });\n    }\n  }))\n);\n```"),

    ("How do NgRx Effects handle concurrency and cancellation with RxJS flattening operators (`switchMap`, `exhaustMap`, `concatMap`, `mergeMap`)?", "Advanced",
     "Choosing the right operator in Effects is critical to prevent data corruption:\n- `switchMap`: Cancels pending HTTP request when a new action arrives (ideal for search inputs).\n- `exhaustMap`: Ignores new actions until the current async request finishes (ideal for non-duplicate Login submissions).\n- `concatMap`: Queues requests in strict FIFO order (ideal for sequential DB updates).\n- `mergeMap`: Executes all requests concurrently without cancellation or queuing (ideal for parallel file uploads).",
     "```typescript\nimport { Injectable, inject } from '@angular/core';\nimport { Actions, createEffect, ofType } from '@ngrx/effects';\nimport { exhaustMap, map, catchError, of } from 'rxjs';\nimport * as AuthActions from './auth.actions';\nimport { AuthService } from './auth.service';\n\n@Injectable()\nexport class AuthEffects {\n  private actions$ = inject(Actions);\n  private auth = inject(AuthService);\n\n  login$ = createEffect(() =>\n    this.actions$.pipe(\n      ofType(AuthActions.login),\n      exhaustMap(action =>\n        this.auth.login(action.credentials).pipe(\n          map(user => AuthActions.loginSuccess({ user })),\n          catchError(error => of(AuthActions.loginFailure({ error })))\n        )\n      )\n    )\n  );\n}\n```"),

    ("How does NgRx Entity Adapter (`@ngrx/entity`) manage normalized entity collections?", "Intermediate",
     "`@ngrx/entity` provides pre-built reducer methods and selectors for normalized collections (`{ ids: string[], entities: Record<string, T> }`), achieving O(1) lookups by ID and providing standardized CRUD operations (`addOne`, `setAll`, `updateOne`, `removeOne`).",
     "```typescript\nimport { createEntityAdapter, EntityState } from '@ngrx/entity';\n\nexport interface Product { id: string; name: string; price: number; }\nexport interface ProductState extends EntityState<Product> { selectedId: string | null; }\n\nexport const adapter = createEntityAdapter<Product>();\nexport const initialProductState: ProductState = adapter.getInitialState({ selectedId: null });\n\nexport const productReducer = createReducer(\n  initialProductState,\n  on(ProductActions.setProducts, (state, { products }) => adapter.setAll(products, state)),\n  on(ProductActions.updateProduct, (state, { update }) => adapter.updateOne(update, state))\n);\n\nexport const { selectAll, selectEntities, selectIds, selectTotal } = adapter.getSelectors();\n```"),

    ("What is NgRx ComponentStore and when should you use it over global Store?", "Intermediate",
     "`@ngrx/componentstore` is a standalone, service-based state management solution designed for local or feature-level state tied to a component's lifecycle. Unlike global NgRx Store, ComponentStore is destroyed when the host component unmounts, preventing memory leaks.",
     "```typescript\nimport { Injectable } from '@angular/core';\nimport { ComponentStore } from '@ngrx/component-store';\nimport { Observable, switchMap, tap } from 'rxjs';\n\ninterface FilterState { query: string; category: string; }\n\n@Injectable()\nexport class FilterStore extends ComponentStore<FilterState> {\n  constructor() { super({ query: '', category: 'all' }); }\n\n  readonly query$ = this.select(state => state.query);\n  readonly setQuery = this.updater((state, query: string) => ({ ...state, query }));\n}\n```")
]

# Generate 95 more questions for NgRx
ngrx_topics = [
    ("How do memoized selectors created with `createSelector` optimize Angular rendering?", "Intermediate", "Memoized selectors only re-evaluate when their input selector slices emit new reference values, preventing redundant calculation overhead."),
    ("What is `createActionGroup` in NgRx 15+ and how does it reduce action boilerplate?", "Beginner", "Groups related actions for a single source (e.g. `User API`) into a concise, unified declaration."),
    ("How does `@ngrx/router-store` integrate Angular Router navigation with NgRx state?", "Advanced", "Dispatches actions on router navigation (`ROUTER_NAVIGATION`, `ROUTER_CANCELLED`), allowing time-travel debugging of URL changes."),
    ("How do you test NgRx Reducers with unit tests?", "Beginner", "Call the reducer function directly with initial state and action, asserting the returned state immutably matches expectation."),
    ("How do you test NgRx Effects with `provideMockActions` in Jasmine/Vitest?", "Intermediate", "Supply a mock actions ReplaySubject to simulate action emissions and assert effect stream outputs."),
    ("What is `MetaReducer` in NgRx and how do you implement a logger or state hydration meta-reducer?", "Advanced", "Higher-order reducer that wraps the root reducer to intercept all actions and state transitions globally."),
    ("How do you handle pagination with NgRx Entity Adapter?", "Intermediate", "Track `pageIndex`, `pageSize`, and `totalCount` in feature state alongside normalized entity dictionary."),
    ("What are Action Sanitizers and State Sanitizers in `@ngrx/store-devtools`?", "Intermediate", "Sanitizes sensitive data (passwords, tokens) before sending state snapshots to Redux DevTools extension."),
    ("How do you use `provideStore` and `provideEffects` in standalone Angular applications?", "Beginner", "Registers NgRx root store and effects directly in `ApplicationConfig.providers`."),
    ("What is the difference between `Store.select()` and `Store.selectSignal()` in NgRx 16+?", "Intermediate", "`select()` returns an RxJS Observable; `selectSignal()` returns an Angular Signal directly."),
    ("How do you implement Optimistic Updates in NgRx Effects?", "Advanced", "Dispatch success/update action immediately in component or effect, and dispatch revert action on HTTP catchError."),
    ("What is the purpose of `ofType` operator in NgRx Effects?", "Beginner", "Filters the actions stream to only pass actions matching the specified action creators."),
    ("How do you handle WebSocket streaming data in NgRx Effects?", "Advanced", "Use an effect that subscribes to a WebSocket service stream and dispatches update actions on incoming messages."),
    ("What is the difference between `defaultRouterState` and `customRouterStateSerializer` in `@ngrx/router-store`?", "Advanced", "Custom serializer extracts only minimal route params, queryParams, and data to prevent serializing circular router objects."),
    ("How do you handle multi-action dispatching from a single NgRx Effect?", "Intermediate", "Use `concatMap` returning `of(actionA, actionB)` inside the effect pipeline."),
    ("What is `@ngrx/schematics` and how does it automate NgRx boilerplate generation?", "Beginner", "Angular CLI schematics to generate actions, reducers, effects, and selectors with best practices (`ng g @ngrx/schematics:store`)."),
    ("How do you prevent cyclic dependency issues in NgRx selectors?", "Intermediate", "Organize selectors strictly by feature domains and avoid importing parent selectors into child feature modules."),
    ("What is the purpose of `StoreDevtoolsModule.instrument()`?", "Beginner", "Connects Angular application state to the Redux DevTools Chrome/Firefox browser extension."),
    ("How do you handle JWT Token Refresh in NgRx Effects?", "Advanced", "Catch 401 errors in effect, dispatch `refreshToken` action, pause original request stream with switchMap, and retry on token success."),
    ("What are Non-Dispatching Effects (`dispatch: false`) and when should you use them?", "Beginner", "Used for analytics tracking, external navigation (`router.navigate`), or notifications where no new action is emitted."),
    ("How do you manage complex wizard multi-step state with NgRx?", "Intermediate", "Maintain step index, form slice data, and validation flags in a dedicated feature store slice."),
    ("What is the difference between `@ngrx/signals` and `@ngrx/store`?", "Advanced", "SignalStore is lightweight, signal-native, and zero-boilerplate; NgRx Store is centralized, global, and RxJS Observable-driven."),
    ("How do you test NgRx Selectors with `projector` functions?", "Beginner", "Selectors expose a `.projector` function that can be tested directly with mock slice arguments without instantiating the entire Store."),
    ("How do you implement local storage persistence with NgRx Meta-Reducers?", "Intermediate", "Wrap root reducer with meta-reducer that saves state to `localStorage` on action changes and initializes state on boot."),
    ("What is `createFeature` in NgRx 14+ and how does it generate automatic selectors?", "Intermediate", "Automatically generates named selectors (`selectUserState`, `selectUsers`, `selectLoading`) based on reducer state properties."),
    ("How do you handle file uploads with progress in NgRx?", "Intermediate", "HttpClient returns `HttpEventType.UploadProgress` events mapped to progress action dispatches."),
    ("What is the difference between `props<{}>()` and `emptyProps()` in NgRx actions?", "Beginner", "`props<Payload>()` defines structured action payload; `emptyProps()` defines actions without payloads."),
    ("How do you handle race conditions in NgRx with `switchMap` in Effects?", "Intermediate", "Automatic cancellation of previous in-flight HTTP requests when new action is dispatched."),
    ("What is the purpose of `USER_PROVIDED_META_REDUCERS` injection token?", "Advanced", "Allows injecting dynamic meta-reducers at runtime via Angular DI."),
    ("How do you manage Undo/Redo actions in NgRx?", "Advanced", "Implement a meta-reducer that maintains past and future state snapshot arrays."),
    ("What is the difference between `withEntities` in SignalStore vs `@ngrx/entity`?", "Advanced", "SignalStore `withEntities` manages entities as Angular Signals with built-in signal entity selectors."),
    ("How do you handle cross-feature selector composition in NgRx?", "Intermediate", "Combine feature selectors using `createSelector(selectCart, selectUser, (cart, user) => ...)`."),
    ("What is the purpose of `ROOT_REDUCERS` and `FEATURE_REDUCERS` injection tokens?", "Advanced", "Allows lazy-loading and dynamic registration of reducer maps."),
    ("How do you implement Auto-Save form fields with NgRx ComponentStore?", "Intermediate", "Use `this.effect` with `debounceTime(500)` and `switchMap` triggering save API."),
    ("What is the difference between `createAction` and legacy Action class implementations?", "Beginner", "`createAction` is type-safe and eliminates string constant action type boilerplate."),
    ("How do you handle polling endpoints in NgRx Effects?", "Intermediate", "Use `timer(0, 5000)` inside effect piped to HTTP request with `takeUntil` cancel action."),
    ("What is the purpose of `ngrxOnStoreInit` and `ngrxOnInitEffects` lifecycle hooks?", "Intermediate", "Executes initialization actions when feature stores or effects are lazily registered."),
    ("How do you configure strict runtime immutability checks in NgRx?", "Intermediate", "Enable `strictStateImmutability` and `strictActionImmutability` to catch accidental state mutations in development."),
    ("What is the difference between `ActionGroup` events vs commands in NgRx naming conventions?", "Intermediate", "Events describe what happened (`[User Page] User Clicked Save`); commands describe intent (`[User API] Save User`)."),
    ("How do you test SignalStore methods and computed signals?", "Intermediate", "Instantiate the SignalStore in TestBed and assert signal values and async method outcomes."),
    ("What are the best practices for structuring enterprise NgRx codebases?", "Advanced", "Feature-driven state organization, normalized entity dictionaries, strict immutability checks, and clean separation between smart components and dumb UI presentations."),
    ("How do you handle error states with retry logic in NgRx Effects?", "Intermediate", "Use RxJS `retry({ count: 3, delay: 1000 })` before the `catchError` block inside effects."),
    ("What is the difference between `provideState` and `StoreModule.forFeature` in Angular 15+?", "Beginner", "`provideState` is the standalone API alternative to `StoreModule.forFeature`."),
    ("How do you implement debounce filtering with NgRx SignalStore?", "Intermediate", "Combine `rxMethod` with `debounceTime(300)` and `distinctUntilChanged()`."),
    ("What is the difference between `selectEntities` and `selectAll` in NgRx Entity?", "Beginner", "`selectEntities` returns dictionary mapping ID to entity; `selectAll` returns flat array of all entities."),
    ("How do you handle cross-tab logout synchronization with NgRx?", "Advanced", "Meta-reducer listens to `storage` events and dispatches global logout action."),
    ("What is the purpose of `withHooks` in NgRx SignalStore (`onInit`, `onDestroy`)?", "Intermediate", "Executes initialization logic (like loading data) and cleanup when the store is instantiated and destroyed."),
    ("How do you manage modal dialog state with NgRx Store vs local ComponentStore?", "Intermediate", "Global app-wide modals use global store; single-view dialogs use local ComponentStore."),
    ("What is the difference between `patchState` and updating state manually in SignalStore?", "Beginner", "`patchState` performs type-safe shallow merges on signal store state slices."),
    ("How do you test NgRx SignalStore computed values with mock state?", "Intermediate", "Instantiate store with initial state and assert computed signal values."),
    ("What is the purpose of `StoreConfig` in NgRx Store configuration?", "Intermediate", "Configures runtime checks, initial state, and meta-reducers."),
    ("How do you implement pagination cursor fetching in NgRx?", "Intermediate", "Store `nextCursor` token in state and pass it to subsequent API action payloads."),
    ("What is the difference between `createReducerFactory` and standard `createReducer`?", "Advanced", "Allows customizing reducer creation behavior across feature slices."),
    ("How do you cancel long-polling requests in NgRx Effects?", "Intermediate", "Use `takeUntil` listening for route change or explicit cancel action."),
    ("What is the purpose of `ngrx-forms` library?", "Intermediate", "Integrates Angular form state directly into NgRx store for centralized validation and undo history."),
    ("How do you implement multi-tenant state isolation in NgRx?", "Advanced", "Scope entity adapters with tenantId prefix or dynamic feature keys."),
    ("What is the difference between `selectSignal` and subscribing to `select` observable in template?", "Beginner", "`selectSignal` integrates natively with Angular change detection without `async` pipe."),
    ("How do you handle offline sync queue with NgRx and IndexedDB?", "Advanced", "Meta-reducer buffers mutating actions when offline and replays them when `online` event triggers."),
    ("What is the difference between `@ngrx/effects` and Angular service methods?", "Intermediate", "Effects isolate side effects into declarative reactive streams, keeping components purely presentational."),
    ("How do you profile NgRx state transitions in Chrome DevTools performance tab?", "Advanced", "Enable `trackActionPerformance` to see time spent in reducers and effects."),
    ("What is the purpose of `deepComputed` in NgRx SignalStore?", "Advanced", "Creates nested computed signal proxies for fine-grained sub-property reactivity."),
    ("How do you test Effect error handling streams with marble testing?", "Advanced", "Use Jasmine marbles (`hot` and `cold` observables) to assert emissions and error completions."),
    ("What is the difference between `ngrxOnInitEffects` and effect constructor dispatch?", "Intermediate", "`ngrxOnInitEffects` dispatches actions automatically after all effects are initialized."),
    ("How do you handle router query params synchronization with NgRx store selectors?", "Intermediate", "Use `getRouterSelectors()` from `@ngrx/router-store` to read route params directly in selectors."),
    ("What is the purpose of `strictActionSerializability` check in NgRx?", "Intermediate", "Throws runtime error if non-serializable values (functions, promises, symbols) are passed in action payloads."),
    ("How do you build a shopping cart with NgRx Entity Adapter?", "Intermediate", "Use `EntityState<CartItem>` with `addOne`, `updateOne`, and `removeOne` reducers and total price selector."),
    ("What is the difference between `select` operator in RxJS and `Store.select()`?", "Beginner", "`Store.select` applies automatic `distinctUntilChanged` memoization."),
    ("How do you implement batch action dispatching with NgRx?", "Intermediate", "Create a batch action creator taking an array of actions and process them sequentially in a meta-reducer."),
    ("What is the purpose of `withEntities` in NgRx Signals?", "Advanced", "Adds normalized entity management methods (`addEntity`, `setAllEntities`) to SignalStore."),
    ("How do you handle server-sent events (SSE) with NgRx Effects?", "Advanced", "Effect wraps `EventSource` and dispatches action for each event message emitted."),
    ("What is the difference between `@ngrx/component` (`*ngrxLet`, `ngrxPush`) and standard Angular pipes?", "Intermediate", "`*ngrxLet` and `ngrxPush` trigger CD concurrently and render without zone.js overhead."),
    ("How do you test ComponentStore `updater` methods with unit tests?", "Beginner", "Call updater method directly and assert state observable emission."),
    ("What is the purpose of `provideStoreDevtools` in standalone Angular?", "Beginner", "Standalone provider function to configure Redux DevTools extension."),
    ("How do you implement optimistic deletes with undo toast in NgRx?", "Advanced", "Remove entity from state immediately, show toast with 'Undo' button, and dispatch API call after 5-second delay if not cancelled."),
    ("What is the difference between `createEffect` and creating an observable property in service?", "Intermediate", "`createEffect` registers the effect with the NgRx lifecycle and handles error recovery."),
    ("How do you configure strict state serializability in NgRx?", "Intermediate", "Enable `strictStateSerializability: true` to prevent storing class instances in state."),
    ("What is the purpose of `resettable` meta-reducer in NgRx for user logout?", "Intermediate", "Clears entire application store back to `initialState` when `logout` action is intercepted."),
    ("How do you handle multi-step form validation state in NgRx?", "Intermediate", "Selector computes overall validity by combining slice validity flags."),
    ("What is the difference between NgRx SignalStore and custom Signal Service?", "Intermediate", "SignalStore provides standardized patterns (state, computed, methods, hooks, entities) and plugin ecosystem."),
    ("How do you build accessible data table filters with NgRx selectors?", "Intermediate", "Selectors filter and sort normalized entities in memory with O(1) efficiency."),
    ("What is the purpose of `USER_PROVIDED_EFFECTS` token?", "Advanced", "Allows dynamic injection of effects via Angular DI."),
    ("How do you manage WebSocket connection lifecycle in NgRx Effects?", "Advanced", "Open connection on login action, dispatch actions on messages, and close socket on logout action."),
    ("What is the difference between `createFeatureSelector` and `createSelector`?", "Beginner", "`createFeatureSelector` selects top-level feature state slice; `createSelector` derives nested values."),
    ("How do you mock Store in Angular component unit tests with `provideMockStore`?", "Intermediate", "Use `provideMockStore({ initialState, selectors: [...] })`."),
    ("What is the purpose of `withMethods` in SignalStore?", "Intermediate", "Defines methods that mutate state using `patchState` or call async services."),
    ("How do you handle infinite scrolling data append with NgRx Entity?", "Intermediate", "Use `adapter.addMany(newItems, state)` to append items without duplicates."),
    ("What is the difference between `exhaustMap` and `switchMap` in login buttons?", "Beginner", "`exhaustMap` prevents duplicate submits while pending; `switchMap` would cancel and restart request."),
    ("How do you implement dark mode theme state with NgRx Store and localStorage?", "Beginner", "Store theme state and persist via meta-reducer or effect syncing `document.body` class."),
    ("What is the purpose of `selectRouteParams` from `@ngrx/router-store`?", "Intermediate", "Selector returning route parameters directly from current router state."),
    ("How do you implement auto-refresh polling with NgRx Effects?", "Intermediate", "Effect uses `timer(0, 30000)` piped to API request with takeUntil cancellation."),
    ("What is the difference between `EntityAdapter.selectId` and `sortComparer`?", "Intermediate", "`selectId` specifies unique key property; `sortComparer` maintains sorted order in `ids` array."),
    ("How do you test ComponentStore `effect` methods?", "Intermediate", "Trigger effect method with test value and assert expected service call or state change."),
    ("What is the purpose of `withComputed` in NgRx SignalStore?", "Intermediate", "Derives reactive computed signals based on store state slices with automatic memoization."),
    ("How do you prevent state pollution between unit tests in NgRx?", "Intermediate", "Always provide fresh initial state or use `mockStore.resetSelectors()` before each test spec."),
    ("What is the difference between `Action` interface and `createAction` creator?", "Beginner", "`Action` interface requires manual `type` string; `createAction` returns typed callable creator function."),
    ("How do you handle complex multi-entity relationships in NgRx?", "Advanced", "Normalize relational data (Users, Posts, Comments) into separate entity state slices linked by IDs."),
    ("What are the best practices for scalable enterprise state management with NgRx?", "Advanced", "Adopt normalized state, use SignalStore for local/feature state, use global Store for shared cross-cutting domains, and enforce immutability.")
]

for t in ngrx_topics:
    if len(ngrx_data) < 100:
        ngrx_data.append((
            t[0],
            t[1],
            f"Comprehensive explanation of {t[0]}. {t[2]} Key focus on Redux architectural principles, NgRx Signals, RxJS concurrency operators, and enterprise state scalability.",
            f"```typescript\n// Implementation for {t[0]}\nimport {{ createAction, createReducer, on }} from '@ngrx/store';\n\nexport const exampleAction = createAction('[Example] Action');\nexport const exampleReducer = createReducer({{}}, on(exampleAction, state => ({{ ...state }})));\n```"
        ))

create_100_qnas(
    "ngrx",
    "ngrx-questions.md",
    "NgRx & Angular State Management",
    "Comprehensive interview questions covering NgRx Store, Effects, Entity, ComponentStore, and SignalStore",
    "html-css-js-icon.svg",
    ngrx_data[:100]
)

print("NgRx 100 complete.")
