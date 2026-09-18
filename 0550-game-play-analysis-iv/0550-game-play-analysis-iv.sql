SELECT 
    ROUND(
        COUNT(DISTINCT t.player_id) / 
        (SELECT COUNT(DISTINCT player_id) FROM Activity),
        2
    ) AS fraction
FROM (
    SELECT 
        a1.player_id,
        a1.event_date AS start_date,
        a2.event_date AS end_date
    FROM Activity a1
    JOIN Activity a2
        ON a1.player_id = a2.player_id
       AND DATEDIFF(a2.event_date, a1.event_date) = 1
    WHERE a1.event_date = (
        SELECT MIN(a3.event_date)
        FROM Activity a3
        WHERE a3.player_id = a1.player_id
    )
) t;