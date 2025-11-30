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

### Q1: How do you implement a responsive 12-column grid using CSS Grid?

**Difficulty**: Intermediate

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

### Q2: How do you center an element absolutely both vertically and horizontally?

**Difficulty**: Intermediate

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

### Q3: How do you implement a sticky footer that stays at the bottom even with little content?

**Difficulty**: Intermediate

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

### Q4: How do you implement a pure CSS tooltip?

**Difficulty**: Intermediate

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

### Q5: How do you create a custom checkbox using CSS?

**Difficulty**: Intermediate

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

### Q6: How do you implement Dark Mode using CSS Variables?

**Difficulty**: Intermediate

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

### Q7: How do you create a responsive aspect ratio box (e.g., 16:9 video embed)?

**Difficulty**: Intermediate

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

### Q8: How do you truncate text with an ellipsis (...) for a single line and multiple lines?

**Difficulty**: Intermediate

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

### Q9: How do you use Container Queries to build component-based responsive styles?

**Difficulty**: Intermediate

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

### Q10: How do you optimize CSS performance (Painting and Layout)?

**Difficulty**: Intermediate

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

### Q11: How do you implement a parallax scrolling effect purely in CSS?

**Difficulty**: Intermediate

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

### Q12: How do you ensure an element is visually hidden but accessible to screen readers?

**Difficulty**: Intermediate

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

### Q13: How do you implement a CSS Triangle?

**Difficulty**: Intermediate

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

### Q14: How do you prevent content layout shift (CLS) for images?

**Difficulty**: Intermediate

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

### Q15: How do you implement a masonry layout using CSS only?

**Difficulty**: Intermediate

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

### Q16: How do you use Flexbox for a navigation bar?

**Difficulty**: Intermediate

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

### Q17: How do you use `flex-grow`, `flex-shrink`, and `flex-basis`?

**Difficulty**: Intermediate

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

### Q18: How do you implement a sidebar layout with Flexbox?

**Difficulty**: Intermediate

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

### Q19: How do you align items in a grid using `justify-items` and `align-items`?

**Difficulty**: Intermediate

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

### Q20: How do you use `minmax()` in CSS Grid?

**Difficulty**: Intermediate

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

### Q21: How do you create overlapping elements with CSS Grid?

**Difficulty**: Intermediate

**Strategy:**
Place items in the same grid cell(s) using line numbers. Later items stack on top (control with z-index if needed).

**Code Snippet:**
```css
.item1 { grid-column: 1 / 3; grid-row: 1; }
.item2 { grid-column: 2 / 4; grid-row: 1; opacity: 0.8; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q22: How do you use `z-index` and stacking contexts effectively?

**Difficulty**: Intermediate

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

### Q23: How do you debug `z-index` issues?

**Difficulty**: Intermediate

**Strategy:**
Check if the element has `position` set (if not flex/grid child). Check parent stacking contexts (e.g., parent has `overflow: hidden` or `opacity`). Use browser devtools 'Layers' view.

**Code Snippet:**
```css
/* Debug helper */
* { outline: 1px solid red; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q24: How do you style a scrollbar using `::-webkit-scrollbar`?

**Difficulty**: Intermediate

**Strategy:**
Use pseudo-elements: `::-webkit-scrollbar` (width), `::-webkit-scrollbar-track` (background), `::-webkit-scrollbar-thumb` (handle).

**Code Snippet:**
```css
::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-thumb { background: #888; border-radius: 4px; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q25: How do you use `scroll-behavior: smooth`?

**Difficulty**: Intermediate

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

### Q26: How do you use `scroll-snap-type` for snapping sections?

**Difficulty**: Intermediate

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

### Q27: How do you implement a CSS reset or normalize?

**Difficulty**: Intermediate

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

### Q28: How do you use `box-sizing: border-box` globally?

**Difficulty**: Intermediate

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

### Q29: How do you style inputs to look consistent across browsers?

**Difficulty**: Intermediate

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

### Q30: How do you remove the default outline on focus (and what to replace it with)?

**Difficulty**: Intermediate

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

### Q31: How do you style a broken image using `img::before`?

**Difficulty**: Intermediate

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

### Q32: How do you style list markers using `::marker`?

**Difficulty**: Intermediate

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

### Q33: How do you use `object-fit` and `object-position` for images?

**Difficulty**: Intermediate

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

### Q34: How do you use `background-size: cover` vs `contain`?

**Difficulty**: Intermediate

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

### Q35: How do you create a gradient background?

**Difficulty**: Intermediate

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

### Q36: How do you create a text gradient?

**Difficulty**: Intermediate

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

### Q37: How do you use `clip-path` to create shapes?

**Difficulty**: Intermediate

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

### Q38: How do you use `mask-image` for transparency masks?

**Difficulty**: Intermediate

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

### Q39: How do you use `backdrop-filter` for glassmorphism?

**Difficulty**: Intermediate

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

### Q40: How do you use `filter` for image effects (blur, grayscale)?

**Difficulty**: Intermediate

**Strategy:**
Applies graphical effects to the element itself.

**Code Snippet:**
```css
img:hover {
  filter: grayscale(100%) blur(2px);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q41: How do you use `mix-blend-mode` for blending effects?

**Difficulty**: Intermediate

**Strategy:**
Blends element with its parent/background (like Photoshop layers).

**Code Snippet:**
```css
.text {
  mix-blend-mode: difference;
  color: white;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q42: How do you implement a loading spinner with CSS animations?

**Difficulty**: Intermediate

**Strategy:**
Rotate a border with one transparent side.

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

### Q43: How do you create a shake animation?

**Difficulty**: Intermediate

**Strategy:**
Translate X back and forth rapidly.

**Code Snippet:**
```css
@keyframes shake {
  0%, 100% { transform: translateX(0); }
  25% { transform: translateX(-5px); }
  75% { transform: translateX(5px); }
}
.error { animation: shake 0.3s; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q44: How do you pause an animation on hover?

**Difficulty**: Intermediate

**Strategy:**
Use `animation-play-state`.

**Code Snippet:**
```css
.box:hover {
  animation-play-state: paused;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q45: How do you use CSS transitions for hover effects?

**Difficulty**: Intermediate

**Strategy:**
Define `transition` on the base state, not the hover state.

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

### Q46: How do you use the `:not()` pseudo-class?

**Difficulty**: Intermediate

**Strategy:**
Selects elements that do NOT match the selector.

**Code Snippet:**
```css
li:not(:last-child) {
  border-bottom: 1px solid #ccc;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q47: How do you use the `:has()` pseudo-class (parent selector)?

**Difficulty**: Intermediate

**Strategy:**
Selects a parent if it contains a specific child. 'Parent selector'.

**Code Snippet:**
```css
/* Style card if it contains an image */
.card:has(img) {
  padding: 0;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q48: How do you use the `:is()` and `:where()` pseudo-classes?

**Difficulty**: Intermediate

**Strategy:**
`is()` and `:where()` group selectors. `:is()` takes specificity of most specific arg. `:where()` has 0 specificity.

**Code Snippet:**
```css
:is(h1, h2, h3) { margin-top: 0; }
:where(article) p { color: #666; /* easy to override */ }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q49: How do you use `:nth-child()` and `:nth-of-type()`?

**Difficulty**: Intermediate

**Strategy:**
`:nth-child` counts ALL children. `:nth-of-type` counts only children of that tag type.

**Code Snippet:**
```css
li:nth-child(odd) { background: #eee; }
p:nth-of-type(2) { font-weight: bold; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q50: How do you use `::first-letter` and `::first-line`?

**Difficulty**: Intermediate

**Strategy:**
Styles the first letter or first line of a block element.

**Code Snippet:**
```css
p::first-letter {
  font-size: 2em;
  float: left;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q51: How do you use attribute selectors?

**Difficulty**: Intermediate

**Strategy:**
`[attr]` (exists), `[attr=val]` (exact), `[attr*=val]` (contains), `[attr^=val]` (starts), `[attr$=val]` (ends).

**Code Snippet:**
```css
a[href^="https"] { color: green; }
input[type="text"] { width: 100%; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q52: How do you style placeholder text?

**Difficulty**: Intermediate

**Strategy:**
Use `::placeholder` pseudo-element.

**Code Snippet:**
```css
input::placeholder {
  color: #999;
  font-style: italic;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q53: How do you style selection color (`::selection`)?

**Difficulty**: Intermediate

**Strategy:**
Use `::selection` pseudo-element. Only supports color, background, text-shadow.

**Code Snippet:**
```css
::selection {
  background: gold;
  color: black;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q54: How do you use CSS Variables for spacing and typography scales?

**Difficulty**: Intermediate

**Strategy:**
Define vars in `:root` for global reuse.

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

### Q55: How do you use `calc()` function?

**Difficulty**: Intermediate

**Strategy:**
Perform math mixing units.

**Code Snippet:**
```css
.sidebar { width: 300px; }
.content { width: calc(100% - 300px); }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q56: How do you use `clamp()` for responsive typography?

**Difficulty**: Intermediate

**Strategy:**
`clamp(min, preferred, max)`. Font size scales with viewport but stays within bounds.

**Code Snippet:**
```css
h1 {
  font-size: clamp(2rem, 5vw, 4rem);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q57: How do you use viewport units (`vw`, `vh`, `dvh`, `lvh`)?

**Difficulty**: Intermediate

**Strategy:**
`100vh` is full height. `100dvh` (dynamic) accounts for mobile browser bars expanding/collapsing.

**Code Snippet:**
```css
.hero {
  height: 100dvh;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q58: How do you handle notch areas on mobile (`safe-area-inset`)?

**Difficulty**: Intermediate

**Strategy:**
Use `env(safe-area-inset-*)` in padding/margin.

**Code Snippet:**
```css
body {
  padding-top: env(safe-area-inset-top);
  padding-bottom: env(safe-area-inset-bottom);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q59: How do you support high contrast mode?

**Difficulty**: Intermediate

**Strategy:**
Use `@media (prefers-contrast: more)`. Avoid relying solely on color.

**Code Snippet:**
```css
@media (prefers-contrast: more) {
  .btn { border: 2px solid black; }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q60: How do you use `@media (prefers-reduced-motion)`?

**Difficulty**: Intermediate

**Strategy:**
Disable or reduce animations for users prone to motion sickness.

**Code Snippet:**
```css
@media (prefers-reduced-motion: reduce) {
  * { animation-duration: 0.01s !important; transition-duration: 0.01s !important; }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q61: How do you use `@supports` to check for feature support?

**Difficulty**: Intermediate

**Strategy:**
Feature queries. Apply styles only if browser supports a property.

**Code Snippet:**
```css
@supports (display: grid) {
  .layout { display: grid; }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q62: How do you use `@font-face` to load custom fonts?

**Difficulty**: Intermediate

**Strategy:**
Define font family and source files (woff2 preferred).

**Code Snippet:**
```css
@font-face {
  font-family: 'MyFont';
  src: url('font.woff2') format('woff2');
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q63: How do you use `font-display: swap` for performance?

**Difficulty**: Intermediate

**Strategy:**
Shows fallback font immediately, swaps to custom font when loaded (avoids invisible text).

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

### Q64: How do you prevent text selection (`user-select`)?

**Difficulty**: Intermediate

**Strategy:**
Use `user-select: none`. Useful for buttons/UI controls.

**Code Snippet:**
```css
.btn {
  user-select: none;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q65: How do you enable hardware acceleration for animations?

**Difficulty**: Intermediate

**Strategy:**
Use `transform: translateZ(0)` or `will-change` to promote element to a new layer.

**Code Snippet:**
```css
.animated {
  will-change: transform;
  transform: translateZ(0);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q66: How do you style a `details` and `summary` element?

**Difficulty**: Intermediate

**Strategy:**
Style `summary` for the header (cursor pointer, remove list-style). Content shows when open.

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

### Q67: How do you style a `range` input slider?

**Difficulty**: Intermediate

**Strategy:**
Use `appearance: none` and style `::-webkit-slider-thumb` and `::-webkit-slider-runnable-track`.

**Code Snippet:**
```css
input[type=range] { appearance: none; width: 100%; }
input[type=range]::-webkit-slider-thumb { appearance: none; height: 20px; width: 20px; background: blue; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q68: How do you style a file input?

**Difficulty**: Intermediate

**Strategy:**
Hide the actual input `display: none` and use a `label` styled as a button.

**Code Snippet:**
```css
input[type=file] { display: none; }
.file-label { padding: 10px; background: #eee; cursor: pointer; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q69: How do you create a custom toggle switch?

**Difficulty**: Intermediate

**Strategy:**
Hide checkbox. Style label as track, `::after` as thumb. Change position on `:checked`.

**Code Snippet:**
```css
.toggle-input { display: none; }
.toggle-label { width: 40px; height: 20px; background: #ccc; position: relative; }
.toggle-input:checked + .toggle-label { background: green; }
.toggle-input:checked + .toggle-label::after { transform: translateX(20px); }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q70: How do you create a pure CSS dropdown menu?

**Difficulty**: Intermediate

**Strategy:**
Show submenu on parent hover.

**Code Snippet:**
```css
.submenu { display: none; position: absolute; }
.has-submenu:hover .submenu { display: block; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q71: How do you create a pure CSS modal (using `:target` or checkbox hack)?

**Difficulty**: Intermediate

**Strategy:**
Use `:target` to show modal when URL matches `#modal-id`.

**Code Snippet:**
```css
.modal { display: none; position: fixed; }
.modal:target { display: flex; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q72: How do you create a pure CSS accordion?

**Difficulty**: Intermediate

**Strategy:**
Use Radio buttons (for one open at a time) or Checkboxes + Labels.

**Code Snippet:**
```css
input[type=radio] { display: none; }
input:checked + .content { max-height: 200px; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q73: How do you create a pure CSS tab system?

**Difficulty**: Intermediate

**Strategy:**
Radio buttons + Labels. Content hidden by default, shown when corresponding radio is checked.

**Code Snippet:**
```css
.tab-content { display: none; }
#tab1:checked ~ .content1 { display: block; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q74: How do you use `counters` for automatic numbering?

**Difficulty**: Intermediate

**Strategy:**
Initialize with `counter-reset`, increment with `counter-increment`, display with `content: counter(name)`.

**Code Snippet:**
```css
ol { counter-reset: item; }
li::before { counter-increment: item; content: counter(item) '. '; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q75: How do you use `content` property in pseudo-elements?

**Difficulty**: Intermediate

**Strategy:**
Inserts generated content. Can be string, url, counter, or attr().

**Code Snippet:**
```css
a::after { content: ' (' attr(href) ')'; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q76: How do you handle text overflow in a table cell?

**Difficulty**: Intermediate

**Strategy:**
`table-layout: fixed`, width on cell, and text-overflow props.

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

### Q77: How do you make a table responsive (scrollable or stacked)?

**Difficulty**: Intermediate

**Strategy:**
Scrollable: Wrap in `overflow-x: auto` div. Stacked: `@media` query, `display: block` for rows/cells.

**Code Snippet:**
```css
.table-wrapper { overflow-x: auto; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q78: How do you style alternate table rows?

**Difficulty**: Intermediate

**Strategy:**
Use `:nth-child(even)` or `odd`.

**Code Snippet:**
```css
tr:nth-child(even) { background: #f2f2f2; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q79: How do you stick a table header?

**Difficulty**: Intermediate

**Strategy:**
`position: sticky; top: 0`. Requires table to not have `overflow: hidden` parents usually.

**Code Snippet:**
```css
th { position: sticky; top: 0; background: white; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q80: How do you implement print styles (`@media print`)?

**Difficulty**: Intermediate

**Strategy:**
Define styles specifically for printing (black/white, remove backgrounds).

**Code Snippet:**
```css
@media print {
  body { color: black; background: white; }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q81: How do you hide elements in print view?

**Difficulty**: Intermediate

**Strategy:**
Hide navs, ads, footers.

**Code Snippet:**
```css
@media print {
  .no-print { display: none; }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q82: How do you force page breaks in print?

**Difficulty**: Intermediate

**Strategy:**
Use `break-before`, `break-after`, `page-break-*`.

**Code Snippet:**
```css
.chapter { break-before: page; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q83: How do you use `shape-outside` for text wrapping around images?

**Difficulty**: Intermediate

**Strategy:**
Floats element and wraps text around a defined shape.

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

### Q84: How do you use `writing-mode` for vertical text?

**Difficulty**: Intermediate

**Strategy:**
Changes text orientation (e.g., for Asian languages or design).

**Code Snippet:**
```css
.vertical { writing-mode: vertical-rl; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q85: How do you use `direction: rtl` for right-to-left languages?

**Difficulty**: Intermediate

**Strategy:**
Sets direction for Arabic/Hebrew. Usually set on `html` or `body`.

**Code Snippet:**
```css
html { direction: rtl; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q86: How do you use `text-align-last` for justified text?

**Difficulty**: Intermediate

**Strategy:**
Aligns the last line of a justified block.

**Code Snippet:**
```css
p {
  text-align: justify;
  text-align-last: center;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q87: How do you use `text-decoration` styling (color, style, thickness)?

**Difficulty**: Intermediate

**Strategy:**
Shorthand for line, style, color, thickness.

**Code Snippet:**
```css
a { text-decoration: underline wavy red 2px; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q88: How do you use `text-transform`?

**Difficulty**: Intermediate

**Strategy:**
Controls capitalization (uppercase, lowercase, capitalize).

**Code Snippet:**
```css
.heading { text-transform: uppercase; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q89: How do you use `letter-spacing` and `word-spacing`?

**Difficulty**: Beginner

**Strategy:**
Use `letter-spacing` to adjust the space between characters (tracking) and `word-spacing` for space between words. Use relative units (`em`) for better responsiveness.

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

### Q90: How do you use `white-space` property?

**Difficulty**: Intermediate

**Strategy:**
Controls how whitespace and line breaks are handled. `nowrap` prevents wrapping. `pre-wrap` preserves whitespace and wraps text. `pre` preserves both (like HTML `<pre>`).

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

### Q91: How do you use `word-break` and `overflow-wrap`?

**Difficulty**: Intermediate

**Strategy:**
Use `overflow-wrap: break-word` (standard) to break long words only if they cause overflow. Use `word-break: break-all` to break words at any character (useful for CJK or long URLs).

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

### Q92: How do you use `hyphens` for auto-hyphenation?

**Difficulty**: Intermediate

**Strategy:**
Use `hyphens: auto` to allow the browser to hyphenate words at line breaks. Requires the `lang` attribute to be set on the HTML element (e.g., `<html lang="en">`).

**Code Snippet:**
```css
p {
  hyphens: auto;
  text-align: justify; /* Often used together */
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q93: How do you use `caret-color`?

**Difficulty**: Beginner

**Strategy:**
Customizes the color of the text insertion cursor (caret) in inputs and textareas.

**Code Snippet:**
```css
input {
  caret-color: red;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q94: How do you use `pointer-events`?

**Difficulty**: Intermediate

**Strategy:**
`pointer-events: none` makes an element ignore mouse events (clicks, hovers), allowing clicks to pass through to elements behind it. `auto` restores default behavior.

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

### Q95: How do you use `cursor` property?

**Difficulty**: Beginner

**Strategy:**
Changes the mouse cursor to indicate interaction type. Common values: `pointer` (links/buttons), `not-allowed` (disabled), `grab`/`grabbing` (drag and drop).

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

### Q96: How do you use `outline` vs `border`?

**Difficulty**: Intermediate

**Strategy:**
`border` takes up layout space; `outline` does not. `outline` is often used for accessibility focus rings (`:focus-visible`). Use `outline-offset` to create space between the element and the outline.

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

### Q97: How do you use `box-shadow` for elevation?

**Difficulty**: Beginner

**Strategy:**
Use `box-shadow` to create depth. Combine multiple shadows (ambient and direct) for realistic effects.

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

### Q98: How do you use `border-radius` for different shapes?

**Difficulty**: Beginner

**Strategy:**
Use `50%` for circles (if width equals height). Use 4 values for different corners, or 8 values (slashes) for elliptical corners.

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

### Q99: How do you use `display: contents`?

**Difficulty**: Advanced

**Strategy:**
The element itself is removed from the box tree, but its children remain. Useful when you want children of a wrapper to participate in a parent's Grid or Flex layout directly.

**Code Snippet:**
```css
.wrapper {
  display: contents;
}
/* .wrapper's children now act as direct children of .wrapper's parent */
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q100: How do you use `gap` in Flexbox?

**Difficulty**: Beginner

**Strategy:**
Use `gap` (formerly `grid-gap`) to define space between flex items, replacing the need for margins on children.

**Code Snippet:**
```css
.flex-container {
  display: flex;
  gap: 1rem; /* Space between items */
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q101: How do you use Logical Properties (`margin-block`, `padding-inline`)?

**Difficulty**: Intermediate

**Strategy:**
Use logical properties instead of physical (`top`, `left`, etc.) to support internationalization (LTR/RTL modes) automatically. `block` is vertical (usually), `inline` is horizontal.

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

### Q102: How do you use `inset` property?

**Difficulty**: Intermediate

**Strategy:**
Shorthand for `top`, `right`, `bottom`, `left`. Useful for positioning absolute/fixed elements.

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

### Q103: How do you use `place-items` (Centering Trick)?

**Difficulty**: Intermediate

**Strategy:**
Shorthand for `align-items` and `justify-items`. In CSS Grid, `place-items: center` is the modern way to perfectly center content.

**Code Snippet:**
```css
.center-box {
  display: grid;
  place-items: center;
  height: 100vh;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

