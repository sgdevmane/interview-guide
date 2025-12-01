<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/golang-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>Golang Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for developers</b></p>
</div>

---

## Table of Contents

1. [How do you manage Goroutine lifecycles to prevent memory leaks?](#q1-how-do-you-manage-goroutine-lifecycles-to-prevent-memory-leaks) <span class="intermediate">Intermediate</span>
2. [How do you implement the Worker Pool pattern to limit concurrency?](#q2-how-do-you-implement-the-worker-pool-pattern-to-limit-concurrency) <span class="intermediate">Intermediate</span>
3. [How do you handle errors gracefully using custom error types and wrapping?](#q3-how-do-you-handle-errors-gracefully-using-custom-error-types-and-wrapping) <span class="intermediate">Intermediate</span>
4. [How do you implement a thread-safe Singleton in Go?](#q4-how-do-you-implement-a-thread-safe-singleton-in-go) <span class="intermediate">Intermediate</span>
5. [How do you use the Functional Options pattern to configure complex structs?](#q5-how-do-you-use-the-functional-options-pattern-to-configure-complex-structs) <span class="intermediate">Intermediate</span>
6. [How do you implement a Graceful Shutdown for an HTTP server?](#q6-how-do-you-implement-a-graceful-shutdown-for-an-http-server) <span class="intermediate">Intermediate</span>
7. [How do you test code effectively using Table-Driven Tests?](#q7-how-do-you-test-code-effectively-using-table-driven-tests) <span class="intermediate">Intermediate</span>
8. [How do you use Generics to create a type-safe Set data structure?](#q8-how-do-you-use-generics-to-create-a-type-safe-set-data-structure) <span class="intermediate">Intermediate</span>
9. [How do you use `sync.WaitGroup` to wait for multiple concurrent operations?](#q9-how-do-you-use-sync.waitgroup-to-wait-for-multiple-concurrent-operations) <span class="intermediate">Intermediate</span>
10. [How do you implement middleware for an HTTP handler?](#q10-how-do-you-implement-middleware-for-an-http-handler) <span class="intermediate">Intermediate</span>
11. [How do you use interfaces for dependency injection to improve testability?](#q11-how-do-you-use-interfaces-for-dependency-injection-to-improve-testability) <span class="intermediate">Intermediate</span>
12. [How do you use the `select` statement to implement a timeout?](#q12-how-do-you-use-the-select-statement-to-implement-a-timeout) <span class="intermediate">Intermediate</span>
13. [How do you use `io.Reader` and `io.Writer` to stream data efficiently?](#q13-how-do-you-use-io.reader-and-io.writer-to-stream-data-efficiently) <span class="intermediate">Intermediate</span>
14. [How do you prevent race conditions using `sync.Mutex`?](#q14-how-do-you-prevent-race-conditions-using-sync.mutex) <span class="intermediate">Intermediate</span>
15. [How do you optimize memory usage with `sync.Pool`?](#q15-how-do-you-optimize-memory-usage-with-sync.pool) <span class="intermediate">Intermediate</span>
16. [How do you implement a custom JSON Marshaler to hide sensitive fields?](#q16-how-do-you-implement-a-custom-json-marshaler-to-hide-sensitive-fields) <span class="intermediate">Intermediate</span>
17. [How do you use `sync.Once` to ensure a function runs exactly once?](#q17-how-do-you-use-sync.once-to-ensure-a-function-runs-exactly-once) <span class="intermediate">Intermediate</span>
18. [How do you implement a rate limiter using a Token Bucket algorithm?](#q18-how-do-you-implement-a-rate-limiter-using-a-token-bucket-algorithm) <span class="intermediate">Intermediate</span>
19. [How do you correctly handle loop variables in Goroutines?](#q19-how-do-you-correctly-handle-loop-variables-in-goroutines) <span class="intermediate">Intermediate</span>
20. [How do you use `go:embed` to bundle static assets?](#q20-how-do-you-use-go:embed-to-bundle-static-assets) <span class="intermediate">Intermediate</span>
21. [How do you use `errgroup` to manage parallel tasks with error propagation?](#q21-how-do-you-use-errgroup-to-manage-parallel-tasks-with-error-propagation) <span class="intermediate">Intermediate</span>
22. [How do you implement atomic counters using `sync/atomic`?](#q22-how-do-you-implement-atomic-counters-using-syncatomic) <span class="intermediate">Intermediate</span>
23. [How do you benchmark code using `testing.B`?](#q23-how-do-you-benchmark-code-using-testing.b) <span class="intermediate">Intermediate</span>
24. [How do you optimize memory layout by reordering struct fields?](#q24-how-do-you-optimize-memory-layout-by-reordering-struct-fields) <span class="expert">Expert</span>
25. [How do you use `context.WithValue` to pass request-scoped data?](#q25-how-do-you-use-context.withvalue-to-pass-request-scoped-data) <span class="intermediate">Intermediate</span>
26. [How do you implement a simple Fan-Out/Fan-In pattern?](#q26-how-do-you-implement-a-simple-fan-outfan-in-pattern) <span class="intermediate">Intermediate</span>
27. [How do you use `defer` effectively for cleanup (and avoid common traps)?](#q27-how-do-you-use-defer-effectively-for-cleanup-and-avoid-common-traps) <span class="intermediate">Intermediate</span>
28. [How do you implement a custom HTTP RoundTripper?](#q28-how-do-you-implement-a-custom-http-roundtripper) <span class="expert">Expert</span>
29. [How do you use `reflect` to iterate over struct fields?](#q29-how-do-you-use-reflect-to-iterate-over-struct-fields) <span class="expert">Expert</span>
30. [How do you use `slices` package (Go 1.21+) for common operations?](#q30-how-do-you-use-slices-package-go-1.21+-for-common-operations) <span class="intermediate">Intermediate</span>
31. [How do you use the new `slices` package (Go 1.21+) for common operations?](#q31-how-do-you-use-the-new-slices-package-go-1.21+-for-common-operations) <span class="beginner">Beginner</span>
32. [How do you iterate over an integer range using `range` in Go 1.22+?](#q32-how-do-you-iterate-over-an-integer-range-using-range-in-go-1.22+) <span class="beginner">Beginner</span>
33. [How do you use `cmp.Or` (Go 1.22+) to return the first non-zero value?](#q33-how-do-you-use-cmp.or-go-1.22+-to-return-the-first-non-zero-value) <span class="intermediate">Intermediate</span>
34. [How do you create a structured logger using `log/slog` (Go 1.21+)?](#q34-how-do-you-create-a-structured-logger-using-logslog-go-1.21+) <span class="intermediate">Intermediate</span>
35. [How do you use `sync.OnceValue` (Go 1.21+) for lazy initialization?](#q35-how-do-you-use-sync.oncevalue-go-1.21+-for-lazy-initialization) <span class="intermediate">Intermediate</span>
36. [How do you check for race conditions in Go?](#q36-how-do-you-check-for-race-conditions-in-go) <span class="intermediate">Intermediate</span>
37. [How do you use `context.WithTimeout` to cancel long-running operations?](#q37-how-do-you-use-context.withtimeout-to-cancel-long-running-operations) <span class="intermediate">Intermediate</span>
38. [How do you embed static files into a Go binary?](#q38-how-do-you-embed-static-files-into-a-go-binary) <span class="beginner">Beginner</span>
39. [How do you perform atomic operations to avoid mutexes?](#q39-how-do-you-perform-atomic-operations-to-avoid-mutexes) <span class="advanced">Advanced</span>
40. [How do you benchmark Go code?](#q40-how-do-you-benchmark-go-code) <span class="intermediate">Intermediate</span>
41. [How do you marshal JSON with custom field names or omission?](#q41-how-do-you-marshal-json-with-custom-field-names-or-omission) <span class="beginner">Beginner</span>
42. [How do you implement a simple HTTP middleware?](#q42-how-do-you-implement-a-simple-http-middleware) <span class="intermediate">Intermediate</span>
43. [How do you detect and handle panics in a Goroutine?](#q43-how-do-you-detect-and-handle-panics-in-a-goroutine) <span class="intermediate">Intermediate</span>
44. [How do you use `io.Pipe` to stream data between a reader and writer?](#q44-how-do-you-use-io.pipe-to-stream-data-between-a-reader-and-writer) <span class="advanced">Advanced</span>
45. [How do you use Go Fuzzing (Go 1.18+) to find bugs?](#q45-how-do-you-use-go-fuzzing-go-1.18+-to-find-bugs) <span class="advanced">Advanced</span>
46. [How do you use sync.Map for concurrent map access?](#q46-how-do-you-use-sync.map-for-concurrent-map-access) <span class="intermediate">Intermediate</span>
47. [How do you use atomic.Pointer[T] (Go 1.19+)?](#q47-how-do-you-use-atomic.pointer[t]-go-1.19+) <span class="advanced">Advanced</span>
48. [How do you use httptest to test HTTP handlers?](#q48-how-do-you-use-httptest-to-test-http-handlers) <span class="intermediate">Intermediate</span>
49. [How do you use json.RawMessage to delay parsing?](#q49-how-do-you-use-json.rawmessage-to-delay-parsing) <span class="intermediate">Intermediate</span>
50. [How do you use pprof to profile CPU usage?](#q50-how-do-you-use-pprof-to-profile-cpu-usage) <span class="advanced">Advanced</span>
51. [How do you use runtime/trace to analyze latency?](#q51-how-do-you-use-runtimetrace-to-analyze-latency) <span class="expert">Expert</span>
52. [How do you use Go Workspaces (Go 1.18+) for multi-module development?](#q52-how-do-you-use-go-workspaces-go-1.18+-for-multi-module-development) <span class="intermediate">Intermediate</span>
53. [How do you implement a custom Scanner using bufio?](#q53-how-do-you-implement-a-custom-scanner-using-bufio) <span class="intermediate">Intermediate</span>
54. [How do you use text/template for generating dynamic content?](#q54-how-do-you-use-texttemplate-for-generating-dynamic-content) <span class="intermediate">Intermediate</span>
55. [How do you use Singleflight to prevent cache stampedes?](#q55-how-do-you-use-singleflight-to-prevent-cache-stampedes) <span class="advanced">Advanced</span>
56. [How do you use sync.Cond for complex synchronization?](#q56-how-do-you-use-sync.cond-for-complex-synchronization) <span class="expert">Expert</span>
57. [How do you use the os/exec package to run external commands safely?](#q57-how-do-you-use-the-osexec-package-to-run-external-commands-safely) <span class="intermediate">Intermediate</span>
58. [How do you use the plugin package to load code at runtime?](#q58-how-do-you-use-the-plugin-package-to-load-code-at-runtime) <span class="expert">Expert</span>
59. [How do you use testing/quick for property-based testing?](#q59-how-do-you-use-testingquick-for-property-based-testing) <span class="advanced">Advanced</span>
60. [How do you use context.AfterFunc (Go 1.21+) for cleanup?](#q60-how-do-you-use-context.afterfunc-go-1.21+-for-cleanup) <span class="intermediate">Intermediate</span>
61. [How do you use the new min/max built-ins (Go 1.21+)?](#q61-how-do-you-use-the-new-minmax-built-ins-go-1.21+) <span class="beginner">Beginner</span>
62. [How do you debug Go memory leaks in microservices?](#q62-how-do-you-debug-go-memory-leaks-in-microservices) <span class="advanced">Advanced</span>
63. [Best practices for Go code organization in mobile devices?](#q63-best-practices-for-go-code-organization-in-mobile-devices) <span class="beginner">Beginner</span>
64. [How do you implement Go error handling for legacy systems?](#q64-how-do-you-implement-go-error-handling-for-legacy-systems) <span class="intermediate">Intermediate</span>
65. [How do you test Go functionality in cloud infrastructure?](#q65-how-do-you-test-go-functionality-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
66. [How do you handle Go state management in real-time systems?](#q66-how-do-you-handle-go-state-management-in-real-time-systems) <span class="advanced">Advanced</span>
67. [How do you perform Go data validation in distributed systems?](#q67-how-do-you-perform-go-data-validation-in-distributed-systems) <span class="beginner">Beginner</span>
68. [How do you automate Go deployment for high-traffic sites?](#q68-how-do-you-automate-go-deployment-for-high-traffic-sites) <span class="advanced">Advanced</span>
69. [How do you handle Go concurrency issues in embedded systems?](#q69-how-do-you-handle-go-concurrency-issues-in-embedded-systems) <span class="advanced">Advanced</span>
70. [How do you implement Go caching in production environments?](#q70-how-do-you-implement-go-caching-in-production-environments) <span class="intermediate">Intermediate</span>
71. [How do you manage Go configuration for large scale applications?](#q71-how-do-you-manage-go-configuration-for-large-scale-applications) <span class="beginner">Beginner</span>
72. [How do you handle Go internationalization (i18n) in microservices?](#q72-how-do-you-handle-go-internationalization-i18n-in-microservices) <span class="intermediate">Intermediate</span>
73. [How do you ensure Go accessibility (a11y) in mobile devices?](#q73-how-do-you-ensure-go-accessibility-a11y-in-mobile-devices) <span class="beginner">Beginner</span>
74. [How do you optimize Go network requests in legacy systems?](#q74-how-do-you-optimize-go-network-requests-in-legacy-systems) <span class="advanced">Advanced</span>
75. [How do you handle Go performance optimization for cloud infrastructure?](#q75-how-do-you-handle-go-performance-optimization-for-cloud-infrastructure) <span class="advanced">Advanced</span>
76. [What are the security implications of Go in real-time systems?](#q76-what-are-the-security-implications-of-go-in-real-time-systems) <span class="intermediate">Intermediate</span>
77. [How do you debug Go memory leaks in distributed systems?](#q77-how-do-you-debug-go-memory-leaks-in-distributed-systems) <span class="advanced">Advanced</span>
78. [Best practices for Go code organization in high-traffic sites?](#q78-best-practices-for-go-code-organization-in-high-traffic-sites) <span class="beginner">Beginner</span>
79. [How do you implement Go error handling for embedded systems?](#q79-how-do-you-implement-go-error-handling-for-embedded-systems) <span class="intermediate">Intermediate</span>
80. [How do you test Go functionality in production environments?](#q80-how-do-you-test-go-functionality-in-production-environments) <span class="intermediate">Intermediate</span>
81. [How do you handle Go state management in large scale applications?](#q81-how-do-you-handle-go-state-management-in-large-scale-applications) <span class="advanced">Advanced</span>
82. [How do you perform Go data validation in microservices?](#q82-how-do-you-perform-go-data-validation-in-microservices) <span class="beginner">Beginner</span>
83. [How do you automate Go deployment for mobile devices?](#q83-how-do-you-automate-go-deployment-for-mobile-devices) <span class="advanced">Advanced</span>
84. [How do you handle Go concurrency issues in legacy systems?](#q84-how-do-you-handle-go-concurrency-issues-in-legacy-systems) <span class="advanced">Advanced</span>
85. [How do you implement Go caching in cloud infrastructure?](#q85-how-do-you-implement-go-caching-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
86. [How do you manage Go configuration for real-time systems?](#q86-how-do-you-manage-go-configuration-for-real-time-systems) <span class="beginner">Beginner</span>
87. [How do you handle Go internationalization (i18n) in distributed systems?](#q87-how-do-you-handle-go-internationalization-i18n-in-distributed-systems) <span class="intermediate">Intermediate</span>
88. [How do you ensure Go accessibility (a11y) in high-traffic sites?](#q88-how-do-you-ensure-go-accessibility-a11y-in-high-traffic-sites) <span class="beginner">Beginner</span>
89. [How do you optimize Go network requests in embedded systems?](#q89-how-do-you-optimize-go-network-requests-in-embedded-systems) <span class="advanced">Advanced</span>
90. [How do you handle Go performance optimization for production environments?](#q90-how-do-you-handle-go-performance-optimization-for-production-environments) <span class="advanced">Advanced</span>
91. [What are the security implications of Go in large scale applications?](#q91-what-are-the-security-implications-of-go-in-large-scale-applications) <span class="intermediate">Intermediate</span>
92. [How do you debug Go memory leaks in microservices?](#q92-how-do-you-debug-go-memory-leaks-in-microservices) <span class="advanced">Advanced</span>
93. [Best practices for Go code organization in mobile devices?](#q93-best-practices-for-go-code-organization-in-mobile-devices) <span class="beginner">Beginner</span>
94. [How do you implement Go error handling for legacy systems?](#q94-how-do-you-implement-go-error-handling-for-legacy-systems) <span class="intermediate">Intermediate</span>
95. [How do you test Go functionality in cloud infrastructure?](#q95-how-do-you-test-go-functionality-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
96. [How do you handle Go state management in real-time systems?](#q96-how-do-you-handle-go-state-management-in-real-time-systems) <span class="advanced">Advanced</span>
97. [How do you perform Go data validation in distributed systems?](#q97-how-do-you-perform-go-data-validation-in-distributed-systems) <span class="beginner">Beginner</span>
98. [How do you automate Go deployment for high-traffic sites?](#q98-how-do-you-automate-go-deployment-for-high-traffic-sites) <span class="advanced">Advanced</span>
99. [How do you handle Go concurrency issues in embedded systems?](#q99-how-do-you-handle-go-concurrency-issues-in-embedded-systems) <span class="advanced">Advanced</span>
100. [How do you implement Go caching in production environments?](#q100-how-do-you-implement-go-caching-in-production-environments) <span class="intermediate">Intermediate</span>

---

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
### Q62: How do you debug Go memory leaks in microservices?

**Difficulty**: Advanced

**Strategy**:
Use heap snapshots and look for detached DOM nodes or uncleared listeners.

**Code Example**:
```go
// Check listeners
process.on('exit', () => cleanup());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q63: Best practices for Go code organization in mobile devices?

**Difficulty**: Beginner

**Strategy**:
Follow SOLID principles. Keep functions small and focused.

**Code Example**:
```go
// Single responsibility
function doOneThing() { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q64: How do you implement Go error handling for legacy systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```go
try {
  await GoOperation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q65: How do you test Go functionality in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```go
test('Go works', () => {
  expect(Go()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q66: How do you handle Go state management in real-time systems?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```go
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q67: How do you perform Go data validation in distributed systems?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```go
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q68: How do you automate Go deployment for high-traffic sites?

**Difficulty**: Advanced

**Strategy**:
Use CI/CD pipelines. Dockerize the application. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```go
steps:
  - run: npm test
  - run: docker build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q69: How do you handle Go concurrency issues in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use locks, queues, or atomic operations. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```go
await mutex.runExclusive(async () => {
  // critical section
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q70: How do you implement Go caching in production environments?

**Difficulty**: Intermediate

**Strategy**:
Use Redis or in-memory LRU caches. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```go
const cache = new Map();
if (cache.has(key)) return cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q71: How do you manage Go configuration for large scale applications?

**Difficulty**: Beginner

**Strategy**:
Use environment variables or config files. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```go
const config = process.env.CONFIG || 'default';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q72: How do you handle Go internationalization (i18n) in microservices?

**Difficulty**: Intermediate

**Strategy**:
Use i18n libraries. Extract strings to resource files.

**Code Example**:
```go
t('welcome_message')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q73: How do you ensure Go accessibility (a11y) in mobile devices?

**Difficulty**: Beginner

**Strategy**:
Use semantic HTML and ARIA roles. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```go
<button aria-label="Close">X</button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q74: How do you optimize Go network requests in legacy systems?

**Difficulty**: Advanced

**Strategy**:
Use batching, debouncing, or GraphQL. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```go
debounce(() => fetch(), 300);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q75: How do you handle Go performance optimization for cloud infrastructure?

**Difficulty**: Advanced

**Strategy**:
Profile first, then optimize hot paths. Use caching and efficient algorithms.

**Code Example**:
```go
const start = performance.now();
// Go logic
const end = performance.now();
console.log('Time:', end - start);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q76: What are the security implications of Go in real-time systems?

**Difficulty**: Intermediate

**Strategy**:
Validate all inputs. Sanitize data. Use least privilege principle.

**Code Example**:
```go
// Sanitize input
const clean = input.replace(/<script>/g, '');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q77: How do you debug Go memory leaks in distributed systems?

**Difficulty**: Advanced

**Strategy**:
Use heap snapshots and look for detached DOM nodes or uncleared listeners.

**Code Example**:
```go
// Check listeners
process.on('exit', () => cleanup());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q78: Best practices for Go code organization in high-traffic sites?

**Difficulty**: Beginner

**Strategy**:
Follow SOLID principles. Keep functions small and focused.

**Code Example**:
```go
// Single responsibility
function doOneThing() { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q79: How do you implement Go error handling for embedded systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```go
try {
  await GoOperation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q80: How do you test Go functionality in production environments?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```go
test('Go works', () => {
  expect(Go()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q81: How do you handle Go state management in large scale applications?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```go
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q82: How do you perform Go data validation in microservices?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```go
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q83: How do you automate Go deployment for mobile devices?

**Difficulty**: Advanced

**Strategy**:
Use CI/CD pipelines. Dockerize the application. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```go
steps:
  - run: npm test
  - run: docker build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q84: How do you handle Go concurrency issues in legacy systems?

**Difficulty**: Advanced

**Strategy**:
Use locks, queues, or atomic operations. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```go
await mutex.runExclusive(async () => {
  // critical section
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q85: How do you implement Go caching in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Use Redis or in-memory LRU caches. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```go
const cache = new Map();
if (cache.has(key)) return cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q86: How do you manage Go configuration for real-time systems?

**Difficulty**: Beginner

**Strategy**:
Use environment variables or config files. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```go
const config = process.env.CONFIG || 'default';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q87: How do you handle Go internationalization (i18n) in distributed systems?

**Difficulty**: Intermediate

**Strategy**:
Use i18n libraries. Extract strings to resource files.

**Code Example**:
```go
t('welcome_message')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q88: How do you ensure Go accessibility (a11y) in high-traffic sites?

**Difficulty**: Beginner

**Strategy**:
Use semantic HTML and ARIA roles. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```go
<button aria-label="Close">X</button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q89: How do you optimize Go network requests in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use batching, debouncing, or GraphQL. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```go
debounce(() => fetch(), 300);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q90: How do you handle Go performance optimization for production environments?

**Difficulty**: Advanced

**Strategy**:
Profile first, then optimize hot paths. Use caching and efficient algorithms.

**Code Example**:
```go
const start = performance.now();
// Go logic
const end = performance.now();
console.log('Time:', end - start);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q91: What are the security implications of Go in large scale applications?

**Difficulty**: Intermediate

**Strategy**:
Validate all inputs. Sanitize data. Use least privilege principle.

**Code Example**:
```go
// Sanitize input
const clean = input.replace(/<script>/g, '');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q92: How do you debug Go memory leaks in microservices?

**Difficulty**: Advanced

**Strategy**:
Use heap snapshots and look for detached DOM nodes or uncleared listeners.

**Code Example**:
```go
// Check listeners
process.on('exit', () => cleanup());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q93: Best practices for Go code organization in mobile devices?

**Difficulty**: Beginner

**Strategy**:
Follow SOLID principles. Keep functions small and focused.

**Code Example**:
```go
// Single responsibility
function doOneThing() { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q94: How do you implement Go error handling for legacy systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```go
try {
  await GoOperation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q95: How do you test Go functionality in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```go
test('Go works', () => {
  expect(Go()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q96: How do you handle Go state management in real-time systems?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```go
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q97: How do you perform Go data validation in distributed systems?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```go
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q98: How do you automate Go deployment for high-traffic sites?

**Difficulty**: Advanced

**Strategy**:
Use CI/CD pipelines. Dockerize the application. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```go
steps:
  - run: npm test
  - run: docker build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q99: How do you handle Go concurrency issues in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use locks, queues, or atomic operations. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```go
await mutex.runExclusive(async () => {
  // critical section
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q100: How do you implement Go caching in production environments?

**Difficulty**: Intermediate

**Strategy**:
Use Redis or in-memory LRU caches. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```go
const cache = new Map();
if (cache.has(key)) return cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---
