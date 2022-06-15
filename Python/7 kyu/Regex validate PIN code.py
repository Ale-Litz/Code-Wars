#https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/python


def validate_pin(pin):
    quatro = (len(pin) == 4)
    seis = (len(pin) == 6)
    enumero = (pin.isnumeric())
    return ((quatro or seis) and enumero)

    ---------
 
def validate_pin(pin):
    etamanho = (len(pin) in (4,6))
    enumero = (pin.isnumeric())
    return (etamanho and enumero)

    ---------

def validate_pin(pin):
    import re
    return bool(re.fullmatch("\d{4}|\d{6}", pin))
