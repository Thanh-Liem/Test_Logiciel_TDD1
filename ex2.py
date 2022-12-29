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
