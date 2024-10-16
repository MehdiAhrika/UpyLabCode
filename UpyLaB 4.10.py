from random import randint, seed


s = int(input())
seed(s)

PIERRE = 0
FEUILLE = 1
CISEAUX = 2
points = 0
name_cj = None
name_cia = None


def pfc(choice_j, choice_ia):
    global name_cj, name_cia

    if choice_j == PIERRE:
        name_cj = "Pierre"
    elif choice_j == FEUILLE:
        name_cj = "Feuille"
    elif choice_j == CISEAUX:
        name_cj = "Ciseaux"

    if choice_ia == PIERRE:
        name_cia = "Pierre"
    elif choice_ia == FEUILLE:
        name_cia = "Feuille"
    elif choice_ia == CISEAUX:
        name_cia = "Ciseaux"

    if choice_j == PIERRE and choice_ia == CISEAUX:
        return 1
    elif choice_j == FEUILLE and choice_ia == PIERRE:
        return 1
    elif choice_j == CISEAUX and choice_ia == FEUILLE:
        return 1
    if choice_ia == PIERRE and choice_j == CISEAUX:
        return -1
    elif choice_ia == FEUILLE and choice_j == PIERRE:
        return -1
    elif choice_ia == CISEAUX and choice_j == FEUILLE:
        return -1
    elif choice_ia == choice_j:
        return 0






for i in range(5):
    coup_ia = randint(0, 2)
    coup_joueur = int(input())
    resultat = pfc(coup_joueur, coup_ia)
    points += resultat

    if resultat == 1:
        print(f"{name_cj} bat {name_cia} : {points}")
    elif resultat == -1:
        print(f"{name_cj} est battu par {name_cia} : {points}")
    else:
        print(f"{name_cj} annule {name_cia} : {points}")


if points > 0:
    print("gagné")
elif points == 0:
    print("Nul")
else:
    print("Perdu")


