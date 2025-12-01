<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/vue-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>Vue Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for developers</b></p>
</div>

---

## Table of Contents

1. [You are migrating a Vue 2 app to Vue 3. You notice that reactivity is not working for a new property added to an object. Why does this happen in Vue 2 but works in Vue 3?](#q1-you-are-migrating-a-vue-2-app-to-vue-3.-you-notice-that-reactivity-is-not-working-for-a-new-property-added-to-an-object.-why-does-this-happen-in-vue-2-but-works-in-vue-3) <span class="intermediate">Intermediate</span>
2. [When using the Composition API, should you use `ref` or `reactive` for declaring state? What are the trade-offs?](#q2-when-using-the-composition-api-should-you-use-ref-or-reactive-for-declaring-state-what-are-the-trade-offs) <span class="intermediate">Intermediate</span>
3. [You have a large list of items and `v-if` / `v-for` on the same element. Why is this considered a bad practice and how do you fix it?](#q3-you-have-a-large-list-of-items-and-v-if--v-for-on-the-same-element.-why-is-this-considered-a-bad-practice-and-how-do-you-fix-it) <span class="intermediate">Intermediate</span>
4. [How do you share logic between components in Vue 3 using Composables?](#q4-how-do-you-share-logic-between-components-in-vue-3-using-composables) <span class="intermediate">Intermediate</span>
5. [You need to render a modal that is visually separate from the main app layout (e.g., outside `overflow: hidden` containers). How do you achieve this in Vue 3?](#q5-you-need-to-render-a-modal-that-is-visually-separate-from-the-main-app-layout-e.g.-outside-overflow:-hidden-containers.-how-do-you-achieve-this-in-vue-3) <span class="intermediate">Intermediate</span>
6. [How do you ensure the DOM has updated before performing an action using `nextTick`?](#q6-how-do-you-ensure-the-dom-has-updated-before-performing-an-action-using-nexttick) <span class="intermediate">Intermediate</span>
7. [How do you scope styles to a component effectively using CSS Modules vs Scoped Styles?](#q7-how-do-you-scope-styles-to-a-component-effectively-using-css-modules-vs-scoped-styles) <span class="intermediate">Intermediate</span>
8. [How do you map Options API lifecycle hooks to Composition API `setup()` hooks?](#q8-how-do-you-map-options-api-lifecycle-hooks-to-composition-api-setup-hooks) <span class="intermediate">Intermediate</span>
9. [How do you avoid Prop Drilling using Provide/Inject?](#q9-how-do-you-avoid-prop-drilling-using-provideinject) <span class="intermediate">Intermediate</span>
10. [How do you create a Custom Directive to handle outside clicks?](#q10-how-do-you-create-a-custom-directive-to-handle-outside-clicks) <span class="intermediate">Intermediate</span>
11. [How do you optimize performance for a component that renders static content (never changes)?](#q11-how-do-you-optimize-performance-for-a-component-that-renders-static-content-never-changes) <span class="intermediate">Intermediate</span>
12. [How do you handle asynchronous component loading (Lazy Loading) in Vue Router?](#q12-how-do-you-handle-asynchronous-component-loading-lazy-loading-in-vue-router) <span class="intermediate">Intermediate</span>
13. [How do you implement two-way binding manually using `v-model` on a custom component?](#q13-how-do-you-implement-two-way-binding-manually-using-v-model-on-a-custom-component) <span class="intermediate">Intermediate</span>
14. [How would you implement a 'Suspense' feature to handle async dependencies?](#q14-how-would-you-implement-a-suspense-feature-to-handle-async-dependencies) <span class="intermediate">Intermediate</span>
15. [Why is mutating a prop directly in a child component an anti-pattern?](#q15-why-is-mutating-a-prop-directly-in-a-child-component-an-anti-pattern) <span class="intermediate">Intermediate</span>
16. [How do you use `v-memo` to skip unnecessary updates?](#q16-how-do-you-use-v-memo-to-skip-unnecessary-updates) <span class="advanced">Advanced</span>
17. [How do you implement a scoped slot to pass data from child to parent?](#q17-how-do-you-implement-a-scoped-slot-to-pass-data-from-child-to-parent) <span class="intermediate">Intermediate</span>
18. [How do you use `Teleport` to render a modal outside the app root?](#q18-how-do-you-use-teleport-to-render-a-modal-outside-the-app-root) <span class="intermediate">Intermediate</span>
19. [How do you use `KeepAlive` to cache component instances?](#q19-how-do-you-use-keepalive-to-cache-component-instances) <span class="intermediate">Intermediate</span>
20. [How do you use `v-once` for static content optimization?](#q20-how-do-you-use-v-once-for-static-content-optimization) <span class="beginner">Beginner</span>
21. [How do you implement global state management using Pinia?](#q21-how-do-you-implement-global-state-management-using-pinia) <span class="intermediate">Intermediate</span>
22. [How do you access a Pinia store inside a component?](#q22-how-do-you-access-a-pinia-store-inside-a-component) <span class="intermediate">Intermediate</span>
23. [How do you implement a navigation guard in Vue Router?](#q23-how-do-you-implement-a-navigation-guard-in-vue-router) <span class="intermediate">Intermediate</span>
24. [How do you use `watchEffect` vs `watch`?](#q24-how-do-you-use-watcheffect-vs-watch) <span class="intermediate">Intermediate</span>
25. [How do you handle errors in Vue 3 using `onErrorCaptured`?](#q25-how-do-you-handle-errors-in-vue-3-using-onerrorcaptured) <span class="advanced">Advanced</span>
26. [How do you use `defineAsyncComponent` for lazy loading?](#q26-how-do-you-use-defineasynccomponent-for-lazy-loading) <span class="intermediate">Intermediate</span>
27. [How do you implement a custom v-model modifier?](#q27-how-do-you-implement-a-custom-v-model-modifier) <span class="advanced">Advanced</span>
28. [How do you test a Vue component using Vue Test Utils?](#q28-how-do-you-test-a-vue-component-using-vue-test-utils) <span class="intermediate">Intermediate</span>
29. [How do you use `provide` and `inject` for dependency injection?](#q29-how-do-you-use-provide-and-inject-for-dependency-injection) <span class="intermediate">Intermediate</span>
30. [How do you use `shallowRef` vs `ref` for performance?](#q30-how-do-you-use-shallowref-vs-ref-for-performance) <span class="advanced">Advanced</span>
31. [How do you use `toRef` and `toRefs` to maintain reactivity?](#q31-how-do-you-use-toref-and-torefs-to-maintain-reactivity) <span class="intermediate">Intermediate</span>
32. [How do you handle multiple root nodes in Vue 3 (Fragments)?](#q32-how-do-you-handle-multiple-root-nodes-in-vue-3-fragments) <span class="beginner">Beginner</span>
33. [How do you use `Suspense` for async components?](#q33-how-do-you-use-suspense-for-async-components) <span class="advanced">Advanced</span>
34. [How do you optimize list rendering with `v-for` and `key`?](#q34-how-do-you-optimize-list-rendering-with-v-for-and-key) <span class="beginner">Beginner</span>
35. [How do you use `style scoped` with `v-html` content (deep selector)?](#q35-how-do-you-use-style-scoped-with-v-html-content-deep-selector) <span class="intermediate">Intermediate</span>
36. [How do you use dynamic arguments for directives?](#q36-how-do-you-use-dynamic-arguments-for-directives) <span class="intermediate">Intermediate</span>
37. [How do you create a Global Property in Vue 3?](#q37-how-do-you-create-a-global-property-in-vue-3) <span class="intermediate">Intermediate</span>
38. [How do you force a component to re-render correctly?](#q38-how-do-you-force-a-component-to-re-render-correctly) <span class="intermediate">Intermediate</span>
39. [How do you create a generic component with Props (TypeScript)?](#q39-how-do-you-create-a-generic-component-with-props-typescript) <span class="advanced">Advanced</span>
40. [How do you implement a composable that manages Event Listeners safely?](#q40-how-do-you-implement-a-composable-that-manages-event-listeners-safely) <span class="intermediate">Intermediate</span>
41. [How do you expose methods/state to a parent component using `defineExpose`?](#q41-how-do-you-expose-methodsstate-to-a-parent-component-using-defineexpose) <span class="intermediate">Intermediate</span>
42. [How do you animate element entry/leave using `<Transition>`?](#q42-how-do-you-animate-element-entryleave-using-<transition>) <span class="beginner">Beginner</span>
43. [How do you access Slots and Attributes in `<script setup>`?](#q43-how-do-you-access-slots-and-attributes-in-<script-setup>) <span class="intermediate">Intermediate</span>
44. [How do you simplify `v-model` implementation using `defineModel` (Vue 3.4+)?](#q44-how-do-you-simplify-v-model-implementation-using-definemodel-vue-3.4+) <span class="intermediate">Intermediate</span>
45. [How do you normalize refs, getters, or values using `toValue` (Vue 3.3+)?](#q45-how-do-you-normalize-refs-getters-or-values-using-tovalue-vue-3.3+) <span class="advanced">Advanced</span>
46. [How do you fetch data on the server before rendering (SSR) using `serverPrefetch`?](#q46-how-do-you-fetch-data-on-the-server-before-rendering-ssr-using-serverprefetch) <span class="advanced">Advanced</span>
47. [How do you set component options (like `name`) in `<script setup>` using `defineOptions`?](#q47-how-do-you-set-component-options-like-name-in-<script-setup>-using-defineoptions) <span class="beginner">Beginner</span>
48. [How do you create a debounced ref using `customRef`?](#q48-how-do-you-create-a-debounced-ref-using-customref) <span class="advanced">Advanced</span>
49. [How do you create a Web Component using Vue (`defineCustomElement`)?](#q49-how-do-you-create-a-web-component-using-vue-definecustomelement) <span class="advanced">Advanced</span>
50. [How do you handle Global Errors in a Vue App?](#q50-how-do-you-handle-global-errors-in-a-vue-app) <span class="intermediate">Intermediate</span>
51. [How do you handle Vue.js state management in large scale applications?](#q51-how-do-you-handle-vue.js-state-management-in-large-scale-applications) <span class="advanced">Advanced</span>
52. [How do you perform Vue.js data validation in microservices?](#q52-how-do-you-perform-vue.js-data-validation-in-microservices) <span class="beginner">Beginner</span>
53. [How do you automate Vue.js deployment for mobile devices?](#q53-how-do-you-automate-vue.js-deployment-for-mobile-devices) <span class="advanced">Advanced</span>
54. [How do you handle Vue.js concurrency issues in legacy systems?](#q54-how-do-you-handle-vue.js-concurrency-issues-in-legacy-systems) <span class="advanced">Advanced</span>
55. [How do you implement Vue.js caching in cloud infrastructure?](#q55-how-do-you-implement-vue.js-caching-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
56. [How do you manage Vue.js configuration for real-time systems?](#q56-how-do-you-manage-vue.js-configuration-for-real-time-systems) <span class="beginner">Beginner</span>
57. [How do you handle Vue.js internationalization (i18n) in distributed systems?](#q57-how-do-you-handle-vue.js-internationalization-i18n-in-distributed-systems) <span class="intermediate">Intermediate</span>
58. [How do you ensure Vue.js accessibility (a11y) in high-traffic sites?](#q58-how-do-you-ensure-vue.js-accessibility-a11y-in-high-traffic-sites) <span class="beginner">Beginner</span>
59. [How do you optimize Vue.js network requests in embedded systems?](#q59-how-do-you-optimize-vue.js-network-requests-in-embedded-systems) <span class="advanced">Advanced</span>
60. [How do you handle Vue.js performance optimization for production environments?](#q60-how-do-you-handle-vue.js-performance-optimization-for-production-environments) <span class="advanced">Advanced</span>
61. [What are the security implications of Vue.js in large scale applications?](#q61-what-are-the-security-implications-of-vue.js-in-large-scale-applications) <span class="intermediate">Intermediate</span>
62. [How do you debug Vue.js memory leaks in microservices?](#q62-how-do-you-debug-vue.js-memory-leaks-in-microservices) <span class="advanced">Advanced</span>
63. [Best practices for Vue.js code organization in mobile devices?](#q63-best-practices-for-vue.js-code-organization-in-mobile-devices) <span class="beginner">Beginner</span>
64. [How do you implement Vue.js error handling for legacy systems?](#q64-how-do-you-implement-vue.js-error-handling-for-legacy-systems) <span class="intermediate">Intermediate</span>
65. [How do you test Vue.js functionality in cloud infrastructure?](#q65-how-do-you-test-vue.js-functionality-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
66. [How do you handle Vue.js state management in real-time systems?](#q66-how-do-you-handle-vue.js-state-management-in-real-time-systems) <span class="advanced">Advanced</span>
67. [How do you perform Vue.js data validation in distributed systems?](#q67-how-do-you-perform-vue.js-data-validation-in-distributed-systems) <span class="beginner">Beginner</span>
68. [How do you automate Vue.js deployment for high-traffic sites?](#q68-how-do-you-automate-vue.js-deployment-for-high-traffic-sites) <span class="advanced">Advanced</span>
69. [How do you handle Vue.js concurrency issues in embedded systems?](#q69-how-do-you-handle-vue.js-concurrency-issues-in-embedded-systems) <span class="advanced">Advanced</span>
70. [How do you implement Vue.js caching in production environments?](#q70-how-do-you-implement-vue.js-caching-in-production-environments) <span class="intermediate">Intermediate</span>
71. [How do you manage Vue.js configuration for large scale applications?](#q71-how-do-you-manage-vue.js-configuration-for-large-scale-applications) <span class="beginner">Beginner</span>
72. [How do you handle Vue.js internationalization (i18n) in microservices?](#q72-how-do-you-handle-vue.js-internationalization-i18n-in-microservices) <span class="intermediate">Intermediate</span>
73. [How do you ensure Vue.js accessibility (a11y) in mobile devices?](#q73-how-do-you-ensure-vue.js-accessibility-a11y-in-mobile-devices) <span class="beginner">Beginner</span>
74. [How do you optimize Vue.js network requests in legacy systems?](#q74-how-do-you-optimize-vue.js-network-requests-in-legacy-systems) <span class="advanced">Advanced</span>
75. [How do you handle Vue.js performance optimization for cloud infrastructure?](#q75-how-do-you-handle-vue.js-performance-optimization-for-cloud-infrastructure) <span class="advanced">Advanced</span>
76. [What are the security implications of Vue.js in real-time systems?](#q76-what-are-the-security-implications-of-vue.js-in-real-time-systems) <span class="intermediate">Intermediate</span>
77. [How do you debug Vue.js memory leaks in distributed systems?](#q77-how-do-you-debug-vue.js-memory-leaks-in-distributed-systems) <span class="advanced">Advanced</span>
78. [Best practices for Vue.js code organization in high-traffic sites?](#q78-best-practices-for-vue.js-code-organization-in-high-traffic-sites) <span class="beginner">Beginner</span>
79. [How do you implement Vue.js error handling for embedded systems?](#q79-how-do-you-implement-vue.js-error-handling-for-embedded-systems) <span class="intermediate">Intermediate</span>
80. [How do you test Vue.js functionality in production environments?](#q80-how-do-you-test-vue.js-functionality-in-production-environments) <span class="intermediate">Intermediate</span>
81. [How do you handle Vue.js state management in large scale applications?](#q81-how-do-you-handle-vue.js-state-management-in-large-scale-applications) <span class="advanced">Advanced</span>
82. [How do you perform Vue.js data validation in microservices?](#q82-how-do-you-perform-vue.js-data-validation-in-microservices) <span class="beginner">Beginner</span>
83. [How do you automate Vue.js deployment for mobile devices?](#q83-how-do-you-automate-vue.js-deployment-for-mobile-devices) <span class="advanced">Advanced</span>
84. [How do you handle Vue.js concurrency issues in legacy systems?](#q84-how-do-you-handle-vue.js-concurrency-issues-in-legacy-systems) <span class="advanced">Advanced</span>
85. [How do you implement Vue.js caching in cloud infrastructure?](#q85-how-do-you-implement-vue.js-caching-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
86. [How do you manage Vue.js configuration for real-time systems?](#q86-how-do-you-manage-vue.js-configuration-for-real-time-systems) <span class="beginner">Beginner</span>
87. [How do you handle Vue.js internationalization (i18n) in distributed systems?](#q87-how-do-you-handle-vue.js-internationalization-i18n-in-distributed-systems) <span class="intermediate">Intermediate</span>
88. [How do you ensure Vue.js accessibility (a11y) in high-traffic sites?](#q88-how-do-you-ensure-vue.js-accessibility-a11y-in-high-traffic-sites) <span class="beginner">Beginner</span>
89. [How do you optimize Vue.js network requests in embedded systems?](#q89-how-do-you-optimize-vue.js-network-requests-in-embedded-systems) <span class="advanced">Advanced</span>
90. [How do you handle Vue.js performance optimization for production environments?](#q90-how-do-you-handle-vue.js-performance-optimization-for-production-environments) <span class="advanced">Advanced</span>
91. [What are the security implications of Vue.js in large scale applications?](#q91-what-are-the-security-implications-of-vue.js-in-large-scale-applications) <span class="intermediate">Intermediate</span>
92. [How do you debug Vue.js memory leaks in microservices?](#q92-how-do-you-debug-vue.js-memory-leaks-in-microservices) <span class="advanced">Advanced</span>
93. [Best practices for Vue.js code organization in mobile devices?](#q93-best-practices-for-vue.js-code-organization-in-mobile-devices) <span class="beginner">Beginner</span>
94. [How do you implement Vue.js error handling for legacy systems?](#q94-how-do-you-implement-vue.js-error-handling-for-legacy-systems) <span class="intermediate">Intermediate</span>
95. [How do you test Vue.js functionality in cloud infrastructure?](#q95-how-do-you-test-vue.js-functionality-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
96. [How do you handle Vue.js state management in real-time systems?](#q96-how-do-you-handle-vue.js-state-management-in-real-time-systems) <span class="advanced">Advanced</span>
97. [How do you perform Vue.js data validation in distributed systems?](#q97-how-do-you-perform-vue.js-data-validation-in-distributed-systems) <span class="beginner">Beginner</span>
98. [How do you automate Vue.js deployment for high-traffic sites?](#q98-how-do-you-automate-vue.js-deployment-for-high-traffic-sites) <span class="advanced">Advanced</span>
99. [How do you handle Vue.js concurrency issues in embedded systems?](#q99-how-do-you-handle-vue.js-concurrency-issues-in-embedded-systems) <span class="advanced">Advanced</span>
100. [How do you implement Vue.js caching in production environments?](#q100-how-do-you-implement-vue.js-caching-in-production-environments) <span class="intermediate">Intermediate</span>

---

### Q1: You are migrating a Vue 2 app to Vue 3. You notice that reactivity is not working for a new property added to an object. Why does this happen in Vue 2 but works in Vue 3?

**Difficulty**: Intermediate

**Strategy:**
**Vue 2 (Object.defineProperty):**
Vue 2 converts properties to getters/setters on initialization. It **cannot detect** property addition or deletion.
*   `obj.newProp = 123` -> Not reactive.
*   Fix: `Vue.set(obj, 'newProp', 123)`.

**Vue 3 (Proxy):**
Vue 3 wraps the object in a JavaScript Proxy. The proxy intercepts *all* operations, including adding new properties.
*   `obj.newProp = 123` -> **Is reactive**.
*   No need for `Vue.set`.

**Code Example:**
```javascript
// Vue 2
data() { return { obj: {} } }
mounted() {
  this.obj.newProp = 123 // ❌ Not reactive
  this.$set(this.obj, 'newProp', 123) // ✅ Reactive
}

// Vue 3
const state = reactive({})
state.newProp = 123 // ✅ Reactive (Proxy intercepts set)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q2: When using the Composition API, should you use `ref` or `reactive` for declaring state? What are the trade-offs?

**Difficulty**: Intermediate

**Strategy:**
**`ref`:**
*   **Usage:** `const count = ref(0)`. Access via `count.value`.
*   **Pros:** Works for primitives (string, number) AND objects. Easy to replace the whole object (`obj.value = newObj`).
*   **Cons:** Requires `.value` everywhere in JS (but auto-unwrapped in template).

**`reactive`:**
*   **Usage:** `const state = reactive({ count: 0 })`. Access via `state.count`.
*   **Pros:** No `.value`. Feels like a normal JS object.
*   **Cons:** Only works for objects (not primitives). Destructuring breaks reactivity (`const { count } = state` -> `count` is dead).

**Recommendation:** Use `ref` by default for consistency, or `reactive` for grouped state where you don't destructure.

**Code Example:**
```javascript
import { ref, reactive, toRefs } from 'vue'

// Ref
const count = ref(0)
count.value++

// Reactive
const state = reactive({ count: 0 })
state.count++

// Destructuring reactive (loses reactivity)
const { count: dead } = state

// Fix destructuring
const { count: alive } = toRefs(state)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q3: You have a large list of items and `v-if` / `v-for` on the same element. Why is this considered a bad practice and how do you fix it?

**Difficulty**: Intermediate

**Strategy:**
In Vue 2, `v-for` has higher precedence than `v-if`. In Vue 3, `v-if` has higher precedence. Mixing them is confusing and inefficient (iterating over all items just to hide some).

**Fix:** Use a `computed` property to filter the list *before* rendering.

**Code Example:**
```html
<!-- ❌ Bad -->
<li v-for="item in items" v-if="item.isActive">{{ item.name }}</li>

<!-- ✅ Good -->
<li v-for="item in activeItems" :key="item.id">{{ item.name }}</li>

<script setup>
const activeItems = computed(() => items.value.filter(i => i.isActive))
</script>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q4: How do you share logic between components in Vue 3 using Composables?

**Difficulty**: Intermediate

**Strategy:**
Composables are functions that encapsulate stateful logic using Composition API (`ref`, `computed`, `onMounted`). They are the Vue 3 replacement for Mixins (which had naming collisions and implicit dependencies).

**Code Example:**
```javascript
// useMouse.js
import { ref, onMounted, onUnmounted } from 'vue'

export function useMouse() {
  const x = ref(0)
  const y = ref(0)

  function update(e) {
    x.value = e.pageX
    y.value = e.pageY
  }

  onMounted(() => window.addEventListener('mousemove', update))
  onUnmounted(() => window.removeEventListener('mousemove', update))

  return { x, y }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q5: You need to render a modal that is visually separate from the main app layout (e.g., outside `overflow: hidden` containers). How do you achieve this in Vue 3?

**Difficulty**: Intermediate

**Strategy:**
`<Teleport>` allows you to render a component's template part into a DOM node that exists outside the component hierarchy of the Vue app.

**Code Example:**
```html
<template>
  <button @click="open = true">Open Modal</button>

  <Teleport to="body">
    <div v-if="open" class="modal">
      <p>I am attached to the body tag!</p>
      <button @click="open = false">Close</button>
    </div>
  </Teleport>
</template>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q6: How do you ensure the DOM has updated before performing an action using `nextTick`?

**Difficulty**: Intermediate

**Strategy:**
Vue updates the DOM asynchronously. When you change data, the DOM is not updated immediately. `nextTick` waits for the next DOM update cycle.

**Code Example:**
```javascript
import { nextTick } from 'vue'

async function updateAndFocus() {
  inputValue.value = 'New Value'
  
  // DOM not updated yet
  
  await nextTick()
  
  // DOM is now updated
  document.getElementById('myInput').focus()
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q7: How do you scope styles to a component effectively using CSS Modules vs Scoped Styles?

**Difficulty**: Intermediate

**Strategy:**
**Scoped Styles (`<style scoped>`):**
Vue adds a unique attribute (e.g., `data-v-f3f3eg9`) to elements and selectors.
*   **Pros:** Easy, zero config.
*   **Cons:** Deep selectors (`::v-deep`) needed for child components.

**CSS Modules (`<style module>`):**
Classes are compiled to unique names (e.g., `.red` -> `._red_12345`).
*   **Pros:** Explicit usage in template (`$style.red`), prevents collisions completely.
*   **Cons:** Slightly more verbose template syntax.

**Code Example:**
```html
<template>
  <p :class="$style.red">This is red</p>
</template>

<style module>
.red {
  color: red;
}
</style>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q8: How do you map Options API lifecycle hooks to Composition API `setup()` hooks?

**Difficulty**: Intermediate

**Strategy:**
In `setup()`, lifecycle hooks are imported functions.

*   `beforeCreate` / `created` -> Not needed (just write code in `setup()`).
*   `beforeMount` -> `onBeforeMount`
*   `mounted` -> `onMounted`
*   `beforeUpdate` -> `onBeforeUpdate`
*   `updated` -> `onUpdated`
*   `beforeDestroy` -> `onBeforeUnmount`
*   `destroyed` -> `onUnmounted`
*   `errorCaptured` -> `onErrorCaptured`

**Code Example:**
```javascript
import { onMounted } from 'vue'

setup() {
  onMounted(() => {
    console.log('Component is mounted!')
  })
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q9: How do you avoid Prop Drilling using Provide/Inject?

**Difficulty**: Intermediate

**Strategy:**
Prop drilling occurs when you pass data through multiple layers of components that don't need it. `provide`/`inject` allows a parent to pass data to *any* descendant.

**Code Example:**
```javascript
// Parent (Provider)
import { provide, ref } from 'vue'
setup() {
  const theme = ref('dark')
  provide('theme', theme)
}

// Deep Child (Injector)
import { inject } from 'vue'
setup() {
  const theme = inject('theme', 'light') // 'light' is default
  return { theme }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q10: How do you create a Custom Directive to handle outside clicks?

**Difficulty**: Intermediate

**Strategy:**
Custom directives allow low-level DOM access.

**Code Example:**
```javascript
// v-click-outside directive
const clickOutside = {
  mounted(el, binding) {
    el.clickOutsideEvent = (event) => {
      if (!(el == event.target || el.contains(event.target))) {
        binding.value(event); // Call the provided method
      }
    };
    document.body.addEventListener('click', el.clickOutsideEvent);
  },
  unmounted(el) {
    document.body.removeEventListener('click', el.clickOutsideEvent);
  },
};

// Usage
<div v-click-outside="closeModal">...</div>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q11: How do you optimize performance for a component that renders static content (never changes)?

**Difficulty**: Intermediate

**Strategy:**
Use `v-once` or `v-memo`.

1.  **`v-once`:** Renders the element/component once and treats it as static content for future updates.
    javascript

**Code Example:**
```javascript
2.  **`v-memo` (Vue 3.2+):** Memoize a sub-tree based on dependency array (like React's `useMemo` but for templates).
    ```html
    <div v-memo="[item.id, item.selected]">
      ...complex markup...
    </div>
    ```

**Code Example:**
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q12: How do you handle asynchronous component loading (Lazy Loading) in Vue Router?

**Difficulty**: Intermediate

**Strategy:**
Lazy loading splits the bundle so components are loaded only when the route is visited.

**Code Example:**
```javascript
// router/index.js
const routes = [
  {
    path: '/about',
    name: 'About',
    // Dynamic import
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q13: How do you implement two-way binding manually using `v-model` on a custom component?

**Difficulty**: Intermediate

**Strategy:**
In Vue 3, `v-model` defaults to the `modelValue` prop and `update:modelValue` event.

**Code Example:**
```html
<!-- ChildComponent.vue -->
<template>
  <input 
    :value="modelValue"
    @input="$emit('update:modelValue', $event.target.value)"
  >
</template>

<script setup>
defineProps(['modelValue'])
defineEmits(['update:modelValue'])
</script>

<!-- Parent -->
<ChildComponent v-model="searchText" />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q14: How would you implement a 'Suspense' feature to handle async dependencies?

**Difficulty**: Intermediate

**Strategy:**
`<Suspense>` is an experimental feature (stable in Nuxt 3) that orchestrates async dependencies (like `await` in `setup`).

**Code Example:**
```javascript
<Suspense>
  <!-- Component with async setup() -->
  <template #default>
    <AsyncUserProfile />
  </template>

  <!-- Loading state -->
  <template #fallback>
    <div>Loading Profile...</div>
  </template>
</Suspense>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q15: Why is mutating a prop directly in a child component an anti-pattern?

**Difficulty**: Intermediate

**Strategy:**
Props are **read-only** (one-way data flow).
If a child mutates a prop, the change will be overwritten when the parent re-renders, causing bugs.

**Correct Way:** Emit an event to the parent to update the source of truth.

**Code Example:**
```javascript
// Bad
props.count++

// Good
emit('update:count', props.count + 1)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q16: How do you use `v-memo` to skip unnecessary updates?

**Difficulty**: Advanced

**Strategy:**
`v-memo` is a directive used to memoize a sub-tree of the template. The element and its children will only be re-rendered if one of the values in the dependency array changes. This is useful for optimizing large lists or heavy render trees.

**Code Example:**
```html
<template>
  <div v-for="item in list" :key="item.id" v-memo="[item.id === selectedId]">
    <p>ID: {{ item.id }} - Selected: {{ item.id === selectedId }}</p>
    <!-- Heavy rendering logic here -->
  </div>
</template>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q17: How do you implement a scoped slot to pass data from child to parent?

**Difficulty**: Intermediate

**Strategy:**
Scoped slots allow a child component to expose data to the parent's slot content. In the child, use `<slot :data="someData">`. In the parent, use `v-slot="slotProps"` (or `#default="{ data }"`) to access it.

**Code Example:**
```html
<!-- Child.vue -->
<template>
  <ul>
    <li v-for="item in items" :key="item.id">
      <!-- Expose 'item' to the parent -->
      <slot :item="item">{{ item.defaultText }}</slot>
    </li>
  </ul>
</template>

<!-- Parent.vue -->
<template>
  <Child :items="[1, 2, 3]">
    <template #default="{ item }">
      <span class="custom">Item {{ item }}</span>
    </template>
  </Child>
</template>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q18: How do you use `Teleport` to render a modal outside the app root?

**Difficulty**: Intermediate

**Strategy:**
`<Teleport>` allows you to render a component's template logic in a different part of the DOM (e.g., `body`), which is useful for modals, tooltips, and popovers to avoid z-index and overflow issues.

**Code Example:**
```html
<template>
  <button @click="open = true">Open Modal</button>

  <Teleport to="body">
    <div v-if="open" class="modal">
      <p>I am in the body!</p>
      <button @click="open = false">Close</button>
    </div>
  </Teleport>
</template>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q19: How do you use `KeepAlive` to cache component instances?

**Difficulty**: Intermediate

**Strategy:**
Wrap dynamic components with `<KeepAlive>` to cache their state when they are inactive, preventing re-rendering and preserving user input (e.g., form data, scroll position).

**Code Example:**
```html
<template>
  <KeepAlive include="UserProfile">
    <component :is="currentComponent" />
  </KeepAlive>
</template>

<script setup>
import UserProfile from './UserProfile.vue'
import Settings from './Settings.vue'
// UserProfile will be cached, Settings will not (unless included)
</script>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q20: How do you use `v-once` for static content optimization?

**Difficulty**: Beginner

**Strategy:**
`v-once` renders the element and component once and skips future updates. This is useful for static content that never changes, saving re-render costs.

**Code Example:**
```html
<template>
  <div>
    <h1>Dynamic: {{ title }}</h1>
    <div v-once>
      <h2>Static Section</h2>
      <p>This content will never update: {{ title }}</p>
    </div>
  </div>
</template>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q21: How do you implement global state management using Pinia?

**Difficulty**: Intermediate

**Strategy:**
Pinia is the recommended state management library for Vue 3. Define a store using `defineStore`, which returns a composable hook.

**Code Example:**
```javascript
// stores/counter.js
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)
  const doubleCount = computed(() => count.value * 2)
  function increment() {
    count.value++
  }

  return { count, doubleCount, increment }
})
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q22: How do you access a Pinia store inside a component?

**Difficulty**: Intermediate

**Strategy:**
Import the store hook and call it inside `setup()`. You can destruct state/getters using `storeToRefs` to maintain reactivity.

**Code Example:**
```html
<script setup>
import { useCounterStore } from '@/stores/counter'
import { storeToRefs } from 'pinia'

const store = useCounterStore()
// Use actions directly
const { increment } = store
// Use state/getters with storeToRefs to keep reactivity
const { count, doubleCount } = storeToRefs(store)
</script>

<template>
  <button @click="increment">Count: {{ count }}</button>
</template>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q23: How do you implement a navigation guard in Vue Router?

**Difficulty**: Intermediate

**Strategy:**
Use `beforeEach` globally or `beforeEnter` per-route to protect routes (e.g., authentication). Return `true`, `false`, or a route location.

**Code Example:**
```javascript
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({ ... })

router.beforeEach((to, from) => {
  if (to.meta.requiresAuth && !isAuthenticated()) {
    // Redirect to login
    return { name: 'Login' }
  }
  // Continue
  return true
})
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q24: How do you use `watchEffect` vs `watch`?

**Difficulty**: Intermediate

**Strategy:**
`watch` requires explicit sources and allows access to previous values. `watchEffect` automatically tracks dependencies used inside it and runs immediately.

**Code Example:**
```javascript
import { ref, watch, watchEffect } from 'vue'

const count = ref(0)

// Watch: Lazy (unless immediate: true), explicit source
watch(count, (newVal, oldVal) => {
  console.log(`Count changed: ${oldVal} -> ${newVal}`)
})

// WatchEffect: Immediate, implicit dependency tracking
watchEffect(() => {
  console.log(`Current count is: ${count.value}`)
})
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q25: How do you handle errors in Vue 3 using `onErrorCaptured`?

**Difficulty**: Advanced

**Strategy:**
`onErrorCaptured` hook captures errors from descendant components. It can return `false` to stop propagation to global `app.config.errorHandler`.

**Code Example:**
```html
<script setup>
import { onErrorCaptured } from 'vue'

onErrorCaptured((err, instance, info) => {
  console.error('Captured error:', err)
  console.log('Component:', instance)
  console.log('Info:', info)
  
  // Prevent propagation
  return false
})
</script>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q26: How do you use `defineAsyncComponent` for lazy loading?

**Difficulty**: Intermediate

**Strategy:**
Use `defineAsyncComponent` to load components only when they are needed (e.g., rendered). This reduces the initial bundle size.

**Code Example:**
```javascript
import { defineAsyncComponent } from 'vue'

const AsyncComp = defineAsyncComponent(() =>
  import('./components/MyComponent.vue')
)

// Usage in template is identical to normal components
// <AsyncComp />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q27: How do you implement a custom v-model modifier?

**Difficulty**: Advanced

**Strategy:**
Modifiers added to `v-model` (e.g., `v-model.capitalize`) are passed via the `modelModifiers` prop.

**Code Example:**
```html
<!-- Parent -->
<MyInput v-model.capitalize="myText" />

<!-- Child (MyInput.vue) -->
<script setup>
const props = defineProps({
  modelValue: String,
  modelModifiers: { default: () => ({}) }
})
const emit = defineEmits(['update:modelValue'])

function emitValue(e) {
  let value = e.target.value
  if (props.modelModifiers.capitalize) {
    value = value.charAt(0).toUpperCase() + value.slice(1)
  }
  emit('update:modelValue', value)
}
</script>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q28: How do you test a Vue component using Vue Test Utils?

**Difficulty**: Intermediate

**Strategy:**
Use `mount` to render the component and assertion libraries (like Vitest/Jest) to check output, events, or state.

**Code Example:**
```javascript
import { mount } from '@vue/test-utils'
import Counter from './Counter.vue'

test('increments value on click', async () => {
  const wrapper = mount(Counter)
  
  expect(wrapper.text()).toContain('Count: 0')
  
  await wrapper.find('button').trigger('click')
  
  expect(wrapper.text()).toContain('Count: 1')
})
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q29: How do you use `provide` and `inject` for dependency injection?

**Difficulty**: Intermediate

**Strategy:**
`provide` allows an ancestor to provide data/methods, and `inject` allows descendants to consume it, bypassing intermediate components (avoiding prop drilling).

**Code Example:**
```html
<!-- Ancestor -->
<script setup>
import { provide, ref } from 'vue'
const theme = ref('dark')
provide('theme', theme)
</script>

<!-- Descendant (Deeply nested) -->
<script setup>
import { inject } from 'vue'
const theme = inject('theme', 'light') // 'light' is default
</script>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q30: How do you use `shallowRef` vs `ref` for performance?

**Difficulty**: Advanced

**Strategy:**
`ref` makes deep objects reactive. `shallowRef` only tracks the `.value` change, not nested property changes. Use `shallowRef` for large objects where deep reactivity is unnecessary.

**Code Example:**
```javascript
import { shallowRef, triggerRef } from 'vue'

const state = shallowRef({ nested: { count: 0 } })

// This WON'T trigger updates
state.value.nested.count++

// This WILL trigger updates
state.value = { nested: { count: 1 } }

// Or force update manually
triggerRef(state)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q31: How do you use `toRef` and `toRefs` to maintain reactivity?

**Difficulty**: Intermediate

**Strategy:**
Destructuring a reactive object loses reactivity. Use `toRefs` to convert all properties to refs, or `toRef` for a single property.

**Code Example:**
```javascript
import { reactive, toRefs } from 'vue'

const state = reactive({ foo: 1, bar: 2 })

// Bad (loses reactivity):
// const { foo, bar } = state

// Good:
const { foo, bar } = toRefs(state)

foo.value++ // Updates state.foo
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q32: How do you handle multiple root nodes in Vue 3 (Fragments)?

**Difficulty**: Beginner

**Strategy:**
Vue 3 supports multi-root components (Fragments). However, if you pass attributes (like class/style) to the component, you must explicitly bind them using `$attrs` if there are multiple roots.

**Code Example:**
```html
<!-- MyComponent.vue -->
<template>
  <header>Header</header>
  <main v-bind="$attrs">Main Content</main>
  <footer>Footer</footer>
</template>

<!-- Usage -->
<MyComponent class="layout-class" /> 
<!-- 'layout-class' is applied to <main> -->
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q33: How do you use `Suspense` for async components?

**Difficulty**: Advanced

**Strategy:**
`<Suspense>` orchestrates async dependencies (async `setup()`, async components). It has `#default` and `#fallback` slots.

**Code Example:**
```html
<template>
  <Suspense>
    <!-- Component with async setup() -->
    <template #default>
      <AsyncUserList />
    </template>

    <!-- Loading state -->
    <template #fallback>
      <div>Loading users...</div>
    </template>
  </Suspense>
</template>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q34: How do you optimize list rendering with `v-for` and `key`?

**Difficulty**: Beginner

**Strategy:**
Always provide a unique `key` attribute (like an ID) when using `v-for`. This allows Vue to track node identity and optimize DOM updates (reordering instead of recreating).

**Code Example:**
```javascript
<!-- BAD: using index as key (issues with reordering/deletion) -->
<div v-for="(item, index) in items" :key="index">...</div>

<!-- GOOD: using unique ID -->
<div v-for="item in items" :key="item.id">...</div>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q35: How do you use `style scoped` with `v-html` content (deep selector)?

**Difficulty**: Intermediate

**Strategy:**
Scoped styles don't apply to `v-html` content because it's dynamically injected. Use the deep selector `:deep()` (or `::v-deep`) to target them.

**Code Example:**
```html
<template>
  <div class="content" v-html="htmlContent"></div>
</template>

<style scoped>
/* Won't work for v-html content */
.content p { color: red; }

/* Works */
.content :deep(p) {
  color: red;
}
</style>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q36: How do you use dynamic arguments for directives?

**Difficulty**: Intermediate

**Strategy:**
You can use dynamic arguments in directives by wrapping the argument in square brackets `[]`. This allows you to bind to a dynamic event or attribute name.

**Code Example:**
```html
<template>
  <!-- Dynamic attribute -->
  <a v-bind:[attributeName]="url">Link</a>
  
  <!-- Dynamic event -->
  <button v-on:[eventName]="handler">Click Me</button>
</template>

<script setup>
import { ref } from 'vue'
const attributeName = ref('href')
const eventName = ref('click')
</script>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q37: How do you create a Global Property in Vue 3?

**Difficulty**: Intermediate

**Strategy:**
Use `app.config.globalProperties` to add global properties accessible in all components (Options API) or via `getCurrentInstance` (Composition API - though Provide/Inject is preferred).

**Code Example:**
```javascript
// main.js
const app = createApp(App)
app.config.globalProperties.$http = axios

// Component (Options API)
this.$http.get('/api')

// Component (Composition API)
import { getCurrentInstance } from 'vue'
const { proxy } = getCurrentInstance()
proxy.$http.get('/api')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q38: How do you force a component to re-render correctly?

**Difficulty**: Intermediate

**Strategy:**
The best way to force a re-render is to change the `key` prop of the component. Avoid using `v-if` hacks or `forceUpdate`.

**Code Example:**
```html
<template>
  <ComplexComponent :key="componentKey" />
  <button @click="reload">Reload</button>
</template>

<script setup>
import { ref } from 'vue'
const componentKey = ref(0)

function reload() {
  componentKey.value++
}
</script>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q39: How do you create a generic component with Props (TypeScript)?

**Difficulty**: Advanced

**Strategy:**
In `<script setup lang="ts">`, use `defineProps<Props>()` with a generic type parameter. Vue 3.3+ supports `<script setup generic="T">`.

**Code Example:**
```html
<script setup lang="ts" generic="T">
defineProps<{
  items: T[]
  selected: T
}>()
</script>

<template>
  <ul>
    <li v-for="item in items">{{ item }}</li>
  </ul>
</template>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q40: How do you implement a composable that manages Event Listeners safely?

**Difficulty**: Intermediate

**Strategy:**
Register the event listener in `onMounted` and remove it in `onUnmounted` to prevent memory leaks. Returns a composable function.

**Code Example:**
```javascript
import { onMounted, onUnmounted } from 'vue'

export function useEventListener(target, event, callback) {
  onMounted(() => target.addEventListener(event, callback))
  onUnmounted(() => target.removeEventListener(event, callback))
}

// Usage
useEventListener(window, 'resize', handleResize)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---


### Q41: How do you expose methods/state to a parent component using `defineExpose`?

**Difficulty**: Intermediate

**Strategy:**
By default, `<script setup>` components are closed. Use `defineExpose` to explicitly expose properties to the parent (accessible via template ref).

**Code Example:**
<!-- Child.vue -->
<script setup>
import { ref } from 'vue'
const count = ref(0)
function reset() { count.value = 0 }

defineExpose({ count, reset })
</script>

<!-- Parent.vue -->
<script setup>
import { ref } from 'vue'
const childRef = ref(null)

function handleReset() {
  childRef.value.reset() // Works because of defineExpose
}
</script>
<template>
  <Child ref="childRef" />
</template>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q42: How do you animate element entry/leave using `<Transition>`?

**Difficulty**: Beginner

**Strategy:**
Wrap the element (v-if/v-show) in `<Transition>`. Define CSS classes like `.v-enter-active`, `.v-leave-active`.

**Code Example:**
<template>
  <button @click="show = !show">Toggle</button>
  <Transition>
    <p v-if="show">Hello</p>
  </Transition>
</template>

<style>
.v-enter-active, .v-leave-active {
  transition: opacity 0.5s ease;
}
.v-enter-from, .v-leave-to {
  opacity: 0;
}
</style>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q43: How do you access Slots and Attributes in `<script setup>`?

**Difficulty**: Intermediate

**Strategy:**
Use `useSlots()` and `useAttrs()` helpers. Note that these are rarely needed as `$slots` and `$attrs` are available in templates directly.

**Code Example:**
<script setup>
import { useSlots, useAttrs } from 'vue'

const slots = useSlots()
const attrs = useAttrs()

if (slots.default) {
  console.log('Default slot is present')
}
</script>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q44: How do you simplify `v-model` implementation using `defineModel` (Vue 3.4+)?

**Difficulty**: Intermediate

**Strategy:**
`defineModel` creates a ref that syncs with the parent's v-model automatically, removing the need for manual props/emits.

**Code Example:**
<!-- Child.vue -->
<script setup>
const model = defineModel()

function update() {
  model.value++ // Emits 'update:modelValue' automatically
}
</script>

<template>
  <input v-model="model" />
</template>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q45: How do you normalize refs, getters, or values using `toValue` (Vue 3.3+)?

**Difficulty**: Advanced

**Strategy:**
`toValue` un-nests a value, ref, or getter function into the plain value. Useful in composables that accept flexible arguments.

**Code Example:**
import { toValue } from 'vue'

function useFeature(arg) {
  const value = toValue(arg) // Works if arg is 1, ref(1), or () => 1
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q46: How do you fetch data on the server before rendering (SSR) using `serverPrefetch`?

**Difficulty**: Advanced

**Strategy:**
The `serverPrefetch` hook (Options API) or `await` in `setup()` (Composition API with Suspense) allows waiting for async data during SSR.

**Code Example:**
<!-- Composition API -->
<script setup>
const data = await fetchData() // Suspense handles this on client, SSR waits for it
</script>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q47: How do you set component options (like `name`) in `<script setup>` using `defineOptions`?

**Difficulty**: Beginner

**Strategy:**
`defineOptions` allows declaring options that cannot be expressed in `<script setup>`, such as `name`, `inheritAttrs`, or custom options.

**Code Example:**
<script setup>
defineOptions({
  name: 'MyComponent',
  inheritAttrs: false
})
</script>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q48: How do you create a debounced ref using `customRef`?

**Difficulty**: Advanced

**Strategy:**
`customRef` allows controlling the dependency tracking and update triggering of a ref. Useful for debounce or throttle.

**Code Example:**
import { customRef } from 'vue'

function useDebouncedRef(value, delay = 200) {
  let timeout
  return customRef((track, trigger) => {
    return {
      get() {
        track()
        return value
      },
      set(newValue) {
        clearTimeout(timeout)
        timeout = setTimeout(() => {
          value = newValue
          trigger()
        }, delay)
      }
    }
  })
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q49: How do you create a Web Component using Vue (`defineCustomElement`)?

**Difficulty**: Advanced

**Strategy:**
Use `defineCustomElement` to create a native Custom Element class from a Vue component, then register it with `customElements.define`.

**Code Example:**
import { defineCustomElement } from 'vue'
import MyVueComponent from './MyVueComponent.vue'

const MyElement = defineCustomElement(MyVueComponent)
customElements.define('my-element', MyElement)

// Usage in HTML: <my-element></my-element>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q50: How do you handle Global Errors in a Vue App?

**Difficulty**: Intermediate

**Strategy:**
Assign a handler to `app.config.errorHandler`. It catches errors from all components, lifecycle hooks, and directives.

**Code Example:**
const app = createApp(App)

app.config.errorHandler = (err, instance, info) => {
  console.error('Global Error:', err)
  // Send to logging service (Sentry, etc.)
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---


### Q51: How do you handle Vue.js state management in large scale applications?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```javascript
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q52: How do you perform Vue.js data validation in microservices?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```javascript
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q53: How do you automate Vue.js deployment for mobile devices?

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

### Q54: How do you handle Vue.js concurrency issues in legacy systems?

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

### Q55: How do you implement Vue.js caching in cloud infrastructure?

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

### Q56: How do you manage Vue.js configuration for real-time systems?

**Difficulty**: Beginner

**Strategy**:
Use environment variables or config files. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const config = process.env.CONFIG || 'default';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q57: How do you handle Vue.js internationalization (i18n) in distributed systems?

**Difficulty**: Intermediate

**Strategy**:
Use i18n libraries. Extract strings to resource files.

**Code Example**:
```javascript
t('welcome_message')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q58: How do you ensure Vue.js accessibility (a11y) in high-traffic sites?

**Difficulty**: Beginner

**Strategy**:
Use semantic HTML and ARIA roles. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
<button aria-label="Close">X</button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q59: How do you optimize Vue.js network requests in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use batching, debouncing, or GraphQL. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
debounce(() => fetch(), 300);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q60: How do you handle Vue.js performance optimization for production environments?

**Difficulty**: Advanced

**Strategy**:
Profile first, then optimize hot paths. Use caching and efficient algorithms.

**Code Example**:
```javascript
const start = performance.now();
// Vue.js logic
const end = performance.now();
console.log('Time:', end - start);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q61: What are the security implications of Vue.js in large scale applications?

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

### Q62: How do you debug Vue.js memory leaks in microservices?

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

### Q63: Best practices for Vue.js code organization in mobile devices?

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

### Q64: How do you implement Vue.js error handling for legacy systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```javascript
try {
  await Vue.jsOperation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q65: How do you test Vue.js functionality in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```javascript
test('Vue.js works', () => {
  expect(Vue.js()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q66: How do you handle Vue.js state management in real-time systems?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```javascript
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q67: How do you perform Vue.js data validation in distributed systems?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```javascript
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q68: How do you automate Vue.js deployment for high-traffic sites?

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

### Q69: How do you handle Vue.js concurrency issues in embedded systems?

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

### Q70: How do you implement Vue.js caching in production environments?

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

### Q71: How do you manage Vue.js configuration for large scale applications?

**Difficulty**: Beginner

**Strategy**:
Use environment variables or config files. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const config = process.env.CONFIG || 'default';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q72: How do you handle Vue.js internationalization (i18n) in microservices?

**Difficulty**: Intermediate

**Strategy**:
Use i18n libraries. Extract strings to resource files.

**Code Example**:
```javascript
t('welcome_message')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q73: How do you ensure Vue.js accessibility (a11y) in mobile devices?

**Difficulty**: Beginner

**Strategy**:
Use semantic HTML and ARIA roles. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
<button aria-label="Close">X</button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q74: How do you optimize Vue.js network requests in legacy systems?

**Difficulty**: Advanced

**Strategy**:
Use batching, debouncing, or GraphQL. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
debounce(() => fetch(), 300);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q75: How do you handle Vue.js performance optimization for cloud infrastructure?

**Difficulty**: Advanced

**Strategy**:
Profile first, then optimize hot paths. Use caching and efficient algorithms.

**Code Example**:
```javascript
const start = performance.now();
// Vue.js logic
const end = performance.now();
console.log('Time:', end - start);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q76: What are the security implications of Vue.js in real-time systems?

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

### Q77: How do you debug Vue.js memory leaks in distributed systems?

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

### Q78: Best practices for Vue.js code organization in high-traffic sites?

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

### Q79: How do you implement Vue.js error handling for embedded systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```javascript
try {
  await Vue.jsOperation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q80: How do you test Vue.js functionality in production environments?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```javascript
test('Vue.js works', () => {
  expect(Vue.js()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q81: How do you handle Vue.js state management in large scale applications?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```javascript
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q82: How do you perform Vue.js data validation in microservices?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```javascript
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q83: How do you automate Vue.js deployment for mobile devices?

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

### Q84: How do you handle Vue.js concurrency issues in legacy systems?

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

### Q85: How do you implement Vue.js caching in cloud infrastructure?

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

### Q86: How do you manage Vue.js configuration for real-time systems?

**Difficulty**: Beginner

**Strategy**:
Use environment variables or config files. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const config = process.env.CONFIG || 'default';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q87: How do you handle Vue.js internationalization (i18n) in distributed systems?

**Difficulty**: Intermediate

**Strategy**:
Use i18n libraries. Extract strings to resource files.

**Code Example**:
```javascript
t('welcome_message')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q88: How do you ensure Vue.js accessibility (a11y) in high-traffic sites?

**Difficulty**: Beginner

**Strategy**:
Use semantic HTML and ARIA roles. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
<button aria-label="Close">X</button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q89: How do you optimize Vue.js network requests in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use batching, debouncing, or GraphQL. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
debounce(() => fetch(), 300);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q90: How do you handle Vue.js performance optimization for production environments?

**Difficulty**: Advanced

**Strategy**:
Profile first, then optimize hot paths. Use caching and efficient algorithms.

**Code Example**:
```javascript
const start = performance.now();
// Vue.js logic
const end = performance.now();
console.log('Time:', end - start);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q91: What are the security implications of Vue.js in large scale applications?

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

### Q92: How do you debug Vue.js memory leaks in microservices?

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

### Q93: Best practices for Vue.js code organization in mobile devices?

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

### Q94: How do you implement Vue.js error handling for legacy systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```javascript
try {
  await Vue.jsOperation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q95: How do you test Vue.js functionality in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```javascript
test('Vue.js works', () => {
  expect(Vue.js()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q96: How do you handle Vue.js state management in real-time systems?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```javascript
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q97: How do you perform Vue.js data validation in distributed systems?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```javascript
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q98: How do you automate Vue.js deployment for high-traffic sites?

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

### Q99: How do you handle Vue.js concurrency issues in embedded systems?

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

### Q100: How do you implement Vue.js caching in production environments?

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
