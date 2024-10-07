n = int(input())
end = 0
somme = 0

while n != -1:
    inp = int(input())
    somme = inp + somme
    end = end + 1
    if end == n:
        break

if n == -1:
    while end != "F":
        inp = input()
        end = inp
        if inp != "F":
            try:
                inp = int(inp)
                somme = inp + somme
            except:
                break

print(somme)