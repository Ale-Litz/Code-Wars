#https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/train/python


def solution(string, ending):
    return bool(string[-(len(ending)):] == ending) or bool(ending == '')

---------

def solution(string, ending):
    return string.endswith(ending)
