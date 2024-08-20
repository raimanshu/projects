# https://www.geeksforgeeks.org/singleton-method-python-design-patterns/

# https://www.youtube.com/watch?v=YxGyIm46C94

# https://github.com/hnmpatel/design-patterns-python

# https://www.youtube.com/watch?v=h-TLrwLCFQ8&list=PLwzO627zBnSD2sbolkpJhi7sp4dphcrDF&index=5

# It lets you ensure that a class has only one instance, while providing a global access point to this instance., Monostate/Borg Singleton Design pattern vs Double Checked Locking Singleton Design pattern

# It ensures only one instance of a class is created
# Use when control access to shared database or file 
# Use when provide access to global variable

# Eg -  Database connectivity 


# Object vs Instance ??
# https://www.youtube.com/watch?v=1hPn4jkQoAM
# https://www.youtube.com/watch?v=kyNfaY_id3c


# Solution - 1
class SingleTon(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

o1 = SingleTon()
print("Object - 1 ==>", o1)
o1.data = 10

o2 = SingleTon()
print("Object - 2 ==>", o2)
print("Object - 2 data ==>", o2.data)
o2.data = 5

print("Object - 1 data ==>", o1.data)


# Solution - 2
# class Borg(object):
#     _shared = {}

#     def __init__(self):
#         self.__dict__ = self._shared


# class SingleTon(Borg):
#     def __init__(self, arg):
#         Borg.__init__(self)
#         self.val = arg

#     # def __str__(self):
#     #     return "<{} - Object>".format(self.val)


# o1 = SingleTon("Hardik")
# print("Object - 1 ==>", o1)
# print("Object - 1 val ==>", o1.val)

# o2 = SingleTon("Aarav")
# print("Object - 2 ==>", o2)
# print("Object - 2 val ==>", o2.val)
# print("Object - 1 val ==>", o1.val)

# print(o1.__dict__)
# print(o2.__dict__)



# Solution - 3
# class SingletonDecorator(object):
#     def __init__(self, klass):
#         self.klass = klass
#         self.instance = None
        
#     def __call__(self, *args, **kwargs):
#         if self.instance == None:
#             self.instance = self.klass(*args,**kwargs)
#         return self.instance


# @SingletonDecorator
# class Logger(object):
#     def __init__(self):
#         self.start = None

#     def write(self, message):
#         if self.start:
#             print(self.start, message)
#         else:
#             print(message)

# logger1 = Logger()
# logger1.start = "# >"
# print("Logger 1", logger1)
# logger1.write("Logger1 object is created.")

# logger2 = Logger()
# logger2.start = "$ >"
# print("Logger 2", logger2)
# logger1.write("Logger2 object is created.")



# Solution - 4
# class SingletonMeta(type):
#     __instances = {}

#     def __call__(cls, *args, **kwargs):
#         if cls not in cls.__instances:
#             cls.__instances[cls] = super().__call__(*args, **kwargs)
#         print(cls.__instances)
#         return cls.__instances[cls]

    
# class DBConnector(metaclass=SingletonMeta):
#     def __init__(self):
#         self.status = "Not Connected"

#     def disconnect(self):
#         self.status = "Disconnected"

#     def connect(self):
#         self.status = "Connected"


# client1 = DBConnector()
# print("Client 1 ", client1)
# print(client1.status)

# client2 = DBConnector()
# print("Client 2 ", client2)
# client2.connect()
# print(client1.status)

# client1.disconnect()
# print(client2.status)