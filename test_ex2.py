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

	def test_ajout_utilisateur(self):
		# On reset la base de donnée pour repartir de 0 que qu'il n'y a pas de dépendance avec le test d'avant
		self.assertTrue(ex2.reset_init_db("test_database.db"))											# Condition initial
		self.assertTrue(ex2.verif_table("test_database.db")) 											# Test si la table existe
		self.assertTrue(ex2.ajout_utilisateur("test_database.db", "testUsername", "testPassword0?")) 	# Ajout d'un utilisateur
		self.assertTrue(ex2.verif_utilisateur_db("test_database.db", "testUsername", "testPassword0?"))	# Test si l'utilisateur existe

		self.assertFalse(ex2.ajout_utilisateur("test_database.db", 123, "testPassword0?")) 				# Test username non conforme
		self.assertFalse(ex2.verif_utilisateur_db("test_database.db", "testUsername", 123))				# Test password non conforme
		self.assertFalse(ex2.ajout_utilisateur("test_database.db", "testUsername!", "testPassword0?")) 	# Test username non conforme
		self.assertFalse(ex2.verif_utilisateur_db("test_database.db", "testUsername", "testPassword"))	# Test password non conforme


if __name__ == "__main__":
    unittest.main()