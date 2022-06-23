#https://www.codewars.com/kata/523f5d21c841566fde000009/train/python

def array_diff(a, b):
    res = []
    for i in a:
        if i not in b:
            res.append(i)
    return res
