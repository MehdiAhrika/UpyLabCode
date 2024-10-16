
def longueur(*points):
    return sum([((points[i][0]-points[i+1][0])**2 + (points[i][1]-points[i+1][1])**2)**0.5 for i in range(len(points)-1)])