#https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9/train/python

def number(lines):
    result = []
    count = 1
    for i in lines:
        if type(i) == str:
            x = str(count) + ': ' + i
            result.append(x)
        count += 1
    return result
  
  ----------
  
  def number(lines):
    return [f"{counter}: {line}" for counter, line in enumerate(lines, start=1)]
