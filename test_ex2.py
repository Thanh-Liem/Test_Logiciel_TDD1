import ex2
import sqlite3
import unittest


class Test(unittest.TestCase):
	def test_table(self):
		# On reset la base de donnée pour repartir de 0 que qu'il n'y a pas de dépendance avec le test d'avant
		self.assertTrue(ex2.reset_init_db("test_database.db"))	# Condition initial
		self.assertTrue(ex2.verif_table("test_database.db")) 	# Test si la table existe

		self.assertFalse(ex2.reset_init_db(123))				# Test non string
		self.assertFalse(ex2.verif_table(123))					# Test non string

if __name__ == "__main__":
    unittest.main()