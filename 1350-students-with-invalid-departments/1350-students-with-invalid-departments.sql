# Write your MySQL query statement below
select distinct id, name
from students
where department_id not in (select id from departments)
