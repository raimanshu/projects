
# create a database vs create a table (with exists)
create database if not exists database_name;
create table table_name (column_1 data_type, column_2 data_type...);
# create a table of same structure of another table
create table new_table_name as (select * from table_name where 1=2);
# create a table of same structure and same data of another table
create table new_table_name as (select * from table_name);
# query to find 2nd/3rd/nth highest salary
select max(salary) from employee where salary < (select max(salary) from employee where salary < (select max(salary) from employee));
select salary from employee order by salary desc limit 1 offset N-1;
select salary from employee order by salary asc limit N-1,1;
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



SQL 
Database
SQL vs NoSQL
How SQL Works? - Query Dispatcher, Optimization Engines, Classic Query Engine, SQL Query Engine

DBMS vs RDBMS
table 
Records or rows 
Fields or attributes
NULL 
Constraints - not null, unique, primary key, foreign key, check, default, index
Data Integrity - Entity Integrity, Referential Integrity, Domain Integrity, User-Defined Integrity
Normalization - 1NF, 2NF, 3NF, 4NF or BCNF

Data types - Numeric, String and Date Time
https://www.tutorialspoint.com/sql/sql-data-types.htm
SQL Operators - Arithmetic, Comparison, Logical
SQL Expressions - Boolean, Numeric and Date time
SQL Comments - --..., /* ... */

DCL vs DML vs DCL vs TCL vs DQL -> civil engineer child vs Mother vs Security Guard vs Father vs curious kids
DCL - create, drop, alter, rename, truncate, 
DML - insert, update, delete,
DQL - select
❌ DCL - grant, revoke,
TCL - commit, rollback, savepoint
DQL - select

# region SQL DATABASE 
# CREATE database - create database, create database with exists, create multiple database 
'''
CREATE DATABASE DatabaseName;

DROP DATABASE IF NOT EXISTS DatabaseName;

CREATE DATABASE DatabaseName1, DatabaseName2;
'''
# DROP database - drop database, drop database with exists, drop multiple database
'''
DROP DATABASE DatabaseName;

DROP DATABASE IF EXISTS DatabaseName;

DROP DATABASE DatabaseName1, DatabaseName2;
'''
# select database - select database, select database if not exists will throw error
'''
USE DatabaseName;

❌ USE DatabaseName; throw error if not exists 
'''
# rename database - using alter and modify, using rename...to...
'''
ALTER DATABASE OldDatabaseName MODIFY NAME = NewDatabaseName;

RENAME DATABASE OldDatabaseName TO NewDatabaseName;
'''
# show database - 
'''
SHOW DATABASES [LIKE 'pattern' | WHERE expr] ;

SHOW SCHEMAS [LIKE 'pattern' | WHERE expr] ;
'''
# backup database - Full Backup, ❌ Differential Backup, ❌ Transaction Log (T-log) backup
'''
BACKUP DATABASE database_name
TO DISK = 'filepath'
GO

BACKUP DATABASE my_db
TO medium = 'filepath'
WITH DIFFERENTIAL;
GO

BACKUP LOG database_name
TO medium = 'filepath';
GO

RESTORE DATABASE database_name
FROM DISK = 'filepath';
GO

BACKUP DATABASE database_name
TO DISK = 'filepath'
GO
'''
# endregion




# region SQL TABLE
# Create Table - create table, create table if not exists, create table from existing table
'''
CREATE TABLE table_name(
   column1 datatype,
   column2 datatype,
   column3 datatype,
   .....
   columnN datatype,
   PRIMARY KEY( one or more columns )
);

CREATE TABLE IF NOT EXISTS table_name(
   column1 datatype,
   column2 datatype,
   column3 datatype,
   .....
   columnN datatype,
   PRIMARY KEY( one or more columns )
);

CREATE TABLE NEW_TABLE_NAME AS
SELECT [column1, column2...columnN]
FROM EXISTING_TABLE_NAME
WHERE Condition;
'''
# Show Tables - shaow all tables, show table description
'''
SHOW TABLES;

DESC table_name;
'''
# Rename Table - rename table_name
'''
RENAME TABLE table_name TO new_table_name;
'''
# Truncate Table - TRUNCATE vs DELETE, TRUNCATE vs DROP https://www.tutorialspoint.com/sql/sql-truncate-table.htm
'''
TRUNCATE TABLE table_name;
'''
# Clone Table - Simple Cloning, Shallow Cloning, Deep Cloning
'''
CREATE TABLE new_table SELECT * FROM original_table;

CREATE TABLE new_table LIKE original_table;

CREATE TABLE new_table LIKE original_table;
INSERT INTO new_table SELECT * FROM original_table;

'''
# Temporary Table or Heap tables - Local Temporary Tables, ❌ Global Temporary Tables
'''
CREATE TEMPORARY TABLE table_name(
   column1 datatype,
   column2 datatype,
   column3 datatype,
   .....
   columnN datatype,
   PRIMARY KEY( one or more columns )
);

DROP TEMPORARY TABLE table_name;

CREATE TABLE #table_name(
   column1 datatype,
   column2 datatype,
   column3 datatype,
   .....
   columnN datatype,
   PRIMARY KEY( one or more columns )
);

CREATE TABLE ##table_name(
   column1 datatype,
   column2 datatype,
   column3 datatype,
   .....
   columnN datatype,
   PRIMARY KEY( one or more columns )
);

'''
# Alter Table -
'''
ALTER TABLE table_name [alter_option ...];

ALTER TABLE table_name ADD column_name datatype;

ALTER TABLE table_name DROP COLUMN column_name;

ALTER TABLE table_name RENAME [TO|AS] new_table_name;

ALTER TABLE table_name ADD INDEX index_name [column_name];

ALTER TABLE table_name DROP INDEX index_name;

ALTER TABLE table_name 
ADD CONSTRAINT constraint_name
PRIMARY KEY (column1, column2...);

ALTER TABLE table_name DROP PRIMARY KEY;

ALTER TABLE table_name 
ADD CONSTRAINT constraint_name 
UNIQUE(column1, column2...);

ALTER TABLE table_name DROP CONSTRAINT constraint_name; 

ALTER TABLE table_name 
RENAME COLUMN old_column_name to new_column_name;

ALTER TABLE table_name ALTER COLUMN column_name datatype;
'''
# Drop Table -
'''
DROP TABLE table_name;

DROP TABLE IF EXISTS table_name;

DROP TEMPORARY TABLE TEMP_TABLE;
'''
# Delete Table -
'''
DELETE FROM table_name;

DELETE FROM table_name
WHERE condition;

DELETE FROM table_name
WHERE condition1 AND condition2 OR ... conditionN;
'''
# Constraints - Null, Unique, Default, Check, Primary Key, Foreign Key, Index
'''
CREATE TABLE table_name (
   column1 datatype constraint,
   column2 datatype constraint,
   ....
   columnN datatype constraint
);

CREATE TABLE CUSTOMERS (
   ID INT NOT NULL,
   NAME VARCHAR (20) NOT NULL,
   AGE INT NOT NULL,
   ADDRESS CHAR (25),
   SALARY DECIMAL (18, 2)
);

CREATE TABLE CUSTOMERS (
   ID INT NOT NULL UNIQUE,
   NAME VARCHAR (20) NOT NULL,
   AGE INT NOT NULL,
   ADDRESS CHAR (25),
   SALARY DECIMAL (18, 2)
);

CREATE TABLE CUSTOMERS (
   ID INT NOT NULL UNIQUE,
   NAME VARCHAR (20) DEFAULT 'Not Available',
   AGE INT NOT NULL,
   ADDRESS CHAR (25),
   SALARY DECIMAL (18, 2)
);

CREATE TABLE CUSTOMERS(
   ID          INT NOT NULL,
   NAME        VARCHAR (20) NOT NULL,
   AGE         INT NOT NULL,
   ADDRESS     CHAR (25),
   SALARY      DECIMAL (18, 2),
   PRIMARY KEY (ID)
);

CREATE TABLE ORDERS (
   ID INT NOT NULL,
   DATE DATETIME,
   CUSTOMER_ID INT FOREIGN KEY REFERENCES CUSTOMERS(ID),
   AMOUNT DECIMAL,
   PRIMARY KEY (ID)
);

CREATE TABLE CUSTOMERS(
   ID          INT NOT NULL,
   NAME        VARCHAR (20) NOT NULL,
   AGE         INT NOT NULL CHECK(AGE>=18),
   ADDRESS     CHAR (25),
   SALARY      DECIMAL (18, 2),
   PRIMARY KEY (ID)
);

CREATE INDEX idx_age ON CUSTOMERS ( AGE );

ALTER TABLE CUSTOMERS DROP CONSTRAINT PRIMARY KEY;
'''
# endregion




# region SQL QUERIES
# Insert Query
'''
INSERT INTO TABLE_NAME (column1, column2...columnN) 
VALUES (value1, value2...valueN);

INSERT INTO TABLE_NAME 
VALUES (value1,value2...valueN);

INSERT INTO first_table_name [(column_name(s))]
SELECT column1, column2, ...columnN
FROM second_table_name
[WHERE condition];

INSERT INTO first_table_name TABLE second_table_name;

INSERT INTO BUYERS (ID, NAME, AGE) 
SELECT ID, NAME, AGE FROM CUSTOMERS;
'''
# Select Query
'''
SELECT column1, column2, columnN FROM table_name;

SELECT * FROM table_name;

SELECT mathematical_expression;

SELECT column_name 
AS alias_name 
FROM table_name;
'''
# Select Into - NOT supported by MySQL
# Insert Into Select
'''
INSERT INTO table_new 
SELECT (column1, column2, ...columnN) 
FROM table_old;

'''
# Update Query
'''
UPDATE table_name
SET column1 = value1, column2 = value2,..., columnN = valueN
WHERE [condition];

'''
# Delete Query
'''
DELETE FROM table_name WHERE [condition];

DELETE CUSTOMERS, ORDERS FROM CUSTOMERS
INNER JOIN ORDERS ON ORDERS.CUSTOMER_ID = CUSTOMERS.ID
WHERE CUSTOMERS.SALARY > 2000;
'''
# Sorting Data 
'''
SELECT column-list 
FROM table_name 
[WHERE condition] 
[ORDER BY column1, column2, .. columnN] [ASC | DESC];

SELECT * FROM CUSTOMERS
ORDER BY ( CASE ADDRESS
   WHEN 'DELHI' 	 THEN 1
   WHEN 'BHOPAL' 	 THEN 2
   WHEN 'KOTA' 	 THEN 3
   WHEN 'AHMEDABAD' THEN 4
   WHEN 'Hyderabad' 	THEN 5
   ELSE 100 END) ASC, ADDRESS DESC;
'''
# endregion 




# region SQL VIEWS
# Create Views
'''
CREATE VIEW view_name AS
SELECT column1, column2....
FROM table_name
WHERE [condition];

CREATE VIEW MY_VIEW AS
SELECT name, age
FROM  CUSTOMERS
WHERE age >= 25
WITH CHECK OPTION;
'''
# Update Views 
'''
UPDATE view_name
SET column1 = value1, column2 = value2...., columnN = valueN
WHERE [condition];
'''
# DROP VIEWS
'''
DROP VIEW view_name;

DROP VIEW [IF EXISTS] view_name;

DELETE FROM view_name WHERE condition;
'''
# RENAME VIEWS
'''
RENAME TABLE old_view_name To new_view_name;

'''
# endregion 



# region SQL Operators and Clauses
# WHERE Clause
'''
DML_Statement column1, column2,... columnN
FROM table_name
WHERE [condition];

SELECT column1, column2, ...
FROM table_name
WHERE condition;

UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;

WHERE column_name IN (value1, value2, ...);

WHERE column_name NOT IN (value1, value2, ...);

WHERE column_name LIKE pattern;

WHERE (condition1 OR condition2) AND condition3;
'''
# TOP Clause - NOT supported by MYSQL
# DISTINCT Keyword
'''
SELECT DISTINCT column1, column2,.....columnN 
FROM table_name;

SELECT COUNT(DISTINCT column_name) 
FROM table_name WHERE condition;
'''
# ORDER BY Clause
'''
SELECT column-list
FROM table_name
[ORDER BY column1, column2, .. columnN] [ASC | DESC];

SELECT * FROM CUSTOMERS ORDER BY AGE ASC, SALARY DESC;

SELECT column1, column2, ...
FROM table_name
ORDER BY column_name1 [ASC | DESC], column_name2 [ASC | DESC], ...
LIMIT N;

SELECT * FROM CUSTOMERS ORDER BY (
CASE ADDRESS
   WHEN 'MUMBAI' THEN 1
   WHEN 'DELHI' THEN 2
   WHEN 'HYDERABAD' THEN 3
   WHEN 'AHMEDABAD' THEN 4
   WHEN 'INDORE' THEN 5
   WHEN 'BHOPAL' THEN 6
   WHEN 'KOTA' THEN 7
   ELSE 100 END
);
'''
# GROUP BY Clause
'''
SELECT column_name(s)
FROM table_name
GROUP BY column_name(s);

SELECT AGE, COUNT(Name) FROM CUSTOMERS GROUP BY AGE;

SELECT AGE, MAX(salary) AS MAX_SALARY 
FROM CUSTOMERS GROUP BY AGE;

SELECT ADDRESS, AGE, SUM(SALARY) AS TOTAL_SALARY 
FROM CUSTOMERS GROUP BY ADDRESS, AGE;

SELECT column1, column2, ..., aggregate_function(columnX) AS alias
FROM table
GROUP BY column1, column2, ...
ORDER BY column1 [ASC | DESC], column2 [ASC | DESC], ...;
'''
# HAVING Clause
'''
SELECT column1, column2, aggregate_function(column)
FROM table_name
GROUP BY column1, column2
HAVING condition;

Order - 
SELECT
FROM
WHERE
GROUP BY
HAVING
ORDER BY
'''
# AND and OR Conjunctive Operators
'''
WHERE [condition1] AND [condition2];

WHERE [condition1] AND [condition2]...AND [conditionN];

SELECT * FROM CUSTOMERS 
WHERE NOT (SALARY > 4500 AND AGE < 26);

UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition1 AND condition2 AND ...;

WHERE (condition1 OR condition2) AND condition3;

DELETE FROM table_name
WHERE column1 = 'value1' OR column2 = 'value2';
'''
# BOOLEAN (BIT) Operator
'''
CREATE TABLE CARS (
   ID INT NOT NULL,
   Name VARCHAR(150),
   IsRed BOOLEAN
);
'''
# LIKE Operator - 	% (zero, one or multiple), _ (single number or character)
'''
WHERE student_name LIKE 'K%';

SELECT column1, column2, ...
FROM table_name
WHERE columnn LIKE specified_pattern;

SELECT column1, column2, ...
FROM table_name
WHERE column1 LIKE pattern1 OR column2 LIKE pattern2 OR ...;

SELECT column1, column2, ...
FROM table_name
WHERE column1 NOT LIKE pattern;

SELECT column1, column2, ...
FROM table_name
WHERE column1 LIKE 'pattern ESCAPE escape_character';

SELECT * FROM EMPLOYEE 
WHERE BONUS_PERCENT LIKE'%!%%' ESCAPE '!';
'''
# IN Operator
'''
WHERE column_name IN (value1, value2, value3, ...);

WHERE column_name NOT IN (value1, value2, ...);

WHERE column_name IN (subquery);
'''
# ANY, ALL Operators
'''
Column_name operator ANY (subquery);

SELECT * FROM CUSTOMERS 
WHERE SALARY > ANY (SELECT SALARY FROM CUSTOMERS WHERE AGE = 32);

Column_name operator ALL (subquery);
'''
# EXISTS Operator
'''
WHERE EXISTS (subquery);

SELECT * FROM CUSTOMERS WHERE 
EXISTS (
   SELECT PRICE FROM CARS 
   WHERE CARS.ID = CUSTOMERS.ID AND PRICE > 2000000
);

UPDATE CUSTOMERS SET NAME = 'Kushal' 
WHERE EXISTS (
   SELECT NAME FROM CARS WHERE CUSTOMERS.ID = CARS.ID
);

DELETE FROM CUSTOMERS WHERE 
EXISTS (
   SELECT * FROM CARS 
   WHERE CARS.ID = CUSTOMERS.ID AND CARS.PRICE = 2250000
);

WHERE NOT EXISTS (subquery);
'''
# CASE
'''
CASE
   WHEN condition1 THEN statement1,
   WHEN condition2 THEN statement2,
   WHEN condition THEN statementN
   ELSE result
END;

SELECT NAME, AGE,
CASE 
WHEN AGE > 30 THEN 'Gen X'
WHEN AGE > 25 THEN 'Gen Y'
WHEN AGE > 22 THEN 'Gen Z'
ELSE 'Gen Alpha' 
END AS Generation
FROM CUSTOMERS;

SELECT * FROM CUSTOMERS
ORDER BY
(CASE
    WHEN NAME LIKE 'k%' THEN NAME
    ELSE ADDRESS
END);

SELECT 
   CASE 
      WHEN SALARY <= 4000 THEN 'Lowest paid'
      WHEN SALARY > 4000 AND SALARY <= 6500 THEN 'Average paid'
   ELSE 'Highest paid' 
      END AS SALARY_STATUS,
   SUM(SALARY) AS Total
   FROM CUSTOMERS
   GROUP BY 
   CASE 
      WHEN SALARY <= 4000 THEN 'Lowest paid'
      WHEN SALARY > 4000 AND SALARY <= 6500 THEN 'Average paid'
   ELSE 'Highest paid'
END;

SELECT NAME, ADDRESS, 
   CASE 
      WHEN AGE < 25 THEN 'Intern'
      WHEN AGE >= 25 and AGE <= 27 THEN 'Associate Engineer'
      ELSE 'Senior Developer'
   END as Designation
FROM CUSTOMERS
WHERE SALARY >= 2000;

UPDATE CUSTOMERS
SET SALARY= 
CASE AGE
WHEN 25 THEN 17000
WHEN 32 THEN 25000
ELSE 12000
END;

INSERT INTO CUSTOMERS (ID, NAME, AGE, ADDRESS, SALARY)
VALUES (10, 'Viren', 28, 'Varanasi', 
   CASE 
      WHEN AGE >= 25 THEN 23000
      ELSE 14000
   END
);
'''
# NOT OPERATOR 
'''
NOT [CONDITION or BOOLEAN EXPRESSION];

SELECT * FROM CUSTOMERS WHERE NOT (SALARY > 2000.00);
SELECT * FROM CUSTOMERS WHERE NAME NOT LIKE 'K%';
SELECT * FROM CUSTOMERS WHERE AGE NOT IN (25, 26, 32);
SELECT * FROM CUSTOMERS WHERE AGE IS NOT NULL;
SELECT * FROM CUSTOMERS 
WHERE SALARY NOT BETWEEN 1500.00 AND 2500.00;
SELECT * FROM CUSTOMERS WHERE NOT EXISTS (
SELECT CUSTOMER_ID FROM ORDERS 
WHERE ORDERS.CUSTOMER_ID = CUSTOMERS.ID);
'''
# NOT EQUAL - <> , !=
'''
WHERE expression1 != expression2;
'''
# IS NULL
'''
SELECT column_name1, column_name2, column_name3, ... , column_nameN
FROM table_name
WHERE column_nameN IS NULL;

DELETE FROM table_name
WHERE columnname1, columnname2, ... IS NULL;
'''
# IS NOT NULL
'''
SELECT column_names
FROM table_name
WHERE column_name IS NOT NULL;

SELECT COUNT(column_name)
FROM table_name
WHERE condition IS NOT NULL;

DELETE FROM table_name
WHERE columnname1, columnname2, ... IS NOT NULL;

UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE columnname1, columnname2, ... IS NOT NULL;
'''
# NOT NULL Constraint
'''
CREATE TABLE table_name (
   column1 datatype NOT NULL,
   column2 datatype,
   column3 datatype NOT NULL,
   ...
);

ALTER TABLE table_name
MODIFY COLUMN column_name datatype NULL;

ALTER TABLE table_name
MODIFY COLUMN column_name datatype NOT NULL;
'''
# BETWEEN Operator
'''
SELECT column1, column2, column3,....columnN
FROM table_name
WHERE column BETWEEN value1 AND value2;

SELECT column_name1, column_name2, column_name3,......column_nameN
FROM table_name
WHERE column_name NOT BETWEEN value1 AND value2;
'''
# UNION 
'''
SELECT column1 [, column2 ]
FROM table1 [, table2 ]
[WHERE condition]
UNION
SELECT column1 [, column2 ]
FROM table1 [, table2 ]
[WHERE condition];

SELECT column1, column2, column3
FROM table1
WHERE column1 = 'value1'
UNION
SELECT column1, column2, column3
FROM table2
WHERE column1 = 'value2';
'''
# ❌ UNION vs UNION ALL
'''
SELECT * FROM table1
UNION ALL
SELECT * FROM table2;
'''
# ❌ INTERSECT 
'''
SELECT column1, column2,..., columnN
FROM table1, table2,..., tableN
INTERSECT
SELECT column1, column2,..., columnN
FROM table1, table2,..., tableN
'''
# EXCEPT Operator - NOT Supported in MYSQL
# Alias
'''
SELECT column1, column2....
FROM table_name AS alias_name;

SELECT column_name AS alias_name
FROM table_name;

SELECT column_name(s)
FROM my_table a, my_table b
ON a.join_column = b.join_column;
'''
# endregion




# region SQL JOINS
# INNER JOIN - Equijoin or join
'''
SELECT column_name(s)
FROM table1
INNER JOIN table2
ON table1.column_name = table2.column_name;

SELECT column1, column2, column3... 
FROM table1
INNER JOIN table2
ON condition_1
INNER JOIN table3
ON condition_2
....
....
INNER JOIN tableN
ON condition_N;
'''
# LEFT  JOIN
'''
SELECT column_name(s)
FROM table1
LEFT JOIN table2
ON table1.column_name = table2.column_name;

SELECT column1, column2, column3... 
FROM table1
LEFT JOIN table2
ON condition_1
LEFT JOIN table3
ON condition_2
....
....
LEFT JOIN tableN
ON condition_N;
'''
# RIGHT JOIN
'''
SELECT table1.column1, table2.column2...
FROM table1
RIGHT JOIN table2
ON table1.common_field = table2.common_field;

SELECT column1, column2, column3... 
FROM table1
RIGHT JOIN table2
ON condition_1
RIGHT JOIN table3
ON condition_2
....
....
RIGHT JOIN tableN
ON condition_N;
'''
# ❌ FULL JOIN
'''
SELECT column_name(s)
FROM table1
FULL JOIN table2
ON table1.column_name = table2.column_name;

SELECT column1, column2, column3... 
FROM table1
FULL JOIN table2
ON condition_1
FULL JOIN table3
ON condition_2
....
....
FULL JOIN tableN
ON condition_N;
'''
# ❌ CROSS JOIN
'''
SELECT column_name(s)
FROM table1
CROSS JOIN table2;
'''
# ❌ SELF JOIN
'''
SELECT column_name(s)
FROM table1 a, table1 b
WHERE a.common_field = b.common_field;

SELECT column_name(s)
FROM table1 a, table1 b
WHERE a.common_field = b.common_field
ORDER BY column_name;
'''
# ❌ DELETE JOIN
'''
DELETE table(s)
FROM table1 JOIN table2
ON table1.common_field = table2.common_field;
'''
# ❌ UPDATE JOIN
'''
UPDATE table(s)
JOIN table2 ON table1.join_column = table2.join_column
SET table1.column1 = table2.new_value1, 
    table1.column2 = table2.new_value2;

    UPDATE table(s)
JOIN table2 ON column3 = column4
SET table1.column1 = value1, table1.column2 = value2, ...
WHERE condition;

UPDATE tables(s)
SET column1 = value1, column2 = value2, ...
FROM table1
JOIN table2 ON table1.join_column = table2.join_column;
# LEFT JOIN VS RIGHT JOIN
https://www.tutorialspoint.com/sql/sql-leftjoin-vs-rightjoin.htm
# UNION VS JOIN
https://www.tutorialspoint.com/sql/sql-union-vs-join.htm
'''

# endregion




# region SQL KEYS
# UNIQUE KEY
'''
- similar to the primary key in a table, but it can accept NULL values, whereas the primary key does not.
- accepts only one NULL value.
- cannot have duplicate values.
- can also be used as a foreign key in another table.
- a table can have more than one Unique column.

CREATE TABLE table_name(
   column1 datatype UNIQUE KEY,
   column2 datatype,
   .....
   .....
   columnN datatype
);

CREATE TABLE table_name(
   column1 datatype UNIQUE KEY,
   column2 datatype UNIQUE KEY,
   .....
   .....
   columnN datatype
);

ALTER TABLE table_name ADD CONSTRAINT 
UNIQUE_KEY_NAME UNIQUE (column_name);

ALTER TABLE table_name DROP CONSTRAINT UNIQUE_KEY_NAME;
'''
# PRIMARY KEY
'''
- contains only a unique value.
- can not be null.
- one table can have only one Primary Key.
-  primary key length cannot be more than 900 bytes.

CREATE TABLE table_name(
   column1 datatype,
   column2 datatype,
   column3 datatype,
   .....
   columnN datatype,
   PRIMARY KEY(column_name)
);

ALTER TABLE table_name ADD CONSTRAINT PRIMARY KEY (column_name);

ALTER TABLE table_name DROP PRIMARY KEY;
'''
# FOREIGN KEY
'''
- Foreign Key is used to reduce the redundancy (or duplicates) in the table.
- helps to normalize (or organize the data in a database) the data in multiple tables.

CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    ...
    CONSTRAINT fk_name 
	FOREIGN KEY (column_name) 
	REFERENCES referenced_table(referenced_column)
);

ALTER TABLE TABLE2 
ADD CONSTRAINT[symbol] 
FOREIGN KEY(column_name) 
REFERENCES TABLE1(column_name);


ALTER TABLE table_name DROP FOREIGN KEY (constraint symbol);
'''
# PRIMARY VS FOREIGN KEY
'''
https://www.tutorialspoint.com/sql/sql-foreign-key.htm
'''
# COMPOSITE KEY
'''
- created by combining more than one Candidate Key.
- each Candidate Key (or column) that makes up a Composite Key may or may not be a Foreign Key. However, if all the columns of the Composite Key are Foreign Keys in their own right, then the Composite Key is known as a Compound Key.
- a Composite Key cannot be NULL; i.e. any column of the Composite Key must not contain NULL values.
- the individual columns making up the Composite Key can contain duplicate values, but, the combination of these columns must be unique across the database table.

CREATE TABLE table_name(
   column1 datatype,
   column2 datatype,
   column3 datatype,
   .....
   columnN datatype,
   CONSTRAINT composite_key_name,
   PRIMARY KEY(column_name)
);

ALTER TABLE table_name DROP PRIMARY KEY;

ALTER TABLE table_name DROP composite_key_name;
'''
# ALTERNATE KEY
'''
The alternate key does not allow duplicate values.
A table can have more than one alternate keys.
The alternate key can contain NULL values unless the NOT NULL constraint is set explicitly.
All alternate keys can be candidate keys, but all candidate keys can not be alternate keys.
The primary key, which is also a candidate key, can not be considered as an alternate key.
'''
# COMPOUND KEY
# endregion

# region SQL INDEX 
# INDEXES 
Indexes should not be used on small tables.

They should not be used on tables that have frequent, large batch updates or insert operations.

Indexes should not be used on columns that contain a high number of NULL values.

Columns that are frequently manipulated should not be indexed.

Unique Index

Single-Column Index

Composite Index

Implicit Index

CREATE INDEX index_name ON table_name;

CREATE UNIQUE INDEX index_name
on table_name (column_name);

CREATE INDEX index_name
ON table_name (column_name);
CREATE INDEX index_name
on table_name (column1, column2);

# CREATE INDEX 
CREATE INDEX index_name 
ON table_name (column_name1, column_name2,... column_nameN);

# Drop Index
DROP INDEX index_name ON table_name;

# Show Indexes
SHOW INDEX FROM table_name;

# Unique Indexes
If the unique index is only created on a single column, the rows in that column will be unique.
If a single column contains NULL in multiple rows, we cannot create a unique index on that column.
If the unique index is created on multiple columns, the combination of rows in these columns will be unique.
We cannot create a unique index on multiple columns if the combination of columns contains NULL in more than one row.

CREATE UNIQUE INDEX index_name
ON table_name (column1, column2, ..., columnN);

#  Clustered Index
It is recommended to have only one clustered index on a table. If we create multiple clustered indexes on the same table, the table will have to store the same data in multiple orders which is not possible.
When we try to create a primary key constraint on a table, a unique clustered index is automatically created on the table. However, the clustered index is not the same as a primary key. A primary key is a constraint that imposes uniqueness on a column or set of columns, while a clustered index determines the physical order of the data in the table.

CREATE INDEX index_name ON table_name(column_name [asc|desc])

# Non-Clustered Index
The non-clustered indexes are a type of index used in databases to speed up the execution time of database queries.
These indexes require less storage space than clustered indexes because they do not store the actual data rows.
We can create multiple non-clustered indexes on a single table.

CREATE NONCLUSTERED INDEX index_name 
ON table_name (column_name)

# endregion

# SQL FUNCTIONS
# Date Functions 
https://www.tutorialspoint.com/sql/sql-date-functions.htm
# String Functions
https://www.tutorialspoint.com/sql/sql-string-functions.htm
# Aggregate Functions
https://www.tutorialspoint.com/sql/sql-aggregate-functions.htm
# Numeric Functions 
https://www.tutorialspoint.com/sql/sql-numeric-functions.htm
# Text and Image Functions
https://www.tutorialspoint.com/sql/sql-text-image-functions.htm
# Statistical Functions 
https://www.tutorialspoint.com/sql/sql-statistical-functions.htm
# Logical Functions 
https://www.tutorialspoint.com/sql/sql-logical-funtions.htm
# Cursor Functions
https://www.tutorialspoint.com/sql/sql-cursor-functions.htm
# JSON Functions
https://www.tutorialspoint.com/sql/sql-json-functions.htm
# Conversion Functions 
https://www.tutorialspoint.com/sql/sql-conversion-functions.htm
# Datatype Functions 
https://www.tutorialspoint.com/sql/sql-datatype-functions.htm


# ADVANCED SQL 
# WILDCARDS - 
%, _,  special characters used as substitutes for one or more characters in a string
# Injection - 
type of security attack that exploits a vulnerability in a database by executing malicious queries
# Hosting - 
nothing but a means to manage any RDBMS linked to your website using SQL. If the website has an access to a RDBMS, any data from the website you created will be stored and retrieved from this database.
# MIN() - MAX() function 
used to compare values in a set and, retrieve the maximum and minimum values respectively.
# Null Functions - 
used to perform operations on NULL values that are stored in the database tables.
ISNULL() - returns 0 and 1 depending on whether the expression is null or not
COALESCE() -  returns the first occurred NON-NULL expression among its arguments. If all the expressions are NULL, then the COALESCE() function will return NULL.
COALESCE(expression_1, expression_2, expression_n);
NULLIF() - compares two expressions. If both expressions are the same, it returns NULL. Otherwise, it returns the first expression.
NULLIF(expression_1, expression_2);
IFNULL() - replaces the NULL values in a database table with a specific value. This function accepts two arguments. If the first argument is a NULL value, it is replaced with the second argument. Otherwise, the first argument is returned as it is.
IFNULL(column_name, value_to_replace);
# Stored Procedures - https://www.tutorialspoint.com/sql/sql-stored-procedures.htm
group of pre-compiled SQL statements (prepared SQL code) that can be reused by simply calling it whenever needed.
DELIMITER //
CREATE PROCEDURE procedure_name(parameter1 datatype, parameter2 datatype, ...)
BEGIN
   -- SQL statements to be executed
END
DELIMITER ;
# Transaction - https://www.tutorialspoint.com/sql/sql-transactions.htm
# SQL Subqueries -https://www.tutorialspoint.com/sql/sql-sub-queries.htm
# Handling Duplicates - https://www.tutorialspoint.com/sql/sql-handling-duplicates.htm
# Cursors - https://www.tutorialspoint.com/sql/sql-cursors.htm
# Common Table Expression (CTE) - https://www.tutorialspoint.com/sql/sql-common-table-expression.htm
# Group By vs Order By - https://www.tutorialspoint.com/sql/sql-group-by-vs-order-by.htm
# IN vs EXISTS - https://www.tutorialspoint.com/sql/sql-in-vs-exists.htm
# Database Tuning - https://www.tutorialspoint.com/sql/sql-database-tuning.htm
INTERSECTION vs INNER JOIN - 
UNION vs UNION ALL
FULL JOIN vs UNION ALL 

View
Index 
stored procedures or Routines or functions 