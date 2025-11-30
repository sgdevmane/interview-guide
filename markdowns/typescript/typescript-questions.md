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
10. [How do you define a React Component Prop type that accepts *either* an `image` URL *or* a `text` label, but not both?](#q10-how-do-you-define-a-react-component-prop-type-that-accepts-*either*-an-image-url-*or*-a-text-label-but-not-both) <span class="intermediate">Intermediate</span>
11. [How do you implement a generic 'Singleton' pattern in TypeScript using a static `getInstance` method?](#q11-how-do-you-implement-a-generic-singleton-pattern-in-typescript-using-a-static-getinstance-method) <span class="intermediate">Intermediate</span>
12. [How do you use the `infer` keyword to extract the type of the first argument of a function?](#q12-how-do-you-use-the-infer-keyword-to-extract-the-type-of-the-first-argument-of-a-function) <span class="intermediate">Intermediate</span>
13. [How do you fix the error 'Element implicitly has an any type because expression of type string can't be used to index type'?](#q13-how-do-you-fix-the-error-element-implicitly-has-an-any-type-because-expression-of-type-string-cant-be-used-to-index-type) <span class="intermediate">Intermediate</span>
14. [How do you declare a global variable (e.g., `window.myConfig`) so TypeScript recognizes it without errors?](#q14-how-do-you-declare-a-global-variable-eg-windowmyconfig-so-typescript-recognizes-it-without-errors) <span class="intermediate">Intermediate</span>
15. [How do you use TypeScript's `satisfies` operator to validate an expression matches a type without widening it?](#q15-how-do-you-use-typescripts-satisfies-operator-to-validate-an-expression-matches-a-type-without-widening-it) <span class="intermediate">Intermediate</span>
16. [How do you implement a `DeepPartial<T>` utility type?](#q16-how-do-you-implement-a-deeppartial<t>-utility-type) <span class="advanced">Advanced</span>
17. [How do you use `const` assertions (`as const`) to create literal types?](#q17-how-do-you-use-const-assertions-as-const-to-create-literal-types) <span class="intermediate">Intermediate</span>
18. [How do you use `Awaited<T>` to unwrap Promise types recursively?](#q18-how-do-you-use-awaited<t>-to-unwrap-promise-types-recursively) <span class="intermediate">Intermediate</span>
19. [How do you create a type that requires exactly one of two properties (XOR)?](#q19-how-do-you-create-a-type-that-requires-exactly-one-of-two-properties-xor) <span class="advanced">Advanced</span>
20. [How do you use `keyof` with Generics to access properties safely?](#q20-how-do-you-use-keyof-with-generics-to-access-properties-safely) <span class="intermediate">Intermediate</span>
21. [How do you implement a specialized `Pick` that filters by value type?](#q21-how-do-you-implement-a-specialized-pick-that-filters-by-value-type) <span class="advanced">Advanced</span>
22. [How do you use `asserts` to create a custom assertion function?](#q22-how-do-you-use-asserts-to-create-a-custom-assertion-function) <span class="intermediate">Intermediate</span>
23. [How do you use `ThisType<T>` to type `this` in object literals?](#q23-how-do-you-use-thistype<t>-to-type-this-in-object-literals) <span class="advanced">Advanced</span>
24. [How do you make a tuple type with a variable number of elements (Variadic Tuples)?](#q24-how-do-you-make-a-tuple-type-with-a-variable-number-of-elements-variadic-tuples) <span class="advanced">Advanced</span>
25. [How do you use `never` type for exhaustive checks in switch statements?](#q25-how-do-you-use-never-type-for-exhaustive-checks-in-switch-statements) <span class="intermediate">Intermediate</span>
26. [How do you use Module Augmentation to extend third-party libraries?](#q26-how-do-you-use-module-augmentation-to-extend-third-party-libraries) <span class="intermediate">Intermediate</span>
27. [How do you implement a generic `Mutable<T>` utility type?](#q27-how-do-you-implement-a-generic-mutable<t>-utility-type) <span class="intermediate">Intermediate</span>
28. [How do you use `Omit` to exclude properties from a type?](#q28-how-do-you-use-omit-to-exclude-properties-from-a-type) <span class="beginner">Beginner</span>
29. [How do you type a function with function overloads?](#q29-how-do-you-type-a-function-with-function-overloads) <span class="intermediate">Intermediate</span>
30. [How do you use the `instanceof` type guard?](#q30-how-do-you-use-the-instanceof-type-guard) <span class="beginner">Beginner</span>

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

