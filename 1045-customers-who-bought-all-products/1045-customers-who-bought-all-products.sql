# Write your MySQL query state
select customer_id from
(select customer_id,
count( distinct product_key) as cnt
from Customer
group by customer_id) as t
where t.cnt = (select count(distinct product_key) from Product);
