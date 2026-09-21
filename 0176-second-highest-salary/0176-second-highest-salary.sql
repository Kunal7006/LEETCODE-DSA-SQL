# Write your MySQL query statement below
select MAX(salary) as SecondHighestSalary
from (select
salary,
DENSE_RANK() OVER(order by salary desc) as rn
from Employee) t
where t.rn =2

