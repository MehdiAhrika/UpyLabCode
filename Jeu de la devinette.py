import random

answer = "x"
secret_number = "y"
tryinput = False

while secret_number != answer:
    secret_number = int(random.randint(1, 5))

    while tryinput == False:
        try:
         answer = int(input("devinez le nombre entre 1 et 5 ?\n "))
        except ValueError:
            print("Entrez un nombre valide et non une chaine de caractére !")
        else:
            tryinput = True
    if answer == secret_number:
        print("vous avez gagné(e) !")
        break
    else:
        print("votre réponse est fausse ! \n réessayez ")
