import ex1
import unittest
import math


class Test(unittest.TestCase):
    def test_minimum(self):
        # Avec un minimum positif
        self.assertEqual(ex1.minimum([0, 1, 2, 3]), 0)      # Minimum au début
        self.assertEqual(ex1.minimum([3, 2, 1, 0]), 0)      # Minimum à la fin
        self.assertEqual(ex1.minimum([3, 2, 0, 1]), 0)      # Minimum pas au bord

        # Avec un minimum négatif
        self.assertEqual(ex1.minimum([-2, 0, 2, 4]), -2)    # Minimum au début
        self.assertEqual(ex1.minimum([4, 2, 0, -2]), -2)    # Minimum à la fin
        self.assertEqual(ex1.minimum([4, 2, -2, 0]), -2)    # Minimum pas au bord

        # Avec un minimum positif
        self.assertNotEqual(ex1.minimum([0, 1, 2, 3]), 3)   # Minimum au début
        self.assertNotEqual(ex1.minimum([3, 2, 1, 0]), 2)   # Minimum à la fin
        self.assertNotEqual(ex1.minimum([3, 2, 0, 1]), 1)   # Minimum pas au bord

        # Avec un minimum négatif
        self.assertNotEqual(ex1.minimum([-2, 0, 2, 4]), 4)  # Minimum au début
        self.assertNotEqual(ex1.minimum([4, 2, 0, -2]), 0)  # Minimum à la fin
        self.assertNotEqual(ex1.minimum([4, 2, -2, 0]), 2)  # Minimum pas au bord

        # Tests des variables
        self.assertFalse(ex1.minimum([]))                   # Liste vide
        self.assertEqual(ex1.minimum([1]), 1)               # Liste 1 élements
        self.assertFalse(ex1.minimum("haha"))               # Liste non liste

    def test_racine_carre(self):
        # Test Equal
        self.assertEqual(ex1.racine_carre(4), 2)                            # Test simple
        self.assertEqual(ex1.racine_carre(5, 7), round(5 ** (1 / 2), 7))    # Test avec la formule mathématique
        self.assertEqual(ex1.racine_carre(5, 7), round(math.sqrt(5), 7))    # Test avec math.sqrt()
        self.assertEqual(ex1.racine_carre(1234, 2), 35.13)                  # Test en dur (résultat à la calculatrice)
        self.assertEqual(ex1.racine_carre(4321, 5), 65.73431)               # Test en dur (résultat à la calculatrice)
        self.assertEqual(ex1.racine_carre(1111, 0), 33)                     # Test en dur (résultat à la calculatrice)

        # Test Not Equal
        self.assertNotEqual(ex1.racine_carre(4), 3)                         # Test simple
        self.assertNotEqual(ex1.racine_carre(5, 7), round(5 ** (1 / 2), 1)) # Test avec la formule mathématique
        self.assertNotEqual(ex1.racine_carre(5, 7), round(math.sqrt(5), 1)) # Test avec math.sqrt()
        self.assertNotEqual(ex1.racine_carre(1234, 2), 35.14)               # Test en dur (résultat à la calculatrice)
        self.assertNotEqual(ex1.racine_carre(4321, 5), 65.74)               # Test en dur (résultat à la calculatrice)
        self.assertNotEqual(ex1.racine_carre(1111, 0), 34)                  # Test en dur (résultat à la calculatrice)

        # Test Error -> False
        self.assertFalse(ex1.racine_carre(-2, nb_decimal=2))                # False : Racine carré d'un chiffre négatif
        self.assertFalse(ex1.racine_carre(4, nb_decimal=-1))                # False : Nombre de décimal impossible

        # Test des variables
        self.assertFalse(ex1.racine_carre("haha", 2))                       # x n'est pas un nombre
        self.assertFalse(ex1.racine_carre(2, "haha"))                       # nb_decimal n'est pas un nombre
        self.assertFalse(ex1.racine_carre(2, 2.1))                          # nb_decimal n'est pas un nombre entier

    def test_perimetre_cercle(self):
        # Test Equal
        self.assertEqual(ex1.perimetre_cercle(rayon=4, nb_decimal=2, math_pi=True), round(2 * math.pi * 4, 2))      # Test simple
        self.assertEqual(ex1.perimetre_cercle(rayon=6, nb_decimal=2, math_pi=False), round(2 * 3.14 * 6, 2))        # Test simple
        self.assertEqual(ex1.perimetre_cercle(rayon=11, nb_decimal=2, math_pi=True), 69.12)                         # Test en dur avec math.pi  (résultat à la calculatrice)
        self.assertEqual(ex1.perimetre_cercle(rayon=11, nb_decimal=6, math_pi=True), 69.115038)                     # Test en dur avec math.pi  (résultat à la calculatrice)
        self.assertEqual(ex1.perimetre_cercle(rayon=23, nb_decimal=0, math_pi=False), 144)                          # Test en dur pi = 3.14  (résultat à la calculatrice)
        self.assertEqual(ex1.perimetre_cercle(rayon=23, nb_decimal=1, math_pi=False), 144.4)                        # Test en dur pi = 3.14  (résultat à la calculatrice)

        # Test Equal
        self.assertNotEqual(ex1.perimetre_cercle(rayon=4, nb_decimal=2, math_pi=True), round(2 * math.pi * 5, 2))   # Test simple
        self.assertNotEqual(ex1.perimetre_cercle(rayon=6, nb_decimal=2, math_pi=False), round(2 * 3.14 * 6, 1))     # Test simple
        self.assertNotEqual(ex1.perimetre_cercle(rayon=11, nb_decimal=2, math_pi=True), 71.12)                      # Test en dur avec math.pi  (résultat à la calculatrice)
        self.assertNotEqual(ex1.perimetre_cercle(rayon=11, nb_decimal=6, math_pi=True), 68.115038)                  # Test en dur avec math.pi  (résultat à la calculatrice)
        self.assertNotEqual(ex1.perimetre_cercle(rayon=23, nb_decimal=0, math_pi=False), 145)                       # Test en dur pi = 3.14  (résultat à la calculatrice)
        self.assertNotEqual(ex1.perimetre_cercle(rayon=23, nb_decimal=1, math_pi=False), 144.5)                     # Test en dur pi = 3.14  (résultat à la calculatrice)

        # Test Error -> False
        self.assertFalse(ex1.perimetre_cercle(rayon=-1))                                                            # False : Rayon négatif
        self.assertFalse(ex1.perimetre_cercle(rayon=3, nb_decimal=-1))                                              # False : Nombre de décimal  négatif

        # Test des variables
        self.assertFalse(ex1.perimetre_cercle("haha", 2, True))                                                     # rayon n'est pas un nombre
        self.assertFalse(ex1.perimetre_cercle(2, "haha", True))                                                     # nb_decimal n'est pas un nombre entier
        self.assertFalse(ex1.perimetre_cercle(2, 2.1, True))                                                        # nb_decimal n'est pas un nombre entier
        self.assertFalse(ex1.perimetre_cercle(2, 2, "haha"))                                                        # math_pi n'est pas un bool

    def test_angles_trangles(self):
        # Test Equal
        self.assertEqual(ex1.angles_triangles(a=2, b=3, c=4, nb_decimal=2, degree=True, math_pi=True), (28.96, 46.57, 104.48))                  # Test simple (d'après le site planetclac
        self.assertEqual(ex1.angles_triangles(a=1, b=2, c=3, nb_decimal=2, degree=True, math_pi=True), (0, 0, 180))                             # Test simple (d'après le site planetclac
        self.assertEqual(ex1.angles_triangles(a=2, b=3, c=4, nb_decimal=6, degree=True, math_pi=True), (28.955024, 46.567463, 104.477512))      # Test simple (d'après le site planetclac
        self.assertEqual(ex1.angles_triangles(a=2, b=3, c=4, nb_decimal=2, degree=True, math_pi=False), (28.97, 46.59, 104.53))                 # Test simple avec la conversion avec pi = 3.14 ( calculatrice)

        # Test Not Equal
        self.assertNotEqual(ex1.angles_triangles(a=2, b=3, c=4, nb_decimal=2, degree=True, math_pi=True), (28.97, 46.56, 104.49))               # Test simple (d'après le site planetclac
        self.assertNotEqual(ex1.angles_triangles(a=1, b=2, c=3, nb_decimal=2, degree=True, math_pi=True), (0, 0, 0))                            # Test simple (d'après le site planetclac
        self.assertNotEqual(ex1.angles_triangles(a=2, b=3, c=4, nb_decimal=6, degree=True, math_pi=True), (28.955025, 46.567464, 104.477511))   # Test simple (d'après le site planetclac
        self.assertNotEqual(ex1.angles_triangles(a=2, b=3, c=4, nb_decimal=2, degree=True, math_pi=False), (28.96, 46.58, 104.52))              # Test simple avec la conversion avec pi = 3.14 ( calculatrice)

        # Test Error -> False
        self.assertFalse(ex1.angles_triangles(a=-2, b=3, c=4, nb_decimal=2, degree=True, math_pi=True))                                         # False : a négatif
        self.assertFalse(ex1.angles_triangles(a=2, b=-3, c=4, nb_decimal=2, degree=True, math_pi=True))                                         # False : b négatif
        self.assertFalse(ex1.angles_triangles(a=2, b=3, c=-4, nb_decimal=2, degree=True, math_pi=True))                                         # False : c négatif

        # Test des variables
        self.assertFalse(ex1.angles_triangles(a="haha", b=3, c=4, nb_decimal=2, degree=True, math_pi=True))  # a n'est pas un nombre
        self.assertFalse(ex1.angles_triangles(a=2, b="haha", c=4, nb_decimal=2, degree=True, math_pi=True))  # b n'est pas un nombre
        self.assertFalse(ex1.angles_triangles(a=2, b=3, c="haha", nb_decimal=2, degree=True, math_pi=True))  # c n'est pas un nombre
        self.assertFalse(ex1.angles_triangles(a=2, b=3, c=4, nb_decimal="haha", degree=True, math_pi=True))  # nb_decimal n'est pas un nombre
        self.assertFalse(ex1.angles_triangles(a=2, b=3, c=4, nb_decimal=2, degree="haha", math_pi=True))  # degree n'est pas un bool
        self.assertFalse(ex1.angles_triangles(a=2, b=3, c=4, nb_decimal=2, degree=True, math_pi="haha"))  # math_pi n'est pas un bool
        self.assertFalse(ex1.angles_triangles(a=2, b=3, c=4, nb_decimal=2.1, degree=True, math_pi=True))  # nb_decimal n'est pas un nombre entier


if __name__ == "__main__":
    unittest.main()
