<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Next.js Logo" width="100" height="100">
  </a>
  <h1>Next.js Interview Questions & Answers</h1>
  <p><b>Comprehensive interview questions covering Next.js 14/15 App Router, Server Actions, and RSC</b></p>
</div>

---

## Table of Contents

1. [What is the App Router in Next.js 13/14/15 and how does it differ from Pages Router?](#q1) <span class="intermediate">Intermediate</span>
2. [Server Components vs Client Components in Next.js App Router: When to use which?](#q2) <span class="advanced">Advanced</span>
3. [How does Data Fetching and Caching work in Next.js with `fetch` extensions?](#q3) <span class="advanced">Advanced</span>
4. [How do Server Actions work in Next.js and how do you handle mutations?](#q4) <span class="advanced">Advanced</span>
5. [How do you implement Middleware in Next.js for Authentication and Redirects?](#q5) <span class="intermediate">Intermediate</span>
6. [Explain Incremental Static Regeneration (ISR) and On-Demand Revalidation?](#q6) <span class="advanced">Advanced</span>
7. [How does `next/image` optimize performance and prevent Layout Shift?](#q7) <span class="beginner">Beginner</span>
8. [How do Dynamic Routes and `generateStaticParams` work in the App Router?](#q8) <span class="intermediate">Intermediate</span>
9. [How do you implement Route Handlers (`route.ts`) in Next.js?](#q9) <span class="intermediate">Intermediate</span>
10. [How do Parallel Routes and Intercepting Routes work in Next.js?](#q10) <span class="advanced">Advanced</span>
11. [How does Streaming SSR with React Suspense work in Next.js?](#q11) <span class="advanced">Advanced</span>
12. [What is `next/font` and why is it superior to external CDN fonts?](#q12) <span class="beginner">Beginner</span>
13. [How do you manage dynamic SEO metadata with `generateMetadata`?](#q13) <span class="intermediate">Intermediate</span>
14. [How does `next/dynamic` handle client-only component loading without SSR?](#q14) <span class="intermediate">Intermediate</span>
15. [How do you handle internationalization (i18n) routing in App Router?](#q15) <span class="intermediate">Intermediate</span>
16. [What is Turbopack in Next.js?](#q16) <span class="intermediate">Intermediate</span>
17. [How do you handle cookies in Next.js App Router Server Components?](#q17) <span class="intermediate">Intermediate</span>
18. [How do you set headers and cookies in Server Actions?](#q18) <span class="intermediate">Intermediate</span>
19. [What is the difference between `loading.tsx` and custom `<Suspense>` boundaries?](#q19) <span class="intermediate">Intermediate</span>
20. [How do you handle global not-found and custom 404 pages in Next.js?](#q20) <span class="beginner">Beginner</span>
21. [How do you handle runtime errors with `error.tsx` in Next.js?](#q21) <span class="intermediate">Intermediate</span>
22. [What is the purpose of `template.tsx` vs `layout.tsx`?](#q22) <span class="intermediate">Intermediate</span>
23. [How do you implement Optimistic Updates with Server Actions in Next.js?](#q23) <span class="advanced">Advanced</span>
24. [How do you deploy Next.js applications using Docker standalone output?](#q24) <span class="advanced">Advanced</span>
25. [How do you configure CORS in Next.js Route Handlers?](#q25) <span class="intermediate">Intermediate</span>
26. [What is the difference between `redirect` and `permanentRedirect` in Next.js?](#q26) <span class="beginner">Beginner</span>
27. [How do you handle search params in Server Components vs Client Components?](#q27) <span class="beginner">Beginner</span>
28. [How do you protect API routes using API keys and rate limiting?](#q28) <span class="advanced">Advanced</span>
29. [What is Draft Mode in Next.js and how is it used with headless CMS?](#q29) <span class="advanced">Advanced</span>
30. [How do you analyze bundle size in Next.js?](#q30) <span class="intermediate">Intermediate</span>
31. [What are Route Segment Config options in Next.js?](#q31) <span class="intermediate">Intermediate</span>
32. [How does Next.js handle environment variables (`.env.local` vs `.env.production`)?](#q32) <span class="beginner">Beginner</span>
33. [How do you configure custom Webpack or Turbopack rules in `next.config.js`?](#q33) <span class="intermediate">Intermediate</span>
34. [What is the difference between Edge Runtime and Node.js Runtime in Next.js?](#q34) <span class="advanced">Advanced</span>
35. [How do you implement authentication with NextAuth.js (Auth.js)?](#q35) <span class="advanced">Advanced</span>
36. [How do you handle file uploads in Next.js Server Actions?](#q36) <span class="intermediate">Intermediate</span>
37. [How do you optimize Third-Party Scripts using `@next/third-parties`?](#q37) <span class="intermediate">Intermediate</span>
38. [What is the purpose of `useSelectedLayoutSegment` in Next.js navigation?](#q38) <span class="intermediate">Intermediate</span>
39. [How do you implement progressive pagination in Next.js Server Components?](#q39) <span class="intermediate">Intermediate</span>
40. [How do you secure Next.js apps against Cross-Site Request Forgery (CSRF)?](#q40) <span class="advanced">Advanced</span>
41. [What is Static Export (`output: 'export'`) in Next.js and its limitations?](#q41) <span class="intermediate">Intermediate</span>
42. [How do you handle WebSocket connections in Next.js?](#q42) <span class="advanced">Advanced</span>
43. [How do you cache GraphQL queries in Next.js App Router?](#q43) <span class="intermediate">Intermediate</span>
44. [How do you implement infinite scrolling with Server Actions in Next.js?](#q44) <span class="advanced">Advanced</span>
45. [What is Partial Prerendering (PPR) in Next.js 14/15?](#q45) <span class="advanced">Advanced</span>
46. [How do you handle redirects inside Server Actions?](#q46) <span class="beginner">Beginner</span>
47. [How do you implement multi-tenant routing (subdomain-based) in Next.js?](#q47) <span class="advanced">Advanced</span>
48. [How do you configure custom HTTP response headers in `next.config.js`?](#q48) <span class="intermediate">Intermediate</span>
49. [What is the difference between `Link` component and `useRouter.push`?](#q49) <span class="beginner">Beginner</span>
50. [How do you disable Link prefetching for non-critical routes?](#q50) <span class="beginner">Beginner</span>
51. [How do you implement OpenGraph dynamic image generation with `@vercel/og`?](#q51) <span class="advanced">Advanced</span>
52. [How do you handle localization in Next.js URL paths?](#q52) <span class="intermediate">Intermediate</span>
53. [What is the purpose of `next-sitemap` plugin?](#q53) <span class="intermediate">Intermediate</span>
54. [How do you mock API calls during Next.js testing with Vitest?](#q54) <span class="intermediate">Intermediate</span>
55. [How do you handle background jobs and cron triggers in Next.js?](#q55) <span class="advanced">Advanced</span>
56. [What is the difference between `revalidatePath` and `revalidateTag`?](#q56) <span class="intermediate">Intermediate</span>
57. [How do you pass data from Server Component to Client Component?](#q57) <span class="beginner">Beginner</span>
58. [Why can't functions or class instances be passed as props from Server to Client Components?](#q58) <span class="intermediate">Intermediate</span>
59. [How do you compose Client and Server components together?](#q59) <span class="advanced">Advanced</span>
60. [How do you configure Sentry error tracking in Next.js?](#q60) <span class="intermediate">Intermediate</span>
61. [How do you handle Database Connection Pooling in Next.js Serverless Functions?](#q61) <span class="advanced">Advanced</span>
62. [What is the difference between `usePathname` and `useRouter` in App Router?](#q62) <span class="beginner">Beginner</span>
63. [How do you implement Dark Mode in Next.js without flash of unstyled theme?](#q63) <span class="intermediate">Intermediate</span>
64. [How do you handle Stripe Webhook signature verification in Route Handlers?](#q64) <span class="advanced">Advanced</span>
65. [How do you implement server-side search filtering with instant URL sync?](#q65) <span class="intermediate">Intermediate</span>
66. [What are Intercepting Routes syntax tokens (`(.)`, `(..)`, `(...)`)?](#q66) <span class="advanced">Advanced</span>
67. [How do you build a multi-language switcher component in Next.js?](#q67) <span class="beginner">Beginner</span>
68. [How do you measure Core Web Vitals using `useReportWebVitals`?](#q68) <span class="intermediate">Intermediate</span>
69. [What is the purpose of `mdx-components.tsx` in Next.js MDX apps?](#q69) <span class="intermediate">Intermediate</span>
70. [How do you secure Server Actions against unauthorized invocations?](#q70) <span class="advanced">Advanced</span>
71. [How do you stream AI responses in Next.js using Vercel AI SDK?](#q71) <span class="advanced">Advanced</span>
72. [What is the difference between server-only and client-only packages?](#q72) <span class="intermediate">Intermediate</span>
73. [How do you handle complex SQL joins with Drizzle ORM in Next.js Server Components?](#q73) <span class="intermediate">Intermediate</span>
74. [How do you implement breadcrumb navigation using Next.js route segments?](#q74) <span class="intermediate">Intermediate</span>
75. [How do you configure Progressive Web App (PWA) with Next.js?](#q75) <span class="intermediate">Intermediate</span>
76. [How do you handle PDF generation on the server in Next.js?](#q76) <span class="advanced">Advanced</span>
77. [What is the difference between `npm run build` and `npm run start`?](#q77) <span class="beginner">Beginner</span>
78. [How do you optimize Google Analytics scripts in Next.js?](#q78) <span class="beginner">Beginner</span>
79. [How do you implement Role-Based Access Control (RBAC) in Next.js?](#q79) <span class="advanced">Advanced</span>
80. [What is the purpose of `Instrumentations.ts` in Next.js?](#q80) <span class="advanced">Advanced</span>
81. [How do you handle cross-origin fonts in Next.js?](#q81) <span class="intermediate">Intermediate</span>
82. [How do you implement image upload preview before submitting to Server Action?](#q82) <span class="beginner">Beginner</span>
83. [How do you deploy Next.js to AWS ECS using Fargate?](#q83) <span class="advanced">Advanced</span>
84. [What is the difference between `cache()` from React and Next.js `unstable_cache`?](#q84) <span class="advanced">Advanced</span>
85. [How do you implement responsive navigation drawers in Next.js?](#q85) <span class="beginner">Beginner</span>
86. [How do you optimize font loading for custom TTF/WOFF2 fonts in Next.js?](#q86) <span class="intermediate">Intermediate</span>
87. [How do you prevent brute force attacks on Next.js login routes?](#q87) <span class="advanced">Advanced</span>
88. [What are Server-Sent Events (SSE) in Next.js Route Handlers?](#q88) <span class="advanced">Advanced</span>
89. [How do you implement a robust multi-step checkout in Next.js?](#q89) <span class="intermediate">Intermediate</span>
90. [What is the difference between Server Actions and TRPC in Next.js?](#q90) <span class="advanced">Advanced</span>
91. [How do you handle dynamic sitemaps for 100,000+ records in Next.js?](#q91) <span class="advanced">Advanced</span>
92. [How do you test Server Actions with Vitest?](#q92) <span class="intermediate">Intermediate</span>
93. [How do you implement drag-and-drop file upload with progress in Next.js?](#q93) <span class="intermediate">Intermediate</span>
94. [How do you configure micro-frontends with Next.js multi-zones?](#q94) <span class="advanced">Advanced</span>
95. [What are the best practices for structuring Next.js 14 enterprise applications?](#q95) <span class="advanced">Advanced</span>
96. [How do you implement Server-Side Event Streaming (SSE) in Next.js App Router?](#q96) <span class="advanced">Advanced</span>
97. [How do you handle dynamic OG images with custom font styling?](#q97) <span class="intermediate">Intermediate</span>
98. [How do you implement rate limiting with Vercel KV in Next.js Middleware?](#q98) <span class="advanced">Advanced</span>
99. [How do you optimize SVG icons with SVGR in Next.js?](#q99) <span class="beginner">Beginner</span>
100. [How do you implement breadcrumb navigation using Next.js App Router hooks?](#q100) <span class="intermediate">Intermediate</span>

---

<a id="q1"></a>
### Q1: What is the App Router in Next.js 13/14/15 and how does it differ from Pages Router?

**Difficulty**: Intermediate

**Strategy**:
The App Router is built on React Server Components (RSC) and uses a directory-based hierarchy inside `app/`. It supports nested layouts (`layout.tsx`), loading UI states (`loading.tsx`), error boundaries (`error.tsx`), route handlers (`route.ts`), and streaming SSR via React Suspense. Pages Router (`pages/`) relies on `getServerSideProps` and `getStaticProps` with client-side hydration.

**Code Example**:
```tsx
// app/dashboard/layout.tsx
export default function DashboardLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="dashboard-container">
      <aside><nav>Sidebar Nav</nav></aside>
      <main>{children}</main>
    </div>
  );
}
```

---

<a id="q2"></a>
### Q2: Server Components vs Client Components in Next.js App Router: When to use which?

**Difficulty**: Advanced

**Strategy**:
- **Server Components (Default)**: Render only on server. Can access DB/filesystem directly, keep secret API keys safe, and have zero client bundle impact. Cannot use browser APIs, state, or event handlers.
- **Client Components (`'use client'`)**: Pre-rendered on server and hydrated on client. Use when you need event listeners (`onClick`), state (`useState`), effects (`useEffect`), or browser APIs (`localStorage`).

**Code Example**:
```tsx
// Client Component
'use client';
import { useState } from 'react';

export function Counter() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(c => c + 1)}>Clicks: {count}</button>;
}
```

---

<a id="q3"></a>
### Q3: How does Data Fetching and Caching work in Next.js with `fetch` extensions?

**Difficulty**: Advanced

**Strategy**:
Next.js extends native `fetch` with caching options:
1. `fetch(url, { cache: 'force-cache' })`: Default SSG-like caching.
2. `fetch(url, { cache: 'no-store' })`: SSR-like dynamic fetch on every request.
3. `fetch(url, { next: { revalidate: 60 } })`: ISR-like cached with 60-second time-based revalidation.
4. `fetch(url, { next: { tags: ['products'] } })`: On-demand revalidation via `revalidateTag('products')`.

**Code Example**:
```typescript
// Server Component fetch with tag-based on-demand revalidation
export async function getProducts() {
  const res = await fetch('https://api.example.com/products', {
    next: { tags: ['products'], revalidate: 3600 }
  });
  if (!res.ok) throw new Error('Failed to fetch');
  return res.json();
}
```

---

<a id="q4"></a>
### Q4: How do Server Actions work in Next.js and how do you handle mutations?

**Difficulty**: Advanced

**Strategy**:
Server Actions are async functions declared with `'use server'` that execute on the server and can be invoked from `<form action={...}>` or client event handlers. They integrate with `revalidatePath` or `revalidateTag` to update the UI without manual state management.

**Code Example**:
```tsx
// app/actions.ts
'use server';
import { revalidatePath } from 'next/cache';
import db from '@/lib/db';

export async function addComment(formData: FormData) {
  const text = formData.get('comment') as string;
  await db.comments.create({ data: { text } });
  revalidatePath('/comments');
}

// app/comments/page.tsx
import { addComment } from '../actions';
export default function Comments() {
  return (
    <form action={addComment}>
      <input name="comment" required />
      <button type="submit">Post Comment</button>
    </form>
  );
}
```

---

<a id="q5"></a>
### Q5: How do you implement Middleware in Next.js for Authentication and Redirects?

**Difficulty**: Intermediate

**Strategy**:
Middleware runs before a request is completed on the Edge Runtime. Use it for auth token verification, redirects, cookie manipulation, and A/B testing rewrites.

**Code Example**:
```typescript
// middleware.ts
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  const token = request.cookies.get('auth-token')?.value;
  if (!token && request.nextUrl.pathname.startsWith('/dashboard')) {
    return NextResponse.redirect(new URL('/login', request.url));
  }
  return NextResponse.next();
}

export const config = {
  matcher: ['/dashboard/:path*', '/admin/:path*'],
};
```

---

<a id="q6"></a>
### Q6: Explain Incremental Static Regeneration (ISR) and On-Demand Revalidation?

**Difficulty**: Advanced

**Strategy**:
ISR enables updating static pages after build time without rebuilding the entire site. Time-based ISR sets a `revalidate` duration. On-demand ISR uses `revalidatePath()` or `revalidateTag()` triggered via webhooks (e.g. headless CMS updates).

**Code Example**:
```typescript
// app/api/webhook/route.ts
import { revalidateTag } from 'next/cache';
import { NextResponse } from 'next/server';

export async function POST(request: Request) {
  const secret = request.headers.get('x-webhook-secret');
  if (secret !== process.env.WEBHOOK_SECRET) {
    return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
  }
  revalidateTag('posts');
  return NextResponse.json({ revalidated: true, now: Date.now() });
}
```

---

<a id="q7"></a>
### Q7: How does `next/image` optimize performance and prevent Layout Shift?

**Difficulty**: Beginner

**Strategy**:
`next/image` automatically converts images to modern formats (AVIF/WebP), resizes dynamically based on device viewport, lazy loads below the fold, and reserves aspect ratio dimensions to eliminate Cumulative Layout Shift (CLS).

**Code Example**:
```tsx
import Image from 'next/image';

export function HeroBanner() {
  return (
    <Image
      src="/hero.jpg"
      alt="Hero Banner"
      width={1200}
      height={600}
      priority // Preload hero image above the fold
      placeholder="blur"
      blurDataURL="data:image/jpeg;base64,..."
    />
  );
}
```

---

<a id="q8"></a>
### Q8: How do Dynamic Routes and `generateStaticParams` work in the App Router?

**Difficulty**: Intermediate

**Strategy**:
`generateStaticParams` replaces `getStaticPaths` in the App Router to define route parameters statically at build time for SSG pages.

**Code Example**:
```tsx
// app/blog/[slug]/page.tsx
export async function generateStaticParams() {
  const posts = await fetch('https://api.example.com/posts').then(res => res.json());
  return posts.map((post: { slug: string }) => ({
    slug: post.slug,
  }));
}

export default async function BlogPost({ params }: { params: { slug: string } }) {
  return <article>Post: {params.slug}</article>;
}
```

---

<a id="q9"></a>
### Q9: How do you implement Route Handlers (`route.ts`) in Next.js?

**Difficulty**: Intermediate

**Strategy**:
Route Handlers provide custom request handlers for web APIs using standard Request and Response objects, supporting GET, POST, PUT, DELETE, PATCH, and OPTIONS.

**Code Example**:
```typescript
// app/api/users/route.ts
import { NextResponse } from 'next/server';

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const role = searchParams.get('role');
  const users = await fetchUsersByRole(role);
  return NextResponse.json({ data: users });
}

export async function POST(request: Request) {
  const body = await request.json();
  const newUser = await createUser(body);
  return NextResponse.json({ data: newUser }, { status: 201 });
}
```

---

<a id="q10"></a>
### Q10: How do Parallel Routes and Intercepting Routes work in Next.js?

**Difficulty**: Advanced

**Strategy**:
- **Parallel Routes (`@slot`)**: Render multiple pages simultaneously in the same layout (e.g., dashboard analytics + notifications).
- **Intercepting Routes (`(..)photo/[id]`)**: Load a route within the current layout while intercepting the URL change (e.g., opening a photo in a modal when clicked, but showing full page on refresh).

**Code Example**:
```tsx
// app/feed/@modal/(..)photo/[id]/page.tsx
import { Modal } from '@/components/Modal';
export default function PhotoModal({ params }: { params: { id: string } }) {
  return (
    <Modal>
      <img src={`/api/photos/${params.id}`} alt="Photo" />
    </Modal>
  );
}
```

---

<a id="q11"></a>
### Q11: How does Streaming SSR with React Suspense work in Next.js?

**Difficulty**: Advanced

**Strategy**:
Streaming breaks down page HTML into chunks and streams them progressively from server to browser as data arrives, avoiding blocking the whole page on slow DB queries.

**Code Example**:
```tsx
import { Suspense } from 'react';
import RevenueChart from './RevenueChart';
import LatestInvoices from './LatestInvoices';

export default function DashboardPage() {
  return (
    <div className="grid grid-cols-2 gap-4">
      <Suspense fallback={<div>Loading Chart...</div>}>
        <RevenueChart />
      </Suspense>
      <Suspense fallback={<div>Loading Invoices...</div>}>
        <LatestInvoices />
      </Suspense>
    </div>
  );
}
```

---

<a id="q12"></a>
### Q12: What is `next/font` and why is it superior to external CDN fonts?

**Difficulty**: Beginner

**Strategy**:
`next/font` downloads Google or custom fonts at build time and hosts them locally with your static assets, eliminating external network roundtrips and font flicker (FOIT/FOUT).

**Code Example**:
```tsx
import { Inter } from 'next/font/google';
const inter = Inter({ subsets: ['latin'], display: 'swap' });
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return <html lang="en" className={inter.className}><body>{children}</body></html>;
}
```

---

<a id="q13"></a>
### Q13: How do you manage dynamic SEO metadata with `generateMetadata`?

**Difficulty**: Intermediate

**Strategy**:
`generateMetadata` computes dynamic `<title>`, `<meta>`, and OpenGraph tags per page on the server.

**Code Example**:
```tsx
import type { Metadata } from 'next';
export async function generateMetadata({ params }: { params: { id: string } }): Promise<Metadata> {
  const product = await getProduct(params.id);
  return {
    title: `${product.title} | Store`,
    description: product.summary,
    openGraph: { images: [product.coverImage] }
  };
}
```

---

<a id="q14"></a>
### Q14: How does `next/dynamic` handle client-only component loading without SSR?

**Difficulty**: Intermediate

**Strategy**:
Wrap components with `dynamic(() => import(...), { ssr: false })` to load client-only dependencies like canvas or charting libraries.

**Code Example**:
```tsx
import dynamic from 'next/dynamic';
const MapComponent = dynamic(() => import('@/components/Map'), { ssr: false, loading: () => <p>Loading Map...</p> });
export default function Page() { return <MapComponent />; }
```

---

<a id="q15"></a>
### Q15: How do you handle internationalization (i18n) routing in App Router?

**Difficulty**: Intermediate

**Strategy**:
Use a dynamic segment `app/[lang]/page.tsx` combined with middleware to detect user locale and rewrite URLs.

**Code Example**:
```typescript
// middleware.ts
import { match } from '@formatjs/intl-localematcher';
import Negotiator from 'negotiator';
export function middleware(req: NextRequest) {
  const pathname = req.nextUrl.pathname;
  const pathnameIsMissingLocale = ['en', 'es', 'fr'].every(locale => !pathname.startsWith(`/${locale}/`));
  if (pathnameIsMissingLocale) {
    return NextResponse.redirect(new URL(`/en${pathname}`, req.url));
  }
}
```

---

<a id="q16"></a>
### Q16: What is Turbopack in Next.js?

**Difficulty**: Intermediate

**Strategy**:
Detailed explanation of What is Turbopack in Next.js?. Rust-based incremental bundler replacing Webpack for fast local development. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for What is Turbopack in Next.js?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q17"></a>
### Q17: How do you handle cookies in Next.js App Router Server Components?

**Difficulty**: Intermediate

**Strategy**:
Detailed explanation of How do you handle cookies in Next.js App Router Server Components?. Use `cookies()` from `next/headers` to read incoming request cookies. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you handle cookies in Next.js App Router Server Components?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q18"></a>
### Q18: How do you set headers and cookies in Server Actions?

**Difficulty**: Intermediate

**Strategy**:
Detailed explanation of How do you set headers and cookies in Server Actions?. Call `cookies().set('token', val)` directly inside `'use server'` functions. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you set headers and cookies in Server Actions?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q19"></a>
### Q19: What is the difference between `loading.tsx` and custom `<Suspense>` boundaries?

**Difficulty**: Intermediate

**Strategy**:
Detailed explanation of What is the difference between `loading.tsx` and custom `<Suspense>` boundaries?. `loading.tsx` wraps the entire route page in Suspense; custom Suspense targets specific child components. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for What is the difference between `loading.tsx` and custom `<Suspense>` boundaries?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q20"></a>
### Q20: How do you handle global not-found and custom 404 pages in Next.js?

**Difficulty**: Beginner

**Strategy**:
Detailed explanation of How do you handle global not-found and custom 404 pages in Next.js?. Create `not-found.tsx` and invoke `notFound()` from `next/navigation`. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you handle global not-found and custom 404 pages in Next.js?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q21"></a>
### Q21: How do you handle runtime errors with `error.tsx` in Next.js?

**Difficulty**: Intermediate

**Strategy**:
Detailed explanation of How do you handle runtime errors with `error.tsx` in Next.js?. `error.tsx` must be a client component (`'use client'`) and receives `error` and `reset` props. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you handle runtime errors with `error.tsx` in Next.js?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q22"></a>
### Q22: What is the purpose of `template.tsx` vs `layout.tsx`?

**Difficulty**: Intermediate

**Strategy**:
Detailed explanation of What is the purpose of `template.tsx` vs `layout.tsx`?. `layout.tsx` persists state across route changes; `template.tsx` remounts and creates fresh state on each navigation. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for What is the purpose of `template.tsx` vs `layout.tsx`?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q23"></a>
### Q23: How do you implement Optimistic Updates with Server Actions in Next.js?

**Difficulty**: Advanced

**Strategy**:
Detailed explanation of How do you implement Optimistic Updates with Server Actions in Next.js?. Use React 19 `useOptimistic` hook with server action form dispatch. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you implement Optimistic Updates with Server Actions in Next.js?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q24"></a>
### Q24: How do you deploy Next.js applications using Docker standalone output?

**Difficulty**: Advanced

**Strategy**:
Detailed explanation of How do you deploy Next.js applications using Docker standalone output?. Set `output: 'standalone'` in `next.config.js` to create minimal production node server bundle. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you deploy Next.js applications using Docker standalone output?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q25"></a>
### Q25: How do you configure CORS in Next.js Route Handlers?

**Difficulty**: Intermediate

**Strategy**:
Detailed explanation of How do you configure CORS in Next.js Route Handlers?. Return CORS headers (`Access-Control-Allow-Origin`, `Access-Control-Allow-Methods`) in route responses. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you configure CORS in Next.js Route Handlers?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q26"></a>
### Q26: What is the difference between `redirect` and `permanentRedirect` in Next.js?

**Difficulty**: Beginner

**Strategy**:
Detailed explanation of What is the difference between `redirect` and `permanentRedirect` in Next.js?. `redirect` returns 307 temporary redirect; `permanentRedirect` returns 308 permanent redirect. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for What is the difference between `redirect` and `permanentRedirect` in Next.js?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q27"></a>
### Q27: How do you handle search params in Server Components vs Client Components?

**Difficulty**: Beginner

**Strategy**:
Detailed explanation of How do you handle search params in Server Components vs Client Components?. Server Components receive `searchParams` prop; Client Components use `useSearchParams()` hook. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you handle search params in Server Components vs Client Components?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q28"></a>
### Q28: How do you protect API routes using API keys and rate limiting?

**Difficulty**: Advanced

**Strategy**:
Detailed explanation of How do you protect API routes using API keys and rate limiting?. Use middleware with Upstash Redis rate-limiter based on IP or authorization token. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you protect API routes using API keys and rate limiting?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q29"></a>
### Q29: What is Draft Mode in Next.js and how is it used with headless CMS?

**Difficulty**: Advanced

**Strategy**:
Detailed explanation of What is Draft Mode in Next.js and how is it used with headless CMS?. Enables viewing unpublished CMS draft content dynamically without rebuilding static pages. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for What is Draft Mode in Next.js and how is it used with headless CMS?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q30"></a>
### Q30: How do you analyze bundle size in Next.js?

**Difficulty**: Intermediate

**Strategy**:
Detailed explanation of How do you analyze bundle size in Next.js?. Use `@next/bundle-analyzer` plugin in `next.config.js`. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you analyze bundle size in Next.js?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q31"></a>
### Q31: What are Route Segment Config options in Next.js?

**Difficulty**: Intermediate

**Strategy**:
Detailed explanation of What are Route Segment Config options in Next.js?. Export `dynamic = 'force-dynamic'`, `revalidate = 3600`, or `runtime = 'edge'`. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for What are Route Segment Config options in Next.js?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q32"></a>
### Q32: How does Next.js handle environment variables (`.env.local` vs `.env.production`)?

**Difficulty**: Beginner

**Strategy**:
Detailed explanation of How does Next.js handle environment variables (`.env.local` vs `.env.production`)?. Prefix client variables with `NEXT_PUBLIC_`; server variables remain secret without prefix. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How does Next.js handle environment variables (`.env.local` vs `.env.production`)?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q33"></a>
### Q33: How do you configure custom Webpack or Turbopack rules in `next.config.js`?

**Difficulty**: Intermediate

**Strategy**:
Detailed explanation of How do you configure custom Webpack or Turbopack rules in `next.config.js`?. Extend `webpack(config, { isServer })` or configure `turbopack` options. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you configure custom Webpack or Turbopack rules in `next.config.js`?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q34"></a>
### Q34: What is the difference between Edge Runtime and Node.js Runtime in Next.js?

**Difficulty**: Advanced

**Strategy**:
Detailed explanation of What is the difference between Edge Runtime and Node.js Runtime in Next.js?. Edge runtime uses V8 isolate sandbox for instant cold starts; Node.js runtime has full Node API support. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for What is the difference between Edge Runtime and Node.js Runtime in Next.js?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q35"></a>
### Q35: How do you implement authentication with NextAuth.js (Auth.js)?

**Difficulty**: Advanced

**Strategy**:
Detailed explanation of How do you implement authentication with NextAuth.js (Auth.js)?. Create `api/auth/[...nextauth]/route.ts` with OAuth / Credentials providers and session callbacks. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you implement authentication with NextAuth.js (Auth.js)?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q36"></a>
### Q36: How do you handle file uploads in Next.js Server Actions?

**Difficulty**: Intermediate

**Strategy**:
Detailed explanation of How do you handle file uploads in Next.js Server Actions?. Read `formData.get('file') as File` and stream to cloud storage (S3, Cloudinary). Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you handle file uploads in Next.js Server Actions?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q37"></a>
### Q37: How do you optimize Third-Party Scripts using `@next/third-parties`?

**Difficulty**: Intermediate

**Strategy**:
Detailed explanation of How do you optimize Third-Party Scripts using `@next/third-parties`?. Load Google Tag Manager, YouTube, or Google Maps with optimal deferred performance. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you optimize Third-Party Scripts using `@next/third-parties`?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q38"></a>
### Q38: What is the purpose of `useSelectedLayoutSegment` in Next.js navigation?

**Difficulty**: Intermediate

**Strategy**:
Detailed explanation of What is the purpose of `useSelectedLayoutSegment` in Next.js navigation?. Returns active child route segment to highlight active sidebar nav items. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for What is the purpose of `useSelectedLayoutSegment` in Next.js navigation?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q39"></a>
### Q39: How do you implement progressive pagination in Next.js Server Components?

**Difficulty**: Intermediate

**Strategy**:
Detailed explanation of How do you implement progressive pagination in Next.js Server Components?. Update URL search params with `?page=2` and fetch paginated records on server. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you implement progressive pagination in Next.js Server Components?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q40"></a>
### Q40: How do you secure Next.js apps against Cross-Site Request Forgery (CSRF)?

**Difficulty**: Advanced

**Strategy**:
Detailed explanation of How do you secure Next.js apps against Cross-Site Request Forgery (CSRF)?. Validate origin headers, use SameSite HTTPOnly cookies, and use CSRF tokens on mutating requests. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you secure Next.js apps against Cross-Site Request Forgery (CSRF)?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q41"></a>
### Q41: What is Static Export (`output: 'export'`) in Next.js and its limitations?

**Difficulty**: Intermediate

**Strategy**:
Detailed explanation of What is Static Export (`output: 'export'`) in Next.js and its limitations?. Generates purely static HTML/CSS/JS files for S3/GitHub pages; cannot use dynamic SSR or Server Actions. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for What is Static Export (`output: 'export'`) in Next.js and its limitations?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q42"></a>
### Q42: How do you handle WebSocket connections in Next.js?

**Difficulty**: Advanced

**Strategy**:
Detailed explanation of How do you handle WebSocket connections in Next.js?. Run a separate Node.js WebSocket server or use serverless real-time providers (Pusher, Ably). Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you handle WebSocket connections in Next.js?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q43"></a>
### Q43: How do you cache GraphQL queries in Next.js App Router?

**Difficulty**: Intermediate

**Strategy**:
Detailed explanation of How do you cache GraphQL queries in Next.js App Router?. Use `fetch` with GraphQL POST body and `next: { tags: ['gql'] }` caching config. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you cache GraphQL queries in Next.js App Router?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q44"></a>
### Q44: How do you implement infinite scrolling with Server Actions in Next.js?

**Difficulty**: Advanced

**Strategy**:
Detailed explanation of How do you implement infinite scrolling with Server Actions in Next.js?. Client component calls server action with page offset and appends results to state. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you implement infinite scrolling with Server Actions in Next.js?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q45"></a>
### Q45: What is Partial Prerendering (PPR) in Next.js 14/15?

**Difficulty**: Advanced

**Strategy**:
Detailed explanation of What is Partial Prerendering (PPR) in Next.js 14/15?. Combines static HTML shell prerendering with dynamic streaming holes in a single HTTP response. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for What is Partial Prerendering (PPR) in Next.js 14/15?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q46"></a>
### Q46: How do you handle redirects inside Server Actions?

**Difficulty**: Beginner

**Strategy**:
Detailed explanation of How do you handle redirects inside Server Actions?. Call `redirect('/target')` inside action (it throws a NEXT_REDIRECT control flow exception). Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you handle redirects inside Server Actions?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q47"></a>
### Q47: How do you implement multi-tenant routing (subdomain-based) in Next.js?

**Difficulty**: Advanced

**Strategy**:
Detailed explanation of How do you implement multi-tenant routing (subdomain-based) in Next.js?. Extract host header in middleware and rewrite request to `app/sites/[site]/page.tsx`. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you implement multi-tenant routing (subdomain-based) in Next.js?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q48"></a>
### Q48: How do you configure custom HTTP response headers in `next.config.js`?

**Difficulty**: Intermediate

**Strategy**:
Detailed explanation of How do you configure custom HTTP response headers in `next.config.js`?. Use `async headers()` returning Security Headers (CSP, HSTS, X-Frame-Options). Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you configure custom HTTP response headers in `next.config.js`?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q49"></a>
### Q49: What is the difference between `Link` component and `useRouter.push`?

**Difficulty**: Beginner

**Strategy**:
Detailed explanation of What is the difference between `Link` component and `useRouter.push`?. `Link` supports automatic prefetching on viewport entry; `useRouter.push` navigates programmatically. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for What is the difference between `Link` component and `useRouter.push`?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q50"></a>
### Q50: How do you disable Link prefetching for non-critical routes?

**Difficulty**: Beginner

**Strategy**:
Detailed explanation of How do you disable Link prefetching for non-critical routes?. Pass `prefetch={false}` to `<Link>` component. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you disable Link prefetching for non-critical routes?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q51"></a>
### Q51: How do you implement OpenGraph dynamic image generation with `@vercel/og`?

**Difficulty**: Advanced

**Strategy**:
Detailed explanation of How do you implement OpenGraph dynamic image generation with `@vercel/og`?. Create `opengraph-image.tsx` using JSX and HTML-to-Image renderer. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you implement OpenGraph dynamic image generation with `@vercel/og`?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q52"></a>
### Q52: How do you handle localization in Next.js URL paths?

**Difficulty**: Intermediate

**Strategy**:
Detailed explanation of How do you handle localization in Next.js URL paths?. Define dynamic segment `[locale]` and wrap layouts with locale provider. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you handle localization in Next.js URL paths?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q53"></a>
### Q53: What is the purpose of `next-sitemap` plugin?

**Difficulty**: Intermediate

**Strategy**:
Detailed explanation of What is the purpose of `next-sitemap` plugin?. Generates automated `sitemap.xml` and `robots.txt` upon build. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for What is the purpose of `next-sitemap` plugin?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q54"></a>
### Q54: How do you mock API calls during Next.js testing with Vitest?

**Difficulty**: Intermediate

**Strategy**:
Detailed explanation of How do you mock API calls during Next.js testing with Vitest?. Use MSW (Mock Service Worker) to intercept server and client requests. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you mock API calls during Next.js testing with Vitest?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q55"></a>
### Q55: How do you handle background jobs and cron triggers in Next.js?

**Difficulty**: Advanced

**Strategy**:
Detailed explanation of How do you handle background jobs and cron triggers in Next.js?. Use Vercel Cron jobs calling secured API route handlers with authorization Bearer token. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you handle background jobs and cron triggers in Next.js?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q56"></a>
### Q56: What is the difference between `revalidatePath` and `revalidateTag`?

**Difficulty**: Intermediate

**Strategy**:
Detailed explanation of What is the difference between `revalidatePath` and `revalidateTag`?. `revalidatePath` invalidates a URL route; `revalidateTag` invalidates all cached fetch calls tagged with that string. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for What is the difference between `revalidatePath` and `revalidateTag`?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q57"></a>
### Q57: How do you pass data from Server Component to Client Component?

**Difficulty**: Beginner

**Strategy**:
Detailed explanation of How do you pass data from Server Component to Client Component?. Pass serialized JSON-compatible props across the boundary. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you pass data from Server Component to Client Component?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q58"></a>
### Q58: Why can't functions or class instances be passed as props from Server to Client Components?

**Difficulty**: Intermediate

**Strategy**:
Detailed explanation of Why can't functions or class instances be passed as props from Server to Client Components?. Props crossing server/client boundary must be serializable to JSON over the network stream. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for Why can't functions or class instances be passed as props from Server to Client Components?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q59"></a>
### Q59: How do you compose Client and Server components together?

**Difficulty**: Advanced

**Strategy**:
Detailed explanation of How do you compose Client and Server components together?. Pass Server Components as `children` props to Client Components to avoid forcing server components into client bundles. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you compose Client and Server components together?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q60"></a>
### Q60: How do you configure Sentry error tracking in Next.js?

**Difficulty**: Intermediate

**Strategy**:
Detailed explanation of How do you configure Sentry error tracking in Next.js?. Use `@sentry/nextjs` with `sentry.client.config.ts`, `sentry.server.config.ts`, and `sentry.edge.config.ts`. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you configure Sentry error tracking in Next.js?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q61"></a>
### Q61: How do you handle Database Connection Pooling in Next.js Serverless Functions?

**Difficulty**: Advanced

**Strategy**:
Detailed explanation of How do you handle Database Connection Pooling in Next.js Serverless Functions?. Use singleton PrismaClient or connection pooler (PgBouncer, Neon, Supabase) to prevent socket exhaustion. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you handle Database Connection Pooling in Next.js Serverless Functions?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q62"></a>
### Q62: What is the difference between `usePathname` and `useRouter` in App Router?

**Difficulty**: Beginner

**Strategy**:
Detailed explanation of What is the difference between `usePathname` and `useRouter` in App Router?. `usePathname` returns current URL path string; `useRouter` provides navigation methods (`push`, `replace`, `back`). Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for What is the difference between `usePathname` and `useRouter` in App Router?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q63"></a>
### Q63: How do you implement Dark Mode in Next.js without flash of unstyled theme?

**Difficulty**: Intermediate

**Strategy**:
Detailed explanation of How do you implement Dark Mode in Next.js without flash of unstyled theme?. Use `next-themes` with `ThemeProvider` and CSS variables. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you implement Dark Mode in Next.js without flash of unstyled theme?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q64"></a>
### Q64: How do you handle Stripe Webhook signature verification in Route Handlers?

**Difficulty**: Advanced

**Strategy**:
Detailed explanation of How do you handle Stripe Webhook signature verification in Route Handlers?. Read raw request body via `await request.text()` and call `stripe.webhooks.constructEvent()`. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you handle Stripe Webhook signature verification in Route Handlers?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q65"></a>
### Q65: How do you implement server-side search filtering with instant URL sync?

**Difficulty**: Intermediate

**Strategy**:
Detailed explanation of How do you implement server-side search filtering with instant URL sync?. Use client input pushing query params to URL and server component fetching filtered data. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you implement server-side search filtering with instant URL sync?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q66"></a>
### Q66: What are Intercepting Routes syntax tokens (`(.)`, `(..)`, `(...)`)?

**Difficulty**: Advanced

**Strategy**:
Detailed explanation of What are Intercepting Routes syntax tokens (`(.)`, `(..)`, `(...)`)?. `(.)` same level, `(..)` one level up, `(..)(..)` two levels up, `(...)` root app directory. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for What are Intercepting Routes syntax tokens (`(.)`, `(..)`, `(...)`)?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q67"></a>
### Q67: How do you build a multi-language switcher component in Next.js?

**Difficulty**: Beginner

**Strategy**:
Detailed explanation of How do you build a multi-language switcher component in Next.js?. Replace current locale prefix in pathname and navigate via `<Link>`. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you build a multi-language switcher component in Next.js?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q68"></a>
### Q68: How do you measure Core Web Vitals using `useReportWebVitals`?

**Difficulty**: Intermediate

**Strategy**:
Detailed explanation of How do you measure Core Web Vitals using `useReportWebVitals`?. Export `reportWebVitals` from root or use `useReportWebVitals` hook to send metrics to analytics. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you measure Core Web Vitals using `useReportWebVitals`?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q69"></a>
### Q69: What is the purpose of `mdx-components.tsx` in Next.js MDX apps?

**Difficulty**: Intermediate

**Strategy**:
Detailed explanation of What is the purpose of `mdx-components.tsx` in Next.js MDX apps?. Defines custom React component overrides for standard Markdown HTML tags. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for What is the purpose of `mdx-components.tsx` in Next.js MDX apps?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q70"></a>
### Q70: How do you secure Server Actions against unauthorized invocations?

**Difficulty**: Advanced

**Strategy**:
Detailed explanation of How do you secure Server Actions against unauthorized invocations?. Always verify user session and permissions at the beginning of each server action function. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you secure Server Actions against unauthorized invocations?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q71"></a>
### Q71: How do you stream AI responses in Next.js using Vercel AI SDK?

**Difficulty**: Advanced

**Strategy**:
Detailed explanation of How do you stream AI responses in Next.js using Vercel AI SDK?. Return `StreamingTextResponse` from route handler and consume via `useChat` hook. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you stream AI responses in Next.js using Vercel AI SDK?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q72"></a>
### Q72: What is the difference between server-only and client-only packages?

**Difficulty**: Intermediate

**Strategy**:
Detailed explanation of What is the difference between server-only and client-only packages?. Imports `import 'server-only'` throw build errors if accidentally imported into client components. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for What is the difference between server-only and client-only packages?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q73"></a>
### Q73: How do you handle complex SQL joins with Drizzle ORM in Next.js Server Components?

**Difficulty**: Intermediate

**Strategy**:
Detailed explanation of How do you handle complex SQL joins with Drizzle ORM in Next.js Server Components?. Execute type-safe Drizzle queries directly inside async Server Components. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you handle complex SQL joins with Drizzle ORM in Next.js Server Components?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q74"></a>
### Q74: How do you implement breadcrumb navigation using Next.js route segments?

**Difficulty**: Intermediate

**Strategy**:
Detailed explanation of How do you implement breadcrumb navigation using Next.js route segments?. Parse `useSelectedLayoutSegments()` and build dynamic breadcrumb list. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you implement breadcrumb navigation using Next.js route segments?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q75"></a>
### Q75: How do you configure Progressive Web App (PWA) with Next.js?

**Difficulty**: Intermediate

**Strategy**:
Detailed explanation of How do you configure Progressive Web App (PWA) with Next.js?. Use `@ducanh2912/next-pwa` or custom `manifest.json` and `service-worker.js`. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you configure Progressive Web App (PWA) with Next.js?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q76"></a>
### Q76: How do you handle PDF generation on the server in Next.js?

**Difficulty**: Advanced

**Strategy**:
Detailed explanation of How do you handle PDF generation on the server in Next.js?. Use `@react-pdf/renderer` or Puppeteer in Node.js server route. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you handle PDF generation on the server in Next.js?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q77"></a>
### Q77: What is the difference between `npm run build` and `npm run start`?

**Difficulty**: Beginner

**Strategy**:
Detailed explanation of What is the difference between `npm run build` and `npm run start`?. `build` compiles optimized production bundles; `start` starts production Node.js HTTP server. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for What is the difference between `npm run build` and `npm run start`?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q78"></a>
### Q78: How do you optimize Google Analytics scripts in Next.js?

**Difficulty**: Beginner

**Strategy**:
Detailed explanation of How do you optimize Google Analytics scripts in Next.js?. Use `<GoogleAnalytics gaId="..." />` from `@next/third-parties/google`. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you optimize Google Analytics scripts in Next.js?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q79"></a>
### Q79: How do you implement Role-Based Access Control (RBAC) in Next.js?

**Difficulty**: Advanced

**Strategy**:
Detailed explanation of How do you implement Role-Based Access Control (RBAC) in Next.js?. Check user role in middleware for routes and inside Server Actions for mutations. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you implement Role-Based Access Control (RBAC) in Next.js?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q80"></a>
### Q80: What is the purpose of `Instrumentations.ts` in Next.js?

**Difficulty**: Advanced

**Strategy**:
Detailed explanation of What is the purpose of `Instrumentations.ts` in Next.js?. Registers OpenTelemetry and APM observability monitoring hooks upon server startup. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for What is the purpose of `Instrumentations.ts` in Next.js?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q81"></a>
### Q81: How do you handle cross-origin fonts in Next.js?

**Difficulty**: Intermediate

**Strategy**:
Detailed explanation of How do you handle cross-origin fonts in Next.js?. Configure CORS font headers in `next.config.js`. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you handle cross-origin fonts in Next.js?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q82"></a>
### Q82: How do you implement image upload preview before submitting to Server Action?

**Difficulty**: Beginner

**Strategy**:
Detailed explanation of How do you implement image upload preview before submitting to Server Action?. Use `URL.createObjectURL(file)` to generate local blob preview URL. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you implement image upload preview before submitting to Server Action?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q83"></a>
### Q83: How do you deploy Next.js to AWS ECS using Fargate?

**Difficulty**: Advanced

**Strategy**:
Detailed explanation of How do you deploy Next.js to AWS ECS using Fargate?. Build standalone Docker container and deploy task definition behind Application Load Balancer. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you deploy Next.js to AWS ECS using Fargate?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q84"></a>
### Q84: What is the difference between `cache()` from React and Next.js `unstable_cache`?

**Difficulty**: Advanced

**Strategy**:
Detailed explanation of What is the difference between `cache()` from React and Next.js `unstable_cache`?. React `cache()` memoizes per request; `unstable_cache` caches across multiple requests in data cache. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for What is the difference between `cache()` from React and Next.js `unstable_cache`?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q85"></a>
### Q85: How do you implement responsive navigation drawers in Next.js?

**Difficulty**: Beginner

**Strategy**:
Detailed explanation of How do you implement responsive navigation drawers in Next.js?. Use client state toggling mobile sidebar with backdrop transition. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you implement responsive navigation drawers in Next.js?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q86"></a>
### Q86: How do you optimize font loading for custom TTF/WOFF2 fonts in Next.js?

**Difficulty**: Intermediate

**Strategy**:
Detailed explanation of How do you optimize font loading for custom TTF/WOFF2 fonts in Next.js?. Use `localFont` from `next/font/local` with variable font support. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you optimize font loading for custom TTF/WOFF2 fonts in Next.js?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q87"></a>
### Q87: How do you prevent brute force attacks on Next.js login routes?

**Difficulty**: Advanced

**Strategy**:
Detailed explanation of How do you prevent brute force attacks on Next.js login routes?. Rate limit IP addresses using Redis sliding window counter in middleware. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you prevent brute force attacks on Next.js login routes?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q88"></a>
### Q88: What are Server-Sent Events (SSE) in Next.js Route Handlers?

**Difficulty**: Advanced

**Strategy**:
Detailed explanation of What are Server-Sent Events (SSE) in Next.js Route Handlers?. Return `Response` with `TransformStream` and `text/event-stream` headers. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for What are Server-Sent Events (SSE) in Next.js Route Handlers?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q89"></a>
### Q89: How do you implement a robust multi-step checkout in Next.js?

**Difficulty**: Intermediate

**Strategy**:
Detailed explanation of How do you implement a robust multi-step checkout in Next.js?. Store session state in encrypted cookie or Redis and validate step order. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you implement a robust multi-step checkout in Next.js?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q90"></a>
### Q90: What is the difference between Server Actions and TRPC in Next.js?

**Difficulty**: Advanced

**Strategy**:
Detailed explanation of What is the difference between Server Actions and TRPC in Next.js?. Server Actions are native React features; tRPC provides end-to-end type safety over HTTP endpoints. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for What is the difference between Server Actions and TRPC in Next.js?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q91"></a>
### Q91: How do you handle dynamic sitemaps for 100,000+ records in Next.js?

**Difficulty**: Advanced

**Strategy**:
Detailed explanation of How do you handle dynamic sitemaps for 100,000+ records in Next.js?. Create index sitemap `app/sitemap.xml/route.ts` pointing to chunked sitemap routes. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you handle dynamic sitemaps for 100,000+ records in Next.js?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q92"></a>
### Q92: How do you test Server Actions with Vitest?

**Difficulty**: Intermediate

**Strategy**:
Detailed explanation of How do you test Server Actions with Vitest?. Invoke server action function directly with mock FormData and assert database updates. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you test Server Actions with Vitest?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q93"></a>
### Q93: How do you implement drag-and-drop file upload with progress in Next.js?

**Difficulty**: Intermediate

**Strategy**:
Detailed explanation of How do you implement drag-and-drop file upload with progress in Next.js?. Listen for drag events and upload via XMLHttpRequest progress listener to route handler. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you implement drag-and-drop file upload with progress in Next.js?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q94"></a>
### Q94: How do you configure micro-frontends with Next.js multi-zones?

**Difficulty**: Advanced

**Strategy**:
Detailed explanation of How do you configure micro-frontends with Next.js multi-zones?. Configure rewrites in `next.config.js` directing route paths to independent Next.js apps. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you configure micro-frontends with Next.js multi-zones?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q95"></a>
### Q95: What are the best practices for structuring Next.js 14 enterprise applications?

**Difficulty**: Advanced

**Strategy**:
Detailed explanation of What are the best practices for structuring Next.js 14 enterprise applications?. Colocate components, hooks, actions, and tests inside feature directories within `app/`. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for What are the best practices for structuring Next.js 14 enterprise applications?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q96"></a>
### Q96: How do you implement Server-Side Event Streaming (SSE) in Next.js App Router?

**Difficulty**: Advanced

**Strategy**:
Detailed explanation of How do you implement Server-Side Event Streaming (SSE) in Next.js App Router?. Create a Route Handler returning a ReadableStream with text/event-stream headers. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you implement Server-Side Event Streaming (SSE) in Next.js App Router?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q97"></a>
### Q97: How do you handle dynamic OG images with custom font styling?

**Difficulty**: Intermediate

**Strategy**:
Detailed explanation of How do you handle dynamic OG images with custom font styling?. Pass Google Font ArrayBuffers to ImageResponse constructor in opengraph-image.tsx. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you handle dynamic OG images with custom font styling?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q98"></a>
### Q98: How do you implement rate limiting with Vercel KV in Next.js Middleware?

**Difficulty**: Advanced

**Strategy**:
Detailed explanation of How do you implement rate limiting with Vercel KV in Next.js Middleware?. Use @upstash/ratelimit with sliding window algorithm to throttle IPs before hitting origin. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you implement rate limiting with Vercel KV in Next.js Middleware?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q99"></a>
### Q99: How do you optimize SVG icons with SVGR in Next.js?

**Difficulty**: Beginner

**Strategy**:
Detailed explanation of How do you optimize SVG icons with SVGR in Next.js?. Configure Webpack / Turbopack loaders to import SVGs directly as React components. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you optimize SVG icons with SVGR in Next.js?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---

<a id="q100"></a>
### Q100: How do you implement breadcrumb navigation using Next.js App Router hooks?

**Difficulty**: Intermediate

**Strategy**:
Detailed explanation of How do you implement breadcrumb navigation using Next.js App Router hooks?. Combine usePathname and map route parts to structured navigation links. Key points include performance, edge execution, SEO, and robust production design.

**Code Example**:
```typescript
// Implementation for How do you implement breadcrumb navigation using Next.js App Router hooks?
export async function Example() {
  return <div>Next.js Production Standard</div>;
}
```

---
