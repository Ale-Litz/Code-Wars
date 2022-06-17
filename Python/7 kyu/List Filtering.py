#https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python

def filter_list(l):
    result = []
    for i in l:
        if type(i) == int:
            result.append(i)
    return result
  
  ----------
  
  def filter_list(l):
  return [i for i in l if not isinstance(i, str)]
