import sqlite3 as lite
import csv

def main():
	dbname = "PredatorPreyAlphaGammaChi-find_cyles.db"

	makeMeans(dbname)

def makeMeans(dbname):
	conn = lite.connect(dbname, isolation_level=None)
	c = conn.cursor()

	c.execute("DROP TABLE IF EXISTS Means")
	conn.commit()

	sql = """	CREATE TABLE Means AS
				SELECT 	alpha, 
						gamma, 
						initRabbits, 
						initFoxes, 
						AVG(steps) as meansteps, 
						hash
				FROM Cycles
				GROUP BY hash
	"""

	c.execute(sql)
	conn.commit()
	conn.close()


if __name__ == '__main__':
	main()

