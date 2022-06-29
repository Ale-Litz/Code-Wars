#https://www.codewars.com/kata/53d40c1e2f13e331fc000c26/train/python

from gmpy2 import fib as fibb
def fib(n):
    if n < 0:
        if n % 2 == 0:
            return -fibb(-n)
        else:
            return fibb(-n)
    else:
        return fibb(n)
