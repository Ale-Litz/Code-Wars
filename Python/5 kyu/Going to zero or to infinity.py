#https://www.codewars.com/kata/55a29405bc7d2efaff00007c/train/python

def going(n):
    fs = 0
    nf = 1
    for i in range(1,n+1):
        nf *= i
        fs += nf
    a = str(int.__truediv__(fs,nf))
    i = a.find('.')
    if len(a[i+1:]) > 6:
        a = a[:i+7]
    return float(a)
