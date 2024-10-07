
i = 0
total = 0
diviseur = 0

while True:
    user_input = int(input())

    if user_input != -1:
        total = total + user_input
        diviseur = diviseur + 1
    else:
        break

print(total/diviseur)