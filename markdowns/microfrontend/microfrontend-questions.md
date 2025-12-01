<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>Microfrontend Interview Questions</h1>
  <p><b>Practical, code-focused questions for frontend architects</b></p>
</div>

---

## Table of Contents

1. [What are Microfrontends?](#q1-what-are-microfrontends) <span class="beginner">Beginner</span>
2. [What are the key benefits of Microfrontends?](#q2-what-are-the-key-benefits-of-microfrontends) <span class="beginner">Beginner</span>
3. [What are the drawbacks of Microfrontends?](#q3-what-are-the-drawbacks-of-microfrontends) <span class="beginner">Beginner</span>
4. [What is Build-time integration?](#q4-what-is-build-time-integration) <span class="intermediate">Intermediate</span>
5. [What is Run-time integration?](#q5-what-is-run-time-integration) <span class="intermediate">Intermediate</span>
6. [What is Webpack Module Federation?](#q6-what-is-webpack-module-federation) <span class="advanced">Advanced</span>
7. [How do Microfrontends communicate?](#q7-how-do-microfrontends-communicate) <span class="intermediate">Intermediate</span>
8. [What is Single-SPA?](#q8-what-is-single-spa) <span class="intermediate">Intermediate</span>
9. [How do you handle shared state?](#q9-how-do-you-handle-shared-state) <span class="advanced">Advanced</span>
10. [How do you handle CSS isolation?](#q10-how-do-you-handle-css-isolation) <span class="intermediate">Intermediate</span>
11. [What is Shadow DOM?](#q11-what-is-shadow-dom) <span class="intermediate">Intermediate</span>
12. [How do you handle routing in Microfrontends?](#q12-how-do-you-handle-routing-in-microfrontends) <span class="advanced">Advanced</span>
13. [What is the Shell (Container) App?](#q13-what-is-the-shell-container-app) <span class="beginner">Beginner</span>
14. [How do you handle version mismatches (e.g., React 16 vs 18)?](#q14-how-do-you-handle-version-mismatches-eg-react-16-vs-18) <span class="advanced">Advanced</span>
15. [What is Server-Side Composition (SSI)?](#q15-what-is-server-side-composition-ssi) <span class="intermediate">Intermediate</span>
16. [How do you test Microfrontends?](#q16-how-do-you-test-microfrontends) <span class="intermediate">Intermediate</span>
17. [What is Bit?](#q17-what-is-bit) <span class="advanced">Advanced</span>
18. [How do you handle authentication?](#q18-how-do-you-handle-authentication) <span class="intermediate">Intermediate</span>
19. [What is iframe integration?](#q19-what-is-iframe-integration) <span class="beginner">Beginner</span>
20. [What is Web Components approach?](#q20-what-is-web-components-approach) <span class="intermediate">Intermediate</span>
21. [How do you share dependencies (e.g., Lodash)?](#q21-how-do-you-share-dependencies-eg-lodash) <span class="intermediate">Intermediate</span>
22. [What are Import Maps?](#q22-what-are-import-maps) <span class="advanced">Advanced</span>
23. [How do you handle error boundaries?](#q23-how-do-you-handle-error-boundaries) <span class="intermediate">Intermediate</span>
24. [What is Lazy Loading in MFE?](#q24-what-is-lazy-loading-in-mfe) <span class="beginner">Beginner</span>
25. [How do you handle local development?](#q25-how-do-you-handle-local-development) <span class="intermediate">Intermediate</span>
26. [What is the Backend for Frontend (BFF) pattern in MFE?](#q26-what-is-the-backend-for-frontend-bff-pattern-in-mfe) <span class="advanced">Advanced</span>
27. [How do you handle navigation between MFEs?](#q27-how-do-you-handle-navigation-between-mfes) <span class="intermediate">Intermediate</span>
28. [What is Piral?](#q28-what-is-piral) <span class="advanced">Advanced</span>
29. [What is Luigis?](#q29-what-is-luigis) <span class="advanced">Advanced</span>
30. [How do you optimize performance?](#q30-how-do-you-optimize-performance) <span class="advanced">Advanced</span>
31. [What is Resiliency?](#q31-what-is-resiliency) <span class="beginner">Beginner</span>
32. [How do you handle global styles/resets?](#q32-how-do-you-handle-global-styles-resets) <span class="intermediate">Intermediate</span>
33. [What is Cross-Application Communication?](#q33-what-is-cross-application-communication) <span class="intermediate">Intermediate</span>
34. [How do you deploy Microfrontends?](#q34-how-do-you-deploy-microfrontends) <span class="intermediate">Intermediate</span>
35. [What is a Monorepo?](#q35-what-is-a-monorepo) <span class="beginner">Beginner</span>
36. [Monorepo vs Polyrepo for MFE?](#q36-monorepo-vs-polyrepo-for-mfe) <span class="intermediate">Intermediate</span>
37. [What is Dependency Hell?](#q37-what-is-dependency-hell) <span class="intermediate">Intermediate</span>
38. [How do you fix Dependency Hell?](#q38-how-do-you-fix-dependency-hell) <span class="advanced">Advanced</span>
39. [What is Zone.js in MFE?](#q39-what-is-zonejs-in-mfe) <span class="advanced">Advanced</span>
40. [Can you mix Frameworks (React + Angular)?](#q40-can-you-mix-frameworks-react--angular) <span class="beginner">Beginner</span>
41. [What is Hydration in SSR MFE?](#q41-what-is-hydration-in-ssr-mfe) <span class="advanced">Advanced</span>
42. [What is Tailor?](#q42-what-is-tailor) <span class="advanced">Advanced</span>
43. [How do you handle analytics?](#q43-how-do-you-handle-analytics) <span class="intermediate">Intermediate</span>
44. [What is a Manifest file?](#q44-what-is-a-manifest-file) <span class="intermediate">Intermediate</span>
45. [How do you handle shared UI components?](#q45-how-do-you-handle-shared-ui-components) <span class="intermediate">Intermediate</span>
46. [What is Code Splitting?](#q46-what-is-code-splitting) <span class="beginner">Beginner</span>
47. [How do you handle fonts and assets?](#q47-how-do-you-handle-fonts-and-assets) <span class="intermediate">Intermediate</span>
48. [What is Federated Modules Loader?](#q48-what-is-federated-modules-loader) <span class="advanced">Advanced</span>
49. [What is Atomic Design?](#q49-what-is-atomic-design) <span class="beginner">Beginner</span>
50. [How do you secure MFE routes?](#q50-how-do-you-secure-mfe-routes) <span class="intermediate">Intermediate</span>
51. [What is Feature Toggles?](#q51-what-is-feature-toggles) <span class="beginner">Beginner</span>
52. [What is 'Islands Architecture'?](#q52-what-is-islands-architecture) <span class="advanced">Advanced</span>
53. [Islands vs Microfrontends?](#q53-islands-vs-microfrontends) <span class="advanced">Advanced</span>
54. [How do you debug production issues?](#q54-how-do-you-debug-production-issues) <span class="intermediate">Intermediate</span>
55. [What is Layout Thrashing?](#q55-what-is-layout-thrashing) <span class="advanced">Advanced</span>
56. [How do you use Skeletons?](#q56-how-do-you-use-skeletons) <span class="beginner">Beginner</span>
57. [What is 'Vertical Split'?](#q57-what-is-vertical-split) <span class="intermediate">Intermediate</span>
58. [What is 'Horizontal Split'?](#q58-what-is-horizontal-split) <span class="intermediate">Intermediate</span>
59. [How do you handle internationalization (i18n)?](#q59-how-do-you-handle-internationalization-i18n) <span class="intermediate">Intermediate</span>
60. [What is Context API in React MFE?](#q60-what-is-context-api-in-react-mfe) <span class="intermediate">Intermediate</span>
61. [How do you handle cookies?](#q61-how-do-you-handle-cookies) <span class="beginner">Beginner</span>
62. [What is CORS in MFE?](#q62-what-is-cors-in-mfe) <span class="intermediate">Intermediate</span>
63. [What is Content Security Policy (CSP)?](#q63-what-is-content-security-policy-csp) <span class="advanced">Advanced</span>
64. [How do you upgrade a shared library?](#q64-how-do-you-upgrade-a-shared-library) <span class="advanced">Advanced</span>
65. [What is Web Workers?](#q65-what-is-web-workers) <span class="advanced">Advanced</span>
66. [How do you handle memory leaks?](#q66-how-do-you-handle-memory-leaks) <span class="intermediate">Intermediate</span>
67. [What is a 'Remote'?](#q67-what-is-a-remote) <span class="beginner">Beginner</span>
68. [What is a 'Host'?](#q68-what-is-a-host) <span class="beginner">Beginner</span>
69. [What is Bi-directional Module Federation?](#q69-what-is-bi-directional-module-federation) <span class="advanced">Advanced</span>
70. [How do you handle form state across MFEs?](#q70-how-do-you-handle-form-state-across-mfes) <span class="intermediate">Intermediate</span>
71. [What is 'fragment' in SSI?](#q71-what-is-fragment-in-ssi) <span class="beginner">Beginner</span>
72. [How do you handle SEO?](#q72-how-do-you-handle-seo) <span class="advanced">Advanced</span>
73. [What is qiankun?](#q73-what-is-qiankun) <span class="advanced">Advanced</span>
74. [How do you handle local storage?](#q74-how-do-you-handle-local-storage) <span class="beginner">Beginner</span>
75. [What is 'Runtime Chunk'?](#q75-what-is-runtime-chunk) <span class="advanced">Advanced</span>
76. [How do you handle slow networks?](#q76-how-do-you-handle-slow-networks) <span class="intermediate">Intermediate</span>
77. [What is Module Federation Dashboard?](#q77-what-is-module-federation-dashboard) <span class="advanced">Advanced</span>
78. [How do you handle breaking changes?](#q78-how-do-you-handle-breaking-changes) <span class="intermediate">Intermediate</span>
79. [What is 'Loose Coupling'?](#q79-what-is-loose-coupling) <span class="beginner">Beginner</span>
80. [What is 'High Cohesion'?](#q80-what-is-high-cohesion) <span class="beginner">Beginner</span>

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
Wrap frameworks in Custom Elements. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Module Federation 'shared' config or Import Maps. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Load MFE code only when route is visited. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Each MFE has its own BFF to aggregate data. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Shell navigation function or history API. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Framework for microfrontends based on 'Pilets'. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Microfrontend framework by SAP. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Share common libs, lazy load, HTTP/2. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
If one MFE fails, the rest should work. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Passing messages between distinct MFEs. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Upload assets to CDN. Update import map/manifest. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Single repo for all MFEs (e.g., Nx, Turborepo). This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Conflicting versions of shared libs. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Client takes over server-rendered HTML. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Layout service by Zalando for SSI. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
JSON mapping MFE names to URLs. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Breaking bundle into chunks. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Serve from CDN with absolute paths. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Dynamic loading of remotes. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Route guards in the Shell. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Enable/Disable features at runtime. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Static HTML with interactive 'islands' (Astro). This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Source maps, correlation IDs, logging. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
MFE loading causes page jump. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Show placeholder structure while loading. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Slice by business domain (e.g., Checkout Page). This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Slice by visual elements (e.g., Header, Footer). This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Shell loads language, MFEs load translations. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Can share context if React instance is shared. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Same domain cookies are shared. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Whitelist trusted scripts. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Coordination or backward compatibility. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Run script in background thread. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Cleanup on unmount (remove listeners). This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
The MFE being consumed. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
The app consuming the Remote. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
App acts as both Host and Remote. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Lift state to Shell or use URL. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Piece of HTML included. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
SSR is required for best SEO. CSR is harder. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Webpack boilerplate code. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Service Workers, Caching, Fallback UI. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Tool to visualize dependencies. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Communication and Versioning. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Minimize dependencies between MFEs. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Code that changes together stays together. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Domain logic
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---
