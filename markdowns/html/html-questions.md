# HTML Interview Questions

## Table of Contents

1. [Q1: What is HTML and how does it work?](#q1-what-is-html-and-how-does-it-work)
2. [Q2: What are HTML5 semantic elements and why are they important?](#q2-what-are-html5-semantic-elements-and-why-are-they-important)
3. [Q3: What are the different HTML5 input types and form elements?](#q3-what-are-the-different-html5-input-types-and-form-elements)
4. [Q4: What are some important HTML5 APIs?](#q4-what-are-some-important-html5-apis)
5. [Q5: What is the difference between `<div>` and `<span>`?](#q5-what-is-the-difference-between-`div`-and-`span`)
6. [Q6: What is the purpose of the `<head>` section in an HTML document?](#q6-what-is-the-purpose-of-the-`head`-section-in-an-html-document)
7. [Q7: What are the different types of lists in HTML?](#q7-what-are-the-different-types-of-lists-in-html)
8. [Q8: How do you embed audio and video in a webpage?](#q8-how-do-you-embed-audio-and-video-in-a-webpage)
9. [Q9: What is an `<iframe>` and when should you use it?](#q9-what-is-an-`iframe`-and-when-should-you-use-it)
10. [Q10: What is the difference between `id` and `class` attributes?](#q10-what-is-the-difference-between-`id`-and-`class`-attributes)
11. [Q11: What are `data-*` attributes and how are they used?](#q11-what-are-`data-*`-attributes-and-how-are-they-used)
12. [Q12: What is the purpose of the `alt` attribute on an `<img>` tag?](#q12-what-is-the-purpose-of-the-`alt`-attribute-on-an-`img`-tag)
13. [Q13: How do you create a hyperlink in HTML?](#q13-how-do-you-create-a-hyperlink-in-html)
14. [Q14: What are HTML entities and why are they used?](#q14-what-are-html-entities-and-why-are-they-used)
15. [Q15: What is the difference between `<script>`, `<script async>`, and `<script defer>`?](#q15-what-is-the-difference-between-`script`,-`script-async`,-and-`script-defer`)
16. [Q16: What is CORS and why is it important?](#q16-what-is-cors-and-why-is-it-important)
17. [Q17: What is the difference between `localStorage` and `sessionStorage`?](#q17-what-is-the-difference-between-`localstorage`-and-`sessionstorage`)
18. [Q18: What is the difference between `<canvas>` and `<svg>`?](#q18-what-is-the-difference-between-`canvas`-and-`svg`)
19. [Q19: How do you create responsive images in HTML?](#q19-how-do-you-create-responsive-images-in-html)
20. [Q20: What is the purpose of the `<meta>` tag in HTML?](#q20-what-is-the-purpose-of-the-`meta`-tag-in-html)
21. [Q21: What is the purpose of the `rel` attribute on a `link` tag?](#q21-what-is-the-purpose-of-the-`rel`-attribute-on-a-`link`-tag)
22. [Q22: What are Web Workers and what are they used for?](#q22-what-are-web-workers-and-what-are-they-used-for)
23. [Q23: What are Server-Sent Events (SSE)?](#q23-what-are-server-sent-events-sse)
24. [Q24: Explain the `defer` attribute in a `<script>` tag.](#q24-explain-the-`defer`-attribute-in-a-`script`-tag)
25. [Q25: What is the difference between block and inline elements?](#q25-what-is-the-difference-between-block-and-inline-elements)
26. [Q26: What is the purpose of the `box-sizing` property in CSS?](#q26-what-is-the-purpose-of-the-`box-sizing`-property-in-css)
27. [Q27: What is CSS Specificity and how is it calculated?](#q27-what-is-css-specificity-and-how-is-it-calculated)
28. [Q28: What is the difference between `em` and `rem` units in CSS?](#q28-what-is-the-difference-between-`em`-and-`rem`-units-in-css)
29. [Q29: What is CSS Flexbox and what are its key features?](#q29-what-is-css-flexbox-and-what-are-its-key-features)
30. [Q30: How do you make HTML accessible?](#q30-how-do-you-make-html-accessible)
31. [Q31: What are important HTML elements for SEO?](#q31-what-are-important-html-elements-for-seo)
32. [Q32: How do you optimize HTML for performance?](#q32-how-do-you-optimize-html-for-performance)
33. [Q33: How do you work with HTML5 audio and video elements?](#q33-how-do-you-work-with-html5-audio-and-video-elements)
34. [Q34: What are HTML coding best practices?](#q34-what-are-html-coding-best-practices)
35. [Q35: Explain HTML5 Web Components and their implementation.](#q35-explain-html5-web-components-and-their-implementation)
36. [Q36: Explain HTML5 Performance Optimization techniques.](#q36-explain-html5-performance-optimization-techniques)
37. [Q37: Explain HTML5 Accessibility (a11y) best practices.](#q37-explain-html5-accessibility-a11y-best-practices)
38. [Q38: Explain HTML5 Progressive Web App (PWA) implementation.](#q38-explain-html5-progressive-web-app-pwa-implementation)
39. [Q39: Explain HTML5 Security best practices.](#q39-explain-html5-security-best-practices)
40. [Q40: What are the latest HTML features and how do you implement modern web standards?](#q40-what-are-the-latest-html-features-and-how-do-you-implement-modern-web-standards)
41. [Q41: How do you create and implement custom Web Components?](#q41-how-do-you-create-and-implement-custom-web-components)
42. [Q42: How do you implement advanced Progressive Web App (PWA) features?](#q42-how-do-you-implement-advanced-progressive-web-app-pwa-features)
43. [Q43: How do you implement advanced HTML5 Web APIs and modern browser features?](#q43-how-do-you-implement-advanced-html5-web-apis-and-modern-browser-features)
44. [Q44: How do you implement advanced HTML5 accessibility and inclusive design patterns?](#q44-how-do-you-implement-advanced-html5-accessibility-and-inclusive-design-patterns)
45. [Q45: How do you implement advanced Web Components with Shadow DOM and modern HTML5 features?](#q45-how-do-you-implement-advanced-web-components-with-shadow-dom-and-modern-html5-features)
46. [Q46: How do you implement Progressive Web App (PWA) features with advanced caching strategies and offline functionality?](#q46-how-do-you-implement-progressive-web-app-pwa-features-with-advanced-caching-strategies-and-offline-functionality)
47. [Q47: How do you work with HTML5 Canvas API for graphics and animations?](#q47-how-do-you-work-with-html5-canvas-api-for-graphics-and-animations)
48. [Q48: How do you implement HTML5 Drag and Drop functionality?](#q48-how-do-you-implement-html5-drag-and-drop-functionality)
49. [Q49: How do you work with Web Storage API (localStorage and sessionStorage)?](#q49-how-do-you-work-with-web-storage-api-localstorage-and-sessionstorage)
50. [Q50: What is the difference between `<em>` and `<strong>` tags?](#q50-what-is-the-difference-between-`em`-and-`strong`-tags)
51. [Q51: What is the purpose of the `DOCTYPE` declaration?](#q51-what-is-the-purpose-of-the-`doctype`-declaration)
52. [Q52: What is the difference between an `id` and a `class`?](#q52-what-is-the-difference-between-an-`id`-and-a-`class`)
53. [Q53: What are `data-*` attributes and why are they used?](#q53-what-are-`data-*`-attributes-and-why-are-they-used)
54. [Q54: What is the difference between block and inline elements?](#q54-what-is-the-difference-between-block-and-inline-elements)
55. [Q55: What is the CSS Box Model?](#q55-what-is-the-css-box-model)
56. [Q56: What is CSS Specificity and how is it calculated?](#q56-what-is-css-specificity-and-how-is-it-calculated)
57. [Q57: What is the difference between `display: none;` and `visibility: hidden;`?](#q57-what-is-the-difference-between-`display:-none;`-and-`visibility:-hidden;`)
58. [Q58: What are the different values for the CSS `position` property?](#q58-what-are-the-different-values-for-the-css-`position`-property)
59. [Q59: What is CSS Flexbox?](#q59-what-is-css-flexbox)
60. [Q60: What is CSS Grid?](#q60-what-is-css-grid)
61. [Q61: What is the difference between CSS Flexbox and Grid?](#q61-what-is-the-difference-between-css-flexbox-and-grid)
62. [Q62: What is responsive web design and how are media queries used?](#q62-what-is-responsive-web-design-and-how-are-media-queries-used)
63. [Q63: What are CSS preprocessors and why are they useful?](#q63-what-are-css-preprocessors-and-why-are-they-useful)
64. [Q64: What is the difference between `px`, `em`, and `rem` units?](#q64-what-is-the-difference-between-`px`,-`em`,-and-`rem`-units)
65. [Q65: What is the `z-index` property and how does stacking context work?](#q65-what-is-the-`z-index`-property-and-how-does-stacking-context-work)
66. [Q66: What are pseudo-classes and pseudo-elements in CSS?](#q66-what-are-pseudo-classes-and-pseudo-elements-in-css)
67. [Q67: What is the difference between `==` and `===` in JavaScript?](#q67-what-is-the-difference-between-`==`-and-`===`-in-javascript)
68. [Q68: What is hoisting in JavaScript?](#q68-what-is-hoisting-in-javascript)
69. [Q69: What is the difference between `null` and `undefined` in JavaScript?](#q69-what-is-the-difference-between-`null`-and-`undefined`-in-javascript)
70. [Q70: What is a closure in JavaScript?](#q70-what-is-a-closure-in-javascript)
71. [Q71: Explain the `this` keyword in JavaScript.](#q71-explain-the-`this`-keyword-in-javascript)
72. [Q72: What is prototypal inheritance in JavaScript?](#q72-what-is-prototypal-inheritance-in-javascript)
73. [Q73: What is the difference between Promises and Callbacks?](#q73-what-is-the-difference-between-promises-and-callbacks)
74. [Q74: What is `async/await` and how does it work?](#q74-what-is-`async-await`-and-how-does-it-work)
75. [Q75: What is the Event Loop in JavaScript?](#q75-what-is-the-event-loop-in-javascript)
76. [Q76: What are the differences between `var`, `let`, and `const`?](#q76-what-are-the-differences-between-`var`,-`let`,-and-`const`)
77. [Q77: What are arrow functions and how do they differ from regular functions?](#q77-what-are-arrow-functions-and-how-do-they-differ-from-regular-functions)
78. [Q78: What is the difference between the spread and rest operators?](#q78-what-is-the-difference-between-the-spread-and-rest-operators)
79. [Q79: Explain the array methods `map`, `filter`, and `reduce`.](#q79-explain-the-array-methods-`map`,-`filter`,-and-`reduce`)
80. [Q80: What is the difference between a shallow copy and a deep copy of an object?](#q80-what-is-the-difference-between-a-shallow-copy-and-a-deep-copy-of-an-object)
81. [Q81: What is event delegation in JavaScript?](#q81-what-is-event-delegation-in-javascript)
82. [Q82: What are the differences between `localStorage`, `sessionStorage`, and Cookies?](#q82-what-are-the-differences-between-`localstorage`,-`sessionstorage`,-and-cookies)
83. [Q83: What are debouncing and throttling in JavaScript?](#q83-what-are-debouncing-and-throttling-in-javascript)
84. [Q84: What is the Shadow DOM?](#q84-what-is-the-shadow-dom)
85. [Q85: What are "Void Elements" in HTML?](#q85-what-are-"void-elements"-in-html)
86. [Q86: What is the purpose of the `<template>` tag?](#q86-what-is-the-purpose-of-the-`template`-tag)
87. [Q87: What is the difference between `<link>` and `<a>` tags?](#q87-what-is-the-difference-between-`link`-and-`a`-tags)
88. [Q88: What are Microdata in HTML?](#q88-what-are-microdata-in-html)
89. [Q89: What is the `contenteditable` attribute?](#q89-what-is-the-`contenteditable`-attribute)
90. [Q90: What is the difference between SVG and Canvas?](#q90-what-is-the-difference-between-svg-and-canvas)
91. [Q91: What is the purpose of the `autocomplete` attribute?](#q91-what-is-the-purpose-of-the-`autocomplete`-attribute)
92. [Q92: How do you specify the language of the page content?](#q92-how-do-you-specify-the-language-of-the-page-content)
93. [Q93: What is the `<noscript>` tag?](#q93-what-is-the-`noscript`-tag)
94. [Q94: What is the purpose of the `download` attribute on an anchor tag?](#q94-what-is-the-purpose-of-the-`download`-attribute-on-an-anchor-tag)
95. [Q95: What are the new form input types introduced in HTML5?](#q95-what-are-the-new-form-input-types-introduced-in-html5)
96. [Q96: What is the `<figure>` and `<figcaption>` element?](#q96-what-is-the-`figure`-and-`figcaption`-element)
97. [Q97: What is the difference between `<b>` and `<strong>`?](#q97-what-is-the-difference-between-`b`-and-`strong`)
98. [Q98: What is the difference between `<i>` and `<em>`?](#q98-what-is-the-difference-between-`i`-and-`em`)
99. [Q99: What is the purpose of the `hidden` attribute?](#q99-what-is-the-purpose-of-the-`hidden`-attribute)
100. [Q100: What is the `details` and `summary` element?](#q100-what-is-the-`details`-and-`summary`-element)
101. [Q101: What is the `<dialog>` element and how is it used?](#q101-what-is-the-`dialog`-element-and-how-is-it-used)
102. [Q102: What are the `details` and `summary` tags?](#q102-what-are-the-`details`-and-`summary`-tags)
103. [Q103: What is the difference between `<article>`, `<section>`, and `<div>`?](#q103-what-is-the-difference-between-`article`,-`section`,-and-`div`)
104. [Q104: What is the `picture` element?](#q104-what-is-the-`picture`-element)
105. [Q105: What is the `srcset` attribute?](#q105-what-is-the-`srcset`-attribute)
106. [Q106: What are `meta` tags for SEO?](#q106-what-are-`meta`-tags-for-seo)
107. [Q107: What is Open Graph Protocol?](#q107-what-is-open-graph-protocol)
108. [Q108: What is `preload`, `prefetch`, and `preconnect`?](#q108-what-is-`preload`,-`prefetch`,-and-`preconnect`)
109. [Q109: What is the `template` tag?](#q109-what-is-the-`template`-tag)
110. [Q110: What is `contenteditable`?](#q110-what-is-`contenteditable`)
111. [Q111: What is the `hidden` attribute?](#q111-what-is-the-`hidden`-attribute)
112. [Q112: What is the `tabindex` attribute?](#q112-what-is-the-`tabindex`-attribute)
113. [Q113: What are HTML5 Form Validation attributes?](#q113-what-are-html5-form-validation-attributes)
114. [Q114: What is the `datalist` element?](#q114-what-is-the-`datalist`-element)
115. [Q115: What is the difference between `script` in `head` vs `body`?](#q115-what-is-the-difference-between-`script`-in-`head`-vs-`body`)
116. [Q116: What is a Favicon?](#q116-what-is-a-favicon)
117. [Q117: What is the `base` tag?](#q117-what-is-the-`base`-tag)
118. [Q118: What are Void Elements?](#q118-what-are-void-elements)
119. [Q119: What is the `noscript` tag?](#q119-what-is-the-`noscript`-tag)
120. [Q120: What is Character Encoding?](#q120-what-is-character-encoding)
121. [Q121: What is `autocomplete` attribute?](#q121-what-is-`autocomplete`-attribute)
122. [Q122: What is the `download` attribute?](#q122-what-is-the-`download`-attribute)
123. [Q123: What is Accessibility (a11y)?](#q123-what-is-accessibility-a11y)
124. [Q124: What are ARIA roles?](#q124-what-are-aria-roles)
125. [Q125: What is `aria-label` vs `aria-labelledby`?](#q125-what-is-`aria-label`-vs-`aria-labelledby`)
126. [Q126: What is `DOCTYPE`?](#q126-what-is-`doctype`)
127. [Q127: What is Quirks Mode?](#q127-what-is-quirks-mode)
128. [Q128: What is the `lang` attribute?](#q128-what-is-the-`lang`-attribute)
129. [Q129: What is `target='_blank'` security risk?](#q129-what-is-`target=_blank`-security-risk)
130. [Q130: What is Microdata?](#q130-what-is-microdata)
131. [Q131: What is IndexedDB?](#q131-what-is-indexeddb)
132. [Q132: What is the Geolocation API?](#q132-what-is-the-geolocation-api)
133. [Q133: What is the Drag and Drop API?](#q133-what-is-the-drag-and-drop-api)
134. [Q134: What is the History API?](#q134-what-is-the-history-api)
135. [Q135: What is Content Security Policy (CSP)?](#q135-what-is-content-security-policy-csp)
136. [Q136: What is the `progress` element?](#q136-what-is-the-`progress`-element)
137. [Q137: What is the `meter` element?](#q137-what-is-the-`meter`-element)
138. [Q138: What is the `figure` and `figcaption` element?](#q138-what-is-the-`figure`-and-`figcaption`-element)
139. [Q139: What is the `time` element?](#q139-what-is-the-`time`-element)
140. [Q140: What is the `output` element?](#q140-what-is-the-`output`-element)
141. [Q141: What is the `abbr` element?](#q141-what-is-the-`abbr`-element)
142. [Q142: What is the `kbd` element?](#q142-what-is-the-`kbd`-element)
143. [Q143: What is the `code` element?](#q143-what-is-the-`code`-element)
144. [Q144: What is the `pre` element?](#q144-what-is-the-`pre`-element)
145. [Q145: What is the `blockquote` element?](#q145-what-is-the-`blockquote`-element)
146. [Q146: What is the `cite` element?](#q146-what-is-the-`cite`-element)
147. [Q147: What is the `address` element?](#q147-what-is-the-`address`-element)
148. [Q148: What is the `map` and `area` element?](#q148-what-is-the-`map`-and-`area`-element)
149. [Q149: What is the `track` element?](#q149-what-is-the-`track`-element)
150. [Q150: What is the `wbr` element?](#q150-what-is-the-`wbr`-element)
151. [Q151: What is the `ruby` element?](#q151-what-is-the-`ruby`-element)
152. [Q152: What is `inputmode`?](#q152-what-is-`inputmode`)
153. [Q153: What is the `translate` attribute?](#q153-what-is-the-`translate`-attribute)
154. [Q154: What is the `manifest` attribute?](#q154-what-is-the-`manifest`-attribute)
155. [Q155: What is the `sandbox` attribute for iframes?](#q155-what-is-the-`sandbox`-attribute-for-iframes)
156. [Q156: What is the `srcdoc` attribute for iframes?](#q156-what-is-the-`srcdoc`-attribute-for-iframes)

---

### Q1: What is HTML and how does it work?

**Answer:**
HTML (HyperText Markup Language) is the standard markup language for creating web pages. It describes the structure and content of web documents using elements and tags.

**Basic HTML Structure:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document Title</title>
    <meta name="description" content="Page description">
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Main Heading</h1>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>
    
    <main>
        <section>
            <h2>Section Heading</h2>
            <p>Paragraph content with <strong>strong text</strong> and <em>emphasized text</em>.</p>
        </section>
    </main>
    
    <footer>
        <p>&copy; 2024 Company Name</p>
    </footer>
    
    <script src="script.js"></script>
</body>
</html>
```

**HTML Element Anatomy:**
```html
<!-- Element with attributes -->
<a href="https://example.com" target="_blank" rel="noopener noreferrer">
    Link text
</a>

<!-- Self-closing elements -->
<img src="image.jpg" alt="Description" width="300" height="200">
<br>
<hr>
<input type="text" name="username" required>

<!-- Nested elements -->
<div class="container">
    <p>This is a <span class="highlight">highlighted</span> word.</p>
</div>
```

---

---

### Q2: What are HTML5 semantic elements and why are they important?

**Answer:**
Semantic elements provide meaning to the structure of web content, making it more accessible and SEO-friendly.

**Semantic Layout Structure:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Semantic HTML Example</title>
</head>
<body>
    <!-- Page header -->
    <header>
        <h1>Website Title</h1>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#about">About</a></li>
            </ul>
        </nav>
    </header>
    
    <!-- Main content area -->
    <main>
        <!-- Hero section -->
        <section class="hero">
            <h2>Welcome to Our Website</h2>
            <p>This is the main content area.</p>
        </section>
        
        <!-- Article content -->
        <article>
            <header>
                <h2>Article Title</h2>
                <p>Published on <time datetime="2024-01-15">January 15, 2024</time></p>
                <address>By <a href="mailto:author@example.com">John Doe</a></address>
            </header>
            
            <section>
                <h3>Article Section</h3>
                <p>Article content goes here...</p>
                
                <figure>
                    <img src="chart.png" alt="Sales data chart">
                    <figcaption>Sales performance for Q4 2023</figcaption>
                </figure>
            </section>
            
            <aside>
                <h4>Related Links</h4>
                <ul>
                    <li><a href="#related1">Related Article 1</a></li>
                    <li><a href="#related2">Related Article 2</a></li>
                </ul>
            </aside>
        </article>
    </main>
    
    <!-- Sidebar content -->
    <aside class="sidebar">
        <section>
            <h3>Latest News</h3>
            <ul>
                <li><a href="#news1">News Item 1</a></li>
                <li><a href="#news2">News Item 2</a></li>
            </ul>
        </section>
    </aside>
    
    <!-- Page footer -->
    <footer>
        <section>
            <h3>Contact Information</h3>
            <address>
                123 Main Street<br>
                City, State 12345<br>
                <a href="tel:+1234567890">Phone: (123) 456-7890</a><br>
                <a href="mailto:info@example.com">Email: info@example.com</a>
            </address>
        </section>
        
        <small>&copy; 2024 Company Name. All rights reserved.</small>
    </footer>
</body>
</html>
```

**Content Sectioning Elements:**
```html
<!-- Details and Summary -->
<details>
    <summary>Click to expand</summary>
    <p>This content is hidden by default and can be toggled.</p>
</details>

<!-- Mark element for highlighting -->
<p>Search results for <mark>"HTML5"</mark> found 42 matches.</p>

<!-- Progress and Meter -->
<label for="progress">Download progress:</label>
<progress id="progress" value="70" max="100">70%</progress>

<label for="disk-usage">Disk usage:</label>
<meter id="disk-usage" value="0.6" min="0" max="1">60%</meter>

<!-- Dialog element -->
<dialog id="modal">
    <h2>Modal Title</h2>
    <p>Modal content goes here.</p>
    <button onclick="document.getElementById('modal').close()">Close</button>
</dialog>
```

---

---

### Q3: What are the different HTML5 input types and form elements?

**Answer:**
HTML5 introduced many new input types and form features for better user experience and validation.

**HTML5 Input Types:**
```html
<form action="/submit" method="POST" novalidate>
    <!-- Text inputs -->
    <label for="text">Text:</label>
    <input type="text" id="text" name="text" placeholder="Enter text" required>
    
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" placeholder="user@example.com" required>
    
    <label for="password">Password:</label>
    <input type="password" id="password" name="password" minlength="8" required>
    
    <label for="tel">Phone:</label>
    <input type="tel" id="tel" name="tel" pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}" placeholder="123-456-7890">
    
    <label for="url">Website:</label>
    <input type="url" id="url" name="url" placeholder="https://example.com">
    
    <!-- Number inputs -->
    <label for="number">Number:</label>
    <input type="number" id="number" name="number" min="1" max="100" step="1">
    
    <label for="range">Range:</label>
    <input type="range" id="range" name="range" min="0" max="100" value="50">
    
    <!-- Date and time inputs -->
    <label for="date">Date:</label>
    <input type="date" id="date" name="date" min="2024-01-01" max="2024-12-31">
    
    <label for="time">Time:</label>
    <input type="time" id="time" name="time">
    
    <label for="datetime-local">Date and Time:</label>
    <input type="datetime-local" id="datetime-local" name="datetime-local">
    
    <label for="month">Month:</label>
    <input type="month" id="month" name="month">
    
    <label for="week">Week:</label>
    <input type="week" id="week" name="week">
    
    <!-- File and color inputs -->
    <label for="file">File:</label>
    <input type="file" id="file" name="file" accept=".pdf,.doc,.docx" multiple>
    
    <label for="color">Color:</label>
    <input type="color" id="color" name="color" value="#ff0000">
    
    <!-- Search input -->
    <label for="search">Search:</label>
    <input type="search" id="search" name="search" placeholder="Search...">
    
    <!-- Hidden input -->
    <input type="hidden" name="csrf_token" value="abc123">
    
    <!-- Checkboxes and radio buttons -->
    <fieldset>
        <legend>Preferences</legend>
        
        <input type="checkbox" id="newsletter" name="newsletter" value="yes">
        <label for="newsletter">Subscribe to newsletter</label>
        
        <input type="radio" id="size-small" name="size" value="small">
        <label for="size-small">Small</label>
        
        <input type="radio" id="size-medium" name="size" value="medium" checked>
        <label for="size-medium">Medium</label>
        
        <input type="radio" id="size-large" name="size" value="large">
        <label for="size-large">Large</label>
    </fieldset>
    
    <!-- Select dropdown -->
    <label for="country">Country:</label>
    <select id="country" name="country" required>
        <option value="">Select a country</option>
        <option value="us">United States</option>
        <option value="ca">Canada</option>
        <option value="uk">United Kingdom</option>
    </select>
    
    <!-- Multi-select -->
    <label for="skills">Skills:</label>
    <select id="skills" name="skills" multiple size="4">
        <option value="html">HTML</option>
        <option value="css">CSS</option>
        <option value="js">JavaScript</option>
        <option value="react">React</option>
    </select>
    
    <!-- Textarea -->
    <label for="message">Message:</label>
    <textarea id="message" name="message" rows="4" cols="50" placeholder="Enter your message" maxlength="500"></textarea>
    
    <!-- Datalist for autocomplete -->
    <label for="browser">Choose a browser:</label>
    <input list="browsers" id="browser" name="browser">
    <datalist id="browsers">
        <option value="Chrome">
        <option value="Firefox">
        <option value="Safari">
        <option value="Edge">
    </datalist>
    
    <!-- Submit buttons -->
    <button type="submit">Submit</button>
    <button type="reset">Reset</button>
    <input type="submit" value="Submit Form">
</form>
```

**Form Validation:**
```html
<form>
    <!-- Required field -->
    <input type="text" name="username" required>
    
    <!-- Pattern validation -->
    <input type="text" name="zipcode" pattern="[0-9]{5}" title="5-digit zip code">
    
    <!-- Length validation -->
    <input type="password" name="password" minlength="8" maxlength="20">
    
    <!-- Custom validation message -->
    <input type="email" name="email" required 
           oninvalid="this.setCustomValidity('Please enter a valid email address')"
           oninput="this.setCustomValidity('')">
    
    <!-- Numeric validation -->
    <input type="number" name="age" min="18" max="100" step="1">
    
    <button type="submit">Submit</button>
</form>
```

---

---

### Q4: What are some important HTML5 APIs?

**Answer:**
HTML5 introduced many powerful APIs for enhanced web functionality.

**Geolocation API:**
```html
<button onclick="getLocation()">Get Location</button>
<div id="location"></div>

<script>
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            function(position) {
                const lat = position.coords.latitude;
                const lon = position.coords.longitude;
                document.getElementById('location').innerHTML = 
                    `Latitude: ${lat}<br>Longitude: ${lon}`;
            },
            function(error) {
                document.getElementById('location').innerHTML = 
                    'Error: ' + error.message;
            },
            {
                enableHighAccuracy: true,
                timeout: 5000,
                maximumAge: 0
            }
        );
    } else {
        document.getElementById('location').innerHTML = 
            'Geolocation is not supported by this browser.';
    }
}
</script>
```

**Local Storage API:**
```html
<input type="text" id="dataInput" placeholder="Enter data">
<button onclick="saveData()">Save</button>
<button onclick="loadData()">Load</button>
<button onclick="clearData()">Clear</button>
<div id="output"></div>

<script>
function saveData() {
    const data = document.getElementById('dataInput').value;
    localStorage.setItem('userData', data);
    document.getElementById('output').innerHTML = 'Data saved!';
}

function loadData() {
    const data = localStorage.getItem('userData');
    if (data) {
        document.getElementById('dataInput').value = data;
        document.getElementById('output').innerHTML = 'Data loaded!';
    } else {
        document.getElementById('output').innerHTML = 'No data found!';
    }
}

function clearData() {
    localStorage.removeItem('userData');
    document.getElementById('dataInput').value = '';
    document.getElementById('output').innerHTML = 'Data cleared!';
}
</script>
```

**Canvas API:**
```html
<canvas id="myCanvas" width="400" height="200" style="border: 1px solid #000;"></canvas>

<script>
const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');

// Draw rectangle
ctx.fillStyle = '#007bff';
ctx.fillRect(10, 10, 100, 50);

// Draw circle
ctx.beginPath();
ctx.arc(200, 50, 30, 0, 2 * Math.PI);
ctx.fillStyle = '#28a745';
ctx.fill();

// Draw text
ctx.font = '20px Arial';
ctx.fillStyle = '#dc3545';
ctx.fillText('Hello Canvas!', 10, 100);

// Draw line
ctx.beginPath();
ctx.moveTo(10, 150);
ctx.lineTo(390, 150);
ctx.strokeStyle = '#6c757d';
ctx.lineWidth = 3;
ctx.stroke();
</script>
```

**Drag and Drop API:**
```html
<div class="drag-container">
    <div class="drag-item" draggable="true" ondragstart="drag(event)" id="item1">
        Drag me!
    </div>
</div>

<div class="drop-zone" ondrop="drop(event)" ondragover="allowDrop(event)">
    Drop here
</div>

<script>
function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    ev.dataTransfer.setData('text', ev.target.id);
}

function drop(ev) {
    ev.preventDefault();
    const data = ev.dataTransfer.getData('text');
    const draggedElement = document.getElementById(data);
    ev.target.appendChild(draggedElement);
}
</script>

<style>

---

---

### Q5: What is the difference between `<div>` and `<span>`?

**Answer:**
Both `<div>` and `<span>` are generic HTML elements used to group content. The key difference lies in their display behavior and semantic purpose.

**`<div>` (Division Element):**
- **Block-level element**: It occupies the full width available and starts on a new line.
- **Purpose**: Used to group larger sections of content, such as a layout container, a card, or a section of a page.

**`<span>` (Span Element):**
- **Inline element**: It only occupies the space required for its content and does not start on a new line.
- **Purpose**: Used to group smaller, inline pieces of content, such as a few words within a paragraph, to apply styling or scripting.

**Example:**
```html
<div style="border: 1px solid black; padding: 10px;">
  <h2>This is a heading inside a div</h2>
  <p>This is a paragraph. <span style="color: blue; font-weight: bold;">This part is a span</span> and is styled differently.</p>
  <p>This div takes up the full width.</p>
</div>

<p>Here is another paragraph outside the div.</p>
```

**Summary of Differences:**

| Feature      | `<div>`                               | `<span>`                                   |
|--------------|---------------------------------------|--------------------------------------------|
| **Display**  | Block-level                           | Inline                                     |
| **New Line** | Starts on a new line                  | Does not start on a new line               |
| **Usage**    | Grouping block-level content, layouts | Grouping inline content, styling text      |
| **Content**  | Can contain other block/inline elements | Should primarily contain inline elements/text |

---

---

### Q6: What is the purpose of the `<head>` section in an HTML document?

**Answer:**
The `<head>` section of an HTML document contains machine-readable information (metadata) about the page. It is not displayed in the browser's main content area, but it provides essential information for the browser, search engines, and other web services.

**Key elements found in the `<head>`:**

- **`<title>`**: Sets the title of the page, which appears in the browser tab and search engine results.
- **`<meta>`**: Provides metadata such as character set, viewport settings, page description, keywords, and author.
- **`<link>`**: Used to link external resources, most commonly CSS stylesheets.
- **`<style>`**: Contains inline CSS styles for the document.
- **`<script>`**: Used to include JavaScript files or inline scripts.
- **`<base>`**: Specifies the base URL for all relative URLs in the document.

**Example:**
```html
<head>
    <!-- Character encoding -->
    <meta charset="UTF-8">

    <!-- Viewport settings for responsive design -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- Page title -->
    <title>My Awesome Webpage</title>

    <!-- SEO metadata -->
    <meta name="description" content="A brief description of the page content.">
    <meta name="keywords" content="html, head, metadata, seo">
    <meta name="author" content="John Doe">

    <!-- Link to external stylesheet -->
    <link rel="stylesheet" href="/css/styles.css">

    <!-- Favicon -->
    <link rel="icon" href="/favicon.ico" type="image/x-icon">

    <!-- Inline styles -->
    <style>
        body {
            font-family: Arial, sans-serif;
        }
    </style>

    <!-- JavaScript file -->
    <script src="/js/main.js" defer></script>

    <!-- Base URL -->
    <base href="https://www.example.com/">
</head>
```

---

---

### Q7: What are the different types of lists in HTML?

**Answer:**
HTML provides three main types of lists to structure content: ordered lists, unordered lists, and description lists.

**1. Unordered List (`<ul>`):**
- Used when the order of items is not important.
- Items are typically displayed with bullet points.
- Each list item is defined with the `<li>` tag.

```html
<ul>
  <li>Apple</li>
  <li>Banana</li>
  <li>Orange</li>
</ul>
```

**2. Ordered List (`<ol>`):**
- Used when the order of items is important.
- Items are displayed with numbers by default.
- The `type` attribute can be used to change the marker (e.g., 'A', 'a', 'I', 'i').

```html
<ol type="1">
  <li>First item</li>
  <li>Second item</li>
  <li>Third item</li>
</ol>
```

**3. Description List (`<dl>`):**
- Used to create a list of terms and their descriptions.
- Consists of three tags: `<dl>` (the list itself), `<dt>` (the term), and `<dd>` (the description).

```html
<dl>
  <dt>HTML</dt>
  <dd>HyperText Markup Language, the standard for creating web pages.</dd>
  <dt>CSS</dt>
  <dd>Cascading Style Sheets, used for styling the presentation of a document.</dd>
</dl>
```

**Nested Lists:**
Lists can also be nested inside one another to create hierarchical structures.

```html
<ul>
  <li>Fruit
    <ol>
      <li>Apple</li>
      <li>Banana</li>
    </ol>
  </li>
  <li>Vegetable
    <ul>
      <li>Carrot</li>
      <li>Broccoli</li>
    </ul>
  </li>
</ul>
```

---

---

### Q8: How do you embed audio and video in a webpage?

**Answer:**
HTML5 introduced the `<audio>` and `<video>` elements to natively embed media content in a webpage without requiring plugins like Flash.

**Embedding Audio:**
The `<audio>` element is used to embed sound content.

```html
<audio controls>
  <source src="audio.mp3" type="audio/mpeg">
  <source src="audio.ogg" type="audio/ogg">
  Your browser does not support the audio element.
</audio>
```

**Common `<audio>` Attributes:**
- **`controls`**: Displays standard audio controls (play, pause, volume).
- **`autoplay`**: Starts playing the audio automatically (often blocked by browsers).
- **`loop`**: Repeats the audio once it finishes.
- **`muted`**: Mutes the audio by default.
- **`preload`**: Specifies if and how the audio should be loaded when the page loads ('auto', 'metadata', 'none').

**Embedding Video:**
The `<video>` element is used for embedding video content.

```html
<video width="640" height="360" controls poster="poster.jpg">
  <source src="movie.mp4" type="video/mp4">
  <source src="movie.webm" type="video/webm">
  <track src="captions_en.vtt" kind="captions" srclang="en" label="English">
  Your browser does not support the video tag.
</video>
```

**Common `<video>` Attributes:**
- **`width` / `height`**: Sets the dimensions of the video player.
- **`poster`**: Specifies an image to be shown while the video is downloading or until the user hits play.
- **`playsinline`**: Allows the video to play within the element's playback area on mobile devices.
- **`<source>`**: Allows you to specify multiple media resources for different browser compatibility.
- **`<track>`**: Used to specify timed text tracks (like subtitles or captions).

---

---

### Q9: What is an `<iframe>` and when should you use it?

**Answer:**
An `<iframe>` (Inline Frame) is an HTML element that allows you to embed another HTML document within the current one. This is useful for including content from other sources, such as maps, videos, or advertisements.

**Syntax:**
```html
<iframe src="https://www.example.com" width="600" height="400" title="Example Website"></iframe>
```

**Common `<iframe>` Attributes:**
- **`src`**: The URL of the page to embed.
- **`width` / `height`**: The dimensions of the iframe.
- **`title`**: A descriptive title for accessibility.
- **`allow`**: Specifies a feature policy for the iframe (e.g., `allow="fullscreen"`).
- **`sandbox`**: Enables a set of restrictions for the content in the iframe for security.

**Use Cases:**
- **Embedding third-party content**: YouTube videos, Google Maps, social media widgets.
- **Advertisements**: Displaying ads from an ad network.
- **Isolated components**: Embedding a complex application or widget that needs to be isolated from the main page's CSS and JavaScript.

**Security Considerations:**
- **Clickjacking**: Iframes can be used for clickjacking attacks. Use the `X-Frame-Options` HTTP header or Content Security Policy (CSP) `frame-ancestors` directive to prevent your site from being embedded in malicious iframes.
- **Sandboxing**: Use the `sandbox` attribute to restrict the capabilities of the embedded content, such as preventing scripts from running or forms from being submitted.

**Example of a sandboxed iframe:**
```html
<iframe src="untrusted.html" sandbox="allow-scripts allow-same-origin">
</iframe>
```
This example allows the iframe to run scripts and access its own origin but blocks other potentially dangerous actions.

---

---

### Q10: What is the difference between `id` and `class` attributes?

**Answer:**
Both `id` and `class` are global attributes used to apply identifiers to HTML elements, but they serve different purposes.

**`id` Attribute:**
- **Uniqueness**: The `id` must be unique within the entire HTML document. An `id` should only be used once.
- **Purpose**: Primarily used to identify a single, specific element for JavaScript manipulation (e.g., `document.getElementById()`) or for linking to a specific part of a page with anchor tags (`<a href="#unique-id">`).
- **CSS**: Can be used as a CSS selector (`#unique-id`), but it's highly specific and generally less reusable than classes.

**`class` Attribute:**
- **Reusability**: The same `class` name can be used on multiple elements.
- **Purpose**: Primarily used to group multiple elements that share the same styling or behavior. An element can also have multiple classes, separated by spaces.
- **CSS**: The primary way to apply styles to elements. It promotes reusable and modular CSS.

**Example:**
```html
<!-- Using id for a unique element -->
<header id="main-header">
  <h1>Website Title</h1>
</header>

<!-- Using class for multiple, reusable components -->
<div class="card">
  <h2>Card 1</h2>
  <p>Some text.</p>
</div>

<div class="card featured">
  <h2>Card 2 (Featured)</h2>
  <p>This card has two classes.</p>
</div>

<a href="#main-header">Back to top</a>
```

**CSS:**
```css
/* Styling a unique element by id */
#main-header {
  background-color: #333;
  color: white;
}

/* Styling reusable components by class */
.card {
  border: 1px solid #ccc;
  padding: 1rem;
  margin-bottom: 1rem;
}

.featured {
  border-color: gold;
  background-color: #fffbe6;
}
```

**Summary of Differences:**

| Feature        | `id`                                      | `class`                                       |
|----------------|-------------------------------------------|-----------------------------------------------|
| **Uniqueness** | Must be unique in the document            | Can be used on multiple elements              |
| **Selector**   | CSS: `#id`, JS: `getElementById()`        | CSS: `.class`, JS: `getElementsByClassName()` |
| **Use Case**   | Identifying a single element, page anchors | Styling multiple elements, component styling  |
| **Specificity**| High specificity in CSS                   | Lower specificity, more reusable              |

---

---

### Q11: What are `data-*` attributes and how are they used?

**Answer:**
`data-*` attributes are a way to store custom data private to the page or application, for which there are no more appropriate attributes or elements. They are intended to store data that is primarily used by scripts.

**Syntax:**
The attribute name must start with `data-` and contain no uppercase letters.

```html
<div class="user" data-user-id="12345" data-user-role="admin">
  John Doe
</div>
```

**Accessing `data-*` Attributes in JavaScript:**
You can access these attributes using the `dataset` property of the element object.

```javascript
const userElement = document.querySelector('.user');

// Accessing data attributes
const userId = userElement.dataset.userId; // "12345"
const userRole = userElement.dataset.userRole; // "admin"

console.log(`User ID: ${userId}, Role: ${userRole}`);

// Modifying data attributes
userElement.dataset.userRole = 'editor';
console.log(userElement.dataset.userRole); // "editor"
```

**Accessing `data-*` Attributes in CSS:**
You can also use `data-*` attributes in CSS for styling, using attribute selectors.

```css
.user[data-user-role="admin"] {
  color: red;
  font-weight: bold;
}

.user[data-user-role="editor"] {
  color: blue;
}

/* You can also display the data content */
.user::after {
  content: ' (' attr(data-user-role) ')';
}
```

**Use Cases:**
- Storing extra information about an element that doesn't have a semantic representation (e.g., the ID of a product in a list).
- Triggering JavaScript behavior based on the data.
- Styling elements based on their data.

---

---

### Q12: What is the purpose of the `alt` attribute on an `<img>` tag?

**Answer:**
The `alt` attribute (alternative text) on an `<img>` tag provides a textual alternative to the image. It serves several important purposes:

1.  **Accessibility**: Screen readers read the `alt` text aloud to visually impaired users, allowing them to understand the content and context of the image.

2.  **Broken Images**: If the image fails to load (due to a broken link, slow connection, etc.), the browser will display the `alt` text instead.

3.  **SEO (Search Engine Optimization)**: Search engines use `alt` text to understand the content of an image, which can help with image search rankings.

**How to write good `alt` text:**
-   **Be descriptive but concise**: Describe the important information in the image.
-   **Avoid redundancy**: Don't start with "Image of..." or "Picture of...".
-   **Context is key**: The `alt` text should make sense within the context of the surrounding text.
-   **Decorative images**: If an image is purely decorative and provides no information, use an empty `alt` attribute (`alt=""`). This tells screen readers to ignore the image.

**Examples:**

**Good `alt` text:**
```html
<img src="dog.jpg" alt="A golden retriever playing fetch in a park.">
```

**`alt` text for a logo link:**
```html
<a href="/">
  <img src="logo.png" alt="Homepage">
</a>
```

**Decorative image:**
```html
<img src="background-pattern.png" alt="">

---

---

### Q13: How do you create a hyperlink in HTML?

**Answer:**
Hyperlinks are created using the `<a>` (anchor) tag. The `href` attribute is the most important attribute of the `<a>` tag, as it specifies the destination of the link.

**Types of Hyperlinks:**

**1. External Link:**
Links to a page on a different website.
```html
<a href="https://www.google.com">Go to Google</a>
```

**2. Internal Link:**
Links to another page within the same website.
```html
<a href="/about.html">About Us</a>
```

**3. Anchor Link (Jumping to a section on the same page):**
Links to a specific element on the same page that has an `id`.
```html
<a href="#section2">Go to Section 2</a>

<!-- ... later in the page ... -->

<h2 id="section2">Section 2</h2>
```

**4. Email Link:**
Creates a link that opens the user's default email client.
```html
<a href="mailto:contact@example.com">Email Us</a>
```

**5. Telephone Link:**
Creates a link that initiates a phone call on mobile devices.
```html
<a href="tel:+1234567890">Call Us</a>
```

**Important `<a>` Tag Attributes:**
- **`target`**: Specifies where to open the linked document.
  - `_self`: (Default) Opens in the same frame.
  - `_blank`: Opens in a new tab or window.
  - `_parent`: Opens in the parent frame.
  - `_top`: Opens in the full body of the window.
- **`rel`**: Specifies the relationship between the current document and the linked document. For `target="_blank"`, it's a security best practice to include `rel="noopener noreferrer"`.
- **`download`**: Prompts the user to download the linked file.

**Example with `target` and `rel`:**
```html
<a href="https://www.example.com" target="_blank" rel="noopener noreferrer">
  External Site (opens in new tab)
</a>
```

---

---

### Q14: What are HTML entities and why are they used?

**Answer:**
HTML entities are used to display reserved characters that have a special meaning in HTML (like `<` and `>`), or characters that are not present on a standard keyboard.

An entity consists of an ampersand (`&`), an entity name or number, and a semicolon (`;`).

**Why use HTML entities?**
1.  **To display reserved characters**: If you want to display the `<` character in your text, you need to use an entity (`&lt;`) to prevent the browser from interpreting it as the start of a tag.
2.  **To display special characters**: For symbols like the copyright sign (`©`) or the Euro sign (`€`), entities provide a universal way to display them across different platforms and character sets.

**Common HTML Entities:**

| Character | Entity Name | Entity Number | Description         |
| :-------: | :---------: | :-----------: | ------------------- |
|    `<`    | `&lt;`      | `&#60;`       | Less than           |
|    `>`    | `&gt;`      | `&#62;`       | Greater than        |
|    `&`    | `&amp;`     | `&#38;`       | Ampersand           |
|    `"`    | `&quot;`    | `&#34;`       | Double quote        |
|    `'`    | `&apos;`    | `&#39;`       | Single quote (apostrophe) |
|   ` `   | `&nbsp;`    | `&#160;`      | Non-breaking space  |
|    `©`    | `&copy;`    | `&#169;`      | Copyright           |
|    `®`    | `&reg;`     | `&#174;`      | Registered trademark|
|    `€`    | `&euro;`    | `&#8364;`      | Euro                |

**Example:**
```html
<!-- Displaying code with reserved characters -->
<p>The `&lt;p&gt;` tag is used for paragraphs.</p>

<!-- Using a non-breaking space to keep words together -->
<p>Price: 10&nbsp;€</p>

<!-- Copyright notice -->
<footer>
  <p>&copy; 2024 My Company. All rights reserved.</p>
</footer>
```

---

---

### Q15: What is the difference between `<script>`, `<script async>`, and `<script defer>`?

**Answer:**
These attributes control how an external JavaScript file is downloaded and executed, which significantly impacts page load performance.

**1. `<script>` (Default)**
- **HTML Parsing:** Pauses.
- **Script Download:** Happens immediately, blocking HTML parsing.
- **Script Execution:** Happens immediately after download, also blocking HTML parsing.
- **Order:** Scripts are fetched and executed in the order they appear in the document.

This is render-blocking. If the script is large, the user will see a blank page until it's downloaded and executed.

```html
<script src="main.js"></script>
```

**2. `<script async>`**
- **HTML Parsing:** Does not pause.
- **Script Download:** Happens asynchronously alongside HTML parsing.
- **Script Execution:** Happens as soon as the script is downloaded, which pauses HTML parsing.
- **Order:** Scripts are executed as soon as they are downloaded, not necessarily in the order they appear.

Use `async` for independent scripts that don't rely on other scripts or the DOM being fully parsed (e.g., analytics).

```html
<script async src="analytics.js"></script>
```

**3. `<script defer>`**
- **HTML Parsing:** Does not pause.
- **Script Download:** Happens asynchronously alongside HTML parsing.
- **Script Execution:** Is deferred until the HTML document has been fully parsed (just before the `DOMContentLoaded` event).
- **Order:** Scripts are executed in the order they appear in the document.

Use `defer` for scripts that need the full DOM and/or depend on other scripts. This is often the best choice for performance.

```html
<script defer src="library.js"></script>
<script defer src="main.js"></script> <!-- Executes after library.js -->
```

**Summary Table:**

| Attribute | Pauses HTML Parsing? | Asynchronous Download? | Executes Before DOMContentLoaded? | Execution Order Guaranteed? |
| :-------- | :------------------: | :--------------------: | :-------------------------------: | :-------------------------: |
| `(none)`  |          Yes         |           No           |                Yes                |             Yes             |
| `async`   |   Only on execution  |          Yes           |            Not guaranteed           |              No             |
| `defer`   |          No          |          Yes           |                No                 |             Yes             |

---

---

### Q16: What is CORS and why is it important?

**Answer:**
CORS (Cross-Origin Resource Sharing) is a security mechanism that allows a web page from one origin (domain, protocol, or port) to request resources from a different origin. It is a crucial part of the modern web, enabling complex applications that fetch data from various APIs.

**Why is CORS needed?**
Web browsers enforce a **Same-Origin Policy (SOP)**, which restricts web pages from making requests to a different origin than the one that served the page. This is a critical security measure to prevent malicious scripts on one page from accessing sensitive data on another page.

CORS provides a controlled way to relax the SOP, allowing servers to explicitly permit cross-origin requests from specific origins.

**How CORS Works:**
CORS works by adding new HTTP headers to the request and response. The most important one is `Access-Control-Allow-Origin`.

1.  **Client-Side Request:** When a browser makes a cross-origin request (e.g., using `fetch` or `XMLHttpRequest`), it automatically adds an `Origin` header with the current page's origin.

    ```javascript
    // Request from http://example.com to http://api.com/data
    fetch('http://api.com/data');
    // Browser adds header: Origin: http://example.com
    ```

2.  **Server-Side Response:** The server at `api.com` receives the request. If it wants to allow the request, it must include the `Access-Control-Allow-Origin` header in its response.

    -   To allow a specific origin:
        `Access-Control-Allow-Origin: http://example.com`
    -   To allow any origin (less secure):
        `Access-Control-Allow-Origin: *`

3.  **Browser Enforcement:** The browser receives the response. If the `Access-Control-Allow-Origin` header is missing or doesn't match the page's origin, the browser blocks the request, and the JavaScript code receives an error.

**Preflight Requests (`OPTIONS`):**
For requests that can modify data (e.g., `PUT`, `DELETE`) or have custom headers, the browser sends a "preflight" request using the `OPTIONS` method first. This request asks the server for permission before sending the actual request. The server must respond with the appropriate CORS headers (`Access-Control-Allow-Methods`, `Access-Control-Allow-Headers`) to approve the preflight check.

---

---

### Q17: What is the difference between `localStorage` and `sessionStorage`?

**Answer:**
Both `localStorage` and `sessionStorage` are part of the Web Storage API, which allows browsers to store key/value pairs locally on the user's computer. They provide a way to store data on the client-side that persists across page reloads.

The main difference lies in their **persistence and scope**.

**`localStorage`**
- **Persistence:** The data has no expiration time. It remains until it is explicitly cleared through JavaScript or by the user clearing their browser cache/data.
- **Scope:** The data is shared across all tabs and windows from the same origin (domain).
- **Use Cases:** Storing user preferences (like a theme), keeping a user logged in, or storing data that needs to be available for a long time.

**`sessionStorage`**
- **Persistence:** The data is only available for the duration of the page session. A session ends when the browser tab is closed. Reloading the page does not clear it.
- **Scope:** The data is scoped to a single browser tab. Data in one tab is not accessible in another tab, even if they are from the same origin.
- **Use Cases:** Storing temporary data for a multi-step form, preserving application state for a single session, or storing data that should be discarded after the user leaves.

**Summary Table:**

| Feature          | `localStorage`                               | `sessionStorage`                             |
| :--------------- | :------------------------------------------- | :------------------------------------------- |
| **Lifetime**     | Persists until explicitly deleted            | Persists for one session (until tab is closed) |
| **Scope**        | Shared across all tabs/windows of an origin  | Scoped to a single tab                       |
| **Accessibility**| Available in any tab or window from the origin | Only available in the tab that created it    |
| **Data Sharing** | Data is shared between tabs                  | Data is isolated between tabs                |

**API and Example:**
Both objects share the same API methods:
- `setItem(key, value)`: Add a key/value pair.
- `getItem(key)`: Retrieve an item by its key.
- `removeItem(key)`: Remove an item by its key.
- `clear()`: Remove all items.
- `key(index)`: Get the key at a given index.
- `length`: Get the number of stored items.

```javascript
// --- localStorage Example ---

// Store a user's preferred theme
localStorage.setItem('theme', 'dark');

// Retrieve the theme on a different page or later visit
const currentTheme = localStorage.getItem('theme'); // 'dark'

// --- sessionStorage Example ---

// Store temporary form data in a multi-step process
sessionStorage.setItem('formStep1Data', 'Some user input');

// Retrieve it on the next step in the same tab
const step1Data = sessionStorage.getItem('formStep1Data');

// This data will be gone if the user closes and reopens the tab.
```

---

---

### Q18: What is the difference between `<canvas>` and `<svg>`?

**Answer:**
Both `<canvas>` and `<svg>` are used to draw graphics on a web page, but they work in fundamentally different ways and are suited for different tasks.

**`<canvas>`**
- **Type:** Raster-based (pixel-based).
- **How it works:** Provides a drawing surface where you can draw graphics dynamically using JavaScript. Once drawn, the graphics are not part of the DOM.
- **Performance:** Better for a large number of objects or fast, real-time animations (like games).
- **Scalability:** Resolution-dependent. Graphics can become pixelated when scaled up.
- **Accessibility:** Poor. Content is not accessible to screen readers.
- **Use Cases:** Games, data visualizations, image editing applications, real-time video processing.

**`<svg>` (Scalable Vector Graphics)**
- **Type:** Vector-based (shape-based).
- **How it works:** Defines graphics using an XML-based markup language. Each shape is a DOM element that can be manipulated with CSS and JavaScript.
- **Performance:** Can be slow with a very large number of elements, as each one is a node in the DOM.
- **Scalability:** Resolution-independent. Graphics scale perfectly to any size without losing quality.
- **Accessibility:** Excellent. Text within SVG is accessible, and you can add titles and descriptions to elements.
- **Use Cases:** Logos, icons, illustrations, charts, and diagrams where scalability and interactivity are important.

**Summary Table:**

| Feature           | `<canvas>`                                  | `<svg>`                                      |
| :---------------- | :------------------------------------------ | :------------------------------------------- |
| **Technology**    | Raster (Bitmap)                             | Vector                                       |
| **Drawing API**   | JavaScript (Imperative)                     | XML/DOM (Declarative)                        |
| **DOM Interaction**| No, it's a single element                   | Yes, every shape is a DOM node               |
| **Scalability**   | Poor, resolution-dependent                  | Excellent, resolution-independent            |
| **Performance**   | High for complex scenes and animations      | Can be slow with many elements               |
| **Accessibility** | Poor                                        | Good, supports text and ARIA attributes      |
| **Best For**      | Dynamic graphics, games, pixel manipulation | High-quality, scalable icons, charts, logos  |

**Example:**

**Canvas (drawing a red rectangle):**
```html
<canvas id="myCanvas" width="200" height="100"></canvas>
<script>
  const canvas = document.getElementById('myCanvas');
  const ctx = canvas.getContext('2d');
  ctx.fillStyle = 'red';
  ctx.fillRect(10, 10, 150, 80);
</script>
```

**SVG (creating a red rectangle):**
```html
<svg width="200" height="100">
  <rect x="10" y="10" width="150" height="80" style="fill:red" />
</svg>
```

---

---

### Q19: How do you create responsive images in HTML?

**Answer:**
Responsive images are crucial for performance and user experience, ensuring that the browser loads the most appropriate image for the user's device and screen size. There are two main approaches:

**1. Resolution Switching with `srcset` and `sizes`**
This is the most common technique. It allows the browser to choose the best image from a set of options based on the device's resolution and viewport width.

- **`srcset`**: A comma-separated list of image URLs and their intrinsic widths (e.g., `image-small.jpg 400w`, `image-large.jpg 800w`). The `w` descriptor tells the browser the width of the image file.
- **`sizes`**: A comma-separated list of media conditions and the width of the image slot for that condition. This tells the browser how wide the image will be displayed on the page at different viewport widths. The last item is the default.

**Example:**
```html
<img 
  srcset="image-small.jpg 400w, 
          image-medium.jpg 800w, 
          image-large.jpg 1200w"
  sizes="(max-width: 600px) 100vw, 
         (max-width: 900px) 50vw, 
         33vw"
  src="image-medium.jpg" 
  alt="A responsive image.">
```

**How it works:**
- If the viewport is `600px` or less, the image will take up `100%` of the viewport width (`100vw`). The browser might choose `image-small.jpg` or `image-medium.jpg`.
- If the viewport is between `601px` and `900px`, the image will take up `50%` of the viewport width (`50vw`).
- Above `900px`, the image will take up `33%` of the viewport width (`33vw`).
- The `src` attribute is a fallback for older browsers that don't support `srcset`.

**2. Art Direction with the `<picture>` Element**
This technique is used when you need to show completely different images at different screen sizes (e.g., a cropped version on mobile).

- **`<picture>`**: A container element.
- **`<source>`**: One or more source elements, each with a `media` attribute (a media query) and a `srcset` attribute.
- **`<img>`**: The fallback element, which is always required and is displayed if no media queries match.

**Example:**
```html
<picture>
  <!-- Show this image on screens 700px or wider -->
  <source media="(min-width: 700px)" srcset="image-wide.jpg">
  
  <!-- Show this image on screens 500px or wider -->
  <source media="(min-width: 500px)" srcset="image-medium.jpg">
  
  <!-- Fallback image for screens smaller than 500px and older browsers -->
  <img src="image-narrow.jpg" alt="A description of the image.">
</picture>
```

---

---

### Q20: What is the purpose of the `<meta>` tag in HTML?

**Answer:**
The `<meta>` tag, placed inside the `<head>` section, provides metadata about the HTML document. Metadata is data (information) about data; it is not displayed on the page but is machine-parsable. It is used by browsers, search engines, and other web services.

**Common Uses of the `<meta>` Tag:**

**1. Specifying Character Set:**
This is crucial for ensuring the browser interprets the text content correctly. UTF-8 is the standard.
```html
<meta charset="UTF-8">
```

**2. SEO and Social Media Optimization:**
   - **`description`**: A concise summary of the page's content, often used by search engines in search results.
   - **`keywords`**: A list of keywords relevant to the page (less important for modern SEO but still seen).
   - **Open Graph (for Facebook, LinkedIn, etc.)**: Controls how content appears when shared.

```html
<meta name="description" content="High-quality interview questions for HTML, CSS, and JavaScript.">
<meta name="keywords" content="HTML, CSS, JavaScript, Interview, Questions">

<!-- Open Graph Data -->
<meta property="og:title" content="Web Dev Interview Guide">
<meta property="og:type" content="website">
<meta property="og:image" content="https://example.com/image.jpg">
```

**3. Setting the Viewport for Responsive Design:**
This tag is essential for responsive web design, telling the browser how to control the page's dimensions and scaling.
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```
- `width=device-width`: Sets the width of the page to follow the screen-width of the device.
- `initial-scale=1.0`: Sets the initial zoom level when the page is first loaded by the browser.

**4. Controlling Browser Behavior:**
   - **`http-equiv`**: Can be used to simulate an HTTP response header.

```html
<!-- Auto-refresh the page every 30 seconds -->
<meta http-equiv="refresh" content="30">

<!-- Set compatibility mode for Internet Explorer -->
<meta http-equiv="X-UA-Compatible" content="IE=edge">
```

**5. Author Information:**
```html
<meta name="author" content="John Doe">
```

---

---

### Q21: What is the purpose of the `rel` attribute on a `link` tag?

**Answer:**
The `rel` attribute on a `<link>` tag specifies the relationship between the current document and the linked resource. It is a required attribute and is crucial for the browser to understand how to handle the linked file.

**Common `rel` attribute values:**

**1. `stylesheet`**
This is the most common value. It indicates that the linked resource is a CSS stylesheet.
```html
<link rel="stylesheet" href="/css/styles.css">
```

**2. `icon`**
Specifies the favicon for the website, which is displayed in the browser tab and bookmarks.
```html
<link rel="icon" href="/favicon.ico" type="image/x-icon">
<link rel="apple-touch-icon" href="/apple-touch-icon.png"> <!-- For Apple devices -->
```

**3. `preconnect`**
Instructs the browser to connect to a domain in advance without revealing any private information. This can speed up the loading of resources from that domain later on.
```html
<link rel="preconnect" href="https://fonts.gstatic.com">
```

**4. `preload`**
Instructs the browser to fetch a resource in the background with a high priority, because it will be needed soon. This is useful for critical resources like fonts or above-the-fold images.
```html
<link rel="preload" href="/fonts/myfont.woff2" as="font" type="font/woff2" crossorigin>
```
- The `as` attribute is required to specify the type of content being preloaded.

**5. `dns-prefetch`**
Instructs the browser to perform a DNS lookup for a domain in advance. This is a lighter-weight version of `preconnect`.
```html
<link rel="dns-prefetch" href="//example.com">
```

**6. `alternate`**
Indicates an alternate version of the document, such as a print-friendly version, a translation, or an RSS feed.
```html
<!-- Link to an RSS feed -->
<link rel="alternate" type="application/rss+xml" title="RSS Feed" href="/feed.xml">

<!-- Link to a translated version of the page -->
<link rel="alternate" hreflang="es" href="https://example.com/es/">
```

**7. `canonical`**
Specifies the preferred or "canonical" URL for a page that has multiple versions. This is important for SEO to avoid duplicate content issues.
```html
<link rel="canonical" href="https://example.com/products/original-page/">
```

---

---

### Q22: What are Web Workers and what are they used for?

**Answer:**
Web Workers are a simple means for web content to run scripts in background threads. The worker thread can perform tasks without interfering with the user interface. A worker can send and receive messages from the main thread that created it.

**Why use Web Workers?**
JavaScript is single-threaded. Long-running scripts can block the main thread, making the user interface unresponsive (e.g., freezing the page, preventing clicks). Web Workers solve this by allowing you to delegate computationally intensive tasks to a separate thread.

**Use Cases:**
-   Processing large amounts of data (e.g., sorting, searching).
-   Complex calculations (e.g., cryptography, image or video processing).
-   Keeping a persistent connection open with a server (e.g., WebSockets).
-   Prefetching and caching data in the background.

**How Web Workers Work:**
1.  **Main Script:** Creates a new `Worker` object, passing the URL of the worker script.
2.  **Communication:** The main script and the worker communicate using the `postMessage()` method to send messages and an `onmessage` event handler to receive them.
3.  **Worker Script:** The worker script runs in a separate global context. It does not have access to the DOM, the `window` object, or the `document` object.

**Example of a Dedicated Worker:**

**`main.js` (Main Thread)**
```javascript
// 1. Create a new worker
const myWorker = new Worker('worker.js');

// 2. Send a message to the worker
myWorker.postMessage([5, 10]);
console.log('Message posted to worker');

// 3. Listen for messages from the worker
myWorker.onmessage = function(e) {
  console.log('Message received from worker:', e.data);
};

// 4. Handle errors
myWorker.onerror = function(error) {
  console.error('Error in worker:', error.message);
};
```

**`worker.js` (Worker Thread)**
```javascript
// Listen for messages from the main thread
self.onmessage = function(e) {
  console.log('Message received from main script');
  const result = e.data[0] * e.data[1];

  // Send the result back to the main thread
  self.postMessage(result);
};
```

**Types of Web Workers:**
-   **Dedicated Workers:** Are owned by a single script.
-   **Shared Workers:** Can be shared by multiple scripts running in different windows or iframes (from the same origin).
-   **Service Workers:** Act as a proxy server between the web application, the browser, and the network. They are essential for Progressive Web Apps (PWAs), enabling features like offline access and push notifications.

---

---

### Q23: What are Server-Sent Events (SSE)?

**Answer:**
Server-Sent Events (SSE) is a technology that enables a server to push data to a client asynchronously once an initial client connection has been established. It provides a one-way communication channel from the server to the client over a single, long-lived HTTP connection.

**How SSE Works:**
1.  The client creates an `EventSource` object, specifying the URL of an endpoint that will push updates.
2.  The server keeps the connection open and sends messages to the client in a specific text format (`data: ...\n\n`).
3.  The client receives these messages as events in the browser.

**Key Features:**
-   **One-way communication:** Server to client only.
-   **Automatic reconnection:** If the connection is lost, the `EventSource` will automatically try to reconnect.
-   **Standard HTTP:** It works over regular HTTP, so it doesn't require special protocols or servers like WebSockets.
-   **Event-based:** The server can send named events, allowing the client to handle different types of messages.

**SSE vs. WebSockets:**

| Feature             | Server-Sent Events (SSE)          | WebSockets                            |
| :------------------ | :-------------------------------- | :------------------------------------ |
| **Communication**   | Unidirectional (Server -> Client) | Bidirectional (Client <-> Server)     |
| **Protocol**        | Standard HTTP/S                   | WebSocket protocol (`ws://`, `wss://`) |
| **Complexity**      | Simpler to implement              | More complex                          |
| **Reconnection**    | Automatic                         | Manual implementation required        |
| **Data Format**     | UTF-8 text only                   | Text and binary                       |
| **Use Cases**       | News feeds, stock tickers, notifications | Real-time chat, online gaming, collaboration tools |

**Example:**

**Client-Side JavaScript:**
```javascript
const eventSource = new EventSource('/sse-endpoint');

// Listen for messages with the default 'message' event name
eventSource.onmessage = function(event) {
  console.log('New message:', event.data);
};

// Listen for a custom named event
eventSource.addEventListener('update', function(event) {
  console.log('Update received:', event.data);
});

eventSource.onerror = function(err) {
  console.error('EventSource failed:', err);
};
```

**Server-Side (Node.js/Express Example):**
```javascript
app.get('/sse-endpoint', (req, res) => {
  // Set headers for SSE
  res.setHeader('Content-Type', 'text/event-stream');
  res.setHeader('Cache-Control', 'no-cache');
  res.setHeader('Connection', 'keep-alive');
  res.flushHeaders(); // Flush the headers to establish the connection

  // Send a message every 2 seconds
  const intervalId = setInterval(() => {
    const date = new Date().toLocaleTimeString();
    res.write(`data: ${date}\n\n`); // Note the format
  }, 2000);

  // Clean up when the client closes the connection
  req.on('close', () => {
    clearInterval(intervalId);
    res.end();
  });
});
```

---

---

### Q24: Explain the `defer` attribute in a `<script>` tag.

**Answer:**
The `defer` attribute is a boolean attribute for the `<script>` tag that tells the browser to execute the script file after the HTML document has been fully parsed, but before the `DOMContentLoaded` event is fired.

**Key Characteristics of `defer`:**

1.  **Asynchronous Download:** The script is downloaded asynchronously in the background, meaning it does not block the HTML parser. The page continues to render while the script is being downloaded.

2.  **Delayed Execution:** Unlike a regular script, a deferred script is not executed immediately after it's downloaded. Instead, the browser waits until it has finished parsing all the HTML.

3.  **Execution Order:** If there are multiple deferred scripts, they are guaranteed to execute in the order they appear in the HTML document. This is a key difference from the `async` attribute.

**Visual Representation:**

-   **Normal `<script>`:**
    `HTML Parsing -> [Script Download -> Script Execution] -> HTML Parsing Continues`

-   **`<script defer>`:**
    `HTML Parsing --------------------------------------> [All Scripts Execute] -> DOMContentLoaded`
    `           (Script Download in parallel)          `

**When to use `defer`:**
`defer` is the preferred method for including external JavaScript files when:
-   The script needs to access or manipulate the DOM.
-   The script is not critical for the initial rendering of the page.
-   The script depends on another script (and their order needs to be maintained).

By using `defer`, you ensure that your scripts don't block the page from rendering, leading to a faster perceived load time and a better user experience.

**Example:**
In this example, `library.js` is guaranteed to execute before `main.js`, and both will run after the browser has parsed the entire page.

```html
<!DOCTYPE html>
<html>
<head>
  <title>Defer Example</title>
  <script src="library.js" defer></script>
  <script src="main.js" defer></script>
</head>
<body>
  <h1>Hello, World!</h1>
  <p>This content will be visible even while the scripts are downloading.</p>
</body>
</html>
```

**`defer` vs. `async`:**

| Feature             | `defer`                                      | `async`                                      |
| :------------------ | :------------------------------------------- | :------------------------------------------- |
| **Execution Time**  | After HTML parsing is complete               | As soon as the script is downloaded          |
| **Execution Order** | Guaranteed to be in the order of appearance  | No order guaranteed; executes when ready     |
| **DOM Access**      | Safe; DOM is fully parsed                    | Not safe; DOM may not be ready               |
| **Use Case**        | Scripts that need the DOM or depend on others | Independent scripts (e.g., analytics, ads)   |

---

---

### Q25: What is the difference between block and inline elements?

**Answer:**
In HTML, elements are generally categorized as either **block-level** or **inline-level**. This distinction defines how the element behaves in the page layout and what kind of content it can hold.

#### Block-Level Elements

Block-level elements are designed to structure the main parts of your web page. They have the following key characteristics:

1.  **Always Start on a New Line:** They take up the full width available, pushing any subsequent elements to a new line.
2.  **Can Have Width and Height:** You can explicitly set their `width`, `height`, `margin`, and `padding`.
3.  **Can Contain Other Elements:** They can contain other block-level elements and inline-level elements.

**Common Examples:**
-   `<div>`
-   `<p>`
-   `<h1>` - `<h6>`
-   `<ul>`, `<ol>`, `<li>`
-   `<form>`
-   `<table>`
-   `<header>`, `<footer>`, `<section>`, `<article>`

#### Inline-Level Elements

Inline-level elements are used for smaller pieces of content within a block-level element. They do not disrupt the flow of the document.

1.  **Do Not Start on a New Line:** They only take up as much width as necessary and sit within the flow of the text.
2.  **Limited Styling:** You can set horizontal `padding` and `margin`, but vertical `padding` and `margin` (top/bottom) will not affect the surrounding elements. `width` and `height` properties have no effect.
3.  **Can Only Contain Data and Other Inline Elements:** It is semantically incorrect for an inline element to contain a block-level element.

**Common Examples:**
-   `<span>`
-   `<a>`
-   `<img>`
-   `<strong>`, `<em>`
-   `<input>`
-   `<button>`
-   `<label>`

#### Example:

```html
<div style="background-color: lightblue;">
  This is a block-level div. 
  <p style="background-color: lightgreen;">This paragraph is also a block element.</p>
</div>

<p style="background-color: lightcoral;">
  This is a paragraph containing an <span style="background-color: yellow;">inline span</span>, an 
  <a href="#">inline link</a>, and an <img src="#" alt="image"> inline image. They all flow together on the same line.
</p>
```

#### Summary Table

| Feature                  | Block-Level Element                          | Inline-Level Element                         |
| :----------------------- | :------------------------------------------- | :------------------------------------------- |
| **Layout**               | Starts on a new line; takes up full width    | Flows within text; takes up necessary width  |
| **Dimensions**           | `width` and `height` can be set              | `width` and `height` have no effect          |
| **Margin/Padding**       | All sides are respected                      | Only horizontal margin/padding is respected  |
| **Content Model**        | Can contain block and inline elements        | Can contain data and other inline elements   |
| **Primary Use**          | Structural sections of a page                | Text-level semantics and content styling     |

---

---

### Q26: What is the purpose of the `box-sizing` property in CSS?

**Answer:**
The `box-sizing` property in CSS defines how the `width` and `height` of an element are calculated. It determines whether the element's padding and border are included in the total width and height.

There are two main values for `box-sizing`:

1.  `content-box` (the default)
2.  `border-box`

#### `content-box` (Default Behavior)

When `box-sizing` is set to `content-box`, the `width` and `height` properties only apply to the content of the element. The padding and border are added *on top of* the specified width and height, making the element larger than you might expect.

**Total Width** = `width` + `padding-left` + `padding-right` + `border-left` + `border-right`
**Total Height** = `height` + `padding-top` + `padding-bottom` + `border-top` + `border-bottom`

This can make layout calculations tricky. For example, if you want two elements to fit side-by-side in a container, you have to subtract their padding and border from their widths.

#### `border-box` (Intuitive Behavior)

When `box-sizing` is set to `border-box`, the `width` and `height` properties include the content, padding, and border. This means that if you set an element's width to `100px`, it will be exactly `100px` wide on the screen, regardless of its padding or border.

**Total Width** = `width` (includes padding and border)
**Total Height** = `height` (includes padding and border)

The content area inside the element shrinks to accommodate the padding and border.

#### Example:

Let's compare two `div` elements, both with the same width, padding, and border, but different `box-sizing` values.

```html
<style>
  .box {
    width: 200px;
    height: 100px;
    padding: 20px;
    border: 10px solid #333;
    margin-bottom: 20px;
  }

  .content-box {
    box-sizing: content-box; /* Default */
    background-color: lightcoral;
  }

  .border-box {
    box-sizing: border-box;
    background-color: lightblue;
  }
</style>

<div class="box content-box">
  content-box (Total Width: 200 + 40 + 20 = 260px)
</div>

<div class="box border-box">
  border-box (Total Width: 200px)
</div>
```

#### Why `border-box` is Recommended

Using `box-sizing: border-box;` is widely considered a best practice in modern web development. It makes creating layouts much more predictable and intuitive. Many developers apply this rule to all elements on the page with a universal selector:

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}
```

This ensures that all elements use the more manageable `border-box` model, simplifying responsive design and grid layouts.

---

---

### Q27: What is CSS Specificity and how is it calculated?

**Answer:**
CSS Specificity is the set of rules browsers use to determine which CSS style declaration should be applied to an element when multiple, conflicting declarations exist. The more specific a selector is, the higher its precedence, meaning its styles will override those from less specific selectors.

#### How Specificity is Calculated

Specificity is typically calculated by scoring selectors based on their components. A common way to visualize this is as a four-part value, often represented as `(I, C, A, E)`:

1.  **I - Inline Styles:** `(1, 0, 0, 0)` - Styles applied directly to an element using the `style` attribute. This has the highest specificity.
2.  **C - IDs:** `(0, 1, 0, 0)` - Selectors that use an ID (e.g., `#my-id`).
3.  **A - Classes, Attributes, and Pseudo-classes:** `(0, 0, 1, 0)` - Selectors that use a class (`.my-class`), an attribute (`[type="text"]`), or a pseudo-class (`:hover`).
4.  **E - Elements and Pseudo-elements:** `(0, 0, 0, 1)` - Selectors that use an element name (`div`) or a pseudo-element (`::before`).

The universal selector (`*`) and the combinators (`+`, `>`, `~`, ' ') have no effect on specificity (a value of `0, 0, 0, 0`).

**The `!important` Rule**
The `!important` rule is an exception. When used on a style declaration, it overrides any other declaration, regardless of specificity. However, it should be used sparingly as it can make debugging difficult.

#### Example Calculation:

Let's analyze a few selectors:

-   `p` -> Specificity: `(0, 0, 0, 1)` (1 element)
-   `p.intro` -> Specificity: `(0, 0, 1, 1)` (1 class, 1 element)
-   `#main p.intro` -> Specificity: `(0, 1, 1, 1)` (1 ID, 1 class, 1 element)
-   `<p style="color: blue;">` -> Specificity: `(1, 0, 0, 0)` (inline style)

**Conflict Resolution:**
When comparing two selectors, the browser starts from the highest-specificity column (IDs) and moves down. The selector with the higher score in the most specific column wins.

For example, `(0, 1, 0, 0)` is more specific than `(0, 0, 10, 0)` because the single ID outweighs any number of classes.

If two selectors have the same specificity, the one that appears later in the CSS file (or stylesheet order) wins. This is known as the **last-in-wins** rule.

#### Code Example:

```html
<style>
  /* Specificity: 0,0,0,1 */
  p {
    color: blue;
  }

  /* Specificity: 0,0,1,1 */
  p.intro {
    color: green;
  }

  /* Specificity: 0,1,0,1 */
  #main-content p {
    color: red;
  }
</style>

<div id="main-content">
  <p class="intro">This text will be red.</p>
  <p>This text will also be red.</p>
</div>

<p class="intro">This text will be green.</p>
```

**Explanation:**
-   The first two paragraphs are inside the `div` with the ID `main-content`. The selector `#main-content p` has a higher specificity `(0,1,0,1)` than `p.intro` `(0,0,1,1)`, so the text is **red**.
-   The last paragraph is not inside `#main-content`. The selector `p.intro` `(0,0,1,1)` is more specific than `p` `(0,0,0,1)`, so the text is **green**.

---

---

### Q28: What is the difference between `em` and `rem` units in CSS?

**Answer:**
`em` and `rem` are relative length units in CSS, meaning they scale based on the font size of other elements. They are essential for creating scalable and responsive designs, but they have a key difference in what they are relative to.

#### `em` Unit

The `em` unit is relative to the `font-size` of its **direct or nearest parent element**.

-   If an element has a `font-size` of `16px`, then for that element and its children, `1em` = `16px`.
-   The main challenge with `em` units is that they can compound. If you have nested elements and each one uses `em` for font-size, the sizing can become complex and hard to predict.

**Example of Compounding:**

```html
<style>
  .parent {
    font-size: 1.2em; /* 1.2 * 16px = 19.2px (assuming root is 16px) */
  }
  .child {
    font-size: 1.2em; /* 1.2 * 19.2px = 23.04px */
  }
</style>

<div class="parent">
  This is the parent.
  <div class="child">
    This is the child. Its font size has compounded.
  </div>
</div>
```

#### `rem` (Root em) Unit

The `rem` unit is relative only to the `font-size` of the **root element** (the `<html>` element). This avoids the compounding issue of `em` units.

-   By default, the root font size in most browsers is `16px`, so `1rem` = `16px`.
-   No matter how deeply nested an element is, its `rem` value will always be a multiple of the root font size.
-   This makes `rem` units highly predictable and easy to manage for creating consistent spacing and sizing across a website.

**Example:**

```html
<style>
  html {
    font-size: 16px; /* This is the root font size */
  }
  .parent {
    font-size: 1.2rem; /* 1.2 * 16px = 19.2px */
  }
  .child {
    font-size: 1.2rem; /* 1.2 * 16px = 19.2px (does not compound) */
  }
</style>

<div class="parent">
  This is the parent.
  <div class="child">
    This is the child. Its font size is the same as the parent's.
  </div>
</div>
```

#### Summary Table

| Feature          | `em`                                       | `rem` (Root em)                            |
| :--------------- | :----------------------------------------- | :----------------------------------------- |
| **Relative To**  | `font-size` of the parent element          | `font-size` of the root (`<html>`) element |
| **Compounding**  | Yes, values can cascade and compound       | No, values are always relative to the root |
| **Predictability** | Can be complex in nested structures        | Highly predictable and consistent          |
| **Use Case**     | Sizing elements relative to their container (e.g., padding on a button) | Global sizing, typography, and spacing for overall layout consistency |

---

---

### Q29: What is CSS Flexbox and what are its key features?

**Answer:**
CSS Flexbox (Flexible Box Layout) is a one-dimensional layout model that provides an efficient way to arrange, align, and distribute space among items in a container, even when their size is unknown or dynamic. It is the ideal tool for creating responsive layouts and positioning elements within a container.

To use Flexbox, you define a **flex container** by setting its `display` property to `flex` or `inline-flex`. The direct children of this container automatically become **flex items**.

#### Key Features and Properties

Flexbox is controlled by a set of properties on both the container and the items.

**Container Properties:**

1.  **`display`**: Initializes a flex container. (`flex` for block-level, `inline-flex` for inline-level).

2.  **`flex-direction`**: Defines the main axis along which flex items are placed.
    -   `row` (default): Left to right.
    -   `row-reverse`: Right to left.
    -   `column`: Top to bottom.
    -   `column-reverse`: Bottom to top.

3.  **`justify-content`**: Aligns flex items along the **main axis**.
    -   `flex-start` (default): Items are packed at the start.
    -   `flex-end`: Items are packed at the end.
    -   `center`: Items are centered.
    -   `space-between`: Items are evenly distributed with the first item at the start and the last at the end.
    -   `space-around`: Items are evenly distributed with equal space around them.

4.  **`align-items`**: Aligns flex items along the **cross axis** (the axis perpendicular to `flex-direction`).
    -   `stretch` (default): Items stretch to fill the container.
    -   `flex-start`: Items are aligned at the start of the cross axis.
    -   `flex-end`: Items are aligned at the end of the cross axis.
    -   `center`: Items are centered on the cross axis.

5.  **`flex-wrap`**: Controls whether flex items are forced onto one line or can wrap onto multiple lines.
    -   `nowrap` (default): All items are on one line.
    -   `wrap`: Items wrap onto multiple lines if needed.

**Item Properties:**

1.  **`flex-grow`**: Defines the ability of a flex item to grow if necessary. It accepts a unitless value that serves as a proportion.

2.  **`flex-shrink`**: Defines the ability of a flex item to shrink if necessary.

3.  **`flex-basis`**: Defines the default size of an element before the remaining space is distributed.

4.  **`order`**: Controls the order in which items appear in the flex container.

#### Example:

This example creates a container that centers its children both horizontally and vertically.

```html
<style>
  .flex-container {
    display: flex;
    justify-content: center; /* Horizontal centering */
    align-items: center;     /* Vertical centering */
    height: 200px;
    background-color: #f0f0f0;
  }

  .flex-item {
    width: 50px;
    height: 50px;
    margin: 10px;
    background-color: dodgerblue;
    color: white;
    text-align: center;
    line-height: 50px;
  }
</style>

<div class="flex-container">
  <div class="flex-item">1</div>
  <div class="flex-item">2</div>
  <div class="flex-item">3</div>
</div>
```

Flexbox simplifies many layout challenges that were once difficult with traditional methods like floats, making it a fundamental tool for modern CSS development.
```




.drag-item {
    width: 100px;
    height: 50px;
    background: #007bff;
    color: white;
    text-align: center;
    line-height: 50px;
    cursor: move;
    margin: 10px;
}

.drop-zone {
    width: 200px;
    height: 100px;
    border: 2px dashed #ccc;
    text-align: center;
    line-height: 100px;
    margin: 10px;
}

.drop-zone:hover {
    border-color: #007bff;
}
</style>
```

---

---

### Q30: How do you make HTML accessible?

**Answer:**
Accessibility ensures web content is usable by people with disabilities.

**Semantic HTML and ARIA:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Accessible Web Page</title>
</head>
<body>
    <!-- Skip navigation link -->
    <a href="#main-content" class="skip-link">Skip to main content</a>
    
    <!-- Accessible navigation -->
    <nav role="navigation" aria-label="Main navigation">
        <ul>
            <li><a href="#home" aria-current="page">Home</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#services">Services</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>
    
    <!-- Main content with proper heading hierarchy -->
    <main id="main-content">
        <h1>Page Title</h1>
        
        <section>
            <h2>Section Title</h2>
            
            <!-- Accessible form -->
            <form>
                <fieldset>
                    <legend>Personal Information</legend>
                    
                    <label for="firstName">First Name (required):</label>
                    <input type="text" id="firstName" name="firstName" 
                           required aria-describedby="firstName-help">
                    <div id="firstName-help" class="help-text">
                        Enter your first name as it appears on your ID
                    </div>
                    
                    <label for="email">Email:</label>
                    <input type="email" id="email" name="email" 
                           aria-describedby="email-error">
                    <div id="email-error" class="error" aria-live="polite"></div>
                </fieldset>
                
                <!-- Accessible button -->
                <button type="submit" aria-describedby="submit-help">
                    Submit Form
                </button>
                <div id="submit-help" class="help-text">
                    Click to submit your information
                </div>
            </form>
            
            <!-- Accessible table -->
            <table>
                <caption>Sales Data for Q4 2023</caption>
                <thead>
                    <tr>
                        <th scope="col">Month</th>
                        <th scope="col">Sales ($)</th>
                        <th scope="col">Growth (%)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <th scope="row">October</th>
                        <td>$50,000</td>
                        <td>+5%</td>
                    </tr>
                    <tr>
                        <th scope="row">November</th>
                        <td>$55,000</td>
                        <td>+10%</td>
                    </tr>
                </tbody>
            </table>
            
            <!-- Accessible images -->
            <img src="chart.png" alt="Bar chart showing 15% increase in sales from Q3 to Q4">
            
            <!-- Decorative image -->
            <img src="decoration.png" alt="" role="presentation">
            
            <!-- Complex image with long description -->
            <img src="complex-chart.png" alt="Sales performance chart" 
                 aria-describedby="chart-description">
            <div id="chart-description">
                This chart shows sales performance across four quarters...
            </div>
        </section>
        
        <!-- Accessible modal -->
        <button onclick="openModal()" aria-haspopup="dialog">
            Open Modal
        </button>
        
        <div id="modal" role="dialog" aria-labelledby="modal-title" 
             aria-describedby="modal-description" aria-hidden="true">
            <h2 id="modal-title">Modal Title</h2>
            <p id="modal-description">Modal content description</p>
            <button onclick="closeModal()" aria-label="Close modal">
                ×
            </button>
        </div>
    </main>
    
    <!-- Accessible footer -->
    <footer role="contentinfo">
        <p>&copy; 2024 Company Name</p>
    </footer>
</body>
</html>
```

**ARIA Attributes:**
```html
<!-- Live regions for dynamic content -->
<div aria-live="polite" id="status"></div>
<div aria-live="assertive" id="errors"></div>

<!-- Expandable content -->
<button aria-expanded="false" aria-controls="content" onclick="toggle()">
    Show Details
</button>
<div id="content" aria-hidden="true">
    Hidden content that can be toggled
</div>

<!-- Tab interface -->
<div role="tablist" aria-label="Content tabs">
    <button role="tab" aria-selected="true" aria-controls="panel1" id="tab1">
        Tab 1
    </button>
    <button role="tab" aria-selected="false" aria-controls="panel2" id="tab2">
        Tab 2
    </button>
</div>

<div role="tabpanel" id="panel1" aria-labelledby="tab1">
    Content for tab 1
</div>

<div role="tabpanel" id="panel2" aria-labelledby="tab2" hidden>
    Content for tab 2
</div>

<!-- Progress indicator -->
<div role="progressbar" aria-valuenow="70" aria-valuemin="0" 
     aria-valuemax="100" aria-label="Loading progress">
    70% complete
</div>
```

---

---

### Q31: What are important HTML elements for SEO?

**Answer:**
Proper HTML structure and meta tags are crucial for search engine optimization.

**Essential SEO Meta Tags:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Basic meta tags -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- Title tag (most important for SEO) -->
    <title>Page Title - Brand Name | 50-60 characters</title>
    
    <!-- Meta description -->
    <meta name="description" content="Compelling description of the page content in 150-160 characters that encourages clicks from search results.">
    
    <!-- Keywords (less important now) -->
    <meta name="keywords" content="keyword1, keyword2, keyword3">
    
    <!-- Author and copyright -->
    <meta name="author" content="Author Name">
    <meta name="copyright" content="Company Name">
    
    <!-- Robots meta tag -->
    <meta name="robots" content="index, follow">
    <!-- Other options: noindex, nofollow, noarchive, nosnippet -->
    
    <!-- Canonical URL -->
    <link rel="canonical" href="https://example.com/page">
    
    <!-- Open Graph meta tags for social media -->
    <meta property="og:title" content="Page Title">
    <meta property="og:description" content="Page description for social sharing">
    <meta property="og:image" content="https://example.com/image.jpg">
    <meta property="og:url" content="https://example.com/page">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="Site Name">
    
    <!-- Twitter Card meta tags -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:site" content="@username">
    <meta name="twitter:title" content="Page Title">
    <meta name="twitter:description" content="Page description for Twitter">
    <meta name="twitter:image" content="https://example.com/image.jpg">
    
    <!-- Favicon -->
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
    
    <!-- Structured data (JSON-LD) -->
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": "Company Name",
        "url": "https://example.com",
        "logo": "https://example.com/logo.png",
        "contactPoint": {
            "@type": "ContactPoint",
            "telephone": "+1-234-567-8900",
            "contactType": "customer service"
        }
    }
    </script>
</head>
<body>
    <!-- Proper heading hierarchy -->
    <h1>Main Page Heading (only one H1 per page)</h1>
    
    <h2>Section Heading</h2>
    <h3>Subsection Heading</h3>
    
    <!-- Semantic HTML structure -->
    <nav>
        <ul>
            <li><a href="/" title="Home page">Home</a></li>
            <li><a href="/about" title="About us">About</a></li>
            <li><a href="/services" title="Our services">Services</a></li>
        </ul>
    </nav>
    
    <main>
        <article>
            <header>
                <h1>Article Title</h1>
                <time datetime="2024-01-15">January 15, 2024</time>
            </header>
            
            <p>Article content with <strong>important keywords</strong> naturally integrated.</p>
            
            <!-- Optimized images -->
            <img src="optimized-image.webp" 
                 alt="Descriptive alt text with keywords" 
                 width="800" height="600"
                 loading="lazy">
        </article>
    </main>
    
    <!-- Breadcrumb navigation -->
    <nav aria-label="Breadcrumb">
        <ol>
            <li><a href="/">Home</a></li>
            <li><a href="/category">Category</a></li>
            <li aria-current="page">Current Page</li>
        </ol>
    </nav>
</body>
</html>
```

**Structured Data Examples:**
```html
<!-- Article structured data -->
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "Article Title",
    "author": {
        "@type": "Person",
        "name": "Author Name"
    },
    "datePublished": "2024-01-15",
    "dateModified": "2024-01-16",
    "image": "https://example.com/article-image.jpg",
    "publisher": {
        "@type": "Organization",
        "name": "Publisher Name",
        "logo": {
            "@type": "ImageObject",
            "url": "https://example.com/logo.png"
        }
    }
}
</script>

<!-- Local business structured data -->
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "Business Name",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "123 Main St",
        "addressLocality": "City",
        "addressRegion": "State",
        "postalCode": "12345"
    },
    "telephone": "+1-234-567-8900",
    "openingHours": "Mo-Fr 09:00-17:00"
}
</script>
```

---

---

### Q32: How do you optimize HTML for performance?

**Answer:**
HTML performance optimization involves reducing load times and improving rendering speed.

**Resource Loading Optimization:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Performance Optimized Page</title>
    
    <!-- Preconnect to external domains -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://cdn.example.com">
    
    <!-- DNS prefetch for external resources -->
    <link rel="dns-prefetch" href="//analytics.google.com">
    
    <!-- Preload critical resources -->
    <link rel="preload" href="critical.css" as="style">
    <link rel="preload" href="hero-image.webp" as="image">
    <link rel="preload" href="critical.js" as="script">
    
    <!-- Critical CSS inline -->
    <style>
        /* Critical above-the-fold styles */
        body { margin: 0; font-family: system-ui; }
        .hero { height: 100vh; background: #007bff; }
    </style>
    
    <!-- Non-critical CSS with media attribute trick -->
    <link rel="preload" href="styles.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
    <noscript><link rel="stylesheet" href="styles.css"></noscript>
</head>
<body>
    <!-- Optimized images -->
    <picture>
        <source media="(min-width: 800px)" srcset="hero-large.webp">
        <source media="(min-width: 400px)" srcset="hero-medium.webp">
        <img src="hero-small.webp" alt="Hero image" 
             width="800" height="600" 
             loading="eager" 
             decoding="async">
    </picture>
    
    <!-- Lazy loaded images -->
    <img src="placeholder.jpg" 
         data-src="actual-image.webp" 
         alt="Description" 
         loading="lazy" 
         decoding="async"
         width="400" height="300">
    
    <!-- Responsive images with srcset -->
    <img srcset="image-320w.webp 320w,
                 image-480w.webp 480w,
                 image-800w.webp 800w"
         sizes="(max-width: 320px) 280px,
                (max-width: 480px) 440px,
                800px"
         src="image-800w.webp"
         alt="Responsive image"
         loading="lazy">
    
    <!-- Optimized video -->
    <video width="800" height="450" 
           poster="video-poster.webp" 
           preload="metadata"
           controls>
        <source src="video.webm" type="video/webm">
        <source src="video.mp4" type="video/mp4">
        Your browser doesn't support video.
    </video>
    
    <!-- Defer non-critical JavaScript -->
    <script src="analytics.js" defer></script>
    <script src="non-critical.js" async></script>
    
    <!-- Critical JavaScript inline -->
    <script>
        // Critical JavaScript here
        console.log('Page loaded');
    </script>
</body>
</html>
```

**HTML Minification and Compression:**
```html
<!-- Before minification -->
<div class="container">
    <h1>Title</h1>
    <p>Paragraph with some text.</p>
</div>

<!-- After minification -->
<div class="container"><h1>Title</h1><p>Paragraph with some text.</p></div>

<!-- Gzip compression headers (server configuration) -->
<!-- 
Content-Encoding: gzip
Content-Type: text/html; charset=utf-8
-->
```

---

---

### Q33: How do you work with HTML5 audio and video elements?

**Answer:**
HTML5 provides native support for audio and video without plugins.

**Video Element:**
```html
<!-- Basic video -->
<video width="800" height="450" controls>
    <source src="movie.mp4" type="video/mp4">
    <source src="movie.webm" type="video/webm">
    <source src="movie.ogg" type="video/ogg">
    Your browser does not support the video tag.
</video>

<!-- Advanced video with attributes -->
<video width="800" height="450" 
       controls 
       autoplay 
       muted 
       loop 
       poster="video-thumbnail.jpg"
       preload="metadata"
       crossorigin="anonymous">
    <source src="movie-hd.mp4" type="video/mp4" media="(min-width: 1024px)">
    <source src="movie-sd.mp4" type="video/mp4">
    <track kind="subtitles" src="subtitles-en.vtt" srclang="en" label="English">
    <track kind="subtitles" src="subtitles-es.vtt" srclang="es" label="Spanish">
    <track kind="captions" src="captions.vtt" srclang="en" label="English Captions">
    <p>Your browser doesn't support HTML5 video. 
       <a href="movie.mp4">Download the video</a> instead.</p>
</video>

<!-- Responsive video -->
<div class="video-container">
    <video width="100%" height="auto" controls>
        <source src="responsive-video.mp4" type="video/mp4">
    </video>
</div>

<style>
.video-container {
    position: relative;
    width: 100%;
    height: 0;
    padding-bottom: 56.25%; /* 16:9 aspect ratio */
}

.video-container video {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
}
</style>
```

**Audio Element:**
```html
<!-- Basic audio -->
<audio controls>
    <source src="audio.mp3" type="audio/mpeg">
    <source src="audio.ogg" type="audio/ogg">
    <source src="audio.wav" type="audio/wav">
    Your browser does not support the audio element.
</audio>

<!-- Audio with attributes -->
<audio controls 
       autoplay 
       loop 
       muted 
       preload="auto">
    <source src="background-music.mp3" type="audio/mpeg">
    <source src="background-music.ogg" type="audio/ogg">
</audio>

<!-- Audio playlist -->
<div class="audio-playlist">
    <audio id="audioPlayer" controls>
        <source id="audioSource" src="" type="audio/mpeg">
    </audio>
    
    <ul class="playlist">
        <li><button onclick="playTrack('song1.mp3')">Song 1</button></li>
        <li><button onclick="playTrack('song2.mp3')">Song 2</button></li>
        <li><button onclick="playTrack('song3.mp3')">Song 3</button></li>
    </ul>
</div>

<script>
function playTrack(src) {
    const audio = document.getElementById('audioPlayer');
    const source = document.getElementById('audioSource');
    source.src = src;
    audio.load();
    audio.play();
}
</script>
```

**Media API JavaScript:**
```html
<video id="myVideo" width="800" height="450">
    <source src="movie.mp4" type="video/mp4">
</video>

<div class="controls">
    <button onclick="playPause()">Play/Pause</button>
    <button onclick="makeBig()">Big</button>
    <button onclick="makeSmall()">Small</button>
    <button onclick="makeNormal()">Normal</button>
    <input type="range" id="volumeSlider" min="0" max="1" step="0.1" value="1" onchange="setVolume()">
</div>

<script>
const video = document.getElementById('myVideo');

function playPause() {
    if (video.paused) {
        video.play();
    } else {
        video.pause();
    }
}

function makeBig() {
    video.width = 1200;
    video.height = 675;
}

function makeSmall() {
    video.width = 400;
    video.height = 225;
}

function makeNormal() {
    video.width = 800;
    video.height = 450;
}

function setVolume() {
    const slider = document.getElementById('volumeSlider');
    video.volume = slider.value;
}

// Event listeners
video.addEventListener('loadstart', () => console.log('Started loading'));
video.addEventListener('loadeddata', () => console.log('Data loaded'));
video.addEventListener('canplay', () => console.log('Can start playing'));
video.addEventListener('play', () => console.log('Started playing'));
video.addEventListener('pause', () => console.log('Paused'));
video.addEventListener('ended', () => console.log('Ended'));
video.addEventListener('timeupdate', () => {
    console.log('Current time:', video.currentTime);
});
</script>
```

---

---

### Q34: What are HTML coding best practices?

**Answer:**
Following best practices ensures maintainable, accessible, and performant HTML.

**Code Structure and Organization:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Meta tags first -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- Title and description -->
    <title>Page Title</title>
    <meta name="description" content="Page description">
    
    <!-- External resources -->
    <link rel="stylesheet" href="styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
</head>
<body>
    <!-- Use semantic HTML -->
    <header>
        <nav>
            <!-- Use proper list structure for navigation -->
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
            </ul>
        </nav>
    </header>
    
    <main>
        <!-- Use proper heading hierarchy -->
        <h1>Main Page Title</h1>
        
        <section>
            <h2>Section Title</h2>
            
            <!-- Use meaningful class names -->
            <div class="card-container">
                <article class="card">
                    <h3 class="card__title">Card Title</h3>
                    <p class="card__content">Card content</p>
                </article>
            </div>
        </section>
    </main>
    
    <footer>
        <p>&copy; 2024 Company Name</p>
    </footer>
    
    <!-- Scripts at the end of body -->
    <script src="script.js"></script>
</body>
</html>
```

**Validation and Standards:**
```html
<!-- Always include DOCTYPE -->
<!DOCTYPE html>

<!-- Use valid HTML -->
<!-- GOOD -->
<img src="image.jpg" alt="Description">
<input type="text" name="username" id="username">

<!-- BAD -->
<img src="image.jpg"> <!-- Missing alt attribute -->
<input type="text" name="username"> <!-- Missing id for label association -->

<!-- Close all tags properly -->
<!-- GOOD -->
<p>Paragraph content</p>
<br>
<img src="image.jpg" alt="Description">

<!-- BAD -->
<p>Paragraph content
<br>
<img src="image.jpg" alt="Description">

<!-- Use lowercase for tags and attributes -->
<!-- GOOD -->
<div class="container" id="main">

<!-- BAD -->
<DIV CLASS="container" ID="main">

<!-- Quote attribute values -->
<!-- GOOD -->
<div class="container" data-value="123">

<!-- BAD -->
<div class=container data-value=123>
```

**Performance Best Practices:**
```html
<!-- Optimize images -->
<img src="optimized-image.webp" 
     alt="Description" 
     width="400" 
     height="300" 
     loading="lazy" 
     decoding="async">

<!-- Use appropriate input types -->
<input type="email" name="email" autocomplete="email">
<input type="tel" name="phone" autocomplete="tel">
<input type="url" name="website">

<!-- Minimize HTTP requests -->
<link rel="stylesheet" href="combined-styles.css">
<script src="combined-scripts.js"></script>

<!-- Use CDN for common libraries -->
<script src="https://cdn.jsdelivr.net/npm/jquery@3.6.0/dist/jquery.min.js"></script>

<!-- Enable compression -->
<!-- Server configuration for gzip/brotli compression -->
```

This comprehensive HTML guide covers all essential topics from basic structure to advanced APIs and best practices, providing practical examples for interview preparation and development work.

---

---

### Q35: Explain HTML5 Web Components and their implementation.

**Difficulty: Hard**

**Answer:**
Web Components are a set of web platform APIs that allow you to create custom, reusable HTML elements.

**Custom Elements:**
```javascript
// Define a custom element
class CustomButton extends HTMLElement {
  constructor() {
    super();
    
    // Create shadow DOM
    this.attachShadow({ mode: 'open' });
    
    // Create template
    this.shadowRoot.innerHTML = `
      <style>
        :host {
          display: inline-block;
          --button-color: #007bff;
          --button-hover-color: #0056b3;
        }
        
        button {
          background: var(--button-color);
          color: white;
          border: none;
          padding: 0.5rem 1rem;
          border-radius: 0.25rem;
          cursor: pointer;
          font-family: inherit;
          font-size: inherit;
          transition: background-color 0.15s;
        }
        
        button:hover {
          background: var(--button-hover-color);
        }
        
        button:disabled {
          opacity: 0.6;
          cursor: not-allowed;
        }
        
        .icon {
          margin-right: 0.5rem;
        }
      </style>
      <button>
        <span class="icon"></span>
        <slot></slot>
      </button>
    `;
    
    this.button = this.shadowRoot.querySelector('button');
    this.iconSpan = this.shadowRoot.querySelector('.icon');
  }
  
  // Observed attributes
  static get observedAttributes() {
    return ['disabled', 'type', 'icon'];
  }
  
  // Lifecycle callbacks
  connectedCallback() {
    this.button.addEventListener('click', this.handleClick.bind(this));
    this.updateIcon();
  }
  
  disconnectedCallback() {
    this.button.removeEventListener('click', this.handleClick.bind(this));
  }
  
  attributeChangedCallback(name, oldValue, newValue) {
    switch (name) {
      case 'disabled':
        this.button.disabled = newValue !== null;
        break;
      case 'type':
        this.button.type = newValue || 'button';
        break;
      case 'icon':
        this.updateIcon();
        break;
    }
  }
  
  handleClick(event) {
    if (this.disabled) {
      event.preventDefault();
      event.stopPropagation();
      return;
    }
    
    // Dispatch custom event
    this.dispatchEvent(new CustomEvent('custom-click', {
      detail: { originalEvent: event },
      bubbles: true,
      cancelable: true
    }));
  }
  
  updateIcon() {
    const icon = this.getAttribute('icon');
    if (icon) {
      this.iconSpan.innerHTML = `<i class="${icon}"></i>`;
      this.iconSpan.style.display = 'inline';
    } else {
      this.iconSpan.style.display = 'none';
    }
  }
  
  // Public methods
  focus() {
    this.button.focus();
  }
  
  blur() {
    this.button.blur();
  }
  
  // Properties
  get disabled() {
    return this.hasAttribute('disabled');
  }
  
  set disabled(value) {
    if (value) {
      this.setAttribute('disabled', '');
    } else {
      this.removeAttribute('disabled');
    }
  }
}

// Register the custom element
customElements.define('custom-button', CustomButton);

// Advanced custom element with form integration
class CustomInput extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
    
    this.shadowRoot.innerHTML = `
      <style>
        :host {
          display: block;
          margin-bottom: 1rem;
        }
        
        .form-group {
          position: relative;
        }
        
        label {
          display: block;
          margin-bottom: 0.25rem;
          font-weight: 600;
          color: #333;
        }
        
        input {
          width: 100%;
          padding: 0.5rem;
          border: 1px solid #ccc;
          border-radius: 0.25rem;
          font-size: 1rem;
          transition: border-color 0.15s, box-shadow 0.15s;
        }
        
        input:focus {
          outline: none;
          border-color: #007bff;
          box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
        }
        
        input:invalid {
          border-color: #dc3545;
        }
        
        .error-message {
          color: #dc3545;
          font-size: 0.875rem;
          margin-top: 0.25rem;
          display: none;
        }
        
        :host([invalid]) .error-message {
          display: block;
        }
        
        :host([invalid]) input {
          border-color: #dc3545;
        }
      </style>
      <div class="form-group">
        <label></label>
        <input />
        <div class="error-message"></div>
      </div>
    `;
    
    this.label = this.shadowRoot.querySelector('label');
    this.input = this.shadowRoot.querySelector('input');
    this.errorMessage = this.shadowRoot.querySelector('.error-message');
  }
  
  static get observedAttributes() {
    return ['label', 'type', 'placeholder', 'required', 'pattern', 'error-message'];
  }
  
  connectedCallback() {
    this.input.addEventListener('input', this.handleInput.bind(this));
    this.input.addEventListener('blur', this.handleBlur.bind(this));
    this.updateAttributes();
  }
  
  attributeChangedCallback(name, oldValue, newValue) {
    this.updateAttributes();
  }
  
  updateAttributes() {
    this.label.textContent = this.getAttribute('label') || '';
    this.input.type = this.getAttribute('type') || 'text';
    this.input.placeholder = this.getAttribute('placeholder') || '';
    this.input.required = this.hasAttribute('required');
    this.input.pattern = this.getAttribute('pattern') || '';
    this.errorMessage.textContent = this.getAttribute('error-message') || 'Invalid input';
  }
  
  handleInput(event) {
    this.removeAttribute('invalid');
    this.dispatchEvent(new CustomEvent('input', {
      detail: { value: this.input.value },
      bubbles: true
    }));
  }
  
  handleBlur(event) {
    this.validate();
  }
  
  validate() {
    const isValid = this.input.checkValidity();
    if (!isValid) {
      this.setAttribute('invalid', '');
    } else {
      this.removeAttribute('invalid');
    }
    return isValid;
  }
  
  get value() {
    return this.input.value;
  }
  
  set value(val) {
    this.input.value = val;
  }
  
  get validity() {
    return this.input.validity;
  }
  
  get validationMessage() {
    return this.input.validationMessage;
  }
}

customElements.define('custom-input', CustomInput);
```

**Usage:**
```html
<!-- Custom button usage -->
<custom-button icon="fas fa-save">Save Document</custom-button>
<custom-button disabled>Disabled Button</custom-button>

<!-- Custom input usage -->
<custom-input 
  label="Email Address" 
  type="email" 
  placeholder="Enter your email"
  required
  error-message="Please enter a valid email address">
</custom-input>

<script>
// Using custom elements
const button = document.querySelector('custom-button');
button.addEventListener('custom-click', (event) => {
  console.log('Custom button clicked!', event.detail);
});

const input = document.querySelector('custom-input');
input.addEventListener('input', (event) => {
  console.log('Input value:', event.detail.value);
});
</script>
```

---

---

### Q36: Explain HTML5 Performance Optimization techniques.

**Difficulty: Medium**

**Answer:**
HTML5 performance optimization involves reducing load times, improving rendering, and optimizing resource delivery.

**1. Resource Loading Optimization:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- DNS prefetch for external domains -->
  <link rel="dns-prefetch" href="//fonts.googleapis.com">
  <link rel="dns-prefetch" href="//api.example.com">
  
  <!-- Preconnect for critical third-party origins -->
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  
  <!-- Preload critical resources -->
  <link rel="preload" href="/fonts/main.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="/css/critical.css" as="style">
  <link rel="preload" href="/js/main.js" as="script">
  
  <!-- Critical CSS inlined -->
  <style>
    /* Critical above-the-fold styles */
    body { margin: 0; font-family: Arial, sans-serif; }
    .header { background: #333; color: white; padding: 1rem; }
    .hero { height: 100vh; background: #f0f0f0; }
  </style>
  
  <!-- Non-critical CSS loaded asynchronously -->
  <link rel="preload" href="/css/styles.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link rel="stylesheet" href="/css/styles.css"></noscript>
  
  <title>Optimized Page</title>
</head>
<body>
  <!-- Content here -->
  
  <!-- Scripts at the end of body -->
  <script src="/js/main.js" defer></script>
  
  <!-- Non-critical scripts loaded asynchronously -->
  <script>
    // Load analytics asynchronously
    (function() {
      const script = document.createElement('script');
      script.src = '/js/analytics.js';
      script.async = true;
      document.head.appendChild(script);
    })();
  </script>
</body>
</html>
```

**2. Image Optimization:**
```html
<!-- Responsive images with srcset -->
<img src="image-800w.jpg"
     srcset="image-400w.jpg 400w,
             image-800w.jpg 800w,
             image-1200w.jpg 1200w"
     sizes="(max-width: 600px) 400px,
            (max-width: 1000px) 800px,
            1200px"
     alt="Descriptive alt text"
     loading="lazy"
     decoding="async">

<!-- Modern image formats with fallbacks -->
<picture>
  <source srcset="image.avif" type="image/avif">
  <source srcset="image.webp" type="image/webp">
  <img src="image.jpg" alt="Fallback image" loading="lazy">
</picture>

<!-- Hero images with priority loading -->
<img src="hero.jpg" 
     alt="Hero image" 
     fetchpriority="high"
     decoding="sync">

<!-- Background images with intersection observer -->
<div class="lazy-bg" data-bg="background-image.jpg">
  Content here
</div>

<script>
// Lazy load background images
const lazyBgObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const element = entry.target;
      const bgImage = element.dataset.bg;
      element.style.backgroundImage = `url(${bgImage})`;
      lazyBgObserver.unobserve(element);
    }
  });
});

document.querySelectorAll('.lazy-bg').forEach(el => {
  lazyBgObserver.observe(el);
});
</script>
```

**3. Script Loading Optimization:**
```html
<!-- Critical scripts with high priority -->
<script src="/js/critical.js" fetchpriority="high"></script>

<!-- Deferred scripts for non-critical functionality -->
<script src="/js/non-critical.js" defer></script>

<!-- Async scripts for independent functionality -->
<script src="/js/analytics.js" async></script>

<!-- Module scripts for modern browsers -->
<script type="module" src="/js/modern.js"></script>
<script nomodule src="/js/legacy.js"></script>

<!-- Dynamic imports for code splitting -->
<script>
async function loadFeature() {
  const { feature } = await import('/js/feature.js');
  feature.init();
}

// Load on user interaction
document.getElementById('feature-button').addEventListener('click', loadFeature);
</script>

<!-- Service worker registration -->
<script>
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/sw.js')
      .then(registration => {
        console.log('SW registered: ', registration);
      })
      .catch(registrationError => {
        console.log('SW registration failed: ', registrationError);
      });
  });
}
</script>
```

**4. HTML Structure Optimization:**
```html
<!-- Semantic HTML for better parsing -->
<article>
  <header>
    <h1>Article Title</h1>
    <time datetime="2023-12-01">December 1, 2023</time>
  </header>
  
  <section>
    <h2>Section Title</h2>
    <p>Content here...</p>
  </section>
  
  <aside>
    <h3>Related Links</h3>
    <nav>
      <ul>
        <li><a href="#">Link 1</a></li>
        <li><a href="#">Link 2</a></li>
      </ul>
    </nav>
  </aside>
</article>

<!-- Minimize DOM depth -->
<!-- BAD: Deep nesting -->
<div class="wrapper">
  <div class="container">
    <div class="content">
      <div class="article">
        <div class="text">
          <p>Content</p>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- GOOD: Flatter structure -->
<article class="article">
  <p>Content</p>
</article>

<!-- Efficient form structure -->
<form>
  <fieldset>
    <legend>Personal Information</legend>
    
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required autocomplete="name">
    
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required autocomplete="email">
  </fieldset>
  
  <button type="submit">Submit</button>
</form>
```

**5. Performance Monitoring:**
```html
<script>
// Performance monitoring
function measurePerformance() {
  // Core Web Vitals
  new PerformanceObserver((entryList) => {
    for (const entry of entryList.getEntries()) {
      if (entry.name === 'first-contentful-paint') {
        console.log('FCP:', entry.startTime);
      }
    }
  }).observe({ entryTypes: ['paint'] });
  
  // Largest Contentful Paint
  new PerformanceObserver((entryList) => {
    const entries = entryList.getEntries();
    const lastEntry = entries[entries.length - 1];
    console.log('LCP:', lastEntry.startTime);
  }).observe({ entryTypes: ['largest-contentful-paint'] });
  
  // Cumulative Layout Shift
  let clsValue = 0;
  new PerformanceObserver((entryList) => {
    for (const entry of entryList.getEntries()) {
      if (!entry.hadRecentInput) {
        clsValue += entry.value;
      }
    }
    console.log('CLS:', clsValue);
  }).observe({ entryTypes: ['layout-shift'] });
  
  // First Input Delay
  new PerformanceObserver((entryList) => {
    for (const entry of entryList.getEntries()) {
      console.log('FID:', entry.processingStart - entry.startTime);
    }
  }).observe({ entryTypes: ['first-input'] });
}

// Resource timing
function analyzeResources() {
  const resources = performance.getEntriesByType('resource');
  resources.forEach(resource => {
    console.log(`${resource.name}: ${resource.duration}ms`);
  });
}

window.addEventListener('load', () => {
  measurePerformance();
  analyzeResources();
});
</script>
```

---

---

### Q37: Explain HTML5 Accessibility (a11y) best practices.

**Difficulty: Medium**

**Answer:**
HTML5 accessibility ensures web content is usable by people with disabilities through proper semantic markup and ARIA attributes.

**1. Semantic HTML Structure:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Accessible Page Title</title>
</head>
<body>
  <!-- Skip navigation for screen readers -->
  <a href="#main-content" class="skip-link">Skip to main content</a>
  
  <header role="banner">
    <nav role="navigation" aria-label="Main navigation">
      <ul>
        <li><a href="/" aria-current="page">Home</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/contact">Contact</a></li>
      </ul>
    </nav>
  </header>
  
  <main id="main-content" role="main">
    <article>
      <header>
        <h1>Article Title</h1>
        <p>Published on <time datetime="2023-12-01">December 1, 2023</time></p>
      </header>
      
      <section>
        <h2>Section Heading</h2>
        <p>Content with proper heading hierarchy...</p>
        
        <h3>Subsection</h3>
        <p>More content...</p>
      </section>
    </article>
    
    <aside role="complementary" aria-labelledby="sidebar-heading">
      <h2 id="sidebar-heading">Related Information</h2>
      <nav aria-label="Related links">
        <ul>
          <li><a href="#">Related Article 1</a></li>
          <li><a href="#">Related Article 2</a></li>
        </ul>
      </nav>
    </aside>
  </main>
  
  <footer role="contentinfo">
    <p>&copy; 2023 Company Name. All rights reserved.</p>
  </footer>
</body>
</html>
```

**2. Form Accessibility:**
```html
<form>
  <fieldset>
    <legend>Personal Information</legend>
    
    <!-- Proper label association -->
    <div class="form-group">
      <label for="full-name">Full Name *</label>
      <input type="text" 
             id="full-name" 
             name="fullName" 
             required 
             aria-describedby="name-help name-error"
             autocomplete="name">
      <div id="name-help" class="help-text">
        Enter your first and last name
      </div>
      <div id="name-error" class="error-message" aria-live="polite">
        <!-- Error message will be inserted here -->
      </div>
    </div>
    
    <!-- Email with validation -->
    <div class="form-group">
      <label for="email">Email Address *</label>
      <input type="email" 
             id="email" 
             name="email" 
             required 
             aria-describedby="email-help"
             autocomplete="email">
      <div id="email-help" class="help-text">
        We'll use this to send you updates
      </div>
    </div>
    
    <!-- Radio buttons with fieldset -->
    <fieldset>
      <legend>Preferred Contact Method</legend>
      <div class="radio-group">
        <input type="radio" id="contact-email" name="contact" value="email">
        <label for="contact-email">Email</label>
      </div>
      <div class="radio-group">
        <input type="radio" id="contact-phone" name="contact" value="phone">
        <label for="contact-phone">Phone</label>
      </div>
    </fieldset>
    
    <!-- Checkbox with proper labeling -->
    <div class="form-group">
      <input type="checkbox" 
             id="newsletter" 
             name="newsletter" 
             aria-describedby="newsletter-desc">
      <label for="newsletter">Subscribe to newsletter</label>
      <div id="newsletter-desc" class="help-text">
        Receive monthly updates about our products
      </div>
    </div>
    
    <!-- Select with proper labeling -->
    <div class="form-group">
      <label for="country">Country</label>
      <select id="country" name="country" required>
        <option value="">Select a country</option>
        <option value="us">United States</option>
        <option value="ca">Canada</option>
        <option value="uk">United Kingdom</option>
      </select>
    </div>
  </fieldset>
  
  <button type="submit" aria-describedby="submit-help">
    Submit Form
  </button>
  <div id="submit-help" class="help-text">
    All required fields must be completed
  </div>
</form>

<script>
// Form validation with accessibility
function validateForm() {
  const form = document.querySelector('form');
  const nameInput = document.getElementById('full-name');
  const nameError = document.getElementById('name-error');
  
  form.addEventListener('submit', (e) => {
    let isValid = true;
    
    // Validate name
    if (!nameInput.value.trim()) {
      nameError.textContent = 'Full name is required';
      nameInput.setAttribute('aria-invalid', 'true');
      nameInput.focus();
      isValid = false;
    } else {
      nameError.textContent = '';
      nameInput.removeAttribute('aria-invalid');
    }
    
    if (!isValid) {
      e.preventDefault();
    }
  });
  
  // Clear errors on input
  nameInput.addEventListener('input', () => {
    if (nameInput.value.trim()) {
      nameError.textContent = '';
      nameInput.removeAttribute('aria-invalid');
    }
  });
}

validateForm();
</script>
```

**3. Interactive Elements Accessibility:**
```html
<!-- Accessible button -->
<button type="button" 
        aria-expanded="false" 
        aria-controls="dropdown-menu"
        id="dropdown-button">
  Options
  <span aria-hidden="true">▼</span>
</button>

<ul id="dropdown-menu" 
    role="menu" 
    aria-labelledby="dropdown-button"
    hidden>
  <li role="menuitem"><a href="#">Option 1</a></li>
  <li role="menuitem"><a href="#">Option 2</a></li>
  <li role="menuitem"><a href="#">Option 3</a></li>
</ul>

<!-- Accessible modal dialog -->
<div id="modal" 
     role="dialog" 
     aria-labelledby="modal-title"
     aria-describedby="modal-description"
     aria-modal="true"
     hidden>
  <div class="modal-content">
    <header>
      <h2 id="modal-title">Confirm Action</h2>
      <button type="button" 
              class="close-button"
              aria-label="Close dialog">
        <span aria-hidden="true">&times;</span>
      </button>
    </header>
    
    <div id="modal-description">
      <p>Are you sure you want to delete this item?</p>
    </div>
    
    <footer>
      <button type="button" class="cancel-button">Cancel</button>
      <button type="button" class="confirm-button">Delete</button>
    </footer>
  </div>
</div>

<!-- Accessible tabs -->
<div class="tabs">
  <div role="tablist" aria-label="Content sections">
    <button role="tab" 
            aria-selected="true" 
            aria-controls="panel1" 
            id="tab1"
            tabindex="0">
      Tab 1
    </button>
    <button role="tab" 
            aria-selected="false" 
            aria-controls="panel2" 
            id="tab2"
            tabindex="-1">
      Tab 2
    </button>
    <button role="tab" 
            aria-selected="false" 
            aria-controls="panel3" 
            id="tab3"
            tabindex="-1">
      Tab 3
    </button>
  </div>
  
  <div id="panel1" 
       role="tabpanel" 
       aria-labelledby="tab1" 
       tabindex="0">
    <h3>Panel 1 Content</h3>
    <p>Content for the first tab...</p>
  </div>
  
  <div id="panel2" 
       role="tabpanel" 
       aria-labelledby="tab2" 
       tabindex="0" 
       hidden>
    <h3>Panel 2 Content</h3>
    <p>Content for the second tab...</p>
  </div>
  
  <div id="panel3" 
       role="tabpanel" 
       aria-labelledby="tab3" 
       tabindex="0" 
       hidden>
    <h3>Panel 3 Content</h3>
    <p>Content for the third tab...</p>
  </div>
</div>

<script>
// Accessible tabs implementation
class AccessibleTabs {
  constructor(tabsContainer) {
    this.tabsContainer = tabsContainer;
    this.tabs = tabsContainer.querySelectorAll('[role="tab"]');
    this.panels = tabsContainer.querySelectorAll('[role="tabpanel"]');
    
    this.init();
  }
  
  init() {
    this.tabs.forEach((tab, index) => {
      tab.addEventListener('click', () => this.selectTab(index));
      tab.addEventListener('keydown', (e) => this.handleKeydown(e, index));
    });
  }
  
  selectTab(selectedIndex) {
    this.tabs.forEach((tab, index) => {
      const isSelected = index === selectedIndex;
      tab.setAttribute('aria-selected', isSelected);
      tab.tabIndex = isSelected ? 0 : -1;
      
      this.panels[index].hidden = !isSelected;
    });
    
    this.tabs[selectedIndex].focus();
  }
  
  handleKeydown(event, currentIndex) {
    let newIndex = currentIndex;
    
    switch (event.key) {
      case 'ArrowLeft':
        newIndex = currentIndex > 0 ? currentIndex - 1 : this.tabs.length - 1;
        break;
      case 'ArrowRight':
        newIndex = currentIndex < this.tabs.length - 1 ? currentIndex + 1 : 0;
        break;
      case 'Home':
        newIndex = 0;
        break;
      case 'End':
        newIndex = this.tabs.length - 1;
        break;
      default:
        return;
    }
    
    event.preventDefault();
    this.selectTab(newIndex);
  }
}

// Initialize accessible tabs
document.querySelectorAll('.tabs').forEach(tabs => {
  new AccessibleTabs(tabs);
});
</script>
```

**4. Media Accessibility:**
```html
<!-- Images with proper alt text -->
<img src="chart.png" 
     alt="Sales increased 25% from Q1 to Q2, with highest growth in mobile devices">

<!-- Decorative images -->
<img src="decoration.png" alt="" role="presentation">

<!-- Complex images with long descriptions -->
<figure>
  <img src="complex-chart.png" 
       alt="Quarterly sales data" 
       aria-describedby="chart-description">
  <figcaption id="chart-description">
    Detailed description: Q1 sales were $100k, Q2 increased to $125k, 
    Q3 reached $150k, and Q4 peaked at $175k. Mobile sales accounted 
    for 60% of total revenue in Q4.
  </figcaption>
</figure>

<!-- Video with captions and transcripts -->
<video controls 
       aria-labelledby="video-title"
       aria-describedby="video-description">
  <source src="video.mp4" type="video/mp4">
  <source src="video.webm" type="video/webm">
  <track kind="captions" 
         src="captions-en.vtt" 
         srclang="en" 
         label="English captions" 
         default>
  <track kind="subtitles" 
         src="subtitles-es.vtt" 
         srclang="es" 
         label="Spanish subtitles">
  <p>Your browser doesn't support video. 
     <a href="video.mp4">Download the video</a> instead.</p>
</video>

<h3 id="video-title">Product Demo Video</h3>
<p id="video-description">
  This video demonstrates the key features of our product, 
  including setup, basic usage, and advanced features.
</p>

<details>
  <summary>Video Transcript</summary>
  <div>
    <p><strong>0:00</strong> Welcome to our product demo...</p>
    <p><strong>0:15</strong> First, let's look at the setup process...</p>
    <!-- Full transcript here -->
  </div>
</details>

<!-- Audio with transcript -->
<audio controls aria-labelledby="audio-title">
  <source src="podcast.mp3" type="audio/mpeg">
  <source src="podcast.ogg" type="audio/ogg">
  <p>Your browser doesn't support audio. 
     <a href="podcast.mp3">Download the audio</a> instead.</p>
</audio>

<h3 id="audio-title">Weekly Podcast Episode</h3>
<details>
  <summary>Podcast Transcript</summary>
  <div>
    <!-- Full transcript here -->
  </div>
</details>
```

---

---

### Q38: Explain HTML5 Progressive Web App (PWA) implementation.

**Difficulty: Hard**

**Answer:**
Progressive Web Apps use HTML5 features to create app-like experiences that work offline and can be installed on devices.

**1. Web App Manifest:**
```json
// manifest.json
{
  "name": "My Progressive Web App",
  "short_name": "MyPWA",
  "description": "A comprehensive PWA example",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#ffffff",
  "theme_color": "#007bff",
  "orientation": "portrait-primary",
  "scope": "/",
  "lang": "en",
  "dir": "ltr",
  "icons": [
    {
      "src": "/icons/icon-72x72.png",
      "sizes": "72x72",
      "type": "image/png",
      "purpose": "maskable any"
    },
    {
      "src": "/icons/icon-96x96.png",
      "sizes": "96x96",
      "type": "image/png",
      "purpose": "maskable any"
    },
    {
      "src": "/icons/icon-128x128.png",
      "sizes": "128x128",
      "type": "image/png",
      "purpose": "maskable any"
    },
    {
      "src": "/icons/icon-144x144.png",
      "sizes": "144x144",
      "type": "image/png",
      "purpose": "maskable any"
    },
    {
      "src": "/icons/icon-152x152.png",
      "sizes": "152x152",
      "type": "image/png",
      "purpose": "maskable any"
    },
    {
      "src": "/icons/icon-192x192.png",
      "sizes": "192x192",
      "type": "image/png",
      "purpose": "maskable any"
    },
    {
      "src": "/icons/icon-384x384.png",
      "sizes": "384x384",
      "type": "image/png",
      "purpose": "maskable any"
    },
    {
      "src": "/icons/icon-512x512.png",
      "sizes": "512x512",
      "type": "image/png",
      "purpose": "maskable any"
    }
  ],
  "shortcuts": [
    {
      "name": "New Document",
      "short_name": "New",
      "description": "Create a new document",
      "url": "/new",
      "icons": [{ "src": "/icons/new.png", "sizes": "192x192" }]
    },
    {
      "name": "Recent Documents",
      "short_name": "Recent",
      "description": "View recent documents",
      "url": "/recent",
      "icons": [{ "src": "/icons/recent.png", "sizes": "192x192" }]
    }
  ],
  "categories": ["productivity", "utilities"],
  "screenshots": [
    {
      "src": "/screenshots/desktop.png",
      "sizes": "1280x720",
      "type": "image/png",
      "form_factor": "wide"
    },
    {
      "src": "/screenshots/mobile.png",
      "sizes": "750x1334",
      "type": "image/png",
      "form_factor": "narrow"
    }
  ]
}
```

**2. HTML with PWA Meta Tags:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- PWA Meta Tags -->
  <link rel="manifest" href="/manifest.json">
  <meta name="theme-color" content="#007bff">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="default">
  <meta name="apple-mobile-web-app-title" content="MyPWA">
  
  <!-- Apple Touch Icons -->
  <link rel="apple-touch-icon" href="/icons/icon-152x152.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/icons/icon-180x180.png">
  
  <!-- Microsoft Tiles -->
  <meta name="msapplication-TileImage" content="/icons/icon-144x144.png">
  <meta name="msapplication-TileColor" content="#007bff">
  
  <title>My Progressive Web App</title>
</head>
<body>
  <!-- App Shell -->
  <div id="app">
    <header class="app-header">
      <h1>My PWA</h1>
      <button id="install-button" hidden>Install App</button>
    </header>
    
    <nav class="app-nav">
      <ul>
        <li><a href="/" data-route="home">Home</a></li>
        <li><a href="/about" data-route="about">About</a></li>
        <li><a href="/contact" data-route="contact">Contact</a></li>
      </ul>
    </nav>
    
    <main id="main-content" class="app-main">
      <!-- Dynamic content loaded here -->
    </main>
    
    <div id="offline-indicator" class="offline-indicator" hidden>
      <p>You're currently offline. Some features may be limited.</p>
    </div>
  </div>
  
  <!-- Loading indicator -->
  <div id="loading" class="loading-indicator">
    <div class="spinner"></div>
    <p>Loading...</p>
  </div>
  
  <script>
    // Register service worker
    if ('serviceWorker' in navigator) {
      window.addEventListener('load', async () => {
        try {
          const registration = await navigator.serviceWorker.register('/sw.js');
          console.log('SW registered: ', registration);
          
          // Handle updates
          registration.addEventListener('updatefound', () => {
            const newWorker = registration.installing;
            newWorker.addEventListener('statechange', () => {
              if (newWorker.state === 'installed' && navigator.serviceWorker.controller) {
                // New content available
                showUpdateNotification();
              }
            });
          });
        } catch (registrationError) {
          console.log('SW registration failed: ', registrationError);
        }
      });
    }
    
    // Install prompt
    let deferredPrompt;
    const installButton = document.getElementById('install-button');
    
    window.addEventListener('beforeinstallprompt', (e) => {
      e.preventDefault();
      deferredPrompt = e;
      installButton.hidden = false;
    });
    
    installButton.addEventListener('click', async () => {
      if (deferredPrompt) {
        deferredPrompt.prompt();
        const { outcome } = await deferredPrompt.userChoice;
        console.log(`User response to the install prompt: ${outcome}`);
        deferredPrompt = null;
        installButton.hidden = true;
      }
    });
    
    // Handle app installation
    window.addEventListener('appinstalled', (evt) => {
      console.log('App was installed');
      installButton.hidden = true;
    });
    
    // Network status
    function updateOnlineStatus() {
      const offlineIndicator = document.getElementById('offline-indicator');
      offlineIndicator.hidden = navigator.onLine;
    }
    
    window.addEventListener('online', updateOnlineStatus);
    window.addEventListener('offline', updateOnlineStatus);
    updateOnlineStatus();
    
    // Update notification
    function showUpdateNotification() {
      if (confirm('New version available! Reload to update?')) {
        window.location.reload();
      }
    }
  </script>
</body>
</html>
```

**3. Service Worker (sw.js):**
```javascript
const CACHE_NAME = 'my-pwa-v1';
const urlsToCache = [
  '/',
  '/css/styles.css',
  '/js/app.js',
  '/icons/icon-192x192.png',
  '/offline.html'
];

// Install event
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

// Fetch event
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request)
      .then((response) => {
        // Return cached version or fetch from network
        if (response) {
          return response;
        }
        
        return fetch(event.request).catch(() => {
          // If both cache and network fail, show offline page
          if (event.request.destination === 'document') {
            return caches.match('/offline.html');
          }
        });
      })
  );
});

// Activate event
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheName !== CACHE_NAME) {
            console.log('Deleting old cache:', cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});

// Background sync
self.addEventListener('sync', (event) => {
  if (event.tag === 'background-sync') {
    event.waitUntil(doBackgroundSync());
  }
});

// Push notifications
self.addEventListener('push', (event) => {
  const options = {
    body: event.data ? event.data.text() : 'New notification',
    icon: '/icons/icon-192x192.png',
    badge: '/icons/badge.png',
    vibrate: [100, 50, 100],
    data: {
      dateOfArrival: Date.now(),
      primaryKey: 1
    },
    actions: [
      {
        action: 'explore',
        title: 'Explore',
        icon: '/icons/checkmark.png'
      },
      {
        action: 'close',
        title: 'Close',
        icon: '/icons/xmark.png'
      }
    ]
  };
  
  event.waitUntil(
    self.registration.showNotification('PWA Notification', options)
  );
});

// Notification click
self.addEventListener('notificationclick', (event) => {
  event.notification.close();
  
  if (event.action === 'explore') {
    event.waitUntil(
      clients.openWindow('/explore')
    );
  } else if (event.action === 'close') {
    // Just close the notification
  } else {
    // Default action
    event.waitUntil(
      clients.openWindow('/')
    );
  }
});

function doBackgroundSync() {
  // Perform background sync operations
  return fetch('/api/sync')
    .then(response => response.json())
    .then(data => {
      console.log('Background sync completed:', data);
    })
    .catch(error => {
      console.error('Background sync failed:', error);
    });
}
```

---

---

### Q39: Explain HTML5 Security best practices.

**Difficulty: Medium**

**Answer:**
HTML5 security involves protecting against various attacks and implementing secure coding practices.

**1. Content Security Policy (CSP):**
```html
<!-- CSP via meta tag -->
<meta http-equiv="Content-Security-Policy" 
      content="default-src 'self'; 
               script-src 'self' 'unsafe-inline' https://trusted-cdn.com; 
               style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; 
               img-src 'self' data: https:; 
               font-src 'self' https://fonts.gstatic.com; 
               connect-src 'self' https://api.example.com; 
               frame-src 'none'; 
               object-src 'none'; 
               base-uri 'self'; 
               form-action 'self';">

<!-- Better: CSP via HTTP header (server-side) -->
<!-- Content-Security-Policy: default-src 'self'; script-src 'self' 'nonce-abc123'; style-src 'self' 'nonce-def456' -->

<!-- Using nonces for inline scripts -->
<script nonce="abc123">
  // Inline script with nonce
  console.log('This script is allowed by CSP');
</script>

<!-- Using nonces for inline styles -->
<style nonce="def456">
  /* Inline styles with nonce */
  .secure-style { color: blue; }
</style>
```

**2. Input Validation and Sanitization:**
```html
<!-- Secure form inputs -->
<form id="secure-form">
  <!-- Input validation -->
  <label for="username">Username:</label>
  <input type="text" 
         id="username" 
         name="username" 
         pattern="[a-zA-Z0-9_]{3,20}" 
         maxlength="20" 
         required 
         autocomplete="username">
  
  <!-- Email validation -->
  <label for="email">Email:</label>
  <input type="email" 
         id="email" 
         name="email" 
         maxlength="254" 
         required 
         autocomplete="email">
  
  <!-- Password with requirements -->
  <label for="password">Password:</label>
  <input type="password" 
         id="password" 
         name="password" 
         minlength="8" 
         maxlength="128" 
         pattern="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$" 
         required 
         autocomplete="new-password">
  
  <!-- URL validation -->
  <label for="website">Website:</label>
  <input type="url" 
         id="website" 
         name="website" 
         maxlength="2048">
  
  <!-- Number validation -->
  <label for="age">Age:</label>
  <input type="number" 
         id="age" 
         name="age" 
         min="13" 
         max="120" 
         required>
  
  <!-- File upload with restrictions -->
  <label for="avatar">Avatar:</label>
  <input type="file" 
         id="avatar" 
         name="avatar" 
         accept="image/jpeg,image/png,image/webp" 
         maxlength="5242880"> <!-- 5MB -->
  
  <button type="submit">Submit</button>
</form>

<script>
// Client-side validation and sanitization
class SecureForm {
  constructor(formElement) {
    this.form = formElement;
    this.init();
  }
  
  init() {
    this.form.addEventListener('submit', this.handleSubmit.bind(this));
    
    // Real-time validation
    this.form.querySelectorAll('input').forEach(input => {
      input.addEventListener('input', this.validateInput.bind(this));
    });
  }
  
  handleSubmit(event) {
    event.preventDefault();
    
    if (this.validateForm()) {
      const formData = this.sanitizeFormData();
      this.submitSecurely(formData);
    }
  }
  
  validateForm() {
    let isValid = true;
    const inputs = this.form.querySelectorAll('input[required]');
    
    inputs.forEach(input => {
      if (!this.validateInput({ target: input })) {
        isValid = false;
      }
    });
    
    return isValid;
  }
  
  validateInput(event) {
    const input = event.target;
    const value = input.value;
    let isValid = true;
    let errorMessage = '';
    
    // Basic validation
    if (input.required && !value.trim()) {
      isValid = false;
      errorMessage = 'This field is required';
    } else if (input.pattern && !new RegExp(input.pattern).test(value)) {
      isValid = false;
      errorMessage = 'Invalid format';
    } else if (input.type === 'email' && !this.isValidEmail(value)) {
      isValid = false;
      errorMessage = 'Invalid email address';
    } else if (input.type === 'url' && value && !this.isValidURL(value)) {
      isValid = false;
      errorMessage = 'Invalid URL';
    }
    
    // Custom validation
    switch (input.name) {
      case 'username':
        if (value && !this.isValidUsername(value)) {
          isValid = false;
          errorMessage = 'Username can only contain letters, numbers, and underscores';
        }
        break;
      case 'password':
        if (value && !this.isStrongPassword(value)) {
          isValid = false;
          errorMessage = 'Password must contain at least 8 characters with uppercase, lowercase, number, and special character';
        }
        break;
    }
    
    this.showValidationMessage(input, isValid, errorMessage);
    return isValid;
  }
  
  sanitizeFormData() {
    const formData = new FormData(this.form);
    const sanitizedData = {};
    
    for (const [key, value] of formData.entries()) {
      if (typeof value === 'string') {
        // Basic HTML sanitization
        sanitizedData[key] = this.sanitizeHTML(value);
      } else {
        sanitizedData[key] = value;
      }
    }
    
    return sanitizedData;
  }
  
  sanitizeHTML(str) {
    const div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
  }
  
  isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }
  
  isValidURL(url) {
    try {
      new URL(url);
      return true;
    } catch {
      return false;
    }
  }
  
  isValidUsername(username) {
    const usernameRegex = /^[a-zA-Z0-9_]{3,20}$/;
    return usernameRegex.test(username);
  }
  
  isStrongPassword(password) {
    const strongPasswordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    return strongPasswordRegex.test(password);
  }
  
  showValidationMessage(input, isValid, message) {
    const errorElement = input.parentNode.querySelector('.error-message') || 
                        this.createErrorElement(input);
    
    if (isValid) {
      errorElement.textContent = '';
      errorElement.style.display = 'none';
      input.classList.remove('invalid');
    } else {
      errorElement.textContent = message;
      errorElement.style.display = 'block';
      input.classList.add('invalid');
    }
  }
  
  createErrorElement(input) {
    const errorElement = document.createElement('div');
    errorElement.className = 'error-message';
    errorElement.style.color = 'red';
    errorElement.style.fontSize = '0.875rem';
    input.parentNode.appendChild(errorElement);
    return errorElement;
  }
  
  async submitSecurely(data) {
    try {
      const response = await fetch('/api/submit', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-Requested-With': 'XMLHttpRequest', // CSRF protection
          'X-CSRF-Token': this.getCSRFToken()
        },
        body: JSON.stringify(data)
      });
      
      if (response.ok) {
        const result = await response.json();
        console.log('Form submitted successfully:', result);
      } else {
        throw new Error('Submission failed');
      }
    } catch (error) {
      console.error('Submission error:', error);
    }
  }
  
  getCSRFToken() {
    return document.querySelector('meta[name="csrf-token"]')?.getAttribute('content');
  }
}

// Initialize secure form
const secureForm = new SecureForm(document.getElementById('secure-form'));
</script>
```

**3. Secure Headers and Meta Tags:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- Security headers via meta tags -->
  <meta http-equiv="X-Content-Type-Options" content="nosniff">
  <meta http-equiv="X-Frame-Options" content="DENY">
  <meta http-equiv="X-XSS-Protection" content="1; mode=block">
  <meta http-equiv="Referrer-Policy" content="strict-origin-when-cross-origin">
  
  <!-- CSRF token -->
  <meta name="csrf-token" content="abc123def456">
  
  <!-- Permissions Policy -->
  <meta http-equiv="Permissions-Policy" 
        content="geolocation=(), microphone=(), camera=()">
  
  <title>Secure Page</title>
</head>
<body>
  <!-- Content here -->
  
  <script>
    // Secure JavaScript practices
    
    // Avoid eval and similar functions
    // BAD: eval(userInput);
    // GOOD: Use JSON.parse for data, proper parsing for code
    
    // Secure DOM manipulation
    function securelyUpdateContent(element, content) {
      // Use textContent for plain text
      element.textContent = content;
      
      // Or sanitize HTML if needed
      element.innerHTML = sanitizeHTML(content);
    }
    
    function sanitizeHTML(html) {
      const div = document.createElement('div');
      div.textContent = html;
      return div.innerHTML;
    }
    
    // Secure event handling
    document.addEventListener('click', (event) => {
      // Validate event target
      if (event.target.matches('.safe-button')) {
        handleSafeButtonClick(event);
      }
    });
    
    // Secure AJAX requests
    async function secureAjaxRequest(url, data) {
      try {
        const response = await fetch(url, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRF-Token': getCSRFToken()
          },
          credentials: 'same-origin', // Include cookies for same-origin requests
          body: JSON.stringify(data)
        });
        
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        return await response.json();
      } catch (error) {
        console.error('Request failed:', error);
        throw error;
      }
    }
    
    function getCSRFToken() {
      return document.querySelector('meta[name="csrf-token"]')?.getAttribute('content');
    }
  </script>
</body>
</html>
```

This comprehensive HTML guide now covers fundamental concepts through advanced modern features, providing practical examples for interview preparation and real-world development with a strong focus on security, accessibility, performance, and modern web standards.

---

---

### Q40: What are the latest HTML features and how do you implement modern web standards?

**Difficulty: Advanced**

**Answer:**
Modern HTML includes new elements, attributes, and APIs that enhance functionality, accessibility, and user experience.

**1. Modern HTML Elements and Attributes:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Modern HTML Features</title>
  
  <!-- Modern meta tags -->
  <meta name="theme-color" content="#2196F3">
  <meta name="color-scheme" content="light dark">
  <link rel="manifest" href="/manifest.json">
  
  <!-- Preload critical resources -->
  <link rel="preload" href="/fonts/main.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="/css/critical.css" as="style">
  <link rel="preload" href="/js/main.js" as="script">
  
  <!-- Module preloading -->
  <link rel="modulepreload" href="/js/modules/core.js">
  
  <!-- DNS prefetch for external resources -->
  <link rel="dns-prefetch" href="//fonts.googleapis.com">
  <link rel="preconnect" href="https://api.example.com" crossorigin>
</head>
<body>
  <!-- Modern semantic elements -->
  <header>
    <nav>
      <ul>
        <li><a href="#home" aria-current="page">Home</a></li>
        <li><a href="#about">About</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
    </nav>
  </header>
  
  <main>
    <!-- Search element -->
    <search>
      <form role="search" action="/search" method="get">
        <label for="search-input">Search:</label>
        <input type="search" id="search-input" name="q" 
               placeholder="Search products..." 
               autocomplete="off"
               spellcheck="false"
               enterkeyhint="search">
        <button type="submit">Search</button>
      </form>
    </search>
    
    <!-- Details and summary for collapsible content -->
    <details open>
      <summary>Product Features</summary>
      <ul>
        <li>Feature 1: Advanced functionality</li>
        <li>Feature 2: Enhanced performance</li>
        <li>Feature 3: Better user experience</li>
      </ul>
    </details>
    
    <!-- Dialog element for modals -->
    <dialog id="product-modal" aria-labelledby="modal-title">
      <header>
        <h2 id="modal-title">Product Details</h2>
        <button type="button" onclick="closeModal()" aria-label="Close modal">
          <span aria-hidden="true">&times;</span>
        </button>
      </header>
      <main>
        <p>Detailed product information goes here.</p>
      </main>
      <footer>
        <button type="button" onclick="closeModal()">Close</button>
        <button type="button" class="primary">Add to Cart</button>
      </footer>
    </dialog>
    
    <!-- Modern form elements -->
    <form>
      <!-- Color picker -->
      <label for="theme-color">Choose theme color:</label>
      <input type="color" id="theme-color" name="color" value="#2196F3">
      
      <!-- Date and time inputs -->
      <label for="appointment-date">Appointment date:</label>
      <input type="date" id="appointment-date" name="date" 
             min="2024-01-01" max="2024-12-31">
      
      <label for="appointment-time">Appointment time:</label>
      <input type="time" id="appointment-time" name="time" 
             min="09:00" max="17:00" step="1800">
      
      <!-- Range slider -->
      <label for="price-range">Price range: $<span id="price-value">500</span></label>
      <input type="range" id="price-range" name="price" 
             min="0" max="1000" value="500" step="50"
             oninput="document.getElementById('price-value').textContent = this.value">
      
      <!-- File input with multiple and accept -->
      <label for="product-images">Upload product images:</label>
      <input type="file" id="product-images" name="images" 
             multiple accept="image/*" capture="environment">
      
      <!-- Datalist for autocomplete -->
      <label for="product-category">Product category:</label>
      <input type="text" id="product-category" name="category" 
             list="categories" autocomplete="off">
      <datalist id="categories">
        <option value="Electronics">
        <option value="Clothing">
        <option value="Books">
        <option value="Home & Garden">
        <option value="Sports">
      </datalist>
      
      <!-- Output element for calculations -->
      <label for="quantity">Quantity:</label>
      <input type="number" id="quantity" name="quantity" value="1" min="1" max="10"
             oninput="calculateTotal()">
      
      <label for="price">Price per item:</label>
      <input type="number" id="price" name="price" value="29.99" step="0.01"
             oninput="calculateTotal()">
      
      <label>Total: $<output id="total" for="quantity price">29.99</output></label>
      
      <!-- Progress element -->
      <label for="completion">Task completion:</label>
      <progress id="completion" value="75" max="100">75%</progress>
      
      <!-- Meter element -->
      <label for="disk-usage">Disk usage:</label>
      <meter id="disk-usage" value="0.6" min="0" max="1" 
             low="0.5" high="0.8" optimum="0.3">60%</meter>
    </form>
    
    <!-- Picture element for responsive images -->
    <picture>
      <source media="(min-width: 800px)" 
              srcset="hero-large.webp 1x, hero-large-2x.webp 2x" 
              type="image/webp">
      <source media="(min-width: 400px)" 
              srcset="hero-medium.webp 1x, hero-medium-2x.webp 2x" 
              type="image/webp">
      <source srcset="hero-small.webp 1x, hero-small-2x.webp 2x" 
              type="image/webp">
      <img src="hero-fallback.jpg" 
           alt="Hero image description" 
           loading="lazy" 
           decoding="async"
           width="800" 
           height="400">
    </picture>
    
    <!-- Template element -->
    <template id="product-card-template">
      <article class="product-card">
        <img src="" alt="" loading="lazy">
        <h3></h3>
        <p class="price"></p>
        <button type="button">Add to Cart</button>
      </article>
    </template>
  </main>
  
  <script>
    // Modern JavaScript for HTML features
    
    // Dialog API
    function openModal() {
      const modal = document.getElementById('product-modal');
      modal.showModal();
      
      // Trap focus within modal
      modal.addEventListener('keydown', handleModalKeydown);
    }
    
    function closeModal() {
      const modal = document.getElementById('product-modal');
      modal.close();
      modal.removeEventListener('keydown', handleModalKeydown);
    }
    
    function handleModalKeydown(event) {
      if (event.key === 'Escape') {
        closeModal();
      }
    }
    
    // Form calculations
    function calculateTotal() {
      const quantity = document.getElementById('quantity').value;
      const price = document.getElementById('price').value;
      const total = (quantity * price).toFixed(2);
      document.getElementById('total').value = total;
    }
    
    // Template usage
    function createProductCard(product) {
      const template = document.getElementById('product-card-template');
      const clone = template.content.cloneNode(true);
      
      clone.querySelector('img').src = product.image;
      clone.querySelector('img').alt = product.name;
      clone.querySelector('h3').textContent = product.name;
      clone.querySelector('.price').textContent = `$${product.price}`;
      
      return clone;
    }
    
    // Intersection Observer for lazy loading
    const imageObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const img = entry.target;
          img.src = img.dataset.src;
          img.classList.remove('lazy');
          observer.unobserve(img);
        }
      });
    });
    
    document.querySelectorAll('img[data-src]').forEach(img => {
      imageObserver.observe(img);
    });
  </script>
</body>
</html>
```

**2. Web Components:**
```html
<!-- Custom Elements -->
<script>
  // Define a custom element
  class ProductCard extends HTMLElement {
    constructor() {
      super();
      
      // Create shadow DOM
      this.attachShadow({ mode: 'open' });
      
      // Define template
      this.shadowRoot.innerHTML = `
        <style>
          :host {
            display: block;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 16px;
            margin: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
          }
          
          :host([featured]) {
            border-color: #2196F3;
            box-shadow: 0 4px 8px rgba(33,150,243,0.2);
          }
          
          .image {
            width: 100%;
            height: 200px;
            object-fit: cover;
            border-radius: 4px;
          }
          
          .title {
            font-size: 1.2em;
            font-weight: bold;
            margin: 8px 0;
          }
          
          .price {
            color: #2196F3;
            font-size: 1.1em;
            font-weight: bold;
          }
          
          .button {
            background: #2196F3;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 4px;
            cursor: pointer;
            margin-top: 8px;
          }
          
          .button:hover {
            background: #1976D2;
          }
        </style>
        
        <img class="image" alt="">
        <div class="title"></div>
        <div class="price"></div>
        <button class="button" type="button">Add to Cart</button>
      `;
    }
    
    static get observedAttributes() {
      return ['name', 'price', 'image', 'featured'];
    }
    
    attributeChangedCallback(name, oldValue, newValue) {
      switch (name) {
        case 'name':
          this.shadowRoot.querySelector('.title').textContent = newValue;
          break;
        case 'price':
          this.shadowRoot.querySelector('.price').textContent = `$${newValue}`;
          break;
        case 'image':
          const img = this.shadowRoot.querySelector('.image');
          img.src = newValue;
          img.alt = this.getAttribute('name') || 'Product image';
          break;
      }
    }
    
    connectedCallback() {
      // Set up event listeners
      this.shadowRoot.querySelector('.button').addEventListener('click', () => {
        this.dispatchEvent(new CustomEvent('add-to-cart', {
          detail: {
            name: this.getAttribute('name'),
            price: this.getAttribute('price')
          },
          bubbles: true
        }));
      });
    }
  }
  
  // Register the custom element
  customElements.define('product-card', ProductCard);
  
  // Usage event listener
  document.addEventListener('add-to-cart', (event) => {
    console.log('Product added to cart:', event.detail);
  });
</script>

<!-- Use the custom element -->
<product-card 
  name="Wireless Headphones" 
  price="99.99" 
  image="headphones.jpg"
  featured>
</product-card>

<product-card 
  name="Smartphone" 
  price="599.99" 
  image="phone.jpg">
</product-card>
```

**3. Progressive Web App Features:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PWA Example</title>
  
  <!-- PWA meta tags -->
  <meta name="theme-color" content="#2196F3">
  <meta name="background-color" content="#ffffff">
  <meta name="display" content="standalone">
  <meta name="orientation" content="portrait">
  
  <!-- App manifest -->
  <link rel="manifest" href="/manifest.json">
  
  <!-- iOS specific -->
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="default">
  <meta name="apple-mobile-web-app-title" content="My PWA">
  <link rel="apple-touch-icon" href="/icons/apple-touch-icon.png">
  
  <!-- Service Worker registration -->
  <script>
    if ('serviceWorker' in navigator) {
      window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js')
          .then(registration => {
            console.log('SW registered: ', registration);
          })
          .catch(registrationError => {
            console.log('SW registration failed: ', registrationError);
          });
      });
    }
  </script>
</head>
<body>
  <!-- Install prompt -->
  <div id="install-prompt" style="display: none;">
    <p>Install this app for a better experience!</p>
    <button id="install-button">Install</button>
    <button id="dismiss-button">Dismiss</button>
  </div>
  
  <!-- Offline indicator -->
  <div id="offline-indicator" style="display: none;">
    <p>You're currently offline. Some features may not be available.</p>
  </div>
  
  <main>
    <h1>Progressive Web App</h1>
    <p>This app works offline and can be installed!</p>
    
    <!-- Push notification subscription -->
    <button id="subscribe-notifications">Enable Notifications</button>
  </main>
  
  <script>
    // Install prompt handling
    let deferredPrompt;
    
    window.addEventListener('beforeinstallprompt', (e) => {
      e.preventDefault();
      deferredPrompt = e;
      
      const installPrompt = document.getElementById('install-prompt');
      installPrompt.style.display = 'block';
    });
    
    document.getElementById('install-button').addEventListener('click', () => {
      if (deferredPrompt) {
        deferredPrompt.prompt();
        deferredPrompt.userChoice.then((choiceResult) => {
          if (choiceResult.outcome === 'accepted') {
            console.log('User accepted the install prompt');
          }
          deferredPrompt = null;
          document.getElementById('install-prompt').style.display = 'none';
        });
      }
    });
    
    document.getElementById('dismiss-button').addEventListener('click', () => {
      document.getElementById('install-prompt').style.display = 'none';
    });
    
    // Online/offline detection
    function updateOnlineStatus() {
      const offlineIndicator = document.getElementById('offline-indicator');
      if (navigator.onLine) {
        offlineIndicator.style.display = 'none';
      } else {
        offlineIndicator.style.display = 'block';
      }
    }
    
    window.addEventListener('online', updateOnlineStatus);
    window.addEventListener('offline', updateOnlineStatus);
    updateOnlineStatus();
    
    // Push notifications
    document.getElementById('subscribe-notifications').addEventListener('click', async () => {
      if ('Notification' in window && 'serviceWorker' in navigator) {
        const permission = await Notification.requestPermission();
        
        if (permission === 'granted') {
          const registration = await navigator.serviceWorker.ready;
          const subscription = await registration.pushManager.subscribe({
            userVisibleOnly: true,
            applicationServerKey: 'YOUR_VAPID_PUBLIC_KEY'
          });
          
          // Send subscription to server
          await fetch('/api/subscribe', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(subscription)
          });
          
          console.log('Push notification subscription successful');
        }
      }
    });
  </script>
</body>
</html>
```

**4. Advanced Accessibility Patterns:**
```html
<!-- ARIA Live Regions -->
<div aria-live="polite" aria-atomic="true" id="status-message" class="sr-only"></div>
<div aria-live="assertive" id="error-message" class="sr-only"></div>

<!-- Complex Navigation with ARIA -->
<nav aria-label="Main navigation">
  <ul role="menubar">
    <li role="none">
      <a href="#" role="menuitem" aria-haspopup="true" aria-expanded="false">
        Products
      </a>
      <ul role="menu" aria-label="Products submenu">
        <li role="none">
          <a href="#" role="menuitem">Laptops</a>
        </li>
        <li role="none">
          <a href="#" role="menuitem">Phones</a>
        </li>
      </ul>
    </li>
  </ul>
</nav>

<!-- Accessible Data Table -->
<table role="table" aria-label="Sales data">
  <caption>Quarterly Sales Report 2024</caption>
  <thead>
    <tr>
      <th scope="col" id="quarter">Quarter</th>
      <th scope="col" id="revenue">Revenue</th>
      <th scope="col" id="growth">Growth</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row" headers="quarter">Q1</th>
      <td headers="revenue quarter">$1.2M</td>
      <td headers="growth quarter">+15%</td>
    </tr>
    <tr>
      <th scope="row" headers="quarter">Q2</th>
      <td headers="revenue quarter">$1.4M</td>
      <td headers="growth quarter">+18%</td>
    </tr>
  </tbody>
</table>

<!-- Accessible Form with Error Handling -->
<form novalidate>
  <fieldset>
    <legend>Personal Information</legend>
    
    <div class="form-group">
      <label for="email">Email Address *</label>
      <input type="email" id="email" name="email" 
             required aria-describedby="email-error email-help"
             aria-invalid="false">
      <div id="email-help" class="help-text">
        We'll never share your email with anyone else.
      </div>
      <div id="email-error" class="error-message" aria-live="polite"></div>
    </div>
    
    <div class="form-group">
      <fieldset>
        <legend>Preferred Contact Method</legend>
        <div>
          <input type="radio" id="contact-email" name="contact" value="email">
          <label for="contact-email">Email</label>
        </div>
        <div>
          <input type="radio" id="contact-phone" name="contact" value="phone">
          <label for="contact-phone">Phone</label>
        </div>
      </fieldset>
    </div>
  </fieldset>
  
  <button type="submit" aria-describedby="submit-help">
    Submit Form
  </button>
  <div id="submit-help" class="help-text">
    All required fields must be completed before submission.
  </div>
</form>

<script>
  // Accessible form validation
  function validateForm() {
    const emailInput = document.getElementById('email');
    const emailError = document.getElementById('email-error');
    
    if (!emailInput.validity.valid) {
      emailInput.setAttribute('aria-invalid', 'true');
      emailError.textContent = 'Please enter a valid email address.';
      emailInput.focus();
      return false;
    } else {
      emailInput.setAttribute('aria-invalid', 'false');
      emailError.textContent = '';
    }
    
    return true;
  }
  
  // Announce status updates
  function announceStatus(message, isError = false) {
    const statusElement = isError ? 
      document.getElementById('error-message') : 
      document.getElementById('status-message');
    
    statusElement.textContent = message;
    
    // Clear message after a delay
    setTimeout(() => {
      statusElement.textContent = '';
    }, 5000);
  }
</script>
```

This enhanced HTML guide now includes cutting-edge web standards, modern HTML features, web components, PWA capabilities, and advanced accessibility patterns that represent the current state of web development.

---

---

### Q41: How do you create and implement custom Web Components?

**Difficulty: Expert**

**Answer:**
Web Components provide a way to create reusable, encapsulated HTML elements with custom functionality using native browser APIs.

**1. Custom Elements with Shadow DOM:**
```html
<!-- Custom Button Component -->
<script>
class CustomButton extends HTMLElement {
  constructor() {
    super();
    
    // Create shadow root for encapsulation
    this.attachShadow({ mode: 'open' });
    
    // Define component state
    this.state = {
      loading: false,
      disabled: false,
      variant: 'primary'
    };
    
    this.render();
    this.setupEventListeners();
  }
  
  // Define observed attributes
  static get observedAttributes() {
    return ['variant', 'disabled', 'loading', 'size', 'icon'];
  }
  
  // Lifecycle callback when attributes change
  attributeChangedCallback(name, oldValue, newValue) {
    if (oldValue !== newValue) {
      this.state[name] = newValue;
      this.render();
    }
  }
  
  // Lifecycle callback when element is connected to DOM
  connectedCallback() {
    this.setAttribute('role', 'button');
    this.setAttribute('tabindex', '0');
    
    // Handle accessibility
    if (!this.hasAttribute('aria-label') && !this.textContent.trim()) {
      console.warn('Custom button should have aria-label or text content');
    }
  }
  
  // Lifecycle callback when element is disconnected
  disconnectedCallback() {
    this.removeEventListeners();
  }
  
  render() {
    const { variant, loading, disabled, size, icon } = this.state;
    
    this.shadowRoot.innerHTML = `
      <style>
        :host {
          display: inline-block;
          --primary-color: #007bff;
          --secondary-color: #6c757d;
          --success-color: #28a745;
          --danger-color: #dc3545;
          --warning-color: #ffc107;
          --info-color: #17a2b8;
        }
        
        .btn {
          display: inline-flex;
          align-items: center;
          justify-content: center;
          gap: 0.5rem;
          padding: 0.75rem 1.5rem;
          border: none;
          border-radius: 0.375rem;
          font-family: inherit;
          font-size: 1rem;
          font-weight: 500;
          line-height: 1.5;
          text-decoration: none;
          cursor: pointer;
          transition: all 0.2s ease-in-out;
          position: relative;
          overflow: hidden;
        }
        
        .btn:focus {
          outline: 2px solid var(--primary-color);
          outline-offset: 2px;
        }
        
        .btn:disabled {
          opacity: 0.6;
          cursor: not-allowed;
          pointer-events: none;
        }
        
        /* Variants */
        .btn--primary {
          background-color: var(--primary-color);
          color: white;
        }
        
        .btn--primary:hover:not(:disabled) {
          background-color: #0056b3;
          transform: translateY(-1px);
        }
        
        .btn--secondary {
          background-color: var(--secondary-color);
          color: white;
        }
        
        .btn--outline {
          background-color: transparent;
          color: var(--primary-color);
          border: 2px solid var(--primary-color);
        }
        
        .btn--ghost {
          background-color: transparent;
          color: var(--primary-color);
        }
        
        .btn--ghost:hover:not(:disabled) {
          background-color: rgba(0, 123, 255, 0.1);
        }
        
        /* Sizes */
        .btn--small {
          padding: 0.5rem 1rem;
          font-size: 0.875rem;
        }
        
        .btn--large {
          padding: 1rem 2rem;
          font-size: 1.125rem;
        }
        
        /* Loading state */
        .btn--loading {
          color: transparent;
        }
        
        .spinner {
          position: absolute;
          top: 50%;
          left: 50%;
          transform: translate(-50%, -50%);
          width: 1rem;
          height: 1rem;
          border: 2px solid transparent;
          border-top: 2px solid currentColor;
          border-radius: 50%;
          animation: spin 1s linear infinite;
        }
        
        @keyframes spin {
          to { transform: translate(-50%, -50%) rotate(360deg); }
        }
        
        .icon {
          width: 1em;
          height: 1em;
          fill: currentColor;
        }
        
        /* Ripple effect */
        .ripple {
          position: absolute;
          border-radius: 50%;
          background-color: rgba(255, 255, 255, 0.6);
          transform: scale(0);
          animation: ripple 0.6s linear;
          pointer-events: none;
        }
        
        @keyframes ripple {
          to {
            transform: scale(4);
            opacity: 0;
          }
        }
      </style>
      
      <button 
        class="btn btn--${variant} ${size ? `btn--${size}` : ''} ${loading === 'true' ? 'btn--loading' : ''}"
        ${disabled === 'true' ? 'disabled' : ''}
        aria-label="${this.getAttribute('aria-label') || ''}"
      >
        ${loading === 'true' ? '<div class="spinner"></div>' : ''}
        ${icon ? `<svg class="icon"><use href="#${icon}"></use></svg>` : ''}
        <slot></slot>
      </button>
    `;
  }
  
  setupEventListeners() {
    this.addEventListener('click', this.handleClick.bind(this));
    this.addEventListener('keydown', this.handleKeydown.bind(this));
  }
  
  removeEventListeners() {
    this.removeEventListener('click', this.handleClick);
    this.removeEventListener('keydown', this.handleKeydown);
  }
  
  handleClick(event) {
    if (this.state.disabled === 'true' || this.state.loading === 'true') {
      event.preventDefault();
      return;
    }
    
    // Create ripple effect
    this.createRipple(event);
    
    // Dispatch custom event
    this.dispatchEvent(new CustomEvent('custom-click', {
      detail: { originalEvent: event },
      bubbles: true
    }));
  }
  
  handleKeydown(event) {
    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault();
      this.click();
    }
  }
  
  createRipple(event) {
    const button = this.shadowRoot.querySelector('.btn');
    const rect = button.getBoundingClientRect();
    const size = Math.max(rect.width, rect.height);
    const x = event.clientX - rect.left - size / 2;
    const y = event.clientY - rect.top - size / 2;
    
    const ripple = document.createElement('div');
    ripple.className = 'ripple';
    ripple.style.width = ripple.style.height = size + 'px';
    ripple.style.left = x + 'px';
    ripple.style.top = y + 'px';
    
    button.appendChild(ripple);
    
    setTimeout(() => {
      ripple.remove();
    }, 600);
  }
  
  // Public methods
  setLoading(loading) {
    this.setAttribute('loading', loading);
  }
  
  setDisabled(disabled) {
    this.setAttribute('disabled', disabled);
  }
}

// Register the custom element
customElements.define('custom-button', CustomButton);
</script>

<!-- Usage Examples -->
<custom-button variant="primary">Primary Button</custom-button>
<custom-button variant="secondary" size="large">Large Secondary</custom-button>
<custom-button variant="outline" icon="star">Starred</custom-button>
<custom-button variant="ghost" loading="true">Loading...</custom-button>
<custom-button disabled="true">Disabled</custom-button>
```

**2. Advanced Data Table Component:**
```html
<script>
class DataTable extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
    
    this.state = {
      data: [],
      columns: [],
      sortColumn: null,
      sortDirection: 'asc',
      currentPage: 1,
      pageSize: 10,
      searchTerm: '',
      selectedRows: new Set()
    };
    
    this.render();
  }
  
  static get observedAttributes() {
    return ['data', 'columns', 'page-size', 'searchable', 'sortable', 'selectable'];
  }
  
  attributeChangedCallback(name, oldValue, newValue) {
    switch (name) {
      case 'data':
        try {
          this.state.data = JSON.parse(newValue);
        } catch (e) {
          console.error('Invalid JSON data:', e);
        }
        break;
      case 'columns':
        try {
          this.state.columns = JSON.parse(newValue);
        } catch (e) {
          console.error('Invalid JSON columns:', e);
        }
        break;
      case 'page-size':
        this.state.pageSize = parseInt(newValue) || 10;
        break;
    }
    this.render();
  }
  
  connectedCallback() {
    this.setAttribute('role', 'region');
    this.setAttribute('aria-label', 'Data table');
  }
  
  render() {
    const filteredData = this.getFilteredData();
    const sortedData = this.getSortedData(filteredData);
    const paginatedData = this.getPaginatedData(sortedData);
    const totalPages = Math.ceil(filteredData.length / this.state.pageSize);
    
    this.shadowRoot.innerHTML = `
      <style>
        :host {
          display: block;
          font-family: system-ui, -apple-system, sans-serif;
        }
        
        .table-container {
          border: 1px solid #e0e0e0;
          border-radius: 8px;
          overflow: hidden;
          background: white;
        }
        
        .table-header {
          padding: 1rem;
          background: #f8f9fa;
          border-bottom: 1px solid #e0e0e0;
          display: flex;
          justify-content: space-between;
          align-items: center;
        }
        
        .search-input {
          padding: 0.5rem;
          border: 1px solid #ccc;
          border-radius: 4px;
          font-size: 0.875rem;
        }
        
        .table {
          width: 100%;
          border-collapse: collapse;
        }
        
        .table th,
        .table td {
          padding: 0.75rem;
          text-align: left;
          border-bottom: 1px solid #e0e0e0;
        }
        
        .table th {
          background: #f8f9fa;
          font-weight: 600;
          position: sticky;
          top: 0;
          z-index: 1;
        }
        
        .sortable {
          cursor: pointer;
          user-select: none;
          position: relative;
        }
        
        .sortable:hover {
          background: #e9ecef;
        }
        
        .sort-indicator {
          margin-left: 0.5rem;
          opacity: 0.5;
        }
        
        .sort-indicator.active {
          opacity: 1;
        }
        
        .table tbody tr:hover {
          background: #f8f9fa;
        }
        
        .table tbody tr.selected {
          background: #e3f2fd;
        }
        
        .checkbox {
          margin: 0;
        }
        
        .pagination {
          padding: 1rem;
          display: flex;
          justify-content: space-between;
          align-items: center;
          background: #f8f9fa;
          border-top: 1px solid #e0e0e0;
        }
        
        .pagination-info {
          font-size: 0.875rem;
          color: #6c757d;
        }
        
        .pagination-controls {
          display: flex;
          gap: 0.5rem;
        }
        
        .pagination-btn {
          padding: 0.5rem 0.75rem;
          border: 1px solid #ccc;
          background: white;
          cursor: pointer;
          border-radius: 4px;
          font-size: 0.875rem;
        }
        
        .pagination-btn:hover:not(:disabled) {
          background: #f8f9fa;
        }
        
        .pagination-btn:disabled {
          opacity: 0.5;
          cursor: not-allowed;
        }
        
        .pagination-btn.active {
          background: #007bff;
          color: white;
          border-color: #007bff;
        }
        
        .no-data {
          text-align: center;
          padding: 2rem;
          color: #6c757d;
        }
      </style>
      
      <div class="table-container">
        ${this.hasAttribute('searchable') ? `
          <div class="table-header">
            <h3>Data Table</h3>
            <input 
              type="text" 
              class="search-input" 
              placeholder="Search..."
              value="${this.state.searchTerm}"
            >
          </div>
        ` : ''}
        
        <table class="table" role="table">
          <thead>
            <tr role="row">
              ${this.hasAttribute('selectable') ? '<th><input type="checkbox" class="checkbox select-all"></th>' : ''}
              ${this.state.columns.map(col => `
                <th 
                  role="columnheader"
                  class="${this.hasAttribute('sortable') ? 'sortable' : ''}"
                  data-column="${col.key}"
                  aria-sort="${this.getSortAriaValue(col.key)}"
                >
                  ${col.label}
                  ${this.hasAttribute('sortable') ? `
                    <span class="sort-indicator ${this.state.sortColumn === col.key ? 'active' : ''}">
                      ${this.getSortIcon(col.key)}
                    </span>
                  ` : ''}
                </th>
              `).join('')}
            </tr>
          </thead>
          <tbody>
            ${paginatedData.length > 0 ? paginatedData.map((row, index) => `
              <tr role="row" data-index="${index}" class="${this.state.selectedRows.has(index) ? 'selected' : ''}">
                ${this.hasAttribute('selectable') ? `<td><input type="checkbox" class="checkbox row-select" ${this.state.selectedRows.has(index) ? 'checked' : ''}></td>` : ''}
                ${this.state.columns.map(col => `
                  <td role="gridcell">${this.formatCellValue(row[col.key], col)}</td>
                `).join('')}
              </tr>
            `).join('') : `
              <tr>
                <td colspan="${this.state.columns.length + (this.hasAttribute('selectable') ? 1 : 0)}" class="no-data">
                  No data available
                </td>
              </tr>
            `}
          </tbody>
        </table>
        
        ${filteredData.length > this.state.pageSize ? `
          <div class="pagination">
            <div class="pagination-info">
              Showing ${(this.state.currentPage - 1) * this.state.pageSize + 1} to 
              ${Math.min(this.state.currentPage * this.state.pageSize, filteredData.length)} 
              of ${filteredData.length} entries
            </div>
            <div class="pagination-controls">
              <button class="pagination-btn" ${this.state.currentPage === 1 ? 'disabled' : ''} data-page="prev">
                Previous
              </button>
              ${this.getPaginationNumbers(totalPages).map(page => `
                <button 
                  class="pagination-btn ${page === this.state.currentPage ? 'active' : ''}"
                  data-page="${page}"
                >
                  ${page}
                </button>
              `).join('')}
              <button class="pagination-btn" ${this.state.currentPage === totalPages ? 'disabled' : ''} data-page="next">
                Next
              </button>
            </div>
          </div>
        ` : ''}
      </div>
    `;
    
    this.setupEventListeners();
  }
  
  setupEventListeners() {
    // Search functionality
    const searchInput = this.shadowRoot.querySelector('.search-input');
    if (searchInput) {
      searchInput.addEventListener('input', (e) => {
        this.state.searchTerm = e.target.value;
        this.state.currentPage = 1;
        this.render();
      });
    }
    
    // Sorting functionality
    this.shadowRoot.querySelectorAll('.sortable').forEach(header => {
      header.addEventListener('click', () => {
        const column = header.dataset.column;
        if (this.state.sortColumn === column) {
          this.state.sortDirection = this.state.sortDirection === 'asc' ? 'desc' : 'asc';
        } else {
          this.state.sortColumn = column;
          this.state.sortDirection = 'asc';
        }
        this.render();
      });
    });
    
    // Selection functionality
    const selectAll = this.shadowRoot.querySelector('.select-all');
    if (selectAll) {
      selectAll.addEventListener('change', (e) => {
        if (e.target.checked) {
          this.state.data.forEach((_, index) => this.state.selectedRows.add(index));
        } else {
          this.state.selectedRows.clear();
        }
        this.render();
        this.dispatchSelectionEvent();
      });
    }
    
    this.shadowRoot.querySelectorAll('.row-select').forEach((checkbox, index) => {
      checkbox.addEventListener('change', (e) => {
        if (e.target.checked) {
          this.state.selectedRows.add(index);
        } else {
          this.state.selectedRows.delete(index);
        }
        this.render();
        this.dispatchSelectionEvent();
      });
    });
    
    // Pagination functionality
    this.shadowRoot.querySelectorAll('[data-page]').forEach(btn => {
      btn.addEventListener('click', () => {
        const page = btn.dataset.page;
        if (page === 'prev') {
          this.state.currentPage = Math.max(1, this.state.currentPage - 1);
        } else if (page === 'next') {
          const totalPages = Math.ceil(this.getFilteredData().length / this.state.pageSize);
          this.state.currentPage = Math.min(totalPages, this.state.currentPage + 1);
        } else {
          this.state.currentPage = parseInt(page);
        }
        this.render();
      });
    });
  }
  
  getFilteredData() {
    if (!this.state.searchTerm) return this.state.data;
    
    return this.state.data.filter(row => 
      this.state.columns.some(col => 
        String(row[col.key]).toLowerCase().includes(this.state.searchTerm.toLowerCase())
      )
    );
  }
  
  getSortedData(data) {
    if (!this.state.sortColumn) return data;
    
    return [...data].sort((a, b) => {
      const aVal = a[this.state.sortColumn];
      const bVal = b[this.state.sortColumn];
      
      if (aVal < bVal) return this.state.sortDirection === 'asc' ? -1 : 1;
      if (aVal > bVal) return this.state.sortDirection === 'asc' ? 1 : -1;
      return 0;
    });
  }
  
  getPaginatedData(data) {
    const start = (this.state.currentPage - 1) * this.state.pageSize;
    const end = start + this.state.pageSize;
    return data.slice(start, end);
  }
  
  getPaginationNumbers(totalPages) {
    const pages = [];
    const current = this.state.currentPage;
    const delta = 2;
    
    for (let i = Math.max(1, current - delta); i <= Math.min(totalPages, current + delta); i++) {
      pages.push(i);
    }
    
    return pages;
  }
  
  getSortIcon(column) {
    if (this.state.sortColumn !== column) return '↕️';
    return this.state.sortDirection === 'asc' ? '↑' : '↓';
  }
  
  getSortAriaValue(column) {
    if (this.state.sortColumn !== column) return 'none';
    return this.state.sortDirection === 'asc' ? 'ascending' : 'descending';
  }
  
  formatCellValue(value, column) {
    if (column.formatter) {
      return column.formatter(value);
    }
    return value;
  }
  
  dispatchSelectionEvent() {
    this.dispatchEvent(new CustomEvent('selection-change', {
      detail: {
        selectedRows: Array.from(this.state.selectedRows),
        selectedData: Array.from(this.state.selectedRows).map(index => this.state.data[index])
      },
      bubbles: true
    }));
  }
  
  // Public API
  setData(data) {
    this.state.data = data;
    this.render();
  }
  
  getSelectedRows() {
    return Array.from(this.state.selectedRows).map(index => this.state.data[index]);
  }
  
  clearSelection() {
    this.state.selectedRows.clear();
    this.render();
  }
}

customElements.define('data-table', DataTable);
</script>

<!-- Usage Example -->
<data-table 
  searchable 
  sortable 
  selectable 
  page-size="5"
  columns='[
    {"key": "name", "label": "Name"},
    {"key": "email", "label": "Email"},
    {"key": "role", "label": "Role"},
    {"key": "status", "label": "Status"}
  ]'
  data='[
    {"name": "John Doe", "email": "john@example.com", "role": "Admin", "status": "Active"},
    {"name": "Jane Smith", "email": "jane@example.com", "role": "User", "status": "Active"},
    {"name": "Bob Johnson", "email": "bob@example.com", "role": "User", "status": "Inactive"}
  ]'
></data-table>
```

---

### Q42: How do you implement advanced Progressive Web App (PWA) features?

**Difficulty: Expert**

**Answer:**
Modern PWAs require sophisticated service workers, offline capabilities, push notifications, and native-like experiences.

**1. Advanced Service Worker with Caching Strategies:**
```html
<!-- manifest.json -->
<script>
// Advanced PWA Manifest
const manifest = {
  "name": "Advanced PWA Application",
  "short_name": "AdvancedPWA",
  "description": "A comprehensive Progressive Web Application",
  "start_url": "/",
  "display": "standalone",
  "orientation": "portrait-primary",
  "theme_color": "#007bff",
  "background_color": "#ffffff",
  "categories": ["productivity", "utilities"],
  "lang": "en",
  "dir": "ltr",
  "scope": "/",
  "icons": [
    {
      "src": "/icons/icon-72x72.png",
      "sizes": "72x72",
      "type": "image/png",
      "purpose": "maskable any"
    },
    {
      "src": "/icons/icon-96x96.png",
      "sizes": "96x96",
      "type": "image/png",
      "purpose": "maskable any"
    },
    {
      "src": "/icons/icon-128x128.png",
      "sizes": "128x128",
      "type": "image/png",
      "purpose": "maskable any"
    },
    {
      "src": "/icons/icon-144x144.png",
      "sizes": "144x144",
      "type": "image/png",
      "purpose": "maskable any"
    },
    {
      "src": "/icons/icon-152x152.png",
      "sizes": "152x152",
      "type": "image/png",
      "purpose": "maskable any"
    },
    {
      "src": "/icons/icon-192x192.png",
      "sizes": "192x192",
      "type": "image/png",
      "purpose": "maskable any"
    },
    {
      "src": "/icons/icon-384x384.png",
      "sizes": "384x384",
      "type": "image/png",
      "purpose": "maskable any"
    },
    {
      "src": "/icons/icon-512x512.png",
      "sizes": "512x512",
      "type": "image/png",
      "purpose": "maskable any"
    }
  ],
  "shortcuts": [
    {
      "name": "New Document",
      "short_name": "New Doc",
      "description": "Create a new document",
      "url": "/new",
      "icons": [{ "src": "/icons/new-doc.png", "sizes": "96x96" }]
    },
    {
      "name": "Dashboard",
      "short_name": "Dashboard",
      "description": "View dashboard",
      "url": "/dashboard",
      "icons": [{ "src": "/icons/dashboard.png", "sizes": "96x96" }]
    }
  ],
  "share_target": {
    "action": "/share",
    "method": "POST",
    "enctype": "multipart/form-data",
    "params": {
      "title": "title",
      "text": "text",
      "url": "url",
      "files": [
        {
          "name": "file",
          "accept": ["image/*", "text/*"]
        }
      ]
    }
  },
  "protocol_handlers": [
    {
      "protocol": "web+pwa",
      "url": "/handle?url=%s"
    }
  ]
};

// Write manifest to file
const manifestBlob = new Blob([JSON.stringify(manifest, null, 2)], {
  type: 'application/json'
});
</script>

<!-- Advanced Service Worker -->
<script>
// sw.js - Advanced Service Worker
const CACHE_NAME = 'advanced-pwa-v1';
const RUNTIME_CACHE = 'runtime-cache-v1';
const OFFLINE_CACHE = 'offline-cache-v1';

// Cache strategies
const CACHE_STRATEGIES = {
  CACHE_FIRST: 'cache-first',
  NETWORK_FIRST: 'network-first',
  STALE_WHILE_REVALIDATE: 'stale-while-revalidate',
  NETWORK_ONLY: 'network-only',
  CACHE_ONLY: 'cache-only'
};

// Route configurations
const ROUTE_CONFIG = [
  {
    pattern: /\.(js|css|woff2?)$/,
    strategy: CACHE_STRATEGIES.CACHE_FIRST,
    cacheName: CACHE_NAME,
    maxAge: 30 * 24 * 60 * 60 * 1000 // 30 days
  },
  {
    pattern: /\.(png|jpg|jpeg|svg|gif|webp)$/,
    strategy: CACHE_STRATEGIES.CACHE_FIRST,
    cacheName: 'images-cache',
    maxAge: 7 * 24 * 60 * 60 * 1000 // 7 days
  },
  {
    pattern: /\/api\//,
    strategy: CACHE_STRATEGIES.NETWORK_FIRST,
    cacheName: 'api-cache',
    maxAge: 5 * 60 * 1000 // 5 minutes
  },
  {
    pattern: /\/(dashboard|profile|settings)/,
    strategy: CACHE_STRATEGIES.STALE_WHILE_REVALIDATE,
    cacheName: RUNTIME_CACHE
  }
];

// Install event
self.addEventListener('install', event => {
  console.log('Service Worker installing...');
  
  event.waitUntil(
    Promise.all([
      // Cache essential resources
      caches.open(CACHE_NAME).then(cache => {
        return cache.addAll([
          '/',
          '/index.html',
          '/styles/main.css',
          '/scripts/main.js',
          '/offline.html'
        ]);
      }),
      // Skip waiting to activate immediately
      self.skipWaiting()
    ])
  );
});

// Activate event
self.addEventListener('activate', event => {
  console.log('Service Worker activating...');
  
  event.waitUntil(
    Promise.all([
      // Clean up old caches
      caches.keys().then(cacheNames => {
        return Promise.all(
          cacheNames
            .filter(cacheName => {
              return cacheName !== CACHE_NAME && 
                     cacheName !== RUNTIME_CACHE && 
                     cacheName !== OFFLINE_CACHE;
            })
            .map(cacheName => caches.delete(cacheName))
        );
      }),
      // Claim all clients
      self.clients.claim()
    ])
  );
});

// Fetch event with advanced caching strategies
self.addEventListener('fetch', event => {
  const { request } = event;
  const url = new URL(request.url);
  
  // Skip non-GET requests
  if (request.method !== 'GET') {
    return;
  }
  
  // Find matching route configuration
  const routeConfig = ROUTE_CONFIG.find(config => 
    config.pattern.test(url.pathname + url.search)
  );
  
  if (routeConfig) {
    event.respondWith(handleRequest(request, routeConfig));
  } else {
    // Default strategy for unmatched routes
    event.respondWith(
      handleRequest(request, {
        strategy: CACHE_STRATEGIES.NETWORK_FIRST,
        cacheName: RUNTIME_CACHE
      })
    );
  }
});

// Advanced request handling
async function handleRequest(request, config) {
  const { strategy, cacheName, maxAge } = config;
  
  switch (strategy) {
    case CACHE_STRATEGIES.CACHE_FIRST:
      return cacheFirst(request, cacheName, maxAge);
    
    case CACHE_STRATEGIES.NETWORK_FIRST:
      return networkFirst(request, cacheName, maxAge);
    
    case CACHE_STRATEGIES.STALE_WHILE_REVALIDATE:
      return staleWhileRevalidate(request, cacheName);
    
    case CACHE_STRATEGIES.NETWORK_ONLY:
      return fetch(request);
    
    case CACHE_STRATEGIES.CACHE_ONLY:
      return caches.match(request);
    
    default:
      return networkFirst(request, cacheName, maxAge);
  }
}

// Cache-first strategy
async function cacheFirst(request, cacheName, maxAge) {
  const cache = await caches.open(cacheName);
  const cachedResponse = await cache.match(request);
  
  if (cachedResponse) {
    // Check if cache is expired
    if (maxAge && isCacheExpired(cachedResponse, maxAge)) {
      // Try to update cache in background
      updateCacheInBackground(request, cache);
    }
    return cachedResponse;
  }
  
  try {
    const networkResponse = await fetch(request);
    if (networkResponse.ok) {
      cache.put(request, networkResponse.clone());
    }
    return networkResponse;
  } catch (error) {
    return getOfflineFallback(request);
  }
}

// Network-first strategy
async function networkFirst(request, cacheName, maxAge) {
  const cache = await caches.open(cacheName);
  
  try {
    const networkResponse = await fetch(request);
    if (networkResponse.ok) {
      cache.put(request, networkResponse.clone());
    }
    return networkResponse;
  } catch (error) {
    const cachedResponse = await cache.match(request);
    if (cachedResponse) {
      return cachedResponse;
    }
    return getOfflineFallback(request);
  }
}

// Stale-while-revalidate strategy
async function staleWhileRevalidate(request, cacheName) {
  const cache = await caches.open(cacheName);
  const cachedResponse = await cache.match(request);
  
  // Update cache in background
  const networkPromise = fetch(request).then(response => {
    if (response.ok) {
      cache.put(request, response.clone());
    }
    return response;
  });
  
  return cachedResponse || networkPromise;
}

// Utility functions
function isCacheExpired(response, maxAge) {
  const dateHeader = response.headers.get('date');
  if (!dateHeader) return false;
  
  const cacheDate = new Date(dateHeader);
  const now = new Date();
  return (now.getTime() - cacheDate.getTime()) > maxAge;
}

async function updateCacheInBackground(request, cache) {
  try {
    const response = await fetch(request);
    if (response.ok) {
      cache.put(request, response);
    }
  } catch (error) {
    console.log('Background cache update failed:', error);
  }
}

async function getOfflineFallback(request) {
  const url = new URL(request.url);
  
  if (request.destination === 'document') {
    return caches.match('/offline.html');
  }
  
  if (request.destination === 'image') {
    return caches.match('/images/offline-image.svg');
  }
  
  return new Response('Offline', {
    status: 503,
    statusText: 'Service Unavailable'
  });
}

// Background sync
self.addEventListener('sync', event => {
  if (event.tag === 'background-sync') {
    event.waitUntil(doBackgroundSync());
  }
});

async function doBackgroundSync() {
  // Implement background sync logic
  console.log('Performing background sync...');
}

// Push notifications
self.addEventListener('push', event => {
  const options = {
    body: event.data ? event.data.text() : 'New notification',
    icon: '/icons/icon-192x192.png',
    badge: '/icons/badge-72x72.png',
    vibrate: [100, 50, 100],
    data: {
      dateOfArrival: Date.now(),
      primaryKey: 1
    },
    actions: [
      {
        action: 'explore',
        title: 'Explore',
        icon: '/icons/checkmark.png'
      },
      {
        action: 'close',
        title: 'Close',
        icon: '/icons/xmark.png'
      }
    ]
  };
  
  event.waitUntil(
    self.registration.showNotification('PWA Notification', options)
  );
});

// Notification click handling
self.addEventListener('notificationclick', event => {
  event.notification.close();
  
  if (event.action === 'explore') {
    event.waitUntil(
      clients.openWindow('/explore')
    );
  } else if (event.action === 'close') {
    // Just close the notification
  } else {
    // Default action
    event.waitUntil(
      clients.openWindow('/')
    );
  }
});
</script>

<!-- PWA Installation and Management -->
<script>
class PWAManager {
  constructor() {
    this.deferredPrompt = null;
    this.isInstalled = false;
    this.registration = null;
    
    this.init();
  }
  
  async init() {
    // Register service worker
    if ('serviceWorker' in navigator) {
      try {
        this.registration = await navigator.serviceWorker.register('/sw.js');
        console.log('Service Worker registered:', this.registration);
        
        // Listen for updates
        this.registration.addEventListener('updatefound', () => {
          this.handleServiceWorkerUpdate();
        });
      } catch (error) {
        console.error('Service Worker registration failed:', error);
      }
    }
    
    // Handle install prompt
    window.addEventListener('beforeinstallprompt', (e) => {
      e.preventDefault();
      this.deferredPrompt = e;
      this.showInstallButton();
    });
    
    // Check if already installed
    window.addEventListener('appinstalled', () => {
      this.isInstalled = true;
      this.hideInstallButton();
      this.trackInstallation();
    });
    
    // Handle online/offline status
    window.addEventListener('online', () => this.handleOnlineStatus(true));
    window.addEventListener('offline', () => this.handleOnlineStatus(false));
    
    // Request notification permission
    this.requestNotificationPermission();
    
    // Setup push notifications
    this.setupPushNotifications();
  }
  
  async installApp() {
    if (!this.deferredPrompt) {
      console.log('Install prompt not available');
      return;
    }
    
    this.deferredPrompt.prompt();
    const { outcome } = await this.deferredPrompt.userChoice;
    
    if (outcome === 'accepted') {
      console.log('User accepted the install prompt');
      this.trackInstallation();
    } else {
      console.log('User dismissed the install prompt');
    }
    
    this.deferredPrompt = null;
  }
  
  showInstallButton() {
    const installButton = document.getElementById('install-button');
    if (installButton) {
      installButton.style.display = 'block';
      installButton.addEventListener('click', () => this.installApp());
    }
  }
  
  hideInstallButton() {
    const installButton = document.getElementById('install-button');
    if (installButton) {
      installButton.style.display = 'none';
    }
  }
  
  handleServiceWorkerUpdate() {
    const newWorker = this.registration.installing;
    
    newWorker.addEventListener('statechange', () => {
      if (newWorker.state === 'installed' && navigator.serviceWorker.controller) {
        this.showUpdateAvailable();
      }
    });
  }
  
  showUpdateAvailable() {
    const updateBanner = document.createElement('div');
    updateBanner.className = 'update-banner';
    updateBanner.innerHTML = `
      <div class="update-content">
        <span>A new version is available!</span>
        <button id="update-button">Update</button>
        <button id="dismiss-update">Dismiss</button>
      </div>
    `;
    
    document.body.appendChild(updateBanner);
    
    document.getElementById('update-button').addEventListener('click', () => {
      this.applyUpdate();
    });
    
    document.getElementById('dismiss-update').addEventListener('click', () => {
      updateBanner.remove();
    });
  }
  
  async applyUpdate() {
    if (this.registration && this.registration.waiting) {
      this.registration.waiting.postMessage({ type: 'SKIP_WAITING' });
      window.location.reload();
    }
  }
  
  handleOnlineStatus(isOnline) {
    const statusIndicator = document.getElementById('connection-status');
    if (statusIndicator) {
      statusIndicator.textContent = isOnline ? 'Online' : 'Offline';
      statusIndicator.className = isOnline ? 'status-online' : 'status-offline';
    }
    
    // Show/hide offline banner
    const offlineBanner = document.getElementById('offline-banner');
    if (offlineBanner) {
      offlineBanner.style.display = isOnline ? 'none' : 'block';
    }
  }
  
  async requestNotificationPermission() {
    if ('Notification' in window) {
      const permission = await Notification.requestPermission();
      console.log('Notification permission:', permission);
      return permission === 'granted';
    }
    return false;
  }
  
  async setupPushNotifications() {
    if (!this.registration || !('PushManager' in window)) {
      console.log('Push notifications not supported');
      return;
    }
    
    try {
      const subscription = await this.registration.pushManager.subscribe({
        userVisibleOnly: true,
        applicationServerKey: this.urlBase64ToUint8Array('YOUR_VAPID_PUBLIC_KEY')
      });
      
      // Send subscription to server
      await this.sendSubscriptionToServer(subscription);
    } catch (error) {
      console.error('Failed to subscribe to push notifications:', error);
    }
  }
  
  urlBase64ToUint8Array(base64String) {
    const padding = '='.repeat((4 - base64String.length % 4) % 4);
    const base64 = (base64String + padding)
      .replace(/-/g, '+')
      .replace(/_/g, '/');
    
    const rawData = window.atob(base64);
    const outputArray = new Uint8Array(rawData.length);
    
    for (let i = 0; i < rawData.length; ++i) {
      outputArray[i] = rawData.charCodeAt(i);
    }
    
    return outputArray;
  }
  
  async sendSubscriptionToServer(subscription) {
    try {
      await fetch('/api/push-subscription', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(subscription)
      });
    } catch (error) {
      console.error('Failed to send subscription to server:', error);
    }
  }
  
  trackInstallation() {
    // Analytics tracking
    if (typeof gtag !== 'undefined') {
      gtag('event', 'pwa_install', {
        event_category: 'PWA',
        event_label: 'App Installed'
      });
    }
  }
  
  // Share API
  async shareContent(data) {
    if (navigator.share) {
      try {
        await navigator.share(data);
        console.log('Content shared successfully');
      } catch (error) {
        console.error('Error sharing content:', error);
        this.fallbackShare(data);
      }
    } else {
      this.fallbackShare(data);
    }
  }
  
  fallbackShare(data) {
    // Implement fallback sharing (copy to clipboard, social media links, etc.)
    if (navigator.clipboard) {
      navigator.clipboard.writeText(data.url || data.text);
      this.showToast('Link copied to clipboard!');
    }
  }
  
  showToast(message) {
    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.textContent = message;
    document.body.appendChild(toast);
    
    setTimeout(() => {
      toast.remove();
    }, 3000);
  }
}

// Initialize PWA Manager
const pwaManager = new PWAManager();

// Export for global use
window.pwaManager = pwaManager;
</script>

<!-- PWA HTML Structure -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Advanced PWA</title>
  
  <!-- PWA Meta Tags -->
  <link rel="manifest" href="/manifest.json">
  <meta name="theme-color" content="#007bff">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="default">
  <meta name="apple-mobile-web-app-title" content="Advanced PWA">
  
  <!-- iOS Icons -->
  <link rel="apple-touch-icon" href="/icons/icon-152x152.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/icons/icon-180x180.png">
  
  <!-- Windows Tiles -->
  <meta name="msapplication-TileImage" content="/icons/icon-144x144.png">
  <meta name="msapplication-TileColor" content="#007bff">
  
  <style>
    .update-banner {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      background: #007bff;
      color: white;
      padding: 1rem;
      z-index: 1000;
      text-align: center;
    }
    
    .update-content {
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 1rem;
    }
    
    .update-content button {
      padding: 0.5rem 1rem;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    
    #update-button {
      background: white;
      color: #007bff;
    }
    
    #dismiss-update {
      background: transparent;
      color: white;
      border: 1px solid white;
    }
    
    .status-online {
      color: green;
    }
    
    .status-offline {
      color: red;
    }
    
    #offline-banner {
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      background: #dc3545;
      color: white;
      padding: 0.5rem;
      text-align: center;
      display: none;
    }
    
    .toast {
      position: fixed;
      bottom: 2rem;
      left: 50%;
      transform: translateX(-50%);
      background: #333;
      color: white;
      padding: 1rem 2rem;
      border-radius: 4px;
      z-index: 1000;
    }
    
    #install-button {
      display: none;
      position: fixed;
      bottom: 2rem;
      right: 2rem;
      background: #007bff;
      color: white;
      border: none;
      padding: 1rem 2rem;
      border-radius: 50px;
      cursor: pointer;
      box-shadow: 0 4px 12px rgba(0, 123, 255, 0.3);
    }
  </style>
</head>
<body>
  <header>
    <h1>Advanced PWA</h1>
    <div id="connection-status" class="status-online">Online</div>
  </header>
  
  <main>
    <section>
      <h2>PWA Features</h2>
      <button onclick="pwaManager.shareContent({title: 'Advanced PWA', text: 'Check out this amazing PWA!', url: window.location.href})">
        Share App
      </button>
    </section>
  </main>
  
  <button id="install-button">Install App</button>
  
  <div id="offline-banner">
    You are currently offline. Some features may not be available.
  </div>
  
  <script src="/js/pwa-manager.js"></script>
</body>
</html>
```

---

---

### Q43: How do you implement advanced HTML5 Web APIs and modern browser features?

**Difficulty: Expert**

**Answer:**
Modern HTML5 applications leverage sophisticated Web APIs for enhanced user experiences, performance optimization, and native-like functionality.

**1. Advanced Intersection Observer and Performance APIs:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Advanced Web APIs Demo</title>
</head>
<body>
  <!-- Lazy loading with advanced intersection observer -->
  <div class="image-container" data-src="/images/hero-large.webp" data-srcset="/images/hero-small.webp 480w, /images/hero-medium.webp 768w, /images/hero-large.webp 1200w">
    <div class="placeholder"></div>
  </div>
  
  <!-- Performance monitoring elements -->
  <div id="performance-metrics"></div>
  
  <script>
    // Advanced Intersection Observer with performance monitoring
    class AdvancedLazyLoader {
      constructor() {
        this.imageObserver = null;
        this.performanceObserver = null;
        this.loadedImages = new Set();
        this.init();
      }
      
      init() {
        this.setupImageObserver();
        this.setupPerformanceObserver();
        this.observeImages();
      }
      
      setupImageObserver() {
        const options = {
          root: null,
          rootMargin: '50px 0px',
          threshold: [0, 0.25, 0.5, 0.75, 1]
        };
        
        this.imageObserver = new IntersectionObserver((entries) => {
          entries.forEach(entry => {
            if (entry.isIntersecting && entry.intersectionRatio > 0.25) {
              this.loadImage(entry.target);
            }
          });
        }, options);
      }
      
      setupPerformanceObserver() {
        if ('PerformanceObserver' in window) {
          this.performanceObserver = new PerformanceObserver((list) => {
            for (const entry of list.getEntries()) {
              if (entry.entryType === 'largest-contentful-paint') {
                this.reportLCP(entry);
              }
              if (entry.entryType === 'layout-shift') {
                this.reportCLS(entry);
              }
              if (entry.entryType === 'first-input') {
                this.reportFID(entry);
              }
            }
          });
          
          this.performanceObserver.observe({
            entryTypes: ['largest-contentful-paint', 'layout-shift', 'first-input']
          });
        }
      }
      
      async loadImage(container) {
        if (this.loadedImages.has(container)) return;
        
        const src = container.dataset.src;
        const srcset = container.dataset.srcset;
        
        if (!src) return;
        
        this.loadedImages.add(container);
        
        try {
          const img = new Image();
          
          // Progressive loading with WebP support
          const supportsWebP = await this.checkWebPSupport();
          const finalSrc = supportsWebP ? src.replace(/\.(jpg|jpeg|png)$/, '.webp') : src;
          
          img.onload = () => {
            const imgElement = document.createElement('img');
            imgElement.src = finalSrc;
            if (srcset) imgElement.srcset = srcset;
            imgElement.alt = container.dataset.alt || '';
            imgElement.loading = 'lazy';
            
            // Smooth transition
            imgElement.style.opacity = '0';
            imgElement.style.transition = 'opacity 0.3s ease-in-out';
            
            container.appendChild(imgElement);
            
            requestAnimationFrame(() => {
              imgElement.style.opacity = '1';
              container.querySelector('.placeholder')?.remove();
            });
            
            this.imageObserver.unobserve(container);
          };
          
          img.onerror = () => {
            console.error('Failed to load image:', finalSrc);
            this.loadedImages.delete(container);
          };
          
          img.src = finalSrc;
          
        } catch (error) {
          console.error('Error loading image:', error);
          this.loadedImages.delete(container);
        }
      }
      
      async checkWebPSupport() {
        return new Promise((resolve) => {
          const webP = new Image();
          webP.onload = webP.onerror = () => {
            resolve(webP.height === 2);
          };
          webP.src = 'data:image/webp;base64,UklGRjoAAABXRUJQVlA4IC4AAACyAgCdASoCAAIALmk0mk0iIiIiIgBoSygABc6WWgAA/veff/0PP8bA//LwYAAA';
        });
      }
      
      observeImages() {
        const imageContainers = document.querySelectorAll('.image-container[data-src]');
        imageContainers.forEach(container => {
          this.imageObserver.observe(container);
        });
      }
      
      reportLCP(entry) {
        console.log('Largest Contentful Paint:', entry.startTime);
        this.sendMetric('lcp', entry.startTime);
      }
      
      reportCLS(entry) {
        if (!entry.hadRecentInput) {
          console.log('Cumulative Layout Shift:', entry.value);
          this.sendMetric('cls', entry.value);
        }
      }
      
      reportFID(entry) {
        console.log('First Input Delay:', entry.processingStart - entry.startTime);
        this.sendMetric('fid', entry.processingStart - entry.startTime);
      }
      
      sendMetric(name, value) {
        // Send to analytics service
        if (typeof gtag !== 'undefined') {
          gtag('event', 'web_vitals', {
            event_category: 'performance',
            event_label: name,
            value: Math.round(value)
          });
        }
      }
    }
    
    // Initialize lazy loader
    const lazyLoader = new AdvancedLazyLoader();
  </script>
</body>
</html>
```

**2. Advanced Web Workers and Background Sync:**
```html
<!-- Main HTML -->
<script>
  // Advanced Web Worker implementation
  class AdvancedWorkerManager {
    constructor() {
      this.workers = new Map();
      this.taskQueue = [];
      this.maxWorkers = navigator.hardwareConcurrency || 4;
      this.init();
    }
    
    init() {
      this.setupBackgroundSync();
      this.setupPeriodicBackgroundSync();
    }
    
    async createWorker(name, script) {
      if (this.workers.has(name)) {
        return this.workers.get(name);
      }
      
      const worker = new Worker(script);
      const workerProxy = {
        worker,
        busy: false,
        postMessage: (data) => {
          return new Promise((resolve, reject) => {
            const id = Math.random().toString(36).substr(2, 9);
            
            const messageHandler = (event) => {
              if (event.data.id === id) {
                worker.removeEventListener('message', messageHandler);
                worker.removeEventListener('error', errorHandler);
                
                if (event.data.error) {
                  reject(new Error(event.data.error));
                } else {
                  resolve(event.data.result);
                }
              }
            };
            
            const errorHandler = (error) => {
              worker.removeEventListener('message', messageHandler);
              worker.removeEventListener('error', errorHandler);
              reject(error);
            };
            
            worker.addEventListener('message', messageHandler);
            worker.addEventListener('error', errorHandler);
            
            worker.postMessage({ id, ...data });
          });
        }
      };
      
      this.workers.set(name, workerProxy);
      return workerProxy;
    }
    
    async executeTask(workerName, script, data) {
      const worker = await this.createWorker(workerName, script);
      
      if (worker.busy) {
        return new Promise((resolve, reject) => {
          this.taskQueue.push({ workerName, script, data, resolve, reject });
        });
      }
      
      worker.busy = true;
      
      try {
        const result = await worker.postMessage(data);
        return result;
      } finally {
        worker.busy = false;
        this.processQueue();
      }
    }
    
    processQueue() {
      if (this.taskQueue.length === 0) return;
      
      const availableWorker = Array.from(this.workers.values())
        .find(worker => !worker.busy);
      
      if (availableWorker) {
        const task = this.taskQueue.shift();
        this.executeTask(task.workerName, task.script, task.data)
          .then(task.resolve)
          .catch(task.reject);
      }
    }
    
    async setupBackgroundSync() {
      if ('serviceWorker' in navigator && 'sync' in window.ServiceWorkerRegistration.prototype) {
        const registration = await navigator.serviceWorker.ready;
        
        // Register background sync
        await registration.sync.register('background-data-sync');
        
        console.log('Background sync registered');
      }
    }
    
    async setupPeriodicBackgroundSync() {
      if ('serviceWorker' in navigator && 'periodicSync' in window.ServiceWorkerRegistration.prototype) {
        const registration = await navigator.serviceWorker.ready;
        
        // Request permission for periodic background sync
        const status = await navigator.permissions.query({ name: 'periodic-background-sync' });
        
        if (status.state === 'granted') {
          await registration.periodicSync.register('periodic-data-update', {
            minInterval: 24 * 60 * 60 * 1000 // 24 hours
          });
          
          console.log('Periodic background sync registered');
        }
      }
    }
  }
  
  // Usage example
  const workerManager = new AdvancedWorkerManager();
  
  // Heavy computation in worker
  async function processLargeDataset(data) {
    const result = await workerManager.executeTask(
      'data-processor',
      '/workers/data-processor.js',
      { action: 'process', data }
    );
    
    return result;
  }
  
  // Image processing in worker
  async function processImage(imageData) {
    const result = await workerManager.executeTask(
      'image-processor',
      '/workers/image-processor.js',
      { action: 'filter', imageData, filter: 'blur' }
    );
    
    return result;
  }
</script>
```

---

---

### Q44: How do you implement advanced HTML5 accessibility and inclusive design patterns?

**Difficulty: Expert**

**Answer:**
Advanced accessibility involves sophisticated ARIA patterns, inclusive design principles, and comprehensive support for assistive technologies.

**1. Advanced ARIA Patterns and Live Regions:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Advanced Accessibility Patterns</title>
  <style>
    /* High contrast mode support */
    @media (prefers-contrast: high) {
      .button {
        border: 2px solid;
      }
    }
    
    /* Reduced motion support */
    @media (prefers-reduced-motion: reduce) {
      * {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
      }
    }
    
    /* Focus management */
    .skip-link {
      position: absolute;
      top: -40px;
      left: 6px;
      background: #000;
      color: #fff;
      padding: 8px;
      text-decoration: none;
      z-index: 1000;
    }
    
    .skip-link:focus {
      top: 6px;
    }
    
    /* Screen reader only content */
    .sr-only {
      position: absolute;
      width: 1px;
      height: 1px;
      padding: 0;
      margin: -1px;
      overflow: hidden;
      clip: rect(0, 0, 0, 0);
      white-space: nowrap;
      border: 0;
    }
  </style>
</head>
<body>
  <!-- Skip navigation -->
  <a href="#main-content" class="skip-link">Skip to main content</a>
  
  <!-- Live regions for dynamic content -->
  <div aria-live="polite" aria-atomic="true" id="status-messages" class="sr-only"></div>
  <div aria-live="assertive" aria-atomic="true" id="error-messages" class="sr-only"></div>
  
  <!-- Advanced combobox with autocomplete -->
  <div class="combobox-container">
    <label for="country-input">Country</label>
    <div class="combobox" role="combobox" aria-expanded="false" aria-haspopup="listbox" aria-owns="country-listbox">
      <input
        type="text"
        id="country-input"
        aria-autocomplete="list"
        aria-describedby="country-help"
        autocomplete="country"
      >
      <button type="button" aria-label="Show countries" tabindex="-1">
        <span aria-hidden="true">▼</span>
      </button>
    </div>
    <div id="country-help" class="help-text">
      Type to search for a country or use arrow keys to browse
    </div>
    <ul id="country-listbox" role="listbox" aria-label="Countries" hidden>
      <!-- Options populated dynamically -->
    </ul>
  </div>
  
  <!-- Advanced data table with sorting and filtering -->
  <div class="table-container">
    <div class="table-controls">
      <label for="table-filter">Filter table:</label>
      <input type="text" id="table-filter" aria-describedby="filter-help">
      <div id="filter-help" class="help-text">
        Filter results by typing. <span id="result-count" aria-live="polite"></span>
      </div>
    </div>
    
    <table role="table" aria-label="Employee data">
      <caption>
        Employee Information
        <span class="sr-only">Use arrow keys to navigate. Press Enter to sort by column.</span>
      </caption>
      <thead>
        <tr role="row">
          <th role="columnheader" aria-sort="none" tabindex="0">
            <button type="button" aria-describedby="name-sort-help">
              Name
              <span aria-hidden="true" class="sort-indicator"></span>
            </button>
            <div id="name-sort-help" class="sr-only">
              Click to sort by name
            </div>
          </th>
          <th role="columnheader" aria-sort="none" tabindex="0">
            <button type="button" aria-describedby="role-sort-help">
              Role
              <span aria-hidden="true" class="sort-indicator"></span>
            </button>
            <div id="role-sort-help" class="sr-only">
              Click to sort by role
            </div>
          </th>
          <th role="columnheader" aria-sort="none" tabindex="0">
            <button type="button" aria-describedby="status-sort-help">
              Status
              <span aria-hidden="true" class="sort-indicator"></span>
            </button>
            <div id="status-sort-help" class="sr-only">
              Click to sort by status
            </div>
          </th>
        </tr>
      </thead>
      <tbody role="rowgroup">
        <!-- Rows populated dynamically -->
      </tbody>
    </table>
  </div>
  
  <!-- Advanced modal dialog -->
  <div id="modal-overlay" class="modal-overlay" hidden>
    <div
      role="dialog"
      aria-modal="true"
      aria-labelledby="modal-title"
      aria-describedby="modal-description"
      class="modal"
    >
      <div class="modal-header">
        <h2 id="modal-title">Confirmation Required</h2>
        <button
          type="button"
          aria-label="Close dialog"
          class="modal-close"
          data-action="close-modal"
        >
          <span aria-hidden="true">×</span>
        </button>
      </div>
      <div class="modal-body">
        <p id="modal-description">
          Are you sure you want to delete this item? This action cannot be undone.
        </p>
      </div>
      <div class="modal-footer">
        <button type="button" data-action="cancel" class="button button-secondary">
          Cancel
        </button>
        <button type="button" data-action="confirm" class="button button-danger">
          Delete
        </button>
      </div>
    </div>
  </div>
  
  <script>
    // Advanced accessibility manager
    class AccessibilityManager {
      constructor() {
        this.focusableElements = 'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])';
        this.init();
      }
      
      init() {
        this.setupKeyboardNavigation();
        this.setupLiveRegions();
        this.setupFocusManagement();
        this.setupScreenReaderSupport();
      }
      
      setupKeyboardNavigation() {
        // Global keyboard event handler
        document.addEventListener('keydown', (event) => {
          // Escape key handling
          if (event.key === 'Escape') {
            this.handleEscape();
          }
          
          // Tab trapping in modals
          if (event.key === 'Tab') {
            this.handleTabTrapping(event);
          }
          
          // Arrow key navigation for custom components
          if (['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'].includes(event.key)) {
            this.handleArrowNavigation(event);
          }
        });
      }
      
      setupLiveRegions() {
        this.statusRegion = document.getElementById('status-messages');
        this.errorRegion = document.getElementById('error-messages');
      }
      
      announceToScreenReader(message, type = 'status') {
        const region = type === 'error' ? this.errorRegion : this.statusRegion;
        
        // Clear previous message
        region.textContent = '';
        
        // Add new message with slight delay to ensure it's announced
        setTimeout(() => {
          region.textContent = message;
        }, 100);
        
        // Clear message after announcement
        setTimeout(() => {
          region.textContent = '';
        }, 5000);
      }
      
      setupFocusManagement() {
        // Focus management for dynamic content
        this.focusStack = [];
        
        // Store focus before opening modal
        document.addEventListener('modal-open', (event) => {
          this.focusStack.push(document.activeElement);
          this.trapFocus(event.detail.modal);
        });
        
        // Restore focus after closing modal
        document.addEventListener('modal-close', () => {
          const previousFocus = this.focusStack.pop();
          if (previousFocus) {
            previousFocus.focus();
          }
        });
      }
      
      trapFocus(container) {
        const focusableElements = container.querySelectorAll(this.focusableElements);
        const firstElement = focusableElements[0];
        const lastElement = focusableElements[focusableElements.length - 1];
        
        // Focus first element
        firstElement?.focus();
        
        // Set up tab trapping
        container.addEventListener('keydown', (event) => {
          if (event.key === 'Tab') {
            if (event.shiftKey) {
              if (document.activeElement === firstElement) {
                event.preventDefault();
                lastElement?.focus();
              }
            } else {
              if (document.activeElement === lastElement) {
                event.preventDefault();
                firstElement?.focus();
              }
            }
          }
        });
      }
      
      handleEscape() {
        // Close any open modals or dropdowns
        const openModal = document.querySelector('[role="dialog"]:not([hidden])');
        if (openModal) {
          this.closeModal(openModal);
        }
        
        const openDropdown = document.querySelector('[aria-expanded="true"]');
        if (openDropdown) {
          this.closeDropdown(openDropdown);
        }
      }
      
      handleTabTrapping(event) {
        const modal = document.querySelector('[role="dialog"]:not([hidden])');
        if (modal) {
          const focusableElements = modal.querySelectorAll(this.focusableElements);
          const firstElement = focusableElements[0];
          const lastElement = focusableElements[focusableElements.length - 1];
          
          if (event.shiftKey) {
            if (document.activeElement === firstElement) {
              event.preventDefault();
              lastElement?.focus();
            }
          } else {
            if (document.activeElement === lastElement) {
              event.preventDefault();
              firstElement?.focus();
            }
          }
        }
      }
      
      setupScreenReaderSupport() {
        // Detect screen reader usage
        this.isScreenReaderActive = this.detectScreenReader();
        
        if (this.isScreenReaderActive) {
          document.body.classList.add('screen-reader-active');
        }
      }
      
      detectScreenReader() {
        // Various methods to detect screen reader
        return (
          navigator.userAgent.includes('NVDA') ||
          navigator.userAgent.includes('JAWS') ||
          navigator.userAgent.includes('VoiceOver') ||
          window.speechSynthesis?.getVoices().length > 0
        );
      }
    }
    
    // Initialize accessibility manager
    const a11yManager = new AccessibilityManager();
  </script>
</body>
</html>
```

---

---

### Q45: How do you implement advanced Web Components with Shadow DOM and modern HTML5 features?

**Answer:**
Web Components provide a way to create reusable, encapsulated HTML elements using native browser APIs. They combine Custom Elements, Shadow DOM, HTML Templates, and ES Modules for powerful component architecture.

**Advanced Web Components Implementation:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Advanced Web Components</title>
    <style>
        /* Global styles */
        :root {
            --primary-color: #007bff;
            --secondary-color: #6c757d;
            --success-color: #28a745;
            --danger-color: #dc3545;
            --warning-color: #ffc107;
            --info-color: #17a2b8;
            --light-color: #f8f9fa;
            --dark-color: #343a40;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 2rem;
            background-color: var(--light-color);
        }
    </style>
</head>
<body>
    <!-- Advanced Card Component -->
    <advanced-card 
        title="Product Card"
        subtitle="Premium Quality"
        image="https://via.placeholder.com/300x200"
        price="$99.99"
        rating="4.5"
        theme="primary">
        <p slot="description">
            This is a high-quality product with excellent features and outstanding performance.
        </p>
        <div slot="actions">
            <button class="btn btn-primary">Add to Cart</button>
            <button class="btn btn-secondary">Wishlist</button>
        </div>
    </advanced-card>
    
    <!-- Advanced Form Component -->
    <advanced-form 
        action="/api/submit"
        method="POST"
        validation="strict"
        auto-save="true">
        <form-field 
            type="text"
            name="fullName"
            label="Full Name"
            required
            pattern="[A-Za-z\s]+"
            error-message="Please enter a valid name">
        </form-field>
        
        <form-field 
            type="email"
            name="email"
            label="Email Address"
            required
            error-message="Please enter a valid email">
        </form-field>
        
        <form-field 
            type="tel"
            name="phone"
            label="Phone Number"
            pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}"
            placeholder="123-456-7890"
            error-message="Please enter phone in format: 123-456-7890">
        </form-field>
        
        <form-field 
            type="select"
            name="country"
            label="Country"
            required
            options='[{"value":"us","label":"United States"},{"value":"ca","label":"Canada"},{"value":"uk","label":"United Kingdom"}]'
            error-message="Please select a country">
        </form-field>
        
        <form-field 
            type="textarea"
            name="message"
            label="Message"
            rows="4"
            maxlength="500"
            error-message="Message is required">
        </form-field>
    </advanced-form>
    
    <!-- Advanced Data Table Component -->
    <data-table 
        endpoint="/api/users"
        sortable="true"
        filterable="true"
        paginated="true"
        page-size="10"
        columns='[
            {"key":"id","label":"ID","sortable":true,"width":"80px"},
            {"key":"name","label":"Name","sortable":true,"filterable":true},
            {"key":"email","label":"Email","sortable":true,"filterable":true},
            {"key":"role","label":"Role","sortable":true,"filterable":true},
            {"key":"status","label":"Status","sortable":true,"type":"badge"},
            {"key":"actions","label":"Actions","type":"actions"}
        ]'>
    </data-table>
    
    <!-- Advanced Modal Component -->
    <advanced-modal 
        id="confirmModal"
        size="medium"
        backdrop="static"
        keyboard="false">
        <div slot="header">
            <h3>Confirm Action</h3>
        </div>
        <div slot="body">
            <p>Are you sure you want to proceed with this action?</p>
        </div>
        <div slot="footer">
            <button class="btn btn-secondary" onclick="closeModal('confirmModal')">Cancel</button>
            <button class="btn btn-danger" onclick="confirmAction()">Confirm</button>
        </div>
    </advanced-modal>
    
    <!-- Advanced Notification System -->
    <notification-system 
        position="top-right"
        auto-dismiss="5000"
        max-notifications="5">
    </notification-system>
    
    <script type="module">
        // Advanced Card Component
        class AdvancedCard extends HTMLElement {
            constructor() {
                super();
                this.attachShadow({ mode: 'open' });
                this.render();
            }
            
            static get observedAttributes() {
                return ['title', 'subtitle', 'image', 'price', 'rating', 'theme'];
            }
            
            attributeChangedCallback(name, oldValue, newValue) {
                if (oldValue !== newValue) {
                    this.render();
                }
            }
            
            render() {
                const title = this.getAttribute('title') || '';
                const subtitle = this.getAttribute('subtitle') || '';
                const image = this.getAttribute('image') || '';
                const price = this.getAttribute('price') || '';
                const rating = parseFloat(this.getAttribute('rating')) || 0;
                const theme = this.getAttribute('theme') || 'primary';
                
                this.shadowRoot.innerHTML = `
                    <style>
                        :host {
                            display: block;
                            margin: 1rem 0;
                            font-family: inherit;
                        }
                        
                        .card {
                            background: white;
                            border-radius: 12px;
                            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                            overflow: hidden;
                            transition: transform 0.2s ease, box-shadow 0.2s ease;
                            max-width: 400px;
                        }
                        
                        .card:hover {
                            transform: translateY(-4px);
                            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
                        }
                        
                        .card-image {
                            width: 100%;
                            height: 200px;
                            object-fit: cover;
                            background: #f0f0f0;
                        }
                        
                        .card-content {
                            padding: 1.5rem;
                        }
                        
                        .card-header {
                            margin-bottom: 1rem;
                        }
                        
                        .card-title {
                            font-size: 1.5rem;
                            font-weight: 600;
                            margin: 0 0 0.5rem 0;
                            color: var(--${theme}-color, #333);
                        }
                        
                        .card-subtitle {
                            font-size: 0.9rem;
                            color: #666;
                            margin: 0;
                        }
                        
                        .card-meta {
                            display: flex;
                            justify-content: space-between;
                            align-items: center;
                            margin: 1rem 0;
                        }
                        
                        .price {
                            font-size: 1.25rem;
                            font-weight: 700;
                            color: var(--success-color);
                        }
                        
                        .rating {
                            display: flex;
                            align-items: center;
                            gap: 0.25rem;
                        }
                        
                        .star {
                            color: #ffc107;
                            font-size: 1rem;
                        }
                        
                        .star.empty {
                            color: #e0e0e0;
                        }
                        
                        .card-description {
                            margin: 1rem 0;
                        }
                        
                        .card-actions {
                            margin-top: 1.5rem;
                        }
                        
                        ::slotted(.btn) {
                            padding: 0.5rem 1rem;
                            border: none;
                            border-radius: 6px;
                            cursor: pointer;
                            font-weight: 500;
                            margin-right: 0.5rem;
                            transition: all 0.2s ease;
                        }
                        
                        ::slotted(.btn-primary) {
                            background: var(--primary-color);
                            color: white;
                        }
                        
                        ::slotted(.btn-secondary) {
                            background: var(--secondary-color);
                            color: white;
                        }
                        
                        ::slotted(.btn:hover) {
                            transform: translateY(-1px);
                            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
                        }
                    </style>
                    
                    <div class="card">
                        ${image ? `<img src="${image}" alt="${title}" class="card-image">` : ''}
                        <div class="card-content">
                            <div class="card-header">
                                <h3 class="card-title">${title}</h3>
                                ${subtitle ? `<p class="card-subtitle">${subtitle}</p>` : ''}
                            </div>
                            
                            <div class="card-meta">
                                ${price ? `<span class="price">${price}</span>` : ''}
                                ${rating > 0 ? `
                                    <div class="rating">
                                        ${this.generateStars(rating)}
                                        <span>(${rating})</span>
                                    </div>
                                ` : ''}
                            </div>
                            
                            <div class="card-description">
                                <slot name="description"></slot>
                            </div>
                            
                            <div class="card-actions">
                                <slot name="actions"></slot>
                            </div>
                        </div>
                    </div>
                `;
            }
            
            generateStars(rating) {
                const fullStars = Math.floor(rating);
                const hasHalfStar = rating % 1 !== 0;
                const emptyStars = 5 - Math.ceil(rating);
                
                let stars = '';
                
                for (let i = 0; i < fullStars; i++) {
                    stars += '<span class="star">★</span>';
                }
                
                if (hasHalfStar) {
                    stars += '<span class="star">☆</span>';
                }
                
                for (let i = 0; i < emptyStars; i++) {
                    stars += '<span class="star empty">☆</span>';
                }
                
                return stars;
            }
        }
        
        // Advanced Form Component
        class AdvancedForm extends HTMLElement {
            constructor() {
                super();
                this.attachShadow({ mode: 'open' });
                this.formData = new Map();
                this.validators = new Map();
                this.render();
                this.setupEventListeners();
            }
            
            static get observedAttributes() {
                return ['action', 'method', 'validation', 'auto-save'];
            }
            
            render() {
                this.shadowRoot.innerHTML = `
                    <style>
                        :host {
                            display: block;
                            margin: 2rem 0;
                        }
                        
                        .form-container {
                            background: white;
                            padding: 2rem;
                            border-radius: 12px;
                            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                            max-width: 600px;
                        }
                        
                        .form-title {
                            font-size: 1.5rem;
                            font-weight: 600;
                            margin-bottom: 1.5rem;
                            color: #333;
                        }
                        
                        .form-actions {
                            margin-top: 2rem;
                            display: flex;
                            gap: 1rem;
                        }
                        
                        .btn {
                            padding: 0.75rem 1.5rem;
                            border: none;
                            border-radius: 6px;
                            cursor: pointer;
                            font-weight: 500;
                            transition: all 0.2s ease;
                        }
                        
                        .btn-primary {
                            background: var(--primary-color);
                            color: white;
                        }
                        
                        .btn-secondary {
                            background: var(--secondary-color);
                            color: white;
                        }
                        
                        .btn:hover {
                            transform: translateY(-1px);
                            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
                        }
                        
                        .btn:disabled {
                            opacity: 0.6;
                            cursor: not-allowed;
                            transform: none;
                            box-shadow: none;
                        }
                        
                        .form-status {
                            margin-top: 1rem;
                            padding: 0.75rem;
                            border-radius: 6px;
                            display: none;
                        }
                        
                        .form-status.success {
                            background: #d4edda;
                            color: #155724;
                            border: 1px solid #c3e6cb;
                        }
                        
                        .form-status.error {
                            background: #f8d7da;
                            color: #721c24;
                            border: 1px solid #f5c6cb;
                        }
                    </style>
                    
                    <div class="form-container">
                        <h2 class="form-title">Contact Form</h2>
                        <form id="advancedForm">
                            <slot></slot>
                            <div class="form-actions">
                                <button type="submit" class="btn btn-primary">Submit</button>
                                <button type="reset" class="btn btn-secondary">Reset</button>
                            </div>
                        </form>
                        <div class="form-status" id="formStatus"></div>
                    </div>
                `;
            }
            
            setupEventListeners() {
                const form = this.shadowRoot.getElementById('advancedForm');
                const statusDiv = this.shadowRoot.getElementById('formStatus');
                
                form.addEventListener('submit', async (e) => {
                    e.preventDefault();
                    
                    if (this.validateForm()) {
                        await this.submitForm();
                    }
                });
                
                form.addEventListener('reset', () => {
                    this.resetForm();
                });
                
                // Auto-save functionality
                if (this.getAttribute('auto-save') === 'true') {
                    form.addEventListener('input', this.debounce(() => {
                        this.autoSave();
                    }, 1000));
                }
            }
            
            validateForm() {
                const fields = this.querySelectorAll('form-field');
                let isValid = true;
                
                fields.forEach(field => {
                    if (!field.validate()) {
                        isValid = false;
                    }
                });
                
                return isValid;
            }
            
            async submitForm() {
                const formData = this.getFormData();
                const action = this.getAttribute('action');
                const method = this.getAttribute('method') || 'POST';
                
                try {
                    const response = await fetch(action, {
                        method,
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify(formData)
                    });
                    
                    if (response.ok) {
                        this.showStatus('Form submitted successfully!', 'success');
                        this.dispatchEvent(new CustomEvent('form-submitted', {
                            detail: { data: formData, response }
                        }));
                    } else {
                        throw new Error('Submission failed');
                    }
                } catch (error) {
                    this.showStatus('Error submitting form. Please try again.', 'error');
                }
            }
            
            getFormData() {
                const fields = this.querySelectorAll('form-field');
                const data = {};
                
                fields.forEach(field => {
                    const name = field.getAttribute('name');
                    const value = field.getValue();
                    if (name && value !== null) {
                        data[name] = value;
                    }
                });
                
                return data;
            }
            
            showStatus(message, type) {
                const statusDiv = this.shadowRoot.getElementById('formStatus');
                statusDiv.textContent = message;
                statusDiv.className = `form-status ${type}`;
                statusDiv.style.display = 'block';
                
                setTimeout(() => {
                    statusDiv.style.display = 'none';
                }, 5000);
            }
            
            autoSave() {
                const data = this.getFormData();
                localStorage.setItem('form-auto-save', JSON.stringify(data));
            }
            
            resetForm() {
                const fields = this.querySelectorAll('form-field');
                fields.forEach(field => field.reset());
                localStorage.removeItem('form-auto-save');
            }
            
            debounce(func, wait) {
                let timeout;
                return function executedFunction(...args) {
                    const later = () => {
                        clearTimeout(timeout);
                        func(...args);
                    };
                    clearTimeout(timeout);
                    timeout = setTimeout(later, wait);
                };
            }
        }
        
        // Form Field Component
        class FormField extends HTMLElement {
            constructor() {
                super();
                this.attachShadow({ mode: 'open' });
                this.render();
                this.setupValidation();
            }
            
            static get observedAttributes() {
                return ['type', 'name', 'label', 'required', 'pattern', 'error-message', 'options'];
            }
            
            render() {
                const type = this.getAttribute('type') || 'text';
                const name = this.getAttribute('name') || '';
                const label = this.getAttribute('label') || '';
                const required = this.hasAttribute('required');
                const placeholder = this.getAttribute('placeholder') || '';
                const pattern = this.getAttribute('pattern') || '';
                const maxlength = this.getAttribute('maxlength') || '';
                const rows = this.getAttribute('rows') || '3';
                const options = this.getAttribute('options') ? JSON.parse(this.getAttribute('options')) : [];
                
                let inputHTML = '';
                
                switch (type) {
                    case 'textarea':
                        inputHTML = `<textarea 
                            id="${name}" 
                            name="${name}" 
                            placeholder="${placeholder}"
                            rows="${rows}"
                            ${maxlength ? `maxlength="${maxlength}"` : ''}
                            ${required ? 'required' : ''}></textarea>`;
                        break;
                    case 'select':
                        inputHTML = `<select id="${name}" name="${name}" ${required ? 'required' : ''}>
                            <option value="">Select ${label}</option>
                            ${options.map(opt => `<option value="${opt.value}">${opt.label}</option>`).join('')}
                        </select>`;
                        break;
                    default:
                        inputHTML = `<input 
                            type="${type}" 
                            id="${name}" 
                            name="${name}" 
                            placeholder="${placeholder}"
                            ${pattern ? `pattern="${pattern}"` : ''}
                            ${maxlength ? `maxlength="${maxlength}"` : ''}
                            ${required ? 'required' : ''}>`;
                }
                
                this.shadowRoot.innerHTML = `
                    <style>
                        :host {
                            display: block;
                            margin-bottom: 1.5rem;
                        }
                        
                        .field-group {
                            display: flex;
                            flex-direction: column;
                        }
                        
                        label {
                            font-weight: 500;
                            margin-bottom: 0.5rem;
                            color: #333;
                        }
                        
                        .required {
                            color: #dc3545;
                        }
                        
                        input, textarea, select {
                            padding: 0.75rem;
                            border: 2px solid #e0e0e0;
                            border-radius: 6px;
                            font-size: 1rem;
                            transition: border-color 0.2s ease, box-shadow 0.2s ease;
                            font-family: inherit;
                        }
                        
                        input:focus, textarea:focus, select:focus {
                            outline: none;
                            border-color: var(--primary-color);
                            box-shadow: 0 0 0 3px rgba(0, 123, 255, 0.1);
                        }
                        
                        input:invalid, textarea:invalid, select:invalid {
                            border-color: var(--danger-color);
                        }
                        
                        .error-message {
                            color: var(--danger-color);
                            font-size: 0.875rem;
                            margin-top: 0.25rem;
                            display: none;
                        }
                        
                        .field-group.error .error-message {
                            display: block;
                        }
                        
                        .field-group.error input,
                        .field-group.error textarea,
                        .field-group.error select {
                            border-color: var(--danger-color);
                        }
                        
                        textarea {
                            resize: vertical;
                            min-height: 100px;
                        }
                        
                        select {
                            cursor: pointer;
                        }
                    </style>
                    
                    <div class="field-group">
                        <label for="${name}">
                            ${label}
                            ${required ? '<span class="required">*</span>' : ''}
                        </label>
                        ${inputHTML}
                        <div class="error-message">${this.getAttribute('error-message') || 'This field is invalid'}</div>
                    </div>
                `;
            }
            
            setupValidation() {
                const input = this.shadowRoot.querySelector('input, textarea, select');
                const fieldGroup = this.shadowRoot.querySelector('.field-group');
                
                if (input) {
                    input.addEventListener('blur', () => {
                        this.validate();
                    });
                    
                    input.addEventListener('input', () => {
                        if (fieldGroup.classList.contains('error')) {
                            this.validate();
                        }
                    });
                }
            }
            
            validate() {
                const input = this.shadowRoot.querySelector('input, textarea, select');
                const fieldGroup = this.shadowRoot.querySelector('.field-group');
                const isValid = input.checkValidity();
                
                if (isValid) {
                    fieldGroup.classList.remove('error');
                } else {
                    fieldGroup.classList.add('error');
                }
                
                return isValid;
            }
            
            getValue() {
                const input = this.shadowRoot.querySelector('input, textarea, select');
                return input ? input.value : null;
            }
            
            setValue(value) {
                const input = this.shadowRoot.querySelector('input, textarea, select');
                if (input) {
                    input.value = value;
                }
            }
            
            reset() {
                const input = this.shadowRoot.querySelector('input, textarea, select');
                const fieldGroup = this.shadowRoot.querySelector('.field-group');
                
                if (input) {
                    input.value = '';
                    fieldGroup.classList.remove('error');
                }
            }
        }
        
        // Register components
        customElements.define('advanced-card', AdvancedCard);
        customElements.define('advanced-form', AdvancedForm);
        customElements.define('form-field', FormField);
        
        // Demo functionality
        window.closeModal = function(modalId) {
            const modal = document.getElementById(modalId);
            if (modal) {
                modal.style.display = 'none';
            }
        };
        
        window.confirmAction = function() {
            alert('Action confirmed!');
            closeModal('confirmModal');
        };
    </script>
</body>
</html>
```

---

---

### Q46: How do you implement Progressive Web App (PWA) features with advanced caching strategies and offline functionality?

**Answer:**
Progressive Web Apps combine the best of web and mobile apps, providing app-like experiences with advanced caching, offline functionality, push notifications, and native device integration.

**Complete PWA Implementation:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Advanced PWA</title>
    
    <!-- PWA Meta Tags -->
    <meta name="description" content="Advanced Progressive Web App with offline capabilities">
    <meta name="theme-color" content="#007bff">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="default">
    <meta name="apple-mobile-web-app-title" content="Advanced PWA">
    <meta name="msapplication-TileColor" content="#007bff">
    <meta name="msapplication-config" content="/browserconfig.xml">
    
    <!-- PWA Icons -->
    <link rel="icon" type="image/png" sizes="32x32" href="/icons/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/icons/favicon-16x16.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/icons/apple-touch-icon.png">
    <link rel="mask-icon" href="/icons/safari-pinned-tab.svg" color="#007bff">
    
    <!-- PWA Manifest -->
    <link rel="manifest" href="/manifest.json">
    
    <!-- Preload Critical Resources -->
    <link rel="preload" href="/fonts/inter-var.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="preload" href="/css/critical.css" as="style">
    <link rel="preload" href="/js/app.js" as="script">
    
    <!-- Critical CSS -->
    <style>
        /* Critical above-the-fold styles */
        :root {
            --primary-color: #007bff;
            --secondary-color: #6c757d;
            --success-color: #28a745;
            --danger-color: #dc3545;
            --warning-color: #ffc107;
            --info-color: #17a2b8;
            --light-color: #f8f9fa;
            --dark-color: #343a40;
            --font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        }
        
        * {
            box-sizing: border-box;
        }
        
        body {
            margin: 0;
            font-family: var(--font-family);
            line-height: 1.6;
            color: #333;
            background-color: #f8f9fa;
        }
        
        .app-header {
            background: var(--primary-color);
            color: white;
            padding: 1rem;
            position: sticky;
            top: 0;
            z-index: 1000;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        .app-title {
            margin: 0;
            font-size: 1.5rem;
            font-weight: 600;
        }
        
        .main-content {
            padding: 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }
        
        .loading {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 200px;
        }
        
        .spinner {
            width: 40px;
            height: 40px;
            border: 4px solid #f3f3f3;
            border-top: 4px solid var(--primary-color);
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .offline-indicator {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            background: var(--warning-color);
            color: #333;
            padding: 0.5rem;
            text-align: center;
            transform: translateY(-100%);
            transition: transform 0.3s ease;
            z-index: 2000;
        }
        
        .offline-indicator.show {
            transform: translateY(0);
        }
        
        .install-prompt {
            position: fixed;
            bottom: 20px;
            left: 20px;
            right: 20px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            padding: 1rem;
            display: none;
            z-index: 1500;
        }
        
        .install-prompt.show {
            display: block;
        }
        
        .btn {
            padding: 0.5rem 1rem;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-weight: 500;
            text-decoration: none;
            display: inline-block;
            transition: all 0.2s ease;
        }
        
        .btn-primary {
            background: var(--primary-color);
            color: white;
        }
        
        .btn-secondary {
            background: var(--secondary-color);
            color: white;
        }
        
        .btn:hover {
            transform: translateY(-1px);
            box-shadow: 0 2px 8px rgba(0,0,0,0.2);
        }
    </style>
</head>
<body>
    <!-- Offline Indicator -->
    <div id="offlineIndicator" class="offline-indicator">
        <span>You're currently offline. Some features may be limited.</span>
    </div>
    
    <!-- App Header -->
    <header class="app-header">
        <h1 class="app-title">Advanced PWA</h1>
        <div class="header-actions">
            <button id="syncBtn" class="btn btn-secondary">Sync Data</button>
            <button id="notificationBtn" class="btn btn-secondary">Enable Notifications</button>
        </div>
    </header>
    
    <!-- Main Content -->
    <main class="main-content">
        <section id="appContent">
            <div class="loading">
                <div class="spinner"></div>
            </div>
        </section>
        
        <!-- Data Display -->
        <section id="dataSection" style="display: none;">
            <h2>Data Management</h2>
            <div id="dataList"></div>
            <button id="addDataBtn" class="btn btn-primary">Add New Item</button>
        </section>
        
        <!-- Sync Status -->
        <section id="syncStatus">
            <h3>Sync Status</h3>
            <div id="syncInfo"></div>
        </section>
    </main>
    
    <!-- Install Prompt -->
    <div id="installPrompt" class="install-prompt">
        <h3>Install App</h3>
        <p>Install this app on your device for a better experience!</p>
        <button id="installBtn" class="btn btn-primary">Install</button>
        <button id="dismissBtn" class="btn btn-secondary">Maybe Later</button>
    </div>
    
    <!-- Service Worker Registration -->
    <script>
        // Service Worker Registration
        if ('serviceWorker' in navigator) {
            window.addEventListener('load', async () => {
                try {
                    const registration = await navigator.serviceWorker.register('/sw.js');
                    console.log('SW registered: ', registration);
                    
                    // Handle service worker updates
                    registration.addEventListener('updatefound', () => {
                        const newWorker = registration.installing;
                        newWorker.addEventListener('statechange', () => {
                            if (newWorker.state === 'installed' && navigator.serviceWorker.controller) {
                                // New content is available
                                showUpdateNotification();
                            }
                        });
                    });
                } catch (error) {
                    console.log('SW registration failed: ', error);
                }
            });
        }
        
        // PWA Install Prompt
        let deferredPrompt;
        const installPrompt = document.getElementById('installPrompt');
        const installBtn = document.getElementById('installBtn');
        const dismissBtn = document.getElementById('dismissBtn');
        
        window.addEventListener('beforeinstallprompt', (e) => {
            e.preventDefault();
            deferredPrompt = e;
            installPrompt.classList.add('show');
        });
        
        installBtn.addEventListener('click', async () => {
            if (deferredPrompt) {
                deferredPrompt.prompt();
                const { outcome } = await deferredPrompt.userChoice;
                console.log(`User response to the install prompt: ${outcome}`);
                deferredPrompt = null;
                installPrompt.classList.remove('show');
            }
        });
        
        dismissBtn.addEventListener('click', () => {
            installPrompt.classList.remove('show');
        });
        
        // Network Status Management
        const offlineIndicator = document.getElementById('offlineIndicator');
        
        function updateOnlineStatus() {
            if (navigator.onLine) {
                offlineIndicator.classList.remove('show');
                syncPendingData();
            } else {
                offlineIndicator.classList.add('show');
            }
        }
        
        window.addEventListener('online', updateOnlineStatus);
        window.addEventListener('offline', updateOnlineStatus);
        
        // Initialize app
        updateOnlineStatus();
        
        // Advanced Data Management with IndexedDB
        class DataManager {
            constructor() {
                this.dbName = 'AdvancedPWADB';
                this.dbVersion = 1;
                this.db = null;
                this.init();
            }
            
            async init() {
                return new Promise((resolve, reject) => {
                    const request = indexedDB.open(this.dbName, this.dbVersion);
                    
                    request.onerror = () => reject(request.error);
                    request.onsuccess = () => {
                        this.db = request.result;
                        resolve(this.db);
                    };
                    
                    request.onupgradeneeded = (event) => {
                        const db = event.target.result;
                        
                        // Create object stores
                        if (!db.objectStoreNames.contains('items')) {
                            const itemStore = db.createObjectStore('items', { keyPath: 'id', autoIncrement: true });
                            itemStore.createIndex('timestamp', 'timestamp', { unique: false });
                            itemStore.createIndex('synced', 'synced', { unique: false });
                        }
                        
                        if (!db.objectStoreNames.contains('syncQueue')) {
                            const syncStore = db.createObjectStore('syncQueue', { keyPath: 'id', autoIncrement: true });
                            syncStore.createIndex('action', 'action', { unique: false });
                            syncStore.createIndex('timestamp', 'timestamp', { unique: false });
                        }
                    };
                });
            }
            
            async addItem(data) {
                const transaction = this.db.transaction(['items', 'syncQueue'], 'readwrite');
                const itemStore = transaction.objectStore('items');
                const syncStore = transaction.objectStore('syncQueue');
                
                const item = {
                    ...data,
                    timestamp: Date.now(),
                    synced: navigator.onLine
                };
                
                const result = await this.promisifyRequest(itemStore.add(item));
                
                // Add to sync queue if offline
                if (!navigator.onLine) {
                    await this.promisifyRequest(syncStore.add({
                        action: 'create',
                        itemId: result,
                        data: item,
                        timestamp: Date.now()
                    }));
                }
                
                return result;
            }
            
            async getItems() {
                const transaction = this.db.transaction(['items'], 'readonly');
                const store = transaction.objectStore('items');
                return this.promisifyRequest(store.getAll());
            }
            
            async syncPendingItems() {
                const transaction = this.db.transaction(['syncQueue'], 'readonly');
                const store = transaction.objectStore('syncQueue');
                const pendingItems = await this.promisifyRequest(store.getAll());
                
                for (const item of pendingItems) {
                    try {
                        await this.syncItem(item);
                        await this.removeSyncItem(item.id);
                    } catch (error) {
                        console.error('Sync failed for item:', item, error);
                    }
                }
            }
            
            async syncItem(syncItem) {
                const response = await fetch('/api/items', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(syncItem.data)
                });
                
                if (!response.ok) {
                    throw new Error('Sync failed');
                }
                
                // Update item as synced
                const transaction = this.db.transaction(['items'], 'readwrite');
                const store = transaction.objectStore('items');
                const item = await this.promisifyRequest(store.get(syncItem.itemId));
                item.synced = true;
                await this.promisifyRequest(store.put(item));
            }
            
            async removeSyncItem(id) {
                const transaction = this.db.transaction(['syncQueue'], 'readwrite');
                const store = transaction.objectStore('syncQueue');
                return this.promisifyRequest(store.delete(id));
            }
            
            promisifyRequest(request) {
                return new Promise((resolve, reject) => {
                    request.onsuccess = () => resolve(request.result);
                    request.onerror = () => reject(request.error);
                });
            }
        }
        
        // Initialize Data Manager
        const dataManager = new DataManager();
        
        // Push Notifications
        class NotificationManager {
            constructor() {
                this.vapidPublicKey = 'YOUR_VAPID_PUBLIC_KEY';
            }
            
            async requestPermission() {
                if (!('Notification' in window)) {
                    console.log('This browser does not support notifications');
                    return false;
                }
                
                const permission = await Notification.requestPermission();
                return permission === 'granted';
            }
            
            async subscribeToPush() {
                if (!('serviceWorker' in navigator) || !('PushManager' in window)) {
                    console.log('Push messaging is not supported');
                    return null;
                }
                
                const registration = await navigator.serviceWorker.ready;
                const subscription = await registration.pushManager.subscribe({
                    userVisibleOnly: true,
                    applicationServerKey: this.urlBase64ToUint8Array(this.vapidPublicKey)
                });
                
                // Send subscription to server
                await fetch('/api/subscribe', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(subscription)
                });
                
                return subscription;
            }
            
            urlBase64ToUint8Array(base64String) {
                const padding = '='.repeat((4 - base64String.length % 4) % 4);
                const base64 = (base64String + padding)
                    .replace(/-/g, '+')
                    .replace(/_/g, '/');
                
                const rawData = window.atob(base64);
                const outputArray = new Uint8Array(rawData.length);
                
                for (let i = 0; i < rawData.length; ++i) {
                    outputArray[i] = rawData.charCodeAt(i);
                }
                return outputArray;
            }
            
            showNotification(title, options) {
                if (Notification.permission === 'granted') {
                    new Notification(title, options);
                }
            }
        }
        
        // Initialize Notification Manager
        const notificationManager = new NotificationManager();
        
        // Event Listeners
        document.getElementById('notificationBtn').addEventListener('click', async () => {
            const granted = await notificationManager.requestPermission();
            if (granted) {
                await notificationManager.subscribeToPush();
                notificationManager.showNotification('Notifications Enabled', {
                    body: 'You will now receive push notifications',
                    icon: '/icons/icon-192x192.png'
                });
            }
        });
        
        document.getElementById('syncBtn').addEventListener('click', async () => {
            await syncPendingData();
        });
        
        document.getElementById('addDataBtn').addEventListener('click', async () => {
            const data = {
                title: `Item ${Date.now()}`,
                description: 'Sample item description',
                category: 'general'
            };
            
            await dataManager.addItem(data);
            await loadData();
        });
        
        // Utility Functions
        async function syncPendingData() {
            if (navigator.onLine) {
                try {
                    await dataManager.syncPendingItems();
                    updateSyncStatus('All data synced successfully');
                } catch (error) {
                    updateSyncStatus('Sync failed: ' + error.message);
                }
            } else {
                updateSyncStatus('Cannot sync while offline');
            }
        }
        
        async function loadData() {
            const items = await dataManager.getItems();
            const dataList = document.getElementById('dataList');
            
            dataList.innerHTML = items.map(item => `
                <div class="data-item" style="padding: 1rem; margin: 0.5rem 0; background: white; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                    <h4>${item.title}</h4>
                    <p>${item.description}</p>
                    <small>Created: ${new Date(item.timestamp).toLocaleString()} | Synced: ${item.synced ? 'Yes' : 'No'}</small>
                </div>
            `).join('');
        }
        
        function updateSyncStatus(message) {
            document.getElementById('syncInfo').textContent = message;
        }
        
        function showUpdateNotification() {
            notificationManager.showNotification('App Updated', {
                body: 'A new version is available. Refresh to update.',
                icon: '/icons/icon-192x192.png',
                actions: [{
                    action: 'refresh',
                    title: 'Refresh Now'
                }]
            });
        }
        
        // Initialize app content
        setTimeout(async () => {
            document.getElementById('appContent').innerHTML = '<h2>Welcome to Advanced PWA</h2><p>This app works offline and provides native app-like experience.</p>';
            document.getElementById('dataSection').style.display = 'block';
            await loadData();
            updateSyncStatus('Ready');
        }, 1000);
    </script>
</body>
</html>
```

**Service Worker (sw.js):**
```javascript
const CACHE_NAME = 'advanced-pwa-v1';
const STATIC_CACHE = 'static-v1';
const DYNAMIC_CACHE = 'dynamic-v1';
const API_CACHE = 'api-v1';

// Files to cache immediately
const STATIC_FILES = [
    '/',
    '/index.html',
    '/css/styles.css',
    '/js/app.js',
    '/icons/icon-192x192.png',
    '/icons/icon-512x512.png',
    '/manifest.json'
];

// API endpoints to cache
const API_ENDPOINTS = [
    '/api/items',
    '/api/user'
];

// Install event - cache static files
self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(STATIC_CACHE)
            .then(cache => cache.addAll(STATIC_FILES))
            .then(() => self.skipWaiting())
    );
});

// Activate event - clean up old caches
self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys()
            .then(cacheNames => {
                return Promise.all(
                    cacheNames
                        .filter(cacheName => {
                            return cacheName !== STATIC_CACHE && 
                                   cacheName !== DYNAMIC_CACHE && 
                                   cacheName !== API_CACHE;
                        })
                        .map(cacheName => caches.delete(cacheName))
                );
            })
            .then(() => self.clients.claim())
    );
});

// Fetch event - implement caching strategies
self.addEventListener('fetch', (event) => {
    const { request } = event;
    const url = new URL(request.url);
    
    // Handle API requests
    if (url.pathname.startsWith('/api/')) {
        event.respondWith(handleApiRequest(request));
        return;
    }
    
    // Handle static files
    if (STATIC_FILES.includes(url.pathname)) {
        event.respondWith(handleStaticRequest(request));
        return;
    }
    
    // Handle other requests
    event.respondWith(handleDynamicRequest(request));
});

// Cache-first strategy for static files
async function handleStaticRequest(request) {
    const cache = await caches.open(STATIC_CACHE);
    const cachedResponse = await cache.match(request);
    
    if (cachedResponse) {
        return cachedResponse;
    }
    
    try {
        const networkResponse = await fetch(request);
        cache.put(request, networkResponse.clone());
        return networkResponse;
    } catch (error) {
        // Return offline fallback if available
        return cache.match('/offline.html');
    }
}

// Network-first strategy for API requests
async function handleApiRequest(request) {
    const cache = await caches.open(API_CACHE);
    
    try {
        const networkResponse = await fetch(request);
        
        // Cache successful GET requests
        if (request.method === 'GET' && networkResponse.ok) {
            cache.put(request, networkResponse.clone());
        }
        
        return networkResponse;
    } catch (error) {
        // Return cached response for GET requests
        if (request.method === 'GET') {
            const cachedResponse = await cache.match(request);
            if (cachedResponse) {
                return cachedResponse;
            }
        }
        
        // Return offline response
        return new Response(
            JSON.stringify({ error: 'Offline', cached: false }),
            {
                status: 503,
                headers: { 'Content-Type': 'application/json' }
            }
        );
    }
}

// Stale-while-revalidate strategy for dynamic content
async function handleDynamicRequest(request) {
    const cache = await caches.open(DYNAMIC_CACHE);
    const cachedResponse = await cache.match(request);
    
    const fetchPromise = fetch(request)
        .then(networkResponse => {
            cache.put(request, networkResponse.clone());
            return networkResponse;
        })
        .catch(() => cachedResponse);
    
    return cachedResponse || fetchPromise;
}

// Background sync
self.addEventListener('sync', (event) => {
    if (event.tag === 'background-sync') {
        event.waitUntil(doBackgroundSync());
    }
});

async function doBackgroundSync() {
    // Implement background sync logic
    console.log('Background sync triggered');
}

// Push notifications
self.addEventListener('push', (event) => {
    const options = {
        body: event.data ? event.data.text() : 'New notification',
        icon: '/icons/icon-192x192.png',
        badge: '/icons/badge-72x72.png',
        vibrate: [100, 50, 100],
        data: {
            dateOfArrival: Date.now(),
            primaryKey: 1
        },
        actions: [
            {
                action: 'explore',
                title: 'Explore',
                icon: '/icons/checkmark.png'
            },
            {
                action: 'close',
                title: 'Close',
                icon: '/icons/xmark.png'
            }
        ]
    };
    
    event.waitUntil(
        self.registration.showNotification('PWA Notification', options)
    );
});

// Notification click handling
self.addEventListener('notificationclick', (event) => {
    event.notification.close();
    
    if (event.action === 'explore') {
        event.waitUntil(
            clients.openWindow('/')
        );
    }
});
```

**PWA Manifest (manifest.json):**
```json
{
    "name": "Advanced Progressive Web App",
    "short_name": "Advanced PWA",
    "description": "A comprehensive PWA with offline capabilities and native features",
    "start_url": "/",
    "display": "standalone",
    "background_color": "#ffffff",
    "theme_color": "#007bff",
    "orientation": "portrait-primary",
    "scope": "/",
    "lang": "en",
    "categories": ["productivity", "utilities"],
    "screenshots": [
        {
            "src": "/screenshots/desktop.png",
            "sizes": "1280x720",
            "type": "image/png",
            "form_factor": "wide"
        },
        {
            "src": "/screenshots/mobile.png",
            "sizes": "750x1334",
            "type": "image/png",
            "form_factor": "narrow"
        }
    ],
    "icons": [
        {
            "src": "/icons/icon-72x72.png",
            "sizes": "72x72",
            "type": "image/png"
        },
        {
            "src": "/icons/icon-96x96.png",
            "sizes": "96x96",
            "type": "image/png"
        },
        {
            "src": "/icons/icon-128x128.png",
            "sizes": "128x128",
            "type": "image/png"
        },
        {
            "src": "/icons/icon-144x144.png",
            "sizes": "144x144",
            "type": "image/png"
        },
        {
            "src": "/icons/icon-152x152.png",
            "sizes": "152x152",
            "type": "image/png"
        },
        {
            "src": "/icons/icon-192x192.png",
            "sizes": "192x192",
            "type": "image/png"
        },
        {
            "src": "/icons/icon-384x384.png",
            "sizes": "384x384",
            "type": "image/png"
        },
        {
            "src": "/icons/icon-512x512.png",
            "sizes": "512x512",
            "type": "image/png"
        },
        {
            "src": "/icons/maskable-icon.png",
            "sizes": "512x512",
            "type": "image/png",
            "purpose": "maskable"
        }
    ],
    "shortcuts": [
        {
            "name": "Add New Item",
            "short_name": "Add Item",
            "description": "Quickly add a new item",
            "url": "/add",
            "icons": [
                {
                    "src": "/icons/add-icon.png",
                    "sizes": "192x192"
                }
            ]
        },
        {
            "name": "View Dashboard",
            "short_name": "Dashboard",
            "description": "View your dashboard",
            "url": "/dashboard",
            "icons": [
                {
                    "src": "/icons/dashboard-icon.png",
                    "sizes": "192x192"
                }
            ]
        }
    ],
    "related_applications": [
        {
            "platform": "play",
            "url": "https://play.google.com/store/apps/details?id=com.example.app",
            "id": "com.example.app"
        }
    ],
    "prefer_related_applications": false
}
```

This comprehensive enhancement adds cutting-edge web components, advanced PWA capabilities, sophisticated caching strategies, push notifications, offline functionality, modern web standards, advanced Web APIs, performance monitoring, accessibility patterns, and inclusive design principles that represent the current state of HTML5 and web development.

---

### Q47: How do you work with HTML5 Canvas API for graphics and animations?

**Answer:**
The HTML5 Canvas API provides a powerful way to draw graphics, create animations, and manipulate images directly in the browser without plugins. It offers a resolution-dependent bitmap canvas that can be used to render graphs, game graphics, art, or other visual images on the fly.

**Basic Canvas Setup:**
```html
<canvas id="myCanvas" width="600" height="400"></canvas>

<script>
  // Get the canvas element
  const canvas = document.getElementById('myCanvas');
  
  // Get the drawing context
  const ctx = canvas.getContext('2d');
  
  // Now you can use ctx to draw on the canvas
</script>
```

**Drawing Basic Shapes:**
```javascript
// Drawing rectangles
ctx.fillStyle = '#3498db';  // Set fill color
ctx.fillRect(50, 50, 100, 75);  // x, y, width, height

ctx.strokeStyle = '#e74c3c';  // Set stroke color
ctx.lineWidth = 5;  // Set line width
ctx.strokeRect(200, 50, 100, 75);  // Outlined rectangle

// Drawing paths (lines, curves)
ctx.beginPath();
ctx.moveTo(50, 200);  // Starting point
ctx.lineTo(200, 200);  // Draw line to point
ctx.lineTo(125, 250);  // Draw another line
ctx.closePath();  // Close the path
ctx.fillStyle = '#2ecc71';
ctx.fill();  // Fill the path

// Drawing circles/arcs
ctx.beginPath();
ctx.arc(350, 200, 50, 0, Math.PI * 2);  // x, y, radius, startAngle, endAngle
ctx.fillStyle = '#9b59b6';
ctx.fill();
```

**Working with Text:**
```javascript
// Drawing text
ctx.font = 'bold 24px Arial';  // Set font style
ctx.fillStyle = '#34495e';
ctx.textAlign = 'center';
ctx.fillText('Hello Canvas!', canvas.width/2, 350);  // text, x, y

// Outlined text
ctx.strokeStyle = '#f39c12';
ctx.lineWidth = 1;
ctx.strokeText('Outlined Text', canvas.width/2, 380);
```

**Creating Basic Animation:**
```javascript
// Animation variables
let x = 0;
let y = 200;
let dx = 2;
let radius = 30;

// Animation function
function animate() {
  // Clear the canvas
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  
  // Draw the circle
  ctx.beginPath();
  ctx.arc(x, y, radius, 0, Math.PI * 2);
  ctx.fillStyle = '#3498db';
  ctx.fill();
  
  // Update position
  x += dx;
  
  // Bounce off walls
  if (x + radius > canvas.width || x - radius < 0) {
    dx = -dx;
  }
  
  // Request next frame
  requestAnimationFrame(animate);
}

// Start animation
animate();
```

**Working with Images:**
```javascript
// Load and draw an image
const img = new Image();
img.src = 'image.jpg';
img.onload = function() {
  // Draw the image once it's loaded
  ctx.drawImage(img, 50, 50);  // Basic: image, x, y
  
  // With sizing: image, x, y, width, height
  ctx.drawImage(img, 200, 50, 150, 100);
  
  // Cropping: image, srcX, srcY, srcW, srcH, destX, destY, destW, destH
  ctx.drawImage(img, 0, 0, 100, 100, 400, 50, 100, 100);
};
```

**Advanced Canvas Techniques:**

**1. Gradients and Patterns:**
```javascript
// Linear gradient
const gradient = ctx.createLinearGradient(0, 0, canvas.width, 0);
gradient.addColorStop(0, '#3498db');
gradient.addColorStop(0.5, '#9b59b6');
gradient.addColorStop(1, '#e74c3c');

ctx.fillStyle = gradient;
ctx.fillRect(50, 50, 500, 100);

// Radial gradient
const radialGradient = ctx.createRadialGradient(300, 250, 20, 300, 250, 100);
radialGradient.addColorStop(0, '#f1c40f');
radialGradient.addColorStop(1, '#e67e22');

ctx.fillStyle = radialGradient;
ctx.beginPath();
ctx.arc(300, 250, 100, 0, Math.PI * 2);
ctx.fill();

// Pattern
const patternImg = new Image();
patternImg.src = 'pattern.png';
patternImg.onload = function() {
  const pattern = ctx.createPattern(patternImg, 'repeat');
  ctx.fillStyle = pattern;
  ctx.fillRect(50, 400, 500, 100);
};
```

**2. Shadows and Transparency:**
```javascript
// Shadows
ctx.shadowColor = 'rgba(0, 0, 0, 0.5)';
ctx.shadowBlur = 10;
ctx.shadowOffsetX = 5;
ctx.shadowOffsetY = 5;

ctx.fillStyle = '#3498db';
ctx.fillRect(100, 100, 200, 100);

// Reset shadows
ctx.shadowColor = 'transparent';

// Transparency
ctx.globalAlpha = 0.5;  // Set global transparency
ctx.fillStyle = '#e74c3c';
ctx.fillRect(150, 150, 200, 100);

// Reset transparency
ctx.globalAlpha = 1.0;
```

**3. Transformations:**
```javascript
// Save the current state
ctx.save();

// Translate (move the origin)
ctx.translate(canvas.width/2, canvas.height/2);

// Rotate (in radians)
ctx.rotate(Math.PI / 4);  // 45 degrees

// Scale
ctx.scale(1.5, 0.5);  // x, y scale factors

// Draw a rectangle at the transformed position
ctx.fillStyle = '#2ecc71';
ctx.fillRect(-50, -50, 100, 100);  // Centered at the transformed origin

// Restore the original state
ctx.restore();
```

**4. Compositing Operations:**
```javascript
// Draw a background shape
ctx.fillStyle = '#3498db';
ctx.fillRect(100, 100, 200, 200);

// Set compositing operation
ctx.globalCompositeOperation = 'source-atop';  // Only draw where both shapes overlap

// Draw another shape with the compositing effect
ctx.fillStyle = '#e74c3c';
ctx.beginPath();
ctx.arc(250, 250, 100, 0, Math.PI * 2);
ctx.fill();

// Reset compositing
ctx.globalCompositeOperation = 'source-over';  // Default
```

**5. Pixel Manipulation:**
```javascript
// Get image data
const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
const data = imageData.data;

// Manipulate pixels (invert colors)
for (let i = 0; i < data.length; i += 4) {
  data[i]     = 255 - data[i];     // red
  data[i + 1] = 255 - data[i + 1]; // green
  data[i + 2] = 255 - data[i + 2]; // blue
  // data[i + 3] is alpha (leave unchanged)
}

// Put the modified image data back
ctx.putImageData(imageData, 0, 0);
```

**6. Advanced Animation with Physics:**
```javascript
// Ball object
class Ball {
  constructor(x, y, radius, color) {
    this.x = x;
    this.y = y;
    this.radius = radius;
    this.color = color;
    this.dx = (Math.random() - 0.5) * 5;
    this.dy = (Math.random() - 0.5) * 5;
    this.gravity = 0.1;
    this.friction = 0.99;
    this.bounce = 0.8;
  }
  
  update() {
    // Apply gravity
    this.dy += this.gravity;
    
    // Update position
    this.x += this.dx;
    this.y += this.dy;
    
    // Bounce off walls
    if (this.x + this.radius > canvas.width || this.x - this.radius < 0) {
      this.dx = -this.dx * this.friction;
    }
    
    // Bounce off floor
    if (this.y + this.radius > canvas.height) {
      this.y = canvas.height - this.radius;
      this.dy = -this.dy * this.bounce;
      this.dx *= this.friction;
    }
  }
  
  draw() {
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
    ctx.fillStyle = this.color;
    ctx.fill();
    ctx.closePath();
  }
}

// Create balls
const balls = [];
for (let i = 0; i < 20; i++) {
  const radius = Math.random() * 20 + 10;
  const x = Math.random() * (canvas.width - radius * 2) + radius;
  const y = Math.random() * (canvas.height - radius * 2) + radius;
  const color = `hsl(${Math.random() * 360}, 50%, 50%)`;
  
  balls.push(new Ball(x, y, radius, color));
}

// Animation loop
function animate() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  
  balls.forEach(ball => {
    ball.update();
    ball.draw();
  });
  
  requestAnimationFrame(animate);
}

animate();
```

**7. Canvas Performance Optimization:**
```javascript
// 1. Use multiple canvases for layering
const backgroundCanvas = document.createElement('canvas');
backgroundCanvas.width = canvas.width;
backgroundCanvas.height = canvas.height;
const bgCtx = backgroundCanvas.getContext('2d');

// Draw static background once
function drawBackground() {
  // Draw complex background
  bgCtx.fillStyle = '#f5f5f5';
  bgCtx.fillRect(0, 0, backgroundCanvas.width, backgroundCanvas.height);
  
  // Draw grid
  bgCtx.strokeStyle = '#ddd';
  bgCtx.lineWidth = 1;
  
  for (let x = 0; x < backgroundCanvas.width; x += 20) {
    bgCtx.beginPath();
    bgCtx.moveTo(x, 0);
    bgCtx.lineTo(x, backgroundCanvas.height);
    bgCtx.stroke();
  }
  
  for (let y = 0; y < backgroundCanvas.height; y += 20) {
    bgCtx.beginPath();
    bgCtx.moveTo(0, y);
    bgCtx.lineTo(backgroundCanvas.width, y);
    bgCtx.stroke();
  }
}

drawBackground();

// In animation loop, draw background once then animated elements
function optimizedAnimate() {
  // Clear main canvas
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  
  // Draw background (just once per frame)
  ctx.drawImage(backgroundCanvas, 0, 0);
  
  // Draw animated elements
  // ...
  
  requestAnimationFrame(optimizedAnimate);
}
```

**8. Responsive Canvas:**
```javascript
function resizeCanvas() {
  // Set canvas dimensions to match window size
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
  
  // Redraw everything after resize
  draw();
}

// Listen for window resize events
window.addEventListener('resize', resizeCanvas);

// Initial setup
resizeCanvas();
```

**9. Canvas Interaction:**
```javascript
// Mouse interaction
let isDrawing = false;
let lastX = 0;
let lastY = 0;

canvas.addEventListener('mousedown', (e) => {
  isDrawing = true;
  [lastX, lastY] = [e.offsetX, e.offsetY];
});

canvas.addEventListener('mousemove', (e) => {
  if (!isDrawing) return;
  
  ctx.beginPath();
  ctx.moveTo(lastX, lastY);
  ctx.lineTo(e.offsetX, e.offsetY);
  ctx.strokeStyle = '#3498db';
  ctx.lineWidth = 5;
  ctx.lineCap = 'round';
  ctx.stroke();
  
  [lastX, lastY] = [e.offsetX, e.offsetY];
});

canvas.addEventListener('mouseup', () => {
  isDrawing = false;
});

canvas.addEventListener('mouseout', () => {
  isDrawing = false;
});

// Touch support
canvas.addEventListener('touchstart', (e) => {
  e.preventDefault();
  const touch = e.touches[0];
  const mouseEvent = new MouseEvent('mousedown', {
    clientX: touch.clientX,
    clientY: touch.clientY
  });
  canvas.dispatchEvent(mouseEvent);
});

canvas.addEventListener('touchmove', (e) => {
  e.preventDefault();
  const touch = e.touches[0];
  const mouseEvent = new MouseEvent('mousemove', {
    clientX: touch.clientX,
    clientY: touch.clientY
  });
  canvas.dispatchEvent(mouseEvent);
});

canvas.addEventListener('touchend', (e) => {
  e.preventDefault();
  const mouseEvent = new MouseEvent('mouseup');
  canvas.dispatchEvent(mouseEvent);
});
```

**10. Canvas with WebGL (3D):**
```javascript
// Get WebGL context instead of 2D
const gl = canvas.getContext('webgl') || canvas.getContext('experimental-webgl');

if (!gl) {
  console.error('WebGL not supported');
} else {
  // Set clear color (RGBA)
  gl.clearColor(0.9, 0.9, 0.9, 1.0);
  
  // Clear the canvas
  gl.clear(gl.COLOR_BUFFER_BIT);
  
  // Create shaders, buffers, etc. for 3D rendering
  // This is just a basic setup - WebGL requires much more code
  
  // Vertex shader program
  const vsSource = `
    attribute vec4 aVertexPosition;
    uniform mat4 uModelViewMatrix;
    uniform mat4 uProjectionMatrix;
    void main() {
      gl_Position = uProjectionMatrix * uModelViewMatrix * aVertexPosition;
    }
  `;
  
  // Fragment shader program
  const fsSource = `
    void main() {
      gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0);
    }
  `;
  
  // Initialize shader program
  const shaderProgram = initShaderProgram(gl, vsSource, fsSource);
  
  // WebGL initialization continues...
}

// Helper function to initialize shader program
function initShaderProgram(gl, vsSource, fsSource) {
  const vertexShader = loadShader(gl, gl.VERTEX_SHADER, vsSource);
  const fragmentShader = loadShader(gl, gl.FRAGMENT_SHADER, fsSource);
  
  // Create the shader program
  const shaderProgram = gl.createProgram();
  gl.attachShader(shaderProgram, vertexShader);
  gl.attachShader(shaderProgram, fragmentShader);
  gl.linkProgram(shaderProgram);
  
  // Check if it linked successfully
  if (!gl.getProgramParameter(shaderProgram, gl.LINK_STATUS)) {
    console.error('Unable to initialize shader program: ' + gl.getProgramInfoLog(shaderProgram));
    return null;
  }
  
  return shaderProgram;
}

function loadShader(gl, type, source) {
  const shader = gl.createShader(type);
  gl.shaderSource(shader, source);
  gl.compileShader(shader);
  
  // Check if compilation was successful
  if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
    console.error('An error occurred compiling the shaders: ' + gl.getShaderInfoLog(shader));
    gl.deleteShader(shader);
    return null;
  }
  
  return shader;
}
```

**Best Practices for Canvas Development:**

1. **Performance Optimization**:
   - Use multiple canvases for layering (static vs. dynamic content)
   - Batch similar drawing operations
   - Use `requestAnimationFrame` instead of `setTimeout` for animations
   - Avoid unnecessary canvas state changes
   - Consider using offscreen canvas for complex calculations

2. **Responsive Design**:
   - Scale canvas dimensions based on device pixel ratio
   - Adjust drawing based on canvas size
   - Handle window resize events appropriately

3. **Accessibility**:
   - Provide alternative content inside the canvas element
   - Add ARIA attributes for screen readers
   - Implement keyboard navigation for interactive canvas elements

4. **Cross-Browser Compatibility**:
   - Test on different browsers and devices
   - Use feature detection
   - Provide fallbacks for unsupported features

5. **Memory Management**:
   - Clean up resources when they're no longer needed
   - Remove event listeners when appropriate
   - Be mindful of large image manipulations

---

### Q48: How do you implement HTML5 Drag and Drop functionality?

**Answer:**
HTML5 Drag and Drop (DnD) API allows users to drag and drop elements within a web application, providing a more intuitive and interactive user experience. It's built into the browser and doesn't require external libraries.

**Basic Implementation:**

```html
<!-- Basic Drag and Drop Example -->
<div id="draggable" draggable="true">Drag me</div>
<div id="dropzone">Drop here</div>

<script>
  // Get elements
  const draggable = document.getElementById('draggable');
  const dropzone = document.getElementById('dropzone');
  
  // Add event listeners for the draggable element
  draggable.addEventListener('dragstart', (e) => {
    // Set data to be transferred
    e.dataTransfer.setData('text/plain', e.target.id);
    
    // Add a class for styling during drag
    e.target.classList.add('dragging');
  });
  
  draggable.addEventListener('dragend', (e) => {
    // Remove the dragging class
    e.target.classList.remove('dragging');
  });
  
  // Add event listeners for the drop zone
  dropzone.addEventListener('dragover', (e) => {
    // Prevent default to allow drop
    e.preventDefault();
    
    // Add a class for styling during dragover
    e.target.classList.add('dragover');
  });
  
  dropzone.addEventListener('dragleave', (e) => {
    // Remove the dragover class
    e.target.classList.remove('dragover');
  });
  
  dropzone.addEventListener('drop', (e) => {
    // Prevent default action
    e.preventDefault();
    
    // Remove the dragover class
    e.target.classList.remove('dragover');
    
    // Get the dragged element's ID from dataTransfer
    const id = e.dataTransfer.getData('text/plain');
    const draggedElement = document.getElementById(id);
    
    // Append the dragged element to the drop zone
    e.target.appendChild(draggedElement);
  });
</script>

<style>
  #draggable {
    width: 100px;
    height: 100px;
    background-color: #3498db;
    color: white;
    padding: 10px;
    cursor: move;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  #dropzone {
    width: 200px;
    height: 200px;
    border: 2px dashed #2c3e50;
    padding: 10px;
    min-height: 120px;
  }
  
  .dragging {
    opacity: 0.5;
  }
  
  .dragover {
    background-color: #ecf0f1;
    border-color: #3498db;
  }
</style>
```

**Key Drag and Drop Events:**

1. **For the draggable element:**
   - `dragstart`: Fired when the drag operation begins
   - `drag`: Fired continuously during the drag operation
   - `dragend`: Fired when the drag operation ends

2. **For the drop target:**
   - `dragenter`: Fired when a dragged element enters the drop target
   - `dragover`: Fired continuously when a dragged element is over the drop target
   - `dragleave`: Fired when a dragged element leaves the drop target
   - `drop`: Fired when an element is dropped on the target

**The DataTransfer Object:**

The `dataTransfer` object is used to hold data during drag and drop operations:

```javascript
// Setting data during dragstart
document.addEventListener('dragstart', (e) => {
  // Set plain text
  e.dataTransfer.setData('text/plain', 'This is text data');
  
  // Set JSON data
  const jsonData = JSON.stringify({ id: 123, name: 'Item' });
  e.dataTransfer.setData('application/json', jsonData);
  
  // Set HTML content
  e.dataTransfer.setData('text/html', '<p>This is <strong>HTML</strong> content</p>');
  
  // Set drag image (custom visual representation)
  const img = new Image();
  img.src = 'custom-drag-image.png';
  e.dataTransfer.setDragImage(img, 10, 10); // image, offsetX, offsetY
  
  // Set allowed effects
  e.dataTransfer.effectAllowed = 'copy'; // 'copy', 'move', 'link', or 'copyMove'
});

// Getting data during drop
document.addEventListener('drop', (e) => {
  // Get plain text
  const text = e.dataTransfer.getData('text/plain');
  
  // Get and parse JSON data
  const jsonData = e.dataTransfer.getData('application/json');
  const parsedData = JSON.parse(jsonData);
  
  // Get HTML content
  const html = e.dataTransfer.getData('text/html');
  
  // Set the drop effect
  e.dataTransfer.dropEffect = 'copy'; // 'copy', 'move', or 'link'
});
```

**Advanced Drag and Drop Implementations:**

**1. Sortable List:**

```html
<ul id="sortable-list">
  <li draggable="true" data-id="1">Item 1</li>
  <li draggable="true" data-id="2">Item 2</li>
  <li draggable="true" data-id="3">Item 3</li>
  <li draggable="true" data-id="4">Item 4</li>
  <li draggable="true" data-id="5">Item 5</li>
</ul>

<script>
  const sortableList = document.getElementById('sortable-list');
  let draggedItem = null;
  
  // Add event listeners to all list items
  sortableList.querySelectorAll('li').forEach(item => {
    // Dragstart event
    item.addEventListener('dragstart', (e) => {
      draggedItem = item;
      setTimeout(() => {
        item.classList.add('dragging');
      }, 0);
      e.dataTransfer.setData('text/plain', item.dataset.id);
    });
    
    // Dragend event
    item.addEventListener('dragend', () => {
      draggedItem.classList.remove('dragging');
      draggedItem = null;
    });
    
    // Dragover event
    item.addEventListener('dragover', (e) => {
      e.preventDefault();
      if (item !== draggedItem) {
        const rect = item.getBoundingClientRect();
        const y = e.clientY - rect.top;
        const height = rect.height;
        
        // Determine if we should insert before or after the hovered item
        if (y < height / 2) {
          sortableList.insertBefore(draggedItem, item);
        } else {
          sortableList.insertBefore(draggedItem, item.nextSibling);
        }
      }
    });
  });
</script>

<style>
  #sortable-list {
    list-style: none;
    padding: 0;
    width: 300px;
  }
  
  #sortable-list li {
    padding: 10px 15px;
    background-color: #f8f9fa;
    border: 1px solid #dee2e6;
    margin-bottom: 5px;
    cursor: move;
    user-select: none;
  }
  
  #sortable-list li.dragging {
    opacity: 0.5;
    background-color: #e9ecef;
  }
</style>
```

**2. File Drag and Drop Upload:**

```html
<div id="file-dropzone" class="file-drop-area">
  <span class="file-msg">Drag & drop files here or click to browse</span>
  <input type="file" class="file-input" multiple>
</div>

<div id="preview-container" class="preview-container"></div>

<script>
  const dropzone = document.getElementById('file-dropzone');
  const fileInput = dropzone.querySelector('.file-input');
  const previewContainer = document.getElementById('preview-container');
  
  // Handle file selection via input
  fileInput.addEventListener('change', handleFiles);
  
  // Handle drag and drop events
  ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    dropzone.addEventListener(eventName, preventDefaults, false);
  });
  
  function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
  }
  
  ['dragenter', 'dragover'].forEach(eventName => {
    dropzone.addEventListener(eventName, highlight, false);
  });
  
  ['dragleave', 'drop'].forEach(eventName => {
    dropzone.addEventListener(eventName, unhighlight, false);
  });
  
  function highlight() {
    dropzone.classList.add('highlight');
  }
  
  function unhighlight() {
    dropzone.classList.remove('highlight');
  }
  
  // Handle dropped files
  dropzone.addEventListener('drop', (e) => {
    const dt = e.dataTransfer;
    const files = dt.files;
    handleFiles({ target: { files } });
  });
  
  function handleFiles(e) {
    const files = [...e.target.files];
    previewContainer.innerHTML = '';
    
    files.forEach(file => {
      // Check if file is an image
      if (file.type.startsWith('image/')) {
        const reader = new FileReader();
        
        reader.onload = (e) => {
          const img = document.createElement('img');
          img.src = e.target.result;
          img.classList.add('preview-image');
          previewContainer.appendChild(img);
        };
        
        reader.readAsDataURL(file);
      } else {
        // For non-image files
        const fileInfo = document.createElement('div');
        fileInfo.classList.add('file-info');
        fileInfo.textContent = `${file.name} (${formatFileSize(file.size)})`;
        previewContainer.appendChild(fileInfo);
      }
      
      // Here you would typically upload the file to a server
      // uploadFile(file);
    });
  }
  
  function formatFileSize(bytes) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
  }
  
  // Simulate click on file input when dropzone is clicked
  dropzone.addEventListener('click', () => {
    fileInput.click();
  });
</script>

<style>
  .file-drop-area {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 450px;
    max-width: 100%;
    padding: 25px;
    border: 2px dashed #d9d9d9;
    border-radius: 3px;
    transition: 0.2s;
    background-color: #f8f8f8;
    text-align: center;
    margin-bottom: 20px;
  }
  
  .file-drop-area.highlight {
    border-color: #3498db;
    background-color: rgba(52, 152, 219, 0.05);
  }
  
  .file-msg {
    font-size: 16px;
    color: #777;
    font-weight: 300;
    white-space: nowrap;
    cursor: pointer;
  }
  
  .file-input {
    position: absolute;
    left: 0;
    top: 0;
    height: 100%;
    width: 100%;
    opacity: 0;
    cursor: pointer;
  }
  
  .preview-container {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 20px;
  }
  
  .preview-image {
    max-width: 100px;
    max-height: 100px;
    border-radius: 4px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.12);
  }
  
  .file-info {
    padding: 8px 12px;
    background-color: #e9ecef;
    border-radius: 4px;
    font-size: 14px;
  }
</style>
```

**3. Drag Between Multiple Containers:**

```html
<div class="container">
  <div class="board">
    <h3>To Do</h3>
    <div class="dropzone" id="todo">
      <div class="card" draggable="true" data-id="task1">Complete project proposal</div>
      <div class="card" draggable="true" data-id="task2">Research competitors</div>
      <div class="card" draggable="true" data-id="task3">Create wireframes</div>
    </div>
  </div>
  
  <div class="board">
    <h3>In Progress</h3>
    <div class="dropzone" id="inprogress"></div>
  </div>
  
  <div class="board">
    <h3>Done</h3>
    <div class="dropzone" id="done"></div>
  </div>
</div>

<script>
  // Get all cards and dropzones
  const cards = document.querySelectorAll('.card');
  const dropzones = document.querySelectorAll('.dropzone');
  let draggedCard = null;
  
  // Add event listeners to cards
  cards.forEach(card => {
    card.addEventListener('dragstart', dragStart);
    card.addEventListener('dragend', dragEnd);
  });
  
  // Add event listeners to dropzones
  dropzones.forEach(dropzone => {
    dropzone.addEventListener('dragover', dragOver);
    dropzone.addEventListener('dragleave', dragLeave);
    dropzone.addEventListener('drop', drop);
  });
  
  function dragStart() {
    draggedCard = this;
    setTimeout(() => {
      this.classList.add('dragging');
    }, 0);
  }
  
  function dragEnd() {
    this.classList.remove('dragging');
    draggedCard = null;
  }
  
  function dragOver(e) {
    e.preventDefault();
    this.classList.add('dragover');
  }
  
  function dragLeave() {
    this.classList.remove('dragover');
  }
  
  function drop() {
    this.classList.remove('dragover');
    this.appendChild(draggedCard);
    
    // Here you would typically update your backend
    updateCardStatus(draggedCard.dataset.id, this.id);
  }
  
  function updateCardStatus(cardId, newStatus) {
    console.log(`Card ${cardId} moved to ${newStatus}`);
    // API call to update status in the backend
    // fetch('/api/tasks/' + cardId, {
    //   method: 'PATCH',
    //   headers: { 'Content-Type': 'application/json' },
    //   body: JSON.stringify({ status: newStatus })
    // });
  }
</script>

<style>
  .container {
    display: flex;
    gap: 20px;
    padding: 20px;
    max-width: 1200px;
    margin: 0 auto;
  }
  
  .board {
    flex: 1;
    background-color: #f1f3f5;
    border-radius: 4px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.12);
    padding: 10px;
  }
  
  .board h3 {
    margin-top: 0;
    padding: 10px;
    text-align: center;
    border-bottom: 1px solid #dee2e6;
  }
  
  .dropzone {
    min-height: 200px;
    padding: 10px;
    transition: background-color 0.2s ease;
  }
  
  .dropzone.dragover {
    background-color: rgba(52, 152, 219, 0.1);
  }
  
  .card {
    background-color: white;
    padding: 15px;
    margin-bottom: 10px;
    border-radius: 4px;
    box-shadow: 0 1px 2px rgba(0,0,0,0.1);
    cursor: move;
    user-select: none;
  }
  
  .card.dragging {
    opacity: 0.5;
    transform: scale(0.95);
  }
</style>
```

**Cross-Browser Compatibility and Accessibility:**

```javascript
// Feature detection for drag and drop
function dragDropSupported() {
  const div = document.createElement('div');
  return ('draggable' in div) || ('ondragstart' in div && 'ondrop' in div);
}

// Add fallback for browsers that don't support drag and drop
if (!dragDropSupported()) {
  // Implement alternative UI (e.g., click to select, then click to place)
  implementFallbackUI();
}

// Accessibility enhancements
function enhanceAccessibility() {
  // Add keyboard support
  const draggables = document.querySelectorAll('[draggable="true"]');
  const dropzones = document.querySelectorAll('.dropzone');
  
  draggables.forEach((item, index) => {
    // Add ARIA attributes
    item.setAttribute('role', 'button');
    item.setAttribute('aria-grabbed', 'false');
    item.setAttribute('tabindex', '0');
    
    // Add keyboard event listeners
    item.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        // Toggle selection
        const isGrabbed = item.getAttribute('aria-grabbed') === 'true';
        
        // Deselect all items first
        draggables.forEach(d => d.setAttribute('aria-grabbed', 'false'));
        
        if (!isGrabbed) {
          item.setAttribute('aria-grabbed', 'true');
          announceToScreenReader(`Item ${index + 1} selected. Use arrow keys to navigate to a drop target and press Enter to drop.`);
        }
      }
      
      // Handle arrow keys for navigation when an item is selected
      if (item.getAttribute('aria-grabbed') === 'true') {
        if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
          e.preventDefault();
          focusNextDropzone(document.activeElement);
        }
      }
    });
  });
  
  dropzones.forEach((zone, index) => {
    zone.setAttribute('role', 'region');
    zone.setAttribute('aria-dropeffect', 'move');
    zone.setAttribute('tabindex', '0');
    
    zone.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        // Find the currently selected draggable
        const selectedItem = document.querySelector('[aria-grabbed="true"]');
        
        if (selectedItem) {
          // Perform the drop
          zone.appendChild(selectedItem);
          selectedItem.setAttribute('aria-grabbed', 'false');
          announceToScreenReader(`Item dropped in zone ${index + 1}.`);
        }
      }
    });
  });
}

function announceToScreenReader(message) {
  const announcer = document.getElementById('a11y-announcer') || createAnnouncer();
  announcer.textContent = message;
}

function createAnnouncer() {
  const announcer = document.createElement('div');
  announcer.id = 'a11y-announcer';
  announcer.setAttribute('aria-live', 'assertive');
  announcer.setAttribute('aria-atomic', 'true');
  announcer.className = 'sr-only';
  document.body.appendChild(announcer);
  return announcer;
}

function focusNextDropzone(currentElement) {
  const dropzones = Array.from(document.querySelectorAll('.dropzone'));
  const currentIndex = dropzones.indexOf(currentElement);
  const nextIndex = (currentIndex + 1) % dropzones.length;
  dropzones[nextIndex].focus();
}

// Call the accessibility enhancement function
enhanceAccessibility();
```

**Best Practices for HTML5 Drag and Drop:**

1. **Visual Feedback**:
   - Provide clear visual cues during drag operations
   - Highlight drop zones when items are dragged over them
   - Show a preview of where the item will be placed

2. **Performance**:
   - Use event delegation for large numbers of draggable items
   - Minimize DOM manipulations during drag operations
   - Consider throttling or debouncing dragover events

3. **Accessibility**:
   - Provide keyboard alternatives for drag and drop operations
   - Use ARIA attributes to enhance screen reader support
   - Ensure sufficient color contrast for visual indicators

4. **Mobile Support**:
   - Implement touch event handlers for mobile devices
   - Consider using libraries like mobile-drag-drop for better cross-device support
   - Test on various mobile devices and browsers

5. **Error Handling**:
   - Validate data during drop operations
   - Provide clear feedback when drops are invalid
   - Implement undo functionality for accidental drops

---

### Q49: How do you work with Web Storage API (localStorage and sessionStorage)?

**Answer:**
The Web Storage API provides mechanisms for storing key-value pairs in a web browser. It offers two storage objects with similar APIs but different behaviors:

1. **localStorage**: Persists data with no expiration date, even when the browser is closed and reopened
2. **sessionStorage**: Stores data for one session (data is lost when the browser tab is closed)

**Basic Usage:**

```javascript
// localStorage operations

// Storing data
localStorage.setItem('username', 'JohnDoe');
localStorage.setItem('isLoggedIn', 'true');
localStorage.setItem('lastLogin', new Date().toISOString());

// Retrieving data
const username = localStorage.getItem('username'); // Returns 'JohnDoe'
const isLoggedIn = localStorage.getItem('isLoggedIn'); // Returns 'true' as a string
const lastLogin = localStorage.getItem('lastLogin');

// Removing specific data
localStorage.removeItem('lastLogin');

// Clearing all data
localStorage.clear();

// Getting the number of items
const itemCount = localStorage.length;

// Getting key by index
for (let i = 0; i < localStorage.length; i++) {
  const key = localStorage.key(i);
  const value = localStorage.getItem(key);
  console.log(`${key}: ${value}`);
}

// sessionStorage operations (identical API)
sessionStorage.setItem('currentPage', 'dashboard');
const currentPage = sessionStorage.getItem('currentPage');
sessionStorage.removeItem('currentPage');
sessionStorage.clear();
```

**Storing Complex Data Types:**

Web Storage only supports strings. To store objects or arrays, you need to convert them to JSON:

```javascript
// Storing objects or arrays
const userPreferences = {
  theme: 'dark',
  fontSize: 16,
  notifications: {
    email: true,
    push: false
  },
  recentSearches: ['javascript', 'html5', 'css3']
};

// Convert to JSON string before storing
localStorage.setItem('userPreferences', JSON.stringify(userPreferences));

// Retrieve and parse back to object
const storedPreferences = JSON.parse(localStorage.getItem('userPreferences'));
console.log(storedPreferences.theme); // 'dark'
console.log(storedPreferences.notifications.email); // true
console.log(storedPreferences.recentSearches[0]); // 'javascript'
```

**Storage Event:**

The `storage` event fires when storage changes in one tab/window and can be detected in other tabs/windows:

```javascript
// Listen for changes to localStorage from other tabs/windows
window.addEventListener('storage', (event) => {
  console.log('Storage changed in another window/tab');
  console.log('Key modified:', event.key);
  console.log('Old value:', event.oldValue);
  console.log('New value:', event.newValue);
  console.log('Storage area:', event.storageArea); // localStorage or sessionStorage
  console.log('Page URL:', event.url);
  
  // Update UI based on the change if needed
  if (event.key === 'theme') {
    applyTheme(event.newValue);
  }
});
```

**Storage Wrapper Utility:**

A common pattern is to create a wrapper utility for Web Storage to handle JSON conversion and provide additional functionality:

```javascript
// Storage utility class
class StorageUtil {
  constructor(storageType = 'local') {
    this.storage = storageType === 'local' ? localStorage : sessionStorage;
  }
  
  // Get item with optional default value
  get(key, defaultValue = null) {
    const item = this.storage.getItem(key);
    
    if (item === null) {
      return defaultValue;
    }
    
    try {
      return JSON.parse(item);
    } catch (e) {
      return item;
    }
  }
  
  // Set item with automatic JSON stringification
  set(key, value) {
    try {
      const valueToStore = typeof value === 'object' ? JSON.stringify(value) : value;
      this.storage.setItem(key, valueToStore);
      return true;
    } catch (e) {
      console.error('Storage error:', e);
      return false;
    }
  }
  
  // Remove item
  remove(key) {
    this.storage.removeItem(key);
  }
  
  // Clear all items
  clear() {
    this.storage.clear();
  }
  
  // Get all stored items as an object
  getAll() {
    const items = {};
    
    for (let i = 0; i < this.storage.length; i++) {
      const key = this.storage.key(i);
      items[key] = this.get(key);
    }
    
    return items;
  }
  
  // Check if key exists
  has(key) {
    return this.storage.getItem(key) !== null;
  }
}

// Usage
const localStore = new StorageUtil('local');
const sessionStore = new StorageUtil('session');

localStore.set('user', { id: 123, name: 'John' });
const user = localStore.get('user');
console.log(user.name); // 'John'

// With default value
const settings = localStore.get('settings', { darkMode: false });
```

**Practical Examples:**

**1. Theme Switcher:**

```javascript
// Theme switcher with localStorage persistence
const themeToggle = document.getElementById('theme-toggle');
const body = document.body;

// Initialize theme from localStorage or default to 'light'
function initTheme() {
  const savedTheme = localStorage.getItem('theme') || 'light';
  body.setAttribute('data-theme', savedTheme);
  themeToggle.checked = savedTheme === 'dark';
}

// Toggle theme and save to localStorage
themeToggle.addEventListener('change', () => {
  const newTheme = themeToggle.checked ? 'dark' : 'light';
  body.setAttribute('data-theme', newTheme);
  localStorage.setItem('theme', newTheme);
});

// Initialize theme on page load
initTheme();
```

**2. Form Data Persistence:**

```javascript
// Save form data as user types
const contactForm = document.getElementById('contact-form');
const formFields = contactForm.querySelectorAll('input, textarea');
const formKey = 'contact_form_draft';

// Load saved form data
function loadFormData() {
  const savedData = sessionStorage.getItem(formKey);
  
  if (savedData) {
    const formData = JSON.parse(savedData);
    
    formFields.forEach(field => {
      if (formData[field.name]) {
        field.value = formData[field.name];
      }
    });
  }
}

// Save form data as user types
formFields.forEach(field => {
  field.addEventListener('input', saveFormData);
});

function saveFormData() {
  const formData = {};
  
  formFields.forEach(field => {
    formData[field.name] = field.value;
  });
  
  sessionStorage.setItem(formKey, JSON.stringify(formData));
}

// Clear saved data on form submission
contactForm.addEventListener('submit', () => {
  sessionStorage.removeItem(formKey);
});

// Load saved data when page loads
loadFormData();
```

**3. Shopping Cart:**

```javascript
// Simple shopping cart with localStorage
class ShoppingCart {
  constructor() {
    this.cartKey = 'shopping_cart';
    this.cart = this.getCart();
  }
  
  // Get cart from localStorage
  getCart() {
    const cartData = localStorage.getItem(this.cartKey);
    return cartData ? JSON.parse(cartData) : [];
  }
  
  // Save cart to localStorage
  saveCart() {
    localStorage.setItem(this.cartKey, JSON.stringify(this.cart));
    this.updateCartUI();
  }
  
  // Add item to cart
  addItem(product) {
    // Check if product already exists
    const existingItem = this.cart.find(item => item.id === product.id);
    
    if (existingItem) {
      existingItem.quantity += 1;
    } else {
      this.cart.push({
        ...product,
        quantity: 1
      });
    }
    
    this.saveCart();
  }
  
  // Remove item from cart
  removeItem(productId) {
    this.cart = this.cart.filter(item => item.id !== productId);
    this.saveCart();
  }
  
  // Update item quantity
  updateQuantity(productId, quantity) {
    const item = this.cart.find(item => item.id === productId);
    
    if (item) {
      item.quantity = Math.max(1, quantity);
      this.saveCart();
    }
  }
  
  // Clear cart
  clearCart() {
    this.cart = [];
    this.saveCart();
  }
  
  // Get cart total
  getTotal() {
    return this.cart.reduce((total, item) => {
      return total + (item.price * item.quantity);
    }, 0);
  }
  
  // Update cart UI
  updateCartUI() {
    const cartCount = document.getElementById('cart-count');
    const cartItems = document.getElementById('cart-items');
    const cartTotal = document.getElementById('cart-total');
    
    // Update cart count
    const itemCount = this.cart.reduce((count, item) => count + item.quantity, 0);
    cartCount.textContent = itemCount;
    
    // Update cart items list
    cartItems.innerHTML = '';
    
    this.cart.forEach(item => {
      const cartItem = document.createElement('div');
      cartItem.className = 'cart-item';
      cartItem.innerHTML = `
        <span>${item.name} x ${item.quantity}</span>
        <span>$${(item.price * item.quantity).toFixed(2)}</span>
        <button class="remove-item" data-id="${item.id}">Remove</button>
      `;
      cartItems.appendChild(cartItem);
    });
    
    // Add event listeners to remove buttons
    document.querySelectorAll('.remove-item').forEach(button => {
      button.addEventListener('click', () => {
        this.removeItem(button.dataset.id);
      });
    });
    
    // Update total
    cartTotal.textContent = `$${this.getTotal().toFixed(2)}`;
  }
}

// Initialize cart
const cart = new ShoppingCart();

// Add product to cart when 'Add to Cart' button is clicked
document.querySelectorAll('.add-to-cart').forEach(button => {
  button.addEventListener('click', () => {
    const productId = button.dataset.id;
    const productName = button.dataset.name;
    const productPrice = parseFloat(button.dataset.price);
    
    cart.addItem({
      id: productId,
      name: productName,
      price: productPrice
    });
  });
});

// Initialize cart UI
cart.updateCartUI();
```

**Storage Limitations and Best Practices:**

1. **Storage Limits**:
   - Most browsers limit storage to 5-10MB per domain
   - When the limit is exceeded, browsers may throw a `QuotaExceededError`

```javascript
// Handle storage quota errors
function safelyStoreData(key, data) {
  try {
    localStorage.setItem(key, data);
    return true;
  } catch (e) {
    if (isQuotaExceededError(e)) {
      alert('Storage quota exceeded. Please clear some space.');
      // Implement a cleanup strategy here
      cleanupOldData();
      return false;
    }
    throw e; // Re-throw if it's a different error
  }
}

function isQuotaExceededError(e) {
  return (
    e instanceof DOMException &&
    // Firefox
    (e.code === 22 ||
     // Chrome
     e.code === 1014 ||
     // Safari
     e.name === 'QuotaExceededError' ||
     // Firefox
     e.name === 'NS_ERROR_DOM_QUOTA_REACHED')
  );
}

function cleanupOldData() {
  // Strategy: Remove oldest items first
  const itemTimestamps = JSON.parse(localStorage.getItem('item_timestamps') || '{}');
  const keys = Object.keys(itemTimestamps);
  
  // Sort keys by timestamp (oldest first)
  keys.sort((a, b) => itemTimestamps[a] - itemTimestamps[b]);
  
  // Remove oldest items until we've cleared enough space
  for (let i = 0; i < Math.min(keys.length, 5); i++) {
    localStorage.removeItem(keys[i]);
  }
  
  // Update timestamps
  for (let i = 0; i < keys.length; i++) {
    delete itemTimestamps[keys[i]];
  }
  
  localStorage.setItem('item_timestamps', JSON.stringify(itemTimestamps));
}

// When storing an item, also store its timestamp
function storeWithTimestamp(key, value) {
  // Store the actual data
  localStorage.setItem(key, value);
  
  // Update timestamp registry
  const timestamps = JSON.parse(localStorage.getItem('item_timestamps') || '{}');
  timestamps[key] = Date.now();
  localStorage.setItem('item_timestamps', JSON.stringify(timestamps));
}
```

2. **Security Considerations**:
   - Never store sensitive data (passwords, tokens) in localStorage as it's accessible via JavaScript
   - sessionStorage is slightly more secure but still vulnerable to XSS attacks

```javascript
// DON'T DO THIS - Insecure storage of sensitive data
localStorage.setItem('authToken', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...');

// Better approach - store non-sensitive data only
localStorage.setItem('userPreferences', JSON.stringify({ theme: 'dark' }));

// For sensitive data, use HttpOnly cookies (server-side) or a more secure approach
```

3. **Data Expiration**:
   - localStorage doesn't have built-in expiration, but you can implement it manually

```javascript
// Storage with expiration
const storageWithExpiry = {
  setWithExpiry(key, value, ttl) {
    const item = {
      value: value,
      expiry: Date.now() + ttl,
    };
    localStorage.setItem(key, JSON.stringify(item));
  },
  
  getWithExpiry(key) {
    const itemStr = localStorage.getItem(key);
    
    // Return null if item doesn't exist
    if (!itemStr) {
      return null;
    }
    
    const item = JSON.parse(itemStr);
    const isExpired = Date.now() > item.expiry;
    
    // Delete if expired
    if (isExpired) {
      localStorage.removeItem(key);
      return null;
    }
    
    return item.value;
  }
};

// Usage
// Store data with 1-day expiration (86400000 ms)
storageWithExpiry.setWithExpiry('user', { name: 'John' }, 86400000);

// Get data (returns null if expired)
const user = storageWithExpiry.getWithExpiry('user');
```

4. **Storage Events and Synchronization**:
   - Use storage events to keep multiple tabs in sync

```javascript
// Synchronize data across tabs
function syncDataAcrossTabs() {
  // Listen for changes in other tabs
  window.addEventListener('storage', (event) => {
    if (event.key === 'appState') {
      updateUIFromState(JSON.parse(event.newValue));
    }
  });
  
  // Update data and notify other tabs
  function updateAppState(newState) {
    // Update localStorage
    localStorage.setItem('appState', JSON.stringify(newState));
    
    // Update current tab's UI
    updateUIFromState(newState);
  }
  
  function updateUIFromState(state) {
    // Update UI based on state
    document.body.className = state.theme;
    document.getElementById('username').textContent = state.username;
    // etc.
  }
  
  return {
    updateAppState
  };
}

const tabSync = syncDataAcrossTabs();

// Usage
document.getElementById('theme-switch').addEventListener('click', () => {
  const currentState = JSON.parse(localStorage.getItem('appState') || '{}');
  const newTheme = currentState.theme === 'dark' ? 'light' : 'dark';
  
  tabSync.updateAppState({
    ...currentState,
    theme: newTheme
  });
});
```

5. **Feature Detection**:
   - Always check if Web Storage is available before using it

```javascript
function isStorageAvailable(type) {
  try {
    const storage = window[type];
    const testKey = '__storage_test__';
    storage.setItem(testKey, testKey);
    storage.removeItem(testKey);
    return true;
  } catch (e) {
    return false;
  }
}

// Usage
if (isStorageAvailable('localStorage')) {
  // localStorage is available
  initializeApp();
} else {
  // localStorage is not available
  // Implement fallback (cookies, in-memory storage, etc.)
  initializeAppWithFallback();
}
```

**Comparison with Cookies:**

| Feature | localStorage | sessionStorage | Cookies |
|---------|-------------|----------------|--------|
| Capacity | ~5-10MB | ~5-10MB | ~4KB |
| Expiration | Never | Tab close | Configurable |
| Storage Location | Browser only | Browser only | Browser & Server |
| Sent with Requests | No | No | Yes |
| Accessibility | JavaScript only | JavaScript only | JavaScript & Server |
| Editable by User | Yes | Yes | Yes |
| Security | Vulnerable to XSS | Vulnerable to XSS | Can be made secure with HttpOnly flag |

**Modern Alternatives:**

1. **IndexedDB**: For larger, structured data storage
2. **Cache API**: For storing HTTP responses (part of Service Workers)
3. **Web SQL**: Deprecated, not recommended for new projects

```javascript
// Example of when to use IndexedDB instead of localStorage
function shouldUseIndexedDB(dataSize) {
  // If data is larger than 1MB, prefer IndexedDB
  return dataSize > 1024 * 1024;
}

// Example of using Cache API with Service Worker
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open('app-static-v1').then((cache) => {
      return cache.addAll([
        '/',
        '/styles.css',
        '/app.js',
        '/logo.png'
      ]);
    })
  );
});

---

---

### Q50: What is the difference between `<em>` and `<strong>` tags?

**Answer:**

Both `<em>` and `<strong>` are HTML tags used to give special emphasis to text, but they convey different semantic meanings and are used for different purposes.

#### `<em>` (Emphasis) Tag

*   **Semantic Meaning**: The `<em>` tag is used to indicate **stress emphasis**. It suggests that the enclosed text should be read with a different tone or emphasis, which can change the meaning of the sentence.
*   **Default Browser Styling**: Browsers typically render `<em>` text in *italics*.
*   **Use Case**: Use `<em>` when you want to change the nuance of a sentence. It's about linguistic emphasis.

**Example**:

```html
<p>I am <em>so</em> excited to learn HTML!</p>
<!-- The emphasis on "so" intensifies the feeling of excitement. -->

<p>You <em>must</em> complete this task by Friday.</p>
<!-- The emphasis on "must" highlights the urgency or requirement. -->
```

#### `<strong>` (Strong Importance) Tag

*   **Semantic Meaning**: The `<strong>` tag is used to indicate **strong importance, seriousness, or urgency**. It marks text that is more important than the surrounding content.
*   **Default Browser Styling**: Browsers typically render `<strong>` text in **bold**.
*   **Use Case**: Use `<strong>` for warnings, important notices, or to highlight keywords that are central to the content.

**Example**:

```html
<p><strong>Warning:</strong> Do not touch the live wires.</p>
<!-- The "Warning" is critical information for safety. -->

<p>This task is of <strong>high priority</strong>.</p>
<!-- "High priority" signals the importance of the task. -->
```

#### Key Differences Summarized

| Feature             | `<em>` Tag                               | `<strong>` Tag                             |
| ------------------- | ----------------------------------------- | ------------------------------------------ |
| **Semantic Meaning**| Stress emphasis (changes sentence meaning) | Strong importance, seriousness, or urgency |
| **Default Style**   | Italic                                    | Bold                                       |
| **Use Case**        | To alter the tone or nuance of a sentence | For warnings, critical notices, or keywords|
| **Accessibility**   | Screen readers may change their tone of voice | Screen readers may speak with a stronger voice |

#### Why Not Just Use `<b>` and `<i>`?

The `<b>` (bold) and `<i>` (italic) tags are purely presentational. They tell the browser to make text bold or italic without conveying any semantic meaning. While they still work, `<strong>` and `<em>` are preferred because they provide additional context to search engines and assistive technologies like screen readers, which improves both SEO and accessibility.

---

---

### Q51: What is the purpose of the `DOCTYPE` declaration?

**Answer:**

The `<!DOCTYPE html>` declaration is an instruction to the web browser about what version of HTML the page is written in. It is the very first thing in your HTML document, before the `<html>` tag.

#### Why is it Important?

1.  **Triggers Standards Mode**: The primary purpose of the `DOCTYPE` is to prevent the browser from switching into **"quirks mode."**
    *   **Standards Mode**: The browser renders the page according to the W3C and IETF standards. This ensures more predictable and consistent rendering across different browsers.
    *   **Quirks Mode**: If the `DOCTYPE` is missing or incorrect, the browser makes a best-guess attempt to render the page, often by emulating the behavior of older, non-standard browsers (like Netscape 4 and Internet Explorer 5). This can lead to inconsistent layouts and buggy behavior.

2.  **Ensures Cross-Browser Compatibility**: By telling all browsers to use the same rendering mode (standards mode), the `DOCTYPE` helps ensure that your website looks and functions the same way for all users, regardless of the browser they are using.

3.  **Enables HTML5 Features**: The modern `<!DOCTYPE html>` declaration is specifically what tells the browser to interpret the document as HTML5. Without it, new HTML5 elements (like `<article>`, `<section>`, `<nav>`) and APIs may not work correctly.

#### The HTML5 `DOCTYPE`

The `DOCTYPE` for HTML5 is simple and case-insensitive:

```html
<!DOCTYPE html>
```

This is much simpler than the `DOCTYPE` declarations required for older versions of HTML, which were based on SGML (Standard Generalized Markup Language) and required a reference to a Document Type Definition (DTD).

**Example of an older XHTML 1.0 Strict `DOCTYPE`:**

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
```

Fortunately, with HTML5, we only need to remember the simple version.

#### In Summary

| Without `<!DOCTYPE html>` (Quirks Mode) | With `<!DOCTYPE html>` (Standards Mode) |
| --------------------------------------- | --------------------------------------- |
| Inconsistent rendering across browsers  | Consistent, predictable rendering       |
| CSS might not apply as expected         | CSS rules are interpreted correctly     |
| Layouts can break easily                | Layouts are more stable and reliable    |
| HTML5 features may not work             | Full HTML5 support is enabled           |

**Conclusion**: Always include the `<!DOCTYPE html>` declaration at the very beginning of every HTML document. It is not an HTML tag; it is a mandatory instruction that ensures your web page is rendered correctly and consistently.

---

---

### Q52: What is the difference between an `id` and a `class`?

**Answer:**

The `id` and `class` attributes are both used to apply identifiers to HTML elements, but they serve different purposes and have different rules.

#### `id` Attribute

*   **Uniqueness**: An `id` must be **unique** within the entire HTML document. No two elements can have the same `id`.
*   **Purpose**: It is used to identify a single, specific element.
*   **Use Cases**:
    1.  **Styling with CSS**: To apply styles to a unique element (e.g., `#header`, `#main-content`).
    2.  **JavaScript Manipulation**: To select and manipulate a specific element using `document.getElementById()`.
    3.  **Fragment Identifiers (Anchor Links)**: To create links that jump to a specific section of a page (e.g., `<a href="#section1">`).

**Example**:

```html
<div id="main-header">
  <h1>Welcome to my Website</h1>
</div>

<style>
  #main-header {
    background-color: #333;
    color: white;
  }
</style>

<script>
  const header = document.getElementById('main-header');
  header.style.padding = '20px';
</script>
```

#### `class` Attribute

*   **Uniqueness**: A `class` name can be used on **multiple** elements.
*   **Purpose**: It is used to group multiple elements that share the same characteristics or styling.
*   **Multiple Classes**: An element can have multiple class names, separated by spaces.
*   **Use Cases**:
    1.  **Styling with CSS**: To apply the same styles to a group of elements (e.g., `.button`, `.alert`, `.card`).
    2.  **JavaScript Manipulation**: To select and manipulate a group of elements using `document.getElementsByClassName()` or `document.querySelectorAll()`.

**Example**:

```html
<button class="btn btn-primary">Submit</button>
<button class="btn btn-secondary">Cancel</button>

<div class="alert alert-success">Operation was successful!</div>
<div class="alert alert-danger">An error occurred.</div>

<style>
  .btn {
    padding: 10px 15px;
    border-radius: 5px;
  }
  .btn-primary {
    background-color: blue;
    color: white;
  }
  .alert {
    padding: 15px;
    margin-bottom: 10px;
  }
  .alert-success {
    background-color: lightgreen;
  }
</style>
```

#### Summary of Key Differences

| Feature          | `id`                                      | `class`                                       |
| ---------------- | ----------------------------------------- | --------------------------------------------- |
| **Uniqueness**   | Must be unique within the page            | Can be used on multiple elements              |
| **CSS Selector** | `#` (e.g., `#my-id`)                      | `.` (e.g., `.my-class`)                       |
| **JavaScript**   | `document.getElementById()` (returns one element) | `getElementsByClassName()` (returns a collection) |
| **Usage**        | For a single, unique element              | For a group of similar elements               |
| **Anchor Links** | Yes (`href="#my-id"`)                     | No                                            |

#### Best Practices

*   Use `id` for major, unique page sections like headers, footers, and main content areas.
*   Use `class` for reusable components and elements that appear multiple times, like buttons, cards, alerts, and list items.
*   Avoid using `id` for styling if the same style might be needed elsewhere. A `class` is more flexible and reusable.

---

---

### Q53: What are `data-*` attributes and why are they used?

**Answer:**

`data-*` attributes are a standardized way to embed custom, private data on an HTML element. They allow you to store extra information that doesn't have a defined semantic meaning, which can then be easily accessed and manipulated by JavaScript.

#### Syntax and Rules

*   The attribute name must start with `data-`.
*   It must contain at least one character after the prefix.
*   The attribute name should not contain any uppercase letters.
*   The attribute value can be any string.

**Example**:

```html
<div id="user-profile" data-user-id="12345" data-user-role="admin" data-active-status="true">
  <p>Username: JohnDoe</p>
</div>

<ul>
  <li data-animal-type="mammal">Dog</li>
  <li data-animal-type="bird">Eagle</li>
  <li data-animal-type="reptile">Lizard</li>
</ul>
```

#### Why Use `data-*` Attributes?

1.  **Storing Element-Specific Data**: They are perfect for storing simple data that is directly related to an element, such as a product ID, a user role, or a component's state, without polluting the `class` or `id` attributes.

2.  **Clean Separation**: They keep custom data within the HTML, separating it from JavaScript logic. This can make the code cleaner and more declarative.

3.  **JavaScript Hooks**: They provide a way for JavaScript to interact with elements without relying on non-semantic classes like `js-modal-trigger`. Instead, you can use a selector like `[data-action="open-modal"]`.

4.  **Styling with CSS**: You can also use `data-*` attributes as selectors in CSS to apply styles based on the data.

#### Accessing `data-*` Attributes

You can access `data-*` attributes in JavaScript using two main methods:

1.  **`getAttribute()` / `setAttribute()`**: The traditional way to access any attribute.

2.  **`dataset` Property**: The recommended, more convenient way. The `dataset` property is a `DOMStringMap` object that provides access to all `data-*` attributes on an element. The part of the attribute name after `data-` is converted from kebab-case to camelCase.

**Example of Accessing Data:**

```html
<div id="product" data-product-id="987" data-in-stock="false">...</div>
```

```javascript
const productElement = document.getElementById('product');

// Using getAttribute()
const productId = productElement.getAttribute('data-product-id'); // "987"

// Using the dataset property (recommended)
const productIdFromDataset = productElement.dataset.productId; // "987"
const inStock = productElement.dataset.inStock; // "false"

console.log(productIdFromDataset); // "987"
console.log(typeof inStock); // string

// Modifying data attributes
productElement.dataset.inStock = 'true';
// This changes the HTML to: <div ... data-in-stock="true">
```

**Note**: All values read from `dataset` are strings. You may need to convert them to the appropriate type (e.g., using `parseInt()` or `JSON.parse()`).

#### Styling with CSS

You can use attribute selectors to style elements based on their `data-*` attributes.

```css
/* Style all elements with a specific data attribute */
[data-user-role] {
  border: 1px solid #ccc;
}

/* Style based on a specific data attribute value */
[data-user-role="admin"] {
  background-color: lightyellow;
  border-color: gold;
}

[data-active-status="false"] {
  opacity: 0.5;
}
```

In summary, `data-*` attributes provide a powerful and standard-compliant way to add custom data to your HTML, making your code more organized and maintainable.

---

---

### Q54: What is the difference between block and inline elements?

**Answer:**

In HTML, elements are generally categorized as either **block-level** or **inline-level**. The primary difference between them lies in how they are displayed on the page and the box model properties they can accept.

#### Block-Level Elements

Block-level elements are designed to structure the main parts of your web page.

*   **Display Behavior**:
    *   They always start on a **new line**.
    *   They take up the **full width** available to them, stretching from the left to the right edge of their container.
*   **Content Model**: They can contain other block-level elements and inline-level elements.
*   **Box Model**: You can set `width`, `height`, `margin` (top and bottom), and `padding` on them.

**Common Block-Level Elements**:
*   `<div>`
*   `<p>`
*   `<h1>` - `<h6>`
*   `<ul>`, `<ol>`, `<li>`
*   `<form>`
*   `<header>`, `<footer>`, `<section>`, `<article>`, `<nav>`

**Example**:

```html
<div style="background-color: lightblue;">This is a div.</div>
<p style="background-color: lightcoral;">This is a paragraph.</p>
```

Each of these elements will appear on its own line and span the full width of the page.

#### Inline-Level Elements

Inline-level elements are used for smaller pieces of content within a block-level element.

*   **Display Behavior**:
    *   They do **not** start on a new line.
    *   They only take up as much **width as necessary** to fit their content.
*   **Content Model**: They can generally only contain other inline-level elements.
*   **Box Model**: You can set `padding` and `margin` on the left and right, but **top and bottom margins and padding are not respected**. `width` and `height` properties have no effect.

**Common Inline-Level Elements**:
*   `<span>`
*   `<a>`
*   `<img>`
*   `<strong>`, `<em>`
*   `<input>`, `<button>`, `<label>`
*   `<br>`

**Example**:

```html
<p>
  This is a paragraph with an <a href="#">inline link</a> and a 
  <span style="background-color: lightgreen;">span element</span> inside it.
</p>
```

Both the `<a>` and `<span>` elements will appear within the flow of the paragraph text.

#### Key Differences Summarized

| Feature              | Block-Level Elements                      | Inline-Level Elements                          |
| -------------------- | ----------------------------------------- | ---------------------------------------------- |
| **Starts on New Line** | Yes                                       | No                                             |
| **Width**            | Takes up the full available width         | Takes up only the necessary width              |
| **Content**          | Can contain block and inline elements     | Can usually only contain inline elements       |
| **`width` & `height`** | Respected                                 | Not respected                                  |
| **`margin` & `padding`** | All sides are respected                   | Only left and right sides are respected        |

#### The `display` Property

You can change the default display behavior of any element using the CSS `display` property. The most common values are:

*   `display: block;` (Makes an inline element behave like a block)
*   `display: inline;` (Makes a block element behave like an inline)
*   `display: inline-block;` (A hybrid of the two)
*   `display: none;` (Hides the element completely)

**`inline-block`**: This value is particularly useful. It makes an element flow like an inline element (doesn't start on a new line) but allows you to set `width`, `height`, and top/bottom `margin` and `padding` like a block element.

---

---

### Q55: What is the CSS Box Model?

**Answer:**

The CSS Box Model is a fundamental concept that describes how every HTML element is represented as a rectangular box on a web page. This box consists of four parts, layered like an onion:

1.  **Content**: The actual content of the box, where text and images appear. Its dimensions are defined by `width` and `height`.
2.  **Padding**: The transparent area around the content, clearing space between the content and the border. It is controlled by `padding` properties.
3.  **Border**: A border that goes around the padding and content. It is defined by `border` properties.
4.  **Margin**: The transparent area outside the border, creating space between this element and other elements. It is controlled by `margin` properties.

Here is a visual representation:

```
  +---------------------------------------------------+
  |                      Margin                       |
  |   +-------------------------------------------+   |
  |   |                   Border                  |   |
  |   |   +-----------------------------------+   |   |
  |   |   |              Padding              |   |   |
  |   |   |   +---------------------------+   |   |   |
  |   |   |   |          Content          |   |   |   |
  |   |   |   +---------------------------+   |   |   |
  |   |   |                                   |   |   |
  |   |   +-----------------------------------+   |   |
  |   |                                           |   |
  |   +-------------------------------------------+   |
  |                                                   |
  +---------------------------------------------------+
```

#### `box-sizing` Property

The `box-sizing` property changes how the total width and height of an element are calculated.

1.  **`content-box` (Default)**:
    *   The `width` and `height` properties apply only to the **content area**.
    *   The total width of the element is `width` + `padding-left` + `padding-right` + `border-left` + `border-right`.
    *   The total height is `height` + `padding-top` + `padding-bottom` + `border-top` + `border-bottom`.

    **Example**:

    ```css
    .box {
      width: 200px;
      padding: 20px;
      border: 10px solid black;
      box-sizing: content-box; /* Default behavior */
    }
    /* Total width = 200 + 20 + 20 + 10 + 10 = 260px */
    ```

2.  **`border-box`**:
    *   The `width` and `height` properties include the **content, padding, and border**.
    *   The total width of the element is simply the value of the `width` property.
    *   The content area shrinks to accommodate the padding and border.

    **Example**:

    ```css
    .box {
      width: 200px;
      padding: 20px;
      border: 10px solid black;
      box-sizing: border-box;
    }
    /* Total width = 200px */
    ```

Using `box-sizing: border-box;` is a common best practice because it makes layout calculations more intuitive and predictable. It's often applied globally:

```css
html {
  box-sizing: border-box;
}

*, *::before, *::after {
  box-sizing: inherit;
}
```

This setup ensures that all elements use the more manageable `border-box` model, simplifying responsive design and grid layouts.

---

---

### Q56: What is CSS Specificity and how is it calculated?

**Answer:**

CSS Specificity is the set of rules browsers use to determine which CSS style declaration is applied to an element when multiple, conflicting declarations exist. It's a weighting system that gives more importance to certain types of selectors.

#### The Specificity Hierarchy

Specificity is calculated by scoring selectors based on their components. The hierarchy, from highest to lowest specificity, is as follows:

1.  **Inline Styles**: Styles applied directly to an element using the `style` attribute.
    *   Example: `<div style="color: red;">`

2.  **IDs**: Selectors that target an element by its unique `id`.
    *   Example: `#my-id`

3.  **Classes, Attributes, and Pseudo-classes**: This group includes:
    *   Classes (`.my-class`)
    *   Attribute selectors (`[type="text"]`)
    *   Pseudo-classes (`:hover`, `:focus`)

4.  **Elements and Pseudo-elements**: This is the least specific group.
    *   Element selectors (`div`, `p`)
    *   Pseudo-elements (`::before`, `::after`)

#### How to Calculate Specificity

A common way to visualize specificity is as a three-column value: `(IDs, Classes, Elements)`.

*   **IDs**: Count the number of ID selectors. `(1, 0, 0)`
*   **Classes**: Count the number of class, attribute, and pseudo-class selectors. `(0, 1, 0)`
*   **Elements**: Count the number of element and pseudo-element selectors. `(0, 0, 1)`

When comparing two selectors, the one with the highest value in the leftmost column wins. If they are equal, move to the next column to the right.

**Example Calculation**:

Consider the following CSS:

```css
/* Specificity: (0, 0, 1) */
div { color: blue; }

/* Specificity: (0, 1, 0) */
.my-class { color: green; }

/* Specificity: (1, 0, 0) */
#my-id { color: purple; }

/* Specificity: (0, 1, 1) */
div.my-class { color: orange; }

/* Specificity: (1, 1, 0) */
#my-id.my-class { color: pink; }
```

And this HTML:

```html
<div id="my-id" class="my-class">Hello World</div>
```

The text will be **pink**. Here's why:

1.  `#my-id.my-class` `(1, 1, 0)` beats `#my-id` `(1, 0, 0)` because it has a higher value in the second column.
2.  It also beats `div.my-class` `(0, 1, 1)` because it has a higher value in the first column.

#### The `!important` Rule

The `!important` rule is an exception that overrides all other specificity rules. When `!important` is added to a style declaration, that declaration takes precedence over any other.

```css
p {
  color: blue !important; /* This will always be applied */
}

#my-paragraph {
  color: red; /* This will be ignored */
}
```

**Best Practice**: Avoid using `!important` unless absolutely necessary (e.g., overriding styles from a third-party library). Overusing it can lead to a specificity war and make your CSS difficult to maintain.

#### Summary Table

| Selector Type                               | Specificity Value |
| ------------------------------------------- | ----------------- |
| `!important`                                | Overrides all     |
| Inline Styles (`style="..."`)               | `(1, 0, 0, 0)`*   |
| ID (`#my-id`)                               | `(0, 1, 0, 0)`    |
| Class (`.my-class`), Attribute (`[type]`), Pseudo-class (`:hover`) | `(0, 0, 1, 0)`    |
| Element (`div`), Pseudo-element (`::before`) | `(0, 0, 0, 1)`    |
| Universal Selector (`*`), Combinators (`+`, `>`) | No specificity    |

*Note: Some representations use four columns to include inline styles.*

---

---

### Q57: What is the difference between `display: none;` and `visibility: hidden;`?

**Answer:**

Both `display: none;` and `visibility: hidden;` make an element invisible, but they do so in fundamentally different ways, which affects page layout and behavior.

#### `display: none;`

When you apply `display: none;` to an element, it's as if the element doesn't exist in the document at all.

*   **Layout**: The element is completely **removed from the document flow**. It takes up **no space** on the page, and other elements will reflow to fill the void.
*   **Visibility**: The element and all its descendant elements are hidden.
*   **Accessibility**: The element is ignored by screen readers.
*   **Events**: The element cannot be targeted by JavaScript events.

**Example**:

```html
<p>First paragraph.</p>
<p style="display: none;">This paragraph is hidden.</p>
<p>Third paragraph.</p>
```

In this case, the third paragraph will appear immediately after the first, as if the second paragraph never existed.

#### `visibility: hidden;`

When you apply `visibility: hidden;`, the element is hidden, but it still occupies its space in the layout.

*   **Layout**: The element is **still part of the document flow** and **takes up its original space**. It's rendered as an invisible box.
*   **Visibility**: The element is hidden, but its descendant elements can be made visible again by setting `visibility: visible;` on them.
*   **Accessibility**: The element is still accessible to screen readers (though its content is not spoken).
*   **Events**: The element cannot be targeted by JavaScript events.

**Example**:

```html
<p>First paragraph.</p>
<p style="visibility: hidden;">This paragraph is invisible but takes up space.</p>
<p>Third paragraph.</p>
```

Here, there will be a visible gap between the first and third paragraphs, which is the space occupied by the hidden second paragraph.

#### Comparison Table

| Feature                      | `display: none;`                                  | `visibility: hidden;`                             |
| ---------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| **Effect on Layout**         | Element is removed from the document flow.        | Element remains in the flow, occupying space.     |
| **Space Occupied**           | Takes up no space.                                | Takes up its full, original space.                |
| **Child Elements**           | All children are hidden and cannot be made visible. | Children are hidden but can be made visible.      |
| **Performance**              | Triggers a browser **reflow** (re-calculation of layout). | Triggers a browser **repaint** (re-drawing the screen). |
| **Accessibility**            | Ignored by screen readers.                        | Not read by screen readers but still in the accessibility tree. |
| **Use Case**                 | Hiding/showing elements dynamically (e.g., modals, dropdowns). | Creating visual effects where space must be preserved. |

In summary, use `display: none;` when you want to completely remove an element from the page, and use `visibility: hidden;` when you need to hide an element while preserving the space it occupies.

---

---

### Q58: What are the different values for the CSS `position` property?

**Answer:**

The CSS `position` property determines the positioning method used for an element. It works in conjunction with the offset properties `top`, `right`, `bottom`, and `left`. There are five main values for `position`.

#### 1. `static`

*   **Default value**.
*   The element is positioned according to the **normal document flow**.
*   The offset properties (`top`, `right`, `bottom`, `left`) and `z-index` have **no effect**.

```css
.static-element {
  position: static;
}
```

#### 2. `relative`

*   The element is positioned according to the normal document flow, but you can then **offset it relative to its original position**.
*   The offset properties move the element from its static position without affecting the layout of surrounding elements.
*   It creates a **new stacking context** and establishes a positioning context for `absolute`-ly positioned child elements.

```css
.relative-element {
  position: relative;
  top: -20px; /* Moves up 20px */
  left: 20px; /* Moves right 20px */
}
```

#### 3. `absolute`

*   The element is **removed from the normal document flow**.
*   It is positioned relative to its **nearest positioned ancestor** (i.e., an ancestor with a `position` value other than `static`).
*   If no positioned ancestor is found, it is positioned relative to the initial containing block (usually the `<html>` element).
*   Other elements behave as if the absolutely positioned element does not exist.

```css
.parent {
  position: relative; /* Establishes positioning context */
}

.absolute-element {
  position: absolute;
  top: 10px;
  right: 10px;
}
```

#### 4. `fixed`

*   The element is **removed from the normal document flow**.
*   It is positioned relative to the **viewport** (the browser window).
*   It stays in the same place even when the page is scrolled.
*   Commonly used for navigation bars, headers, or chat widgets.

```css
.fixed-element {
  position: fixed;
  bottom: 0;
  width: 100%;
  background-color: #333;
}
```

#### 5. `sticky`

*   A hybrid of `relative` and `fixed` positioning.
*   The element is treated as `position: relative` until it crosses a specified threshold (defined by `top`, `right`, `bottom`, or `left`) during scrolling, at which point it becomes `position: fixed`.
*   It "sticks" to its container.

```css
.sticky-element {
  position: sticky;
  top: 0; /* Sticks to the top of the viewport when scrolling */
}
```

#### Comparison Table

| `position` Value | In Document Flow? | Positioning Context                               | Use Case                                    |
| :--------------- | :---------------- | :------------------------------------------------ | :------------------------------------------ |
| **`static`**     | Yes               | N/A                                               | Default element behavior.                   |
| **`relative`**   | Yes               | Its own static position                           | Minor adjustments; creating a context for `absolute` children. |
| **`absolute`**   | No                | Nearest positioned ancestor                       | Overlays, tooltips, complex layouts.        |
| **`fixed`**      | No                | Viewport                                          | Sticky headers/footers, modals.             |
| **`sticky`**     | Yes               | Scrolls with parent, then sticks to the viewport | Sticky navigation, section headings.        |

---

---

### Q59: What is CSS Flexbox?

**Answer:**

CSS Flexible Box Layout, commonly known as **Flexbox**, is a one-dimensional layout model designed to provide a more efficient way to arrange, align, and distribute space among items in a container, even when their size is unknown or dynamic.

To start using Flexbox, you apply `display: flex;` to a container element. This container becomes a **flex container**, and its direct children become **flex items**.

```html
<div class="flex-container">
  <div>1</div>
  <div>2</div>
  <div>3</div>
</div>
```

```css
.flex-container {
  display: flex;
}
```

Flexbox has two axes:

*   **Main Axis**: The primary axis along which flex items are laid out. It is defined by the `flex-direction` property.
*   **Cross Axis**: The axis perpendicular to the main axis.

#### Key Properties for the Flex Container

1.  **`flex-direction`**: Defines the direction of the main axis.
    *   `row` (default): Left to right.
    *   `row-reverse`: Right to left.
    *   `column`: Top to bottom.
    *   `column-reverse`: Bottom to top.

2.  **`justify-content`**: Aligns flex items along the **main axis**.
    *   `flex-start` (default): Items are packed toward the start.
    *   `flex-end`: Items are packed toward the end.
    *   `center`: Items are centered.
    *   `space-between`: Items are evenly distributed; the first item is on the start line, the last on the end line.
    *   `space-around`: Items are evenly distributed with equal space around them.

3.  **`align-items`**: Aligns flex items along the **cross axis**.
    *   `stretch` (default): Items stretch to fill the container.
    *   `flex-start`: Items are placed at the start of the cross axis.
    *   `flex-end`: Items are placed at the end of the cross axis.
    *   `center`: Items are centered on the cross axis.

4.  **`flex-wrap`**: Controls whether flex items are forced onto one line or can wrap onto multiple lines.
    *   `nowrap` (default): All items will be on one line.
    *   `wrap`: Items will wrap onto multiple lines, from top to bottom.
    *   `wrap-reverse`: Items will wrap onto multiple lines from bottom to top.

#### Key Properties for Flex Items

1.  **`flex-grow`**: Defines the ability of a flex item to grow if necessary. It accepts a unitless value that serves as a proportion.
    *   `flex-grow: 1;` means the item will take up any remaining space in the container.

2.  **`flex-shrink`**: Defines the ability of a flex item to shrink if necessary.

3.  **`flex-basis`**: Defines the default size of an element before the remaining space is distributed.

4.  **`flex` (Shorthand)**: Combines `flex-grow`, `flex-shrink`, and `flex-basis`.
    *   `flex: 0 1 auto;` (default)
    *   `flex: 1;` is equivalent to `flex: 1 1 0;`

5.  **`align-self`**: Allows the default alignment (or the one specified by `align-items`) to be overridden for individual flex items.

**Example**: A simple centered layout.

```css
.container {
  display: flex;
  justify-content: center; /* Center horizontally */
  align-items: center;     /* Center vertically */
  height: 100vh;
}
```

Flexbox is ideal for component layouts and small-scale designs, while CSS Grid is generally better for large-scale, two-dimensional page layouts.

---

---

### Q60: What is CSS Grid?

**Answer:**

CSS Grid Layout is a **two-dimensional** layout system for the web. It lets you create complex, responsive layouts with rows and columns, making it easier to design web pages without having to use hacks like floats and positioning.

To start using Grid, you apply `display: grid;` to a container element. This becomes a **grid container**, and its direct children become **grid items**.

```html
<div class="grid-container">
  <div class="item">1</div>
  <div class="item">2</div>
  <div class="item">3</div>
  <div class="item">4</div>
</div>
```

#### Core Concepts of CSS Grid

*   **Grid Container**: The element on which `display: grid` is applied.
*   **Grid Item**: The direct children of the grid container.
*   **Grid Line**: The dividing lines that make up the structure of the grid.
*   **Grid Track**: The space between two adjacent grid lines (a column or a row).
*   **Grid Cell**: The space between two adjacent row and two adjacent column grid lines (a single "unit" of the grid).
*   **Grid Area**: A total space surrounded by four grid lines, which can be composed of any number of grid cells.

#### Key Properties for the Grid Container

1.  **`grid-template-columns` / `grid-template-rows`**: Defines the columns and rows of the grid.
    *   You can use any length unit (`px`, `%`, `em`).
    *   The `fr` unit represents a fraction of the available space.

    ```css
    .container {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr; /* Three equal-width columns */
      grid-template-rows: 100px 200px;   /* Two rows with specified heights */
    }
    ```

2.  **`grid-gap` (or `gap`)**: A shorthand for `grid-row-gap` and `grid-column-gap`, specifying the size of the grid lines (the gutter).

    ```css
    .container {
      display: grid;
      gap: 20px;
    }
    ```

3.  **`justify-items` / `align-items`**: Aligns grid items along the row (inline) and column (block) axes within their grid area.
    *   Values: `start`, `end`, `center`, `stretch` (default).

4.  **`justify-content` / `align-content`**: Aligns the entire grid within the grid container when the total size of the grid is smaller than its container.

#### Key Properties for Grid Items

1.  **`grid-column-start` / `grid-column-end`**: Determines a grid item's size and location by specifying which grid lines it starts and ends on.
2.  **`grid-row-start` / `grid-row-end`**: Same as above, but for rows.
3.  **`grid-column` / `grid-row` (Shorthand)**: Combines the start and end properties.

    ```css
    .item-1 {
      grid-column: 1 / 3; /* Span from line 1 to line 3 */
      grid-row: 1 / 2;
    }
    ```

4.  **`grid-area`**: Gives an item a name so that it can be placed by a template created with the `grid-template-areas` property.

**Example**: A simple page layout.

```css
.container {
  display: grid;
  grid-template-columns: 1fr 3fr;
  grid-template-rows: auto 1fr auto;
  grid-template-areas:
    "header header"
    "sidebar main"
    "footer footer";
  gap: 10px;
  height: 100vh;
}

.header { grid-area: header; }
.sidebar { grid-area: sidebar; }
.main { grid-area: main; }
.footer { grid-area: footer; }
```

CSS Grid is powerful for overall page layouts, while Flexbox excels at aligning items within a component.

---

---

### Q61: What is the difference between CSS Flexbox and Grid?

**Answer:**

Both CSS Flexbox and Grid are powerful layout models, but they are designed to solve different problems. The primary difference is that **Flexbox is for one-dimensional layouts**, while **Grid is for two-dimensional layouts**.

#### CSS Flexbox (One-Dimensional)

Flexbox is designed to lay out items in a single dimension—either in a row or a column.

*   **Axis**: It works along a single main axis (`flex-direction`).
*   **Content-First**: Its primary strength is distributing space along that axis, making it ideal for aligning items within a container.
*   **Use Cases**: Perfect for component-level layouts, such as navigation bars, form elements, or card components where items are arranged in a line.

**Think of Flexbox as arranging items in a list.**

```css
.flex-container {
  display: flex; /* Lays out children in a row by default */
  justify-content: space-between;
}
```

#### CSS Grid (Two-Dimensional)

Grid is designed for laying out items in two dimensions—rows and columns simultaneously.

*   **Axes**: It works with both a horizontal and a vertical axis at the same time.
*   **Layout-First**: It allows you to define a rigid grid structure and place items within it, giving you precise control over the overall page layout.
*   **Use Cases**: Ideal for the main page layout, such as creating headers, footers, sidebars, and main content areas.

**Think of Grid as arranging items in a spreadsheet.**

```css
.grid-container {
  display: grid;
  grid-template-columns: 1fr 2fr; /* Defines two columns */
  grid-template-rows: auto 1fr;    /* Defines two rows */
}
```

#### Comparison Table

| Feature         | Flexbox                                       | Grid                                              |
| --------------- | --------------------------------------------- | ------------------------------------------------- |
| **Dimensions**  | **One-dimensional** (row or column)           | **Two-dimensional** (rows and columns)            |
| **Primary Use** | Aligning content and distributing space within a container. | Overall page layout.                              |
| **Approach**    | Content-first                                 | Layout-first                                      |
| **Item Sizing** | Items can grow/shrink along the main axis.    | Items are placed into explicitly defined grid cells. |
| **Flexibility** | More flexible for content that changes size.  | More rigid and structured.                        |
| **Best For**    | Components, navigation bars, UI elements.     | Full-page layouts, complex responsive designs.    |

#### Can They Be Used Together?

Yes, and they often should be. A common pattern is to use **Grid for the main page structure** and **Flexbox for the components within that structure**.

**Example**:

1.  Use **Grid** to create a `header`, `main`, and `footer` layout.
2.  Inside the `header`, use **Flexbox** to align the logo and navigation links.

This approach leverages the strengths of both models, resulting in clean, maintainable, and responsive designs.

---

---

### Q62: What is responsive web design and how are media queries used?

**Answer:**

**Responsive Web Design (RWD)** is an approach to web design that makes web pages render well on a variety of devices and window or screen sizes. The goal is to create a single, flexible website that adapts its layout to the viewing environment.

The core principles of RWD are:

1.  **Fluid Grids**: Using relative units like percentages (`%`) or viewport units (`vw`, `vh`) for layout widths, rather than fixed units like pixels (`px`). This allows the layout to stretch or shrink with the browser size.
2.  **Flexible Images**: Sizing images and other media with relative units (like `max-width: 100%;`) to prevent them from overflowing their containers.
3.  **Media Queries**: A CSS feature that allows you to apply styles only when certain conditions about the browser or device environment are met, such as its width, height, or orientation.

#### How Media Queries Work

Media queries are the key to RWD. They allow you to create different layouts for different screen sizes using CSS. A media query consists of a media type and one or more expressions involving media features.

**Syntax**:

```css
@media media-type and (media-feature: value) {
  /* CSS rules to apply when the condition is true */
}
```

*   **`media-type`**: Describes the general category of a device (e.g., `screen`, `print`, `all`).
*   **`media-feature`**: Describes a specific characteristic of the user agent or display (e.g., `width`, `height`, `orientation`).

**Example**: Changing the layout based on screen width.

This is a **mobile-first** approach, where the default styles target mobile devices, and media queries add complexity for larger screens.

```css
/* Default styles for mobile */
.container {
  width: 100%;
}

.sidebar {
  display: none; /* Hide sidebar on small screens */
}

/* Styles for tablets and larger (min-width: 768px) */
@media screen and (min-width: 768px) {
  .container {
    display: flex;
  }

  .sidebar {
    display: block; /* Show sidebar */
    width: 30%;
  }

  .main-content {
    width: 70%;
  }
}

/* Styles for desktops and larger (min-width: 1024px) */
@media screen and (min-width: 1024px) {
  .container {
    max-width: 1200px;
    margin: 0 auto;
  }
}
```

#### The Viewport Meta Tag

For media queries to work correctly on mobile devices, you must include the viewport meta tag in the `<head>` of your HTML document. This tag tells the browser how to control the page's dimensions and scaling.

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

*   `width=device-width`: Sets the width of the page to follow the screen-width of the device.
*   `initial-scale=1.0`: Sets the initial zoom level when the page is first loaded by the browser.

Without this tag, mobile browsers will render the page at a typical desktop screen width and then scale it down, making it unreadable.

---

---

### Q63: What are CSS preprocessors and why are they useful?

**Answer:**

A **CSS preprocessor** is a scripting language that extends the default capabilities of CSS. It allows you to use features that don't exist in plain CSS, such as variables, nesting, mixins, and functions. The preprocessor takes code written in its own syntax and compiles it into standard, browser-readable CSS.

The most popular CSS preprocessors are **Sass (Syntactically Awesome Style Sheets)**, **Less**, and **Stylus**.

#### Why Are They Useful?

CSS preprocessors help make your stylesheets more maintainable, scalable, and organized. They promote DRY (Don't Repeat Yourself) principles and reduce code duplication.

Key features and their benefits include:

1.  **Variables**: Store values (like colors or fonts) that you can reuse throughout your stylesheets. This makes global changes much easier.

    **Sass Example**:
    ```scss
    $primary-color: #3498db;

    .button {
      background-color: $primary-color;
    }

    .link {
      color: $primary-color;
    }
    ```

2.  **Nesting**: Nest your CSS selectors in a way that follows the same visual hierarchy as your HTML. This makes your code more readable and organized.

    **Sass Example**:
    ```scss
    nav {
      ul {
        margin: 0;
        padding: 0;
        list-style: none;

        li { display: inline-block; }

        a {
          text-decoration: none;
        }
      }
    }
    ```

3.  **Mixins**: Reusable blocks of styles that can be included anywhere in your stylesheet. You can even pass arguments to them, making them like functions for CSS.

    **Sass Example**:
    ```scss
    @mixin flex-center {
      display: flex;
      justify-content: center;
      align-items: center;
    }

    .container {
      @include flex-center;
    }
    ```

4.  **Partials and Imports**: Break your CSS into smaller, more manageable files (partials) and then import them into a single main file. This is great for organizing large projects.

    ```scss
    // _variables.scss
    $font-stack: Helvetica, sans-serif;

    // styles.scss
    @import 'variables';

    body {
      font-family: $font-stack;
    }
    ```

5.  **Functions and Logic**: Use built-in functions to manipulate values (e.g., darken or lighten a color) or write your own. You can also use control directives like `@if`, `@for`, and `@each`.

    **Sass Example**:
    ```scss
    .button {
      background-color: #3498db;
      &:hover {
        background-color: darken(#3498db, 10%);
      }
    }
    ```

#### The Compilation Step

Because browsers don't understand preprocessor syntax, you need a **compiler** to convert your `.scss` or `.less` files into a standard `.css` file. This compilation step can be automated with build tools like Webpack, Gulp, or Parcel, or through command-line tools provided by the preprocessors themselves.

---

---

### Q64: What is the difference between `px`, `em`, and `rem` units?

**Answer:**

Choosing the right CSS unit is crucial for creating scalable, maintainable, and accessible web designs. `px`, `em`, and `rem` are three of the most common units for sizing fonts and other elements, each with different behaviors.

#### `px` (Pixels)

*   **Type**: Absolute Unit
*   **Definition**: A pixel is a fixed-size unit that corresponds to one dot on the screen. It is not scalable and is considered an absolute unit because it is not relative to anything else.
*   **Behavior**: `1px` is always `1px`, regardless of any other element's size.
*   **Use Case**: Best used for things that should remain a fixed size, such as `border-width` or when you need pixel-perfect precision. It is generally discouraged for font sizes because it doesn't scale with user preferences, which can be an accessibility issue.

```css
.element {
  font-size: 16px; /* Always 16 pixels */
  border: 1px solid black;
}
```

#### `em` (Ep-Mutton)

*   **Type**: Relative Unit
*   **Definition**: The `em` unit is relative to the **`font-size` of its direct parent element**.
*   **Behavior**: If a parent has `font-size: 16px;`, then `1em` for a child element will be `16px`, `2em` will be `32px`, and so on. This can lead to a compounding effect, as `em` units on nested elements are relative to their parent's font size, which might also be set in `em`.
*   **Use Case**: Useful when you want an element's size (like `padding` or `margin`) to scale relative to the font size of its parent. This is common in modular components.

```html
<div style="font-size: 20px;">
  <p style="font-size: 1.2em;">This text is 24px (20px * 1.2)</p>
</div>
```

#### `rem` (Root Em)

*   **Type**: Relative Unit
*   **Definition**: The `rem` unit is relative to the **`font-size` of the root element** (the `<html>` element).
*   **Behavior**: It avoids the compounding issue of `em` units. No matter how deeply nested an element is, `1rem` is always equal to the font size of the `<html>` element. The browser's default is typically `16px`.
*   **Use Case**: The modern standard for font sizes and often for spacing (`padding`, `margin`). It allows users to change their browser's base font size for accessibility, and the entire layout will scale predictably.

```css
html {
  font-size: 16px; /* Browser default */
}

.title {
  font-size: 2rem; /* 32px */
}

.subtitle {
  font-size: 1.5rem; /* 24px */
}
```

#### Comparison Table

| Unit | Type      | Relative To                               | Compounding? | Best For                                       |
| :--- | :-------- | :---------------------------------------- | :----------- | :--------------------------------------------- |
| `px` | Absolute  | N/A (fixed)                               | No           | Borders, fixed-size elements.                  |
| `em` | Relative  | Parent element's `font-size`              | Yes          | Sizing within a component that should scale together. |
| `rem`| Relative  | Root (`<html>`) element's `font-size`     | No           | Global font sizes, margins, and paddings.      |

**Best Practice**: Use `rem` for font sizes and spacing to ensure your layout is scalable and accessible. Use `em` for properties that should be relative to an element's own font size. Use `px` sparingly for elements that must have a fixed size.

---

---

### Q65: What is the `z-index` property and how does stacking context work?

**Answer:**

The `z-index` property in CSS controls the vertical stacking order of positioned elements (i.e., elements with a `position` value other than `static`). An element with a higher `z-index` will appear in front of an element with a lower `z-index`.

However, `z-index` only works within the same **stacking context**. This is a crucial concept to understand why `z-index` sometimes doesn't behave as expected.

#### What is a Stacking Context?

A stacking context is a three-dimensional conceptualization of HTML elements along an imaginary z-axis, perpendicular to the screen. Within a stacking context, child elements are stacked according to specific rules, and `z-index` values are only meaningful within that context.

A new stacking context can be created by any element that has:

1.  A `position` value of `absolute` or `relative` and a `z-index` value other than `auto`.
2.  A `position` value of `fixed` or `sticky`.
3.  An `opacity` value less than `1`.
4.  A `transform`, `filter`, or `perspective` value other than `none`.
5.  A `mix-blend-mode` value other than `normal`.

#### How Stacking Works

When a new stacking context is formed, all of its child elements are contained within it. This means that if an element inside Stacking Context A has a `z-index` of 999, and an element inside Stacking Context B has a `z-index` of 1, the element in Context A can **never** appear on top of the element in Context B if Context B itself has a higher stack level.

**Stacking Order Within a Context**:

Within a single stacking context, elements are stacked in the following order, from back to front:

1.  The background and borders of the element forming the stacking context.
2.  Positioned elements with a **negative `z-index`** (higher values are closer to the front).
3.  Non-positioned, block-level elements in the order they appear in the HTML.
4.  Positioned elements with a `z-index` of `auto` or `0`.
5.  Positioned elements with a **positive `z-index`** (higher values are closer to the front).

**Example**:

```html
<div class="parent-1" style="position: relative; z-index: 1;">
  <div class="child-1" style="position: absolute; z-index: 999; background: lightblue;">
    Child 1 (z-index: 999)
  </div>
</div>

<div class="parent-2" style="position: relative; z-index: 2;">
  <div class="child-2" style="position: absolute; z-index: 1; background: lightcoral;">
    Child 2 (z-index: 1)
  </div>
</div>
```

Even though `child-1` has a much higher `z-index` (999) than `child-2` (1), **`parent-2` will appear on top** because its stacking context (`z-index: 2`) is higher than `parent-1`'s (`z-index: 1`). The `z-index` of the children is only compared within their respective parent's stacking context.

#### Key Takeaways

*   `z-index` only applies to **positioned elements**.
*   `z-index` values are only compared **within the same stacking context**.
*   A new stacking context can be formed by various properties, not just `position` and `z-index`.
*   To fix `z-index` issues, you often need to adjust the `z-index` or `position` of a parent element, not just the element you're trying to move.

---

---

### Q66: What are pseudo-classes and pseudo-elements in CSS?

**Answer:**

Pseudo-classes and pseudo-elements are CSS selectors that allow you to style elements based on state or to style specific parts of an element, respectively. They both extend the functionality of regular CSS selectors.

#### Pseudo-Classes

A **pseudo-class** is used to define a special state of an element. It's like applying a class to an element when a certain condition is met, but without any JavaScript or changes to the HTML.

*   **Syntax**: A single colon (`:`), e.g., `:hover`.
*   **Purpose**: To style an element based on its state or its relationship to other elements.

**Common Pseudo-Classes:**

*   `:hover`: Selects an element when the user mouses over it.
*   `:focus`: Selects an element that has received focus (e.g., an input field that is clicked into).
*   `:active`: Selects an element that is currently being activated by the user (e.g., a button being clicked).
*   `:visited`: Selects a link that the user has already visited.
*   `:first-child`: Selects the first element among a group of siblings.
*   `:last-child`: Selects the last element among a group of siblings.
*   `:nth-child(n)`: Selects an element based on its position among its siblings (e.g., `:nth-child(2n)` selects all even elements).

**Example**:

```css
/* Style a button on hover */
button:hover {
  background-color: #0056b3;
}

/* Style an input field when it's in focus */
input:focus {
  border-color: #007bff;
  box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
}

/* Style every odd list item */
li:nth-child(odd) {
  background-color: #f2f2f2;
}
```

#### Pseudo-Elements

A **pseudo-element** is used to style a specific part of an element. It's like adding a new, virtual element to the DOM that you can style independently.

*   **Syntax**: A double colon (`::`), e.g., `::before`. (Note: A single colon was used in older CSS versions and is still supported for backward compatibility, but `::` is the standard for pseudo-elements in CSS3).
*   **Purpose**: To style a specific part of an element's content.

**Common Pseudo-Elements:**

*   `::before`: Creates a pseudo-element that is the first child of the selected element. Often used to add cosmetic content.
*   `::after`: Creates a pseudo-element that is the last child of the selected element.
*   `::first-letter`: Selects the first letter of a block-level element.
*   `::first-line`: Selects the first line of a block-level element.
*   `::selection`: Selects the portion of an element that is currently highlighted by the user.
*   `::placeholder`: Selects the placeholder text in an input field.

**Example**:

```css
/* Add a decorative quote before a blockquote */
blockquote::before {
  content: '"';
  font-size: 3em;
  color: #ccc;
}

/* Style the first letter of every paragraph */
p::first-letter {
  font-size: 200%;
  font-weight: bold;
  color: #007bff;
}

/* Change the background color of selected text */
::selection {
  background: #ffc107;
  color: #333;
}
```

#### Comparison Table

| Feature          | Pseudo-Class (`:`)                               | Pseudo-Element (`::`)                                |
| ---------------- | ------------------------------------------------ | ---------------------------------------------------- |
| **Purpose**      | Styles an element based on its state.            | Styles a specific part of an element.                |
| **Analogy**      | A "fake" class that is dynamically applied.    | A "fake" element inserted into the DOM.            |
| **Syntax**       | Single colon (`:hover`)                          | Double colon (`::before`)                            |
| **Example Use**  | Styling a link on hover (`a:hover`).             | Adding an icon before a link (`a::before`).          |
| **DOM Impact**   | Does not create new elements.                    | Acts as if it's creating a new element.              |

---

---

### Q67: What is the difference between `==` and `===` in JavaScript?

**Answer:**

The difference between the `==` (loose equality) and `===` (strict equality) operators is a fundamental concept in JavaScript. The key distinction lies in how they handle data types when comparing values.

#### Strict Equality (`===`)

The strict equality operator, also known as the identity operator, compares two values for equality **without performing any type conversion**.

*   **How it works**: It returns `true` only if both the **value** and the **data type** are the same.
*   **Best Practice**: This is the recommended comparison operator to use in almost all cases because it is predictable and avoids subtle bugs related to type coercion.

**Example**:

```javascript
1 === 1;       // true (number vs. number, same value)
'1' === 1;     // false (string vs. number)
'1' === '1';   // true (string vs. string, same value)

true === 1;    // false (boolean vs. number)
null === undefined; // false (null vs. undefined)
0 === -0;      // true
NaN === NaN;   // false (NaN is not equal to anything, including itself)
```

#### Loose Equality (`==`)

The loose equality operator, also known as the equality operator, compares two values for equality **after converting both values to a common type** (a process called type coercion).

*   **How it works**: If the two values have different types, it will attempt to convert one or both values to a matching type before making the comparison.
*   **Disadvantages**: The rules for type coercion can be complex and non-obvious, leading to unexpected results and making code harder to debug.

**Example**:

```javascript
1 == 1;        // true
'1' == 1;      // true (string '1' is coerced to number 1)
'1' == '1';    // true

true == 1;     // true (boolean true is coerced to number 1)
false == 0;    // true (boolean false is coerced to number 0)

null == undefined; // true (this is a special case in the language spec)
'' == false;   // true (empty string is coerced to 0, false is coerced to 0)
```

#### Comparison Table

| Feature         | Loose Equality (`==`)                               | Strict Equality (`===`)                              |
| --------------- | --------------------------------------------------- | ---------------------------------------------------- |
| **Comparison**  | Compares **value** only.                            | Compares both **value** and **type**.                |
| **Type Coercion** | **Performs** type coercion if types are different.  | **Does not perform** any type coercion.              |
| **Predictability**| Can lead to unexpected results.                     | Predictable and safe.                                |
| **Recommendation**| Avoid unless you have a specific reason for it.     | **Always prefer** this operator.                     |

#### Why You Should Almost Always Use `===`

Using `===` makes your code more robust, readable, and easier to maintain. It prevents bugs that can arise from JavaScript's automatic type conversions. By checking both type and value, you are being more explicit about your intentions, which leads to fewer surprises.

The only time you might consider using `==` is when you specifically need to check for `null` or `undefined` at the same time, as `x == null` will be `true` if `x` is either `null` or `undefined`, and `false` otherwise. However, even this can be written more explicitly if needed.

---

---

### Q68: What is hoisting in JavaScript?

**Answer:**

Hoisting is a JavaScript mechanism where variable and function declarations are moved to the top of their containing scope (either the global scope or a function scope) before code execution. It's important to understand that only the **declarations** are hoisted, not the **initializations**.

This means you can use a variable or call a function before it has been declared in your code.

#### Hoisting with `var`

Variables declared with `var` are hoisted to the top of their scope and are initialized with the value `undefined`.

**Example**:

```javascript
console.log(myVar); // Outputs: undefined

var myVar = 5;

console.log(myVar); // Outputs: 5
```

**How the engine sees it**:

```javascript
var myVar; // Declaration is hoisted, initialized to undefined

console.log(myVar); // Reads the undefined value

myVar = 5; // Initialization happens here

console.log(myVar); // Reads the new value
```

#### Hoisting with `let` and `const`

Variables declared with `let` and `const` are also hoisted, but they are not initialized. They are in a state called the **Temporal Dead Zone (TDZ)** from the start of the block until the declaration is encountered.

Accessing a `let` or `const` variable before its declaration results in a `ReferenceError`.

**Example**:

```javascript
console.log(myLet); // Throws ReferenceError: Cannot access 'myLet' before initialization

let myLet = 10;
```

**Temporal Dead Zone (TDZ)**:
The TDZ is the period between entering scope and the variable declaration. During this time, the variable cannot be accessed. This helps to avoid bugs by making it an error to use a variable before it has been declared.

#### Function Hoisting

Function declarations are fully hoisted, meaning both the declaration and the definition are moved to the top. This allows you to call a function before you've declared it.

**Example (Function Declaration)**:

```javascript
hoistedFunction(); // Outputs: "Hello, world!"

function hoistedFunction() {
  console.log("Hello, world!");
}
```

However, **function expressions** are not hoisted in the same way. If a function expression is assigned to a `var` variable, the variable declaration is hoisted, but the function body is not. If assigned to `let` or `const`, it is subject to the TDZ.

**Example (Function Expression)**:

```javascript
console.log(notHoisted); // Outputs: undefined
notHoisted(); // Throws TypeError: notHoisted is not a function

var notHoisted = function() {
  console.log("This will not work.");
};
```

#### Summary Table

| Keyword              | Hoisted? | Initialized?      | Temporal Dead Zone (TDZ)? | Scope         |
| -------------------- | -------- | ----------------- | ------------------------- | ------------- |
| `var`                | Yes      | `undefined`       | No                        | Function      |
| `let`                | Yes      | Not initialized   | Yes                       | Block         |
| `const`              | Yes      | Not initialized   | Yes                       | Block         |
| `function` (decl.)   | Yes      | The function itself | No                        | Function      |
| `function` (expr.)   | Depends on `var`/`let`/`const` | Depends on `var`/`let`/`const` | Depends on `let`/`const` | Depends on `var`/`let`/`const` |

**Best Practice**: Always declare your variables and functions at the top of their scope to avoid confusion related to hoisting. Using `let` and `const` over `var` is recommended as it leads to more predictable code and helps prevent common errors.

---

---

### Q69: What is the difference between `null` and `undefined` in JavaScript?

**Answer:**

In JavaScript, both `null` and `undefined` represent the absence of a value, but they are used in different contexts and have distinct meanings.

#### `undefined`

`undefined` is a primitive value that indicates that a variable has been declared but has not yet been assigned a value. It is the default value for:

*   Variables that are declared but not initialized.
*   Function arguments that are not provided.
*   The return value of functions that do not explicitly return a value.
*   Properties of an object that do not exist.

**Example**:

```javascript
let myVar; // Declared but not initialized
console.log(myVar); // Outputs: undefined

function greet(name) {
  console.log(`Hello, ${name}`);
}
greet(); // Outputs: "Hello, undefined"

const obj = { a: 1 };
console.log(obj.b); // Outputs: undefined
```

#### `null`

`null` is also a primitive value, but it represents the **intentional absence** of any object value. It is a value that can be assigned to a variable to explicitly indicate that it has no value.

Think of it as a placeholder for an object that is expected to be assigned later, or as an explicit signal that there is no object to return.

**Example**:

```javascript
let user = null; // Explicitly set to null

// Later, this might be assigned an object
user = { name: 'Alice' };

function findUser(id) {
  if (id === 1) {
    return { name: 'Bob' };
  }
  return null; // Explicitly return null if no user is found
}

console.log(findUser(2)); // Outputs: null
```

#### Key Differences and Comparison

| Feature         | `undefined`                                       | `null`                                              |
| --------------- | ------------------------------------------------- | --------------------------------------------------- |
| **Meaning**     | A variable has been declared but not assigned a value. | An intentional absence of any value.                |
| **Type**        | `typeof undefined` is `"undefined"`.              | `typeof null` is `"object"` (a historical bug).     |
| **Origin**      | Usually set by the JavaScript engine automatically. | Usually set by the developer intentionally.         |
| **Math Ops**    | `undefined + 1` results in `NaN`.                 | `null + 1` results in `1` (`null` is coerced to `0`).|

#### Equality Checks

When comparing `null` and `undefined`, the results differ based on the equality operator used:

*   **Loose Equality (`==`)**: `null == undefined` returns `true`. This is a special case where they are considered equal.
*   **Strict Equality (`===`)**: `null === undefined` returns `false` because they are of different types.

```javascript
console.log(null == undefined);  // true
console.log(null === undefined); // false
```

**Best Practice**: Use `null` to explicitly signal "no value" for a variable or return value. Rely on `undefined` as the default state for uninitialized variables. When checking for either, be mindful of the difference between `==` and `===`.

---

---

### Q70: What is a closure in JavaScript?

**Answer:**

A closure is the combination of a function and the lexical environment within which that function was declared. In simpler terms, a closure gives you access to an outer function's scope from an inner function, even after the outer function has finished executing.

This means the inner function "remembers" the environment (the variables, constants, and arguments) in which it was created.

#### How Closures Work

Three key ingredients create a closure:

1.  **An outer function** that contains an inner function.
2.  **An inner function** that makes use of variables from the outer function.
3.  **The outer function returns the inner function**.

When the outer function is called, it creates an environment. When it returns the inner function, that inner function maintains a reference to its lexical environment, preventing it from being garbage collected.

**Example: A Simple Counter**

```javascript
function createCounter() {
  let count = 0; // This variable is part of the closure's environment

  // This inner function is a closure
  return function() {
    count++;
    console.log(count);
  };
}

const counter1 = createCounter(); // counter1 is now a function that has its own private 'count' variable
const counter2 = createCounter(); // counter2 has a completely separate 'count' variable

counter1(); // Outputs: 1
counter1(); // Outputs: 2

counter2(); // Outputs: 1 (independent of counter1)
console.log(typeof count); // Outputs: "undefined". The 'count' variable is not accessible in the global scope.
```

In this example, `createCounter` is called twice, creating two separate execution environments. Each of the returned functions (`counter1` and `counter2`) forms a closure, each with its own private `count` variable that persists across calls.

#### Common Use Cases for Closures

1.  **Data Privacy and Encapsulation**: Closures are the primary way to create private variables and methods in JavaScript, mimicking the behavior of private members in object-oriented programming. The `count` variable in the example above is effectively private.

2.  **Event Handlers and Callbacks**: Closures are essential for event handlers, especially in loops, to capture the correct value of a variable at the time the handler is created.

    ```javascript
    for (var i = 1; i <= 3; i++) {
      // Using a closure to capture the value of 'i' for each timeout
      (function(j) {
        setTimeout(function() {
          console.log(j);
        }, j * 1000);
      })(i);
    }
    // Outputs: 1 (after 1s), 2 (after 2s), 3 (after 3s)
    // Without the closure, it would output 4, 4, 4.
    // Note: This specific problem is more easily solved with `let` in modern JS.
    ```

3.  **Currying and Partial Application**: Closures enable functional programming techniques like currying, where a function that takes multiple arguments is transformed into a sequence of functions that each take a single argument.

    ```javascript
    function multiply(a) {
      return function(b) {
        return a * b;
      };
    }

    const multiplyByTwo = multiply(2);
    console.log(multiplyByTwo(5)); // Outputs: 10
    ```

#### Key Takeaway

A closure is a function that remembers the variables from the scope where it was created. It's a fundamental concept in JavaScript that enables powerful patterns like data privacy and functional programming.

---

---

### Q71: Explain the `this` keyword in JavaScript.

**Answer:**

The `this` keyword in JavaScript is a reference to an object. The object it refers to depends on how and where `this` is called. Its value is determined at the time a function is executed (runtime binding), not when it is defined.

Understanding the context of `this` is crucial for writing predictable JavaScript code. Here are the primary rules for how its value is determined:

#### 1. Global Context

In the global execution context (outside of any function), `this` refers to the global object. In a web browser, the global object is `window`.

```javascript
console.log(this); // In a browser, this will log the Window object
```

In strict mode (`'use strict'`), `this` in the global context remains the global object, but within a function, it's `undefined` if not set by the call.

#### 2. Function Context (Method Invocation)

When a function is called as a method of an object, `this` refers to the object the method is called on.

```javascript
const person = {
  name: 'Alice',
  greet: function() {
    console.log(`Hello, my name is ${this.name}.`);
  }
};

person.greet(); // Outputs: "Hello, my name is Alice." (this refers to 'person')
```

This is the most common and straightforward use of `this`.

#### 3. Function Context (Simple Function Call)

When a function is called as a standalone function (not as a method of an object), `this` will refer to the global object (`window` in browsers). This can lead to unexpected behavior.

```javascript
function showName() {
  console.log(this.name);
}

const person = { name: 'Bob', showName: showName };
const name = 'Global Name';

person.showName(); // Outputs: "Bob" (this is 'person')

const standaloneShowName = person.showName;
standaloneShowName(); // Outputs: "Global Name" (this is 'window')
```

In **strict mode**, `this` will be `undefined` in this case to prevent accidental modification of the global object.

#### 4. Constructor Context (`new` Keyword)

When a function is used as a constructor with the `new` keyword, `this` refers to the newly created instance of the object.

```javascript
function Person(name) {
  // this = {}; (implicitly created)
  this.name = name;
  // return this; (implicitly returned)
}

const alice = new Person('Alice');
console.log(alice.name); // Outputs: "Alice" (this refers to the 'alice' instance)
```

#### 5. Explicit Binding (`call`, `apply`, `bind`)

You can explicitly set the value of `this` using these three methods of the `Function.prototype`.

*   **`call(thisArg, arg1, arg2, ...)`**: Invokes the function immediately with a specified `this` value and arguments provided individually.
*   **`apply(thisArg, [argsArray])`**: Invokes the function immediately with a specified `this` value and arguments provided as an array.
*   **`bind(thisArg)`**: Returns a **new function** where `this` is permanently bound to the provided value. It does not invoke the function immediately.

```javascript
function introduce(greeting, punctuation) {
  console.log(`${greeting}, I'm ${this.name}${punctuation}`);
}

const person = { name: 'Charlie' };

introduce.call(person, 'Hi', '!');   // Outputs: "Hi, I'm Charlie!"
introduce.apply(person, ['Hey', '.']); // Outputs: "Hey, I'm Charlie."

const boundIntroduce = introduce.bind(person);
boundIntroduce('Hello', '...'); // Outputs: "Hello, I'm Charlie..."
```

#### 6. Arrow Functions

Arrow functions (`=>`) do not have their own `this` context. Instead, they inherit `this` from their enclosing (lexical) scope. This behavior is different from all other function types and is extremely useful for callbacks and methods that need to access the parent object's context.

```javascript
const person = {
  name: 'David',
  hobbies: ['reading', 'coding'],
  showHobbies: function() {
    this.hobbies.forEach(hobby => {
      // 'this' here is lexically inherited from showHobbies
      // so it correctly refers to the 'person' object.
      console.log(`${this.name} likes ${hobby}.`);
    });
  }
};

person.showHobbies();
// Outputs:
// "David likes reading."
// "David likes coding."
```
If a regular function were used inside `forEach`, `this` would refer to the global object (or be `undefined` in strict mode).

#### Summary Table

| Invocation Type        | `this` refers to...                                |
| ---------------------- | -------------------------------------------------- |
| **Global**             | The global object (`window`)                       |
| **Method** (`obj.fn()`)  | The object (`obj`)                                 |
| **Simple Call** (`fn()`) | The global object (`window`) or `undefined` (strict) |
| **Constructor** (`new fn()`) | The newly created instance                       |
| **`call`/`apply`/`bind`** | The object explicitly passed as an argument        |
| **Arrow Function**     | The `this` of its surrounding lexical scope        |

---

---

### Q72: What is prototypal inheritance in JavaScript?

**Answer:**

Prototypal inheritance is a fundamental concept in JavaScript where objects can inherit properties and methods from other objects. Unlike classical inheritance (found in languages like Java or C++), JavaScript does not have classes in the traditional sense. Instead, it uses a **prototype chain**.

Every JavaScript object has a private property which holds a link to another object called its **prototype**. That prototype object has a prototype of its own, and so on, until an object is reached with `null` as its prototype. This series of linked objects is the prototype chain.

When you try to access a property on an object, the JavaScript engine first checks if the property exists on the object itself. If not, it looks at the object's prototype. If it's still not found, it continues up the prototype chain until it either finds the property or reaches the end of the chain (`null`).

#### How to Implement Prototypal Inheritance

There are several ways to set up prototypal inheritance in JavaScript.

**1. Using `Object.create()`**

This is the modern and recommended way to create an object with a specific prototype.

```javascript
// The object we want to inherit from
const animal = {
  makeSound: function() {
    console.log('Some generic sound');
  }
};

// Create a new object 'dog' that inherits from 'animal'
const dog = Object.create(animal);
dog.breed = 'Golden Retriever';

dog.makeSound(); // Outputs: "Some generic sound" (inherited from animal)
console.log(dog.breed); // Outputs: "Golden Retriever" (own property)

// The prototype of 'dog' is the 'animal' object
console.log(Object.getPrototypeOf(dog) === animal); // true
```

**2. Using Constructor Functions**

This was the traditional way to mimic classes before ES6. The link between instances and the prototype is established through the constructor's `prototype` property.

```javascript
// Constructor function for Animal
function Animal(name) {
  this.name = name;
}

// Add a method to the Animal's prototype
Animal.prototype.makeSound = function() {
  console.log('Some generic sound');
};

// Constructor function for Dog
function Dog(name, breed) {
  // Call the parent constructor to set the 'name' property
  Animal.call(this, name);
  this.breed = breed;
}

// Set up the prototype chain: Dog.prototype inherits from Animal.prototype
Dog.prototype = Object.create(Animal.prototype);
// Restore the constructor property
Dog.prototype.constructor = Dog;

// Add a method specific to Dog
Dog.prototype.bark = function() {
  console.log('Woof!');
};

const myDog = new Dog('Buddy', 'Labrador');

myDog.makeSound(); // Outputs: "Some generic sound" (inherited from Animal.prototype)
myDog.bark();      // Outputs: "Woof!"
console.log(myDog.name); // Outputs: "Buddy"
```

**3. Using ES6 `class` Syntax**

ES6 introduced the `class` keyword, which provides a much cleaner and more familiar syntax for setting up prototypal inheritance. It is important to remember that this is **syntactic sugar** over the existing prototypal inheritance mechanism; it does not introduce a new inheritance model.

```javascript
class Animal {
  constructor(name) {
    this.name = name;
  }

  makeSound() {
    console.log('Some generic sound');
  }
}

class Dog extends Animal {
  constructor(name, breed) {
    super(name); // Call the parent constructor
    this.breed = breed;
  }

  bark() {
    console.log('Woof!');
  }
}

const myDog = new Dog('Rex', 'German Shepherd');

myDog.makeSound(); // Outputs: "Some generic sound"
myDog.bark();      // Outputs: "Woof!"
console.log(myDog.name); // Outputs: "Rex"
```

#### Key Takeaways

*   JavaScript uses **prototypal inheritance**, not classical inheritance.
*   Objects inherit directly from other objects via the **prototype chain**.
*   When accessing a property, JavaScript searches up the prototype chain until the property is found or the chain ends.
*   ES6 `class` syntax is the modern way to work with prototypes, but it's syntactic sugar over the underlying prototypal mechanism.

---

---

### Q73: What is the difference between Promises and Callbacks?

**Answer:**

Both callbacks and Promises are used to handle asynchronous operations in JavaScript. However, Promises were introduced in ES6 to solve several problems associated with the traditional callback-based approach, most notably "Callback Hell."

#### Callbacks

A callback is a function that is passed as an argument to another function and is executed after the outer function has completed its operation. This is the classic way of handling asynchronous code.

**How it works**: You provide one function to handle success and another to handle errors.

**Example (Callback-based)**:

```javascript
function fetchData(url, successCallback, errorCallback) {
  // Simulate a network request
  setTimeout(() => {
    if (url) {
      const data = { message: 'Data fetched successfully' };
      successCallback(data);
    } else {
      const error = new Error('Invalid URL');
      errorCallback(error);
    }
  }, 1000);
}

// Usage
fetchData(
  'https://api.example.com/data',
  (data) => console.log('Success:', data.message),
  (error) => console.error('Error:', error.message)
);
```

**Problems with Callbacks**:

1.  **Callback Hell (Pyramid of Doom)**: When you need to perform multiple sequential asynchronous operations, you end up nesting callbacks inside each other, leading to code that is hard to read, reason about, and maintain.

    ```javascript
    // Pyramid of Doom
    asyncOp1(data1 => {
      asyncOp2(data2 => {
        asyncOp3(data3 => {
          // ...and so on
        });
      });
    });
    ```

2.  **Inversion of Control**: You pass your callback function to another function, trusting that it will be called correctly (e.g., only once, with the right arguments). You lose control over its execution.

#### Promises

A Promise is an object that represents the eventual completion (or failure) of an asynchronous operation and its resulting value. A Promise can be in one of three states:

*   **Pending**: The initial state; neither fulfilled nor rejected.
*   **Fulfilled**: The operation completed successfully.
*   **Rejected**: The operation failed.

**How it works**: A function returns a Promise object. You can then attach callbacks to this object using the `.then()` (for fulfillment) and `.catch()` (for rejection) methods.

**Example (Promise-based)**:

```javascript
function fetchData(url) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (url) {
        const data = { message: 'Data fetched successfully' };
        resolve(data); // Fulfill the promise
      } else {
        const error = new Error('Invalid URL');
        reject(error); // Reject the promise
      }
    }, 1000);
  });
}

// Usage
fetchData('https://api.example.com/data')
  .then(data => {
    console.log('Success:', data.message);
  })
  .catch(error => {
    console.error('Error:', error.message);
  });
```

**Advantages of Promises**:

1.  **Readability and Chaining**: Promises allow you to chain asynchronous operations in a flat, sequential manner, avoiding the pyramid of doom.

    ```javascript
    asyncOp1()
      .then(result1 => asyncOp2(result1))
      .then(result2 => asyncOp3(result2))
      .then(result3 => console.log('Done!'))
      .catch(error => console.error(error));
    ```

2.  **Better Error Handling**: You can use a single `.catch()` at the end of the chain to handle any error that occurs in any of the preceding steps.

3.  **Control is not Inverted**: You receive a Promise object and decide when and how to handle its result. The control remains with your code.

#### Comparison Table

| Feature              | Callbacks                                          | Promises                                             |
| -------------------- | -------------------------------------------------- | ---------------------------------------------------- |
| **Style**            | Nested, pyramid-like structure (Callback Hell).    | Chainable, linear structure (`.then()`).             |
| **Readability**      | Poor for complex operations.                       | Excellent, easy to follow.                           |
| **Error Handling**   | Error callback for each operation.                 | Centralized error handling with `.catch()`.          |
| **Control Flow**     | Inversion of Control: you pass your function away. | You get a return value (the Promise) to work with.   |
| **Composition**      | Difficult to compose multiple operations.          | Easy to compose with methods like `Promise.all()`.   |

**Conclusion**: While callbacks are a fundamental pattern, Promises provide a more robust, readable, and maintainable way to handle asynchronous code in modern JavaScript. The introduction of `async/await` in ES2017 builds on top of Promises, making asynchronous code look and feel even more synchronous and further improving readability.

---

---

### Q74: What is `async/await` and how does it work?

**Answer:**

`async/await` is a modern JavaScript feature (introduced in ES2017) that provides syntactic sugar on top of Promises, making asynchronous code easier to write and read. It allows you to write asynchronous code that looks and behaves like synchronous code, thus avoiding the need for long `.then()` chains.

#### The `async` Keyword

The `async` keyword is used to declare an **asynchronous function**. When a function is declared with `async`, it automatically does two things:

1.  It ensures that the function always returns a Promise.
2.  If the function explicitly returns a value, that value will be wrapped in a resolved Promise (e.g., `return 42` becomes `Promise.resolve(42)`).

```javascript
async function myFunc() {
  return 'Hello, world!';
}

myFunc().then(value => console.log(value)); // Outputs: "Hello, world!"
```

#### The `await` Keyword

The `await` keyword can **only be used inside an `async` function**. It pauses the execution of the `async` function until a Promise is settled (either fulfilled or rejected).

*   If the Promise is **fulfilled**, `await` returns the fulfilled value.
*   If the Promise is **rejected**, `await` throws the rejected value (the error).

This allows you to assign the result of a Promise to a variable directly, just as you would with synchronous code.

**Example: From `.then()` to `async/await`**

Let's take a Promise-based function:

```javascript
function fetchData() {
  return new Promise(resolve => {
    setTimeout(() => resolve('Data has been fetched!'), 1000);
  });
}
```

**Using `.then()` chains:**

```javascript
function processData() {
  fetchData()
    .then(data => {
      console.log(data);
      return fetchData(); // another async operation
    })
    .then(data2 => {
      console.log(data2);
    });
}
```

**Using `async/await`:**

```javascript
async function processDataWithAsync() {
  console.log('Fetching data...');
  const data = await fetchData(); // Pauses here until the promise resolves
  console.log(data); // Runs after the promise is fulfilled

  console.log('Fetching data again...');
  const data2 = await fetchData();
  console.log(data2);
  
  console.log('All done!');
}

processDataWithAsync();
```

As you can see, the `async/await` version is much more linear and readable.

#### Error Handling with `try...catch`

One of the most significant advantages of `async/await` is that it allows you to use standard `try...catch` blocks for error handling, just like with synchronous code. This is often cleaner than the `.catch()` method used with Promises.

```javascript
async function fetchAndProcess() {
  try {
    const response = await fetch('https://api.invalid-url.com/data');
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    console.log(data);
  } catch (error) {
    // Catches both network errors and thrown errors
    console.error('Failed to fetch data:', error);
  }
}
```

#### Key Takeaways

*   `async/await` is syntactic sugar for Promises.
*   `async` functions always return a Promise.
*   `await` pauses the execution of an `async` function until a Promise settles.
*   `await` can only be used inside `async` functions.
*   Error handling is done with standard `try...catch` blocks.
*   It dramatically improves the readability and maintainability of asynchronous code.

---

---

### Q75: What is the Event Loop in JavaScript?

**Answer:**

The Event Loop is a fundamental concept in JavaScript that enables its non-blocking, asynchronous behavior. JavaScript is single-threaded, meaning it can only execute one piece of code at a time. The Event Loop is the mechanism that allows JavaScript to perform long-running tasks (like network requests or timers) without freezing the main thread, ensuring a smooth user experience.

To understand the Event Loop, you need to know its key components:

1.  **Call Stack**: A data structure that keeps track of function calls. When a function is called, it's pushed onto the stack. When it returns, it's popped off. JavaScript executes whatever is on top of the stack.

2.  **Web APIs / Node.js APIs**: These are APIs provided by the browser (or Node.js) that handle asynchronous operations (e.g., `setTimeout`, `fetch`, DOM events). When an async operation is initiated, it's handed off to these APIs, freeing up the Call Stack.

3.  **Callback Queue (or Task Queue)**: When an asynchronous operation completes, its callback function is placed in the Callback Queue. These are considered **macrotasks**.

4.  **Microtask Queue**: This queue is for callbacks from Promises (`.then()`, `.catch()`, `.finally()`) and other microtasks like `queueMicrotask()` and `MutationObserver`. The Microtask Queue has a **higher priority** than the Callback Queue.

#### How it Works

The process follows a continuous loop:

1.  Code is executed from the Call Stack. If it's an asynchronous operation, it's passed to a Web API.
2.  The Event Loop constantly checks if the **Call Stack is empty**.
3.  If the Call Stack is empty, the Event Loop first checks the **Microtask Queue**.
4.  It executes **all** available microtasks in the Microtask Queue, one by one, until the queue is empty. If these microtasks create new microtasks, those are also executed before moving on.
5.  Once the Microtask Queue is empty, the Event Loop checks the **Callback Queue (Macrotask Queue)**.
6.  It takes the **oldest** task (one macrotask) from the Callback Queue, pushes it onto the Call Stack for execution.
7.  The loop repeats from step 1.

**Example of Execution Order:**

```javascript
console.log('1. Start');

setTimeout(() => {
  console.log('2. setTimeout (Macrotask)');
}, 0);

Promise.resolve().then(() => {
  console.log('3. Promise (Microtask)');
});

console.log('4. End');
```

**Execution Order and Output:**

1.  `'1. Start'` is logged. `setTimeout` is sent to the Web API. `Promise.resolve()` puts its `.then()` callback into the Microtask Queue.
2.  `'4. End'` is logged.
3.  The initial script is done, so the Call Stack is now empty.
4.  The Event Loop checks the **Microtask Queue**. It finds the Promise callback and executes it. `'3. Promise (Microtask)'` is logged.
5.  The Microtask Queue is now empty. The Event Loop checks the **Callback Queue**.
6.  It finds the `setTimeout` callback and executes it. `'2. setTimeout (Macrotask)'` is logged.

**Final Output:**

```
1. Start
4. End
3. Promise (Microtask)
2. setTimeout (Macrotask)
```

#### Key Takeaway

The Event Loop is the reason JavaScript can be non-blocking. It orchestrates the execution of code between the Call Stack, Web APIs, and the different task queues. The most important rule to remember is that **microtasks always have priority and are executed completely before any single macrotask**.

---

---

### Q76: What are the differences between `var`, `let`, and `const`?

**Answer:**

In JavaScript, `var`, `let`, and `const` are used for variable declaration, but they differ in terms of scope, hoisting, and mutability. The introduction of `let` and `const` in ES6 addressed common issues associated with `var`.

#### 1. Scope

*   **`var`**: Has **function scope**. A variable declared with `var` is accessible anywhere within the function it's declared in, regardless of block. If declared outside any function, it has global scope.
*   **`let` and `const`**: Have **block scope**. They are only accessible within the block (`{...}`) in which they are defined. This is generally more predictable and helps avoid bugs.

**Example:**

```javascript
function scopeTest() {
  if (true) {
    var varVariable = 'I am var'; // function scope
    let letVariable = 'I am let'; // block scope
    const constVariable = 'I am const'; // block scope
  }
  console.log(varVariable);   // 'I am var'
  // console.log(letVariable);   // ReferenceError: letVariable is not defined
  // console.log(constVariable); // ReferenceError: constVariable is not defined
}
scopeTest();
```

#### 2. Hoisting

Hoisting is JavaScript's behavior of moving declarations to the top of their scope before code execution.

*   **`var`**: Declarations are hoisted and initialized with `undefined`. You can access a `var` variable before it's declared without an error, but its value will be `undefined`.
*   **`let` and `const`**: Declarations are hoisted but **not initialized**. Accessing them before the declaration results in a `ReferenceError`. The period from the start of the block to the declaration is known as the **Temporal Dead Zone (TDZ)**.

**Example:**

```javascript
console.log(x); // undefined (hoisted and initialized)
var x = 5;

// console.log(y); // ReferenceError: Cannot access 'y' before initialization (TDZ)
let y = 10;

// console.log(z); // ReferenceError: Cannot access 'z' before initialization (TDZ)
const z = 15;
```

#### 3. Re-declaration and Re-assignment

*   **`var`**: Can be **re-declared** and **re-assigned** within the same scope.
*   **`let`**: Can be **re-assigned** but **cannot be re-declared** within the same scope.
*   **`const`**: **Cannot be re-declared or re-assigned**. The variable is immutable, meaning its value cannot be changed. However, for objects and arrays, the *contents* (properties or elements) can be modified, but the variable cannot be reassigned to a new object or array.

**Example:**

```javascript
// var
var a = 1;
var a = 2; // Re-declaration allowed
a = 3;     // Re-assignment allowed
console.log(a); // 3

// let
let b = 1;
// let b = 2; // SyntaxError: 'b' has already been declared
b = 3;     // Re-assignment allowed
console.log(b); // 3

// const
const c = 1;
// const c = 2; // SyntaxError: 'c' has already been declared
// c = 3;       // TypeError: Assignment to constant variable.

const obj = { key: 'value' };
obj.key = 'new value'; // This is allowed
// obj = { newKey: 'newValue' }; // TypeError: Assignment to constant variable.
```

#### Comparison Table

| Feature | `var` | `let` | `const` |
| :--- | :--- | :--- | :--- |
| **Scope** | Function | Block | Block |
| **Hoisting** | Hoisted & initialized to `undefined` | Hoisted, not initialized (TDZ) | Hoisted, not initialized (TDZ) |
| **Re-declaration** | Allowed | Not allowed in the same scope | Not allowed in the same scope |
| **Re-assignment** | Allowed | Allowed | Not allowed |
| **Global Object** | Attaches to `window` in browsers | Does not attach to `window` | Does not attach to `window` |

#### Best Practice

*   Use **`const`** by default for all variable declarations.
*   Use **`let`** only when you know the variable's value needs to change (e.g., in a loop counter).
*   Avoid using **`var`** in modern JavaScript to prevent scope and hoisting-related issues.

---

---

### Q77: What are arrow functions and how do they differ from regular functions?

**Answer:**

Arrow functions, introduced in ES6, provide a more concise syntax for writing function expressions. They also behave differently from traditional function expressions in a few key ways, particularly regarding the `this` keyword.

#### Syntax

Arrow functions offer a shorter syntax compared to regular functions.

```javascript
// Regular Function Expression
const add = function(a, b) {
  return a + b;
};

// Arrow Function
const addArrow = (a, b) => a + b; // Implicit return for single expressions

// Arrow function with a block body
const subtract = (a, b) => {
  const result = a - b;
  return result; // Explicit return required
};

// Arrow function with a single parameter
const square = x => x * x;
```

#### Key Differences

1.  **Lexical `this` Binding**

    This is the most significant difference. Arrow functions do **not** have their own `this` context. Instead, they inherit `this` from their parent scope (the enclosing lexical context). Regular functions get their own `this` value depending on how they are called (e.g., as a method, in the global context, with `call`/`apply`).

    This behavior is extremely useful for callbacks and event handlers, as it solves the common problem of having to use `that = this` or `.bind(this)`.

    **Example:**

    ```javascript
    function Timer() {
      this.seconds = 0;

      // Regular function - `this` refers to the global object (or is undefined in strict mode)
      // setInterval(function() {
      //   this.seconds++; // Fails because `this` is not the Timer instance
      //   console.log(this.seconds);
      // }, 1000);

      // Arrow function - `this` is inherited from the Timer's scope
      setInterval(() => {
        this.seconds++;
        console.log(this.seconds); // Works correctly, `this` is the Timer instance
      }, 1000);
    }

    const myTimer = new Timer();
    ```

2.  **No `arguments` Object**

    Arrow functions do not have their own `arguments` object. If you need to access the arguments passed to an arrow function, you should use **rest parameters** (`...args`).

    ```javascript
    // Regular function
    function logArgs() {
      console.log(arguments);
    }
    logArgs(1, 2, 3); // [Arguments] { '0': 1, '1': 2, '2': 3 }

    // Arrow function
    const logArgsArrow = (...args) => {
      // console.log(arguments); // ReferenceError: arguments is not defined
      console.log(args);
    };
    logArgsArrow(1, 2, 3); // [1, 2, 3]
    ```

3.  **Cannot be used as Constructors**

    Arrow functions cannot be used as constructors and will throw an error when used with `new`. They do not have a `prototype` property.

    ```javascript
    const Person = (name) => {
      this.name = name;
    };

    // const john = new Person('John'); // TypeError: Person is not a constructor
    ```

#### When to Use Arrow Functions

*   **Callbacks and Higher-Order Functions**: Perfect for short, non-method functions, especially in array methods like `.map()`, `.filter()`, and `.forEach()`, where lexical `this` is a benefit.
*   **When you need to preserve the `this` context** from the parent scope without using `.bind()`.

#### When NOT to Use Arrow Functions

*   **Object Methods**: If you need a method to access the object's properties via `this`, use a regular function or the ES6 method syntax.
*   **Constructors**: As they cannot be used with `new`.
*   **Event Handlers that need a dynamic `this`**: When you need `this` to refer to the element that triggered the event, a regular function is required.

---

---

### Q78: What is the difference between the spread and rest operators?

**Answer:**

The spread (`...`) and rest (`...`) operators in JavaScript use the same syntax but perform opposite functions depending on where they are used. The rest operator collects multiple elements into an array, while the spread operator expands an iterable into individual elements.

#### Rest Operator (`...`)

The rest operator is used in a function's parameter list to **collect all remaining arguments into a single array**. This allows you to handle functions with a variable number of arguments.

*   It must be the **last parameter** in a function definition.
*   It gathers individual arguments into an array.

**Syntax:**

```javascript
function myFunction(firstArg, secondArg, ...restOfArgs) {
  console.log(firstArg);      // 1
  console.log(secondArg);     // 2
  console.log(restOfArgs);    // [3, 4, 5]
}

myFunction(1, 2, 3, 4, 5);
```

In this example, `...restOfArgs` collects all arguments after the first two into an array named `restOfArgs`.

#### Spread Operator (`...`)

The spread operator is used to **expand an iterable** (like an array or string) into its individual elements. It can be used in various contexts, such as in function calls, array literals, and object literals.

*   It "spreads out" the elements of an iterable.
*   It can be used anywhere in an array or object literal, and multiple times.

**Use Cases:**

1.  **In Function Calls:** To pass elements of an array as individual arguments to a function.

    ```javascript
    function sum(x, y, z) {
      return x + y + z;
    }

    const numbers = [1, 2, 3];
    const result = sum(...numbers); // Equivalent to sum(1, 2, 3)
    console.log(result); // 6
    ```

2.  **In Array Literals:** To create a new array containing elements from another array (useful for copying or merging arrays).

    ```javascript
    const arr1 = [1, 2];
    const arr2 = [3, 4];

    // Copying an array
    const arr1Copy = [...arr1];
    console.log(arr1Copy); // [1, 2]

    // Merging arrays
    const mergedArray = [...arr1, ...arr2, 5];
    console.log(mergedArray); // [1, 2, 3, 4, 5]
    ```

3.  **In Object Literals (ES2018):** To copy or merge properties from one object into another.

    ```javascript
    const obj1 = { a: 1, b: 2 };
    const obj2 = { c: 3, d: 4 };

    // Copying an object
    const obj1Copy = { ...obj1 };
    console.log(obj1Copy); // { a: 1, b: 2 }

    // Merging objects
    const mergedObject = { ...obj1, ...obj2, e: 5 };
    console.log(mergedObject); // { a: 1, b: 2, c: 3, d: 4, e: 5 }

    // Overwriting properties
    const updatedObject = { ...obj1, b: 99 };
    console.log(updatedObject); // { a: 1, b: 99 }
    ```

#### Summary Table

| Operator | Usage | Function | Example |
| :--- | :--- | :--- | :--- |
| **Rest** | In function parameter lists | **Collects** multiple elements into a single array | `function fn(a, ...rest) {}` |
| **Spread** | In function calls, array/object literals | **Expands** an iterable into individual elements | `const arr = [...iterable];` |

**Key Takeaway:** Think of **rest** as *gathering* items into an array and **spread** as *spreading* them out. The context in which `...` is used determines its behavior.

---

---

### Q79: Explain the array methods `map`, `filter`, and `reduce`.

**Answer:**

`map`, `filter`, and `reduce` are three of the most powerful and commonly used array methods in JavaScript. They are higher-order functions that allow for a declarative, functional approach to handling arrays, and they all operate by iterating over an array and returning a new value without modifying the original array.

#### 1. `map()`

The `map()` method **transforms** each element in an array and returns a **new array** of the same length with the transformed elements.

*   **Purpose**: To create a new array by applying a function to every element of the original array.
*   **Return Value**: A new array.

**Syntax:**

```javascript
const newArray = originalArray.map((currentValue, index, array) => {
  // return transformed value
});
```

**Example:** Doubling each number in an array.

```javascript
const numbers = [1, 2, 3, 4];
const doubled = numbers.map(num => num * 2);

console.log(doubled); // [2, 4, 6, 8]
console.log(numbers); // [1, 2, 3, 4] (original array is unchanged)
```

#### 2. `filter()`

The `filter()` method **creates a new array** containing only the elements from the original array that pass a certain test (i.e., for which the callback function returns `true`).

*   **Purpose**: To select a subset of elements from an array based on a condition.
*   **Return Value**: A new array, which can be shorter than the original.

**Syntax:**

```javascript
const newArray = originalArray.filter((currentValue, index, array) => {
  // return true to keep the element, false to discard it
});
```

**Example:** Filtering out only the even numbers.

```javascript
const numbers = [1, 2, 3, 4, 5, 6];
const evens = numbers.filter(num => num % 2 === 0);

console.log(evens); // [2, 4, 6]
console.log(numbers); // [1, 2, 3, 4, 5, 6] (original array is unchanged)
```

#### 3. `reduce()`

The `reduce()` method executes a reducer function on each element of the array, resulting in a **single output value**. It "reduces" the array to a single value (e.g., a number, string, or object).

*   **Purpose**: To aggregate all elements of an array into one final value.
*   **Return Value**: A single value of any type.

**Syntax:**

```javascript
const singleValue = originalArray.reduce((accumulator, currentValue, index, array) => {
  // return the new accumulator value
}, initialValue);
```

*   `accumulator`: The value returned from the previous iteration. On the first call, it's the `initialValue` if provided; otherwise, it's the first element of the array.
*   `initialValue`: An optional starting value for the accumulator.

**Example:** Summing all numbers in an array.

```javascript
const numbers = [1, 2, 3, 4];
const sum = numbers.reduce((accumulator, currentValue) => {
  return accumulator + currentValue;
}, 0); // 0 is the initial value for the accumulator

console.log(sum); // 10
```

**Another Example:** Grouping objects by a property.

```javascript
const people = [
  { name: 'Alice', age: 21 },
  { name: 'Bob', age: 25 },
  { name: 'Charlie', age: 21 },
];

const groupedByAge = people.reduce((acc, person) => {
  const age = person.age;
  if (!acc[age]) {
    acc[age] = [];
  }
  acc[age].push(person);
  return acc;
}, {});

// Output:
// {
//   '21': [ { name: 'Alice', age: 21 }, { name: 'Charlie', age: 21 } ],
//   '25': [ { name: 'Bob', age: 25 } ]
// }
```

#### Summary Table

| Method | Purpose | Returns | Use Case Example |
| :--- | :--- | :--- | :--- |
| **`map()`** | Transform each element | A new array of the same length | Converting an array of numbers to an array of strings |
| **`filter()`** | Select a subset of elements | A new array with elements that pass a test | Getting all users who are active |
| **`reduce()`** | Aggregate elements to a single value | A single value (any type) | Calculating the total price of items in a cart |

---

---

### Q80: What is the difference between a shallow copy and a deep copy of an object?

**Answer:**

The difference between a shallow and a deep copy lies in how they handle nested objects and arrays. Understanding this is crucial for avoiding unintended side effects when working with complex data structures in JavaScript.

#### Shallow Copy

A shallow copy of an object creates a new object, but it only copies the **top-level properties**. If a property's value is a primitive type (like a number or string), the value is copied. However, if a property's value is a reference type (like an object or array), only the **reference** is copied, not the actual nested object itself.

This means that both the original object and the copied object will point to the **same nested object**. Modifying the nested object through one copy will affect the other.

**Common ways to create a shallow copy:**

1.  **Spread Operator (`...`)**
2.  **`Object.assign()`**

**Example:**

```javascript
const original = {
  name: 'Alice',
  details: { age: 30, city: 'New York' }
};

// Create a shallow copy
const shallowCopy = { ...original };

// Modify a top-level property
shallowCopy.name = 'Bob';

// Modify a nested property
shallowCopy.details.age = 31;

console.log(original.name);       // 'Alice' (Unaffected)
console.log(shallowCopy.name);      // 'Bob' (Changed)

console.log(original.details.age);  // 31 (Affected!)
console.log(shallowCopy.details.age); // 31 (Changed)
```

As you can see, changing `shallowCopy.details.age` also changed `original.details.age` because both objects share the same `details` object.

#### Deep Copy

A deep copy creates a **completely independent** new object. It recursively copies all properties, including all nested objects and arrays. The new object and the original object do not share any references.

Modifying any part of the deep copy, no matter how nested, will not affect the original object.

**Common ways to create a deep copy:**

1.  **`JSON.parse(JSON.stringify(object))`**: A common and easy trick, but it has limitations. It cannot copy functions, `undefined`, Symbols, or handle circular references.
2.  **Libraries like Lodash**: The `_.cloneDeep()` method is a robust and reliable way to create a deep copy.
3.  **Custom recursive function**: For full control, you can write your own function to traverse and copy the object.

**Example:**

```javascript
const original = {
  name: 'Alice',
  details: { age: 30, city: 'New York' },
  greet: () => console.log('Hello')
};

// Create a deep copy using JSON methods
const deepCopy = JSON.parse(JSON.stringify(original));

// Modify a nested property
deepCopy.details.age = 31;

console.log(original.details.age);  // 30 (Unaffected)
console.log(deepCopy.details.age); // 31 (Changed)

// Note the limitation with functions
console.log(original.greet); // [Function: greet]
console.log(deepCopy.greet); // undefined (Function was lost)
```

#### Comparison Table

| Feature | Shallow Copy | Deep Copy |
| :--- | :--- | :--- |
| **Top-Level Properties** | Copied | Copied |
| **Nested Objects/Arrays** | References are copied (shared) | Cloned recursively (not shared) |
| **Independence** | Not fully independent | Fully independent |
| **Common Methods** | `...`, `Object.assign()` | `JSON.parse(JSON.stringify())`, `_.cloneDeep()` |
| **Performance** | Faster | Slower (more work to do) |

**Best Practice:**

*   Use a **shallow copy** when your object only contains primitive values or when you intentionally want to share nested objects.
*   Use a **deep copy** when you need a complete, independent duplicate of an object to prevent side effects, especially in complex applications (e.g., state management in frameworks like React/Redux).

---

---

### Q81: What is event delegation in JavaScript?

**Answer:**

Event delegation is a powerful technique for handling events in JavaScript where, instead of attaching an event listener to every single child element, you attach a single listener to a common parent element. This listener then analyzes the event as it bubbles up the DOM tree to find the actual target element that triggered it.

This pattern relies on **event bubbling**, the mechanism where an event fired on a child element propagates (or "bubbles") up to its parent elements in the DOM hierarchy.

#### Why Use Event Delegation?

1.  **Improved Performance and Memory Efficiency**: Attaching hundreds or thousands of event listeners can consume a lot of memory and slow down your application. A single listener on a parent element is far more efficient.

2.  **Simplified Code**: It keeps your code cleaner and more maintainable by centralizing the event handling logic.

3.  **Handles Dynamically Added Elements**: If you add new child elements to the parent (e.g., fetching data and rendering a new list item), you don't need to manually attach new event listeners to them. The parent's listener will automatically handle events from these new elements.

#### How it Works

The process involves three steps:

1.  Attach an event listener to a parent container element.
2.  When an event is triggered on a child element, it bubbles up to the parent.
3.  Inside the parent's event listener, use the `event.target` property to identify the specific child element that was the source of the event.

**Example:**

Imagine you have a list of items, and you want to log the text of any item that is clicked.

**HTML:**

```html
<ul id="my-list">
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ul>
<button id="add-item">Add New Item</button>
```

**Without Event Delegation (Inefficient):**

```javascript
const listItems = document.querySelectorAll('#my-list li');
listItems.forEach(item => {
  item.addEventListener('click', event => {
    console.log(event.target.textContent);
  });
});
// This approach fails to add listeners to dynamically added items.
```

**With Event Delegation (Efficient and Dynamic):**

```javascript
const list = document.getElementById('my-list');

list.addEventListener('click', event => {
  // Check if the clicked element is an <li>
  if (event.target && event.target.nodeName === 'LI') {
    console.log('Clicked on:', event.target.textContent);
  }
});

// Now, even if we add new items, the listener will work for them.
const addItemButton = document.getElementById('add-item');
let itemCount = 3;

addItemButton.addEventListener('click', () => {
  itemCount++;
  const newItem = document.createElement('li');
  newItem.textContent = `Item ${itemCount}`;
  list.appendChild(newItem);
});
```

In the event delegation example, we attach only one listener to the `<ul>` element. When an `<li>` is clicked, the event bubbles up to the `<ul>`. The listener checks if the `event.target` (the actual element clicked) was an `<li>` and, if so, performs the action. This single listener works for all existing and future `<li>` elements inside the list.

#### Key Takeaway

Event delegation is a memory-efficient and flexible pattern for handling events on a large number of elements or on elements that are added to the DOM dynamically. It's a fundamental concept for writing scalable and performant web applications.

---

---

### Q82: What are the differences between `localStorage`, `sessionStorage`, and Cookies?

**Answer:**

`localStorage`, `sessionStorage`, and `cookies` are all client-side storage mechanisms that allow you to store data in the user's browser, but they have different use cases, storage limits, and lifespans.

#### Cookies

Cookies are small strings of data that a server sends to the user's browser. The browser stores them and sends them back to the same server with every subsequent request. They were originally designed for server-side communication.

*   **Storage Limit**: ~4KB.
*   **Expiration**: Manually set expiration date.
*   **Accessibility**: Accessible on both the server and client (via `document.cookie`).
*   **Sent with HTTP Requests**: Yes, automatically sent with every HTTP request to the same domain, which can impact performance if the data is large.
*   **Use Case**: Primarily for session management (like keeping a user logged in) and tracking user behavior.

#### Web Storage API (`localStorage` and `sessionStorage`)

The Web Storage API provides a simpler, more modern way to store key-value pairs in the browser. It is not sent with every HTTP request.

**1. `localStorage`**

`localStorage` stores data with no expiration date. The data persists even after the browser window is closed and reopened.

*   **Storage Limit**: ~5-10MB (much larger than cookies).
*   **Expiration**: Never expires. Data remains until it is explicitly cleared by the user or web app.
*   **Accessibility**: Accessible only on the client-side, within the same origin.
*   **Sent with HTTP Requests**: No.
*   **Use Case**: Storing user preferences (like a theme setting), application state, or data that needs to be available across multiple sessions.

**Example:**

```javascript
// Set an item
localStorage.setItem('theme', 'dark');

// Get an item
const theme = localStorage.getItem('theme'); // 'dark'

// Remove an item
localStorage.removeItem('theme');

// Clear all items
localStorage.clear();
```

**2. `sessionStorage`**

`sessionStorage` is identical to `localStorage` except that it only stores data for the duration of a **browser session**. A session ends when the tab or window is closed.

*   **Storage Limit**: ~5-10MB.
*   **Expiration**: Expires when the tab is closed.
*   **Accessibility**: Accessible only on the client-side, within the same origin and the same tab/window.
*   **Sent with HTTP Requests**: No.
*   **Use Case**: Storing temporary data for a single session, like data in a multi-step form, so it's not lost if the user reloads the page.

**Example:**

```javascript
// Set an item
sessionStorage.setItem('formData', 'some data');

// Get an item
const data = sessionStorage.getItem('formData');
```

#### Comparison Table

| Feature | `localStorage` | `sessionStorage` | `Cookies` |
| :--- | :--- | :--- | :--- |
| **Storage Limit** | 5-10MB | 5-10MB | ~4KB |
| **Expiration** | Never | On tab close | Manually set | 
| **Accessibility** | Client-side only | Client-side only | Client & Server |
| **Sent with HTTP Requests**| No | No | Yes |
| **Scope** | Same origin | Same origin, per tab | Same domain |

**Key Takeaway:**

*   Use **Cookies** for small pieces of data that need to be accessed by the server (e.g., authentication tokens).
*   Use **`localStorage`** for persistent client-side data that should be available across sessions.
*   Use **`sessionStorage`** for temporary data that is relevant only to the current browser tab session.

---

---

### Q83: What are debouncing and throttling in JavaScript?

**Answer:**

Debouncing and throttling are two rate-limiting techniques used to control how often a function is executed. They are essential for improving performance in response to frequent events like resizing the window, scrolling, or user input.

#### Debouncing

Debouncing ensures that a function is not called again until a certain amount of time has passed **without it being called**. It groups a burst of events into a single one.

*   **Analogy**: Imagine you are in an elevator. The door stays open as long as people keep arriving (triggering the sensor). The door only closes (the event fires) after a few seconds of no one else arriving.
*   **How it works**: Every time the event is triggered, a timer is reset. The function is only executed after the timer completes without being reset.

**Use Cases:**

*   **Search Bar Suggestions**: You only want to fetch search results after the user has stopped typing for a moment, not on every keystroke.
*   **Window Resizing**: You only want to recalculate a layout after the user has finished resizing the window, not continuously during the resize.

**Example Implementation:**

```javascript
function debounce(func, delay) {
  let timeoutId;

  return function(...args) {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => {
      func.apply(this, args);
    }, delay);
  };
}

// Usage
const expensiveOperation = () => console.log('Performing an expensive operation...');
const debouncedOperation = debounce(expensiveOperation, 300);

window.addEventListener('resize', debouncedOperation);
```

#### Throttling

Throttling ensures that a function is called **at most once** in a specified time interval, no matter how many times the event is triggered.

*   **Analogy**: Imagine a machine gun that can only fire one bullet every second. Even if you pull the trigger 10 times in that second, it will only fire once.
*   **How it works**: When the event is first triggered, the function is called, and a cooldown period starts. All subsequent calls during this cooldown are ignored. The function can only be called again after the cooldown period has ended.

**Use Cases:**

*   **Infinite Scrolling**: Firing a request to fetch more content as the user scrolls. Throttling prevents sending too many requests.
*   **Tracking Mouse Movement**: Updating an element's position based on the cursor. Throttling ensures the updates happen smoothly without overwhelming the browser.

**Example Implementation:**

```javascript
function throttle(func, limit) {
  let inThrottle = false;

  return function(...args) {
    if (!inThrottle) {
      func.apply(this, args);
      inThrottle = true;
      setTimeout(() => (inThrottle = false), limit);
    }
  };
}

// Usage
const onScroll = () => console.log('Scrolled!');
const throttledScroll = throttle(onScroll, 1000);

window.addEventListener('scroll', throttledScroll);
```

#### Comparison Table

| Feature | Debouncing | Throttling |
| :--- | :--- | :--- |
| **Execution** | Executes only **after** a period of inactivity. | Executes **at most once** per specified interval. |
| **Main Goal** | Postpone execution until there's a pause. | Guarantee a minimum time between executions. |
| **Example** | "Wait until the user stops typing." | "Fire this event every 100ms as the user scrolls." |

**Key Takeaway:**

*   Use **debounce** when you only care about the final state of an event series (e.g., final input value, final window size).
*   Use **throttle** when you want to handle an event at a regular, controlled rate during a continuous series of events (e.g., scrolling, dragging).
```

---

### Q84: What is the Shadow DOM?

**Difficulty: Advanced**

**Answer:**
The Shadow DOM is a web standard that offers component style and markup encapsulation. It is a critical piece of the Web Components story. It allows hidden DOM trees to be attached to elements in the regular DOM tree.

```javascript
// Create a shadow root
const host = document.querySelector('#host');
const shadow = host.attachShadow({mode: 'open'});
shadow.innerHTML = '<p>I am in the shadow DOM!</p>';
```

---

### Q85: What are "Void Elements" in HTML?

**Difficulty: Beginner**

**Answer:**
Void elements are elements that cannot have any child nodes (i.e., nested elements or text nodes). They are self-closing in XHTML, but in HTML5, the closing slash is optional.
Examples: `<br>`, `<hr>`, `<img>`, `<input>`, `<link>`, `<meta>`.

---

### Q86: What is the purpose of the `<template>` tag?

**Difficulty: Intermediate**

**Answer:**
The `<template>` tag is used to hold client-side content that will not be rendered when the page loads but may be instantiated subsequently during runtime using JavaScript.

```html
<template id="my-template">
  <div class="content">This is hidden content</div>
</template>
```

---

### Q87: What is the difference between `<link>` and `<a>` tags?

**Difficulty: Beginner**

**Answer:**
- `<a>` (Anchor): Defines a hyperlink to another page or a location within the same page. It is clickable by the user.
- `<link>`: Defines a relationship between the current document and an external resource (like CSS files, favicons). It is typically placed in the `<head>` and is not clickable.

---

### Q88: What are Microdata in HTML?

**Difficulty: Advanced**

**Answer:**
Microdata is a specification to nest metadata within existing content on web pages. Search engines (like Google) use it to understand the content better (Schema.org).

```html
<div itemscope itemtype="http://schema.org/Person">
  <span itemprop="name">John Doe</span>
</div>
```

---

### Q89: What is the `contenteditable` attribute?

**Difficulty: Intermediate**

**Answer:**
The `contenteditable` attribute specifies whether the content of an element is editable or not.

```html
<div contenteditable="true">
  This text can be edited by the user.
</div>
```

---

### Q90: What is the difference between SVG and Canvas?

**Difficulty: Intermediate**

**Answer:**
- **SVG (Scalable Vector Graphics):** Vector-based, XML format. Each shape is a DOM element. Good for logos, icons, and scalability. Event handlers can be attached to individual shapes.
- **Canvas:** Raster-based (pixels). Drawn via JavaScript. Good for high-performance games or complex animations with many moving parts. No DOM nodes for individual shapes.

---

### Q91: What is the purpose of the `autocomplete` attribute?

**Difficulty: Beginner**

**Answer:**
The `autocomplete` attribute specifies whether a form or an input field should have autocomplete on or off. When on, the browser automatically complete values based on values that the user has entered before.

---

### Q92: How do you specify the language of the page content?

**Difficulty: Beginner**

**Answer:**
Using the `lang` attribute on the `<html>` tag. This is important for accessibility (screen readers) and SEO.

```html
<html lang="en">
```

---

### Q93: What is the `<noscript>` tag?

**Difficulty: Beginner**

**Answer:**
The `<noscript>` tag defines an alternate content to be displayed to users that have disabled scripts in their browser or have a browser that doesn't support script.

---

### Q94: What is the purpose of the `download` attribute on an anchor tag?

**Difficulty: Intermediate**

**Answer:**
The `download` attribute instructs the browser to download the URL instead of navigating to it, so the user will be prompted to save it as a local file.

```html
<a href="/images/logo.png" download="my-logo.png">Download Logo</a>
```

---

### Q95: What are the new form input types introduced in HTML5?

**Difficulty: Beginner**

**Answer:**
HTML5 introduced several new input types for better mobile support and validation:
`color`, `date`, `datetime-local`, `email`, `month`, `number`, `range`, `search`, `tel`, `time`, `url`, `week`.

---

### Q96: What is the `<figure>` and `<figcaption>` element?

**Difficulty: Beginner**

**Answer:**
- `<figure>`: Specifies self-contained content, like illustrations, diagrams, photos, code listings, etc.
- `<figcaption>`: Defines a caption for a `<figure>` element.

```html
<figure>
  <img src="pic.jpg" alt="My Picture">
  <figcaption>Fig.1 - My Picture</figcaption>
</figure>
```

---

### Q97: What is the difference between `<b>` and `<strong>`?

**Difficulty: Beginner**

**Answer:**
- `<b>`: Stylistic. Brings attention to the element without indicating importance (Bold).
- `<strong>`: Semantic. Indicates that its contents have strong importance, seriousness, or urgency. Browsers typically render it in bold.

---

### Q98: What is the difference between `<i>` and `<em>`?

**Difficulty: Beginner**

**Answer:**
- `<i>`: Stylistic. Represents a range of text that is set off from the normal text for some reason, such as idiomatic text, technical terms, taxonomical designations, etc. (Italic).
- `<em>`: Semantic. Indicates emphasis of its contents. Browsers typically render it in italic.

---

### Q99: What is the purpose of the `hidden` attribute?

**Difficulty: Beginner**

**Answer:**
The `hidden` attribute is a boolean attribute. When present, it specifies that an element is not yet, or is no longer, relevant. Browsers will not render elements with the hidden attribute specified.

```html
<p hidden>This paragraph should be hidden.</p>
```

---

### Q100: What is the `details` and `summary` element?

**Difficulty: Intermediate**

**Answer:**
The `<details>` tag specifies additional details that the user can view or hide on demand. The `<summary>` tag defines a visible heading for the `<details>` element.

```html
<details>
  <summary>Click to open</summary>
  <p>Hidden content here...</p>
</details>
```

---

### Q101: What is the `<dialog>` element and how is it used?

**Difficulty: Intermediate**

**Answer:**
The `<dialog>` element represents a dialog box or other interactive component, such as a dismissible alert, inspector, or subwindow.

**Usage:**
```html
<dialog id="myDialog">
  <p>This is a dialog window</p>
  <button onclick="document.getElementById('myDialog').close()">Close</button>
</dialog>

<button onclick="document.getElementById('myDialog').showModal()">Open Dialog</button>
```

**Key Methods:**
- `show()`: Opens the dialog (non-modal).
- `showModal()`: Opens the dialog as a modal (blocks interaction with the rest of the page).
- `close()`: Closes the dialog.

---

### Q102: What are the `details` and `summary` tags?

**Difficulty: Beginner**

**Answer:**
The `<details>` element specifies additional details that the user can open and close on demand. The `<summary>` tag defines a visible heading for the `<details>` element.

**Example:**
```html
<details>
  <summary>More Information</summary>
  <p>This is the hidden content that appears when you click 'More Information'.</p>
</details>
```

---

### Q103: What is the difference between `<article>`, `<section>`, and `<div>`?

**Difficulty: Intermediate**

**Answer:**
- **`<article>`**: Self-contained content that could be distributed independently (e.g., blog post, news article).
- **`<section>`**: A thematic grouping of content, typically with a heading.
- **`<div>`**: A generic container with no semantic meaning. Used for styling or layout.

**Rule of Thumb:**
Use `<article>` if it makes sense on its own (like in an RSS feed). Use `<section>` if it's part of a larger whole but grouped thematically. Use `<div>` only when no other semantic element applies.

---

### Q104: What is the `picture` element?

**Difficulty: Intermediate**

**Answer:**
The `<picture>` element gives developers more flexibility in specifying image resources. It allows you to define multiple `<source>` elements for different screen sizes or image formats (like WebP), falling back to an `<img>`.

**Example:**
```html
<picture>
  <source media="(min-width: 650px)" srcset="img_large.jpg">
  <source media="(min-width: 465px)" srcset="img_medium.jpg">
  <img src="img_small.jpg" alt="Flowers">
</picture>
```

---

### Q105: What is the `srcset` attribute?

**Difficulty: Intermediate**

**Answer:**
The `srcset` attribute allows you to provide a set of images for the browser to choose from based on screen width or pixel density (e.g., Retina displays).

**Example:**
```html
<img src="small.jpg" 
     srcset="small.jpg 500w, medium.jpg 1000w, large.jpg 1500w"
     sizes="(max-width: 600px) 480px, 800px"
     alt="Responsive Image">
```

---

### Q106: What are `meta` tags for SEO?

**Difficulty: Beginner**

**Answer:**
Meta tags provide metadata about the HTML document. Important ones for SEO include:

- **Description:** `<meta name="description" content="Page summary...">`
- **Keywords:** `<meta name="keywords" content="HTML, CSS, JS">` (Less important now)
- **Viewport:** `<meta name="viewport" content="width=device-width, initial-scale=1.0">` (Mobile friendliness)
- **Robots:** `<meta name="robots" content="index, follow">`

---

### Q107: What is Open Graph Protocol?

**Difficulty: Intermediate**

**Answer:**
Open Graph (OG) tags control how your page is displayed when shared on social media (Facebook, LinkedIn, etc.).

**Example:**
```html
<meta property="og:title" content="My Article Title" />
<meta property="og:image" content="https://example.com/image.jpg" />
<meta property="og:description" content="Description of the article" />
```

---

### Q108: What is `preload`, `prefetch`, and `preconnect`?

**Difficulty: Advanced**

**Answer:**
Resource hints to optimize performance:

- **`preload`**: Fetch a critical resource (font, script) immediately for the current page.
  `<link rel="preload" href="style.css" as="style">`
- **`prefetch`**: Fetch a resource that might be needed for the *next* navigation (low priority).
  `<link rel="prefetch" href="next-page.js">`
- **`preconnect`**: Establish a network connection (DNS, TCP, TLS) to a server ahead of time.
  `<link rel="preconnect" href="https://api.example.com">`

---

### Q109: What is the `template` tag?

**Difficulty: Advanced**

**Answer:**
The `<template>` element holds client-side content that is not rendered when the page loads but can be instantiated subsequently during runtime using JavaScript.

**Example:**
```html
<template id="myTemplate">
  <div class="card">
    <h2>Title</h2>
    <p>Content</p>
  </div>
</template>
```

---

### Q110: What is `contenteditable`?

**Difficulty: Intermediate**

**Answer:**
The `contenteditable` global attribute specifies whether the content of an element is editable or not.

**Example:**
```html
<div contenteditable="true">
  You can edit this text directly in the browser!
</div>
```

---

### Q111: What is the `hidden` attribute?

**Difficulty: Beginner**

**Answer:**
The `hidden` boolean attribute indicates that the element is not yet, or is no longer, relevant. Browsers render it as `display: none`.

```html
<p hidden>This paragraph is hidden.</p>
```

---

### Q112: What is the `tabindex` attribute?

**Difficulty: Intermediate**

**Answer:**
`tabindex` controls whether an element is focusable and the order in which it receives focus via the keyboard (Tab key).

- **`tabindex="0"`**: Insert into tab order based on source order.
- **`tabindex="-1"`**: Focusable programmatically but not via Tab key.
- **`tabindex="1"`** (or positive): Defines specific tab order (avoid using this as it disrupts natural flow).

---

### Q113: What are HTML5 Form Validation attributes?

**Difficulty: Beginner**

**Answer:**
- **`required`**: Field must be filled.
- **`pattern`**: Regex pattern the value must match.
- **`min`/`max`**: Range for numbers/dates.
- **`minlength`/`maxlength`**: Character limits.
- **`type`**: Email, url, etc. triggers validation.

**Example:**
```html
<input type="text" pattern="[A-Za-z]{3}" title="Three letters code" required>
```

---

### Q114: What is the `datalist` element?

**Difficulty: Intermediate**

**Answer:**
The `<datalist>` element provides an "autocomplete" feature for `<input>` elements. Users see a drop-down list of pre-defined options as they input data.

**Example:**
```html
<input list="browsers" name="browser">
<datalist id="browsers">
  <option value="Chrome">
  <option value="Firefox">
  <option value="Safari">
</datalist>
```

---

### Q115: What is the difference between `script` in `head` vs `body`?

**Difficulty: Beginner**

**Answer:**
- **In `<head>`**: Scripts block parsing of the rest of the HTML until they are downloaded and executed (unless `async`/`defer` is used). Good for critical initializations.
- **End of `<body>`**: Allows the HTML to be parsed and displayed before the script runs. Traditionally used to improve perceived performance.

---

### Q116: What is a Favicon?

**Difficulty: Beginner**

**Answer:**
A small icon associated with a particular website or web page, displayed in the browser tab.

```html
<link rel="icon" type="image/png" href="/favicon.png">
```

---

### Q117: What is the `base` tag?

**Difficulty: Intermediate**

**Answer:**
The `<base>` tag specifies the base URL and/or target for all relative URLs in a document. It must be inside the `<head>`.

```html
<head>
  <base href="https://www.example.com/images/" target="_blank">
</head>
<body>
  <img src="logo.png"> <!-- Resolves to https://www.example.com/images/logo.png -->
</body>
```

---

### Q118: What are Void Elements?

**Difficulty: Beginner**

**Answer:**
Void elements are elements that cannot have any child nodes (i.e., nested elements or text nodes). They do not have a closing tag.

Examples: `<br>`, `<hr>`, `<img>`, `<input>`, `<link>`, `<meta>`.

---

### Q119: What is the `noscript` tag?

**Difficulty: Beginner**

**Answer:**
The `<noscript>` tag defines an alternate content to be displayed to users that have disabled scripts in their browser or have a browser that doesn't support script.

---

### Q120: What is Character Encoding?

**Difficulty: Intermediate**

**Answer:**
It tells the browser how to interpret the bytes in the HTML file into characters. UTF-8 is the standard for the web.

```html
<meta charset="UTF-8">
```
Without this, special characters might appear as garbage text (mojibake).

---

### Q121: What is `autocomplete` attribute?

**Difficulty: Beginner**

**Answer:**
Specifies whether a form or an input field should have autocomplete enabled. Browsers can predict the value based on earlier typed values.

Values: `on`, `off`, `name`, `email`, `username`, `current-password`, `new-password`, etc.

---

### Q122: What is the `download` attribute?

**Difficulty: Intermediate**

**Answer:**
Used on `<a>` tags to instruct the browser to download the URL instead of navigating to it.

```html
<a href="/path/to/image.jpg" download="filename.jpg">Download Image</a>
```

---

### Q123: What is Accessibility (a11y)?

**Difficulty: Intermediate**

**Answer:**
The practice of making websites usable by people with disabilities. This involves using semantic HTML, ARIA roles, keyboard navigation support, and sufficient color contrast.

---

### Q124: What are ARIA roles?

**Difficulty: Advanced**

**Answer:**
ARIA (Accessible Rich Internet Applications) roles define what an element is or does. They are used when native HTML elements don't provide the correct semantics.

Examples: `role="button"`, `role="navigation"`, `role="alert"`, `role="dialog"`.

---

### Q125: What is `aria-label` vs `aria-labelledby`?

**Difficulty: Advanced**

**Answer:**
- **`aria-label`**: Defines a string value that labels the current element.
  `<button aria-label="Close">X</button>`
- **`aria-labelledby`**: References the ID of another element that labels the current element.
  `<h2 id="title">Settings</h2> <div aria-labelledby="title">...</div>`

---

### Q126: What is `DOCTYPE`?

**Difficulty: Beginner**

**Answer:**
`<!DOCTYPE html>` is not an HTML tag; it's an instruction to the web browser about what version of HTML the page is written in. It triggers "Standards Mode" instead of "Quirks Mode".

---

### Q127: What is Quirks Mode?

**Difficulty: Advanced**

**Answer:**
A compatibility mode used by browsers to render pages that don't have a valid DOCTYPE. It mimics the behavior of older browsers (like IE5) to prevent breaking legacy sites.

---

### Q128: What is the `lang` attribute?

**Difficulty: Beginner**

**Answer:**
Declares the language of the page or element. Important for screen readers and search engines.

```html
<html lang="en">
```

---

### Q129: What is `target='_blank'` security risk?

**Difficulty: Advanced**

**Answer:**
When you use `target="_blank"`, the linked page gets partial access to the linking page via the `window.opener` object. This can be a security risk (phishing).
Fix: Add `rel="noopener noreferrer"`.

---

### Q130: What is Microdata?

**Difficulty: Advanced**

**Answer:**
A way to nest metadata within existing content on web pages. Search engines use it to understand content (Schema.org).

```html
<div itemscope itemtype="https://schema.org/Person">
  <span itemprop="name">John Doe</span>
</div>
```

---

### Q131: What is IndexedDB?

**Difficulty: Advanced**

**Answer:**
A low-level API for client-side storage of significant amounts of structured data, including files/blobs. It uses indexes to enable high-performance searches of this data. It is more powerful than LocalStorage.

---

### Q132: What is the Geolocation API?

**Difficulty: Intermediate**

**Answer:**
An API to get the geographical position of a user.

```javascript
navigator.geolocation.getCurrentPosition((position) => {
  console.log(position.coords.latitude, position.coords.longitude);
});
```

---

### Q133: What is the Drag and Drop API?

**Difficulty: Intermediate**

**Answer:**
Allows elements to be dragged and dropped.
Attributes: `draggable="true"`, events: `ondragstart`, `ondragover`, `ondrop`.

---

### Q134: What is the History API?

**Difficulty: Intermediate**

**Answer:**
Allows manipulation of the browser session history.
Methods: `history.pushState()`, `history.replaceState()`, `history.back()`, `history.forward()`.
Used heavily by Single Page Applications (SPAs).

---

### Q135: What is Content Security Policy (CSP)?

**Difficulty: Advanced**

**Answer:**
An added layer of security that helps to detect and mitigate certain types of attacks, including Cross-Site Scripting (XSS) and data injection attacks.

```html
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; img-src https://*;">
```

---

### Q136: What is the `progress` element?

**Difficulty: Intermediate**

**Answer:**
Represents the completion progress of a task.

```html
<progress value="70" max="100">70%</progress>
```

---

### Q137: What is the `meter` element?

**Difficulty: Intermediate**

**Answer:**
Represents a scalar measurement within a known range (e.g., disk usage).

```html
<meter value="0.6">60%</meter>
```

---

### Q138: What is the `figure` and `figcaption` element?

**Difficulty: Intermediate**

**Answer:**
Used for self-contained content, like illustrations, diagrams, photos, code listings, etc. `figcaption` provides a caption.

```html
<figure>
  <img src="pic.jpg">
  <figcaption>Fig.1 - A nice picture.</figcaption>
</figure>
```

---

### Q139: What is the `time` element?

**Difficulty: Beginner**

**Answer:**
Represents a specific period in time.

```html
<time datetime="2023-10-05">October 5, 2023</time>
```

---

### Q140: What is the `output` element?

**Difficulty: Intermediate**

**Answer:**
Represents the result of a calculation (like one performed by a script).

```html
<form oninput="x.value=parseInt(a.value)+parseInt(b.value)">
  <input type="range" id="a" value="50"> +
  <input type="number" id="b" value="50"> =
  <output name="x" for="a b"></output>
</form>
```

---

### Q141: What is the `abbr` element?

**Difficulty: Beginner**

**Answer:**
Represents an abbreviation or acronym. The `title` attribute can provide the full description.

```html
<abbr title="HyperText Markup Language">HTML</abbr>
```

---

### Q142: What is the `kbd` element?

**Difficulty: Beginner**

**Answer:**
Represents user input, typically keyboard input.

```html
<p>Press <kbd>Ctrl</kbd> + <kbd>C</kbd> to copy.</p>
```

---

### Q143: What is the `code` element?

**Difficulty: Beginner**

**Answer:**
Displays a short fragment of computer code.

---

### Q144: What is the `pre` element?

**Difficulty: Beginner**

**Answer:**
Defines preformatted text. Text in a `<pre>` element is displayed in a fixed-width font, and the text preserves both spaces and line breaks.

---

### Q145: What is the `blockquote` element?

**Difficulty: Beginner**

**Answer:**
Specifies a section that is quoted from another source. Browsers usually indent `blockquote` elements.

---

### Q146: What is the `cite` element?

**Difficulty: Beginner**

**Answer:**
Defines the title of a creative work (e.g., a book, a poem, a song, a movie).

---

### Q147: What is the `address` element?

**Difficulty: Beginner**

**Answer:**
Defines the contact information for the author/owner of a document or an article.

---

### Q148: What is the `map` and `area` element?

**Difficulty: Advanced**

**Answer:**
Used to create an image map (an image with clickable areas).

```html
<img src="workplace.jpg" usemap="#workmap">
<map name="workmap">
  <area shape="rect" coords="34,44,270,350" href="computer.htm">
</map>
```

---

### Q149: What is the `track` element?

**Difficulty: Intermediate**

**Answer:**
Specifies subtitles, captions, or other files to be visible when the media is playing (for `<video>` and `<audio>`).

```html
<video controls>
  <source src="movie.mp4" type="video/mp4">
  <track src="subtitles_en.vtt" kind="subtitles" srclang="en" label="English">
</video>
```

---

### Q150: What is the `wbr` element?

**Difficulty: Intermediate**

**Answer:**
Word Break Opportunity. Specifies where in a text it would be ok to add a line-break.

---

### Q151: What is the `ruby` element?

**Difficulty: Advanced**

**Answer:**
Specifies a ruby annotation (small text attached to the main text, primarily used for East Asian typography).

---

### Q152: What is `inputmode`?

**Difficulty: Intermediate**

**Answer:**
Hints at the type of data that might be entered by the user while editing the element or its contents. This allows a browser to display an appropriate virtual keyboard.
Values: `text`, `decimal`, `numeric`, `tel`, `search`, `email`, `url`.

---

### Q153: What is the `translate` attribute?

**Difficulty: Intermediate**

**Answer:**
Specifies whether the content of an element should be translated or not.
`<p translate="no">BrandName</p>`

---

### Q154: What is the `manifest` attribute?

**Difficulty: Advanced**

**Answer:**
Used on the `<html>` tag to specify the URL of the document's cache manifest (deprecated in favor of Service Workers).

---

### Q155: What is the `sandbox` attribute for iframes?

**Difficulty: Advanced**

**Answer:**
Enables an extra set of restrictions for the content in the iframe.
Values: `allow-forms`, `allow-scripts`, `allow-same-origin`, etc.

---

### Q156: What is the `srcdoc` attribute for iframes?

**Difficulty: Advanced**

**Answer:**
Specifies the HTML content of the page to show in the inline frame.

