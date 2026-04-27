<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>Svelte Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for developers</b></p>
</div>

---

## Table of Contents

1. [What is the lifecycle of a Svelte component?](#q1-what-is-the-lifecycle-of-a-svelte-component) <span class="beginner">Beginner</span>
2. [How do you create a reactive declaration?](#q2-how-do-you-create-a-reactive-declaration) <span class="beginner">Beginner</span>
3. [How do you share state between components?](#q3-how-do-you-share-state-between-components) <span class="intermediate">Intermediate</span>
4. [How do you dispatch custom events?](#q4-how-do-you-dispatch-custom-events) <span class="intermediate">Intermediate</span>
5. [How do you use slots?](#q5-how-do-you-use-slots) <span class="beginner">Beginner</span>
6. [How do you optimize rendering with `keyed` each blocks?](#q6-how-do-you-optimize-rendering-with-keyed-each-blocks) <span class="intermediate">Intermediate</span>
7. [How do you bind form inputs?](#q7-how-do-you-bind-form-inputs) <span class="beginner">Beginner</span>
8. [How do you use Svelte actions?](#q8-how-do-you-use-svelte-actions) <span class="advanced">Advanced</span>
9. [How do you handle transitions?](#q9-how-do-you-handle-transitions) <span class="intermediate">Intermediate</span>
10. [What is `tick()`?](#q10-what-is-tick) <span class="advanced">Advanced</span>
11. [Difference between Svelte and React?](#q11-difference-between-svelte-and-react) <span class="beginner">Beginner</span>
12. [How do you use the special element `<svelte:head>`?](#q12-how-do-you-use-the-special-element-sveltehead) <span class="intermediate">Intermediate</span>
13. [What are Derived Stores?](#q13-what-are-derived-stores) <span class="intermediate">Intermediate</span>
14. [How do you handle context in Svelte?](#q14-how-do-you-handle-context-in-svelte) <span class="intermediate">Intermediate</span>
15. [What is the purpose of `<svelte:component>`?](#q15-what-is-the-purpose-of-sveltecomponent) <span class="advanced">Advanced</span>
16. [How do you loop with an index in Svelte?](#q16-how-do-you-loop-with-an-index-in-svelte) <span class="beginner">Beginner</span>
17. [What is the `bind:this` directive?](#q17-what-is-the-bindthis-directive) <span class="intermediate">Intermediate</span>
18. [How do you prevent event bubbling in Svelte?](#q18-how-do-you-prevent-event-bubbling-in-svelte) <span class="beginner">Beginner</span>
19. [What is SvelteKit?](#q19-what-is-sveltekit) <span class="intermediate">Intermediate</span>
20. [How do you use the `await` block?](#q20-how-do-you-use-the-await-block) <span class="intermediate">Intermediate</span>
21. [What are Custom Stores?](#q21-what-are-custom-stores) <span class="advanced">Advanced</span>
22. [How do you style components in Svelte?](#q22-how-do-you-style-components-in-svelte) <span class="beginner">Beginner</span>
23. [How do you use the @html tag?](#q23-how-do-you-use-the-html-tag) <span class="beginner">Beginner</span>
24. [What is the difference between on:click and on:click|once?](#q24-what-is-the-difference-between-onclick-and-onclickonce) <span class="beginner">Beginner</span>
25. [How do you forward events in Svelte?](#q25-how-do-you-forward-events-in-svelte) <span class="intermediate">Intermediate</span>
26. [What is the `class:` directive?](#q26-what-is-the-class-directive) <span class="beginner">Beginner</span>
27. [How do you use `<svelte:window>`?](#q27-how-do-you-use-sveltewindow) <span class="intermediate">Intermediate</span>
28. [What is `<svelte:body>`?](#q28-what-is-sveltebody) <span class="intermediate">Intermediate</span>
29. [How do you use `<svelte:head>`?](#q29-how-do-you-use-sveltehead) <span class="intermediate">Intermediate</span>
30. [What are Module Context scripts?](#q30-what-are-module-context-scripts) <span class="advanced">Advanced</span>
31. [How do you handle fallback content in slots?](#q31-how-do-you-handle-fallback-content-in-slots) <span class="beginner">Beginner</span>
32. [What is `$$props`?](#q32-what-is-props) <span class="advanced">Advanced</span>
33. [What is `$$restProps`?](#q33-what-is-restprops) <span class="intermediate">Intermediate</span>
34. [How do you debug Svelte reactivity?](#q34-how-do-you-debug-svelte-reactivity) <span class="beginner">Beginner</span>
35. [What is the `key` block?](#q35-what-is-the-key-block) <span class="intermediate">Intermediate</span>
36. [How do you define props in Svelte?](#q36-how-do-you-define-props-in-svelte) <span class="beginner">Beginner</span>
37. [What is `createEventDispatcher`?](#q37-what-is-createeventdispatcher) <span class="intermediate">Intermediate</span>
38. [How do you use the `use:action` directive?](#q38-how-do-you-use-the-useaction-directive) <span class="advanced">Advanced</span>
39. [What is the return value of an action?](#q39-what-is-the-return-value-of-an-action) <span class="advanced">Advanced</span>
40. [How do you bind `this` in Svelte?](#q40-how-do-you-bind-this-in-svelte) <span class="intermediate">Intermediate</span>
41. [How do you bind component props?](#q41-how-do-you-bind-component-props) <span class="intermediate">Intermediate</span>
42. [What is the `store` contract?](#q42-what-is-the-store-contract) <span class="advanced">Advanced</span>
43. [How do you auto-subscribe to a store?](#q43-how-do-you-auto-subscribe-to-a-store) <span class="beginner">Beginner</span>
44. [What is `get` from `svelte/store`?](#q44-what-is-get-from-sveltestore) <span class="intermediate">Intermediate</span>
45. [How do you make a store read-only?](#q45-how-do-you-make-a-store-read-only) <span class="intermediate">Intermediate</span>
46. [What is `derived` store?](#q46-what-is-derived-store) <span class="intermediate">Intermediate</span>
47. [How do you use `style:` directive?](#q47-how-do-you-use-style-directive) <span class="beginner">Beginner</span>
48. [What is `svelte:options`?](#q48-what-is-svelteoptions) <span class="advanced">Advanced</span>
49. [How do you detect if code is running in browser?](#q49-how-do-you-detect-if-code-is-running-in-browser) <span class="beginner">Beginner</span>
50. [What is Hydration?](#q50-what-is-hydration) <span class="advanced">Advanced</span>
51. [How do you create a transition?](#q51-how-do-you-create-a-transition) <span class="advanced">Advanced</span>
52. [What is `crossfade`?](#q52-what-is-crossfade) <span class="advanced">Advanced</span>
53. [How do you use `animate:flip`?](#q53-how-do-you-use-animateflip) <span class="intermediate">Intermediate</span>
54. [What is `svelte:fragment`?](#q54-what-is-sveltefragment) <span class="intermediate">Intermediate</span>
55. [How do you lazy load a component?](#q55-how-do-you-lazy-load-a-component) <span class="advanced">Advanced</span>
56. [What is the difference between `bind:group` and `bind:value`?](#q56-what-is-the-difference-between-bindgroup-and-bindvalue) <span class="intermediate">Intermediate</span>
57. [How do you handle multiple classes?](#q57-how-do-you-handle-multiple-classes) <span class="beginner">Beginner</span>
58. [What is `svelte-ignore`?](#q58-what-is-svelte-ignore) <span class="intermediate">Intermediate</span>
59. [How do you access the component instance?](#q59-how-do-you-access-the-component-instance) <span class="advanced">Advanced</span>
60. [What is `beforeUpdate`?](#q60-what-is-beforeupdate) <span class="intermediate">Intermediate</span>
61. [What is `afterUpdate`?](#q61-what-is-afterupdate) <span class="intermediate">Intermediate</span>
62. [How do you create a custom store?](#q62-how-do-you-create-a-custom-store) <span class="intermediate">Intermediate</span>
63. [What is `spring` motion?](#q63-what-is-spring-motion) <span class="intermediate">Intermediate</span>
64. [What is `tweened` motion?](#q64-what-is-tweened-motion) <span class="intermediate">Intermediate</span>
65. [How do you use `svelte:self`?](#q65-how-do-you-use-svelteself) <span class="intermediate">Intermediate</span>
66. [What is the `src/routes` folder in SvelteKit?](#q66-what-is-the-srcroutes-folder-in-sveltekit) <span class="beginner">Beginner</span>
67. [What is a `+page.svelte` file?](#q67-what-is-a-pagesvelte-file) <span class="beginner">Beginner</span>
68. [What is a `+page.server.js` file?](#q68-what-is-a-pageserverjs-file) <span class="intermediate">Intermediate</span>
69. [What is a `+layout.svelte` file?](#q69-what-is-a-layoutsvelte-file) <span class="beginner">Beginner</span>
70. [How do you handle form actions in SvelteKit?](#q70-how-do-you-handle-form-actions-in-sveltekit) <span class="intermediate">Intermediate</span>
71. [What is `enhance` in SvelteKit forms?](#q71-what-is-enhance-in-sveltekit-forms) <span class="intermediate">Intermediate</span>
72. [How do you use environment variables?](#q72-how-do-you-use-environment-variables) <span class="intermediate">Intermediate</span>
73. [What is adapter in SvelteKit?](#q73-what-is-adapter-in-sveltekit) <span class="intermediate">Intermediate</span>
74. [How do you handle errors in SvelteKit?](#q74-how-do-you-handle-errors-in-sveltekit) <span class="intermediate">Intermediate</span>
75. [What is `hooks.server.js`?](#q75-what-is-hooksserverjs) <span class="advanced">Advanced</span>
76. [How do you prefetch data?](#q76-how-do-you-prefetch-data) <span class="intermediate">Intermediate</span>
77. [What is the difference between `onMount` and `load`?](#q77-what-is-the-difference-between-onmount-and-load) <span class="intermediate">Intermediate</span>
78. [How do you use global styles?](#q78-how-do-you-use-global-styles) <span class="beginner">Beginner</span>
79. [What is accessibility warning in Svelte?](#q79-what-is-accessibility-warning-in-svelte) <span class="beginner">Beginner</span>
80. [How do you optimize loops?](#q80-how-do-you-optimize-loops) <span class="intermediate">Intermediate</span>
81. [What is the purpose of `tick` in tests?](#q81-what-is-the-purpose-of-tick-in-tests) <span class="advanced">Advanced</span>
82. [How do you test Svelte components?](#q82-how-do-you-test-svelte-components) <span class="intermediate">Intermediate</span>
83. [What is `vite` in Svelte context?](#q83-what-is-vite-in-svelte-context) <span class="beginner">Beginner</span>
84. [How do you deploy a Svelte app?](#q84-how-do-you-deploy-a-svelte-app) <span class="beginner">Beginner</span>
85. [What is `svelte-check`?](#q85-what-is-svelte-check) <span class="intermediate">Intermediate</span>
86. [How do you use TypeScript with Svelte?](#q86-how-do-you-use-typescript-with-svelte) <span class="beginner">Beginner</span>
87. [What is `$$slots`?](#q87-what-is-slots) <span class="advanced">Advanced</span>
88. [How do you debounce an input?](#q88-how-do-you-debounce-an-input) <span class="intermediate">Intermediate</span>
89. [What is `await` block `catch`?](#q89-what-is-await-block-catch) <span class="beginner">Beginner</span>
90. [How do you use `placeholder` attribute on inputs?](#q90-how-do-you-use-placeholder-attribute-on-inputs) <span class="beginner">Beginner</span>
91. [Can you have multiple script tags?](#q91-can-you-have-multiple-script-tags) <span class="advanced">Advanced</span>
92. [What is `immutable` option?](#q92-what-is-immutable-option) <span class="advanced">Advanced</span>
93. [How do you access `window` safely in SSR?](#q93-how-do-you-access-window-safely-in-ssr) <span class="intermediate">Intermediate</span>
94. [What is `svelte/motion`?](#q94-what-is-sveltemotion) <span class="intermediate">Intermediate</span>
95. [What is `svelte/easing`?](#q95-what-is-svelteeasing) <span class="beginner">Beginner</span>
96. [How do you pass data to layout?](#q96-how-do-you-pass-data-to-layout) <span class="intermediate">Intermediate</span>
97. [What is `page` store in SvelteKit?](#q97-what-is-page-store-in-sveltekit) <span class="intermediate">Intermediate</span>
98. [How do you use `navigating` store?](#q98-how-do-you-use-navigating-store) <span class="intermediate">Intermediate</span>
99. [What is `updated` store?](#q99-what-is-updated-store) <span class="advanced">Advanced</span>
100. [How do you handle 404s?](#q100-how-do-you-handle-404s) <span class="beginner">Beginner</span>
101. [What is `data-sveltekit-reload`?](#q101-what-is-data-sveltekit-reload) <span class="intermediate">Intermediate</span>
102. [How do you reset a store?](#q102-how-do-you-reset-a-store) <span class="intermediate">Intermediate</span>

---

<a id="q1"></a>
### Q1: What is the lifecycle of a Svelte component?

**Difficulty**: Beginner

**Strategy**:
Svelte has `onMount`, `onDestroy`, `beforeUpdate`, and `afterUpdate`.

**Code Example**:
```javascript
onMount(() => { console.log('Mounted'); });
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q2"></a>
### Q2: How do you create a reactive declaration?

**Difficulty**: Beginner

**Strategy**:
Understanding reactive declarations is fundamental to Svelte because they define computed values that automatically update when their dependencies change. The `$:` syntax tells the compiler to track referenced variables and re-run the statement whenever they change, replacing the need for manual dependency arrays found in other frameworks. A common pitfall is trying to use reactive declarations for side effects without understanding that they execute synchronously during the component update cycle.

**Code Example**:
```javascript
$: doubled = count * 2;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q3"></a>
### Q3: How do you share state between components?

**Difficulty**: Intermediate

**Strategy**:
Use Svelte `stores` (writable, readable, derived).

**Code Example**:
```javascript
export const count = writable(0);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q4"></a>
### Q4: How do you dispatch custom events?

**Difficulty**: Intermediate

**Strategy**:
Custom events are the primary mechanism for child-to-parent communication in Svelte, making this essential for building composable component hierarchies. The `createEventDispatcher` must be called at the top level of the component script during initialization, not inside functions or conditionals. A common mistake is forgetting that dispatched events do not bubble through intermediate components, so each layer must explicitly forward them.

**Code Example**:
```javascript
const dispatch = createEventDispatcher(); dispatch('msg', 'hello');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q5"></a>
### Q5: How do you use slots?

**Difficulty**: Beginner

**Strategy**:
Slots are Svelte's composition mechanism, allowing parent components to inject content into child components, which is critical for building reusable UI wrappers and layouts. Default slot content is rendered only when no content is provided by the parent. A common pitfall is expecting slot content to have access to the child component's variables, but slots are scoped to the parent where they are defined.

**Code Example**:
```javascript
<div><slot>Default</slot></div>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q6"></a>
### Q6: How do you optimize rendering with `keyed` each blocks?

**Difficulty**: Intermediate

**Strategy**:
Keyed each blocks are important for performance when rendering dynamic lists because they let Svelte reconcile DOM elements by identity rather than by index. Without a key, Svelte reuses DOM nodes in place, which can cause unintended state retention (like input values persisting when list items are reordered). Always use a stable, unique identifier as the key rather than the array index to avoid subtle bugs.

**Code Example**:
```javascript
{#each items as item (item.id)}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q7"></a>
### Q7: How do you bind form inputs?

**Difficulty**: Beginner

**Strategy**:
Two-way binding on form inputs is one of Svelte's most convenient features, drastically reducing boilerplate compared to manual event handlers. The `bind:value` directive keeps the variable and input in sync automatically, and Svelte supports binding to different properties like `bind:checked` for checkboxes and `bind:files` for file inputs. A common pitfall is using `bind:value` with a constant or non-reactive variable, which silently fails to update.

**Code Example**:
```javascript
<input bind:value={name}>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q8"></a>
### Q8: How do you use Svelte actions?

**Difficulty**: Advanced

**Strategy**:
Actions are functions called when an element is created.

**Code Example**:
```javascript
function tooltip(node, params) { ... } <div use:tooltip>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q9"></a>
### Q9: How do you handle transitions?

**Difficulty**: Intermediate

**Strategy**:
Transitions are a key differentiator for Svelte because they are built into the framework with first-class support, making animated UIs far easier to implement than in most alternatives. Svelte provides `transition:`, `in:`, and `out:` directives that integrate with element lifecycle, and transitions only play when elements are actually added or removed from the DOM. A common mistake is applying transitions inside `{#each}` blocks without adding a unique key, which causes animations to target wrong elements.

**Code Example**:
```javascript
<div transition:fade>...</div>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q10"></a>
### Q10: What is `tick()`?

**Difficulty**: Advanced

**Strategy**:
Returns a promise that resolves after pending state changes are applied to DOM.

**Code Example**:
```javascript
await tick();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q11"></a>
### Q11: Difference between Svelte and React?

**Difficulty**: Beginner

**Strategy**:
Svelte is a compiler that converts components to imperative code at build time. React uses a virtual DOM at runtime.

**Code Example**:
```javascript
// Svelte: No virtual DOM overhead
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q12"></a>
### Q12: How do you use the special element `<svelte:head>`?

**Difficulty**: Intermediate

**Strategy**:
The `<svelte:head>` element is essential for SEO and meta-tag management because it allows components to inject content into the document's `<head>` from anywhere in the component tree. During SSR, Svelte renders this content server-side so search engines and social media crawlers can read it. A best practice is to use it in layout or page-level components rather than deeply nested ones, to keep head management predictable and avoid conflicts.

**Code Example**:
```javascript
<svelte:head><title>My Page</title></svelte:head>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q13"></a>
### Q13: What are Derived Stores?

**Difficulty**: Intermediate

**Strategy**:
Stores whose values are based on one or more other stores.

**Code Example**:
```javascript
const doubled = derived(count, $count => $count * 2);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q14"></a>
### Q14: How do you handle context in Svelte?

**Difficulty**: Intermediate

**Strategy**:
Use `setContext` and `getContext`. Must be called during component initialization.

**Code Example**:
```javascript
setContext('key', value); const value = getContext('key');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q15"></a>
### Q15: What is the purpose of `<svelte:component>`?

**Difficulty**: Advanced

**Strategy**:
To render a component dynamically based on a variable.

**Code Example**:
```javascript
<svelte:component this={selectedComponent} />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q16"></a>
### Q16: How do you loop with an index in Svelte?

**Difficulty**: Beginner

**Strategy**:
Looping with an index is a basic but frequently needed skill when rendering lists where position matters, such as numbered items or alternating row styles. The second argument in the `{#each}` block provides the index, and a third argument is available for the key expression. A common pitfall is relying on the index as a key in dynamic lists where items can be added, removed, or reordered, which leads to incorrect DOM reuse.

**Code Example**:
```javascript
{#each items as item, index}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q17"></a>
### Q17: What is the `bind:this` directive?

**Difficulty**: Intermediate

**Strategy**:
To get a reference to a DOM element or component instance.

**Code Example**:
```javascript
<div bind:this={element}>...</div>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q18"></a>
### Q18: How do you prevent event bubbling in Svelte?

**Difficulty**: Beginner

**Strategy**:
Use event modifiers like `on:click|stopPropagation`.

**Code Example**:
```javascript
<button on:click|stopPropagation={handler}>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q19"></a>
### Q19: What is SvelteKit?

**Difficulty**: Intermediate

**Strategy**:
The official application framework for Svelte, handling routing, SSR, SSG, etc.

**Code Example**:
```javascript
// Similar to Next.js for React
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q20"></a>
### Q20: How do you use the `await` block?

**Difficulty**: Intermediate

**Strategy**:
The `await` block is a powerful Svelte feature that lets you handle promises declaratively in your template, eliminating the need for manual loading-state management in many cases. It provides three branches -- pending, resolved, and rejected -- giving you a clean way to show loading spinners, data, or error messages. A common pitfall is reassigning the promise variable on every render instead of keeping a stable reference, which causes the loading state to re-trigger unnecessarily.

**Code Example**:
```javascript
{#await promise}Loading...{:then value}{value}{:catch error}{error}{/await}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q21"></a>
### Q21: What are Custom Stores?

**Difficulty**: Advanced

**Strategy**:
Custom stores demonstrate advanced Svelte patterns by wrapping writable store internals behind a tailored API, which is key for encapsulating business logic in real applications. Any object with a `subscribe` method satisfies the store contract, so you can expose only the methods you want (like `increment`, `reset`) while hiding direct mutation. A best practice is to keep custom stores focused on a single domain and export them from dedicated modules for testability.

**Code Example**:
```javascript
function createCount() { const { subscribe } = writable(0); return { subscribe }; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q22"></a>
### Q22: How do you style components in Svelte?

**Difficulty**: Beginner

**Strategy**:
Styles in `<style>` blocks are scoped to the component by default.

**Code Example**:
```javascript
<style> p { color: red; } </style>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q23"></a>
### Q23: How do you use the @html tag?

**Difficulty**: Beginner

**Strategy**:
The `{@html}` tag is essential when you need to render raw HTML strings in your template, such as rich text from a CMS or Markdown output. Unlike normal interpolation, it bypasses Svelte's automatic HTML escaping, so you must sanitize any user-supplied content before passing it to `{@html}` to prevent XSS attacks. A common mistake is using it for simple text formatting when standard template syntax would be safer and more idiomatic.

**Code Example**:
```javascript
{@html post.content}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q24"></a>
### Q24: What is the difference between on:click and on:click|once?

**Difficulty**: Beginner

**Strategy**:
Modifiers change event behavior. `once` removes the handler after first trigger.

**Code Example**:
```javascript
<button on:click|once={handler}>Click me once</button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q25"></a>
### Q25: How do you forward events in Svelte?

**Difficulty**: Intermediate

**Strategy**:
Event forwarding is crucial for building wrapper components that transparently pass DOM events up to parent consumers without manual dispatching. Adding an `on:event` directive without a handler (e.g., `on:click`) on a DOM element forwards the event to the parent. A common pitfall is assuming custom events forward automatically -- only native DOM events forward with this pattern, while custom dispatched events must be explicitly forwarded via `createEventDispatcher`.

**Code Example**:
```javascript
<button on:click>Forwarded</button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q26"></a>
### Q26: What is the `class:` directive?

**Difficulty**: Beginner

**Strategy**:
The `class:` directive is Svelte's concise way to conditionally apply CSS classes, making it cleaner than string interpolation or ternary expressions in the `class` attribute. It adds the class when the expression is truthy and removes it when falsy, and you can use shorthand `class:name` when the variable name matches the class name. A best practice is to prefer `class:` over dynamic string concatenation because it integrates better with Svelte's scoped style analysis.

**Code Example**:
```javascript
<div class:active={isActive}>...</div>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q27"></a>
### Q27: How do you use `<svelte:window>`?

**Difficulty**: Intermediate

**Strategy**:
The `<svelte:window>` element is important for declaratively binding to window events like `resize`, `scroll`, or `keydown` without manual `addEventListener`/`removeEventListener` cleanup. You can also bind window properties such as `bind:scrollY` or `bind:innerWidth` for reactive access. A common mistake is placing `<svelte:window>` inside conditional blocks, which can cause unexpected event listener lifecycle issues.

**Code Example**:
```javascript
<svelte:window on:keydown={handleKeydown} />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q28"></a>
### Q28: What is `<svelte:body>`?

**Difficulty**: Intermediate

**Strategy**:
The `<svelte:body>` element lets you attach event listeners to the document body declaratively, which is useful for global interactions like mouse tracking or escape-key handling that should work regardless of which element is focused. Like `<svelte:window>`, it automatically handles listener cleanup when the component is destroyed. A best practice is to use it sparingly and prefer `<svelte:window>` for most global events, reserving `<svelte:body>` for events that specifically need body-level handling.

**Code Example**:
```javascript
<svelte:body on:mouseenter={handleEnter} />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q29"></a>
### Q29: How do you use `<svelte:head>`?

**Difficulty**: Intermediate

**Strategy**:
`<svelte:head>` allows components to inject elements into the document `<head>`, which is critical for per-page SEO tags, Open Graph metadata, and dynamically loading external stylesheets or scripts. During server-side rendering, these elements are merged into the initial HTML response, ensuring crawlers see them. A common pitfall is inserting duplicate tags (like multiple `<title>` elements) when multiple components each add their own head content, so coordinate ownership carefully.

**Code Example**:
```javascript
<svelte:head><title>Page</title></svelte:head>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q30"></a>
### Q30: What are Module Context scripts?

**Difficulty**: Advanced

**Strategy**:
Scripts that run once per module, not per instance.

**Code Example**:
```javascript
<script context="module">
  let totalComponents = 0;
</script>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q31"></a>
### Q31: How do you handle fallback content in slots?

**Difficulty**: Beginner

**Strategy**:
Fallback content in slots provides sensible defaults for reusable components when the consumer does not supply custom content. Any markup placed inside a `<slot>` tag is rendered only when the parent omits that slot, making components work out of the box while remaining extensible. A common pitfall is assuming fallback content is always rendered alongside consumer content, but it is completely replaced when content is provided.

**Code Example**:
```javascript
<slot>Default Content</slot>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q32"></a>
### Q32: What is `$$props`?

**Difficulty**: Advanced

**Strategy**:
An object containing all props passed to the component. Not recommended for general use.

**Code Example**:
```javascript
console.log($$props);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q33"></a>
### Q33: What is `$$restProps`?

**Difficulty**: Intermediate

**Strategy**:
`$$restProps` captures all props passed to a component that are not explicitly declared with `export let`, making it invaluable for building thin wrapper components that forward unknown attributes to an underlying element. It differs from `$$props` by excluding declared props, preventing accidental attribute duplication. A best practice is to use `$$restProps` with `{...$$restProps}` spread on the target element rather than manually forwarding individual attributes.

**Code Example**:
```javascript
<div {...$$restProps}></div>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q34"></a>
### Q34: How do you debug Svelte reactivity?

**Difficulty**: Beginner

**Strategy**:
Debugging reactivity is a common challenge in Svelte interviews because reactive bugs are often caused by subtle assignment issues like mutating arrays or objects in place. The `{@debug}` tag pauses execution and logs specified variables whenever they change, acting as a reactive-aware breakpoint. A common pitfall is expecting reactivity to trigger on property mutations like `obj.key = newVal` without reassigning the variable itself; you must use `obj = obj` or spread patterns to notify Svelte of the change.

**Code Example**:
```javascript
{@debug count}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q35"></a>
### Q35: What is the `key` block?

**Difficulty**: Intermediate

**Strategy**:
The `{#key}` block forces Svelte to destroy and recreate its contents whenever the key expression changes, which is useful for resetting component state or re-triggering transitions. Unlike keyed `{#each}` blocks which reconcile list items, `{#key}` destroys the entire subtree and rebuilds it from scratch. A common use case is resetting a form or animation when an ID changes, but overusing it can hurt performance since it bypasses Svelte's efficient DOM diffing.

**Code Example**:
```javascript
{#key id}<Component />{/key}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q36"></a>
### Q36: How do you define props in Svelte?

**Difficulty**: Beginner

**Strategy**:
Props are the foundational mechanism for passing data into child components, and understanding them is essential for any Svelte interview. Props are declared using `export let` inside the component's script block, and default values can be provided directly in the declaration. A common pitfall is forgetting that prop changes from the parent trigger reactive updates in the child, so you should avoid simultaneously mutating a prop locally and from the parent.

**Code Example**:
```javascript
export let name = 'World';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q37"></a>
### Q37: What is `createEventDispatcher`?

**Difficulty**: Intermediate

**Strategy**:
`createEventDispatcher` is the standard way for child components to communicate upward to parents, which is critical to understand since Svelte uses one-way data flow. The dispatcher must be instantiated at component initialization time (top level of the script), not lazily inside functions. Note that in Svelte 5, this pattern is replaced by callback props, so mentioning both approaches in an interview demonstrates up-to-date knowledge.

**Code Example**:
```javascript
const dispatch = createEventDispatcher();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q38"></a>
### Q38: How do you use the `use:action` directive?

**Difficulty**: Advanced

**Strategy**:
Actions are a powerful but underutilized Svelte feature that lets you directly interact with DOM elements when they are created, making them ideal for integrating third-party libraries, tooltips, drag-and-drop, and click-outside detection. The action function receives the DOM node and optional parameters, and can return an update and destroy lifecycle. A best practice is to keep actions focused on a single concern and make them reusable across components by defining them in separate utility files.

**Code Example**:
```javascript
<div use:action={params} />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q39"></a>
### Q39: What is the return value of an action?

**Difficulty**: Advanced

**Strategy**:
Understanding action return values is essential for writing production-quality actions that properly clean up after themselves and respond to parameter changes. The returned object can include `destroy` (called when the element is removed), `update` (called when parameters change), and an `abort` method for intro transitions. A common pitfall is forgetting to return a `destroy` function, which leads to memory leaks from dangling event listeners or intervals.

**Code Example**:
```javascript
return { destroy() { ... } }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q40"></a>
### Q40: How do you bind `this` in Svelte?

**Difficulty**: Intermediate

**Strategy**:
The `bind:this` directive gives you a direct reference to a DOM element or component instance, which is necessary when you need to call imperative methods like `focus()`, `scrollIntoView()`, or measure element dimensions. The bound variable is `undefined` until the element mounts, so you must guard against accessing it before `onMount` fires. A best practice is to prefer declarative Svelte patterns over imperative `bind:this` whenever possible.

**Code Example**:
```javascript
<div bind:this={element}></div>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q41"></a>
### Q41: How do you bind component props?

**Difficulty**: Intermediate

**Strategy**:
Binding component props with `bind:` on a child component enables two-way data flow, which is essential for form-like patterns where child components manage their own state but the parent needs to stay in sync. This works by allowing the child to write back to the parent's variable through its exported prop. A common pitfall is using `bind:` on components that don't expect it, since the child must explicitly declare the prop with `export let` for binding to work.

**Code Example**:
```javascript
<Child bind:value={parentValue} />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q42"></a>
### Q42: What is the `store` contract?

**Difficulty**: Advanced

**Strategy**:
The store contract is the foundation of Svelte's reactivity system for cross-component state, and understanding it unlocks the ability to create any custom store implementation. An object qualifies as a store if it has a `subscribe` method that returns an `unsubscribe` function, and Svelte's `$` prefix auto-subscription relies on this contract alone. A common pitfall is forgetting to return the unsubscribe function from `subscribe`, which causes memory leaks in long-lived components.

**Code Example**:
```javascript
const store = { subscribe: (cb) => { ... } }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q43"></a>
### Q43: How do you auto-subscribe to a store?

**Difficulty**: Beginner

**Strategy**:
Auto-subscription with the `$` prefix is Svelte's most ergonomic store feature, eliminating the need for manual `subscribe`/`unsubscribe` lifecycle management. The compiler automatically subscribes when the component mounts and unsubscribes when it destroys, and you can both read and write to `$store` in reactive contexts. A common mistake is trying to use the `$` prefix in non-component files like plain `.js` utilities, where it is not compiled and will throw an error.

**Code Example**:
```javascript
<h1>{$count}</h1>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q44"></a>
### Q44: What is `get` from `svelte/store`?

**Difficulty**: Intermediate

**Strategy**:
Gets the current value of a store synchronously (not reactive).

**Code Example**:
```javascript
const value = get(store);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q45"></a>
### Q45: How do you make a store read-only?

**Difficulty**: Intermediate

**Strategy**:
Making stores read-only is important for enforcing unidirectional data flow and protecting shared state from unintended mutations by consumer components. The `readonly` utility wraps a writable store and exposes only the `subscribe` method, silently ignoring any `set` or `update` calls. A best practice is to export writable stores as `readonly` from modules when consumers should only read the state, while keeping the writable reference private for authorized mutations.

**Code Example**:
```javascript
const read = readonly(write);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q46"></a>
### Q46: What is `derived` store?

**Difficulty**: Intermediate

**Strategy**:
Derived stores are the Svelte equivalent of computed properties at the application level, letting you compute new state from one or more source stores without duplicating logic. They automatically recalculate when any dependency changes and support both synchronous and asynchronous derivation functions. A common pitfall is performing expensive computations inside the derivation without using the `get()` function or caching, which can degrade performance in frequently updated stores.

**Code Example**:
```javascript
const double = derived(count, $c => $c * 2);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q47"></a>
### Q47: How do you use `style:` directive?

**Difficulty**: Beginner

**Strategy**:
The `style:` directive provides a clean way to set inline styles reactively, avoiding the string concatenation mess of the traditional `style` attribute. Svelte also supports shorthand like `style:color` when the CSS property name matches the variable name. A best practice is to use `style:` for dynamic values that change at runtime (like positions or dimensions) while keeping static styles in the `<style>` block for better scoping and maintainability.

**Code Example**:
```javascript
<div style:color={color}>text</div>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q48"></a>
### Q48: What is `svelte:options`?

**Difficulty**: Advanced

**Strategy**:
Compiler options for the component (immutable, accessors).

**Code Example**:
```javascript
<svelte:options immutable={true} />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q49"></a>
### Q49: How do you detect if code is running in browser?

**Difficulty**: Beginner

**Strategy**:
Use `browser` from `$app/environment` (SvelteKit) or check `typeof window`.

**Code Example**:
```javascript
if (browser) { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q50"></a>
### Q50: What is Hydration?

**Difficulty**: Advanced

**Strategy**:
Hydration is a critical concept in SSR applications because it bridges server-rendered static HTML with interactive client-side Svelte components, and interviewers often test this to gauge SSR understanding. During hydration, Svelte attaches event listeners and reactive state to the existing DOM without destroying and recreating it, which preserves the fast initial paint from SSR. A common pitfall is generating mismatched HTML between server and client, which forces Svelte to discard the server-rendered DOM and re-render from scratch.

**Code Example**:
```javascript
// Svelte handles this automatically
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q51"></a>
### Q51: How do you create a transition?

**Difficulty**: Advanced

**Strategy**:
Custom transitions let you create bespoke animation effects beyond the built-in `fade`, `slide`, and `fly`, which is valuable for branded or complex UI motion design. A transition function receives the DOM node and a parameters object, and must return a CSS or JavaScript animation object with `duration`, `delay`, and easing properties. A common pitfall is forgetting to handle the `direction` parameter (`in` or `out`) when the transition should behave differently for enter versus exit.

**Code Example**:
```javascript
function fade(node, { duration }) { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q52"></a>
### Q52: What is `crossfade`?

**Difficulty**: Advanced

**Strategy**:
Creates a pair of transitions for moving elements.

**Code Example**:
```javascript
const [send, receive] = crossfade(...) 
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q53"></a>
### Q53: How do you use `animate:flip`?

**Difficulty**: Intermediate

**Strategy**:
The `animate:flip` directive creates smooth position-change animations when list items are reordered, which significantly improves user experience in sortable lists and filtered views. It works by remembering an element's position before the update and animating it to the new position using the FLIP (First, Last, Invert, Play) technique. A common pitfall is using `animate:flip` without a keyed `{#each}` block, which causes the animation to target wrong elements.

**Code Example**:
```javascript
<li animate:flip>{item}</li>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q54"></a>
### Q54: What is `svelte:fragment`?

**Difficulty**: Intermediate

**Strategy**:
A container for slots that doesn't render a DOM element.

**Code Example**:
```javascript
<svelte:fragment slot="header">...</svelte:fragment>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q55"></a>
### Q55: How do you lazy load a component?

**Difficulty**: Advanced

**Strategy**:
Use dynamic imports in `await` block or SvelteKit's features.

**Code Example**:
```javascript
{#await import('./Comp.svelte') then {default: Comp}} <Comp /> {/await}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q56"></a>
### Q56: What is the difference between `bind:group` and `bind:value`?

**Difficulty**: Intermediate

**Strategy**:
Understanding these two binding mechanisms is important for building forms correctly, as they serve different purposes for different input types. `bind:value` binds the input's value to a variable for text and select inputs, while `bind:group` binds multiple radio buttons or checkboxes to a single shared variable, automatically managing checked state. A common pitfall is using `bind:value` on radio buttons instead of `bind:group`, which prevents proper mutual exclusion behavior.

**Code Example**:
```javascript
<input type=radio bind:group={flavour} value=scoop>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q57"></a>
### Q57: How do you handle multiple classes?

**Difficulty**: Beginner

**Strategy**:
Managing multiple conditional classes is a day-to-day task in component development, and Svelte offers several approaches worth comparing in interviews. You can combine static class strings with ternary expressions, use multiple `class:` directives, or pass an object or array to the `class` attribute. A best practice is to prefer the `class:` directive for conditional classes because it produces cleaner template code and works seamlessly with Svelte's scoped style system.

**Code Example**:
```javascript
class="btn {active ? 'active' : ''}"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q58"></a>
### Q58: What is `svelte-ignore`?

**Difficulty**: Intermediate

**Strategy**:
The `svelte-ignore` comment directive lets you suppress specific compiler warnings, most commonly accessibility warnings that are false positives in your specific context. Svelte includes strong a11y warnings by default (like requiring alt attributes on images and key events on clickable elements), which is a great feature but sometimes needs selective suppression. A best practice is to always add a comment explaining why the ignore is justified, rather than silencing warnings out of convenience.

**Code Example**:
```javascript
<!-- svelte-ignore a11y-click-events-have-key-events -->
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q59"></a>
### Q59: How do you access the component instance?

**Difficulty**: Advanced

**Strategy**:
Accessing a component instance via `bind:this` is necessary when you need to call methods exposed by the child component imperatively from the parent. For this to work, the child must export functions from its script block so they are accessible on the instance object. A common pitfall is trying to access the instance before the component mounts (the variable will be `undefined`), so always guard instance method calls inside `onMount` or after lifecycle confirmation.

**Code Example**:
```javascript
<Component bind:this={instance} />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q60"></a>
### Q60: What is `beforeUpdate`?

**Difficulty**: Intermediate

**Strategy**:
`beforeUpdate` is a lifecycle function that runs before the DOM is updated after a state change, useful for measuring or saving the previous DOM state. It fires on initial render as well, unlike `afterUpdate`, so you need to handle the first-call case explicitly. A common pitfall is modifying reactive state inside `beforeUpdate`, which can create infinite update loops since state changes trigger another `beforeUpdate` call.

**Code Example**:
```javascript
beforeUpdate(() => { ... })
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q61"></a>
### Q61: What is `afterUpdate`?

**Difficulty**: Intermediate

**Strategy**:
`afterUpdate` runs after the DOM has been updated following a state change, making it the right place to perform DOM measurements, third-party library synchronization, or scroll-position adjustments. Unlike `beforeUpdate`, it does not fire on the initial render, only on subsequent updates. A common pitfall is calling `afterUpdate` to modify state that triggers another update, creating an infinite loop that degrades performance.

**Code Example**:
```javascript
afterUpdate(() => { ... })
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q62"></a>
### Q62: How do you create a custom store?

**Difficulty**: Intermediate

**Strategy**:
Return an object with subscribe and other methods.

**Code Example**:
```javascript
function createCount() { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q63"></a>
### Q63: What is `spring` motion?

**Difficulty**: Intermediate

**Strategy**:
`spring` provides physics-based animation that feels natural because it uses stiffness and damping parameters instead of fixed durations, making it ideal for interactive elements like drag handles and toggles. Unlike `tweened`, spring animations naturally handle interruptions gracefully -- if the target value changes mid-animation, the spring adjusts smoothly without jarring resets. A common pitfall is setting the stiffness too high, which causes rapid oscillations that look buggy rather than smooth.

**Code Example**:
```javascript
const coords = spring({ x: 0, y: 0 });
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q64"></a>
### Q64: What is `tweened` motion?

**Difficulty**: Intermediate

**Strategy**:
`tweened` provides time-based interpolation between values using easing functions, which is ideal for progress bars, sliders, and other UI elements that need predictable duration-based animation. It interpolates between the current and target value over a specified duration whenever the store value changes. A common pitfall is rapid successive updates to the same tweened store, which restarts the animation each time and can appear stuttery; use `spring` instead for frequently changing interactive values.

**Code Example**:
```javascript
const progress = tweened(0);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q65"></a>
### Q65: How do you use `svelte:self`?

**Difficulty**: Intermediate

**Strategy**:
`svelte:self` allows a component to render instances of itself recursively, which is essential for tree views, nested menus, comment threads, and other recursive data structures. Without it, you would need to dynamically import the component or use `<svelte:component>` with a reference to itself. A common pitfall is forgetting to provide a base case in your template logic, which causes infinite recursion and crashes the browser.

**Code Example**:
```javascript
<svelte:self {children} />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q66"></a>
### Q66: What is the `src/routes` folder in SvelteKit?

**Difficulty**: Beginner

**Strategy**:
The `src/routes` folder is the backbone of SvelteKit's file-based routing system, where the directory structure directly maps to your application's URL structure. Each route directory can contain page components, server logic, layout wrappers, and error handlers, making it intuitive to organize features by URL. A common pitfall is mixing up page files and layout files or placing non-route files directly in the routes directory, which can accidentally create unwanted routes.

**Code Example**:
```javascript
// +page.svelte
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q67"></a>
### Q67: What is a `+page.svelte` file?

**Difficulty**: Beginner

**Strategy**:
`+page.svelte` is the core building block of SvelteKit routing, representing the UI component rendered when a user visits a specific route. It receives data from its corresponding `+page.js` or `+page.server.js` load function through the `data` prop, keeping data fetching and presentation cleanly separated. A common mistake is putting server-only logic (database calls, private env vars) directly in `+page.svelte` instead of the server load file.

**Code Example**:
```javascript
<h1>Hello</h1>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q68"></a>
### Q68: What is a `+page.server.js` file?

**Difficulty**: Intermediate

**Strategy**:
`+page.server.js` is critical for SvelteKit's server-side data loading, as its `load` function runs exclusively on the server and has access to databases, private environment variables, and other server-only resources. The returned data is serialized and passed to the page component as props, and during client-side navigation it is fetched via a network call. A common pitfall is returning non-serializable values (like functions or class instances) from load, which causes runtime errors during dehydration.

**Code Example**:
```javascript
export function load() { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q69"></a>
### Q69: What is a `+layout.svelte` file?

**Difficulty**: Beginner

**Strategy**:
Layout components wrap all pages within their route subtree, making them essential for shared UI elements like navigation bars, sidebars, and footers that persist across page navigations. The `<slot/>` tag in a layout renders the matched child page or nested layout, and layouts can be nested by placing `+layout.svelte` files at different route depths. A common pitfall is putting one-time initialization logic in layouts that rerun on every child navigation.

**Code Example**:
```javascript
<slot />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q70"></a>
### Q70: How do you handle form actions in SvelteKit?

**Difficulty**: Intermediate

**Strategy**:
Form actions are SvelteKit's built-in solution for handling form submissions on the server, providing a progressive-enhancement-friendly alternative to custom API endpoints. Named actions in `+page.server.js` receive form data, validate it, and return success or failure results that the page component can react to. A best practice is always validating input on the server side even if you have client-side validation, because client validation can be bypassed.

**Code Example**:
```javascript
export const actions = { default: async ({ request }) => { ... } }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q71"></a>
### Q71: What is `enhance` in SvelteKit forms?

**Difficulty**: Intermediate

**Strategy**:
The `use:enhance` directive progressively enhances standard HTML forms to use SvelteKit's client-side navigation instead of full page reloads, while maintaining full functionality without JavaScript. It intercepts the form submission, sends it via `fetch`, and handles the response without a page reload, giving users a smoother experience. A common pitfall is adding custom submit handlers with `use:enhance` without calling `form.submit()` or managing the `cancel()` method, which breaks the default enhanced behavior.

**Code Example**:
```javascript
<form use:enhance>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q72"></a>
### Q72: How do you use environment variables?

**Difficulty**: Intermediate

**Strategy**:
Environment variables in SvelteKit are split into public (`$env/static/public`) and private (`$env/static/private`) modules, which is critical for security since private variables are never exposed to the client bundle. Static imports are validated at build time and replaced with actual values, while dynamic imports from `$env/dynamic/*` read values at request time. A common pitfall is accidentally importing a private env var in a client-side file, which SvelteKit will catch and throw an error for.

**Code Example**:
```javascript
import { API_KEY } from '$env/static/private';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q73"></a>
### Q73: What is adapter in SvelteKit?

**Difficulty**: Intermediate

**Strategy**:
Plugins to deploy apps to different platforms (Node, Vercel, Static).

**Code Example**:
```javascript
import adapter from '@sveltejs/adapter-auto';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q74"></a>
### Q74: How do you handle errors in SvelteKit?

**Difficulty**: Intermediate

**Strategy**:
Error handling in SvelteKit uses a layered approach with `+error.svelte` pages at each route level, `handleError` hooks for unexpected errors, and the `error()` function for expected HTTP errors. The `error()` function throws a properly formatted HTTP error that the nearest error boundary catches and displays. A best practice is to create custom error pages for common status codes and to use `handleError` in `hooks.server.js` for logging unexpected errors to monitoring services.

**Code Example**:
```javascript
throw error(404, 'Not found');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q75"></a>
### Q75: What is `hooks.server.js`?

**Difficulty**: Advanced

**Strategy**:
`hooks.server.js` is the central interception layer in SvelteKit that runs on every server request, making it essential for authentication, logging, CORS handling, and request transformation. The `handle` function wraps every request and can modify the request before it reaches your route and the response before it reaches the client. A common pitfall is making `handle` async operations expensive (like unnecessary database calls on every request), which adds latency to every page load.

**Code Example**:
```javascript
export async function handle({ event, resolve }) { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q76"></a>
### Q76: How do you prefetch data?

**Difficulty**: Intermediate

**Strategy**:
Prefetching dramatically improves perceived performance by loading route data and code before the user clicks a link, making navigation feel instant. The `data-sveltekit-preload-data` attribute on anchor tags triggers prefetching on hover by default, and you can configure it globally or per-link. A common pitfall is over-prefetching on pages with many links, which can saturate the user's bandwidth and slow down the current page.

**Code Example**:
```javascript
<a href="/blog" data-sveltekit-preload-data>Blog</a>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q77"></a>
### Q77: What is the difference between `onMount` and `load`?

**Difficulty**: Intermediate

**Strategy**:
`onMount` is client-side lifecycle. `load` is SvelteKit data loading (server/client).

**Code Example**:
```javascript
// load runs before render
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q78"></a>
### Q78: How do you use global styles?

**Difficulty**: Beginner

**Strategy**:
Understanding global versus scoped styles is essential because Svelte scopes all `<style>` block CSS to the component by default, but real applications need some global styles for resets, fonts, and theme variables. The `:global()` modifier lets you break out of scoping for specific selectors, and you can also place global CSS in a top-level stylesheet imported in your root layout. A best practice is to minimize global styles and use CSS custom properties for theming to keep component encapsulation intact.

**Code Example**:
```javascript
:global(body) { margin: 0; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q79"></a>
### Q79: What is accessibility warning in Svelte?

**Difficulty**: Beginner

**Strategy**:
Svelte's built-in accessibility warnings are a standout feature that catches common a11y mistakes at compile time, such as missing `alt` attributes, non-semantic clickable elements, and improper ARIA usage. These warnings help developers build inclusive applications by default without needing external linting tools. A best practice is to fix the underlying issue rather than silencing warnings with `svelte-ignore`, unless there is a well-documented reason for the exception.

**Code Example**:
```javascript
// e.g., <img> missing alt
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q80"></a>
### Q80: How do you optimize loops?

**Difficulty**: Intermediate

**Strategy**:
Optimizing loops is crucial for rendering large lists efficiently in Svelte, and interviewers use this to assess whether you understand reconciliation performance. Key techniques include using keyed `{#each}` blocks with unique identifiers, avoiding expensive computations inside the loop body, and leveraging the `immutable` compiler option when list data never mutates in place. A common pitfall is creating new object references on every render for items that haven't changed, which forces unnecessary DOM updates.

**Code Example**:
```javascript
{#each items as item (item.id)}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q81"></a>
### Q81: What is the purpose of `tick` in tests?

**Difficulty**: Advanced

**Strategy**:
`tick()` is essential in testing because Svelte batches DOM updates asynchronously, so assertions immediately after state changes may fail if the DOM hasn't updated yet. Calling `await tick()` flushes all pending updates and ensures the DOM reflects the current state before you make assertions. A common pitfall is using arbitrary `setTimeout` delays instead of `tick()`, which makes tests flaky and slow.

**Code Example**:
```javascript
await tick(); expect(...)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q82"></a>
### Q82: How do you test Svelte components?

**Difficulty**: Intermediate

**Strategy**:
Testing components effectively is crucial for maintaining confidence in your UI code, and Svelte's compiled output requires specific tooling like `@testing-library/svelte` or `svelte-testing-library`. These tools encourage testing user-visible behavior (clicking, typing, reading text) rather than implementation details like internal state variables. A best practice is to use `vitest` as the test runner since it shares the same Vite configuration as your SvelteKit project, eliminating configuration drift.

**Code Example**:
```javascript
render(Component);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q83"></a>
### Q83: What is `vite` in Svelte context?

**Difficulty**: Beginner

**Strategy**:
Vite is the build tool that powers SvelteKit, replacing older bundlers like Rollup and Webpack with dramatically faster development experience through native ES modules and hot module replacement. In development, Vite serves modules on demand without bundling, giving near-instant startup, and in production it uses Rollup for optimized output. A common pitfall is assuming all Vite plugins work with SvelteKit out of the box, since some require specific Svelte-aware configuration.

**Code Example**:
```javascript
// Fast HMR
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q84"></a>
### Q84: How do you deploy a Svelte app?

**Difficulty**: Beginner

**Strategy**:
Deployment is the final step in delivering a Svelte application, and the approach depends on whether you use SvelteKit (with adapters) or plain Svelte (static build). For SvelteKit, adapters transform the build output for specific platforms like Vercel, Netlify, or a Node.js server, while plain Svelte outputs static assets deployable to any hosting provider. A common pitfall is forgetting to set the correct adapter before deploying, which results in a build that doesn't work on the target platform.

**Code Example**:
```javascript
npm run build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q85"></a>
### Q85: What is `svelte-check`?

**Difficulty**: Intermediate

**Strategy**:
`svelte-check` is a command-line tool that performs type checking and static analysis on your entire Svelte project, catching errors that the editor might miss. It checks TypeScript types in script blocks, validates component props, detects unused CSS, and reports accessibility warnings across all files. A best practice is to integrate `svelte-check` into your CI pipeline to prevent type errors and a11y issues from reaching production.

**Code Example**:
```javascript
svelte-check --watch
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q86"></a>
### Q86: How do you use TypeScript with Svelte?

**Difficulty**: Beginner

**Strategy**:
TypeScript integration is a key skill since modern Svelte projects default to TypeScript, and interviewers expect you to know how to type props, events, and stores properly. Add `lang="ts"` to your script tag to enable TypeScript, and Svelte's preprocessor handles type stripping at build time. A common pitfall is not properly typing generic stores or event payloads, which weakens the type safety benefits that TypeScript provides.

**Code Example**:
```javascript
<script lang="ts">
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q87"></a>
### Q87: What is `$$slots`?

**Difficulty**: Advanced

**Strategy**:
`$$slots` is a special object that tells you which named slots the parent has provided content for, enabling conditional rendering based on slot presence. This is useful for layout components that should only render wrapper elements (like headers or footers) when the corresponding slot content exists. A common pitfall is checking for default slot content with `$$slots.default`, which can be truthy even when the parent passes only whitespace.

**Code Example**:
```javascript
if ($$slots.header) { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q88"></a>
### Q88: How do you debounce an input?

**Difficulty**: Intermediate

**Strategy**:
Debouncing is essential for performance when handling rapid-fire input events like search-as-you-type, preventing excessive API calls or expensive computations on every keystroke. The pattern uses `setTimeout` and `clearTimeout` to delay processing until the user pauses typing, typically for 300-500 milliseconds. A common pitfall is forgetting to clear the timeout when the component is destroyed via `onDestroy`, which can cause "state update on unmounted component" errors.

**Code Example**:
```javascript
let timer; const handle = () => { clearTimeout(timer); timer = setTimeout(...) }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q89"></a>
### Q89: What is `await` block `catch`?

**Difficulty**: Beginner

**Strategy**:
The `{:catch}` branch of the `await` block handles promise rejections declaratively in your template, giving you a clean way to display error messages without try/catch wrapping in your script. It receives the rejection value as a variable you can use to show specific error details to the user. A best practice is to always include a `{:catch}` branch in your `await` blocks, since unhandled promise rejections in templates fail silently and leave users staring at a loading state.

**Code Example**:
```javascript
{:catch error} {error.message}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q90"></a>
### Q90: How do you use `placeholder` attribute on inputs?

**Difficulty**: Beginner

**Strategy**:
The placeholder attribute is a basic but important UX feature for form inputs, providing hint text that guides users on expected input format. In Svelte, standard HTML attributes like `placeholder` work as expected, and you can bind the value dynamically with `bind:value` or set it via a variable. A best practice is to use placeholder as a supplementary hint rather than a replacement for proper labels, since placeholder text disappears when users start typing.

**Code Example**:
```javascript
<input placeholder="Type here" />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q91"></a>
### Q91: Can you have multiple script tags?

**Difficulty**: Advanced

**Strategy**:
Svelte supports exactly two script tags per component: one with `context="module"` for instance-shared logic and one regular script for per-instance logic, and understanding their differences is key to advanced component design. The module script runs once when the component is first imported and shares its exported values across all instances, while the instance script runs for each component creation. A common pitfall is trying to access instance-specific variables (like props or reactive declarations) from the module script, which is impossible since the module context has no access to individual component state.

**Code Example**:
```javascript
<script context="module">...</script><script>...</script>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q92"></a>
### Q92: What is `immutable` option?

**Difficulty**: Advanced

**Strategy**:
The `immutable` compiler option is a performance optimization that tells Svelte it can skip equality checks on prop changes, relying on reference equality instead of deep comparison. When enabled, Svelte assumes that if a prop reference hasn't changed, its value hasn't either, which eliminates unnecessary update checks in data-heavy components. A common pitfall is enabling `immutable` while still mutating objects in place, which causes the UI to silently stop updating because Svelte thinks nothing changed.

**Code Example**:
```javascript
<svelte:options immutable />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q93"></a>
### Q93: How do you access `window` safely in SSR?

**Difficulty**: Intermediate

**Strategy**:
Accessing `window` safely is critical in SvelteKit applications because server-side rendering runs in Node.js where `window` is undefined, causing crashes if you reference it unconditionally. The safest approach is to use `onMount` (which only runs in the browser) or check `typeof window !== 'undefined'` before accessing it. A common pitfall is using `window` in reactive declarations or at the top level of a component script, which executes during SSR and throws a reference error.

**Code Example**:
```javascript
onMount(() => window.scrollTo(0,0))
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q94"></a>
### Q94: What is `svelte/motion`?

**Difficulty**: Intermediate

**Strategy**:
The `svelte/motion` module provides `spring` and `tweened` stores that animate numeric values over time, bridging the gap between state management and visual animation. These animated stores behave like regular stores but interpolate their values when updated, making them ideal for progress indicators, animated counters, and drag interactions. A common pitfall is using motion stores for CSS-animatable properties where `transition:` directives would be more performant since they leverage the browser's animation engine.

**Code Example**:
```javascript
import { spring } from 'svelte/motion';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q95"></a>
### Q95: What is `svelte/easing`?

**Difficulty**: Beginner

**Strategy**:
The `svelte/easing` module provides a comprehensive library of easing functions that control the acceleration curve of animations and transitions, which is essential for creating natural-feeling motion. Easing functions like `cubicInOut`, `elasticOut`, and `bounceOut` transform a linear time progression into non-linear curves that match real-world physics. A best practice is to use `easeInOut` variants for most UI transitions and reserve dramatic easings like `bounce` or `elastic` for playful, attention-grabbing moments.

**Code Example**:
```javascript
import { bounceOut } from 'svelte/easing';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q96"></a>
### Q96: How do you pass data to layout?

**Difficulty**: Intermediate

**Strategy**:
Return data from `load` function in layout.server.js.

**Code Example**:
```javascript
return { user: ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q97"></a>
### Q97: What is `page` store in SvelteKit?

**Difficulty**: Intermediate

**Strategy**:
The `page` store is a central SvelteKit store that provides reactive access to the current URL, parameters, and route data, making it essential for navigation-aware UI components. It exposes `$page.url`, `$page.params`, `$page.route`, and `$page.data`, all of which update automatically during client-side navigation. A common pitfall is destructuring the page store outside of reactive contexts, which captures stale values instead of tracking changes.

**Code Example**:
```javascript
import { page } from '$app/stores';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q98"></a>
### Q98: How do you use `navigating` store?

**Difficulty**: Intermediate

**Strategy**:
The `navigating` store provides a reactive way to detect when client-side navigation is in progress, which is essential for showing loading indicators during slow data fetches. It is `null` when no navigation is active and contains `from` and `to` route information during navigation, letting you build global progress bars or skeleton loaders. A common pitfall is relying on `navigating` for page transitions that are fast enough to not need indicators, which causes distracting flash effects.

**Code Example**:
```javascript
if ($navigating) Loading...
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q99"></a>
### Q99: What is `updated` store?

**Difficulty**: Advanced

**Strategy**:
The `updated` store is a SvelteKit feature for handling service worker updates, becoming `true` when a new version of the application is available after the initial load. This enables you to prompt users to reload for the latest version, which is critical for applications that are updated frequently. A best practice is to show a non-intrusive toast or banner rather than forcing an immediate reload, giving users control over when they switch to the new version.

**Code Example**:
```javascript
if ($updated) location.reload()
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q100"></a>
### Q100: How do you handle 404s?

**Difficulty**: Beginner

**Strategy**:
Handling 404s properly is important for user experience and SEO, and SvelteKit provides a structured approach through error boundaries and the `$page.status` value. You create `+error.svelte` components at different route levels to display custom not-found pages, and the root-level error page acts as a catch-all for unmatched routes. A best practice is to include helpful navigation links and a search function on your 404 page to help users find what they were looking for.

**Code Example**:
```javascript
<h1>Error {$page.status}</h1>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q101"></a>
### Q101: What is `data-sveltekit-reload`?

**Difficulty**: Intermediate

**Strategy**:
The `data-sveltekit-reload` attribute forces a full page reload instead of SvelteKit's default client-side navigation, which is necessary for certain scenarios like linking to external domains or resetting application state. Without it, SvelteKit intercepts all internal link clicks and handles them via the router, which can cause issues with third-party scripts that expect a full page load. A common use case is adding it to logout links to ensure all client-side state is cleared.

**Code Example**:
```javascript
<a href="/" data-sveltekit-reload>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q102"></a>
### Q102: How do you reset a store?

**Difficulty**: Intermediate

**Strategy**:
Resetting a store to its initial state is a common requirement in form workflows, game state management, and logout handlers, making it a practical interview topic. The approach depends on your store type: for writable stores, call `.set(initialValue)`, and for custom stores, expose a dedicated `reset()` method. A best practice is to store the initial value in a separate constant so you always have a clean reference to reset to, rather than hardcoding the same value in multiple places.

**Code Example**:
```javascript
store.set(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>