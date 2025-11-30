<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/flutter-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>Flutter Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for mobile developers</b></p>
</div>

---

## Table of Contents

1. [How do you optimize the performance of a large list in Flutter to prevent jank?](#q1-how-do-you-optimize-the-performance-of-a-large-list-in-flutter-to-prevent-jank) <span class="intermediate">Intermediate</span>
2. [How do you manage global state efficiently using Riverpod?](#q2-how-do-you-manage-global-state-efficiently-using-riverpod) <span class="intermediate">Intermediate</span>
3. [How do you prevent memory leaks when using Streams in Flutter?](#q3-how-do-you-prevent-memory-leaks-when-using-streams-in-flutter) <span class="beginner">Beginner</span>
4. [How do you run heavy computational tasks without blocking the UI thread (Isolates)?](#q4-how-do-you-run-heavy-computational-tasks-without-blocking-the-ui-thread-isolates) <span class="advanced">Advanced</span>
5. [How do you handle platform-specific code (e.g., accessing battery level)?](#q5-how-do-you-handle-platform-specific-code-eg-accessing-battery-level) <span class="intermediate">Intermediate</span>
6. [How do you reduce the app size for production builds?](#q6-how-do-you-reduce-the-app-size-for-production-builds) <span class="intermediate">Intermediate</span>
7. [How do you implement a custom painter for complex drawing?](#q7-how-do-you-implement-a-custom-painter-for-complex-drawing) <span class="advanced">Advanced</span>
8. [How do you ensure a widget rebuilds only when specific data changes (Selector)?](#q8-how-do-you-ensure-a-widget-rebuilds-only-when-specific-data-changes-selector) <span class="intermediate">Intermediate</span>
9. [How do you implement deep linking in Flutter (Navigator 2.0)?](#q9-how-do-you-implement-deep-linking-in-flutter-navigator-20) <span class="advanced">Advanced</span>
10. [How do you debug layout issues where widgets have 'unbounded height'?](#q10-how-do-you-debug-layout-issues-where-widgets-have-unbounded-height) <span class="beginner">Beginner</span>
11. [How do you use Keys to preserve widget state when the list order changes?](#q11-how-do-you-use-keys-to-preserve-widget-state-when-the-list-order-changes) <span class="intermediate">Intermediate</span>
12. [How do you implement a theme switch (Dark/Light mode) dynamically?](#q12-how-do-you-implement-a-theme-switch-darklight-mode-dynamically) <span class="beginner">Beginner</span>
13. [How do you optimize images by caching them?](#q13-how-do-you-optimize-images-by-caching-them) <span class="beginner">Beginner</span>
14. [How do you write a unit test for a simple business logic class?](#q14-how-do-you-write-a-unit-test-for-a-simple-business-logic-class) <span class="beginner">Beginner</span>
15. [How do you handle errors globally in Flutter (e.g., crash reporting)?](#q15-how-do-you-handle-errors-globally-in-flutter-eg-crash-reporting) <span class="intermediate">Intermediate</span>
16. [How do you perform Dependency Injection using GetIt?](#q16-how-do-you-perform-dependency-injection-using-getit) <span class="intermediate">Intermediate</span>
17. [How do you use Flutter Hooks to simplify AnimationController management?](#q17-how-do-you-use-flutter-hooks-to-simplify-animationcontroller-management) <span class="intermediate">Intermediate</span>
18. [How do you communicate with native platform code using MethodChannel?](#q18-how-do-you-communicate-with-native-platform-code-using-methodchannel) <span class="advanced">Advanced</span>
19. [How do you handle keyboard visibility and dismissal efficiently?](#q19-how-do-you-handle-keyboard-visibility-and-dismissal-efficiently) <span class="beginner">Beginner</span>
20. [How do you implement a SliverAppBar with a floating title?](#q20-how-do-you-implement-a-sliverappbar-with-a-floating-title) <span class="intermediate">Intermediate</span>
21. [How do you make your Flutter app accessible using Semantics?](#q21-how-do-you-make-your-flutter-app-accessible-using-semantics) <span class="intermediate">Intermediate</span>
22. [How do you implement internationalization (i18n) using the flutter_localizations package?](#q22-how-do-you-implement-internationalization-i18n-using-the-flutter_localizations-package) <span class="intermediate">Intermediate</span>
23. [How do you write an integration test in Flutter?](#q23-how-do-you-write-an-integration-test-in-flutter) <span class="advanced">Advanced</span>
24. [How do you debug performance issues using Flutter DevTools?](#q24-how-do-you-debug-performance-issues-using-flutter-devtools) <span class="intermediate">Intermediate</span>
25. [How do you create a custom animation using TweenAnimationBuilder?](#q25-how-do-you-create-a-custom-animation-using-tweenanimationbuilder) <span class="intermediate">Intermediate</span>
26. [How do you display a floating widget using OverlayEntry?](#q26-how-do-you-display-a-floating-widget-using-overlayentry) <span class="advanced">Advanced</span>
27. [How do you optimize rebuilds with ValueListenableBuilder?](#q27-how-do-you-optimize-rebuilds-with-valuelistenablebuilder) <span class="beginner">Beginner</span>
28. [How do you handle asynchronous data in Riverpod with AsyncValue?](#q28-how-do-you-handle-asynchronous-data-in-riverpod-with-asyncvalue) <span class="intermediate">Intermediate</span>
29. [How do you validate a Form in Flutter?](#q29-how-do-you-validate-a-form-in-flutter) <span class="beginner">Beginner</span>
30. [How do you embed a native Android/iOS view in Flutter?](#q30-how-do-you-embed-a-native-androidios-view-in-flutter) <span class="advanced">Advanced</span>
31. [How do you implement Pull-to-Refresh functionality?](#q31-how-do-you-implement-pull-to-refresh-functionality) <span class="beginner">Beginner</span>
32. [How do you create a Hero animation between two screens?](#q32-how-do-you-create-a-hero-animation-between-two-screens) <span class="intermediate">Intermediate</span>
33. [How do you create a rounded image using `ClipRRect`?](#q33-how-do-you-create-a-rounded-image-using-cliprrect) <span class="beginner">Beginner</span>
34. [How do you create a blur effect (Glassmorphism)?](#q34-how-do-you-create-a-blur-effect-glassmorphism) <span class="intermediate">Intermediate</span>
35. [How do you implement Drag and Drop?](#q35-how-do-you-implement-drag-and-drop) <span class="intermediate">Intermediate</span>
36. [How do you allow users to pinch-to-zoom and pan an image?](#q36-how-do-you-allow-users-to-pinch-to-zoom-and-pan-an-image) <span class="intermediate">Intermediate</span>
37. [How do you implement a page view (swiping between screens)?](#q37-how-do-you-implement-a-page-view-swiping-between-screens) <span class="beginner">Beginner</span>
38. [How do you create a Tab Bar layout?](#q38-how-do-you-create-a-tab-bar-layout) <span class="beginner">Beginner</span>
39. [How do you implement search functionality using `SearchDelegate`?](#q39-how-do-you-implement-search-functionality-using-searchdelegate) <span class="intermediate">Intermediate</span>
40. [How do you use `InheritedWidget` to pass data down the tree?](#q40-how-do-you-use-inheritedwidget-to-pass-data-down-the-tree) <span class="advanced">Advanced</span>
41. [How do you handle keyboard shortcuts (Web/Desktop)?](#q41-how-do-you-handle-keyboard-shortcuts-webdesktop) <span class="intermediate">Intermediate</span>
42. [How do you group multiple semantics into one (`MergeSemantics`)?](#q42-how-do-you-group-multiple-semantics-into-one-mergesemantics) <span class="intermediate">Intermediate</span>
43. [How do you create a gradient text effect?](#q43-how-do-you-create-a-gradient-text-effect) <span class="intermediate">Intermediate</span>
44. [How do you use `RepaintBoundary` to improve performance?](#q44-how-do-you-use-repaintboundary-to-improve-performance) <span class="advanced">Advanced</span>
45. [What is the difference between `Offstage`, `Visibility`, and `Opacity`?](#q45-what-is-the-difference-between-offstage-visibility-and-opacity) <span class="intermediate">Intermediate</span>
46. [What is the difference between `Flexible` and `Expanded`?](#q46-what-is-the-difference-between-flexible-and-expanded) <span class="beginner">Beginner</span>
47. [How do you make responsive layouts based on parent size (`LayoutBuilder`)?](#q47-how-do-you-make-responsive-layouts-based-on-parent-size-layoutbuilder) <span class="intermediate">Intermediate</span>
48. [How do you size a widget relative to its parent (`FractionallySizedBox`)?](#q48-how-do-you-size-a-widget-relative-to-its-parent-fractionallysizedbox) <span class="intermediate">Intermediate</span>
49. [How do you create complex flow layouts (`Flow`)?](#q49-how-do-you-create-complex-flow-layouts-flow) <span class="advanced">Advanced</span>
50. [How do you check if the device is online?](#q50-how-do-you-check-if-the-device-is-online) <span class="intermediate">Intermediate</span>

---

### Q1: How do you optimize the performance of a large list in Flutter to prevent jank?

**Difficulty**: Intermediate

**Strategy:**
1.  Use `ListView.builder` to lazily build items only when they are visible.
2.  Use `const` constructors for item widgets to avoid unnecessary rebuilds.
3.  Implement `itemExtent` (if items have fixed height) to avoid expensive layout calculations.

**Code Example:**
```dart
ListView.builder(
  itemCount: 10000,
  itemExtent: 50.0, // Fixed height optimization
  itemBuilder: (context, index) {
    return const ListTile(title: Text('Optimized Item'));
  },
);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q2: How do you manage global state efficiently using Riverpod?

**Difficulty**: Intermediate

**Strategy:**
Use a `StateNotifierProvider` (or `NotifierProvider` in Riverpod 2.0) to encapsulate state logic. Watch the provider in the UI using `ConsumerWidget` or `ref.watch()`. This ensures only dependent widgets rebuild.

**Code Example:**
```dart
// 1. Define State
class Counter extends Notifier<int> {
  @override
  int build() => 0;
  void increment() => state++;
}

// 2. Define Provider
final counterProvider = NotifierProvider<Counter, int>(Counter.new);

// 3. Consume
class Home extends ConsumerWidget {
  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final count = ref.watch(counterProvider);
    return Text('$count');
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q3: How do you prevent memory leaks when using Streams in Flutter?

**Difficulty**: Beginner

**Strategy:**
Always cancel stream subscriptions in the `dispose()` method of a `StatefulWidget`. Alternatively, use `StreamBuilder` which handles subscription and unsubscription automatically.

**Code Example:**
```dart
class MyWidget extends StatefulWidget {
  @override
  _MyWidgetState createState() => _MyWidgetState();
}

class _MyWidgetState extends State<MyWidget> {
  late StreamSubscription _sub;

  @override
  void initState() {
    super.initState();
    _sub = stream.listen((event) => print(event));
  }

  @override
  void dispose() {
    _sub.cancel(); // Crucial cleanup
    super.dispose();
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q4: How do you run heavy computational tasks without blocking the UI thread (Isolates)?

**Difficulty**: Advanced

**Strategy:**
Use `Isolate.run()` (Flutter 3.7+) or `compute()` function. Flutter is single-threaded; running heavy loops on the main thread causes frame drops. Isolates run in separate memory spaces.

**Code Example:**
```dart
Future<int> heavyTask(int value) async {
  // Blocks if run on main thread
  return Future.delayed(Duration(seconds: 2), () => value * 2);
}

void calculate() async {
  // Spawns a new isolate, runs the function, returns result, kills isolate
  final result = await Isolate.run(() => heavyTask(10));
  print(result);
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q5: How do you handle platform-specific code (e.g., accessing battery level)?

**Difficulty**: Intermediate

**Strategy:**
Use **Platform Channels** (`MethodChannel`). The Flutter app sends a message to the host (Android/iOS), which executes native code (Kotlin/Swift) and returns the result.

**Code Example:**
```dart
static const platform = MethodChannel('com.example/battery');

Future<void> getBatteryLevel() async {
  try {
    final int result = await platform.invokeMethod('getBatteryLevel');
    print('Battery level: $result%');
  } on PlatformException catch (e) {
    print("Failed to get battery level: '${e.message}'.");
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q6: How do you reduce the app size for production builds?

**Difficulty**: Intermediate

**Strategy:**
1.  Use `flutter build apk --split-per-abi` (Android) to generate separate APKs for different architectures.
2.  Remove unused resources and dependencies.
3.  Use the `--obfuscate` and `--split-debug-info` flags to compress code and remove symbols.
4.  Compress images/assets.

**Code Example:**
```bash
# Build app bundle (Android)
flutter build appbundle --target-platform android-arm,android-arm64

# Obfuscate (Optional)
flutter build apk --obfuscate --split-debug-info=/<project-name>/<directory>

# Analyze size
flutter build apk --analyze-size
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q7: How do you implement a custom painter for complex drawing?

**Difficulty**: Advanced

**Strategy:**
Subclass `CustomPainter` and override `paint()` and `shouldRepaint()`. Use the `Canvas` object to draw paths, shapes, or images. Wrap it in a `CustomPaint` widget.

**Code Example:**
```dart
class MyPainter extends CustomPainter {
  @override
  void paint(Canvas canvas, Size size) {
    final paint = Paint()..color = Colors.blue;
    canvas.drawCircle(Offset(size.width / 2, size.height / 2), 20, paint);
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) => false;
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q8: How do you ensure a widget rebuilds only when specific data changes (Selector)?

**Difficulty**: Intermediate

**Strategy:**
If using `Provider`, use the `Selector` widget. It filters updates by selecting a specific value from the provider model and comparing it to the previous value.

**Code Example:**
```dart
Selector<UserModel, String>(
  selector: (_, model) => model.name, // Only listen to 'name'
  builder: (_, name, __) {
    return Text(name); // Rebuilds ONLY when name changes
  },
);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q9: How do you implement deep linking in Flutter (Navigator 2.0)?

**Difficulty**: Advanced

**Strategy:**
Use `MaterialApp.router` with a `RouterDelegate` and `RouteInformationParser` (or use GoRouter). Configure native AndroidManifest/Info.plist to handle intent filters.

**Code Example:**
```dart
final router = GoRouter(
  routes: [
    GoRoute(
      path: '/details/:id',
      builder: (context, state) => DetailsPage(id: state.params['id']),
    ),
  ],
);

// Native config is still required in android/app/src/main/AndroidManifest.xml
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q10: How do you debug layout issues where widgets have 'unbounded height'?

**Difficulty**: Beginner

**Strategy:**
This usually happens when a `Column` is inside a scrollable widget (like `ListView`). Wrap the `Column` (or the overflowing widget) in `ShrinkWrap` (bad performance) or give it a bounded constraint using `SizedBox`/`Expanded`.

**Code Example:**
```dart
// BAD: ListView > Column (unbounded) > ListView (unbounded)
// GOOD:
ListView(
  children: [
    Text('Header'),
    SizedBox(
      height: 200, // Give explicit constraint
      child: ListView(children: [...]),
    ),
  ],
)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q11: How do you use Keys to preserve widget state when the list order changes?

**Difficulty**: Intermediate

**Strategy:**
Use `ValueKey` or `ObjectKey` when working with collections of stateful widgets. Without keys, Flutter matches widgets by type and position, potentially losing state if items are reordered.

**Code Example:**
```dart
List<Widget> items = [
  ItemWidget(key: ValueKey(1), id: 1),
  ItemWidget(key: ValueKey(2), id: 2),
];
// Even if list is shuffled, state for id=1 is preserved
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q12: How do you implement a theme switch (Dark/Light mode) dynamically?

**Difficulty**: Beginner

**Strategy:**
Store the `ThemeMode` in a state management solution. Pass `theme`, `darkTheme`, and `themeMode` to `MaterialApp`.

**Code Example:**
```dart
MaterialApp(
  theme: ThemeData.light(),
  darkTheme: ThemeData.dark(),
  themeMode: isDarkMode ? ThemeMode.dark : ThemeMode.light,
  home: HomePage(),
);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q13: How do you optimize images by caching them?

**Difficulty**: Beginner

**Strategy:**
Use the `cached_network_image` package. It downloads images, stores them on disk/memory, and displays a placeholder while loading.

**Code Example:**
```dart
CachedNetworkImage(
  imageUrl: "http://via.placeholder.com/350x150",
  placeholder: (context, url) => CircularProgressIndicator(),
  errorWidget: (context, url, error) => Icon(Icons.error),
);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q14: How do you write a unit test for a simple business logic class?

**Difficulty**: Beginner

**Strategy:**
Use the `flutter_test` package. Create a file `test/unit_test.dart`. Use `test()` function and `expect()` to verify results.

**Code Example:**
```dart
void main() {
  test('Counter increments value', () {
    final counter = Counter();
    counter.increment();
    expect(counter.value, 1);
  });
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q15: How do you handle errors globally in Flutter (e.g., crash reporting)?

**Difficulty**: Intermediate

**Strategy:**
Override `FlutterError.onError` for framework errors and use `runZonedGuarded` for async errors. Integrate with Sentry or Firebase Crashlytics.

**Code Example:**
```dart
void main() {
  runZonedGuarded(() {
    runApp(MyApp());
  }, (error, stackTrace) {
    // Send to Crashlytics
    FirebaseCrashlytics.instance.recordError(error, stackTrace);
  });
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q16: How do you perform Dependency Injection using GetIt?

**Difficulty**: Intermediate

**Strategy:**
Use `GetIt` as a service locator to register and retrieve singletons or factories. This decouples implementation from usage, making testing easier.

**Code Example:**
```dart
final getIt = GetIt.instance;

void setup() {
  getIt.registerSingleton<ApiService>(ApiService());
  getIt.registerFactory<HomeViewModel>(() => HomeViewModel(getIt<ApiService>()));
}

// Usage
final viewModel = getIt<HomeViewModel>();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q17: How do you use Flutter Hooks to simplify AnimationController management?

**Difficulty**: Intermediate

**Strategy:**
Use `useAnimationController` from `flutter_hooks` to automatically handle the lifecycle (dispose) of the controller, reducing boilerplate code.

**Code Example:**
```dart
class HookExample extends HookWidget {
  @override
  Widget build(BuildContext context) {
    final controller = useAnimationController(
      duration: const Duration(seconds: 1),
    );
    
    useListenable(controller); // Rebuild on change

    return RotationTransition(
      turns: controller,
      child: Container(color: Colors.red, width: 50, height: 50),
    );
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q18: How do you communicate with native platform code using MethodChannel?

**Difficulty**: Advanced

**Strategy:**
Define a `MethodChannel` with a unique name on both Flutter and Native sides. Use `invokeMethod` from Flutter and `setMethodCallHandler` on Android/iOS to handle calls.

**Code Example:**
```dart
// Flutter
static const platform = MethodChannel('com.example.app/battery');
final int result = await platform.invokeMethod('getBatteryLevel');

// Android (Kotlin)
MethodChannel(flutterEngine.dartExecutor, "com.example.app/battery").setMethodCallHandler { call, result ->
    if (call.method == "getBatteryLevel") {
        result.success(batteryLevel)
    } else {
        result.notImplemented()
    }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q19: How do you handle keyboard visibility and dismissal efficiently?

**Difficulty**: Beginner

**Strategy:**
Use `GestureDetector` wrapping the Scaffold to unfocus the current focus node when tapping outside. Use `MediaQuery.of(context).viewInsets.bottom` to detect keyboard height.

**Code Example:**
```dart
GestureDetector(
  onTap: () => FocusManager.instance.primaryFocus?.unfocus(),
  child: Scaffold(
    body: TextField(decoration: InputDecoration(labelText: 'Tap outside to dismiss')),
  ),
);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q20: How do you implement a SliverAppBar with a floating title?

**Difficulty**: Intermediate

**Strategy:**
Use a `CustomScrollView` with `SliverAppBar`. Set `floating: true` and `pinned: true` to keep the app bar visible or floating as the user scrolls.

**Code Example:**
```dart
CustomScrollView(
  slivers: [
    SliverAppBar(
      title: Text('Sliver App Bar'),
      floating: true,
      pinned: true,
      expandedHeight: 200.0,
      flexibleSpace: FlexibleSpaceBar(
        background: Image.network('https://via.placeholder.com/350', fit: BoxFit.cover),
      ),
    ),
    SliverList(
      delegate: SliverChildBuilderDelegate(
        (context, index) => ListTile(title: Text('Item $index')),
        childCount: 50,
      ),
    ),
  ],
);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q21: How do you make your Flutter app accessible using Semantics?

**Difficulty**: Intermediate

**Strategy:**
Wrap widgets with `Semantics` to provide descriptions for screen readers. Use properties like `label`, `hint`, and `onTap` to describe interactions.

**Code Example:**
```dart
Semantics(
  label: 'Profile Picture',
  hint: 'Double tap to change photo',
  button: true,
  onTap: () => changePhoto(),
  child: CircleAvatar(backgroundImage: NetworkImage(url)),
);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q22: How do you implement internationalization (i18n) using the flutter_localizations package?

**Difficulty**: Intermediate

**Strategy:**
Add `flutter_localizations` dependency. Define ARB files for each language. Generate Dart code using `flutter gen-l10n`. Use `AppLocalizations.of(context)` to access strings.

**Code Example:**
```dart
// l10n.yaml configuration needed
// app_en.arb
{
  "helloWorld": "Hello World!"
}

// Usage
Text(AppLocalizations.of(context)!.helloWorld);

// MaterialApp setup
MaterialApp(
  localizationsDelegates: AppLocalizations.localizationsDelegates,
  supportedLocales: AppLocalizations.supportedLocales,
  home: HomePage(),
);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q23: How do you write an integration test in Flutter?

**Difficulty**: Advanced

**Strategy:**
Use the `integration_test` package. Create a test file in `integration_test/`, initialize `IntegrationTestWidgetsFlutterBinding`, and use `WidgetTester` to interact with the app.

**Code Example:**
```dart
import 'package:integration_test/integration_test.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:my_app/main.dart' as app;

void main() {
  IntegrationTestWidgetsFlutterBinding.ensureInitialized();

  testWidgets('tap on the floating action button, verify counter', (tester) async {
    app.main();
    await tester.pumpAndSettle();

    final Finder fab = find.byTooltip('Increment');
    await tester.tap(fab);
    await tester.pumpAndSettle();

    expect(find.text('1'), findsOneWidget);
  });
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q24: How do you debug performance issues using Flutter DevTools?

**Difficulty**: Intermediate

**Strategy:**
Open DevTools and use the 'Performance' tab. Record a trace to analyze UI (Raster) and UI (Dart) thread frames. Look for jank (red bars) and identify expensive build or layout operations.

**Code Example:**
```dart
// Run app in profile mode for accurate performance data
flutter run --profile

// Then open DevTools
// Inspect 'Frame Analysis' to see if 'Build', 'Layout', or 'Paint' is the bottleneck.
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q25: How do you create a custom animation using TweenAnimationBuilder?

**Difficulty**: Intermediate

**Strategy:**
Use `TweenAnimationBuilder` for simple implicit animations without managing a controller. Define a `Tween` (start/end values) and a `builder` to apply the value.

**Code Example:**
```dart
TweenAnimationBuilder<double>(
  tween: Tween<double>(begin: 0, end: 1),
  duration: const Duration(seconds: 2),
  builder: (context, value, child) {
    return Opacity(
      opacity: value,
      child: Padding(
        padding: EdgeInsets.all(value * 20),
        child: child,
      ),
    );
  },
  child: const Text('Fade In & Move'),
);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q26: How do you display a floating widget using OverlayEntry?

**Difficulty**: Advanced

**Strategy:**
Insert an `OverlayEntry` into the `Overlay` of the current context. Remember to remove the entry when it's no longer needed.

**Code Example:**
```dart
void showFloatingWidget(BuildContext context) {
  OverlayEntry entry;
  entry = OverlayEntry(
    builder: (context) => Positioned(
      top: 100,
      right: 20,
      child: Material(
        child: Text('Floating!'),
      ),
    ),
  );

  Overlay.of(context).insert(entry);
  
  // Remove later: entry.remove();
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q27: How do you optimize rebuilds with ValueListenableBuilder?

**Difficulty**: Beginner

**Strategy:**
Use `ValueListenableBuilder` to listen to a `ValueNotifier`. This rebuilds only the builder part of the widget tree when the value changes, avoiding full widget rebuilds.

**Code Example:**
```dart
final ValueNotifier<int> _counter = ValueNotifier<int>(0);

@override
Widget build(BuildContext context) {
  return Scaffold(
    body: ValueListenableBuilder<int>(
      valueListenable: _counter,
      builder: (context, value, child) {
        // Only this part rebuilds
        return Text('$value');
      },
    ),
    floatingActionButton: FloatingActionButton(
      onPressed: () => _counter.value++,
    ),
  );
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q28: How do you handle asynchronous data in Riverpod with AsyncValue?

**Difficulty**: Intermediate

**Strategy:**
Use `ref.watch(provider)` which returns an `AsyncValue`. Use `.when()` to handle `data`, `loading`, and `error` states gracefully in the UI.

**Code Example:**
```dart
final userProvider = FutureProvider<User>((ref) async {
  return fetchUser();
});

class UserWidget extends ConsumerWidget {
  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final userAsync = ref.watch(userProvider);

    return userAsync.when(
      data: (user) => Text(user.name),
      loading: () => CircularProgressIndicator(),
      error: (err, stack) => Text('Error: $err'),
    );
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q29: How do you validate a Form in Flutter?

**Difficulty**: Beginner

**Strategy:**
Wrap `TextFormField` widgets in a `Form` widget. Use a `GlobalKey<FormState>`. Assign `validator` functions to fields. Call `_formKey.currentState!.validate()` to check all fields.

**Code Example:**
```dart
final _formKey = GlobalKey<FormState>();

Form(
  key: _formKey,
  child: Column(
    children: [
      TextFormField(
        validator: (value) {
          if (value == null || value.isEmpty) return 'Please enter text';
          return null;
        },
      ),
      ElevatedButton(
        onPressed: () {
          if (_formKey.currentState!.validate()) {
            // Process data
          }
        },
        child: Text('Submit'),
      ),
    ],
  ),
);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q30: How do you embed a native Android/iOS view in Flutter?

**Difficulty**: Advanced

**Strategy:**
Use `AndroidView` (or `PlatformViewLink`) for Android and `UiKitView` for iOS. This allows rendering native components directly within the Flutter widget tree.

**Code Example:**
```dart
// Android
AndroidView(
  viewType: 'plugins.example.com/native_view',
  creationParams: <String, dynamic>{'id': 1},
  creationParamsCodec: const StandardMessageCodec(),
);

// iOS
UiKitView(
  viewType: 'plugins.example.com/native_view',
  creationParams: <String, dynamic>{'id': 1},
  creationParamsCodec: const StandardMessageCodec(),
);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---


### Q31: How do you implement Pull-to-Refresh functionality?

**Difficulty**: Beginner

**Strategy:**
Wrap a scrollable widget (like `ListView`) in a `RefreshIndicator`. Provide an `onRefresh` callback that returns a Future.

**Code Example:**
RefreshIndicator(
  onRefresh: () async {
    await Future.delayed(const Duration(seconds: 1));
    // Update data
  },
  child: ListView(children: [...]),
)

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q32: How do you create a Hero animation between two screens?

**Difficulty**: Intermediate

**Strategy:**
Wrap the shared element (e.g., image) in a `Hero` widget with the same `tag` on both the source and destination screens.

**Code Example:**
// Screen 1
Hero(
  tag: 'profile-pic',
  child: Image.asset('profile.jpg'),
)

// Screen 2
Hero(
  tag: 'profile-pic',
  child: Image.asset('profile.jpg'),
)

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q33: How do you create a rounded image using `ClipRRect`?

**Difficulty**: Beginner

**Strategy:**
Wrap the widget (Image, Container) in a `ClipRRect` and define a `borderRadius`.

**Code Example:**
ClipRRect(
  borderRadius: BorderRadius.circular(20.0),
  child: Image.network('https://example.com/image.jpg'),
)

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q34: How do you create a blur effect (Glassmorphism)?

**Difficulty**: Intermediate

**Strategy:**
Use `BackdropFilter` with an `ImageFilter.blur`. Typically combined with a semi-transparent container.

**Code Example:**
Stack(
  children: [
    Image.network('bg.jpg'),
    BackdropFilter(
      filter: ImageFilter.blur(sigmaX: 5, sigmaY: 5),
      child: Container(color: Colors.black.withOpacity(0.2)),
    ),
  ],
)

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q35: How do you implement Drag and Drop?

**Difficulty**: Intermediate

**Strategy:**
Use `Draggable<T>` for the moving item and `DragTarget<T>` for the drop zone.

**Code Example:**
Draggable<int>(
  data: 10,
  feedback: Container(color: Colors.red, width: 50, height: 50),
  child: Container(color: Colors.blue, width: 50, height: 50),
)

DragTarget<int>(
  onAccept: (data) => print('Accepted $data'),
  builder: (context, candidates, rejects) {
    return Container(width: 100, height: 100, color: Colors.green);
  },
)

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q36: How do you allow users to pinch-to-zoom and pan an image?

**Difficulty**: Intermediate

**Strategy:**
Wrap the content in an `InteractiveViewer` widget.

**Code Example:**
InteractiveViewer(
  minScale: 0.5,
  maxScale: 4.0,
  child: Image.asset('map.png'),
)

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q37: How do you implement a page view (swiping between screens)?

**Difficulty**: Beginner

**Strategy:**
Use `PageView` or `PageView.builder`. Use a `PageController` to control the current page programmatically.

**Code Example:**
final controller = PageController(initialPage: 0);

PageView(
  controller: controller,
  children: [
    Container(color: Colors.red),
    Container(color: Colors.green),
    Container(color: Colors.blue),
  ],
)

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q38: How do you create a Tab Bar layout?

**Difficulty**: Beginner

**Strategy:**
Use `DefaultTabController` (simplest) wrapping a `Scaffold`. Place `TabBar` in the `appBar` and `TabBarView` in the `body`.

**Code Example:**
DefaultTabController(
  length: 3,
  child: Scaffold(
    appBar: AppBar(
      bottom: TabBar(tabs: [Tab(text: 'A'), Tab(text: 'B'), Tab(text: 'C')]),
    ),
    body: TabBarView(
      children: [PageA(), PageB(), PageC()],
    ),
  ),
)

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q39: How do you implement search functionality using `SearchDelegate`?

**Difficulty**: Intermediate

**Strategy:**
Create a class extending `SearchDelegate`. Use `showSearch(context: context, delegate: MySearchDelegate())`.

**Code Example:**
class MySearchDelegate extends SearchDelegate {
  @override
  List<Widget> buildActions(BuildContext context) => [IconButton(icon: Icon(Icons.clear), onPressed: () => query = '')];

  @override
  Widget buildLeading(BuildContext context) => IconButton(icon: Icon(Icons.arrow_back), onPressed: () => close(context, null));

  @override
  Widget buildResults(BuildContext context) => Text('Result: $query');

  @override
  Widget buildSuggestions(BuildContext context) => Text('Suggestions for $query');
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q40: How do you use `InheritedWidget` to pass data down the tree?

**Difficulty**: Advanced

**Strategy:**
Subclass `InheritedWidget`, implement `updateShouldNotify`. Child widgets access data via `context.dependOnInheritedWidgetOfExactType`.

**Code Example:**
class MyColor extends InheritedWidget {
  final Color color;
  MyColor({required this.color, required Widget child}) : super(child: child);

  @override
  bool updateShouldNotify(MyColor oldWidget) => color != oldWidget.color;

  static MyColor? of(BuildContext context) => context.dependOnInheritedWidgetOfExactType<MyColor>();
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q41: How do you handle keyboard shortcuts (Web/Desktop)?

**Difficulty**: Intermediate

**Strategy:**
Use the `Shortcuts` and `Actions` widgets, or `CallbackShortcuts` for simpler cases.

**Code Example:**
CallbackShortcuts(
  bindings: {
    const SingleActivator(LogicalKeyboardKey.keyS, control: true): () => save(),
  },
  child: Focus(autofocus: true, child: Container()),
)

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q42: How do you group multiple semantics into one (`MergeSemantics`)?

**Difficulty**: Intermediate

**Strategy:**
Wrap a widget subtree in `MergeSemantics` so screen readers treat it as a single focusable element (e.g., a custom list item with text and icon).

**Code Example:**
MergeSemantics(
  child: Row(
    children: [
      Text('Title'),
      Text('Subtitle'), // Read together as "Title, Subtitle"
    ],
  ),
)

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q43: How do you create a gradient text effect?

**Difficulty**: Intermediate

**Strategy:**
Use `ShaderMask` to paint a gradient over the text.

**Code Example:**
ShaderMask(
  shaderCallback: (bounds) => LinearGradient(
    colors: [Colors.blue, Colors.red],
  ).createShader(bounds),
  child: Text(
    'Gradient Text',
    style: TextStyle(color: Colors.white, fontSize: 40),
  ),
)

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q44: How do you use `RepaintBoundary` to improve performance?

**Difficulty**: Advanced

**Strategy:**
Wrap a widget in `RepaintBoundary` if it repaints frequently (e.g., animation) but its parent does not. This isolates the painting layer.

**Code Example:**
RepaintBoundary(
  child: CircularProgressIndicator(), // Repaints independently of the rest of the UI
)

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q45: What is the difference between `Offstage`, `Visibility`, and `Opacity`?

**Difficulty**: Intermediate

**Strategy:**
- `Offstage`: Lays out but doesn't paint/hit-test (hidden but takes space logic depends on parent).
- `Visibility`: Can hide, not paint, and remove from layout (`gone`).
- `Opacity`: Paints fully transparent (expensive if 0, still takes space/hits).

**Code Example:**
Visibility(
  visible: false,
  maintainState: true, // Keeps state
  child: Text('Hidden'),
)

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q46: What is the difference between `Flexible` and `Expanded`?

**Difficulty**: Beginner

**Strategy:**
`Expanded` forces the child to fill available space (`flex: 1`, `fit: FlexFit.tight`). `Flexible` allows the child to size itself up to the available space (default `fit: FlexFit.loose`).

**Code Example:**
Row(
  children: [
    Expanded(child: Container(color: Colors.red)), // Fills space
    Flexible(child: Container(color: Colors.blue)), // Sizes to child
  ],
)

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q47: How do you make responsive layouts based on parent size (`LayoutBuilder`)?

**Difficulty**: Intermediate

**Strategy:**
Use `LayoutBuilder` to get `BoxConstraints` of the parent. `MediaQuery` gets screen size.

**Code Example:**
LayoutBuilder(
  builder: (context, constraints) {
    if (constraints.maxWidth > 600) {
      return WideLayout();
    } else {
      return NarrowLayout();
    }
  },
)

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q48: How do you size a widget relative to its parent (`FractionallySizedBox`)?

**Difficulty**: Intermediate

**Strategy:**
Use `FractionallySizedBox` to size a child as a fraction (percentage) of the available space.

**Code Example:**
Container(
  height: 200,
  width: 200,
  child: FractionallySizedBox(
    widthFactor: 0.5, // 50% of parent width
    heightFactor: 0.5,
    child: Container(color: Colors.red),
  ),
)

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q49: How do you create complex flow layouts (`Flow`)?

**Difficulty**: Advanced

**Strategy:**
Use the `Flow` widget with a `FlowDelegate`. It's highly optimized for transformations and positioning of children during animation.

**Code Example:**
Flow(
  delegate: MyFlowDelegate(),
  children: menuItems,
)

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q50: How do you check if the device is online?

**Difficulty**: Intermediate

**Strategy:**
Use the `connectivity_plus` package (check network type) or `internet_connection_checker` (ping test).

**Code Example:**
import 'package:connectivity_plus/connectivity_plus.dart';

final connectivityResult = await (Connectivity().checkConnectivity());
if (connectivityResult == ConnectivityResult.mobile) {
  // I am connected to a mobile network.
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

