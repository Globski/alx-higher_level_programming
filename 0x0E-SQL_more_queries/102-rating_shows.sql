-- Lists all shows and their total ratings, sorted by rating in descending order
SELECT tv_shows.title, COALESCE(SUM(tv_show_ratings.rate), 0) AS rating
FROM tv_shows
LEFT JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.id
ORDER BY rating DESC;
