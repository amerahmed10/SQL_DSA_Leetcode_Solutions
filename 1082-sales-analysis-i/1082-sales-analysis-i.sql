# Write your MySQL query statement below
with total_added as (select seller_id, sum(price) as total
from Sales
group by seller_id),

ranked as (select seller_id , dense_rank() over(order by total desc) as rk from total_added)

select seller_id
from ranked
where rk=1