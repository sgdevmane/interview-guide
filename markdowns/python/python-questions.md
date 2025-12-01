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
6. [How do you merge two dictionaries in Python 3.9+?](#q6-how-do-you-merge-two-dictionaries-in-python-3.9+) <span class="beginner">Beginner</span>
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
27. [How do you use unittest.mock to mock dependencies?](#q27-how-do-you-use-unittest.mock-to-mock-dependencies) <span class="intermediate">Intermediate</span>
28. [How do you use functools.partial?](#q28-how-do-you-use-functools.partial) <span class="intermediate">Intermediate</span>
29. [How do you use threading.Event for thread synchronization?](#q29-how-do-you-use-threading.event-for-thread-synchronization) <span class="intermediate">Intermediate</span>
30. [How do you run shell commands with subprocess.run?](#q30-how-do-you-run-shell-commands-with-subprocess.run) <span class="intermediate">Intermediate</span>
31. [How do you use json.dumps with a custom encoder?](#q31-how-do-you-use-json.dumps-with-a-custom-encoder) <span class="intermediate">Intermediate</span>
32. [How do you use collections.Counter?](#q32-how-do-you-use-collections.counter) <span class="beginner">Beginner</span>
33. [How do you use heapq for a priority queue?](#q33-how-do-you-use-heapq-for-a-priority-queue) <span class="intermediate">Intermediate</span>
34. [How do you use zip to iterate over multiple lists?](#q34-how-do-you-use-zip-to-iterate-over-multiple-lists) <span class="beginner">Beginner</span>
35. [How do you use enumerate?](#q35-how-do-you-use-enumerate) <span class="beginner">Beginner</span>
36. [How do you use if __name__ == "__main__":?](#q36-how-do-you-use-if-__name__-==-"__main__":) <span class="beginner">Beginner</span>
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
51. [How does the GIL (Global Interpreter Lock) affect concurrency?](#q51-how-does-the-gil-global-interpreter-lock-affect-concurrency) <span class="advanced">Advanced</span>
52. [What are Python Decorators?](#q52-what-are-python-decorators) <span class="intermediate">Intermediate</span>
53. [Difference between `__new__` and `__init__`?](#q53-difference-between-__new__-and-__init__) <span class="advanced">Advanced</span>
54. [How do Generators work?](#q54-how-do-generators-work) <span class="intermediate">Intermediate</span>
55. [What are Context Managers?](#q55-what-are-context-managers) <span class="intermediate">Intermediate</span>
56. [Difference between `deepcopy` and `shallow copy`?](#q56-difference-between-deepcopy-and-shallow-copy) <span class="beginner">Beginner</span>
57. [How does Python memory management work?](#q57-how-does-python-memory-management-work) <span class="advanced">Advanced</span>
58. [What are Metaclasses?](#q58-what-are-metaclasses) <span class="advanced">Advanced</span>
59. [How do you use `asyncio`?](#q59-how-do-you-use-asyncio) <span class="intermediate">Intermediate</span>
60. [What is `*args` and `**kwargs`?](#q60-what-is-*args-and-**kwargs) <span class="beginner">Beginner</span>
61. [How do you implement a Singleton in Python?](#q61-how-do-you-implement-a-singleton-in-python) <span class="intermediate">Intermediate</span>
62. [What are Python descriptors?](#q62-what-are-python-descriptors) <span class="advanced">Advanced</span>
63. [Difference between `is` and `==`?](#q63-difference-between-is-and-==) <span class="beginner">Beginner</span>
64. [How do you manage dependencies?](#q64-how-do-you-manage-dependencies) <span class="beginner">Beginner</span>
65. [What is the `with` statement for?](#q65-what-is-the-with-statement-for) <span class="intermediate">Intermediate</span>
66. [How do you profile Python code?](#q66-how-do-you-profile-python-code) <span class="intermediate">Intermediate</span>
67. [What are list comprehensions?](#q67-what-are-list-comprehensions) <span class="beginner">Beginner</span>
68. [How do you create a virtual environment?](#q68-how-do-you-create-a-virtual-environment) <span class="beginner">Beginner</span>
69. [What is `__name__ == '__main__'`?](#q69-what-is-__name__-==-__main__) <span class="beginner">Beginner</span>
70. [How do you handle exceptions?](#q70-how-do-you-handle-exceptions) <span class="beginner">Beginner</span>
71. [What is Method Resolution Order (MRO)?](#q71-what-is-method-resolution-order-mro) <span class="advanced">Advanced</span>
72. [How do you implement unit tests?](#q72-how-do-you-implement-unit-tests) <span class="intermediate">Intermediate</span>
73. [What are Type Hints?](#q73-what-are-type-hints) <span class="intermediate">Intermediate</span>
74. [How do you use `slots`?](#q74-how-do-you-use-slots) <span class="advanced">Advanced</span>
75. [What is the difference between `staticmethod` and `classmethod`?](#q75-what-is-the-difference-between-staticmethod-and-classmethod) <span class="intermediate">Intermediate</span>
76. [How do you parse JSON?](#q76-how-do-you-parse-json) <span class="beginner">Beginner</span>
77. [How do you make HTTP requests?](#q77-how-do-you-make-http-requests) <span class="beginner">Beginner</span>
78. [What is a lambda function?](#q78-what-is-a-lambda-function) <span class="beginner">Beginner</span>
79. [How do you copy a file?](#q79-how-do-you-copy-a-file) <span class="beginner">Beginner</span>
80. [How do you handle command line arguments?](#q80-how-do-you-handle-command-line-arguments) <span class="beginner">Beginner</span>
81. [What is the `logging` module?](#q81-what-is-the-logging-module) <span class="intermediate">Intermediate</span>
82. [How do you connect to a database?](#q82-how-do-you-connect-to-a-database) <span class="intermediate">Intermediate</span>
83. [What is `functools`?](#q83-what-is-functools) <span class="intermediate">Intermediate</span>
84. [How do you implement multithreading?](#q84-how-do-you-implement-multithreading) <span class="intermediate">Intermediate</span>
85. [How do you implement multiprocessing?](#q85-how-do-you-implement-multiprocessing) <span class="intermediate">Intermediate</span>
86. [What is a deque?](#q86-what-is-a-deque) <span class="intermediate">Intermediate</span>
87. [How do you sort a dictionary by value?](#q87-how-do-you-sort-a-dictionary-by-value) <span class="intermediate">Intermediate</span>
88. [What is `zip`?](#q88-what-is-zip) <span class="beginner">Beginner</span>
89. [How do you read a CSV file?](#q89-how-do-you-read-a-csv-file) <span class="beginner">Beginner</span>
90. [What is `pickling`?](#q90-what-is-pickling) <span class="intermediate">Intermediate</span>
91. [How do you document code?](#q91-how-do-you-document-code) <span class="beginner">Beginner</span>
92. [What is `pdb`?](#q92-what-is-pdb) <span class="intermediate">Intermediate</span>
93. [How do you use `enumerate`?](#q93-how-do-you-use-enumerate) <span class="beginner">Beginner</span>
94. [What is the `collections` module?](#q94-what-is-the-collections-module) <span class="intermediate">Intermediate</span>
95. [How do you implement a property?](#q95-how-do-you-implement-a-property) <span class="intermediate">Intermediate</span>
96. [What is `itertools`?](#q96-what-is-itertools) <span class="intermediate">Intermediate</span>
97. [How do you execute shell commands?](#q97-how-do-you-execute-shell-commands) <span class="intermediate">Intermediate</span>
98. [What is `virtualenv`?](#q98-what-is-virtualenv) <span class="beginner">Beginner</span>
99. [How do you install packages?](#q99-how-do-you-install-packages) <span class="beginner">Beginner</span>
100. [What is `pylint`?](#q100-what-is-pylint) <span class="beginner">Beginner</span>

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


### Q51: How does the GIL (Global Interpreter Lock) affect concurrency?

**Difficulty**: Advanced

**Strategy**:
Prevents multiple native threads from executing Python bytecodes at once. Limits CPU-bound tasks to single core.

**Code Example**:
```javascript
// Use multiprocessing for CPU-bound tasks to bypass GIL
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q52: What are Python Decorators?

**Difficulty**: Intermediate

**Strategy**:
Functions that modify other functions. Syntactic sugar for `func = decorator(func)`.

**Code Example**:
```javascript
def log(func):
    def wrapper():
        print('Call')
        func()
    return wrapper
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q53: Difference between `__new__` and `__init__`?

**Difficulty**: Advanced

**Strategy**:
`__new__` creates the instance (static method). `__init__` initializes it. `__new__` is used for immutable types.

**Code Example**:
```javascript
def __new__(cls): return super().__new__(cls)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q54: How do Generators work?

**Difficulty**: Intermediate

**Strategy**:
Functions that `yield` values one by one. They maintain state and are memory efficient.

**Code Example**:
```javascript
def gen():
    yield 1
    yield 2
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q55: What are Context Managers?

**Difficulty**: Intermediate

**Strategy**:
Objects that define runtime context (setup/teardown). Used with `with` statement.

**Code Example**:
```javascript
with open('file.txt') as f:
    data = f.read()
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q56: Difference between `deepcopy` and `shallow copy`?

**Difficulty**: Beginner

**Strategy**:
Shallow copy stores references to objects. Deep copy recursively copies objects.

**Code Example**:
```javascript
import copy
new_list = copy.deepcopy(old_list)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q57: How does Python memory management work?

**Difficulty**: Advanced

**Strategy**:
Reference counting + Cyclic Garbage Collector. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
// sys.getrefcount(obj)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q58: What are Metaclasses?

**Difficulty**: Advanced

**Strategy**:
Classes of classes. They define how a class behaves. `type` is the default metaclass.

**Code Example**:
```javascript
class MyMeta(type): pass
class MyClass(metaclass=MyMeta): pass
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q59: How do you use `asyncio`?

**Difficulty**: Intermediate

**Strategy**:
Library for writing concurrent code using async/await syntax.

**Code Example**:
```javascript
async def main():
    await asyncio.sleep(1)
asyncio.run(main())
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q60: What is `*args` and `**kwargs`?

**Difficulty**: Beginner

**Strategy**:
Variable length arguments. `*args` is tuple, `**kwargs` is dictionary.

**Code Example**:
```javascript
def func(*args, **kwargs): print(args, kwargs)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q61: How do you implement a Singleton in Python?

**Difficulty**: Intermediate

**Strategy**:
Override `__new__` or use a decorator. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
class Singleton:
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q62: What are Python descriptors?

**Difficulty**: Advanced

**Strategy**:
Objects that define `__get__`, `__set__`, or `__delete__`. Basis for properties.

**Code Example**:
```javascript
class Descriptor:
    def __get__(self, obj, objtype): return 10
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q63: Difference between `is` and `==`?

**Difficulty**: Beginner

**Strategy**:
`is` checks identity (memory address). `==` checks equality (value).

**Code Example**:
```javascript
a = [1]; b = [1]
a == b # True
a is b # False
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q64: How do you manage dependencies?

**Difficulty**: Beginner

**Strategy**:
Use `pip`, `requirements.txt`, or `poetry`/`pipenv`.

**Code Example**:
```javascript
pip install -r requirements.txt
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q65: What is the `with` statement for?

**Difficulty**: Intermediate

**Strategy**:
Ensures cleanup (like closing files) even if errors occur.

**Code Example**:
```javascript
with open('file') as f: pass
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q66: How do you profile Python code?

**Difficulty**: Intermediate

**Strategy**:
Use `cProfile` module. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
python -m cProfile script.py
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q67: What are list comprehensions?

**Difficulty**: Beginner

**Strategy**:
Concise way to create lists. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
[x**2 for x in range(10)]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q68: How do you create a virtual environment?

**Difficulty**: Beginner

**Strategy**:
Use `venv` module. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
python -m venv venv
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q69: What is `__name__ == '__main__'`?

**Difficulty**: Beginner

**Strategy**:
Checks if script is run directly or imported. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
if __name__ == '__main__': main()
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q70: How do you handle exceptions?

**Difficulty**: Beginner

**Strategy**:
Use `try-except-else-finally`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
try: 1/0
except ZeroDivisionError: pass
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q71: What is Method Resolution Order (MRO)?

**Difficulty**: Advanced

**Strategy**:
Order in which base classes are searched. Python uses C3 Linearization.

**Code Example**:
```javascript
ClassName.mro()
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q72: How do you implement unit tests?

**Difficulty**: Intermediate

**Strategy**:
Use `unittest` or `pytest`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
def test_sum(): assert sum([1, 2]) == 3
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q73: What are Type Hints?

**Difficulty**: Intermediate

**Strategy**:
Annotations for static type checking (mypy). This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
def greeting(name: str) -> str: ...
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q74: How do you use `slots`?

**Difficulty**: Advanced

**Strategy**:
Restricts attribute creation to save memory. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
class Point: __slots__ = ['x', 'y']
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q75: What is the difference between `staticmethod` and `classmethod`?

**Difficulty**: Intermediate

**Strategy**:
`classmethod` takes `cls` as first arg. `staticmethod` takes nothing special.

**Code Example**:
```javascript
@classmethod
def create(cls): return cls()
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q76: How do you parse JSON?

**Difficulty**: Beginner

**Strategy**:
Use `json` module. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
import json; d = json.loads(s)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q77: How do you make HTTP requests?

**Difficulty**: Beginner

**Strategy**:
Use `requests` library. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
requests.get('https://api.com')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q78: What is a lambda function?

**Difficulty**: Beginner

**Strategy**:
Anonymous inline function. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
add = lambda x, y: x + y
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q79: How do you copy a file?

**Difficulty**: Beginner

**Strategy**:
Use `shutil` module. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
shutil.copy('src', 'dst')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q80: How do you handle command line arguments?

**Difficulty**: Beginner

**Strategy**:
Use `argparse`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
parser = argparse.ArgumentParser()
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q81: What is the `logging` module?

**Difficulty**: Intermediate

**Strategy**:
Standard way to log events. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
logging.warning('Watch out!')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q82: How do you connect to a database?

**Difficulty**: Intermediate

**Strategy**:
Use `sqlite3` or SQLAlchemy. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
engine = create_engine('sqlite:///:memory:')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q83: What is `functools`?

**Difficulty**: Intermediate

**Strategy**:
Higher-order functions like `partial`, `reduce`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
partial(func, arg1)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q84: How do you implement multithreading?

**Difficulty**: Intermediate

**Strategy**:
Use `threading` module. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
t = threading.Thread(target=func); t.start()
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q85: How do you implement multiprocessing?

**Difficulty**: Intermediate

**Strategy**:
Use `multiprocessing` module. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
p = multiprocessing.Process(target=func); p.start()
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q86: What is a deque?

**Difficulty**: Intermediate

**Strategy**:
Double-ended queue from `collections`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
d = deque([1, 2]); d.appendleft(0)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q87: How do you sort a dictionary by value?

**Difficulty**: Intermediate

**Strategy**:
Use `sorted` with key. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
sorted(d.items(), key=lambda x: x[1])
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q88: What is `zip`?

**Difficulty**: Beginner

**Strategy**:
Aggregates elements from iterables. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
zip([1,2], ['a','b'])
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q89: How do you read a CSV file?

**Difficulty**: Beginner

**Strategy**:
Use `csv` module or pandas. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
csv.reader(file)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q90: What is `pickling`?

**Difficulty**: Intermediate

**Strategy**:
Serializing objects. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
pickle.dumps(obj)
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q91: How do you document code?

**Difficulty**: Beginner

**Strategy**:
Use Docstrings. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
def func(): """Docstring"""
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q92: What is `pdb`?

**Difficulty**: Intermediate

**Strategy**:
Python Debugger. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
import pdb; pdb.set_trace()
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q93: How do you use `enumerate`?

**Difficulty**: Beginner

**Strategy**:
Get index and value. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
for i, v in enumerate(list): ...
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q94: What is the `collections` module?

**Difficulty**: Intermediate

**Strategy**:
Specialized container datatypes (Counter, defaultdict).

**Code Example**:
```javascript
c = Counter('abracadabra')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q95: How do you implement a property?

**Difficulty**: Intermediate

**Strategy**:
Use `@property` decorator. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
@property
def x(self): return self._x
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q96: What is `itertools`?

**Difficulty**: Intermediate

**Strategy**:
Iterator building blocks. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
itertools.cycle('ABCD')
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q97: How do you execute shell commands?

**Difficulty**: Intermediate

**Strategy**:
Use `subprocess`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
subprocess.run(['ls', '-l'])
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q98: What is `virtualenv`?

**Difficulty**: Beginner

**Strategy**:
Tool to create isolated environments. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
virtualenv myenv
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q99: How do you install packages?

**Difficulty**: Beginner

**Strategy**:
Use `pip`. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
pip install package_name
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q100: What is `pylint`?

**Difficulty**: Beginner

**Strategy**:
Static code analyzer. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```javascript
pylint script.py
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---
