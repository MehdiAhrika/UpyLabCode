
def est_adn(adn):
    for i in adn:
        if i not in "ATCG":
            return False
    if len(adn) != 0:
        return True
    else:
        return False


