
def premier(user_input):
    is_premier = 0
    for i in range(2, user_input):
        is_premier = user_input % i
        if is_premier == 0:
            return False
    return True


user_input = int(input())

for i in range(2, user_input):
    if premier(i):
        print(i)


