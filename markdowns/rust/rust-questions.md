<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/rust-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>Rust Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for developers</b></p>
</div>

---

## Table of Contents

1. [How do you handle errors without using exceptions?](#q1-how-do-you-handle-errors-without-using-exceptions) <span class="beginner">Beginner</span>
2. [How do you share data between threads safely?](#q2-how-do-you-share-data-between-threads-safely) <span class="intermediate">Intermediate</span>
3. [How do you prevent 'use after free' errors?](#q3-how-do-you-prevent-use-after-free-errors) <span class="beginner">Beginner</span>
4. [How do you implement polymorphism in Rust?](#q4-how-do-you-implement-polymorphism-in-rust) <span class="intermediate">Intermediate</span>
5. [How do you manage memory without a Garbage Collector?](#q5-how-do-you-manage-memory-without-a-garbage-collector) <span class="intermediate">Intermediate</span>
6. [How do you modify a variable inside a closure?](#q6-how-do-you-modify-a-variable-inside-a-closure) <span class="intermediate">Intermediate</span>
7. [How do you handle global state?](#q7-how-do-you-handle-global-state) <span class="advanced">Advanced</span>
8. [How do you optimize string concatenation?](#q8-how-do-you-optimize-string-concatenation) <span class="intermediate">Intermediate</span>
9. [How do you return multiple values from a function?](#q9-how-do-you-return-multiple-values-from-a-function) <span class="beginner">Beginner</span>
10. [How do you create a custom error type?](#q10-how-do-you-create-a-custom-error-type) <span class="intermediate">Intermediate</span>
11. [How do you iterate over a collection without consuming it?](#q11-how-do-you-iterate-over-a-collection-without-consuming-it) <span class="beginner">Beginner</span>
12. [How do you implement an asynchronous function?](#q12-how-do-you-implement-an-asynchronous-function) <span class="intermediate">Intermediate</span>
13. [How do you create a macro to reduce boilerplate?](#q13-how-do-you-create-a-macro-to-reduce-boilerplate) <span class="advanced">Advanced</span>
14. [How do you reference a slice of an array?](#q14-how-do-you-reference-a-slice-of-an-array) <span class="beginner">Beginner</span>
15. [How do you use unsafe code for performance?](#q15-how-do-you-use-unsafe-code-for-performance) <span class="advanced">Advanced</span>
16. [How do you use Option and Result combinators?](#q16-how-do-you-use-option-and-result-combinators) <span class="intermediate">Intermediate</span>
17. [When should you use Box<T>?](#q17-when-should-you-use-boxt) <span class="intermediate">Intermediate</span>
18. [What is the difference between RefCell and Cell?](#q18-what-is-the-difference-between-refcell-and-cell) <span class="advanced">Advanced</span>
19. [When to use Arc vs Rc?](#q19-when-to-use-arc-vs-rc) <span class="intermediate">Intermediate</span>
20. [How do you implement From and Into traits?](#q20-how-do-you-implement-from-and-into-traits) <span class="intermediate">Intermediate</span>
21. [How does Deref coercion work?](#q21-how-does-deref-coercion-work) <span class="advanced">Advanced</span>
22. [How do you swap values efficiently?](#q22-how-do-you-swap-values-efficiently) <span class="intermediate">Intermediate</span>
23. [What is Cow (Copy-on-Write)?](#q23-what-is-cow-copy-on-write) <span class="advanced">Advanced</span>
24. [When should you use PhantomData?](#q24-when-should-you-use-phantomdata) <span class="advanced">Advanced</span>
25. [How do you write unit tests in Rust?](#q25-how-do-you-write-unit-tests-in-rust) <span class="beginner">Beginner</span>
26. [How do you use the Entry API for HashMaps?](#q26-how-do-you-use-the-entry-api-for-hashmaps) <span class="intermediate">Intermediate</span>
27. [What is the difference between const and static?](#q27-what-is-the-difference-between-const-and-static) <span class="intermediate">Intermediate</span>
28. [How do you use match guards?](#q28-how-do-you-use-match-guards) <span class="beginner">Beginner</span>
29. [How do you create a thread-safe global counter?](#q29-how-do-you-create-a-thread-safe-global-counter) <span class="intermediate">Intermediate</span>
30. [How do you handle results with the ? operator?](#q30-how-do-you-handle-results-with-the--operator) <span class="beginner">Beginner</span>
31. [How do you implement the `Iterator` trait for a custom type?](#q31-how-do-you-implement-the-iterator-trait-for-a-custom-type) <span class="intermediate">Intermediate</span>
32. [How do you handle errors using `thiserror`?](#q32-how-do-you-handle-errors-using-thiserror) <span class="intermediate">Intermediate</span>
33. [How do you use `serde` for JSON serialization?](#q33-how-do-you-use-serde-for-json-serialization) <span class="beginner">Beginner</span>
34. [How do you use `tokio` for async execution?](#q34-how-do-you-use-tokio-for-async-execution) <span class="intermediate">Intermediate</span>
35. [How do you use `Weak` pointers to prevent reference cycles?](#q35-how-do-you-use-weak-pointers-to-prevent-reference-cycles) <span class="advanced">Advanced</span>
36. [How do you create a declarative macro?](#q36-how-do-you-create-a-declarative-macro) <span class="advanced">Advanced</span>
37. [How do you call C code from Rust (FFI)?](#q37-how-do-you-call-c-code-from-rust-ffi) <span class="advanced">Advanced</span>
38. [How do you implement a Builder Pattern?](#q38-how-do-you-implement-a-builder-pattern) <span class="intermediate">Intermediate</span>
39. [How do you use `std::sync::mpsc` for message passing?](#q39-how-do-you-use-stdsyncmpsc-for-message-passing) <span class="intermediate">Intermediate</span>
40. [How do you write documentation comments?](#q40-how-do-you-write-documentation-comments) <span class="beginner">Beginner</span>
41. [How do you use `Cow` (Copy-on-Write) efficiently?](#q41-how-do-you-use-cow-copy-on-write-efficiently) <span class="advanced">Advanced</span>
42. [How do you implement the `Default` trait?](#q42-how-do-you-implement-the-default-trait) <span class="beginner">Beginner</span>
43. [How do you use `Any` trait for dynamic typing?](#q43-how-do-you-use-any-trait-for-dynamic-typing) <span class="expert">Expert</span>
44. [How do you use `lazy_static` or `OnceLock` (std)?](#q44-how-do-you-use-lazy_static-or-oncelock-std) <span class="intermediate">Intermediate</span>
45. [How do you optimize memory layout with `#[repr(C)]` or `#[repr(packed)]`?](#q45-how-do-you-optimize-memory-layout-with-reprc-or-reprpacked) <span class="advanced">Advanced</span>
46. [How do you use `Pin` to handle self-referential structs?](#q46-how-do-you-use-pin-to-handle-self-referential-structs) <span class="expert">Expert</span>
47. [How do you use `std::collections::BTreeMap` vs `HashMap`?](#q47-how-do-you-use-stdcollectionsbtreemap-vs-hashmap) <span class="intermediate">Intermediate</span>
48. [How do you implement a custom Drop trait?](#q48-how-do-you-implement-a-custom-drop-trait) <span class="beginner">Beginner</span>
49. [How do you use `rayon` for data parallelism?](#q49-how-do-you-use-rayon-for-data-parallelism) <span class="intermediate">Intermediate</span>
50. [How do you use `std::process::Command` to run external programs?](#q50-how-do-you-use-stdprocesscommand-to-run-external-programs) <span class="beginner">Beginner</span>

---

### Q1: How do you handle errors without using exceptions?

**Difficulty**: Beginner

**Strategy:**
Use the `Result<T, E>` enum for recoverable errors and `Option<T>` for optional values. Use pattern matching (`match`) or helper methods like `.unwrap_or()`, `?` operator.

**Code Example:**
```rust
fn divide(a: f64, b: f64) -> Result<f64, String> {
    if b == 0.0 {
        Err("Division by zero".to_string())
    } else {
        Ok(a / b)
    }
}

fn main() {
    match divide(10.0, 2.0) {
        Ok(val) => println!("Result: {}", val),
        Err(e) => println!("Error: {}", e),
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q2: How do you share data between threads safely?

**Difficulty**: Intermediate

**Strategy:**
Use `Arc` (Atomic Reference Counting) for shared ownership and `Mutex` (Mutual Exclusion) or `RwLock` for synchronization.

**Code Example:**
```rust
use std::sync::{Arc, Mutex};
use std::thread;

let counter = Arc::new(Mutex::new(0));
let mut handles = vec![];

for _ in 0..10 {
    let counter = Arc::clone(&counter);
    let handle = thread::spawn(move || {
        let mut num = counter.lock().unwrap();
        *num += 1;
    });
    handles.push(handle);
}

for handle in handles {
    handle.join().unwrap();
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q3: How do you prevent 'use after free' errors?

**Difficulty**: Beginner

**Strategy:**
Rust's **Ownership** system prevents this at compile time. When a value is moved to another variable, the original variable becomes invalid.

**Code Example:**
```rust
let s1 = String::from("hello");
let s2 = s1; // Move occurs here

// println!("{}", s1); // Compile error: value used after move
println!("{}", s2); // Valid
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q4: How do you implement polymorphism in Rust?

**Difficulty**: Intermediate

**Strategy:**
Use **Traits**. Define a trait with methods and implement it for different structs. Use `Box<dyn Trait>` for dynamic dispatch or generics `T: Trait` for static dispatch.

**Code Example:**
```rust
trait Speak {
    fn say(&self);
}

struct Dog;
impl Speak for Dog {
    fn say(&self) { println!("Woof"); }
}

fn make_it_speak(animal: &impl Speak) {
    animal.say();
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q5: How do you manage memory without a Garbage Collector?

**Difficulty**: Intermediate

**Strategy:**
Rust uses **RAII** (Resource Acquisition Is Initialization). Memory is automatically freed when the owner goes out of scope (`drop` is called).

**Code Example:**
```rust
{
    let s = String::from("hello"); // Allocation
    // use s
} // s goes out of scope, memory freed automatically
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q6: How do you modify a variable inside a closure?

**Difficulty**: Intermediate

**Strategy:**
Use a `FnMut` closure and declare the variable as `mut`. The closure must capture the variable by mutable reference.

**Code Example:**
```rust
let mut count = 0;
let mut increment = || {
    count += 1;
    println!("Count: {}", count);
};

increment();
increment();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q7: How do you handle global state?

**Difficulty**: Advanced

**Strategy:**
Use `lazy_static!` or `std::sync::OnceLock` (Rust 1.70+) to create thread-safe singletons.

**Code Example:**
```rust
use std::sync::OnceLock;
use std::sync::Mutex;

static GLOBAL_DATA: OnceLock<Mutex<Vec<i32>>> = OnceLock::new();

fn main() {
    let data = GLOBAL_DATA.get_or_init(|| Mutex::new(vec![]));
    data.lock().unwrap().push(1);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q8: How do you optimize string concatenation?

**Difficulty**: Intermediate

**Strategy:**
Use a `String` buffer and `push_str` or `format!` macro. Avoid repeated `+` operations which can create intermediate allocations.

**Code Example:**
```rust
let mut s = String::with_capacity(10); // Pre-allocate
s.push_str("Hello");
s.push(' ');
s.push_str("World");
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q9: How do you return multiple values from a function?

**Difficulty**: Beginner

**Strategy:**
Return a **Tuple**.

**Code Example:**
```rust
fn calculate(a: i32, b: i32) -> (i32, i32) {
    (a + b, a * b)
}

let (sum, product) = calculate(2, 3);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q10: How do you create a custom error type?

**Difficulty**: Intermediate

**Strategy:**
Implement the `std::fmt::Display` and `std::fmt::Debug` traits (and optionally `std::error::Error`). Using the `thiserror` crate simplifies this.

**Code Example:**
```rust
use std::fmt;

#[derive(Debug)]
struct MyError;

impl fmt::Display for MyError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "Something went wrong")
    }
}

impl std::error::Error for MyError {}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q11: How do you iterate over a collection without consuming it?

**Difficulty**: Beginner

**Strategy:**
Use `.iter()` to borrow items immutably. `.into_iter()` consumes the collection (moves items).

**Code Example:**
```rust
let nums = vec![1, 2, 3];
for num in nums.iter() {
    println!("{}", num);
}
// nums is still valid here
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q12: How do you implement an asynchronous function?

**Difficulty**: Intermediate

**Strategy:**
Use `async fn` and an async runtime like **Tokio**. Call `.await` on futures.

**Code Example:**
```rust
async fn fetch_data() -> u32 {
    100
}

#[tokio::main]
async fn main() {
    let value = fetch_data().await;
    println!("{}", value);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q13: How do you create a macro to reduce boilerplate?

**Difficulty**: Advanced

**Strategy:**
Use `macro_rules!` for declarative macros.

**Code Example:**
```rust
macro_rules! say_hello {
    () => {
        println!("Hello!");
    };
}

say_hello!();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q14: How do you reference a slice of an array?

**Difficulty**: Beginner

**Strategy:**
Use the range syntax `&array[start..end]`.

**Code Example:**
```rust
let arr = [1, 2, 3, 4, 5];
let slice = &arr[1..4]; // [2, 3, 4]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q15: How do you use unsafe code for performance?

**Difficulty**: Advanced

**Strategy:**
Wrap code in an `unsafe` block. This allows dereferencing raw pointers, calling unsafe functions, etc. Use with extreme caution.

**Code Example:**
```rust
let mut num = 5;
let r1 = &num as *const i32;
unsafe {
    println!("r1 is: {}", *r1);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q16: How do you use Option and Result combinators?

**Difficulty**: Intermediate

**Strategy:**
Use combinators like `map`, `and_then`, `unwrap_or`, and `ok_or` to chain operations and handle values safely without explicit `match` statements.

**Code Example:**
```rust
fn get_username(id: i32) -> Option<String> {
    if id == 1 { Some("Alice".to_string()) } else { None }
}

fn main() {
    let name_len = get_username(1)
        .map(|name| name.len()) // Transform if Some
        .unwrap_or(0);          // Default if None
        
    println!("Length: {}", name_len);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q17: When should you use Box<T>?

**Difficulty**: Intermediate

**Strategy:**
Use `Box<T>` to store data on the heap instead of the stack. It is essential for recursive types (where size must be known at compile time) and when transferring ownership of large data to avoid copying.

**Code Example:**
```rust
enum List {
    Cons(i32, Box<List>),
    Nil,
}

fn main() {
    let list = List::Cons(1, Box::new(List::Cons(2, Box::new(List::Nil))));
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q18: What is the difference between RefCell and Cell?

**Difficulty**: Advanced

**Strategy:**
`Cell<T>` provides interior mutability by moving values in and out (for `Copy` types). `RefCell<T>` allows borrowing dynamically at runtime (checking borrowing rules at runtime instead of compile time), causing a panic if rules are violated.

**Code Example:**
```rust
use std::cell::{Cell, RefCell};

struct Data {
    count: Cell<i32>,
    name: RefCell<String>,
}

fn main() {
    let data = Data { count: Cell::new(0), name: RefCell::new("Rust".into()) };
    
    data.count.set(10); // Mutate via shared reference
    *data.name.borrow_mut() = "Go".into(); // Runtime borrow check
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q19: When to use Arc vs Rc?

**Difficulty**: Intermediate

**Strategy:**
`Rc` (Reference Counted) is for single-threaded scenarios where you need multiple owners. `Arc` (Atomic Reference Counted) is thread-safe and can be shared across threads, but has a slight performance overhead due to atomic operations.

**Code Example:**
```rust
use std::sync::Arc;
use std::thread;

fn main() {
    let data = Arc::new(vec![1, 2, 3]);
    let data_clone = Arc::clone(&data);

    thread::spawn(move || {
        println!("{:?}", data_clone);
    }).join().unwrap();
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q20: How do you implement From and Into traits?

**Difficulty**: Intermediate

**Strategy:**
Implement `From<T>` for your type. `Into<U>` is automatically implemented when `From` is defined. This allows for easy type conversions.

**Code Example:**
```rust
struct Number(i32);

impl From<i32> for Number {
    fn from(item: i32) -> Self {
        Number(item)
    }
}

fn main() {
    let num: Number = 10.into(); // Uses Into automatically
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q21: How does Deref coercion work?

**Difficulty**: Advanced

**Strategy:**
Implementing the `Deref` trait allows a type to behave like the type it points to. Rust automatically coerces types (e.g., `&String` to `&str`) when passing arguments to functions.

**Code Example:**
```rust
use std::ops::Deref;

struct MyBox<T>(T);

impl<T> Deref for MyBox<T> {
    type Target = T;
    fn deref(&self) -> &T {
        &self.0
    }
}

fn hello(name: &str) {
    println!("Hello, {}", name);
}

fn main() {
    let m = MyBox(String::from("Rust"));
    hello(&m); // Deref coercion: &MyBox<String> -> &String -> &str
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q22: How do you swap values efficiently?

**Difficulty**: Intermediate

**Strategy:**
Use `std::mem::swap` to exchange values of two mutable references without ownership transfer issues. Use `std::mem::replace` to take a value out of a mutable reference and replace it with another.

**Code Example:**
```rust
use std::mem;

fn main() {
    let mut x = 5;
    let mut y = 10;

    mem::swap(&mut x, &mut y);
    assert_eq!(x, 10);
    assert_eq!(y, 5);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q23: What is Cow (Copy-on-Write)?

**Difficulty**: Advanced

**Strategy:**
`Cow` is a smart pointer that holds either borrowed data or owned data. It clones the data only when mutation is necessary (lazy cloning).

**Code Example:**
```rust
use std::borrow::Cow;

fn remove_spaces(s: &str) -> Cow<str> {
    if s.contains(' ') {
        Cow::Owned(s.replace(' ', ""))
    } else {
        Cow::Borrowed(s)
    }
}

fn main() {
    let s1 = "hello";
    let s2 = "hello world";
    
    // No allocation
    let res1 = remove_spaces(s1);
    
    // Allocation happens here
    let res2 = remove_spaces(s2);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q24: When should you use PhantomData?

**Difficulty**: Advanced

**Strategy:**
`PhantomData<T>` is a zero-sized type used to mark that a struct generically "owns" or "references" a type `T`, even if `T` isn't used in any field. This is crucial for informing the compiler about drop checks and variance.

**Code Example:**
```rust
use std::marker::PhantomData;

struct MyPtr<T> {
    ptr: *const T,
    _marker: PhantomData<T>, // Acts as if we own a T
}

fn main() {
    let _p: MyPtr<i32> = MyPtr { ptr: std::ptr::null(), _marker: PhantomData };
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q25: How do you write unit tests in Rust?

**Difficulty**: Beginner

**Strategy:**
Place unit tests in the same file as the code, inside a module annotated with `#[cfg(test)]`. Use `#[test]` on test functions.

**Code Example:**
```rust
fn add(a: i32, b: i32) -> i32 {
    a + b
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_add() {
        assert_eq!(add(2, 2), 4);
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q26: How do you use the Entry API for HashMaps?

**Difficulty**: Intermediate

**Strategy:**
The `entry` API allows efficient insertion or modification of values in a `HashMap` without double lookups.

**Code Example:**
```rust
use std::collections::HashMap;

fn main() {
    let mut scores = HashMap::new();
    
    scores.entry("Blue").or_insert(10);
    scores.entry("Blue").and_modify(|e| *e += 1).or_insert(10);
    
    println!("{:?}", scores);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q27: What is the difference between const and static?

**Difficulty**: Intermediate

**Strategy:**
`const` items are inlined at each usage site (no fixed memory address). `static` items have a fixed memory address and live for the entire program duration. `static mut` is unsafe.

**Code Example:**
```rust
const MAX_POINTS: u32 = 100_000;
static LANGUAGE: &str = "Rust";

fn main() {
    println!("{}, {}", MAX_POINTS, LANGUAGE);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q28: How do you use match guards?

**Difficulty**: Beginner

**Strategy:**
Match guards allow you to add an extra `if` condition to a `match` arm pattern.

**Code Example:**
```rust
fn main() {
    let pair = (2, -2);
    
    match pair {
        (x, y) if x == y => println!("Equal"),
        (x, y) if x + y == 0 => println!("Sum is zero"),
        _ => println!("Other"),
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q29: How do you create a thread-safe global counter?

**Difficulty**: Intermediate

**Strategy:**
Use `std::sync::atomic::AtomicUsize` (or other atomic types) for simple counters, or `Mutex` for more complex data.

**Code Example:**
```rust
use std::sync::atomic::{AtomicUsize, Ordering};

static COUNTER: AtomicUsize = AtomicUsize::new(0);

fn main() {
    COUNTER.fetch_add(1, Ordering::SeqCst);
    println!("{}", COUNTER.load(Ordering::SeqCst));
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q30: How do you handle results with the ? operator?

**Difficulty**: Beginner

**Strategy:**
The `?` operator propagates errors. If a Result is `Err`, it returns early from the function; otherwise, it unwraps the `Ok` value.

**Code Example:**
```rust
use std::fs::File;
use std::io::{self, Read};

fn read_username() -> Result<String, io::Error> {
    let mut s = String::new();
    File::open("hello.txt")?.read_to_string(&mut s)?;
    Ok(s)
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---


---

### Q31: How do you implement the `Iterator` trait for a custom type?

**Difficulty**: Intermediate

**Strategy:**
Implement the `Iterator` trait by defining the `Item` associated type and the `next` method. The `next` method should return `Option<Self::Item>`.

**Code Example:**
```rust
struct Counter {
    count: u32,
}

impl Iterator for Counter {
    type Item = u32;

    fn next(&mut self) -> Option<Self::Item> {
        self.count += 1;
        if self.count < 6 {
            Some(self.count)
        } else {
            None
        }
    }
}

fn main() {
    let counter = Counter { count: 0 };
    for i in counter {
        println!("{}", i);
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q32: How do you handle errors using `thiserror`?

**Difficulty**: Intermediate

**Strategy:**
`thiserror` provides a convenient macro to derive the `Error` trait for custom enums, reducing boilerplate code for error definitions.

**Code Example:**
```rust
use thiserror::Error;

#[derive(Error, Debug)]
pub enum DataStoreError {
    #[error("data not found")]
    NotFound,
    #[error("invalid disconnect")]
    Disconnect(#[from] std::io::Error),
    #[error("unknown error")]
    Unknown,
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q33: How do you use `serde` for JSON serialization?

**Difficulty**: Beginner

**Strategy:**
Add `serde` and `serde_json` dependencies. Derive `Serialize` and `Deserialize` traits on your structs to enable automatic conversion to/from JSON.

**Code Example:**
```rust
use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize, Debug)]
struct User {
    id: u32,
    name: String,
}

fn main() {
    let user = User { id: 1, name: "Alice".into() };
    
    // Serialize
    let json = serde_json::to_string(&user).unwrap();
    println!("{}", json);
    
    // Deserialize
    let parsed: User = serde_json::from_str(&json).unwrap();
    println!("{:?}", parsed);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q34: How do you use `tokio` for async execution?

**Difficulty**: Intermediate

**Strategy:**
Use the `#[tokio::main]` attribute to turn the `main` function into an async runtime entry point. Use `.await` to suspend execution until a future completes.

**Code Example:**
```rust
#[tokio::main]
async fn main() {
    let result = say_hello().await;
    println!("{}", result);
}

async fn say_hello() -> &'static str {
    // Simulate async work
    tokio::time::sleep(tokio::time::Duration::from_millis(100)).await;
    "Hello, World!"
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q35: How do you use `Weak` pointers to prevent reference cycles?

**Difficulty**: Advanced

**Strategy:**
`Weak<T>` provides a non-owning reference to an allocation managed by `Arc<T>` or `Rc<T>`. It doesn't prevent deallocation, thus breaking cycles (e.g., parent-child relationships).

**Code Example:**
```rust
use std::rc::{Rc, Weak};
use std::cell::RefCell;

struct Node {
    parent: RefCell<Weak<Node>>,
    children: RefCell<Vec<Rc<Node>>>,
}

fn main() {
    let leaf = Rc::new(Node {
        parent: RefCell::new(Weak::new()),
        children: RefCell::new(vec![]),
    });
    
    let branch = Rc::new(Node {
        parent: RefCell::new(Weak::new()),
        children: RefCell::new(vec![leaf.clone()]),
    });
    
    *leaf.parent.borrow_mut() = Rc::downgrade(&branch);
    // No memory leak!
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q36: How do you create a declarative macro?

**Difficulty**: Advanced

**Strategy:**
Use `macro_rules!` to define a macro. Macros match patterns in the code and expand into Rust code at compile time.

**Code Example:**
```rust
macro_rules! say_hello {
    () => {
        println!("Hello!");
    };
    ($name:expr) => {
        println!("Hello, {}!", $name);
    };
}

fn main() {
    say_hello!();
    say_hello!("Rustacean");
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q37: How do you call C code from Rust (FFI)?

**Difficulty**: Advanced

**Strategy:**
Use `extern "C"` blocks to define foreign function signatures. Mark the call as `unsafe` because the compiler cannot guarantee safety across the FFI boundary.

**Code Example:**
```rust
extern "C" {
    fn abs(input: i32) -> i32;
}

fn main() {
    unsafe {
        let result = abs(-10);
        println!("Absolute value: {}", result);
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q38: How do you implement a Builder Pattern?

**Difficulty**: Intermediate

**Strategy:**
Create a separate Builder struct with methods to set fields, returning `&mut Self` or `Self`. Add a `build()` method to consume the builder and return the final struct.

**Code Example:**
```rust
#[derive(Debug)]
struct Server {
    host: String,
    port: u16,
}

struct ServerBuilder {
    host: String,
    port: u16,
}

impl ServerBuilder {
    fn new() -> Self {
        Self { host: "localhost".into(), port: 8080 }
    }
    
    fn port(mut self, port: u16) -> Self {
        self.port = port;
        self
    }
    
    fn build(self) -> Server {
        Server { host: self.host, port: self.port }
    }
}

fn main() {
    let s = ServerBuilder::new().port(3000).build();
    println!("{:?}", s);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q39: How do you use `std::sync::mpsc` for message passing?

**Difficulty**: Intermediate

**Strategy:**
`mpsc` stands for Multi-Producer, Single-Consumer. Use `channel()` to create a sender and receiver pair for communicating between threads.

**Code Example:**
```rust
use std::sync::mpsc;
use std::thread;

fn main() {
    let (tx, rx) = mpsc::channel();

    thread::spawn(move || {
        tx.send("ping").unwrap();
    });

    let msg = rx.recv().unwrap();
    println!("{}", msg);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q40: How do you write documentation comments?

**Difficulty**: Beginner

**Strategy:**
Use `///` for documenting items (functions, structs). These comments support Markdown and are used by `rustdoc` to generate HTML documentation.

**Code Example:**
```rust
/// Adds one to the number given.
///
/// # Examples
///
/// ```
/// let arg = 5;
/// let answer = my_crate::add_one(arg);
///
/// assert_eq!(6, answer);
/// ```
pub fn add_one(x: i32) -> i32 {
    x + 1
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q41: How do you use `Cow` (Copy-on-Write) efficiently?

**Difficulty**: Advanced

**Strategy:**
`Cow<str>` allows holding either a borrowed `&str` or an owned `String`. It only allocates (clones) when mutation is necessary or ownership is required.

**Code Example:**
```rust
use std::borrow::Cow;

fn sanitize(input: &str) -> Cow<str> {
    if input.contains("bad") {
        Cow::Owned(input.replace("bad", "good"))
    } else {
        Cow::Borrowed(input)
    }
}

fn main() {
    let s1 = "this is good";
    let s2 = "this is bad";
    
    // No allocation
    println!("{}", sanitize(s1));
    
    // Allocation happens here
    println!("{}", sanitize(s2));
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q42: How do you implement the `Default` trait?

**Difficulty**: Beginner

**Strategy:**
Implement `Default` to provide a standard default value for your type. This is often used with `..Default::default()` struct update syntax.

**Code Example:**
```rust
#[derive(Debug)]
struct Config {
    timeout: u32,
    retries: u32,
}

impl Default for Config {
    fn default() -> Self {
        Self { timeout: 30, retries: 3 }
    }
}

fn main() {
    let conf = Config {
        retries: 5,
        ..Default::default()
    };
    println!("{:?}", conf);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q43: How do you use `Any` trait for dynamic typing?

**Difficulty**: Expert

**Strategy:**
`Any` allows dynamic typing and downcasting at runtime. It works for types with static lifetime (usually `'static`).

**Code Example:**
```rust
use std::any::Any;

fn print_if_string(s: &dyn Any) {
    if let Some(string) = s.downcast_ref::<String>() {
        println!("It's a string: {}", string);
    } else {
        println!("Not a string");
    }
}

fn main() {
    print_if_string(&String::from("Hello"));
    print_if_string(&10);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q44: How do you use `lazy_static` or `OnceLock` (std)?

**Difficulty**: Intermediate

**Strategy:**
`std::sync::OnceLock` (Rust 1.70+) allows lazy initialization of global static variables without external crates like `lazy_static`.

**Code Example:**
```rust
use std::sync::OnceLock;

static CONFIG: OnceLock<String> = OnceLock::new();

fn get_config() -> &'static str {
    CONFIG.get_or_init(|| {
        println!("Initializing...");
        "Production".to_string()
    })
}

fn main() {
    println!("{}", get_config());
    println!("{}", get_config());
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q45: How do you optimize memory layout with `#[repr(C)]` or `#[repr(packed)]`?

**Difficulty**: Advanced

**Strategy:**
`#[repr(C)]` ensures C-compatible memory layout. `#[repr(packed)]` minimizes padding but may cause misaligned access (undefined behavior if not handled carefully).

**Code Example:**
```rust
#[repr(C)]
struct MyStruct {
    a: u8,
    b: u32,
}

fn main() {
    println!("Size: {}", std::mem::size_of::<MyStruct>());
    // Size is 8 (4 bytes alignment for u32)
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q46: How do you use `Pin` to handle self-referential structs?

**Difficulty**: Expert

**Strategy:**
`Pin<P>` prevents the value pointed to by `P` from being moved in memory. This is crucial for async futures which generate self-referential state machines.

**Code Example:**
```rust
use std::pin::Pin;
use std::marker::PhantomPinned;

struct SelfRef {
    data: String,
    ptr_to_data: *const String,
    _marker: PhantomPinned, // Makes it !Unpin
}

impl SelfRef {
    fn new(data: String) -> Pin<Box<Self>> {
        let res = Self {
            data,
            ptr_to_data: std::ptr::null(),
            _marker: PhantomPinned,
        };
        let mut boxed = Box::pin(res);
        let self_ptr: *const String = &boxed.data;
        unsafe {
            let mut_ref: &mut SelfRef = Pin::get_unchecked_mut(boxed.as_mut());
            mut_ref.ptr_to_data = self_ptr;
        }
        boxed
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q47: How do you use `std::collections::BTreeMap` vs `HashMap`?

**Difficulty**: Intermediate

**Strategy:**
`BTreeMap` keeps keys sorted. Use it when iteration order matters or you need range queries. `HashMap` is faster O(1) but unordered.

**Code Example:**
```rust
use std::collections::BTreeMap;

fn main() {
    let mut map = BTreeMap::new();
    map.insert(3, "c");
    map.insert(1, "a");
    map.insert(2, "b");

    // Iterates in sorted order of keys
    for (key, value) in &map {
        println!("{}: {}", key, value);
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q48: How do you implement a custom Drop trait?

**Difficulty**: Beginner

**Strategy:**
Implement `Drop` to execute code when a value goes out of scope (e.g., closing file handles, freeing resources).

**Code Example:**
```rust
struct FileHandler {
    name: String,
}

impl Drop for FileHandler {
    fn drop(&mut self) {
        println!("Closing file: {}", self.name);
    }
}

fn main() {
    let _f = FileHandler { name: "log.txt".into() };
    println!("Doing work...");
} // _f dropped here
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q49: How do you use `rayon` for data parallelism?

**Difficulty**: Intermediate

**Strategy:**
`rayon` is a data-parallelism library. Convert iterators to parallel iterators using `.par_iter()` to process items concurrently across CPU cores.

**Code Example:**
```rust
use rayon::prelude::*;

fn main() {
    let mut nums: Vec<i32> = (0..100).collect();
    
    // Parallel processing
    nums.par_iter_mut().for_each(|p| *p *= 2);
    
    println!("{:?}", &nums[0..5]);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q50: How do you use `std::process::Command` to run external programs?

**Difficulty**: Beginner

**Strategy:**
Use `Command` to spawn child processes. You can capture output, pipe input, and wait for completion.

**Code Example:**
```rust
use std::process::Command;

fn main() {
    let output = Command::new("echo")
        .arg("Hello from process")
        .output()
        .expect("Failed to execute command");

    println!("{}", String::from_utf8_lossy(&output.stdout));
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>
