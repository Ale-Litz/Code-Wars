--https://www.codewars.com/kata/580d08b5c049aef8f900007c/train/sql

select 
  cust.customer_id as customer_id,
  cust.email as email,
  count(distinct(pay.payment_id)) payments_count,
  sum(pay.amount)::float as total_amount
from customer cust
left join payment pay on cust.customer_id = pay.customer_id
  group by cust.customer_id
  order by sum(pay.amount)::float desc
  limit 10
