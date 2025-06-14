# RESOURCE - takeuforward.org
# ---------------------------

2.1 -> 3
2.2 -> 4
3.1 -> 13
3.2 -> 6,8,14

""" 

Majority Element  - > n/2 (3.2.3), > n/3 (3.3.2)
Two sum - 2 sum (3.2.1), 3 sum (3.3.3), 4 sum (3.3.4)
binary search - (8,9)


algorithm - 

Euclidian algo for HCF/GCD ✅

selection sort✅, bubble sort✅, insertion sort, merge sort✅, quick sort, 

Dutch National flag algorithm✅, Moore's voting algorithm✅

Kadane's algorithm✅, extended version of kadane's algorithm✅, Boyer Moore's majority voting algorithm✅

Manacher's Algorithm, the Tortoise and Hare algorithm., Sieve of Eratosthenes algorithm, Shunting Yard algorithm, Job First algorithm, least recently used (LRU) page replacement , flood-fill-algorithm, topological-sort-algorithm, kahn's algorithm, Dijkatra's algorithm, bellman ford algorithm, floyd warshall algorithm, Prim's algorithm, kruskal's algorithm, tarjans-algorithm, kosaraju's algorithm, Rabin-Karp Algorithm, KMP algo/LSP(pl) array or Knuth-Morris-Pratt Algorithm),


"""



# region ARRAY
# ------------ 
# array 
'''
data structure that stores a collection of elements (usually of the same type) in a contiguous block of memory.
'''
# characteristics of array
'''
stores multiple values in one variable, fixed size.
elements are stored sequentially, contiguous memory.
can be accessed using indices (starting at 0).
typically stores items of the same data type (especially in low-level languages).
'''
# operations
''' 
Access	            Get value at a specific index	                arr[2] → 30
Update	            Change value at a specific index	            arr[2] = 99
Insert	            Add a new item (not native in arrays)	        arr.insert(2, 25)
Append	            Add to the end	                                arr.append(60)
Delete	            Remove an item	                                del arr[1] or arr.remove(20)
Search	            Find if an item exists	                        30 in arr → True
Length	            Number of items	                                len(arr) → 5
Iteration	        Loop through all items	                        for item in arr: print(item)
'''
# time complexity
'''
Access              | O(1) |                                        Fast: Direct index access
Search              | O(n) |                                        Linear search unless sorted
Insert              (End) | O(1) / O(n) |                           Amortized O(1), worst O(n)
Insert              (Middle) | O(n) |                               Needs shifting
Delete              | O(n) |                                        Shifting required
'''
# application of arrays 
'''
data structures (stacks, queues, heaps)
image processing (pixels in 2D arrays)
machine learning (vectors and matrices)
database indexing
games (2D maps, player positions)
simulations
'''
# types of array 
# one dimentional array
'''
# Python List (most common, flexible, can hold mixed types) 
arr = [1, "hello", 3.5]

# Array Module (for numeric values only)    
import array
a = array.array('i', [1, 2, 3])

# NumPy Arrays (powerful for numerical computing) 
import numpy as np
a = np.array([1, 2, 3])
'''
# multi dimentional array
'''
# normal array
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(matrix[1][2])  # Output: 6

# with numpy
import numpy as np
a = np.array([[1, 2], [3, 4]])
print(a[1][0])  # Output: 3
'''

# arrays vs list vs tuple 
'''
Feature             | List          | Tuple             | Array 
Mutable             | ✅            | ❌               | ✅
Fixed Type          | ❌            | ❌               | ✅
Performance         | Medium        | Fastest           | Fast (numeric)

'''

- maximum array size can be 10^7 in c++ and 10^6 in python

# endregion


# region LINKED LIST 
'''
https://www.youtube.com/watch?v=Nq7ok-OyEpg&list=PLgUwDviBIf0oF6QL8m22w1hIDC1vJ_BHz&index=237

Reference - mysirji, takeuforward

- follows the First In First Out (FIFO) principle
- linear data structure
- collection of elements
- non-primitive data structure
- NOT in contegious memory allocation
- types of linked list - single linked list, double linked list, circular linked list, doubly circular linked list

- head - first element of the linked list
- tail - last element of the linked list
- next - pointer to the next element
- prev - pointer to the previous element
- data - data stored in the linked list


- heap memory ?
- stack memory ?

- operations - insertion, deletion, traversal, search, sorting, merging, splitting, reversing, rotating, shuffling
- types - single linked list, double linked list, circular linked list, doubly circular linked list
- real world examples - 
browser url - search -> takeuforward.org -> a2z -> article

- application of linked list - in stacks ans queues



'''


GREEDY ALGORITHM 
- greedy algorithm is an algorithm that always makes the choice that looks best at the moment

when not to use greedy algorithm
when there is no uniformity in the data, sometimes it may be very large sometimes it may be very less and it cannot sorted like in a 2D matrix 


# endregion 



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

- Time Complexity (TC): 
O(1) -> for average and best case 
O(n) -> for worst case, where n is the number of elements in the map.

- Space Complexity (SC): 
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

- Time Complexity (TC): O(log n), where n is the number of elements in the map.

- Space Complexity (SC): 
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

- Time Complexity (TC): O(n), where n is the number of elements in the array.

- Space Complexity (SC): O(n), where n is the number of unique elements in the array.
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

- Time Complexity (TC): O(n), where n is the number of elements in the array.

- Space Complexity (SC): O(n), where n is the number of unique elements in the array.
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
- FOR CALL STACK / STACK SPACE, when the function is called first donot put it in the call stack, when it is called during the function execution then put it inside the stack
- FOR RECURSION TREE, when the function is called first put it in the recursion tree, when it is called during the function execution then again put it inside the recursion tree
- base case - the condition when the recursion stops
- recursive call - the function calls itself
- recursive call stack - the stack of recursive calls
- recursive call stack frame - the frame of the recursive call
- recursive call stack frame size - the size of the recursive call stack frame
- segmentation fault / stack overflow - when the recursive call stack frame size exceeds the memory limit
'''

# endregion



# region BIT MANIPULATION
'''
OPERATORS
---------
code for binary to decimal
//...code
code for decimal to binary
//...code
code for 1's complement
//...code
code for 2's complement
//...code

and - & (all true -> true, 1 false -> false)
a = 5   # 0101 in binary
b = 3   # 0011 in binary
result = a & b  # 0001 in binary (1 in decimal)
print(result)  # Output: 1

or - | (1 true -> true, all false -> false)
a = 5   # 0101 in binary
b = 3   # 0011 in binary
result = a | b  # 0111 in binary (7 in decimal)
print(result)  # Output: 7

xor - ^ (nos of 1's odd -> 1, nos of 1's even -> 0 )
The bitwise XOR (exclusive OR) operator compares corresponding bits of two numbers and returns a 1 if the bits are different, otherwise, it returns 0.
a = 5   # 0101 in binary
b = 3   # 0011 in binary
result = a ^ b  # 0110 in binary (6 in decimal)
print(result)  # Output: 6

not - ~
The bitwise NOT operator inverts the bits of the number. It flips 0 to 1 and 1 to 0. In Python, ~a is equivalent to -a-1 because of the way negative numbers are represented in binary using two's complement.
- for positive number 
convert to binary 
flip the values 
check if the flipped value is negative or not ie sign bit is 1 or not, if it's negative store 2's complement of the flipped value ie flip it again and 1 else stop and store the binary value
- for negative number
take 2's complement of the number
flip the values of 2's complement value
check if the flipped value is negative or not ie sign bit is 1 or not, if it's negative store 2's complement of the flipped value ie flip it again and 1 else stop and store the binary value
a = 5   # 0101 in binary
result = ~a  # Inverts the bits
print(result)  # Output: -6 (because ~5 = -6 in two's complement)

shift - 
<< (left shift, multiply by 2) 
The left shift operator (<<) shifts the bits of a number to the left by the specified number of positions. Each shift to the left is equivalent to multiplying the number by 2.
- if left shift by 1 the INT-MAX, then it will throw error says data overflow
a = 5   # 0101 in binary
result = a << 2  # Shifting left by 2 positions (multiply by 2^2 = 4)
print(result)  # Output: 20 (10100 in binary)


>> (right shift, divide by 2, num // 2^k where num is the given number and k is shift)
The right shift operator (>>) shifts the bits of a number to the right by the specified number of positions. Each shift to the right is equivalent to integer division by 2.
a = 20  # 10100 in binary
result = a >> 2  # Shifting right by 2 positions (divide by 2^2 = 4)
print(result)  # Output: 5 (0101 in binary)

# store 13 and -13 in 32-bit system, the last bit or 32nd bit is the sign bit, 0 for positive and 1 for negative
- store positive number as it's binary
13 = 00000000000000000000000000001101
- store negative number as 2's complement
-13 = 
13 binary is 00000000000000000000000000001101
1's complement of 13 is 11111111111111111111111111110010
add 1 to the binary number is 11111111111111111111111111110011

- largest integer number a 32-bit system can store is 2^31 - 1 = 2147483647, INT-MAX
- smallest integer number a 32-bit system can store is -2^31 = -2147483648, INT-MIN
'''

# endregion


# region STRINGS

# http://youtube.com/watch?v=9kdHxplyl5I&list=PLgUwDviBIf0oF6QL8m22w1hIDC1vJ_BHz&index=272

# - sliding window is a technique used to solve problems related to arrays and strings
# - when to use - when we have a problem that involves finding the maximum or minimum of a subarray of size k


# TWO POINTERS TECHNIQUE 
# - two pointers is a technique used to solve problems related to arrays and strings
# - where to use -


# PATTERN 1 - constant size window
'''
Example - Maximum Sum of a Subarray of Size K
'''
def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        return None  # If array length is smaller than k, no valid subarray exists

    # Calculate sum of first 'k' elements (initial window)
    window_sum = sum(arr[:k])
    max_sum = window_sum  # Initialize max_sum with the first window sum

    start = 0  # Start index of the sliding window
    end = k    # End index (exclusive) of the sliding window

    # Slide the window while the end pointer is within array bounds
    while end < n:
        # Remove the element leaving the window and add the new element coming in
        window_sum = window_sum - arr[start] + arr[end]

        # Update max_sum if the current window sum is greater
        if window_sum > max_sum:
            max_sum = window_sum

        # Move the window forward by incrementing start and end
        start += 1
        end += 1
    return max_sum

# Example usage:
arr = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum_subarray(arr, k))  # Output: 9

# PATTERN 2 - longest subarray/sustring where <condition>
'''
Example - Maximum Sum of a Subarray of Size K
'''
'''
Brute Force - using nested loops, using breaks and continue
'''
def longest_subarray_bruteforce(arr, k):
    n = len(arr)          # Get the length of the array
    max_len = 0           # Initialize max length of subarray found so far to 0
    # Outer loop picks the start index of the subarray
    for i in range(n):
        current_sum = 0   # Reset the current sum for the new start index
        # Inner loop picks the end index of the subarray
        for j in range(i, n):
            current_sum += arr[j]  # Add the current element to the current sum
            # Check if the current sum is within the allowed limit k
            if current_sum <= k:
                # Update max_len if the current subarray is longer than previous max
                max_len = max(max_len, j - i + 1)
            else:
                # If sum exceeded k, no need to check longer subarrays starting at i
                break
    return max_len   # Return the length of the longest subarray found

arr = [2, 5, 1, 7, 10]
k = 14
print(longest_subarray_bruteforce(arr, k))  # Output: 3 (e.g. subarray [2, 5, 1])

'''
Better Approach - using two pointers l and r, r is incremented to expand, l is incremented to shrink
'''
def longest_subarray_with_sum_less_than_k(arr, k):
    n = len(arr)         # Length of the array
    l = 0                # Left pointer of the window (start of subarray)
    r = 0                # Right pointer of the window (end of subarray)
    current_sum = 0      # Sum of elements in the current window
    max_len = 0          # Maximum length of valid subarray found so far

    # Move the right pointer to expand the window
    while r < n:
        current_sum += arr[r]   # Add the current element to the window sum

        # If the sum exceeds k, shrink the window from the left
        while current_sum > k:
            current_sum -= arr[l]  # Remove the leftmost element
            l += 1                # Move the left pointer to the right

        # At this point, sum <= k, update max_len if this window is longer
        if current_sum <= k:
            max_len = max(max_len, r - l + 1)
        r += 1   # Expand the window by moving right pointer to the right
    return max_len

arr = [2, 5, 1, 7, 10]
k = 14
print(longest_subarray_with_sum_less_than_k(arr, k))  # Output: 3 (e.g. subarray [2, 5, 1])

'''
optimal approch - replacing while with if
'''
def longest_subarray_with_sum_less_than_k(arr, k):
    n = len(arr)
    l = 0                  # Left pointer of the sliding window
    r = 0                  # Right pointer of the sliding window
    current_sum = 0        # Current sum of the sliding window
    max_len = 0            # Maximum length found so far

    while r < n:
        current_sum += arr[r]   # Expand window by adding element at right pointer

        # Shrink window from left if sum exceeds k
        if current_sum > k:
            current_sum -= arr[l]
            l += 1

        # Update max length if current sum <= k
        if current_sum <= k:
            max_len = max(max_len, r - l + 1)
        r += 1
    return max_len

arr = [2, 5, 1, 7, 10]
k = 14
print(longest_subarray_with_sum_less_than_k(arr, k))  # Output: 3 ([2, 5, 1])

# PATTERN 3 - Number of subarrays where <condition>
'''
Example - Maximum Sum of a Subarray of Size K
'''
'''
Use better approch of previous problem to solve this problem
'''
def count_subarrays_sum_k(arr, k):
    n = len(arr)
    l = 0
    current_sum = 0
    count = 0

    for r in range(n):
        current_sum += arr[r]  # Expand window from right
        # Shrink window from left while sum > k (non-negative array assumption)
        while current_sum > k and l <= r:
            current_sum -= arr[l]
            l += 1

        # If current sum equals k, increment count
        if current_sum == k:
            count += 1
    return count

arr = [1, 2, 3, 4, 2]
k = 5
print(count_subarrays_sum_k(arr, k))  # Output: 2 ([2,3], [5])

# PATTERN 4 - Shortest/minimum window where <condition>
'''
Example - Maximum Sum of a Subarray of Size K
'''
def min_subarray_len_with_sum_at_least_k(arr, k):
    n = len(arr)
    left = 0
    current_sum = 0
    min_len = float('inf')  # Track minimum length found

    for right in range(n):
        current_sum += arr[right]  # Expand window by adding arr[right]
        # Shrink window from left as long as condition is met
        while current_sum >= k:
            min_len = min(min_len, right - left + 1)  # Update minimum length
            current_sum -= arr[left]  # Remove leftmost element
            left += 1  # Shrink window
    # If min_len was never updated, return 0 (no such window)
    return 0 if min_len == float('inf') else min_len

arr = [2, 3, 1, 2, 4, 3]
k = 7
print(min_subarray_len_with_sum_at_least_k(arr, k))  # Output: 2 ([4,3])

# endregion 

# region STACK 
- stack is a data structure that follows the Last In First Out (LIFO) principle
- stack is a linear data structure
- stack is a collection of elements
- stack is a non-primitive data structure
 homogeneous data structures
indexing is typically not maintained 
- list are used in python for implementing stacks

- operations - push/add, pop, peek/top, isEmpty, isFull, size, clear, print
- stack implementation using array
https://www.geeksforgeeks.org/implement-stack-using-array/
- stack implementation using linked list
https://www.geeksforgeeks.org/implement-a-stack-using-singly-linked-list/
- stack implementation using queue 
https://www.geeksforgeeks.org/implement-stack-using-queue/
# endregion


# region QUEUE
- queue is a data structure that follows the First In First Out (FIFO) principle
- queue is a linear data structure
- queue is a collection of elements
indexing is typically not maintained 
 homogeneous data structures

Use deque from the collections module for a general-purpose queue.
from collections import deque

queue = deque()
queue.append(1)  # Enqueue element to the back
queue.append(2)
queue.append(3)

print(queue.popleft())  # Dequeue element from the front (1)
print(queue.popleft())  # Dequeue next element (2)

Use queue.Queue for thread-safe queues.
    import queue

q = queue.Queue()

q.put(1)  # Enqueue element
q.put(2)
q.put(3)

print(q.get())  # Dequeue element (1)
print(q.get())  # Dequeue next element (2)



- list are used in python for implementing stacks
- queue is a non-primitive data structure
- operations - enqueue/add, dequeue, peek/top, isEmpty, isFull, size, clear, print
- types - simple queue, circular queue, priority queue, double ended queue
- queue implementation using array
https://www.geeksforgeeks.org/array-implementation-of-queue-simple/
- queue implementation using linked list
https://www.geeksforgeeks.org/queue-linked-list-implementation/
- queue implementation using stack
https://www.geeksforgeeks.org/queue-using-stacks/
# endregion


BINARY TREE



# region BINARY SEARCH
# binary search
'''
- search algorithm that finds the position of a target value within a sorted array
- recursive algorithm
'''
# time complexity 
'''
O(log2(n)) - logarithmic time complexity algorithm
'''
# time complexity
'''
Best Case: O(1) (found at the middle)
Average & Worst Case: O(log n)
'''
# space complexity:
'''
Iterative: O(1)
Recursive: O(log n) due to recursive call stack
'''
# when to apply binary search
'''
when the search space is sorted
''' 
# real life examples of binary serach
'''
searching for a book in a library, searching for a person in a phone book, searching for a word in a dictionary
Search engines
Databases (B-Trees use binary search internally)
Debugging: Finding first buggy commit (via binary search)
Games/AI: Efficient decision-making
Competitive Programming: Super useful in time-constrained problems
'''
# iterative approch to implement binary search
def binary_search_iterative(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found

arr = [1, 3, 5, 7, 9, 11, 13]
target = 7
print(binary_search_iterative(arr, target))

# recursive approch to implement binary search
def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1  # Base case: target not found

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)

arr = [1, 3, 5, 7, 9, 11, 13]
target = 7
print(binary_search_recursive(arr, target))

# Overflow condition
'''
IF low or high - float("inf") or exceeds integer range

mid = (low + high) // 2 ❌

mid low + (high - low) // 2 ✅
'''

# endregion



HEAP
- heap is a data structure that follows the Heap property
- heap is a binary tree
- heap is a complete binary tree
- heap is a binary tree where the value of each node is greater than or equal to the value of its children
- heap is a binary tree where the value of each node is less than or equal to the value of its children



# region TREE
'''
takeuforwrd.org - https://www.youtube.com/watch?v=_ANrF3FJm7I&list=PLgUwDviBIf0oF6QL8m22w1hIDC1vJ_BHz&index=73

'''
# - Binary Tree (can have max two nodes)
- terminologies - root node, children, parent, leaf node, ancestor, sibling, sub-tree, level, height, depth, degree of a node, degree of a tree
- types - full binary tree, complete binary tree, perfect binary tree, balanced binary tree, degenerate tree, skewed tree
- full binary tree - every node has either 0 or 2 children
- complete binary tree - all levels are completely filled except possibly the last level and the last level has all keys as left as possible
- perfect binary tree - all internal nodes have two children and all leaves are at the same level
- balanced binary tree - height of the tree is O(logN)
- degenerate/skewed tree - every node has only one child
- Traversal in a tree - BFS & DFS(inorder, preorder, postorder)

real lfe example - folder structure in computer systems

# endregion

# region BINARY SEARCH TREE 

- bst -> left node value < right node value < root node value
- duplicate values are not allowed
- height of the bst - O(logN)






# endregion

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





# region DYNAMIC PROGRAMMING

'''
those who cannot remember the past are condemned to repeat it. ~ DP

ways to solve DP - tabulation and memoization

tabulation - bottom up approach

memoization - top down approach, tend to store the value of sub problems in some map/table

space optimization - 

overlapping subproblems - 



1. Recursion: each function calls give rise to 2 more: therefore O(2^n)
2. Memoization: stores in an array: O(n)
   Subproblem results are stored in an array, ensuring that each subproblem is solved only once.
3. Tabulation: iterative approach and takes O(n) subproblems from the smallest to the largest.
RECURSION: Top down: We start from answer, go to the base case and then go back
MEMOIZATION: TOP DOWN:  avoids redundant calls done in recursion reducing time complexity
TABULATION IS: Bottom up: We start from the base case and we try to go to the required answer



where to use recursion - 
try all possible ways - count or maximum/minimum
1. when we have to find the number of ways to do something
2. when we have to find the maximum/minimum of something

how to convert recursion to DP -
1. Try to represent any problems in terms of index
2. Do all possible stuffs on that index, according to the problem statement
3. Sum of all stuffs ->count all the ways , min(of all stuffs) -> Find min

steps to convert a memoization solution into a tabulation solution
1. Declare base cases
2. express all states in for loops
3. Copy the recurence and write

when can we apply space optimization technique -
1. when we have 2 states and the value of the states is dependent on the previous value of the state
ie if there is a previous data row and previous column in case of 2D array
ic if there are two states value previous data like n-1 and n-2


when not to use greedy algorithm
when there is no uniformity in the data, sometimes it may be very large sometimes it may be very less and it cannot sorted like in a 2D matrix 

subsequence/subsets - may be contiguous or non-contiguous
[1,2,3]
subsets - [1,2,3], [1,2], [1,3], [2,3], [1], [2], [3], [] ✅ need to follow order
non-subsequence - [3,2,1], [3,1], [2,1], [1] ❌

how to solve subsequences/subarray problem
1. express in (index, target)
2. explore possibilities of that index
- arr[index is the part of the subsequence 
- arr[index] is not the part of the subsequence
3. return True/False

how to solve subsequences/subarray problem
1. express in index_1, index_2
2. explore possibilities of that index
3. take the best among them


how to solve dp problems on stocks
1. express in (index, buy)
2. explore possibilities on that index
3. take the max of all profits made
4. base case



'''

- techniques - memoization, tabulation
- memoization - technique of storing the solution of a subproblem, so that we do not have to recompute it when needed later.
- tabulation - 
- types - top-down, bottom-up
- memoization - top-down
- tabulation - bottom up 
- overlapping subproblems - when a subproblem is called multiple times 
- optimal substructure - when an optimal solution can be constructed from optimal solutions of its subproblems
- 

# endregion 