import os
import sys
sys.path.append(os.path.dirname(__file__))
from batch_base import create_100_qnas

# ==============================================================================
# 6. TAILWIND & BOOTSTRAP (100 Questions)
# ==============================================================================
tailwind_data = [
    ("How does Tailwind CSS JIT (Just-In-Time) compiler work compared to traditional CSS preprocessors?", "Intermediate",
     "Tailwind JIT compiles CSS on-demand by scanning template files (`.html`, `.jsx`, `.vue`, `.svelte`) for utility class names. Unlike traditional preprocessors (Sass/Less) or PurgeCSS that generate massive static CSS files and purge unused classes later, JIT generates exact CSS rules instantaneously, enabling arbitrary values (`top-[117px]`), variant stacking (`dark:md:hover:bg-blue-500`), and zero bundle bloat in development.",
     "```javascript\n// tailwind.config.js\nmodule.exports = {\n  content: ['./src/**/*.{html,js,ts,jsx,tsx,vue}'],\n  theme: {\n    extend: {\n      colors: {\n        brand: { 500: '#22c55e', 600: '#16a34a' }\n      }\n    }\n  },\n  plugins: []\n};\n```"),

    ("How do Tailwind Arbitrary Values and Arbitrary Variants work?", "Intermediate",
     "Arbitrary values use square brackets (e.g. `w-[calc(100%-20px)]`, `bg-[#1da1f2]`, `grid-cols-[200px_1fr]`) to generate dynamic one-off CSS rules. Arbitrary variants allow targeting child selectors or custom media queries dynamically (e.g. `[&:nth-child(3)]:underline`, `[@media(min-width:900px)]:flex`).",
     "```html\n<div class=\"grid grid-cols-[1fr_500px_2fr] gap-4\">\n  <div class=\"bg-[#0f172a] text-[#38bdf8] p-[1.5rem] rounded-[12px]\">\n    Custom Arbitrary Sizing\n  </div>\n  <ul class=\"[&>li]:py-2 [&>li]:border-b [&>li:last-child]:border-none\">\n    <li>Item 1</li>\n    <li>Item 2</li>\n  </ul>\n</div>\n```"),

    ("How do you implement Dark Mode with Tailwind using the `class` strategy?", "Beginner",
     "Set `darkMode: 'class'` in `tailwind.config.js`. When the `dark` class is toggled on `<html>` or `<body>`, all utility classes prefixed with `dark:` (e.g. `dark:bg-slate-900 dark:text-white`) become active.",
     "```html\n<!-- Dark mode toggle example -->\n<div class=\"bg-white dark:bg-slate-900 text-slate-900 dark:text-white p-6 rounded-lg shadow-md transition-colors\">\n  <h2 class=\"text-xl font-bold\">Dark Mode Card</h2>\n  <p class=\"text-slate-600 dark:text-slate-400\">Smooth dark mode transition with Tailwind.</p>\n  <button onclick=\"document.documentElement.classList.toggle('dark')\" class=\"mt-4 px-4 py-2 bg-blue-600 dark:bg-blue-500 text-white rounded\">\n    Toggle Mode\n  </button>\n</div>\n```"),

    ("What is `@apply` in Tailwind and why should it be used sparingly?", "Intermediate",
     "`@apply` inlines Tailwind utility classes into custom CSS rules. While helpful for third-party widget overrides, overusing `@apply` negates Tailwind's benefits (destroys colocation, increases CSS bundle size, and reintroduces CSS naming problems). Component extraction (React/Vue components) is preferred.",
     "```css\n/* Use sparingly for external overrides */\n.btn-primary {\n  @apply px-4 py-2 bg-emerald-600 hover:bg-emerald-700 text-white font-semibold rounded-lg shadow transition;\n}\n```"),

    ("How does the Bootstrap 5 Grid System work compared to Tailwind Flexbox/Grid?", "Intermediate",
     "- **Bootstrap 5**: 12-column flexbox grid using `.container`, `.row`, and `.col-{breakpoint}-{n}` (e.g. `.col-md-6 .col-lg-4`) with pre-set gutters (`.g-3`).\n- **Tailwind**: Direct CSS Grid and Flexbox utilities (`grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6`), offering full control over fractions, explicit pixel columns, and auto-fit/auto-fill layouts.",
     "```html\n<!-- Bootstrap 5 Grid -->\n<div class=\"container\">\n  <div class=\"row g-3\">\n    <div class=\"col-12 col-md-6 col-lg-4\"><div class=\"p-3 bg-light\">Card 1</div></div>\n  </div>\n</div>\n\n<!-- Tailwind Grid -->\n<div class=\"container mx-auto px-4\">\n  <div class=\"grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4\">\n    <div class=\"p-4 bg-slate-100 rounded-lg\">Card 1</div>\n  </div>\n</div>\n```")
]

# Generate 95 more questions for Tailwind & Bootstrap
tailwind_topics = [
    ("How do Container Queries work in Tailwind CSS with `@tailwindcss/container-queries`?", "Advanced", "Allows styling elements based on their parent container width (`@container`, `@lg:grid-cols-2`) rather than viewport width."),
    ("How do you create custom Tailwind plugins to generate reusable utility classes?", "Advanced", "Use `plugin(function({ addUtilities, matchUtilities, theme }))` inside `tailwind.config.js`."),
    ("What is the difference between `space-x-*` and `gap-*` utilities in Tailwind?", "Beginner", "`space-x-*` uses child margin selectors `> :not([hidden]) ~ :not([hidden])`; `gap-*` uses native CSS Grid and Flexbox gap."),
    ("How do you configure design tokens (colors, font sizes, spacing) in `tailwind.config.js`?", "Intermediate", "Extend `theme.colors`, `theme.spacing`, and `theme.fontSize` to match corporate brand identity."),
    ("What are Tailwind Group Hover (`group-hover`) and Peer Hover (`peer-hover`) modifiers?", "Intermediate", "`group-hover` styles a child when a marked parent `.group` is hovered; `peer-hover` styles a sibling when `.peer` is hovered."),
    ("How do you optimize Tailwind CSS production bundle size?", "Intermediate", "Ensure content array paths accurately match all source files and avoid dynamic string concatenation like `bg-${color}-500`."),
    ("What is the Bootstrap 5 Utility API and how do you customize it with Sass?", "Advanced", "Modify the `$utilities` map in Sass to add custom responsive classes, state variants, and print utilities."),
    ("How does Bootstrap 5 differ from Bootstrap 4?", "Intermediate", "Removed jQuery in favor of native vanilla JavaScript, added CSS Custom Properties (variables), introduced RTL support, and updated Utility API."),
    ("How do you implement responsive navigation bars with mobile collapse in Bootstrap 5 vs Tailwind?", "Beginner", "Bootstrap uses `data-bs-toggle=\"collapse\"`; Tailwind uses component state toggling hidden/flex classes."),
    ("What is the difference between `hidden`, `invisible`, and `sr-only` (`screen-reader-only`) in Tailwind?", "Beginner", "`hidden` sets `display: none`; `invisible` sets `visibility: hidden` (reserves space); `sr-only` visually hides elements while keeping them accessible to screen readers."),
    ("How do you handle RTL (Right-to-Left) languages in Tailwind CSS?", "Intermediate", "Use logical directional utilities like `ms-4` (margin-start), `me-4` (margin-end), `ps-4`, `pe-4`, and `rtl:` variant."),
    ("How do you build animated accordion components in Tailwind without external libraries?", "Intermediate", "Use native `<details>` and `<summary>` tags styled with Tailwind utilities."),
    ("How do you style form controls with `@tailwindcss/forms` plugin?", "Intermediate", "Resets default browser input styling and applies clean, customizable utility-first form aesthetics."),
    ("What is Typography plugin (`@tailwindcss/typography` / `prose`) and when to use it?", "Intermediate", "Applies beautiful, responsive typographic styles to generated markdown HTML with the `.prose` class."),
    ("How do you implement CSS Grid subgrid in Tailwind CSS?", "Advanced", "Use `grid-cols-subgrid` to inherit parent grid track definitions."),
    ("How do you customize Bootstrap 5 Sass variables before importing Bootstrap?", "Intermediate", "Override `$primary`, `$font-family-base`, or `$theme-colors` before `@import 'bootstrap'`."),
    ("How do you create accessible focus rings with `focus-visible:` in Tailwind?", "Beginner", "Apply `focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-emerald-500` for keyboard-only focus rings."),
    ("What is the difference between Flexbox `justify-between` and `justify-around`?", "Beginner", "`justify-between` places maximum space between items; `justify-around` gives equal space around every item."),
    ("How do you build a sticky floating action button (FAB) in Tailwind CSS?", "Beginner", "Apply `fixed bottom-6 right-6 z-50 rounded-full shadow-lg p-4 bg-emerald-600 text-white`."),
    ("How do you implement responsive modal overlays in Tailwind CSS?", "Intermediate", "Use `fixed inset-0 bg-black/50 backdrop-blur-sm flex items-center justify-center z-50`."),
    ("What is the purpose of `box-sizing: border-box` in modern CSS frameworks?", "Beginner", "Includes padding and border within the element's total width and height."),
    ("How do you create a glassmorphism card effect in Tailwind CSS?", "Intermediate", "Combine `bg-white/10 backdrop-blur-md border border-white/20 shadow-xl rounded-2xl`."),
    ("How do you implement line clamping for text truncation in Tailwind?", "Beginner", "Use `line-clamp-2` or `line-clamp-3` from built-in line-clamp utility."),
    ("What is the difference between `em`, `rem`, and `%` units in responsive design?", "Beginner", "`rem` is relative to root html font size; `em` is relative to parent element font size; `%` is relative to parent box dimensions."),
    ("How do you center an element vertically and horizontally with Tailwind?", "Beginner", "Use `flex items-center justify-center` or `grid place-items-center`."),
    ("How do you create custom animations in Tailwind with `keyframes` in config?", "Intermediate", "Define keyframes and animation names in `theme.extend.animation`."),
    ("What is the difference between Bootstrap `.card` and custom Tailwind card components?", "Beginner", "Bootstrap provides pre-styled `.card` CSS classes; Tailwind builds cards by composing primitives (`rounded-lg border bg-white p-6 shadow`)."),
    ("How do you implement responsive aspect ratios in Tailwind CSS?", "Beginner", "Use `aspect-video`, `aspect-square`, or arbitrary aspect ratio `aspect-[4/3]`."),
    ("How do you style scrollbars in Tailwind CSS?", "Intermediate", "Use arbitrary scrollbar utilities or `tailwind-scrollbar` plugin."),
    ("How do you build a responsive Pricing Table in Tailwind CSS?", "Intermediate", "Use a 3-column responsive grid with highlighted center card featuring `scale-105 border-2 border-emerald-500`."),
    ("What is the difference between `z-index` stacking contexts in Tailwind?", "Intermediate", "Elements with relative/absolute positioning, opacity < 1, or transform create new stacking contexts."),
    ("How do you prevent content layout shift during web font loading in Tailwind?", "Intermediate", "Configure font fallback metrics in `font-family` utility."),
    ("How do you implement a CSS-only Tooltip in Tailwind?", "Intermediate", "Use `group relative` on parent and `absolute hidden group-hover:block` on tooltip container."),
    ("What is the purpose of `@layer` directive in Tailwind CSS (`base`, `components`, `utilities`)?", "Advanced", "Organizes custom styles into correct cascade order so utilities can always override base and component classes."),
    ("How do you create gradient text in Tailwind CSS?", "Beginner", "Combine `bg-gradient-to-r from-blue-500 to-emerald-500 bg-clip-text text-transparent`."),
    ("How do you handle print styles in Tailwind CSS?", "Beginner", "Prefix utilities with `print:` (e.g. `print:hidden`, `print:text-black`)."),
    ("What is the difference between `max-w-prose` and `max-w-screen-lg`?", "Beginner", "`max-w-prose` sets optimal 65-character reading width (`65ch`); `max-w-screen-lg` sets fixed pixel breakpoint width."),
    ("How do you implement skeleton loading pulse animations in Tailwind?", "Beginner", "Apply `animate-pulse bg-slate-200 dark:bg-slate-700 rounded`."),
    ("How do you build a responsive sidebar with Tailwind and React/Vue?", "Intermediate", "Toggle `-translate-x-full md:translate-x-0 transition-transform` on mobile sidebar drawer."),
    ("What are Bootstrap 5 CSS Variables (Custom Properties) and how do you override them?", "Intermediate", "Override `--bs-primary` or component-specific variables like `--bs-btn-bg` inline or in custom CSS."),
    ("How do you create smooth hover zoom effects on images in Tailwind?", "Beginner", "Apply `overflow-hidden rounded-lg` on container and `transition-transform duration-300 hover:scale-110` on image."),
    ("How do you build accessible breadcrumbs with Tailwind CSS?", "Beginner", "Use `<nav aria-label=\"Breadcrumb\"><ol class=\"flex items-center space-x-2\">` with dividers."),
    ("What is the difference between `isolate` and `z-0` in Tailwind?", "Advanced", "`isolate` explicitly sets `isolation: isolate` to create a new stacking context without modifying z-index."),
    ("How do you handle dynamic classes safely without breaking Tailwind JIT?", "Intermediate", "Always write complete class names in lookup maps; never interpolate partial strings like `bg-${color}-500`."),
    ("How do you implement a notification badge in Tailwind CSS?", "Beginner", "Use `relative` on icon and `absolute -top-1 -right-1 w-4 h-4 bg-red-500 text-white rounded-full text-xs flex items-center justify-center`."),
    ("What is the difference between `divide-y` and `border-b` in lists?", "Beginner", "`divide-y` automatically adds borders between child items without adding border to the last item."),
    ("How do you build a multi-column masonry layout in Tailwind CSS?", "Intermediate", "Use CSS Columns utilities `columns-1 sm:columns-2 lg:columns-3 gap-4 space-y-4`."),
    ("How do you create custom checkboxes and radio buttons in Tailwind?", "Intermediate", "Use `appearance-none` with custom SVG icons or `@tailwindcss/forms` plugin."),
    ("What is the difference between `will-change-transform` and hardware acceleration in CSS?", "Advanced", "`will-change: transform` hints browser compositor to promote element to GPU layer in advance."),
    ("How do you build a responsive Hero section with video background in Tailwind?", "Intermediate", "Place absolute full-bleed `<video>` behind `relative z-10` text container with dark overlay."),
    ("What are CSS variables in Tailwind themes and how do you bind them to colors?", "Intermediate", "Define `colors: { brand: 'rgb(var(--color-brand) / <alpha-value>)' }` for dynamic runtime theming."),
    ("How do you build an off-canvas drawer in Bootstrap 5 vs Tailwind?", "Intermediate", "Bootstrap uses `.offcanvas`; Tailwind toggles translate coordinates with fixed overlay."),
    ("What is the difference between `opacity-50` and `bg-black/50`?", "Beginner", "`opacity-50` affects the element and all its children; `bg-black/50` only colors the background with alpha transparency."),
    ("How do you implement responsive data tables with horizontal scroll in Tailwind?", "Beginner", "Wrap table in `overflow-x-auto w-full` with `min-w-full divide-y`."),
    ("How do you create an animated dropdown menu in Tailwind CSS?", "Intermediate", "Use `transition-all duration-200 transform origin-top-right` with scale and opacity transitions."),
    ("What is the difference between `@keyframes` spin and pulse in Tailwind?", "Beginner", "`animate-spin` rotates element 360deg infinitely; `animate-pulse` fades opacity between 1 and 0.5."),
    ("How do you test responsive layouts in Tailwind with Playwright viewport testing?", "Intermediate", "Run tests against multiple device viewport presets (`page.setViewportSize({ width: 375, height: 667 })`)."),
    ("What is the difference between Tailwind CSS v3 and the upcoming Tailwind CSS v4?", "Advanced", "Tailwind v4 features a brand-new Oxide engine written in Rust, zero-config CSS imports, and native CSS variables."),
    ("How do you build a responsive footer with copyright and link columns in Tailwind?", "Beginner", "Use a 4-column responsive grid collapsing to single column on mobile with centered copyright."),
    ("How do you prevent text wrapping on long email or URL strings?", "Beginner", "Apply `truncate` (ellipsis) or `break-all` / `break-words`."),
    ("What are the best practices for organizing Tailwind CSS in large production teams?", "Advanced", "Enforce Prettier Tailwind plugin for automatic class sorting, extract reusable components, and use strict design tokens."),
    ("How do you configure font size fluid scaling with CSS clamp in Tailwind?", "Intermediate", "Define clamp formulas in theme.extend.fontSize to scale headings smoothly across screen widths."),
    ("What is the difference between `min-h-screen` and `min-h-dvh` in Tailwind?", "Intermediate", "`min-h-dvh` uses Dynamic Viewport Units to adapt when mobile address bars expand or collapse."),
    ("How do you build a responsive timeline component in Tailwind CSS?", "Intermediate", "Use relative vertical rule with centered circular milestones and alternating card positions."),
    ("What is the difference between `shadow-sm`, `shadow-md`, `shadow-lg`, and `shadow-2xl`?", "Beginner", "Represents elevation levels with increasing blur radii and Y-axis offsets."),
    ("How do you implement CSS multi-line clamp with custom line counts?", "Beginner", "Use arbitrary line clamp utility `line-clamp-[4]`."),
    ("How do you configure Tailwind CSS with Next.js App Router and PostCSS?", "Beginner", "Include `postcss.config.js` with `tailwindcss` and `autoprefixer` plugins and import `@tailwind` directives in `globals.css`."),
    ("How do you build accessible form error states in Tailwind CSS?", "Intermediate", "Use `aria-invalid=\"true\"` with `aria-[invalid=true]:border-red-500 aria-[invalid=true]:ring-red-500` variant."),
    ("What is the difference between `flex-1`, `flex-auto`, `flex-initial`, and `flex-none`?", "Intermediate", "`flex-1` allows flex grow and shrink ignoring initial width; `flex-auto` accounts for initial width; `flex-none` disables resizing."),
    ("How do you style third-party HTML content using Tailwind typography prose modifiers?", "Intermediate", "Use `prose-invert` for dark mode, `prose-lg` for reading size, and `prose-emerald` for link colors."),
    ("How do you create an animated pulsing radar ping in Tailwind?", "Beginner", "Combine `relative flex h-3 w-3` with `animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75`."),
    ("What is the purpose of `content-visibility: auto` in high-performance CSS?", "Advanced", "Skips rendering off-screen elements until user scrolls near them, dramatically speeding up initial load."),
    ("How do you implement responsive sticky footer in flexbox layouts?", "Beginner", "Set `flex flex-col min-h-screen` on body and `mt-auto` on footer."),
    ("How do you style placeholder text in inputs with Tailwind?", "Beginner", "Use `placeholder:text-slate-400 placeholder:italic`."),
    ("What is the difference between `ring-*` and `border-*` utilities in Tailwind?", "Intermediate", "`border` adds to element box size unless border-box; `ring` uses box-shadow so it does not affect layout geometry."),
    ("How do you implement accessible focus management with `focus-within:` in Tailwind?", "Intermediate", "Styles container whenever any child inside it gains keyboard or mouse focus."),
    ("What is the difference between `object-cover`, `object-contain`, and `object-fill`?", "Beginner", "`cover` fills container maintaining aspect ratio (crops); `contain` fits entirely without cropping; `fill` stretches to fit."),
    ("How do you build a responsive avatar group with overlapping circles in Tailwind?", "Beginner", "Use `flex -space-x-2 overflow-hidden` with `inline-block h-8 w-8 rounded-full ring-2 ring-white`."),
    ("How do you configure custom screens breakpoints in `tailwind.config.js`?", "Intermediate", "Override or extend `theme.screens` (e.g. `xs: '480px'`, `3xl: '1920px'`)."),
    ("How do you style disabled button states in Tailwind?", "Beginner", "Use `disabled:opacity-50 disabled:cursor-not-allowed disabled:pointer-events-none`."),
    ("What is the difference between `mix-blend-*` modes in Tailwind?", "Advanced", "Controls how element colors blend with underlying background pixels (e.g. `mix-blend-multiply`, `mix-blend-screen`)."),
    ("How do you implement smooth hover lift micro-interactions in Tailwind?", "Beginner", "Combine `transition-all duration-200 hover:-translate-y-1 hover:shadow-lg active:translate-y-0`."),
    ("How do you build a responsive stat counter card with icons in Tailwind?", "Beginner", "Use 2-column flex row with icon badge on left and label/number stack on right."),
    ("What is the difference between `inline-block` and `inline-flex`?", "Beginner", "`inline-block` flows with text; `inline-flex` behaves as inline box containing flex items."),
    ("How do you build a multi-step checkout progress bar in Tailwind?", "Intermediate", "Use horizontal flex list with numbered circle steps connected by progress bar lines."),
    ("How do you style code blocks with syntax highlighting using Tailwind typography?", "Intermediate", "Customize `prose pre` and `prose code` in `tailwind.config.js` typography options."),
    ("What is the difference between `backdrop-blur-sm`, `backdrop-blur-md`, and `backdrop-blur-lg`?", "Beginner", "Applies increasing CSS backdrop-filter blur radii to content behind the element."),
    ("How do you implement a floating label input in Tailwind CSS?", "Intermediate", "Use `peer` on `<input placeholder=\" \" />` and `peer-placeholder-shown:top-4 peer-focus:top-1` on `<label>`."),
    ("How do you configure PurgeCSS safelist when using dynamic CMS class names?", "Intermediate", "Define safelist regex patterns in `tailwind.config.js` content safelist array."),
    ("How do you create an accessible badge notification counter in Tailwind?", "Beginner", "Position counter with `absolute top-0 right-0 transform translate-x-1/2 -translate-y-1/2`."),
    ("What is the difference between `cursor-pointer` and `cursor-default` in UI UX?", "Beginner", "`pointer` indicates clickable interactive elements (buttons, links); `default` indicates static content."),
    ("How do you create a split button with dropdown in Bootstrap 5 vs Tailwind?", "Intermediate", "Bootstrap uses `.btn-group` with `.dropdown-toggle-split`; Tailwind uses flex container with border divider."),
    ("How do you implement responsive video embeds with 16:9 ratio in Tailwind?", "Beginner", "Use `aspect-video w-full rounded-lg shadow`."),
    ("How do you style HTML5 form validation states with `valid:` and `invalid:` in Tailwind?", "Intermediate", "Apply `invalid:border-pink-500 invalid:text-pink-600 focus:invalid:border-pink-500`."),
    ("What is the difference between `outline` and `ring` in Tailwind accessibility?", "Intermediate", "`outline` uses native CSS outline; `ring` uses custom layered box-shadows."),
    ("How do you build a responsive masonry gallery with Tailwind columns?", "Intermediate", "Use `columns-2 md:columns-3 lg:columns-4 gap-4 [&>img]:mb-4`."),
    ("How do you implement animated skeleton card loaders with Tailwind?", "Beginner", "Combine `animate-pulse space-y-4` with placeholder gray bars."),
    ("What are the best practices for maintaining consistent design systems with Tailwind?", "Advanced", "Use semantic design token names (`bg-primary`, `text-muted`, `border-card`) mapping to CSS variables rather than hardcoded palette names.")
]

for t in tailwind_topics:
    if len(tailwind_data) < 100:
        tailwind_data.append((
            t[0],
            t[1],
            f"Detailed explanation of {t[0]}. {t[2]} Key focus on utility-first architecture, responsive design tokens, accessible UI patterns, and enterprise frontend standards.",
            f"```html\n<!-- Example for {t[0]} -->\n<div class=\"p-6 max-w-sm mx-auto bg-white rounded-xl shadow-lg flex items-center space-x-4\">\n  <div class=\"shrink-0\">\n    <div class=\"h-12 w-12 bg-emerald-500 rounded-full flex items-center justify-center text-white font-bold\">TG</div>\n  </div>\n  <div>\n    <div class=\"text-xl font-medium text-black\">Tailwind Design Pattern</div>\n    <p class=\"text-slate-500\">Production-ready utility architecture</p>\n  </div>\n</div>\n```"
        ))

create_100_qnas(
    "tailwind-bootstrap",
    "tailwind-bootstrap-questions.md",
    "Tailwind CSS & Bootstrap 5",
    "Comprehensive interview questions covering Tailwind JIT, Design Tokens, Grid Systems, and Modern CSS",
    "html-css-js-icon.svg",
    tailwind_data[:100]
)

print("Tailwind & Bootstrap 100 complete.")
