# Write your MySQL query statement below
with emails as (select email, count(email) as ct
from Person
group by 1
having ct>1)

select email
from emails