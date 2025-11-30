# Tailwind CSS & Bootstrap Interview Questions

## Table of Contents

1. [How do you dynamically toggle Tailwind CSS classes in a React component without using string concatenation?](#q1-how-do-you-dynamically-toggle-tailwind-css-classes-in-a-react-component-without-using-string-concatenation) <span class="intermediate">Intermediate</span>
2. [How do you customize the Bootstrap 5 theme colors using SASS variables?](#q2-how-do-you-customize-the-bootstrap-5-theme-colors-using-sass-variables) <span class="intermediate">Intermediate</span>
3. [How do you extend Tailwind CSS configuration to add custom breakpoints?](#q3-how-do-you-extend-tailwind-css-configuration-to-add-custom-breakpoints) <span class="intermediate">Intermediate</span>
4. [How do you create a reusable component style in Tailwind using the `@apply` directive?](#q4-how-do-you-create-a-reusable-component-style-in-tailwind-using-the-apply-directive) <span class="beginner">Beginner</span>
5. [How do you implement a responsive grid layout in Bootstrap 5 without using custom CSS?](#q5-how-do-you-implement-a-responsive-grid-layout-in-bootstrap-5-without-using-custom-css) <span class="beginner">Beginner</span>
6. [How do you enable and use arbitrary values in Tailwind CSS for one-off styles?](#q6-how-do-you-enable-and-use-arbitrary-values-in-tailwind-css-for-one-off-styles) <span class="intermediate">Intermediate</span>
7. [How do you optimize Tailwind CSS for production to remove unused styles?](#q7-how-do-you-optimize-tailwind-css-for-production-to-remove-unused-styles) <span class="advanced">Advanced</span>
8. [How do you use Bootstrap 5's Utility API to generate custom utility classes?](#q8-how-do-you-use-bootstrap-5s-utility-api-to-generate-custom-utility-classes) <span class="advanced">Advanced</span>
9. [How do you implement Dark Mode support in Tailwind CSS?](#q9-how-do-you-implement-dark-mode-support-in-tailwind-css) <span class="intermediate">Intermediate</span>
10. [How do you use Bootstrap components (like Modals) in a React application without jQuery?](#q10-how-do-you-use-bootstrap-components-like-modals-in-a-react-application-without-jquery) <span class="intermediate">Intermediate</span>
11. [How do you create a custom Tailwind CSS plugin to add new variants?](#q11-how-do-you-create-a-custom-tailwind-css-plugin-to-add-new-variants) <span class="advanced">Advanced</span>
12. [How do you handle z-index values in Tailwind to avoid conflicts?](#q12-how-do-you-handle-z-index-values-in-tailwind-to-avoid-conflicts) <span class="intermediate">Intermediate</span>
13. [How do you center a div both vertically and horizontally using Bootstrap classes?](#q13-how-do-you-center-a-div-both-vertically-and-horizontally-using-bootstrap-classes) <span class="beginner">Beginner</span>
14. [How do you apply styles to children elements in Tailwind without adding classes to each child?](#q14-how-do-you-apply-styles-to-children-elements-in-tailwind-without-adding-classes-to-each-child) <span class="advanced">Advanced</span>
15. [How do you implement a sticky footer in Tailwind CSS?](#q15-how-do-you-implement-a-sticky-footer-in-tailwind-css) <span class="intermediate">Intermediate</span>
16. [How do you implement a responsive Grid Layout in Tailwind CSS?](#q16-how-do-you-implement-a-responsive-grid-layout-in-tailwind-css) <span class="beginner">Beginner</span>
17. [How do you align items using Flexbox in Bootstrap?](#q17-how-do-you-align-items-using-flexbox-in-bootstrap) <span class="beginner">Beginner</span>
18. [How do you style Markdown content using Tailwind Typography?](#q18-how-do-you-style-markdown-content-using-tailwind-typography) <span class="intermediate">Intermediate</span>
19. [How do you apply Spacing (Margin/Padding) in Bootstrap?](#q19-how-do-you-apply-spacing-marginpadding-in-bootstrap) <span class="beginner">Beginner</span>
20. [How do you create circular images with borders in Tailwind?](#q20-how-do-you-create-circular-images-with-borders-in-tailwind) <span class="beginner">Beginner</span>
21. [How do you add shadows in Bootstrap?](#q21-how-do-you-add-shadows-in-bootstrap) <span class="beginner">Beginner</span>
22. [How do you apply a blur filter in Tailwind?](#q22-how-do-you-apply-a-blur-filter-in-tailwind) <span class="intermediate">Intermediate</span>
23. [How do you make a link stretch to cover the entire parent card in Bootstrap?](#q23-how-do-you-make-a-link-stretch-to-cover-the-entire-parent-card-in-bootstrap) <span class="intermediate">Intermediate</span>
24. [How do you rotate an element in Tailwind?](#q24-how-do-you-rotate-an-element-in-tailwind) <span class="beginner">Beginner</span>
25. [How do you prevent text selection in Bootstrap?](#q25-how-do-you-prevent-text-selection-in-bootstrap) <span class="beginner">Beginner</span>
26. [How do you style an SVG icon's color in Tailwind?](#q26-how-do-you-style-an-svg-icons-color-in-tailwind) <span class="intermediate">Intermediate</span>
27. [How do you hide elements visually but keep them accessible to screen readers in Bootstrap?](#q27-how-do-you-hide-elements-visually-but-keep-them-accessible-to-screen-readers-in-bootstrap) <span class="beginner">Beginner</span>
28. [How do you style form inputs easily in Tailwind?](#q28-how-do-you-style-form-inputs-easily-in-tailwind) <span class="intermediate">Intermediate</span>
29. [How do you make a table responsive in Bootstrap?](#q29-how-do-you-make-a-table-responsive-in-bootstrap) <span class="beginner">Beginner</span>
30. [How do you style a sibling element based on the state of another in Tailwind (Peer)?](#q30-how-do-you-style-a-sibling-element-based-on-the-state-of-another-in-tailwind-peer) <span class="advanced">Advanced</span>
31. [How do you indicate form validation errors in Bootstrap?](#q31-how-do-you-indicate-form-validation-errors-in-bootstrap) <span class="intermediate">Intermediate</span>
32. [How do you style children when hovering the parent in Tailwind (Group)?](#q32-how-do-you-style-children-when-hovering-the-parent-in-tailwind-group) <span class="intermediate">Intermediate</span>
33. [How do you create a full-screen modal in Bootstrap?](#q33-how-do-you-create-a-full-screen-modal-in-bootstrap) <span class="intermediate">Intermediate</span>
34. [How do you enforce an aspect ratio in Tailwind?](#q34-how-do-you-enforce-an-aspect-ratio-in-tailwind) <span class="intermediate">Intermediate</span>
35. [How do you limit text to a specific number of lines in Tailwind?](#q35-how-do-you-limit-text-to-a-specific-number-of-lines-in-tailwind) <span class="intermediate">Intermediate</span>
36. [How do you position Toasts in Bootstrap?](#q36-how-do-you-position-toasts-in-bootstrap) <span class="intermediate">Intermediate</span>
37. [How do you create a loading spinner animation in Tailwind?](#q37-how-do-you-create-a-loading-spinner-animation-in-tailwind) <span class="beginner">Beginner</span>
38. [How do you implement Scrollspy in Bootstrap?](#q38-how-do-you-implement-scrollspy-in-bootstrap) <span class="advanced">Advanced</span>
39. [How do you create gradient text in Tailwind?](#q39-how-do-you-create-gradient-text-in-tailwind) <span class="intermediate">Intermediate</span>
40. [How do you create an Offcanvas sidebar in Bootstrap?](#q40-how-do-you-create-an-offcanvas-sidebar-in-bootstrap) <span class="intermediate">Intermediate</span>
41. [How do you add dividers between children in Tailwind?](#q41-how-do-you-add-dividers-between-children-in-tailwind) <span class="intermediate">Intermediate</span>
42. [How do you remove borders from an Accordion in Bootstrap (Flush)?](#q42-how-do-you-remove-borders-from-an-accordion-in-bootstrap-flush) <span class="beginner">Beginner</span>
43. [How do you add space between children in Tailwind (Space Between)?](#q43-how-do-you-add-space-between-children-in-tailwind-space-between) <span class="intermediate">Intermediate</span>
44. [How do you make a Badge rounded like a pill in Bootstrap?](#q44-how-do-you-make-a-badge-rounded-like-a-pill-in-bootstrap) <span class="beginner">Beginner</span>
45. [How do you add a focus ring to an element in Tailwind?](#q45-how-do-you-add-a-focus-ring-to-an-element-in-tailwind) <span class="beginner">Beginner</span>
46. [How do you group buttons together in Bootstrap?](#q46-how-do-you-group-buttons-together-in-bootstrap) <span class="beginner">Beginner</span>
47. [How do you use Container Queries in Tailwind?](#q47-how-do-you-use-container-queries-in-tailwind) <span class="advanced">Advanced</span>
48. [How do you vertically center content in a Bootstrap column?](#q48-how-do-you-vertically-center-content-in-a-bootstrap-column) <span class="intermediate">Intermediate</span>
49. [How do you invert colors in Tailwind (Dark Mode manual)?](#q49-how-do-you-invert-colors-in-tailwind-dark-mode-manual) <span class="intermediate">Intermediate</span>
50. [How do you create a Dismissible Alert in Bootstrap?](#q50-how-do-you-create-a-dismissible-alert-in-bootstrap) <span class="intermediate">Intermediate</span>

---

### Q2: How do you customize the Bootstrap 5 theme colors using SASS variables?

**Difficulty**: Intermediate

**Strategy:**
Import the functions and variables, override the map or variables, and then import the rest of Bootstrap.

**Code Example:**
```scss
// 1. Include functions first (so you can manipulate colors, SVGs, calc, etc)
@import "bootstrap/scss/functions";

// 2. Override default variables
$primary: #ff00cc;
$danger: #ff4136;

// 3. Include remainder of required Bootstrap stylesheets
@import "bootstrap/scss/variables";
@import "bootstrap/scss/mixins";
@import "bootstrap/scss/root";
// ... other parts
@import "bootstrap/scss/bootstrap";
```

---

### Q3: How do you extend Tailwind CSS configuration to add custom breakpoints?

**Difficulty**: Intermediate

**Strategy:**
Modify `tailwind.config.js` inside the `theme.extend.screens` object to preserve defaults, or `theme.screens` to override them.

**Code Example:**
```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      screens: {
        '3xl': '1600px', // Adds a new breakpoint
        'portrait': {'raw': '(orientation: portrait)'},
      },
    },
  },
}
```

---

### Q4: How do you create a reusable component style in Tailwind using the `@apply` directive?

**Difficulty**: Beginner

**Strategy:**
Use `@apply` in your global CSS file (e.g., `input.css`) inside a `@layer components` block.

**Code Example:**
```css
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer components {
  .btn-primary {
    @apply py-2 px-4 bg-blue-500 text-white font-semibold rounded-lg shadow-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-400 focus:ring-opacity-75;
  }
}
```

---

### Q5: How do you implement a responsive grid layout in Bootstrap 5 without using custom CSS?

**Difficulty**: Beginner

**Strategy:**
Use the `.container`, `.row`, and `.col-{breakpoint}-{size}` classes.

**Code Example:**
```html
<div class="container">
  <div class="row">
    <!-- Stack on mobile, side-by-side on md screens -->
    <div class="col-12 col-md-6 bg-light">Column 1</div>
    <div class="col-12 col-md-6 bg-secondary">Column 2</div>
  </div>
  <div class="row mt-3">
    <!-- 3 equal columns -->
    <div class="col">1 of 3</div>
    <div class="col">2 of 3</div>
    <div class="col">3 of 3</div>
  </div>
</div>
```

---

### Q6: How do you enable and use arbitrary values in Tailwind CSS for one-off styles?

**Difficulty**: Intermediate

**Strategy:**
Use the square bracket syntax `property-[value]` directly in your HTML.

**Code Example:**
```html
<!-- Specific width, custom color, specific rotation -->
<div class="w-[32rem] bg-[#bada55] rotate-[17deg]">
  Custom arbitrary values
</div>
```

---

### Q7: How do you optimize Tailwind CSS for production to remove unused styles?

**Difficulty**: Advanced

**Strategy:**
Configure the `content` array in `tailwind.config.js` to point to all your template files. Tailwind's JIT engine generates styles on demand.

**Code Example:**
```js
// tailwind.config.js
module.exports = {
  content: [
    './src/**/*.{html,js,jsx,ts,tsx,vue}',
    './public/index.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

---

### Q8: How do you use Bootstrap 5's Utility API to generate custom utility classes?

**Difficulty**: Advanced

**Strategy:**
Modify the `$utilities` map in SASS before importing Bootstrap.

**Code Example:**
```scss
@import "bootstrap/scss/functions";
@import "bootstrap/scss/variables";
@import "bootstrap/scss/mixins";
@import "bootstrap/scss/utilities";

// Add a custom utility for 'cursor'
$utilities: map-merge(
  $utilities,
  (
    "cursor": (
      property: cursor,
      class: cursor,
      values: (
        pointer: pointer,
        grab: grab,
        not-allowed: not-allowed
      )
    )
  )
);

@import "bootstrap/scss/bootstrap";
```

---

### Q9: How do you implement Dark Mode support in Tailwind CSS?

**Difficulty**: Intermediate

**Strategy:**
Set `darkMode: 'class'` in config, then use the `dark:` variant. Toggle the `dark` class on the `html` element via JS.

**Code Example:**
```js
// tailwind.config.js
module.exports = {
  darkMode: 'class', // or 'media' for system preference
  // ...
}
```

```html
<!-- Markup -->
<div class="bg-white dark:bg-gray-800 text-black dark:text-white">
  <h1 class="text-2xl">Dark Mode Supported</h1>
</div>
```

---

### Q10: How do you use Bootstrap components (like Modals) in a React application without jQuery?

**Difficulty**: Intermediate

**Strategy:**
Use `react-bootstrap` or `reactstrap`, which replace Bootstrap's JavaScript with React state management.

**Code Example:**
```jsx
import { Modal, Button } from 'react-bootstrap';
import { useState } from 'react';

function Example() {
  const [show, setShow] = useState(false);

  return (
    <>
      <Button variant="primary" onClick={() => setShow(true)}>
        Launch demo modal
      </Button>

      <Modal show={show} onHide={() => setShow(false)}>
        <Modal.Header closeButton>
          <Modal.Title>Modal heading</Modal.Title>
        </Modal.Header>
        <Modal.Body>Woohoo, you're reading this text in a modal!</Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={() => setShow(false)}>
            Close
          </Button>
        </Modal.Footer>
      </Modal>
    </>
  );
}
```

---

### Q11: How do you create a custom Tailwind CSS plugin to add new variants?

**Difficulty**: Advanced

**Strategy:**
Use the `plugin` function to register a new variant.

**Code Example:**
```js
// tailwind.config.js
const plugin = require('tailwindcss/plugin')

module.exports = {
  plugins: [
    plugin(function({ addVariant }) {
      addVariant('optional', '&:optional')
      addVariant('hocus', ['&:hover', '&:focus'])
    })
  ]
}
```
Usage: `<input class="optional:bg-gray-100 hocus:bg-blue-100" />`

---

### Q12: How do you handle z-index values in Tailwind to avoid conflicts?

**Difficulty**: Intermediate

**Strategy:**
Extend the `zIndex` theme in configuration to use a semantic scale or specific values required by your design system.

**Code Example:**
```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      zIndex: {
        'toast': '5000',
        'modal': '4000',
        'dropdown': '3000',
      }
    }
  }
}
```

---

### Q13: How do you center a div both vertically and horizontally using Bootstrap classes?

**Difficulty**: Beginner

**Strategy:**
Use Flexbox utilities: `d-flex`, `justify-content-center`, and `align-items-center`. Ensure the parent has a defined height (e.g., `vh-100`).

**Code Example:**
```html
<div class="d-flex justify-content-center align-items-center vh-100">
  <div class="p-5 bg-primary text-white">
    Centered Content
  </div>
</div>
```

---

### Q14: How do you apply styles to children elements in Tailwind without adding classes to each child?

**Difficulty**: Advanced

**Strategy:**
Use arbitrary variants like `[&>p]:mt-4` or create a custom plugin/component style.

**Code Example:**
```html
<div class="[&>p]:text-gray-600 [&>p]:mb-4 [&>h2]:text-xl [&>h2]:font-bold">
  <h2>Title</h2>
  <p>First paragraph.</p>
  <p>Second paragraph.</p>
</div>
```

---

### Q15: How do you implement a sticky footer in Tailwind CSS?

**Difficulty**: Intermediate

**Strategy:**
Use Flexbox on the body/wrapper with `flex-col` and `min-h-screen`, then set the main content to `flex-grow` (or `flex-1`).

**Code Example:**
```html
<div class="flex flex-col min-h-screen">
  <header class="bg-blue-500 p-4">Header</header>
  
  <main class="flex-grow p-4">
    Main Content (pushes footer down)
  </main>
  
  <footer class="bg-gray-800 text-white p-4">
    Sticky Footer
  </footer>
</div>
```

---

### Q16: How do you implement a responsive Grid Layout in Tailwind CSS?

**Difficulty**: Beginner

**Strategy:**
Use `grid` and `grid-cols-{n}` utilities. Use breakpoints like `md:grid-cols-3` to change layout on different screens.

**Code Example:**
<div class="grid grid-cols-1 md:grid-cols-3 gap-4">
  <div class="bg-red-200">1</div>
  <div class="bg-blue-200">2</div>
  <div class="bg-green-200">3</div>
</div>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q17: How do you align items using Flexbox in Bootstrap?

**Difficulty**: Beginner

**Strategy:**
Use `d-flex` to enable flexbox. Use `justify-content-*` for main axis and `align-items-*` for cross axis.

**Code Example:**
<div class="d-flex justify-content-between align-items-center">
  <div>Left</div>
  <div>Right</div>
</div>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q18: How do you style Markdown content using Tailwind Typography?

**Difficulty**: Intermediate

**Strategy:**
Install `@tailwindcss/typography` and use the `prose` class on the container.

**Code Example:**
<article class="prose lg:prose-xl">
  <h1>Heading</h1>
  <p>Content...</p>
</article>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q19: How do you apply Spacing (Margin/Padding) in Bootstrap?

**Difficulty**: Beginner

**Strategy:**
Use `{property}{sides}-{size}` syntax. Property: `m` (margin), `p` (padding). Sides: `t`, `b`, `s` (start), `e` (end), `x`, `y`. Size: 0-5.

**Code Example:**
<div class="m-3 p-4 bg-light">
  Margin 3, Padding 4
</div>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q20: How do you create circular images with borders in Tailwind?

**Difficulty**: Beginner

**Strategy:**
Use `rounded-full` for circle, and `border-{width}` `border-{color}`.

**Code Example:**
<img class="rounded-full border-4 border-white h-24 w-24" src="avatar.jpg" />

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q21: How do you add shadows in Bootstrap?

**Difficulty**: Beginner

**Strategy:**
Use `shadow-sm`, `shadow`, `shadow-lg` classes.

**Code Example:**
<div class="shadow-lg p-3 mb-5 bg-body rounded">
  Larger shadow
</div>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q22: How do you apply a blur filter in Tailwind?

**Difficulty**: Intermediate

**Strategy:**
Use `blur-{amount}` utilities (e.g., `blur-sm`, `blur-md`). Often used with `backdrop-blur` for glassmorphism.

**Code Example:**
<div class="backdrop-blur-md bg-white/30 p-4">
  Frosted Glass
</div>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q23: How do you make a link stretch to cover the entire parent card in Bootstrap?

**Difficulty**: Intermediate

**Strategy:**
Use the `stretched-link` class on the link inside a `position-relative` container (like a card).

**Code Example:**
<div class="card">
  <div class="card-body">
    <h5 class="card-title">Card with stretched link</h5>
    <a href="#" class="btn btn-primary stretched-link">Go somewhere</a>
  </div>
</div>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q24: How do you rotate an element in Tailwind?

**Difficulty**: Beginner

**Strategy:**
Use `rotate-{degree}` utilities.

**Code Example:**
<div class="transform rotate-45 bg-blue-500 h-10 w-10"></div>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q25: How do you prevent text selection in Bootstrap?

**Difficulty**: Beginner

**Strategy:**
Use `user-select-none`.

**Code Example:**
<p class="user-select-none">You cannot select this text.</p>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q26: How do you style an SVG icon's color in Tailwind?

**Difficulty**: Intermediate

**Strategy:**
Use `text-{color}` and `fill-current` or `stroke-current` on the SVG.

**Code Example:**
<svg class="h-6 w-6 text-blue-500 fill-current" ...></svg>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q27: How do you hide elements visually but keep them accessible to screen readers in Bootstrap?

**Difficulty**: Beginner

**Strategy:**
Use the `visually-hidden` class.

**Code Example:**
<h2 class="visually-hidden">Title for Screen Readers</h2>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q28: How do you style form inputs easily in Tailwind?

**Difficulty**: Intermediate

**Strategy:**
Install `@tailwindcss/forms` plugin. It resets form styles to be easier to override.

**Code Example:**
// tailwind.config.js
plugins: [require('@tailwindcss/forms')],

// HTML
<input type="text" class="form-input px-4 py-3 rounded-full">

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q29: How do you make a table responsive in Bootstrap?

**Difficulty**: Beginner

**Strategy:**
Wrap the `.table` in a container with `.table-responsive`.

**Code Example:**
<div class="table-responsive">
  <table class="table">
    ...
  </table>
</div>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q30: How do you style a sibling element based on the state of another in Tailwind (Peer)?

**Difficulty**: Advanced

**Strategy:**
Add `peer` class to the trigger element, and `peer-{modifier}:` to the target sibling.

**Code Example:**
<input type="checkbox" class="peer" />
<p class="invisible peer-checked:visible">Checked!</p>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q31: How do you indicate form validation errors in Bootstrap?

**Difficulty**: Intermediate

**Strategy:**
Add `.was-validated` to the form or `.is-invalid` to the input. Provide `.invalid-feedback` div.

**Code Example:**
<input type="text" class="form-control is-invalid" required>
<div class="invalid-feedback">
  Please choose a username.
</div>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q32: How do you style children when hovering the parent in Tailwind (Group)?

**Difficulty**: Intermediate

**Strategy:**
Add `group` class to the parent, and `group-hover:` to the child.

**Code Example:**
<div class="group bg-white hover:bg-blue-500">
  <p class="text-black group-hover:text-white">Text changes color on parent hover</p>
</div>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q33: How do you create a full-screen modal in Bootstrap?

**Difficulty**: Intermediate

**Strategy:**
Use `.modal-fullscreen` class on the `.modal-dialog`.

**Code Example:**
<div class="modal-dialog modal-fullscreen">
  ...
</div>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q34: How do you enforce an aspect ratio in Tailwind?

**Difficulty**: Intermediate

**Strategy:**
Use `aspect-{ratio}` utilities (e.g., `aspect-video`, `aspect-square`).

**Code Example:**
<iframe class="w-full aspect-video" src="..."></iframe>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q35: How do you limit text to a specific number of lines in Tailwind?

**Difficulty**: Intermediate

**Strategy:**
Install `@tailwindcss/line-clamp` (included in v3.3+) and use `line-clamp-{n}`.

**Code Example:**
<p class="line-clamp-3">
  Long text that will be truncated after three lines...
</p>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q36: How do you position Toasts in Bootstrap?

**Difficulty**: Intermediate

**Strategy:**
Wrap toasts in a `.toast-container` and use positioning utilities like `top-0 end-0`.

**Code Example:**
<div class="toast-container position-fixed top-0 end-0 p-3">
  <div class="toast show">...</div>
</div>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q37: How do you create a loading spinner animation in Tailwind?

**Difficulty**: Beginner

**Strategy:**
Use `animate-spin`.

**Code Example:**
<svg class="animate-spin h-5 w-5 mr-3" ...></svg>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q38: How do you implement Scrollspy in Bootstrap?

**Difficulty**: Advanced

**Strategy:**
Add `data-bs-spy='scroll'` to the scrollable element and `data-bs-target` pointing to the navigation.

**Code Example:**
<body data-bs-spy="scroll" data-bs-target="#navbar-example">
  ...
</body>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q39: How do you create gradient text in Tailwind?

**Difficulty**: Intermediate

**Strategy:**
Use `bg-gradient-to-r`, `from-{color}`, `to-{color}`, `bg-clip-text`, and `text-transparent`.

**Code Example:**
<h1 class="text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-pink-600">
  Gradient Text
</h1>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q40: How do you create an Offcanvas sidebar in Bootstrap?

**Difficulty**: Intermediate

**Strategy:**
Use `.offcanvas` component.

**Code Example:**
<div class="offcanvas offcanvas-start" id="demo">
  <div class="offcanvas-header">...</div>
  <div class="offcanvas-body">...</div>
</div>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q41: How do you add dividers between children in Tailwind?

**Difficulty**: Intermediate

**Strategy:**
Use `divide-y` or `divide-x` on the parent container.

**Code Example:**
<div class="divide-y divide-gray-200">
  <div>Item 1</div>
  <div>Item 2</div>
</div>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q42: How do you remove borders from an Accordion in Bootstrap (Flush)?

**Difficulty**: Beginner

**Strategy:**
Use `.accordion-flush` class.

**Code Example:**
<div class="accordion accordion-flush" id="accordionFlushExample">
  ...
</div>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q43: How do you add space between children in Tailwind (Space Between)?

**Difficulty**: Intermediate

**Strategy:**
Use `space-x-{n}` or `space-y-{n}` on the parent. Note: It adds margin to children except the first.

**Code Example:**
<div class="flex space-x-4">
  <div>1</div>
  <div>2</div>
</div>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q44: How do you make a Badge rounded like a pill in Bootstrap?

**Difficulty**: Beginner

**Strategy:**
Use `.rounded-pill` utility along with `.badge`.

**Code Example:**
<span class="badge rounded-pill bg-primary">New</span>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q45: How do you add a focus ring to an element in Tailwind?

**Difficulty**: Beginner

**Strategy:**
Use `ring-{width}`.

**Code Example:**
<button class="focus:ring-2 focus:ring-blue-600">
  Button
</button>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q46: How do you group buttons together in Bootstrap?

**Difficulty**: Beginner

**Strategy:**
Wrap buttons in `.btn-group`.

**Code Example:**
<div class="btn-group" role="group">
  <button type="button" class="btn btn-primary">Left</button>
  <button type="button" class="btn btn-primary">Middle</button>
  <button type="button" class="btn btn-primary">Right</button>
</div>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q47: How do you use Container Queries in Tailwind?

**Difficulty**: Advanced

**Strategy:**
Install `@tailwindcss/container-queries`. Mark parent as `@container`. Use `@lg:text-xl` etc. on children.

**Code Example:**
<div class="@container">
  <div class="@lg:underline">
    Underlined when container is large
  </div>
</div>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q48: How do you vertically center content in a Bootstrap column?

**Difficulty**: Intermediate

**Strategy:**
Use `align-items-center` on the `.row`.

**Code Example:**
<div class="row align-items-center">
  <div class="col">Centered Vertically</div>
</div>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q49: How do you invert colors in Tailwind (Dark Mode manual)?

**Difficulty**: Intermediate

**Strategy:**
Tailwind doesn't have a built-in 'invert' utility for colors specifically, but you can use `invert` filter or explicit dark mode classes.

**Code Example:**
<div class="invert filter">
  <!-- Content colors inverted -->
</div>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q50: How do you create a Dismissible Alert in Bootstrap?

**Difficulty**: Intermediate

**Strategy:**
Add `.alert-dismissible` and a close button with `data-bs-dismiss='alert'`.

**Code Example:**
<div class="alert alert-warning alert-dismissible fade show" role="alert">
  Error!
  <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
</div>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

