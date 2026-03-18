# Write your MySQL query statement below
with grouped as (select num,id-rank() over(partition by num order by id) as grp
from Logs),

grouped_ct as (select num,count(num) as cons_ct
from grouped
group by num,grp)

select distinct num as ConsecutiveNums
from grouped_ct
where cons_ct>2