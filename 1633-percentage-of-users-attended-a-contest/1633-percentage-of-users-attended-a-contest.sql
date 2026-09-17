# Write your MySQL query statement below
select r.contest_id as contest_id,
ROUND(count(r.user_id) * 100/ (Select count(*) from Users) , 2) as percentage
from Register r 
left join Users u
on r.user_id = u.user_id
group by contest_id
order by percentage desc,
contest_id asc;
