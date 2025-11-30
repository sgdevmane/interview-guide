<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>C++ Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for developers</b></p>
</div>

---

## Table of Contents

1. [How do you prevent memory leaks in Modern C++ using RAII?](#q1-how-do-you-prevent-memory-leaks-in-modern-c++-using-raii) <span class="beginner">Beginner</span>
2. [How do you implement Move Semantics to optimize performance when returning large objects?](#q2-how-do-you-implement-move-semantics-to-optimize-performance-when-returning-large-objects) <span class="intermediate">Intermediate</span>
3. [How do you resolve circular dependencies when using `std::shared_ptr`?](#q3-how-do-you-resolve-circular-dependencies-when-using-std::shared_ptr) <span class="intermediate">Intermediate</span>
4. [How do you use `std::async` to run a task asynchronously and retrieve the result?](#q4-how-do-you-use-std::async-to-run-a-task-asynchronously-and-retrieve-the-result) <span class="intermediate">Intermediate</span>
5. [How do you use `if constexpr` to optimize template code at compile time?](#q5-how-do-you-use-if-constexpr-to-optimize-template-code-at-compile-time) <span class="advanced">Advanced</span>
6. [How do you ensure thread safety when accessing a shared variable without using heavy mutexes?](#q6-how-do-you-ensure-thread-safety-when-accessing-a-shared-variable-without-using-heavy-mutexes) <span class="advanced">Advanced</span>
7. [How do you implement Perfect Forwarding in a template function?](#q7-how-do-you-implement-perfect-forwarding-in-a-template-function) <span class="advanced">Advanced</span>
8. [How do you handle multiple return values from a function efficiently?](#q8-how-do-you-handle-multiple-return-values-from-a-function-efficiently) <span class="intermediate">Intermediate</span>
9. [How do you avoid Virtual Function overhead (dynamic dispatch) when polymorphism is needed?](#q9-how-do-you-avoid-virtual-function-overhead-dynamic-dispatch-when-polymorphism-is-needed) <span class="expert">Expert</span>
10. [How do you use `std::variant` to create a type-safe union?](#q10-how-do-you-use-std::variant-to-create-a-type-safe-union) <span class="intermediate">Intermediate</span>
11. [How do you prevent 'Object Slicing' when passing derived objects to functions?](#q11-how-do-you-prevent-object-slicing-when-passing-derived-objects-to-functions) <span class="beginner">Beginner</span>
12. [How do you use `std::optional` to handle values that might not exist?](#q12-how-do-you-use-std::optional-to-handle-values-that-might-not-exist) <span class="intermediate">Intermediate</span>
13. [How do you optimize vector growth to avoid frequent reallocations?](#q13-how-do-you-optimize-vector-growth-to-avoid-frequent-reallocations) <span class="beginner">Beginner</span>
14. [How do you debug a segmentation fault caused by a dangling pointer?](#q14-how-do-you-debug-a-segmentation-fault-caused-by-a-dangling-pointer) <span class="intermediate">Intermediate</span>
15. [How do you ensure a destructor in a base class allows proper cleanup of derived classes?](#q15-how-do-you-ensure-a-destructor-in-a-base-class-allows-proper-cleanup-of-derived-classes) <span class="beginner">Beginner</span>
16. [What is the difference between std::unique_ptr and std::shared_ptr?](#q16-what-is-the-difference-between-std::unique_ptr-and-std::shared_ptr) <span class="intermediate">Intermediate</span>
17. [When should you choose std::map over std::unordered_map?](#q17-when-should-you-choose-std::map-over-std::unordered_map) <span class="intermediate">Intermediate</span>
18. [How does const_cast work and when should you avoid it?](#q18-how-does-const_cast-work-and-when-should-you-avoid-it) <span class="intermediate">Intermediate</span>
19. [What is the purpose of the volatile keyword?](#q19-what-is-the-purpose-of-the-volatile-keyword) <span class="advanced">Advanced</span>
20. [How do you use a custom deleter with std::unique_ptr?](#q20-how-do-you-use-a-custom-deleter-with-std::unique_ptr) <span class="advanced">Advanced</span>
21. [What is Template Specialization?](#q21-what-is-template-specialization) <span class="intermediate">Intermediate</span>
22. [How does SFINAE work?](#q22-how-does-sfinae-work) <span class="advanced">Advanced</span>
23. [What does std::move actually do?](#q23-what-does-std::move-actually-do) <span class="intermediate">Intermediate</span>
24. [When should you use std::function over function pointers?](#q24-when-should-you-use-std::function-over-function-pointers) <span class="intermediate">Intermediate</span>
25. [How do lambda captures work?](#q25-how-do-lambda-captures-work) <span class="beginner">Beginner</span>
26. [What are Structured Bindings (C++17)?](#q26-what-are-structured-bindings-c++17) <span class="beginner">Beginner</span>
27. [Why use std::string_view (C++17)?](#q27-why-use-std::string_view-c++17) <span class="intermediate">Intermediate</span>
28. [What is the difference between constexpr and consteval (C++20)?](#q28-what-is-the-difference-between-constexpr-and-consteval-c++20) <span class="intermediate">Intermediate</span>
29. [What is Uniform Initialization?](#q29-what-is-uniform-initialization) <span class="beginner">Beginner</span>
30. [Why are Virtual Destructors important?](#q30-why-are-virtual-destructors-important) <span class="intermediate">Intermediate</span>

---

### Q1: How do you prevent memory leaks in Modern C++ using RAII?

**Difficulty**: Beginner

**Strategy:**
**Difficulty**: Beginner


Avoid manual `new`/`delete`. Use **Smart Pointers** (`std::unique_ptr`, `std::shared_ptr`) and stack allocation. RAII ensures resources are released when the object goes out of scope.

**Code Example:**
```cpp
#include <memory>

class Resource { public: ~Resource() { /* Cleanup */ } };

void process() {
    // Automatically deleted when function exits
    std::unique_ptr<Resource> res = std::make_unique<Resource>();
    
    // No need for delete res;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q2: How do you implement Move Semantics to optimize performance when returning large objects?

**Difficulty**: Intermediate

**Strategy:**
**Difficulty**: Intermediate


Implement a **Move Constructor** and **Move Assignment Operator**. Use `std::move` to cast an lvalue to an rvalue, allowing resources (like pointers) to be "stolen" rather than copied.

**Code Example:**
```cpp
class Buffer {
    int* data;
public:
    // Move Constructor
    Buffer(Buffer&& other) noexcept : data(other.data) {
        other.data = nullptr; // Transfer ownership
    }
};

Buffer createBuffer() {
    Buffer b;
    return b; // Compiler uses Move automatically (or RVO)
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q3: How do you resolve circular dependencies when using `std::shared_ptr`?

**Difficulty**: Intermediate

**Strategy:**
**Difficulty**: Intermediate


Use `std::weak_ptr` for one of the references. A weak pointer does not increase the reference count, preventing the cycle that keeps objects alive forever.

**Code Example:**
```cpp
struct Node {
    std::shared_ptr<Node> next;
    std::weak_ptr<Node> prev; // Weak reference prevents cycle
};

void link(std::shared_ptr<Node> a, std::shared_ptr<Node> b) {
    a->next = b;
    b->prev = a;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q4: How do you use `std::async` to run a task asynchronously and retrieve the result?

**Difficulty**: Intermediate

**Strategy:**
**Difficulty**: Intermediate


Use `std::async` with the `std::launch::async` policy. It returns a `std::future` which holds the result. Calling `.get()` on the future blocks until the result is ready.

**Code Example:**
```cpp
#include <future>

int heavyComputation(int x) { return x * x; }

void main() {
    // Run in a separate thread
    std::future<int> result = std::async(std::launch::async, heavyComputation, 10);
    
    // Do other work...
    
    int value = result.get(); // Blocks here if not ready
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q5: How do you use `if constexpr` to optimize template code at compile time?

**Difficulty**: Advanced

**Strategy:**
**Difficulty**: Advanced


Use `if constexpr` (C++17) to discard branches of code at compile-time based on template arguments. This avoids compilation errors for invalid operations in the discarded branch (like SFINAE but cleaner).

**Code Example:**
```cpp
template <typename T>
void print(T value) {
    if constexpr (std::is_pointer_v<T>) {
        std::cout << *value << "\n";
    } else {
        std::cout << value << "\n";
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q6: How do you ensure thread safety when accessing a shared variable without using heavy mutexes?

**Difficulty**: Advanced

**Strategy:**
**Difficulty**: Advanced


Use `std::atomic<T>` for simple types (integers, pointers). It provides lock-free thread safety for operations like increment, load, and store.

**Code Example:**
```cpp
#include <atomic>

std::atomic<int> counter(0);

void increment() {
    counter.fetch_add(1, std::memory_order_relaxed);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q7: How do you implement Perfect Forwarding in a template function?

**Difficulty**: Advanced

**Strategy:**
**Difficulty**: Advanced


Use **Universal References** (`T&&`) and `std::forward<T>`. This preserves the value category (lvalue vs rvalue) of the arguments passed to the function.

**Code Example:**
```cpp
template <typename T>
void wrapper(T&& arg) {
    // Forwards arg exactly as it was passed
    process(std::forward<T>(arg)); 
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q8: How do you handle multiple return values from a function efficiently?

**Difficulty**: Intermediate

**Strategy:**
**Difficulty**: Intermediate


Use `std::tuple` or, in C++17, **Structured Binding** with a struct or pair. This avoids output parameters and improves readability.

**Code Example:**
```cpp
struct Result { int x; double y; };

Result calculate() { return {1, 2.5}; }

void main() {
    auto [x, y] = calculate(); // Structured binding
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q9: How do you avoid Virtual Function overhead (dynamic dispatch) when polymorphism is needed?

**Difficulty**: Expert

**Strategy:**
**Difficulty**: Expert


Use **Static Polymorphism** via CRTP (Curiously Recurring Template Pattern). The derived class is passed as a template argument to the base class, allowing compile-time resolution.

**Code Example:**
```cpp
template <typename Derived>
class Base {
public:
    void interface() {
        static_cast<Derived*>(this)->implementation();
    }
};

class Derived : public Base<Derived> {
public:
    void implementation() { /* ... */ }
};
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q10: How do you use `std::variant` to create a type-safe union?

**Difficulty**: Intermediate

**Strategy:**
**Difficulty**: Intermediate


`std::variant` (C++17) can hold one of several types. Use `std::visit` or `std::get_if` to access the value safely, handling all possible types.

**Code Example:**
```cpp
#include <variant>

std::variant<int, float> v = 10;

struct Visitor {
    void operator()(int i) { std::cout << "Int: " << i; }
    void operator()(float f) { std::cout << "Float: " << f; }
};

std::visit(Visitor{}, v);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q11: How do you prevent 'Object Slicing' when passing derived objects to functions?

**Difficulty**: Beginner

**Strategy:**
**Difficulty**: Beginner


Always pass polymorphic objects by **Reference** (`Base&`) or **Pointer** (`Base*`). Passing by value copies only the `Base` part of the object, discarding the `Derived` data.

**Code Example:**
```cpp
class Base { virtual void foo() {} };
class Derived : public Base { ... };

// BAD: Slices object
void process(Base b) { ... }

// GOOD: Preserves polymorphism
void process(const Base& b) { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q12: How do you use `std::optional` to handle values that might not exist?

**Difficulty**: Intermediate

**Strategy:**
**Difficulty**: Intermediate


Return `std::optional<T>` instead of using pointers (`nullptr`) or magic values (e.g., -1) to indicate failure/absence.

**Code Example:**
```cpp
#include <optional>

std::optional<int> findUser(int id) {
    if (id == 0) return std::nullopt;
    return 42;
}

void main() {
    auto user = findUser(0);
    if (user.has_value()) { /* ... */ }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q13: How do you optimize vector growth to avoid frequent reallocations?

**Difficulty**: Beginner

**Strategy:**
**Difficulty**: Beginner


Use `reserve(n)` if you know (or can estimate) the number of elements beforehand. This allocates memory once, preventing expensive copy/move operations during growth.

**Code Example:**
```cpp
std::vector<int> vec;
vec.reserve(1000); // Allocates for 1000 ints

for(int i=0; i<1000; ++i) {
    vec.push_back(i); // No reallocations occur here
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q14: How do you debug a segmentation fault caused by a dangling pointer?

**Difficulty**: Intermediate

**Strategy:**
**Difficulty**: Intermediate


Use tools like **Valgrind** or **AddressSanitizer** (ASan). Compile with `-fsanitize=address` (GCC/Clang) to get detailed reports on use-after-free or out-of-bounds access.

**Code Example (Command):**
```bash
g++ -fsanitize=address -g main.cpp -o main
./main
# Output will show exact line number of invalid access
```

**Code Example:**
```cpp

```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q15: How do you ensure a destructor in a base class allows proper cleanup of derived classes?

**Difficulty**: Beginner

**Strategy:**
**Difficulty**: Beginner


Declare the base class destructor as **virtual**. This ensures that when deleting a derived object through a base pointer, the derived destructor is called first.

**Code Example:**
```cpp
class Base {
public:
    virtual ~Base() { /* Always make this virtual */ }
};

class Derived : public Base {
    ~Derived() { /* Cleanup derived resources */ }
};
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q16: What is the difference between std::unique_ptr and std::shared_ptr?

**Difficulty**: Intermediate

**Strategy:**
`std::unique_ptr` represents exclusive ownership (cannot be copied, only moved). `std::shared_ptr` represents shared ownership (reference counted). Use `unique_ptr` by default.

**Code Example:**
```cpp
#include <memory>

void example() {
    std::unique_ptr<int> p1 = std::make_unique<int>(10);
    // std::unique_ptr<int> p2 = p1; // Error: Copying not allowed
    std::unique_ptr<int> p2 = std::move(p1); // OK: Ownership transferred

    std::shared_ptr<int> s1 = std::make_shared<int>(20);
    std::shared_ptr<int> s2 = s1; // OK: Reference count increases
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q17: When should you choose std::map over std::unordered_map?

**Difficulty**: Intermediate

**Strategy:**
Use `std::map` (Red-Black Tree) when you need ordered keys or range iterations. Use `std::unordered_map` (Hash Table) for O(1) average time complexity lookups when order doesn't matter.

**Code Example:**
```cpp
#include <map>
#include <unordered_map>
#include <string>

void example() {
    std::map<int, std::string> ordered; // Keys sorted by int
    ordered[2] = "two";
    ordered[1] = "one"; // Iteration: 1, 2

    std::unordered_map<int, std::string> unordered; // Order undefined
    unordered[2] = "two";
    unordered[1] = "one";
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q18: How does const_cast work and when should you avoid it?

**Difficulty**: Intermediate

**Strategy:**
`const_cast` removes or adds `const` qualification. Modifying a value that was originally declared `const` using `const_cast` invokes undefined behavior. It is mostly used to interface with legacy APIs that are not const-correct.

**Code Example:**
```cpp
void print(char* str) {
    // Legacy API that takes non-const char* but doesn't modify it
}

void example() {
    const char* msg = "Hello";
    print(const_cast<char*>(msg)); // Necessary evil
    
    const int x = 10;
    int* px = const_cast<int*>(&x);
    *px = 20; // Undefined Behavior!
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q19: What is the purpose of the volatile keyword?

**Difficulty**: Advanced

**Strategy:**
`volatile` tells the compiler not to optimize reads/writes to a variable because it may change unexpectedly (e.g., by hardware or signal handler). It does NOT provide thread safety or atomicity.

**Code Example:**
```cpp
volatile bool flag = false;

void wait_for_flag() {
    while (!flag) {
        // Compiler won't optimize this loop away
        // or cache 'flag' in a register
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q20: How do you use a custom deleter with std::unique_ptr?

**Difficulty**: Advanced

**Strategy:**
You can pass a custom deleter (function or struct) as a template argument (and constructor argument) to `std::unique_ptr` to handle resource cleanup other than `delete` (e.g., `fclose`).

**Code Example:**
```cpp
#include <memory>
#include <cstdio>

struct FileDeleter {
    void operator()(FILE* file) const {
        if (file) fclose(file);
    }
};

void example() {
    std::unique_ptr<FILE, FileDeleter> file(fopen("test.txt", "w"));
    // file will be automatically closed when it goes out of scope
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q21: What is Template Specialization?

**Difficulty**: Intermediate

**Strategy:**
Template specialization allows you to define a different implementation of a template for a specific type. Useful for optimizing for specific types or handling types that behave differently.

**Code Example:**
```cpp
#include <iostream>

template <typename T>
struct Printer {
    static void print(T val) { std::cout << "Generic: " << val << "\n"; }
};

// Specialization for char*
template <>
struct Printer<const char*> {
    static void print(const char* val) { std::cout << "String: " << val << "\n"; }
};

void example() {
    Printer<int>::print(42);
    Printer<const char*>::print("Hello");
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q22: How does SFINAE work?

**Difficulty**: Advanced

**Strategy:**
SFINAE (Substitution Failure Is Not An Error) allows templates to be discarded from the overload set if type substitution fails, rather than causing a compile error. Used with `std::enable_if`.

**Code Example:**
```cpp
#include <type_traits>
#include <iostream>

template <typename T>
typename std::enable_if<std::is_integral<T>::value>::type
process(T t) {
    std::cout << "Integral: " << t << "\n";
}

template <typename T>
typename std::enable_if<std::is_floating_point<T>::value>::type
process(T t) {
    std::cout << "Float: " << t << "\n";
}

void example() {
    process(10);   // Calls Integral version
    process(3.14); // Calls Float version
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q23: What does std::move actually do?

**Difficulty**: Intermediate

**Strategy:**
`std::move` casts an lvalue to an rvalue reference (`T&&`), enabling move semantics. It doesn't move anything itself; it just allows the move constructor or move assignment operator to be called.

**Code Example:**
```cpp
#include <utility>
#include <vector>

void example() {
    std::vector<int> v1 = {1, 2, 3};
    std::vector<int> v2 = std::move(v1); 
    
    // v1 is now in a valid but unspecified state (likely empty)
    // v2 owns the data {1, 2, 3}
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q24: When should you use std::function over function pointers?

**Difficulty**: Intermediate

**Strategy:**
Use `std::function` when you need to store any callable target (functions, lambdas, functors, bind expressions). Use function pointers only for C compatibility or extreme performance (avoiding `std::function` overhead).

**Code Example:**
```cpp
#include <functional>
#include <iostream>

void free_func() { std::cout << "Free function\n"; }

void example() {
    std::function<void()> f;
    
    f = free_func;
    f();
    
    f = []() { std::cout << "Lambda\n"; };
    f();
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q25: How do lambda captures work?

**Difficulty**: Beginner

**Strategy:**
`[=]` captures all local variables by value. `[&]` captures all by reference. `[x, &y]` captures `x` by value and `y` by reference. Be careful with lifetimes when capturing by reference.

**Code Example:**
```cpp
#include <iostream>

void example() {
    int x = 10;
    int y = 20;
    
    auto lambda = [x, &y]() {
        // x is a copy, y is a reference
        std::cout << x << " " << y << "\n";
        y = 30; // Modifies outer y
    };
    
    lambda();
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q26: What are Structured Bindings (C++17)?

**Difficulty**: Beginner

**Strategy:**
Structured bindings allow you to unpack tuples, pairs, arrays, and structs into individual variables directly.

**Code Example:**
```cpp
#include <tuple>
#include <map>

std::tuple<int, int> get_coords() { return {10, 20}; }

void example() {
    auto [x, y] = get_coords();
    
    std::map<int, int> m = {{1, 2}};
    for (const auto& [key, val] : m) {
        // Use key and val
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q27: Why use std::string_view (C++17)?

**Difficulty**: Intermediate

**Strategy:**
`std::string_view` provides a non-owning reference to a string (or part of it). It avoids memory allocation when passing substrings or C-strings to functions.

**Code Example:**
```cpp
#include <string_view>
#include <iostream>

void print(std::string_view sv) {
    std::cout << sv << "\n";
}

void example() {
    const char* s = "Hello World";
    print(s); // No allocation (unlike std::string)
    
    std::string str = "Hello C++";
    print(str); // No allocation
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q28: What is the difference between constexpr and consteval (C++20)?

**Difficulty**: Intermediate

**Strategy:**
`constexpr` functions *can* be evaluated at compile time if arguments are constant expressions, but can also run at runtime. `consteval` (immediate functions) *must* be evaluated at compile time; otherwise, it's a compilation error.

**Code Example:**
```cpp
consteval int square(int n) {
    return n * n;
}

void example() {
    int x = 10;
    // int y = square(x); // Error: x is not a constant expression
    constexpr int z = square(10); // OK
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q29: What is Uniform Initialization?

**Difficulty**: Beginner

**Strategy:**
Uniform initialization uses braces `{}` to initialize objects. It prevents narrowing conversions and can be used for almost all initialization contexts.

**Code Example:**
```cpp
#include <vector>

class Point {
    int x, y;
public:
    Point(int x, int y) : x(x), y(y) {}
};

void example() {
    int a{5};
    int b = {10};
    Point p{1, 2};
    std::vector<int> v{1, 2, 3, 4};
    
    // int c{3.14}; // Error: Narrowing conversion
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q30: Why are Virtual Destructors important?

**Difficulty**: Intermediate

**Strategy:**
If a class is intended to be used polymorphically (accessed via a base class pointer), its destructor should be `virtual`. This ensures the derived class destructor is called when the object is deleted through the base pointer.

**Code Example:**
```cpp
class Base {
public:
    virtual ~Base() { /* Cleanup */ }
};

class Derived : public Base {
    int* ptr;
public:
    Derived() { ptr = new int[10]; }
    ~Derived() { delete[] ptr; } // Won't be called if Base dtor isn't virtual
};

void example() {
    Base* b = new Derived();
    delete b; // Calls ~Derived() then ~Base() correctly
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

