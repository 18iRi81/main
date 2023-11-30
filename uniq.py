lista = [1, 2, 3, 2, 4, 6, 7, 6, 8]
def uniq(lista):
    uniqlista = []
    for i in lista:
        if i not in uniqlista:
            uniqlista.append(i)
    return uniqlista
print(uniq(lista))

print('___________________________')

#liczba pierwsza(ma tylko dwa dzielniki 1 i siebie)


liczba = 7 #dzielniki to 1,2,3,6
def dzielniki(liczba):
    wynik = []
    for i in range(1, int(liczba/2+1)):
        if liczba % i == 0:
            wynik.append(i)
        wynik.append(liczba)
    return wynik



def sza(liczba):
    if liczba < 1:
        return False
    d = dzielniki(liczba)
    return len(d) == 2
print(sza(liczba))

"""
def dzielniki(liczba, zliczba=True):
    wynik = []
    for i in range(1, int(liczba/2+1)):
        if liczba % i == 0:
            wynik.append(i)
    if zliczba:
        wynik.append(liczba)
    return wynik
"""
