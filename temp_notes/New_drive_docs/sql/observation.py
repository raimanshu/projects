
# region RECOMMENDED LINKS

'''
https://www.w3schools.com/sql/default.asp
'''

# endregion


# region BEST PRACTICES

# create database
create database if not exists database_name;
# create table
create table if not exists table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
   .... 
)
# drop  table 
drop table if exists table_name;




# region



# region DATABASE COMMANDS 

# create 
'''
- create database / table
CREATE DATABASE databasename;

CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
   ....
);

- create table from another table
CREATE TABLE TestTable AS
SELECT customername, contactname
FROM customers;
'''
# show
'''
- used to show the databases
SHOW DATABASES;
'''
# use
'''
- used to select the database
USE databasename;
'''
# drop
'''
- used to drop database / table
DROP DATABASE databasename;

DROP TABLE table_name;

'''
drop vs delete vs truncate
# backup database 
'''
- used to backup the database
BACKUP DATABASE databasename
TO DISK = 'filepath';

- used to backup the database with differential/parts
BACKUP DATABASE databasename
TO DISK = 'filepath'
WITH DIFFERENTIAL;
'''
# alter 
'''
- used to alter/modify the database

- add column
ALTER TABLE table_name
ADD column_name datatype;

- drop column
ALTER TABLE table_name
DROP COLUMN column_name;

- rename column
ALTER TABLE table_name
RENAME COLUMN column_name TO new_column_name;

- modify column/datatype
ALTER TABLE table_name
MODIFY COLUMN column_name datatype;
'''
# create view 
'''
- used to create a view
CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;
'''
# create or replace view
'''
- used to update a view
CREATE OR REPLACE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;
'''
# drop view
'''
- used to drop a view
DROP VIEW view_name;
'''
view vs table

# sql injections



# endregion 

# region TABLE COMMANDS 

# select
'''
- if you want to return all columns
SELECT * FROM Customers;

- if you want to return specific columns
SELECT column1, column2, ...
FROM table_name;
'''
# select distinct
'''
- used to return only distinct (different) values.
SELECT DISTINCT column1, column2, ...
FROM table_name;
'''
# where
'''
- used to filter records
SELECT column1, column2, ...
FROM table_name
WHERE condition;

- it orders by Country, but if some rows have the same Country, it orders them by CustomerName
SELECT * FROM Customers
ORDER BY Country, CustomerName;

- selects all customers from the "Customers" table, sorted ascending by the "Country" and descending by the "CustomerName" column
SELECT * FROM Customers
ORDER BY Country ASC, CustomerName DESC;

- WHERE clause is not only used in SELECT statements, it is also used in UPDATE, DELETE, etc.!
- for string values the ORDER BY keyword will order alphabetically
'''

Operator	Description	Example
=	Equal	
>	Greater than	
<	Less than	
>=	Greater than or equal	
<=	Less than or equal	
<>	Not equal. Note: In some versions of SQL this operator may be written as !=	
BETWEEN	Between a certain range	
LIKE	Search for a pattern	
IN	To specify multiple possible values for a column	



# order by 
'''
- used to sort the result-set in ascending or descending order
SELECT column1, column2, ...
FROM table_name
ORDER BY column1, column2, ... ASC|DESC;

- it orders by Country, but if some rows have the same Country, it orders them by CustomerName
SELECT * FROM Customers
ORDER BY Country, CustomerName;
'''
# and 
'''
- used to filter records based on more than one condition
SELECT column1, column2, ...
FROM table_name
WHERE condition1 AND condition2 AND condition3 ...;
'''
# or
'''
- used to filter records based on more than one condition
SELECT column1, column2, ...
FROM table_name
WHERE condition1 OR condition2 OR condition3 ...;
'''
# not 
'''
-  used in combination with other operators to give the opposite result, also called the negative result
SELECT column1, column2, ...
FROM table_name
WHERE NOT condition;

- can be used with like, between, in, greater than, less than, etc.
-  not less than === !< and others also can be written as same
'''
# insert into 
'''
- used to insert new records in a table
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);

insert into table_name(column_1, column_2) values(value_1, value_2),(value_1, value_2);

- if you are adding values for all the columns of the table BUT order must be followed
INSERT INTO table_name
VALUES (value1, value2, value3, ...);
'''
# null value 
'''
- field with a NULL value is one that has been left blank during record creation
- NULL value is different from a zero value or a field that contains spaces
SELECT column_names
FROM table_name
WHERE column_name IS NULL;

SELECT column_names
FROM table_name
WHERE column_name IS NOT NULL;

- It is not possible to test for NULL values with comparison operators, such as =, <, or <>.
'''
# update
'''
- used to modify the existing records in a table
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;

- if you omit the WHERE clause, all records in the table will be updated!
'''
# delete
'''
- used to delete existing records in a table
DELETE FROM table_name WHERE condition;

- delete all rows
DELETE FROM table_name;

- delete a table
drop table table_name;

'''
delete vs drop
# select limit
'''
- used to specify the number of records to return.
SELECT column_name(s)
FROM table_name
WHERE condition
LIMIT number;

- NOT all database systems support the SELECT TOP clause. MySQL supports the LIMIT clause to select a limited number of records, while Oracle uses FETCH FIRST n ROWS ONLY and ROWNUM.
'''
# like
'''
- used in a WHERE clause to search for a specified pattern in a column.
SELECT column1, column2, ...
FROM table_name
WHERE columnN LIKE pattern;

- the percent sign (%) represents zero, one, or multiple characters
- the underscore sign (_) represents one, single character
'''
# in operator 
'''
- allows you to specify multiple values in a WHERE clause
SELECT column_name(s)
FROM table_name
WHERE column_name IN (value1, value2, ...);

- return all records that are NOT any of the values in the list
SELECT * FROM Customers
WHERE Country NOT IN ('Germany', 'France', 'UK');

- Return all customers that have NOT placed any orders in the Orders table:
SELECT * FROM Customers
WHERE CustomerID NOT IN (SELECT CustomerID FROM Orders);
'''
# between 
'''
- selects values within a given range. The values can be numbers, text, or dates.
SELECT column_name(s)
FROM table_name
WHERE column_name BETWEEN value1 AND value2;

- to display the products outside the range
SELECT * FROM Products
WHERE Price NOT BETWEEN 10 AND 20;

- selects all products with a ProductName alphabetically between Carnarvon Tigers and Mozzarella di Giovanni:
SELECT * FROM Products
WHERE ProductName BETWEEN 'Carnarvon Tigers' AND 'Mozzarella di Giovanni'
ORDER BY ProductName;

- selects all orders with an OrderDate between '01-July-1996' and '31-July-1996'
SELECT * FROM Orders
WHERE OrderDate BETWEEN #07/01/1996# AND #07/31/1996#;

SELECT * FROM Orders
WHERE OrderDate BETWEEN '1996-07-01' AND '1996-07-31';
'''
# aliases 
'''
- used to give a table, or a column in a table, a temporary name.
SELECT column_name AS alias_name
FROM table_name;

SELECT column_name(s)
FROM table_name AS alias_name;

SELECT ProductName AS [My Great Products]
FROM Products;

SELECT ProductName AS "My Great Products"
FROM Products;

SELECT CustomerName, CONCAT(Address,', ',PostalCode,', ',City,', ',Country) AS Address
FROM Customers;
*format may differ in other RDBMS 
'''
# joins
# join / inner join 
'''
- selects records that have matching values in both tables
SELECT column_name(s)
FROM table1
INNER JOIN table2
ON table1.column_name = table2.column_name;
'''
# left join / left outer join
'''
- returns all records from the left table (table1), and the matching records from the right table (table2).
SELECT column_name(s)
FROM table1
LEFT JOIN table2
ON table1.column_name = table2.column_name;

- the result is 0 records from the right side, if there is no match.
'''
# right join / right outer join
'''
- returns all records from the right table (table2), and the matching records from the left table (table1).
SELECT column_name(s)
FROM table1
RIGHT JOIN table2
ON table1.column_name = table2.column_name;

- the result is 0 records from the left side, if there is no match.
'''
# full outer join / full join
'''
- returns all records when there is a match in left (table1) or right (table2) table records
SELECT column_name(s)
FROM table1
FULL OUTER JOIN table2
ON table1.column_name = table2.column_name
WHERE condition;
'''
# self join 
'''
- A self join is a regular join, but the table is joined with itself.
SELECT column_name(s)
FROM table1 T1, table1 T2
WHERE condition;
'''
# union 
'''
- used to combine the result-set of two or more SELECT statements.
SELECT column_name(s) FROM table1
UNION
SELECT column_name(s) FROM table2;

- Every SELECT statement within UNION must have the same number of columns
'''
# union all 
'''
- UNION operator selects only distinct values by default. To allow duplicate values, use UNION ALL
SELECT column_name(s) FROM table1
UNION ALL
SELECT column_name(s) FROM table2;
'''
UNION ALL vs full  outer join
# group by 
'''
- groups the rows that have the same values into summary rows, like "find the number of customers in each country".
SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
ORDER BY column_name(s);

- often used with aggregate functions (COUNT(), MAX(), MIN(), SUM(), AVG()) to group the result-set by one or more columns.
'''
group by vs join
# having
'''
-  used to filter groups.
SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
HAVING condition
ORDER BY column_name(s);

- HAVING clause was added to SQL because the WHERE keyword could not be used with aggregate functions.
- often used with the GROUP BY clause to filter groups based on a specified condition.
'''
# exists 
'''
- tests for the existence of any record in a subquery.
SELECT column_name(s)
FROM table_name
WHERE EXISTS
(SELECT column_name FROM table_name WHERE condition);
'''
# any
'''
- returns true if any of the subquery values meet the condition.
SELECT column_name(s)
FROM table_name
WHERE column_name operator ANY
  (SELECT column_name
  FROM table_name
  WHERE condition);

- operator must be a logical operator (>, <, =, !=, <>, >=, <= etc.)
'''
# all
'''
- return true if all of the subquery values meet the condition.
SELECT ALL column_name(s)
FROM table_name
WHERE condition;

SELECT ALL column_name(s)
FROM table_name
WHERE column_name operator ALL
  (SELECT column_name
  FROM table_name
  WHERE condition);

- is used with SELECT, WHERE and HAVING statements.
- operator must be a logical operator (>, <, =, !=, <>, >=, <= etc.)
'''
* vs all
# select into
'''
- copies data from one table into a new table.
SELECT *
INTO newtable [IN externaldb]
FROM oldtable
WHERE condition;

SELECT column1, column2, column3, ...
INTO newtable [IN externaldb]
FROM oldtable
WHERE condition;

- new table will be created with the column-names and types as defined in the old table.
- create new table with 0 entries based on the old table
SELECT * 
INTO newtable [IN externaldb]
WHERE 1 = 0;
'''
# insert into select
'''
-  copies data from one table and inserts it into an existing table.
INSERT INTO table2
SELECT * FROM table1
WHERE condition;

INSERT INTO table2 (column1, column2, column3, ...)
SELECT column1, column2, column3, ...
FROM table1
WHERE condition;

- requires that the data types in source and target tables match.
'''
# case
'''
-  used to return different values based on different conditions.
CASE
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
    WHEN conditionN THEN resultN
    ELSE result
END;
'''
# null functions
IFNULL(), ISNULL(), COALESCE(), and NVL() 

# stored procedures
for the scripting of SQL statements
CREATE PROCEDURE procedure_name
AS
sql_statement
GO;

for executing the script
EXEC procedure_name;

# comments
-- SELECT * FROM Customers;

/*Select all the columns
of all the records
in the Customers table:*/

# operators
https://www.w3schools.com/sql/sql_operators.asp



# endregion


# region ADDITIONAL TOPICS 

# aggregate functions
'''
- MIN(), MAX(), COUNT(), SUM(), AVG()
- Aggregate functions ignore null values (except for COUNT()).

- min and max
SELECT MIN(column_name)
FROM table_name
WHERE condition;

- max
SELECT MAX(column_name)
FROM table_name
WHERE condition;
'''




 returned column will not have a descriptive name
SELECT MIN(Price) AS SmallestPrice
FROM Products;


return the smallest price for each category in the Products table
SELECT MIN(Price) AS SmallestPrice, CategoryID
FROM Products
GROUP BY CategoryID;
# count 
SELECT COUNT(column_name)
FROM table_name
WHERE condition;


SELECT COUNT(DISTINCT Price)
FROM Products;
*Give the counted column a name by using the AS keyword
SELECT COUNT(*) AS [Number of records]
FROM Products;

 return the number of records for each category in the Products table
SELECT COUNT(*) AS [Number of records], CategoryID
FROM Products
GROUP BY CategoryID;
# sum 
SELECT SUM(column_name)
FROM table_name
WHERE condition;

summarized column a name by using the AS keyword.
SELECT SUM(Quantity) AS total
FROM OrderDetails;

return the Quantity for each OrderID in the OrderDetails table
  SELECT OrderID, SUM(Quantity) AS [Total Quantity]
FROM OrderDetails
GROUP BY OrderID;

If we assume that each product in the OrderDetails column costs 10 dollars, we can find the total earnings in dollars by multiply each quantity with 10
SELECT SUM(Quantity * 10)
FROM OrderDetails;

We can also join the OrderDetails table to the Products table to find the actual amount, instead of assuming it is 10 dollars:
SELECT SUM(Price * Quantity)
FROM OrderDetails
LEFT JOIN Products ON OrderDetails.ProductID = Products.ProductID;
# avg
*NULL values are ignored.
SELECT AVG(column_name)
FROM table_name
WHERE condition;

To list all records with a higher price than average, we can use the AVG() function in a sub query
SELECT * FROM Products
WHERE price > (SELECT AVG(price) FROM Products);

return the average price for each category in the Products table:
SELECT AVG(Price) AS AveragePrice, CategoryID
FROM Products
GROUP BY CategoryID;


















# endregion





# region DOUBTS

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
fields/attributes/columns, record/rows/tuples, constraints, primary key, foreign key, base/referenced table/parent table, referencing/child table, 
'''
# DATA TYPES
'''https://www.w3schools.com/sql/sql_datatypes.asp'''
# KEYS in SQL
# CONSTRAINTS
unique, not null, check, default, primary key, foreign key, create index, auto increment
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
# DELETE vs DROP vs TRUNCATE
'''https://www.geeksforgeeks.org/difference-between-delete-drop-and-truncate/'''
# Constraints
'''https://www.geeksforgeeks.org/sql-constraints/'''
# how to use "use" safely like if exists if there is a non-existant database ?
# SELECT column_1, column_2 FROM table_1, table_2; what happens, is it correct ?
# data types - decimal, unsigned constraint, 
# Binary data type vs boolean data type 
# char vs varchar
# primary key vs unique key 
# alter vs update 



# endregion








































































