# High-Level Programming - Python Network #0

## Description

This project covers the basics of networking in the context of web development. You will learn about URLs, HTTP methods, HTTP headers, and how to use `curl` to make HTTP requests. The project aims to provide you with a solid understanding of how web communication works at the protocol level.

## Project Structure

| Task                               | Description                                                                                                | Source Code                                   |
|------------------------------------|------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| 0. cURL body size                  | Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response | [0-body_size.sh](./0-body_size.sh)           |
| 1. cURL to the end                 | Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response | [1-body.sh](./1-body.sh)                     |
| 2. cURL Method                     | Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response | [2-delete.sh](./2-delete.sh)                 |
| 3. cURL only methods               | Write a Bash script that takes in a URL and displays all HTTP methods the server will accept               | [3-methods.sh](./3-methods.sh)               |
| 4. cURL headers                    | Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response | [4-header.sh](./4-header.sh)                 |
| 5. cURL POST parameters            | Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response | [5-post_params.sh](./5-post_params.sh)       |
| 6. Find a peak                     | Write a function that finds a peak in a list of unsorted integers                                          | [6-peak.py](./6-peak.py)                     |
| 7. Only status code                | Write a Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response | [100-status_code.sh](./100-status_code.sh)   |
| 8. cURL a JSON file                | Write a Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response | [101-post_json.sh](./101-post_json.sh)       |
| 9. Catch me if you can!            | Write a Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing `You got me!` in the body of the response | [102-catch_me.sh](./102-catch_me.sh)         |


## Learning Objectives

By the end of this project, you should be able to:

   - Explain what a URL is and its components.
   - Define HTTP and understand its purpose.
   - Read and interpret a URL.
   - Identify the scheme in an HTTP URL.
   - Understand what a domain name is.
   - Differentiate between a domain and a sub-domain.
   - Define and identify a port number in a URL.
   - Explain what a query string is.
   - Describe what an HTTP request is.
   - Explain what an HTTP response is.
   - Identify and explain HTTP headers.
   - Understand the HTTP message body.
   - Describe various HTTP request methods.
   - Understand HTTP response status codes.
   - Explain what an HTTP cookie is.
   - Make HTTP requests using `curl`.
   - Describe what happens when you type a URL into a browser (application level).

## Environment

- OS: Ubuntu 20.04 LTS
- Interpreter: Python 3 (version 3.8.5)

## Requirements

- Bash scripts should be exactly 3 lines long (`wc -l file` should print 3).
- All files should end with a new line.
- All files must be executable.
- The first line of all Bash scripts should be exactly `#!/bin/bash`.
- All `curl` commands must include the `-s` option (silent mode).
- The first line of all Python files should be exactly `#!/usr/bin/python3`.
- Code should follow the `pycodestyle` guidelines (version 2.8.*).
- All modules, classes, and functions should be documented with proper docstrings.

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/alx-higher_level_programming.git
   ```
2. Navigate to the project directory:
   ```bash
   cd alx-higher_level_programming/0x10-python-network_0
   ```
3. Run the scripts according to their tasks. For example, to run Task 0:
   ```bash
   ./0-body_size.sh http://example.com

4. To execute a Bash script, use the following command:

```sh
./script_name.sh
```

5. To run a Python script, use the following command:

```sh
./script_name.py
```

### Additional Info

Ensure you have the necessary permissions to execute the scripts. If not, you can grant execute permissions using:

```bash
chmod +x script_name.sh
```
```
Replace `script_name.sh` with the actual script name you intend to run.
```

## Tasks

### Task 0: cURL body size

**Description:** Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response in bytes.

**Example:**
```bash
./0-body_size.sh 0.0.0.0:5000
```

- File: `0-body_size.sh`

### Task 1: cURL to the end

**Description:** Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response (only for a 200 status code response).

**Example:**
```bash
./1-body.sh 0.0.0.0:5000/route_1
```

- File: `1-body.sh`

### Task 2: cURL Method

**Description:** Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response.

**Example:**
```bash
./2-delete.sh 0.0.0.0:5000/route_3
```

- File: `2-delete.sh`

### Task 3: cURL only methods

**Description:** Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.

**Example:**
```bash
./3-methods.sh 0.0.0.0:5000/route_4
```

- File: `3-methods.sh`

### Task 4: cURL headers

**Description:** Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response. A header variable `X-School-User-Id` must be sent with the value `98`.

**Example:**
```bash
./4-header.sh 0.0.0.0:5000/route_5
```

- File: `4-header.sh`

### Task 5: cURL POST parameters

**Description:** Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response. A variable `email` must be sent with the value `test@gmail.com`. A variable `subject` must be sent with the value `I will always be here for PLD`.

**Example:**
```bash
./5-post_params.sh 0.0.0.0:5000/route_6
```

- File: `5-post_params.sh`

### Task 6: Find a peak

**Description:** Write a function that finds a peak in a list of unsorted integers. The algorithm must have the lowest complexity.

**Example:**
```python
find_peak([1, 2, 4, 6, 3])
```

- File: `6-peak.py`
- File: `6-peak.txt`

### Task 7: Only status code

**Description:** Write a Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.

**Example:**
```bash
./100-status_code.sh 0.0.0.0:5000
```

- File: `100-status_code.sh`

### Task 8: cURL a JSON file

**Description:** Write a Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response. The script must send a POST request with the contents of a file, passed with the filename as the second argument of the script, in the body of the request.

**Example:**
```bash
./101-post_json.sh 0.0.0.0:5000/route_json my_json_0
```

- File: `101-post_json.sh`

### Task 9: Catch me if you can!

**Description:** Write a Bash script that makes a request to `0.0.0.0:5000/catch_me` that causes the server to respond with a message containing `You got me!` in the body of the response.

**Example:**
```bash
./102-catch_me.sh
```

- File: `102-catch_me.sh`


