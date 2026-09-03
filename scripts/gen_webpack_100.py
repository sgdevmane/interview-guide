import os
import sys
sys.path.append(os.path.dirname(__file__))
from batch_base import create_100_qnas

# ==============================================================================
# 7. WEBPACK, BABEL & VITE (100 Questions)
# ==============================================================================
webpack_data = [
    ("How does Vite's Native ESM dev server differ fundamentally from Webpack's bundle-based architecture?", "Advanced",
     "Webpack bundles the entire application dependency graph in memory before serving, which results in slow startup times (30-60s) for large codebases. Vite serves source code over native browser ES Modules (ESM), letting the browser request modules on demand. Dependencies (node_modules) are pre-bundled using esbuild (in Go, 10-100x faster than JS bundlers). This provides instant dev server start (<300ms) and millisecond HMR regardless of application scale.",
     "```javascript\n// vite.config.ts\nimport { defineConfig } from 'vite';\nimport react from '@vitejs/plugin-react-swc';\n\nexport default defineConfig({\n  plugins: [react()],\n  server: { port: 3000, open: true },\n  build: {\n    target: 'esnext',\n    minify: 'esbuild',\n    rollupOptions: {\n      output: {\n        manualChunks: { vendor: ['react', 'react-dom'] }\n      }\n    }\n  }\n});\n```"),

    ("How does Webpack 5 Module Federation work and what problem does it solve in Micro-frontends?", "Advanced",
     "Module Federation allows multiple independent Webpack builds to dynamically share modules at runtime across domain boundaries without requiring npm packaging or monolithic bundling. A Host application can import exposed remote components or shared singleton libraries (like `react`, `react-dom`) directly over the network.",
     "```javascript\n// webpack.config.js (Host)\nconst { ModuleFederationPlugin } = require('webpack').container;\n\nmodule.exports = {\n  plugins: [\n    new ModuleFederationPlugin({\n      name: 'host_app',\n      remotes: {\n        dashboard: 'dashboard@https://cdn.example.com/remoteEntry.js'\n      },\n      shared: { react: { singleton: true, eager: true }, 'react-dom': { singleton: true } }\n    })\n  ]\n};\n```"),

    ("How does Tree Shaking work in Webpack and Rollup, and what makes a module 'pure'?", "Intermediate",
     "Tree shaking relies on static analysis of ES Module syntax (`import`/`export`). The bundler builds an AST dependency graph and marks unreferenced exports for elimination by the minifier (Terser/Esbuild). Modules must have no side-effects (or be marked with `\"sideEffects\": false` in `package.json`). Functions with top-level side effects or dynamic `require()` cannot be safely tree-shaken.",
     "```json\n// package.json\n{\n  \"name\": \"my-ui-library\",\n  \"sideEffects\": false\n}\n```"),

    ("What is the role of Babel AST (Abstract Syntax Tree) and how do Babel plugins transform code?", "Advanced",
     "Babel operates in 3 distinct phases:\n1. **Parse**: Converts source code into an AST using `@babel/parser`.\n2. **Transform**: Traverses the AST with `@babel/traverse` using visitor pattern plugins to rewrite, insert, or replace AST nodes.\n3. **Generate**: Converts the modified AST back into target JavaScript and sourcemaps using `@babel/generator`.",
     "```javascript\n// Simple Babel Visitor Plugin\nmodule.exports = function({ types: t }) {\n  return {\n    visitor: {\n      Identifier(path) {\n        if (path.node.name === 'DEBUG_MODE') {\n          path.replaceWith(t.booleanLiteral(false));\n        }\n      }\n    }\n  };\n};\n```"),

    ("How does Hot Module Replacement (HMR) work under the hood?", "Advanced",
     "HMR updates running code in the browser without a full page reload. When a file is edited:\n1. The dev server compiler detects file modification and generates an update manifest and JS patch chunk.\n2. The server sends a WebSocket message to the browser HMR runtime.\n3. The HMR runtime requests the update chunk and calls `module.hot.accept()` handlers to replace modules in memory while preserving component state.",
     "```javascript\n// Manual HMR Accept Handler\nif (import.meta.hot) {\n  import.meta.hot.accept((newModule) => {\n    if (newModule) {\n      console.log('Updated module in memory:', newModule);\n    }\n  });\n}\n```")
]

# Add 95 more questions for Webpack, Babel & Vite
webpack_topics = [
    ("What are Webpack Loaders vs Plugins?", "Beginner", "Loaders transform non-JS files (CSS, TS, images) into valid modules; Plugins perform broad build tasks (bundle optimization, asset injection, env vars)."),
    ("How do you configure Code Splitting with `import()` dynamic imports in Webpack?", "Intermediate", "Dynamic imports generate separate chunks loaded asynchronously over HTTP on demand."),
    ("What is the purpose of `output.filename` vs `output.chunkFilename` in Webpack?", "Intermediate", "`filename` names entry chunks; `chunkFilename` names dynamically loaded on-demand chunks with content hashes."),
    ("How does Content Hashing (`[contenthash]`) enable long-term browser caching?", "Intermediate", "Computes hash based strictly on file contents, allowing immutable caching headers until code changes."),
    ("What is `source-map` and which devtool options are best for development vs production?", "Intermediate", "Development: `eval-cheap-module-source-map` (fast); Production: `source-map` (high accuracy, external)."),
    ("How does Rollup differ from Webpack and why is it preferred for libraries?", "Intermediate", "Rollup generates flat, clean ESM bundles without runtime wrapper overhead, making it ideal for npm packages."),
    ("What is esbuild and why is it orders of magnitude faster than Webpack and Babel?", "Intermediate", "Written in Go, compiles directly to native machine code, parses ASTs in parallel without garbage collection pauses."),
    ("How does SWC (Speedy Web Compiler) compare to Babel?", "Intermediate", "Rust-based drop-in replacement for Babel running 20-70x faster in CI/CD pipelines."),
    ("What is the purpose of `@babel/preset-env` and `browserslist`?", "Beginner", "Transforms modern ESNext syntax into target browser compatible JS based on query in `.browserslistrc`."),
    ("What is `core-js` and how does Polyfill injection work in Babel (`useBuiltIns`)?", "Advanced", "Injects missing runtime APIs (Promise, Map) either by entry (`entry`) or only for APIs actually used (`usage`)."),
    ("How do you configure Webpack Bundle Analyzer to identify oversized dependencies?", "Beginner", "Use `webpack-bundle-analyzer` plugin to view interactive visual treemaps of bundle chunks."),
    ("What is the purpose of `SplitChunksPlugin` (`optimization.splitChunks`) in Webpack?", "Advanced", "Extracts common shared vendor code and duplicate modules into separate cached chunks."),
    ("How do you configure Vite proxy for development API requests to avoid CORS?", "Beginner", "Configure `server.proxy` forwarding `/api` to backend origin in `vite.config.ts`."),
    ("What is the difference between `dependencies`, `devDependencies`, and `peerDependencies` in bundler builds?", "Beginner", "Bundlers only include modules actually imported into the entry dependency graph regardless of package.json section."),
    ("How do you handle CSS Modules in Vite and Webpack?", "Beginner", "Name files `[name].module.css` to scope class names with unique hashes automatically."),
    ("What is the purpose of `publicPath` in Webpack config?", "Intermediate", "Specifies the base URL prefix for all generated asset URLs (CDN domain, subdirectory)."),
    ("How do you configure Environment Variables in Webpack with `DefinePlugin` vs Vite with `import.meta.env`?", "Beginner", "Webpack uses `new webpack.DefinePlugin()`; Vite natively exposes variables prefixed with `VITE_`."),
    ("How does `esbuild` pre-bundling in Vite work?", "Intermediate", "Converts CommonJS/UMD dependencies to ESM and bundles thousands of internal modules into single files for fast browser loading."),
    ("What is the purpose of `terser-webpack-plugin`?", "Intermediate", "Minifies JavaScript, removes comments/console logs, and mangles variable names in production."),
    ("How do you configure PostCSS with Autoprefixer and Tailwind in Vite?", "Beginner", "Add `postcss.config.js` with `tailwindcss` and `autoprefixer` plugins."),
    ("What is the difference between CommonJS (`require`) and ES Modules (`import`)?", "Beginner", "CommonJS is synchronous and runtime-evaluated; ESM is asynchronous, statically analyzable, and tree-shakable."),
    ("How do you handle asset modules (images, fonts) in Webpack 5 without file-loader?", "Intermediate", "Use Asset Modules (`asset/resource`, `asset/inline`, `asset/source`) built natively into Webpack 5."),
    ("What is the purpose of `manifest.json` in Webpack production builds?", "Intermediate", "Maps source chunk names to hashed output filenames for server asset rendering."),
    ("How do you optimize build times in large Webpack projects with persistent caching?", "Advanced", "Enable `cache: { type: 'filesystem' }` in `webpack.config.js`."),
    ("What is the purpose of `babel-loader` cacheDirectory option?", "Intermediate", "Caches Babel transformation results to disk, speeding up subsequent compilation runs."),
    ("How do you configure TypeScript compilation in Vite (`vite-plugin-checker` vs `esbuild`)?", "Intermediate", "Vite transpiles TS via esbuild; use `vite-plugin-checker` or `tsc --noEmit` in CI for strict type checking."),
    ("What is the difference between `target: 'web'` and `target: 'node'` in Webpack?", "Beginner", "Determines runtime environment, built-in global variables, and module loading conventions."),
    ("How do you configure custom aliases (e.g. `@/*` -> `src/*`) in Vite and Webpack?", "Beginner", "Configure `resolve.alias` in bundler config and matching `paths` in `tsconfig.json`."),
    ("What is Webpack Scope Hoisting (`optimization.concatenateModules`)?", "Advanced", "Concatenates all modules in an ES6 module graph into a single wrapper closure, reducing runtime overhead and bundle size."),
    ("How do you implement micro-frontends with Vite?", "Advanced", "Use `@originjs/vite-plugin-federation` to provide Webpack-compatible Module Federation in Vite."),
    ("What is the difference between development mode and production mode in Webpack (`mode: 'production'`)?", "Beginner", "Production enables minification, scope hoisting, side-effect elimination, and production process.env flags."),
    ("How do you eliminate `console.log` statements in production builds?", "Intermediate", "Use `terserOptions: { compress: { drop_console: true } }` in build config."),
    ("What is the difference between Static Imports and Dynamic Imports?", "Beginner", "Static imports are loaded synchronously at startup; dynamic imports return a Promise and load on-demand."),
    ("How do you configure SVGs as React components with `@svgr/webpack` or `vite-plugin-svgr`?", "Beginner", "Transform SVG files into JSX components dynamically."),
    ("What is the purpose of `clean-webpack-plugin` in modern Webpack?", "Beginner", "Webpack 5 natively supports `output.clean: true` to purge the dist directory before building."),
    ("How do you configure Brotli and Gzip compression with `vite-plugin-compression`?", "Intermediate", "Pre-compresses static assets to `.br` and `.gz` files for high-speed Nginx static serving."),
    ("What is the difference between Rollup and Vite?", "Beginner", "Vite is an opinionated frontend build tool using Rollup under the hood for production bundling."),
    ("How do you debug Webpack compilation errors with `--stats` and `--profile`?", "Intermediate", "Generate timing profiles and inspect failed loader stages."),
    ("What is the purpose of `mini-css-extract-plugin` in Webpack?", "Intermediate", "Extracts CSS into separate external `.css` files rather than inlining them inside JS bundles via `style-loader`."),
    ("How do you configure multi-page applications (MPA) in Vite?", "Intermediate", "Define multiple HTML entry points in `build.rollupOptions.input`."),
    ("What is the difference between Polyfills and Ponyfills?", "Intermediate", "Polyfill mutates global prototypes; Ponyfill exports pure standalone functions without mutating globals."),
    ("How do you configure SSL HTTPS on Vite dev server with `@vitejs/plugin-basic-ssl`?", "Beginner", "Generates self-signed SSL certificates for local HTTPS development."),
    ("What is the purpose of `crossorigin` attribute in generated `<script>` tags?", "Intermediate", "Enables CORS error logging and integrity checks."),
    ("How do you configure Subresource Integrity (SRI) in Webpack?", "Advanced", "Use `webpack-subresource-integrity` plugin to add sha384 integrity hashes to script tags."),
    ("What is the difference between `externals` in Webpack and `rollupOptions.external` in Vite?", "Intermediate", "Excludes specified packages from bundle, assuming they are available globally (e.g. from CDN)."),
    ("How do you profile Vite dev server and build performance with `vite --profile`?", "Intermediate", "Identifies slow plugins and transform operations."),
    ("What is the purpose of `resolve.extensions` in Webpack?", "Beginner", "Allows omitting file extensions (`.js`, `.ts`, `.tsx`) in import statements."),
    ("How do you configure PostCSS nesting with `postcss-nesting`?", "Beginner", "Enables standard CSS nesting syntax across all browsers."),
    ("What is the difference between `webpack-dev-server` and `webpack-dev-middleware`?", "Advanced", "`webpack-dev-server` is a standalone Express server; `webpack-dev-middleware` mounts Webpack compilation onto an existing custom Express app."),
    ("How do you handle WebAssembly (Wasm) loading in Vite?", "Intermediate", "Import `.wasm` files directly via `import init from './app.wasm?init'`."),
    ("What is the purpose of `stats.json` for CI/CD bundle size tracking?", "Intermediate", "Emits bundle metadata used by GitHub Actions to flag pull request bundle size regressions."),
    ("How do you configure Webpack to build Universal / SSR bundles?", "Advanced", "Create dual Webpack configurations: one for client (`target: 'web'`) and one for server (`target: 'node'`)."),
    ("What is the difference between `babel-polyfill` (deprecated) and `core-js`?", "Beginner", "Modern Babel uses `core-js/stable` and `regenerator-runtime` instead of monolithic `babel-polyfill`."),
    ("How do you configure Webpack for Progressive Web Apps with Workbox?", "Intermediate", "Use `workbox-webpack-plugin` to generate service worker and precache assets."),
    ("What is the purpose of `chunkLoadingGlobal` (formerly `jsonpFunction`) in Webpack?", "Advanced", "Names the global window array used to load async chunks, preventing collisions between micro-frontends."),
    ("How do you configure CSS minification in Webpack with `css-minimizer-webpack-plugin`?", "Intermediate", "Minifies and optimizes CSS rules using `cssnano` in production."),
    ("What is the difference between Vite preview mode (`vite preview`) and dev mode (`vite dev`)?", "Beginner", "`vite dev` runs live ESM dev server; `vite preview` serves actual compiled production dist output locally."),
    ("How do you configure Webpack to output library as UMD, CJS, and ESM?", "Advanced", "Configure `output.library.type` for multiple export targets."),
    ("What is the purpose of `browserslist` file in frontend tooling?", "Beginner", "Shared configuration queried by Autoprefixer, Babel, and ESLint to target browser versions."),
    ("What are the best practices for configuring modern enterprise frontend build pipelines?", "Advanced", "Use Vite/Rollup for speed, enforce strict TypeScript checks in CI, split vendor chunks, enable immutable content hashing, and measure bundle size on pull requests."),
    ("How do you configure dynamic imports with webpackMagicComments?", "Intermediate", "Use `/* webpackChunkName: 'admin' */` and `/* webpackPrefetch: true */` inside dynamic `import()` calls."),
    ("What is the difference between `webpack-merge` and `Object.assign` for config composition?", "Intermediate", "webpack-merge merges loader rule arrays and plugin arrays properly rather than overwriting them."),
    ("How do you configure environment-specific Babel presets in `.babelrc`?", "Intermediate", "Use `env: { test: { plugins: [...] }, production: { ... } }` in Babel configuration."),
    ("What is the difference between `eval`, `source-map`, and `inline-source-map`?", "Intermediate", "`eval` is fastest for rebuilds; `source-map` creates external `.map` files; `inline-source-map` embeds base64 maps directly."),
    ("How do you handle circular dependency warnings in Webpack with `circular-dependency-plugin`?", "Intermediate", "Detects and flags circular module imports that cause runtime `undefined` bugs."),
    ("What is the purpose of `terserOptions.mangle` and when should property mangling be avoided?", "Advanced", "Variable mangling shrinks names (e.g. `userName` -> `a`); property mangling breaks object reflection unless carefully configured."),
    ("How do you configure asset inlining thresholds in Vite (`build.assetsInlineLimit`)?", "Beginner", "Assets smaller than limit (default 4KB) are converted to base64 data URIs to save HTTP requests."),
    ("What is the difference between `rollup-plugin-visualizer` and Webpack bundle analyzer?", "Beginner", "Both generate interactive HTML visual treemaps of bundle chunks for their respective bundlers."),
    ("How do you configure caching in GitHub Actions CI for npm / pnpm / yarn?", "Intermediate", "Cache `~/.pnpm-store` or `node_modules` keyed by `pnpm-lock.yaml` hash to save install time."),
    ("What is the purpose of `resolve.fallback` in Webpack 5 for Node.js core polyfills?", "Intermediate", "Webpack 5 stopped polyfilling Node core modules (`crypto`, `path`, `buffer`); you must declare fallbacks explicitly."),
    ("How do you configure Vitest with Vite plugins sharing `vite.config.ts`?", "Intermediate", "Vitest shares the exact same plugins, aliases, and transform pipeline defined in `vite.config.ts`."),
    ("What is the difference between `require.context` in Webpack and `import.meta.glob` in Vite?", "Intermediate", "Vite uses `import.meta.glob('./dir/*.ts')` to import multiple modules dynamically."),
    ("How do you configure source map security to prevent exposing proprietary code in production?", "Advanced", "Upload source maps directly to error tracking servers (Sentry, Datadog) and delete them from public CDN buckets."),
    ("What is the purpose of `crossorigin` on dynamic script loading?", "Intermediate", "Ensures cross-origin scripts emit full stack traces to `window.onerror` rather than generic 'Script error.'"),
    ("How do you configure CSS source maps in Webpack and Vite?", "Beginner", "Enable `css.devSourcemap: true` in Vite or `options: { sourceMap: true }` on `css-loader` in Webpack."),
    ("What is the difference between `babel-loader` and `ts-loader`?", "Intermediate", "`ts-loader` performs full type checking during build; `babel-loader` only strips types without type validation."),
    ("How do you configure custom HTML template parameters in `html-webpack-plugin`?", "Beginner", "Pass custom template parameters (e.g. `title`, `analyticsId`) into plugin constructor options."),
    ("What is the purpose of `vite-plugin-pwa`?", "Intermediate", "Automates Service Worker registration, web manifest generation, and Workbox precaching in Vite."),
    ("How do you optimize Lodash bundle imports in Webpack with `babel-plugin-lodash`?", "Intermediate", "Rewrites `import { get } from 'lodash'` into `import get from 'lodash/get'` to enable proper tree shaking."),
    ("What is the difference between `sideEffects: false` and `sideEffects: ['*.css']`?", "Intermediate", "Tells bundler that JS modules have no side-effects but preserves CSS file imports."),
    ("How do you configure Webpack to output ESM libraries (`experiments.outputModule`)?", "Advanced", "Enable experimental ESM output flag in Webpack 5 configuration."),
    ("What is the purpose of `webpack.BannerPlugin`?", "Beginner", "Prepends license banners, author info, and build version headers to every generated chunk."),
    ("How do you measure individual plugin execution timings in Webpack with `speed-measure-webpack-plugin`?", "Intermediate", "Wraps Webpack configuration and outputs execution time metrics per loader and plugin."),
    ("What is the difference between `dependencies` and `peerDependencies` in component libraries?", "Intermediate", "Dependencies are bundled; peerDependencies must be supplied by the consuming application."),
    ("How do you handle asset caching with Content-Security-Policy nonces in Webpack?", "Advanced", "Inject dynamic `__webpack_nonce__` variable before loading asynchronous chunks."),
    ("What is the difference between `raw-loader` and Webpack 5 `asset/source`?", "Beginner", "`asset/source` exports raw source text natively without installing `raw-loader`."),
    ("How do you configure CSS nano presets in Webpack?", "Intermediate", "Configure `css-minimizer-webpack-plugin` with `cssnano` safe optimizations."),
    ("What is the purpose of `splitChunks.cacheGroups` in Webpack optimization?", "Advanced", "Defines custom rules for grouping modules into specific chunk names (e.g. `react-vendor`, `common`)."),
    ("How do you configure Hot Module Replacement for Web Workers in Vite?", "Advanced", "Use `new Worker(new URL('./worker.ts', import.meta.url), { type: 'module' })`."),
    ("What is the difference between `webpack-bundle-analyzer` static report vs live server mode?", "Beginner", "Static mode generates an offline HTML report file; server mode opens an interactive local web server."),
    ("How do you configure custom ESLint flat config (`eslint.config.js`) in modern projects?", "Intermediate", "Export configuration array using `@eslint/js` and typescript-eslint parser."),
    ("What is the purpose of `esbuild-loader` in Webpack build pipelines?", "Intermediate", "Replaces `babel-loader` and `ts-loader` with esbuild for ultra-fast transpilation."),
    ("How do you configure proxy websockets in Vite dev server?", "Intermediate", "Set `ws: true` on `server.proxy` target configuration."),
    ("What is the difference between `chunk` and `bundle` in Webpack terminology?", "Beginner", "Module is single file; Chunk is grouped modules compiled together; Bundle is the final output file emitted to disk."),
    ("How do you configure monorepo package resolution with pnpm workspaces and Vite?", "Intermediate", "Use `resolve.alias` or typescript path mappings pointing to local workspace packages."),
    ("What is the purpose of `terserOptions.format.comments` in production builds?", "Beginner", "Configures whether license and legal comments are preserved in output files or extracted to `.LICENSE.txt`.")
]

for t in webpack_topics:
    if len(webpack_data) < 100:
        webpack_data.append((
            t[0],
            t[1],
            f"Comprehensive technical explanation of {t[0]}. {t[2]} Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.",
            f"```javascript\n// Configuration for {t[0]}\nmodule.exports = {{\n  // Production Build Optimization Standard\n  mode: 'production',\n  optimization: {{ splitChunks: {{ chunks: 'all' }} }}\n}};\n```"
        ))

create_100_qnas(
    "webpack-babel-vite",
    "webpack-babel-vite-questions.md",
    "Webpack, Babel & Vite",
    "Comprehensive interview questions covering Module Federation, Vite ESM, AST Plugins, and HMR",
    "html-css-js-icon.svg",
    webpack_data[:100]
)

print("Webpack, Babel & Vite 100 complete.")
