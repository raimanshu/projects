


# region 1.2 PATTERN PROBLEMS 
# ---------------------------




# region 1.4 MATHS PROBLEM (123 / 10 = 12.000...., 123 % 2 = 3)
# -------------------------------------------------------------

# NOTE : 

# TODO : 1 Count digits in a number - 
# Method 1 - brute force, TC- O(log10(N) + 1), SC - O(1)
def count():
  count = 0
  while(num > 0):
    count = count + 1  
    num = num//10
  return count

num = 5216566
print(count(num))

# Method 2 - optimal approch, int(log10(Number) +  1), TC - O(1), SC - O(1)
import math
num = 5216566
print(int(math.log10(num)) + 1)


# TODO : 2 Reverse a number -
# Method 1 - optimal approch, newNumber = newNumber * 10 + lastDigit, TC - O(log10(N) + 1), SC - O(1)
def reverse(n):
  reverse_num = 0
  while(num > 0):
    rem = num % 10
    reverse_num = reverse_num * 10 + rem
    num = num//10
  return int(reverse_num)

num = 23521
print(reverse(num))

# Method 2 - use euclidian maths 
num = 521
reverse_num = ""
while(num > 0):
  reverse_num = reverse_num + str(num%10)
  num = num//10
print(int(reverse_num))


# TODO : 3 Check pallindrome - 121
# Method 1 - optimal solution, use euclidian maths, TC - O(log10(N) + 1), SC - (1) 
def pallindrome(num):
  original_num = num
  reverse_num = 0
  while(num > 0):
    rem  = num % 10
    reverse_num = reverse_num * 10 + rem
    num = num//10
  if original_num is reverse_num:
    return True
  else:
    return False
num = 121
print(pallindrome(num))

# 4 Armstrong Numbers - (3^3 + 7^3 + 1^3 = 371)
# Method 1 - optimal approch, use euclidian maths, TC - O(log10(N) + 1), SC - O(1)
def armstrong(num):
  original_num = num
  calculated_num = 0
  while(num > 0):
    temp_num = num%10
    calculated_num = calculated_num + temp_num * temp_num * temp_num
    num = num//10
  if original_num == calculated_num:
    print(f"{original_num} is armstrong number.")
  else:
    print(f"{original_num} is not armstrong number.")
num = 371
print(armstrong(num))

# 5 Print all divisors
#     method 1 - optimized approch, using math.sqrt(), TC - O(sqrt(N)), SC - (2*sqrt(N))
import math
def divisors(num):
  divisors_lst = []
  for i in range(1,int(math.sqrt(num))):
    if(num%i == 0):
      divisors_lst.append(i)
      if(num//i != i):
        divisors_lst.append(num//i)
  return divisors_lst

num = 15
print(divisors(num))

# Method 2 - brute force, check number % i === 0, TC - O(N), SC - O(N)
def divisors(num):
  divisors_lst = []
  for i in range(1,num):
    if num%i == 0:
      divisors_lst.append(i)
num = 15
print(divisors(num))

# 6 Check for prime (having exactly two factors, 1 and itself)
# Method 1 - brute force, TC -O(N), SC - O(1)
def checkPrime(num):
  divisors_lst = []
  for i in range(1,num):
    if num%i == 0:
      divisors_lst.append(i)
  if(len(divisors_lst) == 2):
    print(f"{num} is not prime number.")
  else:
    print(f"{num} is prime number.")
num = 15
print(checkPrime(num))

# Method 2 - optimal approch, TC -O(sqrt(N)), SC - O(1)
def checkPrime(num):
  cnt = 0
  for i in range(1,int(sqrt(num)) + 1):
    if num%i == 0:
      cnt = cnt + 1
      if (num//i != i):
        cnt = cnt + 1
  if(cnt == 2):
    print(f"{num} is not prime number.")
  else:
    print(f"{num} is prime number.")
num = 15
print(checkPrime(num))

# 7 GCD or HCF (Highest Common Factor)
# Method 1 - brute force, using euclidian maths, TC - O(min(N1,N2)), SC - O(1)
def find_hcf(num_1, num_2):
  hcf = 1
  for i in range(1, min(num_1, num_2)):
    if num_1%i == 0 and num_2%i == 0:
      hcf = i
  return hcf
num_1 = 18
num_2 = 12
print(find_hcf(num_1,num_2))

# Method 2 - brute force, using euclidian maths, TC - O(min(N1,N2)), SC - O(1)
def find_hcf(num_1, num_2):
  hcf = 1
  for i in range(min(num_1, num_2), 0, -1):
    if num_1%i == 0 and num_2%i == 0:
      hcf = i
  return hcf
num_1 = 18
num_2 = 12
print(find_hcf(num_1,num_2))

# 8 method 3 : optimal approch, Euclidian algo, TC - O(min(N1,N2)), SC - O(1)
'''  GCD(a, b) = GCD(a-b, b) if a > b
  =>  GCD(a, b) = GCD(a % b, b) if a > b
'''
def find_gcd(a, b):
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    if a==0:
        return b
    else:
        return a
print(find_gcd(8, 12))

# endregion




# region 1.5 RECURSION PROBLEM
# ----------------------------

# 1 Introduction
# NOTE : https://www.youtube.com/watch?v=6IIgSFBPQ0U 
# 2 print name N times using recursion 
def recursive_call_1(N):
  if N == 0:
    return 
  print("Himanshu")
  recursive_call_1(N-1)
recursive_call_1(5)

# 3 print 1 to N using recursion
def recursive_call_2(N):
  if N == 0:
    return 
  recursive_call_2(N-1)
  print("head recursion => ", N)
recursive_call_2(5)

# 4 print N to 1 using recursion
def recursive_call_3(N):
  if N == 0:
    return 
  print("tail recursion => ", N)
  recursive_call_3(N-1)
recursive_call_3(5)

# 5 sum of first N numbers
def sum(N):
  if N == 1:
    return 1
  return N + sum(N-1)
print(sum(3))

# 6 factorial of a numbers
def fact(N):
  if N == 1:
    return 1
  return N * fact(N-1)
print(fact(4))

# TODO : 7 reverse an array
# NOTE: https://www.youtube.com/watch?v=twuC1F6gLI8&list=PLgUwDviBIf0oF6QL8m22w1hIDC1vJ_BHz&index=11
# method 1 - using built-in methods
def rev(arr, reversed_arr):
  if len(arr) == 0:
    return
  reversed_arr.append(arr.pop())
  rev(arr, reversed_arr)
  return reversed_arr
print(rev([3,2,1],[]))

# method 2 - using python swaping technique
def reverse_arr(arr, start, end):
  if start >= end:
    return
  arr[start], arr[end] = arr[end], arr[start]                           # ---> swaping in python
  reverse_arr(arr, start+1, end-1)
  return arr

array = [1,2,3,4]
print(reverse_arr(array, 0, len(array) - 1))

# method 3 - without using any other variable
def reverse_arr(arr, index):
  if index >= len(arr)//2:
    return arr
  arr[index], arr[len(arr) - index - 1] = arr[len(arr) - index - 1], arr[index]      # ---> start = arr[i], end = arr[len(arr) - i 1]
  return reverse_arr(arr, index + 1)
  
array = [1,2,3,4]
print(reverse_arr(array, 0))

# method 4 - using for loop / extra array
def reverse_arr(arr):
  reversed_arr = [0]*len(arr)
  for i in range(n-1, -1, -1):
    reversed_arr[n-i-1] = arr[i]
  return reversed_arr
array = [1,2,3,4]
print(reverse_arr(array, 0))

# method 4 - using while loop/ space optimized meyhod
def reverse_arr(arr, index):
  p1 = 0
  p2 = len(arr) - 1
  while p1 < p2:
    arr[p1], arr[p2] = arr[p2], arr[p1]
    p1 += 1
    p2 -= 1
  return arr
array = [1,2,3,4]
print(reverse_arr(array, 0))

# 8 TODO : check if a string is palindrome or not using recursion
# method 1 : using while loop 
def pallindrome(str, i):
  left = 0
  right = len(str) - 1
  while left < right:
    if str[left] != str[right]:
      return False
    left += 1
    right -= 1
  return True
print(pallindrome("MADAM", 0))

# method  2 : using recursion  
def pallindrome(str, i):
  if i >= len(str)//2:
    return True
  if str[i] != str[len(str) - i - 1]:
    return False
  return pallindrome(str, i + 1)    
print(pallindrome("MADAM", 0))
  
# 9 fibonacci number
def fibonacci(num):
  if num == 0: return 0
  if num == 1: return 1
  return fibonacci(num-2) + fibonacci(num-1)
  
print(fibonacci(6))

# endregion




# region 1.6 HASHING PROBLEM
# --------------------------

# TODO : 1 introduction
# theory - https://www.youtube.com/watch?v=TLk7_Ia3rzQ&t=431s
# practical - https://www.youtube.com/watch?v=KEs5UyBJ39g&list=PLgUwDviBIf0oF6QL8m22w1hIDC1vJ_BHz&index=13

# TODO : 2 counting frequency of array elements 
def frequency_arr(arr):
  freq_arr = [0] * (max(arr) + 1)
  for value in arr:
    freq_arr[value] = freq_arr[value] + 1
  return freq_arr

print(frequency_arr([1,2,4,5,3,2,4,1]))               # ---> [0, 2, 2, 1, 2, 1]

# TODO : 3 find the highest/lowest frequency element in an array
def frequency_arr(arr):
  freq_arr = [0] * (max(arr) + 1)
  for value in arr:
    freq_arr[value] = freq_arr[value] + 1

  highest_freq = max(freq_arr)
  lowest_freq = min(f for f in freq_arr if f > 0)

  highest_freq_index = freq_arr.index(highest_freq)
  lowest_freq_index = freq_arr.index(lowest_freq) 
  return {"highest_frequncy => " : highest_freq,
    "highest_frequncy_element => " : arr[highest_freq_index],
    "lowest_frequncy => " : lowest_freq,
    "lowest_frequncy_index => " : arr[lowest_freq_index],
  }

print(frequency_arr([1,2,4,5,3,2,4,1]))  # ---> {'highest_frequncy => ': 2, 'highest_frequncy_element => ': 2, 'lowest_frequncy => ': 1, 'lowest_frequncy_index => ': 5}


# endregion




# region 2.1 SORTING-I
# --------------------

# TODO : 1 selection sort
'''
- select the smallest element and swap
- https://www.youtube.com/watch?v=HGk_ypEuS24&list=PLgUwDviBIf0oF6QL8m22w1hIDC1vJ_BHz&index=14
- https://www.geeksforgeeks.org/selection-sort-algorithm-2/
'''
def selection_sort(arr):
  n = len(arr)
  for i in range(n-1):
    min = i
    for j in range(i+1,n):
      if arr[j] < arr[min]:
        min = j 
    arr[i], arr[min] = arr[min], arr[i]
  return arr  

print(selection_sort([1,2,4,5,3,2,4,1]))

# TODO : 2 bubble sort
'''
- swapping the adjacent elements and push the max element in the last
- https://www.youtube.com/watch?v=HGk_ypEuS24&list=PLgUwDviBIf0oF6QL8m22w1hIDC1vJ_BHz&index=14
- https://www.geeksforgeeks.org/bubble-sort/
'''
def bubble_sort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(n -i -1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr  

print(bubble_sort([1,2,4,5,3,2,4,1]))


# TODO : 3 insertion sort
'''
- takes an element and place it in the correct position
- https://www.youtube.com/watch?v=HGk_ypEuS24&list=PLgUwDviBIf0oF6QL8m22w1hIDC1vJ_BHz&index=14
- https://www.geeksforgeeks.org/insertion-sort/
'''
def insertion_sort(arr):
  n = len(arr)
  for i in range(1,n):
    key = arr[i]
    j= i-1
    while j>=0 and key < arr[j]:
      arr[j+1] = arr[j]
      j = j -1 
    arr[j+1] = key
  return arr  
print(insertion_sort([1,2,4,5,3,2,4,1]))

# endregion




# region 2.2 SORTING-II
# ---------------------

# TODO : 1 merge sort
'''
- divide array into two parts and sort them
- https://www.youtube.com/watch?v=ogjf7ORKfd8&list=PLgUwDviBIf0oF6QL8m22w1hIDC1vJ_BHz&index=15
- https://www.geeksforgeeks.org/merge-sort/ 
'''
def merge_sort(arr, low, high):
  if low >= high:
    return
  
  mid = (low + high)//2
  merge_sort(arr, low, mid )
  merge_sort(arr, mid+1, high)
  merge(arr, low, mid, high)
  return arr  
  
  
def merge(arr, low, mid, high):
  temp = []
  left = low
  right = mid+1
  
  while left<=mid and right<=high:
    if arr[left] < arr[right]:
      temp.append(arr[left])
      left = left + 1
    else:
      temp.append(arr[right])
      right = right + 1
      
  while left<=mid:
    temp.append(left)
    left = left + 1
    
  while right<=high:
    temp.append(right)
    right = right + 1
    
  for i in range(len(temp)):
    arr[low+1] = temp[i]
    
  # return arr
  
arr = [1,2,4,5,3,2,4,1]
print(merge_sort(arr, 0, len(arr)-1))

# TODO : 2 recursive bubble sort


# TODO : 3 recursive insertion sort

# TODO : 4 quick sort
'''
- pick a pivot and place it in the correct position
- https://www.youtube.com/watch?v=WIrA4YexLRQ&list=PLgUwDviBIf0oF6QL8m22w1hIDC1vJ_BHz&index=16
'''
def quick_sort(arr, low, high):
    if low < high:
        partition_index = find_right_place(arr, low, high)
        quick_sort(arr, low, partition_index - 1)
        quick_sort(arr, partition_index + 1, high)
    return arr

def find_right_place(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    
    while i < j:
        # find element greater than pivot
        while i <= high and arr[i] <= pivot:
            i += 1
            
        # find element smaller than pivot
        while j >= low and arr[j] > pivot:
            j -= 1
            
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[low], arr[j] = arr[j], arr[low]
    return j

arr = [1,2,4,5,3,2,4,1]
print(quick_sort(arr, 0, len(arr)-1))

# endregion




# region 3.1 ARRAYS - EASY
# ------------------------
# TODO : 1 largest element in an array
# - method 1 : brute force using sort, TC - O(N^2), TC - O(N)
def largest_element_2(arr):
  n = len(arr)
  for i in range(n-1):
    min = i
    for j in range(i+1, n):
      if arr[j] < arr[min]:
        min = j
    arr[i], arr[min] = arr[min], arr[i]
  return arr  
arr = [1,2,4,7,7,5]
largest_element_2(arr)
print("largest element => ", arr[len(arr) - 1])

# - method 2 : brute force using sort buit-in, TC - O(N log(N)), TC - O(N)
def largest_element_2(arr):
  arr.sort()
  return arr[-1]  
arr = [1,2,4,7,7,5]
print(largest_element_2(arr))

# - method 3 : using max()
print(max([1,2,4,7,7,5]))

# - method 4 : using loop, TC - O(n), SC - O(1) 
def largest_element_1(arr):
  largest = arr[0]
  for i in arr:
    if i > largest:
      largest = i
  return largest
print(largest_element_1([1,2,4,7,7,5]))

# ---------------------------------------------------------------------------------------------------------------------------------------------

# 2 TODO : find smallest and second largest element in an array
# method 1: brute force using sort, TC - O(N log(N)), TC - O(1)
# NOTE : ONLY WORK IF ARRAY DOESNOT CONTAIN DUPLICATES
def second_largest_element_2(arr):
  arr.sort()
  return {
    "smallest": arr[0],
    "second_largest": arr[len(arr)-2]
  }
arr = [1,2,4,7,7,5]
print(second_largest_element_2(arr))

# method 2: better approch, using loop, TC - O(N), SC - O(1)
def largest_smallest(arr):
  n = len(arr)
  if n == 0 and n==1:
    print(-1, -1)
  small = float("inf")
  second_small = float("inf")
  large = float("-inf")
  second_large = float("-inf")
  for i in range(n):
    small = min(small,arr[i])
    large = max(large,arr[i])
  for i in range(n):
    if arr[i] < second_small and arr[i] != small:
      second_small = arr[i]
    if arr[i] > second_large and arr[i] != large:
      second_large = arr[i]
  return {
    "smallest": small,
    "second_small": second_small,
    "large": large,
    "second_largest": second_large
  }
arr = [1,3,6,6,2,6]
print(largest_smallest(arr))

# method 3: optimal approch, TC - O(n), SC -- O(1)
def second_smallest(arr):
  if len(arr) < 2:
    return -1
  smallest_item = float("inf")
  second_smallest_item = float("inf")
  
  for i in range(len(arr)):
    if arr[i] < smallest_item:
      second_smallest_item = smallest_item
      smallest_item = arr[i]
    elif arr[i] < second_smallest and arr[i] != smallest_item:
      second_smallest = arr[i]
  return {"second_largest_item = " : second_largest_item, "largest_item = " : largest_item}

def second_largest(arr):
  if len(arr) < 2:
    return -1
  largest_item = float("-inf")
  second_largest_item = float("-inf")
  
  for i in range(len(arr)):
    if arr[i] > largest_item:
      second_largest_item = largest_item
      largest_item = arr[i]
    elif arr[i] > second_largest_item and arr[i] != largest_item:
      second_largest_item = arr[i]
  return {"second_largest_item = " : second_largest_item, "largest_item = " : largest_item}
  
arr = [1,3,6,6,2,6]
print(second_largest(arr))
print(second_smallest(arr))

# ---------------------------------------------------------------------------------------------------------------------------------------------

# 3 TODO : check if array is sorted
# method 1 : brute force, TC - O(N^2), SC - O(1)
def arr_sorted(arr):
  n = len(arr)
  for i in range(n):
    for j in range(i+1, n):
      if arr[i] > arr[j]:
        return False 
  return True
arr = [1,2,2,3,3,4]
print(arr_sorted(arr))

# method 2 : optimal approch, TC - O(N), SC - O(1)
def arr_sorted(arr):
  for i in range(1,len(arr)):
    if arr[i-1] > arr[i]:
      return False
  return True
arr = [1,2,2,3,3,4]
print(arr_sorted(arr))

# ---------------------------------------------------------------------------------------------------------------------------------------------

# 4 TODO : remove duplicate from sorted array
# - method 1: brute force, using set(), TC - O(Nlog(N)), SC - O(N)
def remove_duplicates(arr):
  my_set = set()
  for i in arr:
    my_set.add(i)
  return my_set
arr = [1,2,2,3,3,4]
print(remove_duplicates(arr))

# - method 2: optimal approch, using two pointers, TC - O(N), SC - O(1)
def remove_duplicates(arr):
    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
            
    print(arr)
    return i + 1, arr[:i+1]

arr = [1, 2, 2, 3, 3, 4]
k, unique_arr = remove_duplicates(arr)            # ---> k = 4, unique_arr = [1, 2, 3, 4]

# ---------------------------------------------------------------------------------------------------------------------------------------------

# 5 TODO : left rotate an array by one place
# - method 1: brute force, TC - O(N), SC - O(N)
def rotate_arr(arr):
    temp  = [0]*len(arr)
    temp = arr[0]
    for i in range(1, len(arr)):
      temp[i-1] = arr[i]
    temp[len(arr) - 1] = arr[0]
    return temp

arr = [1, 2, 2, 3, 3, 4]
print(rotate_arr(arr))

# - method 2: optimal approch, TC - O(N), SC - O(1)
def rotate_arr(arr):
    
    temp = arr[0]
    for i in range(1, len(arr)):
      arr[i-1] = arr[i]
    arr[len(arr)-1] = temp
    return arr

arr = [1, 2, 2, 3, 3, 4]
print(rotate_arr(arr))

# ---------------------------------------------------------------------------------------------------------------------------------------------

# 6 TODO : left rotate an array by d places
# - method 1: brute force, using temp arr,  TC - O(N), SC - O(N)
def rotate_arr(arr, rotation):
    if len(arr) == 0:
        return 
    rotation_number = rotation % len(arr)
    temp = arr[:rotation_number]
    for i in range(rotation_number, len(arr)):
      arr[i-rotation_number] = arr[i]
    arr[rotation_number : ] = temp
    return arr
arr = [1, 2, 2, 3, 3, 4]
print(rotate_arr(arr, 9))

# - method 2: optimal approch, using slicing, TC - O(i), SC - O(N)
def rotate_arr(arr, rotation):
    if len(arr) == 0:
      return 
    rotation_number = rotation%len(arr)
    arr[:rotation_number],arr[rotation_number : ] = arr[rotation_number : ],arr[:rotation_number] 
    return arr
arr = [1, 2, 2, 3, 3, 4]
print(rotate_arr(arr, 9))

# - method 3: optimal approch, using built-in reverse() and reversed() methods, TC - O(N), SC - O(1)
def left_rotate(arr, d):
    n = len(arr)    
    d = d % n    
    arr.reverse()
    arr[:d] = reversed(arr[:d])    
    arr[d:] = reversed(arr[d:])
    return arr

arr = [1, 2, 3, 4, 5]
d = 2
rotated_arr = left_rotate(arr, d)

# - method 4: optimal approch, using reversal algorithm,🤯🤯🤯
def reverse_arr(arr, start, end):
  while start <= end:
    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp
    start += 1
    end -= 1

def left_rotate(arr, d):
    n = len(arr)
    d = d % n
    reverse_arr(arr, 0, d - 1)
    reverse_arr(arr, d, n - 1)
    reverse_arr(arr, 0, n-1)

arr = [1, 2, 3, 4, 5]
d = 2
rotated_arr = left_rotate(arr, d)

# ---------------------------------------------------------------------------------------------------------------------------------------------

# 👉👉 TODO : left rotate an array by d places
# - method 1: brute force, using temp arr,  TC - O(N), SC - O(N)

# - method 2: optimal approch, using reversal algorithm,🤯🤯🤯
def reverse_arr(arr, start, end):
  while start <= end:
    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp
    start += 1
    end -= 1

def left_rotate(arr, d):
    n = len(arr)
    d = d % n
    reverse_arr(arr, 0, n - d - 1)
    reverse_arr(arr, n - d, n - 1)
    reverse_arr(arr, 0, n-1)

arr = [1, 2, 3, 4, 5]
d = 2
rotated_arr = left_rotate(arr, d)

# ---------------------------------------------------------------------------------------------------------------------------------------------

# 7 TODO : move all zeros to the end of the array
# - method 1: brute force, TC - O(N), SC - O(2N) 
def move_zeros(arr):
    temp = []
    temp2 = []
    for i in arr:
      if i != 0:
        temp.append(i)
      else:
        temp2.append(i)
    return temp + temp2
        
arr = [1, 0, 2, 3, 0, 4]
print(move_zeros(arr))

# method 2: optimal approch, using two pointers TC - O(N), SC - O(1)🤯🤯🤯
def move_zeros(arr):
  j = -1
  for i in range(len(arr)):
    if arr[i] == 0:
      j = i
      break
  if j == -1:
    return arr 
  for i in range(j+1, len(arr)):
    if arr[i] != 0:
      arr[i], arr[j] = arr[j], arr[i]
      j = j+1
  return arr    

arr = [1, 0, 2, 3, 0, 4]
print(move_zeros(arr))

# ---------------------------------------------------------------------------------------------------------------------------------------------

# 8 TODO : linear search
def linear_search(arr, target):
  for i in range(len(arr)):
    if arr[i] == target:
      return i
  return -1

# ---------------------------------------------------------------------------------------------------------------------------------------------

# 9 TODO : find the union of sorted arrays
# - method 1: brute force, using map, TC - O((M+N)log(M+N)), SC - O(1)
def union(arr1, arr2):
  freq = {}
  union = []
  for i in arr1:
    freq[i] = freq.get(i, 0) + 1
  for i in arr2:
    freq[i] = freq.get(i, 0) + 1
  return list(freq.keys())
arr1 = [0, 1, 2, 3, 4]
arr2 = [1,4,5,7]
print(union(arr1, arr2))

# - method 2: brute force, using set, TC - O((M+N)log(M+N)), SC - O(1)

def union(arr1, arr2):
  s1 = set()
  for i in arr1:
    s1.add(i)
  for i in arr2:
    s1.add(i)
  return list(s1)
arr1 = [0, 1, 2, 3, 4]
arr2 = [1,4,5,7]
print(union(arr1, arr2))


# method 2: optimal approch, using two pointers, TC - O(M+N), SC - O(1)🤯🤯🤯
def union(arr1, arr2):
  i,j = 0,0
  union = []
  while i < len(arr1) and j < len(arr2):
    if arr1[i] <= arr2[j]:
      if len(union) == 0 or union[-1] != arr1[i]:
        union.append(arr1[i])
      i += 1
    else:
      if len(union) == 0 or union[-1] != arr2[j]:
        union.append(arr2[j])
      j += 1
  while i < len(arr1):
    if union[-1] != arr1[i]:
      union.append(arr1[i])
    i += 1
  while j < len(arr2):
    if union[-1] != arr2[j]:
      union.append(arr2[j])
    j += 1
  return union
arr1 = [0, 1, 2, 3, 4]
arr2 = [1,4,5,7]
print(union(arr1, arr2))


# ---------------------------------------------------------------------------------------------------------------------------------------------


# 👉👉👉 TODO : find the intersection of sorted arrays


# ---------------------------------------------------------------------------------------------------------------------------------------------


# 10 TODO : find missing number in an array
# method 1 : brute force, TC - O(N^2), SC - O(1)
def missing_num(arr, n):
  for i in range(1, n +1):
    flag = 0
    if j in range(len(a)):
      if arr[j] == i:
        flag = 1
        break
    if flag == 0:
      return i
  return -1
print(missing_num([1,2,4,5], 5))

# method 2 : better solution, using hashing, TC - O(2*N), SC - O(N)
def missing_num(arr, n):
  hash = [0]*(n+1)
  for i in range(n-1):
    hash[arr[i]] += 1
  for i in range(1, n+1):
    if hash[i] == 0:
      return i
  return -1
print(missing_num([1,2,4,5], 5))

# method 3 : optimal solution, summation approch, TC - O(N), SC - O(1)
def missing_num(arr, n):
  summation = (n*(n+1))//2
  s2 = sum(arr)
  return summation - s2
print(missing_num([1,2,4,5], 5))

# method 4 : optimal solution, using XOR, TC - O(N), SC - O(1)
def missing_num(arr, n):
  xor1 = 0
  xor2 = 0
  for i in range(1, n+1):
    xor1 = xor1 ^ arr[i]
    xor2 = xor2 ^ (i + 1)
  xor1 = xor1 ^ n
  return xor1 ^ xor2
print(missing_num([1,2,4,5], 5))

# ---------------------------------------------------------------------------------------------------------------------------------------------

# 11 TODO : maximum consecutive ones
# method 1 : brute force, TC - O(N), SC - O(1)
def maximum_consecutive(arr):
  maximum = 0
  counter = 0
  for i in range(len(arr)):
    if arr[i] == 1:
      counter = counter + 1 
    else: 
      counter = 0
    maximum = max(maximum, counter)
  return maximum

print(maximum_consecutive([1,1,0,1,1,1,3,1,1]))

# method 2 : optimal solution 

# ---------------------------------------------------------------------------------------------------------------------------------------------

# 12 TODO : find the number that appears once and other number twice
# method 1 : brute force, TC - O(N^2), SC - O(1)
def appear_once(arr):
  for i in range(len(arr)):
    num = arr[i]
    count = 0
    for j in range(len(arr)):
      if arr[j] == num:
        count = count+1 
    if count == 1:
      return arr[i]

print(appear_once([1,1,3,3,2,4,4]))

# method 2 : better solution, using hash array, TC - O(N) + O(N) + O(N), SC - O(maxElement + 1)
def appear_once(arr):
  hash_arr = [0] * len(arr)
  # print(hash_arr)
  for i in range(len(arr)):
    hash_arr[arr[i]] = hash_arr[arr[i]] + 1
  for i in range(len(hash_arr)):
    if hash_arr[i] == 1:
      return i
  return -1
print(appear_once([1,1,3,3,2,4,4]))
  
# method 3 : better solution, using unorderd_map, TC - O(N*log(M)) + O(M), SC - O(M)
def appear_once(arr):
  unordered_map = {}
  for i in range(len(arr)):
    unordered_map[arr[i]] = unordered_map.get(arr[i],0) + 1
  for k,v in unordered_map.items():
    if v == 1:
      return k  
  return -1
print(appear_once([1,1,3,3,2,4,4]))

# method 5 : optimal solution, using XOR, TC - O(N), SC - O(1)
def appear_once(arr):
  xor = 0
  for i in range(len(arr)):
    xor = xor ^ arr[i]
  return xor
print(appear_once([1,1,3,3,2,4,4]))

# ---------------------------------------------------------------------------------------------------------------------------------------------

# 13 TODO : longest subarray with given sum K (positives) 🤯🤯🤯
# subarray - contigious part of the array 
# method 1 : brute force, TC - O(N^3), SC - O(1)
def sub_array(arr, target):
  length = 0
  for i in range(len(arr)):
    for j in range(i,len(arr)):
      total_sum = 0
      for k in range(i, j+1):
        total_sum = total_sum + arr[k]
      if total_sum == target:
        length = max(length, j-i+1)
  return length
print(sub_array([1,2,3,1,1,1,1,4,2,3], 3))

# method 2 : brute force solution, TC - O(N^2), SC - O(i)
def sub_array(arr, target):
  length = 0
  for i in range(len(arr)):
    total_sum = 0
    for j in range(i,len(arr)):
      total_sum = total_sum + arr[j]
      if total_sum == target:
        length = max(length, j-i+1)
  return length
print(sub_array([1,2,3,1,1,1,1,4,2,3], 3))

# - method 3 : better solution, using hashing, TC - O(N), SC - O(N) 🤯🤯🤯🤯
def sub_array(arr, target):
  n  = len(arr)
  preSumMap = {}
  sum = 0
  maxLen = 0
  for i in range(n):
    sun += arr[i]
    if sum == target:
      maxLen = max(maxLen, i+1)
    rem  = sum - target
    if rem in preSumMap:
      length = i - preSumMap[rem]
      maxLen = max(maxLen, length)
    if sum not in preSumMap:
      preSumMap[sum] = i
  return maxLen
print(sub_array([1,2,3,1,1,1,1,4,2,3], 3))

# - method 4 : better solution, using two pointers, TC - O(2*N), SC - O(1) 🤯🤯🤯🤯
def sub_array(arr, target):
  n  = len(arr)
  left, right = 0,0
  sum = 0
  maxLen = 0
  while right < n:
    while sum > target:
      sum -= arr[left]
      left += 1
    if sum == target:
      maxLen = max(maxLen, right-left+1)
    right += 1
    if right < n:
      sum += arr[right]
  return maxLen
print(sub_array([1,2,3,1,1,1,1,4,2,3], 3))

# ---------------------------------------------------------------------------------------------------------------------------------------------

# 14 TODO : longest subarray with given sum K (positives and negatives)
# method 1 : brute force, TC - O(N^3), SC - O(1)
def sub_array(arr, target):
  length = 0
  for i in range(len(arr)):
    for j in range(i,len(arr)):
      total_sum = 0
      for k in range(i, j+1):
        total_sum = total_sum + arr[k]
      if total_sum == target:
        length = max(length, j-i+1)
  return length
print(sub_array([1,-2,-3,1,1,-1,1,4,2,3], 3))

# method 2 : better approch, TC - O(N^2), SC - O(1)
def sub_array(arr, target):
  length = 0
  for i in range(len(arr)):
    for j in range(i,len(arr)):
      total_sum = 0
      for k in range(i, j+1):
        total_sum = total_sum + arr[k]
      if total_sum == target:
        length = max(length, j-i+1)
  return length
print(sub_array([1,-2,-3,1,1,-1,1,4,2,3], 3))

# method 3 : optimal approch, using hashing, TC - O(N), SC - O(N)
def sub_array(arr, target):
  n  = len(arr)
  preSumMap = {}
  sum = 0
  maxLen = 0
  for i in range(n):
    sun += arr[i]
    if sum == target:
      maxLen = max(maxLen, i+1)
    rem  = sum - target
    if rem in preSumMap:
      length = i - preSumMap[rem]
      maxLen = max(maxLen, length)
    if sum not in preSumMap:
      preSumMap[sum] = i
  return maxLen
print(sub_array([1,-2,-3,1,1,-1,1,4,2,3], 3))


# endregion




# region 3.1 ARRAYS - MEDIUM
# --------------------------

# 1 TODO : two sum problem : check if a pair with given sum exists in Array
# - method 1 : brute force, TC - O(N^2), SC - O(1)
def two_sum(arr, target):
  for i in range(len(arr)):
    for j in range(i,len(arr)):
      if arr[i]+arr[j] == target:
        return [i,j]
  return [-1,-1]
print(two_sum([2,6,5,8,11], 14))


# method 2 : better solution, using hash map, TC - O(N*log(N)), SC - O(N)
def two_sum(arr, target):
    hash = {}  # hash map to store {number: index}
    for i in range(len(arr)):
        num = arr[i]
        more_needed = target - num
        if more_needed in hash:
            return [hash[more_needed], i]
        more_needed[num] = i
    return [-1,-1]  
print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]

# method 3 : optimal solution, using two pointer, TC - O(N) + O(N*log(N)), SC - O(1)
def two_sum(arr, target):
  left_ptr = 0
  right_ptr = len(arr) -1
  arr.sort()
  while left_ptr < right_ptr:
    total_sum = arr[left_ptr] + arr[right_ptr] 
    if total_sum == target:
      return [left_ptr, right_ptr]
    if total_sum < target:
      left_ptr= left_ptr + 1
    else:
      right_ptr = right_ptr - 1 
    
print(two_sum([2,6,5,8,11], 14))

# ---------------------------------------------------------------------------------------------------------------------------------------------


# 2 TODO : sort an array of 0's and 2's
# - method 1 : brute force, using any sorting technique, TC - O(N*log(N)), SC - O(1)

# - method 2 : better approch, TC - O(N) + O(N), SC - O(1)  
def sort(arr):
  count0 = 0
  count1 = 0
  count2 = 0
  for i in arr:
    if i == 0:
      count0 = count0 + 1 
    elif i == 1:
      count1 = count1 + 1
    else:
      count2 = count2 + 1
  return [0]*count0 + [1]*count1 + [2]*count2
print(sort([0,1,2,0,0,2,2,0,1,1,1,0]))

# - method 3 : optimal solution, Dutch National flag algorithm, TC - O(N), SC - (1) 🤯🤯🤯
'''
RULES OF DUTCH NATIONAL FLAG ALGORITHM
1. All elements < pivot must be in the left partition. O -> low-1 => 0
2. All elements > pivot must be in the right partition. low -> mid-1 => 1
3. Elements equal to pivot can go either way. mid+1 -> high => 2
'''
def sort(arr):
    low = 0
    mid = 0
    high = len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low] 
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1  
        else:  
            arr[high], arr[mid] = arr[mid], arr[high] 
            high -= 1 
    return arr
print(sort([0,1,2,0,0,2,2,0,1,1,1,0]))

# ---------------------------------------------------------------------------------------------------------------------------------------------

# 3 TODO : find the majority element that occurs more than >n/2 times
# - method 1 : brute force, TC - O(N), SC - O(1)
def sort(arr):
  for i in range(len(arr)):
    count = 0
    for j in range(len(arr)):
      if arr[i] == arr[j]:
        count +=1
    if count > (len(arr)/2):
      return count
  return -1
print(sort([2,2,1,4,2,2,3]))

# - method 2 : better solution, using hashing, TC - O(N*log(N)) + O(N), SC - O(N)
def sort(arr):
  dict = {}
  for i in arr:
    dict[i] = dict.get(i,0) + 1
  for k,v in dict.items():
    if v > (len(arr)//2):
      return v 
  return -1
print(sort([2,2,1,4,2,2,3]))

# - method 3 : better solution, using Counter, TC - O(N*log(N)) + O(N), SC - O(N)
from collections import Counter
def sort(arr):
  counter = Counter(arr)
  for k,v in dict.items():
    if v > (len(arr)//2):
      return v 
  return -1
print(sort([2,2,1,4,2,2,3]))

# - method 3 : optimal solution, using Moore's voting algorithm,
'''
MOORE's VOTING ALGORITHM, it states that if an element occurs more than n/2 times in the array then it is the majority element.
'''
def moores_voting_algorithm(arr):
    el = None
    count = 0
    for i in range(len(arr)):
        if count == 0:
            el = arr[i]
            count = 1
        elif el == arr[i]:
            count += 1
        else:
            count -= 1
    count = arr.count(el)
    if count > len(arr) // 2:
        return el
    return None
arr = [2, 2, 1, 4, 2, 2, 3]
print(moores_voting_algorithm(arr))

# ---------------------------------------------------------------------------------------------------------------------------------------------

# 4 TODO : Kadane's algorithm, mximum subarray sum in an array
'''
KANDANE's ALGORITHM - 
- 
'''
# - method 1 : brute force, TC - O(N^3), SC - O(1)
def kandane_algo(arr):
  previous_sum = float('-inf')
  for i in range(len(arr)):
    for j in range(i, len(arr)):
      sum = 0
      for k in range(i,j):
        sum +=arr[k]
        previous_sum = max(previous_sum,sum)
  return previous_sum
arr = [-2,-3,4, -1,-2,1,2,-3]
print(kandane_algo(arr))


# - method 2 : better solution, time complexity O(n)
def kandane_algo(arr):
  previous_sum = float('-inf')
  for i in range(len(arr)):
    sum = 0
    for j in range(i, len(arr)):
      sum +=arr[j]
      previous_sum = max(previous_sum,sum)
  return previous_sum
arr = [-2,-3,4, -1,-2,1,2,-3]
print(kandane_algo(arr))

# - method 3 : optimal solution, using Kandane's algo, TC -O(N), SC - (1) 🤯🤯🤯
'''
# https://www.youtube.com/watch?v=AHZpyENo7k4
'''
# below function is also right 
# def kadane_algorithm(arr):
#     current_max = float('-inf')
#     max_sum = 0
#     for i in range(len(arr)):
#         current_max = max(current_max, current_max + arr[i])        
#         max_sum = max(max_sum, current_max)
#     return max_sum

def kadane_algorithm(arr):
    maxi = float('-inf')
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
        if sum > maxi:
            maxi = sum
        if sum < 0:
          sum = 0
    return maxi
arr = [2, 3, -2, 4, -1, 5, -3]
print(kadane_algorithm(arr))  

# ---------------------------------------------------------------------------------------------------------------------------------------------

# 5 TODO : print subarray with maximum sum (extended version of kadane's algorithm)
# - method 1 : brute force,

# - method 2 : better solution, 

# - method 3 : optimal solution, using Kandane'algo, TC -O(N), SC - (1)
def kadane_algorithm(arr):
    maxi = float('-inf')
    sum = 0
    start = 0
    ansStart, ansEnd = -1, -1
    for i in range(len(arr)):
        if sum == 0:
            start = i
        sum += arr[i]
        if sum > maxi:
            maxi = sum
            ansStart = start
            ansEnd = i
        if sum < 0:
          sum = 0
    for i in range(ansStart, ansEnd + 1):
      print(arr[i], end=" ")
    return maxi
arr = [-2,1,-3,4,-1,2,1,-5,4]
print(kadane_algorithm(arr))

# ---------------------------------------------------------------------------------------------------------------------------------------------

# 6 TODO : stock buy and sell
# - method 1 : brute force, TC -O(N^2), SC - (1)
def buy_sell(arr):
  minimum = arr[0]
  minimum_profit = 
  max_profit = 0
  for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
      if arr[j] > arr[i]:
        max_profit = max(arr[j] - arr[i], profit)
  return max_profit
arr = [7,1,5,3,6,4]
print(buy_sell(arr))

# - method 2 : better solution, 

# - method 3 : optimal solution,TC - O(N), SC - (1)
def buy_sell(arr):
  min_price = float("inf")
  mx_profit = 0
  for i in range(len(arr)):
    min_price = min(min_price, arr[i])
    cost = arr[i] - min_price
    mx_profit = max(mx_profit, cost)
  return max_profit
arr = [7,1,5,3,6,4]
print(buy_sell(arr)) 

# ---------------------------------------------------------------------------------------------------------------------------------------------

# 7 TODO : rearrange the array in alternating positive and negative items
# - method 1 : brute force, TC - O(N + N/2), SC - O(N + N/2)
def rearrange(arr):
  pos,neg = [],[]
  
  for i in arr:
    if i >= 0:
      pos.append(i)
    else:
      neg.append(i)
  result = [0] * len(arr)
  for i in range(len(pos)):
    result[2*i] = pos[i]
  for i in range(len(neg)):
    result[2*i+1] = neg[i]
  # for i in range(len(arr)//2):
  #   result[2*i] = pos[i]
  #   result[2*i+1] = neg[i]
  return result
arr = [3,1,-2,-5,2,-4]
print(rearrange(arr))

# - method 2 : better solution, time complexity O(n)

# - method 3 : optimal solution, TC - O(N), SC - (N)
def rearrange(arr):
  posIndex = 0
  negIndex=1
  res = [0]*len(arr)
  for i in range(len(arr)):
    if arr[i] < 0:
      res[negIndex] = arr[i]
      negIndex += 2 
    else:
      res[posIndex] = arr[i]
      posIndex +=2
  return res
arr = [3,1,-2,-5,2,-4]
print(rearrange(arr))

# ---------------------------------------------------------------------------------------------------------------------------------------------

# 👉👉👉 TODO : rearrange the array in alternating positive and negative items (number of positives and negatives are not equal)
# - method 1 : brute force, 
def rearrange(arr):
    pos, neg, result = [], [], []  
    for i in arr:
        if i >= 0:
            pos.append(i)
        else:
            neg.append(i)
    res = [0] * len(arr)
    if len(pos) > len(neg):
        for i in range(len(neg)):
            res[2 * i] = pos[i]
            res[2 * i + 1] = neg[i]
        posIndex = len(neg) * 2
        for i in range(len(pos) - len(neg)):
            res[posIndex] = pos[len(neg) + i]
            posIndex += 1
    else:
        for i in range(len(pos)):
            res[2 * i] = pos[i]
            res[2 * i + 1] = neg[i]
        negIndex = len(pos) * 2
        for i in range(len(neg) - len(pos)):
            res[negIndex] = neg[len(pos) + i]
            negIndex += 1
    return res
arr = [3, 1, -2, -5, 2, -4, 4, 7]
print(rearrange(arr))


# - method 2 : better solution, 

# - method 3 : optimal solution,

# ---------------------------------------------------------------------------------------------------------------------------------------------


# 8 TODO : next permutation - find the next lexiographically greater permutation 🤯🤯🤯🤯🤯
# - method 1 : brute force, TC - O(N! * N), SC - O(N)
'''
generate all permutations
linear search on that 
get the arrays
'''

# - method 2 : better solution, using built in function



# - method 3 : optimal solution, TC - O(3*N), SC - O(1) 🤯🤯🤯
'''
reference : https://www.takeuforward.org/data-structure/next_permutation-find-next-lexicographically-greater-permutation/
'''
def next_permutation(arr):
    n = len(arr)
    ind = -1

    for i in range(n - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            ind = i
            break
    if ind == -1:
      arr.reverse()
      return arr
    for i in range(n - 1, ind, -1):
        if arr[i] > arr[ind]:
            arr[i], arr[ind] = arr[ind], arr[i]
            break
    arr[ind + 1:] = reversed(arr[ind + 1:])
    return arr
arr = [1,3,2]
print(next_permutation(arr))

# ---------------------------------------------------------------------------------------------------------------------------------------------


# 9 TODO : leaders in array problem (every thing in the right should be smaller)
# - method 1 : brute force, TC - O(N^2), SC - O(N)
def leaders(arr):
  leaders = []
  for i in range(len(arr)):
    leader = True
    for j in range(i+1,len(arr)):
      if arr[j] >arr[i]:
        leader = False
    if leader:
      leaders.append(arr[i])
  return leaders
arr = [10,22, 12,3,0,6]
print(leaders(arr))


# - method 2 : better solution, time complexity O(n)

# - method 3 : optimal solution, TC - (N), SC - (N)
def leaders(arr):
  leaders = []
  maximum = float("-inf")
  for i in range(len(arr)-1, 0, -1):
    if arr[i] > maximum:
      maximum = arr[i]
      leaders.append(arr[i])
  return leaders
arr = [10,22, 12,3,0,6]
print(leaders(arr))

# ---------------------------------------------------------------------------------------------------------------------------------------------


# 10 TODO : largest consecutive sequence in an array
# - method 1 : brute force, TC -O(N^2), SC - O(1)
def linear_search(arr, num):
  for i in range(len(arr)):
    if arr[i] == num:
      return True
  return False
def longest_consecutive_length(arr):
  longest = 1
  for i in range(len(arr)):
    x = arr[i]
    count = 1
    while linear_search(arr, x+1):
      x += 1
      count += 1
    longest_len = max(longest_len, count)
  return longest_len
arr = [100, 4, 200, 1, 3, 2]
print(longest_consecutive_length(arr))
# - method 2 : better solution, using sorting, TC - O(N*log(N)) + O(N), SC - O(1)
def longest_consecutive_length(arr):
  if len(arr) == 0:
    return 0
  arr.sort()
  lastSmaller = float("-inf")
  longest = 1
  count = 0
  for i in range(len(arr)):
    if arr[i] - 1 == lastSmaller:
      count += 1
      lastSmaller = arr[i]
    elif arr[i] != lastSmaller:
      count = 1
      lastSmaller = arr[i]
    longest = max(longest, count)
  return longest
arr = [100, 4, 200, 1, 3, 2]
print(longest_consecutive_length(arr))

# - method 3 : optimal solution, using set(), TC - O(N) + O(2*N) ~ O(3*N), SC - O(N)
def longest_consecutive_length(arr):
    if len(arr) == 0:
        return 0
    num_set = set(arr)  
    longest_len = 0
    for num in arr:
        if num - 1 not in num_set:
            current_num = num
            current_len = 1
            while current_num + 1 in num_set:
                current_num += 1
                current_len += 1
            longest_len = max(longest_len, current_len)
    return longest_len
arr = [100, 4, 200, 1, 3, 2]
print(longest_consecutive_length(arr))

# ---------------------------------------------------------------------------------------------------------------------------------------------


# 11 TODO : set matrix zeros 🤯🤯🤯🤯
# - method 1 : brute force, TC - O((N*M)*(M*N)) +O(N*M), SC - O(1)

def set_zeros(matrix, n,m):
  for i in range(n):
    for j in range(m):
      if matrix[i][j] == 0:
        mark_row(matrix,n,m,i)
        mark_col(matrix,n,m,j)
  for i in range(n):
    for j in range(m):
      if matrix[i][j] == -1:
        matrix[i][j] = 0
  return matrix
  
def mark_col(matrix, n, m, j):
  for i in range(n):
    if arr[i][j] != 0:
      arr[i][j] = -1

def mark_row(matrix, n, m, i):
  for j in range(len(arr)):
    if arr[i][j] != 0:
      arr[i][j] = -1
      
arr = [[1,1,1], [1,0,1], [1,1,1]]
n, m = len(arr), len(arr[0])
for i in set_zeros(arr, n, m) :
  print(i) 


# - method 2 : better solution, TC - O(2*(N*M)), SC - O(N) + O(M)
def set_zeros(matrix, n,m):
  row = [0]*n
  col = [0]*m

  for i in range(n):
    for j in range(m):
      if matrix[i][j] == 0:
        row[i] = 1
        col[j] = 1
  for i in range(n):
    for j in range(m):
      if row[i] or col[j]:
        matrix[i][j] = 0
  return matrix

arr = [[1,1,1], [1,0,1], [1,1,1]]
n, m = len(arr), len(arr[0])
for i in set_zeros(arr, n, m) :
  print(i) 

# - method 3 : optimal solution, TC - O(2*(N*M)), SC - O(1)
def set_zeros(matrix, n,m):
  col0 = 1
  for i in range(n):
    for j in range(m):
      if matrix[i][j] == 0:
        matrix[i][0] = 0
        if j != 0:
          matrix[0][j] = 0
        else:
          col0 = 0
  for i in range(1, n):
    for j in range(1, m):
      if matrix[i][j] != 0:
        if matrix[i][0] == 0 or matrix[0][j] == 0:
          matrix[i][j] = 0
  if matrix[0][0] == 0:
    for j in range(m):
      matrix[0][j] = 0
  if col0 == 0:
    for i in range(n):
      matrix[i][0] = 0
  return matrix

arr = [[1,1,1], [1,0,1], [1,1,1]]
n, m = len(arr), len(arr[0])
for i in set_zeros(arr, n, m) :
  print(i) 

# ---------------------------------------------------------------------------------------------------------------------------------------------


# 12 TODO : rotate matrix by 90 degrees
# - method 1 : brute force, TC - O(N*N), SC - O(N*N)
def rotate_90(matrix, n,m):
  rotated = [[0 for _ in range(n)] for _ in range(m)]
  for i in range(n):
    for j in range(m):
      rotated[j][n-i-1] = matrix[i][j]
  return rotated

arr = [[1,1,1], [1,0,1], [1,1,1]]
n, m = len(arr), len(arr[0])
for i in rotate_90(arr, n, m) :
  print(i) 

# - method 2 : better solution, time complexity O(n)

# - method 3 : optimal solution, TC - O(N*N) + O(N*N), SC - O(1))
def rotate_90(matrix, n,m):
  rotated = [[0 for _ in range(n)] for _ in range(m)]
  for i in range(n):
    for j in range(i):
      rotated[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
  for i in range(n):
    matrix[i].reverse()
  return matrix

arr = [[1,2,3], [4,5,6], [7,8,9]]
n, m = len(arr), len(arr[0])
for i in rotate_90(arr, n, m) :
  print(i) 

# ---------------------------------------------------------------------------------------------------------------------------------------------

# 13 TODO : print the matrix in spiral manner
# - method 1 : brute force, TC - O(N*M), SC - O(N*M)
def rotate_90(matrix, n,m):
  ans = []
  top = 0
  bottom = n-1
  left = 0
  right = m-1
  while top <= bottom and left <= right:
    for i in range(left, right+1):
      ans.append(matrix[top][i])
    top += 1
    for i in range(top, bottom+1):
      ans.append(matrix[i][right])
    right -= 1
    if top <= bottom:
      for i in range(right, left-1, -1):
        ans.append(matrix[bottom][i])
      bottom -= 1
    if left <= right:
      for i in range(bottom, top-1, -1):
        ans.append(matrix[i][left])
      left += 1
    return ans

arr = [[1,2,3], [4,5,6], [7,8,9]]
n, m = len(arr), len(arr[0])
print(rotate_90(arr, n, m))

# - method 2 : better solution, time complexity O(n)

# - method 3 : optimal solution, time complexity O(n)


# ---------------------------------------------------------------------------------------------------------------------------------------------

# 14 TODO : count subarrays with given sum

# - method 1 : brute force, TC - O(N*N*N), SC - O(1)
def find_subarrays(arr, sum):
  count = 0
  for i in range(len(arr)):
    for j in range(i, len(arr)):
      subarray_sum = sum(arr[i:j+1])
      if subarray_sum == sum:
        count += 1
  return count

arr = [3,1,2,4]
sum = 6
print(find_subarrays(arr, sum))

# - method 2 : better solution, TC - O(N*N), SC - O(1)
def find_subarrays(arr, sum):
  count = 0
  for i in range(len(arr)):
    subarray_sum = 0
    for j in range(i, len(arr)):
      subarray_sum += arr[j]
      if subarray_sum == sum:
        count += 1
  return count

arr = [3,1,2,4]
sum = 6
print(find_subarrays(arr, sum))

# - method 3 : optimal solution, TC - O(N) or O(N*log(N)), SC - O(N)
from collections import defaultdict
def find_subarrays(arr, sum):
  n = len(arr)
  mpp = defaultdict(int)
  preSum = 1
  cnt = 0
  mpp[0] = 1
  for i in range(n):
    preSum += arr[i]
    remove = preSum - sum
    cnt += mpp[remove]
    mpp[preSum] += 1
  return cnt

arr = [3,1,2,4]
sum = 6
print(find_subarrays(arr, sum))

# endregion

# region 3.1 ARRAYS - HARD
# ------------------------

# 1 TODO : pascal's triangle

'''
VARIATION 1 : In this case, we are given row number r and column number c, and we need to find the element at position (r, c).
'''
# - method 1 : brute force
'''
formulae, nCr = n! / (r! * (n-r)!)
'''

# - method 2 : better solution, 

# - method 3 : optimal solution, TC - O(c), SC - O(1)
def nCr(n,r):
  res = 1
  for i in range(r):
    res = res * (n-i)
    res = res // (i+1)
  return res
def pascal_triangle(r,c):
  element = nCr(r-1,c-1)
  return element

r,c = 5,3
print(pascal_triangle(r,c))

'''
VARIATION 2 : Given the row number, print the n-th row of Pascal’s triangle.
'''
# - method 1 : brute force, TC - O(n*r), SC - O(1)
def nCr(n,r):
  res = 1
  for i in range(r):
    res = res * (n-i)
    res = res // (i+1)
  return res
def pascal_triangle(n):
  for c in range(1,n+1):
    print(nCr(n-1,c-1), end=" ")
  print()

n = 5
print(pascal_triangle(n))

# - method 2 : better solution, time complexity O(n)

# - method 3 : optimal solution, TC - O(N), SC - O(1)
def pascal_triangle(n):
  ans = 1
  print(ans, end=" ")
  for i in range(1,n):
    ans = ans * (n - 1)
    ans = ans // i
    print(ans, end=" ")

n = 5
print(pascal_triangle(n))

'''
VARIATION 3 : OTHER
'''
# - method 1 : brute force, TC - O(n*n*r) ~O(N*N*N), SC - O(1)
from typing import *
def nCr(n,r):
  res = 1
  for i in range(r):
    res = res * (n-i)
    res = res // (i+1)
  return int(res)
def pascal_triangle(n):
  ans =[]
  for row in range(1,n+1):
    tempList = []
    for col in range(1,row+1):
      tempList.append(nCr(row-1,col-1))
    ans.append(tempList)
  return ans

n = 5
print(pascal_triangle(n))

# - method 2 : better solution, time complexity O(n)

# - method 3 : optimal solution, TC - O(N*N), SC - O(1)
from typing import *
def generateRow(row):
  ans = 1
  ansRow = [1]
  for col in range(1, row):
    ans = ans * (row - col)
    ans = ans // col
    ansRow.append(ans)
  return ansRow
def pascal_triangle(n):
  ans =[]
  for row in range(1,n+1):
    ans.append(generateRow(row))
  return ans

n = 5
print(pascal_triangle(n))

# ---------------------------------------------------------------------------------------------------------------------------------------------

# 2 TODO : majority element (>n/3 times)

# - method 1 : brute force, TC -O(N*N), SC - O(1)
def majority_element(arr):
  n = len(arr)
  ls = []
  for i in range(n):
    if len(ls) == 0 or ls[0] != arr[i]:
      cnt = 0
      for j in range(n):
        if arr[i] == arr[j]:
          cnt += 1
      if cnt > (n//3):
        ls.append(arr[i])
    if len(ls) == 2:
      break
  return ls

arr = [1,3,3,1,3,1]
print(majority_element(arr))

# - method 2 : better solution, using hashing, TC - O(N*log(N)), SC - O(N)
from collections import Counter
def majority_element(arr):
  n = len(arr)
  counter = Counter(arr)
  for num,count in counter.items():
    if count > (n//3):
      return num
  return -1

arr = [1,3,3,1,3,1]
print(majority_element(arr))

# - method 3 : optimal solution, using Boyer Moore's majority voting algorithm, TC - O(N) + O(N), SC - O(1)
from collections import Counter
def majority_element(arr):
  n = len(arr)
  cnt1,cnt2 = 0,0
  el1,el2 = float('-inf'),float('-inf')
  for i in range(n):
    if cnt1 == 0 and el2 != arr[i]:
      cnt1 = 1
      el1 = arr[i]
    elif cnt2 == 0 and el1 != arr[i]:
      cnt2 = 1
      el2 = arr[i]
    elif arr[i] == el1:
      cnt1 += 1
    elif arr[i] == el2:
      cnt2 += 1
    else:
      cnt1 -= 1
      cnt2 -= 1

  ls = []
  cnt1,cnt2 = 0,0
  for i in range(n):
    if arr[i] == el1:
      cnt1 += 1
    if arr[i] == el2:
      cnt2 += 1
  mini = int(n/3) + 1
  if cnt1 >= mini:
    ls.append(el1)
  if cnt2 >= mini:
    ls.append(el2)
  return ls

arr = [1,3,3,1,3,1]
print(majority_element(arr))

# ---------------------------------------------------------------------------------------------------------------------------------------------


# 3 TODO : 3-sum problem - find triplets that add up to a zero
# - method 1 : brute force, TC - O(N*N*N*log(nos of unique triplets)), SC - O(2*nos of unique triplets)
def triplet(n, arr):
  st = set()
  for i in range(n):
    for j in range(i+1,n):
      for k in range(j+1,n):      
        sum = arr[i] + arr[j] + arr[k]
        if sum == 0:
          temp = [arr[i],arr[j],arr[k]]
          temp.sort()
          st.add(tuple(temp))
  ans = [list(item) for item in st]
  return ans

arr = [-1,0,1,2,-1,-4]
n = len(arr)
print(triplet(n, arr))

# - method 2 : better solution, using hashing,  TC - O(N*N*log(nos of unique triplets)), SC - O(2*nos of unique triplets)
def triplet(n, arr):
  st = set()
  for i in range(n):
    hashset = set()
    for j in range(i+1,n):
      third = -(arr[i] + arr[j])
      if third in hashset:
        temp = [arr[i],arr[j],third]
        temp.sort()
        st.add(tuple(temp))
      hashset.add(arr[j])
  ans = list(st)
  return ans

arr = [-1,0,1,2,-1,-4]
n = len(arr)
print(triplet(n, arr))

# - method 3 : optimal solution, TC - O(N*log(N)) + O(N*N), SC - O(nos of triplets)
def triplet(n, arr):
  # st = set()
  ans = []
  arr.sort()
  for i in range(n):
    if i != 0 and arr[i] == arr[i-1]:
      continue

    j = i+1
    k = n-1
    while j < k:
      sum = arr[i] + arr[j] + arr[k]
      if sum < 0:
        j += 1
      elif sum > 0:
        k -= 1
      else:
        temp = [arr[i],arr[j],arr[k]]
        ans.append(temp)
        j += 1
        k -= 1
        while j < k and arr[j] == arr[j-1]:
          j += 1
        while j < k and arr[k] == arr[k+1]:
          k -= 1
  return ans

arr = [-1,0,1,2,-1,-4]
n = len(arr)
print(triplet(n, arr))

# ---------------------------------------------------------------------------------------------------------------------------------------------


# 4 TODO : 4-sum problem
# - method 1 : brute force, TC - O(N*N*N*N), SC - O(2*nos of quadruplets)
from collections import deque
def fourSum(nums, target):
  n = len(nums)
  st = set()
  for i in range(n):
    for j in range(i+1,n):
      for k in range(j+1,n):
        for l in range(k+1,n):
          sum = num[i] + sum[j] + sum[k] + sum[l]
          if sum == target:
            temp = [num[i],num[j],num[k],num[l]]
            temp.sort()
            st.add(tuple(temp))
  ans = [list(item) for item in st]
  return ans

arr = [4,3,3,4,4,2,1,2,1,1]
target = 9
print(fourSum(arr, target))

# - method 2 : better solution, using hashing,  TC - O(N*N*log(nos of unique triplets)), SC - O(2*nos of unique triplets) + O(N)
import itertools
def fourSum(nums, target):
  n = len(nums)
  st = set()
  for i in range(n):
    for j in range(i+1,n):
      hashset = set()
      for k in range(j+1,n):
        sum_ = nums[i] + nums[j] + nums[k]
        fourth = target - sum_
        if fourth in hashset:
          temp = [nums[i],nums[j],nums[k],fourth]
          temp.sort()
          st.add(tuple(temp))
        hashset.add(nums[k])
  ans = [list(item) for item in st]
  return ans

arr = [4,3,3,4,4,2,1,2,1,1]
target = 9
print(fourSum(arr, target))

# - method 3 : optimal solution, TC - O(N*N*N), SC - O(nos of quadruplets)
def fourSum(nums, target):
  n = len(nums)
  ans = []
  nums.sort()
  for i in range(n):
    if i > 0 and nums[i] == nums[i-1]:
      continue
    for j in range(i+1,n):
      if j > i+1 and nums[j] == nums[j-1]:
        continue
      k = j+1
      l = n-1
      while k < l:
        _sum = nums[i] + nums[j] + nums[k] + nums[l]
        if _sum < target:
          k += 1
        elif _sum > target:
          l -= 1
        else:
          temp = [nums[i],nums[j],nums[k],nums[l]]
          ans.append(temp)
          k += 1
          l -= 1
          while k < l and nums[k] == nums[k-1]:
            k += 1
          while k < l and nums[l] == nums[l+1]:
            l -= 1
  return ans

arr = [4,3,3,4,4,2,1,2,1,1]
target = 9
print(fourSum(arr, target))

# ---------------------------------------------------------------------------------------------------------------------------------------------


# 5 TODO : largest subarray with 0 sum
# - method 1 : brute force, TC - O(n^2), SC - O(1)
def solve(arr):
  n = len(arr)
  maxi = 0
  for i in range(n):
    sum = 0
    for j in range(i,n):
      sum += arr[j]
      if sum == 0:
        maxi = max(maxi, j-i+1)
  return maxi
arr = [9,-3,3,-1,6,-5]
print(solve(arr))

# - method 2 : better solution, time complexity O(n)

# - method 3 : optimal solution, using hashmap,  TC - O(n), SC - O(n)
def solve(arr):
  mpp = {}
  sum = 0
  maxi = 0
  for i in range(len(arr)):
    sum += arr[i]
    if sum == 0:
      maxi =  i+1
    else:
      if sum in mpp:
        maxi = max(maxi, i-mpp[sum])
      else:
        mpp[sum] = i
  return maxi
arr = [9,-3,3,-1,6,-5]
print(solve(arr))

# ---------------------------------------------------------------------------------------------------------------------------------------------


# 6 TODO : count number of subarrays with given xor k
# - method 1 : brute force, TC - O(n^3), SC - O(1)
def subarray(a,b):
  n = len(a)
  cnt = 0
  for i in range(n):
    for j in range(i,n):
      xor = 0
      for k in range(i,j+1):
        xor = xor ^ a[k]
      if xor == b:
        cnt += 1
  return cnt

a = [4,2,2,6,4]
k = 6
print(subarray(a,k))

# - method 2 : better solution, TC - O(n^2), SC - O(1)
def subarray(a,b):
  n = len(a)
  cnt = 0
  for i in range(n):
    xor = 0
    for j in range(i,n):
      xor = xor ^ a[j]
      if xor == b:
        cnt += 1
  return cnt

a = [4,2,2,6,4]
k = 6
print(subarray(a,k))

# - method 3 : optimal solution, using hashing, TC - O(n*log(n)), SC - O(N)
from collections import defaultdict
def subarray(a,b):
  n = len(a)
  xr = 0
  mpp = defaultdict(int)
  mpp[xr] = 1
  cnt = 0
  for i in range(n):
    xr = xr ^ a[i]
    x = xr ^ b
    cnt += mpp[x]
    mpp[xr] += 1
  return cnt

a = [4,2,2,6,4]
k = 6
print(subarray(a,k))

# ---------------------------------------------------------------------------------------------------------------------------------------------

# 7 TODO : merge overlapping subintervals
# - method 1 : brute force, TC - O(nlogn)+O(2n), SC - O(n)
def merge(arr):
  n = len(arr)
  arr.sort()
  ans = []
  for i in range(n):
    start, end = arr[i][0], arr[i][1]
    if ans and start <= ans[-1][1]:
      continue
    for j in range(i+1,n):
      if arr[j][0] <= end:
        end = max(end, arr[j][1])
      else:
        break
    ans.append(start, end)
  return ans

arr = [[1,3],[2,6],[8,10],[15,18]]
print(merge(arr))

# - method 2 : better solution, time complexity O(n)

# - method 3 : optimal solution, TC - O(nlogn)+O(n), SC - O(n)
def merge(arr):
  n = len(arr)
  arr.sort()
  ans = []
  for i in range(n):
    if not ans or arr[i][0] > ans[-1][1]:
      ans.append(arr[i])
    else:
      ans[-1][1] = max(ans[-1][1], arr[i][1])
  return ans

arr = [[1,3],[2,6],[8,10],[15,18]]
print(merge(arr))

# ---------------------------------------------------------------------------------------------------------------------------------------------

# 8 TODO : merge two sorted arrays without extra space
# - method 1 : brute force, TC - O(n+m) + O(n+m), SC - O(n+m)
def merge(arr1, arr2):
  n = len(arr1)
  m = len(arr2)
  arr3 = [] * (n + m)
  left = 0
  right = 0
  index = 0
  while left < n and right < m:
    if arr1[left] <= arr2[right]:
      arr3[index] = arr1[left]
      left += 1
      index += 1
    else: 
      arr3[index] = arr2[right]
      right += 1
      index += 1
  while left < n:
    arr3[index] = arr1[left]
    left += 1
    index += 1
  while right < m:
    arr3[index] = arr2[right]
    right += 1
    index += 1
  for i in range(n+m):
    if i < n:
      arr1[i] = arr3[i]
    else:
      arr2[i-n] = arr3[i]
  return arr3
arr1 = [1,4,8,10]
arr2 = [2,3,9]
print(merge(arr1, arr2))

# - method 2 : better solution, time complexity O(n)

# - method 3 : optimal solution, TC - O(min(n,m)) + O(nlogn), SC - O(1)
def merge(arr1, arr2):
  n = len(arr1)
  m = len(arr2)
  left = n -1
  right = 0
  while left >= 0 and right < m:
    if arr1[left] > arr2[right]:
      arr1[left], arr2[right] = arr2[right], arr1[left]
      left -= 1
      right += 1
    else:
      break
  arr1.sort()
  arr2.sort()
  return arr1 + arr2

arr1 = [1,4,8,10]
arr2 = [2,3,9]
print(merge(arr1, arr2))

# - method 4 : optimal solution, using gap method, TC - O((n+m)*log(n+m)), SC - O(1)
def swapIfGreater(arr1, arr2, ind1, ind2):
    if arr1[ind1] > arr2[ind2]:
        arr1[ind1], arr2[ind2] = arr2[ind2], arr1[ind1]

def merge(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    max_len = n + m
    gap = (max_len // 2) + (max_len % 2)
    while gap > 0:
        left = 0
        right = left + gap
        while right < max_len:
            if left < n and right >= n:  
                swapIfGreater(arr1, arr2, left, right - n)
            elif left >= n:  
                swapIfGreater(arr2, arr2, left - n, right - n)
            else: 
                swapIfGreater(arr1, arr1, left, right)
            left += 1
            right += 1
        if gap == 1:
            break
        gap = (gap // 2) + (gap % 2)
    return arr1 + arr2

arr1 = [1, 4, 8, 10]
arr2 = [2, 3, 9]
print(merge(arr1, arr2))

# ---------------------------------------------------------------------------------------------------------------------------------------------

# 9 TODO : find the repeating and missing number
# - method 1 : brute force, TC - O(n^2), SC - O(1)
def solve(a):
  n = len(a)
  rep, mis = -1, -1
  for i in range(1,n+1):
    cnt = 0
    for j in range(n):
      if a[j] == i:
        cnt += 1
    if cnt == 2:
      rep = i
    elif cnt == 0:
      mis = i
    if rep != -1 and mis != -1:
      break
  return rep, mis

a = [3,1,2,5,4,6,7,5]
print(solve(a))

# - method 2 : better solution, using hashing, TC - O(2N), SC - O(N)
def solve(a):
  n = len(a)
  hash = [0] * (n+1)
  for i in range(n):
    hash[a[i]] += 1
  rep, mis = -1, -1
  for i in range(1,n+1):
    if hash[i] == 2:
      rep = i
    elif hash[i] == 0:
      mis = i
    if rep != -1 and mis != -1:
      break
  return rep, mis

a = [3,1,2,5,4,6,7,5]
print(solve(a))


# - method 3 : optimal solution, using maths, TC - O(N), SC - O(1)
def solve(a):
  n = len(a)
  sn = (n * (n+1)) // 2
  s2n = (n * (n+1) * (2*n+1)) // 6
  s, s2 = 0, 0
  for i in range(n):
    s += a[i]
    s2 += a[i] * a[i]
  val1 = s - sn
  val2 = s2 - s2n
  val2 = val2 // val1
  mis = (val1 + val2) // 2
  rep = mis - val1
  return rep, mis

a = [3,1,2,5,4,6,7,5]
print(solve(a))

# - method 3 : optimal solution, using xor, TC - O(N), SC - O(1) ❌❌❌❌
# def solve(a):
#   n = len(a)
#   xr = 0
#   for i in range(n):
#     xr = xr ^ a[i]
#     xr = xr ^ (i+1)
#   number = xr & ~(xr-1)
#   zero = 0
#   one = 0
#   for i in range(n):
#     if a[i] & number != 0:
#       one = one ^ a[i]
#     else:
#       zero = zero ^ a[i]
#   for i in range(1, n+1):
#     if (i & number) != 0:
#       one = one ^ i
#     else:
#       zero = zero ^ i
#   cnt = 0
#   for i in range(n):
#     if a[i] == zero:
#       cnt += 1
#   if cnt == 2:
#     return one, zero

# a = [3,1,2,5,4,6,7,5]
# print(solve(a))


# ---------------------------------------------------------------------------------------------------------------------------------------------

# 10 TODO : count inversions
# - method 1 : brute force, TC - O O(n^2), SC - O(1)
def solve(a, n):
  cnt = 0
  for i in range(n):
    for j in range(i+1, n):
      if a[i] > a[j]:
        cnt += 1
  return cnt

a = [5,4,3,2,1]
print(solve(a, len(a)))

# - method 2 : better solution, time complexity O(n)

# - method 3 : optimal solution, time complexity O(n)

# ---------------------------------------------------------------------------------------------------------------------------------------------

# 11 TODO : reverse pairs
# - method 1 : brute force, time complexity O(nlogn)

# - method 2 : better solution, time complexity O(n)

# - method 3 : optimal solution, time complexity O(n)

# ---------------------------------------------------------------------------------------------------------------------------------------------

# 12 TODO : maximum product subarray
# - method 1 : brute force, time complexity O(nlogn)

# - method 2 : better solution, time complexity O(n)

# - method 3 : optimal solution, time complexity O(n)

# endregion


# region 4.1 BINARY SEARCH on 1D ARRAY
# ------------------------------------

# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 
# 5 TODO : 
# 6 TODO : 
# 7 TODO : 
# 8 TODO : 
# 9 TODO : 
# 10 TODO :  
# 11 TODO : 
# 12 TODO : 
# 13 TODO : 


# endregion




# region 4.2 BINARY SEARCH on ANSWERS
# -----------------------------------


# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 
# 5 TODO : 
# 6 TODO : 
# 7 TODO : 
# 8 TODO : 
# 9 TODO : 
# 10 TODO :  
# 11 TODO : 
# 12 TODO : 
# 13 TODO : 
# 14 TODO : 

# endregion






# region 4.3 BINARY SEARCH on 2D ARRAY
# ------------------------------------

# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 
# 5 TODO : 


# endregion


# region 5.1 STRINGS - EASY
# -------------------------

# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 
# 5 TODO : 
# 6 TODO : 
# 7 TODO : 



# endregion

# region 5.2 STRINGS - MEDIUM
# ---------------------------

# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 
# 5 TODO : 
# 6 TODO : 
# 7 TODO : 
# 8 TODO : 


# endregion







# region 6.1 LINKED LIST - 1D EASY
# --------------------------

# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 
# 5 TODO : 

# endregion



# region 6.2 LINKED LIST - DOUBLY  EASY
# -------------------------------------
# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 



# endregion


# region 6.3 LINKED LIST - MEDIUM
# --------------------------------

# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 
# 5 TODO : 
# 6 TODO : 
# 7 TODO : 
# 8 TODO : 
# 9 TODO : 
# 10 TODO :  
# 11 TODO : 
# 12 TODO : 
# 13 TODO : 
# 14 TODO : 
# 15 TODO :

# endregion


# region 6.4 LINKED LIST - DOUBLY MEDIUM
# --------------------------------------

# 1 TODO :  
# 2 TODO : 
# 3 TODO : 



# endregion

# region 6.5 LINKED LIST - HARD
# -----------------------------

# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 

# endregion



# region 7.1 RECURSION - BASIC
# ----------------------------

# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 
# 5 TODO : 


# endregion


# region 7.2 RECURSION - PATTERN
# ------------------------------

# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 
# 5 TODO : 
# 6 TODO : 
# 7 TODO : 
# 8 TODO : 
# 9 TODO : 
# 10 TODO :  
# 11 TODO : 
# 12 TODO : 

# endregion


# region 7.3 RECUSION - HARD
# --------------------------

# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 
# 5 TODO : 
# 6 TODO : 
# 7 TODO : 
# 8 TODO : 

# endregion



# region 8.1 BIT MANIPULATION - BASIC
# -----------------------------------

# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 
# 5 TODO : 
# 6 TODO : 
# 7 TODO : 
# 8 TODO : 

# endregion



# region 8.2 BIT MANIPULATION - MEDIUM
# ------------------------------------

# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 
# 5 TODO : 


# endregion



# region 8.3 BIT MANIPULATION - HARD
# ----------------------------------

# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 
# 5 TODO : 


# endregion




# region 9.1 STACK/QUEUE - LEARNING
# ---------------------------------

# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 
# 5 TODO : 
# 6 TODO : 
# 7 TODO : 
# 8 TODO : 


# endregion



# region 9.2 STACK/QUEUE - PREFIX/POSTFIX
# ---------------------------------------

# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 
# 5 TODO : 
# 6 TODO : 


# endregion


# region 9.3 STACK/QUEUE - MONOTONIC
# ----------------------------------

# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 
# 5 TODO : 
# 6 TODO : 
# 7 TODO : 
# 8 TODO : 
# 9 TODO : 
# 10 TODO :  
# 11 TODO : 


# endregion



# region 9.4 STACK/QUEUE - IMPLEMENTATION
# ---------------------------------------

# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 
# 5 TODO : 



# endregion




# region 10.1 SLIDING WINDOW/TWO POINTER - MEDIUM
# -----------------------------------------------

# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 
# 5 TODO : 
# 6 TODO : 
# 7 TODO : 
# 8 TODO : 


# endregion




# region 10.2 SLIDING WINDOW/TWO POINTER - HARD
# ---------------------------------------------

# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 


# endregion




# region 11.1 HEAP/PRIORITY QUEUE - LEARNING
# ------------------------------------------

# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 


# endregion




# region 11.2 HEAP/PRIORITY QUEUE - MEDIUM
# ----------------------------------------

# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 
# 5 TODO : 
# 6 TODO : 
# 7 TODO : 



# endregion


# region 11.3 HEAP/PRIORITY QUEUE - HARD
# --------------------------------------

# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 
# 5 TODO : 
# 6 TODO : 


# endregion


# region 12.1 GREEDY ALGORITHM - EASY
# -----------------------------------

# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 
# 5 TODO : 


# endregion



# region 12.2 GREEDY ALGORITHM - MEDIUM/HARD
# ------------------------------------------

# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 
# 5 TODO : 
# 6 TODO : 
# 7 TODO : 
# 8 TODO : 
# 9 TODO : 
# 10 TODO :  
# 11 TODO : 


# endregion


# region 13.1 BINARY TREES - TRAVERSALS
# -------------------------------------

# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 
# 5 TODO : 
# 6 TODO : 
# 7 TODO : 
# 8 TODO : 
# 9 TODO : 
# 10 TODO :  
# 11 TODO : 
# 12 TODO : 
# 13 TODO : 



# endregion



# region 13.2 BINARY TREES - MEDIUM
# ----------------------------------

# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 
# 5 TODO : 
# 6 TODO : 
# 7 TODO : 
# 8 TODO : 
# 9 TODO : 
# 10 TODO :  
# 11 TODO : 
# 12 TODO : 


# endregion



# region 13.3 BINARY TREES - HARD
# --------------------------------


# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 
# 5 TODO : 
# 6 TODO : 
# 7 TODO : 
# 8 TODO : 
# 9 TODO : 
# 10 TODO :  
# 11 TODO : 
# 12 TODO : 
# 13 TODO : 
# 14 TODO : 

# endregion



# region 14.1 BINARY SEARCH TREES - CONCEPTS
# ------------------------------------------

# 1 TODO :  
# 2 TODO : 
# 3 TODO : 


# endregion




# region 14.2 BINARY SEARCH TREES - PRACTICE PROBLEMS
# ---------------------------------------------------

# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 
# 5 TODO : 
# 6 TODO : 
# 7 TODO : 
# 8 TODO : 
# 9 TODO : 
# 10 TODO :  
# 11 TODO : 
# 12 TODO : 
# 13 TODO : 


# endregion



# region 15.1 GRAPHS - LEARNING
# -----------------------------

# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 
# 5 TODO : 
# 6 TODO : 


# endregion



# region 15.2 GRAPHS - BFS/DFS
# ----------------------------
# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 
# 5 TODO : 
# 6 TODO : 
# 7 TODO : 
# 8 TODO : 
# 9 TODO : 
# 10 TODO :  
# 11 TODO : 
# 12 TODO : 
# 13 TODO : 
# 14 TODO : 


# endregion



# region 15.3 GRAPHS - TOPO SORT
# ------------------------------

# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 
# 5 TODO : 
# 6 TODO : 
# 7 TODO : 


# endregion


# region 15.4 GRAPHS - SORTEST PATH
# ---------------------------------

# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 
# 5 TODO : 
# 6 TODO : 
# 7 TODO : 
# 8 TODO : 
# 9 TODO : 
# 10 TODO :  
# 11 TODO : 
# 12 TODO : 
# 13 TODO : 


# endregion


# region 15.5 GRAPHS - MST/DISJOINT SET
# -------------------------------------

# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 
# 5 TODO : 
# 6 TODO : 
# 7 TODO : 
# 8 TODO : 
# 9 TODO : 
# 10 TODO :  
# 11 TODO : 


# endregion


# region 15.6 GRAPHS - OTHER ALGORITHMS
# -------------------------------------

# 1 TODO :  
# 2 TODO : 
# 3 TODO : 


# endregion



# region 16.1 DP - INTRODUCTION
# -----------------------------

# 1 TODO :  


# endregion


# region 16.2 DP - 1D
# -------------------
# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 
# 5 TODO : 



# endregion

# region 16.3 DP - 2D/3D/GRIDS
# ----------------------------
# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 
# 5 TODO : 
# 6 TODO : 
# 7 TODO : 



# endregion

# region 16.4 DP - SUBSEQUENCES
# -----------------------------

# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 
# 5 TODO : 
# 6 TODO : 
# 7 TODO : 
# 8 TODO : 
# 9 TODO : 
# 10 TODO :  
# 11 TODO : 


# endregion


# region 16.5 DP - STRINGS
# ------------------------

# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 
# 5 TODO : 
# 6 TODO : 
# 7 TODO : 
# 8 TODO : 
# 9 TODO : 
# 10 TODO :  



# endregion


# region 16.6 DP - STOCKS
# -----------------------

# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 
# 5 TODO : 
# 6 TODO : 


# endregion


# region 16.7 DP - LIS
# --------------------

# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 
# 5 TODO : 
# 6 TODO : 
# 7 TODO : 


# endregion



# region 16.8 DP - MCM/PARTITION
# ------------------------------

# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 
# 5 TODO : 
# 6 TODO : 
# 7 TODO : 


# endregion



# region 16.9 DP - SQUARES
# ------------------------

# 1 TODO :  
# 2 TODO : 



# endregion


# region 17.1 TRIES - THEORY
# --------------------------

# 1 TODO :  


# endregion


# region 17.2 TRIES - PRACTICE PROBLEMS
# -------------------------------------

# 1 TODO :  
# 2 TODO : 
# 3 TODO : 
# 4 TODO : 
# 5 TODO : 
# 6 TODO : 


# endregion


# region 18.1 STRINGS - HARD
# --------------------------

# 1 TODO :  


# endregion

