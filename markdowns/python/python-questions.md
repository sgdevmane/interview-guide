<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>Python Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for developers</b></p>
</div>

---

## Table of Contents

1. [How do you optimize memory usage when processing large datasets in Python?](#q1-how-do-you-optimize-memory-usage-when-processing-large-datasets-in-python) <span class="intermediate">Intermediate</span>
2. [How do you ensure resources (files, sockets) are properly closed even if errors occur?](#q2-how-do-you-ensure-resources-files-sockets-are-properly-closed-even-if-errors-occur) <span class="beginner">Beginner</span>
3. [How do you implement a decorator to measure the execution time of a function?](#q3-how-do-you-implement-a-decorator-to-measure-the-execution-time-of-a-function) <span class="intermediate">Intermediate</span>
4. [How do you bypass the Global Interpreter Lock (GIL) for CPU-bound tasks?](#q4-how-do-you-bypass-the-global-interpreter-lock-gil-for-cpu-bound-tasks) <span class="advanced">Advanced</span>
5. [How do you handle concurrent I/O-bound operations efficiently?](#q5-how-do-you-handle-concurrent-io-bound-operations-efficiently) <span class="intermediate">Intermediate</span>
6. [How do you merge two dictionaries in Python 3.9+?](#q6-how-do-you-merge-two-dictionaries-in-python-39) <span class="beginner">Beginner</span>
7. [How do you create a lightweight immutable data class?](#q7-how-do-you-create-a-lightweight-immutable-data-class) <span class="intermediate">Intermediate</span>
8. [How do you optimize function calls with caching (memoization)?](#q8-how-do-you-optimize-function-calls-with-caching-memoization) <span class="intermediate">Intermediate</span>
9. [How do you enforce type safety in a large Python codebase?](#q9-how-do-you-enforce-type-safety-in-a-large-python-codebase) <span class="intermediate">Intermediate</span>
10. [How do you create a true deep copy of a nested object?](#q10-how-do-you-create-a-true-deep-copy-of-a-nested-object) <span class="beginner">Beginner</span>
11. [How do you manage project dependencies effectively?](#q11-how-do-you-manage-project-dependencies-effectively) <span class="intermediate">Intermediate</span>
12. [How do you safely handle exceptions without crashing the app?](#q12-how-do-you-safely-handle-exceptions-without-crashing-the-app) <span class="beginner">Beginner</span>
13. [How do you dynamically create classes or modify class behavior?](#q13-how-do-you-dynamically-create-classes-or-modify-class-behavior) <span class="advanced">Advanced</span>
14. [How do you unpack a list with variable elements?](#q14-how-do-you-unpack-a-list-with-variable-elements) <span class="beginner">Beginner</span>
15. [How do you implement an iterator class manually?](#q15-how-do-you-implement-an-iterator-class-manually) <span class="intermediate">Intermediate</span>
16. [How do you debug code using PDB?](#q16-how-do-you-debug-code-using-pdb) <span class="intermediate">Intermediate</span>
17. [How do you optimize Pandas operations using Vectorization?](#q17-how-do-you-optimize-pandas-operations-using-vectorization) <span class="intermediate">Intermediate</span>
18. [How do you use Numpy Broadcasting?](#q18-how-do-you-use-numpy-broadcasting) <span class="intermediate">Intermediate</span>
19. [How do you create an async API endpoint with FastAPI?](#q19-how-do-you-create-an-async-api-endpoint-with-fastapi) <span class="intermediate">Intermediate</span>
20. [How do you use ContextVars for thread-safe state management?](#q20-how-do-you-use-contextvars-for-thread-safe-state-management) <span class="advanced">Advanced</span>
21. [How do you use the Walrus Operator (Assignment Expression)?](#q21-how-do-you-use-the-walrus-operator-assignment-expression) <span class="beginner">Beginner</span>
22. [How do you implement abstract base classes (ABCs)?](#q22-how-do-you-implement-abstract-base-classes-abcs) <span class="intermediate">Intermediate</span>
23. [How do you use Python's gc module to handle cyclic references?](#q23-how-do-you-use-pythons-gc-module-to-handle-cyclic-references) <span class="advanced">Advanced</span>
24. [How do you use __slots__ to optimize memory?](#q24-how-do-you-use-__slots__-to-optimize-memory) <span class="intermediate">Intermediate</span>
25. [How do you use Itertools to chain iterables?](#q25-how-do-you-use-itertools-to-chain-iterables) <span class="intermediate">Intermediate</span>
26. [How do you use defaultdict for cleaner grouping code?](#q26-how-do-you-use-defaultdict-for-cleaner-grouping-code) <span class="beginner">Beginner</span>
27. [How do you use unittest.mock to mock dependencies?](#q27-how-do-you-use-unittestmock-to-mock-dependencies) <span class="intermediate">Intermediate</span>
28. [How do you use functools.partial?](#q28-how-do-you-use-functoolspartial) <span class="intermediate">Intermediate</span>
29. [How do you use threading.Event for thread synchronization?](#q29-how-do-you-use-threadingevent-for-thread-synchronization) <span class="intermediate">Intermediate</span>
30. [How do you run shell commands with subprocess.run?](#q30-how-do-you-run-shell-commands-with-subprocessrun) <span class="intermediate">Intermediate</span>
31. [How do you use json.dumps with a custom encoder?](#q31-how-do-you-use-jsondumps-with-a-custom-encoder) <span class="intermediate">Intermediate</span>
32. [How do you use collections.Counter?](#q32-how-do-you-use-collectionscounter) <span class="beginner">Beginner</span>
33. [How do you use heapq for a priority queue?](#q33-how-do-you-use-heapq-for-a-priority-queue) <span class="intermediate">Intermediate</span>
34. [How do you use zip to iterate over multiple lists?](#q34-how-do-you-use-zip-to-iterate-over-multiple-lists) <span class="beginner">Beginner</span>
35. [How do you use enumerate?](#q35-how-do-you-use-enumerate) <span class="beginner">Beginner</span>
36. [How do you use if __name__ == "__main__":?](#q36-how-do-you-use-if-__name__--__main__) <span class="beginner">Beginner</span>
37. [How do you use re module for regex matching?](#q37-how-do-you-use-re-module-for-regex-matching) <span class="intermediate">Intermediate</span>
38. [How do you use with statement (Context Managers)?](#q38-how-do-you-use-with-statement-context-managers) <span class="beginner">Beginner</span>
39. [How do you use Generators (yield)?](#q39-how-do-you-use-generators-yield) <span class="intermediate">Intermediate</span>
40. [How do you use Decorators?](#q40-how-do-you-use-decorators) <span class="intermediate">Intermediate</span>
41. [How do you implement asynchronous tasks with Celery?](#q41-how-do-you-implement-asynchronous-tasks-with-celery) <span class="advanced">Advanced</span>
42. [How do you define a One-to-Many relationship in SQLAlchemy?](#q42-how-do-you-define-a-one-to-many-relationship-in-sqlalchemy) <span class="intermediate">Intermediate</span>
43. [How do you structure a large Flask application using Blueprints?](#q43-how-do-you-structure-a-large-flask-application-using-blueprints) <span class="intermediate">Intermediate</span>
44. [How do you use Django Signals to decouple logic?](#q44-how-do-you-use-django-signals-to-decouple-logic) <span class="intermediate">Intermediate</span>
45. [How do you use Pytest Fixtures with scopes?](#q45-how-do-you-use-pytest-fixtures-with-scopes) <span class="intermediate">Intermediate</span>
46. [How do you implement Generics using TypeVar?](#q46-how-do-you-implement-generics-using-typevar) <span class="advanced">Advanced</span>
47. [How do you use Protocols for structural subtyping (Duck Typing)?](#q47-how-do-you-use-protocols-for-structural-subtyping-duck-typing) <span class="advanced">Advanced</span>
48. [How do you use Single Dispatch for function overloading?](#q48-how-do-you-use-single-dispatch-for-function-overloading) <span class="intermediate">Intermediate</span>
49. [How do you use WeakRef to manage memory?](#q49-how-do-you-use-weakref-to-manage-memory) <span class="advanced">Advanced</span>
50. [How do you validate data using Pydantic?](#q50-how-do-you-validate-data-using-pydantic) <span class="intermediate">Intermediate</span>
51. [How do you implement Dependency Injection in FastAPI?](#q51-how-do-you-implement-dependency-injection-in-fastapi) <span class="intermediate">Intermediate</span>
52. [How do you make concurrent HTTP requests with Aiohttp?](#q52-how-do-you-make-concurrent-http-requests-with-aiohttp) <span class="intermediate">Intermediate</span>
53. [How do you group and aggregate data in Pandas?](#q53-how-do-you-group-and-aggregate-data-in-pandas) <span class="beginner">Beginner</span>
54. [How do you create a Machine Learning Pipeline with Scikit-learn?](#q54-how-do-you-create-a-machine-learning-pipeline-with-scikit-learn) <span class="intermediate">Intermediate</span>
55. [How do you scrape a website using Beautiful Soup?](#q55-how-do-you-scrape-a-website-using-beautiful-soup) <span class="intermediate">Intermediate</span>
56. [How do you create a command-line interface (CLI) with Click?](#q56-how-do-you-create-a-command-line-interface-cli-with-click) <span class="intermediate">Intermediate</span>
57. [How do you use Loguru for better logging?](#q57-how-do-you-use-loguru-for-better-logging) <span class="beginner">Beginner</span>
58. [How do you use Python's bisect module for binary search?](#q58-how-do-you-use-pythons-bisect-module-for-binary-search) <span class="intermediate">Intermediate</span>
59. [How do you profile a Python script to find bottlenecks?](#q59-how-do-you-profile-a-python-script-to-find-bottlenecks) <span class="advanced">Advanced</span>
60. [How do you implement a Context Manager as a Class?](#q60-how-do-you-implement-a-context-manager-as-a-class) <span class="intermediate">Intermediate</span>

---

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

### Q24: How do you use __slots__ to optimize memory?

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

### Q36: How do you use if __name__ == "__main__":?

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



---

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

### Q51: How do you implement Dependency Injection in FastAPI?

**Difficulty**: Intermediate

**Strategy:**
Use `Depends`. It declares a dependency that FastAPI resolves and injects into your path operation. It supports nested dependencies and caching.

**Code Example:**
```python
def get_db():
    db = Session()
    try: yield db
    finally: db.close()

@app.get("/users")
def read_users(db: Session = Depends(get_db)):
    return db.query(User).all()
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q52: How do you make concurrent HTTP requests with Aiohttp?

**Difficulty**: Intermediate

**Strategy:**
Use `aiohttp.ClientSession` within an `async` function. Combine with `asyncio.gather` to fire multiple requests simultaneously.

**Code Example:**
```python
async with aiohttp.ClientSession() as session:
    tasks = [session.get(url) for url in urls]
    responses = await asyncio.gather(*tasks)
    for resp in responses:
        print(resp.status)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q53: How do you group and aggregate data in Pandas?

**Difficulty**: Beginner

**Strategy:**
Use `.groupby()` followed by an aggregation function like `.sum()`, `.mean()`, or `.agg()` for multiple metrics.

**Code Example:**
```python
df.groupby('Category').agg({
    'Sales': 'sum',
    'Profit': 'mean'
})
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q54: How do you create a Machine Learning Pipeline with Scikit-learn?

**Difficulty**: Intermediate

**Strategy:**
Use `Pipeline` to chain preprocessing steps (scalers, encoders) and the model. This ensures the same transformations are applied to train and test data.

**Code Example:**
```python
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('svc', SVC())
])
pipe.fit(X_train, y_train)
pipe.score(X_test, y_test)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q55: How do you scrape a website using Beautiful Soup?

**Difficulty**: Intermediate

**Strategy:**
Fetch the page with `requests`, then parse the HTML with `BeautifulSoup`. Use `.find()` or `.select()` to extract elements.

**Code Example:**
```python
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.find('h1').text
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q56: How do you create a command-line interface (CLI) with Click?

**Difficulty**: Intermediate

**Strategy:**
Decorate functions with `@click.command()` and `@click.option()`. Click handles argument parsing and help generation automatically.

**Code Example:**
```python
@click.command()
@click.option('--count', default=1, help='Number of greetings.')
def hello(count):
    for _ in range(count):
        click.echo('Hello!')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q57: How do you use Loguru for better logging?

**Difficulty**: Beginner

**Strategy:**
`Loguru` simplifies logging. No configuration boilerplate is needed. It supports rotation, compression, and colorized output out of the box.

**Code Example:**
```python
from loguru import logger

logger.add("file.log", rotation="500 MB")
logger.info("Information message")
logger.error("Something went wrong")
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q58: How do you use Python's bisect module for binary search?

**Difficulty**: Intermediate

**Strategy:**
`bisect` provides support for maintaining a list in sorted order without having to sort the list after each insertion.

**Code Example:**
```python
import bisect

scores = [10, 20, 30, 40]
bisect.insort(scores, 25)
# scores is now [10, 20, 25, 30, 40]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q59: How do you profile a Python script to find bottlenecks?

**Difficulty**: Advanced

**Strategy:**
Use `cProfile`. It provides deterministic profiling of Python programs, showing how much time is spent in each function.

**Code Example:**
```python
python -m cProfile -o output.pstats myscript.py
# Visualize with snakeviz
# snakeviz output.pstats
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q60: How do you implement a Context Manager as a Class?

**Difficulty**: Intermediate

**Strategy:**
Define `__enter__` and `__exit__` methods. `__enter__` returns the resource, and `__exit__` handles cleanup and exceptions.

**Code Example:**
```python
class FileManager:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.f = open(self.name, 'w')
        return self.f

    def __exit__(self, type, value, traceback):
        self.f.close()
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>
