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
Use the `$:` label. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Use `createEventDispatcher`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Use the `<slot>` element. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Provide a unique key in parentheses. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Use `bind:value`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Import from `svelte/transition`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
To insert elements into the document `<head>`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Add a second argument to the `#each` block. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
To handle promises directly in the template. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Any object with a `subscribe` method is a store. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
To render raw HTML strings. Be careful of XSS. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
By adding `on:eventname` without a handler. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Conditionally toggle classes. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
To add event listeners to the window object. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
To add listeners to document.body. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
To inject elements into the head (title, meta). This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Put content inside the `<slot>` tag. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Props that are not explicitly exported. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Use `{@debug variable}`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Re-creates the component when the key changes. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Use the `export` keyword. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Creates a function to dispatch custom events. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Attaches a lifecycle to an element. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
An object with `update` and `destroy` methods. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Use `bind:this` to get a reference. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Use `bind:propName`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Any object with a `subscribe` method. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Prefix with `$`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Use `readonly` from `svelte/store`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
A store based on other stores. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Set inline styles conditionally. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Attaching interactivity to server-rendered HTML. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Return a config object (duration, css, tick). This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Animates reordering of list items. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
`bind:group` is for radio/checkbox groups. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Standard class attribute or `class:` directive. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Comments to suppress compiler warnings. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Use `bind:this` on the component tag. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Runs before the DOM updates. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Runs after the DOM updates. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Physics-based store for animations. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Interpolation-based store. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Recursively render the current component. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
File-based routing directory. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Defines the UI for a route. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Server-side load function for data. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Defines a layout wrapper for pages. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Export `actions` in `+page.server.js`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Progressive enhancement for forms. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Import from `$env/static/private` or `public`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Use `+error.svelte` or throw `error()` helper. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Global server-side hooks (handle, fetch). This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Use `<a data-sveltekit-preload-data>`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Use `:global(...)` or a global stylesheet. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Compiler warnings for A11y issues. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Use keyed each blocks. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
To wait for DOM updates after state change. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Using `@testing-library/svelte`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
The build tool and dev server. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Build via adapter and deploy output. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
CLI tool for type checking and diagnostics. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Add `lang="ts"` to script tag. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Object checking which slots are passed. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Custom action or logic in handler. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Handles promise rejection. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Standard HTML attribute. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Yes, one `context="module"` and one normal. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Tells Svelte to use strict equality for props. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Check `browser` check or `onMount`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Module for `spring` and `tweened`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Easing functions for transitions. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Contains info about current route, params, data. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Tracks navigation state. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Notifies when a new version of app is available. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Create a `+error.svelte` file. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Forces a full page reload on link click. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Manually set it to initial value. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
store.set(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>