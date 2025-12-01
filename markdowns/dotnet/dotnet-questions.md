<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>.NET Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for developers</b></p>
</div>

---

## Table of Contents

2. [How do you prevent thread-pool starvation in a high-concurrency .NET application?](#q2-how-do-you-prevent-thread-pool-starvation-in-a-high-concurrency-.net-application) <span class="expert">Expert</span>
3. [How do you implement efficient caching with automatic expiration using `IMemoryCache`?](#q3-how-do-you-implement-efficient-caching-with-automatic-expiration-using-imemorycache) <span class="intermediate">Intermediate</span>
4. [How do you handle background tasks in ASP.NET Core without blocking the request thread?](#q4-how-do-you-handle-background-tasks-in-asp.net-core-without-blocking-the-request-thread) <span class="intermediate">Intermediate</span>
5. [How do you optimize Entity Framework Core queries to avoid the N+1 problem?](#q5-how-do-you-optimize-entity-framework-core-queries-to-avoid-the-n+1-problem) <span class="intermediate">Intermediate</span>
6. [How do you implement the Outbox Pattern in .NET to ensure reliable messaging?](#q6-how-do-you-implement-the-outbox-pattern-in-.net-to-ensure-reliable-messaging) <span class="expert">Expert</span>
7. [How do you use `IAsyncEnumerable<T>` to stream data efficiently from a database or API?](#q7-how-do-you-use-iasyncenumerable<t>-to-stream-data-efficiently-from-a-database-or-api) <span class="advanced">Advanced</span>
8. [How do you implement custom middleware in ASP.NET Core to handle global exceptions?](#q8-how-do-you-implement-custom-middleware-in-asp.net-core-to-handle-global-exceptions) <span class="intermediate">Intermediate</span>
9. [How do you use `ValueTask` to reduce allocations in hot paths?](#q9-how-do-you-use-valuetask-to-reduce-allocations-in-hot-paths) <span class="advanced">Advanced</span>
10. [How do you implement dependency injection for a service that requires a runtime parameter?](#q10-how-do-you-implement-dependency-injection-for-a-service-that-requires-a-runtime-parameter) <span class="advanced">Advanced</span>
11. [How do you cancel a long-running async operation properly?](#q11-how-do-you-cancel-a-long-running-async-operation-properly) <span class="intermediate">Intermediate</span>
12. [How do you optimize string concatenation in a tight loop?](#q12-how-do-you-optimize-string-concatenation-in-a-tight-loop) <span class="beginner">Beginner</span>
13. [How do you implement structured logging using Serilog in .NET Core?](#q13-how-do-you-implement-structured-logging-using-serilog-in-.net-core) <span class="intermediate">Intermediate</span>
14. [How do you ensure a singleton service is thread-safe?](#q14-how-do-you-ensure-a-singleton-service-is-thread-safe) <span class="intermediate">Intermediate</span>
15. [How do you handle database migrations in a CI/CD pipeline using EF Core?](#q15-how-do-you-handle-database-migrations-in-a-cicd-pipeline-using-ef-core) <span class="advanced">Advanced</span>
16. [How do you implement efficient caching with `IMemoryCache` and expiration policies?](#q16-how-do-you-implement-efficient-caching-with-imemorycache-and-expiration-policies) <span class="intermediate">Intermediate</span>
17. [How do you solve the 'N+1' problem in Entity Framework Core?](#q17-how-do-you-solve-the-n+1-problem-in-entity-framework-core) <span class="intermediate">Intermediate</span>
18. [How do you implement the Outbox Pattern for reliable messaging?](#q18-how-do-you-implement-the-outbox-pattern-for-reliable-messaging) <span class="advanced">Advanced</span>
19. [How do you use `IHttpClientFactory` to manage HTTP connections?](#q19-how-do-you-use-ihttpclientfactory-to-manage-http-connections) <span class="intermediate">Intermediate</span>
20. [How do you handle global exceptions in ASP.NET Core?](#q20-how-do-you-handle-global-exceptions-in-asp.net-core) <span class="intermediate">Intermediate</span>
21. [How do you implement a background service (Hosted Service)?](#q21-how-do-you-implement-a-background-service-hosted-service) <span class="intermediate">Intermediate</span>
22. [How do you use `ValueTask` to optimize hot paths?](#q22-how-do-you-use-valuetask-to-optimize-hot-paths) <span class="advanced">Advanced</span>
23. [How do you implement resilient HTTP calls with Polly?](#q23-how-do-you-implement-resilient-http-calls-with-polly) <span class="intermediate">Intermediate</span>
24. [How do you optimize LINQ queries with `AsNoTracking`?](#q24-how-do-you-optimize-linq-queries-with-asnotracking) <span class="intermediate">Intermediate</span>
25. [How do you use `IAsyncEnumerable` for streaming data?](#q25-how-do-you-use-iasyncenumerable-for-streaming-data) <span class="advanced">Advanced</span>
26. [How do you use Channels for Producer-Consumer patterns?](#q26-how-do-you-use-channels-for-producer-consumer-patterns) <span class="advanced">Advanced</span>
27. [How do you implement Structured Logging with Serilog?](#q27-how-do-you-implement-structured-logging-with-serilog) <span class="beginner">Beginner</span>
28. [How do you prevent Thread Pool starvation?](#q28-how-do-you-prevent-thread-pool-starvation) <span class="advanced">Advanced</span>
29. [How do you use `ArrayPool<T>` to reduce GC pressure?](#q29-how-do-you-use-arraypool<t>-to-reduce-gc-pressure) <span class="expert">Expert</span>
30. [How do you implement a custom attribute filter in ASP.NET Core?](#q30-how-do-you-implement-a-custom-attribute-filter-in-asp.net-core) <span class="intermediate">Intermediate</span>
31. [How do you use `ConcurrentDictionary` safely?](#q31-how-do-you-use-concurrentdictionary-safely) <span class="intermediate">Intermediate</span>
32. [How do you implement Dependency Injection for multiple implementations of an interface?](#q32-how-do-you-implement-dependency-injection-for-multiple-implementations-of-an-interface) <span class="intermediate">Intermediate</span>
33. [How do you use `stackalloc` for high-performance memory allocation?](#q33-how-do-you-use-stackalloc-for-high-performance-memory-allocation) <span class="expert">Expert</span>
34. [How do you secure an API using JWT Authentication?](#q34-how-do-you-secure-an-api-using-jwt-authentication) <span class="intermediate">Intermediate</span>
35. [How do you use `FrozenDictionary` (common in .NET 8)?](#q35-how-do-you-use-frozendictionary-common-in-.net-8) <span class="advanced">Advanced</span>
36. [How do you implement Health Checks in ASP.NET Core?](#q36-how-do-you-implement-health-checks-in-asp.net-core) <span class="beginner">Beginner</span>
37. [How do you use EF Core Interceptors?](#q37-how-do-you-use-ef-core-interceptors) <span class="advanced">Advanced</span>
38. [How do you implement Rate Limiting in .NET 7+?](#q38-how-do-you-implement-rate-limiting-in-.net-7+) <span class="intermediate">Intermediate</span>
39. [How do you use `BlockingCollection`?](#q39-how-do-you-use-blockingcollection) <span class="advanced">Advanced</span>
40. [How do you use `System.Text.Json` Source Generators?](#q40-how-do-you-use-system.text.json-source-generators) <span class="advanced">Advanced</span>
41. [How do you handle configuration with the Options Pattern?](#q41-how-do-you-handle-configuration-with-the-options-pattern) <span class="beginner">Beginner</span>
42. [How do you use `PeriodicTimer` (Net 6)?](#q42-how-do-you-use-periodictimer-net-6) <span class="intermediate">Intermediate</span>
43. [How do you implement a custom Tag Helper in ASP.NET Core?](#q43-how-do-you-implement-a-custom-tag-helper-in-asp.net-core) <span class="intermediate">Intermediate</span>
44. [How do you use `Interlocked` class for atomic operations?](#q44-how-do-you-use-interlocked-class-for-atomic-operations) <span class="advanced">Advanced</span>
45. [How do you use Records with `with` expressions?](#q45-how-do-you-use-records-with-with-expressions) <span class="beginner">Beginner</span>
46. [How do you implement API Versioning?](#q46-how-do-you-implement-api-versioning) <span class="intermediate">Intermediate</span>
47. [How do you use `simd` (Single Instruction, Multiple Data) in .NET?](#q47-how-do-you-use-simd-single-instruction-multiple-data-in-.net) <span class="expert">Expert</span>
48. [How do you use `CallerMemberName` attribute?](#q48-how-do-you-use-callermembername-attribute) <span class="beginner">Beginner</span>
49. [How do you use `Yield Return` for state machine generation?](#q49-how-do-you-use-yield-return-for-state-machine-generation) <span class="intermediate">Intermediate</span>
50. [How do you use `Unsafe` class for memory manipulation?](#q50-how-do-you-use-unsafe-class-for-memory-manipulation) <span class="expert">Expert</span>
51. [How do you handle .NET state management in large scale applications?](#q51-how-do-you-handle-.net-state-management-in-large-scale-applications) <span class="advanced">Advanced</span>
52. [How do you perform .NET data validation in microservices?](#q52-how-do-you-perform-.net-data-validation-in-microservices) <span class="beginner">Beginner</span>
53. [How do you automate .NET deployment for mobile devices?](#q53-how-do-you-automate-.net-deployment-for-mobile-devices) <span class="advanced">Advanced</span>
54. [How do you handle .NET concurrency issues in legacy systems?](#q54-how-do-you-handle-.net-concurrency-issues-in-legacy-systems) <span class="advanced">Advanced</span>
55. [How do you implement .NET caching in cloud infrastructure?](#q55-how-do-you-implement-.net-caching-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
56. [How do you manage .NET configuration for real-time systems?](#q56-how-do-you-manage-.net-configuration-for-real-time-systems) <span class="beginner">Beginner</span>
57. [How do you handle .NET internationalization (i18n) in distributed systems?](#q57-how-do-you-handle-.net-internationalization-i18n-in-distributed-systems) <span class="intermediate">Intermediate</span>
58. [How do you ensure .NET accessibility (a11y) in high-traffic sites?](#q58-how-do-you-ensure-.net-accessibility-a11y-in-high-traffic-sites) <span class="beginner">Beginner</span>
59. [How do you optimize .NET network requests in embedded systems?](#q59-how-do-you-optimize-.net-network-requests-in-embedded-systems) <span class="advanced">Advanced</span>
60. [How do you handle .NET performance optimization for production environments?](#q60-how-do-you-handle-.net-performance-optimization-for-production-environments) <span class="advanced">Advanced</span>
61. [What are the security implications of .NET in large scale applications?](#q61-what-are-the-security-implications-of-.net-in-large-scale-applications) <span class="intermediate">Intermediate</span>
62. [How do you debug .NET memory leaks in microservices?](#q62-how-do-you-debug-.net-memory-leaks-in-microservices) <span class="advanced">Advanced</span>
63. [Best practices for .NET code organization in mobile devices?](#q63-best-practices-for-.net-code-organization-in-mobile-devices) <span class="beginner">Beginner</span>
64. [How do you implement .NET error handling for legacy systems?](#q64-how-do-you-implement-.net-error-handling-for-legacy-systems) <span class="intermediate">Intermediate</span>
65. [How do you test .NET functionality in cloud infrastructure?](#q65-how-do-you-test-.net-functionality-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
66. [How do you handle .NET state management in real-time systems?](#q66-how-do-you-handle-.net-state-management-in-real-time-systems) <span class="advanced">Advanced</span>
67. [How do you perform .NET data validation in distributed systems?](#q67-how-do-you-perform-.net-data-validation-in-distributed-systems) <span class="beginner">Beginner</span>
68. [How do you automate .NET deployment for high-traffic sites?](#q68-how-do-you-automate-.net-deployment-for-high-traffic-sites) <span class="advanced">Advanced</span>
69. [How do you handle .NET concurrency issues in embedded systems?](#q69-how-do-you-handle-.net-concurrency-issues-in-embedded-systems) <span class="advanced">Advanced</span>
70. [How do you implement .NET caching in production environments?](#q70-how-do-you-implement-.net-caching-in-production-environments) <span class="intermediate">Intermediate</span>
71. [How do you manage .NET configuration for large scale applications?](#q71-how-do-you-manage-.net-configuration-for-large-scale-applications) <span class="beginner">Beginner</span>
72. [How do you handle .NET internationalization (i18n) in microservices?](#q72-how-do-you-handle-.net-internationalization-i18n-in-microservices) <span class="intermediate">Intermediate</span>
73. [How do you ensure .NET accessibility (a11y) in mobile devices?](#q73-how-do-you-ensure-.net-accessibility-a11y-in-mobile-devices) <span class="beginner">Beginner</span>
74. [How do you optimize .NET network requests in legacy systems?](#q74-how-do-you-optimize-.net-network-requests-in-legacy-systems) <span class="advanced">Advanced</span>
75. [How do you handle .NET performance optimization for cloud infrastructure?](#q75-how-do-you-handle-.net-performance-optimization-for-cloud-infrastructure) <span class="advanced">Advanced</span>
76. [What are the security implications of .NET in real-time systems?](#q76-what-are-the-security-implications-of-.net-in-real-time-systems) <span class="intermediate">Intermediate</span>
77. [How do you debug .NET memory leaks in distributed systems?](#q77-how-do-you-debug-.net-memory-leaks-in-distributed-systems) <span class="advanced">Advanced</span>
78. [Best practices for .NET code organization in high-traffic sites?](#q78-best-practices-for-.net-code-organization-in-high-traffic-sites) <span class="beginner">Beginner</span>
79. [How do you implement .NET error handling for embedded systems?](#q79-how-do-you-implement-.net-error-handling-for-embedded-systems) <span class="intermediate">Intermediate</span>
80. [How do you test .NET functionality in production environments?](#q80-how-do-you-test-.net-functionality-in-production-environments) <span class="intermediate">Intermediate</span>
81. [How do you handle .NET state management in large scale applications?](#q81-how-do-you-handle-.net-state-management-in-large-scale-applications) <span class="advanced">Advanced</span>
82. [How do you perform .NET data validation in microservices?](#q82-how-do-you-perform-.net-data-validation-in-microservices) <span class="beginner">Beginner</span>
83. [How do you automate .NET deployment for mobile devices?](#q83-how-do-you-automate-.net-deployment-for-mobile-devices) <span class="advanced">Advanced</span>
84. [How do you handle .NET concurrency issues in legacy systems?](#q84-how-do-you-handle-.net-concurrency-issues-in-legacy-systems) <span class="advanced">Advanced</span>
85. [How do you implement .NET caching in cloud infrastructure?](#q85-how-do-you-implement-.net-caching-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
86. [How do you manage .NET configuration for real-time systems?](#q86-how-do-you-manage-.net-configuration-for-real-time-systems) <span class="beginner">Beginner</span>
87. [How do you handle .NET internationalization (i18n) in distributed systems?](#q87-how-do-you-handle-.net-internationalization-i18n-in-distributed-systems) <span class="intermediate">Intermediate</span>
88. [How do you ensure .NET accessibility (a11y) in high-traffic sites?](#q88-how-do-you-ensure-.net-accessibility-a11y-in-high-traffic-sites) <span class="beginner">Beginner</span>
89. [How do you optimize .NET network requests in embedded systems?](#q89-how-do-you-optimize-.net-network-requests-in-embedded-systems) <span class="advanced">Advanced</span>
90. [How do you handle .NET performance optimization for production environments?](#q90-how-do-you-handle-.net-performance-optimization-for-production-environments) <span class="advanced">Advanced</span>
91. [What are the security implications of .NET in large scale applications?](#q91-what-are-the-security-implications-of-.net-in-large-scale-applications) <span class="intermediate">Intermediate</span>
92. [How do you debug .NET memory leaks in microservices?](#q92-how-do-you-debug-.net-memory-leaks-in-microservices) <span class="advanced">Advanced</span>
93. [Best practices for .NET code organization in mobile devices?](#q93-best-practices-for-.net-code-organization-in-mobile-devices) <span class="beginner">Beginner</span>
94. [How do you implement .NET error handling for legacy systems?](#q94-how-do-you-implement-.net-error-handling-for-legacy-systems) <span class="intermediate">Intermediate</span>
95. [How do you test .NET functionality in cloud infrastructure?](#q95-how-do-you-test-.net-functionality-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
96. [How do you handle .NET state management in real-time systems?](#q96-how-do-you-handle-.net-state-management-in-real-time-systems) <span class="advanced">Advanced</span>
97. [How do you perform .NET data validation in distributed systems?](#q97-how-do-you-perform-.net-data-validation-in-distributed-systems) <span class="beginner">Beginner</span>
98. [How do you automate .NET deployment for high-traffic sites?](#q98-how-do-you-automate-.net-deployment-for-high-traffic-sites) <span class="advanced">Advanced</span>
99. [How do you handle .NET concurrency issues in embedded systems?](#q99-how-do-you-handle-.net-concurrency-issues-in-embedded-systems) <span class="advanced">Advanced</span>
100. [How do you implement .NET caching in production environments?](#q100-how-do-you-implement-.net-caching-in-production-environments) <span class="intermediate">Intermediate</span>

---

<a id="q2"></a>
### Q2: How do you prevent thread-pool starvation in a high-concurrency .NET application?

**Difficulty**: Expert

**Strategy**:

**Strategy:**
1.  **Avoid blocking calls:** Never use `.Wait()` or `.Result` on Tasks. Always use `await`.
2.  **Sync over Async:** Avoid wrapping async calls in synchronous wrappers.
3.  **Thread Injection:** The thread pool injects threads slowly (1-2 per second). Large bursts of blocking work will stall the app.

**Code Example (Bad vs Good):**
```csharp
// BAD: Blocks thread pool thread
public string GetData()
{
    return _service.GetDataAsync().Result; 
}

// GOOD: Frees thread while waiting
public async Task<string> GetDataAsync()
{
    return await _service.GetDataAsync();
}
```

---

<a id="q3"></a>
### Q3: How do you implement efficient caching with automatic expiration using `IMemoryCache`?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Inject `IMemoryCache` and use `GetOrCreateAsync` with `MemoryCacheEntryOptions` for sliding or absolute expiration.

**Code Example:**
```csharp
public async Task<User> GetUserAsync(int id)
{
    return await _cache.GetOrCreateAsync($"user_{id}", async entry =>
    {
        entry.SlidingExpiration = TimeSpan.FromMinutes(5);
        entry.AbsoluteExpirationRelativeToNow = TimeSpan.FromHours(1);
        return await _db.Users.FindAsync(id);
    });
}
```

---

<a id="q4"></a>
### Q4: How do you handle background tasks in ASP.NET Core without blocking the request thread?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Use `IHostedService` or `BackgroundService`. For fire-and-forget tasks from a request, channel them to a background worker or use a library like Hangfire/Quartz. Do NOT just use `Task.Run` without tracking, as it may be killed on app shutdown.

**Code Example:**
```csharp
public class Worker : BackgroundService
{
    protected override async Task ExecuteAsync(CancellationToken stoppingToken)
    {
        while (!stoppingToken.IsCancellationRequested)
        {
            // Do work
            await Task.Delay(1000, stoppingToken);
        }
    }
}
```

---

<a id="q5"></a>
### Q5: How do you optimize Entity Framework Core queries to avoid the N+1 problem?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Use Eager Loading (`.Include()`) or Projection (`.Select()`) to fetch related data in a single query.

**Code Example:**
```csharp
// BAD: Triggers 1 query for users + N queries for orders
var users = context.Users.ToList();
foreach(var user in users) { ... user.Orders ... }

// GOOD: 1 Query with Join
var users = context.Users.Include(u => u.Orders).ToList();

// BETTER: Select only what you need
var dtos = context.Users.Select(u => new UserDto { 
    Name = u.Name, 
    OrderCount = u.Orders.Count 
}).ToList();
```

---

<a id="q6"></a>
### Q6: How do you implement the Outbox Pattern in .NET to ensure reliable messaging?

**Difficulty**: Expert

**Strategy**:

**Strategy:**
1.  Start a database transaction.
2.  Save the business entity (e.g., Order).
3.  Save the event (e.g., OrderCreated) to an "Outbox" table in the same transaction.
4.  Commit transaction.
5.  A background worker polls the Outbox table and publishes events to the message broker (RabbitMQ/Azure Service Bus).

**Code Example (Concept):**
```csharp
using (var transaction = _context.Database.BeginTransaction())
{
    _context.Orders.Add(order);
    _context.OutboxMessages.Add(new OutboxMessage { Type = "OrderCreated", Data = json });
    await _context.SaveChangesAsync();
    await transaction.CommitAsync();
}
```

---

<a id="q7"></a>
### Q7: How do you use `IAsyncEnumerable<T>` to stream data efficiently from a database or API?

**Difficulty**: Advanced

**Strategy**:

**Strategy:**
Return `IAsyncEnumerable<T>` from your method and use `await foreach` to consume it. This allows processing items as they arrive rather than buffering the whole list.

**Code Example:**
```csharp
public async IAsyncEnumerable<int> GetDataAsync()
{
    for (int i = 0; i < 100; i++)
    {
        await Task.Delay(10); // Simulate IO
        yield return i;
    }
}

// Usage
await foreach (var item in GetDataAsync())
{
    Process(item);
}
```

---

<a id="q8"></a>
### Q8: How do you implement custom middleware in ASP.NET Core to handle global exceptions?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Create a middleware class with `InvokeAsync`. Wrap the `next(context)` call in a try-catch block.

**Code Example:**
```csharp
public class ExceptionMiddleware
{
    private readonly RequestDelegate _next;

    public ExceptionMiddleware(RequestDelegate next) { _next = next; }

    public async Task InvokeAsync(HttpContext context)
    {
        try
        {
            await _next(context);
        }
        catch (Exception ex)
        {
            context.Response.StatusCode = 500;
            await context.Response.WriteAsJsonAsync(new { Error = ex.Message });
        }
    }
}
```

---

<a id="q9"></a>
### Q9: How do you use `ValueTask` to reduce allocations in hot paths?

**Difficulty**: Advanced

**Strategy**:

**Strategy:**
Use `ValueTask<T>` when the result is often available synchronously (e.g., cached). This avoids allocating a `Task` object on the heap for the synchronous case.

**Code Example:**
```csharp
public ValueTask<int> GetCountAsync()
{
    if (_cache.TryGetValue("count", out int count))
    {
        return new ValueTask<int>(count); // No allocation
    }
    return new ValueTask<int>(FetchFromDbAsync()); // Wraps Task
}
```

---

<a id="q10"></a>
### Q10: How do you implement dependency injection for a service that requires a runtime parameter?

**Difficulty**: Advanced

**Strategy**:

**Strategy:**
Use a Factory Delegate or `ActivatorUtilities`. Register a `Func<TParam, TService>`.

**Code Example:**
```csharp
// Registration
services.AddTransient<Func<string, MyService>>(provider => 
    key => new MyService(key, provider.GetRequiredService<ILogger<MyService>>()));

// Usage
public class Consumer
{
    public Consumer(Func<string, MyService> serviceFactory)
    {
        var service = serviceFactory("runtime_key");
    }
}
```

---

<a id="q11"></a>
### Q11: How do you cancel a long-running async operation properly?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Pass a `CancellationToken` down the call stack and check `token.ThrowIfCancellationRequested()` or pass it to async APIs (EF Core, HttpClient).

**Code Example:**
```csharp
public async Task DoWorkAsync(CancellationToken token)
{
    foreach (var item in items)
    {
        token.ThrowIfCancellationRequested(); // Check loop
        await _client.GetAsync(url, token);   // Pass to IO
    }
}
```

---

<a id="q12"></a>
### Q12: How do you optimize string concatenation in a tight loop?

**Difficulty**: Beginner

**Strategy**:

**Strategy:**
Use `StringBuilder` (mutable) instead of `string` (immutable) to avoid creating N temporary string objects. For very high performance, use `Span<char>` or `ValueStringBuilder`.

**Code Example:**
```csharp
var sb = new StringBuilder();
for (int i = 0; i < 1000; i++)
{
    sb.Append("Item ");
    sb.Append(i);
}
var result = sb.ToString();
```

---

<a id="q13"></a>
### Q13: How do you implement structured logging using Serilog in .NET Core?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Configure Serilog as the logging provider. Use message templates (braces) to capture properties, not string interpolation.

**Code Example:**
```csharp
// Bad: String interpolation loses structure
_logger.LogInformation($"User {userId} logged in");

// Good: Structured logging
_logger.LogInformation("User {UserId} logged in", userId);
// In the log system (Seq/ELK), you can query: UserId == 123
```

---

<a id="q14"></a>
### Q14: How do you ensure a singleton service is thread-safe?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Use `ConcurrentDictionary`, `Interlocked`, or `lock` statements for mutable state. Immutable state is inherently thread-safe.

**Code Example:**
```csharp
public class CounterService
{
    private int _count;
    
    public int Increment()
    {
        return Interlocked.Increment(ref _count); // Atomic operation
    }
}
```

---

<a id="q15"></a>
### Q15: How do you handle database migrations in a CI/CD pipeline using EF Core?

**Difficulty**: Advanced

**Strategy**:

**Strategy:**
Generate an SQL script using `dotnet ef migrations script --idempotent` and execute it against the database during the deployment phase. Avoid running `context.Database.Migrate()` at app startup in production (concurrency issues).

**Command:**
```bash
dotnet ef migrations script --output deploy.sql --idempotent
```


---

<a id="q16"></a>
### Q16: How do you implement efficient caching with `IMemoryCache` and expiration policies?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Use `IMemoryCache` with `MemoryCacheEntryOptions`. Set `AbsoluteExpiration` (hard expiry) and `SlidingExpiration` (extend if accessed) to manage memory usage effectively.

**Code Example:**
```csharp
public class CacheService
{
    private readonly IMemoryCache _cache;

    public CacheService(IMemoryCache cache)
    {
        _cache = cache;
    }

    public async Task<string> GetValueAsync(string key)
    {
        return await _cache.GetOrCreateAsync(key, entry =>
        {
            entry.AbsoluteExpirationRelativeToNow = TimeSpan.FromMinutes(5);
            entry.SlidingExpiration = TimeSpan.FromMinutes(2);
            return FetchFromDbAsync(key);
        });
    }

    private Task<string> FetchFromDbAsync(string key) => Task.FromResult("value");
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q17"></a>
### Q17: How do you solve the 'N+1' problem in Entity Framework Core?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
The N+1 problem occurs when related data is loaded in a loop. Use `.Include()` for eager loading or `.Select()` for projection to fetch all required data in a single query.

**Code Example:**
```csharp
// BAD: Triggers 1 query for Users + N queries for Orders
var users = context.Users.ToList();
foreach (var user in users)
{
    var orders = user.Orders.ToList();
}

// GOOD: Eager loading (1 query with JOIN)
var usersWithOrders = context.Users
    .Include(u => u.Orders)
    .ToList();

// BEST: Projection (Select only what you need)
var dtos = context.Users
    .Select(u => new UserDto 
    { 
        Name = u.Name, 
        OrderCount = u.Orders.Count 
    })
    .ToList();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q18"></a>
### Q18: How do you implement the Outbox Pattern for reliable messaging?

**Difficulty**: Advanced

**Strategy**:

**Strategy:**
Save the message to a database table ('Outbox') in the same transaction as the business data. A background worker then reads the Outbox and publishes to the message bus, ensuring atomicity.

**Code Example:**
```csharp
using var transaction = _dbContext.Database.BeginTransaction();

// 1. Save Business Entity
_dbContext.Orders.Add(newOrder);

// 2. Save Message to Outbox
_dbContext.OutboxMessages.Add(new OutboxMessage
{
    Id = Guid.NewGuid(),
    Payload = JsonSerializer.Serialize(newOrder),
    Topic = "orders.created",
    CreatedAt = DateTime.UtcNow
});

await _dbContext.SaveChangesAsync();
await transaction.CommitAsync();

// Background worker will pick up OutboxMessages later...
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q19"></a>
### Q19: How do you use `IHttpClientFactory` to manage HTTP connections?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
`IHttpClientFactory` manages the lifetime of `HttpMessageHandler` to prevent socket exhaustion and DNS staleness. Use Named or Typed clients for better organization.

**Code Example:**
```csharp
// Program.cs registration
builder.Services.AddHttpClient<GitHubClient>(client =>
{
    client.BaseAddress = new Uri("https://api.github.com/");
    client.DefaultRequestHeaders.Add("User-Agent", "MyApp");
});

// Typed Client Usage
public class GitHubClient
{
    private readonly HttpClient _client;

    public GitHubClient(HttpClient client)
    {
        _client = client;
    }

    public async Task<string> GetRepoAsync()
    {
        return await _client.GetStringAsync("repos/dotnet/runtime");
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q20"></a>
### Q20: How do you handle global exceptions in ASP.NET Core?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Use the `UseExceptionHandler` middleware. It captures unhandled exceptions and allows you to return a standard error response (e.g., RFC 7807 Problem Details).

**Code Example:**
```csharp
var app = builder.Build();

if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler(errorApp =>
    {
        errorApp.Run(async context =>
        {
            var exception = context.Features.Get<IExceptionHandlerFeature>()?.Error;
            context.Response.StatusCode = 500;
            context.Response.ContentType = "application/json";
            
            await context.Response.WriteAsJsonAsync(new 
            { 
                Error = "Internal Server Error", 
                Detail = exception?.Message 
            });
        });
    });
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q21"></a>
### Q21: How do you implement a background service (Hosted Service)?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Inherit from `BackgroundService` and override `ExecuteAsync`. Register it using `AddHostedService`. It runs as a long-running task for the application lifetime.

**Code Example:**
```csharp
public class EmailWorker : BackgroundService
{
    private readonly ILogger<EmailWorker> _logger;

    public EmailWorker(ILogger<EmailWorker> logger)
    {
        _logger = logger;
    }

    protected override async Task ExecuteAsync(CancellationToken stoppingToken)
    {
        while (!stoppingToken.IsCancellationRequested)
        {
            _logger.LogInformation("Processing emails...");
            await Task.Delay(1000, stoppingToken);
        }
    }
}

// Registration
// builder.Services.AddHostedService<EmailWorker>();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q22"></a>
### Q22: How do you use `ValueTask` to optimize hot paths?

**Difficulty**: Advanced

**Strategy**:

**Strategy:**
Use `ValueTask<T>` when the result is often available synchronously (e.g., cached). This avoids allocating a `Task` object on the heap for every call.

**Code Example:**
```csharp
public ValueTask<int> GetCountAsync()
{
    if (_cachedCount.HasValue)
    {
        // No allocation
        return new ValueTask<int>(_cachedCount.Value);
    }

    // Allocation only when async I/O is needed
    return new ValueTask<int>(FetchCountFromDbAsync());
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q23"></a>
### Q23: How do you implement resilient HTTP calls with Polly?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Use Polly to define policies like Retry, Circuit Breaker, and Timeout. Integrate with `IHttpClientFactory` for seamless application.

**Code Example:**
```csharp
var retryPolicy = HttpPolicyExtensions
    .HandleTransientHttpError()
    .WaitAndRetryAsync(3, retryAttempt => TimeSpan.FromSeconds(Math.Pow(2, retryAttempt)));

builder.Services.AddHttpClient("ResilientClient")
    .AddPolicyHandler(retryPolicy);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q24"></a>
### Q24: How do you optimize LINQ queries with `AsNoTracking`?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
For read-only queries, use `.AsNoTracking()`. This tells EF Core not to track changes to the entities, significantly reducing memory usage and CPU overhead.

**Code Example:**
```csharp
public async Task<List<Product>> GetProductsAsync()
{
    // Faster, less memory
    return await _context.Products
        .AsNoTracking()
        .Where(p => p.Price > 100)
        .ToListAsync();
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q25"></a>
### Q25: How do you use `IAsyncEnumerable` for streaming data?

**Difficulty**: Advanced

**Strategy**:

**Strategy:**
`IAsyncEnumerable<T>` (C# 8) allows streaming data asynchronously as it becomes available, rather than buffering the entire collection in memory.

**Code Example:**
```csharp
public async IAsyncEnumerable<int> GetNumbersAsync()
{
    for (int i = 0; i < 10; i++)
    {
        await Task.Delay(100); // Simulate work
        yield return i;
    }
}

// Usage
await foreach (var num in GetNumbersAsync())
{
    Console.WriteLine(num);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q26"></a>
### Q26: How do you use Channels for Producer-Consumer patterns?

**Difficulty**: Advanced

**Strategy**:

**Strategy:**
`System.Threading.Channels` provides a high-performance, thread-safe queue for passing data between producers and consumers asynchronously.

**Code Example:**
```csharp
var channel = Channel.CreateBounded<string>(100);

// Producer
_ = Task.Run(async () =>
{
    await channel.Writer.WriteAsync("Message 1");
    channel.Writer.Complete();
});

// Consumer
await foreach (var msg in channel.Reader.ReadAllAsync())
{
    Console.WriteLine(msg);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q27"></a>
### Q27: How do you implement Structured Logging with Serilog?

**Difficulty**: Beginner

**Strategy**:

**Strategy:**
Structured logging preserves message parameters as data fields rather than just text. Serilog enables this, making logs queryable in tools like Seq or ELK.

**Code Example:**
```csharp
Log.Logger = new LoggerConfiguration()
    .WriteTo.Console()
    .CreateLogger();

var user = new { Id = 123, Name = "Alice" };

// "User" is stored as a structured object, not just a string
Log.Information("Processed login for {@User}", user);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q28"></a>
### Q28: How do you prevent Thread Pool starvation?

**Difficulty**: Advanced

**Strategy**:

**Strategy:**
Avoid blocking calls like `.Result` or `.Wait()` on async tasks ('Sync over Async'). This consumes Thread Pool threads while waiting, leading to starvation. Always use `await`.

**Code Example:**
```csharp
// BAD: Blocks a thread
public string GetData()
{
    return GetDataAsync().Result; 
}

// GOOD: Yields the thread
public async Task<string> GetDataWrapperAsync()
{
    return await GetDataAsync();
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q29"></a>
### Q29: How do you use `ArrayPool<T>` to reduce GC pressure?

**Difficulty**: Expert

**Strategy**:

**Strategy:**
`ArrayPool<T>.Shared` allows reusing arrays instead of allocating and discarding them, which reduces garbage collection overhead in high-throughput apps.

**Code Example:**
```csharp
var pool = ArrayPool<int>.Shared;
int[] buffer = pool.Rent(1024); // Request array of at least 1024

try
{
    // Use buffer...
    buffer[0] = 42;
}
finally
{
    pool.Return(buffer); // Return to pool
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q30"></a>
### Q30: How do you implement a custom attribute filter in ASP.NET Core?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Create a class inheriting from `Attribute` and `IActionFilter`. This allows you to run logic before or after a controller action executes.

**Code Example:**
```csharp
public class LogAttribute : ActionFilterAttribute
{
    public override void OnActionExecuting(ActionExecutingContext context)
    {
        Console.WriteLine($"Executing: {context.ActionDescriptor.DisplayName}");
        base.OnActionExecuting(context);
    }
}

[Log]
[HttpGet]
public IActionResult Get() => Ok();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q31"></a>
### Q31: How do you use `ConcurrentDictionary` safely?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
`ConcurrentDictionary` is thread-safe. Use methods like `GetOrAdd` or `AddOrUpdate` to ensure atomic operations without manual locking.

**Code Example:**
```csharp
var cache = new ConcurrentDictionary<string, int>();

// Atomic check and add
int value = cache.GetOrAdd("key", k => 
{
    return k.Length; // Only executed if key doesn't exist
});

// Atomic update
cache.AddOrUpdate("key", 1, (k, oldVal) => oldVal + 1);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q32"></a>
### Q32: How do you implement Dependency Injection for multiple implementations of an interface?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Register all implementations. Inject `IEnumerable<IInterface>` to get all, or use a delegate/factory to select a specific one based on runtime criteria.

**Code Example:**
```csharp
// Registration
services.AddTransient<INotification, EmailService>();
services.AddTransient<INotification, SmsService>();

// Usage
public class Notifier
{
    private readonly IEnumerable<INotification> _services;

    public Notifier(IEnumerable<INotification> services)
    {
        _services = services;
    }

    public void NotifyAll()
    {
        foreach (var service in _services) service.Send();
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q33"></a>
### Q33: How do you use `stackalloc` for high-performance memory allocation?

**Difficulty**: Expert

**Strategy**:

**Strategy:**
`stackalloc` allocates memory on the stack instead of the heap. Combined with `Span<T>`, it provides safe, high-speed buffer manipulation without GC pressure.

**Code Example:**
```csharp
public void ProcessBytes()
{
    // Allocate 100 bytes on stack (fast, no GC)
    Span<byte> buffer = stackalloc byte[100];
    
    for (int i = 0; i < buffer.Length; i++)
    {
        buffer[i] = (byte)i;
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q34"></a>
### Q34: How do you secure an API using JWT Authentication?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Configure `JwtBearer` authentication. Validate the token's signature, issuer, and audience. Use `[Authorize]` attribute to protect endpoints.

**Code Example:**
```csharp
builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddJwtBearer(options =>
    {
        options.TokenValidationParameters = new TokenValidationParameters
        {
            ValidateIssuer = true,
            ValidateAudience = true,
            ValidateLifetime = true,
            ValidateIssuerSigningKey = true,
            ValidIssuer = "my-app",
            ValidAudience = "my-app",
            IssuerSigningKey = new SymmetricSecurityKey(key)
        };
    });

app.UseAuthentication();
app.UseAuthorization();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q35"></a>
### Q35: How do you use `FrozenDictionary` (common in .NET 8)?

**Difficulty**: Advanced

**Strategy**:

**Strategy:**
`FrozenDictionary` (from `System.Collections.Frozen`) is optimized for read-heavy scenarios where the collection is immutable after creation. It offers faster lookups than standard Dictionary.

**Code Example:**
```csharp
var config = new Dictionary<string, string>
{
    ["env"] = "prod",
    ["version"] = "1.0"
}.ToFrozenDictionary(); // Immutable and optimized

string val = config["env"];
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q36"></a>
### Q36: How do you implement Health Checks in ASP.NET Core?

**Difficulty**: Beginner

**Strategy**:

**Strategy:**
Use `AddHealthChecks()` and `MapHealthChecks()`. You can add custom checks for database, cache, or external services.

**Code Example:**
```csharp
builder.Services.AddHealthChecks()
    .AddCheck("Database", () => 
        IsDbConnected() ? HealthCheckResult.Healthy() : HealthCheckResult.Unhealthy());

app.MapHealthChecks("/health");

// Helper
bool IsDbConnected() => true;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q37"></a>
### Q37: How do you use EF Core Interceptors?

**Difficulty**: Advanced

**Strategy**:

**Strategy:**
Interceptors allow you to hook into EF Core operations (like `SaveChanges` or query execution) to modify behavior, log, or audit changes globally.

**Code Example:**
```csharp
public class AuditInterceptor : SaveChangesInterceptor
{
    public override InterceptionResult<int> SavingChanges(
        DbContextEventData eventData, 
        InterceptionResult<int> result)
    {
        Console.WriteLine("Saving changes...");
        return base.SavingChanges(eventData, result);
    }
}

// Register
optionsBuilder.AddInterceptors(new AuditInterceptor());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q38"></a>
### Q38: How do you implement Rate Limiting in .NET 7+?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Use the built-in `RateLimiter` middleware. You can define policies like Fixed Window, Sliding Window, or Token Bucket.

**Code Example:**
```csharp
builder.Services.AddRateLimiter(options =>
{
    options.GlobalLimiter = PartitionedRateLimiter.Create<HttpContext, string>(context =>
        RateLimitPartition.GetFixedWindowLimiter(
            partitionKey: context.User.Identity?.Name ?? "anonymous",
            factory: partition => new FixedWindowRateLimiterOptions
            {
                PermitLimit = 10,
                Window = TimeSpan.FromSeconds(10)
            }));
});

app.UseRateLimiter();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q39"></a>
### Q39: How do you use `BlockingCollection`?

**Difficulty**: Advanced

**Strategy**:

**Strategy:**
`BlockingCollection<T>` wraps a thread-safe collection and provides blocking capabilities. It's ideal for implementing bounded producer-consumer queues.

**Code Example:**
```csharp
var queue = new BlockingCollection<int>(boundedCapacity: 5);

// Producer
Task.Run(() =>
{
    for(int i=0; i<10; i++) queue.Add(i);
    queue.CompleteAdding();
});

// Consumer
foreach (var item in queue.GetConsumingEnumerable())
{
    Console.WriteLine($"Consumed: {item}");
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q40"></a>
### Q40: How do you use `System.Text.Json` Source Generators?

**Difficulty**: Advanced

**Strategy**:

**Strategy:**
Source Generators generate serialization code at compile time, improving startup performance and reducing runtime overhead compared to reflection-based serialization.

**Code Example:**
```csharp
[JsonSerializable(typeof(WeatherForecast))]
internal partial class MyJsonContext : JsonSerializerContext { }

var json = JsonSerializer.Serialize(
    new WeatherForecast { Date = DateTime.Now }, 
    MyJsonContext.Default.WeatherForecast
);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q41"></a>
### Q41: How do you handle configuration with the Options Pattern?

**Difficulty**: Beginner

**Strategy**:

**Strategy:**
Bind configuration sections to strongly-typed classes using `IOptions<T>`. This supports validation and hot-reloading (`IOptionsSnapshot`, `IOptionsMonitor`).

**Code Example:**
```csharp
// appsettings.json: { "MySettings": { "RetryCount": 3 } }

public class MySettings { public int RetryCount { get; set; } }

// Register
builder.Services.Configure<MySettings>(builder.Configuration.GetSection("MySettings"));

// Inject
public class Service
{
    public Service(IOptions<MySettings> options)
    {
        int retries = options.Value.RetryCount;
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q42"></a>
### Q42: How do you use `PeriodicTimer` (Net 6)?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
`PeriodicTimer` is an async-friendly timer that doesn't fire overlapping ticks. It's safer and cleaner than `System.Timers.Timer` for async loops.

**Code Example:**
```csharp
var timer = new PeriodicTimer(TimeSpan.FromSeconds(1));

while (await timer.WaitForNextTickAsync())
{
    Console.WriteLine("Tick: " + DateTime.Now);
    // Even if this takes > 1s, next tick waits until this finishes (no overlap)
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q43"></a>
### Q43: How do you implement a custom Tag Helper in ASP.NET Core?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Inherit from `TagHelper` and override `Process`. Tag Helpers allow server-side code to participate in creating and rendering HTML elements in Razor views.

**Code Example:**
```csharp
[HtmlTargetElement("bold")]
public class BoldTagHelper : TagHelper
{
    public override void Process(TagHelperContext context, TagHelperOutput output)
    {
        output.TagName = "strong"; // Replace <bold> with <strong>
    }
}

// Usage in View: <bold>Hello</bold> -> <strong>Hello</strong>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q44"></a>
### Q44: How do you use `Interlocked` class for atomic operations?

**Difficulty**: Advanced

**Strategy**:

**Strategy:**
`Interlocked` provides atomic operations for variables shared by multiple threads. It's faster than locking for simple increments or exchanges.

**Code Example:**
```csharp
private int _counter = 0;

public void Increment()
{
    // Atomic increment
    Interlocked.Increment(ref _counter);
}

public void CompareExchange()
{
    // Set to 10 only if currently 0
    Interlocked.CompareExchange(ref _counter, 10, 0);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q45"></a>
### Q45: How do you use Records with `with` expressions?

**Difficulty**: Beginner

**Strategy**:

**Strategy:**
Records are immutable by default. The `with` expression allows non-destructive mutation, creating a new record with modified properties.

**Code Example:**
```csharp
public record Person(string Name, int Age);

var p1 = new Person("Alice", 30);
var p2 = p1 with { Age = 31 }; // Copy of p1 with new Age

Console.WriteLine(p1.Age); // 30
Console.WriteLine(p2.Age); // 31
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q46"></a>
### Q46: How do you implement API Versioning?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Use `Asp.Versioning.Http` package. Configure it to read versions from the URL, header, or query string. Decorate controllers with `[ApiVersion]`. 

**Code Example:**
```csharp
builder.Services.AddApiVersioning(options =>
{
    options.AssumeDefaultVersionWhenUnspecified = true;
    options.DefaultApiVersion = new ApiVersion(1, 0);
});

[ApiVersion("1.0")]
[Route("api/v{version:apiVersion}/[controller]")]
public class ProductsController : ControllerBase { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q47"></a>
### Q47: How do you use `simd` (Single Instruction, Multiple Data) in .NET?

**Difficulty**: Expert

**Strategy**:

**Strategy:**
Use `Vector<T>` or `Vector128<T>`/`Vector256<T>` from `System.Runtime.Intrinsics` to perform parallel operations on data using CPU vector instructions.

**Code Example:**
```csharp
public void AddVectors(ReadOnlySpan<int> a, ReadOnlySpan<int> b, Span<int> result)
{
    int i = 0;
    int vectorSize = Vector<int>.Count;
    
    // Vectorized loop
    for (; i <= a.Length - vectorSize; i += vectorSize)
    {
        var v1 = new Vector<int>(a.Slice(i));
        var v2 = new Vector<int>(b.Slice(i));
        (v1 + v2).CopyTo(result.Slice(i));
    }
    
    // Handle remaining elements...
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q48"></a>
### Q48: How do you use `CallerMemberName` attribute?

**Difficulty**: Beginner

**Strategy**:

**Strategy:**
`[CallerMemberName]` automatically populates a parameter with the name of the calling method or property. Useful for `INotifyPropertyChanged`.

**Code Example:**
```csharp
public void OnPropertyChanged([CallerMemberName] string propertyName = null)
{
    PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
}

public string Name
{
    get => _name;
    set
    {
        _name = value;
        OnPropertyChanged(); // "Name" is passed automatically
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q49"></a>
### Q49: How do you use `Yield Return` for state machine generation?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
`yield return` generates an iterator state machine. It allows returning elements one by one, enabling lazy evaluation of sequences.

**Code Example:**
```csharp
public IEnumerable<int> Filter(IEnumerable<int> numbers)
{
    foreach (var n in numbers)
    {
        if (n > 10)
        {
            yield return n; // Returns control to caller, then resumes here
        }
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q50"></a>
### Q50: How do you use `Unsafe` class for memory manipulation?

**Difficulty**: Expert

**Strategy:**
`Unsafe` allows bypassing type safety checks (like `reinterpret_cast` in C++). Use it with caution for high-performance memory reinterpretation.

**Code Example:**
```csharp
using System.Runtime.CompilerServices;

public void CastExample()
{
    int value = 123;
    
    // Reinterpret int as float (unsafe)
    float f = Unsafe.As<int, float>(ref value);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

<a id="q51"></a>
### Q51: How do you handle .NET state management in large scale applications?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```javascript
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q52"></a>
### Q52: How do you perform .NET data validation in microservices?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```javascript
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q53"></a>
### Q53: How do you automate .NET deployment for mobile devices?

**Difficulty**: Advanced

**Strategy**:
Use CI/CD pipelines. Dockerize the application. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
steps:
  - run: npm test
  - run: docker build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q54"></a>
### Q54: How do you handle .NET concurrency issues in legacy systems?

**Difficulty**: Advanced

**Strategy**:
Use locks, queues, or atomic operations. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
await mutex.runExclusive(async () => {
  // critical section
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q55"></a>
### Q55: How do you implement .NET caching in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Use Redis or in-memory LRU caches. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const cache = new Map();
if (cache.has(key)) return cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q56"></a>
### Q56: How do you manage .NET configuration for real-time systems?

**Difficulty**: Beginner

**Strategy**:
Use environment variables or config files. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const config = process.env.CONFIG || 'default';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q57"></a>
### Q57: How do you handle .NET internationalization (i18n) in distributed systems?

**Difficulty**: Intermediate

**Strategy**:
Use i18n libraries. Extract strings to resource files.

**Code Example**:
```javascript
t('welcome_message')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q58"></a>
### Q58: How do you ensure .NET accessibility (a11y) in high-traffic sites?

**Difficulty**: Beginner

**Strategy**:
Use semantic HTML and ARIA roles. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
<button aria-label="Close">X</button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q59"></a>
### Q59: How do you optimize .NET network requests in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use batching, debouncing, or GraphQL. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
debounce(() => fetch(), 300);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q60"></a>
### Q60: How do you handle .NET performance optimization for production environments?

**Difficulty**: Advanced

**Strategy**:
Profile first, then optimize hot paths. Use caching and efficient algorithms.

**Code Example**:
```javascript
const start = performance.now();
// .NET logic
const end = performance.now();
console.log('Time:', end - start);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q61"></a>
### Q61: What are the security implications of .NET in large scale applications?

**Difficulty**: Intermediate

**Strategy**:
Validate all inputs. Sanitize data. Use least privilege principle.

**Code Example**:
```javascript
// Sanitize input
const clean = input.replace(/<script>/g, '');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q62"></a>
### Q62: How do you debug .NET memory leaks in microservices?

**Difficulty**: Advanced

**Strategy**:
Use heap snapshots and look for detached DOM nodes or uncleared listeners.

**Code Example**:
```javascript
// Check listeners
process.on('exit', () => cleanup());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q63"></a>
### Q63: Best practices for .NET code organization in mobile devices?

**Difficulty**: Beginner

**Strategy**:
Follow SOLID principles. Keep functions small and focused.

**Code Example**:
```javascript
// Single responsibility
function doOneThing() { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q64"></a>
### Q64: How do you implement .NET error handling for legacy systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```javascript
try {
  await .NETOperation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q65"></a>
### Q65: How do you test .NET functionality in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```javascript
test('.NET works', () => {
  expect(.NET()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q66"></a>
### Q66: How do you handle .NET state management in real-time systems?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```javascript
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q67"></a>
### Q67: How do you perform .NET data validation in distributed systems?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```javascript
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q68"></a>
### Q68: How do you automate .NET deployment for high-traffic sites?

**Difficulty**: Advanced

**Strategy**:
Use CI/CD pipelines. Dockerize the application. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
steps:
  - run: npm test
  - run: docker build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q69"></a>
### Q69: How do you handle .NET concurrency issues in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use locks, queues, or atomic operations. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
await mutex.runExclusive(async () => {
  // critical section
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q70"></a>
### Q70: How do you implement .NET caching in production environments?

**Difficulty**: Intermediate

**Strategy**:
Use Redis or in-memory LRU caches. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const cache = new Map();
if (cache.has(key)) return cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q71"></a>
### Q71: How do you manage .NET configuration for large scale applications?

**Difficulty**: Beginner

**Strategy**:
Use environment variables or config files. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const config = process.env.CONFIG || 'default';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q72"></a>
### Q72: How do you handle .NET internationalization (i18n) in microservices?

**Difficulty**: Intermediate

**Strategy**:
Use i18n libraries. Extract strings to resource files.

**Code Example**:
```javascript
t('welcome_message')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q73"></a>
### Q73: How do you ensure .NET accessibility (a11y) in mobile devices?

**Difficulty**: Beginner

**Strategy**:
Use semantic HTML and ARIA roles. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
<button aria-label="Close">X</button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q74"></a>
### Q74: How do you optimize .NET network requests in legacy systems?

**Difficulty**: Advanced

**Strategy**:
Use batching, debouncing, or GraphQL. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
debounce(() => fetch(), 300);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q75"></a>
### Q75: How do you handle .NET performance optimization for cloud infrastructure?

**Difficulty**: Advanced

**Strategy**:
Profile first, then optimize hot paths. Use caching and efficient algorithms.

**Code Example**:
```javascript
const start = performance.now();
// .NET logic
const end = performance.now();
console.log('Time:', end - start);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q76"></a>
### Q76: What are the security implications of .NET in real-time systems?

**Difficulty**: Intermediate

**Strategy**:
Validate all inputs. Sanitize data. Use least privilege principle.

**Code Example**:
```javascript
// Sanitize input
const clean = input.replace(/<script>/g, '');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q77"></a>
### Q77: How do you debug .NET memory leaks in distributed systems?

**Difficulty**: Advanced

**Strategy**:
Use heap snapshots and look for detached DOM nodes or uncleared listeners.

**Code Example**:
```javascript
// Check listeners
process.on('exit', () => cleanup());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q78"></a>
### Q78: Best practices for .NET code organization in high-traffic sites?

**Difficulty**: Beginner

**Strategy**:
Follow SOLID principles. Keep functions small and focused.

**Code Example**:
```javascript
// Single responsibility
function doOneThing() { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q79"></a>
### Q79: How do you implement .NET error handling for embedded systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```javascript
try {
  await .NETOperation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q80"></a>
### Q80: How do you test .NET functionality in production environments?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```javascript
test('.NET works', () => {
  expect(.NET()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q81"></a>
### Q81: How do you handle .NET state management in large scale applications?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```javascript
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q82"></a>
### Q82: How do you perform .NET data validation in microservices?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```javascript
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q83"></a>
### Q83: How do you automate .NET deployment for mobile devices?

**Difficulty**: Advanced

**Strategy**:
Use CI/CD pipelines. Dockerize the application. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
steps:
  - run: npm test
  - run: docker build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q84"></a>
### Q84: How do you handle .NET concurrency issues in legacy systems?

**Difficulty**: Advanced

**Strategy**:
Use locks, queues, or atomic operations. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
await mutex.runExclusive(async () => {
  // critical section
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q85"></a>
### Q85: How do you implement .NET caching in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Use Redis or in-memory LRU caches. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const cache = new Map();
if (cache.has(key)) return cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q86"></a>
### Q86: How do you manage .NET configuration for real-time systems?

**Difficulty**: Beginner

**Strategy**:
Use environment variables or config files. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const config = process.env.CONFIG || 'default';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q87"></a>
### Q87: How do you handle .NET internationalization (i18n) in distributed systems?

**Difficulty**: Intermediate

**Strategy**:
Use i18n libraries. Extract strings to resource files.

**Code Example**:
```javascript
t('welcome_message')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q88"></a>
### Q88: How do you ensure .NET accessibility (a11y) in high-traffic sites?

**Difficulty**: Beginner

**Strategy**:
Use semantic HTML and ARIA roles. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
<button aria-label="Close">X</button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q89"></a>
### Q89: How do you optimize .NET network requests in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use batching, debouncing, or GraphQL. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
debounce(() => fetch(), 300);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q90"></a>
### Q90: How do you handle .NET performance optimization for production environments?

**Difficulty**: Advanced

**Strategy**:
Profile first, then optimize hot paths. Use caching and efficient algorithms.

**Code Example**:
```javascript
const start = performance.now();
// .NET logic
const end = performance.now();
console.log('Time:', end - start);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q91"></a>
### Q91: What are the security implications of .NET in large scale applications?

**Difficulty**: Intermediate

**Strategy**:
Validate all inputs. Sanitize data. Use least privilege principle.

**Code Example**:
```javascript
// Sanitize input
const clean = input.replace(/<script>/g, '');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q92"></a>
### Q92: How do you debug .NET memory leaks in microservices?

**Difficulty**: Advanced

**Strategy**:
Use heap snapshots and look for detached DOM nodes or uncleared listeners.

**Code Example**:
```javascript
// Check listeners
process.on('exit', () => cleanup());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q93"></a>
### Q93: Best practices for .NET code organization in mobile devices?

**Difficulty**: Beginner

**Strategy**:
Follow SOLID principles. Keep functions small and focused.

**Code Example**:
```javascript
// Single responsibility
function doOneThing() { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q94"></a>
### Q94: How do you implement .NET error handling for legacy systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```javascript
try {
  await .NETOperation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q95"></a>
### Q95: How do you test .NET functionality in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```javascript
test('.NET works', () => {
  expect(.NET()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q96"></a>
### Q96: How do you handle .NET state management in real-time systems?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```javascript
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q97"></a>
### Q97: How do you perform .NET data validation in distributed systems?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```javascript
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q98"></a>
### Q98: How do you automate .NET deployment for high-traffic sites?

**Difficulty**: Advanced

**Strategy**:
Use CI/CD pipelines. Dockerize the application. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
steps:
  - run: npm test
  - run: docker build
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q99"></a>
### Q99: How do you handle .NET concurrency issues in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use locks, queues, or atomic operations. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
await mutex.runExclusive(async () => {
  // critical section
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q100"></a>
### Q100: How do you implement .NET caching in production environments?

**Difficulty**: Intermediate

**Strategy**:
Use Redis or in-memory LRU caches. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const cache = new Map();
if (cache.has(key)) return cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>
