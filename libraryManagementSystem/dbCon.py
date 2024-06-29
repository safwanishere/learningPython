import sqlite3

con = sqlite3.connect("libraryManagementSystem/library.db")
cur = con.cursor()

# table creation command
# cur.execute("CREATE TABLE BOOKS(ID INT(5), TITLE VARCHAR(20), AUTHOR VARCHAR(20), GENRE VARCHAR(10), AVAILABLE BOOL);")
# cur.execute("CREATE TABLE USERS(USERID INT(5), NAME VARCHAR(20), MOBILENUMBER INT(10), BORROWEDBOOKS VARCHAR(100));")

# book information variables
id = 6
title = 'The Trials of Apollo 2'
author = 'Rick Riordan'
genre = 'fiction'
available = True

#user information variables

userID = 4
name = 'Khaja Viqhar Uddin'
mobileNumber = 7674023587
borrowedBooks = []

# ------------------- BOOKS TABLE -----------------------

#book insertion command
def insertBook(title, author, genre):
    cur.execute("SELECT MAX(ID) FROM BOOKS;")
    result = int(cur.fetchall()[0][0])
    bookID = result + 1
    cur.execute(f"INSERT INTO BOOKS VALUES({bookID}, '{title}', '{author}', '{genre}', 'True');")

def removeBook(bookID: int):
    cur.execute(f"DELETE FROM BOOKS WHERE ID = '{bookID}';")

def alterBookDetails(bookID, columnName, newValue):
    cur.execute(f"UPDATE BOOKS SET {columnName} = '{newValue}' WHERE ID = '{bookID}';")

# -------------------------------------------------------

# ------------------- USERS TABLE -----------------------

#user insertion command
def insertUser(name, mobileNumber):
    cur.execute("SELECT MAX(USERID) FROM USERS;")
    result = int(cur.fetchall()[0][0])
    userID = result + 1
    cur.execute(f"INSERT INTO USERS VALUES({userID}, '{name}', '{mobileNumber}', '[]');")

def removeUser(userID :int):
    cur.execute(f"DELETE FROM USERS WHERE USERID = '{userID}';")

def alterUserDetails(columnName, beforeValue, afterValue):
    if columnName == "NAME":
        cur.execute(f"UPDATE USERS SET {columnName} = '{afterValue}' WHERE {columnName} = '{beforeValue}';")
    if columnName == "MOBILENUMBER":
        cur.execute(f"UPDATE USERS SET {columnName} = {afterValue} WHERE {columnName} = {beforeValue};")
    

# -------------------------------------------------------

# function calls
# insertBook('Peer-e-Kamil', 'Umera Ahmed', 'Novel')
# insertUser("Abdul Basith Khan", 7856945234)
# removeBook(5)
# removeUser(2)
# alterBookDetails(2, 'AUTHOR', 'G. Orwell')
# alterUserDetails('NAME', 'Mohammed Safwan', 'Mohammed Kaif')