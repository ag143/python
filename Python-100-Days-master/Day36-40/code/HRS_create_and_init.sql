-- create a database named hrs
drop database if exists `hrs`;
create database `hrs` default charset utf8mb4;

-- switch to hrs database
use `hrs`;

-- create department table
create table `tb_dept`
(
`dno` int not null comment 'Number',
`dname` varchar(10) not null comment 'name',
`dloc` varchar(20) not null comment 'Location',
primary key (dno)
);

-- insert 4 departments
insert into `tb_dept` values
    (10, 'Accounting Department', 'Beijing'),
    (20, 'R&D Department', 'Chengdu'),
    (30, 'Sales Department', 'Chongqing'),
    (40, 'Operation and Maintenance Department', 'Shenzhen');

-- create employee table
create table `tb_emp`
(
`eno` int not null comment 'employee number',
`ename` varchar(20) not null comment 'employee name',
`job` varchar(20) not null comment 'employee position',
`mgr` int comment 'Supervisor number',
`sal` int not null comment 'Employee monthly salary',
`comm` int comment 'Monthly allowance',
`dno` int comment 'Department number',
primary key (eno),
constraint `fk_emp_mgr` foreign key (`mgr`) references tb_emp (`eno`),
constraint `fk_emp_dno` foreign key (`dno`) references tb_dept (`dno`)
);

-- Insert 14 employees
insert into `tb_emp` values
    (7800, 'Zhang Sanfeng', 'President', null, 9000, 1200, 20),
    (2056, 'Qiao Feng', 'Analyst', 7800, 5000, 1500, 20),
    (3088, 'Li Mochou', 'Designer', 2056, 3500, 800, 20),
    (3211, 'Zhang Wuji', 'Programmer', 2056, 3200, null, 20),
    (3233, 'Qiu Chuji', 'programmer', 2056, 3400, null, 20),
    (3251, 'Zhang Cuishan', 'programmer', 2056, 4000, null, 20),
    (5566, 'Song Yuanqiao', 'Accountant', 7800, 4000, 1000, 10),
    (5234, 'Guo Jing', 'Cashier', 5566, 2000, null, 10),
    (3344, 'Huang Rong', 'Sales Supervisor', 7800, 3000, 800, 30),
    (1359, 'Hu Yidao', 'Salesman', 3344, 1800, 200, 30),
    (4466, 'Miao Renfeng', 'Salesman', 3344, 2500, null, 30),
    (3244, 'Ouyang Feng', 'Programmer', 3088, 3200, null, 20),
    (3577, 'Yang Guo', 'Accounting', 5566, 2200, null, 10),
    (3588, 'Zhu Jiuzhen', 'Accounting', 5566, 2500, null, 10);


-- Query the name and monthly salary of the employee with the highest monthly salary

-- Query the employee's name and annual salary (annual salary=(sal+comm)*13)

-- Query the number and number of employees in the department

-- Query the name and number of all departments

-- Query the name and monthly salary of employees whose monthly salary exceeds the average monthly salary

-- Query the name, department number and monthly salary of employees whose monthly salary exceeds the average monthly salary of their department

-- Query the name, monthly salary and department name of the person with the highest monthly salary in the department

-- Query supervisor's name and position

-- Query the rank, name and monthly salary of employees with monthly salary ranking 4~6

-- Query the name, monthly salary and department number of the top 2 employees with monthly salary in each department