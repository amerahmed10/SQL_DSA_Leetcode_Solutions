# Write your MySQL query statement below
with ranked as (select name, salary, departmentId, dense_rank() over(partition by departmentId order by salary desc) as rk
from Employee)

select d.name as Department, r.name as Employee, r.salary as Salary
from ranked r join Department d on r.departmentId=d.id
where r.rk<4
