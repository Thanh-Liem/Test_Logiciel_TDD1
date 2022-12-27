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
    return -1