from math import sqrt

def solveQuadraticEquation(a, b, c):
    discriminant = b * b - 4 * a * c
    root1 = 0
    root2 = 0

    if (discriminant > 0):
        root1 = (-b + sqrt(discriminant)) / (2 * a)
        root2 = (-b - sqrt(discriminant)) / (2 * a)
    elif (discriminant == 0):
        root1 = root2 = -b / (2 * a)
    else:
        return []

    return [root1, root2]