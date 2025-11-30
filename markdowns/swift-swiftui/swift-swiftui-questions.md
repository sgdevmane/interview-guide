# Swift & SwiftUI Interview Questions

## Table of Contents

1. [What is the difference between `class` and `struct` in Swift?](#q1-what-is-the-difference-between-class-and-struct-in-swift) <span class="beginner">Beginner</span>
2. [How do you implement a thread-safe counter using Swift Actors?](#q2-how-do-you-implement-a-thread-safe-counter-using-swift-actors) <span class="advanced">Advanced</span>
3. [How do you efficiently handle large lists of data in SwiftUI to avoid performance issues?](#q3-how-do-you-efficiently-handle-large-lists-of-data-in-swiftui-to-avoid-performance-issues) <span class="intermediate">Intermediate</span>
4. [How do you migrate legacy callback-based code to Swift Concurrency (async/await)?](#q4-how-do-you-migrate-legacy-callback-based-code-to-swift-concurrency-asyncawait) <span class="advanced">Advanced</span>
5. [How do you inject dependencies into a SwiftUI view hierarchy without passing them through every initializer?](#q5-how-do-you-inject-dependencies-into-a-swiftui-view-hierarchy-without-passing-them-through-every-initializer) <span class="intermediate">Intermediate</span>
6. [How do you implement custom error handling in a Swift network layer?](#q6-how-do-you-implement-custom-error-handling-in-a-swift-network-layer) <span class="intermediate">Intermediate</span>
7. [How do you optimize the performance of a SwiftUI view that updates too frequently?](#q7-how-do-you-optimize-the-performance-of-a-swiftui-view-that-updates-too-frequently) <span class="advanced">Advanced</span>
8. [How do you integrate a UIKit view (e.g., MKMapView) into a SwiftUI app?](#q8-how-do-you-integrate-a-uikit-view-eg-mkmapview-into-a-swiftui-app) <span class="intermediate">Intermediate</span>
9. [How do you implement Unit Tests for a ViewModel with async network calls?](#q9-how-do-you-implement-unit-tests-for-a-viewmodel-with-async-network-calls) <span class="advanced">Advanced</span>
10. [How do you handle deep linking in a SwiftUI application using the new NavigationStack?](#q10-how-do-you-handle-deep-linking-in-a-swiftui-application-using-the-new-navigationstack) <span class="advanced">Advanced</span>
11. [How do you manage the lifecycle of an `@ObservedObject` vs `@StateObject`?](#q11-how-do-you-manage-the-lifecycle-of-an-observedobject-vs-stateobject) <span class="beginner">Beginner</span>
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
32. [How do you use `@MainActor` to ensure UI updates on the main thread?](#q32-how-do-you-use-mainactor-to-ensure-ui-updates-on-the-main-thread) <span class="intermediate">Intermediate</span>
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
50. [How do you prevent a retain cycle in a Delegate?](#q50-how-do-you-prevent-a-retain-cycle-in-a-delegate) <span class="beginner">Beginner</span>

---

### Q1: What is the difference between `class` and `struct` in Swift?

**Difficulty**: Beginner

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

### Q2: How do you implement a thread-safe counter using Swift Actors?

**Difficulty**: Advanced

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

### Q3: How do you efficiently handle large lists of data in SwiftUI to avoid performance issues?

**Difficulty**: Intermediate

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

### Q4: How do you migrate legacy callback-based code to Swift Concurrency (async/await)?

**Difficulty**: Advanced

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

### Q5: How do you inject dependencies into a SwiftUI view hierarchy without passing them through every initializer?

**Difficulty**: Intermediate

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

### Q6: How do you implement custom error handling in a Swift network layer?

**Difficulty**: Intermediate

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

### Q7: How do you optimize the performance of a SwiftUI view that updates too frequently?

**Difficulty**: Advanced

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

### Q8: How do you integrate a UIKit view (e.g., MKMapView) into a SwiftUI app?

**Difficulty**: Intermediate

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

### Q9: How do you implement Unit Tests for a ViewModel with async network calls?

**Difficulty**: Advanced

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

### Q10: How do you handle deep linking in a SwiftUI application using the new NavigationStack?

**Difficulty**: Advanced

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

### Q11: How do you manage the lifecycle of an `@ObservedObject` vs `@StateObject`?

**Difficulty**: Beginner

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

### Q12: How do you implement custom property wrappers to validate user input automatically?

**Difficulty**: Advanced

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

### Q13: How do you use the `some` and `any` keywords in Swift generics?

**Difficulty**: Advanced

**Concepts:**
*   `some Protocol` (Opaque Type): Returns a specific concrete type that conforms to the protocol, but the identity is hidden. Performance is better (static dispatch).
*   `any Protocol` (Existential Type): A box that can hold *any* type conforming to the protocol. More flexible but has runtime overhead (dynamic dispatch).

**Code Example:**
```swift
func makeView() -> some View { Text("Hello") } // Opaque
func process(items: [any Equatable]) { ... }   // Existential
```

---

### Q14: How do you implement Codable for a JSON response with dynamic keys?

**Difficulty**: Expert

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

### Q15: How do you force a SwiftUI view to redraw without changing its state?

**Difficulty**: Intermediate

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

### Q16: How do you set up a basic Core Data Stack?

**Difficulty**: Intermediate

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

### Q17: How do you use Combine to handle a text field input with debounce?

**Difficulty**: Intermediate

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

### Q18: How do you create programmatic Auto Layout constraints?

**Difficulty**: Intermediate

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

### Q19: How do you write a generic function that works with any Numeric type?

**Difficulty**: Beginner

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

### Q20: What is an escaping closure and when do you use it?

**Difficulty**: Intermediate

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

### Q21: How do Structs (Value Types) differ from Classes (Reference Types) in mutation?

**Difficulty**: Beginner

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

### Q22: How do you provide a default implementation for a Protocol method?

**Difficulty**: Intermediate

**Strategy:**
Use a Protocol Extension.

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

### Q23: How do you add a computed property to an existing type using Extensions?

**Difficulty**: Beginner

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

### Q24: How do you define and throw a custom Error?

**Difficulty**: Beginner

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

### Q25: Why is Set lookup faster than Array lookup?

**Difficulty**: Intermediate

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

### Q26: How do you support Dynamic Type (text scaling) in SwiftUI?

**Difficulty**: Beginner

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

### Q27: How do you localize strings using NSLocalizedString?

**Difficulty**: Beginner

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

### Q28: What is the role of SceneDelegate vs AppDelegate?

**Difficulty**: Intermediate

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

### Q29: How do you write an async unit test with XCTest?

**Difficulty**: Intermediate

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

### Q30: How do you configure a basic Fastfile for Fastlane?

**Difficulty**: Intermediate

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

### Q31: How do you define dependencies in Swift Package Manager?

**Difficulty**: Beginner

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

### Q32: How do you use `@MainActor` to ensure UI updates on the main thread?

**Difficulty**: Intermediate

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

### Q33: When should you use the `defer` keyword?

**Difficulty**: Beginner

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

### Q34: How do you use a `lazy` stored property?

**Difficulty**: Beginner

**Strategy:**
Mark a property as `lazy var`. It is initialized only when first accessed. Must be mutable (`var`).

**Code Example:**

```swift
class Manager {
    lazy var importer = Importer() // Expensive creation
}
```

---

### Q35: What is the difference between Computed and Stored properties?

**Difficulty**: Beginner

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

### Q36: What is the difference between `guard` and `if let`?

**Difficulty**: Beginner

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

### Q37: How do you handle custom date formats with Codable?

**Difficulty**: Intermediate

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

### Q38: How do you use the `Result` type?

**Difficulty**: Intermediate

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

### Q39: How do you use `map`, `filter`, and `reduce`?

**Difficulty**: Beginner

**Strategy:**
Functional methods for collections. `map` transforms, `filter` selects, `reduce` combines.

**Code Example:**

```swift
let nums = [1, 2, 3, 4]
let squaredEvens = nums.filter { $0 % 2 == 0 }.map { $0 * $0 }
let sum = nums.reduce(0, +)
```

---

### Q40: How do you use KeyPaths in Swift?

**Difficulty**: Intermediate

**Strategy:**
KeyPaths allow referring to a property without accessing it. Syntax: `\Type.property`.

**Code Example:**

```swift
struct User { var name: String }
let users = [User(name: "A"), User(name: "B")]
let names = users.map(\.name)
```

---

### Q41: How do you implement the Singleton pattern correctly?

**Difficulty**: Beginner

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

### Q42: How do you use `DispatchGroup` to wait for multiple async tasks?

**Difficulty**: Intermediate

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

### Q43: How do you use `OperationQueue` for dependent tasks?

**Difficulty**: Advanced

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

### Q44: How do you configure `URLSession` caching?

**Difficulty**: Intermediate

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

### Q45: How do you implement the Factory Pattern?

**Difficulty**: Intermediate

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

### Q46: How do you implement the Observer Pattern using NotificationCenter?

**Difficulty**: Intermediate

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

### Q47: How do you use the Coordinator Pattern for navigation?

**Difficulty**: Advanced

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

### Q48: How do you optimize memory using `autoreleasepool`?

**Difficulty**: Advanced

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

### Q49: How do you check for API availability?

**Difficulty**: Beginner

**Strategy:**
Use `#available` check.

**Code Example:**

```swift
if #available(iOS 15, *) {
    // Use iOS 15 APIs
} else {
    // Fallback
}
```

---

### Q50: How do you prevent a retain cycle in a Delegate?

**Difficulty**: Beginner

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

---

