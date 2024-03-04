#創建table

import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",    # root最高權限，不會被擋。
    passwd="Password123"
)

mycursor=mydb.cursor()
mycursor.execute("use testDB")
#mycursor.execute("create table person( id int not null auto_increment PRIMARY KEY,username varchar(255) not null,coded int not null,job varchar(200) NOT NULL,note text)")
mycursor.execute("show tables")
for table in mycursor:
    print(table)