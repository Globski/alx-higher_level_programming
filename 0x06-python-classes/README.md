# Alx Higher Level Programming - Python Classes and Objects

## Description

This project emphasizes Object-Oriented Programming (OOP) concepts in Python. You'll learn how to create and manage classes and instances, encapsulate data, and implement attributes and methods. The project includes a **Square** class for modeling squares and a **Node** class for a singly linked list. These examples effectively demonstrate key OOP principles, helping you understand how to apply OOP in Python.

## Project Structure

| Task Number | Description                                                                                   | Source Code               |
|-------------|-----------------------------------------------------------------------------------------------|---------------------------|
| 0           | Write an empty class `Square` that defines a square.                                        | [0-square.py](0-square.py) |
| 1           | Write a class `Square` that defines a square by: Private instance attribute: `size`.       | [1-square.py](1-square.py) |
| 2           | Write a class `Square` that validates size and raises exceptions for invalid values.        | [2-square.py](2-square.py) |
| 3           | Write a class `Square` that returns the area of the square.                                 | [3-square.py](3-square.py) |
| 4           | Write a class `Square` with properties for `size` and methods to validate and retrieve it. | [4-square.py](4-square.py) |
| 5           | Write a class `Square` that prints the square using `#` characters.                        | [5-square.py](5-square.py) |
| 6           | Write a class `Square` that includes position attributes for printing.                      | [6-square.py](6-square.py) |
| 7           | Write a class `Node` and `SinglyLinkedList` for a basic linked list implementation.        | [100-singly_linked_list.py](100-singly_linked_list.py) |
| 8           | Write a class `Square` that implements printing functionality via a custom method.         | [101-square.py](101-square.py) |
| 9           | Write a class `Square` that allows for comparisons based on area.                          | [102-square.py](102-square.py) |
| 10          | Write a class `MagicClass` that emulates a certain functionality as shown in bytecode.    | [103-magic_class.py](103-magic_class.py) |

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

## Additional Notes 

- **Why Python programming is awesome**: Python is loved for its simplicity, readability, and versatility, making it suitable for beginners and experts alike.

- **What is OOP**: Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes to structure code, enabling better organization and reusability.

- **“First-class everything”**: This principle means that in Python, functions and objects can be passed around as values, allowing for flexible and dynamic programming.

- **What is a class**: A class is a blueprint for creating objects that defines attributes and methods, encapsulating related data and behavior.

- **What is an object and an instance**: An object is a specific realization of a class, while an instance refers to the created object that belongs to a particular class.

- **Difference between a class and an object/instance**: A class is a template for creating objects, whereas an object (or instance) is a concrete representation of that class with its own unique data.

- **What is an attribute**: An attribute is a variable that belongs to an object or class, representing data associated with that object or class.

- **Public, protected, and private attributes**: 
  - **Public attributes** are accessible from outside the class.
  - **Protected attributes** are intended for internal use and should not be accessed from outside the class hierarchy.
  - **Private attributes** are prefixed with double underscores and are not accessible outside the class.

- **What is self**: `self` is a reference to the current instance of a class, allowing access to its attributes and methods.

- **What is a method**: A method is a function defined within a class that operates on the instance of that class.

- **What is the special `__init__` method and how to use it**: The `__init__` method is a constructor that initializes a new object’s attributes when it is created.

- **Data Abstraction, Data Encapsulation, and Information Hiding**:
  - **Data Abstraction** refers to hiding complex implementation details and showing only the essential features of an object.
  - **Data Encapsulation** involves bundling data and methods that operate on that data within a class.
  - **Information Hiding** prevents access to certain details of an object to protect its integrity.

- **What is a property**: A property is a special kind of attribute that allows you to customize access to an instance variable using getter and setter methods.

- **Difference between an attribute and a property in Python**: An attribute is a direct variable associated with an object, while a property uses methods to get or set the value of an attribute.

- **Pythonic way to write getters and setters**: Use the `@property` decorator for getters and `@<property_name>.setter` for setters, providing a clean interface for attribute access.

- **How to dynamically create arbitrary new attributes for existing instances of a class**: You can assign new attributes to an instance by directly setting them using dot notation, like `instance.new_attr = value`.

- **How to bind attributes to objects and classes**: You can bind attributes to objects using dot notation and to classes by defining them within the class body.

- **What is the `__dict__` of a class and/or instance**: The `__dict__` attribute is a dictionary that contains all the attributes (and their values) for a class or instance.

- **How does Python find the attributes of an object or class**: Python searches for attributes in the object's `__dict__` first, then in its class, and continues up the inheritance hierarchy if not found.

- **How to use the `getattr` function**: The `getattr` function retrieves an attribute from an object by name, allowing you to access attributes dynamically.

## Tasks

### 0. My First Square

Write an empty class `Square` that defines a square:

You are not allowed to import any module.

```python
guillaume@ubuntu:~/0x06$ cat 0-main.py
#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)

guillaume@ubuntu:~/0x06$ ./0-main.py
<class '0-square.Square'>
{}
guillaume@ubuntu:~/0x06$ 
```

### 1. Square with Size

Write a class `Square` that defines a square by: (based on 0-square.py)

Private instance attribute: `size`  
Instantiation with `size` (no type/value verification)  
You are not allowed to import any module.
Why?

Why size is private attribute?

The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. One way to have the control is to keep it privately. You will see in next tasks how to get, update and validate the size value.

```javascript
guillaume@ubuntu:~/0x06$ cat 1-main.py
#!/usr/bin/python3
Square = __import__('1-square').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)

guillaume@ubuntu:~/0x06$ ./1-main.py
<class '1-square.Square'>
{'_Square__size': 3}
'Square' object has no attribute 'size'
'Square' object has no attri
```
### 2. Size Validation

Write a class `Square` that defines a square by: (based on 1-square.py)

Private instance attribute: `size`  
Instantiation with optional size: `def __init__(self, size=0):`  
`size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`.  
If `size` is less than 0, raise a `ValueError` exception with the message `size must be >= 0`.  
You are not allowed to import any module.
```javascript
guillaume@ubuntu:~/0x06$ cat 2-main.py
#!/usr/bin/python3
Square = __import__('2-square').Square

my_square_1 = Square(3)
print(type(my_square_1))
print(my_square_1.__dict__)

my_square_2 = Square()
print(type(my_square_2))
print(my_square_2.__dict__)

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

try:
    my_square_3 = Square("3")
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)

try:
    my_square_4 = Square(-89)
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)

guillaume@ubuntu:~/0x06$ ./2-main.py
<class '2-square.Square'>
{'_Square__size': 3}
<class '2-square.Square'>
{'_Square__size': 0}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
size must be an integer
size must be >= 0
guillaume@ubuntu:~/0x06$ 
```
### 3. Area of a Square

Write a class `Square` that defines a square by: (based on 2-square.py)

Private instance attribute: `size`  
Instantiation with optional size: `def __init__(self, size=0):`  
`size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`.  
If `size` is less than 0, raise a `ValueError` exception with the message `size must be >= 0`.  
Public instance method: `def area(self):` that returns the current square area.  
You are not allowed to import any module.
```javascript
guillaume@ubuntu:~/0x06$ cat 3-main.py
#!/usr/bin/python3
Square = __import__('3-square').Square

my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))

guillaume@ubuntu:~/0x06$ ./3-main.py
Area: 9
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
Area: 25
guillaume@ubuntu:~/0x06$
```
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

Why?

Why a getter and setter?

Reminder: size is a private attribute. We did that to make sure we control the type and value. Getter and setter methods are not 100% Python, but more OOP. With them, you will be able to validate the assignment of a private attribute and also define how getting the attribute value will be available from outside - by copy? by assignment? etc. Also, adding type/value validation in the setter will centralize the logic, since you will do it in only one place.

```javascript
guillaume@ubuntu:~/0x06$ cat 4-main.py
#!/usr/bin/python3
Square = __import__('4-square').Square

my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)

guillaume@ubuntu:~/0x06$ ./4-main.py
Area: 7921 for size: 89
Area: 9 for size: 3
size must be an integer
guillaume@ubuntu:~/0x06$ 
```
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
```javascript
guillaume@ubuntu:~/0x06$ cat 5-main.py
#!/usr/bin/python3
Square = __import__('5-square').Square

my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")

guillaume@ubuntu:~/0x06$ ./5-main.py
###
###
###
--
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
--

--
guillaume@ubuntu:~/0x06$
```
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
```javascript
guillaume@ubuntu:~/0x06$ cat 6-main.py
#!/usr/bin/python3
Square = __import__('6-square').Square

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")

guillaume@ubuntu:~/0x06$ ./6-main.py | tr " " "_" | cat -e
###$
###$
###$
--$
$
_###$
_###$
_###$
--$
___###$
___###$
___###$
--$
guillaume@ubuntu:~/0x06$ 
```
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
```javascript
guillaume@ubuntu:~/0x06$ cat 100-main.py
#!/usr/bin/python3
SinglyLinkedList = __import__('100-singly_linked_list').SinglyLinkedList

sll = SinglyLinkedList()
sll.sorted_insert(2)
sll.sorted_insert(5)
sll.sorted_insert(3)
sll.sorted_insert(10)
sll.sorted_insert(1)
sll.sorted_insert(-4)
sll.sorted_insert(-3)
sll.sorted_insert(4)
sll.sorted_insert(5)
sll.sorted_insert(12)
sll.sorted_insert(3)
print(sll)

guillaume@ubuntu:~/0x06$ ./100-main.py
-4
-3
1
2
3
3
4
5
5
10
12
guillaume@ubuntu:~/0x06$ 
```
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
```javascript
guillaume@ubuntu:~/0x06$ cat 101-main.py
#!/usr/bin/python3
Square = __import__('101-square').Square

my_square = Square(5, (0, 0))
print(my_square)

print("--")

my_square = Square(5, (4, 1))
print(my_square)

guillaume@ubuntu:~/0x06$ ./101-main.py | tr " " "_" | cat -e
#####$
#####$
#####$
#####$
#####$
--$
$
____#####$
____#####$
____#####$
____#####$
____#####$
guillaume@ubuntu:~/0x06$
```
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
```javascript
guillaume@ubuntu:~/0x06$ cat 102-main.py
#!/usr/bin/python3
Square = __import__('102-square').Square

s_5 = Square(5)
s_6 = Square(6)

if s_5 < s_6:
    print("Square 5 < Square 6")
if s_5 <= s_6:
    print("Square 5 <= Square 6")
if s_5 == s_6:
    print("Square 5 == Square 6")
if s_5 != s_6:
    print("Square 5 != Square 6")
if s_5 > s_6:
    print("Square 5 > Square 6")
if s_5 >= s_6:
    print("Square 5 >= Square 6")

guillaume@ubuntu:~/0x06$ ./102-main.py
Square 5 < Square 6
Square 5 <= Square 6
Square 5 != Square 6
guillaume@ubuntu:~/0x06$ 
```
### 10. ByteCode -> Python #5

Write the Python class `MagicClass` that does exactly the same as the following Python bytecode:

Disassembly of `__init__`:
[Tip: Python bytecode](https://docs.python.org/3.4/library/dis.html)
```
 Disassembly of __init__:
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
             36 LOAD_GLOBAL              3 (float)
             39 COMPARE_OP               9 (is not)
             42 POP_JUMP_IF_FALSE       60

 12          45 LOAD_GLOBAL              4 (TypeError)
             48 LOAD_CONST               2 ('radius must be a number')
             51 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             54 RAISE_VARARGS            1
             57 JUMP_FORWARD             0 (to 60)

 13     >>   60 LOAD_FAST                1 (radius)
             63 LOAD_FAST                0 (self)
             66 STORE_ATTR               0 (_MagicClass__radius)
             69 LOAD_CONST               3 (None)
             72 RETURN_VALUE

Disassembly of area:
 17           0 LOAD_FAST                0 (self)
              3 LOAD_ATTR                0 (_MagicClass__radius)
              6 LOAD_CONST               1 (2)
              9 BINARY_POWER
             10 LOAD_GLOBAL              1 (math)
             13 LOAD_ATTR                2 (pi)
             16 BINARY_MULTIPLY
             17 RETURN_VALUE

Disassembly of circumference:
 21           0 LOAD_CONST               1 (2)
              3 LOAD_GLOBAL              0 (math)
              6 LOAD_ATTR                1 (pi)
              9 BINARY_MULTIPLY
             10 LOAD_FAST                0 (self)
             13 LOAD_ATTR                2 (_MagicClass__radius)
             16 BINARY_MULTIPLY
             17 RETURN_VALUE
```           
