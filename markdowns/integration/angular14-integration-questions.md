<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>Integration Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for developers</b></p>
</div>

---

## Table of Contents

1. [What are the key new features introduced in Angular 14?](#q1-what-are-the-key-new-features-introduced-in-angular-14) <span class="beginner">Beginner</span>
2. [How do you migrate from NgModules to Standalone Components?](#q2-how-do-you-migrate-from-ngmodules-to-standalone-components) <span class="beginner">Beginner</span>
3. [How do you set up and use Angular CLI auto-completion?](#q3-how-do-you-set-up-and-use-angular-cli-auto-completion) <span class="beginner">Beginner</span>
4. [How do you use optional injectors in embedded views?](#q4-how-do-you-use-optional-injectors-in-embedded-views) <span class="beginner">Beginner</span>
5. [How do you implement micro-frontend architecture with Angular 14?](#q5-how-do-you-implement-micro-frontend-architecture-with-angular-14) <span class="beginner">Beginner</span>
6. [How do you implement advanced state sharing between Angular 14 applications?](#q6-how-do-you-implement-advanced-state-sharing-between-angular-14-applications) <span class="beginner">Beginner</span>
7. [How do you implement real-time collaboration features in Angular 14?](#q7-how-do-you-implement-real-time-collaboration-features-in-angular-14) <span class="beginner">Beginner</span>
8. [How would you implement advanced Angular 14+ integration with modern development tools and CI/CD pipelines?](#q8-how-would-you-implement-advanced-angular-14+-integration-with-modern-development-tools-and-cicd-pipelines) <span class="beginner">Beginner</span>
9. [How would you implement advanced Angular 14+ integration with modern monitoring, analytics, and observability tools?](#q9-how-would-you-implement-advanced-angular-14+-integration-with-modern-monitoring-analytics-and-observability-tools) <span class="beginner">Beginner</span>
10. [How do you integrate Angular with Firebase using AngularFire?](#q10-how-do-you-integrate-angular-with-firebase-using-angularfire) <span class="beginner">Beginner</span>
11. [How do you integrate Redux DevTools with NgRx?](#q11-how-do-you-integrate-redux-devtools-with-ngrx) <span class="beginner">Beginner</span>
12. [How do you integrate Tailwind CSS with Angular?](#q12-how-do-you-integrate-tailwind-css-with-angular) <span class="beginner">Beginner</span>
13. [How do you integrate Angular Material?](#q13-how-do-you-integrate-angular-material) <span class="beginner">Beginner</span>
14. [How do you integrate GraphQL with Apollo in Angular?](#q14-how-do-you-integrate-graphql-with-apollo-in-angular) <span class="beginner">Beginner</span>
15. [How do you integrate Storybook with Angular?](#q15-how-do-you-integrate-storybook-with-angular) <span class="beginner">Beginner</span>
16. [How do you integrate Jest for testing in Angular?](#q16-how-do-you-integrate-jest-for-testing-in-angular) <span class="beginner">Beginner</span>
17. [How do you integrate Cypress for E2E testing?](#q17-how-do-you-integrate-cypress-for-e2e-testing) <span class="beginner">Beginner</span>
18. [How do you integrate Google Maps?](#q18-how-do-you-integrate-google-maps) <span class="beginner">Beginner</span>
19. [How do you integrate Socket.io with Angular?](#q19-how-do-you-integrate-socket.io-with-angular) <span class="beginner">Beginner</span>
20. [How do you integrate Stripe Elements?](#q20-how-do-you-integrate-stripe-elements) <span class="beginner">Beginner</span>
21. [How do you integrate Chart.js?](#q21-how-do-you-integrate-chart.js) <span class="beginner">Beginner</span>
22. [How do you integrate Auth0?](#q22-how-do-you-integrate-auth0) <span class="beginner">Beginner</span>
23. [How do you integrate Angular with Docker?](#q23-how-do-you-integrate-angular-with-docker) <span class="beginner">Beginner</span>
24. [How do you integrate Internationalization (i18n)?](#q24-how-do-you-integrate-internationalization-i18n) <span class="beginner">Beginner</span>
25. [How do you integrate `ngx-translate` for dynamic i18n?](#q25-how-do-you-integrate-ngx-translate-for-dynamic-i18n) <span class="beginner">Beginner</span>
26. [How do you integrate Sentry for error tracking?](#q26-how-do-you-integrate-sentry-for-error-tracking) <span class="beginner">Beginner</span>
27. [How do you integrate Prettier and ESLint?](#q27-how-do-you-integrate-prettier-and-eslint) <span class="beginner">Beginner</span>
28. [How do you integrate Husky for git hooks?](#q28-how-do-you-integrate-husky-for-git-hooks) <span class="beginner">Beginner</span>
29. [How do you integrate a mock server (JSON Server)?](#q29-how-do-you-integrate-a-mock-server-json-server) <span class="beginner">Beginner</span>
30. [How do you integrate Keycloak for IAM?](#q30-how-do-you-integrate-keycloak-for-iam) <span class="beginner">Beginner</span>
31. [How do you integrate AG Grid?](#q31-how-do-you-integrate-ag-grid) <span class="beginner">Beginner</span>
32. [How do you integrate RxJS Operators for HTTP retry strategies?](#q32-how-do-you-integrate-rxjs-operators-for-http-retry-strategies) <span class="beginner">Beginner</span>
33. [How do you integrate Web Workers in Angular?](#q33-how-do-you-integrate-web-workers-in-angular) <span class="beginner">Beginner</span>
34. [How do you integrate Service Workers (PWA)?](#q34-how-do-you-integrate-service-workers-pwa) <span class="beginner">Beginner</span>
35. [How do you integrate Module Federation (Micro-frontends)?](#q35-how-do-you-integrate-module-federation-micro-frontends) <span class="beginner">Beginner</span>
36. [How do you integrate Angular Universal (SSR)?](#q36-how-do-you-integrate-angular-universal-ssr) <span class="beginner">Beginner</span>
37. [How do you integrate a Virtual Scroller (CDK)?](#q37-how-do-you-integrate-a-virtual-scroller-cdk) <span class="beginner">Beginner</span>
38. [How do you integrate Drag and Drop (CDK)?](#q38-how-do-you-integrate-drag-and-drop-cdk) <span class="beginner">Beginner</span>
39. [How do you integrate Lottie Animations?](#q39-how-do-you-integrate-lottie-animations) <span class="beginner">Beginner</span>
40. [How do you integrate Markdown rendering?](#q40-how-do-you-integrate-markdown-rendering) <span class="beginner">Beginner</span>
41. [How do you integrate a Date Picker (Material)?](#q41-how-do-you-integrate-a-date-picker-material) <span class="beginner">Beginner</span>
42. [How do you integrate Form Validation (Reactive)?](#q42-how-do-you-integrate-form-validation-reactive) <span class="beginner">Beginner</span>
43. [How do you integrate File Upload?](#q43-how-do-you-integrate-file-upload) <span class="beginner">Beginner</span>
44. [How do you integrate JWT Handling?](#q44-how-do-you-integrate-jwt-handling) <span class="beginner">Beginner</span>
45. [How do you integrate FontAwesome?](#q45-how-do-you-integrate-fontawesome) <span class="beginner">Beginner</span>
46. [How do you integrate Google Analytics 4 (GA4)?](#q46-how-do-you-integrate-google-analytics-4-ga4) <span class="beginner">Beginner</span>
47. [How do you integrate Hotjar?](#q47-how-do-you-integrate-hotjar) <span class="beginner">Beginner</span>
48. [How do you integrate Bootstrap 5?](#q48-how-do-you-integrate-bootstrap-5) <span class="beginner">Beginner</span>
49. [How do you integrate PrimeNG?](#q49-how-do-you-integrate-primeng) <span class="beginner">Beginner</span>
50. [How do you integrate Lodash?](#q50-how-do-you-integrate-lodash) <span class="beginner">Beginner</span>
51. [How do you integrate Moment.js (or Day.js)?](#q51-how-do-you-integrate-moment.js-or-day.js) <span class="beginner">Beginner</span>
52. [How do you integrate PDF generation (`jspdf`)?](#q52-how-do-you-integrate-pdf-generation-jspdf) <span class="beginner">Beginner</span>
53. [How do you integrate Excel export (`xlsx`)?](#q53-how-do-you-integrate-excel-export-xlsx) <span class="beginner">Beginner</span>
54. [How do you integrate Clipboard copy?](#q54-how-do-you-integrate-clipboard-copy) <span class="beginner">Beginner</span>
55. [How do you integrate QR Code generation?](#q55-how-do-you-integrate-qr-code-generation) <span class="beginner">Beginner</span>
56. [How do you integrate Toast Notifications (`ngx-toastr`)?](#q56-how-do-you-integrate-toast-notifications-ngx-toastr) <span class="beginner">Beginner</span>
57. [How do you integrate Loading Spinner (Overlay)?](#q57-how-do-you-integrate-loading-spinner-overlay) <span class="beginner">Beginner</span>
58. [How do you integrate Environment Variables?](#q58-how-do-you-integrate-environment-variables) <span class="beginner">Beginner</span>
59. [How do you integrate Custom Web Elements?](#q59-how-do-you-integrate-custom-web-elements) <span class="beginner">Beginner</span>
60. [How do you integrate Angular with Electron?](#q60-how-do-you-integrate-angular-with-electron) <span class="beginner">Beginner</span>
61. [How do you integrate Angular with Tauri?](#q61-how-do-you-integrate-angular-with-tauri) <span class="beginner">Beginner</span>
62. [How do you integrate Angular with Ionic?](#q62-how-do-you-integrate-angular-with-ionic) <span class="beginner">Beginner</span>
63. [How do you integrate Push Notifications?](#q63-how-do-you-integrate-push-notifications) <span class="beginner">Beginner</span>
64. [How do you integrate Biometric Auth (WebAuthn)?](#q64-how-do-you-integrate-biometric-auth-webauthn) <span class="beginner">Beginner</span>
65. [How do you integrate Voice Recognition (Web Speech API)?](#q65-how-do-you-integrate-voice-recognition-web-speech-api) <span class="beginner">Beginner</span>
66. [How do you integrate Text-to-Speech?](#q66-how-do-you-integrate-text-to-speech) <span class="beginner">Beginner</span>
67. [How do you integrate Drag and Drop File Upload?](#q67-how-do-you-integrate-drag-and-drop-file-upload) <span class="beginner">Beginner</span>
68. [How do you integrate Infinite Scroll?](#q68-how-do-you-integrate-infinite-scroll) <span class="beginner">Beginner</span>
69. [How do you integrate Skeleton Loading?](#q69-how-do-you-integrate-skeleton-loading) <span class="beginner">Beginner</span>
70. [How do you integrate Image Cropping?](#q70-how-do-you-integrate-image-cropping) <span class="beginner">Beginner</span>
71. [How do you integrate PDF Viewer?](#q71-how-do-you-integrate-pdf-viewer) <span class="beginner">Beginner</span>
72. [How do you integrate Video Player?](#q72-how-do-you-integrate-video-player) <span class="beginner">Beginner</span>
73. [How do you integrate Rich Text Editor (WYSIWYG)?](#q73-how-do-you-integrate-rich-text-editor-wysiwyg) <span class="beginner">Beginner</span>
74. [How do you integrate Code Highlighting?](#q74-how-do-you-integrate-code-highlighting) <span class="beginner">Beginner</span>
75. [How do you integrate Cookie Handling?](#q75-how-do-you-integrate-cookie-handling) <span class="beginner">Beginner</span>
76. [How do you integrate LocalStorage/SessionStorage?](#q76-how-do-you-integrate-localstoragesessionstorage) <span class="beginner">Beginner</span>
77. [How do you integrate Key Bindings (Hotkeys)?](#q77-how-do-you-integrate-key-bindings-hotkeys) <span class="beginner">Beginner</span>
78. [How do you integrate Screen/Device Detection?](#q78-how-do-you-integrate-screendevice-detection) <span class="beginner">Beginner</span>
79. [How do you integrate FullCalendar?](#q79-how-do-you-integrate-fullcalendar) <span class="beginner">Beginner</span>
80. [How do you integrate Tooltips?](#q80-how-do-you-integrate-tooltips) <span class="beginner">Beginner</span>
81. [How do you integrate Popovers?](#q81-how-do-you-integrate-popovers) <span class="beginner">Beginner</span>
82. [How do you integrate Modals/Dialogs?](#q82-how-do-you-integrate-modalsdialogs) <span class="beginner">Beginner</span>
83. [How do you integrate Side Navigation (Drawer)?](#q83-how-do-you-integrate-side-navigation-drawer) <span class="beginner">Beginner</span>
84. [How do you integrate Tabs?](#q84-how-do-you-integrate-tabs) <span class="beginner">Beginner</span>
85. [How do you integrate Stepper?](#q85-how-do-you-integrate-stepper) <span class="beginner">Beginner</span>
86. [How do you integrate Tree View?](#q86-how-do-you-integrate-tree-view) <span class="beginner">Beginner</span>
87. [How do you integrate Autocomplete?](#q87-how-do-you-integrate-autocomplete) <span class="beginner">Beginner</span>
88. [How do you integrate Slider?](#q88-how-do-you-integrate-slider) <span class="beginner">Beginner</span>
89. [How do you integrate Toggle Switch?](#q89-how-do-you-integrate-toggle-switch) <span class="beginner">Beginner</span>
90. [How do you integrate Badge?](#q90-how-do-you-integrate-badge) <span class="beginner">Beginner</span>
91. [How do you integrate Progress Bar/Spinner?](#q91-how-do-you-integrate-progress-barspinner) <span class="beginner">Beginner</span>
92. [How do you integrate Snackbar/Toast?](#q92-how-do-you-integrate-snackbartoast) <span class="beginner">Beginner</span>
93. [How do you integrate Bottom Sheet?](#q93-how-do-you-integrate-bottom-sheet) <span class="beginner">Beginner</span>
94. [How do you integrate Expansion Panel (Accordion)?](#q94-how-do-you-integrate-expansion-panel-accordion) <span class="beginner">Beginner</span>
95. [How do you integrate Divider?](#q95-how-do-you-integrate-divider) <span class="beginner">Beginner</span>
96. [How do you integrate Grid List?](#q96-how-do-you-integrate-grid-list) <span class="beginner">Beginner</span>
97. [How do you integrate Virtual Keyboard?](#q97-how-do-you-integrate-virtual-keyboard) <span class="beginner">Beginner</span>
98. [How do you integrate Signature Pad?](#q98-how-do-you-integrate-signature-pad) <span class="beginner">Beginner</span>
99. [How do you integrate Barcode Scanner?](#q99-how-do-you-integrate-barcode-scanner) <span class="beginner">Beginner</span>
100. [How do you integrate Geolocation?](#q100-how-do-you-integrate-geolocation) <span class="beginner">Beginner</span>
101. [How do you integrate Vibration?](#q101-how-do-you-integrate-vibration) <span class="beginner">Beginner</span>
102. [How do you integrate Battery Status?](#q102-how-do-you-integrate-battery-status) <span class="beginner">Beginner</span>
103. [How do you integrate Network Status Detection?](#q103-how-do-you-integrate-network-status-detection) <span class="beginner">Beginner</span>
104. [How do you integrate Page Visibility API?](#q104-how-do-you-integrate-page-visibility-api) <span class="beginner">Beginner</span>
105. [How do you integrate Fullscreen API?](#q105-how-do-you-integrate-fullscreen-api) <span class="beginner">Beginner</span>
106. [How do you integrate Picture-in-Picture?](#q106-how-do-you-integrate-picture-in-picture) <span class="beginner">Beginner</span>
107. [How do you integrate Share API (Web Share)?](#q107-how-do-you-integrate-share-api-web-share) <span class="beginner">Beginner</span>
108. [How do you integrate Payment Request API?](#q108-how-do-you-integrate-payment-request-api) <span class="beginner">Beginner</span>
109. [How do you integrate Bluetooth (Web Bluetooth)?](#q109-how-do-you-integrate-bluetooth-web-bluetooth) <span class="beginner">Beginner</span>

---

## Angular 14 New Features

<a id="q1"></a>
### Q1: What are the key new features introduced in Angular 14?

**Difficulty**: Intermediate

**Answer:**
Angular 14 introduced several significant features that enhance developer experience and application performance.

**Key Angular 14 Features:**

1. **Standalone Components**
2. **Optional Injectors in Embedded Views**
3. **Extended Developer Diagnostics**
4. **Angular CLI Auto-completion**
5. **Bind Route Info to Component Inputs**
6. **Page Title Strategy**
7. **Angular DevKit**
8. **Strict Typed Forms**

**Feature Implementation Examples:**
```typescript
// 1. Standalone Components
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-standalone',
  standalone: true,
  imports: [CommonModule, RouterModule, MatButtonModule],
  template: `
    <div class="standalone-component">
      <h2>Standalone Component</h2>
      <button mat-raised-button color="primary" (click)="onClick()">
        Click Me
      </button>
      <p *ngIf="showMessage">{{ message }}</p>
    </div>
  `,
  styles: [`
    .standalone-component {
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 8px;
      margin: 10px;
    }
  `]
})
export class StandaloneComponent {
  showMessage = false;
  message = 'Hello from Standalone Component!';
  
  onClick() {
    this.showMessage = !this.showMessage;
  }
}

// 2. Bootstrapping with Standalone Components
import { bootstrapApplication } from '@angular/platform-browser';
import { importProvidersFrom } from '@angular/core';
import { RouterModule } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { AppComponent } from './app/app.component';
import { routes } from './app/app.routes';

bootstrapApplication(AppComponent, {
  providers: [
    importProvidersFrom(
      RouterModule.forRoot(routes),
      HttpClientModule,
      BrowserAnimationsModule
    ),
    // Additional providers
    { provide: 'API_URL', useValue: 'https://api.example.com' }
  ]
}).catch(err => console.error(err));

// 3. Route Configuration with Standalone Components
import { Routes } from '@angular/router';

export const routes: Routes = [
  {
    path: '',
    loadComponent: () => import('./home/home.component').then(m => m.HomeComponent)
  },
  {
    path: 'about',
    loadComponent: () => import('./about/about.component').then(m => m.AboutComponent)
  },
  {
    path: 'products',
    loadChildren: () => import('./products/products.routes').then(m => m.routes)
  },
  {
    path: 'user/:id',
    loadComponent: () => import('./user/user.component').then(m => m.UserComponent),
    // Bind route parameters to component inputs
    data: { bindToComponentInputs: true }
  }
];

// 4. Component with Route Input Binding
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-user',
  standalone: true,
  template: `
    <div class="user-profile">
      <h2>User Profile</h2>
      <p>User ID: {{ id }}</p>
      <p>Tab: {{ tab }}</p>
    </div>
  `
})
export class UserComponent {
  @Input() id!: string; // Automatically bound from route params
  @Input() tab?: string; // Automatically bound from query params
}

// 5. Page Title Strategy
import { Injectable } from '@angular/core';
import { Title } from '@angular/platform-browser';
import { RouterStateSnapshot, TitleStrategy } from '@angular/router';

@Injectable({ providedIn: 'root' })
export class CustomTitleStrategy extends TitleStrategy {
  constructor(private readonly title: Title) {
    super();
  }
  
  override updateTitle(routerState: RouterStateSnapshot): void {
    const title = this.buildTitle(routerState);
    if (title !== undefined) {
      this.title.setTitle(`MyApp - ${title}`);
    } else {
      this.title.setTitle('MyApp - Default Title');
    }
  }
}

// Register the title strategy
bootstrapApplication(AppComponent, {
  providers: [
    { provide: TitleStrategy, useClass: CustomTitleStrategy },
    // other providers
  ]
});

// 6. Optional Injectors in Embedded Views
import { Component, TemplateRef, ViewChild, ViewContainerRef, Injector } from '@angular/core';
import { UserService } from './user.service';

@Component({
  selector: 'app-dynamic-content',
  standalone: true,
  template: `
    <div class="container">
      <ng-template #dynamicTemplate let-user="user">
        <div class="user-card">
          <h3>{{ user.name }}</h3>
          <p>{{ user.email }}</p>
          <button (click)="updateUser(user)">Update</button>
        </div>
      </ng-template>
      
      <div #dynamicContainer></div>
      
      <button (click)="loadDynamicContent()">Load Dynamic Content</button>
    </div>
  `
})
export class DynamicContentComponent {
  @ViewChild('dynamicTemplate', { read: TemplateRef }) template!: TemplateRef<any>;
  @ViewChild('dynamicContainer', { read: ViewContainerRef }) container!: ViewContainerRef;
  
  constructor(private injector: Injector) {}
  
  loadDynamicContent() {
    // Create a custom injector for the embedded view
    const customInjector = Injector.create({
      providers: [
        { provide: UserService, useClass: UserService },
        { provide: 'CUSTOM_CONFIG', useValue: { theme: 'dark' } }
      ],
      parent: this.injector
    });
    
    // Create embedded view with custom injector
    const embeddedView = this.container.createEmbeddedView(
      this.template,
      { user: { name: 'John Doe', email: 'john@example.com' } },
      { injector: customInjector }
    );
  }
  
  updateUser(user: any) {
    console.log('Updating user:', user);
  }
}

// 7. Extended Developer Diagnostics
import { enableProdMode, isDevMode } from '@angular/core';

if (!isDevMode()) {
  enableProdMode();
} else {
  // Enable extended diagnostics in development
  console.log('Development mode - Extended diagnostics enabled');
  
  // Custom error handler for better debugging
  window.addEventListener('unhandledrejection', (event) => {
    console.error('Unhandled promise rejection:', event.reason);
  });
}

// 8. Strict Typed Forms (Angular 14+)
import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators, FormControl } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';

interface UserForm {
  name: FormControl<string>;
  email: FormControl<string>;
  age: FormControl<number>;
  preferences: FormGroup<{
    newsletter: FormControl<boolean>;
    theme: FormControl<'light' | 'dark'>;
  }>;
}

@Component({
  selector: 'app-typed-form',
  standalone: true,
  imports: [ReactiveFormsModule],
  template: `
    <form [formGroup]="userForm" (ngSubmit)="onSubmit()">
      <div class="form-group">
        <label for="name">Name:</label>
        <input id="name" formControlName="name" type="text">
        <div *ngIf="userForm.get('name')?.errors?.['required']">
          Name is required
        </div>
      </div>
      
      <div class="form-group">
        <label for="email">Email:</label>
        <input id="email" formControlName="email" type="email">
        <div *ngIf="userForm.get('email')?.errors?.['email']">
          Invalid email format
        </div>
      </div>
      
      <div class="form-group">
        <label for="age">Age:</label>
        <input id="age" formControlName="age" type="number">
      </div>
      
      <div formGroupName="preferences">
        <h3>Preferences</h3>
        
        <label>
          <input formControlName="newsletter" type="checkbox">
          Subscribe to newsletter
        </label>
        
        <div class="form-group">
          <label for="theme">Theme:</label>
          <select id="theme" formControlName="theme">
            <option value="light">Light</option>
            <option value="dark">Dark</option>
          </select>
        </div>
      </div>
      
      <button type="submit" [disabled]="userForm.invalid">
        Submit
      </button>
    </form>
  `
})
export class TypedFormComponent {
  userForm: FormGroup<UserForm>;
  
  constructor(private fb: FormBuilder) {
    this.userForm = this.fb.group({
      name: this.fb.control('', { validators: [Validators.required], nonNullable: true }),
      email: this.fb.control('', { validators: [Validators.required, Validators.email], nonNullable: true }),
      age: this.fb.control(0, { validators: [Validators.min(0)], nonNullable: true }),
      preferences: this.fb.group({
        newsletter: this.fb.control(false, { nonNullable: true }),
        theme: this.fb.control<'light' | 'dark'>('light', { nonNullable: true })
      })
    });
  }
  
  onSubmit() {
    if (this.userForm.valid) {
      const formValue = this.userForm.value;
      // TypeScript now knows the exact types
      console.log('Form submitted:', formValue);
      
      // Access typed values
      const name: string = formValue.name!;
      const email: string = formValue.email!;
      const age: number = formValue.age!;
      const newsletter: boolean = formValue.preferences?.newsletter!;
      const theme: 'light' | 'dark' = formValue.preferences?.theme!;
    }
  }
}
```

---

## Standalone Components

<a id="q2"></a>
### Q2: How do you migrate from NgModules to Standalone Components?

**Difficulty**: Intermediate

**Answer:**
Migrating to standalone components involves converting existing NgModule-based components and updating the application bootstrap process.

**Migration Strategy:**
```typescript
// BEFORE: Traditional NgModule approach
// user.module.ts
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule } from '@angular/forms';
import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';
import { MatInputModule } from '@angular/material/input';

import { UserComponent } from './user.component';
import { UserListComponent } from './user-list.component';
import { UserDetailComponent } from './user-detail.component';
import { UserService } from './user.service';

@NgModule({
  declarations: [
    UserComponent,
    UserListComponent,
    UserDetailComponent
  ],
  imports: [
    CommonModule,
    ReactiveFormsModule,
    MatCardModule,
    MatButtonModule,
    MatInputModule
  ],
  providers: [UserService],
  exports: [UserComponent]
})
export class UserModule { }

// AFTER: Standalone Components approach
// user.component.ts
import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule, FormBuilder, Validators } from '@angular/forms';
import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';
import { MatInputModule } from '@angular/material/input';

import { UserService } from './user.service';
import { UserListComponent } from './user-list.component';
import { UserDetailComponent } from './user-detail.component';

@Component({
  selector: 'app-user',
  standalone: true,
  imports: [
    CommonModule,
    ReactiveFormsModule,
    MatCardModule,
    MatButtonModule,
    MatInputModule,
    UserListComponent,
    UserDetailComponent
  ],
  providers: [UserService],
  template: `
    <div class="user-container">
      <mat-card>
        <mat-card-header>
          <mat-card-title>User Management</mat-card-title>
        </mat-card-header>
        
        <mat-card-content>
          <form [formGroup]="userForm" (ngSubmit)="onSubmit()">
            <mat-form-field appearance="fill">
              <mat-label>Name</mat-label>
              <input matInput formControlName="name">
              <mat-error *ngIf="userForm.get('name')?.errors?.['required']">
                Name is required
              </mat-error>
            </mat-form-field>
            
            <mat-form-field appearance="fill">
              <mat-label>Email</mat-label>
              <input matInput formControlName="email" type="email">
              <mat-error *ngIf="userForm.get('email')?.errors?.['email']">
                Invalid email
              </mat-error>
            </mat-form-field>
            
            <div class="form-actions">
              <button mat-raised-button color="primary" type="submit" 
                      [disabled]="userForm.invalid">
                Save User
              </button>
              <button mat-button type="button" (click)="onReset()">
                Reset
              </button>
            </div>
          </form>
        </mat-card-content>
      </mat-card>
      
      <app-user-list 
        [users]="users" 
        (userSelected)="onUserSelected($event)">
      </app-user-list>
      
      <app-user-detail 
        *ngIf="selectedUser" 
        [user]="selectedUser"
        (userUpdated)="onUserUpdated($event)">
      </app-user-detail>
    </div>
  `,
  styles: [`
    .user-container {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      padding: 20px;
    }
    
    .form-actions {
      display: flex;
      gap: 10px;
      margin-top: 20px;
    }
    
    mat-form-field {
      width: 100%;
      margin-bottom: 15px;
    }
  `]
})
export class UserComponent {
  private fb = inject(FormBuilder);
  private userService = inject(UserService);
  
  users: any[] = [];
  selectedUser: any = null;
  
  userForm = this.fb.group({
    name: ['', Validators.required],
    email: ['', [Validators.required, Validators.email]]
  });
  
  ngOnInit() {
    this.loadUsers();
  }
  
  async loadUsers() {
    try {
      this.users = await this.userService.getUsers();
    } catch (error) {
      console.error('Error loading users:', error);
    }
  }
  
  async onSubmit() {
    if (this.userForm.valid) {
      try {
        const user = await this.userService.createUser(this.userForm.value);
        this.users.push(user);
        this.userForm.reset();
      } catch (error) {
        console.error('Error creating user:', error);
      }
    }
  }
  
  onReset() {
    this.userForm.reset();
    this.selectedUser = null;
  }
  
  onUserSelected(user: any) {
    this.selectedUser = user;
  }
  
  onUserUpdated(user: any) {
    const index = this.users.findIndex(u => u.id === user.id);
    if (index !== -1) {
      this.users[index] = user;
    }
  }
}

// user-list.component.ts
import { Component, Input, Output, EventEmitter } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatListModule } from '@angular/material/list';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-user-list',
  standalone: true,
  imports: [CommonModule, MatListModule, MatIconModule, MatButtonModule],
  template: `
    <mat-list>
      <h3 mat-subheader>Users</h3>
      <mat-list-item *ngFor="let user of users" (click)="selectUser(user)">
        <mat-icon matListItemIcon>person</mat-icon>
        <h4 matListItemTitle>{{ user.name }}</h4>
        <p matListItemLine>{{ user.email }}</p>
        <button mat-icon-button (click)="$event.stopPropagation(); deleteUser(user)">
          <mat-icon>delete</mat-icon>
        </button>
      </mat-list-item>
    </mat-list>
  `,
  styles: [`
    mat-list-item {
      cursor: pointer;
    }
    
    mat-list-item:hover {
      background-color: #f5f5f5;
    }
  `]
})
export class UserListComponent {
  @Input() users: any[] = [];
  @Output() userSelected = new EventEmitter<any>();
  @Output() userDeleted = new EventEmitter<any>();
  
  selectUser(user: any) {
    this.userSelected.emit(user);
  }
  
  deleteUser(user: any) {
    this.userDeleted.emit(user);
  }
}

// Migration Utility
class StandaloneMigrationHelper {
  static convertComponentToStandalone(componentPath: string) {
    // This would be a CLI tool or script to help with migration
    console.log(`Converting ${componentPath} to standalone component`);
    
    // Steps:
    // 1. Add standalone: true to @Component decorator
    // 2. Move imports from NgModule to component imports array
    // 3. Move providers from NgModule to component providers array
    // 4. Update routing configuration
    // 5. Update tests
  }
  
  static generateStandaloneBootstrap(appComponentPath: string) {
    return `
import { bootstrapApplication } from '@angular/platform-browser';
import { importProvidersFrom } from '@angular/core';
import { RouterModule } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { AppComponent } from '${appComponentPath}';
import { routes } from './app.routes';

bootstrapApplication(AppComponent, {
  providers: [
    importProvidersFrom(
      RouterModule.forRoot(routes),
      HttpClientModule,
      BrowserAnimationsModule
    )
  ]
}).catch(err => console.error(err));
    `;
  }
}

// Lazy Loading with Standalone Components
export const userRoutes: Routes = [
  {
    path: '',
    loadComponent: () => import('./user.component').then(m => m.UserComponent)
  },
  {
    path: 'profile/:id',
    loadComponent: () => import('./user-profile.component').then(m => m.UserProfileComponent)
  },
  {
    path: 'settings',
    loadComponent: () => import('./user-settings.component').then(m => m.UserSettingsComponent),
    canActivate: [AuthGuard]
  }
];

// Feature-based routing with standalone components
export const routes: Routes = [
  {
    path: '',
    loadComponent: () => import('./home/home.component').then(m => m.HomeComponent)
  },
  {
    path: 'users',
    loadChildren: () => import('./users/user.routes').then(m => m.userRoutes)
  },
  {
    path: 'products',
    loadChildren: () => import('./products/product.routes').then(m => m.productRoutes)
  }
];
```

**Migration Checklist:**
1. ✅ Convert components to standalone
2. ✅ Update routing configuration
3. ✅ Replace NgModule bootstrap with bootstrapApplication
4. ✅ Move shared services to root providers
5. ✅ Update lazy loading routes
6. ✅ Update unit tests
7. ✅ Update e2e tests
8. ✅ Remove unused NgModules

---

## Angular CLI Auto-completion

<a id="q3"></a>
### Q3: How do you set up and use Angular CLI auto-completion?

**Difficulty**: Intermediate

**Answer:**
Angular 14 introduced CLI auto-completion to improve developer productivity.

**Setting up Auto-completion:**
```bash
# Enable auto-completion for current session
ng completion

# Add to shell profile for permanent setup
# For Bash
echo 'source <(ng completion script)' >> ~/.bashrc

# For Zsh
echo 'source <(ng completion script)' >> ~/.zshrc

# For Fish
ng completion script | source

# Reload shell or source the profile
source ~/.bashrc  # or ~/.zshrc
```

**Auto-completion Features:**
```bash
# Command completion
ng <TAB>  # Shows: build, serve, test, lint, e2e, generate, add, etc.

# Subcommand completion
ng generate <TAB>  # Shows: component, service, module, directive, etc.

# Option completion
ng build --<TAB>  # Shows: --configuration, --prod, --watch, --output-path, etc.

# Configuration completion
ng build --configuration <TAB>  # Shows: development, production, etc.

# Schematic completion
ng generate component <TAB>  # Shows available component options

# File path completion
ng generate component src/app/<TAB>  # Shows directory structure
```

**Custom CLI Commands with Auto-completion:**
```typescript
// custom-schematic.ts
import {
  Rule,
  SchematicContext,
  Tree,
  apply,
  url,
  template,
  move,
  chain,
  mergeWith
} from '@angular-devkit/schematics';
import { strings, normalize, experimental } from '@angular-devkit/core';

interface Options {
  name: string;
  path?: string;
  project?: string;
  type: 'basic' | 'advanced' | 'custom';
}

export function customComponent(options: Options): Rule {
  return (tree: Tree, _context: SchematicContext) => {
    const workspaceConfig = tree.read('/angular.json');
    if (!workspaceConfig) {
      throw new Error('Could not find Angular workspace configuration');
    }

    const workspaceContent = workspaceConfig.toString();
    const workspace = JSON.parse(workspaceContent);
    
    if (!options.project) {
      options.project = workspace.defaultProject;
    }

    const projectConfig = workspace.projects[options.project];
    const projectRoot = projectConfig.root;
    const sourceRoot = projectConfig.sourceRoot || 'src';

    if (!options.path) {
      options.path = `${sourceRoot}/app`;
    }

    const templateSource = apply(url('./files'), [
      template({
        classify: strings.classify,
        dasherize: strings.dasherize,
        name: options.name,
        type: options.type
      }),
      move(normalize(options.path as string))
    ]);

    return chain([
      mergeWith(templateSource)
    ]);
  };
}

// schema.json for auto-completion
{
  "$schema": "http://json-schema.org/schema",
  "id": "CustomComponent",
  "title": "Custom Component Options Schema",
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "description": "The name of the component.",
      "$default": {
        "$source": "argv",
        "index": 0
      },
      "x-prompt": "What name would you like to use for the component?"
    },
    "path": {
      "type": "string",
      "format": "path",
      "description": "The path at which to create the component file.",
      "visible": false
    },
    "project": {
      "type": "string",
      "description": "The name of the project.",
      "$default": {
        "$source": "projectName"
      }
    },
    "type": {
      "type": "string",
      "description": "The type of component to create.",
      "enum": ["basic", "advanced", "custom"],
      "default": "basic",
      "x-prompt": {
        "message": "Which type of component would you like to create?",
        "type": "list",
        "items": [
          { "value": "basic", "label": "Basic Component" },
          { "value": "advanced", "label": "Advanced Component with Services" },
          { "value": "custom", "label": "Custom Component with Full Setup" }
        ]
      }
    }
  },
  "required": ["name"]
}

// collection.json
{
  "$schema": "../node_modules/@angular-devkit/schematics/collection-schema.json",
  "schematics": {
    "custom-component": {
      "description": "A custom component schematic with auto-completion.",
      "factory": "./custom-component/index#customComponent",
      "schema": "./custom-component/schema.json"
    }
  }
}
```

**Enhanced CLI Workflow:**
```bash
# Auto-completion in action
ng generate custom-component <TAB>
# Prompts for component name with auto-completion

ng generate custom-component my-feature --type <TAB>
# Shows: basic, advanced, custom

ng build --configuration <TAB>
# Shows all available configurations from angular.json

ng test --browsers <TAB>
# Shows available browsers: Chrome, Firefox, Safari, etc.

ng lint --files <TAB>
# Shows file patterns and paths
```

---

## Optional Injectors

<a id="q4"></a>
### Q4: How do you use optional injectors in embedded views?

**Difficulty**: Intermediate

**Answer:**
Optional injectors in Angular 14 allow you to provide different dependency injection contexts for embedded views.

**Implementation Examples:**
```typescript
// Dynamic Component Loading with Custom Injector
import {
  Component,
  ViewChild,
  ViewContainerRef,
  TemplateRef,
  Injector,
  inject,
  Injectable
} from '@angular/core';

// Services for injection
@Injectable()
export class ThemeService {
  private currentTheme = 'light';
  
  getTheme() {
    return this.currentTheme;
  }
  
  setTheme(theme: string) {
    this.currentTheme = theme;
  }
}

@Injectable()
export class ConfigService {
  constructor(private config: any) {}
  
  getConfig(key: string) {
    return this.config[key];
  }
}

// Component with optional injectors
@Component({
  selector: 'app-dynamic-injector',
  standalone: true,
  template: `
    <div class="container">
      <h2>Dynamic Injector Example</h2>
      
      <!-- Template for embedded view -->
      <ng-template #dynamicTemplate let-data="data">
        <div class="dynamic-content" [class]="getThemeClass()">
          <h3>{{ data.title }}</h3>
          <p>{{ data.description }}</p>
          <p>Theme: {{ getCurrentTheme() }}</p>
          <p>Config: {{ getConfigValue('apiUrl') }}</p>
          <button (click)="performAction(data)">Action</button>
        </div>
      </ng-template>
      
      <!-- Container for dynamic content -->
      <div #dynamicContainer class="dynamic-container"></div>
      
      <!-- Controls -->
      <div class="controls">
        <button (click)="createLightThemeView()">Create Light Theme View</button>
        <button (click)="createDarkThemeView()">Create Dark Theme View</button>
        <button (click)="createCustomConfigView()">Create Custom Config View</button>
        <button (click)="clearViews()">Clear All Views</button>
      </div>
    </div>
  `,
  styles: [`
    .container {
      padding: 20px;
    }
    
    .dynamic-container {
      border: 2px dashed #ccc;
      padding: 20px;
      margin: 20px 0;
      min-height: 200px;
    }
    
    .dynamic-content {
      padding: 15px;
      border-radius: 8px;
      margin-bottom: 10px;
    }
    
    .dynamic-content.light {
      background-color: #f8f9fa;
      border: 1px solid #dee2e6;
    }
    
    .dynamic-content.dark {
      background-color: #343a40;
      color: white;
      border: 1px solid #495057;
    }
    
    .controls {
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
    }
    
    button {
      padding: 8px 16px;
      border: none;
      border-radius: 4px;
      background-color: #007bff;
      color: white;
      cursor: pointer;
    }
    
    button:hover {
      background-color: #0056b3;
    }
  `]
})
export class DynamicInjectorComponent {
  @ViewChild('dynamicTemplate', { read: TemplateRef }) template!: TemplateRef<any>;
  @ViewChild('dynamicContainer', { read: ViewContainerRef }) container!: ViewContainerRef;
  
  private parentInjector = inject(Injector);
  private viewCounter = 0;
  
  createLightThemeView() {
    const lightThemeService = new ThemeService();
    lightThemeService.setTheme('light');
    
    const customInjector = Injector.create({
      providers: [
        { provide: ThemeService, useValue: lightThemeService },
        { provide: ConfigService, useValue: new ConfigService({ apiUrl: 'https://api.light.com' }) }
      ],
      parent: this.parentInjector
    });
    
    this.createEmbeddedView(customInjector, {
      title: `Light Theme View ${++this.viewCounter}`,
      description: 'This view uses a light theme configuration'
    });
  }
  
  createDarkThemeView() {
    const darkThemeService = new ThemeService();
    darkThemeService.setTheme('dark');
    
    const customInjector = Injector.create({
      providers: [
        { provide: ThemeService, useValue: darkThemeService },
        { provide: ConfigService, useValue: new ConfigService({ apiUrl: 'https://api.dark.com' }) }
      ],
      parent: this.parentInjector
    });
    
    this.createEmbeddedView(customInjector, {
      title: `Dark Theme View ${++this.viewCounter}`,
      description: 'This view uses a dark theme configuration'
    });
  }
  
  createCustomConfigView() {
    const customThemeService = new ThemeService();
    customThemeService.setTheme('custom');
    
    const customInjector = Injector.create({
      providers: [
        { provide: ThemeService, useValue: customThemeService },
        { provide: ConfigService, useValue: new ConfigService({ 
          apiUrl: 'https://api.custom.com',
          features: ['advanced', 'premium'],
          version: '2.0'
        }) },
        { provide: 'CUSTOM_TOKEN', useValue: 'Custom Value' }
      ],
      parent: this.parentInjector
    });
    
    this.createEmbeddedView(customInjector, {
      title: `Custom Config View ${++this.viewCounter}`,
      description: 'This view uses a custom configuration with additional features'
    });
  }
  
  private createEmbeddedView(injector: Injector, data: any) {
    const embeddedViewRef = this.container.createEmbeddedView(
      this.template,
      { data },
      { injector }
    );
    
    // Store reference for cleanup
    embeddedViewRef.context.getThemeClass = () => {
      const themeService = injector.get(ThemeService);
      return themeService.getTheme();
    };
    
    embeddedViewRef.context.getCurrentTheme = () => {
      const themeService = injector.get(ThemeService);
      return themeService.getTheme();
    };
    
    embeddedViewRef.context.getConfigValue = (key: string) => {
      const configService = injector.get(ConfigService);
      return configService.getConfig(key);
    };
    
    embeddedViewRef.context.performAction = (data: any) => {
      console.log('Action performed with data:', data);
      console.log('Theme:', injector.get(ThemeService).getTheme());
      console.log('Config:', injector.get(ConfigService));
    };
  }
  
  clearViews() {
    this.container.clear();
    this.viewCounter = 0;
  }
}

// Advanced Example: Modal Service with Custom Injectors
@Injectable({ providedIn: 'root' })
export class ModalService {
  private modals = new Map<string, any>();
  
  constructor(
    private viewContainerRef: ViewContainerRef,
    private injector: Injector
  ) {}
  
  open<T>(component: any, config: ModalConfig<T> = {}): ModalRef<T> {
    const modalId = this.generateId();
    
    // Create custom injector for modal
    const modalInjector = Injector.create({
      providers: [
        { provide: 'MODAL_DATA', useValue: config.data },
        { provide: 'MODAL_CONFIG', useValue: config },
        { provide: ModalRef, useValue: new ModalRef(modalId, this) },
        ...(config.providers || [])
      ],
      parent: this.injector
    });
    
    // Create component with custom injector
    const componentRef = this.viewContainerRef.createComponent(
      component,
      { injector: modalInjector }
    );
    
    const modalRef = new ModalRef<T>(modalId, this);
    modalRef.componentRef = componentRef;
    
    this.modals.set(modalId, modalRef);
    
    return modalRef;
  }
  
  close(modalId: string, result?: any) {
    const modal = this.modals.get(modalId);
    if (modal) {
      modal.componentRef.destroy();
      this.modals.delete(modalId);
      modal.afterClosed.next(result);
      modal.afterClosed.complete();
    }
  }
  
  private generateId(): string {
    return Math.random().toString(36).substr(2, 9);
  }
}

interface ModalConfig<T = any> {
  data?: T;
  providers?: any[];
  width?: string;
  height?: string;
  disableClose?: boolean;
}

export class ModalRef<T = any> {
  componentRef: any;
  afterClosed = new Subject<T>();
  
  constructor(
    private modalId: string,
    private modalService: ModalService
  ) {}
  
  close(result?: T) {
    this.modalService.close(this.modalId, result);
  }
}

// Modal Component Example
@Component({
  selector: 'app-custom-modal',
  standalone: true,
  template: `
    <div class="modal-overlay">
      <div class="modal-content">
        <h2>{{ modalData.title }}</h2>
        <p>{{ modalData.message }}</p>
        <p>Custom Service Value: {{ customValue }}</p>
        
        <div class="modal-actions">
          <button (click)="onConfirm()">Confirm</button>
          <button (click)="onCancel()">Cancel</button>
        </div>
      </div>
    </div>
  `,
  styles: [`
    .modal-overlay {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-color: rgba(0, 0, 0, 0.5);
      display: flex;
      align-items: center;
      justify-content: center;
    }
    
    .modal-content {
      background: white;
      padding: 20px;
      border-radius: 8px;
      max-width: 400px;
      width: 90%;
    }
    
    .modal-actions {
      display: flex;
      gap: 10px;
      justify-content: flex-end;
      margin-top: 20px;
    }
  `]
})
export class CustomModalComponent {
  modalData = inject('MODAL_DATA');
  modalRef = inject(ModalRef);
  customValue = inject('CUSTOM_SERVICE', { optional: true })?.getValue() || 'No custom service';
  
  onConfirm() {
    this.modalRef.close({ confirmed: true, data: this.modalData });
  }
  
  onCancel() {
    this.modalRef.close({ confirmed: false });
  }
}

// Usage
@Component({
  selector: 'app-modal-example',
  standalone: true,
  template: `
    <button (click)="openModal()">Open Modal with Custom Injector</button>
  `
})
export class ModalExampleComponent {
  constructor(private modalService: ModalService) {}
  
  openModal() {
    const modalRef = this.modalService.open(CustomModalComponent, {
      data: {
        title: 'Custom Modal',
        message: 'This modal has a custom injector context'
      },
      providers: [
        { provide: 'CUSTOM_SERVICE', useValue: { getValue: () => 'Injected Value' } }
      ]
    });
    
    modalRef.afterClosed.subscribe(result => {
      console.log('Modal closed with result:', result);
    });
  }
}
```

This comprehensive guide covers Angular 14's new features and integration patterns, providing practical examples for modern Angular development.

---

## Advanced Angular 14 Integration Patterns

<a id="q5"></a>
### Q5: How do you implement micro-frontend architecture with Angular 14?

**Difficulty**: Intermediate

**Answer:**
Micro-frontend architecture allows teams to develop and deploy frontend applications independently. Angular 14 provides excellent support for this pattern.

**Module Federation Setup:**
```typescript
// webpack.config.js for Shell Application
const ModuleFederationPlugin = require('@module-federation/webpack');

module.exports = {
  mode: 'development',
  devServer: {
    port: 4200,
  },
  plugins: [
    new ModuleFederationPlugin({
      name: 'shell',
      remotes: {
        'mfe1': 'mfe1@http://localhost:4201/remoteEntry.js',
        'mfe2': 'mfe2@http://localhost:4202/remoteEntry.js',
      },
      shared: {
        '@angular/core': { singleton: true, strictVersion: true },
        '@angular/common': { singleton: true, strictVersion: true },
        '@angular/router': { singleton: true, strictVersion: true },
      },
    }),
  ],
};

// webpack.config.js for Micro-frontend
const ModuleFederationPlugin = require('@module-federation/webpack');

module.exports = {
  mode: 'development',
  devServer: {
    port: 4201,
  },
  plugins: [
    new ModuleFederationPlugin({
      name: 'mfe1',
      filename: 'remoteEntry.js',
      exposes: {
        './Component': './src/app/mfe1/mfe1.component.ts',
        './Module': './src/app/mfe1/mfe1.module.ts',
      },
      shared: {
        '@angular/core': { singleton: true, strictVersion: true },
        '@angular/common': { singleton: true, strictVersion: true },
        '@angular/router': { singleton: true, strictVersion: true },
      },
    }),
  ],
};
```

**Dynamic Component Loading:**
```typescript
// Dynamic MFE Loader Service
import { Injectable, ComponentRef, ViewContainerRef } from '@angular/core';
import { loadRemoteModule } from '@module-federation/runtime';

@Injectable({
  providedIn: 'root'
})
export class MicroFrontendLoaderService {
  private loadedComponents = new Map<string, ComponentRef<any>>();

  async loadMicroFrontend(
    containerRef: ViewContainerRef,
    remoteName: string,
    exposedModule: string,
    componentName: string
  ): Promise<ComponentRef<any>> {
    try {
      // Clear existing component
      containerRef.clear();

      // Load remote module
      const module = await loadRemoteModule({
        remoteName,
        exposedModule
      });

      // Get component from module
      const component = module[componentName];
      
      // Create component
      const componentRef = containerRef.createComponent(component);
      
      // Store reference for cleanup
      this.loadedComponents.set(`${remoteName}-${componentName}`, componentRef);
      
      return componentRef;
    } catch (error) {
      console.error(`Failed to load micro-frontend: ${remoteName}`, error);
      throw error;
    }
  }

  unloadMicroFrontend(remoteName: string, componentName: string): void {
    const key = `${remoteName}-${componentName}`;
    const componentRef = this.loadedComponents.get(key);
    
    if (componentRef) {
      componentRef.destroy();
      this.loadedComponents.delete(key);
    }
  }

  unloadAllMicroFrontends(): void {
    this.loadedComponents.forEach(componentRef => componentRef.destroy());
    this.loadedComponents.clear();
  }
}

// Shell Component
@Component({
  selector: 'app-shell',
  template: `
    <nav class="navigation">
      <button (click)="loadMFE('mfe1', 'UserManagement')">User Management</button>
      <button (click)="loadMFE('mfe2', 'ProductCatalog')">Product Catalog</button>
      <button (click)="unloadAll()">Clear All</button>
    </nav>
    
    <div class="mfe-container" #mfeContainer></div>
    
    <div class="error-boundary" *ngIf="error">
      <h3>Error Loading Micro-Frontend</h3>
      <p>{{ error }}</p>
      <button (click)="clearError()">Dismiss</button>
    </div>
  `,
  styles: [`
    .navigation {
      padding: 20px;
      background: #f5f5f5;
      border-bottom: 1px solid #ddd;
    }
    
    .navigation button {
      margin-right: 10px;
      padding: 10px 20px;
      border: none;
      background: #007bff;
      color: white;
      border-radius: 4px;
      cursor: pointer;
    }
    
    .mfe-container {
      padding: 20px;
      min-height: 400px;
    }
    
    .error-boundary {
      background: #f8d7da;
      color: #721c24;
      padding: 20px;
      border: 1px solid #f5c6cb;
      border-radius: 4px;
      margin: 20px;
    }
  `]
})
export class ShellComponent implements OnDestroy {
  @ViewChild('mfeContainer', { read: ViewContainerRef }) 
  mfeContainer!: ViewContainerRef;
  
  error: string | null = null;
  
  constructor(private mfeLoader: MicroFrontendLoaderService) {}
  
  async loadMFE(remoteName: string, componentName: string): Promise<void> {
    try {
      this.error = null;
      await this.mfeLoader.loadMicroFrontend(
        this.mfeContainer,
        remoteName,
        './Component',
        componentName
      );
    } catch (error) {
      this.error = `Failed to load ${componentName} from ${remoteName}`;
      console.error(error);
    }
  }
  
  unloadAll(): void {
    this.mfeLoader.unloadAllMicroFrontends();
    this.mfeContainer.clear();
  }
  
  clearError(): void {
    this.error = null;
  }
  
  ngOnDestroy(): void {
    this.unloadAll();
  }
}
```

**Inter-MFE Communication:**
```typescript
// Shared Event Bus Service
import { Injectable } from '@angular/core';
import { Subject, Observable } from 'rxjs';
import { filter, map } from 'rxjs/operators';

interface MFEEvent {
  type: string;
  source: string;
  target?: string;
  payload: any;
  timestamp: number;
}

@Injectable({
  providedIn: 'root'
})
export class MFEEventBusService {
  private eventSubject = new Subject<MFEEvent>();
  private events$ = this.eventSubject.asObservable();
  
  // Emit event to other MFEs
  emit(type: string, payload: any, source: string, target?: string): void {
    const event: MFEEvent = {
      type,
      source,
      target,
      payload,
      timestamp: Date.now()
    };
    
    this.eventSubject.next(event);
  }
  
  // Listen for specific event types
  on(eventType: string, source?: string): Observable<MFEEvent> {
    return this.events$.pipe(
      filter(event => {
        const typeMatch = event.type === eventType;
        const sourceMatch = !source || event.source === source;
        return typeMatch && sourceMatch;
      })
    );
  }
  
  // Listen for events targeted to specific MFE
  onTargeted(target: string): Observable<MFEEvent> {
    return this.events$.pipe(
      filter(event => event.target === target)
    );
  }
  
  // Get event payload directly
  onPayload<T>(eventType: string, source?: string): Observable<T> {
    return this.on(eventType, source).pipe(
      map(event => event.payload as T)
    );
  }
}

// Usage in MFE1
@Component({
  selector: 'app-user-management',
  template: `
    <div class="user-management">
      <h2>User Management MFE</h2>
      <button (click)="selectUser()">Select User</button>
      <div *ngIf="selectedProduct">
        <h3>Related Product: {{ selectedProduct.name }}</h3>
        <p>Price: {{ selectedProduct.price | currency }}</p>
      </div>
    </div>
  `
})
export class UserManagementComponent implements OnInit, OnDestroy {
  selectedProduct: any = null;
  private destroy$ = new Subject<void>();
  
  constructor(private eventBus: MFEEventBusService) {}
  
  ngOnInit(): void {
    // Listen for product selection from other MFEs
    this.eventBus.onPayload<any>('product-selected')
      .pipe(takeUntil(this.destroy$))
      .subscribe(product => {
        this.selectedProduct = product;
      });
  }
  
  selectUser(): void {
    const user = {
      id: 1,
      name: 'John Doe',
      email: 'john@example.com'
    };
    
    // Emit user selection event
    this.eventBus.emit('user-selected', user, 'mfe1');
  }
  
  ngOnDestroy(): void {
    this.destroy$.next();
    this.destroy$.complete();
  }
}
```

<a id="q6"></a>
### Q6: How do you implement advanced state sharing between Angular 14 applications?

**Difficulty**: Intermediate

**Answer:**
Advanced state sharing involves multiple strategies for different scenarios, from simple cross-component communication to complex distributed state management.

**Cross-Application State Management:**
```typescript
// Shared State Service using BroadcastChannel
import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable, fromEvent } from 'rxjs';
import { map, filter } from 'rxjs/operators';

interface StateMessage {
  type: string;
  payload: any;
  timestamp: number;
  source: string;
}

@Injectable({
  providedIn: 'root'
})
export class CrossAppStateService {
  private channel: BroadcastChannel;
  private localState = new BehaviorSubject<any>({});
  private channelMessages$: Observable<StateMessage>;
  
  constructor() {
    this.channel = new BroadcastChannel('app-state-sync');
    
    // Listen for messages from other app instances
    this.channelMessages$ = fromEvent<MessageEvent>(this.channel, 'message')
      .pipe(
        map(event => event.data as StateMessage),
        filter(message => message.source !== this.getAppId())
      );
    
    // Subscribe to external state changes
    this.channelMessages$.subscribe(message => {
      this.handleExternalStateChange(message);
    });
  }
  
  // Update local state and broadcast to other instances
  updateState(key: string, value: any): void {
    const currentState = this.localState.value;
    const newState = { ...currentState, [key]: value };
    
    this.localState.next(newState);
    
    // Broadcast to other app instances
    this.broadcastStateChange(key, value);
  }
  
  // Get current state
  getState(): Observable<any> {
    return this.localState.asObservable();
  }
  
  // Get specific state slice
  getStateSlice<T>(key: string): Observable<T> {
    return this.localState.pipe(
      map(state => state[key] as T),
      filter(value => value !== undefined)
    );
  }
  
  // Listen for external state changes
  onExternalStateChange(type?: string): Observable<StateMessage> {
    return this.channelMessages$.pipe(
      filter(message => !type || message.type === type)
    );
  }
  
  private broadcastStateChange(key: string, value: any): void {
    const message: StateMessage = {
      type: 'state-update',
      payload: { key, value },
      timestamp: Date.now(),
      source: this.getAppId()
    };
    
    this.channel.postMessage(message);
  }
  
  private handleExternalStateChange(message: StateMessage): void {
    if (message.type === 'state-update') {
      const { key, value } = message.payload;
      const currentState = this.localState.value;
      const newState = { ...currentState, [key]: value };
      
      // Update local state without broadcasting (to avoid loops)
      this.localState.next(newState);
    }
  }
  
  private getAppId(): string {
    // Generate or retrieve unique app instance ID
    if (!sessionStorage.getItem('app-instance-id')) {
      sessionStorage.setItem('app-instance-id', 
        `app-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`);
    }
    return sessionStorage.getItem('app-instance-id')!;
  }
  
  destroy(): void {
    this.channel.close();
  }
}

// Advanced State Synchronization with Conflict Resolution
@Injectable({
  providedIn: 'root'
})
export class AdvancedStateSync {
  private stateVersions = new Map<string, number>();
  private conflictResolver = new Map<string, (local: any, remote: any) => any>();
  
  constructor(private crossAppState: CrossAppStateService) {
    this.setupConflictResolvers();
    this.listenForConflicts();
  }
  
  // Register conflict resolution strategy
  registerConflictResolver(
    key: string, 
    resolver: (local: any, remote: any) => any
  ): void {
    this.conflictResolver.set(key, resolver);
  }
  
  // Update state with versioning
  updateVersionedState(key: string, value: any): void {
    const version = (this.stateVersions.get(key) || 0) + 1;
    this.stateVersions.set(key, version);
    
    const versionedValue = {
      data: value,
      version,
      timestamp: Date.now(),
      source: this.getInstanceId()
    };
    
    this.crossAppState.updateState(key, versionedValue);
  }
  
  private setupConflictResolvers(): void {
    // Last-write-wins resolver
    this.registerConflictResolver('user-preferences', 
      (local, remote) => remote.timestamp > local.timestamp ? remote : local
    );
    
    // Merge resolver for arrays
    this.registerConflictResolver('notifications', 
      (local, remote) => {
        const localIds = new Set(local.data.map((item: any) => item.id));
        const mergedData = [
          ...local.data,
          ...remote.data.filter((item: any) => !localIds.has(item.id))
        ];
        return {
          data: mergedData,
          version: Math.max(local.version, remote.version),
          timestamp: Math.max(local.timestamp, remote.timestamp),
          source: 'merged'
        };
      }
    );
    
    // Custom business logic resolver
    this.registerConflictResolver('shopping-cart', 
      (local, remote) => {
        // Merge cart items, sum quantities for same products
        const mergedItems = new Map();
        
        [...local.data.items, ...remote.data.items].forEach((item: any) => {
          const existing = mergedItems.get(item.productId);
          if (existing) {
            existing.quantity += item.quantity;
          } else {
            mergedItems.set(item.productId, { ...item });
          }
        });
        
        return {
          data: {
            items: Array.from(mergedItems.values()),
            total: Array.from(mergedItems.values())
              .reduce((sum, item) => sum + (item.price * item.quantity), 0)
          },
          version: Math.max(local.version, remote.version) + 1,
          timestamp: Date.now(),
          source: 'conflict-resolved'
        };
      }
    );
  }
  
  private listenForConflicts(): void {
    this.crossAppState.onExternalStateChange('state-update')
      .subscribe(message => {
        const { key, value: remoteValue } = message.payload;
        
        this.crossAppState.getStateSlice(key).pipe(
          take(1)
        ).subscribe(localValue => {
          if (localValue && this.hasConflict(localValue, remoteValue)) {
            this.resolveConflict(key, localValue, remoteValue);
          }
        });
      });
  }
  
  private hasConflict(local: any, remote: any): boolean {
    return local.version !== remote.version && 
           local.source !== remote.source;
  }
  
  private resolveConflict(key: string, local: any, remote: any): void {
    const resolver = this.conflictResolver.get(key);
    
    if (resolver) {
      const resolved = resolver(local, remote);
      this.crossAppState.updateState(key, resolved);
    } else {
      // Default: use timestamp-based resolution
      const winner = remote.timestamp > local.timestamp ? remote : local;
      this.crossAppState.updateState(key, winner);
    }
  }
  
  private getInstanceId(): string {
    return sessionStorage.getItem('app-instance-id') || 'unknown';
  }
}
```

<a id="q7"></a>
### Q7: How do you implement real-time collaboration features in Angular 14?

**Difficulty**: Intermediate

**Answer:**
Real-time collaboration requires WebSocket connections, operational transformation, and conflict resolution strategies.

**Real-time Collaboration Service:**
```typescript
// WebSocket-based Collaboration Service
import { Injectable } from '@angular/core';
import { Observable, Subject, BehaviorSubject } from 'rxjs';
import { webSocket, WebSocketSubject } from 'rxjs/webSocket';
import { retry, catchError } from 'rxjs/operators';

interface CollaborationEvent {
  type: 'operation' | 'cursor' | 'selection' | 'user-join' | 'user-leave';
  userId: string;
  documentId: string;
  operation?: Operation;
  cursor?: CursorPosition;
  selection?: SelectionRange;
  timestamp: number;
}

interface Operation {
  type: 'insert' | 'delete' | 'retain';
  position: number;
  content?: string;
  length?: number;
  attributes?: any;
}

interface CursorPosition {
  line: number;
  column: number;
  color: string;
}

interface SelectionRange {
  start: { line: number; column: number };
  end: { line: number; column: number };
  color: string;
}

@Injectable({
  providedIn: 'root'
})
export class CollaborationService {
  private socket$: WebSocketSubject<any> | null = null;
  private connectionStatus$ = new BehaviorSubject<'connected' | 'disconnected' | 'connecting'>('disconnected');
  private collaborationEvents$ = new Subject<CollaborationEvent>();
  private activeUsers$ = new BehaviorSubject<Map<string, any>>(new Map());
  
  private currentUserId: string;
  private currentDocumentId: string | null = null;
  
  constructor() {
    this.currentUserId = this.generateUserId();
  }
  
  // Connect to collaboration server
  connect(documentId: string, wsUrl: string): Observable<CollaborationEvent> {
    this.currentDocumentId = documentId;
    this.connectionStatus$.next('connecting');
    
    this.socket$ = webSocket({
      url: `${wsUrl}?documentId=${documentId}&userId=${this.currentUserId}`,
      openObserver: {
        next: () => {
          this.connectionStatus$.next('connected');
          this.joinDocument(documentId);
        }
      },
      closeObserver: {
        next: () => {
          this.connectionStatus$.next('disconnected');
        }
      }
    });
    
    // Handle incoming messages
    this.socket$.pipe(
      retry({ delay: 3000 }),
      catchError(error => {
        console.error('WebSocket error:', error);
        this.connectionStatus$.next('disconnected');
        throw error;
      })
    ).subscribe(event => {
      this.handleCollaborationEvent(event);
    });
    
    return this.collaborationEvents$.asObservable();
  }
  
  // Send operation to other collaborators
  sendOperation(operation: Operation): void {
    if (this.socket$ && this.currentDocumentId) {
      const event: CollaborationEvent = {
        type: 'operation',
        userId: this.currentUserId,
        documentId: this.currentDocumentId,
        operation,
        timestamp: Date.now()
      };
      
      this.socket$.next(event);
    }
  }
  
  // Send cursor position
  sendCursorPosition(cursor: CursorPosition): void {
    if (this.socket$ && this.currentDocumentId) {
      const event: CollaborationEvent = {
        type: 'cursor',
        userId: this.currentUserId,
        documentId: this.currentDocumentId,
        cursor,
        timestamp: Date.now()
      };
      
      this.socket$.next(event);
    }
  }
  
  // Send selection range
  sendSelection(selection: SelectionRange): void {
    if (this.socket$ && this.currentDocumentId) {
      const event: CollaborationEvent = {
        type: 'selection',
        userId: this.currentUserId,
        documentId: this.currentDocumentId,
        selection,
        timestamp: Date.now()
      };
      
      this.socket$.next(event);
    }
  }
  
  // Get connection status
  getConnectionStatus(): Observable<'connected' | 'disconnected' | 'connecting'> {
    return this.connectionStatus$.asObservable();
  }
  
  // Get active users
  getActiveUsers(): Observable<Map<string, any>> {
    return this.activeUsers$.asObservable();
  }
  
  // Disconnect from collaboration
  disconnect(): void {
    if (this.socket$) {
      this.socket$.complete();
      this.socket$ = null;
    }
    this.connectionStatus$.next('disconnected');
    this.activeUsers$.next(new Map());
  }
  
  private joinDocument(documentId: string): void {
    if (this.socket$) {
      this.socket$.next({
        type: 'user-join',
        userId: this.currentUserId,
        documentId,
        userInfo: {
          name: this.getUserName(),
          avatar: this.getUserAvatar(),
          color: this.getUserColor()
        },
        timestamp: Date.now()
      });
    }
  }
  
  private handleCollaborationEvent(event: CollaborationEvent): void {
    // Don't process our own events
    if (event.userId === this.currentUserId) {
      return;
    }
    
    switch (event.type) {
      case 'user-join':
        this.handleUserJoin(event);
        break;
      case 'user-leave':
        this.handleUserLeave(event);
        break;
      default:
        this.collaborationEvents$.next(event);
    }
  }
  
  private handleUserJoin(event: CollaborationEvent): void {
    const users = this.activeUsers$.value;
    users.set(event.userId, {
      id: event.userId,
      ...event,
      joinedAt: event.timestamp
    });
    this.activeUsers$.next(new Map(users));
    this.collaborationEvents$.next(event);
  }
  
  private handleUserLeave(event: CollaborationEvent): void {
    const users = this.activeUsers$.value;
    users.delete(event.userId);
    this.activeUsers$.next(new Map(users));
    this.collaborationEvents$.next(event);
  }
  
  private generateUserId(): string {
    return `user-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
  }
  
  private getUserName(): string {
    return localStorage.getItem('userName') || 'Anonymous User';
  }
  
  private getUserAvatar(): string {
    return localStorage.getItem('userAvatar') || '/assets/default-avatar.png';
  }
  
  private getUserColor(): string {
    const colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD'];
    const index = this.currentUserId.charCodeAt(0) % colors.length;
    return colors[index];
  }
}

// Operational Transformation for Text Editing
@Injectable({
  providedIn: 'root'
})
export class OperationalTransformService {
  // Transform operation against another operation
  transform(op1: Operation, op2: Operation): [Operation, Operation] {
    if (op1.type === 'retain' && op2.type === 'retain') {
      return [op1, op2];
    }
    
    if (op1.type === 'insert' && op2.type === 'insert') {
      if (op1.position <= op2.position) {
        return [
          op1,
          { ...op2, position: op2.position + (op1.content?.length || 0) }
        ];
      } else {
        return [
          { ...op1, position: op1.position + (op2.content?.length || 0) },
          op2
        ];
      }
    }
    
    if (op1.type === 'delete' && op2.type === 'delete') {
      if (op1.position <= op2.position) {
        return [
          op1,
          { ...op2, position: Math.max(op2.position - (op1.length || 0), op1.position) }
        ];
      } else {
        return [
          { ...op1, position: Math.max(op1.position - (op2.length || 0), op2.position) },
          op2
        ];
      }
    }
    
    if (op1.type === 'insert' && op2.type === 'delete') {
      if (op1.position <= op2.position) {
        return [
          op1,
          { ...op2, position: op2.position + (op1.content?.length || 0) }
        ];
      } else {
        return [
          { ...op1, position: Math.max(op1.position - (op2.length || 0), op2.position) },
          op2
        ];
      }
    }
    
    if (op1.type === 'delete' && op2.type === 'insert') {
      if (op1.position <= op2.position) {
        return [
          op1,
          { ...op2, position: Math.max(op2.position - (op1.length || 0), op1.position) }
        ];
      } else {
        return [
          { ...op1, position: op1.position + (op2.content?.length || 0) },
          op2
        ];
      }
    }
    
    return [op1, op2];
  }
  
  // Apply operation to text
  applyOperation(text: string, operation: Operation): string {
    switch (operation.type) {
      case 'insert':
        return text.slice(0, operation.position) + 
               (operation.content || '') + 
               text.slice(operation.position);
      
      case 'delete':
        return text.slice(0, operation.position) + 
               text.slice(operation.position + (operation.length || 0));
      
      case 'retain':
        return text;
      
      default:
        return text;
    }
  }
  
  // Compose multiple operations
  composeOperations(ops: Operation[]): Operation[] {
    if (ops.length === 0) return [];
    if (ops.length === 1) return ops;
    
    const result: Operation[] = [];
    let current = ops[0];
    
    for (let i = 1; i < ops.length; i++) {
      const next = ops[i];
      
      // Try to merge operations
      if (this.canMerge(current, next)) {
        current = this.mergeOperations(current, next);
      } else {
        result.push(current);
        current = next;
      }
    }
    
    result.push(current);
    return result;
  }
  
  private canMerge(op1: Operation, op2: Operation): boolean {
    if (op1.type !== op2.type) return false;
    
    if (op1.type === 'insert' && op2.type === 'insert') {
      return op1.position + (op1.content?.length || 0) === op2.position;
    }
    
    if (op1.type === 'delete' && op2.type === 'delete') {
      return op1.position === op2.position;
    }
    
    return false;
  }
  
  private mergeOperations(op1: Operation, op2: Operation): Operation {
    if (op1.type === 'insert' && op2.type === 'insert') {
      return {
        type: 'insert',
        position: op1.position,
        content: (op1.content || '') + (op2.content || '')
      };
    }
    
    if (op1.type === 'delete' && op2.type === 'delete') {
      return {
        type: 'delete',
        position: op1.position,
        length: (op1.length || 0) + (op2.length || 0)
      };
    }
    
    return op1;
  }
}
```

<a id="q8"></a>
### Q8: How would you implement advanced Angular 14+ integration with modern development tools and CI/CD pipelines?

**Difficulty**: Intermediate

**Answer:**
Advanced Angular 14+ integration involves sophisticated tooling, automated workflows, and modern development practices to ensure scalable, maintainable, and high-performance applications.

**Modern Development Toolchain Integration:**

1. **Advanced Angular CLI Workspace Configuration:**
```json
// angular.json - Advanced workspace configuration
{
  "version": 1,
  "newProjectRoot": "projects",
  "projects": {
    "main-app": {
      "projectType": "application",
      "schematics": {
        "@schematics/angular:component": {
          "style": "scss",
          "standalone": true,
          "changeDetection": "OnPush"
        },
        "@schematics/angular:directive": {
          "standalone": true
        },
        "@schematics/angular:pipe": {
          "standalone": true
        }
      },
      "architect": {
        "build": {
          "builder": "@angular-devkit/build-angular:browser-esbuild",
          "options": {
            "outputPath": "dist/main-app",
            "index": "src/index.html",
            "main": "src/main.ts",
            "polyfills": ["zone.js"],
            "tsConfig": "tsconfig.app.json",
            "assets": [
              "src/favicon.ico",
              "src/assets",
              {
                "glob": "**/*",
                "input": "node_modules/@angular/material/prebuilt-themes/",
                "output": "/assets/themes/"
              }
            ],
            "styles": [
              "@angular/material/prebuilt-themes/indigo-pink.css",
              "src/styles.scss"
            ],
            "scripts": [],
            "budgets": [
              {
                "type": "initial",
                "maximumWarning": "500kb",
                "maximumError": "1mb"
              },
              {
                "type": "anyComponentStyle",
                "maximumWarning": "2kb",
                "maximumError": "4kb"
              }
            ],
            "optimization": {
              "scripts": true,
              "styles": {
                "minify": true,
                "inlineCritical": true
              },
              "fonts": true
            },
            "sourceMap": false,
            "namedChunks": false,
            "aot": true,
            "extractLicenses": true,
            "vendorChunk": false,
            "buildOptimizer": true
          },
          "configurations": {
            "production": {
              "fileReplacements": [
                {
                  "replace": "src/environments/environment.ts",
                  "with": "src/environments/environment.prod.ts"
                }
              ],
              "serviceWorker": true,
              "ngswConfigPath": "ngsw-config.json"
            },
            "development": {
              "buildOptimizer": false,
              "optimization": false,
              "vendorChunk": true,
              "extractLicenses": false,
              "sourceMap": true,
              "namedChunks": true
            }
          }
        },
        "test": {
          "builder": "@angular-devkit/build-angular:karma",
          "options": {
            "main": "src/test.ts",
            "polyfills": ["zone.js", "zone.js/testing"],
            "tsConfig": "tsconfig.spec.json",
            "karmaConfig": "karma.conf.js",
            "assets": ["src/favicon.ico", "src/assets"],
            "styles": ["src/styles.scss"],
            "scripts": [],
            "codeCoverage": true,
            "browsers": "ChromeHeadless"
          }
        },
        "lint": {
          "builder": "@angular-eslint/builder:lint",
          "options": {
            "lintFilePatterns": ["src/**/*.ts", "src/**/*.html"]
          }
        },
        "e2e": {
          "builder": "@cypress/schematic:cypress",
          "options": {
            "devServerTarget": "main-app:serve",
            "watch": true,
            "headless": false
          },
          "configurations": {
            "production": {
              "devServerTarget": "main-app:serve:production",
              "headless": true
            }
          }
        }
      }
    }
  },
  "cli": {
    "analytics": false,
    "cache": {
      "enabled": true,
      "path": ".angular/cache",
      "environment": "all"
    },
    "completion": {
      "prompted": true
    },
    "schematicCollections": [
      "@angular-eslint/schematics",
      "@ngrx/schematics"
    ]
  }
}
```

2. **Advanced ESBuild Integration:**
```typescript
// esbuild.config.ts - Custom ESBuild configuration
import { BuildOptions } from 'esbuild';
import { sassPlugin } from 'esbuild-sass-plugin';
import { copy } from 'esbuild-plugin-copy';

export const esbuildConfig: BuildOptions = {
  entryPoints: ['src/main.ts'],
  bundle: true,
  outdir: 'dist',
  format: 'esm',
  target: 'es2020',
  platform: 'browser',
  splitting: true,
  chunkNames: 'chunks/[name]-[hash]',
  assetNames: 'assets/[name]-[hash]',
  metafile: true,
  sourcemap: true,
  minify: process.env['NODE_ENV'] === 'production',
  treeShaking: true,
  plugins: [
    sassPlugin({
      filter: /\.(s[ac]ss|css)$/,
      type: 'css',
      cache: true
    }),
    copy({
      resolveFrom: 'cwd',
      assets: [
        {
          from: ['src/assets/**/*'],
          to: ['dist/assets']
        },
        {
          from: ['src/favicon.ico'],
          to: ['dist']
        }
      ]
    })
  ],
  define: {
    'process.env.NODE_ENV': JSON.stringify(process.env['NODE_ENV'] || 'development'),
    'process.env.API_URL': JSON.stringify(process.env['API_URL'] || 'http://localhost:3000')
  },
  external: [
    // Mark certain dependencies as external if needed
  ],
  loader: {
    '.png': 'file',
    '.jpg': 'file',
    '.jpeg': 'file',
    '.gif': 'file',
    '.svg': 'file',
    '.woff': 'file',
    '.woff2': 'file',
    '.ttf': 'file',
    '.eot': 'file'
  },
  banner: {
    js: '/* Angular Application Bundle */'
  }
};
```

3. **Advanced CI/CD Pipeline Integration:**
```yaml
# .github/workflows/ci-cd.yml - GitHub Actions workflow
name: Angular CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  NODE_VERSION: '18.x'
  CACHE_KEY: 'node-modules'

jobs:
  lint-and-test:
    runs-on: ubuntu-latest
    
    strategy:
      matrix:
        node-version: [16.x, 18.x, 20.x]
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        with:
          fetch-depth: 0
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
          cache: 'npm'
      
      - name: Install dependencies
        run: |
          npm ci --prefer-offline --no-audit
          npx ngcc --properties es2020 browser module main
      
      - name: Lint code
        run: |
          npm run lint
          npm run lint:html
      
      - name: Run unit tests
        run: |
          npm run test:ci
          npm run test:coverage
      
      - name: Upload coverage reports
        uses: codecov/codecov-action@v3
        with:
          file: ./coverage/lcov.info
          flags: unittests
          name: codecov-umbrella
      
      - name: Run e2e tests
        run: |
          npm run e2e:ci
      
      - name: Build application
        run: |
          npm run build:prod
      
      - name: Analyze bundle
        run: |
          npm run analyze
          npm run lighthouse:ci
      
      - name: Security audit
        run: |
          npm audit --audit-level=high
          npm run security:check
  
  build-and-deploy:
    needs: lint-and-test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci --prefer-offline --no-audit
      
      - name: Build for production
        run: |
          npm run build:prod
          npm run prerender
      
      - name: Build Docker image
        run: |
          docker build -t angular-app:${{ github.sha }} .
          docker tag angular-app:${{ github.sha }} angular-app:latest
      
      - name: Run security scan
        run: |
          docker run --rm -v /var/run/docker.sock:/var/run/docker.sock \
            -v $PWD:/tmp/.cache/ aquasec/trivy:latest image \
            --exit-code 0 --no-progress --format table \
            angular-app:${{ github.sha }}
      
      - name: Deploy to staging
        if: github.ref == 'refs/heads/develop'
        run: |
          echo "Deploying to staging environment"
          # Add staging deployment commands
      
      - name: Deploy to production
        if: github.ref == 'refs/heads/main'
        run: |
          echo "Deploying to production environment"
          # Add production deployment commands
      
      - name: Notify deployment
        uses: 8398a7/action-slack@v3
        with:
          status: ${{ job.status }}
          channel: '#deployments'
          webhook_url: ${{ secrets.SLACK_WEBHOOK }}
```

4. **Advanced Development Tools Integration:**
```typescript
// tools/dev-server.ts - Custom development server
import { createServer } from 'vite';
import { angular } from '@analogjs/vite-plugin-angular';
import { defineConfig } from 'vite';

export const devServerConfig = defineConfig({
  plugins: [
    angular({
      tsconfig: 'tsconfig.app.json',
      workspaceRoot: process.cwd(),
      inlineStylesExtension: 'scss'
    })
  ],
  server: {
    port: 4200,
    host: '0.0.0.0',
    hmr: {
      port: 4201
    },
    proxy: {
      '/api': {
        target: 'http://localhost:3000',
        changeOrigin: true,
        secure: false,
        ws: true
      }
    }
  },
  build: {
    target: 'es2020',
    outDir: 'dist',
    sourcemap: true,
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['@angular/core', '@angular/common', '@angular/platform-browser'],
          material: ['@angular/material'],
          rxjs: ['rxjs']
        }
      }
    }
  },
  optimizeDeps: {
    include: [
      '@angular/core',
      '@angular/common',
      '@angular/platform-browser',
      '@angular/material',
      'rxjs'
    ]
  },
  define: {
    'import.meta.env.VITE_API_URL': JSON.stringify(process.env['API_URL'] || 'http://localhost:3000')
  }
});

// Custom development middleware
export class DevServerMiddleware {
  static setupMiddleware(app: any) {
    // API mocking middleware
    app.use('/api/mock', (req: any, res: any, next: any) => {
      const mockData = this.generateMockData(req.path);
      res.json(mockData);
    });
    
    // Performance monitoring middleware
    app.use('/api/performance', (req: any, res: any, next: any) => {
      const performanceData = this.collectPerformanceMetrics();
      res.json(performanceData);
    });
    
    // Hot reload middleware for standalone components
    app.use('/api/hmr', (req: any, res: any, next: any) => {
      this.handleHotModuleReplacement(req, res);
    });
  }
  
  private static generateMockData(path: string): any {
    // Generate mock data based on API path
    const mockResponses = {
      '/users': [
        { id: 1, name: 'John Doe', email: 'john@example.com' },
        { id: 2, name: 'Jane Smith', email: 'jane@example.com' }
      ],
      '/products': [
        { id: 1, name: 'Product 1', price: 99.99 },
        { id: 2, name: 'Product 2', price: 149.99 }
      ]
    };
    
    return mockResponses[path] || { message: 'Mock data not found' };
  }
  
  private static collectPerformanceMetrics(): any {
    return {
      timestamp: Date.now(),
      memory: process.memoryUsage(),
      uptime: process.uptime()
    };
  }
  
  private static handleHotModuleReplacement(req: any, res: any): void {
    // Handle HMR for Angular standalone components
    res.json({ status: 'HMR enabled', timestamp: Date.now() });
  }
}
```

<a id="q9"></a>
### Q9: How would you implement advanced Angular 14+ integration with modern monitoring, analytics, and observability tools?

**Difficulty**: Intermediate

**Answer:**
Advanced monitoring and observability integration involves comprehensive tracking, real-time analytics, and intelligent alerting to ensure optimal application performance and user experience.

**Comprehensive Observability Integration:**

1. **Advanced Application Performance Monitoring:**
```typescript
// monitoring/apm.service.ts - Advanced APM integration
import { Injectable } from '@angular/core';
import { Router, NavigationEnd } from '@angular/router';
import { HttpInterceptor, HttpRequest, HttpHandler, HttpResponse, HttpErrorResponse } from '@angular/common/http';
import { Observable, BehaviorSubject, fromEvent } from 'rxjs';
import { filter, tap, catchError, map } from 'rxjs/operators';

@Injectable({ providedIn: 'root' })
export class AdvancedAPMService {
  private performanceObserver: PerformanceObserver;
  private metricsSubject = new BehaviorSubject<PerformanceMetrics>({});
  private errorTracker = new Map<string, ErrorMetric>();
  
  constructor(private router: Router) {
    this.initializeAPM();
    this.setupRouteTracking();
    this.setupErrorTracking();
    this.setupUserInteractionTracking();
  }
  
  private initializeAPM() {
    // Initialize performance observer
    this.performanceObserver = new PerformanceObserver((list) => {
      for (const entry of list.getEntries()) {
        this.processPerformanceEntry(entry);
      }
    });
    
    this.performanceObserver.observe({
      entryTypes: [
        'navigation',
        'resource',
        'paint',
        'largest-contentful-paint',
        'first-input',
        'layout-shift',
        'long-animation-frame',
        'user-timing',
        'measure'
      ]
    });
    
    // Track Core Web Vitals
    this.trackCoreWebVitals();
    
    // Setup real-time monitoring
    this.setupRealTimeMonitoring();
  }
  
  private trackCoreWebVitals() {
    // Largest Contentful Paint (LCP)
    new PerformanceObserver((entryList) => {
      const entries = entryList.getEntries();
      const lastEntry = entries[entries.length - 1];
      
      this.sendMetric({
        name: 'LCP',
        value: lastEntry.startTime,
        timestamp: Date.now(),
        url: window.location.href,
        rating: this.getRating('LCP', lastEntry.startTime)
      });
    }).observe({ entryTypes: ['largest-contentful-paint'] });
    
    // First Input Delay (FID)
    new PerformanceObserver((entryList) => {
      for (const entry of entryList.getEntries()) {
        const fid = entry.processingStart - entry.startTime;
        
        this.sendMetric({
          name: 'FID',
          value: fid,
          timestamp: Date.now(),
          url: window.location.href,
          rating: this.getRating('FID', fid)
        });
      }
    }).observe({ entryTypes: ['first-input'] });
    
    // Cumulative Layout Shift (CLS)
    let clsValue = 0;
    new PerformanceObserver((entryList) => {
      for (const entry of entryList.getEntries()) {
        if (!(entry as any).hadRecentInput) {
          clsValue += (entry as any).value;
        }
      }
      
      this.sendMetric({
        name: 'CLS',
        value: clsValue,
        timestamp: Date.now(),
        url: window.location.href,
        rating: this.getRating('CLS', clsValue)
      });
    }).observe({ entryTypes: ['layout-shift'] });
  }
  
  private setupRouteTracking() {
    this.router.events
      .pipe(
        filter(event => event instanceof NavigationEnd),
        tap((event: NavigationEnd) => {
          this.trackPageView({
            url: event.url,
            timestamp: Date.now(),
            loadTime: performance.now(),
            referrer: document.referrer,
            userAgent: navigator.userAgent
          });
        })
      )
      .subscribe();
  }
  
  private setupErrorTracking() {
    // Global error handler
    window.addEventListener('error', (event) => {
      this.trackError({
        type: 'javascript',
        message: event.message,
        filename: event.filename,
        lineno: event.lineno,
        colno: event.colno,
        stack: event.error?.stack,
        timestamp: Date.now(),
        url: window.location.href,
        userAgent: navigator.userAgent
      });
    });
    
    // Unhandled promise rejection handler
    window.addEventListener('unhandledrejection', (event) => {
      this.trackError({
        type: 'promise',
        message: event.reason?.message || 'Unhandled Promise Rejection',
        stack: event.reason?.stack,
        timestamp: Date.now(),
        url: window.location.href,
        userAgent: navigator.userAgent
      });
    });
  }
  
  private setupUserInteractionTracking() {
    // Track user interactions
    const interactionEvents = ['click', 'scroll', 'keydown', 'touchstart'];
    
    interactionEvents.forEach(eventType => {
      fromEvent(document, eventType)
        .pipe(
          tap((event) => {
            this.trackUserInteraction({
              type: eventType,
              target: (event.target as Element)?.tagName,
              timestamp: Date.now(),
              url: window.location.href
            });
          })
        )
        .subscribe();
    });
  }
  
  private setupRealTimeMonitoring() {
    // Monitor memory usage
    setInterval(() => {
      if ('memory' in performance) {
        const memory = (performance as any).memory;
        
        this.sendMetric({
          name: 'Memory',
          value: memory.usedJSHeapSize,
          metadata: {
            totalJSHeapSize: memory.totalJSHeapSize,
            jsHeapSizeLimit: memory.jsHeapSizeLimit,
            usagePercentage: (memory.usedJSHeapSize / memory.jsHeapSizeLimit) * 100
          },
          timestamp: Date.now()
        });
      }
    }, 30000);
    
    // Monitor network quality
    if ('connection' in navigator) {
      const connection = (navigator as any).connection;
      
      connection.addEventListener('change', () => {
        this.sendMetric({
          name: 'NetworkQuality',
          value: connection.downlink,
          metadata: {
            effectiveType: connection.effectiveType,
            rtt: connection.rtt,
            saveData: connection.saveData
          },
          timestamp: Date.now()
        });
      });
    }
  }
  
  private getRating(metric: string, value: number): 'good' | 'needs-improvement' | 'poor' {
    const thresholds = {
      LCP: { good: 2500, poor: 4000 },
      FID: { good: 100, poor: 300 },
      CLS: { good: 0.1, poor: 0.25 }
    };
    
    const threshold = thresholds[metric];
    if (!threshold) return 'good';
    
    if (value <= threshold.good) return 'good';
    if (value <= threshold.poor) return 'needs-improvement';
    return 'poor';
  }
  
  private sendMetric(metric: any) {
    // Send to analytics service
    this.sendToAnalytics(metric);
    
    // Send to APM service
    this.sendToAPM(metric);
    
    // Update local metrics
    this.metricsSubject.next(metric);
  }
  
  private sendToAnalytics(data: any) {
    // Google Analytics 4 integration
    if (typeof gtag !== 'undefined') {
      gtag('event', data.name, {
        custom_parameter_1: data.value,
        custom_parameter_2: data.rating
      });
    }
    
    // Custom analytics endpoint
    fetch('/api/analytics', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    }).catch(console.error);
  }
  
  private sendToAPM(data: any) {
    // New Relic integration
    if (typeof newrelic !== 'undefined') {
      newrelic.addPageAction(data.name, data);
    }
    
    // Datadog integration
    if (typeof DD_RUM !== 'undefined') {
      DD_RUM.addAction(data.name, data);
    }
    
    // Custom APM endpoint
    fetch('/api/apm', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    }).catch(console.error);
  }
  
  trackPageView(data: any) {
    this.sendMetric({
      name: 'PageView',
      ...data
    });
  }
  
  trackError(error: any) {
    const errorKey = `${error.message}-${error.filename}-${error.lineno}`;
    const existingError = this.errorTracker.get(errorKey);
    
    if (existingError) {
      existingError.count++;
      existingError.lastOccurrence = Date.now();
    } else {
      this.errorTracker.set(errorKey, {
        ...error,
        count: 1,
        firstOccurrence: Date.now(),
        lastOccurrence: Date.now()
      });
    }
    
    this.sendMetric({
      name: 'Error',
      ...error,
      count: this.errorTracker.get(errorKey)?.count
    });
  }
  
  trackUserInteraction(interaction: any) {
    this.sendMetric({
      name: 'UserInteraction',
      ...interaction
    });
  }
}
```

2. **Advanced HTTP Interceptor for API Monitoring:**
```typescript
// monitoring/http-monitoring.interceptor.ts
import { Injectable } from '@angular/core';
import { HttpInterceptor, HttpRequest, HttpHandler, HttpEvent, HttpResponse, HttpErrorResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { tap, catchError, finalize } from 'rxjs/operators';

@Injectable()
export class HttpMonitoringInterceptor implements HttpInterceptor {
  private activeRequests = new Map<string, RequestMetric>();
  
  constructor(private apmService: AdvancedAPMService) {}
  
  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    const requestId = this.generateRequestId();
    const startTime = performance.now();
    
    // Track request start
    this.activeRequests.set(requestId, {
      url: req.url,
      method: req.method,
      startTime,
      headers: this.sanitizeHeaders(req.headers)
    });
    
    return next.handle(req).pipe(
      tap(event => {
        if (event instanceof HttpResponse) {
          this.trackSuccessfulRequest(requestId, event, startTime);
        }
      }),
      catchError(error => {
        if (error instanceof HttpErrorResponse) {
          this.trackFailedRequest(requestId, error, startTime);
        }
        throw error;
      }),
      finalize(() => {
        this.activeRequests.delete(requestId);
      })
    );
  }
  
  private trackSuccessfulRequest(requestId: string, response: HttpResponse<any>, startTime: number) {
    const request = this.activeRequests.get(requestId);
    if (!request) return;
    
    const duration = performance.now() - startTime;
    
    this.apmService.sendMetric({
      name: 'HTTPRequest',
      type: 'success',
      url: request.url,
      method: request.method,
      statusCode: response.status,
      duration,
      responseSize: this.getResponseSize(response),
      timestamp: Date.now(),
      rating: this.getRating(duration)
    });
  }
  
  private trackFailedRequest(requestId: string, error: HttpErrorResponse, startTime: number) {
    const request = this.activeRequests.get(requestId);
    if (!request) return;
    
    const duration = performance.now() - startTime;
    
    this.apmService.sendMetric({
      name: 'HTTPRequest',
      type: 'error',
      url: request.url,
      method: request.method,
      statusCode: error.status,
      errorMessage: error.message,
      duration,
      timestamp: Date.now()
    });
  }
  
  private generateRequestId(): string {
    return `req_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
  }
  
  private sanitizeHeaders(headers: any): any {
    const sanitized = {};
    headers.keys().forEach(key => {
      if (!this.isSensitiveHeader(key)) {
        sanitized[key] = headers.get(key);
      }
    });
    return sanitized;
  }
  
  private isSensitiveHeader(headerName: string): boolean {
    const sensitiveHeaders = ['authorization', 'cookie', 'x-api-key'];
    return sensitiveHeaders.includes(headerName.toLowerCase());
  }
  
  private getResponseSize(response: HttpResponse<any>): number {
    const contentLength = response.headers.get('content-length');
    return contentLength ? parseInt(contentLength, 10) : 0;
  }
  
  private getRating(duration: number): 'fast' | 'average' | 'slow' {
    if (duration < 200) return 'fast';
    if (duration < 1000) return 'average';
    return 'slow';
  }
}
```

3. **Advanced Analytics Dashboard Integration:**
```typescript
// analytics/dashboard.service.ts
import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable, interval } from 'rxjs';
import { map, switchMap } from 'rxjs/operators';

@Injectable({ providedIn: 'root' })
export class AnalyticsDashboardService {
  private dashboardData$ = new BehaviorSubject<DashboardData>({});
  private realTimeMetrics$ = new BehaviorSubject<RealTimeMetrics>({});
  
  constructor(private apmService: AdvancedAPMService) {
    this.initializeRealTimeUpdates();
  }
  
  private initializeRealTimeUpdates() {
    // Update dashboard every 30 seconds
    interval(30000)
      .pipe(
        switchMap(() => this.fetchDashboardData())
      )
      .subscribe(data => {
        this.dashboardData$.next(data);
      });
    
    // Update real-time metrics every 5 seconds
    interval(5000)
      .pipe(
        switchMap(() => this.fetchRealTimeMetrics())
      )
      .subscribe(metrics => {
        this.realTimeMetrics$.next(metrics);
      });
  }
  
  getDashboardData(): Observable<DashboardData> {
    return this.dashboardData$.asObservable();
  }
  
  getRealTimeMetrics(): Observable<RealTimeMetrics> {
    return this.realTimeMetrics$.asObservable();
  }
  
  private async fetchDashboardData(): Promise<DashboardData> {
    try {
      const response = await fetch('/api/analytics/dashboard');
      return await response.json();
    } catch (error) {
      console.error('Failed to fetch dashboard data:', error);
      return {};
    }
  }
  
  private async fetchRealTimeMetrics(): Promise<RealTimeMetrics> {
    try {
      const response = await fetch('/api/analytics/realtime');
      return await response.json();
    } catch (error) {
      console.error('Failed to fetch real-time metrics:', error);
      return {};
    }
  }
  
  generateReport(timeRange: string, metrics: string[]): Observable<AnalyticsReport> {
    return this.fetchReport(timeRange, metrics);
  }
  
  private fetchReport(timeRange: string, metrics: string[]): Observable<AnalyticsReport> {
    return new Observable(observer => {
      fetch('/api/analytics/report', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ timeRange, metrics })
      })
      .then(response => response.json())
      .then(data => {
        observer.next(data);
        observer.complete();
      })
      .catch(error => {
        observer.error(error);
      });
    });
  }
}

// Types for analytics
interface DashboardData {
  pageViews?: number;
  uniqueUsers?: number;
  averageLoadTime?: number;
  errorRate?: number;
  topPages?: Array<{ url: string; views: number }>;
  performanceMetrics?: {
    lcp: number;
    fid: number;
    cls: number;
  };
}

interface RealTimeMetrics {
  activeUsers?: number;
  currentPageViews?: number;
  realtimeErrors?: number;
  serverResponseTime?: number;
}

interface AnalyticsReport {
  summary: any;
  charts: any[];
  tables: any[];
  insights: string[];
}
```

This comprehensive integration guide now covers advanced Angular 14 patterns including micro-frontend architecture, cross-application state management, real-time collaboration features, modern development toolchain integration, advanced CI/CD pipelines, comprehensive monitoring and observability, and analytics dashboard integration with practical implementation examples.

---

<a id="q10"></a>
### Q10: How do you integrate Angular with Firebase using AngularFire?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Integration Steps:**

1.  **Install:** `ng add @angular/fire`
2.  **Configuration:** Set up `firebase` config in `environment.ts`.
3.  **Setup (Standalone):**
```typescript
// app.config.ts
import { provideFirebaseApp, initializeApp } from '@angular/fire/app';
import { provideFirestore, getFirestore } from '@angular/fire/firestore';

export const appConfig: ApplicationConfig = {
  providers: [
    provideFirebaseApp(() => initializeApp(environment.firebase)),
    provideFirestore(() => getFirestore())
  ]
};
```
4.  **Usage:** Inject `Firestore` service to interact with the database.

---

<a id="q11"></a>
### Q11: How do you integrate Redux DevTools with NgRx?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Integration:**

1.  **Install:** `npm install @ngrx/store-devtools --save-dev`
2.  **Register:**
```typescript
// app.config.ts
import { provideStoreDevtools } from '@ngrx/store-devtools';

export const appConfig: ApplicationConfig = {
  providers: [
    provideStore(),
    provideStoreDevtools({
      maxAge: 25, // Retains last 25 states
      logOnly: !isDevMode(), // Restrict extension to log-only mode
      autoPause: true, // Pauses recording actions and state changes when the extension window is not open
      trace: false, //  If set to true, will include stack trace for every dispatched action
      traceLimit: 75, // maximum stack trace frames to be stored (in case trace option was provided as true)
    })
  ]
};
```

---

<a id="q12"></a>
### Q12: How do you integrate Tailwind CSS with Angular?

**Difficulty**: Intermediate

**Difficulty: Beginner**

**Answer:**
**Steps:**

1.  **Install:** `npm install -D tailwindcss postcss autoprefixer`
2.  **Init:** `npx tailwindcss init`
3.  **Configure `tailwind.config.js`:**
```javascript
module.exports = {
  content: [
    "./src/**/*.{html,ts}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```
4.  **Update `styles.css`:**
```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

---

<a id="q13"></a>
### Q13: How do you integrate Angular Material?

**Difficulty**: Intermediate

**Difficulty: Beginner**

**Answer:**
**Command:**
`ng add @angular/material`

**What it does:**
1.  Adds dependencies.
2.  Asks for a theme selection (Deep Purple/Amber, Indigo/Pink, etc.).
3.  Sets up global typography and browser animations.
4.  Imports `MatModule`s are no longer automatic in Standalone; you import what you need in components.

---

<a id="q14"></a>
### Q14: How do you integrate GraphQL with Apollo in Angular?

**Difficulty**: Intermediate

**Difficulty: Advanced**

**Answer:**
**Integration:**

1.  **Install:** `ng add apollo-angular`
2.  **Configuration:** Creates `graphql.provider.ts` (or config in `app.config.ts`).
```typescript
import { ApolloClientOptions, InMemoryCache } from '@apollo/client/core';
import { HttpLink } from 'apollo-angular/http';

const uri = 'https://api.example.com/graphql';

export function createApollo(httpLink: HttpLink): ApolloClientOptions<any> {
  return {
    link: httpLink.create({ uri }),
    cache: new InMemoryCache(),
  };
}
```
3.  **Usage:** Inject `Apollo` service to watch queries or mutate data.

---

<a id="q15"></a>
### Q15: How do you integrate Storybook with Angular?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Command:**
`npx storybook@latest init`

**Process:**
1.  Detects Angular project.
2.  Installs dependencies (`@storybook/angular`).
3.  Adds `storybook` and `build-storybook` scripts to `package.json`.
4.  Creates `.storybook` folder with config.
5.  Generates example stories.

---

<a id="q16"></a>
### Q16: How do you integrate Jest for testing in Angular?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Migration from Karma/Jasmine:**

1.  **Remove Karma:** `npm uninstall karma karma-chrome-launcher ...`
2.  **Install Jest:** `npm install -D jest @types/jest jest-preset-angular`
3.  **Configure `setup-jest.ts`:**
```typescript
import 'jest-preset-angular/setup-jest';
```
4.  **Update `package.json`:**
```json
"scripts": {
  "test": "jest"
},
"jest": {
  "preset": "jest-preset-angular",
  "setupFilesAfterEnv": ["<rootDir>/setup-jest.ts"]
}
```

---

<a id="q17"></a>
### Q17: How do you integrate Cypress for E2E testing?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Integration:**

1.  **Install:** `ng add @cypress/schematic`
2.  **Command:** `ng e2e`
3.  **Structure:** Creates `cypress/` folder with `e2e/` and `support/`.
4.  **Configuration:** `cypress.config.ts` handles base URL and other settings.

---

<a id="q18"></a>
### Q18: How do you integrate Google Maps?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Using `@angular/google-maps`:**

1.  **Install:** `npm install @angular/google-maps`
2.  **Load API:** Add script to `index.html` with API Key.
3.  **Usage:**
```typescript
import { GoogleMapsModule } from '@angular/google-maps';

@Component({
  standalone: true,
  imports: [GoogleMapsModule],
  template: `
    <google-map height="400px" width="750px" [center]="center" [zoom]="zoom">
      <map-marker [position]="center"></map-marker>
    </google-map>
  `
})
export class MapComponent {
  center: google.maps.LatLngLiteral = {lat: 24, lng: 12};
  zoom = 4;
}
```

---

<a id="q19"></a>
### Q19: How do you integrate Socket.io with Angular?

**Difficulty**: Intermediate

**Difficulty: Advanced**

**Answer:**
**Using `ngx-socket-io`:**

1.  **Install:** `npm install ngx-socket-io`
2.  **Config:**
```typescript
import { SocketIoModule, SocketIoConfig } from 'ngx-socket-io';
const config: SocketIoConfig = { url: 'http://localhost:3000', options: {} };
```
3.  **Service:**
```typescript
@Injectable({ providedIn: 'root' })
export class ChatService {
  constructor(private socket: Socket) {}

  sendMessage(msg: string) {
    this.socket.emit('message', msg);
  }

  getMessage() {
    return this.socket.fromEvent('message');
  }
}
```

---

<a id="q20"></a>
### Q20: How do you integrate Stripe Elements?

**Difficulty**: Intermediate

**Difficulty: Advanced**

**Answer:**
**Integration:**

1.  **Script:** Load Stripe.js in `index.html`.
2.  **Wrapper:** Use `ngx-stripe` or custom wrapper.
3.  **Component:**
```typescript
@ViewChild(StripeCardComponent) card: StripeCardComponent;

createToken() {
  this.stripeService
    .createToken(this.card.element, { name: 'John Doe' })
    .subscribe((result) => {
      if (result.token) {
        // Send token to backend
      }
    });
}
```

---

<a id="q21"></a>
### Q21: How do you integrate Chart.js?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Using `ng2-charts`:**

1.  **Install:** `npm install ng2-charts chart.js`
2.  **Imports:** `BaseChartDirective` (Standalone).
3.  **Template:**
```html
<canvas baseChart
        [data]="barChartData"
        [options]="barChartOptions"
        [type]="'bar'">
</canvas>
```

---

<a id="q22"></a>
### Q22: How do you integrate Auth0?

**Difficulty**: Intermediate

**Difficulty: Advanced**

**Answer:**
**Using Auth0 Angular SDK:**

1.  **Install:** `npm install @auth0/auth0-angular`
2.  **Config:**
```typescript
provideAuth0({
  domain: '{yourDomain}',
  clientId: '{yourClientId}',
  authorizationParams: {
    redirect_uri: window.location.origin
  }
})
```
3.  **Guard:** Use `authGuardFn` to protect routes.
4.  **Interceptor:** Use `authHttpInterceptorFn` to attach tokens.

---

<a id="q23"></a>
### Q23: How do you integrate Angular with Docker?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Dockerfile:**

```dockerfile
# Stage 1: Build
FROM node:18 as build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Stage 2: Serve
FROM nginx:alpine
COPY --from=build /app/dist/my-app /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
```

---

<a id="q24"></a>
### Q24: How do you integrate Internationalization (i18n)?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Native Angular i18n:**

1.  **Mark Text:** `<h1 i18n>Hello</h1>`
2.  **Extract:** `ng extract-i18n` -> generates `messages.xlf`.
3.  **Translate:** Create `messages.fr.xlf`.
4.  **Build:** `ng build --localize` to generate bundles for each locale.

---

<a id="q25"></a>
### Q25: How do you integrate `ngx-translate` for dynamic i18n?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Setup:**

1.  **Install:** `npm install @ngx-translate/core @ngx-translate/http-loader`
2.  **Loader:**
```typescript
export function HttpLoaderFactory(http: HttpClient) {
  return new TranslateHttpLoader(http);
}
```
3.  **Usage:**
```typescript
translate.setDefaultLang('en');
translate.use('fr');
```
```html
<h1 translate>HELLO</h1>
```

---

<a id="q26"></a>
### Q26: How do you integrate Sentry for error tracking?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Integration:**

1.  **Install:** `npm install @sentry/angular-ivy @sentry/browser`
2.  **Init:**
```typescript
Sentry.init({
  dsn: "https://examplePublicKey@o0.ingest.sentry.io/0",
  integrations: [
    new Sentry.BrowserTracing({
      routingInstrumentation: Sentry.routingInstrumentation,
    }),
  ],
});
```
3.  **ErrorHandler:** Provide `Sentry.createErrorHandler()`.

---

<a id="q27"></a>
### Q27: How do you integrate Prettier and ESLint?

**Difficulty**: Intermediate

**Difficulty: Beginner**

**Answer:**
**Setup:**

1.  **Install:** `npm install -D eslint prettier eslint-config-prettier`
2.  **ESLint Config:**
```json
{
  "extends": ["plugin:@angular-eslint/recommended", "prettier"]
}
```
3.  **Prettier Config:** `.prettierrc`
4.  **Scripts:** Add `"lint": "eslint ."` and `"format": "prettier --write ."`.

---

<a id="q28"></a>
### Q28: How do you integrate Husky for git hooks?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Integration:**

1.  **Install:** `npx husky-init && npm install`
2.  **Configure Hook:** Edit `.husky/pre-commit`:
```bash
npm run lint
npm test
```
3.  **Result:** Runs lint and tests before every commit.

---

<a id="q29"></a>
### Q29: How do you integrate a mock server (JSON Server)?

**Difficulty**: Intermediate

**Difficulty: Beginner**

**Answer:**
**Steps:**

1.  **Install:** `npm install -g json-server`
2.  **Data:** Create `db.json`.
3.  **Run:** `json-server --watch db.json`
4.  **Angular:** Point `HttpClient` to `http://localhost:3000/...`.

---

<a id="q30"></a>
### Q30: How do you integrate Keycloak for IAM?

**Difficulty**: Intermediate

**Difficulty: Advanced**

**Answer:**
**Using `keycloak-angular`:**

1.  **Install:** `npm install keycloak-angular keycloak-js`
2.  **Init Factory:**
```typescript
function initializeKeycloak(keycloak: KeycloakService) {
  return () =>
    keycloak.init({
      config: {
        url: 'http://localhost:8080/auth',
        realm: 'myrealm',
        clientId: 'myclient'
      },
      initOptions: {
        onLoad: 'check-sso',
        silentCheckSsoRedirectUri: window.location.origin + '/assets/silent-check-sso.html'
      }
    });
}
```

---

<a id="q31"></a>
### Q31: How do you integrate AG Grid?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Steps:**

1.  **Install:** `npm install ag-grid-angular ag-grid-community`
2.  **Import:** `AgGridModule`
3.  **Styles:** Import `ag-grid.css` and theme in `styles.css`.
4.  **Template:**
```html
<ag-grid-angular
    class="ag-theme-alpine"
    [rowData]="rowData"
    [columnDefs]="colDefs">
</ag-grid-angular>
```

---

<a id="q32"></a>
### Q32: How do you integrate RxJS Operators for HTTP retry strategies?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Integration:**

Use `retryWhen` or `retry` with `delay`:
```typescript
http.get('/api/data').pipe(
  retry({
    count: 3,
    delay: (error, retryCount) => timer(retryCount * 1000)
  })
);
```

---

<a id="q33"></a>
### Q33: How do you integrate Web Workers in Angular?

**Difficulty**: Intermediate

**Difficulty: Advanced**

**Answer:**
**CLI Command:**
`ng generate web-worker app`

**Result:**
1.  Creates `app.worker.ts`.
2.  Updates `angular.json` with web worker config.
3.  **Usage:**
```typescript
const worker = new Worker(new URL('./app.worker', import.meta.url));
worker.onmessage = ({ data }) => {
  console.log('From Worker:', data);
};
worker.postMessage('hello');
```

---

<a id="q34"></a>
### Q34: How do you integrate Service Workers (PWA)?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Command:**
`ng add @angular/pwa`

**What it does:**
1.  Adds `service-worker.js` build step.
2.  Creates `ngsw-config.json` for caching strategies.
3.  Adds `manifest.webmanifest`.
4.  Registers SW in `app.config.ts`/`AppModule`.

---

<a id="q35"></a>
### Q35: How do you integrate Module Federation (Micro-frontends)?

**Difficulty**: Intermediate

**Difficulty: Expert**

**Answer:**
**Using `@angular-architects/module-federation`:**

1.  **Install:** `ng add @angular-architects/module-federation`
2.  **Config:** `webpack.config.js` generated.
3.  **Expose:**
```javascript
exposes: {
  './Component': './src/app/my.component.ts',
},
```
4.  **Remotes:** Define remote apps in config.

---

<a id="q36"></a>
### Q36: How do you integrate Angular Universal (SSR)?

**Difficulty**: Intermediate

**Difficulty: Advanced**

**Answer:**
**Command (Angular <17):**
`ng add @nguniversal/express-engine`

**Command (Angular 17+):**
`ng add @angular/ssr`

**Result:**
1.  Creates `server.ts`.
2.  Updates `angular.json` with `server` target.
3.  Enables Hydration in `app.config.ts` (`provideClientHydration()`).

---

<a id="q37"></a>
### Q37: How do you integrate a Virtual Scroller (CDK)?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Using `@angular/cdk/scrolling`:**

1.  **Import:** `ScrollingModule`
2.  **Template:**
```html
<cdk-virtual-scroll-viewport itemSize="50" class="viewport">
  <div *cdkVirtualFor="let item of items" class="item">
    {{item}}
  </div>
</cdk-virtual-scroll-viewport>
```

---

<a id="q38"></a>
### Q38: How do you integrate Drag and Drop (CDK)?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Using `@angular/cdk/drag-drop`:**

1.  **Import:** `DragDropModule`
2.  **Template:**
```html
<div cdkDropList (cdkDropListDropped)="drop($event)">
  <div *ngFor="let item of items" cdkDrag>{{item}}</div>
</div>
```
3.  **Handler:**
```typescript
drop(event: CdkDragDrop<string[]>) {
  moveItemInArray(this.items, event.previousIndex, event.currentIndex);
}
```

---

<a id="q39"></a>
### Q39: How do you integrate Lottie Animations?

**Difficulty**: Intermediate

**Difficulty: Beginner**

**Answer:**
**Using `ngx-lottie`:**

1.  **Install:** `npm install ngx-lottie lottie-web`
2.  **Config:** Provide `playerFactory`.
3.  **Template:**
```html
<ng-lottie [options]="options"></ng-lottie>
```

---

<a id="q40"></a>
### Q40: How do you integrate Markdown rendering?

**Difficulty**: Intermediate

**Difficulty: Beginner**

**Answer:**
**Using `ngx-markdown`:**

1.  **Install:** `npm install ngx-markdown`
2.  **Import:** `MarkdownModule.forRoot()`
3.  **Usage:**
```html
<markdown [data]="markdownString"></markdown>
<!-- or -->
<markdown src="assets/readme.md"></markdown>
```

---

<a id="q41"></a>
### Q41: How do you integrate a Date Picker (Material)?

**Difficulty**: Intermediate

**Difficulty: Beginner**

**Answer:**
**Components:**
`MatDatepickerModule`, `MatNativeDateModule`

**Usage:**
```html
<mat-form-field>
  <mat-label>Choose a date</mat-label>
  <input matInput [matDatepicker]="picker">
  <mat-hint>MM/DD/YYYY</mat-hint>
  <mat-datepicker-toggle matIconSuffix [for]="picker"></mat-datepicker-toggle>
  <mat-datepicker #picker></mat-datepicker>
</mat-form-field>
```

---

<a id="q42"></a>
### Q42: How do you integrate Form Validation (Reactive)?

**Difficulty**: Intermediate

**Difficulty: Beginner**

**Answer:**
**Integration:**

1.  **Import:** `ReactiveFormsModule`
2.  **Control:**
```typescript
email = new FormControl('', [Validators.required, Validators.email]);
```
3.  **Template:**
```html
<input [formControl]="email">
<div *ngIf="email.invalid && email.touched">Invalid Email</div>
```

---

<a id="q43"></a>
### Q43: How do you integrate File Upload?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Basic Integration:**

1.  **Input:** `<input type="file" (change)="onFileSelected($event)">`
2.  **Handler:**
```typescript
onFileSelected(event: any) {
  const file: File = event.target.files[0];
  const formData = new FormData();
  formData.append('file', file);
  this.http.post('/upload', formData).subscribe();
}
```

---

<a id="q44"></a>
### Q44: How do you integrate JWT Handling?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Using `auth0/angular-jwt` (optional) or manual:**

**Manual:**
1.  **Store:** `localStorage.setItem('token', token)`
2.  **Interceptor:**
```typescript
intercept(req, next) {
  const token = localStorage.getItem('token');
  if (token) {
    const cloned = req.clone({
      headers: req.headers.set('Authorization', `Bearer ${token}`)
    });
    return next.handle(cloned);
  }
  return next.handle(req);
}
```

---

<a id="q45"></a>
### Q45: How do you integrate FontAwesome?

**Difficulty**: Intermediate

**Difficulty: Beginner**

**Answer:**
**Using `@fortawesome/angular-fontawesome`:**

1.  **Install:** `npm install @fortawesome/angular-fontawesome @fortawesome/free-solid-svg-icons`
2.  **Import:** `FontAwesomeModule`
3.  **Icon:**
```typescript
import { faCoffee } from '@fortawesome/free-solid-svg-icons';
icon = faCoffee;
```
4.  **Template:** `<fa-icon [icon]="icon"></fa-icon>`

---

<a id="q46"></a>
### Q46: How do you integrate Google Analytics 4 (GA4)?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Integration:**

1.  **Script:** Add GTAG script to `index.html`.
2.  **Router Events:**
```typescript
constructor(private router: Router) {
  this.router.events.subscribe(event => {
    if (event instanceof NavigationEnd) {
      gtag('config', 'G-XXXXX', { 'page_path': event.urlAfterRedirects });
    }
  });
}
```

---

<a id="q47"></a>
### Q47: How do you integrate Hotjar?

**Difficulty**: Intermediate

**Difficulty: Beginner**

**Answer:**
**Steps:**

1.  **Script:** Add Hotjar tracking code to `<head>` in `index.html`.
2.  **Alternative:** Use `ngx-hotjar` wrapper for more control (identify users, trigger events).

---

<a id="q48"></a>
### Q48: How do you integrate Bootstrap 5?

**Difficulty**: Intermediate

**Difficulty: Beginner**

**Answer:**
**Steps:**

1.  **Install:** `npm install bootstrap`
2.  **Styles:** Add `node_modules/bootstrap/dist/css/bootstrap.min.css` to `angular.json` styles array.
3.  **Scripts:** Add `node_modules/bootstrap/dist/js/bootstrap.bundle.min.js` to scripts array (if needing JS components).
4.  **Alternative:** Use `ng-bootstrap` or `ngx-bootstrap` for Angular native components.

---

<a id="q49"></a>
### Q49: How do you integrate PrimeNG?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Steps:**

1.  **Install:** `npm install primeng primeicons`
2.  **Styles:** Add theme, layout, and primeicons css to `angular.json`.
3.  **Animations:** Ensure `BrowserAnimationsModule` is imported.
4.  **Import:** Import specific modules (e.g., `ButtonModule`) in component/module.

---

<a id="q50"></a>
### Q50: How do you integrate Lodash?

**Difficulty**: Intermediate

**Difficulty: Beginner**

**Answer:**
**Integration:**

1.  **Install:** `npm install lodash @types/lodash`
2.  **Import:**
```typescript
import * as _ from 'lodash';
// or
import { cloneDeep } from 'lodash';
```
3.  **Optimization:** Use `lodash-es` for better tree-shaking.

---

<a id="q51"></a>
### Q51: How do you integrate Moment.js (or Day.js)?

**Difficulty**: Intermediate

**Difficulty: Beginner**

**Answer:**
**Day.js (Recommended over Moment):**

1.  **Install:** `npm install dayjs`
2.  **Usage:**
```typescript
import dayjs from 'dayjs';
const now = dayjs().format();
```
3.  **Pipe:** Create a `DatePipe` using Day.js for templates.

---

<a id="q52"></a>
### Q52: How do you integrate PDF generation (`jspdf`)?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Steps:**

1.  **Install:** `npm install jspdf`
2.  **Usage:**
```typescript
import { jsPDF } from 'jspdf';

downloadPDF() {
  const doc = new jsPDF();
  doc.text("Hello world!", 10, 10);
  doc.save("a4.pdf");
}
```

---

<a id="q53"></a>
### Q53: How do you integrate Excel export (`xlsx`)?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Steps:**

1.  **Install:** `npm install xlsx`
2.  **Usage:**
```typescript
import * as XLSX from 'xlsx';

exportExcel() {
  const ws: XLSX.WorkSheet = XLSX.utils.json_to_sheet(this.data);
  const wb: XLSX.WorkBook = XLSX.utils.book_new();
  XLSX.utils.book_append_sheet(wb, ws, 'Sheet1');
  XLSX.writeFile(wb, 'data.xlsx');
}
```

---

<a id="q54"></a>
### Q54: How do you integrate Clipboard copy?

**Difficulty**: Intermediate

**Difficulty: Beginner**

**Answer:**
**Using CDK Clipboard:**

1.  **Import:** `ClipboardModule` from `@angular/cdk/clipboard`.
2.  **Template:**
```html
<button [cdkCopyToClipboard]="value">Copy</button>
```

---

<a id="q55"></a>
### Q55: How do you integrate QR Code generation?

**Difficulty**: Intermediate

**Difficulty: Beginner**

**Answer:**
**Using `angularx-qrcode`:**

1.  **Install:** `npm install angularx-qrcode`
2.  **Template:**
```html
<qrcode [qrdata]="'https://example.com'" [width]="256" [errorCorrectionLevel]="'M'"></qrcode>
```

---

<a id="q56"></a>
### Q56: How do you integrate Toast Notifications (`ngx-toastr`)?

**Difficulty**: Intermediate

**Difficulty: Beginner**

**Answer:**
**Steps:**

1.  **Install:** `npm install ngx-toastr`
2.  **Config:** Provide `provideToastr()`.
3.  **Styles:** Import CSS.
4.  **Usage:**
```typescript
constructor(private toastr: ToastrService) {}
showSuccess() {
  this.toastr.success('Hello world!', 'Toastr fun!');
}
```

---

<a id="q57"></a>
### Q57: How do you integrate Loading Spinner (Overlay)?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Integration:**

1.  **Service:** Create `LoaderService` with `Subject<boolean>`.
2.  **Interceptor:** Set `isLoading = true` on request, `false` on finalize.
3.  **Component:** Subscribe to `isLoading` and show/hide Spinner (can use CDK Overlay for global blocking).

---

<a id="q58"></a>
### Q58: How do you integrate Environment Variables?

**Difficulty**: Intermediate

**Difficulty: Beginner**

**Answer:**
**Steps:**

1.  **Files:** `environment.ts`, `environment.prod.ts`.
2.  **Build:** `angular.json` "fileReplacements".
3.  **Usage:**
```typescript
import { environment } from './environments/environment';
if (environment.production) { ... }
```

---

<a id="q59"></a>
### Q59: How do you integrate Custom Web Elements?

**Difficulty**: Intermediate

**Difficulty: Advanced**

**Answer:**
**Steps:**

1.  **Schema:** Add `CUSTOM_ELEMENTS_SCHEMA` to module/component schemas.
2.  **Script:** Load web element JS.
3.  **Template:** `<my-custom-element [prop]="val"></my-custom-element>`.

---

<a id="q60"></a>
### Q60: How do you integrate Angular with Electron?

**Difficulty**: Intermediate

**Difficulty: Expert**

**Answer:**
**Steps:**

1.  **Setup:** Install `electron`.
2.  **Main Process:** Create `main.js`.
3.  **Build:** Build Angular to `dist/`.
4.  **Load:** Electron loads `dist/index.html`.
5.  **IPC:** Use `ipcRenderer` to communicate between Angular and Electron Main process.

---

<a id="q61"></a>
### Q61: How do you integrate Angular with Tauri?

**Difficulty**: Intermediate

**Difficulty: Expert**

**Answer:**
**Steps:**

1.  **Init:** `npm create tauri-app` (select Angular).
2.  **Build:** Configure `tauri.conf.json` to point to Angular dist.
3.  **Dev:** Run `tauri dev`.
4.  **API:** Use `@tauri-apps/api` to access OS features.

---

<a id="q62"></a>
### Q62: How do you integrate Angular with Ionic?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Steps:**

1.  **Command:** `ionic start myApp tabs --type=angular`
2.  **Components:** Use `IonHeader`, `IonContent`, etc.
3.  **Capacitor:** Use Capacitor plugins for native device access.

---

<a id="q63"></a>
### Q63: How do you integrate Push Notifications?

**Difficulty**: Intermediate

**Difficulty: Advanced**

**Answer:**
**Using SW:**

1.  **Enable PWA:** `ng add @angular/pwa`
2.  **Service:** `SwPush` from `@angular/service-worker`.
3.  **Request:** `swPush.requestSubscription({ serverPublicKey: '...' })`.
4.  **Listen:** `swPush.messages.subscribe(...)`.

---

<a id="q64"></a>
### Q64: How do you integrate Biometric Auth (WebAuthn)?

**Difficulty**: Intermediate

**Difficulty: Advanced**

**Answer:**
**Integration:**

1.  **Browser API:** `navigator.credentials.create()` (Registration) and `navigator.credentials.get()` (Login).
2.  **Backend:** Verify signatures.
3.  **Angular:** Wrap in a service, handle errors gracefully.

---

<a id="q65"></a>
### Q65: How do you integrate Voice Recognition (Web Speech API)?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Integration:**

1.  **Types:** `npm install @types/dom-speech-recognition`
2.  **Service:**
```typescript
const recognition = new (window as any).webkitSpeechRecognition();
recognition.onresult = (event) => {
  this.zone.run(() => {
    this.transcript = event.results[0][0].transcript;
  });
};
recognition.start();
```

---

<a id="q66"></a>
### Q66: How do you integrate Text-to-Speech?

**Difficulty**: Intermediate

**Difficulty: Beginner**

**Answer:**
**Integration:**

```typescript
speak(text: string) {
  const utterance = new SpeechSynthesisUtterance(text);
  window.speechSynthesis.speak(utterance);
}
```

---

<a id="q67"></a>
### Q67: How do you integrate Drag and Drop File Upload?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Steps:**

1.  **Directive:** Create `DndDirective`.
2.  **Events:** Listen to `dragover`, `dragleave`, `drop`.
3.  **Prevent Default:** `event.preventDefault()`, `event.stopPropagation()`.
4.  **Emit:** Emit `files` from `event.dataTransfer.files`.

---

<a id="q68"></a>
### Q68: How do you integrate Infinite Scroll?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Using `ngx-infinite-scroll`:**

1.  **Install:** `npm install ngx-infinite-scroll`
2.  **Template:**
```html
<div infiniteScroll (scrolled)="onScroll()">
  ...items
</div>
```
3.  **Logic:** Load more data when `onScroll` triggers.

---

<a id="q69"></a>
### Q69: How do you integrate Skeleton Loading?

**Difficulty**: Intermediate

**Difficulty: Beginner**

**Answer:**
**Using `ngx-skeleton-loader`:**

1.  **Install:** `npm install ngx-skeleton-loader`
2.  **Template:**
```html
<div *ngIf="loading; else content">
  <ngx-skeleton-loader count="5"></ngx-skeleton-loader>
</div>
<ng-template #content>...</ng-template>
```

---

<a id="q70"></a>
### Q70: How do you integrate Image Cropping?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Using `ngx-image-cropper`:**

1.  **Install:** `npm install ngx-image-cropper`
2.  **Template:**
```html
<image-cropper
    [imageChangedEvent]="imageChangedEvent"
    [maintainAspectRatio]="true"
    (imageCropped)="imageCropped($event)">
</image-cropper>
```

---

<a id="q71"></a>
### Q71: How do you integrate PDF Viewer?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Using `ng2-pdf-viewer`:**

1.  **Install:** `npm install ng2-pdf-viewer`
2.  **Template:**
```html
<pdf-viewer [src]="pdfSrc"
            [render-text]="true"
            style="display: block;"></pdf-viewer>
```

---

<a id="q72"></a>
### Q72: How do you integrate Video Player?

**Difficulty**: Intermediate

**Difficulty: Beginner**

**Answer:**
**Native:**
`<video controls src="...">`

**Custom (plyr, video.js):**
1.  Install library.
2.  Initialize player on `ngAfterViewInit`.
3.  Destroy on `ngOnDestroy`.

---

<a id="q73"></a>
### Q73: How do you integrate Rich Text Editor (WYSIWYG)?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Using `ngx-editor` or Quill:**

**Quill:**
1.  **Install:** `npm install ngx-quill quill`
2.  **Template:**
```html
<quill-editor [(ngModel)]="content"></quill-editor>
```

---

<a id="q74"></a>
### Q74: How do you integrate Code Highlighting?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Using `ngx-highlightjs`:**

1.  **Install:** `npm install ngx-highlightjs`
2.  **Config:** Provide languages.
3.  **Template:**
```html
<pre><code [highlight]="code"></code></pre>
```

---

<a id="q75"></a>
### Q75: How do you integrate Cookie Handling?

**Difficulty**: Intermediate

**Difficulty: Beginner**

**Answer:**
**Using `ngx-cookie-service`:**

1.  **Install:** `npm install ngx-cookie-service`
2.  **Usage:**
```typescript
constructor(private cookieService: CookieService) {}
set() { this.cookieService.set('Test', 'Hello World'); }
get() { return this.cookieService.get('Test'); }
```

---

<a id="q76"></a>
### Q76: How do you integrate LocalStorage/SessionStorage?

**Difficulty**: Intermediate

**Difficulty: Beginner**

**Answer:**
**Native API:**

```typescript
localStorage.setItem('key', 'value');
const val = localStorage.getItem('key');
```

**Abstraction:** Wrap in a service to handle SSR (check `isPlatformBrowser`).

---

<a id="q77"></a>
### Q77: How do you integrate Key Bindings (Hotkeys)?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**HostListener:**

```typescript
@HostListener('window:keydown.control.z', ['$event'])
handleUndo(event: KeyboardEvent) {
  event.preventDefault();
  this.undo();
}
```

---

<a id="q78"></a>
### Q78: How do you integrate Screen/Device Detection?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Using CDK Layout:**

1.  **Import:** `LayoutModule`
2.  **Usage:**
```typescript
breakpointObserver.observe([Breakpoints.Handset])
  .subscribe(result => {
    this.isHandset = result.matches;
  });
```

---

<a id="q79"></a>
### Q79: How do you integrate FullCalendar?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Steps:**

1.  **Install:** `@fullcalendar/angular @fullcalendar/daygrid`
2.  **Template:**
```html
<full-calendar [options]="calendarOptions"></full-calendar>
```
3.  **Config:** `calendarOptions` object with plugins and events.

---

<a id="q80"></a>
### Q80: How do you integrate Tooltips?

**Difficulty**: Intermediate

**Difficulty: Beginner**

**Answer:**
**Using Material Tooltip:**

```html
<button mat-button matTooltip="Info message">Action</button>
```

**Using Bootstrap:** Add `data-bs-toggle="tooltip"`. Initialized via JS.

---

<a id="q81"></a>
### Q81: How do you integrate Popovers?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Using CDK Overlay:**
Create flexible floating panels.

**Using Library:** `ngb-popover` (ng-bootstrap)
`<button [ngbPopover]="content">Click me</button>`

---

<a id="q82"></a>
### Q82: How do you integrate Modals/Dialogs?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Using Material Dialog:**

1.  **Open:**
```typescript
dialog.open(MyDialogComponent, {
  data: { name: 'Angular' }
});
```
2.  **Component:** Inject `MAT_DIALOG_DATA` to access data.

---

<a id="q83"></a>
### Q83: How do you integrate Side Navigation (Drawer)?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Using Material Sidenav:**

```html
<mat-sidenav-container>
  <mat-sidenav mode="side" opened>Sidenav</mat-sidenav>
  <mat-sidenav-content>Main content</mat-sidenav-content>
</mat-sidenav-container>
```

---

<a id="q84"></a>
### Q84: How do you integrate Tabs?

**Difficulty**: Intermediate

**Difficulty: Beginner**

**Answer:**
**Using Material Tabs:**

```html
<mat-tab-group>
  <mat-tab label="First"> Content 1 </mat-tab>
  <mat-tab label="Second"> Content 2 </mat-tab>
</mat-tab-group>
```

---

<a id="q85"></a>
### Q85: How do you integrate Stepper?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Using Material Stepper:**

```html
<mat-stepper>
  <mat-step [stepControl]="firstFormGroup">
    <form [formGroup]="firstFormGroup">...</form>
  </mat-step>
  <mat-step>Done</mat-step>
</mat-stepper>
```

---

<a id="q86"></a>
### Q86: How do you integrate Tree View?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Using Material Tree:**

1.  **DataSource:** Create `FlatTreeControl` and `DataSource`.
2.  **Template:** `<mat-tree [dataSource]="dataSource" ...>`
3.  **Nodes:** Define templates for leaf nodes and expandable nodes.

---

<a id="q87"></a>
### Q87: How do you integrate Autocomplete?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Using Material Autocomplete:**

1.  **Input:** `<input [matAutocomplete]="auto">`
2.  **Dropdown:** `<mat-autocomplete #auto="matAutocomplete">`
3.  **Filter:** Filter options based on input value change.

---

<a id="q88"></a>
### Q88: How do you integrate Slider?

**Difficulty**: Intermediate

**Difficulty: Beginner**

**Answer:**
**Using Material Slider:**

```html
<mat-slider min="1" max="100" step="1">
  <input matSliderThumb [(ngModel)]="value">
</mat-slider>
```

---

<a id="q89"></a>
### Q89: How do you integrate Toggle Switch?

**Difficulty**: Intermediate

**Difficulty: Beginner**

**Answer:**
**Using Material Slide Toggle:**

```html
<mat-slide-toggle [(ngModel)]="isChecked">Enable Feature</mat-slide-toggle>
```

---

<a id="q90"></a>
### Q90: How do you integrate Badge?

**Difficulty**: Intermediate

**Difficulty: Beginner**

**Answer:**
**Using Material Badge:**

```html
<span matBadge="4" matBadgeOverlap="false">Text with badge</span>
```

---

<a id="q91"></a>
### Q91: How do you integrate Progress Bar/Spinner?

**Difficulty**: Intermediate

**Difficulty: Beginner**

**Answer:**
**Material:**
`<mat-progress-bar mode="indeterminate"></mat-progress-bar>`
`<mat-progress-spinner mode="indeterminate"></mat-progress-spinner>`

---

<a id="q92"></a>
### Q92: How do you integrate Snackbar/Toast?

**Difficulty**: Intermediate

**Difficulty: Beginner**

**Answer:**
**Material:**
```typescript
snackBar.open('Message archived', 'Undo', {
  duration: 3000
});
```

---

<a id="q93"></a>
### Q93: How do you integrate Bottom Sheet?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Material:**
```typescript
bottomSheet.open(BottomSheetOverviewExampleSheet);
```

---

<a id="q94"></a>
### Q94: How do you integrate Expansion Panel (Accordion)?

**Difficulty**: Intermediate

**Difficulty: Beginner**

**Answer:**
**Material:**
```html
<mat-accordion>
  <mat-expansion-panel>
    <mat-expansion-panel-header>
      <mat-panel-title>Title</mat-panel-title>
    </mat-expansion-panel-header>
    <p>Content</p>
  </mat-expansion-panel>
</mat-accordion>
```

---

<a id="q95"></a>
### Q95: How do you integrate Divider?

**Difficulty**: Intermediate

**Difficulty: Beginner**

**Answer:**
**Material:**
`<mat-divider></mat-divider>`
Or CSS `border-bottom`.

---

<a id="q96"></a>
### Q96: How do you integrate Grid List?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Material:**
```html
<mat-grid-list cols="2" rowHeight="2:1">
  <mat-grid-tile>1</mat-grid-tile>
  <mat-grid-tile>2</mat-grid-tile>
</mat-grid-list>
```

---

<a id="q97"></a>
### Q97: How do you integrate Virtual Keyboard?

**Difficulty**: Intermediate

**Difficulty: Advanced**

**Answer:**
**Custom Implementation:**
1.  Create component with buttons.
2.  On click, append char to focused input.
3.  Handle Shift/Caps states.

---

<a id="q98"></a>
### Q98: How do you integrate Signature Pad?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Using `angular2-signaturepad`:**

1.  **Install:** `npm install angular2-signaturepad`
2.  **Template:** `<signature-pad [options]="options"></signature-pad>`
3.  **Data:** `signaturePad.toDataURL()`.

---

<a id="q99"></a>
### Q99: How do you integrate Barcode Scanner?

**Difficulty**: Intermediate

**Difficulty: Advanced**

**Answer:**
**Using `ngx-scanner` (Webcam):**
Scans QR/Barcodes from camera.

**Using Hardware Scanner:**
Listen to global `keypress` events (scanners usually emulate keyboard input).

---

<a id="q100"></a>
### Q100: How do you integrate Geolocation?

**Difficulty**: Intermediate

**Difficulty: Beginner**

**Answer:**
**Native API:**

```typescript
navigator.geolocation.getCurrentPosition((position) => {
  console.log(position.coords.latitude, position.coords.longitude);
});
```

---

<a id="q101"></a>
### Q101: How do you integrate Vibration?

**Difficulty**: Intermediate

**Difficulty: Beginner**

**Answer:**
**Native API:**
`navigator.vibrate(200);` // Vibrate for 200ms

---

<a id="q102"></a>
### Q102: How do you integrate Battery Status?

**Difficulty**: Intermediate

**Difficulty: Beginner**

**Answer:**
**Native API:**

```typescript
(navigator as any).getBattery().then((battery: any) => {
  console.log(battery.level);
});
```

---

<a id="q103"></a>
### Q103: How do you integrate Network Status Detection?

**Difficulty**: Intermediate

**Difficulty: Beginner**

**Answer:**
**Native:** `window.navigator.onLine`.

**Events:**
```typescript
window.addEventListener('offline', () => { ... });
window.addEventListener('online', () => { ... });
```

---

<a id="q104"></a>
### Q104: How do you integrate Page Visibility API?

**Difficulty**: Intermediate

**Difficulty: Beginner**

**Answer:**
**Usage:** Detect when user switches tab.
```typescript
document.addEventListener('visibilitychange', () => {
  if (document.hidden) {
    // Pause video/polling
  }
});
```

---

<a id="q105"></a>
### Q105: How do you integrate Fullscreen API?

**Difficulty**: Intermediate

**Difficulty: Beginner**

**Answer:**
**Usage:**
`elem.requestFullscreen();`
`document.exitFullscreen();`

---

<a id="q106"></a>
### Q106: How do you integrate Picture-in-Picture?

**Difficulty**: Intermediate

**Difficulty: Intermediate**

**Answer:**
**Usage:**
`videoElement.requestPictureInPicture();`

---

<a id="q107"></a>
### Q107: How do you integrate Share API (Web Share)?

**Difficulty**: Intermediate

**Difficulty: Beginner**

**Answer:**
**Usage:**
```typescript
if (navigator.share) {
  navigator.share({
    title: 'Web Fundamentals',
    text: 'Check out Web Fundamentals — it rocks!',
    url: 'https://developers.google.com/web',
  });
}
```

---

<a id="q108"></a>
### Q108: How do you integrate Payment Request API?

**Difficulty**: Intermediate

**Difficulty: Advanced**

**Answer:**
**Usage:**
Native browser UI for payments (Apple Pay/Google Pay).
```typescript
const request = new PaymentRequest(methods, details, options);
request.show().then(response => ...);
```

---

<a id="q109"></a>
### Q109: How do you integrate Bluetooth (Web Bluetooth)?

**Difficulty**: Intermediate

**Difficulty: Advanced**

**Answer:**
**Usage:**
Connect to BLE devices.
```typescript
navigator.bluetooth.requestDevice({ filters: [...] })
  .then(device => device.gatt.connect())
```

