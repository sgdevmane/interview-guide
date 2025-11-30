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
17. [When should you use Box<T>?](#q17-when-should-you-use-box<t>) <span class="intermediate">Intermediate</span>
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

---

### Q1: How do you handle errors without using exceptions?

**Difficulty**: Beginner

**Strategy:**
**Difficulty**: Beginner


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
**Difficulty**: Intermediate


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
**Difficulty**: Beginner


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
**Difficulty**: Intermediate


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
**Difficulty**: Intermediate


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
**Difficulty**: Intermediate


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
**Difficulty**: Advanced


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
**Difficulty**: Intermediate


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
**Difficulty**: Beginner


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
**Difficulty**: Intermediate


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
**Difficulty**: Beginner


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
**Difficulty**: Intermediate


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
**Difficulty**: Advanced


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
**Difficulty**: Beginner


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
**Difficulty**: Advanced


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

