import sqlite3

con = sqlite3.connect("database.db")
cursor = con.cursor()

# cursor.execute("CREATE TABLE USERS(USERID INT(10), NAME VARCHAR(20), DOB DATE, PASSWORD VARCHAR(12));")
cursor.execute("DELETE FROM USERS;")
cursor.execute("INSERT INTO USERS VALUES(1, 'Mohammed Safwan', '2005-12-26', '261205');") 

con.commit()
con.close()