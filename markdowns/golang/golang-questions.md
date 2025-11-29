# Golang Interview Questions

## Table of Contents

1. [Q1: What is Go (Golang) and what are its key features?](#q1-what-is-go-golang-and-what-are-its-key-features)
2. [Q2: What are Goroutines?](#q2-what-are-goroutines)
3. [Q3: What are Channels?](#q3-what-are-channels)
4. [Q4: Explain the `defer` keyword.](#q4-explain-the-defer-keyword)
5. [Q5: What is the difference between Arrays and Slices?](#q5-what-is-the-difference-between-arrays-and-slices)
6. [Q6: How does Error Handling work in Go?](#q6-how-does-error-handling-work-in-go)
7. [Q7: What are Interfaces in Go?](#q7-what-are-interfaces-in-go)
8. [Q8: Explain the difference between `make` and `new`.](#q8-explain-the-difference-between-make-and-new)
9. [Q9: What is the `select` statement?](#q9-what-is-the-select-statement)
10. [Q10: What is the difference between Buffered and Unbuffered channels?](#q10-what-is-the-difference-between-buffered-and-unbuffered-channels)
11. [Q11: Explain `panic` and `recover`.](#q11-explain-panic-and-recover)
12. [Q12: How do you implement inheritance in Go?](#q12-how-do-you-implement-inheritance-in-go)
13. [Q13: What is the `context` package used for?](#q13-what-is-the-context-package-used-for)
14. [Q14: What is the `init()` function?](#q14-what-is-the-init-function)
15. [Q15: What are Pointers in Go?](#q15-what-are-pointers-in-go)
16. [Q16: How does Garbage Collection work in Go?](#q16-how-does-garbage-collection-work-in-go)
17. [Q17: What is `GOMAXPROCS`?](#q17-what-is-gomaxprocs)
18. [Q18: What is the difference between a method and a function?](#q18-what-is-the-difference-between-a-method-and-a-function)
19. [Q19: Can you have optional parameters in Go functions?](#q19-can-you-have-optional-parameters-in-go-functions)
20. [Q20: What is a Struct?](#q20-what-is-a-struct)
21. [Q21: What are Variadic Functions?](#q21-what-are-variadic-functions)
22. [Q22: What is the difference between Exported and Unexported names?](#q22-what-is-the-difference-between-exported-and-unexported-names)
23. [Q23: What is a Type Assertion?](#q23-what-is-a-type-assertion)
24. [Q24: What is a Type Switch?](#q24-what-is-a-type-switch)
25. [Q25: What is the `Stringer` interface?](#q25-what-is-the-stringer-interface)
26. [Q26: What is `iota`?](#q26-what-is-iota)
27. [Q27: What are Struct Tags?](#q27-what-are-struct-tags)
28. [Q28: How do you Marshal and Unmarshal JSON?](#q28-how-do-you-marshal-and-unmarshal-json)
29. [Q29: Are Maps concurrent safe?](#q29-are-maps-concurrent-safe)
30. [Q30: What is `sync.Mutex`?](#q30-what-is-syncmutex)
31. [Q31: What is `sync.WaitGroup`?](#q31-what-is-syncwaitgroup)
32. [Q32: How do you detect Race Conditions?](#q32-how-do-you-detect-race-conditions)
33. [Q33: What are Go Modules?](#q33-what-are-go-modules)
34. [Q34: What is the difference between `go.mod` and `go.sum`?](#q34-what-is-the-difference-between-gomod-and-gosum)
35. [Q35: What is the `internal` package?](#q35-what-is-the-internal-package)
36. [Q36: What is the `vendor` directory?](#q36-what-is-the-vendor-directory)
37. [Q37: How does Cross-Compilation work in Go?](#q37-how-does-cross-compilation-work-in-go)
38. [Q38: What are Generics in Go?](#q38-what-are-generics-in-go)
39. [Q39: What is the `comparable` constraint?](#q39-what-is-the-comparable-constraint)
40. [Q40: What is the `any` type?](#q40-what-is-the-any-type)
41. [Q41: Difference between Slice Length and Capacity?](#q41-difference-between-slice-length-and-capacity)
42. [Q42: Difference between `nil` slice and empty slice?](#q42-difference-between-nil-slice-and-empty-slice)
43. [Q43: How do you copy a slice?](#q43-how-do-you-copy-a-slice)
44. [Q44: How do you delete an element from a Map?](#q44-how-do-you-delete-an-element-from-a-map)
45. [Q45: Is Map iteration order guaranteed?](#q45-is-map-iteration-order-guaranteed)
46. [Q46: How are Structs compared?](#q46-how-are-structs-compared)
47. [Q47: Pointer Receiver vs Value Receiver?](#q47-pointer-receiver-vs-value-receiver)
48. [Q48: Can Interfaces be embedded?](#q48-can-interfaces-be-embedded)
49. [Q49: What are Circular Dependencies and how to avoid them?](#q49-what-are-circular-dependencies-and-how-to-avoid-them)
50. [Q50: Type Alias vs Type Definition?](#q50-type-alias-vs-type-definition)
51. [Q51: What is `reflect.DeepEqual`?](#q51-what-is-reflectdeepequal)
52. [Q52: What is Reflection?](#q52-what-is-reflection)
53. [Q53: What is `sync.Pool`?](#q53-what-is-syncpool)
54. [Q54: What are Atomic Operations?](#q54-what-are-atomic-operations)
55. [Q55: How does Context Cancellation work?](#q55-how-does-context-cancellation-work)
56. [Q56: Pitfalls of using Context Values?](#q56-pitfalls-of-using-context-values)
57. [Q57: What is the Middleware Pattern?](#q57-what-is-the-middleware-pattern)
58. [Q58: What is the `http.Handler` interface?](#q58-what-is-the-httphandler-interface)
59. [Q59: What is `http.ServeMux`?](#q59-what-is-httpservemux)
60. [Q60: What does `omitempty` do in JSON tags?](#q60-what-does-omitempty-do-in-json-tags)
61. [Q61: Does panic propagate across Goroutines?](#q61-does-panic-propagate-across-goroutines)
62. [Q62: What is `runtime.Goexit`?](#q62-what-is-runtimegoexit)
63. [Q63: Common mistake with Closures in Loops?](#q63-common-mistake-with-closures-in-loops)
64. [Q64: What is Escape Analysis?](#q64-what-is-escape-analysis)
65. [Q65: Stack vs Heap memory in Go?](#q65-stack-vs-heap-memory-in-go)
66. [Q66: What is Inlining?](#q66-what-is-inlining)
67. [Q67: What is PGO (Profile Guided Optimization)?](#q67-what-is-pgo-profile-guided-optimization)
68. [Q68: How do you write tests in Go?](#q68-how-do-you-write-tests-in-go)
69. [Q69: What are Table-Driven Tests?](#q69-what-are-table-driven-tests)
70. [Q70: How do you write Benchmarks?](#q70-how-do-you-write-benchmarks)
71. [Q71: What is Fuzzing?](#q71-what-is-fuzzing)
72. [Q72: What are Build Tags?](#q72-what-are-build-tags)
73. [Q73: What is `go generate`?](#q73-what-is-go-generate)
74. [Q74: What is `go vet`?](#q74-what-is-go-vet)
75. [Q75: What is `go fmt`?](#q75-what-is-go-fmt)
76. [Q76: How to use Makefiles with Go?](#q76-how-to-use-makefiles-with-go)
77. [Q77: Best practices for Dockerizing Go apps?](#q77-best-practices-for-dockerizing-go-apps)
78. [Q78: What are Distroless Images?](#q78-what-are-distroless-images)
79. [Q79: gRPC vs REST in Go?](#q79-grpc-vs-rest-in-go)
80. [Q80: What are Protocol Buffers?](#q80-what-are-protocol-buffers)
81. [Q81: How does `sql.DB` handle connections?](#q81-how-does-sqldb-handle-connections)
82. [Q82: How to prevent SQL Injection in Go?](#q82-how-to-prevent-sql-injection-in-go)
83. [Q83: How do you Mock dependencies in tests?](#q83-how-do-you-mock-dependencies-in-tests)
84. [Q84: What is Interface Pollution?](#q84-what-is-interface-pollution)
85. [Q85: What is the Functional Options Pattern?](#q85-what-is-the-functional-options-pattern)
86. [Q86: What is the Builder Pattern in Go?](#q86-what-is-the-builder-pattern-in-go)
87. [Q87: How to implement Singleton Pattern?](#q87-how-to-implement-singleton-pattern)
88. [Q88: What is the Factory Pattern?](#q88-what-is-the-factory-pattern)
89. [Q89: What is the Adapter Pattern?](#q89-what-is-the-adapter-pattern)
90. [Q90: What is the Decorator Pattern?](#q90-what-is-the-decorator-pattern)
91. [Q91: What is the Worker Pool Pattern?](#q91-what-is-the-worker-pool-pattern)
92. [Q92: Explain Fan-out/Fan-in Pattern.](#q92-explain-fan-outfan-in-pattern)
93. [Q93: What is the Pipeline Pattern?](#q93-what-is-the-pipeline-pattern)
94. [Q94: What is the Semaphore Pattern?](#q94-what-is-the-semaphore-pattern)
95. [Q95: How to implement Rate Limiting?](#q95-how-to-implement-rate-limiting)
96. [Q96: How to handle Graceful Shutdown?](#q96-how-to-handle-graceful-shutdown)
97. [Q97: Logging Best Practices?](#q97-logging-best-practices)
98. [Q98: What is Error Wrapping?](#q98-what-is-error-wrapping)
99. [Q99: `errors.Is` vs `errors.As`?](#q99-errorsis-vs-errorsas)
100. [Q100: What is the future of Go?](#q100-what-is-the-future-of-go)

---

## Golang Fundamentals

### Q1: What is Go (Golang) and what are its key features?
**Difficulty: Easy**

**Answer:**
Go is an open-source programming language developed by Google. It is statically typed, compiled, and designed for simplicity and concurrency.
**Key Features:**
- **Simplicity:** Minimalistic syntax.
- **Concurrency:** Built-in support via Goroutines and Channels.
- **Performance:** Compiles to machine code; fast execution.
- **Garbage Collection:** Automatic memory management.
- **Fast Compilation:** Extremely fast build times.

### Q2: What are Goroutines?
**Difficulty: Medium**

**Answer:**
Goroutines are lightweight threads managed by the Go runtime. They are cheaper than OS threads (start with ~2KB stack). You can start a goroutine simply by using the `go` keyword before a function call.
```go
go doSomething()
```

### Q3: What are Channels?
**Difficulty: Medium**

**Answer:**
Channels are the pipes that connect concurrent goroutines. You can send values into channels from one goroutine and receive those values into another goroutine. They provide a way to synchronize execution and communicate data.
```go
ch := make(chan int)
ch <- v    // Send v to channel ch.
v := <-ch  // Receive from ch, and assign value to v.
```

### Q4: Explain the `defer` keyword.
**Difficulty: Easy**

**Answer:**
`defer` schedules a function call to be run after the function completes (returns). It is commonly used for cleanup actions like closing files, unlocking mutexes, or closing database connections. Deferred calls are executed in LIFO (Last In, First Out) order.

### Q5: What is the difference between Arrays and Slices?
**Difficulty: Medium**

**Answer:**
- **Array:** Fixed size. The size is part of the type (e.g., `[5]int`). Value type (assigning copies the entire array).
- **Slice:** Dynamic size. It is a reference to an underlying array. It has three components: pointer to data, length, and capacity. Slices are much more common in Go.

### Q6: How does Error Handling work in Go?
**Difficulty: Easy**

**Answer:**
Go does not have exceptions (like try/catch). Instead, functions return errors as the last return value. The caller is expected to check if the error is `nil`.
```go
file, err := os.Open("filename.txt")
if err != nil {
    log.Fatal(err)
}
```

### Q7: What are Interfaces in Go?
**Difficulty: Medium**

**Answer:**
Interfaces are collections of method signatures. They are implemented *implicitly*. If a type provides definitions for all the methods in an interface, it implements that interface. No `implements` keyword is needed.
Empty interface `interface{}` can hold values of any type.

### Q8: Explain the difference between `make` and `new`.
**Difficulty: Medium**

**Answer:**
- **`new(T)`:** Allocates zeroed storage for a new item of type `T` and returns its address (`*T`). Used for value types (structs, ints).
- **`make(T, args)`:** Creates slices, maps, and channels only. It returns an initialized (not zeroed) value of type `T` (not `*T`). These types require internal initialization.

### Q9: What is the `select` statement?
**Difficulty: Medium**

**Answer:**
`select` lets a goroutine wait on multiple communication operations. It is like a `switch` statement but for channels. It blocks until one of its cases can run, then executes that case. If multiple are ready, it chooses one at random.

### Q10: What is the difference between Buffered and Unbuffered channels?
**Difficulty: Medium**

**Answer:**
- **Unbuffered:** The sender blocks until the receiver receives the value. Synchronous.
- **Buffered:** Has a capacity. The sender only blocks when the buffer is full. The receiver blocks when the buffer is empty.

### Q11: Explain `panic` and `recover`.
**Difficulty: Medium**

**Answer:**
- **`panic`:** Stops the ordinary flow of control and begins panicking. Similar to throwing an exception. It should be used only for unrecoverable errors.
- **`recover`:** Regains control of a panicking goroutine. It is only useful inside deferred functions.

### Q12: How do you implement inheritance in Go?
**Difficulty: Medium**

**Answer:**
Go does not support inheritance (no `extends` keyword). Instead, it uses **Composition** via Struct Embedding.
```go
type Animal struct {
    Name string
}
type Dog struct {
    Animal // Embedded struct
    Breed string
}
```

### Q13: What is the `context` package used for?
**Difficulty: Advanced**

**Answer:**
The `context` package is used to carry deadlines, cancellation signals, and other request-scoped values across API boundaries and between processes (goroutines). It is crucial for managing timeouts and cancellation in concurrent applications.

### Q14: What is the `init()` function?
**Difficulty: Medium**

**Answer:**
`init()` is a special function that executes before the `main()` function. It is used for package initialization (e.g., setting up database connections, verifying env vars). You can have multiple `init` functions per package.

### Q15: What are Pointers in Go?
**Difficulty: Easy**

**Answer:**
A pointer holds the memory address of a value. Go has pointers but no pointer arithmetic (unlike C).
- `&` generates a pointer to its operand.
- `*` dereferences a pointer (accesses the value).

### Q16: How does Garbage Collection work in Go?
**Difficulty: Advanced**

**Answer:**
Go uses a concurrent, tri-color mark-and-sweep garbage collector. It is designed to have very low pause times (sub-millisecond) to be suitable for low-latency network servers.

### Q17: What is `GOMAXPROCS`?
**Difficulty: Advanced**

**Answer:**
`GOMAXPROCS` is a variable (or function `runtime.GOMAXPROCS`) that limits the number of operating system threads that can execute user-level Go code simultaneously. By default, it is equal to the number of logical CPUs.

### Q18: What is the difference between a method and a function?
**Difficulty: Easy**

**Answer:**
- **Function:** Independent block of code.
- **Method:** A function with a *receiver* argument. The receiver allows the function to be associated with a specific type.

### Q19: Can you have optional parameters in Go functions?
**Difficulty: Easy**

**Answer:**
No, Go does not support optional parameters or method overloading. You must pass arguments for all defined parameters. Common workarounds include using a struct as a parameter (config object) or variadic functions (`...Type`).

### Q20: What is a Struct?
**Difficulty: Easy**

**Answer:**
A struct is a typed collection of fields. It is used to group data together to form records.
```go
type Person struct {
    Name string
    Age  int
}
```

### Q21: What are Variadic Functions?
**Difficulty: Easy**

**Answer:**
Variadic functions can accept a variable number of arguments. In the function definition, the last parameter type is preceded by `...`.
```go
func sum(nums ...int) int {
    total := 0
    for _, num := range nums {
        total += num
    }
    return total
}
```

### Q22: What is the difference between Exported and Unexported names?
**Difficulty: Easy**

**Answer:**
In Go, visibility is controlled by capitalization.
- **Exported (Public):** Starts with a capital letter (e.g., `fmt.Println`). Accessible from other packages.
- **Unexported (Private):** Starts with a lowercase letter (e.g., `var myVar`). Accessible only within the same package.

### Q23: What is a Type Assertion?
**Difficulty: Medium**

**Answer:**
A type assertion provides access to an interface's underlying concrete value.
```go
t := i.(T)
```
It asserts that interface `i` holds the concrete type `T` and assigns the underlying value to `t`. If `i` does not hold `T`, the statement triggers a panic. To test safely: `t, ok := i.(T)`.

### Q24: What is a Type Switch?
**Difficulty: Medium**

**Answer:**
A type switch is a construct that permits several type assertions in series. It looks like a regular switch statement, but the cases are types, not values.
```go
switch v := i.(type) {
case int:
    // v is int
case string:
    // v is string
default:
    // ...
}
```

### Q25: What is the `Stringer` interface?
**Difficulty: Easy**

**Answer:**
`Stringer` is a ubiquitous interface defined in the `fmt` package. Types that implement `String()` method can define how they are printed as a string.
```go
type Stringer interface {
    String() string
}
```

### Q26: What is `iota`?
**Difficulty: Easy**

**Answer:**
`iota` is a predeclared identifier representing the untyped integer ordinal number of the current const specification in a (usually parenthesized) `const` declaration. It simplifies creating incrementing constants.
```go
const (
    C0 = iota // 0
    C1        // 1
    C2        // 2
)
```

### Q27: What are Struct Tags?
**Difficulty: Medium**

**Answer:**
Struct tags are small pieces of metadata attached to struct fields. They provide instructions to libraries on how to treat the fields (e.g., for JSON encoding, ORM mapping).
```go
type User struct {
    Name string `json:"name" xml:"name"`
}
```

### Q28: How do you Marshal and Unmarshal JSON?
**Difficulty: Medium**

**Answer:**
The `encoding/json` package is used.
- `json.Marshal(v)`: Converts a Go value to JSON (byte slice).
- `json.Unmarshal(data, v)`: Parses JSON data into a Go value.

### Q29: Are Maps concurrent safe?
**Difficulty: Medium**

**Answer:**
No, built-in maps are not safe for concurrent use. If multiple goroutines read and write to a map simultaneously, it can cause a runtime panic. You must use a `sync.Mutex` or `sync.RWMutex` to lock access, or use `sync.Map` for specific use cases.

### Q30: What is `sync.Mutex`?
**Difficulty: Medium**

**Answer:**
`sync.Mutex` is a mutual exclusion lock. It ensures that only one goroutine can access a critical section of code (usually shared data) at a time.
```go
var mu sync.Mutex
mu.Lock()
// critical section
mu.Unlock()
```

### Q31: What is `sync.WaitGroup`?
**Difficulty: Medium**

**Answer:**
`sync.WaitGroup` is used to wait for a collection of goroutines to finish executing.
1. `Add(n)`: Increments the counter.
2. `Done()`: Decrements the counter (usually deferred).
3. `Wait()`: Blocks until the counter becomes 0.

### Q32: How do you detect Race Conditions?
**Difficulty: Medium**

**Answer:**
Go has a built-in race detector. You can enable it by adding the `-race` flag to your build, run, or test commands.
```bash
go run -race main.go
```

### Q33: What are Go Modules?
**Difficulty: Medium**

**Answer:**
Go Modules are the dependency management solution for Go (introduced in 1.11). They allow you to define project dependencies and versions in a `go.mod` file, replacing the old `GOPATH` workspace approach.

### Q34: What is the difference between `go.mod` and `go.sum`?
**Difficulty: Medium**

**Answer:**
- **`go.mod`**: Defines the module path, go version, and direct/indirect dependencies with semantic versioning.
- **`go.sum`**: Contains the expected cryptographic checksums of the content of specific module versions. It ensures that the dependencies have not been modified.

### Q35: What is the `internal` package?
**Difficulty: Medium**

**Answer:**
Packages named `internal` can only be imported by the code in the tree rooted at the parent of the `internal` directory. It is a mechanism to enforce encapsulation at the package level.

### Q36: What is the `vendor` directory?
**Difficulty: Easy**

**Answer:**
The `vendor` directory contains copies of all the dependency packages used by the project. It ensures reproducible builds without relying on external repositories being online. Use `go mod vendor` to create it.

### Q37: How does Cross-Compilation work in Go?
**Difficulty: Medium**

**Answer:**
Go makes cross-compilation very easy by setting `GOOS` and `GOARCH` environment variables.
```bash
GOOS=linux GOARCH=amd64 go build -o myapp
```

### Q38: What are Generics in Go?
**Difficulty: Advanced**

**Answer:**
Introduced in Go 1.18, Generics allow you to write functions and data structures that can work with any of a set of types defined by constraints.
```go
func Print[T any](s []T) { ... }
```

### Q39: What is the `comparable` constraint?
**Difficulty: Advanced**

**Answer:**
`comparable` is a built-in constraint in Generics that allows types that can be compared using `==` and `!=`. It is often used for map keys.

### Q40: What is the `any` type?
**Difficulty: Easy**

**Answer:**
`any` is an alias for `interface{}` introduced in Go 1.18. It represents a type that can hold any value.

### Q41: Difference between Slice Length and Capacity?
**Difficulty: Medium**

**Answer:**
- **Length (`len`):** The number of elements currently in the slice.
- **Capacity (`cap`):** The number of elements the underlying array can hold starting from the slice pointer.

### Q42: Difference between `nil` slice and empty slice?
**Difficulty: Medium**

**Answer:**
- **Nil slice:** `var s []int`. Has no underlying array. `len=0`, `cap=0`.
- **Empty slice:** `s := []int{}` or `make([]int, 0)`. Has an underlying array (pointer is not nil). `len=0`, `cap=0`.
Functionally they are often treated the same (both have len 0), but JSON serialization differs (`null` vs `[]`).

### Q43: How do you copy a slice?
**Difficulty: Easy**

**Answer:**
Use the built-in `copy` function.
```go
dest := make([]int, len(src))
copy(dest, src)
```
Note that `dest` must have enough length allocated.

### Q44: How do you delete an element from a Map?
**Difficulty: Easy**

**Answer:**
Use the built-in `delete` function.
```go
delete(m, "key")
```
If the key doesn't exist, it does nothing (no error).

### Q45: Is Map iteration order guaranteed?
**Difficulty: Easy**

**Answer:**
No. Map iteration order is randomized in Go. Every time you iterate over a map, you may get the keys in a different order. This is intentional to prevent developers from relying on order.

### Q46: How are Structs compared?
**Difficulty: Medium**

**Answer:**
Structs are comparable if all their fields are comparable. You can use `==` to compare them. If they contain slices, maps, or functions, they are not directly comparable (must use `reflect.DeepEqual`).

### Q47: Pointer Receiver vs Value Receiver?
**Difficulty: Medium**

**Answer:**
- **Value Receiver (`func (s MyStruct)`):** Operates on a copy of the struct. Cannot modify original.
- **Pointer Receiver (`func (s *MyStruct)`):** Operates on the actual struct. Can modify it. More efficient for large structs (avoids copying).

### Q48: Can Interfaces be embedded?
**Difficulty: Medium**

**Answer:**
Yes, interfaces can embed other interfaces.
```go
type ReadWriter interface {
    Reader
    Writer
}
```

### Q49: What are Circular Dependencies and how to avoid them?
**Difficulty: Medium**

**Answer:**
Circular dependencies happen when Package A imports Package B, and Package B imports Package A. Go compiler forbids this.
**Solutions:**
1. Move shared code to a new common package (Package C).
2. Use interfaces to decouple dependencies.

### Q50: Type Alias vs Type Definition?
**Difficulty: Advanced**

**Answer:**
- **Type Definition:** `type MyInt int`. Creates a *new* type. `MyInt` and `int` are distinct.
- **Type Alias:** `type MyInt = int`. `MyInt` and `int` are the *same* type. Mostly used for refactoring/migration.

### Q51: What is `reflect.DeepEqual`?
**Difficulty: Advanced**

**Answer:**
`reflect.DeepEqual` is a function that compares two variables deeply. It can compare slices, maps, and structs that `==` cannot. It is slower than `==`.

### Q52: What is Reflection?
**Difficulty: Advanced**

**Answer:**
Reflection (`reflect` package) allows a program to examine its own structure, types, and values at runtime. It is powerful but complex and slow. Used in `json`, `fmt`, etc.

### Q53: What is `sync.Pool`?
**Difficulty: Advanced**

**Answer:**
`sync.Pool` is a set of temporary objects that may be individually saved and retrieved. It is used to relieve pressure on the Garbage Collector by reusing objects (e.g., buffers) instead of allocating new ones.

### Q54: What are Atomic Operations?
**Difficulty: Advanced**

**Answer:**
The `sync/atomic` package provides low-level atomic memory primitives (Add, Load, Store, Swap, CAS) useful for implementing synchronization algorithms without using mutexes.

### Q55: How does Context Cancellation work?
**Difficulty: Advanced**

**Answer:**
When a parent context is canceled (via `cancel()` or timeout), the `Done()` channel of that context and all its children is closed. Goroutines listening to `<-ctx.Done()` receive the signal and clean up.

### Q56: Pitfalls of using Context Values?
**Difficulty: Medium**

**Answer:**
`context.WithValue` should only be used for request-scoped data (Trace IDs, User info), NOT for optional function parameters or dependency injection. Keys should be custom types to avoid collisions.

### Q57: What is the Middleware Pattern?
**Difficulty: Medium**

**Answer:**
Middleware is a function that wraps an `http.Handler` to perform pre- or post-processing (logging, auth, panic recovery) before calling the next handler.
```go
func logging(next http.Handler) http.Handler { ... }
```

### Q58: What is the `http.Handler` interface?
**Difficulty: Medium**

**Answer:**
It is the core interface for handling HTTP requests.
```go
type Handler interface {
    ServeHTTP(ResponseWriter, *Request)
}
```

### Q59: What is `http.ServeMux`?
**Difficulty: Easy**

**Answer:**
`ServeMux` is an HTTP request multiplexer (router). It matches the URL of incoming requests against a list of registered patterns and calls the corresponding handler.

### Q60: What does `omitempty` do in JSON tags?
**Difficulty: Easy**

**Answer:**
The `omitempty` option in a struct tag tells `json.Marshal` not to output the field if it has the zero value (0, "", nil, false).

### Q61: Does panic propagate across Goroutines?
**Difficulty: Advanced**

**Answer:**
No. A panic only crashes the goroutine where it happened (and the whole program if not recovered). You cannot `recover` a panic from a different goroutine.

### Q62: What is `runtime.Goexit`?
**Difficulty: Advanced**

**Answer:**
`runtime.Goexit` terminates the goroutine that calls it. No other goroutine is affected. `defer` functions are still executed.

### Q63: Common mistake with Closures in Loops?
**Difficulty: Medium**

**Answer:**
Capturing loop variables in closures (goroutines) often leads to bugs where all goroutines see the last value of the loop variable.
**Fix:** Pass the variable as an argument or re-declare it inside the loop body (`v := v`).
*(Note: Fixed in Go 1.22)*

### Q64: What is Escape Analysis?
**Difficulty: Advanced**

**Answer:**
Escape analysis is a compiler phase that determines whether variables should be allocated on the stack or the heap. If a reference to a variable "escapes" the function (e.g., returned), it must be on the heap.

### Q65: Stack vs Heap memory in Go?
**Difficulty: Advanced**

**Answer:**
- **Stack:** Fast allocation/deallocation (pointer movement). Used for local variables.
- **Heap:** Slower, managed by GC. Used for data that outlives the function scope.

### Q66: What is Inlining?
**Difficulty: Advanced**

**Answer:**
Inlining is an optimization where the compiler replaces a function call with the body of the function itself to save call overhead.

### Q67: What is PGO (Profile Guided Optimization)?
**Difficulty: Advanced**

**Answer:**
PGO (introduced in Go 1.20/1.21) allows the compiler to use a CPU profile from a real execution to make better optimization decisions (e.g., which functions to inline).

### Q68: How do you write tests in Go?
**Difficulty: Easy**

**Answer:**
Create a file ending in `_test.go`. Write functions named `TestXxx(t *testing.T)`. Use `go test` to run.

### Q69: What are Table-Driven Tests?
**Difficulty: Medium**

**Answer:**
A pattern where you define a slice of structs (test cases) containing inputs and expected outputs, and loop over them to run the same test logic. Preferred way to test in Go.

### Q70: How do you write Benchmarks?
**Difficulty: Medium**

**Answer:**
Write functions named `BenchmarkXxx(b *testing.B)` in `_test.go` files. Loop `b.N` times. Use `go test -bench .`.

### Q71: What is Fuzzing?
**Difficulty: Advanced**

**Answer:**
Fuzzing (Go 1.18+) is automated testing that provides random invalid/unexpected inputs to your code to find bugs/crashes.
`func FuzzXxx(f *testing.F) { ... }`

### Q72: What are Build Tags?
**Difficulty: Medium**

**Answer:**
Build tags (or build constraints) are comments like `//go:build linux` that control when a file should be included in the package build (e.g., OS-specific code).

### Q73: What is `go generate`?
**Difficulty: Medium**

**Answer:**
`go generate` is a standard way to run code generators. You add comments like `//go:generate command args` in your code, and run `go generate` to execute them (e.g., generating mocks).

### Q74: What is `go vet`?
**Difficulty: Easy**

**Answer:**
`go vet` is a tool that examines Go source code and reports suspicious constructs (e.g., Printf format mismatches, unreachable code).

### Q75: What is `go fmt`?
**Difficulty: Easy**

**Answer:**
`go fmt` automatically formats Go source code to the standard style. It eliminates style debates.

### Q76: How to use Makefiles with Go?
**Difficulty: Medium**

**Answer:**
Makefiles are often used to automate common tasks: build, test, lint, docker-build. It simplifies complex command invocations.

### Q77: Best practices for Dockerizing Go apps?
**Difficulty: Medium**

**Answer:**
- Multi-stage builds (build in one stage, copy binary to a minimal runtime image).
- Use `alpine` or `distroless` for small images.
- Static compilation (CGO_ENABLED=0).

### Q78: What are Distroless Images?
**Difficulty: Medium**

**Answer:**
Images provided by Google that contain only your application and its runtime dependencies. They do not contain package managers, shells, or other programs, improving security.

### Q79: gRPC vs REST in Go?
**Difficulty: Medium**

**Answer:**
- **REST:** JSON over HTTP/1.1. Human readable, ubiquitous.
- **gRPC:** Protobuf over HTTP/2. Binary, strongly typed, higher performance, supports streaming. Go has excellent support for both.

### Q80: What are Protocol Buffers?
**Difficulty: Medium**

**Answer:**
Protocol Buffers (protobuf) is a language-neutral, platform-neutral extensible mechanism for serializing structured data. Smaller and faster than JSON.

### Q81: How does `sql.DB` handle connections?
**Difficulty: Advanced**

**Answer:**
`sql.DB` is not a single connection but a pool of connections. It opens and closes connections as needed. It is safe for concurrent use.

### Q82: How to prevent SQL Injection in Go?
**Difficulty: Medium**

**Answer:**
Always use parameterized queries (placeholders like `$1`, `?`) provided by `sql` package. Never concatenate strings to build SQL queries.

### Q83: How do you Mock dependencies in tests?
**Difficulty: Medium**

**Answer:**
Define interfaces for dependencies. In tests, create a struct that implements the interface but returns fake data. Libraries like `gomock` or `testify/mock` can help.

### Q84: What is Interface Pollution?
**Difficulty: Advanced**

**Answer:**
Creating interfaces before they are needed. In Go, interfaces should be defined where they are *used* (consumer-side), not where the type is defined. "Accept interfaces, return structs".

### Q85: What is the Functional Options Pattern?
**Difficulty: Advanced**

**Answer:**
A pattern for creating complex structs with optional configuration.
```go
func NewServer(opts ...Option) *Server { ... }
```
It is clean, extensible, and API-friendly.

### Q86: What is the Builder Pattern in Go?
**Difficulty: Medium**

**Answer:**
Used to construct complex objects step by step. Less common in Go than Functional Options, but useful for building things like SQL queries.

### Q87: How to implement Singleton Pattern?
**Difficulty: Medium**

**Answer:**
Use `sync.Once`.
```go
var once sync.Once
var instance *Singleton
func GetInstance() *Singleton {
    once.Do(func() {
        instance = &Singleton{}
    })
    return instance
}
```

### Q88: What is the Factory Pattern?
**Difficulty: Easy**

**Answer:**
Simple functions like `NewPerson()` that return a pointer to a struct. Go doesn't use classes, so constructor methods act as factories.

### Q89: What is the Adapter Pattern?
**Difficulty: Medium**

**Answer:**
Used to adapt one interface to another. Frequently used with `http.HandlerFunc` adapting a function to `http.Handler`.

### Q90: What is the Decorator Pattern?
**Difficulty: Medium**

**Answer:**
Wrapping an object to add behavior. HTTP Middleware is a classic example of the Decorator pattern in Go.

### Q91: What is the Worker Pool Pattern?
**Difficulty: Advanced**

**Answer:**
A pattern where a fixed number of workers (goroutines) pull tasks from a shared channel. Limits concurrency and resource usage.

### Q92: Explain Fan-out/Fan-in Pattern.
**Difficulty: Advanced**

**Answer:**
- **Fan-out:** Distribute work to multiple goroutines.
- **Fan-in:** Multiplex results from multiple goroutines into a single channel.

### Q93: What is the Pipeline Pattern?
**Difficulty: Advanced**

**Answer:**
A series of stages connected by channels, where each stage is a group of goroutines running the same function. Data flows through the pipeline.

### Q94: What is the Semaphore Pattern?
**Difficulty: Advanced**

**Answer:**
Using a buffered channel to limit the number of concurrent operations.
```go
sem := make(chan struct{}, maxConcurrency)
sem <- struct{}{} // Acquire
// do work
<-sem // Release
```

### Q95: How to implement Rate Limiting?
**Difficulty: Medium**

**Answer:**
Use `time.Ticker` or `rate.Limiter` (token bucket algorithm) to control the frequency of events or requests.

### Q96: How to handle Graceful Shutdown?
**Difficulty: Medium**

**Answer:**
Listen for OS signals (`SIGINT`, `SIGTERM`) using `signal.Notify`. When received, stop accepting new requests, finish current ones (using `context` and `WaitGroup`), and then exit.

### Q97: Logging Best Practices?
**Difficulty: Medium**

**Answer:**
- Use structured logging (JSON).
- Include context (Trace IDs).
- Use levels (Info, Error, Debug).
- New `log/slog` package (Go 1.21) is the standard for structured logging.

### Q98: What is Error Wrapping?
**Difficulty: Medium**

**Answer:**
Adding context to an error while preserving the original error.
```go
fmt.Errorf("failed to read: %w", err)
```
Allows unwrapping later.

### Q99: `errors.Is` vs `errors.As`?
**Difficulty: Medium**

**Answer:**
- **`errors.Is`:** Checks if an error wraps a specific sentinel error (value comparison).
- **`errors.As`:** Checks if an error wraps a specific type of error and assigns it (type assertion).

### Q100: What is the future of Go?
**Difficulty: Easy**

**Answer:**
Go continues to evolve with focus on performance, developer experience, and stability. Recent additions include Generics, Fuzzing, and PGO. It remains a dominant language for cloud-native infrastructure, microservices, and CLI tools.
