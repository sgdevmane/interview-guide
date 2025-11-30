<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>Performance Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for developers</b></p>
</div>

---

## Table of Contents

1. [You have a React application with a slow initial load time due to a large bundle. How do you implement 'Route-Based Code Splitting' to fix this?](#q1-you-have-a-react-application-with-a-slow-initial-load-time-due-to-a-large-bundle.-how-do-you-implement-route-based-code-splitting-to-fix-this) <span class="beginner">Beginner</span>
2. [Your LCP (Largest Contentful Paint) score is poor because the hero image loads late. How do you use `fetchpriority` and `preload` to optimize it?](#q2-your-lcp-largest-contentful-paint-score-is-poor-because-the-hero-image-loads-late.-how-do-you-use-fetchpriority-and-preload-to-optimize-it) <span class="beginner">Beginner</span>
3. [You notice 'Layout Thrashing' in a loop where you read and write DOM properties. How do you refactor this to improve rendering performance?](#q3-you-notice-layout-thrashing-in-a-loop-where-you-read-and-write-dom-properties.-how-do-you-refactor-this-to-improve-rendering-performance) <span class="beginner">Beginner</span>
4. [How do you implement a 'Virtual List' (Windowing) in React to render 10,000 rows without crashing the browser?](#q4-how-do-you-implement-a-virtual-list-windowing-in-react-to-render-10000-rows-without-crashing-the-browser) <span class="beginner">Beginner</span>
5. [You have a heavy calculation running on the main thread that blocks UI interactions. How do you offload this to a Web Worker?](#q5-you-have-a-heavy-calculation-running-on-the-main-thread-that-blocks-ui-interactions.-how-do-you-offload-this-to-a-web-worker) <span class="beginner">Beginner</span>
6. [How do you prevent 'Cumulative Layout Shift' (CLS) caused by images loading without dimensions?](#q6-how-do-you-prevent-cumulative-layout-shift-cls-caused-by-images-loading-without-dimensions) <span class="beginner">Beginner</span>
7. [How do you use the `IntersectionObserver` API to lazy load images as they scroll into view?](#q7-how-do-you-use-the-intersectionobserver-api-to-lazy-load-images-as-they-scroll-into-view) <span class="beginner">Beginner</span>
8. [You are optimizing a search input. How do you implement a 'Debounce' function to reduce the number of API calls?](#q8-you-are-optimizing-a-search-input.-how-do-you-implement-a-debounce-function-to-reduce-the-number-of-api-calls) <span class="beginner">Beginner</span>
9. [How do you identify and fix a 'Memory Leak' caused by a detached event listener in a React component?](#q9-how-do-you-identify-and-fix-a-memory-leak-caused-by-a-detached-event-listener-in-a-react-component) <span class="beginner">Beginner</span>
10. [How do you use `requestAnimationFrame` to create smooth, 60fps animations instead of using `setInterval`?](#q10-how-do-you-use-requestanimationframe-to-create-smooth-60fps-animations-instead-of-using-setinterval) <span class="beginner">Beginner</span>
11. [How do you optimize a large React context that causes unnecessary re-renders in consumer components?](#q11-how-do-you-optimize-a-large-react-context-that-causes-unnecessary-re-renders-in-consumer-components) <span class="beginner">Beginner</span>
12. [How do you use the 'Performance API' to measure the execution time of a specific function?](#q12-how-do-you-use-the-performance-api-to-measure-the-execution-time-of-a-specific-function) <span class="beginner">Beginner</span>
13. [How do you configure Webpack to use 'Tree Shaking' to remove unused code from your production bundle?](#q13-how-do-you-configure-webpack-to-use-tree-shaking-to-remove-unused-code-from-your-production-bundle) <span class="beginner">Beginner</span>
14. [How do you implement 'Resource Hints' (dns-prefetch, preconnect) to speed up third-party API connections?](#q14-how-do-you-implement-resource-hints-dns-prefetch-preconnect-to-speed-up-third-party-api-connections) <span class="beginner">Beginner</span>
15. [How do you optimize CSS delivery to avoid 'Render Blocking' resources?](#q15-how-do-you-optimize-css-delivery-to-avoid-render-blocking-resources) <span class="beginner">Beginner</span>
16. [How do you minimize main thread work to improve INP (Interaction to Next Paint)?](#q16-how-do-you-minimize-main-thread-work-to-improve-inp-interaction-to-next-paint) <span class="expert">Expert</span>
17. [How do you optimize font loading using `font-display: swap`?](#q17-how-do-you-optimize-font-loading-using-font-display:-swap) <span class="beginner">Beginner</span>
18. [How do you prevent Layout Shifts from dynamic ads?](#q18-how-do-you-prevent-layout-shifts-from-dynamic-ads) <span class="intermediate">Intermediate</span>
19. [How do you implement a 'Cache First' strategy in a Service Worker?](#q19-how-do-you-implement-a-cache-first-strategy-in-a-service-worker) <span class="intermediate">Intermediate</span>
20. [How do you configure HTTP Cache-Control headers for immutable static assets?](#q20-how-do-you-configure-http-cache-control-headers-for-immutable-static-assets) <span class="intermediate">Intermediate</span>
21. [How do you implement ETags for conditional requests?](#q21-how-do-you-implement-etags-for-conditional-requests) <span class="intermediate">Intermediate</span>
22. [How do you optimize SVG assets?](#q22-how-do-you-optimize-svg-assets) <span class="beginner">Beginner</span>
23. [How do you serve responsive images using `srcset` and `sizes`?](#q23-how-do-you-serve-responsive-images-using-srcset-and-sizes) <span class="beginner">Beginner</span>
24. [How do you serve modern image formats (WebP/AVIF) with fallback?](#q24-how-do-you-serve-modern-image-formats-webpavif-with-fallback) <span class="beginner">Beginner</span>
25. [How do you optimize video delivery to save bandwidth?](#q25-how-do-you-optimize-video-delivery-to-save-bandwidth) <span class="advanced">Advanced</span>
26. [How do you lazy load third-party scripts (e.g., Chat Widget)?](#q26-how-do-you-lazy-load-third-party-scripts-e.g.-chat-widget) <span class="intermediate">Intermediate</span>
27. [How do you optimize Google Fonts performance?](#q27-how-do-you-optimize-google-fonts-performance) <span class="intermediate">Intermediate</span>
28. [How do you reduce the performance impact of A/B testing scripts?](#q28-how-do-you-reduce-the-performance-impact-of-ab-testing-scripts) <span class="advanced">Advanced</span>
29. [How do you detect 'Forced Synchronous Layout' (Layout Thrashing)?](#q29-how-do-you-detect-forced-synchronous-layout-layout-thrashing) <span class="advanced">Advanced</span>
30. [How do you optimize CSS selectors for rendering performance?](#q30-how-do-you-optimize-css-selectors-for-rendering-performance) <span class="advanced">Advanced</span>
31. [How do you reduce DOM size complexity?](#q31-how-do-you-reduce-dom-size-complexity) <span class="intermediate">Intermediate</span>
32. [How do you prevent unnecessary React re-renders using `React.memo`?](#q32-how-do-you-prevent-unnecessary-react-re-renders-using-react.memo) <span class="intermediate">Intermediate</span>
33. [How do you implement Windowing (Virtualization) for a list?](#q33-how-do-you-implement-windowing-virtualization-for-a-list) <span class="advanced">Advanced</span>
34. [Why should you NOT use the array index as a key in React lists?](#q34-why-should-you-not-use-the-array-index-as-a-key-in-react-lists) <span class="beginner">Beginner</span>
35. [When should you use `useMemo`?](#q35-when-should-you-use-usememo) <span class="beginner">Beginner</span>
36. [How do you implement Code Splitting in Webpack?](#q36-how-do-you-implement-code-splitting-in-webpack) <span class="intermediate">Intermediate</span>
37. [How do you prefetch a resource when a user hovers over a link?](#q37-how-do-you-prefetch-a-resource-when-a-user-hovers-over-a-link) <span class="intermediate">Intermediate</span>
38. [What is the PRPL Pattern?](#q38-what-is-the-prpl-pattern) <span class="advanced">Advanced</span>
39. [How do you use Selective Hydration in React 18?](#q39-how-do-you-use-selective-hydration-in-react-18) <span class="advanced">Advanced</span>
40. [How do you reduce Time to First Byte (TTFB)?](#q40-how-do-you-reduce-time-to-first-byte-ttfb) <span class="intermediate">Intermediate</span>
41. [How do you enable Brotli compression?](#q41-how-do-you-enable-brotli-compression) <span class="beginner">Beginner</span>
42. [How do you solve the N+1 Query Problem?](#q42-how-do-you-solve-the-n+1-query-problem) <span class="intermediate">Intermediate</span>
43. [Why use HTTP/3 (QUIC)?](#q43-why-use-http3-quic) <span class="advanced">Advanced</span>
44. [How do you measure Core Web Vitals in code?](#q44-how-do-you-measure-core-web-vitals-in-code) <span class="intermediate">Intermediate</span>
45. [How do you enforce a Performance Budget?](#q45-how-do-you-enforce-a-performance-budget) <span class="advanced">Advanced</span>
46. [How do you improve the initial load of a Single Page Application (SPA)?](#q46-how-do-you-improve-the-initial-load-of-a-single-page-application-spa) <span class="intermediate">Intermediate</span>
47. [How do you use the Next.js Image component for optimization?](#q47-how-do-you-use-the-next.js-image-component-for-optimization) <span class="intermediate">Intermediate</span>
48. [How do you subset fonts to reduce file size?](#q48-how-do-you-subset-fonts-to-reduce-file-size) <span class="advanced">Advanced</span>
49. [How do you avoid request waterfalls?](#q49-how-do-you-avoid-request-waterfalls) <span class="intermediate">Intermediate</span>
50. [When should you inline assets as Base64?](#q50-when-should-you-inline-assets-as-base64) <span class="beginner">Beginner</span>
51. [How do you handle Performance state management in large scale applications?](#q51-how-do-you-handle-performance-state-management-in-large-scale-applications) <span class="advanced">Advanced</span>
52. [How do you perform Performance data validation in microservices?](#q52-how-do-you-perform-performance-data-validation-in-microservices) <span class="beginner">Beginner</span>
53. [How do you automate Performance deployment for mobile devices?](#q53-how-do-you-automate-performance-deployment-for-mobile-devices) <span class="advanced">Advanced</span>
54. [How do you handle Performance concurrency issues in legacy systems?](#q54-how-do-you-handle-performance-concurrency-issues-in-legacy-systems) <span class="advanced">Advanced</span>
55. [How do you implement Performance caching in cloud infrastructure?](#q55-how-do-you-implement-performance-caching-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
56. [How do you manage Performance configuration for real-time systems?](#q56-how-do-you-manage-performance-configuration-for-real-time-systems) <span class="beginner">Beginner</span>
57. [How do you handle Performance internationalization (i18n) in distributed systems?](#q57-how-do-you-handle-performance-internationalization-i18n-in-distributed-systems) <span class="intermediate">Intermediate</span>
58. [How do you ensure Performance accessibility (a11y) in high-traffic sites?](#q58-how-do-you-ensure-performance-accessibility-a11y-in-high-traffic-sites) <span class="beginner">Beginner</span>
59. [How do you optimize Performance network requests in embedded systems?](#q59-how-do-you-optimize-performance-network-requests-in-embedded-systems) <span class="advanced">Advanced</span>
60. [How do you handle Performance performance optimization for production environments?](#q60-how-do-you-handle-performance-performance-optimization-for-production-environments) <span class="advanced">Advanced</span>
61. [What are the security implications of Performance in large scale applications?](#q61-what-are-the-security-implications-of-performance-in-large-scale-applications) <span class="intermediate">Intermediate</span>
62. [How do you debug Performance memory leaks in microservices?](#q62-how-do-you-debug-performance-memory-leaks-in-microservices) <span class="advanced">Advanced</span>
63. [Best practices for Performance code organization in mobile devices?](#q63-best-practices-for-performance-code-organization-in-mobile-devices) <span class="beginner">Beginner</span>
64. [How do you implement Performance error handling for legacy systems?](#q64-how-do-you-implement-performance-error-handling-for-legacy-systems) <span class="intermediate">Intermediate</span>
65. [How do you test Performance functionality in cloud infrastructure?](#q65-how-do-you-test-performance-functionality-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
66. [How do you handle Performance state management in real-time systems?](#q66-how-do-you-handle-performance-state-management-in-real-time-systems) <span class="advanced">Advanced</span>
67. [How do you perform Performance data validation in distributed systems?](#q67-how-do-you-perform-performance-data-validation-in-distributed-systems) <span class="beginner">Beginner</span>
68. [How do you automate Performance deployment for high-traffic sites?](#q68-how-do-you-automate-performance-deployment-for-high-traffic-sites) <span class="advanced">Advanced</span>
69. [How do you handle Performance concurrency issues in embedded systems?](#q69-how-do-you-handle-performance-concurrency-issues-in-embedded-systems) <span class="advanced">Advanced</span>
70. [How do you implement Performance caching in production environments?](#q70-how-do-you-implement-performance-caching-in-production-environments) <span class="intermediate">Intermediate</span>
71. [How do you manage Performance configuration for large scale applications?](#q71-how-do-you-manage-performance-configuration-for-large-scale-applications) <span class="beginner">Beginner</span>
72. [How do you handle Performance internationalization (i18n) in microservices?](#q72-how-do-you-handle-performance-internationalization-i18n-in-microservices) <span class="intermediate">Intermediate</span>
73. [How do you ensure Performance accessibility (a11y) in mobile devices?](#q73-how-do-you-ensure-performance-accessibility-a11y-in-mobile-devices) <span class="beginner">Beginner</span>
74. [How do you optimize Performance network requests in legacy systems?](#q74-how-do-you-optimize-performance-network-requests-in-legacy-systems) <span class="advanced">Advanced</span>
75. [How do you handle Performance performance optimization for cloud infrastructure?](#q75-how-do-you-handle-performance-performance-optimization-for-cloud-infrastructure) <span class="advanced">Advanced</span>
76. [What are the security implications of Performance in real-time systems?](#q76-what-are-the-security-implications-of-performance-in-real-time-systems) <span class="intermediate">Intermediate</span>
77. [How do you debug Performance memory leaks in distributed systems?](#q77-how-do-you-debug-performance-memory-leaks-in-distributed-systems) <span class="advanced">Advanced</span>
78. [Best practices for Performance code organization in high-traffic sites?](#q78-best-practices-for-performance-code-organization-in-high-traffic-sites) <span class="beginner">Beginner</span>
79. [How do you implement Performance error handling for embedded systems?](#q79-how-do-you-implement-performance-error-handling-for-embedded-systems) <span class="intermediate">Intermediate</span>
80. [How do you test Performance functionality in production environments?](#q80-how-do-you-test-performance-functionality-in-production-environments) <span class="intermediate">Intermediate</span>
81. [How do you handle Performance state management in large scale applications?](#q81-how-do-you-handle-performance-state-management-in-large-scale-applications) <span class="advanced">Advanced</span>
82. [How do you perform Performance data validation in microservices?](#q82-how-do-you-perform-performance-data-validation-in-microservices) <span class="beginner">Beginner</span>
83. [How do you automate Performance deployment for mobile devices?](#q83-how-do-you-automate-performance-deployment-for-mobile-devices) <span class="advanced">Advanced</span>
84. [How do you handle Performance concurrency issues in legacy systems?](#q84-how-do-you-handle-performance-concurrency-issues-in-legacy-systems) <span class="advanced">Advanced</span>
85. [How do you implement Performance caching in cloud infrastructure?](#q85-how-do-you-implement-performance-caching-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
86. [How do you manage Performance configuration for real-time systems?](#q86-how-do-you-manage-performance-configuration-for-real-time-systems) <span class="beginner">Beginner</span>
87. [How do you handle Performance internationalization (i18n) in distributed systems?](#q87-how-do-you-handle-performance-internationalization-i18n-in-distributed-systems) <span class="intermediate">Intermediate</span>
88. [How do you ensure Performance accessibility (a11y) in high-traffic sites?](#q88-how-do-you-ensure-performance-accessibility-a11y-in-high-traffic-sites) <span class="beginner">Beginner</span>
89. [How do you optimize Performance network requests in embedded systems?](#q89-how-do-you-optimize-performance-network-requests-in-embedded-systems) <span class="advanced">Advanced</span>
90. [How do you handle Performance performance optimization for production environments?](#q90-how-do-you-handle-performance-performance-optimization-for-production-environments) <span class="advanced">Advanced</span>
91. [What are the security implications of Performance in large scale applications?](#q91-what-are-the-security-implications-of-performance-in-large-scale-applications) <span class="intermediate">Intermediate</span>
92. [How do you debug Performance memory leaks in microservices?](#q92-how-do-you-debug-performance-memory-leaks-in-microservices) <span class="advanced">Advanced</span>
93. [Best practices for Performance code organization in mobile devices?](#q93-best-practices-for-performance-code-organization-in-mobile-devices) <span class="beginner">Beginner</span>
94. [How do you implement Performance error handling for legacy systems?](#q94-how-do-you-implement-performance-error-handling-for-legacy-systems) <span class="intermediate">Intermediate</span>
95. [How do you test Performance functionality in cloud infrastructure?](#q95-how-do-you-test-performance-functionality-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
96. [How do you handle Performance state management in real-time systems?](#q96-how-do-you-handle-performance-state-management-in-real-time-systems) <span class="advanced">Advanced</span>
97. [How do you perform Performance data validation in distributed systems?](#q97-how-do-you-perform-performance-data-validation-in-distributed-systems) <span class="beginner">Beginner</span>
98. [How do you automate Performance deployment for high-traffic sites?](#q98-how-do-you-automate-performance-deployment-for-high-traffic-sites) <span class="advanced">Advanced</span>
99. [How do you handle Performance concurrency issues in embedded systems?](#q99-how-do-you-handle-performance-concurrency-issues-in-embedded-systems) <span class="advanced">Advanced</span>
100. [How do you implement Performance caching in production environments?](#q100-how-do-you-implement-performance-caching-in-production-environments) <span class="intermediate">Intermediate</span>

---

### Q1: You have a React application with a slow initial load time due to a large bundle. How do you implement 'Route-Based Code Splitting' to fix this?

**Solution: `React.lazy` and `Suspense`**

Split the code at the route level so users only download what they need for the current page.

```javascript
import React, { Suspense, lazy } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

// Lazy load components
const Home = lazy(() => import('./routes/Home'));
const Dashboard = lazy(() => import('./routes/Dashboard'));

function App() {
  return (
    <Router>
      {/* Show fallback while loading chunk */}
      <Suspense fallback={<div>Loading page...</div>}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/dashboard" element={<Dashboard />} />
        </Routes>
      </Suspense>
    </Router>
  );
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q2: Your LCP (Largest Contentful Paint) score is poor because the hero image loads late. How do you use `fetchpriority` and `preload` to optimize it?

**Solution: Resource Prioritization**

1.  **Preload** the image in `<head>` to start downloading immediately.
2.  **Fetch Priority** on the `<img>` tag to signal high importance to the browser.

```html
<!-- In <head> -->
<link rel="preload" href="/hero-image.jpg" as="image" />

<!-- In <body> -->
<img 
  src="/hero-image.jpg" 
  alt="Hero" 
  fetchpriority="high" 
  width="1200" 
  height="600"
/>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q3: You notice 'Layout Thrashing' in a loop where you read and write DOM properties. How do you refactor this to improve rendering performance?

**Solution: Batch Reads and Writes**

Reading a layout property (like `offsetHeight`) forces the browser to recalculate styles (Reflow). Doing this in a loop causes Thrashing.

**Bad Code:**
```javascript
const items = document.querySelectorAll('.item');
for (let i = 0; i < items.length; i++) {
  // Read causes reflow
  const width = items[i].offsetWidth; 
  // Write invalidates layout
  items[i].style.width = (width + 10) + 'px'; 
}
```

**Optimized Code:**
```javascript
const items = document.querySelectorAll('.item');
// 1. Batch Reads
const widths = Array.from(items).map(item => item.offsetWidth);

// 2. Batch Writes
items.forEach((item, i) => {
  item.style.width = (widths[i] + 10) + 'px';
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q4: How do you implement a 'Virtual List' (Windowing) in React to render 10,000 rows without crashing the browser?

**Solution: `react-window` or `react-virtualized`**

Only render the items currently visible in the viewport.

```javascript
import { FixedSizeList as List } from 'react-window';

const Row = ({ index, style }) => (
  <div style={style}>Row {index}</div>
);

const Example = () => (
  <List
    height={500}      // Height of the container
    itemCount={10000} // Total items
    itemSize={35}     // Height of each row
    width={300}       // Width of the container
  >
    {Row}
  </List>
);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q5: You have a heavy calculation running on the main thread that blocks UI interactions. How do you offload this to a Web Worker?

**Solution: Web Workers**

Move CPU-intensive tasks to a background thread.

**worker.js:**
```javascript
self.onmessage = (e) => {
  const result = heavyComputation(e.data);
  postMessage(result);
};
```

**main.js:**
```javascript
const worker = new Worker('worker.js');

worker.onmessage = (e) => {
  console.log('Result:', e.data);
};

worker.postMessage(inputData); // Start task
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q6: How do you prevent 'Cumulative Layout Shift' (CLS) caused by images loading without dimensions?

**Solution: Explicit Dimensions or Aspect Ratio**

Reserve space for the image before it loads.

```css
/* Modern approach using aspect-ratio */
img.hero {
  width: 100%;
  aspect-ratio: 16 / 9; 
  object-fit: cover;
}
```

```html
<!-- Or explicit attributes -->
<img src="pic.jpg" width="800" height="450" alt="..." />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q7: How do you use the `IntersectionObserver` API to lazy load images as they scroll into view?

**Solution: IntersectionObserver**

Check if the element is intersecting with the viewport.

```javascript
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const img = entry.target;
      img.src = img.dataset.src; // Load real image
      observer.unobserve(img);
    }
  });
});

document.querySelectorAll('img[data-src]').forEach(img => {
  observer.observe(img);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q8: You are optimizing a search input. How do you implement a 'Debounce' function to reduce the number of API calls?

**Solution: Debounce Function**

Delay the execution until the user stops typing for a specified delay.

```javascript
function debounce(func, delay) {
  let timeout;
  return function(...args) {
    clearTimeout(timeout);
    timeout = setTimeout(() => func.apply(this, args), delay);
  };
}

const handleSearch = debounce((query) => {
  fetch(`/api/search?q=${query}`);
}, 300);

// Usage: <input onChange={(e) => handleSearch(e.target.value)} />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q9: How do you identify and fix a 'Memory Leak' caused by a detached event listener in a React component?

**Solution: Cleanup Function in `useEffect`**

Always remove event listeners when the component unmounts.

```javascript
useEffect(() => {
  const handleResize = () => console.log('Resized');
  
  window.addEventListener('resize', handleResize);

  // Cleanup function
  return () => {
    window.removeEventListener('resize', handleResize);
  };
}, []);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q10: How do you use `requestAnimationFrame` to create smooth, 60fps animations instead of using `setInterval`?

**Solution: `requestAnimationFrame` loop**

The browser syncs the update with the display refresh rate.

```javascript
function animate() {
  // Update animation state
  element.style.transform = `translateX(${pos}px)`;
  pos++;

  if (pos < 500) {
    requestAnimationFrame(animate);
  }
}

requestAnimationFrame(animate);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q11: How do you optimize a large React context that causes unnecessary re-renders in consumer components?

**Solution: Split Context or Memoize Value**

If `value` creates a new object every render, all consumers re-render.

```javascript
// Bad
// <Context.Provider value={{ user, theme }}>

// Good: Memoize the value object
const value = useMemo(() => ({ user, theme }), [user, theme]);

return (
  <Context.Provider value={value}>
    {children}
  </Context.Provider>
);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q12: How do you use the 'Performance API' to measure the execution time of a specific function?

**Solution: `performance.now()` or `performance.mark()`**

```javascript
const start = performance.now();

heavyFunction();

const end = performance.now();
console.log(`Execution time: ${end - start} ms`);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q13: How do you configure Webpack to use 'Tree Shaking' to remove unused code from your production bundle?

**Solution: ES Modules + Production Mode**

Ensure you use `import/export` syntax and set `mode: 'production'`.

```javascript
// webpack.config.js
module.exports = {
  mode: 'production', // Automatically enables Tree Shaking
  optimization: {
    usedExports: true, // Marks unused exports
  },
};

// Code
import { useful } from './utils'; // 'useless' function is dropped
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q14: How do you implement 'Resource Hints' (dns-prefetch, preconnect) to speed up third-party API connections?

**Solution: `<link>` tags in Head**

Establish network handshake early.

```html
<head>
  <!-- Resolve DNS early -->
  <link rel="dns-prefetch" href="https://api.example.com">
  
  <!-- Perform DNS + TCP + TLS handshake early -->
  <link rel="preconnect" href="https://fonts.googleapis.com" crossorigin>
</head>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q15: How do you optimize CSS delivery to avoid 'Render Blocking' resources?

**Solution: Critical CSS + Async Loading**

Inline critical CSS for above-the-fold content, load the rest asynchronously.

```html
<head>
  <!-- Critical CSS inlined -->
  <style> .hero { color: red; } </style>
  
  <!-- Non-critical CSS loaded async -->
  <link rel="preload" href="styles.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link rel="stylesheet" href="styles.css"></noscript>
</head>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q16: How do you minimize main thread work to improve INP (Interaction to Next Paint)?

**Difficulty**: Expert

**Strategy:**
Break up long tasks using `setTimeout`, `requestIdleCallback`, or the new `scheduler.yield()` API to yield control back to the browser, allowing it to respond to user input.

**Code Example:**
async function heavyTask() {
  for (const item of items) {
    process(item);
    // Yield to main thread every 50ms
    if (shouldYield()) await scheduler.yield(); 
  }
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q17: How do you optimize font loading using `font-display: swap`?

**Difficulty**: Beginner

**Strategy:**
Use `font-display: swap` in your `@font-face` rule. It tells the browser to use a fallback font immediately and swap to the custom font once it loads, preventing invisible text (FOIT).

**Code Example:**
@font-face {
  font-family: 'MyFont';
  src: url('myfont.woff2') format('woff2');
  font-display: swap;
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q18: How do you prevent Layout Shifts from dynamic ads?

**Difficulty**: Intermediate

**Strategy:**
Reserve space for the ad slot using a container with fixed dimensions (min-height). If the ad doesn't load, keep the empty space or collapse it only if it won't shift viewport content.

**Code Example:**
<div class="ad-slot" style="min-height: 250px; width: 300px; background: #f0f0f0;">
  <!-- Ad injects here -->
</div>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q19: How do you implement a 'Cache First' strategy in a Service Worker?

**Difficulty**: Intermediate

**Strategy:**
Intercept the fetch event. Check the cache; if found, return it. If not, fetch from network, cache it, and return it.

**Code Example:**
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request).then(cached => {
      return cached || fetch(event.request).then(response => {
        return caches.open('v1').then(cache => {
          cache.put(event.request, response.clone());
          return response;
        });
      });
    })
  );
});

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q20: How do you configure HTTP Cache-Control headers for immutable static assets?

**Difficulty**: Intermediate

**Strategy:**
For hashed assets (e.g., `main.a1b2c.js`), use a long `max-age` and `immutable`. This tells the browser the file will never change.

**Code Example:**
Cache-Control: public, max-age=31536000, immutable

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q21: How do you implement ETags for conditional requests?

**Difficulty**: Intermediate

**Strategy:**
The server generates a hash (ETag) of the content. The client sends `If-None-Match`. If hashes match, server returns 304 Not Modified (empty body), saving bandwidth.

**Code Example:**
// Express.js (enabled by default)
app.set('etag', true); 
// Response: ETag: "12345"
// Request: If-None-Match: "12345" -> 304

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q22: How do you optimize SVG assets?

**Difficulty**: Beginner

**Strategy:**
Use tools like SVGO to remove unnecessary metadata, comments, and hidden elements. Minify paths.

**Code Example:**
# CLI
svgo input.svg -o output.svg

# Webpack
{
  loader: 'image-webpack-loader',
  options: { svgo: { ... } }
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q23: How do you serve responsive images using `srcset` and `sizes`?

**Difficulty**: Beginner

**Strategy:**
Provide multiple resolutions of the same image. The browser picks the best one based on screen density (DPR) and layout width.

**Code Example:**
<img 
  src="small.jpg"
  srcset="small.jpg 500w, medium.jpg 1000w, large.jpg 1500w"
  sizes="(max-width: 600px) 100vw, 50vw"
  alt="Responsive"
/>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q24: How do you serve modern image formats (WebP/AVIF) with fallback?

**Difficulty**: Beginner

**Strategy:**
Use the `<picture>` element with `<source>` tags for modern formats and `<img>` for fallback.

**Code Example:**
<picture>
  <source srcset="image.avif" type="image/avif">
  <source srcset="image.webp" type="image/webp">
  <img src="image.jpg" alt="Fallback">
</picture>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q25: How do you optimize video delivery to save bandwidth?

**Difficulty**: Advanced

**Strategy:**
Use `preload='none'` if autoplay isn't needed. Use adaptive bitrate streaming (HLS/DASH) to serve quality matching the user's bandwidth. Use muted/autoplay for gif-like behavior.

**Code Example:**
<video controls preload="none" poster="preview.jpg">
  <source src="video.mp4" type="video/mp4">
</video>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q26: How do you lazy load third-party scripts (e.g., Chat Widget)?

**Difficulty**: Intermediate

**Strategy:**
Load the script only when the user interacts (e.g., clicks a button) or after the page is idle (`requestIdleCallback`). Use a 'Facade' (fake button) initially.

**Code Example:**
const loadChat = () => {
  const script = document.createElement('script');
  script.src = 'https://chat-widget.com/embed.js';
  document.body.appendChild(script);
};

<button onClick={loadChat}>Chat with us</button>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q27: How do you optimize Google Fonts performance?

**Difficulty**: Intermediate

**Strategy:**
Self-host if possible. If not, use `preconnect` to `fonts.gstatic.com`. Combine requests. Use `text=` parameter to fetch only used characters.

**Code Example:**
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q28: How do you reduce the performance impact of A/B testing scripts?

**Difficulty**: Advanced

**Strategy:**
Avoid client-side A/B testing (flicker, delay). Use Server-Side A/B testing (Edge Config/Middleware) to serve different HTML versions directly.

**Code Example:**
// Next.js Middleware (Edge)
if (bucket === 'variant-a') {
  return NextResponse.rewrite('/home-a');
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q29: How do you detect 'Forced Synchronous Layout' (Layout Thrashing)?

**Difficulty**: Advanced

**Strategy:**
Use Chrome DevTools Performance tab. Look for 'Layout' events triggered by JS (purple bars) with warning flags. They occur when you read layout properties (e.g., `offsetHeight`) after writing style.

**Code Example:**
// Thrashing
div.style.width = '100px';
console.log(div.offsetWidth); // Forces layout recalculation immediately

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q30: How do you optimize CSS selectors for rendering performance?

**Difficulty**: Advanced

**Strategy:**
Avoid complex, deep descendants (`div > div > p > span`). Use specific classes (`.user-name`). Browsers match right-to-left; simple classes are fastest.

**Code Example:**
/* Slow */
div.container > ul li:nth-child(odd) a.link { ... }

/* Fast */
.link-item { ... }

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q31: How do you reduce DOM size complexity?

**Difficulty**: Intermediate

**Strategy:**
Avoid wrapper `<div>` soup. Use CSS Grid/Flexbox to reduce structural depth. Use `<ng-container>` (Angular) or `<Fragment>` (React) to group elements without DOM nodes.

**Code Example:**
// React
return (
  <>
    <Header />
    <Main />
  </>
);

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q32: How do you prevent unnecessary React re-renders using `React.memo`?

**Difficulty**: Intermediate

**Strategy:**
Wrap functional components in `React.memo`. It does a shallow comparison of props and skips rendering if props haven't changed.

**Code Example:**
const MyComponent = React.memo(({ data }) => {
  return <div>{data}</div>;
});

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q33: How do you implement Windowing (Virtualization) for a list?

**Difficulty**: Advanced

**Strategy:**
Render only the visible subset of rows. Use libraries like `react-window`.

**Code Example:**
<FixedSizeList height={500} itemCount={1000} itemSize={35} width={300}>
  {({ index, style }) => <div style={style}>Row {index}</div>}
</FixedSizeList>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q34: Why should you NOT use the array index as a key in React lists?

**Difficulty**: Beginner

**Strategy:**
If the list can be reordered, filtered, or prepended, using index as key causes bugs with component state and inefficient DOM updates. Use a unique ID.

**Code Example:**
// Bad
items.map((item, index) => <Li key={index} />)

// Good
items.map(item => <Li key={item.id} />)

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q35: When should you use `useMemo`?

**Difficulty**: Beginner

**Strategy:**
Use `useMemo` to cache the result of an expensive calculation (e.g., filtering a large array) so it doesn't run on every render.

**Code Example:**
const sortedList = useMemo(() => {
  return list.sort((a, b) => a.value - b.value);
}, [list]);

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q36: How do you implement Code Splitting in Webpack?

**Difficulty**: Intermediate

**Strategy:**
Use Dynamic Imports (`import()`). Webpack automatically creates a separate chunk for imported modules.

**Code Example:**
import('./module').then(module => {
  module.doSomething();
});

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q37: How do you prefetch a resource when a user hovers over a link?

**Difficulty**: Intermediate

**Strategy:**
Add a `<link rel='prefetch'>` tag dynamically on hover.

**Code Example:**
const prefetch = (url) => {
  const link = document.createElement('link');
  link.rel = 'prefetch';
  link.href = url;
  document.head.appendChild(link);
};

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q38: What is the PRPL Pattern?

**Difficulty**: Advanced

**Strategy:**
**Push** critical resources (preload). **Render** initial route. **Pre-cache** remaining routes. **Lazy-load** remaining routes on demand.

**Code Example:**
// Service Worker Caching strategy implements Pre-cache and Lazy-load.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q39: How do you use Selective Hydration in React 18?

**Difficulty**: Advanced

**Strategy:**
Wrap slow parts of the UI in `<Suspense>`. React hydrates the critical parts first and hydrates suspended parts later (or prioritizes based on user interaction).

**Code Example:**
<Suspense fallback={<Spinner />}>
  <Comments />
</Suspense>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q40: How do you reduce Time to First Byte (TTFB)?

**Difficulty**: Intermediate

**Strategy:**
Cache database queries. Use a CDN to cache HTML at the edge. Optimize server logic. Upgrade server hardware.

**Code Example:**
// CDN Edge Cache
Cache-Control: s-maxage=60, stale-while-revalidate

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q41: How do you enable Brotli compression?

**Difficulty**: Beginner

**Strategy:**
Configure your web server (Nginx, Apache) or CDN to use Brotli (`br`). It compresses better than Gzip for text.

**Code Example:**
# Nginx
brotli on;
brotli_comp_level 6;
brotli_types text/plain text/css application/javascript;

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q42: How do you solve the N+1 Query Problem?

**Difficulty**: Intermediate

**Strategy:**
Use eager loading (`JOIN` in SQL) or batching (DataLoader in GraphQL) to fetch related data in a single query instead of one per item.

**Code Example:**
// Bad: Loop queries
// Good: SELECT * FROM comments WHERE post_id IN (1, 2, 3)

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q43: Why use HTTP/3 (QUIC)?

**Difficulty**: Advanced

**Strategy:**
HTTP/3 uses UDP instead of TCP. It solves Head-of-Line Blocking (packet loss doesn't stop other streams), establishes connections faster (0-RTT), and handles network switching better.

**Code Example:**
# Enable in Nginx
listen 443 quic reuseport;

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q44: How do you measure Core Web Vitals in code?

**Difficulty**: Intermediate

**Strategy:**
Use the `web-vitals` library to capture CLS, LCP, and INP.

**Code Example:**
import { onLCP, onFID, onCLS } from 'web-vitals';

onCLS(console.log);
onLCP(console.log);

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q45: How do you enforce a Performance Budget?

**Difficulty**: Advanced

**Strategy:**
Use `bundlesize` or Lighthouse CI. Fail the build if bundle size exceeds the limit.

**Code Example:**
// package.json
"bundlesize": [
  { "path": "./dist/*.js", "maxSize": "100 kB" }
]

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q46: How do you improve the initial load of a Single Page Application (SPA)?

**Difficulty**: Intermediate

**Strategy:**
Use Server-Side Rendering (SSR) or Static Site Generation (SSG) to deliver HTML immediately. Use Code Splitting to reduce JS bundle size.

**Code Example:**
// Next.js uses SSR/SSG by default.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q47: How do you use the Next.js Image component for optimization?

**Difficulty**: Intermediate

**Strategy:**
Use `<Image />`. It automatically resizes, optimizes (WebP), and lazy loads images.

**Code Example:**
import Image from 'next/image';

<Image src="/me.png" width={500} height={500} alt="Me" />

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q48: How do you subset fonts to reduce file size?

**Difficulty**: Advanced

**Strategy:**
Generate a font file containing only the characters you need (e.g., Latin subset, or specific headers). Use `glyphhanger` or `pyftsubset`.

**Code Example:**
pyftsubset font.ttf --unicodes=U+0020-007E --flavor=woff2

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q49: How do you avoid request waterfalls?

**Difficulty**: Intermediate

**Strategy:**
Don't wait for one request to finish before starting the next if they are independent. Use `Promise.all`.

**Code Example:**
// Bad
await getUser();
await getPosts();

// Good
await Promise.all([getUser(), getPosts()]);

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q50: When should you inline assets as Base64?

**Difficulty**: Beginner

**Strategy:**
Only for very small images (icons < 1KB). It saves an HTTP request but increases file size by ~33% and blocks rendering (if in CSS).

**Code Example:**
background: url(data:image/png;base64,iVBOR...);

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---


### Q51: How do you handle Performance state management in large scale applications?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```javascript
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q52: How do you perform Performance data validation in microservices?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```javascript
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q53: How do you automate Performance deployment for mobile devices?

**Difficulty**: Advanced

**Strategy**:
Use CI/CD pipelines. Dockerize the application.

**Code Example**:
```javascript
steps:
  - run: npm test
  - run: docker build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q54: How do you handle Performance concurrency issues in legacy systems?

**Difficulty**: Advanced

**Strategy**:
Use locks, queues, or atomic operations.

**Code Example**:
```javascript
await mutex.runExclusive(async () => {
  // critical section
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q55: How do you implement Performance caching in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Use Redis or in-memory LRU caches.

**Code Example**:
```javascript
const cache = new Map();
if (cache.has(key)) return cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q56: How do you manage Performance configuration for real-time systems?

**Difficulty**: Beginner

**Strategy**:
Use environment variables or config files.

**Code Example**:
```javascript
const config = process.env.CONFIG || 'default';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q57: How do you handle Performance internationalization (i18n) in distributed systems?

**Difficulty**: Intermediate

**Strategy**:
Use i18n libraries. Extract strings to resource files.

**Code Example**:
```javascript
t('welcome_message')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q58: How do you ensure Performance accessibility (a11y) in high-traffic sites?

**Difficulty**: Beginner

**Strategy**:
Use semantic HTML and ARIA roles.

**Code Example**:
```javascript
<button aria-label="Close">X</button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q59: How do you optimize Performance network requests in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use batching, debouncing, or GraphQL.

**Code Example**:
```javascript
debounce(() => fetch(), 300);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q60: How do you handle Performance performance optimization for production environments?

**Difficulty**: Advanced

**Strategy**:
Profile first, then optimize hot paths. Use caching and efficient algorithms.

**Code Example**:
```javascript
const start = performance.now();
// Performance logic
const end = performance.now();
console.log('Time:', end - start);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q61: What are the security implications of Performance in large scale applications?

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

### Q62: How do you debug Performance memory leaks in microservices?

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

### Q63: Best practices for Performance code organization in mobile devices?

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

### Q64: How do you implement Performance error handling for legacy systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```javascript
try {
  await PerformanceOperation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q65: How do you test Performance functionality in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```javascript
test('Performance works', () => {
  expect(Performance()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q66: How do you handle Performance state management in real-time systems?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```javascript
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q67: How do you perform Performance data validation in distributed systems?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```javascript
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q68: How do you automate Performance deployment for high-traffic sites?

**Difficulty**: Advanced

**Strategy**:
Use CI/CD pipelines. Dockerize the application.

**Code Example**:
```javascript
steps:
  - run: npm test
  - run: docker build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q69: How do you handle Performance concurrency issues in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use locks, queues, or atomic operations.

**Code Example**:
```javascript
await mutex.runExclusive(async () => {
  // critical section
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q70: How do you implement Performance caching in production environments?

**Difficulty**: Intermediate

**Strategy**:
Use Redis or in-memory LRU caches.

**Code Example**:
```javascript
const cache = new Map();
if (cache.has(key)) return cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q71: How do you manage Performance configuration for large scale applications?

**Difficulty**: Beginner

**Strategy**:
Use environment variables or config files.

**Code Example**:
```javascript
const config = process.env.CONFIG || 'default';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q72: How do you handle Performance internationalization (i18n) in microservices?

**Difficulty**: Intermediate

**Strategy**:
Use i18n libraries. Extract strings to resource files.

**Code Example**:
```javascript
t('welcome_message')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q73: How do you ensure Performance accessibility (a11y) in mobile devices?

**Difficulty**: Beginner

**Strategy**:
Use semantic HTML and ARIA roles.

**Code Example**:
```javascript
<button aria-label="Close">X</button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q74: How do you optimize Performance network requests in legacy systems?

**Difficulty**: Advanced

**Strategy**:
Use batching, debouncing, or GraphQL.

**Code Example**:
```javascript
debounce(() => fetch(), 300);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q75: How do you handle Performance performance optimization for cloud infrastructure?

**Difficulty**: Advanced

**Strategy**:
Profile first, then optimize hot paths. Use caching and efficient algorithms.

**Code Example**:
```javascript
const start = performance.now();
// Performance logic
const end = performance.now();
console.log('Time:', end - start);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q76: What are the security implications of Performance in real-time systems?

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

### Q77: How do you debug Performance memory leaks in distributed systems?

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

### Q78: Best practices for Performance code organization in high-traffic sites?

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

### Q79: How do you implement Performance error handling for embedded systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```javascript
try {
  await PerformanceOperation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q80: How do you test Performance functionality in production environments?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```javascript
test('Performance works', () => {
  expect(Performance()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q81: How do you handle Performance state management in large scale applications?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```javascript
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q82: How do you perform Performance data validation in microservices?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```javascript
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q83: How do you automate Performance deployment for mobile devices?

**Difficulty**: Advanced

**Strategy**:
Use CI/CD pipelines. Dockerize the application.

**Code Example**:
```javascript
steps:
  - run: npm test
  - run: docker build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q84: How do you handle Performance concurrency issues in legacy systems?

**Difficulty**: Advanced

**Strategy**:
Use locks, queues, or atomic operations.

**Code Example**:
```javascript
await mutex.runExclusive(async () => {
  // critical section
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q85: How do you implement Performance caching in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Use Redis or in-memory LRU caches.

**Code Example**:
```javascript
const cache = new Map();
if (cache.has(key)) return cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q86: How do you manage Performance configuration for real-time systems?

**Difficulty**: Beginner

**Strategy**:
Use environment variables or config files.

**Code Example**:
```javascript
const config = process.env.CONFIG || 'default';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q87: How do you handle Performance internationalization (i18n) in distributed systems?

**Difficulty**: Intermediate

**Strategy**:
Use i18n libraries. Extract strings to resource files.

**Code Example**:
```javascript
t('welcome_message')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q88: How do you ensure Performance accessibility (a11y) in high-traffic sites?

**Difficulty**: Beginner

**Strategy**:
Use semantic HTML and ARIA roles.

**Code Example**:
```javascript
<button aria-label="Close">X</button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q89: How do you optimize Performance network requests in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use batching, debouncing, or GraphQL.

**Code Example**:
```javascript
debounce(() => fetch(), 300);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q90: How do you handle Performance performance optimization for production environments?

**Difficulty**: Advanced

**Strategy**:
Profile first, then optimize hot paths. Use caching and efficient algorithms.

**Code Example**:
```javascript
const start = performance.now();
// Performance logic
const end = performance.now();
console.log('Time:', end - start);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q91: What are the security implications of Performance in large scale applications?

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

### Q92: How do you debug Performance memory leaks in microservices?

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

### Q93: Best practices for Performance code organization in mobile devices?

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

### Q94: How do you implement Performance error handling for legacy systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```javascript
try {
  await PerformanceOperation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q95: How do you test Performance functionality in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```javascript
test('Performance works', () => {
  expect(Performance()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q96: How do you handle Performance state management in real-time systems?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```javascript
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q97: How do you perform Performance data validation in distributed systems?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```javascript
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q98: How do you automate Performance deployment for high-traffic sites?

**Difficulty**: Advanced

**Strategy**:
Use CI/CD pipelines. Dockerize the application.

**Code Example**:
```javascript
steps:
  - run: npm test
  - run: docker build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q99: How do you handle Performance concurrency issues in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use locks, queues, or atomic operations.

**Code Example**:
```javascript
await mutex.runExclusive(async () => {
  // critical section
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q100: How do you implement Performance caching in production environments?

**Difficulty**: Intermediate

**Strategy**:
Use Redis or in-memory LRU caches.

**Code Example**:
```javascript
const cache = new Map();
if (cache.has(key)) return cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---
