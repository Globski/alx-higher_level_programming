# High-Level Programming - Python Import & Modules

## Description

This repository contains a collection of Python scripts designed to help you learn important concepts like importing and creating modules, using command-line arguments, and working with functions from external files. Each script focuses on these key topics to gradually build your understanding of how to structure and organize Python programs effectively.

## Project Structure

| Task | Description | Source Code Link |
| ---- | ----------- | ----------------- |
| 0. Import a simple function from a simple file | Program to import a function from an external file | [0-import_add.py](./0-import_add.py), [0-add.py](./0-add.py) |
| 1. My first toolbox! | Program to import functions from an external file and perform mathematical operations | [1-calculation.py](./1-calculation.py), [calculator_1.py](./calculator_1.py) |
| 2. How to make a script dynamic! | Program to print the number and list of command line arguments | [2-args.py](./2-args.py) |
| 3. Infinite addition | Program to print the result of the addition of all command line arguments | [3-infinite_add.py](./3-infinite_add.py) |
| 4. Who are you? | Program to print names defined in a compiled module | [4-hidden_discovery.py](./4-hidden_discovery.py), [hidden_4.pyc](./hidden_4.pyc) |
| 5. Everything can be imported | Program to import a variable from an external file | [5-variable_load.py](./5-variable_load.py), [variable_load_5.py](./variable_load_5.py) |
| 6. Build my own calculator! | Program to import functions and handle basic operations | [100-my_calculator.py](./100-my_calculator.py), [calculator_1.py](./calculator_1.py) |
| 7. Easy print | Program to print a specific string without using print, eval, open, or sys | [101-easy_print.py](./101-easy_print.py) |
| 8. ByteCode -> Python #3 | Python function to match given Python bytecode | [102-magic_calculation.py](./102-magic_calculation.py) |
| 9. Fast alphabet | Program to print the alphabet in uppercase | [103-fast_alphabet.py](./103-fast_alphabet.py) |

## Environment
- Ubuntu 20.04 LTS
- Python 3.8.5.
- Pycodestyle


## Requirements

- All Python scripts are interpreted on Ubuntu 20.04 LTS using Python 3.8.5.
- The project follows the Pycodestyle style guide.
- Python scripts should end with a newline and start with #!/usr/bin/python3.
- All files must be executable.

## Coding Style

This project adheres to the Pycodestyle style guide. Ensure your Python code follows Pycodestyle conventions by running the following command:

```bash
pycodestyle *.py
```

If Pycodestyle is not installed, you can install it using:
```bash
pip install pycodestyle
```

## Learning Objectives
After completing this project, you should be able to explain:

- How to import functions from another file
- How to use imported functions
- How to create a module
- How to use the built-in function dir()
- How to prevent code in your script from being executed when imported
- How to use command line arguments with your Python programs

## How to Use

Before you begin, ensure you have the following installed on your machine:

- Python 3.x (version 3.8.5 recommended)
- Pycodestyle (version 2.8.*)

You can check your Python version using:
```bash
python3 --version
```

### Installation
Clone the repository and navigate to the project directory:
```bash
git clone https://github.com/your-username/alx-higher_level_programming.git
cd alx-higher_level_programming/0x02-python-import_modules
```

Running Python Scripts
Each Python script can be executed using the python3 command. For example:
```bash
python3 0-import_add.py
```

Ensure that all scripts are executable with:
```bash
chmod +x *.py
```

## Additional Notes 
- **How to import functions from another file**: Use the `import` statement to bring functions from one Python file into another.
  
- **How to use imported functions**: Once imported, call the functions using their name as if they were defined in the current file.

- **How to create a module**: A module is a Python file that contains functions, classes, or variables. Save your file with a `.py` extension to create a module.

- **How to use the built-in function `dir()`**: `dir()` returns a list of attributes and methods available in an object or module, helping you inspect its contents.

- **How to prevent code in your script from being executed when imported**: Use `if __name__ == "__main__":` to ensure certain code only runs when the file is executed directly, not when imported.

- **How to use command-line arguments with your Python programs**: Use the `sys.argv` list from the `sys` module to access command-line arguments passed to your script.

## Tasks

0. **Import a simple function from a simple file**
   - Write a program that imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`.
   - You have to use print function with string format to display integers.
   - You have to assign:
     - the value `1` to a variable called `a`
     - the value `2` to a variable called `b`
   - and use those two variables as arguments when calling the functions `add` and `print`.
   - `a` and `b` must be defined in 2 different lines: `a = 1` and another `b = 2`.
   - Your program should print: `<a value> + <b value> = <add(a, b) value>` followed with a new line.
   - You can only use the word `add_0` once in your code.
   - You are not allowed to use `*` for importing or `__import__`.
   - Your code should not be executed when imported.
```python
guillaume@ubuntu:~/0x02$ cat add_0.py
#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)

guillaume@ubuntu:~/0x02$ ./0-add.py
1 + 2 = 3
guillaume@ubuntu:~/0x02$ cat 0-import_add.py
__import__("0-add")
guillaume@ubuntu:~/0x02$ python3 0-import_add.py 
guillaume@ubuntu:~/0x02$ 
```
---

1. **My first toolbox!**
   - Write a program that imports functions from the file `calculator_1.py`, does some Maths, and prints the result.
   - Do not use the function `print` (with string format to display integers) more than 4 times.
   - You have to define:
     - the value `10` to a variable `a`
     - the value `5` to a variable `b`
   - and use those two variables only, as arguments when calling functions (including print).
   - `a` and `b` must be defined in 2 different lines: `a = 10` and another `b = 5`.
   - Your program should call each of the imported functions.
   - The word `calculator_1` should be used only once in your file.
   - You are not allowed to use `*` for importing or `__import__`.
   - Your code should not be executed when imported.
```python
guillaume@ubuntu:~/0x02$ cat calculator_1.py
#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)


def sub(a, b):
    """My subtraction function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    """
    return (a - b)


def mul(a, b):
    """My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    """
    return (a * b)


def div(a, b):
    """My division function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a / b
    """
    return int(a / b)

guillaume@ubuntu:~/0x02$ ./1-calculation.py
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
guillaume@ubuntu:~/0x02$
```
---

2. **How to make a script dynamic!**
   - Write a program that prints the number of and the list of its arguments.
   - The output should be:
     - Number of argument(s) followed by argument (if number is one) or arguments (otherwise), followed by
     - `:` (or `.` if no arguments were passed) followed by
     - a new line, followed by (if at least one argument),
     - one line per argument: the position of the argument (starting at 1) followed by `:` followed by the argument value and a new line.
   - Your code should not be executed when imported.
   - The number of elements of `argv` can be retrieved by using: `len(argv)`.
```python
guillaume@ubuntu:~/0x02$ ./2-args.py 
0 arguments.
guillaume@ubuntu:~/0x02$ ./2-args.py Hello
1 argument:
1: Hello
guillaume@ubuntu:~/0x02$ ./2-args.py Hello Welcome To The Best School
6 arguments:
1: Hello
2: Welcome
3: To
4: The
5: Best
6: School
guillaume@ubuntu:~/0x02$
```
---

3. **Infinite addition**
   - Write a program that prints the result of the addition of all arguments.
   - The output should be the result of the addition of all arguments, followed by a new line.
   - You can cast arguments into integers by using `int()` (you can assume that all arguments can be casted into integers).
   - Your code should not be executed when imported.
   - Remember how you did (or did not) do it in C? #pythoniscool.
```python
guillaume@ubuntu:~/0x02$ ./3-infinite_add.py
0
guillaume@ubuntu:~/0x02$ ./3-infinite_add.py 79 10
89
guillaume@ubuntu:~/0x02$ ./3-infinite_add.py 79 10 -40 -300 89 
-162
guillaume@ubuntu:~/0x02$ 
```

Last but not least, your program should also handle big numbers. And the good news is: if your program works for the above example, it will work for the following example:

```python
guillaume@ubuntu:~/0x02$ ./3-infinite_add.py 1111111111111111111111111111111111111111111111111111111111112222222222222222222222222222222222223435467866765443534434222222254444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555666666666666666666666666666666777777777777777777777777777777888888888888888888888888888888899999999999999999999999990000000000000000000 11111111111111111111111111111111111111111111111111222222222222222222222222222333333333333333333334567788888899999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
11111111111111111111111111111111111111111111111111222222222222222222222222222333333333333333333334568900000011111111111111111111111111111111111111111111111111112222222222222222222222222222222222223435467866765443534434222222254444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555666666666666666666666666666666777777777777777777777777777777888888888888888888888888888888899999999999999999999999989999999999999999999
guillaume@ubuntu:~/0x02$
```
---

4. **Who are you?**
   - Write a program that prints all the names defined by the compiled module `hidden_4.pyc` (please download it locally).
   - You should print one name per line, in alpha order.
   - You should print only names that do not start with `__`.
   - Your code should not be executed when imported.
   - Make sure you are running your code in Python3.8.x (hidden_4.pyc has been compiled with this version).
```python
guillaume@ubuntu:~/0x02$ curl -Lso "hidden_4.pyc" "https://github.com/alx-tools/0x02.py/raw/master/hidden_4.pyc"
guillaume@ubuntu:~/0x02$ ./4-hidden_discovery.py | sort
my_secret_santa
print_hidden
print_school
guillaume@ubuntu:~/0x02$
```
---

5. **Everything can be imported**
   - Write a program that imports the variable `a` from the file `variable_load_5.py` and prints its value.
   - You are not allowed to use `*` for importing or `__import__`.
   - Your code should not be executed when imported.
```python
guillaume@ubuntu:~/0x02$ cat variable_load_5.py
#!/usr/bin/python3
a = 98
"""Simple variable
"""

guillaume@ubuntu:~/0x02$ ./5-variable_load.py
98
guillaume@ubuntu:~/0x02$
```
---

6. **Build my own calculator!**
   - Write a program that imports all functions from the file `calculator_1.py` and handles basic operations.
   - Usage: `./100-my_calculator.py a operator b`.
   - If the number of arguments is not `3`, your program has to:
     - print `Usage: ./100-my_calculator.py <a> <operator> <b>` followed with a new line.
     - exit with the value `1`.
   - `operator` can be:
     - `+` for addition
     - `-` for subtraction
     - `*` for multiplication
     - `/` for division.
   - If the operator is not one of the above:
     - print `Unknown operator. Available operators: +, -, * and /` followed with a new line.
     - exit with the value `1`.
   - You can cast `a` and `b` into integers by using `int()` (you can assume that all arguments will be castable into integers).
   - The result should be printed like this: `<a> <operator> <b> = <result>`, followed by a new line.
   - You are not allowed to use `*` for importing or `__import__`.
   - Your code should not be executed when imported.
```python
guillaume@ubuntu:~/0x02$ cat calculator_1.py
#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)


def sub(a, b):
    """My subtraction function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    """
    return (a - b)


def mul(a, b):
    """My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    """
    return (a * b)


def div(a, b):
    """My division function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a / b
    """
    return int(a / b)

guillaume@ubuntu:~/0x02$ ./100-my_calculator.py ; echo $?
Usage: ./100-my_calculator.py <a> <operator> <b>
1
guillaume@ubuntu:~/0x02$ ./100-my_calculator.py 3 + 5 ; echo $?
3 + 5 = 8
0
guillaume@ubuntu:~/0x02$ ./100-my_calculator.py 3 H 5 ; echo $?
Unknown operator. Available operators: +, -, * and /
1
guillaume@ubuntu:~/0x02$
```
---

7. **Easy print**
   - Write a program that prints `#pythoniscool`, followed by a new line, in the standard output.
   - Your program should be maximum `2` lines long.
   - You are not allowed to use `print` or `eval` or `open` or `import sys` in your file `101-easy_print.py`.
```python
guillaume@ubuntu:~/0x02$ ./101-easy_print.py
#pythoniscool
guillaume@ubuntu:~/0x02$
```
---

8. **ByteCode -> Python #3**
   - Write the Python function `def magic_calculation(a, b):` that does exactly the same as the following Python bytecode:
     - (bytecode content)
   - Tip: Python bytecode.
```python
  3           0 LOAD_CONST               1 (0)
              3 LOAD_CONST               2 (('add', 'sub'))
              6 IMPORT_NAME              0 (magic_calculation_102)
              9 IMPORT_FROM              1 (add)
             12 STORE_FAST               2 (add)
             15 IMPORT_FROM              2 (sub)
             18 STORE_FAST               3 (sub)
             21 POP_TOP

  4          22 LOAD_FAST                0 (a)
             25 LOAD_FAST                1 (b)
             28 COMPARE_OP               0 (<)
             31 POP_JUMP_IF_FALSE       94

  5          34 LOAD_FAST                2 (add)
             37 LOAD_FAST                0 (a)
             40 LOAD_FAST                1 (b)
             43 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             46 STORE_FAST               4 (c)

  6          49 SETUP_LOOP              38 (to 90)
             52 LOAD_GLOBAL              3 (range)
             55 LOAD_CONST               3 (4)
             58 LOAD_CONST               4 (6)
             61 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             64 GET_ITER
        >>   65 FOR_ITER                21 (to 89)
             68 STORE_FAST               5 (i)

  7          71 LOAD_FAST                2 (add)
             74 LOAD_FAST                4 (c)
             77 LOAD_FAST                5 (i)
             80 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             83 STORE_FAST               4 (c)
             86 JUMP_ABSOLUTE           65
        >>   89 POP_BLOCK

  8     >>   90 LOAD_FAST                4 (c)
             93 RETURN_VALUE

 10     >>   94 LOAD_FAST                3 (sub)
             97 LOAD_FAST                0 (a)
            100 LOAD_FAST                1 (b)
            103 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
            106 RETURN_VALUE
            107 LOAD_CONST               0 (None)
            110 RETURN_VALUE
```
[Tip: Python bytecode](https://docs.python.org/3.4/library/dis.html)

---

9. **Fast alphabet**
   - Write a program that prints the alphabet in uppercase, followed by a new line.
   - Your program should be maximum `3` lines long.
   - You are not allowed to use:
     - any loops
     - any conditional statements
     - `str.join()`
     - any string literal
     - any system calls.
```python
guillaume@ubuntu:~/0x02$ ./103-fast_alphabet.py
ABCDEFGHIJKLMNOPQRSTUVWXYZ
guillaume@ubuntu:~/0x02$ wc -l 103-fast_alphabet.py
3 103-fast_alphabet.py
guillaume@ubuntu:~/0x02$
```
