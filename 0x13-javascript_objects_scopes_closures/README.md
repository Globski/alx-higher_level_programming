# High-Level Programming - JavaScript Objects, Scopes, and Closures

# Description

This project covers various concepts in JavaScript including objects, scopes, closures, and more. The goal is to understand and demonstrate, Creating and manipulating objects in JavaScript. Understanding the this keyword. Comprehending the concept of undefined.Recognizing the importance of variable type and scope. Understanding closures and their use cases. Understanding prototypes and inheritance in JavaScript.

## Project Structure

| Task | Description | Source Code |
|------|-------------|-------------|
| 0 | Write an empty class `Rectangle` that defines a rectangle. | [0-rectangle.js](./0-rectangle.js) |
| 1 | Write a class `Rectangle` that defines a rectangle with a constructor taking two arguments `w` and `h`. | [1-rectangle.js](./1-rectangle.js) |
| 2 | Write a class `Rectangle` that creates an empty object if `w` or `h` is not a positive integer. | [2-rectangle.js](./2-rectangle.js) |
| 3 | Write a class `Rectangle` with an instance method `print()` that prints the rectangle using `X`. | [3-rectangle.js](./3-rectangle.js) |
| 4 | Write a class `Rectangle` with instance methods `rotate()` and `double()`. | [4-rectangle.js](./4-rectangle.js) |
| 5 | Write a class `Square` that inherits from `Rectangle` and initializes with one argument `size`. | [5-square.js](./5-square.js) |
| 6 | Write a class `Square` with an instance method `charPrint(c)` that prints the square using character `c`. | [6-square.js](./6-square.js) |
| 7 | Write a function that returns the number of occurrences of an element in a list. | [7-occurrences.js](./7-occurrences.js) |
| 8 | Write a function that returns the reversed version of a list without using the built-in `reverse` method. | [8-esrever.js](./8-esrever.js) |
| 9 | Write a function that prints the number of arguments already printed and the new argument value. | [9-logme.js](./9-logme.js) |
| 10 | Write a function that converts a number from base 10 to another base passed as argument. | [10-converter.js](./10-converter.js) |
| 11 | Write a script that imports an array and computes a new array with each value multiplied by the index. | [100-map.js](./100-map.js) |
| 12 | Write a script that imports a dictionary and computes a dictionary of user ids by occurrence. | [101-sorted.js](./101-sorted.js) |
| 13 | Write a script that concatenates two files. | [102-concat.js](./102-concat.js) |

## Requirements

- **Editors**: vi, vim, emacs
- **Environment**: Ubuntu 20.04 LTS using Node.js (version 14.x)
- **Code Style**: Your code should be semistandard compliant.
- **Execution**: All your files must be executable.
- **Variables**: You are not allowed to use `var`.
- **First Line**: The first line of all your files should be `#!/usr/bin/node`.

## Learning Objectives

By the end of this project, you should be able to:

- Explain why JavaScript programming is amazing.
- Create an object in JavaScript.
- Understand what `this` means.
- Understand what `undefined` means.
- Recognize why variable type and scope are important.
- Explain what a closure is.
- Understand what a prototype is.
- Inherit an object from another.

## How to Use
To use these scripts, ensure you have Node.js installed on your machine. 

### Install Node.js 14

```bash
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

### Install semistandard

```bash
$ sudo npm install semistandard --global
```

You can run each script by navigating to the directory containing the script files and using the following command:

```bash
$ ./<script-name>.js
```

For example, to run `0-rectangle.js`, you would use:

```bash
$ ./0-rectangle.js
```

Make sure that the scripts have execute permissions. If not, you can add execute permissions using:

```bash
$ chmod +x <script-name>.js
```

## Project Tasks

### Task 0: Rectangle #0

Write an empty class `Rectangle` that defines a rectangle:

- You must use the class notation for defining your class

```javascript
guillaume@ubuntu:~/0x13$ cat 0-main.js
#!/usr/bin/node
const Rectangle = require('./0-rectangle');

const r1 = new Rectangle();
console.log(r1);
console.log(r1.constructor);

guillaume@ubuntu:~/0x13$ ./0-main.js
Rectangle {}
[Class: Rectangle]
guillaume@ubuntu:~/0x13$ 
```

**File**: `0-rectangle.js`

### Task 1: Rectangle #1

Write a class `Rectangle` that defines a rectangle:

- You must use the class notation for defining your class
- The constructor must take 2 arguments `w` and `h`
- Initialize the instance attribute `width` with the value of `w`
- Initialize the instance attribute `height` with the value of `h`

```javascript
guillaume@ubuntu:~/0x13$ cat 1-main.js
#!/usr/bin/node
const Rectangle = require('./1-rectangle');

const r1 = new Rectangle(2, 3);
console.log(r1);
console.log(r1.width);
console.log(r1.height);

const r2 = new Rectangle(2, -3);
console.log(r2);
console.log(r2.width);
console.log(r2.height);

const r3 = new Rectangle(2);
console.log(r3);
console.log(r3.width);
console.log(r3.height);

guillaume@ubuntu:~/0x13$ ./1-main.js
Rectangle { width: 2, height: 3 }
2
3
Rectangle { width: 2, height: -3 }
2
-3
Rectangle { width: 2, height: undefined }
2
undefined
guillaume@ubuntu:~/0x13$ 
```

**File**: `1-rectangle.js`

### Task 2: Rectangle #2

Write a class `Rectangle` that defines a rectangle:

- You must use the class notation for defining your class
- The constructor must take 2 arguments `w` and `h`
- Initialize the instance attribute `width` with the value of `w`
- Initialize the instance attribute `height` with the value of `h`
- If `w` or `h` is equal to 0 or not a positive integer, create an empty object

**File**: `2-rectangle.js`

### Task 3: Rectangle #3

Write a class `Rectangle` that defines a rectangle:

- You must use the class notation for defining your class
- The constructor must take 2 arguments: `w` and `h`
- Initialize the instance attribute `width` with the value of `w`
- Initialize the instance attribute `height` with the value of `h`
- If `w` or `h` is equal to 0 or not a positive integer, create an empty object
- Create an instance method called `print()` that prints the rectangle using the character `X`

**File**: `3-rectangle.js`

### Task 4: Rectangle #4

Write a class `Rectangle` that defines a rectangle:

- You must use the class notation for defining your class
- The constructor must take 2 arguments: `w` and `h`
- Initialize the instance attribute `width` with the value of `w`
- Initialize the instance attribute `height` with the value of `h`
- If `w` or `h` is equal to 0 or not a positive integer, create an empty object
- Create an instance method called `print()` that prints the rectangle using the character `X`
- Create an instance method called `rotate()` that exchanges the width and the height of the rectangle
- Create an instance method called `double()` that multiples the width and the height of the rectangle by 2

**File**: `4-rectangle.js`

### Task 5: Square #0

Write a class `Square` that defines a square and inherits from `Rectangle` of `4-rectangle.js`:

- You must use the class notation for defining your class and `extends`
- The constructor must take 1 argument: `size`
- The constructor of `Rectangle` must be called (by using `super()`)

**File**: `5-square.js`

### Task 6: Square #1

Write a class `Square` that defines a square and inherits from `Square` of `5-square.js`:

- You must use the class notation for defining your class and `extends`
- Create an instance method called `charPrint(c)` that prints the rectangle using the character `c`
- If `c` is undefined, use the character `X`

**File**: `6-square.js`

### Task 7: Occurrences

Write a function that returns the number of occurrences in a list:

- Prototype: `exports.nbOccurences = function (list, searchElement)`

**File**: `7-occurrences.js`

### Task 8: Esrever

Write a function that returns the reversed version of a list:

- Prototype: `exports.esrever = function (list)`
- You are not allowed to use the built-in method `reverse`

**File**: `8-esrever.js`

### Task 9: Log me

Write a function that prints the number of arguments already printed and the new argument value. (see example below)

- Prototype: `exports.logMe = function (item)`
- Output format: `<number arguments already printed>: <current argument value>`

**File**: `9-logme.js`

### Task 10: Number conversion

Write a function that converts a number from base 10 to another base passed as argument:

- Prototype: `exports.converter = function (base)`
- You are not allowed to import any file
- You are not allowed to declare any new variable (var, let, etc..)

**File**: `10-converter.js`

### Task 11: Factor index

Write a script that imports an array and computes a new array.

- Your script must import `list` from the file `100-data.js`
- You must use a `map`
- A new list must be created

 with each value equal to the value of the initial list, multipled by the index in the list
- Print both the initial list and the new list

**File**: `100-map.js`

### Task 12: Sorted occurrences

Write a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.

- Your script must import `dict` from the file `101-data.js`
- In the new dictionary:
  - A key is a number of occurrences
  - A value is the list of user ids
- Print the new dictionary at the end

**File**: `101-sorted.js`

### Task 13: Concat files

Write a script that concatenates two files.

- The first argument is the file path of the first source file
- The second argument is the file path of the second source file
- The third argument is the file path of the destination

**File**: `102-concat.js`

Happy coding!
