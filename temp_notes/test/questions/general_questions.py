# concurency vs parallelism


# process vs threads 


# multi-processing vs multi-threading vs multi-tasking vs multi-programming vs hyper-threading 
"""
multi-processing - system with multiple processors/cpu/core 
multi-threading - multiple threads running at the same time
multi-tasking - multiple processes running at the same time by single cpu/core
multi-programming - multiple programs running at the same time
multi-processing is faster than multi-threading
https://www.youtube.com/watch?v=_BhJ2rSo5Wo
"""

# AI vs ML vs DL vs DS vs DM vs DMML vs DMDL vs DMMLDL vs DMDLDL
"""
AI - Artificial Intelligence
ML - Machine Learning
DL - Deep Learning
DS - Data Science
DM - Data Mining
DMML - Data Mining Machine Learning
DMDL - Data Mining
DMMLDL - Data Mining Machine Learning Deep Learning
DMDLDL - Data Mining Deep Learning Deep Learning
https://www.youtube.com/watch?v=Z27llwBA0Uw
"""

# cohesion vs coupling

# tight coupling vs loose coupling

# sql vs nosql vs mysql

# web server vs application server

# website vs web application vs web service vs web api

# SOLID principles
"""
S - Single Responsibility Principle - A class should have one and only one reason to change, meaning that a class should have only one job.

O - Open-Closed Principle
L - Liskov Substitution Principle
I - Interface Segregation Principle
D - Dependency Inversion Principle






"""

# shallow copy vs deep copy
"""
Shallow copy:
The new object is a copy of the original, but nested objects inside it are shared between the original and the copy.

Deep copy:
The new object and the original share no nested objects; changes to one do not affect the other

# python
import copy
original = [[1, 2], [3, 4]]

shallow = copy.copy(original)
deep = copy.deepcopy(original)

shallow[0][0] = 'A'
print(original)  # [['A', 2], [3, 4]] — changed because inner list is shared
deep[1][1] = 'B'
print(original)  # [['A', 2], [3, 4]] — no change because deep copy is independent

# javascript
const original = {
  name: 'Alice',
  address: { city: 'Wonderland' }
};

// Shallow copy using spread operator
const shallowCopy = { ...original };

// Deep copy using JSON methods
const deepCopy = JSON.parse(JSON.stringify(original));

// Modify nested object in shallow copy
shallowCopy.address.city = 'Shallow City';

// Modify nested object in deep copy
deepCopy.address.city = 'Deep City';

console.log('Original:', original.address.city);  // Shallow City (changed)
console.log('Shallow Copy:', shallowCopy.address.city);  // Shallow City
console.log('Deep Copy:', deepCopy.address.city);  // Deep City


"""