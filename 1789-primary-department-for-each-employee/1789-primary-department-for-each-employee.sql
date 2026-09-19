# Write your MySQL query statement below

select
e1.employee_id as employee_id,
e1.department_id as department_id
from
Employee e1
join (select employee_id,COUNT(department_id) as cnt from Employee group by employee_id) as e2
on e1.employee_id = e2.employee_id
where e1.primary_flag in('Y') or e2.cnt =1
group by employee_id;

