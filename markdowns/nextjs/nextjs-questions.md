<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/nextjs-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>Next.js Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for Next.js developers</b></p>
</div>

---

## Table of Contents

1. [How do you choose between Static Site Generation (SSG) and Server-Side Rendering (SSR) for a dynamic page?](#q1-how-do-you-choose-between-static-site-generation-ssg-and-server-side-rendering-ssr-for-a-dynamic-page) <span class="intermediate">Intermediate</span>
2. [How do you implement Incremental Static Regeneration (ISR) to update static pages without a full rebuild?](#q2-how-do-you-implement-incremental-static-regeneration-isr-to-update-static-pages-without-a-full-rebuild) <span class="intermediate">Intermediate</span>
3. [How do you optimize images for performance using the Next.js Image component?](#q3-how-do-you-optimize-images-for-performance-using-the-next.js-image-component) <span class="beginner">Beginner</span>
4. [How do you implement Server Actions to handle form submissions in the App Router?](#q4-how-do-you-implement-server-actions-to-handle-form-submissions-in-the-app-router) <span class="advanced">Advanced</span>
5. [How do you optimize font loading using `next/font`?](#q5-how-do-you-optimize-font-loading-using-nextfont) <span class="intermediate">Intermediate</span>
6. [How do you create a custom 404 error page in the Pages Router?](#q6-how-do-you-create-a-custom-404-error-page-in-the-pages-router) <span class="beginner">Beginner</span>
7. [How do you handle authentication protection in Middleware?](#q7-how-do-you-handle-authentication-protection-in-middleware) <span class="advanced">Advanced</span>
8. [How do you dynamic import a heavy component to reduce initial bundle size?](#q8-how-do-you-dynamic-import-a-heavy-component-to-reduce-initial-bundle-size) <span class="intermediate">Intermediate</span>
9. [How do you generate dynamic sitemaps for SEO in Next.js?](#q9-how-do-you-generate-dynamic-sitemaps-for-seo-in-next.js) <span class="advanced">Advanced</span>
10. [How do you implement API Routes to handle backend logic?](#q10-how-do-you-implement-api-routes-to-handle-backend-logic) <span class="beginner">Beginner</span>
11. [How do you share layouts across multiple pages in the App Router?](#q11-how-do-you-share-layouts-across-multiple-pages-in-the-app-router) <span class="intermediate">Intermediate</span>
12. [How do you optimize metadata (SEO tags) dynamically for each page?](#q12-how-do-you-optimize-metadata-seo-tags-dynamically-for-each-page) <span class="intermediate">Intermediate</span>
13. [How do you configure environment variables securely?](#q13-how-do-you-configure-environment-variables-securely) <span class="beginner">Beginner</span>
14. [How do you deploy a Next.js app to a Docker container (Standalone mode)?](#q14-how-do-you-deploy-a-next.js-app-to-a-docker-container-standalone-mode) <span class="advanced">Advanced</span>
15. [How do you handle loading states in the App Router?](#q15-how-do-you-handle-loading-states-in-the-app-router) <span class="beginner">Beginner</span>
16. [How do you implement Parallel Routes for complex layouts (e.g. Dashboards)?](#q16-how-do-you-implement-parallel-routes-for-complex-layouts-e.g.-dashboards) <span class="advanced">Advanced</span>
17. [How do you implement Intercepting Routes (e.g. Modals)?](#q17-how-do-you-implement-intercepting-routes-e.g.-modals) <span class="advanced">Advanced</span>
18. [How do you handle redirects in Server Components?](#q18-how-do-you-handle-redirects-in-server-components) <span class="intermediate">Intermediate</span>
19. [When should you use Client Components vs Server Components?](#q19-when-should-you-use-client-components-vs-server-components) <span class="beginner">Beginner</span>
20. [How do you revalidate cached data on-demand using Server Actions?](#q20-how-do-you-revalidate-cached-data-on-demand-using-server-actions) <span class="advanced">Advanced</span>
21. [How do you use `generateStaticParams` for dynamic SSG in the App Router?](#q21-how-do-you-use-generatestaticparams-for-dynamic-ssg-in-the-app-router) <span class="intermediate">Intermediate</span>
22. [What is the difference between `layout.js` and `template.js`?](#q22-what-is-the-difference-between-layout.js-and-template.js) <span class="intermediate">Intermediate</span>
23. [How do you handle errors in the App Router using `error.js`?](#q23-how-do-you-handle-errors-in-the-app-router-using-error.js) <span class="intermediate">Intermediate</span>
24. [How do you implement Route Handlers for backend logic in App Router?](#q24-how-do-you-implement-route-handlers-for-backend-logic-in-app-router) <span class="intermediate">Intermediate</span>
25. [When should you use the Edge Runtime?](#q25-when-should-you-use-the-edge-runtime) <span class="advanced">Advanced</span>
26. [How do you highlight the active link using `useSelectedLayoutSegment`?](#q26-how-do-you-highlight-the-active-link-using-useselectedlayoutsegment) <span class="intermediate">Intermediate</span>
27. [How do you optimize third-party scripts using `next/script`?](#q27-how-do-you-optimize-third-party-scripts-using-nextscript) <span class="beginner">Beginner</span>
28. [How do you implement Draft Mode for CMS previews?](#q28-how-do-you-implement-draft-mode-for-cms-previews) <span class="advanced">Advanced</span>
29. [What is the difference between Request Memoization and the Data Cache?](#q29-what-is-the-difference-between-request-memoization-and-the-data-cache) <span class="advanced">Advanced</span>
30. [How do you revalidate specific data cache entries using Tags?](#q30-how-do-you-revalidate-specific-data-cache-entries-using-tags) <span class="advanced">Advanced</span>
31. [How do you implement Internationalization (i18n) in the App Router?](#q31-how-do-you-implement-internationalization-i18n-in-the-app-router) <span class="advanced">Advanced</span>
32. [What is Streaming and how does it improve UX?](#q32-what-is-streaming-and-how-does-it-improve-ux) <span class="intermediate">Intermediate</span>
33. [How do you generate dynamic Metadata for SEO?](#q33-how-do-you-generate-dynamic-metadata-for-seo) <span class="intermediate">Intermediate</span>
34. [How do you protect routes from unauthorized access using Middleware?](#q34-how-do-you-protect-routes-from-unauthorized-access-using-middleware) <span class="intermediate">Intermediate</span>
35. [What is the purpose of `output: 'standalone'` in `next.config.js`?](#q35-what-is-the-purpose-of-output:-standalone-in-next.config.js) <span class="advanced">Advanced</span>
36. [How do you use React Server Components (RSC) effectively?](#q36-how-do-you-use-react-server-components-rsc-effectively) <span class="beginner">Beginner</span>
37. [How do you handle static assets like images and fonts?](#q37-how-do-you-handle-static-assets-like-images-and-fonts) <span class="beginner">Beginner</span>
38. [How do you implement Infinite Scroll in Next.js?](#q38-how-do-you-implement-infinite-scroll-in-next.js) <span class="intermediate">Intermediate</span>
39. [What is Turbopack?](#q39-what-is-turbopack) <span class="beginner">Beginner</span>
40. [How do you debug Core Web Vitals in Next.js?](#q40-how-do-you-debug-core-web-vitals-in-next.js) <span class="intermediate">Intermediate</span>
41. [How do you generate dynamic Open Graph images using `ImageResponse`?](#q41-how-do-you-generate-dynamic-open-graph-images-using-imageresponse) <span class="advanced">Advanced</span>
42. [How do you implement Partial Prerendering (PPR)?](#q42-how-do-you-implement-partial-prerendering-ppr) <span class="advanced">Advanced</span>
43. [How do you configure Content Security Policy (CSP) in Next.js?](#q43-how-do-you-configure-content-security-policy-csp-in-next.js) <span class="advanced">Advanced</span>
44. [How do you unit test Server Components with Jest?](#q44-how-do-you-unit-test-server-components-with-jest) <span class="intermediate">Intermediate</span>
45. [How do you implement E2E testing with Playwright in Next.js?](#q45-how-do-you-implement-e2e-testing-with-playwright-in-next.js) <span class="intermediate">Intermediate</span>
46. [How do you use Multi-Zones to split a large Next.js app?](#q46-how-do-you-use-multi-zones-to-split-a-large-next.js-app) <span class="advanced">Advanced</span>
47. [How do you run Cron Jobs in a Next.js app (Vercel Cron)?](#q47-how-do-you-run-cron-jobs-in-a-next.js-app-vercel-cron) <span class="intermediate">Intermediate</span>
48. [How do you prevent specific pages from being indexed by search engines?](#q48-how-do-you-prevent-specific-pages-from-being-indexed-by-search-engines) <span class="beginner">Beginner</span>
49. [How do you use `useOptimistic` for instant UI updates?](#q49-how-do-you-use-useoptimistic-for-instant-ui-updates) <span class="advanced">Advanced</span>
50. [How do you configure a custom build output directory?](#q50-how-do-you-configure-a-custom-build-output-directory) <span class="intermediate">Intermediate</span>
51. [How do you handle Next.js state management in large scale applications?](#q51-how-do-you-handle-next.js-state-management-in-large-scale-applications) <span class="advanced">Advanced</span>
52. [How do you perform Next.js data validation in microservices?](#q52-how-do-you-perform-next.js-data-validation-in-microservices) <span class="beginner">Beginner</span>
53. [How do you automate Next.js deployment for mobile devices?](#q53-how-do-you-automate-next.js-deployment-for-mobile-devices) <span class="advanced">Advanced</span>
54. [How do you handle Next.js concurrency issues in legacy systems?](#q54-how-do-you-handle-next.js-concurrency-issues-in-legacy-systems) <span class="advanced">Advanced</span>
55. [How do you implement Next.js caching in cloud infrastructure?](#q55-how-do-you-implement-next.js-caching-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
56. [How do you manage Next.js configuration for real-time systems?](#q56-how-do-you-manage-next.js-configuration-for-real-time-systems) <span class="beginner">Beginner</span>
57. [How do you handle Next.js internationalization (i18n) in distributed systems?](#q57-how-do-you-handle-next.js-internationalization-i18n-in-distributed-systems) <span class="intermediate">Intermediate</span>
58. [How do you ensure Next.js accessibility (a11y) in high-traffic sites?](#q58-how-do-you-ensure-next.js-accessibility-a11y-in-high-traffic-sites) <span class="beginner">Beginner</span>
59. [How do you optimize Next.js network requests in embedded systems?](#q59-how-do-you-optimize-next.js-network-requests-in-embedded-systems) <span class="advanced">Advanced</span>
60. [How do you handle Next.js performance optimization for production environments?](#q60-how-do-you-handle-next.js-performance-optimization-for-production-environments) <span class="advanced">Advanced</span>
61. [What are the security implications of Next.js in large scale applications?](#q61-what-are-the-security-implications-of-next.js-in-large-scale-applications) <span class="intermediate">Intermediate</span>
62. [How do you debug Next.js memory leaks in microservices?](#q62-how-do-you-debug-next.js-memory-leaks-in-microservices) <span class="advanced">Advanced</span>
63. [Best practices for Next.js code organization in mobile devices?](#q63-best-practices-for-next.js-code-organization-in-mobile-devices) <span class="beginner">Beginner</span>
64. [How do you implement Next.js error handling for legacy systems?](#q64-how-do-you-implement-next.js-error-handling-for-legacy-systems) <span class="intermediate">Intermediate</span>
65. [How do you test Next.js functionality in cloud infrastructure?](#q65-how-do-you-test-next.js-functionality-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
66. [How do you handle Next.js state management in real-time systems?](#q66-how-do-you-handle-next.js-state-management-in-real-time-systems) <span class="advanced">Advanced</span>
67. [How do you perform Next.js data validation in distributed systems?](#q67-how-do-you-perform-next.js-data-validation-in-distributed-systems) <span class="beginner">Beginner</span>
68. [How do you automate Next.js deployment for high-traffic sites?](#q68-how-do-you-automate-next.js-deployment-for-high-traffic-sites) <span class="advanced">Advanced</span>
69. [How do you handle Next.js concurrency issues in embedded systems?](#q69-how-do-you-handle-next.js-concurrency-issues-in-embedded-systems) <span class="advanced">Advanced</span>
70. [How do you implement Next.js caching in production environments?](#q70-how-do-you-implement-next.js-caching-in-production-environments) <span class="intermediate">Intermediate</span>
71. [How do you manage Next.js configuration for large scale applications?](#q71-how-do-you-manage-next.js-configuration-for-large-scale-applications) <span class="beginner">Beginner</span>
72. [How do you handle Next.js internationalization (i18n) in microservices?](#q72-how-do-you-handle-next.js-internationalization-i18n-in-microservices) <span class="intermediate">Intermediate</span>
73. [How do you ensure Next.js accessibility (a11y) in mobile devices?](#q73-how-do-you-ensure-next.js-accessibility-a11y-in-mobile-devices) <span class="beginner">Beginner</span>
74. [How do you optimize Next.js network requests in legacy systems?](#q74-how-do-you-optimize-next.js-network-requests-in-legacy-systems) <span class="advanced">Advanced</span>
75. [How do you handle Next.js performance optimization for cloud infrastructure?](#q75-how-do-you-handle-next.js-performance-optimization-for-cloud-infrastructure) <span class="advanced">Advanced</span>
76. [What are the security implications of Next.js in real-time systems?](#q76-what-are-the-security-implications-of-next.js-in-real-time-systems) <span class="intermediate">Intermediate</span>
77. [How do you debug Next.js memory leaks in distributed systems?](#q77-how-do-you-debug-next.js-memory-leaks-in-distributed-systems) <span class="advanced">Advanced</span>
78. [Best practices for Next.js code organization in high-traffic sites?](#q78-best-practices-for-next.js-code-organization-in-high-traffic-sites) <span class="beginner">Beginner</span>
79. [How do you implement Next.js error handling for embedded systems?](#q79-how-do-you-implement-next.js-error-handling-for-embedded-systems) <span class="intermediate">Intermediate</span>
80. [How do you test Next.js functionality in production environments?](#q80-how-do-you-test-next.js-functionality-in-production-environments) <span class="intermediate">Intermediate</span>
81. [How do you handle Next.js state management in large scale applications?](#q81-how-do-you-handle-next.js-state-management-in-large-scale-applications) <span class="advanced">Advanced</span>
82. [How do you perform Next.js data validation in microservices?](#q82-how-do-you-perform-next.js-data-validation-in-microservices) <span class="beginner">Beginner</span>
83. [How do you automate Next.js deployment for mobile devices?](#q83-how-do-you-automate-next.js-deployment-for-mobile-devices) <span class="advanced">Advanced</span>
84. [How do you handle Next.js concurrency issues in legacy systems?](#q84-how-do-you-handle-next.js-concurrency-issues-in-legacy-systems) <span class="advanced">Advanced</span>
85. [How do you implement Next.js caching in cloud infrastructure?](#q85-how-do-you-implement-next.js-caching-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
86. [How do you manage Next.js configuration for real-time systems?](#q86-how-do-you-manage-next.js-configuration-for-real-time-systems) <span class="beginner">Beginner</span>
87. [How do you handle Next.js internationalization (i18n) in distributed systems?](#q87-how-do-you-handle-next.js-internationalization-i18n-in-distributed-systems) <span class="intermediate">Intermediate</span>
88. [How do you ensure Next.js accessibility (a11y) in high-traffic sites?](#q88-how-do-you-ensure-next.js-accessibility-a11y-in-high-traffic-sites) <span class="beginner">Beginner</span>
89. [How do you optimize Next.js network requests in embedded systems?](#q89-how-do-you-optimize-next.js-network-requests-in-embedded-systems) <span class="advanced">Advanced</span>
90. [How do you handle Next.js performance optimization for production environments?](#q90-how-do-you-handle-next.js-performance-optimization-for-production-environments) <span class="advanced">Advanced</span>
91. [What are the security implications of Next.js in large scale applications?](#q91-what-are-the-security-implications-of-next.js-in-large-scale-applications) <span class="intermediate">Intermediate</span>
92. [How do you debug Next.js memory leaks in microservices?](#q92-how-do-you-debug-next.js-memory-leaks-in-microservices) <span class="advanced">Advanced</span>
93. [Best practices for Next.js code organization in mobile devices?](#q93-best-practices-for-next.js-code-organization-in-mobile-devices) <span class="beginner">Beginner</span>
94. [How do you implement Next.js error handling for legacy systems?](#q94-how-do-you-implement-next.js-error-handling-for-legacy-systems) <span class="intermediate">Intermediate</span>
95. [How do you test Next.js functionality in cloud infrastructure?](#q95-how-do-you-test-next.js-functionality-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
96. [How do you handle Next.js state management in real-time systems?](#q96-how-do-you-handle-next.js-state-management-in-real-time-systems) <span class="advanced">Advanced</span>
97. [How do you perform Next.js data validation in distributed systems?](#q97-how-do-you-perform-next.js-data-validation-in-distributed-systems) <span class="beginner">Beginner</span>
98. [How do you automate Next.js deployment for high-traffic sites?](#q98-how-do-you-automate-next.js-deployment-for-high-traffic-sites) <span class="advanced">Advanced</span>
99. [How do you handle Next.js concurrency issues in embedded systems?](#q99-how-do-you-handle-next.js-concurrency-issues-in-embedded-systems) <span class="advanced">Advanced</span>
100. [How do you implement Next.js caching in production environments?](#q100-how-do-you-implement-next.js-caching-in-production-environments) <span class="intermediate">Intermediate</span>

---

<a id="q1"></a>
### Q1: How do you choose between Static Site Generation (SSG) and Server-Side Rendering (SSR) for a dynamic page?

**Difficulty**: Intermediate

**Strategy:**
Use **SSG** (`getStaticProps`) if data is available at build time and doesn't change often (e.g., blog posts, marketing pages).
Use **SSR** (`getServerSideProps` or App Router dynamic fetch) if data changes on every request or requires user-specific data (e.g., personalized dashboard).

**Code Example:**

```javascript
// SSG (Build time)
export async function getStaticProps() {
  const data = await fetchData();
  return { props: { data } };
}

// SSR (Request time)
export async function getServerSideProps(context) {
  const data = await fetchData(context.params.id);
  return { props: { data } };
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q2"></a>
### Q2: How do you implement Incremental Static Regeneration (ISR) to update static pages without a full rebuild?

**Difficulty**: Intermediate

**Strategy:**
Return a `revalidate` property (in seconds) from `getStaticProps`. Next.js will serve the cached page, then regenerate it in the background for the next request if the timer has expired.

**Code Example:**

```javascript
export async function getStaticProps() {
  const posts = await getPosts();
  return {
    props: { posts },
    revalidate: 60, // Re-generate at most once every 60 seconds
  };
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q3"></a>
### Q3: How do you optimize images for performance using the Next.js Image component?

**Difficulty**: Beginner

**Strategy:**
Use `<Image />` from `next/image`. It automatically handles resizing, lazy loading (default), and serving modern formats (WebP/AVIF). Always provide `width`/`height` or `fill` to prevent Cumulative Layout Shift (CLS).

**Code Example:**

```jsx
import Image from "next/image";

<Image
  src="/hero.jpg"
  alt="Hero Image"
  width={800}
  height={600}
  priority // Preload LCP image
/>;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q4"></a>
### Q4: How do you implement Server Actions to handle form submissions in the App Router?

**Difficulty**: Advanced

**Strategy:**
Define an async function with the `"use server"` directive. Pass this function to the `action` prop of a `<form>`. This eliminates the need for API routes for simple mutations.

**Code Example:**

```tsx
// app/page.tsx
import { db } from "@/lib/db";

export default function Page() {
  async function createPost(formData: FormData) {
    "use server";
    const title = formData.get("title");
    await db.post.create({ data: { title } });
  }

  return (
    <form action={createPost}>
      <input name="title" />
      <button type="submit">Create</button>
    </form>
  );
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q5"></a>
### Q5: How do you optimize font loading using `next/font`?

**Difficulty**: Intermediate

**Strategy:**
Use `next/font/google` or `next/font/local`. This automatically self-hosts the fonts (zero layout shift) and removes external network requests to Google Fonts.

**Code Example:**

```tsx
import { Inter } from "next/font/google";

const inter = Inter({ subsets: ["latin"] });

export default function RootLayout({ children }) {
  return (
    <html lang="en" className={inter.className}>
      <body>{children}</body>
    </html>
  );
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q6"></a>
### Q6: How do you create a custom 404 error page in the Pages Router?

**Difficulty**: Beginner

**Strategy:**
Create a file named `404.js` (or `.tsx`) in the `pages` directory. Next.js will automatically use this component when a route is not found.

**Code Example:**

```jsx
// pages/404.js
export default function Custom404() {
  return <h1>404 - Page Not Found</h1>;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q7"></a>
### Q7: How do you handle authentication protection in Middleware?

**Difficulty**: Advanced

**Strategy:**
Create `middleware.ts` at the root. Check for a session token (cookie). If missing and the user is accessing a protected route, redirect to login.

**Code Example:**

```typescript
import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

export function middleware(request: NextRequest) {
  const token = request.cookies.get("token");

  if (!token && request.nextUrl.pathname.startsWith("/dashboard")) {
    return NextResponse.redirect(new URL("/login", request.url));
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q8"></a>
### Q8: How do you dynamic import a heavy component to reduce initial bundle size?

**Difficulty**: Intermediate

**Strategy:**
Use `next/dynamic` with `ssr: false` (if it's client-only) to lazy load the component. It will only be loaded when needed.

**Code Example:**

```jsx
import dynamic from "next/dynamic";

const HeavyChart = dynamic(() => import("../components/Chart"), {
  loading: () => <p>Loading...</p>,
  ssr: false,
});

export default function Page() {
  return <HeavyChart />;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q9"></a>
### Q9: How do you generate dynamic sitemaps for SEO in Next.js?

**Difficulty**: Advanced

**Strategy:**
In App Router, add a `sitemap.ts` (or `.js`) file in the `app` directory. Fetch dynamic routes and return an array of URL objects.

**Code Example:**

```typescript
// app/sitemap.ts
export default async function sitemap() {
  const posts = await getPosts();
  const urls = posts.map((post) => ({
    url: `https://acme.com/blog/${post.slug}`,
    lastModified: post.date,
  }));

  return [{ url: "https://acme.com", lastModified: new Date() }, ...urls];
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q10"></a>
### Q10: How do you implement API Routes to handle backend logic?

**Difficulty**: Beginner

**Strategy:**
Create files in `pages/api` (Pages Router) or `app/api/route.ts` (App Router). Export async functions for HTTP methods (GET, POST, etc.).

**Code Example (App Router):**

```typescript
// app/api/users/route.ts
import { NextResponse } from "next/server";

export async function GET() {
  const users = [{ id: 1, name: "John" }];
  return NextResponse.json(users);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q11"></a>
### Q11: How do you share layouts across multiple pages in the App Router?

**Difficulty**: Intermediate

**Strategy:**
Define a `layout.tsx` file in a directory. It wraps all page components (and nested layouts) within that directory. Use the `children` prop to render the nested content.

**Code Example:**

```tsx
// app/dashboard/layout.tsx
export default function DashboardLayout({ children }) {
  return (
    <section>
      <nav>Dashboard Nav</nav>
      {children}
    </section>
  );
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q12"></a>
### Q12: How do you optimize metadata (SEO tags) dynamically for each page?

**Difficulty**: Intermediate

**Strategy:**
In App Router, export a `generateMetadata` function from your `page.tsx`. Fetch data needed for the title/description and return a `Metadata` object.

**Code Example:**

```typescript
export async function generateMetadata({ params }) {
  const product = await getProduct(params.id);
  return {
    title: product.name,
    description: product.summary,
  };
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q13"></a>
### Q13: How do you configure environment variables securely?

**Difficulty**: Beginner

**Strategy:**
Use `.env.local` for secrets. Variables prefixed with `NEXT_PUBLIC_` are exposed to the browser. Others are server-only.

**Code Example:**

```bash
# .env.local
DB_PASS=secret123       # Server only
NEXT_PUBLIC_API_URL=... # Available in browser
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q14"></a>
### Q14: How do you deploy a Next.js app to a Docker container (Standalone mode)?

**Difficulty**: Advanced

**Strategy:**
Set `output: 'standalone'` in `next.config.js`. This reduces the image size by copying only necessary production dependencies. Use a multi-stage Dockerfile.

**Code Example:**

```javascript
// next.config.js
module.exports = {
  output: "standalone",
};
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q15"></a>
### Q15: How do you handle loading states in the App Router?

**Difficulty**: Beginner

**Strategy:**
Create a `loading.tsx` file in the same directory as your page. Next.js automatically wraps the page in a Suspense boundary and shows this component while data is fetching.

**Code Example:**

```tsx
// app/dashboard/loading.tsx
export default function Loading() {
  return <div className="spinner">Loading dashboard...</div>;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q16"></a>
### Q16: How do you implement Parallel Routes for complex layouts (e.g. Dashboards)?

**Difficulty**: Advanced

**Strategy:**
Use **Parallel Routes** by creating slots named `@folder`. Pass these slots as props to the `layout.tsx`. This allows rendering multiple pages in the same layout simultaneously.

**Code Example:**

```tsx
// app/layout.tsx
export default function Layout({ children, team, analytics }) {
  return (
    <>
      {children}
      <div className="dashboard">
        {team}
        {analytics}
      </div>
    </>
  );
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q17"></a>
### Q17: How do you implement Intercepting Routes (e.g. Modals)?

**Difficulty**: Advanced

**Strategy:**
Use **Intercepting Routes** with the `(.)` convention (e.g., `(.)photos/[id]`). This allows you to load a route within the current layout (like a modal) while soft-navigating, but show the full page on refresh.

**Code Example:**

```tsx
// app/@modal/(.)photos/[id]/page.tsx
import Modal from "@/components/Modal";

export default function PhotoModal({ params }) {
  return (
    <Modal>
      <Photo id={params.id} />
    </Modal>
  );
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q18"></a>
### Q18: How do you handle redirects in Server Components?

**Difficulty**: Intermediate

**Strategy:**
Use the `redirect` function from `next/navigation`. It throws an error that interrupts rendering and redirects the user. It can be used in Server Components, Server Actions, and Route Handlers.

**Code Example:**

```tsx
import { redirect } from "next/navigation";

async function fetchUser(id) {
  const res = await fetch(`https://api.example.com/users/${id}`);
  if (!res.ok) return undefined;
  return res.json();
}

export default async function Profile({ params }) {
  const user = await fetchUser(params.id);

  if (!user) {
    redirect("/login"); // Interrupts and redirects
  }

  return <h1>Welcome {user.name}</h1>;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q19"></a>
### Q19: When should you use Client Components vs Server Components?

**Difficulty**: Beginner

**Strategy:**
By default, all components in the App Router are **Server Components**. Add `"use client"` at the top of the file to make it a **Client Component**.

- **Server Components**: Fetching data, accessing backend resources, keeping sensitive info.
- **Client Components**: Interactivity (`onClick`, `onChange`), `useState`, `useEffect`, browser APIs.

**Code Example:**

```tsx
"use client";

import { useState } from "react";

export default function Counter() {
  const [count, setCount] = useState(0);

  return <button onClick={() => setCount(count + 1)}>{count}</button>;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q20"></a>
### Q20: How do you revalidate cached data on-demand using Server Actions?

**Difficulty**: Advanced

**Strategy:**
Use `revalidatePath` or `revalidateTag` inside a Server Action to purge cached data. This allows you to update the UI immediately after a mutation without waiting for a time-based revalidation.

**Code Example:**

```tsx
import { revalidatePath } from "next/cache";

export async function createPost(formData: FormData) {
  "use server";
  // ... create post logic ...

  revalidatePath("/posts"); // Purge cache for /posts
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

<a id="q21"></a>
### Q21: How do you use `generateStaticParams` for dynamic SSG in the App Router?

**Difficulty**: Intermediate

**Strategy:**
In the App Router, `generateStaticParams` replaces `getStaticPaths`. It returns an array of objects representing the dynamic parameters for routes that should be statically generated at build time.

**Code Example:**
// app/blog/[slug]/page.tsx
export async function generateStaticParams() {
  const posts = await getPosts();
  return posts.map((post) => ({
    slug: post.slug,
  }));
}

export default function Page({ params }) {
  return <h1>Post: {params.slug}</h1>;
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q22"></a>
### Q22: What is the difference between `layout.js` and `template.js`?

**Difficulty**: Intermediate

**Strategy:**
`layout.js` preserves state and does not re-mount on navigation between sibling routes. `template.js` creates a new instance for each child on navigation, resetting state and effects.

**Code Example:**
// app/template.tsx
import { useEffect } from 'react';

export default function Template({ children }) {
  useEffect(() => {
    console.log('Page visited (runs on every navigation)');
  }, []);
  
  return <div>{children}</div>;
}

// Use Template when you need to:
// - Log page views
// - Reset scroll position
// - Reset state on navigation

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q23"></a>
### Q23: How do you handle errors in the App Router using `error.js`?

**Difficulty**: Intermediate

**Strategy:**
`error.js` creates a React Error Boundary that wraps a route segment. It must be a Client Component (`'use client'`) and receives an `error` object and a `reset` function to attempt recovery.

**Code Example:**
'use client'; // Error components must be Client Components

import { useEffect } from 'react';

export default function Error({ error, reset }) {
  useEffect(() => {
    console.error(error);
  }, [error]);

  return (
    <div>
      <h2>Something went wrong!</h2>
      <button onClick={() => reset()}>Try again</button>
    </div>
  );
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q24"></a>
### Q24: How do you implement Route Handlers for backend logic in App Router?

**Difficulty**: Intermediate

**Strategy:**
Route Handlers are defined in `route.ts` files inside the `app` directory. They export async functions named after HTTP verbs (GET, POST, etc.).

**Code Example:**
// app/api/users/route.ts
import { NextResponse } from 'next/server';

export async function GET() {
  const data = { users: ['Alice', 'Bob'] };
  return NextResponse.json(data);
}

export async function POST(request: Request) {
  const body = await request.json();
  return NextResponse.json({ message: 'Created', body });
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q25"></a>
### Q25: When should you use the Edge Runtime?

**Difficulty**: Advanced

**Strategy:**
Use the Edge Runtime for middleware, personalized content delivery, or low-latency APIs that need to run close to the user. It has a limited API (subset of Node.js) but starts up instantly.

**Code Example:**
// app/api/edge/route.ts
export const runtime = 'edge'; // Specify runtime

export async function GET(request: Request) {
  return new Response('Hello from the Edge!');
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q26"></a>
### Q26: How do you highlight the active link using `useSelectedLayoutSegment`?

**Difficulty**: Intermediate

**Strategy:**
`useSelectedLayoutSegment` returns the active route segment one level down from the layout. It's useful for styling navigation menus in a parent layout.

**Code Example:**
'use client';
import { useSelectedLayoutSegment } from 'next/navigation';
import Link from 'next/link';

export default function Nav() {
  const segment = useSelectedLayoutSegment();

  return (
    <nav>
      <Link href="/blog" className={segment === 'blog' ? 'active' : ''}>
        Blog
      </Link>
      <Link href="/about" className={segment === 'about' ? 'active' : ''}>
        About
      </Link>
    </nav>
  );
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q27"></a>
### Q27: How do you optimize third-party scripts using `next/script`?

**Difficulty**: Beginner

**Strategy:**
Use the `<Script />` component. The `strategy` prop controls loading: `beforeInteractive` (critical), `afterInteractive` (default), `lazyOnload` (low priority), or `worker` (web worker).

**Code Example:**
import Script from 'next/script';

export default function Page() {
  return (
    <>
      <Script 
        src="https://www.google-analytics.com/analytics.js" 
        strategy="lazyOnload" 
      />
      <h1>Home Page</h1>
    </>
  );
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q28"></a>
### Q28: How do you implement Draft Mode for CMS previews?

**Difficulty**: Advanced

**Strategy:**
Draft Mode allows you to render pages at request time with draft content instead of the statically generated production content. You toggle it via a Route Handler setting a cookie.

**Code Example:**
// app/api/draft/route.ts
import { draftMode } from 'next/headers';

export async function GET(request: Request) {
  draftMode().enable();
  return new Response('Draft mode enabled');
}

// app/page.tsx
import { draftMode } from 'next/headers';

export default function Page() {
  const { isEnabled } = draftMode();
  // Fetch draft data if isEnabled is true
  return <div>Draft Mode: {isEnabled ? 'ON' : 'OFF'}</div>;
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q29"></a>
### Q29: What is the difference between Request Memoization and the Data Cache?

**Difficulty**: Advanced

**Strategy:**
**Request Memoization** avoids duplicate fetch requests within the *same* render pass (e.g., layout and page fetching same user). **Data Cache** persists fetch results across *multiple* requests/users (server-side caching).

**Code Example:**
// Request Memoization:
// Calling getItem() in Layout AND Page will only trigger ONE network call.
async function getItem() {
  const res = await fetch('https://api/item');
  return res.json();
}

// Data Cache:
// By default, fetch is cached indefinitely.
fetch('https://api/item', { cache: 'force-cache' }); // Default

// Opt-out (Dynamic):
fetch('https://api/item', { cache: 'no-store' });

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q30"></a>
### Q30: How do you revalidate specific data cache entries using Tags?

**Difficulty**: Advanced

**Strategy:**
Assign tags to fetch requests, then use `revalidateTag` in a Server Action or Route Handler to purge that specific cache.

**Code Example:**
// Fetch with tag
fetch('https://api/data', { next: { tags: ['collection'] } });

// Revalidate in Server Action
import { revalidateTag } from 'next/cache';

export async function updateData() {
  'use server';
  // Update DB...
  revalidateTag('collection');
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q31"></a>
### Q31: How do you implement Internationalization (i18n) in the App Router?

**Difficulty**: Advanced

**Strategy:**
Use Middleware to detect the user's locale and rewrite the URL (e.g., `/about` -> `/en/about`). Dynamically load dictionaries based on the `[lang]` param.

**Code Example:**
// middleware.ts
import { match } from '@formatjs/intl-localematcher';
import Negotiator from 'negotiator';

export function middleware(request) {
  // Check if there is any supported locale in the pathname
  const pathname = request.nextUrl.pathname;
  const pathnameIsMissingLocale = missingLocale(pathname);

  if (pathnameIsMissingLocale) {
    const locale = getLocale(request);
    return NextResponse.redirect(new URL(`/${locale}/${pathname}`, request.url));
  }
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q32"></a>
### Q32: What is Streaming and how does it improve UX?

**Difficulty**: Intermediate

**Strategy:**
Streaming allows you to break down the page's HTML into smaller chunks and progressively send them to the client. This enables parts of the UI to display sooner without waiting for all data to load.

**Code Example:**
import { Suspense } from 'react';

export default function Page() {
  return (
    <section>
      <h1>Header (Loads instantly)</h1>
      <Suspense fallback={<p>Loading feed...</p>}>
        <Feed /> {/* Streams in when ready */}
      </Suspense>
    </section>
  );
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q33"></a>
### Q33: How do you generate dynamic Metadata for SEO?

**Difficulty**: Intermediate

**Strategy:**
Export a `generateMetadata` function from your `page.tsx` or `layout.tsx`. It receives route parameters and can fetch data to populate title, description, and Open Graph tags.

**Code Example:**
export async function generateMetadata({ params }) {
  const product = await getProduct(params.id);
 
  return {
    title: product.title,
    description: product.description,
    openGraph: {
      images: [product.imageUrl],
    },
  };
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q34"></a>
### Q34: How do you protect routes from unauthorized access using Middleware?

**Difficulty**: Intermediate

**Strategy:**
Middleware runs before a request completes. You can check cookies/headers for a token. If invalid, rewrite to a login page or return a 401 response.

**Code Example:**
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';
 
export function middleware(request: NextRequest) {
  const token = request.cookies.get('token');
 
  if (!token && request.nextUrl.pathname.startsWith('/dashboard')) {
    return NextResponse.redirect(new URL('/login', request.url));
  }
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q35"></a>
### Q35: What is the purpose of `output: 'standalone'` in `next.config.js`?

**Difficulty**: Advanced

**Strategy:**
It tells Next.js to automatically trace dependencies and create a minimal `node_modules` folder containing only what's necessary for production. This significantly reduces the Docker image size.

**Code Example:**
// next.config.js
module.exports = {
  output: 'standalone',
};

// Result:
// A standalone folder is created at `.next/standalone`
// You can run it with `node .next/standalone/server.js`

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q36"></a>
### Q36: How do you use React Server Components (RSC) effectively?

**Difficulty**: Beginner

**Strategy:**
By default, components in the App Router are Server Components. They run on the server, have direct DB access, and send zero JS to the client. Use them for data fetching. Use Client Components (`'use client'`) only for interactivity (onClick, useState).

**Code Example:**
// Server Component (default)
import { db } from '@/lib/db';

export default async function UserList() {
  const users = await db.user.findMany();
  return (
    <ul>
      {users.map(u => <li key={u.id}>{u.name}</li>)}
    </ul>
  );
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q37"></a>
### Q37: How do you handle static assets like images and fonts?

**Difficulty**: Beginner

**Strategy:**
Place static files in the `public` directory. They can be referenced by your code starting from the base URL (`/`).

**Code Example:**
// File structure: /public/logo.png

// Usage
<Image src="/logo.png" width={50} height={50} alt="Logo" />

// CSS
// background-image: url('/logo.png');

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q38"></a>
### Q38: How do you implement Infinite Scroll in Next.js?

**Difficulty**: Intermediate

**Strategy:**
Use `IntersectionObserver` in a Client Component to detect when the user scrolls to the bottom. Then, trigger a Server Action or API call to fetch the next page of data.

**Code Example:**
'use client';
import { useEffect, useState } from 'react';
import { useInView } from 'react-intersection-observer';
import { fetchMoreData } from './actions';

export default function InfiniteList({ initialData }) {
  const [data, setData] = useState(initialData);
  const { ref, inView } = useInView();

  useEffect(() => {
    if (inView) {
      fetchMoreData(data.length).then(newData => {
        setData([...data, ...newData]);
      });
    }
  }, [inView]);

  return (
    <div>
      {data.map(item => <div key={item.id}>{item.title}</div>)}
      <div ref={ref}>Loading more...</div>
    </div>
  );
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q39"></a>
### Q39: What is Turbopack?

**Difficulty**: Beginner

**Strategy:**
Turbopack is an incremental bundler written in Rust, built by the creators of Webpack and Next.js. It aims to replace Webpack with significantly faster build times.

**Code Example:**
// Usage
// Update your package.json scripts:

"scripts": {
  "dev": "next dev --turbo"
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q40"></a>
### Q40: How do you debug Core Web Vitals in Next.js?

**Difficulty**: Intermediate

**Strategy:**
Next.js provides a built-in `useReportWebVitals` hook. You can log the results to the console or send them to an analytics endpoint.

**Code Example:**
'use client';
import { useReportWebVitals } from 'next/web-vitals';

export default function WebVitals() {
  useReportWebVitals((metric) => {
    console.log(metric);
    // { id: '...', name: 'LCP', startTime: ..., value: ... }
  });

  return null;
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---


<a id="q41"></a>
### Q41: How do you generate dynamic Open Graph images using `ImageResponse`?

**Difficulty**: Advanced

**Strategy:**
Use `ImageResponse` from `next/og`. It allows you to generate images using HTML and CSS (JSX) at the edge.

**Code Example:**
```javascript
import { ImageResponse } from 'next/og';

export const runtime = 'edge';

export async function GET() {
  return new ImageResponse(
    (
      <div
        style={{
          fontSize: 128,
          background: 'white',
          width: '100%',
          height: '100%',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        Hello World
      </div>
    ),
    {
      width: 1200,
      height: 600,
    },
  );
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q42"></a>
### Q42: How do you implement Partial Prerendering (PPR)?

**Difficulty**: Advanced

**Strategy:**
PPR combines static and dynamic rendering in the same route. Wrap dynamic parts in `<Suspense>`. Enable `ppr` in `next.config.js`.

**Code Example:**
```javascript
// next.config.js
module.exports = {
  experimental: {
    ppr: true,
  },
};

// Page Component
export default function Page() {
  return (
    <main>
      <h1>Static Header</h1>
      <Suspense fallback={<Spinner />}>
        <DynamicFeed />
      </Suspense>
    </main>
  );
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q43"></a>
### Q43: How do you configure Content Security Policy (CSP) in Next.js?

**Difficulty**: Advanced

**Strategy:**
Set the `Content-Security-Policy` header in `middleware.ts`. Use nonces for inline scripts.

**Code Example:**
```javascript
// middleware.ts
import { NextResponse } from 'next/server';

export function middleware(request) {
  const nonce = Buffer.from(crypto.randomUUID()).toString('base64');
  const cspHeader = `
    default-src 'self';
    script-src 'self' 'nonce-${nonce}' 'strict-dynamic';
    style-src 'self' 'nonce-${nonce}';
    img-src 'self' blob: data:;
    font-src 'self';
    object-src 'none';
    base-uri 'self';
    form-action 'self';
    frame-ancestors 'none';
    block-all-mixed-content;
    upgrade-insecure-requests;
  `;

  const requestHeaders = new Headers(request.headers);
  requestHeaders.set('x-nonce', nonce);
  requestHeaders.set('Content-Security-Policy', cspHeader.replace(/\s{2,}/g, ' ').trim());

  return NextResponse.next({
    headers: requestHeaders,
    request: {
      headers: requestHeaders,
    },
  });
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q44"></a>
### Q44: How do you unit test Server Components with Jest?

**Difficulty**: Intermediate

**Strategy:**
Since Server Components are async, you need to mock the data fetching. Use `render` from `@testing-library/react` for the component, ensuring you `await` the component if testing it directly (experimental) or test the child components.

**Code Example:**
```javascript
import Page from './page';
import { render, screen } from '@testing-library/react';

// Mock fetch or db call
jest.mock('./api', () => ({
  getData: jest.fn(() => Promise.resolve({ title: 'Test' })),
}));

test('renders page', async () => {
  const ui = await Page(); // Call async component directly
  render(ui);
  expect(screen.getByText('Test')).toBeInTheDocument();
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q45"></a>
### Q45: How do you implement E2E testing with Playwright in Next.js?

**Difficulty**: Intermediate

**Strategy:**
Use `@playwright/test`. Start the Next.js dev server or build/start for production tests.

**Code Example:**
```javascript
// tests/example.spec.ts
import { test, expect } from '@playwright/test';

test('has title', async ({ page }) => {
  await page.goto('http://localhost:3000/');
  await expect(page).toHaveTitle(/Create Next App/);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q46"></a>
### Q46: How do you use Multi-Zones to split a large Next.js app?

**Difficulty**: Advanced

**Strategy:**
Use `rewrites` in `next.config.js` to map specific paths to different Next.js apps (zones). This allows micro-frontend architecture.

**Code Example:**
```javascript
// next.config.js
module.exports = {
  async rewrites() {
    return [
      {
        source: '/blog',
        destination: 'https://blog.my-app.com/blog',
      },
      {
        source: '/blog/:path*',
        destination: 'https://blog.my-app.com/blog/:path*',
      },
    ];
  },
};
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q47"></a>
### Q47: How do you run Cron Jobs in a Next.js app (Vercel Cron)?

**Difficulty**: Intermediate

**Strategy:**
Create a `vercel.json` file and define `crons`. Point them to an API route.

**Code Example:**
```javascript
// vercel.json
{
  "crons": [
    {
      "path": "/api/cron",
      "schedule": "0 10 * * *"
    }
  ]
}

// app/api/cron/route.ts
export async function GET() {
  // Perform scheduled task
  return new Response('Cron job executed');
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q48"></a>
### Q48: How do you prevent specific pages from being indexed by search engines?

**Difficulty**: Beginner

**Strategy:**
Export a `metadata` object with `robots: { index: false }`.

**Code Example:**
```javascript
export const metadata = {
  title: 'Private Page',
  robots: {
    index: false,
    follow: false,
    nocache: true,
    googleBot: {
      index: false,
      follow: false,
    },
  },
};
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q49"></a>
### Q49: How do you use `useOptimistic` for instant UI updates?

**Difficulty**: Advanced

**Strategy:**
Use the `useOptimistic` hook to show a state immediately while a Server Action is pending. It reverts automatically if the action fails.

**Code Example:**
```javascript
'use client';
import { useOptimistic } from 'react';
import { sendName } from './actions';

export default function Form({ currentName }) {
  const [optimisticName, addOptimisticName] = useOptimistic(
    currentName,
    (state, newName) => newName
  );

  async function action(formData) {
    const name = formData.get('name');
    addOptimisticName(name);
    await sendName(name);
  }

  return (
    <form action={action}>
      <p>Name: {optimisticName}</p>
      <input name="name" />
    </form>
  );
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q50"></a>
### Q50: How do you configure a custom build output directory?

**Difficulty**: Intermediate

**Strategy:**
Set `distDir` in `next.config.js`.

**Code Example:**
```javascript
// next.config.js
module.exports = {
  distDir: 'build',
};
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q51"></a>
### Q51: How do you handle Next.js state management in large scale applications?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```javascript
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q52"></a>
### Q52: How do you perform Next.js data validation in microservices?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```javascript
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q53"></a>
### Q53: How do you automate Next.js deployment for mobile devices?

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

<a id="q54"></a>
### Q54: How do you handle Next.js concurrency issues in legacy systems?

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

<a id="q55"></a>
### Q55: How do you implement Next.js caching in cloud infrastructure?

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

<a id="q56"></a>
### Q56: How do you manage Next.js configuration for real-time systems?

**Difficulty**: Beginner

**Strategy**:
Use environment variables or config files. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const config = process.env.CONFIG || 'default';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q57"></a>
### Q57: How do you handle Next.js internationalization (i18n) in distributed systems?

**Difficulty**: Intermediate

**Strategy**:
Use i18n libraries. Extract strings to resource files.

**Code Example**:
```javascript
t('welcome_message')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q58"></a>
### Q58: How do you ensure Next.js accessibility (a11y) in high-traffic sites?

**Difficulty**: Beginner

**Strategy**:
Use semantic HTML and ARIA roles. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
<button aria-label="Close">X</button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q59"></a>
### Q59: How do you optimize Next.js network requests in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use batching, debouncing, or GraphQL. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
debounce(() => fetch(), 300);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q60"></a>
### Q60: How do you handle Next.js performance optimization for production environments?

**Difficulty**: Advanced

**Strategy**:
Profile first, then optimize hot paths. Use caching and efficient algorithms.

**Code Example**:
```javascript
const start = performance.now();
// Next.js logic
const end = performance.now();
console.log('Time:', end - start);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q61"></a>
### Q61: What are the security implications of Next.js in large scale applications?

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

<a id="q62"></a>
### Q62: How do you debug Next.js memory leaks in microservices?

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

<a id="q63"></a>
### Q63: Best practices for Next.js code organization in mobile devices?

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

<a id="q64"></a>
### Q64: How do you implement Next.js error handling for legacy systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```javascript
try {
  await Next.jsOperation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q65"></a>
### Q65: How do you test Next.js functionality in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```javascript
test('Next.js works', () => {
  expect(Next.js()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q66"></a>
### Q66: How do you handle Next.js state management in real-time systems?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```javascript
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q67"></a>
### Q67: How do you perform Next.js data validation in distributed systems?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```javascript
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q68"></a>
### Q68: How do you automate Next.js deployment for high-traffic sites?

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

<a id="q69"></a>
### Q69: How do you handle Next.js concurrency issues in embedded systems?

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

<a id="q70"></a>
### Q70: How do you implement Next.js caching in production environments?

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

<a id="q71"></a>
### Q71: How do you manage Next.js configuration for large scale applications?

**Difficulty**: Beginner

**Strategy**:
Use environment variables or config files. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const config = process.env.CONFIG || 'default';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q72"></a>
### Q72: How do you handle Next.js internationalization (i18n) in microservices?

**Difficulty**: Intermediate

**Strategy**:
Use i18n libraries. Extract strings to resource files.

**Code Example**:
```javascript
t('welcome_message')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q73"></a>
### Q73: How do you ensure Next.js accessibility (a11y) in mobile devices?

**Difficulty**: Beginner

**Strategy**:
Use semantic HTML and ARIA roles. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
<button aria-label="Close">X</button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q74"></a>
### Q74: How do you optimize Next.js network requests in legacy systems?

**Difficulty**: Advanced

**Strategy**:
Use batching, debouncing, or GraphQL. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
debounce(() => fetch(), 300);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q75"></a>
### Q75: How do you handle Next.js performance optimization for cloud infrastructure?

**Difficulty**: Advanced

**Strategy**:
Profile first, then optimize hot paths. Use caching and efficient algorithms.

**Code Example**:
```javascript
const start = performance.now();
// Next.js logic
const end = performance.now();
console.log('Time:', end - start);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q76"></a>
### Q76: What are the security implications of Next.js in real-time systems?

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

<a id="q77"></a>
### Q77: How do you debug Next.js memory leaks in distributed systems?

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

<a id="q78"></a>
### Q78: Best practices for Next.js code organization in high-traffic sites?

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

<a id="q79"></a>
### Q79: How do you implement Next.js error handling for embedded systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```javascript
try {
  await Next.jsOperation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q80"></a>
### Q80: How do you test Next.js functionality in production environments?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```javascript
test('Next.js works', () => {
  expect(Next.js()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q81"></a>
### Q81: How do you handle Next.js state management in large scale applications?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```javascript
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q82"></a>
### Q82: How do you perform Next.js data validation in microservices?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```javascript
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q83"></a>
### Q83: How do you automate Next.js deployment for mobile devices?

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

<a id="q84"></a>
### Q84: How do you handle Next.js concurrency issues in legacy systems?

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

<a id="q85"></a>
### Q85: How do you implement Next.js caching in cloud infrastructure?

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

<a id="q86"></a>
### Q86: How do you manage Next.js configuration for real-time systems?

**Difficulty**: Beginner

**Strategy**:
Use environment variables or config files. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const config = process.env.CONFIG || 'default';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q87"></a>
### Q87: How do you handle Next.js internationalization (i18n) in distributed systems?

**Difficulty**: Intermediate

**Strategy**:
Use i18n libraries. Extract strings to resource files.

**Code Example**:
```javascript
t('welcome_message')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q88"></a>
### Q88: How do you ensure Next.js accessibility (a11y) in high-traffic sites?

**Difficulty**: Beginner

**Strategy**:
Use semantic HTML and ARIA roles. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
<button aria-label="Close">X</button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q89"></a>
### Q89: How do you optimize Next.js network requests in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use batching, debouncing, or GraphQL. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
debounce(() => fetch(), 300);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q90"></a>
### Q90: How do you handle Next.js performance optimization for production environments?

**Difficulty**: Advanced

**Strategy**:
Profile first, then optimize hot paths. Use caching and efficient algorithms.

**Code Example**:
```javascript
const start = performance.now();
// Next.js logic
const end = performance.now();
console.log('Time:', end - start);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q91"></a>
### Q91: What are the security implications of Next.js in large scale applications?

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

<a id="q92"></a>
### Q92: How do you debug Next.js memory leaks in microservices?

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

<a id="q93"></a>
### Q93: Best practices for Next.js code organization in mobile devices?

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

<a id="q94"></a>
### Q94: How do you implement Next.js error handling for legacy systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```javascript
try {
  await Next.jsOperation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q95"></a>
### Q95: How do you test Next.js functionality in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```javascript
test('Next.js works', () => {
  expect(Next.js()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q96"></a>
### Q96: How do you handle Next.js state management in real-time systems?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```javascript
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q97"></a>
### Q97: How do you perform Next.js data validation in distributed systems?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```javascript
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q98"></a>
### Q98: How do you automate Next.js deployment for high-traffic sites?

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

<a id="q99"></a>
### Q99: How do you handle Next.js concurrency issues in embedded systems?

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

<a id="q100"></a>
### Q100: How do you implement Next.js caching in production environments?

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
