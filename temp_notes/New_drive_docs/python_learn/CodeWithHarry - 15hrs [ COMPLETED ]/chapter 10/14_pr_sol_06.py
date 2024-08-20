
from unicodedata import name


class Sample:
    a = "harry"
    def __init__(self, name):
        self.name = name

obj = Sample("Harry")
print(obj.name)

# We can rename with other name to self, but it will create confusion to other programmers
class Sample1:
    def __init__(harry, name):
        print(harry)
        harry.name = name

obj = Sample1("Harry")
print(obj.name)