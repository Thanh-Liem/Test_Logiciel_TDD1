import math


def minimum(liste):
    if not liste or not isinstance(liste, list):
        return False

    for x in liste:
        if not isinstance(x, (int, float)):
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
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)) or not isinstance(nb_decimal, int) or not isinstance(degree, bool) or not isinstance(math_pi, bool):
        return False
    if a <= 0 or b <= 0 or c <= 0 or nb_decimal < 0:
        return False

    if math_pi:
        pi = math.pi
    else:
        pi = 3.14

    gamma = math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))
    alpha = math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c))
    beta = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))

    if degree:
        gamma = gamma * 180 / pi
        alpha = alpha * 180 / pi
        beta = beta * 180 / pi

    return round(beta, nb_decimal), round(alpha, nb_decimal), round(gamma, nb_decimal)
