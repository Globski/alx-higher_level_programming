-- Create table unique_id with id and name columns, id must be unique
CREATE TABLE IF NOT EXISTS `unique_id` (
    `id`   INT          DEFAULT 1 UNIQUE,
    `name` VARCHAR(256)
);
