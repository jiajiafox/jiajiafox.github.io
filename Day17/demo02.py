#創建table

import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",    # root最高權限，不會被擋。
    passwd="Password123"
)

mycursor=mydb.cursor()
mycursor.execute("use testDB")
# mycursor.execute("create table students(name varchar(255),age int(10))")
mycursor.execute("show tables")
for table in mycursor:
    print(table)