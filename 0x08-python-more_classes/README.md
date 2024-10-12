# Alx Higher Level Programming - Python More Classes and Objects

## Description

This project contains tasks aimed at deepening understanding of object-oriented programming in Python, focusing on class definitions, instance management, and special methods.

## Project Structure

| Task | Description | Source Code |
|------|-------------|-------------|
| 0 | My First Rectangle | [0-rectangle.py](0-rectangle.py) |
| 1 | Rectangle | [1-rectangle.py](1-rectangle.py) |
| 2 | Area and Perimeter | [2-rectangle.py](2-rectangle.py) |
| 3 | String Representation | [3-rectangle.py](3-rectangle.py) |
| 4 | Eval String Representation | [4-rectangle.py](4-rectangle.py) |
| 5 | Detect Instance Deletion | [5-rectangle.py](5-rectangle.py) |
| 6 | How Many Instances | [6-rectangle.py](6-rectangle.py) |
| 7 | Change Representation | [7-rectangle.py](7-rectangle.py) |
| 8 | Compare Rectangles | [8-rectangle.py](8-rectangle.py) |
| 9 | A Square is a Rectangle | [9-rectangle.py](9-rectangle.py) |
| 10 | N Queens | [101-nqueens.py](101-nqueens.py) |

## Environment

-  Ubuntu 20.04 LTS
- python3 (version 3.8.5)

## Requirements

- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc

## Learning Objectives

- Why Python programming is awesome
- What is OOP
- “first-class everything”
- What is a class
- What is an object and an instance
- What is the difference between a class and an object or instance
- What is an attribute
- What are and how to use public, protected and private attributes
- What is self
- What is a method
- What is the special __init__ method and how to use it
- What is Data Abstraction, Data Encapsulation, and Information Hiding
- What is a property
- What is the difference between an attribute and a property in Python
- What is the Pythonic way to write getters and setters in Python
- What are the special __str__ and __repr__ methods and how to use them
- What is the difference between __str__ and __repr__
- What is a class attribute
- What is the difference between a object attribute and a class attribute
- What is a class method
- What is a static method
- How to dynamically create arbitrary new attributes for existing instances of a class
- How to bind attributes to object and classes
- What is and what does contain __dict__ of a class and of an instance of a class
- How does Python find the attributes of an object or class
- How to use the getattr function

## Prototype Table

| Function | Parameters | Returns | Description |
|----------|------------|---------|-------------|
| `__init__` | `width=0`, `height=0` | None | Initializes a rectangle instance. |
| `area` | None | Area of the rectangle | Calculates the area. |
| `perimeter` | None | Perimeter of the rectangle | Calculates the perimeter. |
| `__str__` | None | String representation | Returns a string for printing. |
| `__repr__` | None | Evaluatable string | Returns a string for eval(). |
| `__del__` | None | None | Prints a deletion message. |
| `bigger_or_equal` | `rect_1`, `rect_2` | Larger rectangle | Compares two rectangles. |
| `square` | `size=0` | New Rectangle | Creates a square instance. |

## How to Use

1. Clone the repository.
2. Navigate to the task directory.
3. Run the Python scripts to see the functionality.

## Usage

To use the classes, create instances and call the methods as demonstrated in the respective task examples.

## Tasks

## Task 0: My First Rectangle

Create a class `Rectangle` that defines a rectangle.

## Task 1: Rectangle

Write a class `Rectangle` that defines a rectangle by:

- Private instance attribute: `width`
- Property `def width(self)` to retrieve it
- Property setter `def width(self, value)` to set it:
  - Width must be an integer, otherwise raise a TypeError exception with the message "width must be an integer"
  - If width is less than 0, raise a ValueError exception with the message "width must be >= 0"
  
- Private instance attribute: `height`
- Property `def height(self)` to retrieve it
- Property setter `def height(self, value)` to set it:
  - Height must be an integer, otherwise raise a TypeError exception with the message "height must be an integer"
  - If height is less than 0, raise a ValueError exception with the message "height must be >= 0"
  
- Instantiation with optional width and height: `def __init__(self, width=0, height=0)`

## Task 2: Area and Perimeter

Write a class `Rectangle` that defines a rectangle by (based on 1-rectangle.py):

- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
  - If width or height is equal to 0, perimeter has to be equal to 0

## Task 3: String Representation

Write a class `Rectangle` that defines a rectangle by (based on 2-rectangle.py):

- Print and `str()` should print the rectangle with the character `#`:
  - If width or height is equal to 0, return an empty string

## Task 4: Eval String Representation

Write a class `Rectangle` that defines a rectangle by (based on 3-rectangle.py):

- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`

## Task 5: Detect Instance Deletion

Write a class `Rectangle` that defines a rectangle by (based on 4-rectangle.py):

- Print the message "Bye rectangle..." (... being 3 dots not ellipsis) when an instance of Rectangle is deleted

## Task 6: How Many Instances

Write a class `Rectangle` that defines a rectangle by (based on 5-rectangle.py):

- Public class attribute `number_of_instances`:
  - Initialized to 0
  - Incremented during each new instance instantiation
  - Decremented during each instance deletion

## Task 7: Change Representation

Write a class `Rectangle` that defines a rectangle by (based on 6-rectangle.py):

- Public class attribute `print_symbol`:
  - Initialized to `#`
  - Used as a symbol for string representation
  - Can be any type

## Task 8: Compare Rectangles

Write a class `Rectangle` that defines a rectangle by (based on 7-rectangle.py):

- Static method `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area

## Task 9: A Square is a Rectangle

Write a class `Rectangle` that defines a rectangle by (based on 8-rectangle.py):

- Class method `def square(cls, size=0):` that returns a new Rectangle instance with width == height == size

## Task 10: N Queens

The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.

- Usage: `nqueens N`
- If the user called the program with the wrong number of arguments, print "Usage: nqueens N", followed by a new line, and exit with the status 1
- Where N must be an integer greater or equal to 4
- If N is not an integer, print "N must be a number", followed by a new line, and exit with the status 1
- If N is smaller than 4, print "N must be at least 4", followed by a new line, and exit with the status 1
- The program should print every possible solution to the problem
- One solution per line
- Format: see example

## Additional Notes

1. **Object-Oriented Programming (OOP)**:
   - A programming paradigm based on the concept of "objects," which can contain data and code.

2. **Classes and Objects**:
   - A **class** is a blueprint for creating objects. An **object** (or instance) is a specific realization of a class.
   - Example: `class Dog:` defines the Dog class, while `my_dog = Dog()` creates an instance of that class.

3. **Attributes**:
   - Variables that belong to a class or an object.
   - **Class attributes** are shared among all instances, while **instance attributes** are unique to each instance.

4. **Methods**:
   - Functions defined within a class that operate on instances of the class.
   - The first parameter is typically `self`, which refers to the instance itself.

5. **Special Methods**:
   - `__init__`: The constructor method that initializes an instance.
   - `__str__` and `__repr__`: Methods that define string representations of the object.

6. **Data Encapsulation**:
   - Restricting access to certain attributes to prevent unintended interference and misuse.
   - Use of public, protected, and private attributes (e.g., `_protected`, `__private`).

7. **Properties**:
   - Use properties to manage access to attributes, allowing you to use getter/setter logic while keeping the attribute access syntax clean.

8. **Class and Static Methods**:
   - `@classmethod`: Receives the class as its first argument, allowing access to class attributes.
   - `@staticmethod`: Does not take a class or instance as a parameter, acting like a regular function.

9. **Dynamic Attributes**:
   - You can add attributes to instances dynamically by simply assigning a value (e.g., `instance.new_attribute = value`).

10. **`__dict__`**:
    - A dictionary representation of an object's attributes and their values.
