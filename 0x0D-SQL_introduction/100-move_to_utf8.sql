-- Convert hbtn_0c_0 database, first_table table, and name field to UTF8

-- Convert database to UTF8
USE hbtn_0c_0
ALTER DATABASE hbtn_0c_0
CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Convert table to UTF8
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert field to UTF8
ALTER TABLE first_table MODIFY name VARCHAR(256)
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
