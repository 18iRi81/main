#zad Czy lista zawiera sie w drugiej
lista = [1,2,3,4,5,6,7,8,9,10]
listaa = [1,2,3,4,5,]
listaaa = [55,66,77,88,99]
"""
counter = 0
for i in lista:
    for j in listaa:
        if i == j:
            counter +=1
if counter >= len(listaa):
    print('1st lista zawiera sie w 2nd')
else:
    print('1st lista nie zawiera sie w 2nd')
    
"""
def czy_nalezy(lista, e):
    for i in lista:
        if i == e:
            return True
        return False



def czy_zawieraa(lista,listaa):
    for i in listaa:
        if not czy_nalezy(lista,i):
            return False
    return True
print(czy_zawieraa(lista,listaa))



print('__________________________________________________________')
#zad Czy element zawiera sie w liscie
"""
def czy_zawiera(arg):
    for i in lista:
        if arg == i:
            return True
    return False
print(czy_zawiera)
arg = 5
if arg in lista:
    print(f'{arg} nalezy')
else:
    print(f'{arg} nie nalezy')
"""




