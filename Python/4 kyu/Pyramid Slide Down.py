#https://www.codewars.com/kata/551f23362ff852e2ab000037/train/python

def longest_slide_down(pyramid):
    if len(pyramid) == 1:
        return pyramid[0][0]

    ultimo = pyramid[-1]
    novo = []
    for i in range(1, len(ultimo)):
        novo.append(max(ultimo[i], ultimo[i-1]))
    
    pyramid[-2] = [a+b for a, b in zip(pyramid[-2], novo)]
    
    return longest_slide_down(pyramid[:-1])
