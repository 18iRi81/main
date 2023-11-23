lista = [44,66,88,22,11]
def miniumum(lista):
    naj = lista[0]
    for e in lista:
        if e < naj:
            naj = e
    return naj





print('_______________________________________________________')

def czy_nalezy(lista, x):
    wynik = False
    for e in lista:
        if e == x:
           wynik = True
    return wynik


def czy_nalezy(lista, x):
    for e in lista:
        if e == x:
            return True
        return False



"""
def czy_zawieraa(lista,listaa):
    for i in listaa:
        if not czy_nalezy(lista,i):
            return False
    return True
print(czy_zawieraa(lista,listaa))
"""