#https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python

def duplicate_count(text):
    text = text.lower()
    result = []
    maxi = 0
    for i in text:
        count = text.count(i)
        if (count > 1) and (i not in result):
            result.append(i)
            maxi += 1
    return maxi
