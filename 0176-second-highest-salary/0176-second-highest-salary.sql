# Write your MySQL query statement below
with ranked as (select salary, dense_rank() over(order by salary desc) as rk from Employee)

select max(salary) as SecondHighestSalary
from ranked
where rk=2