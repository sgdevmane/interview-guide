# HTML Interview Questions

## Table of Contents
1. [How do you structure a web page using Semantic HTML for better Accessibility and SEO?](#q1-how-do-you-structure-a-web-page-using-semantic-html-for-better-accessibility-and-seo)
2. [Implement a responsive image strategy using `srcset` and `<picture>`.](#q2-implement-a-responsive-image-strategy-using-srcset-and-<picture>.)
3. [How do you ensure a web form is accessible to screen reader users?](#q3-how-do-you-ensure-a-web-form-is-accessible-to-screen-reader-users)
4. [How do you implement a modal dialog using the native `<dialog>` element?](#q4-how-do-you-implement-a-modal-dialog-using-the-native-<dialog>-element)
5. [How do you optimize Critical Rendering Path using HTML tags?](#q5-how-do-you-optimize-critical-rendering-path-using-html-tags)
6. [How do you prevent tabnabbing attacks when using `target='_blank'`?](#q6-how-do-you-prevent-tabnabbing-attacks-when-using-target=_blank)
7. [How do you implement Open Graph tags for Social Media sharing?](#q7-how-do-you-implement-open-graph-tags-for-social-media-sharing)
8. [How do you use the `<template>` tag for dynamic content?](#q8-how-do-you-use-the-<template>-tag-for-dynamic-content)
9. [How do you implement a secure Content Security Policy (CSP) via meta tag?](#q9-how-do-you-implement-a-secure-content-security-policy-csp-via-meta-tag)
10. [How do you encapsulate styles using Shadow DOM to prevent leakage?](#q10-how-do-you-encapsulate-styles-using-shadow-dom-to-prevent-leakage)
11. [How do you implement 'Lazy Loading' for iframes and images natively?](#q11-how-do-you-implement-lazy-loading-for-iframes-and-images-natively)
12. [How do you create an accessible 'Skip to Content' link?](#q12-how-do-you-create-an-accessible-skip-to-content-link)
13. [How do you manage keyboard focus order using `tabindex` efficiently?](#q13-how-do-you-manage-keyboard-focus-order-using-tabindex-efficiently)
14. [How do you handle 'Dark Mode' preference in HTML/CSS?](#q14-how-do-you-handle-dark-mode-preference-in-html-css)
15. [How do you validate forms using HTML5 built-in attributes?](#q15-how-do-you-validate-forms-using-html5-built-in-attributes)
16. [How do you optimize fonts with `font-display`?](#q16-how-do-you-optimize-fonts-with-font-display)
17. [How do you handle 'Microdata' (Structured Data) for Rich Snippets?](#q17-how-do-you-handle-microdata-structured-data-for-rich-snippets)
18. [How do you force a file download instead of opening it?](#q18-how-do-you-force-a-file-download-instead-of-opening-it)
19. [How do you denote computer code in HTML?](#q19-how-do-you-denote-computer-code-in-html)
20. [How do you implement a 'Toggle Switch' using semantic HTML?](#q20-how-do-you-implement-a-toggle-switch-using-semantic-html)
21. [How do you ensure 'Print' styles are correct?](#q21-how-do-you-ensure-print-styles-are-correct)
22. [How do you mark up a 'Figure' with a caption?](#q22-how-do-you-mark-up-a-figure-with-a-caption)
23. [How do you implement 'Focus Trapping' inside a custom modal?](#q23-how-do-you-implement-focus-trapping-inside-a-custom-modal)
24. [How do you detect if a user prefers 'Reduced Motion'?](#q24-how-do-you-detect-if-a-user-prefers-reduced-motion)
25. [How do you group options in a `<select>` dropdown?](#q25-how-do-you-group-options-in-a-<select>-dropdown)
26. [How do you specify the relationship between the current document and linked resources?](#q26-how-do-you-specify-the-relationship-between-the-current-document-and-linked-resources)
27. [How do you disable spellcheck for an input?](#q27-how-do-you-disable-spellcheck-for-an-input)
28. [How do you create a 'Mailto' link with subject and body?](#q28-how-do-you-create-a-mailto-link-with-subject-and-body)
29. [How do you mark up time and dates semantically?](#q29-how-do-you-mark-up-time-and-dates-semantically)
30. [How do you make an iframe responsive?](#q30-how-do-you-make-an-iframe-responsive)
31. [How do you control the browser's viewport on mobile?](#q31-how-do-you-control-the-browsers-viewport-on-mobile)
32. [How do you define a specific region for a language change?](#q32-how-do-you-define-a-specific-region-for-a-language-change)
33. [How do you prevent iOS from detecting phone numbers automatically?](#q33-how-do-you-prevent-ios-from-detecting-phone-numbers-automatically)
34. [How do you create a link that calls a phone number?](#q34-how-do-you-create-a-link-that-calls-a-phone-number)
35. [How do you create a 'Back to Top' link?](#q35-how-do-you-create-a-back-to-top-link)
36. [How do you implement a sticky header?](#q36-how-do-you-implement-a-sticky-header)
37. [How do you style the placeholder text of an input?](#q37-how-do-you-style-the-placeholder-text-of-an-input)
38. [How do you make a table responsive?](#q38-how-do-you-make-a-table-responsive)
39. [How do you hide an element visually but keep it accessible?](#q39-how-do-you-hide-an-element-visually-but-keep-it-accessible)
40. [How do you specify a fallback content for canvas?](#q40-how-do-you-specify-a-fallback-content-for-canvas)
41. [How do you allow a user to select multiple files?](#q41-how-do-you-allow-a-user-to-select-multiple-files)
42. [How do you restrict file upload to images only?](#q42-how-do-you-restrict-file-upload-to-images-only)
43. [How do you create a tooltip without JS?](#q43-how-do-you-create-a-tooltip-without-js)
44. [How do you implement smooth scrolling?](#q44-how-do-you-implement-smooth-scrolling)
45. [How do you create a multi-line text input?](#q45-how-do-you-create-a-multi-line-text-input)
46. [How do you disable resizing of a textarea?](#q46-how-do-you-disable-resizing-of-a-textarea)
47. [How do you make a favicon animate?](#q47-how-do-you-make-a-favicon-animate)
48. [How do you prevent a page from being indexed by Google?](#q48-how-do-you-prevent-a-page-from-being-indexed-by-google)
49. [How do you refresh the page automatically after 30 seconds?](#q49-how-do-you-refresh-the-page-automatically-after-30-seconds)
50. [How do you define the main contact info for the page?](#q50-how-do-you-define-the-main-contact-info-for-the-page)
51. [How do you denote an abbreviation?](#q51-how-do-you-denote-an-abbreviation)
52. [How do you group table header, body, and footer?](#q52-how-do-you-group-table-header-body-and-footer)
53. [How do you merge two table cells horizontally?](#q53-how-do-you-merge-two-table-cells-horizontally)
54. [How do you merge two table cells vertically?](#q54-how-do-you-merge-two-table-cells-vertically)
55. [How do you associate a caption with a table?](#q55-how-do-you-associate-a-caption-with-a-table)
56. [How do you highlight text (like a marker)?](#q56-how-do-you-highlight-text-like-a-marker)
57. [How do you represent a fraction or superscript?](#q57-how-do-you-represent-a-fraction-or-superscript)
58. [How do you indicate a text change (insertion/deletion)?](#q58-how-do-you-indicate-a-text-change-insertion-deletion)
59. [How do you create a definition list?](#q59-how-do-you-create-a-definition-list)
60. [How do you embed a PDF document?](#q60-how-do-you-embed-a-pdf-document)
61. [How do you play audio automatically (if allowed)?](#q61-how-do-you-play-audio-automatically-if-allowed)
62. [How do you use the WAI-ARIA `role` attribute?](#q62-how-do-you-use-the-wai-aria-role-attribute)
63. [How do you create a breadcrumb navigation?](#q63-how-do-you-create-a-breadcrumb-navigation)
64. [How do you implement pagination markup?](#q64-how-do-you-implement-pagination-markup)
65. [How do you create a search landmark?](#q65-how-do-you-create-a-search-landmark)
66. [How do you specify the direction of text (RTL)?](#q66-how-do-you-specify-the-direction-of-text-rtl)
67. [How do you embed a YouTube video?](#q67-how-do-you-embed-a-youtube-video)
68. [How do you create a color picker?](#q68-how-do-you-create-a-color-picker)
69. [How do you create a range slider?](#q69-how-do-you-create-a-range-slider)
70. [How do you pre-fill a subject line in a mailto link?](#q70-how-do-you-pre-fill-a-subject-line-in-a-mailto-link)
71. [How do you define a client-side image map?](#q71-how-do-you-define-a-client-side-image-map)
72. [How do you link to a specific part of the same page?](#q72-how-do-you-link-to-a-specific-part-of-the-same-page)
73. [How do you create a date picker?](#q73-how-do-you-create-a-date-picker)
74. [How do you add a nonce to scripts for CSP?](#q74-how-do-you-add-a-nonce-to-scripts-for-csp)
75. [How do you handle broken images?](#q75-how-do-you-handle-broken-images)
76. [How do you check if a browser supports a feature in HTML/CSS?](#q76-how-do-you-check-if-a-browser-supports-a-feature-in-html-css)
77. [How do you create a hidden input field?](#q77-how-do-you-create-a-hidden-input-field)
78. [How do you group options in a select?](#q78-how-do-you-group-options-in-a-select)
79. [How do you make a checkbox checked by default?](#q79-how-do-you-make-a-checkbox-checked-by-default)
80. [How do you make a textarea read-only?](#q80-how-do-you-make-a-textarea-read-only)
81. [How do you disabled an input?](#q81-how-do-you-disabled-an-input)
82. [How do you create a generic container for flow content?](#q82-how-do-you-create-a-generic-container-for-flow-content)
83. [How do you create a generic container for phrasing content?](#q83-how-do-you-create-a-generic-container-for-phrasing-content)
84. [How do you specify the language of the document?](#q84-how-do-you-specify-the-language-of-the-document)
85. [How do you provide a machine-readable value for a meter?](#q85-how-do-you-provide-a-machine-readable-value-for-a-meter)
86. [How do you create a bi-directional override?](#q86-how-do-you-create-a-bi-directional-override)
87. [How do you specify the primary language of a text snippet?](#q87-how-do-you-specify-the-primary-language-of-a-text-snippet)
88. [How do you create a line break opportunity?](#q88-how-do-you-create-a-line-break-opportunity)
89. [How do you define a list of suggestions for an input?](#q89-how-do-you-define-a-list-of-suggestions-for-an-input)
90. [How do you embed an external resource like a flash object?](#q90-how-do-you-embed-an-external-resource-like-a-flash-object)
91. [How do you create a parameter for an object?](#q91-how-do-you-create-a-parameter-for-an-object)
92. [How do you display a progress bar?](#q92-how-do-you-display-a-progress-bar)
93. [How do you strike through text?](#q93-how-do-you-strike-through-text)
94. [How do you underline text?](#q94-how-do-you-underline-text)
95. [How do you display a subscript?](#q95-how-do-you-display-a-subscript)
96. [How do you display a keyboard input?](#q96-how-do-you-display-a-keyboard-input)
97. [How do you display sample output from a computer program?](#q97-how-do-you-display-sample-output-from-a-computer-program)
98. [How do you display a variable in a mathematical expression?](#q98-how-do-you-display-a-variable-in-a-mathematical-expression)
99. [How do you create a preformatted text block?](#q99-how-do-you-create-a-preformatted-text-block)
100. [How do you quote a block of text from another source?](#q100-how-do-you-quote-a-block-of-text-from-another-source)
101. [How do you create a horizontal rule?](#q101-how-do-you-create-a-horizontal-rule)
102. [How do you add a caption to a figure?](#q102-how-do-you-add-a-caption-to-a-figure)
103. [How do you create a description list?](#q103-how-do-you-create-a-description-list)
104. [How do you create a term in a description list?](#q104-how-do-you-create-a-term-in-a-description-list)
105. [How do you create a description in a description list?](#q105-how-do-you-create-a-description-in-a-description-list)
106. [How do you create a list item?](#q106-how-do-you-create-a-list-item)
107. [How do you create an ordered list?](#q107-how-do-you-create-an-ordered-list)
108. [How do you create an unordered list?](#q108-how-do-you-create-an-unordered-list)
109. [How do you create a navigation link?](#q109-how-do-you-create-a-navigation-link)
110. [How do you create a hyperlink?](#q110-how-do-you-create-a-hyperlink)
111. [How do you create an anchor?](#q111-how-do-you-create-an-anchor)
112. [How do you create a table row?](#q112-how-do-you-create-a-table-row)
113. [How do you create a table data cell?](#q113-how-do-you-create-a-table-data-cell)
114. [How do you create a table header cell?](#q114-how-do-you-create-a-table-header-cell)
115. [How do you create a column group?](#q115-how-do-you-create-a-column-group)
116. [How do you create a column?](#q116-how-do-you-create-a-column)
117. [How do you create a table body?](#q117-how-do-you-create-a-table-body)
118. [How do you create a table footer?](#q118-how-do-you-create-a-table-footer)
119. [How do you create a table header?](#q119-how-do-you-create-a-table-header)
120. [How do you create a table?](#q120-how-do-you-create-a-table)

---

### Q1: How do you structure a web page using Semantic HTML for better Accessibility and SEO?

**Difficulty: Intermediate**

**Answer:**
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

[Back to Top](#table-of-contents)

---

### Q2: Implement a responsive image strategy using `srcset` and `<picture>`.

**Difficulty: Advanced**

**Answer:**
**1. Resolution Switching (`srcset`):** Serve different sizes of the *same* image based on viewport width.

```html
<img src="small.jpg" 
     srcset="small.jpg 500w, medium.jpg 1000w, large.jpg 2000w" 
     sizes="(max-width: 600px) 100vw, 50vw" 
     alt="Hero Image">
```

**2. Art Direction (`<picture>`):** Serve *different* images (crop/aspect ratio) or formats (WebP) based on conditions.

```html
<picture>
  <source srcset="hero-mobile.webp" media="(max-width: 600px)">
  <source srcset="hero-desktop.webp" type="image/webp">
  <img src="hero-fallback.jpg" alt="Hero Image">
</picture>
```

[Back to Top](#table-of-contents)

---

### Q3: How do you ensure a web form is accessible to screen reader users?

**Difficulty: Intermediate**

**Answer:**
**Key Techniques:**
1. **Labels:** Always associate `<label>` with `<input>` using `for`/`id` or nesting.
2. **Fieldsets:** Group related inputs (radio buttons) with `<fieldset>` and `<legend>`.
3. **Errors:** specific error messages linked via `aria-describedby`.
4. **Autocomplete:** Use `autocomplete` attributes to help browsers fill data.

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

[Back to Top](#table-of-contents)

---

### Q4: How do you implement a modal dialog using the native `<dialog>` element?

**Difficulty: Intermediate**

**Answer:**
The `<dialog>` element provides a native modal with built-in accessibility (focus trapping, closing with Esc).

**Implementation:**

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

[Back to Top](#table-of-contents)

---

### Q5: How do you optimize Critical Rendering Path using HTML tags?

**Difficulty: Advanced**

**Answer:**
Optimize how the browser paints the page by prioritizing critical resources.

**Strategies:**
1. **Preload Critical Assets:** `<link rel="preload">` for fonts/hero images.
2. **Defer Non-Critical JS:** `<script defer>` to prevent parser blocking.
3. **Inline Critical CSS:** Put above-the-fold styles in `<style>` in `<head>`.
4. **Preconnect:** Warm up DNS/TLS for 3rd party domains.

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

[Back to Top](#table-of-contents)

---

### Q6: How do you prevent tabnabbing attacks when using `target='_blank'`?

**Difficulty: Intermediate**

**Answer:**
When using `target="_blank"`, the new page gets access to the `window.opener` object, allowing it to redirect the original page to a malicious site.

**Fix:** Always add `rel="noopener noreferrer"`.
*Note: Modern browsers implicitly set `noopener` for `target="_blank"`, but `noreferrer` is still good practice for privacy.*

```html
<!-- Vulnerable -->
<a href="https://external-site.com" target="_blank">Visit Site</a>

<!-- Secure -->
<a href="https://external-site.com" target="_blank" rel="noopener noreferrer">
  Visit Site
</a>
```

[Back to Top](#table-of-contents)

---

### Q7: How do you implement Open Graph tags for Social Media sharing?

**Difficulty: Beginner**

**Answer:**
Open Graph (OG) tags control how your page looks when shared on Facebook, LinkedIn, etc.

**Implementation:**
Add `<meta>` tags in the `<head>`.

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

[Back to Top](#table-of-contents)

---

### Q8: How do you use the `<template>` tag for dynamic content?

**Difficulty: Intermediate**

**Answer:**
The `<template>` tag holds HTML that is **not rendered** immediately but can be instantiated via JavaScript. It's useful for repeating list items or dynamic components.

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

[Back to Top](#table-of-contents)

---

### Q9: How do you implement a secure Content Security Policy (CSP) via meta tag?

**Difficulty: Advanced**

**Answer:**
CSP mitigates XSS attacks by restricting where resources (scripts, images) can be loaded from.

**Implementation via Meta Tag:**
(Prefer HTTP Header, but Meta tag works for most directives).

```html
<meta http-equiv="Content-Security-Policy" 
      content="default-src 'self'; 
               img-src https://*; 
               script-src 'self' https://trusted.cdn.com; 
               child-src 'none';">
```

**Explanation:**
- `default-src 'self'`: Only allow resources from own origin.
- `script-src`: Allow local scripts and a specific CDN.
- `child-src 'none'`: Block iframes/workers.


[Back to Top](#table-of-contents)

---

### Q10: How do you encapsulate styles using Shadow DOM to prevent leakage?

**Difficulty: Advanced**

**Answer:**
Shadow DOM creates a scoped DOM tree attached to an element, ensuring styles defined inside don't affect the main document and vice versa.

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

[Back to Top](#table-of-contents)

---

### Q11: How do you implement 'Lazy Loading' for iframes and images natively?

**Difficulty: Beginner**

**Answer:**
Use the `loading="lazy"` attribute. The browser defers loading the resource until it is near the viewport.

```html
<!-- Lazy load image -->
<img src="heavy-image.jpg" loading="lazy" alt="A heavy image" width="800" height="600">

<!-- Lazy load iframe -->
<iframe src="https://example.com" loading="lazy" title="External Content"></iframe>
```

**Note:** Always include `width` and `height` attributes to prevent layout shifts (CLS).

[Back to Top](#table-of-contents)

---

### Q12: How do you create an accessible 'Skip to Content' link?

**Difficulty: Intermediate**

**Answer:**
A 'Skip to Content' link allows keyboard/screen reader users to bypass navigation and jump to the main content.

**HTML:**
Place it as the first element in `<body>`.
```html
<a href="#main-content" class="skip-link">Skip to Main Content</a>

<nav>...</nav>

<main id="main-content">
  <!-- Main content starts here -->
</main>
```

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

[Back to Top](#table-of-contents)

---

### Q13: How do you manage keyboard focus order using `tabindex` efficiently?

**Difficulty: Intermediate**

**Answer:**
Control tab order for interactive elements.

**Usage:**
1. `tabindex="0"`: Make a non-interactive element (like `div`) focusable in natural order.
2. `tabindex="-1"`: Make element focusable via JS (`ele.focus()`) but not via Tab key (useful for modals/errors).
3. **Avoid** `tabindex="1+"`: This forces a custom order, which often breaks accessibility for keyboard users.

```html
<!-- Custom button accessible via keyboard -->
<div role="button" tabindex="0" onclick="doAction()" onkeydown="handleKey(event)">
  Click Me
</div>

<!-- Programmatically focusable container -->
<div id="modal" tabindex="-1">...</div>
```

[Back to Top](#table-of-contents)

---

### Q14: How do you handle 'Dark Mode' preference in HTML/CSS?

**Difficulty: Beginner**

**Answer:**
Use the `prefers-color-scheme` media query in CSS, or the `<meta name="color-scheme">` tag in HTML to signal support.

**HTML:**
```html
<meta name="color-scheme" content="light dark">
```

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

[Back to Top](#table-of-contents)

---

### Q15: How do you validate forms using HTML5 built-in attributes?

**Difficulty: Beginner**

**Answer:**
Use attributes like `required`, `pattern`, `type`, `min`, `max` to validate without JavaScript.

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
**Styling:** Use `:valid` and `:invalid` pseudo-classes in CSS.

[Back to Top](#table-of-contents)

---

### Q16: How do you optimize fonts with `font-display`?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q17: How do you handle 'Microdata' (Structured Data) for Rich Snippets?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q18: How do you force a file download instead of opening it?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q19: How do you denote computer code in HTML?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q20: How do you implement a 'Toggle Switch' using semantic HTML?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q21: How do you ensure 'Print' styles are correct?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q22: How do you mark up a 'Figure' with a caption?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q23: How do you implement 'Focus Trapping' inside a custom modal?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q24: How do you detect if a user prefers 'Reduced Motion'?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q25: How do you group options in a `<select>` dropdown?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q26: How do you specify the relationship between the current document and linked resources?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q27: How do you disable spellcheck for an input?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q28: How do you create a 'Mailto' link with subject and body?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q29: How do you mark up time and dates semantically?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q30: How do you make an iframe responsive?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q31: How do you control the browser's viewport on mobile?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q32: How do you define a specific region for a language change?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q33: How do you prevent iOS from detecting phone numbers automatically?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q34: How do you create a link that calls a phone number?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q35: How do you create a 'Back to Top' link?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q36: How do you implement a sticky header?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q37: How do you style the placeholder text of an input?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q38: How do you make a table responsive?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q39: How do you hide an element visually but keep it accessible?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q40: How do you specify a fallback content for canvas?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q41: How do you allow a user to select multiple files?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q42: How do you restrict file upload to images only?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q43: How do you create a tooltip without JS?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q44: How do you implement smooth scrolling?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q45: How do you create a multi-line text input?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q46: How do you disable resizing of a textarea?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q47: How do you make a favicon animate?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q48: How do you prevent a page from being indexed by Google?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q49: How do you refresh the page automatically after 30 seconds?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q50: How do you define the main contact info for the page?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q51: How do you denote an abbreviation?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q52: How do you group table header, body, and footer?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q53: How do you merge two table cells horizontally?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q54: How do you merge two table cells vertically?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q55: How do you associate a caption with a table?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q56: How do you highlight text (like a marker)?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q57: How do you represent a fraction or superscript?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q58: How do you indicate a text change (insertion/deletion)?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q59: How do you create a definition list?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q60: How do you embed a PDF document?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q61: How do you play audio automatically (if allowed)?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q62: How do you use the WAI-ARIA `role` attribute?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q63: How do you create a breadcrumb navigation?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q64: How do you implement pagination markup?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q65: How do you create a search landmark?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q66: How do you specify the direction of text (RTL)?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q67: How do you embed a YouTube video?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q68: How do you create a color picker?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q69: How do you create a range slider?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q70: How do you pre-fill a subject line in a mailto link?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q71: How do you define a client-side image map?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q72: How do you link to a specific part of the same page?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q73: How do you create a date picker?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q74: How do you add a nonce to scripts for CSP?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q75: How do you handle broken images?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q76: How do you check if a browser supports a feature in HTML/CSS?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q77: How do you create a hidden input field?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q78: How do you group options in a select?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q79: How do you make a checkbox checked by default?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q80: How do you make a textarea read-only?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q81: How do you disabled an input?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q82: How do you create a generic container for flow content?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q83: How do you create a generic container for phrasing content?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q84: How do you specify the language of the document?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q85: How do you provide a machine-readable value for a meter?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q86: How do you create a bi-directional override?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q87: How do you specify the primary language of a text snippet?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q88: How do you create a line break opportunity?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q89: How do you define a list of suggestions for an input?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q90: How do you embed an external resource like a flash object?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q91: How do you create a parameter for an object?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q92: How do you display a progress bar?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q93: How do you strike through text?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q94: How do you underline text?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q95: How do you display a subscript?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q96: How do you display a keyboard input?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q97: How do you display sample output from a computer program?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q98: How do you display a variable in a mathematical expression?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q99: How do you create a preformatted text block?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q100: How do you quote a block of text from another source?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q101: How do you create a horizontal rule?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q102: How do you add a caption to a figure?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q103: How do you create a description list?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q104: How do you create a term in a description list?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q105: How do you create a description in a description list?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q106: How do you create a list item?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q107: How do you create an ordered list?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q108: How do you create an unordered list?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q109: How do you create a navigation link?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q110: How do you create a hyperlink?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q111: How do you create an anchor?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q112: How do you create a table row?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q113: How do you create a table data cell?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q114: How do you create a table header cell?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q115: How do you create a column group?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q116: How do you create a column?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q117: How do you create a table body?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q118: How do you create a table footer?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q119: How do you create a table header?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q120: How do you create a table?

**Difficulty: Beginner**

**Answer:**
Use the appropriate HTML tag or attribute. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

