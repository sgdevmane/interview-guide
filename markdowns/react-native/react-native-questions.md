# React Native Interview Questions

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
50. [How do you implement a Shadow on Android?](#q50-how-do-you-implement-a-shadow-on-android) <span class="beginner">Beginner</span>

---

### Q1: How do you optimize the performance of a long FlatList with thousands of items?

**Difficulty**: Advanced

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

### Q2: How do you implement platform-specific code for iOS and Android?

**Difficulty**: Beginner

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

### Q3: How do you handle deep linking in a React Native app using React Navigation?

**Difficulty**: Intermediate

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

### Q4: How do you implement high-performance animations using React Native Reanimated?

**Difficulty**: Advanced

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

### Q5: How do you persist global state data using AsyncStorage?

**Difficulty**: Beginner

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

### Q6: How do you create a custom Native Module for Android (Java/Kotlin)?

**Difficulty**: Expert

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

### Q7: How do you handle safe area insets on devices with notches?

**Difficulty**: Beginner

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

### Q8: How do you debug React Native apps effectively?

**Difficulty**: Intermediate

**Strategy:**
1.  **React Native Debugger / Flipper:** For Redux, Network, and Component tree.
2.  **Console:** `console.log` (visible in Metro terminal).
3.  **Performance Monitor:** Toggle in Dev Menu.
4.  **LogBox:** Inspect warnings/errors in-app.

**Command:**
Press `Cmd+D` (iOS) or `Cmd+M` (Android) to open the Dev Menu.


---

### Q9: How do you prevent the on-screen keyboard from covering input fields?

**Difficulty**: Intermediate

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

### Q10: How do you implement an infinite scroll list?

**Difficulty**: Intermediate

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

### Q11: How do you use custom fonts in React Native (CLI workflow)?

**Difficulty**: Intermediate

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

### Q12: How do you handle offline network connectivity?

**Difficulty**: Intermediate

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

### Q13: How do you optimize image loading and caching?

**Difficulty**: Intermediate

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

### Q14: How do you create a translucent status bar on Android?

**Difficulty**: Intermediate

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

### Q15: How do you upgrade React Native to a newer version?

**Difficulty**: Advanced

**Strategy:**
Use the **React Native Upgrade Helper** web tool to see the diff between versions.
Run `npx react-native upgrade` (automated) or manually apply changes to `android/` and `ios/` folders based on the diff.


---

### Q16: How do you implement Stack Navigation using React Navigation?

**Difficulty**: Beginner

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

### Q17: How do you use Redux Toolkit in React Native?

**Difficulty**: Intermediate

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

### Q18: How do you use Context API for theming?

**Difficulty**: Intermediate

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

### Q19: What is the difference between Expo Managed and Bare workflows?

**Difficulty**: Beginner

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

### Q20: How do you enable Hermes Engine on Android?

**Difficulty**: Intermediate

**Strategy:**
In `android/app/build.gradle`, set `enableHermes: true`.

**Code Example:**
project.ext.react = [
    enableHermes: true  // clean and rebuild
]

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q21: What are TurboModules?

**Difficulty**: Advanced

**Strategy:**
TurboModules are part of the New Architecture (JSI). They allow lazy loading of native modules and direct C++ to JS communication without the asynchronous bridge serialization overhead.

**Code Example:**
// C++ implementation required for TurboModules
// JS side accesses it synchronously via JSI

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q22: What is the Fabric Renderer?

**Difficulty**: Advanced

**Strategy:**
Fabric is the new UI rendering system. It moves rendering logic to C++, improving performance, interoperability with host platforms, and enabling concurrent React features.

**Code Example:**
// Enabled via newArchEnabled=true in gradle/podfile
// Uses JSI to manipulate UI directly

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q23: How do you handle Push Notifications with Firebase (FCM)?

**Difficulty**: Intermediate

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

### Q24: How do you integrate Google Maps?

**Difficulty**: Intermediate

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

### Q25: How do you capture a photo using the Camera?

**Difficulty**: Intermediate

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

### Q26: How do you implement Biometric Authentication?

**Difficulty**: Intermediate

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

### Q27: How do you make a custom button accessible?

**Difficulty**: Beginner

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

### Q28: How do you implement Internationalization (i18n)?

**Difficulty**: Intermediate

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

### Q29: How do you perform Over-the-Air (OTA) updates?

**Difficulty**: Advanced

**Strategy:**
Use `react-native-code-push` (Microsoft) or `expo-updates`.

**Code Example:**
import CodePush from 'react-native-code-push';

let App = () => <Root />;
App = CodePush(App); // Wrap root component

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q30: How do you display a WebView?

**Difficulty**: Beginner

**Strategy:**
Use `react-native-webview`.

**Code Example:**
import { WebView } from 'react-native-webview';

<WebView source={{ uri: 'https://reactnative.dev/' }} />

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q31: How do you render SVG images?

**Difficulty**: Intermediate

**Strategy:**
Use `react-native-svg`. Import `Svg`, `Path`, `Circle` etc., or use `react-native-svg-transformer` to import .svg files.

**Code Example:**
import Svg, { Circle } from 'react-native-svg';

<Svg height="100" width="100">
  <Circle cx="50" cy="50" r="45" stroke="blue" strokeWidth="2.5" fill="green" />
</Svg>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q32: How do you handle complex gestures (Drag/Swipe)?

**Difficulty**: Intermediate

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

### Q33: How do you share content with other apps?

**Difficulty**: Beginner

**Strategy:**
Use the `Share` API.

**Code Example:**
import { Share } from 'react-native';

const onShare = async () => {
  await Share.share({
    message: 'Check out this cool app!',
  });
};

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q34: How do you detect App State changes (Background/Active)?

**Difficulty**: Beginner

**Strategy:**
Use `AppState` API.

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

### Q35: How do you open the device Settings?

**Difficulty**: Beginner

**Strategy:**
Use `Linking.openSettings()`.

**Code Example:**
import { Linking } from 'react-native';

<Button title="Open Settings" onPress={() => Linking.openSettings()} />

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q36: How do you securely store sensitive data (Tokens)?

**Difficulty**: Intermediate

**Strategy:**
Do NOT use AsyncStorage. Use `expo-secure-store` or `react-native-keychain` or `react-native-encrypted-storage`.

**Code Example:**
import * as SecureStore from 'expo-secure-store';

await SecureStore.setItemAsync('secure_token', 'secret-value');
const token = await SecureStore.getItemAsync('secure_token');

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q37: How do you use Vector Icons?

**Difficulty**: Beginner

**Strategy:**
Use `react-native-vector-icons`.

**Code Example:**
import Icon from 'react-native-vector-icons/FontAwesome';

<Icon name="rocket" size={30} color="#900" />

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q38: How do you display Lottie animations?

**Difficulty**: Intermediate

**Strategy:**
Use `lottie-react-native`. Import the JSON file.

**Code Example:**
import LottieView from 'lottie-react-native';

<LottieView source={require('./animation.json')} autoPlay loop />

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q39: How do you implement a Blur effect?

**Difficulty**: Intermediate

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

### Q40: How do you implement a Linear Gradient?

**Difficulty**: Beginner

**Strategy:**
Use `react-native-linear-gradient` (or `expo-linear-gradient`).

**Code Example:**
import LinearGradient from 'react-native-linear-gradient';

<LinearGradient colors={['#4c669f', '#3b5998', '#192f6a']} style={styles.linearGradient}>
  <Text>Sign in with Facebook</Text>
</LinearGradient>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q41: How do you handle the hardware back button on Android?

**Difficulty**: Beginner

**Strategy:**
Use `BackHandler` API.

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

### Q42: How do you get device information (Model, System Version)?

**Difficulty**: Beginner

**Strategy:**
Use `react-native-device-info`.

**Code Example:**
import DeviceInfo from 'react-native-device-info';

let systemVersion = DeviceInfo.getSystemVersion();
let model = DeviceInfo.getModel();

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q43: How do you copy text to the clipboard?

**Difficulty**: Beginner

**Strategy:**
Use `@react-native-clipboard/clipboard`.

**Code Example:**
import Clipboard from '@react-native-clipboard/clipboard';

const copyToClipboard = () => {
  Clipboard.setString('hello world');
};

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q44: How do you implement a modal?

**Difficulty**: Beginner

**Strategy:**
Use the `Modal` component.

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

### Q45: How do you check internet connectivity type (WiFi/Cellular)?

**Difficulty**: Beginner

**Strategy:**
Use `NetInfo`.

**Code Example:**
NetInfo.fetch().then(state => {
  console.log('Connection type', state.type);
  console.log('Is connected?', state.isConnected);
});

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q46: How do you implement a Pager View (ViewPager)?

**Difficulty**: Intermediate

**Strategy:**
Use `react-native-pager-view`.

**Code Example:**
import PagerView from 'react-native-pager-view';

<PagerView style={styles.pagerView} initialPage={0}>
  <View key="1"><Text>First page</Text></View>
  <View key="2"><Text>Second page</Text></View>
</PagerView>

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q47: How do you debug Network Requests?

**Difficulty**: Intermediate

**Strategy:**
Use React Native Debugger (includes Network tab) or Flipper.

**Code Example:**
// No code needed, just tooling setup.
// Flipper is enabled by default in newer RN versions.

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q48: How do you use Native Driver for Animations?

**Difficulty**: Intermediate

**Strategy:**
Set `useNativeDriver: true` in `Animated` configurations to offload animation to the UI thread.

**Code Example:**
Animated.timing(fadeAnim, {
  toValue: 1,
  duration: 1000,
  useNativeDriver: true // Critical for performance
}).start();

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q49: How do you measure the dimensions of a View?

**Difficulty**: Beginner

**Strategy:**
Use the `onLayout` prop.

**Code Example:**
<View onLayout={(event) => {
  const {x, y, width, height} = event.nativeEvent.layout;
  console.log(width, height);
}} />

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q50: How do you implement a Shadow on Android?

**Difficulty**: Beginner

**Strategy:**
Use `elevation` style property (Android only). For iOS, use `shadowColor`, `shadowOffset`, `shadowOpacity`, `shadowRadius`.

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

