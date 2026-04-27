<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>Kotlin Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for developers</b></p>
</div>

---

## Table of Contents

1. [How do you prevent blocking the Main Thread when performing network operations in Kotlin?](#q1-how-do-you-prevent-blocking-the-main-thread-when-performing-network-operations-in-kotlin) <span class="beginner">Beginner</span>
2. [How do you choose between `val`, `var`, `const val`, and `lateinit var`?](#q2-how-do-you-choose-between-val-var-const-val-and-lateinit-var) <span class="beginner">Beginner</span>
3. [How do you use Sealed Classes to model UI state effectively?](#q3-how-do-you-use-sealed-classes-to-model-ui-state-effectively) <span class="intermediate">Intermediate</span>
4. [How do you safely handle null values without using the `!!` operator?](#q4-how-do-you-safely-handle-null-values-without-using-the-!!-operator) <span class="beginner">Beginner</span>
5. [How do you optimize collection processing using Sequences?](#q5-how-do-you-optimize-collection-processing-using-sequences) <span class="intermediate">Intermediate</span>
6. [How do you implement the Singleton pattern in Kotlin?](#q6-how-do-you-implement-the-singleton-pattern-in-kotlin) <span class="beginner">Beginner</span>
7. [How do you extend a class functionality without inheriting from it (Extension Functions)?](#q7-how-do-you-extend-a-class-functionality-without-inheriting-from-it-extension-functions) <span class="intermediate">Intermediate</span>
8. [How do you use `StateFlow` vs `SharedFlow` for event handling?](#q8-how-do-you-use-stateflow-vs-sharedflow-for-event-handling) <span class="advanced">Advanced</span>
9. [How do you delegate property logic using the `by` keyword?](#q9-how-do-you-delegate-property-logic-using-the-by-keyword) <span class="intermediate">Intermediate</span>
10. [How do you handle structured concurrency to ensure no coroutines leak?](#q10-how-do-you-handle-structured-concurrency-to-ensure-no-coroutines-leak) <span class="advanced">Advanced</span>
11. [How do you access the reified type parameter in an inline function?](#q11-how-do-you-access-the-reified-type-parameter-in-an-inline-function) <span class="advanced">Advanced</span>
12. [How do you filter a list of objects and return a new list containing only non-null results?](#q12-how-do-you-filter-a-list-of-objects-and-return-a-new-list-containing-only-non-null-results) <span class="beginner">Beginner</span>
13. [How do you create a Domain Specific Language (DSL) in Kotlin?](#q13-how-do-you-create-a-domain-specific-language-dsl-in-kotlin) <span class="expert">Expert</span>
14. [How do you use Destructuring Declarations to return multiple values?](#q14-how-do-you-use-destructuring-declarations-to-return-multiple-values) <span class="beginner">Beginner</span>
15. [How do you choose between `apply`, `also`, `let`, `run`, and `with`?](#q15-how-do-you-choose-between-apply-also-let-run-and-with) <span class="intermediate">Intermediate</span>
16. [How do you use `value class` (Inline Classes) to optimize memory?](#q16-how-do-you-use-value-class-inline-classes-to-optimize-memory) <span class="intermediate">Intermediate</span>
17. [What is the difference between `sealed class` and `sealed interface`?](#q17-what-is-the-difference-between-sealed-class-and-sealed-interface) <span class="intermediate">Intermediate</span>
18. [When should you use `init` blocks?](#q18-when-should-you-use-init-blocks) <span class="beginner">Beginner</span>
19. [How do you make Kotlin code Java-friendly using `@JvmStatic` and `@JvmOverloads`?](#q19-how-do-you-make-kotlin-code-java-friendly-using-@jvmstatic-and-@jvmoverloads) <span class="intermediate">Intermediate</span>
20. [How do you optimize recursion using `tailrec`?](#q20-how-do-you-optimize-recursion-using-tailrec) <span class="intermediate">Intermediate</span>
21. [How do you create readable DSL-like code using `infix` functions?](#q21-how-do-you-create-readable-dsl-like-code-using-infix-functions) <span class="intermediate">Intermediate</span>
22. [How do you overload operators (e.g., `+`, `[]`)?](#q22-how-do-you-overload-operators-e.g.-+-[]) <span class="intermediate">Intermediate</span>
23. [How do you validate arguments using `check`, `require`, and `assert`?](#q23-how-do-you-validate-arguments-using-check-require-and-assert) <span class="beginner">Beginner</span>
24. [What is the difference between `runBlocking` and `coroutineScope`?](#q24-what-is-the-difference-between-runblocking-and-coroutinescope) <span class="intermediate">Intermediate</span>
25. [How do you handle Flow emissions with `collect` vs `collectLatest`?](#q25-how-do-you-handle-flow-emissions-with-collect-vs-collectlatest) <span class="advanced">Advanced</span>
26. [How do you convert a callback-based API to a Flow (`callbackFlow`)?](#q26-how-do-you-convert-a-callback-based-api-to-a-flow-callbackflow) <span class="advanced">Advanced</span>
27. [How do you ensure thread safety using `Mutex`?](#q27-how-do-you-ensure-thread-safety-using-mutex) <span class="advanced">Advanced</span>
28. [How do you handle exceptions in Coroutines globally?](#q28-how-do-you-handle-exceptions-in-coroutines-globally) <span class="advanced">Advanced</span>
29. [How do you use `SupervisorJob` to prevent failure propagation?](#q29-how-do-you-use-supervisorjob-to-prevent-failure-propagation) <span class="advanced">Advanced</span>
30. [How do you define multiplatform code using `expect` and `actual`?](#q30-how-do-you-define-multiplatform-code-using-expect-and-actual) <span class="intermediate">Intermediate</span>
31. [How do you generate a Sequence using `sequence { yield }`?](#q31-how-do-you-generate-a-sequence-using-sequence-{-yield-}) <span class="intermediate">Intermediate</span>
32. [How do you use `Nothing` type to represent unreachable code?](#q32-how-do-you-use-nothing-type-to-represent-unreachable-code) <span class="intermediate">Intermediate</span>
33. [What is a `typealias` and when to use it?](#q33-what-is-a-typealias-and-when-to-use-it) <span class="beginner">Beginner</span>
34. [How do you control backing fields using the `field` identifier?](#q34-how-do-you-control-backing-fields-using-the-field-identifier) <span class="intermediate">Intermediate</span>
35. [How do you prevent a lambda parameter from being inlined (`noinline`, `crossinline`)?](#q35-how-do-you-prevent-a-lambda-parameter-from-being-inlined-noinline-crossinline) <span class="advanced">Advanced</span>
36. [How do you use Contracts to help the compiler with smart casts?](#q36-how-do-you-use-contracts-to-help-the-compiler-with-smart-casts) <span class="advanced">Advanced</span>
37. [How do you use Functional (SAM) interfaces?](#q37-how-do-you-use-functional-sam-interfaces) <span class="intermediate">Intermediate</span>
38. [How do you use Destructuring in lambdas?](#q38-how-do-you-use-destructuring-in-lambdas) <span class="beginner">Beginner</span>
39. [How do you use Receiver Functions (`String.() -> Unit`)?](#q39-how-do-you-use-receiver-functions-string.-->-unit) <span class="advanced">Advanced</span>
40. [How do you delegate properties to a Map?](#q40-how-do-you-delegate-properties-to-a-map) <span class="intermediate">Intermediate</span>
41. [How do you perform bitwise operations in Kotlin?](#q41-how-do-you-perform-bitwise-operations-in-kotlin) <span class="beginner">Beginner</span>
42. [What is Covariance (`out`) and Contravariance (`in`)?](#q42-what-is-covariance-out-and-contravariance-in) <span class="advanced">Advanced</span>
43. [How do you use `Dispatchers.Unconfined`?](#q43-how-do-you-use-dispatchers.unconfined) <span class="advanced">Advanced</span>
44. [How do you buffer a Flow?](#q44-how-do-you-buffer-a-flow) <span class="intermediate">Intermediate</span>
45. [How do you combine multiple Flows (`zip`, `combine`)?](#q45-how-do-you-combine-multiple-flows-zip-combine) <span class="intermediate">Intermediate</span>
46. [How do you use `ConflatedBroadcastChannel` (or `StateFlow`)?](#q46-how-do-you-use-conflatedbroadcastchannel-or-stateflow) <span class="advanced">Advanced</span>
47. [How do you mock final classes in Kotlin with Mockito?](#q47-how-do-you-mock-final-classes-in-kotlin-with-mockito) <span class="intermediate">Intermediate</span>
48. [How do you use `measureTimeMillis` for benchmarking?](#q48-how-do-you-use-measuretimemillis-for-benchmarking) <span class="beginner">Beginner</span>
49. [How do you create a singleton with arguments?](#q49-how-do-you-create-a-singleton-with-arguments) <span class="intermediate">Intermediate</span>
50. [How do you use `remember` in Jetpack Compose (Kotlin context)?](#q50) <span class="intermediate">Intermediate</span>

---

<a id="q1"></a>
### Q1: How do you prevent blocking the Main Thread when performing network operations in Kotlin?

**Difficulty**: Beginner

**Strategy**:
Blocking the main thread causes ANR (Application Not Responding) crashes on Android and freezes UI in any graphical application. Interviewers test this to verify you understand asynchronous programming, which is fundamental to modern Kotlin development. The key is using coroutines with the appropriate dispatcher to offload work, and a common pitfall is forgetting to use `withContext` and accidentally running I/O on the main thread.

**Strategy:**
Use **Coroutines**. Mark the function as `suspend` and switch to the IO dispatcher using `withContext(Dispatchers.IO)`. Call it from a `CoroutineScope` (like `viewModelScope`).

**Code Example:**
```kotlin
suspend fun fetchUser(): User = withContext(Dispatchers.IO) {
    // This runs on a background thread
    api.getUser() 
}

// Usage in ViewModel
fun loadData() {
    viewModelScope.launch {
        val user = fetchUser() // Suspends here, doesn't block UI
        _uiState.value = user // Back on Main thread
    }
}
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q2"></a>
### Q2: How do you choose between `val`, `var`, `const val`, and `lateinit var`?

**Difficulty**: Beginner

**Strategy**:
Choosing the right variable declaration is one of the first things interviewers assess because it reveals your grasp of immutability, compile-time optimization, and initialization safety. Defaulting to `val` promotes predictable code, while misusing `lateinit var` (e.g., accessing before initialization) causes runtime crashes. Understanding `const val` shows awareness of compile-time constants and how they differ from runtime-assigned values.

**Strategy:**
*   `val`: Immutable reference (prefer this).
*   `var`: Mutable reference.
*   `const val`: Compile-time constant (primitives/strings only).
*   `lateinit var`: Non-null mutable variable initialized later (e.g., dependency injection).

**Code Example:**
```kotlin
const val MAX_RETRIES = 3 // Compile-time
class Service {
    lateinit var db: Database // Initialized later
    val id = UUID.randomUUID() // Runtime immutable
    var count = 0 // Mutable
}
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q3"></a>
### Q3: How do you use Sealed Classes to model UI state effectively?

**Difficulty**: Intermediate

**Strategy**:
Sealed classes are the idiomatic Kotlin way to represent finite state machines, which makes them essential for UI state management in Android (MVI/MVVM patterns). Interviewers value this topic because it leverages the compiler to guarantee exhaustive handling of all states, eliminating missed branches that cause subtle bugs. A common pitfall is using enums with extra data instead of sealed classes, which limits flexibility.

**Strategy:**
Use **Sealed Classes** (or Interfaces) to define a restricted hierarchy. This allows exhaustive `when` expressions, ensuring all states (Loading, Success, Error) are handled.

**Code Example:**
```kotlin
sealed class UiState {
    object Loading : UiState()
    data class Success(val data: String) : UiState()
    data class Error(val message: String) : UiState()
}

fun render(state: UiState) {
    when (state) {
        is UiState.Loading -> showSpinner()
        is UiState.Success -> showData(state.data)
        is UiState.Error -> showError(state.message)
    } // No 'else' branch needed
}
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q4"></a>
### Q4: How do you safely handle null values without using the `!!` operator?

**Difficulty**: Beginner

**Strategy**:
Null safety is Kotlin's flagship feature and consistently appears in interviews. Using `!!` is a code smell that defeats the purpose of Kotlin's null-safety system and will cause a NullPointerException at runtime if the value is null. The best practice is to use safe calls and the Elvis operator to handle nulls gracefully, ensuring your code never crashes due to unexpected null values.

**Strategy:**
Use the **Safe Call** operator (`?.`) combined with `let` or the **Elvis Operator** (`?:`) to provide a default value or return early.

**Code Example:**
```kotlin
val name: String? = null

// Safe call with let
name?.let { println("Name is $it") }

// Elvis operator
val validName = name ?: "Unknown"

// Early return
val len = name?.length ?: return
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q5"></a>
### Q5: How do you optimize collection processing using Sequences?

**Difficulty**: Intermediate

**Strategy**:
Understanding lazy vs. eager evaluation is critical when processing large datasets or chaining multiple operations. Regular collection operators create intermediate lists at every step, which wastes memory and CPU. Sequences process elements one at a time through the entire chain, avoiding intermediate allocations. A common mistake is using sequences for small collections where the overhead outweighs the benefit.

**Strategy:**
Use **Sequences** (`asSequence()`) for large collections or multi-step chains (`map`, `filter`). Sequences evaluate lazily (element-by-element), avoiding intermediate list creation.

**Code Example:**
```kotlin
val list = (1..1_000_000).toList()

// BAD: Creates 2 intermediate lists
list.filter { it % 2 == 0 }.map { it * 2 }.first()

// GOOD: No intermediate lists, stops after finding first match
list.asSequence()
    .filter { it % 2 == 0 }
    .map { it * 2 }
    .first()
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q6"></a>
### Q6: How do you implement the Singleton pattern in Kotlin?

**Difficulty**: Beginner

**Strategy**:
The Singleton pattern is a classic interview topic, and Kotlin's `object` declaration is the most concise and thread-safe way to implement it. Unlike Java's double-checked locking boilerplate, Kotlin handles lazy thread-safe initialization automatically. Be aware that `object` singletons cannot accept constructor parameters, so if you need parameterized singletons you must use a different approach.

**Strategy:**
Use the `object` keyword. It creates a thread-safe singleton instance lazily.

**Code Example:**
```kotlin
object DatabaseConnection {
    val url = "jdbc:mysql://localhost:3306"
    fun connect() { /* ... */ }
}

// Usage
DatabaseConnection.connect()
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q7"></a>
### Q7: How do you extend a class functionality without inheriting from it (Extension Functions)?

**Difficulty**: Intermediate

**Strategy**:
Extension functions are one of Kotlin's most practical features and demonstrate your ability to write clean, reusable code without modifying existing classes. They are resolved statically, so they do not actually modify the class bytecode. A key pitfall is that if an extension function has the same signature as a member function, the member always wins, which can lead to confusing behavior.

**Strategy:**
Define an **Extension Function**. It looks like a member function but is resolved statically. Useful for utility methods on classes you don't own (like String or View).

**Code Example:**
```kotlin
// Add a method to String class
fun String.removeSpaces(): String {
    return this.replace(" ", "")
}

val clean = "Hello World".removeSpaces() // "HelloWorld"
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q8"></a>
### Q8: How do you use `StateFlow` vs `SharedFlow` for event handling?

**Difficulty**: Advanced

**Strategy**:
Choosing the right reactive stream type is crucial in modern Android architecture. Using StateFlow for one-time events like navigation or snackbar messages causes issues because new collectors receive the last replayed value on configuration changes. SharedFlow with appropriate replay settings handles events correctly. Interviewers test this to see if you understand the distinction between state (always has a value) and events (transient occurrences).

**Strategy:**
*   **StateFlow:** Use for **State** (holds a value, replays last value to new collectors, similar to LiveData).
*   **SharedFlow:** Use for **Events** (no initial value, can configure replay, hot stream).

**Code Example:**
```kotlin
// State (UI State)
private val _uiState = MutableStateFlow(UiState.Loading)
val uiState = _uiState.asStateFlow()

// Event (Navigation, Snackbar)
private val _events = MutableSharedFlow<String>()
val events = _events.asSharedFlow()
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q9"></a>
### Q9: How do you delegate property logic using the `by` keyword?

**Difficulty**: Intermediate

**Strategy**:
Property delegation is a powerful mechanism that eliminates boilerplate for common patterns like lazy initialization, observable properties, and storing values in maps or SharedPreferences. It demonstrates an understanding of Kotlin's DSL-friendly design. The most common pitfall is overusing custom delegates when a simple getter/setter would be clearer.

**Strategy:**
Use **Property Delegation** to reuse getter/setter logic. Common delegates are `lazy`, `observable`, or custom ones (e.g., for SharedPreferences).

**Code Example:**
```kotlin
// Lazy initialization
val heavyObject by lazy {
    HeavyComputation() // Executed only on first access
}

// Observable
var user: User by Delegates.observable(initialUser) { prop, old, new ->
    println("User changed from $old to $new")
}
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q10"></a>
### Q10: How do you handle structured concurrency to ensure no coroutines leak?

**Difficulty**: Advanced

**Strategy**:
Structured concurrency is the cornerstone of reliable coroutine usage and a frequent advanced interview topic. Leaked coroutines waste resources, cause memory leaks, and can crash the app with unhandled exceptions. The key principle is that every coroutine must have a parent scope that manages its lifecycle. A common mistake is using `GlobalScope`, which bypasses structured concurrency entirely and should almost never be used in production code.

**Strategy:**
Always launch coroutines within a specific `CoroutineScope` (e.g., `viewModelScope`, `lifecycleScope`) or use `coroutineScope { }` builder. When the scope is cancelled, all children are cancelled automatically.

**Code Example:**
```kotlin
suspend fun loadTwoThings() = coroutineScope {
    // Both run in parallel
    val data1 = async { api.fetchOne() }
    val data2 = async { api.fetchTwo() }
    
    // If fetchOne fails, fetchTwo is automatically cancelled
    combine(data1.await(), data2.await())
}
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q11"></a>
### Q11: How do you access the reified type parameter in an inline function?

**Difficulty**: Advanced

**Strategy**:
Generics are erased at runtime on the JVM (type erasure), which means you normally cannot check `T::class.java`. Reified type parameters solve this by inlining the function at the call site, preserving type information. This is essential for building type-safe APIs like JSON parsers, fragment argument bundles, or repository abstractions. Be aware that reified only works with `inline` functions, so it cannot be used on open or abstract functions.

**Strategy:**
Mark the function as `inline` and the type parameter as `reified`. This allows you to access the type class at runtime (e.g., for JSON parsing or intent creation).

**Code Example:**
```kotlin
inline fun <reified T> parseJson(json: String): T {
    // T::class.java is available because of reified
    return Gson().fromJson(json, T::class.java)
}

val user: User = parseJson(jsonString)
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q12"></a>
### Q12: How do you filter a list of objects and return a new list containing only non-null results?

**Difficulty**: Beginner

**Strategy**:
This is a practical question that tests your familiarity with Kotlin's standard library and functional collection operations. Writing a manual loop with null checks is verbose and error-prone. `mapNotNull` combines transformation and null filtering in a single pass, producing cleaner and more idiomatic code. Interviewers look for this as a signal that you write concise, functional-style Kotlin rather than Java-style loops.

**Strategy:**
Use `mapNotNull`. It transforms the collection and drops any `null` results in one step.

**Code Example:**
```kotlin
val inputs = listOf("1", "2", "abc", "4")
val numbers = inputs.mapNotNull { it.toIntOrNull() }
// Result: [1, 2, 4]
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q13"></a>
### Q13: How do you create a Domain Specific Language (DSL) in Kotlin?

**Difficulty**: Expert

**Strategy**:
DSLs showcase advanced Kotlin mastery and are used heavily in libraries like Ktor, Gradle Kotlin DSL, and Jetpack Compose. The core mechanism is function literals with receivers, which let lambda bodies access the receiver's members implicitly. When building DSLs, always use `@DslMarker` annotations to prevent accidental access to outer receiver scopes, which is a subtle but important correctness concern.

**Strategy:**
Use **Function Literals with Receiver** (lambda with receiver). This allows you to call methods on the receiver object inside the lambda without `this`.

**Code Example:**
```kotlin
class HtmlBuilder {
    fun body(block: () -> Unit) { println("<body>"); block(); println("</body>") }
    fun p(text: String) { println("<p>$text</p>") }
}

fun html(block: HtmlBuilder.() -> Unit) {
    HtmlBuilder().block()
}

// Usage
html {
    body {
        p("Hello DSL")
    }
}
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q14"></a>
### Q14: How do you use Destructuring Declarations to return multiple values?

**Difficulty**: Beginner

**Strategy**:
Destructuring declarations make code more readable by unpacking composite values into named variables in a single line. This is especially common when working with map entries, API responses with multiple fields, or when a function needs to return related but distinct values. Prefer data classes over Pairs or Triples for production code since named components are self-documenting and less error-prone than positional access.

**Strategy:**
Return a `Pair`, `Triple`, or a `data class`. Kotlin allows unpacking these directly into variables.

**Code Example:**
```kotlin
data class Result(val code: Int, val message: String)

fun getResult(): Result = Result(200, "OK")

fun main() {
    val (code, msg) = getResult()
    println("$code: $msg")
}
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q15"></a>
### Q15: How do you choose between `apply`, `also`, `let`, `run`, and `with`?

**Difficulty**: Intermediate

**Strategy**:
Scope functions are ubiquitous in Kotlin codebases and interviewers test whether you can select the right one for each situation. The decision comes down to two questions: do you need to return the object or a result, and do you prefer `this` or `it` as the reference? Misusing scope functions leads to confusing code, so memorizing the two-axis decision table (return type + reference type) is the best approach.

**Strategy:**
*   `apply`: Configure object (returns object, `this`).
*   `also`: Side effects (returns object, `it`).
*   `let`: Transform/Null-check (returns result, `it`).
*   `run`: Transform/Initialize (returns result, `this`).
*   `with`: Call multiple methods on object (returns result, `this`, not extension).

**Code Example:**
```kotlin
val intent = Intent().apply {
    action = "VIEW"
    data = uri
}

val len = str?.let {
    println("Non-null: $it")
    it.length
}
```

[⬆️ Back to Top](#table-of-contents)

---

<a id="q16"></a>
### Q16: How do you use `value class` (Inline Classes) to optimize memory?

**Difficulty**: Intermediate

**Strategy**:
Value classes give you type safety without the runtime cost of wrapper objects, which is a powerful optimization for performance-critical code. They are particularly useful for domain modeling where you want to distinguish between different kinds of IDs, passwords, or measurements at compile time. A key constraint is that value classes can only wrap a single property and cannot participate in complex inheritance hierarchies.

**Strategy:**
Use `value class` (formerly `inline class`) to wrap a single value without allocating a new object on the heap. Useful for type safety (e.g., Password, ID).

**Code Example:**
@JvmInline
value class Password(val s: String)

// At runtime, this is just a String, but compile-time checks prevent mixing it with other Strings.
fun login(p: Password) {}

[⬆️ Back to Top](#table-of-contents)

---

<a id="q17"></a>
### Q17: What is the difference between `sealed class` and `sealed interface`?

**Difficulty**: Intermediate

**Strategy**:
Understanding when to use sealed class vs. sealed interface shows depth in Kotlin's type system design. Sealed interfaces enable multiple inheritance within sealed hierarchies, which is useful when a type needs to participate in more than one restricted classification. Sealed classes carry state via constructors, making them better for rich domain models. A common pitfall is trying to make a class extend multiple sealed classes, which is not allowed in Kotlin.

**Strategy:**
Both restrict hierarchy. `sealed class` allows state (constructor parameters) and default behavior. `sealed interface` allows a class to inherit from multiple sealed hierarchies (multiple inheritance of types).

**Code Example:**
sealed interface Error
sealed class NetworkError : Error

data class Timeout(val time: Long) : NetworkError()
// Can implement multiple sealed interfaces
class ComplexError : Error, Serializable

[⬆️ Back to Top](#table-of-contents)

---

<a id="q18"></a>
### Q18: When should you use `init` blocks?

**Difficulty**: Beginner

**Strategy**:
Init blocks are Kotlin's way of running validation and setup logic during object construction, filling the role that constructor bodies serve in Java. They are essential for enforcing invariants early and failing fast when invalid data is provided. A common mistake is placing initialization logic outside init blocks where it runs before property initialization, causing unexpected null or default values.

**Strategy:**
Use `init` blocks to run code during object instantiation, immediately after the primary constructor. You can have multiple `init` blocks, executed in order.

**Code Example:**
class User(val name: String) {
  init {
    require(name.isNotEmpty()) { "Name cannot be empty" }
  }
}

[⬆️ Back to Top](#table-of-contents)

---

<a id="q19"></a>
### Q19: How do you make Kotlin code Java-friendly using `@JvmStatic` and `@JvmOverloads`?

**Difficulty**: Intermediate

**Strategy**:
Interoperability with Java is critical in mixed codebases, especially during incremental migration from Java to Kotlin. Without these annotations, Java callers face awkward syntax like `Companion.instance` or must supply every default parameter explicitly. These annotations generate the bytecode Java expects, making the Kotlin API feel natural to Java consumers. A pitfall is forgetting that `@JvmOverloads` generates overloads based on parameter order, so parameter ordering matters.

**Strategy:**
- `@JvmStatic`: Generates a static method in the bytecode (instead of instance method on companion).
- `@JvmOverloads`: Generates multiple overloads for functions with default parameters.

**Code Example:**
object Utils {
  @JvmStatic
  @JvmOverloads
  fun greet(name: String = "World") {
    println("Hello, $name")
  }
}
// Java: Utils.greet(); Utils.greet("John");

[⬆️ Back to Top](#table-of-contents)

---

<a id="q20"></a>
### Q20: How do you optimize recursion using `tailrec`?

**Difficulty**: Intermediate

**Strategy**:
Recursive algorithms are elegant but risk stack overflow on large inputs. The `tailrec` modifier tells the compiler to convert the recursion into an iterative loop under the hood, preserving readability without sacrificing safety. The compiler will warn you if the recursive call is not truly in tail position, which is important because a non-tail call silently remains unoptimized.

**Strategy:**
Mark a function as `tailrec` if the recursive call is the last operation. The compiler optimizes it into a fast loop, preventing StackOverflowError.

**Code Example:**
tailrec fun factorial(n: Int, run: Int = 1): Int {
    return if (n == 1) run else factorial(n - 1, run * n)
}

[⬆️ Back to Top](#table-of-contents)

---

<a id="q21"></a>
### Q21: How do you create readable DSL-like code using `infix` functions?

**Difficulty**: Intermediate

**Strategy**:
Infix functions improve code readability by enabling natural-language-style call syntax, which is why libraries like Kotlin's test framework and Ktor use them extensively. They are restricted to single-parameter functions, which limits their scope but keeps them focused. A best practice is to use them only when the operation reads naturally as a verb or relationship, not as a general replacement for method calls.

**Strategy:**
Mark a member or extension function as `infix` to call it without dots and parentheses. It must take exactly one parameter.

**Code Example:**
infix fun Int.times(str: String) = str.repeat(this)

// Usage
val result = 3 times "Hello " // "Hello Hello Hello " 

[⬆️ Back to Top](#table-of-contents)

---

<a id="q22"></a>
### Q22: How do you overload operators (e.g., `+`, `[]`)?

**Difficulty**: Intermediate

**Strategy**:
Operator overloading lets your custom types behave like built-in types, making mathematical or collection-like abstractions intuitive to use. Each operator maps to a predefined function name (like `plus` for `+`), so you cannot invent arbitrary operators. The main pitfall is overusing operator overloading for non-intuitive operations, which makes code harder to read and violates the principle of least surprise.

**Strategy:**
Define a function with a specific name (`plus`, `get`, `set`, etc.) and mark it with `operator` modifier.

**Code Example:**
data class Point(val x: Int, val y: Int) {
    operator fun plus(other: Point) = Point(x + other.x, y + other.y)
}

val p1 = Point(1, 2)
val p2 = Point(3, 4)
val p3 = p1 + p2 // Point(4, 6)

[⬆️ Back to Top](#table-of-contents)

---

<a id="q23"></a>
### Q23: How do you validate arguments using `check`, `require`, and `assert`?

**Difficulty**: Beginner

**Strategy**:
Proper input validation is a hallmark of defensive programming, and Kotlin provides these built-in functions to make it concise and idiomatic. Using the right one signals intent clearly: `require` for caller-provided arguments, `check` for object state, and `assert` for development-time invariants. A common pitfall is relying on `assert` in production code since assertions are disabled by default at runtime.

**Strategy:**
- `require(Boolean)`: Throws `IllegalArgumentException` (Argument validation).
- `check(Boolean)`: Throws `IllegalStateException` (State validation).
- `assert(Boolean)`: Throws `AssertionError` (Only if assertions enabled, `-ea`).

**Code Example:**
fun setAge(age: Int) {
    require(age >= 0) { "Age must be positive" }
    check(isInitialized) { "Not initialized" }
}

[⬆️ Back to Top](#table-of-contents)

---

<a id="q24"></a>
### Q24: What is the difference between `runBlocking` and `coroutineScope`?

**Difficulty**: Intermediate

**Strategy**:
Understanding the difference between blocking and suspending is fundamental to writing correct coroutine code. `runBlocking` is a bridge between blocking and non-blocking worlds, primarily used in `main()` functions and tests. `coroutineScope` is the suspending equivalent that does not block the underlying thread. A critical pitfall is using `runBlocking` inside a coroutine, which blocks a thread from the dispatcher pool and can cause deadlocks.

**Strategy:**
`runBlocking` blocks the current thread until the coroutine completes (use in main/tests). `coroutineScope` suspends (does not block thread) and waits for children.

**Code Example:**
fun main() = runBlocking { // Blocks main thread
    launch { delay(1000) }
}

suspend fun work() = coroutineScope { // Suspends
    launch { delay(1000) }
}

[⬆️ Back to Top](#table-of-contents)

---

<a id="q25"></a>
### Q25: How do you handle Flow emissions with `collect` vs `collectLatest`?

**Difficulty**: Advanced

**Strategy**:
Choosing the right collection operator prevents both missed updates and unnecessary processing. `collect` guarantees every emission is processed, which is important for events that must not be dropped. `collectLatest` is ideal for search-as-you-type scenarios where only the latest query matters and stale results should be discarded. A pitfall is using `collectLatest` when side effects like database writes must happen for every emission.

**Strategy:**
`collect` processes every emission sequentially. `collectLatest` cancels the processing of the previous value if a new value arrives.

**Code Example:**
flow.collectLatest { value ->
    // If new value emits while this is running, this block is cancelled
    delay(100) 
    println(value)
}

[⬆️ Back to Top](#table-of-contents)

---

<a id="q26"></a>
### Q26: How do you convert a callback-based API to a Flow (`callbackFlow`)?

**Difficulty**: Advanced

**Strategy**:
Many legacy or platform APIs (location services, sensors, WebSocket listeners) are callback-based, and converting them to Flow enables consistent reactive patterns throughout your codebase. `callbackFlow` bridges the two worlds by letting you emit values from callbacks while maintaining Flow's cancellation semantics. The most critical requirement is implementing `awaitClose` to unregister callbacks and prevent resource leaks.

**Strategy:**
Use `callbackFlow`. Register the callback inside, `trySend` elements, and use `awaitClose` to unregister the callback.

**Code Example:**
fun getLocationFlow(): Flow<Location> = callbackFlow {
    val listener = object : LocationListener {
        override fun onLocationChanged(loc: Location) { trySend(loc) }
    }
    locationManager.register(listener)
    awaitClose { locationManager.unregister(listener) }
}

[⬆️ Back to Top](#table-of-contents)

---

<a id="q27"></a>
### Q27: How do you ensure thread safety using `Mutex`?

**Difficulty**: Advanced

**Strategy**:
Shared mutable state is one of the hardest concurrency problems, and interviewers test whether you know the coroutine-friendly way to handle it. Kotlin's `Mutex` suspends instead of blocking, which is far more efficient than `synchronized` or `ReentrantLock` in a coroutine context. A common mistake is using Java's `synchronized` block inside coroutines, which blocks the thread and defeats the purpose of structured concurrency.

**Strategy:**
Use `Mutex` (Mutual Exclusion) lock. It suspends the coroutine instead of blocking the thread like `synchronized`.

**Code Example:**
val mutex = Mutex()
var counter = 0

suspend fun increment() {
    mutex.withLock {
        counter++
    }
}

[⬆️ Back to Top](#table-of-contents)

---

<a id="q28"></a>
### Q28: How do you handle exceptions in Coroutines globally?

**Difficulty**: Advanced

**Strategy**:
Unhandled coroutine exceptions crash the app, so a solid exception handling strategy is non-negotiable in production code. `CoroutineExceptionHandler` acts as a last-resort catch-all for `launch`-based coroutines, similar to `Thread.uncaughtExceptionHandler`. A critical nuance is that it does not catch exceptions from `async` blocks, since those are expected to be handled at the `await` call site.

**Strategy:**
Use `CoroutineExceptionHandler` attached to the scope or root coroutine. Note: It only catches uncaught exceptions (not valid for `async` which expects user to call `await`).

**Code Example:**
val handler = CoroutineExceptionHandler { _, exception ->
    println("Caught $exception")
}
val scope = CoroutineScope(Job() + handler)

[⬆️ Back to Top](#table-of-contents)

---

<a id="q29"></a>
### Q29: How do you use `SupervisorJob` to prevent failure propagation?

**Difficulty**: Advanced

**Strategy**:
Understanding failure propagation in coroutines is essential for building resilient applications. A regular `Job` cancels all siblings when one child fails, which is often undesirable (e.g., one failed network request should not kill an unrelated UI update). `SupervisorJob` isolates failures to the failing child only. The key pitfall is using a regular `Job` in a scope that runs independent tasks, causing cascading cancellation.

**Strategy:**
With a standard `Job`, if one child fails, the parent and all siblings are cancelled. With `SupervisorJob`, children can fail independently.

**Code Example:**
val scope = CoroutineScope(SupervisorJob())

scope.launch { throw Error("Fail") }
scope.launch { 
    delay(100)
    println("I am still alive") 
}

[⬆️ Back to Top](#table-of-contents)

---

<a id="q30"></a>
### Q30: How do you define multiplatform code using `expect` and `actual`?

**Difficulty**: Intermediate

**Strategy**:
Kotlin Multiplatform (KMP) is increasingly important for sharing business logic across Android, iOS, and web platforms. The `expect`/`actual` mechanism is the bridge between shared code and platform-specific implementations, similar to interfaces with platform-specific implementations. A best practice is to keep `expect` declarations minimal and push as much logic as possible into common code, only delegating to `actual` for platform-specific APIs.

**Strategy:**
In the `common` module, define an `expect` class/function. In platform-specific modules (android, ios), provide the `actual` implementation.

**Code Example:**
// Common
expect fun getPlatformName(): String

// Android
actual fun getPlatformName(): String = "Android"

// iOS
actual fun getPlatformName(): String = "iOS" 

[⬆️ Back to Top](#table-of-contents)

---

<a id="q31"></a>
### Q31: How do you generate a Sequence using `sequence { yield }`?

**Difficulty**: Intermediate

**Strategy**:
The `sequence` builder enables you to generate infinite or dynamically computed sequences without loading all values into memory. It uses coroutines under the hood, suspending at each `yield` until the next value is requested. This is ideal for generating mathematical series, reading streams, or paginating data. A common mistake is forgetting that sequences are lazy, so side effects inside the builder may not execute when expected.

**Strategy:**
Use the `sequence` builder and `yield()` to produce values lazily. Execution suspends at `yield` and resumes when the next value is requested.

**Code Example:**
val fibonacci = sequence {
    var a = 0
    var b = 1
    while (true) {
        yield(a)
        val next = a + b
        a = b
        b = next
    }
}
println(fibonacci.take(5).toList())

[⬆️ Back to Top](#table-of-contents)

---

<a id="q32"></a>
### Q32: How do you use `Nothing` type to represent unreachable code?

**Difficulty**: Intermediate

**Strategy**:
`Nothing` is Kotlin's bottom type and understanding it demonstrates depth in the type system. Functions that always throw or never return (infinite loops) should return `Nothing`, which allows the compiler to perform smart casts and dead-code analysis. This pattern is commonly used for `TODO()`, `error()`, and custom fail functions. Without `Nothing`, the compiler cannot infer that code after a throw is unreachable.

**Strategy:**
`Nothing` has no instances. It's used as a return type for functions that never return (throw exception or infinite loop), allowing compiler optimizations.

**Code Example:**
fun fail(msg: String): Nothing {
    throw IllegalArgumentException(msg)
}

val data = nullableData ?: fail("Data is null")
// Compiler knows 'data' is non-null here

[⬆️ Back to Top](#table-of-contents)

---

<a id="q33"></a>
### Q33: What is a `typealias` and when to use it?

**Difficulty**: Beginner

**Strategy**:
Type aliases improve code readability without creating new types, making them a lightweight tool for simplifying complex generic signatures and function type declarations. They are purely a compile-time feature with zero runtime overhead. A best practice is to use them for complex function types that appear frequently, but avoid aliasing simple types in ways that obscure what the underlying data actually represents.

**Strategy:**
It provides an alternative name for an existing type. Useful for shortening long generic types or function types.

**Code Example:**
typealias Handler = (Int, String, Boolean) -> Unit

fun register(h: Handler) {}

[⬆️ Back to Top](#table-of-contents)

---

<a id="q34"></a>
### Q34: How do you control backing fields using the `field` identifier?

**Difficulty**: Intermediate

**Strategy**:
Custom setters are common when you need to validate or transform values before storing them, and `field` is the only way to access the underlying storage without causing recursive calls to the setter itself. Without `field`, assigning inside a setter would trigger the setter again, creating infinite recursion. This is a subtle but essential mechanism that interviewers use to test your understanding of property internals.

**Strategy:**
Inside a custom setter, use `field` to access the backing memory of the property to avoid infinite recursion.

**Code Example:**
var counter = 0
    set(value) {
        if (value >= 0) field = value
    }

[⬆️ Back to Top](#table-of-contents)

---

<a id="q35"></a>
### Q35: How do you prevent a lambda parameter from being inlined (`noinline`, `crossinline`)?

**Difficulty**: Advanced

**Strategy**:
Inline functions with lambda parameters are a key Kotlin optimization, but not all lambdas can or should be inlined. `noinline` is needed when passing the lambda to a non-inline function or storing it. `crossinline` prevents non-local returns, which are dangerous when the lambda executes in a different context like another thread or nested coroutine. Misusing these modifiers can lead to compiler errors or subtle concurrency bugs.

**Strategy:**
- `noinline`: Do not inline this lambda (e.g., passing it to another function).
- `crossinline`: Allow inlining but forbid non-local returns (e.g., using inside a nested lambda/runnable).

**Code Example:**
inline fun execute(crossinline task: () -> Unit) {
    runOnThread { task() } // allowed because of crossinline
}

[⬆️ Back to Top](#table-of-contents)

---

<a id="q36"></a>
### Q36: How do you use Contracts to help the compiler with smart casts?

**Difficulty**: Advanced

**Strategy**:
Contracts are an advanced feature that bridge the gap between what your code guarantees at runtime and what the compiler can verify statically. They are especially useful for utility functions that perform null checks or type checks, enabling smart casts in the calling code without explicit casts. Since contracts are still experimental, use them judiciously and ensure the contract accurately reflects the function's behavior to avoid misleading the compiler.

**Strategy:**
Use the `contract` builder to tell the compiler about function effects (e.g., if this function returns, argument is not null).

**Code Example:**
@OptIn(ExperimentalContracts::class)
fun isValid(s: String?): Boolean {
    contract {
        returns(true) implies (s != null)
    }
    return s != null && s.isNotEmpty()
}

if (isValid(name)) {
    println(name.length) // Smart cast to String
}

[⬆️ Back to Top](#table-of-contents)

---

<a id="q37"></a>
### Q37: How do you use Functional (SAM) interfaces?

**Difficulty**: Intermediate

**Strategy**:
SAM (Single Abstract Method) conversion is Kotlin's way of enabling lambda-based instantiation of single-method interfaces, which is essential for Java interoperability and writing clean callback APIs. Marking an interface with `fun interface` makes the intent explicit and allows the compiler to optimize the conversion. This pattern is cleaner than using a full object expression and is the idiomatic way to define listener or callback types.

**Strategy:**
Define an interface with `fun interface`. You can then instantiate it using a lambda.

**Code Example:**
fun interface Predicate {
    fun accept(i: Int): Boolean
}

val isEven = Predicate { it % 2 == 0 }

[⬆️ Back to Top](#table-of-contents)

---

<a id="q38"></a>
### Q38: How do you use Destructuring in lambdas?

**Difficulty**: Beginner

**Strategy**:
Destructuring in lambdas eliminates the need for intermediate variables when working with pairs, data classes, or map entries inside functional chains like `map`, `filter`, or `forEach`. It makes collection processing code significantly more concise and readable. A limitation to remember is that Kotlin does not support destructuring for regular classes, only for types that declare `componentN()` functions (data classes, Pair, Triple, Map.Entry).

**Strategy:**
If a lambda parameter is a data class or Map.Entry, you can destructure it directly in the parameter list.

**Code Example:**
map.forEach { (key, value) ->
    println("$key -> $value")
}

[⬆️ Back to Top](#table-of-contents)

---

<a id="q39"></a>
### Q39: How do you use Receiver Functions (`String.() -> Unit`)?

**Difficulty**: Advanced

**Strategy**:
Function literals with receivers are the building block behind Kotlin's most powerful features including DSLs, scope functions (`apply`, `with`), and Compose modifiers. They let you define a block of code that operates as if it were a member of the receiver type. Understanding this concept is critical for reading and writing library code, and the main challenge is keeping track of which receiver is in scope when multiple are nested.

**Strategy:**
A lambda with a receiver type allows you to access members of the receiver object implicitly (used in DSLs and `apply`).

**Code Example:**
val buildString: StringBuilder.() -> Unit = {
    append("Hello")
    append(" World")
}

val sb = StringBuilder()
sb.buildString()

[⬆️ Back to Top](#table-of-contents)

---

<a id="q40"></a>
### Q40: How do you delegate properties to a Map?

**Difficulty**: Intermediate

**Strategy**:
Delegating properties to a Map is a surprisingly useful technique for dynamically typed data like JSON parsing, configuration objects, or database rows where keys match property names. It leverages Kotlin's built-in `Map` delegate extension functions, avoiding manual key lookups. A pitfall is that type mismatches between the map value and the property type will cause `ClassCastException` at runtime, so this pattern works best with trusted data sources.

**Strategy:**
Use a Map instance as a delegate for properties. The map keys must match property names.

**Code Example:**
class User(val map: Map<String, Any?>) {
    val name: String by map
    val age: Int by map
}

[⬆️ Back to Top](#table-of-contents)

---

<a id="q41"></a>
### Q41: How do you perform bitwise operations in Kotlin?

**Difficulty**: Beginner

**Strategy**:
Unlike Java and C which use symbolic operators (`&`, `|`, `<<`), Kotlin uses named infix functions for bitwise operations, which improves readability but surprises developers coming from those languages. These operations are essential for working with flags, permissions, compression algorithms, and low-level protocol handling. The key is remembering that these are infix function calls, not operators, so they follow function call precedence rules.

**Strategy:**
Use named infix functions: `shl` (shift left), `shr` (shift right), `and`, `or`, `xor`, `inv`.

**Code Example:**
val flags = 0b1010
val mask = 0b0010
val result = flags and mask // 0b0010

[⬆️ Back to Top](#table-of-contents)

---

<a id="q42"></a>
### Q42: What is Covariance (`out`) and Contravariance (`in`)?

**Difficulty**: Advanced

**Strategy**:
Variance is one of the most challenging generics concepts in interviews because it governs subtyping relationships between generic types. The rule of thumb is "producer uses `out`, consumer uses `in`" (PECS principle). Covariance (`out`) allows a `Source<String>` to be assigned where a `Source<Any>` is expected, while contravariance (`in`) allows the reverse. Getting variance wrong leads to either compiler errors or unsafe type casts at runtime.

**Strategy:**
- `out T` (Producer): Can only read T. `List<out String>` can accept `String` or `Any` (subtype to supertype).
- `in T` (Consumer): Can only write T. `Comparable<in Number>` can compare `Number` or `Double`.

**Code Example:**
interface Source<out T> { fun next(): T }
interface Sink<in T> { fun put(x: T) }

[⬆️ Back to Top](#table-of-contents)

---

<a id="q43"></a>
### Q43: How do you use `Dispatchers.Unconfined`?

**Difficulty**: Advanced

**Strategy**:
`Dispatchers.Unconfined` is a specialized dispatcher that avoids any thread confinement, which makes it useful for testing and debugging but dangerous in production. Because the coroutine can resume on any thread, it breaks assumptions about thread safety and can cause unpredictable ordering issues. Interviewers ask about this to verify you understand why the standard dispatchers (Main, IO, Default) exist and when deviating from them is appropriate.

**Strategy:**
It starts the coroutine in the current thread, but resumes in whatever thread the suspending function used. Generally avoided in application code.

**Code Example:**
launch(Dispatchers.Unconfined) {
    println(Thread.currentThread().name) // Main
    delay(100)
    println(Thread.currentThread().name) // DefaultExecutor
}

[⬆️ Back to Top](#table-of-contents)

---

<a id="q44"></a>
### Q44: How do you buffer a Flow?

**Difficulty**: Intermediate

**Strategy**:
When the emitter is faster than the collector, Flow's default behavior is to suspend the emitter until the collector finishes, which can become a bottleneck. The `buffer()` operator introduces a concurrent buffer between the two, allowing the emitter to continue producing values while the collector processes previous ones. Be mindful of buffer capacity limits and consider `conflate` if you only care about the latest value rather than every emission.

**Strategy:**
Use the `buffer()` operator. It allows the emitter to continue emitting without waiting for the collector to finish processing the previous item.

**Code Example:**
flow.buffer().collect { ... }

[⬆️ Back to Top](#table-of-contents)

---

<a id="q45"></a>
### Q45: How do you combine multiple Flows (`zip`, `combine`)?

**Difficulty**: Intermediate

**Strategy**:
Combining multiple reactive streams is a common real-world requirement, such as merging network responses with local cache data or pairing user input with search results. `zip` produces a value only when both flows have emitted, pairing them strictly, which is ideal for parallel API calls. `combine` is reactive and emits whenever either flow changes, making it suitable for derived state. Choosing the wrong one leads to stale data or unnecessary emissions.

**Strategy:**
- `zip`: Waits for both flows to emit, pairs them 1-to-1.
- `combine`: Emits whenever *any* flow emits, using the latest value from the others.

**Code Example:**
flowA.combine(flowB) { a, b -> "$a-$b" }

[⬆️ Back to Top](#table-of-contents)

---

<a id="q46"></a>
### Q46: How do you use `ConflatedBroadcastChannel` (or `StateFlow`)?

**Difficulty**: Advanced

**Strategy**:
Understanding deprecated API migrations demonstrates that you stay current with Kotlin's evolving coroutines library. `ConflatedBroadcastChannel` was the original way to broadcast a single conflate value, but it had complex lifecycle issues that led to its replacement by `StateFlow` and `SharedFlow`. When migrating, be aware that `StateFlow` requires an initial value while `ConflatedBroadcastChannel` did not, which can affect how you model optional or nullable states.

**Strategy:**
`ConflatedBroadcastChannel` is deprecated. Use `StateFlow` or `SharedFlow` with `replay=1, onBufferOverflow=DROP_OLDEST`.

**Code Example:**
val shared = MutableSharedFlow<Int>(replay = 1, onBufferOverflow = BufferOverflow.DROP_OLDEST)
shared.tryEmit(1)

[⬆️ Back to Top](#table-of-contents)

---

<a id="q47"></a>
### Q47: How do you mock final classes in Kotlin with Mockito?

**Difficulty**: Intermediate

**Strategy**:
Testing is a critical part of production development, and Kotlin's default-final classes create a unique challenge since Mockito cannot mock final classes without extra configuration. The `mockito-inline` extension enables mocking of final classes without modifying production code, keeping your tests clean. A best practice is to prefer interface-based dependency injection so you can mock interfaces instead, reserving `mockito-inline` as a fallback for third-party or legacy classes.

**Strategy:**
Kotlin classes are final by default. Use `mockito-inline` dependency or open the class/methods with `open` modifier (not recommended just for tests).

**Code Example:**
// build.gradle
testImplementation "org.mockito:mockito-inline:4.0.0" 

[⬆️ Back to Top](#table-of-contents)

---

<a id="q48"></a>
### Q48: How do you use `measureTimeMillis` for benchmarking?

**Difficulty**: Beginner

**Strategy**:
Performance measurement is a practical skill that interviewers use to check whether you can diagnose bottlenecks and validate optimizations. `measureTimeMillis` is the simplest way to time a block of code without manually recording start and end timestamps. For production benchmarking, prefer `kotlinx-benchmark` or Android's `Benchmark` library, since `measureTimeMillis` includes warm-up overhead and JVM optimization effects that can skew results.

**Strategy:**
Wrap code in `measureTimeMillis` to get execution time in milliseconds.

**Code Example:**
val time = measureTimeMillis {
    heavyTask()
}
println("Took $time ms")

[⬆️ Back to Top](#table-of-contents)

---

<a id="q49"></a>
### Q49: How do you create a singleton with arguments?

**Difficulty**: Intermediate

**Strategy**:
Real-world singletons often need runtime dependencies like context, configuration, or API keys, which Kotlin's `object` declaration cannot accept. This question tests whether you can implement the classic pattern with thread-safe lazy initialization while accepting parameters. The main pitfall is race conditions during initialization, so always use `synchronized` or a `lazy` delegate to ensure thread safety when multiple threads might call `getInstance` simultaneously.

**Strategy:**
Kotlin `object` cannot have constructors. Use a class with a `companion object` containing a `getInstance(arg)` method (checking for null/instance).

**Code Example:**
class Singleton private constructor(val arg: String) {
    companion object {
        private var instance: Singleton? = null
        fun getInstance(arg: String) = instance ?: Singleton(arg).also { instance = it }
    }
}

[⬆️ Back to Top](#table-of-contents)

---

<a id="q50"></a>
### Q50: How do you use `remember` in Jetpack Compose (Kotlin context)?

**Difficulty**: Intermediate

**Strategy**:
`remember` is fundamental to Compose's state management model and frequently appears in Android Kotlin interviews. Without `remember`, objects would be recreated on every recomposition, causing unnecessary allocations, lost state, and flickering UI. A common pitfall is forgetting to pair `remember` with `mutableStateOf` when the value needs to trigger recomposition, or using `remember` for values that should actually reset on recomposition.

**Strategy:**
Although Compose specific, `remember` caches objects across recompositions. It works by storing values in the slot table.

**Code Example:**
@Composable
fun MyWidget() {
    val interactionSource = remember { MutableInteractionSource() }
}

[⬆️ Back to Top](#table-of-contents)
