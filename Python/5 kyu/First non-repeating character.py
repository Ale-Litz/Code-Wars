#https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/train/python

def first_non_repeating_letter(string):
    x = ''
    lista = list(string)
    listaup = list(string.upper())
    if string.lower() == string:    
        if string == '':
            x = ''
        else:
            for i in reversed(range(0,len(lista))):
                if lista.count(lista[i]) == 1:
                    x = str(lista[i])
    else:
        for i in reversed(range(0,len(listaup))):
            if listaup.count(listaup[i]) == 1:
                if str(listaup[i]) in str(lista):
                    x = str(listaup[i])
                else:
                    x = str(listaup[i])
                    x = x.lower()

    return x
