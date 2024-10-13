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

# How to Use

1. Install **MySQL 8.0** if it is not already installed.

   ```bash
   sudo apt update
   sudo apt install mysql-server
   ```

2. **Start MySQL:**
   - Start the MySQL service.

   ```bash
   sudo service mysql start
   ```

3. **Connect to MySQL:**
   - Access the MySQL monitor.

   ```bash
   sudo mysql
   ```

4. **Container Setup (if applicable):**
   - If using a "container-on-demand," request an Ubuntu 20.04 container.
   - Connect using SSH or the web terminal.
   - Start MySQL inside the container.

   ```bash
   service mysql start
   ```

## Additional Info

## Comments and Documentation

- Each SQL query must have a comment directly above it explaining its purpose. This improves readability and helps reviewers understand your work.

   ```sql
   -- Fetch all records from the students table
   SELECT * FROM students;
   ```

## Task Execution

1. **Write SQL Queries:**
   - Ensure all SQL keywords are written in uppercase (e.g., `SELECT`, `FROM`, `WHERE`).

2. **Running Your SQL Scripts:**
   - You can execute your SQL scripts directly from the command line using:

   ```bash
   cat your_script.sql | mysql -uroot -p
   ```

   - Replace `your_script.sql` with the appropriate SQL file name.

3. **Testing Queries:**
   - After writing each query, test it to ensure it behaves as expected. Check for syntax errors.

## Troubleshooting

- If you encounter issues:
   - Double-check your SQL syntax for errors.
   - Ensure MySQL is running correctly and that you are connected.

### Tasks

0. **List databases**  
   Write a script that lists all databases of your MySQL server.

1. **Create a database**  
   Write a script that creates the database `hbtn_0c_0` in your MySQL server. If the database `hbtn_0c_0` already exists, your script should not fail. You are not allowed to use the SELECT or SHOW statements.

2. **Delete a database**  
   Write a script that deletes the database `hbtn_0c_0` in your MySQL server. If the database `hbtn_0c_0` doesn’t exist, your script should not fail. You are not allowed to use the SELECT or SHOW statements.

3. **List tables**  
   Write a script that lists all the tables of a database in your MySQL server. The database name will be passed as an argument of the mysql command.

4. **First table**  
   Write a script that creates a table called `first_table` in the current database in your MySQL server.  
   `first_table` description:  
   - id INT  
   - name VARCHAR(256)  
   The database name will be passed as an argument of the mysql command. If the table `first_table` already exists, your script should not fail. You are not allowed to use the SELECT or SHOW statements.

5. **Full description**  
   Write a script that prints the full description of the table `first_table` from the database `hbtn_0c_0` in your MySQL server. The database name will be passed as an argument of the mysql command. You are not allowed to use the DESCRIBE or EXPLAIN statements.

6. **List all in table**  
   Write a script that lists all rows of the table `first_table` from the database `hbtn_0c_0` in your MySQL server. All fields should be printed. The database name will be passed as an argument of the mysql command.

7. **First add**  
   Write a script that inserts a new row in the table `first_table` (database `hbtn_0c_0`) in your MySQL server.  
   New row:  
   - id = 89  
   - name = Best School  
   The database name will be passed as an argument of the mysql command.

8. **Count 89**  
   Write a script that displays the number of records with id = 89 in the table `first_table` of the database `hbtn_0c_0` in your MySQL server. The database name will be passed as an argument of the mysql command.

9. **Full creation**  
   Write a script that creates a table `second_table` in the database `hbtn_0c_0` in your MySQL server and add multiple rows.  
   `second_table` description:  
   - id INT  
   - name VARCHAR(256)  
   - score INT  
   The database name will be passed as an argument to the mysql command. If the table `second_table` already exists, your script should not fail. You are not allowed to use the SELECT and SHOW statements. Your script should create these records:  
   - id = 1, name = “John”, score = 10  
   - id = 2, name = “Alex”, score = 3  
   - id = 3, name = “Bob”, score = 14  
   - id = 4, name = “George”, score = 8  

10. **List by best**  
    Write a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server.  
    Results should display both the score and the name (in this order). Records should be ordered by score (top first). The database name will be passed as an argument of the mysql command.

11. **Select the best**  
    Write a script that lists all records with a score >= 10 in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.  
    Results should display both the score and the name (in this order). Records should be ordered by score (top first). The database name will be passed as an argument of the mysql command.

12. **Cheating is bad**  
    Write a script that updates the score of Bob to 10 in the table `second_table`. You are not allowed to use Bob’s id value, only the name field. The database name will be passed as an argument of the mysql command.

13. **Score too low**  
    Write a script that removes all records with a score <= 5 in the table `second_table` of the database `hbtn_0c_0` in your MySQL server. The database name will be passed as an argument to the mysql command.

14. **Average**  
    Write a script that computes the score average of all records in the table `second_table` of the database `hbtn_0c_0` in your MySQL server. The result column name should be average. The database name will be passed as an argument of the mysql command.

15. **Number by score**  
    Write a script that lists the number of records with the same score in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.  
    The result should display:  
    - the score  
    - the number of records for this score with the label number  
    The list should be sorted by the number of records (descending). The database name will be passed as an argument to the mysql command.

16. **Say my name**  
    Write a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server.  
    Don’t list rows without a name value. Results should display the score and the name (in this order). Records should be listed by descending score. The database name will be passed as an argument of the mysql command.

17. **Go to UTF8**  
    Write a script that converts `hbtn_0c_0` database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.  
    You need to convert all of the following to UTF8:  
    - Database `hbtn_0c_0`  
    - Table `first_table`  
    - Field `name` in `first_table`  

18. **Temperatures #0**  
    Import in `hbtn_0c_0` database this table dump: download.  
    Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

19. **Temperatures #1**  
    Import in `hbtn_0c_0` database this table dump: download (same as Temperatures #0).  
    Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending).

20. **Temperatures #2**  
    Import in `hbtn_0c_0` database this table dump: download (same as Temperatures #0).  
    Write a script that displays the max temperature of each state (ordered by State name).
