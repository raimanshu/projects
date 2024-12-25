
1. Object Oriented Programming Python -01 | Object Oriented Programming in Python | OOP Syllabus
Basics of OOP 
Types of variables and methods
Inheritance 
Polymorphism
Encapsulation 
Abstraction 
Interface

2. What is Object Oriented Programming | Object Oriented Programming Python -02 | OOP Tutorial Python
- Python supports procedural oriented paradigm, functional oriented paradigm and object oriented paradigm
- procedural oriented paradigm - all code is written as line by line in one file 
- functional oriented paradigm - all code is written in several functions 
- object oriented - an approch of writting programs by createing classes and objects. More fous on data rather than creating logic. It is used to solve real-world problems effectively.
- An object in OOP represents real-world objects. Every object has two properties - attributes (data) and behaviour (actions)
 
3. Object Oriented Programming Python -03 | Class and Object in Python | Creating Class and Object
- class is a template/blueprint/prototype for creating objects.
- class is a collection of attributes and methods.
- class is a collection of objects.
- class is an user-defined datatype
- every object belongs to some class 
class ClassName:
    #attributes
    #methods
obj1 = ClassName([args])
obj2 = ClassName([args])
- to fine class name of an object 
print(type(object_name))

4. Object Oriented Programming Python -04 | Constructor in Python | Types of Constructor | Init Method
- __init__ - to initialize an object of a class 
- __dict__ - to see attributes and methods of a class object 
- __init__ is the constructor of a class.
- types of constructor - default, parameterized, non-parameterized 
- Non-Parameterized constructor 
class Employee(self):
    def __init__(self):
        self.salary = 20000
        self.age = 22
obj1 = Employee()
- Parameterized constructor 
class Employee(self):
    def __init__(self, salary, age):
        self.salary = salary
        self.age = age
obj1 = Employee(20000, 22)
- Default constructor 
class Employee(self):
    pass
obj1 = Employee()
- without constructor an object cannot be created. In 3rd case constructor cannot be seen but internally default constructor will execute

5. Self Variable in Python | Object Oriented Programming Python -05 | How OOP Works
- self is a variable that contains memory reference of current object
- Steps while creating object - memory allocation for object, memory reference returned to the object, memory reference automatically passed inside constructor, constructor creates/initializes variables at that memory reference 

6. Object Oriented Programming Python -06 | Accessing Class Members Outside the Class
- class members are the class attributes and methods. We can access these variables using object outside the class 
object_name.attribute_name
object_name.method_name()

7. Object Oriented Programming Python -07 | Built in Class Functions | Accessing attributes
- getattr(object_name, attribute_name) 
- setattr(object_name, attribute_name, new_value) 
- delattr(object_name, attribute_name)  
- hasattr(object_name, attribute_name)

8. Object Oriented Programming Python -08| Built in Class Attributes
- __dict__ - dictionary containing class's namespace 
- __doc__ - class documentation string 
- __name__ - class name
- __module__ - module name  in which class is defined 
- __bases__ - list of base classes

9. Object Oriented Programming Python -09 | isinstance() Function in Python
- instance() method - used to check wheather given object is an instance of provided class or not. It returns boolean True/False 
class Employee:
    pass
e1 = Employee()
print(isInstance(e1, Employee))  // True

10. Object Oriented Programming Python | What is Instance Variables Python | Instance Method Python
- instance variable - variables made for particular instance, separate copy is created for every object, values of variables differs from objecct to object, modifications in one object won't affect other object 
- creating instance variables - using constructor, using instance methods, using outside class
- using constructor
class Employee:
    def __init__(self):
        self.salary = 20000
        self.age = 22
obj1 = Employee()
- using instance methods 
class Employee:
    def __init__(self, salary, age):
        self.salary = self.salary
        self.age = self.age
obj1 = Employee()
- using outside class
class Employee:
    def __init__(self):
        self.salary = 20000
        self.age = 22
obj1 = Employee()
obj1.name = "test"

11. Object Oriented Programming Python -11 | Class Variables in Python | Class Method in Python
- Several copies of instance variables are created for each object created but class is single created and objects share that variable between them but they can't modify that.
- class variable - variables made for entire class (all objects), only one copy is created and distributed to all objects, modification in class variable impact on all objects.
class Student:
    college = "test"
    def __init__(self):
        self.name = "name"
        self.marks = 22
obj1 = Student()        // separate name & marks variable are created but share same college variable
obj2 = Student()        // separate name & marks variable are created but share same college variable
print(Student.college)  // test
print(obj1.college)     // test 
obj1.college = "Himanshu"      
print(obj1)                     // {name: "name", marks: 22, college: "test"}
print(obj2)                     // {name: "name", marks: 22}
print(Student.college)          // "test"
- class method - method which works on class variables, first argument is class reference (cls), made using decorator @classmethod,
class Student:
    college = "test"
    def __init__(self):
        self.name = "name"
        self.marks = 22
    @classmethod
    def getCollegeName(cls):
        print(cls.college)
print(Student.getCollegeName())          // "test"


12. Object Oriented Programming Python -12 | Setter and Getter Methods in Python
- Instance methods - setter & getter 
- setter - set values of instance variables 
- getter - get values of instance variables 

13. Object Oriented Programming in Python -13 | Staticmethod in Python
- static methods - methods which performs operations on external data, can alsoperform operations on class data, no need to pass object or class reference, created using decorator "@staticmethod"



OBSERVATIONS
-------------
- class methods works with class variables but instance methods works with instance variables
- self and cls keywords are not mandatory to give names, we can change their names 
- access way of class methods ?? can it acces via object
class Employee:
    def setName(self, name):
        self.name = name 
    def getName(self):
        print(self.name)
obj1 = Employee()
obj1.setName("test")
print(obj1.getName())

