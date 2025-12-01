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
31. [How do you use C++20 Concepts to constrain template parameters?](#q31-how-do-you-use-c++20-concepts-to-constrain-template-parameters) <span class="intermediate">Intermediate</span>
32. [How do you use `std::jthread` (C++20) for automatic joining?](#q32-how-do-you-use-std::jthread-c++20-for-automatic-joining) <span class="beginner">Beginner</span>
33. [How do you use the C++20 Ranges library for pipeline operations?](#q33-how-do-you-use-the-c++20-ranges-library-for-pipeline-operations) <span class="intermediate">Intermediate</span>
34. [How do you implement the Observer pattern using `std::function`?](#q34-how-do-you-implement-the-observer-pattern-using-std::function) <span class="advanced">Advanced</span>
35. [How do you use `std::span` (C++20) to pass contiguous memory safely?](#q35-how-do-you-use-std::span-c++20-to-pass-contiguous-memory-safely) <span class="intermediate">Intermediate</span>
36. [How do you use `std::atomic_flag` for a spinlock?](#q36-how-do-you-use-std::atomic_flag-for-a-spinlock) <span class="advanced">Advanced</span>
37. [How do you perform compile-time string hashing?](#q37-how-do-you-perform-compile-time-string-hashing) <span class="advanced">Advanced</span>
38. [How do you use `std::any` to store values of any type?](#q38-how-do-you-use-std::any-to-store-values-of-any-type) <span class="intermediate">Intermediate</span>
39. [How do you implement the Pimpl (Pointer to Implementation) idiom?](#q39-how-do-you-implement-the-pimpl-pointer-to-implementation-idiom) <span class="advanced">Advanced</span>
40. [How do you use `std::reduce` for parallel accumulation?](#q40-how-do-you-use-std::reduce-for-parallel-accumulation) <span class="advanced">Advanced</span>
41. [How do you avoid Small String Optimization (SSO) pitfalls?](#q41-how-do-you-avoid-small-string-optimization-sso-pitfalls) <span class="expert">Expert</span>
42. [How do you use `std::filesystem` to traverse directories?](#q42-how-do-you-use-std::filesystem-to-traverse-directories) <span class="beginner">Beginner</span>
43. [How do you use `std::visit` with `std::variant`?](#q43-how-do-you-use-std::visit-with-std::variant) <span class="intermediate">Intermediate</span>
44. [How do you implement a thread-safe Singleton in C++11?](#q44-how-do-you-implement-a-thread-safe-singleton-in-c++11) <span class="intermediate">Intermediate</span>
45. [How do you use `std::format` (C++20) for string formatting?](#q45-how-do-you-use-std::format-c++20-for-string-formatting) <span class="beginner">Beginner</span>
46. [How do you use `std::source_location` for logging?](#q46-how-do-you-use-std::source_location-for-logging) <span class="intermediate">Intermediate</span>
47. [How do you implement the Factory Pattern with unique_ptr?](#q47-how-do-you-implement-the-factory-pattern-with-unique_ptr) <span class="intermediate">Intermediate</span>
48. [How do you use `std::bit_cast` for type punning?](#q48-how-do-you-use-std::bit_cast-for-type-punning) <span class="advanced">Advanced</span>
49. [How do you use `std::latch` for thread synchronization?](#q49-how-do-you-use-std::latch-for-thread-synchronization) <span class="intermediate">Intermediate</span>
50. [How do you detect memory leaks with Valgrind?](#q50-how-do-you-detect-memory-leaks-with-valgrind) <span class="beginner">Beginner</span>
51. [How do you handle C++ state management in large scale applications?](#q51-how-do-you-handle-c++-state-management-in-large-scale-applications) <span class="advanced">Advanced</span>
52. [How do you perform C++ data validation in microservices?](#q52-how-do-you-perform-c++-data-validation-in-microservices) <span class="beginner">Beginner</span>
53. [How do you automate C++ deployment for mobile devices?](#q53-how-do-you-automate-c++-deployment-for-mobile-devices) <span class="advanced">Advanced</span>
54. [How do you handle C++ concurrency issues in legacy systems?](#q54-how-do-you-handle-c++-concurrency-issues-in-legacy-systems) <span class="advanced">Advanced</span>
55. [How do you implement C++ caching in cloud infrastructure?](#q55-how-do-you-implement-c++-caching-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
56. [How do you manage C++ configuration for real-time systems?](#q56-how-do-you-manage-c++-configuration-for-real-time-systems) <span class="beginner">Beginner</span>
57. [How do you handle C++ internationalization (i18n) in distributed systems?](#q57-how-do-you-handle-c++-internationalization-i18n-in-distributed-systems) <span class="intermediate">Intermediate</span>
58. [How do you ensure C++ accessibility (a11y) in high-traffic sites?](#q58-how-do-you-ensure-c++-accessibility-a11y-in-high-traffic-sites) <span class="beginner">Beginner</span>
59. [How do you optimize C++ network requests in embedded systems?](#q59-how-do-you-optimize-c++-network-requests-in-embedded-systems) <span class="advanced">Advanced</span>
60. [How do you handle C++ performance optimization for production environments?](#q60-how-do-you-handle-c++-performance-optimization-for-production-environments) <span class="advanced">Advanced</span>
61. [What are the security implications of C++ in large scale applications?](#q61-what-are-the-security-implications-of-c++-in-large-scale-applications) <span class="intermediate">Intermediate</span>
62. [How do you debug C++ memory leaks in microservices?](#q62-how-do-you-debug-c++-memory-leaks-in-microservices) <span class="advanced">Advanced</span>
63. [Best practices for C++ code organization in mobile devices?](#q63-best-practices-for-c++-code-organization-in-mobile-devices) <span class="beginner">Beginner</span>
64. [How do you implement C++ error handling for legacy systems?](#q64-how-do-you-implement-c++-error-handling-for-legacy-systems) <span class="intermediate">Intermediate</span>
65. [How do you test C++ functionality in cloud infrastructure?](#q65-how-do-you-test-c++-functionality-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
66. [How do you handle C++ state management in real-time systems?](#q66-how-do-you-handle-c++-state-management-in-real-time-systems) <span class="advanced">Advanced</span>
67. [How do you perform C++ data validation in distributed systems?](#q67-how-do-you-perform-c++-data-validation-in-distributed-systems) <span class="beginner">Beginner</span>
68. [How do you automate C++ deployment for high-traffic sites?](#q68-how-do-you-automate-c++-deployment-for-high-traffic-sites) <span class="advanced">Advanced</span>
69. [How do you handle C++ concurrency issues in embedded systems?](#q69-how-do-you-handle-c++-concurrency-issues-in-embedded-systems) <span class="advanced">Advanced</span>
70. [How do you implement C++ caching in production environments?](#q70-how-do-you-implement-c++-caching-in-production-environments) <span class="intermediate">Intermediate</span>
71. [How do you manage C++ configuration for large scale applications?](#q71-how-do-you-manage-c++-configuration-for-large-scale-applications) <span class="beginner">Beginner</span>
72. [How do you handle C++ internationalization (i18n) in microservices?](#q72-how-do-you-handle-c++-internationalization-i18n-in-microservices) <span class="intermediate">Intermediate</span>
73. [How do you ensure C++ accessibility (a11y) in mobile devices?](#q73-how-do-you-ensure-c++-accessibility-a11y-in-mobile-devices) <span class="beginner">Beginner</span>
74. [How do you optimize C++ network requests in legacy systems?](#q74-how-do-you-optimize-c++-network-requests-in-legacy-systems) <span class="advanced">Advanced</span>
75. [How do you handle C++ performance optimization for cloud infrastructure?](#q75-how-do-you-handle-c++-performance-optimization-for-cloud-infrastructure) <span class="advanced">Advanced</span>
76. [What are the security implications of C++ in real-time systems?](#q76-what-are-the-security-implications-of-c++-in-real-time-systems) <span class="intermediate">Intermediate</span>
77. [How do you debug C++ memory leaks in distributed systems?](#q77-how-do-you-debug-c++-memory-leaks-in-distributed-systems) <span class="advanced">Advanced</span>
78. [Best practices for C++ code organization in high-traffic sites?](#q78-best-practices-for-c++-code-organization-in-high-traffic-sites) <span class="beginner">Beginner</span>
79. [How do you implement C++ error handling for embedded systems?](#q79-how-do-you-implement-c++-error-handling-for-embedded-systems) <span class="intermediate">Intermediate</span>
80. [How do you test C++ functionality in production environments?](#q80-how-do-you-test-c++-functionality-in-production-environments) <span class="intermediate">Intermediate</span>
81. [How do you handle C++ state management in large scale applications?](#q81-how-do-you-handle-c++-state-management-in-large-scale-applications) <span class="advanced">Advanced</span>
82. [How do you perform C++ data validation in microservices?](#q82-how-do-you-perform-c++-data-validation-in-microservices) <span class="beginner">Beginner</span>
83. [How do you automate C++ deployment for mobile devices?](#q83-how-do-you-automate-c++-deployment-for-mobile-devices) <span class="advanced">Advanced</span>
84. [How do you handle C++ concurrency issues in legacy systems?](#q84-how-do-you-handle-c++-concurrency-issues-in-legacy-systems) <span class="advanced">Advanced</span>
85. [How do you implement C++ caching in cloud infrastructure?](#q85-how-do-you-implement-c++-caching-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
86. [How do you manage C++ configuration for real-time systems?](#q86-how-do-you-manage-c++-configuration-for-real-time-systems) <span class="beginner">Beginner</span>
87. [How do you handle C++ internationalization (i18n) in distributed systems?](#q87-how-do-you-handle-c++-internationalization-i18n-in-distributed-systems) <span class="intermediate">Intermediate</span>
88. [How do you ensure C++ accessibility (a11y) in high-traffic sites?](#q88-how-do-you-ensure-c++-accessibility-a11y-in-high-traffic-sites) <span class="beginner">Beginner</span>
89. [How do you optimize C++ network requests in embedded systems?](#q89-how-do-you-optimize-c++-network-requests-in-embedded-systems) <span class="advanced">Advanced</span>
90. [How do you handle C++ performance optimization for production environments?](#q90-how-do-you-handle-c++-performance-optimization-for-production-environments) <span class="advanced">Advanced</span>
91. [What are the security implications of C++ in large scale applications?](#q91-what-are-the-security-implications-of-c++-in-large-scale-applications) <span class="intermediate">Intermediate</span>
92. [How do you debug C++ memory leaks in microservices?](#q92-how-do-you-debug-c++-memory-leaks-in-microservices) <span class="advanced">Advanced</span>
93. [Best practices for C++ code organization in mobile devices?](#q93-best-practices-for-c++-code-organization-in-mobile-devices) <span class="beginner">Beginner</span>
94. [How do you implement C++ error handling for legacy systems?](#q94-how-do-you-implement-c++-error-handling-for-legacy-systems) <span class="intermediate">Intermediate</span>
95. [How do you test C++ functionality in cloud infrastructure?](#q95-how-do-you-test-c++-functionality-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
96. [How do you handle C++ state management in real-time systems?](#q96-how-do-you-handle-c++-state-management-in-real-time-systems) <span class="advanced">Advanced</span>
97. [How do you perform C++ data validation in distributed systems?](#q97-how-do-you-perform-c++-data-validation-in-distributed-systems) <span class="beginner">Beginner</span>
98. [How do you automate C++ deployment for high-traffic sites?](#q98-how-do-you-automate-c++-deployment-for-high-traffic-sites) <span class="advanced">Advanced</span>
99. [How do you handle C++ concurrency issues in embedded systems?](#q99-how-do-you-handle-c++-concurrency-issues-in-embedded-systems) <span class="advanced">Advanced</span>
100. [How do you implement C++ caching in production environments?](#q100-how-do-you-implement-c++-caching-in-production-environments) <span class="intermediate">Intermediate</span>

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


---

### Q31: How do you use C++20 Concepts to constrain template parameters?

**Difficulty**: Intermediate

**Strategy:**
Concepts allow you to specify requirements on template arguments, producing more readable error messages and enabling overloading based on properties. Use the `requires` clause or shorthand syntax.

**Code Example:**
```cpp
#include <concepts>
#include <iostream>

// Constrain T to be an integral type
template <std::integral T>
T add(T a, T b) {
    return a + b;
}

// Custom concept
template <typename T>
concept Hashable = requires(T a) {
    { std::hash<T>{}(a) } -> std::convertible_to<std::size_t>;
};

void process(Hashable auto const& item) {
    std::cout << "Processing hashable item\n";
}

int main() {
    std::cout << add(5, 10) << "\n";
    // add(5.5, 1.2); // Compile error: double is not integral
    
    process(10); // int is hashable
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q32: How do you use `std::jthread` (C++20) for automatic joining?

**Difficulty**: Beginner

**Strategy:**
`std::jthread` is a wrapper around `std::thread` that automatically joins on destruction and supports cooperative interruption via `std::stop_token`.

**Code Example:**
```cpp
#include <thread>
#include <iostream>
#include <chrono>

void worker(std::stop_token stoken) {
    while (!stoken.stop_requested()) {
        std::cout << "Working...\n";
        std::this_thread::sleep_for(std::chrono::milliseconds(500));
    }
    std::cout << "Worker stopped.\n";
}

int main() {
    // jthread automatically joins when it goes out of scope
    std::jthread t(worker);
    
    std::this_thread::sleep_for(std::chrono::seconds(2));
    // t destructor calls request_stop() and join()
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q33: How do you use the C++20 Ranges library for pipeline operations?

**Difficulty**: Intermediate

**Strategy:**
Ranges allow you to compose algorithms using the pipe operator (`|`). This creates lazy, readable sequences of operations without creating intermediate containers.

**Code Example:**
```cpp
#include <iostream>
#include <vector>
#include <ranges>
#include <algorithm>

int main() {
    std::vector<int> nums = {1, 2, 3, 4, 5, 6};

    // Filter even numbers, square them, and take the first 2
    auto result = nums 
        | std::views::filter([](int n) { return n % 2 == 0; }) 
        | std::views::transform([](int n) { return n * n; })
        | std::views::take(2);

    for (int n : result) {
        std::cout << n << " "; // Output: 4 16
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q34: How do you implement the Observer pattern using `std::function`?

**Difficulty**: Advanced

**Strategy:**
Use `std::vector<std::function<void()>>` to store listeners. This avoids inheritance hierarchies for observers and allows lambdas to be used as callbacks.

**Code Example:**
```cpp
#include <iostream>
#include <vector>
#include <functional>

class Subject {
    std::vector<std::function<void(int)>> observers;
    int state;

public:
    void attach(std::function<void(int)> observer) {
        observers.push_back(observer);
    }

    void setState(int s) {
        state = s;
        notify();
    }

    void notify() {
        for (const auto& obs : observers) {
            obs(state);
        }
    }
};

int main() {
    Subject subj;
    
    subj.attach([](int s) { std::cout << "Observer 1: " << s << "\n"; });
    subj.attach([](int s) { std::cout << "Observer 2: " << s * 2 << "\n"; });
    
    subj.setState(5);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q35: How do you use `std::span` (C++20) to pass contiguous memory safely?

**Difficulty**: Intermediate

**Strategy:**
`std::span` is a non-owning view over a contiguous sequence (array, vector, C-array). It provides bounds safety and avoids decaying pointers, without copying data.

**Code Example:**
```cpp
#include <span>
#include <iostream>
#include <vector>

void print_span(std::span<int> data) {
    for (int i : data) {
        std::cout << i << " ";
    }
    std::cout << "\n";
}

int main() {
    int arr[] = {1, 2, 3};
    std::vector<int> vec = {4, 5, 6};

    print_span(arr); // Works with C-array
    print_span(vec); // Works with std::vector
    
    // Sub-span
    print_span(std::span{vec}.subspan(1)); // Output: 5 6
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q36: How do you use `std::atomic_flag` for a spinlock?

**Difficulty**: Advanced

**Strategy:**
`std::atomic_flag` is the only atomic type guaranteed to be lock-free. It can be used to implement a simple spinlock for short critical sections.

**Code Example:**
```cpp
#include <atomic>
#include <thread>
#include <iostream>
#include <vector>

std::atomic_flag lock = ATOMIC_FLAG_INIT;

void critical_section(int id) {
    while (lock.test_and_set(std::memory_order_acquire)) {
        // Spin
    }
    
    std::cout << "Thread " << id << " inside\n";
    
    lock.clear(std::memory_order_release);
}

int main() {
    std::vector<std::thread> threads;
    for (int i = 0; i < 5; ++i) {
        threads.emplace_back(critical_section, i);
    }
    for (auto& t : threads) t.join();
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q37: How do you perform compile-time string hashing?

**Difficulty**: Advanced

**Strategy:**
Use `constexpr` functions to compute hashes at compile time. This allows strings to be used in switch statements (conceptually) or for optimized lookups.

**Code Example:**
```cpp
#include <iostream>

constexpr unsigned int hash(const char* str, int h = 0) {
    return !str[h] ? 5381 : (hash(str, h+1) * 33) ^ str[h];
}

int main() {
    constexpr auto h1 = hash("hello");
    constexpr auto h2 = hash("world");
    
    // Static assert proves it runs at compile time
    static_assert(h1 != h2, "Hashes should differ");
    
    std::cout << "Hash of hello: " << h1 << "\n";
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q38: How do you use `std::any` to store values of any type?

**Difficulty**: Intermediate

**Strategy:**
`std::any` (C++17) is a type-safe container for single values of any type. Use `std::any_cast` to retrieve the value safely.

**Code Example:**
```cpp
#include <any>
#include <iostream>
#include <string>

int main() {
    std::any a = 10;
    std::cout << std::any_cast<int>(a) << "\n"; // 10

    a = std::string("Hello");
    
    try {
        std::cout << std::any_cast<std::string>(a) << "\n";
        // std::cout << std::any_cast<int>(a) << "\n"; // Throws bad_any_cast
    } catch (const std::bad_any_cast& e) {
        std::cout << e.what() << "\n";
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q39: How do you implement the Pimpl (Pointer to Implementation) idiom?

**Difficulty**: Advanced

**Strategy:**
Move private members to a separate struct defined in the .cpp file. The main class holds a `std::unique_ptr` to this struct. This reduces compilation dependencies and hides implementation details.

**Code Example:**
```cpp
// Widget.h
#include <memory>

class Widget {
public:
    Widget();
    ~Widget(); // Must be defined in .cpp where Impl is complete
    void doSomething();
    
private:
    struct Impl;
    std::unique_ptr<Impl> pImpl;
};

// Widget.cpp
#include "Widget.h"
#include <iostream>

struct Widget::Impl {
    void work() { std::cout << "Implementation working...\n"; }
};

Widget::Widget() : pImpl(std::make_unique<Impl>()) {}
Widget::~Widget() = default;
void Widget::doSomething() { pImpl->work(); }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q40: How do you use `std::reduce` for parallel accumulation?

**Difficulty**: Advanced

**Strategy:**
`std::reduce` (C++17) is similar to `std::accumulate` but supports out-of-order execution, enabling parallelization via execution policies (C++17).

**Code Example:**
```cpp
#include <numeric>
#include <vector>
#include <execution>
#include <iostream>

int main() {
    std::vector<int> v(1000000, 1);

    // Parallel reduction
    int sum = std::reduce(std::execution::par, v.begin(), v.end());

    std::cout << "Sum: " << sum << "\n";
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q41: How do you avoid Small String Optimization (SSO) pitfalls?

**Difficulty**: Expert

**Strategy:**
SSO stores small strings directly in the `std::string` object to avoid allocation. Be aware that moving a string might invalidate iterators pointing to the internal buffer if the string is small (implementation dependent, but generally safe in standard, though pointers to buffer might change location if object moves).

**Code Example:**
```cpp
#include <iostream>
#include <string>

int main() {
    // Small string (fits in SSO buffer)
    std::string s1 = "short"; 
    const char* ptr1 = s1.data();
    
    // Move s1 to s2
    std::string s2 = std::move(s1);
    
    // ptr1 is likely dangling or pointing to s2's buffer now
    // Unlike heap-allocated strings, the data physically moved location
    std::cout << "Pointer address changed: " << (void*)s2.data() << " vs " << (void*)ptr1 << "\n";
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q42: How do you use `std::filesystem` to traverse directories?

**Difficulty**: Beginner

**Strategy:**
Use `std::filesystem::recursive_directory_iterator` to walk through a directory tree. It's part of C++17 standard library.

**Code Example:**
```cpp
#include <filesystem>
#include <iostream>

namespace fs = std::filesystem;

int main() {
    // Create dummy dir for demo
    fs::create_directory("sandbox");
    fs::create_directory("sandbox/subdir");
    
    for (const auto& entry : fs::recursive_directory_iterator("sandbox")) {
        std::cout << entry.path() << "\n";
    }
    
    fs::remove_all("sandbox");
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q43: How do you use `std::visit` with `std::variant`?

**Difficulty**: Intermediate

**Strategy:**
`std::visit` applies a callable (visitor) to the value currently held by a `std::variant`. You can use a struct with overloaded `operator()` or the `overloaded` helper pattern with lambdas.

**Code Example:**
```cpp
#include <variant>
#include <iostream>

// Helper for overloaded lambdas
template<class... Ts> struct overloaded : Ts... { using Ts::operator()...; };
template<class... Ts> overloaded(Ts...) -> overloaded<Ts...>;

int main() {
    std::variant<int, float, std::string> v = "Hello";

    std::visit(overloaded {
        [](int arg) { std::cout << "Int: " << arg << "\n"; },
        [](float arg) { std::cout << "Float: " << arg << "\n"; },
        [](const std::string& arg) { std::cout << "String: " << arg << "\n"; }
    }, v);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q44: How do you implement a thread-safe Singleton in C++11?

**Difficulty**: Intermediate

**Strategy:**
In C++11, static local variables are guaranteed to be initialized in a thread-safe manner. This is the 'Meyers Singleton'.

**Code Example:**
```cpp
class Singleton {
public:
    static Singleton& getInstance() {
        static Singleton instance; // Thread-safe initialization
        return instance;
    }
    
    void doWork() {}

private:
    Singleton() {}
    Singleton(const Singleton&) = delete;
    void operator=(const Singleton&) = delete;
};

int main() {
    Singleton::getInstance().doWork();
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q45: How do you use `std::format` (C++20) for string formatting?

**Difficulty**: Beginner

**Strategy:**
`std::format` provides a type-safe, python-like string formatting alternative to `printf` and `iostreams`. It is faster and more readable.

**Code Example:**
```cpp
#include <format>
#include <iostream>
#include <string>

int main() {
    std::string name = "Alice";
    int age = 30;
    
    std::string s = std::format("User {} is {} years old.", name, age);
    std::cout << s << "\n";
    
    // Format specifiers
    std::cout << std::format("Pi: {:.2f}", 3.14159) << "\n"; // 3.14
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q46: How do you use `std::source_location` for logging?

**Difficulty**: Intermediate

**Strategy:**
`std::source_location` (C++20) captures file name, line number, and function name at the call site. It replaces preprocessor macros like `__FILE__` and `__LINE__`.

**Code Example:**
```cpp
#include <source_location>
#include <iostream>

void log(const char* message, 
         const std::source_location location = std::source_location::current()) {
    std::cout << "INFO: " << message << "\n"
              << "File: " << location.file_name() << "\n"
              << "Line: " << location.line() << "\n"
              << "Func: " << location.function_name() << "\n";
}

int main() {
    log("Application started");
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q47: How do you implement the Factory Pattern with unique_ptr?

**Difficulty**: Intermediate

**Strategy:**
A factory function should return `std::unique_ptr<Base>` to transfer ownership to the caller. This ensures proper cleanup without manual `delete`.

**Code Example:**
```cpp
#include <memory>
#include <iostream>

class Animal {
public:
    virtual void speak() = 0;
    virtual ~Animal() = default;
};

class Dog : public Animal {
    void speak() override { std::cout << "Woof!\n"; }
};

class Cat : public Animal {
    void speak() override { std::cout << "Meow!\n"; }
};

std::unique_ptr<Animal> createAnimal(const std::string& type) {
    if (type == "dog") return std::make_unique<Dog>();
    if (type == "cat") return std::make_unique<Cat>();
    return nullptr;
}

int main() {
    auto pet = createAnimal("dog");
    if (pet) pet->speak();
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q48: How do you use `std::bit_cast` for type punning?

**Difficulty**: Advanced

**Strategy:**
`std::bit_cast` (C++20) safely reinterprets the bits of a value as another type of the same size. It is the only undefined-behavior-free way to do type punning (unlike `reinterpret_cast` or unions).

**Code Example:**
```cpp
#include <bit>
#include <iostream>
#include <cstdint>

int main() {
    float f = 3.14f;
    
    // View bits of float as uint32_t
    uint32_t i = std::bit_cast<uint32_t>(f);
    
    std::cout << std::hex << i << "\n";
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q49: How do you use `std::latch` for thread synchronization?

**Difficulty**: Intermediate

**Strategy:**
`std::latch` (C++20) is a downward counter. Threads wait until the counter reaches zero. Unlike `std::barrier`, it cannot be reused.

**Code Example:**
```cpp
#include <latch>
#include <thread>
#include <vector>
#include <iostream>

std::latch work_done(3);

void worker(int id) {
    std::cout << "Worker " << id << " done\n";
    work_done.count_down();
}

int main() {
    std::vector<std::thread> threads;
    for(int i=0; i<3; ++i) threads.emplace_back(worker, i);
    
    work_done.wait(); // Wait for all 3
    std::cout << "All workers finished\n";
    
    for(auto& t : threads) t.join();
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q50: How do you detect memory leaks with Valgrind?

**Difficulty**: Beginner

**Strategy:**
Valgrind is a command-line tool. Run your executable with `valgrind --leak-check=full ./program`. It reports memory that was allocated but not freed.

**Code Example:**
```cpp
// Compile: g++ -g main.cpp -o main
// Run: valgrind --leak-check=full ./main

#include <iostream>

void leak() {
    int* p = new int[10];
    p[0] = 5;
    // Missing delete[] p;
}

int main() {
    leak();
    return 0;
}

/* Valgrind Output Snippet:
==12345== 40 bytes in 1 blocks are definitely lost in loss record 1 of 1
==12345==    at 0x4C2E80F: operator new[](unsigned long) (in /usr/lib/valgrind/...)
==12345==    by 0x4006F6: leak() (main.cpp:7)
*/
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

### Q51: How do you handle C++ state management in large scale applications?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```cpp
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q52: How do you perform C++ data validation in microservices?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```cpp
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q53: How do you automate C++ deployment for mobile devices?

**Difficulty**: Advanced

**Strategy**:
Use CI/CD pipelines. Dockerize the application. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```cpp
steps:
  - run: npm test
  - run: docker build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q54: How do you handle C++ concurrency issues in legacy systems?

**Difficulty**: Advanced

**Strategy**:
Use locks, queues, or atomic operations. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```cpp
await mutex.runExclusive(async () => {
  // critical section
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q55: How do you implement C++ caching in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Use Redis or in-memory LRU caches. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```cpp
const cache = new Map();
if (cache.has(key)) return cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q56: How do you manage C++ configuration for real-time systems?

**Difficulty**: Beginner

**Strategy**:
Use environment variables or config files. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```cpp
const config = process.env.CONFIG || 'default';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q57: How do you handle C++ internationalization (i18n) in distributed systems?

**Difficulty**: Intermediate

**Strategy**:
Use i18n libraries. Extract strings to resource files.

**Code Example**:
```cpp
t('welcome_message')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q58: How do you ensure C++ accessibility (a11y) in high-traffic sites?

**Difficulty**: Beginner

**Strategy**:
Use semantic HTML and ARIA roles. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```cpp
<button aria-label="Close">X</button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q59: How do you optimize C++ network requests in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use batching, debouncing, or GraphQL. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```cpp
debounce(() => fetch(), 300);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q60: How do you handle C++ performance optimization for production environments?

**Difficulty**: Advanced

**Strategy**:
Profile first, then optimize hot paths. Use caching and efficient algorithms.

**Code Example**:
```cpp
const start = performance.now();
// C++ logic
const end = performance.now();
console.log('Time:', end - start);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q61: What are the security implications of C++ in large scale applications?

**Difficulty**: Intermediate

**Strategy**:
Validate all inputs. Sanitize data. Use least privilege principle.

**Code Example**:
```cpp
// Sanitize input
const clean = input.replace(/<script>/g, '');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q62: How do you debug C++ memory leaks in microservices?

**Difficulty**: Advanced

**Strategy**:
Use heap snapshots and look for detached DOM nodes or uncleared listeners.

**Code Example**:
```cpp
// Check listeners
process.on('exit', () => cleanup());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q63: Best practices for C++ code organization in mobile devices?

**Difficulty**: Beginner

**Strategy**:
Follow SOLID principles. Keep functions small and focused.

**Code Example**:
```cpp
// Single responsibility
function doOneThing() { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q64: How do you implement C++ error handling for legacy systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```cpp
try {
  await C++Operation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q65: How do you test C++ functionality in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```cpp
test('C++ works', () => {
  expect(C++()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q66: How do you handle C++ state management in real-time systems?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```cpp
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q67: How do you perform C++ data validation in distributed systems?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```cpp
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q68: How do you automate C++ deployment for high-traffic sites?

**Difficulty**: Advanced

**Strategy**:
Use CI/CD pipelines. Dockerize the application. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```cpp
steps:
  - run: npm test
  - run: docker build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q69: How do you handle C++ concurrency issues in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use locks, queues, or atomic operations. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```cpp
await mutex.runExclusive(async () => {
  // critical section
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q70: How do you implement C++ caching in production environments?

**Difficulty**: Intermediate

**Strategy**:
Use Redis or in-memory LRU caches. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```cpp
const cache = new Map();
if (cache.has(key)) return cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q71: How do you manage C++ configuration for large scale applications?

**Difficulty**: Beginner

**Strategy**:
Use environment variables or config files. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```cpp
const config = process.env.CONFIG || 'default';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q72: How do you handle C++ internationalization (i18n) in microservices?

**Difficulty**: Intermediate

**Strategy**:
Use i18n libraries. Extract strings to resource files.

**Code Example**:
```cpp
t('welcome_message')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q73: How do you ensure C++ accessibility (a11y) in mobile devices?

**Difficulty**: Beginner

**Strategy**:
Use semantic HTML and ARIA roles. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```cpp
<button aria-label="Close">X</button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q74: How do you optimize C++ network requests in legacy systems?

**Difficulty**: Advanced

**Strategy**:
Use batching, debouncing, or GraphQL. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```cpp
debounce(() => fetch(), 300);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q75: How do you handle C++ performance optimization for cloud infrastructure?

**Difficulty**: Advanced

**Strategy**:
Profile first, then optimize hot paths. Use caching and efficient algorithms.

**Code Example**:
```cpp
const start = performance.now();
// C++ logic
const end = performance.now();
console.log('Time:', end - start);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q76: What are the security implications of C++ in real-time systems?

**Difficulty**: Intermediate

**Strategy**:
Validate all inputs. Sanitize data. Use least privilege principle.

**Code Example**:
```cpp
// Sanitize input
const clean = input.replace(/<script>/g, '');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q77: How do you debug C++ memory leaks in distributed systems?

**Difficulty**: Advanced

**Strategy**:
Use heap snapshots and look for detached DOM nodes or uncleared listeners.

**Code Example**:
```cpp
// Check listeners
process.on('exit', () => cleanup());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q78: Best practices for C++ code organization in high-traffic sites?

**Difficulty**: Beginner

**Strategy**:
Follow SOLID principles. Keep functions small and focused.

**Code Example**:
```cpp
// Single responsibility
function doOneThing() { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q79: How do you implement C++ error handling for embedded systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```cpp
try {
  await C++Operation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q80: How do you test C++ functionality in production environments?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```cpp
test('C++ works', () => {
  expect(C++()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q81: How do you handle C++ state management in large scale applications?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```cpp
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q82: How do you perform C++ data validation in microservices?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```cpp
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q83: How do you automate C++ deployment for mobile devices?

**Difficulty**: Advanced

**Strategy**:
Use CI/CD pipelines. Dockerize the application. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```cpp
steps:
  - run: npm test
  - run: docker build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q84: How do you handle C++ concurrency issues in legacy systems?

**Difficulty**: Advanced

**Strategy**:
Use locks, queues, or atomic operations. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```cpp
await mutex.runExclusive(async () => {
  // critical section
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q85: How do you implement C++ caching in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Use Redis or in-memory LRU caches. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```cpp
const cache = new Map();
if (cache.has(key)) return cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q86: How do you manage C++ configuration for real-time systems?

**Difficulty**: Beginner

**Strategy**:
Use environment variables or config files. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```cpp
const config = process.env.CONFIG || 'default';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q87: How do you handle C++ internationalization (i18n) in distributed systems?

**Difficulty**: Intermediate

**Strategy**:
Use i18n libraries. Extract strings to resource files.

**Code Example**:
```cpp
t('welcome_message')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q88: How do you ensure C++ accessibility (a11y) in high-traffic sites?

**Difficulty**: Beginner

**Strategy**:
Use semantic HTML and ARIA roles. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```cpp
<button aria-label="Close">X</button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q89: How do you optimize C++ network requests in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use batching, debouncing, or GraphQL. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```cpp
debounce(() => fetch(), 300);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q90: How do you handle C++ performance optimization for production environments?

**Difficulty**: Advanced

**Strategy**:
Profile first, then optimize hot paths. Use caching and efficient algorithms.

**Code Example**:
```cpp
const start = performance.now();
// C++ logic
const end = performance.now();
console.log('Time:', end - start);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q91: What are the security implications of C++ in large scale applications?

**Difficulty**: Intermediate

**Strategy**:
Validate all inputs. Sanitize data. Use least privilege principle.

**Code Example**:
```cpp
// Sanitize input
const clean = input.replace(/<script>/g, '');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q92: How do you debug C++ memory leaks in microservices?

**Difficulty**: Advanced

**Strategy**:
Use heap snapshots and look for detached DOM nodes or uncleared listeners.

**Code Example**:
```cpp
// Check listeners
process.on('exit', () => cleanup());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q93: Best practices for C++ code organization in mobile devices?

**Difficulty**: Beginner

**Strategy**:
Follow SOLID principles. Keep functions small and focused.

**Code Example**:
```cpp
// Single responsibility
function doOneThing() { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q94: How do you implement C++ error handling for legacy systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```cpp
try {
  await C++Operation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q95: How do you test C++ functionality in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```cpp
test('C++ works', () => {
  expect(C++()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q96: How do you handle C++ state management in real-time systems?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```cpp
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q97: How do you perform C++ data validation in distributed systems?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```cpp
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q98: How do you automate C++ deployment for high-traffic sites?

**Difficulty**: Advanced

**Strategy**:
Use CI/CD pipelines. Dockerize the application. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```cpp
steps:
  - run: npm test
  - run: docker build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q99: How do you handle C++ concurrency issues in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use locks, queues, or atomic operations. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```cpp
await mutex.runExclusive(async () => {
  // critical section
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q100: How do you implement C++ caching in production environments?

**Difficulty**: Intermediate

**Strategy**:
Use Redis or in-memory LRU caches. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```cpp
const cache = new Map();
if (cache.has(key)) return cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---
