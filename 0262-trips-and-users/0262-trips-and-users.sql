select t.request_at as Day, round(count(case when t.status in ('cancelled_by_driver','cancelled_by_client') then 1 end)/count(*),2) as 'Cancellation Rate'
from Trips t join Users d on t.driver_id=d.users_id join Users c on t.client_id=c.users_id
where d.banned='No' and c.banned='No' and t.request_at between "2013-10-01" and "2013-10-03"
group by 1