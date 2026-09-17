# Write your MySQL query statement below
select s.user_id as user_id,
ROUND(COALESCE(count(CASE WHEN c.action = 'confirmed' THEN  1 END)/count(c.action),0),2) as confirmation_rate
from Signups s
left join Confirmations c
on s.user_id = c.user_id
group by user_id;