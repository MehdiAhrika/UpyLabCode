from random import randint, seed


def alea_dice(s):
    seed(s)
    de1 = randint(1, 6)
    de2 = randint(1, 6)
    de3 = randint(1, 6)
    de_list = [de1, de2, de3]
    if 4 in de_list and 2 in de_list and 1 in de_list:
        return True
    else:
        return False
