-- Lists all cities in California from the database hbtn_0d_usa
-- The states table is queried to find the state_id for California,
-- then used to select cities with that state_id, sorted by city id.
SELECT * FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
