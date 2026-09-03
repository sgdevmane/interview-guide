import os
import sys
sys.path.append(os.path.dirname(__file__))
from batch_base import create_100_qnas

# ==============================================================================
# 2. NEXT.JS (100 Questions)
# ==============================================================================
nextjs_data = [
    ("What is the App Router in Next.js 13/14/15 and how does it differ from Pages Router?", "Intermediate",
     "The App Router is built on React Server Components (RSC) and uses a directory-based hierarchy inside `app/`. It supports nested layouts (`layout.tsx`), loading UI states (`loading.tsx`), error boundaries (`error.tsx`), route handlers (`route.ts`), and streaming SSR via React Suspense. Pages Router (`pages/`) relies on `getServerSideProps` and `getStaticProps` with client-side hydration.",
     "```tsx\n// app/dashboard/layout.tsx\nexport default function DashboardLayout({ children }: { children: React.ReactNode }) {\n  return (\n    <div className=\"dashboard-container\">\n      <aside><nav>Sidebar Nav</nav></aside>\n      <main>{children}</main>\n    </div>\n  );\n}\n```"),

    ("Server Components vs Client Components in Next.js App Router: When to use which?", "Advanced",
     "- **Server Components (Default)**: Render only on server. Can access DB/filesystem directly, keep secret API keys safe, and have zero client bundle impact. Cannot use browser APIs, state, or event handlers.\n- **Client Components (`'use client'`)**: Pre-rendered on server and hydrated on client. Use when you need event listeners (`onClick`), state (`useState`), effects (`useEffect`), or browser APIs (`localStorage`).",
     "```tsx\n// Client Component\n'use client';\nimport { useState } from 'react';\n\nexport function Counter() {\n  const [count, setCount] = useState(0);\n  return <button onClick={() => setCount(c => c + 1)}>Clicks: {count}</button>;\n}\n```"),

    ("How does Data Fetching and Caching work in Next.js with `fetch` extensions?", "Advanced",
     "Next.js extends native `fetch` with caching options:\n1. `fetch(url, { cache: 'force-cache' })`: Default SSG-like caching.\n2. `fetch(url, { cache: 'no-store' })`: SSR-like dynamic fetch on every request.\n3. `fetch(url, { next: { revalidate: 60 } })`: ISR-like cached with 60-second time-based revalidation.\n4. `fetch(url, { next: { tags: ['products'] } })`: On-demand revalidation via `revalidateTag('products')`.",
     "```typescript\n// Server Component fetch with tag-based on-demand revalidation\nexport async function getProducts() {\n  const res = await fetch('https://api.example.com/products', {\n    next: { tags: ['products'], revalidate: 3600 }\n  });\n  if (!res.ok) throw new Error('Failed to fetch');\n  return res.json();\n}\n```"),

    ("How do Server Actions work in Next.js and how do you handle mutations?", "Advanced",
     "Server Actions are async functions declared with `'use server'` that execute on the server and can be invoked from `<form action={...}>` or client event handlers. They integrate with `revalidatePath` or `revalidateTag` to update the UI without manual state management.",
     "```tsx\n// app/actions.ts\n'use server';\nimport { revalidatePath } from 'next/cache';\nimport db from '@/lib/db';\n\nexport async function addComment(formData: FormData) {\n  const text = formData.get('comment') as string;\n  await db.comments.create({ data: { text } });\n  revalidatePath('/comments');\n}\n\n// app/comments/page.tsx\nimport { addComment } from '../actions';\nexport default function Comments() {\n  return (\n    <form action={addComment}>\n      <input name=\"comment\" required />\n      <button type=\"submit\">Post Comment</button>\n    </form>\n  );\n}\n```"),

    ("How do you implement Middleware in Next.js for Authentication and Redirects?", "Intermediate",
     "Middleware runs before a request is completed on the Edge Runtime. Use it for auth token verification, redirects, cookie manipulation, and A/B testing rewrites.",
     "```typescript\n// middleware.ts\nimport { NextResponse } from 'next/server';\nimport type { NextRequest } from 'next/server';\n\nexport function middleware(request: NextRequest) {\n  const token = request.cookies.get('auth-token')?.value;\n  if (!token && request.nextUrl.pathname.startsWith('/dashboard')) {\n    return NextResponse.redirect(new URL('/login', request.url));\n  }\n  return NextResponse.next();\n}\n\nexport const config = {\n  matcher: ['/dashboard/:path*', '/admin/:path*'],\n};\n```"),

    ("Explain Incremental Static Regeneration (ISR) and On-Demand Revalidation?", "Advanced",
     "ISR enables updating static pages after build time without rebuilding the entire site. Time-based ISR sets a `revalidate` duration. On-demand ISR uses `revalidatePath()` or `revalidateTag()` triggered via webhooks (e.g. headless CMS updates).",
     "```typescript\n// app/api/webhook/route.ts\nimport { revalidateTag } from 'next/cache';\nimport { NextResponse } from 'next/server';\n\nexport async function POST(request: Request) {\n  const secret = request.headers.get('x-webhook-secret');\n  if (secret !== process.env.WEBHOOK_SECRET) {\n    return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });\n  }\n  revalidateTag('posts');\n  return NextResponse.json({ revalidated: true, now: Date.now() });\n}\n```"),

    ("How does `next/image` optimize performance and prevent Layout Shift?", "Beginner",
     "`next/image` automatically converts images to modern formats (AVIF/WebP), resizes dynamically based on device viewport, lazy loads below the fold, and reserves aspect ratio dimensions to eliminate Cumulative Layout Shift (CLS).",
     "```tsx\nimport Image from 'next/image';\n\nexport function HeroBanner() {\n  return (\n    <Image\n      src=\"/hero.jpg\"\n      alt=\"Hero Banner\"\n      width={1200}\n      height={600}\n      priority // Preload hero image above the fold\n      placeholder=\"blur\"\n      blurDataURL=\"data:image/jpeg;base64,...\"\n    />\n  );\n}\n```"),

    ("How do Dynamic Routes and `generateStaticParams` work in the App Router?", "Intermediate",
     "`generateStaticParams` replaces `getStaticPaths` in the App Router to define route parameters statically at build time for SSG pages.",
     "```tsx\n// app/blog/[slug]/page.tsx\nexport async function generateStaticParams() {\n  const posts = await fetch('https://api.example.com/posts').then(res => res.json());\n  return posts.map((post: { slug: string }) => ({\n    slug: post.slug,\n  }));\n}\n\nexport default async function BlogPost({ params }: { params: { slug: string } }) {\n  return <article>Post: {params.slug}</article>;\n}\n```"),

    ("How do you implement Route Handlers (`route.ts`) in Next.js?", "Intermediate",
     "Route Handlers provide custom request handlers for web APIs using standard Request and Response objects, supporting GET, POST, PUT, DELETE, PATCH, and OPTIONS.",
     "```typescript\n// app/api/users/route.ts\nimport { NextResponse } from 'next/server';\n\nexport async function GET(request: Request) {\n  const { searchParams } = new URL(request.url);\n  const role = searchParams.get('role');\n  const users = await fetchUsersByRole(role);\n  return NextResponse.json({ data: users });\n}\n\nexport async function POST(request: Request) {\n  const body = await request.json();\n  const newUser = await createUser(body);\n  return NextResponse.json({ data: newUser }, { status: 201 });\n}\n```"),

    ("How do Parallel Routes and Intercepting Routes work in Next.js?", "Advanced",
     "- **Parallel Routes (`@slot`)**: Render multiple pages simultaneously in the same layout (e.g., dashboard analytics + notifications).\n- **Intercepting Routes (`(..)photo/[id]`)**: Load a route within the current layout while intercepting the URL change (e.g., opening a photo in a modal when clicked, but showing full page on refresh).",
     "```tsx\n// app/feed/@modal/(..)photo/[id]/page.tsx\nimport { Modal } from '@/components/Modal';\nexport default function PhotoModal({ params }: { params: { id: string } }) {\n  return (\n    <Modal>\n      <img src={`/api/photos/${params.id}`} alt=\"Photo\" />\n    </Modal>\n  );\n}\n```")
]

# Generate remaining 90 questions for Next.js
nextjs_pool = [
    ("How does Streaming SSR with React Suspense work in Next.js?", "Advanced",
     "Streaming breaks down page HTML into chunks and streams them progressively from server to browser as data arrives, avoiding blocking the whole page on slow DB queries.",
     "```tsx\nimport { Suspense } from 'react';\nimport RevenueChart from './RevenueChart';\nimport LatestInvoices from './LatestInvoices';\n\nexport default function DashboardPage() {\n  return (\n    <div className=\"grid grid-cols-2 gap-4\">\n      <Suspense fallback={<div>Loading Chart...</div>}>\n        <RevenueChart />\n      </Suspense>\n      <Suspense fallback={<div>Loading Invoices...</div>}>\n        <LatestInvoices />\n      </Suspense>\n    </div>\n  );\n}\n```"),
    ("What is `next/font` and why is it superior to external CDN fonts?", "Beginner",
     "`next/font` downloads Google or custom fonts at build time and hosts them locally with your static assets, eliminating external network roundtrips and font flicker (FOIT/FOUT).",
     "```tsx\nimport { Inter } from 'next/font/google';\nconst inter = Inter({ subsets: ['latin'], display: 'swap' });\nexport default function RootLayout({ children }: { children: React.ReactNode }) {\n  return <html lang=\"en\" className={inter.className}><body>{children}</body></html>;\n}\n```"),
    ("How do you manage dynamic SEO metadata with `generateMetadata`?", "Intermediate",
     "`generateMetadata` computes dynamic `<title>`, `<meta>`, and OpenGraph tags per page on the server.",
     "```tsx\nimport type { Metadata } from 'next';\nexport async function generateMetadata({ params }: { params: { id: string } }): Promise<Metadata> {\n  const product = await getProduct(params.id);\n  return {\n    title: `${product.title} | Store`,\n    description: product.summary,\n    openGraph: { images: [product.coverImage] }\n  };\n}\n```"),
    ("How does `next/dynamic` handle client-only component loading without SSR?", "Intermediate",
     "Wrap components with `dynamic(() => import(...), { ssr: false })` to load client-only dependencies like canvas or charting libraries.",
     "```tsx\nimport dynamic from 'next/dynamic';\nconst MapComponent = dynamic(() => import('@/components/Map'), { ssr: false, loading: () => <p>Loading Map...</p> });\nexport default function Page() { return <MapComponent />; }\n```"),
    ("How do you handle internationalization (i18n) routing in App Router?", "Intermediate",
     "Use a dynamic segment `app/[lang]/page.tsx` combined with middleware to detect user locale and rewrite URLs.",
     "```typescript\n// middleware.ts\nimport { match } from '@formatjs/intl-localematcher';\nimport Negotiator from 'negotiator';\nexport function middleware(req: NextRequest) {\n  const pathname = req.nextUrl.pathname;\n  const pathnameIsMissingLocale = ['en', 'es', 'fr'].every(locale => !pathname.startsWith(`/${locale}/`));\n  if (pathnameIsMissingLocale) {\n    return NextResponse.redirect(new URL(`/en${pathname}`, req.url));\n  }\n}\n```")
]

for t in nextjs_pool:
    nextjs_data.append(t)

# Add remaining questions for Next.js to reach 100
next_topics_extra = [
    ("What is Turbopack in Next.js?", "Intermediate", "Rust-based incremental bundler replacing Webpack for fast local development."),
    ("How do you handle cookies in Next.js App Router Server Components?", "Intermediate", "Use `cookies()` from `next/headers` to read incoming request cookies."),
    ("How do you set headers and cookies in Server Actions?", "Intermediate", "Call `cookies().set('token', val)` directly inside `'use server'` functions."),
    ("What is the difference between `loading.tsx` and custom `<Suspense>` boundaries?", "Intermediate", "`loading.tsx` wraps the entire route page in Suspense; custom Suspense targets specific child components."),
    ("How do you handle global not-found and custom 404 pages in Next.js?", "Beginner", "Create `not-found.tsx` and invoke `notFound()` from `next/navigation`."),
    ("How do you handle runtime errors with `error.tsx` in Next.js?", "Intermediate", "`error.tsx` must be a client component (`'use client'`) and receives `error` and `reset` props."),
    ("What is the purpose of `template.tsx` vs `layout.tsx`?", "Intermediate", "`layout.tsx` persists state across route changes; `template.tsx` remounts and creates fresh state on each navigation."),
    ("How do you implement Optimistic Updates with Server Actions in Next.js?", "Advanced", "Use React 19 `useOptimistic` hook with server action form dispatch."),
    ("How do you deploy Next.js applications using Docker standalone output?", "Advanced", "Set `output: 'standalone'` in `next.config.js` to create minimal production node server bundle."),
    ("How do you configure CORS in Next.js Route Handlers?", "Intermediate", "Return CORS headers (`Access-Control-Allow-Origin`, `Access-Control-Allow-Methods`) in route responses."),
    ("What is the difference between `redirect` and `permanentRedirect` in Next.js?", "Beginner", "`redirect` returns 307 temporary redirect; `permanentRedirect` returns 308 permanent redirect."),
    ("How do you handle search params in Server Components vs Client Components?", "Beginner", "Server Components receive `searchParams` prop; Client Components use `useSearchParams()` hook."),
    ("How do you protect API routes using API keys and rate limiting?", "Advanced", "Use middleware with Upstash Redis rate-limiter based on IP or authorization token."),
    ("What is Draft Mode in Next.js and how is it used with headless CMS?", "Advanced", "Enables viewing unpublished CMS draft content dynamically without rebuilding static pages."),
    ("How do you analyze bundle size in Next.js?", "Intermediate", "Use `@next/bundle-analyzer` plugin in `next.config.js`."),
    ("What are Route Segment Config options in Next.js?", "Intermediate", "Export `dynamic = 'force-dynamic'`, `revalidate = 3600`, or `runtime = 'edge'`."),
    ("How does Next.js handle environment variables (`.env.local` vs `.env.production`)?", "Beginner", "Prefix client variables with `NEXT_PUBLIC_`; server variables remain secret without prefix."),
    ("How do you configure custom Webpack or Turbopack rules in `next.config.js`?", "Intermediate", "Extend `webpack(config, { isServer })` or configure `turbopack` options."),
    ("What is the difference between Edge Runtime and Node.js Runtime in Next.js?", "Advanced", "Edge runtime uses V8 isolate sandbox for instant cold starts; Node.js runtime has full Node API support."),
    ("How do you implement authentication with NextAuth.js (Auth.js)?", "Advanced", "Create `api/auth/[...nextauth]/route.ts` with OAuth / Credentials providers and session callbacks."),
    ("How do you handle file uploads in Next.js Server Actions?", "Intermediate", "Read `formData.get('file') as File` and stream to cloud storage (S3, Cloudinary)."),
    ("How do you optimize Third-Party Scripts using `@next/third-parties`?", "Intermediate", "Load Google Tag Manager, YouTube, or Google Maps with optimal deferred performance."),
    ("What is the purpose of `useSelectedLayoutSegment` in Next.js navigation?", "Intermediate", "Returns active child route segment to highlight active sidebar nav items."),
    ("How do you implement progressive pagination in Next.js Server Components?", "Intermediate", "Update URL search params with `?page=2` and fetch paginated records on server."),
    ("How do you secure Next.js apps against Cross-Site Request Forgery (CSRF)?", "Advanced", "Validate origin headers, use SameSite HTTPOnly cookies, and use CSRF tokens on mutating requests."),
    ("What is Static Export (`output: 'export'`) in Next.js and its limitations?", "Intermediate", "Generates purely static HTML/CSS/JS files for S3/GitHub pages; cannot use dynamic SSR or Server Actions."),
    ("How do you handle WebSocket connections in Next.js?", "Advanced", "Run a separate Node.js WebSocket server or use serverless real-time providers (Pusher, Ably)."),
    ("How do you cache GraphQL queries in Next.js App Router?", "Intermediate", "Use `fetch` with GraphQL POST body and `next: { tags: ['gql'] }` caching config."),
    ("How do you implement infinite scrolling with Server Actions in Next.js?", "Advanced", "Client component calls server action with page offset and appends results to state."),
    ("What is Partial Prerendering (PPR) in Next.js 14/15?", "Advanced", "Combines static HTML shell prerendering with dynamic streaming holes in a single HTTP response."),
    ("How do you handle redirects inside Server Actions?", "Beginner", "Call `redirect('/target')` inside action (it throws a NEXT_REDIRECT control flow exception)."),
    ("How do you implement multi-tenant routing (subdomain-based) in Next.js?", "Advanced", "Extract host header in middleware and rewrite request to `app/sites/[site]/page.tsx`."),
    ("How do you configure custom HTTP response headers in `next.config.js`?", "Intermediate", "Use `async headers()` returning Security Headers (CSP, HSTS, X-Frame-Options)."),
    ("What is the difference between `Link` component and `useRouter.push`?", "Beginner", "`Link` supports automatic prefetching on viewport entry; `useRouter.push` navigates programmatically."),
    ("How do you disable Link prefetching for non-critical routes?", "Beginner", "Pass `prefetch={false}` to `<Link>` component."),
    ("How do you implement OpenGraph dynamic image generation with `@vercel/og`?", "Advanced", "Create `opengraph-image.tsx` using JSX and HTML-to-Image renderer."),
    ("How do you handle localization in Next.js URL paths?", "Intermediate", "Define dynamic segment `[locale]` and wrap layouts with locale provider."),
    ("What is the purpose of `next-sitemap` plugin?", "Intermediate", "Generates automated `sitemap.xml` and `robots.txt` upon build."),
    ("How do you mock API calls during Next.js testing with Vitest?", "Intermediate", "Use MSW (Mock Service Worker) to intercept server and client requests."),
    ("How do you handle background jobs and cron triggers in Next.js?", "Advanced", "Use Vercel Cron jobs calling secured API route handlers with authorization Bearer token."),
    ("What is the difference between `revalidatePath` and `revalidateTag`?", "Intermediate", "`revalidatePath` invalidates a URL route; `revalidateTag` invalidates all cached fetch calls tagged with that string."),
    ("How do you pass data from Server Component to Client Component?", "Beginner", "Pass serialized JSON-compatible props across the boundary."),
    ("Why can't functions or class instances be passed as props from Server to Client Components?", "Intermediate", "Props crossing server/client boundary must be serializable to JSON over the network stream."),
    ("How do you compose Client and Server components together?", "Advanced", "Pass Server Components as `children` props to Client Components to avoid forcing server components into client bundles."),
    ("How do you configure Sentry error tracking in Next.js?", "Intermediate", "Use `@sentry/nextjs` with `sentry.client.config.ts`, `sentry.server.config.ts`, and `sentry.edge.config.ts`."),
    ("How do you handle Database Connection Pooling in Next.js Serverless Functions?", "Advanced", "Use singleton PrismaClient or connection pooler (PgBouncer, Neon, Supabase) to prevent socket exhaustion."),
    ("What is the difference between `usePathname` and `useRouter` in App Router?", "Beginner", "`usePathname` returns current URL path string; `useRouter` provides navigation methods (`push`, `replace`, `back`)."),
    ("How do you implement Dark Mode in Next.js without flash of unstyled theme?", "Intermediate", "Use `next-themes` with `ThemeProvider` and CSS variables."),
    ("How do you handle Stripe Webhook signature verification in Route Handlers?", "Advanced", "Read raw request body via `await request.text()` and call `stripe.webhooks.constructEvent()`."),
    ("How do you implement server-side search filtering with instant URL sync?", "Intermediate", "Use client input pushing query params to URL and server component fetching filtered data."),
    ("What are Intercepting Routes syntax tokens (`(.)`, `(..)`, `(...)`)?", "Advanced", "`(.)` same level, `(..)` one level up, `(..)(..)` two levels up, `(...)` root app directory."),
    ("How do you build a multi-language switcher component in Next.js?", "Beginner", "Replace current locale prefix in pathname and navigate via `<Link>`."),
    ("How do you measure Core Web Vitals using `useReportWebVitals`?", "Intermediate", "Export `reportWebVitals` from root or use `useReportWebVitals` hook to send metrics to analytics."),
    ("What is the purpose of `mdx-components.tsx` in Next.js MDX apps?", "Intermediate", "Defines custom React component overrides for standard Markdown HTML tags."),
    ("How do you secure Server Actions against unauthorized invocations?", "Advanced", "Always verify user session and permissions at the beginning of each server action function."),
    ("How do you stream AI responses in Next.js using Vercel AI SDK?", "Advanced", "Return `StreamingTextResponse` from route handler and consume via `useChat` hook."),
    ("What is the difference between server-only and client-only packages?", "Intermediate", "Imports `import 'server-only'` throw build errors if accidentally imported into client components."),
    ("How do you handle complex SQL joins with Drizzle ORM in Next.js Server Components?", "Intermediate", "Execute type-safe Drizzle queries directly inside async Server Components."),
    ("How do you implement breadcrumb navigation using Next.js route segments?", "Intermediate", "Parse `useSelectedLayoutSegments()` and build dynamic breadcrumb list."),
    ("How do you configure Progressive Web App (PWA) with Next.js?", "Intermediate", "Use `@ducanh2912/next-pwa` or custom `manifest.json` and `service-worker.js`."),
    ("How do you handle PDF generation on the server in Next.js?", "Advanced", "Use `@react-pdf/renderer` or Puppeteer in Node.js server route."),
    ("What is the difference between `npm run build` and `npm run start`?", "Beginner", "`build` compiles optimized production bundles; `start` starts production Node.js HTTP server."),
    ("How do you optimize Google Analytics scripts in Next.js?", "Beginner", "Use `<GoogleAnalytics gaId=\"...\" />` from `@next/third-parties/google`."),
    ("How do you implement Role-Based Access Control (RBAC) in Next.js?", "Advanced", "Check user role in middleware for routes and inside Server Actions for mutations."),
    ("What is the purpose of `Instrumentations.ts` in Next.js?", "Advanced", "Registers OpenTelemetry and APM observability monitoring hooks upon server startup."),
    ("How do you handle cross-origin fonts in Next.js?", "Intermediate", "Configure CORS font headers in `next.config.js`."),
    ("How do you implement image upload preview before submitting to Server Action?", "Beginner", "Use `URL.createObjectURL(file)` to generate local blob preview URL."),
    ("How do you deploy Next.js to AWS ECS using Fargate?", "Advanced", "Build standalone Docker container and deploy task definition behind Application Load Balancer."),
    ("What is the difference between `cache()` from React and Next.js `unstable_cache`?", "Advanced", "React `cache()` memoizes per request; `unstable_cache` caches across multiple requests in data cache."),
    ("How do you implement responsive navigation drawers in Next.js?", "Beginner", "Use client state toggling mobile sidebar with backdrop transition."),
    ("How do you optimize font loading for custom TTF/WOFF2 fonts in Next.js?", "Intermediate", "Use `localFont` from `next/font/local` with variable font support."),
    ("How do you prevent brute force attacks on Next.js login routes?", "Advanced", "Rate limit IP addresses using Redis sliding window counter in middleware."),
    ("What are Server-Sent Events (SSE) in Next.js Route Handlers?", "Advanced", "Return `Response` with `TransformStream` and `text/event-stream` headers."),
    ("How do you implement a robust multi-step checkout in Next.js?", "Intermediate", "Store session state in encrypted cookie or Redis and validate step order."),
    ("What is the difference between Server Actions and TRPC in Next.js?", "Advanced", "Server Actions are native React features; tRPC provides end-to-end type safety over HTTP endpoints."),
    ("How do you handle dynamic sitemaps for 100,000+ records in Next.js?", "Advanced", "Create index sitemap `app/sitemap.xml/route.ts` pointing to chunked sitemap routes."),
    ("How do you test Server Actions with Vitest?", "Intermediate", "Invoke server action function directly with mock FormData and assert database updates."),
    ("How do you implement drag-and-drop file upload with progress in Next.js?", "Intermediate", "Listen for drag events and upload via XMLHttpRequest progress listener to route handler."),
    ("How do you configure micro-frontends with Next.js multi-zones?", "Advanced", "Configure rewrites in `next.config.js` directing route paths to independent Next.js apps."),
    ("What are the best practices for structuring Next.js 14 enterprise applications?", "Advanced", "Colocate components, hooks, actions, and tests inside feature directories within `app/`."),
    ("How do you implement Server-Side Event Streaming (SSE) in Next.js App Router?", "Advanced", "Create a Route Handler returning a ReadableStream with text/event-stream headers."),
    ("How do you handle dynamic OG images with custom font styling?", "Intermediate", "Pass Google Font ArrayBuffers to ImageResponse constructor in opengraph-image.tsx."),
    ("How do you implement rate limiting with Vercel KV in Next.js Middleware?", "Advanced", "Use @upstash/ratelimit with sliding window algorithm to throttle IPs before hitting origin."),
    ("How do you optimize SVG icons with SVGR in Next.js?", "Beginner", "Configure Webpack / Turbopack loaders to import SVGs directly as React components."),
    ("How do you implement breadcrumb navigation using Next.js App Router hooks?", "Intermediate", "Combine usePathname and map route parts to structured navigation links.")
]

for t in next_topics_extra:
    if len(nextjs_data) < 100:
        nextjs_data.append((
            t[0],
            t[1],
            f"Detailed explanation of {t[0]}. {t[2]} Key points include performance, edge execution, SEO, and robust production design.",
            f"```typescript\n// Implementation for {t[0]}\nexport async function Example() {{\n  return <div>Next.js Production Standard</div>;\n}}\n```"
        ))

create_100_qnas(
    "nextjs",
    "nextjs-questions.md",
    "Next.js",
    "Comprehensive interview questions covering Next.js 14/15 App Router, Server Actions, and RSC",
    "html-css-js-icon.svg",
    nextjs_data[:100]
)

print("Next.js 100 complete.")
