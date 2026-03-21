# Write your MySQL query statement below
with tab1 as (select question_id, count(case when answer_id is not null then 1 end) as ans, count(case when action='show' then 1 end) as shw
from SurveyLog
group by 1),

tab2 as (select question_id, ans/shw as ans_rate
from tab1
order by ans_rate desc, question_id
limit 1)

select question_id as survey_log 
from tab2
