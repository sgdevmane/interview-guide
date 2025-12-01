<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/golang-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>Golang Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for developers</b></p>
</div>

---

## Table of Contents

1. [How do you manage Goroutine lifecycles to prevent memory leaks?](#q1) <span class="intermediate">Intermediate</span>
2. [How do you implement the Worker Pool pattern to limit concurrency?](#q2) <span class="intermediate">Intermediate</span>
3. [How do you handle errors gracefully using custom error types and wrapping?](#q3) <span class="intermediate">Intermediate</span>
4. [How do you implement a thread-safe Singleton in Go?](#q4) <span class="intermediate">Intermediate</span>
5. [How do you use the Functional Options pattern to configure complex structs?](#q5) <span class="intermediate">Intermediate</span>
6. [How do you implement a Graceful Shutdown for an HTTP server?](#q6) <span class="intermediate">Intermediate</span>
7. [How do you test code effectively using Table-Driven Tests?](#q7) <span class="intermediate">Intermediate</span>
8. [How do you use Generics to create a type-safe Set data structure?](#q8) <span class="intermediate">Intermediate</span>
9. [How do you use `sync.WaitGroup` to wait for multiple concurrent operations?](#q9) <span class="intermediate">Intermediate</span>
10. [How do you implement middleware for an HTTP handler?](#q10) <span class="intermediate">Intermediate</span>
11. [How do you use interfaces for dependency injection to improve testability?](#q11) <span class="intermediate">Intermediate</span>
12. [How do you use the `select` statement to implement a timeout?](#q12) <span class="intermediate">Intermediate</span>
13. [How do you use `io.Reader` and `io.Writer` to stream data efficiently?](#q13) <span class="intermediate">Intermediate</span>
14. [How do you prevent race conditions using `sync.Mutex`?](#q14) <span class="intermediate">Intermediate</span>
15. [How do you optimize memory usage with `sync.Pool`?](#q15) <span class="intermediate">Intermediate</span>
16. [How do you implement a custom JSON Marshaler to hide sensitive fields?](#q16) <span class="intermediate">Intermediate</span>
17. [How do you use `sync.Once` to ensure a function runs exactly once?](#q17) <span class="intermediate">Intermediate</span>
18. [How do you implement a rate limiter using a Token Bucket algorithm?](#q18) <span class="intermediate">Intermediate</span>
19. [How do you correctly handle loop variables in Goroutines?](#q19) <span class="intermediate">Intermediate</span>
20. [How do you use `go:embed` to bundle static assets?](#q20) <span class="intermediate">Intermediate</span>
21. [How do you use `errgroup` to manage parallel tasks with error propagation?](#q21) <span class="intermediate">Intermediate</span>
22. [How do you implement atomic counters using `sync/atomic`?](#q22) <span class="intermediate">Intermediate</span>
23. [How do you benchmark code using `testing.B`?](#q23) <span class="intermediate">Intermediate</span>
24. [How do you optimize memory layout by reordering struct fields?](#q24) <span class="advanced">Expert</span>
25. [How do you use `context.WithValue` to pass request-scoped data?](#q25) <span class="intermediate">Intermediate</span>
26. [How do you implement a simple Fan-Out/Fan-In pattern?](#q26) <span class="intermediate">Intermediate</span>
27. [How do you use `defer` effectively for cleanup (and avoid common traps)?](#q27) <span class="intermediate">Intermediate</span>
28. [How do you implement a custom HTTP RoundTripper?](#q28) <span class="advanced">Expert</span>
29. [How do you use `reflect` to iterate over struct fields?](#q29) <span class="advanced">Expert</span>
30. [How do you use `slices` package (Go 1.21+) for common operations?](#q30) <span class="intermediate">Intermediate</span>
31. [How do you use the new `slices` package (Go 1.21+) for common operations?](#q31) <span class="beginner">Beginner</span>
32. [How do you iterate over an integer range using `range` in Go 1.22+?](#q32) <span class="beginner">Beginner</span>
33. [How do you use `cmp.Or` (Go 1.22+) to return the first non-zero value?](#q33) <span class="intermediate">Intermediate</span>
34. [How do you create a structured logger using `log/slog` (Go 1.21+)?](#q34) <span class="intermediate">Intermediate</span>
35. [How do you use `sync.OnceValue` (Go 1.21+) for lazy initialization?](#q35) <span class="intermediate">Intermediate</span>
36. [How do you check for race conditions in Go?](#q36) <span class="intermediate">Intermediate</span>
37. [How do you use `context.WithTimeout` to cancel long-running operations?](#q37) <span class="intermediate">Intermediate</span>
38. [How do you embed static files into a Go binary?](#q38) <span class="beginner">Beginner</span>
39. [How do you perform atomic operations to avoid mutexes?](#q39) <span class="advanced">Advanced</span>
40. [How do you benchmark Go code?](#q40) <span class="intermediate">Intermediate</span>
41. [How do you marshal JSON with custom field names or omission?](#q41) <span class="beginner">Beginner</span>
42. [How do you implement a simple HTTP middleware?](#q42) <span class="intermediate">Intermediate</span>
43. [How do you detect and handle panics in a Goroutine?](#q43) <span class="intermediate">Intermediate</span>
44. [How do you use `io.Pipe` to stream data between a reader and writer?](#q44) <span class="advanced">Advanced</span>
45. [How do you use Go Fuzzing (Go 1.18+) to find bugs?](#q45) <span class="advanced">Advanced</span>
46. [How do you use sync.Map for concurrent map access?](#q46) <span class="intermediate">Intermediate</span>
47. [How do you use atomic.Pointer[T] (Go 1.19+)?](#q47) <span class="advanced">Advanced</span>
48. [How do you use httptest to test HTTP handlers?](#q48) <span class="intermediate">Intermediate</span>
49. [How do you use json.RawMessage to delay parsing?](#q49) <span class="intermediate">Intermediate</span>
50. [How do you use pprof to profile CPU usage?](#q50) <span class="advanced">Advanced</span>
51. [How do you use runtime/trace to analyze latency?](#q51) <span class="advanced">Expert</span>
52. [How do you use Go Workspaces (Go 1.18+) for multi-module development?](#q52) <span class="intermediate">Intermediate</span>
53. [How do you implement a custom Scanner using bufio?](#q53) <span class="intermediate">Intermediate</span>
54. [How do you use text/template for generating dynamic content?](#q54) <span class="intermediate">Intermediate</span>
55. [How do you use Singleflight to prevent cache stampedes?](#q55) <span class="advanced">Advanced</span>
56. [How do you use sync.Cond for complex synchronization?](#q56) <span class="advanced">Expert</span>
57. [How do you use the os/exec package to run external commands safely?](#q57) <span class="intermediate">Intermediate</span>
58. [How do you use the plugin package to load code at runtime?](#q58) <span class="advanced">Expert</span>
59. [How do you use testing/quick for property-based testing?](#q59) <span class="advanced">Advanced</span>
60. [How do you use context.AfterFunc (Go 1.21+) for cleanup?](#q60) <span class="intermediate">Intermediate</span>
61. [How do you use the new min/max built-ins (Go 1.21+)?](#q61) <span class="beginner">Beginner</span>
62. [How do you reduce GC pressure using `sync.Pool`?](#q62) <span class="advanced">Advanced</span>
63. [How do you use `sync.Cond` for complex synchronization?](#q63) <span class="advanced">Expert</span>
64. [How do you perform lock-free operations using `atomic`?](#q64) <span class="advanced">Advanced</span>
65. [How do you manage groups of goroutines with `errgroup`?](#q65) <span class="intermediate">Intermediate</span>
66. [What is Escape Analysis?](#q66) <span class="advanced">Advanced</span>
67. [How do you tune the Garbage Collector with `GOGC`?](#q67) <span class="advanced">Advanced</span>
68. [How do you write Fuzz Tests in Go (1.18+)?](#q68) <span class="intermediate">Intermediate</span>
69. [How do you test HTTP handlers with `httptest`?](#q69) <span class="intermediate">Intermediate</span>
70. [How do you benchmark code?](#q70) <span class="intermediate">Intermediate</span>
71. [How do you profile a Go application?](#q71) <span class="advanced">Advanced</span>
72. [How do you use Go Workspaces (`go.work`)?](#q72) <span class="intermediate">Intermediate</span>
73. [How do you embed files into the binary?](#q73) <span class="beginner">Beginner</span>
74. [How do you handle Context timeouts?](#q74) <span class="intermediate">Intermediate</span>
75. [How do you implement Graceful Shutdown?](#q75) <span class="advanced">Advanced</span>
76. [How do you implement a Worker Pool?](#q76) <span class="advanced">Advanced</span>
77. [How do you use `iota` for enumerations?](#q77) <span class="beginner">Beginner</span>
78. [What is Variable Shadowing and how to avoid it?](#q78) <span class="beginner">Beginner</span>
79. [What does a Slice Header look like internally?](#q79) <span class="advanced">Advanced</span>
80. [How do you recover from a panic?](#q80) <span class="intermediate">Intermediate</span>
81. [How do you implement the Middleware pattern in Go?](#q81) <span class="intermediate">Intermediate</span>
82. [How do you customize JSON marshaling?](#q82) <span class="intermediate">Intermediate</span>
83. [What is the difference between `time.Ticker` and `time.Timer`?](#q83) <span class="intermediate">Intermediate</span>
84. [How do you inspect types at runtime using `reflect`?](#q84) <span class="advanced">Advanced</span>
85. [How do you bypass type safety with `unsafe`?](#q85) <span class="advanced">Expert</span>
86. [How do you use Build Tags?](#q86) <span class="intermediate">Intermediate</span>
87. [What are the caveats of the `init()` function?](#q87) <span class="intermediate">Intermediate</span>
88. [How do you load Go plugins at runtime?](#q88) <span class="advanced">Advanced</span>
89. [How do you detect data races?](#q89) <span class="intermediate">Intermediate</span>
90. [How can re-slicing cause memory leaks?](#q90) <span class="advanced">Advanced</span>
91. [When should you use `sync.Map`?](#q91) <span class="advanced">Advanced</span>
92. [How do you suppress duplicate function calls with `singleflight`?](#q92) <span class="advanced">Advanced</span>
93. [When should you use `crypto/rand` vs `math/rand`?](#q93) <span class="beginner">Beginner</span>
94. [How do you handle NULL values in SQL databases?](#q94) <span class="intermediate">Intermediate</span>
95. [How do you use Structured Logging (Go 1.21+)?](#q95) <span class="intermediate">Intermediate</span>
96. [Why are `io.Reader` and `io.Writer` important?](#q96) <span class="beginner">Beginner</span>
97. [How do you read a file line by line?](#q97) <span class="beginner">Beginner</span>
98. [How do you run external commands safely?](#q98) <span class="intermediate">Intermediate</span>
99. [How do you traverse a directory tree?](#q99) <span class="intermediate">Intermediate</span>
100. [What are Go Proverbs?](#q100) <span class="beginner">Beginner</span>

---

<a id="q1"></a>
### Q1: How do you manage Goroutine lifecycles to prevent memory leaks?

**Difficulty**: Intermediate

**Strategy:**
To prevent memory leaks with Goroutines, you must ensure they have a defined exit condition. This is typically achieved using `context.Context` for cancellation or a `done` channel.


1. Pass a `context` or a signal channel to the Goroutine.
2. Use a `select` statement to listen for the cancellation signal.
3. Clean up resources before returning.

**Code Example:**
```go
package main

import (
	"context"
	"fmt"
	"time"
)

func worker(ctx context.Context, id int) {
	for {
		select {
		case <-ctx.Done():
			fmt.Printf("Worker %d stopping\n", id)
			return
		default:
			fmt.Printf("Worker %d working...\n", id)
			time.Sleep(500 * time.Millisecond)
		}
	}
}

func main() {
	ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)
	defer cancel()

	go worker(ctx, 1)

	// Wait for the context to timeout
	<-ctx.Done()
	fmt.Println("Main finished")
	
	// Give time for worker to print stop message
	time.Sleep(100 * time.Millisecond)
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q2"></a>
### Q2: How do you implement the Worker Pool pattern to limit concurrency?

**Difficulty**: Intermediate

**Strategy:**
A Worker Pool limits the number of concurrent tasks to prevent resource exhaustion. It uses a buffered channel to queue jobs and a fixed number of Goroutines to process them.


1. Create a `jobs` channel and a `results` channel.
2. Start a fixed number of worker Goroutines.
3. Send jobs to the `jobs` channel.
4. Close the `jobs` channel when all jobs are sent.
5. Collect results.

**Code Example:**
```go
package main

import (
	"fmt"
	"sync"
	"time"
)

func worker(id int, jobs <-chan int, results chan<- int, wg *sync.WaitGroup) {
	defer wg.Done()
	for j := range jobs {
		fmt.Printf("Worker %d started job %d\n", id, j)
		time.Sleep(time.Second) // Simulate work
		fmt.Printf("Worker %d finished job %d\n", id, j)
		results <- j * 2
	}
}

func main() {
	const numJobs = 5
	const numWorkers = 3
	
	jobs := make(chan int, numJobs)
	results := make(chan int, numJobs)
	var wg sync.WaitGroup

	// Start workers
	for w := 1; w <= numWorkers; w++ {
		wg.Add(1)
		go worker(w, jobs, results, &wg)
	}

	// Send jobs
	for j := 1; j <= numJobs; j++ {
		jobs <- j
	}
	close(jobs)

	// Wait for all workers to finish
	go func() {
		wg.Wait()
		close(results)
	}()

	// Collect results
	for r := range results {
		fmt.Println("Result:", r)
	}
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q3"></a>
### Q3: How do you handle errors gracefully using custom error types and wrapping?

**Difficulty**: Intermediate

**Strategy:**
In Go, errors are values. Custom error types allow adding context, and `fmt.Errorf` with `%w` allows wrapping errors to preserve the original cause for `errors.Is` and `errors.As` checks.


1. Define a struct that implements the `error` interface.
2. Use `fmt.Errorf("context: %w", err)` to wrap lower-level errors.
3. Use `errors.Is` to check for specific sentinels and `errors.As` to extract custom types.

**Code Example:**
```go
package main

import (
	"errors"
	"fmt"
)

// Custom error type
type QueryError struct {
	Query string
	Err   error
}

func (e *QueryError) Error() string {
	return fmt.Sprintf("query %q failed: %v", e.Query, e.Err)
}

func (e *QueryError) Unwrap() error { return e.Err }

var ErrNotFound = errors.New("not found")

func findUser(id int) error {
	if id < 0 {
		// Wrapping a sentinel error
		return fmt.Errorf("validation failed: %w", ErrNotFound)
	}
	// Returning a custom error
	return &QueryError{Query: "SELECT * FROM users", Err: errors.New("db connection lost")}
}

func main() {
	err := findUser(1)
	if err != nil {
		var qErr *QueryError
		if errors.As(err, &qErr) {
			fmt.Printf("Custom Error: Query='%s' Original='%v'\n", qErr.Query, qErr.Err)
		}
	}

	err2 := findUser(-1)
	if errors.Is(err2, ErrNotFound) {
		fmt.Println("Sentinel Error: Record not found")
	}
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q4"></a>
### Q4: How do you implement a thread-safe Singleton in Go?

**Difficulty**: Intermediate

**Strategy:**
The `sync.Once` primitive ensures that a piece of code is executed only once, making it perfect for initializing Singletons lazily and safely in a concurrent environment.


1. Declare a global variable for the instance.
2. Declare a `sync.Once` variable.
3. In the accessor function, use `once.Do(func() { ... })` to initialize the instance.

**Code Example:**
```go
package main

import (
	"fmt"
	"sync"
)

type Database struct {
	URL string
}

var (
	instance *Database
	once     sync.Once
)

func GetDatabase() *Database {
	once.Do(func() {
		fmt.Println("Initializing database...")
		instance = &Database{URL: "postgres://localhost:5432/mydb"}
	})
	return instance
}

func main() {
	var wg sync.WaitGroup
	
	for i := 0; i < 5; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			db := GetDatabase()
			fmt.Printf("DB URL: %s\n", db.URL)
		}()
	}
	
	wg.Wait()
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q5"></a>
### Q5: How do you use the Functional Options pattern to configure complex structs?

**Difficulty**: Intermediate

**Strategy:**
The Functional Options pattern provides a clean, extensible API for configuring structs with many optional parameters, avoiding massive constructors or nil checks.


1. Define an `Option` function type.
2. Create functions that return this `Option` type, modifying the struct.
3. Create a constructor that accepts a variadic slice of `Option`.

**Code Example:**
```go
package main

import "fmt"

type Server struct {
	Host string
	Port int
	TLS  bool
}

type Option func(*Server)

func WithHost(host string) Option {
	return func(s *Server) {
		s.Host = host
	}
}

func WithPort(port int) Option {
	return func(s *Server) {
		s.Port = port
	}
}

func WithTLS() Option {
	return func(s *Server) {
		s.TLS = true
	}
}

func NewServer(opts ...Option) *Server {
	// Default configuration
	s := &Server{
		Host: "localhost",
		Port: 8080,
		TLS:  false,
	}
	
	// Apply options
	for _, opt := range opts {
		opt(s)
	}
	
	return s
}

func main() {
	srv := NewServer(
		WithHost("example.com"),
		WithTLS(),
	)
	
	fmt.Printf("Server: %+v\n", srv)
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q6"></a>
### Q6: How do you implement a Graceful Shutdown for an HTTP server?

**Difficulty**: Intermediate

**Strategy:**
Graceful shutdown ensures that the server stops accepting new requests but finishes processing active requests before exiting. This is crucial for data integrity and user experience.


1. Start the server in a separate Goroutine.
2. Listen for OS signals (`SIGINT`, `SIGTERM`) using `signal.Notify`.
3. Call `server.Shutdown(ctx)` when a signal is received.

**Code Example:**
```go
package main

import (
	"context"
	"fmt"
	"net/http"
	"os"
	"os/signal"
	"syscall"
	"time"
)

func main() {
	srv := &http.Server{Addr: ":8080"}

	go func() {
		if err := srv.ListenAndServe(); err != http.ErrServerClosed {
			fmt.Printf("HTTP server error: %v\n", err)
		}
	}()

	// Wait for interrupt signal
	quit := make(chan os.Signal, 1)
	signal.Notify(quit, syscall.SIGINT, syscall.SIGTERM)
	<-quit
	fmt.Println("Shutting down server...")

	// Context with timeout for active requests to finish
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	if err := srv.Shutdown(ctx); err != nil {
		fmt.Printf("Server forced to shutdown: %v\n", err)
	}

	fmt.Println("Server exited")
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q7"></a>
### Q7: How do you test code effectively using Table-Driven Tests?

**Difficulty**: Intermediate

**Strategy:**
Table-driven tests allow you to define test cases as data (structs) and iterate over them, making it easy to add new scenarios and keeping the test logic DRY (Don't Repeat Yourself).


1. Define a struct containing `name`, `input`, and `expected` fields.
2. Create a slice of these structs with various test cases.
3. Iterate over the slice using `t.Run` to execute subtests.

**Code Example:**
```go
package main

import "testing"

func Add(a, b int) int {
	return a + b
}

func TestAdd(t *testing.T) {
	tests := []struct {
		name     string
		a, b     int
		expected int
	}{
		{"Positive numbers", 2, 3, 5},
		{"Negative numbers", -1, -1, -2},
		{"Mixed numbers", -5, 5, 0},
		{"Zero", 0, 0, 0},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := Add(tt.a, tt.b)
			if result != tt.expected {
				t.Errorf("Add(%d, %d) = %d; want %d", tt.a, tt.b, result, tt.expected)
			}
		})
	}
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q8"></a>
### Q8: How do you use Generics to create a type-safe Set data structure?

**Difficulty**: Intermediate

**Strategy:**
Go Generics (introduced in Go 1.18) allow you to write data structures that work with any type that satisfies a constraint (e.g., `comparable`).


1. Define a generic struct `Set[T comparable]`.
2. Use a `map[T]struct{}` for underlying storage (efficient O(1) lookups).
3. Implement methods like `Add`, `Remove`, and `Contains`.

**Code Example:**
```go
package main

import "fmt"

type Set[T comparable] struct {
	items map[T]struct{}
}

func NewSet[T comparable]() *Set[T] {
	return &Set[T]{items: make(map[T]struct{})}
}

func (s *Set[T]) Add(item T) {
	s.items[item] = struct{}{}
}

func (s *Set[T]) Contains(item T) bool {
	_, exists := s.items[item]
	return exists
}

func (s *Set[T]) Remove(item T) {
	delete(s.items, item)
}

func main() {
	// String Set
	names := NewSet[string]()
	names.Add("Alice")
	names.Add("Bob")
	fmt.Println("Contains Alice:", names.Contains("Alice"))

	// Integer Set
	ids := NewSet[int]()
	ids.Add(101)
	ids.Add(102)
	fmt.Println("Contains 103:", ids.Contains(103))
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q9"></a>
### Q9: How do you use `sync.WaitGroup` to wait for multiple concurrent operations?

**Difficulty**: Intermediate

**Strategy:**
`sync.WaitGroup` is used to wait for a collection of Goroutines to finish execution. It maintains a counter that is incremented when a Goroutine starts and decremented when it finishes.


1. Call `wg.Add(1)` before starting a Goroutine.
2. Pass the `wg` pointer to the Goroutine (or capture via closure).
3. Call `wg.Done()` inside the Goroutine (usually deferred).
4. Call `wg.Wait()` in the main thread to block until the counter is zero.

**Code Example:**
```go
package main

import (
	"fmt"
	"sync"
	"time"
)

func process(id int, wg *sync.WaitGroup) {
	defer wg.Done() // Decrement counter when function exits
	fmt.Printf("Process %d starting\n", id)
	time.Sleep(time.Second)
	fmt.Printf("Process %d done\n", id)
}

func main() {
	var wg sync.WaitGroup

	for i := 1; i <= 3; i++ {
		wg.Add(1) // Increment counter
		go process(i, &wg)
	}

	fmt.Println("Waiting for processes...")
	wg.Wait() // Block until counter is 0
	fmt.Println("All done!")
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q10"></a>
### Q10: How do you implement middleware for an HTTP handler?

**Difficulty**: Intermediate

**Strategy:**
Middleware allows you to wrap an `http.Handler` to execute logic before or after the main handler, such as logging, authentication, or panic recovery.


1. Create a function that takes `http.Handler` and returns `http.Handler`.
2. Inside the returned handler, perform pre-processing.
3. Call `next.ServeHTTP(w, r)` to pass control.
4. Perform post-processing if needed.

**Code Example:**
```go
package main

import (
	"fmt"
	"log"
	"net/http"
	"time"
)

func LoggingMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		start := time.Now()
		
		// Pass control to the next handler
		next.ServeHTTP(w, r)
		
		// Post-processing
		log.Printf("%s %s %s", r.Method, r.URL.Path, time.Since(start))
	})
}

func homeHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "Welcome Home!")
}

func main() {
	mux := http.NewServeMux()
	mux.HandleFunc("/", homeHandler)

	// Wrap mux with middleware
	wrappedMux := LoggingMiddleware(mux)

	log.Println("Server starting on :8080")
	http.ListenAndServe(":8080", wrappedMux)
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q11"></a>
### Q11: How do you use interfaces for dependency injection to improve testability?

**Difficulty**: Intermediate

**Strategy:**
Dependency Injection (DI) via interfaces allows you to decouple components and swap real implementations with mocks during testing.


1. Define an interface for the dependency (e.g., `DataStore`).
2. Have the consumer struct accept the interface, not the concrete type.
3. In production, pass the real implementation; in tests, pass a mock.

**Code Example:**
```go
package main

import "fmt"

// 1. Define Interface
type DataStore interface {
	Save(data string) error
}

// 2. Real Implementation
type PostgresStore struct{}
func (p *PostgresStore) Save(data string) error {
	fmt.Println("Saving to Postgres:", data)
	return nil
}

// 3. Mock Implementation
type MockStore struct{}
func (m *MockStore) Save(data string) error {
	fmt.Println("Mock save (no side effects):", data)
	return nil
}

// 4. Consumer
type Service struct {
	store DataStore
}

func (s *Service) ProcessData(data string) {
	// Logic...
	s.store.Save(data)
}

func main() {
	// Production usage
	realService := &Service{store: &PostgresStore{}}
	realService.ProcessData("Real Data")

	// Test usage
	testService := &Service{store: &MockStore{}}
	testService.ProcessData("Test Data")
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q12"></a>
### Q12: How do you use the `select` statement to implement a timeout?

**Difficulty**: Intermediate

**Strategy:**
The `select` statement lets a Goroutine wait on multiple communication operations. By including a case for `time.After`, you can enforce a timeout on channel operations.


1. Define a `select` block.
2. Add a case for the expected channel operation (receive or send).
3. Add a case for `<-time.After(duration)` to handle the timeout.

**Code Example:**
```go
package main

import (
	"fmt"
	"time"
)

func expensiveOperation() chan string {
	ch := make(chan string)
	go func() {
		time.Sleep(2 * time.Second) // Simulate delay
		ch <- "Success"
	}()
	return ch
}

func main() {
	select {
	case res := <-expensiveOperation():
		fmt.Println("Result:", res)
	case <-time.After(1 * time.Second):
		fmt.Println("Error: Operation timed out")
	}
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q13"></a>
### Q13: How do you use `io.Reader` and `io.Writer` to stream data efficiently?

**Difficulty**: Intermediate

**Strategy:**
Go's `io` interfaces allow you to stream data without loading it all into memory. `io.Copy` is a powerful utility that connects a reader to a writer efficiently.


1. Use `os.Open` to get a file (Reader).
2. Use `os.Create` or `http.ResponseWriter` as the destination (Writer).
3. Use `io.Copy(dst, src)` to transfer data in chunks.

**Code Example:**
```go
package main

import (
	"fmt"
	"io"
	"os"
	"strings"
)

func main() {
	// Create a reader from a string
	reader := strings.NewReader("Streaming data from source to destination...")

	// Create a file to write to
	file, err := os.Create("output.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	// Copy from reader to writer
	// This uses a small buffer internally, efficient for large data
	written, err := io.Copy(file, reader)
	if err != nil {
		panic(err)
	}

	fmt.Printf("Copied %d bytes to output.txt\n", written)
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q14"></a>
### Q14: How do you prevent race conditions using `sync.Mutex`?

**Difficulty**: Intermediate

**Strategy:**
Race conditions occur when multiple Goroutines access shared memory concurrently without synchronization. `sync.Mutex` provides a locking mechanism to ensure exclusive access.


1. Embed or include `sync.Mutex` in the struct holding the shared data.
2. Call `mu.Lock()` before accessing the data.
3. Call `mu.Unlock()` (usually deferred) after accessing.

**Code Example:**
```go
package main

import (
	"fmt"
	"sync"
)

type SafeCounter struct {
	mu    sync.Mutex
	value int
}

func (c *SafeCounter) Inc() {
	c.mu.Lock()         // Lock before modifying
	defer c.mu.Unlock() // Unlock when done
	c.value++
}

func (c *SafeCounter) Value() int {
	c.mu.Lock()         // Lock before reading
	defer c.mu.Unlock()
	return c.value
}

func main() {
	c := SafeCounter{}
	var wg sync.WaitGroup

	for i := 0; i < 1000; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			c.Inc()
		}()
	}

	wg.Wait()
	fmt.Println("Final Value:", c.Value())
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q15"></a>
### Q15: How do you optimize memory usage with `sync.Pool`?

**Difficulty**: Intermediate

**Strategy:**
`sync.Pool` caches allocated but unused objects for later reuse, reducing the pressure on the Garbage Collector (GC). It is ideal for frequently allocated, short-lived objects like buffers.


1. Initialize `sync.Pool` with a `New` function.
2. Use `pool.Get()` to retrieve an object (type assert it).
3. Reset the object state.
4. Use `pool.Put()` to return the object to the pool.

**Code Example:**
```go
package main

import (
	"bytes"
	"fmt"
	"sync"
)

var bufPool = sync.Pool{
	New: func() interface{} {
		// Pre-allocate buffer
		return new(bytes.Buffer)
	},
}

func LogMessage(msg string) {
	// Get buffer from pool
	b := bufPool.Get().(*bytes.Buffer)
	b.Reset() // Reset before use
	
	// Use buffer
	b.WriteString("Log: ")
	b.WriteString(msg)
	fmt.Println(b.String())
	
	// Return to pool
	bufPool.Put(b)
}

func main() {
	LogMessage("Hello")
	LogMessage("World")
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q16"></a>
### Q16: How do you implement a custom JSON Marshaler to hide sensitive fields?

**Difficulty**: Intermediate

**Strategy:**
To customize JSON encoding, implement the `json.Marshaler` interface. This is useful for masking sensitive data (PII, passwords) or changing the output format without altering the struct definition.

**Code Example:**
```go
package main

import (
	"encoding/json"
	"fmt"
)

type User struct {
	ID       int
	Username string
	Password string // Sensitive
	Email    string
}

// Implement json.Marshaler interface
func (u User) MarshalJSON() ([]byte, error) {
	// Create an alias to avoid infinite recursion
	type Alias User
	return json.Marshal(&struct {
		Password string `json:"password"` // Override
		*Alias
	}{
		Password: "***", // Mask password
		Alias:    (*Alias)(&u),
	})
}

func main() {
	u := User{ID: 1, Username: "alice", Password: "secret123", Email: "alice@example.com"}
	
	data, _ := json.MarshalIndent(u, "", "  ")
	fmt.Println(string(data))
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q17"></a>
### Q17: How do you use `sync.Once` to ensure a function runs exactly once?

**Difficulty**: Intermediate

**Strategy:**
`sync.Once` is perfect for lazy initialization of global resources (like singletons or config loading) in a thread-safe manner. It guarantees that the `Do` function is called only once, even if invoked concurrently.

**Code Example:**
```go
package main

import (
	"fmt"
	"sync"
)

var (
	config map[string]string
	once   sync.Once
)

func loadConfig() {
	fmt.Println("Loading configuration...")
	config = map[string]string{
		"db_host": "localhost",
		"port":    "5432",
	}
}

func GetConfig() map[string]string {
	once.Do(loadConfig) // Only runs once
	return config
}

func main() {
	var wg sync.WaitGroup
	
	// Simulate concurrent access
	for i := 0; i < 5; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			cfg := GetConfig()
			fmt.Println("Got config:", cfg["db_host"])
		}()
	}
	
	wg.Wait()
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q18"></a>
### Q18: How do you implement a rate limiter using a Token Bucket algorithm?

**Difficulty**: Intermediate

**Strategy:**
The `golang.org/x/time/rate` package provides a robust token bucket rate limiter. You can use `Wait`, `Allow`, or `Reserve` to control event frequency.

**Code Example:**
```go
package main

import (
	"context"
	"fmt"
	"time"

	"golang.org/x/time/rate"
)

func main() {
	// Limit: 5 events per second, burst of 10
	limiter := rate.NewLimiter(5, 10)
	ctx := context.Background()

	for i := 0; i < 20; i++ {
		// Block until a token is available
		if err := limiter.Wait(ctx); err != nil {
			fmt.Println("Error:", err)
			return
		}
		fmt.Printf("Processed request %d at %v
", i, time.Now().Format("15:04:05.000"))
	}
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q19"></a>
### Q19: How do you correctly handle loop variables in Goroutines?

**Difficulty**: Intermediate

**Strategy:**
Prior to Go 1.22, loop variables were reused across iterations. Capturing them in a closure (Goroutine) would often lead to processing the last value for all iterations. The fix was to pass the variable as an argument or redeclare it inside the loop.

**Code Example:**
```go
package main

import (
	"fmt"
	"sync"
)

func main() {
	values := []string{"a", "b", "c"}
	var wg sync.WaitGroup

	for _, v := range values {
		wg.Add(1)
		// Correct: Pass 'v' as an argument to the closure
		go func(val string) {
			defer wg.Done()
			fmt.Println(val)
		}(v)
		
		// Alternative (Shadowing):
		// v := v 
		// go func() { fmt.Println(v) }()
	}

	wg.Wait()
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q20"></a>
### Q20: How do you use `go:embed` to bundle static assets?

**Difficulty**: Intermediate

**Strategy:**
The `embed` package (Go 1.16+) allows you to include static files (HTML, SQL, configs) directly into the binary. This simplifies deployment by producing a single executable.

**Code Example:**
```go
package main

import (
	"embed"
	"fmt"
	"net/http"
)

//go:embed index.html
var content embed.FS

func main() {
	// Read file content directly
	data, _ := content.ReadFile("index.html")
	fmt.Println("HTML Content:", string(data))

	// Serve embedded filesystem
	http.Handle("/", http.FileServer(http.FS(content)))
	
	// In a real scenario: http.ListenAndServe(":8080", nil)
}

/*
// index.html
<html><body><h1>Hello Embed!</h1></body></html>
*/
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q21"></a>
### Q21: How do you use `errgroup` to manage parallel tasks with error propagation?

**Difficulty**: Intermediate

**Strategy:**
`errgroup` (from `golang.org/x/sync/errgroup`) is superior to `WaitGroup` when you need to propagate errors or cancel all tasks if one fails.

**Code Example:**
```go
package main

import (
	"context"
	"fmt"
	"time"

	"golang.org/x/sync/errgroup"
)

func main() {
	g, ctx := errgroup.WithContext(context.Background())

	urls := []string{"http://google.com", "http://bad-url", "http://bing.com"}

	for _, url := range urls {
		url := url // Capture variable
		g.Go(func() error {
			// Simulate work
			if url == "http://bad-url" {
				return fmt.Errorf("failed to fetch %s", url)
			}
			
			select {
			case <-ctx.Done():
				return ctx.Err() // Canceled
			case <-time.After(100 * time.Millisecond):
				fmt.Printf("Fetched %s
", url)
				return nil
			}
		})
	}

	if err := g.Wait(); err != nil {
		fmt.Println("Group error:", err)
	} else {
		fmt.Println("All fetched successfully")
	}
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q22"></a>
### Q22: How do you implement atomic counters using `sync/atomic`?

**Difficulty**: Intermediate

**Strategy:**
For simple counters, `sync/atomic` is much faster and lighter than `sync.Mutex`. It provides low-level atomic memory primitives.

**Code Example:**
```go
package main

import (
	"fmt"
	"sync"
	"sync/atomic"
)

func main() {
	var ops atomic.Uint64 // Go 1.19+ type-safe atomic
	var wg sync.WaitGroup

	for i := 0; i < 50; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			for j := 0; j < 1000; j++ {
				ops.Add(1)
			}
		}()
	}

	wg.Wait()
	fmt.Println("Ops:", ops.Load())
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q23"></a>
### Q23: How do you benchmark code using `testing.B`?

**Difficulty**: Intermediate

**Strategy:**
Go has a built-in benchmarking tool. Functions starting with `Benchmark` in `_test.go` files take `*testing.B` and run the code `b.N` times to measure performance.

**Code Example:**
```go
package main

import (
	"strings"
	"testing"
)

// Function to benchmark
func JoinStrings(n int) string {
	var sb strings.Builder
	for i := 0; i < n; i++ {
		sb.WriteString("x")
	}
	return sb.String()
}

// Benchmark function
func BenchmarkJoinStrings(b *testing.B) {
	// Run the loop b.N times
	for i := 0; i < b.N; i++ {
		JoinStrings(1000)
	}
}

// Run with: go test -bench=. -benchmem
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q24"></a>
### Q24: How do you optimize memory layout by reordering struct fields?

**Difficulty**: Expert

**Strategy:**
Struct fields are aligned in memory based on their size. Ordering fields from largest to smallest (pointers/int64 -> int32 -> bool) can minimize padding and reduce memory usage.

**Code Example:**
```go
package main

import (
	"fmt"
	"unsafe"
)

// Bad layout: lots of padding
type BadStruct struct {
	isActive bool    // 1 byte + 7 bytes padding
	id       int64   // 8 bytes
	score    float64 // 8 bytes
	flags    int8    // 1 byte + 7 bytes padding
}

// Optimized layout: minimal padding
type GoodStruct struct {
	id       int64   // 8 bytes
	score    float64 // 8 bytes
	isActive bool    // 1 byte
	flags    int8    // 1 byte
	// + 6 bytes padding at end to align to 8 bytes
}

func main() {
	fmt.Printf("BadStruct size: %d
", unsafe.Sizeof(BadStruct{}))   // 32 bytes
	fmt.Printf("GoodStruct size: %d
", unsafe.Sizeof(GoodStruct{})) // 24 bytes
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q25"></a>
### Q25: How do you use `context.WithValue` to pass request-scoped data?

**Difficulty**: Intermediate

**Strategy:**
`context.WithValue` creates a child context carrying a key-value pair. It's commonly used in middleware to pass user info, trace IDs, or logger instances down the call chain. Use custom types for keys to avoid collisions.

**Code Example:**
```go
package main

import (
	"context"
	"fmt"
)

// Define custom type for context key to avoid collisions
type key int

const (
	userKey key = iota
)

func processRequest(ctx context.Context) {
	// Retrieve value
	if user, ok := ctx.Value(userKey).(string); ok {
		fmt.Println("Processing request for:", user)
	} else {
		fmt.Println("No user found")
	}
}

func main() {
	ctx := context.Background()
	
	// Inject value
	ctxWithUser := context.WithValue(ctx, userKey, "Alice")
	
	processRequest(ctxWithUser)
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q26"></a>
### Q26: How do you implement a simple Fan-Out/Fan-In pattern?

**Difficulty**: Intermediate

**Strategy:**
Fan-Out starts multiple Goroutines to process work in parallel. Fan-In combines their results into a single channel.

**Code Example:**
```go
package main

import (
	"fmt"
	"sync"
)

func producer(nums ...int) <-chan int {
	out := make(chan int)
	go func() {
		for _, n := range nums {
			out <- n
		}
		close(out)
	}()
	return out
}

func worker(in <-chan int) <-chan int {
	out := make(chan int)
	go func() {
		for n := range in {
			out <- n * n // Square
		}
		close(out)
	}()
	return out
}

func merge(cs ...<-chan int) <-chan int {
	var wg sync.WaitGroup
	out := make(chan int)

	output := func(c <-chan int) {
		for n := range c {
			out <- n
		}
		wg.Done()
	}

	wg.Add(len(cs))
	for _, c := range cs {
		go output(c)
	}

	go func() {
		wg.Wait()
		close(out)
	}()
	return out
}

func main() {
	in := producer(1, 2, 3, 4, 5)
	
	// Fan-out: 2 workers
	c1 := worker(in)
	c2 := worker(in)
	
	// Fan-in: merge results
	for n := range merge(c1, c2) {
		fmt.Println(n)
	}
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q27"></a>
### Q27: How do you use `defer` effectively for cleanup (and avoid common traps)?

**Difficulty**: Intermediate

**Strategy:**
`defer` schedules a function call to run when the surrounding function returns. It's vital for closing files/connections. Note that deferred calls arguments are evaluated immediately, but execution happens later.

**Code Example:**
```go
package main

import (
	"fmt"
	"os"
)

func readFile(filename string) {
	f, err := os.Open(filename)
	if err != nil {
		return
	}
	// Close immediately when function exits
	defer f.Close() 

	// Read logic...
	fmt.Println("Reading file...")
}

func deferTrap() {
	for i := 0; i < 3; i++ {
		// Trap: defer runs at function exit, not loop iteration end
		// This can exhaust file descriptors in tight loops
		defer fmt.Println("Deferred:", i) 
	}
	fmt.Println("Loop done")
}

func main() {
	deferTrap() 
	// Output: Loop done, Deferred: 2, Deferred: 1, Deferred: 0 (LIFO)
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q28"></a>
### Q28: How do you implement a custom HTTP RoundTripper?

**Difficulty**: Expert

**Strategy:**
A custom `http.RoundTripper` allows you to intercept and modify requests/responses globally for an `http.Client`. Useful for logging, caching, or adding auth headers.

**Code Example:**
```go
package main

import (
	"fmt"
	"net/http"
)

type AuthTransport struct {
	Token string
	Base  http.RoundTripper
}

func (t *AuthTransport) RoundTrip(req *http.Request) (*http.Response, error) {
	// Modify Request
	req.Header.Add("Authorization", "Bearer "+t.Token)
	
	// Call base RoundTripper (or DefaultTransport)
	return t.Base.RoundTrip(req)
}

func main() {
	client := &http.Client{
		Transport: &AuthTransport{
			Token: "secret-token",
			Base:  http.DefaultTransport,
		},
	}
	
	// Request will have Auth header
	resp, err := client.Get("https://httpbin.org/headers")
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()
	
	fmt.Println("Status:", resp.Status)
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q29"></a>
### Q29: How do you use `reflect` to iterate over struct fields?

**Difficulty**: Expert

**Strategy:**
Reflection (`reflect` package) allows runtime inspection of types. It's powerful but slow and unsafe. Use it for serialization, ORMs, or generic tools.

**Code Example:**
```go
package main

import (
	"fmt"
	"reflect"
)

type Config struct {
	Host string `env:"HOST"`
	Port int    `env:"PORT"`
}

func PrintTags(v interface{}) {
	val := reflect.ValueOf(v)
	typ := reflect.TypeOf(v)

	for i := 0; i < val.NumField(); i++ {
		field := typ.Field(i)
		value := val.Field(i)
		tag := field.Tag.Get("env")
		
		fmt.Printf("Field: %s, Value: %v, Tag: %s
", field.Name, value, tag)
	}
}

func main() {
	c := Config{Host: "localhost", Port: 8080}
	PrintTags(c)
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q30"></a>
### Q30: How do you use `slices` package (Go 1.21+) for common operations?

**Difficulty**: Intermediate

**Strategy:**
Go 1.21 introduced the `slices` package for generic slice operations like sorting, searching, and modifying, replacing the need for custom utility functions.

**Code Example:**
```go
package main

import (
	"fmt"
	"slices"
)

func main() {
	nums := []int{5, 2, 9, 1, 5}

	// Sort
	slices.Sort(nums)
	fmt.Println("Sorted:", nums)

	// Binary Search (on sorted slice)
	idx, found := slices.BinarySearch(nums, 9)
	fmt.Printf("Found 9 at index %d: %v
", idx, found)

	// Compact (remove adjacent duplicates)
	nums = slices.Compact(nums)
	fmt.Println("Compact:", nums)

	// Contains
	hasTwo := slices.Contains(nums, 2)
	fmt.Println("Has 2:", hasTwo)
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---


---

<a id="q31"></a>
### Q31: How do you use the new `slices` package (Go 1.21+) for common operations?

**Difficulty**: Beginner

**Strategy:**
The `slices` package provides generic functions for common slice operations like sorting, searching, and reversing. It is more efficient and type-safe than the older `sort` package.

**Code Example:**
```go
package main

import (
    "fmt"
    "slices"
)

func main() {
    nums := []int{5, 2, 9, 1, 5, 6}

    // Sort
    slices.Sort(nums)
    fmt.Println("Sorted:", nums) // [1 2 5 5 6 9]

    // Binary Search (must be sorted)
    idx, found := slices.BinarySearch(nums, 6)
    fmt.Printf("Found 6 at index %d: %v\n", idx, found)

    // Compact (remove consecutive duplicates)
    nums = slices.Compact(nums)
    fmt.Println("Compact:", nums) // [1 2 5 6 9]

    // Max
    maxVal := slices.Max(nums)
    fmt.Println("Max:", maxVal)
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q32"></a>
### Q32: How do you iterate over an integer range using `range` in Go 1.22+?

**Difficulty**: Beginner

**Strategy:**
Go 1.22 introduced iterating over integers directly in `range` loops, replacing the traditional `for i := 0; i < n; i++` syntax.

**Code Example:**
```go
package main

import "fmt"

func main() {
    // Iterate from 0 to 4 (exclusive of 5)
    for i := range 5 {
        fmt.Println(i)
    }

    // Works with variable
    n := 3
    for i := range n {
        fmt.Printf("Index: %d\n", i)
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q33"></a>
### Q33: How do you use `cmp.Or` (Go 1.22+) to return the first non-zero value?

**Difficulty**: Intermediate

**Strategy:**
`cmp.Or` returns the first argument that is not the zero value for its type. It's useful for setting default values or falling back to secondary configurations.

**Code Example:**
```go
package main

import (
    "cmp"
    "fmt"
    "os"
)

func main() {
    // Simulating environment variables
    userEnv := ""
    defaultUser := "Guest"

    // Returns userEnv if not empty, otherwise defaultUser
    currentUser := cmp.Or(userEnv, defaultUser)
    fmt.Println("User:", currentUser)

    // Works with numbers too (0 is zero value)
    port := cmp.Or(0, 8080)
    fmt.Println("Port:", port)
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q34"></a>
### Q34: How do you create a structured logger using `log/slog` (Go 1.21+)?

**Difficulty**: Intermediate

**Strategy:**
`log/slog` provides structured, leveled logging. It supports key-value pairs and different output formats (Text, JSON) natively.

**Code Example:**
```go
package main

import (
    "log/slog"
    "os"
)

func main() {
    // JSON Logger
    logger := slog.New(slog.NewJSONHandler(os.Stdout, nil))

    // Log with attributes
    logger.Info("User logged in",
        "user_id", 42,
        "status", "success",
        slog.Group("meta",
            "ip", "192.168.1.1",
            "region", "us-east-1",
        ),
    )
    
    // Error logging
    logger.Error("Database connection failed", "retry_count", 3)
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q35"></a>
### Q35: How do you use `sync.OnceValue` (Go 1.21+) for lazy initialization?

**Difficulty**: Intermediate

**Strategy:**
`sync.OnceValue` returns a function that invokes the initializer only once and returns the value. Subsequent calls return the same value without re-executing the initializer.

**Code Example:**
```go
package main

import (
    "fmt"
    "sync"
)

func main() {
    // Initialize expensive resource lazily
    getConfig := sync.OnceValue(func() map[string]string {
        fmt.Println("Loading config...")
        return map[string]string{"env": "production"}
    })

    // First call runs the function
    fmt.Println(getConfig())

    // Second call returns cached value
    fmt.Println(getConfig())
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q36"></a>
### Q36: How do you check for race conditions in Go?

**Difficulty**: Intermediate

**Strategy:**
Use the built-in race detector by adding the `-race` flag when running tests or the application: `go run -race main.go` or `go test -race`.

**Code Example:**
```go
// Run with: go run -race main.go
package main

import (
    "fmt"
    "sync"
)

func main() {
    var count int
    var wg sync.WaitGroup

    // This code has a race condition
    for i := 0; i < 1000; i++ {
        wg.Add(1)
        go func() {
            defer wg.Done()
            count++ // Unsafe concurrent access
        }()
    }
    wg.Wait()
    fmt.Println("Count:", count)
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q37"></a>
### Q37: How do you use `context.WithTimeout` to cancel long-running operations?

**Difficulty**: Intermediate

**Strategy:**
Wrap the parent context with a timeout. Pass the context to the operation. The operation should listen to `ctx.Done()`.

**Code Example:**
```go
package main

import (
    "context"
    "fmt"
    "time"
)

func slowOperation(ctx context.Context) {
    select {
    case <-time.After(2 * time.Second):
        fmt.Println("Operation finished")
    case <-ctx.Done():
        fmt.Println("Operation cancelled:", ctx.Err())
    }
}

func main() {
    // Create context that cancels after 1 second
    ctx, cancel := context.WithTimeout(context.Background(), 1*time.Second)
    defer cancel() // Always call cancel to release resources

    slowOperation(ctx)
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q38"></a>
### Q38: How do you embed static files into a Go binary?

**Difficulty**: Beginner

**Strategy:**
Use the `//go:embed` directive to include files or directories at compile time. Access them via `string`, `[]byte`, or `embed.FS`.

**Code Example:**
```go
package main

import (
    "embed"
    "fmt"
)

//go:embed config.json
var configData string

//go:embed static/*
var staticFiles embed.FS

func main() {
    fmt.Println("Config Content:", configData)

    content, _ := staticFiles.ReadFile("static/index.html")
    fmt.Println("Index HTML:", string(content))
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q39"></a>
### Q39: How do you perform atomic operations to avoid mutexes?

**Difficulty**: Advanced

**Strategy:**
Use the `sync/atomic` package for low-level atomic memory primitives. This is faster than Mutex for simple counters or boolean flags.

**Code Example:**
```go
package main

import (
    "fmt"
    "sync"
    "sync/atomic"
)

func main() {
    var ops atomic.Int64
    var wg sync.WaitGroup

    for i := 0; i < 50; i++ {
        wg.Add(1)
        go func() {
            defer wg.Done()
            ops.Add(1) // Atomic increment
        }()
    }

    wg.Wait()
    fmt.Println("Ops:", ops.Load())
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q40"></a>
### Q40: How do you benchmark Go code?

**Difficulty**: Intermediate

**Strategy:**
Create a test file ending in `_test.go` and functions starting with `Benchmark`. Use `b.N` to loop the operation. Run with `go test -bench=.`.

**Code Example:**
```go
package main

import (
    "fmt"
    "testing"
)

func Calculate(n int) int {
    return n * n
}

// Run: go test -bench=.
func BenchmarkCalculate(b *testing.B) {
    for i := 0; i < b.N; i++ {
        Calculate(100)
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q41"></a>
### Q41: How do you marshal JSON with custom field names or omission?

**Difficulty**: Beginner

**Strategy:**
Use struct tags like `json:"name"` to rename fields and `json:"-"` to ignore them. `omitempty` omits the field if it has a zero value.

**Code Example:**
```go
package main

import (
    "encoding/json"
    "fmt"
)

type User struct {
    ID       int    `json:"id"`
    Name     string `json:"username"`
    Password string `json:"-"` // Ignored
    Email    string `json:"email,omitempty"`
}

func main() {
    u := User{ID: 1, Name: "Alice", Password: "secret"}
    
    data, _ := json.Marshal(u)
    fmt.Println(string(data)) 
    // Output: {"id":1,"username":"Alice"} (Email omitted)
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q42"></a>
### Q42: How do you implement a simple HTTP middleware?

**Difficulty**: Intermediate

**Strategy:**
Middleware is a function that takes an `http.Handler` and returns an `http.Handler`. It wraps the inner handler to execute logic before or after it.

**Code Example:**
```go
package main

import (
    "fmt"
    "net/http"
    "time"
)

func LoggingMiddleware(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        start := time.Now()
        next.ServeHTTP(w, r) // Call next handler
        fmt.Printf("%s %s took %v\n", r.Method, r.URL.Path, time.Since(start))
    })
}

func hello(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintln(w, "Hello, World!")
}

func main() {
    mux := http.NewServeMux()
    mux.HandleFunc("/", hello)
    
    http.ListenAndServe(":8080", LoggingMiddleware(mux))
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q43"></a>
### Q43: How do you detect and handle panics in a Goroutine?

**Difficulty**: Intermediate

**Strategy:**
Use `recover()` inside a `defer` function. This must be done within the goroutine where the panic might occur, as panics do not propagate across goroutine boundaries.

**Code Example:**
```go
package main

import "fmt"

func riskyTask() {
    defer func() {
        if r := recover(); r != nil {
            fmt.Println("Recovered from panic:", r)
        }
    }()
    
    panic("Something went wrong!")
}

func main() {
    go riskyTask()
    
    // Wait for goroutine (for demo purposes)
    var input string
    fmt.Scanln(&input)
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q44"></a>
### Q44: How do you use `io.Pipe` to stream data between a reader and writer?

**Difficulty**: Advanced

**Strategy:**
`io.Pipe` creates a synchronous in-memory pipe. Data written to the `PipeWriter` is available to be read from the `PipeReader`. Useful for connecting streams without buffering everything in memory.

**Code Example:**
```go
package main

import (
    "fmt"
    "io"
    "os"
)

func main() {
    pr, pw := io.Pipe()

    // Writer goroutine
    go func() {
        defer pw.Close()
        fmt.Fprintln(pw, "Hello from pipe!")
    }()

    // Reader (Main thread)
    io.Copy(os.Stdout, pr)
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q45"></a>
### Q45: How do you use Go Fuzzing (Go 1.18+) to find bugs?

**Difficulty**: Advanced

**Strategy:**
Go Fuzzing automatically generates random inputs to test your code for edge cases and crashes. Use `FuzzXxx` functions in test files.

**Code Example:**
```go
func FuzzReverse(f *testing.F) {
    f.Add("hello") // Seed corpus
    f.Fuzz(func(t *testing.T, orig string) {
        rev := Reverse(orig)
        doubleRev := Reverse(rev)
        if orig != doubleRev {
            t.Errorf("Before: %q, after: %q", orig, doubleRev)
        }
    })
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q46"></a>
### Q46: How do you use sync.Map for concurrent map access?

**Difficulty**: Intermediate

**Strategy:**
`sync.Map` is a thread-safe map implementation optimized for cases where keys are only written once but read many times, or when disjoint sets of keys are used by different goroutines.

**Code Example:**
```go
var m sync.Map

// Store
m.Store("key", "value")

// Load
if val, ok := m.Load("key"); ok {
    fmt.Println("Value:", val)
}

// LoadOrStore
actual, loaded := m.LoadOrStore("key", "newValue")
fmt.Println(actual, loaded)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q47"></a>
### Q47: How do you use atomic.Pointer[T] (Go 1.19+)?

**Difficulty**: Advanced

**Strategy:**
`atomic.Pointer[T]` provides type-safe atomic operations on pointers, avoiding the need for `unsafe.Pointer` or `atomic.Value`.

**Code Example:**
```go
import "sync/atomic"

type Config struct {
    Port int
}

var config atomic.Pointer[Config]

func UpdateConfig(c *Config) {
    config.Store(c)
}

func GetConfig() *Config {
    return config.Load()
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q48"></a>
### Q48: How do you use httptest to test HTTP handlers?

**Difficulty**: Intermediate

**Strategy:**
`httptest` provides utilities to test HTTP handlers without starting a real server. Use `NewRecorder` to capture the response.

**Code Example:**
```go
func TestHandler(t *testing.T) {
    req := httptest.NewRequest("GET", "/", nil)
    w := httptest.NewRecorder()

    MyHandler(w, req)

    resp := w.Result()
    if resp.StatusCode != http.StatusOK {
        t.Errorf("Expected 200, got %d", resp.StatusCode)
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q49"></a>
### Q49: How do you use json.RawMessage to delay parsing?

**Difficulty**: Intermediate

**Strategy:**
`json.RawMessage` allows you to store a part of the JSON as raw bytes and decode it later based on other fields (e.g., a `type` field).

**Code Example:**
```go
type Event struct {
    Type string          `json:"type"`
    Data json.RawMessage `json:"data"`
}

func parse(e Event) {
    if e.Type == "login" {
        var l LoginPayload
        json.Unmarshal(e.Data, &l)
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q50"></a>
### Q50: How do you use pprof to profile CPU usage?

**Difficulty**: Advanced

**Strategy:**
Import `net/http/pprof` and start an HTTP server. Then use the `go tool pprof` command to analyze CPU profiles.

**Code Example:**
```go
import _ "net/http/pprof"

func main() {
    go func() {
        http.ListenAndServe("localhost:6060", nil)
    }()
    // ... app logic
}

// go tool pprof http://localhost:6060/debug/pprof/profile?seconds=30
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q51"></a>
### Q51: How do you use runtime/trace to analyze latency?

**Difficulty**: Expert

**Strategy:**
Use `runtime/trace` to capture execution traces, including goroutine scheduling, GC pauses, and blocking syscalls. View with `go tool trace`.

**Code Example:**
```go
f, _ := os.Create("trace.out")
defer f.Close()
trace.Start(f)
defer trace.Stop()

// Run workload...
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q52"></a>
### Q52: How do you use Go Workspaces (Go 1.18+) for multi-module development?

**Difficulty**: Intermediate

**Strategy:**
Workspaces allow you to work on multiple modules simultaneously without publishing them. Create a `go.work` file using `go work init`.

**Code Example:**
```bash
# go.work
go 1.21

use (
    ./my-app
    ./my-lib
)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q53"></a>
### Q53: How do you implement a custom Scanner using bufio?

**Difficulty**: Intermediate

**Strategy:**
Use `bufio.Scanner` with a custom `SplitFunc` to parse data streams based on custom delimiters or protocols.

**Code Example:**
```go
scanner := bufio.NewScanner(reader)
scanner.Split(func(data []byte, atEOF bool) (int, []byte, error) {
    // Custom splitting logic
    return 0, nil, nil
})

for scanner.Scan() {
    fmt.Println(scanner.Text())
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q54"></a>
### Q54: How do you use text/template for generating dynamic content?

**Difficulty**: Intermediate

**Strategy:**
`text/template` implements data-driven templates. It allows logic like loops and conditions within the template string.

**Code Example:**
```go
tmpl, _ := template.New("test").Parse("Hello {{.Name}}!")
tmpl.Execute(os.Stdout, map[string]string{"Name": "World"})
// Output: Hello World!
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q55"></a>
### Q55: How do you use Singleflight to prevent cache stampedes?

**Difficulty**: Advanced

**Strategy:**
Use `golang.org/x/sync/singleflight` to suppress duplicate function calls. If multiple goroutines ask for the same key, only one execution happens.

**Code Example:**
```go
var g singleflight.Group

func getData(key string) (interface{}, error) {
    v, err, _ := g.Do(key, func() (interface{}, error) {
        return fetchFromDB(key) // Executed once
    })
    return v, err
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q56"></a>
### Q56: How do you use sync.Cond for complex synchronization?

**Difficulty**: Expert

**Strategy:**
`sync.Cond` implements a condition variable, allowing goroutines to wait for or signal an event (like a queue becoming non-empty).

**Code Example:**
```go
c := sync.NewCond(&sync.Mutex{})

// Waiter
c.L.Lock()
for !condition() {
    c.Wait()
}
// Process...
c.L.Unlock()

// Signaler
c.L.Lock()
// Change state...
c.Signal() // Wake one
c.L.Unlock()
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q57"></a>
### Q57: How do you use the os/exec package to run external commands safely?

**Difficulty**: Intermediate

**Strategy:**
Use `exec.Command` and `CommandContext` to run external processes. Ensure inputs are validated to prevent command injection.

**Code Example:**
```go
cmd := exec.Command("ls", "-l")
output, err := cmd.CombinedOutput()
if err != nil {
    log.Fatal(err)
}
fmt.Println(string(output))
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q58"></a>
### Q58: How do you use the plugin package to load code at runtime?

**Difficulty**: Expert

**Strategy:**
Go plugins allow loading shared libraries (`.so` files) at runtime. Use `plugin.Open` and `Lookup` to access symbols.

**Code Example:**
```go
p, _ := plugin.Open("myplugin.so")
sym, _ := p.Lookup("MyFunction")
myFunc := sym.(func())
myFunc()
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q59"></a>
### Q59: How do you use testing/quick for property-based testing?

**Difficulty**: Advanced

**Strategy:**
`testing/quick` performs black-box testing by generating random input values to verify properties of a function.

**Code Example:**
```go
func TestOdd(t *testing.T) {
    f := func(x int) bool {
        if x%2 == 0 {
            return !IsOdd(x)
        }
        return IsOdd(x)
    }
    if err := quick.Check(f, nil); err != nil {
        t.Error(err)
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q60"></a>
### Q60: How do you use context.AfterFunc (Go 1.21+) for cleanup?

**Difficulty**: Intermediate

**Strategy:**
`context.AfterFunc` registers a function to be called when the context is done. It's useful for cleaning up resources associated with a context asynchronously.

**Code Example:**
```go
stop := context.AfterFunc(ctx, func() {
    fmt.Println("Context done, cleaning up...")
})
// stop() can be called to unregister if needed
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q61"></a>
### Q61: How do you use the new min/max built-ins (Go 1.21+)?

**Difficulty**: Beginner

**Strategy:**
Go 1.21 introduced built-in `min` and `max` functions for ordered types, simplifying basic comparisons.

**Code Example:**
```go
a, b := 10, 20
m := max(a, b)
fmt.Println(m) // 20
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---

<a id="q62"></a>

### Q62: How do you reduce GC pressure using `sync.Pool`?

**Difficulty**: Advanced

**Strategy:**
`sync.Pool` caches allocated but unused objects for later reuse, relieving pressure on the garbage collector. Ideal for frequently allocated objects like buffers.

**Code Example:**

```go
package main

import (
	"bytes"
	"sync"
)

var bufPool = sync.Pool{
	New: func() interface{} {
		return new(bytes.Buffer)
	},
}

func main() {
	b := bufPool.Get().(*bytes.Buffer)
	b.Reset()
	b.WriteString("Hello")
	bufPool.Put(b)
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q63"></a>

### Q63: How do you use `sync.Cond` for complex synchronization?

**Difficulty**: Expert

**Strategy:**
`sync.Cond` implements a condition variable, a rendezvous point for goroutines waiting for or announcing the occurrence of an event. It's more efficient than polling.

**Code Example:**

```go
package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	var mu sync.Mutex
	cond := sync.NewCond(&mu)
	ready := false

	go func() {
		time.Sleep(time.Second)
		mu.Lock()
		ready = true
		cond.Signal() // Wake up one waiter
		mu.Unlock()
	}()

	mu.Lock()
	for !ready {
		cond.Wait() // Unlocks mu, waits, locks mu
	}
	fmt.Println("Ready!")
	mu.Unlock()
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q64"></a>

### Q64: How do you perform lock-free operations using `atomic`?

**Difficulty**: Advanced

**Strategy:**
The `sync/atomic` package provides low-level atomic memory primitives useful for implementing synchronization algorithms.

**Code Example:**

```go
package main

import (
	"fmt"
	"sync/atomic"
)

func main() {
	var ops int64

	// Increment atomically
	atomic.AddInt64(&ops, 1)

	// Load safely
	val := atomic.LoadInt64(&ops)
	fmt.Println(val) // 1
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q65"></a>

### Q65: How do you manage groups of goroutines with `errgroup`?

**Difficulty**: Intermediate

**Strategy:**
`golang.org/x/sync/errgroup` provides synchronization, error propagation, and context cancellation for groups of goroutines working on a subtask.

**Code Example:**

```go
package main

import (
	"context"
	"fmt"
	"golang.org/x/sync/errgroup"
)

func main() {
	g, _ := errgroup.WithContext(context.Background())

	g.Go(func() error {
		return nil
	})

	g.Go(func() error {
		return fmt.Errorf("something went wrong")
	})

	if err := g.Wait(); err != nil {
		fmt.Println("Error:", err)
	}
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q66"></a>

### Q66: What is Escape Analysis?

**Difficulty**: Advanced

**Strategy:**
It's a compiler phase that determines whether variables can be allocated on the stack (fast) or must "escape" to the heap (slower, GC managed). Inspect with `go build -gcflags="-m"`.

**Code Example:**

```go
package main

func create() *int {
	x := 10
	return &x // x escapes to heap because it's returned
}

func main() {
	_ = create()
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q67"></a>

### Q67: How do you tune the Garbage Collector with `GOGC`?

**Difficulty**: Advanced

**Strategy:**
`GOGC` sets the percentage of new heap growth before a GC run. Default is 100 (wait until heap doubles). `GOGC=off` disables GC.

**Code Example:**

```bash
# Run with aggressive GC (50% growth)
GOGC=50 go run main.go

# Run with no GC
GOGC=off go run main.go
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q68"></a>

### Q68: How do you write Fuzz Tests in Go (1.18+)?

**Difficulty**: Intermediate

**Strategy:**
Use `FuzzXxx` functions in `_test.go`. Fuzzing feeds random data to your test to find edge cases and crashes.

**Code Example:**

```go
package main

import "testing"

func Reverse(s string) string { return s } // Buggy

func FuzzReverse(f *testing.F) {
	f.Add("hello")
	f.Fuzz(func(t *testing.T, orig string) {
		rev := Reverse(orig)
		doubleRev := Reverse(rev)
		if orig != doubleRev {
			t.Errorf("Before: %q, after: %q", orig, doubleRev)
		}
	})
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q69"></a>

### Q69: How do you test HTTP handlers with `httptest`?

**Difficulty**: Intermediate

**Strategy:**
Use `httptest.NewRecorder` to record the response of an HTTP handler without spinning up a real server.

**Code Example:**

```go
package main

import (
	"net/http"
	"net/http/httptest"
	"testing"
)

func handler(w http.ResponseWriter, r *http.Request) {
	w.WriteHeader(http.StatusOK)
}

func TestHandler(t *testing.T) {
	req := httptest.NewRequest("GET", "/", nil)
	w := httptest.NewRecorder()

	handler(w, req)

	if w.Result().StatusCode != http.StatusOK {
		t.Error("Expected 200 OK")
	}
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q70"></a>

### Q70: How do you benchmark code?

**Difficulty**: Intermediate

**Strategy:**
Use `BenchmarkXxx` functions in `_test.go`. Run with `go test -bench=.`. Use `b.ResetTimer()` to ignore setup time.

**Code Example:**

```go
package main

import "testing"

func BenchmarkAppend(b *testing.B) {
	for i := 0; i < b.N; i++ {
		_ = append([]int{}, i)
	}
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q71"></a>

### Q71: How do you profile a Go application?

**Difficulty**: Advanced

**Strategy:**
Use `net/http/pprof` for web apps or `runtime/pprof` for CLI. Inspect profiles using `go tool pprof`. It shows CPU usage, memory allocation, and blocking goroutines.

**Code Example:**

```go
package main

import (
	"net/http"
	_ "net/http/pprof" // Registers handlers
)

func main() {
	http.ListenAndServe(":6060", nil)
}
// go tool pprof http://localhost:6060/debug/pprof/profile
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q72"></a>

### Q72: How do you use Go Workspaces (`go.work`)?

**Difficulty**: Intermediate

**Strategy:**
Workspaces allow you to work on multiple modules simultaneously without publishing them. Create a `go.work` file referencing local module paths.

**Code Example:**

```go
// go.work
go 1.21

use (
    ./my-app
    ./my-library
)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q73"></a>

### Q73: How do you embed files into the binary?

**Difficulty**: Beginner

**Strategy:**
Use the `//go:embed` directive (Go 1.16+) to include static files (HTML, SQL, Config) in the compiled binary.

**Code Example:**

```go
package main

import (
	"embed"
	"fmt"
)

//go:embed config.txt
var content string

//go:embed templates/*.html
var templates embed.FS

func main() {
	fmt.Println(content)
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q74"></a>

### Q74: How do you handle Context timeouts?

**Difficulty**: Intermediate

**Strategy:**
Use `context.WithTimeout` to ensure operations don't hang forever. Always `defer cancel()` to release resources.

**Code Example:**

```go
package main

import (
	"context"
	"fmt"
	"time"
)

func main() {
	ctx, cancel := context.WithTimeout(context.Background(), 100*time.Millisecond)
	defer cancel()

	select {
	case <-time.After(200 * time.Millisecond):
		fmt.Println("Done")
	case <-ctx.Done():
		fmt.Println("Timeout:", ctx.Err()) // Timeout: context deadline exceeded
	}
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q75"></a>

### Q75: How do you implement Graceful Shutdown?

**Difficulty**: Advanced

**Strategy:**
Listen for OS signals (`SIGINT`, `SIGTERM`) and shutdown the server using `server.Shutdown(ctx)`. This allows active requests to complete.

**Code Example:**

```go
package main

import (
	"context"
	"net/http"
	"os"
	"os/signal"
	"syscall"
)

func main() {
	srv := &http.Server{Addr: ":8080"}
	
	go func() {
		stop := make(chan os.Signal, 1)
		signal.Notify(stop, syscall.SIGINT, syscall.SIGTERM)
		<-stop
		srv.Shutdown(context.Background())
	}()

	srv.ListenAndServe()
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q76"></a>

### Q76: How do you implement a Worker Pool?

**Difficulty**: Advanced

**Strategy:**
Create a fixed number of worker goroutines that consume tasks from a buffered channel. This limits concurrency and resource usage.

**Code Example:**

```go
package main

import "fmt"

func worker(id int, jobs <-chan int, results chan<- int) {
	for j := range jobs {
		fmt.Printf("worker %d started job %d\n", id, j)
		results <- j * 2
	}
}

func main() {
	jobs := make(chan int, 100)
	results := make(chan int, 100)

	for w := 1; w <= 3; w++ {
		go worker(w, jobs, results)
	}

	for j := 1; j <= 5; j++ {
		jobs <- j
	}
	close(jobs)

	for a := 1; a <= 5; a++ {
		<-results
	}
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q77"></a>

### Q77: How do you use `iota` for enumerations?

**Difficulty**: Beginner

**Strategy:**
`iota` is a predeclared identifier representing the untyped integer ordinal number of the current const specification. It simplifies creating auto-incrementing constants.

**Code Example:**

```go
package main

import "fmt"

type Status int

const (
	Pending Status = iota // 0
	Running               // 1
	Failed                // 2
)

func main() {
	fmt.Println(Running) // 1
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q78"></a>

### Q78: What is Variable Shadowing and how to avoid it?

**Difficulty**: Beginner

**Strategy:**
It occurs when a variable in an inner scope has the same name as a variable in an outer scope, hiding the outer one. Use `go vet` or linters to detect it.

**Code Example:**

```go
func main() {
	x := 10
	if true {
		x := 5 // Shadows outer x
		print(x) // 5
	}
	print(x) // 10
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q79"></a>

### Q79: What does a Slice Header look like internally?

**Difficulty**: Advanced

**Strategy:**
A slice is a struct with three fields: a pointer to the underlying array, a length, and a capacity. Understanding this helps avoid memory leaks and performance issues.

**Code Example:**

```go
package main

import (
	"fmt"
	"reflect"
	"unsafe"
)

func main() {
	s := []int{1, 2, 3}
	header := (*reflect.SliceHeader)(unsafe.Pointer(&s))
	
	fmt.Printf("Data: %x, Len: %d, Cap: %d\n", header.Data, header.Len, header.Cap)
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q80"></a>

### Q80: How do you recover from a panic?

**Difficulty**: Intermediate

**Strategy:**
Use the `recover()` function inside a deferred function. It stops the panicking sequence and returns the error value passed to `panic()`.

**Code Example:**

```go
package main

import "fmt"

func safe() {
	defer func() {
		if r := recover(); r != nil {
			fmt.Println("Recovered from:", r)
		}
	}()
	panic("boom")
}

func main() {
	safe()
	fmt.Println("Continued")
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q81"></a>

### Q81: How do you implement the Middleware pattern in Go?

**Difficulty**: Intermediate

**Strategy:**
Middleware wraps an `http.Handler` to perform pre- or post-processing (logging, auth) before calling the next handler.

**Code Example:**

```go
func loggingMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		log.Println(r.RequestURI)
		next.ServeHTTP(w, r)
	})
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q82"></a>

### Q82: How do you customize JSON marshaling?

**Difficulty**: Intermediate

**Strategy:**
Implement the `json.Marshaler` interface (`MarshalJSON()`) or `json.Unmarshaler` interface (`UnmarshalJSON()`) on your type.

**Code Example:**

```go
type User struct {
	Name string
}

func (u User) MarshalJSON() ([]byte, error) {
	return []byte(`{"name": "Super ` + u.Name + `"}`), nil
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q83"></a>

### Q83: What is the difference between `time.Ticker` and `time.Timer`?

**Difficulty**: Intermediate

**Strategy:**
`Ticker` fires repeatedly at an interval (for periodic tasks). `Timer` fires once after a delay (for timeouts). Both must be stopped to release resources.

**Code Example:**

```go
ticker := time.NewTicker(1 * time.Second)
defer ticker.Stop()

timer := time.NewTimer(5 * time.Second)
defer timer.Stop()

select {
case <-ticker.C:
	fmt.Println("Tick")
case <-timer.C:
	fmt.Println("Timeout")
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q84"></a>

### Q84: How do you inspect types at runtime using `reflect`?

**Difficulty**: Advanced

**Strategy:**
The `reflect` package allows inspecting the type and value of objects at runtime. It's powerful but slow and unsafe; use sparingly.

**Code Example:**

```go
import "reflect"

func printType(i interface{}) {
	t := reflect.TypeOf(i)
	v := reflect.ValueOf(i)
	fmt.Printf("Type: %s, Value: %v\n", t, v)
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q85"></a>

### Q85: How do you bypass type safety with `unsafe`?

**Difficulty**: Expert

**Strategy:**
The `unsafe` package allows operations that bypass Go's type safety, like converting a pointer of one type to another. Essential for low-level optimizations but dangerous.

**Code Example:**

```go
import "unsafe"

func float64bits(f float64) uint64 {
	return *(*uint64)(unsafe.Pointer(&f))
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q86"></a>

### Q86: How do you use Build Tags?

**Difficulty**: Intermediate

**Strategy:**
Build tags (constraints) control which files are included in the build. Add `//go:build tagname` at the top of the file.

**Code Example:**

```go
//go:build linux
package main

func init() {
	println("Linux build")
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q87"></a>

### Q87: What are the caveats of the `init()` function?

**Difficulty**: Intermediate

**Strategy:**
`init()` runs before `main()`. It's hard to test, errors can't be handled gracefully (must panic), and order depends on import order. Avoid complex logic in `init()`.

**Code Example:**

```go
var db map[string]string

func init() {
	db = make(map[string]string)
	// If DB connection fails here, we must panic
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q88"></a>

### Q88: How do you load Go plugins at runtime?

**Difficulty**: Advanced

**Strategy:**
Use the `plugin` package to load shared libraries (`.so` files) built with `go build -buildmode=plugin`. Only works on Linux/macOS.

**Code Example:**

```go
p, _ := plugin.Open("myplugin.so")
sym, _ := p.Lookup("MyFunction")
myFunc := sym.(func())
myFunc()
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q89"></a>

### Q89: How do you detect data races?

**Difficulty**: Intermediate

**Strategy:**
Run your tests or application with the `-race` flag. It instruments memory accesses to detect unsynchronized concurrent access.

**Code Example:**

```bash
go test -race ./...
go run -race main.go
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q90"></a>

### Q90: How can re-slicing cause memory leaks?

**Difficulty**: Advanced

**Strategy:**
If you slice a small part of a large array and keep it, the entire underlying array stays in memory. Copy the data to a new slice to release the large array.

**Code Example:**

```go
var small []byte

func process(large []byte) {
    // Bad: keeps 'large' in memory
    // small = large[:10]

    // Good: copies only what is needed
    small = make([]byte, 10)
    copy(small, large[:10])
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q91"></a>

### Q91: When should you use `sync.Map`?

**Difficulty**: Advanced

**Strategy:**
Use `sync.Map` only for specific cases: cache implementations (stable keys) or disjoint sets of keys. For general use, a `map` with a `RWMutex` is faster and type-safe.

**Code Example:**

```go
var m sync.Map

m.Store("key", "value")
if v, ok := m.Load("key"); ok {
	fmt.Println(v)
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q92"></a>

### Q92: How do you suppress duplicate function calls with `singleflight`?

**Difficulty**: Advanced

**Strategy:**
`golang.org/x/sync/singleflight` ensures that only one execution of a function happens for a given key at a time, sharing the result with all callers. Prevents cache stampedes.

**Code Example:**

```go
import "golang.org/x/sync/singleflight"

var g singleflight.Group

func getData(key string) (string, error) {
	v, err, _ := g.Do(key, func() (interface{}, error) {
		return fetchFromDB(key) // Expensive call
	})
	return v.(string), err
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q93"></a>

### Q93: When should you use `crypto/rand` vs `math/rand`?

**Difficulty**: Beginner

**Strategy:**
Use `math/rand` for simulations (fast, deterministic if seeded). Use `crypto/rand` for security (slow, cryptographically secure, OS entropy).

**Code Example:**

```go
import (
	cRand "crypto/rand"
	mRand "math/rand"
)

// Secure
b := make([]byte, 16)
cRand.Read(b)

// Fast
n := mRand.Intn(100)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q94"></a>

### Q94: How do you handle NULL values in SQL databases?

**Difficulty**: Intermediate

**Strategy:**
Use `sql.NullString`, `sql.NullInt64`, etc., or use pointers (`*string`) when scanning database rows.

**Code Example:**

```go
var name sql.NullString
row.Scan(&name)
if name.Valid {
	fmt.Println(name.String)
} else {
	fmt.Println("NULL")
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q95"></a>

### Q95: How do you use Structured Logging (Go 1.21+)?

**Difficulty**: Intermediate

**Strategy:**
Use the `log/slog` package. It provides high-performance, structured logging (JSON, Text) with levels and attributes.

**Code Example:**

```go
import "log/slog"

func main() {
	slog.Info("User logged in", "user_id", 42, "ip", "127.0.0.1")
}
// Output: time=... level=INFO msg="User logged in" user_id=42 ip=127.0.0.1
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q96"></a>

### Q96: Why are `io.Reader` and `io.Writer` important?

**Difficulty**: Beginner

**Strategy:**
They are the fundamental abstractions for I/O in Go. By implementing them, your types can work with files, network connections, buffers, and compressors seamlessly.

**Code Example:**

```go
func Stream(r io.Reader, w io.Writer) {
	io.Copy(w, r)
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q97"></a>

### Q97: How do you read a file line by line?

**Difficulty**: Beginner

**Strategy:**
Use `bufio.Scanner`. It's efficient and handles buffering automatically.

**Code Example:**

```go
f, _ := os.Open("file.txt")
defer f.Close()

scanner := bufio.NewScanner(f)
for scanner.Scan() {
	fmt.Println(scanner.Text())
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q98"></a>

### Q98: How do you run external commands safely?

**Difficulty**: Intermediate

**Strategy:**
Use `os/exec`. Avoid passing raw strings to shell; pass arguments as a slice to prevent injection.

**Code Example:**

```go
cmd := exec.Command("grep", "hello", "file.txt")
out, _ := cmd.Output()
fmt.Println(string(out))
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q99"></a>

### Q99: How do you traverse a directory tree?

**Difficulty**: Intermediate

**Strategy:**
Use `filepath.WalkDir` (more efficient than `Walk`). It streams directory entries.

**Code Example:**

```go
filepath.WalkDir(".", func(path string, d fs.DirEntry, err error) error {
	if !d.IsDir() {
		fmt.Println("File:", path)
	}
	return nil
})
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q100"></a>

### Q100: What are Go Proverbs?

**Difficulty**: Beginner

**Strategy:**
Rob Pike's proverbs capture the essence of Go design. Examples: "Don't communicate by sharing memory, share memory by communicating.", "Concurrency is not parallelism."

**Code Example:**

```go
// Just a concept
fmt.Println("Errors are values.")
fmt.Println("A little copying is better than a little dependency.")
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>
