<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Interview Guide Logo" width="100" height="100">
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
16. [How do you implement a custom JSON unmarshaler?](#q16-how-do-you-implement-a-custom-json-unmarshaler) <span class="intermediate">Intermediate</span>
17. [How do you use the `defer` keyword to ensure resource cleanup?](#q17-how-do-you-use-the-defer-keyword-to-ensure-resource-cleanup) <span class="intermediate">Intermediate</span>
18. [How do you handle panic and recover in a middleware?](#q18-how-do-you-handle-panic-and-recover-in-a-middleware) <span class="intermediate">Intermediate</span>
19. [How do you use `atomic` package for lock-free counters?](#q19-how-do-you-use-atomic-package-for-lock-free-counters) <span class="intermediate">Intermediate</span>
20. [How do you profile a Go application using `pprof`?](#q20-how-do-you-profile-a-go-application-using-pprof) <span class="intermediate">Intermediate</span>
21. [How do you debug a deadlock using stack traces?](#q21-how-do-you-debug-a-deadlock-using-stack-traces) <span class="intermediate">Intermediate</span>
22. [How do you use build tags to compile code for specific OS?](#q22-how-do-you-use-build-tags-to-compile-code-for-specific-os) <span class="intermediate">Intermediate</span>
23. [How do you use `go:embed` to include static assets in the binary?](#q23-how-do-you-use-goembed-to-include-static-assets-in-the-binary) <span class="intermediate">Intermediate</span>
24. [How do you implement a rate limiter using channels?](#q24-how-do-you-implement-a-rate-limiter-using-channels) <span class="intermediate">Intermediate</span>
25. [How do you use `context.WithValue` to pass request-scoped data?](#q25-how-do-you-use-contextwithvalue-to-pass-request-scoped-data) <span class="intermediate">Intermediate</span>
26. [How do you implement a custom `http.RoundTripper`?](#q26-how-do-you-implement-a-custom-httproundtripper) <span class="intermediate">Intermediate</span>
27. [How do you use the `reflect` package to inspect types at runtime?](#q27-how-do-you-use-the-reflect-package-to-inspect-types-at-runtime) <span class="intermediate">Intermediate</span>
28. [How do you use `unsafe` pointers (and when should you avoid them)?](#q28-how-do-you-use-unsafe-pointers-and-when-should-you-avoid-them) <span class="intermediate">Intermediate</span>
29. [How do you optimize string concatenation using `strings.Builder`?](#q29-how-do-you-optimize-string-concatenation-using-stringsbuilder) <span class="intermediate">Intermediate</span>
30. [How do you use `time.Ticker` for periodic tasks?](#q30-how-do-you-use-timeticker-for-periodic-tasks) <span class="intermediate">Intermediate</span>
31. [How do you implement a priority queue using `container/heap`?](#q31-how-do-you-implement-a-priority-queue-using-containerheap) <span class="intermediate">Intermediate</span>
32. [How do you use `bufio` for efficient file reading?](#q32-how-do-you-use-bufio-for-efficient-file-reading) <span class="intermediate">Intermediate</span>
33. [How do you handle signals (SIGTERM) to stop a worker pool?](#q33-how-do-you-handle-signals-sigterm-to-stop-a-worker-pool) <span class="intermediate">Intermediate</span>
34. [How do you use `errgroup` to manage a group of Goroutines?](#q34-how-do-you-use-errgroup-to-manage-a-group-of-goroutines) <span class="intermediate">Intermediate</span>
35. [How do you implement a custom `Sort` interface?](#q35-how-do-you-implement-a-custom-sort-interface) <span class="intermediate">Intermediate</span>
36. [How do you use `go work` for multi-module workspaces?](#q36-how-do-you-use-go-work-for-multi-module-workspaces) <span class="intermediate">Intermediate</span>
37. [How do you manage dependencies using `go.mod` and `go.sum`?](#q37-how-do-you-manage-dependencies-using-gomod-and-gosum) <span class="intermediate">Intermediate</span>
38. [How do you use `GOMAXPROCS` to tune concurrency?](#q38-how-do-you-use-gomaxprocs-to-tune-concurrency) <span class="intermediate">Intermediate</span>
39. [How do you use the `testing/quick` package for property-based testing?](#q39-how-do-you-use-the-testingquick-package-for-property-based-testing) <span class="intermediate">Intermediate</span>
40. [How do you implement a fan-out/fan-in concurrency pattern?](#q40-how-do-you-implement-a-fan-outfan-in-concurrency-pattern) <span class="intermediate">Intermediate</span>
41. [How do you use `httptest` to test HTTP handlers?](#q41-how-do-you-use-httptest-to-test-http-handlers) <span class="intermediate">Intermediate</span>
42. [How do you use `sqlmock` to test database interactions?](#q42-how-do-you-use-sqlmock-to-test-database-interactions) <span class="intermediate">Intermediate</span>
43. [How do you use `gomock` for interface mocking?](#q43-how-do-you-use-gomock-for-interface-mocking) <span class="intermediate">Intermediate</span>
44. [How do you optimize struct padding for memory alignment?](#q44-how-do-you-optimize-struct-padding-for-memory-alignment) <span class="intermediate">Intermediate</span>
45. [How do you use `singleflight` to prevent cache stampedes?](#q45-how-do-you-use-singleflight-to-prevent-cache-stampedes) <span class="intermediate">Intermediate</span>
46. [How do you use `runtime/trace` to analyze latency?](#q46-how-do-you-use-runtimetrace-to-analyze-latency) <span class="intermediate">Intermediate</span>
47. [How do you implement a simple circuit breaker pattern?](#q47-how-do-you-implement-a-simple-circuit-breaker-pattern) <span class="intermediate">Intermediate</span>
48. [How do you use `encoding/gob` for binary serialization?](#q48-how-do-you-use-encodinggob-for-binary-serialization) <span class="intermediate">Intermediate</span>
49. [How do you use `net/url` to parse and modify URLs?](#q49-how-do-you-use-neturl-to-parse-and-modify-urls) <span class="intermediate">Intermediate</span>
50. [How do you use `filepath.Walk` (or `WalkDir`) to traverse directories?](#q50-how-do-you-use-filepathwalk-or-walkdir-to-traverse-directories) <span class="intermediate">Intermediate</span>
51. [How do you use `os/exec` to run external commands?](#q51-how-do-you-use-osexec-to-run-external-commands) <span class="intermediate">Intermediate</span>
52. [How do you use `plugin` package to load code dynamically?](#q52-how-do-you-use-plugin-package-to-load-code-dynamically) <span class="intermediate">Intermediate</span>
53. [How do you use `syscall` to interact with low-level OS features?](#q53-how-do-you-use-syscall-to-interact-with-low-level-os-features) <span class="intermediate">Intermediate</span>
54. [How do you use `image` package to process images?](#q54-how-do-you-use-image-package-to-process-images) <span class="intermediate">Intermediate</span>
55. [How do you use `compress/gzip` to handle compressed data?](#q55-how-do-you-use-compressgzip-to-handle-compressed-data) <span class="intermediate">Intermediate</span>
56. [How do you use `crypto/rand` for secure random number generation?](#q56-how-do-you-use-cryptorand-for-secure-random-number-generation) <span class="intermediate">Intermediate</span>
57. [How do you use `crypto/tls` to configure HTTPS clients?](#q57-how-do-you-use-cryptotls-to-configure-https-clients) <span class="intermediate">Intermediate</span>
58. [How do you use `html/template` to render secure HTML?](#q58-how-do-you-use-htmltemplate-to-render-secure-html) <span class="intermediate">Intermediate</span>
59. [How do you use `text/template` for code generation?](#q59-how-do-you-use-texttemplate-for-code-generation) <span class="intermediate">Intermediate</span>
60. [How do you use `expvar` to expose internal metrics?](#q60-how-do-you-use-expvar-to-expose-internal-metrics) <span class="intermediate">Intermediate</span>
61. [How do you use `net/http/pprof` for live profiling?](#q61-how-do-you-use-nethttppprof-for-live-profiling) <span class="intermediate">Intermediate</span>
62. [How do you use `runtime.GC()` manually (and why is it rarely needed)?](#q62-how-do-you-use-runtimegc-manually-and-why-is-it-rarely-needed) <span class="intermediate">Intermediate</span>
63. [How do you use `runtime.Goexit()` to kill a Goroutine?](#q63-how-do-you-use-runtimegoexit-to-kill-a-goroutine) <span class="intermediate">Intermediate</span>
64. [How do you use `runtime.NumGoroutine()` for monitoring?](#q64-how-do-you-use-runtimenumgoroutine-for-monitoring) <span class="intermediate">Intermediate</span>
65. [How do you use `debug.Stack()` to print the current stack?](#q65-how-do-you-use-debugstack-to-print-the-current-stack) <span class="intermediate">Intermediate</span>
66. [How do you use `debug.BuildInfo()` to get version information?](#q66-how-do-you-use-debugbuildinfo-to-get-version-information) <span class="intermediate">Intermediate</span>
67. [How do you use `runtime/metrics` to read GC stats?](#q67-how-do-you-use-runtimemetrics-to-read-gc-stats) <span class="intermediate">Intermediate</span>
68. [How do you use `sync.Cond` for broadcasting signals?](#q68-how-do-you-use-synccond-for-broadcasting-signals) <span class="intermediate">Intermediate</span>
69. [How do you use `sync.Map` for concurrent map access?](#q69-how-do-you-use-syncmap-for-concurrent-map-access) <span class="intermediate">Intermediate</span>
70. [How do you use `sync.RWMutex` for read-heavy workloads?](#q70-how-do-you-use-syncrwmutex-for-read-heavy-workloads) <span class="intermediate">Intermediate</span>
71. [How do you use `atomic.Value` to store arbitrary types atomically?](#q71-how-do-you-use-atomicvalue-to-store-arbitrary-types-atomically) <span class="intermediate">Intermediate</span>
72. [How do you use `math/big` for high-precision arithmetic?](#q72-how-do-you-use-mathbig-for-high-precision-arithmetic) <span class="intermediate">Intermediate</span>
73. [How do you use `sort.Search` for binary search?](#q73-how-do-you-use-sortsearch-for-binary-search) <span class="intermediate">Intermediate</span>
74. [How do you use `index/suffixarray` for substring search?](#q74-how-do-you-use-indexsuffixarray-for-substring-search) <span class="intermediate">Intermediate</span>
75. [How do you use `archive/zip` to create zip files?](#q75-how-do-you-use-archivezip-to-create-zip-files) <span class="intermediate">Intermediate</span>
76. [How do you use `archive/tar` to create tar archives?](#q76-how-do-you-use-archivetar-to-create-tar-archives) <span class="intermediate">Intermediate</span>
77. [How do you use `encoding/csv` to parse CSV files?](#q77-how-do-you-use-encodingcsv-to-parse-csv-files) <span class="intermediate">Intermediate</span>
78. [How do you use `encoding/xml` to parse XML?](#q78-how-do-you-use-encodingxml-to-parse-xml) <span class="intermediate">Intermediate</span>
79. [How do you use `encoding/base64` for data encoding?](#q79-how-do-you-use-encodingbase64-for-data-encoding) <span class="intermediate">Intermediate</span>
80. [How do you use `encoding/hex` for hex encoding?](#q80-how-do-you-use-encodinghex-for-hex-encoding) <span class="intermediate">Intermediate</span>
81. [How do you use `mime/multipart` for file uploads?](#q81-how-do-you-use-mimemultipart-for-file-uploads) <span class="intermediate">Intermediate</span>
82. [How do you use `net/mail` to parse email addresses?](#q82-how-do-you-use-netmail-to-parse-email-addresses) <span class="intermediate">Intermediate</span>
83. [How do you use `net/smtp` to send emails?](#q83-how-do-you-use-netsmtp-to-send-emails) <span class="intermediate">Intermediate</span>
84. [How do you use `net` package for raw TCP/UDP sockets?](#q84-how-do-you-use-net-package-for-raw-tcpudp-sockets) <span class="intermediate">Intermediate</span>
85. [How do you use `path/filepath` for cross-platform paths?](#q85-how-do-you-use-pathfilepath-for-cross-platform-paths) <span class="intermediate">Intermediate</span>
86. [How do you use `regexp` for pattern matching?](#q86-how-do-you-use-regexp-for-pattern-matching) <span class="intermediate">Intermediate</span>
87. [How do you use `strconv` for efficient string conversions?](#q87-how-do-you-use-strconv-for-efficient-string-conversions) <span class="intermediate">Intermediate</span>
88. [How do you use `unicode` package for character properties?](#q88-how-do-you-use-unicode-package-for-character-properties) <span class="intermediate">Intermediate</span>
89. [How do you use `fmt.Scanner` interface for custom scanning?](#q89-how-do-you-use-fmtscanner-interface-for-custom-scanning) <span class="intermediate">Intermediate</span>
90. [How do you use `fmt.Formatter` interface for custom printing?](#q90-how-do-you-use-fmtformatter-interface-for-custom-printing) <span class="intermediate">Intermediate</span>
91. [How do you use `flag.Value` interface for custom flags?](#q91-how-do-you-use-flagvalue-interface-for-custom-flags) <span class="intermediate">Intermediate</span>
92. [How do you use `log/slog` for structured logging (Go 1.21+)?](#q92-how-do-you-use-logslog-for-structured-logging-go-121) <span class="intermediate">Intermediate</span>
93. [How do you use `cmp` package for comparing structs in tests?](#q93-how-do-you-use-cmp-package-for-comparing-structs-in-tests) <span class="intermediate">Intermediate</span>
94. [How do you use `fstest` for testing filesystem operations?](#q94-how-do-you-use-fstest-for-testing-filesystem-operations) <span class="intermediate">Intermediate</span>
95. [How do you use `testing.B` for benchmarking?](#q95-how-do-you-use-testingb-for-benchmarking) <span class="intermediate">Intermediate</span>
96. [How do you use `testing.F` for fuzzing (Go 1.18+)?](#q96-how-do-you-use-testingf-for-fuzzing-go-118) <span class="intermediate">Intermediate</span>
97. [How do you use `go doc` to view documentation?](#q97-how-do-you-use-go-doc-to-view-documentation) <span class="intermediate">Intermediate</span>
98. [How do you use `go vet` to find common errors?](#q98-how-do-you-use-go-vet-to-find-common-errors) <span class="intermediate">Intermediate</span>
99. [How do you use `go fmt` to format code?](#q99-how-do-you-use-go-fmt-to-format-code) <span class="intermediate">Intermediate</span>
100. [How do you use `go mod tidy` to clean up dependencies?](#q100-how-do-you-use-go-mod-tidy-to-clean-up-dependencies) <span class="intermediate">Intermediate</span>
101. [How do you use `go list` to inspect module details?](#q101-how-do-you-use-go-list-to-inspect-module-details) <span class="intermediate">Intermediate</span>
102. [How do you use `go clean` to remove build artifacts?](#q102-how-do-you-use-go-clean-to-remove-build-artifacts) <span class="intermediate">Intermediate</span>
103. [How do you use `go install` to install binaries?](#q103-how-do-you-use-go-install-to-install-binaries) <span class="intermediate">Intermediate</span>
104. [How do you use `go get` to update dependencies?](#q104-how-do-you-use-go-get-to-update-dependencies) <span class="intermediate">Intermediate</span>
105. [How do you use `go test -race` to detect race conditions?](#q105-how-do-you-use-go-test--race-to-detect-race-conditions) <span class="intermediate">Intermediate</span>
106. [How do you use `go test -cover` to check code coverage?](#q106-how-do-you-use-go-test--cover-to-check-code-coverage) <span class="intermediate">Intermediate</span>

---

### Q1: How do you manage Goroutine lifecycles to prevent memory leaks?

To prevent memory leaks with Goroutines, you must ensure they have a defined exit condition. This is typically achieved using `context.Context` for cancellation or a `done` channel.

**Key Strategy:**
1. Pass a `context` or a signal channel to the Goroutine.
2. Use a `select` statement to listen for the cancellation signal.
3. Clean up resources before returning.

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

A Worker Pool limits the number of concurrent tasks to prevent resource exhaustion. It uses a buffered channel to queue jobs and a fixed number of Goroutines to process them.

**Key Strategy:**
1. Create a `jobs` channel and a `results` channel.
2. Start a fixed number of worker Goroutines.
3. Send jobs to the `jobs` channel.
4. Close the `jobs` channel when all jobs are sent.
5. Collect results.

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

In Go, errors are values. Custom error types allow adding context, and `fmt.Errorf` with `%w` allows wrapping errors to preserve the original cause for `errors.Is` and `errors.As` checks.

**Key Strategy:**
1. Define a struct that implements the `error` interface.
2. Use `fmt.Errorf("context: %w", err)` to wrap lower-level errors.
3. Use `errors.Is` to check for specific sentinels and `errors.As` to extract custom types.

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

The `sync.Once` primitive ensures that a piece of code is executed only once, making it perfect for initializing Singletons lazily and safely in a concurrent environment.

**Key Strategy:**
1. Declare a global variable for the instance.
2. Declare a `sync.Once` variable.
3. In the accessor function, use `once.Do(func() { ... })` to initialize the instance.

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

The Functional Options pattern provides a clean, extensible API for configuring structs with many optional parameters, avoiding massive constructors or nil checks.

**Key Strategy:**
1. Define an `Option` function type.
2. Create functions that return this `Option` type, modifying the struct.
3. Create a constructor that accepts a variadic slice of `Option`.

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

Graceful shutdown ensures that the server stops accepting new requests but finishes processing active requests before exiting. This is crucial for data integrity and user experience.

**Key Strategy:**
1. Start the server in a separate Goroutine.
2. Listen for OS signals (`SIGINT`, `SIGTERM`) using `signal.Notify`.
3. Call `server.Shutdown(ctx)` when a signal is received.

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

Table-driven tests allow you to define test cases as data (structs) and iterate over them, making it easy to add new scenarios and keeping the test logic DRY (Don't Repeat Yourself).

**Key Strategy:**
1. Define a struct containing `name`, `input`, and `expected` fields.
2. Create a slice of these structs with various test cases.
3. Iterate over the slice using `t.Run` to execute subtests.

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

Go Generics (introduced in Go 1.18) allow you to write data structures that work with any type that satisfies a constraint (e.g., `comparable`).

**Key Strategy:**
1. Define a generic struct `Set[T comparable]`.
2. Use a `map[T]struct{}` for underlying storage (efficient O(1) lookups).
3. Implement methods like `Add`, `Remove`, and `Contains`.

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

`sync.WaitGroup` is used to wait for a collection of Goroutines to finish execution. It maintains a counter that is incremented when a Goroutine starts and decremented when it finishes.

**Key Strategy:**
1. Call `wg.Add(1)` before starting a Goroutine.
2. Pass the `wg` pointer to the Goroutine (or capture via closure).
3. Call `wg.Done()` inside the Goroutine (usually deferred).
4. Call `wg.Wait()` in the main thread to block until the counter is zero.

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

Middleware allows you to wrap an `http.Handler` to execute logic before or after the main handler, such as logging, authentication, or panic recovery.

**Key Strategy:**
1. Create a function that takes `http.Handler` and returns `http.Handler`.
2. Inside the returned handler, perform pre-processing.
3. Call `next.ServeHTTP(w, r)` to pass control.
4. Perform post-processing if needed.

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

Dependency Injection (DI) via interfaces allows you to decouple components and swap real implementations with mocks during testing.

**Key Strategy:**
1. Define an interface for the dependency (e.g., `DataStore`).
2. Have the consumer struct accept the interface, not the concrete type.
3. In production, pass the real implementation; in tests, pass a mock.

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

The `select` statement lets a Goroutine wait on multiple communication operations. By including a case for `time.After`, you can enforce a timeout on channel operations.

**Key Strategy:**
1. Define a `select` block.
2. Add a case for the expected channel operation (receive or send).
3. Add a case for `<-time.After(duration)` to handle the timeout.

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

Go's `io` interfaces allow you to stream data without loading it all into memory. `io.Copy` is a powerful utility that connects a reader to a writer efficiently.

**Key Strategy:**
1. Use `os.Open` to get a file (Reader).
2. Use `os.Create` or `http.ResponseWriter` as the destination (Writer).
3. Use `io.Copy(dst, src)` to transfer data in chunks.

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

Race conditions occur when multiple Goroutines access shared memory concurrently without synchronization. `sync.Mutex` provides a locking mechanism to ensure exclusive access.

**Key Strategy:**
1. Embed or include `sync.Mutex` in the struct holding the shared data.
2. Call `mu.Lock()` before accessing the data.
3. Call `mu.Unlock()` (usually deferred) after accessing.

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

`sync.Pool` caches allocated but unused objects for later reuse, reducing the pressure on the Garbage Collector (GC). It is ideal for frequently allocated, short-lived objects like buffers.

**Key Strategy:**
1. Initialize `sync.Pool` with a `New` function.
2. Use `pool.Get()` to retrieve an object (type assert it).
3. Reset the object state.
4. Use `pool.Put()` to return the object to the pool.

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

### Q16: How do you implement a custom JSON unmarshaler?

This is a placeholder answer for practical question #16. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q17: How do you use the `defer` keyword to ensure resource cleanup?

This is a placeholder answer for practical question #17. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q18: How do you handle panic and recover in a middleware?

This is a placeholder answer for practical question #18. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q19: How do you use `atomic` package for lock-free counters?

This is a placeholder answer for practical question #19. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q20: How do you profile a Go application using `pprof`?

This is a placeholder answer for practical question #20. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q21: How do you debug a deadlock using stack traces?

This is a placeholder answer for practical question #21. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q22: How do you use build tags to compile code for specific OS?

This is a placeholder answer for practical question #22. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q23: How do you use `go:embed` to include static assets in the binary?

This is a placeholder answer for practical question #23. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q24: How do you implement a rate limiter using channels?

This is a placeholder answer for practical question #24. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q25: How do you use `context.WithValue` to pass request-scoped data?

This is a placeholder answer for practical question #25. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q26: How do you implement a custom `http.RoundTripper`?

This is a placeholder answer for practical question #26. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q27: How do you use the `reflect` package to inspect types at runtime?

This is a placeholder answer for practical question #27. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q28: How do you use `unsafe` pointers (and when should you avoid them)?

This is a placeholder answer for practical question #28. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q29: How do you optimize string concatenation using `strings.Builder`?

This is a placeholder answer for practical question #29. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q30: How do you use `time.Ticker` for periodic tasks?

This is a placeholder answer for practical question #30. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q31: How do you implement a priority queue using `container/heap`?

This is a placeholder answer for practical question #31. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q32: How do you use `bufio` for efficient file reading?

This is a placeholder answer for practical question #32. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q33: How do you handle signals (SIGTERM) to stop a worker pool?

This is a placeholder answer for practical question #33. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q34: How do you use `errgroup` to manage a group of Goroutines?

This is a placeholder answer for practical question #34. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q35: How do you implement a custom `Sort` interface?

This is a placeholder answer for practical question #35. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q36: How do you use `go work` for multi-module workspaces?

This is a placeholder answer for practical question #36. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q37: How do you manage dependencies using `go.mod` and `go.sum`?

This is a placeholder answer for practical question #37. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q38: How do you use `GOMAXPROCS` to tune concurrency?

This is a placeholder answer for practical question #38. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q39: How do you use the `testing/quick` package for property-based testing?

This is a placeholder answer for practical question #39. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q40: How do you implement a fan-out/fan-in concurrency pattern?

This is a placeholder answer for practical question #40. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q41: How do you use `httptest` to test HTTP handlers?

This is a placeholder answer for practical question #41. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q42: How do you use `sqlmock` to test database interactions?

This is a placeholder answer for practical question #42. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q43: How do you use `gomock` for interface mocking?

This is a placeholder answer for practical question #43. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q44: How do you optimize struct padding for memory alignment?

This is a placeholder answer for practical question #44. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q45: How do you use `singleflight` to prevent cache stampedes?

This is a placeholder answer for practical question #45. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q46: How do you use `runtime/trace` to analyze latency?

This is a placeholder answer for practical question #46. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q47: How do you implement a simple circuit breaker pattern?

This is a placeholder answer for practical question #47. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q48: How do you use `encoding/gob` for binary serialization?

This is a placeholder answer for practical question #48. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q49: How do you use `net/url` to parse and modify URLs?

This is a placeholder answer for practical question #49. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q50: How do you use `filepath.Walk` (or `WalkDir`) to traverse directories?

This is a placeholder answer for practical question #50. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q51: How do you use `os/exec` to run external commands?

This is a placeholder answer for practical question #51. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q52: How do you use `plugin` package to load code dynamically?

This is a placeholder answer for practical question #52. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q53: How do you use `syscall` to interact with low-level OS features?

This is a placeholder answer for practical question #53. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q54: How do you use `image` package to process images?

This is a placeholder answer for practical question #54. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q55: How do you use `compress/gzip` to handle compressed data?

This is a placeholder answer for practical question #55. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q56: How do you use `crypto/rand` for secure random number generation?

This is a placeholder answer for practical question #56. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q57: How do you use `crypto/tls` to configure HTTPS clients?

This is a placeholder answer for practical question #57. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q58: How do you use `html/template` to render secure HTML?

This is a placeholder answer for practical question #58. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q59: How do you use `text/template` for code generation?

This is a placeholder answer for practical question #59. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q60: How do you use `expvar` to expose internal metrics?

This is a placeholder answer for practical question #60. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q61: How do you use `net/http/pprof` for live profiling?

This is a placeholder answer for practical question #61. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q62: How do you use `runtime.GC()` manually (and why is it rarely needed)?

This is a placeholder answer for practical question #62. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q63: How do you use `runtime.Goexit()` to kill a Goroutine?

This is a placeholder answer for practical question #63. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q64: How do you use `runtime.NumGoroutine()` for monitoring?

This is a placeholder answer for practical question #64. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q65: How do you use `debug.Stack()` to print the current stack?

This is a placeholder answer for practical question #65. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q66: How do you use `debug.BuildInfo()` to get version information?

This is a placeholder answer for practical question #66. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q67: How do you use `runtime/metrics` to read GC stats?

This is a placeholder answer for practical question #67. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q68: How do you use `sync.Cond` for broadcasting signals?

This is a placeholder answer for practical question #68. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q69: How do you use `sync.Map` for concurrent map access?

This is a placeholder answer for practical question #69. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q70: How do you use `sync.RWMutex` for read-heavy workloads?

This is a placeholder answer for practical question #70. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q71: How do you use `atomic.Value` to store arbitrary types atomically?

This is a placeholder answer for practical question #71. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q72: How do you use `math/big` for high-precision arithmetic?

This is a placeholder answer for practical question #72. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q73: How do you use `sort.Search` for binary search?

This is a placeholder answer for practical question #73. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q74: How do you use `index/suffixarray` for substring search?

This is a placeholder answer for practical question #74. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q75: How do you use `archive/zip` to create zip files?

This is a placeholder answer for practical question #75. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q76: How do you use `archive/tar` to create tar archives?

This is a placeholder answer for practical question #76. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q77: How do you use `encoding/csv` to parse CSV files?

This is a placeholder answer for practical question #77. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q78: How do you use `encoding/xml` to parse XML?

This is a placeholder answer for practical question #78. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q79: How do you use `encoding/base64` for data encoding?

This is a placeholder answer for practical question #79. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q80: How do you use `encoding/hex` for hex encoding?

This is a placeholder answer for practical question #80. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q81: How do you use `mime/multipart` for file uploads?

This is a placeholder answer for practical question #81. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q82: How do you use `net/mail` to parse email addresses?

This is a placeholder answer for practical question #82. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q83: How do you use `net/smtp` to send emails?

This is a placeholder answer for practical question #83. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q84: How do you use `net` package for raw TCP/UDP sockets?

This is a placeholder answer for practical question #84. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q85: How do you use `path/filepath` for cross-platform paths?

This is a placeholder answer for practical question #85. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q86: How do you use `regexp` for pattern matching?

This is a placeholder answer for practical question #86. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q87: How do you use `strconv` for efficient string conversions?

This is a placeholder answer for practical question #87. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q88: How do you use `unicode` package for character properties?

This is a placeholder answer for practical question #88. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q89: How do you use `fmt.Scanner` interface for custom scanning?

This is a placeholder answer for practical question #89. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q90: How do you use `fmt.Formatter` interface for custom printing?

This is a placeholder answer for practical question #90. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q91: How do you use `flag.Value` interface for custom flags?

This is a placeholder answer for practical question #91. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q92: How do you use `log/slog` for structured logging (Go 1.21+)?

This is a placeholder answer for practical question #92. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q93: How do you use `cmp` package for comparing structs in tests?

This is a placeholder answer for practical question #93. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q94: How do you use `fstest` for testing filesystem operations?

This is a placeholder answer for practical question #94. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q95: How do you use `testing.B` for benchmarking?

This is a placeholder answer for practical question #95. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q96: How do you use `testing.F` for fuzzing (Go 1.18+)?

This is a placeholder answer for practical question #96. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q97: How do you use `go doc` to view documentation?

This is a placeholder answer for practical question #97. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q98: How do you use `go vet` to find common errors?

This is a placeholder answer for practical question #98. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q99: How do you use `go fmt` to format code?

This is a placeholder answer for practical question #99. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q100: How do you use `go mod tidy` to clean up dependencies?

This is a placeholder answer for practical question #100. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q101: How do you use `go list` to inspect module details?

This is a placeholder answer for practical question #101. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q102: How do you use `go clean` to remove build artifacts?

This is a placeholder answer for practical question #102. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q103: How do you use `go install` to install binaries?

This is a placeholder answer for practical question #103. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q104: How do you use `go get` to update dependencies?

This is a placeholder answer for practical question #104. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q105: How do you use `go test -race` to detect race conditions?

This is a placeholder answer for practical question #105. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q106: How do you use `go test -cover` to check code coverage?

This is a placeholder answer for practical question #106. In a real interview, you would demonstrate this by writing code or explaining the implementation steps using standard library features or common patterns.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---
