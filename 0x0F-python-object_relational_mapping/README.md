# High-Level Programming - Python Object-relational mapping

## Description
In this project, you will link two amazing worlds: Databases and Python! You will use the MySQLdb module to connect to a MySQL database and execute SQL queries. Additionally, you will use SQLAlchemy, an Object Relational Mapper (ORM), which abstracts database queries into Python objects.

The biggest difference with an ORM is that you will no longer need to write SQL queries directly. The purpose of an ORM is to abstract the storage layer, allowing you to interact with the database using Python objects. This means your main focus will be on manipulating objects rather than worrying about how and where these objects are stored.

With an ORM, your code becomes storage type-independent, making it easier to switch between different types of storage without needing to rewrite your entire project.
## Project structure

| Task                                  | Description                                                     | Source Code |
|---------------------------------------|-----------------------------------------------------------------|-------------|
| 0. Get all states                     | Lists all states from the database                               | [0-select_states.py](./0-select_states.py) |
| 1. Filter states                      | Lists all states with a name starting with 'N'                   | [1-filter_states.py](./1-filter_states.py) |
| 2. Filter states by user input        | Lists all states with a name starting with user input            | [2-my_filter_states.py](./2-my_filter_states.py) |
| 3. SQL Injection...                   | Securely lists states matching a user-provided name              | [3-my_safe_filter_states.py](./3-my_safe_filter_states.py) |
| 4. Cities by states                   | Lists all cities from the database                               | [4-cities_by_state.py](./4-cities_by_state.py) |
| 5. All cities by state                | Lists all cities of a state specified by the user                | [5-filter_cities.py](./5-filter_cities.py) |
| 6. First state model                  | Defines a State class and links to MySQL table `states`          | [model_state.py](./model_state.py) |
| 7. All states via SQLAlchemy          | Lists all State objects from the database                        | [7-model_state_fetch_all.py](./7-model_state_fetch_all.py) |
| 8. First state                        | Prints the first State object from the database                  | [8-model_state_fetch_first.py](./8-model_state_fetch_first.py) |
| 9. Contains `a`                       | Lists all State objects that contain the letter `a`              | [9-model_state_filter_a.py](./9-model_state_filter_a.py) |
| 10. Get a state                       | Prints the State object with the name passed as argument         | [10-model_state_my_get.py](./10-model_state_my_get.py) |
| 11. Add a new state                   | Adds the State object "Louisiana" to the database                | [11-model_state_insert.py](./11-model_state_insert.py) |
| 12. Update a state                    | Changes the name of a State object where `id = 2` to "New Mexico"| [12-model_state_update_id_2.py](./12-model_state_update_id_2.py) |
| 13. Delete states                     | Deletes all State objects with a name containing the letter `a`  | [13-model_state_delete_a.py](./13-model_state_delete_a.py) |
| 14. Cities in state                   | Defines a City class with relationship to State                  | [model_city.py](./model_city.py) |
| 15. City relationship                 | Improves the State class to add relationship with City           | [model_state.py](./model_state.py) |
| 16. List relationship                 | Lists all City objects from the database                         | [101-relationship_states_cities_list.py](./101-relationship_states_cities_list.py) |
| 17. From city                         | Lists all City objects from the database                         | [102-relationship_cities_states_list.py](./102-relationship_cities_states_list.py) |

## Requirements

- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- Your files will be executed with MySQLdb version `2.0.x`
- Your files will be executed with SQLAlchemy version `1.4.x`
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- Your code should use the `pycodestyle` (version `2.8.*`)
- All your files must be executable
- You are not allowed to use `execute` with SQLAlchemy

## Learning Objectives

- Why Python programming is awesome
- How to connect to a MySQL database from a Python script
- How to `SELECT` rows in a MySQL table from a Python script
- How to `INSERT` rows in a MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table
- How to create a Python Virtual Environment

## Setup Instructions

### Install and activate `venv`
To create a Python Virtual Environment, allowing you to install specific dependencies for this project:
```sh
$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate
```

### Install MySQLdb module version 2.0.x
For installing MySQLdb, you need to have MySQL installed:
```sh
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)
```

### Install SQLAlchemy module version 1.4.x
```sh
$ sudo pip3 install SQLAlchemy
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
```

## How to Use
- Clone the repository.
- Ensure your MySQL server is running and you have created the necessary databases and tables.
- Use the provided scripts to interact with your database via ORM.

## Project Tasks

### Task 0: Get all states

#### Description:
- Write a script that lists all `states` from the database `hbtn_0e_0_usa`.

#### Requirements:
- Your script should take 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation needed)
- You must use the module `MySQLdb` (`import MySQLdb`)
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- Results must be sorted in ascending order by `states.id`
- Results should be displayed as they are in the example below
- Your code should not be executed when imported


### Task 1: Filter states

#### Description:
- Write a script that lists all `states` with a `name` starting with `N` (upper N) from the database `hbtn_0e_0_usa`.

#### Requirements:
- Your script should take 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation needed)
- You must use the module `MySQLdb` (`import MySQLdb`)
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- Results must be sorted in ascending order by `states.id`
- Results should be displayed as they are in the example below
- Your code should not be executed when imported


### Task 2: Filter states by user input

#### Description:
- Write a script that takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument.

#### Requirements:
- Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name searched` (no argument validation needed)
- You must use the module `MySQLdb` (`import MySQLdb`)
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- You must use `format` to create the SQL query with the user input
- Results must be sorted in ascending order by `states.id`
- Results should be displayed as they are in the example below
- Your code should not be executed when imported


### Task 3: SQL Injection...

#### Description:
- Write a script that takes in arguments and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument. But this time, write one that is safe from MySQL injections!

#### Requirements:
- Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name searched` (safe from MySQL injection)
- You must use the module `MySQLdb` (`import MySQLdb`)
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- Results must be sorted in ascending order by `states.id`
- Results should be displayed as they are in the example below
- Your code should not be executed when imported

### Task 4: Cities by states

#### Description:
- Write a script that lists all `cities` from the database `hbtn_0e_4_usa`.

#### Requirements:
- Your script should take 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation needed)
- You must use the module `MySQLdb` (`import MySQLdb`)
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- Results must be sorted in ascending order by `cities.id`
- You can use only `execute()` once
- Results should be displayed as they are in the example below
- Your code should not be executed when imported

### Task 5: All cities by state

#### Description:
- Write a script that takes in the name of a state as an argument and lists all `cities` of that state, using the database `hbtn_0e_4_usa`.

#### Requirements:
- Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name` (no argument validation needed)
- You must use the module `MySQLdb` (`import MySQLdb`)
- Your script should connect to a MySQL server running on `localhost` at port `330

6`
- You must use `format` to create the SQL query with the user input
- Results must be sorted in ascending order by `cities.id`
- You can use only `execute()` once
- Results should be displayed as they are in the example below
- Your code should not be executed when imported

### Task 6: First state model

#### Description:
- Write a python file that contains the class definition of a `State` and an instance `Base = declarative_base()`.

#### Requirements:
- `State` class:
  - inherits from `Base` [imported from `sqlalchemy.ext.declarative`]
  - links to the MySQL table `states`
  - class attribute `id` that represents a column of an auto-generated, unique integer, can't be null and is a primary key
  - class attribute `name` that represents a column of a string with maximum 128 characters and can't be null
- You must use the module `SQLAlchemy`

### Task 7: All states via SQLAlchemy

#### Description:
- Write a script that lists all `State` objects from the database `hbtn_0e_6_usa`.

#### Requirements:
- Your script should take 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation needed)
- You must use the module `SQLAlchemy`
- You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- Results must be sorted in ascending order by `states.id`
- Your code should not be executed when imported

### Task 8: First state

#### Description:
- Write a script that prints the first `State` object from the database `hbtn_0e_6_usa`.

#### Requirements:
- Your script should take 3 arguments: `mysql username`, `mysql password`, and `database name` (no argument validation needed)
- You must use the module `SQLAlchemy`
- You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- Results must be sorted in ascending order by `states.id`
- Your code should not be executed when imported

### Task 9: Contains `a`

#### Description:
- Write a script that lists all `State` objects that contain the letter `a` from the database `hbtn_0e_6_usa`.

#### Requirements:
- Your script should take 3 arguments: `mysql username`, `mysql password`, and `database name` (no argument validation needed)
- You must use the module `SQLAlchemy`
- You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- Results must be sorted in ascending order by `states.id`
- Your code should not be executed when imported

### Task 10: Get a state

#### Description:
- Write a script that prints the `State` object with the `name` passed as argument from the database `hbtn_0e_6_usa`.

#### Requirements:
- Your script should take 4 arguments: `mysql username`, `mysql password`, `database name`, and `state name to search` (no argument validation needed)
- You must use the module `SQLAlchemy`
- You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- You can assume you have one record with the state name to search
- Results must be displayed as they are in the example below
- Your code should not be executed when imported

### Task 11: Add a new state

#### Description:
- Write a script that adds the `State` object "Louisiana" to the database `hbtn_0e_6_usa`.

#### Requirements:
- Your script should take 3 arguments: `mysql username`, `mysql password`, and `database name` (no argument validation needed)
- You must use the module `SQLAlchemy`
- You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- You must print the new `states.id` after creation
- Your code should not be executed when imported

### Task 12: Update a state

#### Description:
- Write a script that changes the name of a `State` object from the database `hbtn_0e_6_usa`.

#### Requirements:
- Your script should take 3 arguments: `mysql username`, `mysql password`, and `database name` (no argument validation needed)
- You must use the module `SQLAlchemy`
- You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- Change the name of the `State` where `id = 2` to `New Mexico`
- Your code should not be executed when imported

### Task 13: Delete states

#### Description:
- Write a script that deletes all `State` objects with a name containing the letter `a` from the database `hbtn_0e_6_usa`.

#### Requirements:
- Your script should take 3 arguments: `mysql username`, `mysql password`, and `database name` (no argument validation needed)
- You must use the module `SQLAlchemy`
- You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- Your code should not be executed when imported

### Task 14: Cities in state

#### Description:
- Write a Python file similar to `model_state.py` named `model_city.py` that contains the class definition of a `City`.

#### Requirements:
- `City` class:
  - inherits from `Base` [imported from `sqlalchemy.ext.declarative`]
  - links to the MySQL table `cities`
  - class attribute `id` that represents a column of an auto-generated, unique integer, can't be null and is a primary key
  - class attribute `name` that represents a column of a string with maximum 128 characters and can't be null
  - class attribute `state_id` that represents a column of an integer, can't be null and is a foreign key to `states.id`
- You must use the module `SQLAlchemy`

### Task 15: City relationship

#### Description:
- Improve the `State` class to add the relationship with the class `City`.

#### Requirements:
- You must use the module `SQLAlchemy`
- Update `State` to link to `City` objects:
  - One to Many relationship: State (1) -> City (Many)
  - class attribute `cities` must represent a relationship with the class `City`. If the State object is deleted, all linked City objects must be automatically deleted. Also, the reference from a City object to its State should be named `state`.

### Task 16: List relationship

#### Description:
- Write a script that lists all `City` objects from the database `hbtn_0e_101_usa`.

#### Requirements:
- Your script should take 3 arguments: `mysql username`, `mysql password`, and `database name` (no argument validation needed)
- You must use the module `SQLAlchemy`
- You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- Results must be sorted in ascending order by `cities.id`
- You must use the `cities` relationship for all `State` objects

### Task 17: From city

#### Description:
- Write a script that lists all `City` objects from the database `hbtn_0e_101_usa`.

#### Requirements:
- Your script should take 3 arguments: `mysql username`, `mysql password`, and `database name` (no argument validation needed)
- You must use the module `SQLAlchemy`
- You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- Results must be sorted in ascending order by `cities.id`
