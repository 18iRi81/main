"""
a = float(input("podaj liczbe zmiennoprzecinkowa: "))
if a > 0:
    print(a)
elif a < 0:
    a *= -1
    print(a)
"""
print('_________________________')
"""
def sgn(x):
    znak = -1
    if x > 0:
        znak = 1
    elif x == 0:
        znak = 0
    print(f'znak argumentu to {znak}')

def main():
    x = float(input('podaj liczbe: '))
    return sgn(x)

main()
"""
print('_________________________')

a = float(input('podaj liczbe zmiennoprzecinkowa a: '))
b = float(input('podaj liczbe zmiennoprzecinkowa b: '))
z = 0
if b != 0:
    z = a/b
else:
    print('dzielenie niemozliwe')
print(z)
