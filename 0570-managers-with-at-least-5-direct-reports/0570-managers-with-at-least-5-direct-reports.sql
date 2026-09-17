# Write your MySQL query statement below
select e1.name as name
from Employee e1 
left join employee e2
on e1.id = e2.managerId
group by e1.id,name
having count(e2.id)>=5
order by name;
