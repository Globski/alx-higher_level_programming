# Alx Higher Level Programming - Python More Classes and Objects

## Description

This project contains tasks designed to deepen your understanding of object-oriented programming (OOP) in Python. You'll focus on key topics such as class definitions, instance management, and special methods. Through these tasks, you'll gain practical experience in applying OOP concepts, which will enhance your programming skills.

## Project Structure

| Task | Description | Source Code |
|------|-------------|-------------|
| 0. Simple rectangle | Create a simple rectangle class. | [0-rectangle.py](0-rectangle.py) |
| 1. Real definition of a rectangle | Define a rectangle with width and height properties. | [1-rectangle.py](1-rectangle.py) |
| 2. Area and Perimeter | Add methods to calculate area and perimeter. | [2-rectangle.py](2-rectangle.py) |
| 3. String representation | Implement string and representation methods for visualizing the rectangle. | [3-rectangle.py](3-rectangle.py) |
| 4. Eval is magic | Add a delete method to print a message upon deletion. | [4-rectangle.py](4-rectangle.py) |
| 5. Detect instance deletion | Included in the previous example. | [4-rectangle.py](4-rectangle.py) |
| 6. How many instances | Count instances created and deleted. | [6-rectangle.py](6-rectangle.py) |
| 7. Change representation | Allow custom symbols for representation. | [7-rectangle.py](7-rectangle.py) |
| 8. Compare rectangles | Implement a method to compare the area of two rectangles. | [8-rectangle.py](8-rectangle.py) |
| 9. A square is a rectangle | Add a class method to create a square instance. | [9-rectangle.py](9-rectangle.py) |
| 10. N queens | Solve the N queens problem using backtracking. | [101-nqueens.py](101-nqueens.py) |

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

- **Why Python programming is awesome**: Python is known for its simplicity, readability, and versatility, making it a great choice for beginners and experienced developers alike.

- **What is OOP**: Object-Oriented Programming (OOP) is a programming paradigm that organizes code into objects and classes, promoting code reuse and modularity.

- **“First-class everything”**: This concept means that functions and objects in Python can be treated as first-class citizens, allowing them to be passed around and manipulated like any other data type.

- **What is a class**: A class is a blueprint for creating objects, defining attributes and methods that describe the object's behavior and characteristics.

- **What is an object and an instance**: An object is a specific realization of a class. An instance refers to the created object that belongs to a particular class.

- **Difference between a class and an object/instance**: A class serves as a template for creating objects, while an object (or instance) is a concrete representation of that class.

- **What is an attribute**: An attribute is a variable associated with an object or class, representing data related to that object or class.

- **Public, protected, and private attributes**:
  - **Public attributes** can be accessed from outside the class.
  - **Protected attributes** are intended for internal use and should not be accessed from outside the class hierarchy.
  - **Private attributes** are prefixed with double underscores and are not accessible outside the class.

- **What is self**: `self` is a reference to the current instance of a class, allowing access to its attributes and methods.

- **What is a method**: A method is a function defined within a class that operates on the instance of that class.

- **What is the special `__init__` method and how to use it**: The `__init__` method is a constructor that initializes a new object's attributes when it is created.

- **What is Data Abstraction, Data Encapsulation, and Information Hiding**:
  - **Data Abstraction** hides complex implementation details while exposing only essential features of an object.
  - **Data Encapsulation** bundles data and methods that operate on that data within a class.
  - **Information Hiding** restricts access to certain details of an object to protect its integrity.

- **What is a property**: A property is a special kind of attribute that allows you to customize access to an instance variable using getter and setter methods.

- **Difference between an attribute and a property in Python**: An attribute is a direct variable associated with an object, while a property uses methods to get or set the value of an attribute.

- **Pythonic way to write getters and setters**: Use the `@property` decorator for getters and the `@<property_name>.setter` decorator for setters to create a clean interface for attribute access.

- **What are the special `__str__` and `__repr__` methods and how to use them**:
  - **`__str__`** provides a readable string representation of an object, typically for end-user display.
  - **`__repr__`** provides an unambiguous string representation of an object, useful for debugging.

- **Difference between `__str__` and `__repr__`**: `__str__` is intended for human-readable output, while `__repr__` is meant for developers and should ideally return a string that can recreate the object.

- **What is a class attribute**: A class attribute is a variable defined within a class that is shared by all instances of that class.

- **Difference between an object attribute and a class attribute**: An object attribute is specific to an instance, while a class attribute is shared across all instances of the class.

- **What is a class method**: A class method is a method that is bound to the class rather than its instance, defined using the `@classmethod` decorator and takes `cls` as its first parameter.

- **What is a static method**: A static method is a method that does not modify class or instance state and is defined using the `@staticmethod` decorator. It behaves like a regular function but belongs to the class's namespace.

- **How to dynamically create arbitrary new attributes for existing instances of a class**: You can create new attributes for an instance by assigning a value to it directly, like `instance.new_attr = value`.

- **How to bind attributes to objects and classes**: Bind attributes to objects using dot notation and to classes by defining them within the class body.

- **What is `__dict__` of a class and of an instance**: The `__dict__` attribute is a dictionary that contains all the attributes (and their values) of a class or instance.

- **How does Python find the attributes of an object or class**: Python searches for attributes in the object's `__dict__` first, then in its class, continuing up the inheritance hierarchy if not found.

- **How to use the `getattr` function**: The `getattr` function retrieves an attribute from an object by name, allowing for dynamic attribute access.

## Tasks

## Task 0: My First Rectangle

Create a class `Rectangle` that defines a rectangle.
- You are not allowed to import any module
```python
guillaume@ubuntu:~/0x08$ cat 0-main.py
#!/usr/bin/python3
Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)

guillaume@ubuntu:~/0x08$ ./0-main.py
<class '0-rectangle.Rectangle'>
{}
guillaume@ubuntu:~/0x08$
```

---

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
```python
guillaume@ubuntu:~/0x08$ cat 1-main.py
#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)

guillaume@ubuntu:~/0x08$ ./1-main.py
{'_Rectangle__height': 4, '_Rectangle__width': 2}
{'_Rectangle__height': 3, '_Rectangle__width': 10}
guillaume@ubuntu:~/0x08$ 
```

---
## Task 2: Area and Perimeter

Write a class `Rectangle` that defines a rectangle by (based on 1-rectangle.py):

- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
  - If width or height is equal to 0, perimeter has to be equal to 0
```python
guillaume@ubuntu:~/0x08$ cat 2-main.py
#!/usr/bin/python3
Rectangle = __import__('2-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

guillaume@ubuntu:~/0x08$ ./2-main.py
Area: 8 - Perimeter: 12
--
Area: 30 - Perimeter: 26
guillaume@ubuntu:~/0x08$ 
```

---
## Task 3: String Representation

Write a class `Rectangle` that defines a rectangle by (based on 2-rectangle.py):

- Print and `str()` should print the rectangle with the character `#`:
  - If width or height is equal to 0, return an empty string
```python
guillaume@ubuntu:~/0x08$ cat 3-main.py
#!/usr/bin/python3
Rectangle = __import__('3-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print(str(my_rectangle))
print(repr(my_rectangle))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle)
print(repr(my_rectangle))

guillaume@ubuntu:~/0x08$ ./3-main.py
Area: 8 - Perimeter: 12
##
##
##
##
<3-rectangle.Rectangle object at 0x7f92a75a2eb8>
--
##########
##########
##########
<3-rectangle.Rectangle object at 0x7f92a75a2eb8>
guillaume@ubuntu:~/0x08$ 
```

---
## Task 4: Eval String Representation

Write a class `Rectangle` that defines a rectangle by (based on 3-rectangle.py):

- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
```python
guillaume@ubuntu:~/0x08$ cat 4-main.py
#!/usr/bin/python3
Rectangle = __import__('4-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(str(my_rectangle))
print("--")
print(my_rectangle)
print("--")
print(repr(my_rectangle))
print("--")
print(hex(id(my_rectangle)))
print("--")

# create new instance based on representation
new_rectangle = eval(repr(my_rectangle))
print(str(new_rectangle))
print("--")
print(new_rectangle)
print("--")
print(repr(new_rectangle))
print("--")
print(hex(id(new_rectangle)))
print("--")

print(new_rectangle is my_rectangle)
print(type(new_rectangle) is type(my_rectangle))

guillaume@ubuntu:~/0x08$ ./4-main.py
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f09ebf7cc88
--
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f09ebf7ccc0
--
False
True
guillaume@ubuntu:~/0x08$ 
```

---
## Task 5: Detect Instance Deletion

Write a class `Rectangle` that defines a rectangle by (based on 4-rectangle.py):

- Print the message "Bye rectangle..." (... being 3 dots not ellipsis) when an instance of Rectangle is deleted
```python
guillaume@ubuntu:~/0x08$ cat 5-main.py
#!/usr/bin/python3
Rectangle = __import__('5-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

del my_rectangle

try:
    print(my_rectangle)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/0x08$ ./5-main.py
Area: 8 - Perimeter: 12
Bye rectangle...
[NameError] name 'my_rectangle' is not defined
guillaume@ubuntu:~/0x08$ 
```

---
## Task 6: How Many Instances

Write a class `Rectangle` that defines a rectangle by (based on 5-rectangle.py):

- Public class attribute `number_of_instances`:
  - Initialized to 0
  - Incremented during each new instance instantiation
  - Decremented during each instance deletion
```python
guillaume@ubuntu:~/0x08$ cat 6-main.py
#!/usr/bin/python3
Rectangle = __import__('6-rectangle').Rectangle

my_rectangle_1 = Rectangle(2, 4)
my_rectangle_2 = Rectangle(2, 4)
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_1
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_2
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))

guillaume@ubuntu:~/0x08$ ./6-main.py
2 instances of Rectangle
Bye rectangle...
1 instances of Rectangle
Bye rectangle...
0 instances of Rectangle
guillaume@ubuntu:~/0x08$ 
```

---
## Task 7: Change Representation

Write a class `Rectangle` that defines a rectangle by (based on 6-rectangle.py):

- Public class attribute `print_symbol`:
  - Initialized to `#`
  - Used as a symbol for string representation
  - Can be any type
```python
guillaume@ubuntu:~/0x08$ cat 7-main.py
#!/usr/bin/python3
Rectangle = __import__('7-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
print(my_rectangle_1)
print("--")
my_rectangle_1.print_symbol = "&"
print(my_rectangle_1)
print("--")

my_rectangle_2 = Rectangle(2, 1)
print(my_rectangle_2)
print("--")
Rectangle.print_symbol = "C"
print(my_rectangle_2)
print("--")

my_rectangle_3 = Rectangle(7, 3)
print(my_rectangle_3)

print("--")

my_rectangle_3.print_symbol = ["C", "is", "fun!"]
print(my_rectangle_3)

print("--")

guillaume@ubuntu:~/0x08$ ./7-main.py
########
########
########
########
--
&&&&&&&&
&&&&&&&&
&&&&&&&&
&&&&&&&&
--
##
--
CC
--
CCCCCCC
CCCCCCC
CCCCCCC
--
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
--
Bye rectangle...
Bye rectangle...
Bye rectangle...
guillaume@ubuntu:~/0x08$
```

---
## Task 8: Compare Rectangles

Write a class `Rectangle` that defines a rectangle by (based on 7-rectangle.py):

- Static method `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area
```python
guillaume@ubuntu:~/0x08$ cat 8-main.py
#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
my_rectangle_2 = Rectangle(2, 3)

if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")


my_rectangle_2.width = 10
my_rectangle_2.height = 5
if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")

guillaume@ubuntu:~/0x08$ ./8-main.py
my_rectangle_1 is bigger or equal to my_rectangle_2
my_rectangle_2 is bigger than my_rectangle_1
Bye rectangle...
Bye rectangle...
guillaume@ubuntu:~/0x08$ 
```

---
## Task 9: A Square is a Rectangle

Write a class `Rectangle` that defines a rectangle by (based on 8-rectangle.py):

- Class method `def square(cls, size=0):` that returns a new Rectangle instance with width == height == size
```python
guillaume@ubuntu:~/0x08$ cat 9-main.py
#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)

guillaume@ubuntu:~/0x08$ ./9-main.py
Area: 25 - Perimeter: 20
#####
#####
#####
#####
#####
Bye rectangle...
guillaume@ubuntu:~/0x08$ 
```

---
## Task 10: N Queens

Chess grandmaster [Judit Polgár](https://en.wikipedia.org/wiki/Judit_Polg%C3%A1r), the strongest female chess player of all time

The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.

- Usage: `nqueens N`
- If the user called the program with the wrong number of arguments, print "Usage: nqueens N", followed by a new line, and exit with the status 1
- Where N must be an integer greater or equal to 4
- If N is not an integer, print "N must be a number", followed by a new line, and exit with the status 1
- If N is smaller than 4, print "N must be at least 4", followed by a new line, and exit with the status 1
- The program should print every possible solution to the problem
- One solution per line
- Format: see example
- You don’t have to print the solutions in a specific order
- You are only allowed to import the sys module
Read: [Queen](https://en.wikipedia.org/wiki/Queen_%28chess%29), [Backtracking](https://en.wikipedia.org/wiki/Backtracking)
```python
julien@ubuntu:~/0x08. N Queens$ ./101-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
julien@ubuntu:~/0x08. N Queens$ ./101-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
julien@ubuntu:~/0x08. N Queens$ 
```
