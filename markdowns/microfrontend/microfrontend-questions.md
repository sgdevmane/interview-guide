<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>Microfrontend Interview Questions</h1>
  <p><b>Practical, code-focused questions for frontend architects</b></p>
</div>

---

## Table of Contents

1. [What are Microfrontends?](#q1) <span class="beginner">Beginner</span>
2. [What are the key benefits of Microfrontends?](#q2) <span class="beginner">Beginner</span>
3. [What are the drawbacks of Microfrontends?](#q3) <span class="beginner">Beginner</span>
4. [What is Build-time integration?](#q4) <span class="intermediate">Intermediate</span>
5. [What is Run-time integration?](#q5) <span class="intermediate">Intermediate</span>
6. [What is Webpack Module Federation?](#q6) <span class="advanced">Advanced</span>
7. [How do Microfrontends communicate?](#q7) <span class="intermediate">Intermediate</span>
8. [What is Single-SPA?](#q8) <span class="intermediate">Intermediate</span>
9. [How do you handle shared state?](#q9) <span class="advanced">Advanced</span>
10. [How do you handle CSS isolation?](#q10) <span class="intermediate">Intermediate</span>
11. [What is Shadow DOM?](#q11) <span class="intermediate">Intermediate</span>
12. [How do you handle routing in Microfrontends?](#q12) <span class="advanced">Advanced</span>
13. [What is the Shell (Container) App?](#q13) <span class="beginner">Beginner</span>
14. [How do you handle version mismatches (e.g., React 16 vs 18)?](#q14) <span class="advanced">Advanced</span>
15. [What is Server-Side Composition (SSI)?](#q15) <span class="intermediate">Intermediate</span>
16. [How do you test Microfrontends?](#q16) <span class="intermediate">Intermediate</span>
17. [What is Bit?](#q17) <span class="advanced">Advanced</span>
18. [How do you handle authentication?](#q18) <span class="intermediate">Intermediate</span>
19. [What is iframe integration?](#q19) <span class="beginner">Beginner</span>
20. [What is Web Components approach?](#q20) <span class="intermediate">Intermediate</span>
21. [How do you share dependencies (e.g., Lodash)?](#q21) <span class="intermediate">Intermediate</span>
22. [What are Import Maps?](#q22) <span class="advanced">Advanced</span>
23. [How do you handle error boundaries?](#q23) <span class="intermediate">Intermediate</span>
24. [What is Lazy Loading in MFE?](#q24) <span class="beginner">Beginner</span>
25. [How do you handle local development?](#q25) <span class="intermediate">Intermediate</span>
26. [What is the Backend for Frontend (BFF) pattern in MFE?](#q26) <span class="advanced">Advanced</span>
27. [How do you handle navigation between MFEs?](#q27) <span class="intermediate">Intermediate</span>
28. [What is Piral?](#q28) <span class="advanced">Advanced</span>
29. [What is Luigis?](#q29) <span class="advanced">Advanced</span>
30. [How do you optimize performance?](#q30) <span class="advanced">Advanced</span>
31. [What is Resiliency?](#q31) <span class="beginner">Beginner</span>
32. [How do you handle global styles/resets?](#q32) <span class="intermediate">Intermediate</span>
33. [What is Cross-Application Communication?](#q33) <span class="intermediate">Intermediate</span>
34. [How do you deploy Microfrontends?](#q34) <span class="intermediate">Intermediate</span>
35. [What is a Monorepo?](#q35) <span class="beginner">Beginner</span>
36. [Monorepo vs Polyrepo for MFE?](#q36) <span class="intermediate">Intermediate</span>
37. [What is Dependency Hell?](#q37) <span class="intermediate">Intermediate</span>
38. [How do you fix Dependency Hell?](#q38) <span class="advanced">Advanced</span>
39. [What is Zone.js in MFE?](#q39) <span class="advanced">Advanced</span>
40. [Can you mix Frameworks (React + Angular)?](#q40) <span class="beginner">Beginner</span>
41. [What is Hydration in SSR MFE?](#q41) <span class="advanced">Advanced</span>
42. [What is Tailor?](#q42) <span class="advanced">Advanced</span>
43. [How do you handle analytics?](#q43) <span class="intermediate">Intermediate</span>
44. [What is a Manifest file?](#q44) <span class="intermediate">Intermediate</span>
45. [How do you handle shared UI components?](#q45) <span class="intermediate">Intermediate</span>
46. [What is Code Splitting?](#q46) <span class="beginner">Beginner</span>
47. [How do you handle fonts and assets?](#q47) <span class="intermediate">Intermediate</span>
48. [What is Federated Modules Loader?](#q48) <span class="advanced">Advanced</span>
49. [What is Atomic Design?](#q49) <span class="beginner">Beginner</span>
50. [How do you secure MFE routes?](#q50) <span class="intermediate">Intermediate</span>
51. [What is Feature Toggles?](#q51) <span class="beginner">Beginner</span>
52. [What is 'Islands Architecture'?](#q52) <span class="advanced">Advanced</span>
53. [Islands vs Microfrontends?](#q53) <span class="advanced">Advanced</span>
54. [How do you debug production issues?](#q54) <span class="intermediate">Intermediate</span>
55. [What is Layout Thrashing?](#q55) <span class="advanced">Advanced</span>
56. [How do you use Skeletons?](#q56) <span class="beginner">Beginner</span>
57. [What is 'Vertical Split'?](#q57) <span class="intermediate">Intermediate</span>
58. [What is 'Horizontal Split'?](#q58) <span class="intermediate">Intermediate</span>
59. [How do you handle internationalization (i18n)?](#q59) <span class="intermediate">Intermediate</span>
60. [What is Context API in React MFE?](#q60) <span class="intermediate">Intermediate</span>
61. [How do you handle cookies?](#q61) <span class="beginner">Beginner</span>
62. [What is CORS in MFE?](#q62) <span class="intermediate">Intermediate</span>
63. [What is Content Security Policy (CSP)?](#q63) <span class="advanced">Advanced</span>
64. [How do you upgrade a shared library?](#q64) <span class="advanced">Advanced</span>
65. [What is Web Workers?](#q65) <span class="advanced">Advanced</span>
66. [How do you handle memory leaks?](#q66) <span class="intermediate">Intermediate</span>
67. [What is a 'Remote'?](#q67) <span class="beginner">Beginner</span>
68. [What is a 'Host'?](#q68) <span class="beginner">Beginner</span>
69. [What is Bi-directional Module Federation?](#q69) <span class="advanced">Advanced</span>
70. [How do you handle form state across MFEs?](#q70) <span class="intermediate">Intermediate</span>
71. [What is 'fragment' in SSI?](#q71) <span class="beginner">Beginner</span>
72. [How do you handle SEO?](#q72) <span class="advanced">Advanced</span>
73. [What is qiankun?](#q73) <span class="advanced">Advanced</span>
74. [How do you handle local storage?](#q74) <span class="beginner">Beginner</span>
75. [What is 'Runtime Chunk'?](#q75) <span class="advanced">Advanced</span>
76. [How do you handle slow networks?](#q76) <span class="intermediate">Intermediate</span>
77. [What is Module Federation Dashboard?](#q77) <span class="advanced">Advanced</span>
78. [How do you handle breaking changes?](#q78) <span class="intermediate">Intermediate</span>
79. [What is 'Loose Coupling'?](#q79) <span class="beginner">Beginner</span>
80. [What is 'High Cohesion'?](#q80) <span class="beginner">Beginner</span>
81. [What is NX?](#q81) <span class="intermediate">Intermediate</span>
82. [What is Turborepo?](#q82) <span class="intermediate">Intermediate</span>
83. [How do you handle CSS naming collisions?](#q83) <span class="intermediate">Intermediate</span>
84. [What is a 'Pub/Sub' pattern in MFE?](#q84) <span class="intermediate">Intermediate</span>
85. [How do you handle global error handling?](#q85) <span class="advanced">Advanced</span>
86. [What is 'Tree Shaking'?](#q86) <span class="intermediate">Intermediate</span>
87. [What is 'Vendor Chunk'?](#q87) <span class="intermediate">Intermediate</span>
88. [How do you mock a remote MFE locally?](#q88) <span class="advanced">Advanced</span>
89. [What is 'Eager Consumption' in Module Federation?](#q89) <span class="advanced">Advanced</span>
90. [What is 'Singleton' loading?](#q90) <span class="advanced">Advanced</span>
91. [How do you handle end-to-end (E2E) testing?](#q91) <span class="intermediate">Intermediate</span>
92. [What is 'Contract Testing' for MFEs?](#q92) <span class="advanced">Advanced</span>
93. [How do you handle custom fonts?](#q93) <span class="beginner">Beginner</span>
94. [What is 'Prefetching'?](#q94) <span class="intermediate">Intermediate</span>
95. [How do you handle A/B Testing?](#q95) <span class="advanced">Advanced</span>
96. [What is 'Asset Discovery'?](#q96) <span class="advanced">Advanced</span>
97. [How do you handle Analytics tracking?](#q97) <span class="intermediate">Intermediate</span>
98. [What is 'Failover Strategy'?](#q98) <span class="advanced">Advanced</span>
99. [How do you handle authentication tokens?](#q99) <span class="intermediate">Intermediate</span>
100. [What is 'Route-based Splitting'?](#q100) <span class="beginner">Beginner</span>
101. [How do you handle 'Flash of Unstyled Content' (FOUC)?](#q101) <span class="intermediate">Intermediate</span>

---

<a id="q1"></a>
### Q1: What are Microfrontends?

**Difficulty**: Beginner

**Strategy**:
Microfrontends extend the concepts of microservices to the frontend world. The idea is to split a website or web app into a composition of features which are owned by independent teams. Each team has a distinct area of business or mission it cares about and specializes in.

**Code Example**:
```javascript
// App A + App B = Main App
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q2"></a>
### Q2: What are the key benefits of Microfrontends?

**Difficulty**: Beginner

**Strategy**:
Key benefits include: 
1. **Independent Deployment**: Teams can deploy their features without waiting for a monolithic release train.
2. **Autonomous Teams**: Teams can choose their own tech stack (within reason) and work in parallel.
3. **Incremental Upgrades**: You can rewrite a legacy app piece by piece instead of a 'big bang' rewrite.
4. **Fault Isolation**: A bug in one microfrontend doesn't necessarily crash the whole app.

**Code Example**:
```javascript
// Team A uses React, Team B uses Vue
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q3"></a>
### Q3: What are the drawbacks of Microfrontends?

**Difficulty**: Beginner

**Strategy**:
Drawbacks include:
1. **Payload Size**: Users may download duplicate dependencies (e.g., React loaded twice).
2. **Operational Complexity**: Managing multiple pipelines and deployments is harder than a monolith.
3. **Consistent Styling**: Ensuring a unified look and feel across teams requires a strong Design System.
4. **Communication**: Sharing state between isolated apps can be tricky.

**Code Example**:
```javascript
// Multiple React versions loaded
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q4"></a>
### Q4: What is Build-time integration?

**Difficulty**: Intermediate

**Strategy**:
In build-time integration, microfrontends are published as packages (e.g., npm) and installed by the container app. The container is then built and deployed. The downside is that a change in any microfrontend requires a rebuild and redeploy of the container.

**Code Example**:
```javascript
import Header from '@org/header';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q5"></a>
### Q5: What is Run-time integration?

**Difficulty**: Intermediate

**Strategy**:
Run-time integration allows the container application to fetch microfrontends independently over the network once it gets loaded in the browser. This means individual microfrontends can be deployed at any time without touching the container.

**Code Example**:
```javascript
const Header = await import('http://cdn/header.js');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q6"></a>
### Q6: What is Webpack Module Federation?

**Difficulty**: Advanced

**Strategy**:
Module Federation allows a JavaScript application to dynamically load code from another application and in the process, share dependencies. If an application consuming a federated module does not have a dependency needed by the federated code, Webpack will download the missing dependency from that federated build origin.

**Code Example**:
```javascript
new ModuleFederationPlugin({ name: 'app1', remotes: { app2: 'app2@http://...' } })
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q7"></a>
### Q7: How do Microfrontends communicate?

**Difficulty**: Intermediate

**Strategy**:
Microfrontends should be as decoupled as possible, but when communication is needed, standard web APIs are preferred. Options include:
1. **Custom Events**: Dispatching events on the window object.
2. **URL Params**: Passing state via the address bar.
3. **Props/Attributes**: If using a container/shell that passes data down.
4. **Global Store**: A shared Redux/Zustand store (use with caution to avoid coupling).

**Code Example**:
```javascript
window.dispatchEvent(new CustomEvent('user-login', { detail: user }));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q8"></a>
### Q8: What is Single-SPA?

**Difficulty**: Intermediate

**Strategy**:
Single-SPA is a javascript framework for front-end microservices. It enables you to use multiple frameworks in a single-page application, allowing you to split code by functionality and have Angular, React, Vue.js, etc. all running together.

**Code Example**:
```javascript
registerApplication('app1', () => import('app1'), location => location.pathname.startsWith('/app1'));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q9"></a>
### Q9: How do you handle shared state?

**Difficulty**: Advanced

**Strategy**:
Shared state should be minimized to avoid coupling. For global data like User Auth or Theme, use a small shared store (Redux/Zustand/Context) exposed by the Shell, or use Custom Events. Avoid sharing business logic state; each Microfrontend should be self-contained.

**Code Example**:
```javascript
window.globalState.subscribe(user => ...)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q10"></a>
### Q10: How do you handle CSS isolation?

**Difficulty**: Intermediate

**Strategy**:
CSS isolation prevents styles from one MFE bleeding into another. Techniques include:
- **CSS Modules**: Scopes class names (e.g., `.btn_x7z`).
- **Shadow DOM**: Provides true browser-level encapsulation.
- **CSS-in-JS**: Libraries like styled-components generate unique class names.
- **Prefixing**: Manually prefixing classes (e.g., `.teamA-btn`).

**Code Example**:
```javascript
// .header_abc123 { color: red; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q11"></a>
### Q11: What is Shadow DOM?

**Difficulty**: Intermediate

**Strategy**:
Browser API for DOM encapsulation. Styles don't leak in or out.

**Code Example**:
```javascript
element.attachShadow({ mode: 'open' });
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q12"></a>
### Q12: How do you handle routing in Microfrontends?

**Difficulty**: Advanced

**Strategy**:
The Shell application typically handles the top-level routing (e.g., `/checkout` loads the Checkout MFE). The Microfrontend then handles its own sub-routes (e.g., `/checkout/payment`). Both the Shell and MFEs must listen to the same history object to stay in sync.

**Code Example**:
```javascript
// Shell: /app1/* -> App1 handles /app1/dashboard
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q13"></a>
### Q13: What is the Shell (Container) App?

**Difficulty**: Beginner

**Strategy**:
The Shell (or Host) is the parent application that loads the Microfrontends. It is responsible for the common layout (Header, Footer, Navigation), Authentication, and orchestration of which MFE to display based on the URL.

**Code Example**:
```javascript
// Layout, Navigation, Auth
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q14"></a>
### Q14: How do you handle version mismatches (e.g., React 16 vs 18)?

**Difficulty**: Advanced

**Strategy**:
Each MFE bundles its own React (Run-time isolation) or upgrade all together (Coordination).

**Code Example**:
```javascript
// Increased bundle size
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q15"></a>
### Q15: What is Server-Side Composition (SSI)?

**Difficulty**: Intermediate

**Strategy**:
Assembling fragments on the server (e.g., Nginx SSI, Tailor, Podium).

**Code Example**:
```javascript
<!--#include virtual="/header" -->
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q16"></a>
### Q16: How do you test Microfrontends?

**Difficulty**: Intermediate

**Strategy**:
Testing strategies include:
- **Unit Tests**: Test components within the MFE in isolation.
- **Integration Tests**: Test the MFE running standalone.
- **E2E Tests**: Test the fully assembled application (Shell + MFEs) to ensure contracts (props/events) are honored.

**Code Example**:
```javascript
// Cypress/Playwright on shell
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q17"></a>
### Q17: What is Bit?

**Difficulty**: Advanced

**Strategy**:
Toolchain for component-driven development and microfrontends.

**Code Example**:
```javascript
bit export user-profile
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q18"></a>
### Q18: How do you handle authentication?

**Difficulty**: Intermediate

**Strategy**:
Shell handles login/tokens and passes them to MFEs.

**Code Example**:
```javascript
const token = window.shell.getToken();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q19"></a>
### Q19: What is iframe integration?

**Difficulty**: Beginner

**Strategy**:
Hard isolation. Oldest method. Difficult to build responsive/seamless UX.

**Code Example**:
```javascript
<iframe src="https://app2.com"></iframe>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q20"></a>
### Q20: What is Web Components approach?

**Difficulty**: Intermediate

**Strategy**:
Web Components (Custom Elements, Shadow DOM, HTML Templates) provide a framework-agnostic way to build microfrontends. Each MFE is registered as a custom HTML element that the shell can drop into the page like any native tag. This approach matters because it avoids vendor lock-in and gives you true encapsulation without extra libraries. The main trade-off is that you lose framework-specific features like React's state management inside the Shadow DOM boundary.

**Code Example**:
```javascript
<user-profile-mfe id="1"></user-profile-mfe>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q21"></a>
### Q21: How do you share dependencies (e.g., Lodash)?

**Difficulty**: Intermediate

**Strategy**:
Sharing dependencies reduces bundle size by ensuring common libraries like React or Lodash are loaded only once across all microfrontends. Module Federation's `shared` config and Import Maps are the two primary mechanisms for achieving this. The key pitfall is version conflicts -- if two MFEs require incompatible versions, you must decide whether to duplicate the library or coordinate an upgrade across teams.

**Code Example**:
```javascript
shared: { react: { singleton: true } }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q22"></a>
### Q22: What are Import Maps?

**Difficulty**: Advanced

**Strategy**:
Browser feature to control behavior of JS imports.

**Code Example**:
```javascript
<script type="importmap">{ "imports": { "react": "..." } }</script>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q23"></a>
### Q23: How do you handle error boundaries?

**Difficulty**: Intermediate

**Strategy**:
Wrap each MFE in an Error Boundary to prevent crashing the shell.

**Code Example**:
```javascript
<ErrorBoundary><MicroFrontend /></ErrorBoundary>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q24"></a>
### Q24: What is Lazy Loading in MFE?

**Difficulty**: Beginner

**Strategy**:
Lazy loading defers fetching a microfrontend's code until it is actually needed, typically when the user navigates to the relevant route. This is critical for initial page load performance because the browser does not waste bandwidth downloading features the user may never visit. The trade-off is a slight delay on first navigation, which can be mitigated with prefetching or skeleton placeholders while the chunk loads.

**Code Example**:
```javascript
const App = React.lazy(() => import('remote/App'));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q25"></a>
### Q25: How do you handle local development?

**Difficulty**: Intermediate

**Strategy**:
Run shell + MFE locally, or proxy production shell to local MFE.

**Code Example**:
```javascript
// npm start shell & npm start mfe1
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q26"></a>
### Q26: What is the Backend for Frontend (BFF) pattern in MFE?

**Difficulty**: Advanced

**Strategy**:
Each microfrontend owns a dedicated backend service (its BFF) that aggregates and tailors data specifically for that frontend. This pattern keeps teams fully autonomous because they control both the UI and the API surface it consumes. The downside is potential data duplication across BFFs, so a shared API gateway or caching layer is often introduced to reduce redundancy and maintain consistency.

**Code Example**:
```javascript
// Profile MFE -> Profile BFF -> Services
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q27"></a>
### Q27: How do you handle navigation between MFEs?

**Difficulty**: Intermediate

**Strategy**:
Navigation between microfrontends should go through the shell's router to ensure a consistent user experience and proper loading/unloading lifecycle. Using the History API or a shared router instance prevents full page reloads and preserves application state where possible. A common mistake is letting an MFE hard-link to another MFE's URL, which causes a full reload and breaks the single-page app experience.

**Code Example**:
```javascript
history.pushState(null, null, '/app2')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q28"></a>
### Q28: What is Piral?

**Difficulty**: Advanced

**Strategy**:
Piral is an open-source framework for building microfrontend applications using a plugin-based architecture called "pilets." The shell (called a Piral instance) defines extension slots that pilets can plug into dynamically at runtime. It is worth knowing because it handles many cross-cutting concerns out of the box -- dependency sharing, event bus, and shared state. A potential drawback is its opinionated API, which requires teams to learn Piral-specific patterns.

**Code Example**:
```javascript
// Extensible shell
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q29"></a>
### Q29: What is Luigis?

**Difficulty**: Advanced

**Strategy**:
Luigi is an open-source microfrontend framework developed by SAP that uses a configuration-driven approach. The shell defines navigation, authorization, and lifecycle hooks through a central JSON/JS config, while each microfrontend runs inside an iframe or a shadow DOM slot. Interviewers ask about Luigi because it highlights the config-over-code philosophy and strong enterprise features like role-based visibility. Be aware that heavy iframe usage can limit shared state and responsive design.

**Code Example**:
```javascript
// Config driven
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q30"></a>
### Q30: How do you optimize performance?

**Difficulty**: Advanced

**Strategy**:
Performance optimization in microfrontends requires deduplicating shared dependencies, lazy loading non-critical MFEs, and leveraging browser caching via content-hashed filenames. Code splitting at the route level and prefetching chunks the user is likely to visit next are also essential techniques. The most common pitfall is neglecting bundle analysis -- without it, teams accidentally ship the same library multiple times or include unused code that inflates the total payload.

**Code Example**:
```javascript
// Dedupe dependencies
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q31"></a>
### Q31: What is Resiliency?

**Difficulty**: Beginner

**Strategy**:
Resiliency means the shell and sibling microfrontends continue to function even when one MFE fails to load or crashes at runtime. This is achieved through error boundaries, fallback UIs, and timeout-based loading strategies. Without resiliency, a single broken MFE can take down the entire application, defeating the isolation benefit that microfrontends promise.

**Code Example**:
```javascript
// Header loads, but Sidebar fails gracefully
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q32"></a>
### Q32: How do you handle global styles/resets?

**Difficulty**: Intermediate

**Strategy**:
Shell defines base styles. MFEs should avoid global resets.

**Code Example**:
```javascript
// Use scoped CSS
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q33"></a>
### Q33: What is Cross-Application Communication?

**Difficulty**: Intermediate

**Strategy**:
Cross-application communication refers to how independent microfrontends exchange data without creating tight coupling. Preferred mechanisms include Custom Events, BroadcastChannel API, and a shared event bus provided by the shell. The key best practice is to keep messages small, typed, and one-directional -- bidirectional syncing of complex state almost always leads to race conditions and debugging nightmares.

**Code Example**:
```javascript
const bus = new BroadcastChannel('app_bus');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q34"></a>
### Q34: How do you deploy Microfrontends?

**Difficulty**: Intermediate

**Strategy**:
Each microfrontend should have its own CI/CD pipeline that builds, tests, and deploys independently to a CDN or static host. The shell application references each MFE via a URL, often resolved at runtime through a manifest or remote entry file. A common pitfall is forgetting to version or cache-bust remote entries, which can cause users to load stale MFE code after a new deployment.

**Code Example**:
```javascript
// Independent pipelines
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q35"></a>
### Q35: What is a Monorepo?

**Difficulty**: Beginner

**Strategy**:
A monorepo stores multiple related projects (shell and all microfrontends) in a single version-controlled repository. This simplifies code sharing, enforces consistent tooling, and makes cross-team refactoring straightforward. The trade-off is that the repository can grow large, so tools like Nx or Turborepo are typically used to manage build caching and avoid rebuilding unaffected projects.

**Code Example**:
```javascript
// Easy code sharing
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q36"></a>
### Q36: Monorepo vs Polyrepo for MFE?

**Difficulty**: Intermediate

**Strategy**:
Monorepo: Easier coordination. Polyrepo: Strict independence.

**Code Example**:
```javascript
// Nx is popular for Monorepo MFE
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q37"></a>
### Q37: What is Dependency Hell?

**Difficulty**: Intermediate

**Strategy**:
Dependency hell occurs when multiple microfrontends require incompatible versions of the same library, such as one team needing React 16 while another uses React 18. This matters because loading duplicate versions increases bundle size and can cause runtime errors if shared global state is expected. Left unchecked, dependency conflicts become the single biggest source of bugs in a microfrontend architecture.

**Code Example**:
```javascript
// React 16 vs 17 conflict
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q38"></a>
### Q38: How do you fix Dependency Hell?

**Difficulty**: Advanced

**Strategy**:
Semver matching in Module Federation or isolation.

**Code Example**:
```javascript
requiredVersion: '^16.8.0'
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q39"></a>
### Q39: What is Zone.js in MFE?

**Difficulty**: Advanced

**Strategy**:
Angular's change detection. Can conflict if multiple Angular apps run.

**Code Example**:
```javascript
// Load Zone.js only once
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q40"></a>
### Q40: Can you mix Frameworks (React + Angular)?

**Difficulty**: Beginner

**Strategy**:
Yes, that's a key feature. Use Web Components or Single-SPA.

**Code Example**:
```javascript
// React shell, Angular widget
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q41"></a>
### Q41: What is Hydration in SSR MFE?

**Difficulty**: Advanced

**Strategy**:
Hydration is the process of attaching JavaScript event listeners to server-rendered HTML so the page becomes interactive without a full re-render. In a microfrontend context, each MFE must hydrate its own fragment independently, which gets complex when different frameworks (React, Angular) manage hydration differently. A common pitfall is hydration mismatches where the client-rendered output differs from the server HTML, causing duplicate nodes or lost state.

**Code Example**:
```javascript
// Complex with multiple frameworks
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q42"></a>
### Q42: What is Tailor?

**Difficulty**: Advanced

**Strategy**:
Tailor is a layout and template composition server developed by Zuora that assembles HTML fragments from multiple services into a single response using streaming. It processes templates with special tags to fetch and stitch together microfrontend fragments on the server side. This approach is relevant because it enables server-side composition with progressive rendering -- the browser starts painting as soon as the first fragment arrives. The trade-off is that Tailor requires a Node.js middleware layer and a specific template syntax.

**Code Example**:
```javascript
// Streaming layout
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q43"></a>
### Q43: How do you handle analytics?

**Difficulty**: Intermediate

**Strategy**:
Shell tracks page views. MFEs track specific events.

**Code Example**:
```javascript
shell.track('button_click')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q44"></a>
### Q44: What is a Manifest file?

**Difficulty**: Intermediate

**Strategy**:
A manifest file is a JSON configuration that maps each microfrontend name to its deployed URL (or remote entry file). The shell reads this manifest at runtime to discover where to load each MFE from, enabling zero-downtime updates by simply changing the URL in the manifest. A best practice is to serve the manifest from a highly available endpoint and cache it with a short TTL so updates propagate quickly without hammering the server.

**Code Example**:
```javascript
{ "app1": "https://cdn.../main.js" }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q45"></a>
### Q45: How do you handle shared UI components?

**Difficulty**: Intermediate

**Strategy**:
Publish a UI library (npm) or expose via Module Federation.

**Code Example**:
```javascript
import { Button } from 'design-system'
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q46"></a>
### Q46: What is Code Splitting?

**Difficulty**: Beginner

**Strategy**:
Code splitting breaks a large JavaScript bundle into smaller chunks that are loaded on demand rather than upfront. This is fundamental to microfrontend performance because it ensures users only download the code they need for the current view. Route-based splitting and dynamic `import()` are the most common approaches; the main pitfall is over-splitting, which creates too many small HTTP requests and can actually hurt performance on slow networks.

**Code Example**:
```javascript
import()
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q47"></a>
### Q47: How do you handle fonts and assets?

**Difficulty**: Intermediate

**Strategy**:
Static assets like fonts, images, and icons should be centralized on a CDN and referenced by absolute URLs so every microfrontend loads the same version without duplication. The shell app is typically responsible for loading fonts to avoid flash-of-unstyled-text and redundant requests. A common mistake is bundling fonts inside each MFE, which bloats bundles and causes the browser to download the same font file multiple times.

**Code Example**:
```javascript
url('https://cdn.../font.woff')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q48"></a>
### Q48: What is Federated Modules Loader?

**Difficulty**: Advanced

**Strategy**:
The Federated Modules Loader is Webpack's internal runtime that resolves, loads, and shares modules across separately built applications at runtime. It handles the negotiation of shared dependencies, ensuring only one copy of a singleton library is loaded. Understanding this loader is important for debugging "shared module not available" errors, which typically occur when the loading order or version negotiation fails between the host and a remote.

**Code Example**:
```javascript
// webpack/container/reference
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q49"></a>
### Q49: What is Atomic Design?

**Difficulty**: Beginner

**Strategy**:
Atomic Design is a methodology for creating design systems. It breaks interfaces down into Atoms (buttons, inputs), Molecules (search form), Organisms (header), Templates, and Pages. This structure is highly effective for sharing UI components across Microfrontends.

**Code Example**:
```javascript
// Atoms, Molecules, Organisms
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q50"></a>
### Q50: How do you secure MFE routes?

**Difficulty**: Intermediate

**Strategy**:
Route security in microfrontends requires coordination between the shell and each MFE -- the shell enforces top-level auth checks, while individual MFEs can add granular permission checks for their own features. A best practice is to never load an MFE's JavaScript bundle until authentication and authorization are confirmed, because shipping protected code to an unauthenticated client is a security risk. Always validate permissions on the server side as well, since client-side checks can be bypassed.

**Code Example**:
```javascript
if (!auth) redirect('/login')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q51"></a>
### Q51: What is Feature Toggles?

**Difficulty**: Beginner

**Strategy**:
Feature toggles (or flags) let you enable or disable a microfrontend or specific functionality at runtime without deploying new code. This is especially valuable in MFE architectures because it allows gradual rollouts, A/B testing, and instant kill switches for broken features. The pitfall to watch for is accumulating stale toggles -- every flag adds branching complexity, so teams should archive toggles once a feature is fully rolled out.

**Code Example**:
```javascript
if (flags.newCheckout) ...
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q52"></a>
### Q52: What is 'Islands Architecture'?

**Difficulty**: Advanced

**Strategy**:
Islands Architecture, popularized by frameworks like Astro, renders most of the page as static HTML and only hydrates interactive "islands" of JavaScript. This matters because it dramatically reduces the JavaScript sent to the browser compared to a fully client-rendered MFE. The trade-off is that interactive regions must be clearly delineated ahead of time, and complex state sharing between islands requires extra plumbing compared to a traditional SPA approach.

**Code Example**:
```javascript
// Less JS, faster load
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q53"></a>
### Q53: Islands vs Microfrontends?

**Difficulty**: Advanced

**Strategy**:
Islands: Optimization technique. MFEs: Organization technique.

**Code Example**:
```javascript
// Can use both
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q54"></a>
### Q54: How do you debug production issues?

**Difficulty**: Intermediate

**Strategy**:
Debugging microfrontends in production requires distributed tracing, structured logging, and source maps so you can trace an error back to the specific team and deployment that caused it. The shell should attach correlation IDs to every request, and each MFE should tag its log entries with its name and version. A common pitfall is not preserving source maps securely (e.g., on a private server), which makes production stack traces useless.

**Code Example**:
```javascript
// Identify which MFE failed
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q55"></a>
### Q55: What is Layout Thrashing?

**Difficulty**: Advanced

**Strategy**:
Layout thrashing occurs when JavaScript repeatedly reads and writes to the DOM in an alternating pattern, forcing the browser to recalculate styles and layout dozens of times per frame. In an MFE context this is especially dangerous because multiple microfrontends mutating the same DOM tree can compound the problem. Prevent it by batching DOM reads before writes, using `requestAnimationFrame`, and relying on placeholder skeletons rather than measuring real elements during load.

**Code Example**:
```javascript
// Use Skeletons/Placeholders
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q56"></a>
### Q56: How do you use Skeletons?

**Difficulty**: Beginner

**Strategy**:
Skeleton screens are placeholder UI elements that mimic the shape of real content and display while a microfrontend is loading. They improve perceived performance by giving users immediate visual feedback instead of a blank area or spinner. The best practice is to define skeleton components in the shell so they render instantly, then swap them out with the actual MFE content once the remote chunk finishes loading.

**Code Example**:
```javascript
<Skeleton height={50} />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q57"></a>
### Q57: What is 'Vertical Split'?

**Difficulty**: Intermediate

**Strategy**:
A vertical split divides the application by business domain or feature -- each microfrontend owns its entire vertical slice from UI to database (e.g., a "Product Catalog" MFE with its own components, state, and API). This is the preferred approach because it maximizes team autonomy and minimizes cross-team coordination. The pitfall is accidentally splitting along technical layers instead of business capabilities, which creates coupling and defeats the purpose of microfrontends.

**Code Example**:
```javascript
// Preferred approach
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q58"></a>
### Q58: What is 'Horizontal Split'?

**Difficulty**: Intermediate

**Strategy**:
A horizontal split divides the application by technical layer -- for example, one team owns the header, another owns the footer, and a third owns the sidebar. This approach tends to create coupling because these horizontal sections often share layout logic, data, and styling rules. It is generally discouraged in favor of vertical splits, but it can work for truly isolated layout regions like a global navigation bar that has no data dependency on the rest of the page.

**Code Example**:
```javascript
// Can cause coupling
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q59"></a>
### Q59: How do you handle internationalization (i18n)?

**Difficulty**: Intermediate

**Strategy**:
Internationalization in microfrontends requires a coordinated strategy where the shell determines the user's locale and passes it down, while each MFE manages its own translation files. Using a shared i18n library with namespaced translation keys prevents collisions between MFE dictionaries. A common pitfall is hard-coding locale in individual MFEs instead of receiving it from the shell, which breaks consistency when the user switches languages.

**Code Example**:
```javascript
t('welcome')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q60"></a>
### Q60: What is Context API in React MFE?

**Difficulty**: Intermediate

**Strategy**:
React's Context API provides a way to pass data through the component tree without prop drilling, commonly used for themes, authentication, or locale data. In an MFE architecture, context does not cross microfrontend boundaries because each MFE has its own React instance and component tree. The best practice is for the shell to expose global data through a shared JavaScript object or custom events rather than relying on React Context across MFE borders.

**Code Example**:
```javascript
<AuthProvider>...</AuthProvider>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q61"></a>
### Q61: How do you handle cookies?

**Difficulty**: Beginner

**Strategy**:
Cookies are shared across all microfrontends running on the same domain, making them a simple way to pass data like auth tokens or user preferences. However, this shared nature also means MFEs can accidentally overwrite each other's cookies, so namespacing cookie keys is essential. For cross-domain MFE setups, cookies will not be shared automatically and you will need to use token-based authentication passed through headers or postMessage instead.

**Code Example**:
```javascript
document.cookie
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q62"></a>
### Q62: What is CORS in MFE?

**Difficulty**: Intermediate

**Strategy**:
Cross-Origin Resource Sharing. CDN assets must allow origin.

**Code Example**:
```javascript
Access-Control-Allow-Origin: *
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q63"></a>
### Q63: What is Content Security Policy (CSP)?

**Difficulty**: Advanced

**Strategy**:
Content Security Policy is an HTTP header that restricts which sources the browser is allowed to load scripts, styles, and other resources from. In a microfrontend setup, the CSP must explicitly whitelist every CDN and domain that hosts an MFE or its assets. A common pitfall is setting an overly permissive policy like `*` for convenience, which defeats the security benefit -- instead, list each specific origin and use nonces or hashes for inline scripts.

**Code Example**:
```javascript
script-src 'self' https://cdn...
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q64"></a>
### Q64: How do you upgrade a shared library?

**Difficulty**: Advanced

**Strategy**:
Upgrading a shared library in a microfrontend ecosystem requires a coordinated rollout strategy to avoid breaking consumers. Semantic versioning and Module Federation's `requiredVersion` field let you declare compatibility ranges, while a canary deployment lets you test the upgrade with one MFE before rolling it out to all. The biggest risk is a major version bump that changes the public API, so always communicate changes through a changelog and consider using contract tests to verify compatibility.

**Code Example**:
```javascript
// Major version bump
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q65"></a>
### Q65: What is Web Workers?

**Difficulty**: Advanced

**Strategy**:
Web Workers run JavaScript in a background thread, keeping the main thread free for UI rendering -- valuable when an MFE needs to do heavy computation like data parsing or image processing. Each microfrontend can spawn its own worker without interfering with others, providing natural isolation. The trade-off is that workers cannot access the DOM directly, so all communication must go through `postMessage`, which adds serialization overhead.

**Code Example**:
```javascript
new Worker('worker.js')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q66"></a>
### Q66: How do you handle memory leaks?

**Difficulty**: Intermediate

**Strategy**:
Memory leaks are especially dangerous in microfrontends because when an MFE is unmounted, it must release all DOM references, event listeners, timers, and subscriptions. The shell must enforce strict lifecycle hooks (`mount`/`unmount`) that every MFE implements, and React's `useEffect` cleanup function is the primary tool for tearing down resources. A common pitfall is forgetting to remove global event listeners or intervals when an MFE is navigated away from, which keeps orphaned objects in memory indefinitely.

**Code Example**:
```javascript
useEffect(() => cleanup, [])
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q67"></a>
### Q67: What is a 'Remote'?

**Difficulty**: Beginner

**Strategy**:
In Module Federation terminology, a Remote is an application that exposes modules (components, functions, or utilities) for other applications to consume at runtime. Each Remote publishes a `remoteEntry.js` file that acts as a catalog of its available modules. The key concept to remember is that a Remote does not need to know who consumes it -- it simply declares what it exposes, keeping the relationship loosely coupled.

**Code Example**:
```javascript
exposes: { './App': './src/App' }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q68"></a>
### Q68: What is a 'Host'?

**Difficulty**: Beginner

**Strategy**:
A Host (also called a consumer or shell) is the application that loads and renders modules from one or more Remotes at runtime. It declares which Remotes it depends on in the Module Federation config and handles the overall page layout, routing, and shared dependency coordination. A best practice is to keep the Host as thin as possible -- it should orchestrate, not implement business logic -- so it rarely needs changes.

**Code Example**:
```javascript
remotes: { app1: ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q69"></a>
### Q69: What is Bi-directional Module Federation?

**Difficulty**: Advanced

**Strategy**:
Bi-directional Module Federation means an application can act as both a Host and a Remote simultaneously -- it consumes modules from others while also exposing its own. This enables peer-to-peer module sharing between microfrontends rather than a strict hub-and-spoke model. The danger is circular dependencies where App A depends on App B which depends on App A, which can cause infinite loading loops if not carefully managed.

**Code Example**:
```javascript
// Circular dependency risk
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q70"></a>
### Q70: How do you handle form state across MFEs?

**Difficulty**: Intermediate

**Strategy**:
When a multi-step form spans multiple microfrontends (e.g., Step 1 in MFE-A, Step 2 in MFE-B), the state must be persisted through a neutral medium such as URL parameters, a shared store, or session storage. Each MFE validates its own step independently and passes validated data forward, never backward. A common mistake is storing partial form state in a global store that every MFE can mutate, which creates hidden coupling and makes bugs difficult to trace.

**Code Example**:
```javascript
// Step 1 -> URL -> Step 2
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q71"></a>
### Q71: What is 'fragment' in SSI?

**Difficulty**: Beginner

**Strategy**:
A fragment in Server-Side Includes (SSI) is a self-contained piece of HTML generated by an individual microfrontend's backend service. The composition server (like Nginx or Tailor) assembles these fragments into a single page by including each one at a designated placeholder. This approach is interview-relevant because it achieves microfrontend composition with zero client-side JavaScript overhead. The main limitation is that all fragments must return HTML synchronously unless streaming is supported.

**Code Example**:
```javascript
<fragment src="..." />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q72"></a>
### Q72: How do you handle SEO?

**Difficulty**: Advanced

**Strategy**:
SEO in microfrontends is challenging because search engine crawlers may not execute JavaScript, meaning a purely client-rendered MFE produces an empty page in the crawl. Server-side rendering (SSR) or static pre-rendering is the standard solution -- each MFE renders its content on the server so the crawler sees fully formed HTML. A best practice is to use server-side composition (SSI or edge-side includes) so the entire page is delivered as a single HTML response rather than requiring multiple round trips.

**Code Example**:
```javascript
// Prerendering
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q73"></a>
### Q73: What is qiankun?

**Difficulty**: Advanced

**Strategy**:
MFE implementation based on single-spa (popular in China).

**Code Example**:
```javascript
// HTML Entry
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q74"></a>
### Q74: How do you handle local storage?

**Difficulty**: Beginner

**Strategy**:
Shared if same domain. Namespacing keys recommended.

**Code Example**:
```javascript
localStorage.setItem('app1:key', ...)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q75"></a>
### Q75: What is 'Runtime Chunk'?

**Difficulty**: Advanced

**Strategy**:
A runtime chunk contains Webpack's module resolution and loading logic -- the boilerplate code that knows how to import other chunks and resolve dependencies. Extracting it into a single shared file (`runtimeChunk: 'single'`) is critical in MFE builds because it ensures all microfrontends use the same module resolution mechanism. Without this extraction, each MFE bundles its own runtime, which can cause conflicts when modules are shared across federated applications.

**Code Example**:
```javascript
optimization: { runtimeChunk: 'single' }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q76"></a>
### Q76: How do you handle slow networks?

**Difficulty**: Intermediate

**Strategy**:
Slow networks amplify the latency of loading multiple remote microfrontend bundles, so strategies like aggressive caching, service workers, and skeleton UIs become essential. You should also implement timeout-based loading so a slow MFE does not block the entire page -- show a fallback after a reasonable wait. A common pitfall is not testing under throttled network conditions during development, which hides performance problems that real users on mobile connections will experience.

**Code Example**:
```javascript
// Offline mode
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q77"></a>
### Q77: What is Module Federation Dashboard?

**Difficulty**: Advanced

**Strategy**:
The Module Federation Dashboard (also called Medusa) is a visualization and management tool that shows which microfrontends are deployed, what modules they expose, and which shared dependencies they consume. It provides real-time visibility into the federated architecture, making it easier to detect version conflicts, unused exports, and dependency mismatches. This is particularly valuable in large organizations where dozens of teams independently publish remotes and need a central registry to track the ecosystem.

**Code Example**:
```javascript
// Medusa
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q78"></a>
### Q78: How do you handle breaking changes?

**Difficulty**: Intermediate

**Strategy**:
Breaking changes in a microfrontend ecosystem can cascade across all consumers, so they must be managed through versioning, deprecation notices, and gradual migration. Semantic versioning of shared APIs and contract testing between producer and consumer MFEs help catch incompatibilities before they reach production. The key best practice is to maintain backward compatibility for at least one release cycle and communicate upcoming changes through a shared changelog or RFC process.

**Code Example**:
```javascript
// Changelogs
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q79"></a>
### Q79: What is 'Loose Coupling'?

**Difficulty**: Beginner

**Strategy**:
Loose coupling means each microfrontend knows as little as possible about the others, communicating only through well-defined interfaces like events or shared contracts. This is the core goal of microfrontend architecture because it enables independent deployment, testing, and technology choices per team. The pitfall is letting convenience erode coupling over time -- a quick shared-state shortcut today becomes the hardest bug to fix tomorrow.

**Code Example**:
```javascript
// Goal of MFE
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q80"></a>
### Q80: What is 'High Cohesion'?

**Difficulty**: Beginner

**Strategy**:
High cohesion means all the code related to a single business feature (UI components, state, API calls, tests) lives together inside the same microfrontend. This matters because cohesive MFEs are easier to understand, maintain, and deploy as a unit. A common mistake is splitting related functionality across MFEs -- for example, separating the product listing UI from its API layer -- which forces teams to coordinate every change.

**Code Example**:
```javascript
// Domain logic
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---
<a id="q81"></a>

### Q81: What is NX?

**Difficulty**: Intermediate

**Strategy**:
A smart build system with first-class monorepo support and powerful integrations for Angular, React, and more.

**Code Example**:
```javascript
nx serve my-app
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q82"></a>

### Q82: What is Turborepo?

**Difficulty**: Intermediate

**Strategy**:
A high-performance build system for JavaScript/TypeScript monorepos. Caches build results.

**Code Example**:
```javascript
turbo run build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q83"></a>

### Q83: How do you handle CSS naming collisions?

**Difficulty**: Intermediate

**Strategy**:
CSS Modules (scoping classes), BEM naming convention, or Shadow DOM (true isolation).

**Code Example**:
```javascript
.button_hash123 { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q84"></a>

### Q84: What is a 'Pub/Sub' pattern in MFE?

**Difficulty**: Intermediate

**Strategy**:
Publish-Subscribe. Decoupled communication where senders (publishers) send messages to a topic, and receivers (subscribers) listen.

**Code Example**:
```javascript
window.dispatchEvent(new CustomEvent('order:placed'))
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q85"></a>

### Q85: How do you handle global error handling?

**Difficulty**: Advanced

**Strategy**:
Global 'window.onerror' handler in the Shell app, plus React Error Boundaries in each MFE.

**Code Example**:
```javascript
window.onerror = function() { logError() }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q86"></a>

### Q86: What is 'Tree Shaking'?

**Difficulty**: Intermediate

**Strategy**:
Removing unused code from bundles during the build process. Critical for MFE performance.

**Code Example**:
```javascript
import { func } from 'lib'; // Only func is bundled
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q87"></a>

### Q87: What is 'Vendor Chunk'?

**Difficulty**: Intermediate

**Strategy**:
A separate bundle containing third-party libraries (React, Lodash) to improve caching.

**Code Example**:
```javascript
vendors.js (cached long-term)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q88"></a>

### Q88: How do you mock a remote MFE locally?

**Difficulty**: Advanced

**Strategy**:
Point the remote URL to a local dev server or a static mock file in Webpack config.

**Code Example**:
```javascript
remotes: { app1: 'http://localhost:3001/remoteEntry.js' }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q89"></a>

### Q89: What is 'Eager Consumption' in Module Federation?

**Difficulty**: Advanced

**Strategy**:
Loading shared modules immediately on startup instead of async. Solves 'Shared module is not available' error.

**Code Example**:
```javascript
shared: { react: { eager: true } }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q90"></a>

### Q90: What is 'Singleton' loading?

**Difficulty**: Advanced

**Strategy**:
Ensuring a library (like React) is loaded only once, even if multiple MFEs use different versions.

**Code Example**:
```javascript
shared: { react: { singleton: true } }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q91"></a>

### Q91: How do you handle end-to-end (E2E) testing?

**Difficulty**: Intermediate

**Strategy**:
Test the Shell app with all MFEs integrated using Cypress or Playwright.

**Code Example**:
```javascript
cy.visit('/'); cy.get('#cart-mfe').click();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q92"></a>

### Q92: What is 'Contract Testing' for MFEs?

**Difficulty**: Advanced

**Strategy**:
Verifying that the API/Events exposed by an MFE match what the consumer expects. Prevents breaking changes.

**Code Example**:
```javascript
Provider: 'I emit {id: number}'. Consumer: 'I expect {id: number}'.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q93"></a>

### Q93: How do you handle custom fonts?

**Difficulty**: Beginner

**Strategy**:
Load fonts in the Shell app to ensure consistency and avoid duplicate downloads.

**Code Example**:
```javascript
<link rel='stylesheet' href='fonts.css'>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q94"></a>

### Q94: What is 'Prefetching'?

**Difficulty**: Intermediate

**Strategy**:
Loading resources (chunks) for other MFEs in the background before the user navigates to them.

**Code Example**:
```javascript
<link rel='prefetch' href='chunk.js'>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q95"></a>

### Q95: How do you handle A/B Testing?

**Difficulty**: Advanced

**Strategy**:
The Shell app or a feature flag service decides which version of an MFE to load for a user.

**Code Example**:
```javascript
if (user.group === 'B') load('mfe-v2') else load('mfe-v1')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q96"></a>

### Q96: What is 'Asset Discovery'?

**Difficulty**: Advanced

**Strategy**:
Dynamically finding where static assets (images) are located for a remote MFE (using publicPath).

**Code Example**:
```javascript
__webpack_public_path__ = scriptUrl;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q97"></a>

### Q97: How do you handle Analytics tracking?

**Difficulty**: Intermediate

**Strategy**:
Centralized analytics service in Shell. MFEs send events to Shell.

**Code Example**:
```javascript
shell.track('product_viewed')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q98"></a>

### Q98: What is 'Failover Strategy'?

**Difficulty**: Advanced

**Strategy**:
What to display if a remote MFE fails to load. Fallback UI or a cached version.

**Code Example**:
```javascript
try { load() } catch { return <ErrorUI /> }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q99"></a>

### Q99: How do you handle authentication tokens?

**Difficulty**: Intermediate

**Strategy**:
Shell handles login and stores token (cookie/localStorage). MFEs read token or attach via interceptor.

**Code Example**:
```javascript
const token = localStorage.getItem('token');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q100"></a>

### Q100: What is 'Route-based Splitting'?

**Difficulty**: Beginner

**Strategy**:
Loading a different MFE based on the URL path.

**Code Example**:
```javascript
/checkout -> CheckoutMFE
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q101"></a>

### Q101: How do you handle 'Flash of Unstyled Content' (FOUC)?

**Difficulty**: Intermediate

**Strategy**:
Ensure critical CSS is loaded before JS execution or use SSR.

**Code Example**:
```javascript
Critical CSS in <head>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

