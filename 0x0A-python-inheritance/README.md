# Alx Higher Level Programming - Python Inheritance

## Description

This project focuses on understanding and implementing inheritance in Python. It covers key aspects of object-oriented programming, including creating classes, overriding methods, and using built-in functions in conjunction with classes. The goal is to create custom data types while effectively using inheritance in class design.

## Project Structure

| Task                      | Description                                                                                                                                                     | Source Code                    |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------|
| 0. Lookup                 | Write a function that returns the list of available attributes and methods of an object.                                                                       | [0-lookup.py](0-lookup.py)    |
| 1. My list                | Write a class `MyList` that inherits from `list` with a method `print_sorted` that prints the list in sorted order.                                          | [1-my_list.py](1-my_list.py)  |
| 2. Exact same object      | Write a function that returns True if the object is exactly an instance of the specified class; otherwise False.                                              | [2-is_same_class.py](2-is_same_class.py) |
| 3. Same class or inherit  | Write a function that returns True if the object is an instance of, or inherited from the specified class; otherwise False.                                  | [3-is_kind_of_class.py](3-is_kind_of_class.py) |
| 4. Only subclass of       | Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise False. | [4-inherits_from.py](4-inherits_from.py) |
| 5. Geometry module        | Write an empty class `BaseGeometry`.                                                                                                                         | [5-base_geometry.py](5-base_geometry.py) |
| 6. Improve Geometry       | Write a class `BaseGeometry` with a method `area` that raises an Exception with the message `area() is not implemented`.                                     | [6-base_geometry.py](6-base_geometry.py) |
| 7. Integer validator      | Extend `BaseGeometry` to include `integer_validator` that validates integers.                                                                                 | [7-base_geometry.py](7-base_geometry.py) |
| 8. Rectangle              | Write a class `Rectangle` that inherits from `BaseGeometry`, with private attributes for width and height.                                                   | [8-rectangle.py](8-rectangle.py) |
| 9. Full rectangle         | Enhance `Rectangle` to implement the `area()` method and provide string representation.                                                                         | [9-rectangle.py](9-rectangle.py) |
| 10. Square #1             | Write a class `Square` that inherits from `Rectangle` with size validation.                                                                                   | [10-square.py](10-square.py)   |
| 11. Square #2             | Extend `Square` to provide custom string representation.                                                                                                      | [11-square.py](11-square.py)   |
| 12. My integer            | Create a class `MyInt` that inherits from `int`, with inverted `==` and `!=` operators.                                                                        | [100-my_int.py](100-my_int.py) |
| 13. Can I?                | Write a function that adds a new attribute to an object if it’s possible, raising a TypeError if not.                                                          | [101-add_attribute.py](101-add_attribute.py) |

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
- Do not use the words import or from inside your comments, the checker will think you try to import some modules

## Learning Objectives

By the end of this project, you should be able to explain the following concepts:

- Why Python programming is awesome
- What is a superclass, baseclass or parentclass
- What is a subclass
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit class from another
- How to define a class with multiple base classes
- What is the default class every class inherit from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- What is the purpose of inheritance
- What are, when and how to use isinstance, issubclass, type and super built-in functions

## Prototype Table

| Function/Method                    | Prototype                                      |
|------------------------------------|------------------------------------------------|
| lookup                             | `def lookup(obj):`                            |
| MyList.print_sorted                | `def print_sorted(self):`                     |
| is_same_class                      | `def is_same_class(obj, a_class):`           |
| is_kind_of_class                   | `def is_kind_of_class(obj, a_class):`        |
| inherits_from                      | `def inherits_from(obj, a_class):`           |
| BaseGeometry.area                  | `def area(self):`                            |
| BaseGeometry.integer_validator      | `def integer_validator(self, name, value):`  |
| Rectangle.__init__                 | `def __init__(self, width, height):`         |
| Rectangle.area                     | `def area(self):`                            |
| Square.__init__                    | `def __init__(self, size):`                  |
| MyInt.__eq__                      | `def __eq__(self, other):`                   |
| MyInt.__ne__                      | `def __ne__(self, other):`                   |
| add_attribute                      | `def add_attribute(obj, name, value):`      |

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/alx-higher_level_programming.git
   cd alx-higher_level_programming/0x0A-python-inheritance
   ```

2. Run the tasks:
   Each task can be run individually by executing the corresponding main file:
   ```bash
   ./0-main.py
   ./1-main.py
   ./2-main.py
   ```

3. To run the tests:
   Place your test files in the `tests` directory and use:
   ```bash
   python3 -m doctest ./tests/*
   ```

## How to Use
1. Clone the repository.
2. Navigate to the directory containing the Python files.
3. Run the desired main file using Python 3.

## Tasks

### 0. Lookup
Write a function that returns the list of available attributes and methods of an object:

**Prototype:** `def lookup(obj):`

Returns a list object. You are not allowed to import any module.

---

### 1. My list
Write a class `MyList` that inherits from `list`:

Public instance method: `def print_sorted(self):` that prints the list, but sorted (ascending sort). You can assume that all the elements of the list will be of type int. You are not allowed to import any module.

---

### 2. Exact same object
Write a function that returns True if the object is exactly an instance of the specified class; otherwise False.

**Prototype:** `def is_same_class(obj, a_class):`

You are not allowed to import any module.

---

### 3. Same class or inherit from
Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise False.

**Prototype:** `def is_kind_of_class(obj, a_class):`

You are not allowed to import any module.

---

### 4. Only sub class of
Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise False.

**Prototype:** `def inherits_from(obj, a_class):`

You are not allowed to import any module.

---

### 5. Geometry module
Write an empty class `BaseGeometry`.

You are not allowed to import any module.

---

### 6. Improve Geometry
Write a class `BaseGeometry` (based on 5-base_geometry.py).

Public instance method: `def area(self):` that raises an Exception with the message `area() is not implemented`. You are not allowed to import any module.

---

### 7. Integer validator
Write a class `BaseGeometry` (based on 6-base_geometry.py).

Public instance method: `def area(self):` that raises an Exception with the message `area() is not implemented`.

Public instance method: `def integer_validator(self, name, value):` that validates value:
- you can assume name is always a string
- if value is not an integer: raise a TypeError exception, with the message `<name> must be an integer`
- if value is less or equal to 0: raise a ValueError exception with the message `<name> must be greater than 0`

You are not allowed to import any module.

---

### 8. Rectangle
Write a class `Rectangle` that inherits from `BaseGeometry` (7-base_geometry.py).

Instantiation with width and height: `def __init__(self, width, height):`
- width and height must be private. No getter or setter.
- width and height must be positive integers, validated by `integer_validator`.

---

### 9. Full rectangle
Write a class `Rectangle` that inherits from `BaseGeometry` (7-base_geometry.py). (task based on 8-rectangle.py)

Instantiation with width and height: `def __init__(self, width, height):`
- width and height must be private. No getter or setter.
- width and height must be positive integers validated by `integer_validator`.
- the `area()` method must be implemented.
- print() should print, and str() should return, the following rectangle description: `[Rectangle] <width>/<height>`.

---

### 10. Square #1
Write a class `Square` that inherits from `Rectangle` (9-rectangle.py):

Instantiation with size: `def __init__(self, size):`
- size must be private. No getter or setter.
- size must be a positive integer, validated by `integer_validator`.
- the `area()` method must be implemented.

---

### 11. Square #2
Write a class `Square` that inherits from `Rectangle` (9-rectangle.py). (task based on 10-square.py).

Instantiation with size: `def __init__(self, size):`
- size must be private. No getter or setter.
- size must be a positive integer, validated by `integer_validator`.
- the `area()` method must be implemented.
- print() should print, and str() should return, the square description: `[Square] <width>/<height>`.

---

### 12. My integer
Write a class `MyInt` that inherits from `int`:

`MyInt` is a rebel. MyInt has `==` and `!=` operators inverted. You are not allowed to import any module.

---

### 13. Can I?
Write a function that adds a new attribute to an object if it’s possible:

Raise a TypeError exception, with the message `can't add new attribute` if the object can’t have new attributes. You are not allowed to use try/except. You are not allowed to import any module.

### Additional Notes

1. **Classes and Inheritance**:
   - **Superclass/Parent Class**: The class from which properties and methods are inherited.
   - **Subclass/Child Class**: The class that inherits properties and methods from another class.

2. **Attributes and Methods**:
   - Attributes: Variables that belong to a class.
   - Methods: Functions defined within a class.

3. **Multiple Inheritance**: When a class inherits from more than one class.

4. **Overriding**: Redefining a method in a subclass that was defined in a parent class.

5. **Built-in Functions**:
   - `isinstance()`: Checks if an object is an instance of a class or a subclass thereof.
   - `issubclass()`: Checks if a class is a subclass of another class.
   - `type()`: Returns the type of an object.
   - `super()`: Used to call methods from a parent class.
