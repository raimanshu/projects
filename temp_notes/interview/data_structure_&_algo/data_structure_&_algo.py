# RESOURCE - takeuforward.org
# ---------------------------


# region ARRAY
# ------------ 
'''
- contiguous memory
- fixed size
- random access
- insertion and deletion is costly
- 2d array - matrix
- 3d array - cube
- 4d array - hypercube
- 5d array - hypercube
- types - single dimensional array, multi dimensional array
- operations - insertion, deletion, traversal, search, sorting, merging, splitting, reversing, rotating, shuffling
- indexing - 0 based indexing, 1 based indexing
- maximum array size can be 10^7 in c++ and 10^6 in python
-




- sorting algorithms - bubble sort, selection sort, insertion sort, merge sort, quick sort, heap sort, counting sort, radix sort, bucket sort, shell sort, tim sort, cocktail sort, comb sort, gnome sort, pigeonhole sort, cycle sort, strand sort, bitonic sort, pancake sort, bogo sort, stooge sort, bead sort, pigeon sort
- searching algorithms - linear search, binary search, jump search, interpolation search, exponential search, fibonacci search, ternary search, polynomial search, jump search, fibonacci search, interpolation search, exponential search

'''

# endregion


LINKED LIST 
- linked list is a data structure that follows the First In First Out (FIFO) principle
- linked list is a linear data structure
- linked list is a collection of elements
- linked list is a non-primitive data structure
- operations - insertion, deletion, traversal, search, sorting, merging, splitting, reversing, rotating, shuffling
- types - single linked list, double linked list, circular linked list, doubly circular linked list
- real world examples - 

GREEDY ALGORITHM 
- greedy algorithm is an algorithm that always makes the choice that looks best at the moment


# region HASHING
# --------------
# theory - https://www.youtube.com/watch?v=TLk7_Ia3rzQ&t=431s
# practical - https://www.youtube.com/watch?v=KEs5UyBJ39g&list=PLgUwDviBIf0oF6QL8m22w1hIDC1vJ_BHz&index=13

# hashing 
'''
- pre-storing and fetching
- hashing is a technique used to uniquely map data (e.g., strings, numbers) to a fixed-size value, In Python, hashing is primarily used in data structures like dictionaries and sets
- types of hashing - division method, folding method, mid square method

- division method -  
Formul for division method,
    hash(key) = key % size
example - hash(123) = 123 % 10 = 3

- folding method - The basic idea behind the folding method is to split the key into parts, apply a simple operation (like addition or XOR) on the parts, and then combine them to form a hash value.

advantage -     
drawback - 

- mid-square method - technique where the key is squared, and the middle portion of the resulting number is taken as the hash value. 
advantage -     
drawback - 
'''

# hash collisions 
'''
- hash collisions - when two different keys have the same hash value
- types of collisions - chaining / separate chaing & open addressing / closed hashing 
- other hashing techniques - Cuckooo hashing, hopscotch hashing, perfect hashing, etc 

- chaining / separate chaining - In chaining, each element of the hash table is a linked list. When a collision occurs (i.e., two keys hash to the same index), the elements are stored in the linked list at that index. This approach allows multiple elements to be stored at the same index, and it's particularly useful when the number of elements is large.

- open addressing / closed hashing - In open addressing, all elements are stored directly in the hash table itself. When a collision occurs (i.e., two keys hash to the same index), the algorithm searches for another available slot in the hash table according to a predefined strategy.The idea behind open addressing is that, instead of using additional data structures (like linked lists), the table itself is used to store all elements.
- types of open addressing / closed hashing - linear probing, quadratic probing & double hashing

- linear probing -  If a collision occurs, the algorithm searches for the next available index linearly
Formula for probing:
    new_index=(original_index + i) % table_size
where i is the number of attempts.
- drawback - primary clustering

- quadratic probing - Instead of probing sequentially, we use a quadratic function to find the next available slot.
Formula for probing:
    new_index=(original_index + i^2 ) % table_size
where i is the number of attempts.
- drwback - secondary clustering

- double hashing - If a collision occurs, another hash function is applied to the key to calculate the step size for the next probe.
Formula:
    new_index=(hash1(key) + i × hash2(key)) % table_size
where hash1 and hash2 are two different hash functions. 
drawback - computationally expensive
'''

# clustering
'''
- clustering - phenomenon where multiple keys in a hash table end up mapping to the same or neighboring indices, leading to a concentration of hash values in a particular region of the table.
- types of clustering - primary clustering, secondary clustering, tertiary clustering

- primary clustering - where consecutive or nearby slots become occupied due to collision resolution strategies like linear probing.
- secondary clustering - cause keys to probe the same sequence of slots based on their hash values.
- tertiary clustering - 
- external clustering -  happen when multiple keys hash to the same index and are stored in a linked list or other data structure at the same index.
'''


# terminologies
'''
- hash function - A function that takes an input (or "key") and returns a fixed-size string of bytes (usually an integer). 
example - hash(123) = 123 % 10 = 3 where 10 is the size of the hash table, hash(123) is the hash function, 123 is the key, 3 is the hash value/hash code
- compression function - A function that takes the output of the hash function and maps it to an index within the hash table.
- hash table - A data structure that uses hash functions to map keys to values for efficient lookup, insertion, and deletion operations.
- load factor -It's a measure of how full the hash table is. A load factor of 0.75 is often considered a good balance between space efficiency and performance.
Formula,
    load factor = total number of elements in the hash table / size of the hash table
example - load factor = 10 / 10 = 1
- hash value - The output of the hash function. It's a fixed-size string of bytes.
- encryption - The process of converting data into a form that cannot be easily understood by unauthorized parties.
- decryption - The process of converting encrypted data back into its original form.
- public/private key encryption - A method of encryption that uses a pair of keys: a public key and a private key. The public key is used to encrypt data, and the private key is used to decrypt it.
- digital signature - A cryptographic technique used to verify the authenticity and integrity of data.
- salting - Adding a random value (salt) to a password before hashing it. This makes it more difficult for attackers to crack passwords.
- key derivation function - A function that takes a password and a salt and produces a key. This is used to generate keys for encryption and decryption.
- key stretching - The process of applying a key derivation function multiple times to a password to make it more secure.
- key stretching algorithm - A specific algorithm used for key stretching.
- bucket array - In a hash table, the data is distributed into an array of "buckets" based on hash values derived from keys. Each bucket can contain multiple elements (in cases of hash collisions)
'''

# implementation_of_hash_table_in_python 
'''
- map / dictionay / unordered map - unordered map is a data structure that does not maintain the insertion order of keys. It is used when we have to maintain the order of keys and the key values are larger than the size of 10^6.
'''
def frequency_array(arr):
    frequency_map = {}
    
    # Iterate through the array and count each element's frequency
    for num in arr:
        if num in frequency_map:
            frequency_map[num] += 1
        else:
            frequency_map[num] = 1
    
    return frequency_map

# Example usage
arr = [4, 5, 6, 4, 6, 4, 7]
result = frequency_array(arr)
print(result)                                                   # ---> {4: 3, 5: 1, 6: 2, 7: 1}

# using ordered map in python
'''
- ordered map - ordered map is a data structure that maintains the insertion order of keys.It is used when we have to maintain the order of keys and the key values are larger than the size of 10^6.
'''
from collections import OrderedDict

# Creating an ordered dictionary
ordered_map = OrderedDict()
ordered_map["apple"] = 1
ordered_map["banana"] = 2
ordered_map["cherry"] = 3

# Inserting more elements
ordered_map["date"] = 4
ordered_map["elderberry"] = 5

# Printing in the order of insertion
for key, value in ordered_map.items():
    print(f"{key}: {value}")

# Output:
# apple: 1
# banana: 2
# cherry: 3
# date: 4
# elderberry: 5

# Additional functionality of OrderedDict:
# Move "banana" to the end
ordered_map.move_to_end("banana")
print("After moving 'banana' to the end:", ordered_map)

# Move "apple" to the beginning
ordered_map.move_to_end("apple", last=False)
print("After moving 'apple' to the beginning:", ordered_map)
# Output:
# After moving 'banana' to the end: OrderedDict([('apple', 1), ('cherry', 3), ('date', 4), ('elderberry', 5), ('banana', 2)])
# After moving 'apple' to the beginning: OrderedDict([('apple', 1), ('cherry', 3), ('date', 4), ('elderberry', 5), ('banana', 2)])

'''
frequency array / hash array - A frequency array is a data structure that stores the frequency of each element in an array. It is used when we have to maintain the order of keys and the key values are less than the size of 10^6.
'''
def frequency_array(arr, max_value):
    # Initialize a list of zeros with length max_value + 1
    freq = [0] * (max_value + 1)
    
    # Iterate through the array and increment the count at the respective index
    for num in arr:
        freq[num] += 1
    return freq

# Example usage
arr = [4, 5, 6, 4, 6, 4, 7]
max_value = 7  # Maximum value in the array
result = frequency_array(arr, max_value)
print(result)                                               # ---> [0, 0, 0, 0, 3, 1, 2, 1]

'''
- using counter - A counter is a data structure that stores the frequency of each element in an array.
'''
from collections import Counter

def frequency_array(arr):
    return dict(Counter(arr))

# Example usage
arr = [4, 5, 6, 4, 6, 4, 7]
result = frequency_array(arr)
print(result)                                           # ---> {4: 3, 5: 1, 6: 2, 7: 1}

# endregion



# region RECUSSION
# ----------------
# 👉👉👉  https://www.youtube.com/watch?v=6IIgSFBPQ0U
# https://www.youtube.com/watch?v=69ZCDFy-OUo&list=PLgUwDviBIf0oF6QL8m22w1hIDC1vJ_BHz&index=10
'''
- when a function calls itself until a specified condition is met
- Recursion is a method where the solution to a problem depends on solutions to smaller instances of the same problem
- types - tail recursion, head recursion, tree recursion, direct recursion, indirect recursion, mutual recursion
'''
'''
- direct recursion - Direct recursion occurs when a function directly calls itself within its body.
'''
def factorial(n):
    if n == 0:
        return 1  # Base case
    else:
        return n * factorial(n - 1)  # Direct recursion
print(factorial(5))  # Output: 120

'''
- indireact recursion - Indirect recursion happens when a function calls another function, and that second function calls the first function, forming a cycle. This means two or more functions are involved in the recursion.
'''
def is_even(n):
    if n == 0:
        return True  # Base case: 0 is even
    else:
        return is_odd(n - 1)  # Call the other function for odd case

def is_odd(n):
    if n == 0:
        return False  # Base case: 0 is not odd
    else:
        return is_even(n - 1)  # Call the other function for even case
print(is_even(4))  # Output: True
print(is_odd(5))   # Output: True

'''
- tail recursion - when the recursive call is the last thing executed by the function
'''
def factorial_tail(n, accumulator=1):
    if n == 0:
        return accumulator  # Base case
    else:
        return factorial_tail(n - 1, n * accumulator)  # Tail recursion
print(factorial_tail(5))  # Output: 120

'''
- head recursion - when the recursive call is the first thing executed by the function
'''
def factorial_head(n):
    if n == 0:
        return 1  # Base case
    else:
        result = factorial_head(n - 1)  # Head recursion
        return n * result  # Multiply after recursion
print(factorial_head(5))  # Output: 120

'''
- tree recursion - when the function calls itself more than once
'''
def fibonacci(n):
    if n <= 1:
        return n  # Base case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Two recursive calls
print(fibonacci(5))  # Output: 5

'''
- mutual recursion - when two functions call each other recursively. This is similar to indirect recursion, but it involves a set of functions calling each other recursively.
'''
def is_even(n):
    if n == 0:
        return True  # Base case: 0 is even
    else:
        return is_odd(n - 1)  # Call the other function for odd case

def is_odd(n):
    if n == 0:
        return False  # Base case: 0 is not odd
    else:
        return is_even(n - 1)  # Call the other function for even case
print(is_even(4))  # Output: True
print(is_odd(5))   # Output: True

'''
- recursion tree - a tree where each node represents a recursive call
- FOR CALL STACK / STACK SPACE, when the function is called first donot put it in the call stack, when it is callduring the function execution then put it inside the stack
- FOR RECURSION TREE, when the function is called first put it in the recursion tree, when it is called during the function execution then again put it inside the recursion tree
- base case - the condition when the recursion stops
- recursive call - the function calls itself
- recursive call stack - the stack of recursive calls
- recursive call stack frame - the frame of the recursive call
- recursive call stack frame size - the size of the recursive call stack frame
- segmentation fault / stack overflow - when the recursive call stack frame size exceeds the memory limit
'''

# endregion

SLIDING WINDOW
- sliding window is a technique used to solve problems related to arrays and strings
- when to use - when we have a problem that involves finding the maximum or minimum of a subarray of size k


TWO POINTERS TECHNIQUE 
- two pointers is a technique used to solve problems related to arrays and strings
- where to use -


STACK 
- stack is a data structure that follows the Last In First Out (LIFO) principle
- stack is a linear data structure
- stack is a collection of elements
- stack is a non-primitive data structure
- operations - push/add, pop, peek/top, isEmpty, isFull, size, clear, print
- stack implementation using array
https://www.geeksforgeeks.org/implement-stack-using-array/
- stack implementation using linked list
https://www.geeksforgeeks.org/implement-a-stack-using-singly-linked-list/
- stack implementation using queue 
https://www.geeksforgeeks.org/implement-stack-using-queue/



QUEUE
- queue is a data structure that follows the First In First Out (FIFO) principle
- queue is a linear data structure
- queue is a collection of elements
- queue is a non-primitive data structure
- operations - enqueue/add, dequeue, peek/top, isEmpty, isFull, size, clear, print
- types - simple queue, circular queue, priority queue, double ended queue
- queue implementation using array
https://www.geeksforgeeks.org/array-implementation-of-queue-simple/
- queue implementation using linked list
https://www.geeksforgeeks.org/queue-linked-list-implementation/
- queue implementation using stack
https://www.geeksforgeeks.org/queue-using-stacks/



BINARY TREE



BINARY SEARCH
- when to use - all the entries must be  sorted
- real life example - searching for a book in a library, searching for a person in a phone book, searching for a word in a dictionary
- binary search is a search algorithm that finds the position of a target value within a sorted array
- binary search is a divide and conquer algorithm
- binary search is a recursive algorithm
- binary search is a logarithmic time complexity algorithm




HEAP
- heap is a data structure that follows the Heap property
- heap is a binary tree
- heap is a complete binary tree
- heap is a binary tree where the value of each node is greater than or equal to the value of its children
- heap is a binary tree where the value of each node is less than or equal to the value of its children



TREE
- Binary Tree (can have max two nodes)
- terminologies -root node, children, parent, leaf node, ancestor, sibling, sub-tree, level, height, depth, degree of a node, degree of a tree
- types - full binary tree, complete binary tree, perfect binary tree, balanced binary tree, degenerate tree, skewed tree
- full binary tree - every node has either 0 or 2 children
- complete binary tree - all levels are completely filled except possibly the last level and the last level has all keys as left as possible
- perfect binary tree - all internal nodes have two children and all leaves are at the same level
- balanced binary tree - height of the tree is O(logN)
- degenerate tree - every node has only one child
- Traversal in a tree - BFS & DFS(inorder, preorder, postorder)



GRAPH
------
- terminologies - nodes/vertices, edge, directed edge, undirected edge, cycle of a graph, 
- types - directed graph, undirected graph, weighted graph, unweighted graph, connected graph, disconnected graph, cyclic graph, acyclic graph, complete graph, regular graph, complete bipartite graph, planar graph, multigraph, pseudograph, simple graph
- directed graph - edges have direction
- undirected graph - edges have no direction
- weighted graph - edges have weight
- unweighted graph - edges have no weight
- connected graph - every node is reachable from every other node
- disconnected graph - 
- cyclic graph -
- acyclic graph -
- complete graph -
- regular graph -
- complete bipartite graph -
- planar graph -
- multigraph -
- pseudograph - 
- simple graph -





DYNAMIC PROGRAMMING
- techniques - memoization, tabulation
- memoization - technique of storing the solution of a subproblem, so that we do not have to recompute it when needed later.
- tabulation - 
- types - top-down, bottom-up
- memoization - top-down
- tabulation - bottom up 
- overlapping subproblems - when a subproblem is called multiple times 
- optimal substructure - when an optimal solution can be constructed from optimal solutions of its subproblems
- 

