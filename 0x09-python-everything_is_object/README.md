# Alx Higher Level Programming - Python Everything is object

## Description
This project aims to improve your understanding of fundamental concepts in Python's object-oriented programming paradigm. It will focus on the nature of objects, variable references, and the distinction between mutable and immutable types. Through a series of coding challenges, you will explore how Python manages different types of objects, including the implications of mutability and immutability. This will deepen your understanding of Python's object references and memory management.

## Project Structure

| Task | Description | Source Code |
|------|-------------|-------------|
| 0    | What function would you use to get the type of an object? | [0-answer.txt](./0-answer.txt) |
| 1    | How do you get the variable identifier (memory address)? | [1-answer.txt](./1-answer.txt) |
| 2    | Do `a` and `b` point to the same object? (`a = 89; b = 100`) | [2-answer.txt](./2-answer.txt) |
| 3    | Do `a` and `b` point to the same object? (`a = 89; b = 89`) | [3-answer.txt](./3-answer.txt) |
| 4    | Do `a` and `b` point to the same object? (`a = 89; b = a`) | [4-answer.txt](./4-answer.txt) |
| 5    | Do `a` and `b` point to the same object? (`a = 89; b = a + 1`) | [5-answer.txt](./5-answer.txt) |
| 6    | What do these lines print? (`s1 = "Best School"; s2 = s1; print(s1 == s2)`) | [6-answer.txt](./6-answer.txt) |
| 7    | What do these lines print? (`s1 = "Best"; s2 = s1; print(s1 is s2)`) | [7-answer.txt](./7-answer.txt) |
| 8    | What do these lines print? (`s1 = "Best School"; s2 = "Best School"; print(s1 == s2)`) | [8-answer.txt](./8-answer.txt) |
| 9    | What do these lines print? (`s1 = "Best School"; s2 = "Best School"; print(s1 is s2)`) | [9-answer.txt](./9-answer.txt) |
| 10   | What do these lines print? (`l1 = [1, 2, 3]; l2 = [1, 2, 3]; print(l1 == l2)`) | [10-answer.txt](./10-answer.txt) |
| 11   | What do these lines print? (`l1 = [1, 2, 3]; l2 = [1, 2, 3]; print(l1 is l2)`) | [11-answer.txt](./11-answer.txt) |
| 12   | What do these lines print? (`l1 = [1, 2, 3]; l2 = l1; print(l1 == l2)`) | [12-answer.txt](./12-answer.txt) |
| 13   | What do these lines print? (`l1 = [1, 2, 3]; l2 = l1; print(l1 is l2)`) | [13-answer.txt](./13-answer.txt) |
| 14   | What does this script print? (`l1 = [1, 2, 3]; l2 = l1; l1.append(4); print(l2)`) | [14-answer.txt](./14-answer.txt) |
| 15   | What does this script print? (`l1 = [1, 2, 3]; l2 = l1; l1 = l1 + [4]; print(l2)`) | [15-answer.txt](./15-answer.txt) |
| 16   | What does this script print? (`def increment(n): n += 1; a = 1; increment(a); print(a)`) | [16-answer.txt](./16-answer.txt) |
| 17   | What does this script print? (`def increment(n): n.append(4); l = [1, 2, 3]; increment(l); print(l)`) | [17-answer.txt](./17-answer.txt) |
| 18   | What does this script print? (`def assign_value(n, v): n = v; l1 = [1, 2, 3]; l2 = [4, 5, 6]; assign_value(l1, l2); print(l1)`) | [18-answer.txt](./18-answer.txt) |
| 19   | Write a function `copy_list(l)` that returns a copy of a list. | [19-copy_list.py](./19-copy_list.py) |
| 20   | Is `a = ()` a tuple? | [20-answer.txt](./20-answer.txt) |
| 21   | Is `a = (1, 2)` a tuple? | [21-answer.txt](./21-answer.txt) |
| 22   | Is `a = (1)` a tuple? | [22-answer.txt](./22-answer.txt) |
| 23   | Is `a = (1,)` a tuple? | [23-answer.txt](./23-answer.txt) |
| 24   | What does `a = (1); b = (1); a is b` print? | [24-answer.txt](./24-answer.txt) |
| 25   | What does `a = (1, 2); b = (1, 2); a is b` print? | [25-answer.txt](./25-answer.txt) |
| 26   | What does `a = (); b = (); a is b` print? | [26-answer.txt](./26-answer.txt) |
| 27   | Will `id(a)` remain the same after `a = a + [5]`? | [27-answer.txt](./27-answer.txt) |
| 28   | Will `id(a)` remain the same after `a += [4]`? | [28-answer.txt](./28-answer.txt) |
| 29   | Write a function `magic_string()` that returns "BestSchool" n times the number of the iteration. | [100-magic_string.py](./100-magic_string.py) |
| 30   | Create a class `LockedClass` that only allows the creation of a `first_name` attribute. | [101-locked_class.py](./101-locked_class.py) |
| 31   | How many int objects are created by `a = 1` and `b = 1`? | [103-line1.txt](./103-line1.txt) |
| 32   | Analyze int objects created in a specific sequence. | [104-line1.txt](./104-line1.txt) |
| 33   | Before `print("Love")`, how many int objects are in memory? | [105-line1.txt](./105-line1.txt) |
| 34   | Analyze string objects created in a specific sequence. | [106-line1.txt](./106-line1.txt) |

## Environment

- Ubuntu 20.04 LTS
- python3 (version 3.8.5)
- Any IDE or code editor (e.g., VSCode, PyCharm)

## Requirements

- Python 3.8.5
- All scripts must be executable and adhere to the [pycodestyle](https://pypi.org/project/pycodestyle/) guidelines.
- All scripts must end with a newline character.

#### Python Scripts
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a newline character
- The first line of all your script files should be exactly #!/usr/bin/python3
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc

#### .txt Answer Files
- Only one line
- No Shebang
- All your files should end with a new line

## Learning Objectives

By the end of this project, you should be able to:

- Why Python programming is awesome
- What is an object
- What is the difference between a class and an object or instance
- What is the difference between immutable object and mutable object
- What is a reference
- What is an assignment
- What is an alias
- How to know if two variables are identical
- How to know if two variables are linked to the same object
- How to display the variable identifier (which is the memory address in the CPython implementation)
- What is mutable and immutable
- What are the built-in mutable types
- What are the built-in immutable types
- How does Python pass variables to functions

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/alx-higher_level_programming.git
   cd 0x09-python-everything_is_object
   ```

2. Navigate to the directory of the task you wish to execute and run the Python scripts.

3. Review the corresponding answer files to see the solutions to each task.


## Prototypes Used in the Project

| Prototype Name | Description |
|----------------|-------------|
| magic_string    | Returns a string repeated n times. |
| copy_list       | Returns a copy of a list. |
| LockedClass     | Prevents dynamic creation of attributes. |

## Additional Note

1. **Everything is an Object**: In Python, all data types are objects, which means they have identity, type, and value.
  
2. **Immutable vs Mutable**:
   - **Immutable**: Objects that cannot be changed after creation (e.g., integers, strings, tuples).
   - **Mutable**: Objects that can be modified (e.g., lists, dictionaries, sets).

3. **Reference and Assignment**:
   - Assigning a variable creates a reference to an object, not a copy.
   - Aliasing occurs when two variables refer to the same object.

4. **Memory and Identifiers**: Every object has a unique identifier, which can be accessed using the `id()` function.

5. **Why Python is Awesome**: Emphasizes readability, simplicity, and a vast ecosystem.
  
6. **Object vs Class**: A class is a blueprint; an object is an instance of that class.

7. **References and Aliasing**:
   - To check if two variables are identical, use `a is b`.
   - To see if two variables point to the same object, again use `a is b`.

8. **Memory Management**: Use the `id()` function to display a variable's identifier.

10. **What is an object?**  
   An object is an instance of a class, containing data and methods.

11. **What is the difference between a class and an object?**  
   A class is a blueprint for creating objects; an object is an instantiated class.

12. **What is an immutable object?**  
   An immutable object is one whose state cannot be modified after it is created.

13. **How to check if two variables are linked to the same object?**  
   Use `a is b` to check if both variables reference the same object.

14. **How to display the variable identifier?**  
   Use `id(variable)` to display the memory address of the variable.

### Why Python Programming is Awesome
Python is a versatile and user-friendly programming language known for its simplicity and readability. Its extensive libraries and frameworks facilitate rapid development, making it popular for web development, data analysis, machine learning, and more.

### What is an Object
An object is a fundamental building block in Python that represents data and functionality. It is an instance of a class and contains attributes (data) and methods (functions) that define its behavior.

### What is the Difference Between a Class and an Object (or Instance)
- **Class**: A blueprint for creating objects. It defines attributes and methods that the created objects will have.
- **Object (or Instance)**: A specific realization of a class, created using the class definition. Each object can have unique attribute values.

### What is the Difference Between Immutable and Mutable Objects
- **Immutable Objects**: These cannot be changed after they are created. Examples include integers, strings, and tuples.
- **Mutable Objects**: These can be modified after creation. Examples include lists, dictionaries, and sets.

### What is a Reference
A reference is a pointer or link to an object in memory. When you create a variable in Python, you are creating a reference to an object, not the object itself.

### What is an Assignment
Assignment in Python refers to the process of creating a reference to an object by giving a variable name to it. For example, `x = [1, 2, 3]` assigns the list `[1, 2, 3]` to the variable `x`.

### What is an Alias
An alias is another name or reference to the same object. If two variables reference the same object, they are aliases of each other. For instance, if `y = x`, both `x` and `y` point to the same list.

### How to Know if Two Variables are Identical
You can check if two variables are identical (i.e., they reference the same object) using the `is` operator:
```python
if x is y:
    print("x and y are identical")
```

### How to Know if Two Variables are Linked to the Same Object
Use the `is` operator to determine if two variables point to the same object in memory. If `x is y` returns `True`, they are linked to the same object.

### How to Display the Variable Identifier (Memory Address in CPython)
You can display the memory address of a variable using the `id()` function:
```python
print(id(x))
```

### What is Mutable and Immutable
- **Mutable**: Objects that can be changed without creating a new object.
- **Immutable**: Objects that cannot be changed after they are created, requiring a new object to reflect any changes.

### What are the Built-in Mutable Types
Common built-in mutable types in Python include:
- Lists (`list`)
- Dictionaries (`dict`)
- Sets (`set`)

### What are the Built-in Immutable Types
Common built-in immutable types in Python include:
- Integers (`int`)
- Floats (`float`)
- Strings (`str`)
- Tuples (`tuple`)
- Frozensets (`frozenset`)

### How Does Python Pass Variables to Functions (Brief)
Python uses **pass-by-reference** (or pass-by-object-reference), meaning that when you pass a variable to a function, you are passing a reference to the object. If the object is mutable, changes made to it within the function will affect the original object. If it’s immutable, a new object is created instead of modifying the original.


## Tasks

0. Who am I?  
What function would you use to get the type of an object? Write the name of the function in the file, without ().

1. Where are you?  
How do you get the variable identifier (which is the memory address in the CPython implementation)? Write the name of the function in the file, without ().

2. Right count  
In the following code, do a and b point to the same object? Answer with Yes or No.  
```python
>>> a = 89
>>> b = 100
```

3. Right count =  
In the following code, do a and b point to the same object? Answer with Yes or No.  
```python
>>> a = 89
>>> b = 89
```

4. Right count =  
In the following code, do a and b point to the same object? Answer with Yes or No.  
```python
>>> a = 89
>>> b = a
```

5. Right count =+  
In the following code, do a and b point to the same object? Answer with Yes or No.  
```python
>>> a = 89
>>> b = a + 1
```

6. Is equal  
What do these 3 lines print?  
```python
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
```

7. Is the same  
What do these 3 lines print?  
```python
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
```

8. Is really equal  
What do these 3 lines print?  
```python
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
```

9. Is really the same  
What do these 3 lines print?  
```python
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
```

10. And with a list, is it equal  
What do these 3 lines print?  
```python
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
```

11. And with a list, is it the same  
What do these 3 lines print?  
```python
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
```

12. And with a list, is it really equal  
What do these 3 lines print?  
```python
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```

13. And with a list, is it really the same  
What do these 3 lines print?  
```python
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```

14. List append  
What does this script print?  
```python
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```

15. List add  
What does this script print?  
```python
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```

16. Integer incrementation  
What does this script print?  
```python
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```

17. List incrementation  
What does this script print?  
```python
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```

18. List assignation  
What does this script print?  
```python
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```

19. Copy a list object  
Write a function `def copy_list(l):` that returns a copy of a list. The input list can contain any type of objects. Your file should be maximum 3-line long (no documentation needed).
```
guillaume@ubuntu:~/0x09$ cat 19-main.py
#!/usr/bin/python3
copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

print(my_list)
print(new_list)

print(new_list == my_list)
print(new_list is my_list)

guillaume@ubuntu:~/0x09$ ./19-main.py
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
True
False
guillaume@ubuntu:~/0x09$ wc -l 19-copy_list.py 
3 19-copy_list.py
guillaume@ubuntu:~/0x09$
```

20. Tuple or not?  
a = ()  
Is a a tuple? Answer with Yes or No.

21. Tuple or not?  
a = (1, 2)  
Is a a tuple? Answer with Yes or No.
```
a = (1, 2)
```
22. Tuple or not?  
a = (1)  
Is a a tuple? Answer with Yes or No.
```
a = (1)
```
23. Tuple or not?  
a = (1, )  
Is a a tuple? Answer with Yes or No.
```
a = (1, )
```
24. Who I am?  
What does this script print?  
```python
a = (1)
b = (1)
a is b
```

25. Tuple or not  
What does this script print?  
```python
a = (1, 2)
b = (1, 2)
a is b
```

26. Empty is not empty  
What does this script print?  
```python
a = ()
b = ()
a is b
```

27. Still the same?  
Will the last line of this script print 139926795932424? Answer with Yes or No.  
```python
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
```

28. Same or not?  
Will the last line of this script print 139926795932424? Answer with Yes or No.  
```python
>>> a
[1, 2, 3]
>>> id(a)
139926795932424
>>> a += [4]
>>> id(a)
```

29. #pythonic  
Write a function `magic_string()` that returns a string “BestSchool” n times the number of the iteration (see code). Your file should be maximum 4-line long (no documentation needed).
```

guillaume@ubuntu:~/0x09$ cat 100-main.py
#!/usr/bin/python3
magic_string = __import__('100-magic_string').magic_string

for i in range(10):
    print(magic_string())

guillaume@ubuntu:~/0x09$ ./100-main.py | cat -e
BestSchool$
BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
guillaume@ubuntu:~/0x09$ wc -l 100-magic_string.py 
4 100-magic_string.py
guillaume@ubuntu:~/0x09$ 
```
30. Low memory cost  
Write a class `LockedClass` with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called `first_name`.
```
guillaume@ubuntu:~/0x09$ cat 101-main.py
#!/usr/bin/python3
LockedClass = __import__('101-locked_class').LockedClass

lc = LockedClass()
lc.first_name = "John"
try:
    lc.last_name = "Snow"
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/0x09$ ./101-main.py
[AttributeError] 'LockedClass' object has no attribute 'last_name'
guillaume@ubuntu:~/0x09$
```
31. int 1/3  
How many int objects are created by the execution of the first line of the script? (103-line1.txt)  
How many int objects are created by the execution of the second line of the script (103-line2.txt).
```
julien@ubuntu:/python3$ cat int.py 
a = 1
b = 1
julien@ubuntu:/python3$ 
```
32. int 2/3  
How many int objects are created by the execution of the first line of the script? (104-line1.txt)  
How many int objects are created by the execution of the second line of the script (104-line2.txt)  
After the execution of line 3, is the int object pointed by a deleted? Answer with Yes or No (104-line3.txt)  
After the execution of line 4, is the int object pointed by b deleted? Answer with Yes or No (104-line4.txt)  
How many int objects are created by the execution of the last line of the script (104-line5.txt).
```
julien@ubuntu:/python3$ cat int.py 
a = 1024
b = 1024
del a
del b
c = 1024
julien@ubuntu:/python3$
```
33. int 3/3  
Before the execution of line 2 (print("Love")), how many int objects have been created and are still in memory? (105-line1.txt)  
Why? (optional blog post:).
```
julien@twix:/tmp/so$ cat int.py 
print("I")
print("Love")
print("Python")
julien@ubuntu:/tmp/so$ 
```
34. Clear strings  
How many string objects are created by the execution of the first line of the script? (106-line1.txt)  
How many string objects are created by the execution of the second line of the script (106-line2.txt)  
After the execution of line 3, is the string object pointed by a deleted? Answer with Yes or No (106-line3.txt)  
After the execution of line 4, is the string object pointed by b deleted? Answer with Yes or No (106-line4.txt)  
How many string objects are created by the execution of the last line of the script (106-line5.txt).
```
guillaume@ubuntu:/python3$ cat string.py 
a = "SCHL"
b = "SCHL"
del a
del b
c = "SCHL"
guillaume@ubuntu:/python3$
```
