# High-Level Programming - SQL Introduction

## Project Description

This project focuses on SQL (Structured Query Language) introduction and practical applications. It covers various SQL concepts and tasks, including creating databases, tables, executing queries, and manipulating data.

## Project Structure

| Task | Description | Source Code |
|------|-------------|-------------|
| 0. List databases | Write a script to list all databases in MySQL server. | [0-list_databases.sql](./0-list_databases.sql) |
| 1. Create a database | Write a script to create a database if it doesn't exist in MySQL server. | [1-create_database_if_missing.sql](./1-create_database_if_missing.sql) |
| 2. Delete a database | Write a script to delete a database if it exists in MySQL server. | [2-remove_database.sql](./2-remove_database.sql) |
| 3. List tables | Write a script to list all tables of a database in MySQL server. | [3-list_tables.sql](./3-list_tables.sql) |
| 4. First table | Write a script to create a table called first_table in MySQL server. | [4-first_table.sql](./4-first_table.sql) |
| 5. Full description | Write a script to print the full description of a table in MySQL server. | [5-full_table.sql](./5-full_table.sql) |
| 6. List all in table | Write a script to list all rows of a table in MySQL server. | [6-list_values.sql](./6-list_values.sql) |
| 7. First add | Write a script to insert a new row in a table in MySQL server. | [7-insert_value.sql](./7-insert_value.sql) |
| 8. Count 89 | Write a script to count records with id = 89 in a table in MySQL server. | [8-count_89.sql](./8-count_89.sql) |
| 9. Full creation | Write a script to create a table and add multiple rows in MySQL server. | [9-full_creation.sql](./9-full_creation.sql) |
| 10. List by best | Write a script to list all records ordered by score in MySQL server. | [10-top_score.sql](./10-top_score.sql) |
| 11. Select the best | Write a script to list records with a score >= 10 ordered by score in MySQL server. | [11-best_score.sql](./11-best_score.sql) |
| 12. Cheating is bad | Write a script to update the score of a specific record in MySQL server. | [12-no_cheating.sql](./12-no_cheating.sql) |
| 13. Score too low | Write a script to remove records with a score <= 5 in MySQL server. | [13-change_class.sql](./13-change_class.sql) |
| 14. Average | Write a script to compute the score average of all records in MySQL server. | [14-average.sql](./14-average.sql) |
| 15. Number by score | Write a script to list the number of records with the same score in MySQL server. | [15-groups.sql](./15-groups.sql) |
| 16. Say my name | Write a script to list all records with a name value in MySQL server. | [16-no_link.sql](./16-no_link.sql) |
| 17. Go to UTF8 | Write a script to convert database, table, and field to UTF8 in MySQL server. | [100-move_to_utf8.sql](./100-move_to_utf8.sql) |
| 18. Temperatures #0 | Write a script to display the average temperature by city in MySQL server. | [101-avg_temperatures.sql](./101-avg_temperatures.sql) |
| 19. Temperatures #1 | Write a script to display the top 3 cities' temperatures during July and August in MySQL server. | [102-top_city.sql](./102-top_city.sql) |
| 20. Temperatures #2 | Write a script to display the max temperature of each state in MySQL server. | [103-max_state.sql](./103-max_state.sql) |

## Environment

- All scripts are executed on Ubuntu 20.04 LTS.
- MySQL version 8.0.25 is used.

## Learning Objectives

After completing this project, you should be able to:

- Explain the concepts of databases, relational databases, SQL, and MySQL.
- Create databases and tables, execute queries, and manipulate data in MySQL.
- Understand SQL keywords, syntax, and functions.
- Implement advanced SQL queries and operations.

## Requirements

- All files executed on Ubuntu 20.04 LTS using MySQL 8.0
- All SQL keywords should be in uppercase
- All files should end with a new line

## How to Use

Follow these steps to run the SQL scripts:

1. Make sure you have MySQL 8.0 installed on your Ubuntu 20.04 LTS system.
2. Clone the repository to your local machine.
3. Navigate to the directory containing the SQL files.
4. Open a terminal and execute the scripts using the MySQL command-line client.
5. Provide any required credentials when prompted.

## Additional Info

- Install MySQL 8.0 on Ubuntu 20.04 LTS:
  ```
  $ sudo apt update
  $ sudo apt install mysql-server
  ```
  - Use "container-on-demand" to run MySQL:
  ```
  $ service mysql start
  ```
- Connect to MySQL server:
  ```
  $ sudo mysql
  ```

