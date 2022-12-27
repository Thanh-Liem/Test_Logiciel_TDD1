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

if __name__ == "__main__":
    unittest.main()
