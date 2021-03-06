--https://www.codewars.com/kata/526989a41034285187000de4/sql

select
  cast(id as int) id,
  ( 
    (((cast(substring(last from '[0-9]+') as bigint)) - (cast(substring(first from '[0-9]+') as bigint)))*16777216)+
    (((cast(translate(substring(last from '[.][0-9]+[.]'), '.','') as bigint)) - (cast(translate(substring(first from '[.][0-9]+[.]'), '.','') as bigint)))*65536)+
    (((cast(replace(substring(last from '[.][0-9]{1,3}[.][0-9]{1,3}'), substring(last from '[.][0-9]{1,3}[.]'),'') as bigint)) - (cast(replace(substring(first from '[.][0-9]{1,3}[.][0-9]{1,3}'), substring(first from '[.][0-9]{1,3}[.]'),'') as bigint)))*256)+
    (cast(substring(last from '[0-9]+$') as bigint)) - (cast(substring(first from '[0-9]+$') as bigint))
  ) ips_between
--  first,
--  last
from ip_addresses;

----------

SELECT id, last::inet - first::inet as ips_between
FROM ip_addresses;

----------

SELECT id
        ,((SPLIT_PART(last, '.',  1)::bigint - SPLIT_PART(first, '.',  1)::int)*256^3
        + (SPLIT_PART(last, '.',  2)::int    - SPLIT_PART(first, '.',  2)::int)*256^2
        + (SPLIT_PART(last, '.',  3)::int    - SPLIT_PART(first, '.',  3)::int)*256^1
        + (SPLIT_PART(last, '.',  4)::int    - SPLIT_PART(first, '.',  4)::int)*256^0)::bigint AS ips_between
FROM ip_addresses;
