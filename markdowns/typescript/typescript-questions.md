<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="TypeScript Logo" width="100" height="100">
  </a>
  <h1>TypeScript Interview Questions & Answers</h1>
  <p><b>Comprehensive interview questions covering Type System, Generics, Conditional Types, and tsconfig</b></p>
</div>

---

## Table of Contents

1. [What is the difference between `interface` and `type` in TypeScript, and when should you choose one over the other?](#q1) <span class="intermediate">Intermediate</span>
2. [Explain Conditional Types and the `infer` keyword in TypeScript?](#q2) <span class="advanced">Advanced</span>
3. [How do Mapped Types and Template Literal Types work in TypeScript?](#q3) <span class="advanced">Advanced</span>
4. [What is the difference between `any`, `unknown`, `never`, and `void`?](#q4) <span class="beginner">Beginner</span>
5. [How do Const Assertions (`as const`) and Satisfies Operator (`satisfies`) work?](#q5) <span class="intermediate">Intermediate</span>
6. [What are Generics and Generic Constraints (`T extends object`) in TypeScript?](#q6) <span class="beginner">Beginner</span>
7. [How do User-Defined Type Guards (`x is Type`) and Assertion Functions (`asserts x is Type`) work?](#q7) <span class="intermediate">Intermediate</span>
8. [What is the difference between `keyof`, `typeof`, and indexed access types (`T[K]`)?](#q8) <span class="intermediate">Intermediate</span>
9. [What are TypeScript Utility Types (`Partial`, `Required`, `Readonly`, `Record`, `Pick`, `Omit`, `Exclude`, `Extract`)?](#q9) <span class="intermediate">Intermediate</span>
10. [How does Discriminated Unions (Tagged Unions) enable safe pattern matching in TypeScript?](#q10) <span class="intermediate">Intermediate</span>
11. [What is Covariance, Contravariance, Invariance, and Bivariance in TypeScript Subtyping?](#q11) <span class="advanced">Advanced</span>
12. [What is the purpose of `noImplicitAny`, `strictNullChecks`, and `noUncheckedIndexedAccess` in `tsconfig.json`?](#q12) <span class="intermediate">Intermediate</span>
13. [How do Ambient Declarations (`.d.ts` files) and `declare module` work?](#q13) <span class="intermediate">Intermediate</span>
14. [What is the difference between `export type` and `export` in TypeScript 3.8+?](#q14) <span class="beginner">Beginner</span>
15. [How does Brand Typing (Nominal Typing) work in a structurally-typed language?](#q15) <span class="advanced">Advanced</span>
16. [What is the `override` keyword in TypeScript 4.3+ class methods?](#q16) <span class="beginner">Beginner</span>
17. [How do Function Overloads work in TypeScript?](#q17) <span class="intermediate">Intermediate</span>
18. [What is the difference between `readonly` array (`ReadonlyArray<T>`) and `const` array?](#q18) <span class="beginner">Beginner</span>
19. [How do Decorators work in TypeScript (Legacy Stage 2 vs Modern Stage 3 Decorators)?](#q19) <span class="advanced">Advanced</span>
20. [What is the purpose of `tsconfig.json` `moduleResolution: "bundler"` vs `"node16"`?](#q20) <span class="intermediate">Intermediate</span>
21. [How does `instanceof` narrowing work with classes in TypeScript?](#q21) <span class="beginner">Beginner</span>
22. [What is the difference between `in` operator type narrowing and property checking?](#q22) <span class="beginner">Beginner</span>
23. [How do recursive types work in TypeScript for JSON structures?](#q23) <span class="advanced">Advanced</span>
24. [What is the purpose of `ThisType<T>` utility type?](#q24) <span class="advanced">Advanced</span>
25. [How do you configure Project References and Composite Projects for large TypeScript monorepos?](#q25) <span class="advanced">Advanced</span>
26. [What are Template Literal Types and how do they enable advanced string manipulation at the type level?](#q26) <span class="advanced">Advanced</span>
27. [How do Conditional Types distribute over unions, and how do you prevent distribution?](#q27) <span class="advanced">Advanced</span>
28. [How does `infer` work inside conditional types?](#q28) <span class="advanced">Advanced</span>
29. [What are Mapped Types and Key Remapping via `as`?](#q29) <span class="intermediate">Intermediate</span>
30. [Explain `keyof`, index access types, and the `KeyofTrait` for exhaustive Records?](#q30) <span class="intermediate">Intermediate</span>
31. [What is `satisfies` (TS 4.9) and how does it differ from a type annotation?](#q31) <span class="intermediate">Intermediate</span>
32. [What are `const` Type Parameters (TS 5.0) and when do you reach for them?](#q32) <span class="advanced">Advanced</span>
33. [What problem does `NoInfer<T>` (TS 5.4) solve?](#q33) <span class="advanced">Advanced</span>
34. [How do ECMAScript Stage-3 Decorators (TS 5.0) differ from legacy `experimentalDecorators`?](#q34) <span class="advanced">Advanced</span>
35. [Why are `enum`s controversial, and what are the alternatives?](#q35) <span class="intermediate">Intermediate</span>
36. [What does `unknown` enforce that `any` does not?](#q36) <span class="beginner">Beginner</span>
37. [How do you use `never` for exhaustiveness checking?](#q37) <span class="intermediate">Intermediate</span>
38. [What are Discriminated Unions and why are they TS's best modeling tool?](#q38) <span class="intermediate">Intermediate</span>
39. [Explain variance: covariance, contravariance, and bivariance in TypeScript?](#q39) <span class="expert">Expert</span>
40. [What are Branded (Nominal) types and why does structural typing need them?](#q40) <span class="advanced">Advanced</span>
41. [How do Variadic Tuple Types work?](#q41) <span class="advanced">Advanced</span>
42. [What is declaration merging, and which declarations merge?](#q42) <span class="intermediate">Intermediate</span>
43. [interface vs type alias — when does the choice matter?](#q43) <span class="beginner">Beginner</span>
44. [How do `readonly`, `Readonly<T>`, `ReadonlyArray<T>`, and `as const` differ?](#q44) <span class="intermediate">Intermediate</span>
45. [How do User-Defined Type Guards and Assertion Functions differ in control-flow effects?](#q45) <span class="intermediate">Intermediate</span>
46. [How do you type generics with defaults and multiple constraints?](#q46) <span class="intermediate">Intermediate</span>
47. [What are the strict-family flags a production tsconfig should enable?](#q47) <span class="intermediate">Intermediate</span>
48. [What does `noUncheckedIndexedAccess` change and how do you code around it?](#q48) <span class="intermediate">Intermediate</span>
49. [How does module resolution differ between `node16`, `bundler`, and classic `node` modes?](#q49) <span class="advanced">Advanced</span>
50. [What does `verbatimModuleSyntax` enforce vs `isolatedModules`?](#q50) <span class="advanced">Advanced</span>
51. [How do `export =` and `esModuleInterop` interact for CJS interop?](#q51) <span class="advanced">Advanced</span>
52. [How do you write recursive and deeply-applied utility types (DeepPartial, DeepReadonly)?](#q52) <span class="advanced">Advanced</span>
53. [How would you implement built-in utilities `Pick`, `Omit`, `Partial`, and `ReturnType` yourself?](#q53) <span class="intermediate">Intermediate</span>
54. [How do function overloads compare with union-parameter signatures?](#q54) <span class="intermediate">Intermediate</span>
55. [What are abstract classes vs interfaces for shared contracts, and when is each right?](#q55) <span class="beginner">Beginner</span>
56. [How do Mixins work in TypeScript without classes-inheriting-classes?](#q56) <span class="advanced">Advanced</span>
57. [How do `private`, `#private`, and `protected` differ?](#q57) <span class="intermediate">Intermediate</span>
58. [What is type widening and how do literal types escape it?](#q58) <span class="intermediate">Intermediate</span>
59. [How does Control Flow Analysis narrow, and where does it fail?](#q59) <span class="intermediate">Intermediate</span>
60. [What are the pitfalls of non-null assertion (`!`) and better alternatives?](#q60) <span class="beginner">Beginner</span>
61. [How do you type `this` and polymorphic `this` for fluent APIs?](#q61) <span class="advanced">Advanced</span>
62. [How do Generators and AsyncGenerators interact with typing?](#q62) <span class="advanced">Advanced</span>
63. [What is Module Augmentation for third-party libraries?](#q63) <span class="advanced">Advanced</span>
64. [How do you type environment variables and external config safely?](#q64) <span class="intermediate">Intermediate</span>
65. [How do runtime validators (zod) bridge to compile-time types?](#q65) <span class="intermediate">Intermediate</span>
66. [What typing does `Awaited<T>` provide and how do you unwrap nested Promises?](#q66) <span class="intermediate">Intermediate</span>
67. [How do you model Result/Either-style error handling to avoid exceptions?](#q67) <span class="advanced">Advanced</span>
68. [How do you keep barrel files (`index.ts`) from hurting build performance?](#q68) <span class="intermediate">Intermediate</span>
69. [How does `skipLibCheck` trade safety for speed, and what does it skip exactly?](#q69) <span class="beginner">Beginner</span>
70. [How do Project References and `tsc --build` speed up monorepos?](#q70) <span class="advanced">Advanced</span>
71. [What are `incremental`, `.tsbuildinfo`, and `assumeChangesOnlyAffectDirectDependencies` for CI caching?](#q71) <span class="advanced">Advanced</span>
72. [How do path aliases work, and how do you keep bundler + tsc + jest in sync?](#q72) <span class="intermediate">Intermediate</span>
73. [How do you migrate a large JavaScript codebase to TypeScript incrementally?](#q73) <span class="advanced">Advanced</span>
74. [When is `@ts-ignore` acceptable versus `@ts-expect-error`?](#q74) <span class="beginner">Beginner</span>
75. [How do you unit-test types themselves?](#q75) <span class="advanced">Advanced</span>
76. [How does TypeScript's structural typing leak soundness with mutable properties?](#q76) <span class="expert">Expert</span>
77. [What are `unique symbol` and `symbol` registry patterns?](#q77) <span class="advanced">Advanced</span>
78. [How do you type React-generic components and forwardRef correctly in modern TS?](#q78) <span class="advanced">Advanced</span>
79. [How do you type event handlers and native events without `any`?](#q79) <span class="beginner">Beginner</span>
80. [How do you type fetch wrappers so errors and payloads are precise?](#q80) <span class="intermediate">Intermediate</span>
81. [What is the difference between `type` imports and regular imports for bundlers?](#q81) <span class="intermediate">Intermediate</span>
82. [How do `namespace`s survive today, and should new code use them?](#q82) <span class="intermediate">Intermediate</span>
83. [What are index signatures vs `Record` vs a fixed set of known keys?](#q83) <span class="beginner">Beginner</span>
84. [How do optional properties differ under `exactOptionalPropertyTypes`?](#q84) <span class="advanced">Advanced</span>
85. [How do you type curried functions and point-free composition?](#q85) <span class="expert">Expert</span>
86. [What are the typing rules for optional and rest parameters in implementations?](#q86) <span class="beginner">Beginner</span>
87. [How do conditional `infer` patterns extract array element, promise value, and function param types together?](#q87) <span class="advanced">Advanced</span>
88. [How do you write type-safe reducers for state machines?](#q88) <span class="advanced">Advanced</span>
89. [What are assertion-free strategies for typing JSON Schema / API contracts (OpenAPI codegen)?](#q89) <span class="intermediate">Intermediate</span>
90. [How do you avoid `any` when dealing with genuinely dynamic objects (records of callbacks, registries)?](#q90) <span class="intermediate">Intermediate</span>
91. [What is the `in` operator narrowing, and how does it interact with optional/private properties?](#q91) <span class="intermediate">Intermediate</span>
92. [How do you keep `Promise.all`-style combinators precisely typed with heterogeneous tuples?](#q92) <span class="intermediate">Intermediate</span>
93. [What are the typing subtleties of class static blocks and static members with generics?](#q93) <span class="advanced">Advanced</span>
94. [How do `ConstructorParameters`, `InstanceType`, and `AbstractConstructor` utilities work?](#q94) <span class="intermediate">Intermediate</span>
95. [How does `useDefineForClassFields` change class emit and interop with decorators?](#q95) <span class="expert">Expert</span>
96. [What typing strategies keep tRPC-like end-to-end inference working, and how would you build a minimal router?](#q96) <span class="expert">Expert</span>
97. [How do you encode "exactly one of" and "at least one of" constraints at the type level?](#q97) <span class="expert">Expert</span>
98. [What are the rules for typing getters/setters and readonly-only arrays in classes?](#q98) <span class="intermediate">Intermediate</span>
99. [How do you diagnose and fix TS performance problems (deep instantiation, large unions)?](#q99) <span class="expert">Expert</span>
100. [How do you structure a production-grade tsconfig for a Node.js + library + test matrix?](#q100) <span class="advanced">Advanced</span>

---

<a id="q1"></a>
### Q1: What is the difference between `interface` and `type` in TypeScript, and when should you choose one over the other?

**Difficulty**: Intermediate

**Strategy**:
- **`interface`**: Open for declaration merging (ideal for public APIs/libraries), extends with `extends`, supports object/class definitions only.
- **`type` alias**: Cannot be merged, supports primitives, unions (`type A = B | C`), intersections, tuples, mapped types, and conditional types.
*Best Practice*: Use `interface` for public OOP APIs and polymorphic contracts; use `type` for complex utility types, unions, and React component props.

**Code Example**:
```typescript
// Declaration Merging with interface
interface User { name: string; }
interface User { age: number; }
const u: User = { name: 'Alice', age: 30 }; // Merged

// Union and Utility Types with type
type Status = 'idle' | 'loading' | 'success' | 'error';
type Action<T> = { type: 'SET_DATA'; payload: T } | { type: 'RESET' };
```

---

<a id="q2"></a>
### Q2: Explain Conditional Types and the `infer` keyword in TypeScript?

**Difficulty**: Advanced

**Strategy**:
Conditional types select one of two possible types based on type relationships (`T extends U ? X : Y`). The `infer` keyword introduces a type variable within the `extends` clause to deduce and extract internal types dynamically (e.g. ReturnType, Promise unwrap).

**Code Example**:
```typescript
// Unwrap Promise / Awaited type using infer
type MyAwaited<T> = T extends Promise<infer U> ? MyAwaited<U> : T;

type Res = MyAwaited<Promise<Promise<string>>>; // string

// Extract Function Parameters
type MyParameters<T> = T extends (...args: infer P) => any ? P : never;
```

---

<a id="q3"></a>
### Q3: How do Mapped Types and Template Literal Types work in TypeScript?

**Difficulty**: Advanced

**Strategy**:
Mapped types iterate over union keys using `[K in keyof T]` to construct new types with modifiers (`readonly`, `?`, `-?`). Template literal types build string types based on string concatenation patterns.

**Code Example**:
```typescript
// Custom DeepReadonly Mapped Type
type DeepReadonly<T> = {
  readonly [K in keyof T]: T[K] extends object ? DeepReadonly<T[K]> : T[K];
};

// Template Literal Types for Event Handlers
type EventName = 'click' | 'hover' | 'focus';
type EventHandler = `on${Capitalize<EventName>}`;
// 'onClick' | 'onHover' | 'onFocus'
```

---

<a id="q4"></a>
### Q4: What is the difference between `any`, `unknown`, `never`, and `void`?

**Difficulty**: Beginner

**Strategy**:
- `any`: Disables all type checking (unsafe escape hatch).
- `unknown`: Type-safe counterpart of `any`; requires type narrowing/guards before performing operations.
- `never`: Represents values that never occur (exhaustive switch checks, functions throwing infinite errors).
- `void`: Represents functions that return no meaningful value (`undefined`).

**Code Example**:
```typescript
function processValue(val: unknown) {
  if (typeof val === 'string') {
    console.log(val.toUpperCase()); // Safe after narrowing
  }
}

function assertNever(x: never): never {
  throw new Error(`Unexpected object: ${x}`);
}
```

---

<a id="q5"></a>
### Q5: How do Const Assertions (`as const`) and Satisfies Operator (`satisfies`) work?

**Difficulty**: Intermediate

**Strategy**:
- `as const`: Narrow types to literal types, makes object properties deeply `readonly`, and converts arrays into fixed-length tuples.
- `satisfies` (TS 4.9+): Validates that an expression matches a type constraint WITHOUT widening or altering the inferred literal type of the expression.

**Code Example**:
```typescript
// as const
const routes = {
  home: '/',
  login: '/auth/login'
} as const;
// routes.home is literal '/' and readonly

// satisfies operator
type Palette = Record<string, string | [number, number, number]>;
const theme = {
  primary: '#22c55e',
  secondary: [255, 0, 0]
} satisfies Palette;

theme.primary.toUpperCase(); // Inferred as string, not string | [number, number, number]
```

---

<a id="q6"></a>
### Q6: What are Generics and Generic Constraints (`T extends object`) in TypeScript?

**Difficulty**: Beginner

**Strategy**:
Generics parameterize functions and types over the shapes they operate on, preserving input/output relationships instead of collapsing them to `any`. Constraints (`T extends object`) bound the parameter so only types with the required members are accepted while inference still picks the narrowest candidate.

**Code Example**:
```typescript
function prop<T extends object, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}
const n = prop({ id: 1 }, "id"); // number
// prop("str", "length"); // Error: string does not satisfy `extends object`
```

---

<a id="q7"></a>
### Q7: How do User-Defined Type Guards (`x is Type`) and Assertion Functions (`asserts x is Type`) work?

**Difficulty**: Intermediate

**Strategy**:
A type guard is a boolean-returning function whose return type is a predicate (`x is T`), narrowing in truthy branches. An assertion function declares `asserts x is T` and must return void; when it does not throw, the compiler narrows after the call site — enabling centralized validation.

**Code Example**:
```typescript
function isString(x: unknown): x is string { return typeof x === "string"; }
function assertString(x: unknown): asserts x is string {
  if (!isString(x)) throw new TypeError("expected string");
}
declare const v: unknown;
assertString(v);
v.toUpperCase(); // narrowed to string
```

---

<a id="q8"></a>
### Q8: What is the difference between `keyof`, `typeof`, and indexed access types (`T[K]`)?

**Difficulty**: Intermediate

**Strategy**:
`typeof` (in a type position) queries the static type of a value; `keyof T` produces the union of T's keys; `T[K]` is indexed access — the type of property K on T. Composed, they build type-safe lookups: `keyof typeof config` derives key unions from runtime constants.

**Code Example**:
```typescript
const routes = { home: "/", admin: "/admin" } as const;
type Routes = typeof routes;            // { readonly home: "/"; readonly admin: "/admin" }
type RouteName = keyof Routes;          // "home" | "admin"
type Path = Routes[RouteName];          // "/" | "/admin"
function go(name: RouteName, path: Routes[name]) {}
```

---

<a id="q9"></a>
### Q9: What are TypeScript Utility Types (`Partial`, `Required`, `Readonly`, `Record`, `Pick`, `Omit`, `Exclude`, `Extract`)?

**Difficulty**: Intermediate

**Strategy**:
Utility types are prebuilt mapped/conditional transforms: `Partial`/`Required`/`Readonly` toggle modifiers; `Record<K,V>` builds dictionaries; `Pick`/`Omit` subset keys; `Exclude`/`Extract` filter unions. They eliminate hand-written mirror types for patch payloads, views, and config subsets.

**Code Example**:
```typescript
interface User { id: string; name: string; email: string }
type UserPatch = Partial<Pick<User, "name" | "email">>; // { name?: string; email?: string }
type IdOnly = Pick<User, "id">;
type Role = "admin" | "editor" | "viewer";
type Staff = Exclude<Role, "viewer">; // "admin" | "editor"
const dirs: Record<Role, string> = { admin: "a", editor: "e", viewer: "v" };
```

---

<a id="q10"></a>
### Q10: How does Discriminated Unions (Tagged Unions) enable safe pattern matching in TypeScript?

**Difficulty**: Intermediate

**Strategy**:
Tagged unions add a literal discriminant (`kind`) to each variant so `switch`/`if` narrows both the variant and its payload. Exhaustiveness via a `never` default turns "forgot a case" from a runtime bug into a compile error — TS's idiomatic sum types.

**Code Example**:
```typescript
type ApiResult =
  | { ok: true; data: string[] }
  | { ok: false; error: { code: number; message: string } };

function render(r: ApiResult) {
  switch (r.ok) {
    case true:  return r.data.join(", ");
    case false: return `Error ${r.error.code}`;
    default: { const _: never = r; return _; }
  }
}
```

---

<a id="q11"></a>
### Q11: What is Covariance, Contravariance, Invariance, and Bivariance in TypeScript Subtyping?

**Difficulty**: Advanced

**Strategy**:
Subtyping direction depends on position: outputs are covariant (`Producer<Cat>` is a `Producer<Animal>`), inputs contravariant under `strictFunctionTypes` (`Consumer<Animal>` is a `Consumer<Cat>`), and method parameters stay bivariant for JS compatibility — a deliberate soundness trade to preserve DOM-era code.

**Code Example**:
```typescript
class Animal { name = "a"; }
class Cat extends Animal { meow() {} }

let a: (x: Animal) => void = (x) => x.name;
let c: (x: Cat) => void = a; // OK under strictFunctionTypes: contravariance
let p: () => Cat = () => new Cat();
let q: () => Animal = p;     // OK: covariant return
```

---

<a id="q12"></a>
### Q12: What is the purpose of `noImplicitAny`, `strictNullChecks`, and `noUncheckedIndexedAccess` in `tsconfig.json`?

**Difficulty**: Intermediate

**Strategy**:
`strictNullChecks` removes `undefined`/`null` from every type unless declared, forcing explicit handling; `noImplicitAny` errors on inferred-`any` parameters; `noUncheckedIndexedAccess` adds `| undefined` to index operations. Together they eliminate the majority of runtime crashes TS can statically prevent.

**Code Example**:
```typescript
// noImplicitAny: function f(x) {} // Error: x implicitly has an 'any' type
function len(x: string) { return x.length; }
declare const arr: number[];
const v = arr[0]; // number | undefined with noUncheckedIndexedAccess
const safe = v ?? 0;
function greet(name?: string) { return `Hi ${name ?? "guest"}`; } // strictNullChecks-aware
```

---

<a id="q13"></a>
### Q13: How do Ambient Declarations (`.d.ts` files) and `declare module` work?

**Difficulty**: Intermediate

**Strategy**:
Ambient declarations describe types for code that exists outside TS — globals, JS libs, or modules you extend. A `.d.ts` contains only `declare` statements (no emit); `declare module "name"` reopens a library's shape, and triple-slash references pull in type packages for legacy toolchains.

**Code Example**:
```typescript
// globals.d.ts — no runtime output
declare const APP_VERSION: string;
declare interface Window { __CONFIG__: { api: string } }
declare module "legacy-uuid" { export default function uuid(): string }

// usage anywhere:
console.log(APP_VERSION, window.__CONFIG__.api, (await import("legacy-uuid")).default());
```

---

<a id="q14"></a>
### Q14: What is the difference between `export type` and `export` in TypeScript 3.8+?

**Difficulty**: Beginner

**Strategy**:
`export type` (and `import type`) mark bindings as type-only: they are fully erased at emit, which keeps single-file transpilers (esbuild/swc) and `verbatimModuleSyntax` correct and avoids pulling runtime modules for shapes. Plain `export` emits a live binding, required for values.

**Code Example**:
```typescript
// types.ts
export type UserID = string & { __brand: "UserID" };
export interface DTO { id: UserID }
// value.ts
export const toUserID = (s: string): UserID => s as UserID;

// consumer.ts
import type { DTO } from "./types";   // erased
import { toUserID } from "./value";   // runtime import emitted
```

---

<a id="q15"></a>
### Q15: How does Brand Typing (Nominal Typing) work in a structurally-typed language?

**Difficulty**: Advanced

**Strategy**:
Structural typing makes `Meters` and `Feet` (both `number`) interchangeable — a unit-mixing bug factory. Branding intersects an invisible phantom tag so the structures differ nominally while remaining zero-cost at runtime; only an explicit cast can mint a branded value.

**Code Example**:
```typescript
type Meters = number & { readonly __unit: "m" };
type Feet = number & { readonly __unit: "ft" };

const meters = (n: number) => n as Meters;
function altitude(m: Meters) { return m; }
altitude(meters(100));
// altitude(3.28 as Feet); // Error: structurally distinct now
```

---

<a id="q16"></a>
### Q16: What is the `override` keyword in TypeScript 4.3+ class methods?

**Difficulty**: Beginner

**Strategy**:
The `override` keyword (with `noImplicitOverride`) declares intent to replace an inherited member. It catches two bug classes instantly: typos that silently create new methods, and members that vanish when the base class is refactored — the subclass then fails to compile instead of drifting.

**Code Example**:
```typescript
class Base {
  greet() { return "hello"; }
  deprecated() {}
}
class Sub extends Base {
  override greet() { return "hi"; } // explicit
  // greeter() {} // Error only with noImplicitOverride + no override kw
  // override deprecated() {} // Error: nothing to override
}
```

---

<a id="q17"></a>
### Q17: How do Function Overloads work in TypeScript?

**Difficulty**: Intermediate

**Strategy**:
Overloads declare multiple ordered call signatures above a compatible implementation. The compiler matches callers against the signatures top-down and only sees that matched shape, enabling precise input/output correlations (string in → number out) that a union signature cannot express.

**Code Example**:
```typescript
function format(x: string | number): string;
function format(x: Date): number;
function format(x: string | number | Date): string | number {
  return x instanceof Date ? x.getTime() : String(x);
}
const a: string = format("7");
const b: number = format(new Date());
```

---

<a id="q18"></a>
### Q18: What is the difference between `readonly` array (`ReadonlyArray<T>`) and `const` array?

**Difficulty**: Beginner

**Strategy**:
`ReadonlyArray<T>` removes mutating methods at the type level (no runtime copying), while `as const` deeply freezes literals AND pins their narrowest types. Use `ReadonlyArray` for function parameters accepting any array read-only; use `as const` when literal tuple/enum-like values must be preserved.

**Code Example**:
```typescript
function sum(xs: ReadonlyArray<number>) { return xs.reduce((a, b) => a + b, 0); }
const mutable = [1, 2];
sum(mutable); // OK — no defensive copy needed

const RGB = ["red", "green", "blue"] as const; // readonly ["red","green","blue"]
type Color = (typeof RGB)[number];
const c: Color = "red";
```

---

<a id="q19"></a>
### Q19: How do Decorators work in TypeScript (Legacy Stage 2 vs Modern Stage 3 Decorators)?

**Difficulty**: Advanced

**Strategy**:
Legacy Stage-2 decorators (flag `experimentalDecorators`) pass typed `(target, key, descriptor)` tuples and power Angular/NestJS. Stage-3 standard decorators are plain functions `(value, context)` with initializer hooks and metadata — stronger, framework-neutral, and what new code should target.

**Code Example**:
```typescript
// Stage 3
function trace<T extends Function>(fn: T, ctx: ClassMethodDecoratorContext): T {
  return ((...args: unknown[]) => { console.log(ctx.name); return fn(...args); }) as unknown as T;
}
class Api {
  @trace fetch() {}
}
// Legacy: function log(target: any, key: string, desc: PropertyDescriptor) {}
```

---

<a id="q20"></a>
### Q20: What is the purpose of `tsconfig.json` `moduleResolution: "bundler"` vs `"node16"`?

**Difficulty**: Intermediate

**Strategy**:
`bundler` assumes a bundler resolves modules: extensionless imports, `exports` awareness, permissive ESM/CJS mixing. `node16`/`nodenext` mimic real Node resolution — extensions required in ESM, `exports` conditions honored strictly. Mismatches surface as "compiles in editor, fails at runtime".

**Code Example**:
```json
// app bundling with Vite/esbuild
{ "moduleResolution": "bundler", "module": "ESNext" }
// library published for real Node
{ "moduleResolution": "NodeNext", "module": "NodeNext" }
```

---

<a id="q21"></a>
### Q21: How does `instanceof` narrowing work with classes in TypeScript?

**Difficulty**: Beginner

**Strategy**:
`instanceof` narrows to the class's instance type via its construct signature, and narrows subclasses to the most specific declared class. It fails across realms (iframes, vm), with `Symbol.hasInstance` tricks, and on structurally-typed shapes — prefer discriminants for serialized data.

**Code Example**:
```json
// app bundling with Vite/esbuild
{ "moduleResolution": "bundler", "module": "ESNext" }
// library published for real Node
{ "moduleResolution": "NodeNext", "module": "NodeNext" }
```

---

<a id="q22"></a>
### Q22: What is the difference between `in` operator type narrowing and property checking?

**Difficulty**: Beginner

**Strategy**:
`in` narrowing selects union members that declare the key — best for untagged variants. Property checking via `"k" in obj` sees optional keys too, but cannot distinguish present-but-undefined from absent; when semantics differ, use an explicit discriminant tag instead of shape sniffing.

**Code Example**:
```json
// app bundling with Vite/esbuild
{ "moduleResolution": "bundler", "module": "ESNext" }
// library published for real Node
{ "moduleResolution": "NodeNext", "module": "NodeNext" }
```

---

<a id="q23"></a>
### Q23: How do recursive types work in TypeScript for JSON structures?

**Difficulty**: Advanced

**Strategy**:
Recursive types self-reference through interfaces (or type aliases with indirection pre-4.1) to describe arbitrarily nested JSON: each node is a union of primitives, arrays of nodes, or maps of nodes. Lazy evaluation via interface members defers instantiation so the compiler handles infinite depth at use-sites.

**Code Example**:
```json
// app bundling with Vite/esbuild
{ "moduleResolution": "bundler", "module": "ESNext" }
// library published for real Node
{ "moduleResolution": "NodeNext", "module": "NodeNext" }
```

---

<a id="q24"></a>
### Q24: What is the purpose of `ThisType<T>` utility type?

**Difficulty**: Advanced

**Strategy**:
`ThisType<T>` is a marker interface: when it appears (intersected) in an object literal's contextual type, `this` inside methods is typed as T — without emitting anything. It's how Vue and Vuex type options objects where methods read sibling state.

**Code Example**:
```json
// app bundling with Vite/esbuild
{ "moduleResolution": "bundler", "module": "ESNext" }
// library published for real Node
{ "moduleResolution": "NodeNext", "module": "NodeNext" }
```

---

<a id="q25"></a>
### Q25: How do you configure Project References and Composite Projects for large TypeScript monorepos?

**Difficulty**: Advanced

**Strategy**:
Project references split a monorepo into `composite` sub-projects with declared edges. `tsc --build` compiles the graph topologically, caching per-project state in `.tsbuildinfo` so only stale packages rebuild — turning whole-repo type checks into incremental ones.

**Code Example**:
```json
// app bundling with Vite/esbuild
{ "moduleResolution": "bundler", "module": "ESNext" }
// library published for real Node
{ "moduleResolution": "NodeNext", "module": "NodeNext" }
```

---

<a id="q26"></a>
### Q26: What are Template Literal Types and how do they enable advanced string manipulation at the type level?

**Difficulty**: Advanced

**Strategy**:
Project references split a monorepo into `composite` sub-projects with declared edges. `tsc --build` compiles the graph topologically, caching per-project state in `.tsbuildinfo` so only stale packages rebuild — turning whole-repo type checks into incremental ones.

**Code Example**:
```json
// app bundling with Vite/esbuild
{ "moduleResolution": "bundler", "module": "ESNext" }
// library published for real Node
{ "moduleResolution": "NodeNext", "module": "NodeNext" }
```

---

<a id="q27"></a>
### Q27: How do Conditional Types distribute over unions, and how do you prevent distribution?

**Difficulty**: Advanced

**Strategy**:
A conditional type whose checked parameter is a *naked* type parameter distributes: `Distribute<A|B>` evaluates the branch for each member and unions the results. Wrapping the parameter in a tuple `[T]` prevents distribution when you need to inspect the union as a whole.

**Code Example**:
```typescript
type Distributed<T> = T extends string ? "s" : "n";        // ("s" | "n") for string|number
type NonDistributed<T> = [T] extends [string] ? "s" : "n";  // "n" for string|number

type ToArrayDist<T> = T extends unknown ? T[] : never;
type R1 = ToArrayDist<string | number>; // string[] | number[]
```

---

<a id="q28"></a>
### Q28: How does `infer` work inside conditional types?

**Difficulty**: Advanced

**Strategy**:
`infer U` declares a type variable within the `extends` clause of a conditional type, binding it to whatever occupies that position in the matched structure. It is the core mechanism for extracting element types, return types, and function parameters at the type level.

**Code Example**:
```typescript
type ElementType<T> = T extends (infer U)[] ? U : never;
type R = ElementType<string[]>; // string

type UnwrapPromise<T> = T extends Promise<infer V> ? UnwrapPromise<V> : T;
type R2 = UnwrapPromise<Promise<Promise<number>>>; // number
```

---

<a id="q29"></a>
### Q29: What are Mapped Types and Key Remapping via `as`?

**Difficulty**: Intermediate

**Strategy**:
Mapped types iterate a union of keys (`{ [K in keyof T]: ... }`) producing a transformed object shape. The `as` clause (TS 4.1) remaps keys — filtering with `never` or renaming with template literals — enabling `Getters<T>` or `PartialBy<T, Keys>` utilities.

**Code Example**:
```typescript
type Getters<T> = { [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K] };
interface Person { name: string; age: number }
type PersonGetters = Getters<Person>; // { getName: () => string; getAge: () => number }

type OmitByType<T, V> = { [K in keyof T as T[K] extends V ? never : K]: T[K] };
```

---

<a id="q30"></a>
### Q30: Explain `keyof`, index access types, and the `KeyofTrait` for exhaustive Records?

**Difficulty**: Intermediate

**Strategy**:
`keyof T` yields the union of T's keys; `T[K]` is an indexed access extracting the property type. Combining them lets `Record<keyof T, ...>` stay in sync with T — adding a property to T becomes a compile error in every exhaustive map, enforced by the compiler rather than tests.

**Code Example**:
```typescript
interface Config { host: string; port: number }
type ConfigDefault = Record<keyof Config, boolean>;

const defaults: ConfigDefault = { host: true, port: true }; // missing key = compile error
type PortType = Config["port"]; // number
```

---

<a id="q31"></a>
### Q31: What is `satisfies` (TS 4.9) and how does it differ from a type annotation?

**Difficulty**: Intermediate

**Strategy**:
`satisfies T` validates an expression against a type **without widening** it: literal types and exact property sets are preserved for inference, yet conformance is checked. An annotation `: T` checks conformance but widens the expression's inferred type to T, losing literal precision.

**Code Example**:
```typescript
type Routes = Record<string, string[] | string>;
const config = {
  home: "/",
  admin: ["/admin", "/admin/users"],
} satisfies Routes;

config.admin.map(r => r.length); // OK: inferred as string[] thanks to satisfies
// With `: Routes` this errors: string | string[] has no .map
```

---

<a id="q32"></a>
### Q32: What are `const` Type Parameters (TS 5.0) and when do you reach for them?

**Difficulty**: Advanced

**Strategy**:
Marking a type parameter `const` infers the most specific (literal, readonly) type possible for the argument, without callers needing `as const`. It removes boilerplate in APIs that consume literal tuples/objects — declaration merging of inference and immutability.

**Code Example**:
```typescript
function defineRoutes<const T extends readonly string[]>(routes: T): T { return routes; }
const r = defineRoutes(["/home", "/about"]);
// r: readonly ["/home", "/about"] — literal tuple preserved, no `as const` needed
```

---

<a id="q33"></a>
### Q33: What problem does `NoInfer<T>` (TS 5.4) solve?

**Difficulty**: Advanced

**Strategy**:
Normally a type parameter appearing in both parameter and return positions unifies their inference, which can lock the wrong literal (e.g., default values widening). `NoInfer<T>` excludes positions from inference so T is inferred only from the primary input, enabling correct defaults in generic APIs.

**Code Example**:
```typescript
function createSocket<const Name extends string>(name: Name, defaultName: NoInfer<Name> = "server"): Name {
  return name;
}
const s = createSocket("db"); // Name inferred only from first arg; default checked against it
```

---

<a id="q34"></a>
### Q34: How do ECMAScript Stage-3 Decorators (TS 5.0) differ from legacy `experimentalDecorators`?

**Difficulty**: Advanced

**Strategy**:
Standard decorators are plain functions receiving `(value, context)` where value is the decorated element and context carries `kind`, `name`, `addInitializer`, and metadata access. Legacy decorators (used by older NestJS/typeorm) receive typed `(target, key, descriptor)` tuples and require `experimentalDecorators`; the two systems are mutually incompatible.

**Code Example**:
```typescript
function logged(value: Function, context: ClassMethodDecoratorContext) {
  return function (this: any, ...args: unknown[]) {
    console.log(`calling ${String(context.name)}`);
    return value.apply(this, args);
  };
}
class Service {
  @logged run() {}
}
```

---

<a id="q35"></a>
### Q35: Why are `enum`s controversial, and what are the alternatives?

**Difficulty**: Intermediate

**Strategy**:
Enums are one of TS's few *non-erasable* syntaxes: they emit runtime objects, support surprising reverse-mapping for numeric enums, and interact awkwardly with `isolatedModules`. Alternatives: `as const` objects plus a derived union type, or plain string literal unions — both fully erasable and structural.

**Code Example**:
```typescript
// Alternative to enum
const LogLevel = { Debug: "debug", Info: "info" } as const;
type LogLevel = (typeof LogLevel)[keyof typeof LogLevel]; // "debug" | "info"

function log(level: LogLevel) {}
log(LogLevel.Debug);
```

---

<a id="q36"></a>
### Q36: What does `unknown` enforce that `any` does not?

**Difficulty**: Beginner

**Strategy**:
`any` opts out of type checking entirely — it is assignable both ways and silences all errors. `unknown` is the type-safe top type: anything is assignable **to** it, but using it requires narrowing (guards, assertion, `instanceof`) first. Use `unknown` at boundaries (catch clauses, JSON.parse, external input).

**Code Example**:
```typescript
function parse(raw: string): unknown {
  return JSON.parse(raw);
}
const data = parse('{"id":1}');
// data.id // Error: 'data' is of type 'unknown'
if (typeof data === "object" && data !== null && "id" in data) {
  console.log(data.id); // narrowed
}
```

---

<a id="q37"></a>
### Q37: How do you use `never` for exhaustiveness checking?

**Difficulty**: Intermediate

**Strategy**:
`never` is the bottom type — uninhabitable. After narrowing a union through every case, the remaining type is `never`; assigning it to `never` in a default branch makes the compiler error whenever a new union member is added but not handled.

**Code Example**:
```typescript
type Shape = { kind: "circle"; r: number } | { kind: "square"; s: number };
function area(shape: Shape): number {
  switch (shape.kind) {
    case "circle": return Math.PI * shape.r ** 2;
    case "square": return shape.s ** 2;
    default:
      const _exhaustive: never = shape; // compile error if a variant is missed
      return _exhaustive;
  }
}
```

---

<a id="q38"></a>
### Q38: What are Discriminated Unions and why are they TS's best modeling tool?

**Difficulty**: Intermediate

**Strategy**:
A discriminated union tags each variant with a literal `kind`/`type` field. The compiler narrows on the tag, giving each branch precisely-typed payload fields — modeling state machines, API results, and async actions with impossible states made unrepresentable.

**Code Example**:
```typescript
type FetchState =
  | { status: "idle" }
  | { status: "loading" }
  | { status: "success"; data: User[] }
  | { status: "error"; error: Error };

function render(state: FetchState) {
  if (state.status === "success") return state.data; // User[] is known here
}
```

---

<a id="q39"></a>
### Q39: Explain variance: covariance, contravariance, and bivariance in TypeScript?

**Difficulty**: Expert

**Strategy**:
Return positions are covariant (`() => Cat` is assignable to `() => Animal`); parameter positions are contravariant under `strictFunctionTypes` (a handler of `Animal` accepts a `Cat`). Method parameters are bivariant for JS compatibility — a known soundness hole interviewers probe. TS 4.7 added explicit `in`/`out` variance annotations for type parameters.

**Code Example**:
```typescript
interface Producer<out T> { get(): T }       // covariant
interface Consumer<in T> { put(x: T): void } // contravariant

let p: Producer<Cat> = {} as Producer<Animal>; // Animal producer is a Cat producer? no — reversed
let c: Consumer<Animal> = {} as Consumer<Cat>; // contravariance allows this direction
```

---

<a id="q40"></a>
### Q40: What are Branded (Nominal) types and why does structural typing need them?

**Difficulty**: Advanced

**Strategy**:
TS is structural — `{ id: string }` for UserId and OrderId are interchangeable, which lets invalid IDs flow silently. Branding adds a phantom tag (`& { __brand: "UserId" }`) making types distinct again; an assertion constructor is the single gateway.

**Code Example**:
```typescript
type UserId = string & { readonly __brand: "UserId" };
type OrderId = string & { readonly __brand: "OrderId" };

function toUserId(id: string): UserId { return id as UserId; }
function getUser(id: UserId) {}
getUser("abc");          // Error
getUser(toUserId("abc")); // OK
```

---

<a id="q41"></a>
### Q41: How do Variadic Tuple Types work?

**Difficulty**: Advanced

**Strategy**:
TS 4.0 allows generic rest elements `[...T, ...U]` anywhere in a tuple, enabling type-safe `concat`, `curry`, and middleware composition. Prefixes/suffixes around a rest element must be matched structurally, which the compiler checks rather than guesses.

**Code Example**:
```typescript
type Concat<T extends readonly unknown[], U extends readonly unknown[]> = [...T, ...U];
type R = Concat<[1, 2], ["a"]>; // [1, 2, "a"]

function partialCall<T extends unknown[], U extends unknown[], R>(
  f: (...args: [...T, ...U]) => R, ...headArgs: T
) {
  return (...tailArgs: U) => f(...headArgs, ...tailArgs);
}
```

---

<a id="q42"></a>
### Q42: What is declaration merging, and which declarations merge?

**Difficulty**: Intermediate

**Strategy**:
Interfaces, namespaces (with classes/functions/enums), and global augmentation merge by concatenating members; type aliases do **not** merge. Libraries exploit it for statics+instances (`interface JQuery` + `namespace JQuery`) and consumers use it to extend third-party module shapes safely.

**Code Example**:
```typescript
interface Window { __APP_VERSION__: string }
declare global { interface Console { audit(msg: string): void } }

interface Box { size: number }
interface Box { weight: number }
const b: Box = { size: 1, weight: 2 }; // merged members required
```

---

<a id="q43"></a>
### Q43: interface vs type alias — when does the choice matter?

**Difficulty**: Beginner

**Strategy**:
Both support generics and implement/extend each other. Choose `interface` for object contracts benefiting from merging and declaration caching; choose `type` for unions, intersections, tuples, mapped/conditional types, and primitives. Perf differences are negligible at scale — semantics drive the choice.

**Code Example**:
```typescript
interface Point { x: number; y: number }
type Vector = [number, number];                 // tuple — type only
type StringOrId = string | Point["x"];          // union — type only
type ReadonlyPoint = Readonly<Point>;           // mapped — type only
interface Extended extends Point { z: number }  // both work
```

---

<a id="q44"></a>
### Q44: How do `readonly`, `Readonly<T>`, `ReadonlyArray<T>`, and `as const` differ?

**Difficulty**: Intermediate

**Strategy**:
`readonly` on a property blocks reassignment at one level; `Readonly<T>` maps all top-level props readonly (shallow); `ReadonlyArray<T>` removes mutators; `as const` freezes literals deeply into readonly literal types. None affect runtime — erasure-only immutability, so pair with runtime freezing at boundaries.

**Code Example**:
```typescript
const cfg = { retries: 3, hosts: ["a"] } as const;
// cfg.retries: 3, cfg.hosts: readonly ["a"]

function freeze<T>(x: readonly T[]): readonly T[] { return x; }
freeze([1, 2, 3]).push(4); // Error: property 'push' does not exist
```

---

<a id="q45"></a>
### Q45: How do User-Defined Type Guards and Assertion Functions differ in control-flow effects?

**Difficulty**: Intermediate

**Strategy**:
A guard `x is T` returns boolean and narrows in `if` branches; an assertion function `asserts x is T` (must return `void`) narrows **after** the call when control continues — modeled as never-returning on failure. Assertions cannot be arrow functions assigned without an explicit type.

**Code Example**:
```typescript
function isError(x: unknown): x is Error { return x instanceof Error; }
function assertDefined<T>(x: T | undefined): asserts x is T {
  if (x === undefined) throw new Error("undefined");
}

const e: unknown = new Error();
assertDefined(e); // from here e is non-undefined
if (isError(e)) console.log(e.message);
```

---

<a id="q46"></a>
### Q46: How do you type generics with defaults and multiple constraints?

**Difficulty**: Intermediate

**Strategy**:
Type parameters can default (`T = never`) and chain constraints (`T extends object & { id: string }`). Defaults let callers omit parameters; constraints bound what members are visible inside the function. Later parameters may reference earlier ones, enabling curried inference.

**Code Example**:
```typescript
function pluck<T, K extends keyof T = keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}
const n = pluck({ id: 1 }, "id");   // number
const all = pluck({ id: 1 });       // K defaults to "id"

function merge<A extends object, B extends object>(a: A, b: B): A & B { return { ...a, ...b }; }
```

---

<a id="q47"></a>
### Q47: What are the strict-family flags a production tsconfig should enable?

**Difficulty**: Intermediate

**Strategy**:
Beyond `strict: true`, mature codebases add `noUncheckedIndexedAccess` (indexing yields `T | undefined`), `exactOptionalPropertyTypes` ( distinguishes `{x?: 1}` from `{x: 1 | undefined}`), `noImplicitOverride`, `noFallthroughCasesInSwitch`, and `verbatimModuleSyntax`. Each closes a distinct soundness gap.

**Code Example**:
```json
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true,
    "noImplicitOverride": true,
    "verbatimModuleSyntax": true
  }
}
```

---

<a id="q48"></a>
### Q48: What does `noUncheckedIndexedAccess` change and how do you code around it?

**Difficulty**: Intermediate

**Strategy**:
Index signatures and array element access return `T | undefined` because JS lookups can miss at runtime. Idiomatic handling: `Map.get` style checks, default values, `??`, or `Array.prototype.at` with narrowing — forcing the missing-key case to be designed, not discovered.

**Code Example**:
```typescript
const scores = [90, 85];
const first = scores[0]; // number | undefined under the flag

if (first !== undefined) first + 1; // narrowed
const val = scores.at(2) ?? 0;      // explicit default
const dict: Record<string, number> = {};
const x = dict["missing"] ?? 0;
```

---

<a id="q49"></a>
### Q49: How does module resolution differ between `node16`, `bundler`, and classic `node` modes?

**Difficulty**: Advanced

**Strategy**:
`node16`/`nodenext` honor `package.json` `exports`/`types` conditions and require file extensions in relative ESM imports; `bundler` assumes a bundler resolves extensionless imports with loose ESM/CJS interop; classic `node` mimics old Node lookup and ignores `exports`. Mismatched mode causes "works in dev, breaks at runtime" resolution errors.

**Code Example**:
```json
// package.json
{
  "type": "module",
  "exports": {
    ".": { "types": "./dist/index.d.ts", "import": "./dist/index.js", "require": "./dist/index.cjs" }
  }
}
// tsconfig: "moduleResolution": "node16" respects the map; "bundler" also allows extensionless imports
```

---

<a id="q50"></a>
### Q50: What does `verbatimModuleSyntax` enforce vs `isolatedModules`?

**Difficulty**: Advanced

**Strategy**:
`isolatedModules` assumes each file transpiles independently (as esbuild/swc do) so type-only re-exports must be marked. `verbatimModuleSyntax` (5.0) subsumes it: every import/export is emitted exactly as written, forcing `import type` for type-only imports and preventing subtle CJS/ESM emit surprises.

**Code Example**:
```typescript
import type { Config } from "./config";  // erased — required for types
import { loadConfig } from "./config";   // emitted as-is

export type { Config };                  // type-only export must be marked
// import { Config } from "./config" as value would now be a compile error
```

---

<a id="q51"></a>
### Q51: How do `export =` and `esModuleInterop` interact for CJS interop?

**Difficulty**: Advanced

**Strategy**:
`export =` models a CommonJS `module.exports` value. Under `esModuleInterop`, TS wraps CJS imports so default/named access works from ESM (`import fs from "fs"`), synthesizing a default and hoisting named properties; without it you need `import * as` with care. `allowSyntheticDefaultImports` alone only fakes the types without the runtime helper.

**Code Example**:
```typescript
// legacy-cjs-module.d.ts
declare const legacy: { run(): void };
export = legacy;

// consumer with esModuleInterop
import legacy from "./legacy-cjs-module";
legacy.run();
```

---

<a id="q52"></a>
### Q52: How do you write recursive and deeply-applied utility types (DeepPartial, DeepReadonly)?

**Difficulty**: Advanced

**Strategy**:
Recursive conditional types (TS 4.1+) let utilities descend into nested objects: check for primitives/functions to stop, recurse on arrays and plain objects, and map the rest. Depth is compiler-limited (~50–100 instantiations) so guard with intersection stops for known leaves.

**Code Example**:
```typescript
type DeepReadonly<T> = T extends (infer U)[]
  ? readonly DeepReadonly<U>[]
  : T extends object
  ? { readonly [K in keyof T]: DeepReadonly<T[K]> }
  : T;

type Nested = { a: { b: { c: number } }; list: { x: string }[] };
type Frozen = DeepReadonly<Nested>; // everything readonly at every depth
```

---

<a id="q53"></a>
### Q53: How would you implement built-in utilities `Pick`, `Omit`, `Partial`, and `ReturnType` yourself?

**Difficulty**: Intermediate

**Strategy**:
`Pick` maps over the constrained key subset; `Omit` is Pick plus `Exclude` on keys; `Partial` maps all props optional; `ReturnType` uses conditional + `infer` on the call signature. Interviewers verify you can compose mapped types, `keyof`, and `infer` fluently.

**Code Example**:
```typescript
type MyPick<T, K extends keyof T> = { [P in K]: T[P] };
type MyOmit<T, K extends keyof T> = MyPick<T, Exclude<keyof T, K>>;
type MyPartial<T> = { [P in keyof T]?: T[P] };
type MyReturnType<T> = T extends (...args: never[]) => infer R ? R : never;

type T1 = MyPick<{ a: 1; b: 2 }, "a">; // { a: 1 }
type T2 = MyReturnType<() => string>;  // string
```

---

<a id="q54"></a>
### Q54: How do function overloads compare with union-parameter signatures?

**Difficulty**: Intermediate

**Strategy**:
Overloads list ordered call signatures with a permissive implementation; unions accept `string | number` but then require internal narrowing and lose the input-output correlation. Overloads (or conditional return types) preserve precise correlations like "string in, number out".

**Code Example**:
```typescript
function parse(input: string): number;
function parse(input: number): string;
function parse(input: string | number): string | number {
  return typeof input === "string" ? input.length : String(input);
}
const n = parse("abc"); // number — correlated, no cast needed
```

---

<a id="q55"></a>
### Q55: What are abstract classes vs interfaces for shared contracts, and when is each right?

**Difficulty**: Beginner

**Strategy**:
Interfaces define pure structural contracts with zero runtime. Abstract classes can hold state, constructors, and concrete method bodies — providing partial implementation plus a nominal runtime identity (`instanceof`). Use interfaces by default; abstract classes when subclasses share real logic or DI frameworks need a class token.

**Code Example**:
```typescript
abstract class Repository<T> {
  protected cache = new Map<string, T>();
  abstract fetch(id: string): Promise<T>;
  async get(id: string): Promise<T> {
    return this.cache.get(id) ?? this.set(id, await this.fetch(id));
  }
  protected async set(id: string, v: T) { this.cache.set(id, v); return v; }
}
```

---

<a id="q56"></a>
### Q56: How do Mixins work in TypeScript without classes-inheriting-classes?

**Difficulty**: Advanced

**Strategy**:
Use `Object.assign(Child, Base)` at runtime plus intersection types (`typeof Base & typeof Child`) or the documented `Constructor<Mixin>` generic pattern for typing. This composes behaviors while keeping single-inheritance semantics intact.

**Code Example**:
```typescript
type Constructor<T = {}> = new (...args: any[]) => T;
function Timestamped<TBase extends Constructor>(Base: TBase) {
  return class extends Base {
    timestamp = Date.now();
  };
}
class Entity { id = Math.random(); }
const TimedEntity = Timestamped(Entity);
const e = new TimedEntity(); // Entity fields + timestamp
```

---

<a id="q57"></a>
### Q57: How do `private`, `#private`, and `protected` differ?

**Difficulty**: Intermediate

**Strategy**:
`private`/`protected` are erased at runtime and cross-instance accessible (same class can read other instances' privates). `#field` is the ECMAScript hard-private: runtime-enforced, not accessible via brackets/reflection, and incompatible with declaration merging or `Object.assign` mixins. `protected` additionally permits subclass access.

**Code Example**:
```typescript
class Wallet {
  #balance = 0;            // runtime private
  private auditLog: string[] = []; // type-level only
  protected owner: string = "";
  deposit(n: number) { this.#balance += n; }
  audit(other: Wallet) { return other.auditLog; } // legal: same class
}
```

---

<a id="q58"></a>
### Q58: What is type widening and how do literal types escape it?

**Difficulty**: Intermediate

**Strategy**:
Initializing `let x = "hello"` widens to `string` because mutation is allowed; `const` freezes the literal. Explicit annotations, `as const`, or const type parameters pin literal types. Fresh object literals widen property types unless the target type is literal or readonly.

**Code Example**:
```typescript
let a = "click";        // string
const b = "click";      // "click"
let c = "click" as const; // "click"
function handle(event: "click" | "hover") {}
handle(a);              // Error: string not assignable
handle(b);              // OK
```

---

<a id="q59"></a>
### Q59: How does Control Flow Analysis narrow, and where does it fail?

**Difficulty**: Intermediate

**Strategy**:
TS narrows via guards, `typeof`/`instanceof`/`in`, discriminants, and assignment. It fails across function boundaries (closures may run later), after `await` re-assignments, through mutable aliased properties, and inside callbacks referencing `let` outer variables — requiring guards repeated or IIFE boundaries.

**Code Example**:
```typescript
function f(x: string | number) {
  if (typeof x === "string") {
    [1, 2].forEach(() => x.toUpperCase()); // OK: x narrowed to string and captured
  }
  let y: string | number = "a";
  const set = () => { y = 1; };
  set();
  // y.toUpperCase(); // Error: still string | number — assignment analyzed conservatively
}
```

---

<a id="q60"></a>
### Q60: What are the pitfalls of non-null assertion (`!`) and better alternatives?

**Difficulty**: Beginner

**Strategy**:
`x!` silences the compiler without any runtime check — every `!` is a potential crash contract. Prefer narrowing, default values (`??`), optional chaining with explicit fallback, `Map.get` guards, or assertion functions that centralize and throw loudly.

**Code Example**:
```typescript
const el = document.querySelector<HTMLInputElement>("#name");
// el!.value            // crashes if missing
const value = el?.value ?? "";           // safe default
function requireEl<T>(x: T | null): T { if (!x) throw new Error("missing"); return x; }
requireEl(el).value;    // centralized, loud failure
```

---

<a id="q61"></a>
### Q61: How do you type `this` and polymorphic `this` for fluent APIs?

**Difficulty**: Advanced

**Strategy**:
`this` types let methods return the concrete subclass (`this`), keeping builder chains typed to the actual instance rather than the base. Combined with `ThisType<T>` marker interfaces, they also enable context-sensitive `this` in object literals — the mechanism behind Vue's and Vuex's ergonomic options APIs.

**Code Example**:
```typescript
class QueryBuilder<T> {
  private filters: string[] = [];
  where(cond: string): this { this.filters.push(cond); return this; }
}
class UserQuery extends QueryBuilder<"users"> {
  activeOnly(): this { return this.where("active = true"); }
}
const q = new UserQuery().activeOnly().where("id = 1"); // still UserQuery
```

---

<a id="q62"></a>
### Q62: How do Generators and AsyncGenerators interact with typing?

**Difficulty**: Advanced

**Strategy**:
`function*` returns `Generator<Y, R, N>` (yield, return, next types) and `async function*` returns `AsyncGenerator`. The third parameter types `next()` inputs, enabling typed two-way communication — the core of Redux-Saga and effect systems. `for await...of` consumes async generators lazily.

**Code Example**:
```typescript
function* counter(): Generator<number, string, boolean> {
  let i = 0;
  while (true) {
    const stop = yield i++;
    if (stop) return "done";
  }
}
const it = counter();
it.next();        // { value: 0, done: false }
it.next(true);    // { value: "done", done: true }

async function* pages(): AsyncGenerator<number[]> {
  yield [1, 2]; yield [3];
}
for await (const p of pages()) console.log(p);
```

---

<a id="q63"></a>
### Q63: What is Module Augmentation for third-party libraries?

**Difficulty**: Advanced

**Strategy**:
`declare module "lib"` within a module reopens the library's types to add or specialize members — required when attaching plugins (e.g., Vue prototypes, Express request decorators). Without augmentation, such additions type as errors or `any`.

**Code Example**:
```typescript
import express, { Request } from "express";

declare global {
  namespace Express {
    interface Request {
      currentUser?: { id: string };
    }
  }
}

declare module "express-serve-static-core" {
  interface Request { traceId: string }
}

const app = express();
app.use((req: Request) => req.currentUser?.id);
```

---

<a id="q64"></a>
### Q64: How do you type environment variables and external config safely?

**Difficulty**: Intermediate

**Strategy**:
Declare `process.env` fields via `Readonly<Record<string, string|undefined>>` interfaces or import-meta generics, then validate once at boot with a parser (zod/valibot) that returns a fully-typed, immutable config — converting "possibly undefined everywhere" into one guarded checkpoint.

**Code Example**:
```typescript
import { z } from "zod";

const EnvSchema = z.object({
  PORT: z.coerce.number().default(3000),
  DATABASE_URL: z.string().url(),
  FEATURES: z.string().transform(s => s.split(",") as Array<"a" | "b">),
});

const env = EnvSchema.parse(process.env); // typed, validated, throws fast
export const config = Object.freeze(env);
```

---

<a id="q65"></a>
### Q65: How do runtime validators (zod) bridge to compile-time types?

**Difficulty**: Intermediate

**Strategy**:
Libraries like zod derive a static type from a schema (`z.infer<typeof Schema>`), making the runtime shape and the compile-time type one source of truth. This kills drift at trust boundaries: API payloads, env, forms, and third-party JSON enter as validated, precisely-typed values.

**Code Example**:
```typescript
import { z } from "zod";
const UserSchema = z.object({ id: z.string().uuid(), email: z.string().email() });
type User = z.infer<typeof UserSchema>;

async function getUser(url: string): Promise<User> {
  const res = await fetch(url);
  return UserSchema.parse(await res.json()); // runtime-checked User
}
```

---

<a id="q66"></a>
### Q66: What typing does `Awaited<T>` provide and how do you unwrap nested Promises?

**Difficulty**: Intermediate

**Strategy**:
`Awaited<T>` recursively unwraps thenables — `Awaited<Promise<Promise<number>>>` is `number`, and it distributes over unions. It powers `ReturnType` of async functions and `async` inference; use it when mapping types over values that may arrive asynchronously.

**Code Example**:
```typescript
type Unwrap<T> = Awaited<T>;
type A = Unwrap<Promise<string>>;            // string
type B = Unwrap<Promise<Promise<number>[]>>; // number[] (element-wise then array)
type C = Awaited<ReturnType<typeof fetch>>;  // Response

async function load(): Promise<{ id: number }> { return { id: 1 }; }
type Loaded = Awaited<ReturnType<typeof load>>; // { id: number }
```

---

<a id="q67"></a>
### Q67: How do you model Result/Either-style error handling to avoid exceptions?

**Difficulty**: Advanced

**Strategy**:
A `Result<T, E>` discriminated union forces callers to handle both branches at the type level. Combine with helper constructors (`ok`, `err`), exhaustiveness in `match`, and `tryCatch` wrappers around unknown-throwing code to make failures explicit values — the foundation of predictable async pipelines.

**Code Example**:
```typescript
type Result<T, E = Error> =
  | { ok: true; value: T }
  | { ok: false; error: E };

const ok = <T>(value: T): Result<T, never> => ({ ok: true, value });
const err = <E>(error: E): Result<never, E> => ({ ok: false, error });

async function tryCatch<T>(p: Promise<T>): Promise<Result<T>> {
  try { return ok(await p); } catch (e) { return err(e as Error); }
}

const r = await tryCatch(fetch("/api"));
if (!r.ok) console.error(r.error.message);
```

---

<a id="q68"></a>
### Q68: How do you keep barrel files (`index.ts`) from hurting build performance?

**Difficulty**: Intermediate

**Strategy**:
Barrels re-export whole libraries, so importing one symbol pulls the graph into every bundler analysis and can defeat tree-shaking and circularity checks. Mitigate with `import type` re-exports, deep per-module imports in hot paths, package `exports` maps, and `isolatedModules`-friendly explicit exports.

**Code Example**:
```typescript
// ui/index.ts — type-only re-exports erase at compile time
export type { ButtonProps } from "./button";
export type { InputProps } from "./input";
// runtime imports bypass the barrel in hot paths:
import { Button } from "./ui/button"; // direct
```

---

<a id="q69"></a>
### Q69: How does `skipLibCheck` trade safety for speed, and what does it skip exactly?

**Difficulty**: Beginner

**Strategy**:
`skipLibCheck` skips type-checking of all `.d.ts` files — including yours and third-party's — dramatically cutting large monorepo check times. It does **not** skip how your code *uses* those types. Keep it on for speed, but validate your own declarations in a separate CI job if you publish a library.

**Code Example**:
```json
{
  "compilerOptions": {
    "skipLibCheck": true,
    "declaration": true,
    "declarationMap": true
  }
}
// Your app code using lib types is still fully checked;
// only intra-.d.ts consistency is skipped.
```

---

<a id="q70"></a>
### Q70: How do Project References and `tsc --build` speed up monorepos?

**Difficulty**: Advanced

**Strategy**:
Project references split a repo into independently buildable programs with `composite: true`, dependency edges in `references`, and `.tsbuildinfo` caching — rebuilding only stale subgraphs. `tsc -b` orchestrates topologically; `paths` aliases keep editor resolution working while emit stays per-package.

**Code Example**:
```json
// packages/core/tsconfig.json
{ "compilerOptions": { "composite": true, "outDir": "dist", "rootDir": "src" },
  "include": ["src"] }
// tsconfig.json (solution style)
{ "files": [], "references": [{ "path": "./packages/core" }, { "path": "./packages/app" }] }
```

---

<a id="q71"></a>
### Q71: What are `incremental`, `.tsbuildinfo`, and `assumeChangesOnlyAffectDirectDependencies` for CI caching?

**Difficulty**: Advanced

**Strategy**:
`incremental: true` serializes the compiler state so subsequent checks replay only changed files; CI caches the `.tsbuildinfo` artifact between runs. `assumeChangesOnlyAffectDirectDependencies` further prunes the recheck graph when you accept its optimistic trade-off — large wins on 5k+ file repos.

**Code Example**:
```yaml
# .github/workflows/ci.yml
- uses: actions/cache@v4
  with:
    path: .tsbuildinfo
    key: tsc-${{ runner.os }}-${{ hashFiles('**/*.ts') }}
- run: npx tsc --noEmit --incremental --tsBuildInfoFile .tsbuildinfo
```

---

<a id="q72"></a>
### Q72: How do path aliases work, and how do you keep bundler + tsc + jest in sync?

**Difficulty**: Intermediate

**Strategy**:
`baseUrl` + `paths` map `@/x` for the type checker only — the runtime needs matching config (tsconfig-paths, jest moduleNameMapper, bundler alias, or package `exports`). Desync shows as editor-clean but runtime/module-not-found; ship one source (tsconfig or package.json workspaces) and generate the rest.

**Code Example**:
```json
// tsconfig.json
{ "compilerOptions": { "baseUrl": ".", "paths": { "@/*": ["src/*"] } } }
// jest.config.js
{ moduleNameMapper: { "^@/(.*)$": "<rootDir>/src/$1" } }
// vite.config.ts
resolve: { alias: { "@": path.resolve(__dirname, "src") } }
```

---

<a id="q73"></a>
### Q73: How do you migrate a large JavaScript codebase to TypeScript incrementally?

**Difficulty**: Advanced

**Strategy**:
Enable `allowJs` + `checkJs` with JSDoc first, rename files opportunistically, and ratchet strictness: `noImplicitAny` last. Use `// @ts-expect-error` as migration scaffolding with a lint rule forbidding new ones, and convert leaf utility modules first so types flow inward.

**Code Example**:
```javascript
// utils.js with checkJs — JSDoc gives real types pre-rename
/** @param {string} id @returns {Promise<import('./types').User>} */
export async function getUser(id) { return fetch(`/users/${id}`).then(r => r.json()); }
```

---

<a id="q74"></a>
### Q74: When is `@ts-ignore` acceptable versus `@ts-expect-error`?

**Difficulty**: Beginner

**Strategy**:
`@ts-expect-error` fails when the suppressed error disappears — self-cleaning, so it's the only acceptable suppression for known limitations. `@ts-ignore` silently rots. Neither should paper over genuine bugs; prefer guards or `unknown` handling, and lint-count all suppressions.

**Code Example**:
```typescript
// @ts-expect-error upstream lib mistypes until v3 (tracked in #1234)
legacyConnect(options);

// CI fails once lib is fixed — the comment must be removed,
// unlike @ts-ignore which hides forever.
```

---

<a id="q75"></a>
### Q75: How do you unit-test types themselves?

**Difficulty**: Advanced

**Strategy**:
Use `expectTypeOf` (vitest) or `tsd` fixtures that assert assignability, equivalence, and never-match at compile time. Type tests run with `tsc --noEmit` in CI and catch regressions in generic utilities that runtime tests cannot express.

**Code Example**:
```typescript
import { expectTypeOf } from "vitest";
import { DeepReadonly } from "./utils";

test("DeepReadonly freezes nesting", () => {
  expectTypeOf<DeepReadonly<{ a: { b: number[] } }>().a.b>().toEqualTypeOf<readonly number[]>();
  expectTypeOf<DeepReadonly<string>>().toEqualTypeOf<string>();
});
```

---

<a id="q76"></a>
### Q76: How does TypeScript's structural typing leak soundness with mutable properties?

**Difficulty**: Expert

**Strategy**:
`{ x: number }` and `{ x: number, y: number }` are mutually assignable, so an object with extra props can flow where fewer are declared; with mutable arrays/props this permits aliasing writes TS cannot track — a deliberate soundness-for-ergonomics trade. Readonly modifiers and exact utility types tighten the holes.

**Code Example**:
```typescript
interface Point { x: number }
const withExtra = { x: 1, y: 2 };
const p: Point = withExtra; // structural: OK, y invisible via p

const arr: Point[] = [withExtra];
function scale(points: { x: number }[]) { points.forEach(pt => pt.x *= 2); }
scale(arr); // y untouched — but nothing stops shapes drifting through aliases
```

---

<a id="q77"></a>
### Q77: What are `unique symbol` and `symbol` registry patterns?

**Difficulty**: Advanced

**Strategy**:
`const s = Symbol()` with `unique symbol` typing makes each symbol a distinct nominal type usable as a precise key. This powers brand metadata and DI tokens whose identity the compiler can distinguish — impossible with strings.

**Code Example**:
```typescript
const LogToken: unique symbol = Symbol("Log") as any;
type Token = typeof LogToken;

const container = new Map<symbol, unknown>();
container.set(LogToken, console.log);

function inject<T>(t: unique symbol): T { return container.get(t) as T; }
const log = inject<typeof console.log>(LogToken);
```

---

<a id="q78"></a>
### Q78: How do you type React-generic components and forwardRef correctly in modern TS?

**Difficulty**: Advanced

**Strategy**:
Type generic components by parameterizing props with their value type and constraining `onChange` against it. Since React 19, `forwardRef` is unnecessary — `ref` is a regular prop; before that, type `forwardRef<HTMLElement, Props>` with the DOM element first. Use `ComponentProps<typeof Button>` to derive instead of duplicating.

**Code Example**:
```tsx
type SelectProps<T extends string> = {
  value: T;
  options: readonly T[];
  onChange: (v: T) => void;
};
function Select<T extends string>({ value, options, onChange }: SelectProps<T>) {
  return <select value={value} onChange={e => onChange(e.target.value as T)}>
    {options.map(o => <option key={o}>{o}</option>)}
  </select>;
}
// React 19: function Input(props: Props & { ref?: Ref<HTMLInputElement> })
```

---

<a id="q79"></a>
### Q79: How do you type event handlers and native events without `any`?

**Difficulty**: Beginner

**Strategy**:
Derive handler types from the element: `React.ChangeEvent<HTMLInputElement>` for inputs, `React.MouseEvent<HTMLButtonElement>` for clicks, or reuse library types via `ComponentProps<"button">["onClick"]`. Never annotate `e: any` — the generic parameters carry the precise `currentTarget` shape.

**Code Example**:
```tsx
function Form() {
  const onChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    e.target.value.trim(); // input-specific
  };
  const onClick = (e: React.MouseEvent<HTMLButtonElement>) => e.currentTarget.disabled;
  return <input onChange={onChange} /><button onClick={onClick} />;
}
```

---

<a id="q80"></a>
### Q80: How do you type fetch wrappers so errors and payloads are precise?

**Difficulty**: Intermediate

**Strategy**:
Wrap fetch to assert `res.ok` (fetch never throws on 4xx/5xx), parse via a validator into `z.infer` types, and return a Result union. This pushes network chaos to one boundary and gives callers a typed `data | error` with status information.

**Code Example**:
```typescript
export async function api<T>(url: string, schema: z.ZodType<T>): Promise<T> {
  const res = await fetch(url);
  if (!res.ok) throw new ApiError(res.status, await res.text());
  return schema.parse(await res.json());
}
class ApiError extends Error { constructor(public status: number, body: string) { super(`HTTP ${status}: ${body}`); } }
const user = await api("/me", UserSchema); // typed or ApiError
```

---

<a id="q81"></a>
### Q81: What is the difference between `type` imports and regular imports for bundlers?

**Difficulty**: Intermediate

**Strategy**:
Types are erased, so a value import used only as a type still emits an import statement — pulling modules into the bundle needlessly under some CJS transforms. `import type` / `export type` guarantees erasure, which `verbatimModuleSyntax` enforces and tree-shakers reward.

**Code Example**:
```typescript
import type { Config } from "./config"; // zero runtime import emitted
import { load } from "./config";        // runtime import

// conditional type-only usage needs the type form even mid-file:
let x: import("./types").User;
```

---

<a id="q82"></a>
### Q82: How do `namespace`s survive today, and should new code use them?

**Difficulty**: Intermediate

**Strategy**:
Namespaces were TS's pre-ESM module system; modern code uses ES modules. Namespaces remain valid for: declaration merging with globals, typing the static side of libraries (`jQuery.ajax`), and co-locating types with runtime constants in `.d.ts`. Avoid them for app-level organization.

**Code Example**:
```typescript
// legacy-global.d.ts — appropriate use
declare namespace Legacy {
  function ajax(url: string): Promise<unknown>;
  const version: string;
}

// modern code: ES modules instead
export const version = "2.0";
export function ajax(url: string) { return fetch(url); }
```

---

<a id="q83"></a>
### Q83: What are index signatures vs `Record` vs a fixed set of known keys?

**Difficulty**: Beginner

**Strategy**:
`{ [k: string]: T }` allows any key (with the pitfalls of `noUncheckedIndexedAccess`), `Record<K, V>` constrains keys to K, and an explicit interface documents a closed shape. Prefer closed shapes → `Record` with a key union → index signature as a last resort for true dictionaries.

**Code Example**:
```typescript
type Env = "dev" | "staging" | "prod";
const urls: Record<Env, string> = { dev: "localhost", staging: "stg", prod: "api" }; // exhaustive

const cache: { [key: string]: number } = {}; // open dictionary
const hit = cache["x"] ?? 0;
```

---

<a id="q84"></a>
### Q84: How do optional properties differ under `exactOptionalPropertyTypes`?

**Difficulty**: Advanced

**Strategy**:
By default `{ opt?: T }` accepts `undefined` assignments (treated as `T | undefined`). With `exactOptionalPropertyTypes`, an omitted key and an explicitly-`undefined` key become distinct — modeling "not provided" vs "provided as undefined", which serializers and patch APIs (JSON Merge Patch) need.

**Code Example**:
```typescript
interface Patch { title?: string }
declare function apply(p: Patch): void;
// without the flag:
apply({ title: undefined });       // allowed
// with exactOptionalPropertyTypes:
apply({ title: undefined });       // Error: undefined not assignable to string|absent
apply({});                          // OK — the only way to express "absent"
```

---

<a id="q85"></a>
### Q85: How do you type curried functions and point-free composition?

**Difficulty**: Expert

**Strategy**:
Currying types chain single-argument returns with inference flowing through generics: each application pins one parameter. `compose` typing uses variadic tuples to thread argument and return types; the classic `pipe(...fns)` signature is the canonical interview challenge.

**Code Example**:
```typescript
function curry<A, B, C>(f: (a: A, b: B) => C) {
  return (a: A) => (b: B) => f(a, b);
}
const add = curry((x: number, y: number) => x + y);
add(1)(2); // 3 — each step typed

function pipe<T extends unknown[], R>(
  ...fns: [(...a: T) => unknown, ...unknown[], (...a: any[]) => R]
): (...a: T) => R {
  return ((...a: T) => (fns as any).reduce((acc, f) => f(acc), fns[0](...a))) as any;
}
```

---

<a id="q86"></a>
### Q86: What are the typing rules for optional and rest parameters in implementations?

**Difficulty**: Beginner

**Strategy**:
Optional parameters must trail required ones; rest parameters are arrays and count as trailing too. A signature accepting `...args: unknown[]` is compatible with concrete tuples, but implementations should type rest as tuples (`...args: [string, number]`) to preserve names and checks.

**Code Example**:
```typescript
function log(msg: string, level?: "info" | "error") {}
function tagged(...args: [template: string, ...values: unknown[]]) {}
function forward<F extends (...a: any[]) => any>(fn: F, ...args: Parameters<F>): ReturnType<F> {
  return fn(...args);
}
```

---

<a id="q87"></a>
### Q87: How do conditional `infer` patterns extract array element, promise value, and function param types together?

**Difficulty**: Advanced

**Strategy**:
Compose conditional types: arrays via `T extends (infer E)[]`, promises via `T extends Promise<infer V>`, functions via `T extends (...a: infer A) => infer R`. Chaining them builds utilities like `Flatten`, `Unwrap`, or `Actions` extraction from reducer maps.

**Code Example**:
```typescript
type ElementOf<T> = T extends readonly (infer E)[] ? E : never;
type AwaitedVal<T> = T extends Promise<infer V> ? AwaitedVal<V> : T;
type Params<T> = T extends (...a: infer A) => any ? A : never;

type Demo = ElementOf<AwaitedVal<Promise<Promise<string[]>>>>; // string
```

---

<a id="q88"></a>
### Q88: How do you write type-safe reducers for state machines?

**Difficulty**: Advanced

**Strategy**:
Model states as a discriminated union and actions as a discriminated union with `type` tags. Type the reducer as `(state: State, action: Action) => State` and switch on both discriminants — illegal transitions become compile errors via the `never` exhaustiveness check.

**Code Example**:
```typescript
type State =
  | { status: "idle" }
  | { status: "saving"; draft: string }
  | { status: "saved"; savedAt: number };
type Action =
  | { type: "edit"; text: string }
  | { type: "save" }
  | { type: "saved"; at: number };

function reducer(s: State, a: Action): State {
  switch (a.type) {
    case "edit": return { status: "saving", draft: a.text };
    case "save": return s.status === "saving" ? s : s; // guard illegal states
    case "saved": return { status: "saved", savedAt: a.at };
    default: { const _: never = a; return s; }
  }
}
```

---

<a id="q89"></a>
### Q89: What are assertion-free strategies for typing JSON Schema / API contracts (OpenAPI codegen)?

**Difficulty**: Intermediate

**Strategy**:
Generate types from the contract source: `openapi-typescript` emits `.d.ts` from specs, tRPC/GraphQL codegen derives client types from the server, Prisma emits models from the schema. Generated-with-drift-prevention beats hand-maintained mirrors; CI diffs fail when the contract changes without regeneration.

**Code Example**:
```bash
npx openapi-typescript ./api-spec.yaml -o ./src/api/schema.d.ts
npx prisma generate
```

---

<a id="q90"></a>
### Q90: How do you avoid `any` when dealing with genuinely dynamic objects (records of callbacks, registries)?

**Difficulty**: Intermediate

**Strategy**:
Type registries as mapped types over known keys (`Record<EventName, Handler>`), use `unknown` for open worlds, and reach for `object`/`Record<string, unknown>` plus guards before narrowing. Generic factory functions preserve relationships so stored/retrieved types stay linked.

**Code Example**:
```typescript
type Event = "click" | "scroll";
const handlers: Record<Event, ((e: unknown) => void)[]> = { click: [], scroll: [] };

function on<E extends Event>(event: E, h: (e: unknown) => void) {
  handlers[event].push(h);
}
const raw: unknown = JSON.parse("{}");
if (typeof raw === "object" && raw !== null && "type" in raw) { /* narrowed */ }
```

---

<a id="q91"></a>
### Q91: What is the `in` operator narrowing, and how does it interact with optional/private properties?

**Difficulty**: Intermediate

**Strategy**:
`"k" in x` narrows to types declaring `k` — the tool for untagged unions. It cannot see optional-vs-required intent (a present-but-undefined optional still narrows positive) and knows nothing about `#private` fields; use discriminant tags when behavior, not shape, differentiates.

**Code Example**:
```typescript
type Response = { error: string } | { data: number[] };
function handle(r: Response) {
  if ("error" in r) return r.error;   // narrowed to error variant
  return r.data.reduce((a, b) => a + b);
}

interface A { kind?: "a"; x?: number }
declare const a: A;
if ("kind" in a && a.kind === "a") a.x?.toFixed(2); // optional still needs inner checks
```

---

<a id="q92"></a>
### Q92: How do you keep `Promise.all`-style combinators precisely typed with heterogeneous tuples?

**Difficulty**: Intermediate

**Strategy**:
`Promise.all` accepts iterables of promises **or** plain values and returns the positional tuple of unwrapped results — driven by mapped-tuple inference. Writing your own combinator requires mapping over the tuple (`{ [K in keyof T]: Awaited<T[K]> }`) — a classic exercise.

**Code Example**:
```typescript
const [user, settings, flag] = await Promise.all([
  fetchUser(),                    // Promise<User>
  fetchSettings(),                // Promise<Settings>
  true,                           // boolean passthrough
]); // tuple types preserved positionally

type All<T extends readonly unknown[]> = { [K in keyof T]: Awaited<T[K]> };
```

---

<a id="q93"></a>
### Q93: What are the typing subtleties of class static blocks and static members with generics?

**Difficulty**: Advanced

**Strategy**:
Static members cannot reference the class's own type parameters (types exist per-instance-generic, statics are per-class). Static blocks (ES2022) initialize complex static state with access to private statics; typing shared per-class state requires a separate interface or a static type parameter pattern.

**Code Example**:
```typescript
class Registry<T> {
  static instances = 0;             // fine: no T
  static defaultFactory: (() => unknown) | null = null; // no T here either
  static { Registry.instances = 0; Registry.defaultFactory = () => ({}); }

  constructor(public value: T) { Registry.instances++; }
  static count(): number { return Registry.instances; }
}
```

---

<a id="q94"></a>
### Q94: How do `ConstructorParameters`, `InstanceType`, and `AbstractConstructor` utilities work?

**Difficulty**: Intermediate

**Strategy**:
`ConstructorParameters<T>` extracts a construct-signature's args as a tuple; `InstanceType<T>` yields the instance; abstract classes need the `abstract new (...)` signature shape. These power DI containers, factory generics, and mixin typing.

**Code Example**:
```typescript
class Repo { constructor(public uri: string, opts?: { ssl?: boolean }) {} }
type RepoArgs = ConstructorParameters<typeof Repo>;   // [uri: string, opts?: {ssl?: boolean}]
type RepoInstance = InstanceType<typeof Repo>;        // Repo

type AnyCtor<T> = abstract new (...args: any[]) => T;
function instantiate<C extends AnyCtor<unknown>>(C: C, ...args: ConstructorParameters<C>): InstanceType<C> {
  return new C(...args);
}
```

---

<a id="q95"></a>
### Q95: How does `useDefineForClassFields` change class emit and interop with decorators?

**Difficulty**: Expert

**Strategy**:
With ES2022 target, class fields use `Object.defineProperty` semantics (own fields defined even when initialized to `undefined`) instead of assignment in the constructor. This breaks patterns relying on assignment-based overrides and interacts with declaration order relative to super() — often surprising with inheritance + field initializers.

**Code Example**:
```typescript
class Base { get name() { return "base"; } }
class Derived extends Base {
  name = "derived"; // defineProperty: own field shadows the getter
}
new Derived().name; // "derived"

class Careful extends Base {
  // declare avoids redefining an inherited field:
  declare name: string;
  constructor() { super(); this.name = "set-in-ctor"; }
}
```

---

<a id="q96"></a>
### Q96: What typing strategies keep tRPC-like end-to-end inference working, and how would you build a minimal router?

**Difficulty**: Expert

**Strategy**:
A tiny RPC layer types a route map object, then indexes it by procedure name so the client's input/output come from the handler's signatures — inference flows server → client with zero codegen. Mapped types + generics over the map are the whole trick.

**Code Example**:
```typescript
type Handler = (input: any) => any;
type Router = Record<string, Handler>;

const router = {
  getUser: (id: string) => ({ id, name: "Ada" }),
  listUsers: (q: { limit: number }) => [{ id: "1", name: "Ada" }],
} satisfies Router;

function createClient<R extends Router>(routes: R) {
  return <K extends keyof R & string>(name: K, ...args: Parameters<R[K]>) =>
    (routes[name] as any)(...args) as ReturnType<R[K]>;
}
const client = createClient(router);
const u = client("getUser", "1");        // typed { id: string; name: string }
```

---

<a id="q97"></a>
### Q97: How do you encode "exactly one of" and "at least one of" constraints at the type level?

**Difficulty**: Expert

**Strategy**:
Use generic constraints over key unions: `AtLeastOne<T>` distributes over `keyof T` making each single-key variant valid; `ExactlyOne` similarly but also `never`-ing the rest via `Pick`. These enforce API payloads (search params, PATCH bodies) without runtime checks.

**Code Example**:
```typescript
type AtLeastOne<T, K extends keyof T = keyof T> =
  K extends K ? { [P in K]: Required<T>[P] } & Partial<T> : never;

interface Search { name?: string; email?: string }
declare function find(s: AtLeastOne<Search>): void;
find({});                    // Error — must provide at least one
find({ name: "a" });         // OK
find({ name: "a", email: "b" }); // OK
```

---

<a id="q98"></a>
### Q98: What are the rules for typing getters/setters and readonly-only arrays in classes?

**Difficulty**: Intermediate

**Strategy**:
Accessors share one type — the getter's return type must be assignable to the setter's parameter. You can declare a public getter with a protected/private setter for read-outside/write-inside semantics; tuple/readonly arrays pair with index-signature-free classes for immutable views.

**Code Example**:
```typescript
class Account {
  #cents = 0;
  get balance(): number { return this.#cents / 100; }
  protected set balance(v: number) { this.#cents = Math.round(v * 100); }
  credit(v: number) { this.balance += v; }
}

class Timeline {
  readonly events: readonly string[] = [];
  record(e: string) { (this.events as string[]).push(e); } // internal mutation via cast gate
}
```

---

<a id="q99"></a>
### Q99: How do you diagnose and fix TS performance problems (deep instantiation, large unions)?

**Difficulty**: Expert

**Strategy**:
Use `tsc --extendedDiagnostics` and `--generateTrace` to find hot spots. Common culprits: recursively-instantiating generics, `keyof` over enormous object types, chain intersections, and project-wide `paths`. Remedies: name intermediate types, split unions, prefer interfaces over type intersections, and enable project references + `skipLibCheck`.

**Code Example**:
```bash
npx tsc --noEmit --extendedDiagnostics
npx tsc --noEmit --generateTrace traces/
```

---

<a id="q100"></a>
### Q100: How do you structure a production-grade tsconfig for a Node.js + library + test matrix?

**Difficulty**: Advanced

**Strategy**:
Use a solution-style root with project references: a `base` config with strictness, an app config targeting the runtime (NodeNext), a library config with `declaration` + `declarationMap` + `composite`, and a test config referencing sources without emitting. This keeps checks incremental, emit correct per target, and editor experience uniform.

**Code Example**:
```json
// tsconfig.base.json
{ "compilerOptions": { "strict": true, "skipLibCheck": true,
  "noUncheckedIndexedAccess": true, "verbatimModuleSyntax": true } }
// tsconfig.src.json (library)
{ "extends": "./tsconfig.base.json",
  "compilerOptions": { "module": "NodeNext", "target": "ES2022",
    "composite": true, "declaration": true, "declarationMap": true, "outDir": "dist" },
  "include": ["src"] }
// tsconfig.test.json
{ "extends": "./tsconfig.base.json", "references": [{ "path": "./tsconfig.src.json" }],
  "compilerOptions": { "noEmit": true, "types": ["vitest/globals"] }, "include": ["tests"] }
```

---
