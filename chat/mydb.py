import mysql.connector

dataBase = mysql.connector.connect(
    host= 'localhost',
    user= 'root1',
    passwd= 'elpepe'
)

cursorObject = dataBase.cursor()

cursorObject.execute("Create Database Chats")

print("done")