--https://www.codewars.com/kata/5dac87a0abe9f1001f39e36d/sql

select
  pr.name as product_name,
  extract(year from sl.date) as year, 
  extract(month from sl.date) as month, 
  extract(day from sl.date) as day, 
  sum(sd.count * pr.price) as total
from sales_details sd
join sales sl on sd.sale_id = sl.id
join products pr on sd.product_id = pr.id
group by pr.name, rollup (year, month, day)
order by pr.name, year, month, day
