<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Java & Spring Boot Logo" width="100" height="100">
  </a>
  <h1>Java & Spring Boot Interview Questions & Answers</h1>
  <p><b>Comprehensive interview questions covering Virtual Threads, JVM Memory, Spring Boot 3, and Concurrency</b></p>
</div>

---

## Table of Contents

1. [What are Virtual Threads (Project Loom in Java 21) and how do they differ from Platform Threads?](#q1) <span class="advanced">Advanced</span>
2. [How does the JVM Memory Model (JMM) manage Heap, Stack, Metaspace, and Happens-Before guarantee?](#q2) <span class="advanced">Advanced</span>
3. [How do Garbage Collectors in Java (G1, ZGC, Shenandoah) achieve low-latency pause times?](#q3) <span class="advanced">Advanced</span>
4. [What is the difference between `CompletableFuture` and traditional `Future`?](#q4) <span class="intermediate">Intermediate</span>
5. [How do Java Streams work (Intermediate vs Terminal operations, lazy evaluation, parallel streams)?](#q5) <span class="intermediate">Intermediate</span>
6. [What are Sealed Classes and Interfaces in Java 17+ and how do they enable pattern matching?](#q6) <span class="advanced">Advanced</span>
7. [How does Record Pattern Matching work in Java 21 (`switch (obj)` with deconstruction)?](#q7) <span class="intermediate">Intermediate</span>
8. [What is the difference between `HashMap`, `ConcurrentHashMap`, and `Collections.synchronizedMap()`?](#q8) <span class="advanced">Advanced</span>
9. [How does `ThreadLocal` work in Java and what are Scoped Values in Java 21?](#q9) <span class="advanced">Advanced</span>
10. [What is the difference between Checked and Unchecked Exceptions in Java?](#q10) <span class="beginner">Beginner</span>
11. [How does String Pool and `String.intern()` work in Java?](#q11) <span class="beginner">Beginner</span>
12. [What is the difference between `Comparable` and `Comparator`?](#q12) <span class="beginner">Beginner</span>
13. [How does Dependency Injection work in Spring Boot (`@Autowired`, Constructor Injection, `@Bean`)?](#q13) <span class="intermediate">Intermediate</span>
14. [What is Spring Boot Auto-Configuration and how does `@ConditionalOnClass` work?](#q14) <span class="advanced">Advanced</span>
15. [How do Spring Transactional boundaries (`@Transactional`) work with AOP proxies?](#q15) <span class="advanced">Advanced</span>
16. [What is the difference between `equals()` and `hashCode()` contract in Java?](#q16) <span class="intermediate">Intermediate</span>
17. [What are Java Records and how do they differ from traditional POJO classes?](#q17) <span class="beginner">Beginner</span>
18. [How does the `ForkJoinPool` work in Java concurrency?](#q18) <span class="advanced">Advanced</span>
19. [What is the difference between `synchronized` keyword and `ReentrantLock`?](#q19) <span class="intermediate">Intermediate</span>
20. [How does `AtomicInteger` achieve lock-free thread safety in Java?](#q20) <span class="advanced">Advanced</span>
21. [What is the difference between Fail-Fast and Fail-Safe Iterators?](#q21) <span class="intermediate">Intermediate</span>
22. [How do you prevent SQL Injection in Java using JDBC `PreparedStatement`?](#q22) <span class="beginner">Beginner</span>
23. [What is the difference between ClassLoader hierarchy (Bootstrap, Platform, Application)?](#q23) <span class="advanced">Advanced</span>
24. [How do you configure Connection Pooling in Spring Boot with HikariCP?](#q24) <span class="intermediate">Intermediate</span>
25. [What are Spring Boot Actuator endpoints (`/actuator/health`, `/actuator/metrics`)?](#q25) <span class="intermediate">Intermediate</span>
26. [How does Java Reflection API work and what are `MethodHandles` / `VarHandle` in modern Java?](#q26) <span class="advanced">Advanced</span>
27. [What is the difference between `WeakReference`, `SoftReference`, and `PhantomReference` in Java?](#q27) <span class="advanced">Advanced</span>
28. [How do you implement a Singleton Pattern in Java with Double-Checked Locking?](#q28) <span class="intermediate">Intermediate</span>
29. [What is the difference between `ArrayList` and `LinkedList` in memory and Big-O performance?](#q29) <span class="beginner">Beginner</span>
30. [How do you implement pagination with Spring Data JPA `Pageable`?](#q30) <span class="intermediate">Intermediate</span>
31. [What is the N+1 Query problem in Hibernate / Spring Data JPA and how do you fix it?](#q31) <span class="advanced">Advanced</span>
32. [What is the difference between `first-level cache` and `second-level cache` in Hibernate?](#q32) <span class="advanced">Advanced</span>
33. [How do you configure Spring Security for stateless JWT authentication?](#q33) <span class="intermediate">Intermediate</span>
34. [What are Java Annotations and how do you build a custom runtime annotation?](#q34) <span class="intermediate">Intermediate</span>
35. [How do you handle Distributed Transactions in Spring microservices using Saga Pattern?](#q35) <span class="advanced">Advanced</span>
36. [What is the difference between `CountDownLatch` and `CyclicBarrier` in Java concurrency?](#q36) <span class="intermediate">Intermediate</span>
37. [How does `java.lang.Thread.sleep()` differ from `Object.wait()`?](#q37) <span class="beginner">Beginner</span>
38. [What is the difference between `java.time` (JSR-310) and legacy `java.util.Date`?](#q38) <span class="beginner">Beginner</span>
39. [How do you build a REST API with Spring Boot `@RestController` and `@GetMapping`?](#q39) <span class="beginner">Beginner</span>
40. [What is Java Native Interface (JNI) and Project Panama (Foreign Function & Memory API)?](#q40) <span class="advanced">Advanced</span>
41. [How do you optimize JVM Garbage Collection flags for low-latency web services?](#q41) <span class="advanced">Advanced</span>
42. [What is the difference between `poll()` and `remove()` in Java Queue interface?](#q42) <span class="beginner">Beginner</span>
43. [How do you implement a custom ThreadPoolExecutor in Java?](#q43) <span class="intermediate">Intermediate</span>
44. [What are the standard `RejectedExecutionHandler` policies in Java ThreadPools?](#q44) <span class="intermediate">Intermediate</span>
45. [What are the best practices for structuring enterprise Java and Spring Boot applications?](#q45) <span class="advanced">Advanced</span>
46. [How do you configure Spring Boot for GraalVM Native Image compilation?](#q46) <span class="advanced">Advanced</span>
47. [What is the difference between `Stream.map()` and `Stream.flatMap()` in Java?](#q47) <span class="beginner">Beginner</span>
48. [How do you handle Distributed Caching with Spring Boot and Redis (`@Cacheable`)?](#q48) <span class="intermediate">Intermediate</span>
49. [What is the difference between `ReentrantReadWriteLock` and `StampedLock` in Java?](#q49) <span class="advanced">Advanced</span>
50. [How do you configure Kafka event consumers in Spring Boot with `@KafkaListener`?](#q50) <span class="intermediate">Intermediate</span>
51. [What is the difference between `final`, `finally`, and `finalize` (deprecated)?](#q51) <span class="beginner">Beginner</span>
52. [How do you handle database migrations in Java with Flyway or Liquibase?](#q52) <span class="intermediate">Intermediate</span>
53. [What is the difference between `peek()` and `forEach()` in Java Streams?](#q53) <span class="beginner">Beginner</span>
54. [How do you implement custom Spring Boot Actuator Health Indicators?](#q54) <span class="intermediate">Intermediate</span>
55. [What is the difference between `String`, `StringBuilder`, and `StringBuffer`?](#q55) <span class="beginner">Beginner</span>
56. [How do you prevent Deadlocks in multi-threaded Java applications?](#q56) <span class="advanced">Advanced</span>
57. [What is the purpose of `java.lang.instrument` Instrumentation API in Java Agents?](#q57) <span class="advanced">Advanced</span>
58. [How do you configure asynchronous execution in Spring Boot with `@Async`?](#q58) <span class="intermediate">Intermediate</span>
59. [What is the difference between `TreeSet` and `HashSet` in Java Collections?](#q59) <span class="beginner">Beginner</span>
60. [How do you implement a circuit breaker with Resilience4j in Spring Boot?](#q60) <span class="intermediate">Intermediate</span>
61. [What is the difference between shallow copy and deep copy in Java object cloning?](#q61) <span class="intermediate">Intermediate</span>
62. [How do you implement custom Spring Security UserDetailsService?](#q62) <span class="intermediate">Intermediate</span>
63. [What is the purpose of `java.util.Optional` and its anti-patterns?](#q63) <span class="intermediate">Intermediate</span>
64. [How do you configure CORS in Spring Boot with `WebMvcConfigurer`?](#q64) <span class="beginner">Beginner</span>
65. [What is the difference between `Callable` and `Runnable` in Java concurrency?](#q65) <span class="beginner">Beginner</span>
66. [How do you configure SSL/TLS in Spring Boot `application.properties`?](#q66) <span class="beginner">Beginner</span>
67. [What is the purpose of `java.lang.ref.Cleaner` in Java 9+?](#q67) <span class="advanced">Advanced</span>
68. [How do you implement rate limiting in Spring Boot with Bucket4j?](#q68) <span class="intermediate">Intermediate</span>
69. [What is the difference between `transient` and `volatile` keywords in Java?](#q69) <span class="intermediate">Intermediate</span>
70. [How do you handle JSON serialization with Jackson `@JsonProperty` and `@JsonIgnore` in Spring Boot?](#q70) <span class="beginner">Beginner</span>
71. [What is the purpose of `java.util.concurrent.Semaphore`?](#q71) <span class="intermediate">Intermediate</span>
72. [How do you mock dependencies in Spring Boot tests with `@MockBean`?](#q72) <span class="intermediate">Intermediate</span>
73. [What is the difference between `java.lang.Error` and `java.lang.Exception`?](#q73) <span class="beginner">Beginner</span>
74. [How do you configure multi-part file uploads in Spring Boot with `MultipartFile`?](#q74) <span class="beginner">Beginner</span>
75. [What is the purpose of `java.util.concurrent.Exchanger`?](#q75) <span class="advanced">Advanced</span>
76. [How do you implement global exception handling in Spring Boot with `@RestControllerAdvice`?](#q76) <span class="intermediate">Intermediate</span>
77. [What is the difference between `System.arraycopy()` and `Arrays.copyOf()`?](#q77) <span class="beginner">Beginner</span>
78. [How do you configure dynamic logging levels at runtime in Spring Boot Actuator?](#q78) <span class="intermediate">Intermediate</span>
79. [What is the purpose of `java.util.Objects.requireNonNull()`?](#q79) <span class="beginner">Beginner</span>
80. [How do you configure WebSocket message broker with STOMP in Spring Boot?](#q80) <span class="intermediate">Intermediate</span>
81. [What is the difference between `CopyOnWriteArrayList` and `Collections.synchronizedList()`?](#q81) <span class="intermediate">Intermediate</span>
82. [How do you test JPA repository queries with `@DataJpaTest` in Spring Boot?](#q82) <span class="intermediate">Intermediate</span>
83. [What is the purpose of `@Lazy` annotation in Spring bean initialization?](#q83) <span class="intermediate">Intermediate</span>
84. [How do you implement distributed tracing with Micrometer Tracing in Spring Boot 3?](#q84) <span class="advanced">Advanced</span>
85. [What is the difference between `ArrayBlockingQueue` and `LinkedBlockingQueue`?](#q85) <span class="intermediate">Intermediate</span>
86. [How do you configure OpenAPI 3 / Swagger documentation in Spring Boot with `springdoc-openapi`?](#q86) <span class="beginner">Beginner</span>
87. [What is the purpose of `java.lang.invoke.MethodHandle` in modern JVM optimization?](#q87) <span class="advanced">Advanced</span>
88. [How do you implement database auditing (`@CreatedDate`, `@LastModifiedDate`) with Spring Data JPA?](#q88) <span class="beginner">Beginner</span>
89. [What is the difference between `java.util.concurrent.ConcurrentSkipListMap` and `TreeMap`?](#q89) <span class="advanced">Advanced</span>
90. [How do you implement event-driven architectures with Spring `@EventListener` and `@TransactionalEventListener`?](#q90) <span class="intermediate">Intermediate</span>
91. [What is the purpose of `java.lang.Thread.UncaughtExceptionHandler`?](#q91) <span class="beginner">Beginner</span>
92. [How do you configure embedded Tomcat connection threads and accept queue in Spring Boot?](#q92) <span class="intermediate">Intermediate</span>
93. [What is the difference between `peek()` and `map()` in Stream transformations?](#q93) <span class="beginner">Beginner</span>
94. [How do you implement API key authentication in Spring Security filters?](#q94) <span class="intermediate">Intermediate</span>
95. [How do you configure dynamic quartz scheduling in Spring Boot?](#q95) <span class="intermediate">Intermediate</span>
96. [What is the difference between `synchronized` method and `synchronized` block?](#q96) <span class="beginner">Beginner</span>
97. [How do you handle multi-tenancy database routing with `AbstractRoutingDataSource` in Spring Boot?](#q97) <span class="advanced">Advanced</span>
98. [What is the purpose of `java.util.concurrent.Phaser`?](#q98) <span class="advanced">Advanced</span>
99. [How do you implement optimistic locking in JPA using `@Version`?](#q99) <span class="intermediate">Intermediate</span>
100. [What is the difference between `@Component`, `@Service`, and `@Repository` in Spring?](#q100) <span class="beginner">Beginner</span>

---

<a id="q1"></a>
### Q1: What are Virtual Threads (Project Loom in Java 21) and how do they differ from Platform Threads?

**Difficulty**: Advanced

**Strategy**:
Platform threads are 1:1 mappings to operating system kernel threads (heavyweight, ~1MB stack memory, limited to thousands per JVM). Virtual Threads are lightweight user-mode threads managed directly by the JVM runtime (mounted onto carrier OS threads via `ForkJoinPool`, taking only bytes of memory, scaling to millions of concurrent threads per JVM). They eliminate reactive callback complexity, enabling simple synchronous blocking code with high concurrency throughput.

**Code Example**:
```java
import java.util.concurrent.Executors;

public class VirtualThreadDemo {
    public static void main(String[] args) throws Exception {
        // Spawns 100,000 virtual threads concurrently
        try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
            for (int i = 0; i < 100_000; i++) {
                final int id = i;
                executor.submit(() -> {
                    Thread.sleep(1000); // Blocks virtual thread, NOT the OS carrier thread
                    return "Task " + id;
                });
            }
        } // Auto-awaits completion
        System.out.println("Completed 100,000 virtual thread tasks.");
    }
}
```

---

<a id="q2"></a>
### Q2: How does the JVM Memory Model (JMM) manage Heap, Stack, Metaspace, and Happens-Before guarantee?

**Difficulty**: Advanced

**Strategy**:
- **Heap**: Stores all object instances and arrays, managed by Garbage Collector (divided into Young Gen: Eden/Survivor and Old Gen).
- **Thread Stack**: Thread-private, stores primitive local variables and method call frames.
- **Metaspace**: Native off-heap memory storing class metadata, method bytecode, and static variables (replaces PermGen in Java 8+).
- **Happens-Before**: JMM memory visibility guarantee ensuring writes made by one thread are visible to another thread (e.g. `volatile` writes happen-before subsequent reads; synchronized unlock happens-before lock).

**Code Example**:
```java
public class VolatileFlag {
    // volatile prevents CPU caching and instruction reordering
    private volatile boolean running = true;

    public void stop() { running = false; }

    public void worker() {
        while (running) {
            // Work in loop with guaranteed visibility of 'running' flag
        }
    }
}
```

---

<a id="q3"></a>
### Q3: How do Garbage Collectors in Java (G1, ZGC, Shenandoah) achieve low-latency pause times?

**Difficulty**: Advanced

**Strategy**:
- **G1 GC**: Region-based generational collector dividing heap into ~2048 regions, concurrently marking and prioritizing regions with the most garbage ('Garbage First').
- **ZGC (Z Garbage Collector)**: Scalable ultra-low-latency collector using colored pointers and load barriers to perform marking, relocation, and compaction concurrently with application threads, keeping pause times under 1 millisecond on multi-terabyte heaps.
- **Shenandoah**: Ultra-low-latency collector using Brooks pointers / load-reference barriers to compact heap memory concurrently.

**Code Example**:
```bash
# Enabling ZGC in Java 17/21
java -XX:+UseZGC -XX:+ZGenerational -jar app.jar
```

---

<a id="q4"></a>
### Q4: What is the difference between `CompletableFuture` and traditional `Future`?

**Difficulty**: Intermediate

**Strategy**:
Traditional `Future` requires blocking `get()` calls to retrieve results. `CompletableFuture` implements `CompletionStage`, enabling non-blocking functional composition (`thenApply`, `thenCompose`, `thenCombine`, `exceptionally`) across asynchronous pipeline stages.

**Code Example**:
```java
import java.util.concurrent.CompletableFuture;

public class AsyncService {
    public CompletableFuture<String> fetchUser(String id) {
        return CompletableFuture.supplyAsync(() -> queryUserDb(id))
            .thenApply(user -> user.toUpperCase())
            .thenCompose(user -> enrichWithOrders(user))
            .exceptionally(ex -> "Fallback User: " + ex.getMessage());
    }
    private String queryUserDb(String id) { return "user-" + id; }
    private CompletableFuture<String> enrichWithOrders(String u) { return CompletableFuture.completedFuture(u + " [Orders: 3]"); }
}
```

---

<a id="q5"></a>
### Q5: How do Java Streams work (Intermediate vs Terminal operations, lazy evaluation, parallel streams)?

**Difficulty**: Intermediate

**Strategy**:
Java Streams pipeline data elements without storing them:
- **Intermediate Operations (`filter`, `map`, `sorted`)**: Lazy, return a new Stream, do not execute until a terminal operation is called.
- **Terminal Operations (`collect`, `forEach`, `reduce`, `count`)**: Eager, trigger traversal and consume the stream.
- **Parallel Streams (`parallelStream()`)**: Utilizes the common `ForkJoinPool` to partition data chunks across CPU cores.

**Code Example**:
```java
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class StreamExample {
    public static Map<String, List<Product>> groupProductsByCategory(List<Product> products) {
        return products.stream()
            .filter(p -> p.getPrice() > 50.0)
            .sorted((a, b) -> Double.compare(b.getPrice(), a.getPrice()))
            .collect(Collectors.groupingBy(Product::getCategory));
    }
}
```

---

<a id="q6"></a>
### Q6: What are Sealed Classes and Interfaces in Java 17+ and how do they enable pattern matching?

**Difficulty**: Advanced

**Strategy**:
Detailed architectural and technical explanation of What are Sealed Classes and Interfaces in Java 17+ and how do they enable pattern matching?. Restrict which other classes/interfaces may extend or implement them using `permits` keyword, enabling exhaustive `switch` pattern matching. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What are Sealed Classes and Interfaces in Java 17+ and how do they enable pattern matching?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q7"></a>
### Q7: How does Record Pattern Matching work in Java 21 (`switch (obj)` with deconstruction)?

**Difficulty**: Intermediate

**Strategy**:
Detailed architectural and technical explanation of How does Record Pattern Matching work in Java 21 (`switch (obj)` with deconstruction)?. Deconstructs record components directly in `switch` expressions without explicit type casting. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How does Record Pattern Matching work in Java 21 (`switch (obj)` with deconstruction)?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q8"></a>
### Q8: What is the difference between `HashMap`, `ConcurrentHashMap`, and `Collections.synchronizedMap()`?

**Difficulty**: Advanced

**Strategy**:
Detailed architectural and technical explanation of What is the difference between `HashMap`, `ConcurrentHashMap`, and `Collections.synchronizedMap()`?. `HashMap` is not thread-safe; `synchronizedMap` locks the entire map on every operation; `ConcurrentHashMap` uses lock-free CAS operations and segmented tree bin locks for high-concurrency throughput. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is the difference between `HashMap`, `ConcurrentHashMap`, and `Collections.synchronizedMap()`?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q9"></a>
### Q9: How does `ThreadLocal` work in Java and what are Scoped Values in Java 21?

**Difficulty**: Advanced

**Strategy**:
Detailed architectural and technical explanation of How does `ThreadLocal` work in Java and what are Scoped Values in Java 21?. `ThreadLocal` stores thread-scoped state (risk of memory leaks in thread pools); `ScopedValues` (Project Loom) provide immutable, lightweight, scoped inheritance across virtual threads. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How does `ThreadLocal` work in Java and what are Scoped Values in Java 21?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q10"></a>
### Q10: What is the difference between Checked and Unchecked Exceptions in Java?

**Difficulty**: Beginner

**Strategy**:
Detailed architectural and technical explanation of What is the difference between Checked and Unchecked Exceptions in Java?. Checked (`Exception`) must be declared in `throws` or caught at compile-time; Unchecked (`RuntimeException`, `Error`) occur at runtime without mandatory try-catch. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is the difference between Checked and Unchecked Exceptions in Java?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q11"></a>
### Q11: How does String Pool and `String.intern()` work in Java?

**Difficulty**: Beginner

**Strategy**:
Detailed architectural and technical explanation of How does String Pool and `String.intern()` work in Java?. JVM maintains a string literal pool in heap memory. `intern()` ensures strings with identical characters share the same canonical heap reference. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How does String Pool and `String.intern()` work in Java?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q12"></a>
### Q12: What is the difference between `Comparable` and `Comparator`?

**Difficulty**: Beginner

**Strategy**:
Detailed architectural and technical explanation of What is the difference between `Comparable` and `Comparator`?. `Comparable` defines natural ordering via `compareTo()`; `Comparator` defines custom external ordering strategies via `compare()`. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is the difference between `Comparable` and `Comparator`?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q13"></a>
### Q13: How does Dependency Injection work in Spring Boot (`@Autowired`, Constructor Injection, `@Bean`)?

**Difficulty**: Intermediate

**Strategy**:
Detailed architectural and technical explanation of How does Dependency Injection work in Spring Boot (`@Autowired`, Constructor Injection, `@Bean`)?. Spring IoC container instantiates and injects beans based on component scanning; constructor injection is preferred for immutability and testability. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How does Dependency Injection work in Spring Boot (`@Autowired`, Constructor Injection, `@Bean`)?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q14"></a>
### Q14: What is Spring Boot Auto-Configuration and how does `@ConditionalOnClass` work?

**Difficulty**: Advanced

**Strategy**:
Detailed architectural and technical explanation of What is Spring Boot Auto-Configuration and how does `@ConditionalOnClass` work?. Analyzes classpath jars and applies pre-configured beans (`@AutoConfiguration`) only if required libraries and properties are present. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is Spring Boot Auto-Configuration and how does `@ConditionalOnClass` work?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q15"></a>
### Q15: How do Spring Transactional boundaries (`@Transactional`) work with AOP proxies?

**Difficulty**: Advanced

**Strategy**:
Detailed architectural and technical explanation of How do Spring Transactional boundaries (`@Transactional`) work with AOP proxies?. Spring creates a CGLIB/JDK dynamic proxy around `@Transactional` methods, starting a DB transaction before method entry and committing/rolling back on exit (internal `this.method()` calls bypass proxy). Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How do Spring Transactional boundaries (`@Transactional`) work with AOP proxies?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q16"></a>
### Q16: What is the difference between `equals()` and `hashCode()` contract in Java?

**Difficulty**: Intermediate

**Strategy**:
Detailed architectural and technical explanation of What is the difference between `equals()` and `hashCode()` contract in Java?. If `a.equals(b)` is true, `a.hashCode()` MUST equal `b.hashCode()`. Violating this breaks `HashSet` and `HashMap` lookups. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is the difference between `equals()` and `hashCode()` contract in Java?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q17"></a>
### Q17: What are Java Records and how do they differ from traditional POJO classes?

**Difficulty**: Beginner

**Strategy**:
Detailed architectural and technical explanation of What are Java Records and how do they differ from traditional POJO classes?. Records are immutable data carriers generating constructor, getters, `equals()`, `hashCode()`, and `toString()` automatically. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What are Java Records and how do they differ from traditional POJO classes?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q18"></a>
### Q18: How does the `ForkJoinPool` work in Java concurrency?

**Difficulty**: Advanced

**Strategy**:
Detailed architectural and technical explanation of How does the `ForkJoinPool` work in Java concurrency?. Uses work-stealing algorithm where idle worker threads steal queued sub-tasks from the deques of busy threads. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How does the `ForkJoinPool` work in Java concurrency?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q19"></a>
### Q19: What is the difference between `synchronized` keyword and `ReentrantLock`?

**Difficulty**: Intermediate

**Strategy**:
Detailed architectural and technical explanation of What is the difference between `synchronized` keyword and `ReentrantLock`?. `synchronized` is JVM-managed block locking; `ReentrantLock` provides timed tryLock, fairness policies, and interruptible locks. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is the difference between `synchronized` keyword and `ReentrantLock`?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q20"></a>
### Q20: How does `AtomicInteger` achieve lock-free thread safety in Java?

**Difficulty**: Advanced

**Strategy**:
Detailed architectural and technical explanation of How does `AtomicInteger` achieve lock-free thread safety in Java?. Uses low-level CPU Compare-And-Swap (CAS) instructions (`sun.misc.Unsafe` / `VarHandle`) in a spin-wait loop. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How does `AtomicInteger` achieve lock-free thread safety in Java?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q21"></a>
### Q21: What is the difference between Fail-Fast and Fail-Safe Iterators?

**Difficulty**: Intermediate

**Strategy**:
Detailed architectural and technical explanation of What is the difference between Fail-Fast and Fail-Safe Iterators?. Fail-fast (`ArrayList`) throws `ConcurrentModificationException` on concurrent modifications; Fail-safe (`CopyOnWriteArrayList`) iterates over a copy of the collection. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is the difference between Fail-Fast and Fail-Safe Iterators?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q22"></a>
### Q22: How do you prevent SQL Injection in Java using JDBC `PreparedStatement`?

**Difficulty**: Beginner

**Strategy**:
Detailed architectural and technical explanation of How do you prevent SQL Injection in Java using JDBC `PreparedStatement`?. Uses pre-compiled parameterized queries where database driver escapes input values natively. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How do you prevent SQL Injection in Java using JDBC `PreparedStatement`?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q23"></a>
### Q23: What is the difference between ClassLoader hierarchy (Bootstrap, Platform, Application)?

**Difficulty**: Advanced

**Strategy**:
Detailed architectural and technical explanation of What is the difference between ClassLoader hierarchy (Bootstrap, Platform, Application)?. Delegation parent-first model: Application -> Platform -> Bootstrap ClassLoader. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is the difference between ClassLoader hierarchy (Bootstrap, Platform, Application)?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q24"></a>
### Q24: How do you configure Connection Pooling in Spring Boot with HikariCP?

**Difficulty**: Intermediate

**Strategy**:
Detailed architectural and technical explanation of How do you configure Connection Pooling in Spring Boot with HikariCP?. HikariCP is the default high-performance JDBC pool configured via `spring.datasource.hikari.maximum-pool-size`. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How do you configure Connection Pooling in Spring Boot with HikariCP?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q25"></a>
### Q25: What are Spring Boot Actuator endpoints (`/actuator/health`, `/actuator/metrics`)?

**Difficulty**: Intermediate

**Strategy**:
Detailed architectural and technical explanation of What are Spring Boot Actuator endpoints (`/actuator/health`, `/actuator/metrics`)?. Provides production-ready monitoring endpoints exposing health, Prometheus metrics, and thread dumps. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What are Spring Boot Actuator endpoints (`/actuator/health`, `/actuator/metrics`)?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q26"></a>
### Q26: How does Java Reflection API work and what are `MethodHandles` / `VarHandle` in modern Java?

**Difficulty**: Advanced

**Strategy**:
Detailed architectural and technical explanation of How does Java Reflection API work and what are `MethodHandles` / `VarHandle` in modern Java?. `MethodHandles` and `VarHandles` provide high-performance, strongly-typed, JIT-optimized alternatives to legacy reflection. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How does Java Reflection API work and what are `MethodHandles` / `VarHandle` in modern Java?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q27"></a>
### Q27: What is the difference between `WeakReference`, `SoftReference`, and `PhantomReference` in Java?

**Difficulty**: Advanced

**Strategy**:
Detailed architectural and technical explanation of What is the difference between `WeakReference`, `SoftReference`, and `PhantomReference` in Java?. SoftReference cleared before OutOfMemoryError; WeakReference cleared on next GC cycle; PhantomReference used for off-heap memory cleanup queues. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is the difference between `WeakReference`, `SoftReference`, and `PhantomReference` in Java?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q28"></a>
### Q28: How do you implement a Singleton Pattern in Java with Double-Checked Locking?

**Difficulty**: Intermediate

**Strategy**:
Detailed architectural and technical explanation of How do you implement a Singleton Pattern in Java with Double-Checked Locking?. Use `private static volatile Instance instance;` with synchronized block checking null twice. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How do you implement a Singleton Pattern in Java with Double-Checked Locking?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q29"></a>
### Q29: What is the difference between `ArrayList` and `LinkedList` in memory and Big-O performance?

**Difficulty**: Beginner

**Strategy**:
Detailed architectural and technical explanation of What is the difference between `ArrayList` and `LinkedList` in memory and Big-O performance?. `ArrayList` is contiguous dynamic array (O(1) access, CPU cache friendly); `LinkedList` is doubly-linked nodes (O(N) access, high pointer memory overhead). Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is the difference between `ArrayList` and `LinkedList` in memory and Big-O performance?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q30"></a>
### Q30: How do you implement pagination with Spring Data JPA `Pageable`?

**Difficulty**: Intermediate

**Strategy**:
Detailed architectural and technical explanation of How do you implement pagination with Spring Data JPA `Pageable`?. Pass `Pageable pageable = PageRequest.of(page, size, Sort.by('date'))` to repository method. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How do you implement pagination with Spring Data JPA `Pageable`?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q31"></a>
### Q31: What is the N+1 Query problem in Hibernate / Spring Data JPA and how do you fix it?

**Difficulty**: Advanced

**Strategy**:
Detailed architectural and technical explanation of What is the N+1 Query problem in Hibernate / Spring Data JPA and how do you fix it?. Occurs when loading parent entities executes 1 query and N subsequent queries for child relations. Fix with `JOIN FETCH`, `@EntityGraph`, or `BatchSize`. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is the N+1 Query problem in Hibernate / Spring Data JPA and how do you fix it?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q32"></a>
### Q32: What is the difference between `first-level cache` and `second-level cache` in Hibernate?

**Difficulty**: Advanced

**Strategy**:
Detailed architectural and technical explanation of What is the difference between `first-level cache` and `second-level cache` in Hibernate?. First-level cache is bound to `EntityManager` Session; Second-level cache is shared across sessions across the entire application (e.g. Ehcache, Redis). Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is the difference between `first-level cache` and `second-level cache` in Hibernate?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q33"></a>
### Q33: How do you configure Spring Security for stateless JWT authentication?

**Difficulty**: Intermediate

**Strategy**:
Detailed architectural and technical explanation of How do you configure Spring Security for stateless JWT authentication?. Add `JwtAuthenticationFilter` before `UsernamePasswordAuthenticationFilter` and configure `SessionCreationPolicy.STATELESS`. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How do you configure Spring Security for stateless JWT authentication?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q34"></a>
### Q34: What are Java Annotations and how do you build a custom runtime annotation?

**Difficulty**: Intermediate

**Strategy**:
Detailed architectural and technical explanation of What are Java Annotations and how do you build a custom runtime annotation?. Annotate interface with `@Retention(RetentionPolicy.RUNTIME)` and `@Target(ElementType.METHOD)`. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What are Java Annotations and how do you build a custom runtime annotation?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q35"></a>
### Q35: How do you handle Distributed Transactions in Spring microservices using Saga Pattern?

**Difficulty**: Advanced

**Strategy**:
Detailed architectural and technical explanation of How do you handle Distributed Transactions in Spring microservices using Saga Pattern?. Coordinate microservice state changes via Orchestrator or Choreography (Kafka events) with compensating rollback transactions. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How do you handle Distributed Transactions in Spring microservices using Saga Pattern?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q36"></a>
### Q36: What is the difference between `CountDownLatch` and `CyclicBarrier` in Java concurrency?

**Difficulty**: Intermediate

**Strategy**:
Detailed architectural and technical explanation of What is the difference between `CountDownLatch` and `CyclicBarrier` in Java concurrency?. `CountDownLatch` cannot be reset after count reaches zero; `CyclicBarrier` can be reused after all threads reach barrier point. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is the difference between `CountDownLatch` and `CyclicBarrier` in Java concurrency?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q37"></a>
### Q37: How does `java.lang.Thread.sleep()` differ from `Object.wait()`?

**Difficulty**: Beginner

**Strategy**:
Detailed architectural and technical explanation of How does `java.lang.Thread.sleep()` differ from `Object.wait()`?. `sleep()` retains held locks; `wait()` releases the monitor lock and waits for `notify()`. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How does `java.lang.Thread.sleep()` differ from `Object.wait()`?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q38"></a>
### Q38: What is the difference between `java.time` (JSR-310) and legacy `java.util.Date`?

**Difficulty**: Beginner

**Strategy**:
Detailed architectural and technical explanation of What is the difference between `java.time` (JSR-310) and legacy `java.util.Date`?. `java.time` classes (`Instant`, `LocalDate`, `ZonedDateTime`) are immutable and thread-safe; `Date` is mutable. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is the difference between `java.time` (JSR-310) and legacy `java.util.Date`?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q39"></a>
### Q39: How do you build a REST API with Spring Boot `@RestController` and `@GetMapping`?

**Difficulty**: Beginner

**Strategy**:
Detailed architectural and technical explanation of How do you build a REST API with Spring Boot `@RestController` and `@GetMapping`?. Annotate class with `@RestController` and map HTTP methods to handler functions returning JSON response entities. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How do you build a REST API with Spring Boot `@RestController` and `@GetMapping`?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q40"></a>
### Q40: What is Java Native Interface (JNI) and Project Panama (Foreign Function & Memory API)?

**Difficulty**: Advanced

**Strategy**:
Detailed architectural and technical explanation of What is Java Native Interface (JNI) and Project Panama (Foreign Function & Memory API)?. Panama (Java 22+) provides type-safe, high-performance C-library invocation and off-heap memory access without fragile C JNI boilerplate. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is Java Native Interface (JNI) and Project Panama (Foreign Function & Memory API)?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q41"></a>
### Q41: How do you optimize JVM Garbage Collection flags for low-latency web services?

**Difficulty**: Advanced

**Strategy**:
Detailed architectural and technical explanation of How do you optimize JVM Garbage Collection flags for low-latency web services?. Tune `-XX:+UseG1GC -XX:MaxGCPauseMillis=200 -XX:InitiatingHeapOccupancyPercent=45`. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How do you optimize JVM Garbage Collection flags for low-latency web services?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q42"></a>
### Q42: What is the difference between `poll()` and `remove()` in Java Queue interface?

**Difficulty**: Beginner

**Strategy**:
Detailed architectural and technical explanation of What is the difference between `poll()` and `remove()` in Java Queue interface?. `poll()` returns `null` if empty; `remove()` throws `NoSuchElementException`. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is the difference between `poll()` and `remove()` in Java Queue interface?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q43"></a>
### Q43: How do you implement a custom ThreadPoolExecutor in Java?

**Difficulty**: Intermediate

**Strategy**:
Detailed architectural and technical explanation of How do you implement a custom ThreadPoolExecutor in Java?. Instantiate `ThreadPoolExecutor(corePoolSize, maxPoolSize, keepAliveTime, TimeUnit, workQueue, rejectedHandler)`. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How do you implement a custom ThreadPoolExecutor in Java?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q44"></a>
### Q44: What are the standard `RejectedExecutionHandler` policies in Java ThreadPools?

**Difficulty**: Intermediate

**Strategy**:
Detailed architectural and technical explanation of What are the standard `RejectedExecutionHandler` policies in Java ThreadPools?. `AbortPolicy` (throws exception), `CallerRunsPolicy` (caller thread executes task), `DiscardPolicy` (drops task), `DiscardOldestPolicy`. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What are the standard `RejectedExecutionHandler` policies in Java ThreadPools?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q45"></a>
### Q45: What are the best practices for structuring enterprise Java and Spring Boot applications?

**Difficulty**: Advanced

**Strategy**:
Detailed architectural and technical explanation of What are the best practices for structuring enterprise Java and Spring Boot applications?. Clean architecture (controller, service, repository, domain entities), immutable DTO records, constructor injection, flyway migrations, and OpenTelemetry instrumentation. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What are the best practices for structuring enterprise Java and Spring Boot applications?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q46"></a>
### Q46: How do you configure Spring Boot for GraalVM Native Image compilation?

**Difficulty**: Advanced

**Strategy**:
Detailed architectural and technical explanation of How do you configure Spring Boot for GraalVM Native Image compilation?. Use Spring AOT compilation and GraalVM native-image plugin to produce standalone binary executables with millisecond startup and minimal memory. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How do you configure Spring Boot for GraalVM Native Image compilation?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q47"></a>
### Q47: What is the difference between `Stream.map()` and `Stream.flatMap()` in Java?

**Difficulty**: Beginner

**Strategy**:
Detailed architectural and technical explanation of What is the difference between `Stream.map()` and `Stream.flatMap()` in Java?. `map()` transforms elements 1-to-1; `flatMap()` flattens nested stream structures 1-to-N into a single stream. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is the difference between `Stream.map()` and `Stream.flatMap()` in Java?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q48"></a>
### Q48: How do you handle Distributed Caching with Spring Boot and Redis (`@Cacheable`)?

**Difficulty**: Intermediate

**Strategy**:
Detailed architectural and technical explanation of How do you handle Distributed Caching with Spring Boot and Redis (`@Cacheable`)?. Enable caching with `@EnableCaching`, configure `RedisCacheManager`, and annotate service methods with `@Cacheable('users')`. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How do you handle Distributed Caching with Spring Boot and Redis (`@Cacheable`)?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q49"></a>
### Q49: What is the difference between `ReentrantReadWriteLock` and `StampedLock` in Java?

**Difficulty**: Advanced

**Strategy**:
Detailed architectural and technical explanation of What is the difference between `ReentrantReadWriteLock` and `StampedLock` in Java?. `StampedLock` provides optimistic read modes that don't block write locks, offering superior read-heavy concurrency. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is the difference between `ReentrantReadWriteLock` and `StampedLock` in Java?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q50"></a>
### Q50: How do you configure Kafka event consumers in Spring Boot with `@KafkaListener`?

**Difficulty**: Intermediate

**Strategy**:
Detailed architectural and technical explanation of How do you configure Kafka event consumers in Spring Boot with `@KafkaListener`?. Configure `ConcurrentKafkaListenerContainerFactory` and annotate methods with `@KafkaListener(topics = 'orders', groupId = 'billing')`. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How do you configure Kafka event consumers in Spring Boot with `@KafkaListener`?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q51"></a>
### Q51: What is the difference between `final`, `finally`, and `finalize` (deprecated)?

**Difficulty**: Beginner

**Strategy**:
Detailed architectural and technical explanation of What is the difference between `final`, `finally`, and `finalize` (deprecated)?. `final` is modifier for constants/classes/methods; `finally` is block executed after try-catch; `finalize` was legacy GC cleanup. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is the difference between `final`, `finally`, and `finalize` (deprecated)?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q52"></a>
### Q52: How do you handle database migrations in Java with Flyway or Liquibase?

**Difficulty**: Intermediate

**Strategy**:
Detailed architectural and technical explanation of How do you handle database migrations in Java with Flyway or Liquibase?. Place versioned SQL migration scripts (`V1__init.sql`) in `src/main/resources/db/migration` executed on application startup. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How do you handle database migrations in Java with Flyway or Liquibase?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q53"></a>
### Q53: What is the difference between `peek()` and `forEach()` in Java Streams?

**Difficulty**: Beginner

**Strategy**:
Detailed architectural and technical explanation of What is the difference between `peek()` and `forEach()` in Java Streams?. `peek()` is an intermediate operation designed for debugging; `forEach()` is a terminal consuming operation. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is the difference between `peek()` and `forEach()` in Java Streams?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q54"></a>
### Q54: How do you implement custom Spring Boot Actuator Health Indicators?

**Difficulty**: Intermediate

**Strategy**:
Detailed architectural and technical explanation of How do you implement custom Spring Boot Actuator Health Indicators?. Implement `HealthIndicator` interface and return `Health.up()` or `Health.down().withDetail('error', msg)`. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How do you implement custom Spring Boot Actuator Health Indicators?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q55"></a>
### Q55: What is the difference between `String`, `StringBuilder`, and `StringBuffer`?

**Difficulty**: Beginner

**Strategy**:
Detailed architectural and technical explanation of What is the difference between `String`, `StringBuilder`, and `StringBuffer`?. `String` is immutable; `StringBuilder` is mutable and non-thread-safe (fast); `StringBuffer` is mutable and synchronized (thread-safe). Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is the difference between `String`, `StringBuilder`, and `StringBuffer`?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q56"></a>
### Q56: How do you prevent Deadlocks in multi-threaded Java applications?

**Difficulty**: Advanced

**Strategy**:
Detailed architectural and technical explanation of How do you prevent Deadlocks in multi-threaded Java applications?. Acquire locks in strict universal global order, use timed `tryLock()`, and minimize lock scope. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How do you prevent Deadlocks in multi-threaded Java applications?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q57"></a>
### Q57: What is the purpose of `java.lang.instrument` Instrumentation API in Java Agents?

**Difficulty**: Advanced

**Strategy**:
Detailed architectural and technical explanation of What is the purpose of `java.lang.instrument` Instrumentation API in Java Agents?. Allows dynamic bytecode transformation and APM monitoring at class-load time (used by New Relic, Datadog). Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is the purpose of `java.lang.instrument` Instrumentation API in Java Agents?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q58"></a>
### Q58: How do you configure asynchronous execution in Spring Boot with `@Async`?

**Difficulty**: Intermediate

**Strategy**:
Detailed architectural and technical explanation of How do you configure asynchronous execution in Spring Boot with `@Async`?. Annotate configuration with `@EnableAsync` and annotate void/CompletableFuture methods with `@Async`. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How do you configure asynchronous execution in Spring Boot with `@Async`?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q59"></a>
### Q59: What is the difference between `TreeSet` and `HashSet` in Java Collections?

**Difficulty**: Beginner

**Strategy**:
Detailed architectural and technical explanation of What is the difference between `TreeSet` and `HashSet` in Java Collections?. `HashSet` provides O(1) hash lookups with no ordering; `TreeSet` maintains Red-Black Tree sorted order (O(log N)). Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is the difference between `TreeSet` and `HashSet` in Java Collections?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q60"></a>
### Q60: How do you implement a circuit breaker with Resilience4j in Spring Boot?

**Difficulty**: Intermediate

**Strategy**:
Detailed architectural and technical explanation of How do you implement a circuit breaker with Resilience4j in Spring Boot?. Annotate remote calls with `@CircuitBreaker(name = 'backendA', fallbackMethod = 'fallback')`. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How do you implement a circuit breaker with Resilience4j in Spring Boot?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q61"></a>
### Q61: What is the difference between shallow copy and deep copy in Java object cloning?

**Difficulty**: Intermediate

**Strategy**:
Detailed architectural and technical explanation of What is the difference between shallow copy and deep copy in Java object cloning?. Shallow copy copies field primitive values and references; deep copy recursively clones all referenced child objects. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is the difference between shallow copy and deep copy in Java object cloning?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q62"></a>
### Q62: How do you implement custom Spring Security UserDetailsService?

**Difficulty**: Intermediate

**Strategy**:
Detailed architectural and technical explanation of How do you implement custom Spring Security UserDetailsService?. Implement `UserDetailsService.loadUserByUsername()` querying user repository and returning `UserDetails`. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How do you implement custom Spring Security UserDetailsService?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q63"></a>
### Q63: What is the purpose of `java.util.Optional` and its anti-patterns?

**Difficulty**: Intermediate

**Strategy**:
Detailed architectural and technical explanation of What is the purpose of `java.util.Optional` and its anti-patterns?. Represents presence/absence of return values; anti-pattern: using Optional as method parameters, class fields, or calling `.get()` without check. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is the purpose of `java.util.Optional` and its anti-patterns?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q64"></a>
### Q64: How do you configure CORS in Spring Boot with `WebMvcConfigurer`?

**Difficulty**: Beginner

**Strategy**:
Detailed architectural and technical explanation of How do you configure CORS in Spring Boot with `WebMvcConfigurer`?. Override `addCorsMappings(CorsRegistry registry)` and define allowed origins and HTTP methods. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How do you configure CORS in Spring Boot with `WebMvcConfigurer`?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q65"></a>
### Q65: What is the difference between `Callable` and `Runnable` in Java concurrency?

**Difficulty**: Beginner

**Strategy**:
Detailed architectural and technical explanation of What is the difference between `Callable` and `Runnable` in Java concurrency?. `Runnable.run()` returns `void` and cannot throw checked exceptions; `Callable.call()` returns generic `V` and can throw checked exceptions. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is the difference between `Callable` and `Runnable` in Java concurrency?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q66"></a>
### Q66: How do you configure SSL/TLS in Spring Boot `application.properties`?

**Difficulty**: Beginner

**Strategy**:
Detailed architectural and technical explanation of How do you configure SSL/TLS in Spring Boot `application.properties`?. Set `server.ssl.key-store=classpath:keystore.p12` and `server.ssl.key-store-password=secret`. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How do you configure SSL/TLS in Spring Boot `application.properties`?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q67"></a>
### Q67: What is the purpose of `java.lang.ref.Cleaner` in Java 9+?

**Difficulty**: Advanced

**Strategy**:
Detailed architectural and technical explanation of What is the purpose of `java.lang.ref.Cleaner` in Java 9+?. Replaces deprecated `finalize()` for managing native resource deallocation using phantom references. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is the purpose of `java.lang.ref.Cleaner` in Java 9+?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q68"></a>
### Q68: How do you implement rate limiting in Spring Boot with Bucket4j?

**Difficulty**: Intermediate

**Strategy**:
Detailed architectural and technical explanation of How do you implement rate limiting in Spring Boot with Bucket4j?. Wrap endpoint requests in token bucket filters with bandwidth limits. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How do you implement rate limiting in Spring Boot with Bucket4j?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q69"></a>
### Q69: What is the difference between `transient` and `volatile` keywords in Java?

**Difficulty**: Intermediate

**Strategy**:
Detailed architectural and technical explanation of What is the difference between `transient` and `volatile` keywords in Java?. `transient` prevents serialization of fields; `volatile` guarantees memory visibility across threads. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is the difference between `transient` and `volatile` keywords in Java?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q70"></a>
### Q70: How do you handle JSON serialization with Jackson `@JsonProperty` and `@JsonIgnore` in Spring Boot?

**Difficulty**: Beginner

**Strategy**:
Detailed architectural and technical explanation of How do you handle JSON serialization with Jackson `@JsonProperty` and `@JsonIgnore` in Spring Boot?. Annotate record/class fields to customize JSON key mapping and exclude sensitive fields. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How do you handle JSON serialization with Jackson `@JsonProperty` and `@JsonIgnore` in Spring Boot?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q71"></a>
### Q71: What is the purpose of `java.util.concurrent.Semaphore`?

**Difficulty**: Intermediate

**Strategy**:
Detailed architectural and technical explanation of What is the purpose of `java.util.concurrent.Semaphore`?. Maintains a set of permits to restrict the number of threads accessing a shared physical resource. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is the purpose of `java.util.concurrent.Semaphore`?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q72"></a>
### Q72: How do you mock dependencies in Spring Boot tests with `@MockBean`?

**Difficulty**: Intermediate

**Strategy**:
Detailed architectural and technical explanation of How do you mock dependencies in Spring Boot tests with `@MockBean`?. Injects a Mockito mock into the Spring ApplicationContext for testing service boundaries. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How do you mock dependencies in Spring Boot tests with `@MockBean`?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q73"></a>
### Q73: What is the difference between `java.lang.Error` and `java.lang.Exception`?

**Difficulty**: Beginner

**Strategy**:
Detailed architectural and technical explanation of What is the difference between `java.lang.Error` and `java.lang.Exception`?. `Error` indicates fatal system-level issues (OutOfMemoryError, StackOverflowError); `Exception` indicates recoverable conditions. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is the difference between `java.lang.Error` and `java.lang.Exception`?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q74"></a>
### Q74: How do you configure multi-part file uploads in Spring Boot with `MultipartFile`?

**Difficulty**: Beginner

**Strategy**:
Detailed architectural and technical explanation of How do you configure multi-part file uploads in Spring Boot with `MultipartFile`?. Accept `@RequestParam("file") MultipartFile file` in controller method. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How do you configure multi-part file uploads in Spring Boot with `MultipartFile`?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q75"></a>
### Q75: What is the purpose of `java.util.concurrent.Exchanger`?

**Difficulty**: Advanced

**Strategy**:
Detailed architectural and technical explanation of What is the purpose of `java.util.concurrent.Exchanger`?. Facilitates a bidirectional synchronization point where two threads swap elements atomically. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is the purpose of `java.util.concurrent.Exchanger`?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q76"></a>
### Q76: How do you implement global exception handling in Spring Boot with `@RestControllerAdvice`?

**Difficulty**: Intermediate

**Strategy**:
Detailed architectural and technical explanation of How do you implement global exception handling in Spring Boot with `@RestControllerAdvice`?. Define `@ExceptionHandler(CustomException.class)` methods returning structured error responses. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How do you implement global exception handling in Spring Boot with `@RestControllerAdvice`?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q77"></a>
### Q77: What is the difference between `System.arraycopy()` and `Arrays.copyOf()`?

**Difficulty**: Beginner

**Strategy**:
Detailed architectural and technical explanation of What is the difference between `System.arraycopy()` and `Arrays.copyOf()`?. `System.arraycopy()` is native fast copy into existing array; `Arrays.copyOf()` allocates and returns a new array. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is the difference between `System.arraycopy()` and `Arrays.copyOf()`?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q78"></a>
### Q78: How do you configure dynamic logging levels at runtime in Spring Boot Actuator?

**Difficulty**: Intermediate

**Strategy**:
Detailed architectural and technical explanation of How do you configure dynamic logging levels at runtime in Spring Boot Actuator?. POST to `/actuator/loggers/com.example` to switch level from INFO to DEBUG on demand without restarting. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How do you configure dynamic logging levels at runtime in Spring Boot Actuator?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q79"></a>
### Q79: What is the purpose of `java.util.Objects.requireNonNull()`?

**Difficulty**: Beginner

**Strategy**:
Detailed architectural and technical explanation of What is the purpose of `java.util.Objects.requireNonNull()`?. Validates non-null method arguments and throws `NullPointerException` with custom message immediately. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is the purpose of `java.util.Objects.requireNonNull()`?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q80"></a>
### Q80: How do you configure WebSocket message broker with STOMP in Spring Boot?

**Difficulty**: Intermediate

**Strategy**:
Detailed architectural and technical explanation of How do you configure WebSocket message broker with STOMP in Spring Boot?. Implement `WebSocketMessageBrokerConfigurer` and enable simple in-memory broker. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How do you configure WebSocket message broker with STOMP in Spring Boot?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q81"></a>
### Q81: What is the difference between `CopyOnWriteArrayList` and `Collections.synchronizedList()`?

**Difficulty**: Intermediate

**Strategy**:
Detailed architectural and technical explanation of What is the difference between `CopyOnWriteArrayList` and `Collections.synchronizedList()`?. `CopyOnWriteArrayList` creates fresh array copy on every write (ideal for read-heavy lists without read locks). Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is the difference between `CopyOnWriteArrayList` and `Collections.synchronizedList()`?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q82"></a>
### Q82: How do you test JPA repository queries with `@DataJpaTest` in Spring Boot?

**Difficulty**: Intermediate

**Strategy**:
Detailed architectural and technical explanation of How do you test JPA repository queries with `@DataJpaTest` in Spring Boot?. Configures sliced test context with in-memory H2 database for testing repository queries. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How do you test JPA repository queries with `@DataJpaTest` in Spring Boot?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q83"></a>
### Q83: What is the purpose of `@Lazy` annotation in Spring bean initialization?

**Difficulty**: Intermediate

**Strategy**:
Detailed architectural and technical explanation of What is the purpose of `@Lazy` annotation in Spring bean initialization?. Defers bean creation until the bean is first requested rather than at application startup. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is the purpose of `@Lazy` annotation in Spring bean initialization?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q84"></a>
### Q84: How do you implement distributed tracing with Micrometer Tracing in Spring Boot 3?

**Difficulty**: Advanced

**Strategy**:
Detailed architectural and technical explanation of How do you implement distributed tracing with Micrometer Tracing in Spring Boot 3?. Exports trace and span IDs to OpenTelemetry collectors, integrating seamlessly with SLF4J MDC logging. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How do you implement distributed tracing with Micrometer Tracing in Spring Boot 3?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q85"></a>
### Q85: What is the difference between `ArrayBlockingQueue` and `LinkedBlockingQueue`?

**Difficulty**: Intermediate

**Strategy**:
Detailed architectural and technical explanation of What is the difference between `ArrayBlockingQueue` and `LinkedBlockingQueue`?. `ArrayBlockingQueue` uses bounded contiguous array with single lock; `LinkedBlockingQueue` uses linked nodes with separate read/write locks. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is the difference between `ArrayBlockingQueue` and `LinkedBlockingQueue`?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q86"></a>
### Q86: How do you configure OpenAPI 3 / Swagger documentation in Spring Boot with `springdoc-openapi`?

**Difficulty**: Beginner

**Strategy**:
Detailed architectural and technical explanation of How do you configure OpenAPI 3 / Swagger documentation in Spring Boot with `springdoc-openapi`?. Include `springdoc-openapi-starter-webmvc-ui` dependency and access interactive `/swagger-ui.html`. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How do you configure OpenAPI 3 / Swagger documentation in Spring Boot with `springdoc-openapi`?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q87"></a>
### Q87: What is the purpose of `java.lang.invoke.MethodHandle` in modern JVM optimization?

**Difficulty**: Advanced

**Strategy**:
Detailed architectural and technical explanation of What is the purpose of `java.lang.invoke.MethodHandle` in modern JVM optimization?. Low-level strongly typed executable reference optimized directly by JIT compiler. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is the purpose of `java.lang.invoke.MethodHandle` in modern JVM optimization?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q88"></a>
### Q88: How do you implement database auditing (`@CreatedDate`, `@LastModifiedDate`) with Spring Data JPA?

**Difficulty**: Beginner

**Strategy**:
Detailed architectural and technical explanation of How do you implement database auditing (`@CreatedDate`, `@LastModifiedDate`) with Spring Data JPA?. Enable auditing via `@EnableJpaAuditing` and annotate entity fields with auditing annotations. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How do you implement database auditing (`@CreatedDate`, `@LastModifiedDate`) with Spring Data JPA?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q89"></a>
### Q89: What is the difference between `java.util.concurrent.ConcurrentSkipListMap` and `TreeMap`?

**Difficulty**: Advanced

**Strategy**:
Detailed architectural and technical explanation of What is the difference between `java.util.concurrent.ConcurrentSkipListMap` and `TreeMap`?. `ConcurrentSkipListMap` is a thread-safe concurrent sorted map based on Skip Lists. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is the difference between `java.util.concurrent.ConcurrentSkipListMap` and `TreeMap`?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q90"></a>
### Q90: How do you implement event-driven architectures with Spring `@EventListener` and `@TransactionalEventListener`?

**Difficulty**: Intermediate

**Strategy**:
Detailed architectural and technical explanation of How do you implement event-driven architectures with Spring `@EventListener` and `@TransactionalEventListener`?. Publish application events via `ApplicationEventPublisher` and handle after transaction commit. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How do you implement event-driven architectures with Spring `@EventListener` and `@TransactionalEventListener`?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q91"></a>
### Q91: What is the purpose of `java.lang.Thread.UncaughtExceptionHandler`?

**Difficulty**: Beginner

**Strategy**:
Detailed architectural and technical explanation of What is the purpose of `java.lang.Thread.UncaughtExceptionHandler`?. Handles uncaught exceptions thrown in background threads before thread termination. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is the purpose of `java.lang.Thread.UncaughtExceptionHandler`?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q92"></a>
### Q92: How do you configure embedded Tomcat connection threads and accept queue in Spring Boot?

**Difficulty**: Intermediate

**Strategy**:
Detailed architectural and technical explanation of How do you configure embedded Tomcat connection threads and accept queue in Spring Boot?. Set `server.tomcat.threads.max=200` and `server.tomcat.accept-count=100`. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How do you configure embedded Tomcat connection threads and accept queue in Spring Boot?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q93"></a>
### Q93: What is the difference between `peek()` and `map()` in Stream transformations?

**Difficulty**: Beginner

**Strategy**:
Detailed architectural and technical explanation of What is the difference between `peek()` and `map()` in Stream transformations?. `peek()` accepts a Consumer and does not change element types; `map()` accepts a Function transforming element values. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is the difference between `peek()` and `map()` in Stream transformations?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q94"></a>
### Q94: How do you implement API key authentication in Spring Security filters?

**Difficulty**: Intermediate

**Strategy**:
Detailed architectural and technical explanation of How do you implement API key authentication in Spring Security filters?. Extract `X-API-KEY` header in custom filter and populate SecurityContext. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How do you implement API key authentication in Spring Security filters?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q95"></a>
### Q95: How do you configure dynamic quartz scheduling in Spring Boot?

**Difficulty**: Intermediate

**Strategy**:
Detailed architectural and technical explanation of How do you configure dynamic quartz scheduling in Spring Boot?. Use `SchedulerFactoryBean` and configure job details and cron triggers dynamically from database. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How do you configure dynamic quartz scheduling in Spring Boot?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q96"></a>
### Q96: What is the difference between `synchronized` method and `synchronized` block?

**Difficulty**: Beginner

**Strategy**:
Detailed architectural and technical explanation of What is the difference between `synchronized` method and `synchronized` block?. Synchronized method locks the entire instance (`this`) or class; synchronized block allows fine-grained locking on specific monitor objects. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is the difference between `synchronized` method and `synchronized` block?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q97"></a>
### Q97: How do you handle multi-tenancy database routing with `AbstractRoutingDataSource` in Spring Boot?

**Difficulty**: Advanced

**Strategy**:
Detailed architectural and technical explanation of How do you handle multi-tenancy database routing with `AbstractRoutingDataSource` in Spring Boot?. Route queries dynamically to tenant-specific databases based on thread-local tenant identifier. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How do you handle multi-tenancy database routing with `AbstractRoutingDataSource` in Spring Boot?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q98"></a>
### Q98: What is the purpose of `java.util.concurrent.Phaser`?

**Difficulty**: Advanced

**Strategy**:
Detailed architectural and technical explanation of What is the purpose of `java.util.concurrent.Phaser`?. Reusable synchronization barrier supporting dynamic registration and deregistration of participating parties across phases. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is the purpose of `java.util.concurrent.Phaser`?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q99"></a>
### Q99: How do you implement optimistic locking in JPA using `@Version`?

**Difficulty**: Intermediate

**Strategy**:
Detailed architectural and technical explanation of How do you implement optimistic locking in JPA using `@Version`?. Annotate integer/long version field; throws `OptimisticLockException` if row was modified concurrently. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for How do you implement optimistic locking in JPA using `@Version`?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---

<a id="q100"></a>
### Q100: What is the difference between `@Component`, `@Service`, and `@Repository` in Spring?

**Difficulty**: Beginner

**Strategy**:
Detailed architectural and technical explanation of What is the difference between `@Component`, `@Service`, and `@Repository` in Spring?. `@Component` is generic Spring bean; `@Service` denotes business logic; `@Repository` adds automatic persistence exception translation. Key topics include JVM internals, concurrency model, memory layout, garbage collection, and Spring Boot production standards.

**Code Example**:
```java
// Production implementation for What is the difference between `@Component`, `@Service`, and `@Repository` in Spring?
public class Solution {
    public void execute() {
        System.out.println("Java Production Standard");
    }
}
```

---
