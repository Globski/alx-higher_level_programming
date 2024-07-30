# High-Level Programming - JavaScript Web scraping

# Description

This project involves creating various scripts to practice web scraping, handle file operations, and API interactions using JavaScript. The scripts are designed to practice web scraping, reading and writing files, making HTTP requests, and interacting with APIs. The tasks range from simple file operations to complex API queries.

## Project Structure

| Task | Description | Source Code |
|------|-------------|-------------|
| `0-readme.js` | Write a script that reads and prints the content of a file. The first argument is the file path. The content of the file must be read in UTF-8. If an error occurs during reading, print the error object. | [Source Code](./0-readme.js) |
| `1-writeme.js` | Write a script that writes a string to a file. The first argument is the file path. The second argument is the string to write. The content of the file must be written in UTF-8. If an error occurs during writing, print the error object. | [Source Code](./1-writeme.js) |
| `2-statuscode.js` | Write a script that displays the status code of a GET request. The first argument is the URL to request (GET). The status code must be printed in the format: `code: <status_code>`. You must use the module `request`. | [Source Code](./2-statuscode.js) |
| `3-starwars_title.js` | Write a script that prints the title of a Star Wars movie where the episode number matches a given integer. The first argument is the movie ID. You must use the Star Wars API with the endpoint `https://swapi-api.alx-tools.com/api/films/:id`. You must use the module `request`. | [Source Code](./3-starwars_title.js) |
| `4-starwars_count.js` | Write a script that prints the number of movies where the character "Wedge Antilles" is present. The first argument is the API URL of the Star Wars API: `https://swapi-api.alx-tools.com/api/films/`. Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API. You must use the module `request`. | [Source Code](./4-starwars_count.js) |
| `5-request_store.js` | Write a script that gets the contents of a webpage and stores it in a file. The first argument is the URL to request. The second argument is the file path to store the body response. The file must be UTF-8 encoded. You must use the module `request`. | [Source Code](./5-request_store.js) |
| `6-completed_tasks.js` | Write a script that computes the number of tasks completed by user ID. The first argument is the API URL: `https://jsonplaceholder.typicode.com/todos`. Only print users with completed tasks. You must use the module `request`. | [Source Code](./6-completed_tasks.js) |
| `100-starwars_characters.js` | Write a script that prints all characters of a Star Wars movie. The first argument is the Movie ID - example: 3 = “Return of the Jedi”. Display one character name per line. You must use the Star Wars API. You must use the module `request`. | [Source Code](./100-starwars_characters.js) |
| `101-starwars_characters.js` | Write a script that prints all characters of a Star Wars movie in the same order as listed in the `characters` field. The first argument is the Movie ID - example: 3 = “Return of the Jedi”. Display one character name per line in the same order of the list “characters” in the `/films/` response. You must use the Star Wars API. You must use the module `request`. | [Source Code](./101-starwars_characters.js) |

## Features

1. **Web Scraping with `request`**
   - Use the `request` module to fetch data from a URL. For example:

2. **JSON Data Manipulation**
   - Parse JSON data and manipulate it. For example:

3. **Reading and Writing Files with `fs`**
   - Read from and write to files using the `fs` module:

## Learning Objectives
By the end of this project, you should be able to:

- Explain why JavaScript programming is amazing.
- Manipulate JSON data.
- Use `request` and `fetch` APIs.
- Read and write files using the `fs` module.

## Environment

- Node.js version 14.x
- Ubuntu 20.04 LTS

## Requirements

- The first line of each script should be `#!/usr/bin/node`.
- Code must be semistandard compliant with semicolons on top.
- Ensure that all files are executable and end with a new line.

## How to Use

1. **Install Node.js 14.x**
   ```bash
   curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
   sudo apt-get install -y nodejs
   ```

2. **Install `semistandard`**
   ```bash
   sudo npm install semistandard --global
   ```

3. **Install `request` module**
   ```bash
   sudo npm install request --global
   export NODE_PATH=/usr/lib/node_modules
   ```

4. **To execute each script, use the following command structure:**

   ```bash
   ./<script_name> <argument1> <argument2>
   ```

## Additional Info

- The `request` module has been deprecated since February 2020 but is still used for practicing web scraping in JavaScript.

## Tasks

### 0. `0-readme.js`
**Description:**  
Write a script that reads and prints the content of a file.

**Requirements:**
- The first argument is the file path.
- The content of the file must be read in UTF-8.
- If an error occurs during reading, print the error object.

**Example Usage:**
```bash
guillaume@ubuntu:~/0x14$ ./0-readme.js cisfun
C is super fun!

guillaume@ubuntu:~/0x14$ ./0-readme.js doesntexist
{ Error: ENOENT: no such file or directory, open 'doesntexist'
    at Error (native)
  errno: -2,
  code: 'ENOENT',
  syscall: 'open',
  path: 'doesntexist' }
```

### 1. `1-writeme.js`
**Description:**  
Write a script that writes a string to a file.

**Requirements:**
- The first argument is the file path.
- The second argument is the string to write.
- The content of the file must be written in UTF-8.
- If an error occurs during writing, print the error object.

**Example Usage:**
```bash
guillaume@ubuntu:~/0x14$ ./1-writeme.js my_file.txt "Python is cool"
guillaume@ubuntu:~/0x14$ cat my_file.txt ; echo ""
Python is cool
```

### 2. `2-statuscode.js`
**Description:**  
Write a script that displays the status code of a GET request.

**Requirements:**
- The first argument is the URL to request (GET).
- The status code must be printed in the format: `code: <status_code>`.
- You must use the module `request`.

**Example Usage:**
```bash
guillaume@ubuntu:~/0x14$ ./2-statuscode.js https://alx-intranet.hbtn.io/status
code: 200

guillaume@ubuntu:~/0x14$ ./2-statuscode.js https://alx-intranet.hbtn.io/doesnt_exist
code: 404
```

### 3. `3-starwars_title.js`
**Description:**  
Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.

**Requirements:**
- The first argument is the movie ID.
- You must use the Star Wars API with the endpoint `https://swapi-api.alx-tools.com/api/films/:id`.
- You must use the module `request`.

**Example Usage:**
```bash
guillaume@ubuntu:~/0x14$ ./3-starwars_title.js 1
A New Hope

guillaume@ubuntu:~/0x14$ ./3-starwars_title.js 5
Attack of the Clones
```

### 4. `4-starwars_count.js`
**Description:**  
Write a script that prints the number of movies where the character "Wedge Antilles" is present.

**Requirements:**
- The first argument is the API URL of the Star Wars API: `https://swapi-api.alx-tools.com/api/films/`.
- Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API.
- You must use the module `request`.

**Example Usage:**
```bash
guillaume@ubuntu:~/0x14$ ./4-starwars_count.js https://swapi-api.alx-tools.com/api/films
3
```

### 5. `5-request_store.js`
**Description:**  
Write a script that gets the contents of a webpage and stores it in a file.

**Requirements:**
- The first argument is the URL to request.
- The second argument is the file path to store the body response.
- The file must be UTF-8 encoded.
- You must use the module `request`.

**Example Usage:**
```bash
guillaume@ubuntu:~/0x14$ ./5-request_store.js http://loripsum.net/api loripsum
guillaume@ubuntu:~/0x14$ cat loripsum
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Haec quo modo conveniant, non sane intellego. Nam memini etiam quae nolo, oblivisci non possum quae volo. Te enim iudicem aequum puto, modo quae dicat ille bene noris. Terram, mihi crede, ea lanx et maria deprimet. Deinde prima illa, quae in congressu solemus: Quid tu, inquit, huc? Hoc etsi multimodis reprehendi potest, tamen accipio, quod dant. </p>
...
```

### 6. `6-completed_tasks.js`
**Description:**  
Write a script that computes the number of tasks completed by user ID.

**Requirements:**
- The first argument is the API URL: `https://jsonplaceholder.typicode.com/todos`.
- Only print users with completed tasks.
- You must use the module `request`.

**Example Usage:**
```bash
guillaume@ubuntu:~/0x14$ ./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos
{ '1': 11,
  '2': 8,
  '3': 7,
  '4': 6,
  '5': 12,
  '6': 6,
  '7': 9,
  '8': 11,
  '9': 8,
  '10': 12 }
```

### 7. `100-starwars_characters.js`
**Description:**  
Write a script that prints all characters of a Star Wars movie.

**Requirements:**
- The first argument is the Movie ID - example: 3 = “Return of the Jedi”.
- Display one character name per line.
- You must use the Star Wars API.
- You must use the module `request`.

**Example Usage:**
```bash
guillaume@ubuntu:~/0x14$ ./100-starwars_characters.js 3
Darth Vader
R2-D2
Luke Skywalker
Han Solo
Leia Organa
```

### 8. `101-starwars_characters.js`
**Description:**  
Write a script that prints all characters of a Star Wars movie in the same order as listed in the `characters` field.

**Requirements:**
- The first argument is the Movie ID - example: 3 = “Return of the Jedi”.
- Display one character name per line in the same order of the list “characters” in the `/films/` response.
- You must use the Star Wars API.
- You must use the module `request`.

**Example Usage:**
```bash
guillaume@ubuntu:~/0x14$ ./101-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
```
