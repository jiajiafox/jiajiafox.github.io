import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password123"
)
myCursor=mydb.cursor()
myCursor.execute("show databases")

for db in myCursor:
    print(db)