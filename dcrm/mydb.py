import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = ''
)

# Prepare a cursor object 
cursorObect = dataBase.cursor()

# Craete a Database
cursorObect.execute("CREATE DATABASE elderco")

print("All Done!") 