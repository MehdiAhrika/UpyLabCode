n = int(input())
end = 0
somme = 0


if n != -1:
    for i in range(n):
        inp = int(input())
        somme = inp + somme

if n == -1:
    inp = input()
    while inp != "F":
        somme = int(inp) + somme
        inp = input()


print(somme)
