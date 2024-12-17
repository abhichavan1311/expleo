# Python Data Types

Python provides a variety of built-in data types that are categorized based on their mutability: **immutable** and **mutable**. Understanding these data types and their characteristics is crucial when working with Python.

## 1. Immutable Data Types

Immutable data types are those whose value cannot be modified after they are created. If you need to update an immutable object, Python creates a new object with the updated value.

### Types of Immutable Data Types

- **Numbers**  
  - Includes:
    - `int` (e.g., `1`, `42`)
    - `float` (e.g., `3.14`, `2.0`)
    - `complex` (e.g., `1 + 2j`)
  - Example:
    ```python
    x = 10
    x = x + 1  # A new object is created for the updated value
    ```

- **Strings (`str`)**  
  Strings are sequences of characters.
  - Example:
    ```python
    s = "Hello"
    s = s + " World"  # Creates a new string object
    ```

- **Tuples (`tuple`)**  
  Tuples are ordered collections of items, similar to lists but immutable.
  - Example:
    ```python
    t = (1, 2, 3)
    # t[0] = 10  # This will raise an error
    ```

- **Frozen Sets (`frozenset`)**  
  An immutable version of a set.
  - Example:
    ```python
    fs = frozenset([1, 2, 3])
    # fs.add(4)  # This will raise an error
    ```

- **Booleans (`bool`)**  
  Represents `True` or `False`.
  - Example:
    ```python
    is_valid = True
    ```

- **NoneType**  
  Represents the absence of a value (`None`).
  - Example:
    ```python
    x = None
    ```

---

## 2. Mutable Data Types

Mutable data types are those whose values can be modified after creation. They allow in-place modification without creating a new object.

### Types of Mutable Data Types

- **Lists (`list`)**  
  Ordered collections of items that can be modified.
  - Example:
    ```python
    lst = [1, 2, 3]
    lst[0] = 10  # Modifies the existing list
    ```

- **Dictionaries (`dict`)**  
  Collections of key-value pairs.
  - Example:
    ```python
    d = {"name": "Alice", "age": 25}
    d["age"] = 26  # Updates the dictionary
    ```

- **Sets (`set`)**  
  Unordered collections of unique items.
  - Example:
    ```python
    s = {1, 2, 3}
    s.add(4)  # Modifies the existing set
    ```

- **Byte Arrays (`bytearray`)**  
  Mutable sequences of bytes.
  - Example:
    ```python
    ba = bytearray(b"hello")
    ba[0] = 97  # Modifies the byte array
    ```

---

## 3. Key Differences Between Mutable and Immutable Data Types

| Aspect          | Mutable                           | Immutable                            |
|-----------------|-----------------------------------|--------------------------------------|
| **Modifiability**| Can be changed in-place.           | Cannot be changed after creation.    |
| **Examples**    | list, dict, set                   | int, str, tuple, frozenset          |
| **Performance** | Slower (more overhead for mutability). | Faster (no overhead for changes).  |

---

## 4. Summary Table of Data Types

| Category    | Data Types                                                   |
|-------------|--------------------------------------------------------------|
| **Immutable** | `int`, `float`, `complex`, `str`, `tuple`, `frozenset`, `bool`, `NoneType` |
| **Mutable**   | `list`, `dict`, `set`, `bytearray`                           |
