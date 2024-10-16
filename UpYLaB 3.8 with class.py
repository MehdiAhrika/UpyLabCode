from math import sqrt

name = input()
a = float(input())

class Volume:
    def __int__(self, name, a):
        self.name = name
        self.a = a

    def T(self, name, a):
        volume = (sqrt(2) / 12) * a ** 3
        return volume

    def C(self, name, a):
        volume = a ** 3
        return volume

    def O(self, name, a):
        volume = (sqrt(2) / 3) * a ** 3
        return volume

    def D(self, name, a):
        volume = (15 + 7 * sqrt(5)) / 4 * a ** 3
        return volume

    def I(self, name, a):
        volume = (5 * (3 + sqrt(5)) / 12) * a ** 3
        return volume



vol = Volume()

figures = {
    'T': vol.T,
    'C': vol.C,
    'O': vol.O,
    'D': vol.D,
    'I': vol.I
}

if name in figures:
    calulated_vol = figures[name]  # Récupérer la fonction correspondante
    resultat = calulated_vol(name, a)  # Appeler la fonction avec les deux nombres
    print(resultat)
else:
    print("Polyèdre non connu")
