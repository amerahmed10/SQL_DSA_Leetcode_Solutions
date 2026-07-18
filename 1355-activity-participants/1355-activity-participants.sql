# Write your MySQL query statement below
with cnt as (select activity, count(activity) as ct
from Friends
group by activity),

maxmin as (select activity from cnt where ct in (select max(ct) from cnt) or ct in (select min(ct) from cnt))

select name as activity
from Activities
where not exists (select 1 from maxmin where maxmin.activity = Activities.name)