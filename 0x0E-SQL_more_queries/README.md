# High-Level Programming - SQL More queries

This project focuses on advanced SQL queries, including creating users, granting privileges, using various constraints, and retrieving data from multiple tables using different techniques.

## Project Structure

| Task Number | Task Description                              | Source Code                |
|-------------|-----------------------------------------------|----------------------------|
| 0           | List all privileges of MySQL users.           | [0-privileges.sql](./0-privileges.sql)       |
| 1           | Create MySQL user `bob@localhost`.            | [1-create_user.sql](./1-create_user.sql)     |
| 2           | Create MySQL user `bob@localhost` with SELECT privileges. | [2-create_read_user.sql](./2-create_read_user.sql) |
| 3           | Create MySQL user `bob@localhost` with the name `Bob`. | [3-force_name.sql](./3-force_name.sql)       |
| 4           | List all privileges of MySQL user `bob@localhost`. | [4-needs_privileges.sql](./4-needs_privileges.sql) |
| 5           | Grant SELECT privilege to `bob@localhost` for the database `hbtn_0d_2`. | [5-grant_privileges.sql](./5-grant_privileges.sql) |
| 6           | Revoke all privileges for `bob@localhost` on the database `hbtn_0d_2`. | [6-revoke_privileges.sql](./6-revoke_privileges.sql) |
| 7           | List all MySQL users and their privileges.    | [7-who_needs_what.sql](./7-who_needs_what.sql)   |
| 8           | List all MySQL users who do not have any privileges. | [8-no_privileges.sql](./8-no_privileges.sql)   |
| 9           | List the number of records in the table `tv_shows` of `hbtn_0d_tvshows`. | [9-aggregate.sql](./9-aggregate.sql)       |
| 10          | List the number of records in the table `tv_shows` and order them by `genre`. | [10-aggregate_order.sql](./10-aggregate_order.sql) |
| 11          | List the average rating of shows in the table `tv_shows`. | [11-average.sql](./11-average.sql)        |
| 12          | List the average rating of each genre in the table `tv_shows`. | [12-average_score.sql](./12-average_score.sql)  |
| 13          | Count the number of shows in each genre in the table `tv_shows`. | [13-count.sql](./13-count.sql)          |
| 14          | List the highest score of each genre in the table `tv_shows`. | [14-top_score.sql](./14-top_score.sql)      |
| 15          | List the top three highest scoring shows of each genre in the table `tv_shows`. | [15-best_scores.sql](./15-best_scores.sql)    |
| 16          | List all shows and their genres in the database `hbtn_0d_tvshows`. | [16-shows_by_genre.sql](./16-shows_by_genre.sql) |
| 17          | List all genres not liked by the user `1` in the database `hbtn_0d_tvshows`. | [100-not_my_genres.sql](./100-not_my_genres.sql) |
| 18          | List all shows that are not comedies in the database `hbtn_0d_tvshows`. | [101-not_a_comedy.sql](./101-not_a_comedy.sql)  |
| 19          | List all shows with a rating greater than 8 in the database `hbtn_0d_tvshows`. | [102-rating_shows.sql](./102-rating_shows.sql)  |
| 20          | List all genres with an average rating greater than 8 in the database `hbtn_0d_tvshows`. | [103-rating_genres.sql](./103-rating_genres.sql) |


## Environment

- OS: Ubuntu 20.04 LTS
- MySQL version: 8.0.25

## Learning Objectives
After completing this project, you should be able to:

- How to create a new MySQL user
- How to manage privileges for a user to a database or table
- The concepts of PRIMARY KEY and FOREIGN KEY
- How to use NOT NULL and UNIQUE constraints
- How to retrieve data from multiple tables in one request
- The use of subqueries
- The use of JOIN and UNION

## Requirements

- All SQL keywords should be in uppercase (e.g., SELECT, WHERE)

## How to Use

### Install MySQL 8.0 on Ubuntu 20.04 LTS

```bash
$ sudo apt update
$ sudo apt install mysql-server
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
```

### Connect to the MySQL server

```bash
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> quit
Bye
```


### Use “container-on-demand” to run MySQL

- In the container, credentials are `root/root`
- Start MySQL before running commands:

```bash
$ service mysql start
* Starting MySQL database server mysqld
```

## Run the scripts

1. Ensure MySQL server is running.
2. Use the following command to execute each script:

```bash
$ cat FILENAME.sql | mysql -uroot -p
```

Replace `FILENAME.sql` with the name of the script you want to run.

## Tasks

### 0. My privileges!

Write a script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (in localhost).

**File:** `0-privileges.sql`

### 1. Root user

Write a script that creates the MySQL server user `user_0d_1` with all privileges.
- If the user user_0d_1 already exists, your script should not fail

**File:** `1-create_user.sql`

### 2. Read user

Write a script that creates the database `hbtn_0d_2` and the user `user_0d_2` with only SELECT privilege on the database.
- If the database hbtn_0d_2 already exists, your script should not fail
- If the user user_0d_2 already exists, your script should not fail

**File:** `2-create_read_user.sql`

### 3. Always a name

Write a script that creates the table `force_name` on your MySQL server with the following columns:
- `id` INT
- `name` VARCHAR(256) NOT NULL

- The database name will be passed as an argument of the mysql command
- If the table force_name already exists, your script should not fail

**File:** `3-force_name.sql`

### 4. ID can't be null

Write a script that creates the table `id_not_null` on your MySQL server with the following columns:
- `id` INT DEFAULT 1
- `name` VARCHAR(256)
- The database name will be passed as an argument of the mysql command
- If the table id_not_null already exists, your script should not fail

**File:** `4-never_empty.sql`

### 5. Unique ID

Write a script that creates the table `unique_id` on your MySQL server with the following columns:
- `id` INT DEFAULT 1 UNIQUE
- `name` VARCHAR(256)

**File:** `5-unique_id.sql`

### 6. States table

Write a script that creates the database `hbtn_0d_usa` and the table `states` with the following columns:
- `id` INT AUTO_INCREMENT PRIMARY KEY
- `name` VARCHAR(256) NOT NULL

**File:** `6-states.sql`

### 7. Cities table

Write a script that creates the table `cities` in the database `hbtn_0d_usa` with the following columns:
- `id` INT AUTO_INCREMENT PRIMARY KEY
- `state_id` INT NOT NULL (FOREIGN KEY referencing `id` of the `states` table)
- `name` VARCHAR(256) NOT NULL

**File:** `7-cities.sql`

### 8. Cities of California

Write a script that lists all the cities of California that can be found in the database `hbtn_0d_usa`.

**File:** `8-cities_of_california_subquery.sql`

### 9. Cities by States

Write a script that lists all cities contained in the database `hbtn_0d_usa`, displaying `cities.id`, `cities.name`, and `states.name`.

**File:** `9-cities_by_state_join.sql`

### 10. Genre ID by show

Import the database dump from `hbtn_0d_tvshows` and write a script that lists all shows that have at least one genre linked.

**File:** `10-genre_id_by_show.sql`

### 11. Genre ID for all shows

Import the database dump from `hbtn_0d_tvshows` and write a script that lists all shows, including those without a genre.

**File:** `11-genre_id_all_shows.sql`

### 12. No genre

Write a script that lists all shows contained in the database `hbtn_0d_tvshows` without any genre linked.

**File:** `12-no_genre.sql`

### 13. Number of shows by genre

Write a script that lists the number of shows by genre in the database `hbtn_0d_tvshows`.

**File:** `13-count_shows_by_genre.sql`

### 14. Top rated shows

Write a script that lists the top 10 highest-rated shows in the database `hbtn_0d_tvshows`.

**File:** `14-top_rated_shows.sql`

### 15. Shows by genre

Write a script that lists the number of shows for each genre in the database `hbtn_0d_tvshows`.

**File:** `15-shows_by_genre.sql`

### 16. Shows and genres

Write a script that lists all shows and their genres in the database `hbtn_0d_tvshows`.

**File:** `16-shows_and_genres.sql`

### 17. Genres not liked

Write a script that lists all genres not liked by the user `1` in the database `hbtn_0d_tvshows`.

**File:** `100-not_my_genres.sql`

### 18. Not a comedy

Write a script that lists all shows that are not comedies in the database `hbtn_0d_tvshows`.

**File:** `101-not_a_comedy.sql`

### 19. Highly rated shows

Write a script that lists all shows with a rating greater than 8 in the database `hbtn_0d_tvshows`.

**File:** `102-rating_shows.sql`

### 20. Highly rated genres

Write a script that lists all genres with an average rating greater than 8 in the database `hbtn_0d_tvshows`.

**File:** `103-rating_genres.sql`
