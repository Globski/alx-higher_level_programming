# High-Level Programming - Python Test-driven development

## Description

This project focuses on implementing various Python functions and writing tests using test-driven development (TDD). You'll explore fundamental concepts in Python programming, including exception handling, matrix operations, and string manipulation. By completing the tasks, you will gain practical experience in writing functions and ensuring their correctness through testing.

## Project Structure

| Task | Description | Source Code |
|------|-------------|-------------|
| 0. Integers addition | Write a function that adds 2 integers. `def add_integer(a, b=98):` | [0-add_integer.py](0-add_integer.py) |
| 1. Divide a matrix | Write a function that divides all elements of a matrix. `def matrix_divided(matrix, div):` | [2-matrix_divided.py](2-matrix_divided.py) |
| 2. Say my name | Write a function that prints `My name is <first name> <last name>`. `def say_my_name(first_name, last_name=""): ` | [3-say_my_name.py](3-say_my_name.py) |
| 3. Print square | Write a function that prints a square with the character `#`. `def print_square(size):` | [4-print_square.py](4-print_square.py) |
| 4. Text indentation | Write a function that prints a text with 2 new lines after each of these characters: `., ?` and `:`. `def text_indentation(text):` | [5-text_indentation.py](5-text_indentation.py) |
| 5. Max integer - Unittest | Write unittests for the function `def max_integer(list=[]):`. | [6-max_integer.py](6-max_integer.py) <br> [tests/6-max_integer_test.py](tests/6-max_integer_test.py) |
| 6. Matrix multiplication | Write a function that multiplies 2 matrices. `def matrix_mul(m_a, m_b):` | [100-matrix_mul.py](100-matrix_mul.py) |
| 7. Lazy matrix multiplication | Write a function that multiplies 2 matrices by using the module NumPy. `def lazy_matrix_mul(m_a, m_b):` | [101-lazy_matrix_mul.py](101-lazy_matrix_mul.py) |
| 8. CPython #3: Python Strings | Create a function that prints Python strings. `void print_python_string(PyObject *p);` | [102-python.c](102-python.c) <br> [102-tests.py](102-tests.py) |


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

##### Example Usage
**To run the unittests for task 5:**

```sh
python3 -m unittest tests/6-max_integer_test.py
```

**To install NumPy for task 7:**

```sh
pip3 install numpy==1.15.0
```
- Ensure NumPy is installed with `pip3 install numpy==1.15.0` for matrix operations in task 7.

## Additional Notes

- **Test-Driven Development (TDD):** Writing tests before writing the actual code.
- **Unit Tests:** Test individual parts of the code to ensure they work as expected.
- **Edge Cases:** Identifying and testing unusual or extreme conditions.

- **Why Python programming is awesome**: Python is praised for its simplicity, readability, and versatility, making it accessible for beginners and powerful for experts.

- **What’s an interactive test**: An interactive test allows users to run code snippets and see immediate results, helping to validate functionality in real-time.

- **Why tests are important**: Tests ensure that code behaves as expected, catch bugs early, and help maintain code quality as projects grow.

- **How to write Docstrings to create tests**: Use Docstrings to describe the purpose and usage of functions, providing a clear understanding of their behavior for tests.

- **How to write documentation for each module and function**: Clearly document each module and function, detailing inputs, outputs, and any side effects to enhance usability and maintainability.

- **What are the basic option flags to create tests**: Basic option flags like `-v` (verbose), `-q` (quiet), and `-f` (failfast) help customize the output of test results when running tests.

- **How to find edge cases**: Identify edge cases by considering extreme or unexpected input values, which can help uncover hidden bugs.

- **Understand and apply test-driven development**: TDD is a methodology where tests are written before the code itself, guiding development and ensuring each piece of code meets its requirements.

- **Handle exceptions and validate input types**: Use exception handling to manage errors gracefully and validate input types to ensure functions receive the expected data.

- **Perform matrix operations and string manipulations**: Implement functions to handle operations on matrices (like addition and multiplication) and manipulate strings (like reversing or formatting).

- **Write and run unittests to ensure code correctness**: Use the `unittest` framework to create and execute tests that verify the accuracy of your code, ensuring it behaves as intended.

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

```python
guillaume@ubuntu:~/0x07$ cat 0-main.py
#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)

guillaume@ubuntu:~/0x07$ ./0-main.py
3
98
100
98
b must be an integer
a must be an integer
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/0-add_integer.txt | tail -2
9 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/0x07$ python3 -c 'print(__import__("0-add_integer").__doc__)' | wc -l
5
guillaume@ubuntu:~/0x07$ python3 -c 'print(__import__("0-add_integer").add_integer.__doc__)' | wc -l
3
guillaume@ubuntu:~/0x07$
```

---

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

```python
guillaume@ubuntu:~/0x07$ cat 2-main.py
#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)

guillaume@ubuntu:~/0x07$ ./2-main.py
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
[[1, 2, 3], [4, 5, 6]]
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/2-matrix_divided.txt | tail -2
5 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/0x07$ 
```

---

### 2. Say my name
**Mandatory**

Write a function that prints `My name is <first name> <last name>`.

**Prototype:** `def say_my_name(first_name, last_name=""):`

- `first_name` and `last_name` must be strings otherwise, raise a TypeError exception with the message `first_name must be a string` or `last_name must be a string`.
- You are not allowed to import any module.

**Files:**
- `3-say_my_name.py`
- `tests/3-say_my_name.txt`

```python

guillaume@ubuntu:~/0x07$ cat 3-main.py
#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name("Bob")
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)

guillaume@ubuntu:~/0x07$ ./3-main.py | cat -e
My name is John Smith$
My name is Walter White$
My name is Bob $
first_name must be a string$
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/3-say_my_name.txt | tail -2
5 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/0x07$

```

---

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

```python
guillaume@ubuntu:~/0x07$ cat 4-main.py
#!/usr/bin/python3
print_square = __import__('4-print_square').print_square

print_square(4)
print("")
print_square(10)
print("")
print_square(0)
print("")
print_square(1)
print("")
try:
    print_square(-1)
except Exception as e:
    print(e)
print("")

guillaume@ubuntu:~/0x07$ ./4-main.py
####
####
####
####

##########
##########
##########
##########
##########
##########
##########
##########
##########
##########


#

size must be >= 0

guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/4-print_square.txt
guillaume@ubuntu:~/0x07$
```

---

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

```python
guillaume@ubuntu:~/0x07$ cat 5-main.py
#!/usr/bin/python3
text_indentation = __import__('5-text_indentation').text_indentation

text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")

guillaume@ubuntu:~/0x07$ ./5-main.py | cat -e
Lorem ipsum dolor sit amet, consectetur adipiscing elit.$
$
Quonam modo?$
$
Utrum igitur tibi litteram videor an totas paginas commovere?$
$
Non autem hoc:$
$
igitur ne illud quidem.$
$
Fortasse id optimum, sed ubi illud:$
$
Plus semper voluptatis?$
$
Teneo, inquit, finem illi videri nihil dolere.$
$
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum rationi oboediens.$
$
Si id dicis, vicimus.$
$
Inde sermone vario sex illa a Dipylo stadia confecimus.$
$
Sin aliud quid voles, postea.$
$
Quae animi affectio suum cuique tribuens atque hanc, quam dico.$
$
Utinam quidem dicerent alium alio beatiorem! Iam ruinas videresguillaume@ubuntu:~/0x07$
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/5-text_indentation.txt
guillaume@ubuntu:~/0x07$ 
```

---

### 5. Max integer - Unittest
**Mandatory**

Since the beginning you have been creating “Interactive tests”. For this exercise, you will add Unittests.

In this task, you will write unittests for the function `def max_integer(list=[]):`.

Your test file should be inside a folder `tests`.

- You have to use the [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest).
- Your test file should be Python files (extension: `.py`).
- Your test file should be executed by using this command: `python3 -m unittest tests.6-max_integer_test`.
- All tests you make must be passable by the function below.
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case.

**Files:**
- `6-max_integer.py`
- `tests/6-max_integer_test.py`

```python
guillaume@ubuntu:~/0x07$ cat 6-max_integer.py
#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result

guillaume@ubuntu:~/0x07$ 
guillaume@ubuntu:~/0x07$ cat 6-main.py
#!/usr/bin/python3
max_integer = __import__('6-max_integer').max_integer

print(max_integer([1, 2, 3, 4]))
print(max_integer([1, 3, 4, 2]))
guillaume@ubuntu:~/0x07$
guillaume@ubuntu:~/0x07$ ./6-main.py
4
4
guillaume@ubuntu:~/0x07$
guillaume@ubuntu:~/0x07$ python3 -m unittest tests.6-max_integer_test 2>&1 | tail -1
OK
guillaume@ubuntu:~/0x07$
guillaume@ubuntu:~/0x07$ head -7 tests/6-max_integer_test.py 
#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
guillaume@ubuntu:~/0x07$
```

---

### 6. Matrix multiplication
**Advanced**

Write a function that multiplies 2 matrices.
Read: [Matrix multiplication - only Matrix product (two matrices)](https://en.wikipedia.org/wiki/Matrix_multiplication)

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

```python
guillaume@ubuntu:~/0x07$ cat 100-main.py
#!/usr/bin/python3
matrix_mul = __import__('100-matrix_mul').matrix_mul

print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))

guillaume@ubuntu:~/0x07$ ./100-main.py 
[[7, 10], [15, 22]]
[[13, 16]]
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/100-matrix_mul.txt | tail -2
6 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/0x07$
```

---

### 7. Lazy matrix multiplication
**Advanced**

Write a function that multiplies 2 matrices by using the module [NumPy](https://numpy.org/).

**To install it:** `pip3 install numpy==1.15.0`

**Prototype:** `def lazy_matrix_mul(m_a, m_b):`

Test cases should be the same as `100-matrix_mul` but with new exception type/message.

**Files:**
- `101-lazy_matrix_mul.py`
- `tests/101-lazy_matrix_mul.txt`

```python
guillaume@ubuntu:~/0x07$ cat 101-main.py
#!/usr/bin/python3
lazy_matrix_mul = __import__('101-lazy_matrix_mul').lazy_matrix_mul

print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]]))

guillaume@ubuntu:~/0x07$ ./101-main.py 
[[ 7 10]
 [15 22]]
[[13 16]]
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/101-lazy_matrix_mul.txt 
guillaume@ubuntu:~/0x07$ 
```

---

### 8. CPython #3: Python Strings
**Advanced**

Create a function that prints Python strings.

**Prototype:** `void print_python_string(PyObject *p);`

- Format: see example.
- If `p` is not a valid string, print an error message (see example).
- Read: [Unicode HOWTO](https://docs.python.org/3.4/howto/unicode.html).
- About:
  - Python version: 3.4
  - You are allowed to use the C standard library.
  - Your shared library will be compiled with this command line: `gcc -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 102-python.c`.

**Files:**
- `102-python.c`
- `102-tests.py`

```python
julien@ubuntu:~/0x07. Pyhton Strings$ cat 102-tests.py
import ctypes

lib = ctypes.CDLL('./libPython.so')
lib.print_python_string.argtypes = [ctypes.py_object]
s = "The spoon does not exist"
lib.print_python_string(s)
s = "ложка не существует"
lib.print_python_string(s)
s = "La cuillère n'existe pas"
lib.print_python_string(s)
s = "勺子不存在"
lib.print_python_string(s)
s = "숟가락은 존재하지 않는다."
lib.print_python_string(s)
s = "スプーンは存在しない"
lib.print_python_string(s)
s = b"The spoon does not exist"
lib.print_python_string(s)
julien@ubuntu:~/0x07. Pyhton Strings$ gcc -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 102-python.c
julien@ubuntu:~/0x07. Pyhton Strings$ python3 ./102-tests.py
[.] string object info
  type: compact ascii
  length: 24
  value: The spoon does not exist
[.] string object info
  type: compact unicode object
  length: 19
  value: ложка не существует
[.] string object info
  type: compact unicode object
  length: 24
  value: La cuillère n'existe pas
[.] string object info
  type: compact unicode object
  length: 5
  value: 勺子不存在
[.] string object info
  type: compact unicode object
  length: 14
  value: 숟가락은 존재하지 않는다.
[.] string object info
  type: compact unicode object
  length: 10
  value: スプーンは存在しない
[.] string object info
  [ERROR] Invalid String Object
julien@ubuntu:~/0x07. Pyhton Strings$ 
```
