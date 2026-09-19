# Write your MySQL query statement below

(select u.name as results
from 
MovieRating m join Users u
on m.user_id = u.user_id
group by u.name
order by count(m.movie_id) desc,
u.name asc
limit 1)
UNION ALL
(SELECT m.title AS results
    FROM MovieRating r
    JOIN Movies m
        ON r.movie_id = m.movie_id
    WHERE r.created_at >= '2020-02-01'
      AND r.created_at < '2020-03-01'
    GROUP BY m.movie_id, m.title
    ORDER BY AVG(r.rating) DESC, m.title ASC
    LIMIT 1);



