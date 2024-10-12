# Alx Higher Level Programming - Python Classes and Objects

## Description

This project emphasizes Object-Oriented Programming (OOP) concepts in Python, covering the creation and management of classes and instances, data encapsulation, and the implementation of attributes and methods. It includes a Square class for modeling squares and a Node class for a singly linked list, effectively demonstrating key OOP principles in Python.

## Project Structure

| Task Number | Description                                                                                   | Source Code      |
|-------------|-----------------------------------------------------------------------------------------------|------------------|
| 0           | Write an empty class `Square` that defines a square.                                        | [0-square.py](#) |
| 1           | Write a class `Square` that defines a square by: Private instance attribute: `size`.       | [1-square.py](#) |
| 2           | Write a class `Square` that validates size and raises exceptions for invalid values.        | [2-square.py](#) |
| 3           | Write a class `Square` that returns the area of the square.                                 | [3-square.py](#) |
| 4           | Write a class `Square` with properties for `size` and methods to validate and retrieve it. | [4-square.py](#) |
| 5           | Write a class `Square` that prints the square using `#` characters.                        | [5-square.py](#) |
| 6           | Write a class `Square` that includes position attributes for printing.                      | [6-square.py](#) |
| 7           | Write a class `Node` and `SinglyLinkedList` for a basic linked list implementation.        | [linked_list.py](#) |
| 8           | Write a class `Square` that implements printing functionality via a custom method.         | [6-square.py](#) |
| 9           | Write a class `Square` that allows for comparisons based on area.                          | [4-square.py](#) |
| 10          | Write a class `MagicClass` that emulates a certain functionality as shown in bytecode.    | [magic_class.py](#) |

## Environment
- Ubuntu 20.04 LTS 
- python3 (version 3.8.5)

## Requirements

- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 
'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Learning Objectives

By the end of this project, you should be able to explain:

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
- How to dynamically create arbitrary new attributes for existing instances of a class
- How to bind attributes to object and classes
- What is the __dict__ of a class and/or instance of a class and what does it contain
- How does Python find the attributes of an object or class
- How to use the getattr function

## Prototypes Used in the Project

| Function/Method                | Prototype                             |
|--------------------------------|---------------------------------------|
| `Square.__init__(self, size=0)`| Initializes a Square instance.      |
| `Square.area(self)`            | Returns the area of the square.     |
| `Square.my_print(self)`        | Prints the square using `#`.        |
| `Node.__init__(self, data, next_node=None)` | Initializes a Node instance. |
| `SinglyLinkedList.__init__(self)` | Initializes a singly linked list.  |
| `SinglyLinkedList.sorted_insert(self, value)` | Inserts a value into the list.|

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/alx-higher_level_programming.git
   ```
2. Navigate to the project directory:
   ```bash
   cd 0x06-python-classes
   ```
3. Run the main files to test the implementation.
4. You can instantiate the classes as needed and utilize their methods to perform operations related to squares and linked lists.

## Tasks

### 0. My First Square

Write an empty class `Square` that defines a square:

You are not allowed to import any module.

### 1. Square with Size

Write a class `Square` that defines a square by: (based on 0-square.py)

Private instance attribute: `size`  
Instantiation with `size` (no type/value verification)  
You are not allowed to import any module.

### 2. Size Validation

Write a class `Square` that defines a square by: (based on 1-square.py)

Private instance attribute: `size`  
Instantiation with optional size: `def __init__(self, size=0):`  
`size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`.  
If `size` is less than 0, raise a `ValueError` exception with the message `size must be >= 0`.  
You are not allowed to import any module.

### 3. Area of a Square

Write a class `Square` that defines a square by: (based on 2-square.py)

Private instance attribute: `size`  
Instantiation with optional size: `def __init__(self, size=0):`  
`size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`.  
If `size` is less than 0, raise a `ValueError` exception with the message `size must be >= 0`.  
Public instance method: `def area(self):` that returns the current square area.  
You are not allowed to import any module.

### 4. Access and Update Private Attribute

Write a class `Square` that defines a square by: (based on 3-square.py)

Private instance attribute: `size`  
Property `def size(self):` to retrieve it.  
Property setter `def size(self, value):` to set it:  
`size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`.  
If `size` is less than 0, raise a `ValueError` exception with the message `size must be >= 0`.  
Instantiation with optional size: `def __init__(self, size=0):`  
Public instance method: `def area(self):` that returns the current square area.  
You are not allowed to import any module.

### 5. Printing a Square

Write a class `Square` that defines a square by: (based on 4-square.py)

Private instance attribute: `size`  
Property `def size(self):` to retrieve it.  
Property setter `def size(self, value):` to set it:  
`size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`.  
If `size` is less than 0, raise a `ValueError` exception with the message `size must be >= 0`.  
Instantiation with optional size: `def __init__(self, size=0):`  
Public instance method: `def area(self):` that returns the current square area.  
Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:  
If `size` is equal to 0, print an empty line.  
You are not allowed to import any module.

### 6. Coordinates of a Square

Write a class `Square` that defines a square by: (based on 5-square.py)

Private instance attribute: `size`  
Property `def size(self):` to retrieve it.  
Property setter `def size(self, value):` to set it:  
`size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`.  
If `size` is less than 0, raise a `ValueError` exception with the message `size must be >= 0`.  
Private instance attribute: `position`  
Property `def position(self):` to retrieve it.  
Property setter `def position(self, value):` to set it:  
`position` must be a tuple of 2 positive integers, otherwise raise a `TypeError` exception with the message `position must be a tuple of 2 positive integers`.  
Instantiation with optional size and optional position: `def __init__(self, size=0, position=(0, 0)):`  
Public instance method: `def area(self):` that returns the current square area.  
Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:  
If `size` is equal to 0, print an empty line.  
`position` should be used by using space - Don’t fill lines by spaces when `position[1] > 0`.  
You are not allowed to import any module.

### 7. Singly Linked List

Write a class `Node` that defines a node of a singly linked list by:

Private instance attribute: `data`  
Property `def data(self):` to retrieve it.  
Property setter `def data(self, value):` to set it:  
`data` must be an integer, otherwise raise a `TypeError` exception with the message `data must be an integer`.  
Private instance attribute: `next_node`  
Property `def next_node(self):` to retrieve it.  
Property setter `def next_node(self, value):` to set it:  
`next_node` can be `None` or must be a `Node`, otherwise raise a `TypeError` exception with the message `next_node must be a Node object`.  
Instantiation with data and next_node: `def __init__(self, data, next_node=None):`  

And, write a class `SinglyLinkedList` that defines a singly linked list by:

Private instance attribute: `head` (no setter or getter)  
Simple instantiation: `def __init__(self):`  
Should be printable:  
Print the entire list in stdout, one node number by line.  
Public instance method: `def sorted_insert(self, value):` that inserts a new Node into the correct sorted position in the list (increasing order).  
You are not allowed to import any module.

### 8. Print Square Instance

Write a class `Square` that defines a square by: (based on 6-square.py)

Private instance attribute: `size`  
Property `def size(self):` to retrieve it.  
Property setter `def size(self, value):` to set it:  
`size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`.  
If `size` is less than 0, raise a `ValueError` exception with the message `size must be >= 0`.  
Private instance attribute: `position`  
Property `def position(self):` to retrieve it.  
Property setter `def position(self, value):` to set it:  
`position` must be a tuple of 2 positive integers, otherwise raise a `TypeError` exception with the message `position must be a tuple of 2 positive integers`.  
Instantiation with optional size and optional position: `def __init__(self, size=0, position=(0, 0)):`  
Public instance method: `def area(self):` that returns the current square area.  
Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:  
If `size` is equal to 0, print an empty line.  
Printing a Square instance should have the same behavior as `my_print()`.  
You are not allowed to import any module.

### 9. Compare 2 Squares

Write a class `Square` that defines a square by: (based on 4-square.py)

Private instance attribute: `size`  
Property `def size(self):` to retrieve it.  
Property setter `def size(self, value):` to set it:  
`size` must be a number (float or integer), otherwise raise a `TypeError` exception with the message `size must be a number`.  
If `size` is less than 0, raise a `ValueError` exception with the message `size must be >= 0`.  
Instantiation with size: `def __init__(self, size=0):`  
Public instance method: `def area(self):` that returns the current square area.  
Square instance can answer to comparators: `==`, `!=`, `>`, `>=`, `<`, and `<=` based on the square area.  
You are not allowed to import any module.

### 10. ByteCode -> Python #5

Write the Python class `MagicClass` that does exactly the same as the following Python bytecode:

Disassembly of `__init__`:

```
 10           0 LOAD_CONST               1 (0)
              3 LOAD_FAST                0 (self)
              6 STORE_ATTR               0 (_MagicClass__radius)

 11           9 LOAD_GLOBAL              1 (type)
             12 LOAD_FAST                1 (radius)
             15 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             18 LOAD_GLOBAL              2 (int)
             21 COMPARE_OP               9 (is not)
             24 POP_JUMP_IF_FALSE       60
             27 LOAD_GLOBAL              1 (type)
             30 LOAD_FAST                1 (radius)
             33 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
```           
