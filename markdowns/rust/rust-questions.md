# Rust Interview Questions

## Table of Contents

1. [Q1: What is Rust and what are its key features?](#q1-what-is-rust-and-what-are-its-key-features)
2. [Q2: Explain the concept of Ownership in Rust.](#q2-explain-the-concept-of-ownership-in-rust)
3. [Q3: What is Borrowing?](#q3-what-is-borrowing)
4. [Q4: What is the difference between `String` and `&str`?](#q4-what-is-the-difference-between-string-and-str)
5. [Q5: What are Lifetimes in Rust?](#q5-what-are-lifetimes-in-rust)
6. [Q6: Explain the `Option` and `Result` enums.](#q6-explain-the-option-and-result-enums)
7. [Q7: What is the difference between `unwrap()` and `expect()`?](#q7-what-is-the-difference-between-unwrap-and-expect)
8. [Q8: What are Traits?](#q8-what-are-traits)
9. [Q9: How does Rust handle concurrency?](#q9-how-does-rust-handle-concurrency)
10. [Q10: What is `unsafe` Rust?](#q10-what-is-unsafe-rust)
11. [Q11: What is the difference between `Copy` and `Clone`?](#q11-what-is-the-difference-between-copy-and-clone)
12. [Q12: Explain Smart Pointers (`Box`, `Rc`, `Arc`, `RefCell`).](#q12-explain-smart-pointers-box-rc-arc-refcell)
13. [Q13: How does Rust ensure memory safety without a Garbage Collector?](#q13-how-does-rust-ensure-memory-safety-without-a-garbage-collector)
14. [Q14: What is the purpose of the `mut` keyword?](#q14-what-is-the-purpose-of-the-mut-keyword)
15. [Q15: What are Closures in Rust?](#q15-what-are-closures-in-rust)
16. [Q16: What is Cargo?](#q16-what-is-cargo)
17. [Q17: Explain Pattern Matching with `match`.](#q17-explain-pattern-matching-with-match)
18. [Q18: What is the `impl` block used for?](#q18-what-is-the-impl-block-used-for)
19. [Q19: What is a Crate?](#q19-what-is-a-crate)
20. [Q20: What is the difference between `const` and `static`?](#q20-what-is-the-difference-between-const-and-static)
21. [Q21: What is the `?` operator?](#q21-what-is-the-operator)
22. [Q22: What is a module in Rust?](#q22-what-is-a-module-in-rust)
23. [Q23: Explain visibility modifiers (`pub`).](#q23-explain-visibility-modifiers-pub)
24. [Q24: What is the `use` keyword?](#q24-what-is-the-use-keyword)
25. [Q25: What is the `vec!` macro?](#q25-what-is-the-vec-macro)
26. [Q26: Difference between `String::from` and `.to_string()`.](#q26-difference-between-stringfrom-and-tostring)
27. [Q27: What is a Slice?](#q27-what-is-a-slice)
28. [Q28: How do `for` loops work with Iterators?](#q28-how-do-for-loops-work-with-iterators)
29. [Q29: What is the `collect()` method?](#q29-what-is-the-collect-method)
30. [Q30: What is the `derive` attribute?](#q30-what-is-the-derive-attribute)
31. [Q31: Difference between `Debug` and `Display` traits.](#q31-difference-between-debug-and-display-traits)
32. [Q32: Difference between `PartialEq` and `Eq`.](#q32-difference-between-partialeq-and-eq)
33. [Q33: What is the `Drop` trait?](#q33-what-is-the-drop-trait)
34. [Q34: Explain `From` and `Into` traits.](#q34-explain-from-and-into-traits)
35. [Q35: What are `AsRef` and `AsMut`?](#q35-what-are-asref-and-asmut)
36. [Q36: How do Generics work in Rust?](#q36-how-do-generics-work-in-rust)
37. [Q37: What are Trait Bounds?](#q37-what-are-trait-bounds)
38. [Q38: What is the `where` clause?](#q38-what-is-the-where-clause)
39. [Q39: Associated Types vs Generics.](#q39-associated-types-vs-generics)
40. [Q40: What is the `move` keyword in closures?](#q40-what-is-the-move-keyword-in-closures)
41. [Q41: Difference between `Fn`, `FnMut`, and `FnOnce`.](#q41-difference-between-fn-fnmut-and-fnonce)
42. [Q42: What are Iterator Adaptors?](#q42-what-are-iterator-adaptors)
43. [Q43: What are Consuming Adaptors?](#q43-what-are-consuming-adaptors)
44. [Q44: What are Trait Objects?](#q44-what-are-trait-objects)
45. [Q45: Static Dispatch vs Dynamic Dispatch.](#q45-static-dispatch-vs-dynamic-dispatch)
46. [Q46: What is Object Safety?](#q46-what-is-object-safety)
47. [Q47: What is the `Deref` trait?](#q47-what-is-the-deref-trait)
48. [Q48: What is Deref Coercion?](#q48-what-is-deref-coercion)
49. [Q49: What is `Cow` (Clone on Write)?](#q49-what-is-cow-clone-on-write)
50. [Q50: Detailed difference between `Rc` and `Arc`.](#q50-detailed-difference-between-rc-and-arc)
51. [Q51: `RefCell` vs `Mutex`.](#q51-refcell-vs-mutex)
52. [Q52: What is Interior Mutability?](#q52-what-is-interior-mutability)
53. [Q53: What is the `Cell` type?](#q53-what-is-the-cell-type)
54. [Q54: How do you handle Reference Cycles?](#q54-how-do-you-handle-reference-cycles)
55. [Q55: How to create Global Variables in Rust?](#q55-how-to-create-global-variables-in-rust)
56. [Q56: What are Macros in Rust?](#q56-what-are-macros-in-rust)
57. [Q57: What are Declarative Macros?](#q57-what-are-declarative-macros)
58. [Q58: What are Procedural Macros?](#q58-what-are-procedural-macros)
59. [Q59: What is a Custom Derive macro?](#q59-what-is-a-custom-derive-macro)
60. [Q60: What are Attribute-like macros?](#q60-what-are-attribute-like-macros)
61. [Q61: Explain Async/Await in Rust.](#q61-explain-asyncawait-in-rust)
62. [Q62: What is a Future?](#q62-what-is-a-future)
63. [Q63: What is the Tokio runtime?](#q63-what-is-the-tokio-runtime)
64. [Q64: What is an `async` block?](#q64-what-is-an-async-block)
65. [Q65: What does `.await` do?](#q65-what-does-await-do)
66. [Q66: What is Pinning (`Pin`)?](#q66-what-is-pinning-pin)
67. [Q67: What is the `Unpin` trait?](#q67-what-is-the-unpin-trait)
68. [Q68: `Send` vs `Sync` in depth.](#q68-send-vs-sync-in-depth)
69. [Q69: How does `std::thread::spawn` work?](#q69-how-does-stdthreadspawn-work)
70. [Q70: How do Channels (`mpsc`) work?](#q70-how-do-channels-mpsc-work)
71. [Q71: `Mutex` vs `RwLock`.](#q71-mutex-vs-rwlock)
72. [Q72: What are Atomics?](#q72-what-are-atomics)
73. [Q73: What is a `Condvar`?](#q73-what-is-a-condvar)
74. [Q74: What is FFI?](#q74-what-is-ffi)
75. [Q75: What is `extern "C"`?](#q75-what-is-extern-c)
76. [Q76: What is `#[no_mangle]`?](#q76-what-is-no_mangle)
77. [Q77: What are Raw Pointers?](#q77-what-are-raw-pointers)
78. [Q78: What is `mem::transmute`?](#q78-what-is-memtransmute)
79. [Q79: What is `MaybeUninit`?](#q79-what-is-maybeuninit)
80. [Q80: How do you write Unit Tests?](#q80-how-do-you-write-unit-tests)
81. [Q81: What are Integration Tests?](#q81-what-are-integration-tests)
82. [Q82: How do you benchmark Rust code?](#q82-how-do-you-benchmark-rust-code)
83. [Q83: Explain Documentation Comments.](#q83-explain-documentation-comments)
84. [Q84: What are Doc Tests?](#q84-what-are-doc-tests)
85. [Q85: What is `Cargo.toml` vs `Cargo.lock`?](#q85-what-is-cargotoml-vs-cargolock)
86. [Q86: Explain Semantic Versioning in Cargo.](#q86-explain-semantic-versioning-in-cargo)
87. [Q87: What are Cargo Workspaces?](#q87-what-are-cargo-workspaces)
88. [Q88: What is a Build Script (`build.rs`)?](#q88-what-is-a-build-script-buildrs)
89. [Q89: What is Cross-Compilation?](#q89-what-is-cross-compilation)
90. [Q90: What is `rustfmt`?](#q90-what-is-rustfmt)
91. [Q91: What is `clippy`?](#q91-what-is-clippy)
92. [Q92: `cargo check` vs `cargo build`.](#q92-cargo-check-vs-cargo-build)
93. [Q93: What is the Release Profile?](#q93-what-is-the-release-profile)
94. [Q94: Explain `HashMap` in Rust.](#q94-explain-hashmap-in-rust)
95. [Q95: What is `BTreeMap`?](#q95-what-is-btreemap)
96. [Q96: What is `HashSet`?](#q96-what-is-hashset)
97. [Q97: What is `VecDeque`?](#q97-what-is-vecdeque)
98. [Q98: What is `BinaryHeap`?](#q98-what-is-binaryheap)
99. [Q99: What is Type Inference in Rust?](#q99-what-is-type-inference-in-rust)
100. [Q100: What is the Never Type (`!`)?](#q100-what-is-the-never-type)

---

## Rust Fundamentals

### Q1: What is Rust and what are its key features?
**Difficulty: Easy**

**Answer:**
Rust is a systems programming language focused on safety, speed, and concurrency. It is designed to provide the performance of C/C++ but with memory safety guarantees.
**Key Features:**
- **Memory Safety:** Guaranteed at compile-time via ownership and borrowing (no segfaults).
- **No Garbage Collector:** Manages memory deterministically.
- **Concurrency:** "Fearless concurrency" prevents data races at compile time.
- **Zero-cost Abstractions:** High-level syntax with low-level performance.

### Q2: Explain the concept of Ownership in Rust.
**Difficulty: Medium**

**Answer:**
Ownership is Rust's most unique feature. It enables Rust to make memory safety guarantees without needing a garbage collector.
**Rules of Ownership:**
1.  Each value in Rust has a variable that's called its *owner*.
2.  There can only be one owner at a time.
3.  When the owner goes out of scope, the value will be dropped (freed).

### Q3: What is Borrowing?
**Difficulty: Medium**

**Answer:**
Borrowing allows you to access data without taking ownership of it. This is done via references (`&T` for immutable, `&mut T` for mutable).
**Rules of Borrowing:**
- At any given time, you can have either *one mutable reference* OR *any number of immutable references*.
- References must always be valid.

### Q4: What is the difference between `String` and `&str`?
**Difficulty: Easy**

**Answer:**
- **`String`:** A heap-allocated, growable, owned UTF-8 string. You have ownership of it and can modify it.
- **`&str` (String Slice):** An immutable reference to a string slice (a view into a string). It can point to a `String` in the heap or a string literal in the binary. It is often faster as it doesn't involve allocation.

### Q5: What are Lifetimes in Rust?
**Difficulty: Advanced**

**Answer:**
Lifetimes are a way for the Rust compiler to ensure that references are valid as long as they are needed. Every reference has a lifetime, which is the scope for which that reference is valid. Most of the time, lifetimes are inferred (lifetime elision), but sometimes you must annotate them explicitly (e.g., `'a`) to tell the compiler how the lifetimes of arguments and return values relate to each other.

```rust
// Example of lifetime annotation
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

### Q6: Explain the `Option` and `Result` enums.
**Difficulty: Easy**

**Answer:**
Rust does not have `null`. Instead, it uses enums to handle absence of value or errors.
- **`Option<T>`:** Represents a value that can be `Some(T)` or `None`.
- **`Result<T, E>`:** Used for error handling. It can be `Ok(T)` (success) or `Err(E)` (failure).

### Q7: What is the difference between `unwrap()` and `expect()`?
**Difficulty: Easy**

**Answer:**
Both are used to extract the value from an `Option` or `Result`. If the value is `None` or `Err`, both will panic (crash the program).
- **`unwrap()`:** Panics with a generic message.
- **`expect("msg")`:** Panics with a custom message provided by the developer, making debugging easier.

### Q8: What are Traits?
**Difficulty: Medium**

**Answer:**
Traits are similar to interfaces in other languages. They define shared behavior that types can implement. A trait tells the Rust compiler about functionality a particular type has and can share with other types.
*Example:* `Display`, `Debug`, `Clone`, `Copy`.

### Q9: How does Rust handle concurrency?
**Difficulty: Advanced**

**Answer:**
Rust leverages its ownership and type system to ensure thread safety.
- **`Send` Trait:** Indicates that ownership of values of the type can be transferred to another thread.
- **`Sync` Trait:** Indicates that it is safe for the type to be referenced from multiple threads.
- **Mutex:** `std::sync::Mutex` allows safe mutable access across threads.
- **Arc:** `std::sync::Arc` (Atomic Reference Counting) allows shared ownership across threads.
The compiler prevents data races by ensuring you cannot have multiple mutable references to the same data across threads without synchronization.

### Q10: What is `unsafe` Rust?
**Difficulty: Advanced**

**Answer:**
`unsafe` is a keyword that allows you to bypass certain safety checks of the Rust compiler. Inside an `unsafe` block, you can:
- Dereference raw pointers.
- Call unsafe functions or methods (like C FFI).
- Access or modify mutable static variables.
- Implement unsafe traits.
It is used when the developer guarantees safety that the compiler cannot verify automatically (e.g., low-level system programming).

### Q11: What is the difference between `Copy` and `Clone`?
**Difficulty: Medium**

**Answer:**
- **`Copy`:** Implicit, inexpensive bit-wise copy. Happens automatically for simple types (integers, floats, bools) when passed to functions or assigned. Types must implement the `Copy` trait.
- **`Clone`:** Explicit, potentially expensive copy. Must be called manually (`.clone()`). Used for types that manage resources (like `String` or `Vec`) where a deep copy is needed.

### Q12: Explain Smart Pointers (`Box`, `Rc`, `Arc`, `RefCell`).
**Difficulty: Advanced**

**Answer:**
- **`Box<T>`:** Allocates data on the heap. Simplest smart pointer.
- **`Rc<T>` (Reference Counted):** Enables multiple ownership of data for single-threaded scenarios.
- **`Arc<T>` (Atomic Reference Counted):** Thread-safe version of `Rc`.
- **`RefCell<T>`:** Enforces borrowing rules at *runtime* instead of compile-time. Allows "interior mutability" (mutating data even when there are immutable references to it).

### Q13: How does Rust ensure memory safety without a Garbage Collector?
**Difficulty: Medium**

**Answer:**
Through the **Ownership** system (Ownership, Borrowing, Lifetimes). The compiler inserts calls to `drop()` (which frees memory) automatically at the exact point where a variable goes out of scope. This deterministic cleanup avoids the need for a runtime GC.

### Q14: What is the purpose of the `mut` keyword?
**Difficulty: Easy**

**Answer:**
Variables in Rust are immutable by default. The `mut` keyword is used to make a variable mutable, allowing its value to be changed.

### Q15: What are Closures in Rust?
**Difficulty: Medium**

**Answer:**
Closures are anonymous functions that can capture values from their enclosing environment.
```rust
let x = 4;
let equal_to_x = |z| z == x; // Captures x
```

### Q16: What is Cargo?
**Difficulty: Easy**

**Answer:**
Cargo is Rust's package manager and build system. It handles:
- Building the project (`cargo build`).
- Downloading and managing dependencies (crates).
- Running tests (`cargo test`).
- Generating documentation (`cargo doc`).

### Q17: Explain Pattern Matching with `match`.
**Difficulty: Easy**

**Answer:**
`match` allows you to compare a value against a series of patterns and execute code based on which pattern matches. It is exhaustive, meaning you must handle all possible cases.
```rust
match number {
    1 => println!("One"),
    2 => println!("Two"),
    _ => println!("Something else"),
}
```

### Q18: What is the `impl` block used for?
**Difficulty: Easy**

**Answer:**
The `impl` block is used to define methods and associated functions for a struct or an enum. It is also used to implement a Trait for a type.

### Q19: What is a Crate?
**Difficulty: Easy**

**Answer:**
A crate is the smallest amount of code that the Rust compiler considers at a time.
- **Binary Crate:** Compiles to an executable (has a `main` function).
- **Library Crate:** Compiles to a library to be used by other projects.

### Q20: What is the difference between `const` and `static`?
**Difficulty: Medium**

**Answer:**
- **`const`:** Values are inlined to each place they are used. They have no fixed memory address.
- **`static`:** Has a fixed memory address. All references to it point to the same address. Global variables are usually `static`.

### Q21: What is the `?` operator?
**Difficulty: Medium**

**Answer:**
The `?` operator is a shorthand for propagating errors. It can be placed after a `Result` or `Option` value. If the value is `Err` (or `None`), the function returns immediately with that error/none. If it is `Ok` (or `Some`), it unwraps the value and continues.

### Q22: What is a module in Rust?
**Difficulty: Easy**

**Answer:**
Modules organize code within a crate into groups for readability and easy reuse. They control the scope and privacy of items. Defined using the `mod` keyword.

### Q23: Explain visibility modifiers (`pub`).
**Difficulty: Easy**

**Answer:**
By default, everything in Rust is private (only accessible within the current module). The `pub` keyword makes an item public.
- `pub`: Publicly accessible.
- `pub(crate)`: Visible anywhere within the current crate.
- `pub(super)`: Visible in the parent module.

### Q24: What is the `use` keyword?
**Difficulty: Easy**

**Answer:**
The `use` keyword brings paths into scope, so you can call items by shorter names (e.g., `use std::io;` allows `io::stdin()` instead of `std::io::stdin()`).

### Q25: What is the `vec!` macro?
**Difficulty: Easy**

**Answer:**
`vec!` is a macro used to create a `Vec<T>` (Vector) conveniently with initial values.
```rust
let v = vec![1, 2, 3];
```

### Q26: Difference between `String::from` and `.to_string()`.
**Difficulty: Easy**

**Answer:**
Functionally they are very similar for creating a `String` from a string literal. `String::from` implements `From` trait, while `.to_string()` comes from the `ToString` (via `Display`) trait. In modern Rust, both are efficient.

### Q27: What is a Slice?
**Difficulty: Easy**

**Answer:**
A slice is a reference to a contiguous sequence of elements in a collection rather than the whole collection. Written as `&[T]`. String slices (`&str`) are slices of bytes containing UTF-8 text.

### Q28: How do `for` loops work with Iterators?
**Difficulty: Medium**

**Answer:**
In Rust, `for` loops work by converting a collection into an iterator using the `IntoIterator` trait. The loop consumes elements from the iterator until it returns `None`.

### Q29: What is the `collect()` method?
**Difficulty: Medium**

**Answer:**
`collect()` is a powerful consumer method that transforms an iterator into a collection (like `Vec`, `String`, `HashMap`). You often need to specify the type because `collect` can produce many different collections.
```rust
let v: Vec<i32> = (0..5).collect();
```

### Q30: What is the `derive` attribute?
**Difficulty: Medium**

**Answer:**
`#[derive(...)]` automatically implements certain traits for your struct or enum using procedural macros. Common traits: `Debug`, `Clone`, `Copy`, `PartialEq`.

### Q31: Difference between `Debug` and `Display` traits.
**Difficulty: Medium**

**Answer:**
- **`Display`:** Intended for user-facing output. Uses `{}`. Not implemented automatically.
- **`Debug`:** Intended for programmer debugging. Uses `{:?}`. Can be derived automatically via `#[derive(Debug)]`.

### Q32: Difference between `PartialEq` and `Eq`.
**Difficulty: Advanced**

**Answer:**
- **`PartialEq`:** Allows comparison (`==`, `!=`).
- **`Eq`:** implies reflexivity (`a == a`). Floating point numbers (`f32`, `f64`) implement `PartialEq` but NOT `Eq` because `NaN != NaN`.

### Q33: What is the `Drop` trait?
**Difficulty: Medium**

**Answer:**
The `Drop` trait allows you to customize what happens when a value goes out of scope (destructor). You can implement `drop` to release resources (files, network connections).

### Q34: Explain `From` and `Into` traits.
**Difficulty: Medium**

**Answer:**
They are used for type conversions. `From` converts *from* another type to this type. `Into` is the reciprocal; if you implement `From`, you get `Into` for free.

### Q35: What are `AsRef` and `AsMut`?
**Difficulty: Advanced**

**Answer:**
Traits for cheap reference-to-reference conversions. Used in generic functions to accept any type that can be viewed as a reference to a type (e.g., accepting `String` or `&str` as `&str`).

### Q36: How do Generics work in Rust?
**Difficulty: Medium**

**Answer:**
Generics allow you to write code that works with multiple types. Rust compiles generics using *monomorphization*, meaning it generates specific code for each concrete type used at compile time, resulting in no runtime overhead.

### Q37: What are Trait Bounds?
**Difficulty: Medium**

**Answer:**
Trait bounds specify that a generic type must implement certain traits.
```rust
fn print_it<T: Display>(t: T) { println!("{}", t); }
```

### Q38: What is the `where` clause?
**Difficulty: Medium**

**Answer:**
A `where` clause allows you to specify trait bounds separately from the generic type parameters, making complex function signatures cleaner.

### Q39: Associated Types vs Generics.
**Difficulty: Advanced**

**Answer:**
- **Generics:** The caller specifies the type.
- **Associated Types:** The implementor specifies the type. Used in traits (like `Iterator::Item`) where the type logically belongs to the implementation.

### Q40: What is the `move` keyword in closures?
**Difficulty: Medium**

**Answer:**
`move` forces the closure to take ownership of the values it captures from the environment, rather than borrowing them.

### Q41: Difference between `Fn`, `FnMut`, and `FnOnce`.
**Difficulty: Advanced**

**Answer:**
- **`Fn`:** Captures immutably. Can be called multiple times.
- **`FnMut`:** Captures mutably. Can be called multiple times.
- **`FnOnce`:** Captures by ownership. Can be called only once (consumes the closure).

### Q42: What are Iterator Adaptors?
**Difficulty: Medium**

**Answer:**
Methods that take an iterator and produce another iterator (lazy). Examples: `map`, `filter`, `zip`, `enumerate`.

### Q43: What are Consuming Adaptors?
**Difficulty: Medium**

**Answer:**
Methods that call `next` on the iterator and use up the elements to produce a final value. Examples: `sum`, `collect`, `for_each`.

### Q44: What are Trait Objects?
**Difficulty: Advanced**

**Answer:**
Trait objects allow for dynamic dispatch. Using `&dyn Trait` or `Box<dyn Trait>`, you can store different types that implement the same trait in a single collection. It has a runtime cost.

### Q45: Static Dispatch vs Dynamic Dispatch.
**Difficulty: Advanced**

**Answer:**
- **Static:** Generics. Resolved at compile time. Faster. Larger binary size.
- **Dynamic:** Trait Objects. Resolved at runtime (vtable). Slower. Smaller binary size.

### Q46: What is Object Safety?
**Difficulty: Advanced**

**Answer:**
Not all traits can be made into trait objects. A trait is object-safe if:
- The return type isn't `Self`.
- There are no generic type parameters.

### Q47: What is the `Deref` trait?
**Difficulty: Advanced**

**Answer:**
`Deref` allows you to customize the behavior of the dereference operator `*`. It allows smart pointers to behave like regular references.

### Q48: What is Deref Coercion?
**Difficulty: Advanced**

**Answer:**
Rust automatically converts a reference to a type that implements `Deref` into a reference to the target type (e.g., `&String` -> `&str`, `&Vec<T>` -> `&[T]`).

### Q49: What is `Cow` (Clone on Write)?
**Difficulty: Advanced**

**Answer:**
`std::borrow::Cow` is a smart pointer enum that can hold either borrowed data or owned data. It clones the data only when mutation is necessary.

### Q50: Detailed difference between `Rc` and `Arc`.
**Difficulty: Advanced**

**Answer:**
Both are reference counting pointers. `Rc` is faster but not thread-safe (uses non-atomic counters). `Arc` uses atomic counters, making it thread-safe but slightly slower.

### Q51: `RefCell` vs `Mutex`.
**Difficulty: Advanced**

**Answer:**
- **`RefCell`:** Interior mutability for single-threaded scenarios. Panics at runtime if borrowing rules are violated.
- **`Mutex`:** Interior mutability for multi-threaded scenarios. Blocks threads waiting for the lock.

### Q52: What is Interior Mutability?
**Difficulty: Advanced**

**Answer:**
A design pattern in Rust that allows you to mutate data even when there are immutable references to that data. Used by `RefCell`, `Mutex`, `Cell`.

### Q53: What is the `Cell` type?
**Difficulty: Advanced**

**Answer:**
A wrapper for `Copy` types that provides interior mutability by moving values in and out, rather than giving references (like `RefCell`).

### Q54: How do you handle Reference Cycles?
**Difficulty: Advanced**

**Answer:**
Reference cycles (memory leaks) can occur with `Rc`/`Arc`. You break them using `Weak` pointers (`Rc::downgrade`). `Weak` pointers don't keep the value alive.

### Q55: How to create Global Variables in Rust?
**Difficulty: Medium**

**Answer:**
- `const`: Inlined.
- `static`: Fixed address.
- `static mut`: Unsafe.
- `lazy_static` / `once_cell`: Thread-safe, lazily initialized globals.

### Q56: What are Macros in Rust?
**Difficulty: Medium**

**Answer:**
Macros are code that writes other code (metaprogramming). They are expanded at compile time.

### Q57: What are Declarative Macros?
**Difficulty: Medium**

**Answer:**
Defined using `macro_rules!`. They use pattern matching to replace code. `vec!` and `println!` are declarative macros.

### Q58: What are Procedural Macros?
**Difficulty: Advanced**

**Answer:**
Functions that accept code as input (TokenStream) and produce code as output. More powerful than declarative macros. Three types: Custom Derive, Attribute-like, Function-like.

### Q59: What is a Custom Derive macro?
**Difficulty: Advanced**

**Answer:**
Allows you to define new inputs for the `derive` attribute (e.g., `#[derive(MyTrait)]`).

### Q60: What are Attribute-like macros?
**Difficulty: Advanced**

**Answer:**
Macros that define new custom attributes attached to items (e.g., `#[route(GET, "/")]`).

### Q61: Explain Async/Await in Rust.
**Difficulty: Advanced**

**Answer:**
Rust's async/await syntax looks like synchronous code but runs asynchronously. It transforms functions into state machines that implement the `Future` trait.

### Q62: What is a Future?
**Difficulty: Advanced**

**Answer:**
A trait representing a value that might not be available yet. It has a `poll` method that the runtime calls to drive the computation forward.

### Q63: What is the Tokio runtime?
**Difficulty: Advanced**

**Answer:**
Rust's standard library does not include an async runtime. Tokio is the most popular third-party runtime that provides the event loop, I/O, and timer facilities to execute async code.

### Q64: What is an `async` block?
**Difficulty: Advanced**

**Answer:**
A block of code `async { ... }` that returns a Future.

### Q65: What does `.await` do?
**Difficulty: Advanced**

**Answer:**
It yields control back to the executor (runtime) if the Future is not ready, allowing other tasks to run. When the Future is ready, it resumes execution.

### Q66: What is Pinning (`Pin`)?
**Difficulty: Advanced**

**Answer:**
`Pin<P>` wraps a pointer to prevent the value it points to from moving in memory. This is critical for self-referential structs, which are common in generated Futures.

### Q67: What is the `Unpin` trait?
**Difficulty: Advanced**

**Answer:**
A marker trait that says a type *can* be safely moved even when pinned. Most types are `Unpin`. Futures generated by async/await are `!Unpin`.

### Q68: `Send` vs `Sync` in depth.
**Difficulty: Advanced**

**Answer:**
- `T` is `Send` if it's safe to move `T` to another thread.
- `T` is `Sync` if it's safe to share `&T` between threads (i.e., `&T` is `Send`).

### Q69: How does `std::thread::spawn` work?
**Difficulty: Medium**

**Answer:**
It creates a new OS thread. It takes a closure. The closure must capture values with `move` if they are needed inside the thread.

### Q70: How do Channels (`mpsc`) work?
**Difficulty: Medium**

**Answer:**
`mpsc` stands for "Multi-Producer, Single-Consumer". It provides a way to send messages between threads.

### Q71: `Mutex` vs `RwLock`.
**Difficulty: Medium**

**Answer:**
- `Mutex`: Only one thread can access data at a time (read or write).
- `RwLock`: Multiple readers allowed, or one writer. Better for read-heavy workloads.

### Q72: What are Atomics?
**Difficulty: Advanced**

**Answer:**
Primitives (like `AtomicBool`, `AtomicI32`) that provide thread-safe access to simple data without locks, using hardware instructions.

### Q73: What is a `Condvar`?
**Difficulty: Advanced**

**Answer:**
Condition Variable. It blocks a thread until notified by another thread. Used with a `Mutex` to wait for a specific condition.

### Q74: What is FFI?
**Difficulty: Advanced**

**Answer:**
Foreign Function Interface. Allows Rust to call functions written in other languages (like C) and vice versa.

### Q75: What is `extern "C"`?
**Difficulty: Advanced**

**Answer:**
It specifies the C ABI (Application Binary Interface) for a function, making it compatible with C code.

### Q76: What is `#[no_mangle]`?
**Difficulty: Advanced**

**Answer:**
It tells the compiler not to change the name of the function during compilation, so it can be linked by name from other languages.

### Q77: What are Raw Pointers?
**Difficulty: Advanced**

**Answer:**
`*const T` and `*mut T`. Similar to C pointers. No safety guarantees. Must be dereferenced inside `unsafe`.

### Q78: What is `mem::transmute`?
**Difficulty: Advanced**

**Answer:**
An unsafe function that reinterprets the bits of a value of one type as another type. Extremely dangerous.

### Q79: What is `MaybeUninit`?
**Difficulty: Advanced**

**Answer:**
A type used to handle uninitialized memory safely, typically when interacting with foreign code or optimizing arrays.

### Q80: How do you write Unit Tests?
**Difficulty: Easy**

**Answer:**
Put them in the same file as the code, inside a module annotated with `#[cfg(test)]`. Use `#[test]` attribute on functions.

### Q81: What are Integration Tests?
**Difficulty: Medium**

**Answer:**
Tests placed in the `tests/` directory at the crate root. They treat the crate as an external library.

### Q82: How do you benchmark Rust code?
**Difficulty: Advanced**

**Answer:**
Using the `test` crate (unstable) with `#[bench]`, or using stable tools like `criterion`.

### Q83: Explain Documentation Comments.
**Difficulty: Easy**

**Answer:**
- `///`: Documents the item following it. Supports Markdown.
- `//!`: Documents the containing module/crate.

### Q84: What are Doc Tests?
**Difficulty: Medium**

**Answer:**
Code blocks inside documentation comments are automatically compiled and run as tests by `cargo test`.

### Q85: What is `Cargo.toml` vs `Cargo.lock`?
**Difficulty: Easy**

**Answer:**
- `Cargo.toml`: Manifest file where you declare dependencies and version ranges.
- `Cargo.lock`: Auto-generated file that locks exact versions of dependencies for reproducible builds.

### Q86: Explain Semantic Versioning in Cargo.
**Difficulty: Medium**

**Answer:**
Cargo assumes dependencies follow SemVer. `^1.2.3` allows updates to `1.3.0` but not `2.0.0`.

### Q87: What are Cargo Workspaces?
**Difficulty: Medium**

**Answer:**
A feature to manage multiple related packages in the same repository, sharing a single `Cargo.lock` and output directory.

### Q88: What is a Build Script (`build.rs`)?
**Difficulty: Advanced**

**Answer:**
A Rust script that runs before the package is built. Used for compiling C code, generating code, or detecting system configuration.

### Q89: What is Cross-Compilation?
**Difficulty: Medium**

**Answer:**
Compiling code on one platform (host) to run on another platform (target). Rust makes this easy via `rustup target add`.

### Q90: What is `rustfmt`?
**Difficulty: Easy**

**Answer:**
The official tool for formatting Rust code according to style guidelines.

### Q91: What is `clippy`?
**Difficulty: Easy**

**Answer:**
A collection of lints to catch common mistakes and improve your Rust code (a linter).

### Q92: `cargo check` vs `cargo build`.
**Difficulty: Easy**

**Answer:**
- `check`: Compiles code but skips code generation (faster). Checks for errors.
- `build`: Compiles and produces the binary/library.

### Q93: What is the Release Profile?
**Difficulty: Easy**

**Answer:**
`cargo build --release`. Optimizes the code (slower compile, faster execution). Removes debug assertions.

### Q94: Explain `HashMap` in Rust.
**Difficulty: Medium**

**Answer:**
A hash map implementation (`std::collections::HashMap`). Keys must implement `Eq` and `Hash`. Uses SipHash by default (DOS resistant).

### Q95: What is `BTreeMap`?
**Difficulty: Medium**

**Answer:**
A map based on a B-Tree. Keys are sorted. Keys must implement `Ord`.

### Q96: What is `HashSet`?
**Difficulty: Medium**

**Answer:**
A set implementation using a hash map internally. Stores unique values.

### Q97: What is `VecDeque`?
**Difficulty: Medium**

**Answer:**
A double-ended queue implemented with a growable ring buffer. Efficient push/pop at both ends.

### Q98: What is `BinaryHeap`?
**Difficulty: Medium**

**Answer:**
A priority queue implemented with a binary heap. Pops the maximum element.

### Q99: What is Type Inference in Rust?
**Difficulty: Easy**

**Answer:**
The compiler can usually deduce the type of variables, so you don't need to write explicit types everywhere. `let x = 5;` (x is inferred as i32).

### Q100: What is the Never Type (`!`)?
**Difficulty: Advanced**

**Answer:**
The never type `!` represents the type of computations which will never resolve to any value at all. For example, the `exit` function `fn exit(code: i32) -> !` returns the never type. `!` can be coerced into any other type. This is useful in `match` arms:
```rust
let x: i32 = match input {
    Ok(v) => v,
    Err(_) => panic!("Error!"), // panic! returns !, so this is valid
};
```
