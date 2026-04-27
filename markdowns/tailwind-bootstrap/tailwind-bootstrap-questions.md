<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>Tailwind & Bootstrap Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for developers</b></p>
</div>

---

## Table of Contents

2. [How do you customize the Bootstrap 5 theme colors using SASS variables?](#q2) <span class="intermediate">Intermediate</span>
3. [How do you extend Tailwind CSS configuration to add custom breakpoints?](#q3) <span class="intermediate">Intermediate</span>
4. [How do you create a reusable component style in Tailwind using the `@apply` directive?](#q4) <span class="beginner">Beginner</span>
5. [How do you implement a responsive grid layout in Bootstrap 5 without using custom CSS?](#q5) <span class="beginner">Beginner</span>
6. [How do you enable and use arbitrary values in Tailwind CSS for one-off styles?](#q6) <span class="intermediate">Intermediate</span>
7. [How do you optimize Tailwind CSS for production to remove unused styles?](#q7) <span class="advanced">Advanced</span>
8. [How do you use Bootstrap 5's Utility API to generate custom utility classes?](#q8) <span class="advanced">Advanced</span>
9. [How do you implement Dark Mode support in Tailwind CSS?](#q9) <span class="intermediate">Intermediate</span>
10. [How do you use Bootstrap components (like Modals) in a React application without jQuery?](#q10) <span class="intermediate">Intermediate</span>
11. [How do you create a custom Tailwind CSS plugin to add new variants?](#q11) <span class="advanced">Advanced</span>
12. [How do you handle z-index values in Tailwind to avoid conflicts?](#q12) <span class="intermediate">Intermediate</span>
13. [How do you center a div both vertically and horizontally using Bootstrap classes?](#q13) <span class="beginner">Beginner</span>
14. [How do you apply styles to children elements in Tailwind without adding classes to each child?](#q14) <span class="advanced">Advanced</span>
15. [How do you implement a sticky footer in Tailwind CSS?](#q15) <span class="intermediate">Intermediate</span>
16. [How do you implement a responsive Grid Layout in Tailwind CSS?](#q16) <span class="beginner">Beginner</span>
17. [How do you align items using Flexbox in Bootstrap?](#q17) <span class="beginner">Beginner</span>
18. [How do you style Markdown content using Tailwind Typography?](#q18) <span class="intermediate">Intermediate</span>
19. [How do you apply Spacing (Margin/Padding) in Bootstrap?](#q19) <span class="beginner">Beginner</span>
20. [How do you create circular images with borders in Tailwind?](#q20) <span class="beginner">Beginner</span>
21. [How do you add shadows in Bootstrap?](#q21) <span class="beginner">Beginner</span>
22. [How do you apply a blur filter in Tailwind?](#q22) <span class="intermediate">Intermediate</span>
23. [How do you make a link stretch to cover the entire parent card in Bootstrap?](#q23) <span class="intermediate">Intermediate</span>
24. [How do you rotate an element in Tailwind?](#q24) <span class="beginner">Beginner</span>
25. [How do you prevent text selection in Bootstrap?](#q25) <span class="beginner">Beginner</span>
26. [How do you style an SVG icon's color in Tailwind?](#q26) <span class="intermediate">Intermediate</span>
27. [How do you hide elements visually but keep them accessible to screen readers in Bootstrap?](#q27) <span class="beginner">Beginner</span>
28. [How do you style form inputs easily in Tailwind?](#q28) <span class="intermediate">Intermediate</span>
29. [How do you make a table responsive in Bootstrap?](#q29) <span class="beginner">Beginner</span>
30. [How do you style a sibling element based on the state of another in Tailwind (Peer)?](#q30) <span class="advanced">Advanced</span>
31. [How do you indicate form validation errors in Bootstrap?](#q31) <span class="intermediate">Intermediate</span>
32. [How do you style children when hovering the parent in Tailwind (Group)?](#q32) <span class="intermediate">Intermediate</span>
33. [How do you create a full-screen modal in Bootstrap?](#q33) <span class="intermediate">Intermediate</span>
34. [How do you enforce an aspect ratio in Tailwind?](#q34) <span class="intermediate">Intermediate</span>
35. [How do you limit text to a specific number of lines in Tailwind?](#q35) <span class="intermediate">Intermediate</span>
36. [How do you position Toasts in Bootstrap?](#q36) <span class="intermediate">Intermediate</span>
37. [How do you create a loading spinner animation in Tailwind?](#q37) <span class="beginner">Beginner</span>
38. [How do you implement Scrollspy in Bootstrap?](#q38) <span class="advanced">Advanced</span>
39. [How do you create gradient text in Tailwind?](#q39) <span class="intermediate">Intermediate</span>
40. [How do you create an Offcanvas sidebar in Bootstrap?](#q40) <span class="intermediate">Intermediate</span>
41. [How do you add dividers between children in Tailwind?](#q41) <span class="intermediate">Intermediate</span>
42. [How do you remove borders from an Accordion in Bootstrap (Flush)?](#q42) <span class="beginner">Beginner</span>
43. [How do you add space between children in Tailwind (Space Between)?](#q43) <span class="intermediate">Intermediate</span>
44. [How do you make a Badge rounded like a pill in Bootstrap?](#q44) <span class="beginner">Beginner</span>
45. [How do you add a focus ring to an element in Tailwind?](#q45) <span class="beginner">Beginner</span>
46. [How do you group buttons together in Bootstrap?](#q46) <span class="beginner">Beginner</span>
47. [How do you use Container Queries in Tailwind?](#q47) <span class="advanced">Advanced</span>
48. [How do you vertically center content in a Bootstrap column?](#q48) <span class="intermediate">Intermediate</span>
49. [How do you invert colors in Tailwind (Dark Mode manual)?](#q49) <span class="intermediate">Intermediate</span>
50. [How do you create a Dismissible Alert in Bootstrap?](#q50) <span class="intermediate">Intermediate</span>

---

<a id="q2"></a>
### Q2: How do you customize the Bootstrap 5 theme colors using SASS variables?

**Difficulty**: Intermediate

**Strategy**:

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

<a id="q3"></a>
### Q3: How do you extend Tailwind CSS configuration to add custom breakpoints?

**Difficulty**: Intermediate

**Strategy**:

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

<a id="q4"></a>
### Q4: How do you create a reusable component style in Tailwind using the `@apply` directive?

**Difficulty**: Beginner

**Strategy**:

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

<a id="q5"></a>
### Q5: How do you implement a responsive grid layout in Bootstrap 5 without using custom CSS?

**Difficulty**: Beginner

**Strategy**:

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

<a id="q6"></a>
### Q6: How do you enable and use arbitrary values in Tailwind CSS for one-off styles?

**Difficulty**: Intermediate

**Strategy**:

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

<a id="q7"></a>
### Q7: How do you optimize Tailwind CSS for production to remove unused styles?

**Difficulty**: Advanced

**Strategy**:

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

<a id="q8"></a>
### Q8: How do you use Bootstrap 5's Utility API to generate custom utility classes?

**Difficulty**: Advanced

**Strategy**:

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

<a id="q9"></a>
### Q9: How do you implement Dark Mode support in Tailwind CSS?

**Difficulty**: Intermediate

**Strategy**:

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

<a id="q10"></a>
### Q10: How do you use Bootstrap components (like Modals) in a React application without jQuery?

**Difficulty**: Intermediate

**Strategy**:

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

<a id="q11"></a>
### Q11: How do you create a custom Tailwind CSS plugin to add new variants?

**Difficulty**: Advanced

**Strategy**:

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

<a id="q12"></a>
### Q12: How do you handle z-index values in Tailwind to avoid conflicts?

**Difficulty**: Intermediate

**Strategy**:

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

<a id="q13"></a>
### Q13: How do you center a div both vertically and horizontally using Bootstrap classes?

**Difficulty**: Beginner

**Strategy**:

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

<a id="q14"></a>
### Q14: How do you apply styles to children elements in Tailwind without adding classes to each child?

**Difficulty**: Advanced

**Strategy**:

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

<a id="q15"></a>
### Q15: How do you implement a sticky footer in Tailwind CSS?

**Difficulty**: Intermediate

**Strategy**:

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

<a id="q16"></a>
### Q16: How do you implement a responsive Grid Layout in Tailwind CSS?

**Difficulty**: Beginner

**Strategy**:

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

<a id="q17"></a>
### Q17: How do you align items using Flexbox in Bootstrap?

**Difficulty**: Beginner

**Strategy**:

**Strategy:**
Use `d-flex` to enable flexbox. Use `justify-content-*` for main axis and `align-items-*` for cross axis.

**Code Example:**
<div class="d-flex justify-content-between align-items-center">
  <div>Left</div>
  <div>Right</div>
</div>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q18"></a>
### Q18: How do you style Markdown content using Tailwind Typography?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Install `@tailwindcss/typography` and use the `prose` class on the container.

**Code Example:**
<article class="prose lg:prose-xl">
  <h1>Heading</h1>
  <p>Content...</p>
</article>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q19"></a>
### Q19: How do you apply Spacing (Margin/Padding) in Bootstrap?

**Difficulty**: Beginner

**Strategy**:

**Strategy:**
Use `{property}{sides}-{size}` syntax. Property: `m` (margin), `p` (padding). Sides: `t`, `b`, `s` (start), `e` (end), `x`, `y`. Size: 0-5.

**Code Example:**
<div class="m-3 p-4 bg-light">
  Margin 3, Padding 4
</div>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q20"></a>
### Q20: How do you create circular images with borders in Tailwind?

**Difficulty**: Beginner

**Strategy**:

**Strategy:**
Use `rounded-full` for circle, and `border-{width}` `border-{color}`.

**Code Example:**
<img class="rounded-full border-4 border-white h-24 w-24" src="avatar.jpg" />

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q21"></a>
### Q21: How do you add shadows in Bootstrap?

**Difficulty**: Beginner

**Strategy**:

**Strategy:**
Use `shadow-sm`, `shadow`, `shadow-lg` classes.

**Code Example:**
<div class="shadow-lg p-3 mb-5 bg-body rounded">
  Larger shadow
</div>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q22"></a>
### Q22: How do you apply a blur filter in Tailwind?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Use `blur-{amount}` utilities (e.g., `blur-sm`, `blur-md`). Often used with `backdrop-blur` for glassmorphism.

**Code Example:**
<div class="backdrop-blur-md bg-white/30 p-4">
  Frosted Glass
</div>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q23"></a>
### Q23: How do you make a link stretch to cover the entire parent card in Bootstrap?

**Difficulty**: Intermediate

**Strategy**:

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

<a id="q24"></a>
### Q24: How do you rotate an element in Tailwind?

**Difficulty**: Beginner

**Strategy**: CSS transforms are fundamental for animations and visual effects, and Tailwind makes rotation accessible through utility classes. The `rotate-{angle}` utilities (e.g., `rotate-45`, `rotate-90`) apply CSS transform values, and they compose with `transform` for broader transform chains. A common pitfall is forgetting that transforms create a new stacking context, which can affect z-index and overflow behavior.

**Strategy:**

**Code Example:**
<div class="transform rotate-45 bg-blue-500 h-10 w-10"></div>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q25"></a>
### Q25: How do you prevent text selection in Bootstrap?

**Difficulty**: Beginner

**Strategy**: Controlling text selection is important for interactive UI elements like buttons, drag handles, and custom controls where accidental selection degrades the user experience. Bootstrap provides `user-select-none` (and related utilities) that map to the CSS `user-select` property. Use this sparingly though, as preventing selection on actual content harms accessibility and frustrates users.

**Strategy:**

**Code Example:**
<p class="user-select-none">You cannot select this text.</p>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q26"></a>
### Q26: How do you style an SVG icon's color in Tailwind?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Use `text-{color}` and `fill-current` or `stroke-current` on the SVG.

**Code Example:**
<svg class="h-6 w-6 text-blue-500 fill-current" ...></svg>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q27"></a>
### Q27: How do you hide elements visually but keep them accessible to screen readers in Bootstrap?

**Difficulty**: Beginner

**Strategy**: Accessibility is a critical frontend skill, and visually hiding content while keeping it available to assistive technology is a standard WCAG technique. Bootstrap's `visually-hidden` class applies the well-known sr-only pattern using `clip`, `position`, and `overflow` to remove elements from the visual flow without hiding them from screen readers. A common mistake is using `display: none` or `visibility: hidden`, which also removes the element from the accessibility tree.

**Strategy:**

**Code Example:**
<h2 class="visually-hidden">Title for Screen Readers</h2>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q28"></a>
### Q28: How do you style form inputs easily in Tailwind?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Install `@tailwindcss/forms` plugin. It resets form styles to be easier to override.

**Code Example:**
// tailwind.config.js
plugins: [require('@tailwindcss/forms')],

// HTML
<input type="text" class="form-input px-4 py-3 rounded-full">

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q29"></a>
### Q29: How do you make a table responsive in Bootstrap?

**Difficulty**: Beginner

**Strategy**:

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

<a id="q30"></a>
### Q30: How do you style a sibling element based on the state of another in Tailwind (Peer)?

**Difficulty**: Advanced

**Strategy**:

**Strategy:**
Add `peer` class to the trigger element, and `peer-{modifier}:` to the target sibling.

**Code Example:**
<input type="checkbox" class="peer" />
<p class="invisible peer-checked:visible">Checked!</p>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q31"></a>
### Q31: How do you indicate form validation errors in Bootstrap?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Add `.was-validated` to the form or `.is-invalid` to the input. Provide `.invalid-feedback` div.

**Code Example:**
<input type="text" class="form-control is-invalid" required>
<div class="invalid-feedback">
  Please choose a username.
</div>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q32"></a>
### Q32: How do you style children when hovering the parent in Tailwind (Group)?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Add `group` class to the parent, and `group-hover:` to the child.

**Code Example:**
<div class="group bg-white hover:bg-blue-500">
  <p class="text-black group-hover:text-white">Text changes color on parent hover</p>
</div>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q33"></a>
### Q33: How do you create a full-screen modal in Bootstrap?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Use `.modal-fullscreen` class on the `.modal-dialog`.

**Code Example:**
<div class="modal-dialog modal-fullscreen">
  ...
</div>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q34"></a>
### Q34: How do you enforce an aspect ratio in Tailwind?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Use `aspect-{ratio}` utilities (e.g., `aspect-video`, `aspect-square`).

**Code Example:**
<iframe class="w-full aspect-video" src="..."></iframe>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q35"></a>
### Q35: How do you limit text to a specific number of lines in Tailwind?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Install `@tailwindcss/line-clamp` (included in v3.3+) and use `line-clamp-{n}`.

**Code Example:**
<p class="line-clamp-3">
  Long text that will be truncated after three lines...
</p>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q36"></a>
### Q36: How do you position Toasts in Bootstrap?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Wrap toasts in a `.toast-container` and use positioning utilities like `top-0 end-0`.

**Code Example:**
<div class="toast-container position-fixed top-0 end-0 p-3">
  <div class="toast show">...</div>
</div>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q37"></a>
### Q37: How do you create a loading spinner animation in Tailwind?

**Difficulty**: Beginner

**Strategy**: Loading indicators are essential UX elements that provide feedback during async operations, and Tailwind's built-in animation utilities make spinners trivial to implement. The `animate-spin` utility applies a continuous CSS rotation keyframe, commonly used on SVG or div elements to create spinner visuals. For production use, remember to add ARIA attributes like `role="status"` and `aria-label="Loading"` for accessibility.

**Strategy:**

**Code Example:**
<svg class="animate-spin h-5 w-5 mr-3" ...></svg>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q38"></a>
### Q38: How do you implement Scrollspy in Bootstrap?

**Difficulty**: Advanced

**Strategy**:

**Strategy:**
Add `data-bs-spy='scroll'` to the scrollable element and `data-bs-target` pointing to the navigation.

**Code Example:**
<body data-bs-spy="scroll" data-bs-target="#navbar-example">
  ...
</body>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q39"></a>
### Q39: How do you create gradient text in Tailwind?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Use `bg-gradient-to-r`, `from-{color}`, `to-{color}`, `bg-clip-text`, and `text-transparent`.

**Code Example:**
<h1 class="text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-pink-600">
  Gradient Text
</h1>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q40"></a>
### Q40: How do you create an Offcanvas sidebar in Bootstrap?

**Difficulty**: Intermediate

**Strategy**: Offcanvas components are a modern UI pattern for navigation drawers, filter panels, and mobile menus that slide in from the edge of the viewport. Bootstrap's Offcanvas component provides built-in backdrop, animation, and responsive behavior with minimal markup. A best practice is to use the `responsive` variant (`offcanvas-lg`) so the sidebar renders inline on larger screens and as an offcanvas drawer only on mobile.

**Strategy:**

**Code Example:**
<div class="offcanvas offcanvas-start" id="demo">
  <div class="offcanvas-header">...</div>
  <div class="offcanvas-body">...</div>
</div>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q41"></a>
### Q41: How do you add dividers between children in Tailwind?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Use `divide-y` or `divide-x` on the parent container.

**Code Example:**
<div class="divide-y divide-gray-200">
  <div>Item 1</div>
  <div>Item 2</div>
</div>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q42"></a>
### Q42: How do you remove borders from an Accordion in Bootstrap (Flush)?

**Difficulty**: Beginner

**Strategy**: Default accordion styling includes borders and rounded corners that may not fit every design system, especially when accordions are placed inside cards or containers that already have their own borders. The `accordion-flush` class removes outer borders and rounded corners, giving a seamless, embedded look. A common mistake is trying to override borders with custom CSS when this built-in modifier already handles it.

**Strategy:**

**Code Example:**
<div class="accordion accordion-flush" id="accordionFlushExample">
  ...
</div>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q43"></a>
### Q43: How do you add space between children in Tailwind (Space Between)?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Use `space-x-{n}` or `space-y-{n}` on the parent. Note: It adds margin to children except the first.

**Code Example:**
<div class="flex space-x-4">
  <div>1</div>
  <div>2</div>
</div>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q44"></a>
### Q44: How do you make a Badge rounded like a pill in Bootstrap?

**Difficulty**: Beginner

**Strategy**:

**Strategy:**
Use `.rounded-pill` utility along with `.badge`.

**Code Example:**
<span class="badge rounded-pill bg-primary">New</span>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q45"></a>
### Q45: How do you add a focus ring to an element in Tailwind?

**Difficulty**: Beginner

**Strategy**: Focus indicators are essential for keyboard accessibility and a common interview topic because many developers accidentally remove them with `outline-none` without providing an alternative. Tailwind's `focus:ring-*` utilities provide a visible, customizable focus ring that replaces the default browser outline. Always pair `focus:outline-none` with a `focus:ring` variant to maintain keyboard accessibility compliance.

**Strategy:**

**Code Example:**
<button class="focus:ring-2 focus:ring-blue-600">
  Button
</button>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q46"></a>
### Q46: How do you group buttons together in Bootstrap?

**Difficulty**: Beginner

**Strategy**: Button groups are a fundamental UI pattern for toolbars, toggle sets, and segmented controls where related actions should be visually connected. Bootstrap's `btn-group` applies flexbox layout with rounded corners only on the outer edges and removes gaps between buttons. A best practice is to always include the `role="group"` ARIA attribute so screen readers announce the buttons as a related set rather than individual controls.

**Strategy:**

**Code Example:**
<div class="btn-group" role="group">
  <button type="button" class="btn btn-primary">Left</button>
  <button type="button" class="btn btn-primary">Middle</button>
  <button type="button" class="btn btn-primary">Right</button>
</div>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q47"></a>
### Q47: How do you use Container Queries in Tailwind?

**Difficulty**: Advanced

**Strategy**:

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

<a id="q48"></a>
### Q48: How do you vertically center content in a Bootstrap column?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Use `align-items-center` on the `.row`.

**Code Example:**
<div class="row align-items-center">
  <div class="col">Centered Vertically</div>
</div>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q49"></a>
### Q49: How do you invert colors in Tailwind (Dark Mode manual)?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Tailwind doesn't have a built-in 'invert' utility for colors specifically, but you can use `invert` filter or explicit dark mode classes.

**Code Example:**
<div class="invert filter">
  <!-- Content colors inverted -->
</div>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q50"></a>
### Q50: How do you create a Dismissible Alert in Bootstrap?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Add `.alert-dismissible` and a close button with `data-bs-dismiss='alert'`.

**Code Example:**
<div class="alert alert-warning alert-dismissible fade show" role="alert">
  Error!
  <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
</div>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>
