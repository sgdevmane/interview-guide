<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>Java Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for developers</b></p>
</div>

---

## Table of Contents

1. [How do you optimize memory usage by handling String duplicates efficiently?](#q1-how-do-you-optimize-memory-usage-by-handling-string-duplicates-efficiently) <span class="beginner">Beginner</span>
2. [How do you prevent memory leaks?](#q2-how-do-you-prevent-memory-leaks) <span class="intermediate">Intermediate</span>
3. [How do you execute tasks asynchronously and get the result later?](#q3-how-do-you-execute-tasks-asynchronously-and-get-the-result-later) <span class="intermediate">Intermediate</span>
4. [How do you handle null safety efficiently in modern Java?](#q4-how-do-you-handle-null-safety-efficiently-in-modern-java) <span class="beginner">Beginner</span>
5. [How do you ensure thread safety when modifying shared variables?](#q5-how-do-you-ensure-thread-safety-when-modifying-shared-variables) <span class="intermediate">Intermediate</span>
6. [How do you create an immutable class in Java?](#q6-how-do-you-create-an-immutable-class-in-java) <span class="intermediate">Intermediate</span>
7. [How do you process a collection of items in parallel?](#q7-how-do-you-process-a-collection-of-items-in-parallel) <span class="intermediate">Intermediate</span>
8. [How do you implement the Singleton pattern thread-safely?](#q8-how-do-you-implement-the-singleton-pattern-thread-safely) <span class="intermediate">Intermediate</span>
9. [How do you sort a list of objects based on multiple criteria?](#q9-how-do-you-sort-a-list-of-objects-based-on-multiple-criteria) <span class="beginner">Beginner</span>
10. [How do you handle exceptions in Lambda expressions?](#q10-how-do-you-handle-exceptions-in-lambda-expressions) <span class="intermediate">Intermediate</span>
11. [How do you dynamically access methods or fields at runtime?](#q11-how-do-you-dynamically-access-methods-or-fields-at-runtime) <span class="advanced">Advanced</span>
12. [How do you ensure a variable's value is always read from main memory?](#q12-how-do-you-ensure-a-variables-value-is-always-read-from-main-memory) <span class="advanced">Advanced</span>
13. [How do you filter a list using the Stream API?](#q13-how-do-you-filter-a-list-using-the-stream-api) <span class="beginner">Beginner</span>
14. [How do you create a fixed-size thread pool?](#q14-how-do-you-create-a-fixed-size-thread-pool) <span class="intermediate">Intermediate</span>
15. [How do you implement a custom annotation?](#q15-how-do-you-implement-a-custom-annotation) <span class="intermediate">Intermediate</span>
16. [How do you create a custom Spring Boot Starter?](#q16-how-do-you-create-a-custom-spring-boot-starter) <span class="advanced">Advanced</span>
17. [How do you implement AOP for logging execution time?](#q17-how-do-you-implement-aop-for-logging-execution-time) <span class="intermediate">Intermediate</span>
18. [What are Java Records and when should you use them?](#q18-what-are-java-records-and-when-should-you-use-them) <span class="beginner">Beginner</span>
19. [How do Sealed Classes control inheritance hierarchy?](#q19-how-do-sealed-classes-control-inheritance-hierarchy) <span class="intermediate">Intermediate</span>
20. [How do you use Pattern Matching in Switch expressions?](#q20-how-do-you-use-pattern-matching-in-switch-expressions) <span class="intermediate">Intermediate</span>
21. [How do Virtual Threads (Project Loom) differ from Platform Threads?](#q21-how-do-virtual-threads-project-loom-differ-from-platform-threads) <span class="advanced">Advanced</span>
22. [How do you use Structured Concurrency?](#q22-how-do-you-use-structured-concurrency) <span class="advanced">Advanced</span>
23. [How do you tune Garbage Collection for low latency?](#q23-how-do-you-tune-garbage-collection-for-low-latency) <span class="advanced">Advanced</span>
24. [How do you chain multiple asynchronous tasks?](#q24-how-do-you-chain-multiple-asynchronous-tasks) <span class="intermediate">Intermediate</span>
25. [How do you group elements in a Stream?](#q25-how-do-you-group-elements-in-a-stream) <span class="intermediate">Intermediate</span>
26. [How do you flatten a list of lists using Streams?](#q26-how-do-you-flatten-a-list-of-lists-using-streams) <span class="intermediate">Intermediate</span>
27. [How do you solve the N+1 Select problem in Hibernate/JPA?](#q27-how-do-you-solve-the-n+1-select-problem-in-hibernatejpa) <span class="advanced">Advanced</span>
28. [How do you implement Caching with Redis in Spring Boot?](#q28-how-do-you-implement-caching-with-redis-in-spring-boot) <span class="intermediate">Intermediate</span>
29. [How do you implement a Circuit Breaker using Resilience4j?](#q29-how-do-you-implement-a-circuit-breaker-using-resilience4j) <span class="advanced">Advanced</span>
30. [How do you unit test a Spring Service with Mockito?](#q30-how-do-you-unit-test-a-spring-service-with-mockito) <span class="intermediate">Intermediate</span>
31. [How do you handle global exceptions in Spring Boot?](#q31-how-do-you-handle-global-exceptions-in-spring-boot) <span class="intermediate">Intermediate</span>
32. [How do you create a Dockerfile for a Java application?](#q32-how-do-you-create-a-dockerfile-for-a-java-application) <span class="intermediate">Intermediate</span>
33. [How do you implement an API Gateway pattern?](#q33-how-do-you-implement-an-api-gateway-pattern) <span class="advanced">Advanced</span>
34. [How do you create a non-blocking REST API with Spring WebFlux?](#q34-how-do-you-create-a-non-blocking-rest-api-with-spring-webflux) <span class="advanced">Advanced</span>
35. [How do you implement Health Checks in Spring Boot?](#q35-how-do-you-implement-health-checks-in-spring-boot) <span class="beginner">Beginner</span>
36. [How do you ensure a specific execution order of beans?](#q36-how-do-you-ensure-a-specific-execution-order-of-beans) <span class="beginner">Beginner</span>
37. [How do you handle configuration for multiple environments?](#q37-how-do-you-handle-configuration-for-multiple-environments) <span class="beginner">Beginner</span>
38. [How do you implement a Kafka Consumer with Spring Boot?](#q38-how-do-you-implement-a-kafka-consumer-with-spring-boot) <span class="intermediate">Intermediate</span>
39. [How do you secure passwords in Java?](#q39-how-do-you-secure-passwords-in-java) <span class="intermediate">Intermediate</span>
40. [How do you debug a deadlock in Java?](#q40-how-do-you-debug-a-deadlock-in-java) <span class="advanced">Advanced</span>
41. [How do you implement the Singleton pattern safely in Java?](#q41-how-do-you-implement-the-singleton-pattern-safely-in-java) <span class="beginner">Beginner</span>
42. [How do you implement the Factory Pattern using Java 8+ features?](#q42-how-do-you-implement-the-factory-pattern-using-java-8+-features) <span class="intermediate">Intermediate</span>
43. [How do you implement the Strategy Pattern with Lambdas?](#q43-how-do-you-implement-the-strategy-pattern-with-lambdas) <span class="intermediate">Intermediate</span>
44. [How do you implement the Observer Pattern using Spring Events?](#q44-how-do-you-implement-the-observer-pattern-using-spring-events) <span class="intermediate">Intermediate</span>
45. [What is the difference between REQUIRED and REQUIRES_NEW transaction propagation?](#q45-what-is-the-difference-between-required-and-requires_new-transaction-propagation) <span class="advanced">Advanced</span>
46. [How do you implement Optimistic Locking in JPA?](#q46-how-do-you-implement-optimistic-locking-in-jpa) <span class="intermediate">Intermediate</span>
47. [How do you chain multiple asynchronous tasks using CompletableFuture?](#q47-how-do-you-chain-multiple-asynchronous-tasks-using-completablefuture) <span class="advanced">Advanced</span>
48. [How do you write a Parameterized Test in JUnit 5?](#q48-how-do-you-write-a-parameterized-test-in-junit-5) <span class="intermediate">Intermediate</span>
49. [How do you use TestContainers for integration testing?](#q49-how-do-you-use-testcontainers-for-integration-testing) <span class="advanced">Advanced</span>
50. [How do you implement a simple Rate Limiter using Bucket4j?](#q50-how-do-you-implement-a-simple-rate-limiter-using-bucket4j) <span class="advanced">Advanced</span>
51. [How do you implement Distributed Locking with Redis (Redisson)?](#q51-how-do-you-implement-distributed-locking-with-redis-redisson) <span class="advanced">Advanced</span>
52. [How do you handle JWT Authentication in Spring Security?](#q52-how-do-you-handle-jwt-authentication-in-spring-security) <span class="advanced">Advanced</span>
53. [How do you expose a custom metric in Spring Boot Actuator?](#q53-how-do-you-expose-a-custom-metric-in-spring-boot-actuator) <span class="intermediate">Intermediate</span>
54. [What is the difference between @Mock and @Spy in Mockito?](#q54-what-is-the-difference-between-@mock-and-@spy-in-mockito) <span class="intermediate">Intermediate</span>
55. [How do you solve the 'LazyInitializationException' in Hibernate?](#q55-how-do-you-solve-the-lazyinitializationexception-in-hibernate) <span class="intermediate">Intermediate</span>
56. [How do you implement a simple REST Client using RestClient (Spring Boot 3.2+)?](#q56-how-do-you-implement-a-simple-rest-client-using-restclient-spring-boot-3.2+) <span class="intermediate">Intermediate</span>
57. [How do you use 'var' (Local Variable Type Inference)?](#q57-how-do-you-use-var-local-variable-type-inference) <span class="beginner">Beginner</span>
58. [What are Text Blocks and how do they simplify String handling?](#q58-what-are-text-blocks-and-how-do-they-simplify-string-handling) <span class="beginner">Beginner</span>
59. [How do you use SequencedCollection in Java 21?](#q59-how-do-you-use-sequencedcollection-in-java-21) <span class="intermediate">Intermediate</span>
60. [How does ConcurrentHashMap ensure thread safety without locking the entire map?](#q60-how-does-concurrenthashmap-ensure-thread-safety-without-locking-the-entire-map) <span class="advanced">Advanced</span>
61. [What is the difference between WeakReference and SoftReference?](#q61-what-is-the-difference-between-weakreference-and-softreference) <span class="advanced">Advanced</span>
62. [How do you use Spring Data JPA Projections to optimize read performance?](#q62-how-do-you-use-spring-data-jpa-projections-to-optimize-read-performance) <span class="intermediate">Intermediate</span>
63. [How do you implement a Dead Letter Queue (DLQ) in Kafka with Spring Boot?](#q63-how-do-you-implement-a-dead-letter-queue-dlq-in-kafka-with-spring-boot) <span class="advanced">Advanced</span>
64. [How do you use Feign Client for declarative REST communication?](#q64-how-do-you-use-feign-client-for-declarative-rest-communication) <span class="intermediate">Intermediate</span>
65. [How do you configure L2 Cache in Hibernate?](#q65-how-do-you-configure-l2-cache-in-hibernate) <span class="advanced">Advanced</span>
66. [How do you secure methods using @PreAuthorize in Spring Security?](#q66-how-do-you-secure-methods-using-@preauthorize-in-spring-security) <span class="intermediate">Intermediate</span>
67. [How do you handle transactions programmatically (TransactionTemplate)?](#q67-how-do-you-handle-transactions-programmatically-transactiontemplate) <span class="advanced">Advanced</span>
68. [How do you implement a custom validation annotation (Bean Validation)?](#q68-how-do-you-implement-a-custom-validation-annotation-bean-validation) <span class="intermediate">Intermediate</span>
69. [How do you use CompletableFuture.allOf to wait for multiple tasks?](#q69-how-do-you-use-completablefuture.allof-to-wait-for-multiple-tasks) <span class="intermediate">Intermediate</span>
70. [How do you profile a Java application using JFR (Java Flight Recorder)?](#q70-how-do-you-profile-a-java-application-using-jfr-java-flight-recorder) <span class="advanced">Advanced</span>
71. [How do you implement a retry mechanism with exponential backoff?](#q71-how-do-you-implement-a-retry-mechanism-with-exponential-backoff) <span class="intermediate">Intermediate</span>
72. [How do you handle Java internationalization (i18n) in microservices?](#q72-how-do-you-handle-java-internationalization-i18n-in-microservices) <span class="intermediate">Intermediate</span>
73. [How do you ensure Java accessibility (a11y) in mobile devices?](#q73-how-do-you-ensure-java-accessibility-a11y-in-mobile-devices) <span class="beginner">Beginner</span>
74. [How do you optimize Java network requests in legacy systems?](#q74-how-do-you-optimize-java-network-requests-in-legacy-systems) <span class="advanced">Advanced</span>
75. [How do you handle Java performance optimization for cloud infrastructure?](#q75-how-do-you-handle-java-performance-optimization-for-cloud-infrastructure) <span class="advanced">Advanced</span>
76. [What are the security implications of Java in real-time systems?](#q76-what-are-the-security-implications-of-java-in-real-time-systems) <span class="intermediate">Intermediate</span>
77. [How do you debug Java memory leaks in distributed systems?](#q77-how-do-you-debug-java-memory-leaks-in-distributed-systems) <span class="advanced">Advanced</span>
78. [Best practices for Java code organization in high-traffic sites?](#q78-best-practices-for-java-code-organization-in-high-traffic-sites) <span class="beginner">Beginner</span>
79. [How do you implement Java error handling for embedded systems?](#q79-how-do-you-implement-java-error-handling-for-embedded-systems) <span class="intermediate">Intermediate</span>
80. [How do you test Java functionality in production environments?](#q80-how-do-you-test-java-functionality-in-production-environments) <span class="intermediate">Intermediate</span>
81. [How do you handle Java state management in large scale applications?](#q81-how-do-you-handle-java-state-management-in-large-scale-applications) <span class="advanced">Advanced</span>
82. [How do you perform Java data validation in microservices?](#q82-how-do-you-perform-java-data-validation-in-microservices) <span class="beginner">Beginner</span>
83. [How do you automate Java deployment for mobile devices?](#q83-how-do-you-automate-java-deployment-for-mobile-devices) <span class="advanced">Advanced</span>
84. [How do you handle Java concurrency issues in legacy systems?](#q84-how-do-you-handle-java-concurrency-issues-in-legacy-systems) <span class="advanced">Advanced</span>
85. [How do you implement Java caching in cloud infrastructure?](#q85-how-do-you-implement-java-caching-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
86. [How do you manage Java configuration for real-time systems?](#q86-how-do-you-manage-java-configuration-for-real-time-systems) <span class="beginner">Beginner</span>
87. [How do you handle Java internationalization (i18n) in distributed systems?](#q87-how-do-you-handle-java-internationalization-i18n-in-distributed-systems) <span class="intermediate">Intermediate</span>
88. [How do you ensure Java accessibility (a11y) in high-traffic sites?](#q88-how-do-you-ensure-java-accessibility-a11y-in-high-traffic-sites) <span class="beginner">Beginner</span>
89. [How do you optimize Java network requests in embedded systems?](#q89-how-do-you-optimize-java-network-requests-in-embedded-systems) <span class="advanced">Advanced</span>
90. [How do you handle Java performance optimization for production environments?](#q90-how-do-you-handle-java-performance-optimization-for-production-environments) <span class="advanced">Advanced</span>
91. [What are the security implications of Java in large scale applications?](#q91-what-are-the-security-implications-of-java-in-large-scale-applications) <span class="intermediate">Intermediate</span>
92. [How do you debug Java memory leaks in microservices?](#q92-how-do-you-debug-java-memory-leaks-in-microservices) <span class="advanced">Advanced</span>
93. [Best practices for Java code organization in mobile devices?](#q93-best-practices-for-java-code-organization-in-mobile-devices) <span class="beginner">Beginner</span>
94. [How do you implement Java error handling for legacy systems?](#q94-how-do-you-implement-java-error-handling-for-legacy-systems) <span class="intermediate">Intermediate</span>
95. [How do you test Java functionality in cloud infrastructure?](#q95-how-do-you-test-java-functionality-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
96. [How do you handle Java state management in real-time systems?](#q96-how-do-you-handle-java-state-management-in-real-time-systems) <span class="advanced">Advanced</span>
97. [How do you perform Java data validation in distributed systems?](#q97-how-do-you-perform-java-data-validation-in-distributed-systems) <span class="beginner">Beginner</span>
98. [How do you automate Java deployment for high-traffic sites?](#q98-how-do-you-automate-java-deployment-for-high-traffic-sites) <span class="advanced">Advanced</span>
99. [How do you handle Java concurrency issues in embedded systems?](#q99-how-do-you-handle-java-concurrency-issues-in-embedded-systems) <span class="advanced">Advanced</span>
100. [How do you implement Java caching in production environments?](#q100-how-do-you-implement-java-caching-in-production-environments) <span class="intermediate">Intermediate</span>

---

### Q1: How do you optimize memory usage by handling String duplicates efficiently?

**Difficulty**: Beginner

**Strategy:**
Use **String Interning** (`String.intern()`) or the **String Deduplication** feature in G1GC. Avoid creating new String objects with `new String("...")` unnecessarily.

**Code Example:**
```java
// BAD: Creates a new object in heap
String s1 = new String("hello");

// GOOD: Uses String Constant Pool
String s2 = "hello";

// GOOD: Manually intern (if computed at runtime)
String s3 = new String("hello").intern();

System.out.println(s2 == s3); // true
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q2: How do you prevent memory leaks?

**Difficulty**: Intermediate

**Strategy:**
Avoid static references to large objects, close resources (Streams, Connections) using **try-with-resources**, and unregister listeners/callbacks when no longer needed.

**Code Example:**
```java
// GOOD: Auto-close resource
try (BufferedReader br = new BufferedReader(new FileReader("file.txt"))) {
    System.out.println(br.readLine());
} catch (IOException e) {
    e.printStackTrace();
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q3: How do you execute tasks asynchronously and get the result later?

**Difficulty**: Intermediate

**Strategy:**
Use **CompletableFuture**. It allows non-blocking execution and chaining of tasks (callbacks) when the result is available.

**Code Example:**
```java
CompletableFuture.supplyAsync(() -> {
    // Long running task
    return "Result";
}).thenAccept(result -> {
    System.out.println("Got: " + result);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q4: How do you handle null safety efficiently in modern Java?

**Difficulty**: Beginner

**Strategy:**
Use **Optional<T>** to represent a value that might be absent, avoiding `NullPointerException`.

**Code Example:**
```java
Optional<String> optionalName = Optional.ofNullable(getName());

// Execute only if present
optionalName.ifPresent(System.out::println);

// Default value
String name = optionalName.orElse("Unknown");
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q5: How do you ensure thread safety when modifying shared variables?

**Difficulty**: Intermediate

**Strategy:**
Use **Atomic Classes** (like `AtomicInteger`) for simple counters, or `synchronized` blocks/`ReentrantLock` for complex critical sections.

**Code Example:**
```java
import java.util.concurrent.atomic.AtomicInteger;

class Counter {
    private AtomicInteger count = new AtomicInteger(0);

    public void increment() {
        count.incrementAndGet(); // Thread-safe
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q6: How do you create an immutable class in Java?

**Difficulty**: Intermediate

**Strategy:**
Declare the class `final`, make all fields `private final`, do not provide setters, and return deep copies of mutable fields in getters.

**Code Example:**
```java
public final class User {
    private final String name;
    private final List<String> roles;

    public User(String name, List<String> roles) {
        this.name = name;
        this.roles = new ArrayList<>(roles); // Deep copy
    }

    public List<String> getRoles() {
        return new ArrayList<>(roles); // Return copy
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q7: How do you process a collection of items in parallel?

**Difficulty**: Intermediate

**Strategy:**
Use **Parallel Streams** (`collection.parallelStream()`). It utilizes the ForkJoinPool to split the task across multiple threads.

**Code Example:**
```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);

numbers.parallelStream()
       .map(n -> n * n)
       .forEach(System.out::println);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q8: How do you implement the Singleton pattern thread-safely?

**Difficulty**: Intermediate

**Strategy:**
Use an **Enum** (simplest and safest) or **Double-Checked Locking** with `volatile`.

**Code Example:**
```java
// Best practice
public enum Singleton {
    INSTANCE;
    
    public void doSomething() {
        System.out.println("Doing something");
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q9: How do you sort a list of objects based on multiple criteria?

**Difficulty**: Beginner

**Strategy:**
Use `Comparator.comparing()` chained with `thenComparing()`.

**Code Example:**
```java
List<User> users = getUsers();

users.sort(Comparator.comparing(User::getLastName)
                     .thenComparing(User::getFirstName));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q10: How do you handle exceptions in Lambda expressions?

**Difficulty**: Intermediate

**Strategy:**
Since standard functional interfaces don't throw checked exceptions, wrap the code in a try-catch block or write a wrapper method/interface that handles the exception.

**Code Example:**
```java
list.forEach(item -> {
    try {
        process(item);
    } catch (Exception e) {
        System.err.println("Error: " + e);
    }
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q11: How do you dynamically access methods or fields at runtime?

**Difficulty**: Advanced

**Strategy:**
Use the **Reflection API**. It allows inspection and modification of classes, fields, and methods at runtime, though it has performance overhead.

**Code Example:**
```java
Class<?> clazz = Class.forName("com.example.User");
Method method = clazz.getMethod("getName");
Object instance = clazz.getConstructor().newInstance();
Object result = method.invoke(instance);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q12: How do you ensure a variable's value is always read from main memory?

**Difficulty**: Advanced

**Strategy:**
Use the `volatile` keyword. It guarantees visibility of changes to variables across threads (happens-before relationship), preventing CPU caching of that variable.

**Code Example:**
```java
private volatile boolean running = true;

public void stop() {
    running = false; // Immediately visible to other threads
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q13: How do you filter a list using the Stream API?

**Difficulty**: Beginner

**Strategy:**
Use `.filter(Predicate)`.

**Code Example:**
```java
List<String> names = Arrays.asList("Alice", "Bob", "Charlie");

List<String> filtered = names.stream()
                             .filter(name -> name.startsWith("A"))
                             .collect(Collectors.toList());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q14: How do you create a fixed-size thread pool?

**Difficulty**: Intermediate

**Strategy:**
Use `Executors.newFixedThreadPool(n)`. It reuses a fixed number of threads for executing tasks.

**Code Example:**
```java
ExecutorService executor = Executors.newFixedThreadPool(5);

for (int i = 0; i < 10; i++) {
    executor.submit(() -> System.out.println("Task running"));
}
executor.shutdown();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q15: How do you implement a custom annotation?

**Difficulty**: Intermediate

**Strategy:**
Define an interface with `@interface`. Use meta-annotations like `@Retention` and `@Target` to define scope and applicability.

**Code Example:**
```java
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
public @interface LogExecutionTime {
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q16: How do you create a custom Spring Boot Starter?

**Difficulty**: Advanced

**Strategy:**
Create a separate module with an **AutoConfiguration** class, register it in `META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports` (Spring Boot 3+), and optionally provide a `Properties` class for configuration.

**Code Example:**
```java
@Configuration
@ConditionalOnClass(MyService.class)
@EnableConfigurationProperties(MyProperties.class)
public class MyStarterAutoConfiguration {

    @Bean
    @ConditionalOnMissingBean
    public MyService myService(MyProperties properties) {
        return new MyService(properties.getConfig());
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q17: How do you implement AOP for logging execution time?

**Difficulty**: Intermediate

**Strategy:**
Use Spring AOP with `@Aspect` and `@Around`. This allows you to intercept method execution, start a timer, proceed with the execution, and log the duration.

**Code Example:**
```java
@Aspect
@Component
public class LoggingAspect {
    @Around("@annotation(LogExecutionTime)")
    public Object logExecutionTime(ProceedingJoinPoint joinPoint) throws Throwable {
        long start = System.currentTimeMillis();
        Object proceed = joinPoint.proceed();
        long executionTime = System.currentTimeMillis() - start;
        System.out.println(joinPoint.getSignature() + " executed in " + executionTime + "ms");
        return proceed;
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q18: What are Java Records and when should you use them?

**Difficulty**: Beginner

**Strategy:**
Records (introduced in Java 14/16) are immutable data carriers. They automatically generate `constructor`, `getters` (without `get` prefix), `equals()`, `hashCode()`, and `toString()`. Use them for DTOs and configuration objects.

**Code Example:**
```java
public record Point(int x, int y) {}

// Usage
Point p = new Point(10, 20);
System.out.println(p.x()); // 10
System.out.println(p);     // Point[x=10, y=20]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q19: How do Sealed Classes control inheritance hierarchy?

**Difficulty**: Intermediate

**Strategy:**
Sealed classes (`sealed`) restrict which classes can extend them using `permits`. This provides better control over the hierarchy and enables exhaustive pattern matching in switch expressions.

**Code Example:**
```java
public sealed interface Shape permits Circle, Rectangle {}

public final class Circle implements Shape {}
public final class Rectangle implements Shape {}
// public class Triangle implements Shape {} // Compilation Error
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q20: How do you use Pattern Matching in Switch expressions?

**Difficulty**: Intermediate

**Strategy:**
Use modern `switch` expressions (Java 17+) to handle different types directly without casting. It works well with Sealed Classes for exhaustive checks.

**Code Example:**
```java
String result = switch (obj) {
    case Integer i -> "It's an integer: " + i;
    case String s -> "It's a string: " + s;
    case null -> "It's null";
    default -> "Unknown type";
};
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q21: How do Virtual Threads (Project Loom) differ from Platform Threads?

**Difficulty**: Advanced

**Strategy:**
**Virtual Threads** (Java 21) are lightweight user-mode threads managed by the JVM, not the OS. They allow creating millions of threads for high-throughput concurrent applications (blocking I/O), whereas Platform Threads are expensive OS threads.

**Code Example:**
```java
try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
    IntStream.range(0, 10_000).forEach(i -> {
        executor.submit(() -> {
            Thread.sleep(Duration.ofSeconds(1));
            return i;
        });
    });
} // Executor auto-closes and waits for tasks
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q22: How do you use Structured Concurrency?

**Difficulty**: Advanced

**Strategy:**
Structured Concurrency (Preview) treats multiple tasks running in different threads as a single unit of work. It simplifies error handling and cancellation.

**Code Example:**
```java
try (var scope = new StructuredTaskScope.ShutdownOnFailure()) {
    Supplier<String> user  = scope.fork(() -> fetchUser(id));
    Supplier<List<Order>> orders = scope.fork(() -> fetchOrders(id));

    scope.join().throwIfFailed(); // Wait for all, fail if any fails

    return new Response(user.get(), orders.get());
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q23: How do you tune Garbage Collection for low latency?

**Difficulty**: Advanced

**Strategy:**
Use **ZGC** (Java 15+) or **Shenandoah GC** for sub-millisecond pause times on large heaps. Alternatively, tune **G1GC** (default) by adjusting max pause time targets.

**Code Example:**
```bash
# Enable ZGC
java -XX:+UseZGC -jar app.jar

# Tune G1GC for 200ms max pause
java -XX:+UseG1GC -XX:MaxGCPauseMillis=200 -jar app.jar
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q24: How do you chain multiple asynchronous tasks?

**Difficulty**: Intermediate

**Strategy:**
Use `CompletableFuture.thenCompose()` to chain dependent tasks (flatmap style) or `thenCombine()` to run tasks in parallel and combine results.

**Code Example:**
```java
CompletableFuture.supplyAsync(() -> fetchUserId())
    .thenCompose(userId -> fetchUserDetails(userId))
    .thenAccept(details -> System.out.println(details));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q25: How do you group elements in a Stream?

**Difficulty**: Intermediate

**Strategy:**
Use `Collectors.groupingBy()`. It returns a Map where keys are the classification and values are Lists of items.

**Code Example:**
```java
Map<String, List<Person>> byCity = people.stream()
    .collect(Collectors.groupingBy(Person::getCity));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q26: How do you flatten a list of lists using Streams?

**Difficulty**: Intermediate

**Strategy:**
Use `.flatMap()` to transform each element into a stream and flatten the result into a single stream.

**Code Example:**
```java
List<List<String>> nested = Arrays.asList(
    Arrays.asList("a", "b"), 
    Arrays.asList("c", "d")
);

List<String> flat = nested.stream()
    .flatMap(List::stream)
    .collect(Collectors.toList());
// Result: [a, b, c, d]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q27: How do you solve the N+1 Select problem in Hibernate/JPA?

**Difficulty**: Advanced

**Strategy:**
Use **JOIN FETCH** in JPQL to load related entities in a single query, or use **Entity Graphs**.

**Code Example:**
```java
// BAD: Triggers N+1 queries if accessing orders
@Query("SELECT u FROM User u")
List<User> findAll();

// GOOD: Fetches orders in the same query
@Query("SELECT u FROM User u JOIN FETCH u.orders")
List<User> findAllWithOrders();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q28: How do you implement Caching with Redis in Spring Boot?

**Difficulty**: Intermediate

**Strategy:**
Enable caching with `@EnableCaching`, configure Redis as the cache manager, and use `@Cacheable` on service methods.

**Code Example:**
```java
@Service
public class UserService {
    @Cacheable(value = "users", key = "#userId")
    public User getUser(String userId) {
        // Expensive DB call
        return userRepository.findById(userId).orElseThrow();
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q29: How do you implement a Circuit Breaker using Resilience4j?

**Difficulty**: Advanced

**Strategy:**
Use `@CircuitBreaker` annotation. It monitors failures and "opens" the circuit (stops requests) to prevent cascading failures, then periodically checks if the service is back.

**Code Example:**
```java
@CircuitBreaker(name = "inventoryService", fallbackMethod = "fallbackInventory")
public String getInventory(String productId) {
    return restTemplate.getForObject("/inventory/" + productId, String.class);
}

public String fallbackInventory(String productId, Throwable t) {
    return "Default Inventory";
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q30: How do you unit test a Spring Service with Mockito?

**Difficulty**: Intermediate

**Strategy:**
Use `@ExtendWith(MockitoExtension.class)` and `@InjectMocks` for the service under test, and `@Mock` for dependencies.

**Code Example:**
```java
@ExtendWith(MockitoExtension.class)
class UserServiceTest {
    @Mock UserRepository repo;
    @InjectMocks UserService service;

    @Test
    void testGetUser() {
        when(repo.findById(1L)).thenReturn(Optional.of(new User(1L, "John")));
        
        User user = service.getUser(1L);
        
        assertEquals("John", user.getName());
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q31: How do you handle global exceptions in Spring Boot?

**Difficulty**: Intermediate

**Strategy:**
Use `@ControllerAdvice` (or `@RestControllerAdvice`) with `@ExceptionHandler` methods to handle exceptions globally and return consistent error responses.

**Code Example:**
```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(UserNotFoundException.class)
    public ResponseEntity<String> handleNotFound(UserNotFoundException ex) {
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(ex.getMessage());
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q32: How do you create a Dockerfile for a Java application?

**Difficulty**: Intermediate

**Strategy:**
Use a multi-stage build to compile the code (Maven/Gradle) in the first stage and copy the JAR to a lightweight JRE image in the second stage.

**Code Example:**
```dockerfile
# Stage 1: Build
FROM maven:3.8-eclipse-temurin-17 AS build
COPY . /app
WORKDIR /app
RUN mvn clean package -DskipTests

# Stage 2: Run
FROM eclipse-temurin:17-jre
COPY --from=build /app/target/myapp.jar app.jar
ENTRYPOINT ["java", "-jar", "app.jar"]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q33: How do you implement an API Gateway pattern?

**Difficulty**: Advanced

**Strategy:**
Use **Spring Cloud Gateway**. It acts as a single entry point for microservices, handling routing, security, rate limiting, and monitoring.

**Code Example:**
```yaml
spring:
  cloud:
    gateway:
      routes:
        - id: user-service
          uri: lb://USER-SERVICE
          predicates:
            - Path=/users/**
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q34: How do you create a non-blocking REST API with Spring WebFlux?

**Difficulty**: Advanced

**Strategy:**
Use **Spring WebFlux** with `Mono` (0..1) and `Flux` (0..N) types. It uses Netty by default for high concurrency.

**Code Example:**
```java
@RestController
@RequestMapping("/reactive")
public class ReactiveController {

    @GetMapping("/stream")
    public Flux<String> streamData() {
        return Flux.interval(Duration.ofSeconds(1))
                   .map(i -> "Data chunk " + i);
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q35: How do you implement Health Checks in Spring Boot?

**Difficulty**: Beginner

**Strategy:**
Add `spring-boot-starter-actuator`. It exposes endpoints like `/actuator/health` to monitor application status, database connectivity, and disk space.

**Code Example:**
```properties
# application.properties
management.endpoints.web.exposure.include=health,info
management.endpoint.health.show-details=always
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q36: How do you ensure a specific execution order of beans?

**Difficulty**: Beginner

**Strategy:**
Use `@Order` annotation or implement `Ordered` interface. However, for dependency injection order, rely on `@DependsOn` (though explicit dependency injection is preferred).

**Code Example:**
```java
@Component
@Order(1)
public class FirstFilter implements Filter { ... }

@Component
@Order(2)
public class SecondFilter implements Filter { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q37: How do you handle configuration for multiple environments?

**Difficulty**: Beginner

**Strategy:**
Use **Spring Profiles**. Create separate properties files (`application-dev.properties`, `application-prod.properties`) and activate them using `spring.profiles.active`.

**Code Example:**
```bash
# Run with production profile
java -jar app.jar --spring.profiles.active=prod
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q38: How do you implement a Kafka Consumer with Spring Boot?

**Difficulty**: Intermediate

**Strategy:**
Use `@KafkaListener`. Configure the bootstrap servers and group ID in properties, then annotate a method to listen to a topic.

**Code Example:**
```java
@KafkaListener(topics = "orders", groupId = "order-group")
public void listen(String message) {
    System.out.println("Received Order: " + message);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q39: How do you secure passwords in Java?

**Difficulty**: Intermediate

**Strategy:**
Never store plain text. Use a strong hashing algorithm like **BCrypt** (provided by Spring Security) or **Argon2**.

**Code Example:**
```java
BCryptPasswordEncoder encoder = new BCryptPasswordEncoder();
String hashed = encoder.encode("mySecretPassword");

boolean matches = encoder.matches("mySecretPassword", hashed);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q40: How do you debug a deadlock in Java?

**Difficulty**: Advanced

**Strategy:**
Use `jstack` or **VisualVM** to take a thread dump. Look for threads stuck in `BLOCKED` state waiting for a lock held by another thread that is also waiting.

**Code Example:**
```bash
# Find PID
jps -l

# Take thread dump
jstack <PID> > dump.txt

# Look for "Found one Java-level deadlock" in dump.txt
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---

### Q41: How do you implement the Singleton pattern safely in Java?

**Difficulty**: Beginner

**Strategy:**
The best way to implement a Singleton in modern Java is using an **Enum**. It provides serialization machinery for free, prevents multiple instantiation (even with reflection), and is thread-safe.

**Code Example:**
```java
public enum Singleton {
    INSTANCE;

    public void doSomething() {
        System.out.println("Doing something...");
    }
}

// Usage
Singleton.INSTANCE.doSomething();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q42: How do you implement the Factory Pattern using Java 8+ features?

**Difficulty**: Intermediate

**Strategy:**
Instead of a switch-case or if-else block, use a `Map<String, Supplier<MyInterface>>` to register implementations. This makes the factory open for extension but closed for modification.

**Code Example:**
```java
public class ShapeFactory {
    private final Map<String, Supplier<Shape>> map = new HashMap<>();

    public ShapeFactory() {
        map.put("CIRCLE", Circle::new);
        map.put("SQUARE", Square::new);
    }

    public Shape create(String type) {
        return map.getOrDefault(type, () -> { 
            throw new IllegalArgumentException("Unknown shape"); 
        }).get();
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q43: How do you implement the Strategy Pattern with Lambdas?

**Difficulty**: Intermediate

**Strategy:**
You don't always need separate classes for strategies. You can use a Functional Interface and pass lambdas or method references.

**Code Example:**
```java
public class PaymentProcessor {
    private final Function<Integer, String> strategy;

    public PaymentProcessor(Function<Integer, String> strategy) {
        this.strategy = strategy;
    }

    public void process(int amount) {
        System.out.println(strategy.apply(amount));
    }
}

// Usage
new PaymentProcessor(amt -> "Paid $" + amt + " via Credit Card").process(100);
new PaymentProcessor(amt -> "Paid $" + amt + " via PayPal").process(200);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q44: How do you implement the Observer Pattern using Spring Events?

**Difficulty**: Intermediate

**Strategy:**
Spring provides a built-in event mechanism. Create an event class extending `ApplicationEvent` (or just a POJO), publish it using `ApplicationEventPublisher`, and listen using `@EventListener`.

**Code Example:**
```java
@Component
public class UserRegistrationService {
    @Autowired private ApplicationEventPublisher publisher;

    public void register(String email) {
        // Logic...
        publisher.publishEvent(new UserRegisteredEvent(email));
    }
}

@Component
public class EmailService {
    @EventListener
    public void sendWelcomeEmail(UserRegisteredEvent event) {
        System.out.println("Sending email to " + event.getEmail());
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q45: What is the difference between REQUIRED and REQUIRES_NEW transaction propagation?

**Difficulty**: Advanced

**Strategy:**
**REQUIRED** (default) joins an existing transaction or creates a new one if none exists. **REQUIRES_NEW** suspends the current transaction and creates a completely new, independent transaction. If the inner REQUIRES_NEW transaction fails, it rolls back, but the outer transaction can continue (if the exception is caught).

**Code Example:**
```java
@Transactional(propagation = Propagation.REQUIRED)
public void outer() {
    // Part of outer transaction
    innerService.inner();
    // If inner fails, outer is marked for rollback
}

@Transactional(propagation = Propagation.REQUIRES_NEW)
public void inner() {
    // Runs in a separate transaction
    // If this fails, it rolls back ONLY this part (if caught in outer)
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q46: How do you implement Optimistic Locking in JPA?

**Difficulty**: Intermediate

**Strategy:**
Add a `@Version` annotation to a field (usually Long or Integer) in your entity. JPA will check this version during updates. If the version in the DB is higher than the entity's version, an `OptimisticLockException` is thrown.

**Code Example:**
```java
@Entity
public class Product {
    @Id private Long id;
    
    @Version
    private Long version;
    
    private String name;
}

// When updating:
// UPDATE product SET name=?, version=2 WHERE id=? AND version=1

```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q47: How do you chain multiple asynchronous tasks using CompletableFuture?

**Difficulty**: Advanced

**Strategy:**
Use methods like `thenApply` (transform result), `thenCompose` (chain another Future), and `thenAccept` (consume result). Use `exceptionally` for error handling.

**Code Example:**
```java
CompletableFuture.supplyAsync(() -> "Hello")
    .thenApply(s -> s + " World")
    .thenCompose(s -> CompletableFuture.supplyAsync(() -> s.toUpperCase()))
    .thenAccept(System.out::println)
    .exceptionally(ex -> {
        System.err.println("Error: " + ex.getMessage());
        return null;
    });
// Output: HELLO WORLD
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q48: How do you write a Parameterized Test in JUnit 5?

**Difficulty**: Intermediate

**Strategy:**
Use `@ParameterizedTest` with a source like `@ValueSource`, `@CsvSource`, or `@MethodSource`. This allows running the same test logic with different inputs.

**Code Example:**
```java
@ParameterizedTest
@CsvSource({
    "1, 1, 2",
    "2, 3, 5",
    "10, 5, 15"
})
void testAddition(int a, int b, int expected) {
    assertEquals(expected, Calculator.add(a, b));
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q49: How do you use TestContainers for integration testing?

**Difficulty**: Advanced

**Strategy:**
TestContainers spins up real Docker containers (e.g., PostgreSQL, Redis) for tests. Use `@Container` and `@Testcontainers` (JUnit 5 support) or manually start/stop in setup/teardown.

**Code Example:**
```java
@Testcontainers
@SpringBootTest
class UserServiceIT {

    @Container
    static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:15");

    @DynamicPropertySource
    static void configureProperties(DynamicPropertyRegistry registry) {
        registry.add("spring.datasource.url", postgres::getJdbcUrl);
        registry.add("spring.datasource.username", postgres::getUsername);
        registry.add("spring.datasource.password", postgres::getPassword);
    }

    @Test
    void testDatabaseInteraction() {
        // Runs against real Postgres in Docker
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q50: How do you implement a simple Rate Limiter using Bucket4j?

**Difficulty**: Advanced

**Strategy:**
Create a `Bucket` with a `Bandwidth` (limit). In your controller or filter, call `bucket.tryConsume(1)`. If it returns false, reject the request.

**Code Example:**
```java
// Configuration
Bandwidth limit = Bandwidth.classic(10, Refill.greedy(10, Duration.ofMinutes(1)));
Bucket bucket = Bucket4j.builder().addLimit(limit).build();

// Usage in Controller
if (bucket.tryConsume(1)) {
    return ResponseEntity.ok("Request processed");
} else {
    return ResponseEntity.status(429).body("Too Many Requests");
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q51: How do you implement Distributed Locking with Redis (Redisson)?

**Difficulty**: Advanced

**Strategy:**
Use Redisson's `RLock`. It implements `java.util.concurrent.locks.Lock`. Always use `try-finally` to ensure the lock is released.

**Code Example:**
```java
@Autowired RedissonClient redisson;

public void criticalSection() {
    RLock lock = redisson.getLock("myLock");
    try {
        // Wait up to 10s, lock expires after 60s
        if (lock.tryLock(10, 60, TimeUnit.SECONDS)) {
            // Do critical work
        }
    } catch (InterruptedException e) {
        Thread.currentThread().interrupt();
    } finally {
        if (lock.isHeldByCurrentThread()) {
            lock.unlock();
        }
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q52: How do you handle JWT Authentication in Spring Security?

**Difficulty**: Advanced

**Strategy:**
Implement a `OncePerRequestFilter`. Extract the token from the `Authorization` header, validate it, create an `Authentication` object (e.g., `UsernamePasswordAuthenticationToken`), and set it in the `SecurityContextHolder`.

**Code Example:**
```java
protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain chain) {
    String token = extractToken(request);
    if (token != null && jwtUtils.validate(token)) {
        String user = jwtUtils.getUser(token);
        Authentication auth = new UsernamePasswordAuthenticationToken(user, null, Collections.emptyList());
        SecurityContextHolder.getContext().setAuthentication(auth);
    }
    chain.doFilter(request, response);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q53: How do you expose a custom metric in Spring Boot Actuator?

**Difficulty**: Intermediate

**Strategy:**
Inject `MeterRegistry` and use it to create counters, gauges, or timers. Counters are for monotonic increments; gauges are for values that go up and down.

**Code Example:**
```java
@Service
public class OrderService {
    private final Counter orderCounter;

    public OrderService(MeterRegistry registry) {
        this.orderCounter = registry.counter("orders.created");
    }

    public void createOrder() {
        // Logic
        orderCounter.increment();
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q54: What is the difference between @Mock and @Spy in Mockito?

**Difficulty**: Intermediate

**Strategy:**
**@Mock** creates a complete dummy object; real methods are NOT called unless stubbed. **@Spy** wraps a real object; real methods ARE called unless stubbed. Use Spy when you need partial mocking.

**Code Example:**
```java
@Mock
List<String> mockList; // mockList.add("a") does nothing

@Spy
List<String> spyList = new ArrayList<>(); // spyList.add("a") actually adds "a"

// Stubbing spy
doReturn("b").when(spyList).get(0); // partial mock
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q55: How do you solve the 'LazyInitializationException' in Hibernate?

**Difficulty**: Intermediate

**Strategy:**
This occurs when accessing a lazy-loaded collection after the session is closed. Solutions: 1) Use `JOIN FETCH` in the query (best). 2) Use `@Transactional` on the service method (extends session). 3) Use Entity Graphs. 4) DTO Projection.

**Code Example:**
```java
// Solution 1: Join Fetch
@Query("SELECT u FROM User u JOIN FETCH u.roles WHERE u.id = :id")
Optional<User> findByIdWithRoles(Long id);

// Solution 2: Transactional Service
@Service
public class UserService {
    @Transactional
    public User getUser(Long id) {
        User u = repo.findById(id).get();
        u.getRoles().size(); // Init collection while session open
        return u;
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q56: How do you implement a simple REST Client using RestClient (Spring Boot 3.2+)?

**Difficulty**: Intermediate

**Strategy:**
`RestClient` is the modern, fluent alternative to `RestTemplate`. It offers a functional API similar to `WebClient` but is synchronous.

**Code Example:**
```java
RestClient client = RestClient.create();

String result = client.get()
    .uri("https://api.example.com/users/{id}", 1)
    .retrieve()
    .body(String.class);

// Post example
User newUser = new User("Alice");
ResponseEntity<Void> response = client.post()
    .uri("https://api.example.com/users")
    .contentType(MediaType.APPLICATION_JSON)
    .body(newUser)
    .retrieve()
    .toBodilessEntity();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---

### Q57: How do you use 'var' (Local Variable Type Inference)?

**Difficulty**: Beginner

**Strategy:**
Use `var` to reduce boilerplate when the type is obvious from the right-hand side. It only works for local variables with an initializer.

**Code Example:**
```java
// Explicit type
Map<String, List<String>> map = new HashMap<>();

// Using var
var map = new HashMap<String, List<String>>();

// Loop
for (var entry : map.entrySet()) {
    System.out.println(entry.getKey());
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q58: What are Text Blocks and how do they simplify String handling?

**Difficulty**: Beginner

**Strategy:**
Text Blocks (introduced in Java 15) allow multi-line strings without explicit escape sequences for newlines or quotes. They start and end with `"""`.

**Code Example:**
```java
String json = """
              {
                  "name": "John",
                  "age": 30
              }
              """;
              
System.out.println(json);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q59: How do you use SequencedCollection in Java 21?

**Difficulty**: Intermediate

**Strategy:**
`SequencedCollection` provides a uniform API for collections with a defined encounter order (like List, Deque, SortedSet). It adds methods like `addFirst`, `addLast`, `getFirst`, `getLast`.

**Code Example:**
```java
SequencedCollection<String> list = new ArrayList<>();
list.add("B");
list.addFirst("A");
list.addLast("C");

System.out.println(list.getFirst()); // A
System.out.println(list.getLast());  // C
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q60: How does ConcurrentHashMap ensure thread safety without locking the entire map?

**Difficulty**: Advanced

**Strategy:**
`ConcurrentHashMap` uses a bucket-level locking mechanism (Node locking) using `synchronized` on the head node of the bucket and CAS (Compare-And-Swap) operations. It allows concurrent reads without locking and concurrent writes to different buckets.

**Code Example:**
```java
ConcurrentHashMap<String, Integer> map = new ConcurrentHashMap<>();

map.put("A", 1);
map.put("B", 2);

// Atomic update
map.compute("A", (k, v) -> v + 1);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q61: What is the difference between WeakReference and SoftReference?

**Difficulty**: Advanced

**Strategy:**
**WeakReference**: Objects are collected eagerly by GC as soon as they are weakly reachable. Useful for mapping keys (WeakHashMap). **SoftReference**: Objects are collected only when JVM is low on memory. Useful for implementing memory-sensitive caches.

**Code Example:**
```java
Object strong = new Object();
WeakReference<Object> weak = new WeakReference<>(strong);
SoftReference<Object> soft = new SoftReference<>(strong);

strong = null; 

// weak.get() might return null after next GC
// soft.get() will likely return the object unless memory is low
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q62: How do you use Spring Data JPA Projections to optimize read performance?

**Difficulty**: Intermediate

**Strategy:**
Use interface-based projections to fetch only the required columns instead of the entire entity. This reduces memory usage and database load.

**Code Example:**
```java
// Interface Projection
public interface UserSummary {
    String getUsername();
    String getEmail();
}

// Repository
public interface UserRepository extends JpaRepository<User, Long> {
    List<UserSummary> findByActiveTrue();
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q63: How do you implement a Dead Letter Queue (DLQ) in Kafka with Spring Boot?

**Difficulty**: Advanced

**Strategy:**
Configure a `DeadLetterPublishingRecoverer` with a `DefaultErrorHandler`. When a message processing fails repeatedly, it is sent to a DLQ topic (e.g., `original-topic.DLT`).

**Code Example:**
```java
@Bean
public CommonErrorHandler errorHandler(KafkaTemplate<Object, Object> template) {
    return new DefaultErrorHandler(
        new DeadLetterPublishingRecoverer(template),
        new FixedBackOff(1000L, 2) // Retry 2 times, 1s interval
    );
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q64: How do you use Feign Client for declarative REST communication?

**Difficulty**: Intermediate

**Strategy:**
Add `spring-cloud-starter-openfeign`, enable it with `@EnableFeignClients`, and define an interface annotated with `@FeignClient`.

**Code Example:**
```java
@FeignClient(name = "user-service", url = "https://api.example.com")
public interface UserClient {
    @GetMapping("/users/{id}")
    User getUser(@PathVariable("id") Long id);
}

// Usage
@Autowired UserClient userClient;
User u = userClient.getUser(1L);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q65: How do you configure L2 Cache in Hibernate?

**Difficulty**: Advanced

**Strategy:**
Enable L2 cache in properties (`hibernate.cache.use_second_level_cache=true`), choose a provider (e.g., Ehcache, Redis), and annotate entities with `@Cache`.

**Code Example:**
```java
@Entity
@Cacheable
@Cache(usage = CacheConcurrencyStrategy.READ_WRITE)
public class Product {
    @Id Long id;
    String name;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q66: How do you secure methods using @PreAuthorize in Spring Security?

**Difficulty**: Intermediate

**Strategy:**
Enable method security with `@EnableMethodSecurity` and use `@PreAuthorize` with SpEL expressions to restrict access based on roles or permissions.

**Code Example:**
```java
@Service
public class AdminService {
    
    @PreAuthorize("hasRole('ADMIN')")
    public void deleteUser(Long id) {
        // ...
    }
    
    @PreAuthorize("#username == authentication.name")
    public void updateProfile(String username) {
        // ...
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q67: How do you handle transactions programmatically (TransactionTemplate)?

**Difficulty**: Advanced

**Strategy:**
Use `TransactionTemplate` when you need fine-grained control over transaction boundaries (e.g., inside a loop or try-catch block) instead of `@Transactional`.

**Code Example:**
```java
@Autowired TransactionTemplate transactionTemplate;

public void process() {
    String result = transactionTemplate.execute(status -> {
        try {
            // DB operations
            return "Success";
        } catch (Exception e) {
            status.setRollbackOnly();
            return "Error";
        }
    });
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q68: How do you implement a custom validation annotation (Bean Validation)?

**Difficulty**: Intermediate

**Strategy:**
Create an annotation annotated with `@Constraint` and implement a `ConstraintValidator`.

**Code Example:**
```java
@Constraint(validatedBy = PasswordValidator.class)
@Target({ ElementType.FIELD })
@Retention(RetentionPolicy.RUNTIME)
public @interface ValidPassword {
    String message() default "Invalid password";
    Class<?>[] groups() default {};
    Class<? extends Payload>[] payload() default {};
}

public class PasswordValidator implements ConstraintValidator<ValidPassword, String> {
    public boolean isValid(String value, ConstraintValidatorContext context) {
        return value != null && value.length() > 8;
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q69: How do you use CompletableFuture.allOf to wait for multiple tasks?

**Difficulty**: Intermediate

**Strategy:**
Use `CompletableFuture.allOf(f1, f2, ...)` to return a new future that completes when all given futures complete. Then use `join()` to wait.

**Code Example:**
```java
CompletableFuture<String> f1 = CompletableFuture.supplyAsync(() -> "A");
CompletableFuture<String> f2 = CompletableFuture.supplyAsync(() -> "B");

CompletableFuture<Void> all = CompletableFuture.allOf(f1, f2);

all.thenRun(() -> {
    System.out.println("All done");
    // f1.join(), f2.join() are safe here
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q70: How do you profile a Java application using JFR (Java Flight Recorder)?

**Difficulty**: Advanced

**Strategy:**
Start the application with `-XX:StartFlightRecording` or use `jcmd` to start/dump recordings. Analyze the `.jfr` file using JDK Mission Control (JMC).

**Code Example:**
```bash
# Start recording for 60 seconds
jcmd <PID> JFR.start duration=60s filename=recording.jfr

# Analyze
# Open recording.jfr in Java Mission Control
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q71: How do you implement a retry mechanism with exponential backoff?

**Difficulty**: Intermediate

**Strategy:**
Use a loop with `Thread.sleep()` increasing exponentially, or better, use **Resilience4j Retry** module.

**Code Example:**
```java
@Retry(name = "backendA")
public String callService() {
    // ...
}

// resilience4j.retry.instances.backendA.waitDuration=1s
// resilience4j.retry.instances.backendA.enableExponentialBackoff=true
// resilience4j.retry.instances.backendA.exponentialBackoffMultiplier=2
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>
### Q72: How do you handle Java internationalization (i18n) in microservices?

**Difficulty**: Intermediate

**Strategy**:
Use i18n libraries. Extract strings to resource files.

**Code Example**:
```java
t('welcome_message')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q73: How do you ensure Java accessibility (a11y) in mobile devices?

**Difficulty**: Beginner

**Strategy**:
Use semantic HTML and ARIA roles. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```java
<button aria-label="Close">X</button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q74: How do you optimize Java network requests in legacy systems?

**Difficulty**: Advanced

**Strategy**:
Use batching, debouncing, or GraphQL. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```java
debounce(() => fetch(), 300);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q75: How do you handle Java performance optimization for cloud infrastructure?

**Difficulty**: Advanced

**Strategy**:
Profile first, then optimize hot paths. Use caching and efficient algorithms.

**Code Example**:
```java
const start = performance.now();
// Java logic
const end = performance.now();
console.log('Time:', end - start);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q76: What are the security implications of Java in real-time systems?

**Difficulty**: Intermediate

**Strategy**:
Validate all inputs. Sanitize data. Use least privilege principle.

**Code Example**:
```java
// Sanitize input
const clean = input.replace(/<script>/g, '');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q77: How do you debug Java memory leaks in distributed systems?

**Difficulty**: Advanced

**Strategy**:
Use heap snapshots and look for detached DOM nodes or uncleared listeners.

**Code Example**:
```java
// Check listeners
process.on('exit', () => cleanup());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q78: Best practices for Java code organization in high-traffic sites?

**Difficulty**: Beginner

**Strategy**:
Follow SOLID principles. Keep functions small and focused.

**Code Example**:
```java
// Single responsibility
function doOneThing() { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q79: How do you implement Java error handling for embedded systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```java
try {
  await JavaOperation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q80: How do you test Java functionality in production environments?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```java
test('Java works', () => {
  expect(Java()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q81: How do you handle Java state management in large scale applications?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```java
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q82: How do you perform Java data validation in microservices?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```java
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q83: How do you automate Java deployment for mobile devices?

**Difficulty**: Advanced

**Strategy**:
Use CI/CD pipelines. Dockerize the application. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```java
steps:
  - run: npm test
  - run: docker build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q84: How do you handle Java concurrency issues in legacy systems?

**Difficulty**: Advanced

**Strategy**:
Use locks, queues, or atomic operations. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```java
await mutex.runExclusive(async () => {
  // critical section
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q85: How do you implement Java caching in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Use Redis or in-memory LRU caches. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```java
const cache = new Map();
if (cache.has(key)) return cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q86: How do you manage Java configuration for real-time systems?

**Difficulty**: Beginner

**Strategy**:
Use environment variables or config files. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```java
const config = process.env.CONFIG || 'default';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q87: How do you handle Java internationalization (i18n) in distributed systems?

**Difficulty**: Intermediate

**Strategy**:
Use i18n libraries. Extract strings to resource files.

**Code Example**:
```java
t('welcome_message')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q88: How do you ensure Java accessibility (a11y) in high-traffic sites?

**Difficulty**: Beginner

**Strategy**:
Use semantic HTML and ARIA roles. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```java
<button aria-label="Close">X</button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q89: How do you optimize Java network requests in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use batching, debouncing, or GraphQL. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```java
debounce(() => fetch(), 300);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q90: How do you handle Java performance optimization for production environments?

**Difficulty**: Advanced

**Strategy**:
Profile first, then optimize hot paths. Use caching and efficient algorithms.

**Code Example**:
```java
const start = performance.now();
// Java logic
const end = performance.now();
console.log('Time:', end - start);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q91: What are the security implications of Java in large scale applications?

**Difficulty**: Intermediate

**Strategy**:
Validate all inputs. Sanitize data. Use least privilege principle.

**Code Example**:
```java
// Sanitize input
const clean = input.replace(/<script>/g, '');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q92: How do you debug Java memory leaks in microservices?

**Difficulty**: Advanced

**Strategy**:
Use heap snapshots and look for detached DOM nodes or uncleared listeners.

**Code Example**:
```java
// Check listeners
process.on('exit', () => cleanup());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q93: Best practices for Java code organization in mobile devices?

**Difficulty**: Beginner

**Strategy**:
Follow SOLID principles. Keep functions small and focused.

**Code Example**:
```java
// Single responsibility
function doOneThing() { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q94: How do you implement Java error handling for legacy systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```java
try {
  await JavaOperation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q95: How do you test Java functionality in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```java
test('Java works', () => {
  expect(Java()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q96: How do you handle Java state management in real-time systems?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```java
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q97: How do you perform Java data validation in distributed systems?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```java
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q98: How do you automate Java deployment for high-traffic sites?

**Difficulty**: Advanced

**Strategy**:
Use CI/CD pipelines. Dockerize the application. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```java
steps:
  - run: npm test
  - run: docker build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q99: How do you handle Java concurrency issues in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use locks, queues, or atomic operations. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```java
await mutex.runExclusive(async () => {
  // critical section
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q100: How do you implement Java caching in production environments?

**Difficulty**: Intermediate

**Strategy**:
Use Redis or in-memory LRU caches. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```java
const cache = new Map();
if (cache.has(key)) return cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---
