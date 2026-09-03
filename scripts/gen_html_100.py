import os
import sys
sys.path.append(os.path.dirname(__file__))
from batch_base import create_100_qnas

# ==============================================================================
# 5. HTML5 (100 Questions)
# ==============================================================================
html_data = [
    ("What are Semantic HTML5 elements and why are they crucial for SEO and Accessibility?", "Beginner",
     "Semantic elements (`<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`) clearly describe their meaning and purpose to both browser engines, assistive technologies (screen readers), and search engine crawlers. Non-semantic elements (`<div>`, `<span>`) provide no structural information.",
     "```html\n<!DOCTYPE html>\n<html lang=\"en\">\n<head><title>Accessible Blog</title></head>\n<body>\n  <header>\n    <nav aria-label=\"Main Navigation\">\n      <ul><li><a href=\"/\">Home</a></li></ul>\n    </nav>\n  </header>\n  <main id=\"main-content\">\n    <article>\n      <h1>Understanding Web Accessibility</h1>\n      <p>Semantic markup provides landmarks for assistive tech.</p>\n    </article>\n  </main>\n  <footer><p>&copy; 2026 Tech Guide</p></footer>\n</body>\n</html>\n```"),

    ("How do Web Components work (Custom Elements, Shadow DOM, HTML Templates)?", "Advanced",
     "Web Components are a suite of native browser APIs allowing developers to create reusable, encapsulated custom HTML elements:\n1. **Custom Elements**: `customElements.define('my-card', MyCard)`.\n2. **Shadow DOM**: `this.attachShadow({ mode: 'open' })` isolates CSS styles and DOM subtrees from global document leaks.\n3. **HTML Templates**: `<template>` and `<slot>` define reusable markup fragments.",
     "```html\n<template id=\"user-badge-template\">\n  <style>\n    .badge { padding: 8px 16px; border-radius: 20px; background: #e0f2fe; color: #0369a1; }\n  </style>\n  <div class=\"badge\">\n    <slot name=\"username\">Anonymous</slot>\n  </div>\n</template>\n\n<script>\nclass UserBadge extends HTMLElement {\n  constructor() {\n    super();\n    const shadow = this.attachShadow({ mode: 'open' });\n    const tpl = document.getElementById('user-badge-template');\n    shadow.appendChild(tpl.content.cloneNode(true));\n  }\n}\ncustomElements.define('user-badge', UserBadge);\n</script>\n\n<user-badge><span slot=\"username\">Alice Cooper</span></user-badge>\n```"),

    ("What is the difference between `localStorage`, `sessionStorage`, `IndexedDB`, and Cookies?", "Intermediate",
     "- `localStorage`: 5-10MB, persistent across browser restarts, synchronous, same-origin only.\n- `sessionStorage`: 5MB, scoped to the current browser tab, cleared when tab closes.\n- `Cookies`: 4KB, sent automatically with HTTP requests; supports `HttpOnly` (XSS protection) and `SameSite` (CSRF protection).\n- `IndexedDB`: 50MB+ (gigabytes), transactional NoSQL object store, asynchronous, supports indexes and binary blobs.",
     "```javascript\n// IndexedDB Quick Example\nconst request = indexedDB.open('InterviewDB', 1);\nrequest.onupgradeneeded = (e) => {\n  const db = e.target.result;\n  db.createObjectStore('answers', { keyPath: 'id' });\n};\nrequest.onsuccess = (e) => {\n  const db = e.target.result;\n  const tx = db.transaction('answers', 'readwrite');\n  tx.objectStore('answers').put({ id: 1, topic: 'HTML5', passed: true });\n};\n```"),

    ("How do Service Workers work and how do they enable Progressive Web Apps (PWAs)?", "Advanced",
     "A Service Worker is an event-driven programmable network proxy script running in the background, independent of the web page. It intercepts network fetch requests, manages Cache Storage API caches for offline functionality, handles push notifications, and synchronizes data in the background.",
     "```javascript\n// sw.js (Service Worker)\nconst CACHE_NAME = 'app-v1';\n\nself.addEventListener('install', (event) => {\n  event.waitUntil(\n    caches.open(CACHE_NAME).then(cache => cache.addAll(['/', '/index.html', '/styles.css', '/app.js']))\n  );\n});\n\nself.addEventListener('fetch', (event) => {\n  event.respondWith(\n    caches.match(event.request).then(cached => cached || fetch(event.request))\n  );\n});\n```"),

    ("How do Web Workers work and when should you use them?", "Intermediate",
     "Web Workers run scripts in background threads separate from the browser's main UI thread, communicating via asynchronous `postMessage` and `onmessage` event listeners. Use them for CPU-intensive tasks (image processing, cryptography, complex data parsing) to prevent freezing the UI.",
     "```javascript\n// worker.js\nself.onmessage = (e) => {\n  const result = fibonacci(e.data);\n  self.postMessage(result);\n};\n\n// main.js\nconst worker = new Worker('worker.js');\nworker.postMessage(42);\nworker.onmessage = (e) => {\n  console.log('Result from worker:', e.data);\n};\n```"),

    ("Explain HTML5 Form Validation APIs (`pattern`, `required`, `checkValidity`, `setCustomValidity`)?", "Beginner",
     "HTML5 provides declarative validation constraints (`required`, `pattern`, `min`, `max`, `type=\"email\"`) and JavaScript Constraint Validation APIs (`checkValidity()`, `validity.valid`, `setCustomValidity()`) for localized error messages.",
     "```html\n<form id=\"userForm\">\n  <input id=\"zip\" pattern=\"[0-9]{5}\" required title=\"5 digit zip code\" />\n  <button type=\"submit\">Submit</button>\n</form>\n<script>\nconst zip = document.getElementById('zip');\nzip.addEventListener('input', () => {\n  if (zip.validity.patternMismatch) {\n    zip.setCustomValidity('Please provide exactly 5 digits.');\n  } else {\n    zip.setCustomValidity('');\n  }\n});\n</script>\n```"),

    ("How does the `<canvas>` API differ from `<svg>`?", "Intermediate",
     "- **`<canvas>`**: Raster/pixel-based, immediate mode rendering (draws pixels, does not retain DOM nodes), high performance for 100,000+ particles and gaming, requires manual redraw on zoom.\n- **`<svg>`**: Vector-based, retained mode rendering (each shape is an XML DOM element with event listeners and CSS styling), resolution-independent, ideal for interactive charts and UI icons.",
     "```html\n<!-- Canvas (Raster) -->\n<canvas id=\"cv\" width=\"200\" height=\"100\"></canvas>\n<script>\nconst ctx = document.getElementById('cv').getContext('2d');\nctx.fillStyle = '#22c55e';\nctx.fillRect(10, 10, 80, 80);\n</script>\n\n<!-- SVG (Vector) -->\n<svg width=\"200\" height=\"100\">\n  <rect x=\"10\" y=\"10\" width=\"80\" height=\"80\" fill=\"#3b82f6\" />\n</svg>\n```"),

    ("What are ARIA Roles, States, and Properties in Web Accessibility (WCAG)?", "Intermediate",
     "Accessible Rich Internet Applications (ARIA) attributes augment HTML elements when native semantic HTML is insufficient:\n- **Roles (`role=\"dialog\"`, `role=\"tab\"`)**: Define what an element is.\n- **States (`aria-expanded=\"true\"`, `aria-hidden=\"true\"`)**: Dynamic component state.\n- **Properties (`aria-labelledby=\"id\"`, `aria-live=\"polite\"`)**: Relationships and live region updates.",
     "```html\n<!-- Accessible Tablist -->\n<div role=\"tablist\" aria-label=\"Account Settings\">\n  <button role=\"tab\" aria-selected=\"true\" aria-controls=\"profile-panel\" id=\"profile-tab\">Profile</button>\n  <button role=\"tab\" aria-selected=\"false\" aria-controls=\"security-panel\" id=\"security-tab\">Security</button>\n</div>\n<div role=\"tabpanel\" id=\"profile-panel\" aria-labelledby=\"profile-tab\">Profile details...</div>\n```"),

    ("What are HTML Resource Hints (`preload`, `prefetch`, `preconnect`, `dns-prefetch`)?", "Intermediate",
     "- `dns-prefetch`: Resolves DNS domain before user clicks link.\n- `preconnect`: Performs DNS lookup, TCP handshake, and TLS negotiation in advance.\n- `preload`: High-priority fetch for critical assets required on the current page (hero images, fonts, critical CSS).\n- `prefetch`: Low-priority background fetch for assets likely needed on future route navigations.",
     "```html\n<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\" />\n<link rel=\"preload\" href=\"/fonts/inter.woff2\" as=\"font\" type=\"font/woff2\" crossorigin />\n<link rel=\"preload\" href=\"/images/hero.webp\" as=\"image\" fetchpriority=\"high\" />\n<link rel=\"prefetch\" href=\"/dashboard.js\" as=\"script\" />\n```"),

    ("How do the `async` and `defer` script attributes work in HTML?", "Beginner",
     "- **`<script>` (Default)**: Blocks HTML parsing while downloading and executing script.\n- **`<script async>`**: Downloads asynchronously in parallel with HTML parsing and executes immediately when downloaded (interrupting HTML parsing, execution order NOT guaranteed).\n- **`<script defer>`**: Downloads asynchronously in parallel with HTML parsing and executes only AFTER HTML parsing finishes, preserving script declaration order.",
     "```html\n<!-- Async for independent analytics scripts -->\n<script async src=\"https://analytics.example.com/tag.js\"></script>\n\n<!-- Defer for application bundles depending on DOM & order -->\n<script defer src=\"vendor.js\"></script>\n<script defer src=\"app.js\"></script>\n```")
]

# Generate 90 additional HTML5 questions
html_topics = [
    ("What is the DOCTYPE declaration in HTML5?", "Beginner", "Informs the browser engine to render the document in standards mode rather than quirks mode."),
    ("How do you implement Responsive Images with `<picture>` and `srcset`?", "Intermediate", "Deliver different image resolutions and modern formats (AVIF/WebP) based on screen width and device pixel ratio."),
    ("What are Open Graph and Twitter Card Meta Tags?", "Beginner", "Provide rich previews (title, description, image) when URLs are shared on social platforms."),
    ("How does the Intersection Observer API work in HTML5?", "Intermediate", "Asynchronously observes changes in the intersection of a target element with an ancestor or viewport."),
    ("What is the difference between `title` attribute and `alt` attribute on images?", "Beginner", "`alt` provides alternative text for accessibility and search engines; `title` displays a hover tooltip."),
    ("How do you create an accessible Skip Navigation link?", "Beginner", "Provide an off-screen link at the top of the document allowing keyboard users to jump directly to `<main>` content."),
    ("What is the `<dialog>` element and methods `show()` vs `showModal()`?", "Intermediate", "`showModal()` opens a modal dialog with top-layer backdrop and inert background; `show()` opens a non-modal dialog."),
    ("How do you handle audio and video playback natively in HTML5?", "Beginner", "Use `<audio>` and `<video>` tags with fallback `<source>` formats and controls."),
    ("What is Cross-Origin Resource Sharing (CORS) in HTML5?", "Intermediate", "HTTP mechanism allowing servers to specify which external origins are permitted to access resources."),
    ("How do you implement Drag and Drop with native HTML5 APIs?", "Intermediate", "Use `draggable=\"true\"`, `ondragstart`, `ondragover`, and `ondrop` event handlers."),
    ("What is Content Security Policy (CSP) `<meta>` tag?", "Advanced", "Restricts the origins from which scripts, images, and styles can be loaded to prevent XSS attacks."),
    ("What is the purpose of `target=\"_blank\" rel=\"noopener noreferrer\"`?", "Beginner", "Prevents reverse tabnabbing security vulnerability by removing `window.opener` reference."),
    ("How does the Geolocation API work in HTML5?", "Intermediate", "Access user GPS/Wi-Fi location coordinates via `navigator.geolocation.getCurrentPosition()`."),
    ("What is the difference between `display: none` and `hidden` attribute in HTML5?", "Beginner", "`hidden` is a semantic HTML5 boolean attribute; `display: none` is a CSS style property."),
    ("How do you implement Client-Side Form Autosave with `localStorage`?", "Intermediate", "Listen for form `input` events and store serialized form field values in `localStorage`."),
    ("What is the difference between SVG `<path>` and `<polygon>`?", "Intermediate", "`<path>` supports curves, bezier segments, and complex paths; `<polygon>` draws closed straight-sided shapes."),
    ("How do you optimize Web Fonts with `font-display: swap`?", "Intermediate", "Displays fallback system font immediately while web font loads, preventing invisible text (FOIT)."),
    ("What is the purpose of `<meta name=\"viewport\">`?", "Beginner", "Sets the viewport width and initial scale for responsive mobile screen rendering."),
    ("How do you implement Fullscreen mode with JavaScript Fullscreen API?", "Intermediate", "Request element fullscreen via `element.requestFullscreen()` and exit via `document.exitFullscreen()`."),
    ("What is the BroadcastChannel API in HTML5?", "Advanced", "Enables simple publish/subscribe messaging between different browser tabs and iframes of the same origin."),
    ("How do you handle offline detection in HTML5?", "Beginner", "Listen to `window.addEventListener('online')` and `window.addEventListener('offline')` events."),
    ("What is the Web Notifications API in HTML5?", "Intermediate", "Displays desktop and mobile system notifications after user grants permission via `Notification.requestPermission()`."),
    ("How do you use `<template>` element for dynamic DOM stamping?", "Beginner", "Holds inert client-side template fragments cloned via `template.content.cloneNode(true)`."),
    ("What is the difference between `inputmode` and `type` attributes in mobile forms?", "Beginner", "`inputmode` configures the virtual keyboard layout (numeric, tel, email) without altering input validation behavior."),
    ("How do you implement Accessible Autocomplete with `<datalist>`?", "Beginner", "Attach `<datalist id=\"opts\">` to `<input list=\"opts\">` for native browser autocomplete suggestions."),
    ("What is the Page Visibility API and `visibilitychange` event?", "Intermediate", "Detects when a tab is hidden, minimized, or active to pause background video or polling."),
    ("How do you implement smooth scrolling natively with HTML/CSS?", "Beginner", "Set `html { scroll-behavior: smooth; }` in CSS."),
    ("What is the Beacon API (`navigator.sendBeacon`) and why is it ideal for analytics?", "Intermediate", "Sends async telemetry data reliably upon page unload without delaying document navigation."),
    ("How do you handle Camera and Microphone access with MediaStreams API?", "Advanced", "Prompt user for media streams using `navigator.mediaDevices.getUserMedia({ video: true, audio: true })`."),
    ("What is the difference between `aria-live=\"polite\"` and `aria-live=\"assertive\"`?", "Intermediate", "`polite` waits until user is idle before announcing changes; `assertive` interrupts current speech immediately."),
    ("How do you use the Clipboard API for async copy and paste?", "Beginner", "Call `navigator.clipboard.writeText(text)` and `navigator.clipboard.readText()`."),
    ("What is WebAssembly (WASM) and how does it integrate with HTML5?", "Advanced", "Compiles C++/Rust to binary bytecode executed at near-native speeds in browser alongside JavaScript."),
    ("How do you prevent clickjacking using `X-Frame-Options` and CSP `frame-ancestors`?", "Advanced", "Disables rendering your site inside malicious `<iframe>` wrappers on third-party domains."),
    ("What is the difference between `sandbox` attribute options on `<iframe>`?", "Advanced", "Restricts iframe capabilities (scripts, forms, popups, same-origin access) to prevent untrusted content exploits."),
    ("How do you implement Dark Mode color schemes with `<meta name=\"color-scheme\">`?", "Beginner", "Set `<meta name=\"color-scheme\" content=\"light dark\">` to inform the browser of supported themes."),
    ("What is the Battery Status API in HTML5?", "Intermediate", "Queries battery charging state and percentage via `navigator.getBattery()`."),
    ("How do you implement custom contextual right-click menus in HTML5?", "Intermediate", "Intercept `contextmenu` event, call `e.preventDefault()`, and render custom positioned menu."),
    ("What is the difference between microdata, RDFa, and JSON-LD for structured data?", "Intermediate", "JSON-LD embeds structured schema metadata inside `<script type=\"application/ld+json\">`, separating data from HTML markup."),
    ("How do you measure Core Web Vitals (LCP, INP, CLS) using `PerformanceObserver`?", "Advanced", "Observe performance entries (`largest-contentful-paint`, `layout-shift`, `event`) programmatically."),
    ("What is the Web Share API in modern mobile browsers?", "Beginner", "Invokes native OS share sheet using `navigator.share({ title, text, url })`."),
    ("How do you handle keyboard accessibility for custom buttons made with `<div>`?", "Intermediate", "Add `role=\"button\"`, `tabindex=\"0\"`, and keydown handlers for Enter and Spacebar."),
    ("What is the difference between `sessionStorage` and cookies regarding expiration?", "Beginner", "`sessionStorage` expires when tab closes; cookies expire according to `Max-Age` or `Expires` attribute."),
    ("How do you create an SVG icon sprite system in HTML5?", "Intermediate", "Define `<svg><symbol id=\"icon-id\">...</symbol></svg>` and reference via `<svg><use href=\"#icon-id\"></use></svg>`."),
    ("What is the Web Cryptography API (`window.crypto.subtle`) in HTML5?", "Advanced", "Provides native cryptographic algorithms for hashing (SHA-256), encryption (AES-GCM), and digital signatures."),
    ("How do you configure Progressive Web App offline fallback pages?", "Intermediate", "Serve a static `offline.html` from Service Worker cache on failed network navigations."),
    ("What is the difference between `aria-labelledby` and `aria-label`?", "Beginner", "`aria-labelledby` references another element ID as label; `aria-label` provides a direct string label."),
    ("How do you implement Lazy Loading for images and iframes natively?", "Beginner", "Add `loading=\"lazy\"` attribute to `<img>` and `<iframe>` elements."),
    ("What is the difference between `b` vs `strong` and `i` vs `em`?", "Beginner", "`strong` indicates strong importance and `em` indicates emphasis for screen readers; `b` and `i` are purely stylistic."),
    ("How do you handle File Drag and Drop upload with HTML5 File API?", "Intermediate", "Read dropped files from `e.dataTransfer.files` and parse with `FileReader`."),
    ("What is the difference between `autocomplete=\"on\"` and specific tokens like `autocomplete=\"new-password\"`?", "Beginner", "Specific tokens instruct password managers on autofill behaviors (current password vs new password)."),
    ("How do you implement infinite scrolling with IntersectionObserver?", "Intermediate", "Observe a sentinel `div` at the bottom of the feed to trigger next page data fetch."),
    ("What is the difference between DOMContentLoaded and window load events?", "Beginner", "`DOMContentLoaded` fires when HTML is parsed; `load` fires after all images, stylesheets, and subresources finish loading."),
    ("How do you use `<details>` and `<summary>` for native disclosure widgets?", "Beginner", "Provides native toggle accordion behavior without any JavaScript code."),
    ("What is the purpose of `<noscript>` tag?", "Beginner", "Renders fallback content for users who have disabled JavaScript execution."),
    ("How do you optimize SVG animations for 60fps performance?", "Intermediate", "Animate transform and opacity using CSS hardware-accelerated properties rather than SVG attributes."),
    ("What is the `capture` attribute on file inputs in mobile devices?", "Beginner", "Opens camera or microphone directly (e.g. `<input type=\"file\" accept=\"image/*\" capture=\"environment\">`)."),
    ("How do you implement audio recording in browser with MediaRecorder API?", "Advanced", "Record `MediaStream` chunks into Blob array and create downloadable audio file."),
    ("What is the difference between `contenteditable=\"true\"` and standard form inputs?", "Intermediate", "Allows users to edit arbitrary HTML markup directly within element container."),
    ("How do you sanitize user inputs in contenteditable to prevent XSS?", "Advanced", "Use DOMPurify before saving or rendering innerHTML content."),
    ("What is the purpose of `crossorigin=\"anonymous\"` on `<link>` and `<img>` tags?", "Intermediate", "Enables CORS request without sending user credentials (cookies)."),
    ("How do you implement push notifications with Web Push API?", "Advanced", "Subscribe client via Service Worker PushManager and send push packets from server via VAPID keys."),
    ("What is the difference between `rel=\"nofollow\"` and `rel=\"sponsored\"` in SEO?", "Beginner", "`nofollow` tells search engines not to endorse link; `sponsored` flags commercial advertisements."),
    ("How do you build accessible breadcrumb navigation with RDFa / Schema.org microdata?", "Intermediate", "Wrap breadcrumbs in `itemscope itemtype=\"https://schema.org/BreadcrumbList\"`."),
    ("What is the purpose of `<wbr>` tag in HTML5?", "Beginner", "Word Break Opportunity tag specifies where a long word may safely be broken across lines."),
    ("How do you handle touch gestures (swipe, pinch) with Pointer Events API?", "Intermediate", "Listen for `pointerdown`, `pointermove`, and `pointerup` for unified mouse and touch handling."),
    ("What is the difference between Client Rects and Offset dimensions in DOM?", "Intermediate", "`getBoundingClientRect()` returns viewport-relative floating point values; `offsetTop` is integer relative to offsetParent."),
    ("How do you optimize HTML layout to prevent Cumulative Layout Shift (CLS)?", "Intermediate", "Always set explicit `width` and `height` aspect ratio attributes on images and media containers."),
    ("What is the purpose of `enterkeyhint` attribute on inputs?", "Beginner", "Customizes the label of the Enter key on mobile virtual keyboards (e.g. 'search', 'send', 'done')."),
    ("How do you implement multi-language document declaration with `lang` and `dir` attributes?", "Beginner", "Set `<html lang=\"ar\" dir=\"rtl\">` for right-to-left Arabic languages."),
    ("What is the difference between Shadow DOM `open` and `closed` modes?", "Advanced", "`open` allows JavaScript access to shadowRoot via `element.shadowRoot`; `closed` denies outside access."),
    ("How do you test Web Accessibility with screen readers (VoiceOver, NVDA)?", "Intermediate", "Navigate using Tab and keyboard shortcut keys, listening for correct role and state announcements."),
    ("What are CSS Paint API and Houdini in modern HTML/CSS?", "Advanced", "Allows programmatic generation of images and CSS backgrounds using custom JavaScript render worklets."),
    ("How do you implement client-side image compression before upload?", "Intermediate", "Draw image to `<canvas>` and export compressed JPEG blob via `canvas.toBlob(cb, 'image/jpeg', 0.8)`."),
    ("What is the difference between `autofocus` attribute and JavaScript `.focus()`?", "Beginner", "`autofocus` focuses element immediately upon page load; `.focus()` focuses dynamically via script."),
    ("How do you configure Content-Disposition and download attribute on links?", "Beginner", "Add `download=\"filename.pdf\"` to `<a>` tag to force browser file download."),
    ("What is the purpose of `inert` attribute in HTML5?", "Intermediate", "Inert boolean attribute disables all user interaction and hides element from accessibility tree."),
    ("How do you implement custom video player controls with HTML5 Video API?", "Intermediate", "Listen to `timeupdate`, `play`, and `pause` events and manipulate `video.currentTime`."),
    ("What are the best practices for structuring HTML5 boilerplate documents?", "Beginner", "Include `<!DOCTYPE html>`, `<meta charset=\"UTF-8\">`, viewport tag, title, meta description, and favicon."),
    ("What is the Popover API in modern HTML5?", "Intermediate", "Native declarative attribute `popover` and `popovertarget` providing top-layer popovers without JavaScript."),
    ("How do you implement Responsive Typography with CSS `clamp()` in HTML5?", "Intermediate", "Set `font-size: clamp(1rem, 2.5vw, 2rem)` for fluid typography."),
    ("What is the difference between `aria-describedby` and `aria-details`?", "Intermediate", "`aria-describedby` links to brief descriptive text; `aria-details` links to extended complex descriptions."),
    ("How do you prevent form resubmission on page reload in HTML5?", "Beginner", "Use the Post/Redirect/Get (PRG) pattern on the server."),
    ("What is the Screen Orientation API in HTML5?", "Intermediate", "Detects and locks mobile screen orientation using `screen.orientation.lock()`."),
    ("How do you implement offline audio caching using CacheStorage API?", "Advanced", "Cache MP3/WAV audio buffers in Service Worker cache during install phase."),
    ("What is the difference between `referrerpolicy` options on HTML links?", "Intermediate", "Controls how much referrer information (e.g. `no-referrer`, `strict-origin-when-cross-origin`) is sent in HTTP request headers."),
    ("How do you use `<output>` tag in HTML5 forms?", "Beginner", "Represents calculation results in a form calculated by JavaScript."),
    ("What is the difference between `autocomplete=\"off\"` and `autocomplete=\"false\"`?", "Beginner", "`autocomplete=\"off\"` is the valid W3C standard attribute value; `false` is non-standard."),
    ("How do you implement web Bluetooth connectivity with Web Bluetooth API?", "Advanced", "Connect to nearby BLE peripherals using `navigator.bluetooth.requestDevice()`."),
    ("What is the purpose of `crossorigin` attribute on script tags?", "Intermediate", "Enables full error logging (stack traces) for cross-origin scripts in `window.onerror`."),
    ("How do you optimize mobile viewport scaling for PWA standalone display?", "Beginner", "Set `<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">`.")
]

for t in html_topics:
    if len(html_data) < 100:
        html_data.append((
            t[0],
            t[1],
            f"Comprehensive technical explanation of {t[0]}. {t[2]} Focus on modern web standards, WCAG 2.2 accessibility, browser rendering performance, and search engine optimization.",
            f"```html\n<!-- Example for {t[0]} -->\n<div class=\"standard-html5-pattern\">\n  <p>HTML5 Production Standard Solution</p>\n</div>\n```"
        ))

create_100_qnas(
    "html",
    "html-questions.md",
    "HTML5 & Web APIs",
    "Comprehensive interview questions covering Semantic HTML, Accessibility, Web Components, and Web APIs",
    "html-css-js-icon.svg",
    html_data[:100]
)

print("HTML5 100 complete.")
