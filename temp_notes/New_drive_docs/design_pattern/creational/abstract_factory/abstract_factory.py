# https://refactoring.guru/design-patterns/abstract-factory

# https://www.youtube.com/watch?v=fsiu8kMQ8Wk

# It  lets you produce families of related objects without specifying their concrete classes.

# Abstract class in python ??
# https://www.youtube.com/watch?v=Iho_Kgj5kfI

# E.g - Abstract class phone() have property brand,model no, size, body and methods buildPhone(), assemblePhone() and packPhone(). This abstract class is inherit by various classes like iphone12, iphone13, oneplus8 and oneplus9 and their own configs using phone().
# Create an abstract class phoneStore having one method createPhone("modelNumber") which take one param modelNumber. It has a methood orderphone() which take modelNumber and using this it will create an instance either onePlusFactory("modelNumber") class or iphoneFactory("modelNumber") class to create it's instance. Each factory can have conditions to create instance of it's sub category like iphone12 and iphone12 in iphone factory.
# After that,using this instance assigned, it will call instance.buildPhone() of phoneClass() and it will perform functionality to it's respective concrete class 

