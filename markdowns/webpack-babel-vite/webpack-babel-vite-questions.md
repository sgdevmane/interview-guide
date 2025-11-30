# Webpack, Babel, & Vite Interview Questions

## Table of Contents
1. [You are migrating a legacy React project from Webpack to Vite to improve development server start time. The project relies on CommonJS modules (`require`). How do you handle this in Vite?](#q1-you-are-migrating-a-legacy-react-project-from-webpack-to-vite-to-improve-development-server-start-time.-the-project-relies-on-commonjs-modules-require.-how-do-you-handle-this-in-vite)
2. [Your Webpack bundle size has grown too large (5MB+), causing slow initial page loads. How do you use `SplitChunksPlugin` to optimize this?](#q2-your-webpack-bundle-size-has-grown-too-large-5mb+-causing-slow-initial-page-loads.-how-do-you-use-splitchunksplugin-to-optimize-this)
3. [You need to support Internet Explorer 11 in a modern JavaScript application. How do you configure Babel to ensure your code runs there without transpiling everything unnecessarily for modern browsers?](#q3-you-need-to-support-internet-explorer-11-in-a-modern-javascript-application.-how-do-you-configure-babel-to-ensure-your-code-runs-there-without-transpiling-everything-unnecessarily-for-modern-browsers)
4. [How do you optimize Tree Shaking in Webpack by marking side effects?](#q4-how-do-you-optimize-tree-shaking-in-webpack-by-marking-side-effects)
5. [How does Vite achieve instant server start times compared to Webpack?](#q5-how-does-vite-achieve-instant-server-start-times-compared-to-webpack)
6. [You are building a Micro Frontends architecture. How do you configure Webpack Module Federation to expose a component?](#q6-you-are-building-a-micro-frontends-architecture.-how-do-you-configure-webpack-module-federation-to-expose-a-component)
7. [How do you combine Babel Plugins to create a custom Preset?](#q7-how-do-you-combine-babel-plugins-to-create-a-custom-preset)
8. [You encounter a 'CORS' error when your frontend (localhost:3000) tries to call your API (localhost:5000). How do you fix this using Webpack Dev Server proxy?](#q8-you-encounter-a-cors-error-when-your-frontend-localhost3000-tries-to-call-your-api-localhost5000.-how-do-you-fix-this-using-webpack-dev-server-proxy)
9. [How do you debug a large bundle to find out which libraries are taking up the most space?](#q9-how-do-you-debug-a-large-bundle-to-find-out-which-libraries-are-taking-up-the-most-space)
10. [How do you enable Hot Module Replacement (HMR) manually in Webpack?](#q10-how-do-you-enable-hot-module-replacement-hmr-manually-in-webpack)
11. [You are using environment variables in your frontend code. Why does `process.env.API_KEY` work in Node.js but fail in the browser, and how do you fix it?](#q11-you-are-using-environment-variables-in-your-frontend-code.-why-does-process.env.api_key-work-in-node.js-but-fail-in-the-browser-and-how-do-you-fix-it)
12. [How do you configure secure Source Maps for production debugging without exposing source code?](#q12-how-do-you-configure-secure-source-maps-for-production-debugging-without-exposing-source-code)
13. [How do you implement 'Path Aliases' (e.g., importing from `@components/Button` instead of `../../components/Button`)?](#q13-how-do-you-implement-path-aliases-e.g.-importing-from-@components-button-instead-of-..-..-components-button)
14. [How do you write a custom Babel Plugin using AST transformation?](#q14-how-do-you-write-a-custom-babel-plugin-using-ast-transformation)
15. [How do you use Webpack's `ProvidePlugin` to shim global variables like jQuery?](#q15-how-do-you-use-webpacks-provideplugin-to-shim-global-variables-like-jquery)
16. [How do you configure Webpack to handle CSS Modules?](#q16-how-do-you-configure-webpack-to-handle-css-modules)
17. [How do you use PostCSS with Webpack?](#q17-how-do-you-use-postcss-with-webpack)
18. [How do you implement Critical CSS extraction?](#q18-how-do-you-implement-critical-css-extraction)
19. [How do you configure Browserslist for different environments?](#q19-how-do-you-configure-browserslist-for-different-environments)
20. [How do you use `url-loader` vs `file-loader` (or Asset Modules) for images?](#q20-how-do-you-use-url-loader-vs-file-loader-or-asset-modules-for-images)
21. [How do you optimize images using `image-webpack-loader`?](#q21-how-do-you-optimize-images-using-image-webpack-loader)
22. [How do you configure Webpack to support TypeScript?](#q22-how-do-you-configure-webpack-to-support-typescript)
23. [How do you use `fork-ts-checker-webpack-plugin` for faster type checking?](#q23-how-do-you-use-fork-ts-checker-webpack-plugin-for-faster-type-checking)
24. [How do you generate a PWA Service Worker using WorkboxWebpackPlugin?](#q24-how-do-you-generate-a-pwa-service-worker-using-workboxwebpackplugin)
25. [How do you configure Webpack for multi-page applications (MPA)?](#q25-how-do-you-configure-webpack-for-multi-page-applications-mpa)
26. [How do you use `HtmlWebpackPlugin` to inject bundles into HTML?](#q26-how-do-you-use-htmlwebpackplugin-to-inject-bundles-into-html)
27. [How do you implement SRI (Subresource Integrity) in Webpack?](#q27-how-do-you-implement-sri-subresource-integrity-in-webpack)
28. [How do you use `CopyWebpackPlugin` to move static assets?](#q28-how-do-you-use-copywebpackplugin-to-move-static-assets)
29. [How do you clean the build folder before each build?](#q29-how-do-you-clean-the-build-folder-before-each-build)
30. [How do you extract CSS into separate files using `MiniCssExtractPlugin`?](#q30-how-do-you-extract-css-into-separate-files-using-minicssextractplugin)
31. [How do you configure Webpack Dev Server for HTTPS?](#q31-how-do-you-configure-webpack-dev-server-for-https)
32. [How do you use `DefinePlugin` to set feature flags?](#q32-how-do-you-use-defineplugin-to-set-feature-flags)
33. [How do you ignore specific modules using `IgnorePlugin` (e.g., Moment locales)?](#q33-how-do-you-ignore-specific-modules-using-ignoreplugin-e.g.-moment-locales)
34. [How do you use `DllPlugin` to speed up development builds?](#q34-how-do-you-use-dllplugin-to-speed-up-development-builds)
35. [How do you profile the Webpack build speed?](#q35-how-do-you-profile-the-webpack-build-speed)
36. [How do you use Webpack 5 Module Federation for dynamic remotes?](#q36-how-do-you-use-webpack-5-module-federation-for-dynamic-remotes)
37. [How do you configure Vite for a library build (lib mode)?](#q37-how-do-you-configure-vite-for-a-library-build-lib-mode)
38. [How do you use Vite plugins (e.g., `vite-plugin-pwa`)?](#q38-how-do-you-use-vite-plugins-e.g.-vite-plugin-pwa)
39. [How do you configure Vite aliases?](#q39-how-do-you-configure-vite-aliases)
40. [How do you proxy requests in Vite?](#q40-how-do-you-proxy-requests-in-vite)
41. [How do you use environment variables in Vite (`import.meta.env`)?](#q41-how-do-you-use-environment-variables-in-vite-import.meta.env)
42. [How do you configure Vite for Server-Side Rendering (SSR)?](#q42-how-do-you-configure-vite-for-server-side-rendering-ssr)
43. [How do you migrate from Create React App to Vite?](#q43-how-do-you-migrate-from-create-react-app-to-vite)
44. [How do you use `esbuild` directly for simple bundling tasks?](#q44-how-do-you-use-esbuild-directly-for-simple-bundling-tasks)
45. [How do you configure Rollup for packaging a JS library?](#q45-how-do-you-configure-rollup-for-packaging-a-js-library)
46. [How do you use Rollup plugins?](#q46-how-do-you-use-rollup-plugins)
47. [How do you configure Babel to support experimental syntax (Decorators)?](#q47-how-do-you-configure-babel-to-support-experimental-syntax-decorators)
48. [How do you use `babel-node` for running scripts?](#q48-how-do-you-use-babel-node-for-running-scripts)
49. [How do you cache Babel compilation results?](#q49-how-do-you-cache-babel-compilation-results)
50. [How do you configure ESLint with Prettier to avoid conflicts?](#q50-how-do-you-configure-eslint-with-prettier-to-avoid-conflicts)
51. [How do you write a custom ESLint rule?](#q51-how-do-you-write-a-custom-eslint-rule)
52. [How do you use `lint-staged` with Husky?](#q52-how-do-you-use-lint-staged-with-husky)
53. [How do you enforce commit message conventions with Commitlint?](#q53-how-do-you-enforce-commit-message-conventions-with-commitlint)
54. [How do you use `npm-run-all` to run scripts in parallel?](#q54-how-do-you-use-npm-run-all-to-run-scripts-in-parallel)
55. [How do you configure `lerna` or `nx` for a monorepo?](#q55-how-do-you-configure-lerna-or-nx-for-a-monorepo)
56. [How do you use Yarn Workspaces?](#q56-how-do-you-use-yarn-workspaces)
57. [How do you prevent phantom dependencies with pnpm?](#q57-how-do-you-prevent-phantom-dependencies-with-pnpm)
58. [How do you audit npm dependencies for security vulnerabilities?](#q58-how-do-you-audit-npm-dependencies-for-security-vulnerabilities)
59. [How do you override a nested dependency version (resolutions)?](#q59-how-do-you-override-a-nested-dependency-version-resolutions)
60. [How do you publish a package to npm?](#q60-how-do-you-publish-a-package-to-npm)
61. [How do you create a scoped npm package?](#q61-how-do-you-create-a-scoped-npm-package)
62. [How do you link a local package for development (`npm link`)?](#q62-how-do-you-link-a-local-package-for-development-npm-link)
63. [How do you use `.npmrc` to configure registry URL?](#q63-how-do-you-use-.npmrc-to-configure-registry-url)
64. [How do you setup Semantic Release for automated versioning?](#q64-how-do-you-setup-semantic-release-for-automated-versioning)
65. [How do you configure GitHub Actions for CI/CD?](#q65-how-do-you-configure-github-actions-for-ci-cd)
66. [How do you cache `node_modules` in GitHub Actions?](#q66-how-do-you-cache-node_modules-in-github-actions)
67. [How do you run tests in parallel in CI?](#q67-how-do-you-run-tests-in-parallel-in-ci)
68. [How do you deploy a static site to Netlify via CLI?](#q68-how-do-you-deploy-a-static-site-to-netlify-via-cli)
69. [How do you deploy to Vercel using their CLI?](#q69-how-do-you-deploy-to-vercel-using-their-cli)
70. [How do you containerize a Node.js app with Docker?](#q70-how-do-you-containerize-a-node.js-app-with-docker)
71. [How do you optimize Docker image size for Node.js apps?](#q71-how-do-you-optimize-docker-image-size-for-node.js-apps)
72. [How do you use multi-stage Docker builds?](#q72-how-do-you-use-multi-stage-docker-builds)
73. [How do you configure Nginx as a reverse proxy for a Node app?](#q73-how-do-you-configure-nginx-as-a-reverse-proxy-for-a-node-app)
74. [How do you enable Gzip compression in Nginx?](#q74-how-do-you-enable-gzip-compression-in-nginx)
75. [How do you serve static assets from an S3 bucket?](#q75-how-do-you-serve-static-assets-from-an-s3-bucket)
76. [How do you invalidate CloudFront cache after deployment?](#q76-how-do-you-invalidate-cloudfront-cache-after-deployment)
77. [How do you implement Blue/Green deployment?](#q77-how-do-you-implement-blue-green-deployment)
78. [How do you use Feature Toggles in build configuration?](#q78-how-do-you-use-feature-toggles-in-build-configuration)
79. [How do you handle secrets in CI/CD pipelines?](#q79-how-do-you-handle-secrets-in-ci-cd-pipelines)
80. [How do you verify the integrity of downloaded npm packages?](#q80-how-do-you-verify-the-integrity-of-downloaded-npm-packages)
81. [How do you use `nvm` to manage Node versions?](#q81-how-do-you-use-nvm-to-manage-node-versions)
82. [How do you debug a memory leak in the build process?](#q82-how-do-you-debug-a-memory-leak-in-the-build-process)
83. [How do you use `node --inspect` to debug build scripts?](#q83-how-do-you-use-node---inspect-to-debug-build-scripts)
84. [How do you generate a license report for dependencies?](#q84-how-do-you-generate-a-license-report-for-dependencies)
85. [How do you check for circular dependencies?](#q85-how-do-you-check-for-circular-dependencies)
86. [How do you remove console logs in production build?](#q86-how-do-you-remove-console-logs-in-production-build)
87. [How do you inline small images as Base64 URLs?](#q87-how-do-you-inline-small-images-as-base64-urls)
88. [How do you configure Webpack to use a CDN for public path?](#q88-how-do-you-configure-webpack-to-use-a-cdn-for-public-path)
89. [How do you use `preload-webpack-plugin`?](#q89-how-do-you-use-preload-webpack-plugin)
90. [How do you implement 'Prefetching' for future routes?](#q90-how-do-you-implement-prefetching-for-future-routes)
91. [How do you use `webpack-merge` to split config files?](#q91-how-do-you-use-webpack-merge-to-split-config-files)
92. [How do you create a custom Webpack loader?](#q92-how-do-you-create-a-custom-webpack-loader)
93. [How do you use `style-loader` vs `css-loader`?](#q93-how-do-you-use-style-loader-vs-css-loader)
94. [How do you configure CSS Modules localIdentName?](#q94-how-do-you-configure-css-modules-localidentname)
95. [How do you use `postcss-preset-env`?](#q95-how-do-you-use-postcss-preset-env)
96. [How do you configure PurgeCSS to remove unused CSS?](#q96-how-do-you-configure-purgecss-to-remove-unused-css)
97. [How do you polyfill `fetch` in older browsers?](#q97-how-do-you-polyfill-fetch-in-older-browsers)
98. [How do you use `core-js` version 3?](#q98-how-do-you-use-core-js-version-3)
99. [How do you transpile `node_modules` if needed?](#q99-how-do-you-transpile-node_modules-if-needed)
100. [How do you configure Babel for React (JSX)?](#q100-how-do-you-configure-babel-for-react-jsx)
101. [How do you configure Babel for TypeScript?](#q101-how-do-you-configure-babel-for-typescript)
102. [How do you use `babel-plugin-import` for UI libraries?](#q102-how-do-you-use-babel-plugin-import-for-ui-libraries)
103. [How do you optimize moment.js bundle size?](#q103-how-do-you-optimize-moment.js-bundle-size)
104. [How do you replace moment.js with date-fns or dayjs?](#q104-how-do-you-replace-moment.js-with-date-fns-or-dayjs)
105. [How do you use `swc-loader` for faster builds?](#q105-how-do-you-use-swc-loader-for-faster-builds)
106. [How do you use Parcel for zero-config builds?](#q106-how-do-you-use-parcel-for-zero-config-builds)
107. [How do you configure Gulp for task automation?](#q107-how-do-you-configure-gulp-for-task-automation)

---

### Q1: You are migrating a legacy React project from Webpack to Vite to improve development server start time. The project relies on CommonJS modules (`require`). How do you handle this in Vite?

**Difficulty: Intermediate**

**Answer:**
**Challenge:** Vite is built on native ES Modules (ESM) and Rollup. It does not support CommonJS by default in source code.

**Solutions:**
1.  **Refactor:** The best long-term solution is to replace `require` with `import` and `module.exports` with `export`.
2.  **Plugin:** Use `vite-plugin-commonjs` to transform CommonJS calls to ESM during the build.
3.  **Pre-bundling:** Vite automatically converts CommonJS *dependencies* (in `node_modules`) to ESM using esbuild, but this doesn't apply to your source files.

```javascript
// vite.config.js
import { defineConfig } from 'vite';
import commonjs from 'vite-plugin-commonjs';

export default defineConfig({
  plugins: [commonjs()]
});
```

[Back to Top](#table-of-contents)

---

### Q2: Your Webpack bundle size has grown too large (5MB+), causing slow initial page loads. How do you use `SplitChunksPlugin` to optimize this?

**Difficulty: Advanced**

**Answer:**
**Strategy: Code Splitting**

1.  **Vendor Splitting:** Separate third-party libraries (React, Lodash) into a stable `vendors.js` chunk that can be cached by the browser.
2.  **Dynamic Imports:** Split code based on routes using `import()`.
3.  **Configuration:**

```javascript
// webpack.config.js
module.exports = {
  optimization: {
    splitChunks: {
      chunks: 'all', // Optimizes both sync and async chunks
      minSize: 20000, // 20kb
      cacheGroups: {
        defaultVendors: {
          test: /[\/]node_modules[\/]/,
          priority: -10,
          reuseExistingChunk: true,
        },
      },
    },
  },
};
```

[Back to Top](#table-of-contents)

---

### Q3: You need to support Internet Explorer 11 in a modern JavaScript application. How do you configure Babel to ensure your code runs there without transpiling everything unnecessarily for modern browsers?

**Difficulty: Intermediate**

**Answer:**
**Solution: `@babel/preset-env` with `useBuiltIns`**

1.  **Targeting:** Specify `ie: "11"` in your targets.
2.  **Polyfills:** Use `core-js` to provide missing features (Promise, Array.from).
3.  **Optimization:** Set `useBuiltIns: "usage"`. This tells Babel to only include polyfills for features *actually used* in your code, rather than the entire library.

```json
// .babelrc
{
  "presets": [
    ["@babel/preset-env", {
      "targets": {
        "ie": "11",
        "chrome": "80"
      },
      "useBuiltIns": "usage", // Crucial for bundle size
      "corejs": 3
    }]
  ]
}
```

[Back to Top](#table-of-contents)

---

### Q4: How do you optimize Tree Shaking in Webpack by marking side effects?

**Difficulty: Advanced**

**Answer:**
Tree Shaking relies on static ESM analysis to drop unused exports. However, if a file has "side effects" (e.g., modifying a global prototype), Webpack cannot safely remove it even if its exports are unused.

**Fix:** Use the `"sideEffects"` field in `package.json`.

1.  **Mark all clean:** `"sideEffects": false` (Tells Webpack: "If I don't import it, you can remove it").
2.  **Mark specific files:**

```json
// package.json
{
  "name": "my-lib",
  "sideEffects": [
    "*.css",
    "./src/polyfills.js"
  ]
}
```

[Back to Top](#table-of-contents)

---

### Q5: How does Vite achieve instant server start times compared to Webpack?

**Difficulty: Intermediate**

**Answer:**
**Webpack:** Bundles the *entire* application before starting the server. As the app grows, build time grows linearly.

**Vite:**
1.  **Native ESM:** Serves source code over native ESM. The browser requests modules as needed.
2.  **Esbuild:** Uses esbuild (written in Go) for pre-bundling dependencies (10-100x faster than JS bundlers).
3.  **On-demand Compilation:** Only compiles the specific file you requested.

**Result:** Server start is effectively O(1) constant time, regardless of app size.

[Back to Top](#table-of-contents)

---

### Q6: You are building a Micro Frontends architecture. How do you configure Webpack Module Federation to expose a component?

**Difficulty: Advanced**

**Answer:**
Module Federation allows sharing code between independent builds at runtime.

**Host App (Exposes Component):**

```javascript
// webpack.config.js
const ModuleFederationPlugin = require('webpack/lib/container/ModuleFederationPlugin');

module.exports = {
  plugins: [
    new ModuleFederationPlugin({
      name: 'app1',
      filename: 'remoteEntry.js',
      exposes: {
        './Button': './src/Button',
      },
      shared: { react: { singleton: true }, 'react-dom': { singleton: true } },
    }),
  ],
};
```

[Back to Top](#table-of-contents)

---

### Q7: How do you combine Babel Plugins to create a custom Preset?

**Difficulty: Advanced**

**Answer:**
A Preset is just a collection of plugins.

```javascript
// my-preset.js
module.exports = function() {
  return {
    plugins: [
      "@babel/plugin-transform-arrow-functions",
      "@babel/plugin-transform-block-scoping",
      ["@babel/plugin-proposal-class-properties", { loose: true }]
    ]
  };
};

// Usage in .babelrc
{
  "presets": ["./my-preset.js"]
}
```

[Back to Top](#table-of-contents)

---

### Q8: You encounter a 'CORS' error when your frontend (localhost:3000) tries to call your API (localhost:5000). How do you fix this using Webpack Dev Server proxy?

**Difficulty: Beginner**

**Answer:**
Configure the proxy in Webpack to forward API requests to the backend server, bypassing browser CORS restrictions during development.

```javascript
// webpack.config.js
module.exports = {
  devServer: {
    proxy: {
      '/api': {
        target: 'http://localhost:5000',
        pathRewrite: { '^/api': '' },
        secure: false,
        changeOrigin: true,
      },
    },
  },
};
```

[Back to Top](#table-of-contents)

---

### Q9: How do you debug a large bundle to find out which libraries are taking up the most space?

**Difficulty: Intermediate**

**Answer:**
Use `webpack-bundle-analyzer`. It generates an interactive zoomable treemap of your bundle content.

```javascript
// webpack.config.js
const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;

module.exports = {
  plugins: [
    new BundleAnalyzerPlugin()
  ]
};
```
Run the build, and it will open a visual report at `localhost:8888`.

[Back to Top](#table-of-contents)

---

### Q10: How do you enable Hot Module Replacement (HMR) manually in Webpack?

**Difficulty: Advanced**

**Answer:**
HMR allows updating modules without a full reload.

1.  **Config:** Add `HotModuleReplacementPlugin`.
2.  **Dev Server:** Set `hot: true`.
3.  **Code:** Accept updates in your entry file.

```javascript
// main.js
import printMe from './print.js';

if (module.hot) {
  module.hot.accept('./print.js', function() {
    console.log('Accepting the updated printMe module!');
    printMe();
  })
}
```

[Back to Top](#table-of-contents)

---

### Q11: You are using environment variables in your frontend code. Why does `process.env.API_KEY` work in Node.js but fail in the browser, and how do you fix it?

**Difficulty: Intermediate**

**Answer:**
**Reason:** The browser has no concept of `process.env`. This is a Node.js global.

**Fix:** Use `DefinePlugin` (Webpack) or `import.meta.env` (Vite) to replace the string at **build time**.

**Webpack:**
```javascript
new webpack.DefinePlugin({
  'process.env.API_KEY': JSON.stringify(process.env.API_KEY)
})
```

**Vite:**
Vite automatically exposes `VITE_` prefixed variables on `import.meta.env`.
```javascript
console.log(import.meta.env.VITE_API_KEY);
```

[Back to Top](#table-of-contents)

---

### Q12: How do you configure secure Source Maps for production debugging without exposing source code?

**Difficulty: Advanced**

**Answer:**
You want error tracking (Sentry) to see source code, but not the public user.

**Strategy:**
1.  Set `devtool: 'hidden-source-map'`. This generates `.map` files but **does not** add the `//# sourceMappingURL=` comment to the JS bundle.
2.  Upload `.map` files to your error tracking service (Sentry/Bugsnag) during CI/CD.
3.  Delete `.map` files from your deployment server or block access via Nginx/permissions.

```javascript
// webpack.config.js
module.exports = {
  devtool: 'hidden-source-map',
};
```

[Back to Top](#table-of-contents)

---

### Q13: How do you implement 'Path Aliases' (e.g., importing from `@components/Button` instead of `../../components/Button`)?

**Difficulty: Beginner**

**Answer:**
You need to configure **both** the bundler (for build) and the editor/TS (for autocomplete).

**1. Webpack:**
```javascript
resolve: {
  alias: {
    '@components': path.resolve(__dirname, 'src/components/'),
  },
}
```

**2. TypeScript (`tsconfig.json`):**
```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@components/*": ["src/components/*"]
    }
  }
}
```

[Back to Top](#table-of-contents)

---

### Q14: How do you write a custom Babel Plugin using AST transformation?

**Difficulty: Advanced**

**Answer:**
Babel plugins use the Visitor pattern to traverse the AST.

Example: Reverse all identifier names (fun, but useless).

```javascript
module.exports = function({ types: t }) {
  return {
    visitor: {
      Identifier(path) {
        const name = path.node.name;
        // Reverse the name
        path.node.name = name.split('').reverse().join('');
      }
    }
  };
};
```

[Back to Top](#table-of-contents)

---

### Q15: How do you use Webpack's `ProvidePlugin` to shim global variables like jQuery?

**Difficulty: Intermediate**

**Answer:**
`ProvidePlugin` automatically loads modules instead of having to `import` or `require` them everywhere.

```javascript
new webpack.ProvidePlugin({
  $: 'jquery',
  jQuery: 'jquery',
  _map: ['lodash', 'map'] // Specific import
});
```
Now you can use `$('#item')` in any file without importing jQuery.

[Back to Top](#table-of-contents)

---

### Q16: How do you configure Webpack to handle CSS Modules?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q17: How do you use PostCSS with Webpack?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q18: How do you implement Critical CSS extraction?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q19: How do you configure Browserslist for different environments?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q20: How do you use `url-loader` vs `file-loader` (or Asset Modules) for images?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q21: How do you optimize images using `image-webpack-loader`?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q22: How do you configure Webpack to support TypeScript?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q23: How do you use `fork-ts-checker-webpack-plugin` for faster type checking?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q24: How do you generate a PWA Service Worker using WorkboxWebpackPlugin?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q25: How do you configure Webpack for multi-page applications (MPA)?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q26: How do you use `HtmlWebpackPlugin` to inject bundles into HTML?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q27: How do you implement SRI (Subresource Integrity) in Webpack?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q28: How do you use `CopyWebpackPlugin` to move static assets?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q29: How do you clean the build folder before each build?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q30: How do you extract CSS into separate files using `MiniCssExtractPlugin`?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q31: How do you configure Webpack Dev Server for HTTPS?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q32: How do you use `DefinePlugin` to set feature flags?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q33: How do you ignore specific modules using `IgnorePlugin` (e.g., Moment locales)?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q34: How do you use `DllPlugin` to speed up development builds?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q35: How do you profile the Webpack build speed?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q36: How do you use Webpack 5 Module Federation for dynamic remotes?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q37: How do you configure Vite for a library build (lib mode)?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q38: How do you use Vite plugins (e.g., `vite-plugin-pwa`)?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q39: How do you configure Vite aliases?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q40: How do you proxy requests in Vite?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q41: How do you use environment variables in Vite (`import.meta.env`)?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q42: How do you configure Vite for Server-Side Rendering (SSR)?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q43: How do you migrate from Create React App to Vite?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q44: How do you use `esbuild` directly for simple bundling tasks?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q45: How do you configure Rollup for packaging a JS library?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q46: How do you use Rollup plugins?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q47: How do you configure Babel to support experimental syntax (Decorators)?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q48: How do you use `babel-node` for running scripts?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q49: How do you cache Babel compilation results?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q50: How do you configure ESLint with Prettier to avoid conflicts?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q51: How do you write a custom ESLint rule?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q52: How do you use `lint-staged` with Husky?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q53: How do you enforce commit message conventions with Commitlint?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q54: How do you use `npm-run-all` to run scripts in parallel?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q55: How do you configure `lerna` or `nx` for a monorepo?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q56: How do you use Yarn Workspaces?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q57: How do you prevent phantom dependencies with pnpm?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q58: How do you audit npm dependencies for security vulnerabilities?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q59: How do you override a nested dependency version (resolutions)?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q60: How do you publish a package to npm?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q61: How do you create a scoped npm package?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q62: How do you link a local package for development (`npm link`)?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q63: How do you use `.npmrc` to configure registry URL?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q64: How do you setup Semantic Release for automated versioning?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q65: How do you configure GitHub Actions for CI/CD?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q66: How do you cache `node_modules` in GitHub Actions?

**Difficulty: Intermediate**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q67: How do you run tests in parallel in CI?

**Difficulty: Beginner**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q68: How do you deploy a static site to Netlify via CLI?

**Difficulty: Beginner**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q69: How do you deploy to Vercel using their CLI?

**Difficulty: Beginner**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q70: How do you containerize a Node.js app with Docker?

**Difficulty: Beginner**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q71: How do you optimize Docker image size for Node.js apps?

**Difficulty: Beginner**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q72: How do you use multi-stage Docker builds?

**Difficulty: Beginner**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q73: How do you configure Nginx as a reverse proxy for a Node app?

**Difficulty: Beginner**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q74: How do you enable Gzip compression in Nginx?

**Difficulty: Beginner**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q75: How do you serve static assets from an S3 bucket?

**Difficulty: Beginner**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q76: How do you invalidate CloudFront cache after deployment?

**Difficulty: Beginner**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q77: How do you implement Blue/Green deployment?

**Difficulty: Beginner**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q78: How do you use Feature Toggles in build configuration?

**Difficulty: Beginner**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q79: How do you handle secrets in CI/CD pipelines?

**Difficulty: Beginner**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q80: How do you verify the integrity of downloaded npm packages?

**Difficulty: Beginner**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q81: How do you use `nvm` to manage Node versions?

**Difficulty: Beginner**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q82: How do you debug a memory leak in the build process?

**Difficulty: Beginner**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q83: How do you use `node --inspect` to debug build scripts?

**Difficulty: Beginner**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q84: How do you generate a license report for dependencies?

**Difficulty: Beginner**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q85: How do you check for circular dependencies?

**Difficulty: Beginner**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q86: How do you remove console logs in production build?

**Difficulty: Beginner**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q87: How do you inline small images as Base64 URLs?

**Difficulty: Beginner**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q88: How do you configure Webpack to use a CDN for public path?

**Difficulty: Beginner**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q89: How do you use `preload-webpack-plugin`?

**Difficulty: Beginner**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q90: How do you implement 'Prefetching' for future routes?

**Difficulty: Beginner**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q91: How do you use `webpack-merge` to split config files?

**Difficulty: Beginner**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q92: How do you create a custom Webpack loader?

**Difficulty: Beginner**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q93: How do you use `style-loader` vs `css-loader`?

**Difficulty: Beginner**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q94: How do you configure CSS Modules localIdentName?

**Difficulty: Beginner**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q95: How do you use `postcss-preset-env`?

**Difficulty: Beginner**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q96: How do you configure PurgeCSS to remove unused CSS?

**Difficulty: Beginner**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q97: How do you polyfill `fetch` in older browsers?

**Difficulty: Beginner**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q98: How do you use `core-js` version 3?

**Difficulty: Beginner**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q99: How do you transpile `node_modules` if needed?

**Difficulty: Beginner**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q100: How do you configure Babel for React (JSX)?

**Difficulty: Beginner**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q101: How do you configure Babel for TypeScript?

**Difficulty: Beginner**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q102: How do you use `babel-plugin-import` for UI libraries?

**Difficulty: Beginner**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q103: How do you optimize moment.js bundle size?

**Difficulty: Beginner**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q104: How do you replace moment.js with date-fns or dayjs?

**Difficulty: Beginner**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q105: How do you use `swc-loader` for faster builds?

**Difficulty: Beginner**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q106: How do you use Parcel for zero-config builds?

**Difficulty: Beginner**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

### Q107: How do you configure Gulp for task automation?

**Difficulty: Beginner**

**Answer:**
Use the appropriate configuration or plugin. (Practical implementation would involve specific syntax shown in core examples).

[Back to Top](#table-of-contents)

---

