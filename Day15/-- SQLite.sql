-- SQLite
-- SQLite
-- SQLite (建立table)新增，刪除，修改，查詢(最常用)
-- SELECT * FROM student; --搜尋全部
-- SELECT name,age FROM student; --搜尋 name,age
--建立database
-- create database mydb1;
--建立table
CREATE TABLE person(
    id not null,
    name not null,
    age not null
    )
INSERT INTO person (id, name, age)
VALUES (1,'Stanley',26);