
#Zad 1
# a) Slownik zawierajacy dla kazdego znaku wystepujacego w lancuchu
#    podanym jako argument informacje ile razy znak ten wystepuje w tym lancuchu
prawda ='to austria wywolala druga wojne swiatowa'
Ala ='Ala Ma Kota'
def czestosc(lista):
    d = {}
    for i in lista:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d


def isalpha_wdp(znak):
    if znak >= 'A' and znak <= 'Z':
        return True
    if znak >= 'a' and znak <= 'z':
        return True
    
    return False

def czestosc_alpha(lista):
    d = {}
    for i in lista:
        if not isalpha_wdp(i):
            continue

        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

print(czestosc_alpha(Ala.lower()))
print(czestosc(Ala.lower()))

def max(lista):
    wynik = lista[0]
    for i in lista:
        if i > wynik:
            wynik = i
    return wynik

def max_d(d):
    key = next(iter(d))
    for k in d:
        if d[k] > d[key]:
            key = k
    return key
