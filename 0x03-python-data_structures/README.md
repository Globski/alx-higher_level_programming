# High-Level Programming - Python Data Structures: Lists, Tuples

## Description

This project involves solving various tasks related to Python data structures, specifically lists and tuples. The goal is to practice and implement different functions that manipulate these data structures, such as creating and manipulating lists, using common list methods, creating and unpacking tuples, applying sequence concepts in Python, and using the del statement to manage and manipulate these data structures effectively. The tasks include printing elements, replacing elements, checking for palindromes in linked lists, and more. The tasks range from simple list manipulations to more complex 

## Project Structure

| Task | Description | Source Code |
|------|-------------|-------------|
| 0. Print a list of integers | Write a function that prints all integers of a list. **Prototype:** def print_list_integer(my_list=[]) **Format:** one integer per line. **Restrictions:** You are not allowed to import any module. Use str.format() to print integers. | [0-print_list_integer.py](0-print_list_integer.py) |
| 1. Secure access to an element in a list | Write a function that retrieves an element from a list like in C. **Prototype:** def element_at(my_list, idx) **Restrictions:** If idx is negative or out of range, return None. No imports or try/except. | [1-element_at.py](1-element_at.py) |
| 2. Replace element | Write a function that replaces an element in a list at a specific position. **Prototype:** def replace_in_list(my_list, idx, element) **Restrictions:** If idx is negative or out of range, return the original list. No imports or try/except. | [2-replace_in_list.py](2-replace_in_list.py) |
| 3. Print a list of integers... in reverse! | Write a function that prints all integers of a list, in reverse order. **Prototype:** def print_reversed_list_integer(my_list=[]) **Format:** one integer per line. **Restrictions:** No imports. Use str.format() to print integers. | [3-print_reversed_list_integer.py](3-print_reversed_list_integer.py) |
| 4. Replace in a copy | Write a function that replaces an element in a list at a specific position without modifying the original list. **Prototype:** def new_in_list(my_list, idx, element) **Restrictions:** If idx is negative or out of range, return a copy of the original list. No imports or try/except. | [4-new_in_list.py](4-new_in_list.py) |
| 5. Can you C me now? | Write a function that removes all characters c and C from a string. **Prototype:** def no_c(my_string) **Restrictions:** The function should return the new string. No imports or str.replace(). | [5-no_c.py](5-no_c.py) |
| 6. Lists of lists = Matrix | Write a function that prints a matrix of integers. **Prototype:** def print_matrix_integer(matrix=[[]]) **Format:** see example. **Restrictions:** No imports. Use str.format() to print integers. | [6-print_matrix_integer.py](6-print_matrix_integer.py) |
| 7. Tuples addition | Write a function that adds 2 tuples. **Prototype:** def add_tuple(tuple_a=(), tuple_b=()) **Restrictions:** Returns a tuple with 2 integers: addition of the first and second elements of each tuple. Handle tuples smaller or larger than 2 elements. No imports. | [7-add_tuple.py](7-add_tuple.py) |
| 8. More returns! | Write a function that returns a tuple with the length of a string and its first character. **Prototype:** def multiple_returns(sentence) **Restrictions:** If the sentence is empty, return None for the first character. | [8-multiple_returns.py](8-multiple_returns.py) |
| 9. Find the max | Write a function that finds the biggest integer of a list. **Prototype:** def max_integer(my_list=[]) **Restrictions:** If the list is empty, return None. No imports or max(). | [9-max_integer.py](9-max_integer.py) |
| 10. Only by 2 | Write a function that finds all multiples of 2 in a list. **Prototype:** def divisible_by_2(my_list=[]) **Restrictions:** Return a list of True or False for multiples of 2. No imports. | [10-divisible_by_2.py](10-divisible_by_2.py) |
| 11. Delete at | Write a function that deletes the item at a specific position in a list. **Prototype:** def delete_at(my_list=[], idx=0) **Restrictions:** If idx is negative or out of range, return the same list. No imports or pop(). | [11-delete_at.py](11-delete_at.py) |
| 12. Switch | Complete the source code to switch the value of a and b. **Note:** Your program should be exactly 5 lines long. | [12-switch.py](12-switch.py) |
| 13. Linked list palindrome | Write a function in C that checks if a singly linked list is a palindrome. **Prototype:** int is_palindrome(listint_t **head) **Return:** 0 if not a palindrome, 1 if it is. An empty list is considered a palindrome. | [13-is_palindrome.c](13-is_palindrome.c) |
| 14. CPython #0: Python lists | Create a C function that prints basic info about Python lists. **Prototype:** void print_python_list_info(PyObject *p) **Note:** Python version 3.4. Your shared library will be compiled with gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c. | [100-print_python_list_info.c](100-print_python_list_info.c) |

## Learning Objectives
- Why Python programming is awesome
- What are lists and how to use them
- What are the differences and similarities between strings and lists
- What are the most common methods of lists and how to use them
- How to use lists as stacks and queues
- What are list comprehensions and how to use them
- What are tuples and how to use them
- When to use tuples versus lists
- What is a sequence
- What is tuple packing
- What is sequence unpacking
- What is the del statement and how to use it

## Environment
- **Python Version:** Python 3.x
- **C Compiler:** GCC
- **OS:** Ubuntu 14.04 LTS or equivalent for C tasks

### Requirements
**Python Scripts**:
- The first line of all your files should be exactly #!/usr/bin/python3
- For Python tasks, your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- No module imports for Python tasks (except built-ins like str methods).
- No use of try/except for error handling.

**C**:
- For C tasks, proper use of GCC to compile the shared libraries.
- Your shared library will be compiled with this command line: gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c  
- Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
- You are not allowed to use global variables
- No more than 5 functions per file
- The prototypes of all your functions should be included in your header file called lists.h
- All your header files should be include guarded

### How to Use
1. **Clone the Repository:** Ensure you have the source code files locally.
2. **Run the Code:** Execute the Python files to test the functions or compile the C files using the provided commands.
3. **Testing:** Use the corresponding main files to run and test the tasks.







# Tasks

### **0. Print a List of Integers**
- **Prototype:** def print_list_integer(my_list=[]):
- **Description:** Prints all integers in a list, one per line.
- **Requirements:** Use str.format() for printing; no imports or casting.

**File:** 0-print_list_integer.py  
**Test file:** 0-main.py

### **1. Secure Access to an Element in a List**
- **Prototype:** def element_at(my_list, idx):
- **Description:** Retrieves an element from a list at a specified position, handling out-of-range and negative indices by returning None.
- **Requirements:** No imports or try/except.

**File:** 1-element_at.py  
**Test file:** 1-main.py  

### **2. Replace Element**
- **Prototype:** def replace_in_list(my_list, idx, element):
- **Description:** Replaces an element in a list at a specific index, handling negative or out-of-range indices by returning the original list.
- **Requirements:** No imports or try/except.

**File:** 2-replace_in_list.py  
**Test file:** 2-main.py

### **3. Print a List of Integers in Reverse**
- **Prototype:** def print_reversed_list_integer(my_list=[]):
- **Description:** Prints all integers in a list in reverse order, one per line.
- **Requirements:** Use str.format() for printing; no imports or casting.

**File:** 3-print_reversed_list_integer.py  
**Test file:** 3-main.py 

### **4. Replace in a Copy**
- **Prototype:** def new_in_list(my_list, idx, element):
- **Description:** Creates a new list with an element replaced at a specific position without modifying the original list.
- **Requirements:** No imports or try/except.

**File:** 4-new_in_list.py  
**Test file:** 4-main.py  

### **5. Can You C Me Now?**
- **Prototype:** def no_c(my_string):
- **Description:** Removes all occurrences of characters 'c' and 'C' from a string.
- **Requirements:** No imports or str.replace().

**File:** 5-no_c.py  
**Test file:** 5-main.py

### **6. Lists of Lists = Matrix**
- **Prototype:** def print_matrix_integer(matrix=[[]]):
- **Description:** Prints a matrix of integers in a formatted style.
- **Requirements:** Use str.format() for printing; no imports or casting.

**File:** 6-print_matrix_integer.py  
**Test file:** 6-main.py  

### **7. Tuples Addition**
- **Prototype:** def add_tuple(tuple_a=(), tuple_b=()):
- **Description:** Adds two tuples element-wise. If a tuple has fewer than 2 elements, use 0 for missing values. Only consider the first two elements of each tuple.
- **Requirements:** No imports.

**File:** 7-add_tuple.py  
**Test file:** 7-main.py  

### **8. More Returns!**
- **Prototype:** def multiple_returns(sentence):
- **Description:** Returns a tuple containing the length of a string and its first character. If the string is empty, the first character should be None.
- **Requirements:** No imports.

**File:** 8-multiple_returns.py  
**Test file:** 8-main.py  

### **9. Find the Max**
- **Prototype:** def max_integer(my_list=[]):
- **Description:** Finds the largest integer in a list.
- **Requirements:** Handle an empty list by returning None; no use of max().

**File:** 9-max_integer.py  
**Test file:** 9-main.py  

### **10. Only by 2**
- **Prototype:** def divisible_by_2(my_list=[]):
- **Description:** Returns a new list indicating whether each element in the original list is divisible by 2.
- **Requirements:** No imports.

**File:** 10-divisible_by_2.py  
**Test file:** 10-main.py  

### **11. Delete at**
- **Prototype:** def delete_at(my_list=[], idx=0):
- **Description:** Deletes the item at a specific index from a list, handling negative or out-of-range indices by returning the same list.
- **Requirements:** No use of pop().

**File:** 11-delete_at.py  
**Test file:** 11-main.py

### **12. Switch**
- **Description:** Switches the values of two variables a and b.
- **Requirements:** Insert code at the specified location in a given script; the solution must be exactly 5 lines long.

**File:** 12-switch.py  

### **13. Linked List Palindrome**
- **Prototype:** int is_palindrome(listint_t **head);
- **Description:** Checks if a singly linked list is a palindrome.
- **Requirements:** Implement in C.
- 
**File:** 13-is_palindrome.c  
**Test file:** 13-main.c  
**Header:** lists.h

### **14. CPython #0: Python Lists**
- **Prototype:** void print_python_list_info(PyObject *p);
- **Description:** Prints basic information about Python lists in C.
- **Requirements:** Implement as a shared library; use provided compilation command.

**File:** 100-print_python_list_info.c
