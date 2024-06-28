import sqlite3

con = sqlite3.connect("database.db")
cursor = con.cursor()
cursor.execute("CREATE TABLE USERS(USERID INT(10), NAME VARCHAR(20), DOB DATE, PASSWORD VARCHAR(12));")
con.commit()
con.close()