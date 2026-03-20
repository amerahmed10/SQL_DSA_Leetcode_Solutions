# Write your MySQL query statement below
with names as (select m.id,m.name,count(distinct e.id) ct
from Employee m join Employee e on m.id=e.managerId
group by 1,2
having  ct>4)

select name
from names
