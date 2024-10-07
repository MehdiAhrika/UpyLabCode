
nb_oeuf = 3
nb_Chocolat = 100
nb_sv = 1
nb_Prsn = 4

nb_oeuf = nb_oeuf / nb_Prsn
nb_Chocolat = nb_Chocolat / nb_Prsn
nb_sv = nb_sv / nb_Prsn

nb_prsn = float(input("pour combien de personne voulez-vous? "))

nb_oeuf = int(nb_oeuf * nb_prsn)
nb_Chocolat = int(nb_Chocolat * nb_prsn)
nb_sv = int(nb_sv * nb_prsn)

print('il vous faut, '+str(nb_oeuf)+' oeufs, '+str(nb_Chocolat)+' grammes de chocolat, '+str(nb_sv)+' Sachet de sucre vanillé')
