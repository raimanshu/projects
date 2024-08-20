# allows objects with incompatible interfaces to collaborate.

# https://www.youtube.com/watch?v=nUPqtnwV9nE&list=PLwzO627zBnSD2sbolkpJhi7sp4dphcrDF&index=9


# https://refactoring.guru/design-patterns/adapter

# E.g Covert xml data into json
# Create interface JSONData which has a method readJSONData() and this class is implemented by a class called JSONSoftware 
# Simillarly, Create interface XMLData which has a method readXMLData() and this class is implemented by a class called XMLSoftware
#  create a class XMLToJSONDataAdapter which implements JSONData class. Create a class variable of xmlData type and assign it into it's constructor.There is another function readJSONData() which will be overridden and put the logic inside it for conversion.
# In the main method create an object xmlDataSoft of XMLSoftware, pass xmlSoftware into XMLToJSONDataAdapter(xmlDataSoft) and assign it to xmlAdapter variable then, we can read data by xmlAdapter.readJSONData()