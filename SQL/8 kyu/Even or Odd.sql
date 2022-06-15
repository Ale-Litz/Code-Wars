--https://www.codewars.com/kata/53da3dbb4a5168369a0000fe/solutions/sql


SELECT 
  CASE 
    WHEN (number % 2) = 0 THEN 'Even'
    ELSE 'Odd'
  END is_even
FROM numbers
