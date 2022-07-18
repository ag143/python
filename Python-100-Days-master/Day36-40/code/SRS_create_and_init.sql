-- delete a database named school if it exists
drop database if exists `school`;

-- Create a database named school and set the default character set and sorting method
create database `school` default charset utf8mb4;

-- switch to the school database context
use `school`;

-- create college table
create table `tb_college`
(
`col_id` int unsigned auto_increment comment 'Number',
`col_name` varchar(50) not null comment 'name',
`col_intro` varchar(5000) default '' comment 'introduction',
primary key (`col_id`)
) engine=innodb comment 'College table';

-- create student table
create table `tb_student`
(
`stu_id` int unsigned not null comment 'Student ID',
`stu_name` varchar(20) not null comment 'name',
`stu_sex` boolean default 1 comment 'sex',
`stu_birth` date not null comment 'date of birth',
`stu_addr` varchar(255) default '' comment 'Origin',
`col_id` int unsigned not null comment 'The college you belong to',
primary key (`stu_id`),
foreign key (`col_id`) references `tb_college` (`col_id`)
) engine=innodb comment 'student table';

-- create teacher table
create table `tb_teacher`
(
`tea_id` int unsigned not null comment 'Work ID',
`tea_name` varchar(20) not null comment 'name',
`tea_title` varchar(10) default 'teaching assistant' comment 'title',
`col_id` int unsigned not null comment 'The college you belong to',
primary key (`tea_id`),
foreign key (`col_id`) references `tb_college` (`col_id`)
) engine=innodb comment 'Teacher table';

-- create a class schedule
create table `tb_course`
(
`cou_id` int unsigned not null comment 'Number',
`cou_name` varchar(50) not null comment 'name',
`cou_credit` int unsigned not null comment 'credit',
`tea_id` int unsigned not null comment 'teaching teacher',
primary key (`cou_id`),
foreign key (`tea_id`) references `tb_teacher` (`tea_id`)
) engine=innodb comment 'Class Schedule';

-- Create a course selection record sheet
create table `tb_record`
(
`rec_id` bigint unsigned auto_increment comment 'Course selection record number',
`sid` int unsigned not null comment 'Student ID',
`cid` int unsigned not null comment 'Course ID',
`sel_date` date not null comment 'Course selection date',
`score` decimal(4,1) comment 'Exam Score',
primary key (`rec_id`),
foreign key (`sid`) references `tb_student` (`stu_id`),
foreign key (`cid`) references `tb_course` (`cou_id`),
unique (`sid`, `cid`)
) engine=innodb comment 'Course selection record';

-- Insert college data
insert into `tb_college`
    (`col_name`, `col_intro`)
values
    ('School of Computer', 'The School of Computer Science established the computer major in 1958, the Department of Computer Science in 1981, and the School of Computer Science in 1998. In May 2005, in order to further integrate teaching and research resources, the school decided that the School of Computer and Software Administration The team merges and operates in a unified manner, and implements a model of independent operation of teaching and student management. The college consists of three departments: Department of Computer Science and Technology, Department of Internet of Things Engineering, Department of Computational Finance; two research institutes: Institute of Graphics and Graphics, Cyberspace Security Research Institute (established in 2015); three teaching experiment centers: Computer Basic Teaching Experiment Center, IBM Technology Center, and Computer Professional Experiment Center.'),
    ('School of Foreign Languages', 'School of Foreign Languages ​​has 7 teaching units and 6 undergraduate majors with a combination of arts and sciences; 1 first-level discipline doctorate award point, 3 second-level discipline doctorate award points, 5 first-level discipline master's degrees Degree authorization points, 5 secondary discipline master's degree authorization points, 5 master's professional authorization areas, and 2 master's degree (MTI) majors; there are more than 210 faculty members, including more than 80 professors and associate professors. More than 60% of the full-time teachers are teachers with doctoral degrees and those who are currently studying for doctoral degrees from prestigious universities in China and abroad.'),
    ('School of Economics and Management', 'The predecessor of the School of Economics is the Economics Department founded in 1905; the late economists Peng Dixian, Zhang Yujiu, Jiang Xuemo, Hu Jichuang, Tao Dayong, Hu Daiguang, and contemporary scholars Liu Shibai have taught or study.');

-- insert student data
insert into `tb_student`
    (`stu_id`, `stu_name`, `stu_sex`, `stu_birth`, `stu_addr`, `col_id`)
values
    (1001, 'Yang Guo', 1, '1990-3-4', 'Hunan Changsha', 1),
    (1002, 'Let me go', 1, '1992-2-2', 'Changsha, Hunan', 1),
    (1033, 'Wang Yuyan', 0, '1989-12-3', 'Chengdu, Sichuan', 1),
    (1572, 'Yue Buqun', 1, '1993-7-19', 'Shaanxi Xianyang', 1),
    (1378, 'Ji Yanran', 0, '1995-8-12', 'Sichuan Mianyang', 1),
    (1954, 'Lin Pingzhi', 1, '1994-9-20', 'Putian, Fujian', 1),
    (2035, 'Eastern Unbeaten', 1, '1988-6-30', null, 2),
    (3011, 'Lin Zhennan', 1, '1985-12-12', 'Putian, Fujian', 3),
    (3755, 'Xiang Shaolong', 1, '1993-1-25', null, 3),
    (3923, 'Yang Buhui', 0, '1985-4-17', 'Chengdu, Sichuan', 3);

-- insert teacher data
insert into `tb_teacher`
    (`tea_id`, `tea_name`, `tea_title`, `col_id`)
values
    (1122, 'Zhang Sanfeng', 'Professor', 1),
    (1133, 'Song Yuanqiao', 'Associate Professor', 1),
    (1144, 'Yang Xiao', 'Associate Professor', 1),
    (2255, 'Fan Yao', 'Associate Professor', 2),
    (3366, 'Wei Yixiao', default, 3);

-- insert course data
insert into `tb_course`
    (`cou_id`, `cou_name`, `cou_credit`, `tea_id`)
values
    (1111, 'Python programming', 3, 1122),
    (2222, 'Web Front-End Development', 2, 1122),
    (3333, 'operating system', 4, 1122),
    (4444, 'computer network', 2, 1133),
    (5555, 'Compilation principle', 4, 1144),
    (6666, 'Algorithms and Data Structures', 3, 1144),
    (7777, 'Business French', 3, 2255),
    (8888, 'Cost Accounting', 2, 3366),
    (9999, 'Auditing', 3, 3366);

-- Insert course selection data
insert into `tb_record`
    (`sid`, `cid`, `sel_date`, `score`)
values
    (1001, 1111, '2017-09-01', 95),
    (1001, 2222, '2017-09-01', 87.5),
    (1001, 3333, '2017-09-01', 100),
    (1001, 4444, '2018-09-03', null),
    (1001, 6666, '2017-09-02', 100),
    (1002, 1111, '2017-09-03', 65),
    (1002, 5555, '2017-09-01', 42),
    (1033, 1111, '2017-09-03', 92.5),
    (1033, 4444, '2017-09-01', 78),
    (1033, 5555, '2017-09-01', 82.5),
    (1572, 1111, '2017-09-02', 78),
    (1378, 1111, '2017-09-05', 82),
    (1378, 7777, '2017-09-02', 65.5),
    (2035, 7777, '2018-09-03', 88),
    (2035, 9999, '2019-09-02', null),
    (3755, 1111, '2019-09-02', null),
    (3755, 8888, '2019-09-02', null),
    (3755, 9999, '2017-09-01', 92);