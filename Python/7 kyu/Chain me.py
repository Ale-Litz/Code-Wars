#https://www.codewars.com/kata/54fb853b2c8785dd5e000957/train/python

def add10(x): return x + 10
def mul30(x): return x * 30

def chain(init_val, functions):
    x = init_val
    for i in functions:
        x = i(x)
    return x
