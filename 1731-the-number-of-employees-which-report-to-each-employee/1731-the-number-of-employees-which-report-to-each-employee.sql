# Write your MySQL query statement below
select e1.employee_id as employee_id,
e1.name as name,
count(e2.employee_id) as reports_count,
ROUND(avg(e2.age)) as average_age
from Employees e1
join Employees e2
on e1.employee_id= e2.reports_to
group by employee_id,name
order by employee_id;
