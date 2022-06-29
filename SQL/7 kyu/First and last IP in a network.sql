#https://www.codewars.com/kata/5db5ff03d10bfa001da9cf2e/train/sql

SELECT
  id,
  network(ip_address) as first_address,
  broadcast(ip_address) as last_address  
FROM connections
order by id
