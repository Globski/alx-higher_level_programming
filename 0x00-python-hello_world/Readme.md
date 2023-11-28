# High-Level Programming - Hello World

## Description
This project introduces the basics of Python programming. It covers fundamental concepts such as printing text, using variables, and adhering to the PEP8 style guide. The tasks range from running Python scripts to manipulating strings and printing formatted output.

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

- All Python scripts are interpreted on Ubuntu 20.04 LTS using Python 3.8.5.
- Shell scripts and C scripts are tested on Ubuntu 20.04 LTS.

## Coding Style

- Python code follows the PEP8 (PyCode) style guide.
- C code adheres to the Betty style guide.

## Requirements

- Python scripts should end with a newline and start with `#!/usr/bin/python3`.
- Shell scripts should end with a newline and start with `#!/bin/bash`.
- All files must be executable.
- The length of files is tested using `wc`.
- C scripts are compiled using `gcc` with specific options.


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

### Additional Notes
Ensure that your Python scripts are executable using the following command:

```bash
chmod +x filename.py
```
For code style validation, use Pycodestyle on your Python files:

```bash
pycodestyle filename.py
```
Enjoy your journey into the Python world!

