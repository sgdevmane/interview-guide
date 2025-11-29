# .NET Interview Questions

## Table of Contents
- [.NET Interview Questions](#net-interview-questions)
  - [Table of Contents](#table-of-contents)
    - [Q1: What is the difference between the .NET Framework, .NET Core, and .NET 5/6/7+? Explain the evolution of the .NET platform.](#q1-what-is-the-difference-between-the-net-framework-net-core-and-net-567-explain-the-evolution-of-the-net-platform)
    - [Q2: What is the Common Language Runtime (CLR)?](#q2-what-is-the-common-language-runtime-clr)
    - [Q3: Explain the difference between managed and unmanaged code.](#q3-explain-the-difference-between-managed-and-unmanaged-code)
    - [Q4: What is the Global Assembly Cache (GAC)?](#q4-what-is-the-global-assembly-cache-gac)
    - [Q5: What is LINQ (Language Integrated Query)?](#q5-what-is-linq-language-integrated-query)
    - [Q6: What is ASP.NET Core?](#q6-what-is-aspnet-core)
    - [Q7: Explain middleware in ASP.NET Core.](#q7-explain-middleware-in-aspnet-core)
    - [Q8: What is dependency injection in .NET?](#q8-what-is-dependency-injection-in-net)
    - [Q9: What is Entity Framework Core?](#q9-what-is-entity-framework-core)
    - [Q10: What is the difference between `IQueryable` and `IEnumerable`?](#q10-what-is-the-difference-between-iqueryable-and-ienumerable)
    - [Q11: What is Razor Pages?](#q11-what-is-razor-pages)
    - [Q12: What is Blazor?](#q12-what-is-blazor)
    - [Q13: What is SignalR?](#q13-what-is-signalr)
    - [Q14: What is a `Task` in .NET?](#q14-what-is-a-task-in-net)
    - [Q15: What is the purpose of the `using` statement in C#?](#q15-what-is-the-purpose-of-the-using-statement-in-c)
    - [Q16: What are delegates in C#?](#q16-what-are-delegates-in-c)
    - [Q17: What are extension methods in C#?](#q17-what-are-extension-methods-in-c)
    - [Q18: What is the difference between `struct` and `class` in C#?](#q18-what-is-the-difference-between-struct-and-class-in-c)
    - [Q19: What is boxing and unboxing?](#q19-what-is-boxing-and-unboxing)
    - [Q20: What is NuGet?](#q20-what-is-nuget)
    - [Q21: What are C# Records (C# 9.0)?](#q21-what-are-c-records-c-90)
    - [Q22: What are Nullable Reference Types (C# 8.0)?](#q22-what-are-nullable-reference-types-c-80)
    - [Q23: What is Pattern Matching in C#?](#q23-what-is-pattern-matching-in-c)
    - [Q24: What are Async Streams (C# 8.0)?](#q24-what-are-async-streams-c-80)
    - [Q25: What is the difference between `Task` and `ValueTask`?](#q25-what-is-the-difference-between-task-and-valuetask)
    - [Q26: What is `Span<T>` and `Memory<T>`?](#q26-what-is-spant-and-memoryt)
    - [Q27: What is Garbage Collection (GC) in .NET?](#q27-what-is-garbage-collection-gc-in-net)
    - [Q28: What is the `IDisposable` interface?](#q28-what-is-the-idisposable-interface)
    - [Q29: What is the difference between `ref` and `out` parameters?](#q29-what-is-the-difference-between-ref-and-out-parameters)
    - [Q30: What is `in` parameter modifier?](#q30-what-is-in-parameter-modifier)
    - [Q31: What is Reflection in .NET?](#q31-what-is-reflection-in-net)
    - [Q32: What are Attributes in C#?](#q32-what-are-attributes-in-c)
    - [Q33: What is Kestrel?](#q33-what-is-kestrel)
    - [Q34: What is the Startup class in ASP.NET Core?](#q34-what-is-the-startup-class-in-aspnet-core)
    - [Q35: What is the difference between `AddTransient`, `AddScoped`, and `AddSingleton`?](#q35-what-is-the-difference-between-addtransient-addscoped-and-addsingleton)
    - [Q36: What is Model Binding?](#q36-what-is-model-binding)
    - [Q37: What are Tag Helpers?](#q37-what-are-tag-helpers)
    - [Q38: What is gRPC?](#q38-what-is-grpc)
    - [Q39: What is SignalR used for?](#q39-what-is-signalr-used-for)
    - [Q40: What is Blazor WebAssembly vs. Blazor Server?](#q40-what-is-blazor-webassembly-vs-blazor-server)
    - [Q41: What is Minimal APIs (C# 10)?](#q41-what-is-minimal-apis-c-10)
    - [Q42: What is AutoMapper?](#q42-what-is-automapper)
    - [Q43: What is FluentValidation?](#q43-what-is-fluentvalidation)
    - [Q44: What is MediatR?](#q44-what-is-mediatr)
    - [Q45: What is CQRS (Command Query Responsibility Segregation)?](#q45-what-is-cqrs-command-query-responsibility-segregation)
    - [Q46: What is xUnit?](#q46-what-is-xunit)
    - [Q47: What is Moq?](#q47-what-is-moq)
    - [Q48: What is `IHttpClientFactory`?](#q48-what-is-ihttpclientfactory)
    - [Q49: What is Polly?](#q49-what-is-polly)
    - [Q50: What is Serilog?](#q50-what-is-serilog)
    - [Q51: What is Swagger/OpenAPI?](#q51-what-is-swaggeropenapi)
    - [Q52: What is JWT (JSON Web Token)?](#q52-what-is-jwt-json-web-token)
    - [Q53: What is CORS (Cross-Origin Resource Sharing)?](#q53-what-is-cors-cross-origin-resource-sharing)
    - [Q54: What is OAuth 2.0?](#q54-what-is-oauth-20)
    - [Q55: What is OpenID Connect?](#q55-what-is-openid-connect)
    - [Q56: What is IdentityServer?](#q56-what-is-identityserver)
    - [Q57: What is Docker support in .NET?](#q57-what-is-docker-support-in-net)
    - [Q58: What is the difference between `IEnumerable` and `IEnumerator`?](#q58-what-is-the-difference-between-ienumerable-and-ienumerator)
    - [Q59: What is `yield return`?](#q59-what-is-yield-return)
    - [Q60: What is the `params` keyword?](#q60-what-is-the-params-keyword)
    - [Q61: What is the `dynamic` type?](#q61-what-is-the-dynamic-type)
    - [Q62: What is the `sealed` keyword?](#q62-what-is-the-sealed-keyword)
    - [Q63: What is the `abstract` keyword?](#q63-what-is-the-abstract-keyword)
    - [Q64: What is an Interface?](#q64-what-is-an-interface)
    - [Q65: What is Multiple Inheritance in C#?](#q65-what-is-multiple-inheritance-in-c)
    - [Q66: What is `Lazy<T>`?](#q66-what-is-lazyt)
    - [Q67: What is the difference between `AppDomain` and `Process`?](#q67-what-is-the-difference-between-appdomain-and-process)
    - [Q68: What is JIT Compilation?](#q68-what-is-jit-compilation)
    - [Q69: What is AOT (Ahead-of-Time) Compilation?](#q69-what-is-aot-ahead-of-time-compilation)
    - [Q70: What is Roslyn?](#q70-what-is-roslyn)
    - [Q71: What is LINQ to SQL vs. Entity Framework?](#q71-what-is-linq-to-sql-vs-entity-framework)
    - [Q72: What is Code First vs. Database First?](#q72-what-is-code-first-vs-database-first)
    - [Q73: What is the Repository Pattern?](#q73-what-is-the-repository-pattern)
    - [Q74: What is the Unit of Work Pattern?](#q74-what-is-the-unit-of-work-pattern)
    - [Q75: What is OData?](#q75-what-is-odata)
    - [Q76: What is GraphQL hot chocolate?](#q76-what-is-graphql-hot-chocolate)
    - [Q77: What is RabbitMQ?](#q77-what-is-rabbitmq)
    - [Q78: What is Azure Functions?](#q78-what-is-azure-functions)
    - [Q79: What is App settings (`appsettings.json`)?](#q79-what-is-app-settings-appsettingsjson)
    - [Q80: What is the Options Pattern?](#q80-what-is-the-options-pattern)
    - [Q81: What is Middleware?](#q81-what-is-middleware)
    - [Q82: What is the difference between `Run`, `Use`, and `Map` in Middleware?](#q82-what-is-the-difference-between-run-use-and-map-in-middleware)
    - [Q83: What are Global Exception Handlers?](#q83-what-are-global-exception-handlers)
    - [Q84: What is Health Checks?](#q84-what-is-health-checks)
    - [Q85: What is Output Caching?](#q85-what-is-output-caching)
    - [Q86: What is Distributed Caching?](#q86-what-is-distributed-caching)
    - [Q87: What is Data Protection API?](#q87-what-is-data-protection-api)
    - [Q88: What is User Secrets?](#q88-what-is-user-secrets)
    - [Q89: What is Environment Variables?](#q89-what-is-environment-variables)
    - [Q90: What is `IHostedService`?](#q90-what-is-ihostedservice)
    - [Q91: What is BackgroundService?](#q91-what-is-backgroundservice)
    - [Q92: What is `System.Text.Json`?](#q92-what-is-systemtextjson)
    - [Q93: What is `IAsyncEnumerable`?](#q93-what-is-iasyncenumerable)
    - [Q94: What is Channels?](#q94-what-is-channels)
    - [Q95: What is Rate Limiting?](#q95-what-is-rate-limiting)
    - [Q96: What is HybridCache (.NET 9)?](#q96-what-is-hybridcache-net-9)
    - [Q97: What is .NET MAUI?](#q97-what-is-net-maui)
    - [Q98: What is Blazor Hybrid?](#q98-what-is-blazor-hybrid)
    - [Q99: What is Upgrade Assistant?](#q99-what-is-upgrade-assistant)
    - [Q100: What is the future of .NET?](#q100-what-is-the-future-of-net)


---

### Q1: What is the difference between the .NET Framework, .NET Core, and .NET 5/6/7+? Explain the evolution of the .NET platform.

**Answer:**
Understanding the evolution of .NET is crucial for any .NET developer. The platform has undergone significant changes, moving from a Windows-only framework to a cross-platform, open-source ecosystem.

**.NET Framework**
- **Initial Release:** 2002
- **Platform:** Windows-only
- **Key Features:**
    - **Common Language Runtime (CLR):** The execution engine that manages memory, security, and other system services.
    - **Framework Class Library (FCL):** A comprehensive library of reusable classes, interfaces, and value types.
    - **Windows-specific APIs:** Deep integration with Windows, including WPF, Windows Forms, and ASP.NET (System.Web).
- **Use Case:** Primarily for building Windows desktop and web applications.

**.NET Core**
- **Initial Release:** 2016
- **Platform:** Cross-platform (Windows, macOS, Linux)
- **Key Features:**
    - **Open Source:** Developed as an open-source project on GitHub.
    - **High Performance:** Optimized for performance and scalability.
    - **Modular:** Built with a modular architecture, allowing you to include only the necessary components.
    - **Side-by-side Installation:** Different versions can run on the same machine without conflicts.
- **Use Case:** For building modern, cross-platform web apps, microservices, and console applications.

**.NET (5/6/7+): The Unification**
- **Initial Release:** .NET 5 in 2020
- **Concept:** A single, unified platform that combines the best of .NET Framework and .NET Core.
- **Key Features:**
    - **Single BCL (Base Class Library):** One set of APIs that works across all application types.
    - **Unified Toolchain:** A single SDK and command-line interface (CLI) for all .NET projects.
    - **Support for a wide range of application models:** Web, mobile (via .NET MAUI), desktop, cloud, and IoT.
    - **Regular Release Cadence:** A new major version is released annually in November.

**Evolution Summary:**

| Platform | Key Characteristic | Primary Focus |
| :--- | :--- | :--- |
| **.NET Framework** | Windows-only, monolithic | Windows desktop and web apps |
| **.NET Core** | Cross-platform, open-source, modular | Modern web apps and microservices |
| **.NET 5+** | Unified, single platform | All application types (web, mobile, desktop, etc.) |

**Code Example (Illustrating cross-platform nature of .NET Core/5+):**

This simple console application can be built and run on Windows, macOS, or Linux without any code changes.

```csharp
// Program.cs
using System;
using System.Runtime.InteropServices;

public class Program
{
    public static void Main()
    {
        Console.WriteLine("Hello from .NET!");
        Console.WriteLine($"Operating System: {RuntimeInformation.OSDescription}");
        Console.WriteLine($"OS Architecture: {RuntimeInformation.OSArchitecture}");
        Console.WriteLine($"Framework: {RuntimeInformation.FrameworkDescription}");
    }
}
```
### Q2: What is the Common Language Runtime (CLR)?

**Answer:**
The CLR is the virtual machine component of Microsoft's .NET framework. It manages the execution of .NET programs by handling memory management, garbage collection, type safety, and exception handling.

### Q3: Explain the difference between managed and unmanaged code.

**Answer:**
-   **Managed Code:** Code that is executed by the CLR. It benefits from services like garbage collection and security.
-   **Unmanaged Code:** Code that is executed directly by the operating system, outside the .NET environment. It requires manual memory management.

### Q4: What is the Global Assembly Cache (GAC)?

**Answer:**
The GAC is a machine-wide code cache that stores assemblies specifically designated to be shared by several applications on the computer.

### Q5: What is LINQ (Language Integrated Query)?

**Answer:**
LINQ is a set of features that extends powerful query capabilities to the language syntax of C# and VB.NET. It provides a consistent way to query data from different sources like databases, XML documents, and in-memory collections.

```csharp
var evenNumbers = from num in numbers
                  where num % 2 == 0
                  select num;
```

### Q6: What is ASP.NET Core?

**Answer:**
ASP.NET Core is a cross-platform, high-performance, open-source framework for building modern, cloud-based, internet-connected applications.

### Q7: Explain middleware in ASP.NET Core.

**Answer:**
Middleware is software that's assembled into an application pipeline to handle requests and responses. Each component chooses whether to pass the request on to the next component in the pipeline, and can perform work before and after the next component is invoked.

### Q8: What is dependency injection in .NET?

**Answer:**
Dependency Injection (DI) is a design pattern used to implement Inversion of Control (IoC). It allows the creation of dependent objects outside of a class and provides those objects to the class through different ways.

### Q9: What is Entity Framework Core?

**Answer:**
Entity Framework (EF) Core is a modern object-database mapper for .NET. It supports LINQ queries, change tracking, updates, and schema migrations.

### Q10: What is the difference between `IQueryable` and `IEnumerable`?

**Answer:**
-   `IEnumerable`: Represents a forward-only cursor of a collection. When you query an `IEnumerable`, it loads the entire collection into memory before filtering.
-   `IQueryable`: Represents a query that can be executed against a specific data source. It builds a query expression tree that is executed on the server side, resulting in a more efficient query.

### Q11: What is Razor Pages?

**Answer:**
Razor Pages is a page-based programming model in ASP.NET Core that makes building web UI easier and more productive. It's a simpler alternative to the Model-View-Controller (MVC) pattern.

### Q12: What is Blazor?

**Answer:**
Blazor is a framework for building interactive client-side web UI with .NET. It allows you to build reusable UI components using C# and Razor syntax.

### Q13: What is SignalR?

**Answer:**
SignalR is a library for ASP.NET developers that simplifies the process of adding real-time web functionality to applications. Real-time web functionality is the ability to have server code push content to connected clients instantly as it becomes available.

### Q14: What is a `Task` in .NET?

**Answer:**
A `Task` represents an asynchronous operation. It's the core of the Task-based Asynchronous Pattern (TAP) in .NET, used with `async` and `await` keywords.

### Q15: What is the purpose of the `using` statement in C#?

**Answer:**
The `using` statement provides a convenient syntax that ensures the correct use of `IDisposable` objects. When the control leaves the `using` block, the `Dispose` method is called on the object.

### Q16: What are delegates in C#?

**Answer:**
A delegate is a type that represents references to methods with a particular parameter list and return type. They are similar to function pointers in C++.

### Q17: What are extension methods in C#?

**Answer:**
Extension methods enable you to "add" methods to existing types without creating a new derived type, recompiling, or otherwise modifying the original type.

### Q18: What is the difference between `struct` and `class` in C#?

**Answer:**
-   `class`: Reference type, stored on the heap.
-   `struct`: Value type, stored on the stack.

### Q19: What is boxing and unboxing?

**Answer:**
-   **Boxing:** The process of converting a value type to the type `object` or to any interface type implemented by this value type.
-   **Unboxing:** The process of converting an `object` type back to a value type.

### Q20: What is NuGet?

**Answer:**
NuGet is the package manager for .NET. It enables developers to create, share, and consume useful .NET libraries.
### Q21: What are C# Records (C# 9.0)?
**Difficulty: Medium**

**Answer:**
Reference types that provide built-in functionality for encapsulating data. They are immutable by default and support value-based equality.
```csharp
public record Person(string FirstName, string LastName);
```

### Q22: What are Nullable Reference Types (C# 8.0)?
**Difficulty: Medium**

**Answer:**
A feature that allows you to specify whether a reference type variable can be null.
```csharp
string? name = null; // Nullable
string name = "John"; // Non-nullable
```
Helps prevent `NullReferenceException`.

### Q23: What is Pattern Matching in C#?
**Difficulty: Medium**

**Answer:**
Allows you to test an expression against a specific shape or type.
```csharp
if (obj is Person { FirstName: "John" } p) { ... }
```
Includes `is` expressions, `switch` expressions, and property patterns.

### Q24: What are Async Streams (C# 8.0)?
**Difficulty: Advanced**

**Answer:**
Allows you to iterate over a collection of data asynchronously using `await foreach`. The return type is `IAsyncEnumerable<T>`.
```csharp
await foreach (var item in GetDataAsync()) { ... }
```

### Q25: What is the difference between `Task` and `ValueTask`?
**Difficulty: Advanced**

**Answer:**
- `Task`: A reference type. Allocates an object on the heap.
- `ValueTask`: A value type (struct). Avoids allocation if the result is already available (synchronous completion). Used for high-performance scenarios.

### Q26: What is `Span<T>` and `Memory<T>`?
**Difficulty: Advanced**

**Answer:**
Types that provide a safe and efficient way to work with contiguous regions of arbitrary memory (managed arrays, native memory, stack memory) without copying.
- `Span<T>`: Stack-only.
- `Memory<T>`: Can be stored on the heap.

### Q27: What is Garbage Collection (GC) in .NET?
**Difficulty: Advanced**

**Answer:**
Automatic memory management. The GC allocates and releases memory for your application. It works on a generational basis (Gen 0, 1, 2) to optimize performance.

### Q28: What is the `IDisposable` interface?
**Difficulty: Medium**

**Answer:**
Defines a method `Dispose()` to release unmanaged resources (file handles, database connections). Used with the `using` statement.

### Q29: What is the difference between `ref` and `out` parameters?
**Difficulty: Easy**

**Answer:**
- `ref`: Variable must be initialized before passing.
- `out`: Variable does not need to be initialized before passing, but must be assigned a value inside the method.

### Q30: What is `in` parameter modifier?
**Difficulty: Medium**

**Answer:**
Passes arguments by reference but prevents modification (read-only reference). Useful for performance with large structs.

### Q31: What is Reflection in .NET?
**Difficulty: Advanced**

**Answer:**
Provides objects (of type `Type`) that describe assemblies, modules, and types. You can use reflection to dynamically create instances, bind types, or invoke methods at runtime.

### Q32: What are Attributes in C#?
**Difficulty: Medium**

**Answer:**
Metadata tags that convey information to the runtime or compiler. (e.g., `[Obsolete]`, `[Serializable]`, `[HttpPost]`).

### Q33: What is Kestrel?
**Difficulty: Medium**

**Answer:**
A cross-platform, lightweight, and high-performance web server for ASP.NET Core. It is included by default and can run standalone or behind a reverse proxy (IIS, Nginx).

### Q34: What is the Startup class in ASP.NET Core?
**Difficulty: Medium**

**Answer:**
The entry point for configuring the application. It contains `ConfigureServices` (for DI) and `Configure` (for middleware pipeline). Note: In .NET 6+, this is often unified into `Program.cs`.

### Q35: What is the difference between `AddTransient`, `AddScoped`, and `AddSingleton`?
**Difficulty: Medium**

**Answer:**
- `Transient`: Created every time they are requested.
- `Scoped`: Created once per client request (HTTP request).
- `Singleton`: Created the first time they are requested (or at startup) and used for all subsequent requests.

### Q36: What is Model Binding?
**Difficulty: Medium**

**Answer:**
The process of mapping data from HTTP requests (route data, query string, body) to action method parameters.

### Q37: What are Tag Helpers?
**Difficulty: Easy**

**Answer:**
Server-side code in Razor files that participates in creating and rendering HTML elements. (e.g., `asp-controller`, `asp-action`).

### Q38: What is gRPC?
**Difficulty: Advanced**

**Answer:**
A high-performance, open-source RPC framework. Uses Protocol Buffers (Protobuf) for serialization and HTTP/2 for transport. Supported natively in .NET.

### Q39: What is SignalR used for?
**Difficulty: Medium**

**Answer:**
Real-time web functionality. It enables server-side code to push content to connected clients instantly (e.g., chat apps, dashboards).

### Q40: What is Blazor WebAssembly vs. Blazor Server?
**Difficulty: Medium**

**Answer:**
- **WebAssembly:** Runs in the browser via WebAssembly. Client-side rendering. Offline capable.
- **Server:** Runs on the server. UI updates are sent over a SignalR connection.

### Q41: What is Minimal APIs (C# 10)?
**Difficulty: Medium**

**Answer:**
A simplified way to build HTTP APIs with minimal dependencies and boilerplate code, typically defined in `Program.cs`.
```csharp
var app = WebApplication.Create(args);
app.MapGet("/", () => "Hello World!");
app.Run();
```

### Q42: What is AutoMapper?
**Difficulty: Medium**

**Answer:**
A library that automatically maps properties from one object to another (e.g., Entity to DTO).

### Q43: What is FluentValidation?
**Difficulty: Medium**

**Answer:**
A library for building strongly-typed validation rules for your business objects.

### Q44: What is MediatR?
**Difficulty: Advanced**

**Answer:**
A library implementation of the Mediator pattern. It decouples request sending from request handling (CQRS support).

### Q45: What is CQRS (Command Query Responsibility Segregation)?
**Difficulty: Advanced**

**Answer:**
A pattern that separates read and update operations for a data store. Commands change state, Queries return data.

### Q46: What is xUnit?
**Difficulty: Easy**

**Answer:**
A free, open-source, community-focused unit testing tool for .NET.

### Q47: What is Moq?
**Difficulty: Medium**

**Answer:**
A mocking library for .NET used in unit testing to isolate the code under test by simulating dependencies.

### Q48: What is `IHttpClientFactory`?
**Difficulty: Advanced**

**Answer:**
A factory abstraction for creating `HttpClient` instances. It manages the underlying `HttpClientHandler` lifetime to avoid socket exhaustion and DNS issues.

### Q49: What is Polly?
**Difficulty: Advanced**

**Answer:**
A .NET resilience and transient-fault-handling library. Provides policies like Retry, Circuit Breaker, Timeout, Bulkhead Isolation, and Fallback.

### Q50: What is Serilog?
**Difficulty: Medium**

**Answer:**
A diagnostic logging library for .NET applications. Supports structured logging.

### Q51: What is Swagger/OpenAPI?
**Difficulty: Easy**

**Answer:**
A specification for building, documenting, and consuming RESTful web services. Swashbuckle is the .NET implementation.

### Q52: What is JWT (JSON Web Token)?
**Difficulty: Medium**

**Answer:**
A compact, URL-safe means of representing claims to be transferred between two parties. Commonly used for stateless authentication.

### Q53: What is CORS (Cross-Origin Resource Sharing)?
**Difficulty: Medium**

**Answer:**
A security feature that restricts web pages from making requests to a different domain than the one that served the web page.

### Q54: What is OAuth 2.0?
**Difficulty: Advanced**

**Answer:**
An authorization framework that enables applications to obtain limited access to user accounts on an HTTP service (e.g., Google, Facebook login).

### Q55: What is OpenID Connect?
**Difficulty: Advanced**

**Answer:**
A simple identity layer on top of the OAuth 2.0 protocol. It allows clients to verify the identity of the end-user.

### Q56: What is IdentityServer?
**Difficulty: Advanced**

**Answer:**
An OpenID Connect and OAuth 2.0 framework for ASP.NET Core. (Note: Duende IdentityServer is the commercial successor).

### Q57: What is Docker support in .NET?
**Difficulty: Medium**

**Answer:**
.NET images are optimized for Docker. You can easily containerize .NET applications using Dockerfiles.

### Q58: What is the difference between `IEnumerable` and `IEnumerator`?
**Difficulty: Medium**

**Answer:**
- `IEnumerable`: Defines a method `GetEnumerator()` which returns an `IEnumerator`.
- `IEnumerator`: Provides the mechanism to iterate through the collection (`Current`, `MoveNext()`, `Reset()`).

### Q59: What is `yield return`?
**Difficulty: Medium**

**Answer:**
Used in an iterator block to provide a value to the enumerator object or to signal the end of iteration. It allows for stateful iteration without creating a temporary collection.

### Q60: What is the `params` keyword?
**Difficulty: Easy**

**Answer:**
Allows a method parameter to take a variable number of arguments.
```csharp
public void Print(params string[] args) { ... }
```

### Q61: What is the `dynamic` type?
**Difficulty: Medium**

**Answer:**
Bypasses compile-time type checking. Operations are resolved at runtime.

### Q62: What is the `sealed` keyword?
**Difficulty: Easy**

**Answer:**
Prevents a class from being inherited.

### Q63: What is the `abstract` keyword?
**Difficulty: Easy**

**Answer:**
- Abstract Class: Cannot be instantiated. Can contain abstract and non-abstract methods.
- Abstract Method: Has no body, must be implemented by derived class.

### Q64: What is an Interface?
**Difficulty: Easy**

**Answer:**
A contract that defines a set of methods, properties, and events. A class implementing an interface must provide implementation for all its members.

### Q65: What is Multiple Inheritance in C#?
**Difficulty: Easy**

**Answer:**
C# does not support multiple inheritance of classes. It supports multiple inheritance of interfaces.

### Q66: What is `Lazy<T>`?
**Difficulty: Medium**

**Answer:**
Provides support for lazy initialization. The object is created only when it is first accessed.

### Q67: What is the difference between `AppDomain` and `Process`?
**Difficulty: Advanced**

**Answer:**
- `Process`: An executing application under the OS.
- `AppDomain`: A logical partition within a process where .NET code executes. One process can contain multiple AppDomains (though this is less common in .NET Core).

### Q68: What is JIT Compilation?
**Difficulty: Advanced**

**Answer:**
Just-In-Time compilation. The CLR compiles MSIL (Intermediate Language) into native machine code just before execution.

### Q69: What is AOT (Ahead-of-Time) Compilation?
**Difficulty: Advanced**

**Answer:**
Compiles IL to native code at build time. Results in faster startup and smaller footprint, but with some limitations on dynamic features. Native AOT is a key feature in .NET 7/8.

### Q70: What is Roslyn?
**Difficulty: Advanced**

**Answer:**
The .NET Compiler Platform. It provides open-source C# and Visual Basic compilers with rich code analysis APIs.

### Q71: What is LINQ to SQL vs. Entity Framework?
**Difficulty: Medium**

**Answer:**
- LINQ to SQL: Lightweight, maps 1:1 to SQL Server tables. (Deprecated/Legacy).
- Entity Framework: Full-featured ORM, supports multiple DB providers, complex mappings, migrations.

### Q72: What is Code First vs. Database First?
**Difficulty: Medium**

**Answer:**
- Code First: Define domain classes first, then EF generates the database.
- Database First: Design database first, then EF generates the context and classes.

### Q73: What is the Repository Pattern?
**Difficulty: Medium**

**Answer:**
Abstractions the data access layer. It mediates between the domain and data mapping layers using a collection-like interface for accessing domain objects.

### Q74: What is the Unit of Work Pattern?
**Difficulty: Medium**

**Answer:**
Maintains a list of objects affected by a business transaction and coordinates the writing out of changes and the resolution of concurrency problems. Often used with Repository.

### Q75: What is OData?
**Difficulty: Advanced**

**Answer:**
Open Data Protocol. Allows the creation and consumption of queryable RESTful APIs.

### Q76: What is GraphQL hot chocolate?
**Difficulty: Advanced**

**Answer:**
Hot Chocolate is a popular GraphQL server for .NET.

### Q77: What is RabbitMQ?
**Difficulty: Advanced**

**Answer:**
A message broker. Used in .NET microservices for asynchronous communication (MassTransit is a popular .NET library for it).

### Q78: What is Azure Functions?
**Difficulty: Medium**

**Answer:**
Serverless compute service. Allows running event-triggered code without managing infrastructure.

### Q79: What is App settings (`appsettings.json`)?
**Difficulty: Easy**

**Answer:**
The standard configuration file in ASP.NET Core for storing application settings, connection strings, and logging configuration.

### Q80: What is the Options Pattern?
**Difficulty: Medium**

**Answer:**
A way to group related settings into strongly-typed classes and inject them via DI (`IOptions<T>`, `IOptionsSnapshot<T>`, `IOptionsMonitor<T>`).

### Q81: What is Middleware?
**Difficulty: Medium**

**Answer:**
Software that's assembled into an application pipeline to handle requests and responses.

### Q82: What is the difference between `Run`, `Use`, and `Map` in Middleware?
**Difficulty: Advanced**

**Answer:**
- `Run`: Terminates the pipeline.
- `Use`: Can chain to the next middleware.
- `Map`: Branches the pipeline based on the request path.

### Q83: What are Global Exception Handlers?
**Difficulty: Medium**

**Answer:**
Middleware configured to catch exceptions thrown anywhere in the pipeline and return a standardized error response.

### Q84: What is Health Checks?
**Difficulty: Medium**

**Answer:**
Middleware that provides an endpoint to report the health status of the application and its dependencies (DB, external services).

### Q85: What is Output Caching?
**Difficulty: Medium**

**Answer:**
Stores the generated output of a page/action to serve subsequent requests faster.

### Q86: What is Distributed Caching?
**Difficulty: Advanced**

**Answer:**
Cache shared by multiple app servers (e.g., Redis, SQL Server). Ensures consistency in a web farm.

### Q87: What is Data Protection API?
**Difficulty: Advanced**

**Answer:**
Provides cryptographic APIs for data protection (encryption/decryption) and key management.

### Q88: What is User Secrets?
**Difficulty: Easy**

**Answer:**
A tool for storing sensitive data (like connection strings) during development, outside the project tree to avoid committing them to source control.

### Q89: What is Environment Variables?
**Difficulty: Easy**

**Answer:**
Used to configure the application based on the runtime environment (Development, Staging, Production).

### Q90: What is `IHostedService`?
**Difficulty: Medium**

**Answer:**
Interface for defining background tasks that run within the ASP.NET Core application lifetime.

### Q91: What is BackgroundService?
**Difficulty: Medium**

**Answer:**
Base class for implementing a long-running `IHostedService`.

### Q92: What is `System.Text.Json`?
**Difficulty: Medium**

**Answer:**
High-performance, low-allocation JSON serialization library included in .NET Core 3.0+. Replaces Newtonsoft.Json for most use cases.

### Q93: What is `IAsyncEnumerable`?
**Difficulty: Advanced**

**Answer:**
Interface exposing an asynchronous enumerator. Enables Async Streams.

### Q94: What is Channels?
**Difficulty: Advanced**

**Answer:**
A thread-safe collection for passing data between producers and consumers asynchronously.

### Q95: What is Rate Limiting?
**Difficulty: Medium**

**Answer:**
Controlling the number of requests a client can make in a given time period. Native support added in .NET 7.

### Q96: What is HybridCache (.NET 9)?
**Difficulty: Advanced**

**Answer:**
A new caching abstraction that combines in-process (L1) and out-of-process (L2) caching to improve performance and reliability (stampede protection).

### Q97: What is .NET MAUI?
**Difficulty: Medium**

**Answer:**
Multi-platform App UI. Evolution of Xamarin.Forms. Allows building native apps for Android, iOS, macOS, and Windows from a single codebase.

### Q98: What is Blazor Hybrid?
**Difficulty: Advanced**

**Answer:**
Running Blazor components within a native app (MAUI, WPF, WinForms) using a WebView.

### Q99: What is Upgrade Assistant?
**Difficulty: Easy**

**Answer:**
A tool provided by Microsoft to help upgrade .NET Framework apps to the latest .NET version.

### Q100: What is the future of .NET?
**Difficulty: Easy**

**Answer:**
Continued focus on performance, cloud-native development (Aspire), AI integration (Semantic Kernel), and unification across all platforms. Yearly releases (Nov) ensure a predictable roadmap.
