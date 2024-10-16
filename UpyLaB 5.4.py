import math

def distance_points(dist1, dist2):
    dist = math.sqrt((dist1[0] - dist2[0])**2 +(dist1[1] - dist2[1])**2)
    return dist
