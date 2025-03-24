# L1 : Lets Start with SQL- 00:00:17
# L2 : What is SQL- 00:05:24
# L3 : MySQL Installation - 00:08:58
# L4 : Types of SQL Commands- 00:13:11
# L5 : Databases and related SQL commands- 00:18:26
# L6 : Tables and related SQL command- 00:37:08
# L7 : Building a Database- From Tables to data insertion- 00:45:33
# L8 : Datatypes in SQL- 00:53:24
# L9 : Keys in SQL- 01:03:36
# L10 : Constraints in SQL- 01:09:23
# L11 : Foreign Key in SQL- 01:24:32
# L12 : Update Command in SQL- 01:37:35
# L13 : Delete Command in SQL- 01:49:55
# L14 : Select Command in SQL- 01:53:24
# L15 : Where Clause in SQL - 01:55:29
# L16 : ALTER Command in SQL- 01:58:59
# L17 : RENAME Command in SQL- 02:09:09
# L18 : TRUNCATE Command- 02:13:13
# L19 : Difference between TRUNCATE, DELETE & DROP in SQL - 02:16:29
# L20 : Distinct Keyword in SQL- 02:18:31
# L21 : Operators in SQL- 02:23:20
# L22 : Clauses in SQL- 02:39:03
# L23 : Aggregate Functions in SQL- 02:47:50
# L24 : GROUP BY and HAVING clause in SQL - 02:57:35
# L25 : Difference between HAVING and WHERE clause in SQL- 03:08:45
# L26 : Practice Question on clause and Aggregate Function in SQL- 03:11:26
# L27 : General Order of SQL command- 03:23:44
# L28 : Joins in SQL- 03:25:31
# L29 : Inner Join in SQL- 03:31:28
# L30 : Left Outer Join in SQL - 03:37:56
# L31 : Right Outer Join in SQL- 03:41:43
# L32 : Full Outer Join in SQL-   03:44:34
# L33 : Cross Join in SQL- 03:51:46
# L34 : Self Join in SQL-  03:56:54
# L35 : Exclusive Joins in SQL- 04:!0:48
# L36 : UNION and UNION ALL in SQL- 04:21:16
# L37 : Subqueries in SQL-  04:30:16
# L38 : Nth Highest Salary in SQL- 04:45:21
# L39 : Stored Procedure in SQL- 04:52:05
# L40 : Views in SQL- 04:56:36





# ==============



data vs database
relational database vs non-relational databases (NoSQL databases)
sql vs mysql
# DBMS vs RDBMS
'''https://www.geeksforgeeks.org/difference-between-rdbms-and-dbms/'''
SQL vs SEQUEL
# DQL vs DML vs DDL vs DCL vs TCL
'''https://www.geeksforgeeks.org/sql-ddl-dql-dml-dcl-tcl-commands/'''
MySQL Server vs MySQL Workbench
# BASIC TERMINOLOGIES
'''
fields/attributes/columns, record/rows/tuples, constraints, primary key, foreign key, base/referenced table, referencing table, 
'''
# DATA TYPES
'''https://www.w3schools.com/sql/sql_datatypes.asp'''
# KEYS in SQL
# CONSTRAINTS
unique, not null, check, default, primary key, foreign key 
# CASCADE in FOREIGN KEY 
'''
1. CASCADE (FK row entries will be deleated or updated)
create table childrenName(
child_id int primary key, 
base_id int,
foreign key (base_id) references baseTableName(base_id)
on delete cascade
)
create table childrenName(
child_id int primary key, 
base_id int,
foreign key (base_id) references baseTableName(base_id)
on delete cascade
)

2. SET NULL (FK row entries will be set to null)
create table childrenName(
child_id int primary key,
base_id int,
foreign key (base_id) references baseTableName(base_id)
on delete set null

3. RESTRICT / NO ACTION (FK row entries will be restricted)
create table childrenName(
child_id int primary key,
base_id int,
foreign key (base_id) references baseTableName(base_id)
on delete restrict
'''
# refrential integrity
# safemode in sql
'''
SET SQL_SAFE_UPDATES = 0; means that the sql safe mode is off
SET SQL_SAFE_UPDATES = 1; means that the sql safe mode is on
'''







# region COMMANDS 
# use 
use database_name;
# create
create database database_name;
create database if not exists database_name;
create table table_name(column_name datatype constraint, column_name datatype constraint);
create table if not exists table_name(column_name datatype constraint, column_name datatype constraint);
create table table_name(column_name datatype primary key);
create table table_name_1(column_name_1 datatype_1, foreign key (column_name_1) references table_name_parent(column_name_parent));
# drop 
drop database database_name;
drop database if exists database_name;
# show
show databases;
# insert
insert into table_name(column_1, column_2) values(value_1, value_2);
insert into table_name(column_1, column_2) values(value_1, value_2),(value_1, value_2);
# select
select * from table_name;
select column_1,column_2 from table_name;
# show
show databases;
show tables;
# where
select * from table_name where condition;
# update
update table_name set column_1 = value_1, column_2 = value_2 where condition;
# delete
delete from table_name where condition;

# constraints
- unique
create table table_name(column_name datatype unique);
- not null
create table table_name(column_name datatype not null);
- check
create table table_name(column_name datatype check(condition));
- default
create table table_name(column_name datatype default value);
- primary key
create table table_name(column_name datatype primary key);
- foreign key
create table child_table(column_name datatype foreign key references parent_table(column_name));
# create
create database database_name;
# insert 
insert into table_name (column1, column2, column3, ...), (column1, column2, column3, ...);
# select 
select column1, column2, ... from table_name;
select * from table_name;
# update
update table_name set column1 = value1, column2 = value2, ... where condition;
# delete
delete from table_name where condition;
# alter 
alter table table_name add column column_name datatype;
alter table table_name drop column column_name;
alter table table_name rename column column_name to new_column_name;
alter table table_name rename to new_table_name;
alter table table_name modify column column_name datatype;
# rename
rename database database_name to new_database_name;
rename table table_name to new_table_name;
# truncate
truncate table table_name;
# distinct
select distinct column_name from table_name;
# operators
- arithmetic operators
+, -, *, /, %
- comparison operators
=, >, <, >=, <=, !=, <>
- logical operators
and, or, not, in, is null, is not null, 
- bitwise operators
And, or
# like and wildcard operator
select * from table_name where column_name like '%pattern%';
select * from table_name where column_name like '_pattern_';



# endregion


# region QUESTIONS
# -----------
# DELETE vs DROP vs TRUNCATE
'''https://www.geeksforgeeks.org/difference-between-delete-drop-and-truncate/'''
# Constraints
'''https://www.geeksforgeeks.org/sql-constraints/'''
# how to use "use" safely like if exists if there is a non-existant database ?
# SELECT column_1, column_2 FROM table_1, table_2; what happens, is it correct ?
# data types - decimal, unsigned constraint, 
# Binary data type vs boolean data type 
# 




# endregion