# Webpack, Babel, and Vite Interview Questions

## Table of Contents

- [Webpack, Babel, and Vite Interview Questions](#webpack-babel-and-vite-interview-questions)
  - [Table of Contents](#table-of-contents)
  - [Build Tools Fundamentals](#build-tools-fundamentals)
    - [Q1: What is Webpack and why is it used?](#q1-what-is-webpack-and-why-is-it-used)
    - [Q2: What is the difference between Webpack and Vite?](#q2-what-is-the-difference-between-webpack-and-vite)
    - [Q3: What is Babel and how does it work?](#q3-what-is-babel-and-how-does-it-work)
    - [Q4: Explain the concept of Loaders and Plugins in Webpack.](#q4-explain-the-concept-of-loaders-and-plugins-in-webpack)
    - [Q5: What is Tree Shaking?](#q5-what-is-tree-shaking)
    - [Q6: What is Hot Module Replacement (HMR)?](#q6-what-is-hot-module-replacement-hmr)
    - [Q7: How does Vite achieve faster development server start times compared to Webpack?](#q7-how-does-vite-achieve-faster-development-server-start-times-compared-to-webpack)
    - [Q8: What is Code Splitting and why is it important?](#q8-what-is-code-splitting-and-why-is-it-important)
    - [Q9: Explain Webpack Module Federation.](#q9-explain-webpack-module-federation)
    - [Q10: How do you handle environment variables in Vite?](#q10-how-do-you-handle-environment-variables-in-vite)
    - [Q11: What are Polyfills and how does Babel handle them?](#q11-what-are-polyfills-and-how-does-babel-handle-them)
    - [Q12: How do you configure multiple entry points in Webpack?](#q12-how-do-you-configure-multiple-entry-points-in-webpack)
    - [Q13: What is the purpose of source maps?](#q13-what-is-the-purpose-of-source-maps)
    - [Q14: How does Vite handle CSS and CSS Modules?](#q14-how-does-vite-handle-css-and-css-modules)
    - [Q15: Explain the difference between `dependencies` and `devDependencies` relevant to build tools.](#q15-explain-the-difference-between-dependencies-and-devdependencies-relevant-to-build-tools)
    - [Q16: What is the `public` directory in Vite used for?](#q16-what-is-the-public-directory-in-vite-used-for)
    - [Q17: How do you optimize a Webpack production build?](#q17-how-do-you-optimize-a-webpack-production-build)
    - [Q18: What is "transpilation" and why do we need it?](#q18-what-is-transpilation-and-why-do-we-need-it)
    - [Q19: How does Babel use Presets?](#q19-how-does-babel-use-presets)
    - [Q20: Can you use Webpack plugins in Vite?](#q20-can-you-use-webpack-plugins-in-vite)
    - [Q21: What is the Webpack `DefinePlugin`?](#q21-what-is-the-webpack-defineplugin)
    - [Q22: How do you resolve file extensions in Webpack?](#q22-how-do-you-resolve-file-extensions-in-webpack)
    - [Q23: What are Webpack Aliases?](#q23-what-are-webpack-aliases)
    - [Q24: How do you analyze bundle size in Webpack?](#q24-how-do-you-analyze-bundle-size-in-webpack)
    - [Q25: What is the `clean-webpack-plugin` (or `output.clean`)?](#q25-what-is-the-clean-webpack-plugin-or-outputclean)
    - [Q26: Explain `babel-loader`.](#q26-explain-babel-loader)
    - [Q27: What is the difference between `babel.config.js` and `.babelrc`?](#q27-what-is-the-difference-between-babelconfigjs-and-babelrc)
    - [Q28: In what order do Babel plugins and presets run?](#q28-in-what-order-do-babel-plugins-and-presets-run)
    - [Q29: What is `core-js`?](#q29-what-is-core-js)
    - [Q30: How does Vite handle static assets?](#q30-how-does-vite-handle-static-assets)
    - [Q31: What is Vite's "Library Mode"?](#q31-what-is-vites-library-mode)
    - [Q32: What is Dependency Pre-Bundling in Vite?](#q32-what-is-dependency-pre-bundling-in-vite)
    - [Q33: How do you use Glob Imports in Vite?](#q33-how-do-you-use-glob-imports-in-vite)
    - [Q34: What is `vite.config.js`?](#q34-what-is-viteconfigjs)
    - [Q35: Does Vite support Server-Side Rendering (SSR)?](#q35-does-vite-support-server-side-rendering-ssr)
    - [Q36: What is the `CopyWebpackPlugin` used for?](#q36-what-is-the-copywebpackplugin-used-for)
    - [Q37: What is "Scope Hoisting" in Webpack?](#q37-what-is-scope-hoisting-in-webpack)
    - [Q38: What is the `sideEffects` flag in `package.json`?](#q38-what-is-the-sideeffects-flag-in-packagejson)
    - [Q39: How do you configure a proxy in Vite/Webpack dev server?](#q39-how-do-you-configure-a-proxy-in-vitewebpack-dev-server)
    - [Q40: What is the difference between `hash`, `chunkhash`, and `contenthash` in Webpack?](#q40-what-is-the-difference-between-hash-chunkhash-and-contenthash-in-webpack)
    - [Q41: What is SWC and how does it relate to Babel?](#q41-what-is-swc-and-how-does-it-relate-to-babel)
    - [Q42: What is esbuild?](#q42-what-is-esbuild)
    - [Q43: How do you handle TypeScript in Webpack?](#q43-how-do-you-handle-typescript-in-webpack)
    - [Q44: How do you handle TypeScript in Vite?](#q44-how-do-you-handle-typescript-in-vite)
    - [Q45: What is Differential Loading?](#q45-what-is-differential-loading)
    - [Q46: What is the `@babel/plugin-transform-runtime`?](#q46-what-is-the-babelplugin-transform-runtime)
    - [Q47: How do you enable HMR in Webpack manually?](#q47-how-do-you-enable-hmr-in-webpack-manually)
    - [Q48: What is the `MiniCssExtractPlugin`?](#q48-what-is-the-minicssextractplugin)
    - [Q49: How does Vite handle JSON files?](#q49-how-does-vite-handle-json-files)
    - [Q50: What is the `resolve.modules` configuration in Webpack?](#q50-what-is-the-resolvemodules-configuration-in-webpack)
    - [Q51: What is the purpose of `html-webpack-plugin`?](#q51-what-is-the-purpose-of-html-webpack-plugin)
    - [Q52: How do you load images in Webpack 5?](#q52-how-do-you-load-images-in-webpack-5)
    - [Q53: What are "Asset Modules" in Webpack 5?](#q53-what-are-asset-modules-in-webpack-5)
    - [Q54: How do you debug a slow Webpack build?](#q54-how-do-you-debug-a-slow-webpack-build)
    - [Q55: What is `vite preview` command?](#q55-what-is-vite-preview-command)
    - [Q56: How does Vite handle `.vue` or `.svelte` files?](#q56-how-does-vite-handle-vue-or-svelte-files)
    - [Q57: What is the Rollup bundler?](#q57-what-is-the-rollup-bundler)
    - [Q58: Why is Rollup often preferred for libraries over Webpack?](#q58-why-is-rollup-often-preferred-for-libraries-over-webpack)
    - [Q59: What is Parcel?](#q59-what-is-parcel)
    - [Q60: What is "Zero Config" in build tools?](#q60-what-is-zero-config-in-build-tools)
    - [Q61: How do you inject global variables in Webpack?](#q61-how-do-you-inject-global-variables-in-webpack)
    - [Q62: What is the `target` option in Webpack?](#q62-what-is-the-target-option-in-webpack)
    - [Q63: How to handle CSS Preprocessors (Sass/Less) in Webpack?](#q63-how-to-handle-css-preprocessors-sassless-in-webpack)
    - [Q64: What is PostCSS?](#q64-what-is-postcss)
    - [Q65: How do you use PostCSS with Vite?](#q65-how-do-you-use-postcss-with-vite)
    - [Q66: What is `autoprefixer`?](#q66-what-is-autoprefixer)
    - [Q67: How do you exclude `node_modules` from Babel transformation?](#q67-how-do-you-exclude-node_modules-from-babel-transformation)
    - [Q68: What is `babel-node`?](#q68-what-is-babel-node)
    - [Q69: What is the AST (Abstract Syntax Tree)?](#q69-what-is-the-ast-abstract-syntax-tree)
    - [Q70: Can Babel parse TypeScript?](#q70-can-babel-parse-typescript)
    - [Q71: What is the difference between `Babel` and `TypeScript` compiler (`tsc`)?](#q71-what-is-the-difference-between-babel-and-typescript-compiler-tsc)
    - [Q72: How do you create a custom Webpack loader?](#q72-how-do-you-create-a-custom-webpack-loader)
    - [Q73: How do you create a custom Webpack plugin?](#q73-how-do-you-create-a-custom-webpack-plugin)
    - [Q74: What is `webpack-dev-server`?](#q74-what-is-webpack-dev-server)
    - [Q75: How do you handle "Magic Comments" in Webpack?](#q75-how-do-you-handle-magic-comments-in-webpack)
    - [Q76: What is Prefetching and Preloading in Webpack?](#q76-what-is-prefetching-and-preloading-in-webpack)
    - [Q77: How does Webpack handle circular dependencies?](#q77-how-does-webpack-handle-circular-dependencies)
    - [Q78: What is the `DLLPlugin` in Webpack?](#q78-what-is-the-dllplugin-in-webpack)
    - [Q79: Why is `DLLPlugin` less relevant in Webpack 5/Vite?](#q79-why-is-dllplugin-less-relevant-in-webpack-5vite)
    - [Q80: How do you measure build performance in Vite?](#q80-how-do-you-measure-build-performance-in-vite)
    - [Q81: What is the `legacy` plugin in Vite?](#q81-what-is-the-legacy-plugin-in-vite)
    - [Q82: How do you deploy a Vite app to GitHub Pages?](#q82-how-do-you-deploy-a-vite-app-to-github-pages)
    - [Q83: What is the `base` config option in Vite?](#q83-what-is-the-base-config-option-in-vite)
    - [Q84: How do you implement Critical CSS extraction?](#q84-how-do-you-implement-critical-css-extraction)
    - [Q85: What is the difference between `module.exports` and `export default`?](#q85-what-is-the-difference-between-moduleexports-and-export-default)
    - [Q86: How does Webpack resolve `import` statements?](#q86-how-does-webpack-resolve-import-statements)
    - [Q87: What is the `externals` configuration in Webpack?](#q87-what-is-the-externals-configuration-in-webpack)
    - [Q88: How do you remove console logs in production build?](#q88-how-do-you-remove-console-logs-in-production-build)
    - [Q89: What is `webpack-merge`?](#q89-what-is-webpack-merge)
    - [Q90: How do you setup ESLint with Vite/Webpack?](#q90-how-do-you-setup-eslint-with-vitewebpack)
    - [Q91: What is Turbopack?](#q91-what-is-turbopack)
    - [Q92: What is the difference between Bundling and Compiling?](#q92-what-is-the-difference-between-bundling-and-compiling)
    - [Q93: How do you handle caching in Webpack?](#q93-how-do-you-handle-caching-in-webpack)
    - [Q94: What are "Runtime Chunks" in Webpack?](#q94-what-are-runtime-chunks-in-webpack)
    - [Q95: How does Vite handle Web Workers?](#q95-how-does-vite-handle-web-workers)
    - [Q96: What is the `optimizeDeps` option in Vite?](#q96-what-is-the-optimizedeps-option-in-vite)
    - [Q97: How do you debug Vite HMR issues?](#q97-how-do-you-debug-vite-hmr-issues)
    - [Q98: What is the `babel-plugin-macros`?](#q98-what-is-the-babel-plugin-macros)
    - [Q99: How do you customize the output directory in Vite?](#q99-how-do-you-customize-the-output-directory-in-vite)
    - [Q100: What is the future of frontend build tools?](#q100-what-is-the-future-of-frontend-build-tools)

---

## Build Tools Fundamentals

### Q1: What is Webpack and why is it used?

**Difficulty: Easy**

**Answer:**
Webpack is a static module bundler for modern JavaScript applications. When Webpack processes your application, it builds a dependency graph that maps every module your project needs and generates one or more bundles.
**Key Features:**

- **Bundling:** Combines multiple files into a single file (or a few files) to reduce HTTP requests.
- **Asset Management:** Can process HTML, CSS, images, and other assets, not just JavaScript.
- **Transformation:** Uses loaders to preprocess files (e.g., TypeScript to JavaScript, SASS to CSS).

### Q2: What is the difference between Webpack and Vite?

**Difficulty: Medium**

**Answer:**

- **Development Server:**
  - **Webpack:** Bundles the entire application before serving. Rebuilding can be slow for large apps.
  - **Vite:** Uses native ES modules (ESM) in the browser. It serves source files directly and only bundles dependencies (using esbuild) which is extremely fast.
- **Build:**
  - **Webpack:** Uses its own bundling logic.
  - **Vite:** Uses Rollup for production builds.
- **Configuration:**
  - **Webpack:** Known for complex configuration.
  - **Vite:** Opinions-based, comes with sensible defaults, often requiring zero config.

### Q3: What is Babel and how does it work?

**Difficulty: Easy**

**Answer:**
Babel is a JavaScript compiler (transpiler) that converts ECMAScript 2015+ (ES6+) code into a backwards-compatible version of JavaScript that can run in current and older browsers or environments.
**How it works:**

1.  **Parsing:** Takes code and outputs an Abstract Syntax Tree (AST).
2.  **Transformation:** Manipulates the AST based on plugins/presets.
3.  **Code Generation:** Converts the modified AST back into code.

### Q4: Explain the concept of Loaders and Plugins in Webpack.

**Difficulty: Easy**

**Answer:**

- **Loaders:** Transformations applied to the source code of a module. They allow you to import files other than JavaScript (like CSS, Images, TypeScript).
  - _Example:_ `css-loader`, `style-loader`, `babel-loader`.
- **Plugins:** Perform a wider range of tasks like bundle optimization, asset management, and injection of environment variables. They tap into the Webpack build lifecycle.
  - _Example:_ `HtmlWebpackPlugin`, `CleanWebpackPlugin`, `MiniCssExtractPlugin`.

### Q5: What is Tree Shaking?

**Difficulty: Medium**

**Answer:**
Tree Shaking is a term commonly used in the JavaScript context for dead-code elimination. It relies on the static structure of ES2015 module syntax (`import` and `export`). Webpack and Rollup (used by Vite) detect unused exports in your code and exclude them from the final bundle, reducing the bundle size.

### Q6: What is Hot Module Replacement (HMR)?

**Difficulty: Medium**

**Answer:**
HMR exchanges, adds, or removes modules while an application is running, without a full reload. This significantly speeds up development by retaining the application state which is lost during a full reload.

### Q7: How does Vite achieve faster development server start times compared to Webpack?

**Difficulty: Advanced**

**Answer:**
Vite divides the application into two categories:

1.  **Dependencies:** Plain JavaScript that does not change often. Vite pre-bundles these using **esbuild**, which is written in Go and is 10-100x faster than JavaScript-based bundlers.
2.  **Source Code:** Code that needs transforming (e.g., JSX, CSS) and changes often. Vite serves this over native ESM. The browser takes over the job of bundling (requesting modules as needed).

### Q8: What is Code Splitting and why is it important?

**Difficulty: Medium**

**Answer:**
Code Splitting is a feature (supported by Webpack and Vite/Rollup) that allows you to split your code into various bundles which can then be loaded on demand or in parallel.
**Importance:**

- Reduces the initial load time of the application.
- Allows for lazy loading of heavy components or routes.
- Improves caching (if vendor code is split, it doesn't need to be re-downloaded when app code changes).

### Q9: Explain Webpack Module Federation.

**Difficulty: Advanced**

**Answer:**
Module Federation allows multiple separate builds to form a single application. These separate builds act like containers and can expose and consume code between each other at runtime. This is the foundation for Micro-Frontends architecture in Webpack 5.

### Q10: How do you handle environment variables in Vite?

**Difficulty: Medium**

**Answer:**
Vite exposes environment variables on the special `import.meta.env` object.

- Variables typically start with `VITE_` (e.g., `VITE_API_URL`) to be exposed to the client.
- Built-in variables: `import.meta.env.MODE`, `import.meta.env.BASE_URL`, `import.meta.env.PROD`, `import.meta.env.DEV`.

### Q11: What are Polyfills and how does Babel handle them?

**Difficulty: Medium**

**Answer:**
A polyfill is a piece of code used to provide modern functionality on older browsers (e.g., `Array.prototype.includes`).
Babel handles polyfills typically via `core-js`. With `@babel/preset-env`, you can set `useBuiltIns: 'usage'`, which automatically imports only the polyfills required by your code based on your target browsers.

### Q12: How do you configure multiple entry points in Webpack?

**Difficulty: Medium**

**Answer:**
Configure the `entry` property in `webpack.config.js` as an object.

```javascript
module.exports = {
  entry: {
    pageOne: "./src/pageOne/index.js",
    pageTwo: "./src/pageTwo/index.js",
  },
  output: {
    filename: "[name].bundle.js",
    path: __dirname + "/dist",
  },
};
```

### Q13: What is the purpose of source maps?

**Difficulty: Easy**

**Answer:**
Source maps are files that map the transformed/minified code back to the original source code. They allow developers to debug the code in the browser as if they were running the original source files, seeing original line numbers and variable names.

### Q14: How does Vite handle CSS and CSS Modules?

**Difficulty: Easy**

**Answer:**
Vite supports importing `.css` files directly.

- **Standard CSS:** `import './style.css'` injects content via `<style>`.
- **CSS Modules:** Files ending in `.module.css` are treated as CSS modules.
- **Pre-processors:** Supports `.scss`, `.less` if installed.

### Q15: Explain the difference between `dependencies` and `devDependencies` relevant to build tools.

**Difficulty: Easy**

**Answer:**

- **dependencies:** Libraries required for the application to run in production (e.g., `react`).
- **devDependencies:** Libraries needed only during development and build time (e.g., `webpack`, `vite`, `babel`). Build tools are usually here.

### Q16: What is the `public` directory in Vite used for?

**Difficulty: Easy**

**Answer:**
Assets in `public` are served at the root path `/` during dev and copied to the root of the dist directory as-is (without hashing) during build. Used for `robots.txt`, `favicon.ico`.

### Q17: How do you optimize a Webpack production build?

**Difficulty: Advanced**

**Answer:**
Strategies include:

1.  **Minification:** `TerserPlugin` (JS), `CssMinimizerPlugin`.
2.  **Tree Shaking:** Ensure ES6 modules are used.
3.  **Code Splitting:** `SplitChunksPlugin` for vendor code.
4.  **Lazy Loading:** Dynamic imports.
5.  **Compression:** `CompressionPlugin` (Gzip).
6.  **Caching:** Use content hashes.

### Q18: What is "transpilation" and why do we need it?

**Difficulty: Easy**

**Answer:**
Transpilation is source-to-source compilation. We need it (via Babel, TypeScript) to run modern JavaScript syntax (ES6+) in older environments that don't support those features yet.

### Q19: How does Babel use Presets?

**Difficulty: Medium**

**Answer:**
Babel Presets are pre-determined sets of plugins.

- `@babel/preset-env`: Smart preset for latest JavaScript.
- `@babel/preset-react`: For React JSX.
- `@babel/preset-typescript`: For TypeScript.

### Q20: Can you use Webpack plugins in Vite?

**Difficulty: Advanced**

**Answer:**
Generally, no. Vite uses Rollup for production builds, so it is compatible with Rollup plugins. Webpack plugins are specific to Webpack. However, there are compatibility layers or equivalent plugins for Vite.

### Q21: What is the Webpack `DefinePlugin`?

**Difficulty: Medium**

**Answer:**
The `DefinePlugin` allows you to create global constants which can be configured at compile time. This is often used for environment variables (e.g., `process.env.NODE_ENV`).

```javascript
new webpack.DefinePlugin({
  "process.env.NODE_ENV": JSON.stringify("production"),
});
```

### Q22: How do you resolve file extensions in Webpack?

**Difficulty: Easy**

**Answer:**
Using the `resolve.extensions` option in configuration.

```javascript
resolve: {
  extensions: [".js", ".jsx", ".ts", ".tsx"];
}
```

This allows importing files without specifying their extension (e.g., `import App from './App'`).

### Q23: What are Webpack Aliases?

**Difficulty: Easy**

**Answer:**
Aliases allow you to create shortcuts for import paths, making imports cleaner and avoiding long relative paths like `../../../../utils`.

```javascript
resolve: {
  alias: {
    '@components': path.resolve(__dirname, 'src/components/')
  }
}
```

### Q24: How do you analyze bundle size in Webpack?

**Difficulty: Medium**

**Answer:**
Using the `webpack-bundle-analyzer` plugin. It creates an interactive treemap visualization of the contents of all your bundles, helping you identify large libraries.

### Q25: What is the `clean-webpack-plugin` (or `output.clean`)?

**Difficulty: Easy**

**Answer:**
It removes/cleans your build folder (e.g., `dist`) before each build, ensuring that only the files from the latest build are present and no old/unused files remain. In Webpack 5, you can simply use `output: { clean: true }`.

### Q26: Explain `babel-loader`.

**Difficulty: Easy**

**Answer:**
`babel-loader` is the Webpack loader that allows transpiling JavaScript files using Babel and Webpack. It acts as the bridge between Webpack and Babel.

### Q27: What is the difference between `babel.config.js` and `.babelrc`?

**Difficulty: Medium**

**Answer:**

- **`babel.config.js`**: Project-wide configuration. Recommended for monorepos.
- **`.babelrc`**: File-relative configuration. Applies only to files in its directory or subdirectories.

### Q28: In what order do Babel plugins and presets run?

**Difficulty: Advanced**

**Answer:**

1. Plugins run before Presets.
2. Plugins run first to last (array order).
3. Presets run last to first (reverse array order).

### Q29: What is `core-js`?

**Difficulty: Medium**

**Answer:**
`core-js` is a modular standard library for JavaScript. It includes polyfills for ECMAScript features (promises, symbols, collections, iterators, etc.). It is the underlying polyfill library used by Babel.

### Q30: How does Vite handle static assets?

**Difficulty: Easy**

**Answer:**
Importing a static asset (image, font) returns the resolved public URL.

```javascript
import imgUrl from "./img.png";
document.getElementById("hero").src = imgUrl;
```

Vite also supports URL queries like `?url` (force URL) or `?raw` (load as string).

### Q31: What is Vite's "Library Mode"?

**Difficulty: Medium**

**Answer:**
Library mode configures Vite to build a library (package) instead of an application. It bundles the code into formats suitable for distribution (ESM and UMD) and allows externalizing dependencies (like React/Vue) so they aren't bundled in.

### Q32: What is Dependency Pre-Bundling in Vite?

**Difficulty: Advanced**

**Answer:**
When you start the dev server, Vite crawls your source code to find dependencies (in `node_modules`). It converts CommonJS/UMD modules to ESM and bundles them using **esbuild**. This improves performance by reducing HTTP requests (combining hundreds of files into one) and ensuring ESM compatibility.

### Q33: How do you use Glob Imports in Vite?

**Difficulty: Medium**

**Answer:**
Vite supports `import.meta.glob` to import multiple modules from the file system.

```javascript
const modules = import.meta.glob("./dir/*.js");
```

### Q34: What is `vite.config.js`?

**Difficulty: Easy**

**Answer:**
It is the configuration file for Vite. It resolves the configuration object, allowing you to configure plugins, build options, server options, and aliases. It supports TypeScript (`vite.config.ts`) out of the box.

### Q35: Does Vite support Server-Side Rendering (SSR)?

**Difficulty: Advanced**

**Answer:**
Yes, Vite provides APIs to load modules in Node.js efficiently, enabling SSR frameworks (like Nuxt, SvelteKit, Remix) to use Vite. It doesn't provide full SSR out of the box but provides the primitives to build it.

### Q36: What is the `CopyWebpackPlugin` used for?

**Difficulty: Easy**

**Answer:**
It copies individual files or entire directories to the build directory (e.g., copying static assets that aren't imported in JS code).

### Q37: What is "Scope Hoisting" in Webpack?

**Difficulty: Advanced**

**Answer:**
Scope Hoisting (Module Concatenation) detects where modules can be concatenated into a single closure. This results in faster code execution in the browser and smaller bundle size by reducing function closure overhead.

### Q38: What is the `sideEffects` flag in `package.json`?

**Difficulty: Advanced**

**Answer:**
It allows packages to hint to bundlers that the files inside the package are "pure" (no side effects like modifying global window). If a file is marked as having no side effects, the bundler can safely skip importing it if none of its exports are used (aiding Tree Shaking).

### Q39: How do you configure a proxy in Vite/Webpack dev server?

**Difficulty: Medium**

**Answer:**
To avoid CORS issues during development, you can proxy API requests.
**Vite:**

```javascript
server: { proxy: { '/api': 'http://localhost:5000' } }
```

**Webpack:**

```javascript
devServer: { proxy: { '/api': 'http://localhost:5000' } }
```

### Q40: What is the difference between `hash`, `chunkhash`, and `contenthash` in Webpack?

**Difficulty: Advanced**

**Answer:**

- **`hash`**: Generated for the entire build. If one file changes, all hashes change.
- **`chunkhash`**: Based on the chunk's content (including dependencies).
- **`contenthash`**: Based solely on the content of the file itself (best for caching).

### Q41: What is SWC and how does it relate to Babel?

**Difficulty: Medium**

**Answer:**
SWC (Speedy Web Compiler) is an extensible Rust-based platform for the next generation of fast developer tools. It is a faster alternative to Babel for transpiling and compiling JavaScript/TypeScript. Next.js uses it by default.

### Q42: What is esbuild?

**Difficulty: Medium**

**Answer:**
esbuild is an extremely fast JavaScript bundler and minifier written in Go. Vite uses it for dependency pre-bundling and TS/JSX transpilation during development. It is 10-100x faster than JS-based tools.

### Q43: How do you handle TypeScript in Webpack?

**Difficulty: Medium**

**Answer:**
Typically using `ts-loader` (uses `tsc`, slower, type checks) or `@babel/preset-typescript` (faster, no type checking during build).

### Q44: How do you handle TypeScript in Vite?

**Difficulty: Medium**

**Answer:**
Vite supports TypeScript out of the box using esbuild for transpilation (stripping types). It does _not_ perform type checking. You should run `tsc --noEmit` in a separate process or as a pre-commit hook for type checking.

### Q45: What is Differential Loading?

**Difficulty: Advanced**

**Answer:**
A strategy where you serve two bundles:

1. Modern bundle (ES2015+) for modern browsers (smaller, faster).
2. Legacy bundle (ES5 with polyfills) for older browsers.
   Browsers choose which to load using `<script type="module">` and `<script nomodule>`.

### Q46: What is the `@babel/plugin-transform-runtime`?

**Difficulty: Advanced**

**Answer:**
It reuses Babel's injected helper code to save on codesize. Instead of injecting helper functions (like `_classCallCheck`) into every file, it imports them from `@babel/runtime`.

### Q47: How do you enable HMR in Webpack manually?

**Difficulty: Advanced**

**Answer:**
Using `module.hot`.

```javascript
if (module.hot) {
  module.hot.accept("./print.js", function () {
    console.log("Accepting the updated printMe module!");
    printMe();
  });
}
```

Most frameworks (React/Vue) have loaders that handle this automatically.

### Q48: What is the `MiniCssExtractPlugin`?

**Difficulty: Medium**

**Answer:**
This plugin extracts CSS into separate files (e.g., `main.css`). It creates a CSS file per JS file which contains CSS. It is preferred for production builds over `style-loader` (which injects CSS into style tags).

### Q49: How does Vite handle JSON files?

**Difficulty: Easy**

**Answer:**
JSON files can be directly imported. Also supports named imports:

```javascript
import { field } from "./data.json";
```

### Q50: What is the `resolve.modules` configuration in Webpack?

**Difficulty: Medium**

**Answer:**
It tells Webpack what directories should be searched when resolving modules. Default is `['node_modules']`. You can add custom directories here.

### Q51: What is the purpose of `html-webpack-plugin`?

**Difficulty: Easy**

**Answer:**
It simplifies the creation of HTML files to serve your webpack bundles. It automatically injects the script tags for your generated bundles (with hashes) into the HTML file.

### Q52: How do you load images in Webpack 5?

**Difficulty: Medium**

**Answer:**
Using Asset Modules (no longer need `file-loader` or `url-loader`).

```javascript
module: {
  rules: [{ test: /\.(png|jpg)$/, type: "asset/resource" }];
}
```

### Q53: What are "Asset Modules" in Webpack 5?

**Difficulty: Medium**

**Answer:**
Built-in replacement for `file-loader`, `url-loader`, and `raw-loader`.

- `asset/resource`: Emits a separate file.
- `asset/inline`: Exports a data URI.
- `asset/source`: Exports the source code.
- `asset`: Automatically chooses between resource and inline based on size.

### Q54: How do you debug a slow Webpack build?

**Difficulty: Advanced**

**Answer:**

1. Use `speed-measure-webpack-plugin` to see per-plugin/loader timing.
2. Use `webpack-bundle-analyzer` to check for duplicates or large libs.
3. Check if Source Maps are too expensive (e.g., `source-map` vs `eval-cheap-module-source-map`).

### Q55: What is `vite preview` command?

**Difficulty: Easy**

**Answer:**
`vite preview` boots up a local static web server that serves the files from `dist` (production build). It's used to verify the production build locally before deploying.

### Q56: How does Vite handle `.vue` or `.svelte` files?

**Difficulty: Medium**

**Answer:**
Vite has official plugins (`@vitejs/plugin-vue`, `@sveltejs/vite-plugin-svelte`) that handle the parsing and compilation of these frameworks' Single File Components (SFCs) into JS.

### Q57: What is the Rollup bundler?

**Difficulty: Medium**

**Answer:**
Rollup is a module bundler for JavaScript which compiles small pieces of code into something larger/more complex. It pioneered Tree Shaking and ESM support. It is the underlying bundler for Vite's production build.

### Q58: Why is Rollup often preferred for libraries over Webpack?

**Difficulty: Advanced**

**Answer:**
Rollup generally produces smaller, cleaner bundles with less runtime overhead (wrappers) than Webpack. It is better at handling ESM output, which is crucial for libraries.

### Q59: What is Parcel?

**Difficulty: Easy**

**Answer:**
Parcel is another web application bundler known for being "zero configuration". It works out of the box for most file types without a config file.

### Q60: What is "Zero Config" in build tools?

**Difficulty: Easy**

**Answer:**
The philosophy that tools should work with standard defaults without requiring a complex setup file. Vite and Parcel adhere to this, whereas Webpack often requires explicit configuration.

### Q61: How do you inject global variables in Webpack?

**Difficulty: Medium**

**Answer:**
Using `ProvidePlugin`. It automatically loads modules instead of having to `import` or `require` them everywhere.

```javascript
new webpack.ProvidePlugin({
  $: "jquery",
});
```

### Q62: What is the `target` option in Webpack?

**Difficulty: Medium**

**Answer:**
It instructs Webpack to compile for a specific environment (e.g., `web`, `node`, `electron-renderer`). Defaults to `web`.

### Q63: How to handle CSS Preprocessors (Sass/Less) in Webpack?

**Difficulty: Easy**

**Answer:**
Chain loaders: `sass-loader` (compiles Sass to CSS) -> `css-loader` (resolves imports) -> `style-loader` (injects CSS).

### Q64: What is PostCSS?

**Difficulty: Medium**

**Answer:**
PostCSS is a tool for transforming CSS with JavaScript. It is often used for Autoprefixing, linting, and using future CSS syntax today.

### Q65: How do you use PostCSS with Vite?

**Difficulty: Medium**

**Answer:**
Vite automatically applies PostCSS if a `postcss.config.js` file is present in the project root.

### Q66: What is `autoprefixer`?

**Difficulty: Easy**

**Answer:**
A PostCSS plugin that parses your CSS and adds vendor prefixes to CSS rules using values from Can I Use.

### Q67: How do you exclude `node_modules` from Babel transformation?

**Difficulty: Easy**

**Answer:**
In Webpack config:

```javascript
rule: {
  test: /\.js$/,
  exclude: /node_modules/,
  use: 'babel-loader'
}
```

This is critical for build performance.

### Q68: What is `babel-node`?

**Difficulty: Medium**

**Answer:**
A CLI that works exactly like the Node.js CLI but compiles the code with Babel presets and plugins before running it. Not recommended for production (slow).

### Q69: What is the AST (Abstract Syntax Tree)?

**Difficulty: Advanced**

**Answer:**
AST is a tree representation of the abstract syntactic structure of source code. Babel (and ESLint, Prettier) parses code into AST, traverses/modifies the nodes, and generates code back.

### Q70: Can Babel parse TypeScript?

**Difficulty: Medium**

**Answer:**
Yes, with `@babel/preset-typescript`, Babel can parse and strip TypeScript types, converting it to JS. However, it does **not** check types.

### Q71: What is the difference between `Babel` and `TypeScript` compiler (`tsc`)?

**Difficulty: Medium**

**Answer:**

- **`tsc`:** Compiles TS to JS AND checks types.
- **Babel:** Compiles TS to JS (faster, more flexible plugins) but does NOT check types.

### Q72: How do you create a custom Webpack loader?

**Difficulty: Advanced**

**Answer:**
A loader is a Node.js function that takes the source of a file as input and returns the transformed source.

```javascript
module.exports = function (source) {
  return source.replace(/foo/g, "bar");
};
```

### Q73: How do you create a custom Webpack plugin?

**Difficulty: Advanced**

**Answer:**
A plugin is a class with an `apply` method. It hooks into Webpack's event system (Tapable).

```javascript
class MyPlugin {
  apply(compiler) {
    compiler.hooks.done.tap('MyPlugin', stats => { ... });
  }
}
```

### Q74: What is `webpack-dev-server`?

**Difficulty: Easy**

**Answer:**
A development server that provides live reloading. It keeps bundles in memory (RAM) instead of writing to disk for speed.

### Q75: How do you handle "Magic Comments" in Webpack?

**Difficulty: Medium**

**Answer:**
Inline comments to configure dynamic imports.

```javascript
import(
  /* webpackChunkName: "my-chunk-name" */
  /* webpackPrefetch: true */
  "./module"
);
```

### Q76: What is Prefetching and Preloading in Webpack?

**Difficulty: Advanced**

**Answer:**

- **Prefetch:** Fetch in background when browser is idle (for future navigation).
- **Preload:** Fetch ASAP (for current navigation).

### Q77: How does Webpack handle circular dependencies?

**Difficulty: Advanced**

**Answer:**
Webpack allows circular dependencies but the module execution order matters. If a module accesses an import that hasn't finished executing, it might get `undefined`. `circular-dependency-plugin` helps detect them.

### Q78: What is the `DLLPlugin` in Webpack?

**Difficulty: Advanced**

**Answer:**
Used to bundle vendor libraries separately in a way that they don't need to be rebuilt every time. It was a major optimization technique in Webpack 4.

### Q79: Why is `DLLPlugin` less relevant in Webpack 5/Vite?

**Difficulty: Advanced**

**Answer:**
Webpack 5 has better caching (Persistent Caching) and Vite uses esbuild pre-bundling, making the complexity of `DLLPlugin` unnecessary for performance.

### Q80: How do you measure build performance in Vite?

**Difficulty: Medium**

**Answer:**
Vite uses `debug` module. You can run `DEBUG=vite:perf vite build` to see performance metrics. Or use the rollup-plugin-visualizer.

### Q81: What is the `legacy` plugin in Vite?

**Difficulty: Medium**

**Answer:**
`@vitejs/plugin-legacy` automatically generates legacy chunks and corresponding ES5 polyfills for older browsers that don't support native ESM.

### Q82: How do you deploy a Vite app to GitHub Pages?

**Difficulty: Medium**

**Answer:**

1. Set `base: '/repo-name/'` in `vite.config.js`.
2. Build (`vite build`).
3. Push the `dist` folder to the `gh-pages` branch.

### Q83: What is the `base` config option in Vite?

**Difficulty: Easy**

**Answer:**
It sets the base public path when serving the app in development or production (e.g., if your app is hosted at `http://my-app.com/blog/`, base should be `/blog/`).

### Q84: How do you implement Critical CSS extraction?

**Difficulty: Advanced**

**Answer:**
Tools like `critters` or `critical` can be integrated into the build pipeline (Webpack plugin or post-build script) to inline the CSS required for above-the-fold content into the HTML.

### Q85: What is the difference between `module.exports` and `export default`?

**Difficulty: Easy**

**Answer:**

- **`module.exports`**: CommonJS (Node.js standard).
- **`export default`**: ES Modules (Modern JS standard).
  Build tools handle interoperability, but ESM is the future.

### Q86: How does Webpack resolve `import` statements?

**Difficulty: Medium**

**Answer:**
It uses the `enhanced-resolve` library. It checks resolve config (extensions, aliases, modules directories), looks at `package.json` (`main`, `module`, `exports` fields), and finds the file.

### Q87: What is the `externals` configuration in Webpack?

**Difficulty: Medium**

**Answer:**
It allows you to exclude dependencies from the output bundles. Instead, the created bundle relies on that dependency to be present in the consumer's environment (e.g., via CDN script tag).

### Q88: How do you remove console logs in production build?

**Difficulty: Easy**

**Answer:**
In Webpack (TerserPlugin) or Vite (esbuild/terser options), you can set `compress: { drop_console: true }`.

### Q89: What is `webpack-merge`?

**Difficulty: Easy**

**Answer:**
A utility to merge Webpack configuration objects. Common pattern: `webpack.common.js`, `webpack.dev.js`, `webpack.prod.js`, and merge them.

### Q90: How do you setup ESLint with Vite/Webpack?

**Difficulty: Medium**

**Answer:**

- **Webpack:** Use `eslint-webpack-plugin`.
- **Vite:** Use `vite-plugin-eslint`.
  However, modern trend is to run ESLint separately or in the IDE, not slowing down the bundler.

### Q91: What is Turbopack?

**Difficulty: Advanced**

**Answer:**
Turbopack is an incremental bundler optimized for JavaScript and TypeScript, written in Rust by the creators of Webpack and Next.js. It aims to be the successor to Webpack with vastly better performance.

### Q92: What is the difference between Bundling and Compiling?

**Difficulty: Medium**

**Answer:**

- **Compiling (Transpiling):** Transforming code syntax (e.g., TS -> JS, ES6 -> ES5). Files map 1:1.
- **Bundling:** Combining multiple files and assets into a single (or few) distributable files.

### Q93: How do you handle caching in Webpack?

**Difficulty: Medium**

**Answer:**
Webpack 5 introduced File System Cache (Persistent Caching).

```javascript
cache: {
  type: 'filesystem',
}
```

This stores the build cache to disk, making secondary builds extremely fast.

### Q94: What are "Runtime Chunks" in Webpack?

**Difficulty: Advanced**

**Answer:**
The runtime chunk contains the boilerplate code Webpack needs to resolve and load modules. Extracting it (`optimization.runtimeChunk: 'single'`) prevents vendor chunks from invalidating hash when only app code changes.

### Q95: How does Vite handle Web Workers?

**Difficulty: Advanced**

**Answer:**
Vite supports importing web workers with the `?worker` suffix.

```javascript
import MyWorker from "./worker?worker";
const worker = new MyWorker();
```

### Q96: What is the `optimizeDeps` option in Vite?

**Difficulty: Advanced**

**Answer:**
Configuration for the dependency pre-bundling process. You can manually `include` or `exclude` dependencies from pre-bundling here.

### Q97: How do you debug Vite HMR issues?

**Difficulty: Advanced**

**Answer:**
Vite logs HMR events in the browser console. You can enable debug logging for HMR in the client or server to see what updates are being sent and why they might fail (causing a full reload).

### Q98: What is the `babel-plugin-macros`?

**Difficulty: Advanced**

**Answer:**
A plugin that allows you to use libraries that perform build-time transformations without adding a new plugin to your babel config (e.g., `styled-components`, `polished`).

### Q99: How do you customize the output directory in Vite?

**Difficulty: Easy**

**Answer:**
Using `build.outDir` in `vite.config.js`. Default is `dist`.

### Q100: What is the future of frontend build tools?

**Difficulty: Easy**

**Answer:**
The trend is moving towards native languages (Rust/Go) for performance (swc, esbuild, Turbopack) and unbundled development (Vite) for better developer experience. Complexity is being abstracted away into "zero-config" tools.
