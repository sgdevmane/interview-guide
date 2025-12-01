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
50. [How do you use `remember` in Jetpack Compose (Kotlin context)?](#q50-how-do-you-use-remember-in-jetpack-compose-kotlin-context) <span class="intermediate">Intermediate</span>
51. [How do you handle Kotlin state management in large scale applications?](#q51-how-do-you-handle-kotlin-state-management-in-large-scale-applications) <span class="advanced">Advanced</span>
52. [How do you perform Kotlin data validation in microservices?](#q52-how-do-you-perform-kotlin-data-validation-in-microservices) <span class="beginner">Beginner</span>
53. [How do you automate Kotlin deployment for mobile devices?](#q53-how-do-you-automate-kotlin-deployment-for-mobile-devices) <span class="advanced">Advanced</span>
54. [How do you handle Kotlin concurrency issues in legacy systems?](#q54-how-do-you-handle-kotlin-concurrency-issues-in-legacy-systems) <span class="advanced">Advanced</span>
55. [How do you implement Kotlin caching in cloud infrastructure?](#q55-how-do-you-implement-kotlin-caching-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
56. [How do you manage Kotlin configuration for real-time systems?](#q56-how-do-you-manage-kotlin-configuration-for-real-time-systems) <span class="beginner">Beginner</span>
57. [How do you handle Kotlin internationalization (i18n) in distributed systems?](#q57-how-do-you-handle-kotlin-internationalization-i18n-in-distributed-systems) <span class="intermediate">Intermediate</span>
58. [How do you ensure Kotlin accessibility (a11y) in high-traffic sites?](#q58-how-do-you-ensure-kotlin-accessibility-a11y-in-high-traffic-sites) <span class="beginner">Beginner</span>
59. [How do you optimize Kotlin network requests in embedded systems?](#q59-how-do-you-optimize-kotlin-network-requests-in-embedded-systems) <span class="advanced">Advanced</span>
60. [How do you handle Kotlin performance optimization for production environments?](#q60-how-do-you-handle-kotlin-performance-optimization-for-production-environments) <span class="advanced">Advanced</span>
61. [What are the security implications of Kotlin in large scale applications?](#q61-what-are-the-security-implications-of-kotlin-in-large-scale-applications) <span class="intermediate">Intermediate</span>
62. [How do you debug Kotlin memory leaks in microservices?](#q62-how-do-you-debug-kotlin-memory-leaks-in-microservices) <span class="advanced">Advanced</span>
63. [Best practices for Kotlin code organization in mobile devices?](#q63-best-practices-for-kotlin-code-organization-in-mobile-devices) <span class="beginner">Beginner</span>
64. [How do you implement Kotlin error handling for legacy systems?](#q64-how-do-you-implement-kotlin-error-handling-for-legacy-systems) <span class="intermediate">Intermediate</span>
65. [How do you test Kotlin functionality in cloud infrastructure?](#q65-how-do-you-test-kotlin-functionality-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
66. [How do you handle Kotlin state management in real-time systems?](#q66-how-do-you-handle-kotlin-state-management-in-real-time-systems) <span class="advanced">Advanced</span>
67. [How do you perform Kotlin data validation in distributed systems?](#q67-how-do-you-perform-kotlin-data-validation-in-distributed-systems) <span class="beginner">Beginner</span>
68. [How do you automate Kotlin deployment for high-traffic sites?](#q68-how-do-you-automate-kotlin-deployment-for-high-traffic-sites) <span class="advanced">Advanced</span>
69. [How do you handle Kotlin concurrency issues in embedded systems?](#q69-how-do-you-handle-kotlin-concurrency-issues-in-embedded-systems) <span class="advanced">Advanced</span>
70. [How do you implement Kotlin caching in production environments?](#q70-how-do-you-implement-kotlin-caching-in-production-environments) <span class="intermediate">Intermediate</span>
71. [How do you manage Kotlin configuration for large scale applications?](#q71-how-do-you-manage-kotlin-configuration-for-large-scale-applications) <span class="beginner">Beginner</span>
72. [How do you handle Kotlin internationalization (i18n) in microservices?](#q72-how-do-you-handle-kotlin-internationalization-i18n-in-microservices) <span class="intermediate">Intermediate</span>
73. [How do you ensure Kotlin accessibility (a11y) in mobile devices?](#q73-how-do-you-ensure-kotlin-accessibility-a11y-in-mobile-devices) <span class="beginner">Beginner</span>
74. [How do you optimize Kotlin network requests in legacy systems?](#q74-how-do-you-optimize-kotlin-network-requests-in-legacy-systems) <span class="advanced">Advanced</span>
75. [How do you handle Kotlin performance optimization for cloud infrastructure?](#q75-how-do-you-handle-kotlin-performance-optimization-for-cloud-infrastructure) <span class="advanced">Advanced</span>
76. [What are the security implications of Kotlin in real-time systems?](#q76-what-are-the-security-implications-of-kotlin-in-real-time-systems) <span class="intermediate">Intermediate</span>
77. [How do you debug Kotlin memory leaks in distributed systems?](#q77-how-do-you-debug-kotlin-memory-leaks-in-distributed-systems) <span class="advanced">Advanced</span>
78. [Best practices for Kotlin code organization in high-traffic sites?](#q78-best-practices-for-kotlin-code-organization-in-high-traffic-sites) <span class="beginner">Beginner</span>
79. [How do you implement Kotlin error handling for embedded systems?](#q79-how-do-you-implement-kotlin-error-handling-for-embedded-systems) <span class="intermediate">Intermediate</span>
80. [How do you test Kotlin functionality in production environments?](#q80-how-do-you-test-kotlin-functionality-in-production-environments) <span class="intermediate">Intermediate</span>
81. [How do you handle Kotlin state management in large scale applications?](#q81-how-do-you-handle-kotlin-state-management-in-large-scale-applications) <span class="advanced">Advanced</span>
82. [How do you perform Kotlin data validation in microservices?](#q82-how-do-you-perform-kotlin-data-validation-in-microservices) <span class="beginner">Beginner</span>
83. [How do you automate Kotlin deployment for mobile devices?](#q83-how-do-you-automate-kotlin-deployment-for-mobile-devices) <span class="advanced">Advanced</span>
84. [How do you handle Kotlin concurrency issues in legacy systems?](#q84-how-do-you-handle-kotlin-concurrency-issues-in-legacy-systems) <span class="advanced">Advanced</span>
85. [How do you implement Kotlin caching in cloud infrastructure?](#q85-how-do-you-implement-kotlin-caching-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
86. [How do you manage Kotlin configuration for real-time systems?](#q86-how-do-you-manage-kotlin-configuration-for-real-time-systems) <span class="beginner">Beginner</span>
87. [How do you handle Kotlin internationalization (i18n) in distributed systems?](#q87-how-do-you-handle-kotlin-internationalization-i18n-in-distributed-systems) <span class="intermediate">Intermediate</span>
88. [How do you ensure Kotlin accessibility (a11y) in high-traffic sites?](#q88-how-do-you-ensure-kotlin-accessibility-a11y-in-high-traffic-sites) <span class="beginner">Beginner</span>
89. [How do you optimize Kotlin network requests in embedded systems?](#q89-how-do-you-optimize-kotlin-network-requests-in-embedded-systems) <span class="advanced">Advanced</span>
90. [How do you handle Kotlin performance optimization for production environments?](#q90-how-do-you-handle-kotlin-performance-optimization-for-production-environments) <span class="advanced">Advanced</span>
91. [What are the security implications of Kotlin in large scale applications?](#q91-what-are-the-security-implications-of-kotlin-in-large-scale-applications) <span class="intermediate">Intermediate</span>
92. [How do you debug Kotlin memory leaks in microservices?](#q92-how-do-you-debug-kotlin-memory-leaks-in-microservices) <span class="advanced">Advanced</span>
93. [Best practices for Kotlin code organization in mobile devices?](#q93-best-practices-for-kotlin-code-organization-in-mobile-devices) <span class="beginner">Beginner</span>
94. [How do you implement Kotlin error handling for legacy systems?](#q94-how-do-you-implement-kotlin-error-handling-for-legacy-systems) <span class="intermediate">Intermediate</span>
95. [How do you test Kotlin functionality in cloud infrastructure?](#q95-how-do-you-test-kotlin-functionality-in-cloud-infrastructure) <span class="intermediate">Intermediate</span>
96. [How do you handle Kotlin state management in real-time systems?](#q96-how-do-you-handle-kotlin-state-management-in-real-time-systems) <span class="advanced">Advanced</span>
97. [How do you perform Kotlin data validation in distributed systems?](#q97-how-do-you-perform-kotlin-data-validation-in-distributed-systems) <span class="beginner">Beginner</span>
98. [How do you automate Kotlin deployment for high-traffic sites?](#q98-how-do-you-automate-kotlin-deployment-for-high-traffic-sites) <span class="advanced">Advanced</span>
99. [How do you handle Kotlin concurrency issues in embedded systems?](#q99-how-do-you-handle-kotlin-concurrency-issues-in-embedded-systems) <span class="advanced">Advanced</span>
100. [How do you implement Kotlin caching in production environments?](#q100-how-do-you-implement-kotlin-caching-in-production-environments) <span class="intermediate">Intermediate</span>

---

### Q1: How do you prevent blocking the Main Thread when performing network operations in Kotlin?

**Difficulty**: Beginner

**Strategy**:

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

### Q2: How do you choose between `val`, `var`, `const val`, and `lateinit var`?

**Difficulty**: Beginner

**Strategy**:

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

### Q3: How do you use Sealed Classes to model UI state effectively?

**Difficulty**: Intermediate

**Strategy**:

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

### Q4: How do you safely handle null values without using the `!!` operator?

**Difficulty**: Beginner

**Strategy**:

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

### Q5: How do you optimize collection processing using Sequences?

**Difficulty**: Intermediate

**Strategy**:

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

### Q6: How do you implement the Singleton pattern in Kotlin?

**Difficulty**: Beginner

**Strategy**:

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

### Q7: How do you extend a class functionality without inheriting from it (Extension Functions)?

**Difficulty**: Intermediate

**Strategy**:

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

### Q8: How do you use `StateFlow` vs `SharedFlow` for event handling?

**Difficulty**: Advanced

**Strategy**:

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

### Q9: How do you delegate property logic using the `by` keyword?

**Difficulty**: Intermediate

**Strategy**:

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

### Q10: How do you handle structured concurrency to ensure no coroutines leak?

**Difficulty**: Advanced

**Strategy**:

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

### Q11: How do you access the reified type parameter in an inline function?

**Difficulty**: Advanced

**Strategy**:

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

### Q12: How do you filter a list of objects and return a new list containing only non-null results?

**Difficulty**: Beginner

**Strategy**:

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

### Q13: How do you create a Domain Specific Language (DSL) in Kotlin?

**Difficulty**: Expert

**Strategy**:

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

### Q14: How do you use Destructuring Declarations to return multiple values?

**Difficulty**: Beginner

**Strategy**:

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

### Q15: How do you choose between `apply`, `also`, `let`, `run`, and `with`?

**Difficulty**: Intermediate

**Strategy**:

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

### Q16: How do you use `value class` (Inline Classes) to optimize memory?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Use `value class` (formerly `inline class`) to wrap a single value without allocating a new object on the heap. Useful for type safety (e.g., Password, ID).

**Code Example:**
@JvmInline
value class Password(val s: String)

// At runtime, this is just a String, but compile-time checks prevent mixing it with other Strings.
fun login(p: Password) {}

[⬆️ Back to Top](#table-of-contents)

---

### Q17: What is the difference between `sealed class` and `sealed interface`?

**Difficulty**: Intermediate

**Strategy**:

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

### Q18: When should you use `init` blocks?

**Difficulty**: Beginner

**Strategy**:

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

### Q19: How do you make Kotlin code Java-friendly using `@JvmStatic` and `@JvmOverloads`?

**Difficulty**: Intermediate

**Strategy**:

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

### Q20: How do you optimize recursion using `tailrec`?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Mark a function as `tailrec` if the recursive call is the last operation. The compiler optimizes it into a fast loop, preventing StackOverflowError.

**Code Example:**
tailrec fun factorial(n: Int, run: Int = 1): Int {
    return if (n == 1) run else factorial(n - 1, run * n)
}

[⬆️ Back to Top](#table-of-contents)

---

### Q21: How do you create readable DSL-like code using `infix` functions?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Mark a member or extension function as `infix` to call it without dots and parentheses. It must take exactly one parameter.

**Code Example:**
infix fun Int.times(str: String) = str.repeat(this)

// Usage
val result = 3 times "Hello " // "Hello Hello Hello " 

[⬆️ Back to Top](#table-of-contents)

---

### Q22: How do you overload operators (e.g., `+`, `[]`)?

**Difficulty**: Intermediate

**Strategy**:

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

### Q23: How do you validate arguments using `check`, `require`, and `assert`?

**Difficulty**: Beginner

**Strategy**:

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

### Q24: What is the difference between `runBlocking` and `coroutineScope`?

**Difficulty**: Intermediate

**Strategy**:

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

### Q25: How do you handle Flow emissions with `collect` vs `collectLatest`?

**Difficulty**: Advanced

**Strategy**:

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

### Q26: How do you convert a callback-based API to a Flow (`callbackFlow`)?

**Difficulty**: Advanced

**Strategy**:

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

### Q27: How do you ensure thread safety using `Mutex`?

**Difficulty**: Advanced

**Strategy**:

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

### Q28: How do you handle exceptions in Coroutines globally?

**Difficulty**: Advanced

**Strategy**:

**Strategy:**
Use `CoroutineExceptionHandler` attached to the scope or root coroutine. Note: It only catches uncaught exceptions (not valid for `async` which expects user to call `await`).

**Code Example:**
val handler = CoroutineExceptionHandler { _, exception ->
    println("Caught $exception")
}
val scope = CoroutineScope(Job() + handler)

[⬆️ Back to Top](#table-of-contents)

---

### Q29: How do you use `SupervisorJob` to prevent failure propagation?

**Difficulty**: Advanced

**Strategy**:

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

### Q30: How do you define multiplatform code using `expect` and `actual`?

**Difficulty**: Intermediate

**Strategy**:

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

### Q31: How do you generate a Sequence using `sequence { yield }`?

**Difficulty**: Intermediate

**Strategy**:

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

### Q32: How do you use `Nothing` type to represent unreachable code?

**Difficulty**: Intermediate

**Strategy**:

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

### Q33: What is a `typealias` and when to use it?

**Difficulty**: Beginner

**Strategy**:

**Strategy:**
It provides an alternative name for an existing type. Useful for shortening long generic types or function types.

**Code Example:**
typealias Handler = (Int, String, Boolean) -> Unit

fun register(h: Handler) {}

[⬆️ Back to Top](#table-of-contents)

---

### Q34: How do you control backing fields using the `field` identifier?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Inside a custom setter, use `field` to access the backing memory of the property to avoid infinite recursion.

**Code Example:**
var counter = 0
    set(value) {
        if (value >= 0) field = value
    }

[⬆️ Back to Top](#table-of-contents)

---

### Q35: How do you prevent a lambda parameter from being inlined (`noinline`, `crossinline`)?

**Difficulty**: Advanced

**Strategy**:

**Strategy:**
- `noinline`: Do not inline this lambda (e.g., passing it to another function).
- `crossinline`: Allow inlining but forbid non-local returns (e.g., using inside a nested lambda/runnable).

**Code Example:**
inline fun execute(crossinline task: () -> Unit) {
    runOnThread { task() } // allowed because of crossinline
}

[⬆️ Back to Top](#table-of-contents)

---

### Q36: How do you use Contracts to help the compiler with smart casts?

**Difficulty**: Advanced

**Strategy**:

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

### Q37: How do you use Functional (SAM) interfaces?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Define an interface with `fun interface`. You can then instantiate it using a lambda.

**Code Example:**
fun interface Predicate {
    fun accept(i: Int): Boolean
}

val isEven = Predicate { it % 2 == 0 }

[⬆️ Back to Top](#table-of-contents)

---

### Q38: How do you use Destructuring in lambdas?

**Difficulty**: Beginner

**Strategy**:

**Strategy:**
If a lambda parameter is a data class or Map.Entry, you can destructure it directly in the parameter list.

**Code Example:**
map.forEach { (key, value) ->
    println("$key -> $value")
}

[⬆️ Back to Top](#table-of-contents)

---

### Q39: How do you use Receiver Functions (`String.() -> Unit`)?

**Difficulty**: Advanced

**Strategy**:

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

### Q40: How do you delegate properties to a Map?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Use a Map instance as a delegate for properties. The map keys must match property names.

**Code Example:**
class User(val map: Map<String, Any?>) {
    val name: String by map
    val age: Int by map
}

[⬆️ Back to Top](#table-of-contents)

---

### Q41: How do you perform bitwise operations in Kotlin?

**Difficulty**: Beginner

**Strategy**:

**Strategy:**
Use named infix functions: `shl` (shift left), `shr` (shift right), `and`, `or`, `xor`, `inv`.

**Code Example:**
val flags = 0b1010
val mask = 0b0010
val result = flags and mask // 0b0010

[⬆️ Back to Top](#table-of-contents)

---

### Q42: What is Covariance (`out`) and Contravariance (`in`)?

**Difficulty**: Advanced

**Strategy**:

**Strategy:**
- `out T` (Producer): Can only read T. `List<out String>` can accept `String` or `Any` (subtype to supertype).
- `in T` (Consumer): Can only write T. `Comparable<in Number>` can compare `Number` or `Double`.

**Code Example:**
interface Source<out T> { fun next(): T }
interface Sink<in T> { fun put(x: T) }

[⬆️ Back to Top](#table-of-contents)

---

### Q43: How do you use `Dispatchers.Unconfined`?

**Difficulty**: Advanced

**Strategy**:

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

### Q44: How do you buffer a Flow?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Use the `buffer()` operator. It allows the emitter to continue emitting without waiting for the collector to finish processing the previous item.

**Code Example:**
flow.buffer().collect { ... }

[⬆️ Back to Top](#table-of-contents)

---

### Q45: How do you combine multiple Flows (`zip`, `combine`)?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
- `zip`: Waits for both flows to emit, pairs them 1-to-1.
- `combine`: Emits whenever *any* flow emits, using the latest value from the others.

**Code Example:**
flowA.combine(flowB) { a, b -> "$a-$b" }

[⬆️ Back to Top](#table-of-contents)

---

### Q46: How do you use `ConflatedBroadcastChannel` (or `StateFlow`)?

**Difficulty**: Advanced

**Strategy**:

**Strategy:**
`ConflatedBroadcastChannel` is deprecated. Use `StateFlow` or `SharedFlow` with `replay=1, onBufferOverflow=DROP_OLDEST`.

**Code Example:**
val shared = MutableSharedFlow<Int>(replay = 1, onBufferOverflow = BufferOverflow.DROP_OLDEST)
shared.tryEmit(1)

[⬆️ Back to Top](#table-of-contents)

---

### Q47: How do you mock final classes in Kotlin with Mockito?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Kotlin classes are final by default. Use `mockito-inline` dependency or open the class/methods with `open` modifier (not recommended just for tests).

**Code Example:**
// build.gradle
testImplementation "org.mockito:mockito-inline:4.0.0" 

[⬆️ Back to Top](#table-of-contents)

---

### Q48: How do you use `measureTimeMillis` for benchmarking?

**Difficulty**: Beginner

**Strategy**:

**Strategy:**
Wrap code in `measureTimeMillis` to get execution time in milliseconds.

**Code Example:**
val time = measureTimeMillis {
    heavyTask()
}
println("Took $time ms")

[⬆️ Back to Top](#table-of-contents)

---

### Q49: How do you create a singleton with arguments?

**Difficulty**: Intermediate

**Strategy**:

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

### Q50: How do you use `remember` in Jetpack Compose (Kotlin context)?

**Difficulty**: Intermediate

**Strategy**:

**Strategy:**
Although Compose specific, `remember` caches objects across recompositions. It works by storing values in the slot table.

**Code Example:**
@Composable
fun MyWidget() {
    val interactionSource = remember { MutableInteractionSource() }
}

[⬆️ Back to Top](#table-of-contents)

---


### Q51: How do you handle Kotlin state management in large scale applications?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```java
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q52: How do you perform Kotlin data validation in microservices?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```java
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q53: How do you automate Kotlin deployment for mobile devices?

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

### Q54: How do you handle Kotlin concurrency issues in legacy systems?

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

### Q55: How do you implement Kotlin caching in cloud infrastructure?

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

### Q56: How do you manage Kotlin configuration for real-time systems?

**Difficulty**: Beginner

**Strategy**:
Use environment variables or config files. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```java
const config = process.env.CONFIG || 'default';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q57: How do you handle Kotlin internationalization (i18n) in distributed systems?

**Difficulty**: Intermediate

**Strategy**:
Use i18n libraries. Extract strings to resource files.

**Code Example**:
```java
t('welcome_message')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q58: How do you ensure Kotlin accessibility (a11y) in high-traffic sites?

**Difficulty**: Beginner

**Strategy**:
Use semantic HTML and ARIA roles. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```java
<button aria-label="Close">X</button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q59: How do you optimize Kotlin network requests in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use batching, debouncing, or GraphQL. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```java
debounce(() => fetch(), 300);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q60: How do you handle Kotlin performance optimization for production environments?

**Difficulty**: Advanced

**Strategy**:
Profile first, then optimize hot paths. Use caching and efficient algorithms.

**Code Example**:
```java
const start = performance.now();
// Kotlin logic
const end = performance.now();
console.log('Time:', end - start);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q61: What are the security implications of Kotlin in large scale applications?

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

### Q62: How do you debug Kotlin memory leaks in microservices?

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

### Q63: Best practices for Kotlin code organization in mobile devices?

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

### Q64: How do you implement Kotlin error handling for legacy systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```java
try {
  await KotlinOperation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q65: How do you test Kotlin functionality in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```java
test('Kotlin works', () => {
  expect(Kotlin()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q66: How do you handle Kotlin state management in real-time systems?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```java
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q67: How do you perform Kotlin data validation in distributed systems?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```java
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q68: How do you automate Kotlin deployment for high-traffic sites?

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

### Q69: How do you handle Kotlin concurrency issues in embedded systems?

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

### Q70: How do you implement Kotlin caching in production environments?

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

### Q71: How do you manage Kotlin configuration for large scale applications?

**Difficulty**: Beginner

**Strategy**:
Use environment variables or config files. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```java
const config = process.env.CONFIG || 'default';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q72: How do you handle Kotlin internationalization (i18n) in microservices?

**Difficulty**: Intermediate

**Strategy**:
Use i18n libraries. Extract strings to resource files.

**Code Example**:
```java
t('welcome_message')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q73: How do you ensure Kotlin accessibility (a11y) in mobile devices?

**Difficulty**: Beginner

**Strategy**:
Use semantic HTML and ARIA roles. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```java
<button aria-label="Close">X</button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q74: How do you optimize Kotlin network requests in legacy systems?

**Difficulty**: Advanced

**Strategy**:
Use batching, debouncing, or GraphQL. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```java
debounce(() => fetch(), 300);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q75: How do you handle Kotlin performance optimization for cloud infrastructure?

**Difficulty**: Advanced

**Strategy**:
Profile first, then optimize hot paths. Use caching and efficient algorithms.

**Code Example**:
```java
const start = performance.now();
// Kotlin logic
const end = performance.now();
console.log('Time:', end - start);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q76: What are the security implications of Kotlin in real-time systems?

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

### Q77: How do you debug Kotlin memory leaks in distributed systems?

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

### Q78: Best practices for Kotlin code organization in high-traffic sites?

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

### Q79: How do you implement Kotlin error handling for embedded systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```java
try {
  await KotlinOperation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q80: How do you test Kotlin functionality in production environments?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```java
test('Kotlin works', () => {
  expect(Kotlin()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q81: How do you handle Kotlin state management in large scale applications?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```java
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q82: How do you perform Kotlin data validation in microservices?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```java
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q83: How do you automate Kotlin deployment for mobile devices?

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

### Q84: How do you handle Kotlin concurrency issues in legacy systems?

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

### Q85: How do you implement Kotlin caching in cloud infrastructure?

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

### Q86: How do you manage Kotlin configuration for real-time systems?

**Difficulty**: Beginner

**Strategy**:
Use environment variables or config files. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```java
const config = process.env.CONFIG || 'default';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q87: How do you handle Kotlin internationalization (i18n) in distributed systems?

**Difficulty**: Intermediate

**Strategy**:
Use i18n libraries. Extract strings to resource files.

**Code Example**:
```java
t('welcome_message')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q88: How do you ensure Kotlin accessibility (a11y) in high-traffic sites?

**Difficulty**: Beginner

**Strategy**:
Use semantic HTML and ARIA roles. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```java
<button aria-label="Close">X</button>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q89: How do you optimize Kotlin network requests in embedded systems?

**Difficulty**: Advanced

**Strategy**:
Use batching, debouncing, or GraphQL. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```java
debounce(() => fetch(), 300);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q90: How do you handle Kotlin performance optimization for production environments?

**Difficulty**: Advanced

**Strategy**:
Profile first, then optimize hot paths. Use caching and efficient algorithms.

**Code Example**:
```java
const start = performance.now();
// Kotlin logic
const end = performance.now();
console.log('Time:', end - start);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q91: What are the security implications of Kotlin in large scale applications?

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

### Q92: How do you debug Kotlin memory leaks in microservices?

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

### Q93: Best practices for Kotlin code organization in mobile devices?

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

### Q94: How do you implement Kotlin error handling for legacy systems?

**Difficulty**: Intermediate

**Strategy**:
Use try/catch blocks or global error boundaries. Log errors for monitoring.

**Code Example**:
```java
try {
  await KotlinOperation();
} catch (e) {
  logger.error(e);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q95: How do you test Kotlin functionality in cloud infrastructure?

**Difficulty**: Intermediate

**Strategy**:
Write unit tests for logic and integration tests for flows.

**Code Example**:
```java
test('Kotlin works', () => {
  expect(Kotlin()).toBe(true);
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q96: How do you handle Kotlin state management in real-time systems?

**Difficulty**: Advanced

**Strategy**:
Use immutable state where possible. Avoid prop drilling.

**Code Example**:
```java
const [state, setState] = useState(initial);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q97: How do you perform Kotlin data validation in distributed systems?

**Difficulty**: Beginner

**Strategy**:
Use schema validation libraries (Zod, Joi) or custom checks.

**Code Example**:
```java
if (!schema.safeParse(data).success) throw Error('Invalid');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q98: How do you automate Kotlin deployment for high-traffic sites?

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

### Q99: How do you handle Kotlin concurrency issues in embedded systems?

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

### Q100: How do you implement Kotlin caching in production environments?

**Difficulty**: Intermediate

**Strategy**:
Use Redis or in-memory LRU caches. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```java
const cache = new Map();
if (cache.has(key)) return cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>
