# Material UI & Radix UI Interview Questions

## Table of Contents

1. [How do you customize the Material UI theme?](#q1-how-do-you-customize-the-material-ui-theme) <span class="beginner">Beginner</span>
2. [How do you use the `sx` prop in Material UI?](#q2-how-do-you-use-the-sx-prop-in-material-ui) <span class="intermediate">Intermediate</span>
3. [Difference between Controlled and Uncontrolled components in Radix UI?](#q3-difference-between-controlled-and-uncontrolled-components-in-radix-ui) <span class="intermediate">Intermediate</span>
4. [How do you optimize Material UI bundle size?](#q4-how-do-you-optimize-material-ui-bundle-size) <span class="advanced">Advanced</span>
5. [How do you implement a Dialog in Radix UI?](#q5-how-do-you-implement-a-dialog-in-radix-ui) <span class="beginner">Beginner</span>
6. [How do you handle responsive styles in Material UI?](#q6-how-do-you-handle-responsive-styles-in-material-ui) <span class="intermediate">Intermediate</span>
7. [How do you style Radix UI components with Tailwind?](#q7-how-do-you-style-radix-ui-components-with-tailwind) <span class="intermediate">Intermediate</span>
8. [How do you create a custom styled component in MUI?](#q8-how-do-you-create-a-custom-styled-component-in-mui) <span class="intermediate">Intermediate</span>
9. [How do you handle accessibility (a11y) in Radix UI?](#q9-how-do-you-handle-accessibility-a11y-in-radix-ui) <span class="beginner">Beginner</span>
10. [How do you implement Dark Mode in MUI?](#q10-how-do-you-implement-dark-mode-in-mui) <span class="intermediate">Intermediate</span>
11. [What is the `asChild` prop in Radix UI?](#q11-what-is-the-aschild-prop-in-radix-ui) <span class="intermediate">Intermediate</span>
12. [How do you override default MUI component styles globally?](#q12-how-do-you-override-default-mui-component-styles-globally) <span class="advanced">Advanced</span>
13. [What is the Box component in MUI?](#q13-what-is-the-box-component-in-mui) <span class="beginner">Beginner</span>
14. [How do you use useMediaQuery in MUI?](#q14-how-do-you-use-usemediaquery-in-mui) <span class="intermediate">Intermediate</span>
15. [What is the difference between Radix UI and Headless UI?](#q15-what-is-the-difference-between-radix-ui-and-headless-ui) <span class="intermediate">Intermediate</span>
16. [How do you handle z-index issues in MUI?](#q16-how-do-you-handle-z-index-issues-in-mui) <span class="intermediate">Intermediate</span>
17. [How do you make a Radix UI Dialog accessible?](#q17-how-do-you-make-a-radix-ui-dialog-accessible) <span class="beginner">Beginner</span>
18. [How do you create a layout with MUI Grid?](#q18-how-do-you-create-a-layout-with-mui-grid) <span class="beginner">Beginner</span>
19. [What is the Portal component used for?](#q19-what-is-the-portal-component-used-for) <span class="intermediate">Intermediate</span>
20. [How do you enable CSS variables in MUI?](#q20-how-do-you-enable-css-variables-in-mui) <span class="advanced">Advanced</span>
21. [How do you handle form validation with MUI?](#q21-how-do-you-handle-form-validation-with-mui) <span class="intermediate">Intermediate</span>
22. [What is the Typography component?](#q22-what-is-the-typography-component) <span class="beginner">Beginner</span>
23. [What is the Grid system in MUI?](#q23-what-is-the-grid-system-in-mui) <span class="beginner">Beginner</span>
24. [What is the Box component?](#q24-what-is-the-box-component) <span class="beginner">Beginner</span>
25. [What is the Stack component?](#q25-what-is-the-stack-component) <span class="beginner">Beginner</span>
26. [How do you override theme defaults?](#q26-how-do-you-override-theme-defaults) <span class="intermediate">Intermediate</span>
27. [What is the `sx` prop performance cost?](#q27-what-is-the-sx-prop-performance-cost) <span class="advanced">Advanced</span>
28. [How do you use Icons in MUI?](#q28-how-do-you-use-icons-in-mui) <span class="beginner">Beginner</span>
29. [What is the Typography variants?](#q29-what-is-the-typography-variants) <span class="beginner">Beginner</span>
30. [How do you handle Date Pickers?](#q30-how-do-you-handle-date-pickers) <span class="intermediate">Intermediate</span>
31. [What is the DataGrid component?](#q31-what-is-the-datagrid-component) <span class="advanced">Advanced</span>
32. [How do you make a responsive drawer?](#q32-how-do-you-make-a-responsive-drawer) <span class="intermediate">Intermediate</span>
33. [What is `CssBaseline`?](#q33-what-is-cssbaseline) <span class="beginner">Beginner</span>
34. [How do you use custom fonts?](#q34-how-do-you-use-custom-fonts) <span class="intermediate">Intermediate</span>
35. [What is the `makeStyles` (legacy)?](#q35-what-is-the-makestyles-legacy) <span class="intermediate">Intermediate</span>
36. [How do you migrate from v4 to v5?](#q36-how-do-you-migrate-from-v4-to-v5) <span class="advanced">Advanced</span>
37. [What is Radix Primitives?](#q37-what-is-radix-primitives) <span class="beginner">Beginner</span>
38. [How does Radix handle focus?](#q38-how-does-radix-handle-focus) <span class="intermediate">Intermediate</span>
39. [What is `asChild` in Radix?](#q39-what-is-aschild-in-radix) <span class="intermediate">Intermediate</span>
40. [How do you style Radix with CSS Modules?](#q40-how-do-you-style-radix-with-css-modules) <span class="beginner">Beginner</span>
41. [How do you animate Radix components?](#q41-how-do-you-animate-radix-components) <span class="intermediate">Intermediate</span>
42. [What is Radix Colors?](#q42-what-is-radix-colors) <span class="beginner">Beginner</span>
43. [How do you use Radix Icons?](#q43-how-do-you-use-radix-icons) <span class="beginner">Beginner</span>
44. [What is `Portal` in Radix?](#q44-what-is-portal-in-radix) <span class="intermediate">Intermediate</span>
45. [Difference between Popover and Tooltip?](#q45-difference-between-popover-and-tooltip) <span class="intermediate">Intermediate</span>
46. [What is Accordion in Radix?](#q46-what-is-accordion-in-radix) <span class="beginner">Beginner</span>
47. [How do you handle form constraints in Radix?](#q47-how-do-you-handle-form-constraints-in-radix) <span class="intermediate">Intermediate</span>
48. [What is the `Slot` utility?](#q48-what-is-the-slot-utility) <span class="advanced">Advanced</span>
49. [How do you implement Toast?](#q49-how-do-you-implement-toast) <span class="intermediate">Intermediate</span>
50. [What is `VisuallyHidden`?](#q50-what-is-visuallyhidden) <span class="beginner">Beginner</span>
51. [How do you server render Radix?](#q51-how-do-you-server-render-radix) <span class="intermediate">Intermediate</span>
52. [What is Shadcn UI?](#q52-what-is-shadcn-ui) <span class="intermediate">Intermediate</span>
53. [How does Shadcn differ from MUI?](#q53-how-does-shadcn-differ-from-mui) <span class="intermediate">Intermediate</span>
54. [What is Headless UI?](#q54-what-is-headless-ui) <span class="intermediate">Intermediate</span>
55. [How do you create a dark mode switch in MUI?](#q55-how-do-you-create-a-dark-mode-switch-in-mui) <span class="beginner">Beginner</span>
56. [What is `useTheme` hook?](#q56-what-is-usetheme-hook) <span class="beginner">Beginner</span>
57. [How do you customize breakpoints?](#q57-how-do-you-customize-breakpoints) <span class="intermediate">Intermediate</span>
58. [What is the `Container` component?](#q58-what-is-the-container-component) <span class="beginner">Beginner</span>
59. [How do you use Skeleton loading?](#q59-how-do-you-use-skeleton-loading) <span class="beginner">Beginner</span>
60. [What is the `Autocomplete` component?](#q60-what-is-the-autocomplete-component) <span class="intermediate">Intermediate</span>
61. [How do you handle virtualized lists in MUI?](#q61-how-do-you-handle-virtualized-lists-in-mui) <span class="advanced">Advanced</span>
62. [What is the `ClickAwayListener`?](#q62-what-is-the-clickawaylistener) <span class="intermediate">Intermediate</span>
63. [How do you use `Backdrop`?](#q63-how-do-you-use-backdrop) <span class="beginner">Beginner</span>
64. [What is `SpeedDial`?](#q64-what-is-speeddial) <span class="intermediate">Intermediate</span>
65. [How do you customize scrollbars in MUI?](#q65-how-do-you-customize-scrollbars-in-mui) <span class="intermediate">Intermediate</span>
66. [What is `Collapse` transition?](#q66-what-is-collapse-transition) <span class="beginner">Beginner</span>
67. [How do you use `Zoom` transition?](#q67-how-do-you-use-zoom-transition) <span class="beginner">Beginner</span>
68. [What is `Grow` transition?](#q68-what-is-grow-transition) <span class="beginner">Beginner</span>
69. [What is `Slide` transition?](#q69-what-is-slide-transition) <span class="beginner">Beginner</span>
70. [How do you use `Fade` transition?](#q70-how-do-you-use-fade-transition) <span class="beginner">Beginner</span>
71. [What is `GlobalStyles`?](#q71-what-is-globalstyles) <span class="intermediate">Intermediate</span>
72. [How do you theme variants?](#q72-how-do-you-theme-variants) <span class="intermediate">Intermediate</span>
73. [What is `shouldForwardProp`?](#q73-what-is-shouldforwardprop) <span class="advanced">Advanced</span>
74. [How do you use `alpha` utility?](#q74-how-do-you-use-alpha-utility) <span class="intermediate">Intermediate</span>
75. [What is `darken`/`lighten`?](#q75-what-is-darkenlighten) <span class="intermediate">Intermediate</span>
76. [How do you use `useScrollTrigger`?](#q76-how-do-you-use-usescrolltrigger) <span class="intermediate">Intermediate</span>
77. [What is `FocusTrap`?](#q77-what-is-focustrap) <span class="intermediate">Intermediate</span>
78. [How do you use `NoSsr`?](#q78-how-do-you-use-nossr) <span class="intermediate">Intermediate</span>
79. [What is `TextareaAutosize`?](#q79-what-is-textareaautosize) <span class="beginner">Beginner</span>
80. [How do you use `Rating`?](#q80-how-do-you-use-rating) <span class="beginner">Beginner</span>
81. [What is `Timeline`?](#q81-what-is-timeline) <span class="intermediate">Intermediate</span>
82. [How do you use `TreeView`?](#q82-how-do-you-use-treeview) <span class="intermediate">Intermediate</span>
83. [What is `Masonry`?](#q83-what-is-masonry) <span class="intermediate">Intermediate</span>
84. [How do you use `Snackbar`?](#q84-how-do-you-use-snackbar) <span class="beginner">Beginner</span>
85. [What is `Alert`?](#q85-what-is-alert) <span class="beginner">Beginner</span>
86. [How do you customize shadow?](#q86-how-do-you-customize-shadow) <span class="intermediate">Intermediate</span>
87. [What is `Paper`?](#q87-what-is-paper) <span class="beginner">Beginner</span>
88. [How do you use `Card`?](#q88-how-do-you-use-card) <span class="beginner">Beginner</span>
89. [What is `Divider`?](#q89-what-is-divider) <span class="beginner">Beginner</span>
90. [How do you use `Chip`?](#q90-how-do-you-use-chip) <span class="beginner">Beginner</span>
91. [What is `Badge`?](#q91-what-is-badge) <span class="beginner">Beginner</span>
92. [How do you use `Avatar`?](#q92-how-do-you-use-avatar) <span class="beginner">Beginner</span>
93. [What is `LinearProgress`?](#q93-what-is-linearprogress) <span class="beginner">Beginner</span>
94. [What is `CircularProgress`?](#q94-what-is-circularprogress) <span class="beginner">Beginner</span>
95. [How do you use `Tabs`?](#q95-how-do-you-use-tabs) <span class="intermediate">Intermediate</span>
96. [What is `BottomNavigation`?](#q96-what-is-bottomnavigation) <span class="intermediate">Intermediate</span>
97. [How do you use `Breadcrumbs`?](#q97-how-do-you-use-breadcrumbs) <span class="beginner">Beginner</span>
98. [What is `Link` component?](#q98-what-is-link-component) <span class="beginner">Beginner</span>
99. [How do you use `Stepper`?](#q99-how-do-you-use-stepper) <span class="intermediate">Intermediate</span>

---

### Q1: How do you customize the Material UI theme?

**Difficulty**: Beginner

**Strategy**:
Use `createTheme` and `ThemeProvider`.

**Code Example**:
```javascript
const theme = createTheme({ palette: { primary: { main: '#ff4400' } } });
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q2: How do you use the `sx` prop in Material UI?

**Difficulty**: Intermediate

**Strategy**:
The `sx` prop allows defining system overrides directly on components.

**Code Example**:
```javascript
<Button sx={{ margin: 2, color: 'primary.main' }}>Click Me</Button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q3: Difference between Controlled and Uncontrolled components in Radix UI?

**Difficulty**: Intermediate

**Strategy**:
Radix primitives support both. Controlled uses `value`/`onValueChange`. Uncontrolled uses `defaultValue`.

**Code Example**:
```javascript
<Accordion value={val} onValueChange={setVal} /> vs <Accordion defaultValue="1" />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q4: How do you optimize Material UI bundle size?

**Difficulty**: Advanced

**Strategy**:
Use path imports instead of top-level imports to aid tree-shaking.

**Code Example**:
```javascript
import Button from '@mui/material/Button'; // Better than import { Button }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q5: How do you implement a Dialog in Radix UI?

**Difficulty**: Beginner

**Strategy**:
Radix provides `Dialog.Root`, `Dialog.Trigger`, `Dialog.Portal`, `Dialog.Overlay`, `Dialog.Content`.

**Code Example**:
```javascript
<Dialog.Root><Dialog.Trigger>Open</Dialog.Trigger><Dialog.Content>...</Dialog.Content></Dialog.Root>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q6: How do you handle responsive styles in Material UI?

**Difficulty**: Intermediate

**Strategy**:
Use the array syntax in `sx` prop or `useMediaQuery` hook.

**Code Example**:
```javascript
<Box sx={{ width: [100, 200, 300] }}>Responsiveness</Box>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q7: How do you style Radix UI components with Tailwind?

**Difficulty**: Intermediate

**Strategy**:
Radix components are unstyled. Just add `className` with Tailwind classes.

**Code Example**:
```javascript
<Dialog.Content className="fixed bg-white p-4 rounded">
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q8: How do you create a custom styled component in MUI?

**Difficulty**: Intermediate

**Strategy**:
Use the `styled` utility.

**Code Example**:
```javascript
const MyButton = styled(Button)({ color: 'red' });
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q9: How do you handle accessibility (a11y) in Radix UI?

**Difficulty**: Beginner

**Strategy**:
It's built-in. Radix handles aria attributes and keyboard navigation automatically.

**Code Example**:
```javascript
// No extra code needed for basic a11y
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q10: How do you implement Dark Mode in MUI?

**Difficulty**: Intermediate

**Strategy**:
Pass a mode ('light' or 'dark') to the palette in `createTheme`.

**Code Example**:
```javascript
const theme = createTheme({ palette: { mode: 'dark' } });
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q11: What is the `asChild` prop in Radix UI?

**Difficulty**: Intermediate

**Strategy**:
It allows a Radix component to pass its functionality to its child element instead of rendering its own DOM node.

**Code Example**:
```javascript
<Dialog.Trigger asChild><button>Open</button></Dialog.Trigger>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q12: How do you override default MUI component styles globally?

**Difficulty**: Advanced

**Strategy**:
Use the `components` key in `createTheme`.

**Code Example**:
```javascript
createTheme({ components: { MuiButton: { styleOverrides: { root: { fontSize: '1rem' } } } } })
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q13: What is the Box component in MUI?

**Difficulty**: Beginner

**Strategy**:
A wrapper component that provides access to system props (margin, padding, colors, flexbox).

**Code Example**:
```javascript
<Box m={2} p={1} bgcolor="grey.100">Content</Box>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q14: How do you use useMediaQuery in MUI?

**Difficulty**: Intermediate

**Strategy**:
A hook to perform media queries in JS.

**Code Example**:
```javascript
const matches = useMediaQuery('(min-width:600px)');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q15: What is the difference between Radix UI and Headless UI?

**Difficulty**: Intermediate

**Strategy**:
Both are headless. Radix offers more complex primitives (like Dialog, Popover, Select) with robust a11y. Headless UI is by Tailwind Labs.

**Code Example**:
```javascript
// Choice depends on ecosystem preference
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q16: How do you handle z-index issues in MUI?

**Difficulty**: Intermediate

**Strategy**:
Use the `zIndex` value from the theme.

**Code Example**:
```javascript
sx={{ zIndex: 'tooltip' }}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q17: How do you make a Radix UI Dialog accessible?

**Difficulty**: Beginner

**Strategy**:
Radix handles focus trapping and screen reader announcements automatically.

**Code Example**:
```javascript
// Just use the primitives correctly
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q18: How do you create a layout with MUI Grid?

**Difficulty**: Beginner

**Strategy**:
Use `Grid` container and `Grid` items with `xs`, `md`, `lg` props.

**Code Example**:
```javascript
<Grid container><Grid item xs={6}>Left</Grid><Grid item xs={6}>Right</Grid></Grid>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q19: What is the Portal component used for?

**Difficulty**: Intermediate

**Strategy**:
To render children into a DOM node that exists outside the DOM hierarchy of the parent component (e.g., for Modals).

**Code Example**:
```javascript
<Portal><div>I am outside root</div></Portal>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q20: How do you enable CSS variables in MUI?

**Difficulty**: Advanced

**Strategy**:
Set `cssVariables: true` in the theme configuration (MUI v6+ or experimental in v5).

**Code Example**:
```javascript
createTheme({ cssVariables: true })
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q21: How do you handle form validation with MUI?

**Difficulty**: Intermediate

**Strategy**:
MUI integrates well with libraries like React Hook Form. Pass `error` and `helperText` props.

**Code Example**:
```javascript
<TextField error={!!errors.email} helperText={errors.email?.message} />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q22: What is the Typography component?

**Difficulty**: Beginner

**Strategy**:
Used to present design and content clearly and efficiently. It maps to HTML tags like h1, p, span.

**Code Example**:
```javascript
<Typography variant="h4">Title</Typography>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q23: What is the Grid system in MUI?

**Difficulty**: Beginner

**Strategy**:
12-column responsive layout.

**Code Example**:
```javascript
<Grid container><Grid item xs={6}></Grid></Grid>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q24: What is the Box component?

**Difficulty**: Beginner

**Strategy**:
Wrapper for CSS utilities.

**Code Example**:
```javascript
<Box m={2} bg='primary.main' />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q25: What is the Stack component?

**Difficulty**: Beginner

**Strategy**:
Flexbox layout for 1D lists.

**Code Example**:
```javascript
<Stack spacing={2}>...</Stack>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q26: How do you override theme defaults?

**Difficulty**: Intermediate

**Strategy**:
Using `createTheme`.

**Code Example**:
```javascript
createTheme({ components: { MuiButton: ... } })
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q27: What is the `sx` prop performance cost?

**Difficulty**: Advanced

**Strategy**:
Slightly slower than styled-components due to runtime calculation.

**Code Example**:
```javascript
// Use styled() for high perf lists
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q28: How do you use Icons in MUI?

**Difficulty**: Beginner

**Strategy**:
Import from `@mui/icons-material`.

**Code Example**:
```javascript
<DeleteIcon />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q29: What is the Typography variants?

**Difficulty**: Beginner

**Strategy**:
h1-h6, subtitle, body, caption.

**Code Example**:
```javascript
<Typography variant='h1'>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q30: How do you handle Date Pickers?

**Difficulty**: Intermediate

**Strategy**:
Use `@mui/x-date-pickers`.

**Code Example**:
```javascript
<DatePicker />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q31: What is the DataGrid component?

**Difficulty**: Advanced

**Strategy**:
Powerful table for large datasets.

**Code Example**:
```javascript
<DataGrid rows={rows} columns={cols} />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q32: How do you make a responsive drawer?

**Difficulty**: Intermediate

**Strategy**:
Use `Drawer` with `hidden` props or `useMediaQuery`.

**Code Example**:
```javascript
<Drawer variant='temporary' />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q33: What is `CssBaseline`?

**Difficulty**: Beginner

**Strategy**:
Normalizes CSS across browsers.

**Code Example**:
```javascript
<CssBaseline />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q34: How do you use custom fonts?

**Difficulty**: Intermediate

**Strategy**:
Load font and set `typography.fontFamily` in theme.

**Code Example**:
```javascript
theme.typography.fontFamily = 'Roboto'
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q35: What is the `makeStyles` (legacy)?

**Difficulty**: Intermediate

**Strategy**:
JSS hook in v4. Deprecated in v5.

**Code Example**:
```javascript
const useStyles = makeStyles(...) 
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q36: How do you migrate from v4 to v5?

**Difficulty**: Advanced

**Strategy**:
Run codemods, switch to emotion.

**Code Example**:
```javascript
npx @mui/codemod v5.0.0/preset-safe .
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q37: What is Radix Primitives?

**Difficulty**: Beginner

**Strategy**:
Unstyled, accessible UI components.

**Code Example**:
```javascript
import * as Dialog from '@radix-ui/react-dialog'
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q38: How does Radix handle focus?

**Difficulty**: Intermediate

**Strategy**:
Automatically traps focus in modals.

**Code Example**:
```javascript
// Built-in FocusScope
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q39: What is `asChild` in Radix?

**Difficulty**: Intermediate

**Strategy**:
Merges props onto child element.

**Code Example**:
```javascript
<Trigger asChild><button>Open</button></Trigger>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q40: How do you style Radix with CSS Modules?

**Difficulty**: Beginner

**Strategy**:
Pass `className`.

**Code Example**:
```javascript
<Dialog.Content className={styles.content} />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q41: How do you animate Radix components?

**Difficulty**: Intermediate

**Strategy**:
Use CSS keyframes on `data-state` attribute.

**Code Example**:
```javascript
&[data-state='open'] { animation: fadeIn ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q42: What is Radix Colors?

**Difficulty**: Beginner

**Strategy**:
Color system for accessible contrast.

**Code Example**:
```javascript
import { blue, slate } from '@radix-ui/colors'
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q43: How do you use Radix Icons?

**Difficulty**: Beginner

**Strategy**:
SVG icons.

**Code Example**:
```javascript
<SunIcon />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q44: What is `Portal` in Radix?

**Difficulty**: Intermediate

**Strategy**:
Renders content into body.

**Code Example**:
```javascript
<Dialog.Portal>...</Dialog.Portal>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q45: Difference between Popover and Tooltip?

**Difficulty**: Intermediate

**Strategy**:
Tooltip is for hover info, Popover is for interactive content.

**Code Example**:
```javascript
// Popover traps focus
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q46: What is Accordion in Radix?

**Difficulty**: Beginner

**Strategy**:
Collapsible sections.

**Code Example**:
```javascript
<Accordion.Root>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q47: How do you handle form constraints in Radix?

**Difficulty**: Intermediate

**Strategy**:
Use `Label` and standard HTML constraints.

**Code Example**:
```javascript
<Label>Name</Label>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q48: What is the `Slot` utility?

**Difficulty**: Advanced

**Strategy**:
Merges props for `asChild` pattern.

**Code Example**:
```javascript
import { Slot } from '@radix-ui/react-slot'
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q49: How do you implement Toast?

**Difficulty**: Intermediate

**Strategy**:
Use `Toast` primitive.

**Code Example**:
```javascript
<Toast.Provider>...
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q50: What is `VisuallyHidden`?

**Difficulty**: Beginner

**Strategy**:
Hide content from screen but keep for screen readers.

**Code Example**:
```javascript
<VisuallyHidden>Label</VisuallyHidden>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q51: How do you server render Radix?

**Difficulty**: Intermediate

**Strategy**:
Works with SSR, supports hydration.

**Code Example**:
```javascript
// Standard React SSR
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q52: What is Shadcn UI?

**Difficulty**: Intermediate

**Strategy**:
Copy-paste components built on Radix + Tailwind.

**Code Example**:
```javascript
npx shadcn-ui@latest add button
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q53: How does Shadcn differ from MUI?

**Difficulty**: Intermediate

**Strategy**:
Shadcn is not a library, it's code you own. MUI is a library.

**Code Example**:
```javascript
// You edit the component files directly
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q54: What is Headless UI?

**Difficulty**: Intermediate

**Strategy**:
Similar to Radix, by Tailwind team.

**Code Example**:
```javascript
import { Menu } from '@headlessui/react'
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q55: How do you create a dark mode switch in MUI?

**Difficulty**: Beginner

**Strategy**:
Toggle context that updates theme mode.

**Code Example**:
```javascript
setMode(prev => prev === 'light' ? 'dark' : 'light')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q56: What is `useTheme` hook?

**Difficulty**: Beginner

**Strategy**:
Access theme variables in component.

**Code Example**:
```javascript
const theme = useTheme();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q57: How do you customize breakpoints?

**Difficulty**: Intermediate

**Strategy**:
In `createTheme`.

**Code Example**:
```javascript
breakpoints: { values: { mobile: 0, tablet: 640 } }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q58: What is the `Container` component?

**Difficulty**: Beginner

**Strategy**:
Centers content horizontally.

**Code Example**:
```javascript
<Container maxWidth='lg'>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q59: How do you use Skeleton loading?

**Difficulty**: Beginner

**Strategy**:
Placeholder for loading states.

**Code Example**:
```javascript
<Skeleton variant='rectangular' />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q60: What is the `Autocomplete` component?

**Difficulty**: Intermediate

**Strategy**:
Input with suggestions.

**Code Example**:
```javascript
<Autocomplete options={...} />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q61: How do you handle virtualized lists in MUI?

**Difficulty**: Advanced

**Strategy**:
Use `react-window` with MUI List.

**Code Example**:
```javascript
// Windowing for performance
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q62: What is the `ClickAwayListener`?

**Difficulty**: Intermediate

**Strategy**:
Detect clicks outside element.

**Code Example**:
```javascript
<ClickAwayListener onClickAway={...}>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q63: How do you use `Backdrop`?

**Difficulty**: Beginner

**Strategy**:
Dimmed layer behind overlays.

**Code Example**:
```javascript
<Backdrop open={true} />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q64: What is `SpeedDial`?

**Difficulty**: Intermediate

**Strategy**:
Floating action button that expands.

**Code Example**:
```javascript
<SpeedDial icon={<SpeedDialIcon />} />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q65: How do you customize scrollbars in MUI?

**Difficulty**: Intermediate

**Strategy**:
Global CSS override in CssBaseline.

**Code Example**:
```javascript
styleOverrides: { body: { '&::-webkit-scrollbar': ... } }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q66: What is `Collapse` transition?

**Difficulty**: Beginner

**Strategy**:
Vertical expand/collapse.

**Code Example**:
```javascript
<Collapse in={open}>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q67: How do you use `Zoom` transition?

**Difficulty**: Beginner

**Strategy**:
Scale animation.

**Code Example**:
```javascript
<Zoom in={true}>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q68: What is `Grow` transition?

**Difficulty**: Beginner

**Strategy**:
Expand from center.

**Code Example**:
```javascript
<Grow in={true}>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q69: What is `Slide` transition?

**Difficulty**: Beginner

**Strategy**:
Slide from edge.

**Code Example**:
```javascript
<Slide direction='up' in={true}>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q70: How do you use `Fade` transition?

**Difficulty**: Beginner

**Strategy**:
Opacity animation.

**Code Example**:
```javascript
<Fade in={true}>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q71: What is `GlobalStyles`?

**Difficulty**: Intermediate

**Strategy**:
Global CSS injection.

**Code Example**:
```javascript
<GlobalStyles styles={{ h1: { color: 'red' } }} />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q72: How do you theme variants?

**Difficulty**: Intermediate

**Strategy**:
Add new variants in theme.

**Code Example**:
```javascript
components: { MuiButton: { variants: [...] } }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q73: What is `shouldForwardProp`?

**Difficulty**: Advanced

**Strategy**:
Filter props passed to DOM in styled components.

**Code Example**:
```javascript
styled('div', { shouldForwardProp: (p) => p !== 'active' })
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q74: How do you use `alpha` utility?

**Difficulty**: Intermediate

**Strategy**:
Add opacity to color.

**Code Example**:
```javascript
bgcolor: alpha(theme.palette.primary.main, 0.5)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q75: What is `darken`/`lighten`?

**Difficulty**: Intermediate

**Strategy**:
Adjust color brightness.

**Code Example**:
```javascript
color: darken('red', 0.2)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q76: How do you use `useScrollTrigger`?

**Difficulty**: Intermediate

**Strategy**:
Detect scroll events for app bars.

**Code Example**:
```javascript
const trigger = useScrollTrigger();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q77: What is `FocusTrap`?

**Difficulty**: Intermediate

**Strategy**:
Keeps focus within element.

**Code Example**:
```javascript
<FocusTrap open>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q78: How do you use `NoSsr`?

**Difficulty**: Intermediate

**Strategy**:
Defer rendering to client side.

**Code Example**:
```javascript
<NoSsr>Client Only</NoSsr>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q79: What is `TextareaAutosize`?

**Difficulty**: Beginner

**Strategy**:
Textarea that grows with content.

**Code Example**:
```javascript
<TextareaAutosize />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q80: How do you use `Rating`?

**Difficulty**: Beginner

**Strategy**:
Star rating input.

**Code Example**:
```javascript
<Rating value={4} />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q81: What is `Timeline`?

**Difficulty**: Intermediate

**Strategy**:
Vertical list of events.

**Code Example**:
```javascript
<Timeline>...</Timeline>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q82: How do you use `TreeView`?

**Difficulty**: Intermediate

**Strategy**:
Hierarchical list.

**Code Example**:
```javascript
<TreeView>...</TreeView>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q83: What is `Masonry`?

**Difficulty**: Intermediate

**Strategy**:
Masonry layout (Pinterest style).

**Code Example**:
```javascript
<Masonry>...</Masonry>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q84: How do you use `Snackbar`?

**Difficulty**: Beginner

**Strategy**:
Brief notifications.

**Code Example**:
```javascript
<Snackbar message='Saved' />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q85: What is `Alert`?

**Difficulty**: Beginner

**Strategy**:
Feedback message.

**Code Example**:
```javascript
<Alert severity='error'>Error</Alert>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q86: How do you customize shadow?

**Difficulty**: Intermediate

**Strategy**:
Edit `shadows` array in theme.

**Code Example**:
```javascript
theme.shadows[1] = '0 2px 4px black'
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q87: What is `Paper`?

**Difficulty**: Beginner

**Strategy**:
Surface with shadow.

**Code Example**:
```javascript
<Paper elevation={3} />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q88: How do you use `Card`?

**Difficulty**: Beginner

**Strategy**:
Container for content.

**Code Example**:
```javascript
<Card><CardContent>...</CardContent></Card>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q89: What is `Divider`?

**Difficulty**: Beginner

**Strategy**:
Line separator.

**Code Example**:
```javascript
<Divider />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q90: How do you use `Chip`?

**Difficulty**: Beginner

**Strategy**:
Compact element (tag).

**Code Example**:
```javascript
<Chip label='Tag' onDelete={...} />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q91: What is `Badge`?

**Difficulty**: Beginner

**Strategy**:
Small status indicator.

**Code Example**:
```javascript
<Badge badgeContent={4} color='primary'>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q92: How do you use `Avatar`?

**Difficulty**: Beginner

**Strategy**:
User image.

**Code Example**:
```javascript
<Avatar src='/img.jpg' />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q93: What is `LinearProgress`?

**Difficulty**: Beginner

**Strategy**:
Loading bar.

**Code Example**:
```javascript
<LinearProgress />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q94: What is `CircularProgress`?

**Difficulty**: Beginner

**Strategy**:
Loading spinner.

**Code Example**:
```javascript
<CircularProgress />
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q95: How do you use `Tabs`?

**Difficulty**: Intermediate

**Strategy**:
Tabbed navigation.

**Code Example**:
```javascript
<Tabs><Tab label='One' /></Tabs>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q96: What is `BottomNavigation`?

**Difficulty**: Intermediate

**Strategy**:
Mobile nav bar.

**Code Example**:
```javascript
<BottomNavigation>...</BottomNavigation>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q97: How do you use `Breadcrumbs`?

**Difficulty**: Beginner

**Strategy**:
Navigation path.

**Code Example**:
```javascript
<Breadcrumbs>...</Breadcrumbs>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q98: What is `Link` component?

**Difficulty**: Beginner

**Strategy**:
Styled anchor tag.

**Code Example**:
```javascript
<Link href='#'>Link</Link>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q99: How do you use `Stepper`?

**Difficulty**: Intermediate

**Strategy**:
Step-by-step wizard.

**Code Example**:
```javascript
<Stepper activeStep={1}>...</Stepper>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>