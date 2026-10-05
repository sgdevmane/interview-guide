<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Swift & SwiftUI (iOS) Logo" width="100" height="100">
  </a>
  <h1>Swift & SwiftUI (iOS) Interview Questions & Answers</h1>
  <p><b>Comprehensive interview questions covering Swift Concurrency, SwiftUI, ARC, SwiftData, and Architecture</b></p>
</div>

---

## Table of Contents

1. [How does Swift Concurrency (async/await, Actors, Sendable, MainActor) work?](#q1) <span class="advanced">Advanced</span>
2. [How does SwiftUI View Rendering and State Management (`@State`, `@Binding`, `@StateObject`, `@ObservedObject`, `@EnvironmentObject`, `@Observable` in iOS 17) work?](#q2) <span class="intermediate">Intermediate</span>
3. [How does Automatic Reference Counting (ARC) work in Swift and how do you resolve Strong Reference Cycles with `weak` and `unowned`?](#q3) <span class="intermediate">Intermediate</span>
4. [What does Swift 6 strict concurrency actually enforce, and how do you migrate a data-racing app?](#q4) <span class="advanced">Advanced</span>
5. [How does `Sendable` work, and when do you use `@unchecked Sendable`?](#q5) <span class="advanced">Advanced</span>
6. [What is `@preconcurrency` and when is it the right tool?](#q6) <span class="advanced">Advanced</span>
7. [How do task groups work and when do you choose them over `async let`?](#q7) <span class="intermediate">Intermediate</span>
8. [How does task cancellation work in Swift Concurrency, and how do you make your code cancellable correctly?](#q8) <span class="advanced">Advanced</span>
9. [What is the difference between `Task {}`, `Task.detached`, and structured child tasks?](#q9) <span class="intermediate">Intermediate</span>
10. [Explain actor reentrancy — why can an actor "interleave" and how do you defend against it?](#q10) <span class="expert">Expert</span>
11. [What are global actors and how does actor hopping affect performance?](#q11) <span class="advanced">Advanced</span>
12. [How does the `@Observable` macro work under the hood?](#q12) <span class="expert">Expert</span>
13. [What does `withObservationTracking` do and when would you use it directly?](#q13) <span class="advanced">Advanced</span>
14. [How does SwiftUI use identity to diff views, and what's the difference between structural and explicit identity?](#q14) <span class="advanced">Advanced</span>
15. [Why is `AnyView` expensive and what should you use instead?](#q15) <span class="advanced">Advanced</span>
16. [How does the `Layout` protocol work, and when do you write a custom layout?](#q16) <span class="expert">Expert</span>
17. [What are alignment guides and how do you use them for cross-view alignment?](#q17) <span class="advanced">Advanced</span>
18. [How do `NavigationStack` and `navigationDestination` replace `NavigationView`, and how do you manage programmatic navigation?](#q18) <span class="intermediate">Intermediate</span>
19. [How does `NavigationSplitView` work and how do you keep selections in sync across columns?](#q19) <span class="intermediate">Intermediate</span>
20. [How do you implement deep links that restore full navigation state in a SwiftUI app?](#q20) <span class="advanced">Advanced</span>
21. [How do you choose between `@State`, `@Binding`, `@Bindable`, `@StateObject`, and `@Environment` for state ownership?](#q21) <span class="intermediate">Intermediate</span>
22. [How does `@Environment` work and how do you define custom environment values with the `@Entry` macro (iOS 18)?](#q22) <span class="intermediate">Intermediate</span>
23. [How does SwiftUI view invalidation work, and how do you debug excessive re-renders?](#q23) <span class="advanced">Advanced</span>
24. [When does `drawingGroup()` help performance, and when does it hurt?](#q24) <span class="advanced">Advanced</span>
25. [How do `LazyVStack`/`LazyHStack` and `List` differ from regular stacks, and what pitfalls come with laziness?](#q25) <span class="beginner">Beginner</span>
26. [How do you profile SwiftUI performance with Instruments' SwiftUI template?](#q26) <span class="advanced">Advanced</span>
27. [How do you model data and relationships in SwiftData?](#q27) <span class="intermediate">Intermediate</span>
28. [How do schema migrations work in SwiftData, and how do they compare to Core Data migrations?](#q28) <span class="expert">Expert</span>
29. [SwiftData vs Core Data in 2025 — which do you pick for a new app?](#q29) <span class="intermediate">Intermediate</span>
30. [Combine vs AsyncStream — how do you bridge event streams into async/await, and when is each the right tool?](#q30) <span class="advanced">Advanced</span>
31. [How do retain cycles manifest in SwiftUI, and where do you actually need `[weak self]`?](#q31) <span class="intermediate">Intermediate</span>
32. [What are typed throws in Swift 6, and when do they improve API design?](#q32) <span class="advanced">Advanced</span>
33. [What is `Result` and when should you use it over throwing functions?](#q33) <span class="beginner">Beginner</span>
34. [What is the difference between `some` and `any`, and what changed with implicit `any`?](#q34) <span class="intermediate">Intermediate</span>
35. [What are primary associated types, and how do they enable `some Sequence<Int>`-style constraints?](#q35) <span class="advanced">Advanced</span>
36. [How do property wrappers work internally, and how do you write a correct one?](#q36) <span class="expert">Expert</span>
37. [Explain value semantics and copy-on-write — how would you implement COW in your own type?](#q37) <span class="intermediate">Intermediate</span>
38. [Compare MVVM, TCA, and VIPER for SwiftUI apps — when would you choose each?](#q38) <span class="advanced">Advanced</span>
39. [How do you do dependency injection in SwiftUI without singletons?](#q39) <span class="intermediate">Intermediate</span>
40. [How does Swift Testing compare to XCTest, and how do you migrate?](#q40) <span class="intermediate">Intermediate</span>
41. [How do you write reliable async tests, including mocking actor dependencies?](#q41) <span class="advanced">Advanced</span>
42. [Why does using `DispatchSemaphore.wait()` inside an `async` context deadlock, and what replaces it?](#q42) <span class="expert">Expert</span>
43. [What is priority inversion in the context of Swift Concurrency and GCD, and how does the runtime mitigate it?](#q43) <span class="advanced">Advanced</span>
44. [How do you build a retrying URLSession client with async/await?](#q44) <span class="intermediate">Intermediate</span>
45. [How does Core Data concurrency work, and what are the rules for `viewContext`, background contexts, and sharing objects?](#q45) <span class="advanced">Advanced</span>
46. [How do you schedule background work with BGTaskScheduler, including the iOS 18 push-to-start model?](#q46) <span class="intermediate">Intermediate</span>
47. [How do you use `ScenePhase` to manage app lifecycle in SwiftUI?](#q47) <span class="beginner">Beginner</span>
48. [How does a WidgetKit widget deliver UI, and how do you keep its timeline fresh?](#q48) <span class="intermediate">Intermediate</span>
49. [How do App Intents work, and how have they absorbed Siri, Shortcuts, and Apple Intelligence surfaces?](#q49) <span class="advanced">Advanced</span>
50. [How do you make a SwiftUI view accessible for VoiceOver users?](#q50) <span class="beginner">Beginner</span>
51. [How does Dynamic Type work, and how do you build layouts that scale with the user's text size?](#q51) <span class="beginner">Beginner</span>
52. [How does `matchedGeometryEffect` work and what are its failure modes?](#q52) <span class="intermediate">Intermediate</span>
53. [When do you reach for `keyframeAnimator` or `phaseAnimator` instead of `withAnimation`?](#q53) <span class="advanced">Advanced</span>
54. [How do you wrap a UIKit view with `UIViewRepresentable` correctly, including updates and sizing?](#q54) <span class="intermediate">Intermediate</span>
55. [How do you embed SwiftUI inside a UIKit app with `UIHostingController`?](#q55) <span class="intermediate">Intermediate</span>
56. [How does Swift interoperate with the Objective-C runtime, and what should you know about swizzling and dynamic dispatch?](#q56) <span class="expert">Expert</span>
57. [GCD vs actors — what do you give up and gain when moving serial queues to actors?](#q57) <span class="advanced">Advanced</span>
58. [How do you use Instruments' Leaks and Time Profiler to diagnose memory and CPU issues?](#q58) <span class="intermediate">Intermediate</span>
59. [How do MetricKit and os_signpost fit into a production diagnostics pipeline?](#q59) <span class="advanced">Advanced</span>
60. [How do you use RegexBuilder and regex literals for robust parsing in Swift 6?](#q60) <span class="intermediate">Intermediate</span>
61. [What makes Swift enums powerful — associated values, pattern matching, and when do you need `indirect`?](#q61) <span class="beginner">Beginner</span>
62. [How are optionals implemented internally, and what are the performance implications?](#q62) <span class="advanced">Advanced</span>
63. [What is protocol-oriented programming, and where does it beat class-based design in Swift?](#q63) <span class="intermediate">Intermediate</span>
64. [What do ABI stability and app thinning actually change for shipping Swift apps?](#q64) <span class="advanced">Advanced</span>
65. [How does StoreKit 2 work, and how do you test in-app purchases without App Store Connect?](#q65) <span class="advanced">Advanced</span>
66. [What window and immersive-space styles does visionOS offer, and how do you choose?](#q66) <span class="advanced">Advanced</span>
67. [How do you set up CI/CD for an iOS app with Xcode Cloud, fastlane, and test plans?](#q67) <span class="intermediate">Intermediate</span>
68. [struct vs class in Swift — how do you decide, and what does "value semantics" buy you in SwiftUI?](#q68) <span class="beginner">Beginner</span>
69. [How do Swift macros work, and how would you write a custom one?](#q69) <span class="advanced">Advanced</span>
70. [What are region-based isolation and `sending` parameters in Swift 6?](#q70) <span class="expert">Expert</span>
71. [What is "approachable concurrency" and the Swift 6.2 default isolation mode?](#q71) <span class="advanced">Advanced</span>
72. [Where does `@MainActor` apply automatically in SwiftUI, and how does a `.task` modifier's actor context work?](#q72) <span class="intermediate">Intermediate</span>
73. [How does `AttributedString` work, and when is it better than `Text` concatenation?](#q73) <span class="beginner">Beginner</span>
74. [When do you use `Grid` instead of `LazyVGrid`, and how do their layout rules differ?](#q74) <span class="intermediate">Intermediate</span>
75. [How do you react to scroll position and geometry in SwiftUI post-iOS 18?](#q75) <span class="advanced">Advanced</span>
76. [How do `#Preview` and `@Previewable` change the SwiftUI preview workflow?](#q76) <span class="intermediate">Intermediate</span>
77. [How do you implement a custom `AsyncSequence`, and what correctness rules apply?](#q77) <span class="advanced">Advanced</span>
78. [How do you build data visualizations with Swift Charts, and how do you make them interactive?](#q78) <span class="intermediate">Intermediate</span>
79. [What are Codable's advanced patterns — custom decoding, key strategies, and heterogeneous payloads?](#q79) <span class="intermediate">Intermediate</span>
80. [How do you implement push notifications end to end in a modern SwiftUI app?](#q80) <span class="intermediate">Intermediate</span>
81. [How do you store secrets and tokens securely — UserDefaults vs Keychain vs file-encrypted storage?](#q81) <span class="intermediate">Intermediate</span>
82. [How do DeviceCheck and App Attest protect your backend from compromised clients?](#q82) <span class="advanced">Advanced</span>
83. [How do you monitor network reachability with NWPathMonitor?](#q83) <span class="beginner">Beginner</span>
84. [When is `autoreleasepool` still needed in Swift?](#q84) <span class="intermediate">Intermediate</span>
85. [How do you catch data races in CI with ThreadSanitizer and Swift 6 diagnostics?](#q85) <span class="advanced">Advanced</span>
86. [How do `@AppStorage` and `UserDefaults` work, and what are their limits?](#q86) <span class="beginner">Beginner</span>
87. [How do you modularize an iOS app with Swift Package Manager, and how does it improve build times and boundaries?](#q87) <span class="intermediate">Intermediate</span>
88. [How do you surface feature tips with TipKit?](#q88) <span class="intermediate">Intermediate</span>
89. [How do you integrate maps in SwiftUI with the modern MapKit API?](#q89) <span class="intermediate">Intermediate</span>
90. [What lock primitives does Swift offer now — `NSLock`, `OSAllocatedUnfairLock`, and the `Mutex` from the Synchronization module?](#q90) <span class="advanced">Advanced</span>
91. [How does Swift Concurrency work under the hood — jobs, executors, and the cooperative pool?](#q91) <span class="expert">Expert</span>
92. [How do `layoutPriority` and fixed vs flexible frames change view sizing in SwiftUI?](#q92) <span class="beginner">Beginner</span>
93. [How do you use `@Query` in SwiftData to drive SwiftUI views?](#q93) <span class="intermediate">Intermediate</span>
94. [What does enabling CloudKit sync on SwiftData entail, and what are the schema constraints?](#q94) <span class="advanced">Advanced</span>
95. [How do App Clips work, and when are they worth the investment?](#q95) <span class="intermediate">Intermediate</span>
96. [What's the difference between `withAnimation`, the `.animation` modifier, and `Transaction`?](#q96) <span class="beginner">Beginner</span>
97. [How does the iOS 18 TabView tab API change tab-based UIs?](#q97) <span class="intermediate">Intermediate</span>
98. [How do String Catalogs modernize localization in Xcode?](#q98) <span class="beginner">Beginner</span>
99. [How should you use os Logger and unified logging so logs are useful in production?](#q99) <span class="beginner">Beginner</span>
100. [Design an offline-first iOS architecture — how do the pieces (local store, sync engine, conflict resolution, UI state) fit together?](#q100) <span class="expert">Expert</span>

---

<a id="q1"></a>
### Q1: How does Swift Concurrency (async/await, Actors, Sendable, MainActor) work?

**Difficulty**: Advanced

**Strategy**:
Swift 5.5+ Concurrency replaces GCD callbacks with structured concurrency:
- `async/await`: Non-blocking cooperative multitasking.
- `actor`: Reference type providing automatic data isolation ensuring only one thread accesses mutable state at a time (preventing data races).
- `@MainActor`: Directs execution to the main UI thread for SwiftUI state updates.
- `Sendable`: Marker protocol indicating types whose values are safe to transfer across concurrency boundaries.

**Code Example**:
```swift
import SwiftUI

actor BankAccount {
    private var balance: Double = 0
    func deposit(amount: Double) { balance += amount }
    func getBalance() -> Double { balance }
}

@MainActor
class ProfileViewModel: ObservableObject {
    @Published var userName: String = ""
    
    func loadProfile() async {
        let name = await fetchRemoteUser()
        self.userName = name // Safely updated on MainActor
    }
    private func fetchRemoteUser() async -> String { "Alice" }
}
```

---

<a id="q2"></a>
### Q2: How does SwiftUI View Rendering and State Management (`@State`, `@Binding`, `@StateObject`, `@ObservedObject`, `@EnvironmentObject`, `@Observable` in iOS 17) work?

**Difficulty**: Intermediate

**Strategy**:
- `@State`: Value type state owned and managed by the local View struct.
- `@Binding`: Two-way reference passing state from parent to child.
- `@StateObject`: Instantiates and owns a reference-type `ObservableObject` across view re-renders.
- `@ObservedObject`: Non-owning reference to an existing `ObservableObject`.
- `@Observable` (iOS 17 Macro): Replaces `ObservableObject` with fine-grained per-property dependency tracking without `@Published`.

**Code Example**:
```swift
import SwiftUI
import Observation

@Observable
class UserSettings {
    var theme: String = "dark"
    var notificationsEnabled: Bool = true
}

struct SettingsView: View {
    @Bindable var settings: UserSettings

    var body: some View {
        Form {
            Toggle("Notifications", isOn: $settings.notificationsEnabled)
        }
    }
}
```

---

<a id="q3"></a>
### Q3: How does Automatic Reference Counting (ARC) work in Swift and how do you resolve Strong Reference Cycles with `weak` and `unowned`?

**Difficulty**: Intermediate

**Strategy**:
ARC tracks reference counts for class instances on the heap. Strong reference cycles occur when two objects hold strong references to each other (e.g. ViewModel and Closure). Fix by using:
- `weak`: Optional non-retaining reference automatically set to `nil` when the target is deallocated.
- `unowned`: Non-optional non-retaining reference used when the target is guaranteed to have the same or longer lifetime.

**Code Example**:
```swift
class Service {
    var onComplete: (() -> Void)?
}

class ViewModel {
    let service = Service()
    
    func setup() {
        // Capture list with [weak self] prevents retain cycle
        service.onComplete = { [weak self] in
            guard let self = self else { return }
            self.handleSuccess()
        }
    }
    func handleSuccess() { print("Done") }
}
```

---

<a id="q4"></a>
### Q4: What does Swift 6 strict concurrency actually enforce, and how do you migrate a data-racing app?

**Difficulty**: Advanced

**Strategy**:
Swift 6 language mode turns data races from runtime undefined behavior into compile-time errors. The compiler enforces Sendable checking of everything crossing isolation domains (global variables, captured references, arguments between actors), `let` constants must be of Sendable type to be shared, and `static var` / global `var` are rejected outright. Migration is gradual: keep Swift 5 mode, set `StrictConcurrency` to `complete` to surface warnings, fix them module by module, and only then flip the target to Swift 6.

- `SwiftSetting .enableUpcomingFeature("StrictConcurrency")` or `.swiftLanguageMode(.v6)` in SPM.
- Fix order: globals → captured references → `@unchecked Sendable` as last resort with a documented invariant.

**Code Example**:
```swift
// Swift 5 mode: compiles, races at runtime. Swift 6 mode: rejected.
final class Counter {
    var count = 0  // not Sendable (mutable class)
}

var sharedCounter = Counter()  // error in Swift 6: global 'var' of non-Sendable type

// Correct: isolated mutable state
@MainActor
final class CounterModel {
    var count = 0
    func increment() { count += 1 }
}

@MainActor var model = CounterModel()  // OK: actor-isolated global

// Cross-domain transfer requires Sendable values
struct Snapshot: Sendable {  // immutable value type: implicitly Sendable
    let value: Int
}

actor Aggregator {
    private var latest: Snapshot?
    func update(_ s: Snapshot) { latest = s }
    func read() -> Snapshot? { latest }
}
```

---

<a id="q5"></a>
### Q5: How does `Sendable` work, and when do you use `@unchecked Sendable`?

**Difficulty**: Advanced

**Strategy**:
`Sendable` is a marker protocol (no requirements, checked by the compiler) promising a value is safe to transfer across concurrency domains. Structs/enums get it automatically when all stored members are Sendable; classes only when they are `final`, have `let` stored properties of Sendable type, and no mutable state; actors conform implicitly; functions/closures use `@Sendable` instead. Use `@unchecked Sendable` only when you guarantee thread safety yourself (internal locking or immutable-after-init storage) — e.g., wrapping a `DispatchQueue`-guarded legacy class — because the compiler cannot see through manual synchronization.

- Never slap `@unchecked` on to silence diagnostics without writing the invariant down.
- `@Sendable` closures cannot capture mutable local variables, only `let`/Sendable captures.

**Code Example**:
```swift
// Automatic conformance: value semantics + Sendable members
struct UserProfile: Sendable {
    let id: UUID
    let displayName: String
}

// Class: immutable -> can conform safely
final class FrozenConfig: Sendable {
    let entries: [String: String]
    init(entries: [String: String]) { self.entries = entries }
}

// Manual guarantee: internal lock makes it safe, compiler cannot prove it
final class LockedBox<Value: Sendable>: @unchecked Sendable {
    private let lock = NSLock()
    private var value: Value

    init(_ value: Value) { self.value = value }

    func with<R>(_ body: (Value) -> R) -> R {
        lock.lock(); defer { lock.unlock() }
        return body(value)
    }
}

// Sendable function type crossing into a Task
func run(work: @Sendable @escaping () -> Void) {
    Task.detached(priority: .background) { work() }
}
```

---

<a id="q6"></a>
### Q6: What is `@preconcurrency` and when is it the right tool?

**Difficulty**: Advanced

**Strategy**:
`@preconcurrency` suppresses concurrency diagnostics for code that cannot yet be modernized, so your Swift 6 target can still interact with legacy dependencies. On an import it relaxes Sendable checking of that module's API; on a protocol conformance it tells the compiler the conforming type predates concurrency so requirements don't demand Sendable; on an attribute usage it hides violations in third-party frameworks. It is a migration aid, not a fix: the underlying races still exist, so plan to remove each usage once the dependency or module adopts strict concurrency.

- `@preconcurrency import LegacySDK` — silence Sendable warnings from an unupdated SDK.
- `final class VM: @preconcurrency ViewModelProtocol` — conform to an old non-Sendable-aware protocol.

**Code Example**:
```swift
// Dependency not yet updated for Swift 6
@preconcurrency import LegacyAnalytics

@MainActor
final class DashboardModel {
    private let analytics = LegacyAnalytics.shared  // non-Sendable SDK singleton

    func logAppear() {
        // Without @preconcurrency: "capture of 'analytics' with non-Sendable
        // type in @Sendable closure" under Swift 6 mode.
        Task { @MainActor in
            analytics.track("dashboard_appear")
        }
    }
}

// Retroactive conformance to a pre-concurrency protocol
protocol OldDelegate: AnyObject {
    func didFinish()
}

final class Adapter: @preconcurrency OldDelegate {
    func didFinish() { print("done") }
}
```

---

<a id="q7"></a>
### Q7: How do task groups work and when do you choose them over `async let`?

**Difficulty**: Intermediate

**Strategy**:
`withTaskGroup` runs a dynamic number of child tasks that share the parent's cancellation and are awaited before the scope exits — the core of structured concurrency. Use `async let` for a fixed, known set of parallel operations (2–3 calls); use a group when the count depends on data. Child task results must be collected by consuming `group.next()` (or iterating) before the scope closes; throwing children surface errors as you await them. Order results by grouping pairs `(index, value)` when you need to preserve input order.

- `group.addTask` children start immediately and may interleave.
- Errors: cancel remaining work by throwing out of the loop; the group cancels children on scope exit.

**Code Example**:
```swift
struct Order: Sendable { let id: String; let total: Decimal }

struct APIClient: Sendable {
    func order(id: String) async throws -> Order { Order(id: id, total: 0) }
    func user() async throws -> User { User() }
    func posts() async throws -> [Post] { [] }
}
struct User: Sendable { let name = "" }
struct Post: Sendable { let id = UUID() }
let client = APIClient()

func fetchOrders(ids: [String]) async throws -> [Order] {
    try await withThrowingTaskGroup(of: (Int, Order).self) { group in
        for (index, id) in ids.enumerated() {
            group.addTask {
                let order = try await client.order(id: id)
                return (index, order)
            }
        }
        var buffer = [Int: Order]()
        buffer.reserveCapacity(ids.count)
        while let (index, order) = try await group.next() {
            buffer[index] = order
        }
        return ids.indices.compactMap { buffer[$0] }  // preserve input order
    }
}

// Fixed parallelism: async let is simpler
func loadProfile() async throws -> (User, [Post]) {
    async let user = client.user()
    async let posts = client.posts()
    return try await (user, posts)
}
```

---

<a id="q8"></a>
### Q8: How does task cancellation work in Swift Concurrency, and how do you make your code cancellable correctly?

**Difficulty**: Advanced

**Strategy**:
Cancellation is cooperative: `Task.cancel()` sets a flag and triggers cancellation of the running operation (e.g., `URLSession` throws `URLError(.cancelled)`, `Task.sleep` throws `CancellationError`), but CPU-bound loops only stop if they check. Respond via `Task.checkCancellation()`, `Task.isCancelled`, or a `withTaskCancellationHandler` to bridge non-async cancellation APIs. Cancellation propagates automatically from parent to child tasks, and structured scopes cancel children when the scope exits early. Cancellation is not rejection: cancelled tasks should clean up and rethrow `CancellationError`, not return partial data silently.

- Never swallow `CancellationError` deep inside — let it propagate so callers can distinguish.
- SwiftUI's `.task` modifier cancels its task when the view disappears.

**Code Example**:
```swift
struct PriceFetcher {
    func fetchPrices(symbols: [String]) async throws -> [String: Decimal] {
        var results: [String: Decimal] = [:]
        for symbol in symbols {
            try Task.checkCancellation()  // throws CancellationError
            results[symbol] = try await price(for: symbol)
        }
        return results
    }

    private func price(for symbol: String) async throws -> Decimal {
        let (data, _) = try await URLSession.shared.data(from: URL(string: "https://api.example.com/p/\(symbol)")!)
        return (try? JSONDecoder().decode(Decimal.self, from: data)) ?? 0
    }
}

final class ImageTransformer {
    func render(url: URL, size: CGSize) async throws -> UIImage { UIImage() }
    func cancel() {}
}

// Bridging an API with a completion-based cancel
func resizedImage(at url: URL, size: CGSize) async throws -> UIImage {
    let transformer = ImageTransformer()
    return try await withTaskCancellationHandler {
        try await transformer.render(url: url, size: size)
    } onCancel: {
        transformer.cancel()  // invoked synchronously on cancel
    }
}

// SwiftUI structured cancellation for free
struct PricesView: View {
    @State private var prices: [String: Decimal] = [:]
    var body: some View {
        List { ForEach(prices.sorted(by: { $0.value > $1.value }), id: \.key) { Text("\($0.key): \($0.value)") } }
            .task { prices = (try? await PriceFetcher().fetchPrices(symbols: ["AAPL", "GOOG"])) ?? [:] }
    }
}
```

---

<a id="q9"></a>
### Q9: What is the difference between `Task {}`, `Task.detached`, and structured child tasks?

**Difficulty**: Intermediate

**Strategy**:
`Task {}` is an unstructured task that inherits the current actor context (e.g., `@MainActor` if started from a view), priority, and task-local values; it starts immediately and does not propagate cancellation to/from its parent. `Task.detached {}` also creates an unstructured task but inherits nothing — it runs on the global concurrent executor — so use it to escape an actor (e.g., kick off CPU work from `@MainActor` without hopping back). Structured children (`async let`, task groups) are tied to their lexical scope: awaited by the parent, automatically cancelled when the scope throws or exits, and inherit priority/context. Rule of thumb: prefer structured; use `Task {}` for fire-and-forget UI work from an event handler; `Task.detached` rarely, and only when inheritance is actively wrong.

**Code Example**:
```swift
@MainActor
final class FeedModel {
    func refreshTapped() async {
        // Inherits @MainActor — safe to touch UI state after awaiting
        Task { await load() }
        // Escapes the main actor entirely; explicitly hop back for UI
        Task.detached(priority: .userInitiated) {
            let digest = Self.computeDigest()  // CPU-bound off main
            await MainActor.run { self.digest = digest }
        }
    }

    private func load() async { /* update @Published state */ }
    nonisolated static func computeDigest() -> String { "0x9f" }
    var digest = ""
}

// Structured: cannot leak, cancels with scope
func handle() async throws {
    async let config = loadConfig()   // child task
    let c = try await config          // must be awaited before return
    print(c)
}
```

---

<a id="q10"></a>
### Q10: Explain actor reentrancy — why can an actor "interleave" and how do you defend against it?

**Difficulty**: Expert

**Strategy**:
An actor serializes access to its state only between suspension points. When an actor method `await`s, the actor's executor can run other work (the method is reentrant), so state observed before an `await` may have changed by the time execution resumes. Reentrancy avoids deadlocks and keeps the cooperative pool utilized, but it breaks naive check-then-act sequences (e.g., deduplication: two callers both see `inFlight == nil` and start duplicate network calls). Defenses: make the check-and-commit synchronous with no awaits in the critical section; store a continuation/task handle for the second caller to await instead of re-fetching; or re-validate state after each suspension and reconcile.

**Code Example**:
```swift
actor ImageCache {
    enum Status { case loading(Task<UIImage, Error>), ready(UIImage) }
    private var entries: [URL: Status] = [:]

    func image(for url: URL) async throws -> UIImage {
        if let status = entries[url] {                 // synchronous section
            switch status {
            case .ready(let image): return image
            case .loading(let task): return try await task.value  // dedupe!
            }
        }
        // Critical: addTask returns Task handle; state committed BEFORE awaiting
        let task = Task { try await download(url) }
        entries[url] = .loading(task)
        do {
            let image = try await task.value
            entries[url] = .ready(image)
            return image
        } catch {
            entries[url] = nil                         // allow retry
            throw error
        }
    }
}
```

---

<a id="q11"></a>
### Q11: What are global actors and how does actor hopping affect performance?

**Difficulty**: Advanced

**Strategy**:
A global actor (`@MainActor`, or your own via `@globalActor`) is a singleton actor whose isolation can be applied to types, methods, and properties; calls from outside hop onto its executor, and calls within it run without suspension. Hopping costs a job enqueue and a thread switch — cheap individually, but hundreds of `@MainActor` hops per frame show up as main-thread congestion. Audit with Instruments: batch work onto one side of a boundary, keep model/parser code `nonisolated`, and use `nonisolated` + value types to move computation off the main actor entirely. `MainActor.assumeIsolated` (and `preconditionIsolation`) bridges synchronous callbacks that are guaranteed to run on the main thread.

**Code Example**:
```swift
@globalActor
actor DBActor {
    static let shared = DBActor()
}

struct Table: Codable, Sendable { let name: String; let rows: Int }

@DBActor
final class Database {                    // all methods isolated to DBActor
    private var tables: [String: Table] = [:]
    func table(_ name: String) -> Table? { tables[name] }

    func sync(data: Data) throws {
        // Parsing stays off the DB actor; only the mutation hops
        let decoded = Parser.decode(data)
        for table in decoded { tables[table.name] = table }
    }
}

struct Parser: Sendable {
    // nonisolated by default: runs on caller's executor, no hop needed
    static func decode(_ data: Data) throws -> [Table] {
        try JSONDecoder().decode([Table].self, from: data)
    }
}

// Bridging a guaranteed-main-thread API
func onMainCallback(_ block: @escaping () -> Void) {
    DispatchQueue.main.async {
        MainActor.assumeIsolated { block() }  // runtime-verified
    }
}
```

---

<a id="q12"></a>
### Q12: How does the `@Observable` macro work under the hood?

**Difficulty**: Expert

**Strategy**:
`@Observable` rewrites the class at compile time: stored properties become computed properties backed by storage inside an inserted `_`-prefixed registrar field (`@ObservationTracked` per property), and the class conforms to `Observable` with an `access`/`withMutation` pair around each get/set. During SwiftUI body evaluation, each property read registers the enclosing view with the registrar keyed by property, so an invalidation fires only for views that actually read the changed property — no `objectWillChange` broadcasting to every observer. Consequences: `@ObservationIgnored` opts properties out (e.g., cancellables, delegates), only `var` stored properties can be tracked, and the macro is just source generation — you can inspect the expansion in Xcode.

- Fine-grained tracking replaces whole-object `@Published` invalidation.
- Observation is UI-toolkit-agnostic: `withObservationTracking` powers any custom observer.

**Code Example**:
```swift
import Observation

@Observable
final class LibraryModel {
    var books: [Book] = []          // tracked: rewritten to computed + registrar
    var filter = ""
    @ObservationIgnored             // not tracked: no UI depends on it
    private var loadTask: Task<Void, Never>?

    var filtered: [Book] {
        books.filter { filter.isEmpty || $0.title.localizedStandardContains(filter) }
    }

    func load() {
        loadTask?.cancel()
        loadTask = Task { books = (try? await fetchBooks()) ?? [] }
    }
}

struct LibraryView: View {
    @State private var model = LibraryModel()
    var body: some View {
        List(model.filtered) { BookRow(book: $0) }   // reads filtered+books+filter
            .safeAreaInset(edge: .bottom) {
                if model.books.isEmpty { ProgressView() }  // reads books only
            }
    }
}
// Changing `filter` re-evaluates the List content, not unrelated views that
// never touched it — this per-property diffing is the macro's whole point.

struct Book: Identifiable { let id = UUID(); var title = "" }
struct BookRow: View { let book: Book; var body: some View { Text(book.title) } }
```

---

<a id="q13"></a>
### Q13: What does `withObservationTracking` do and when would you use it directly?

**Difficulty**: Advanced

**Strategy**:
`withObservationTracking(_:onChange:)` records every `@Observable` property read inside its closure and calls `onChange` once, on the next mutation of any of those properties — then stops. It is one-shot: SwiftUI itself re-registers on each body evaluation. Use it directly to bridge Observation into non-SwiftUI layers: driving UIKit updates from an observable model, logging which properties a render actually touched, or building custom dependency-graph tooling. Because the handler doesn't receive the changed value or property, treat it purely as an invalidation signal.

**Code Example**:
```swift
import Observation
import UIKit

@Observable
final class ScoreBoard {
    var home = 0
    var away = 0
}

@MainActor
final class ScoreLabel: UILabel {
    private var board: ScoreBoard?
    private var observeTask: Task<Void, Never>?

    func bind(_ board: ScoreBoard) {
        self.board = board
        observeTask?.cancel()
        observeTask = Task {              // inherits @MainActor
            render()
            while !Task.isCancelled {
                // Suspend until any tracked property changes, then re-render.
                await withCheckedContinuation { continuation in
                    withObservationTracking {
                        _ = board.home            // register reads
                        _ = board.away
                    } onChange: {
                        continuation.resume()     // one-shot: fires exactly once
                    }
                }
                render()
            }
        }
    }

    private func render() {
        guard let board else { return }
        text = "\(board.home) – \(board.away)"
        setNeedsLayout()
    }
}
// Each mutation of home/away resumes the continuation once; the while-loop
// re-establishes tracking — mirroring what SwiftUI does per body call.
```

---

<a id="q14"></a>
### Q14: How does SwiftUI use identity to diff views, and what's the difference between structural and explicit identity?

**Difficulty**: Advanced

**Strategy**:
SwiftUI diffs the view tree by identity first, then compares values. Structural identity comes from a view's position and type in the hierarchy — same position + same type = same identity, so `@State` survives re-renders and animations interpolate. Explicit identity comes from `ForEach(id:)`, `.id(_:)`, or `List(selection:)`; changing an explicit id makes SwiftUI treat the view as a brand-new element: state resets and it animates in/out rather than updating. Conditional branches (`if/else`) with different types create different structural identities, which is why switching branch types destroys `@State` — `Group`/`@ViewBuilder` merging or matched branch types avoids it.

- `.id(model.id)` forces full teardown/rebuild — a debugging hammer and a state-reset lever.
- `AnyView` erases type so the diffing engine sees different identities and falls back to teardown.

**Code Example**:
```swift
struct Chat: Identifiable { let id = UUID(); var title = "" }
struct ChatRow: View { let chat: Chat; var body: some View { Text(chat.title) } }
struct CounterLabel: View {
    @State private var count = 0
    var body: some View {
        Button("Count \(count)") { count += 1 }
    }
}

struct ChatList: View {
    @State private var chats = [Chat]()
    @State private var editToken = 0

    var body: some View {
        List {
            ForEach(chats) { chat in          // explicit id == chat.id
                ChatRow(chat: chat)
            }
            .onDelete { chats.remove(at: $0) }
        }
        .id(editToken)   // bumping editToken rebuilds the list, resetting rows' @State
    }
}

// Branch pitfall: different types -> identity destroyed on toggle
struct Toggler: View {
    @State private var showText = true
    var body: some View {
        VStack {
            if showText {
                CounterLabel()          // type A: its @State is lost when switching
            } else {
                CounterLabel().hidden() // type B: fresh identity, fresh @State
            }
            Button("Flip") { showText.toggle() }
        }
    }
}
```

---

<a id="q15"></a>
### Q15: Why is `AnyView` expensive and what should you use instead?

**Difficulty**: Advanced

**Strategy**:
`AnyView` is a type-erasing box. It hides the concrete view type from SwiftUI's diffing, so the runtime must tear down and rebuild the subtree on any change it can't prove equal, loses specialized layout/drawing fast paths, and blocks some optimization that relies on static types. Better tools: `@ViewBuilder` lets a single `body` return heterogeneous branches via an implicit `_ConditionalContent`; `Group` merges children without erasure; `if case` pattern matching with `@ViewBuilder` handles enum-driven UI; generics (`func row<V: View>(@ViewBuilder _ content: () -> V)`) keep types concrete. Reserve `AnyView` for genuinely dynamic, API-boundary cases (e.g., migrating table-driven UIs), not to silence compiler errors.

**Code Example**:
```swift
enum ContentState { case loading, loaded([Post]), failed(Error) }

struct FeedView: View {
    let state: ContentState

    var body: some View {
        switch state {                    // @ViewBuilder on body: no erasure
        case .loading:
            ProgressView()
        case .loaded(let posts):
            List(posts) { PostRow(post: $0) }
        case .failed(let error):
            ErrorView(error: error)
        }
    }
}

struct Post: Identifiable { let id = UUID(); var title = "" }
struct PostRow: View { let post: Post; var body: some View { Text(post.title) } }
struct ErrorView: View {
    let error: Error
    var body: some View { ContentUnavailableView("Something went wrong", systemImage: "exclamationmark.triangle") }
}

// Generic instead of AnyView for reusable containers
struct Card<Content: View>: View {
    let content: Content
    init(@ViewBuilder content: () -> Content) { self.content = content() }
    var body: some View {
        content.padding().background(.thinMaterial, in: .rect(cornerRadius: 16))
    }
}
```

---

<a id="q16"></a>
### Q16: How does the `Layout` protocol work, and when do you write a custom layout?

**Difficulty**: Expert

**Strategy**:
The `Layout` protocol (iOS 16+) lets you build custom container geometry that behaves like native containers. Three methods do the work: `sizeThatFits(_:subviews:cache:)` proposes a size to each child, measures results, and returns the container's own size; `placeSubviews(in:proposal:subviews:cache:)` assigns each child a position within the given bounds; `cache(subviews:)` stores intermediate data across the two passes for efficiency. Opt in to parent alignment via `alignmentGuide`-related hooks (`explicitAlignment` methods) and animation by conforming to `Animatable`. Reach for a custom layout when composition of stacks/grids/z-views can't express the geometry — snake/mosaic grids, radial arrangements, flow layout — not as a first resort.

**Code Example**:
```swift
struct FlowLayout: Layout {              // wraps children like text, row by row
    var spacing: CGFloat = 8

    func sizeThatFits(proposal: ProposedViewSize, subviews: Subviews, cache: inout ()) -> CGSize {
        let maxWidth = proposal.width ?? .infinity
        var x: CGFloat = 0, y: CGFloat = 0, rowHeight: CGFloat = 0
        for subview in subviews {
            let size = subview.sizeThatFits(.unspecified)
            if x + size.width > maxWidth, x > 0 { x = 0; y += rowHeight + spacing; rowHeight = 0 }
            x += size.width + spacing
            rowHeight = max(rowHeight, size.height)
        }
        return CGSize(width: maxWidth == .infinity ? x : maxWidth, height: y + rowHeight)
    }

    func placeSubviews(in bounds: CGRect, proposal: ProposedViewSize, subviews: Subviews, cache: inout ()) {
        let maxWidth = bounds.width
        var x = bounds.minX, y = bounds.minY, rowHeight: CGFloat = 0
        for subview in subviews {
            let size = subview.sizeThatFits(.unspecified)
            if x + size.width > bounds.minX + maxWidth, x > bounds.minX {
                x = bounds.minX; y += rowHeight + spacing; rowHeight = 0
            }
            subview.place(at: CGPoint(x: x, y: y), anchor: .topLeading, proposal: .unspecified)
            x += size.width + spacing
            rowHeight = max(rowHeight, size.height)
        }
    }
}

struct TagsView: View {
    let tags = ["swift", "concurrency", "swiftui", "layout", "interview"]
    var body: some View {
        FlowLayout(spacing: 6) {
            ForEach(tags, id: \.self) { Text($0).padding(6).background(.quaternary, in: .capsule) }
        }
        .padding()
    }
}
```

---

<a id="q17"></a>
### Q17: What are alignment guides and how do you use them for cross-view alignment?

**Difficulty**: Advanced

**Strategy**:
Every view has an implicit frame whose edges and well-known guides (`.firstTextBaseline`, `.lastTextBaseline`, `.center`) live in its coordinate space. `alignmentGuide(_:computeValue:)` lets a view shift where a named guide sits within itself; parent containers then line up children along the same guide. `frame(alignment:)` only positions content inside one view, while alignment guides align siblings — classic example: aligning multi-line labels of different font sizes by first text baseline. Use `AlignmentID` to define custom named guides when the built-ins don't fit (e.g., align a column of currency values along the decimal separator).

**Code Example**:
```swift
struct BaselineRows: View {
    let rows: [(title: String, value: String)]

    var body: some View {
        HStack(alignment: .firstTextBaseline, spacing: 16) {
            VStack(alignment: .leading, spacing: 8) {
                ForEach(rows, id: \.title) { Text($0.title).font(.headline) }
            }
            VStack(alignment: .trailing, spacing: 8) {
                ForEach(rows, id: \.title) { Text($0.value).font(.title3.monospacedDigit()) }
            }
        }
    }
}

// Custom guide: align on currency symbol
extension HorizontalAlignment {
    private enum CurrencyAlignment: AlignmentID {
        static func defaultValue(in context: ViewDimensions) -> CGFloat {
            context[.trailing]            // fallback: right edge
        }
    }
    static let currency = HorizontalAlignment(CurrencyAlignment.self)
}

struct AmountRow: View {
    let amount: Decimal
    var body: some View {
        HStack(alignment: .firstTextBaseline) {
            Text("€").alignmentGuide(.currency) { d in d[.leading] }
            Text("\(amount)").alignmentGuide(.currency) { d in d[.leading] - 12 }
        }
    }
}
```

---

<a id="q18"></a>
### Q18: How do `NavigationStack` and `navigationDestination` replace `NavigationView`, and how do you manage programmatic navigation?

**Difficulty**: Intermediate

**Strategy**:
`NavigationStack` is a single-column, push-based container; `NavigationView` (deprecated) tried to be everything and behaved differently per device. Destinations are data-driven: attach `navigationDestination(for: DestinationValue.self)` anywhere inside the stack, then push by making that value appear in the navigation path — either a typed `[DestinationValue]` binding or an untyped `NavigationPath` when you need heterogeneous destinations (e.g., from an App Intents deep link). Because pushes are values, restoring state, deep linking, and "navigate on button tap without NavigationLink" all reduce to appending to the path. Bind path with `@State` locally; keep it in an `@Observable` router for cross-cutting navigation.

**Code Example**:
```swift
enum Route: Hashable {
    case album(UUID), artist(String), settings

    @ViewBuilder var destination: some View {
        switch self {
        case .album(let id): Text("Album \(id.uuidString)")
        case .artist(let name): Text("Artist \(name)")
        case .settings: Text("Settings")
        }
    }
}

struct AlbumGrid: View {
    var body: some View { Text("Albums") }
}
enum URLParser {
    static func albumID(from url: URL) -> UUID? { UUID(uuidString: url.lastPathComponent) }
}

struct RootView: View {
    @State private var path = [Route]()

    var body: some View {
        NavigationStack(path: $path) {
            AlbumGrid()
                .navigationDestination(for: Route.self) { $0.destination }
                .toolbar {
                    Button("Settings") { path.append(.settings) }   // programmatic push
                }
        }
        .onOpenURL { url in
            guard let id = URLParser.albumID(from: url) else { return }
            path = [.album(id)]                                     // deep link: reset + push
        }
    }
}
```

---

<a id="q19"></a>
### Q19: How does `NavigationSplitView` work and how do you keep selections in sync across columns?

**Difficulty**: Intermediate

**Strategy**:
`NavigationSplitView` provides two- or three-column layouts (sidebar/content/detail) that automatically collapse to a stack on compact-width devices like iPhone. The canonical pattern: `NavigationSplitView { sidebar } detail { content }` with the sidebar being a `List(selection:)` bound to an optional value, and `navigationDestination` (or a switch in the detail) rendering the selection. Control column visibility with the `columnVisibility` binding (`.detailOnly`, `.all`, `.automatic`) and sizing with `navigationSplitViewColumnWidth` for sidebar behavior like UIKit's `UISplitViewController`. On compact widths, pushing into detail requires a `NavigationStack` inside the detail column, combined with the two-column binding pattern.

**Code Example**:
```swift
struct MailSplitView: View {
    @State private var selectedFolder: MailFolder?
    @State private var selectedMail: Mail.ID?
    @State private var columnVisibility: NavigationSplitViewVisibility = .all

    var body: some View {
        NavigationSplitView(columnVisibility: $columnVisibility) {
            List(MailFolder.allCases, selection: $selectedFolder) { folder in
                Label(folder.label, systemImage: folder.icon)
            }
            .navigationSplitViewColumnWidth(min: 200, ideal: 240)
        } content: {
            if let folder = selectedFolder {
                List(folder.mails) { mail in
                    MailRow(mail: mail).tag(mail.id as Mail.ID?)
                }
                .listStyle(.plain)
            } else {
                ContentUnavailableView("Choose a folder", systemImage: "folder")
            }
        } detail: {
            NavigationStack {
                if let id = selectedMail, let mail = MailStore.find(id) {
                    MailDetailView(mail: mail)
                } else {
                    ContentUnavailableView("No mail selected", systemImage: "envelope")
                }
            }
        }
    }
}
```

---

<a id="q20"></a>
### Q20: How do you implement deep links that restore full navigation state in a SwiftUI app?

**Difficulty**: Advanced

**Strategy**:
Encode every reachable screen as a `Hashable` route value, drive the stack with a `NavigationStack(path:)` binding, and translate incoming URLs into `[Route]` — the app is then "deep link = array assignment". Parse in `.onOpenURL` (universal links) or via `AppDelegate`/`scenePhase` for cold launches; always restore the full path array, not just the leaf, so back-swiping works naturally. Handle cold start by routing from `init`/`.task` using persisted last-path state (`@SceneStorage`), and debounce or coalesce rapid links so you don't fight the user mid-gesture. Test both paths: `xcrun simctl openurl` and `.onOpenURL` previews.

**Code Example**:
```swift
enum Route: Hashable {
    case order(UUID)
    case orderDetail(UUID, section: DetailSection)
    case support
}

@Observable
final class Router {
    var path = [Route]()

    func handle(_ url: URL) {
        // myapp://order/<uuid>/summary  ->  [.order(id), .orderDetail(id, .summary)]
        guard url.scheme == "myapp" else { return }
        let parts = url.pathComponents.filter { $0 != "/" }
        switch url.host {
        case "order" where parts.count >= 1:
            guard let id = UUID(uuidString: parts[0]) else { return }
            path = [.order(id)]
            if parts.count > 1, let section = DetailSection(rawValue: parts[1]) {
                path.append(.orderDetail(id, section: section))
            }
        case "support":
            path = [.support]
        default:
            break
        }
    }
}

struct RootView: View {
    @State private var router = Router()
    var body: some View {
        NavigationStack(path: Bindable(router).path) {
            OrderListView()
                .navigationDestination(for: Route.self) { $0.destination }
        }
        .onOpenURL { router.handle($0) }
    }
}
```

---

<a id="q21"></a>
### Q21: How do you choose between `@State`, `@Binding`, `@Bindable`, `@StateObject`, and `@Environment` for state ownership?

**Difficulty**: Intermediate

**Strategy**:
Ownership decides the property wrapper. `@State` — the view itself owns ephemeral, local state (struct state, simple models); SwiftUI stores it outside the struct so it survives re-renders. `@Binding` — a child mutates state the parent owns (two-way reference, `$` projection). `@Bindable` — create bindings (`.text`, `$model.prop`) into an `@Observable` reference the parent owns. `@StateObject` — the view owns an `ObservableObject` reference (legacy pattern; with `@Observable` you just use `@State`). `@Environment(.self)` — read a model injected higher up without threading it through initializers; the environment is the SwiftUI-native DI mechanism.

- Rule: state should live at the lowest common ancestor of all views that need it.
- Never create `@Observable`/`ObservableObject` instances in computed properties or `body`.

**Code Example**:
```swift
@Observable
final class Draft { var text = ""; var tags: Set<String> = [] }

struct ComposeView: View {
    @State private var draft = Draft()        // view owns the model
    @Environment(SettingsModel.self) private var settings  // injected from app

    var body: some View {
        Form {
            DraftForm(draft: draft)           // child edits via @Bindable
            Section {
                Text("Signing as \(settings.accountName)")   // read-only env
            }
        }
    }
}

struct DraftForm: View {
    @Bindable var draft: Draft                // parent-owned; bindings for free
    var body: some View {
        TextField("Title", text: $draft.text)
        TextField("Tags", text: .constant(draft.tags.sorted().joined(separator: ",")))
    }
}
```

---

<a id="q22"></a>
### Q22: How does `@Environment` work and how do you define custom environment values with the `@Entry` macro (iOS 18)?

**Difficulty**: Intermediate

**Strategy**:
The environment is a typed, hierarchical key-value store flowing down the view tree: views read values (traits like `colorScheme`, `dismiss`, or injected models via `@Environment(Model.self)`) and any subtree can override them with `.environment(...)` — enabling theme overrides, per-sheet contexts, and preview substitutions. Before iOS 18, custom values needed a boilerplate `EnvironmentKey` struct plus an `EnvironmentValues` extension; the `@Entry` macro (iOS 18+) generates the key, default value, and extension from a single property declaration, and also works for `FocusedValue`, `Transaction`, and `ContainerValues`.

**Code Example**:
```swift
// iOS 18+: @Entry macro replaces ~10 lines of EnvironmentKey boilerplate
extension EnvironmentValues {
    @Entry var featureFlags = FeatureFlags.default
    @Entry var requestTimeout: TimeInterval = 30
}

struct FeatureFlags: Sendable {
    var enableStreaks = true
    static let `default` = FeatureFlags()
}

struct RootView: View {
    @State private var settings = SettingsModel()
    var body: some View {
        ContentView()
            .environment(settings)
            .environment(\.featureFlags, FeatureFlags(enableStreaks: false))
            .environment(\.requestTimeout, 10)   // subtree override for previews/debug
    }
}

struct StreakBadge: View {
    @Environment(\.featureFlags) private var flags
    var body: some View {
        if flags.enableStreaks { Label("12 🔥", systemImage: "flame.fill") }
    }
}
```

---

<a id="q23"></a>
### Q23: How does SwiftUI view invalidation work, and how do you debug excessive re-renders?

**Difficulty**: Advanced

**Strategy**:
A view re-renders when state it read during `body` changes (with `@Observable`, down to the exact property), when its parent re-instantiates it with different inputs, or when identity changes. Cost is proportional to what body re-executes: keep bodies small, push state down into leaf views, extract subviews so a change invalidates one row not the whole list, and pass primitives rather than giant models into rows. Debug with `Self._printChanges()` at the top of body (prints which property triggered the update) and the SwiftUI instrument in Instruments ("View Body" invocations). Common fixes: move `onReceive`/timers out of hot paths, `EquatableView`/`.equatable()` for expensive children, and `id`-scoped state instead of global invalidation.

**Code Example**:
```swift
struct PriceRow: View {
    let symbol: String
    let price: Decimal
    var body: some View {
        let _ = Self._printChanges()   // debug: prints e.g. "price -> ..." triggers
        HStack {
            Text(symbol).foregroundStyle(.secondary)
            Spacer()
            Text(price, format: .currency(code: "USD"))
        }
    }
}

struct TickerList: View {
    @State private var prices: [String: Decimal] = ["AAPL": 199, "GOOG": 141]
    var body: some View {
        List {
            // Only re-created rows re-render when their specific price changes:
            ForEach(prices.sorted(by: { $0.key < $1.key }), id: \.key) { symbol, price in
                PriceRow(symbol: symbol, price: price)   // value inputs, cheap diff
            }
        }
        .task {
            for await update in Feed.updates { prices = update }  // coarse updates OK
        }
    }
}
```

---

<a id="q24"></a>
### Q24: When does `drawingGroup()` help performance, and when does it hurt?

**Difficulty**: Advanced

**Strategy**:
`drawingGroup()` flattens its subtree into a single offscreen bitmap rendered with Metal, trading CPU-based per-view compositing for one GPU texture. It wins when many overlapping, semi-transparent, blurred, or shadowed views create expensive per-frame compositing (gradients, blurs, particle rows), especially during animation. It hurts when the content changes frequently and is large (re-rasterizing the whole bitmap each frame), for text-heavy layouts (Core Text rasterization is already fast and caching changes), or when effects must remain vector-accurate at any scale — the bitmap samples rather than re-renders when scaled. Always measure with Instruments' Core Animation FPS + SwiftUI template before/after; treat it as a scalpel, not a default modifier.

**Code Example**:
```swift
struct AuroraBackground: View {
    var body: some View {
        TimelineView(.animation) { timeline in
            let t = timeline.date.timeIntervalSinceReferenceDate
            ZStack {
                ForEach(0..<6, id: \.self) { i in
                    Circle()
                        .fill(.radialGradient(colors: [.teal.opacity(0.35), .clear],
                                              center: .center,
                                              radius: 180))
                        .frame(width: 320, height: 320)
                        .offset(x: cos(t + Double(i)) * 90,
                                y: sin(t * 1.3 + Double(i)) * 90)
                        .blur(radius: 12)
                }
            }
            .drawingGroup()   // 6 blurred circles composited once per frame on GPU
        }
        .ignoresSafeArea()
    }
}
```

---

<a id="q25"></a>
### Q25: How do `LazyVStack`/`LazyHStack` and `List` differ from regular stacks, and what pitfalls come with laziness?

**Difficulty**: Beginner

**Strategy**:
`VStack` creates and lays out every child immediately — fine for dozens of views, catastrophic for thousands. Lazy stacks defer creation until a child approaches the visible viewport, so memory and initial layout stay flat. `List` adds its own recycling (like UIKit's reuse), selection/editing/swipe actions, and platform styling; lazy stacks are plain layouts without reuse. Pitfalls of laziness: children are created late so `onAppear` fires near-visibility (use it for pagination, not for "view loaded once" logic), items can't use `GeometryReader`-dependent absolute positioning reliably before materialization, and giant non-lazy subviews inside one item defeat the purpose.

**Code Example**:
```swift
struct CatalogView: View {
    let items = (1...10_000).map { CatalogItem(id: $0) }

    var body: some View {
        ScrollView {
            LazyVStack(alignment: .leading, pinnedViews: [.sectionHeaders]) {
                ForEach(items) { item in
                    CatalogRow(item: item)
                        .onAppear {
                            if item.id == items.last?.id { loadMore() }  // pagination hook
                        }
                }
            }
        }
    }

    private func loadMore() { /* fetch next page */ }
}

struct CatalogItem: Identifiable { let id: Int; var title: String { "Item \(id)" } }
struct CatalogRow: View {
    let item: CatalogItem
    var body: some View { Text(item.title).padding(.vertical, 4) }
}
```

---

<a id="q26"></a>
### Q26: How do you profile SwiftUI performance with Instruments' SwiftUI template?

**Difficulty**: Advanced

**Strategy**:
The SwiftUI instrument (run the "SwiftUI" template) annotates the timeline with view updates: it shows when views gained/lost identity, how many times `body` executed, and what state change triggered it — correlate spikes with the "View Updates" and "Body Recomputes" tracks next to Time Profiler and Core Animation FPS. Workflow: reproduce a jank scenario, record ~10s, look for body recomputes that scale with list size (invalidation too broad), hitches in Rendering (long commits), and hangs flagged by the Hangs instrument. Fix patterns: narrow `@Observable` reads, extract rows, remove `AnyView`/`.id` churn, move work out of body into `task`/model. Pair with `Self._printChanges()` in debug builds for the exact trigger property.

**Code Example**:
```swift
// Diagnostic scaffolding to correlate with the SwiftUI instrument
struct FeedRow: View {
    let post: Post
    @Environment(FeedModel.self) private var model

    var body: some View {
        #if DEBUG
        let _ = Self._printChanges()  // prints trigger reason on each recompute
        #endif
        HStack(alignment: .top, spacing: 12) {
            AsyncImage(url: post.avatarURL) { $0.resizable().scaledToFill() }
                placeholder: { Color.quaternary }
                .frame(width: 44, height: 44).clipShape(.circle)
            VStack(alignment: .leading, spacing: 4) {
                Text(post.author).font(.subheadline.weight(.semibold))
                Text(post.body).font(.subheadline).foregroundStyle(.secondary).lineLimit(3)
            }
        }
        .task { await model.warmMedia(for: post) }   // work off body
    }
}
```

---

<a id="q27"></a>
### Q27: How do you model data and relationships in SwiftData?

**Difficulty**: Intermediate

**Strategy**:
SwiftData (iOS 17+) builds persistence on Core Data's stack but drives it from code: annotate a class with `@Model` and its stored properties become persisted attributes, while class-typed properties become relationships — the macro generates the `PersistentModel` conformance and schema. Configure cardinality with `@Relationship(.cascade)` (delete rule) and keep both sides for inverses (or let SwiftData infer). `@Attribute(.unique)` enforces uniqueness, `.allowsCloudEncryption` enables CloudKit field-level encryption, and `@Transient` excludes storage. Fetch with the `@Query` property wrapper or `ModelContext`; use `modelContainer(for:)` at the app root to set up storage.

**Code Example**:
```swift
import SwiftData

@Model
final class Author {
    @Attribute(.unique) var name: String
    var birthYear: Int
    @Relationship(deleteRule: .cascade, inverse: \Book.author)
    var books: [Book] = []

    init(name: String, birthYear: Int) {
        self.name = name
        self.birthYear = birthYear
    }
}

@Model
final class Book {
    @Attribute(.unique) var isbn: String
    var title: String
    var published: Date
    var author: Author?          // inverse side
    @Transient var cachedCover: UIImage?

    init(isbn: String, title: String, published: Date) {
        self.isbn = isbn; self.title = title; self.published = published
    }
}

@main
struct LibraryApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(for: [Author.self, Book.self])
    }
}
```

---

<a id="q28"></a>
### Q28: How do schema migrations work in SwiftData, and how do they compare to Core Data migrations?

**Difficulty**: Expert

**Strategy**:
SwiftData migrations are declared in code with `VersionedSchema` (a snapshot of model types per version) and a `SchemaMigrationPlan` listing stages. A `lightweight` stage handles additive, inferable changes (new optional attributes, new models, renamed via `@Attribute(originalName:)`); a `custom` stage runs a `SchemaMigrationStage.Migration` with `willMigrate`/`didMigrate` hooks where you transform `BackingData` by hand — needed for splits, type changes, or backfills. Point the container at the plan (`modelContainer(for:migrationPlan:)`) and SwiftData infers the path from stored metadata version hashes, similar to Core Data's inferred vs custom mapping models but expressed in Swift instead of xcmappingmodel files. Golden rule: never edit an old schema's types in place — ship a new versioned snapshot.

**Code Example**:
```swift
import SwiftData

enum LibraryV2: VersionedSchema {
    static let versionIdentifier = Schema.Version(2, 0, 0)
    static var models: [any PersistentModel.Type] { [Author.self, Book.self] }

    @Model
    final class Book {
        @Attribute(originalName: "isbn") var isbnV2: String  // renamed attribute
        var title: String
        var wordCount: Int = 0                               // new, defaulted
        init(isbnV2: String, title: String, wordCount: Int) {
            self.isbnV2 = isbnV2; self.title = title; self.wordCount = wordCount
        }
    }
    @Model final class Author { var name = ""; var books: [Book] = []; init() {} }
}

enum LibraryMigrationPlan: SchemaMigrationPlan {
    static var schemas: [any VersionedSchema.Type] { [LibraryV1.self, LibraryV2.self] }
    static var stages: [MigrationStage] {
        [MigrationStage.lightweight(fromVersion: LibraryV1.self, toVersion: LibraryV2.self)]
        // For data transforms:
        // MigrationStage.custom(fromVersion: LibraryV1.self, toVersion: LibraryV2.self) {
        //     context in … willMigrate …
        // } didMigrate: { context, book in … }
    }
}

@main
struct LibraryApp: App {
    var body: some Scene {
        WindowGroup { ContentView() }
            .modelContainer(for: [LibraryV2.Author.self, LibraryV2.Book.self],
                            migrationPlan: LibraryMigrationPlan.self)
    }
}
```

---

<a id="q29"></a>
### Q29: SwiftData vs Core Data in 2025 — which do you pick for a new app?

**Difficulty**: Intermediate

**Strategy**:
SwiftData is the SwiftUI-native default: code-first `@Model` macros, `@Query` views that update automatically, seamless CloudKit sync opt-in, and full interop with the underlying Core Data store (`.storeType(.sqlite)` etc.). Choose Core Data when you need features SwiftData still lacks or exposes awkwardly: complex fetch predicates beyond `#Predicate` limits, granular `NSFetchRequest` batching/tuning, programmatic store migration tooling, pre-existing xcdatamodeld investment, or heavy background-context workflows with fine control. They share the same persistence core, so SwiftData is not a toy — it's a layer with narrower surface. Migration pressure matters too: an existing mature Core Data stack rarely justifies a rewrite.

- New SwiftUI app, standard CRUD + CloudKit: SwiftData.
- Legacy schema, heavy programmatic migrations, or UIKit-heavy app: Core Data.

**Code Example**:
```swift
// SwiftData: query-driven UI in a few lines
import SwiftData

struct ShelfView: View {
    @Query(filter: #Predicate<Book> { $0.wordCount > 50_000 },
           sort: \Book.title,
           order: .forward,
           animation: .snappy)
    private var longBooks: [Book]

    var body: some View {
        List(longBooks) { Text($0.title) }
    }
}

// The same requirement in Core Data — more control, more ceremony:
// let request = NSFetchRequest<BookMO>(entityName: "Book")
// request.predicate = NSPredicate(format: "wordCount > %@", 50_000)
// request.sortDescriptors = [NSSortDescriptor(key: "title", ascending: true)]
// let books = try viewContext.fetch(request)   // + NSFetchedResultsController for UI
```

---

<a id="q30"></a>
### Q30: Combine vs AsyncStream — how do you bridge event streams into async/await, and when is each the right tool?

**Difficulty**: Advanced

**Strategy**:
Combine is a push-based reactive graph: publishers, operators, backpressure via demand, and composition — strong for UIKit/AppKit bindings, combining multiple sources, and debouncing/throttling heavy pipelines. `AsyncSequence`/`AsyncStream` is pull-based: the consumer awaits the next element, structured cancellation applies natively, and `for await` reads like normal code — the default inside SwiftUI (`.task`, `@Observable` models). Bridge callbacks into async with `AsyncStream { continuation in ... }` (including `onTermination` to clean up), and bridge Combine in with `publisher.values` (`AsyncPublisher`). Choose Combine when you need its operator catalog or KVO/timer glue; choose AsyncStream when the consumer drives pacing and you want Swift 6 concurrency semantics for free.

**Code Example**:
```swift
import Combine
import CoreLocation

// Callback-based delegate API -> AsyncStream
// The streamer is its own delegate: CLLocationManager.delegate is weak, so a
// local delegate object would be deallocated immediately — retain it in self.
final class LocationStreamer: NSObject, CLLocationManagerDelegate {
    private let manager = CLLocationManager()
    private var continuation: AsyncStream<CLLocation>.Continuation?

    func locations() -> AsyncStream<CLLocation> {
        manager.delegate = self
        manager.startUpdatingLocation()
        return AsyncStream { continuation in
            self.continuation = continuation
            continuation.onTermination = { [manager] _ in
                manager.stopUpdatingLocation()
            }
        }
    }

    func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
        for location in locations { continuation?.yield(location) }
    }

    func locationManager(_ manager: CLLocationManager, didFailWithError error: Error) {
        continuation?.finish()
    }
}

// SwiftUI consumption: structured, auto-cancelled on disappear
struct SpeedView: View {
    @State private var speed: Double = 0
    var body: some View {
        Text(speed, format: .number.precision(.fractionLength(1)))
            .task {
                let streamer = LocationStreamer()
                for await location in streamer.locations() {
                    speed = location.speed
                }
            }
    }
}
```

---

<a id="q31"></a>
### Q31: How do retain cycles manifest in SwiftUI, and where do you actually need `[weak self]`?

**Difficulty**: Intermediate

**Strategy**:
SwiftUI views are structs (no ARC cycle risk), but cycles appear via long-lived closures and reference-type models: a closure stored on a model that captures that model strongly, `Timer.publish` subscribers, NotificationCenter observers with strong captures, Combine cancellables held by the captured object, and delegates. You generally do NOT need `[weak self]` in `.task`/`.onAppear`/`.button` action closures — they're retained only while the view exists and SwiftUI breaks the lifetime itself. You DO need it when the escape outlives the owner: storing a completion on a singleton, subscribing a service the model owns, or `Task {}` captured inside a model that the task also keeps alive.

**Code Example**:
```swift
import Combine
import SwiftUI

final class SessionModel: ObservableObject {
    @Published var status: Status = .idle
    private var cancellables = Set<AnyCancellable>()
    private let beacon = BeaconService.shared   // singleton outlives the model

    func start() {
        // Cycle: beacon -> cancellable -> closure -> self (strong) -> beacon…
        beacon.signal
            .sink { [weak self] signal in        // break it
                self?.status = .active(signal)
            }
            .store(in: &cancellables)

        // Fire-and-forget from UI: no [weak self] needed — bounded by view lifetime
        Task { await refresh() }
    }

    private func refresh() async { status = .active("refresh") }
}
enum Status { case idle, active(String) }
final class BeaconService {
    static let shared = BeaconService()
    var signal = PassthroughSubject<String, Never>()
}
```

---

<a id="q32"></a>
### Q32: What are typed throws in Swift 6, and when do they improve API design?

**Difficulty**: Advanced

**Strategy**:
Swift 6 lets a function declare the concrete error type it throws — `throws(FileError)` — so callers get an exhaustive, compiler-checked `catch`. Benefits: `catch` clauses match exhaustively (like switching an enum), generic code can propagate `E` from a throwing closure parameter through itself (SE-0413), errors store cheaply in `Result<Success, Failure>`, and rethrows-style wrappers stop losing type information. Caveats: it's part of the signature (binary and source compatibility consideration), conversion to broader `throws` is allowed implicitly, but you cannot narrow a caller's expectations; libraries should use it where the error taxonomy is genuinely closed and stable. Don't use it for wrappers over arbitrary throwing code — `any Error` remains right there.

**Code Example**:
```swift
enum ConfigError: Error {
    case missingKey(String)
    case invalidFormat(key: String)
}

struct ConfigStore {
    func string(_ key: String) throws(ConfigError) -> String {
        guard let raw = rawValues[key] else { throw .missingKey(key) }
        guard raw.hasPrefix("s:") else { throw .invalidFormat(key: key) }
        return String(raw.dropFirst(2))
    }

    var rawValues: [String: String] = ["host": "s:api.example.com"]
}

func demo() {
    do {
        let host = try ConfigStore().string("host")
        print(host)
        let _ = try ConfigStore().string("port")
    } catch .missingKey(let key) {          // typed, exhaustive-friendly
        print("missing: \(key)")
    } catch .invalidFormat(let key) {
        print("bad format: \(key)")
    }                                       // no generic `catch {}` needed

    // Result with the typed failure, no erasure
    let result = Result { try ConfigStore().string("host") }
    print(result)  // success("api.example.com")
}
```

---

<a id="q33"></a>
### Q33: What is `Result` and when should you use it over throwing functions?

**Difficulty**: Beginner

**Strategy**:
`Result<Success, Failure>` models success/failure as a value: `.success` and `.failure` cases where `Failure` must conform to `Error`. Throwing functions express the same thing in control flow, which is more idiomatic in Swift — so prefer `throws` by default. Use `Result` when a value must be stored or transported: completion-based APIs (`(Result<T, E>) -> Void`), retries that remember the last failure, caching outcomes, or pipelines that accumulate errors instead of stopping at the first `throw`. `Result(catching:)` adapts throwing calls, and `try result.get()` converts back to throwing semantics.

**Code Example**:
```swift
struct CloudUploader {
    enum UploadError: Error { case offline, tooLarge(size: Int) }

    // Completion-based API where Result shines
    func upload(_ data: Data, completion: @escaping (Result<URL, UploadError>) -> Void) {
        guard data.count < 10_000_000 else { completion(.failure(.tooLarge(size: data.count))); return }
        guard Connection.isUp else { completion(.failure(.offline)); return }
        completion(.success(URL(string: "https://cdn.example.com/\(UUID().uuidString)")!))
    }

    // Retry loop keeps the last failure around — a value, not control flow
    func uploadWithRetry(_ data: Data, attempts: Int) async -> Result<URL, UploadError> {
        var last: Result<URL, UploadError> = .failure(.offline)
        for _ in 0..<attempts {
            last = await withCheckedContinuation { cont in
                upload(data) { cont.resume(returning: $0) }
            }
            if case .success = last { return last }
            try? await Task.sleep(for: .seconds(1))
        }
        return last
    }
}

enum Connection { static var isUp = true }
```

---

<a id="q34"></a>
### Q34: What is the difference between `some` and `any`, and what changed with implicit `any`?

**Difficulty**: Intermediate

**Strategy**:
`some View` is an opaque type: the caller doesn't know the concrete type, but it exists, is fixed at compile time, and calls are statically dispatched (often inlined/specialized) with no boxing. `any View` is an existential: a box holding any conforming type, dispatching through a witness table and possibly reference semantics, with a runtime cost for allocation and indirection. Since Swift 5.7 opaque types work as parameters (`some` means "one specific type" for the caller), and Swift 5.6+/6 requires writing `any` explicitly where you want an existential — making the cost visible. Use `some` everywhere you can; use `any` only when you truly need heterogeneity (mixed concrete types in a collection, API boundaries that erase type).

**Code Example**:
```swift
protocol Renderer { func draw(into ctx: DrawingContext) }
struct SVGRenderer: Renderer { func draw(into ctx: DrawingContext) {} }
struct PDFRenderer: Renderer { func draw(into ctx: DrawingContext) {} }

struct DrawingContext {}

// `some`: one concrete type, static dispatch — preferred
func makeDefaultRenderer() -> some Renderer { SVGRenderer() }

// Generic parameter: caller picks the type, still specialized
func render<R: Renderer>(scene: Scene, using renderer: R) {
    let ctx = DrawingContext()
    renderer.draw(into: ctx)
}

// `any`: heterogeneous storage — the legitimate existential use case
struct Scene { var name = "" }
final class RendererRegistry {
    private var renderers: [any Renderer] = []      // mixed types, boxed
    func register(_ r: any Renderer) { renderers.append(r) }
    func renderAll(scene: Scene) {
        let ctx = DrawingContext()
        for r in renderers { r.draw(into: ctx) }    // dynamic dispatch per element
    }
}

let registry = RendererRegistry()
registry.register(SVGRenderer())
registry.register(PDFRenderer())
```

---

<a id="q35"></a>
### Q35: What are primary associated types, and how do they enable `some Sequence<Int>`-style constraints?

**Difficulty**: Advanced

**Strategy**:
A primary associated type (SE-0358) is declared in the protocol definition with angle brackets — `protocol Sequence<Element>` — naming one associated type that callers most often want to constrain. It lets you write `some AsyncSequence<Int>` or `any Publisher<Data, Never>` instead of full generic constraints (`<S: AsyncSequence> where S.Element == Int`), applying to opaque types, existentials, and extensions alike. The standard library adopted them for `Sequence`, `AsyncSequence`, `Publisher` (Combine), `StridedSequence`-style APIs, etc. They improve readability of API signatures without changing runtime behavior; the constraint is still checked at compile time.

**Code Example**:
```swift
import Combine

// PATs in a modern service layer signature
final class MetricsPipeline {
    // Without PATs: <S: AsyncSequence> where S.Element == Int
    func subscribe(to stream: some AsyncSequence<Int>) async rethrows -> Int {
        var total = 0
        for await value in stream { total += value }
        return total
    }

    // Existential with two primary associated types (Combine's Publisher has two)
    func tap(_ publisher: any Publisher<Data, Never>) -> AnyCancellable {
        publisher.sink { _ in }
    }
}

extension Sequence where Element == Double {         //PAT-style extension sugar
    func normalized() -> [Double] {
        guard let min = self.min(), let max = self.max(), min != max else { return Array(self) }
        return map { ($0 - min) / (max - min) }
    }
}

let readings = [18.0, 21.5, 30.0, 25.5]
print(readings.normalized())   // [0.0, 0.1935..., 1.0, 0.451...]
```

---

<a id="q36"></a>
### Q36: How do property wrappers work internally, and how do you write a correct one?

**Difficulty**: Expert

**Strategy**:
A property wrapper is a generic type with a `wrappedValue`; the compiler desugars `@Foo var x = v` into a stored `_x: Foo` plus a computed `x` that reads/writes `_x.wrappedValue`, and exposes `$x` from `projectedValue`. Advanced pieces: `init(wrappedValue:)` for assignment-site initialization; `static subscript(_encloseInstance:)` with `_read`/`_modify` coroutines lets the wrapper pull storage from the enclosing instance (how SwiftUI's `@State` binds to view storage outside the struct); and access-level translation (`@Published private(set)` keeps the setter internal to the wrapper). Restrictions: no inheritance, no lazy semantics beyond what you implement, and composition (`@A @B var x`) nests outer wrappers over inner `$` projections — worth knowing when debugging projections like `$$`.

**Code Example**:
```swift
@propertyWrapper
struct Clamped<Value: Comparable> {
    private var value: Value
    let range: ClosedRange<Value>
    init(wrappedValue: Value, _ range: ClosedRange<Value>) {
        self.range = range
        self.value = min(max(wrappedValue, range.lowerBound), range.upperBound)
    }
    var wrappedValue: Value {
        get { value }
        set { value = min(max(newValue, range.lowerBound), range.upperBound) }
    }
    var projectedValue: ClosedRange<Value> { range }   // $volume -> the constraint
}

struct SpeakerSettings {
    @Clamped(0...100) var volume: Int = 50
    @Clamped(20.0...40.0) var temperature: Double = 21
}

var settings = SpeakerSettings()
settings.volume = 180
print(settings.volume)        // 100
print(settings.$temperature)  // 20.0...40.0

// SwiftUI interop pattern: wrapper that projects a Binding
@propertyWrapper
struct PercentageLabel {
    @Binding var wrappedValue: Double           // wraps another wrapper (Binding)
    var projectedValue: String { "\(Int(wrappedValue * 100))%" }
    init(wrappedValue: Binding<Double>) { _wrappedValue = wrappedValue }
}
```

---

<a id="q37"></a>
### Q37: Explain value semantics and copy-on-write — how would you implement COW in your own type?

**Difficulty**: Intermediate

**Strategy**:
Value semantics mean assigning or passing a value gives an independent copy: mutations never leak to the original. `Array`, `String`, `Dictionary`, and `Set` implement this efficiently with copy-on-write: the value holds a reference to shared heap storage, and any mutation first checks `isKnownUniquelyReferenced(_:)` — if other copies share the storage, mutate through a fresh clone, otherwise mutate in place. Copies are therefore O(1) until the first write. To implement it yourself: box the buffer in a `final class`, keep it `private(var)`, and guard every mutating method with the uniqueness check. Pitfall: capturing a COW value in an escaping closure or storing it in a class property bumps the reference count — deep copies at the wrong moment show up as allocation spikes in Instruments.

**Code Example**:
```swift
struct Batch: ExpressibleByArrayLiteral {
    final class Storage {      // reference box shared between copies
        var items: [Int]
        init(_ items: [Int]) { self.items = items }
    }
    private var storage: Storage

    init(_ items: [Int]) { storage = Storage(items) }
    init(arrayLiteral elements: Int...) { storage = Storage(elements) }

    var items: [Int] { storage.items }

    mutating func append(_ value: Int) {
        copyIfNeeded()
        storage.items.append(value)
    }

    private mutating func copyIfNeeded() {
        if !isKnownUniquelyReferenced(&storage) {
            storage = Storage(storage.items)   // detach from other copies
        }
    }
}

var a: Batch = [1, 2, 3]
var b = a                 // O(1): shares storage
a.append(4)               // COW: `a` clones, `b` untouched
print(b.items)            // [1, 2, 3]
print(a.items)            // [1, 2, 3, 4]
```

---

<a id="q38"></a>
### Q38: Compare MVVM, TCA, and VIPER for SwiftUI apps — when would you choose each?

**Difficulty**: Advanced

**Strategy**:
MVVM in SwiftUI means `@Observable` models exposing state + async methods, bound with `@Bindable`/`@Environment` — minimal ceremony, but discipline is on you: state can scatter, navigation and side effects are ad hoc. TCA (The Composable Architecture) formalizes everything: a reducer `(State, Action) -> Effect`, unidirectional data flow, first-class dependency injection and effect cancellation, exhaustive testing of state transitions, and composable features — at the cost of boilerplate and a learning curve. VIPER (View-Interactor-Presenter-Entity-Router) maps well to UIKit delegation boundaries; in SwiftUI its layers collapse awkwardly and it's rarely the right new choice. Pick MVVM (with a router and DI) for small-to-medium apps; TCA when testability, deterministic state, and feature modularity at scale dominate.

**Code Example**:
```swift
// TCA-style feature: state transitions are pure functions — testable without mocks
import Foundation

struct CounterFeature {
    struct State: Equatable { var count = 0; var fact: String?; var loading = false }
    enum Action: Equatable { case incrementTapped, factResponse(String) }

    struct Environment {
        var fetchFact: @Sendable (Int) async throws -> String
    }

    static func reduce(_ state: inout State, _ action: Action, env: Environment) async {
        switch action {
        case .incrementTapped:
            state.count += 1
            state.loading = true
            if let fact = try? await env.fetchFact(state.count) {
                await MainActor.run {
                    state.fact = fact
                    state.loading = false
                }
            }
        case .factResponse(let fact):
            state.fact = fact
            state.loading = false
        }
    }
}

// Exhaustive unit test: no UI, no network — assert the pure transition
func testIncrement() async {
    var state = CounterFeature.State()
    await CounterFeature.reduce(&state, .factResponse("42 is the answer"),
                                env: .init(fetchFact: { _ in "42 is the answer" }))
    precondition(state.fact == "42 is the answer")
}
```

---

<a id="q39"></a>
### Q39: How do you do dependency injection in SwiftUI without singletons?

**Difficulty**: Intermediate

**Strategy**:
Use the environment as the composition root: create dependencies at the `App` scene, inject with `.environment(...)`, and read them in views via `@Environment(Service.self)` or `@Environment(\.featureFlags)` for value settings. This keeps views initializer-testable (pass mocks in previews via `.environment(MockService())`), respects sub-tree overrides (a sheet can swap in a preview/test context), and avoids global mutable state that Swift 6 strict concurrency would reject anyway. For non-UI layers, prefer explicit constructor injection in models (`init(client: APIClient)`) with protocols for seams; the environment then only feeds the root models. Previews and unit tests override at the edge instead of swizzling shared instances.

**Code Example**:
```swift
protocol APIClient: Sendable {
    func headlines() async throws -> [Headline]
}
struct Headline: Identifiable, Sendable { let id = UUID(); let title: String }

@Observable
final class NewsModel {
    private let client: any APIClient
    var headlines: [Headline] = []
    init(client: any APIClient) { self.client = client }

    func load() async { headlines = (try? await client.headlines()) ?? [] }
}

@main
struct NewsApp: App {
    var body: some Scene {
        WindowGroup { NewsView() }
            .environment(NewsModel(client: URLSessionAPIClient()))   // real graph
    }
}

struct NewsView: View {
    @Environment(NewsModel.self) private var model
    var body: some View {
        List(model.headlines) { Text($0.title) }
            .task { await model.load() }
    }
}

#Preview {
    NewsView()
        .environment(NewsModel(client: PreviewClient()))  // test/preview seam
}

struct PreviewClient: APIClient {
    func headlines() async throws -> [Headline] { [Headline(title: "Preview")] }
}
struct URLSessionAPIClient: APIClient {
    func headlines() async throws -> [Headline] { [] }
}
```

---

<a id="q40"></a>
### Q40: How does Swift Testing compare to XCTest, and how do you migrate?

**Difficulty**: Intermediate

**Strategy**:
Swift Testing (the `Testing` module, default for new Xcode 16+ targets) is designed for Swift concurrency: `@Test` functions and `@Suite` types, `#expect` / `#issueRecorded` macros with expressive failures, parameterized tests via `@Test(arguments:)`, traits for tags/limits (`.timeLimit`, `.disabled(if:)`), and parallel execution by default. XCTest remains required for UI tests, performance metrics (`measure`), and some integrations, but both frameworks run in the same test plan side by side — migration is incremental. Concurrency support is first-class: `async` tests await directly, unstructured child tasks are disallowed (a test waits for all its spawned tasks), and argument values are `Sendable`.

**Code Example**:
```swift
import Testing
import Foundation

struct SlugifyTests {
    @Test func basicSlug() {
        #expect(slugify("Hello, SwiftUI World!") == "hello-swiftui-world")
    }

    @Test(arguments: [
        ("Swift 6", "swift-6"),
        ("  spaced   out  ", "spaced-out"),
    ])
    func parameterized(input: String, expected: String) {
        #expect(slugify(input) == expected)
    }

    @Test(.tags(.networking), .timeLimit(.seconds(2)))
    func asyncAwaitIntegration() async throws {
        let result = try await EchoService.echo("ping")
        #expect(result == "ping")
    }

    @Test func recordsIssuesSoftly() {
        #expect(2 + 2 == 4)
        guard 3 * 3 == 9 else {
            Issue.record("multiplication broken")
            return
        }
    }
}

extension Tag {
    @Tag static var networking: Tag
}

func slugify(_ s: String) -> String {
    s.lowercased()
     .map { $0.isLetter || $0.isNumber ? $0 : " " }
     .split(separator: " ")
     .joined(separator: "-")
}
```

---

<a id="q41"></a>
### Q41: How do you write reliable async tests, including mocking actor dependencies?

**Difficulty**: Advanced

**Strategy**:
Make async tests deterministic by injecting dependencies that are controllable actors or value stubs, not real network/queues. With Swift Testing, an `async` test awaits your code directly; use `confirmation` to assert async events fired an exact number of times instead of sleeps. Mock actors serialize through the actor model (no races), can record calls for verification, and can expose programmable responses. Avoid `Task.sleep` synchronization — flaky under CI load; if timing matters, inject a `Clock` (e.g., a manual test clock advancing explicitly) so the test controls time. Finally, keep tests off the main actor unless they exercise `@MainActor` code, so parallel suites don't contend.

**Code Example**:
```swift
import Testing

protocol CartStore: Sendable {
    func items() async -> [String]
    func add(_ item: String) async
}

actor MockCartStore: CartStore {
    private(set) var added: [String] = []
    private var stubbed: [String] = []
    func items() async -> [String] { stubbed }
    func add(_ item: String) async { added.append(item) }
    func given(items: [String]) { stubbed = items }
}

@Observable
@MainActor
final class CartModel {
    private let store: any CartStore
    init(store: any CartStore) { self.store = store }

    func addAll(_ new: [String]) async {
        for item in new { await store.add(item) }
    }
}

@Test func addAllForwardsEachItem() async {
    let mock = MockCartStore()
    let model = await CartModel(store: mock)   // mock is Sendable: pass freely
    await model.addAll(["apple", "pear"])
    let added = await mock.added
    #expect(added == ["apple", "pear"])         // no sleeps, no races
}

@Test func eventFiresExactlyOnce() async {
    await confirmation("add logged", expectedCount: 1) { confirmed in
        let recorder = EventRecorder { _ in confirmed() }   // call on event
        await recorder.add("kiwi")
    }
}

struct EventRecorder: Sendable {
    let onAdd: @Sendable (String) -> Void
    func add(_ item: String) async { onAdd(item) }
}
```

---

<a id="q42"></a>
### Q42: Why does using `DispatchSemaphore.wait()` inside an `async` context deadlock, and what replaces it?

**Difficulty**: Expert

**Strategy**:
Swift Concurrency runs tasks on a small, fixed cooperative thread pool; a blocked thread can't run other work. `semaphore.wait()` parks its OS thread, and the `signal()` that would release it is scheduled as another job — which may itself need that same (now blocked) cooperative thread. With the pool exhausted, every pending job stalls and the app deadlocks; even before full deadlock it causes priority inversion and unbounded thread pileup (each blocked thread is holding a scarce resource). Replace the pattern with async-native tools: `AsyncStream`/continuations to await a signal, task-group-based async semaphores, or simply restructure so the resource is actor-isolated. If you must bridge blocking code, confine it to a dedicated `DispatchQueue` — never a cooperative thread.

**Code Example**:
```swift
// DEADLOCK: wait() blocks a cooperative thread; signal() may need that thread
func brokenFetch(url: URL) async -> Data {
    let semaphore = DispatchSemaphore(value: 0)
    var result = Data()
    URLSession.shared.dataTask(with: url) { data, _, _ in
        result = data ?? Data()
        semaphore.signal()              // queued as a job that can't run
    }.resume()
    semaphore.wait()                    // blocks the cooperative thread
    return result
}

// Correct: continuation — suspend the task, never block the thread
func fixedFetch(url: URL) async throws -> Data {
    let (data, _) = try await URLSession.shared.data(from: url)
    return data
}

// Correct: async semaphore via channel/actor when throttling is the goal
actor AsyncGate {
    private var permits: Int
    init(permits: Int) { self.permits = permits }
    private var waiters: [CheckedContinuation<Void, Never>] = []

    func acquire() async {
        if permits > 0 { permits -= 1; return }
        await withCheckedContinuation { waiters.append($0) }
    }
    func release() {
        if let next = waiters.first {
            waiters.removeFirst()
            next.resume()               // hand the permit directly over
        } else { permits += 1 }
    }
}
```

---

<a id="q43"></a>
### Q43: What is priority inversion in the context of Swift Concurrency and GCD, and how does the runtime mitigate it?

**Difficulty**: Advanced

**Strategy**:
Priority inversion happens when a high-priority task waits on a resource held by a low-priority task that isn't getting CPU time (classic case: low-QoS work holds a lock/queue that high-QoS work needs; worst case a medium task starves both). GCD queues are vulnerable: dispatching a high-QoS block behind low-QoS work on a serial queue can stall UI. Swift Concurrency mitigates it structurally: when a high-priority task awaits, the runtime escalates the priority of tasks it depends on (priority propagation through `async let`/task groups, and escalation across task dependencies), and actor executor jobs inherit escalated priorities so the blocking low-priority job gets boosted to unblock the waiter. Your job is to help it: run CPU work at honest priorities, don't block on semaphores/mutexes across await boundaries, and prefer actors over shared serial queues.

**Code Example**:
```swift
final class ClassicInversion {
    private let queue = DispatchQueue(label: "catalog")   // serial queue, no QoS
    private var cache: [String: Data] = [:]

    func prime() {
        // Low-QoS work enqueued first holds the queue…
        queue.async(qos: .utility) {
            for i in 0..<5_000_000 { _ = i * i }          // long-running
        }
    }

    func cached(_ key: String) -> Data? {
        // …so this userInitiated read waits behind it: inversion on main thread
        queue.sync(qos: .userInitiated) { cache[key] }
    }
}

// Structured version: the runtime escalates the worker when UI awaits it
actor Catalog {
    private var cache: [String: Data] = [:]

    nonisolated func warm() async {
        let keys = await allKeys()
        await heavyWarm(keys: keys)        // utility-class bulk work
    }

    func cached(_ key: String) -> Data? { cache[key] }

    private func allKeys() async -> [String] { ["a", "b"] }
    private func heavyWarm(keys: [String]) async {
        for k in keys { cache[k] = Data() }
    }
}

@MainActor
func loadIcon(catalog: Catalog, key: String) async -> Data? {
    // If this UI task awaits the actor, Swift escalates the actor job's
    // priority so blocking work is boosted — instead of inverting.
    await catalog.cached(key)
}
```

---

<a id="q44"></a>
### Q44: How do you build a retrying URLSession client with async/await?

**Difficulty**: Intermediate

**Strategy**:
Wrap `URLSession.data(for:)` in a loop with capped exponential backoff, honoring cancellation at every step: check `Task.checkCancellation()` between attempts, only retry transient failures (network errors, timeouts, 5xx, 429), and respect `Retry-After` when the server sends it. `Task.sleep(for:)` throws `CancellationError` on cancel so a cancelled retry chain exits cleanly. Include jitter to avoid synchronized retry storms, classify errors into a small enum, and make the retry policy injectable so tests run without real waits.

**Code Example**:
```swift
struct HTTPClient {
    enum Failure: Error { case transport(Error), status(Int), cancelled }

    struct Policy: Sendable {
        var maxAttempts = 3
        var baseDelay: Duration = .milliseconds(300)
        var maxDelay: Duration = .seconds(4)
    }

    private let session: URLSession
    private let policy: Policy
    init(session: URLSession = .shared, policy: Policy = Policy()) {
        self.session = session
        self.policy = policy
    }

    func data(for request: URLRequest) async throws -> Data {
        var attempt = 0
        while true {
            try Task.checkCancellation()
            do {
                let (data, response) = try await session.data(for: request)
                guard let http = response as? HTTPURLResponse else { return data }
                switch http.statusCode {
                case 200..<300: return data
                case 500, 502, 503, 504, 429:
                    attempt += 1
                    guard attempt < policy.maxAttempts else { throw Failure.status(http.statusCode) }
                    try await backoff(attempt: attempt, retryAfter: http.value(forHTTPHeaderField: "Retry-After"))
                default:
                    throw Failure.status(http.statusCode)
                }
            } catch let error as URLError where [.timedOut, .networkConnectionLost].contains(error.code) {
                attempt += 1
                guard attempt < policy.maxAttempts else { throw Failure.transport(error) }
                try await backoff(attempt: attempt, retryAfter: nil)
            }
        }
    }

    private func backoff(attempt: Int, retryAfter: String?) async throws {
        let capped = min(policy.baseDelay * (1 << attempt), policy.maxDelay)
        let jitter = Double.random(in: 0.5...1.0)
        let delay = retryAfter.flatMap { TimeInterval($0) }.map { Duration.seconds($0) }
                     ?? capped * jitter
        try await Task.sleep(for: delay)   // throws CancellationError when cancelled
    }
}
```

---

<a id="q45"></a>
### Q45: How does Core Data concurrency work, and what are the rules for `viewContext`, background contexts, and sharing objects?

**Difficulty**: Advanced

**Strategy**:
`NSManagedObject`s are not thread-safe: each is bound to a context, and a context to a queue. The rules: only touch a managed object on its context's queue (`perform`/`await perform` for background, main queue for `viewContext`); pass objects between contexts via `NSManagedObjectID` (thread-safe) and re-fetch with `object(with:)` on the receiving side; observe background saves into `viewContext` via `.automaticallyMergesChangesFromParent = true` (usually paired with a merge policy). `NSPersistentContainer` gives you `viewContext` (main) and `newBackgroundContext()`/`performBackgroundTask(_:)` for heavy work; since iOS 15 `perform` is async/await native. Data races here won't be caught by Swift 6 automatically (Core Data is ObjC underneath) — discipline and crashes (`NSInternalInconsistencyException`) enforce it.

**Code Example**:
```swift
import CoreData

final class PersistenceController {
    static let shared = PersistenceController()
    let container: NSPersistentContainer

    init(inMemory: Bool = false) {
        container = NSPersistentContainer(name: "Journal")
        if inMemory {
            container.persistentStoreDescriptions.first?.url = URL(fileURLWithPath: "/dev/null")
        }
        container.loadPersistentStores { _, error in
            if let error { fatalError("store load failed: \(error)") }
        }
        container.viewContext.automaticallyMergesChangesFromParent = true
        container.viewContext.mergePolicy = NSMergeByPropertyObjectTrumpMergePolicy
    }

    // iOS 15+: async perform — structured, cancellable with the surrounding task
    func importEntries(_ payloads: [EntryPayload]) async throws {
        let context = container.newBackgroundContext()
        try await context.perform {
            for payload in payloads {
                let entry = Entry(context: context)      // created on its own queue
                entry.id = payload.id
                entry.body = payload.body
                entry.createdAt = payload.date
            }
            try context.save()                            // merges into viewContext
        }
    }

    // Crossing threads: pass ObjectID, never the instance
    func entryID(named name: String) async throws -> NSManagedObjectID {
        let context = container.newBackgroundContext()
        return try await context.perform {
            let request = NSFetchRequest<Entry>(entityName: "Entry")
            request.predicate = NSPredicate(format: "body CONTAINS %@", name)
            request.fetchLimit = 1
            return try context.fetch(request).first!.objectID
        }
    }
}
```

---

<a id="q46"></a>
### Q46: How do you schedule background work with BGTaskScheduler, including the iOS 18 push-to-start model?

**Difficulty**: Intermediate

**Strategy**:
BGTaskScheduler runs `BGAppRefreshTask` (short refreshes, ~30s budget) and `BGProcessingTask` (minutes, e.g. ML training or CDN sync) when the system decides — influenced by usage patterns, battery, and `earliestBeginDate`; you cannot force execution, only submit requests and handle `expirationHandler` promptly. Register task identifiers in `Info.plist` (`BGTaskSchedulerPermittedIdentifiers`) and in the launch handler *before* the app finishes launching. iOS 18's push-to-start lets a task request begin in response to a silent push — register the same task identifier for push-triggered launches, so a server can kick off a refresh without launching the UI; the task then runs under the same budget/expiration rules. Submit a fresh request at the end of each run to keep the cadence going.

**Code Example**:
```swift
import BackgroundTasks
import UIKit

final class BackgroundScheduler {
    static let refreshID = "com.example.app.refresh"
    static let syncID = "com.example.app.datasync"

    func register() {
        BGTaskScheduler.shared.register(forTaskWithIdentifier: Self.refreshID, using: nil) { task in
            self.handleRefresh(task: task as! BGAppRefreshTask)
        }
        BGTaskScheduler.shared.register(forTaskWithIdentifier: Self.syncID, using: nil) { task in
            self.handleSync(task: task as! BGProcessingTask)
        }
    }

    func scheduleRefresh() {
        let request = BGAppRefreshTaskRequest(identifier: Self.refreshID)
        request.earliestBeginDate = Date(timeIntervalSinceNow: 15 * 60)
        submit(request)
    }

    func scheduleSync() {
        let request = BGProcessingTaskRequest(identifier: Self.syncID)
        request.requiresNetworkConnectivity = true   // request-level constraints
        request.requiresExternalPower = true
        request.earliestBeginDate = Date(timeIntervalSinceNow: 6 * 3600)
        submit(request)
    }

    private func submit(_ request: BGTaskRequest) {
        do {
            try BGTaskScheduler.shared.submit(request)
        } catch {
            // Code 1 (unavailable) in simulator: expected — device only.
            print("BGTaskScheduler submit failed: \(error)")
        }
    }

    private func handleRefresh(task: BGAppRefreshTask) {
        scheduleRefresh()                              // keep the pipeline alive
        let work = Task {
            await FeedRefresher.shared.refresh()
            task.setTaskCompleted(success: true)
        }
        task.expirationHandler = { work.cancel() }     // ~30s budget: stop fast
    }

    private func handleSync(task: BGProcessingTask) {
        let work = Task { await CloudSync.run() }
        task.expirationHandler = { work.cancel() }
    }
}

actor FeedRefresher {
    static let shared = FeedRefresher()
    func refresh() async { /* fetch + SwiftData/Core Data save */ }
}
actor CloudSync {
    static func run() async { /* long batch sync */ }
}
```

---

<a id="q47"></a>
### Q47: How do you use `ScenePhase` to manage app lifecycle in SwiftUI?

**Difficulty**: Beginner

**Strategy**:
`scenePhase` is an environment value exposing the scene's lifecycle: `.active` (foreground, receiving events), `.inactive` (foreground but interrupted — notification center, app switcher, during transitions), `.background` (no UI visible, may be suspended at any moment). React with `.onChange(of: scenePhase)` to start/pause work: commit drafts and flush saves on `.inactive` (last guaranteed execution point), stop timers/cameras on `.background`, resume and refresh UI on `.active`. For multi-scene apps (iPad, visionOS) each scene observes its own phase; app-wide "will terminate" still doesn't exist — persist continuously instead.

**Code Example**:
```swift
import SwiftUI

struct WorkoutView: View {
    @Environment(\.scenePhase) private var scenePhase
    @State private var timer: Timer?
    @State private var seconds = 0

    var body: some View {
        VStack {
            Text(seconds.formatted(.number.grouping(.never)))
                .font(.system(size: 64, weight: .bold, design: .rounded))
            Text("seconds").foregroundStyle(.secondary)
        }
        .onChange(of: scenePhase) { _, phase in
            switch phase {
            case .active:
                startTimer()
            case .inactive:
                Persistence.save(seconds)     // last guaranteed CPU window
            case .background:
                stopTimer()                  // release resources now
            @unknown default:
                break
            }
        }
        .onAppear { seconds = Persistence.load() }
    }

    private func startTimer() {
        guard timer == nil else { return }
        timer = Timer.scheduledTimer(withTimeInterval: 1, repeats: true) { _ in
            seconds += 1
        }
    }
    private func stopTimer() { timer?.invalidate(); timer = nil }
}

enum Persistence {
    static func save(_ value: Int) { UserDefaults.standard.set(value, forKey: "seconds") }
    static func load() -> Int { UserDefaults.standard.integer(forKey: "seconds") }
}
```

---

<a id="q48"></a>
### Q48: How does a WidgetKit widget deliver UI, and how do you keep its timeline fresh?

**Difficulty**: Intermediate

**Strategy**:
A widget extension supplies snapshots via a `TimelineProvider`: `placeholder` (generic template), `getSnapshot` (immediate concrete entry for the gallery), and `getTimeline` (array of `TimelineEntry`s plus a refresh policy — `.after(date)`/`.never`). The system, not the app, controls refresh frequency — a few dozen times a day typical — so encode future entries (e.g., one per hour of forecast) instead of relying on frequent reloads. Use `AppIntent`-based configurations for user-editable widgets (iOS 17 `WidgetConfigurationIntent`) and deep-link via `widgetURL` or `Link`. Since iOS 17, wrap content in `containerBackground(for: .widget)`; interactive widgets use `Button`/`Toggle` backed by App Intents. Push widget updates from the server with silent pushes to `widgetCenter`.

**Code Example**:
```swift
import WidgetKit
import SwiftUI

struct StreakEntry: TimelineEntry {
    let date: Date
    let streak: Int
    let goal: Int
}

struct StreakProvider: AppIntentTimelineProvider {
    func placeholder(in context: Context) -> StreakEntry {
        StreakEntry(date: .now, streak: 7, goal: 10)
    }

    func snapshot(for configuration: StreakGoalIntent, in context: Context) async -> StreakEntry {
        StreakEntry(date: .now, streak: await Store.currentStreak(), goal: configuration.goal)
    }

    func timeline(for configuration: StreakGoalIntent, in context: Context) async -> Timeline<StreakEntry> {
        let streak = await Store.currentStreak()
        // Entries every 2h while the day progresses; ask for reload after.
        let entries = (0..<6).map { offset in
            StreakEntry(date: Calendar.current.date(byAdding: .hour, value: offset * 2, to: .now)!,
                        streak: streak, goal: configuration.goal)
        }
        return Timeline(entries: entries, policy: .after(entries.last!.date.addingTimeInterval(2 * 3600)))
    }
}

struct StreakWidget: Widget {
    var body: some WidgetConfiguration {
        AppIntentConfiguration(kind: "StreakWidget", intent: StreakGoalIntent.self, provider: StreakProvider()) { entry in
            StreakView(entry: entry)
                .containerBackground(for: .widget) { Color.indigo.gradient }
        }
        .configurationDisplayName("Daily Streak")
        .supportedFamilies([.systemSmall, .systemMedium])
    }
}

struct StreakGoalIntent: WidgetConfigurationIntent {
    static var title: LocalizedStringResource = "Streak Goal"
    @Parameter(title: "Goal", default: 10) var goal: Int
}

enum Store {
    static func currentStreak() async -> Int { 7 }
}
```

---

<a id="q49"></a>
### Q49: How do App Intents work, and how have they absorbed Siri, Shortcuts, and Apple Intelligence surfaces?

**Difficulty**: Advanced

**Strategy**:
An `AppIntent` declares a typed action: `@Parameter`s (with requestable disambiguation via `@RequestableItem` in 2025-era SDKs), an async `perform()` returning `ProvidesDialog`/`ShowsSnippetView`/entity results, and optional `Dependency` injection for testability. Surfaces reuse the same intents: Shortcuts editor (via `AppShortcut`), Siri, Action button, Control Center widgets, Spotlight, and — since iOS 18 — Apple Intelligence and visual intelligence can compose your intents into on-screen actions via `AppEntity`/`EntityProperty` semantics when you declare them accurately (`isEligibleForPrediction`, `openAppWhenRun` for UI-requiring intents). Because intents are values with typed parameters, they double as your app's deep-link and automation layer; the entity query (`EntityQuery`) supplies dynamic parameters with suggestions.

**Code Example**:
```swift
import AppIntents
import SwiftUI

struct TimerEntity: AppEntity {
    static var typeDisplayRepresentation: Representation = "Timer"
    static var defaultQuery = TimerQuery()

    let id: UUID
    var displayRepresentation: Representation { "Timer \(id.uuidString.prefix(4))" }
}

struct TimerQuery: EntityQuery {
    func entities(for identifiers: [UUID]) async throws -> [TimerEntity] {
        identifiers.map { TimerEntity(id: $0) }
    }
    func suggestedEntities() async throws -> [TimerEntity] {
        TimerStore.active().map { TimerEntity(id: $0) }
    }
}

enum TimerStore {
    static func active() -> [UUID] { [UUID()] }
}

struct LogWorkoutIntent: AppIntent {
    static var title: LocalizedStringResource = "Log Workout"
    static var description = IntentDescription("Add a completed session to your journal.")
    static var openAppWhenRun = false

    @Parameter(title: "Duration", default: 30)
    var duration: Int

    private let store = WorkoutStore()   // injectable seam for tests

    @MainActor
    func perform() async throws -> some ProvidesDialog & ReturnsValue<Int> {
        let total = try await store.log(minutes: duration)
        return .result(value: total, dialog: "Logged \(duration) minutes. \(total) total.")
    }
}

struct WorkoutStore: Sendable {
    func log(minutes: Int) async throws -> Int { minutes * 1 }
}

struct WorkoutShortcuts: AppShortcutsProvider {
    static var appShortcuts: [AppShortcut] {
        AppShortcut(intent: LogWorkoutIntent(),
                    phrases: ["Log a workout in \(.applicationName)"],
                    shortTitle: "Log Workout",
                    systemImageName: "figure.run")
    }
}
```

---

<a id="q50"></a>
### Q50: How do you make a SwiftUI view accessible for VoiceOver users?

**Difficulty**: Beginner

**Strategy**:
Start by auditing with Accessibility Inspector and VoiceOver itself. Core tools: `accessibilityLabel` (name), `accessibilityValue` (state), `accessibilityHint` (usage), `accessibilityAddTraits` (button/selected/image); group related content with `accessibilityElement(children: .combine)` so one swipe reads a coherent unit; hide decorative pieces with `accessibilityHidden(true)`; expose custom gestures as `accessibilityActions`. Native controls get most of this free — prefer `Button("Save")` over an image with a tap gesture so traits and activation come automatically. Order matters: VoiceOver traverses reading order, roughly visual/logical order — verify and reorder with `accessibilitySortPriority` when needed.

**Code Example**:
```swift
struct TrackRow: View {
    let track: Track
    @State private var isDownloading = false

    var body: some View {
        HStack(spacing: 12) {
            AsyncImage(url: track.artwork) { $0.resizable().scaledToFill() }
                placeholder: { Color.quaternary }
                .frame(width: 48, height: 48).clipShape(.circle)
                .accessibilityHidden(true)                       // decorative

            VStack(alignment: .leading, spacing: 2) {
                Text(track.title).font(.headline)
                Text(track.artist).font(.subheadline).foregroundStyle(.secondary)
            }

            Button {
                isDownloading.toggle()
            } label: {
                Image(systemName: isDownloading ? "stop.circle.fill" : "arrow.down.circle")
            }
            .buttonStyle(.borderless)
            .accessibilityLabel(isDownloading ? "Stop download" : "Download")
        }
        .accessibilityElement(children: .combine)               // one focus target
        .accessibilityLabel("\(track.title), by \(track.artist)")
        .accessibilityHint("Double tap to play. Actions available.")
    }
}

struct Track { let title: String; let artist: String; let artwork: URL? }
```

---

<a id="q51"></a>
### Q51: How does Dynamic Type work, and how do you build layouts that scale with the user's text size?

**Difficulty**: Beginner

**Strategy**:
Dynamic Type scales all text styles (`.body`, `.headline`, …) from the user's Accessibility setting; using semantic styles instead of fixed `.system(size:)` makes scaling automatic. Support it structurally: layouts must reflow — stacks wrap with ViewThatFits or custom layouts, `lineLimit` loosens, toolbars move, and `@ScaledMetric` scales non-text metrics (icons, padding, hit targets) in proportion. Test at all sizes (Xcode environment overrides, or `.dynamicTypeSize(.xxxLarge)`/`.accessibility5` in previews) and cap where genuinely necessary with `.dynamicTypeSize(...DynamicTypeSize.accessibility3)`. Never scale text manually from `UIFontMetrics` in SwiftUI — prefer the system's own mechanism.

**Code Example**:
```swift
struct StatCard: View {
    let title: String
    let value: String

    @ScaledMetric(relativeTo: .title2) private var iconSize: CGFloat = 28
    @ScaledMetric(relativeTo: .body) private var spacing: CGFloat = 12

    var body: some View {
        ViewThatFits(in: .horizontal) {
            HStack(spacing: spacing) { content }   // preferred: icon + text
            VStack(alignment: .leading, spacing: spacing) { content }  // wraps at huge sizes
        }
        .padding()
        .background(.fill.quaternary, in: .rect(cornerRadius: 14))
    }

    @ViewBuilder private var content: some View {
        Label {
            VStack(alignment: .leading, spacing: 2) {
                Text(title).font(.subheadline).foregroundStyle(.secondary)
                Text(value).font(.title2.bold()).contentTransition(.numericText())
            }
        } icon: {
            Image(systemName: "chart.line.uptrend.xyaxis")
                .font(.system(size: iconSize, weight: .semibold))
                .foregroundStyle(.tint)
        }
    }
}

#Preview("AX5") {
    StatCard(title: "Steps", value: "12,480")
        .dynamicTypeSize(.accessibility5)
        .padding()
}
```

---

<a id="q52"></a>
### Q52: How does `matchedGeometryEffect` work and what are its failure modes?

**Difficulty**: Intermediate

**Strategy**:
`matchedGeometryEffect(id:in:)` animates two views into the same shape/position across a layout change: both views register geometry under an id in a shared `@Namespace`, and when identity moves from one branch to the other (typically an `if/else` toggle), the system interpolates frame, corner radius, and scale between the outgoing and incoming views. Failure modes: both views present simultaneously with the same id (undefined behavior/jump), matching views inside lazy containers (unrealized views have no geometry — the match breaks), and expecting matched geometry to animate *content* rather than the container. Use it for hero transitions, expanding cards, segmented morphing; use `navigationTransition(.zoom)` (iOS 18) for the similar push-style zoom.

**Code Example**:
```swift
struct GalleryView: View {
    @Namespace private var heroNS
    @State private var selected: Photo? = nil
    let photos = Photo.samples

    var body: some View {
        ZStack {
            ScrollView {
                LazyVGrid(columns: [GridItem(.adaptive(minimum: 110), spacing: 10)]) {
                    ForEach(photos) { photo in
                        // lazy container: match only realized items
                        if selected?.id != photo.id {
                            thumb(photo)
                        }
                    }
                }
                .padding()
            }

            if let selected {
                fullScreen(selected)
            }
        }
    }

    private func thumb(_ photo: Photo) -> some View {
        PhotoCell(photo: photo)
            .matchedGeometryEffect(id: photo.id, in: heroNS)     // source geometry
            .onTapGesture { withAnimation(.spring(duration: 0.35)) { selected = photo } }
    }

    private func fullScreen(_ photo: Photo) -> some View {
        PhotoCell(photo: photo, large: true)
            .matchedGeometryEffect(id: photo.id, in: heroNS)     // destination geometry
            .onTapGesture { withAnimation(.spring(duration: 0.35)) { selected = nil } }
    }
}

struct Photo: Identifiable { let id = UUID(); var name = "photo"; static var samples: [Photo] { (0..<9).map { _ in Photo() } } }
struct PhotoCell: View {
    let photo: Photo; var large = false
    var body: some View { Image(systemName: "photo").font(.system(size: large ? 120 : 40)).frame(maxWidth: .infinity).aspectRatio(1, contentMode: .fit).background(.thinMaterial) }
}
```

---

<a id="q53"></a>
### Q53: When do you reach for `keyframeAnimator` or `phaseAnimator` instead of `withAnimation`?

**Difficulty**: Advanced

**Strategy**:
`withAnimation` interpolates a single change between old and new values — great for state transitions, useless for choreographed multi-stage motion. `keyframeAnimator(initialValue:repeating:content:keyframes:)` (iOS 17) drives a value through a timeline of `KeyframeTrack`s with per-property timing (spring for position, cubic for opacity), letting one animation mix curves — e.g., a badge that pops, overshoots, and settles with independent opacity/rotation tracks. `phaseAnimator(phases:content:animation:)` cycles discrete phases (`.hidden → .peeking → .full`) with a different animation per phase transition — perfect for looping attention effects and state machines that pulse. Both are view modifiers driven by SwiftUI's timeline (they pause offscreen and respect `transaction` disabling), making them safer than manual `TimelineView` math.

**Code Example**:
```swift
struct DeliveryBadge: View {
    var body: some View {
        Image(systemName: "shippingbox.fill")
            .font(.system(size: 44))
            .foregroundStyle(.white)
            .padding(18)
            .background(.green.gradient, in: .circle())
            .keyframeAnimator(initialValue: AnimationState(), repeating: true) { label, state in
                label
                    .scaleEffect(state.scale)
                    .rotationEffect(.degrees(state.tilt))
                    .offset(y: state.lift)
            } keyframes: { _ in
                KeyframeTrack(\.scale) {
                    SpringKeyframe(duration: 0.35, bounce: 0.5)
                    CubicKeyframe(duration: 0.2, value: 1.0)
                }
                KeyframeTrack(\.tilt) {
                    CubicKeyframe(duration: 0.3, value: -12)
                    CubicKeyframe(duration: 0.3, value: 12)
                    CubicKeyframe(duration: 0.2, value: 0)
                }
                KeyframeTrack(\.lift) {
                    CubicKeyframe(duration: 0.35, value: -24)
                    CubicKeyframe(duration: 0.4, value: 0)
                }
            }
    }
}

struct AnimationState {
    var scale = 1.0
    var tilt = 0.0
    var lift = 0.0
}

// phaseAnimator: discrete stages, one animation per transition
struct NudgeDot: View {
    var body: some View {
        Circle().fill(.red).frame(width: 12, height: 12)
            .phaseAnimator([0.0, -8.0, 0.0]) { dot, y in dot.offset(y: y) } phase: { _ in } animation: { phase in
                phase == -8.0 ? .bouncy(duration: 0.18) : .easeOut(duration: 0.22)
            }
    }
}
```

---

<a id="q54"></a>
### Q54: How do you wrap a UIKit view with `UIViewRepresentable` correctly, including updates and sizing?

**Difficulty**: Intermediate

**Strategy**:
`UIViewRepresentable` bridges UIKit into SwiftUI: `makeUIView` builds and configures the view once, `updateUIView` re-syncs SwiftUI state into the view on every re-render (cheap guard clauses avoid redundant work), and a `Coordinator` owns delegates/targets that outlive both calls and pushes events back into SwiftUI. Sizing: SwiftUI proposes a size; if the view self-sizes via `intrinsicContentSize`, return it from `sizeThatFits(_:uiView:context:)` (iOS 16+) so stacks can lay it out correctly. Common pitfalls: creating views/observers in `updateUIView` (duplicates), forgetting `dismantleUIView` for cleanup, and strong delegate cycles — the coordinator should hold targets weakly where UIKit keeps references.

**Code Example**:
```swift
import SwiftUI
import UIKit

struct WrapActivityIndicatorView: UIViewRepresentable {
    var isRunning: Bool
    var style: UIActivityIndicatorView.Style

    func makeUIView(context: Context) -> UIActivityIndicatorView {
        let view = UIActivityIndicatorView(style: style)
        view.hidesWhenStopped = true
        return view
    }

    func updateUIView(_ view: UIActivityIndicatorView, context: Context) {
        guard view.isAnimating != isRunning else { return }   // idempotent sync
        isRunning ? view.startAnimating() : view.stopAnimating()
    }

    static func dismantleUIView(_ view: UIActivityIndicatorView, coordinator: ()) {
        view.stopAnimating()
    }
}

// Full pattern: delegate bridging + auto-sizing
struct RichEditorView: UIViewRepresentable {
    @Binding var html: String
    var onCaretChange: ((Int) -> Void)? = nil

    func makeUIView(context: Context) -> UITextView {
        let tv = UITextView()
        tv.delegate = context.coordinator
        tv.isScrollEnabled = false
        tv.font = .preferredFont(forTextStyle: .body)
        return tv
    }

    func updateUIView(_ tv: UITextView, context: Context) {
        if tv.text != html { tv.text = html }                  // programmatic set only
    }

    func sizeThatFits(_ proposal: ProposedViewSize, uiView: UITextView, context: Context) -> CGSize? {
        let width = proposal.width ?? uiView.bounds.width
        let size = uiView.sizeThatFits(CGSize(width: width, height: .greatestFiniteMagnitude))
        return CGSize(width: width, height: size.height)       // grow with content
    }

    func makeCoordinator() -> Coordinator { Coordinator(self) }

    final class Coordinator: NSObject, UITextViewDelegate {
        var parent: RichEditorView
        init(_ parent: RichEditorView) { self.parent = parent }

        func textViewDidChange(_ tv: UITextView) {
            parent.html = tv.text                              // push into SwiftUI
        }
        func textViewDidChangeSelection(_ tv: UITextView) {
            parent.onCaretChange?(tv.selectedRange.location)
        }
    }
}
```

---

<a id="q55"></a>
### Q55: How do you embed SwiftUI inside a UIKit app with `UIHostingController`?

**Difficulty**: Intermediate

**Strategy**:
`UIHostingController(rootView:)` is the container that renders a SwiftUI hierarchy inside UIKit windows, navigation, and tab flows — the standard migration path (screens migrate inside-out, feature by feature). Sizing matters: by default the host sizes itself to its SwiftUI content; when embedding in auto layout, use `sizingOptions = []` (iOS 16+) to let constraints drive size instead of content hugging, and set `intrinsicContentSize`-friendly constraints. Communication flows through plain Swift (bindings, delegates, closures on the root view's model) since environment injection from UIKit requires care: use `.environment(...)` on the root view itself. Keep UIKit responsible for navigation until the root migrates to `NavigationStack` — mixing `UINavigationController` pushes with SwiftUI navigation in the same flow creates double navigation bars.

**Code Example**:
```swift
import UIKit
import SwiftUI

final class OnboardingCoordinator: NSObject {
    private let nav: UINavigationController
    private var model = OnboardingModel()

    init(nav: UINavigationController) { self.nav = nav }

    func start() {
        let welcome = WelcomeViewController()
        welcome.delegate = self
        nav.setViewControllers([welcome], animated: false)
    }

    private func showSwiftUIStep() {
        let step = OnboardingStepView(model: model) { [nav] in
            nav?.dismiss(animated: true)                       // SwiftUI -> UIKit event
        }
        let host = UIHostingController(rootView: step)
        host.sizingOptions = []                                // constraint-driven size
        host.modalPresentationStyle = .pageSheet               // enable sheet presentation
        host.sheetPresentationController?.detents = [.medium(), .large()]
        nav.present(host, animated: true)
    }
}

extension OnboardingCoordinator: WelcomeViewControllerDelegate {
    func didTapContinue() { showSwiftUIStep() }
}

@Observable
final class OnboardingModel {
    var name = ""
    var notificationsEnabled = true
}

struct OnboardingStepView: View {
    @Bindable var model: OnboardingModel
    var finish: () -> Void

    var body: some View {
        Form {
            TextField("Your name", text: $model.name)
            Toggle("Enable notifications", isOn: $model.notificationsEnabled)
            Button("Finish", action: finish)
        }
    }
}

protocol WelcomeViewControllerDelegate: AnyObject { func didTapContinue() }
final class WelcomeViewController: UIViewController {
    weak var delegate: WelcomeViewControllerDelegate?
    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .systemBackground
        let button = UIButton(type: .system, primaryAction: UIAction { [delegate] _ in
            delegate?.didTapContinue()
        })
        button.setTitle("Continue", for: .normal)
        button.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(button)
        NSLayoutConstraint.activate([
            button.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            button.centerYAnchor.constraint(equalTo: view.centerYAnchor)
        ])
    }
}
```

---

<a id="q56"></a>
### Q56: How does Swift interoperate with the Objective-C runtime, and what should you know about swizzling and dynamic dispatch?

**Difficulty**: Expert

**Strategy**:
`@objc`-exposed Swift classes descend from NSObject and are registered with the ObjC runtime: method calls go through `objc_msgSend` against class method lists, KVC/KVO work where properties are `@objc dynamic`, and selectors (`#selector`) bridge. Swift-native code avoids the runtime: methods are statically or vtable-dispatched unless marked `dynamic`, which forces ObjC message sending — the escape hatch when you need runtime-selected or swizzled behavior. Method swizzling (`method_exchangeImplementations`) swaps implementations in a class's dispatch table at load time; it's still used for analytics/monitoring (e.g., tracking `UIViewController` lifecycle), but it's fragile: execution order with other swizzles, category collisions, Swift code not marked `dynamic` bypassing it entirely, and it breaks under strict concurrency unless done once on the main actor at launch. Prefer composition/injection; treat swizzling as a last-resort tool with tests pinning behavior.

**Code Example**:
```swift
import ObjectiveC
import UIKit

final class AnalyticsSwizzler {
    static let shared = AnalyticsSwizzler()

    @MainActor
    func install() {
        DispatchQueue.main.async {                            // exactly once, on main
            Self.exchange(
                #selector(UIViewController.viewDidAppear(_:)),
                #selector(UIViewController.tracked_viewDidAppear(_:)),
                on: UIViewController.self
            )
        }
    }

    private static func exchange(_ original: Selector, with swizzled: Selector, on cls: AnyClass) {
        guard let originalMethod = class_getInstanceMethod(cls, original),
              let swizzledMethod = class_getInstanceMethod(cls, swizzled) else { return }
        method_exchangeImplementations(originalMethod, swizzledMethod)
    }
}

private extension UIViewController {                         // hidden namespace
    @objc func tracked_viewDidAppear(_ animated: Bool) {
        tracked_viewDidAppear(animated)                       // calls the original now
        Analytics.log(String(describing: type(of: self)))     // typed, no stringly API
    }
}

enum Analytics {
    static func log(_ screen: String) { print("screen:", screen) }
}

// force ObjC dispatch where interception must hold:
class RemoteCommand: NSObject {
    @objc dynamic func execute() { print("base") }            // runtime-dispatchable
}

class PauseCommand: RemoteCommand {
    override func execute() { print("pause") }                // ObjC override works
}
```

---

<a id="q57"></a>
### Q57: GCD vs actors — what do you give up and gain when moving serial queues to actors?

**Difficulty**: Advanced

**Strategy**:
A serial `DispatchQueue` serializes blocks but the compiler doesn't know: nothing prevents you from touching the protected state from another queue, capturing it in a `@Sendable` closure, or deadlocking with `sync` from the wrong thread — races surface at runtime. An actor makes the invariant compiler-checked: only isolated code can touch its mutable state, callers must `await` (no blocking `sync`), and priority escalation and cancellation integrate with Swift Concurrency. You gain data-race safety, structured cancellation, and Swift 6 compliance; you give up blocking waits (impossible by design), ordering guarantees with external queues, and fine QoS control over each item. Migrate queue-protected types by making the class an `actor`, converting `perform` to `func`, and for anything that must remain synchronous, keep a small `nonisolated` surface of pure computations.

**Code Example**:
```swift
// Before: serial queue protects state — by convention only
final class TokenStoreQueue {
    private let queue = DispatchQueue(label: "tokens")
    private var tokens: [String: Date] = [:]

    func refresh(_ key: String) {
        queue.sync { tokens[key] = Date() }              // can deadlock if re-entered
    }
    func valid(_ key: String) -> Bool {
        queue.sync {
            guard let until = tokens[key] else { return false }
            return until > Date()
        }
    }
}

// After: actor — enforced by the compiler, awaitable, non-blocking
actor TokenStore {
    private var tokens: [String: Date] = [:]

    func refresh(_ key: String) {
        tokens[key] = Date()
    }
    func valid(_ key: String) -> Bool {
        guard let until = tokens[key] else { return false }
        return until > Date()
    }
    func purgeExpired(now: Date = .now) {
        tokens = tokens.filter { $0.value > now }        // atomic: no awaits inside
    }
}

@MainActor
func boot(store: TokenStore) async {
    await store.refresh("session")
    if await store.valid("session") {
        print("session live")                            // no thread blocking anywhere
    }
}
```

---

<a id="q58"></a>
### Q58: How do you use Instruments' Leaks and Time Profiler to diagnose memory and CPU issues?

**Difficulty**: Intermediate

**Strategy**:
Run Leaks (or the Leaks template) on a realistic session: it scans the heap for reference clusters unreachable from roots — the classic Swift case is closures strongly capturing `self` (timers, NotificationCenter, delegates) and `NotificationCenter` blocks retaining observers. Leaks flags `malloc` blocks by history; pair with Allocations' generation snapshots (mark generation → navigate → mark again) to find abandoned memory that isn't a strict leak (caches that never evict, ever-growing arrays). Time Profiler samples thread stacks; drive with a fixed scripted interaction, then look for: heavy frames under `body` evaluation or layout, `objc_msgSend` storms, and duplicate work in `updateUIView`-style sync paths. Filter by your module's symbols, invert the call tree, and hide system frames to find your code's share of the samples.

**Code Example**:
```swift
// A classic leak Time Profiler users then find in Leaks — and the fix
final class PlayerController: NSObject, ObservableObject {
    @Published var isPlaying = false
    private var startObservation: NSObjectProtocol?

    func attach() {
        startObservation = NotificationCenter.default
            .addObserver(forName: .AVPlayerItemDidPlayToEndTime,
                         object: nil, queue: .main) { [weak self] _ in   // leak without weak
                self?.isPlaying = false
            }
    }

    deinit {
        if let startObservation {                         // cleanup prevents retention
            NotificationCenter.default.removeObserver(startObservation)
        }
    }
}

extension Notification.Name {
    static let AVPlayerItemDidPlayToEndTime = Notification.Name("playbackEnded")
}

// Modern alternative: no observer API, structured lifetime — nothing to leak
struct PlaybackView: View {
    @State private var isPlaying = false
    var body: some View {
        Toggle("Playing", isOn: $isPlaying)
            .task {                                       // auto-cancelled on disappear
                for await _ in NotificationCenter.default.notifications(named: .AVPlayerItemDidPlayToEndTime) {
                    isPlaying = false
                }
            }
    }
}
```

---

<a id="q59"></a>
### Q59: How do MetricKit and os_signpost fit into a production diagnostics pipeline?

**Difficulty**: Advanced

**Strategy**:
MetricKit delivers privacy-preserving, aggregated real-user diagnostics daily: `MXMetricPayload` (launch time, hang rate, disk/memory writes, scroll hitches, CPU) and `MXDiagnosticPayload` (crash + hang stacks with symbolication hints). Adopt a `MXMetricManagerSubscriber` early in launch — payloads only arrive from users who opt in to sharing analytics, once per day, so never expect real-time telemetry; persist and upload them with your normal pipeline. `os_signpost` complements it with per-interval tracing you define (`begin`/`end` around a workflow), visible in Instruments' os_signpost track, and `Logger` (unified logging) with subsystem/category gives queryable logs that survive release builds with automatic redaction. Together: MetricKit tells you *what* users suffer (hangs, crashes, battery); signposts let you reproduce *where* locally.

**Code Example**:
```swift
import MetricKit
import os

final class MetricsSubscriber: NSObject, MXMetricManagerSubscriber {
    static let shared = MetricsSubscriber()

    private let logger = Logger(subsystem: "com.example.app", category: "metrics")
    private let signposter = OSSignposter(subsystem: "com.example.app", category: "sync")

    func start() {
        MXMetricManager.shared.add(self)
    }

    func didReceive(_ payloads: [MXMetricPayload]) {
        for payload in payloads {
            if let ms = payload.applicationLaunchMetrics?.timeToFirstDrawAverage?
                .converted(to: .milliseconds).value {
                logger.info("TTFD avg \(Int(ms), privacy: .public) ms")
            }
            if let hangRatio = payload.applicationResponsivenessMetrics?.hangTimeRatioAverage?.value {
                logger.info("hang-time ratio \(hangRatio, privacy: .public)")
            }
            DiagnosticStore.enqueue(payload.jsonRepresentation())  // ship to backend
        }
    }

    func didReceive(_ payloads: [MXDiagnosticPayload]) {
        for payload in payloads {
            for crash in payload.crashDiagnostics ?? [] {
                logger.fault("crash signal \(crash.signal?.rawValue ?? 0, privacy: .public)")
            }
            DiagnosticStore.enqueue(payload.jsonRepresentation())
        }
    }
}

// Signpost intervals around a workflow you suspect is slow — visible in Instruments
extension MetricsSubscriber {
    func traceSync() async {
        let state = signposter.beginInterval("cloudSync")
        defer { signposter.endInterval("cloudSync", state) }
        for batch in CloudSync.batches {
            await batch.run()
        }
    }
}

enum DiagnosticStore {
    static func enqueue(_ data: Data) { /* append to upload queue */ }
}
enum CloudSync {
    static var batches: [Batch] { [Batch()] }
    struct Batch { func run() async {} }
}
```

---

<a id="q60"></a>
### Q60: How do you use RegexBuilder and regex literals for robust parsing in Swift 6?

**Difficulty**: Intermediate

**Strategy**:
Swift regex literals (`/pattern/`) compile at build time with syntax checking; RegexBuilder composes the same engine declaratively with strongly typed captures — `Capture`, `TryCapture` (failable conversions), `OneOrMore`, `Optionally`, `ChoiceOf`, `Repeat` — so the match result is a tuple of typed values rather than string groups. Anchoring behavior differs: `firstMatch(in:)` finds anywhere, `^`/`$` anchor (with `.anchorsMatchLineEndings` for multiline), `wholeMatch` requires the entire string. Use `Regex`'s `.matches(in:)` for iteration and `UnicodeWordDomain`/custom semantic domains when parsing natural text. Prefer TryCapture for numbers/dates so malformed input fails the match instead of crashing a conversion.

**Code Example**:
```swift
import RegexBuilder

struct LogLine: Equatable {
    let level: String
    let id: Int
    let message: String
}

let logRegex = Regex {
    Capture(OneOrMore(.word))                       // level
    "["
    TryCapture(OneOrMore(.digit)) { Int($0) }       // typed, failable id
    "] "
    Capture(OneOrMore(.any, atLeast: 1))            // message
}

func parse(_ raw: String) -> [LogLine] {
    raw.split(separator: "\n").compactMap { line -> LogLine? in
        guard let m = try? logRegex.wholeMatch(in: String(line)) else { return nil }
        return LogLine(level: String(m.1), id: m.2, message: String(m.3))
    }
}

let input = """
info[42] sync finished in 1.2s
warn[43] retrying connection
error[oops] malformed id ignored
"""

print(parse(input))
// [LogLine(level: "info", id: 42, message: "sync finished in 1.2s"),
//  LogLine(level: "warn", id: 43, message: "retrying connection")]

// Regex literal for quick validation + extraction
let durationRegex = /(\d+(?:\.\d+)?)s/
if let m = durationRegex.firstMatch(in: "finished in 1.2s") {
    print(Double(m.1) ?? 0)   // 1.2 — literal captures are Substrings
}
```

---

<a id="q61"></a>
### Q61: What makes Swift enums powerful — associated values, pattern matching, and when do you need `indirect`?

**Difficulty**: Beginner

**Strategy**:
Swift enums are sum types: each case optionally carries associated values (typed payloads), giving you a closed set of states the compiler forces you to exhaust in `switch`. Pattern matching — value binding, `where` clauses, `if case`, `guard case` — makes state machines direct and safe; adding a case breaks every non-exhaustive switch at compile time, which is exactly the protection you want when modeling app state (`loading / loaded / failed`). `indirect` lets a case hold the enum itself (recursive payload) by boxing storage; common in expression trees. Use enums over booleans/option-strings whenever a value can only be one of a known set of variants.

**Code Example**:
```swift
indirect enum Expression {
    case number(Double)
    case variable(String)
    case add(Expression, Expression)
    case multiply(Expression, Expression)
    case negate(Expression)
}

extension Expression {
    func evaluate(_ env: [String: Double]) -> Double {
        switch self {
        case .number(let n): return n
        case .variable(let name): return env[name] ?? 0
        case .add(let lhs, let rhs): return lhs.evaluate(env) + rhs.evaluate(env)
        case .multiply(let lhs, let rhs): return lhs.evaluate(env) * rhs.evaluate(env)
        case .negate(let inner): return -inner.evaluate(env)
        }
    }
}

enum FetchState<Value> {
    case idle
    case loading
    case loaded(Value)
    case failed(Error, retries: Int)

    var isRetryable: Bool {
        if case .failed(_, let retries) = self { return retries < 3 }
        return false
    }
}

let state: FetchState<[String]> = .failed(URLError(.notConnectedToInternet), retries: 1)
if case .failed(let error, let retries) = state {
    print("failed after \(retries) tries: \(error.localizedDescription)")
}

let expr: Expression = .multiply(.number(3), .add(.variable("x"), .negate(.number(2))))
print(expr.evaluate(["x": 5]))   // 9.0
```

---

<a id="q62"></a>
### Q62: How are optionals implemented internally, and what are the performance implications?

**Difficulty**: Advanced

**Strategy**:
`Optional<Wrapped>` is a plain enum with `.none` and `.some(Wrapped)` cases — `T?` is pure sugar, and pattern matching, `if let`, and `guard let` are just `switch` over it. Memory layout: for pointer-sized payloads that can't be all-zero (class refs, function refs), the compiler uses the all-zero bit pattern as `.none` inline (a "niche") so `Optional<T>` is one word, not two; otherwise it needs a discriminant byte (`Optional<UInt8>` is 2 bytes). Optionals of value types live inline on the stack with no heap allocation; implicit promotion (`T` → `T?`) is a compile-time construct, free at runtime. Optional chaining short-circuits at the first `.none`; `map`/`flatMap` (`compactMap` on sequences) compose transformations monadically; force unwrap removes safety, not cost.

**Code Example**:
```swift
import Foundation
import UIKit

// Sugar == enum: these are literally the same type
let value: Int? = .some(41)
let sugar: Int? = 41

if case .some(let unwrapped) = value { print(unwrapped + 1) }   // 42: plain enum match

// Memory: class references use the null niche — same size as the bare pointer
MemoryLayout<UIView?>.size      // 8 on 64-bit (pointer with nil niche)
MemoryLayout<Int?>.size         // 9 (Int has no niche -> tag byte)
MemoryLayout<Int>.size          // 8

// Composition without pyramid-of-doom
struct Session { var user: User? }
struct User { var address: Address? }
struct Address { var zip: String? }

let session = Session()
let zipLength: Int? = session.user?.address?.zip?.count   // short-circuits at first nil

// flatMap chains dependent optionals cleanly
func firstValidPort(_ raw: [String]) -> Int? {
    raw.first { $0.hasPrefix(":") }                 // String?
        .flatMap { Int($0.dropFirst()) }            // -> Int? only if numeric
        .flatMap { (0...65_535).contains($0) ? $0 : nil }
}

print(firstValidPort(["host", ":8080", ":99999"]))   // 8080
```

---

<a id="q63"></a>
### Q63: What is protocol-oriented programming, and where does it beat class-based design in Swift?

**Difficulty**: Intermediate

**Strategy**:
POP designs around protocols + value types instead of class inheritance: behavior comes from protocol extensions (default implementations), conformance composes (a type can adopt many protocols, but only inherit one superclass), and value semantics keep sharing safe. Protocol extensions give retroactive-but-scoped default behavior without base classes, and generics specialize statically (no dynamic dispatch penalty) — the standard library itself is built this way (`Sequence`, `Equatable`, `Numeric`). Classes stay right for identity + lifetime + mutation shared across the app (models, actors, delegates); protocols win for shared capability across heterogeneous types, test seams, and algorithms over values. Two gotchas: static vs dynamic dispatch in extensions (a method defined only in an extension isn't dynamically dispatched unless declared in the protocol), and PATs (associated types) make protocols generic until you need existentials.

**Code Example**:
```swift
protocol Grooming {
    var ratePerHour: Decimal { get }
}

extension Grooming {
    func estimate(minutes: Int) -> Decimal {
        (ratePerHour * Decimal(minutes) / 60).rounded(2)
    }
}

protocol Auditable {
    var auditLabel: String { get }
}

struct DogGroomer: Grooming, Auditable {
    let ratePerHour: Decimal = 45
    let auditLabel = "dog-grooming"
}

struct CatGroomer: Grooming, Auditable {
    let ratePerHour: Decimal = 55
    let auditLabel = "cat-grooming"
}

// One generic algorithm over any Grooming — statically specialized per type
func compareEstimates(_ a: some Grooming, _ b: some Grooming, minutes: Int) -> Decimal {
    a.estimate(minutes: minutes) + b.estimate(minutes: minutes)
}

let staff: [any Grooming & Auditable] = [DogGroomer(), CatGroomer()]   // heterogeneous
for groomer in staff {
    print(groomer.auditLabel, groomer.estimate(minutes: 90))
}
print(compareEstimates(DogGroomer(), CatGroomer(), minutes: 60))   // 100
```

---

<a id="q64"></a>
### Q64: What do ABI stability and app thinning actually change for shipping Swift apps?

**Difficulty**: Advanced

**Strategy**:
ABI stability (Swift 5+) means compiled Swift binaries bind to system-provided runtime/standard library in the OS — apps no longer bundle the Swift runtime, shrinking download size and letting binaries from different Swift versions interoperate. Module stability (`.swiftmodule` as text-based interface) additionally lets a library compiled with one compiler be consumed by apps built with another — the basis of XCFramework binary distribution. App thinning is orthogonal delivery optimization: slicing ships only device-required resources from asset catalogs (2x/3x, arm64 variants), on-demand resources defer game-level content, and bitcode was removed from the pipeline in the Xcode 14 era. Practical wins: verify with App Store Connect's "App File Sizes" report; asset catalogs over loose PNGs; avoid embedding Swift runtime in frameworks for OS-provided components.

**Code Example**:
```swift
// Package.swift: ship a binary-targetable, module-stable library
// swift-tools-version: 6.0
import PackageDescription

let package = Package(
    name: "NetworkingCore",
    platforms: [.iOS(.v17)],
    products: [
        .library(name: "NetworkingCore", targets: ["NetworkingCore"]),
    ],
    targets: [
        .target(
            name: "NetworkingCore",
            swiftSettings: [
                .swiftLanguageMode(.v6),          // ABI-stable toolchain, source-stable mode
                .enableUpcomingFeature("StrictConcurrency"),
            ]
        ),
        .binaryTarget(name: "VendorCrypto", path: "./VendorCrypto.xcframework"),
    ]
)

// Slicing check in CI: report per-device variant sizes
// xcodebuild -archive ... -exportArchive ...
//   then App Store Connect > App File Sizes:
//   iPhone (arm64, 3x)  ->  assets only for 3x, arm64 slice
//   iPad (arm64, 2x)    ->  different slice, ~30-40% smaller than universal
```

---

<a id="q65"></a>
### Q65: How does StoreKit 2 work, and how do you test in-app purchases without App Store Connect?

**Difficulty**: Advanced

**Strategy**:
StoreKit 2 is the modern Swift API: `Product.products(for:)` loads store data, `purchase()` returns a `Transaction` you verify with `VerificationResult` (signed by App Store), and `Transaction.currentEntitlements` streams what the user owns — the source of truth for entitlement gates. Sync with `AppStore.sync()`, observe `Transaction.updates` for renewals/refunds in the background, and call `finish()` only after granting. Testing without App Store Connect uses a StoreKit Configuration file (`.storekit`) in Xcode: define products locally, test purchase interruption, refunds, subscription renewals at accelerated speed (advance time manually), and price changes. In unit tests, the `StoreKitTest` framework drives `SKTestSession` to reset state, expire subscriptions, and simulate failures programmatically; sandbox testers cover Apple-ID flows on device.

**Code Example**:
```swift
import StoreKit
import Observation

@Observable
@MainActor
final class EntitlementModel {
    private(set) var proUnlocked = false
    private var updatesTask: Task<Void, Never>?

    private var products: [Product] = []

    func load() async throws {
        products = try await Product.products(for: ["com.example.pro.monthly", "com.example.pro.lifetime"])
        updatesTask = Task.detached { [weak self] in
            for await update in Transaction.updates {          // renewals, refunds
                await self?.handle(update)
            }
        }
        await refreshEntitlements()
    }

    func purchase(_ product: Product) async throws {
        let result = try await product.purchase()
        switch result {
        case .success(let verification):
            if case .verified(let transaction) = verification {   // JWS signature check
                await grant(); await transaction.finish()
            } else {
                print("verification failed — do not unlock")
            }
        case .userCancelled, .pending:
            break   // pending: ask family approval etc.; UI unchanged
        @unknown default:
            break
        }
    }

    func refreshEntitlements() async {
        for await entitlement in Transaction.currentEntitlements {
            if case .verified(let t) = entitlement, t.productID == "com.example.pro.lifetime" {
                proUnlocked = true
            }
        }
    }

    private func handle(_ result: VerificationResult<Transaction>) async {
        if case .verified(let t) = result { await t.finish() }
        await refreshEntitlements()
    }

    private func grant() async { await refreshEntitlements() }
}
```

---

<a id="q66"></a>
### Q66: What window and immersive-space styles does visionOS offer, and how do you choose?

**Difficulty**: Advanced

**Strategy**:
A visionOS app composes SwiftUI scenes: `WindowGroup` with `.windowStyle(.automatic)` gives the standard movable window with glass materials and its own volumetric shadow; `.plain` strips the chrome for full-bleed content (media players); `windowResizability(.contentSize/.contentMinSize)` constrains user resizing. A `Volume` renders 3D content in a fixed cubic region shared with the room — the right home for scene-based RealityKit/Model3D content that users walk around. `ImmersiveSpace` takes over most of the field of view with styles `.mixed` (digital objects layered over passthrough — recommended default) and `.progressive`/`.full` (greater immersion for focused experiences, requiring more user intent to enter). Pick the least immersive space that delivers the experience: users keep spatial context, and mixed style avoids the immersion "confirmation" friction.

**Code Example**:
```swift
import SwiftUI
import RealityKit

@main
struct VisionStudioApp: App {
    @State private var immersionStyle: ImmersionStyle = .mixed

    var body: some Scene {
        WindowGroup(id: "main") {
            ContentView()
                .frame(minWidth: 640, minHeight: 480)
        }
        .windowStyle(.automatic)              // glass window, standard resizing
        .windowResizability(.contentMinSize)

        WindowGroup(id: "player") {
            VideoCanvas().ignoresSafeArea()
        }
        .windowStyle(.plain)                  // borderless cinematic surface

        Volume {
            Model3D(named: "Sculpture") { model in
                model.resizable()
            } placeholder: {
                ProgressView()
            }
        }
        .volumeBaseplateVisibility(.hidden)

        ImmersiveSpace(id: "studio") {
            StudioImmersive()
        }
        .immersionStyle(selection: $immersionStyle, in: .mixed, .progressive)
    }
}

struct StudioImmersive: View {
    var body: some View {
        RealityView { content in
            let anchor = AnchorEntity(world: .zero)
            content.add(anchor)
        }
    }
}

struct VideoCanvas: View { var body: some View { Color.black } }
struct ContentView: View { var body: some View { Text("Vision Studio") } }
```

---

<a id="q67"></a>
### Q67: How do you set up CI/CD for an iOS app with Xcode Cloud, fastlane, and test plans?

**Difficulty**: Intermediate

**Strategy**:
Centralize test configuration in an `.xctestplan`: list target bundles, configure parallelization, random execution order (exposes hidden test interdependence), coverage collection, and language/locale/screen-size variants — Xcode Cloud and fastlane both run these plans natively. Xcode Cloud is the low-ops option: connected to the repo, it builds, runs the plan on managed devices, distributes via TestFlight, and requires workflows (trigger + actions) plus a shared scheme with archive/test configs. fastlane is the code-owned alternative/adjunct: `match` for certificate/profile storage in a private repo or cloud keychain, `gym`/`build_app` for archives, `scan`/`run_tests` for plans, `pilot` for TestFlight — all reproducible locally. A common 2025 shape: fastlane match for signing, Xcode Cloud or a Mac mini runner for build+test, `pilot`/App Store Connect API for rollout, and SwiftLint/SwiftFormat gates before tests.

**Code Example**:
```ruby
# fastlane/Fastfile
default_platform(:ios)

platform :ios do
  desc "Run the full test plan on simulators"
  lane :test do
    scan(
      project: "InterviewGuide.xcodeproj",
      scheme: "AllTests",                        # scheme whose Test action uses the plan
      test_plan: "AllTests",                     # .xctestplan with variants below
      devices: ["iPhone 16", "iPad Pro 13-inch (M4)"],
      parallel_testing: true,
      code_coverage: true,
      fail_build: true
    )
  end

  desc "Nightly beta"
  lane :beta do
    ensure_git_status_clean
    match(type: "appstore", readonly: true)      # certs/profiles from shared store
    build_app(
      project: "InterviewGuide.xcodeproj",
      scheme: "InterviewGuide",
      export_method: "app-store"
    )
    upload_to_testflight(
      distribute_external: true,
      groups: ["Public Beta"],
      reject_build_waiting_for_review: true
    )
  end
end
```

---

<a id="q68"></a>
### Q68: struct vs class in Swift — how do you decide, and what does "value semantics" buy you in SwiftUI?

**Difficulty**: Beginner

**Strategy**:
Default to structs: value semantics mean every assignment is an independent copy (cheaply, via COW for collections), so sharing data across functions/threads can't cause spooky action-at-a-distance — this is also why structs work so well as SwiftUI view data and with Swift 6 concurrency (immutable-by-copy values need no synchronization). Choose classes when you need identity and shared mutable state: a single long-lived object multiple parts mutate (a model object, a cache, an actor), reference semantics, `deinit`, or ObjC interop. A pragmatic signal: if you find yourself adding `id` and mutating properties from several places, a class (usually `@Observable`) fits; if you pass it around and don't want mutations leaking, a struct fits. Remember: structs can still contain reference-type properties, which breaks value semantics unless those are also value-semantic (`@Observable` classes inside a struct behave by reference).

**Code Example**:
```swift
// Struct: copy semantics — bug-proof sharing
struct Playlist: Equatable {
    var name: String
    var tracks: [String] = []
}

var gym = Playlist(name: "Gym", tracks: ["Eye of the Tiger"])
var copy = gym
copy.tracks.append("Till I Collapse")
print(gym.tracks.count)    // 1 — original untouched
print(copy.tracks.count)   // 2

// Class: identity — shared mutable state
@Observable
final class PlayerModel {
    var queue: Playlist
    var isPlaying = false
    init(queue: Playlist) { self.queue = queue }

    func toggle() { isPlaying.toggle() }
}

let gymModel = PlayerModel(queue: gym)
let remote = gymModel                 // same object, no copy
remote.toggle()
print(gymModel.isPlaying)             // true — mutation visible everywhere

// SwiftUI payoff: struct state invalidates predictably
struct PlayerView: View {
    let model: PlayerModel            // reference: shared + observable
    @State private var edits = 0      // value: owned + reset predictably per identity
    var body: some View {
        VStack {
            Text(model.queue.name)
            Button("Edits: \(edits)") { edits += 1 }
        }
    }
}
```

---

<a id="q69"></a>
### Q69: How do Swift macros work, and how would you write a custom one?

**Difficulty**: Advanced

**Strategy**:
Swift macros (5.9) generate code at compile time: `@attached` macros (peer, member, memberAttribute, accessor, conformance) transform declarations and `@freestanding` macros (`#expression`, `#declaration`) expand in place. A macro is a separate compiler-plugin target: SwiftSyntax types the source, your `Macro` implementation returns new syntax, and the compiler type-checks the expansion — unlike old preprocessing, output must be valid, typed Swift. Attached macros can access argument labels but never runtime values; everything is syntactic. `@Observable`, `@Observable`-style wrappers, and `@Entry` in SwiftUI are macros shipped by Apple; building your own requires the plugin target, a macro-testing target (swift-macro-testing's `assertMacroExpansion`), and disciplined naming to keep expansions readable.

**Code Example**:
```swift
// ————— Macro implementation target: PluginCore —————
import SwiftCompilerPlugin
import SwiftSyntax
import SwiftSyntaxBuilder
import SwiftSyntaxMacros

/// #stringify(2 + 2) -> (2 + 2, "2 + 2")
public struct StringifyMacro: ExpressionMacro {
    public static func expansion(
        of node: some FreestandingMacroExpansionSyntax,
        in context: some MacroExpansionContext
    ) -> ExprSyntax {
        guard let argument = node.arguments.first?.expression else {
            fatalError("stringify requires an argument")
        }
        return "(\(argument), \(literal: argument.description))"
    }
}

@main
struct PluginCore: CompilerPlugin {
    let providingMacros: [Macro.Type] = [StringifyMacro.self]
}

// ————— Usage target —————
// #stringify(2 + 2)  expands to  (2 + 2, "2 + 2") at compile time
func demo() {
    let (value, source) = #stringify(2 + 2)
    print(value)    // 4
    print(source)   // 2 + 2
}

// ————— Testing the macro (swift-macro-testing) —————
// import SwiftSyntaxMacrosTestSupport
// func testStringify() {
//     assertMacroExpansion(
//         "#stringify(1 + 2)",
//         expandedSource: "(1 + 2, \"1 + 2\")",
//         macros: ["stringify": StringifyMacro.self]
//     )
// }
```

---

<a id="q70"></a>
### Q70: What are region-based isolation and `sending` parameters in Swift 6?

**Difficulty**: Expert

**Strategy**:
Region-based isolation (SE-0414) lets the compiler prove two things statically that used to require `@unchecked Sendable`: (1) it tracks which values form a "region" — a value plus everything transitively referencing it — so transferring one value out of a domain transfers the whole region, preventing aliasing races; (2) `sending` parameters and results declare that the value is transferred to the callee's (or caller's) isolation, allowing non-Sendable types to cross domains as long as the sender gives up access. Practically: an actor can hand a non-Sendable mutable buffer to another actor and the compiler enforces the sender no longer touches it — an ownership-flavored move without copying or unsafe casts. Related tooling: `Sending` as a parameter modifier, `isolated` parameters for one-shot synchronous access, and `transfer` semantics in `withTaskGroup`.

**Code Example**:
```swift
// A non-Sendable mutable document crossing domains safely via `sending`
final class MutableDocument {              // NOT Sendable — intentionally
    var text: String
    init(text: String) { self.text = text }
}

actor DocumentEditor {
    private var staged: MutableDocument?

    // `sending` doc: the caller transfers ownership; it may never touch it again
    func stage(_ doc: sending MutableDocument) {
        staged = doc
    }

    func append(_ addition: String) -> String? {
        guard let staged else { return nil }
        staged.text += addition
        return staged.text
    }
}

@MainActor
func compose(editor: DocumentEditor) async {
    let draft = MutableDocument(text: "Chapter 1")
    await editor.stage(draft)          // region transferred: `draft` unusable below
    // print(draft.text)               // error in Swift 6: region transferred — no race possible
    let snapshot = await editor.append("\nChapter 2")
    print(snapshot ?? "")
}

// Region transfer in task groups: value moved into child, not shared
actor Pipeline {
    func process(payload: MutableDocument) async -> String {
        await withTaskGroup(of: String.self) { group in
            group.addTask {            // capturing payload would be a race —
                "handled"              // without sending, this is an error
            }
            let result = await group.next() ?? ""
            payload.text += result     // untouched region stays usable here
            return payload.text
        }
    }
}
```

---

<a id="q71"></a>
### Q71: What is "approachable concurrency" and the Swift 6.2 default isolation mode?

**Difficulty**: Advanced

**Strategy**:
Approachable concurrency is Apple's answer to "Swift 6 is too hard to adopt": a set of defaults that make the common app safe with less annotation. Swift 6.2's `defaultIsolation(MainActor.self)` (or `NonisolatedNonsendingByDefault`-style upcoming features chosen per target) flips module-wide inference so plain functions are `@MainActor` by default — matching how UI apps actually work — while `nonisolated(nonsending)` makes nonisolated async functions run on the caller's executor, cutting pointless hops and the "hopping to main" waterfall. The migration story becomes: opt the target into MainActor-default, then carve compute-heavy code out with `nonisolated` deliberately, instead of annotating everything up. Combined with `InlineArray`/`Span` era features, 6.2 is about keeping strict guarantees while lowering ceremony.

**Code Example**:
```swift
// swift-tools-version: 6.2
// target settings:
// .swiftSettings([
//     .defaultIsolation(MainActor.self),        // module default: MainActor
//     .enableUpcomingFeature("NonisolatedNonsendingByDefault")
// ])

// With MainActor-default: this whole type is UI-isolated with zero annotations
final class WeatherModel {                       // implicitly @MainActor
    private(set) var forecast: [Day] = []

    func load() async throws {                   // MainActor by default
        forecast = try await Service.fetch()     // await hops out and back
    }

    // Carve OUT compute-heavy work deliberately:
    nonisolated static func parse(_ data: Data) throws -> [Day] {
        try JSONDecoder().decode([Day].self, from: data)   // no main-thread work
    }
}

struct Day: Codable, Sendable { let high: Double; let low: Double }

enum Service {
    static func fetch() async throws -> [Day] {
        let (data, _) = try await URLSession.shared.data(from: URL(string: "https://wx.example.com/7d")!)
        return try WeatherModel.parse(data)      // explicit boundary, still checked
    }
}
```

---

<a id="q72"></a>
### Q72: Where does `@MainActor` apply automatically in SwiftUI, and how does a `.task` modifier's actor context work?

**Difficulty**: Intermediate

**Strategy**:
`View` and its `body` are implicitly `@MainActor`-isolated (the protocol requirement is annotated), and view-modifier closures that run in response to UI events (`onTapGesture`, `onSubmit`) run on the main actor. `.task`/`.task(id:)` inherit the actor context of their enclosing view — so the async block starts on `@MainActor` and every hop back after an `await` re-enters the main actor; that's fine for UI work but wrong for heavy compute — mark helper functions `nonisolated` or push work to a detached domain explicitly. `onAppear`/`onChange` closures are synchronous main-actor code. The practical bug: a model method that is *not* MainActor-isolated called from `.task` hops off main, mutates state, then the view update reads it — make model methods that touch observable state `@MainActor` (or the model itself) so reads/writes serialize.

**Code Example**:
```swift
struct SearchView: View {
    @State private var query = ""
    @State private var results: [Result] = []
    @Environment(SearchModel.self) private var model

    var body: some View {
        NavigationStack {
            List(results) { Text($0.title) }          // body: MainActor
            .searchable(text: $query)
        }
        .onChange(of: query) { _, new in              // sync main-actor closure
            guard new.count > 2 else { results = [] }
        }
        .task(id: query) {                            // inherits @MainActor
            guard query.count > 2 else { return }
            // Don't block main: hop to a nonisolated search, hop back to assign
            let found = await model.search(new)       // nonisolated compute
            if !Task.isCancelled {                    // query may have changed mid-flight
                withAnimation { results = found }
            }
        }
    }
}

@Observable
final class SearchModel {
    var cache: [String: [Result]] = [:]               // main-actor state

    nonisolated func search(_ q: String) async -> [Result] {
        // CPU/IO off main actor
        let raw = try? await URLSession.data(from: url(q)).0
        return parse(raw)
    }

    @MainActor private var lastQuery = ""
    @MainActor func note(_ q: String) { lastQuery = q }

    nonisolated private func parse(_ data: Data?) -> [Result] {
        data.flatMap { try? JSONDecoder().decode([Result].self, from: $0) } ?? []
    }
    nonisolated private func url(_ q: String) -> URL { URL(string: "https://api.example.com/s?q=\(q)")! }
}

extension URLSession {
    static func data(from url: URL) async throws -> (Data, URLResponse) {
        try await URLSession.shared.data(from: url)
    }
}

struct Result: Identifiable, Codable, Sendable { let id = UUID(); let title: String }
```

---

<a id="q73"></a>
### Q73: How does `AttributedString` work, and when is it better than `Text` concatenation?

**Difficulty**: Beginner

**Strategy**:
`AttributedString` is a value-type attributed string: runs of characters carry attributes (`foregroundColor`, `font`, `link`, custom scopes) and support styling ranges by substring search. In SwiftUI, `Text` accepts an `AttributedString` and *merges* multiple `Text`s with `+`, but plain concatenation can't vary attributes mid-string; `AttributedString` gives you ranged styling, localization-friendly styling via markdown parsing, and per-run introspection. Parse inline markup with `try AttributedString(markdown:)` (supports links, bold, code spans), and define custom attribute scopes for domain styling (e.g., a `tickerSymbol` attribute). For lists of mixed content, prefer `Text(...) + Text(...)` for pure concatenation; reach for `AttributedString` when styling depends on *where* in the string, not which `Text`.

**Code Example**:
```swift
import SwiftUI

struct LegalFooter: View {
    var body: some View {
        Text(legal)
            .font(.footnote)
            .tint(.blue)                    // links use tint
    }

    var legal: AttributedString {
        var text = AttributedString()
        let lead = AttributedString("By continuing you accept the ")
        var terms = AttributedString("Terms of Service")
        terms.link = URL(string: "https://example.com/terms")
        terms.font = .footnote.weight(.semibold)
        var privacy = AttributedString("Privacy Policy")
        privacy.link = URL(string: "https://example.com/privacy")
        text += lead + terms + AttributedString(" and ") + privacy
        return text
    }
}

struct HighlightView: View {
    let haystack = "Swift 6 makes data races a compile-time error in Swift 6 mode"

    var body: some View {
        Text(highlighted)                    // ranged styling by search
    }

    var highlighted: AttributedString {
        var text = AttributedString(haystack)
        text.foregroundColor = .secondary
        var index = text.startIndex
        while let range = text[index...].range(of: "Swift 6") {
            text[range].foregroundColor = .pink
            text[range].font = .body.bold()
            index = range.upperBound
        }
        return text
    }
}

// Markdown source — the localized-friendly path
let md = try! AttributedString(
    markdown: "Upgrade to **Pro** and `sync` everywhere — [details](https://example.com)"
)
```

---

<a id="q74"></a>
### Q74: When do you use `Grid` instead of `LazyVGrid`, and how do their layout rules differ?

**Difficulty**: Intermediate

**Strategy**:
`Grid` (iOS 16) is a non-lazy, table-like container where every cell aligns in rows and columns, supports per-axis scrolling only as a whole, and participates in alignment across the entire grid — ideal for settings/forms/spreadsheets where columns should line up. `LazyVGrid`/`LazyHGrid` lazily materialize items in a single scroll direction, position items independently per column, and do NOT size-share rows (each column stacks independently) — right for photo walls and adaptive card mazes. Rule: if visual column alignment across rows matters, `Grid`; if content is large/homogeneous and laziness matters, lazy grids. `Grid` also accepts `GridRow` with flexible column definitions and combines with `ScrollView` for whole-grid scrolling; for two-dimensional lazy content, chunk data into rows of a non-lazy `Grid` inside the scroll view.

**Code Example**:
```swift
struct ComparisonMatrix: View {
    let plans: [String] = ["Free", "Pro", "Team"]
    let rows: [(String, [String])] = [
        ("Devices",      ["1", "5", "∞"]),
        ("Offline sync", ["—", "✓", "✓"]),
        ("API access",   ["—", "1k/day", "100k/day"]),
    ]

    var body: some View {
        Grid(alignment: .leading, horizontalSpacing: 24, verticalSpacing: 14) {
            GridRow {
                Color.clear.frame(width: 0, height: 1)      // empty corner cell
                ForEach(plans, id: \.self) { Text($0).font(.headline) }
            }
            ForEach(rows, id: \.0) { label, values in
                GridRow {
                    Text(label).foregroundStyle(.secondary)
                    ForEach(values, id: \.self) { Text($0) }
                }
            }
        }
        .padding()
    }
}

// Lazy counterpart: independent columns, lazily created for big data sets
struct PhotoWall: View {
    let items = (1..<400).map { "IMG_\($0)" }
    private let columns = [GridItem(.adaptive(minimum: 96, maximum: 160), spacing: 8)]

    var body: some View {
        ScrollView {
            LazyVGrid(columns: columns, spacing: 8) {
                ForEach(items, id: \.self) { name in
                    Image(systemName: "photo")
                        .resizable().scaledToFill()
                        .frame(height: 96).clipShape(.rect(cornerRadius: 8))
                }
            }
            .padding(.horizontal)
        }
    }
}
```

---

<a id="q75"></a>
### Q75: How do you react to scroll position and geometry in SwiftUI post-iOS 18?

**Difficulty**: Advanced

**Strategy**:
iOS 18 gave scroll views programmatic observability: `onScrollGeometryChange(for:of:action:)` samples a derived value from `ScrollGeometry` (contentOffset, visible rect, content insets) and fires the action only when the derived value changes — e.g., drive a stretchy header or a "scroll to top" button off `contentOffset.y` without GeometryReader. `scrollPosition(id:)` binds an optional/hashable identity for the visible anchor, replacing the old `ScrollViewReader` dance for most cases: assigning the binding scrolls; user scrolling updates it. Combine with `scrollTransition` for appearance effects at the edges and `onScrollVisibilityChange(threshold:)` for reveal triggers. GeometryReader remains for absolute measuring (overlays, full-bleed backgrounds), not for scroll state — it forces layout passes and conflicts with lazy content.

**Code Example**:
```swift
struct ReadingProgress: View {
    let articles: [Article]
    @State private var topID: Article.ID?
    @State private var showJump = false
    @State private var progress: Double = 0

    var body: some View {
        ScrollView {
            LazyVStack(spacing: 0) {
                ForEach(articles) { article in
                    ArticleRow(article: article)
                }
            }
            .scrollTargetLayout()                      // enables target-style paging if desired
        }
        .scrollPosition(id: $topID, anchor: .top)      // programmatic + observed
        .onScrollGeometryChange(for: Double.self) { geo in
            let distance = geo.contentSize.height - geo.containerSize.height
            guard distance > 0 else { return 0 }
            return min(max(geo.contentOffset.y / distance, 0), 1)
        } action: { old, new in
            progress = new                             // fires only on real change
            showJump = new > 0.1
        }
        .safeAreaInset(edge: .bottom) {
            if showJump {
                Button("Jump to top") {
                    withAnimation { topID = articles.first?.id }   // scrolls via binding
                }
                .buttonStyle(.borderedProminent)
                .padding(.bottom, 40)
                .transition(.move(edge: .bottom).combined(with: .opacity))
            }
        }
        .animation(.snappy, value: showJump)
    }
}

struct Article: Identifiable { let id = UUID(); var title = "" }
struct ArticleRow: View { let article: Article; var body: some View { Text(article.title).padding() } }
```

---

<a id="q76"></a>
### Q76: How do `#Preview` and `@Previewable` change the SwiftUI preview workflow?

**Difficulty**: Intermediate

**Strategy**:
`#Preview { ... }` replaces `PreviewProvider` with a macro: multiple previews per file (each with its own name and traits like `.device(...)`, `.colorScheme(.dark)`), no wrapper struct, and support for previews of any view/controller type. `@Previewable` lets a preview declare its own mutable state and bindings inline — previously impossible without a wrapper view: `@Previewable @State var text = ""` then pass `$text` into the view. Previews can be `async`, throw, and set up environment/models directly. For heavy models, build once outside the closure; for variants, add several `#Preview("name")` blocks — they appear in the canvas menu. Previews run in a special Xcode process (previews agent), which is why side effects like file writes should stay out of preview-only code paths.

**Code Example**:
```swift
import SwiftUI

struct TagEditor: View {
    @Binding var tag: String
    var onCommit: () -> Void

    var body: some View {
        HStack {
            TextField("Tag", text: $tag)
                .textFieldStyle(.roundedBorder)
            Button("Add", action: onCommit)
                .buttonStyle(.borderedProminent)
                .disabled(tag.isEmpty)
        }
        .padding()
    }
}

// Preview owns its own state — no wrapper view needed
#Preview("Light") {
    @Previewable @State var tag = "swift"
    TagEditor(tag: $tag, onCommit: { tag = "" })
        .padding()
        .environment(\.colorScheme, .light)
}

#Preview("Dark, AX") {
    @Previewable @State var tag = "concurrency"
    TagEditor(tag: $tag, onCommit: { print(tag) })
        .padding()
        .background(Color(uiColor: .systemBackground))
        .preferredColorScheme(.dark)
        .dynamicTypeSize(.accessibility3)
}

#Preview("With model", traits: .landscapeLeft) {
    let model = SettingsModel(accountName: "Preview User")
    AccountBar()
        .environment(model)
}

@Observable final class SettingsModel {
    var accountName = ""
    init(accountName: String = "") { self.accountName = accountName }
}
struct AccountBar: View {
    @Environment(SettingsModel.self) private var settings
    var body: some View { Text("Signed in as \(settings.accountName)") }
}
```

---

<a id="q77"></a>
### Q77: How do you implement a custom `AsyncSequence`, and what correctness rules apply?

**Difficulty**: Advanced

**Strategy**:
An `AsyncSequence` needs `makeAsyncIterator() -> AsyncIterator` where the iterator conforms to `AsyncIteratorProtocol` with a `next() async throws -> Element?`. The contract: returning `nil` finishes permanently, every iterator must be independent (each call to `makeAsyncIterator` produces a fresh sequence over the source), cancellation must be respected (`Task.isCancelled` or cancellation handlers in long waits), and `next()` after `nil` may return `nil` again but must not loop or crash. Single-consumer sources (like live streams) are naturally one-shot: either finish old iterators or back them with a shared buffer. For callback sources, wrap with `AsyncStream` instead of hand-rolling; hand-rolled sequences shine for computed/paged data where you control pacing (rate-limited polling, cursor pagination).

**Code Example**:
```swift
struct PagedRecords: AsyncSequence {
    typealias Element = Record
    let pageSize: Int

    func makeAsyncIterator() -> Iterator { Iterator(pageSize: pageSize) }

    struct Iterator: AsyncIteratorProtocol {
        let pageSize: Int
        private var cursor = 0
        private var exhausted = false

        mutating func next() async throws -> Record? {
            if exhausted || Task.isCancelled { return nil }   // respect cancellation
            let batch = try await API.records(from: cursor, limit: pageSize)
            guard !batch.isEmpty else {
                exhausted = true
                return nil
            }
            cursor += batch.count
            if batch.count < pageSize { exhausted = true }    // last page reached
            return batch.last                                 // yield final of each page
        }
    }
}

struct Record: Sendable, Codable { let id: Int; let title: String }
enum API {
    static func records(from cursor: Int, limit: Int) async throws -> [Record] {
        let url = URL(string: "https://api.example.com/records?cursor=\(cursor)&limit=\(limit)")!
        let (data, _) = try await URLSession.shared.data(from: url)
        return try JSONDecoder().decode([Record].self, from: data)
    }
}

// Independent iteration (each for-await gets its own iterator):
// for try await record in PagedRecords(pageSize: 50) { print(record.title) }

func sample() async throws {
    let tail = PagedRecords(pageSize: 1)
    var iterator = tail.makeAsyncIterator()
    if let record = try await iterator.next() {
        print("first tail record:", record.title)
    }
}
```

---

<a id="q78"></a>
### Q78: How do you build data visualizations with Swift Charts, and how do you make them interactive?

**Difficulty**: Intermediate

**Strategy**:
Swift Charts composes declarative marks (`LineMark`, `BarMark`, `AreaMark`, `PointMark`, `RuleMark`, `SectorMark` for pie/donut) over identifiable data; the `chart` builder infers axes from the mark's `x`/`y` value types (dates → time axis, plottable values → numeric axis). Style series with `foregroundStyle(by:)` for legends, `.interpolationMethod(.catmullRom)` for smooth lines, and `.symbol(by:)` for scatter clarity. Interactivity: `.chartXSelection(value:)` (iOS 17) binds the hovered/selected x value so you can render a `RuleMark` + detail overlay; `ChartProxy` (`chartXScale`/`plotFrame`) converts between data and view space for gestures; iOS 18 adds `chartScrollableAxes(.horizontal)` and `chartScrollPosition` for zooming into long series without a wrapping ScrollView.

**Code Example**:
```swift
import Charts
import SwiftUI

struct TrendChart: View {
    let readings: [Reading]
    @State private var selectedX: Date?

    var body: some View {
        Chart {
            ForEach(readings) { reading in
                AreaMark(
                    x: .value("Time", reading.timestamp),
                    y: .value("Load", reading.load)
                )
                .foregroundStyle(.green.gradient.opacity(0.25))
                .interpolationMethod(.catmullRom)

                LineMark(
                    x: .value("Time", reading.timestamp),
                    y: .value("Load", reading.load)
                )
                .foregroundStyle(.green)
                .interpolationMethod(.catmullRom)
            }

            if let selectedX {
                RuleMark(x: .value("Selected", selectedX))
                    .foregroundStyle(.secondary.opacity(0.6))
                    .annotation(position: .top, spacing: 8) {
                        detail(at: selectedX)
                    }
            }
        }
        .chartYScale(domain: 0...100)
        .chartScrollableAxes(.horizontal)          // iOS 18: pan long timelines
        .chartXSelection(value: $selectedX)        // iOS 17: hover/tap selection
        .frame(height: 240)
    }

    private func detail(at date: Date) -> some View {
        let nearest = readings.min {
            abs($0.timestamp.timeIntervalSince(date)) < abs($1.timestamp.timeIntervalSince(date))
        }
        return VStack(spacing: 2) {
            Text(nearest?.timestamp.formatted(date: .omitted, time: .shortened) ?? "")
            Text(nearest.map { "\($0.load.formatted(.number))%" } ?? "")
                .font(.headline)
        }
        .padding(8)
        .background(.regularMaterial, in: .rect(cornerRadius: 8))
    }
}

struct Reading: Identifiable {
    let id = UUID()
    let timestamp: Date
    let load: Double
}
```

---

<a id="q79"></a>
### Q79: What are Codable's advanced patterns — custom decoding, key strategies, and heterogeneous payloads?

**Difficulty**: Intermediate

**Strategy**:
Beyond `let data = try JSONDecoder().decode(T.self, from: data)`: `CodingKeys` maps snake_case/API names; `keyDecodingStrategy` (`convertFromSnakeCase`) handles global renaming without per-key work; `dateDecodingStrategy` (`iso8601`, custom formatter, milliseconds-since-epoch) centralizes date handling. Hand-written `init(from:)` covers everything else: defaulting missing keys (`decodeIfPresent` + fallback — remember `decodeIfPresent` throws on type mismatch but returns nil for null), flattening nested objects, validating combinations, and discriminating heterogeneous items by a `"type"` field into an enum with associated values. For eviction-safe evolution, treat unknown enum cases as a decodable `.unknown(String)` rather than failing the whole payload — old clients shouldn't crash on new server fields.

**Code Example**:
```swift
enum EventPayload: Codable {
    case checkin(venue: String)
    case note(body: String)
    case unknown(kind: String)

    private enum CodingKeys: String, CodingKey { case kind, venue, body }

    init(from decoder: Decoder) throws {
        let c = try decoder.container(keyedBy: CodingKeys.self)
        switch try c.decode(String.self, forKey: .kind) {
        case "checkin": self = .checkin(venue: try c.decode(String.self, forKey: .venue))
        case "note":    self = .note(body: try c.decode(String.self, forKey: .body))
        case let other: self = .unknown(kind: other)      // forward-compatible
        }
    }

    func encode(to encoder: Encoder) throws {
        var c = encoder.container(keyedBy: CodingKeys.self)
        switch self {
        case .checkin(let venue): try c.encode("checkin", forKey: .kind); try c.encode(venue, forKey: .venue)
        case .note(let body):     try c.encode("note", forKey: .kind); try c.encode(body, forKey: .body)
        case .unknown(let kind):  try c.encode(kind, forKey: .kind)
        }
    }
}

struct TimelineEntry: Codable {
    let id: UUID
    let occurredAt: Date
    var payload: EventPayload
    let tags: [String]

    private enum CodingKeys: String, CodingKey {
        case id, payload, tags
        case occurredAt = "occurred_at"
    }

    init(from decoder: Decoder) throws {
        let c = try decoder.container(keyedBy: CodingKeys.self)
        id = try c.decode(UUID.self, forKey: .id)
        occurredAt = try c.decode(Date.self, forKey: .occurredAt)
        payload = try c.decode(EventPayload.self, forKey: .payload)
        tags = (try? c.decode([String].self, forKey: .tags)) ?? []   // tolerate absence
    }
}

// Global strategies centralize date + key handling for simple payloads
let decoder = JSONDecoder()
decoder.dateDecodingStrategy = .millisecondsSince1970
```

---

<a id="q80"></a>
### Q80: How do you implement push notifications end to end in a modern SwiftUI app?

**Difficulty**: Intermediate

**Strategy**:
Request authorization via `UNUserNotificationCenter.requestAuthorization` (async/await native), register for remote notifications to get the device token (returned via the app delegate adaptor), and ship the token to your backend, which sends via APNs with your auth key. In-app presentation is delegated: implement `UNUserNotificationCenterDelegate` (via `@UIApplicationDelegateAdaptor` or `AppDelegate` in a `@main` App) to show foreground banners (`willPresent`) and to handle taps (`didReceive`). For SwiftUI-native routing, post taps into your router (`onOpenURL`-style) rather than building UI in the delegate. Declare capabilities (Push Notifications, Background Modes → Remote notifications) and, for silent pushes, send `content-available: 1` — but treat silent push as best-effort (system throttles); guaranteed UI updates use visible notifications or Live Activities.

**Code Example**:
```swift
import SwiftUI
import UserNotifications
import UIKit

final class PushCoordinator: NSObject, UNUserNotificationCenterDelegate, ObservableObject {
    static let shared = PushCoordinator()
    var deviceTokenHandler: (@Sendable (String) -> Void)?

    func enable() async -> Bool {
        let center = UNUserNotificationCenter.current()
        center.delegate = self
        do {
            return try await center.requestAuthorization(options: [.alert, .badge, .sound, .provisional])
        } catch {
            return false
        }
    }

    func registerForRemoteNotifications() {
        UIApplication.shared.registerForRemoteNotifications()
    }

    // Foreground banners
    func userNotificationCenter(_ center: UNUserNotificationCenter,
                                willPresent notification: UNNotification) async
        -> UNNotificationPresentationOptions {
        [.banner, .list, .sound, .badge]
    }

    // User tapped
    func userNotificationCenter(_ center: UNUserNotificationCenter,
                                didReceive response: UNNotificationResponse) async {
        let info = response.notification.request.content.userInfo
        if let route = info["route"] as? String {
            await MainActor.run { NotificationCenter.default.post(name: .pushRoute, object: route) }
        }
    }
}

@main
struct NotificationsApp: App {
    @UIApplicationDelegateAdaptor(AppDelegate.self) private var appDelegate
    @State private var router = Router()

    var body: some Scene {
        WindowGroup {
            RootView()
                .environment(router)
                .task {
                    if await PushCoordinator.shared.enable() {
                        PushCoordinator.shared.registerForRemoteNotifications()
                    }
                }
                .onReceive(NotificationCenter.default.publisher(for: .pushRoute)) { note in
                    if let route = note.object as? String { router.open(route) }
                }
        }
    }
}

final class AppDelegate: NSObject, UIApplicationDelegate {
    func application(_ application: UIApplication,
                     didRegisterForRemoteNotificationsWithDeviceToken token: Data) {
        let hex = token.map { String(format: "%02x", $0) }.joined()
        // Upload to backend: POST /devices { "token": hex, "platform": "ios" }
    }
    func application(_ application: UIApplication,
                     didFailToRegisterForRemoteNotificationsWithError error: Error) {
        assertionFailure("push registration failed: \(error)")
    }
}

extension Notification.Name { static let pushRoute = Notification.Name("pushRoute") }
```

---

<a id="q81"></a>
### Q81: How do you store secrets and tokens securely — UserDefaults vs Keychain vs file-encrypted storage?

**Difficulty**: Intermediate

**Strategy**:
UserDefaults is plaintext plist in the app container — fine for preferences, never for tokens, PII, or keys. The Keychain is the OS-managed, hardware-backed (Secure Enclave-backed class keys) store: items are encrypted at rest, can be device-only (`kSecAttrAccessibleWhenUnlockedThisDeviceOnly`), and sync via iCloud Keychain if you opt in. Model access with a small wrapper (or `Security`-based library) and always query/update by `kSecAttrService` + account, deleting before re-adding to avoid duplicates. SwiftData/Core Data can additionally use `allowsCloudEncryption`-style protections, but high-value secrets belong in the Keychain only. Never log tokens (unified logging auto-redacts but print doesn't), and rotate on `.background`-to-`.inactive` expiry policies; on jailbroken/compromised devices nothing is perfect — combine with App Attest for server-side trust.

**Code Example**:
```swift
import Foundation
import Security

struct Keychain {
    let service: String

    private func query(account: String) -> [String: Any] {
        [
            kSecClass as String: kSecClassGenericPassword,
            kSecAttrService as String: service,
            kSecAttrAccount as String: account,
        ]
    }

    func save(_ data: Data, account: String) throws {
        var add = query(account: account)
        SecItemDelete(query(account: account) as CFDictionary)      // replace semantics
        add[kSecValueData as String] = data
        add[kSecAttrAccessible as String] = kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly
        let status = SecItemAdd(add as CFDictionary, nil)
        guard status == errSecSuccess else { throw NSError(domain: NSOSStatusErrorDomain, code: Int(status)) }
    }

    func read(account: String) -> Data? {
        var q = query(account: account)
        q[kSecReturnData as String] = true
        q[kSecMatchLimit as String] = kSecMatchLimitOne
        var out: AnyObject?
        guard SecItemCopyMatching(q as CFDictionary, &out) == errSecSuccess else { return nil }
        return out as? Data
    }

    func delete(account: String) {
        SecItemDelete(query(account: account) as CFDictionary)
    }
}

struct AuthStore {
    private let keychain = Keychain(service: "com.example.app.auth")
    private static let tokenAccount = "session-token"

    var token: String? {
        get { keychain.read(account: Self.tokenAccount).flatMap { String(data: $0, encoding: .utf8) } }
        set {
            guard let newValue else { keychain.delete(account: Self.tokenAccount); return }
            try? keychain.save(Data(newValue.utf8), account: Self.tokenAccount)
        }
    }
}
```

---

<a id="q82"></a>
### Q82: How do DeviceCheck and App Attest protect your backend from compromised clients?

**Difficulty**: Advanced

**Strategy**:
Two complementary services: DeviceCheck gives each device two persistent per-developer bits (and a timestamped token via `DCDevice.current.generateToken` your server exchanges with Apple) — good for one-time trial eligibility that survives reinstalls. App Attest (`DCAppAttestService`) proves requests come from a *genuine, unmodified* build of *your app*: generate a key (Secure Enclave-backed, non-exportable), attest it once (`attestKey`) so Apple signs a statement binding the key to your app's identity, then `generateAssertion` per request — your server verifies the assertion chain and counter against the Apple endpoint, rejecting replayed/stale assertions via its embedded challenge. Guard against cheating in `generateAssertion` by including the actual request hash (nonce), not a static payload. Availability is `supported` gated and can be unavailable on some platforms — design a graceful degradation path (rate limits) instead of hard-blocking all users.

**Code Example**:
```swift
import DeviceCheck

actor AttestationClient {
    private let service = DCAppAttestService.shared
    private var keyID: String?
    private let server: AttestationServer

    init(server: AttestationServer) { self.server = server }

    var canAttest: Bool { service.isSupported }

    func ensureAttested() async throws {
        if let keyID, await server.isKeyAttested(keyID: keyID) { return }   // fast path
        let newKey = try await service.generateKey()                        // Secure Enclave key
        let challenge = await server.attestationChallenge(keyID: newKey)
        let attestation = try await service.attestKey(newKey, clientDataHash: challenge)
        try await server.registerAttestation(keyID: newKey, object: attestation)
        keyID = newKey
    }

    func assert<T: Encodable>(_ request: T) async throws {
        guard let keyID else { return }                     // degradation path
        let challenge = server.sha256(request)              // hash of the real request
        let assertion = try await service.generateAssertion(keyID, clientDataHash: challenge)
        try await server.verify(keyID: keyID, assertion: assertion, for: request)
    }
}

protocol AttestationServer: Sendable {
    func attestationChallenge(keyID: String) async -> Data
    func registerAttestation(keyID: String, object: Data) async throws
    func isKeyAttested(keyID: String) async -> Bool
    func verify(keyID: String, assertion: Data, for request: some Encodable) async throws
    func sha256(_ value: some Encodable) -> Data
}

// One-time trial with DeviceCheck's persistent bits
func checkTrialEligibility() async throws -> Bool {
    guard DCDevice.current.isSupported else { return false }
    let token = DCDevice.current.generateToken()
    return try await Backend.consumeTrialToken(token)
}
```

---

<a id="q83"></a>
### Q83: How do you monitor network reachability with NWPathMonitor?

**Difficulty**: Beginner

**Strategy**:
`NWPathMonitor` (Network framework) replaces the deprecated SCNetworkReachability: start it, and a closure fires whenever the path changes, telling you status (`.satisfied`/`.unsatisfied`/`.requiresConnection`), interface type (wifi/cellular/wired), whether the connection is expensive (cellular/hotspot), or constrained (low data mode). Run it on a dedicated `DispatchQueue` (never the main queue — callbacks arrive frequently) and hop to main for UI updates; expose state to SwiftUI via an `@Observable` model so views react with `onChange`. Use it for UX (offline banners, syncing deferral) — not for pre-checking before requests: reachability says nothing about your server; always attempt the request and handle the error.

**Code Example**:
```swift
import Network
import Observation

@Observable
@MainActor
final class ConnectivityModel {
    private(set) var isOnline = true
    private(set) var isExpensive = false
    private(set) var usesCellular = false

    private let monitor = NWPathMonitor()
    private let queue = DispatchQueue(label: "com.example.connectivity")

    init() {
        monitor.pathUpdateHandler = { [weak self] path in
            let snapshot = (
                online: path.status == .satisfied,
                expensive: path.isExpensive,
                cellular: path.usesInterfaceType(.cellular)
            )
            Task { @MainActor in
                self?.isOnline = snapshot.online
                self?.isExpensive = snapshot.expensive
                self?.usesCellular = snapshot.cellular
            }
        }
        monitor.start(queue: queue)
    }

    deinit { monitor.cancel() }
}

struct SyncBar: View {
    @Environment(ConnectivityModel.self) private var connectivity
    @Environment(SyncModel.self) private var sync

    var body: some View {
        @Bindable var sync = sync
        VStack {
            if !connectivity.isOnline {
                Label("Offline — changes will sync later", systemImage: "wifi.slash")
                    .font(.footnote)
                    .frame(maxWidth: .infinity)
                    .padding(8)
                    .background(.orange.opacity(0.15))
            }
            Toggle("Sync on cellular", isOn: $sync.cellularAllowed)
                .disabled(connectivity.isExpensive && !sync.cellularAllowed)
        }
        .animation(.snappy, value: connectivity.isOnline)
    }
}

@Observable final class SyncModel { var cellularAllowed = false }
```

---

<a id="q84"></a>
### Q84: When is `autoreleasepool` still needed in Swift?

**Difficulty**: Intermediate

**Strategy**:
ARC releases Swift objects at the end of scope, but objects returned from ObjC/Foundation APIs can be autoreleased — their release is deferred until the owning autorelease pool drains (normally at the end of the current run-loop turn / main thread drain). In a tight loop creating many such temporaries (parsing with `NSData`, string manipulations bridged through ObjC, loading `UIImage`/`CIImage` in a batch), peak memory climbs even though every object would eventually be freed. Wrapping each iteration in `autoreleasepool { }` drains immediately, keeping the high-water mark flat. Pure Swift value types (Array, String in Swift's native path) don't autorelease — profile with Allocations generations before adding ceremony. It's also a legitimate tool in long-running `DispatchQueue` work that lacks a natural drain point.

**Code Example**:
```swift
import UIKit

struct ThumbnailImporter {
    let fileURLs: [URL]

    // Import without ballooning memory: each iteration's autoreleaseables
    // (UIImage decoding paths, NSData reads) drain before the next pass.
    func importAll(into store: ThumbnailStore) async throws {
        for url in fileURLs {
            try autoreleasepool {
                guard let image = UIImage(contentsOfFile: url.path) else { return }
                let thumb = image.preparingThumbnail(of: CGSize(width: 240, height: 240))
                if let thumb { store.add(thumb, for: url) }
            }
            try Task.checkCancellation()
        }
    }
}

actor ThumbnailStore {
    private var thumbs: [URL: UIImage] = [:]
    func add(_ image: UIImage, for url: URL) { thumbs[url] = image }
}
```

---

<a id="q85"></a>
### Q85: How do you catch data races in CI with ThreadSanitizer and Swift 6 diagnostics?

**Difficulty**: Advanced

**Strategy**:
TSan instruments the running binary and reports actual races it observes (two threads touching the same memory with at least one write, unsynchronized) — enable it in the scheme's Diagnostics tab or `xcodebuild -enableThreadSanitizer YES` for test actions. Unlike Swift 6's compile-time checking, TSan finds races the compiler can't see: ObjC/C code, `@unchecked Sendable` lies, Core Data misuse, and closures capturing across dispatch queues. Workflow: run the full test plan with TSan (simulator only), treat every report as a bug (TSan has near-zero false-positive rate for true races, though reports can be noisy near the root cause), reproduce under `TSAN_OPTIONS=abort_on_error=1` in CI to fail fast. Combine: Swift 6 mode for Swift-level guarantees, TSan for boundaries, and address TSan "Swift access race" reports by introducing an actor, confining to a queue, or making the type Sendable correctly.

**Code Example**:
```swift
// CI invocation (Xcode Cloud custom script or fastlane scan):
//   xcodebuild test \
//     -scheme AllTests \
//     -destination 'platform=iOS Simulator,name=iPhone 16' \
//     -enableThreadSanitizer YES \
//     -enableAddressSanitizer NO \
//     -enableUndefinedBehaviorSanitizer NO

import Foundation

// The kind of race TSan catches that Swift 5 compiles happily:
final class OrderBook {
    private var orders: [Int] = []        // unsynchronized shared state

    func record(_ id: Int) {              // called from multiple queues
        orders.append(id)                 // TSan: Swift access race
    }

    var count: Int { orders.count }
}

let book = OrderBook()
DispatchQueue.concurrentPerform(iterations: 1_000) { i in
    book.record(i)                        // race observed at runtime
}

// Fix: serialize access — and let Swift 6 prove it
actor OrderBookActor {
    private var orders: [Int] = []

    func record(_ id: Int) {
        orders.append(id)
    }
    var count: Int { orders.count }
}

@main
struct App {
    static func main() async {
        let safe = OrderBookActor()
        await withTaskGroup(of: Void.self) { group in
            for _ in 0..<1_000 { group.addTask { await safe.record(Int.random(in: 0..<100)) } }
        }
        print(await safe.count)           // 1000, no race possible
    }
}
```

---

<a id="q86"></a>
### Q86: How do `@AppStorage` and `UserDefaults` work, and what are their limits?

**Difficulty**: Beginner

**Strategy**:
`@AppStorage("key")` is a property wrapper that reads/writes `UserDefaults` and invalidates SwiftUI views observing it (in-process only). It's perfect for small user preferences: flags, last tab, onboarding completion. Supported types cover Bool, Int, Double, String, URL, Data, and `RawRepresentable` enums; arrays/dicts require storing encoded `Data`. Limits: it's an unencrypted plist written eagerly — no secrets, no large blobs (megabytes of JSON slow app launch since the plist loads synchronously); changes from other processes (widgets, extensions) don't notify your app (use App Groups only for shared reads, plus explicit sync points); and the main-thread default suite can block — background writes should use a custom suite carefully. For model-scale persistence use SwiftData; for tokens use Keychain.

**Code Example**:
```swift
import SwiftUI

enum Theme: String, CaseIterable, Identifiable {
    case system, light, dark
    var id: String { rawValue }
}

struct PreferencesView: View {
    @AppStorage("theme") private var theme: Theme = .system
    @AppStorage("fontScale") private var fontScale = 1.0
    @AppStorage("favorites") private var favoritesData = Data()
    @AppStorage("showOnboarding") private var showOnboarding = true

    var body: some View {
        Form {
            Picker("Theme", selection: $theme) {
                ForEach(Theme.allCases) { Text($0.rawValue.capitalized).tag($0) }
            }

            Stepper("Font \(fontScale.formatted(.percent))", value: $fontScale, in: 0.8...1.4, step: 0.1)

            Toggle("Show onboarding", isOn: $showOnboarding)

            Section("Favorites") {
                let favorites = decodeFavorites(favoritesData)
                ForEach(favorites, id: \.self) { Text($0) }
            }
        }
        .preferredColorScheme(colorScheme)
        .task { showOnboarding = showOnboarding }   // persists through re-launch
    }

    private var colorScheme: ColorScheme? {
        switch theme { case .system: nil; case .light: .light; case .dark: .dark }
    }

    private func decodeFavorites(_ data: Data) -> [String] {
        (try? JSONDecoder().decode([String].self, from: data)) ?? []
    }
}
```

---

<a id="q87"></a>
### Q87: How do you modularize an iOS app with Swift Package Manager, and how does it improve build times and boundaries?

**Difficulty**: Intermediate

**Strategy**:
Break the app into local SPM packages/targets by feature and by layer (`DesignSystem`, `Networking`, `FeatureHome`, `FeatureCheckout`), with the app target as a thin composition root. Explicit dependency edges make illegal couplings compile-time errors (FeatureCheckout can't reach FeatureHome's internals), enable per-module unit testing, and — the big win — let Xcode build independent modules in parallel and skip unchanged ones, turning clean builds into incremental ones. Prefer library-type products with narrow public APIs (`public` only at the seam), keep resources local to the feature module, and use `.package(path:)` for local development. Watch the cost: too many tiny targets fragment compile jobs; measure with Xcode's Build Timeline and `-showBuildTimingSummary`, and avoid dynamic-linking everything (default static linking keeps launch fast).

**Code Example**:
```swift
// swift-tools-version: 6.0
import PackageDescription

let package = Package(
    name: "ShopApp",
    defaultLocalization: "en",
    platforms: [.iOS(.v17)],
    dependencies: [                                        // package-level graph
        .package(path: "../Domain"),
    ],
    products: [
        .library(name: "DesignSystem", targets: ["DesignSystem"]),
        .library(name: "Networking", targets: ["Networking"]),
        .library(name: "FeatureCheckout", targets: ["FeatureCheckout"]),
    ],
    targets: [
        .target(
            name: "DesignSystem",
            swiftSettings: [.swiftLanguageMode(.v6)]
        ),
        .target(
            name: "Networking",
            dependencies: [],
            swiftSettings: [.swiftLanguageMode(.v6)]
        ),
        .target(
            name: "FeatureCheckout",
            dependencies: [
                "DesignSystem",
                "Networking",
                .product(name: "CartDomain", package: "Domain"),  // remote seam
            ],
            resources: [.process("Resources")]
        ),
        .testTarget(
            name: "FeatureCheckoutTests",
            dependencies: ["FeatureCheckout"]
        ),
        .package(path: "../Domain"),                             // local package
    ]
)

// App target composes only — everything else flows through module APIs:
// @main struct ShopApp: App {
//     WindowGroup { CheckoutFlow() }
//         .modelContainer(for: Cart.self)
//         .environment(CheckoutModel(client: URLSessionClient()))
// }
```

---

<a id="q88"></a>
### Q88: How do you surface feature tips with TipKit?

**Difficulty**: Intermediate

**Strategy**:
TipKit (iOS 17+) standardizes onboarding hints: define a `Tip` (title, message, optional image/`SFSymbol`), gate it with `.rules` (`#Rule` on `$donationFeatureUsed` and `#Predicate`-style conditions including `Event`s with `donations`), and present it via `.popoverTip()` anchored to a view or `Tips.showSuspended`-controlled overlays. Track a custom `Tip.Event` (`.donate` with a count/duration) so tips appear after real usage context — e.g., only after the user has run 3 exports — and call `.invalidate(reason: .actionPerformed)` when the user completes the taught action. Users can reset with `Tips.resetAll()` for demos/testing. Keep copies short and localizable via the standard Tip conformances; don't stack tips (they queue automatically).

**Code Example**:
```swift
import TipKit
import SwiftUI

struct ExportTip: Tip {
    var title: Text { Text("Export as PDF") }
    var message: Text? { Text("Share this report with your team in one tap.") }
    var image: Image? { Image(systemName: "square.and.arrow.up") }

    var actions: [Action] {
        Action(id: "try", title: "Try it now")       // rendered inside the tip UI
    }

    // Custom event: fire when the user has meaningful context
    static let exportAttempted = Tips.Event(id: "export.attempted")
    static let viewedReports = Tips.Event(id: "reports.viewed")

    var rules: [Rule] {
        // Show after 3 report views AND no successful export yet
        #Rule(Self.viewedReports) { $0.donations.count >= 3 }
        #Rule(Self.exportAttempted) { $0.donations.isEmpty }
    }
}

struct ReportsView: View {
    @State private var exportTip = ExportTip()

    var body: some View {
        List(Report.samples) { Text($0.title) }
            .task { ExportTip.viewedReports.donate() }       // context signal
            .toolbar {
                Button {
                    exportTip.invalidate(reason: .actionPerformed)  // taught — done
                    ExportTip.exportAttempted.donate()
                    Exporter.run()
                } label: {
                    Image(systemName: "square.and.arrow.up")
                }
                .popoverTip(exportTip, arrowEdge: .bottom) { action in
                    if action.id == "try" { Exporter.run() }
                }
            }
    }
}

enum Exporter { static func run() {} }
struct Report: Identifiable { let id = UUID(); var title = "Q3 Summary"; static var samples: [Report] { [Report()] } }

@main
struct ReportsApp: App {
    var body: some Scene {
        WindowGroup { ReportsView() }
            .task { try? Tips.configure([.displayFrequency(.daily)]) }
    }
}
```

---

<a id="q89"></a>
### Q89: How do you integrate maps in SwiftUI with the modern MapKit API?

**Difficulty**: Intermediate

**Strategy**:
The SwiftUI-native `Map` (iOS 17+) is driven by a `MapCameraPosition` binding (`.userLocation(followsWithHeading:)`, `.region(...)`, `.camera(...)`) instead of the old coordinator dance — the binding is both programmatically settable and user-updated, so one state drives everything. Annotations compose from Swift data with `Annotation` (fully SwiftUI content, anchor-based) or `Marker` (balloon, cheap), plus `UserAnnotation` for the user dot; selection is first-class via `Map(selection:)` over identifiable tags. iOS 18 adds `LookAroundPreview` for street-level immersion and `mapStyle(.imagery(elevation: .real))` for realistic terrain. Heavy maps (10k+ points) still need clustering/tiles via the full MapKit APIs or UIKit interop, and location permissions run through `CLLocationManager` (or `requestWhenInUseAuthorization` flows) as before.

**Code Example**:
```swift
import SwiftUI
import MapKit
import CoreLocation

struct SiteMap: View {
    @State private var camera: MapCameraPosition = .automatic
    @State private var selectedSite: Site?
    @State private var lookAroundScene: MKMapItem?

    let sites = Site.samples

    var body: some View {
        Map(selection: $selectedSite, position: $camera) {
            UserAnnotation()                        // blue dot

            ForEach(sites) { site in
                Marker(site.name, coordinate: site.coordinate)   // cheap system balloon
                    .tag(site)
            }

            ForEach(sites.filter(\.needsInspection)) { site in
                Annotation("Inspection due", coordinate: site.coordinate) {
                    Circle().fill(.orange).frame(width: 12, height: 12)
                        .overlay(Circle().stroke(.white, lineWidth: 2))
                }
            }
        }
        .mapStyle(.standard(elevation: .real))      // iOS 17: elevation styles
        .mapControls {
            MapUserLocationButton()
            MapCompass()
            MapScaleView()
        }
        .safeAreaInset(edge: .bottom) {
            if let site = selectedSite {
                SiteCard(site: site, onLookAround: { fetchScene(for: site) })
                    .padding()
            }
        }
        .sheet(item: $lookAroundScene) { item in
            LookAroundPreview(initialScene: item)
                .frame(height: 260)
                .clipShape(.rect(cornerRadius: 16))
                .padding()
        }
    }

    private func fetchScene(for site: Site) {
        let request = MKLookAroundSceneRequest(coordinate: site.coordinate)
        Task { lookAroundScene = ((try? await request.get()) ?? nil).map(MKMapItem.init) }
    }
}

struct Site: Identifiable, Hashable {
    let id = UUID()
    var name: String
    var coordinate: CLLocationCoordinate2D
    var needsInspection: Bool
    static var samples: [Site] {
        [Site(name: "North Depot", coordinate: .init(latitude: 37.33, longitude: -122.03), needsInspection: true),
         Site(name: "Harbor Yard", coordinate: .init(latitude: 37.79, longitude: -122.40), needsInspection: false)]
    }
}

struct SiteCard: View {
    let site: Site; var onLookAround: () -> Void
    var body: some View {
        HStack {
            VStack(alignment: .leading) { Text(site.name).font(.headline); Text("Tap marker for details").font(.caption) }
            Spacer()
            Button("Look Around", action: onLookAround).buttonStyle(.bordered)
        }
        .padding()
        .background(.regularMaterial, in: .rect(cornerRadius: 14))
    }
}
```

---

<a id="q90"></a>
### Q90: What lock primitives does Swift offer now — `NSLock`, `OSAllocatedUnfairLock`, and the `Mutex` from the Synchronization module?

**Difficulty**: Advanced

**Strategy**:
Locks are still the right tool for tiny, non-suspending critical sections inside one isolation domain — but Swift's options now span safety levels. `NSLock` is portable but easy to misuse (forgetting unlock, no value coupling). `OSAllocatedUnfairLock` (os module, iOS 16+) is a fast userspace mutex tied to a value: `withLock { $0 }` scopes the protected state and the unlock, and it's Sendable so Swift 6 can pass it across domains. Swift 6's `Mutex` (Synchronization module, iOS 18+) is the concurrency-safe standard-library version — same `withLock` shape, checked for exclusivity, pairs naturally with `sending`. Rules that keep you safe: never hold a lock across an `await` (suspension can interleave and deadlock or race), keep closures small and non-reentrant, and prefer actors when operations need to suspend — locks guard data, actors guard *activities*.

**Code Example**:
```swift
import Synchronization   // iOS 18+ / Swift 6
import Foundation

// Shared statistics pool: hot, tiny critical sections — lock, not actor
final class MetricAccumulator: Sendable {
    private let samples = Mutex<[Double]>([])

    func record(_ value: Double) {
        samples.withLock { $0.append(value) }        // unlock guaranteed
    }

    func snapshot() -> (count: Int, mean: Double?) {
        samples.withLock { buffer in
            guard !buffer.isEmpty else { return (0, nil) }
            let sum = buffer.reduce(0, +)
            return (buffer.count, sum / Double(buffer.count))
        }
    }
}

// Pre-iOS 18: OSAllocatedUnfairLock with state coupling
import os
final class LegacyCounter: Sendable {
    private let count = OSAllocatedUnfairLock(initialState: 0)

    func increment() -> Int {
        count.withLock { state in
            state += 1
            return state
        }
    }
}

// ANTI-PATTERN: never hold a lock across suspension
actor BadExample {
    private let mutex = Mutex<[Int]>([])

    func broken() async {
        mutex.withLock { buffer in
            buffer.append(1)
            // await something()    // error-prone: suspension inside exclusivity
        }
    }
}

// Correct division of labor: lock for synchronous stats, actor for async flow
actor FlowCoordinator {
    private var pending: [Int] = []

    func submit(_ id: Int, stats: MetricAccumulator) async {
        pending.append(id)
        stats.record(Double(id))     // lock is acquired+released synchronously
        await flushIfNeeded()
    }

    private func flushIfNeeded() async { pending.removeAll() }
}
```

---

<a id="q91"></a>
### Q91: How does Swift Concurrency work under the hood — jobs, executors, and the cooperative pool?

**Difficulty**: Expert

**Strategy**:
Every async operation is a task tree: a `Task` wraps state (priority, cancellation flag, task-locals) and enqueues jobs onto executors. The default executor is the global cooperative thread pool (a small, fixed-size set of threads per QoS band, created by the runtime — not GCD's potentially unbounded thread pool), where jobs run to completion; because jobs never block cooperatively, a handful of threads suffices, and blocking them (semaphores, sync waits) is the classic meltdown. Actors add serial executors: each actor has its own queue-like executor, so jobs targeting the actor run one at a time — an "actor hop" is just a job enqueued on a different executor. Suspension (`await`) is a function returning; the continuation reschedules as a new job — which is why state can change across `await` (reentrancy) and why stack traces show "async" frames without deep native stacks. Priorities influence job ordering and are escalated through task dependencies; `MainActor` is simply a global actor whose executor is the main dispatch queue.

**Code Example**:
```swift
// Tracing what actually executes: jobs hopping executors
actor Ledger {
    private(set) var balance = 0

    func deposit(_ amount: Int) {
        print("deposit runs on", Thread.current.description, "- cooperative worker")
        balance += amount
    }
}

@MainActor
func monthlyRun(ledger: Ledger) async {
    print("start on main actor:", Thread.current)         // main thread
    await ledger.deposit(500)                             // hop: job onto Ledger's
                                                          // serial executor
    await Task.yield()                                    // reschedule: new job,
                                                          // back on main actor
    print("resume on main:", Thread.current)              // main thread again
}

// Priorities propagate through structure:
func priorityDemo() async {
    await withTaskGroup(of: Void.self) { group in
        group.addTask(priority: .utility) {
            print("child utility priority:", Task.currentPriority)  // .utility
        }
        group.addTask(priority: nil) {
            print("child inherits:", Task.currentPriority)          // parent's
        }
        // If a .userInitiated task awaits this group, the runtime escalates
        // these children so the blocker gets CPU sooner (anti-inversion).
    }
}
```

---

<a id="q92"></a>
### Q92: How do `layoutPriority` and fixed vs flexible frames change view sizing in SwiftUI?

**Difficulty**: Beginner

**Strategy**:
SwiftUI sizing flows parent→child (a proposal) then child→parent (a chosen size). `frame(width:height:)` makes a fixed frame: the child is offered exactly that size regardless of the parent's proposal; `frame(min:max:)` is flexible: the child may claim anything in the range, and the frame then fills what the parent proposed. Stacks distribute available space to children with equal priority; when space is tight, `layoutPriority(_:)` ranks children — higher priority children are measured and placed first, claiming their ideal size, and lower-priority views get the remainder (the classic fix: a long label truncated next to a small badge). The rule of thumb: reach for `layoutPriority` when H/VStack children fight over a shrinking width; use fixed frames for exact-size chrome, flexible frames to stretch or pad.

**Code Example**:
```swift
struct FlightRow: View {
    let city: String
    let gate: String

    var body: some View {
        HStack(spacing: 8) {
            // Without priority, the short gate text steals width and the city
            // truncates awkwardly. Give the city first claim on space:
            Text(city)
                .layoutPriority(1)                 // measured first, ideal width
                .lineLimit(1)
                .truncationMode(.tail)

            Spacer(minLength: 4)

            Text("GATE \(gate)")
                .font(.caption.weight(.bold))
                .padding(.horizontal, 8)
                .padding(.vertical, 4)
                .background(.blue.opacity(0.12), in: .capsule)
                .fixedSize()                       // never shrink/compress
        }
        .padding(.vertical, 2)
    }
}

struct DemoLayout: View {
    var body: some View {
        VStack(spacing: 12) {
            Text("Fixed frame: proposal ignored")
                .frame(width: 140)                  // always 140 wide, text may clip

            Text("Flexible frame: claims proposal, centers content")
                .frame(maxWidth: .infinity, alignment: .leading)   // stretches

            FlightRow(city: "San Francisco Intl — Terminal 2", gate: "B14")
        }
        .padding()
    }
}
```

---

<a id="q93"></a>
### Q93: How do you use `@Query` in SwiftData to drive SwiftUI views?

**Difficulty**: Intermediate

**Strategy**:
`@Query` is SwiftData's reactive fetch: initialize it with a `FetchDescriptor` (predicate, sort, offsets/limits, relationship prefetching) — or the convenience `#Predicate` + sort keyPath initializer — and the view re-renders automatically whenever matching models change, animate updates with the `animation:` parameter. `@Query` fetches from the `modelContext` in the environment, so it must sit below the `modelContainer`/`modelContext` injection point. Dynamic filters are the classic pitfall: `@Query` is a property wrapper initialized once per identity, so don't reassign it in `body` — instead pass filter values in `init` (view identity change rebuilds the query) or keep a small parent view whose inputs feed the query initializer. Combine query sections with `modelContext.insert/delete` in event handlers for full CRUD.

**Code Example**:
```swift
import SwiftData
import SwiftUI

@Model
final class Recipe {
    var name: String
    var minutes: Int
    var isFavorite: Bool
    var cuisine: String

    init(name: String, minutes: Int, isFavorite: Bool = false, cuisine: String) {
        self.name = name; self.minutes = minutes; self.isFavorite = isFavorite; self.cuisine = cuisine
    }
}

struct RecipeBrowser: View {
    @Environment(\.modelContext) private var context
    @Query(sort: \Recipe.minutes, order: .forward, animation: .snappy)
    private var quickRecipes: [Recipe]

    var body: some View {
        NavigationStack {
            List {
                ForEach(quickRecipes) { recipe in
                    RecipeCell(recipe: recipe)
                }
                .onDelete(perform: delete)
            }
            .overlay {
                if quickRecipes.isEmpty {
                    ContentUnavailableView("No quick recipes", systemImage: "timer")
                }
            }
        }
    }

    private func delete(at offsets: IndexSet) {
        for index in offsets { context.delete(quickRecipes[index]) }
        try? context.save()
    }
}

struct RecipeCell: View {
    @Bindable var recipe: Recipe

    var body: some View {
        HStack {
            VStack(alignment: .leading) {
                Text(recipe.name)
                Text("\(recipe.minutes) min · \(recipe.cuisine)")
                    .font(.caption).foregroundStyle(.secondary)
            }
            Spacer()
            Button {
                recipe.isFavorite.toggle()          // @Bindable writes persist
            } label: {
                Image(systemName: recipe.isFavorite ? "star.fill" : "star")
            }
        }
    }
}

// Dynamic filter via init: parent changes cuisine -> new identity -> new query
struct CuisineFilterView: View {
    let cuisine: String
    @Query private var recipes: [Recipe]

    init(cuisine: String) {
        self.cuisine = cuisine
        let predicate = #Predicate<Recipe> { $0.cuisine == cuisine }
        _recipes = Query(filter: predicate, sort: [SortDescriptor(\Recipe.name)],
                         animation: .snappy)
    }

    var body: some View {
        List(recipes) { Text($0.name) }
    }
}
```

---

<a id="q94"></a>
### Q94: What does enabling CloudKit sync on SwiftData entail, and what are the schema constraints?

**Difficulty**: Advanced

**Strategy**:
SwiftData-to-CloudKit is one line of configuration — `ModelConfiguration(cloudKitDatabase: .automatic)` (or `.private("iCloud.container")`/`.none`) — and the engine maps your models to a CloudKit-managed store with the user's private database, syncing across devices. The constraints come from CloudKit's rules: no unique constraints (`@Attribute(.unique)` is unsupported in CloudKit-backed stores), relationships must be optional or have default values, all attributes need optionality or defaults (lightweight init requirements), `Codable`/struct attributes are stored as blobs (no querying inside), and delete rules apply through CloudKit's reference actions. Sync behavior is eventual: mutations upload opportunistically, remote changes merge via the background machinery — design for convergence (timestamps, deterministic merges) rather than assuming ordering, and handle `PersistentModel` remote-change notifications for live UI refresh.

**Code Example**:
```swift
import SwiftData
import CloudKit
import SwiftUI

// CloudKit-compatible model: optional-or-default everything, no .unique
@Model
final class JournalEntry {
    var localID: UUID = UUID()           // identity via attribute, not .unique constraint
    var body: String = ""
    var mood: Int = 3
    var updatedAt: Date = .now           // merge-resolving timestamp
    var tags: [String] = []              // array of primitives: OK, opaque to queries
    var author: Author?                  // relationships must be optional

    init(body: String, mood: Int, author: Author?) {
        self.body = body; self.mood = mood; self.author = author
    }
}

@Model
final class Author {
    var name: String = ""
    @Relationship(deleteRule: .nullify, inverse: \JournalEntry.author)
    var entries: [JournalEntry] = []
    init(name: String) { self.name = name }
}

@main
struct JournalApp: App {
    let config = ModelConfiguration(
        cloudKitDatabase: .private("iCloud.com.example.journal")   // explicit container
    )

    var body: some Scene {
        WindowGroup { JournalList() }
            .modelContainer(for: [JournalEntry.self, Author.self], configurations: config)
    }
}

struct JournalList: View {
    @Query(sort: \JournalEntry.updatedAt, order: .reverse) private var entries: [JournalEntry]
    @Environment(\.modelContext) private var context

    var body: some View {
        List(entries) { entry in
            VStack(alignment: .leading) {
                Text(entry.body)
                Text(entry.updatedAt.formatted(.relative(presentation: .named)))
                    .font(.caption2).foregroundStyle(.tertiary)
            }
        }
        .task { _ = try? context.save() }   // offline edits sync when reachable later
    }
}
```

---

<a id="q95"></a>
### Q95: How do App Clips work, and when are they worth the investment?

**Difficulty**: Intermediate

**Strategy**:
An App Clip is a <10MB Swift/SwiftUI extension of your app launched instantly from an App Clip Code (NFC/visual), QR link, Safari banner, Maps, or Messages — ideal for transactions someone needs *right now* (parking, ordering, bike rental) before they trust a full download. Build it as an `appclip` target with the shared feature modules; focus its UI on a single flow, authenticate with `ASAuthorizationAppleIDProvider` (limited to name+email verification), and pay with Apple Pay without full account creation. Hand off state to the full app via a shared App Group + `NSUserActivity` so the user continues seamlessly after installing. Worth it when conversion at a physical/place-based moment is core to the business; not worth it for pure social/creation apps whose value needs the full app.

**Code Example**:
```swift
import SwiftUI
import AppClip
import StoreKit

@main
struct ScooterClipApp: App {
    @State private var session = RentalSession()

    var body: some Scene {
        WindowGroup {
            RentalFlow()
                .environment(session)
                .continuousCornerBackground()
                .task { await session.begin() }          // parse invocation URL
                .onAppClip { payload in
                    // payload: invocation metadata (URL, app clip code)
                    session.deepLink = payload?.url
                }
        }
    }
}

@Observable
@MainActor
final class RentalSession {
    var scooterID: String?
    var deepLink: URL?
    var rentalMinutes = 0

    func begin() async {
        if let url = deepLink, let id = url.lastPathComponent.split(separator: "-").last {
            scooterID = String(id)      // sc-bay-4471 -> 4471
        }
    }
}

struct RentalFlow: View {
    @Environment(RentalSession.self) private var session
    @State private var showPay = false

    var body: some View {
        VStack(spacing: 16) {
            Image(systemName: "figure.outdoor.cycle").font(.system(size: 44))
            Text(session.scooterID.map { "Scooter \($0) ready" } ?? "Scan a scooter")
                .font(.title3.weight(.semibold))
            Stepper("Minutes: \(session.rentalMinutes)", value: .init(
                get: { session.rentalMinutes }, set: { session.rentalMinutes = $0 }
            ), in: 5...120, step: 5)
            Button("Pay & Unlock") { showPay = true }
                .buttonStyle(.borderedProminent)
                .disabled(session.rentalMinutes == 0 || session.scooterID == nil)
        }
        .padding()
        .sheet(isPresented: $showPay) {
            ApplePaySheet(minutes: session.rentalMinutes)   // Apple Pay — no signup
        }
    }
}

struct ApplePaySheet: View {
    let minutes: Int
    var body: some View { Text("Apple Pay: \(minutes) min") }
}

extension View {
    func continuousCornerBackground() -> some View {
        background(.thinMaterial, in: .rect(cornerRadius: 20))
    }
}
```

---

<a id="q96"></a>
### Q96: What's the difference between `withAnimation`, the `.animation` modifier, and `Transaction`?

**Difficulty**: Beginner

**Strategy**:
`withAnimation { change }` is *explicit*: wrap a state mutation and SwiftUI animates the resulting layout changes of that one update, with the animation you pass (`.spring`, `.easeInOut`). The `.animation(_:value:)` modifier is *implicit*: attached to a view, it animates changes whenever `value` changes — the modern scoped form (the old unvalued `.animation()` leaked to children and is deprecated). `Transaction` is the mechanism underneath: every view update carries one, and you can inspect or mutate it (`transaction { $0.animation = nil }` to opt a subtree out, `disablesAnimations` to force immediate jumps). Compose them: `withAnimation` at the interaction site for orchestration, `.animation(value:)` for component-local continuous response, and `transaction`/`.transaction(value:)` for surgical opt-outs.

**Code Example**:
```swift
struct CardStack: View {
    @State private var expanded = false
    @State private var spin = false

    var body: some View {
        VStack(spacing: 24) {
            RoundedRectangle(cornerRadius: 20)
                .fill(.indigo.gradient)
                .frame(width: expanded ? 320 : 140, height: expanded ? 420 : 140)
                .overlay { Text("Deal").font(.title).foregroundStyle(.white) }
                // Implicit: reacts whenever `expanded` flips, regardless of source
                .animation(.spring(duration: 0.4, bounce: 0.2), value: expanded)
                .rotation3DEffect(.degrees(spin ? 180 : 0), axis: (x: 0, y: 1, z: 0))
                .transaction { $0.animation = spin ? nil : $0.animation }  // spin jumps

            Button(expanded ? "Collapse" : "Expand") {
                withAnimation(.spring(duration: 0.45)) {   // explicit orchestration
                    expanded.toggle()
                }
                spin.toggle()                              // un-animated: no wrapper
            }
            .buttonStyle(.borderedProminent)
        }
        .padding()
    }
}
```

---

<a id="q97"></a>
### Q97: How does the iOS 18 TabView tab API change tab-based UIs?

**Difficulty**: Intermediate

**Strategy**:
iOS 18 replaced `TabView { }` + `.tabItem { }` with a declarative `Tab` syntax: `TabView { Tab("Home", systemImage: "house") { HomeView() } … }` — searchable tabs via `tabRole(.search)`, section grouping via `TabSection` for sidebar-adaptive tab bars, and per-tab customization support where users can reorder tabs from the trailing menu by default. The old `tabItem` API still compiles (deprecated warnings aside), but the new model composes better with the liquid-glass tab bar and gives the system semantic structure for search/section behavior. Selection still binds by the tab's value or role; combine with `TabView(selection:)` and `.tabViewStyle` as before.

**Code Example**:
```swift
import SwiftUI

enum Section: String, Hashable { case forYou, library, discover }

struct StoreAppView: View {
    @State private var selectedTab = "browse"

    var body: some View {
        TabView(selection: $selectedTab) {
            Tab("Browse", systemImage: "square.grid.2x2", value: "browse") {
                BrowseView()
            }
            Tab("Search", systemImage: "magnifyingglass", value: "search", role: .search) {
                SearchView()
            }
            Tab("Library", systemImage: "books.vertical", value: "library") {
                TabSection("Reading") {
                    Text("Continue Reading").padding()
                }
                TabSection("Archived") {
                    Text("12 archived items").padding()
                }
            }
            Tab("Profile", systemImage: "person.crop.circle", value: "profile") {
                ProfileView()
            }
        }
        .tabViewStyle(.sidebarAdaptable)    // TabSection groups adapt to a sidebar
        .onChange(of: selectedTab) { _, tab in
            Analytics.screenView(tab)                     // observe selection changes
        }
    }
}

struct BrowseView: View { var body: some View { Text("Browse") } }
struct SearchView: View { var body: some View { Text("Search") } }
struct ProfileView: View { var body: some View { Text("Profile") } }
enum Analytics { static func screenView(_ name: String) {} }
```

---

<a id="q98"></a>
### Q98: How do String Catalogs modernize localization in Xcode?

**Difficulty**: Beginner

**Strategy**:
A String Catalog (`.xcstrings`) is a JSON-backed catalog Xcode auto-populates by scanning your code for `String(localized:)`, `Text("...")`, `LocalizedStringResource`, and asset names — replacing manual `.strings`/`.stringsdict` bookkeeping. Each key shows per-language state (translated, needs review, stale), plural variation is edited visually (no more stringsdict syntax), and you can mark strings for review, add comments for translators, and export/import XLIFF for vendors. Workflow: write UI text inline in code → build once to harvest → translate in the catalog or export → CI builds pull the catalog automatically. For dynamic text from the server, `String(localized:)` + `String.LocalizationValue` keys still resolve through the catalog, and `LocalizedStringResource` (usable in non-UI types like App Intents) composes with it.

**Code Example**:
```swift
import SwiftUI

struct OrderSummaryView: View {
    let itemCount: Int
    let eta: Date

    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            // Keys harvested into Localizable.xcstrings at build time
            Text("Order Summary")          // key + source EN, ready to translate

            // Plurals: catalog UI edits the variations, code stays simple
            Text("\(itemCount) items waiting for pickup")

            // Format arguments from localized resources
            Text("Arrives \(eta.formatted(date: .omitted, time: .shortened))")
        }
        .padding()
    }
}

// Non-UI layer (models, App Intents): LocalizedStringResource composes too
struct ReceiptGenerator {
    static let title = LocalizedStringResource("receipt.title", defaultValue: "Your Receipt")
    var greeting: String {
        String(localized: "welcome.back", defaultValue: "Welcome back!")
    }
}

// Plurals resolved by the catalog's variation editor — code stays simple
func badge(_ count: Int) -> String {
    String(localized: "You have \(count) notifications")
}
```

---

<a id="q99"></a>
### Q99: How should you use os Logger and unified logging so logs are useful in production?

**Difficulty**: Beginner

**Strategy**:
Use `Logger(subsystem:category:)` instead of `print`: logs flow into the unified system (Console.app, `log stream`, and sysdiagnoses users send you), are timestamped and thread-tagged, and persist at appropriate levels. Respect levels — `debug` (ephemeral, dev-only), `info` (persisted briefly, flows worth keeping), `notice`/`error`/`fault` (persisted longer; fault captures full context) — and privacy: string interpolations default to redacted (`<private>`) in release; mark truly non-sensitive values with `privacy: .public` (counts, states), never tokens or PII. Structure messages as stable patterns with interpolated *values* so `log stream --predicate 'subsystem == "com.example.app"'` filters cleanly. For time intervals, pair with `OSSignposter` (Q59) — logs tell you what happened, signposts tell you how long it took.

**Code Example**:
```swift
import os
import Foundation

struct SyncEngine {
    private let logger = Logger(subsystem: "com.example.app", category: "sync")
    private let signposter = OSSignposter(subsystem: "com.example.app", category: "sync")

    func run(account: String) async throws {
        logger.debug("sync starting")                       // dev-only, not persisted
        logger.info("sync begin for account \(account, privacy: .private(mask: .hash))")  // identifiable but safe

        let state = signposter.beginInterval("sync.run")
        defer { signposter.endInterval("sync.run", state) }

        do {
            let count = try await pushPending()
            logger.notice("sync pushed \(count, privacy: .public) records")   // persisted
        } catch {
            logger.error("sync failed: \(error.localizedDescription, privacy: .public)")
            logger.fault("sync fault account=\(account, privacy: .private(mask: .hash))") // rich context kept
            throw error
        }
        logger.info("sync complete") 
    }

    private func pushPending() async throws -> Int {
        let (data, _) = try await URLSession.shared.data(from: URL(string: "https://api.example.com/push")!)
        return (try? JSONDecoder().decode(PushResult.self, from: data).count) ?? 0
    }
}

struct PushResult: Codable { let count: Int }

// Console / Terminal:
//   log stream --predicate 'subsystem == "com.example.app" AND category == "sync"'
//   log show --last 1h --predicate 'eventMessage CONTAINS "sync failed"'
```

---

<a id="q100"></a>
### Q100: Design an offline-first iOS architecture — how do the pieces (local store, sync engine, conflict resolution, UI state) fit together?

**Difficulty**: Expert

**Strategy**:
Offline-first inverts the usual stack: the local store (SwiftData) is the source of truth the UI renders from via `@Query`, and the network is a *replication* concern, not a fetch-on-render one. Writes go local-first inside an atomic mutation envelope — record intent + updated-at + pending flag — then a sync engine drains the outbox: a serialized actor (single-flight, cancellable via `BGTaskScheduler`/push-to-start and `.task` foreground triggers) that pushes mutations and pulls server deltas with cursor-based pagination. Conflict resolution must be deterministic and testable: per-field last-writer-wins on server time for independent edits, server authority for money/security with client rebase on 409. The UI layer exposes sync health (`SyncState` observable: idle/syncing/error/offline) so banners and retry affordances reflect reality, and the whole engine is deterministic under test by injecting `HTTPClient` + `Clock` and simulating partitions, stale cursors, and conflicts.

**Code Example**:
```swift
import SwiftData
import Observation

// ——— 1. Local model with sync metadata ———
@Model
final class Note {
    @Attribute(.unique) var localID: UUID
    var body: String
    var updatedAt: Date
    var revision: Int = 0
    var pending: Bool = true                       // part of the outbox

    init(body: String, updatedAt: Date = .now) {
        self.localID = UUID(); self.body = body; self.updatedAt = updatedAt
    }
}

// ——— 2. Sync engine: serialized, outbox-draining actor ———
actor SyncEngine {
    enum State: Equatable { case idle, syncing, offline, failed(String) }
    private var state: State = .idle
    private var inflight: Task<Void, Error>?
    private var cursor = Date.distantPast           // pull cursor persists across runs

    private let api: any NotesAPI
    private let now: @Sendable () -> Date           // injectable clock for deterministic tests

    init(api: any NotesAPI, now: @escaping @Sendable () -> Date = { .now }) {
        self.api = api; self.now = now
    }

    func drain(context: ModelContext) async throws {
        guard inflight == nil else { return }                  // single-flight
        let job = Task {
            defer { inflight = nil }
            state = .syncing
            // Push phase: mutations in stable order
            let outbox = try context.fetch(FetchDescriptor<Note>(
                predicate: #Predicate { $0.pending == true },
                sortBy: [SortDescriptor(\.updatedAt)]))
            for note in outbox {
                let outcome = try await api.push(
                    id: note.localID, body: note.body, revision: note.revision,
                    clientUpdatedAt: note.updatedAt)
                switch outcome {
                case .accepted(let revision):                   // fast path
                    note.revision = revision; note.pending = false
                case .conflict(let server):                     // deterministic rebase
                    note.body = Self.rebase(local: note.body, server: server.body)
                    note.revision = server.revision
                    note.updatedAt = now()
                }
                try context.save()
            }
            // Pull phase: cursor deltas keep payloads bounded
            let delta = try await api.changes(since: cursor)
            for remote in delta.notes where !remote.deleted {
                let id = remote.id
                let local = try context.fetch(FetchDescriptor<Note>(
                    predicate: #Predicate { $0.localID == id })).first
                if let local {
                    if remote.revision > local.revision && !local.pending {
                        local.body = remote.body; local.revision = remote.revision
                    }
                } else {
                    context.insert(Note(body: remote.body))
                }
            }
            cursor = delta.until
            try context.save()
            state = .idle
        }
        inflight = job
        try await job.value
    }

    static func rebase(local: String, server: String) -> String {
        local == server ? server : server + "\n—\n" + local    // explicit merge artifact
    }
}

// ——— 3. UI: local truth + sync health ———
@Observable
@MainActor
final class SyncStatus {
    var state = SyncEngine.State.idle
    var lastSync: Date?
}

struct NotesScreen: View {
    @Query(sort: \Note.updatedAt, order: .reverse) private var notes: [Note]
    @Environment(\.modelContext) private var context
    @Environment(SyncStatus.self) private var status

    var body: some View {
        List {
            if status.state == .offline {
                Label("Offline — edits saved locally", systemImage: "wifi.slash")
                    .font(.footnote).foregroundStyle(.orange)
            }
            ForEach(notes) { NoteCell(note: $0) }
        }
        .refreshable { try? await SyncController.shared.drain(context: context) }
        .task { try? await SyncController.shared.drain(context: context) }   // foreground trigger
    }
}

struct NoteCell: View {
    @Bindable var note: Note
    var body: some View {
        TextField("Note", text: $note.body)
            .onSubmit { note.updatedAt = .now; note.pending = true }
    }
}

// ——— 4. Port of the protocol (nested types live outside) ———
enum Outcome: Sendable { case accepted(revision: Int); case conflict(server: RemoteNote) }
struct RemoteNote: Sendable { let id: UUID; let body: String; let revision: Int; let deleted: Bool }
struct Delta: Sendable { let notes: [RemoteNote]; let until: Date }

protocol NotesAPI: Sendable {
    func push(id: UUID, body: String, revision: Int, clientUpdatedAt: Date) async throws -> Outcome
    func changes(since: Date) async throws -> Delta
}

enum SyncController { static var shared: SyncEngine! }   // wired at launch with API + clock
```

---
