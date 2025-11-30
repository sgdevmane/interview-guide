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
9. [How do you use `sync.WaitGroup` to wait for multiple concurrent operations?](#q9-how-do-you-use-syncwaitgroup-to-wait-for-multiple-concurrent-operations) <span class="intermediate">Intermediate</span>
10. [How do you implement middleware for an HTTP handler?](#q10-how-do-you-implement-middleware-for-an-http-handler) <span class="intermediate">Intermediate</span>
11. [How do you use interfaces for dependency injection to improve testability?](#q11-how-do-you-use-interfaces-for-dependency-injection-to-improve-testability) <span class="intermediate">Intermediate</span>
12. [How do you use the `select` statement to implement a timeout?](#q12-how-do-you-use-the-select-statement-to-implement-a-timeout) <span class="intermediate">Intermediate</span>
13. [How do you use `io.Reader` and `io.Writer` to stream data efficiently?](#q13-how-do-you-use-ioreader-and-iowriter-to-stream-data-efficiently) <span class="intermediate">Intermediate</span>
14. [How do you prevent race conditions using `sync.Mutex`?](#q14-how-do-you-prevent-race-conditions-using-syncmutex) <span class="intermediate">Intermediate</span>
15. [How do you optimize memory usage with `sync.Pool`?](#q15-how-do-you-optimize-memory-usage-with-syncpool) <span class="intermediate">Intermediate</span>
16. [How do you implement a custom JSON Marshaler to hide sensitive fields?](#q16-how-do-you-implement-a-custom-json-marshaler-to-hide-sensitive-fields) <span class="intermediate">Intermediate</span>
17. [How do you use `sync.Once` to ensure a function runs exactly once?](#q17-how-do-you-use-synconce-to-ensure-a-function-runs-exactly-once) <span class="intermediate">Intermediate</span>
18. [How do you implement a rate limiter using a Token Bucket algorithm?](#q18-how-do-you-implement-a-rate-limiter-using-a-token-bucket-algorithm) <span class="intermediate">Intermediate</span>
19. [How do you correctly handle loop variables in Goroutines?](#q19-how-do-you-correctly-handle-loop-variables-in-goroutines) <span class="intermediate">Intermediate</span>
20. [How do you use `go:embed` to bundle static assets?](#q20-how-do-you-use-go:embed-to-bundle-static-assets) <span class="intermediate">Intermediate</span>
21. [How do you use `errgroup` to manage parallel tasks with error propagation?](#q21-how-do-you-use-errgroup-to-manage-parallel-tasks-with-error-propagation) <span class="intermediate">Intermediate</span>
22. [How do you implement atomic counters using `sync/atomic`?](#q22-how-do-you-implement-atomic-counters-using-syncatomic) <span class="intermediate">Intermediate</span>
23. [How do you benchmark code using `testing.B`?](#q23-how-do-you-benchmark-code-using-testingb) <span class="intermediate">Intermediate</span>
24. [How do you optimize memory layout by reordering struct fields?](#q24-how-do-you-optimize-memory-layout-by-reordering-struct-fields) <span class="expert">Expert</span>
25. [How do you use `context.WithValue` to pass request-scoped data?](#q25-how-do-you-use-contextwithvalue-to-pass-request-scoped-data) <span class="intermediate">Intermediate</span>
26. [How do you implement a simple Fan-Out/Fan-In pattern?](#q26-how-do-you-implement-a-simple-fan-outfan-in-pattern) <span class="intermediate">Intermediate</span>
27. [How do you use `defer` effectively for cleanup (and avoid common traps)?](#q27-how-do-you-use-defer-effectively-for-cleanup-and-avoid-common-traps) <span class="intermediate">Intermediate</span>
28. [How do you implement a custom HTTP RoundTripper?](#q28-how-do-you-implement-a-custom-http-roundtripper) <span class="expert">Expert</span>
29. [How do you use `reflect` to iterate over struct fields?](#q29-how-do-you-use-reflect-to-iterate-over-struct-fields) <span class="expert">Expert</span>
30. [How do you use `slices` package (Go 1.21+) for common operations?](#q30-how-do-you-use-slices-package-go-121+-for-common-operations) <span class="intermediate">Intermediate</span>

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

