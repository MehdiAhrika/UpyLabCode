

def bat(joueur_1, joueur_2):
    if (joueur_1 == 0 and joueur_2 == 2) or (joueur_1 == 1 and joueur_2 == 0) or (joueur_1 == 2 and joueur_2 == 1):
        return True
    else:
        return False
