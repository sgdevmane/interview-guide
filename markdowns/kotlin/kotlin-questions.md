# Kotlin Interview Questions

## Table of Contents
1. [What are the key features of Kotlin that make it a preferred language over Java for Android development?](#q1-what-are-the-key-features-of-kotlin-that-make-it-a-preferred-language-over-java-for-android-development)
2. [What are coroutines in Kotlin and how do they compare to traditional threads?](#q2-what-are-coroutines-in-kotlin-and-how-do-they-compare-to-traditional-threads)
3. [Explain extension functions in Kotlin.](#q3-explain-extension-functions-in-kotlin)
4. [What are data classes in Kotlin?](#q4-what-are-data-classes-in-kotlin)
5. [What is null safety in Kotlin?](#q5-what-is-null-safety-in-kotlin)
6. [What are sealed classes in Kotlin?](#q6-what-are-sealed-classes-in-kotlin)
7. [Explain the difference between `val` and `var`.](#q7-explain-the-difference-between-val-and-var)
8. [What are higher-order functions in Kotlin?](#q8-what-are-higher-order-functions-in-kotlin)
9. [What is the `lateinit` keyword used for?](#q9-what-is-the-lateinit-keyword-used-for)
10. [What is the difference between `lazy` and `lateinit`?](#q10-what-is-the-difference-between-lazy-and-lateinit)
11. [What are inline functions in Kotlin?](#q11-what-are-inline-functions-in-kotlin)
12. [What is the `when` expression in Kotlin?](#q12-what-is-the-when-expression-in-kotlin)
13. [What are companion objects?](#q13-what-are-companion-objects)
14. [What is the Elvis operator (`?:`)?](#q14-what-is-the-elvis-operator-)
15. [What are destructuring declarations?](#q15-what-are-destructuring-declarations)
16. [What is the difference between `==` and `===`?](#q16-what-is-the-difference-between--and-)
17. [What are type aliases in Kotlin?](#q17-what-are-type-aliases-in-kotlin)
18. [What is the `Unit` type in Kotlin?](#q18-what-is-the-unit-type-in-kotlin)
19. [What are backing properties?](#q19-what-are-backing-properties)
20. [What is the difference between `List` and `MutableList`?](#q20-what-is-the-difference-between-list-and-mutablelist)

---

### Q1: What are the key features of Kotlin that make it a preferred language over Java for Android development?

**Answer:**
Kotlin offers several features that address common Java pain points, leading to more concise, safer, and more readable code. These features make it a modern and powerful alternative for Android development.

**Key Features:**

1.  **Null Safety:** Kotlin's type system is designed to eliminate `NullPointerException` by distinguishing between nullable and non-nullable references.

    ```kotlin
    // Non-nullable (cannot be null)
    var a: String = "abc"
    // a = null // Compilation error

    // Nullable (can be null)
    var b: String? = "xyz"
    b = null // OK

    // Safe calls
    val length = b?.length // Returns length or null

    // Elvis operator
    val len = b?.length ?: -1 // Returns length or -1 if b is null
    ```

2.  **Coroutines:** Kotlin provides built-in support for asynchronous programming with coroutines, which simplifies non-blocking code and improves app responsiveness.

    ```kotlin
    import kotlinx.coroutines.*

    fun main() = runBlocking {
        launch {
            delay(1000L)
            println("World!")
        }
        println("Hello,")
    }
    ```

3.  **Extension Functions:** You can extend existing classes with new functionality without inheriting from them.

    ```kotlin
    fun String.addExclamation(): String {
        return this + "!"
    }

    val message = "Hello"
    println(message.addExclamation()) // Output: Hello!
    ```

4.  **Data Classes:** Kotlin's `data` classes automatically generate boilerplate code for `equals()`, `hashCode()`, `toString()`, and `copy()`.

    ```kotlin
    data class User(val name: String, val age: Int)

    val user1 = User("Alice", 30)
    val user2 = user1.copy(name = "Bob")

    println(user1) // Output: User(name=Alice, age=30)
    println(user2) // Output: User(name=Bob, age=30)
    ```

5.  **Smart Casts:** The compiler automatically casts variables after a type check, reducing redundant casting.

    ```kotlin
    fun process(obj: Any) {
        if (obj is String) {
            // obj is automatically cast to String
            println("Length: ${obj.length}")
        }
    }
    ```

6.  **Interoperability with Java:** Kotlin is 100% interoperable with Java, allowing you to use existing Java libraries and frameworks seamlessly.

### Q2: What are coroutines in Kotlin and how do they compare to traditional threads?

**Answer:**
Coroutines are a concurrency design pattern that you can use in Kotlin to simplify code that executes asynchronously. They are lightweight threads, but not threads themselves. They run on top of threads but are much more efficient in terms of memory and context switching.

| Feature | Coroutines | Threads |
| :--- | :--- | :--- |
| **Resource Usage** | Lightweight, share a pool of threads. | Heavyweight, each has its own stack. |
| **Context Switching** | Fast, managed by the Kotlin runtime. | Slow, managed by the OS. |
| **Programming Model** | Structured concurrency, easier to manage. | Prone to race conditions and deadlocks. |

```kotlin
import kotlinx.coroutines.*

fun main() = runBlocking {
    launch {
        delay(1000L)
        println("World!")
    }
    print("Hello, ")
}
```

### Q3: Explain extension functions in Kotlin.

**Answer:**
Extension functions allow you to add new functions to existing classes without having to inherit from them. This is a powerful feature for code organization and readability.

```kotlin
fun String.addExclamation(): String {
    return this + "!"
}

val greeting = "Hello"
println(greeting.addExclamation()) // Prints "Hello!"
```

### Q4: What are data classes in Kotlin?

**Answer:**
Data classes are a concise way to create classes that are primarily used to hold data. The compiler automatically generates useful methods like `equals()`, `hashCode()`, `toString()`, `copy()`, and `componentN()` functions.

```kotlin
data class User(val name: String, val age: Int)
```

### Q5: What is null safety in Kotlin?

**Answer:**
Kotlin's type system is designed to eliminate the danger of null references, also known as the "billion-dollar mistake." It distinguishes between nullable and non-nullable types.

-   **Non-nullable types:** `String` (cannot hold `null`)
-   **Nullable types:** `String?` (can hold `null`)

### Q6: What are sealed classes in Kotlin?

**Answer:**
Sealed classes are used for representing restricted class hierarchies, when a value can have one of the types from a limited set, but cannot have any other type. They are often used in `when` expressions for exhaustive checks.

### Q7: Explain the difference between `val` and `var`.

**Answer:**
-   `val` is used for read-only (immutable) variables.
-   `var` is used for mutable variables.

### Q8: What are higher-order functions in Kotlin?

**Answer:**
Higher-order functions are functions that take other functions as parameters or return them.

```kotlin
fun operate(x: Int, y: Int, operation: (Int, Int) -> Int): Int {
    return operation(x, y)
}

val sum = operate(2, 3) { a, b -> a + b }
```

### Q9: What is the `lateinit` keyword used for?

**Answer:**
`lateinit` is used for non-null properties that are initialized after the object's construction. It's a promise to the compiler that the property will be initialized before it's accessed.

### Q10: What is the difference between `lazy` and `lateinit`?

**Answer:**
-   `lateinit`: For mutable properties (`var`), can be initialized multiple times.
-   `lazy`: For immutable properties (`val`), initialized only once when first accessed.

### Q11: What are inline functions in Kotlin?

**Answer:**
Inline functions are a feature that can improve the performance of higher-order functions by avoiding the overhead of creating function objects. The compiler copies the code of the inline function to the call site.

### Q12: What is the `when` expression in Kotlin?

**Answer:**
The `when` expression is a more powerful and flexible replacement for the traditional `switch` statement. It can be used as either a statement or an expression.

### Q13: What are companion objects?

**Answer:**
A companion object is an object that is common to all instances of a class. It's similar to static members in Java.

### Q14: What is the Elvis operator (`?:`)?

**Answer:**
The Elvis operator is used to provide a default value for a nullable type if it's `null`.

```kotlin
val name: String? = null
val displayName = name ?: "Guest"
```

### Q15: What are destructuring declarations?

**Answer:**
Destructuring declarations allow you to unpack a single object into multiple variables.

```kotlin
val (name, age) = User("Alice", 30)
```

### Q16: What is the difference between `==` and `===`?

**Answer:**
-   `==`: Checks for structural equality (calls `equals()`).
-   `===`: Checks for referential equality (checks if two references point to the same object).

### Q17: What are type aliases in Kotlin?

**Answer:**
Type aliases provide alternative names for existing types. They are useful for shortening long generic types or for giving more descriptive names.

### Q18: What is the `Unit` type in Kotlin?

**Answer:**
`Unit` is a type that corresponds to `void` in Java. It indicates that a function does not return any value.

### Q19: What are backing properties?

**Answer:**
Backing properties are a way to provide a private property that is exposed as a read-only public property.

```kotlin
private val _items = mutableListOf<String>()
val items: List<String> = _items
```

### Q20: What is the difference between `List` and `MutableList`?

**Answer:**
-   `List`: An immutable, read-only list.
-   `MutableList`: A list that can be modified (add, remove, update elements).
### Q21: What are Data Classes?
**Difficulty: Easy**

**Answer:**
Classes whose main purpose is to hold data. Kotlin generates `equals()`, `hashCode()`, `toString()`, `copy()`, and `componentN()` functions automatically.
```kotlin
data class User(val name: String, val age: Int)
```

### Q22: What is the `sealed` class?
**Difficulty: Medium**

**Answer:**
A class that restricts class hierarchies. All subclasses must be known at compile time. Useful for representing restricted class hierarchies (like an `Result` type or UI states).
```kotlin
sealed class Result
data class Success(val data: String) : Result()
object Error : Result()
```

### Q23: What are Object Declarations (`object`)?
**Difficulty: Easy**

**Answer:**
Defines a singleton class.
```kotlin
object Database {
    val name = "MainDB"
}
```

### Q24: What are Companion Objects?
**Difficulty: Medium**

**Answer:**
An object scoped to an instance of a class. It is used to hold static members (like factory methods or constants).
```kotlin
class MyClass {
    companion object {
        fun create(): MyClass = MyClass()
    }
}
```

### Q25: What are Extension Functions?
**Difficulty: Medium**

**Answer:**
Ability to extend a class with new functionality without inheriting from it.
```kotlin
fun String.addExclamation() = this + "!"
```

### Q26: What are Higher-Order Functions?
**Difficulty: Medium**

**Answer:**
Functions that take other functions as parameters or return a function.
```kotlin
fun operate(x: Int, op: (Int) -> Int): Int = op(x)
```

### Q27: What is a Lambda Expression?
**Difficulty: Easy**

**Answer:**
A function literal, i.e., a function that is not declared but passed immediately as an expression.
```kotlin
val sum = { x: Int, y: Int -> x + y }
```

### Q28: What is the `it` keyword?
**Difficulty: Easy**

**Answer:**
The implicit name of a single parameter in a lambda expression.
```kotlin
list.map { it * 2 }
```

### Q29: What are Coroutines?
**Difficulty: Advanced**

**Answer:**
Lightweight threads that allow writing asynchronous, non-blocking code in a sequential style. They are suspendable computations.

### Q30: What is a `suspend` function?
**Difficulty: Medium**

**Answer:**
A function that can be paused and resumed. It can only be called from a coroutine or another suspend function.

### Q31: What is `launch` vs `async`?
**Difficulty: Medium**

**Answer:**
- `launch`: Starts a new coroutine and doesn't return a result (returns `Job`). "Fire and forget".
- `async`: Starts a new coroutine and returns a result (returns `Deferred<T>`). You can call `.await()` on it.

### Q32: What is `Dispatchers` in Coroutines?
**Difficulty: Medium**

**Answer:**
Determines what thread or thread pool the coroutine runs on.
- `Dispatchers.Main`: UI thread.
- `Dispatchers.IO`: I/O operations (network, disk).
- `Dispatchers.Default`: CPU-intensive tasks.

### Q33: What is `withContext`?
**Difficulty: Medium**

**Answer:**
Used to switch the context (dispatcher) of a coroutine. It suspends until the block completes.
```kotlin
withContext(Dispatchers.IO) { ... }
```

### Q34: What is Flow?
**Difficulty: Advanced**

**Answer:**
A cold asynchronous data stream that sequentially emits values and completes normally or with an exception. Similar to RxJava Observables.

### Q35: What is `StateFlow` vs `SharedFlow`?
**Difficulty: Advanced**

**Answer:**
- `StateFlow`: A state-holder observable flow that emits the current and new state updates to its collectors. Has an initial value. Hot flow.
- `SharedFlow`: A hot flow that emits values to all consumers that collect from it. Highly configurable (replay, buffer).

### Q36: What is the difference between `val` and `const val`?
**Difficulty: Easy**

**Answer:**
- `val`: Read-only variable. Value is determined at runtime.
- `const val`: Compile-time constant. Must be top-level or in an object.

### Q37: What is `lateinit`?
**Difficulty: Medium**

**Answer:**
Allows initializing a non-null property later. Used mostly for dependency injection or unit testing. Throws exception if accessed before initialization.

### Q38: What is `by lazy`?
**Difficulty: Medium**

**Answer:**
Delegate for lazy initialization. The value is computed only on the first access and cached for subsequent accesses.
```kotlin
val heavy by lazy { loadHeavyResource() }
```

### Q39: What is Delegation?
**Difficulty: Medium**

**Answer:**
A design pattern where an object handles a request by delegating it to a second object (the delegate). Kotlin supports Class Delegation (`by` clause) and Property Delegation.

### Q40: What are Scope Functions?
**Difficulty: Medium**

**Answer:**
Functions that execute a block of code within the context of an object. `let`, `run`, `with`, `apply`, `also`.

### Q41: Explain `let` vs `run` vs `apply` vs `also` vs `with`.
**Difficulty: Advanced**

**Answer:**
| Function | Object Reference | Return Value | Use Case |
| :--- | :--- | :--- | :--- |
| `let` | `it` | Lambda result | Null checks, mapping |
| `run` | `this` | Lambda result | Configuring and computing |
| `with` | `this` | Lambda result | Calling methods on object |
| `apply` | `this` | Object itself | Object configuration |
| `also` | `it` | Object itself | Side effects (logging) |

### Q42: What is Destructuring Declarations?
**Difficulty: Easy**

**Answer:**
Unpacking a single object into multiple variables.
```kotlin
val (name, age) = user
```

### Q43: What is Operator Overloading?
**Difficulty: Medium**

**Answer:**
Providing implementations for a predefined set of operators (like `+`, `-`, `*`) using functions with the `operator` modifier.

### Q44: What is Infix Notation?
**Difficulty: Easy**

**Answer:**
Calling a function without the dot and parentheses.
```kotlin
infix fun Int.times(str: String) = str.repeat(this)
2 times "Bye "
```

### Q45: What is `inline` function?
**Difficulty: Advanced**

**Answer:**
Instructs the compiler to copy the function's code into the call site. Reduces overhead for higher-order functions (lambdas).

### Q46: What is `reified` type parameter?
**Difficulty: Advanced**

**Answer:**
Allows accessing the type passed as a parameter at runtime in inline functions.
```kotlin
inline fun <reified T> isType(value: Any) = value is T
```

### Q47: What is `open` keyword?
**Difficulty: Easy**

**Answer:**
Classes and methods in Kotlin are `final` by default. `open` allows them to be inherited or overridden.

### Q48: What is `internal` visibility modifier?
**Difficulty: Easy**

**Answer:**
Visible only within the same module (e.g., Gradle module, IntelliJ module).

### Q49: What is the difference between `==` and `===`?
**Difficulty: Easy**

**Answer:**
- `==`: Structural equality (calls `equals()`).
- `===`: Referential equality (checks if references point to the same object).

### Q50: What is Platform Type?
**Difficulty: Medium**

**Answer:**
Types returned from Java code (`T!`). Kotlin doesn't know if it's nullable or non-nullable, so it relaxes null-safety checks.

### Q51: What is Elvis Operator (`?:`)?
**Difficulty: Easy**

**Answer:**
Returns the left expression if not null, otherwise returns the right expression.
```kotlin
val l = b?.length ?: -1
```

### Q52: What is Safe Call Operator (`?.`)?
**Difficulty: Easy**

**Answer:**
Executes the call only if the reference is not null, otherwise returns null.

### Q53: What is `Nothing` type?
**Difficulty: Advanced**

**Answer:**
A type that has no values. Used to represent a function that never returns (e.g., throws an exception). Subtype of all types.

### Q54: What is Type Alias?
**Difficulty: Easy**

**Answer:**
Provides alternative names for existing types.
```kotlin
typealias NodeSet = Set<Network.Node>
```

### Q55: What is Smart Cast?
**Difficulty: Medium**

**Answer:**
Compiler automatically casts a variable to a target type if it has been checked.
```kotlin
if (x is String) {
    print(x.length) // x is automatically cast to String
}
```

### Q56: What is `tailrec`?
**Difficulty: Medium**

**Answer:**
Tail recursion optimization. Compiler optimizes recursive calls to a loop to prevent stack overflow.

### Q57: What are Sealed Interfaces (Kotlin 1.5)?
**Difficulty: Advanced**

**Answer:**
Similar to sealed classes but for interfaces. All implementations must be known at compile time.

### Q58: What is `value class` (Inline Class)?
**Difficulty: Advanced**

**Answer:**
Wraps a single value but is inlined at compile time (represented by the underlying value) to avoid allocation overhead.
```kotlin
@JvmInline value class Password(val s: String)
```

### Q59: What is Functional Interface (SAM)?
**Difficulty: Medium**

**Answer:**
Single Abstract Method interface.
```kotlin
fun interface Predicate {
    fun accept(i: Int): Boolean
}
```

### Q60: What is Context Receiver (Kotlin 1.6.20+)?
**Difficulty: Advanced**

**Answer:**
Allows a function to require multiple receivers (contexts) to be present in the scope.
```kotlin
context(View, CoroutineScope)
fun setup() { ... }
```

### Q61: What is KMP (Kotlin Multiplatform)?
**Difficulty: Medium**

**Answer:**
Technology that allows sharing code between platforms (Android, iOS, Web, Desktop) while writing platform-specific code where necessary.

### Q62: What is Ktor?
**Difficulty: Medium**

**Answer:**
An asynchronous framework for creating microservices, web applications, and clients in Kotlin.

### Q63: What is `expect` and `actual` in KMP?
**Difficulty: Advanced**

**Answer:**
- `expect`: Declaration in common code (interface-like).
- `actual`: Implementation in platform-specific code.

### Q64: What is Gradle Kotlin DSL?
**Difficulty: Medium**

**Answer:**
Writing Gradle build scripts using Kotlin (`build.gradle.kts`) instead of Groovy. Provides better IDE support (autocomplete, refactoring).

### Q65: What is `Sequence` in Kotlin?
**Difficulty: Advanced**

**Answer:**
Lazily evaluated collection. Operations are performed one-by-one on elements (vertical) rather than creating intermediate collections (horizontal). Good for large data sets.

### Q66: What is `@JvmStatic`?
**Difficulty: Medium**

**Answer:**
Tells the compiler to generate an additional static method in the compiled Java class. Useful for Java interoperability.

### Q67: What is `@JvmOverloads`?
**Difficulty: Medium**

**Answer:**
Generates multiple overloads for Java callers for a Kotlin function with default parameter values.

### Q68: What is `@JvmField`?
**Difficulty: Medium**

**Answer:**
Instructs the compiler not to generate getters/setters for a property and expose it as a public field.

### Q69: What is `@Volatile` in Kotlin?
**Difficulty: Medium**

**Answer:**
Equivalent to Java's `volatile`. Ensures visibility of changes across threads.

### Q70: What is `@Synchronized` in Kotlin?
**Difficulty: Medium**

**Answer:**
Equivalent to Java's `synchronized` method modifier.

### Q71: How do you create a custom Getter/Setter?
**Difficulty: Easy**

**Answer:**
```kotlin
var stringRepresentation: String
    get() = this.toString()
    set(value) {
        setDataFromString(value)
    }
```

### Q72: What is the `check` function?
**Difficulty: Easy**

**Answer:**
Throws `IllegalStateException` if the condition is false.
```kotlin
check(isValid) { "State is invalid" }
```

### Q73: What is the `require` function?
**Difficulty: Easy**

**Answer:**
Throws `IllegalArgumentException` if the condition is false. Used for argument validation.
```kotlin
require(x > 0) { "x must be positive" }
```

### Q74: What is `TODO()`?
**Difficulty: Easy**

**Answer:**
A function that throws `NotImplementedError`. Used as a placeholder.

### Q75: What is `Repeatable` annotation?
**Difficulty: Medium**

**Answer:**
Allows an annotation to be applied multiple times to the same element.

### Q76: What is Variance (Covariance/Contravariance)?
**Difficulty: Advanced**

**Answer:**
- `out` (Covariant): Producer. `List<out T>`. Can read T, cannot write.
- `in` (Contravariant): Consumer. `Comparable<in T>`. Can write T, cannot read.

### Q77: What is Star Projection (`*`)?
**Difficulty: Advanced**

**Answer:**
Used when you don't know or don't care about the specific type argument. `List<*>` is similar to Java's `List<?>`.

### Q78: What is Contract (Kotlin Contracts)?
**Difficulty: Advanced**

**Answer:**
Allows functions to describe their behavior to the compiler (e.g., "this function returns only if argument is not null", or "this lambda is invoked exactly once"). Helps with smart casts.

### Q79: What is `buildString`?
**Difficulty: Easy**

**Answer:**
A utility function to build a string using `StringBuilder`.
```kotlin
val s = buildString {
    append("Hello")
    append(" World")
}
```

### Q80: What is `use` function?
**Difficulty: Medium**

**Answer:**
Executes a block on a Closeable resource and closes it afterwards (try-with-resources equivalent).

### Q81: What is `measureTimeMillis`?
**Difficulty: Easy**

**Answer:**
Executes a block and returns the elapsed time in milliseconds.

### Q82: What is `Crossinline`?
**Difficulty: Advanced**

**Answer:**
Used in inline functions to forbid non-local returns in a lambda parameter.

### Q83: What is `Noinline`?
**Difficulty: Advanced**

**Answer:**
Used in inline functions to prevent a specific lambda parameter from being inlined.

### Q84: What is the difference between `fold` and `reduce`?
**Difficulty: Medium**

**Answer:**
- `fold`: Takes an initial value.
- `reduce`: Uses the first element as the initial value. Throws exception on empty collection.

### Q85: What is `associateBy`?
**Difficulty: Medium**

**Answer:**
Creates a Map from a collection using a key selector.

### Q86: What is `groupBy`?
**Difficulty: Medium**

**Answer:**
Groups elements of the original collection by the key returned by the given selector function. Returns `Map<K, List<V>>`.

### Q87: What is `partition`?
**Difficulty: Medium**

**Answer:**
Splits the original collection into pair of lists, where first list contains elements for which predicate yielded true, while second list contains elements for which predicate yielded false.

### Q88: What is `flatMap`?
**Difficulty: Medium**

**Answer:**
Transforms each element into a collection and then flattens these collections into a single list.

### Q89: What is `zip`?
**Difficulty: Medium**

**Answer:**
Merges two collections into a list of pairs.

### Q90: What is `distinct`?
**Difficulty: Easy**

**Answer:**
Returns a list containing only distinct elements from the given collection.

### Q91: What is `any`, `all`, `none`?
**Difficulty: Easy**

**Answer:**
- `any`: True if at least one element matches.
- `all`: True if all elements match.
- `none`: True if no elements match.

### Q92: What is `find` vs `first`?
**Difficulty: Medium**

**Answer:**
- `find`: Returns the first matching element or null.
- `first`: Returns the first matching element or throws `NoSuchElementException`.

### Q93: What is `chunked`?
**Difficulty: Easy**

**Answer:**
Splits this collection into a list of lists each not exceeding the given size.

### Q94: What is `windowed`?
**Difficulty: Medium**

**Answer:**
Returns a snapshot (window) of the collection of a given size, sliding by a given step.

### Q95: What is `coerceIn`?
**Difficulty: Easy**

**Answer:**
Ensures a value is within a specified range.

### Q96: What is `takeIf` and `takeUnless`?
**Difficulty: Medium**

**Answer:**
- `takeIf`: Returns object if predicate matches, else null.
- `takeUnless`: Returns object if predicate does NOT match, else null.

### Q97: What is `MutableSharedFlow`?
**Difficulty: Advanced**

**Answer:**
A mutable implementation of SharedFlow that allows emitting values.

### Q98: What is `Job` in Coroutines?
**Difficulty: Medium**

**Answer:**
A background job. Conceptually, it is a cancellable thing with a lifecycle that culminates in its completion.

### Q99: What is `SupervisorJob`?
**Difficulty: Advanced**

**Answer:**
A job where children can fail independently of each other. A failure of a child does not cancel the parent or other children.

### Q100: What is the future of Kotlin?
**Difficulty: Easy**

**Answer:**
Kotlin is becoming a true multiplatform language (KMP). Google is "Kotlin First" for Android. Server-side Kotlin is growing (Ktor, Spring Boot). Kotlin 2.0 (K2 compiler) brings significant performance improvements.
