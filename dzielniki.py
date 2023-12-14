liczba = int(input("podaj liczbe"))
def dzielniki():
    lista = []
    for i in range(1, liczba +1):
        if liczba % i == 0:
            lista.append(i)
    return lista
print(dzielniki())
print("^dzielniki^")
def sza():
    if liczba <= 1 :
        return False
    d = dzielniki()
    if len(d) == 2:
        return True
    else: return False
    # return len(d) == 2
print(sza())
print("^czy pierwsza^")
def suma():
    sum = 0
    d = dzielniki()
    for i in d:
        sum += i
    return sum
print(suma())
print("^suma dzielnikow^")
def doskonala():
    s = suma()
    return s - liczba == liczba
print(doskonala())
print("^czy doskonala^")