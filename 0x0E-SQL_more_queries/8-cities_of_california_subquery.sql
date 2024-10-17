-- This script lists all the cities in California from the database hbtn_0d_usa.
-- It retrieves cities where the state_id corresponds to California's id.
-- Results are sorted in ascending order by cities.id.

SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
