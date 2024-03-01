import mysql.connector
from mysql.connector import Error

try:
    mydb=mysql.connector.connect(
        host="127.0.0.1",  # 或用 "localhost"
        user="root",
        passwd="Password123"
        # port=3306 (除非有改port號，不然不需要增加這一行)
    )
    myCursor=mydb.cursor()
    myCursor.execute("show databases")
    result=myCursor.fetchall()

    for db in result:
        print(db)

except Error as e:
    print("----")
# finally:
#     myCursor.close()