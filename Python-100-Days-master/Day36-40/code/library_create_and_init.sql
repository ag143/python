drop database if exists library;

create database library default charset utf8;

use library;

create table tb_book
(
bookid integer primary key auto_increment,
title varchar(100) not null,
author varchar(50) not null,
publisher varchar(50) not null,
price float not null,
lendout bit default 0,
lenddate datetime,
lendcount integer default 0
);

insert into tb_book (title, author, publisher, price, lendcount) values ​​('Java Core Technology (Volume 1)', 'Kay S. Horstman', 'Mechanical Industry Press', 98.2, 102);
insert into tb_book (title, author, publisher, price, lendcount) values ​​('Java Programming Ideas', 'Escher', 'Machinery Industry Press', 86.4, 87);
insert into tb_book (title, author, publisher, price, lendcount) values ​​('In-depth understanding of Java virtual machine', 'Zhou Zhiming', 'Machinery Industry Press', 64.4, 32);
insert into tb_book (title, author, publisher, price, lendcount) values ​​('Effective Java Chinese Edition (2nd Edition) ', 'Escher', 'Machinery Industry Press', 36.8, 200);
insert into tb_book (title, author, publisher, price, lendcount) values ​​('Data Structure and Algorithm Analysis: Java Language Description (Original Book 3rd Edition)', 'Mark Ellen Weiss', 'Machinery Industry Press ', 51.0, 15);
insert into tb_book (title, author, publisher, price, lendcount) values ​​('Java 8 combat', 'Irma', 'People's Posts and Telecommunications Press', 56.8, 25);
insert into tb_book (title, author, publisher, price, lendcount) values ​​('Refactoring: Improving the Design of Existing Code', 'Martin Fowler', 'People's Posts and Telecommunications Press', 53.1, 99);
insert into tb_book (title, author, publisher, price, lendcount) values ​​('Code Encyclopedia (2nd Edition)', 'Steve McConnell', 'Electronic Industry Press', 53.1, 99);
insert into tb_book (title, author, publisher, price, lendcount) values ​​('The Way of Programmers: From Little Workers to Experts', 'Hunter, Thomas', 'Electronic Industry Press', 45.4, 50);
insert into tb_book (title, author, publisher, price, lendcount) values ​​('The Way to Clean Code', 'Martin', 'People's Posts and Telecommunications Press', 45.4, 30);
insert into tb_book (title, author, publisher, price, lendcount) values ​​('Design Patterns: Fundamentals of Reusable Object-Oriented Software', 'Erich Gamma, Richard Helm', 'Mechanical Industry Press', 30.2, 77);
insert into tb_book (title, author, publisher, price, lendcount) values ​​('Zen of Design Patterns (2nd Edition)', 'Qin Xiaobo', 'Machinery Industry Press', 70.4, 100);