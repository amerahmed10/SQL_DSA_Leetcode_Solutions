# Write your MySQL query statement below
with ranked as (select *, rank() over(partition by player_id order by event_date) as rk
from Activity)

select round((select count(distinct player_id)
from ranked
where rk<3 and (player_id,event_date) in (select player_id,date_add(event_date,interval 1 day) from ranked))/count(distinct player_id),2) as fraction from ranked