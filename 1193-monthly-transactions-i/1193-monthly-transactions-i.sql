# Write your MySQL query statement below
select month,
country,
COUNT(id) as trans_count,
COUNT(CASE WHEN state = 'approved' THEN 1 END) as approved_count,
SUM(amount) as trans_total_amount,
SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) as approved_total_amount 
from 
(select * , DATE_FORMAT(trans_date, '%Y-%m') as month from Transactions) t
group by month, country;