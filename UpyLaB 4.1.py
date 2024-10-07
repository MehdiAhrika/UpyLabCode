


def Is_same(a, b, c):
    if a == b or a == c or c == b:
        return True
    else:
        return False

a = int(input())
b = int(input())
c = int(input())

print(Is_same(a, b ,c))
