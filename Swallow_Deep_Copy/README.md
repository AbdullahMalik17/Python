## Shallow vs Deep Copy in Python

This guide explains what “copying” means in Python, how it differs from simple assignment, and when to use a shallow copy versus a deep copy. It includes practical examples, common pitfalls, and best practices.

### Key ideas in 10 seconds
- **Assignment (`=`)**: No new object is created; two names point to the same object.
- **Shallow copy**: Creates a new outer container, but references the same inner objects.
- **Deep copy**: Recursively copies the entire structure, producing independent inner objects.
- **Rule of thumb**: If your data is nested (lists of lists, dicts of dicts, objects holding containers), prefer `deepcopy` unless you specifically want sharing.

---

1. ## Assignment vs Copy

```python
a = [1, 2, 3]
b = a           # assignment: b references the SAME list as a
b.append(4)
print(a)  # [1, 2, 3, 4]
print(b)  # [1, 2, 3, 4]
```

Assignment does not duplicate data. Both names point to the same object in memory.

---

## 2) Shallow Copy

A shallow copy creates a new outer container but reuses references to the original inner objects.

Common ways to make a shallow copy:
- **Lists**: `new_list = old_list[:]` or `list(old_list)` or `copy.copy(old_list)`
- **Dicts**: `new_dict = old_dict.copy()` or `dict(old_dict)` or `copy.copy(old_dict)`
- **Sets**: `new_set = old_set.copy()` or `set(old_set)` or `copy.copy(old_set)`

```python
import copy

matrix = [[1, 2], [3, 4]]
shallow = copy.copy(matrix)  # or matrix[:] or list(matrix)

shallow[0].append(99)
print(matrix)  # [[1, 2, 99], [3, 4]]  ← inner list is shared
print(shallow) # [[1, 2, 99], [3, 4]]

# Rebinding a top-level element does not affect the original
shallow[1] = [7, 8]
print(matrix)  # [[1, 2, 99], [3, 4]]
print(shallow) # [[1, 2, 99], [7, 8]]
```

### When shallow copy is enough
- The container is flat (no nested mutables), e.g., a list of numbers/strings.
- You want to share inner objects intentionally (e.g., large immutable-like objects).

---

## 3) Deep Copy

A deep copy recursively copies every level, producing an entirely independent structure.

```python
import copy

matrix = [[1, 2], [3, 4]]
deep = copy.deepcopy(matrix)

deep[0].append(99)
print(matrix)  # [[1, 2], [3, 4]]
print(deep)    # [[1, 2, 99], [3, 4]]
```

### When to use deep copy
- Your data structure is nested (lists/dicts/sets within each other).
- You need full independence between the original and the copy.

---

## 4) Copying Different Built-ins

### Lists
```python
import copy

numbers = [1, 2, 3]
numbers_shallow = numbers[:]        # shallow
numbers_deep = copy.deepcopy(numbers)  # same as shallow for flat lists
```

### Dicts
```python
import copy

config = {"db": {"host": "localhost", "port": 5432}}
shallow = config.copy()
deep = copy.deepcopy(config)

shallow["db"]["port"] = 5433
print(config["db"]["port"])  # 5433 (shared inner dict!)
```

### Sets
```python
import copy

tags = {"python", "copy"}
tags_shallow = tags.copy()
tags_deep = copy.deepcopy(tags)  # same as shallow for flat sets
```

### Tuples
Tuples are immutable, but they can contain mutable objects:
```python
import copy

t = (1, [2, 3])
shallow = copy.copy(t)
deep = copy.deepcopy(t)

shallow[1].append(4)
print(t)     # (1, [2, 3, 4])  ← inner list is shared in shallow copy
print(deep)  # (1, [2, 3])
```

---

## 5) The `copy` Module Cheat Sheet

```python
import copy

copy.copy(obj)      # shallow copy
copy.deepcopy(obj)  # deep copy
```

What gets copied:
- **Shallow**: New outer container; inner elements are the same objects.
- **Deep**: New outer container and recursively new inner objects.

Performance notes:
- Shallow copies are faster and use less memory.
- Deep copies can be slow for large nested structures. Only use when independence is required.

---

## 6) Custom Classes and Copying

If you have your own classes, `copy.copy` and `copy.deepcopy` attempt to do the right thing by default. You can customize behavior with `__copy__` and `__deepcopy__`.

```python
import copy

class Report:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages  # list of strings

    def __copy__(self):
        # make a shallow copy: copy title (str) and reuse the same pages list
        return type(self)(self.title, self.pages)

    def __deepcopy__(self, memo):
        # deepcopy title and pages list
        copied_title = copy.deepcopy(self.title, memo)
        copied_pages = copy.deepcopy(self.pages, memo)
        return type(self)(copied_title, copied_pages)

original = Report("Q1", ["p1", "p2"])
shallow = copy.copy(original)
deep = copy.deepcopy(original)

shallow.pages.append("p3")
print(original.pages)  # ['p1', 'p2', 'p3']
print(deep.pages)      # ['p1', 'p2']
```

`memo` is a dict that helps `deepcopy` handle shared references and cycles efficiently.

---

## 7) Cycles and Shared References

Deep copying preserves the shape of graphs, including cycles and shared references.

```python
import copy

a = []
a.append(a)     # a contains itself → a cycle

b = copy.deepcopy(a)
print(b is b[0])  # True: cycle preserved in the copy
```

Shallow copy would only create a new outer list but keep the inner self-reference pointing to the original structure.

---

## 8) Common Gotchas

- **Slicing vs deepcopy**: `list[:]` only shallow-copies. Nested mutables remain shared.
- **Dict `.copy()` is shallow**: Use `copy.deepcopy` for nested dicts when you need isolation.
- **Immutable containers aren’t magic**: Tuples containing lists still share the inner lists under shallow copy.
- **Multiplying lists duplicates references**:
  ```python
  rows = [[0] * 3] * 2
  rows[0][0] = 1
  print(rows)  # [[1, 0, 0], [1, 0, 0]]
  ```
  Use a list comprehension to avoid shared rows: `[ [0]*3 for _ in range(2) ]`.
- **Default-arg trap**: Don’t use mutable defaults like `def f(x, cache={}): ...`.

---

## 9) Choosing the Right Approach

- **Use assignment** when you truly want two names for the same object.
- **Use shallow copy** for flat containers or when shared inner objects are desired.
- **Use deep copy** for nested structures when independence is required.

---

## 10) Quick Reference

- **Lists**: `lst[:]`, `list(lst)`, `copy.copy(lst)` → shallow; `copy.deepcopy(lst)` → deep
- **Dicts**: `d.copy()`, `dict(d)`, `copy.copy(d)` → shallow; `copy.deepcopy(d)` → deep
- **Sets**: `s.copy()`, `set(s)`, `copy.copy(s)` → shallow; `copy.deepcopy(s)` → deep
- **Tuples**: shallow vs deep matters only if tuple contains mutables

---

## 11) Minimal runnable examples

Shallow vs deep on nested lists:
```python
import copy

matrix = [[1], [2]]
shallow = matrix[:]         # or copy.copy(matrix)
deep = copy.deepcopy(matrix)

matrix[0].append(99)
print(shallow)  # [[1, 99], [2]]  ← shared inner list
print(deep)     # [[1], [2]]      ← independent
```

Deep copy of nested dict:
```python
import copy

settings = {"theme": {"bg": "dark", "font": "mono"}}
safe = copy.deepcopy(settings)
safe["theme"]["bg"] = "light"
print(settings["theme"]["bg"])  # 'dark'
```

---

### Further reading
- Python docs: `copy` module — `https://docs.python.org/3/library/copy.html`
- Data model methods: `__copy__` and `__deepcopy__`

