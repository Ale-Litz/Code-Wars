--https://www.codewars.com/kata/5942b066db68b6f35f000084

select project, commits, contributors, translate(address,'1234567890','!!!!!!!!!!') address
from repositories

----------

select project, commits, contributors, regexp_replace(address,'[0-9]','!','g') address
from repositories
