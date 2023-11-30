lista = [12, 3, 43,66, 77, 44, ]
def min(lista):
    a = lista[0]
    for i in lista:
        if i < a:
            a = i
    return a

print(min(lista))

print('___')

def max(lista):
    a = lista[0]
    for i in lista:
        if i > a:
            a = i
    return a
print(max(lista))
