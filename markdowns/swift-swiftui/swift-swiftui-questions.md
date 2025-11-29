# Swift & SwiftUI Interview Questions

## Table of Contents
- [Swift \& SwiftUI Interview Questions](#swift--swiftui-interview-questions)
  - [Table of Contents](#table-of-contents)
    - [Q1: What is the difference between a class and a struct in Swift?](#q1-what-is-the-difference-between-a-class-and-a-struct-in-swift)
    - [Q2: Explain optionals in Swift and how to safely unwrap them.](#q2-explain-optionals-in-swift-and-how-to-safely-unwrap-them)
    - [Q3: What is Automatic Reference Counting (ARC) in Swift?](#q3-what-is-automatic-reference-counting-arc-in-swift)
    - [Q4: Explain closures in Swift. What are trailing closures?](#q4-explain-closures-in-swift-what-are-trailing-closures)
    - [Q5: What are protocols and delegates in Swift?](#q5-what-are-protocols-and-delegates-in-swift)
    - [Q6: What are generics in Swift?](#q6-what-are-generics-in-swift)
    - [Q7: Explain error handling in Swift (try, catch, throw).](#q7-explain-error-handling-in-swift-try-catch-throw)
    - [Q8: What is the difference between `let` and `var`?](#q8-what-is-the-difference-between-let-and-var)
    - [Q9: What is Grand Central Dispatch (GCD)?](#q9-what-is-grand-central-dispatch-gcd)
    - [Q10: What is Swift Concurrency (async/await)?](#q10-what-is-swift-concurrency-asyncawait)
    - [Q11: What is a View in SwiftUI?](#q11-what-is-a-view-in-swiftui)
    - [Q12: What are modifiers in SwiftUI?](#q12-what-are-modifiers-in-swiftui)
    - [Q13: Explain the difference between @State, @Binding, @ObservedObject, and @EnvironmentObject.](#q13-explain-the-difference-between-state-binding-observedobject-and-environmentobject)
    - [Q14: What is the Combine framework?](#q14-what-is-the-combine-framework)
    - [Q15: How do you handle navigation in SwiftUI?](#q15-how-do-you-handle-navigation-in-swiftui)
    - [Q16: What is the purpose of the `Identifiable` protocol?](#q16-what-is-the-purpose-of-the-identifiable-protocol)
    - [Q17: What are property wrappers in Swift?](#q17-what-are-property-wrappers-in-swift)
    - [Q18: What is the difference between `Any` and `AnyObject`?](#q18-what-is-the-difference-between-any-and-anyobject)
    - [Q19: What is a result type in Swift?](#q19-what-is-a-result-type-in-swift)
    - [Q20: What is the purpose of the `Codable` protocol?](#q20-what-is-the-purpose-of-the-codable-protocol)
    - [Q21: What are Extensions in Swift?](#q21-what-are-extensions-in-swift)
    - [Q22: What is the difference between Escaping and Non-Escaping Closures?](#q22-what-is-the-difference-between-escaping-and-non-escaping-closures)
    - [Q23: What is ARC (Automatic Reference Counting)?](#q23-what-is-arc-automatic-reference-counting)
    - [Q24: What is the difference between `weak` and `unowned` references?](#q24-what-is-the-difference-between-weak-and-unowned-references)
    - [Q25: What are Strong Reference Cycles (Retain Cycles)?](#q25-what-are-strong-reference-cycles-retain-cycles)
    - [Q26: Value Types vs Reference Types?](#q26-value-types-vs-reference-types)
    - [Q27: Explain Access Control levels in Swift.](#q27-explain-access-control-levels-in-swift)
    - [Q28: What are Computed Properties?](#q28-what-are-computed-properties)
    - [Q29: What are Lazy Stored Properties?](#q29-what-are-lazy-stored-properties)
    - [Q30: What are Property Observers?](#q30-what-are-property-observers)
    - [Q31: What is Protocol Oriented Programming (POP)?](#q31-what-is-protocol-oriented-programming-pop)
    - [Q32: What are Protocol Extensions?](#q32-what-are-protocol-extensions)
    - [Q33: What are Associated Types?](#q33-what-are-associated-types)
    - [Q34: What are Opaque Types (`some View`)?](#q34-what-are-opaque-types-some-view)
    - [Q35: What are Generic Constraints?](#q35-what-are-generic-constraints)
    - [Q36: `Equatable` vs `Hashable`.](#q36-equatable-vs-hashable)
    - [Q37: What is `CaseIterable`?](#q37-what-is-caseiterable)
    - [Q38: Raw Values vs Associated Values in Enums.](#q38-raw-values-vs-associated-values-in-enums)
    - [Q39: What are KeyPaths?](#q39-what-are-keypaths)
    - [Q40: What is `#selector`?](#q40-what-is-selector)
    - [Q41: What is Copy-on-Write (CoW)?](#q41-what-is-copy-on-write-cow)
    - [Q42: What is the `defer` statement?](#q42-what-is-the-defer-statement)
    - [Q43: `guard` vs `if let`.](#q43-guard-vs-if-let)
    - [Q44: `fatalError` vs `assert` vs `precondition`.](#q44-fatalerror-vs-assert-vs-precondition)
    - [Q45: What is Type Casting (`as`, `as?`, `as!`)?](#q45-what-is-type-casting-as-as-as)
    - [Q46: `Any` vs `AnyObject`.](#q46-any-vs-anyobject)
    - [Q47: Higher Order Functions (`map`, `filter`, `reduce`).](#q47-higher-order-functions-map-filter-reduce)
    - [Q48: `compactMap` vs `flatMap`.](#q48-compactmap-vs-flatmap)
    - [Q49: What is `zip`?](#q49-what-is-zip)
    - [Q50: What are Subscripts?](#q50-what-are-subscripts)
    - [Q51: Explain SwiftUI Lifecycle (`onAppear`, `task`).](#q51-explain-swiftui-lifecycle-onappear-task)
    - [Q52: `@StateObject` vs `@ObservedObject`.](#q52-stateobject-vs-observedobject)
    - [Q53: `@Environment` vs `@EnvironmentObject`.](#q53-environment-vs-environmentobject)
    - [Q54: `@AppStorage` vs `@SceneStorage`.](#q54-appstorage-vs-scenestorage)
    - [Q55: What is `@FocusState`?](#q55-what-is-focusstate)
    - [Q56: What is `@Binding`?](#q56-what-is-binding)
    - [Q57: What is `GeometryReader`?](#q57-what-is-geometryreader)
    - [Q58: What is `PreferenceKey`?](#q58-what-is-preferencekey)
    - [Q59: `ZStack` vs `VStack` vs `HStack`.](#q59-zstack-vs-vstack-vs-hstack)
    - [Q60: `LazyVStack` vs `VStack`.](#q60-lazyvstack-vs-vstack)
    - [Q61: What is `ScrollViewReader`?](#q61-what-is-scrollviewreader)
    - [Q62: Implicit vs Explicit Animations.](#q62-implicit-vs-explicit-animations)
    - [Q63: What are Transitions?](#q63-what-are-transitions)
    - [Q64: What is `matchedGeometryEffect`?](#q64-what-is-matchedgeometryeffect)
    - [Q65: What is `@ViewBuilder`?](#q65-what-is-viewbuilder)
    - [Q66: How do you create Custom Modifiers?](#q66-how-do-you-create-custom-modifiers)
    - [Q67: What is `UIViewRepresentable`?](#q67-what-is-uiviewrepresentable)
    - [Q68: Coordinator Pattern in SwiftUI.](#q68-coordinator-pattern-in-swiftui)
    - [Q69: What is `ObservableObject`?](#q69-what-is-observableobject)
    - [Q70: What is `@Published`?](#q70-what-is-published)
    - [Q71: Combine: Publisher vs Subscriber.](#q71-combine-publisher-vs-subscriber)
    - [Q72: What is `AnyCancellable`?](#q72-what-is-anycancellable)
    - [Q73: `PassthroughSubject` vs `CurrentValueSubject`.](#q73-passthroughsubject-vs-currentvaluesubject)
    - [Q74: `debounce` vs `throttle` in Combine.](#q74-debounce-vs-throttle-in-combine)
    - [Q75: `merge` vs `zip` vs `combineLatest`.](#q75-merge-vs-zip-vs-combinelatest)
    - [Q76: What are Actors in Swift?](#q76-what-are-actors-in-swift)
    - [Q77: What is `@MainActor`?](#q77-what-is-mainactor)
    - [Q78: What is `TaskGroup`?](#q78-what-is-taskgroup)
    - [Q79: What is `async let`?](#q79-what-is-async-let)
    - [Q80: What are Continuations (`CheckedContinuation`)?](#q80-what-are-continuations-checkedcontinuation)
    - [Q81: What is `NSManagedObject`?](#q81-what-is-nsmanagedobject)
    - [Q82: What is `PersistentContainer`?](#q82-what-is-persistentcontainer)
    - [Q83: What is `FetchRequest`?](#q83-what-is-fetchrequest)
    - [Q84: URLSession `dataTask` vs `uploadTask` vs `downloadTask`.](#q84-urlsession-datatask-vs-uploadtask-vs-downloadtask)
    - [Q85: `JSONDecoder` and `JSONEncoder`.](#q85-jsondecoder-and-jsonencoder)
    - [Q86: What are `CodingKeys`?](#q86-what-are-codingkeys)
    - [Q87: Memory Management in Closures (Capture Lists).](#q87-memory-management-in-closures-capture-lists)
    - [Q88: What are Autoclosures?](#q88-what-are-autoclosures)
    - [Q89: What are `inout` parameters?](#q89-what-are-inout-parameters)
    - [Q90: Explain Method Dispatch in Swift.](#q90-explain-method-dispatch-in-swift)
    - [Q91: What is KVO (Key-Value Observing)?](#q91-what-is-kvo-key-value-observing)
    - [Q92: What is KVC (Key-Value Coding)?](#q92-what-is-kvc-key-value-coding)
    - [Q93: `setUp` and `tearDown` in XCTest.](#q93-setup-and-teardown-in-xctest)
    - [Q94: What is `XCTestExpectation`?](#q94-what-is-xctestexpectation)
    - [Q95: UI Testing in Xcode.](#q95-ui-testing-in-xcode)
    - [Q96: What are Instruments?](#q96-what-are-instruments)
    - [Q97: MVVM (Model-View-ViewModel) Pattern.](#q97-mvvm-model-view-viewmodel-pattern)
    - [Q98: VIPER Pattern.](#q98-viper-pattern)
    - [Q99: Singleton Pattern in Swift.](#q99-singleton-pattern-in-swift)
    - [Q100: What is the future of Swift?](#q100-what-is-the-future-of-swift)

---

### Q1: What is the difference between a class and a struct in Swift?

**Answer:**
The main differences between classes and structs in Swift revolve around their underlying implementation (reference vs. value types), which has significant implications for memory management, performance, and data integrity.

| Feature | Class | Struct |
| :--- | :--- | :--- |
| **Type** | Reference Type | Value Type |
| **Memory Management** | Stored in the heap, managed by ARC | Stored on the stack (usually) |
| **Assignment** | Copies a reference to the same instance | Creates a new copy of the instance |
| **Inheritance** | Can inherit from other classes | Cannot inherit |
| **Mutability** | `let` constant can have mutable properties | `let` constant is fully immutable |
| **Deinitializers** | Can have `deinit` | Cannot have `deinit` |

**Choosing Between Class and Struct:**

Use a **struct** when:
- The primary purpose is to encapsulate a few simple data values.
- You expect instances to be copied rather than referenced.
- You don't need inheritance from a base type.
- You want to ensure data immutability and thread safety.

Use a **class** when:
- You need Objective-C interoperability.
- You need to control the identity of an instance (e.g., a shared resource).
- You require inheritance to model a hierarchy of objects.
- You need a deinitializer to clean up resources.

**Code Example:**

```swift
// Struct Example (Value Type)
struct Point {
    var x: Int
    var y: Int
}

var p1 = Point(x: 10, y: 20)
var p2 = p1 // p2 is a new copy of p1
p2.x = 100

print("p1.x: \(p1.x)") // Output: p1.x: 10
print("p2.x: \(p2.x)") // Output: p2.x: 100

// Class Example (Reference Type)
class View {
    var width: Int
    var height: Int

    init(width: Int, height: Int) {
        self.width = width
        self.height = height
    }
}

var v1 = View(width: 300, height: 200)
var v2 = v1 // v2 is a reference to the same instance as v1
v2.width = 600

print("v1.width: \(v1.width)") // Output: v1.width: 600
print("v2.width: \(v2.width)") // Output: v2.width: 600
```



### Q2: Explain optionals in Swift and how to safely unwrap them.

**Answer:**
Optionals are a core feature of Swift designed to handle the absence of a value. An optional is a type that can either hold a value or be `nil`.

**Safe Unwrapping Techniques:**

1.  **Optional Binding (`if let` and `guard let`):**
    ```swift
    var optionalName: String? = "John"

    if let name = optionalName {
        print("Hello, \(name)")
    } else {
        print("No name provided")
    }

    func greet(name: String?) {
        guard let unwrappedName = name else {
            print("Name is nil")
            return
        }
        print("Welcome, \(unwrappedName)")
    }
    ```

2.  **Nil-Coalescing Operator (`??`):**
    ```swift
    let name = optionalName ?? "Guest"
    print("User: \(name)")
    ```

3.  **Optional Chaining (`?.`):**
    ```swift
    struct Person {
        var address: Address?
    }
    struct Address {
        var street: String?
    }
    let person = Person()
    let streetName = person.address?.street?.uppercased() // Returns nil without crashing
    ```

4.  **Force Unwrapping (`!`):** (Use with caution)
    ```swift
    let forcedName = optionalName!
    ```

### Q3: What is Automatic Reference Counting (ARC) in Swift?

**Answer:**
ARC is Swift's memory management system. It automatically tracks and manages the memory usage of your app. When an instance of a class is no longer needed, ARC deallocates the memory used by that instance.

### Q4: Explain closures in Swift. What are trailing closures?

**Answer:**
Closures are self-contained blocks of functionality that can be passed around and used in your code. They can capture and store references to any constants and variables from the context in which they are defined.

**Trailing Closures:**
If a closure is the last argument to a function, you can write it after the function's parentheses. This leads to cleaner, more readable code.

```swift
func performAction(action: () -> Void) {
    action()
}

// Using a trailing closure
performAction { 
    print("Action performed!")
}
```

### Q5: What are protocols and delegates in Swift?

**Answer:**
-   **Protocols:** A protocol defines a blueprint of methods, properties, and other requirements that suit a particular task or piece of functionality. Classes, structs, and enums can then adopt the protocol to provide an actual implementation of those requirements.
-   **Delegation:** A design pattern that enables a class or struct to hand off (or delegate) some of its responsibilities to an instance of another type. This is often implemented using protocols.

### Q6: What are generics in Swift?

**Answer:**
Generics allow you to write flexible, reusable functions and types that can work with any type, subject to requirements that you define.

```swift
func swapValues<T>(_ a: inout T, _ b: inout T) {
    let temp = a
    a = b
    b = temp
}
```

### Q7: Explain error handling in Swift (try, catch, throw).

**Answer:**
Swift provides a powerful error handling model that allows you to represent and handle errors in your code. It uses the `try`, `catch`, and `throw` keywords.

```swift
enum MyError: Error {
    case someError
}

func mightThrow() throws {
    throw MyError.someError
}

do {
    try mightThrow()
} catch {
    print("An error occurred: \(error)")
}
```

### Q8: What is the difference between `let` and `var`?

**Answer:**
-   `let` is used to declare a constant (immutable).
-   `var` is used to declare a variable (mutable).

### Q9: What is Grand Central Dispatch (GCD)?

**Answer:**
GCD is a low-level API for managing concurrent operations. It helps you improve your app's responsiveness by deferring computationally expensive tasks to the background.

### Q10: What is Swift Concurrency (async/await)?

**Answer:**
Introduced in Swift 5.5, `async/await` provides a structured way to write asynchronous code that is easier to read and understand than traditional completion handlers or GCD.

```swift
func fetchData() async -> Data? {
    // ... asynchronous network call
}

Task {
    if let data = await fetchData() {
        // ... process data
    }
}
```

### Q11: What is a View in SwiftUI?

**Answer:**
A `View` in SwiftUI is a protocol that describes a piece of your app's UI. Views are lightweight, value-type structs that you compose to build your UI.

### Q12: What are modifiers in SwiftUI?

**Answer:**
Modifiers are methods that you call on a view to configure its properties (e.g., `font`, `padding`, `foregroundColor`). Each modifier returns a new view with the modification applied.

### Q13: Explain the difference between @State, @Binding, @ObservedObject, and @EnvironmentObject.

**Answer:**
These are property wrappers used for data flow in SwiftUI:
-   `@State`: For simple value types that are owned and managed by a single view.
-   `@Binding`: Creates a two-way connection to a `@State` variable owned by another view.
-   `@ObservedObject`: For complex reference types (classes that conform to `ObservableObject`) that are owned and managed by a view.
-   `@EnvironmentObject`: Allows you to share an `ObservableObject` with all views in a hierarchy.

### Q14: What is the Combine framework?

**Answer:**
Combine is a declarative Swift API for processing values over time. It provides a unified way to handle asynchronous events, such as network responses and user interface events.

### Q15: How do you handle navigation in SwiftUI?

**Answer:**
Navigation in SwiftUI is typically handled using `NavigationView` and `NavigationLink` for push-style navigation, or by presenting views modally with the `.sheet` modifier.

### Q16: What is the purpose of the `Identifiable` protocol?

**Answer:**
The `Identifiable` protocol is used to uniquely identify elements in a collection, which is often required by SwiftUI views like `List` and `ForEach`.

### Q17: What are property wrappers in Swift?

**Answer:**
Property wrappers are a feature that adds a layer of separation between the code that manages how a property is stored and the code that defines a property.

### Q18: What is the difference between `Any` and `AnyObject`?

**Answer:**
-   `Any`: Can represent an instance of any type at all, including function types.
-   `AnyObject`: Can represent an instance of any class type.

### Q19: What is a result type in Swift?

**Answer:**
The `Result` type is an enum with two cases: `success` and `failure`. It's a convenient way to handle operations that can either succeed with a value or fail with an error.

### Q20: What is the purpose of the `Codable` protocol?

**Answer:**
The `Codable` protocol is a type alias for the `Encodable` and `Decodable` protocols. It allows you to easily encode and decode your custom data types to and from external representations like JSON or property lists.
### Q21: What are Extensions in Swift?
**Difficulty: Easy**

**Answer:**
Extensions add new functionality to an existing class, structure, enumeration, or protocol type. They can add computed properties, methods, initializers, and subscripts.

```swift
extension String {
    func reverse() -> String {
        return String(self.reversed())
    }
}
```

### Q22: What is the difference between Escaping and Non-Escaping Closures?
**Difficulty: Medium**

**Answer:**
- **Non-Escaping (`@noescape` default):** The closure is executed within the function body and returns before the function returns.
- **Escaping (`@escaping`):** The closure is stored to be executed later, after the function returns (e.g., asynchronous completion handlers).

```swift
func performAsync(completion: @escaping () -> Void) {
    DispatchQueue.main.async {
        completion()
    }
}
```

### Q23: What is ARC (Automatic Reference Counting)?
**Difficulty: Medium**

**Answer:**
ARC is Swift's memory management mechanism. It automatically tracks and manages your app's memory usage. It frees up memory used by class instances when they are no longer needed (reference count drops to zero).

### Q24: What is the difference between `weak` and `unowned` references?
**Difficulty: Medium**

**Answer:**
Both are used to prevent strong reference cycles.
- **`weak`:** The reference can become `nil` (must be optional `var`). It doesn't keep a strong hold on the instance.
- **`unowned`:** The reference is expected to always have a value (non-optional). If accessed after the instance is deallocated, it crashes.

### Q25: What are Strong Reference Cycles (Retain Cycles)?
**Difficulty: Medium**

**Answer:**
A situation where two class instances hold strong references to each other, preventing ARC from deallocating either. This causes memory leaks. It's common in closures and delegate patterns.

### Q26: Value Types vs Reference Types?
**Difficulty: Easy**

**Answer:**
- **Value Types (Struct, Enum, Tuple):** Copied when assigned to a variable or passed to a function.
- **Reference Types (Class, Closure, Actor):** Shared instance. Multiple variables can refer to the same object in memory.

### Q27: Explain Access Control levels in Swift.
**Difficulty: Medium**

**Answer:**
From least restrictive to most restrictive:
- **`open`:** Can be subclassed/overridden outside the module.
- **`public`:** Accessible outside the module, but cannot be subclassed/overridden.
- **`internal` (default):** Accessible within the entire module.
- **`fileprivate`:** Accessible only within the defining source file.
- **`private`:** Accessible only within the defining enclosing declaration.

### Q28: What are Computed Properties?
**Difficulty: Easy**

**Answer:**
Properties that do not store a value. Instead, they provide a getter and an optional setter to calculate a value dynamically.

```swift
var area: Double {
    get { return width * height }
    set { width = newValue / height }
}
```

### Q29: What are Lazy Stored Properties?
**Difficulty: Easy**

**Answer:**
A property whose initial value is not calculated until the first time it is used. Marked with `lazy`. Must be a `var`.

```swift
lazy var complexData = performExpensiveCalculation()
```

### Q30: What are Property Observers?
**Difficulty: Easy**

**Answer:**
Observe and respond to changes in a property's value.
- **`willSet`:** Called just before the value is stored.
- **`didSet`:** Called immediately after the new value is stored.

### Q31: What is Protocol Oriented Programming (POP)?
**Difficulty: Advanced**

**Answer:**
A programming paradigm in Swift where you design your app around protocols and protocol extensions. It promotes composition over inheritance, allowing you to add functionality to types without a deep class hierarchy.

### Q32: What are Protocol Extensions?
**Difficulty: Medium**

**Answer:**
They allow you to provide default implementations for method/property requirements of a protocol.

```swift
extension MyProtocol {
    func defaultMethod() { print("Default implementation") }
}
```

### Q33: What are Associated Types?
**Difficulty: Advanced**

**Answer:**
An associated type gives a placeholder name to a type that is used as part of the protocol. The actual type to use for that associated type isn't specified until the protocol is adopted.

```swift
protocol Container {
    associatedtype Item
    mutating func append(_ item: Item)
}
```

### Q34: What are Opaque Types (`some View`)?
**Difficulty: Advanced**

**Answer:**
Opaque types hide the specific return type of a function or property, preserving the type identity but hiding the implementation details. Heavily used in SwiftUI (`var body: some View`).

### Q35: What are Generic Constraints?
**Difficulty: Medium**

**Answer:**
Restricting the types that can be used with a generic function or type.
```swift
func findIndex<T: Equatable>(of value: T, in array: [T]) -> Int? { ... }
```

### Q36: `Equatable` vs `Hashable`.
**Difficulty: Easy**

**Answer:**
- **`Equatable`:** Allows instances to be compared for equality (`==`).
- **`Hashable`:** Allows instances to be hashed into an integer value (required for `Set` and `Dictionary` keys). `Hashable` inherits from `Equatable`.

### Q37: What is `CaseIterable`?
**Difficulty: Easy**

**Answer:**
A protocol that automatically generates a collection of all cases in an enum.
```swift
enum Direction: CaseIterable { case north, south, east, west }
let count = Direction.allCases.count
```

### Q38: Raw Values vs Associated Values in Enums.
**Difficulty: Medium**

**Answer:**
- **Raw Values:** Pre-populated values (Int, String, etc.) that are constant for each case.
- **Associated Values:** Custom data attached to each enum case instance, which can vary.

### Q39: What are KeyPaths?
**Difficulty: Advanced**

**Answer:**
A type-safe way to refer to a property of a type, rather than a specific value.
```swift
struct Person { var name: String }
let path = \Person.name
let p = Person(name: "John")
let name = p[keyPath: path]
```

### Q40: What is `#selector`?
**Difficulty: Medium**

**Answer:**
Used to refer to an Objective-C method. Required for older APIs like `NotificationCenter` or `Timer` (pre-block based).
```swift
@objc func timerFired() { ... }
let timer = Timer.scheduledTimer(..., selector: #selector(timerFired), ...)
```

### Q41: What is Copy-on-Write (CoW)?
**Difficulty: Advanced**

**Answer:**
An optimization technique used by Swift collections (Array, Dictionary). The data is copied only when you modify (write to) the second instance. Until then, both instances share the same memory.

### Q42: What is the `defer` statement?
**Difficulty: Medium**

**Answer:**
A block of code that executes just before the current scope exits (whether by return, error, or fallthrough). Useful for cleanup.

```swift
func process() {
    defer { print("Cleanup") }
    print("Processing")
}
```

### Q43: `guard` vs `if let`.
**Difficulty: Easy**

**Answer:**
- **`if let`:** Unwraps optional for the `if` block. Used when you want to handle the "has value" case.
- **`guard let`:** Unwraps optional for the rest of the scope. Requires an `else` block that exits the scope. Used for early exit.

### Q44: `fatalError` vs `assert` vs `precondition`.
**Difficulty: Advanced**

**Answer:**
- **`assert`:** Checks condition in Debug builds only.
- **`precondition`:** Checks condition in Debug and Release builds.
- **`fatalError`:** Crashes the app unconditionally in all builds.

### Q45: What is Type Casting (`as`, `as?`, `as!`)?
**Difficulty: Easy**

**Answer:**
- **`as`:** Upcasting (guaranteed success).
- **`as?`:** Downcasting (returns Optional, nil if fails).
- **`as!`:** Forced Downcasting (crashes if fails).

### Q46: `Any` vs `AnyObject`.
**Difficulty: Easy**

**Answer:**
- **`Any`:** Represents an instance of any type (structs, classes, functions).
- **`AnyObject`:** Represents an instance of any class type only.

### Q47: Higher Order Functions (`map`, `filter`, `reduce`).
**Difficulty: Medium**

**Answer:**
- **`map`:** Transforms each element.
- **`filter`:** Selects elements based on a condition.
- **`reduce`:** Combines all elements into a single value.

### Q48: `compactMap` vs `flatMap`.
**Difficulty: Medium**

**Answer:**
- **`compactMap`:** Transforms and removes `nil` results.
- **`flatMap`:** Flattens a collection of collections (e.g., `[[Int]]` to `[Int]`).

### Q49: What is `zip`?
**Difficulty: Medium**

**Answer:**
Combines two sequences into a sequence of pairs.
```swift
let pairs = zip([1, 2], ["A", "B"]) // [(1, "A"), (2, "B")]
```

### Q50: What are Subscripts?
**Difficulty: Easy**

**Answer:**
Shortcuts for accessing member elements of a collection, list, or sequence using `[]`.

```swift
subscript(index: Int) -> Int { ... }
```

### Q51: Explain SwiftUI Lifecycle (`onAppear`, `task`).
**Difficulty: Medium**

**Answer:**
- **`onAppear`:** Called when the view appears on screen.
- **`onDisappear`:** Called when the view disappears.
- **`task`:** Starts an async task when the view appears and cancels it when it disappears.

### Q52: `@StateObject` vs `@ObservedObject`.
**Difficulty: Medium**

**Answer:**
- **`@StateObject`:** The view OWNS the object. It initializes it. The object persists during view updates.
- **`@ObservedObject`:** The view OBSERVES an object passed to it. It does not own it.

### Q53: `@Environment` vs `@EnvironmentObject`.
**Difficulty: Medium**

**Answer:**
- **`@Environment`:** Access system-provided values (e.g., `colorScheme`, `presentationMode`).
- **`@EnvironmentObject`:** Access custom data models injected into the environment hierarchy.

### Q54: `@AppStorage` vs `@SceneStorage`.
**Difficulty: Medium**

**Answer:**
- **`@AppStorage`:** Wrapper around `UserDefaults`. Persists across app launches.
- **`@SceneStorage`:** Persists data per scene (window) for state restoration (cleared when scene is destroyed).

### Q55: What is `@FocusState`?
**Difficulty: Medium**

**Answer:**
A property wrapper used to control focus in SwiftUI views (e.g., focusing a `TextField`).

### Q56: What is `@Binding`?
**Difficulty: Easy**

**Answer:**
Allows a child view to read and write a value owned by a parent view (two-way data binding).

### Q57: What is `GeometryReader`?
**Difficulty: Advanced**

**Answer:**
A container view that provides access to the size and position (geometry) of its parent view. Used for custom layouts.

### Q58: What is `PreferenceKey`?
**Difficulty: Advanced**

**Answer:**
A mechanism to pass data UP the view hierarchy (from child to parent), opposite of Environment.

### Q59: `ZStack` vs `VStack` vs `HStack`.
**Difficulty: Easy**

**Answer:**
- **`VStack`:** Vertical layout.
- **`HStack`:** Horizontal layout.
- **`ZStack`:** Overlay layout (depth).

### Q60: `LazyVStack` vs `VStack`.
**Difficulty: Medium**

**Answer:**
`LazyVStack` only renders views that are currently visible on the screen (better performance for long lists). `VStack` renders all views immediately.

### Q61: What is `ScrollViewReader`?
**Difficulty: Medium**

**Answer:**
A view that provides a `ScrollViewProxy` to programmatically scroll to a specific location in a `ScrollView`.

### Q62: Implicit vs Explicit Animations.
**Difficulty: Medium**

**Answer:**
- **Implicit:** `.animation(.default, value: x)` attached to a view. Animates whenever `x` changes.
- **Explicit:** `withAnimation { x = newValues }`. Animates the state change specifically.

### Q63: What are Transitions?
**Difficulty: Medium**

**Answer:**
Animations that occur when a view is inserted or removed from the hierarchy (e.g., `.transition(.slide)`).

### Q64: What is `matchedGeometryEffect`?
**Difficulty: Advanced**

**Answer:**
Allows you to synchronize the geometry (position/size) of two different views, creating seamless animations (e.g., Hero animations).

### Q65: What is `@ViewBuilder`?
**Difficulty: Advanced**

**Answer:**
A result builder that constructs a view from a closure containing multiple child views. It allows omitting `return` and listing views sequentially.

### Q66: How do you create Custom Modifiers?
**Difficulty: Medium**

**Answer:**
Create a struct conforming to `ViewModifier` and implement `body(content: Content)`.
```swift
struct MyModifier: ViewModifier {
    func body(content: Content) -> some View {
        content.padding()
    }
}
```

### Q67: What is `UIViewRepresentable`?
**Difficulty: Medium**

**Answer:**
A protocol to wrap UIKit views so they can be used inside SwiftUI. Requires implementing `makeUIView` and `updateUIView`.

### Q68: Coordinator Pattern in SwiftUI.
**Difficulty: Advanced**

**Answer:**
Used with `UIViewRepresentable` to handle delegation and events from the UIKit view back to SwiftUI. The `Coordinator` class acts as the delegate.

### Q69: What is `ObservableObject`?
**Difficulty: Medium**

**Answer:**
A protocol for classes that allows them to publish changes to their properties, triggering UI updates in SwiftUI views observing them.

### Q70: What is `@Published`?
**Difficulty: Medium**

**Answer:**
A property wrapper used inside `ObservableObject` classes. When the property changes, it sends a notification to observers.

### Q71: Combine: Publisher vs Subscriber.
**Difficulty: Medium**

**Answer:**
- **Publisher:** Emits values over time.
- **Subscriber:** Receives and processes values from a publisher.

### Q72: What is `AnyCancellable`?
**Difficulty: Medium**

**Answer:**
A type-erasing cancellable object that executes a closure (cleanup) when deinitialized. Used to store subscriptions so they aren't cancelled immediately.

### Q73: `PassthroughSubject` vs `CurrentValueSubject`.
**Difficulty: Advanced**

**Answer:**
- **`PassthroughSubject`:** Broadcasts values to subscribers. Does not store the current value.
- **`CurrentValueSubject`:** Broadcasts values and stores the current value. New subscribers get the latest value immediately.

### Q74: `debounce` vs `throttle` in Combine.
**Difficulty: Advanced**

**Answer:**
- **`debounce`:** Emits a value only after a specified time has passed without another emission.
- **`throttle`:** Emits the first (or last) value within a specified time interval.

### Q75: `merge` vs `zip` vs `combineLatest`.
**Difficulty: Advanced**

**Answer:**
- **`merge`:** Interleaves elements from multiple publishers.
- **`zip`:** Pairs elements from multiple publishers (wait for all).
- **`combineLatest`:** Emits a tuple of the latest values from all publishers whenever any of them emits.

### Q76: What are Actors in Swift?
**Difficulty: Advanced**

**Answer:**
Reference types (like classes) that protect their mutable state from data races. They ensure that only one task can access their mutable state at a time.

```swift
actor BankAccount {
    var balance: Double = 0
    func deposit(amount: Double) { balance += amount }
}
```

### Q77: What is `@MainActor`?
**Difficulty: Medium**

**Answer:**
A global actor that represents the main thread. You annotate functions or classes with `@MainActor` to ensure they run on the main thread (essential for UI updates).

### Q78: What is `TaskGroup`?
**Difficulty: Advanced**

**Answer:**
Allows you to create a dynamic number of child tasks that run concurrently and collect their results.
```swift
await withTaskGroup(of: Int.self) { group in ... }
```

### Q79: What is `async let`?
**Difficulty: Medium**

**Answer:**
Allows you to start a child task to run concurrently with the current task.
```swift
async let result1 = fetch1()
async let result2 = fetch2()
let combined = await [result1, result2]
```

### Q80: What are Continuations (`CheckedContinuation`)?
**Difficulty: Advanced**

**Answer:**
A mechanism to interface legacy callback-based async code with modern `async/await` code. You suspend the task and resume it manually when the callback fires.

### Q81: What is `NSManagedObject`?
**Difficulty: Medium**

**Answer:**
The base class for all Core Data model objects. It represents a single record in the database.

### Q82: What is `PersistentContainer`?
**Difficulty: Medium**

**Answer:**
Encapsulates the Core Data stack (Context, Model, Coordinator, Store). Simplifies setup.

### Q83: What is `FetchRequest`?
**Difficulty: Medium**

**Answer:**
A description of search criteria used to retrieve data from a persistent store.

### Q84: URLSession `dataTask` vs `uploadTask` vs `downloadTask`.
**Difficulty: Medium**

**Answer:**
- **`dataTask`:** For small data transfers (JSON) in memory.
- **`uploadTask`:** For sending files/data.
- **`downloadTask`:** For retrieving data directly to a file.

### Q85: `JSONDecoder` and `JSONEncoder`.
**Difficulty: Easy**

**Answer:**
Helper classes to convert types conforming to `Codable` to/from JSON data.

### Q86: What are `CodingKeys`?
**Difficulty: Medium**

**Answer:**
An enum used to map custom property names to JSON keys that don't match.

```swift
enum CodingKeys: String, CodingKey {
    case firstName = "first_name"
}
```

### Q87: Memory Management in Closures (Capture Lists).
**Difficulty: Advanced**

**Answer:**
You use a capture list `[weak self]` or `[unowned self]` to define how values are captured in a closure to prevent retain cycles.

```swift
{ [weak self] in self?.doSomething() }
```

### Q88: What are Autoclosures?
**Difficulty: Advanced**

**Answer:**
A closure that is automatically created to wrap an expression that’s being passed as an argument to a function. It delays evaluation.

### Q89: What are `inout` parameters?
**Difficulty: Medium**

**Answer:**
Parameters that can be modified by a function, and the changes persist after the function returns.

### Q90: Explain Method Dispatch in Swift.
**Difficulty: Advanced**

**Answer:**
- **Static Dispatch:** Compile-time (Structs, final classes, extensions). Fastest.
- **Dynamic Dispatch (V-Table):** Runtime (Classes).
- **Message Dispatch:** Runtime (Obj-C runtime, `dynamic` modifier).

### Q91: What is KVO (Key-Value Observing)?
**Difficulty: Advanced**

**Answer:**
An Obj-C mechanism allowing objects to be notified of changes to specified properties of other objects. Requires `NSObject` inheritance and `@objc dynamic`.

### Q92: What is KVC (Key-Value Coding)?
**Difficulty: Advanced**

**Answer:**
Accessing object properties indirectly by name (String) rather than directly via property accessors.

### Q93: `setUp` and `tearDown` in XCTest.
**Difficulty: Easy**

**Answer:**
- **`setUp`:** Called before each test method. Used for initialization.
- **`tearDown`:** Called after each test method. Used for cleanup.

### Q94: What is `XCTestExpectation`?
**Difficulty: Medium**

**Answer:**
Used to test asynchronous code. You wait for the expectation to be fulfilled.

### Q95: UI Testing in Xcode.
**Difficulty: Medium**

**Answer:**
Uses `XCUIApplication` to launch the app and `XCUIElement` to interact with UI elements (tap, type, swipe) to verify behavior.

### Q96: What are Instruments?
**Difficulty: Advanced**

**Answer:**
A performance analysis and testing tool. Common instruments:
- **Time Profiler:** Identify CPU bottlenecks.
- **Leaks:** Detect memory leaks.
- **Allocations:** Monitor memory usage.

### Q97: MVVM (Model-View-ViewModel) Pattern.
**Difficulty: Medium**

**Answer:**
Separates business logic from UI.
- **Model:** Data.
- **View:** UI (SwiftUI View).
- **ViewModel:** Mediation logic (`ObservableObject`).

### Q98: VIPER Pattern.
**Difficulty: Advanced**

**Answer:**
View, Interactor, Presenter, Entity, Router. A very structured architecture promoting separation of concerns, often used in large iOS apps.

### Q99: Singleton Pattern in Swift.
**Difficulty: Easy**

**Answer:**
Ensures a class has only one instance and provides a global point of access.

```swift
class Manager {
    static let shared = Manager()
    private init() {}
}
```

### Q100: What is the future of Swift?
**Difficulty: Easy**

**Answer:**
Swift is expanding beyond iOS (Server-side Swift, Cross-platform). Focus on Concurrency safety (Swift 6), Macros, and performance (Embedded Swift).
