<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>Python Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for developers</b></p>
</div>

---

## Table of Contents

1. [How do you optimize memory usage when processing large datasets in Python?](#q1) <span class="intermediate">Intermediate</span>
2. [How do you ensure resources (files, sockets) are properly closed even if errors occur?](#q2) <span class="beginner">Beginner</span>
3. [How do you implement a decorator to measure the execution time of a function?](#q3) <span class="intermediate">Intermediate</span>
4. [How do you bypass the Global Interpreter Lock (GIL) for CPU-bound tasks?](#q4) <span class="advanced">Advanced</span>
5. [How do you handle concurrent I/O-bound operations efficiently?](#q5) <span class="intermediate">Intermediate</span>
6. [How do you merge two dictionaries in Python 3.9+?](#q6) <span class="beginner">Beginner</span>
7. [How do you create a lightweight immutable data class?](#q7) <span class="intermediate">Intermediate</span>
8. [How do you optimize function calls with caching (memoization)?](#q8) <span class="intermediate">Intermediate</span>
9. [How do you enforce type safety in a large Python codebase?](#q9) <span class="intermediate">Intermediate</span>
10. [How do you create a true deep copy of a nested object?](#q10) <span class="beginner">Beginner</span>
11. [How do you manage project dependencies effectively?](#q11) <span class="intermediate">Intermediate</span>
12. [How do you safely handle exceptions without crashing the app?](#q12) <span class="beginner">Beginner</span>
13. [How do you dynamically create classes or modify class behavior?](#q13) <span class="advanced">Advanced</span>
14. [How do you unpack a list with variable elements?](#q14) <span class="beginner">Beginner</span>
15. [How do you implement an iterator class manually?](#q15) <span class="intermediate">Intermediate</span>
16. [How do you debug code using PDB?](#q16) <span class="intermediate">Intermediate</span>
17. [How do you optimize Pandas operations using Vectorization?](#q17) <span class="intermediate">Intermediate</span>
18. [How do you use Numpy Broadcasting?](#q18) <span class="intermediate">Intermediate</span>
19. [How do you create an async API endpoint with FastAPI?](#q19) <span class="intermediate">Intermediate</span>
20. [How do you use ContextVars for thread-safe state management?](#q20) <span class="advanced">Advanced</span>
21. [How do you use the Walrus Operator (Assignment Expression)?](#q21) <span class="beginner">Beginner</span>
22. [How do you implement abstract base classes (ABCs)?](#q22) <span class="intermediate">Intermediate</span>
23. [How do you use Python's gc module to handle cyclic references?](#q23) <span class="advanced">Advanced</span>
24. [How do you use **slots** to optimize memory?](#q24) <span class="intermediate">Intermediate</span>
25. [How do you use Itertools to chain iterables?](#q25) <span class="intermediate">Intermediate</span>
26. [How do you use defaultdict for cleaner grouping code?](#q26) <span class="beginner">Beginner</span>
27. [How do you use unittest.mock to mock dependencies?](#q27) <span class="intermediate">Intermediate</span>
28. [How do you use functools.partial?](#q28) <span class="intermediate">Intermediate</span>
29. [How do you use threading.Event for thread synchronization?](#q29) <span class="intermediate">Intermediate</span>
30. [How do you run shell commands with subprocess.run?](#q30) <span class="intermediate">Intermediate</span>
31. [How do you use json.dumps with a custom encoder?](#q31) <span class="intermediate">Intermediate</span>
32. [How do you use collections.Counter?](#q32) <span class="beginner">Beginner</span>
33. [How do you use heapq for a priority queue?](#q33) <span class="intermediate">Intermediate</span>
34. [How do you use zip to iterate over multiple lists?](#q34) <span class="beginner">Beginner</span>
35. [How do you use enumerate?](#q35) <span class="beginner">Beginner</span>
36. [How do you use if **name** == "**main**":?](#q36) <span class="beginner">Beginner</span>
37. [How do you use re module for regex matching?](#q37) <span class="intermediate">Intermediate</span>
38. [How do you use with statement (Context Managers)?](#q38) <span class="beginner">Beginner</span>
39. [How do you use Generators (yield)?](#q39) <span class="intermediate">Intermediate</span>
40. [How do you use Decorators?](#q40) <span class="intermediate">Intermediate</span>
41. [How do you implement asynchronous tasks with Celery?](#q41) <span class="advanced">Advanced</span>
42. [How do you define a One-to-Many relationship in SQLAlchemy?](#q42) <span class="intermediate">Intermediate</span>
43. [How do you structure a large Flask application using Blueprints?](#q43) <span class="intermediate">Intermediate</span>
44. [How do you use Django Signals to decouple logic?](#q44) <span class="intermediate">Intermediate</span>
45. [How do you use Pytest Fixtures with scopes?](#q45) <span class="intermediate">Intermediate</span>
46. [How do you implement Generics using TypeVar?](#q46) <span class="advanced">Advanced</span>
47. [How do you use Protocols for structural subtyping (Duck Typing)?](#q47) <span class="advanced">Advanced</span>
48. [How do you use Single Dispatch for function overloading?](#q48) <span class="intermediate">Intermediate</span>
49. [How do you use WeakRef to manage memory?](#q49) <span class="advanced">Advanced</span>
50. [How do you validate data using Pydantic?](#q50) <span class="intermediate">Intermediate</span>
51. [What is a Metaclass and when should you use it?](#q51) <span class="advanced">Expert</span>
52. [How do you implement a Descriptor?](#q52) <span class="advanced">Advanced</span>
53. [What is the difference between `__new__` and `__init__`?](#q53) <span class="advanced">Advanced</span>
54. [How does Python's Method Resolution Order (MRO) work?](#q54) <span class="advanced">Advanced</span>
55. [How do you use `contextlib.contextmanager`?](#q55) <span class="intermediate">Intermediate</span>
56. [How do you use Structural Pattern Matching (match/case)?](#q56) <span class="intermediate">Intermediate</span>
57. [How do you use `asyncio.TaskGroup` (Python 3.11+)?](#q57) <span class="advanced">Advanced</span>
58. [How do you use `typing.TypedDict`?](#q58) <span class="intermediate">Intermediate</span>
59. [How do you use `typing.Annotated` for metadata?](#q59) <span class="advanced">Advanced</span>
60. [When should you use `collections.deque` over a list?](#q60) <span class="intermediate">Intermediate</span>
61. [How do you use `collections.ChainMap` to merge scopes?](#q61) <span class="advanced">Advanced</span>
62. [How do you use `dataclasses` post-init processing?](#q62) <span class="intermediate">Intermediate</span>
63. [How do you preserve function metadata with decorators?](#q63) <span class="beginner">Beginner</span>
64. [How do you split an iterable using `itertools.tee`?](#q64) <span class="advanced">Advanced</span>
65. [How do you inspect Python bytecode?](#q65) <span class="advanced">Expert</span>
66. [What is a `memoryview` and when should you use it?](#q66) <span class="advanced">Advanced</span>
67. [How do you perform manual garbage collection?](#q67) <span class="advanced">Advanced</span>
68. [How do you share memory between processes?](#q68) <span class="advanced">Expert</span>
69. [How do you manage file paths using `pathlib`?](#q69) <span class="beginner">Beginner</span>
70. [How do you run concurrent tasks with `concurrent.futures`?](#q70) <span class="intermediate">Intermediate</span>
71. [How do you create a temporary file safely?](#q71) <span class="intermediate">Intermediate</span>
72. [How do you iterate over large directories efficiently?](#q72) <span class="intermediate">Intermediate</span>
73. [How do you parse command-line arguments?](#q73) <span class="beginner">Beginner</span>
74. [How do you implement custom logging handlers?](#q74) <span class="advanced">Advanced</span>
75. [How do you use `functools.partial` to freeze arguments?](#q75) <span class="intermediate">Intermediate</span>
76. [How do you mock dependencies with `unittest.mock`?](#q76) <span class="advanced">Advanced</span>
77. [How do you share setup code using Pytest fixtures?](#q77) <span class="intermediate">Intermediate</span>
78. [What is Property-Based Testing?](#q78) <span class="advanced">Expert</span>
79. [How do Django Signals work?](#q79) <span class="advanced">Advanced</span>
80. [What is Middleware in Django/Flask?](#q80) <span class="intermediate">Intermediate</span>
81. [How does Dependency Injection work in FastAPI?](#q81) <span class="advanced">Advanced</span>
82. [What is the N+1 Select Problem in ORMs?](#q82) <span class="advanced">Advanced</span>
83. [How do you chain tasks in Celery?](#q83) <span class="advanced">Advanced</span>
84. [What is `pyproject.toml`?](#q84) <span class="intermediate">Intermediate</span>
85. [How do you securely hash passwords?](#q85) <span class="intermediate">Intermediate</span>
86. [What is the difference between `zip` and `itertools.zip_longest`?](#q86) <span class="beginner">Beginner</span>
87. [How do you use `functools.reduce`?](#q87) <span class="intermediate">Intermediate</span>
88. [How do you sort objects by attribute using `operator`?](#q88) <span class="intermediate">Intermediate</span>
89. [How do you use Enums in Python?](#q89) <span class="beginner">Beginner</span>
90. [How do you generate cryptographically strong random numbers?](#q90) <span class="intermediate">Intermediate</span>
91. [How do you handle signals (like SIGINT/Ctrl+C)?](#q91) <span class="advanced">Advanced</span>
92. [How do you issue warnings in your code?](#q92) <span class="intermediate">Intermediate</span>
93. [How do you print the full stack trace programmatically?](#q93) <span class="intermediate">Intermediate</span>
94. [What is the `ast` module used for?](#q94) <span class="advanced">Expert</span>
95. [How do you dynamically import a module?](#q95) <span class="advanced">Advanced</span>
96. [How do you make an instance callable?](#q96) <span class="beginner">Beginner</span>
97. [How do you implement custom indexing (`[]`)?](#q97) <span class="intermediate">Intermediate</span>
98. [How do you implement a manual context manager?](#q98) <span class="intermediate">Intermediate</span>
99. [What is the difference between `__str__` and `__repr__`?](#q99) <span class="beginner">Beginner</span>
100. [What is "The Zen of Python"?](#q100) <span class="beginner">Beginner</span>

---

<a id="q1"></a>

### Q1: How do you optimize memory usage when processing large datasets in Python?

**Difficulty**: Intermediate

**Strategy:**
Use **Generators** instead of Lists. Generators yield items one by one using `yield`, consuming constant memory, whereas lists load everything into memory.

**Code Example:**

```python
# BAD: Loads all 1M items into memory
squares_list = [x**2 for x in range(1000000)]

# GOOD: Yields one item at a time
squares_gen = (x**2 for x in range(1000000))

for val in squares_gen:
    # Process val
    pass
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q2"></a>

### Q2: How do you ensure resources (files, sockets) are properly closed even if errors occur?

**Difficulty**: Beginner

**Strategy:**
Use **Context Managers** (the `with` statement). It guarantees that the `__exit__` method is called, cleaning up resources regardless of exceptions.

**Code Example:**

```python
# GOOD: File closes automatically
with open('data.txt', 'r') as f:
    data = f.read()
    # raise Exception("Error") # File still closes
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q3"></a>

### Q3: How do you implement a decorator to measure the execution time of a function?

**Difficulty**: Intermediate

**Strategy:**
Define a wrapper function inside the decorator that records start and end time, then calls the original function. Use `functools.wraps` to preserve metadata.

**Code Example:**

```python
import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.4f}s")
        return result
    return wrapper

@timer
def slow_task():
    time.sleep(1)

slow_task()
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q4"></a>

### Q4: How do you bypass the Global Interpreter Lock (GIL) for CPU-bound tasks?

**Difficulty**: Advanced

**Strategy:**
Use the **multiprocessing** module instead of `threading`. Processes have their own memory space and GIL, allowing true parallelism on multi-core CPUs.

**Code Example:**

```python
from multiprocessing import Pool

def square(n):
    return n * n

if __name__ == "__main__":
    with Pool(processes=4) as pool:
        results = pool.map(square, range(1000000))
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q5"></a>

### Q5: How do you handle concurrent I/O-bound operations efficiently?

**Difficulty**: Intermediate

**Strategy:**
Use **asyncio** for cooperative multitasking. It allows a single thread to handle many connections by suspending/resuming coroutines during I/O waits.

**Code Example:**

```python
import asyncio

async def fetch_data(id):
    print(f"Fetching {id}")
    await asyncio.sleep(1) # Simulate I/O
    return {"id": id}

async def main():
    # Run concurrently
    results = await asyncio.gather(fetch_data(1), fetch_data(2))
    print(results)

asyncio.run(main())
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q6"></a>

### Q6: How do you merge two dictionaries in Python 3.9+?

**Difficulty**: Beginner

**Strategy:**
Use the **Union Operator (`|`)**. It creates a new dictionary merging both, where the second overrides the first in case of key conflicts.

**Code Example:**

```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

merged = d1 | d2
# Result: {'a': 1, 'b': 3, 'c': 4}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q7"></a>

### Q7: How do you create a lightweight immutable data class?

**Difficulty**: Intermediate

**Strategy:**
Use **NamedTuple** (classic) or **dataclasses** with `frozen=True` (modern). This prevents modification after creation and uses less memory than standard dicts.

**Code Example:**

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int

p = Point(10, 20)
# p.x = 5 # Raises FrozenInstanceError
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q8"></a>

### Q8: How do you optimize function calls with caching (memoization)?

**Difficulty**: Intermediate

**Strategy:**
Use `@functools.lru_cache`. It caches the results of function calls based on arguments, avoiding redundant computations.

**Code Example:**

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)

print(fib(100)) # Computes instantly
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q9"></a>

### Q9: How do you enforce type safety in a large Python codebase?

**Difficulty**: Intermediate

**Strategy:**
Use **Type Hints** and run a static type checker like **mypy**. This catches type errors at development time rather than runtime.

**Code Example:**

```python
def greet(name: str) -> str:
    return f"Hello, {name}"

# mypy will flag this:
# greet(123)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q10"></a>

### Q10: How do you create a true deep copy of a nested object?

**Difficulty**: Beginner

**Strategy:**
Use `copy.deepcopy()`. Standard assignment copies references, and `copy.copy()` does a shallow copy. Deep copy recursively copies all nested objects.

**Code Example:**

```python
import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0][0] = 99
# shallow[0][0] is 99 (shared)
# deep[0][0] is 1 (independent)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q11"></a>

### Q11: How do you manage project dependencies effectively?

**Difficulty**: Intermediate

**Strategy:**
Use a virtual environment (`venv`, `pipenv`, or `poetry`) to isolate dependencies. Freeze versions in `requirements.txt` or `pyproject.toml`.

**Code Example:**

```python
# Create venv
python -m venv .venv
source .venv/bin/activate

# Install and freeze
pip install requests
pip freeze > requirements.txt
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q12"></a>

### Q12: How do you safely handle exceptions without crashing the app?

**Difficulty**: Beginner

**Strategy:**
Use `try-except` blocks. Catch specific exceptions (e.g., `ValueError`) rather than bare `except:` to avoid hiding bugs.

**Code Example:**

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"Unexpected error: {e}")
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q13"></a>

### Q13: How do you dynamically create classes or modify class behavior?

**Difficulty**: Advanced

**Strategy:**
Use **Metaclasses** or `type()`. A metaclass inherits from `type` and intercepts class creation, allowing you to modify attributes or methods automatically.

**Code Example:**

```python
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    pass
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q14"></a>

### Q14: How do you unpack a list with variable elements?

**Difficulty**: Beginner

**Strategy:**
Use the **star operator (`*`)** in assignment (Extended Iterable Unpacking). It captures excess items into a list.

**Code Example:**

```python
data = [1, 2, 3, 4, 5]
first, *middle, last = data

# first: 1
# middle: [2, 3, 4]
# last: 5
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q15"></a>

### Q15: How do you implement an iterator class manually?

**Difficulty**: Intermediate

**Strategy:**
Implement `__iter__` (returns self) and `__next__`. Raise `StopIteration` when done.

**Code Example:**

```python
class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration
        self.count += 1
        return self.count

for n in Counter(3):
    print(n)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q16"></a>

### Q16: How do you debug code using PDB?

**Difficulty**: Intermediate

**Strategy:**
Use `import pdb; pdb.set_trace()` (or `breakpoint()` in Python 3.7+) to pause execution and enter an interactive debugger. You can inspect variables, step through code (`n`), and continue (`c`).

**Code Example:**

```python
def divide(a, b):
    # breakpoint() # Python 3.7+
    import pdb; pdb.set_trace()
    return a / b

print(divide(10, 0))
# Execution pauses here, allowing inspection of 'a' and 'b'
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q17"></a>

### Q17: How do you optimize Pandas operations using Vectorization?

**Difficulty**: Intermediate

**Strategy:**
Avoid loops (`for`, `apply`) when working with Pandas DataFrames. Use built-in vectorized operations which push the loop into C-level code for performance.

**Code Example:**

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({'a': range(100000), 'b': range(100000)})

# Slow (Loop)
# df['c'] = df.apply(lambda row: row['a'] + row['b'], axis=1)

# Fast (Vectorized)
df['c'] = df['a'] + df['b']
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q18"></a>

### Q18: How do you use Numpy Broadcasting?

**Difficulty**: Intermediate

**Strategy:**
Broadcasting allows Numpy to perform arithmetic operations on arrays of different shapes. The smaller array is "broadcast" across the larger array so they have compatible shapes.

**Code Example:**

```python
import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]]) # Shape (2, 3)
B = np.array([10, 20, 30])           # Shape (3,)

# B is broadcast to [[10, 20, 30], [10, 20, 30]]
C = A + B
print(C)
# [[11, 22, 33],
#  [14, 25, 36]]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q19"></a>

### Q19: How do you create an async API endpoint with FastAPI?

**Difficulty**: Intermediate

**Strategy:**
Define path operation functions with `async def`. FastAPI runs these in an event loop. Use `await` for I/O bound operations.

**Code Example:**

```python
from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/")
async def read_root():
    # Simulate non-blocking I/O
    await asyncio.sleep(0.1)
    return {"message": "Hello World"}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q20"></a>

### Q20: How do you use ContextVars for thread-safe state management?

**Difficulty**: Advanced

**Strategy:**
`contextvars` module provides storage for state that is local to a context (like an asyncio task or a thread). It's the async equivalent of `threading.local()`.

**Code Example:**

```python
import contextvars
import asyncio

# Declare a context variable
request_id = contextvars.ContextVar('request_id', default=None)

async def process_request(id):
    request_id.set(id)
    await do_work()

async def do_work():
    # Access the variable safely
    print(f"Processing ID: {request_id.get()}")

asyncio.run(process_request('123'))
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q21"></a>

### Q21: How do you use the Walrus Operator (Assignment Expression)?

**Difficulty**: Beginner

**Strategy:**
The walrus operator `:=` assigns values to variables as part of a larger expression. Useful in `while` loops and `if` conditions to avoid redundant computations.

**Code Example:**

```python
# Without walrus
# data = f.read(1024)
# while data:
#     process(data)
#     data = f.read(1024)

# With walrus
# with open('file.txt') as f:
#     while (data := f.read(1024)):
#         process(data)
print("Supported in Python 3.8+")
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q22"></a>

### Q22: How do you implement abstract base classes (ABCs)?

**Difficulty**: Intermediate

**Strategy:**
Inherit from `abc.ABC` and decorate methods with `@abstractmethod`. This enforces that subclasses must implement these methods.

**Code Example:**

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# s = Shape() # Error: Can't instantiate abstract class
c = Circle(5) # OK
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q23"></a>

### Q23: How do you use Python's gc module to handle cyclic references?

**Difficulty**: Advanced

**Strategy:**
Python uses reference counting, but cyclic references (A->B->A) are handled by the Garbage Collector. Use `gc.collect()` to force collection or `gc.set_debug()` to debug leaks.

**Code Example:**

```python
import gc

class Node:
    def __init__(self):
        self.ref = None

a = Node()
b = Node()
a.ref = b
b.ref = a

del a
del b
# Cycle exists, ref count > 0
print(gc.collect()) # Returns number of objects collected (2)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q24"></a>

### Q24: How do you use **slots** to optimize memory?

**Difficulty**: Intermediate

**Strategy:**
Define `__slots__` in a class to explicitly declare data members. This prevents the creation of `__dict__` for each instance, saving memory.

**Code Example:**

```python
class Point:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)
# p.z = 3 # Error: 'Point' object has no attribute 'z'
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q25"></a>

### Q25: How do you use Itertools to chain iterables?

**Difficulty**: Intermediate

**Strategy:**
`itertools.chain()` allows you to iterate over multiple iterables as if they were one sequence, without creating a large combined list in memory.

**Code Example:**

```python
import itertools

list1 = [1, 2, 3]
list2 = [4, 5, 6]

for item in itertools.chain(list1, list2):
    print(item, end=' ')
# Output: 1 2 3 4 5 6
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q26"></a>

### Q26: How do you use defaultdict for cleaner grouping code?

**Difficulty**: Beginner

**Strategy:**
`collections.defaultdict` automatically initializes dictionary values if the key is missing. Useful for grouping or counting without checking `if key in dict`.

**Code Example:**

```python
from collections import defaultdict

words = ['apple', 'banana', 'apple', 'cherry']
count = defaultdict(int)

for word in words:
    count[word] += 1

print(dict(count))
# {'apple': 2, 'banana': 1, 'cherry': 1}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q27"></a>

### Q27: How do you use unittest.mock to mock dependencies?

**Difficulty**: Intermediate

**Strategy:**
Use `Mock` or `patch` to replace real objects with mock objects during tests. This isolates the code under test.

**Code Example:**

```python
from unittest.mock import patch, MagicMock

# Mocking a function
mock = MagicMock()
mock.return_value = 42
print(mock()) # 42

# Example patch usage:
# @patch('requests.get')
# def test_api(mock_get):
#     mock_get.return_value.status_code = 200
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q28"></a>

### Q28: How do you use functools.partial?

**Difficulty**: Intermediate

**Strategy:**
`partial` creates a new function with some arguments of the original function pre-filled (frozen).

**Code Example:**

```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(4)) # 16
print(cube(4))   # 64
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q29"></a>

### Q29: How do you use threading.Event for thread synchronization?

**Difficulty**: Intermediate

**Strategy:**
An Event is a simple synchronization primitive where one thread signals an event and other threads wait for it.

**Code Example:**

```python
import threading
import time

event = threading.Event()

def worker():
    print("Worker waiting")
    event.wait()
    print("Worker activated")

t = threading.Thread(target=worker)
t.start()

time.sleep(0.1)
print("Main signaling event")
event.set()
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q30"></a>

### Q30: How do you run shell commands with subprocess.run?

**Difficulty**: Intermediate

**Strategy:**
Use `subprocess.run()` (Python 3.5+) to execute shell commands. It waits for the command to complete and returns a `CompletedProcess` instance.

**Code Example:**

```python
import subprocess

result = subprocess.run(
    ['echo', 'Hello from shell'],
    capture_output=True,
    text=True
)

print(result.stdout.strip())
# Hello from shell
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q31"></a>

### Q31: How do you use json.dumps with a custom encoder?

**Difficulty**: Intermediate

**Strategy:**
To serialize objects that aren't JSON serializable by default (like datetime), subclass `json.JSONEncoder` and implement `default`.

**Code Example:**

```python
import json
from datetime import datetime

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

data = {'time': datetime.now()}
print(json.dumps(data, cls=DateTimeEncoder))
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q32"></a>

### Q32: How do you use collections.Counter?

**Difficulty**: Beginner

**Strategy:**
`Counter` is a dict subclass for counting hashable objects. It provides methods like `most_common()`.

**Code Example:**

```python
from collections import Counter

data = [1, 2, 2, 3, 3, 3]
c = Counter(data)

print(c.most_common(1))
# [(3, 3)]  (Element 3 appeared 3 times)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q33"></a>

### Q33: How do you use heapq for a priority queue?

**Difficulty**: Intermediate

**Strategy:**
`heapq` provides an implementation of the heap queue algorithm (min heap). Use `heappush` and `heappop`.

**Code Example:**

```python
import heapq

h = []
heapq.heappush(h, (5, 'write code'))
heapq.heappush(h, (1, 'fix bug'))
heapq.heappush(h, (3, 'review PR'))

print(heapq.heappop(h))
# (1, 'fix bug')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q34"></a>

### Q34: How do you use zip to iterate over multiple lists?

**Difficulty**: Beginner

**Strategy:**
`zip` aggregates elements from each of the iterables. Useful for iterating over two lists in parallel.

**Code Example:**

```python
names = ['Alice', 'Bob']
ages = [25, 30]

for name, age in zip(names, ages):
    print(f"{name} is {age}")
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q35"></a>

### Q35: How do you use enumerate?

**Difficulty**: Beginner

**Strategy:**
`enumerate` adds a counter to an iterable and returns it as an enumerate object.

**Code Example:**

```python
items = ['a', 'b', 'c']
for i, item in enumerate(items):
    print(f"{i}: {item}")
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q36"></a>

### Q36: How do you use if **name** == "**main**":?

**Difficulty**: Beginner

**Strategy:**
This block checks if the script is being run directly or imported as a module. Code inside it won't run when imported.

**Code Example:**

```python
def main():
    print("Main function")

if __name__ == "__main__":
    main()
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q37"></a>

### Q37: How do you use re module for regex matching?

**Difficulty**: Intermediate

**Strategy:**
Use `re.search()` or `re.match()` to find patterns in strings. `re.findall()` finds all occurrences.

**Code Example:**

```python
import re

text = "Contact: 123-456-7890"
match = re.search(r'\d{3}-\d{3}-\d{4}', text)

if match:
    print(f"Found: {match.group()}")
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q38"></a>

### Q38: How do you use with statement (Context Managers)?

**Difficulty**: Beginner

**Strategy:**
The `with` statement simplifies exception handling by encapsulating common preparation and cleanup tasks (like closing files).

**Code Example:**

```python
# Automatically closes file even if error occurs
# with open('file.txt', 'w') as f:
#     f.write('Hello')
print("File closed automatically")
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q39"></a>

### Q39: How do you use Generators (yield)?

**Difficulty**: Intermediate

**Strategy:**
Generators allow you to declare a function that behaves like an iterator. `yield` produces a value and suspends the function's execution.

**Code Example:**

```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for num in count_up_to(3):
    print(num)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q40"></a>

### Q40: How do you use Decorators?

**Difficulty**: Intermediate

**Strategy:**
Decorators modify the behavior of a function or class. They wrap another function.

**Code Example:**

```python
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q41"></a>

### Q41: How do you implement asynchronous tasks with Celery?

**Difficulty**: Advanced

**Strategy:**
Use **Celery** with a message broker (RabbitMQ/Redis). Define tasks with `@app.task` and call them using `.delay()`. This offloads heavy work to background workers.

**Code Example:**

```python
from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def add(x, y):
    return x + y

# Call asynchronously
result = add.delay(4, 4)
print(f"Task ID: {result.id}")
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q42"></a>

### Q42: How do you define a One-to-Many relationship in SQLAlchemy?

**Difficulty**: Intermediate

**Strategy:**
Use `ForeignKey` on the 'Many' side and `relationship` on the 'One' side. `back_populates` synchronizes changes between the two objects.

**Code Example:**

```python
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    posts = relationship("Post", back_populates="author")

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    author = relationship("User", back_populates="posts")
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q43"></a>

### Q43: How do you structure a large Flask application using Blueprints?

**Difficulty**: Intermediate

**Strategy:**
Use **Blueprints** to organize routes into modules (e.g., auth, admin, api). Register them in the main application factory.

**Code Example:**

```python
# auth.py
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login')
def login(): return "Login"

# app.py
app = Flask(__name__)
app.register_blueprint(auth_bp, url_prefix='/auth')
# Access: /auth/login
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q44"></a>

### Q44: How do you use Django Signals to decouple logic?

**Difficulty**: Intermediate

**Strategy:**
Signals allow senders to notify receivers when actions occur. Use `@receiver` with signals like `post_save` to trigger side effects (e.g., creating a profile when a user is created).

**Code Example:**

```python
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q45"></a>

### Q45: How do you use Pytest Fixtures with scopes?

**Difficulty**: Intermediate

**Strategy:**
Fixtures provide setup/teardown code. Use `scope` ('function', 'module', 'session') to control how often the fixture runs. 'session' runs once per test suite.

**Code Example:**

```python
@pytest.fixture(scope="session")
def db_connection():
    conn = connect_db()
    yield conn
    conn.close()

def test_query(db_connection):
    assert db_connection.query("SELECT 1")
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q46"></a>

### Q46: How do you implement Generics using TypeVar?

**Difficulty**: Advanced

**Strategy:**
Use `TypeVar` to create a generic type variable. This allows functions or classes to work with multiple types while maintaining type safety.

**Code Example:**

```python
from typing import TypeVar, List

T = TypeVar('T')

def first_element(items: List[T]) -> T:
    return items[0]

# first_element([1, 2]) -> int
# first_element(["a", "b"]) -> str
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q47"></a>

### Q47: How do you use Protocols for structural subtyping (Duck Typing)?

**Difficulty**: Advanced

**Strategy:**
Use `typing.Protocol`. A class satisfies a Protocol if it implements the declared methods, even if it doesn't explicitly inherit from it.

**Code Example:**

```python
class Drawable(Protocol):
    def draw(self) -> None: ...

class Circle:
    def draw(self) -> None: print("O")

def render(obj: Drawable):
    obj.draw()

render(Circle()) # Valid
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q48"></a>

### Q48: How do you use Single Dispatch for function overloading?

**Difficulty**: Intermediate

**Strategy:**
Use `@functools.singledispatch`. It allows you to define a generic function and register specialized implementations based on the type of the first argument.

**Code Example:**

```python
@singledispatch
def process(arg):
    print("Default processing")

@process.register
def _(arg: int):
    print(f"Processing int: {arg}")

@process.register
def _(arg: list):
    print(f"Processing list: {len(arg)}")
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q49"></a>

### Q49: How do you use WeakRef to manage memory?

**Difficulty**: Advanced

**Strategy:**
Use `weakref` to create references that don't prevent the referent from being garbage collected. Useful for caches or circular references.

**Code Example:**

```python
import weakref

class BigObject: pass

obj = BigObject()
r = weakref.ref(obj)

print(r()) # Access object
del obj
print(r()) # None (object was collected)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q50"></a>

### Q50: How do you validate data using Pydantic?

**Difficulty**: Intermediate

**Strategy:**
Define a model inheriting from `BaseModel`. Pydantic parses and validates data types at runtime, raising errors for invalid data.

**Code Example:**

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str

# Parses dict to object, converts types if possible
user = User(id="123", name="Alice", email="alice@example.com")
print(user.id) # 123 (int)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---
<a id="q51"></a>

### Q51: What is a Metaclass and when should you use it?

**Difficulty**: Expert

**Strategy:**
A metaclass is a class of a class. It controls how classes are created. You use it to modify class creation, enforce coding standards, or automatically register classes.

**Code Example:**

```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        dct['category'] = 'custom'
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

print(MyClass.category) # custom
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q52"></a>

### Q52: How do you implement a Descriptor?

**Difficulty**: Advanced

**Strategy:**
Descriptors are objects that define how attributes are accessed using `__get__`, `__set__`, or `__delete__`. They are the mechanism behind properties, methods, and bound fields.

**Code Example:**

```python
class PositiveNumber:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, type=None):
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value):
        if value < 0:
            raise ValueError("Must be positive")
        obj.__dict__[self.name] = value

class Account:
    balance = PositiveNumber()

acc = Account()
acc.balance = 100 # OK
# acc.balance = -10 # ValueError
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q53"></a>

### Q53: What is the difference between `__new__` and `__init__`?

**Difficulty**: Advanced

**Strategy:**
`__new__` is a static method responsible for _creating_ the instance (returning it). `__init__` is an instance method responsible for _initializing_ the created instance. `__new__` runs before `__init__`.

**Code Example:**

```python
class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

a = Singleton()
b = Singleton()
print(a is b) # True
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q54"></a>

### Q54: How does Python's Method Resolution Order (MRO) work?

**Difficulty**: Advanced

**Strategy:**
Python uses the C3 Linearization algorithm to determine the order in which base classes are searched for a method. Use `ClassName.mro()` to inspect it.

**Code Example:**

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print(D.mro())
# [D, B, C, A, object]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q55"></a>

### Q55: How do you use `contextlib.contextmanager`?

**Difficulty**: Intermediate

**Strategy:**
It's a decorator that converts a generator into a context manager, avoiding the need to write a full class with `__enter__` and `__exit__`.

**Code Example:**

```python
from contextlib import contextmanager

@contextmanager
def open_file(path, mode):
    f = open(path, mode)
    try:
        yield f
    finally:
        f.close()

# with open_file('test.txt', 'w') as f:
#     f.write('hello')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q56"></a>

### Q56: How do you use Structural Pattern Matching (match/case)?

**Difficulty**: Intermediate

**Strategy:**
Introduced in Python 3.10, `match/case` allows matching data structures against patterns, unpacking them, and binding variables.

**Code Example:**

```python
def handle_command(command):
    match command:
        case ["quit"]:
            print("Quitting")
        case ["move", x, y]:
            print(f"Moving to {x}, {y}")
        case _:
            print("Unknown command")

handle_command(["move", 10, 20])
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q57"></a>

### Q57: How do you use `asyncio.TaskGroup` (Python 3.11+)?

**Difficulty**: Advanced

**Strategy:**
`TaskGroup` provides a safer way to manage multiple async tasks. If one task fails, others are cancelled, and exceptions are grouped.

**Code Example:**

```python
import asyncio

async def worker(n):
    await asyncio.sleep(n)
    return n

async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(worker(1))
        task2 = tg.create_task(worker(2))

    print(task1.result(), task2.result())

# asyncio.run(main())
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q58"></a>

### Q58: How do you use `typing.TypedDict`?

**Difficulty**: Intermediate

**Strategy:**
`TypedDict` defines a dictionary where specific keys have specific types. It provides type checking for dictionary structures.

**Code Example:**

```python
from typing import TypedDict

class User(TypedDict):
    name: str
    id: int

user: User = {"name": "Alice", "id": 1}
# user: User = {"name": "Alice", "id": "1"} # Type Error
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q59"></a>

### Q59: How do you use `typing.Annotated` for metadata?

**Difficulty**: Advanced

**Strategy:**
`Annotated` allows attaching runtime metadata to types. It's often used by frameworks (like FastAPI) for dependency injection or validation.

**Code Example:**

```python
from typing import Annotated

def process(value: Annotated[int, "Needs to be positive"]):
    print(value)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q60"></a>

### Q60: When should you use `collections.deque` over a list?

**Difficulty**: Intermediate

**Strategy:**
Use `deque` (double-ended queue) for efficient appends and pops from _both_ ends (O(1)). Lists are O(n) for popping from the beginning.

**Code Example:**

```python
from collections import deque

d = deque([1, 2, 3])
d.appendleft(0) # O(1)
d.popleft()     # O(1)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q61"></a>

### Q61: How do you use `collections.ChainMap` to merge scopes?

**Difficulty**: Advanced

**Strategy:**
`ChainMap` groups multiple dicts into a single mapping. Lookups search the dicts in order. Useful for managing scopes (local, global, built-in).

**Code Example:**

```python
from collections import ChainMap

defaults = {'theme': 'dark', 'show_errors': False}
config = {'show_errors': True}

settings = ChainMap(config, defaults)
print(settings['theme'])       # dark
print(settings['show_errors']) # True
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q62"></a>

### Q62: How do you use `dataclasses` post-init processing?

**Difficulty**: Intermediate

**Strategy:**
Use `__post_init__` to validate fields or calculate derived fields after the object is initialized.

**Code Example:**

```python
from dataclasses import dataclass

@dataclass
class Box:
    width: float
    height: float
    area: float = 0.0

    def __post_init__(self):
        self.area = self.width * self.height

b = Box(2, 5)
print(b.area) # 10.0
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q63"></a>

### Q63: How do you preserve function metadata with decorators?

**Difficulty**: Beginner

**Strategy:**
Use `@functools.wraps(func)` inside your decorator. This copies the original function's name, docstring, and annotations to the wrapper.

**Code Example:**

```python
from functools import wraps

def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Calling")
        return func(*args, **kwargs)
    return wrapper

@log
def my_func():
    """Docstring"""
    pass

print(my_func.__name__) # my_func (not wrapper)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q64"></a>

### Q64: How do you split an iterable using `itertools.tee`?

**Difficulty**: Advanced

**Strategy:**
`tee` creates independent iterators from a single iterable. Be careful: if you consume one much faster than the other, memory usage grows.

**Code Example:**

```python
import itertools

data = [1, 2, 3]
it1, it2 = itertools.tee(data)

print(list(it1)) # [1, 2, 3]
print(list(it2)) # [1, 2, 3]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q65"></a>

### Q65: How do you inspect Python bytecode?

**Difficulty**: Expert

**Strategy:**
Use the `dis` module to disassemble Python code. This helps understand how Python executes your code under the hood.

**Code Example:**

```python
import dis

def add(a, b):
    return a + b

dis.dis(add)
# Output shows LOAD_FAST, BINARY_ADD, RETURN_VALUE instructions
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q66"></a>

### Q66: What is a `memoryview` and when should you use it?

**Difficulty**: Advanced

**Strategy:**
`memoryview` allows zero-copy access to the internal data of an object (like `bytes`). It allows manipulating large data buffers without copying.

**Code Example:**

```python
data = bytearray(b'hello')
mv = memoryview(data)

mv[0] = 72 # 'H'
print(data) # bytearray(b'Hello')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q67"></a>

### Q67: How do you perform manual garbage collection?

**Difficulty**: Advanced

**Strategy:**
Python uses reference counting + a cyclic garbage collector. Use the `gc` module to force a collection or inspect uncollectable objects.

**Code Example:**

```python
import gc

# Force collection
collected = gc.collect()
print(f"Garbage collector: collected {collected} objects.")
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q68"></a>

### Q68: How do you share memory between processes?

**Difficulty**: Expert

**Strategy:**
Use `multiprocessing.shared_memory`. It allocates a block of memory that different processes can attach to, avoiding serialization overhead.

**Code Example:**

```python
from multiprocessing.shared_memory import SharedMemory

# Create shared memory block
shm = SharedMemory(create=True, size=10)
shm.buf[0] = 100

# In another process...
# existing_shm = SharedMemory(name=shm.name)
# print(existing_shm.buf[0])

shm.close()
shm.unlink()
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q69"></a>

### Q69: How do you manage file paths using `pathlib`?

**Difficulty**: Beginner

**Strategy:**
`pathlib` provides an object-oriented interface to filesystem paths, replacing most `os.path` functions. It's cleaner and cross-platform.

**Code Example:**

```python
from pathlib import Path

p = Path('folder') / 'subfolder' / 'file.txt'
# p.write_text('content')
print(p.suffix) # .txt
print(p.parent) # folder/subfolder
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q70"></a>

### Q70: How do you run concurrent tasks with `concurrent.futures`?

**Difficulty**: Intermediate

**Strategy:**
It provides a high-level interface for asynchronously executing callables using threads or processes. `ThreadPoolExecutor` for I/O, `ProcessPoolExecutor` for CPU.

**Code Example:**

```python
from concurrent.futures import ThreadPoolExecutor

def task(n):
    return n * n

with ThreadPoolExecutor(max_workers=2) as executor:
    future = executor.submit(task, 5)
    print(future.result()) # 25
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q71"></a>

### Q71: How do you create a temporary file safely?

**Difficulty**: Intermediate

**Strategy:**
Use the `tempfile` module. `NamedTemporaryFile` or `TemporaryDirectory` creates files/dirs that are automatically deleted when closed or when the context exits.

**Code Example:**

```python
import tempfile

with tempfile.NamedTemporaryFile(delete=True) as tmp:
    tmp.write(b"Hello")
    tmp.flush()
    print(tmp.name)
# File is gone here
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q72"></a>

### Q72: How do you iterate over large directories efficiently?

**Difficulty**: Intermediate

**Strategy:**
Use `os.scandir()` instead of `os.listdir()`. It returns an iterator of `DirEntry` objects containing file attribute information, avoiding additional system calls.

**Code Example:**

```python
import os

with os.scandir('.') as it:
    for entry in it:
        if entry.is_file():
            print(entry.name)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q73"></a>

### Q73: How do you parse command-line arguments?

**Difficulty**: Beginner

**Strategy:**
Use the `argparse` library. It handles positional args, flags, type conversion, and help messages automatically.

**Code Example:**

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name', help='Your name')
args = parser.parse_args()

if args.name:
    print(f"Hello {args.name}")
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q74"></a>

### Q74: How do you implement custom logging handlers?

**Difficulty**: Advanced

**Strategy:**
Inherit from `logging.Handler` and implement the `emit` method. This allows sending logs to external services, databases, or custom formats.

**Code Example:**

```python
import logging

class ListHandler(logging.Handler):
    def __init__(self, log_list):
        super().__init__()
        self.log_list = log_list

    def emit(self, record):
        self.log_list.append(self.format(record))

logs = []
logger = logging.getLogger()
logger.addHandler(ListHandler(logs))
logger.warning("Alert")
print(logs) # ['Alert']
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q75"></a>

### Q75: How do you use `functools.partial` to freeze arguments?

**Difficulty**: Intermediate

**Strategy:**
`partial` creates a new function with some arguments of the original function fixed. Useful for callbacks or simplifying function signatures.

**Code Example:**

```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(5)) # 25
print(cube(5))   # 125
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---
<a id="q76"></a>

### Q76: How do you mock dependencies with `unittest.mock`?

**Difficulty**: Advanced

**Strategy:**
Use `@patch` to replace objects with `Mock` objects during tests. This isolates the code under test from external systems (APIs, DBs).

**Code Example:**

```python
from unittest.mock import patch

def get_data():
    # Imagine this calls an API
    return "Real Data"

@patch('__main__.get_data')
def test_get_data(mock_get):
    mock_get.return_value = "Mocked Data"
    assert get_data() == "Mocked Data"

test_get_data()
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q77"></a>

### Q77: How do you share setup code using Pytest fixtures?

**Difficulty**: Intermediate

**Strategy:**
Fixtures provide a fixed baseline for tests. Use `@pytest.fixture` with scopes (function, module, session) to manage resource lifecycles.

**Code Example:**

```python
import pytest

@pytest.fixture(scope="module")
def db_connection():
    conn = {"status": "connected"}
    yield conn
    conn["status"] = "closed"

def test_db(db_connection):
    assert db_connection["status"] == "connected"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q78"></a>

### Q78: What is Property-Based Testing?

**Difficulty**: Expert

**Strategy:**
Instead of writing specific examples, you define properties that should hold true for a range of inputs. Libraries like `hypothesis` generate edge cases automatically.

**Code Example:**

```python
# pip install hypothesis
from hypothesis import given, strategies as st

def add(a, b):
    return a + b

@given(st.integers(), st.integers())
def test_add_commutative(a, b):
    assert add(a, b) == add(b, a)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q79"></a>

### Q79: How do Django Signals work?

**Difficulty**: Advanced

**Strategy:**
Signals allow decoupled applications to get notified when actions occur elsewhere. Common uses: post-save hooks to trigger side effects (sending emails).

**Code Example:**

```python
# Django specific
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        print(f"Profile created for {instance.username}")
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q80"></a>

### Q80: What is Middleware in Django/Flask?

**Difficulty**: Intermediate

**Strategy:**
Middleware is a hook into the request/response processing. It's a lightweight, low-level plugin system for globally altering input or output.

**Code Example:**

```python
# Simple function-based middleware
def simple_middleware(get_response):
    def middleware(request):
        print("Before view")
        response = get_response(request)
        print("After view")
        return response
    return middleware
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q81"></a>

### Q81: How does Dependency Injection work in FastAPI?

**Difficulty**: Advanced

**Strategy:**
FastAPI uses the `Depends` class to declare dependencies. The framework handles creating and passing these dependencies, supporting caching and sub-dependencies.

**Code Example:**

```python
from fastapi import Depends

def get_db():
    return "Database Connection"

def read_users(db = Depends(get_db)):
    return {"db": db}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q82"></a>

### Q82: What is the N+1 Select Problem in ORMs?

**Difficulty**: Advanced

**Strategy:**
It happens when code iterates a list of objects and performs an additional query for each object. Solve it using eager loading (`select_related` or `joinedload`).

**Code Example:**

```python
# SQLAlchemy example
# Bad: Query for users, then query for address per user
# Good:
# session.query(User).options(joinedload(User.address)).all()
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q83"></a>

### Q83: How do you chain tasks in Celery?

**Difficulty**: Advanced

**Strategy:**
Use `chain` to link tasks together so the output of one becomes the input of the next. Use `group` for parallel execution.

**Code Example:**

```python
from celery import chain

# res = chain(add.s(4, 4), mul.s(8))()
# (4 + 4) * 8
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q84"></a>

### Q84: What is `pyproject.toml`?

**Difficulty**: Intermediate

**Strategy:**
It is the new standard for defining build system requirements and project configuration in Python, replacing `setup.py` and `requirements.txt` for packaging.

**Code Example:**

```toml
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "my_package"
version = "0.1.0"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q85"></a>

### Q85: How do you securely hash passwords?

**Difficulty**: Intermediate

**Strategy:**
Never store plain passwords. Use a library like `bcrypt` or `passlib` which handles salting and hashing using slow algorithms (Argon2, bcrypt).

**Code Example:**

```python
import bcrypt

password = b"secret"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

if bcrypt.checkpw(password, hashed):
    print("Match")
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q86"></a>

### Q86: What is the difference between `zip` and `itertools.zip_longest`?

**Difficulty**: Beginner

**Strategy:**
`zip` stops when the shortest iterable is exhausted. `zip_longest` fills missing values with a `fillvalue` (default `None`) until the longest iterable is exhausted.

**Code Example:**

```python
from itertools import zip_longest

a = [1, 2]
b = [3, 4, 5]

print(list(zip(a, b))) # [(1, 3), (2, 4)]
print(list(zip_longest(a, b, fillvalue=0)))
# [(1, 3), (2, 4), (0, 5)]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q87"></a>

### Q87: How do you use `functools.reduce`?

**Difficulty**: Intermediate

**Strategy:**
`reduce` applies a rolling computation to sequential pairs of values in a list. Commonly used for cumulative operations (like product of a list).

**Code Example:**

```python
from functools import reduce

nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product) # 24
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q88"></a>

### Q88: How do you sort objects by attribute using `operator`?

**Difficulty**: Intermediate

**Strategy:**
`operator.attrgetter` creates a callable that fetches an attribute. It is faster and cleaner than writing a lambda for `key=`.

**Code Example:**

```python
from operator import attrgetter

class User:
    def __init__(self, name):
        self.name = name

users = [User('Bob'), User('Alice')]
users.sort(key=attrgetter('name'))
print(users[0].name) # Alice
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q89"></a>

### Q89: How do you use Enums in Python?

**Difficulty**: Beginner

**Strategy:**
Use the `enum` module to define symbolic names bound to constant values. `IntEnum` allows comparison with integers.

**Code Example:**

```python
from enum import Enum, auto

class Color(Enum):
    RED = auto()
    GREEN = auto()

print(Color.RED)
print(Color.RED.name)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q90"></a>

### Q90: How do you generate cryptographically strong random numbers?

**Difficulty**: Intermediate

**Strategy:**
Use the `secrets` module instead of `random`. `random` is pseudo-random and predictable; `secrets` handles secure tokens and passwords.

**Code Example:**

```python
import secrets

token = secrets.token_hex(16)
print(token)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q91"></a>

### Q91: How do you handle signals (like SIGINT/Ctrl+C)?

**Difficulty**: Advanced

**Strategy:**
Use the `signal` module to register a handler for system signals. This allows for graceful shutdowns (closing DB connections, saving state).

**Code Example:**

```python
import signal
import sys

def handler(signum, frame):
    print("Gracefully exiting...")
    sys.exit(0)

signal.signal(signal.SIGINT, handler)
# While True: pass
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q92"></a>

### Q92: How do you issue warnings in your code?

**Difficulty**: Intermediate

**Strategy:**
Use the `warnings` module to alert users about deprecated features or potential issues without raising an exception that stops execution.

**Code Example:**

```python
import warnings

def old_func():
    warnings.warn("Deprecated", DeprecationWarning)

old_func()
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q93"></a>

### Q93: How do you print the full stack trace programmatically?

**Difficulty**: Intermediate

**Strategy:**
Use `traceback.print_exc()` inside an `except` block to print the full error trace to stderr.

**Code Example:**

```python
import traceback

try:
    1 / 0
except ZeroDivisionError:
    traceback.print_exc()
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q94"></a>

### Q94: What is the `ast` module used for?

**Difficulty**: Expert

**Strategy:**
The Abstract Syntax Tree (`ast`) module allows you to inspect and modify the tree structure of Python code itself. Used by linters and code generators.

**Code Example:**

```python
import ast

code = "x = 1 + 2"
tree = ast.parse(code)
print(type(tree.body[0])) # <class 'ast.Assign'>
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q95"></a>

### Q95: How do you dynamically import a module?

**Difficulty**: Advanced

**Strategy:**
Use `importlib.import_module`. This allows importing modules where the name is only known at runtime (e.g., plugins).

**Code Example:**

```python
import importlib

math_mod = importlib.import_module("math")
print(math_mod.sqrt(4))
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q96"></a>

### Q96: How do you make an instance callable?

**Difficulty**: Beginner

**Strategy:**
Implement the `__call__` magic method. This allows the object to be used like a function.

**Code Example:**

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

double = Multiplier(2)
print(double(5)) # 10
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q97"></a>

### Q97: How do you implement custom indexing (`[]`)?

**Difficulty**: Intermediate

**Strategy:**
Implement `__getitem__` (for reading) and `__setitem__` (for writing). This allows your object to behave like a list or dictionary.

**Code Example:**

```python
class MyList:
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data.get(key, 0)

    def __setitem__(self, key, value):
        self.data[key] = value

m = MyList()
m['a'] = 10
print(m['a'])
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q98"></a>

### Q98: How do you implement a manual context manager?

**Difficulty**: Intermediate

**Strategy:**
Implement `__enter__` and `__exit__`. `__enter__` sets up the resource and returns it. `__exit__` cleans it up, handling any exceptions.

**Code Example:**

```python
class HelloContext:
    def __enter__(self):
        print("Entering")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting")

with HelloContext():
    print("Inside")
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q99"></a>

### Q99: What is the difference between `__str__` and `__repr__`?

**Difficulty**: Beginner

**Strategy:**
`__str__` is for a readable string representation (for users). `__repr__` is for an unambiguous representation (for developers, ideally valid Python code).

**Code Example:**

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return f"Point at {self.x}, {self.y}"

p = Point(1, 2)
print(str(p))  # Point at 1, 2
print(repr(p)) # Point(1, 2)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q100"></a>

### Q100: What is "The Zen of Python"?

**Difficulty**: Beginner

**Strategy:**
It is a collection of guiding principles for writing computer programs in Python. Access it by running `import this`. Key principles: "Explicit is better than implicit", "Simple is better than complex".

**Code Example:**

```python
import this
# Prints the Zen of Python
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>
