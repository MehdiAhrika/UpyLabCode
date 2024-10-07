user_answer = 0
answer = 42
while user_answer != answer:
   user_answer = int(input("Combien de plis sont-ils nécessaires pour se rendre sur la Lune ? : "))
   if user_answer == answer:
      print('Bravo !')
   else:
      print('Mauvaise réponse.')
