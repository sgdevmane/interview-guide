<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>HTML Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for developers</b></p>
</div>

---

## Table of Contents

1. [How do you structure a web page using Semantic HTML for better Accessibility and SEO?](#q1-how-do-you-structure-a-web-page-using-semantic-html-for-better-accessibility-and-seo) <span class="intermediate">Intermediate</span>
2. [Implement a responsive image strategy using `srcset` and `<picture>`.](#q2-implement-a-responsive-image-strategy-using-srcset-and-<picture>) <span class="intermediate">Intermediate</span>
3. [How do you ensure a web form is accessible to screen reader users?](#q3-how-do-you-ensure-a-web-form-is-accessible-to-screen-reader-users) <span class="intermediate">Intermediate</span>
4. [How do you implement a modal dialog using the native `<dialog>` element?](#q4-how-do-you-implement-a-modal-dialog-using-the-native-<dialog>-element) <span class="intermediate">Intermediate</span>
5. [How do you optimize Critical Rendering Path using HTML tags?](#q5-how-do-you-optimize-critical-rendering-path-using-html-tags) <span class="intermediate">Intermediate</span>
6. [How do you prevent tabnabbing attacks when using `target='_blank'`?](#q6-how-do-you-prevent-tabnabbing-attacks-when-using-target=_blank) <span class="intermediate">Intermediate</span>
7. [How do you implement Open Graph tags for Social Media sharing?](#q7-how-do-you-implement-open-graph-tags-for-social-media-sharing) <span class="intermediate">Intermediate</span>
8. [How do you use the `<template>` tag for dynamic content?](#q8-how-do-you-use-the-<template>-tag-for-dynamic-content) <span class="intermediate">Intermediate</span>
9. [How do you implement a secure Content Security Policy (CSP) via meta tag?](#q9-how-do-you-implement-a-secure-content-security-policy-csp-via-meta-tag) <span class="intermediate">Intermediate</span>
10. [How do you encapsulate styles using Shadow DOM to prevent leakage?](#q10-how-do-you-encapsulate-styles-using-shadow-dom-to-prevent-leakage) <span class="intermediate">Intermediate</span>
11. [How do you implement 'Lazy Loading' for iframes and images natively?](#q11-how-do-you-implement-lazy-loading-for-iframes-and-images-natively) <span class="intermediate">Intermediate</span>
12. [How do you create an accessible 'Skip to Content' link?](#q12-how-do-you-create-an-accessible-skip-to-content-link) <span class="intermediate">Intermediate</span>
13. [How do you manage keyboard focus order using `tabindex` efficiently?](#q13-how-do-you-manage-keyboard-focus-order-using-tabindex-efficiently) <span class="intermediate">Intermediate</span>
14. [How do you handle 'Dark Mode' preference in HTML/CSS?](#q14-how-do-you-handle-dark-mode-preference-in-htmlcss) <span class="intermediate">Intermediate</span>
15. [How do you validate forms using HTML5 built-in attributes?](#q15-how-do-you-validate-forms-using-html5-built-in-attributes) <span class="intermediate">Intermediate</span>
16. [How do you optimize font loading using `font-display`?](#q16-how-do-you-optimize-font-loading-using-font-display) <span class="intermediate">Intermediate</span>
17. [How do you use JSON-LD for Structured Data (SEO)?](#q17-how-do-you-use-json-ld-for-structured-data-seo) <span class="intermediate">Intermediate</span>
18. [How do you force a file download using the `download` attribute?](#q18-how-do-you-force-a-file-download-using-the-download-attribute) <span class="beginner">Beginner</span>
19. [What is the semantic difference between `<code>`, `<pre>`, and `<kbd>`?](#q19-what-is-the-semantic-difference-between-<code>-<pre>-and-<kbd>) <span class="beginner">Beginner</span>
20. [How do you implement an accessible Toggle Switch using HTML/CSS?](#q20-how-do-you-implement-an-accessible-toggle-switch-using-htmlcss) <span class="intermediate">Intermediate</span>
21. [How do you optimize a page for printing using CSS media queries?](#q21-how-do-you-optimize-a-page-for-printing-using-css-media-queries) <span class="intermediate">Intermediate</span>
22. [How do you semantically markup an image with a caption?](#q22-how-do-you-semantically-markup-an-image-with-a-caption) <span class="beginner">Beginner</span>
23. [How do you group options in a `<select>` dropdown?](#q23-how-do-you-group-options-in-a-<select>-dropdown) <span class="beginner">Beginner</span>
24. [How do you specify the canonical URL to prevent duplicate content issues?](#q24-how-do-you-specify-the-canonical-url-to-prevent-duplicate-content-issues) <span class="intermediate">Intermediate</span>
25. [How do you disable spellcheck for specific input fields?](#q25-how-do-you-disable-spellcheck-for-specific-input-fields) <span class="beginner">Beginner</span>
26. [How do you create a 'Mailto' link with subject, body, and CC?](#q26-how-do-you-create-a-mailto-link-with-subject-body-and-cc) <span class="beginner">Beginner</span>
27. [How do you mark up time and dates for machine readability?](#q27-how-do-you-mark-up-time-and-dates-for-machine-readability) <span class="beginner">Beginner</span>
28. [How do you make an iframe responsive with correct aspect ratio?](#q28-how-do-you-make-an-iframe-responsive-with-correct-aspect-ratio) <span class="intermediate">Intermediate</span>
29. [How do you define a specific language for a part of the text?](#q29-how-do-you-define-a-specific-language-for-a-part-of-the-text) <span class="beginner">Beginner</span>
30. [How do you use the `pattern` attribute for form validation?](#q30-how-do-you-use-the-pattern-attribute-for-form-validation) <span class="intermediate">Intermediate</span>

---

### Q1: How do you structure a web page using Semantic HTML for better Accessibility and SEO?

**Difficulty**: Intermediate

**Strategy:**
Use semantic tags to describe content meaning, not just appearance.

**Structure:**
- `<header>`: Intro/Nav.
- `<nav>`: Major navigation links.
- `<main>`: Unique content of the page (only one per page).
- `<article>`: Self-contained content (blog post).
- `<section>`: Thematic grouping of content with a heading.
- `<aside>`: Related content (sidebar).
- `<footer>`: Copyright, links.

**Benefit:** Screen readers use these landmarks to navigate; Search engines understand content hierarchy.

**Code Example:**
```html
<body>
  <header>
    <h1>Site Title</h1>
    <nav>...</nav>
  </header>
  <main>
    <article>
      <h2>Blog Post</h2>
      <p>Content...</p>
    </article>
    <aside>
      <h3>Related Links</h3>
    </aside>
  </main>
  <footer>&copy; 2024</footer>
</body>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q2: Implement a responsive image strategy using `srcset` and `<picture>`.

**Difficulty**: Intermediate

**Strategy:**
**1. Resolution Switching (`srcset`):** Serve different sizes of the *same* image based on viewport width.



**2. Art Direction (`<picture>`):** Serve *different* images (crop/aspect ratio) or formats (WebP) based on conditions.

```html
<picture>
  <source srcset="hero-mobile.webp" media="(max-width: 600px)">
  <source srcset="hero-desktop.webp" type="image/webp">
  <img src="hero-fallback.jpg" alt="Hero Image">
</picture>
```

**Code Example:**
```html
<img src="small.jpg" 
     srcset="small.jpg 500w, medium.jpg 1000w, large.jpg 2000w" 
     sizes="(max-width: 600px) 100vw, 50vw" 
     alt="Hero Image">
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q3: How do you ensure a web form is accessible to screen reader users?

**Difficulty**: Intermediate

**Strategy:**
**Key Techniques:**
1. **Labels:** Always associate `<label>` with `<input>` using `for`/`id` or nesting.
2. **Fieldsets:** Group related inputs (radio buttons) with `<fieldset>` and `<legend>`.
3. **Errors:** specific error messages linked via `aria-describedby`.
4. **Autocomplete:** Use `autocomplete` attributes to help browsers fill data.

**Code Example:**
```html
<form>
  <div class="form-group">
    <label for="email">Email Address:</label>
    <input type="email" id="email" name="email" autocomplete="email" required aria-describedby="email-help">
    <small id="email-help">We'll never share your email.</small>
  </div>

  <fieldset>
    <legend>Preferred Contact Method</legend>
    <label><input type="radio" name="contact" value="email"> Email</label>
    <label><input type="radio" name="contact" value="phone"> Phone</label>
  </fieldset>
</form>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q4: How do you implement a modal dialog using the native `<dialog>` element?

**Difficulty**: Intermediate

**Strategy:**
The `<dialog>` element provides a native modal with built-in accessibility (focus trapping, closing with Esc).

**Implementation:**

**Code Example:**
```html
<dialog id="myDialog">
  <form method="dialog">
    <h2>Confirmation</h2>
    <p>Are you sure you want to delete this?</p>
    <button value="cancel">Cancel</button>
    <button value="confirm">Confirm</button>
  </form>
</dialog>

<button id="openBtn">Open Modal</button>

<script>
  const dialog = document.getElementById('myDialog');
  document.getElementById('openBtn').addEventListener('click', () => {
    dialog.showModal(); // Opens as a modal (overlays content)
  });
  
  dialog.addEventListener('close', () => {
    console.log(`User clicked: ${dialog.returnValue}`);
  });
</script>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q5: How do you optimize Critical Rendering Path using HTML tags?

**Difficulty**: Intermediate

**Strategy:**
Optimize how the browser paints the page by prioritizing critical resources.

**Strategies:**
1. **Preload Critical Assets:** `<link rel="preload">` for fonts/hero images.
2. **Defer Non-Critical JS:** `<script defer>` to prevent parser blocking.
3. **Inline Critical CSS:** Put above-the-fold styles in `<style>` in `<head>`.
4. **Preconnect:** Warm up DNS/TLS for 3rd party domains.

**Code Example:**
```html
<head>
  <!-- Preconnect to CDN -->
  <link rel="preconnect" href="https://cdn.example.com">
  
  <!-- Preload Hero Image (High Priority) -->
  <link rel="preload" as="image" href="hero.jpg">
  
  <!-- Non-blocking CSS -->
  <link rel="stylesheet" href="print.css" media="print">
  
  <!-- Defer JS -->
  <script src="app.js" defer></script>
</head>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q6: How do you prevent tabnabbing attacks when using `target='_blank'`?

**Difficulty**: Intermediate

**Strategy:**
When using `target="_blank"`, the new page gets access to the `window.opener` object, allowing it to redirect the original page to a malicious site.

**Fix:** Always add `rel="noopener noreferrer"`.
*Note: Modern browsers implicitly set `noopener` for `target="_blank"`, but `noreferrer` is still good practice for privacy.*

**Code Example:**
```html
<!-- Vulnerable -->
<a href="https://external-site.com" target="_blank">Visit Site</a>

<!-- Secure -->
<a href="https://external-site.com" target="_blank" rel="noopener noreferrer">
  Visit Site
</a>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q7: How do you implement Open Graph tags for Social Media sharing?

**Difficulty**: Intermediate

**Strategy:**
Open Graph (OG) tags control how your page looks when shared on Facebook, LinkedIn, etc.

**Implementation:**
Add `<meta>` tags in the `<head>`.

**Code Example:**
```html
<head>
  <meta property="og:title" content="The Ultimate HTML Guide">
  <meta property="og:description" content="Learn HTML with practical examples.">
  <meta property="og:image" content="https://example.com/thumb.jpg">
  <meta property="og:url" content="https://example.com/article">
  <meta property="og:type" content="article">
  
  <!-- Twitter Card specific -->
  <meta name="twitter:card" content="summary_large_image">
</head>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q8: How do you use the `<template>` tag for dynamic content?

**Difficulty**: Intermediate

**Strategy:**
The `<template>` tag holds HTML that is **not rendered** immediately but can be instantiated via JavaScript. It's useful for repeating list items or dynamic components.

**Code Example:**
```html
<template id="user-card">
  <div class="card">
    <h2 class="name"></h2>
    <p class="email"></p>
  </div>
</template>

<div id="container"></div>

<script>
  const template = document.getElementById('user-card');
  const container = document.getElementById('container');
  
  const users = [{name: 'Alice', email: 'alice@test.com'}];
  
  users.forEach(user => {
    const clone = template.content.cloneNode(true);
    clone.querySelector('.name').textContent = user.name;
    clone.querySelector('.email').textContent = user.email;
    container.appendChild(clone);
  });
</script>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q9: How do you implement a secure Content Security Policy (CSP) via meta tag?

**Difficulty**: Intermediate

**Strategy:**
CSP mitigates XSS attacks by restricting where resources (scripts, images) can be loaded from.

**Implementation via Meta Tag:**
(Prefer HTTP Header, but Meta tag works for most directives).



**Explanation:**
- `default-src 'self'`: Only allow resources from own origin.
- `script-src`: Allow local scripts and a specific CDN.
- `child-src 'none'`: Block iframes/workers.

**Code Example:**
```html
<meta http-equiv="Content-Security-Policy" 
      content="default-src 'self'; 
               img-src https://*; 
               script-src 'self' https://trusted.cdn.com; 
               child-src 'none';">
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q10: How do you encapsulate styles using Shadow DOM to prevent leakage?

**Difficulty**: Intermediate

**Strategy:**
Shadow DOM creates a scoped DOM tree attached to an element, ensuring styles defined inside don't affect the main document and vice versa.

**Code Example:**
```html
<div id="host"></div>

<script>
  const host = document.getElementById('host');
  const shadowRoot = host.attachShadow({ mode: 'open' });
  
  shadowRoot.innerHTML = `
    <style>
      p { color: red; font-weight: bold; } /* Only affects this p */
    </style>
    <p>I am in the shadows!</p>
  `;
</script>

<p>I am in the light (not red).</p>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q11: How do you implement 'Lazy Loading' for iframes and images natively?

**Difficulty**: Intermediate

**Strategy:**
Use the `loading="lazy"` attribute. The browser defers loading the resource until it is near the viewport.



**Note:** Always include `width` and `height` attributes to prevent layout shifts (CLS).

**Code Example:**
```html
<!-- Lazy load image -->
<img src="heavy-image.jpg" loading="lazy" alt="A heavy image" width="800" height="600">

<!-- Lazy load iframe -->
<iframe src="https://example.com" loading="lazy" title="External Content"></iframe>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q12: How do you create an accessible 'Skip to Content' link?

**Difficulty**: Intermediate

**Strategy:**
A 'Skip to Content' link allows keyboard/screen reader users to bypass navigation and jump to the main content.

**HTML:**
Place it as the first element in `<body>`.


**CSS:**
Hide it visually until focused.
```css
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  background: #000;
  color: #fff;
  padding: 8px;
  z-index: 100;
}

.skip-link:focus {
  top: 0;
}
```

**Code Example:**
```html
<a href="#main-content" class="skip-link">Skip to Main Content</a>

<nav>...</nav>

<main id="main-content">
  <!-- Main content starts here -->
</main>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q13: How do you manage keyboard focus order using `tabindex` efficiently?

**Difficulty**: Intermediate

**Strategy:**
Control tab order for interactive elements.

**Usage:**
1. `tabindex="0"`: Make a non-interactive element (like `div`) focusable in natural order.
2. `tabindex="-1"`: Make element focusable via JS (`ele.focus()`) but not via Tab key (useful for modals/errors).
3. **Avoid** `tabindex="1+"`: This forces a custom order, which often breaks accessibility for keyboard users.

**Code Example:**
```html
<!-- Custom button accessible via keyboard -->
<div role="button" tabindex="0" onclick="doAction()" onkeydown="handleKey(event)">
  Click Me
</div>

<!-- Programmatically focusable container -->
<div id="modal" tabindex="-1">...</div>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q14: How do you handle 'Dark Mode' preference in HTML/CSS?

**Difficulty**: Intermediate

**Strategy:**
Use the `prefers-color-scheme` media query in CSS, or the `<meta name="color-scheme">` tag in HTML to signal support.

**HTML:**


**CSS:**
```css
:root {
  --bg-color: white;
  --text-color: black;
}

@media (prefers-color-scheme: dark) {
  :root {
    --bg-color: #121212;
    --text-color: #e0e0e0;
  }
}

body {
  background-color: var(--bg-color);
  color: var(--text-color);
}
```

**Code Example:**
```html
<meta name="color-scheme" content="light dark">
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q15: How do you validate forms using HTML5 built-in attributes?

**Difficulty**: Intermediate

**Strategy:**
Use attributes like `required`, `pattern`, `type`, `min`, `max` to validate without JavaScript.


**Styling:** Use `:valid` and `:invalid` pseudo-classes in CSS.

**Code Example:**
```html
<form>
  <!-- Required field -->
  <input type="text" name="username" required>
  
  <!-- Regex pattern (Letters only) -->
  <input type="text" name="country" pattern="[A-Za-z]+" title="Letters only">
  
  <!-- Number range -->
  <input type="number" name="age" min="18" max="99">
  
  <!-- Email format -->
  <input type="email" name="email">
  
  <button type="submit">Submit</button>
</form>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q16: How do you optimize font loading using `font-display`?

**Difficulty**: Intermediate

**Strategy:**
The `font-display` property defines how a font face is displayed based on whether and when it is downloaded and ready to use. `swap` is commonly used to show fallback text immediately until the custom font loads.

**Code Example:**
```html
<style>
  @font-face {
    font-family: 'MyCustomFont';
    src: url('my-font.woff2') format('woff2');
    /* Fallback text is shown immediately, then swaps */
    font-display: swap; 
  }
  
  body {
    font-family: 'MyCustomFont', sans-serif;
  }
</style>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q17: How do you use JSON-LD for Structured Data (SEO)?

**Difficulty**: Intermediate

**Strategy:**
JSON-LD (JavaScript Object Notation for Linked Data) is the recommended format by Google for structured data. It is placed inside a `<script>` tag.

**Code Example:**
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Wireless Headphones",
  "image": "https://example.com/photos/1x1/photo.jpg",
  "description": "Noise-cancelling headphones",
  "brand": {
    "@type": "Brand",
    "name": "AudioTech"
  },
  "offers": {
    "@type": "Offer",
    "price": "99.99",
    "priceCurrency": "USD"
  }
}
</script>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q18: How do you force a file download using the `download` attribute?

**Difficulty**: Beginner

**Strategy:**
The `download` attribute on an `<a>` tag instructs the browser to download the URL instead of navigating to it. You can optionally specify a filename.

**Code Example:**
```html
<!-- Downloads as 'report.pdf' -->
<a href="/files/report-v2.pdf" download="report.pdf">
  Download Report
</a>

<!-- Downloads with original filename -->
<a href="/images/logo.png" download>
  Download Logo
</a>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q19: What is the semantic difference between `<code>`, `<pre>`, and `<kbd>`?

**Difficulty**: Beginner

**Strategy:**
`<code>` represents a fragment of computer code. `<pre>` preserves whitespace and formatting (blocks of code). `<kbd>` represents user input (keyboard keys).

**Code Example:**
```html
<p>To install dependencies, run:</p>

<pre><code>
npm install
npm start
</code></pre>

<p>Press <kbd>Ctrl</kbd> + <kbd>C</kbd> to exit.</p>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q20: How do you implement an accessible Toggle Switch using HTML/CSS?

**Difficulty**: Intermediate

**Strategy:**
Use a standard `<input type='checkbox'>` for the logic and a `<label>` for the custom UI. This ensures keyboard accessibility and screen reader support natively.

**Code Example:**
```html
<style>
  .switch {
    position: relative;
    display: inline-block;
    width: 60px; height: 34px;
  }
  .switch input { opacity: 0; width: 0; height: 0; }
  .slider {
    position: absolute;
    cursor: pointer;
    top: 0; left: 0; right: 0; bottom: 0;
    background-color: #ccc;
    transition: .4s;
    border-radius: 34px;
  }
  .slider:before {
    position: absolute;
    content: "";
    height: 26px; width: 26px;
    left: 4px; bottom: 4px;
    background-color: white;
    transition: .4s;
    border-radius: 50%;
  }
  input:checked + .slider { background-color: #2196F3; }
  input:checked + .slider:before { transform: translateX(26px); }
</style>

<label class="switch" aria-label="Toggle Dark Mode">
  <input type="checkbox">
  <span class="slider"></span>
</label>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q21: How do you optimize a page for printing using CSS media queries?

**Difficulty**: Intermediate

**Strategy:**
Use `@media print` to hide navigation, adjust margins, and ensure text is black on white for better legibility on paper.

**Code Example:**
```html
<style>
  @media print {
    header, footer, nav, .no-print {
      display: none;
    }
    
    body {
      font-size: 12pt;
      color: #000;
      background: #fff;
    }
    
    a[href]:after {
      content: " (" attr(href) ")";
    }
  }
</style>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q22: How do you semantically markup an image with a caption?

**Difficulty**: Beginner

**Strategy:**
Use the `<figure>` element to wrap the image and `<figcaption>` for the caption. This creates a semantic association between them.

**Code Example:**
```html
<figure>
  <img src="sunset.jpg" alt="Sunset over the mountains" width="600" height="400">
  <figcaption>Fig.1 - A beautiful sunset in the Rockies.</figcaption>
</figure>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q23: How do you group options in a `<select>` dropdown?

**Difficulty**: Beginner

**Strategy:**
Use the `<optgroup>` element to group related `<option>` items. The `label` attribute defines the group name.

**Code Example:**
```html
<label for="cars">Choose a car:</label>
<select id="cars" name="cars">
  <optgroup label="Swedish Cars">
    <option value="volvo">Volvo</option>
    <option value="saab">Saab</option>
  </optgroup>
  <optgroup label="German Cars">
    <option value="mercedes">Mercedes</option>
    <option value="audi">Audi</option>
  </optgroup>
</select>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q24: How do you specify the canonical URL to prevent duplicate content issues?

**Difficulty**: Intermediate

**Strategy:**
Use the `<link rel='canonical'>` tag in the `<head>` to tell search engines which version of a URL is the master copy.

**Code Example:**
```html
<head>
  <!-- Even if accessed via ?ref=twitter, this is the main URL -->
  <link rel="canonical" href="https://example.com/blog/html-guide" />
</head>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q25: How do you disable spellcheck for specific input fields?

**Difficulty**: Beginner

**Strategy:**
Use the `spellcheck='false'` attribute. This is useful for inputs like usernames, emails, or code editors where spellcheck is distracting.

**Code Example:**
```html
<input type="text" name="username" spellcheck="false" placeholder="Username">

<textarea spellcheck="false">
  console.log("Hello World");
</textarea>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q26: How do you create a 'Mailto' link with subject, body, and CC?

**Difficulty**: Beginner

**Strategy:**
You can add query parameters to the `mailto:` URL to pre-fill fields. Remember to URL-encode special characters.

**Code Example:**
```html
<a href="mailto:support@example.com?subject=Help%20Request&cc=manager@example.com&body=I%20need%20help%20with...">
  Contact Support
</a>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q27: How do you mark up time and dates for machine readability?

**Difficulty**: Beginner

**Strategy:**
Use the `<time>` element with the `datetime` attribute. This helps search engines and calendar tools understand the specific date/time.

**Code Example:**
```html
<p>
  The concert starts on 
  <time datetime="2023-12-25T20:00">Christmas Day at 8 PM</time>.
</p>

<article>
  Published <time datetime="2023-10-01">October 1st</time>
</article>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q28: How do you make an iframe responsive with correct aspect ratio?

**Difficulty**: Intermediate

**Strategy:**
Modern CSS `aspect-ratio` property makes this easy. Previously, the 'padding-hack' was used.

**Code Example:**
```html
<style>
  .video-container {
    width: 100%;
    aspect-ratio: 16 / 9;
  }
  .video-container iframe {
    width: 100%;
    height: 100%;
  }
</style>

<div class="video-container">
  <iframe src="https://www.youtube.com/embed/xyz" frameborder="0" allowfullscreen></iframe>
</div>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q29: How do you define a specific language for a part of the text?

**Difficulty**: Beginner

**Strategy:**
Use the `lang` attribute on a span or div. This is important for screen readers to switch pronunciation.

**Code Example:**
```html
<p>
  The French phrase for "Hello" is <span lang="fr">Bonjour</span>.
</p>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q30: How do you use the `pattern` attribute for form validation?

**Difficulty**: Intermediate

**Strategy:**
The `pattern` attribute accepts a Regular Expression that the input value must match.

**Code Example:**
```html
<form>
  <label for="zip">Zip Code (5 digits):</label>
  <input 
    type="text" 
    id="zip" 
    name="zip" 
    pattern="[0-9]{5}" 
    title="Five digit zip code" 
    required
  >
  <button>Submit</button>
</form>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

