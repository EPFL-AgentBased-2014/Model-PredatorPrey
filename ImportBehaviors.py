import sqlite3 as lite
import csv

def main():
	filename = "PredatorPreyAlphaGammaChi-find_cyles-table.csv"
	dbname = "PredatorPreyAlphaGammaChi-find_cyles.db"

	createDB(dbname)

	f = open(filename).readlines()
	f = f[7:]
	reader = csv.reader(f, delimiter=',')
	insertDB(dbname, reader)
	print "All data imported"

def insertDB(dbname, reader):
	conn = lite.connect(dbname, isolation_level=None)
	c = conn.cursor()
	sql = """	INSERT INTO Cycles
				(
					RunNumber, 
					alpha, 
					gamma, 
					initRabbits, 
					initFoxes, 
					steps, 
					countRabbits, 
					countFoxes,
					hash) 
				VALUES (?,?,?,?,?,?,?,?,?)
	"""

	for row in reader:
		h = str(row[1])+'-'+str(row[2])+'-'+str(row[3])+'-'+str(row[4])
		row.append(h)
		#print row
		c.execute(sql,row)
		conn.commit()
	conn.close()

def createDB(dbname):
	conn = lite.connect(dbname, isolation_level=None)
	c = conn.cursor()

	c.execute("DROP TABLE IF EXISTS Cycles")

	createTableCycles = """
				CREATE TABLE Cycles
				(
					Id INTEGER PRIMARY KEY AUTOINCREMENT,
					RunNumber INTEGER,
					alpha REAL,
					gamma REAL,
					initRabbits INTEGER,
					initFoxes INTEGER,
					steps INTEGER,
					countRabbits INTEGER,
					countFoxes INTEGER,
					hash VARCHAR
					)
	"""
	c.execute(createTableCycles)
	conn.commit()
	conn.close()

if __name__ == '__main__':
	main()

