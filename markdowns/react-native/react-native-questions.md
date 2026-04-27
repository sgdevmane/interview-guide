<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/react-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>React Native Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for developers</b></p>
</div>

---

## Table of Contents

1. [How do you optimize the performance of a long FlatList with thousands of items?](#q1-how-do-you-optimize-the-performance-of-a-long-flatlist-with-thousands-of-items) <span class="advanced">Advanced</span>
2. [How do you implement platform-specific code for iOS and Android?](#q2-how-do-you-implement-platform-specific-code-for-ios-and-android) <span class="beginner">Beginner</span>
3. [How do you handle deep linking in a React Native app using React Navigation?](#q3-how-do-you-handle-deep-linking-in-a-react-native-app-using-react-navigation) <span class="intermediate">Intermediate</span>
4. [How do you implement high-performance animations using React Native Reanimated?](#q4-how-do-you-implement-high-performance-animations-using-react-native-reanimated) <span class="advanced">Advanced</span>
5. [How do you persist global state data using AsyncStorage?](#q5-how-do-you-persist-global-state-data-using-asyncstorage) <span class="beginner">Beginner</span>
6. [How do you create a custom Native Module for Android (Java/Kotlin)?](#q6-how-do-you-create-a-custom-native-module-for-android-javakotlin) <span class="expert">Expert</span>
7. [How do you handle safe area insets on devices with notches?](#q7-how-do-you-handle-safe-area-insets-on-devices-with-notches) <span class="beginner">Beginner</span>
8. [How do you debug React Native apps effectively?](#q8-how-do-you-debug-react-native-apps-effectively) <span class="intermediate">Intermediate</span>
9. [How do you prevent the on-screen keyboard from covering input fields?](#q9-how-do-you-prevent-the-on-screen-keyboard-from-covering-input-fields) <span class="intermediate">Intermediate</span>
10. [How do you implement an infinite scroll list?](#q10-how-do-you-implement-an-infinite-scroll-list) <span class="intermediate">Intermediate</span>
11. [How do you use custom fonts in React Native (CLI workflow)?](#q11-how-do-you-use-custom-fonts-in-react-native-cli-workflow) <span class="intermediate">Intermediate</span>
12. [How do you handle offline network connectivity?](#q12-how-do-you-handle-offline-network-connectivity) <span class="intermediate">Intermediate</span>
13. [How do you optimize image loading and caching?](#q13-how-do-you-optimize-image-loading-and-caching) <span class="intermediate">Intermediate</span>
14. [How do you create a translucent status bar on Android?](#q14-how-do-you-create-a-translucent-status-bar-on-android) <span class="intermediate">Intermediate</span>
15. [How do you upgrade React Native to a newer version?](#q15-how-do-you-upgrade-react-native-to-a-newer-version) <span class="advanced">Advanced</span>
16. [How do you implement Stack Navigation using React Navigation?](#q16-how-do-you-implement-stack-navigation-using-react-navigation) <span class="beginner">Beginner</span>
17. [How do you use Redux Toolkit in React Native?](#q17-how-do-you-use-redux-toolkit-in-react-native) <span class="intermediate">Intermediate</span>
18. [How do you use Context API for theming?](#q18-how-do-you-use-context-api-for-theming) <span class="intermediate">Intermediate</span>
19. [What is the difference between Expo Managed and Bare workflows?](#q19-what-is-the-difference-between-expo-managed-and-bare-workflows) <span class="beginner">Beginner</span>
20. [How do you enable Hermes Engine on Android?](#q20-how-do-you-enable-hermes-engine-on-android) <span class="intermediate">Intermediate</span>
21. [What are TurboModules?](#q21-what-are-turbomodules) <span class="advanced">Advanced</span>
22. [What is the Fabric Renderer?](#q22-what-is-the-fabric-renderer) <span class="advanced">Advanced</span>
23. [How do you handle Push Notifications with Firebase (FCM)?](#q23-how-do-you-handle-push-notifications-with-firebase-fcm) <span class="intermediate">Intermediate</span>
24. [How do you integrate Google Maps?](#q24-how-do-you-integrate-google-maps) <span class="intermediate">Intermediate</span>
25. [How do you capture a photo using the Camera?](#q25-how-do-you-capture-a-photo-using-the-camera) <span class="intermediate">Intermediate</span>
26. [How do you implement Biometric Authentication?](#q26-how-do-you-implement-biometric-authentication) <span class="intermediate">Intermediate</span>
27. [How do you make a custom button accessible?](#q27-how-do-you-make-a-custom-button-accessible) <span class="beginner">Beginner</span>
28. [How do you implement Internationalization (i18n)?](#q28-how-do-you-implement-internationalization-i18n) <span class="intermediate">Intermediate</span>
29. [How do you perform Over-the-Air (OTA) updates?](#q29-how-do-you-perform-over-the-air-ota-updates) <span class="advanced">Advanced</span>
30. [How do you display a WebView?](#q30-how-do-you-display-a-webview) <span class="beginner">Beginner</span>
31. [How do you render SVG images?](#q31-how-do-you-render-svg-images) <span class="intermediate">Intermediate</span>
32. [How do you handle complex gestures (Drag/Swipe)?](#q32-how-do-you-handle-complex-gestures-dragswipe) <span class="intermediate">Intermediate</span>
33. [How do you share content with other apps?](#q33-how-do-you-share-content-with-other-apps) <span class="beginner">Beginner</span>
34. [How do you detect App State changes (Background/Active)?](#q34-how-do-you-detect-app-state-changes-backgroundactive) <span class="beginner">Beginner</span>
35. [How do you open the device Settings?](#q35-how-do-you-open-the-device-settings) <span class="beginner">Beginner</span>
36. [How do you securely store sensitive data (Tokens)?](#q36-how-do-you-securely-store-sensitive-data-tokens) <span class="intermediate">Intermediate</span>
37. [How do you use Vector Icons?](#q37-how-do-you-use-vector-icons) <span class="beginner">Beginner</span>
38. [How do you display Lottie animations?](#q38-how-do-you-display-lottie-animations) <span class="intermediate">Intermediate</span>
39. [How do you implement a Blur effect?](#q39-how-do-you-implement-a-blur-effect) <span class="intermediate">Intermediate</span>
40. [How do you implement a Linear Gradient?](#q40-how-do-you-implement-a-linear-gradient) <span class="beginner">Beginner</span>
41. [How do you handle the hardware back button on Android?](#q41-how-do-you-handle-the-hardware-back-button-on-android) <span class="beginner">Beginner</span>
42. [How do you get device information (Model, System Version)?](#q42-how-do-you-get-device-information-model-system-version) <span class="beginner">Beginner</span>
43. [How do you copy text to the clipboard?](#q43-how-do-you-copy-text-to-the-clipboard) <span class="beginner">Beginner</span>
44. [How do you implement a modal?](#q44-how-do-you-implement-a-modal) <span class="beginner">Beginner</span>
45. [How do you check internet connectivity type (WiFi/Cellular)?](#q45-how-do-you-check-internet-connectivity-type-wificellular) <span class="beginner">Beginner</span>
46. [How do you implement a Pager View (ViewPager)?](#q46-how-do-you-implement-a-pager-view-viewpager) <span class="intermediate">Intermediate</span>
47. [How do you debug Network Requests?](#q47-how-do-you-debug-network-requests) <span class="intermediate">Intermediate</span>
48. [How do you use Native Driver for Animations?](#q48-how-do-you-use-native-driver-for-animations) <span class="intermediate">Intermediate</span>
49. [How do you measure the dimensions of a View?](#q49-how-do-you-measure-the-dimensions-of-a-view) <span class="beginner">Beginner</span>
50. [How do you implement a Shadow on Android?](#q50) <span class="beginner">Beginner</span>

---
<a id="q1"></a>
### Q1: How do you optimize the performance of a long FlatList with thousands of items?

**Difficulty**: Advanced

**Strategy**: FlatList performance is critical in production apps because rendering thousands of items naively causes severe frame drops and memory spikes. The key approach is to minimize the number of mounted views, skip unnecessary layout calculations, and batch render cycles. A common pitfall is neglecting `getItemLayout` when items have a fixed height -- without it, FlatList measures every item asynchronously, which is expensive. Always pair these props with `React.memo` on your `renderItem` component to avoid re-rendering unchanged items.

**Strategy:**
1.  **getItemLayout**: Skip measurement calculation.
2.  **windowSize**: Reduce render window (default 21).
3.  **removeClippedSubviews**: Unmount off-screen views (Android).
4.  **initialNumToRender**: Render fewer items initially.
5.  **maxToRenderPerBatch**: Control batch size.
6.  **Memoization**: Use `React.memo` for renderItem.

**Code Example:**
```javascript
const renderItem = React.useCallback(({ item }) => <Item title={item.title} />, []);

<FlatList
  data={data}
  renderItem={renderItem}
  keyExtractor={item => item.id}
  getItemLayout={(data, index) => (
    {length: ITEM_HEIGHT, offset: ITEM_HEIGHT * index, index}
  )}
  windowSize={5}
  initialNumToRender={10}
  maxToRenderPerBatch={10}
  removeClippedSubviews={true}
/>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q2"></a>
### Q2: How do you implement platform-specific code for iOS and Android?

**Difficulty**: Beginner

**Strategy**: Platform-specific code is essential because iOS and Android have different design conventions, APIs, and styling behaviors. React Native provides two main approaches: inline platform checks for small differences and file-based splitting for entirely divergent implementations. A common mistake is using `Platform.OS` checks scattered throughout your codebase when a `.ios.js` / `.android.js` file extension approach would be cleaner and more maintainable.

**Strategy:**
1.  **Platform.select/Platform.OS:** For minor logic/style differences.
2.  **File Extensions:** `Component.ios.js` and `Component.android.js` for completely different implementations.

**Code Example:**
```javascript
import { Platform, StyleSheet } from 'react-native';

const styles = StyleSheet.create({
  container: {
    ...Platform.select({
      ios: { shadowColor: 'black', shadowOffset: { width: 0, height: 2 } },
      android: { elevation: 5 }
    })
  }
});

// Logic
if (Platform.OS === 'ios') {
  // iOS specific logic
}
```

---

<a id="q3"></a>
### Q3: How do you handle deep linking in a React Native app using React Navigation?

**Difficulty**: Intermediate

**Strategy**: Deep linking is a fundamental feature for user engagement, enabling push notifications, email links, and shared URLs to open specific screens within your app. Interviewers ask this to verify you understand the full flow from native platform URL handling through to React Navigation screen resolution. A key pitfall is forgetting to configure URL schemes in the native `AndroidManifest.xml` and `Info.plist` -- without these, the OS will never route URLs to your app in the first place.

**Strategy:**
Configure the `linking` prop in the NavigationContainer with prefixes and a config object mapping paths to screens.

**Code Example:**
```javascript
const linking = {
  prefixes: ['myapp://', 'https://myapp.com'],
  config: {
    screens: {
      Home: 'home',
      Profile: {
        path: 'user/:id',
        parse: { id: (id) => `${id}` },
      },
    },
  },
};

<NavigationContainer linking={linking}>
  {/* ... */}
</NavigationContainer>
```

---

<a id="q4"></a>
### Q4: How do you implement high-performance animations using React Native Reanimated?

**Difficulty**: Advanced

**Strategy**: The Animated API that ships with React Native runs animations on the JavaScript thread, which causes jank whenever JS is busy. Reanimated solves this by executing animations directly on the native UI thread using shared values and worklets. This distinction is critical in interviews because it demonstrates you understand the bridge bottleneck and can choose the right tool for fluid 60fps animations, especially for gestures and complex transitions.

**Strategy:**
Use `useSharedValue` for state and `useAnimatedStyle` to run animations on the UI thread, bypassing the JS bridge.

**Code Example:**
```javascript
import Animated, { useSharedValue, useAnimatedStyle, withSpring } from 'react-native-reanimated';

function Box() {
  const offset = useSharedValue(0);

  const animatedStyles = useAnimatedStyle(() => {
    return {
      transform: [{ translateX: offset.value }],
    };
  });

  return (
    <Button onPress={() => (offset.value = withSpring(Math.random() * 255))}>
      <Animated.View style={[styles.box, animatedStyles]} />
    </Button>
  );
}
```

---

<a id="q5"></a>
### Q5: How do you persist global state data using AsyncStorage?

**Difficulty**: Beginner

**Strategy**: Persisting state across app restarts is essential for user experience -- think saved preferences, onboarding flags, and cached user data. AsyncStorage is an unencrypted, asynchronous key-value store, so it is fine for non-sensitive data but should never hold tokens or secrets. A best practice is to create a custom hook or middleware layer that handles serialization, error handling, and default values so your components stay clean.

**Strategy:**
Use `AsyncStorage.setItem` (stringified) and `AsyncStorage.getItem` (parsed). Ideally, wrap this in a custom hook or state management middleware.

**Code Example:**
```javascript
import AsyncStorage from '@react-native-async-storage/async-storage';

const storeData = async (value) => {
  try {
    const jsonValue = JSON.stringify(value);
    await AsyncStorage.setItem('@storage_Key', jsonValue);
  } catch (e) {
    // saving error
  }
};

const getData = async () => {
  try {
    const jsonValue = await AsyncStorage.getItem('@storage_Key');
    return jsonValue != null ? JSON.parse(jsonValue) : null;
  } catch (e) {
    // error reading value
  }
};
```

---

<a id="q6"></a>
### Q6: How do you create a custom Native Module for Android (Java/Kotlin)?

**Difficulty**: Expert

**Strategy**: Native modules are the bridge between JavaScript and platform-specific capabilities that have no RN equivalent -- Bluetooth, ARKit, payment SDKs, and other hardware or OS-level features. This topic tests whether you can step outside the JavaScript layer and work with the underlying native code. A common pitfall is forgetting to register the module in a package and add that package to the `getPackages()` array, which silently causes the module to be unavailable in JS.

**Strategy:**
1.  Create a Java/Kotlin class extending `ReactContextBaseJavaModule`.
2.  Annotate methods with `@ReactMethod`.
3.  Register the module in a `ReactPackage`.

**Code Example (Kotlin):**
```kotlin
class CalendarModule(reactContext: ReactApplicationContext) : ReactContextBaseJavaModule(reactContext) {
    override fun getName() = "CalendarModule"

    @ReactMethod
    fun createCalendarEvent(name: String, location: String) {
        Log.d("CalendarModule", "Create event called with name: $name and location: $location")
    }
}
```

---

<a id="q7"></a>
### Q7: How do you handle safe area insets on devices with notches?

**Difficulty**: Beginner

**Strategy**: Modern devices have notches, dynamic islands, and rounded corners that can clip or overlap your content. Ignoring safe area insets leads to unusable UI on iPhones and certain Android devices. The community library `react-native-safe-area-context` is preferred over the built-in `SafeAreaView` because it provides a `useSafeAreaInsets` hook for granular padding control and works correctly with modal screens and nested navigators.

**Strategy:**
Use `SafeAreaView` from `react-native-safe-area-context` (preferred over the built-in one) or `useSafeAreaInsets` hook.

**Code Example:**
```javascript
import { SafeAreaView } from 'react-native-safe-area-context';

function App() {
  return (
    <SafeAreaView style={{ flex: 1, backgroundColor: 'red' }}>
      <View style={{ flex: 1, backgroundColor: 'blue' }}>
        <Text>Content inside safe area</Text>
      </View>
    </SafeAreaView>
  );
}
```

---

<a id="q8"></a>
### Q8: How do you debug React Native apps effectively?

**Difficulty**: Intermediate

**Strategy**: Debugging in React Native is inherently more complex than web development because you deal with two platforms, a JavaScript bridge, and native code. Knowing the right tool for each problem is what interviewers look for -- Flipper for network inspection and layout, React DevTools for component hierarchy, and the in-app performance monitor for frame rate issues. A common mistake is leaving `console.log` statements in production, which can degrade performance on Hermes.

**Strategy:**
1.  **React Native Debugger / Flipper:** For Redux, Network, and Component tree.
2.  **Console:** `console.log` (visible in Metro terminal).
3.  **Performance Monitor:** Toggle in Dev Menu.
4.  **LogBox:** Inspect warnings/errors in-app.

**Command:**
Press `Cmd+D` (iOS) or `Cmd+M` (Android) to open the Dev Menu.


---

<a id="q9"></a>
### Q9: How do you prevent the on-screen keyboard from covering input fields?

**Difficulty**: Intermediate

**Strategy**: The on-screen keyboard covering input fields is one of the most common UX complaints in mobile apps and a reliable interview question. `KeyboardAvoidingView` adjusts the view position when the keyboard appears, but its `behavior` prop behaves differently per platform -- `padding` works best on iOS while `height` is more reliable on Android. A frequent pitfall is nesting multiple `KeyboardAvoidingView` wrappers, which causes unpredictable offset calculations.

**Strategy:**
Use `KeyboardAvoidingView`. Adjust `behavior` prop based on platform (`padding` for iOS, `height` for Android often works best).

**Code Example:**
```javascript
<KeyboardAvoidingView
  behavior={Platform.OS === "ios" ? "padding" : "height"}
  style={styles.container}
>
  <TouchableWithoutFeedback onPress={Keyboard.dismiss}>
    <View style={styles.inner}>
      <TextInput placeholder="Username" style={styles.textInput} />
    </View>
  </TouchableWithoutFeedback>
</KeyboardAvoidingView>
```

---

<a id="q10"></a>
### Q10: How do you implement an infinite scroll list?

**Difficulty**: Intermediate

**Strategy**: Infinite scroll is a standard UX pattern for feeds, chat histories, and any paginated data set. The key is using `onEndReached` as a trigger to fetch the next page while managing loading states and duplicate requests. A common pitfall is not guarding against multiple simultaneous fetches -- always use a loading flag and reset it in both the success and error callbacks to prevent overlapping API calls.

**Strategy:**
Use `onEndReached` and `onEndReachedThreshold` props of `FlatList` to trigger a fetch function.

**Code Example:**
```javascript
<FlatList
  data={data}
  renderItem={renderItem}
  onEndReached={fetchMoreData}
  onEndReachedThreshold={0.5} // Trigger when half a screen away from end
  ListFooterComponent={loading ? <ActivityIndicator /> : null}
/>
```

---

<a id="q11"></a>
### Q11: How do you use custom fonts in React Native (CLI workflow)?

**Difficulty**: Intermediate

**Strategy**: Custom fonts are a frequent branding requirement and a topic that tests your familiarity with native linking in React Native CLI projects. The process involves placing font files in an assets directory, configuring the asset path in `react-native.config.js`, and running the link command. A common pitfall is using an incorrect `fontFamily` name -- it must match the font's internal name, not necessarily the file name, and iOS and Android can resolve font names differently.

**Strategy:**
1.  Add font files to `assets/fonts`.
2.  Create `react-native.config.js` to link assets.
3.  Run `npx react-native-asset`.
4.  Use `fontFamily: 'FontFileName'`.

**Code Example:**
```javascript
// react-native.config.js
module.exports = {
  project: {
    ios: {},
    android: {},
  },
  assets: ['./assets/fonts/'],
};
```

---

<a id="q12"></a>
### Q12: How do you handle offline network connectivity?

**Difficulty**: Intermediate

**Strategy**: Handling offline scenarios is essential for mobile apps since users frequently lose connectivity in transit, tunnels, or dead zones. A robust approach involves subscribing to network state changes and combining that with local data caching or queue mechanisms. A best practice is to show a non-intrusive banner when connectivity drops and gracefully retry queued network requests when the connection is restored, rather than blocking the entire UI.

**Strategy:**
Use `@react-native-community/netinfo` to subscribe to network state changes.

**Code Example:**
```javascript
import NetInfo from "@react-native-community/netinfo";

useEffect(() => {
  const unsubscribe = NetInfo.addEventListener(state => {
    console.log("Is connected?", state.isConnected);
  });
  return () => unsubscribe();
}, []);
```

---

<a id="q13"></a>
### Q13: How do you optimize image loading and caching?

**Difficulty**: Intermediate

**Strategy**: Image loading is a major source of performance issues in React Native because the built-in `Image` component provides minimal cache control and can cause flickering on re-renders. Libraries like `react-native-fast-image` leverage native caching systems (Glide on Android, SDWebImage on iOS) to provide priority-based loading, preloading, and proper cache headers. Always set explicit `width` and `height` on images to avoid layout shifts during loading.

**Strategy:**
Use `react-native-fast-image` for advanced caching, priority, and preloading capabilities, as the default `Image` component has limited caching control.

**Code Example:**
```javascript
import FastImage from 'react-native-fast-image';

<FastImage
    style={{ width: 200, height: 200 }}
    source={{
        uri: 'https://unsplash.it/400/400?image=1',
        priority: FastImage.priority.normal,
    }}
    resizeMode={FastImage.resizeMode.contain}
/>
```

---

<a id="q14"></a>
### Q14: How do you create a translucent status bar on Android?

**Difficulty**: Intermediate

**Strategy**: A translucent status bar lets your app content render behind the system status bar, creating the modern full-screen look users expect on Android. This is especially important for apps with image headers or colored navigation bars. The pitfall is that making the status bar translucent without adding top padding causes content to be obscured, so you must pair it with `SafeAreaView` or manual padding equal to the status bar height.

**Strategy:**
Use the `StatusBar` component with `translucent={true}` and set `backgroundColor` to transparent.

**Code Example:**
```javascript
<StatusBar 
  translucent 
  backgroundColor="transparent" 
  barStyle="dark-content" 
/>
```

---

<a id="q15"></a>
### Q15: How do you upgrade React Native to a newer version?

**Difficulty**: Advanced

**Strategy**: Upgrading React Native is notoriously tricky because the `android/` and `ios/` native folders contain version-specific configurations that conflict when bumped. The React Native Upgrade Helper is the go-to tool because it shows a precise diff between your current and target version for every native file. A best practice is to upgrade one minor version at a time rather than jumping multiple majors, and always test on both platforms after each step.

**Strategy:**
Use the **React Native Upgrade Helper** web tool to see the diff between versions.
Run `npx react-native upgrade` (automated) or manually apply changes to `android/` and `ios/` folders based on the diff.


---

<a id="q16"></a>
### Q16: How do you implement Stack Navigation using React Navigation?

**Difficulty**: Beginner

**Strategy**: Stack navigation is the most fundamental navigation pattern -- it mimics a stack of cards where each new screen is pushed on top and popping returns to the previous one. This is the starting point for nearly every React Native app, so interviewers expect you to know the setup fluently. A best practice is to define your screen components outside the navigator to avoid unnecessary re-renders and to type your navigation parameters with TypeScript for safety.

**Strategy:**
Install `@react-navigation/native` and `@react-navigation/stack`. Wrap screens in `Stack.Navigator`.

**Code Example:**
import { createStackNavigator } from '@react-navigation/stack';

const Stack = createStackNavigator();

function MyStack() {
  return (
    <Stack.Navigator>
      <Stack.Screen name="Home" component={HomeScreen} />
      <Stack.Screen name="Profile" component={ProfileScreen} />
    </Stack.Navigator>
  );
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q17"></a>
### Q17: How do you use Redux Toolkit in React Native?

**Difficulty**: Intermediate

**Strategy**: Redux Toolkit simplifies state management by reducing boilerplate with `createSlice` and enabling immutable updates via Immer under the hood. This is especially valuable in React Native where multiple screens may share complex state like cart data, user profiles, or offline queues. A common pitfall is overusing Redux for local component state -- reserve it for truly global, cross-screen data and keep UI-local state in `useState` or `useReducer`.

**Strategy:**
Create a slice, configure the store, and wrap the app in `Provider`. Use `useSelector` and `useDispatch` hooks.

**Code Example:**
// slice.js
const counterSlice = createSlice({
  name: 'counter',
  initialState: { value: 0 },
  reducers: { increment: state => { state.value += 1 } }
});

// Component
const count = useSelector(state => state.counter.value);
const dispatch = useDispatch();

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q18"></a>
### Q18: How do you use Context API for theming?

**Difficulty**: Intermediate

**Strategy**: Theming via Context API is a lightweight alternative to Redux when you only need to share theme state across your component tree without the overhead of a full state library. The pattern involves creating a context with light/dark values, wrapping your app in a provider, and consuming with `useContext`. A best practice is to also persist the user's theme preference in AsyncStorage so it survives app restarts and to memoize the context value to prevent unnecessary re-renders.

**Strategy:**
Create a `ThemeContext`. Provide the theme value. Consume it using `useContext`.

**Code Example:**
const ThemeContext = createContext('light');

export default function App() {
  return (
    <ThemeContext.Provider value="dark">
      <Toolbar />
    </ThemeContext.Provider>
  );
}

function Toolbar() {
  const theme = useContext(ThemeContext);
  return <Text style={{ color: theme === 'dark' ? 'white' : 'black' }}>Text</Text>;
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q19"></a>
### Q19: What is the difference between Expo Managed and Bare workflows?

**Difficulty**: Beginner

**Strategy**: Understanding the Expo workflow distinction is fundamental because it affects your entire development and deployment pipeline. The managed workflow accelerates development by abstracting away native code, but it limits you to modules included in the Expo SDK or available via config plugins. The bare workflow gives full native access but requires you to manage Xcode and Android Studio projects directly. Choose managed for fast iteration on standard apps and bare when you need custom native modules or deep native configuration.

**Strategy:**
- **Managed:** Expo handles native code. You write only JS. limited native modules support (unless using config plugins/dev client).
- **Bare:** You have full access to android/ios folders. Can use any native code.

**Code Example:**
// Managed (app.json)
{ "expo": { "name": "MyApp" } }

// Bare
// You have android/ and ios/ directories.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q20"></a>
### Q20: How do you enable Hermes Engine on Android?

**Difficulty**: Intermediate

**Strategy**: Hermes is a JavaScript engine optimized for React Native that significantly improves app startup time, reduces memory usage, and decreases download size through bytecode precompilation. Enabling it is one of the simplest high-impact performance wins available. Note that after enabling Hermes you must clean and rebuild the native project, and some libraries that depend on `eval()` or dynamic code execution may have compatibility issues.

**Strategy:**
In `android/app/build.gradle`, set `enableHermes: true`.

**Code Example:**
project.ext.react = [
    enableHermes: true  // clean and rebuild
]

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q21"></a>
### Q21: What are TurboModules?

**Difficulty**: Advanced

**Strategy**: TurboModules represent a core piece of React Native's New Architecture and understanding them signals that you stay current with the framework's evolution. Unlike legacy bridge modules that eagerly initialize all native modules at startup, TurboModules load lazily on demand, which dramatically reduces app launch time. They also communicate through JSI (JavaScript Interface) for synchronous calls, eliminating the asynchronous JSON serialization bottleneck of the old bridge.

**Strategy:**
TurboModules are part of the New Architecture (JSI). They allow lazy loading of native modules and direct C++ to JS communication without the asynchronous bridge serialization overhead.

**Code Example:**
// C++ implementation required for TurboModules
// JS side accesses it synchronously via JSI

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q22"></a>
### Q22: What is the Fabric Renderer?

**Difficulty**: Advanced

**Strategy**: Fabric is the New Architecture's rendering layer and replaces the legacy asynchronous shadow tree management with a synchronous, C++-based system. This matters because it enables concurrent React features like Suspense and Transitions, improves cross-platform interoperability, and allows state updates to be committed synchronously. Interviewers ask about Fabric to gauge whether you understand why the old bridge-based architecture had fundamental performance ceilings.

**Strategy:**
Fabric is the new UI rendering system. It moves rendering logic to C++, improving performance, interoperability with host platforms, and enabling concurrent React features.

**Code Example:**
// Enabled via newArchEnabled=true in gradle/podfile
// Uses JSI to manipulate UI directly

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q23"></a>
### Q23: How do you handle Push Notifications with Firebase (FCM)?

**Difficulty**: Intermediate

**Strategy**: Push notifications are essential for user re-engagement and are almost always required in production mobile apps. The implementation involves three distinct phases: requesting OS-level permissions, registering for a device token via FCM, and handling both foreground and background message listeners. A common pitfall is only handling foreground messages -- you must also configure background handlers and headless tasks for notifications received when the app is terminated.

**Strategy:**
Use `@react-native-firebase/messaging`. Request permission, get token, and listen for messages.

**Code Example:**
import messaging from '@react-native-firebase/messaging';

async function requestUserPermission() {
  const authStatus = await messaging().requestPermission();
  const enabled = authStatus === messaging.AuthorizationStatus.AUTHORIZED;
}

useEffect(() => {
  const unsubscribe = messaging().onMessage(async remoteMessage => {
    Alert.alert('New Message', remoteMessage.notification.body);
  });
  return unsubscribe;
}, []);

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q24"></a>
### Q24: How do you integrate Google Maps?

**Difficulty**: Intermediate

**Strategy**: Map integration is a common requirement for delivery, ride-sharing, and location-aware apps. The `react-native-maps` library wraps Apple Maps and Google Maps behind a unified API, but you must configure API keys separately for each platform in native configuration files. A frequent pitfall is forgetting to enable the Google Maps SDK in the Google Cloud Console or omitting the API key in `AndroidManifest.xml`, which results in a blank map with no error message.

**Strategy:**
Use `react-native-maps`. Configure API key in AndroidManifest and AppDelegate.

**Code Example:**
import MapView, { Marker } from 'react-native-maps';

<MapView
  style={{ flex: 1 }}
  initialRegion={{
    latitude: 37.78825,
    longitude: -122.4324,
    latitudeDelta: 0.0922,
    longitudeDelta: 0.0421,
  }}
>
  <Marker coordinate={{ latitude: 37.78825, longitude: -122.4324 }} />
</MapView>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q25"></a>
### Q25: How do you capture a photo using the Camera?

**Difficulty**: Intermediate

**Strategy**: Camera access is a core feature for apps involving QR scanning, photo sharing, or document capture. The critical first step is always requesting runtime permissions -- failing to handle the denied or restricted states leads to crashes. Libraries like `react-native-vision-camera` offer better performance and frame-level control than older alternatives, making them the preferred choice for production apps that need real-time processing or custom frame capture.

**Strategy:**
Use `react-native-vision-camera` (performance) or `expo-camera`. Request permissions first.

**Code Example:**
import { Camera, useCameraDevices } from 'react-native-vision-camera';

const devices = useCameraDevices();
const device = devices.back;

if (device == null) return <LoadingView />;
return <Camera style={StyleSheet.absoluteFill} device={device} isActive={true} />;

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q26"></a>
### Q26: How do you implement Biometric Authentication?

**Difficulty**: Intermediate

**Strategy**: Biometric authentication (fingerprint, Face ID) adds a critical security layer for banking, healthcare, and any app handling sensitive data. The key approach is to first check device capability with `isEnrolledAsync()` before attempting authentication, since not all devices support biometrics. Always provide a fallback mechanism such as a PIN entry so users with damaged sensors or unenrolled biometrics are not locked out of your app.

**Strategy:**
Use `expo-local-authentication` or `react-native-biometrics`.

**Code Example:**
import * as LocalAuthentication from 'expo-local-authentication';

async function authenticate() {
  const result = await LocalAuthentication.authenticateAsync();
  if (result.success) {
    // Authenticated
  }
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q27"></a>
### Q27: How do you make a custom button accessible?

**Difficulty**: Beginner

**Strategy**: Accessibility is both a legal requirement in many jurisdictions and a mark of professional-quality apps. Custom touchable components do not automatically convey their purpose to screen readers like VoiceOver or TalkBack. The `accessible` prop marks the element as an accessibility node, while `accessibilityLabel` provides the spoken description and `accessibilityHint` explains the action the element performs. Always test with a screen reader enabled to verify your labels make sense in context.

**Strategy:**
Use `accessible`, `accessibilityLabel`, and `accessibilityHint` props.

**Code Example:**
<TouchableOpacity
  accessible={true}
  accessibilityLabel="Tap me"
  accessibilityHint="Navigates to the home screen"
  onPress={handlePress}
>
  <Text>Press me</Text>
</TouchableOpacity>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q28"></a>
### Q28: How do you implement Internationalization (i18n)?

**Difficulty**: Intermediate

**Strategy**: Internationalization is essential for any app targeting users across multiple regions and languages. The `i18next` ecosystem is the industry standard because it provides interpolation, pluralization, lazy-loaded namespaces, and language detection out of the box. A common pitfall is hardcoding strings during development and deferring i18n to late in the project -- always wrap strings in translation functions from the start to avoid a painful refactor later.

**Strategy:**
Use `i18next` and `react-i18next`. Define resources and init.

**Code Example:**
import { useTranslation } from 'react-i18next';

function MyComponent() {
  const { t } = useTranslation();
  return <Text>{t('welcome')}</Text>;
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q29"></a>
### Q29: How do you perform Over-the-Air (OTA) updates?

**Difficulty**: Advanced

**Strategy**: OTA updates allow you to push JavaScript bundle changes directly to users without going through the app store review process, making them invaluable for bug fixes and quick iterations. CodePush wraps your root component and checks for updates on launch or resume, downloading and applying the new bundle in the background. A critical best practice is to always test OTA updates on a staging deployment before promoting to production, and to implement rollback logic in case the update causes crashes.

**Strategy:**
Use `react-native-code-push` (Microsoft) or `expo-updates`.

**Code Example:**
import CodePush from 'react-native-code-push';

let App = () => <Root />;
App = CodePush(App); // Wrap root component

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q30"></a>
### Q30: How do you display a WebView?

**Difficulty**: Beginner

**Strategy**: WebViews are essential when you need to embed existing web content such as payment gateways, terms of service pages, or third-party tools that cannot be rebuilt natively. The `react-native-webview` library is the maintained successor to the built-in WebView and supports JavaScript injection, postMessage communication, and custom headers. A common pitfall is using WebViews for content that should be native -- always prefer native components for core UI and reserve WebViews for truly web-only content.

**Strategy:**
Use `react-native-webview`. Pass a URI or HTML string to the `source` prop.

**Code Example:**
import { WebView } from 'react-native-webview';

<WebView source={{ uri: 'https://reactnative.dev/' }} />

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q31"></a>
### Q31: How do you render SVG images?

**Difficulty**: Intermediate

**Strategy**: SVG support is essential for rendering resolution-independent icons, illustrations, and logos that look crisp on all screen densities. Unlike the web, React Native cannot render SVG natively, so you need `react-native-svg` for component-based SVG and `react-native-svg-transformer` to import `.svg` files directly. A common pitfall is trying to use SVG in `Image` tags without the transformer, which silently fails.

**Strategy:**
Use `react-native-svg`. Import `Svg`, `Path`, `Circle` etc., or use `react-native-svg-transformer` to import .svg files.

**Code Example:**
import Svg, { Circle } from 'react-native-svg';

<Svg height="100" width="100">
  <Circle cx="50" cy="50" r="45" stroke="blue" strokeWidth="2.5" fill="green" />
</Svg>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q32"></a>
### Q32: How do you handle complex gestures (Drag/Swipe)?

**Difficulty**: Intermediate

**Strategy**: Complex gesture handling is critical for interactive UIs like swipeable cards, draggable elements, and pull-to-refresh patterns. The `react-native-gesture-handler` library provides composable gesture primitives that run on the native thread, avoiding JS bridge latency. Always pair gestures with Reanimated for smooth visual feedback, and compose multiple gestures using `Race`, `Simultaneous`, or `Exclusive` to define how they interact.

**Strategy:**
Use `react-native-gesture-handler` (GestureDetector) and `react-native-reanimated`.

**Code Example:**
import { GestureDetector, Gesture } from 'react-native-gesture-handler';

const gesture = Gesture.Pan()
  .onUpdate((e) => {
    offset.value = e.translationX;
  });

<GestureDetector gesture={gesture}>
  <Animated.View />
</GestureDetector>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q33"></a>
### Q33: How do you share content with other apps?

**Difficulty**: Beginner

**Strategy**: The Share API enables users to distribute content from your app to social media, messaging apps, or email without integrating each platform's SDK individually. It is a built-in React Native API that triggers the native sharing sheet on both platforms. A best practice is to provide both a `message` and a `url` in the share payload for richer previews, and to handle the promise result to know whether the user completed or dismissed the share action.

**Strategy:**
Use the built-in `Share` API to trigger the native share sheet.

**Code Example:**
import { Share } from 'react-native';

const onShare = async () => {
  await Share.share({
    message: 'Check out this cool app!',
  });
};

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q34"></a>
### Q34: How do you detect App State changes (Background/Active)?

**Difficulty**: Beginner

**Strategy**: Detecting app state transitions is essential for pausing video playback, stopping location tracking, refreshing data on return, or triggering analytics events. The `AppState` API provides `active`, `background`, and `inactive` states, and you subscribe via `addEventListener` in a `useEffect` hook. A common pitfall is forgetting to remove the subscription on unmount, which causes memory leaks and stale callbacks.

**Strategy:**
Subscribe to `AppState.addEventListener('change', callback)` and clean up on unmount.

**Code Example:**
import { AppState } from 'react-native';

useEffect(() => {
  const subscription = AppState.addEventListener('change', nextAppState => {
    if (nextAppState === 'active') {
      console.log('App is active');
    }
  });
  return () => subscription.remove();
}, []);

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q35"></a>
### Q35: How do you open the device Settings?

**Difficulty**: Beginner

**Strategy**: Directing users to device settings is a common requirement when your app needs permissions (location, notifications, camera) that were previously denied. The `Linking.openSettings()` method deep-links directly to your app's settings page on both iOS and Android. A best practice is to detect the denied permission state first and show an explanatory dialog before sending the user to settings, since they otherwise may not understand why they were redirected.

**Strategy:**
Use `Linking.openSettings()` to navigate to the app's system settings screen.

**Code Example:**
import { Linking } from 'react-native';

<Button title="Open Settings" onPress={() => Linking.openSettings()} />

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q36"></a>
### Q36: How do you securely store sensitive data (Tokens)?

**Difficulty**: Intermediate

**Strategy**: Storing authentication tokens, API keys, or user credentials in AsyncStorage is a security risk because it is unencrypted and readable by anyone with physical device access. Secure storage libraries use the iOS Keychain and Android Keystore, which provide hardware-backed encryption. A critical best practice is to never store refresh tokens in plain AsyncStorage and to always clear secure storage on logout to prevent token reuse attacks.

**Strategy:**
Do NOT use AsyncStorage. Use `expo-secure-store` or `react-native-keychain` or `react-native-encrypted-storage`.

**Code Example:**
import * as SecureStore from 'expo-secure-store';

await SecureStore.setItemAsync('secure_token', 'secret-value');
const token = await SecureStore.getItemAsync('secure_token');

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q37"></a>
### Q37: How do you use Vector Icons?

**Difficulty**: Beginner

**Strategy**: Vector icons are a staple of mobile UI for navigation tabs, action buttons, and status indicators. The `react-native-vector-icons` library bundles popular icon sets like FontAwesome, Material Icons, and Ionicons, rendering them as native vector graphics that scale perfectly. A common pitfall is not linking the font assets after installation -- you must run the link command or manually add fonts to your Xcode and Android Studio projects.

**Strategy:**
Install `react-native-vector-icons`, link font assets, and use the icon component with a `name` prop.

**Code Example:**
import Icon from 'react-native-vector-icons/FontAwesome';

<Icon name="rocket" size={30} color="#900" />

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q38"></a>
### Q38: How do you display Lottie animations?

**Difficulty**: Intermediate

**Strategy**: Lottie animations provide a way to render complex, designer-created After Effects animations as lightweight JSON files instead of GIFs or video, resulting in smaller bundle sizes and resolution-independent playback. This makes them ideal for loading states, onboarding flows, and success celebrations. A best practice is to preload animations that appear on app launch and to use hardware-accelerated rendering on Android for smoother playback.

**Strategy:**
Use `lottie-react-native`. Import the JSON file.

**Code Example:**
import LottieView from 'lottie-react-native';

<LottieView source={require('./animation.json')} autoPlay loop />

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q39"></a>
### Q39: How do you implement a Blur effect?

**Difficulty**: Intermediate

**Strategy**: Blur effects are commonly used for privacy screens, modal overlays, and the frosted-glass aesthetic popular in modern mobile UI design. The `@react-native-community/blur` library provides a native `BlurView` that leverages platform blur APIs for GPU-accelerated rendering. Be mindful that excessive blur amounts can cause performance issues on older devices, so test on lower-end hardware and limit blur usage to visible areas.

**Strategy:**
Use `@react-native-community/blur` (BlurView).

**Code Example:**
import { BlurView } from "@react-native-community/blur";

<BlurView
  style={styles.absolute}
  blurType="light"
  blurAmount={10}
/>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q40"></a>
### Q40: How do you implement a Linear Gradient?

**Difficulty**: Beginner

**Strategy**: Linear gradients are used extensively for buttons, headers, backgrounds, and branding elements. React Native does not include a gradient component, so `react-native-linear-gradient` (or `expo-linear-gradient`) fills that gap with a native implementation that performs well. A common pitfall is forgetting that the `colors` prop requires an array of valid CSS color strings, and that gradient direction is controlled by `start` and `end` coordinate objects rather than CSS angle values.

**Strategy:**
Use `react-native-linear-gradient` (or `expo-linear-gradient`).

**Code Example:**
import LinearGradient from 'react-native-linear-gradient';

<LinearGradient colors={['#4c669f', '#3b5998', '#192f6a']} style={styles.linearGradient}>
  <Text>Sign in with Facebook</Text>
</LinearGradient>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q41"></a>
### Q41: How do you handle the hardware back button on Android?

**Difficulty**: Beginner

**Strategy**: Android devices have a hardware or gesture-based back button that by default exits the app or pops the current screen, which may not always be the desired behavior. Using `BackHandler.addEventListener`, you can intercept the press and implement custom logic like showing a confirmation dialog before exiting or navigating back within a webview. Always return `true` from your handler to prevent the default back action, and clean up the listener on unmount to avoid stacking multiple handlers.

**Strategy:**
Listen to `hardwareBackPress` events with `BackHandler` and return `true` to override default behavior.

**Code Example:**
useEffect(() => {
  const backAction = () => {
    Alert.alert("Hold on!", "Are you sure you want to go back?", [
      { text: "Cancel", onPress: () => null, style: "cancel" },
      { text: "YES", onPress: () => BackHandler.exitApp() }
    ]);
    return true; // Prevent default behavior
  };

  const backHandler = BackHandler.addEventListener("hardwareBackPress", backAction);
  return () => backHandler.remove();
}, []);

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q42"></a>
### Q42: How do you get device information (Model, System Version)?

**Difficulty**: Beginner

**Strategy**: Device information is essential for analytics, debugging user-reported issues, and conditionally enabling features based on OS version or device capability. The `react-native-device-info` library provides a comprehensive API for device model, system version, unique identifiers, carrier info, and more. A best practice is to collect device info for error reporting and support tickets, but avoid using device IDs for tracking without user consent to comply with privacy regulations.

**Strategy:**
Use `react-native-device-info` to access model, OS version, and other device properties.

**Code Example:**
import DeviceInfo from 'react-native-device-info';

let systemVersion = DeviceInfo.getSystemVersion();
let model = DeviceInfo.getModel();

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q43"></a>
### Q43: How do you copy text to the clipboard?

**Difficulty**: Beginner

**Strategy**: Clipboard operations are a small but essential UX feature for copy-to-clipboard actions on referral codes, addresses, and transaction details. The `@react-native-clipboard/clipboard` library replaced the deprecated built-in `Clipboard` module and provides both `setString` for writing and `getString` for reading. Always provide user feedback such as a toast or brief highlight when text is copied so users know the action succeeded.

**Strategy:**
Use `@react-native-clipboard/clipboard`.

**Code Example:**
import Clipboard from '@react-native-clipboard/clipboard';

const copyToClipboard = () => {
  Clipboard.setString('hello world');
};

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q44"></a>
### Q44: How do you implement a modal?

**Difficulty**: Beginner

**Strategy**: Modals are fundamental UI patterns for confirmations, bottom sheets, image viewers, and form overlays that need to appear above the current screen. The built-in `Modal` component renders its children above the enclosing `StackNavigator` and supports `animationType`, `transparent`, and `onRequestClose` props. A common pitfall on Android is ignoring `onRequestClose` -- it is required to handle the hardware back button, and omitting it causes a warning.

**Strategy:**
Use the built-in `Modal` component with `visible`, `animationType`, and `onRequestClose` props.

**Code Example:**
<Modal
  animationType="slide"
  transparent={true}
  visible={modalVisible}
  onRequestClose={() => setModalVisible(!modalVisible)}
>
  <View style={styles.centeredView}>
    <View style={styles.modalView}>
      <Text>Hello World!</Text>
    </View>
  </View>
</Modal>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q45"></a>
### Q45: How do you check internet connectivity type (WiFi/Cellular)?

**Difficulty**: Beginner

**Strategy**: Knowing the connectivity type helps you adapt app behavior -- for example, delaying large downloads on cellular to save user data plans, or warning users before streaming HD video on metered connections. The `@react-native-community/netinfo` library provides both a one-time `fetch()` and a subscription-based `addEventListener` for real-time updates. A best practice is to combine connectivity type checks with reachability tests, since being on WiFi does not guarantee internet access.

**Strategy:**
Use `NetInfo.fetch()` to get connection type, or subscribe with `NetInfo.addEventListener()` for live updates.

**Code Example:**
NetInfo.fetch().then(state => {
  console.log('Connection type', state.type);
  console.log('Is connected?', state.isConnected);
});

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q46"></a>
### Q46: How do you implement a Pager View (ViewPager)?

**Difficulty**: Intermediate

**Strategy**: Pager views provide a horizontally or vertically scrollable container for swiping between full-screen pages, commonly used for onboarding flows, image carousels, and tab-like interfaces. The `react-native-pager-view` library wraps the native `ViewPager` on Android and `UIPageViewController` on iOS, delivering smooth, gesture-responsive paging. Remember to assign unique `key` props to each child view for proper page tracking and to avoid rendering issues during page transitions.

**Strategy:**
Use `react-native-pager-view` with child views, each requiring a unique `key` prop.

**Code Example:**
import PagerView from 'react-native-pager-view';

<PagerView style={styles.pagerView} initialPage={0}>
  <View key="1"><Text>First page</Text></View>
  <View key="2"><Text>Second page</Text></View>
</PagerView>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q47"></a>
### Q47: How do you debug Network Requests?

**Difficulty**: Intermediate

**Strategy**:
Network debugging in React Native requires specialized tooling since you can't use browser DevTools directly. React Native Debugger (the standalone app) includes a Chrome DevTools Network tab that intercepts all `fetch`/`XMLHttpRequest` calls. Flipper (Meta's platform debugger) is the modern approach and is integrated by default in newer RN projects -- it shows network requests, logs, and layout inspector in one window.

**Code Example:**
// No code needed, just tooling setup.
// Flipper is enabled by default in newer RN versions.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q48"></a>
### Q48: How do you use Native Driver for Animations?

**Difficulty**: Intermediate

**Strategy**:
The Native Driver offloads animation execution from the JS thread to the native UI thread, preventing jank when JS is busy. Without it, every animation frame must cross the bridge. The key limitation is that `useNativeDriver` only works with non-layout properties (opacity, transform) -- it cannot animate `height`, `width`, or `position` natively. Always enable it for smooth 60fps animations.

**Code Example:**
Animated.timing(fadeAnim, {
  toValue: 1,
  duration: 1000,
  useNativeDriver: true // Critical for performance
}).start();

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q49"></a>
### Q49: How do you measure the dimensions of a View?

**Difficulty**: Beginner

**Strategy**:

**Strategy**:
Use the `onLayout` callback prop on any View to get its position and dimensions relative to its parent. For screen-level dimensions, use `Dimensions.get('window')`. A common pitfall is measuring too early (before layout completes) -- always use `onLayout` for dynamic measurements rather than guessing dimensions.

**Code Example:**
<View onLayout={(event) => {
  const {x, y, width, height} = event.nativeEvent.layout;
  console.log(width, height);
}} />

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q50"></a>
### Q50: How do you implement a Shadow on Android?

**Difficulty**: Beginner

**Strategy**:
iOS and Android handle shadows completely differently. iOS uses CSS-like shadow properties (`shadowColor`, `shadowOffset`, `shadowOpacity`, `shadowRadius`), while Android uses the Material Design `elevation` property. The key pitfall is that Android's `elevation` renders a fixed shadow you can't customize in color or offset. For cross-platform consistency, use `Platform.select()` to apply platform-specific styles, or use a library like `react-native-shadow-2` for pixel-perfect shadows on both platforms.

**Code Example:**
style: {
  ...Platform.select({
    ios: {
      shadowColor: '#000',
      shadowOffset: { width: 0, height: 2 },
      shadowOpacity: 0.8,
      shadowRadius: 2,
    },
    android: {
      elevation: 5,
    },
  }),
}

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---
