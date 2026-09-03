<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Webpack, Babel & Vite Logo" width="100" height="100">
  </a>
  <h1>Webpack, Babel & Vite Interview Questions & Answers</h1>
  <p><b>Comprehensive interview questions covering Module Federation, Vite ESM, AST Plugins, and HMR</b></p>
</div>

---

## Table of Contents

1. [How does Vite's Native ESM dev server differ fundamentally from Webpack's bundle-based architecture?](#q1) <span class="advanced">Advanced</span>
2. [How does Webpack 5 Module Federation work and what problem does it solve in Micro-frontends?](#q2) <span class="advanced">Advanced</span>
3. [How does Tree Shaking work in Webpack and Rollup, and what makes a module 'pure'?](#q3) <span class="intermediate">Intermediate</span>
4. [What is the role of Babel AST (Abstract Syntax Tree) and how do Babel plugins transform code?](#q4) <span class="advanced">Advanced</span>
5. [How does Hot Module Replacement (HMR) work under the hood?](#q5) <span class="advanced">Advanced</span>
6. [What are Webpack Loaders vs Plugins?](#q6) <span class="beginner">Beginner</span>
7. [How do you configure Code Splitting with `import()` dynamic imports in Webpack?](#q7) <span class="intermediate">Intermediate</span>
8. [What is the purpose of `output.filename` vs `output.chunkFilename` in Webpack?](#q8) <span class="intermediate">Intermediate</span>
9. [How does Content Hashing (`[contenthash]`) enable long-term browser caching?](#q9) <span class="intermediate">Intermediate</span>
10. [What is `source-map` and which devtool options are best for development vs production?](#q10) <span class="intermediate">Intermediate</span>
11. [How does Rollup differ from Webpack and why is it preferred for libraries?](#q11) <span class="intermediate">Intermediate</span>
12. [What is esbuild and why is it orders of magnitude faster than Webpack and Babel?](#q12) <span class="intermediate">Intermediate</span>
13. [How does SWC (Speedy Web Compiler) compare to Babel?](#q13) <span class="intermediate">Intermediate</span>
14. [What is the purpose of `@babel/preset-env` and `browserslist`?](#q14) <span class="beginner">Beginner</span>
15. [What is `core-js` and how does Polyfill injection work in Babel (`useBuiltIns`)?](#q15) <span class="advanced">Advanced</span>
16. [How do you configure Webpack Bundle Analyzer to identify oversized dependencies?](#q16) <span class="beginner">Beginner</span>
17. [What is the purpose of `SplitChunksPlugin` (`optimization.splitChunks`) in Webpack?](#q17) <span class="advanced">Advanced</span>
18. [How do you configure Vite proxy for development API requests to avoid CORS?](#q18) <span class="beginner">Beginner</span>
19. [What is the difference between `dependencies`, `devDependencies`, and `peerDependencies` in bundler builds?](#q19) <span class="beginner">Beginner</span>
20. [How do you handle CSS Modules in Vite and Webpack?](#q20) <span class="beginner">Beginner</span>
21. [What is the purpose of `publicPath` in Webpack config?](#q21) <span class="intermediate">Intermediate</span>
22. [How do you configure Environment Variables in Webpack with `DefinePlugin` vs Vite with `import.meta.env`?](#q22) <span class="beginner">Beginner</span>
23. [How does `esbuild` pre-bundling in Vite work?](#q23) <span class="intermediate">Intermediate</span>
24. [What is the purpose of `terser-webpack-plugin`?](#q24) <span class="intermediate">Intermediate</span>
25. [How do you configure PostCSS with Autoprefixer and Tailwind in Vite?](#q25) <span class="beginner">Beginner</span>
26. [What is the difference between CommonJS (`require`) and ES Modules (`import`)?](#q26) <span class="beginner">Beginner</span>
27. [How do you handle asset modules (images, fonts) in Webpack 5 without file-loader?](#q27) <span class="intermediate">Intermediate</span>
28. [What is the purpose of `manifest.json` in Webpack production builds?](#q28) <span class="intermediate">Intermediate</span>
29. [How do you optimize build times in large Webpack projects with persistent caching?](#q29) <span class="advanced">Advanced</span>
30. [What is the purpose of `babel-loader` cacheDirectory option?](#q30) <span class="intermediate">Intermediate</span>
31. [How do you configure TypeScript compilation in Vite (`vite-plugin-checker` vs `esbuild`)?](#q31) <span class="intermediate">Intermediate</span>
32. [What is the difference between `target: 'web'` and `target: 'node'` in Webpack?](#q32) <span class="beginner">Beginner</span>
33. [How do you configure custom aliases (e.g. `@/*` -> `src/*`) in Vite and Webpack?](#q33) <span class="beginner">Beginner</span>
34. [What is Webpack Scope Hoisting (`optimization.concatenateModules`)?](#q34) <span class="advanced">Advanced</span>
35. [How do you implement micro-frontends with Vite?](#q35) <span class="advanced">Advanced</span>
36. [What is the difference between development mode and production mode in Webpack (`mode: 'production'`)?](#q36) <span class="beginner">Beginner</span>
37. [How do you eliminate `console.log` statements in production builds?](#q37) <span class="intermediate">Intermediate</span>
38. [What is the difference between Static Imports and Dynamic Imports?](#q38) <span class="beginner">Beginner</span>
39. [How do you configure SVGs as React components with `@svgr/webpack` or `vite-plugin-svgr`?](#q39) <span class="beginner">Beginner</span>
40. [What is the purpose of `clean-webpack-plugin` in modern Webpack?](#q40) <span class="beginner">Beginner</span>
41. [How do you configure Brotli and Gzip compression with `vite-plugin-compression`?](#q41) <span class="intermediate">Intermediate</span>
42. [What is the difference between Rollup and Vite?](#q42) <span class="beginner">Beginner</span>
43. [How do you debug Webpack compilation errors with `--stats` and `--profile`?](#q43) <span class="intermediate">Intermediate</span>
44. [What is the purpose of `mini-css-extract-plugin` in Webpack?](#q44) <span class="intermediate">Intermediate</span>
45. [How do you configure multi-page applications (MPA) in Vite?](#q45) <span class="intermediate">Intermediate</span>
46. [What is the difference between Polyfills and Ponyfills?](#q46) <span class="intermediate">Intermediate</span>
47. [How do you configure SSL HTTPS on Vite dev server with `@vitejs/plugin-basic-ssl`?](#q47) <span class="beginner">Beginner</span>
48. [What is the purpose of `crossorigin` attribute in generated `<script>` tags?](#q48) <span class="intermediate">Intermediate</span>
49. [How do you configure Subresource Integrity (SRI) in Webpack?](#q49) <span class="advanced">Advanced</span>
50. [What is the difference between `externals` in Webpack and `rollupOptions.external` in Vite?](#q50) <span class="intermediate">Intermediate</span>
51. [How do you profile Vite dev server and build performance with `vite --profile`?](#q51) <span class="intermediate">Intermediate</span>
52. [What is the purpose of `resolve.extensions` in Webpack?](#q52) <span class="beginner">Beginner</span>
53. [How do you configure PostCSS nesting with `postcss-nesting`?](#q53) <span class="beginner">Beginner</span>
54. [What is the difference between `webpack-dev-server` and `webpack-dev-middleware`?](#q54) <span class="advanced">Advanced</span>
55. [How do you handle WebAssembly (Wasm) loading in Vite?](#q55) <span class="intermediate">Intermediate</span>
56. [What is the purpose of `stats.json` for CI/CD bundle size tracking?](#q56) <span class="intermediate">Intermediate</span>
57. [How do you configure Webpack to build Universal / SSR bundles?](#q57) <span class="advanced">Advanced</span>
58. [What is the difference between `babel-polyfill` (deprecated) and `core-js`?](#q58) <span class="beginner">Beginner</span>
59. [How do you configure Webpack for Progressive Web Apps with Workbox?](#q59) <span class="intermediate">Intermediate</span>
60. [What is the purpose of `chunkLoadingGlobal` (formerly `jsonpFunction`) in Webpack?](#q60) <span class="advanced">Advanced</span>
61. [How do you configure CSS minification in Webpack with `css-minimizer-webpack-plugin`?](#q61) <span class="intermediate">Intermediate</span>
62. [What is the difference between Vite preview mode (`vite preview`) and dev mode (`vite dev`)?](#q62) <span class="beginner">Beginner</span>
63. [How do you configure Webpack to output library as UMD, CJS, and ESM?](#q63) <span class="advanced">Advanced</span>
64. [What is the purpose of `browserslist` file in frontend tooling?](#q64) <span class="beginner">Beginner</span>
65. [What are the best practices for configuring modern enterprise frontend build pipelines?](#q65) <span class="advanced">Advanced</span>
66. [How do you configure dynamic imports with webpackMagicComments?](#q66) <span class="intermediate">Intermediate</span>
67. [What is the difference between `webpack-merge` and `Object.assign` for config composition?](#q67) <span class="intermediate">Intermediate</span>
68. [How do you configure environment-specific Babel presets in `.babelrc`?](#q68) <span class="intermediate">Intermediate</span>
69. [What is the difference between `eval`, `source-map`, and `inline-source-map`?](#q69) <span class="intermediate">Intermediate</span>
70. [How do you handle circular dependency warnings in Webpack with `circular-dependency-plugin`?](#q70) <span class="intermediate">Intermediate</span>
71. [What is the purpose of `terserOptions.mangle` and when should property mangling be avoided?](#q71) <span class="advanced">Advanced</span>
72. [How do you configure asset inlining thresholds in Vite (`build.assetsInlineLimit`)?](#q72) <span class="beginner">Beginner</span>
73. [What is the difference between `rollup-plugin-visualizer` and Webpack bundle analyzer?](#q73) <span class="beginner">Beginner</span>
74. [How do you configure caching in GitHub Actions CI for npm / pnpm / yarn?](#q74) <span class="intermediate">Intermediate</span>
75. [What is the purpose of `resolve.fallback` in Webpack 5 for Node.js core polyfills?](#q75) <span class="intermediate">Intermediate</span>
76. [How do you configure Vitest with Vite plugins sharing `vite.config.ts`?](#q76) <span class="intermediate">Intermediate</span>
77. [What is the difference between `require.context` in Webpack and `import.meta.glob` in Vite?](#q77) <span class="intermediate">Intermediate</span>
78. [How do you configure source map security to prevent exposing proprietary code in production?](#q78) <span class="advanced">Advanced</span>
79. [What is the purpose of `crossorigin` on dynamic script loading?](#q79) <span class="intermediate">Intermediate</span>
80. [How do you configure CSS source maps in Webpack and Vite?](#q80) <span class="beginner">Beginner</span>
81. [What is the difference between `babel-loader` and `ts-loader`?](#q81) <span class="intermediate">Intermediate</span>
82. [How do you configure custom HTML template parameters in `html-webpack-plugin`?](#q82) <span class="beginner">Beginner</span>
83. [What is the purpose of `vite-plugin-pwa`?](#q83) <span class="intermediate">Intermediate</span>
84. [How do you optimize Lodash bundle imports in Webpack with `babel-plugin-lodash`?](#q84) <span class="intermediate">Intermediate</span>
85. [What is the difference between `sideEffects: false` and `sideEffects: ['*.css']`?](#q85) <span class="intermediate">Intermediate</span>
86. [How do you configure Webpack to output ESM libraries (`experiments.outputModule`)?](#q86) <span class="advanced">Advanced</span>
87. [What is the purpose of `webpack.BannerPlugin`?](#q87) <span class="beginner">Beginner</span>
88. [How do you measure individual plugin execution timings in Webpack with `speed-measure-webpack-plugin`?](#q88) <span class="intermediate">Intermediate</span>
89. [What is the difference between `dependencies` and `peerDependencies` in component libraries?](#q89) <span class="intermediate">Intermediate</span>
90. [How do you handle asset caching with Content-Security-Policy nonces in Webpack?](#q90) <span class="advanced">Advanced</span>
91. [What is the difference between `raw-loader` and Webpack 5 `asset/source`?](#q91) <span class="beginner">Beginner</span>
92. [How do you configure CSS nano presets in Webpack?](#q92) <span class="intermediate">Intermediate</span>
93. [What is the purpose of `splitChunks.cacheGroups` in Webpack optimization?](#q93) <span class="advanced">Advanced</span>
94. [How do you configure Hot Module Replacement for Web Workers in Vite?](#q94) <span class="advanced">Advanced</span>
95. [What is the difference between `webpack-bundle-analyzer` static report vs live server mode?](#q95) <span class="beginner">Beginner</span>
96. [How do you configure custom ESLint flat config (`eslint.config.js`) in modern projects?](#q96) <span class="intermediate">Intermediate</span>
97. [What is the purpose of `esbuild-loader` in Webpack build pipelines?](#q97) <span class="intermediate">Intermediate</span>
98. [How do you configure proxy websockets in Vite dev server?](#q98) <span class="intermediate">Intermediate</span>
99. [What is the difference between `chunk` and `bundle` in Webpack terminology?](#q99) <span class="beginner">Beginner</span>
100. [How do you configure monorepo package resolution with pnpm workspaces and Vite?](#q100) <span class="intermediate">Intermediate</span>

---

<a id="q1"></a>
### Q1: How does Vite's Native ESM dev server differ fundamentally from Webpack's bundle-based architecture?

**Difficulty**: Advanced

**Strategy**:
Webpack bundles the entire application dependency graph in memory before serving, which results in slow startup times (30-60s) for large codebases. Vite serves source code over native browser ES Modules (ESM), letting the browser request modules on demand. Dependencies (node_modules) are pre-bundled using esbuild (in Go, 10-100x faster than JS bundlers). This provides instant dev server start (<300ms) and millisecond HMR regardless of application scale.

**Code Example**:
```javascript
// vite.config.ts
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react-swc';

export default defineConfig({
  plugins: [react()],
  server: { port: 3000, open: true },
  build: {
    target: 'esnext',
    minify: 'esbuild',
    rollupOptions: {
      output: {
        manualChunks: { vendor: ['react', 'react-dom'] }
      }
    }
  }
});
```

---

<a id="q2"></a>
### Q2: How does Webpack 5 Module Federation work and what problem does it solve in Micro-frontends?

**Difficulty**: Advanced

**Strategy**:
Module Federation allows multiple independent Webpack builds to dynamically share modules at runtime across domain boundaries without requiring npm packaging or monolithic bundling. A Host application can import exposed remote components or shared singleton libraries (like `react`, `react-dom`) directly over the network.

**Code Example**:
```javascript
// webpack.config.js (Host)
const { ModuleFederationPlugin } = require('webpack').container;

module.exports = {
  plugins: [
    new ModuleFederationPlugin({
      name: 'host_app',
      remotes: {
        dashboard: 'dashboard@https://cdn.example.com/remoteEntry.js'
      },
      shared: { react: { singleton: true, eager: true }, 'react-dom': { singleton: true } }
    })
  ]
};
```

---

<a id="q3"></a>
### Q3: How does Tree Shaking work in Webpack and Rollup, and what makes a module 'pure'?

**Difficulty**: Intermediate

**Strategy**:
Tree shaking relies on static analysis of ES Module syntax (`import`/`export`). The bundler builds an AST dependency graph and marks unreferenced exports for elimination by the minifier (Terser/Esbuild). Modules must have no side-effects (or be marked with `"sideEffects": false` in `package.json`). Functions with top-level side effects or dynamic `require()` cannot be safely tree-shaken.

**Code Example**:
```json
// package.json
{
  "name": "my-ui-library",
  "sideEffects": false
}
```

---

<a id="q4"></a>
### Q4: What is the role of Babel AST (Abstract Syntax Tree) and how do Babel plugins transform code?

**Difficulty**: Advanced

**Strategy**:
Babel operates in 3 distinct phases:
1. **Parse**: Converts source code into an AST using `@babel/parser`.
2. **Transform**: Traverses the AST with `@babel/traverse` using visitor pattern plugins to rewrite, insert, or replace AST nodes.
3. **Generate**: Converts the modified AST back into target JavaScript and sourcemaps using `@babel/generator`.

**Code Example**:
```javascript
// Simple Babel Visitor Plugin
module.exports = function({ types: t }) {
  return {
    visitor: {
      Identifier(path) {
        if (path.node.name === 'DEBUG_MODE') {
          path.replaceWith(t.booleanLiteral(false));
        }
      }
    }
  };
};
```

---

<a id="q5"></a>
### Q5: How does Hot Module Replacement (HMR) work under the hood?

**Difficulty**: Advanced

**Strategy**:
HMR updates running code in the browser without a full page reload. When a file is edited:
1. The dev server compiler detects file modification and generates an update manifest and JS patch chunk.
2. The server sends a WebSocket message to the browser HMR runtime.
3. The HMR runtime requests the update chunk and calls `module.hot.accept()` handlers to replace modules in memory while preserving component state.

**Code Example**:
```javascript
// Manual HMR Accept Handler
if (import.meta.hot) {
  import.meta.hot.accept((newModule) => {
    if (newModule) {
      console.log('Updated module in memory:', newModule);
    }
  });
}
```

---

<a id="q6"></a>
### Q6: What are Webpack Loaders vs Plugins?

**Difficulty**: Beginner

**Strategy**:
Comprehensive technical explanation of What are Webpack Loaders vs Plugins?. Loaders transform non-JS files (CSS, TS, images) into valid modules; Plugins perform broad build tasks (bundle optimization, asset injection, env vars). Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What are Webpack Loaders vs Plugins?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q7"></a>
### Q7: How do you configure Code Splitting with `import()` dynamic imports in Webpack?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of How do you configure Code Splitting with `import()` dynamic imports in Webpack?. Dynamic imports generate separate chunks loaded asynchronously over HTTP on demand. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you configure Code Splitting with `import()` dynamic imports in Webpack?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q8"></a>
### Q8: What is the purpose of `output.filename` vs `output.chunkFilename` in Webpack?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of What is the purpose of `output.filename` vs `output.chunkFilename` in Webpack?. `filename` names entry chunks; `chunkFilename` names dynamically loaded on-demand chunks with content hashes. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the purpose of `output.filename` vs `output.chunkFilename` in Webpack?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q9"></a>
### Q9: How does Content Hashing (`[contenthash]`) enable long-term browser caching?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of How does Content Hashing (`[contenthash]`) enable long-term browser caching?. Computes hash based strictly on file contents, allowing immutable caching headers until code changes. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How does Content Hashing (`[contenthash]`) enable long-term browser caching?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q10"></a>
### Q10: What is `source-map` and which devtool options are best for development vs production?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of What is `source-map` and which devtool options are best for development vs production?. Development: `eval-cheap-module-source-map` (fast); Production: `source-map` (high accuracy, external). Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is `source-map` and which devtool options are best for development vs production?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q11"></a>
### Q11: How does Rollup differ from Webpack and why is it preferred for libraries?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of How does Rollup differ from Webpack and why is it preferred for libraries?. Rollup generates flat, clean ESM bundles without runtime wrapper overhead, making it ideal for npm packages. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How does Rollup differ from Webpack and why is it preferred for libraries?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q12"></a>
### Q12: What is esbuild and why is it orders of magnitude faster than Webpack and Babel?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of What is esbuild and why is it orders of magnitude faster than Webpack and Babel?. Written in Go, compiles directly to native machine code, parses ASTs in parallel without garbage collection pauses. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is esbuild and why is it orders of magnitude faster than Webpack and Babel?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q13"></a>
### Q13: How does SWC (Speedy Web Compiler) compare to Babel?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of How does SWC (Speedy Web Compiler) compare to Babel?. Rust-based drop-in replacement for Babel running 20-70x faster in CI/CD pipelines. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How does SWC (Speedy Web Compiler) compare to Babel?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q14"></a>
### Q14: What is the purpose of `@babel/preset-env` and `browserslist`?

**Difficulty**: Beginner

**Strategy**:
Comprehensive technical explanation of What is the purpose of `@babel/preset-env` and `browserslist`?. Transforms modern ESNext syntax into target browser compatible JS based on query in `.browserslistrc`. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the purpose of `@babel/preset-env` and `browserslist`?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q15"></a>
### Q15: What is `core-js` and how does Polyfill injection work in Babel (`useBuiltIns`)?

**Difficulty**: Advanced

**Strategy**:
Comprehensive technical explanation of What is `core-js` and how does Polyfill injection work in Babel (`useBuiltIns`)?. Injects missing runtime APIs (Promise, Map) either by entry (`entry`) or only for APIs actually used (`usage`). Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is `core-js` and how does Polyfill injection work in Babel (`useBuiltIns`)?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q16"></a>
### Q16: How do you configure Webpack Bundle Analyzer to identify oversized dependencies?

**Difficulty**: Beginner

**Strategy**:
Comprehensive technical explanation of How do you configure Webpack Bundle Analyzer to identify oversized dependencies?. Use `webpack-bundle-analyzer` plugin to view interactive visual treemaps of bundle chunks. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you configure Webpack Bundle Analyzer to identify oversized dependencies?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q17"></a>
### Q17: What is the purpose of `SplitChunksPlugin` (`optimization.splitChunks`) in Webpack?

**Difficulty**: Advanced

**Strategy**:
Comprehensive technical explanation of What is the purpose of `SplitChunksPlugin` (`optimization.splitChunks`) in Webpack?. Extracts common shared vendor code and duplicate modules into separate cached chunks. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the purpose of `SplitChunksPlugin` (`optimization.splitChunks`) in Webpack?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q18"></a>
### Q18: How do you configure Vite proxy for development API requests to avoid CORS?

**Difficulty**: Beginner

**Strategy**:
Comprehensive technical explanation of How do you configure Vite proxy for development API requests to avoid CORS?. Configure `server.proxy` forwarding `/api` to backend origin in `vite.config.ts`. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you configure Vite proxy for development API requests to avoid CORS?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q19"></a>
### Q19: What is the difference between `dependencies`, `devDependencies`, and `peerDependencies` in bundler builds?

**Difficulty**: Beginner

**Strategy**:
Comprehensive technical explanation of What is the difference between `dependencies`, `devDependencies`, and `peerDependencies` in bundler builds?. Bundlers only include modules actually imported into the entry dependency graph regardless of package.json section. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the difference between `dependencies`, `devDependencies`, and `peerDependencies` in bundler builds?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q20"></a>
### Q20: How do you handle CSS Modules in Vite and Webpack?

**Difficulty**: Beginner

**Strategy**:
Comprehensive technical explanation of How do you handle CSS Modules in Vite and Webpack?. Name files `[name].module.css` to scope class names with unique hashes automatically. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you handle CSS Modules in Vite and Webpack?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q21"></a>
### Q21: What is the purpose of `publicPath` in Webpack config?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of What is the purpose of `publicPath` in Webpack config?. Specifies the base URL prefix for all generated asset URLs (CDN domain, subdirectory). Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the purpose of `publicPath` in Webpack config?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q22"></a>
### Q22: How do you configure Environment Variables in Webpack with `DefinePlugin` vs Vite with `import.meta.env`?

**Difficulty**: Beginner

**Strategy**:
Comprehensive technical explanation of How do you configure Environment Variables in Webpack with `DefinePlugin` vs Vite with `import.meta.env`?. Webpack uses `new webpack.DefinePlugin()`; Vite natively exposes variables prefixed with `VITE_`. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you configure Environment Variables in Webpack with `DefinePlugin` vs Vite with `import.meta.env`?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q23"></a>
### Q23: How does `esbuild` pre-bundling in Vite work?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of How does `esbuild` pre-bundling in Vite work?. Converts CommonJS/UMD dependencies to ESM and bundles thousands of internal modules into single files for fast browser loading. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How does `esbuild` pre-bundling in Vite work?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q24"></a>
### Q24: What is the purpose of `terser-webpack-plugin`?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of What is the purpose of `terser-webpack-plugin`?. Minifies JavaScript, removes comments/console logs, and mangles variable names in production. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the purpose of `terser-webpack-plugin`?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q25"></a>
### Q25: How do you configure PostCSS with Autoprefixer and Tailwind in Vite?

**Difficulty**: Beginner

**Strategy**:
Comprehensive technical explanation of How do you configure PostCSS with Autoprefixer and Tailwind in Vite?. Add `postcss.config.js` with `tailwindcss` and `autoprefixer` plugins. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you configure PostCSS with Autoprefixer and Tailwind in Vite?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q26"></a>
### Q26: What is the difference between CommonJS (`require`) and ES Modules (`import`)?

**Difficulty**: Beginner

**Strategy**:
Comprehensive technical explanation of What is the difference between CommonJS (`require`) and ES Modules (`import`)?. CommonJS is synchronous and runtime-evaluated; ESM is asynchronous, statically analyzable, and tree-shakable. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the difference between CommonJS (`require`) and ES Modules (`import`)?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q27"></a>
### Q27: How do you handle asset modules (images, fonts) in Webpack 5 without file-loader?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of How do you handle asset modules (images, fonts) in Webpack 5 without file-loader?. Use Asset Modules (`asset/resource`, `asset/inline`, `asset/source`) built natively into Webpack 5. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you handle asset modules (images, fonts) in Webpack 5 without file-loader?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q28"></a>
### Q28: What is the purpose of `manifest.json` in Webpack production builds?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of What is the purpose of `manifest.json` in Webpack production builds?. Maps source chunk names to hashed output filenames for server asset rendering. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the purpose of `manifest.json` in Webpack production builds?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q29"></a>
### Q29: How do you optimize build times in large Webpack projects with persistent caching?

**Difficulty**: Advanced

**Strategy**:
Comprehensive technical explanation of How do you optimize build times in large Webpack projects with persistent caching?. Enable `cache: { type: 'filesystem' }` in `webpack.config.js`. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you optimize build times in large Webpack projects with persistent caching?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q30"></a>
### Q30: What is the purpose of `babel-loader` cacheDirectory option?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of What is the purpose of `babel-loader` cacheDirectory option?. Caches Babel transformation results to disk, speeding up subsequent compilation runs. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the purpose of `babel-loader` cacheDirectory option?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q31"></a>
### Q31: How do you configure TypeScript compilation in Vite (`vite-plugin-checker` vs `esbuild`)?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of How do you configure TypeScript compilation in Vite (`vite-plugin-checker` vs `esbuild`)?. Vite transpiles TS via esbuild; use `vite-plugin-checker` or `tsc --noEmit` in CI for strict type checking. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you configure TypeScript compilation in Vite (`vite-plugin-checker` vs `esbuild`)?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q32"></a>
### Q32: What is the difference between `target: 'web'` and `target: 'node'` in Webpack?

**Difficulty**: Beginner

**Strategy**:
Comprehensive technical explanation of What is the difference between `target: 'web'` and `target: 'node'` in Webpack?. Determines runtime environment, built-in global variables, and module loading conventions. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the difference between `target: 'web'` and `target: 'node'` in Webpack?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q33"></a>
### Q33: How do you configure custom aliases (e.g. `@/*` -> `src/*`) in Vite and Webpack?

**Difficulty**: Beginner

**Strategy**:
Comprehensive technical explanation of How do you configure custom aliases (e.g. `@/*` -> `src/*`) in Vite and Webpack?. Configure `resolve.alias` in bundler config and matching `paths` in `tsconfig.json`. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you configure custom aliases (e.g. `@/*` -> `src/*`) in Vite and Webpack?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q34"></a>
### Q34: What is Webpack Scope Hoisting (`optimization.concatenateModules`)?

**Difficulty**: Advanced

**Strategy**:
Comprehensive technical explanation of What is Webpack Scope Hoisting (`optimization.concatenateModules`)?. Concatenates all modules in an ES6 module graph into a single wrapper closure, reducing runtime overhead and bundle size. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is Webpack Scope Hoisting (`optimization.concatenateModules`)?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q35"></a>
### Q35: How do you implement micro-frontends with Vite?

**Difficulty**: Advanced

**Strategy**:
Comprehensive technical explanation of How do you implement micro-frontends with Vite?. Use `@originjs/vite-plugin-federation` to provide Webpack-compatible Module Federation in Vite. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you implement micro-frontends with Vite?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q36"></a>
### Q36: What is the difference between development mode and production mode in Webpack (`mode: 'production'`)?

**Difficulty**: Beginner

**Strategy**:
Comprehensive technical explanation of What is the difference between development mode and production mode in Webpack (`mode: 'production'`)?. Production enables minification, scope hoisting, side-effect elimination, and production process.env flags. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the difference between development mode and production mode in Webpack (`mode: 'production'`)?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q37"></a>
### Q37: How do you eliminate `console.log` statements in production builds?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of How do you eliminate `console.log` statements in production builds?. Use `terserOptions: { compress: { drop_console: true } }` in build config. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you eliminate `console.log` statements in production builds?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q38"></a>
### Q38: What is the difference between Static Imports and Dynamic Imports?

**Difficulty**: Beginner

**Strategy**:
Comprehensive technical explanation of What is the difference between Static Imports and Dynamic Imports?. Static imports are loaded synchronously at startup; dynamic imports return a Promise and load on-demand. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the difference between Static Imports and Dynamic Imports?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q39"></a>
### Q39: How do you configure SVGs as React components with `@svgr/webpack` or `vite-plugin-svgr`?

**Difficulty**: Beginner

**Strategy**:
Comprehensive technical explanation of How do you configure SVGs as React components with `@svgr/webpack` or `vite-plugin-svgr`?. Transform SVG files into JSX components dynamically. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you configure SVGs as React components with `@svgr/webpack` or `vite-plugin-svgr`?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q40"></a>
### Q40: What is the purpose of `clean-webpack-plugin` in modern Webpack?

**Difficulty**: Beginner

**Strategy**:
Comprehensive technical explanation of What is the purpose of `clean-webpack-plugin` in modern Webpack?. Webpack 5 natively supports `output.clean: true` to purge the dist directory before building. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the purpose of `clean-webpack-plugin` in modern Webpack?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q41"></a>
### Q41: How do you configure Brotli and Gzip compression with `vite-plugin-compression`?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of How do you configure Brotli and Gzip compression with `vite-plugin-compression`?. Pre-compresses static assets to `.br` and `.gz` files for high-speed Nginx static serving. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you configure Brotli and Gzip compression with `vite-plugin-compression`?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q42"></a>
### Q42: What is the difference between Rollup and Vite?

**Difficulty**: Beginner

**Strategy**:
Comprehensive technical explanation of What is the difference between Rollup and Vite?. Vite is an opinionated frontend build tool using Rollup under the hood for production bundling. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the difference between Rollup and Vite?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q43"></a>
### Q43: How do you debug Webpack compilation errors with `--stats` and `--profile`?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of How do you debug Webpack compilation errors with `--stats` and `--profile`?. Generate timing profiles and inspect failed loader stages. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you debug Webpack compilation errors with `--stats` and `--profile`?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q44"></a>
### Q44: What is the purpose of `mini-css-extract-plugin` in Webpack?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of What is the purpose of `mini-css-extract-plugin` in Webpack?. Extracts CSS into separate external `.css` files rather than inlining them inside JS bundles via `style-loader`. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the purpose of `mini-css-extract-plugin` in Webpack?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q45"></a>
### Q45: How do you configure multi-page applications (MPA) in Vite?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of How do you configure multi-page applications (MPA) in Vite?. Define multiple HTML entry points in `build.rollupOptions.input`. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you configure multi-page applications (MPA) in Vite?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q46"></a>
### Q46: What is the difference between Polyfills and Ponyfills?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of What is the difference between Polyfills and Ponyfills?. Polyfill mutates global prototypes; Ponyfill exports pure standalone functions without mutating globals. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the difference between Polyfills and Ponyfills?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q47"></a>
### Q47: How do you configure SSL HTTPS on Vite dev server with `@vitejs/plugin-basic-ssl`?

**Difficulty**: Beginner

**Strategy**:
Comprehensive technical explanation of How do you configure SSL HTTPS on Vite dev server with `@vitejs/plugin-basic-ssl`?. Generates self-signed SSL certificates for local HTTPS development. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you configure SSL HTTPS on Vite dev server with `@vitejs/plugin-basic-ssl`?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q48"></a>
### Q48: What is the purpose of `crossorigin` attribute in generated `<script>` tags?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of What is the purpose of `crossorigin` attribute in generated `<script>` tags?. Enables CORS error logging and integrity checks. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the purpose of `crossorigin` attribute in generated `<script>` tags?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q49"></a>
### Q49: How do you configure Subresource Integrity (SRI) in Webpack?

**Difficulty**: Advanced

**Strategy**:
Comprehensive technical explanation of How do you configure Subresource Integrity (SRI) in Webpack?. Use `webpack-subresource-integrity` plugin to add sha384 integrity hashes to script tags. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you configure Subresource Integrity (SRI) in Webpack?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q50"></a>
### Q50: What is the difference between `externals` in Webpack and `rollupOptions.external` in Vite?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of What is the difference between `externals` in Webpack and `rollupOptions.external` in Vite?. Excludes specified packages from bundle, assuming they are available globally (e.g. from CDN). Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the difference between `externals` in Webpack and `rollupOptions.external` in Vite?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q51"></a>
### Q51: How do you profile Vite dev server and build performance with `vite --profile`?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of How do you profile Vite dev server and build performance with `vite --profile`?. Identifies slow plugins and transform operations. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you profile Vite dev server and build performance with `vite --profile`?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q52"></a>
### Q52: What is the purpose of `resolve.extensions` in Webpack?

**Difficulty**: Beginner

**Strategy**:
Comprehensive technical explanation of What is the purpose of `resolve.extensions` in Webpack?. Allows omitting file extensions (`.js`, `.ts`, `.tsx`) in import statements. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the purpose of `resolve.extensions` in Webpack?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q53"></a>
### Q53: How do you configure PostCSS nesting with `postcss-nesting`?

**Difficulty**: Beginner

**Strategy**:
Comprehensive technical explanation of How do you configure PostCSS nesting with `postcss-nesting`?. Enables standard CSS nesting syntax across all browsers. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you configure PostCSS nesting with `postcss-nesting`?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q54"></a>
### Q54: What is the difference between `webpack-dev-server` and `webpack-dev-middleware`?

**Difficulty**: Advanced

**Strategy**:
Comprehensive technical explanation of What is the difference between `webpack-dev-server` and `webpack-dev-middleware`?. `webpack-dev-server` is a standalone Express server; `webpack-dev-middleware` mounts Webpack compilation onto an existing custom Express app. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the difference between `webpack-dev-server` and `webpack-dev-middleware`?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q55"></a>
### Q55: How do you handle WebAssembly (Wasm) loading in Vite?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of How do you handle WebAssembly (Wasm) loading in Vite?. Import `.wasm` files directly via `import init from './app.wasm?init'`. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you handle WebAssembly (Wasm) loading in Vite?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q56"></a>
### Q56: What is the purpose of `stats.json` for CI/CD bundle size tracking?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of What is the purpose of `stats.json` for CI/CD bundle size tracking?. Emits bundle metadata used by GitHub Actions to flag pull request bundle size regressions. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the purpose of `stats.json` for CI/CD bundle size tracking?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q57"></a>
### Q57: How do you configure Webpack to build Universal / SSR bundles?

**Difficulty**: Advanced

**Strategy**:
Comprehensive technical explanation of How do you configure Webpack to build Universal / SSR bundles?. Create dual Webpack configurations: one for client (`target: 'web'`) and one for server (`target: 'node'`). Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you configure Webpack to build Universal / SSR bundles?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q58"></a>
### Q58: What is the difference between `babel-polyfill` (deprecated) and `core-js`?

**Difficulty**: Beginner

**Strategy**:
Comprehensive technical explanation of What is the difference between `babel-polyfill` (deprecated) and `core-js`?. Modern Babel uses `core-js/stable` and `regenerator-runtime` instead of monolithic `babel-polyfill`. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the difference between `babel-polyfill` (deprecated) and `core-js`?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q59"></a>
### Q59: How do you configure Webpack for Progressive Web Apps with Workbox?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of How do you configure Webpack for Progressive Web Apps with Workbox?. Use `workbox-webpack-plugin` to generate service worker and precache assets. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you configure Webpack for Progressive Web Apps with Workbox?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q60"></a>
### Q60: What is the purpose of `chunkLoadingGlobal` (formerly `jsonpFunction`) in Webpack?

**Difficulty**: Advanced

**Strategy**:
Comprehensive technical explanation of What is the purpose of `chunkLoadingGlobal` (formerly `jsonpFunction`) in Webpack?. Names the global window array used to load async chunks, preventing collisions between micro-frontends. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the purpose of `chunkLoadingGlobal` (formerly `jsonpFunction`) in Webpack?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q61"></a>
### Q61: How do you configure CSS minification in Webpack with `css-minimizer-webpack-plugin`?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of How do you configure CSS minification in Webpack with `css-minimizer-webpack-plugin`?. Minifies and optimizes CSS rules using `cssnano` in production. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you configure CSS minification in Webpack with `css-minimizer-webpack-plugin`?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q62"></a>
### Q62: What is the difference between Vite preview mode (`vite preview`) and dev mode (`vite dev`)?

**Difficulty**: Beginner

**Strategy**:
Comprehensive technical explanation of What is the difference between Vite preview mode (`vite preview`) and dev mode (`vite dev`)?. `vite dev` runs live ESM dev server; `vite preview` serves actual compiled production dist output locally. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the difference between Vite preview mode (`vite preview`) and dev mode (`vite dev`)?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q63"></a>
### Q63: How do you configure Webpack to output library as UMD, CJS, and ESM?

**Difficulty**: Advanced

**Strategy**:
Comprehensive technical explanation of How do you configure Webpack to output library as UMD, CJS, and ESM?. Configure `output.library.type` for multiple export targets. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you configure Webpack to output library as UMD, CJS, and ESM?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q64"></a>
### Q64: What is the purpose of `browserslist` file in frontend tooling?

**Difficulty**: Beginner

**Strategy**:
Comprehensive technical explanation of What is the purpose of `browserslist` file in frontend tooling?. Shared configuration queried by Autoprefixer, Babel, and ESLint to target browser versions. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the purpose of `browserslist` file in frontend tooling?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q65"></a>
### Q65: What are the best practices for configuring modern enterprise frontend build pipelines?

**Difficulty**: Advanced

**Strategy**:
Comprehensive technical explanation of What are the best practices for configuring modern enterprise frontend build pipelines?. Use Vite/Rollup for speed, enforce strict TypeScript checks in CI, split vendor chunks, enable immutable content hashing, and measure bundle size on pull requests. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What are the best practices for configuring modern enterprise frontend build pipelines?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q66"></a>
### Q66: How do you configure dynamic imports with webpackMagicComments?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of How do you configure dynamic imports with webpackMagicComments?. Use `/* webpackChunkName: 'admin' */` and `/* webpackPrefetch: true */` inside dynamic `import()` calls. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you configure dynamic imports with webpackMagicComments?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q67"></a>
### Q67: What is the difference between `webpack-merge` and `Object.assign` for config composition?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of What is the difference between `webpack-merge` and `Object.assign` for config composition?. webpack-merge merges loader rule arrays and plugin arrays properly rather than overwriting them. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the difference between `webpack-merge` and `Object.assign` for config composition?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q68"></a>
### Q68: How do you configure environment-specific Babel presets in `.babelrc`?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of How do you configure environment-specific Babel presets in `.babelrc`?. Use `env: { test: { plugins: [...] }, production: { ... } }` in Babel configuration. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you configure environment-specific Babel presets in `.babelrc`?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q69"></a>
### Q69: What is the difference between `eval`, `source-map`, and `inline-source-map`?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of What is the difference between `eval`, `source-map`, and `inline-source-map`?. `eval` is fastest for rebuilds; `source-map` creates external `.map` files; `inline-source-map` embeds base64 maps directly. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the difference between `eval`, `source-map`, and `inline-source-map`?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q70"></a>
### Q70: How do you handle circular dependency warnings in Webpack with `circular-dependency-plugin`?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of How do you handle circular dependency warnings in Webpack with `circular-dependency-plugin`?. Detects and flags circular module imports that cause runtime `undefined` bugs. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you handle circular dependency warnings in Webpack with `circular-dependency-plugin`?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q71"></a>
### Q71: What is the purpose of `terserOptions.mangle` and when should property mangling be avoided?

**Difficulty**: Advanced

**Strategy**:
Comprehensive technical explanation of What is the purpose of `terserOptions.mangle` and when should property mangling be avoided?. Variable mangling shrinks names (e.g. `userName` -> `a`); property mangling breaks object reflection unless carefully configured. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the purpose of `terserOptions.mangle` and when should property mangling be avoided?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q72"></a>
### Q72: How do you configure asset inlining thresholds in Vite (`build.assetsInlineLimit`)?

**Difficulty**: Beginner

**Strategy**:
Comprehensive technical explanation of How do you configure asset inlining thresholds in Vite (`build.assetsInlineLimit`)?. Assets smaller than limit (default 4KB) are converted to base64 data URIs to save HTTP requests. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you configure asset inlining thresholds in Vite (`build.assetsInlineLimit`)?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q73"></a>
### Q73: What is the difference between `rollup-plugin-visualizer` and Webpack bundle analyzer?

**Difficulty**: Beginner

**Strategy**:
Comprehensive technical explanation of What is the difference between `rollup-plugin-visualizer` and Webpack bundle analyzer?. Both generate interactive HTML visual treemaps of bundle chunks for their respective bundlers. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the difference between `rollup-plugin-visualizer` and Webpack bundle analyzer?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q74"></a>
### Q74: How do you configure caching in GitHub Actions CI for npm / pnpm / yarn?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of How do you configure caching in GitHub Actions CI for npm / pnpm / yarn?. Cache `~/.pnpm-store` or `node_modules` keyed by `pnpm-lock.yaml` hash to save install time. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you configure caching in GitHub Actions CI for npm / pnpm / yarn?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q75"></a>
### Q75: What is the purpose of `resolve.fallback` in Webpack 5 for Node.js core polyfills?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of What is the purpose of `resolve.fallback` in Webpack 5 for Node.js core polyfills?. Webpack 5 stopped polyfilling Node core modules (`crypto`, `path`, `buffer`); you must declare fallbacks explicitly. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the purpose of `resolve.fallback` in Webpack 5 for Node.js core polyfills?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q76"></a>
### Q76: How do you configure Vitest with Vite plugins sharing `vite.config.ts`?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of How do you configure Vitest with Vite plugins sharing `vite.config.ts`?. Vitest shares the exact same plugins, aliases, and transform pipeline defined in `vite.config.ts`. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you configure Vitest with Vite plugins sharing `vite.config.ts`?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q77"></a>
### Q77: What is the difference between `require.context` in Webpack and `import.meta.glob` in Vite?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of What is the difference between `require.context` in Webpack and `import.meta.glob` in Vite?. Vite uses `import.meta.glob('./dir/*.ts')` to import multiple modules dynamically. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the difference between `require.context` in Webpack and `import.meta.glob` in Vite?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q78"></a>
### Q78: How do you configure source map security to prevent exposing proprietary code in production?

**Difficulty**: Advanced

**Strategy**:
Comprehensive technical explanation of How do you configure source map security to prevent exposing proprietary code in production?. Upload source maps directly to error tracking servers (Sentry, Datadog) and delete them from public CDN buckets. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you configure source map security to prevent exposing proprietary code in production?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q79"></a>
### Q79: What is the purpose of `crossorigin` on dynamic script loading?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of What is the purpose of `crossorigin` on dynamic script loading?. Ensures cross-origin scripts emit full stack traces to `window.onerror` rather than generic 'Script error.' Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the purpose of `crossorigin` on dynamic script loading?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q80"></a>
### Q80: How do you configure CSS source maps in Webpack and Vite?

**Difficulty**: Beginner

**Strategy**:
Comprehensive technical explanation of How do you configure CSS source maps in Webpack and Vite?. Enable `css.devSourcemap: true` in Vite or `options: { sourceMap: true }` on `css-loader` in Webpack. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you configure CSS source maps in Webpack and Vite?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q81"></a>
### Q81: What is the difference between `babel-loader` and `ts-loader`?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of What is the difference between `babel-loader` and `ts-loader`?. `ts-loader` performs full type checking during build; `babel-loader` only strips types without type validation. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the difference between `babel-loader` and `ts-loader`?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q82"></a>
### Q82: How do you configure custom HTML template parameters in `html-webpack-plugin`?

**Difficulty**: Beginner

**Strategy**:
Comprehensive technical explanation of How do you configure custom HTML template parameters in `html-webpack-plugin`?. Pass custom template parameters (e.g. `title`, `analyticsId`) into plugin constructor options. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you configure custom HTML template parameters in `html-webpack-plugin`?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q83"></a>
### Q83: What is the purpose of `vite-plugin-pwa`?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of What is the purpose of `vite-plugin-pwa`?. Automates Service Worker registration, web manifest generation, and Workbox precaching in Vite. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the purpose of `vite-plugin-pwa`?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q84"></a>
### Q84: How do you optimize Lodash bundle imports in Webpack with `babel-plugin-lodash`?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of How do you optimize Lodash bundle imports in Webpack with `babel-plugin-lodash`?. Rewrites `import { get } from 'lodash'` into `import get from 'lodash/get'` to enable proper tree shaking. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you optimize Lodash bundle imports in Webpack with `babel-plugin-lodash`?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q85"></a>
### Q85: What is the difference between `sideEffects: false` and `sideEffects: ['*.css']`?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of What is the difference between `sideEffects: false` and `sideEffects: ['*.css']`?. Tells bundler that JS modules have no side-effects but preserves CSS file imports. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the difference between `sideEffects: false` and `sideEffects: ['*.css']`?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q86"></a>
### Q86: How do you configure Webpack to output ESM libraries (`experiments.outputModule`)?

**Difficulty**: Advanced

**Strategy**:
Comprehensive technical explanation of How do you configure Webpack to output ESM libraries (`experiments.outputModule`)?. Enable experimental ESM output flag in Webpack 5 configuration. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you configure Webpack to output ESM libraries (`experiments.outputModule`)?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q87"></a>
### Q87: What is the purpose of `webpack.BannerPlugin`?

**Difficulty**: Beginner

**Strategy**:
Comprehensive technical explanation of What is the purpose of `webpack.BannerPlugin`?. Prepends license banners, author info, and build version headers to every generated chunk. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the purpose of `webpack.BannerPlugin`?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q88"></a>
### Q88: How do you measure individual plugin execution timings in Webpack with `speed-measure-webpack-plugin`?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of How do you measure individual plugin execution timings in Webpack with `speed-measure-webpack-plugin`?. Wraps Webpack configuration and outputs execution time metrics per loader and plugin. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you measure individual plugin execution timings in Webpack with `speed-measure-webpack-plugin`?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q89"></a>
### Q89: What is the difference between `dependencies` and `peerDependencies` in component libraries?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of What is the difference between `dependencies` and `peerDependencies` in component libraries?. Dependencies are bundled; peerDependencies must be supplied by the consuming application. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the difference between `dependencies` and `peerDependencies` in component libraries?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q90"></a>
### Q90: How do you handle asset caching with Content-Security-Policy nonces in Webpack?

**Difficulty**: Advanced

**Strategy**:
Comprehensive technical explanation of How do you handle asset caching with Content-Security-Policy nonces in Webpack?. Inject dynamic `__webpack_nonce__` variable before loading asynchronous chunks. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you handle asset caching with Content-Security-Policy nonces in Webpack?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q91"></a>
### Q91: What is the difference between `raw-loader` and Webpack 5 `asset/source`?

**Difficulty**: Beginner

**Strategy**:
Comprehensive technical explanation of What is the difference between `raw-loader` and Webpack 5 `asset/source`?. `asset/source` exports raw source text natively without installing `raw-loader`. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the difference between `raw-loader` and Webpack 5 `asset/source`?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q92"></a>
### Q92: How do you configure CSS nano presets in Webpack?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of How do you configure CSS nano presets in Webpack?. Configure `css-minimizer-webpack-plugin` with `cssnano` safe optimizations. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you configure CSS nano presets in Webpack?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q93"></a>
### Q93: What is the purpose of `splitChunks.cacheGroups` in Webpack optimization?

**Difficulty**: Advanced

**Strategy**:
Comprehensive technical explanation of What is the purpose of `splitChunks.cacheGroups` in Webpack optimization?. Defines custom rules for grouping modules into specific chunk names (e.g. `react-vendor`, `common`). Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the purpose of `splitChunks.cacheGroups` in Webpack optimization?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q94"></a>
### Q94: How do you configure Hot Module Replacement for Web Workers in Vite?

**Difficulty**: Advanced

**Strategy**:
Comprehensive technical explanation of How do you configure Hot Module Replacement for Web Workers in Vite?. Use `new Worker(new URL('./worker.ts', import.meta.url), { type: 'module' })`. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you configure Hot Module Replacement for Web Workers in Vite?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q95"></a>
### Q95: What is the difference between `webpack-bundle-analyzer` static report vs live server mode?

**Difficulty**: Beginner

**Strategy**:
Comprehensive technical explanation of What is the difference between `webpack-bundle-analyzer` static report vs live server mode?. Static mode generates an offline HTML report file; server mode opens an interactive local web server. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the difference between `webpack-bundle-analyzer` static report vs live server mode?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q96"></a>
### Q96: How do you configure custom ESLint flat config (`eslint.config.js`) in modern projects?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of How do you configure custom ESLint flat config (`eslint.config.js`) in modern projects?. Export configuration array using `@eslint/js` and typescript-eslint parser. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you configure custom ESLint flat config (`eslint.config.js`) in modern projects?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q97"></a>
### Q97: What is the purpose of `esbuild-loader` in Webpack build pipelines?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of What is the purpose of `esbuild-loader` in Webpack build pipelines?. Replaces `babel-loader` and `ts-loader` with esbuild for ultra-fast transpilation. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the purpose of `esbuild-loader` in Webpack build pipelines?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q98"></a>
### Q98: How do you configure proxy websockets in Vite dev server?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of How do you configure proxy websockets in Vite dev server?. Set `ws: true` on `server.proxy` target configuration. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you configure proxy websockets in Vite dev server?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q99"></a>
### Q99: What is the difference between `chunk` and `bundle` in Webpack terminology?

**Difficulty**: Beginner

**Strategy**:
Comprehensive technical explanation of What is the difference between `chunk` and `bundle` in Webpack terminology?. Module is single file; Chunk is grouped modules compiled together; Bundle is the final output file emitted to disk. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for What is the difference between `chunk` and `bundle` in Webpack terminology?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---

<a id="q100"></a>
### Q100: How do you configure monorepo package resolution with pnpm workspaces and Vite?

**Difficulty**: Intermediate

**Strategy**:
Comprehensive technical explanation of How do you configure monorepo package resolution with pnpm workspaces and Vite?. Use `resolve.alias` or typescript path mappings pointing to local workspace packages. Key focus on build performance, module systems (ESM vs CJS), AST transformations, tree shaking, and enterprise CI/CD standards.

**Code Example**:
```javascript
// Configuration for How do you configure monorepo package resolution with pnpm workspaces and Vite?
module.exports = {
  // Production Build Optimization Standard
  mode: 'production',
  optimization: { splitChunks: { chunks: 'all' } }
};
```

---
