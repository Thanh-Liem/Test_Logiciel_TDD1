import math


def minimum(liste):
    if not liste or not isinstance(liste, list):
        return False

    return min(liste)

def racine_carre(x, nb_decimal=2):
    if not isinstance(x, (int, float)) or not isinstance(nb_decimal, int):
        return False
    if x < 0 or nb_decimal < 0:
        return False

    return round(x ** (1 / 2), nb_decimal)

def perimetre_cercle(rayon, nb_decimal=2, math_pi=True):
    if not isinstance(rayon, (int, float)) or not isinstance(nb_decimal, int) or not isinstance(math_pi, bool):
        return False
    if rayon < 0 or nb_decimal < 0:
        return False

    if math_pi:
        pi = math.pi
    else:
        pi = 3.14

    return round(2 * pi * rayon, nb_decimal)

def angles_triangles(a, b, c, nb_decimal=2, degree=True, math_pi=True):
    return -1