# Java Interview Questions

## Table of Contents
- [Java Interview Questions](#java-interview-questions)
  - [Table of Contents](#table-of-contents)
    - [Q1: What is the difference between the Java Development Kit (JDK), Java Runtime Environment (JRE), and Java Virtual Machine (JVM)?](#q1-what-is-the-difference-between-the-java-development-kit-jdk-java-runtime-environment-jre-and-java-virtual-machine-jvm)
    - [Q2: What is the difference between `==` and `.equals()`?](#q2-what-is-the-difference-between--and-equals)
    - [Q3: What are the main principles of Object-Oriented Programming (OOP)?](#q3-what-are-the-main-principles-of-object-oriented-programming-oop)
    - [Q4: What is the difference between an `abstract class` and an `interface`?](#q4-what-is-the-difference-between-an-abstract-class-and-an-interface)
    - [Q5: What is the `final` keyword in Java?](#q5-what-is-the-final-keyword-in-java)
    - [Q6: What is the `static` keyword in Java?](#q6-what-is-the-static-keyword-in-java)
    - [Q7: What is method overloading and method overriding?](#q7-what-is-method-overloading-and-method-overriding)
    - [Q8: What is the Java Collections Framework?](#q8-what-is-the-java-collections-framework)
    - [Q9: What is the difference between `ArrayList` and `LinkedList`?](#q9-what-is-the-difference-between-arraylist-and-linkedlist)
    - [Q10: What is the difference between `HashMap` and `HashTable`?](#q10-what-is-the-difference-between-hashmap-and-hashtable)
    - [Q11: What is exception handling in Java?](#q11-what-is-exception-handling-in-java)
    - [Q12: What is the difference between checked and unchecked exceptions?](#q12-what-is-the-difference-between-checked-and-unchecked-exceptions)
    - [Q13: What is garbage collection in Java?](#q13-what-is-garbage-collection-in-java)
    - [Q14: What is multithreading in Java?](#q14-what-is-multithreading-in-java)
    - [Q15: What is the difference between `Runnable` and `Thread`?](#q15-what-is-the-difference-between-runnable-and-thread)
    - [Q16: What are generics in Java?](#q16-what-are-generics-in-java)
    - [Q17: What are lambda expressions in Java?](#q17-what-are-lambda-expressions-in-java)
    - [Q18: What is the Stream API?](#q18-what-is-the-stream-api)
    - [Q19: What is the `Optional` class?](#q19-what-is-the-optional-class)
    - [Q20: What is dependency injection?](#q20-what-is-dependency-injection)
    - [Q21: What is the `volatile` keyword?](#q21-what-is-the-volatile-keyword)
    - [Q22: What is `synchronized` keyword?](#q22-what-is-synchronized-keyword)
    - [Q23: What is a `ThreadLocal` variable?](#q23-what-is-a-threadlocal-variable)
    - [Q24: What is the difference between `String`, `StringBuilder`, and `StringBuffer`?](#q24-what-is-the-difference-between-string-stringbuilder-and-stringbuffer)
    - [Q25: What is the Java Memory Model?](#q25-what-is-the-java-memory-model)
    - [Q26: What are the different types of Garbage Collectors in Java?](#q26-what-are-the-different-types-of-garbage-collectors-in-java)
    - [Q27: What is ClassLoader?](#q27-what-is-classloader)
    - [Q28: What is the `transient` keyword?](#q28-what-is-the-transient-keyword)
    - [Q29: What is Serialization and Deserialization?](#q29-what-is-serialization-and-deserialization)
    - [Q30: What is `serialVersionUID`?](#q30-what-is-serialversionuid)
    - [Q31: What is Reflection?](#q31-what-is-reflection)
    - [Q32: What are Java Annotations?](#q32-what-are-java-annotations)
    - [Q33: What is `Enum` in Java?](#q33-what-is-enum-in-java)
    - [Q34: What is the Executor Framework?](#q34-what-is-the-executor-framework)
    - [Q35: What is `CompletableFuture`?](#q35-what-is-completablefuture)
    - [Q36: What is the Fork/Join Framework?](#q36-what-is-the-forkjoin-framework)
    - [Q37: What is the difference between `Comparator` and `Comparable`?](#q37-what-is-the-difference-between-comparator-and-comparable)
    - [Q38: What is the `default` method in interfaces?](#q38-what-is-the-default-method-in-interfaces)
    - [Q39: What is a Functional Interface?](#q39-what-is-a-functional-interface)
    - [Q40: What are the core Functional Interfaces in Java 8?](#q40-what-are-the-core-functional-interfaces-in-java-8)
    - [Q41: What is method reference?](#q41-what-is-method-reference)
    - [Q42: What is the Date/Time API (Java 8)?](#q42-what-is-the-datetime-api-java-8)
    - [Q43: What are Java Records (Java 14/16)?](#q43-what-are-java-records-java-1416)
    - [Q44: What are Sealed Classes (Java 15/17)?](#q44-what-are-sealed-classes-java-1517)
    - [Q45: What is Pattern Matching for `instanceof` (Java 14/16)?](#q45-what-is-pattern-matching-for-instanceof-java-1416)
    - [Q46: What are Virtual Threads (Java 21)?](#q46-what-are-virtual-threads-java-21)
    - [Q47: What is the difference between `Checked` and `Unchecked` Exceptions?](#q47-what-is-the-difference-between-checked-and-unchecked-exceptions)
    - [Q48: What is `try-with-resources`?](#q48-what-is-try-with-resources)
    - [Q49: What is `System.gc()`?](#q49-what-is-systemgc)
    - [Q50: What is the difference between `throw` and `throws`?](#q50-what-is-the-difference-between-throw-and-throws)
    - [Q51: What is Singleton Pattern?](#q51-what-is-singleton-pattern)
    - [Q52: What is Factory Pattern?](#q52-what-is-factory-pattern)
    - [Q53: What is Observer Pattern?](#q53-what-is-observer-pattern)
    - [Q54: What is Dependency Injection (DI)?](#q54-what-is-dependency-injection-di)
    - [Q55: What is Spring Framework?](#q55-what-is-spring-framework)
    - [Q56: What is Spring Boot?](#q56-what-is-spring-boot)
    - [Q57: What is `@Autowired`?](#q57-what-is-autowired)
    - [Q58: What is the difference between `@Component`, `@Service`, `@Repository`, and `@Controller`?](#q58-what-is-the-difference-between-component-service-repository-and-controller)
    - [Q59: What is JPA (Java Persistence API)?](#q59-what-is-jpa-java-persistence-api)
    - [Q60: What is the difference between `FetchType.LAZY` and `FetchType.EAGER`?](#q60-what-is-the-difference-between-fetchtypelazy-and-fetchtypeeager)
    - [Q61: What is Hibernate?](#q61-what-is-hibernate)
    - [Q62: What is the N+1 Select Problem?](#q62-what-is-the-n1-select-problem)
    - [Q63: What is JDBC?](#q63-what-is-jdbc)
    - [Q64: What is a Connection Pool?](#q64-what-is-a-connection-pool)
    - [Q65: What is REST?](#q65-what-is-rest)
    - [Q66: What is JSON?](#q66-what-is-json)
    - [Q67: What is Maven/Gradle?](#q67-what-is-mavengradle)
    - [Q68: What is JUnit?](#q68-what-is-junit)
    - [Q69: What is Mockito?](#q69-what-is-mockito)
    - [Q70: What is Log4j/SLF4J?](#q70-what-is-log4jslf4j)
    - [Q71: What is the difference between `Stack` and `Heap` memory in Java?](#q71-what-is-the-difference-between-stack-and-heap-memory-in-java)
    - [Q72: What is `OutOfMemoryError`?](#q72-what-is-outofmemoryerror)
    - [Q73: What is `StackOverflowError`?](#q73-what-is-stackoverflowerror)
    - [Q74: What is Double Checked Locking?](#q74-what-is-double-checked-locking)
    - [Q75: What is Immutable Class?](#q75-what-is-immutable-class)
    - [Q76: What is `String.intern()`?](#q76-what-is-stringintern)
    - [Q77: What is `System.out.println()`?](#q77-what-is-systemoutprintln)
    - [Q78: What is the difference between `PATH` and `CLASSPATH`?](#q78-what-is-the-difference-between-path-and-classpath)
    - [Q79: What is JIT (Just-In-Time) Compiler?](#q79-what-is-jit-just-in-time-compiler)
    - [Q80: What is the difference between `fail-fast` and `fail-safe` iterators?](#q80-what-is-the-difference-between-fail-fast-and-fail-safe-iterators)
    - [Q81: What is `BlockingQueue`?](#q81-what-is-blockingqueue)
    - [Q82: What is `CountDownLatch`?](#q82-what-is-countdownlatch)
    - [Q83: What is `CyclicBarrier`?](#q83-what-is-cyclicbarrier)
    - [Q84: What is `Semaphore`?](#q84-what-is-semaphore)
    - [Q85: What is `ReentrantLock`?](#q85-what-is-reentrantlock)
    - [Q86: What is `AtomicInteger`?](#q86-what-is-atomicinteger)
    - [Q87: What is the difference between `yield()`, `sleep()`, and `join()`?](#q87-what-is-the-difference-between-yield-sleep-and-join)
    - [Q88: What is Deadlock?](#q88-what-is-deadlock)
    - [Q89: How do you prevent Deadlock?](#q89-how-do-you-prevent-deadlock)
    - [Q90: What is Livelock?](#q90-what-is-livelock)
    - [Q91: What is Starvation?](#q91-what-is-starvation)
    - [Q92: What is Race Condition?](#q92-what-is-race-condition)
    - [Q93: What is Microservices Architecture?](#q93-what-is-microservices-architecture)
    - [Q94: What is API Gateway?](#q94-what-is-api-gateway)
    - [Q95: What is Circuit Breaker Pattern?](#q95-what-is-circuit-breaker-pattern)
    - [Q96: What is Service Discovery?](#q96-what-is-service-discovery)
    - [Q97: What is CAP Theorem?](#q97-what-is-cap-theorem)
    - [Q98: What is BASE property?](#q98-what-is-base-property)
    - [Q99: What is SOLID principles?](#q99-what-is-solid-principles)
    - [Q100: What is the future of Java?](#q100-what-is-the-future-of-java)


---
### Q1: What is the difference between the Java Development Kit (JDK), Java Runtime Environment (JRE), and Java Virtual Machine (JVM)?

**Answer:**
These three components are fundamental to the Java platform, and understanding their roles is essential for any Java developer.

**Java Virtual Machine (JVM)**
-   **Role:** The JVM is an abstract machine that provides a runtime environment in which Java bytecode can be executed.
-   **Function:**
    -   Loads code
    -   Verifies code
    -   Executes code
    -   Provides runtime environment
-   **Key Concept:** The JVM is platform-dependent, meaning there are different implementations for different operating systems. This is what makes Java a "write once, run anywhere" language.

**Java Runtime Environment (JRE)**
-   **Role:** The JRE is a software package that contains what is required to run a Java program. It includes the JVM, along with the Java Class Library (JCL) and other supporting files.
-   **Components:**
    -   JVM
    -   Java Class Library (core classes like `java.lang`, `java.util`, etc.)
-   **Use Case:** You need the JRE to run Java applications, but not to develop them.

**Java Development Kit (JDK)**
-   **Role:** The JDK is a full-featured software development kit for Java. It includes everything in the JRE, plus tools for developing, debugging, and monitoring Java applications.
-   **Components:**
    -   JRE (which includes the JVM)
    -   Development tools (e.g., `javac` compiler, `java` launcher, `jar` archiver, `javadoc` documentation generator)
-   **Use Case:** You need the JDK to develop Java applications.

**Relationship:**

`JDK = JRE + Development Tools`
`JRE = JVM + Java Class Library`

**Analogy:**
-   **JVM:** The engine of a car.
-   **JRE:** The car itself (you can drive it, but you can't build a new one with it).
-   **JDK:** A car factory (you have everything you need to build and drive cars).

**Diagram:**

```
+-------------------------------------------+
|                  JDK                      |
|  +-----------------------------------+    |
|  |                JRE                |    |
|  |  +---------------------------+    |    |
|  |  |            JVM            |    |    |
|  |  +---------------------------+    |    |
|  |                                   |    |
|  |      Java Class Library           |    |
|  +-----------------------------------+    |
|                                           |
|         Development Tools                 |
| (javac, jar, javadoc, etc.)               |
+-------------------------------------------+
```

### Q2: What is the difference between `==` and `.equals()`?

**Answer:**
-   `==`: A reference comparison, i.e., it checks if both objects point to the same memory location.
-   `.equals()`: A value comparison, i.e., it checks if the values in the objects are the same. By default, it behaves like `==`, but it's often overridden in classes to provide a meaningful comparison.

### Q3: What are the main principles of Object-Oriented Programming (OOP)?

**Answer:**
-   **Encapsulation:** Bundling of data with the methods that operate on that data.
-   **Abstraction:** Hiding the complex implementation details and showing only the essential features of the object.
-   **Inheritance:** A mechanism wherein a new class derives from an existing class.
-   **Polymorphism:** The ability of an object to take on many forms.

### Q4: What is the difference between an `abstract class` and an `interface`?

**Answer:**

| Feature | Abstract Class | Interface |
| :--- | :--- | :--- |
| **Methods** | Can have both abstract and concrete methods. | Can only have abstract methods (before Java 8). | 
| **Variables** | Can have final, non-final, static, and non-static variables. | Can only have static and final variables. |
| **Inheritance** | A class can inherit only one abstract class. | A class can implement multiple interfaces. |

### Q5: What is the `final` keyword in Java?

**Answer:**
-   **Final variable:** The value cannot be changed.
-   **Final method:** Cannot be overridden by a subclass.
-   **Final class:** Cannot be inherited.

### Q6: What is the `static` keyword in Java?

**Answer:**
-   **Static variable:** Belongs to the class rather than an instance of the class. Shared among all instances.
-   **Static method:** Belongs to the class and can be called without creating an instance.

### Q7: What is method overloading and method overriding?

**Answer:**
-   **Overloading:** When two or more methods in the same class have the same name but different parameters.
-   **Overriding:** When a method in a subclass has the same name and parameters as a method in its superclass.

### Q8: What is the Java Collections Framework?

**Answer:**
The Java Collections Framework is a set of classes and interfaces that implement commonly reusable collection data structures like `List`, `Set`, and `Map`.

### Q9: What is the difference between `ArrayList` and `LinkedList`?

**Answer:**
-   `ArrayList`: Implemented as a dynamic array. Better for storing and accessing data.
-   `LinkedList`: Implemented as a doubly-linked list. Better for manipulating data (insertion and deletion).

### Q10: What is the difference between `HashMap` and `HashTable`?

**Answer:**
-   `HashMap`: Not synchronized, allows one null key and multiple null values.
-   `HashTable`: Synchronized, does not allow null keys or values.

### Q11: What is exception handling in Java?

**Answer:**
Exception handling is a mechanism to handle runtime errors such as `ClassNotFoundException`, `IOException`, `SQLException`, etc. It uses `try`, `catch`, `finally`, `throw`, and `throws` keywords.

### Q12: What is the difference between checked and unchecked exceptions?

**Answer:**
-   **Checked exceptions:** Exceptions that are checked at compile-time. The programmer must handle them using `try-catch` or declare them with `throws`.
-   **Unchecked exceptions:** Exceptions that are not checked at compile-time. They are subclasses of `RuntimeException`.

### Q13: What is garbage collection in Java?

**Answer:**
Garbage collection is the process of automatically freeing up memory that is no longer in use by the program. The JVM's garbage collector runs in the background to reclaim memory.

### Q14: What is multithreading in Java?

**Answer:**
Multithreading is a process of executing multiple threads simultaneously. It allows a program to be more efficient by doing multiple things at the same time.

### Q15: What is the difference between `Runnable` and `Thread`?

**Answer:**
-   `Thread`: A class that you can extend to create a thread.
-   `Runnable`: An interface that you can implement to create a thread. Implementing `Runnable` is generally preferred as it allows the class to extend other classes.

### Q16: What are generics in Java?

**Answer:**
Generics enable types (classes and interfaces) to be parameters when defining classes, interfaces, and methods. This provides compile-time type safety and avoids the need for casting.

### Q17: What are lambda expressions in Java?

**Answer:**
Lambda expressions, introduced in Java 8, provide a clear and concise way to represent one method interface using an expression. They are often used with functional interfaces.

### Q18: What is the Stream API?

**Answer:**
The Stream API, also introduced in Java 8, is used to process collections of objects. A stream is a sequence of objects that supports various methods which can be pipelined to produce the desired result.

### Q19: What is the `Optional` class?

**Answer:**
`Optional` is a container object which may or may not contain a non-null value. It's used to represent the absence of a value, as an alternative to `null` references.

### Q20: What is dependency injection?

**Answer:**
Dependency Injection is a design pattern in which an object receives other objects that it depends on. This pattern is often used in frameworks like Spring to achieve Inversion of Control.
### Q21: What is the `volatile` keyword?
**Difficulty: Advanced**

**Answer:**
The `volatile` keyword guarantees visibility of changes to variables across threads. It prevents the compiler and CPU from reordering instructions or caching the variable in registers/CPU caches, forcing reads/writes to main memory. It does *not* guarantee atomicity.

### Q22: What is `synchronized` keyword?
**Difficulty: Medium**

**Answer:**
It ensures that only one thread can access a block of code or object at a time. It can be applied to instance methods (locks on `this`), static methods (locks on `Class` object), or blocks (locks on a specified object).

### Q23: What is a `ThreadLocal` variable?
**Difficulty: Advanced**

**Answer:**
A variable that provides a separate storage slot for each thread that accesses it. Each thread sees its own independently initialized copy of the variable.
```java
ThreadLocal<Integer> threadId = ThreadLocal.withInitial(() -> 0);
```

### Q24: What is the difference between `String`, `StringBuilder`, and `StringBuffer`?
**Difficulty: Easy**

**Answer:**
- `String`: Immutable. Slow for concatenations. Thread-safe (because immutable).
- `StringBuilder`: Mutable. Fast. Not thread-safe.
- `StringBuffer`: Mutable. Slower than StringBuilder. Thread-safe (synchronized).

### Q25: What is the Java Memory Model?
**Difficulty: Advanced**

**Answer:**
It describes how threads interact through memory. It defines the rules for visibility (happens-before relationship), atomicity, and ordering of operations.

### Q26: What are the different types of Garbage Collectors in Java?
**Difficulty: Advanced**

**Answer:**
- Serial GC: Single-threaded (for small apps).
- Parallel GC: Multi-threaded (throughput-oriented).
- G1 GC (Garbage First): Low-pause, splits heap into regions. Default in modern Java.
- ZGC: Low-latency, scalable (sub-millisecond pauses).
- Shenandoah: Ultra-low pause time.

### Q27: What is ClassLoader?
**Difficulty: Advanced**

**Answer:**
Part of the JVM that dynamically loads Java classes into the JVM. Types:
- Bootstrap ClassLoader (loads core libs).
- Extension/Platform ClassLoader.
- Application/System ClassLoader.

### Q28: What is the `transient` keyword?
**Difficulty: Medium**

**Answer:**
Used in serialization. Variables marked as `transient` are not serialized (saved) when the object is converted to a byte stream.

### Q29: What is Serialization and Deserialization?
**Difficulty: Medium**

**Answer:**
- **Serialization:** Converting an object into a byte stream.
- **Deserialization:** Reconstructing the object from the byte stream.
Classes must implement `Serializable` interface.

### Q30: What is `serialVersionUID`?
**Difficulty: Medium**

**Answer:**
A unique identifier for `Serializable` classes. It ensures that the sender and receiver of a serialized object have loaded classes for that object that are compatible with respect to serialization.

### Q31: What is Reflection?
**Difficulty: Advanced**

**Answer:**
A feature that allows code to inspect and modify the runtime behavior of applications (classes, interfaces, fields, methods) at runtime.

### Q32: What are Java Annotations?
**Difficulty: Medium**

**Answer:**
Metadata about the program that is not part of the program itself. They have no direct effect on the operation of the code they annotate but can be used by compilers or runtime environments (e.g., `@Override`, `@Deprecated`, `@Test`).

### Q33: What is `Enum` in Java?
**Difficulty: Easy**

**Answer:**
A special data type that enables for a variable to be a set of predefined constants. Enums in Java are full-fledged classes.

### Q34: What is the Executor Framework?
**Difficulty: Advanced**

**Answer:**
A framework for asynchronous task execution. It separates task creation from execution.
- `ExecutorService`: Manages thread pools (`newFixedThreadPool`, `newCachedThreadPool`).
- `Future`: Represents the result of an asynchronous computation.

### Q35: What is `CompletableFuture`?
**Difficulty: Advanced**

**Answer:**
Introduced in Java 8, it represents a future result of an asynchronous computation and provides methods to chain computations, combine futures, and handle errors.

### Q36: What is the Fork/Join Framework?
**Difficulty: Advanced**

**Answer:**
Designed for work-stealing algorithms. It recursively breaks a task into smaller subtasks (fork) and then combines the results (join). Used by parallel streams.

### Q37: What is the difference between `Comparator` and `Comparable`?
**Difficulty: Medium**

**Answer:**
- `Comparable`: Interface (`compareTo`) used to define the *natural ordering* of objects. The class itself implements it.
- `Comparator`: Interface (`compare`) used to define *custom ordering*. Implemented by a separate class or lambda.

### Q38: What is the `default` method in interfaces?
**Difficulty: Medium**

**Answer:**
Introduced in Java 8, allows interfaces to have methods with implementation. Enables backward compatibility when adding new methods to interfaces.

### Q39: What is a Functional Interface?
**Difficulty: Medium**

**Answer:**
An interface with exactly one abstract method. Can be implemented using Lambda expressions. Annotated with `@FunctionalInterface`. Examples: `Runnable`, `Callable`, `Comparator`.

### Q40: What are the core Functional Interfaces in Java 8?
**Difficulty: Medium**

**Answer:**
- `Predicate<T>`: `T -> boolean` (test)
- `Consumer<T>`: `T -> void` (accept)
- `Supplier<T>`: `() -> T` (get)
- `Function<T, R>`: `T -> R` (apply)

### Q41: What is method reference?
**Difficulty: Easy**

**Answer:**
Shorthand syntax for a lambda expression that executes just ONE method. `ClassName::methodName`.

### Q42: What is the Date/Time API (Java 8)?
**Difficulty: Medium**

**Answer:**
A modern, immutable, thread-safe API for date and time.
- `LocalDate`, `LocalTime`, `LocalDateTime`
- `ZonedDateTime`
- `Period`, `Duration`
Replaces the old, mutable `java.util.Date` and `Calendar`.

### Q43: What are Java Records (Java 14/16)?
**Difficulty: Medium**

**Answer:**
A concise way to create immutable data-carrying classes.
```java
public record Point(int x, int y) {}
```
Automatically generates constructor, getters, `equals`, `hashCode`, and `toString`.

### Q44: What are Sealed Classes (Java 15/17)?
**Difficulty: Advanced**

**Answer:**
Classes or interfaces that restrict which other classes or interfaces may extend or implement them.
```java
public sealed class Shape permits Circle, Square {}
```

### Q45: What is Pattern Matching for `instanceof` (Java 14/16)?
**Difficulty: Medium**

**Answer:**
Allows testing and casting in a single step.
```java
if (obj instanceof String s) {
    System.out.println(s.length());
}
```

### Q46: What are Virtual Threads (Java 21)?
**Difficulty: Advanced**

**Answer:**
Lightweight threads managed by the JVM (Project Loom). They map M virtual threads to N carrier (OS) threads, allowing millions of concurrent tasks with high throughput.

### Q47: What is the difference between `Checked` and `Unchecked` Exceptions?
**Difficulty: Medium**

**Answer:**
- **Checked:** Inherit from `Exception`. Must be handled (`try-catch`) or declared (`throws`). Compile-time check. (e.g., `IOException`).
- **Unchecked:** Inherit from `RuntimeException`. No need to handle explicitly. (e.g., `NullPointerException`).

### Q48: What is `try-with-resources`?
**Difficulty: Medium**

**Answer:**
Introduced in Java 7. Automatically closes resources (like streams, connections) that implement `AutoCloseable`.
```java
try (BufferedReader br = new BufferedReader(new FileReader(path))) {
    return br.readLine();
}
```

### Q49: What is `System.gc()`?
**Difficulty: Easy**

**Answer:**
A hint to the JVM to run the Garbage Collector. It does not guarantee execution.

### Q50: What is the difference between `throw` and `throws`?
**Difficulty: Easy**

**Answer:**
- `throw`: Used to explicitly throw an exception within a method.
- `throws`: Used in method signature to declare that the method might throw exceptions.

### Q51: What is Singleton Pattern?
**Difficulty: Medium**

**Answer:**
Ensures a class has only one instance and provides a global point of access.
```java
public class Singleton {
    private static final Singleton INSTANCE = new Singleton();
    private Singleton() {}
    public static Singleton getInstance() { return INSTANCE; }
}
```

### Q52: What is Factory Pattern?
**Difficulty: Medium**

**Answer:**
Creates objects without specifying the exact class of object that will be created.

### Q53: What is Observer Pattern?
**Difficulty: Medium**

**Answer:**
Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified. Used in event handling.

### Q54: What is Dependency Injection (DI)?
**Difficulty: Advanced**

**Answer:**
A design pattern where an object's dependencies are "injected" into it (by a framework or container) rather than the object creating them itself. Inversion of Control (IoC).

### Q55: What is Spring Framework?
**Difficulty: Advanced**

**Answer:**
A comprehensive framework for enterprise Java development. Provides DI, AOP, transaction management, MVC, and more.

### Q56: What is Spring Boot?
**Difficulty: Medium**

**Answer:**
An extension of Spring that simplifies setup and development. Provides "starter" dependencies, auto-configuration, and an embedded server (Tomcat).

### Q57: What is `@Autowired`?
**Difficulty: Medium**

**Answer:**
Spring annotation for dependency injection. Can be used on constructors, setters, or fields.

### Q58: What is the difference between `@Component`, `@Service`, `@Repository`, and `@Controller`?
**Difficulty: Medium**

**Answer:**
They are all stereotypes for Spring beans.
- `@Component`: Generic.
- `@Service`: Business logic.
- `@Repository`: Data access (translates exceptions).
- `@Controller`: Web controller.

### Q59: What is JPA (Java Persistence API)?
**Difficulty: Advanced**

**Answer:**
A specification for accessing, persisting, and managing data between Java objects and a relational database. Hibernate is a popular implementation.

### Q60: What is the difference between `FetchType.LAZY` and `FetchType.EAGER`?
**Difficulty: Advanced**

**Answer:**
- `LAZY`: Data is loaded only when accessed (getter called).
- `EAGER`: Data is loaded immediately with the parent entity.

### Q61: What is Hibernate?
**Difficulty: Advanced**

**Answer:**
An ORM (Object-Relational Mapping) framework that maps Java classes to database tables and Java data types to SQL data types.

### Q62: What is the N+1 Select Problem?
**Difficulty: Advanced**

**Answer:**
A performance issue in ORMs where 1 query retrieves the parent entities, and then N queries are executed to fetch related child entities for each parent. Solved using `JOIN FETCH`.

### Q63: What is JDBC?
**Difficulty: Medium**

**Answer:**
Java Database Connectivity. An API for connecting and executing queries on a database.

### Q64: What is a Connection Pool?
**Difficulty: Advanced**

**Answer:**
A cache of database connections maintained so that connections can be reused when future requests to the database are required. Reduces the overhead of establishing connections. (e.g., HikariCP).

### Q65: What is REST?
**Difficulty: Medium**

**Answer:**
Representational State Transfer. An architectural style for designing networked applications. Uses HTTP methods (GET, POST, PUT, DELETE).

### Q66: What is JSON?
**Difficulty: Easy**

**Answer:**
JavaScript Object Notation. A lightweight data-interchange format.

### Q67: What is Maven/Gradle?
**Difficulty: Medium**

**Answer:**
Build automation tools. They manage dependencies, compilation, packaging, and testing.

### Q68: What is JUnit?
**Difficulty: Easy**

**Answer:**
A unit testing framework for Java.

### Q69: What is Mockito?
**Difficulty: Medium**

**Answer:**
A mocking framework for unit tests in Java. Allows creating mock objects to simulate dependencies.

### Q70: What is Log4j/SLF4J?
**Difficulty: Easy**

**Answer:**
Logging libraries. SLF4J is a facade, Log4j/Logback are implementations.

### Q71: What is the difference between `Stack` and `Heap` memory in Java?
**Difficulty: Medium**

**Answer:**
- **Stack:** Stores method frames, local primitive variables, and reference variables. Thread-safe.
- **Heap:** Stores Objects. Shared by all threads.

### Q72: What is `OutOfMemoryError`?
**Difficulty: Medium**

**Answer:**
Thrown when the JVM cannot allocate an object because it is out of memory, and no more memory could be made available by the garbage collector.

### Q73: What is `StackOverflowError`?
**Difficulty: Medium**

**Answer:**
Thrown when the stack size is exceeded, typically due to deep or infinite recursion.

### Q74: What is Double Checked Locking?
**Difficulty: Advanced**

**Answer:**
A pattern used to reduce the overhead of acquiring a lock by first testing the locking criterion (the "lock hint") without actually acquiring the lock. Used in Singleton.

### Q75: What is Immutable Class?
**Difficulty: Medium**

**Answer:**
A class whose instances cannot be modified after creation. Example: `String`, `Integer`. created by making class `final`, fields `private final`, and no setters.

### Q76: What is `String.intern()`?
**Difficulty: Advanced**

**Answer:**
Returns a canonical representation for the string object. It looks up the string in the String Constant Pool. If found, returns it; otherwise adds it to the pool.

### Q77: What is `System.out.println()`?
**Difficulty: Easy**

**Answer:**
- `System`: A class.
- `out`: A static final field (PrintStream).
- `println()`: A method of PrintStream.

### Q78: What is the difference between `PATH` and `CLASSPATH`?
**Difficulty: Easy**

**Answer:**
- `PATH`: System variable used by OS to locate executables (like `javac`, `java`).
- `CLASSPATH`: Environment variable used by JVM to locate `.class` files and libraries.

### Q79: What is JIT (Just-In-Time) Compiler?
**Difficulty: Advanced**

**Answer:**
A component of the JVM that improves performance by compiling bytecodes to native machine code at runtime.

### Q80: What is the difference between `fail-fast` and `fail-safe` iterators?
**Difficulty: Advanced**

**Answer:**
- `fail-fast`: Throws `ConcurrentModificationException` if collection is modified during iteration (e.g., `ArrayList`).
- `fail-safe`: Works on a copy or snapshot, does not throw exception (e.g., `ConcurrentHashMap`).

### Q81: What is `BlockingQueue`?
**Difficulty: Medium**

**Answer:**
A queue that supports operations that wait for the queue to become non-empty when retrieving an element, and wait for space to become available when storing an element.

### Q82: What is `CountDownLatch`?
**Difficulty: Advanced**

**Answer:**
A synchronization aid that allows one or more threads to wait until a set of operations being performed in other threads completes.

### Q83: What is `CyclicBarrier`?
**Difficulty: Advanced**

**Answer:**
A synchronization aid that allows a set of threads to all wait for each other to reach a common barrier point.

### Q84: What is `Semaphore`?
**Difficulty: Advanced**

**Answer:**
A synchronization primitive that maintains a set of permits. Used to control access to a shared resource.

### Q85: What is `ReentrantLock`?
**Difficulty: Advanced**

**Answer:**
A lock with the same basic behavior as the implicit monitor lock (`synchronized`) but with extended capabilities (tryLock, interruptible lock, fair lock).

### Q86: What is `AtomicInteger`?
**Difficulty: Medium**

**Answer:**
An `int` value that may be updated atomically. Used in non-blocking algorithms.

### Q87: What is the difference between `yield()`, `sleep()`, and `join()`?
**Difficulty: Medium**

**Answer:**
- `yield()`: Hints scheduler that thread is willing to yield processor.
- `sleep()`: Pauses execution for a time.
- `join()`: Waits for another thread to die.

### Q88: What is Deadlock?
**Difficulty: Medium**

**Answer:**
A situation where two or more threads are blocked forever, waiting for each other.

### Q89: How do you prevent Deadlock?
**Difficulty: Advanced**

**Answer:**
- Avoid nested locks.
- Lock in a consistent order.
- Use `tryLock()` with timeout.

### Q90: What is Livelock?
**Difficulty: Advanced**

**Answer:**
A situation where threads are not blocked but are unable to make progress because they keep responding to each other's action.

### Q91: What is Starvation?
**Difficulty: Medium**

**Answer:**
When a thread is unable to gain regular access to shared resources and is unable to make progress (e.g., low priority thread).

### Q92: What is Race Condition?
**Difficulty: Medium**

**Answer:**
Occurs when multiple threads access shared data and try to change it at the same time.

### Q93: What is Microservices Architecture?
**Difficulty: Advanced**

**Answer:**
An architectural style where an application is structured as a collection of small, autonomous services, modeled around a business domain.

### Q94: What is API Gateway?
**Difficulty: Advanced**

**Answer:**
A server that acts as an entry point for clients. It routes requests to appropriate microservices.

### Q95: What is Circuit Breaker Pattern?
**Difficulty: Advanced**

**Answer:**
Prevents an application from repeatedly trying to execute an operation that's likely to fail. (e.g., Resilience4j).

### Q96: What is Service Discovery?
**Difficulty: Advanced**

**Answer:**
Automatic detection of devices and services on a network. (e.g., Eureka, Consul).

### Q97: What is CAP Theorem?
**Difficulty: Advanced**

**Answer:**
It states that a distributed data store can only provide two of the following three guarantees:
- **C**onsistency
- **A**vailability
- **P**artition Tolerance

### Q98: What is BASE property?
**Difficulty: Advanced**

**Answer:**
- **B**asically **A**vailable
- **S**oft state
- **E**ventual consistency
Alternative to ACID for NoSQL/Distributed systems.

### Q99: What is SOLID principles?
**Difficulty: Advanced**

**Answer:**
- **S**ingle Responsibility
- **O**pen/Closed
- **L**iskov Substitution
- **I**nterface Segregation
- **D**ependency Inversion

### Q100: What is the future of Java?
**Difficulty: Easy**

**Answer:**
Java continues to evolve rapidly with a 6-month release cycle. Focus areas include:
- Project Loom (Virtual Threads)
- Project Valhalla (Value Types)
- Project Panama (Native Interop)
- Project Amber (Language Features)
It remains a dominant language for enterprise, cloud, and big data.
