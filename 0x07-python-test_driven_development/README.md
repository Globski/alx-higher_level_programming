# High-Level Programming - Python Test-driven development

## Description

This project focuses on implementing various Python functions and writing tests using test-driven development (TDD). The tasks cover fundamental concepts in Python programming, including exception handling, matrix operations, and string manipulation.

## Project Structure

| Task | Description | Source Code |
|------|-------------|-------------|
| 0. Integers addition | Write a function that adds 2 integers. `def add_integer(a, b=98):` | `0-add_integer.py` |
| 1. Divide a matrix | Write a function that divides all elements of a matrix. `def matrix_divided(matrix, div):` | `2-matrix_divided.py` |
| 2. Say my name | Write a function that prints `My name is <first name> <last name>`. `def say_my_name(first_name, last_name=""): ` | `3-say_my_name.py` |
| 3. Print square | Write a function that prints a square with the character `#`. `def print_square(size):` | `4-print_square.py` |
| 4. Text indentation | Write a function that prints a text with 2 new lines after each of these characters: `., ?` and `:`. `def text_indentation(text):` | `5-text_indentation.py` |
| 5. Max integer - Unittest | Write unittests for the function `def max_integer(list=[]):`. | `6-max_integer.py`<br>`tests/6-max_integer_test.py` |
| 6. Matrix multiplication | Write a function that multiplies 2 matrices. `def matrix_mul(m_a, m_b):` | `100-matrix_mul.py` |
| 7. Lazy matrix multiplication | Write a function that multiplies 2 matrices by using the module NumPy. `def lazy_matrix_mul(m_a, m_b):` | `101-lazy_matrix_mul.py` |
| 8. CPython #3: Python Strings | Create a function that prints Python strings. `void print_python_string(PyObject *p);` | `102-python.c`<br>`102-tests.py` |

## Terms
- **Test-Driven Development (TDD):** Writing tests before writing the actual code.
- **Unit Tests:** Test individual parts of the code to ensure they work as expected.
- **Edge Cases:** Identifying and testing unusual or extreme conditions.

## Environment

- Ubuntu 20.04 LTS
- Python (version 3.8.5)
- pycodestyle (version 2.8.*)
- NumPy (for task 7)

## Requirements
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- All your files must be executable
- unittest module for testing
- All your tests should be executed by using this command: python3 -m doctest ./tests/*

## Learning Objectives

- Why Python programming is awesome
- What’s an interactive test
- Why tests are important
- How to write Docstrings to create tests
- How to write documentation for each module and function
- What are the basic option flags to create tests
- How to find edge cases
- Understand and apply test-driven development.
- Handle exceptions and validate input types.
- Perform matrix operations and string manipulations.
- Write and run unittests to ensure code correctness.


### How to Use

- Ensure you have the required environment and dependencies installed.
- Run the Python files directly to test the functions.
- Use the unittest framework to execute the test files and validate your implementation.

## Additional Info

- Use `python3 -m unittest tests.6-max_integer_test` to run unittests.
- Ensure NumPy is installed with `pip3 install numpy==1.15.0` for matrix operations in task 7.


## Tasks

### 0. Integers addition
**Mandatory**

Write a function that adds 2 integers.

**Prototype:** `def add_integer(a, b=98):`

- `a` and `b` must be integers or floats, otherwise raise a TypeError exception with the message `a must be an integer` or `b must be an integer`.
- `a` and `b` must be first casted to integers if they are floats.
- Returns an integer: the addition of `a` and `b`.
- You are not allowed to import any module.

**Files:**
- `0-add_integer.py`
- `tests/0-add_integer.txt`

### 1. Divide a matrix
**Mandatory**

Write a function that divides all elements of a matrix.

**Prototype:** `def matrix_divided(matrix, div):`

- `matrix` must be a list of lists of integers or floats, otherwise raise a TypeError exception with the message `matrix must be a matrix (list of lists) of integers/floats`.
- Each row of the matrix must be of the same size, otherwise raise a TypeError exception with the message `Each row of the matrix must have the same size`.
- `div` must be a number (integer or float), otherwise raise a TypeError exception with the message `div must be a number`.
- `div` can’t be equal to 0, otherwise raise a ZeroDivisionError exception with the message `division by zero`.
- All elements of the matrix should be divided by `div`, rounded to 2 decimal places.
- Returns a new matrix.
- You are not allowed to import any module.

**Files:**
- `2-matrix_divided.py`
- `tests/2-matrix_divided.txt`

### 2. Say my name
**Mandatory**

Write a function that prints `My name is <first name> <last name>`.

**Prototype:** `def say_my_name(first_name, last_name=""):`

- `first_name` and `last_name` must be strings otherwise, raise a TypeError exception with the message `first_name must be a string` or `last_name must be a string`.
- You are not allowed to import any module.

**Files:**
- `3-say_my_name.py`
- `tests/3-say_my_name.txt`

### 3. Print square
**Mandatory**

Write a function that prints a square with the character `#`.

**Prototype:** `def print_square(size):`

- `size` is the size length of the square.
- `size` must be an integer, otherwise raise a TypeError exception with the message `size must be an integer`.
- If `size` is less than 0, raise a ValueError exception with the message `size must be >= 0`.
- If `size` is a float and is less than 0, raise a TypeError exception with the message `size must be an integer`.
- You are not allowed to import any module.

**Files:**
- `4-print_square.py`
- `tests/4-print_square.txt`

### 4. Text indentation
**Mandatory**

Write a function that prints a text with 2 new lines after each of these characters: `., ?` and `:`.

**Prototype:** `def text_indentation(text):`

- `text` must be a string, otherwise raise a TypeError exception with the message `text must be a string`.
- There should be no space at the beginning or at the end of each printed line.
- You are not allowed to import any module.

**Files:**
- `5-text_indentation.py`
- `tests/5-text_indentation.txt`

### 5. Max integer - Unittest
**Mandatory**

Since the beginning you have been creating “Interactive tests”. For this exercise, you will add Unittests.

In this task, you will write unittests for the function `def max_integer(list=[]):`.

Your test file should be inside a folder `tests`.

- You have to use the unittest module.
- Your test file should be Python files (extension: `.py`).
- Your test file should be executed by using this command: `python3 -m unittest tests.6-max_integer_test`.
- All tests you make must be passable by the function below.
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case.

**Files:**
- `6-max_integer.py`
- `tests/6-max_integer_test.py`

### 6. Matrix multiplication
**Advanced**

Write a function that multiplies 2 matrices.

**Prototype:** `def matrix_mul(m_a, m_b):`

- `m_a` and `m_b` must be validated with these requirements in this order:
  - `m_a` and `m_b` must be a list of lists of integers or floats:
    - If `m_a` or `m_b` is not a list: raise a TypeError exception with the message `m_a must be a list` or `m_b must be a list`.
    - If `m_a` or `m_b` is not a list of lists: raise a TypeError exception with the message `m_a must be a list of lists` or `m_b must be a list of lists`.
    - If `m_a` or `m_b` is empty (it means: `= []` or `= [[]]`): raise a ValueError exception with the message `m_a can't be empty` or `m_b can't be empty`.
    - If one element of those list of lists is not an integer or a float: raise a TypeError exception with the message `m_a should contain only integers or floats` or `m_b should contain only integers or floats`.
    - If `m_a` or `m_b` is not a rectangle (all ‘rows’ should be of the same size): raise a TypeError exception with the message `each row of m_a must be of the same size` or `each row of m_b must be of the same size`.
    - If `m_a` and `m_b` can’t be multiplied: raise a ValueError exception with the message `m_a and m_b can't be multiplied`.
- You are not allowed to import any module.

**Files:**
- `100-matrix_mul.py`
- `tests/100-matrix_mul.txt`

### 7. Lazy matrix multiplication
**Advanced**

Write a function that multiplies 2 matrices by using the module NumPy.

**To install it:** `pip3 install numpy==1.15.0`

**Prototype:** `def lazy_matrix_mul(m_a, m_b):`

Test cases should be the same as `100-matrix_mul` but with new exception type/message.

**Files:**
- `101-lazy_matrix_mul.py`
- `tests/101-lazy_matrix_mul.txt`

### 8. CPython #3: Python Strings
**Advanced**

Create a function that prints Python strings.

**Prototype:** `void print_python_string(PyObject *p);`

- Format: see example.
- If `p` is not a valid string, print an error message (see example).
- Read: Unicode HOWTO.
- About:
  - Python version: 3.4
  - You are allowed to use the C standard library.
  - Your shared library will be compiled with this command line: `gcc -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 102-python.c`.

**Files:**
- `102-python.c`
- `102-tests.py`

