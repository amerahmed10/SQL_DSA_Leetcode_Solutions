# Write your MySQL query statement below
select player_id, device_id
from Activity a
where event_date = (select min(event_date) from Activity where a.player_id=player_id)