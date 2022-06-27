#https://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/python

from itertools import permutations as permut
def permutations(string):
    result = set()

    result.update("".join(r) for r in permut(string, len(string)))

    return result
