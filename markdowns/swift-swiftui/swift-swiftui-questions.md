<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>Swift & SwiftUI Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for developers</b></p>
</div>

---

## Table of Contents

1. [What is the difference between `class` and `struct` in Swift?](#q1-what-is-the-difference-between-class-and-struct-in-swift) <span class="beginner">Beginner</span>
2. [How do you implement a thread-safe counter using Swift Actors?](#q2-how-do-you-implement-a-thread-safe-counter-using-swift-actors) <span class="advanced">Advanced</span>
3. [How do you efficiently handle large lists of data in SwiftUI to avoid performance issues?](#q3-how-do-you-efficiently-handle-large-lists-of-data-in-swiftui-to-avoid-performance-issues) <span class="intermediate">Intermediate</span>
4. [How do you migrate legacy callback-based code to Swift Concurrency (async/await)?](#q4-how-do-you-migrate-legacy-callback-based-code-to-swift-concurrency-asyncawait) <span class="advanced">Advanced</span>
5. [How do you inject dependencies into a SwiftUI view hierarchy without passing them through every initializer?](#q5-how-do-you-inject-dependencies-into-a-swiftui-view-hierarchy-without-passing-them-through-every-initializer) <span class="intermediate">Intermediate</span>
6. [How do you implement custom error handling in a Swift network layer?](#q6-how-do-you-implement-custom-error-handling-in-a-swift-network-layer) <span class="intermediate">Intermediate</span>
7. [How do you optimize the performance of a SwiftUI view that updates too frequently?](#q7-how-do-you-optimize-the-performance-of-a-swiftui-view-that-updates-too-frequently) <span class="advanced">Advanced</span>
8. [How do you integrate a UIKit view (e.g., MKMapView) into a SwiftUI app?](#q8-how-do-you-integrate-a-uikit-view-e.g.-mkmapview-into-a-swiftui-app) <span class="intermediate">Intermediate</span>
9. [How do you implement Unit Tests for a ViewModel with async network calls?](#q9-how-do-you-implement-unit-tests-for-a-viewmodel-with-async-network-calls) <span class="advanced">Advanced</span>
10. [How do you handle deep linking in a SwiftUI application using the new NavigationStack?](#q10-how-do-you-handle-deep-linking-in-a-swiftui-application-using-the-new-navigationstack) <span class="advanced">Advanced</span>
11. [How do you manage the lifecycle of an `@ObservedObject` vs `@StateObject`?](#q11-how-do-you-manage-the-lifecycle-of-an-@observedobject-vs-@stateobject) <span class="beginner">Beginner</span>
12. [How do you implement custom property wrappers to validate user input automatically?](#q12-how-do-you-implement-custom-property-wrappers-to-validate-user-input-automatically) <span class="advanced">Advanced</span>
13. [How do you use the `some` and `any` keywords in Swift generics?](#q13-how-do-you-use-the-some-and-any-keywords-in-swift-generics) <span class="advanced">Advanced</span>
14. [How do you implement Codable for a JSON response with dynamic keys?](#q14-how-do-you-implement-codable-for-a-json-response-with-dynamic-keys) <span class="expert">Expert</span>
15. [How do you force a SwiftUI view to redraw without changing its state?](#q15-how-do-you-force-a-swiftui-view-to-redraw-without-changing-its-state) <span class="intermediate">Intermediate</span>
16. [How do you set up a basic Core Data Stack?](#q16-how-do-you-set-up-a-basic-core-data-stack) <span class="intermediate">Intermediate</span>
17. [How do you use Combine to handle a text field input with debounce?](#q17-how-do-you-use-combine-to-handle-a-text-field-input-with-debounce) <span class="intermediate">Intermediate</span>
18. [How do you create programmatic Auto Layout constraints?](#q18-how-do-you-create-programmatic-auto-layout-constraints) <span class="intermediate">Intermediate</span>
19. [How do you write a generic function that works with any Numeric type?](#q19-how-do-you-write-a-generic-function-that-works-with-any-numeric-type) <span class="beginner">Beginner</span>
20. [What is an escaping closure and when do you use it?](#q20-what-is-an-escaping-closure-and-when-do-you-use-it) <span class="intermediate">Intermediate</span>
21. [How do Structs (Value Types) differ from Classes (Reference Types) in mutation?](#q21-how-do-structs-value-types-differ-from-classes-reference-types-in-mutation) <span class="beginner">Beginner</span>
22. [How do you provide a default implementation for a Protocol method?](#q22-how-do-you-provide-a-default-implementation-for-a-protocol-method) <span class="intermediate">Intermediate</span>
23. [How do you add a computed property to an existing type using Extensions?](#q23-how-do-you-add-a-computed-property-to-an-existing-type-using-extensions) <span class="beginner">Beginner</span>
24. [How do you define and throw a custom Error?](#q24-how-do-you-define-and-throw-a-custom-error) <span class="beginner">Beginner</span>
25. [Why is Set lookup faster than Array lookup?](#q25-why-is-set-lookup-faster-than-array-lookup) <span class="intermediate">Intermediate</span>
26. [How do you support Dynamic Type (text scaling) in SwiftUI?](#q26-how-do-you-support-dynamic-type-text-scaling-in-swiftui) <span class="beginner">Beginner</span>
27. [How do you localize strings using NSLocalizedString?](#q27-how-do-you-localize-strings-using-nslocalizedstring) <span class="beginner">Beginner</span>
28. [What is the role of SceneDelegate vs AppDelegate?](#q28-what-is-the-role-of-scenedelegate-vs-appdelegate) <span class="intermediate">Intermediate</span>
29. [How do you write an async unit test with XCTest?](#q29-how-do-you-write-an-async-unit-test-with-xctest) <span class="intermediate">Intermediate</span>
30. [How do you configure a basic Fastfile for Fastlane?](#q30-how-do-you-configure-a-basic-fastfile-for-fastlane) <span class="intermediate">Intermediate</span>
31. [How do you define dependencies in Swift Package Manager?](#q31-how-do-you-define-dependencies-in-swift-package-manager) <span class="beginner">Beginner</span>
32. [How do you use `@MainActor` to ensure UI updates on the main thread?](#q32-how-do-you-use-@mainactor-to-ensure-ui-updates-on-the-main-thread) <span class="intermediate">Intermediate</span>
33. [When should you use the `defer` keyword?](#q33-when-should-you-use-the-defer-keyword) <span class="beginner">Beginner</span>
34. [How do you use a `lazy` stored property?](#q34-how-do-you-use-a-lazy-stored-property) <span class="beginner">Beginner</span>
35. [What is the difference between Computed and Stored properties?](#q35-what-is-the-difference-between-computed-and-stored-properties) <span class="beginner">Beginner</span>
36. [What is the difference between `guard` and `if let`?](#q36-what-is-the-difference-between-guard-and-if-let) <span class="beginner">Beginner</span>
37. [How do you handle custom date formats with Codable?](#q37-how-do-you-handle-custom-date-formats-with-codable) <span class="intermediate">Intermediate</span>
38. [How do you use the `Result` type?](#q38-how-do-you-use-the-result-type) <span class="intermediate">Intermediate</span>
39. [How do you use `map`, `filter`, and `reduce`?](#q39-how-do-you-use-map-filter-and-reduce) <span class="beginner">Beginner</span>
40. [How do you use KeyPaths in Swift?](#q40-how-do-you-use-keypaths-in-swift) <span class="intermediate">Intermediate</span>
41. [How do you implement the Singleton pattern correctly?](#q41-how-do-you-implement-the-singleton-pattern-correctly) <span class="beginner">Beginner</span>
42. [How do you use `DispatchGroup` to wait for multiple async tasks?](#q42-how-do-you-use-dispatchgroup-to-wait-for-multiple-async-tasks) <span class="intermediate">Intermediate</span>
43. [How do you use `OperationQueue` for dependent tasks?](#q43-how-do-you-use-operationqueue-for-dependent-tasks) <span class="advanced">Advanced</span>
44. [How do you configure `URLSession` caching?](#q44-how-do-you-configure-urlsession-caching) <span class="intermediate">Intermediate</span>
45. [How do you implement the Factory Pattern?](#q45-how-do-you-implement-the-factory-pattern) <span class="intermediate">Intermediate</span>
46. [How do you implement the Observer Pattern using NotificationCenter?](#q46-how-do-you-implement-the-observer-pattern-using-notificationcenter) <span class="intermediate">Intermediate</span>
47. [How do you use the Coordinator Pattern for navigation?](#q47-how-do-you-use-the-coordinator-pattern-for-navigation) <span class="advanced">Advanced</span>
48. [How do you optimize memory using `autoreleasepool`?](#q48-how-do-you-optimize-memory-using-autoreleasepool) <span class="advanced">Advanced</span>
49. [How do you check for API availability?](#q49-how-do-you-check-for-api-availability) <span class="beginner">Beginner</span>
50. [How do you prevent a retain cycle in a Delegate?](#q50) <span class="beginner">Beginner</span>

---

<a id="q1"></a>
### Q1: What is the difference between `class` and `struct` in Swift?

**Difficulty**: Beginner

**Strategy**:
This is one of the most fundamental Swift interview questions because the language deliberately favors structs over classes. Understanding value vs reference semantics is critical for writing predictable, bug-free code -- accidental sharing of class instances is a common source of subtle bugs. In practice, use structs by default and reach for classes only when you need identity sharing or inheritance. Be prepared to explain copy-on-write optimization for structs and how reference types affect memory management.

**Strategy:**
*   **Struct**: Value type (copied when passed). Stack allocated (faster). Immutable by default. No inheritance. (Use by default).
*   **Class**: Reference type (shared instance). Heap allocated. Supports inheritance and deinitializers.

**Code Example:**
```swift
struct UserStruct { var name: String }
class UserClass { var name: String; init(name: String) { self.name = name } }

var s1 = UserStruct(name: "A")
var s2 = s1
s2.name = "B" // s1 is still "A"

var c1 = UserClass(name: "A")
var c2 = c1
c2.name = "B" // c1 is now "B"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q2"></a>
### Q2: How do you implement a thread-safe counter using Swift Actors?

**Difficulty**: Advanced

**Strategy**:
Actors are Swift's built-in solution for data-race-safe concurrency, and interviewers ask this to verify you understand modern Swift concurrency beyond GCD. Unlike locks or serial queues, actors enforce isolation at the compiler level -- no other type in Swift provides this guarantee. A common pitfall is forgetting that actor properties and methods require `await` from outside the actor, which is the compiler enforcing safe access. Know when actors are preferable to `@MainActor` or `OSAllocatedUnfairLock`.

**Concept:**
Actors protect their mutable state by ensuring that only one task can access that state at a time, eliminating data races.

**Code Example:**
```swift
actor SafeCounter {
    private var value = 0
    
    func increment() {
        value += 1
    }
    
    func getValue() -> Int {
        return value
    }
}

// Usage
let counter = SafeCounter()
Task {
    await counter.increment()
    print(await counter.getValue())
}
```

---

<a id="q3"></a>
### Q3: How do you efficiently handle large lists of data in SwiftUI to avoid performance issues?

**Difficulty**: Intermediate

**Strategy**:
SwiftUI performance problems are a frequent interview topic because real-world apps routinely display hundreds or thousands of rows. The key insight is that `VStack` eagerly renders all children, while `LazyVStack` and `List` only instantiate visible rows. Always profile with Instruments to confirm lazy loading is working -- a common mistake is using non-lazy containers inside a ScrollView for large datasets. Also ensure each row view is lightweight and that your `Identifiable` conformance uses stable identifiers, not random UUIDs regenerated on each render.

**Strategy:**
1.  **Lazy Containers:** Use `LazyVStack` or `LazyHStack` inside a `ScrollView`, or simply `List` (which is lazy by default).
2.  **Identifiable:** Ensure data models conform to `Identifiable` for stable identity.

**Code Example:**
```swift
struct ContentView: View {
    let items = Array(1...1000)
    
    var body: some View {
        List(items, id: \.self) { item in
            Text("Row \(item)")
        }
    }
}
```

---

<a id="q4"></a>
### Q4: How do you migrate legacy callback-based code to Swift Concurrency (async/await)?

**Difficulty**: Advanced

**Strategy**:
Migrating callbacks to async/await is a practical concern for any team modernizing an established codebase. Interviewers want to see that you understand continuations are the bridge between the old and new worlds, and that you know the critical rule: a continuation must be resumed exactly once, or your program will crash or leak. In production, prefer wrapping legacy APIs in a dedicated adapter layer rather than sprinkling continuations throughout your code. Also know the difference between `withCheckedContinuation` (debug-friendly) and `withUnsafeContinuation` (zero-cost in release).

**Strategy:**
Use `withCheckedContinuation` or `withCheckedThrowingContinuation` to wrap the callback function.

**Code Example:**
```swift
// Legacy function
func fetchUser(completion: @escaping (Result<User, Error>) -> Void) { ... }

// Async wrapper
func fetchUserAsync() async throws -> User {
    return try await withCheckedThrowingContinuation { continuation in
        fetchUser { result in
            switch result {
            case .success(let user):
                continuation.resume(returning: user)
            case .failure(let error):
                continuation.resume(throwing: error)
            }
        }
    }
}
```

---

<a id="q5"></a>
### Q5: How do you inject dependencies into a SwiftUI view hierarchy without passing them through every initializer?

**Difficulty**: Intermediate

**Strategy**:
Environment-based dependency injection is central to SwiftUI architecture and eliminates the problem of prop-drilling through deeply nested views. Interviewers test this to confirm you can design a clean view hierarchy where shared state (user settings, theme, network client) is accessible anywhere without tight coupling. A common pitfall is forgetting to supply the `.environmentObject()` modifier, which causes a runtime crash. In larger apps, consider using the `.environment(\.key, value)` modifier with custom EnvironmentKey for lighter-weight values that don't need ObservableObject.

**Strategy:**
Use `@EnvironmentObject` for global dependencies or the `.environment` modifier.

**Code Example:**
```swift
class UserSettings: ObservableObject {
    @Published var username = "Guest"
}

struct ContentView: View {
    @StateObject var settings = UserSettings()
    
    var body: some View {
        ProfileView()
            .environmentObject(settings)
    }
}

struct ProfileView: View {
    @EnvironmentObject var settings: UserSettings
    
    var body: some View {
        Text("User: \(settings.username)")
    }
}
```

---

<a id="q6"></a>
### Q6: How do you implement custom error handling in a Swift network layer?

**Difficulty**: Intermediate

**Strategy**:
Robust error handling is what separates production-grade networking code from toy examples. Interviewers want to see typed, exhaustive error coverage using enums rather than passing generic `Error` around. The key approach is modeling every failure mode (bad URL, transport errors, HTTP status codes, decoding failures) as distinct cases so callers can handle each appropriately. Best practice: keep network errors in a dedicated module, avoid exposing internal details to the UI layer, and use `async throws` rather than completion handlers in modern Swift.

**Strategy:**
Define a custom `Error` enum and use `Result` types or `async throws`.

**Code Example:**
```swift
enum NetworkError: Error {
    case badURL
    case serverError(statusCode: Int)
    case decodingError
}

func fetchData(url: String) async throws -> Data {
    guard let validURL = URL(string: url) else {
        throw NetworkError.badURL
    }
    
    let (data, response) = try await URLSession.shared.data(from: validURL)
    
    guard let httpResponse = response as? HTTPURLResponse, (200...299).contains(httpResponse.statusCode) else {
        throw NetworkError.serverError(statusCode: (response as? HTTPURLResponse)?.statusCode ?? 500)
    }
    
    return data
}
```

---

<a id="q7"></a>
### Q7: How do you optimize the performance of a SwiftUI view that updates too frequently?

**Difficulty**: Advanced

**Strategy**:
Unnecessary re-renders are the number-one source of SwiftUI performance problems, and this question tests whether you can diagnose and fix them systematically. Start by using `Self._printChanges()` to identify which state change is triggering the redraw. The solution usually involves breaking large views into smaller subviews with isolated state, or using `EquatableView` to skip redraws when the data has not actually changed. A common mistake is putting a frequently-changing value (like a timer or animation progress) in a parent view, which forces every child to re-evaluate.

**Diagnosis:**
Use `Self._printChanges()` inside the view's `body` to identify what triggered the update.

**Fixes:**
1.  **Isolate State:** Move frequent state changes into smaller subviews.
2.  **EquatableView:** Conform views to `Equatable` and implement `static func ==`.

**Code Example:**
```swift
struct ExpensiveView: View, Equatable {
    let data: String
    
    static func == (lhs: ExpensiveView, rhs: ExpensiveView) -> Bool {
        return lhs.data == rhs.data
    }
    
    var body: some View {
        // Complex rendering
        Text(data)
    }
}
```

---

<a id="q8"></a>
### Q8: How do you integrate a UIKit view (e.g., MKMapView) into a SwiftUI app?

**Difficulty**: Intermediate

**Strategy**:
Not every UIKit component has a native SwiftUI equivalent, so bridging via `UIViewRepresentable` or `UIViewControllerRepresentable` is a skill you will use in almost every real project. Interviewers want to see that you understand the two-phase lifecycle (`makeUIView` for creation, `updateUIView` for SwiftUI state changes) and how to communicate delegate callbacks back to SwiftUI via a `Coordinator`. A common pitfall is forgetting to implement the `Coordinator` pattern, which is the standard way to forward UIKit delegate methods to your SwiftUI view.

**Strategy:**
Wrap the UIKit view in a struct conforming to `UIViewRepresentable`.

**Code Example:**
```swift
import SwiftUI
import MapKit

struct MapViewWrapper: UIViewRepresentable {
    func makeUIView(context: Context) -> MKMapView {
        return MKMapView()
    }
    
    func updateUIView(_ uiView: MKMapView, context: Context) {
        // Update map region etc.
    }
}
```

---

<a id="q9"></a>
### Q9: How do you implement Unit Tests for a ViewModel with async network calls?

**Difficulty**: Advanced

**Strategy**:
Testing async code with real network calls is unreliable and slow, so interviewers want to see you design for testability from the start using protocol-based dependency injection. The approach is to define a service protocol, inject a mock conforming to it in tests, and verify behavior without any network dependency. A key pitfall is not making your mock flexible enough to test error paths -- always create mocks that can simulate both success and failure. With Swift Concurrency, mark test methods `async throws` and let XCTest handle the async lifecycle.

**Strategy:**
Use dependency injection to mock the network service and `XCTest` expectations or async test methods.

**Code Example:**
```swift
// Protocol
protocol NetworkService {
    func fetchData() async throws -> String
}

// Mock
class MockService: NetworkService {
    var result: String = ""
    func fetchData() async throws -> String { return result }
}

// Test
func testViewModelFetch() async {
    let mock = MockService()
    mock.result = "Success"
    let viewModel = ViewModel(service: mock)
    
    await viewModel.loadData()
    
    XCTAssertEqual(viewModel.data, "Success")
}
```

---

<a id="q10"></a>
### Q10: How do you handle deep linking in a SwiftUI application using the new NavigationStack?

**Difficulty**: Advanced

**Strategy**:
Deep linking is essential for push notifications, Spotlight search, and universal links, and `NavigationStack` with programmatic navigation makes it far more manageable than the old `NavigationView`. Interviewers want to see that you understand `NavigationPath` as a type-erased collection you can manipulate programmatically, and that you handle incoming URLs by appending destinations to the path. A common pitfall is mixing old-style `NavigationLink(destination:)` with the new value-based API, which leads to unpredictable navigation behavior.

**Strategy:**
Bind the `NavigationStack` path to a state variable and append values to it when a deep link is received.

**Code Example:**
```swift
struct ContentView: View {
    @State private var path = NavigationPath()
    
    var body: some View {
        NavigationStack(path: $path) {
            List {
                NavigationLink("Go to Profile", value: "Profile")
            }
            .navigationDestination(for: String.self) { value in
                Text("Destination: \(value)")
            }
            .onOpenURL { url in
                if url.absoluteString.contains("profile") {
                    path.append("Profile")
                }
            }
        }
    }
}
```

---

<a id="q11"></a>
### Q11: How do you manage the lifecycle of an `@ObservedObject` vs `@StateObject`?

**Difficulty**: Beginner

**Strategy**:
Mixing up these two property wrappers is one of the most common SwiftUI bugs and a frequent interview question. The rule is straightforward: `@StateObject` owns and creates the object (use it once, at the top-level owner), while `@ObservedObject` receives an object that was created elsewhere. Using `@ObservedObject` where you should use `@StateObject` causes the object to be destroyed and recreated on every view re-render, silently losing state. This distinction matters for `ObservableObject`-based view models before the `@Observable` macro in iOS 17.

**Difference:**
*   `@StateObject`: Instantiates and owns the object. The object survives view re-renders. Use this when the view creates the object.
*   `@ObservedObject`: Observes an object created elsewhere. If the view re-renders, the object might be destroyed if not held strongly by a parent.

**Rule of Thumb:**
Use `@StateObject` for creation, `@ObservedObject` for dependency injection.

**Code Example:**
```swift
struct ParentView: View {
    @StateObject var viewModel = ViewModel() // Created here
    
    var body: some View {
        ChildView(viewModel: viewModel)
    }
}

struct ChildView: View {
    @ObservedObject var viewModel: ViewModel // Passed in
    ...
}
```

---

<a id="q12"></a>
### Q12: How do you implement custom property wrappers to validate user input automatically?

**Difficulty**: Advanced

**Strategy**:
Property wrappers are a powerful metaprogramming feature that interviewers use to test your understanding of Swift's type system beyond everyday usage. They encapsulate reusable get/set logic -- validation, transformation, clamping -- so you write it once and apply it declaratively with `@WrapperName`. The key concept is the `wrappedValue` computed property where your logic lives. A pitfall to avoid: property wrappers cannot add stored properties to a type, only computed behavior. They are most impactful when the same validation rule appears across many models in your codebase.

**Strategy:**
Create a struct with `@propertyWrapper` that handles the validation logic in its `wrappedValue` set block.

**Code Example:**
```swift
@propertyWrapper
struct Capitalized {
    private var value: String = ""
    
    var wrappedValue: String {
        get { value }
        set { value = newValue.capitalized }
    }
    
    init(wrappedValue: String) {
        self.wrappedValue = wrappedValue
    }
}

struct User {
    @Capitalized var name: String
}

var user = User(name: "john")
print(user.name) // "John"
```

---

<a id="q13"></a>
### Q13: How do you use the `some` and `any` keywords in Swift generics?

**Difficulty**: Advanced

**Strategy**:
Swift 5.7 formalized the distinction between opaque and existential types, and this question tests your understanding of compile-time vs runtime polymorphism. `some` (opaque return type) preserves concrete type information for static dispatch and is what makes SwiftUI's `some View` performant. `any` (existential) erases the type and uses dynamic dispatch, which is more flexible but incurs overhead. In interviews, explain that `some` should be preferred for return types and generic constraints, while `any` is useful when you truly need heterogeneous collections of protocol-conforming values.

**Concepts:**
*   `some Protocol` (Opaque Type): Returns a specific concrete type that conforms to the protocol, but the identity is hidden. Performance is better (static dispatch).
*   `any Protocol` (Existential Type): A box that can hold *any* type conforming to the protocol. More flexible but has runtime overhead (dynamic dispatch).

**Code Example:**
```swift
func makeView() -> some View { Text("Hello") } // Opaque
func process(items: [any Equatable]) { ... }   // Existential
```

---

<a id="q14"></a>
### Q14: How do you implement Codable for a JSON response with dynamic keys?

**Difficulty**: Expert

**Strategy**:
Real-world APIs often return objects with unpredictable key names (e.g., user IDs as keys), which breaks the standard `CodingKeys` enum approach. Interviewers ask this to see if you can go beyond auto-generated `Codable` conformance and manually control decoding. The technique is to decode the top-level structure as a `[String: Value]` dictionary, then iterate or access values by key. For more complex scenarios, implement `init(from decoder:)` with a `KeyedDecodingContainer` and `allKeys` enumeration. Always handle the case where a dynamic key maps to invalid data.

**Strategy:**
Use `Dictionary<String, Value>` or a custom decoding strategy with `CodingKeys` is not sufficient. For truly dynamic keys, decoding into a Dictionary is best.

**Code Example:**
```swift
let json = """
{
    "user_1": {"name": "A"},
    "user_2": {"name": "B"}
}
""".data(using: .utf8)!

struct User: Codable {
    let name: String
}

// Decode as Dictionary
let users = try JSONDecoder().decode([String: User].self, from: json)
print(users["user_1"]?.name ?? "")
```

---

<a id="q15"></a>
### Q15: How do you force a SwiftUI view to redraw without changing its state?

**Difficulty**: Intermediate

**Strategy**:
There are legitimate cases where you need to fully reset a view -- for example, restarting an animation or resetting a form -- and the `.id()` modifier is the idiomatic SwiftUI approach. By assigning a new identifier, SwiftUI treats the view as an entirely new instance and recreates it from scratch. Interviewers want you to understand that this is a heavy operation: the old view is destroyed and a new one allocated, so use it sparingly. Avoid this as a workaround for state management bugs; prefer isolating state to subviews first.

**Strategy:**
Change the `id` of the view. SwiftUI considers a view with a new ID as a completely new view.

**Code Example:**
```swift
struct ContentView: View {
    @State private var refreshID = UUID()
    
    var body: some View {
        VStack {
            ComplexView()
                .id(refreshID) // Force redraw
            
            Button("Refresh") {
                refreshID = UUID()
            }
        }
    }
}
```

---

<a id="q16"></a>
### Q16: How do you set up a basic Core Data Stack?

**Difficulty**: Intermediate

**Strategy**:
Core Data remains Apple's primary persistence framework for complex data models, and understanding its stack setup is essential even as SwiftData emerges. The `NSPersistentContainer` encapsulates the managed object model, persistent store coordinator, and managed object context into one convenient object. Interviewers expect you to know that `viewContext` runs on the main thread and should only be used for UI-bound operations, while background tasks should use `newBackgroundContext()`. A common pitfall is not handling the `loadPersistentStores` error gracefully in production.

**Strategy:**
Initialize an `NSPersistentContainer`. Load persistent stores. Provide a `viewContext` for the main thread.

**Code Example:**

```swift
import CoreData

class CoreDataStack {
    static let shared = CoreDataStack()
    
    lazy var persistentContainer: NSPersistentContainer = {
        let container = NSPersistentContainer(name: "Model")
        container.loadPersistentStores { _, error in
            if let error = error { fatalError("Failed to load: \(error)") }
        }
        return container
    }()
    
    var context: NSManagedObjectContext { persistentContainer.viewContext }
}
```

---

<a id="q17"></a>
### Q17: How do you use Combine to handle a text field input with debounce?

**Difficulty**: Intermediate

**Strategy**:
Debouncing search-as-you-type input is a classic real-world problem that tests whether you can chain Combine operators effectively. The core idea is to suppress rapid intermediate values and only act after the user pauses typing, preventing excessive API calls. The pipeline is: published property, dollar-sign publisher, debounce for a time interval, remove duplicates, then sink or assign. A key pitfall is forgetting to store the `AnyCancellable` -- if it is deallocated, the subscription is silently dropped and your pipeline stops working.

**Strategy:**
Use `@Published` property, listen to it with `$`, apply `debounce`, `removeDuplicates`, and `sink`.

**Code Example:**

```swift
class ViewModel: ObservableObject {
    @Published var text = ""
    private var cancellables = Set<AnyCancellable>()
    
    init() {
        $text
            .debounce(for: .seconds(0.5), scheduler: RunLoop.main)
            .removeDuplicates()
            .sink { print("Search: \($0)") }
            .store(in: &cancellables)
    }
}
```

---

<a id="q18"></a>
### Q18: How do you create programmatic Auto Layout constraints?

**Difficulty**: Intermediate

**Strategy**:
Even in the SwiftUI era, UIKit layout skills are expected in interviews for teams maintaining existing apps. The anchor-based API is the modern, readable approach compared to the older `NSLayoutConstraint(style:)` format. The non-negotiable rule is setting `translatesAutoresizingMaskIntoConstraints = false` before adding constraints -- forgetting this is the single most common layout bug. Always activate constraints using `NSLayoutConstraint.activate()` rather than setting `isActive` individually, as it is more performant and groups related constraints together.

**Strategy:**
Set `translatesAutoresizingMaskIntoConstraints = false`. Use `NSLayoutConstraint.activate` with anchors.

**Code Example:**

```swift
let view = UIView()
view.translatesAutoresizingMaskIntoConstraints = false
parentView.addSubview(view)

NSLayoutConstraint.activate([
    view.centerXAnchor.constraint(equalTo: parentView.centerXAnchor),
    view.centerYAnchor.constraint(equalTo: parentView.centerYAnchor),
    view.widthAnchor.constraint(equalToConstant: 100),
    view.heightAnchor.constraint(equalToConstant: 100)
])
```

---

<a id="q19"></a>
### Q19: How do you write a generic function that works with any Numeric type?

**Difficulty**: Beginner

**Strategy**:
Generics with protocol constraints are fundamental to writing reusable Swift code, and the `Numeric` protocol is the canonical example. Interviewers use this to check that you understand type constraints beyond bare `<T>`. The `Numeric` protocol provides `+`, `-`, and `*`, so any function constrained to it works with `Int`, `Double`, `Float`, and custom numeric types. Be aware that `Numeric` does not include division -- for that you need `FloatingPoint` or `BinaryInteger` as additional constraints.

**Strategy:**
Use a generic type parameter constrained to the `Numeric` protocol.

**Code Example:**

```swift
func square<T: Numeric>(_ value: T) -> T {
    return value * value
}

print(square(5))       // 25
print(square(5.5))     // 30.25
```

---

<a id="q20"></a>
### Q20: What is an escaping closure and when do you use it?

**Difficulty**: Intermediate

**Strategy**:
Understanding escaping vs non-escaping closures is essential for memory management and async programming in Swift. By default, closures are non-escaping -- the compiler guarantees they run before the function returns, so no retain cycle is possible. When a closure outlives the function (stored in a property, dispatched asynchronously, or passed to another async context), it must be marked `@escaping`, and you must be careful about capturing `self` to avoid retain cycles. The modern best practice is to use `[weak self]` in escaping closures and prefer async/await over callback patterns.

**Strategy:**
An `@escaping` closure is called *after* the function returns (e.g., async callbacks). Non-escaping is default.

**Code Example:**

```swift
func fetchData(completion: @escaping (String) -> Void) {
    DispatchQueue.global().async {
        completion("Data") // Called later
    }
}
```

---

<a id="q21"></a>
### Q21: How do Structs (Value Types) differ from Classes (Reference Types) in mutation?

**Difficulty**: Beginner

**Strategy**:
This builds on the struct vs class distinction by focusing specifically on mutation semantics, which catches many developers off guard. Because structs are copied on assignment, mutating a copy does not affect the original -- but Swift requires you to explicitly opt in to mutation with the `mutating` keyword. Classes need no such keyword because you are always working with a shared reference. Interviewers look for this knowledge because misunderstanding mutation semantics leads to subtle bugs where a function unexpectedly modifies shared state or, conversely, fails to propagate a change.

**Strategy:**
Struct methods mutating properties must be marked `mutating`. Classes don't need this as they are reference types.

**Code Example:**

```swift
struct Point {
    var x = 0
    mutating func moveBy(delta: Int) {
        x += delta
    }
}

class Mover {
    var x = 0
    func moveBy(delta: Int) { // No mutating needed
        x += delta
    }
}
```

---

<a id="q22"></a>
### Q22: How do you provide a default implementation for a Protocol method?

**Difficulty**: Intermediate

**Strategy**:
Default protocol implementations via extensions are the Swift alternative to optional protocol methods and are critical for designing flexible APIs. Interviewers ask this to verify you understand that protocol extensions provide behavior without requiring conformance, and that types can override the default. A key subtlety: if you call a method through a protocol existential (`any MyProtocol`), the extension version is called even if the concrete type provides its own -- only methods declared in the protocol itself use dynamic dispatch.

**Strategy:**

**Code Example:**

```swift
protocol Greeter {
    func greet()
}

extension Greeter {
    func greet() {
        print("Hello")
    }
}

struct Person: Greeter {}
Person().greet() // "Hello"
```

---

<a id="q23"></a>
### Q23: How do you add a computed property to an existing type using Extensions?

**Difficulty**: Beginner

**Strategy**:
Extensions are one of Swift's most practical features for organizing code and adding functionality to types you do not own -- including standard library types like `Double`, `String`, and `Int`. Interviewers expect you to know that extensions support computed properties but cannot add stored properties (except via associated objects on Objective-C compatible classes). This distinction matters because developers sometimes try to use extensions as a workaround for storing state, which the compiler will reject. Extensions are best used for grouping related functionality and improving code readability.

**Strategy:**
Extensions can add computed properties but not stored properties.

**Code Example:**

```swift
extension Double {
    var km: Double { return this * 1000.0 }
    var m: Double { return this }
}

let distance = 5.0.km
```

---

<a id="q24"></a>
### Q24: How do you define and throw a custom Error?

**Difficulty**: Beginner

**Strategy**:
Custom error types are the foundation of reliable error handling in Swift, and using enums is the idiomatic approach because they enforce exhaustive handling in `switch` statements. Interviewers want to see that you model errors as specific, meaningful cases with associated values (like status codes or messages) rather than using a generic string. Best practice: keep your error types narrow and domain-specific (e.g., `AuthError`, `DatabaseError`) rather than one monolithic error enum, and always document what a function can throw.

**Strategy:**
Conform an enum to `Error` protocol. Use `throw` keyword.

**Code Example:**

```swift
enum ValidationError: Error {
    case empty
}

func validate(_ text: String) throws {
    if text.isEmpty { throw ValidationError.empty }
}

do {
    try validate("")
} catch {
    print(error)
}
```

---

<a id="q25"></a>
### Q25: Why is Set lookup faster than Array lookup?

**Difficulty**: Intermediate

**Strategy**:
This question tests your understanding of data structure fundamentals and your ability to choose the right collection type for the task. Sets use hash-based lookup (O(1) average case), while Arrays require linear scanning (O(n)) for `contains`. The tradeoff is that Sets are unordered and require elements to be `Hashable`. In interviews, mention that choosing Array when you frequently check membership (e.g., filtering duplicates, checking allowed values) is a common performance mistake that scales poorly with data size.

**Strategy:**
Sets use hash tables (O(1) complexity), while Arrays require iterating through elements (O(n) complexity) to find a value.

**Code Example:**

```swift
let set: Set = [1, 2, 3]
let array = [1, 2, 3]

// O(1)
set.contains(2) 

// O(n)
array.contains(2)
```

---

<a id="q26"></a>
### Q26: How do you support Dynamic Type (text scaling) in SwiftUI?

**Difficulty**: Beginner

**Strategy**:
Accessibility is not optional in professional iOS development, and Dynamic Type is the most impactful accessibility feature you can support. Interviewers ask this because many apps break at large text sizes -- text gets clipped, layouts overflow, and images do not scale. The key is using semantic text styles (`.body`, `.headline`) instead of fixed font sizes, and `@ScaledMetric` for non-text sizes that should grow proportionally. Test your layouts at all Dynamic Type sizes, especially the accessibility ranges, and use `minimumScaleFactor` as a safety net.

**Strategy:**
Use standard fonts (`.body`, `.headline`) or `scaledMetric`. SwiftUI handles scaling automatically.

**Code Example:**

```swift
Text("Scalable Text")
    .font(.body) // Scales with system settings

@ScaledMetric var size: CGFloat = 20
Image(systemName: "star").frame(width: size, height: size)
```

---

<a id="q27"></a>
### Q27: How do you localize strings using NSLocalizedString?

**Difficulty**: Beginner

**Strategy**:
Localization is a standard requirement for apps distributed globally, and interviewers want to see that you know the fundamentals before reaching for higher-level tools. `NSLocalizedString` returns the localized version of a string from the appropriate `Localizable.strings` file based on the user's language preference. The `comment` parameter is not used at runtime but is extracted by tools like `genstrings` to help translators. In modern Swift projects, prefer the String Catalogs introduced in Xcode 15, but know `NSLocalizedString` for legacy codebases and interviews.

**Strategy:**
Use `NSLocalizedString` with a key and comment. Provide `Localizable.strings` files for languages.

**Code Example:**

```swift
let greeting = NSLocalizedString("hello_key", comment: "Greeting")

// Localizable.strings (en)
// "hello_key" = "Hello";

// Localizable.strings (es)
// "hello_key" = "Hola";
```

---

<a id="q28"></a>
### Q28: What is the role of SceneDelegate vs AppDelegate?

**Difficulty**: Intermediate

**Strategy**:
Understanding the delegate split introduced in iOS 13 is important for maintaining UIKit-based apps and explaining app architecture in interviews. Before iOS 13, AppDelegate handled everything; the split was made to support multi-window apps on iPad. AppDelegate now focuses on app-level concerns (launch setup, push notifications, Core Data stack), while SceneDelegate manages each window scene's lifecycle (connection, disconnection, foreground transitions). In SwiftUI apps using the `@main` App protocol, these delegates are largely abstracted away, but the knowledge still matters for UIKit interop and debugging.

**Strategy:**
AppDelegate handles app-level lifecycle (launch, termination). SceneDelegate (iOS 13+) handles UI lifecycle (foreground, background) for multi-window support.

**Code Example:**

```swift
// SceneDelegate.swift
func sceneDidBecomeActive(_ scene: UIScene) {
    // UI is active
}

// AppDelegate.swift
func application(_ app: UIApplication, didFinishLaunchingWithOptions...) {
    // App launched
}
```

---

<a id="q29"></a>
### Q29: How do you write an async unit test with XCTest?

**Difficulty**: Intermediate

**Strategy**:
Testing async code was historically clunky with XCTestExpectation, but Swift Concurrency made it straightforward with native `async` test methods. Interviewers want to see that you know you can simply mark a test function `async throws` and use `await` directly, letting XCTest manage the async context. A common mistake is calling `async` code without marking the test `async`, which causes a compiler error. For testing timeouts or cancellation, you still need expectations, but for most async testing the direct approach is cleaner and preferred.

**Strategy:**
Mark the test method as `async` and use `await`.

**Code Example:**

```swift
func testAsyncFetch() async throws {
    let data = try await service.fetch()
    XCTAssertNotNil(data)
}
```

---

<a id="q30"></a>
### Q30: How do you configure a basic Fastfile for Fastlane?

**Difficulty**: Intermediate

**Strategy**:
CI/CD automation is increasingly expected of iOS developers, and Fastlane remains the most widely adopted tool. A Fastfile defines lanes -- named sequences of actions -- that automate repetitive tasks like building, testing, screenshot generation, and TestFlight deployment. Interviewers want to see you can write a functional lane and understand concepts like lanes, actions, and environment variables. A best practice is to keep lanes focused and composable, and to store secrets in environment variables or the keychain rather than in the Fastfile itself.

**Strategy:**
Define lanes in `Fastfile` (Ruby) to automate tasks like testing and beta deployment.

**Code Example:**

```swift
default_platform(:ios)

platform :ios do
  lane :beta do
    build_app(scheme: "MyApp")
    upload_to_testflight
  end
  
  lane :tests do
    run_tests(scheme: "MyApp")
  end
end
```

---

<a id="q31"></a>
### Q31: How do you define dependencies in Swift Package Manager?

**Difficulty**: Beginner

**Strategy**:
Swift Package Manager is the standard dependency management tool for Swift, and understanding `Package.swift` configuration is a practical necessity. Dependencies are declared at the package level with a source URL and version constraint, then linked to specific targets. Interviewers expect you to understand versioning strategies: `upToNextMajor` for stability, `upToNextMinor` for stricter control, and `branch` or `revision` for development. A common pitfall is adding a package dependency but forgetting to also add it to the target's dependency list, resulting in "module not found" errors.

**Strategy:**
Edit `Package.swift` and add dependencies in the `dependencies` array.

**Code Example:**

```swift
dependencies: [
    .package(url: "https://github.com/Alamofire/Alamofire.git", .upToNextMajor(from: "5.0.0"))
],
targets: [
    .target(name: "MyApp", dependencies: ["Alamofire"])
]
```

---

<a id="q32"></a>
### Q32: How do you use `@MainActor` to ensure UI updates on the main thread?

**Difficulty**: Intermediate

**Strategy**:
Main thread safety is critical in iOS development because updating UI from a background thread causes undefined behavior, including crashes and visual glitches. `@MainActor` is Swift Concurrency's compiler-enforced solution -- it guarantees annotated code runs on the main thread without manual `DispatchQueue.main.async` calls. You can annotate entire classes, individual functions, or even specific properties. A pitfall: calling a `@MainActor` function from a non-isolated context requires `await`, which the compiler will enforce, but you must understand why the suspension point exists to avoid deadlocks.

**Strategy:**
Annotate a class, function, or property with `@MainActor`. The compiler enforces main thread execution.

**Code Example:**

```swift
@MainActor
class ViewModel: ObservableObject {
    @Published var data = ""
    
    func update() {
        data = "Updated" // Guaranteed main thread
    }
}
```

---

<a id="q33"></a>
### Q33: When should you use the `defer` keyword?

**Difficulty**: Beginner

**Strategy**:
`defer` ensures cleanup code runs regardless of how a scope exits -- whether by `return`, `throw`, or falling through -- making it invaluable for resource management. Common use cases include closing file handles, unlocking mutexes, and resetting temporary state. Interviewers look for understanding of the reverse-order execution (last `defer` runs first), which matters when multiple resources need teardown in the correct sequence. Avoid using `defer` for complex logic that makes control flow hard to follow; keep it focused on simple cleanup.

**Strategy:**
Use `defer` to execute code just before the current scope exits (cleanup, closing files/locks). Executed in reverse order of declaration.

**Code Example:**

```swift
func process() {
    print("Start")
    defer { print("Cleanup") }
    print("Work")
}
// Output: Start, Work, Cleanup
```

---

<a id="q34"></a>
### Q34: How do you use a `lazy` stored property?

**Difficulty**: Beginner

**Strategy**:
Lazy initialization defers expensive setup until first access, which improves app launch time and avoids unnecessary work for code paths that are never executed. Interviewers test this because it is a simple but effective optimization pattern. Key constraints: `lazy` only works with `var` (not `let`), it is not thread-safe by default (use a serial queue if multiple threads might trigger initialization), and it cannot be used with `let` constants or inside structs that need `Sendable` conformance. It is most useful for properties that depend on `self` or require heavy computation.

**Strategy:**
Mark a property as `lazy var`. It is initialized only when first accessed. Must be mutable (`var`).

**Code Example:**

```swift
class Manager {
    lazy var importer = Importer() // Expensive creation
}
```

---

<a id="q35"></a>
### Q35: What is the difference between Computed and Stored properties?

**Difficulty**: Beginner

**Strategy**:
This is a foundational Swift concept that affects how you design your data models. Stored properties allocate memory and hold a value; computed properties recalculate on every access and do not use persistent storage. Interviewers want you to know that computed properties can be read-only (no setter) or read-write, and that they are appropriate for derived values (area from width/height, full name from first/last). A common mistake is using computed properties for expensive calculations that are called frequently -- consider caching the result in a stored property instead.

**Strategy:**
Stored properties store a value in memory. Computed properties calculate a value every time they are accessed.

**Code Example:**

```swift
struct Rect {
    var width = 0.0 // Stored
    var height = 0.0
    
    var area: Double { // Computed
        return width * height
    }
}
```

---

<a id="q36"></a>
### Q36: What is the difference between `guard` and `if let`?

**Difficulty**: Beginner

**Strategy**:
Both `guard let` and `if let` safely unwrap optionals, but they serve different control flow purposes and interviewers want to see you use each correctly. `if let` creates a scoped binding within its block, while `guard let` binds the value for the remainder of the enclosing scope and forces an early exit on `nil`. In practice, prefer `guard` at the top of functions to validate preconditions -- it reduces nesting and makes the "happy path" more readable. `if let` is better when you want to handle the optional case inline without returning early.

**Strategy:**
`if let` unwrap optionals for a specific block. `guard let` unwrap optionals for the rest of the scope and requires an early exit (`return`, `throw`) if it fails.

**Code Example:**

```swift
func printName(_ name: String?) {
    guard let name = name else { return }
    print(name) // Available here
}
```

---

<a id="q37"></a>
### Q37: How do you handle custom date formats with Codable?

**Difficulty**: Intermediate

**Strategy**:
Date handling is a frequent source of decoding bugs because APIs use many different formats -- ISO 8601, unix timestamps, custom strings. Interviewers want to see that you know `JSONDecoder.dateDecodingStrategy` handles common cases (`.iso8601`, `.secondsSince1970`), and that you can configure a custom `DateFormatter` for non-standard formats. A best practice is to configure your decoder once and reuse it, rather than setting the strategy before every decode call. Also remember that `DateFormatter` is not thread-safe, so create new instances or use the decoder's built-in strategy options.

**Strategy:**
Set `dateDecodingStrategy` on `JSONDecoder`.

**Code Example:**

```swift
let decoder = JSONDecoder()
let formatter = DateFormatter()
formatter.dateFormat = "yyyy-MM-dd"
decoder.dateDecodingStrategy = .formatted(formatter)
```

---

<a id="q38"></a>
### Q38: How do you use the `Result` type?

**Difficulty**: Intermediate

**Strategy**:
The `Result` type brings type-safe error handling to completion-handler-based APIs, making success and failure explicit in the function signature. Interviewers ask this because it bridges the gap between throw-based synchronous code and callback-based asynchronous code. Key methods include `get()` (rethrows the failure), `map()` and `flatMap()` for chaining, and `switch` for exhaustive handling. In modern Swift, `async/await` makes `Result` less necessary for new code, but you will encounter it frequently when wrapping or migrating existing callback APIs.

**Strategy:**
`Result<Success, Failure>` is an enum representing success or failure. Useful for completion handlers.

**Code Example:**

```swift
func fetch(completion: (Result<String, Error>) -> Void) {
    if success { completion(.success("Data")) }
    else { completion(.failure(MyError.fail)) }
}
```

---

<a id="q39"></a>
### Q39: How do you use `map`, `filter`, and `reduce`?

**Difficulty**: Beginner

**Strategy**:
These three higher-order functions are the backbone of functional data transformation in Swift and appear in virtually every codebase. Interviewers want to confirm you can chain them fluently rather than writing imperative loops -- `map` transforms each element, `filter` selects matching elements, and `reduce` collapses a collection into a single value. A common pitfall is chaining too many operations in a single expression, which hurts readability; prefer breaking complex pipelines into named intermediate variables. Also know `compactMap` for filtering nils while transforming.

**Strategy:**
Functional methods for collections. `map` transforms, `filter` selects, `reduce` combines.

**Code Example:**

```swift
let nums = [1, 2, 3, 4]
let squaredEvens = nums.filter { $0 % 2 == 0 }.map { $0 * $0 }
let sum = nums.reduce(0, +)
```

---

<a id="q40"></a>
### Q40: How do you use KeyPaths in Swift?

**Difficulty**: Intermediate

**Strategy**:
KeyPaths are an underused but powerful feature that lets you reference properties as first-class values, enabling dynamic property access without stringly-typed APIs. They are most commonly seen in SwiftUI (`\.name` in `List`) but have broader uses: sorting by keypath, filtering by keypath, and type-safe dynamic member access. Interviewers want you to know the hierarchy: `KeyPath` (read-only), `WritableKeyPath` (read-write for vars), and `ReferenceWritableKeyPath` (read-write for class properties). They are particularly useful for building generic data-driven UIs and test helpers.

**Strategy:**
KeyPaths allow referring to a property without accessing it. Syntax: `\Type.property`.

**Code Example:**

```swift
struct User { var name: String }
let users = [User(name: "A"), User(name: "B")]
let names = users.map(\.name)
```

---

<a id="q41"></a>
### Q41: How do you implement the Singleton pattern correctly?

**Difficulty**: Beginner

**Strategy**:
The Singleton pattern ensures a class has exactly one instance, commonly used for managers like `UserDefaults.standard`, `FileManager.default`, or a shared service coordinator. The Swift-idiomatic implementation uses `static let shared` (thread-safe via `dispatch_once` under the hood) and `private init()` to prevent external instantiation. Interviewers also want you to acknowledge the downsides: singletons create hidden global state, make testing harder, and can lead to tight coupling. Prefer dependency injection when possible, and reserve singletons for truly shared, stateless, or system-level resources.

**Strategy:**
Use a `static let shared` property and a `private init()` to prevent external instantiation.

**Code Example:**

```swift
class Settings {
    static let shared = Settings()
    private init() {}
}
```

---

<a id="q42"></a>
### Q42: How do you use `DispatchGroup` to wait for multiple async tasks?

**Difficulty**: Intermediate

**Strategy**:
DispatchGroup coordinates multiple concurrent operations and notifies you when all have completed -- essential for parallel data loading. The pattern requires careful bookkeeping: call `enter()` before each task, `leave()` when it finishes, and `notify()` for the callback when the count reaches zero. The most common bug is an unmatched `enter()`/`leave()` pair, which causes the notify to never fire or fire prematurely. In modern Swift, consider using `async let` or task groups instead, but know DispatchGroup for pre-concurrency codebases and GCD-based APIs.

**Strategy:**
Use `enter()`, `leave()`, and `notify()`. `notify` block runs when enter/leave counts balance.

**Code Example:**

```swift
let group = DispatchGroup()

group.enter()
asyncTask1 { group.leave() }

group.enter()
asyncTask2 { group.leave() }

group.notify(queue: .main) {
    print("All done")
}
```

---

<a id="q43"></a>
### Q43: How do you use `OperationQueue` for dependent tasks?

**Difficulty**: Advanced

**Strategy**:
`OperationQueue` provides a higher-level abstraction than GCD for managing complex task graphs with dependencies, cancellation, and priority. Interviewers ask this to see if you can model multi-step workflows (download, parse, cache) where each step depends on the previous one. Use `addDependency()` to declare ordering, and the queue handles the rest, including maximum concurrent operation limits. A key advantage over GCD is that operations can be cancelled and their state observed. For modern Swift, structured concurrency with `async/await` and task groups covers most use cases, but `OperationQueue` remains relevant for complex pipelines.

**Strategy:**
Create `Operation` objects and use `addDependency`.

**Code Example:**

```swift
let queue = OperationQueue()
let op1 = BlockOperation { print("1") }
let op2 = BlockOperation { print("2") }

op2.addDependency(op1) // op1 runs first
queue.addOperations([op1, op2], waitUntilFinished: false)
```

---

<a id="q44"></a>
### Q44: How do you configure `URLSession` caching?

**Difficulty**: Intermediate

**Strategy**:
HTTP caching is an often-overlooked optimization that can dramatically reduce network traffic and improve app responsiveness. By configuring `URLCache` with appropriate memory and disk capacities on your `URLSessionConfiguration`, the system automatically caches responses and serves subsequent requests from cache when available. Interviewers want to see you understand cache policies like `.returnCacheDataElseLoad` and can size the cache appropriately for your app's data patterns. A common mistake is leaving the default cache configuration untouched, which may result in unnecessarily small cache limits or responses not being cached at all.

**Strategy:**
Use `URLCache` and configure `URLSessionConfiguration`.

**Code Example:**

```swift
let config = URLSessionConfiguration.default
config.requestCachePolicy = .returnCacheDataElseLoad
config.urlCache = URLCache(memoryCapacity: 50*1024*1024, diskCapacity: 0)
let session = URLSession(configuration: config)
```

---

<a id="q45"></a>
### Q45: How do you implement the Factory Pattern?

**Difficulty**: Intermediate

**Strategy**:
The Factory Pattern decouples object creation from usage, which is essential when the concrete type should be determined at runtime (e.g., A/B testing different UI components, cross-platform abstraction). Interviewers look for clean protocol-based design where the factory returns the abstract type, keeping callers unaware of specific implementations. This pattern shines in testability because you can swap the factory to return mock objects. Avoid over-engineering with factories when direct initialization suffices -- use it when there is a genuine need for flexibility or when creation logic is complex.

**Strategy:**
Use a factory class/method to create objects without exposing instantiation logic.

**Code Example:**

```swift
protocol Button { func render() }
class IOSButton: Button { func render() {} }
class AndroidButton: Button { func render() {} }

class ButtonFactory {
    static func create(type: String) -> Button {
        return type == "iOS" ? IOSButton() : AndroidButton()
    }
}
```

---

<a id="q46"></a>
### Q46: How do you implement the Observer Pattern using NotificationCenter?

**Difficulty**: Intermediate

**Strategy**:
NotificationCenter is Cocoa's built-in broadcast mechanism for loosely coupled communication between unrelated components. It is ideal for app-wide events (user logged out, data refreshed, theme changed) where the sender does not need to know who is listening. Interviewers want you to understand the trade-off: NotificationCenter is flexible but makes data flow harder to trace compared to delegates or closures. A best practice is to use custom `Notification.Name` constants and pass typed data via the `userInfo` dictionary. Avoid replacing all delegation with notifications -- use them only when you truly need one-to-many communication.

**Strategy:**
Post notifications and add observers. Remember to remove observers (though simpler in iOS 9+).

**Code Example:**

```swift
NotificationCenter.default.post(name: .myNotif, object: nil)

NotificationCenter.default.addObserver(forName: .myNotif, object: nil, queue: .main) { _ in
    print("Received")
}
```

---

<a id="q47"></a>
### Q47: How do you use the Coordinator Pattern for navigation?

**Difficulty**: Advanced

**Strategy**:
The Coordinator Pattern solves one of the biggest problems in UIKit apps: view controllers directly creating and pushing other view controllers, creating tight coupling and making navigation logic impossible to test. Coordinators own the navigation controller and manage the flow between screens, while view controllers remain focused on presentation. Interviewers value this pattern because it demonstrates you can architect a scalable, testable app. In SwiftUI, the need for coordinators is reduced thanks to `NavigationStack` and programmatic navigation, but the principle of separating navigation logic from view logic still applies.

**Strategy:**
Delegate navigation responsibility to a Coordinator object instead of ViewControllers pushing others directly.

**Code Example:**

```swift
protocol Coordinator {
    var nav: UINavigationController { get }
    func start()
}

class MainCoordinator: Coordinator {
    var nav: UINavigationController
    init(nav: UINavigationController) { self.nav = nav }
    
    func start() {
        let vc = ViewController()
        vc.coordinator = self
        nav.pushViewController(vc, animated: false)
    }
}
```

---

<a id="q48"></a>
### Q48: How do you optimize memory using `autoreleasepool`?

**Difficulty**: Advanced

**Strategy**:
Memory spikes during tight loops that create many temporary objects (images, strings, parsed data) are a real performance concern in data-heavy iOS apps. `autoreleasepool` forces ARC to release objects at the end of the block rather than waiting for the current run loop iteration, keeping memory usage bounded. Interviewers ask this to verify you understand how ARC interacts with run loops and when manual intervention is needed. The most common use case is image processing or data parsing loops -- without autorelease pools, memory can spike to hundreds of megabytes before the system reclaims it.

**Strategy:**
Use `autoreleasepool` inside loops creating many temporary objects to free memory immediately.

**Code Example:**

```swift
for _ in 0..<10000 {
    autoreleasepool {
        let image = UIImage(named: "large")
        // Process image
    } // image released here
}
```

---

<a id="q49"></a>
### Q49: How do you check for API availability?

**Difficulty**: Beginner

**Strategy**:
Maintaining backward compatibility while adopting new APIs is a daily reality for iOS developers supporting multiple OS versions. The `#available` check lets you guard new API usage at runtime, and the compiler enforces that you handle older versions. Interviewers want to see you understand both the runtime check (`if #available`) and the declaration annotation (`@available`) for marking your own APIs. A best practice is to extract version-specific code into small, well-named helper methods rather than scattering `#available` checks throughout your codebase. Also know that Swift's availability checking applies to macOS, watchOS, and tvOS in addition to iOS.

**Strategy:**

**Code Example:**

```swift
if #available(iOS 15, *) {
    // Use iOS 15 APIs
} else {
    // Fallback
}
```

---

<a id="q50"></a>
### Q50: How do you prevent a retain cycle in a Delegate?

**Difficulty**: Beginner

**Strategy**:
Retain cycles are the most common cause of memory leaks in Swift, and the delegate pattern is the classic culprit -- a class holds a strong reference to its delegate, which may also hold a strong reference back. The fix is simple but interviewers want you to explain the reasoning: delegates should always be `weak` (or `unowned` when non-optional) to break the cycle. Note that protocols must be constrained to `AnyObject` (class-only) to allow `weak` references, since value types do not participate in reference counting. Always verify your delegate relationships are unidirectional in ownership to prevent subtle memory leaks in production.

**Strategy:**
Mark the delegate property as `weak`.

**Code Example:**

```swift
protocol MyDelegate: AnyObject {
    func didSomething()
}

class MyClass {
    weak var delegate: MyDelegate?
}
```
