# High-Level Programming - JavaScript Warm-Up

## Description

This repository contains a series of tasks aimed at getting you started with JavaScript. Each script is designed to demonstrate basic JavaScript concepts such as constants, loops, conditionals, and functions and encourages the use of best practices, such as avoiding the `var` keyword.

## Project Structure

| **Task**                     | **Description**                                     | **Source Code**                 |
|------------------------------|-----------------------------------------------------|---------------------------------|
| Task 0: First constant, first print | Write a script that prints "JavaScript is amazing" | [0-javascript_is_amazing.js](./0-javascript_is_amazing.js) |
| Task 1: 3 languages          | Write a script that prints 3 lines                  | [1-multi_languages.js](./1-multi_languages.js)       |
| Task 2: Arguments            | Write a script that prints a message based on arguments passed | [2-arguments.js](./2-arguments.js)      |
| Task 3: Value of my argument | Write a script that prints the first argument passed to it | [3-value_argument.js](./3-value_argument.js) |
| Task 4: Create a sentence    | Write a script that prints two arguments in a specific format | [4-concat.js](./4-concat.js)        |
| Task 5: An Integer           | Write a script that prints "My number: "            | [5-to_integer.js](./5-to_integer.js)            |
| Task 6: Loop to languages    | Write a script that prints 3 lines using an array of strings and a loop | [6-multi_languages_loop.js](./6-multi_languages_loop.js) |
| Task 7: I love C             | Write a script that prints `x` times "C is fun"     | [7-multi_c.js](./7-multi_c.js)               |
| Task 8: Square               | Write a script that prints a square                 | [8-square.js](./8-square.js)                |
| Task 9: Add                  | Write a script that prints the addition of 2 integers | [9-add.js](./9-add.js)                |
| Task 10: Factorial           | Write a script that computes and prints a factorial | [10-factorial.js](./10-factorial.js)            |
| Task 11: Second biggest!     | Write a script that searches for the second biggest integer in the list of arguments | [11-second_biggest.js](./11-second_biggest.js) |
| Task 12: Object              | Update a script to replace the value 12 with 89     | [12-object.js](./12-object.js)               |
| Task 13: Add file            | Write a function that returns the addition of 2 integers | [13-add.js](./13-add.js)                |
| Task 14: Const or not const  | Write a file that modifies the value of `myVar` to 333 | [100-let_me_const.js](./100-let_me_const.js)      |
| Task 15: Call me Moby        | Write a function that executes `x` times a function | [101-call_me_moby.js](./101-call_me_moby.js)        |
| Task 16: Add me maybe        | Write a function that increments and calls a function | [102-add_me_maybe.js](./102-add_me_maybe.js)      |
| Task 17: Increment object    | Update a script by adding a new function `incr` that increments the integer value | [103-object_fct.js](./103-object_fct.js)        |

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- Files will be interpreted on Ubuntu 20.04 LTS using Node.js (version 14.x)
- Files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/node`
- Code should be semistandard compliant (version 16.x.x)
- Files must be executable

## Learning Objectives

By the end of this project, you should be able to explain:

- Why JavaScript programming is amazing
- How to run a JavaScript script
- How to create variables and constants
- The differences between `var`, `const`, and `let`
- All data types available in JavaScript
- How to use `if` and `if ... else` statements
- How to use comments
- How to assign values to variables
- How to use `while` and `for` loops
- How to use `break` and `continue` statements
- What a function is and how to use it
- What a function that does not use any return statement returns
- The scope of variables
- The arithmetic operators and how to use them
- How to manipulate dictionaries
- How to import a file

## How to Use

### Install Node 14

```bash
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

### Install semistandard

```bash
$ sudo npm install semistandard --global
```

To run a script, navigate to the directory containing the script and use the following command:

```bash
./filename.js
```

For example, to run the script for Task 0, use:

```bash
./0-javascript_is_amazing.js
```

## Tasks

### Task 0: First constant, first print

Write a script that prints “JavaScript is amazing”:

- Create a constant variable called `myVar` with the value “JavaScript is amazing”
- Use `console.log(...)` to print all output
- Do not use `var`

**File:** `0-javascript_is_amazing.js`

### Task 1: 3 languages

Write a script that prints 3 lines:

- “C is fun”
- “Python is cool”
- “JavaScript is amazing”
- Use `console.log(...)` to print all output
- Do not use `var`

**File:** `1-multi_languages.js`

### Task 2: Arguments

Write a script that prints a message depending on the number of arguments passed:

- If no arguments are passed, print “No argument”
- If one argument is passed, print “Argument found”
- Otherwise, print “Arguments found”
- Use `console.log(...)` to print all output
- Do not use `var`
- Reference: `process.argv`

**File:** `2-arguments.js`

### Task 3: Value of my argument

Write a script that prints the first argument passed to it:

- If no arguments are passed, print “No argument”
- Use `console.log(...)` to print all output
- Do not use `var`
- Do not use `length`

**File:** `3-value_argument.js`

### Task 4: Create a sentence

Write a script that prints two arguments passed to it, in the format: “<arg1> is <arg2>”

- Use `console.log(...)` to print all output
- Do not use `var`

**File:** `4-concat.js`

### Task 5: An Integer

Write a script that prints `My number: <first argument converted to integer>` if the first argument can be converted to an integer:

- If the argument can’t be converted to an integer, print “Not a number”
- Use `console.log(...)` to print all output
- Do not use `var`
- Do not use `try/catch`

**File:** `5-to_integer.js`

### Task 6: Loop to languages

Write a script that prints 3 lines using an array of strings and a loop:

- “C is fun”
- “Python is cool”
- “JavaScript is amazing”
- Use `console.log(...)` to print all output
- Do not use `var`
- Do not use any `if/else` statement
- Use only one `console.log`
- Use a loop (while, for, etc.)

**File:** `6-multi_languages_loop.js`

### Task 7: I love C

Write a script that prints `x` times “C is fun”:

- Where `x` is the first argument of the script
- If the first argument can’t be converted to an integer, print “Missing number of occurrences”
- Use `console.log(...)` to print all output
- Do not use `var`
- Use only two `console.log`
- Use a loop (while, for, etc.)

**File:** `7-multi_c.js`

### Task 8: Square

Write a script that prints a square:

- The first argument is the size of the square
- If the first argument can’t be converted to an integer, print “Missing size”
- Use the character `X` to print the square
- Use `console.log(...)` to print all output
- Do not use `var`
- Use a loop (while, for, etc.)

**File:** `8-square.js`

### Task 9: Add

Write a script that prints the addition of 2 integers:

- The first argument is the first integer
- The second argument is the second integer
- Define a function with this prototype: `function add(a, b)`
- Use `console.log(...)` to print all output
- Do not use `var`

**File:** `9-add.js`

### Task 10: Factorial

Write a script that computes and prints a factorial:

- The first argument is an integer used for computing the factorial
- Factorial of NaN is 1
- Do it recursively
- Use a function
- Use `console.log(...)` to print all output
- Do not use `var`

**File:** `10-factorial.js`

### Task 11: Second biggest!

Write a script that searches for the second biggest integer in the list of arguments:

- Assume all arguments can be converted to integer
- If no arguments are passed, print 0
- If the number of arguments is 1, print 0
- Use `console.log(...)` to print all output
- Do not use `var`

**File:** `11-second_biggest.js`

### Task 12: Object

Update this script to replace the value 12 with 89:

- Do not use `var`

**File:** `12-object.js`

### Task 13: Add file

Write a function that returns the addition of 2 integers:

- The function must be visible from outside
- The name of the function must be `add`
- Do not use `var`

**File:** `13-add.js`

### Advanced Tasks

#### Task 14: Const or not const

Write a file that modifies the value of `myVar` to 333.

**File:** `100-let_me_const.js`

#### Task 15: Call me Moby

Write a function that executes `x` times a function:

- The function must be visible from outside
- Prototype: `function (x, theFunction)`
- Do not use `var`

**File:** `101-call_me_moby.js`

#### Task 16: Add me maybe

Write a function that increments and calls a function:

- The function must be visible from outside
- Prototype: `function (number, theFunction)`
- Do not use `var`

**File:** `102-add_me_maybe.js`

#### Task 17: Increment object

Update this script by adding a new function `incr` that increments the integer value:

- Do not use `var`

**File:** `103-object_fct.js`

