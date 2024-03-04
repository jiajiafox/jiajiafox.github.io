#建立資料庫

import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",    # root最高權限，不會被擋。
    passwd="Password123"
)
# print(mydb) <mysql.connector.connection_cext.CMySQLConnection object at 0x00000231F9C3B450>

mycursor=mydb.cursor()
# mycursor.execute("create database testDB")  #建立資料庫
mycursor.execute("show databases")  #查詢database

for db in mycursor:
    print(db)