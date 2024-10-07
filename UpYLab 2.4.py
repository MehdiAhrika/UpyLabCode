
from math import cos, sin, pi

r = 100

for i in range(0,301,60):
    i_radiant = i * pi / 180
    x = cos(i_radiant) * r
    y = sin(i_radiant) * r
    print(x, y)
