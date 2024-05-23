-- Lists all records with a score >= 10 from second_table records are ordered by score in descending order
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;

