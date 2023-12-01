# High-Level Programming - Python Import & Modules

## Description

This repository contains a collection of Python scripts focusing on concepts related to importing modules, creating modules, using command line arguments, and working with functions from external files.

## Project Structure

| Task | Description | Source Code Link |
| ---- | ----------- | ----------------- |
| 0. Import a simple function from a simple file | Program to import a function from an external file | [0-import_add.py](./0-import_add.py), [0-add.py](./0-add.py) |
| 1. My first toolbox! | Program to import functions from an external file and perform mathematical operations | [1-calculation.py](./1-calculation.py), [calculator_1.py](./calculator_1.py) |
| 2. How to make a script dynamic! | Program to print the number and list of command line arguments | [2-args.py](./2-args.py) |
| 3. Infinite addition | Program to print the result of the addition of all command line arguments | [3-infinite_add.py](./3-infinite_add.py) |
| 4. Who are you? | Program to print names defined in a compiled module | [4-hidden_discovery.py](./4-hidden_discovery.py), [hidden_4.pyc](./hidden_4.pyc) |
| 5. Everything can be imported | Program to import a variable from an external file | [5-variable_load.py](./5-variable_load.py), [variable_load_5.py](./variable_load_5.py) |
| 6. Build my own calculator! | Program to import functions and handle basic operations | [100-my_calculator.py](./100-my_calculator.py), [calculator_1.py](./calculator_1.py) |
| 7. Easy print | Program to print a specific string without using print, eval, open, or sys | [101-easy_print.py](./101-easy_print.py) |
| 8. ByteCode -> Python #3 | Python function to match given Python bytecode | [102-magic_calculation.py](./102-magic_calculation.py) |
| 9. Fast alphabet | Program to print the alphabet in uppercase | [103-fast_alphabet.py](./103-fast_alphabet.py) |

## Environment
- All Python scripts are interpreted on Ubuntu 20.04 LTS using Python 3.8.5.
- The project follows the Pycodestyle style guide.

## Coding Style

This project adheres to the Pycodestyle style guide. Ensure your Python code follows Pycodestyle conventions by running the following command:

```bash
pycodestyle *.py
```

If Pycodestyle is not installed, you can install it using:
```bash
pip install pycodestyle
```
## Requirements
- Python 3
- Pycodestyle
- Python scripts should end with a newline and start with #!/usr/bin/python3.
- All files must be executable.

## Learning Objectives
After completing this project, you should be able to explain:
- How to import functions from another file
- How to use imported functions
- How to create a module
- How to use the built-in function dir()
- How to prevent code in your script from being executed when imported
- How to use command line arguments with your Python programs

## How to Use

### Prerequisites
Before you begin, ensure you have the following installed on your machine:

- Python 3.x (version 3.8.5 recommended)
- Pycodestyle (version 2.8.*)

You can check your Python version using:
```bash
python3 --version
```

### Installation
Clone the repository and navigate to the project directory:
```bash
git clone https://github.com/your-username/alx-higher_level_programming.git
cd alx-higher_level_programming/0x02-python-import_modules
```

Running Python Scripts
Each Python script can be executed using the python3 command. For example:
```bash
python3 0-import_add.py
```

Ensure that all scripts are executable with:
```bash
chmod +x *.py
```
