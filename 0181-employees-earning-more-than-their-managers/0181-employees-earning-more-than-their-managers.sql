# Write your MySQL query statement below
select e.name as Employee
from Employee m join Employee e on m.id=e.managerId
where m.salary<e.salary