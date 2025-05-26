
'''
https://www.youtube.com/watch?v=LMbGZOU-dtA

https://www.youtube.com/watch?v=Mf2RdpEiXjU

1. procedural vs functional vs object oriented programming
2. OOPS 
    - Class 
        - instance variable/method
        - class variable/method
        - static variable/method
        - self
        - constructor / __init__()
    - Object
    - Inheritance
        - Single
        - Multiple
        - Multilevel
        - Hierarchical
        - Hybrid
    - Encapsulation
        - Access Modifiew
            - Public
            - Protected
            - Private
    - Polymorphism
        - static polymorphism
        - dynamic polymorphism
    - Abstraction
        - Data Abstraction
        - Data Hiding
        - Variable/Method Overloading
        - Variable/Method/Constructor/Operator Overriding


   6. Abstraction
   7. Static and Dynamic Polymorphism
   8. Data Abstraction
   9. Data Hiding
   10. Data Encapsulation
   11. Data Binding
'''



- OOPS - define your own data type, Generality to specificity

- Class - Blueprint, self-defined data type
data/attributes/property and behaviour/method

- Object - everything in python is object 
python gives object literal for builtin data types
- __init__() / Constructor - whenever we create/construct  an object of a class there is an inbuilt method (__init__) which is known as constructor. 
Special method called itself. 
It is like a receptioist which checks and add/gives all information required 
- self - 
it is the reference to the object created of our class 
it is passed whenever we are calling any method 
only an object can access or helpful in connecting attributes and methods inside our class 
- default arguments
- magic/dunder methods
these are special methods in python which are defined inside class 
they begin and end with double underscore __
they have a special where in they get called themselves automatically
createion - __init__()
print - __str__()
+ - __add__()

- __str__() - used to return a string representation of the object
- __add__(self, other) - used to add two objects
- __sub__(self, other) - used to subtract two objects
- __mul__(self, other) - used to multiply two objects
- __truediv__(self, other) - used to divide two objects
- __eq__(self, other) - used to check if two objects are equal
- __neq__(self, other) - used to check if two objects are not equal

- instance variable - 
- class variable - 

- access modifiers - we can choose to make our attributes/variables private, public or protected
Normally, we make our attributes private and then we use getter and setter methods to access them
once we make our data members private using __variable_name, then everywhere we have to make sure to access them using __variable_name
we can also make methods private using __method_name



encapsulation - the binding of data members and methods into a single unit
class variable/methods or static variable/methods - they are defined outside methods at class level, own by class majorly but accessable by objects, 

inheritence - the process of inheriting the properties and methods of one class into another class, code reusability, 
we inherit non-private attributes, non private methods, constructor(another magicc method using super().__init__())  
we cannot in herit private attributes, private methods from parent 
parent cannot inherit from child, only child can inherit from parent

protected class - we can access protected class from outside the class but not from outside the package

super() - it is a special function that allows us to access the methods of the parent class from the child class, can only access parent class methods not attributes

types of inheritence - single, multiple, multilevel, hierarchical, hybrid







