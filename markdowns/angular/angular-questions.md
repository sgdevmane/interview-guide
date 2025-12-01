<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/angular-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>Angular Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for developers</b></p>
</div>

---

## Table of Contents

1. [How do you optimize change detection in a large list of components using `OnPush` strategy?](#q1-how-do-you-optimize-change-detection-in-a-large-list-of-components-using-onpush-strategy) <span class="intermediate">Intermediate</span>
2. [How do you prevent memory leaks when subscribing to Observables in Angular components?](#q2-how-do-you-prevent-memory-leaks-when-subscribing-to-observables-in-angular-components) <span class="intermediate">Intermediate</span>
3. [How do you implement a custom form validator for a Reactive Form?](#q3-how-do-you-implement-a-custom-form-validator-for-a-reactive-form) <span class="intermediate">Intermediate</span>
4. [How do you share data between unrelated components using a Service and RxJS?](#q4-how-do-you-share-data-between-unrelated-components-using-a-service-and-rxjs) <span class="intermediate">Intermediate</span>
5. [How do you lazy load a module or standalone component in Angular Routing?](#q5-how-do-you-lazy-load-a-module-or-standalone-component-in-angular-routing) <span class="intermediate">Intermediate</span>
6. [How do you intercept HTTP requests to add an authentication token automatically?](#q6-how-do-you-intercept-http-requests-to-add-an-authentication-token-automatically) <span class="intermediate">Intermediate</span>
7. [How do you manage state in Angular using Signals (modern approach)?](#q7-how-do-you-manage-state-in-angular-using-signals-modern-approach) <span class="intermediate">Intermediate</span>
8. [How do you optimize the rendering of large lists using `@for` loop tracking?](#q8-how-do-you-optimize-the-rendering-of-large-lists-using-@for-loop-tracking) <span class="intermediate">Intermediate</span>
9. [How do you handle multiple API calls where the second call depends on the result of the first?](#q9-how-do-you-handle-multiple-api-calls-where-the-second-call-depends-on-the-result-of-the-first) <span class="intermediate">Intermediate</span>
10. [How do you dynamically create a component at runtime?](#q10-how-do-you-dynamically-create-a-component-at-runtime) <span class="intermediate">Intermediate</span>
11. [How do you protect a route from being accessed by unauthorized users?](#q11-how-do-you-protect-a-route-from-being-accessed-by-unauthorized-users) <span class="intermediate">Intermediate</span>
12. [How do you configure different environments (dev, prod) in Angular?](#q12-how-do-you-configure-different-environments-dev-prod-in-angular) <span class="intermediate">Intermediate</span>
13. [How do you create a structural directive (like `*ngIf`)?](#q13-how-do-you-create-a-structural-directive-like-*ngif) <span class="intermediate">Intermediate</span>
14. [How do you unit test a component with dependencies?](#q14-how-do-you-unit-test-a-component-with-dependencies) <span class="intermediate">Intermediate</span>
15. [How do you resolve data before a route is activated?](#q15-how-do-you-resolve-data-before-a-route-is-activated) <span class="intermediate">Intermediate</span>
16. [How do you create a custom Pipe in Angular?](#q16-how-do-you-create-a-custom-pipe-in-angular) <span class="intermediate">Intermediate</span>
17. [How do you create a custom Attribute Directive?](#q17-how-do-you-create-a-custom-attribute-directive) <span class="intermediate">Intermediate</span>
18. [How do you organize code using Angular Modules (NgModule)?](#q18-how-do-you-organize-code-using-angular-modules-ngmodule) <span class="intermediate">Intermediate</span>
19. [How do you use Content Projection (`ng-content`)?](#q19-how-do-you-use-content-projection-ng-content) <span class="intermediate">Intermediate</span>
20. [How do you access a child component or DOM element using `@ViewChild`?](#q20-how-do-you-access-a-child-component-or-dom-element-using-@viewchild) <span class="intermediate">Intermediate</span>
21. [How do you listen to DOM events on the host element using `@HostListener`?](#q21-how-do-you-listen-to-dom-events-on-the-host-element-using-@hostlistener) <span class="intermediate">Intermediate</span>
22. [How do you bind host element properties using `@HostBinding`?](#q22-how-do-you-bind-host-element-properties-using-@hostbinding) <span class="intermediate">Intermediate</span>
23. [How do you implement animations in Angular?](#q23-how-do-you-implement-animations-in-angular) <span class="intermediate">Intermediate</span>
24. [How do you make HTTP requests using `HttpClient`?](#q24-how-do-you-make-http-requests-using-httpclient) <span class="intermediate">Intermediate</span>
25. [How do you write a basic unit test for a component?](#q25-how-do-you-write-a-basic-unit-test-for-a-component) <span class="intermediate">Intermediate</span>
26. [How do you convert an Observable to a Signal and vice-versa?](#q26-how-do-you-convert-an-observable-to-a-signal-and-vice-versa) <span class="intermediate">Intermediate</span>
27. [How do you use Deferrable Views (`@defer`) to lazy load content?](#q27-how-do-you-use-deferrable-views-@defer-to-lazy-load-content) <span class="intermediate">Intermediate</span>
28. [How do you use `InjectionToken` for non-class dependencies?](#q28-how-do-you-use-injectiontoken-for-non-class-dependencies) <span class="intermediate">Intermediate</span>
29. [How do you use `useFactory` in Dependency Injection?](#q29-how-do-you-use-usefactory-in-dependency-injection) <span class="advanced">Advanced</span>
30. [How do you use `DestroyRef` for cleanup in non-component classes?](#q30-how-do-you-use-destroyref-for-cleanup-in-non-component-classes) <span class="intermediate">Intermediate</span>
31. [How do you use `ngProjectAs` to project content into a specific slot?](#q31-how-do-you-use-ngprojectas-to-project-content-into-a-specific-slot) <span class="advanced">Advanced</span>
32. [How do you dynamically render a component using `NgComponentOutlet`?](#q32-how-do-you-dynamically-render-a-component-using-ngcomponentoutlet) <span class="intermediate">Intermediate</span>
33. [What is the difference between `CanActivate` and `CanMatch` guards?](#q33-what-is-the-difference-between-canactivate-and-canmatch-guards) <span class="advanced">Advanced</span>
34. [How do you control style encapsulation using `ViewEncapsulation`?](#q34-how-do-you-control-style-encapsulation-using-viewencapsulation) <span class="intermediate">Intermediate</span>
35. [How do you use `NgZone.runOutsideAngular` to optimize performance?](#q35-how-do-you-use-ngzone.runoutsideangular-to-optimize-performance) <span class="advanced">Advanced</span>
36. [What is the difference between `mergeMap`, `concatMap`, and `exhaustMap`?](#q36-what-is-the-difference-between-mergemap-concatmap-and-exhaustmap) <span class="advanced">Advanced</span>
37. [When should you use a `ReplaySubject`?](#q37-when-should-you-use-a-replaysubject) <span class="intermediate">Intermediate</span>
38. [How do you handle errors in an Observable stream using `catchError`?](#q38-how-do-you-handle-errors-in-an-observable-stream-using-catcherror) <span class="intermediate">Intermediate</span>
39. [How do you preserve Query Parameters during navigation?](#q39-how-do-you-preserve-query-parameters-during-navigation) <span class="intermediate">Intermediate</span>
40. [How do you implement a custom `RouteReuseStrategy`?](#q40-how-do-you-implement-a-custom-routereusestrategy) <span class="advanced">Advanced</span>
41. [How do you define an NgRx Action and Reducer?](#q41-how-do-you-define-an-ngrx-action-and-reducer) <span class="advanced">Advanced</span>
42. [How do you create an NgRx Effect?](#q42-how-do-you-create-an-ngrx-effect) <span class="advanced">Advanced</span>
43. [How do you enable Client Hydration for SSR (Angular 16+)?](#q43-how-do-you-enable-client-hydration-for-ssr-angular-16+) <span class="advanced">Advanced</span>
44. [How do you use `LiveAnnouncer` for Accessibility?](#q44-how-do-you-use-liveannouncer-for-accessibility) <span class="intermediate">Intermediate</span>
45. [How do you test asynchronous code using `fakeAsync` and `tick`?](#q45-how-do-you-test-asynchronous-code-using-fakeasync-and-tick) <span class="intermediate">Intermediate</span>
46. [How do you mock HTTP requests in tests using `HttpTestingController`?](#q46-how-do-you-mock-http-requests-in-tests-using-httptestingcontroller) <span class="intermediate">Intermediate</span>
47. [How do you use `APP_INITIALIZER` to load configuration before app startup?](#q47-how-do-you-use-app_initializer-to-load-configuration-before-app-startup) <span class="advanced">Advanced</span>
48. [How do you set the page Title and Meta tags dynamically?](#q48-how-do-you-set-the-page-title-and-meta-tags-dynamically) <span class="beginner">Beginner</span>
49. [How do you use `exportAs` in a Directive?](#q49-how-do-you-use-exportas-in-a-directive) <span class="intermediate">Intermediate</span>
50. [How do you restrict Dependency Injection resolution using `@Self`, `@SkipSelf`, `@Optional`, or `@Host`?](#q50-how-do-you-restrict-dependency-injection-resolution-using-@self-@skipself-@optional-or-@host) <span class="advanced">Advanced</span>
51. [How do you handle Angular state management in large scale applications?](#q51-how-do-you-handle-angular-state-management-in-large-scale-applications) <span class="advanced">Advanced</span>
52. [How do you perform Angular data validation in microservices?](#q52-how-do-you-perform-angular-data-validation-in-microservices) <span class="beginner">Beginner</span>
53. [How do you automate Angular deployment for mobile devices?](#q53-how-do-you-automate-angular-deployment-for-mobile-devices) <span class="advanced">Advanced</span>
54. [How do you handle Angular concurrency issues in legacy systems?](#q54-how-do-you-handle-angular-concurrency-issues-in-legacy-systems) <span class="advanced">Advanced</span>
55. [How do you implement Angular caching in cloud infrastructure?](#q55-how-do-you-implement-angular-caching-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
56. [How do you manage Angular configuration for real-time systems?](#q56-how-do-you-manage-angular-configuration-for-real-time-systems) <span class="beginner">Beginner</span>
57. [How do you handle Angular internationalization (i18n) in distributed systems?](#q57-how-do-you-handle-angular-internationalization-i18n-in-distributed-systems) <span class="intermediate">Intermediate</span>
58. [How do you ensure Angular accessibility (a11y) in high-traffic sites?](#q58-how-do-you-ensure-angular-accessibility-a11y-in-high-traffic-sites) <span class="beginner">Beginner</span>
59. [How do you optimize Angular network requests in embedded systems?](#q59-how-do-you-optimize-angular-network-requests-in-embedded-systems) <span class="advanced">Advanced</span>
60. [How do you handle Angular performance optimization for production environments?](#q60-how-do-you-handle-angular-performance-optimization-for-production-environments) <span class="advanced">Advanced</span>
61. [What are the security implications of Angular in large scale applications?](#q61-what-are-the-security-implications-of-angular-in-large-scale-applications) <span class="intermediate">Intermediate</span>
62. [How do you debug Angular memory leaks in microservices?](#q62-how-do-you-debug-angular-memory-leaks-in-microservices) <span class="advanced">Advanced</span>
63. [Best practices for Angular code organization in mobile devices?](#q63-best-practices-for-angular-code-organization-in-mobile-devices) <span class="beginner">Beginner</span>
64. [How do you implement Angular error handling for legacy systems?](#q64-how-do-you-implement-angular-error-handling-for-legacy-systems) <span class="intermediate">Intermediate</span>
65. [How do you test Angular functionality in cloud infrastructure?](#q65-how-do-you-test-angular-functionality-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
66. [How do you handle Angular state management in real-time systems?](#q66-how-do-you-handle-angular-state-management-in-real-time-systems) <span class="advanced">Advanced</span>
67. [How do you perform Angular data validation in distributed systems?](#q67-how-do-you-perform-angular-data-validation-in-distributed-systems) <span class="beginner">Beginner</span>
68. [How do you automate Angular deployment for high-traffic sites?](#q68-how-do-you-automate-angular-deployment-for-high-traffic-sites) <span class="advanced">Advanced</span>
69. [How do you handle Angular concurrency issues in embedded systems?](#q69-how-do-you-handle-angular-concurrency-issues-in-embedded-systems) <span class="advanced">Advanced</span>
70. [How do you implement Angular caching in production environments?](#q70-how-do-you-implement-angular-caching-in-production-environments) <span class="intermediate">Intermediate</span>
71. [How do you manage Angular configuration for large scale applications?](#q71-how-do-you-manage-angular-configuration-for-large-scale-applications) <span class="beginner">Beginner</span>
72. [How do you handle Angular internationalization (i18n) in microservices?](#q72-how-do-you-handle-angular-internationalization-i18n-in-microservices) <span class="intermediate">Intermediate</span>
73. [How do you ensure Angular accessibility (a11y) in mobile devices?](#q73-how-do-you-ensure-angular-accessibility-a11y-in-mobile-devices) <span class="beginner">Beginner</span>
74. [How do you optimize Angular network requests in legacy systems?](#q74-how-do-you-optimize-angular-network-requests-in-legacy-systems) <span class="advanced">Advanced</span>
75. [How do you handle Angular performance optimization for cloud infrastructure?](#q75-how-do-you-handle-angular-performance-optimization-for-cloud-infrastructure) <span class="advanced">Advanced</span>
76. [What are the security implications of Angular in real-time systems?](#q76-what-are-the-security-implications-of-angular-in-real-time-systems) <span class="intermediate">Intermediate</span>
77. [How do you debug Angular memory leaks in distributed systems?](#q77-how-do-you-debug-angular-memory-leaks-in-distributed-systems) <span class="advanced">Advanced</span>
78. [Best practices for Angular code organization in high-traffic sites?](#q78-best-practices-for-angular-code-organization-in-high-traffic-sites) <span class="beginner">Beginner</span>
79. [How do you implement Angular error handling for embedded systems?](#q79-how-do-you-implement-angular-error-handling-for-embedded-systems) <span class="intermediate">Intermediate</span>
80. [How do you test Angular functionality in production environments?](#q80-how-do-you-test-angular-functionality-in-production-environments) <span class="intermediate">Intermediate</span>
81. [How do you handle Angular state management in large scale applications?](#q81-how-do-you-handle-angular-state-management-in-large-scale-applications) <span class="advanced">Advanced</span>
82. [How do you perform Angular data validation in microservices?](#q82-how-do-you-perform-angular-data-validation-in-microservices) <span class="beginner">Beginner</span>
83. [How do you automate Angular deployment for mobile devices?](#q83-how-do-you-automate-angular-deployment-for-mobile-devices) <span class="advanced">Advanced</span>
84. [How do you handle Angular concurrency issues in legacy systems?](#q84-how-do-you-handle-angular-concurrency-issues-in-legacy-systems) <span class="advanced">Advanced</span>
85. [How do you implement Angular caching in cloud infrastructure?](#q85-how-do-you-implement-angular-caching-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
86. [How do you manage Angular configuration for real-time systems?](#q86-how-do-you-manage-angular-configuration-for-real-time-systems) <span class="beginner">Beginner</span>
87. [How do you handle Angular internationalization (i18n) in distributed systems?](#q87-how-do-you-handle-angular-internationalization-i18n-in-distributed-systems) <span class="intermediate">Intermediate</span>
88. [How do you ensure Angular accessibility (a11y) in high-traffic sites?](#q88-how-do-you-ensure-angular-accessibility-a11y-in-high-traffic-sites) <span class="beginner">Beginner</span>
89. [How do you optimize Angular network requests in embedded systems?](#q89-how-do-you-optimize-angular-network-requests-in-embedded-systems) <span class="advanced">Advanced</span>
90. [How do you handle Angular performance optimization for production environments?](#q90-how-do-you-handle-angular-performance-optimization-for-production-environments) <span class="advanced">Advanced</span>
91. [What are the security implications of Angular in large scale applications?](#q91-what-are-the-security-implications-of-angular-in-large-scale-applications) <span class="intermediate">Intermediate</span>
92. [How do you debug Angular memory leaks in microservices?](#q92-how-do-you-debug-angular-memory-leaks-in-microservices) <span class="advanced">Advanced</span>
93. [Best practices for Angular code organization in mobile devices?](#q93-best-practices-for-angular-code-organization-in-mobile-devices) <span class="beginner">Beginner</span>
94. [How do you implement Angular error handling for legacy systems?](#q94-how-do-you-implement-angular-error-handling-for-legacy-systems) <span class="intermediate">Intermediate</span>
95. [How do you test Angular functionality in cloud infrastructure?](#q95-how-do-you-test-angular-functionality-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
96. [How do you handle Angular state management in real-time systems?](#q96-how-do-you-handle-angular-state-management-in-real-time-systems) <span class="advanced">Advanced</span>
97. [How do you perform Angular data validation in distributed systems?](#q97-how-do-you-perform-angular-data-validation-in-distributed-systems) <span class="beginner">Beginner</span>
98. [How do you automate Angular deployment for high-traffic sites?](#q98-how-do-you-automate-angular-deployment-for-high-traffic-sites) <span class="advanced">Advanced</span>
99. [How do you handle Angular concurrency issues in embedded systems?](#q99-how-do-you-handle-angular-concurrency-issues-in-embedded-systems) <span class="advanced">Advanced</span>
100. [How do you implement Angular caching in production environments?](#q100-how-do-you-implement-angular-caching-in-production-environments) <span class="intermediate">Intermediate</span>

---

### Q1: How do you optimize change detection in a large list of components using `OnPush` strategy?

**Difficulty**: Intermediate

**Strategy:**
By default, Angular uses the `Default` change detection strategy, which checks every component in the tree on every event. 
1. Set `changeDetection: ChangeDetectionStrategy.OnPush` in the component decorator.
2. This tells Angular to only check the component if:
    - Input reference changes (immutability is key).
    - An event originated from the component or its children.
    - `markForCheck()` is manually called.
    - An async pipe emits a new value.

**Code Example:**
```typescript
import { Component, ChangeDetectionStrategy, Input } from '@angular/core';

@Component({
  selector: 'app-item',
  template: `<div>{{ data.name }}</div>`,
  changeDetection: ChangeDetectionStrategy.OnPush // Optimization
})
export class ItemComponent {
  @Input() data: { name: string };
}

// Parent usage: ensure new reference is created for updates
// this.items[0] = { ...this.items[0], name: 'New Name' };
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q2: How do you prevent memory leaks when subscribing to Observables in Angular components?

**Difficulty**: Intermediate

**Strategy:**
Manual subscriptions (`.subscribe()`) inside components must be unsubscribed when the component is destroyed.
1. **Async Pipe:** The best way is to use `| async` in the template, which handles subscription/unsubscription automatically.
2. **takeUntil / takeUntilDestroyed:** Use operators to complete the stream.
3. **Subscription.add:** Manually collect subscriptions and unsubscribe in `ngOnDestroy`.

**Code Example:**
```typescript
import { Component, DestroyRef, inject } from '@angular/core';
import { takeUntilDestroyed } from '@angular/core/rxjs-interop';
import { interval } from 'rxjs';

@Component({ ... })
export class TimerComponent {
  private destroyRef = inject(DestroyRef);

  constructor() {
    interval(1000).pipe(
      takeUntilDestroyed(this.destroyRef) // Auto-cleanup (Angular 16+)
    ).subscribe(console.log);
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q3: How do you implement a custom form validator for a Reactive Form?

**Difficulty**: Intermediate

**Strategy:**
A validator is a function that receives a `AbstractControl` and returns `ValidationErrors | null`.
1. Define a function or factory function.
2. Check the control's value.
3. Return null if valid, or an object `{ errorName: true }` if invalid.

**Code Example:**
```typescript
import { AbstractControl, ValidationErrors, ValidatorFn } from '@angular/forms';

export function forbiddenNameValidator(nameRe: RegExp): ValidatorFn {
  return (control: AbstractControl): ValidationErrors | null => {
    const forbidden = nameRe.test(control.value);
    return forbidden ? { forbiddenName: { value: control.value } } : null;
  };
}

// Usage in FormGroup
// name: ['', [Validators.required, forbiddenNameValidator(/admin/i)]]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q4: How do you share data between unrelated components using a Service and RxJS?

**Difficulty**: Intermediate

**Strategy:**
Use a singleton service with a `BehaviorSubject` (or `ReplaySubject`) to hold state.
1. Create a private `BehaviorSubject` to hold the current value.
2. Expose it as an `Observable` (using `.asObservable()`) for components to subscribe to.
3. Provide a method to update the value.

**Code Example:**
```typescript
import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class DataService {
  private messageSource = new BehaviorSubject<string>('Default Message');
  currentMessage = this.messageSource.asObservable();

  changeMessage(message: string) {
    this.messageSource.next(message);
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q5: How do you lazy load a module or standalone component in Angular Routing?

**Difficulty**: Intermediate

**Strategy:**
Lazy loading reduces the initial bundle size by loading code only when requested.
1. Use `loadChildren` (for modules) or `loadComponent` (for standalone components) in the route definition.
2. Use the dynamic import syntax `() => import(...)`.

**Code Example:**
```typescript
import { Routes } from '@angular/router';

export const routes: Routes = [
  {
    path: 'admin',
    loadComponent: () => import('./admin/admin.component').then(m => m.AdminComponent)
  },
  {
    path: 'users',
    loadChildren: () => import('./users/users.routes').then(m => m.USER_ROUTES)
  }
];
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q6: How do you intercept HTTP requests to add an authentication token automatically?

**Difficulty**: Intermediate

**Strategy:**
Use an `HttpInterceptor` (functional interceptor in newer Angular) to modify outgoing requests.
1. Define an interceptor function.
2. Clone the request and add the `Authorization` header.
3. Pass the request to `next`.
4. Register it in `provideHttpClient(withInterceptors([...]))`.

**Code Example:**
```typescript
import { HttpInterceptorFn } from '@angular/common/http';

export const authInterceptor: HttpInterceptorFn = (req, next) => {
  const authToken = localStorage.getItem('token');
  
  if (authToken) {
    const authReq = req.clone({
      setHeaders: { Authorization: `Bearer ${authToken}` }
    });
    return next(authReq);
  }
  
  return next(req);
};

// In app.config.ts
// providers: [provideHttpClient(withInterceptors([authInterceptor]))]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q7: How do you manage state in Angular using Signals (modern approach)?

**Difficulty**: Intermediate

**Strategy:**
Signals provide fine-grained reactivity without RxJS overhead for synchronous state.
1. Use `signal()` to create writable state.
2. Use `computed()` to derive values.
3. Use `effect()` to run side effects when signals change.

**Code Example:**
```typescript
import { Component, signal, computed, effect } from '@angular/core';

@Component({ ... })
export class CounterComponent {
  count = signal(0);
  doubleCount = computed(() => this.count() * 2);

  constructor() {
    effect(() => {
      console.log(`Count changed to: ${this.count()}`);
    });
  }

  increment() {
    this.count.update(n => n + 1);
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q8: How do you optimize the rendering of large lists using `@for` loop tracking?

**Difficulty**: Intermediate

**Strategy:**
The built-in `@for` block (Angular 17+) requires a `track` expression.
1. Always provide a unique identifier for the `track` expression (e.g., `item.id`).
2. This allows Angular to identify which items moved, were added, or removed, minimizing DOM operations.

**Code Example:**
```typescript
@Component({
  template: `
    <ul>
      @for (user of users; track user.id) {
        <li>{{ user.name }}</li>
      } @empty {
        <li>No users found</li>
      }
    </ul>
  `
})
export class UserListComponent {
  users = [{id: 1, name: 'Alice'}, {id: 2, name: 'Bob'}];
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q9: How do you handle multiple API calls where the second call depends on the result of the first?

**Difficulty**: Intermediate

**Strategy:**
Use the RxJS `switchMap` (or `mergeMap`/`concatMap`) operator to chain Observables.
1. Subscribe to the first Observable.
2. Inside the pipe, map to the second Observable using `switchMap`.
3. `switchMap` automatically unsubscribes from the inner Observable if a new value arrives (cancelling pending requests).

**Code Example:**
```typescript
import { switchMap } from 'rxjs/operators';

this.route.params.pipe(
  switchMap(params => this.apiService.getUser(params['id']))
).subscribe(user => {
  this.user = user;
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q10: How do you dynamically create a component at runtime?

**Difficulty**: Intermediate

**Strategy:**
Use `ViewContainerRef` to create components dynamically.
1. Inject `ViewContainerRef` where you want to insert the component.
2. Call `createComponent` on the container.
3. Set properties on the component instance.

**Code Example:**
```typescript
import { Component, ViewChild, ViewContainerRef } from '@angular/core';
import { AlertComponent } from './alert.component';

@Component({ ... })
export class HostComponent {
  @ViewChild('container', { read: ViewContainerRef }) vcr!: ViewContainerRef;

  loadAlert() {
    this.vcr.clear();
    const ref = this.vcr.createComponent(AlertComponent);
    ref.instance.message = 'Dynamic Alert!';
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q11: How do you protect a route from being accessed by unauthorized users?

**Difficulty**: Intermediate

**Strategy:**
Use Route Guards (functional guards in modern Angular).
1. Create a `CanActivateFn`.
2. Check authentication state (e.g., via a Service).
3. Return `true` if allowed, or `UrlTree` (redirect) if denied.

**Code Example:**
```typescript
import { CanActivateFn, Router } from '@angular/router';
import { inject } from '@angular/core';
import { AuthService } from './auth.service';

export const authGuard: CanActivateFn = (route, state) => {
  const authService = inject(AuthService);
  const router = inject(Router);

  return authService.isLoggedIn() ? true : router.parseUrl('/login');
};

// Usage in Routes:
// { path: 'dashboard', canActivate: [authGuard], ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q12: How do you configure different environments (dev, prod) in Angular?

**Difficulty**: Intermediate

**Strategy:**
Angular uses environment files (e.g., `environment.ts`, `environment.prod.ts`) and build configurations.
1. Define variables in `environment.ts`.
2. In `angular.json`, under `configurations`, replace the file for `production` build.
3. Import `environment` in your code.

**Code Example:**
```typescript
// environment.ts
export const environment = {
  production: false,
  apiUrl: 'http://localhost:3000'
};

// environment.prod.ts
export const environment = {
  production: true,
  apiUrl: 'https://api.myapp.com'
};

// Service
import { environment } from '../environments/environment';
http.get(environment.apiUrl + '/users');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q13: How do you create a structural directive (like `*ngIf`)?

**Difficulty**: Intermediate

**Strategy:**
Structural directives change the DOM layout by adding/removing elements.
1. Inject `TemplateRef` (the content) and `ViewContainerRef` (the location).
2. Use `createEmbeddedView` to show content or `clear` to remove it.
3. Use a setter `@Input` to trigger updates.

**Code Example:**
```typescript
import { Directive, Input, TemplateRef, ViewContainerRef } from '@angular/core';

@Directive({ selector: '[appDelay]' })
export class DelayDirective {
  constructor(
    private templateRef: TemplateRef<any>,
    private viewContainer: ViewContainerRef
  ) {}

  @Input() set appDelay(time: number) {
    setTimeout(() => {
      this.viewContainer.createEmbeddedView(this.templateRef);
    }, time);
  }
}
// Usage: <div *appDelay="1000">Shows after 1s</div>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q14: How do you unit test a component with dependencies?

**Difficulty**: Intermediate

**Strategy:**
Use `TestBed` to configure the testing module and provide mocks.
1. Configure `TestBed.configureTestingModule`.
2. Provide mock services using `{ provide: Service, useValue: mockService }`.
3. Compile components.

**Code Example:**
```typescript
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { UserComponent } from './user.component';
import { UserService } from './user.service';

describe('UserComponent', () => {
  let component: UserComponent;
  let fixture: ComponentFixture<UserComponent>;
  const mockUserService = { getUsers: () => of([]) };

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [UserComponent],
      providers: [{ provide: UserService, useValue: mockUserService }]
    }).compileComponents();

    fixture = TestBed.createComponent(UserComponent);
    component = fixture.componentInstance;
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q15: How do you resolve data before a route is activated?

**Difficulty**: Intermediate

**Strategy:**
Use a `ResolveFn` to fetch data before the route component is rendered.
1. Define a resolver function.
2. Assign it to the `resolve` property in the route definition.
3. Access data via `ActivatedRoute.snapshot.data` or `@Input` with `withComponentInputBinding()`.

**Code Example:**
```typescript
import { ResolveFn } from '@angular/router';

export const userResolver: ResolveFn<User> = (route, state) => {
  return inject(UserService).getUser(route.paramMap.get('id')!);
};

// Route config
{
  path: 'user/:id',
  component: UserComponent,
  resolve: { user: userResolver }
}

// Component (with input binding)
@Input() user!: User;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q16: How do you create a custom Pipe in Angular?

**Difficulty**: Intermediate

**Strategy:**
Implement the `PipeTransform` interface. Decorate the class with `@Pipe`. The `transform` method takes the value and optional arguments.

**Code Example:**
```typescript
import { Pipe, PipeTransform } from '@angular/core';

@Pipe({ name: 'exponentialStrength', standalone: true })
export class ExponentialStrengthPipe implements PipeTransform {
  transform(value: number, exponent = 1): number {
    return Math.pow(value, exponent);
  }
}

// Usage: {{ 2 | exponentialStrength: 10 }}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q17: How do you create a custom Attribute Directive?

**Difficulty**: Intermediate

**Strategy:**
Use `@Directive`. Inject `ElementRef` to access the DOM element. Use `@HostListener` to handle events.

**Code Example:**
```typescript
@Directive({ selector: '[appHighlight]', standalone: true })
export class HighlightDirective {
  constructor(private el: ElementRef) {}

  @HostListener('mouseenter') onMouseEnter() {
    this.highlight('yellow');
  }

  @HostListener('mouseleave') onMouseLeave() {
    this.highlight('');
  }

  private highlight(color: string) {
    this.el.nativeElement.style.backgroundColor = color;
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q18: How do you organize code using Angular Modules (NgModule)?

**Difficulty**: Intermediate

**Strategy:**
Use `@NgModule` to group components, directives, and pipes. Define `declarations` (components), `imports` (other modules), `providers` (services), and `exports` (public API). *Note: Standalone components are preferred in modern Angular.*

**Code Example:**
```typescript
@NgModule({
  declarations: [FeatureComponent],
  imports: [CommonModule],
  exports: [FeatureComponent]
})
export class FeatureModule {}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q19: How do you use Content Projection (`ng-content`)?

**Difficulty**: Intermediate

**Strategy:**
Use `<ng-content>` in the child component's template to insert content provided by the parent. Use `select` attribute for multi-slot projection.

**Code Example:**
```typescript
<!-- Child -->
<div class="header">
  <ng-content select="[header]"></ng-content>
</div>
<div class="body">
  <ng-content></ng-content>
</div>

<!-- Parent -->
<app-child>
  <h1 header>Title</h1>
  <p>Main content</p>
</app-child>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q20: How do you access a child component or DOM element using `@ViewChild`?

**Difficulty**: Intermediate

**Strategy:**
Use `@ViewChild` to query for a component, directive, or template reference variable (`#ref`). Access it in `ngAfterViewInit`.

**Code Example:**
```typescript
@Component({ template: '<input #myInput>' })
export class MyComponent implements AfterViewInit {
  @ViewChild('myInput') input!: ElementRef;

  ngAfterViewInit() {
    this.input.nativeElement.focus();
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q21: How do you listen to DOM events on the host element using `@HostListener`?

**Difficulty**: Intermediate

**Strategy:**
Decorate a method with `@HostListener('eventName', ['$event'])`. It binds the DOM event to the method.

**Code Example:**
```typescript
@HostListener('click', ['$event'])
onClick(e: Event) {
  alert('Host element clicked!');
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q22: How do you bind host element properties using `@HostBinding`?

**Difficulty**: Intermediate

**Strategy:**
Decorate a property with `@HostBinding('attr.class')` or `style.color`. It updates the host element when the property changes.

**Code Example:**
```typescript
@HostBinding('class.active') isActive = false;

@HostListener('click') toggle() {
  this.isActive = !this.isActive;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q23: How do you implement animations in Angular?

**Difficulty**: Intermediate

**Strategy:**
Use `BrowserAnimationsModule` (or `provideAnimations`). Define animations in the component metadata using `trigger`, `state`, `style`, `transition`, and `animate`.

**Code Example:**
```typescript
@Component({
  animations: [
    trigger('openClose', [
      state('open', style({ height: '200px', opacity: 1 })),
      state('closed', style({ height: '0px', opacity: 0.5 })),
      transition('open <=> closed', [animate('0.5s')])
    ])
  ]
})
export class AnimationComponent {
  isOpen = true;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q24: How do you make HTTP requests using `HttpClient`?

**Difficulty**: Intermediate

**Strategy:**
Inject `HttpClient`. Use methods like `get`, `post`, `put`, `delete`. They return Observables. Subscribe to them to trigger the request.

**Code Example:**
```typescript
constructor(private http: HttpClient) {}

getData() {
  return this.http.get<User[]>('https://api.example.com/users');
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q25: How do you write a basic unit test for a component?

**Difficulty**: Intermediate

**Strategy:**
Use Jasmine/Karma (default). Describe the suite, setup `TestBed`, create component fixture, and write expectations.

**Code Example:**
```typescript
it('should have title', () => {
  const fixture = TestBed.createComponent(AppComponent);
  const app = fixture.componentInstance;
  expect(app.title).toEqual('my-app');
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q26: How do you convert an Observable to a Signal and vice-versa?

**Difficulty**: Intermediate

**Strategy:**
Use the `toSignal` and `toObservable` functions from `@angular/core/rxjs-interop`.

**Code Example:**
import { toSignal, toObservable } from '@angular/core/rxjs-interop';

// Observable to Signal
const count = toSignal(this.count$, { initialValue: 0 });

// Signal to Observable
const count$ = toObservable(this.count);

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q27: How do you use Deferrable Views (`@defer`) to lazy load content?

**Difficulty**: Intermediate

**Strategy:**
Use the `@defer` block to delay loading a dependency (component, pipe, etc.) until a trigger condition is met (e.g., `on viewport`).

**Code Example:**
@defer (on viewport) {
  <large-component />
} @placeholder {
  <div>Loading...</div>
} @loading (minimum 1s) {
  <div>Spinner...</div>
} @error {
  <div>Failed to load</div>
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q28: How do you use `InjectionToken` for non-class dependencies?

**Difficulty**: Intermediate

**Strategy:**
Use `InjectionToken` to inject simple values (config objects, strings) or interfaces that don't have a runtime representation.

**Code Example:**
import { InjectionToken, Inject } from '@angular/core';

export const API_URL = new InjectionToken<string>('API_URL');

@Component({
  providers: [{ provide: API_URL, useValue: 'https://api.com' }]
})
export class ApiService {
  constructor(@Inject(API_URL) public url: string) {}
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q29: How do you use `useFactory` in Dependency Injection?

**Difficulty**: Advanced

**Strategy:**
Use `useFactory` when the dependency creation involves logic or depends on other services (using `deps`).

**Code Example:**
const loggerFactory = (config: AppConfig) => {
  return config.isDev ? new ConsoleLogger() : new FileLogger();
};

providers: [
  {
    provide: LoggerService,
    useFactory: loggerFactory,
    deps: [AppConfig]
  }
]

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q30: How do you use `DestroyRef` for cleanup in non-component classes?

**Difficulty**: Intermediate

**Strategy:**
`DestroyRef` allows you to register cleanup callbacks in any injectable context (Services, Directives, Pipes) without implementing `OnDestroy`.

**Code Example:**
import { Injectable, DestroyRef, inject } from '@angular/core';

@Injectable()
export class MyService {
  private destroyRef = inject(DestroyRef);

  constructor() {
    const sub = someObservable.subscribe();
    
    this.destroyRef.onDestroy(() => {
      sub.unsubscribe();
    });
  }
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q31: How do you use `ngProjectAs` to project content into a specific slot?

**Difficulty**: Advanced

**Strategy:**
Use `ngProjectAs` on an element to make it match a specific `ng-content` selector, even if the element tag itself doesn't match.

**Code Example:**
<!-- Child Template -->
<ng-content select="[header]"></ng-content>

<!-- Parent Usage -->
<app-card>
  <!-- Projects into [header] slot despite being a div -->
  <div ngProjectAs="[header]">Custom Header</div>
</app-card>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q32: How do you dynamically render a component using `NgComponentOutlet`?

**Difficulty**: Intermediate

**Strategy:**
Use the `*ngComponentOutlet` directive to render a component class dynamically in the template.

**Code Example:**
@Component({
  template: `<ng-container *ngComponentOutlet="dynamicComponent"></ng-container>`
})
export class HostComponent {
  dynamicComponent = UserProfileComponent;
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q33: What is the difference between `CanActivate` and `CanMatch` guards?

**Difficulty**: Advanced

**Strategy:**
`CanActivate` checks if a user can enter a route. `CanMatch` checks if the route definition matches at all; if false, the router continues matching other routes (useful for feature flagging or role-based route loading).

**Code Example:**
const adminRoute: Route = {
  path: 'admin',
  loadChildren: () => import('./admin/routes'),
  canMatch: [() => inject(AuthService).isAdmin()]
};

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q34: How do you control style encapsulation using `ViewEncapsulation`?

**Difficulty**: Intermediate

**Strategy:**
`Emulated` (default) scopes styles via attributes. `ShadowDom` uses native Shadow DOM. `None` makes styles global.

**Code Example:**
import { ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'app-global-widget',
  template: `<h1>Global Styles</h1>`,
  styles: [`h1 { color: red; }`],
  encapsulation: ViewEncapsulation.None
})
export class WidgetComponent {}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q35: How do you use `NgZone.runOutsideAngular` to optimize performance?

**Difficulty**: Advanced

**Strategy:**
Run heavy tasks or frequent events (like scroll/mousemove) outside Angular's zone to prevent triggering change detection on every event.

**Code Example:**
constructor(private ngZone: NgZone) {}

ngOnInit() {
  this.ngZone.runOutsideAngular(() => {
    window.addEventListener('scroll', () => {
      // Heavy calculation
      // Manually re-enter zone only if UI update is needed
      if (condition) {
        this.ngZone.run(() => this.updateUI());
      }
    });
  });
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q36: What is the difference between `mergeMap`, `concatMap`, and `exhaustMap`?

**Difficulty**: Advanced

**Strategy:**
`mergeMap`: Parallel execution (good for independent requests). `concatMap`: Serial execution (wait for previous to complete, good for order). `exhaustMap`: Ignore new emissions while inner observable is active (good for login buttons).

**Code Example:**
// exhaustMap ignores clicks while request is pending
fromEvent(button, 'click').pipe(
  exhaustMap(() => this.http.post('/login', {}))
).subscribe();

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q37: When should you use a `ReplaySubject`?

**Difficulty**: Intermediate

**Strategy:**
Use `ReplaySubject` when late subscribers need access to previously emitted values (buffer size determines how many).

**Code Example:**
const subject = new ReplaySubject<number>(2); // Buffer last 2 values

subject.next(1);
subject.next(2);
subject.next(3);

// Subscriber gets 2 and 3 immediately
subject.subscribe(console.log);

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q38: How do you handle errors in an Observable stream using `catchError`?

**Difficulty**: Intermediate

**Strategy:**
Use `catchError` to intercept errors. Return a replacement Observable (like `EMPTY` or default value) or re-throw.

**Code Example:**
this.http.get('/data').pipe(
  catchError(error => {
    console.error('Error occurred', error);
    return of([]); // Return empty array on failure
  })
).subscribe();

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q39: How do you preserve Query Parameters during navigation?

**Difficulty**: Intermediate

**Strategy:**
Use `queryParamsHandling: 'preserve'` or `'merge'` in `router.navigate` or `routerLink`.

**Code Example:**
// Merge new params with existing ones
this.router.navigate(['/search'], {
  queryParams: { page: 2 },
  queryParamsHandling: 'merge'
});

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q40: How do you implement a custom `RouteReuseStrategy`?

**Difficulty**: Advanced

**Strategy:**
Implement `RouteReuseStrategy` to control when routes should be detached (cached) and re-attached (restored) instead of destroyed.

**Code Example:**
export class CustomStrategy implements RouteReuseStrategy {
  shouldDetach(route: ActivatedRouteSnapshot): boolean {
    return route.data['reuse']; // Cache if route data says so
  }
  store(route: ActivatedRouteSnapshot, handle: DetachedRouteHandle): void {
    // Store handle
  }
  // ... implement other methods
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q41: How do you define an NgRx Action and Reducer?

**Difficulty**: Advanced

**Strategy:**
Use `createAction` to define the event and `createReducer` to define state transitions.

**Code Example:**
import { createAction, props, createReducer, on } from '@ngrx/store';

export const increment = createAction('[Counter] Increment');
export const reset = createAction('[Counter] Reset', props<{ count: number }>());

export const counterReducer = createReducer(
  0,
  on(increment, (state) => state + 1),
  on(reset, (state, { count }) => count)
);

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q42: How do you create an NgRx Effect?

**Difficulty**: Advanced

**Strategy:**
Effects handle side effects (API calls). They listen for actions and dispatch new actions.

**Code Example:**
loadMovies$ = createEffect(() => this.actions$.pipe(
  ofType('[Movies] Load'),
  mergeMap(() => this.moviesService.getAll().pipe(
    map(movies => ({ type: '[Movies] Load Success', payload: movies })),
    catchError(() => of({ type: '[Movies] Load Failed' }))
  ))
));

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q43: How do you enable Client Hydration for SSR (Angular 16+)?

**Difficulty**: Advanced

**Strategy:**
Add `provideClientHydration()` to the app config. This reuses the server-rendered DOM instead of destroying and re-creating it.

**Code Example:**
// app.config.ts
import { provideClientHydration } from '@angular/platform-browser';

export const appConfig: ApplicationConfig = {
  providers: [
    provideClientHydration()
  ]
};

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q44: How do you use `LiveAnnouncer` for Accessibility?

**Difficulty**: Intermediate

**Strategy:**
Use `LiveAnnouncer` from `@angular/cdk/a11y` to announce messages to screen readers dynamically.

**Code Example:**
import { LiveAnnouncer } from '@angular/cdk/a11y';

constructor(private announcer: LiveAnnouncer) {}

announce() {
  this.announcer.announce('Operation successful');
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q45: How do you test asynchronous code using `fakeAsync` and `tick`?

**Difficulty**: Intermediate

**Strategy:**
Wrap the test in `fakeAsync`. Use `tick(ms)` to simulate time passage for `setTimeout` or timers.

**Code Example:**
it('should update after delay', fakeAsync(() => {
  component.updateLater(); // contains setTimeout 1000ms
  tick(1000);
  fixture.detectChanges();
  expect(component.value).toBe('Updated');
}));

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q46: How do you mock HTTP requests in tests using `HttpTestingController`?

**Difficulty**: Intermediate

**Strategy:**
Inject `HttpTestingController`, expect a request with `expectOne`, and provide a dummy response with `flush`.

**Code Example:**
it('should fetch users', () => {
  service.getUsers().subscribe(users => expect(users.length).toBe(1));

  const req = httpMock.expectOne('/api/users');
  expect(req.request.method).toBe('GET');
  req.flush([{ id: 1, name: 'John' }]);
});

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q47: How do you use `APP_INITIALIZER` to load configuration before app startup?

**Difficulty**: Advanced

**Strategy:**
Provide `APP_INITIALIZER` with a factory function that returns a Promise (or Observable). The app waits for it to resolve.

**Code Example:**
{
  provide: APP_INITIALIZER,
  useFactory: (config: ConfigService) => () => config.load(),
  deps: [ConfigService],
  multi: true
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q48: How do you set the page Title and Meta tags dynamically?

**Difficulty**: Beginner

**Strategy:**
Inject `Title` and `Meta` services from `@angular/platform-browser`.

**Code Example:**
constructor(private title: Title, private meta: Meta) {
  this.title.setTitle('My Page');
  this.meta.updateTag({ name: 'description', content: 'Angular Guide' });
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q49: How do you use `exportAs` in a Directive?

**Difficulty**: Intermediate

**Strategy:**
`exportAs` allows the directive instance to be assigned to a template variable.

**Code Example:**
@Directive({
  selector: '[appTooltip]',
  exportAs: 'tooltip'
})
export class TooltipDirective {
  show() { ... }
}

// Usage
<div appTooltip #t="tooltip"></div>
<button (click)="t.show()">Show Tooltip</button>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q50: How do you restrict Dependency Injection resolution using `@Self`, `@SkipSelf`, `@Optional`, or `@Host`?

**Difficulty**: Advanced

**Strategy:**
- `@Self`: Look only in this component.
- `@SkipSelf`: Start looking in the parent.
- `@Host`: Stop looking at the host component.
- `@Optional`: Don't throw if not found.

**Code Example:**
constructor(@Optional() @SkipSelf() private parentService: MyService) {
  if (parentService) {
    // Service found in parent
  }
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---


### Q51: How do you handle Angular state management in large scale applications?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```javascript
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q52: How do you perform Angular data validation in microservices?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```javascript
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q53: How do you automate Angular deployment for mobile devices?

**Difficulty**: Advanced

**Strategy**:
Use CI/CD pipelines. Dockerize the application. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
steps:
  - run: npm test
  - run: docker build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q54: How do you handle Angular concurrency issues in legacy systems?

**Difficulty**: Advanced

**Strategy**:
Use locks, queues, or atomic operations. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
await mutex.runExclusive(async () => {
  // critical section
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q55: How do you implement Angular caching in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Use Redis or in-memory LRU caches. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const cache = new Map();
if (cache.has(key)) return cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q56: How do you manage Angular configuration for real-time systems?

**Difficulty**: Beginner

**Strategy**:
Use environment variables or config files. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const config = process.env.CONFIG || 'default';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q57: How do you handle Angular internationalization (i18n) in distributed systems?

**Difficulty**: Intermediate

**Strategy**:
Use i18n libraries. Extract strings to resource files.

**Code Example**:
```javascript
t('welcome_message')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q58: How do you ensure Angular accessibility (a11y) in high-traffic sites?

**Difficulty**: Beginner

**Strategy**:
Use semantic HTML and ARIA roles. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
<button aria-label="Close">X</button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q59: How do you optimize Angular network requests in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use batching, debouncing, or GraphQL. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
debounce(() => fetch(), 300);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q60: How do you handle Angular performance optimization for production environments?

**Difficulty**: Advanced

**Strategy**:
Profile first, then optimize hot paths. Use caching and efficient algorithms.

**Code Example**:
```javascript
const start = performance.now();
// Angular logic
const end = performance.now();
console.log('Time:', end - start);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q61: What are the security implications of Angular in large scale applications?

**Difficulty**: Intermediate

**Strategy**:
Validate all inputs. Sanitize data. Use least privilege principle.

**Code Example**:
```javascript
// Sanitize input
const clean = input.replace(/<script>/g, '');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q62: How do you debug Angular memory leaks in microservices?

**Difficulty**: Advanced

**Strategy**:
Use heap snapshots and look for detached DOM nodes or uncleared listeners.

**Code Example**:
```javascript
// Check listeners
process.on('exit', () => cleanup());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q63: Best practices for Angular code organization in mobile devices?

**Difficulty**: Beginner

**Strategy**:
Follow SOLID principles. Keep functions small and focused.

**Code Example**:
```javascript
// Single responsibility
function doOneThing() { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q64: How do you implement Angular error handling for legacy systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```javascript
try {
  await AngularOperation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q65: How do you test Angular functionality in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```javascript
test('Angular works', () => {
  expect(Angular()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q66: How do you handle Angular state management in real-time systems?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```javascript
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q67: How do you perform Angular data validation in distributed systems?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```javascript
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q68: How do you automate Angular deployment for high-traffic sites?

**Difficulty**: Advanced

**Strategy**:
Use CI/CD pipelines. Dockerize the application. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
steps:
  - run: npm test
  - run: docker build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q69: How do you handle Angular concurrency issues in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use locks, queues, or atomic operations. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
await mutex.runExclusive(async () => {
  // critical section
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q70: How do you implement Angular caching in production environments?

**Difficulty**: Intermediate

**Strategy**:
Use Redis or in-memory LRU caches. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const cache = new Map();
if (cache.has(key)) return cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q71: How do you manage Angular configuration for large scale applications?

**Difficulty**: Beginner

**Strategy**:
Use environment variables or config files. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const config = process.env.CONFIG || 'default';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q72: How do you handle Angular internationalization (i18n) in microservices?

**Difficulty**: Intermediate

**Strategy**:
Use i18n libraries. Extract strings to resource files.

**Code Example**:
```javascript
t('welcome_message')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q73: How do you ensure Angular accessibility (a11y) in mobile devices?

**Difficulty**: Beginner

**Strategy**:
Use semantic HTML and ARIA roles. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
<button aria-label="Close">X</button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q74: How do you optimize Angular network requests in legacy systems?

**Difficulty**: Advanced

**Strategy**:
Use batching, debouncing, or GraphQL. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
debounce(() => fetch(), 300);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q75: How do you handle Angular performance optimization for cloud infrastructure?

**Difficulty**: Advanced

**Strategy**:
Profile first, then optimize hot paths. Use caching and efficient algorithms.

**Code Example**:
```javascript
const start = performance.now();
// Angular logic
const end = performance.now();
console.log('Time:', end - start);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q76: What are the security implications of Angular in real-time systems?

**Difficulty**: Intermediate

**Strategy**:
Validate all inputs. Sanitize data. Use least privilege principle.

**Code Example**:
```javascript
// Sanitize input
const clean = input.replace(/<script>/g, '');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q77: How do you debug Angular memory leaks in distributed systems?

**Difficulty**: Advanced

**Strategy**:
Use heap snapshots and look for detached DOM nodes or uncleared listeners.

**Code Example**:
```javascript
// Check listeners
process.on('exit', () => cleanup());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q78: Best practices for Angular code organization in high-traffic sites?

**Difficulty**: Beginner

**Strategy**:
Follow SOLID principles. Keep functions small and focused.

**Code Example**:
```javascript
// Single responsibility
function doOneThing() { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q79: How do you implement Angular error handling for embedded systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```javascript
try {
  await AngularOperation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q80: How do you test Angular functionality in production environments?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```javascript
test('Angular works', () => {
  expect(Angular()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q81: How do you handle Angular state management in large scale applications?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```javascript
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q82: How do you perform Angular data validation in microservices?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```javascript
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q83: How do you automate Angular deployment for mobile devices?

**Difficulty**: Advanced

**Strategy**:
Use CI/CD pipelines. Dockerize the application. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
steps:
  - run: npm test
  - run: docker build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q84: How do you handle Angular concurrency issues in legacy systems?

**Difficulty**: Advanced

**Strategy**:
Use locks, queues, or atomic operations. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
await mutex.runExclusive(async () => {
  // critical section
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q85: How do you implement Angular caching in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Use Redis or in-memory LRU caches. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const cache = new Map();
if (cache.has(key)) return cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q86: How do you manage Angular configuration for real-time systems?

**Difficulty**: Beginner

**Strategy**:
Use environment variables or config files. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const config = process.env.CONFIG || 'default';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q87: How do you handle Angular internationalization (i18n) in distributed systems?

**Difficulty**: Intermediate

**Strategy**:
Use i18n libraries. Extract strings to resource files.

**Code Example**:
```javascript
t('welcome_message')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q88: How do you ensure Angular accessibility (a11y) in high-traffic sites?

**Difficulty**: Beginner

**Strategy**:
Use semantic HTML and ARIA roles. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
<button aria-label="Close">X</button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q89: How do you optimize Angular network requests in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use batching, debouncing, or GraphQL. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
debounce(() => fetch(), 300);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q90: How do you handle Angular performance optimization for production environments?

**Difficulty**: Advanced

**Strategy**:
Profile first, then optimize hot paths. Use caching and efficient algorithms.

**Code Example**:
```javascript
const start = performance.now();
// Angular logic
const end = performance.now();
console.log('Time:', end - start);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q91: What are the security implications of Angular in large scale applications?

**Difficulty**: Intermediate

**Strategy**:
Validate all inputs. Sanitize data. Use least privilege principle.

**Code Example**:
```javascript
// Sanitize input
const clean = input.replace(/<script>/g, '');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q92: How do you debug Angular memory leaks in microservices?

**Difficulty**: Advanced

**Strategy**:
Use heap snapshots and look for detached DOM nodes or uncleared listeners.

**Code Example**:
```javascript
// Check listeners
process.on('exit', () => cleanup());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q93: Best practices for Angular code organization in mobile devices?

**Difficulty**: Beginner

**Strategy**:
Follow SOLID principles. Keep functions small and focused.

**Code Example**:
```javascript
// Single responsibility
function doOneThing() { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q94: How do you implement Angular error handling for legacy systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```javascript
try {
  await AngularOperation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q95: How do you test Angular functionality in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```javascript
test('Angular works', () => {
  expect(Angular()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q96: How do you handle Angular state management in real-time systems?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```javascript
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q97: How do you perform Angular data validation in distributed systems?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```javascript
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q98: How do you automate Angular deployment for high-traffic sites?

**Difficulty**: Advanced

**Strategy**:
Use CI/CD pipelines. Dockerize the application. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
steps:
  - run: npm test
  - run: docker build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q99: How do you handle Angular concurrency issues in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use locks, queues, or atomic operations. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
await mutex.runExclusive(async () => {
  // critical section
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q100: How do you implement Angular caching in production environments?

**Difficulty**: Intermediate

**Strategy**:
Use Redis or in-memory LRU caches. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const cache = new Map();
if (cache.has(key)) return cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---
