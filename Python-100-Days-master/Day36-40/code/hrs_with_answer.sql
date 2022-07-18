drop database if exists hrs;
create database hrs default charset utf8mb4;

use hrs;

create table tb_dept
(
dno int not null comment 'Number',
dname varchar(10) not null comment 'name',
dloc varchar(20) not null comment 'Location',
primary key (dno)
);

insert into tb_dept values
    (10, 'Accounting Department', 'Beijing'),
    (20, 'R&D Department', 'Chengdu'),
    (30, 'Sales Department', 'Chongqing'),
    (40, 'Operation and Maintenance Department', 'Shenzhen');

create table tb_emp
(
eno int not null comment 'employee number',
ename varchar(20) not null comment 'employee name',
job varchar(20) not null comment 'employee position',
mgr int comment 'Supervisor number',
sal int not null comment 'Employee monthly salary',
comm int comment 'Monthly allowance',
dno int comment 'Department number',
primary key (eno),
foreign key (dno) references tb_dept (dno)
);

-- alter table tb_emp add constraint pk_emp_eno primary key (eno);
-- alter table tb_emp add constraint uk_emp_ename unique (ename);
-- alter table tb_emp add constraint fk_emp_mgr foreign key (mgr) references tb_emp (eno);
-- alter table tb_emp add constraint fk_emp_dno foreign key (dno) references tb_dept (dno);

insert into tb_emp values
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
select ename, sal from tb_emp where sal=(select max(sal) from tb_emp);

select ename, sal from tb_emp where sal>=all(select sal from tb_emp);

-- Query employee's name and annual salary ((monthly salary + subsidy)*13)
select ename, (sal+ifnull(comm,0))*13 as ann_sal from tb_emp order by ann_sal desc;

-- Query the number and number of employees in the department
select dno, count(*) as total from tb_emp group by dno;

-- Query the name and number of all departments
select dname, ifnull(total,0) as total from tb_dept left join
(select dno, count(*) as total from tb_emp group by dno) tb_temp
on tb_dept.dno=tb_temp.dno;

-- Query the name and monthly salary of the employee with the highest monthly salary (except Boss)
select ename, sal from tb_emp where sal=(
select max(sal) from tb_emp where mgr is not null
);

-- Query the name and monthly salary of the employee with the second highest monthly salary
select ename, sal from tb_emp where sal=(
select distinct sal from tb_emp order by sal desc limit 1,1
);

select ename, sal from tb_emp where sal=(
select max(sal) from tb_emp where sal<(select max(sal) from tb_emp)
);

-- Query the name and monthly salary of employees whose monthly salary exceeds the average monthly salary
select ename, sal from tb_emp where sal>(select avg(sal) from tb_emp);

-- Query the name, department number and monthly salary of employees whose monthly salary exceeds the average monthly salary of their department
select ename, t1.dno, sal from tb_emp t1 inner join
(select dno, avg(sal) as avg_sal from tb_emp group by dno) t2
on t1.dno=t2.dno and sal>avg_sal;

-- Query the name, monthly salary and department name of the person with the highest monthly salary in the department
select ename, sal, dname
from tb_emp t1, tb_dept t2, (
select dno, max(sal) as max_sal from tb_emp group by dno
) t3 where t1.dno=t2.dno and t1.dno=t3.dno and sal=max_sal;

-- Query supervisor's name and position
-- Tip: Use in/not in operations as little as possible, and distinct operations as little as possible
-- You can use existence judgment (exists/not exists) instead of set operations and deduplication operations
select ename, job from tb_emp where eno in (
select distinct mgr from tb_emp where mgr is not null
);

select ename, job from tb_emp where eno=any(
select distinct mgr from tb_emp where mgr is not null
);

select ename, job from tb_emp t1 where exists (
select 'x' from tb_emp t2 where t1.eno=t2.mgr
);

-- MySQL8 has window functions: row_number() / rank() / dense_rank()
-- Query the rank, name and monthly salary of the employees whose monthly salary ranks 4~6
select ename, sal from tb_emp order by sal desc limit 3,3;

select row_num, ename, sal from
(select @a:=@a+1 as row_num, ename, sal
from tb_emp, (select @a:=0) t1 order by sal desc) t2
where row_num between 4 and 6;

-- Window functions are not suitable for business databases, only suitable for offline data analysis
select
ename, sal,
row_number() over (order by sal desc) as row_num,
    rank() over (order by sal desc) as ranking,
    dense_rank() over (order by sal desc) as dense_ranking
from tb_emp limit 3 offset 3;

select ename, sal, ranking from (
select ename, sal, dense_rank() over (order by sal desc) as ranking from tb_emp
) tb_temp where ranking between 4 and 6;

-- The window function is mainly used to solve the TopN query problem
-- Query the name, monthly salary and department number of the top 2 employees with monthly salary in each department
select ename, sal, dno from (
select ename, sal, dno, rank() over (partition by dno order by sal desc) as ranking
from tb_emp
) tb_temp where ranking<=2;

select ename, sal, dno from tb_emp t1
where (select count(*) from tb_emp t2 where t1.dno=t2.dno and t2.sal>t1.sal)<2
order by dno asc, sal desc;