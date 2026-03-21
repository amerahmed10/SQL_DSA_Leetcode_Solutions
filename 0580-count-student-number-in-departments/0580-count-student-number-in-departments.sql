# Write your MySQL query statement below
select d.dept_name, count(distinct s.student_id) as student_number
from Student s right join Department d using(dept_id)
group by 1
order by 2 desc,1 