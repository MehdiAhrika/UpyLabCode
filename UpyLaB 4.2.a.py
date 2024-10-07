
def soleil_leve(lever, coucher, actuel ):
    if lever == 12 and coucher == 12:
        return False
    elif lever == 0 and coucher == 0:
        return True

    if lever > coucher:
        if actuel >= lever or actuel <= coucher:
            return True
        else:
            return False

    if lever < coucher:
        if lever <= actuel <= coucher:
            return True
        else:
            return False







lever = int(input())
coucher = int(input())
actuel = int(input())

print(soleil_leve(lever, coucher, actuel))