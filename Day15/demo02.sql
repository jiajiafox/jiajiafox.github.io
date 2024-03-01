create table person(
id int auto_increment primary key not null,
username varchar(200) not null,
coded int not null,
job varchar(200) not null,
note text
);

insert into person(username,coded,job,note)value("張三",1,"業務",null),("李四",2,"財務",null),("王五",1,"業務","奧客"),("許六",3,"管理",null),("陳七",2,"財務",null);
update person set coded=2 where id=5;
delete from person where id in(11,12,13,14,15);
select * from person;

select * from person where job <> "業務";

select * from person where coded=1 or coded=2;

select * from person where coded in(2,3);

select * from person where coded between 2 and 3;