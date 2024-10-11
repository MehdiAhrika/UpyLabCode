

def rendre_monnaie(prix, x20, x10, x5, x2, x1):
    somme_monnaie = x20*20 + x10*10 + x5*5 + x2*2 + x1
    monnaie_rendre = [0, 0, 0, 0, 0]
    if somme_monnaie == prix:
        monnaie_rendre = [0, 0, 0, 0, 0]
        return monnaie_rendre
    elif somme_monnaie > prix:
        surplus = somme_monnaie - prix
        if surplus >= 20:
            monnaie_rendre[0] = surplus // 20
            surplus = surplus % 20
        if surplus >= 10:
            monnaie_rendre[1] = surplus // 10
            surplus = surplus % 10
        if surplus >= 5:
            monnaie_rendre[2] = surplus // 5
            surplus = surplus % 5
        if surplus >= 2:
            monnaie_rendre[3] = surplus // 2
            surplus = surplus % 2
        if surplus >= 1:
            monnaie_rendre[4] = surplus // 1
            surplus = surplus % 1
    else:
        return (None, None, None, None, None)

    return tuple(monnaie_rendre)

print(rendre_monnaie(80, 2 , 2, 2, 3, 3))