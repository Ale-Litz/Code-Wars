#https://www.codewars.com/kata/5287e858c6b5a9678200083c/train/python

def narcissistic( value ):
    
    sum = 0
    stri = str(value)
    divi = list(stri)
    
    for i in divi:
        sum += pow(int(i),len(divi))
        if sum == value:
            res = True
        else:
            res = False
    return res
