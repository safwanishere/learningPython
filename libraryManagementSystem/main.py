from dbCon import *

searchResult = searchUser("safwan")
print(searchResult)

con.commit()
con.close()