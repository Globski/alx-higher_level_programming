# Alx Higher Level Programming - Python Exceptions

## Description
This repository contains a series of tasks focusing on handling exceptions in Python. The exercises range from basic exception handling to more advanced scenarios involving custom error messages and list manipulations. Each task emphasizes the use of try/except blocks to ensure that the code behaves gracefully in the face of errors.


## Additional Notes

1. **Errors vs. Exceptions**:
   - **Errors** are issues that occur in the code that typically lead to a program crashing. These can be syntax errors or logical errors.
   - **Exceptions** are specific errors that can be caught and handled using `try` and `except` blocks.

2. **What are Exceptions?**
   - Exceptions are events that disrupt the normal flow of a program. They can be raised by the interpreter or by the programmer using the `raise` statement.

3. **When to Use Exceptions**:
   - Use exceptions when you anticipate potential errors in your code (e.g., file not found, division by zero) and you want to handle them gracefully without crashing the program.

4. **Handling Exceptions**:
   - You can handle exceptions using `try`, `except`, `else`, and `finally` blocks.

5. **Catching Exceptions**:
   - Catching exceptions allows you to respond to errors. You can catch specific exceptions or a general exception.

6. **Raising Exceptions**:
   - You can raise exceptions using the `raise` keyword when you want to signal that an error has occurred.
   ```python
   raise ValueError("A custom error message")
   ```

7. **Clean-Up Actions**:
   - Sometimes, you need to perform clean-up actions after an exception, such as closing files or releasing resources. This can be done in the `finally` block.
