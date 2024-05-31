-- Displays the 3 cities with the highest average temperatures between July and August. 
-- ordered by temperature (descending)

SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
WHERE MONTH(date) IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
