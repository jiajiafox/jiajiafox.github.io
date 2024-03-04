import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",    # root最高權限，不會被擋。
    passwd="Password123"
)

mycursor=mydb.cursor()
mycursor.execute("use testDB")

# mycursor.execute("select * from students")
mycursor.execute("select name as 姓名 from students")
for liststu in mycursor:
    print(liststu)