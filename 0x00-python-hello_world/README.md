# High-Level Programming - Python Hello World

## Description
This project introduces the basics of Python programming, focusing on fundamental concepts such as printing text, using variables and following the PEP8 style guide. The tasks are designed to help you build your skills gradually, starting with running simple Python scripts, manipulating strings, and finally learning how to print formatted output. By working through these tasks, you'll gain a solid foundation in Python programming and understand how to write clean and readable code.

## Project Structure

| Task | Description | Source Code |
|------|-------------|-------------|
| 0. Run Python file | Write a Shell script to run a Python script. | [0-run](./0-run) |
| 1. Run inline | Write a Shell script to run Python code. | [1-run_inline](./1-run_inline) |
| 2. Hello, print | Write a Python script to print a specific string. | [2-print.py](./2-print.py) |
| 3. Print integer | Complete a Python script to print an integer with a specified format. | [3-print_number.py](./3-print_number.py) |
| 4. Print float | Complete a Python script to print a float with a specified format. | [4-print_float.py](./4-print_float.py) |
| 5. Print string | Complete a Python script to print a string multiple times. | [5-print_string.py](./5-print_string.py) |
| 6. Play with strings | Complete a Python script to concatenate strings. | [6-concat.py](./6-concat.py) |
| 7. Copy - Cut - Paste | Complete a Python script to manipulate a string. | [7-edges.py](./7-edges.py) |
| 8. Create a new sentence | Complete a Python script to concatenate parts of a string. | [8-concat_edges.py](./8-concat_edges.py) |
| 9. Easter Egg | Write a Python script to print "The Zen of Python". | [9-easter_egg.py](./9-easter_egg.py) |
| 10. Linked list cycle | Implement a function in C to check if a linked list has a cycle. | [10-check_cycle.c](./10-check_cycle.c), [lists.h](./lists.h) |

## Environment

- Ubuntu 20.04 LTS
- Python 3.8.5.

## Requirements

- All Python scripts are interpreted on Ubuntu 20.04 LTS using Python 3.8.5.
- Shell scripts and C scripts are tested on Ubuntu 20.04 LTS.
- Python scripts should end with a newline and start with `#!/usr/bin/python3`.
- Shell scripts should end with a newline and start with `#!/bin/bash`.
- All files must be executable.
- The length of files is tested using `wc`.
- C scripts are compiled using `gcc` with specific options.

## Coding Style

- Python code follows the PEP8 (PyCode) style guide.
- C code adheres to the Betty style guide.

## Learning Objectives

After completing this project, you should be able to explain:
- The basics of Python programming.
- Why Python is considered awesome.
- Information about Guido van Rossum and the origins of Python.
- The Zen of Python principles.
- How to use the Python interpreter and print text and variables.
- String manipulation using indexing and slicing.
- Official Python coding style (PEP8) and checking code with `pycodestyle`.

## How to Use

### Prerequisites
Before you begin, ensure you have the following installed on your machine:
- Python 3.x (version 3.8.5 recommended)
- Pycodestyle (version 2.8.*)

### Installation
Clone the repository to your local machine:
```bash
git clone https://github.com/yourusername/alx-higher_level_programming.git
```
Navigate to the project directory
```bash
cd alx-higher_level_programming/0x00-python-hello_world
```
Running Python Scripts

To run the Python scripts in this project, follow these steps:
Set the environment variable for the Python file:
```bash
export PYFILE=main.py
```
Execute the run script:
```bash
./0-run
```
This will run the Python script and display the output.

Running Inline Python Code

To run Python code inline, set the environment variable for the Python code:
```bash
export PYCODE='print(f"Best School: {88+10}")'
```
Execute the inline run script:
```bash
./1-run_inline
```
This will run the Python code and display the output.

Ensure that your Python scripts are executable using the following command:

```bash
chmod +x filename.py
```
For code style validation, use Pycodestyle on your Python files:

```bash
pycodestyle filename.py
```

## Additional Notes 

- **The basics of Python programming**: Python is an easy-to-learn, high-level language used for a wide variety of applications, making it a great choice for beginners.
  
- **Why Python is considered awesome**: Python's simplicity, readability, and vast ecosystem of libraries make it powerful for both beginners and experts. It's used in web development, data science, automation, and more.

- **Guido van Rossum and the origins of Python**: Python was created by Guido van Rossum in 1991. His goal was to make a language that emphasized code readability and simplicity.

- **The Zen of Python principles**: This is a set of guiding principles for writing Python code, emphasizing simplicity, readability, and the importance of writing beautiful code. You can access it by typing `import this` in Python.

- **Using the Python interpreter and printing text and variables**: The Python interpreter allows you to run Python code interactively. You can print text and variables using the `print()` function.

- **String manipulation using indexing and slicing**: In Python, you can access parts of a string using indexing (e.g., `string[0]` for the first character) or slicing (e.g., `string[1:3]` for a substring).

- **PEP8 and `pycodestyle`**: PEP8 is the official style guide for Python code. You can use `pycodestyle` to check if your code adheres to PEP8 standards, ensuring it's clean and readable.

## Tasks


0. **Run Python file**  
   Write a Shell script that runs a Python script.  
   The Python file name will be saved in the environment variable `$PYFILE`.
```pyton
 guillaume@ubuntu:~/py/0x00$ cat main.py 
#!/usr/bin/python3
print("Best School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./0-run
Best School
guillaume@ubuntu:~/py/0x00$    
```
---
1. **Run inline**  
   Write a Shell script that runs Python code.  
   The Python code will be saved in the environment variable `$PYCODE`.
```pyton
guillaume@ubuntu:~/py/0x00$ export PYCODE='print(f"Best School: {88+10}")'
guillaume@ubuntu:~/py/0x00$ ./1-run_inline 
Best School: 98
guillaume@ubuntu:~/py/0x00$     
```
---
2. **Hello, print**  
   Write a Python script that prints exactly "Programming is like building a multilingual puzzle", followed by a new line.  
   Use the function `print`.
```pyton
guillaume@ubuntu:~/py/0x00$ ./2-print.py 
"Programming is like building a multilingual puzzle
guillaume@ubuntu:~/py/0x00$     
```
---
3. **Print integer**  
   Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/3-print_number.py) in order to print the integer stored in the variable `number`, followed by "Battery street", followed by a new line.  
   You are not allowed to cast the variable `number` into a string.  
   Your code must be 3 lines long.  
   You have to use f-strings.
```pyton
guillaume@ubuntu:~/py/0x00$ ./3-print_number.py
98 Battery street
guillaume@ubuntu:~/py/0x00$
```
---
4. **Print float**  
   Complete the [source code](https://github.com/alx-tools/0x00.py/blob/master/4-print_float.py) in order to print the float stored in the variable `number` with a precision of 2 digits.  
   You are not allowed to cast `number` to string.  
   You have to use f-strings.
```pyton
guillaume@ubuntu:~/py/0x00$ ./4-print_float.py
Float: 3.14
guillaume@ubuntu:~/py/0x00$      
```
---
5. **Print string**  
   Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/5-print_string.py) in order to print 3 times a string stored in the variable `str`, followed by its first 9 characters.  
   You are not allowed to use any loops or conditional statements.  
   Your program should be a maximum of 5 lines long.
```pyton
guillaume@ubuntu:~/py/0x00$ ./5-print_string.py 
Holberton SchoolHolberton SchoolHolberton School
Holberton
guillaume@ubuntu:~/py/0x00$     
```
---
6. **Play with strings**  
   Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/6-concat.py) to print "Welcome to Holberton School!".  
   You are not allowed to use any loops or conditional statements.  
   You have to use the variables `str1` and `str2` in your new line of code.  
   Your program should be exactly 5 lines long.
```pyton
guillaume@ubuntu:~/py/0x00$ ./6-concat.py
Welcome to Holberton School!
guillaume@ubuntu:~/py/0x00$ wc -l 6-concat.py
5 6-concat.py
guillaume@ubuntu:~/py/0x00$     
```
---
7. **Copy - Cut - Paste**  
   Complete this source code [here](https://github.com/alx-tools/0x00.py/blob/master/7-edges.py).  
   You are not allowed to use any loops or conditional statements.  
   Your program should be exactly 8 lines long.
```pyton
guillaume@ubuntu:~/py/0x00$ ./7-edges.py
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
guillaume@ubuntu:~/py/0x00$ wc -l 7-edges.py
8 7-edges.py
guillaume@ubuntu:~/py/0x00$
```
---
8. **Create a new sentence**  
   Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/8-concat_edges.py) to print "object-oriented programming with Python", followed by a new line.  
   You are not allowed to use any loops or conditional statements.  
   Your program should be exactly 5 lines long.  
   You are not allowed to create new variables.  
   You are not allowed to use string literals.
```pyton
guillaume@ubuntu:~/py/0x00$ ./8-concat_edges.py
object-oriented programming with Python
guillaume@ubuntu:~/py/0x00$ wc -l 8-concat_edges.py
5 8-concat_edges.py
guillaume@ubuntu:~/py/0x00$     
```
---
9. **Easter Egg**  
   Write a Python script that prints “The Zen of Python”, by Tim Peters, followed by a new line.  
   Your script should be a maximum of 98 characters long (please check with `wc -m 9-easter_egg.py`).
```pyton
guillaume@ubuntu:~/py/0x00$ ./9-easter_egg.py
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
guillaume@ubuntu:~/py/0x00$     
```
---
10. **Linked list cycle**  
   Write a function in C that checks if a singly linked list has a cycle in it.  
   Prototype: `int check_cycle(listint_t *list);`  
   Return: 0 if there is no cycle, 1 if there is a cycle.
```c
carrie@ubuntu:~/0x00$ cat lists.h
#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * 
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */
carrie@ubuntu:~/0x00$ cat 10-linked_lists.c
#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
    const listint_t *current;
    unsigned int n; /* number of nodes */

    current = h;
    n = 0;
    while (current != NULL)
    {
        printf("%i\n", current->n);
        current = current->next;
        n++;
    }

    return (n);
}

/**
 * add_nodeint - adds a new node at the beginning of a listint_t list
 * @head: pointer to a pointer of the start of the list
 * @n: integer to be included in node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
    listint_t *new;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = n;
    new->next = *head;
    *head = new;

    return (new);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
    listint_t *current;

    while (head != NULL)
    {
        current = head;
        head = head->next;
        free(current);
    }
}
carrie@ubuntu:~/0x00$ cat 10-main.c
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * main - check the code
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;
    listint_t *current;
    listint_t *temp;
    int i;

    head = NULL;
    add_nodeint(&head, 0);
    add_nodeint(&head, 1);
    add_nodeint(&head, 2);
    add_nodeint(&head, 3);
    add_nodeint(&head, 4);
    add_nodeint(&head, 98);
    add_nodeint(&head, 402);
    add_nodeint(&head, 1024);
    print_listint(head);

    if (check_cycle(head) == 0)
        printf("Linked list has no cycle\n");
    else if (check_cycle(head) == 1)
        printf("Linked list has a cycle\n");

    current = head;
    for (i = 0; i < 4; i++)
        current = current->next;
    temp = current->next;
    current->next = head;

    if (check_cycle(head) == 0)
        printf("Linked list has no cycle\n");
    else if (check_cycle(head) == 1)
        printf("Linked list has a cycle\n");

    current = head;
    for (i = 0; i < 4; i++)
        current = current->next;
    current->next = temp;

    free_listint(head);

    return (0);
}
carrie@ubuntu:~/0x00$ gcc -Wall -Werror -Wextra -pedantic -std=gnu89 10-main.c 10-check_cycle.c 10-linked_lists.c -o cycle
carrie@ubuntu:~/0x00$$ ./cycle 
1024
402
98
4
3
2
1
0
Linked list has no cycle
Linked list has a cycle
carrie@ubuntu:~/0x00$     
```
---
11. **Hello, write**  
   Write a Python script that prints exactly "and that piece of art is useful - Dora Korpar, 2015-10-19", followed by a new line.  
   Use the function `write` from the `sys` module.  
   You are not allowed to use `print`.  
   Your script should print to stderr.  
   Your script should exit with the status code 1.
```pyton
guillaume@ubuntu:~/py/0x00$ ./100-write.py
and that piece of art is useful - Dora Korpar, 2015-10-19
guillaume@ubuntu:~/py/0x00$ echo $?
1
guillaume@ubuntu:~/py/0x00$ ./100-write.py 2> q
guillaume@ubuntu:~/py/0x00$ cat q
and that piece of art is useful - Dora Korpar, 2015-10-19
guillaume@ubuntu:~/py/0x00$      
```
---
12. **Compile**  
   Write a script that compiles a Python script file.  
   The Python file name will be stored in the environment variable `$PYFILE`.  
   The output filename has to be `$PYFILEc` (e.g., export PYFILE=my_main.py => output filename: my_main.pyc).
```pyton
guillaume@ubuntu:~/py/0x00$ cat main.py 
#!/usr/bin/python3
print("Best School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./101-compile
Compiling main.py ...
guillaume@ubuntu:~/py/0x00$ ls
101-compile  main.py  main.pyc
guillaume@ubuntu:~/py/0x00$ cat main.pyc | zgrep -c "Best School"
1
guillaume@ubuntu:~/py/0x00$ od -t x1 main.pyc # SYSTEM DEPENDANT => CAN BE DIFFERENT
0000000 ee 0c 0d 0a 91 26 3e 58 31 00 00 00 e3 00 00 00
0000020 00 00 00 00 00 00 00 00 00 02 00 00 00 40 00 00
0000040 00 73 0e 00 00 00 65 00 00 64 00 00 83 01 00 01
0000060 64 01 00 53 29 02 7a 10 48 6f 6c 62 65 72 74 6f
0000100 6e 20 53 63 68 6f 6f 6c 4e 29 01 da 05 70 72 69
0000120 6e 74 a9 00 72 02 00 00 00 72 02 00 00 00 fa 07
0000140 6d 61 69 6e 2e 70 79 da 08 3c 6d 6f 64 75 6c 65
0000160 3e 02 00 00 00 73 00 00 00 00
0000172
guillaume@ubuntu:~/py/0x00$      
```
---
13. **ByteCode -> Python #1**  
   Write the Python function `def magic_calculation(a, b):` that does exactly the same as the following Python bytecode:  
   ```
   3           0 LOAD_CONST               1 (98)
               3 LOAD_FAST                0 (a)
               6 LOAD_FAST                1 (b)
               9 BINARY_POWER
              10 BINARY_ADD
              11 RETURN_VALUE
   ```
**[TIP](https://docs.python.org/3.4/library/dis.html):**

Enjoy your journey into the Python world!
