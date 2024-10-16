# Alx Higher Level Programming - Python Input/Output

## Description

This project focuses on file handling and serialization in Python. It aims to help you understand how to read from and write to files, work with JSON data, and implement basic data structures. The tasks cover various aspects of file handling, JSON serialization, and object-oriented programming, including reading, writing, and manipulating files, as well as creating classes and managing data serialization.

**Objective**: Master file handling in Python, including reading, writing, and JSON manipulation.

## Project Structure

| Task Number | Description                                                                                                                                           | Source Code                     |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|
| 0           | Write a function that reads a text file (UTF8) and prints it to stdout.                                                                              | [0-read_file.py](0-read_file.py)            |
| 1           | Write a function that returns the number of lines of a text file.                                                                                   | [1-number_of_lines.py](1-number_of_lines.py) |
| 2           | Write a function that reads `n` lines of a text file (UTF8) and prints it to stdout.                                                                  | [2-read_lines.py](2-read_lines.py)          |
| 3           | Write a function that writes a string to a text file (UTF8) and returns the number of characters written.                                            | [3-write_file.py](3-write_file.py)          |
| 4           | Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added.                                  | [4-append_write.py](4-append_write.py)      |
| 5           | Write a function that writes an Object to a text file, using JSON representation.                                                                     | [5-save_to_json_file.py](5-save_to_json_file.py) |
| 6           | Write a function that creates an Object from a “JSON file”.                                                                                          | [6-load_from_json_file.py](6-load_from_json_file.py) |
| 7           | Write a script that adds all arguments to a Python list, and then save them to a file.                                                                | [7-add_item.py](7-add_item.py)              |
| 8           | Write a function that returns the dictionary description for JSON serialization of an object.                                                        | [8-class_to_json.py](8-class_to_json.py)    |
| 9           | Write a class Student that defines a student with attributes: first_name, last_name, and age, with a method to return a dictionary representation.  | [9-student.py](9-student.py)                 |
| 10          | Update the Student class to include a method that filters attributes based on a given list.                                                           | [10-student.py](10-student.py)               |
| 11          | Extend the Student class to include a method that reloads attributes from a JSON representation.                                                      | [11-student.py](11-student.py)               |
| 12          | Create a function that returns Pascal's triangle of `n`.                                                                                             | [12-pascal_triangle.py](12-pascal_triangle.py) |
| 13          | Write a function that inserts a line of text to a file after each line containing a specific string.                                                 | [100-append_after.py](100-append_after.py)   |
| 14          | Write a script that reads stdin line by line and computes metrics based on input format.                                                             | [101-stats.py](101-stats.py)                 |

---

## Environment

- Ubuntu 20.04 LTS
- python3 (version 3.8.5)

## Requirements

#### Python Scripts
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc

#### Python Test Cases
- All your files should end with a new line
- All your test files should be inside a folder tests
- All your test files should be text files (extension: .txt)
- All your tests should be executed by using this command: python3 -m doctest ./tests/*
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

#### Documentation

Ensure every module, class, and function has appropriate docstrings explaining their purpose. Example:

```python
def my_function():
    """This function does something important."""
    pass
```

## Learning Objectives

- Why Python programming is awesome
- How to open a file
- How to write text in a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What is and how to use the with statement
- What is JSON
- What is serialization
- What is deserialization
- How to convert a Python data structure to a JSON string
- How to convert a JSON string to a Python data structure

## Prototype Table

| Prototype                             | Description                                                  |
|---------------------------------------|--------------------------------------------------------------|
| `def read_file(filename=""):`        | Reads a text file and prints it to stdout.                  |
| `def number_of_lines(filename=""): `| Returns the number of lines in a text file.                 |
| `def read_lines(filename="", nb_lines=0):` | Reads `n` lines from a text file and prints them.     |
| `def write_file(filename="", text=""): ` | Writes a string to a text file and returns character count. |
| `def append_write(filename="", text=""): ` | Appends a string to a text file and returns character count. |
| `def save_to_json_file(my_obj, filename):` | Writes an object to a JSON file.                      |
| `def load_from_json_file(filename):` | Creates an object from a JSON file.                       |
| `def class_to_json(obj):`           | Returns dictionary description for JSON serialization.     |
| `def to_json(self):`                | Retrieves a dictionary representation of a Student instance.|
| `def to_json(self, attrs=None):`    | Retrieves filtered dictionary representation of a Student instance. |
| `def reload_from_json(self, json):` | Reloads attributes from a JSON representation.            |
| `def pascal_triangle(n):`            | Returns Pascal's triangle of `n`.                          |
| `def append_after(filename="", search_string="", new_string=""): ` | Inserts a line of text after specific strings in a file. |
| `def main():`                        | Main function to read and compute metrics from stdin.      |

## How to Use
- Clone the repository.
- Navigate to the appropriate directory.
- Run the scripts using Python 3.

1. **Set Up Your Environment**:
   - Ensure you are using Ubuntu 20.04 LTS with Python 3.8.5.
   - Install necessary tools (e.g., `pycodestyle`).

2. **Create Python Scripts**:
   - Start each script with the shebang: `#!/usr/bin/python3`.
   - Implement file reading and writing functions.
   - Include functions for JSON serialization/deserialization.

3. **Documentation**:
   - Write docstrings for your modules, classes, and functions.
   - Make sure to include purpose and usage information in each docstring.

4. **Testing**:
   - Create a `tests` directory.
   - Write test cases for your functions using `doctest`.
   - Execute tests with `python3 -m doctest ./tests/*`.

## Additional Notes

1. **File Handling in Python**
   - **Opening a file**: Use the `open()` function.
   - **Reading a file**: Use methods like `.read()`, `.readline()`, or `.readlines()`.
   - **Writing to a file**: Use `.write()` or `.writelines()`.
   - **Using the `with` statement**: Ensures files are properly closed after their suite finishes.

2. **JSON in Python**
   - **Serialization**: Converting a Python object to a JSON string.
   - **Deserialization**: Converting a JSON string back to a Python object.
   - Use the `json` module for these operations.

## Task

### 0. Read File
Write a function that reads a text file (UTF8) and prints it to stdout:

- Prototype: `def read_file(filename=""):`
- You must use the `with` statement.
---
### 1. Number of Lines
Write a function that returns the number of lines of a text file:

- Prototype: `def number_of_lines(filename=""):`
- You must use the `with` statement.
---
### 2. Read N Lines
Write a function that reads `n` lines of a text file (UTF8) and prints it to stdout:

- Prototype: `def read_lines(filename="", nb_lines=0):`
- You must use the `with` statement.
---
### 3. Write to a File
Write a function that writes a string to a text file (UTF8) and returns the number of characters written:

- Prototype: `def write_file(filename="", text=""):`
- You must use the `with` statement.
---
### 4. Append to a File
Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:

- Prototype: `def append_write(filename="", text=""):`
- You must use the `with` statement.
---
### 5. Save to a JSON File
Write a function that writes an Object to a text file, using JSON representation:

- Prototype: `def save_to_json_file(my_obj, filename):`
- You must use the `with` statement.
---
### 6. Load from a JSON File
Write a function that creates an Object from a “JSON file”:

- Prototype: `def load_from_json_file(filename):`
- You must use the `with` statement.
---
### 7. Load, Add, Save
Write a script that adds all arguments to a Python list, and then save them to a file:

- You must use your function `save_to_json_file` from `5-save_to_json_file.py`.
- You must use your function `load_from_json_file` from `6-load_from_json_file.py`.
- The list must be saved as a JSON representation in a file named `add_item.json`.
- If the file doesn’t exist, it should be created.
- You don’t need to manage file permissions / exceptions.
---
### 8. Class to JSON
Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer, and boolean) for JSON serialization of an object:

- Prototype: `def class_to_json(obj):`
- `obj` is an instance of a Class.
- All attributes of the `obj` Class are serializable: list, dictionary, string, integer, and boolean.
- You are not allowed to import any module.
---
### 9. Student to JSON
Write a class Student that defines a student by:

- Public instance attributes: `first_name`, `last_name`, `age`.
- Instantiation with `first_name`, `last_name`, and `age`: `def __init__(self, first_name, last_name, age):`.
- Public method `def to_json(self):` that retrieves a dictionary representation of a Student instance (same as `8-class_to_json.py`).
---
### 10. Student to JSON with Filter
Write a class Student that defines a student by: (based on `9-student.py`)

- Public instance attributes: `first_name`, `last_name`, `age`.
- Instantiation with `first_name`, `last_name`, and `age`: `def __init__(self, first_name, last_name, age):`.
- Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a Student instance (same as `8-class_to_json.py`):
    - If `attrs` is a list of strings, only attribute names contained in this list must be retrieved.
    - Otherwise, all attributes must be retrieved.

### 11. Student to Disk and Reload
Write a class Student that defines a student by: (based on `10-student.py`)
---
- Public instance attributes: `first_name`, `last_name`, `age`.
- Instantiation with `first_name`, `last_name`, and `age`: `def __init__(self, first_name, last_name, age):`.
- Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a Student instance (same as `8-class_to_json.py`):
    - If `attrs` is a list of strings, only attributes name contained in this list must be retrieved.
    - Otherwise, all attributes must be retrieved.
- Public method `def reload_from_json(self, json):` that replaces all attributes of the Student instance:
    - You can assume `json` will always be a dictionary.
    - A dictionary key will be the public attribute name.
    - A dictionary value will be the value of the public attribute.
---
### 12. Pascal's Triangle
Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of `n`:

- Returns an empty list if `n <= 0`.
- You can assume `n` will be always an integer.
- You are not allowed to import any module.
---
### 13. Search and Update
Write a function that inserts a line of text to a file, after each line containing a specific string (see example):

- Prototype: `def append_after(filename="", search_string="", new_string=""):`
- You must use the `with` statement.
- You don’t need to manage file permission or file doesn't exist exceptions.
- You are not allowed to import any module.
---
### 14. Log Parsing
Write a script that reads stdin line by line and computes metrics:

- Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`.
- Each 10 lines and after a keyboard interruption (CTRL + C), prints those statistics since the beginning:
    - Total file size: File size: `<total size>`, where is the sum of all previous (see input format above).
    - Number of lines by status code:
        - possible status code: `200`, `301`, `400`, `401`, `403`, `404`, `405`, and `500`.
        - if a status code doesn’t appear, don’t print anything for this status code.
        - format: `<status code>: <number>`.
        - status codes should be printed in ascending order.
