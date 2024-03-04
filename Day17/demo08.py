# 刪除資料

import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",    # root最高權限，不會被擋。
    passwd="Password123"
)

mycursor=mydb.cursor()
mycursor.execute("use testDB")


mycursor.execute("delete from students where name='E'")
mydb.commit()
