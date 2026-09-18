# Write your MySQL query statement
select max(num) as num from 
(select num, count(num) as cnt from MyNumbers group by num) as t
where cnt = 1