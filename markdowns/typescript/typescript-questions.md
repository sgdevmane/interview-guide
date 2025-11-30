<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/typescript-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>TypeScript Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for developers</b></p>
</div>

---

## Table of Contents

1. [How do you enforce generic constraints on objects?](#q1-how-do-you-enforce-generic-constraints-on-objects) <span class="intermediate">Intermediate</span>
2. [How do you extract the return type of an async function?](#q2-how-do-you-extract-the-return-type-of-an-async-function) <span class="intermediate">Intermediate</span>
3. [How do you implement a 'Discriminated Union' to handle different API response states (Loading, Success, Error) safely?](#q3-how-do-you-implement-a-discriminated-union-to-handle-different-api-response-states-loading-success-error-safely) <span class="intermediate">Intermediate</span>
4. [How do you create a type requiring at least one property?](#q4-how-do-you-create-a-type-requiring-at-least-one-property) <span class="intermediate">Intermediate</span>
5. [How do you use 'Template Literal Types' to strictly type CSS classes or event names (e.g., 'on-click', 'on-hover')?](#q5-how-do-you-use-template-literal-types-to-strictly-type-css-classes-or-event-names-eg-on-click-on-hover) <span class="intermediate">Intermediate</span>
6. [How do you implement a custom Type Guard?](#q6-how-do-you-implement-a-custom-type-guard) <span class="intermediate">Intermediate</span>
7. [How do you create a 'readonly' array or tuple so that its contents cannot be modified after initialization?](#q7-how-do-you-create-a-readonly-array-or-tuple-so-that-its-contents-cannot-be-modified-after-initialization) <span class="intermediate">Intermediate</span>
8. [How do you use `unknown` vs `any` for type safety?](#q8-how-do-you-use-unknown-vs-any-for-type-safety) <span class="intermediate">Intermediate</span>
9. [How do you use 'Mapped Types' to create a new type where all boolean properties of an interface are changed to strings?](#q9-how-do-you-use-mapped-types-to-create-a-new-type-where-all-boolean-properties-of-an-interface-are-changed-to-strings) <span class="intermediate">Intermediate</span>
10. [How do you define a React Component Prop type that accepts *either* an `image` URL *or* a `text` label, but not both?](#q10-how-do-you-define-a-react-component-prop-type-that-accepts-either-an-image-url-or-a-text-label-but-not-both) <span class="intermediate">Intermediate</span>
11. [How do you implement a generic 'Singleton' pattern in TypeScript using a static `getInstance` method?](#q11-how-do-you-implement-a-generic-singleton-pattern-in-typescript-using-a-static-getinstance-method) <span class="intermediate">Intermediate</span>
12. [How do you use the `infer` keyword to extract the type of the first argument of a function?](#q12-how-do-you-use-the-infer-keyword-to-extract-the-type-of-the-first-argument-of-a-function) <span class="intermediate">Intermediate</span>
13. [How do you fix the error 'Element implicitly has an any type because expression of type string can't be used to index type'?](#q13-how-do-you-fix-the-error-element-implicitly-has-an-any-type-because-expression-of-type-string-cant-be-used-to-index-type) <span class="intermediate">Intermediate</span>
14. [How do you declare a global variable (e.g., `window.myConfig`) so TypeScript recognizes it without errors?](#q14-how-do-you-declare-a-global-variable-eg-windowmyconfig-so-typescript-recognizes-it-without-errors) <span class="intermediate">Intermediate</span>
15. [How do you use TypeScript's `satisfies` operator to validate an expression matches a type without widening it?](#q15-how-do-you-use-typescripts-satisfies-operator-to-validate-an-expression-matches-a-type-without-widening-it) <span class="intermediate">Intermediate</span>
16. [How do you implement a `DeepPartial<T>` utility type?](#q16-how-do-you-implement-a-deeppartialt-utility-type) <span class="advanced">Advanced</span>
17. [How do you use `const` assertions (`as const`) to create literal types?](#q17-how-do-you-use-const-assertions-as-const-to-create-literal-types) <span class="intermediate">Intermediate</span>
18. [How do you use `Awaited<T>` to unwrap Promise types recursively?](#q18-how-do-you-use-awaitedt-to-unwrap-promise-types-recursively) <span class="intermediate">Intermediate</span>
19. [How do you create a type that requires exactly one of two properties (XOR)?](#q19-how-do-you-create-a-type-that-requires-exactly-one-of-two-properties-xor) <span class="advanced">Advanced</span>
20. [How do you use `keyof` with Generics to access properties safely?](#q20-how-do-you-use-keyof-with-generics-to-access-properties-safely) <span class="intermediate">Intermediate</span>
21. [How do you implement a specialized `Pick` that filters by value type?](#q21-how-do-you-implement-a-specialized-pick-that-filters-by-value-type) <span class="advanced">Advanced</span>
22. [How do you use `asserts` to create a custom assertion function?](#q22-how-do-you-use-asserts-to-create-a-custom-assertion-function) <span class="intermediate">Intermediate</span>
23. [How do you use `ThisType<T>` to type `this` in object literals?](#q23-how-do-you-use-thistypet-to-type-this-in-object-literals) <span class="advanced">Advanced</span>
24. [How do you make a tuple type with a variable number of elements (Variadic Tuples)?](#q24-how-do-you-make-a-tuple-type-with-a-variable-number-of-elements-variadic-tuples) <span class="advanced">Advanced</span>
25. [How do you use `never` type for exhaustive checks in switch statements?](#q25-how-do-you-use-never-type-for-exhaustive-checks-in-switch-statements) <span class="intermediate">Intermediate</span>
26. [How do you use Module Augmentation to extend third-party libraries?](#q26-how-do-you-use-module-augmentation-to-extend-third-party-libraries) <span class="intermediate">Intermediate</span>
27. [How do you implement a generic `Mutable<T>` utility type?](#q27-how-do-you-implement-a-generic-mutablet-utility-type) <span class="intermediate">Intermediate</span>
28. [How do you use `Omit` to exclude properties from a type?](#q28-how-do-you-use-omit-to-exclude-properties-from-a-type) <span class="beginner">Beginner</span>
29. [How do you type a function with function overloads?](#q29-how-do-you-type-a-function-with-function-overloads) <span class="intermediate">Intermediate</span>
30. [How do you use the `instanceof` type guard?](#q30-how-do-you-use-the-instanceof-type-guard) <span class="beginner">Beginner</span>
31. [What is the difference between `never` and `void`?](#q31-what-is-the-difference-between-never-and-void) <span class="intermediate">Intermediate</span>
32. [How do you implement Branded Types (Nominal Typing) to prevent accidental assignment?](#q32-how-do-you-implement-branded-types-nominal-typing-to-prevent-accidental-assignment) <span class="advanced">Advanced</span>
33. [How do you create a Conditional Type?](#q33-how-do-you-create-a-conditional-type) <span class="intermediate">Intermediate</span>
34. [How do you use `import type` and why is it useful?](#q34-how-do-you-use-import-type-and-why-is-it-useful) <span class="beginner">Beginner</span>
35. [How do you convert a Tuple to a Union type?](#q35-how-do-you-convert-a-tuple-to-a-union-type) <span class="intermediate">Intermediate</span>
36. [Why should you prefer `as const` objects over `enum`?](#q36-why-should-you-prefer-as-const-objects-over-enum) <span class="intermediate">Intermediate</span>
37. [How do you use `NonNullable<T>` to remove null and undefined?](#q37-how-do-you-use-nonnullablet-to-remove-null-and-undefined) <span class="beginner">Beginner</span>
38. [How do you use `Parameters<T>` to extract function argument types?](#q38-how-do-you-use-parameterst-to-extract-function-argument-types) <span class="intermediate">Intermediate</span>
39. [What is the difference between `Exclude` and `Omit`?](#q39-what-is-the-difference-between-exclude-and-omit) <span class="intermediate">Intermediate</span>
40. [How do you use `Record<K, T>` to create a dictionary?](#q40-how-do-you-use-recordk-t-to-create-a-dictionary) <span class="beginner">Beginner</span>
41. [How do you implement Mixins in TypeScript?](#q41-how-do-you-implement-mixins-in-typescript) <span class="advanced">Advanced</span>
42. [How do you use `ConstructorParameters<T>`?](#q42-how-do-you-use-constructorparameterst) <span class="advanced">Advanced</span>
43. [How do you force a type to be partially optional using a utility type?](#q43-how-do-you-force-a-type-to-be-partially-optional-using-a-utility-type) <span class="advanced">Advanced</span>
44. [What is Covariance vs Contravariance in TypeScript?](#q44-what-is-covariance-vs-contravariance-in-typescript) <span class="expert">Expert</span>
45. [How do you make a class property private at runtime vs compile time?](#q45-how-do-you-make-a-class-property-private-at-runtime-vs-compile-time) <span class="beginner">Beginner</span>
46. [How do you handle circular dependencies in types?](#q46-how-do-you-handle-circular-dependencies-in-types) <span class="intermediate">Intermediate</span>
47. [How do you assert that a value is defined (Not Null Assertion)?](#q47-how-do-you-assert-that-a-value-is-defined-not-null-assertion) <span class="beginner">Beginner</span>
48. [How do you use `Partial<T>` to update objects?](#q48-how-do-you-use-partialt-to-update-objects) <span class="beginner">Beginner</span>
49. [How do you use `ReturnType` to create a type from a function implementation?](#q49-how-do-you-use-returntype-to-create-a-type-from-a-function-implementation) <span class="intermediate">Intermediate</span>
50. [How do you strictly type the `this` context in a function?](#q50-how-do-you-strictly-type-the-this-context-in-a-function) <span class="advanced">Advanced</span>

---

### Q1: How do you enforce generic constraints on objects?

**Difficulty**: Intermediate

**Strategy:**
Use `T extends { id: string | number }` to restrict the generic type.

**Code Example:**
```typescript
interface Identifiable {
  id: string | number;
}

function getIds<T extends Identifiable>(items: T[]): (string | number)[] {
  return items.map(item => item.id);
}

// Usage
getIds([{ id: 1, name: 'A' }, { id: 2, name: 'B' }]); // OK
// getIds([{ name: 'C' }]); // Error: Property 'id' is missing
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q2: How do you extract the return type of an async function?

**Difficulty**: Intermediate

**Strategy:**
Combine `ReturnType` to get the Promise, and `Awaited` (TS 4.5+) to unwrap the Promise.

**Code Example:**
```typescript
async function fetchUser() {
  return { id: 1, name: "Alice", role: "Admin" };
}

// Extract the resolved type
type User = Awaited<ReturnType<typeof fetchUser>>;

// Result: { id: number; name: string; role: string; }
const user: User = { id: 2, name: "Bob", role: "User" };
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q3: How do you implement a 'Discriminated Union' to handle different API response states (Loading, Success, Error) safely?

**Difficulty**: Intermediate

**Strategy:**
Use a `status` property to discriminate between the types.

**Code Example:**
```typescript
type ApiResponse<T> =
  | { status: "loading" }
  | { status: "success"; data: T }
  | { status: "error"; message: string };

function handleResponse(response: ApiResponse<string[]>) {
  switch (response.status) {
    case "loading":
      return "Loading...";
    case "success":
      // TypeScript knows 'data' exists here
      return `Found ${response.data.length} items`;
    case "error":
      // TypeScript knows 'message' exists here
      return `Error: ${response.message}`;
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q4: How do you create a type requiring at least one property?

**Difficulty**: Intermediate

**Strategy:**
There is no built-in utility for this, so you construct it using `Pick`, `Partial`, and a mapped type.

**Code Example:**
```typescript
type RequireAtLeastOne<T> = {
  [K in keyof T]-?: Required<Pick<T, K>> & Partial<Pick<T, Exclude<keyof T, K>>>;
}[keyof T];

interface User {
  name: string;
  email: string;
  age: number;
}

// Valid: Has name
const u1: RequireAtLeastOne<User> = { name: "Alice" };
// Valid: Has email and age
const u2: RequireAtLeastOne<User> = { email: "a@b.com", age: 30 };
// Error: Empty object
// const u3: RequireAtLeastOne<User> = {};
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q5: How do you use 'Template Literal Types' to strictly type CSS classes or event names (e.g., 'on-click', 'on-hover')?

**Difficulty**: Intermediate

**Strategy:**
Combine string literals to generate a set of allowed strings.

**Code Example:**
```typescript
type EventName = "click" | "hover" | "focus";
type HandlerName = `on-${EventName}`; 

// HandlerName is: "on-click" | "on-hover" | "on-focus"

function addHandler(event: HandlerName) {
  console.log(`Adding handler for ${event}`);
}

addHandler("on-click"); // OK
// addHandler("on-drag"); // Error
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q6: How do you implement a custom Type Guard?

**Difficulty**: Intermediate

**Strategy:**
TypeScript automatically narrows the type inside the `if` block.

**Code Example:**
```typescript
function formatInput(input: string | number) {
  if (typeof input === "string") {
    // input is strictly 'string' here
    return input.toUpperCase();
  }
  // input is strictly 'number' here
  return input.toFixed(2);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q7: How do you create a 'readonly' array or tuple so that its contents cannot be modified after initialization?

**Difficulty**: Intermediate

**Strategy:**
Use the `readonly` modifier or `ReadonlyArray<T>` to prevent mutation methods like `push` or `pop`. Alternatively, use `as const` for a deeply readonly literal.

**Code Example:**
```typescript
// Option 1: readonly keyword
const colors: readonly string[] = ["red", "green", "blue"];
// colors.push("yellow"); // Error

// Option 2: as const (makes it a readonly tuple)
const config = ["DEV", "PROD"] as const;
// config[0] = "TEST"; // Error
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q8: How do you use `unknown` vs `any` for type safety?

**Difficulty**: Intermediate

**Strategy:**
`unknown` forces you to check the type before usage, preventing runtime crashes.

**Code Example:**
```typescript
function parseData(json: string) {
  const data: unknown = JSON.parse(json);

  // Error: Object is of type 'unknown'
  // console.log(data.id); 

  if (
    typeof data === "object" && 
    data !== null && 
    "id" in data
  ) {
    // Safe to access
    console.log((data as { id: number }).id);
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q9: How do you use 'Mapped Types' to create a new type where all boolean properties of an interface are changed to strings?

**Difficulty**: Intermediate

**Strategy:**
Iterate over keys and check value types.

**Code Example:**
```typescript
interface Settings {
  darkMode: boolean;
  notifications: boolean;
  version: number;
  title: string;
}

type BooleanToString<T> = {
  [K in keyof T]: T[K] extends boolean ? string : T[K];
};

type NewSettings = BooleanToString<Settings>;
// Result:
// {
//   darkMode: string;
//   notifications: string;
//   version: number;
//   title: string;
// }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q10: How do you define a React Component Prop type that accepts *either* an `image` URL *or* a `text` label, but not both?

**Difficulty**: Intermediate

**Strategy:**
Disable the conflicting property in each union member.

**Code Example:**
```typescript
type ImageProps = {
  image: string;
  text?: never; // text must NOT exist
};

type TextProps = {
  text: string;
  image?: never; // image must NOT exist
};

type CardProps = ImageProps | TextProps;

// Usage
const c1: CardProps = { image: "pic.jpg" }; // OK
const c2: CardProps = { text: "Hello" };    // OK
// const c3: CardProps = { image: "pic.jpg", text: "Hello" }; // Error
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q11: How do you implement a generic 'Singleton' pattern in TypeScript using a static `getInstance` method?

**Difficulty**: Intermediate

**Strategy:**
Make the constructor `private` to prevent direct instantiation. Use a static property to hold the instance and a static method `getInstance()` to return it, creating it only if it doesn't exist.

**Code Example:**
```typescript
class Database {
  private static instance: Database;
  
  // Private constructor prevents direct instantiation
  private constructor() {}

  static getInstance(): Database {
    if (!Database.instance) {
      Database.instance = new Database();
    }
    return Database.instance;
  }
}

const db1 = Database.getInstance();
const db2 = Database.getInstance();
console.log(db1 === db2); // true
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q12: How do you use the `infer` keyword to extract the type of the first argument of a function?

**Difficulty**: Intermediate

**Strategy:**
Use `infer` within a conditional type to deduce a specific type. For the first argument, pattern match the function signature: `(first: infer U, ...args: any[]) => any`.

**Code Example:**
```typescript
type FirstArg<T> = T extends (first: infer U, ...args: any[]) => any 
  ? U 
  : never;

function greet(name: string, age: number) {
  console.log(`Hello ${name}`);
}

type NameType = FirstArg<typeof greet>; // string
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q13: How do you fix the error 'Element implicitly has an any type because expression of type string can't be used to index type'?

**Difficulty**: Intermediate

**Strategy:**
The error occurs when accessing an object with a loose string.

**Code Example:**
```typescript
const colors = {
  red: "#FF0000",
  green: "#00FF00",
  blue: "#0000FF"
};

function getColor(name: string) {
  // Error: Element implicitly has an 'any' type...
  // return colors[name]; 
  
  // Fix 1: Cast the key
  return colors[name as keyof typeof colors];
}

// Fix 2 (if keys are dynamic): Add index signature to type
// type ColorMap = { [key: string]: string };
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q14: How do you declare a global variable (e.g., `window.myConfig`) so TypeScript recognizes it without errors?

**Difficulty**: Intermediate

**Strategy:**
Extend the `Window` interface.

**Code Example:**
```typescript
// global.d.ts
export {}; // Make this a module

declare global {
  interface Window {
    myConfig: {
      apiUrl: string;
      retryCount: number;
    };
  }
}

// Now valid in any file
window.myConfig = { apiUrl: "/api", retryCount: 3 };
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q15: How do you use TypeScript's `satisfies` operator to validate an expression matches a type without widening it?

**Difficulty**: Intermediate

**Strategy:**
It checks compatibility but keeps the specific literal types.

**Code Example:**
```typescript
type Config = {
  colors: Record<string, string | { r: number; g: number; b: number }>;
};

const myTheme = {
  colors: {
    primary: "red",
    secondary: { r: 0, g: 255, b: 0 }
  }
} satisfies Config;

// 'primary' is still strictly "red" (string), not widened
// 'secondary' is still the object structure
console.log(myTheme.colors.primary.toUpperCase()); // OK
console.log(myTheme.colors.secondary.r); // OK
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q16: How do you implement a `DeepPartial<T>` utility type?

**Difficulty**: Advanced

**Strategy:**
The built-in `Partial<T>` only makes top-level properties optional. To make nested properties optional recursively, you need a conditional mapped type.

**Code Example:**
```typescript
type DeepPartial<T> = {
  [P in keyof T]?: T[P] extends object 
    ? DeepPartial<T[P]> 
    : T[P];
};

interface User {
  id: number;
  name: string;
  address: {
    city: string;
    zip: string;
  };
}

const user: DeepPartial<User> = {
  address: {
    city: "New York" // zip is optional
  }
};
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q17: How do you use `const` assertions (`as const`) to create literal types?

**Difficulty**: Intermediate

**Strategy:**
`as const` freezes the object or array, making properties readonly and narrowing types to their literal values instead of general types (e.g., 'string').

**Code Example:**
```typescript
const config = {
  endpoint: "https://api.example.com",
  retries: 3
} as const;

// Type is:
// {
//   readonly endpoint: "https://api.example.com";
//   readonly retries: 3;
// }

// Useful for Redux actions or enums
const Colors = ["red", "green", "blue"] as const;
type Color = typeof Colors[number]; // "red" | "green" | "blue" 
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q18: How do you use `Awaited<T>` to unwrap Promise types recursively?

**Difficulty**: Intermediate

**Strategy:**
`Awaited<T>` (TS 4.5+) models the behavior of `await` in async functions, recursively unwrapping Promises to get the final result type.

**Code Example:**
```typescript
type User = { id: number; name: string };

async function fetchUser(): Promise<User> {
  return { id: 1, name: "Alice" };
}

type FetchResult = ReturnType<typeof fetchUser>; // Promise<User>
type UserResult = Awaited<FetchResult>; // User

// Works recursively
type Nested = Promise<Promise<string>>;
type Result = Awaited<Nested>; // string
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q19: How do you create a type that requires exactly one of two properties (XOR)?

**Difficulty**: Advanced

**Strategy:**
To enforce that an object has property A OR property B, but not both (and not neither), you can use a union type with `never`.

**Code Example:**
```typescript
type XOR<T, U> = (T | U) extends object 
  ? (Without<T, U> & U) | (Without<U, T> & T) 
  : T | U;

type Without<T, U> = { [P in Exclude<keyof T, keyof U>]?: never };

// Simple version for two specific types:
type A = { a: string };
type B = { b: number };

type AorB = 
  | (A & { b?: never })
  | (B & { a?: never });

const valid1: AorB = { a: "hello" };
const valid2: AorB = { b: 42 };
// const invalid: AorB = { a: "hello", b: 42 }; // Error
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q20: How do you use `keyof` with Generics to access properties safely?

**Difficulty**: Intermediate

**Strategy:**
Use `K extends keyof T` to constrain a generic type parameter to be a valid key of object `T`.

**Code Example:**
```typescript
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}

const user = {
  id: 1,
  name: "Alice"
};

const userName = getProperty(user, "name"); // Type is string
// const invalid = getProperty(user, "age"); // Error: Argument of type '"age"' is not assignable...
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q21: How do you implement a specialized `Pick` that filters by value type?

**Difficulty**: Advanced

**Strategy:**
You can combine Mapped Types and Key Remapping (TS 4.1+) to pick properties based on their value type (e.g., keep only string properties).

**Code Example:**
```typescript
type PickByValue<T, ValueType> = {
  [P in keyof T as T[P] extends ValueType ? P : never]: T[P]
};

interface Person {
  id: number;
  name: string;
  isAdmin: boolean;
  bio: string;
}

type StringProps = PickByValue<Person, string>;
// Result: { name: string; bio: string; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q22: How do you use `asserts` to create a custom assertion function?

**Difficulty**: Intermediate

**Strategy:**
Assertion functions tell the compiler that if the function returns, a specific condition must be true. This narrows the type in the scope following the call.

**Code Example:**
```typescript
function assertIsString(val: any): asserts val is string {
  if (typeof val !== "string") {
    throw new Error("Not a string!");
  }
}

function processValue(val: any) {
  assertIsString(val);
  // TypeScript knows 'val' is string here
  console.log(val.toUpperCase());
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q23: How do you use `ThisType<T>` to type `this` in object literals?

**Difficulty**: Advanced

**Strategy:**
`ThisType<T>` is a built-in marker interface used to type `this` inside object literals, typically in frameworks like Vue or generic state managers.

**Code Example:**
```typescript
type ObjectDescriptor<D, M> = {
  data?: D;
  methods?: M & ThisType<D & M>; // 'this' inside methods sees data & methods
};

function makeObject<D, M>(desc: ObjectDescriptor<D, M>): D & M {
  let data = desc.data || {} as D;
  let methods = desc.methods || {} as M;
  return { ...data, ...methods };
}

const obj = makeObject({
  data: { x: 10, y: 20 },
  methods: {
    moveBy(dx: number, dy: number) {
      this.x += dx; // 'this' is typed!
      this.y += dy;
    }
  }
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q24: How do you make a tuple type with a variable number of elements (Variadic Tuples)?

**Difficulty**: Advanced

**Strategy:**
Variadic Tuple Types (TS 4.0+) allow you to use spreads in tuple types, enabling concatenation and manipulation of tuple types.

**Code Example:**
```typescript
type Strings = [string, string];
type Numbers = [number, number];

// Spread types
type StrNumStr = [...Strings, ...Numbers]; 
// [string, string, number, number]

function concat<T extends unknown[], U extends unknown[]>(arr1: [...T], arr2: [...U]): [...T, ...U] {
  return [...arr1, ...arr2];
}

const result = concat([1, 2], ["a", "b"]);
// result type: [number, number, string, string]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q25: How do you use `never` type for exhaustive checks in switch statements?

**Difficulty**: Intermediate

**Strategy:**
The `never` type represents values that never occur. Assigning a value to `never` causes a compile error, which is useful to ensure all cases in a union are handled.

**Code Example:**
```typescript
type Shape = 
  | { kind: "circle"; radius: number }
  | { kind: "square"; side: number };

function getArea(shape: Shape) {
  switch (shape.kind) {
    case "circle":
      return Math.PI * shape.radius ** 2;
    case "square":
      return shape.side ** 2;
    default:
      // This line errors if a new Shape kind is added but not handled
      const _exhaustiveCheck: never = shape;
      return _exhaustiveCheck;
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q26: How do you use Module Augmentation to extend third-party libraries?

**Difficulty**: Intermediate

**Strategy:**
Module Augmentation allows you to add properties to existing types defined in external modules.

**Code Example:**
```typescript
// custom.d.ts
import "express";

declare module "express" {
  interface Request {
    user?: {
      id: string;
      role: string;
    };
  }
}

// main.ts
import express from "express";
const app = express();

app.use((req, res, next) => {
  req.user = { id: "1", role: "admin" }; // Valid now
  next();
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q27: How do you implement a generic `Mutable<T>` utility type?

**Difficulty**: Intermediate

**Strategy:**
`Mutable<T>` removes the `readonly` modifier from all properties of a type.

**Code Example:**
```typescript
type Mutable<T> = {
  -readonly [P in keyof T]: T[P];
};

type ReadonlyUser = {
  readonly id: number;
  readonly name: string;
};

type WritableUser = Mutable<ReadonlyUser>;
// { id: number; name: string; }

const u: WritableUser = { id: 1, name: "Bob" };
u.id = 2; // OK
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q28: How do you use `Omit` to exclude properties from a type?

**Difficulty**: Beginner

**Strategy:**
`Omit<T, K>` constructs a type by picking all properties from T and then removing Keys K.

**Code Example:**
```typescript
interface Todo {
  id: string;
  title: string;
  completed: boolean;
  createdAt: number;
}

// Remove 'id' and 'createdAt' for creation payload
type TodoPreview = Omit<Todo, "id" | "createdAt">;

const todo: TodoPreview = {
  title: "Clean room",
  completed: false
};
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q29: How do you type a function with function overloads?

**Difficulty**: Intermediate

**Strategy:**
Function overloads allow you to define multiple signatures for a single function implementation. The implementation signature must be compatible with all overloads.

**Code Example:**
```typescript
function makeDate(timestamp: number): Date;
function makeDate(m: number, d: number, y: number): Date;
function makeDate(mOrTimestamp: number, d?: number, y?: number): Date {
  if (d !== undefined && y !== undefined) {
    return new Date(y, mOrTimestamp, d);
  } else {
    return new Date(mOrTimestamp);
  }
}

const d1 = makeDate(12345678);
const d2 = makeDate(5, 5, 2021);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q30: How do you use the `instanceof` type guard?

**Difficulty**: Beginner

**Strategy:**
`instanceof` is a runtime check that TypeScript recognizes as a type guard for class instances.

**Code Example:**
```typescript
class Dog {
  bark() { console.log("Woof"); }
}

class Cat {
  meow() { console.log("Meow"); }
}

function interact(pet: Dog | Cat) {
  if (pet instanceof Dog) {
    pet.bark(); // TS knows pet is Dog
  } else {
    pet.meow(); // TS knows pet is Cat
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---


### Q31: What is the difference between `never` and `void`?

**Difficulty**: Intermediate

**Strategy:**
`void` means a function returns nothing (or undefined). `never` means a function *never* returns (e.g., it throws an error or has an infinite loop).

**Code Example:**
function logMessage(msg: string): void {
  console.log(msg);
  // Returns undefined implicitly
}

function throwError(msg: string): never {
  throw new Error(msg);
  // Execution stops here, never returns
}

function infiniteLoop(): never {
  while (true) {}
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q32: How do you implement Branded Types (Nominal Typing) to prevent accidental assignment?

**Difficulty**: Advanced

**Strategy:**
TypeScript uses Structural Typing (duck typing). To enforce Nominal Typing (where types are equal only if they have the same name), you can use a 'brand' property.

**Code Example:**
type USD = number & { __brand: 'USD' };
type EUR = number & { __brand: 'EUR' };

function usd(value: number): USD {
  return value as USD;
}

function eur(value: number): EUR {
  return value as EUR;
}

const dollars = usd(10);
const euros = eur(10);

// dollars = euros; // Error: Type 'EUR' is not assignable to type 'USD'.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q33: How do you create a Conditional Type?

**Difficulty**: Intermediate

**Strategy:**
Conditional types work like ternary operators: `T extends U ? X : Y`. They allow types to be determined dynamically based on other types.

**Code Example:**
type IsString<T> = T extends string ? true : false;

type A = IsString<string>; // true
type B = IsString<number>; // false

// Practical: Extract array type
type Flatten<T> = T extends any[] ? T[number] : T;

type Str = Flatten<string[]>; // string
type Num = Flatten<number>;   // number

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q34: How do you use `import type` and why is it useful?

**Difficulty**: Beginner

**Strategy:**
`import type` ensures that the import is erased during compilation. It avoids circular dependency issues at runtime and clarifies that the import is only for type checking.

**Code Example:**
// types.ts
export interface User { name: string; }

// app.ts
import type { User } from './types';

const user: User = { name: 'Alice' };

// Compiled JS:
// const user = { name: 'Alice' };
// (The import statement is completely removed)

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q35: How do you convert a Tuple to a Union type?

**Difficulty**: Intermediate

**Strategy:**
Use the indexed access type `[number]` on the tuple.

**Code Example:**
const colors = ['red', 'green', 'blue'] as const;

// Type is 'red' | 'green' | 'blue'
type Color = typeof colors[number];

const c1: Color = 'red'; // OK
// const c2: Color = 'yellow'; // Error

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q36: Why should you prefer `as const` objects over `enum`?

**Difficulty**: Intermediate

**Strategy:**
TypeScript `enum` generates extra runtime code (IIFE). Objects with `as const` generate zero runtime overhead (except the object itself) and are safer.

**Code Example:**
// Enum (Generates code)
enum Direction {
  Up,
  Down
}

// Object as const (Cleaner)
const DirectionConst = {
  Up: 'UP',
  Down: 'DOWN'
} as const;

type DirectionType = typeof DirectionConst[keyof typeof DirectionConst];
// 'UP' | 'DOWN'

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q37: How do you use `NonNullable<T>` to remove null and undefined?

**Difficulty**: Beginner

**Strategy:**
`NonNullable<T>` constructs a type by excluding `null` and `undefined` from `T`.

**Code Example:**
type MaybeString = string | null | undefined;

type DefinitelyString = NonNullable<MaybeString>;
// string

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q38: How do you use `Parameters<T>` to extract function argument types?

**Difficulty**: Intermediate

**Strategy:**
`Parameters<T>` returns a tuple type containing the types of the arguments of a function type `T`.

**Code Example:**
function createUser(name: string, age: number) {
  return { name, age };
}

type CreateUserArgs = Parameters<typeof createUser>;
// [name: string, age: number]

const args: CreateUserArgs = ['Alice', 30];
createUser(...args);

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q39: What is the difference between `Exclude` and `Omit`?

**Difficulty**: Intermediate

**Strategy:**
`Exclude<T, U>` removes types from a **Union**. `Omit<T, K>` removes keys from an **Object** type.

**Code Example:**
// Exclude (Union)
type T1 = Exclude<"a" | "b" | "c", "a">;
// "b" | "c"

// Omit (Object)
interface Todo {
  title: string;
  completed: boolean;
  createdAt: number;
}
type TodoPreview = Omit<Todo, "completed" | "createdAt">;
// { title: string; }

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q40: How do you use `Record<K, T>` to create a dictionary?

**Difficulty**: Beginner

**Strategy:**
`Record<K, T>` constructs an object type whose property keys are `K` and whose property values are `T`. Useful for mapping keys to values.

**Code Example:**
type Role = 'admin' | 'user' | 'guest';

interface UserInfo {
  id: number;
}

const usersByRole: Record<Role, UserInfo[]> = {
  admin: [{ id: 1 }],
  user: [{ id: 2 }, { id: 3 }],
  guest: []
};

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q41: How do you implement Mixins in TypeScript?

**Difficulty**: Advanced

**Strategy:**
Mixins allow you to build up classes from reusable components. A mixin is a function that takes a class and returns a new class extending it.

**Code Example:**
type Constructor = new (...args: any[]) => {};

function Timestamped<TBase extends Constructor>(Base: TBase) {
  return class extends Base {
    timestamp = Date.now();
  };
}

class User {
  name = "Alice";
}

const TimestampedUser = Timestamped(User);
const user = new TimestampedUser();
console.log(user.name, user.timestamp);

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q42: How do you use `ConstructorParameters<T>`?

**Difficulty**: Advanced

**Strategy:**
`ConstructorParameters<T>` extracts the tuple of argument types from a constructor function type.

**Code Example:**
class Point {
  constructor(public x: number, public y: number) {}
}

type PointParams = ConstructorParameters<typeof Point>;
// [x: number, y: number]

const coords: PointParams = [10, 20];
const p = new Point(...coords);

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q43: How do you force a type to be partially optional using a utility type?

**Difficulty**: Advanced

**Strategy:**
Combine `Omit`, `Partial`, and intersection `&` to make specific keys optional while keeping others required.

**Code Example:**
interface User {
  id: string;
  name: string;
  email: string;
}

// Make 'email' optional, keep 'id' and 'name' required
type UserOptionalEmail = Omit<User, 'email'> & Partial<Pick<User, 'email'>>;

const u: UserOptionalEmail = {
  id: '1',
  name: 'Alice'
  // email is optional
};

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q44: What is Covariance vs Contravariance in TypeScript?

**Difficulty**: Expert

**Strategy:**
TypeScript is generally covariant (allows subtype assignment). However, function parameters are contravariant (you can pass a function that accepts a supertype), while return types are covariant.

**Code Example:**
interface Animal { name: string; }
interface Dog extends Animal { breed: string; }

let animal: Animal;
let dog: Dog;

// Covariance (Return types):
// A function returning Dog is assignable to a function returning Animal.
type Getter<T> = () => T;
let getAnimal: Getter<Animal>;
let getDog: Getter<Dog>;
getAnimal = getDog; // ✅ OK

// Contravariance (Parameters):
// A function taking Animal is assignable to a function taking Dog.
type Setter<T> = (item: T) => void;
let setAnimal: Setter<Animal>;
let setDog: Setter<Dog>;
setDog = setAnimal; // ✅ OK: If it handles any Animal, it handles a Dog.
// setAnimal = setDog; // ❌ Error: setDog might need 'breed' which Animal lacks.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q45: How do you make a class property private at runtime vs compile time?

**Difficulty**: Beginner

**Strategy:**
`private` keyword is compile-time only (erased in JS). `#` prefix creates a true private field in JavaScript runtime.

**Code Example:**
class Counter {
  private compileTimePrivate = 0; // Accessible via (counter as any).compileTimePrivate
  #runtimePrivate = 0; // Truly inaccessible
  
  increment() {
    this.#runtimePrivate++;
  }
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q46: How do you handle circular dependencies in types?

**Difficulty**: Intermediate

**Strategy:**
TypeScript handles recursive types automatically if they are defined correctly using interfaces or type aliases.

**Code Example:**
interface Category {
  name: string;
  subcategories: Category[]; // Recursive reference
}

const root: Category = {
  name: "Electronics",
  subcategories: [
    { name: "Laptops", subcategories: [] }
  ]
};

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q47: How do you assert that a value is defined (Not Null Assertion)?

**Difficulty**: Beginner

**Strategy:**
Use the postfix `!` operator. Use this only when you are certain the value is not null/undefined.

**Code Example:**
const input = document.getElementById("my-input")!; 
// Type is HTMLElement, not HTMLElement | null

// Alternative (Safer):
if (input) {
  // Type narrowed inside block
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q48: How do you use `Partial<T>` to update objects?

**Difficulty**: Beginner

**Strategy:**
`Partial<T>` sets all properties of T to optional. This is useful for update functions that accept a subset of fields.

**Code Example:**
interface User {
  id: number;
  name: string;
  age: number;
}

function updateUser(id: number, changes: Partial<User>) {
  // ... logic to merge changes
}

updateUser(1, { age: 31 }); // Valid
updateUser(1, { name: "Bob" }); // Valid

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q49: How do you use `ReturnType` to create a type from a function implementation?

**Difficulty**: Intermediate

**Strategy:**
Useful when you have a function but no explicit interface for its return value.

**Code Example:**
function createConfig() {
  return {
    port: 8080,
    db: 'postgres',
    debug: true
  };
}

type Config = ReturnType<typeof createConfig>;
// { port: number; db: string; debug: boolean; }

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q50: How do you strictly type the `this` context in a function?

**Difficulty**: Advanced

**Strategy:**
Declare `this` as the first parameter in the function signature. It is erased at runtime.

**Code Example:**
interface Button {
  disabled: boolean;
}

function handleClick(this: Button) {
  this.disabled = true;
}

const btn: Button = { disabled: false };
// handleClick(); // Error: The 'this' context is missing.
handleClick.call(btn); // OK

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

