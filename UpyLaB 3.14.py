import random
r = random.randint(0, 100)
answer = int(input())
n_essai = 0
while r != answer and n_essai < 5:
    n_essai = n_essai + 1

    if answer < r:
        print('Trop petit')
    elif answer > r:
        print('Trop grand')

    answer = int(input())

if answer == r:
    print('Gagné en {} essai(s) !'.format(n_essai))
else:
    print('Perdu ! Le secret était nombre '+ str(r))