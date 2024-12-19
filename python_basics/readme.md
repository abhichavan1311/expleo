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


# Conditional Statement

# Python Conditional Statements and Loop Control

This repository contains examples demonstrating Python conditional statements and loop control mechanisms. Below are the concepts covered in the script.

---

## Contents

1. **If Statement**
2. **If with Logical Operators**
3. **If-Else Statement**
4. **If-Elif-Else Statement**
5. **Nested If Statement**
6. **Using Conditional Statements with `in` or `is`**
7. **Break Statement**
8. **Continue Statement**
9. **Pass Statement**

---


for conditional statement details refer: https://github.com/abhichavan1311/expleo/blob/main/python_basics/02_Conditional_statement/02_conditional_statement.py

# Input Functions
---

## Contents

1. **Basic Input**
2. **Input with Type Conversion**
3. **Input with Default Value**
4. **Multiple Inputs on a Single Line**
5. **Input Validation**
6. **Yes/No Input**
7. **Input for Lists**
8. **Menu-Driven Input**
9. **Reusable Input Pattern with Default Values**
10. **Password Input**
11. **Perform Operations on a List of Numbers**

---

## Overview

### 1. Basic Input
Use the `input()` function to accept user input and display it back to the user. This is suitable for simple prompts like entering a name.

---

### 2. Input with Type Conversion
Convert the user input to specific data types like `int` or `float` using casting functions. This is particularly useful when dealing with numeric inputs.

---

### 3. Input with Default Value
Allow users to provide optional input, and use a default value if none is provided. This can be achieved using the `or` operator after stripping spaces from the input.

---

### 4. Multiple Inputs on a Single Line
Use `split()` and `map()` to accept multiple values from a single input line. This approach is useful when users need to input several values separated by spaces.

---

### 5. Input Validation
Ensure user input meets specific criteria (e.g., numbers only). A common approach involves looping until valid input is received.

---

### 6. Yes/No Input
Standardize yes/no inputs by converting them to lowercase and stripping whitespace, making it easier to handle user confirmation prompts.

---

### 7. Input for Lists
Use `map()` to process multiple inputs as a list. This is helpful for tasks involving a collection of numbers or other items.

---

### 8. Menu-Driven Input
Present a menu of options to the user and use conditional statements to execute the corresponding actions based on the user's choice.

---

### 9. Reusable Input Pattern with Default Values
Create a reusable input function to reduce redundancy and simplify the codebase. This function can handle optional inputs with default values.

---

### 10. Password Input
- **Masked Input:** Use the `getpass` module for secure password input where the typed characters are not displayed.
- **Unmasked Input:** Use the standard `input()` function for passwords when masking isn't necessary.

---

### 11. Perform Operations on a List of Numbers
Accept a list of numbers from the user, display a menu for arithmetic operations (Add, Subtract, Multiply, Divide), and perform the chosen operation on the list.

---

## Example Scenarios

### Scenario 1: Input with Default Value
- If the user skips the input, the default value is applied automatically.

---

### Scenario 2: Input Validation
- If the user enters invalid data, the program prompts them to re-enter until valid input is received.

---

### Scenario 3: Menu and List Operations
- Combines menu-driven input and list processing to perform arithmetic operations on a user-defined list of numbers.

---

## Notes
- **Type Conversion:** Always ensure proper typecasting to avoid runtime errors.
- **Validation:** Add checks to ensure user inputs are valid (e.g., checking for digits in a number input).
- **User Feedback:** Provide clear prompts and error messages to guide the user.
- **Security:** For passwords, use masked input (`getpass`) for better security.

---
# File handling
---

## Table of Contents

1. **Current Working Directory**
2. **Reading Files**
3. **Overwriting File Content**
4. **Appending to a File**
5. **Renaming a File**
6. **Moving a File**
7. **Deleting a File**
8. **Copying a File**
9. **Checking if a File Exists**
10. **Working with JSON Files**

---

## Overview

### 1. Current Working Directory
- Use `os.getcwd()` to print the current working directory.
- Helpful for ensuring the script accesses the correct file path.

---

### 2. Reading Files
- Open a file in read mode (`"r"`) using the `open()` function.
- Example: Reading the entire content of `file.bin`.

---

### 3. Overwriting File Content
- Use write mode (`"w"`) to overwrite a file's content.
- Example: Write new content to `file.bin` and read it back.

---

### 4. Appending to a File
- Open a file in append mode (`"a+"`) to add new content to the end of a file.
- Example: Append a conversation to `file.bin`.

---

### 5. Renaming a File
- Use `os.rename()` to rename a file.
- Example: Rename `file.bin` to `file_renamed.bin`.

---

### 6. Moving a File
- Use `shutil.move()` to move a file to a new directory.
- Example: Move `file_renamed.bin` to `python_basics/`.

---

### 7. Deleting a File
- Use `os.remove()` to delete a file.
- Example: Remove a file named `abhishek.txt`.

---

### 8. Copying a File
- Use `shutil.copy()` to copy a file to a new location.
- Example: Copy `python_basics/file_renamed.bin` back to the current directory.

---

### 9. Checking if a File Exists
- Use `os.path.exists()` to check whether a file exists.
- Example: Verify the existence of `python_basics/file_renamed.bin`.

---

### 10. Working with JSON Files

#### Writing JSON Data to a File
- Use the `json.dump()` method to write JSON data to a file.
- Example: Save a dictionary as `data.json`.

#### Reading JSON Data from a File
- Use the `json.load()` method to read JSON data from a file.
- Example: Load and print data from `data.json`.

---

## Notes

- **File Modes:** Always use the appropriate mode (`"r"`, `"w"`, `"a+"`, etc.) based on the operation.
- **Error Handling:** Use try-except blocks to handle potential file errors (e.g., file not found).
- **Absolute vs. Relative Paths:** Ensure file paths are correctly set relative to `os.getcwd()`.
- **JSON Operations:** Use the `json` module for structured data handling in files.

---
