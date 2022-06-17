#https://www.codewars.com/kata/5a8d2bf60025e9163c0000bc/train/python

import collections

def solve(arr):
    count = collections.Counter(arr)
    arr.sort(key = lambda x:(-count[x], x))
    return arr
