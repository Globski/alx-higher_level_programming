# Alx Higher Level Programming - Python Everything is object

## Description
This project aims to improve your understanding of Python's object references, memory management, and the distinction between mutable and immutable types through a series of coding challenges. It explores fundamental concepts of Python's object-oriented programming paradigm, focusing on the nature of objects, variable references, and the implications of mutability and immutability. The goal is to deepen your understanding of how Python manages different types of objects.

## Project Structure

| Task Number | Description | Source Code |
|-------------|-------------|-------------|
| 0           | Who am I? | [File](path/to/your/file0.py) |
| 1           | Where are you? | [File](path/to/your/file1.py) |
| 2           | Right count | [File](path/to/your/file2.py) |
| 3           | Right count = | [File](path/to/your/file3.py) |
| 4           | Right count = | [File](path/to/your/file4.py) |
| 5           | Right count =+ | [File](path/to/your/file5.py) |
| 6           | Is equal | [File](path/to/your/file6.py) |
| 7           | Is the same | [File](path/to/your/file7.py) |
| 8           | Is really equal | [File](path/to/your/file8.py) |
| 9           | Is really the same | [File](path/to/your/file9.py) |
| 10          | And with a list, is it equal | [File](path/to/your/file10.py) |
| 11          | And with a list, is it the same | [File](path/to/your/file11.py) |
| 12          | And with a list, is it really equal | [File](path/to/your/file12.py) |
| 13          | And with a list, is it really the same | [File](path/to/your/file13.py) |
| 14          | List append | [File](path/to/your/file14.py) |
| 15          | List add | [File](path/to/your/file15.py) |
| 16          | Integer incrementation | [File](path/to/your/file16.py) |
| 17          | List incrementation | [File](path/to/your/file17.py) |
| 18          | List assignation | [File](path/to/your/file18.py) |
| 19          | Copy a list object | [File](path/to/your/file19.py) |
| 20          | Tuple or not? | [File](path/to/your/file20.py) |
| 21          | Tuple or not? | [File](path/to/your/file21.py) |
| 22          | Tuple or not? | [File](path/to/your/file22.py) |
| 23          | Tuple or not? | [File](path/to/your/file23.py) |
| 24          | Who I am? | [File](path/to/your/file24.py) |
| 25          | Tuple or not | [File](path/to/your/file25.py) |
| 26          | Empty is not empty | [File](path/to/your/file26.py) |
| 27          | Still the same? | [File](path/to/your/file27.py) |
| 28          | Same or not? | [File](path/to/your/file28.py) |
| 29          | #pythonic | [File](path/to/your/file29.py) |
| 30          | Low memory cost | [File](path/to/your/file30.py) |
| 31          | int 1/3 | [File](path/to/your/file31.py) |
| 32          | int 2/3 | [File](path/to/your/file32.py) |
| 33          | int 3/3 | [File](path/to/your/file33.py) |
| 34          | Clear strings | [File](path/to/your/file34.py) |

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

20. Tuple or not?  
a = ()  
Is a a tuple? Answer with Yes or No.

21. Tuple or not?  
a = (1, 2)  
Is a a tuple? Answer with Yes or No.

22. Tuple or not?  
a = (1)  
Is a a tuple? Answer with Yes or No.

23. Tuple or not?  
a = (1, )  
Is a a tuple? Answer with Yes or No.

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

30. Low memory cost  
Write a class `LockedClass` with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called `first_name`.

31. int 1/3  
How many int objects are created by the execution of the first line of the script? (103-line1.txt)  
How many int objects are created by the execution of the second line of the script (103-line2.txt).

32. int 2/3  
How many int objects are created by the execution of the first line of the script? (104-line1.txt)  
How many int objects are created by the execution of the second line of the script (104-line2.txt)  
After the execution of line 3, is the int object pointed by a deleted? Answer with Yes or No (104-line3.txt)  
After the execution of line 4, is the int object pointed by b deleted? Answer with Yes or No (104-line4.txt)  
How many int objects are created by the execution of the last line of the script (104-line5.txt).

33. int 3/3  
Before the execution of line 2 (print("Love")), how many int objects have been created and are still in memory? (105-line1.txt)  
Why? (optional blog post:).

34. Clear strings  
How many string objects are created by the execution of the first line of the script? (106-line1.txt)  
How many string objects are created by the execution of the second line of the script (106-line2.txt)  
After the execution of line 3, is the string object pointed by a deleted? Answer with Yes or No (106-line3.txt)  
After the execution of line 4, is the string object pointed by b deleted? Answer with Yes or No (106-line4.txt)  
How many string objects are created by the execution of the last line of the script (106-line5.txt).
