numero_joueur = int(input())
numero_tirage = int(input())


if 0 <= numero_joueur <= 12 :
    if numero_tirage is numero_joueur:
        print(120)
    else:
        print(0)

elif numero_joueur == 13:
    if numero_tirage%2 == 0:
        print(20)
    else:
        print(0)

elif numero_joueur == 14:
    if numero_tirage%2 != 0:
        print(20)
    else:
        print(0)

elif numero_joueur == 15:
    if numero_tirage in (1,3,5,7,9,12):
        print(20)
    else:
        print(0)

elif numero_joueur == 16:
    if numero_tirage in (2, 4, 6, 8, 10,11):
        print(20)
    else:
        print(0)
