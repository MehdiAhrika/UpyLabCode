
def soleil_leve(lever, coucher, actuel ):
    if lever == 12 and coucher == 12:
        return False
    elif lever == 0 and coucher == 0:
        return True

    if lever > coucher:
        if actuel >= lever or actuel < coucher:
            return True
        else:
            return False

    if lever < coucher:
        if lever <= actuel < coucher:
            return True
        else:
            return False


lever_E1515 = int(input())
coucher_E1515 = int(input())

lever_E666 = int(input())
coucher_E666 = int(input())

for actuel in range(24):
    E1515 = soleil_leve(lever_E1515, coucher_E1515, actuel)
    E666 = soleil_leve(lever_E666, coucher_E666, actuel)
    if E1515 == False and E666 == False:
        print(str(actuel) + "*")
    else:
        print(actuel)