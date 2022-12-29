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

	def test_username_password(self):
		# On reset la base de donnée pour repartir de 0 que qu'il n'y a pas de dépendance avec le test d'avant
		self.assertTrue(ex2.reset_init_db("test_database.db"))											# Condition initial
		self.assertTrue(ex2.verif_table("test_database.db")) 											# Test si la table existe
		self.assertTrue(ex2.ajout_utilisateur("test_database.db", "testUsername", "testPassword0?")) 	# Ajout d'un utilisateur
		self.assertTrue(ex2.verif_utilisateur_db("test_database.db", "testUsername", "testPassword0?"))	# Test si l'utilisateur existe
		self.assertTrue(ex2.verif_utilisateur("test_database.db", "testUsername", "testPassword0?")) 	# Test si la table existe

		self.assertFalse(ex2.verif_utilisateur("test_database.db", "test123", "testPassword0?")) 		# Test username non dans la base
		self.assertFalse(ex2.verif_utilisateur("test_database.db", "testUsername", "test123")) 			# Test password non dans la base

	def test_ajout_link(self):
		# On reset la base de donnée pour repartir de 0 que qu'il n'y a pas de dépendance avec le test d'avant
		self.assertTrue(ex2.reset_init_db("test_database.db"))													# Condition initial
		self.assertTrue(ex2.verif_table("test_database.db")) 													# Test si la table existe
		self.assertTrue(ex2.ajout_utilisateur("test_database.db", "testUsername", "testPassword0?")) 			# Ajout d'un utilisateur
		self.assertTrue(ex2.verif_utilisateur_db("test_database.db", "testUsername", "testPassword0?"))			# Test si l'utilisateur existe
		self.assertTrue(ex2.verif_utilisateur("test_database.db", "testUsername", "testPassword0?")) 			# Test si la table existe
		self.assertTrue(ex2.ajout_link("test_database.db", "testUsername", "testPassword0?", "testlink1")) 		# Ajout d'un link
		self.assertTrue(ex2.ajout_link("test_database.db", "testUsername", "testPassword0?", "testlink2")) 		# Ajout d'un autre link

		self.assertFalse(ex2.ajout_link("test_database.db", "testUsername", "testPassword0?", 123)) 			# Ajout d'un link non conforme (non str)
		self.assertFalse(ex2.ajout_link("test_database.db", "testUsername", "testPassword0?", "testFalse")) 	# Ajout d'un link non conforme (majuscule)
		self.assertFalse(ex2.ajout_link("test_database.db", "testUsername", "testPassword0?", "testfalse?"))	# Ajout d'un link non conforme (caractere special)
		self.assertFalse(ex2.ajout_link("test_database.db", "testUsername", "testPassword0?", ""))				# Ajout d'un link non conforme (vide)
	
if __name__ == "__main__":
    unittest.main()