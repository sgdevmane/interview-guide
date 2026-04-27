<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>Material & Radix UI Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for developers</b></p>
</div>

---

## Table of Contents

1. [How do you customize the Material UI theme?](#q1) <span class="beginner">Beginner</span>
2. [How do you use the `sx` prop in Material UI?](#q2) <span class="intermediate">Intermediate</span>
3. [Difference between Controlled and Uncontrolled components in Radix UI?](#q3) <span class="intermediate">Intermediate</span>
4. [How do you optimize Material UI bundle size?](#q4) <span class="advanced">Advanced</span>
5. [How do you implement a Dialog in Radix UI?](#q5) <span class="beginner">Beginner</span>
6. [How do you handle responsive styles in Material UI?](#q6) <span class="intermediate">Intermediate</span>
7. [How do you style Radix UI components with Tailwind?](#q7) <span class="intermediate">Intermediate</span>
8. [How do you create a custom styled component in MUI?](#q8) <span class="intermediate">Intermediate</span>
9. [How do you handle accessibility (a11y) in Radix UI?](#q9) <span class="beginner">Beginner</span>
10. [How do you implement Dark Mode in MUI?](#q10) <span class="intermediate">Intermediate</span>
11. [What is the `asChild` prop in Radix UI?](#q11) <span class="intermediate">Intermediate</span>
12. [How do you override default MUI component styles globally?](#q12) <span class="advanced">Advanced</span>
13. [What is the Box component in MUI?](#q13) <span class="beginner">Beginner</span>
14. [How do you use useMediaQuery in MUI?](#q14) <span class="intermediate">Intermediate</span>
15. [What is the difference between Radix UI and Headless UI?](#q15) <span class="intermediate">Intermediate</span>
16. [How do you handle z-index issues in MUI?](#q16) <span class="intermediate">Intermediate</span>
17. [How do you make a Radix UI Dialog accessible?](#q17) <span class="beginner">Beginner</span>
18. [How do you create a layout with MUI Grid?](#q18) <span class="beginner">Beginner</span>
19. [What is the Portal component used for?](#q19) <span class="intermediate">Intermediate</span>
20. [How do you enable CSS variables in MUI?](#q20) <span class="advanced">Advanced</span>
21. [How do you handle form validation with MUI?](#q21) <span class="intermediate">Intermediate</span>
22. [What is the Typography component?](#q22) <span class="beginner">Beginner</span>
23. [What is the Grid system in MUI?](#q23) <span class="beginner">Beginner</span>
24. [What is the Box component?](#q24) <span class="beginner">Beginner</span>
25. [What is the Stack component?](#q25) <span class="beginner">Beginner</span>
26. [How do you override theme defaults?](#q26) <span class="intermediate">Intermediate</span>
27. [What is the `sx` prop performance cost?](#q27) <span class="advanced">Advanced</span>
28. [How do you use Icons in MUI?](#q28) <span class="beginner">Beginner</span>
29. [What is the Typography variants?](#q29) <span class="beginner">Beginner</span>
30. [How do you handle Date Pickers?](#q30) <span class="intermediate">Intermediate</span>
31. [What is the DataGrid component?](#q31) <span class="advanced">Advanced</span>
32. [How do you make a responsive drawer?](#q32) <span class="intermediate">Intermediate</span>
33. [What is `CssBaseline`?](#q33) <span class="beginner">Beginner</span>
34. [How do you use custom fonts?](#q34) <span class="intermediate">Intermediate</span>
35. [What is the `makeStyles` (legacy)?](#q35) <span class="intermediate">Intermediate</span>
36. [How do you migrate from v4 to v5?](#q36) <span class="advanced">Advanced</span>
37. [What is Radix Primitives?](#q37) <span class="beginner">Beginner</span>
38. [How does Radix handle focus?](#q38) <span class="intermediate">Intermediate</span>
39. [What is `asChild` in Radix?](#q39) <span class="intermediate">Intermediate</span>
40. [How do you style Radix with CSS Modules?](#q40) <span class="beginner">Beginner</span>
41. [How do you animate Radix components?](#q41) <span class="intermediate">Intermediate</span>
42. [What is Radix Colors?](#q42) <span class="beginner">Beginner</span>
43. [How do you use Radix Icons?](#q43) <span class="beginner">Beginner</span>
44. [What is `Portal` in Radix?](#q44) <span class="intermediate">Intermediate</span>
45. [Difference between Popover and Tooltip?](#q45) <span class="intermediate">Intermediate</span>
46. [What is Accordion in Radix?](#q46) <span class="beginner">Beginner</span>
47. [How do you handle form constraints in Radix?](#q47) <span class="intermediate">Intermediate</span>
48. [What is the `Slot` utility?](#q48) <span class="advanced">Advanced</span>
49. [How do you implement Toast?](#q49) <span class="intermediate">Intermediate</span>
50. [What is `VisuallyHidden`?](#q50) <span class="beginner">Beginner</span>
51. [How do you server render Radix?](#q51) <span class="intermediate">Intermediate</span>
52. [What is Shadcn UI?](#q52) <span class="intermediate">Intermediate</span>
53. [How does Shadcn differ from MUI?](#q53) <span class="intermediate">Intermediate</span>
54. [What is Headless UI?](#q54) <span class="intermediate">Intermediate</span>
55. [How do you create a dark mode switch in MUI?](#q55) <span class="beginner">Beginner</span>
56. [What is `useTheme` hook?](#q56) <span class="beginner">Beginner</span>
57. [How do you customize breakpoints?](#q57) <span class="intermediate">Intermediate</span>
58. [What is the `Container` component?](#q58) <span class="beginner">Beginner</span>
59. [How do you use Skeleton loading?](#q59) <span class="beginner">Beginner</span>
60. [What is the `Autocomplete` component?](#q60) <span class="intermediate">Intermediate</span>
61. [How do you handle virtualized lists in MUI?](#q61) <span class="advanced">Advanced</span>
62. [What is the `ClickAwayListener`?](#q62) <span class="intermediate">Intermediate</span>
63. [How do you use `Backdrop`?](#q63) <span class="beginner">Beginner</span>
64. [What is `SpeedDial`?](#q64) <span class="intermediate">Intermediate</span>
65. [How do you customize scrollbars in MUI?](#q65) <span class="intermediate">Intermediate</span>
66. [What is `Collapse` transition?](#q66) <span class="beginner">Beginner</span>
67. [How do you use `Zoom` transition?](#q67) <span class="beginner">Beginner</span>
68. [What is `Grow` transition?](#q68) <span class="beginner">Beginner</span>
69. [What is `Slide` transition?](#q69) <span class="beginner">Beginner</span>
70. [How do you use `Fade` transition?](#q70) <span class="beginner">Beginner</span>
71. [What is `GlobalStyles`?](#q71) <span class="intermediate">Intermediate</span>
72. [How do you theme variants?](#q72) <span class="intermediate">Intermediate</span>
73. [What is `shouldForwardProp`?](#q73) <span class="advanced">Advanced</span>
74. [How do you use `alpha` utility?](#q74) <span class="intermediate">Intermediate</span>
75. [What is `darken`/`lighten`?](#q75) <span class="intermediate">Intermediate</span>
76. [How do you use `useScrollTrigger`?](#q76) <span class="intermediate">Intermediate</span>
77. [What is `FocusTrap`?](#q77) <span class="intermediate">Intermediate</span>
78. [How do you use `NoSsr`?](#q78) <span class="intermediate">Intermediate</span>
79. [What is `TextareaAutosize`?](#q79) <span class="beginner">Beginner</span>
80. [How do you use `Rating`?](#q80) <span class="beginner">Beginner</span>
81. [What is `Timeline`?](#q81) <span class="intermediate">Intermediate</span>
82. [How do you use `TreeView`?](#q82) <span class="intermediate">Intermediate</span>
83. [What is `Masonry`?](#q83) <span class="intermediate">Intermediate</span>
84. [How do you use `Snackbar`?](#q84) <span class="beginner">Beginner</span>
85. [What is `Alert`?](#q85) <span class="beginner">Beginner</span>
86. [How do you customize shadow?](#q86) <span class="intermediate">Intermediate</span>
87. [What is `Paper`?](#q87) <span class="beginner">Beginner</span>
88. [How do you use `Card`?](#q88) <span class="beginner">Beginner</span>
89. [What is `Divider`?](#q89) <span class="beginner">Beginner</span>
90. [How do you use `Chip`?](#q90) <span class="beginner">Beginner</span>
91. [What is `Badge`?](#q91) <span class="beginner">Beginner</span>
92. [How do you use `Avatar`?](#q92) <span class="beginner">Beginner</span>
93. [What is `LinearProgress`?](#q93) <span class="beginner">Beginner</span>
94. [What is `CircularProgress`?](#q94) <span class="beginner">Beginner</span>
95. [How do you use `Tabs`?](#q95) <span class="intermediate">Intermediate</span>
96. [What is `BottomNavigation`?](#q96) <span class="intermediate">Intermediate</span>
97. [How do you use `Breadcrumbs`?](#q97) <span class="beginner">Beginner</span>
98. [What is `Link` component?](#q98) <span class="beginner">Beginner</span>
99. [How do you use `Stepper`?](#q99) <span class="intermediate">Intermediate</span>
100. [How does Radix UI handle accessibility?](#q100) <span class="intermediate">Intermediate</span>

---

<a id="q1"></a>
### Q1: How do you customize the Material UI theme?

**Difficulty**: Beginner

**Strategy**: Theme customization is fundamental to maintaining a consistent design system across an application. The `createTheme` function lets you override palette, typography, spacing, and component defaults in a single configuration object that propagates through `ThemeProvider`. A common mistake is creating a new theme object on every render -- always define it outside the component or memoize it to avoid unnecessary re-renders.

**Code Example**:
```javascript
const theme = createTheme({ palette: { primary: { main: '#ff4400' } } });
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q2"></a>
### Q2: How do you use the `sx` prop in Material UI?

**Difficulty**: Intermediate

**Strategy**: The `sx` prop is MUI's recommended way to apply one-off styles inline, offering a concise alternative to `styled()` or separate CSS files for quick overrides. It supports shorthand responsive values, theme token references (like `'primary.main'`), and all CSS properties through a system-aware API. A common pitfall is overusing `sx` for complex or reusable styles -- prefer `styled()` for component-level styles that repeat across the app, and reserve `sx` for situational overrides.

**Code Example**:
```javascript
<Button sx={{ margin: 2, color: 'primary.main' }}>Click Me</Button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q3"></a>
### Q3: Difference between Controlled and Uncontrolled components in Radix UI?

**Difficulty**: Intermediate

**Strategy**: Understanding controlled vs. uncontrolled patterns is essential because it determines how form state flows through your application and whether you need to manage it explicitly. Controlled components pair `value` with `onValueChange` so the parent owns the state, while uncontrolled components use `defaultValue` and let the DOM manage it internally. A best practice is to use controlled mode when you need to validate, transform, or react to value changes in real time, and uncontrolled mode for simple forms where the value is only needed on submit.

**Code Example**:
```javascript
<Accordion value={val} onValueChange={setVal} /> vs <Accordion defaultValue="1" />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q4"></a>
### Q4: How do you optimize Material UI bundle size?

**Difficulty**: Advanced

**Strategy**: Bundle size optimization is critical for MUI because the full library includes hundreds of components and icons that can bloat your JavaScript payload if imported carelessly. Path imports (`@mui/material/Button` vs `@mui/material`) enable bundlers to tree-shake unused modules, and MUI v5 also supports second-level path imports for even smaller bundles. A common mistake is importing from the top-level barrel export with destructuring (`import { Button } from '@mui/material'`) -- while modern bundlers handle this better, explicit path imports remain the safest approach.

**Code Example**:
```javascript
import Button from '@mui/material/Button'; // Better than import { Button }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q5"></a>
### Q5: How do you implement a Dialog in Radix UI?

**Difficulty**: Beginner

**Strategy**: Dialogs are one of the most commonly needed UI patterns, and Radix decomposes them into composable parts (`Root`, `Trigger`, `Portal`, `Overlay`, `Content`, `Title`, `Description`, `Close`) so you control every piece of the markup and styling. This composable architecture gives you full design freedom while Radix handles focus trapping, scroll locking, and ARIA attributes behind the scenes. A best practice is to always include `Dialog.Title` and `Dialog.Description` -- omitting them creates accessibility violations that screen readers cannot navigate properly.

**Code Example**:
```javascript
<Dialog.Root><Dialog.Trigger>Open</Dialog.Trigger><Dialog.Content>...</Dialog.Content></Dialog.Root>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q6"></a>
### Q6: How do you handle responsive styles in Material UI?

**Difficulty**: Intermediate

**Strategy**: Responsive design is essential for any production application, and MUI provides two primary approaches: the `sx` prop's breakpoint-aware array/object syntax and the `useMediaQuery` hook for JavaScript-driven responsiveness. The `sx` approach is declarative and preferred for style-only changes, while `useMediaQuery` is necessary when responsiveness affects component structure or logic. A common pitfall is using array syntax without understanding that it maps to MUI's default breakpoints (xs, sm, md, lg, xl) in order -- always verify the mapping matches your design intent.

**Code Example**:
```javascript
<Box sx={{ width: [100, 200, 300] }}>Responsiveness</Box>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q7"></a>
### Q7: How do you style Radix UI components with Tailwind?

**Difficulty**: Intermediate

**Strategy**: Radix's unstyled architecture pairs naturally with Tailwind CSS because every Radix part accepts a `className` prop, letting you apply utility classes directly without a styling library in between. This combination is the foundation of popular frameworks like Shadcn UI and gives you full visual control while retaining Radix's accessibility guarantees. A best practice is to use Radix's `data-state` attributes (e.g., `data-[state=open]`) in Tailwind classes to style open/closed/active states without writing custom CSS.

**Code Example**:
```javascript
<Dialog.Content className="fixed bg-white p-4 rounded">
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q8"></a>
### Q8: How do you create a custom styled component in MUI?

**Difficulty**: Intermediate

**Strategy**: The `styled()` API is the primary way to build reusable custom components with MUI, leveraging emotion (or styled-components) under the hood while accessing theme tokens. It supports dynamic styling through callback functions that receive the theme and props, enabling powerful component variants. Be aware that `styled()` creates a new component identity each time it is called, so define styled components at module level rather than inside render functions to avoid remounting on every update.

**Code Example**:
```javascript
const MyButton = styled(Button)({ color: 'red' });
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q9"></a>
### Q9: How do you handle accessibility (a11y) in Radix UI?

**Difficulty**: Beginner

**Strategy**: Accessibility is not optional in modern web development, and Radix's biggest value proposition is that it handles ARIA attributes, keyboard navigation, focus management, and screen reader support automatically. Each primitive follows the WAI-ARIA Authoring Practices, so developers get compliance without deep accessibility expertise. A common pitfall is assuming accessibility is fully handled -- you must still provide meaningful labels, use semantic HTML for content, and test with actual assistive technology.

**Code Example**:
```javascript
// No extra code needed for basic a11y
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q10"></a>
### Q10: How do you implement Dark Mode in MUI?

**Difficulty**: Intermediate

**Strategy**: Dark mode is a user expectation in modern apps, and MUI supports it natively by toggling `palette.mode` in `createTheme` -- the entire component library automatically adjusts colors when the mode switches. The key trade-off is deciding between a single theme with mode toggling (simpler) vs. two separate themes (more control over individual dark palette values). A common mistake is only changing the mode without customizing the dark palette tokens, which can result in poor contrast or inconsistent branding in dark mode.

**Code Example**:
```javascript
const theme = createTheme({ palette: { mode: 'dark' } });
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q11"></a>
### Q11: What is the `asChild` prop in Radix UI?

**Difficulty**: Intermediate

**Strategy**: The `asChild` prop solves a common composition problem: it lets Radix merge its behavior (event handlers, ARIA attributes, refs) onto your custom child element instead of wrapping it in an extra DOM node. This is crucial for avoiding invalid HTML like a `<button>` nested inside another `<button>`, which violates accessibility rules. Remember that `asChild` expects exactly one React element child -- passing text nodes, fragments, or multiple elements will cause it to fall back to rendering its own default element.

**Code Example**:
```javascript
<Dialog.Trigger asChild><button>Open</button></Dialog.Trigger>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q12"></a>
### Q12: How do you override default MUI component styles globally?

**Difficulty**: Advanced

**Strategy**: Global style overrides through the theme's `components` key ensure consistency without patching individual instances across the codebase. You can target specific slots within a component (like `root`, `outlined`, `contained`) and even define conditional variants based on props. A common pitfall is using overly specific CSS selectors that fight MUI's internal specificity -- prefer `styleOverrides` and `styled` at the theme level over `!important` hacks.

**Code Example**:
```javascript
createTheme({ components: { MuiButton: { styleOverrides: { root: { fontSize: '1rem' } } } } })
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q13"></a>
### Q13: What is the Box component in MUI?

**Difficulty**: Beginner

**Strategy**: Box is the most versatile utility component in MUI, acting as a polymorphic wrapper that accepts all style system props and renders a `<div>` by default but can be changed to any HTML element via the `component` prop. It is the recommended way to apply one-off layout styles using the `sx` prop without creating a new styled component. A common pitfall is overusing Box as a replacement for semantic HTML -- use it for layout utility while still choosing meaningful tags like `<section>`, `<nav>`, or `<article>` when appropriate.

**Code Example**:
```javascript
<Box m={2} p={1} bgcolor="grey.100">Content</Box>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q14"></a>
### Q14: How do you use useMediaQuery in MUI?

**Difficulty**: Intermediate

**Strategy**: `useMediaQuery` provides a React-friendly way to respond to viewport changes, which is essential for building adaptive layouts beyond what CSS media queries alone can handle. It accepts a CSS media query string and returns a boolean that updates reactively when the viewport changes. Remember that this hook relies on `window.matchMedia` and will not work during server-side rendering -- wrap usage in a client-side check or use the `NoSsr` component to avoid hydration mismatches.

**Code Example**:
```javascript
const matches = useMediaQuery('(min-width:600px)');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q15"></a>
### Q15: What is the difference between Radix UI and Headless UI?

**Difficulty**: Intermediate

**Strategy**: Interviewers ask this to gauge your understanding of the headless component ecosystem and your ability to choose the right tool for a project. Both libraries provide unstyled, accessible components, but Radix UI offers a wider range of primitives (over 30) with granular composable parts, while Headless UI by Tailwind Labs has a smaller, simpler API focused on the most common patterns. The trade-off comes down to ecosystem fit: Radix pairs well with any styling solution and powers frameworks like Shadcn UI, while Headless UI is designed to integrate seamlessly with Tailwind CSS.

**Code Example**:
```javascript
// Choice depends on ecosystem preference
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q16"></a>
### Q16: How do you handle z-index issues in MUI?

**Difficulty**: Intermediate

**Strategy**: MUI assigns a managed z-index scale (mobile stepper, speed dial, app bar, drawer, modal, snackbar, tooltip) to keep layered UI elements in a predictable stacking order. Using these semantic tokens instead of arbitrary numbers prevents z-index wars between components like modals, tooltips, and drawers. A common mistake is setting extremely high z-index values to force stacking -- instead, customize the theme's `zIndex` object to keep the hierarchy intentional and maintainable.

**Code Example**:
```javascript
sx={{ zIndex: 'tooltip' }}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q17"></a>
### Q17: How do you make a Radix UI Dialog accessible?

**Difficulty**: Beginner

**Strategy**: Dialog accessibility is one of the most commonly tested UI patterns in interviews because it involves multiple concerns: focus trapping, ARIA roles, keyboard escape behavior, and scroll locking. Radix Dialog handles all of these automatically through its composable parts (`Root`, `Trigger`, `Content`, `Title`, `Description`), but you must include `Dialog.Title` and `Dialog.Description` for full compliance. A best practice is to use `Dialog.Close` with a visible dismiss button so users who cannot press Escape still have a way to close the dialog.

**Code Example**:
```javascript
// Just use the primitives correctly
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q18"></a>
### Q18: How do you create a layout with MUI Grid?

**Difficulty**: Beginner

**Strategy**: Grid layout is fundamental to building responsive page structures, and MUI's Grid uses a 12-column flexbox model where breakpoint props (`xs`, `sm`, `md`, `lg`, `xl`) control column spans at each viewport size. The `container` prop enables the flexbox context and the `item` prop distributes space, with the `spacing` prop handling gutters between cells. A common pitfall is forgetting that Grid uses negative margins for spacing, which can cause overflow -- wrap Grid containers in a parent with `overflow: hidden` or use `spacing={0}` with manual padding.

**Code Example**:
```javascript
<Grid container><Grid item xs={6}>Left</Grid><Grid item xs={6}>Right</Grid></Grid>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q19"></a>
### Q19: What is the Portal component used for?

**Difficulty**: Intermediate

**Strategy**: Portals solve a critical rendering problem by teleporting children to a DOM node outside the current component tree, which is essential for modals, tooltips, and dropdowns that would otherwise be clipped by `overflow: hidden` or trapped in a low stacking context. MUI's Portal wraps React's `createPortal` with a convenient component API and supports a `container` prop to target a specific DOM element. A common pitfall is that portal content does not inherit CSS from parent components -- use global styles, CSS variables, or a shared theme provider to ensure consistent styling across portal boundaries.

**Code Example**:
```javascript
<Portal><div>I am outside root</div></Portal>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q20"></a>
### Q20: How do you enable CSS variables in MUI?

**Difficulty**: Advanced

**Strategy**: CSS variables (custom properties) enable theme values to be consumed directly in CSS rather than only through JavaScript, which unlocks dynamic theming, SSR performance benefits, and interoperability with non-React code. Enabling `cssVariables: true` in `createTheme` tells MUI to serialize palette, spacing, and other tokens to `:root` CSS variables. A best practice is to enable CSS variables when you need runtime theme switching without re-rendering the React tree, but be aware that the variable naming conventions differ between MUI v5 (experimental) and v6 (stable).

**Code Example**:
```javascript
createTheme({ cssVariables: true })
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q21"></a>
### Q21: How do you handle form validation with MUI?

**Difficulty**: Intermediate

**Strategy**: Form validation is a must-know because nearly every application handles user input, and MUI's TextField integrates cleanly with validation libraries through its `error` and `helperText` props. React Hook Form is the most popular pairing because its `register` and `Controller` API connect directly to MUI's controlled input pattern with minimal boilerplate. A common pitfall is mixing controlled and uncontrolled patterns in the same form -- choose one approach consistently and let the validation library own the state management.

**Code Example**:
```javascript
<TextField error={!!errors.email} helperText={errors.email?.message} />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q22"></a>
### Q22: What is the Typography component?

**Difficulty**: Beginner

**Strategy**: Typography is one of the most frequently used MUI components because it enforces a consistent type scale across the application through theme-defined variants (h1 through h6, subtitle, body, caption, overline). Each variant maps to a default HTML element but can be overridden via the `component` prop for semantic correctness. A common mistake is using `variant` and manually setting `fontSize` or `fontWeight` at the same time -- instead, customize the variant in the theme to keep the type system single-source.

**Code Example**:
```javascript
<Typography variant="h4">Title</Typography>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q23"></a>
### Q23: What is the Grid system in MUI?

**Difficulty**: Beginner

**Strategy**: MUI's Grid system is the go-to layout tool for building responsive page structures using a 12-column flexbox model with breakpoint-aware column spans. It supports both `container` and `item` roles, with spacing, direction, and justification controls. A common pitfall is forgetting that the Grid uses negative margins for spacing, which can cause unexpected overflow -- use the `spacing` prop consistently and wrap Grid containers in a parent with `overflow: hidden` when needed.

**Code Example**:
```javascript
<Grid container><Grid item xs={6}></Grid></Grid>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q24"></a>
### Q24: What is the Box component?

**Difficulty**: Beginner

**Strategy**: Box is the most versatile utility component in MUI, acting as a polymorphic wrapper that accepts all style system props (margin, padding, colors, flexbox, grid) via the `sx` prop. It renders a `<div>` by default but can be changed to any HTML element or React component using the `component` prop. Avoid overusing Box as a replacement for semantic HTML elements -- use it for layout utility while still choosing meaningful tags like `<section>` or `<nav>` when appropriate.

**Code Example**:
```javascript
<Box m={2} bg='primary.main' />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q25"></a>
### Q25: What is the Stack component?

**Difficulty**: Beginner

**Strategy**: Stack simplifies one-directional layout (vertical or horizontal) by managing spacing between children automatically, eliminating the need for manual margin on each child. It is ideal for form fields, button groups, and card content where consistent spacing is needed. Remember that Stack applies margin to all children except the last -- if you need a two-dimensional layout with both rows and columns, use Grid instead of nested Stacks.

**Code Example**:
```javascript
<Stack spacing={2}>...</Stack>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q26"></a>
### Q26: How do you override theme defaults?

**Difficulty**: Intermediate

**Strategy**: Theme overrides allow teams to align MUI's default look with a brand design system without modifying every component instance. The `components` key in `createTheme` supports `styleOverrides`, `defaultProps`, and `variants`, giving fine-grained control over each component's appearance and behavior. A best practice is to centralize all overrides in a single theme file so that designers and developers can audit the design system in one place rather than hunting for scattered inline styles.

**Code Example**:
```javascript
createTheme({ components: { MuiButton: ... } })
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q27"></a>
### Q27: What is the `sx` prop performance cost?

**Difficulty**: Advanced

**Strategy**: Understanding `sx` performance trade-offs is important for interviews because it shows you think critically about when convenience outweighs efficiency. The `sx` prop parses style objects at runtime through MUI's style engine, generating CSS-in-JS on every render, which adds a small but measurable overhead compared to `styled()` components that are parsed once at definition time. A common pitfall is using `sx` heavily inside list items or virtualized rows where hundreds of instances amplify the per-instance cost -- switch to `styled()` for those hot paths.

**Code Example**:
```javascript
// Use styled() for high perf lists
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q28"></a>
### Q28: How do you use Icons in MUI?

**Difficulty**: Beginner

**Strategy**: MUI provides over 2,000 Material Design icons as React SVG components via `@mui/icons-material`, ensuring consistent iconography that matches the rest of the design system. Icons support `fontSize`, `color`, and `sx` props just like other MUI components. A common mistake is importing icons from the top-level barrel export, which can bloat your bundle -- always import individual icon components directly to ensure tree-shaking works correctly.

**Code Example**:
```javascript
<DeleteIcon />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q29"></a>
### Q29: What is the Typography variants?

**Difficulty**: Beginner

**Strategy**: Typography variants provide a centralized type scale (h1-h6, subtitle1-2, body1-2, button, caption, overline) that ensures consistent font sizes, weights, and line heights across the application. Custom variants can be added to the theme, and each variant can optionally map to a default HTML element. Avoid overriding individual Typography instances with inline font styles -- instead, define or extend variants in the theme so the type system stays single-source and easy to update globally.

**Code Example**:
```javascript
<Typography variant='h1'>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q30"></a>
### Q30: How do you handle Date Pickers?

**Difficulty**: Intermediate

**Strategy**: MUI's Date Pickers (`@mui/x-date-pickers`) handle complex calendar UI, localization, and keyboard navigation that would be error-prone to build from scratch. They require a date adapter library (dayjs, date-fns, or moment) to manage date operations. A common pitfall is forgetting to wrap the application with `LocalizationProvider` and pass the appropriate adapter -- without it, the picker will throw a runtime error.

**Code Example**:
```javascript
<DatePicker />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q31"></a>
### Q31: What is the DataGrid component?

**Difficulty**: Advanced

**Strategy**: The DataGrid is MUI's enterprise-grade table component that handles sorting, filtering, pagination, and inline editing out of the box, making it essential for data-heavy admin dashboards. It comes in free (MIT) and Pro (commercial) tiers, with the Pro version adding features like row grouping and Excel export. A key performance consideration is to use server-side pagination for large datasets rather than loading thousands of rows into the browser at once.

**Code Example**:
```javascript
<DataGrid rows={rows} columns={cols} />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q32"></a>
### Q32: How do you make a responsive drawer?

**Difficulty**: Intermediate

**Strategy**: Responsive navigation drawers are a staple of dashboard layouts, and interviewers test this because it combines responsive design with MUI's Drawer component variants (`permanent`, `persistent`, `temporary`). The `temporary` variant renders an overlay drawer ideal for mobile, while `permanent` keeps it visible on desktop -- you switch between them using `useMediaQuery` or `Hidden`. A common pitfall is forgetting to close the temporary drawer on route change, leaving it open after navigation on mobile devices.

**Code Example**:
```javascript
<Drawer variant='temporary' />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q33"></a>
### Q33: What is `CssBaseline`?

**Difficulty**: Beginner

**Strategy**: CssBaseline normalizes browser defaults (reset CSS) and applies MUI's baseline typography, background color, and font smoothing so your app starts from a consistent foundation. It should be placed at the root of your component tree, typically inside the `ThemeProvider`. A common mistake is omitting it and wondering why spacing or font rendering differs across browsers -- always include it for cross-browser consistency.

**Code Example**:
```javascript
<CssBaseline />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q34"></a>
### Q34: How do you use custom fonts?

**Difficulty**: Intermediate

**Strategy**: Custom fonts are essential for brand consistency, and interviewers expect you to know how to integrate them with MUI's theme system so all components inherit the correct typeface. You load the font (via Google Fonts CDN, `@font-face`, or a local file) and set `typography.fontFamily` in `createTheme` to apply it globally across all Typography and component text. A common pitfall is setting the font only on `Typography` variants while forgetting that components like `Button`, `Chip`, and `Tab` also render text and need the font applied at the theme level.

**Code Example**:
```javascript
theme.typography.fontFamily = 'Roboto'
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q35"></a>
### Q35: What is the `makeStyles` (legacy)?

**Difficulty**: Intermediate

**Strategy**: `makeStyles` was the primary styling API in MUI v4, using JSS (JavaScript Style Sheets) to generate class names from JavaScript objects. It is still available in v5 via `@mui/styles` but is deprecated in favor of the `sx` prop and `styled()` API. Teams migrating from v4 should prioritize replacing `makeStyles` with `styled()` or `sx` rather than mixing old and new styling approaches, which creates confusion and increases bundle size.

**Code Example**:
```javascript
const useStyles = makeStyles(...) 
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q36"></a>
### Q36: How do you migrate from v4 to v5?

**Difficulty**: Advanced

**Strategy**: The v4-to-v5 migration involves renaming packages (`@material-ui` to `@mui`), replacing the JSS-based styling engine with emotion, and updating theme configuration. MUI provides an official codemod CLI that automates most of the mechanical changes, but manual review is still needed for custom theme extensions and complex style overrides. A best practice is to migrate incrementally using the `@mui/styles` compatibility package to keep existing `makeStyles` working while gradually adopting the new `sx` and `styled` APIs.

**Code Example**:
```javascript
npx @mui/codemod v5.0.0/preset-safe .
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q37"></a>
### Q37: What is Radix Primitives?

**Difficulty**: Beginner

**Strategy**: Radix Primitives are unstyled, accessible UI building blocks (Dialog, Popover, Tabs, Accordion, etc.) that handle complex interaction patterns like focus management and ARIA attributes without imposing any visual design. This matters because building these patterns from scratch is a major source of accessibility bugs, yet teams still want full control over styling. The key trade-off is that you must write all CSS yourself -- pair them with Tailwind, CSS Modules, or any styling solution your team prefers.

**Code Example**:
```javascript
import * as Dialog from '@radix-ui/react-dialog'
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q38"></a>
### Q38: How does Radix handle focus?

**Difficulty**: Intermediate

**Strategy**: Proper focus management is critical for keyboard and screen reader users, and Radix handles it automatically through its internal `FocusScope` utility. When a Dialog or Popover opens, focus moves into it and is trapped there until the component closes, at which point focus restores to the trigger element. A common pitfall when building custom overlays is forgetting to manage focus at all -- always rely on Radix primitives rather than implementing focus trapping yourself.

**Code Example**:
```javascript
// Built-in FocusScope
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q39"></a>
### Q39: What is `asChild` in Radix?

**Difficulty**: Intermediate

**Strategy**: The `asChild` prop uses Radix's `Slot` component internally to merge the Radix element's behavior (event handlers, ARIA attributes, data attributes) onto your custom child element instead of rendering a default DOM node. This is essential for avoiding nested interactive elements (like a button inside a button) when you want to use your own styled component as a trigger. Remember that `asChild` expects exactly one React element as a child -- passing multiple children or plain text will cause it to fall back to rendering its own element.

**Code Example**:
```javascript
<Trigger asChild><button>Open</button></Trigger>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q40"></a>
### Q40: How do you style Radix with CSS Modules?

**Difficulty**: Beginner

**Strategy**: Since Radix components are unstyled and accept standard `className` props, CSS Modules integrate seamlessly by passing the module's class names directly to each primitive part. This gives you scoped, locally hashed class names with zero runtime cost, which is a major advantage for performance-sensitive applications. A common mistake is trying to target Radix's internal data attributes without using the correct selector syntax -- use `&[data-state='open']` in your module CSS to style state changes.

**Code Example**:
```javascript
<Dialog.Content className={styles.content} />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q41"></a>
### Q41: How do you animate Radix components?

**Difficulty**: Intermediate

**Strategy**: Radix exposes `data-state` attributes (e.g., `open`, `closed`, `active`, `inactive`) on its components, which serve as CSS selectors for declarative animations. You can pair these with CSS transitions or `@keyframes` animations to create smooth open/close effects without any JavaScript animation library. A best practice is to keep animations short (150-300ms) and use `will-change` sparingly to avoid triggering unnecessary GPU layers.

**Code Example**:
```javascript
&[data-state='open'] { animation: fadeIn ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q42"></a>
### Q42: What is Radix Colors?

**Difficulty**: Beginner

**Strategy**: Radix Colors provides a curated set of accessible color scales designed to guarantee WCAG contrast compliance across light and dark themes. Each color scale includes 12 steps with consistent perceptual lightness, making it easy to build cohesive palettes without manual contrast testing. A best practice is to use the provided scales as-is for backgrounds, borders, and text rather than picking arbitrary hex values, as the scales are engineered to work together.

**Code Example**:
```javascript
import { blue, slate } from '@radix-ui/colors'
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q43"></a>
### Q43: How do you use Radix Icons?

**Difficulty**: Beginner

**Strategy**: Radix Icons is a set of crisp, 15x15 pixel icons designed to pair visually with Radix UI components, providing a consistent iconography system at a small file size. They are available as individual React SVG components that accept standard SVG props like `width`, `height`, and `color`. Since each icon is a separate import, tree-shaking works automatically -- avoid importing from a barrel file if your bundler does not support it efficiently.

**Code Example**:
```javascript
<SunIcon />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q44"></a>
### Q44: What is `Portal` in Radix?

**Difficulty**: Intermediate

**Strategy**: The Portal renders children into a DOM node outside the current component tree, which is essential for overlays like dialogs and tooltips to escape `overflow: hidden` and stacking context issues. Radix components like Dialog and Popover use portals internally by default, but you can customize the container element via the `container` prop. A common pitfall is portal content not inheriting CSS from parent components -- use global styles or CSS variables to ensure consistent theming across portal boundaries.

**Code Example**:
```javascript
<Dialog.Portal>...</Dialog.Portal>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q45"></a>
### Q45: Difference between Popover and Tooltip?

**Difficulty**: Intermediate

**Strategy**: Interviewers ask this to verify you understand when to use each pattern, since misuse leads to poor UX and accessibility violations. Tooltips display brief, non-interactive text on hover and disappear immediately when the cursor leaves, while Popovers can contain interactive content (forms, buttons, links) and require explicit dismissal. A common pitfall is putting interactive elements inside a Tooltip -- screen readers cannot access them, and mouse users struggle to reach the content before it disappears.

**Code Example**:
```javascript
// Popover traps focus
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q46"></a>
### Q46: What is Accordion in Radix?

**Difficulty**: Beginner

**Strategy**: The Radix Accordion provides a fully accessible expand/collapse pattern with proper ARIA attributes, keyboard navigation (arrow keys, Home, End), and support for both single and multiple item expansion. It is composed of `Root`, `Item`, `Trigger`, and `Content` parts that map directly to the WAI-ARIA accordion pattern. A best practice is to use `type="single"` when only one section should be open at a time and `type="multiple"` when users need to compare sections side by side.

**Code Example**:
```javascript
<Accordion.Root>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q47"></a>
### Q47: How do you handle form constraints in Radix?

**Difficulty**: Intermediate

**Strategy**: Radix provides form primitives like Label, Field, and FormMessage that handle proper `htmlFor`/`id` association, ARIA descriptions, and validation state display without requiring manual attribute wiring. These primitives ensure that error messages are announced by screen readers and visually associated with the correct input. A best practice is to pair Radix form primitives with a validation library like Zod or Conform to keep constraint logic declarative and type-safe.

**Code Example**:
```javascript
<Label>Name</Label>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q48"></a>
### Q48: What is the `Slot` utility?

**Difficulty**: Advanced

**Strategy**: `Slot` is the low-level primitive that powers Radix's `asChild` pattern, merging props (event handlers, refs, ARIA attributes) from a parent component onto its single child element instead of wrapping it in an extra DOM node. This is crucial for maintaining clean HTML semantics and avoiding accessibility violations like interactive elements nested inside other interactive elements. Be cautious when using Slot directly -- it expects exactly one React element child, and passing fragments or multiple elements will silently fail.

**Code Example**:
```javascript
import { Slot } from '@radix-ui/react-slot'
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q49"></a>
### Q49: How do you implement Toast?

**Difficulty**: Intermediate

**Strategy**: Radix Toast provides a viewport-based notification system where toasts are rendered into a dedicated viewport, ensuring they stack correctly and do not interfere with page layout. It includes built-in support for auto-dismiss timers, swipe-to-close gestures, and polite/assertive ARIA live regions for screen reader announcements. A common mistake is placing the Toast viewport inside a scrollable container -- always render it at the root level of your app so toasts remain visible regardless of scroll position.

**Code Example**:
```javascript
<Toast.Provider>...
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q50"></a>
### Q50: What is `VisuallyHidden`?

**Difficulty**: Beginner

**Strategy**: VisuallyHidden is a critical accessibility utility that interviewers look for because it lets you provide screen reader text without affecting visual layout, solving the common problem of icon-only buttons and decorative elements needing accessible labels. It applies CSS (`position: absolute; clip: rect(0,0,0,0)`) that hides content visually while keeping it in the accessibility tree. A common mistake is using `display: none` or `visibility: hidden` instead, which also removes the content from the accessibility tree and defeats the purpose.

**Code Example**:
```javascript
<VisuallyHidden>Label</VisuallyHidden>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q51"></a>
### Q51: How do you server render Radix?

**Difficulty**: Intermediate

**Strategy**: Radix primitives are designed to work with standard React SSR because they do not rely on browser-only APIs during initial render -- client-side effects (like focus trapping) only activate after hydration. This makes them compatible with frameworks like Next.js, Remix, and Astro without extra configuration. A common pitfall is components that read `window.matchMedia` or `document` during render -- defer those calls with `useEffect` or dynamic imports to avoid SSR errors.

**Code Example**:
```javascript
// Standard React SSR
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q52"></a>
### Q52: What is Shadcn UI?

**Difficulty**: Intermediate

**Strategy**: Shadcn UI is a collection of copy-paste components built on top of Radix UI primitives and styled with Tailwind CSS, offering the accessibility guarantees of Radix with a modern utility-first design. Unlike traditional libraries, it is not an npm dependency -- you install components as source files into your project and own the code entirely. This means you get full control over every component, but it also means you are responsible for keeping them updated when Radix or Tailwind releases breaking changes.

**Code Example**:
```javascript
npx shadcn-ui@latest add button
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q53"></a>
### Q53: How does Shadcn differ from MUI?

**Difficulty**: Intermediate

**Strategy**: This comparison tests whether you understand the fundamental architectural difference between component libraries and component collections, which directly impacts how teams maintain and upgrade their UI code. MUI is a traditional npm dependency -- you import components and rely on the package for updates, bug fixes, and breaking changes. Shadcn UI copies component source code directly into your project, giving you full ownership and customization freedom but transferring all maintenance responsibility to your team.

**Code Example**:
```javascript
// You edit the component files directly
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q54"></a>
### Q54: What is Headless UI?

**Difficulty**: Intermediate

**Strategy**: Headless UI, built by the Tailwind CSS team, provides unstyled, accessible components (Menu, Listbox, Combobox, Switch, Dialog, etc.) that integrate naturally with Tailwind's utility classes. It shares the same headless philosophy as Radix but offers fewer component primitives and tighter integration with the Tailwind ecosystem. When choosing between the two, consider that Radix has a wider range of primitives while Headless UI tends to have a simpler API surface -- pick based on your project's component needs and existing tooling.

**Code Example**:
```javascript
import { Menu } from '@headlessui/react'
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q55"></a>
### Q55: How do you create a dark mode switch in MUI?

**Difficulty**: Beginner

**Strategy**: A dark mode toggle is one of the most common user-facing features, and MUI supports it by toggling the theme's `palette.mode` between `'light'` and `'dark'`. You typically store the user's preference in React state (or localStorage for persistence) and recreate the theme when the mode changes. A best practice is to wrap theme creation in `useMemo` so that the theme object reference stays stable between renders, preventing unnecessary re-renders of the entire component tree.

**Code Example**:
```javascript
setMode(prev => prev === 'light' ? 'dark' : 'light')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q56"></a>
### Q56: What is `useTheme` hook?

**Difficulty**: Beginner

**Strategy**: `useTheme` returns the full theme object from the nearest `ThemeProvider`, giving components direct access to palette colors, spacing values, breakpoints, and any custom tokens you have defined. This is useful when you need theme values in JavaScript logic, such as computing dynamic styles or conditional rendering based on breakpoint values. Remember that `useTheme` will return the default theme if called outside a `ThemeProvider` -- always ensure your component tree is wrapped properly.

**Code Example**:
```javascript
const theme = useTheme();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q57"></a>
### Q57: How do you customize breakpoints?

**Difficulty**: Intermediate

**Strategy**: MUI's default breakpoints (xs, sm, md, lg, xl) can be overridden or extended in the theme to match your project's design tokens, ensuring that responsive behavior aligns with your actual layout needs rather than arbitrary defaults. You can rename them (e.g., `mobile`, `tablet`, `desktop`) or change their pixel values. A common pitfall is mixing custom breakpoint names with the default ones -- once you override `values`, all breakpoint references must use your custom keys consistently.

**Code Example**:
```javascript
breakpoints: { values: { mobile: 0, tablet: 640 } }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q58"></a>
### Q58: What is the `Container` component?

**Difficulty**: Beginner

**Strategy**: Container centers content horizontally and constrains its maximum width using the theme's breakpoints (`sm`, `md`, `lg`, `xl`), making it the standard wrapper for page-level content. It supports `fixed` (always at a breakpoint max-width) and `fluid` (grows with the viewport up to `maxWidth`) behaviors. A common mistake is nesting multiple Containers, which compounds horizontal padding -- use a single Container per page section and rely on Grid or Stack for inner layout.

**Code Example**:
```javascript
<Container maxWidth='lg'>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q59"></a>
### Q59: How do you use Skeleton loading?

**Difficulty**: Beginner

**Strategy**: Skeleton components provide a visual placeholder that mimics the shape of content being loaded, giving users immediate feedback that data is on its way rather than showing a blank screen. MUI's Skeleton supports `text`, `rectangular`, and `circular` variants with a pulse animation by default. A best practice is to match the skeleton's dimensions exactly to the expected content so there is no layout shift when the real data loads -- avoid generic placeholder sizes that cause the page to jump.

**Code Example**:
```javascript
<Skeleton variant='rectangular' />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q60"></a>
### Q60: What is the `Autocomplete` component?

**Difficulty**: Intermediate

**Strategy**: Autocomplete is a feature-rich combo box that handles filtering, grouping, async loading, multiple selection, and custom option rendering -- functionality that is complex and error-prone to build from scratch. It integrates seamlessly with TextField for the input and supports controlled/uncontrolled modes via `value`/`defaultValue`. A common pitfall is not debouncing `onInputChange` when fetching options from an API, which can flood the server with requests on every keystroke.

**Code Example**:
```javascript
<Autocomplete options={...} />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q61"></a>
### Q61: How do you handle virtualized lists in MUI?

**Difficulty**: Advanced

**Strategy**: List virtualization is an advanced performance topic that distinguishes senior candidates because rendering thousands of DOM nodes causes severe jank and memory pressure. MUI's DataGrid Pro supports virtualization natively, but for custom lists you pair MUI components with libraries like `react-window` or `@tanstack/react-virtual` to only render items visible in the viewport. A common pitfall is virtualizing lists with variable row heights without configuring the estimators correctly, which causes scroll position jumps and incorrect layout calculations.

**Code Example**:
```javascript
// Windowing for performance
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q62"></a>
### Q62: What is the `ClickAwayListener`?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
<ClickAwayListener onClickAway={...}>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q63"></a>
### Q63: How do you use `Backdrop`?

**Difficulty**: Beginner

**Strategy**:

**Code Example**:
```javascript
<Backdrop open={true} />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q64"></a>
### Q64: What is `SpeedDial`?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
<SpeedDial icon={<SpeedDialIcon />} />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q65"></a>
### Q65: How do you customize scrollbars in MUI?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
styleOverrides: { body: { '&::-webkit-scrollbar': ... } }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q66"></a>
### Q66: What is `Collapse` transition?

**Difficulty**: Beginner

**Strategy**:

**Code Example**:
```javascript
<Collapse in={open}>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q67"></a>
### Q67: How do you use `Zoom` transition?

**Difficulty**: Beginner

**Strategy**:

**Code Example**:
```javascript
<Zoom in={true}>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q68"></a>
### Q68: What is `Grow` transition?

**Difficulty**: Beginner

**Strategy**:

**Code Example**:
```javascript
<Grow in={true}>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q69"></a>
### Q69: What is `Slide` transition?

**Difficulty**: Beginner

**Strategy**:

**Code Example**:
```javascript
<Slide direction='up' in={true}>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q70"></a>
### Q70: How do you use `Fade` transition?

**Difficulty**: Beginner

**Strategy**:

**Code Example**:
```javascript
<Fade in={true}>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q71"></a>
### Q71: What is `GlobalStyles`?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
<GlobalStyles styles={{ h1: { color: 'red' } }} />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q72"></a>
### Q72: How do you theme variants?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
components: { MuiButton: { variants: [...] } }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q73"></a>
### Q73: What is `shouldForwardProp`?

**Difficulty**: Advanced

**Strategy**:

**Code Example**:
```javascript
styled('div', { shouldForwardProp: (p) => p !== 'active' })
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q74"></a>
### Q74: How do you use `alpha` utility?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
bgcolor: alpha(theme.palette.primary.main, 0.5)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q75"></a>
### Q75: What is `darken`/`lighten`?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
color: darken('red', 0.2)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q76"></a>
### Q76: How do you use `useScrollTrigger`?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
const trigger = useScrollTrigger();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q77"></a>
### Q77: What is `FocusTrap`?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
<FocusTrap open>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q78"></a>
### Q78: How do you use `NoSsr`?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
<NoSsr>Client Only</NoSsr>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q79"></a>
### Q79: What is `TextareaAutosize`?

**Difficulty**: Beginner

**Strategy**:

**Code Example**:
```javascript
<TextareaAutosize />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q80"></a>
### Q80: How do you use `Rating`?

**Difficulty**: Beginner

**Strategy**:

**Code Example**:
```javascript
<Rating value={4} />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q81"></a>
### Q81: What is `Timeline`?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
<Timeline>...</Timeline>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q82"></a>
### Q82: How do you use `TreeView`?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
<TreeView>...</TreeView>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q83"></a>
### Q83: What is `Masonry`?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
<Masonry>...</Masonry>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q84"></a>
### Q84: How do you use `Snackbar`?

**Difficulty**: Beginner

**Strategy**:

**Code Example**:
```javascript
<Snackbar message='Saved' />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q85"></a>
### Q85: What is `Alert`?

**Difficulty**: Beginner

**Strategy**:

**Code Example**:
```javascript
<Alert severity='error'>Error</Alert>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q86"></a>
### Q86: How do you customize shadow?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
theme.shadows[1] = '0 2px 4px black'
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q87"></a>
### Q87: What is `Paper`?

**Difficulty**: Beginner

**Strategy**:

**Code Example**:
```javascript
<Paper elevation={3} />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q88"></a>
### Q88: How do you use `Card`?

**Difficulty**: Beginner

**Strategy**:

**Code Example**:
```javascript
<Card><CardContent>...</CardContent></Card>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q89"></a>
### Q89: What is `Divider`?

**Difficulty**: Beginner

**Strategy**:

**Code Example**:
```javascript
<Divider />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q90"></a>
### Q90: How do you use `Chip`?

**Difficulty**: Beginner

**Strategy**:

**Code Example**:
```javascript
<Chip label='Tag' onDelete={...} />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q91"></a>
### Q91: What is `Badge`?

**Difficulty**: Beginner

**Strategy**:

**Code Example**:
```javascript
<Badge badgeContent={4} color='primary'>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q92"></a>
### Q92: How do you use `Avatar`?

**Difficulty**: Beginner

**Strategy**:

**Code Example**:
```javascript
<Avatar src='/img.jpg' />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q93"></a>
### Q93: What is `LinearProgress`?

**Difficulty**: Beginner

**Strategy**:

**Code Example**:
```javascript
<LinearProgress />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q94"></a>
### Q94: What is `CircularProgress`?

**Difficulty**: Beginner

**Strategy**:

**Code Example**:
```javascript
<CircularProgress />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q95"></a>
### Q95: How do you use `Tabs`?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
<Tabs><Tab label='One' /></Tabs>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q96"></a>
### Q96: What is `BottomNavigation`?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
<BottomNavigation>...</BottomNavigation>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q97"></a>
### Q97: How do you use `Breadcrumbs`?

**Difficulty**: Beginner

**Strategy**:

**Code Example**:
```javascript
<Breadcrumbs>...</Breadcrumbs>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q98"></a>
### Q98: What is `Link` component?

**Difficulty**: Beginner

**Strategy**:

**Code Example**:
```javascript
<Link href='#'>Link</Link>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q99"></a>
### Q99: How do you use `Stepper`?

**Difficulty**: Intermediate

**Strategy**:

**Code Example**:
```javascript
<Stepper activeStep={1}>...</Stepper>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div><a id="q100"></a>

### Q100: How does Radix UI handle accessibility?

**Difficulty**: Intermediate

**Strategy**: Radix UI primitives manage ARIA attributes, focus management, and keyboard navigation out of the box. They follow the WAI-ARIA authoring practices, allowing developers to focus on styling without worrying about complex accessibility logic.

**Code Example**: 
```javascript
// Accessible Dialog component
<Dialog.Root>
  <Dialog.Trigger>Open</Dialog.Trigger>
  <Dialog.Portal>
    <Dialog.Content>
      <Dialog.Title>Edit profile</Dialog.Title>
      <Dialog.Description>Make changes to your profile.</Dialog.Description>
      <Dialog.Close>Save</Dialog.Close>
    </Dialog.Content>
  </Dialog.Portal>
</Dialog.Root>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

