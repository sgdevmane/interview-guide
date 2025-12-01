<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>Design Patterns Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for software architects and developers</b></p>
</div>

---

## Table of Contents

1. [What is the Singleton Pattern and when should you use it?](#q1-what-is-the-singleton-pattern-and-when-should-you-use-it) <span class="beginner">Beginner</span>
2. [How do you implement the Factory Method Pattern?](#q2-how-do-you-implement-the-factory-method-pattern) <span class="intermediate">Intermediate</span>
3. [What is the difference between Factory Method and Abstract Factory?](#q3-what-is-the-difference-between-factory-method-and-abstract-factory) <span class="advanced">Advanced</span>
4. [How does the Builder Pattern help in object construction?](#q4-how-does-the-builder-pattern-help-in-object-construction) <span class="intermediate">Intermediate</span>
5. [What is the Prototype Pattern and how does it relate to cloning?](#q5-what-is-the-prototype-pattern-and-how-does-it-relate-to-cloning) <span class="beginner">Beginner</span>
6. [How do you use the Adapter Pattern to make incompatible interfaces work together?](#q6-how-do-you-use-the-adapter-pattern-to-make-incompatible-interfaces-work-together) <span class="intermediate">Intermediate</span>
7. [What is the Decorator Pattern and how does it differ from inheritance?](#q7-what-is-the-decorator-pattern-and-how-does-it-differ-from-inheritance) <span class="intermediate">Intermediate</span>
8. [How does the Facade Pattern simplify complex systems?](#q8-how-does-the-facade-pattern-simplify-complex-systems) <span class="beginner">Beginner</span>
9. [What is the Proxy Pattern and what are its common use cases?](#q9-what-is-the-proxy-pattern-and-what-are-its-common-use-cases) <span class="intermediate">Intermediate</span>
10. [How do you use the Composite Pattern to represent tree structures?](#q10-how-do-you-use-the-composite-pattern-to-represent-tree-structures) <span class="advanced">Advanced</span>
11. [What is the Bridge Pattern and how does it decouple abstraction from implementation?](#q11-what-is-the-bridge-pattern-and-how-does-it-decouple-abstraction-from-implementation) <span class="advanced">Advanced</span>
12. [How does the Flyweight Pattern optimize memory usage?](#q12-how-does-the-flyweight-pattern-optimize-memory-usage) <span class="advanced">Advanced</span>
13. [How do you implement the Observer Pattern (Pub/Sub)?](#q13-how-do-you-implement-the-observer-pattern-pubsub) <span class="intermediate">Intermediate</span>
14. [What is the Strategy Pattern and how does it enable algorithm swapping?](#q14-what-is-the-strategy-pattern-and-how-does-it-enable-algorithm-swapping) <span class="intermediate">Intermediate</span>
15. [How does the Command Pattern encapsulate requests?](#q15-how-does-the-command-pattern-encapsulate-requests) <span class="intermediate">Intermediate</span>
16. [What is the Iterator Pattern?](#q16-what-is-the-iterator-pattern) <span class="beginner">Beginner</span>
17. [How does the Mediator Pattern reduce coupling between components?](#q17-how-does-the-mediator-pattern-reduce-coupling-between-components) <span class="advanced">Advanced</span>
18. [What is the Memento Pattern used for?](#q18-what-is-the-memento-pattern-used-for) <span class="advanced">Advanced</span>
19. [How does the State Pattern allow an object to alter its behavior?](#q19-how-does-the-state-pattern-allow-an-object-to-alter-its-behavior) <span class="intermediate">Intermediate</span>
20. [What is the Template Method Pattern?](#q20-what-is-the-template-method-pattern) <span class="beginner">Beginner</span>
21. [How do you implement the Chain of Responsibility Pattern?](#q21-how-do-you-implement-the-chain-of-responsibility-pattern) <span class="advanced">Advanced</span>
22. [What is the Visitor Pattern and when should you use it?](#q22-what-is-the-visitor-pattern-and-when-should-you-use-it) <span class="advanced">Advanced</span>
23. [What is the Command Pattern?](#q23-what-is-the-command-pattern) <span class="intermediate">Intermediate</span>
24. [What is the Interpreter Pattern?](#q24-what-is-the-interpreter-pattern) <span class="advanced">Advanced</span>
25. [What is the Iterator Pattern?](#q25-what-is-the-iterator-pattern) <span class="beginner">Beginner</span>
26. [What is the Mediator Pattern?](#q26-what-is-the-mediator-pattern) <span class="advanced">Advanced</span>
27. [What is the Memento Pattern?](#q27-what-is-the-memento-pattern) <span class="advanced">Advanced</span>
28. [What is the Observer Pattern?](#q28-what-is-the-observer-pattern) <span class="beginner">Beginner</span>
29. [What is the State Pattern?](#q29-what-is-the-state-pattern) <span class="intermediate">Intermediate</span>
30. [What is the Strategy Pattern?](#q30-what-is-the-strategy-pattern) <span class="intermediate">Intermediate</span>
31. [What is the Template Method?](#q31-what-is-the-template-method) <span class="intermediate">Intermediate</span>
32. [What is the Visitor Pattern?](#q32-what-is-the-visitor-pattern) <span class="advanced">Advanced</span>
33. [What is the Adapter Pattern?](#q33-what-is-the-adapter-pattern) <span class="beginner">Beginner</span>
34. [What is the Bridge Pattern?](#q34-what-is-the-bridge-pattern) <span class="advanced">Advanced</span>
35. [What is the Composite Pattern?](#q35-what-is-the-composite-pattern) <span class="intermediate">Intermediate</span>
36. [What is the Decorator Pattern?](#q36-what-is-the-decorator-pattern) <span class="beginner">Beginner</span>
37. [What is the Facade Pattern?](#q37-what-is-the-facade-pattern) <span class="beginner">Beginner</span>
38. [What is the Flyweight Pattern?](#q38-what-is-the-flyweight-pattern) <span class="advanced">Advanced</span>
39. [What is the Proxy Pattern?](#q39-what-is-the-proxy-pattern) <span class="intermediate">Intermediate</span>
40. [What is the Chain of Responsibility?](#q40-what-is-the-chain-of-responsibility) <span class="intermediate">Intermediate</span>
41. [What is the Abstract Factory?](#q41-what-is-the-abstract-factory) <span class="intermediate">Intermediate</span>
42. [What is the Builder Pattern?](#q42-what-is-the-builder-pattern) <span class="intermediate">Intermediate</span>
43. [What is the Factory Method?](#q43-what-is-the-factory-method) <span class="beginner">Beginner</span>
44. [What is the Prototype Pattern?](#q44-what-is-the-prototype-pattern) <span class="intermediate">Intermediate</span>
45. [What is the Singleton Pattern?](#q45-what-is-the-singleton-pattern) <span class="beginner">Beginner</span>
46. [What is Dependency Injection?](#q46-what-is-dependency-injection) <span class="intermediate">Intermediate</span>
47. [What is Inversion of Control?](#q47-what-is-inversion-of-control) <span class="advanced">Advanced</span>
48. [What is MVVM?](#q48-what-is-mvvm) <span class="intermediate">Intermediate</span>
49. [What is MVC?](#q49-what-is-mvc) <span class="beginner">Beginner</span>
50. [What is MVP?](#q50-what-is-mvp) <span class="intermediate">Intermediate</span>
51. [What is the Repository Pattern?](#q51-what-is-the-repository-pattern) <span class="intermediate">Intermediate</span>
52. [What is the Unit of Work?](#q52-what-is-the-unit-of-work) <span class="advanced">Advanced</span>
53. [What is Active Record?](#q53-what-is-active-record) <span class="intermediate">Intermediate</span>
54. [What is Data Mapper?](#q54-what-is-data-mapper) <span class="advanced">Advanced</span>
55. [What is Event Sourcing?](#q55-what-is-event-sourcing) <span class="advanced">Advanced</span>
56. [What is CQRS?](#q56-what-is-cqrs) <span class="advanced">Advanced</span>
57. [What is the Saga Pattern?](#q57-what-is-the-saga-pattern) <span class="advanced">Advanced</span>
58. [What is Circuit Breaker?](#q58-what-is-circuit-breaker) <span class="advanced">Advanced</span>
59. [What is Bulkhead Pattern?](#q59-what-is-bulkhead-pattern) <span class="advanced">Advanced</span>
60. [What is Sidecar Pattern?](#q60-what-is-sidecar-pattern) <span class="intermediate">Intermediate</span>
61. [What is API Gateway?](#q61-what-is-api-gateway) <span class="intermediate">Intermediate</span>
62. [What is Backends for Frontends (BFF)?](#q62-what-is-backends-for-frontends-bff) <span class="intermediate">Intermediate</span>
63. [What is Strangler Fig?](#q63-what-is-strangler-fig) <span class="advanced">Advanced</span>
64. [What is Retry Pattern?](#q64-what-is-retry-pattern) <span class="beginner">Beginner</span>
65. [What is Throttling?](#q65-what-is-throttling) <span class="intermediate">Intermediate</span>
66. [What is Debouncing?](#q66-what-is-debouncing) <span class="beginner">Beginner</span>
67. [What is Lazy Loading?](#q67-what-is-lazy-loading) <span class="beginner">Beginner</span>
68. [What is Eager Loading?](#q68-what-is-eager-loading) <span class="beginner">Beginner</span>
69. [What is Object Pool?](#q69-what-is-object-pool) <span class="advanced">Advanced</span>
70. [What is Null Object Pattern?](#q70-what-is-null-object-pattern) <span class="intermediate">Intermediate</span>
71. [What is Service Locator?](#q71-what-is-service-locator) <span class="intermediate">Intermediate</span>
72. [What is Module Pattern?](#q72-what-is-module-pattern) <span class="beginner">Beginner</span>
73. [What is Revealing Module Pattern?](#q73-what-is-revealing-module-pattern) <span class="intermediate">Intermediate</span>
74. [What is Mixin Pattern?](#q74-what-is-mixin-pattern) <span class="intermediate">Intermediate</span>
75. [What is Interceptor Pattern?](#q75-what-is-interceptor-pattern) <span class="intermediate">Intermediate</span>
76. [What is Filter Pattern?](#q76-what-is-filter-pattern) <span class="intermediate">Intermediate</span>
77. [What is Publisher-Subscriber?](#q77-what-is-publisher-subscriber) <span class="beginner">Beginner</span>
78. [What is Blackboard Pattern?](#q78-what-is-blackboard-pattern) <span class="advanced">Advanced</span>
79. [What is Layered Architecture?](#q79-what-is-layered-architecture) <span class="beginner">Beginner</span>
80. [What is Hexagonal Architecture?](#q80-what-is-hexagonal-architecture) <span class="advanced">Advanced</span>
81. [What is Clean Architecture?](#q81-what-is-clean-architecture) <span class="advanced">Advanced</span>
82. [What is Domain Driven Design (DDD)?](#q82-what-is-domain-driven-design-ddd) <span class="advanced">Advanced</span>
83. [What is Entity Component System (ECS)?](#q83-what-is-entity-component-system-ecs) <span class="advanced">Advanced</span>
84. [What is Flux Pattern?](#q84-what-is-flux-pattern) <span class="intermediate">Intermediate</span>
85. [What is Redux Pattern?](#q85-what-is-redux-pattern) <span class="intermediate">Intermediate</span>
86. [What is DAO?](#q86-what-is-dao) <span class="intermediate">Intermediate</span>
87. [What is DTO?](#q87-what-is-dto) <span class="beginner">Beginner</span>
88. [What is POJO?](#q88-what-is-pojo) <span class="beginner">Beginner</span>
89. [What is Value Object?](#q89-what-is-value-object) <span class="intermediate">Intermediate</span>
90. [What is Aggregate Root?](#q90-what-is-aggregate-root) <span class="advanced">Advanced</span>
91. [What is Specification Pattern?](#q91-what-is-specification-pattern) <span class="advanced">Advanced</span>
92. [What is Priority Queue?](#q92-what-is-priority-queue) <span class="intermediate">Intermediate</span>
93. [What is LRU Cache?](#q93-what-is-lru-cache) <span class="intermediate">Intermediate</span>
94. [What is Rate Limiter?](#q94-what-is-rate-limiter) <span class="intermediate">Intermediate</span>
95. [What is Consistent Hashing?](#q95-what-is-consistent-hashing) <span class="advanced">Advanced</span>
96. [What is Bloom Filter?](#q96-what-is-bloom-filter) <span class="advanced">Advanced</span>
97. [What is CAP Theorem?](#q97-what-is-cap-theorem) <span class="intermediate">Intermediate</span>
98. [What is SOLID?](#q98-what-is-solid) <span class="intermediate">Intermediate</span>
99. [What is DRY?](#q99-what-is-dry) <span class="beginner">Beginner</span>
100. [What is KISS?](#q100-what-is-kiss) <span class="beginner">Beginner</span>
101. [What is YAGNI?](#q101-what-is-yagni) <span class="beginner">Beginner</span>

---

<a id="q1"></a>
### Q1: What is the Singleton Pattern and when should you use it?

**Difficulty**: Beginner

**Strategy:**
Ensure a class has only one instance and provide a global point of access to it. Use it for logging, database connections, or configuration settings.

**Code Example:**
```javascript
class Singleton {
  constructor() {
    if (Singleton.instance) {
      return Singleton.instance;
    }
    Singleton.instance = this;
    this.data = [];
  }

  add(item) {
    this.data.push(item);
  }
}

const s1 = new Singleton();
const s2 = new Singleton();
console.log(s1 === s2); // true
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q2"></a>
### Q2: How do you implement the Factory Method Pattern?

**Difficulty**: Intermediate

**Strategy:**
Define an interface for creating an object, but let subclasses decide which class to instantiate. It delegates instantiation logic to child classes.

**Code Example:**
```javascript
class Logistics {
  createTransport() {
    throw new Error("Method 'createTransport' must be implemented.");
  }
  
  planDelivery() {
    const transport = this.createTransport();
    return transport.deliver();
  }
}

class RoadLogistics extends Logistics {
  createTransport() {
    return new Truck();
  }
}

class Truck {
  deliver() {
    return "Delivering by land in a box.";
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q3"></a>
### Q3: What is the difference between Factory Method and Abstract Factory?

**Difficulty**: Advanced

**Strategy:**
*   **Factory Method:** Creates one object (a product). Uses inheritance.
*   **Abstract Factory:** Creates families of related objects. Uses composition.

**Code Example:**
```javascript
// Abstract Factory Interface
class GUIFactory {
  createButton() {}
  createCheckbox() {}
}

// Concrete Factory for Mac
class MacFactory extends GUIFactory {
  createButton() { return new MacButton(); }
  createCheckbox() { return new MacCheckbox(); }
}

// Concrete Factory for Windows
class WinFactory extends GUIFactory {
  createButton() { return new WinButton(); }
  createCheckbox() { return new WinCheckbox(); }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q4"></a>
### Q4: How does the Builder Pattern help in object construction?

**Difficulty**: Intermediate

**Strategy:**
Separate the construction of a complex object from its representation. It allows you to construct complex objects step-by-step.

**Code Example:**
```javascript
class CarBuilder {
  constructor() {
    this.car = new Car();
  }
  
  setSeats(seats) {
    this.car.seats = seats;
    return this;
  }
  
  setEngine(engine) {
    this.car.engine = engine;
    return this;
  }
  
  build() {
    return this.car;
  }
}

const car = new CarBuilder().setSeats(4).setEngine('V8').build();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q5"></a>
### Q5: What is the Prototype Pattern and how does it relate to cloning?

**Difficulty**: Beginner

**Strategy:**
Create new objects by copying an existing object (the prototype). It avoids the cost of creating a new instance from scratch.

**Code Example:**
```javascript
const carPrototype = {
  wheels: 4,
  start() {
    console.log('Vroom!');
  },
  clone() {
    return Object.create(this);
  }
};

const myCar = carPrototype.clone();
myCar.color = 'red';
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q6"></a>
### Q6: How do you use the Adapter Pattern to make incompatible interfaces work together?

**Difficulty**: Intermediate

**Strategy:**
Wrap an existing class with a new interface so that it becomes compatible with the client's expectations.

**Code Example:**
```javascript
// Old Interface
class OldCalculator {
  operations(t1, t2, operation) {
    switch (operation) {
      case 'sum': return t1 + t2;
      default: return NaN;
    }
  }
}

// New Interface
class NewCalculator {
  add(t1, t2) { return t1 + t2; }
}

// Adapter
class CalcAdapter {
  constructor() {
    this.calc = new OldCalculator();
  }
  
  add(t1, t2) {
    return this.calc.operations(t1, t2, 'sum');
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q7"></a>
### Q7: What is the Decorator Pattern and how does it differ from inheritance?

**Difficulty**: Intermediate

**Strategy:**
Attach new behaviors to objects efficiently by placing these objects inside special wrapper objects. It allows dynamic behavior addition at runtime, unlike static inheritance.

**Code Example:**
```javascript
class Coffee {
  cost() { return 5; }
}

// Decorator
const withMilk = (coffee) => {
  const cost = coffee.cost();
  coffee.cost = () => cost + 2;
  return coffee;
};

let myCoffee = new Coffee();
myCoffee = withMilk(myCoffee);
console.log(myCoffee.cost()); // 7
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q8"></a>
### Q8: How does the Facade Pattern simplify complex systems?

**Difficulty**: Beginner

**Strategy:**
Provide a simplified interface to a library, a framework, or any other complex set of classes. It hides the complexity of the subsystem.

**Code Example:**
```javascript
class ComputerFacade {
  constructor() {
    this.cpu = new CPU();
    this.memory = new Memory();
    this.disk = new HardDrive();
  }
  
  start() {
    this.cpu.freeze();
    this.memory.load(this.bootAddress, this.disk.read(this.bootSector, this.sectorSize));
    this.cpu.jump(this.bootAddress);
    this.cpu.execute();
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q9"></a>
### Q9: What is the Proxy Pattern and what are its common use cases?

**Difficulty**: Intermediate

**Strategy:**
Provide a substitute or placeholder for another object. A proxy controls access to the original object, allowing you to perform something either before or after the request gets through to the original object (e.g., lazy loading, caching, access control).

**Code Example:**
```javascript
const target = {
  message: "Hello"
};

const handler = {
  get: function(obj, prop) {
    if (prop === "message") {
      return "World"; // Intercepting access
    }
    return obj[prop];
  }
};

const proxy = new Proxy(target, handler);
console.log(proxy.message); // "World"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q10"></a>
### Q10: How do you use the Composite Pattern to represent tree structures?

**Difficulty**: Advanced

**Strategy:**
Compose objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly.

**Code Example:**
```javascript
class Component {
  operation() {}
}

class Leaf extends Component {
  operation() { return "Leaf"; }
}

class Composite extends Component {
  constructor() {
    super();
    this.children = [];
  }
  
  add(component) {
    this.children.push(component);
  }
  
  operation() {
    return `Branch(${this.children.map(c => c.operation()).join('+')})`;
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q11"></a>
### Q11: What is the Bridge Pattern and how does it decouple abstraction from implementation?

**Difficulty**: Advanced

**Strategy:**
Split a large class or a set of closely related classes into two separate hierarchies—abstraction and implementation—which can be developed independently of each other.

**Code Example:**
```javascript
// Implementation
class Device {
  turnOn() {}
  turnOff() {}
}

class TV extends Device {
  turnOn() { console.log("TV On"); }
}

class Radio extends Device {
  turnOn() { console.log("Radio On"); }
}

// Abstraction
class Remote {
  constructor(device) {
    this.device = device;
  }
  
  togglePower() {
    this.device.turnOn(); // Bridge to implementation
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q12"></a>
### Q12: How does the Flyweight Pattern optimize memory usage?

**Difficulty**: Advanced

**Strategy:**
Fit more objects into the available amount of RAM by sharing common parts of state between multiple objects instead of keeping all of the data in each object.

**Code Example:**
```javascript
class TreeType {
  constructor(name, color, texture) {
    this.name = name;
    this.color = color;
    this.texture = texture;
  }
  draw(x, y) {
    console.log(`Drawing ${this.name} at ${x},${y}`);
  }
}

class TreeFactory {
  static types = {};
  static getTreeType(name, color, texture) {
    const key = `${name}-${color}-${texture}`;
    if (!this.types[key]) {
      this.types[key] = new TreeType(name, color, texture);
    }
    return this.types[key];
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q13"></a>
### Q13: How do you implement the Observer Pattern (Pub/Sub)?

**Difficulty**: Intermediate

**Strategy:**
Define a subscription mechanism to notify multiple objects about any events that happen to the object they're observing.

**Code Example:**
```javascript
class Subject {
  constructor() {
    this.observers = [];
  }
  
  subscribe(observer) {
    this.observers.push(observer);
  }
  
  notify(data) {
    this.observers.forEach(obs => obs.update(data));
  }
}

class Observer {
  update(data) {
    console.log(`Received: ${data}`);
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q14"></a>
### Q14: What is the Strategy Pattern and how does it enable algorithm swapping?

**Difficulty**: Intermediate

**Strategy:**
Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it.

**Code Example:**
```javascript
class PaymentContext {
  constructor(strategy) {
    this.strategy = strategy;
  }
  
  pay(amount) {
    return this.strategy.pay(amount);
  }
}

class CreditCardStrategy {
  pay(amount) { console.log(`Paid ${amount} via Credit Card`); }
}

class PayPalStrategy {
  pay(amount) { console.log(`Paid ${amount} via PayPal`); }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q15"></a>
### Q15: How does the Command Pattern encapsulate requests?

**Difficulty**: Intermediate

**Strategy:**
Turn a request into a stand-alone object that contains all information about the request. This transformation lets you pass requests as a method arguments, delay or queue a request's execution, and support undoable operations.

**Code Example:**
```javascript
class Command {
  execute() {}
}

class LightOnCommand extends Command {
  constructor(light) {
    super();
    this.light = light;
  }
  execute() {
    this.light.on();
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q16"></a>
### Q16: What is the Iterator Pattern?

**Difficulty**: Beginner

**Strategy:**
Traverse elements of a collection without exposing its underlying representation (list, stack, tree, etc.).

**Code Example:**
```javascript
const collection = [1, 2, 3];
const iterator = collection[Symbol.iterator]();

console.log(iterator.next()); // { value: 1, done: false }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q17"></a>
### Q17: How does the Mediator Pattern reduce coupling between components?

**Difficulty**: Advanced

**Strategy:**
Restrict direct communications between the objects and force them to collaborate only via a mediator object.

**Code Example:**
```javascript
class Mediator {
  notify(sender, event) {
    if (event === "A") {
      console.log("Mediator reacts on A and triggers following operations:");
      this.component2.doC();
    }
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q18"></a>
### Q18: What is the Memento Pattern used for?

**Difficulty**: Advanced

**Strategy:**
Capture and externalize an object's internal state so that the object can be restored to this state later (e.g., undo/redo).

**Code Example:**
```javascript
class Memento {
  constructor(state) {
    this.state = state;
  }
  getState() { return this.state; }
}

class Originator {
  save() { return new Memento(this.state); }
  restore(memento) { this.state = memento.getState(); }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q19"></a>
### Q19: How does the State Pattern allow an object to alter its behavior?

**Difficulty**: Intermediate

**Strategy:**
Let an object alter its behavior when its internal state changes. It appears as if the object changed its class.

**Code Example:**
```javascript
class State {
  handle(context) {}
}

class ConcreteStateA extends State {
  handle(context) {
    console.log("State A handles request.");
    context.state = new ConcreteStateB();
  }
}

class Context {
  constructor(state) { this.state = state; }
  request() { this.state.handle(this); }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q20"></a>
### Q20: What is the Template Method Pattern?

**Difficulty**: Beginner

**Strategy:**
Define the skeleton of an algorithm in the superclass but let subclasses override specific steps of the algorithm without changing its structure.

**Code Example:**
```javascript
class DataMiner {
  mine() {
    this.openFile();
    this.extractData(); // Abstract step
    this.closeFile();
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q21"></a>
### Q21: How do you implement the Chain of Responsibility Pattern?

**Difficulty**: Advanced

**Strategy:**
Pass requests along a chain of handlers. Upon receiving a request, each handler decides either to process the request or to pass it to the next handler in the chain.

**Code Example:**
```javascript
class Handler {
  setNext(handler) {
    this.next = handler;
    return handler;
  }
  
  handle(request) {
    if (this.next) {
      return this.next.handle(request);
    }
    return null;
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q22"></a>
### Q22: What is the Visitor Pattern and when should you use it?

**Difficulty**: Advanced

**Strategy:**
Separate algorithms from the objects on which they operate. It lets you add new operations to existing object structures without modifying them.

**Code Example:**
```javascript
class Visitor {
  visitConcreteElementA(element) {}
  visitConcreteElementB(element) {}
}

class ConcreteElementA {
  accept(visitor) {
    visitor.visitConcreteElementA(this);
  }
}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>


---

<a id="q23"></a>
### Q23: What is the Command Pattern?

**Difficulty**: Intermediate

**Strategy**:
The Command Pattern encapsulates a request as an object, thereby letting you parameterize other objects with different requests, queue or log requests, and support undoable operations. It decouples the object that invokes the operation from the one that knows how to perform it.

**Code Example**:
```javascript
class Command { execute() {} }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q24"></a>
### Q24: What is the Interpreter Pattern?

**Difficulty**: Advanced

**Strategy**:
Defines a grammar for a language and an interpreter.

**Code Example**:
```javascript
// SQL parsing engines use this
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q25"></a>
### Q25: What is the Iterator Pattern?

**Difficulty**: Beginner

**Strategy**:
Access elements of a collection sequentially. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
for (let item of collection) { ... }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q26"></a>
### Q26: What is the Mediator Pattern?

**Difficulty**: Advanced

**Strategy**:
Centralizes communication between objects. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
mediator.notify(sender, 'event');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q27"></a>
### Q27: What is the Memento Pattern?

**Difficulty**: Advanced

**Strategy**:
Captures object state for undo/rollback. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const savedState = originator.save();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q28"></a>
### Q28: What is the Observer Pattern?

**Difficulty**: Beginner

**Strategy**:
The Observer Pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically. It is commonly used in event handling systems.

**Code Example**:
```javascript
subject.subscribe(observer);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q29"></a>
### Q29: What is the State Pattern?

**Difficulty**: Intermediate

**Strategy**:
Object changes behavior when state changes. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
state.handle();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q30"></a>
### Q30: What is the Strategy Pattern?

**Difficulty**: Intermediate

**Strategy**:
The Strategy Pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from clients that use it. It is useful for swapping behavior at runtime (e.g., different sorting algorithms).

**Code Example**:
```javascript
context.setStrategy(new SortStrategy());
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q31"></a>
### Q31: What is the Template Method?

**Difficulty**: Intermediate

**Strategy**:
Skeleton of algorithm in superclass. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
class Base { step1(); step2(); }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q32"></a>
### Q32: What is the Visitor Pattern?

**Difficulty**: Advanced

**Strategy**:
Add operations to objects without changing them. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
element.accept(visitor);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q33"></a>
### Q33: What is the Adapter Pattern?

**Difficulty**: Beginner

**Strategy**:
Connects incompatible interfaces. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
class Adapter { request() { return old.specificRequest(); } }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q34"></a>
### Q34: What is the Bridge Pattern?

**Difficulty**: Advanced

**Strategy**:
Decouples abstraction from implementation. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
class Remote { constructor(device) { ... } }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q35"></a>
### Q35: What is the Composite Pattern?

**Difficulty**: Intermediate

**Strategy**:
Tree structure of objects. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
composite.add(leaf);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q36"></a>
### Q36: What is the Decorator Pattern?

**Difficulty**: Beginner

**Strategy**:
Adds behavior dynamically. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
@decorator class A {}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q37"></a>
### Q37: What is the Facade Pattern?

**Difficulty**: Beginner

**Strategy**:
Simplified interface to complex system. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
facade.startComputer();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q38"></a>
### Q38: What is the Flyweight Pattern?

**Difficulty**: Advanced

**Strategy**:
Share common state to save memory. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
factory.getFlyweight(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q39"></a>
### Q39: What is the Proxy Pattern?

**Difficulty**: Intermediate

**Strategy**:
Placeholder for another object. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
const proxy = new Proxy(target, handler);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q40"></a>
### Q40: What is the Chain of Responsibility?

**Difficulty**: Intermediate

**Strategy**:
Pass request along a chain of handlers. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
h1.setNext(h2); h1.handle(req);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q41"></a>
### Q41: What is the Abstract Factory?

**Difficulty**: Intermediate

**Strategy**:
Families of related objects. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
factory.createButton(); factory.createCheckbox();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q42"></a>
### Q42: What is the Builder Pattern?

**Difficulty**: Intermediate

**Strategy**:
Step-by-step object construction. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
new Builder().setPartA().build();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q43"></a>
### Q43: What is the Factory Method?

**Difficulty**: Beginner

**Strategy**:
The Factory Method Pattern defines an interface for creating an object, but lets subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses. It is useful when a class doesn't know in advance the class of objects it must create.

**Code Example**:
```javascript
createAnimal() { return new Dog(); }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q44"></a>
### Q44: What is the Prototype Pattern?

**Difficulty**: Intermediate

**Strategy**:
Cloning objects. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
obj.clone();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q45"></a>
### Q45: What is the Singleton Pattern?

**Difficulty**: Beginner

**Strategy**:
The Singleton Pattern ensures a class has only one instance, and provides a global point of access to it. It is often used for things like logging drivers, database connections, or configuration managers. However, it can introduce global state and make testing difficult.

**Code Example**:
```javascript
if (!instance) instance = this;
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q46"></a>
### Q46: What is Dependency Injection?

**Difficulty**: Intermediate

**Strategy**:
Dependency Injection (DI) is a technique in which an object receives other objects that it depends on. These other objects are called dependencies. Instead of creating dependencies itself, the object accepts them, usually via constructor or setter injection. This promotes loose coupling.

**Code Example**:
```javascript
constructor(service) { this.service = service; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q47"></a>
### Q47: What is Inversion of Control?

**Difficulty**: Advanced

**Strategy**:
Inversion of Control (IoC) is a design principle in which the flow of control of a system is inverted in comparison to procedural programming. In traditional programming, your custom code calls into a library. With IoC, a framework calls into your custom code (e.g., React calling your component).

**Code Example**:
```javascript
// React calls your render method
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q48"></a>
### Q48: What is MVVM?

**Difficulty**: Intermediate

**Strategy**:
Model-View-ViewModel (MVVM) is a software architectural pattern that facilitates the separation of the development of the graphical user interface (the view) from the development of the business logic or back-end logic (the model). The view model is a value converter that exposes data objects from the model to the view.

**Code Example**:
```javascript
// Angular, Vue, Knockout
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q49"></a>
### Q49: What is MVC?

**Difficulty**: Beginner

**Strategy**:
Model-View-Controller (MVC) is an architectural pattern that separates an application into three main logical components: the model, the view, and the controller. Each of these components are built to handle specific development aspects of an application. It is widely used for developing user interfaces.

**Code Example**:
```javascript
// Ruby on Rails, Spring MVC
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q50"></a>
### Q50: What is MVP?

**Difficulty**: Intermediate

**Strategy**:
Model-View-Presenter. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Android (old)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q51"></a>
### Q51: What is the Repository Pattern?

**Difficulty**: Intermediate

**Strategy**:
Abstraction of data layer. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
repo.getUser(id);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q52"></a>
### Q52: What is the Unit of Work?

**Difficulty**: Advanced

**Strategy**:
Tracks changes for a transaction. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
uow.commit();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q53"></a>
### Q53: What is Active Record?

**Difficulty**: Intermediate

**Strategy**:
Object wraps a row in DB table. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
user.save();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q54"></a>
### Q54: What is Data Mapper?

**Difficulty**: Advanced

**Strategy**:
Separates in-memory objects from DB. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
mapper.save(user);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q55"></a>
### Q55: What is Event Sourcing?

**Difficulty**: Advanced

**Strategy**:
Event Sourcing is a pattern where the state of the application is determined by a sequence of events. Instead of storing just the current state of the data in a domain, we store a log of actions (events) that happened. The current state is derived by replaying the events.

**Code Example**:
```javascript
events.forEach(e => state.apply(e));
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q56"></a>
### Q56: What is CQRS?

**Difficulty**: Advanced

**Strategy**:
CQRS (Command Query Responsibility Segregation) fits well with Event Sourcing. It separates the read and write models of an application. Commands change the state of the system, while Queries return the state. This allows scaling reads and writes independently.

**Code Example**:
```javascript
// Separate read and write models
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q57"></a>
### Q57: What is the Saga Pattern?

**Difficulty**: Advanced

**Strategy**:
Long running transactions in microservices. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Compensating actions on failure
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q58"></a>
### Q58: What is Circuit Breaker?

**Difficulty**: Advanced

**Strategy**:
The Circuit Breaker pattern prevents an application from repeatedly trying to execute an operation that's likely to fail. It detects failures and encapsulates the logic of preventing a failure from constantly recurring (e.g., during maintenance, temporary external system failure or unexpected system difficulties).

**Code Example**:
```javascript
if (failures > threshold) openCircuit();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q59"></a>
### Q59: What is Bulkhead Pattern?

**Difficulty**: Advanced

**Strategy**:
Isolate resources pools. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Separate thread pools
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q60"></a>
### Q60: What is Sidecar Pattern?

**Difficulty**: Intermediate

**Strategy**:
Helper process alongside main app. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Envoy proxy in K8s
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q61"></a>
### Q61: What is API Gateway?

**Difficulty**: Intermediate

**Strategy**:
An API Gateway is a server that is the single entry point into the system. It encapsulates the internal system architecture and provides an API that is tailored to each client. It might have other responsibilities such as authentication, monitoring, load balancing, caching, request shaping and management, and static response handling.

**Code Example**:
```javascript
// Zuul, Nginx
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q62"></a>
### Q62: What is Backends for Frontends (BFF)?

**Difficulty**: Intermediate

**Strategy**:
Separate backend per UI. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Mobile API, Web API
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q63"></a>
### Q63: What is Strangler Fig?

**Difficulty**: Advanced

**Strategy**:
Gradually replace legacy system. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Route by route migration
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q64"></a>
### Q64: What is Retry Pattern?

**Difficulty**: Beginner

**Strategy**:
Retry failed operations. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
retry(fn, 3);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q65"></a>
### Q65: What is Throttling?

**Difficulty**: Intermediate

**Strategy**:
Limit rate of operations. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
if (rate > limit) reject();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q66"></a>
### Q66: What is Debouncing?

**Difficulty**: Beginner

**Strategy**:
Wait for pause in events. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
setTimeout(fn, delay);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q67"></a>
### Q67: What is Lazy Loading?

**Difficulty**: Beginner

**Strategy**:
Load on demand. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
if (needed) load();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q68"></a>
### Q68: What is Eager Loading?

**Difficulty**: Beginner

**Strategy**:
Load everything upfront. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
loadAll();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q69"></a>
### Q69: What is Object Pool?

**Difficulty**: Advanced

**Strategy**:
Reuse objects instead of creating new. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
pool.acquire();
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q70"></a>
### Q70: What is Null Object Pattern?

**Difficulty**: Intermediate

**Strategy**:
Object with no-op behavior instead of null. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
class NullUser { getName() { return 'Guest'; } }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q71"></a>
### Q71: What is Service Locator?

**Difficulty**: Intermediate

**Strategy**:
Registry of services. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
locator.get('Service');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q72"></a>
### Q72: What is Module Pattern?

**Difficulty**: Beginner

**Strategy**:
Encapsulation with closures. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
return { publicMethod };
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q73"></a>
### Q73: What is Revealing Module Pattern?

**Difficulty**: Intermediate

**Strategy**:
Expose references to private functions. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
return { start: startFn };
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q74"></a>
### Q74: What is Mixin Pattern?

**Difficulty**: Intermediate

**Strategy**:
Add functionality to class. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
Object.assign(Class.prototype, mixin);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q75"></a>
### Q75: What is Interceptor Pattern?

**Difficulty**: Intermediate

**Strategy**:
Intercept requests/responses. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
axios.interceptors.request.use(...)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q76"></a>
### Q76: What is Filter Pattern?

**Difficulty**: Intermediate

**Strategy**:
Filter list of objects. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
list.filter(criteria);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q77"></a>
### Q77: What is Publisher-Subscriber?

**Difficulty**: Beginner

**Strategy**:
Msg queue decoupling. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
pub.publish(topic, msg);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q78"></a>
### Q78: What is Blackboard Pattern?

**Difficulty**: Advanced

**Strategy**:
Shared knowledge base for AI. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Expert systems
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q79"></a>
### Q79: What is Layered Architecture?

**Difficulty**: Beginner

**Strategy**:
Separation into layers (UI, Business, Data). This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// N-tier
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q80"></a>
### Q80: What is Hexagonal Architecture?

**Difficulty**: Advanced

**Strategy**:
Ports and Adapters. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Core logic isolated from external
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q81"></a>
### Q81: What is Clean Architecture?

**Difficulty**: Advanced

**Strategy**:
Dependency Rule (inwards). This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Entities -> Use Cases -> Adapters
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q82"></a>
### Q82: What is Domain Driven Design (DDD)?

**Difficulty**: Advanced

**Strategy**:
Focus on core domain logic. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Bounded Contexts, Aggregates
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q83"></a>
### Q83: What is Entity Component System (ECS)?

**Difficulty**: Advanced

**Strategy**:
Game development pattern. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Unity DOTS
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q84"></a>
### Q84: What is Flux Pattern?

**Difficulty**: Intermediate

**Strategy**:
Flux is an application architecture for building client-side web applications. It complements React's composable view components by utilizing a unidirectional data flow. It is more of a pattern than a formal framework, consisting of a Dispatcher, Stores, and Views (React components).

**Code Example**:
```javascript
// Redux
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q85"></a>
### Q85: What is Redux Pattern?

**Difficulty**: Intermediate

**Strategy**:
Single source of truth, immutability. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
reducer(state, action)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q86"></a>
### Q86: What is DAO?

**Difficulty**: Intermediate

**Strategy**:
Data Access Object. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
dao.findById(1);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q87"></a>
### Q87: What is DTO?

**Difficulty**: Beginner

**Strategy**:
Data Transfer Object. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
class UserDTO { name; email; }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q88"></a>
### Q88: What is POJO?

**Difficulty**: Beginner

**Strategy**:
Plain Old Java/JS Object. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
{ id: 1 }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q89"></a>
### Q89: What is Value Object?

**Difficulty**: Intermediate

**Strategy**:
Object defined by attributes, immutable. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
new Money(10, 'USD');
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q90"></a>
### Q90: What is Aggregate Root?

**Difficulty**: Advanced

**Strategy**:
Entry point to cluster of objects. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Order controls OrderItems
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q91"></a>
### Q91: What is Specification Pattern?

**Difficulty**: Advanced

**Strategy**:
Business rules as objects. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
spec.isSatisfiedBy(obj);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q92"></a>
### Q92: What is Priority Queue?

**Difficulty**: Intermediate

**Strategy**:
Elements processed by priority. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
heap.insert(item);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q93"></a>
### Q93: What is LRU Cache?

**Difficulty**: Intermediate

**Strategy**:
Least Recently Used eviction. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
cache.get(key);
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q94"></a>
### Q94: What is Rate Limiter?

**Difficulty**: Intermediate

**Strategy**:
Control traffic. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
Token Bucket algorithm
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q95"></a>
### Q95: What is Consistent Hashing?

**Difficulty**: Advanced

**Strategy**:
Distributed caching/sharding. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
hash(key) % nodes
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q96"></a>
### Q96: What is Bloom Filter?

**Difficulty**: Advanced

**Strategy**:
Probabilistic set membership. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
mightContain(item)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q97"></a>
### Q97: What is CAP Theorem?

**Difficulty**: Intermediate

**Strategy**:
Consistency, Availability, Partition Tolerance. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Choose 2
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q98"></a>
### Q98: What is SOLID?

**Difficulty**: Intermediate

**Strategy**:
SOLID is an acronym for 5 design principles: Single Responsibility Principle (SRP), Open/Closed Principle (OCP), Liskov Substitution Principle (LSP), Interface Segregation Principle (ISP), and Dependency Inversion Principle (DIP). These principles help make software designs more understandable, flexible, and maintainable.

**Code Example**:
```javascript
// OO Design Principles
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q99"></a>
### Q99: What is DRY?

**Difficulty**: Beginner

**Strategy**:
DRY stands for 'Don't Repeat Yourself'. It is a principle of software development aimed at reducing repetition of software patterns, replacing it with abstractions or using data normalization to avoid redundancy. Violations of DRY are often referred to as WET (Write Everything Twice).

**Code Example**:
```javascript
// Refactor duplicates
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q100"></a>
### Q100: What is KISS?

**Difficulty**: Beginner

**Strategy**:
Keep It Simple, Stupid. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Avoid overengineering
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q101"></a>
### Q101: What is YAGNI?

**Difficulty**: Beginner

**Strategy**:
You Ain't Gonna Need It. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// Don't build for future
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>