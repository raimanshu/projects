- Download python – python.org
- Download vs code
- 

# CH 1 – modules, comments and pip
'''
- extension - .py
- vs extension used - python by microsoft
- semi colon (;) - is not used in python code instead indentation is used
- run python file - python file_name.py
- built-in function - print()
- modules - import os, os is a built-in modules
- pip - package manger for python, pip install module_name eg pip install flask
- types of modules - built-in ( os, etc ) & external ( tenserflow, flask, etc)
- use python as calculator - REPL ( Read Evaluate Print Loop ), IDLE, REPL also known as immidiate mode 
- comments - single line & multi-line 
- single line comment - # comments
- multi-line comment - ''' comments '''
'''
# CH 2 - Variables and Data Types
'''
- variables - container to store data
- string literal vs number literal
- keywords - reserved words used in python like def, etc
- identifiers - class, function, variable name
- Data types - types of data
- types of data types - integer, floating point, strings, booleans, none
- strings - "Himanshu", 'Himanshu', Himanshu
- booleans - True, False
- type of variable - type(variable_name)
- rules to decide a variable name - can contain albhabet, letters and underscores, can only start with alphabet or underscore, cannot start with a digit, no white space in between variable_name
- operators in python - artematic, assignment, logical, comparission
- type() function - to find the type of variable 
- typecasting -  way to convert one type to another like int(), str(), float(), etc
- input() function - allows to take input from user as string
'''
# CH 3: strings
'''
- strings - a data type, squence of strings
- strings - "Himanshu", 'Himanshu', Himanshu
- slicing a string - variable_name[starting_point : ending_point : skipping_index]
- string function - str.len(), str.endswith("item"), str.count("item"), str.capitalize(), str.find("item"), str.replace("old_item", "new_item")
'''
# CH 4: List and Tuples
'''
- list - to store set of values of any data type
- slicing is possible like string slicing
- list methods - list_name.sort(), list_name.reverse(), list_name.append(item), list_name.sort(), list_name.insert(item), list_name.pop(item_index), list_name.remove(item)
- tuples - inmutable data type, cannot be updated once declared
- single element tuple is declared as tuple_variable=(item,) not like tuple_variable=(item) it will be treated like integer  
- tuple methods - tuple_variable.count(item), tuple_variable.index(item)
'''
# CH 5 : Dictionary and Sets
'''
- Dictionary - collection of key-value pair, unordered, mutable, indexed, cannot contain duplicate keys
- Difference between print(myDict.get("coder")) & print(myDict["coder"]) is former one will not throw an error if not found but the later one can
- sets - collection of non-repetative elements, unordered, unindexed, items cannot be changed, cannot contain duplicate items
- a = {}, This syntax will create an empty dictionary not an empty set
'''
# CH 6 : Conditional Expressions
'''
- if, else and elif / else if ladder -
- Relatinal operators - ==, >=, <=, evaluate conditions inside if statements
- logical operators - and, or, not, operate on conditional statements
- elif clause/block - 
- is and in operator - is is same as == operator, in is same as for in loop in javascript
- else block is optional. It is not mandatory to mention.
'''
# CH 7 : Loops
'''
- loops - to repeat instructions
- while loop - repeat instructions until a condition is False
- for loop - iterate through a sequence of list, tuple or strings (iterables)
- range() function - range(start_point, end_point, step_value)
- for with else - else block executes after for loop successful executes, but if complete loop donot executes and used break statement then else block will not executes
- break statement - to come out from a loop
- continue statement - 
- pass statement - to instructs the loop/condition to do nothing, null statement
- def - def keyword is used to create a statement
'''
# CH 8 : Functions and Recurssion
'''
- function - group of statements performing a specific task, can be called any number of times
- function call - place where we need to use the function, funct()
- function definition - set of instruction to provide specific funcitionality, 
def funct()
    statement
- types of function - built-in functions & user defined functions
- built-in functions - already present in python, Eg - len(), print(), range(), etc
- user defined function - defined by user, Eg - funct(), etc
- function with arguments - functions can accept some values to work with, these values are called arguments in function definition where as called parameters in function call
- default parameter value - we can have a value as default argument in a function 
- Recurssion - function which call itself
- In python print("string_literal", end="") function, end parametr denotes new line ie \n 
- strip() function - to trip spacees from left and right of string ie trim() in javascript
'''
# CH 9 : File I/O
'''
- file - data stored in a storage device
- During reading a file data flow from file to progran but during write process code flow vice versa
- RAM - volatile
- HDD - non-volatile
- types of files - text file & binary file
- text file - file contain characters or readable in notepad/word, etc. Eg - .txt, .c etc. In this type of file, Each line of text is terminated with a special character called EOL (End of Line), which is the new line character (‘\n’) in Python by default.
- binary file - need specific programs to read like .jpg, .dot, etc. In this type of file, there is no terminator for a line and the data is stored after converting it into machine-understandable binary language.
- opening a file - open(file_name, mode), by default the mode is read
- modes - read (r), write (w), read and write (r+), write and read (w+), append (a), append and read (a+), read in binary mode (rb), read in text mode (rt)
- read() function to read the opened file. This function takes an int parameter using which it read only upto that character from the starting point like read(5)
- readline() - read only one line
- with statement -  It is the best way to work with file. We donot need to close() function to close the file
'''
# CH 10 : Object Oriented programming
'''
OOP - solving a problem using objects is called OOP
DRY principle - Donot Repeat Yourself principle
class - blueprint of creating objects, class is written in pascal case, contains methods and variables
- pascal case - EmployeeName, etc
- camel case - employeeName, etc
- object - instantiation of a class, when class is defined, a template (info) is defined memory is alocated only after object instantiation
- abstraction - performing a funcitionality without know it's implementation
- encapsulation - 
- Naming convention
Noun - Class - Employee
Adjective - Attributes/Variables/Property - name, age, salary
Verbs - Methods - getSalary(), setSum()
- types of attributes - class attributes and instance attributes
- class attributes - belongs to the class rather than a particular object
- instance attributes - belongs to the instance (object)
- instance attributes takes priority over class attributes during assignment and retrieval
- self - refers to the instance of the class, automatically parsed with a function call fro the object
- If you print self of class it prints memory allocated to that object like
print(self)
<__main__.Employee object at 0x00000202B0CEEDD0>
- Both line are same, if we remove self parameter from class method it throws an error as Employee.getSalary() takes 0 positional arguments but 1 was given because object harry is passed in class Employee implicitly 
harry.getSalary()
Employee.getSalary(harry)
- static method - @staticmethod decorator is used to make a method run without self parameter
- __init__ () or Constructor - is a special method which is first run as soon as the object is created, also known as constructor, takes self argument but can also take more arguments, used to initialize  
- We can rename with other name to self, but it will create confusion to other programmers
'''
# CH 11 : Inheritance
'''
- inheritence =  way of creating a new class from the existing class
- base class / parent class - 
- derived class / child class - 
- types of inheritence - single, multiple & multilevel inheritence
- single inheritence - child inherits only  a single parent class
- multiple inheritence - child class inherits from more than one parent class
- In multiple inheritence, the class which written first it's property will take priority if parent classes have same property or method
- multilevel inheritence -
- super() method - used to access the methods of a base/parent class in the derived class
- class method - method which is bound to the class and not the object of the class, @classmethod decorator is used
- @property decorator - 
- getter and setter methods - 
- dunder methods - 
- operator overloading - operators can be overloaded using dunder methods, __sum__, __mul__, etc
- __str__ method -
- __len__ method -
'''
# CH 12 :  Advanced Python 1
'''
- exception handeling - 
- try - 
- except Exception
- we can raise custom error using raise ValueError("message") inside except block
- In try-except-else pattern, else block only execute when try block successfully execute without exceptions
- In try-except-finally pattern, finally block execute regardless of successful try execution or throw error, mainly used for cleanup or execute those process which we want to execute even program crashes
- In if __name__ == "__main__":, if we print(__name__) it will give from where the program is executing
- global keyword - used to modify the variable outside of the current scope 
- enumerate() function - adds counter to an itterable and returns it
- list/dictionary/set comprehensions - to write the code in shorter syntax
'''
# CH : Advanced Python 2
'''
- Virtual Environment - Environment same as system interpreter but is installed from the other python environments, 
1) install virtual virtualenv using pip install virtualenv
2) virtualenv env_name
3) source env_name/bin/activate (for linux users)
.\env_name\Scripts\...ps1  (for windows poershell users)
4) pip install package_name (IT will be installed in created environment)
- pip freeze - to see all packages installed
- pip freeze > file_name.txt - print all packages in file_name.txt
- lambda/anonymous function - function created using an expression 
- join method - create a string from iterable objects 
- format method - 
- map - map applies a function to all the items in an input list
- filter - creates a list of items for which the function returns True
- reduce - reduce applies a rolling comparision to sequential pair of elements
'''

OBSERVATIONS :
- semi colon (;) - isnot used in python code instead indentation is used
- we can use multi-line comment inside print() function to print multiple lines
- a = '''Himanshu''' is valid
- python automatically decides the type of variable
- Division (/) in python always returns a float value
- Automatic type conversion is not possible in python if b is str like "5" then print(+b)
- print('${b}') and print('''Himanshu''') can be used in python
- str.replace() donot modify original string. It creates/returns a new string with replaced words/characters
- single element tuple is declared as tuple_variable=(item,) not like tuple_variable=(item) it will be treated like integer
- hoisting doesnot work in python
- Dot accessing is not possible in dictionary
- In case of dictionary, Difference between print(myDict.get("coder")) & print(myDict["coder"]) is former one will not throw an error if not found but the later one can
- a = {}, This syntax will create an empty dictionary not an empty set
- list and dictionary cannot be added in a set because it's content can be changed But tuples can be included
- In a set, 18 and 18.0 is treated as single element
- is and in operator - is is same as == operator, in is same as for in loop in javascript
- else block is optional. It is not mandatory to mention.
- for with else - else block executes after for loop successful executes, but if complete loop donot executes and used break statement then else block will not executes
- pass statement - to instructs the loop/condition to do nothing, null statement
- def - def keyword is used to create a statement
- f"{variable_name}string_constant" ie f string is used to write string with string literals and variables
- In python print("string_literal", end="") function, end parametr denotes new line ie \n 
- If file is opened in write mode and mentioned file is not available then the file will be created and if file is already present then the contents of that file will be updated
- If appending file is executed 6 times then 6 times the mentioned content will append
- with statement -  It is the best way to work with file. We donot need to close() function to close the file
- write() function return the number of character inputed to update
- If you print self of class it prints memory allocated to that object like
print(self)
<__main__.Employee object at 0x00000202B0CEEDD0>
- Both line are same, if we remove self parameter from class method it throws an error as Employee.getSalary() takes 0 positional arguments but 1 was given because object harry is passed in class Employee implicitly 
harry.getSalary()
Employee.getSalary(harry)
- If an attribute is not mentioned in the class then use this method to avoid error 
class Employee1:
    company ="Google"
    def getSalary(self):
        print(f"Salary is {self.salary}")


harry1 = Employee1()
harry1.salary = 100000
harry1.getSalary()
- We can rename with other name to self, but it will create confusion to other programmers
- In if __name__ == "__main__":, if we print(__name__) it will give from where the program is executing
- i++ is not valid in python but i += 1 is valid


