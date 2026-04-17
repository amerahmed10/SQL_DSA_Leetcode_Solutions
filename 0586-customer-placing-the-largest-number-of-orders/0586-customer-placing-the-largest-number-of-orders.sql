# Write your MySQL query statement below
with ans as (select customer_number, count(*) ct
from Orders
group by customer_number
order by ct desc
limit 1)

select customer_number
from ans