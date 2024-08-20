
class Sample:
    a = "harry"

obj = Sample()
# This will not change the value of class attribute 
obj.a = "Vikky"

print(obj.a)
print(Sample.a)


# This will not change the value of class attribute 
Sample.a = "Vikky"

print(obj.a)
print(Sample.a)