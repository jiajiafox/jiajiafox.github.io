create database demoDB;
use demodb;

create table student(
	id int primary key auto_increment not null,
    named varchar(255) not null,
    age int not null
    );
    
insert into student(named,age)values('Stanley',18),('Debby',17),('Ashley',17);
select * from student;
select named,age from student;
select age+1 from student;
select named as 名字,age as 年齡 from student;