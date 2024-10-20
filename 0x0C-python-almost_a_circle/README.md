# Alx Higher Level Programming - Python Almost a circle

## Description

This project focuses on creating classes to represent geometric shapes, with an emphasis on how to manipulate these objects, save them (serialization), and display them visually. The key classes include a **Base** class, which handles common attributes and functions, and two specific shape classes: **Rectangle** and **Square**. The project also covers how to save and load these objects using **JSON** and **CSV** formats (serialization and deserialization). Additionally, it demonstrates how to draw these shapes using **Turtle graphics** for a visual representation.


## Project Structure

| Task No. | Description                                                                 | Source Code                  |
|----------|-----------------------------------------------------------------------------|-------------------------------|
| 0        | Base class                                                                 | models/base.py                |
| 1        | Rectangle class                                                            | models/rectangle.py           |
| 2        | Square class                                                               | models/square.py              |
| 3        | String representation                                                       | models/rectangle.py           |
| 4        | Area calculation                                                           | models/rectangle.py           |
| 5        | Update method                                                              | models/rectangle.py           |
| 6        | Dictionary representation                                                   | models/rectangle.py           |
| 7        | JSON string conversion                                                      | models/base.py                |
| 8        | JSON string to file                                                        | models/base.py                |
| 9        | JSON string to dictionary                                                  | models/base.py                |
| 10       | Dictionary to instance                                                      | models/base.py                |
| 11       | File to instances                                                          | models/base.py                |
| 12       | CSV serialization                                                           | models/base.py                |
| 13       | Graphical representation using Turtle                                       | models/base.py                |
| 14       | Square instance to dictionary representation                                | models/square.py              |
| 15       | Dictionary to JSON string                                                   | models/base.py                |
| 16       | JSON string to file                                                         | models/base.py                |
| 17       | JSON string to dictionary                                                   | models/base.py                |
| 18       | Dictionary to Instance                                                      | models/base.py                |
| 19       | File to instances                                                          | models/base.py                |
| 20       | JSON ok, but CSV?                                                          | models/base.py                |
| 21       | Let's draw it                                                              | models/base.py                |

## Environment

- Ubuntu 20.04 LTS
- Python 3 (version 3.8.5).
- pycodestyle (version 2.8.*)
- Turtle graphics library

## Requirements
  - All files must be executable.
  - Use `wc` to test the length of files.

### Python Scripts

- All scripts should start with the line:
  ```python
  #!/usr/bin/python3
  ```
- **Interpreter:** All scripts must be interpreted on Ubuntu 20.04 LTS using Python 3 (version 3.8.5).
- Ensure all files are executable.
- Follow the PEP 8 style guide using `
- Document all modules, classes, and functions properly.

### Python Unit Tests

- Use the `unittest` module for testing.
- Create a `tests` directory containing test files that follow the naming pattern `test_<module_name>.py`.
- Test files should be named starting with `test_`.
- All test files must be in a folder named `tests`.
- The organization of test files should mirror the project structure (e.g., for `models/base.py`, tests should be in `tests/test_models/test_base.py`).
- Execute tests using:
  ```bash
  python3 -m unittest discover tests
  ```

- **Execution Command:** 
  - To discover all tests: `python3 -m unittest discover tests`.
  - To run a specific test file: `python3 -m unittest tests/test_models/test_base.py`.

#### Documentation
- All modules, classes, and functions must be documented.
  - Example command for modules: `python3 -c 'print(__import__("my_module").__doc__)'`
  - Example command for classes: `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`
  - Example command for functions: `python3 -c 'print(__import__("my_module").my_function.__doc__)'`

## Learning Objectives

By completing this project, you will be able to:

- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

## Prototypes Used in the Project

| Prototype        | Description                                       |
|------------------|---------------------------------------------------|
| `Base`           | Manages the ID attribute for future classes.     |
| `Rectangle`      | Represents a rectangle with width and height.    |
| `Square`         | Inherits from Rectangle, represents a square.    |
| `to_json_string` | Converts a list of dictionaries to JSON string.  |
| `save_to_file`   | Saves JSON string representation to a file.      |
| `load_from_file` | Loads instances from a JSON file.                |
| `draw`           | Uses Turtle graphics to draw rectangles and squares.|


## How to Use
1. Clone the repository.
2. Navigate to the project directory.
3. Use the provided scripts to create and manipulate Rectangle and Square instances.
4. Run the Turtle graphics program to visualize the shapes.

## Usage

You can run the provided test scripts to see the functionality in action:

```bash
python3 0-main.py
```

## Additional Notes 

**Unit Testing**
Unit testing is the process of testing individual units or components of a program (like functions or methods) to ensure they work correctly. It helps catch bugs early and ensures code reliability.

   **How to Implement in a Large Project:**
   - Use a testing framework like **unittest** (built-in Python library) or **pytest**.
   - Break down the project into smaller, testable units (classes, functions).
   - Write test cases for each unit, focusing on different scenarios (expected behavior, edge cases, error handling).
   - Organize test files separately (e.g., create a `tests` directory).
   - Automate running tests, especially in Continuous Integration (CI) pipelines.

**Serialization and Deserialization of a Class**
   **Serialization:** Converting an object into a format that can be stored (like JSON, CSV, etc.).
   
   **Deserialization:** Converting stored data back into an object.


**What is *args and How to Use It**
`*args` allows a function to accept a variable number of positional arguments.

**What is **kwargs and How to Use It**

`**kwargs` allows a function to accept a variable number of keyword arguments (i.e., named arguments).

**Handling Named Arguments in a Function**
   
   **Named arguments** are specified by their name when calling a function, and they make the function call more readable.

## Tasks

0. **Base class**
   - Create a base class `Base` that manages the `id` attribute for future classes.

1. **Rectangle class**
   - Implement the `Rectangle` class inheriting from `Base` with attributes `width`, `height`, `x`, and `y`.

2. **Square class**
   - Create the `Square` class inheriting from `Rectangle`, with the `size` attribute.

3. **String representation**
   - Override the `__str__` method for `Rectangle` and `Square` to provide a specific string representation.

4. **Area calculation**
   - Implement the `area()` method for both `Rectangle` and `Square`.

5. **Update method**
   - Add an `update()` method to both classes to update attributes based on positional and keyword arguments.

6. **Dictionary representation**
   - Implement a `to_dictionary()` method for both classes that returns a dictionary representation of the object.

7. **JSON string conversion**
   - Create a static method in `Base` to convert a list of dictionaries to a JSON string.

8. **JSON string to file**
   - Implement a class method to save the JSON string representation of objects to a file.

9. **JSON string to dictionary**
   - Add a static method to convert a JSON string back to a list of dictionaries.

10. **Dictionary to instance**
    - Implement a method to create an instance from a dictionary using the `update()` method.

11. **File to instances**
    - Create a class method to load instances from a JSON file.

12. **CSV serialization**
    - Implement methods to serialize and deserialize the `Rectangle` and `Square` classes to and from CSV format.

13. **Graphical representation**
    - Use the Turtle graphics module to visually represent `Rectangle` and `Square` instances.

14. **Square instance to dictionary representation**
    - Update the class Square by adding the public method `def to_dictionary(self)` that returns the dictionary representation of a Square.

15. **Dictionary to JSON string**
    - Update the class Base by adding the static method `def to_json_string(list_dictionaries)` that returns the JSON string representation of `list_dictionaries`.

16. **JSON string to file**
    - Update the class Base by adding the class method `def save_to_file(cls, list_objs)` that writes the JSON string representation of `list_objs` to a file.

17. **JSON string to dictionary**
    - Update the class Base by adding the static method `def from_json_string(json_string)` that returns the list of the JSON string representation `json_string`.

18. **Dictionary to Instance**
    - Update the class Base by adding the class method `def create(cls, **dictionary)` that returns an instance with all attributes already set.

19. **File to instances**
    - Update the class Base by adding the class method `def load_from_file(cls)` that returns a list of instances.

20. **JSON ok, but CSV?**
    - Update the class Base by adding the class methods `def save_to_file_csv(cls, list_objs)` and `def load_from_file_csv(cls)` that serializes and deserializes in CSV.

21. **Let's draw it**
    - Update the class Base by adding the static method `def draw(list_rectangles, list_squares)` that opens a window and draws all the Rectangles and Squares.
