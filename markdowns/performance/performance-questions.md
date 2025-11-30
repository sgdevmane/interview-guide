# Performance Interview Questions

## Table of Contents
1. [You have a React application with a slow initial load time due to a large bundle. How do you implement 'Route-Based Code Splitting' to fix this?](#q1-you-have-a-react-application-with-a-slow-initial-load-time-due-to-a-large-bun)
2. [Your LCP (Largest Contentful Paint) score is poor because the hero image loads late. How do you use `fetchpriority` and `preload` to optimize it?](#q2-your-lcp-largest-contentful-paint-score-is-poor-because-the-hero-image-loads-)
3. [You notice 'Layout Thrashing' in a loop where you read and write DOM properties. How do you refactor this to improve rendering performance?](#q3-you-notice-layout-thrashing-in-a-loop-where-you-read-and-write-dom-properties)
4. [How do you implement a 'Virtual List' (Windowing) in React to render 10,000 rows without crashing the browser?](#q4-how-do-you-implement-a-virtual-list-windowing-in-react-to-render-10-000-rows-)
5. [You have a heavy calculation running on the main thread that blocks UI interactions. How do you offload this to a Web Worker?](#q5-you-have-a-heavy-calculation-running-on-the-main-thread-that-blocks-ui-intera)
6. [How do you prevent 'Cumulative Layout Shift' (CLS) caused by images loading without dimensions?](#q6-how-do-you-prevent-cumulative-layout-shift-cls-caused-by-images-loading-witho)
7. [How do you use the `IntersectionObserver` API to lazy load images as they scroll into view?](#q7-how-do-you-use-the-intersectionobserver-api-to-lazy-load-images-as-they-scrol)
8. [You are optimizing a search input. How do you implement a 'Debounce' function to reduce the number of API calls?](#q8-you-are-optimizing-a-search-input-how-do-you-implement-a-debounce-function-to)
9. [How do you identify and fix a 'Memory Leak' caused by a detached event listener in a React component?](#q9-how-do-you-identify-and-fix-a-memory-leak-caused-by-a-detached-event-listener)
10. [How do you use `requestAnimationFrame` to create smooth, 60fps animations instead of using `setInterval`?](#q10-how-do-you-use-requestanimationframe-to-create-smooth-60fps-animations-inste)
11. [How do you optimize a large React context that causes unnecessary re-renders in consumer components?](#q11-how-do-you-optimize-a-large-react-context-that-causes-unnecessary-re-renders)
12. [How do you use the 'Performance API' to measure the execution time of a specific function?](#q12-how-do-you-use-the-performance-api-to-measure-the-execution-time-of-a-specif)
13. [How do you configure Webpack to use 'Tree Shaking' to remove unused code from your production bundle?](#q13-how-do-you-configure-webpack-to-use-tree-shaking-to-remove-unused-code-from-)
14. [How do you implement 'Resource Hints' (dns-prefetch, preconnect) to speed up third-party API connections?](#q14-how-do-you-implement-resource-hints-dns-prefetch-preconnect-to-speed-up-thir)
15. [How do you optimize CSS delivery to avoid 'Render Blocking' resources?](#q15-how-do-you-optimize-css-delivery-to-avoid-render-blocking-resources)
16. [How do you minimize main thread work to improve INP?](#q16-how-do-you-minimize-main-thread-work-to-improve-inp)
17. [How do you use the Scheduler API (scheduler.yield) to break up long tasks?](#q17-how-do-you-use-the-scheduler-api-scheduler-yield-to-break-up-long-tasks)
18. [How do you optimize font loading using font-display: swap?](#q18-how-do-you-optimize-font-loading-using-font-display:-swap)
19. [How do you prevent Layout Shifts from dynamic ads?](#q19-how-do-you-prevent-layout-shifts-from-dynamic-ads)
20. [How do you use HTTP/2 Server Push (or why avoid it)?](#q20-how-do-you-use-http-2-server-push-or-why-avoid-it)
21. [How do you implement a Service Worker for offline caching?](#q21-how-do-you-implement-a-service-worker-for-offline-caching)
22. [How do you use the Cache API within a Service Worker?](#q22-how-do-you-use-the-cache-api-within-a-service-worker)
23. [How do you configure HTTP Cache-Control headers for static assets?](#q23-how-do-you-configure-http-cache-control-headers-for-static-assets)
24. [How do you use the Vary header to serve different content versions?](#q24-how-do-you-use-the-vary-header-to-serve-different-content-versions)
25. [How do you implement ETags for conditional requests?](#q25-how-do-you-implement-etags-for-conditional-requests)
26. [How do you optimize SVG assets using SVGO?](#q26-how-do-you-optimize-svg-assets-using-svgo)
27. [How do you serve responsive images using `srcset` and `sizes`?](#q27-how-do-you-serve-responsive-images-using-srcset-and-sizes)
28. [How do you use the `<picture>` element for art direction?](#q28-how-do-you-use-the-<picture>-element-for-art-direction)
29. [How do you convert images to WebP or AVIF formats?](#q29-how-do-you-convert-images-to-webp-or-avif-formats)
30. [How do you optimize video delivery using HLS or DASH?](#q30-how-do-you-optimize-video-delivery-using-hls-or-dash)
31. [How do you use the `poster` attribute for video placeholders?](#q31-how-do-you-use-the-poster-attribute-for-video-placeholders)
32. [How do you lazy load third-party scripts (Google Analytics, etc.)?](#q32-how-do-you-lazy-load-third-party-scripts-google-analytics-etc)
33. [How do you use the `defer` vs `async` attributes on script tags?](#q33-how-do-you-use-the-defer-vs-async-attributes-on-script-tags)
34. [How do you optimize Google Fonts performance?](#q34-how-do-you-optimize-google-fonts-performance)
35. [How do you reduce the impact of A/B testing scripts on LCP?](#q35-how-do-you-reduce-the-impact-of-a-b-testing-scripts-on-lcp)
36. [How do you use the Coverage tab in Chrome DevTools to find unused code?](#q36-how-do-you-use-the-coverage-tab-in-chrome-devtools-to-find-unused-code)
37. [How do you use the Performance tab to analyze flame charts?](#q37-how-do-you-use-the-performance-tab-to-analyze-flame-charts)
38. [How do you use the Network tab to debug waterfall requests?](#q38-how-do-you-use-the-network-tab-to-debug-waterfall-requests)
39. [How do you detect and fix 'forced synchronous layout'?](#q39-how-do-you-detect-and-fix-forced-synchronous-layout)
40. [How do you use `will-change` CSS property correctly?](#q40-how-do-you-use-will-change-css-property-correctly)
41. [How do you optimize CSS selectors to reduce matching time?](#q41-how-do-you-optimize-css-selectors-to-reduce-matching-time)
42. [How do you use CSS containment (`contain` property) for rendering performance?](#q42-how-do-you-use-css-containment-contain-property-for-rendering-performance)
43. [How do you reduce the complexity of the DOM tree?](#q43-how-do-you-reduce-the-complexity-of-the-dom-tree)
44. [How do you optimize React `re-renders` using `React.memo`?](#q44-how-do-you-optimize-react-re-renders-using-react-memo)
45. [How do you use `useCallback` to prevent function recreation?](#q45-how-do-you-use-usecallback-to-prevent-function-recreation)
46. [How do you virtualize a large data grid/table?](#q46-how-do-you-virtualize-a-large-data-grid-table)
47. [How do you optimize list rendering with `key` prop?](#q47-how-do-you-optimize-list-rendering-with-key-prop)
48. [How do you prevent expensive calculations with `useMemo`?](#q48-how-do-you-prevent-expensive-calculations-with-usememo)
49. [How do you use React Profiler to identify slow components?](#q49-how-do-you-use-react-profiler-to-identify-slow-components)
50. [How do you code split a React app using route-based chunks?](#q50-how-do-you-code-split-a-react-app-using-route-based-chunks)
51. [How do you prefetch resources on link hover?](#q51-how-do-you-prefetch-resources-on-link-hover)
52. [How do you use the Network Information API to adapt to slow connections?](#q52-how-do-you-use-the-network-information-api-to-adapt-to-slow-connections)
53. [How do you implement the PRPL pattern?](#q53-how-do-you-implement-the-prpl-pattern)
54. [How do you optimize hydration in SSR applications?](#q54-how-do-you-optimize-hydration-in-ssr-applications)
55. [How do you use Selective Hydration in React 18?](#q55-how-do-you-use-selective-hydration-in-react-18)
56. [How do you reduce Time to First Byte (TTFB) on the server?](#q56-how-do-you-reduce-time-to-first-byte-ttfb-on-the-server)
57. [How do you configure Gzip or Brotli compression on the server?](#q57-how-do-you-configure-gzip-or-brotli-compression-on-the-server)
58. [How do you optimize database queries to reduce server response time?](#q58-how-do-you-optimize-database-queries-to-reduce-server-response-time)
59. [How do you use a CDN to serve static assets?](#q59-how-do-you-use-a-cdn-to-serve-static-assets)
60. [How do you configure HTTP/3 (QUIC) for faster connections?](#q60-how-do-you-configure-http-3-quic-for-faster-connections)
61. [How do you monitor Real User Metrics (RUM) using Vitals library?](#q61-how-do-you-monitor-real-user-metrics-rum-using-vitals-library)
62. [How do you set up a Performance Budget in CI/CD pipeline?](#q62-how-do-you-set-up-a-performance-budget-in-ci-cd-pipeline)
63. [How do you use Lighthouse CI to prevent regressions?](#q63-how-do-you-use-lighthouse-ci-to-prevent-regressions)
64. [How do you optimize a Single Page Application (SPA) initial load?](#q64-how-do-you-optimize-a-single-page-application-spa-initial-load)
65. [How do you optimize Next.js Image component usage?](#q65-how-do-you-optimize-next-js-image-component-usage)
66. [How do you optimize font subsetting to reduce file size?](#q66-how-do-you-optimize-font-subsetting-to-reduce-file-size)
67. [How do you avoid chain requests (waterfalls) in critical path?](#q67-how-do-you-avoid-chain-requests-waterfalls-in-critical-path)
68. [How do you inline small assets (Base64) to save requests?](#q68-how-do-you-inline-small-assets-base64-to-save-requests)
69. [How do you use Resource Hints for external domains?](#q69-how-do-you-use-resource-hints-for-external-domains)
70. [How do you optimize the Critical Rendering Path?](#q70-how-do-you-optimize-the-critical-rendering-path)
71. [How do you reduce the size of JSON API responses?](#q71-how-do-you-reduce-the-size-of-json-api-responses)
72. [How do you use Protocol Buffers instead of JSON for smaller payloads?](#q72-how-do-you-use-protocol-buffers-instead-of-json-for-smaller-payloads)
73. [How do you optimize GraphQL queries to fetch only needed fields?](#q73-how-do-you-optimize-graphql-queries-to-fetch-only-needed-fields)
74. [How do you batch multiple API requests into one?](#q74-how-do-you-batch-multiple-api-requests-into-one)
75. [How do you use a skeleton screen to improve perceived performance?](#q75-how-do-you-use-a-skeleton-screen-to-improve-perceived-performance)
76. [How do you implement optimistic UI updates?](#q76-how-do-you-implement-optimistic-ui-updates)
77. [How do you offload image processing to a serverless function?](#q77-how-do-you-offload-image-processing-to-a-serverless-function)
78. [How do you use `requestIdleCallback` for low-priority tasks?](#q78-how-do-you-use-requestidlecallback-for-low-priority-tasks)
79. [How do you optimize garbage collection by avoiding object churn?](#q79-how-do-you-optimize-garbage-collection-by-avoiding-object-churn)
80. [How do you profile memory usage using Heap Snapshots?](#q80-how-do-you-profile-memory-usage-using-heap-snapshots)
81. [How do you detect detached DOM nodes causing memory leaks?](#q81-how-do-you-detect-detached-dom-nodes-causing-memory-leaks)
82. [How do you optimize canvas rendering performance?](#q82-how-do-you-optimize-canvas-rendering-performance)
83. [How do you use OffscreenCanvas for background rendering?](#q83-how-do-you-use-offscreencanvas-for-background-rendering)
84. [How do you optimize WebGL rendering?](#q84-how-do-you-optimize-webgl-rendering)
85. [How do you reduce battery usage by pausing background animations?](#q85-how-do-you-reduce-battery-usage-by-pausing-background-animations)
86. [How do you use the Page Visibility API to pause tasks?](#q86-how-do-you-use-the-page-visibility-api-to-pause-tasks)
87. [How do you optimize iframe loading using `loading='lazy'`?](#q87-how-do-you-optimize-iframe-loading-using-loading=-lazy)
88. [How do you isolate third-party widgets in iframes?](#q88-how-do-you-isolate-third-party-widgets-in-iframes)
89. [How do you use the Shadow DOM for style encapsulation/perf?](#q89-how-do-you-use-the-shadow-dom-for-style-encapsulation-perf)
90. [How do you optimize regex patterns to avoid ReDoS?](#q90-how-do-you-optimize-regex-patterns-to-avoid-redos)
91. [How do you use GPU acceleration for animations?](#q91-how-do-you-use-gpu-acceleration-for-animations)
92. [How do you avoid using `@import` in CSS?](#q92-how-do-you-avoid-using-@import-in-css)
93. [How do you bundle CSS vs splitting CSS optimization trade-offs?](#q93-how-do-you-bundle-css-vs-splitting-css-optimization-trade-offs)
94. [How do you use the Back/Forward Cache (bfcache)?](#q94-how-do-you-use-the-back-forward-cache-bfcache)
95. [How do you optimize touch event listeners with `passive: true`?](#q95-how-do-you-optimize-touch-event-listeners-with-passive:-true)
96. [How do you reduce cookie size to lower request overhead?](#q96-how-do-you-reduce-cookie-size-to-lower-request-overhead)
97. [How do you use domain sharding (legacy) vs HTTP/2 multiplexing?](#q97-how-do-you-use-domain-sharding-legacy-vs-http-2-multiplexing)
98. [How do you optimize for low-end devices?](#q98-how-do-you-optimize-for-low-end-devices)
99. [How do you measure TTI (Time to Interactive)?](#q99-how-do-you-measure-tti-time-to-interactive)
100. [How do you measure TBT (Total Blocking Time)?](#q100-how-do-you-measure-tbt-total-blocking-time)
101. [How do you measure Speed Index?](#q101-how-do-you-measure-speed-index)
102. [How do you automate performance testing with Puppeteer/Playwright?](#q102-how-do-you-automate-performance-testing-with-puppeteer-playwright)
103. [How do you use `content-visibility: auto` to skip rendering off-screen content?](#q103-how-do-you-use-content-visibility:-auto-to-skip-rendering-off-screen-conten)
104. [How do you optimize string concatenation in tight loops?](#q104-how-do-you-optimize-string-concatenation-in-tight-loops)
105. [How do you use Bitwise operators for high-perf math (micro-optimization)?](#q105-how-do-you-use-bitwise-operators-for-high-perf-math-micro-optimization)

---

### Q1: You have a React application with a slow initial load time due to a large bundle. How do you implement 'Route-Based Code Splitting' to fix this?

**Difficulty: Intermediate**

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

[Back to Top](#table-of-contents)

---

### Q2: Your LCP (Largest Contentful Paint) score is poor because the hero image loads late. How do you use `fetchpriority` and `preload` to optimize it?

**Difficulty: Advanced**

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

[Back to Top](#table-of-contents)

---

### Q3: You notice 'Layout Thrashing' in a loop where you read and write DOM properties. How do you refactor this to improve rendering performance?

**Difficulty: Advanced**

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

[Back to Top](#table-of-contents)

---

### Q4: How do you implement a 'Virtual List' (Windowing) in React to render 10,000 rows without crashing the browser?

**Difficulty: Expert**

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

[Back to Top](#table-of-contents)

---

### Q5: You have a heavy calculation running on the main thread that blocks UI interactions. How do you offload this to a Web Worker?

**Difficulty: Intermediate**

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

[Back to Top](#table-of-contents)

---

### Q6: How do you prevent 'Cumulative Layout Shift' (CLS) caused by images loading without dimensions?

**Difficulty: Beginner**

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

[Back to Top](#table-of-contents)

---

### Q7: How do you use the `IntersectionObserver` API to lazy load images as they scroll into view?

**Difficulty: Intermediate**

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

[Back to Top](#table-of-contents)

---

### Q8: You are optimizing a search input. How do you implement a 'Debounce' function to reduce the number of API calls?

**Difficulty: Intermediate**

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

[Back to Top](#table-of-contents)

---

### Q9: How do you identify and fix a 'Memory Leak' caused by a detached event listener in a React component?

**Difficulty: Intermediate**

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

[Back to Top](#table-of-contents)

---

### Q10: How do you use `requestAnimationFrame` to create smooth, 60fps animations instead of using `setInterval`?

**Difficulty: Intermediate**

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

[Back to Top](#table-of-contents)

---

### Q11: How do you optimize a large React context that causes unnecessary re-renders in consumer components?

**Difficulty: Advanced**

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

[Back to Top](#table-of-contents)

---

### Q12: How do you use the 'Performance API' to measure the execution time of a specific function?

**Difficulty: Beginner**

**Solution: `performance.now()` or `performance.mark()`**

```javascript
const start = performance.now();

heavyFunction();

const end = performance.now();
console.log(`Execution time: ${end - start} ms`);
```

[Back to Top](#table-of-contents)

---

### Q13: How do you configure Webpack to use 'Tree Shaking' to remove unused code from your production bundle?

**Difficulty: Intermediate**

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

[Back to Top](#table-of-contents)

---

### Q14: How do you implement 'Resource Hints' (dns-prefetch, preconnect) to speed up third-party API connections?

**Difficulty: Intermediate**

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

[Back to Top](#table-of-contents)

---

### Q15: How do you optimize CSS delivery to avoid 'Render Blocking' resources?

**Difficulty: Advanced**

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

[Back to Top](#table-of-contents)

---

### Q16: How do you minimize main thread work to improve INP?

**Difficulty: Expert**

**Answer:**

To minimize main thread work to improve INP, you should use specific performance techniques or APIs appropriate for expert tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q17: How do you use the Scheduler API (scheduler.yield) to break up long tasks?

**Difficulty: Advanced**

**Answer:**

To use the Scheduler API (scheduler.yield) to break up long tasks, you should use specific performance techniques or APIs appropriate for advanced tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q18: How do you optimize font loading using font-display: swap?

**Difficulty: Beginner**

**Answer:**

To optimize font loading using font-display: swap, you should use specific performance techniques or APIs appropriate for beginner tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q19: How do you prevent Layout Shifts from dynamic ads?

**Difficulty: Intermediate**

**Answer:**

To prevent Layout Shifts from dynamic ads, you should use specific performance techniques or APIs appropriate for intermediate tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q20: How do you use HTTP/2 Server Push (or why avoid it)?

**Difficulty: Advanced**

**Answer:**

To use HTTP/2 Server Push (or why avoid it), you should use specific performance techniques or APIs appropriate for advanced tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q21: How do you implement a Service Worker for offline caching?

**Difficulty: Intermediate**

**Answer:**

To implement a Service Worker for offline caching, you should use specific performance techniques or APIs appropriate for intermediate tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q22: How do you use the Cache API within a Service Worker?

**Difficulty: Intermediate**

**Answer:**

To use the Cache API within a Service Worker, you should use specific performance techniques or APIs appropriate for intermediate tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q23: How do you configure HTTP Cache-Control headers for static assets?

**Difficulty: Intermediate**

**Answer:**

To configure HTTP Cache-Control headers for static assets, you should use specific performance techniques or APIs appropriate for intermediate tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q24: How do you use the Vary header to serve different content versions?

**Difficulty: Advanced**

**Answer:**

To use the Vary header to serve different content versions, you should use specific performance techniques or APIs appropriate for advanced tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q25: How do you implement ETags for conditional requests?

**Difficulty: Intermediate**

**Answer:**

To implement ETags for conditional requests, you should use specific performance techniques or APIs appropriate for intermediate tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q26: How do you optimize SVG assets using SVGO?

**Difficulty: Beginner**

**Answer:**

To optimize SVG assets using SVGO, you should use specific performance techniques or APIs appropriate for beginner tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q27: How do you serve responsive images using `srcset` and `sizes`?

**Difficulty: Beginner**

**Answer:**

To serve responsive images using `srcset` and `sizes`, you should use specific performance techniques or APIs appropriate for beginner tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q28: How do you use the `<picture>` element for art direction?

**Difficulty: Beginner**

**Answer:**

To use the `<picture>` element for art direction, you should use specific performance techniques or APIs appropriate for beginner tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q29: How do you convert images to WebP or AVIF formats?

**Difficulty: Beginner**

**Answer:**

To convert images to WebP or AVIF formats, you should use specific performance techniques or APIs appropriate for beginner tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q30: How do you optimize video delivery using HLS or DASH?

**Difficulty: Advanced**

**Answer:**

To optimize video delivery using HLS or DASH, you should use specific performance techniques or APIs appropriate for advanced tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q31: How do you use the `poster` attribute for video placeholders?

**Difficulty: Beginner**

**Answer:**

To use the `poster` attribute for video placeholders, you should use specific performance techniques or APIs appropriate for beginner tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q32: How do you lazy load third-party scripts (Google Analytics, etc.)?

**Difficulty: Intermediate**

**Answer:**

To lazy load third-party scripts (Google Analytics, etc.), you should use specific performance techniques or APIs appropriate for intermediate tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q33: How do you use the `defer` vs `async` attributes on script tags?

**Difficulty: Beginner**

**Answer:**

To use the `defer` vs `async` attributes on script tags, you should use specific performance techniques or APIs appropriate for beginner tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q34: How do you optimize Google Fonts performance?

**Difficulty: Intermediate**

**Answer:**

To optimize Google Fonts performance, you should use specific performance techniques or APIs appropriate for intermediate tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q35: How do you reduce the impact of A/B testing scripts on LCP?

**Difficulty: Advanced**

**Answer:**

To reduce the impact of A/B testing scripts on LCP, you should use specific performance techniques or APIs appropriate for advanced tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q36: How do you use the Coverage tab in Chrome DevTools to find unused code?

**Difficulty: Intermediate**

**Answer:**

To use the Coverage tab in Chrome DevTools to find unused code, you should use specific performance techniques or APIs appropriate for intermediate tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q37: How do you use the Performance tab to analyze flame charts?

**Difficulty: Intermediate**

**Answer:**

To use the Performance tab to analyze flame charts, you should use specific performance techniques or APIs appropriate for intermediate tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q38: How do you use the Network tab to debug waterfall requests?

**Difficulty: Beginner**

**Answer:**

To use the Network tab to debug waterfall requests, you should use specific performance techniques or APIs appropriate for beginner tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q39: How do you detect and fix 'forced synchronous layout'?

**Difficulty: Advanced**

**Answer:**

To detect and fix 'forced synchronous layout', you should use specific performance techniques or APIs appropriate for advanced tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q40: How do you use `will-change` CSS property correctly?

**Difficulty: Intermediate**

**Answer:**

To use `will-change` CSS property correctly, you should use specific performance techniques or APIs appropriate for intermediate tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q41: How do you optimize CSS selectors to reduce matching time?

**Difficulty: Advanced**

**Answer:**

To optimize CSS selectors to reduce matching time, you should use specific performance techniques or APIs appropriate for advanced tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q42: How do you use CSS containment (`contain` property) for rendering performance?

**Difficulty: Expert**

**Answer:**

To use CSS containment (`contain` property) for rendering performance, you should use specific performance techniques or APIs appropriate for expert tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q43: How do you reduce the complexity of the DOM tree?

**Difficulty: Intermediate**

**Answer:**

To reduce the complexity of the DOM tree, you should use specific performance techniques or APIs appropriate for intermediate tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q44: How do you optimize React `re-renders` using `React.memo`?

**Difficulty: Intermediate**

**Answer:**

To optimize React `re-renders` using `React.memo`, you should use specific performance techniques or APIs appropriate for intermediate tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q45: How do you use `useCallback` to prevent function recreation?

**Difficulty: Intermediate**

**Answer:**

To use `useCallback` to prevent function recreation, you should use specific performance techniques or APIs appropriate for intermediate tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q46: How do you virtualize a large data grid/table?

**Difficulty: Advanced**

**Answer:**

To virtualize a large data grid/table, you should use specific performance techniques or APIs appropriate for advanced tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q47: How do you optimize list rendering with `key` prop?

**Difficulty: Beginner**

**Answer:**

To optimize list rendering with `key` prop, you should use specific performance techniques or APIs appropriate for beginner tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q48: How do you prevent expensive calculations with `useMemo`?

**Difficulty: Beginner**

**Answer:**

To prevent expensive calculations with `useMemo`, you should use specific performance techniques or APIs appropriate for beginner tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q49: How do you use React Profiler to identify slow components?

**Difficulty: Intermediate**

**Answer:**

To use React Profiler to identify slow components, you should use specific performance techniques or APIs appropriate for intermediate tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q50: How do you code split a React app using route-based chunks?

**Difficulty: Intermediate**

**Answer:**

To code split a React app using route-based chunks, you should use specific performance techniques or APIs appropriate for intermediate tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q51: How do you prefetch resources on link hover?

**Difficulty: Intermediate**

**Answer:**

To prefetch resources on link hover, you should use specific performance techniques or APIs appropriate for intermediate tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q52: How do you use the Network Information API to adapt to slow connections?

**Difficulty: Advanced**

**Answer:**

To use the Network Information API to adapt to slow connections, you should use specific performance techniques or APIs appropriate for advanced tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q53: How do you implement the PRPL pattern?

**Difficulty: Advanced**

**Answer:**

To implement the PRPL pattern, you should use specific performance techniques or APIs appropriate for advanced tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q54: How do you optimize hydration in SSR applications?

**Difficulty: Advanced**

**Answer:**

To optimize hydration in SSR applications, you should use specific performance techniques or APIs appropriate for advanced tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q55: How do you use Selective Hydration in React 18?

**Difficulty: Expert**

**Answer:**

To use Selective Hydration in React 18, you should use specific performance techniques or APIs appropriate for expert tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q56: How do you reduce Time to First Byte (TTFB) on the server?

**Difficulty: Intermediate**

**Answer:**

To reduce Time to First Byte (TTFB) on the server, you should use specific performance techniques or APIs appropriate for intermediate tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q57: How do you configure Gzip or Brotli compression on the server?

**Difficulty: Beginner**

**Answer:**

To configure Gzip or Brotli compression on the server, you should use specific performance techniques or APIs appropriate for beginner tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q58: How do you optimize database queries to reduce server response time?

**Difficulty: Intermediate**

**Answer:**

To optimize database queries to reduce server response time, you should use specific performance techniques or APIs appropriate for intermediate tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q59: How do you use a CDN to serve static assets?

**Difficulty: Beginner**

**Answer:**

To use a CDN to serve static assets, you should use specific performance techniques or APIs appropriate for beginner tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q60: How do you configure HTTP/3 (QUIC) for faster connections?

**Difficulty: Advanced**

**Answer:**

To configure HTTP/3 (QUIC) for faster connections, you should use specific performance techniques or APIs appropriate for advanced tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q61: How do you monitor Real User Metrics (RUM) using Vitals library?

**Difficulty: Intermediate**

**Answer:**

To monitor Real User Metrics (RUM) using Vitals library, you should use specific performance techniques or APIs appropriate for intermediate tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q62: How do you set up a Performance Budget in CI/CD pipeline?

**Difficulty: Advanced**

**Answer:**

To set up a Performance Budget in CI/CD pipeline, you should use specific performance techniques or APIs appropriate for advanced tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q63: How do you use Lighthouse CI to prevent regressions?

**Difficulty: Intermediate**

**Answer:**

To use Lighthouse CI to prevent regressions, you should use specific performance techniques or APIs appropriate for intermediate tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q64: How do you optimize a Single Page Application (SPA) initial load?

**Difficulty: Intermediate**

**Answer:**

To optimize a Single Page Application (SPA) initial load, you should use specific performance techniques or APIs appropriate for intermediate tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q65: How do you optimize Next.js Image component usage?

**Difficulty: Intermediate**

**Answer:**

To optimize Next.js Image component usage, you should use specific performance techniques or APIs appropriate for intermediate tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q66: How do you optimize font subsetting to reduce file size?

**Difficulty: Advanced**

**Answer:**

To optimize font subsetting to reduce file size, you should use specific performance techniques or APIs appropriate for advanced tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q67: How do you avoid chain requests (waterfalls) in critical path?

**Difficulty: Intermediate**

**Answer:**

To avoid chain requests (waterfalls) in critical path, you should use specific performance techniques or APIs appropriate for intermediate tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q68: How do you inline small assets (Base64) to save requests?

**Difficulty: Beginner**

**Answer:**

To inline small assets (Base64) to save requests, you should use specific performance techniques or APIs appropriate for beginner tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q69: How do you use Resource Hints for external domains?

**Difficulty: Intermediate**

**Answer:**

To use Resource Hints for external domains, you should use specific performance techniques or APIs appropriate for intermediate tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q70: How do you optimize the Critical Rendering Path?

**Difficulty: Advanced**

**Answer:**

To optimize the Critical Rendering Path, you should use specific performance techniques or APIs appropriate for advanced tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q71: How do you reduce the size of JSON API responses?

**Difficulty: Intermediate**

**Answer:**

To reduce the size of JSON API responses, you should use specific performance techniques or APIs appropriate for intermediate tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q72: How do you use Protocol Buffers instead of JSON for smaller payloads?

**Difficulty: Expert**

**Answer:**

To use Protocol Buffers instead of JSON for smaller payloads, you should use specific performance techniques or APIs appropriate for expert tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q73: How do you optimize GraphQL queries to fetch only needed fields?

**Difficulty: Intermediate**

**Answer:**

To optimize GraphQL queries to fetch only needed fields, you should use specific performance techniques or APIs appropriate for intermediate tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q74: How do you batch multiple API requests into one?

**Difficulty: Intermediate**

**Answer:**

To batch multiple API requests into one, you should use specific performance techniques or APIs appropriate for intermediate tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q75: How do you use a skeleton screen to improve perceived performance?

**Difficulty: Beginner**

**Answer:**

To use a skeleton screen to improve perceived performance, you should use specific performance techniques or APIs appropriate for beginner tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q76: How do you implement optimistic UI updates?

**Difficulty: Intermediate**

**Answer:**

To implement optimistic UI updates, you should use specific performance techniques or APIs appropriate for intermediate tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q77: How do you offload image processing to a serverless function?

**Difficulty: Advanced**

**Answer:**

To offload image processing to a serverless function, you should use specific performance techniques or APIs appropriate for advanced tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q78: How do you use `requestIdleCallback` for low-priority tasks?

**Difficulty: Intermediate**

**Answer:**

To use `requestIdleCallback` for low-priority tasks, you should use specific performance techniques or APIs appropriate for intermediate tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q79: How do you optimize garbage collection by avoiding object churn?

**Difficulty: Expert**

**Answer:**

To optimize garbage collection by avoiding object churn, you should use specific performance techniques or APIs appropriate for expert tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q80: How do you profile memory usage using Heap Snapshots?

**Difficulty: Advanced**

**Answer:**

To profile memory usage using Heap Snapshots, you should use specific performance techniques or APIs appropriate for advanced tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q81: How do you detect detached DOM nodes causing memory leaks?

**Difficulty: Advanced**

**Answer:**

To detect detached DOM nodes causing memory leaks, you should use specific performance techniques or APIs appropriate for advanced tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q82: How do you optimize canvas rendering performance?

**Difficulty: Advanced**

**Answer:**

To optimize canvas rendering performance, you should use specific performance techniques or APIs appropriate for advanced tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q83: How do you use OffscreenCanvas for background rendering?

**Difficulty: Expert**

**Answer:**

To use OffscreenCanvas for background rendering, you should use specific performance techniques or APIs appropriate for expert tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q84: How do you optimize WebGL rendering?

**Difficulty: Expert**

**Answer:**

To optimize WebGL rendering, you should use specific performance techniques or APIs appropriate for expert tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q85: How do you reduce battery usage by pausing background animations?

**Difficulty: Intermediate**

**Answer:**

To reduce battery usage by pausing background animations, you should use specific performance techniques or APIs appropriate for intermediate tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q86: How do you use the Page Visibility API to pause tasks?

**Difficulty: Intermediate**

**Answer:**

To use the Page Visibility API to pause tasks, you should use specific performance techniques or APIs appropriate for intermediate tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q87: How do you optimize iframe loading using `loading='lazy'`?

**Difficulty: Beginner**

**Answer:**

To optimize iframe loading using `loading='lazy'`, you should use specific performance techniques or APIs appropriate for beginner tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q88: How do you isolate third-party widgets in iframes?

**Difficulty: Intermediate**

**Answer:**

To isolate third-party widgets in iframes, you should use specific performance techniques or APIs appropriate for intermediate tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q89: How do you use the Shadow DOM for style encapsulation/perf?

**Difficulty: Advanced**

**Answer:**

To use the Shadow DOM for style encapsulation/perf, you should use specific performance techniques or APIs appropriate for advanced tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q90: How do you optimize regex patterns to avoid ReDoS?

**Difficulty: Advanced**

**Answer:**

To optimize regex patterns to avoid ReDoS, you should use specific performance techniques or APIs appropriate for advanced tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q91: How do you use GPU acceleration for animations?

**Difficulty: Intermediate**

**Answer:**

To use GPU acceleration for animations, you should use specific performance techniques or APIs appropriate for intermediate tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q92: How do you avoid using `@import` in CSS?

**Difficulty: Beginner**

**Answer:**

To avoid using `@import` in CSS, you should use specific performance techniques or APIs appropriate for beginner tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q93: How do you bundle CSS vs splitting CSS optimization trade-offs?

**Difficulty: Advanced**

**Answer:**

To bundle CSS vs splitting CSS optimization trade-offs, you should use specific performance techniques or APIs appropriate for advanced tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q94: How do you use the Back/Forward Cache (bfcache)?

**Difficulty: Intermediate**

**Answer:**

To use the Back/Forward Cache (bfcache), you should use specific performance techniques or APIs appropriate for intermediate tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q95: How do you optimize touch event listeners with `passive: true`?

**Difficulty: Intermediate**

**Answer:**

To optimize touch event listeners with `passive: true`, you should use specific performance techniques or APIs appropriate for intermediate tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q96: How do you reduce cookie size to lower request overhead?

**Difficulty: Beginner**

**Answer:**

To reduce cookie size to lower request overhead, you should use specific performance techniques or APIs appropriate for beginner tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q97: How do you use domain sharding (legacy) vs HTTP/2 multiplexing?

**Difficulty: Intermediate**

**Answer:**

To use domain sharding (legacy) vs HTTP/2 multiplexing, you should use specific performance techniques or APIs appropriate for intermediate tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q98: How do you optimize for low-end devices?

**Difficulty: Intermediate**

**Answer:**

To optimize for low-end devices, you should use specific performance techniques or APIs appropriate for intermediate tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q99: How do you measure TTI (Time to Interactive)?

**Difficulty: Intermediate**

**Answer:**

To measure TTI (Time to Interactive), you should use specific performance techniques or APIs appropriate for intermediate tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q100: How do you measure TBT (Total Blocking Time)?

**Difficulty: Intermediate**

**Answer:**

To measure TBT (Total Blocking Time), you should use specific performance techniques or APIs appropriate for intermediate tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q101: How do you measure Speed Index?

**Difficulty: Intermediate**

**Answer:**

To measure Speed Index, you should use specific performance techniques or APIs appropriate for intermediate tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q102: How do you automate performance testing with Puppeteer/Playwright?

**Difficulty: Advanced**

**Answer:**

To automate performance testing with Puppeteer/Playwright, you should use specific performance techniques or APIs appropriate for advanced tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q103: How do you use `content-visibility: auto` to skip rendering off-screen content?

**Difficulty: Intermediate**

**Answer:**

To use `content-visibility: auto` to skip rendering off-screen content, you should use specific performance techniques or APIs appropriate for intermediate tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q104: How do you optimize string concatenation in tight loops?

**Difficulty: Beginner**

**Answer:**

To optimize string concatenation in tight loops, you should use specific performance techniques or APIs appropriate for beginner tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

### Q105: How do you use Bitwise operators for high-perf math (micro-optimization)?

**Difficulty: Expert**

**Answer:**

To use Bitwise operators for high-perf math (micro-optimization), you should use specific performance techniques or APIs appropriate for expert tasks. Provide a clear code example or configuration snippet demonstrating the optimization.

[Back to Top](#table-of-contents)

---

