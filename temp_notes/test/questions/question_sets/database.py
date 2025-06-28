
# create a database vs create a table (with exists)
create database if not exists database_name;
create table table_name (column_1 data_type, column_2 data_type...);
# create a table of same structure of another table
create table new_table_name as (select * from table_name where 1=2);
# create a table of same structure and same data of another table
create table new_table_name as (select * from table_name);
# query to find 2nd/3rd/nth highest salary
Mrthod 1 : using sub-query
select max(salary) from employee where salary < (select max(salary) from employee where salary < (select max(salary) from employee));
Method 2 : using limit and offset
select salary from employee order by salary desc limit 1 offset N-1;
Method 3 : using limit
select salary from employee order by salary asc limit N-1,1;
Method 4 : using distinct 
select distinct salary from employee e1 where N-1 = (select count(distinct(e2.salary)) from employee e2 where e2.salary > e1.salary);
# find all employees who also hold the managerial position 
select * from employees where employee_id in (select manager_id from employees);
# find all emplyeess whose name starts with 'A' or 'N'
select * from employees where name like 'A%' or name like 'N%';
# display the current date 
select current_date;
select current_date();
select currdate();
select date(now());
select date(current_timestamp());
# fetch alternate records from a table
select * from table_name where id%2=1; (odd numbers)
select * from table_name where id%2=0; (even numbers)
# find duplicate rows in a table 
select column_name, count(*) from table_name group by column_name having count(*) > 1;  
# delet duplicate rows from a table
delete e1 from employee e1 inner join employee e2 where e1.id < e2.id and e1.name = e2.name;
# find the first 5 and last 5 records from a table
select * from table_name limit 5;
select * from table_name order by id desc limit 5;
# find the distinct record without using distinct keyword
select * from table_name group by column_name;
select dept_id from employee union select dept_id from employee;
select dept_id from employee A where A.id >= all(select B.id from employee B where A.dept_id = B.dept_id) order by dept_id;




table vs fields vs records
primary key vs unique key vs foreign key
select and it's clauses 
where vs having
join - inner join, outer join( left join, right join, full join), cross join, self join
full outer join vs cross join 
delete vs truncate vs drop
aliass
constraints - not null, unique, primary key, foreign key, check, default, index
in vs between 
aggregate functions - count, sum, avg, max, min
subsets in mysql - DDL, DML, DCL, TCL
Types of relationships - one to one, one to many, many to many, self referencing relaationship
DBMS  vs RDBMS
Query
Sub-query & it's types
self join and it's requirements
now() vs current_date() vs current_timestamp() vs current_time()
MOD(dividendd, divisor) as "Value"
char vs varchar vs text
scalar functions - concat, length, lower, upper, round, floor, ceil, sqrt, mod, abs, sign, substring, trim, ltrim, rtrim, lpad, rpad, replace, instr, locate, concat_ws,
scalr functions vs aggregate functions
database vs database schema
SQL vs NoSQL
SQL vs MySQL
DBMS and it's types
zero vs blank space vs null

UNION vs UNION ALL vs minus vs intersect
ACID properties
Normalization and it's types
Denormalization
Index and its types
View in database
OLAP vs OLTP
CTE vs Subquery