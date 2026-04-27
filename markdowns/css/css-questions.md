<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>CSS Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for frontend developers</b></p>
</div>

---

## Table of Contents

1. [How do you implement a responsive 12-column grid using CSS Grid?](#q1-how-do-you-implement-a-responsive-12-column-grid-using-css-grid) <span class="intermediate">Intermediate</span>
2. [How do you center an element absolutely both vertically and horizontally?](#q2-how-do-you-center-an-element-absolutely-both-vertically-and-horizontally) <span class="intermediate">Intermediate</span>
3. [How do you implement a sticky footer that stays at the bottom even with little content?](#q3-how-do-you-implement-a-sticky-footer-that-stays-at-the-bottom-even-with-little-content) <span class="intermediate">Intermediate</span>
4. [How do you implement a pure CSS tooltip?](#q4-how-do-you-implement-a-pure-css-tooltip) <span class="intermediate">Intermediate</span>
5. [How do you create a custom checkbox using CSS?](#q5-how-do-you-create-a-custom-checkbox-using-css) <span class="intermediate">Intermediate</span>
6. [How do you implement Dark Mode using CSS Variables?](#q6-how-do-you-implement-dark-mode-using-css-variables) <span class="intermediate">Intermediate</span>
7. [How do you create a responsive aspect ratio box (e.g., 16:9 video embed)?](#q7-how-do-you-create-a-responsive-aspect-ratio-box-e.g.-16:9-video-embed) <span class="intermediate">Intermediate</span>
8. [How do you truncate text with an ellipsis (...) for a single line and multiple lines?](#q8-how-do-you-truncate-text-with-an-ellipsis-...-for-a-single-line-and-multiple-lines) <span class="intermediate">Intermediate</span>
9. [How do you use Container Queries to build component-based responsive styles?](#q9-how-do-you-use-container-queries-to-build-component-based-responsive-styles) <span class="intermediate">Intermediate</span>
10. [How do you optimize CSS performance (Painting and Layout)?](#q10-how-do-you-optimize-css-performance-painting-and-layout) <span class="intermediate">Intermediate</span>
11. [How do you implement a parallax scrolling effect purely in CSS?](#q11-how-do-you-implement-a-parallax-scrolling-effect-purely-in-css) <span class="intermediate">Intermediate</span>
12. [How do you ensure an element is visually hidden but accessible to screen readers?](#q12-how-do-you-ensure-an-element-is-visually-hidden-but-accessible-to-screen-readers) <span class="intermediate">Intermediate</span>
13. [How do you implement a CSS Triangle?](#q13-how-do-you-implement-a-css-triangle) <span class="intermediate">Intermediate</span>
14. [How do you prevent content layout shift (CLS) for images?](#q14-how-do-you-prevent-content-layout-shift-cls-for-images) <span class="intermediate">Intermediate</span>
15. [How do you implement a masonry layout using CSS only?](#q15-how-do-you-implement-a-masonry-layout-using-css-only) <span class="intermediate">Intermediate</span>
16. [How do you use Flexbox for a navigation bar?](#q16-how-do-you-use-flexbox-for-a-navigation-bar) <span class="intermediate">Intermediate</span>
17. [How do you use `flex-grow`, `flex-shrink`, and `flex-basis`?](#q17-how-do-you-use-flex-grow-flex-shrink-and-flex-basis) <span class="intermediate">Intermediate</span>
18. [How do you implement a sidebar layout with Flexbox?](#q18-how-do-you-implement-a-sidebar-layout-with-flexbox) <span class="intermediate">Intermediate</span>
19. [How do you align items in a grid using `justify-items` and `align-items`?](#q19-how-do-you-align-items-in-a-grid-using-justify-items-and-align-items) <span class="intermediate">Intermediate</span>
20. [How do you use `minmax()` in CSS Grid?](#q20-how-do-you-use-minmax-in-css-grid) <span class="intermediate">Intermediate</span>
21. [How do you create overlapping elements with CSS Grid?](#q21-how-do-you-create-overlapping-elements-with-css-grid) <span class="intermediate">Intermediate</span>
22. [How do you use `z-index` and stacking contexts effectively?](#q22-how-do-you-use-z-index-and-stacking-contexts-effectively) <span class="intermediate">Intermediate</span>
23. [How do you debug `z-index` issues?](#q23-how-do-you-debug-z-index-issues) <span class="intermediate">Intermediate</span>
24. [How do you style a scrollbar using `::-webkit-scrollbar`?](#q24-how-do-you-style-a-scrollbar-using-::-webkit-scrollbar) <span class="intermediate">Intermediate</span>
25. [How do you use `scroll-behavior: smooth`?](#q25-how-do-you-use-scroll-behavior:-smooth) <span class="intermediate">Intermediate</span>
26. [How do you use `scroll-snap-type` for snapping sections?](#q26-how-do-you-use-scroll-snap-type-for-snapping-sections) <span class="intermediate">Intermediate</span>
27. [How do you implement a CSS reset or normalize?](#q27-how-do-you-implement-a-css-reset-or-normalize) <span class="intermediate">Intermediate</span>
28. [How do you use `box-sizing: border-box` globally?](#q28-how-do-you-use-box-sizing:-border-box-globally) <span class="intermediate">Intermediate</span>
29. [How do you style inputs to look consistent across browsers?](#q29-how-do-you-style-inputs-to-look-consistent-across-browsers) <span class="intermediate">Intermediate</span>
30. [How do you remove the default outline on focus (and what to replace it with)?](#q30-how-do-you-remove-the-default-outline-on-focus-and-what-to-replace-it-with) <span class="intermediate">Intermediate</span>
31. [How do you style a broken image using `img::before`?](#q31-how-do-you-style-a-broken-image-using-img::before) <span class="intermediate">Intermediate</span>
32. [How do you style list markers using `::marker`?](#q32-how-do-you-style-list-markers-using-::marker) <span class="intermediate">Intermediate</span>
33. [How do you use `object-fit` and `object-position` for images?](#q33-how-do-you-use-object-fit-and-object-position-for-images) <span class="intermediate">Intermediate</span>
34. [How do you use `background-size: cover` vs `contain`?](#q34-how-do-you-use-background-size:-cover-vs-contain) <span class="intermediate">Intermediate</span>
35. [How do you create a gradient background?](#q35-how-do-you-create-a-gradient-background) <span class="intermediate">Intermediate</span>
36. [How do you create a text gradient?](#q36-how-do-you-create-a-text-gradient) <span class="intermediate">Intermediate</span>
37. [How do you use `clip-path` to create shapes?](#q37-how-do-you-use-clip-path-to-create-shapes) <span class="intermediate">Intermediate</span>
38. [How do you use `mask-image` for transparency masks?](#q38-how-do-you-use-mask-image-for-transparency-masks) <span class="intermediate">Intermediate</span>
39. [How do you use `backdrop-filter` for glassmorphism?](#q39-how-do-you-use-backdrop-filter-for-glassmorphism) <span class="intermediate">Intermediate</span>
40. [How do you use `filter` for image effects (blur, grayscale)?](#q40-how-do-you-use-filter-for-image-effects-blur-grayscale) <span class="intermediate">Intermediate</span>
41. [How do you use `mix-blend-mode` for blending effects?](#q41-how-do-you-use-mix-blend-mode-for-blending-effects) <span class="intermediate">Intermediate</span>
42. [How do you implement a loading spinner with CSS animations?](#q42-how-do-you-implement-a-loading-spinner-with-css-animations) <span class="intermediate">Intermediate</span>
43. [How do you create a shake animation?](#q43-how-do-you-create-a-shake-animation) <span class="intermediate">Intermediate</span>
44. [How do you pause an animation on hover?](#q44-how-do-you-pause-an-animation-on-hover) <span class="intermediate">Intermediate</span>
45. [How do you use CSS transitions for hover effects?](#q45-how-do-you-use-css-transitions-for-hover-effects) <span class="intermediate">Intermediate</span>
46. [How do you use the `:not()` pseudo-class?](#q46-how-do-you-use-the-:not-pseudo-class) <span class="intermediate">Intermediate</span>
47. [How do you use the `:has()` pseudo-class (parent selector)?](#q47-how-do-you-use-the-:has-pseudo-class-parent-selector) <span class="intermediate">Intermediate</span>
48. [How do you use the `:is()` and `:where()` pseudo-classes?](#q48-how-do-you-use-the-:is-and-:where-pseudo-classes) <span class="intermediate">Intermediate</span>
49. [How do you use `:nth-child()` and `:nth-of-type()`?](#q49-how-do-you-use-:nth-child-and-:nth-of-type) <span class="intermediate">Intermediate</span>
50. [How do you use `::first-letter` and `::first-line`?](#q50-how-do-you-use-::first-letter-and-::first-line) <span class="intermediate">Intermediate</span>
51. [How do you use attribute selectors?](#q51-how-do-you-use-attribute-selectors) <span class="intermediate">Intermediate</span>
52. [How do you style placeholder text?](#q52-how-do-you-style-placeholder-text) <span class="intermediate">Intermediate</span>
53. [How do you style selection color (`::selection`)?](#q53-how-do-you-style-selection-color-::selection) <span class="intermediate">Intermediate</span>
54. [How do you use CSS Variables for spacing and typography scales?](#q54-how-do-you-use-css-variables-for-spacing-and-typography-scales) <span class="intermediate">Intermediate</span>
55. [How do you use `calc()` function?](#q55-how-do-you-use-calc-function) <span class="intermediate">Intermediate</span>
56. [How do you use `clamp()` for responsive typography?](#q56-how-do-you-use-clamp-for-responsive-typography) <span class="intermediate">Intermediate</span>
57. [How do you use viewport units (`vw`, `vh`, `dvh`, `lvh`)?](#q57-how-do-you-use-viewport-units-vw-vh-dvh-lvh) <span class="intermediate">Intermediate</span>
58. [How do you handle notch areas on mobile (`safe-area-inset`)?](#q58-how-do-you-handle-notch-areas-on-mobile-safe-area-inset) <span class="intermediate">Intermediate</span>
59. [How do you support high contrast mode?](#q59-how-do-you-support-high-contrast-mode) <span class="intermediate">Intermediate</span>
60. [How do you use `@media (prefers-reduced-motion)`?](#q60-how-do-you-use-@media-prefers-reduced-motion) <span class="intermediate">Intermediate</span>
61. [How do you use `@supports` to check for feature support?](#q61-how-do-you-use-@supports-to-check-for-feature-support) <span class="intermediate">Intermediate</span>
62. [How do you use `@font-face` to load custom fonts?](#q62-how-do-you-use-@font-face-to-load-custom-fonts) <span class="intermediate">Intermediate</span>
63. [How do you use `font-display: swap` for performance?](#q63-how-do-you-use-font-display:-swap-for-performance) <span class="intermediate">Intermediate</span>
64. [How do you prevent text selection (`user-select`)?](#q64-how-do-you-prevent-text-selection-user-select) <span class="intermediate">Intermediate</span>
65. [How do you enable hardware acceleration for animations?](#q65-how-do-you-enable-hardware-acceleration-for-animations) <span class="intermediate">Intermediate</span>
66. [How do you style a `details` and `summary` element?](#q66-how-do-you-style-a-details-and-summary-element) <span class="intermediate">Intermediate</span>
67. [How do you style a `range` input slider?](#q67-how-do-you-style-a-range-input-slider) <span class="intermediate">Intermediate</span>
68. [How do you style a file input?](#q68-how-do-you-style-a-file-input) <span class="intermediate">Intermediate</span>
69. [How do you create a custom toggle switch?](#q69-how-do-you-create-a-custom-toggle-switch) <span class="intermediate">Intermediate</span>
70. [How do you create a pure CSS dropdown menu?](#q70-how-do-you-create-a-pure-css-dropdown-menu) <span class="intermediate">Intermediate</span>
71. [How do you create a pure CSS modal (using `:target` or checkbox hack)?](#q71-how-do-you-create-a-pure-css-modal-using-:target-or-checkbox-hack) <span class="intermediate">Intermediate</span>
72. [How do you create a pure CSS accordion?](#q72-how-do-you-create-a-pure-css-accordion) <span class="intermediate">Intermediate</span>
73. [How do you create a pure CSS tab system?](#q73-how-do-you-create-a-pure-css-tab-system) <span class="intermediate">Intermediate</span>
74. [How do you use `counters` for automatic numbering?](#q74-how-do-you-use-counters-for-automatic-numbering) <span class="intermediate">Intermediate</span>
75. [How do you use `content` property in pseudo-elements?](#q75-how-do-you-use-content-property-in-pseudo-elements) <span class="intermediate">Intermediate</span>
76. [How do you handle text overflow in a table cell?](#q76-how-do-you-handle-text-overflow-in-a-table-cell) <span class="intermediate">Intermediate</span>
77. [How do you make a table responsive (scrollable or stacked)?](#q77-how-do-you-make-a-table-responsive-scrollable-or-stacked) <span class="intermediate">Intermediate</span>
78. [How do you style alternate table rows?](#q78-how-do-you-style-alternate-table-rows) <span class="intermediate">Intermediate</span>
79. [How do you stick a table header?](#q79-how-do-you-stick-a-table-header) <span class="intermediate">Intermediate</span>
80. [How do you implement print styles (`@media print`)?](#q80-how-do-you-implement-print-styles-@media-print) <span class="intermediate">Intermediate</span>
81. [How do you hide elements in print view?](#q81-how-do-you-hide-elements-in-print-view) <span class="intermediate">Intermediate</span>
82. [How do you force page breaks in print?](#q82-how-do-you-force-page-breaks-in-print) <span class="intermediate">Intermediate</span>
83. [How do you use `shape-outside` for text wrapping around images?](#q83-how-do-you-use-shape-outside-for-text-wrapping-around-images) <span class="intermediate">Intermediate</span>
84. [How do you use `writing-mode` for vertical text?](#q84-how-do-you-use-writing-mode-for-vertical-text) <span class="intermediate">Intermediate</span>
85. [How do you use `direction: rtl` for right-to-left languages?](#q85-how-do-you-use-direction:-rtl-for-right-to-left-languages) <span class="intermediate">Intermediate</span>
86. [How do you use `text-align-last` for justified text?](#q86-how-do-you-use-text-align-last-for-justified-text) <span class="intermediate">Intermediate</span>
87. [How do you use `text-decoration` styling (color, style, thickness)?](#q87-how-do-you-use-text-decoration-styling-color-style-thickness) <span class="intermediate">Intermediate</span>
88. [How do you use `text-transform`?](#q88-how-do-you-use-text-transform) <span class="intermediate">Intermediate</span>
89. [How do you use `letter-spacing` and `word-spacing`?](#q89-how-do-you-use-letter-spacing-and-word-spacing) <span class="beginner">Beginner</span>
90. [How do you use `white-space` property?](#q90-how-do-you-use-white-space-property) <span class="intermediate">Intermediate</span>
91. [How do you use `word-break` and `overflow-wrap`?](#q91-how-do-you-use-word-break-and-overflow-wrap) <span class="intermediate">Intermediate</span>
92. [How do you use `hyphens` for auto-hyphenation?](#q92-how-do-you-use-hyphens-for-auto-hyphenation) <span class="intermediate">Intermediate</span>
93. [How do you use `caret-color`?](#q93-how-do-you-use-caret-color) <span class="beginner">Beginner</span>
94. [How do you use `pointer-events`?](#q94-how-do-you-use-pointer-events) <span class="intermediate">Intermediate</span>
95. [How do you use `cursor` property?](#q95-how-do-you-use-cursor-property) <span class="beginner">Beginner</span>
96. [How do you use `outline` vs `border`?](#q96-how-do-you-use-outline-vs-border) <span class="intermediate">Intermediate</span>
97. [How do you use `box-shadow` for elevation?](#q97-how-do-you-use-box-shadow-for-elevation) <span class="beginner">Beginner</span>
98. [How do you use `border-radius` for different shapes?](#q98-how-do-you-use-border-radius-for-different-shapes) <span class="beginner">Beginner</span>
99. [How do you use `display: contents`?](#q99-how-do-you-use-display:-contents) <span class="advanced">Advanced</span>
100. [How do you use `gap` in Flexbox?](#q100-how-do-you-use-gap-in-flexbox) <span class="beginner">Beginner</span>
101. [How do you use Logical Properties (`margin-block`, `padding-inline`)?](#q101-how-do-you-use-logical-properties-margin-block-padding-inline) <span class="intermediate">Intermediate</span>
102. [How do you use `inset` property?](#q102-how-do-you-use-inset-property) <span class="intermediate">Intermediate</span>
103. [How do you use `place-items` (Centering Trick)?](#q103-how-do-you-use-place-items-centering-trick) <span class="intermediate">Intermediate</span>

---

<a id="q1"></a>
### Q1: How do you implement a responsive 12-column grid using CSS Grid?

**Difficulty**: Intermediate

**Strategy**:
The 12-column grid is the industry standard for responsive layouts, mirroring frameworks like Bootstrap but without the overhead. CSS Grid's `repeat()` and `fr` unit make this trivial to implement natively. In interviews, demonstrate that you understand `span` for column allocation and media queries for mobile stacking. A common pitfall is forgetting to handle the mobile breakpoint where columns should collapse to full width.

**Strategy:**
**Difficulty: Intermediate**



CSS Grid makes creating complex layouts easy.
We can define a grid with 12 repeating columns of equal width (`1fr`) and a gap.
We can then place items on this grid spanning multiple columns.

**Code Snippet:**
```css
.container {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 20px;
}

.header {
  grid-column: 1 / -1; /* Spans all columns */
}

.sidebar {
  grid-column: span 3; /* Spans 3 columns */
}

.content {
  grid-column: span 9; /* Spans 9 columns */
}

@media (max-width: 768px) {
  .sidebar, .content {
    grid-column: 1 / -1; /* Stack on mobile */
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q2"></a>
### Q2: How do you center an element absolutely both vertically and horizontally?

**Difficulty**: Intermediate

**Strategy**:
Centering is one of the most frequently asked CSS questions because it reveals whether you understand positioning and transform. The `top: 50%` + `translate(-50%, -50%)` technique works because percentage-based `top`/`left` references the parent, while percentage-based `translate` references the element itself. Be prepared to discuss modern alternatives like `place-items: center` with Grid, which is simpler but requires block-level layout control.

**Strategy:**
**Difficulty: Intermediate**



There are multiple ways (Flexbox/Grid are preferred), but for absolute positioning:
1. Set `top: 50%`, `left: 50%`.
2. Use `transform: translate(-50%, -50%)` to shift it back by half its own width/height.

**Code Snippet:**
```css
.parent {
  position: relative;
  height: 300px;
}

.child {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

/* Modern Alternative (if not absolute) */
/*
.parent {
  display: grid;
  place-items: center;
}
*/
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q3"></a>
### Q3: How do you implement a sticky footer that stays at the bottom even with little content?

**Difficulty**: Intermediate

**Strategy**:
The sticky footer is a classic layout problem that tests your understanding of Flexbox's space distribution. The key insight is that `flex: 1` on the main content area tells it to grow and fill available space, naturally pushing the footer to the viewport bottom. Avoid the old negative-margin hacks. A common mistake is forgetting `min-height: 100vh` on the container, which prevents the flex layout from stretching the full viewport.

**Strategy:**
**Difficulty: Intermediate**



The "Sticky Footer" problem is solved easily with Flexbox.
Make the body (or wrapper) a flex container with `min-height: 100vh` and column direction.
Set `margin-top: auto` on the footer, or `flex-grow: 1` on the main content.

**Code Snippet:**
```css
body {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  margin: 0;
}

main {
  flex: 1; /* Takes up remaining space */
}

footer {
  background: #333;
  color: white;
  padding: 1rem;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q4"></a>
### Q4: How do you implement a pure CSS tooltip?

**Difficulty**: Intermediate

**Strategy**:
Pure CSS tooltips demonstrate mastery of pseudo-elements and the `attr()` function, which pulls values from HTML data attributes. This pattern avoids JavaScript for simple hover hints and keeps behavior declarative. The `pointer-events: none` on the tooltip prevents it from blocking clicks, and `white-space: nowrap` keeps text on one line. Remember that `content: attr()` only works in pseudo-elements, not on real elements.

**Strategy:**
**Difficulty: Intermediate**



Use a data attribute (e.g., `data-tooltip`) on the element.
Use the `::before` or `::after` pseudo-element to display the content of that attribute using `content: attr(data-tooltip)`.
Show it on hover.

**Code Snippet:**
```css
[data-tooltip] {
  position: relative;
  cursor: pointer;
}

[data-tooltip]::after {
  content: attr(data-tooltip);
  position: absolute;
  bottom: 100%;
  left: 50%;
  transform: translateX(-50%);
  background: black;
  color: white;
  padding: 5px 10px;
  border-radius: 4px;
  white-space: nowrap;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.2s;
}

[data-tooltip]:hover::after {
  opacity: 1;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q5"></a>
### Q5: How do you create a custom checkbox using CSS?

**Difficulty**: Intermediate

**Strategy**:
Custom form controls are a common interview topic because they test your understanding of accessibility alongside styling. The key technique is hiding the native input visually while keeping it focusable and screen-reader accessible, then using the sibling combinator (`~`) with `:checked` to style the custom element. Never use `display: none` to hide the input, as that removes it from the keyboard tab order and breaks accessibility.

**Strategy:**
**Difficulty: Intermediate**



1. Hide the default input (`opacity: 0` or `appearance: none`).
2. Style a label (or pseudo-element) connected to it.
3. Use the `:checked` pseudo-class to change the style of the label/sibling.

**Code Snippet:**
```css
/* Hide native checkbox visually but keep accessible */
.custom-checkbox input {
  position: absolute;
  opacity: 0;
  cursor: pointer;
}

/* Create custom box */
.checkmark {
  height: 20px;
  width: 20px;
  background-color: #eee;
  display: inline-block;
}

/* On checked, change background */
.custom-checkbox input:checked ~ .checkmark {
  background-color: #2196F3;
}

/* Create check indicator */
.checkmark::after {
  content: "";
  display: none;
  /* ... styles for the check mark ... */
}

.custom-checkbox input:checked ~ .checkmark::after {
  display: block;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q6"></a>
### Q6: How do you implement Dark Mode using CSS Variables?

**Difficulty**: Intermediate

**Strategy**:
CSS custom properties (variables) are the foundation of theming systems in modern web apps. Defining colors in `:root` and overriding them with a data-attribute selector or `prefers-color-scheme` media query creates a clean separation between theme definitions and component styles. The `transition` on background-color provides a polished switch. In real-world apps, pair the data-attribute approach with JavaScript to persist user preference in localStorage.

**Strategy:**
**Difficulty: Advanced**



Define color variables in `:root`.
Override them in a `[data-theme='dark']` selector or `@media (prefers-color-scheme: dark)`.

**Code Snippet:**
```css
:root {
  --bg-color: white;
  --text-color: black;
}

[data-theme='dark'] {
  --bg-color: #121212;
  --text-color: #ffffff;
}

body {
  background-color: var(--bg-color);
  color: var(--text-color);
  transition: background-color 0.3s;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q7"></a>
### Q7: How do you create a responsive aspect ratio box (e.g., 16:9 video embed)?

**Difficulty**: Intermediate

**Strategy**:
Maintaining aspect ratios is essential for responsive video embeds, image placeholders, and card layouts. The modern `aspect-ratio` property is the preferred approach and has broad browser support. The older padding-top hack exploits the fact that vertical padding percentages resolve against the element's width, not height. In interviews, mention both approaches to show awareness of legacy techniques while favoring the modern solution.

**Strategy:**
**Difficulty: Advanced**



Modern CSS has the `aspect-ratio` property.
Old hack: Use `padding-top` percentage on a container (percentage is based on width).

**Code Snippet:**
```css
/* Modern Way */
.video-container {
  width: 100%;
  aspect-ratio: 16 / 9;
  background: #000;
}

/* Old "Padding Hack" */
.aspect-ratio-box {
  width: 100%;
  padding-top: 56.25%; /* 9/16 = 0.5625 */
  position: relative;
}

.aspect-ratio-box > iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q8"></a>
### Q8: How do you truncate text with an ellipsis (...) for a single line and multiple lines?

**Difficulty**: Intermediate

**Strategy**:
Text truncation appears constantly in real-world UIs -- card titles, table cells, notification text -- so interviewers expect fluency here. Single-line truncation requires all three properties working together: `white-space: nowrap` prevents wrapping, `overflow: hidden` clips the overflow, and `text-overflow: ellipsis` adds the visual indicator. For multi-line, the `-webkit-line-clamp` approach is widely supported despite its vendor prefix and uses the older flexbox box model.

**Strategy:**
**Difficulty: Advanced**



Single line: `text-overflow: ellipsis`, `white-space: nowrap`, `overflow: hidden`.
Multi-line: Use `line-clamp` (webkit prefixed, but standardizing).

**Code Snippet:**
```css
/* Single Line */
.truncate-single {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

/* Multi Line (3 lines) */
.truncate-multi {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q9"></a>
### Q9: How do you use Container Queries to build component-based responsive styles?

**Difficulty**: Intermediate

**Strategy**:
Container queries are a paradigm shift from media queries because they enable truly reusable components that respond to their own container size, not the viewport. This is critical for design systems where the same card component may appear in a sidebar or a full-width page. You must declare `container-type` on the parent before `@container` rules will work. This feature shows interviewers you keep up with modern CSS evolution.

**Strategy:**
**Difficulty: Advanced**



Container Queries allow components to style themselves based on the size of their *container*, not the viewport.
1. Mark a container as a query container: `container-type: inline-size`.
2. Use `@container` rule.

**Code Snippet:**
```css
.card-container {
  container-type: inline-size;
}

.card {
  display: flex;
  flex-direction: column;
}

/* If container is wider than 400px */
@container (min-width: 400px) {
  .card {
    flex-direction: row;
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q10"></a>
### Q10: How do you optimize CSS performance (Painting and Layout)?

**Difficulty**: Intermediate

**Strategy**:
CSS performance optimization separates senior developers from juniors. The browser rendering pipeline goes through Style, Layout, Paint, and Composite -- properties like `transform` and `opacity` skip Layout and Paint entirely, going straight to the GPU compositor. Animating `width`, `height`, or `top` forces the browser to recalculate layout for the entire subtree. Use `will-change` judiciously, as overusing it wastes GPU memory.

**Strategy:**
**Difficulty: Advanced**



1. Use `transform` and `opacity` for animations (compositor only properties).
2. Avoid animating `width`, `height`, `top`, `left` (triggers layout/reflow).
3. Use `will-change` sparingly to hint browser.
4. Reduce selector complexity (though less critical in modern engines).

**Code Snippet:**
```css
/* Bad Performance (Triggers Layout) */
.box:hover {
  width: 200px; 
  top: 20px;
}

/* Good Performance (Compositor only) */
.box:hover {
  transform: scale(1.5) translateY(20px);
}

.animating-element {
  will-change: transform;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q11"></a>
### Q11: How do you implement a parallax scrolling effect purely in CSS?

**Difficulty**: Intermediate

**Strategy**:
CSS-only parallax leverages 3D transforms without JavaScript scroll listeners, making it more performant. Setting `perspective` on the scroll container and `translateZ` on child layers creates the illusion of depth because the browser scales elements based on their Z-position. A critical implementation detail is `overflow-y: auto` with `perspective` on the same element. Be aware this technique can cause issues on some mobile browsers.

**Strategy:**
**Difficulty: Advanced**



Use `perspective` on a container and `translateZ` on children to create depth.
Elements "further away" (negative Z) move slower than elements closer.

**Code Snippet:**
```css
.parallax-wrapper {
  height: 100vh;
  overflow-x: hidden;
  overflow-y: auto;
  perspective: 1px;
}

.parallax-section {
  position: relative;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.bg-image {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: -1;
  /* Push back and scale up to cover viewport */
  transform: translateZ(-1px) scale(2); 
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q12"></a>
### Q12: How do you ensure an element is visually hidden but accessible to screen readers?

**Difficulty**: Intermediate

**Strategy**:
The `.sr-only` (screen-reader-only) pattern is a staple of accessible web development and appears in every major CSS framework. Using `display: none` or `visibility: hidden` completely removes the element from the accessibility tree, making it invisible to assistive technology. The clip-based approach keeps the element in the DOM and accessible while rendering it invisible on screen. This class is essential for providing context to screen readers on icon buttons and skip-navigation links.

**Strategy:**
**Difficulty: Advanced**



Don't use `display: none` or `visibility: hidden` (removes from accessibility tree).
Use a utility class that clips the element to 1px rect.

**Code Snippet:**
```css
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
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q13"></a>
### Q13: How do you implement a CSS Triangle?

**Difficulty**: Intermediate

**Strategy**:
CSS triangles are a classic interview trick question that tests your understanding of the CSS box model and border rendering. When an element has zero width and height, borders from opposing sides meet at diagonal edges, creating triangular shapes. By making three borders transparent and one colored, you control which triangle is visible. While largely replaced by `clip-path` and SVG in production, this technique still appears in legacy codebases and demonstrates deep CSS knowledge.

**Strategy:**
**Difficulty: Advanced**



Use transparent borders. A box with 0 width/height and thick borders creates triangles where borders meet.

**Code Snippet:**
```css
.triangle-up {
  width: 0;
  height: 0;
  border-left: 25px solid transparent;
  border-right: 25px solid transparent;
  border-bottom: 50px solid #555;
}

.triangle-right {
  width: 0;
  height: 0;
  border-top: 25px solid transparent;
  border-bottom: 25px solid transparent;
  border-left: 50px solid #555;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q14"></a>
### Q14: How do you prevent content layout shift (CLS) for images?

**Difficulty**: Intermediate

**Strategy**:
Cumulative Layout Shift (CLS) is a Core Web Vital that Google uses for search ranking, making it critical in production. When images lack explicit dimensions, the browser cannot reserve space and content jumps when the image loads. Always set `width` and `height` attributes in HTML combined with `max-width: 100%; height: auto` in CSS for responsive images. The `aspect-ratio` CSS property provides a modern fallback when HTML attributes are not available.

**Strategy:**
**Difficulty: Advanced**



Always define `width` and `height` attributes (or aspect-ratio) so the browser reserves space before the image loads.





```css
/* CSS */
.responsive-img {
  max-width: 100%;
  height: auto;
  /* Ensure aspect ratio is preserved in older browsers if needed */
  aspect-ratio: 800 / 600;
}
```

**Code Snippet:**
```css
<!-- HTML -->
<img src="image.jpg" width="800" height="600" alt="Example" class="responsive-img" />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q15"></a>
### Q15: How do you implement a masonry layout using CSS only?

**Difficulty**: Intermediate

**Strategy**:
Masonry layouts (like Pinterest) remain one of the trickiest layouts to achieve with pure CSS. The multi-column approach (`column-count`) is the most reliable pure-CSS solution but orders items top-to-bottom instead of left-to-right, which may not match design intent. The experimental `grid-template-rows: masonry` in CSS Grid solves this natively but has limited browser support. For production, JavaScript-based libraries like Masonry.js are still common, but demonstrating the CSS-only approach shows initiative.

**Strategy:**
**Difficulty: Advanced**



Pure CSS masonry is tricky.
1. **Multi-column:** `column-count` works best for top-to-bottom ordering.
2. **Grid:** Can only do masonry if row height is uniform or using experimental `grid-template-rows: masonry`.

**Code Snippet (Multi-column approach):**

**Code Snippet:**
```css
.masonry-container {
  column-count: 3;
  column-gap: 1em;
}

.masonry-item {
  display: inline-block; /* Prevents break inside */
  width: 100%;
  margin-bottom: 1em;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q16"></a>
### Q16: How do you use Flexbox for a navigation bar?

**Difficulty**: Intermediate

**Strategy**:
Flexbox is the go-to solution for navigation bars because it handles both horizontal distribution and vertical alignment in a single declaration. The `space-between` value pushes the logo to one end and navigation links to the other, which is the most common nav pattern. For responsive behavior, wrap nav links in a `<ul>` and switch to `flex-direction: column` on mobile breakpoints.

**Strategy:**
Use `display: flex` on the container. `justify-content: space-between` pushes logo and links apart. `align-items: center` vertically centers them.

**Code Snippet:**
```css
.nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q17"></a>
### Q17: How do you use `flex-grow`, `flex-shrink`, and `flex-basis`?

**Difficulty**: Intermediate

**Strategy**:
Understanding the three components of `flex` is fundamental to mastering Flexbox layouts. The `flex` shorthand (`flex: grow shrink basis`) is preferred over individual properties because it resets all three values intelligently and avoids common pitfalls with `flex-basis: auto`. The shorthand `flex: 1` is equivalent to `flex: 1 1 0%`, which distributes space equally. A frequent interview mistake is confusing `flex-basis` with `width` -- basis sets the initial size before free space is distributed.

**Strategy:**
`flex-grow`: How much space to take (0 default). `flex-shrink`: How much to shrink (1 default). `flex-basis`: Initial size. `flex: 1` sets grow:1, shrink:1, basis:0%.

**Code Snippet:**
```css
.item {
  flex: 1 0 200px;
  /* grow: 1, shrink: 0, basis: 200px */
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q18"></a>
### Q18: How do you implement a sidebar layout with Flexbox?

**Difficulty**: Intermediate

**Strategy**:
The sidebar layout is one of the most common page-level patterns and Flexbox handles it elegantly. The sidebar gets a fixed basis via `flex: 0 0 250px` (no grow, no shrink, 250px basis), while the main content uses `flex: 1` to consume all remaining space. This approach avoids the fragile float-based sidebars of the past. For responsive behavior, switch to `flex-direction: column` on smaller screens to stack the sidebar above the content.

**Strategy:**
Container: `display: flex`. Sidebar: Fixed width or `flex: 0 0 250px`. Main content: `flex: 1` to take remaining space.

**Code Snippet:**
```css
.container {
  display: flex;
}
.sidebar {
  flex: 0 0 250px;
}
.main {
  flex: 1;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q19"></a>
### Q19: How do you align items in a grid using `justify-items` and `align-items`?

**Difficulty**: Intermediate

**Strategy**:
Grid alignment properties control how items are placed within their grid cells, and confusing them with Flexbox alignment is a common interview mistake. In Grid, `justify-items` aligns along the inline (row) axis and `align-items` along the block (column) axis, and both apply to individual grid items within their cells. The default is `stretch`, which is why grid children expand to fill their cells unless you override it. For centering a single item in its cell, `place-items: center` is the shorthand.

**Strategy:**
`justify-items`: Horizontal alignment (start, center, end, stretch). `align-items`: Vertical alignment. Defaults to `stretch`.

**Code Snippet:**
```css
.grid {
  display: grid;
  justify-items: center;
  align-items: center;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q20"></a>
### Q20: How do you use `minmax()` in CSS Grid?

**Difficulty**: Intermediate

**Strategy**:
`minmax()` is the key to building truly responsive grids without media queries. Combined with `auto-fit` or `auto-fill`, it creates a grid that automatically wraps items into as many columns as will fit. `minmax(200px, 1fr)` means each column is at least 200px wide but shares any extra space equally. The difference between `auto-fit` (collapses empty tracks) and `auto-fill` (preserves empty tracks) is a common follow-up question in interviews.

**Strategy:**
Defines a size range. `minmax(100px, 1fr)` means at least 100px, but stretch to fill 1fr if space allows.

**Code Snippet:**
```css
.grid {
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q21"></a>
### Q21: How do you create overlapping elements with CSS Grid?

**Difficulty**: Intermediate

**Strategy**:
One of CSS Grid's unique strengths is that multiple items can occupy the same grid cell, creating overlapping layouts without `position: absolute`. This is useful for hero sections, image overlays, and decorative elements. Later DOM elements naturally stack on top of earlier ones, and `z-index` controls the order within the same stacking context. This approach is more maintainable than absolute positioning because items remain in the document flow.

**Strategy:**
Place items in the same grid cell(s) using line numbers. Later items stack on top (control with z-index if needed).

**Code Snippet:**
```css
.item1 { grid-column: 1 / 3; grid-row: 1; }
.item2 { grid-column: 2 / 4; grid-row: 1; opacity: 0.8; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q22"></a>
### Q22: How do you use `z-index` and stacking contexts effectively?

**Difficulty**: Intermediate

**Strategy**:
Stacking contexts are one of the most misunderstood CSS concepts and a frequent source of bugs in complex UIs. A stacking context is created not just by `z-index` but also by `opacity` less than 1, `transform`, `filter`, `will-change`, and several other properties. Once a stacking context is created, `z-index` values of children cannot escape it to overlap elements in a sibling context. Understanding this prevents the "z-index arms race" of ever-increasing values.

**Strategy:**
`z-index` only works on positioned elements (relative, absolute, fixed, sticky) or flex/grid children. A new stacking context is created by opacity < 1, transform, filter, etc.

**Code Snippet:**
```css
.top {
  position: relative;
  z-index: 10;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q23"></a>
### Q23: How do you debug `z-index` issues?

**Difficulty**: Intermediate

**Strategy**:
Debugging z-index issues requires a systematic approach because the root cause is usually a parent stacking context, not the element itself. Start by checking that the element has a positioning context set. Then trace up the DOM tree for properties that create stacking contexts (`transform`, `opacity`, `filter`). Chrome DevTools' "Layers" panel and the "DOM" panel with "Show stacking context" option visualize these hierarchies and help identify where containment is happening.

**Strategy:**
Check if the element has `position` set (if not flex/grid child). Check parent stacking contexts (e.g., parent has `overflow: hidden` or `opacity`). Use browser devtools 'Layers' view.

**Code Snippet:**
```css
/* Debug helper */
* { outline: 1px solid red; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q24"></a>
### Q24: How do you style a scrollbar using `::-webkit-scrollbar`?

**Difficulty**: Intermediate

**Strategy**:
Custom scrollbars improve visual consistency but come with a critical caveat: `::-webkit-scrollbar` only works in Chromium and Safari browsers. For Firefox, use the `scrollbar-width` and `scrollbar-color` standard properties. In production, consider whether custom scrollbars are necessary at all, as users may rely on the OS-level scrollbar for usability. Always test with both light and dark themes since scrollbars overlay the content.

**Strategy:**
Use pseudo-elements: `::-webkit-scrollbar` (width), `::-webkit-scrollbar-track` (background), `::-webkit-scrollbar-thumb` (handle).

**Code Snippet:**
```css
::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-thumb { background: #888; border-radius: 4px; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q25"></a>
### Q25: How do you use `scroll-behavior: smooth`?

**Difficulty**: Intermediate

**Strategy**:
`scroll-behavior: smooth` is the simplest way to add smooth scrolling for in-page anchor navigation, replacing JavaScript `scrollIntoView()` calls. Apply it to the `html` element for global behavior or to specific scroll containers. Pair it with `prefers-reduced-motion` to disable smooth scrolling for users who experience motion sensitivity, as abrupt stops during smooth scrolling can cause discomfort.

**Strategy:**
Apply to `html` or a scroll container to enable smooth scrolling for anchor links.

**Code Snippet:**
```css
html {
  scroll-behavior: smooth;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q26"></a>
### Q26: How do you use `scroll-snap-type` for snapping sections?

**Difficulty**: Intermediate

**Strategy**:
Scroll snapping creates full-screen section layouts, image carousels, and paginated interfaces without JavaScript. The `mandatory` value forces the scroll to always end at a snap point, while `proximity` only snaps when close to one. Use `mandatory` for fullscreen sections and `proximity` for content lists where forcing snap could feel jarring. Always combine with `overflow-y: scroll` and explicit heights on snap children.

**Strategy:**
Container: `scroll-snap-type: y mandatory`. Children: `scroll-snap-align: start`.

**Code Snippet:**
```css
.container {
  scroll-snap-type: y mandatory;
  overflow-y: scroll;
  height: 100vh;
}
.section {
  scroll-snap-align: start;
  height: 100vh;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q27"></a>
### Q27: How do you implement a CSS reset or normalize?

**Difficulty**: Intermediate

**Strategy**:
A CSS reset strips browser-default styles to create a consistent baseline across all browsers, which is essential for predictable layouts. The universal selector reset (`*`) is the simplest approach, but production resets like `modern-normalize` or Andy Bell's modern reset handle more edge cases like form elements and media elements. Always pair a reset with `box-sizing: border-box` to prevent padding and borders from breaking your width calculations.

**Strategy:**
Remove default margins/paddings to ensure consistency. Minimal reset: `* { margin: 0; padding: 0; box-sizing: border-box; }`.

**Code Snippet:**
```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q28"></a>
### Q28: How do you use `box-sizing: border-box` globally?

**Difficulty**: Intermediate

**Strategy**:
`border-box` is considered a best practice for every production stylesheet because it changes the CSS box model so that `padding` and `border` are included in the element's declared `width` and `height`. Without it, a `width: 200px` element with `padding: 20px` becomes 240px wide, breaking layouts. Applying it via the universal selector with `inherit` on the root ensures third-party components also adopt it consistently.

**Strategy:**
Apply it to `*` and pseudo-elements. It includes padding and border in the element's total width/height.

**Code Snippet:**
```css
*, *::before, *::after {
  box-sizing: border-box;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q29"></a>
### Q29: How do you style inputs to look consistent across browsers?

**Difficulty**: Intermediate

**Strategy**:
Form elements are notoriously inconsistent across browsers, with Safari, Chrome, and Firefox each applying different default styles. The `appearance: none` property strips all native browser styling, giving you a blank canvas. The critical `font: inherit` declaration prevents inputs from using the system font when the rest of the page uses a custom font. Always test styled inputs on multiple browsers, particularly date and select inputs which remain difficult to fully customize.

**Strategy:**
Reset `appearance: none`, border, background, and font inheritance.

**Code Snippet:**
```css
input {
  appearance: none;
  border: 1px solid #ccc;
  font: inherit;
  padding: 0.5em;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q30"></a>
### Q30: How do you remove the default outline on focus (and what to replace it with)?

**Difficulty**: Intermediate

**Strategy**:
Removing focus outlines without providing an alternative is one of the most common accessibility violations on the web. The outline is the primary visual indicator for keyboard users navigating with Tab. The modern approach uses `:focus-visible` to show the ring only for keyboard navigation, not mouse clicks. If you replace the outline with `box-shadow`, ensure it meets WCAG contrast requirements and remains visible on all background colors.

**Strategy:**
Never set `outline: none` without a replacement. Use `box-shadow` or a custom `outline` for accessibility.

**Code Snippet:**
```css
button:focus-visible {
  outline: 2px solid blue;
  outline-offset: 2px;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q31"></a>
### Q31: How do you style a broken image using `img::before`?

**Difficulty**: Intermediate

**Strategy**:
Broken images degrade the user experience, but CSS can provide a graceful fallback. The `::before` pseudo-element on an `img` only renders when the image fails to load, because a replaced element normally has no pseudo-element support. This creates an opportunity to display a custom error message and background. This technique works in Chrome, Firefox, and Edge but has inconsistent behavior in Safari, so always provide an `alt` attribute as the primary fallback.

**Strategy:**
The `::before` and `::after` pseudo-elements on `img` only render if the image fails to load. Use absolute positioning to cover the broken icon.

**Code Snippet:**
```css
img {
  position: relative;
}
img::before {
  content: 'Image failed';
  position: absolute;
  top: 0; left: 0;
  width: 100%; height: 100%;
  background: #eee;
  display: flex; align-items: center; justify-content: center;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q32"></a>
### Q32: How do you style list markers using `::marker`?

**Difficulty**: Intermediate

**Strategy**:
The `::marker` pseudo-element provides direct styling of list bullets and numbered markers without the older workaround of `list-style: none` plus `::before` pseudo-elements. It supports a limited set of properties: `color`, `font-*`, `content`, and `animation`. This is especially useful for customizing summary element disclosure markers and creating visually consistent bullet styles across different list types.

**Strategy:**
Use the `::marker` pseudo-element on `li` or `summary`. Supports `color`, `font-*`, `content`.

**Code Snippet:**
```css
li::marker {
  color: red;
  content: '👉 ';
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q33"></a>
### Q33: How do you use `object-fit` and `object-position` for images?

**Difficulty**: Intermediate

**Strategy**:
`object-fit` solves the common problem of images distorting when placed in fixed-dimension containers like cards or avatars. `cover` fills the container while maintaining aspect ratio (cropping overflow), while `contain` shows the full image with possible letterboxing. The `object-position` property controls which part of the image remains visible after cropping. This is conceptually similar to `background-size` but works directly on `img`, `video`, and `iframe` elements.

**Strategy:**
`object-fit: cover` crops image to fill container. `object-position` adjusts the crop focus.

**Code Snippet:**
```css
img {
  width: 100%;
  height: 200px;
  object-fit: cover;
  object-position: center top;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q34"></a>
### Q34: How do you use `background-size: cover` vs `contain`?

**Difficulty**: Intermediate

**Strategy**:
`background-size: cover` and `contain` control how background images fill their container and are fundamental to hero sections and banner designs. `cover` ensures no empty space by scaling up and cropping, making it ideal for full-bleed backgrounds. `contain` ensures the entire image is visible, which is useful for logos or watermarks. Always pair `cover` with `background-position: center` to ensure the focal point of the image stays visible after cropping.

**Strategy:**
`cover`: Fills entire area, cropping if needed. `contain`: Shows entire image, leaving space if needed.

**Code Snippet:**
```css
.hero {
  background-image: url('bg.jpg');
  background-size: cover;
  background-position: center;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q35"></a>
### Q35: How do you create a gradient background?

**Difficulty**: Intermediate

**Strategy**:
Gradients are set as `background-image`, not `background-color`, which means they layer on top of background colors and can be combined with other images. CSS supports three gradient types: `linear-gradient` for directional blends, `radial-gradient` for circular/elliptical fades, and `conic-gradient` for pie-chart-like patterns. You can chain multiple gradients and use `repeating-*` variants for striped patterns. Gradients also work in `border-image` and `list-style-image`.

**Strategy:**
Use `linear-gradient`, `radial-gradient`, or `conic-gradient` as `background-image`.

**Code Snippet:**
```css
.bg {
  background-image: linear-gradient(to right, #f00, #00f);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q36"></a>
### Q36: How do you create a text gradient?

**Difficulty**: Intermediate

**Strategy**:
Text gradients are a popular design trend that combines `background-clip: text` with a transparent `color` to render gradient fills on text characters. The gradient is applied as a background, then clipped to the text shape. The `-webkit-` prefix is still needed in some browsers for `background-clip: text`. Note that this technique makes text unselectable in some browsers, so use it on headings rather than body text.

**Strategy:**
Background clip text + transparent text color.

**Code Snippet:**
```css
.text-gradient {
  background: linear-gradient(to right, gold, red);
  -webkit-background-clip: text;
  color: transparent;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q37"></a>
### Q37: How do you use `clip-path` to create shapes?

**Difficulty**: Intermediate

**Strategy**:
`clip-path` is the modern replacement for CSS hack shapes (like border triangles), offering clean geometric clipping without pseudo-elements. `polygon()` accepts percentage-based coordinates and can create any straight-edged shape, while `circle()` and `ellipse()` handle curved edges. Tools like Clippy (bennettfeely.com/clippy) generate polygon points visually. Unlike `overflow: hidden`, `clip-path` also clips shadows and borders. Animated clip-paths create dramatic reveal effects.

**Strategy:**
Defines a clipping region. Parts outside are hidden. Use `polygon()`, `circle()`, `ellipse()`, or `path()`.

**Code Snippet:**
```css
.triangle {
  clip-path: polygon(50% 0%, 0% 100%, 100% 100%);
  background: red;
  width: 100px; height: 100px;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q38"></a>
### Q38: How do you use `mask-image` for transparency masks?

**Difficulty**: Intermediate

**Strategy**:
CSS masking uses the alpha channel of an image or gradient to control element visibility, similar to layer masks in design tools. Black pixels show the element, transparent pixels hide it, and gray pixels create partial transparency. A common use case is fading an element's edges with a gradient mask. The `-webkit-` prefix is still required in Safari. Masking differs from `clip-path` in that it supports soft edges and partial transparency.

**Strategy:**
Uses an image (alpha channel) to mask element visibility. Black = visible, Transparent = hidden.

**Code Snippet:**
```css
.masked {
  -webkit-mask-image: linear-gradient(to bottom, black, transparent);
  mask-image: linear-gradient(to bottom, black, transparent);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q39"></a>
### Q39: How do you use `backdrop-filter` for glassmorphism?

**Difficulty**: Intermediate

**Strategy**:
`backdrop-filter` applies visual effects to the content behind an element, which is the key to the popular glassmorphism design trend. A semi-transparent background (`rgba` with low alpha) lets underlying content show through, while `backdrop-filter: blur()` softens it. Performance can be an issue on lower-end devices because the browser must composite layers in real-time. Always provide a fallback solid or semi-transparent background for browsers that do not support it.

**Strategy:**
Applies filter to area *behind* the element. Requires semi-transparent background.

**Code Snippet:**
```css
.glass {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q40"></a>
### Q40: How do you use `filter` for image effects (blur, grayscale)?

**Difficulty**: Intermediate

**Strategy**:
The CSS `filter` property applies graphical effects like blur, brightness, contrast, and grayscale directly to elements, making it essential for image-heavy UIs and interactive hover states. Filters are composited on the GPU, so they perform well for visual effects without requiring image assets. A common pitfall is stacking too many filters on large elements, which can hurt performance on mobile devices.


**Code Snippet:**
```css
img:hover {
  filter: grayscale(100%) blur(2px);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q41"></a>
### Q41: How do you use `mix-blend-mode` for blending effects?

**Difficulty**: Intermediate

**Strategy**:
`mix-blend-mode` controls how an element's colors blend with the content behind it, similar to layer blend modes in design tools like Photoshop. It is widely used for creative text-over-image effects, dark mode inversions, and overlay UIs without requiring pre-composited assets. Be aware that `mix-blend-mode` can be expensive to render when applied to large areas, so test performance on complex pages.


**Code Snippet:**
```css
.text {
  mix-blend-mode: difference;
  color: white;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q42"></a>
### Q42: How do you implement a loading spinner with CSS animations?

**Difficulty**: Intermediate

**Strategy**:
Loading spinners are a staple of UI development, and creating them with pure CSS avoids unnecessary JavaScript or image dependencies. The classic approach uses a circular element with a partially transparent border, animated with `@keyframes` rotation. A common mistake is forgetting `linear` timing for smooth continuous spinning, which otherwise causes stuttering at each loop boundary.


**Code Snippet:**
```css
@keyframes spin { to { transform: rotate(360deg); } }
.loader {
  width: 40px; height: 40px;
  border: 4px solid #ccc;
  border-top-color: #333;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q43"></a>
### Q43: How do you create a shake animation?

**Difficulty**: Intermediate

**Strategy**:
Shake animations provide immediate visual feedback for errors or invalid actions, making them a practical UX pattern interviewers look for. The technique uses `@keyframes` with alternating `translateX` values to create a rapid side-to-side motion. Keep the animation short (0.3s-0.5s) and combine it with `animation-fill-mode: forwards` so the element stays in its final resting position.

```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q44"></a>
### Q44: How do you pause an animation on hover?

**Difficulty**: Intermediate

**Strategy**:
`animation-play-state` gives you control over running CSS animations without JavaScript, enabling interactive pause/resume behavior purely through CSS. This is useful for carousels, loading indicators, or any continuously animated element that should freeze on user interaction. A best practice is to always provide a clear visual cue (like reduced opacity) so users know the animation is intentionally paused.

```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q45"></a>
### Q45: How do you use CSS transitions for hover effects?

**Difficulty**: Intermediate

**Strategy**:
CSS transitions provide smooth state changes between property values and are fundamental to polished UI interactions. The key rule is to always define the `transition` property on the base element state, not on the `:hover` state, so both entering and leaving transitions are smooth. A common mistake is transitioning expensive properties like `width` or `height` instead of using `transform` for better performance.


**Code Snippet:**
```css
.btn {
  background: blue;
  transition: background 0.3s ease;
}
.btn:hover {
  background: darkblue;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q46"></a>
### Q46: How do you use the `:not()` pseudo-class?

**Difficulty**: Intermediate

**Strategy**:
`:not()` is the negation pseudo-class that excludes elements matching a selector, useful for applying styles broadly while carving out exceptions. A common real-world pattern is `li:not(:last-child)` to add separators between items without a trailing one. Keep `:not()` selectors simple -- complex nested negations are hard to read, increase specificity, and can cause unexpected matching that is difficult to debug.


**Code Snippet:**
```css
li:not(:last-child) {
  border-bottom: 1px solid #ccc;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q47"></a>
### Q47: How do you use the `:has()` pseudo-class (parent selector)?

**Difficulty**: Intermediate

**Strategy**:
`:has()` is often called the "parent selector" and is one of the most impactful CSS features added in recent years, enabling styles based on descendant content. It solves long-standing patterns that previously required JavaScript, such as styling a form group differently when it contains an invalid input. A best practice is to keep `:has()` selectors reasonably specific, as complex queries can impact selector-matching performance.


**Code Snippet:**
```css
/* Style card if it contains an image */
.card:has(img) {
  padding: 0;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q48"></a>
### Q48: How do you use the `:is()` and `:where()` pseudo-classes?

**Difficulty**: Intermediate

**Strategy**:
`:is()` and `:where()` both reduce repetitive selector lists, but differ in specificity behavior that interviewers love to quiz you on. `:is()` adopts the specificity of its most specific argument, while `:where()` always has zero specificity, making it ideal for utility classes and themes that must be easily overridable. A common pitfall is using `:is()` in base styles where you later need overrides to win the specificity war.


**Code Snippet:**
```css
:is(h1, h2, h3) { margin-top: 0; }
:where(article) p { color: #666; /* easy to override */ }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q49"></a>
### Q49: How do you use `:nth-child()` and `:nth-of-type()`?

**Difficulty**: Intermediate

**Strategy**:
`:nth-child()` and `:nth-of-type()` are essential for targeting elements without adding classes, commonly used for zebra-striping tables, alternating grid layouts, and typographic styling. The critical distinction is that `:nth-child()` counts all sibling elements regardless of type, while `:nth-of-type()` only counts siblings of the same element type. A frequent mistake is using `:nth-child(2)` expecting the second paragraph when a heading precedes it.


**Code Snippet:**
```css
li:nth-child(odd) { background: #eee; }
p:nth-of-type(2) { font-weight: bold; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q50"></a>
### Q50: How do you use `::first-letter` and `::first-line`?

**Difficulty**: Intermediate

**Strategy**:
`::first-letter` and `::first-line` provide typographic control similar to print design, enabling drop caps and differentiated first-line styling without extra markup. They only work on block-level elements and have a specific set of properties they can apply. A common gotcha is that `::first-letter` will not work if there is whitespace or an inline element immediately inside the target before the text.


**Code Snippet:**
```css
p::first-letter {
  font-size: 2em;
  float: left;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q51"></a>
### Q51: How do you use attribute selectors?

**Difficulty**: Intermediate

**Strategy**:
Attribute selectors let you target elements based on HTML attributes and their values, which is invaluable for styling form controls, links, and data-attribute-driven UIs without extra classes. The five matcher variations (`[attr]`, `[attr=val]`, `[attr*=val]`, `[attr^=val]`, `[attr$=val]`) cover existence, exact match, contains, starts-with, and ends-with patterns. Remember to quote values containing special characters, and prefer attribute selectors over inline styles for dynamic state changes.


**Code Snippet:**
```css
a[href^="https"] { color: green; }
input[type="text"] { width: 100%; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q52"></a>
### Q52: How do you style placeholder text?

**Difficulty**: Intermediate

**Strategy**:
Styling placeholder text ensures form inputs match your design system, improving visual consistency across browsers. The `::placeholder` pseudo-element is the standard approach, though older browsers may still need vendor prefixes like `::-webkit-input-placeholder`. A common pitfall is using very light placeholder colors that fail WCAG contrast requirements -- always ensure at least a 3:1 ratio against the background.

```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q53"></a>
### Q53: How do you style selection color (`::selection`)?

**Difficulty**: Intermediate

**Strategy**:
`::selection` lets you customize the highlight appearance when users select text, reinforcing brand identity in a subtle but noticeable way. Only a limited set of properties work -- `color`, `background`, `text-shadow`, and `outline` -- so keep expectations realistic. A best practice is to ensure the selection colors maintain sufficient contrast for readability, as inverted colors can sometimes confuse users.


**Code Snippet:**
```css
::selection {
  background: gold;
  color: black;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q54"></a>
### Q54: How do you use CSS Variables for spacing and typography scales?

**Difficulty**: Intermediate

**Strategy**:
CSS Variables (custom properties) enable design tokens that centralize spacing, typography, and color decisions in `:root`, making theme switching and maintenance straightforward. They cascade and can be overridden at any selector level, unlike preprocessor variables which are compiled once. A best practice is to establish a naming convention like `--space-{size}` or `--font-{scale}` to keep your token system predictable and scalable.


**Code Snippet:**
```css
:root {
  --space-md: 1rem;
  --font-lg: 1.5rem;
}
.card { padding: var(--space-md); font-size: var(--font-lg); }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q55"></a>
### Q55: How do you use `calc()` function?

**Difficulty**: Intermediate

**Strategy**:
`calc()` lets you combine different CSS units in a single expression, bridging the gap between fixed and relative values. It is essential for layouts where an element must account for a fixed sidebar, header height, or padding while filling remaining space. A common mistake is forgetting spaces around the `+` and `-` operators, which causes the entire expression to fail silently.

.content { width: calc(100% - 300px); }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q56"></a>
### Q56: How do you use `clamp()` for responsive typography?

**Difficulty**: Intermediate

**Strategy**:
`clamp()` is the modern solution for fluid typography and spacing, accepting a minimum, preferred, and maximum value in a single declaration. It eliminates the need for multiple media query breakpoints for font sizes, creating smooth scaling between viewport sizes. A common pattern is `clamp(1rem, 2.5vw, 2rem)` -- just ensure the minimum is readable on mobile and the maximum does not overwhelm desktop layouts.


**Code Snippet:**
```css
h1 {
  font-size: clamp(2rem, 5vw, 4rem);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q57"></a>
### Q57: How do you use viewport units (`vw`, `vh`, `dvh`, `lvh`)?

**Difficulty**: Intermediate

**Strategy**:
Viewport units are critical for full-screen layouts and responsive sizing, but mobile browsers have historically made `100vh` unreliable due to dynamic address bars. `dvh` (dynamic viewport height) is the modern fix that adjusts as browser chrome expands or collapses, while `svh` and `lvh` give you the smallest and largest possible viewport heights. A best practice is to pair `dvh` with a `vh` fallback for browsers that do not yet support it.


**Code Snippet:**
```css
.hero {
  height: 100dvh;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q58"></a>
### Q58: How do you handle notch areas on mobile (`safe-area-inset`)?

**Difficulty**: Intermediate

**Strategy**:
Safe area insets handle the notched and rounded-corner devices (like iPhones) where content can be obscured by hardware features. The `env(safe-area-inset-*)` functions provide pixel values for each edge that should be avoided, and they require the `viewport-fit=cover` meta tag to activate. A common mistake is applying safe area padding globally instead of only on fixed or sticky elements that could overlap the notch.


**Code Snippet:**
```css
body {
  padding-top: env(safe-area-inset-top);
  padding-bottom: env(safe-area-inset-bottom);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q59"></a>
### Q59: How do you support high contrast mode?

**Difficulty**: Intermediate

**Strategy**:
High contrast mode is an accessibility requirement for users with low vision, and supporting it demonstrates mature CSS practices. The `prefers-contrast: more` media query lets you add explicit borders, increase text weight, or adjust colors when the OS high contrast setting is active. A common pitfall is relying solely on subtle color differences to convey meaning -- always pair color with text, icons, or patterns.


**Code Snippet:**
```css
@media (prefers-contrast: more) {
  .btn { border: 2px solid black; }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q60"></a>
### Q60: How do you use `@media (prefers-reduced-motion)`?

**Difficulty**: Intermediate

**Strategy**:
`prefers-reduced-motion` is an accessibility media query that respects the user's OS-level motion preference, and omitting it is an WCAG compliance failure. Rather than removing all animation, the best practice is to reduce duration to near-zero while preserving the final state so functionality is not lost. Always test by enabling "Reduce Motion" in your operating system accessibility settings to verify the experience.


**Code Snippet:**
```css
@media (prefers-reduced-motion: reduce) {
  * { animation-duration: 0.01s !important; transition-duration: 0.01s !important; }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q61"></a>
### Q61: How do you use `@supports` to check for feature support?

**Difficulty**: Intermediate

**Strategy**:
`@supports` (feature queries) lets you apply CSS conditionally based on browser support, serving as CSS's native progressive enhancement tool. Use it to provide modern layouts like Grid or Flexbox only where supported, with safe fallbacks for older browsers. A common mistake is wrapping too many properties in feature queries -- apply them only where the fallback layout would actually break.


**Code Snippet:**
```css
@supports (display: grid) {
  .layout { display: grid; }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q62"></a>
### Q62: How do you use `@font-face` to load custom fonts?

**Difficulty**: Intermediate

**Strategy**:
`@font-face` is how you load self-hosted custom fonts, giving you full control over typography without relying on external services. Always provide `woff2` format as it offers the best compression, and include `font-weight` and `font-style` declarations so the browser matches the correct face. A common pitfall is loading too many font variations, which significantly increases page load time.


**Code Snippet:**
```css
@font-face {
  font-family: 'MyFont';
  src: url('font.woff2') format('woff2');
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q63"></a>
### Q63: How do you use `font-display: swap` for performance?

**Difficulty**: Intermediate

**Strategy**:
`font-display: swap` solves the Flash of Invisible Text (FOIT) problem by showing a fallback font immediately and swapping in the custom font once it loads. This dramatically improves perceived performance and is recommended by Lighthouse audits. A best practice is to pair it with well-matched fallback fonts using `font-family` stacks so the swap is barely noticeable.


**Code Snippet:**
```css
@font-face {
  font-family: 'MyFont';
  src: url('font.woff2');
  font-display: swap;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q64"></a>
### Q64: How do you prevent text selection (`user-select`)?

**Difficulty**: Intermediate

**Strategy**:
`user-select` controls whether users can highlight and copy text, which is essential for polished UI controls like buttons, icons, and interactive elements where accidental selection looks unprofessional. Apply `user-select: none` sparingly -- overusing it harms accessibility and prevents users from copying legitimate content. Always pair it with a `cursor: pointer` to signal interactivity.


**Code Snippet:**
```css
.btn {
  user-select: none;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q65"></a>
### Q65: How do you enable hardware acceleration for animations?

**Difficulty**: Intermediate

**Strategy**:
Hardware acceleration offloads animation rendering to the GPU, eliminating jank by promoting elements to their own compositor layer. `will-change` hints to the browser which properties will animate so it can prepare in advance, while `transform: translateZ(0)` forces layer promotion in older browsers. A critical best practice is to remove `will-change` after animations complete, as each promoted layer consumes GPU memory.


**Code Snippet:**
```css
.animated {
  will-change: transform;
  transform: translateZ(0);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q66"></a>
### Q66: How do you style a `details` and `summary` element?

**Difficulty**: Intermediate

**Strategy**:
`<details>` and `<summary>` provide native accordion behavior without JavaScript, making them valuable for accessible, progressively enhanced UIs. Styling focuses on the `summary` element (remove default markers, add custom icons) and the `[open]` attribute selector for expanded state styles. A common pitfall is forgetting that the disclosure triangle is hard to style cross-browser -- use `list-style: none` and create a custom marker with `::marker` or pseudo-elements.


**Code Snippet:**
```css
details > summary {
  cursor: pointer;
  list-style: none;
}
details[open] { background: #f9f9f9; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q67"></a>
### Q67: How do you style a `range` input slider?

**Difficulty**: Intermediate

**Strategy**:
Range input styling requires resetting browser defaults with `appearance: none` before applying custom styles, making it a practical test of cross-browser CSS skills. You must target both WebKit (`::-webkit-slider-thumb`, `::-webkit-slider-runnable-track`) and Firefox (`::-moz-range-thumb`, `::-moz-range-track`) pseudo-elements for consistent results. A common mistake is forgetting to also reset `appearance: none` on the thumb itself, which causes it to render with default OS styling.


**Code Snippet:**
```css
input[type=range] { appearance: none; width: 100%; }
input[type=range]::-webkit-slider-thumb { appearance: none; height: 20px; width: 20px; background: blue; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q68"></a>
### Q68: How do you style a file input?

**Difficulty**: Intermediate

**Strategy**:
File inputs are notoriously difficult to style directly, so the standard technique hides the native input and uses a `<label>` with a matching `for` attribute as the visual trigger. The label can be fully styled as a button, drag zone, or any custom design. Ensure the label includes clear visual feedback and accessible text, since hiding the input removes the browser's default file selection affordance.


**Code Snippet:**
```css
input[type=file] { display: none; }
.file-label { padding: 10px; background: #eee; cursor: pointer; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q69"></a>
### Q69: How do you create a custom toggle switch?

**Difficulty**: Intermediate

**Strategy**:
Custom toggle switches are a common interview exercise that combines hidden checkbox inputs, adjacent sibling selectors, and pseudo-elements. The pattern uses a hidden checkbox, a styled label as the track, and `::after` as the sliding thumb, with `:checked` state driving the position and color change. Always include `:focus-visible` styles on the hidden input to maintain keyboard accessibility.


**Code Snippet:**
```css
.toggle-input { display: none; }
.toggle-label { width: 40px; height: 20px; background: #ccc; position: relative; }
.toggle-input:checked + .toggle-label { background: green; }
.toggle-input:checked + .toggle-label::after { transform: translateX(20px); }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q70"></a>
### Q70: How do you create a pure CSS dropdown menu?

**Difficulty**: Intermediate

**Strategy**:
Pure CSS dropdowns leverage the `:hover` pseudo-class on a parent container to reveal nested submenu lists without any JavaScript. Position the submenu absolutely within a relatively positioned parent, and toggle visibility with `display` or `opacity` transitions. A common pitfall is having gaps between the parent and submenu that cause the hover state to collapse -- use padding on the parent or overlap zones to prevent this.

```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q71"></a>
### Q71: How do you create a pure CSS modal (using `:target` or checkbox hack)?

**Difficulty**: Intermediate

**Strategy**:
Pure CSS modals demonstrate creative use of the `:target` pseudo-class or the checkbox hack to manage open/close state without JavaScript. The `:target` approach activates when the URL hash matches the modal's ID, while the checkbox hack uses a hidden input and label toggle. Both approaches have accessibility limitations -- real production modals should include focus trapping and ARIA attributes via JavaScript.


**Code Snippet:**
```css
.modal { display: none; position: fixed; }
.modal:target { display: flex; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q72"></a>
### Q72: How do you create a pure CSS accordion?

**Difficulty**: Intermediate

**Strategy**:
Pure CSS accordions use hidden radio inputs (single-open behavior) or checkboxes (multi-open behavior) combined with labels to toggle content visibility through adjacent sibling selectors. The content panel typically transitions `max-height` from `0` to a set value for a smooth expand effect. Be aware that `max-height` transitions require guessing a maximum value, which can cause delayed animations if the value is much larger than actual content.


**Code Snippet:**
```css
input[type=radio] { display: none; }
input:checked + .content { max-height: 200px; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q73"></a>
### Q73: How do you create a pure CSS tab system?

**Difficulty**: Intermediate

**Strategy**:
Pure CSS tab systems use hidden radio inputs paired with labels to control which tab panel is visible, leveraging the general sibling combinator (`~`) to target content panels. Radio inputs enforce single-selection (one tab at a time), while checkboxes allow multi-tab behavior. This pattern is useful for interviews but in production, JavaScript-based tabs provide better keyboard navigation and ARIA support.


**Code Snippet:**
```css
.tab-content { display: none; }
#tab1:checked ~ .content1 { display: block; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q74"></a>
### Q74: How do you use `counters` for automatic numbering?

**Difficulty**: Intermediate

**Strategy**:
CSS counters provide automatic numbering for lists, sections, or any repeated elements without manually numbering in HTML. The three-step process is `counter-reset` on the parent, `counter-increment` on each child, and `content: counter()` in a pseudo-element to display. A common pitfall is forgetting to reset the counter on the parent, causing numbering to continue from previous instances on the page.


**Code Snippet:**
```css
ol { counter-reset: item; }
li::before { counter-increment: item; content: counter(item) '. '; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q75"></a>
### Q75: How do you use `content` property in pseudo-elements?

**Difficulty**: Intermediate

**Strategy**:
The `content` property in `::before` and `::after` pseudo-elements injects generated text, images, counters, or attribute values without modifying the HTML. It is commonly used for decorative quotes, icons, link URLs in print stylesheets, and dynamic labels via `attr()`. Remember that `content` generated text is not selectable or accessible to screen readers, so never put meaningful content exclusively in pseudo-elements.


**Code Snippet:**
```css
a::after { content: ' (' attr(href) ')'; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q76"></a>
### Q76: How do you handle text overflow in a table cell?

**Difficulty**: Intermediate

**Strategy**:
Text overflow in table cells requires `table-layout: fixed` combined with `white-space: nowrap`, `overflow: hidden`, and `text-overflow: ellipsis` on the cell. Without `table-layout: fixed`, the browser auto-sizes columns based on content, which prevents ellipsis from triggering. A best practice is to add a `title` attribute to the cell so users can see the full text on hover when it is truncated.


**Code Snippet:**
```css
td {
  max-width: 100px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q77"></a>
### Q77: How do you make a table responsive (scrollable or stacked)?

**Difficulty**: Intermediate

**Strategy**:
Responsive tables have two main approaches: horizontal scrolling for data integrity, and stacked layout for mobile readability. Wrapping the table in an `overflow-x: auto` container preserves the table structure, while the stacked approach uses a media query to switch rows and cells to `display: block` with `data-*` attribute labels. Choose scrolling for numerical data that needs column alignment, and stacking for content-heavy tables like pricing comparisons.


**Code Snippet:**
```css
.table-wrapper { overflow-x: auto; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q78"></a>
### Q78: How do you style alternate table rows?

**Difficulty**: Intermediate

**Strategy**:
Zebra-striping table rows improves readability by providing visual separation between data rows, and `nth-child(even)` or `nth-child(odd)` is the simplest way to achieve it. This pattern also applies to grids, lists, and card layouts where alternating backgrounds aid scanning. Be careful with row-spanning cells or dynamically added rows, which can break the alternating pattern unexpectedly.

```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q79"></a>
### Q79: How do you stick a table header?

**Difficulty**: Intermediate

**Strategy**:
Sticky table headers keep column labels visible while scrolling through long datasets, significantly improving data table usability. Apply `position: sticky` and `top: 0` to `th` elements with a solid background color to prevent content from showing through. A common pitfall is having an ancestor with `overflow: hidden` or `overflow: auto`, which breaks `position: sticky` entirely.


**Code Snippet:**
```css
th { position: sticky; top: 0; background: white; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q80"></a>
### Q80: How do you implement print styles (`@media print`)?

**Difficulty**: Intermediate

**Strategy**:
Print stylesheets ensure your web content renders cleanly on paper, which matters for invoices, reports, and articles that users commonly print. Use `@media print` to remove backgrounds, switch to serif fonts, expand full-width layouts, and hide interactive-only elements like navigation. A best practice is to always include `@page` margin rules and test with your browser's print preview before shipping.


**Code Snippet:**
```css
@media print {
  body { color: black; background: white; }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q81"></a>
### Q81: How do you hide elements in print view?

**Difficulty**: Intermediate

**Strategy**:
Hiding elements in print view keeps the printed output focused on content by removing navigation, ads, footers, and interactive widgets. Use `display: none` inside `@media print` for a class-based approach (e.g., `.no-print`), or target specific elements like `nav`, `footer`, and `aside`. Avoid using `visibility: hidden` for this purpose as it preserves whitespace, whereas `display: none` collapses the space entirely.

```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q82"></a>
### Q82: How do you force page breaks in print?

**Difficulty**: Intermediate

**Strategy**:
Page break properties control where printed content splits across pages, preventing awkward breaks in the middle of tables, images, or code blocks. The modern `break-before` and `break-after` properties replace the older `page-break-before` and `page-break-after` aliases, though both work. A common pitfall is using `break-inside: avoid` on very tall elements -- if they exceed a full page, the browser will break them anyway regardless of the property.


**Code Snippet:**
```css
.chapter { break-before: page; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q83"></a>
### Q83: How do you use `shape-outside` for text wrapping around images?

**Difficulty**: Intermediate

**Strategy**:
`shape-outside` wraps inline content around a custom shape instead of the default rectangular bounding box, creating magazine-quality text layouts. It only works on floated elements, and the shape functions (`circle()`, `ellipse()`, `polygon()`, `url()`) define the wrapping boundary. A common mistake is forgetting that the shape affects text wrapping, not the element's visual rendering -- pair it with `clip-path` if you want both the shape and the visual to match.


**Code Snippet:**
```css
.circle {
  float: left;
  shape-outside: circle(50%);
  width: 100px; height: 100px;
  border-radius: 50%;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q84"></a>
### Q84: How do you use `writing-mode` for vertical text?

**Difficulty**: Intermediate

**Strategy**:
`writing-mode` controls the direction in which text flows, enabling vertical text layouts common in East Asian typography and modern creative designs. The `vertical-rl` and `vertical-lr` values switch text from horizontal to vertical while maintaining readability. Be aware that `writing-mode` also affects block flow direction, which changes how Flexbox and Grid layouts behave -- test thoroughly when combining them.


**Code Snippet:**
```css
.vertical { writing-mode: vertical-rl; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q85"></a>
### Q85: How do you use `direction: rtl` for right-to-left languages?

**Difficulty**: Intermediate

**Strategy**:
`direction: rtl` is fundamental for internationalization, setting the base text direction for right-to-left languages like Arabic and Hebrew. It reverses not only text flow but also the default alignment and layout direction of block-level elements. A best practice is to use logical properties (`margin-inline-start` instead of `margin-left`) throughout your CSS so layouts adapt automatically when direction changes.


**Code Snippet:**
```css
html { direction: rtl; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q86"></a>
### Q86: How do you use `text-align-last` for justified text?

**Difficulty**: Intermediate

**Strategy**:
`text-align-last` controls the alignment of the final line in a justified text block, solving the common issue of awkwardly spaced last lines. Without it, the last line of `text-align: justify` content defaults to the start direction, which can look inconsistent in centered designs. Use `text-align-last: center` or `start` to give the final line a polished appearance that matches your layout intent.


**Code Snippet:**
```css
p {
  text-align: justify;
  text-align-last: center;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q87"></a>
### Q87: How do you use `text-decoration` styling (color, style, thickness)?

**Difficulty**: Intermediate

**Strategy**:
The `text-decoration` shorthand and its longhand properties (`text-decoration-line`, `text-decoration-color`, `text-decoration-style`, `text-decoration-thickness`) provide fine-grained control over underlines and strikethroughs. This is especially useful for link styling where the default underline color does not match the text color. A best practice is to set `text-underline-offset` alongside thickness to prevent underlines from clipping descenders on letters like "g" and "y".


**Code Snippet:**
```css
a { text-decoration: underline wavy red 2px; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q88"></a>
### Q88: How do you use `text-transform`?

**Difficulty**: Intermediate

**Strategy**:
`text-transform` controls text capitalization purely through CSS, ensuring consistent casing without modifying source content. This is essential for headings, buttons, and labels where uppercase styling is a design requirement but the source text should remain in normal case for accessibility and SEO. Avoid using `text-transform` to compensate for inconsistent data -- fix the data source instead.


**Code Snippet:**
```css
.heading { text-transform: uppercase; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q89"></a>
### Q89: How do you use `letter-spacing` and `word-spacing`?

**Difficulty**: Beginner

**Strategy**:
`letter-spacing` and `word-spacing` fine-tune typographic rhythm, with letter-spacing (tracking) commonly used on headings and uppercase labels for visual polish. Always use relative units like `em` rather than `px` so spacing scales proportionally with font size. A common mistake is over-spacing body text, which hurts readability -- reserve generous letter-spacing for display text and short labels only.


**Code Snippet:**
```css
h1 {
  letter-spacing: 0.05em; /* Spreads characters slightly */
}
p {
  word-spacing: 0.1em; /* Spreads words slightly */
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q90"></a>
### Q90: How do you use `white-space` property?

**Difficulty**: Intermediate

**Strategy**:
`white-space` is a deceptively powerful property that controls how whitespace, line breaks, and text wrapping behave -- it is essential for text truncation, code blocks, and preserving user-entered formatting. The most interview-relevant values are `nowrap` (single-line truncation with ellipsis), `pre-wrap` (preserves spaces and newlines but wraps), and `pre` (preserves everything, no wrapping). A common mistake is using `nowrap` without `overflow: hidden` and `text-overflow: ellipsis`, which causes horizontal overflow.


**Code Snippet:**
```css
/* Prevent text from wrapping */
.truncate {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

/* Preserve formatting (e.g., code blocks) */
.code-block {
  white-space: pre-wrap;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q91"></a>
### Q91: How do you use `word-break` and `overflow-wrap`?

**Difficulty**: Intermediate

**Strategy**:
`word-break` and `overflow-wrap` solve the problem of long unbreakable strings (URLs, emails, hashes) breaking layout containers. `overflow-wrap: break-word` is the safest default -- it only breaks words that would otherwise overflow their container. `word-break: break-all` is more aggressive, breaking at any character, and is better suited for CJK (Chinese/Japanese/Korean) text content. A best practice is to set `overflow-wrap: break-word` as a global body rule to prevent layout explosions.


**Code Snippet:**
```css
.container {
  width: 200px;
  /* Prevents horizontal scrollbar for long words */
  overflow-wrap: break-word; 
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q92"></a>
### Q92: How do you use `hyphens` for auto-hyphenation?

**Difficulty**: Intermediate

**Strategy**:
`hyphens: auto` enables automatic word hyphenation at line breaks, improving the appearance of justified text and narrow columns. It requires the `lang` attribute on the HTML element so the browser can use the correct hyphenation dictionary for the language. A common pitfall is enabling auto-hyphens on short-line layouts where excessive hyphenation looks worse than ragged right text -- test with real content before committing.


**Code Snippet:**
```css
p {
  hyphens: auto;
  text-align: justify; /* Often used together */
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q93"></a>
### Q93: How do you use `caret-color`?

**Difficulty**: Beginner

**Strategy**:
`caret-color` customizes the text insertion cursor (caret) in editable elements, providing a simple branding touch that improves visual consistency in custom-styled forms. It accepts any CSS color value including `transparent` to hide the caret entirely. A best practice is to ensure the caret color contrasts well with both the input background and text color for visibility.


**Code Snippet:**
```css
input {
  caret-color: red;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q94"></a>
### Q94: How do you use `pointer-events`?

**Difficulty**: Intermediate

**Strategy**:
`pointer-events` controls whether an element is a target for mouse, touch, and pointer events, with `none` making it click-through to elements below. This is invaluable for decorative overlays, label overlays on images, and preventing interaction during loading states. Remember that `pointer-events: none` does not prevent keyboard focus or tab navigation -- pair it with `tabindex="-1"` and `aria-hidden="true"` for full non-interactive behavior.


**Code Snippet:**
```css
/* Click-through overlay */
.overlay {
  position: fixed;
  inset: 0;
  pointer-events: none;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q95"></a>
### Q95: How do you use `cursor` property?

**Difficulty**: Beginner

**Strategy**:
The `cursor` property communicates interactivity to users by changing the mouse pointer appearance, reinforcing what actions are possible. Common values include `pointer` for clickable elements, `not-allowed` for disabled states, and `grab`/`grabbing` for drag-and-drop interfaces. A best practice is to always match cursor styling with the actual element behavior -- never use `cursor: pointer` on non-interactive elements, as it confuses users and hurts accessibility.


**Code Snippet:**
```css
button:disabled {
  cursor: not-allowed;
  opacity: 0.5;
}
.draggable {
  cursor: grab;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q96"></a>
### Q96: How do you use `outline` vs `border`?

**Difficulty**: Intermediate

**Strategy**:
Understanding the difference between `outline` and `border` is critical for accessibility and layout debugging. Borders participate in the box model and affect layout dimensions, while outlines are drawn outside the box model and do not affect layout at all. This makes outlines perfect for `:focus-visible` rings, which need to appear without shifting content -- use `outline-offset` to add spacing between the element edge and the outline.


**Code Snippet:**
```css
button:focus-visible {
  outline: 2px solid blue;
  outline-offset: 2px; /* Space between button and outline */
  border-radius: 4px;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q97"></a>
### Q97: How do you use `box-shadow` for elevation?

**Difficulty**: Beginner

**Strategy**:
`box-shadow` creates visual depth and elevation, and stacking multiple shadows with different blur radii produces realistic Material Design-style elevation. The key to natural-looking shadows is combining a tight direct shadow (low blur) with a softer ambient shadow (high blur, lower opacity). Avoid using very large spread values, which create harsh edges that look unnatural -- rely on blur radius for soft transitions instead.


**Code Snippet:**
```css
.card {
  /* x-offset, y-offset, blur-radius, spread-radius, color */
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1), 
              0 2px 4px rgba(0, 0, 0, 0.06);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q98"></a>
### Q98: How do you use `border-radius` for different shapes?

**Difficulty**: Beginner

**Strategy**:
`border-radius` creates rounded corners and shapes, with percentage-based values referencing the element's dimensions. `50%` creates a perfect circle when width equals height, and `9999px` creates pill-shaped elements regardless of dimensions. The four-value syntax (`top-left top-right bottom-right bottom-left`) and the eight-value slash syntax for elliptical corners give you full control over each corner independently.


**Code Snippet:**
```css
.circle {
  width: 50px; height: 50px;
  border-radius: 50%;
}
.pill {
  border-radius: 9999px; /* Fully rounded ends */
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q99"></a>
### Q99: How do you use `display: contents`?

**Difficulty**: Advanced

**Strategy**:
`display: contents` makes an element invisible to the box tree while preserving its children, effectively removing the wrapper from layout without removing the content. This is especially powerful when a semantic wrapper element would otherwise break Grid or Flex layout patterns. Be cautious with accessibility -- some browsers historically removed the element from the accessibility tree, though modern implementations preserve ARIA semantics.


**Code Snippet:**
```css
.wrapper {
  display: contents;
}
/* .wrapper's children now act as direct children of .wrapper's parent */
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q100"></a>
### Q100: How do you use `gap` in Flexbox?

**Difficulty**: Beginner

**Strategy**:
The `gap` property in Flexbox (originally a Grid-only feature) provides clean, consistent spacing between items without the margin hacks that plagued Flexbox layouts. Unlike margins, `gap` only applies between items -- never before the first or after the last -- eliminating the need for `:first-child`/`:last-child` margin removal. Use `row-gap` and `column-gap` separately for asymmetric spacing in wrapped Flexbox layouts.


**Code Snippet:**
```css
.flex-container {
  display: flex;
  gap: 1rem; /* Space between items */
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q101"></a>
### Q101: How do you use Logical Properties (`margin-block`, `padding-inline`)?

**Difficulty**: Intermediate

**Strategy**:
Logical properties replace physical directions (`top`, `right`, `bottom`, `left`) with flow-relative equivalents (`block-start`, `inline-end`, etc.) that automatically adapt to different writing modes and text directions. This is essential for internationalized applications that support both LTR and RTL languages without maintaining separate stylesheets. A best practice is to adopt logical properties as your default -- they future-proof your CSS and make switching to RTL as simple as changing `direction: rtl`.


**Code Snippet:**
```css
.box {
  padding-inline: 20px; /* Left & Right in LTR */
  margin-block-start: 10px; /* Top in LTR */
  border-inline-start: 5px solid red; /* Left border in LTR */
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q102"></a>
### Q102: How do you use `inset` property?

**Difficulty**: Intermediate

**Strategy**:
The `inset` property is a shorthand for `top`, `right`, `bottom`, and `left`, simplifying absolute and fixed positioning declarations. `inset: 0` is the cleanest way to stretch an element to fill its positioned parent, replacing four separate declarations. It follows the same clockwise shorthand rules as `margin` and `padding`, and pairs perfectly with `position: fixed` for full-viewport overlays and modals.


**Code Snippet:**
```css
/* Full screen modal overlay */
.modal-backdrop {
  position: fixed;
  inset: 0; /* top:0, right:0, bottom:0, left:0 */
  background: rgba(0,0,0,0.5);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q103"></a>
### Q103: How do you use `place-items` (Centering Trick)?

**Difficulty**: Intermediate

**Strategy**:
`place-items: center` is the most concise way to center content in CSS Grid, combining `align-items` and `justify-items` into a single declaration. It centers along both the block and inline axes simultaneously, replacing the older `display: flex; justify-content: center; align-items: center` pattern with just three lines. Remember that `place-items` works on Grid containers, while `place-content` centers the grid tracks themselves within the container.


**Code Snippet:**
```css
.center-box {
  display: grid;
  place-items: center;
  height: 100vh;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>
