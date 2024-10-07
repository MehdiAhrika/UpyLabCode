from math import sqrt

name = input()
a = float(input())

if name == 'T':
    volume = (sqrt(2)/12)*a**3
    print(volume)
elif name == "C":
    volume = a ** 3
    print(volume)
elif name == "O":
    volume = (sqrt(2) / 3) * a ** 3
    print(volume)
elif name == "D":
    volume = (15 + 7 * sqrt(5)) / 4 * a ** 3
    print(volume)
elif name == "I":
    volume = (5 * (3 + sqrt(5)) / 12) * a ** 3
    print(volume)
else:
    print('Polyèdre non connu')

