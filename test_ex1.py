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
        self.assertFalse(ex1.racine_carre(2, 2.1))                       # nb_decimal n'est pas un nombre entier

if __name__ == "__main__":
    unittest.main()
