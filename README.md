<div align="center">

# 🐍 Python

**A complete, practical roadmap to learn Python, from your first `print()` to production-grade code.**

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Level](https://img.shields.io/badge/level-beginner%20→%20pro-orange.svg)](#-learning-path)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

</div>

---

## 📚 Table of Contents

1. [Learning Path](#-learning-path)
2. [Setup](#-1-setup)
3. [Basics](#-2-basics)
4. [Data Structures](#-3-data-structures)
5. [Functions](#-4-functions)
6. [Object-Oriented Programming](#-5-object-oriented-programming)
7. [Files and Error Handling](#-6-files-and-error-handling)
8. [Modules and Packages](#-7-modules-and-packages)
9. [Intermediate Concepts](#-8-intermediate-concepts)
10. [Advanced Python](#-9-advanced-python)
11. [Professional Practices](#-10-professional-practices)
12. [Popular Libraries](#-11-popular-libraries)
13. [Project Ideas](#-12-project-ideas)
14. [Resources](#-resources)

---

## 🗺️ Learning Path

| Level | Topics | Time (approx.) |
|-------|--------|----------------|
| 🟢 **Beginner** | Syntax, variables, control flow, data structures, functions | 3–4 weeks |
| 🟡 **Intermediate** | OOP, files, errors, modules, comprehensions, decorators | 4–6 weeks |
| 🟠 **Advanced** | Generators, async, metaclasses, type hints, concurrency | 6–8 weeks |
| 🔴 **Pro** | Testing, packaging, performance, design patterns, CI/CD | Ongoing |

> 💡 **Tip:** Code every day. Reading alone will not make you good; building projects will.

---

## 🛠️ 1. Setup

### Install Python

Download from [python.org](https://www.python.org/downloads/), then verify:

```bash
python --version
```

### Virtual environments

Always isolate project dependencies:

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install requests
pip freeze > requirements.txt
```

### Run a script

```bash
python hello.py
```

---

## 🟢 2. Basics

### Hello, World

```python
print("Hello, World!")
```

### Variables and types

```python
name = "Asha"          # str
age = 25               # int
height = 5.7           # float
is_student = True      # bool
nothing = None         # NoneType

print(type(age))       # <class 'int'>
```

### Operators

```python
10 + 3     # 13   addition
10 - 3     # 7    subtraction
10 * 3     # 30   multiplication
10 / 3     # 3.33 true division
10 // 3    # 3    floor division
10 % 3     # 1    remainder
10 ** 3    # 1000 power
```

### Strings

```python
text = "Python Programming"

text.upper()              # 'PYTHON PROGRAMMING'
text.lower()              # 'python programming'
text.split()              # ['Python', 'Programming']
text[0:6]                 # 'Python'
text[::-1]                # reversed

name, score = "Ravi", 95
print(f"{name} scored {score}%")   # f-strings (preferred)
```

### Input and output

```python
user = input("Your name: ")
print(f"Welcome, {user}!")
```

### Conditions

```python
marks = 82

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
else:
    print("C")
```

### Loops

```python
# for loop
for i in range(5):
    print(i)

# while loop
count = 0
while count < 3:
    print(count)
    count += 1

# control keywords
for n in range(10):
    if n == 3:
        continue     # skip this iteration
    if n == 6:
        break        # stop the loop
    print(n)
```

---

## 📦 3. Data Structures

| Type | Syntax | Ordered | Mutable | Duplicates |
|------|--------|:-------:|:-------:|:----------:|
| **List** | `[1, 2, 3]` | ✅ | ✅ | ✅ |
| **Tuple** | `(1, 2, 3)` | ✅ | ❌ | ✅ |
| **Set** | `{1, 2, 3}` | ❌ | ✅ | ❌ |
| **Dict** | `{"a": 1}` | ✅ | ✅ | keys unique |

### Lists

```python
fruits = ["apple", "banana", "cherry"]

fruits.append("mango")
fruits.insert(1, "kiwi")
fruits.remove("banana")
last = fruits.pop()
fruits.sort()

print(len(fruits), fruits[0], fruits[-1])
```

### Tuples

```python
point = (10, 20)
x, y = point            # unpacking
```

### Sets

```python
a = {1, 2, 3}
b = {3, 4, 5}

a | b      # union        {1, 2, 3, 4, 5}
a & b      # intersection {3}
a - b      # difference   {1, 2}
```

### Dictionaries

```python
student = {"name": "Meera", "age": 21}

student["course"] = "CS"
print(student.get("grade", "N/A"))

for key, value in student.items():
    print(key, value)
```

### Comprehensions

```python
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
lookup = {word: len(word) for word in ["hi", "python"]}
unique = {x % 3 for x in range(10)}
```

---

## 🔧 4. Functions

```python
def greet(name, greeting="Hello"):
    """Return a greeting message."""
    return f"{greeting}, {name}!"

print(greet("Arjun"))
print(greet("Arjun", greeting="Namaste"))
```

### `*args` and `**kwargs`

```python
def total(*numbers, **options):
    result = sum(numbers)
    if options.get("double"):
        result *= 2
    return result

total(1, 2, 3)                 # 6
total(1, 2, 3, double=True)    # 12
```

### Lambda, map, filter

```python
square = lambda x: x * x

nums = [1, 2, 3, 4, 5]
list(map(square, nums))                  # [1, 4, 9, 16, 25]
list(filter(lambda x: x % 2, nums))      # [1, 3, 5]
sorted(["bb", "a", "ccc"], key=len)      # ['a', 'bb', 'ccc']
```

### Scope

```python
x = "global"

def show():
    x = "local"
    print(x)       # local

show()
print(x)           # global
```

---

## 🏛️ 5. Object-Oriented Programming

```python
class Animal:
    species_count = 0                      # class attribute

    def __init__(self, name, sound):
        self.name = name                   # instance attribute
        self.sound = sound
        Animal.species_count += 1

    def speak(self):
        return f"{self.name} says {self.sound}"

    def __str__(self):
        return f"Animal({self.name})"


class Dog(Animal):                         # inheritance
    def __init__(self, name):
        super().__init__(name, "Woof")

    def fetch(self):
        return f"{self.name} fetches the ball!"


dog = Dog("Bruno")
print(dog.speak())     # Bruno says Woof
print(dog.fetch())
```

### The four pillars

| Pillar | Meaning |
|--------|---------|
| **Encapsulation** | Bundle data and methods; hide internals (`_private`) |
| **Inheritance** | Child classes reuse parent behaviour |
| **Polymorphism** | Same method name, different behaviour |
| **Abstraction** | Expose only what is necessary |

### Special (dunder) methods

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

print(Vector(1, 2) + Vector(3, 4))   # Vector(4, 6)
```

### Properties and dataclasses

```python
from dataclasses import dataclass

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return 3.14159 * self._radius ** 2

@dataclass
class Point:
    x: float
    y: float = 0.0
```

---

## 📁 6. Files and Error Handling

### Working with files

```python
# Write
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("Hello file!\n")

# Read
with open("notes.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

### `pathlib` (modern approach)

```python
from pathlib import Path

path = Path("data") / "notes.txt"
path.parent.mkdir(exist_ok=True)
path.write_text("Hello")
print(path.read_text())
```

### JSON and CSV

```python
import json, csv

with open("data.json", "w") as f:
    json.dump({"name": "Asha"}, f, indent=2)

with open("people.csv", newline="") as f:
    for row in csv.DictReader(f):
        print(row)
```

### Exceptions

```python
try:
    number = int(input("Enter a number: "))
    print(10 / number)
except ValueError:
    print("That is not a number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Success!")
finally:
    print("Always runs.")

# Custom exception
class InvalidAgeError(Exception):
    pass

def set_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative")
```

---

## 🧩 7. Modules and Packages

```python
import math
from datetime import datetime
from collections import Counter, defaultdict, deque
import random, os, sys

print(math.sqrt(16))
print(datetime.now().strftime("%Y-%m-%d"))
print(Counter("mississippi").most_common(2))
```

### Your own module

```
myproject/
├── main.py
└── utils/
    ├── __init__.py
    └── helpers.py
```

```python
# main.py
from utils.helpers import add

if __name__ == "__main__":
    print(add(2, 3))
```

---

## 🟡 8. Intermediate Concepts

### Decorators

```python
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.perf_counter() - start:.4f}s")
        return result
    return wrapper

@timer
def slow():
    time.sleep(0.5)
```

### Generators

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(3):
    print(i)

squares = (x * x for x in range(1_000_000))   # lazy, memory-friendly
```

### Context managers

```python
from contextlib import contextmanager

@contextmanager
def opened(path):
    f = open(path)
    try:
        yield f
    finally:
        f.close()
```

### Useful built-ins

```python
enumerate(["a", "b"])              # (0, 'a'), (1, 'b')
zip([1, 2], ["x", "y"])            # (1, 'x'), (2, 'y')
any([False, True])                 # True
all([True, True])                  # True
```

### Regular expressions

```python
import re

re.findall(r"\d+", "Order 66 and 99")        # ['66', '99']
re.sub(r"\s+", " ", "too    many   spaces")
```

---

## 🟠 9. Advanced Python

### Type hints

```python
from typing import Optional

def find_user(user_id: int) -> Optional[dict[str, str]]:
    ...

def average(values: list[float]) -> float:
    return sum(values) / len(values)
```

Check with `mypy` or `pyright`.

### Iterators

```python
class Counter:
    def __init__(self, limit):
        self.n, self.limit = 0, limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.n >= self.limit:
            raise StopIteration
        self.n += 1
        return self.n
```

### Concurrency: pick the right tool

| Task type | Best tool |
|-----------|-----------|
| I/O-bound (network, files) | `asyncio` or `threading` |
| CPU-bound (heavy math) | `multiprocessing` |
| Simple parallel jobs | `concurrent.futures` |

### Async / await

```python
import asyncio

async def fetch(n):
    await asyncio.sleep(1)
    return f"Task {n} done"

async def main():
    results = await asyncio.gather(fetch(1), fetch(2), fetch(3))
    print(results)          # finishes in ~1 second, not 3

asyncio.run(main())
```

### Multiprocessing

```python
from concurrent.futures import ProcessPoolExecutor

def heavy(n):
    return sum(i * i for i in range(n))

with ProcessPoolExecutor() as pool:
    print(list(pool.map(heavy, [10**6, 10**6, 10**6])))
```

### Pattern matching (3.10+)

```python
def handle(command):
    match command.split():
        case ["go", direction]:
            return f"Going {direction}"
        case ["quit"]:
            return "Bye"
        case _:
            return "Unknown command"
```

### Descriptors and metaclasses (deep end)

```python
class Meta(type):
    def __new__(mcs, name, bases, attrs):
        attrs["created_by"] = "Meta"
        return super().__new__(mcs, name, bases, attrs)

class Thing(metaclass=Meta):
    pass

print(Thing.created_by)     # Meta
```

> ⚠️ Metaclasses are rarely needed. Reach for them last.

### Memory and performance

- Profile first: `cProfile`, `timeit`, `line_profiler`
- Use `__slots__` for many small objects
- Prefer generators over big lists
- Cache pure functions with `functools.lru_cache`
- Use built-ins and `numpy` instead of manual loops where possible

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)
```

---

## 🔴 10. Professional Practices

### Code style

- Follow [PEP 8](https://peps.python.org/pep-0008/)
- Format with **Black**, lint with **Ruff**
- Write docstrings and meaningful names

```bash
pip install black ruff mypy pytest
black .
ruff check .
mypy .
```

### Testing with pytest

```python
# test_math.py
import pytest
from mymodule import divide

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

@pytest.mark.parametrize("a,b,expected", [(4, 2, 2), (9, 3, 3)])
def test_many(a, b, expected):
    assert divide(a, b) == expected
```

```bash
pytest --cov
```

### Logging (not `print`)

```python
import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)
log.info("Application started")
```

### Recommended project layout

```
my-project/
├── src/
│   └── my_project/
│       ├── __init__.py
│       └── core.py
├── tests/
│   └── test_core.py
├── pyproject.toml
├── README.md
├── LICENSE
└── .gitignore
```

### Packaging with `pyproject.toml`

```toml
[project]
name = "my-project"
version = "0.1.0"
requires-python = ">=3.10"
dependencies = ["requests>=2.31"]

[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"
```

### Design principles

- **SOLID**, **DRY**, **KISS**
- Learn common patterns: Singleton, Factory, Observer, Strategy
- Prefer composition over inheritance
- Keep functions small and focused

### Tooling checklist

- [ ] Git and GitHub
- [ ] Virtual environments (`venv`, `uv`, or `poetry`)
- [ ] Pre-commit hooks
- [ ] CI with GitHub Actions
- [ ] Docker for deployment
- [ ] Environment variables for secrets (never commit them)

---

## 🌐 11. Popular Libraries

| Domain | Libraries |
|--------|-----------|
| **Data analysis** | `numpy`, `pandas`, `polars` |
| **Visualization** | `matplotlib`, `seaborn`, `plotly` |
| **Machine learning** | `scikit-learn`, `pytorch`, `tensorflow` |
| **Web backend** | `fastapi`, `django`, `flask` |
| **Web scraping** | `requests`, `beautifulsoup4`, `scrapy`, `playwright` |
| **Databases** | `sqlalchemy`, `psycopg`, `redis` |
| **Automation** | `selenium`, `pyautogui`, `schedule` |
| **CLI tools** | `argparse`, `click`, `typer` |
| **GUI** | `tkinter`, `PyQt`, `customtkinter` |
| **Testing** | `pytest`, `hypothesis`, `unittest.mock` |

### Mini example: FastAPI

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello, {name}!"}
```

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```

---

## 🚀 12. Project Ideas

| Level | Project |
|-------|---------|
| 🟢 Beginner | Number guessing game, calculator, to-do list (CLI), password generator |
| 🟡 Intermediate | Expense tracker with CSV/JSON, weather app using an API, web scraper, file organizer |
| 🟠 Advanced | REST API with FastAPI and a database, chat app with websockets, data dashboard |
| 🔴 Pro | Full-stack app with CI/CD and Docker, ML model served via API, open-source package on PyPI |

---

## 📖 Resources

**Official**
- [Python Documentation](https://docs.python.org/3/)
- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [PEP Index](https://peps.python.org/)

**Free learning**
- [Automate the Boring Stuff](https://automatetheboringstuff.com/)
- [Real Python](https://realpython.com/)
- [freeCodeCamp Python](https://www.freecodecamp.org/)

**Books**
- *Python Crash Course*, Eric Matthes
- *Fluent Python*, Luciano Ramalho
- *Effective Python*, Brett Slatkin

**Practice**
- [LeetCode](https://leetcode.com/), [HackerRank](https://www.hackerrank.com/), [Exercism](https://exercism.org/tracks/python)

---

## 🤝 Contributing

Found a mistake or want to add something?

1. Fork this repository
2. Create a branch: `git checkout -b improve-docs`
3. Commit your changes: `git commit -m "Improve explanation"`
4. Push and open a Pull Request

---

## 📄 License

Released under the [MIT License](LICENSE).

---

<div align="center">

**Happy coding! 🐍**

If this guide helped you, give it a ⭐

</div>
