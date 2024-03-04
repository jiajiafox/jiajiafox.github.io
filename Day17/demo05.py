# 新增資料

import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",    # root最高權限，不會被擋。
    passwd="Password123"
)

mycursor=mydb.cursor()
mycursor.execute("use testDB")
sqlsx="insert into students(name,age)values(%s,%s)"  # %s:字串
student1=("Jason",35)
#mycursor.execute("insert into students(name,age)values('Tom',35)")
mycursor.execute(sqlsx,student1)
mydb.commit()