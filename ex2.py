import sqlite3
import string

def reset_init_db(db_name):

	if not isinstance(db_name, str):
		return False

	if db_name == "":
		return False

	# ouverture/initialisation de la base de donnee
	conn = sqlite3.connect(db_name)
	conn.row_factory = sqlite3.Row
	c = conn.cursor()

	# Action
	c.execute("drop table if exists Utilisateur")
	c.execute("create table if not exists Utilisateur(username TEXT NOT NULL PRIMARY KEY, password TEXT NOT NULL, links TEXT)")

	c.fetchall()
	
	# fermeture de la base de donnee
	conn.commit()
	conn.close()

	return True

def verif_table(db_name):

	if not isinstance(db_name, str):
		return False

	if db_name == "":
		return False

	# ouverture/initialisation de la base de donnee
	conn = sqlite3.connect(db_name)
	conn.row_factory = sqlite3.Row
	c = conn.cursor()

	c.execute("select exists (select name from sqlite_schema where type='table' and name='Utilisateur')")

	ret = c.fetchone()[0]

	# fermeture de la base de donnee
	conn.commit()
	conn.close()

	if ret == 0:
		return False
	return True

def verif_username_password(username, password):
	
	# Verification du type
	if not isinstance(username, str) or not isinstance(password, str):
		return False

	special_caracts = string.punctuation
	
	# Verification de la longueur
	if len(username) < 3 or len(password) < 8:
		return False

	# Verification du contenu
	for x in username:
		if x in special_caracts:
			return False
	
	majuscule = False
	caract_special = False
	number = False
	standard_caract = False

	for x in password:
		if x.isupper():
			majuscule = True
		elif x in special_caracts:
			caract_special = True
		elif x.isdigit():
			number = True
		elif x.isascii():
			standard_caract = True

	if not ( majuscule and caract_special and number and standard_caract):
		return False
	return True

def ajout_utilisateur(db_name, username, password):

	if not isinstance(db_name, str) or not isinstance(username, str) or not isinstance(password, str):
		return False

	if not verif_username_password(username, password):
		return False

	if db_name == "":
		return False

	# ouverture/initialisation de la base de donnee
	conn = sqlite3.connect(db_name)
	conn.row_factory = sqlite3.Row
	c = conn.cursor()

	# Action
	action = "insert into Utilisateur(username, password) values ('%s', '%s')" %(username, password)

	c.execute(action)
	c.fetchall()

	# fermeture de la base de donnee
	conn.commit()
	conn.close()

	return True

def verif_utilisateur_db(db_name, username, password):

	if not isinstance(db_name, str) or not isinstance(username, str) or not isinstance(password, str):
		return False
	
	if not verif_username_password(username, password):
		return False

	if db_name == "":
		return False

	# ouverture/initialisation de la base de donnee
	conn = sqlite3.connect(db_name)
	conn.row_factory = sqlite3.Row
	c = conn.cursor()

	action = "select exists (select * from Utilisateur where username='%s' and password='%s')" %(username, password)
	c.execute(action)

	ret = c.fetchone()[0]	# Si le couple username + password existe, renvoie 1

	# fermeture de la base de donnee
	conn.commit()
	conn.close()

	if ret == 0:
		return False
	
	return True

def verif_utilisateur(db_name, username, password):

	if verif_username_password(username, password):
		if verif_utilisateur_db(db_name, username, password):
			return True

	return False