# 新增多筆資料

import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",    # root最高權限，不會被擋。
    passwd="Password123"
)

mycursor=mydb.cursor()
mycursor.execute("use testDB")
sqlsx="insert into students(name,age)values(%s,%s)"  # %s:字串
student2=[("A",18),("B",20),("C",31),("D",45),("E",48)]
mycursor.executemany(sqlsx,student2)    # 要新增多筆資料要改成many。
mydb.commit()