
def duree(debut, fin):
    debut_minute = debut[0]*60 + debut[1]
    fin_minute = fin[0] * 60 + fin[1]
    minute = fin_minute - debut_minute
    temps_heure = minute // 60
    temps_minute = minute % 60
    if fin_minute < debut_minute:
        temps_heure += 24
    return temps_heure, temps_minute
