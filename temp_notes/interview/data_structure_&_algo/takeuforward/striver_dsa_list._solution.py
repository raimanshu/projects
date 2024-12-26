


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

# - method 3 : optimal solution, TC - O(N*log(N)), SC - O(N)
import math 
def solve(a, n):
  return merge_sort(a, 0, n-1)

def merge_sort(a, low, high):
  cnt = 0
  if low >= high:
    return cnt
  mid = (low + high) // 2
  cnt += merge_sort(a, low, mid)
  cnt += merge_sort(a, mid+1, high)
  cnt += merge(a, low, mid, high)
  return cnt

def merge(a, low, mid, high):
  cnt = 0
  temp = []
  left = low
  right = mid+1
  while left <= mid and right <= high:
    if a[left] <= a[right]:
      temp.append(a[left])
      left += 1
    else:
      temp.append(a[right])
      cnt += (mid - left + 1)
      right += 1
  while left <= mid:
    temp.append(a[left])
    left += 1
  while right <= high:
    temp.append(a[right])
    right += 1
  for i in range(low, high+1):
    a[i] = temp[i - low]
  return cnt

a = [5,4,3,2,1]
print(solve(a, len(a)))



# ---------------------------------------------------------------------------------------------------------------------------------------------

# 11 TODO : reverse pairs
# - method 1 : brute force, TC - O(N^2), SC - O(1)
def team(skill, n):
  return countPairs(skill, n)
def countPairs(a, n):
  cnt = 0
  for i in range(n):
    for j in range(i+1, n):
      if a[i] > 2 * a[j]:
        cnt += 1
  return cnt

a = [4,1,2,3,1]
n  =  5
print(team(a, n))
# - method 2 : better solution, time complexity O(n)

# - method 3 : optimal solution, TC - O(2N*log(N)), SC - O(N) ❌❌❌
# def team(skill, n):
#   return merge_sort(skill, 0, n-1)

# def merge_sort(a, low, high):
#   cnt = 0
#   if low >= high:
#     return cnt
#   mid = (low + high) // 2
#   cnt += merge_sort(a, low, mid)
#   cnt += merge_sort(a, mid+1, high)
#   cnt += countPairs(a, low, mid, high)
#   cnt += merge(a, low, mid, high)
#   return cnt

# def countPairs(arr, low, mid, high):
#   right = mid+1
#   cnt = 0
#   for i in range(low, mid+1):
#     while right <= high and a[i] > 2 * a[right]:
#       right += 1
#     cnt += (right - (mid+1))
#   return cnt

# def merge(a, low, mid, high):
#   temp = []
#   left = low
#   right = mid+1
#   while left <= mid and right <= high:
#     if a[left] <= a[right]:
#       temp.append(a[left])
#       left += 1
#     else:
#       temp.append(a[right])
#       cnt += (mid - left + 1)
#       right += 1
#   while left <= mid:
#     temp.append(a[left])
#     left += 1
#   while right <= high:
#     temp.append(a[right])
#     right += 1
#   for i in range(low, high+1):
#     a[i] = temp[i - low]
#   return cnt

# a = [4,1,2,3,1]
# n  =  5
# print(team(a, n))

# ---------------------------------------------------------------------------------------------------------------------------------------------

# 12 TODO : maximum product subarray
# - method 1 : brute force, TC - time complexity O(n^2), SC - O(1)
def maxProduct(nums):
  n = len(nums)
  result = float('-inf')
  for i in range(n-1):
    for j in range(i+1, n):
      prod = 1
      for k in range(i, j+1):
        prod *= nums[k]
      result = max(result, prod)
  return result
nums = [1,2,-3,0,-4,-5]
print(maxProduct(nums))

# - method 2 : better solution, TC - time complexity O(n^2), SC - O(1)
def maxProduct(nums):
  result = nums[0]
  for i in range(len(nums) - 1):
    p = nums[i]
    for j in range(i+1, len(nums)):
      result = max(result, p)
      p *= nums[j]
    result = max(result, p)
  return result
nums = [1,2,-3,0,-4,-5]
print(maxProduct(nums))


# - method 3 : optimal solution, TC - O(N), SC - O(1)
def maxProduct(arr):
  n = len(arr)
  pre, suff = 1,1
  ans = float('-inf')
  for i in range(n):
    if pre == 0:
      pre = 1
    if suff == 0:
      suff = 1
    pre *= arr[i]
    suff *= arr[n-i-1]
    ans = max(ans, max(pre, suff))
  return ans
nums = [1,2,-3,0,-4,-5]
print(maxProduct(nums))

# - method 4 : optimal solution, TC - O(N), SC - O(1)
def maxProduct(nums):
  prod1 = nums[0]
  prod2 = nums[0]
  result = nums[0]
  for i in range(1, len(nums)):
    temp = max(nums[i], nums[i]*prod1, nums[i]*prod2)
    prod2 = min(nums[i], nums[i]*prod1, nums[i]*prod2)
    prod1 = temp
    result = max(result, prod1)
  return result
nums = [1,2,-3,0,-4,-5]
print(maxProduct(nums))

# endregion





# region 4.1 BINARY SEARCH on 1D ARRAY
# ------------------------------------

# 1 TODO : binary search to find x in the sorted array 
# method 1 : iterative approch, TC - o(log(N)) , SC -
def binarySearch(a, target):
  low = 0
  high = len(a) - 1
  while low <= high:
    mid = (low + high) // 2
    if a[mid] == target:
      return mid
    elif a[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
  return low

a = [3,4,6,7,9,12,16,17]
target  = 6
print(binarySearch(a, target))

# method 2 : recursive approch, TC - O(log(N)) , SC -
def binarySearch(nums, low, high, target):
  if low > high:
    return -1
  
  mid = (low + high) // 2
  if nums[mid] == target:
    return mid
  elif target > nums[mid]:
    return binarySearch(nums, mid+1, high, target)
  return binarySearch(nums, low,mid-1, target)

def search(nums, target):
  return binarySearch(nums, 0, len(nums) - 1, target)

a = [3,4,6,7,9,12,16,17]
target  = 6
print(search(a, target))


# method 3 : optimal solution, TC - , SC - 



# 2 TODO : implement lower bound
# method 1 : brute force approch, TC - O(N) , SC - O(1)
def lowerBound(arr, n, x):
  for i in range(n):
    if arr[i] >= x:
      return i
  return n

a = [3,5,8, 15, 19]
n = 5
x = 9
print(lowerBound(a, n, x))


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - O(log(N)), SC - O(1)
def lowerBound(arr, n, x):
  low = 0
  high = n - 1
  ans = n
  while low <= high:
    mid = (low + high) // 2
    if arr[mid] >= x:
      ans = mid
      high = mid - 1
    else:
      low = mid + 1
  return ans

a = [3,5,8, 15, 19]
n = 5
x = 9
print(lowerBound(a, n, x))


# 3 TODO : implement upper bound
def upperBound(arr, x, n):
  for i in range(n):
    if arr[i] > x:
      return i
  return n

a = [3,5,8, 9, 15, 19]
n = 6
x = 9
print(upperBound(a, x, n))


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - O(log(N)), SC - O(1)
def upperBound(arr, x, n):
  low = 0
  high = n - 1
  ans = n
  while low <= high:
    mid = (low + high) // 2
    if arr[mid] > x:
      ans = mid
      high = mid - 1
    else:
      low = mid + 1
  return ans

a = [3,5,8, 9, 15, 19]
n = 6
x = 9
print(upperBound(a, x, n))



# 4 TODO : search insert position
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - O(log(N)), SC - O(1) 
def searchInsert(arr, x):
  n = len(arr)
  low = 0
  high = n - 1
  ans = n
  while low <= high:
    mid = (low + high) // 2
    if arr[mid] >= x:
      ans = mid
      high = mid - 1
    else:
      low = mid + 1
  return ans

arr = [1,2,4,7]
x  = 6
print(searchInsert(arr, x))



# 5 TODO : floor / ceil in sorted array
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 
def findFloor(arr, n, x):
  low = 0
  high = n - 1
  ans = -1
  while low <= high:
    mid = (low + high) // 2
    if arr[mid] <= x:
      ans = arr[mid]
      low = mid + 1
    else:
      high = mid - 1
  return ans

def findCeil(arr, n, x):
  low = 0
  high = n - 1
  ans = -1
  while low <= high:
    mid = (low + high) // 2
    if arr[mid] >= x:
      ans = arr[mid]
      high = mid - 1
    else:
      low = mid + 1
  return ans

def getFloorAndCeil(arr, n, x):
  f = findFloor(arr, n, x)
  c = findCeil(arr, n, x)
  return [f, c]


arr = [3, 4,4,7,8,10]
n = 6
x = 5
print(getFloorAndCeil(arr, n, x))



# 6 TODO : find the first or last occurence of a givennumber in sorted array
# method 1 : brute force approch, TC - O(n), SC - O(1)
def count(n, k, x):
  cnt = -1
  for i in range(k):
    if arr[i] == x:
      cnt = i
  return cnt

arr = [3,4,13,13,13,20,40]
n = 7
x = 13
print(count(arr, n, x))


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - O(log(N)), SC - O(N) 
def count(n, k, x):
  start = 0
  end = k - 1 
  res = -1
  while start <= end:
    mid = start + (end - start) // 2
    if arr[mid] == x:
      res = mid
      start = mid + 1
    elif arr[mid] < x:
      start = mid + 1
    else:
      end = mid - 1
  return res

arr = [3,4,13,13,13,20,40]
n = 7
x = 13
print(count(arr, n, x))


# 7 TODO : count occurence of a number in a sorted array with duplicates
# method 1 : brute force approch, TC - O(N), SC - O(1)

def count(arr, n, x):
  cnt = 0
  for i in range(n):
    if arr[i] == x:
      cnt += 1
  return cnt

arr = [2,4,6,8,8,8,11,13]
n = 8 
x = 8
print(count(arr, n, x))


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - O(2*log(N)) , SC - O(1)
def firstOccurance(arr, n, k):
  low = 0
  high = n -1
  first = -1
  while low <= high:
    mid = (low + high) // 2
    if arr[mid] == k:
      first = mid
      high = mid - 1
    elif arr[mid] < k:
      low = mid + 1
    else:
      high = mid - 1
  return first
def lastOccurance(arr, n, k):
  low = 0
  high = n -1
  last = -1
  while low <= high:
    mid = (low + high) // 2
    if  arr[mid] == k:
      last = mid
      low  = mid + 1
    elif arr[mid] < k:
      low = mid + 1
    else:
      high = mid - 1
  return last

def firstAndLastPosition(arr, n, x):
  first = firstOccurance(arr, n, x)
  if first == -1:
    return (-1, -1)
  last = lastOccurance(arr, n, x)
  return (first, last)

def count(arr, n, x):
  first, last = firstAndLastPosition(arr, n, x)
  if first == -1:
    return 0
  return last - first + 1

arr = [2,4,6,8,8,8,11,13]
n = 8 
x = 8
print(count(arr, n, x))



# 8 TODO : search in rotated array I
# method 1 : brute force approch, TC - O(N), SC - O(1)

def search(arr, n, k):
  for i in range(n):
    if arr[i] == k:
      return i
  return -1

arr = [7,8,9,1,2,3,4,5,6]
n = 9
k = 1
print(search(arr, n, k))



# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - O(log(N)) , SC - O(1)

def search(arr, n, k):
  low = 0
  high = n - 1
  while low <= high:
    mid = (low + high) // 2
    if arr[mid] == k:
      return mid
    if arr[low] <= arr[mid]:
      if arr[low] <= k and k <= arr[mid]:
        high = mid - 1
      else:
        low = mid + 1
    else:
      if arr[mid] <= k and k <= arr[high]:
        low = mid + 1
      else:
        high = mid - 1
  return -1

arr = [7,8,9,1,2,3,4,5,6]
n = 9
k = 1
print(search(arr, n, k))



# 9 TODO : search in rotated array II
# method 1 : brute force approch, TC - O(N), SC - O(1)

def search(arr, n, k):
  for i in arr:
    if i == k:
      return True
  return False

arr = [7,8,1,2,3,3,3,4,5,6]
k = 3
print(search(arr, k))



# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - O(log(N/2)) , SC - O(1)

def search(arr, k):
  n = len(arr)
  low = 0
  high = n - 1
  while low <= high:
    mid = (low + high) // 2
    if arr[mid] == k:
      return True
    if arr[low] == arr[mid] and arr[mid] == arr[high]:
      low += 1
      high -= 1
      continue
    if arr[low] <= arr[mid]:
      if arr[low] <= k and k <= arr[mid]:
        high = mid - 1
      else:
        low = mid + 1
    else:
      if arr[mid] <= k and k <= arr[high]:
        low = mid + 1
      else:
        high = mid - 1
  return False

arr = [7,8,1,2,3,3,3,4,5,6]
k = 3
print(search(arr, k))

# 10 TODO :  find minimum in rotated sorted array
# method 1 : brute force approch, TC - O(N) , SC - O(1)
def findMin(arr):
  n = len(arr)
  mini = float('inf')
  for i in range(n):
    mini = min(mini, arr[i])
  return mini

arr = [4,5,6,7,0,1,2,3]
print(findMin(arr))


# method 2 : better approch, TC - O(log(N)) , SC - O(1)
def findMin(arr):
  low = 0
  high = len(arr) - 1
  ans = float('inf')
  while low <= high:
    mid = (low + high) // 2
    if arr[low] <= arr[mid]:
      ans = min(ans, arr[low])
      low = mid + 1
    else: 
      ans = min(ans, arr[mid])
      high = mid - 1
  return ans

arr = [4,5,6,7,0,1,2,3]
print(findMin(arr))

# method 3 : optimal solution, TC - O(log(N)) , SC - O(1) 
def findMin(arr):
  low = 0
  high = len(arr) - 1
  ans = float('inf')
  while low <= high:
    mid = (low + high) // 2
    if arr[low] <= arr[high]:
      ans = min(ans, arr[low])
      break
    if arr[low] <= arr[mid]:
      ans = min(ans, arr[low])
      low = mid + 1
    else:
      ans = min(ans, arr[mid])
      high = mid - 1
  return ans

arr = [4,5,6,7,0,1,2,3]
print(findMin(arr))


# 11 TODO : find out how many times has an array been rotated
# method 1 : brute force approch, TC - O(N), SC - O(1)
def findRotated(arr):
  n = len(arr)
  mini = float('inf')
  index = -1
  for i in range(n):
    if arr[i] < mini:
      mini = arr[i]
      index = i
  return index

arr = [4,5,6,7,0,1,2,3]
print(findRotated(arr))


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, using binary search, TC - O(log(N)), SC - O(1)
def findRotated(arr):
  low = 0
  high = len(arr) - 1
  ans = float("inf")
  index = -1
  while low <= high:
    mid = (low + high) // 2
    if arr[low] <= arr[high]:
      if arr[low] < ans:
        ans = arr[low]
        index = low
      break
    if arr[low] <= arr[mid]:
      if arr[low] < ans:
        ans = arr[low]
        index = low
      low = mid + 1
    else:
      if arr[mid] < ans:
        ans = arr[mid]
        index = mid
      high = mid - 1
  return index

arr = [4,5,6,7,0,1,2,3]
print(findRotated(arr))



# 12 TODO : single element in a sorted array
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 



# 13 TODO : find peak element
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 




# endregion




# region 4.2 BINARY SEARCH on ANSWERS
# -----------------------------------


# 1 TODO :  find square root of a number in log(n) 
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : find the Nth root of a number using binary search
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : koko eating bananas
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : minimum days to make M bouquets
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 5 TODO : find the smallest divisors
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 6 TODO : capacity to ship packages within D days
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 7 TODO : Kth missing positive number
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 8 TODO : aggressive cows
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 



# 9 TODO : book allocation problem
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 

# 10 TODO :  split array - largest sum

# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 

# 11 TODO : painter's partition
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 12 TODO : minimize max distance in gas station
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 13 TODO : median of 2 sorted arrays
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 14 TODO : Kth element of 2 sorted arrays
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 



# endregion






# region 4.3 BINARY SEARCH on 2D ARRAY
# ------------------------------------

# 1 TODO :  find the row with maximum number of 1's
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : search in a 2 D matrix
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : search in a row and column wise sorted matrix
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : find peak element in a 2D matrix
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 5 TODO : matrix median
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 




# endregion




# region 5.1 STRINGS - EASY
# -------------------------

# 1 TODO :  remove outermost pareanthesis
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : reverse words in a given string / palindrome check
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : largest odd number in a string
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : largest common prefix
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 5 TODO : isomorphic string
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 6 TODO : check whether one string is a rotation of another
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 7 TODO : check if two strings are anagram of each other
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 





# endregion





# region 5.2 STRINGS - MEDIUM
# ---------------------------

# 1 TODO : sort characters by frequency
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : maximum nesting depth of parenthesis
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 

# 3 TODO : roman number to integer and vice versa
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : implement atoi
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 5 TODO : count number of substrings
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 6 TODO : longest pallindromic substring (without using DP)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 7 TODO : sum of beauty of all substring
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 8 TODO : reverse every word in a substring
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 



# endregion




# region 6.1 LINKED LIST - 1D EASY
# --------------------------

# 1 TODO :  introduction to linked list, learn about struct and how is node represented
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : inserting a node in a linked list
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : deleting a node in a linked list
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : find the length of the linked list (learn traversal)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 5 TODO : search an element in the linked list
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 



# endregion





# region 6.2 LINKED LIST - DOUBLY  EASY
# -------------------------------------
# 1 TODO :  introduction to linked list, learn about struct and how is node represented
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : insert a node in DLL
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : delete a node in DLL
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : reverse in DLL
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 



# endregion





# region 6.3 LINKED LIST - MEDIUM
# --------------------------------

# 1 TODO :  middle of a LL (Tortoise Hare method)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : reverse a LL (itterative)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : reverse a LL (recursive)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : detect a loop in Ll
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 5 TODO : find the starting point in LL
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 6 TODO : length of a loop in LL
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 7 TODO : check if LL is pallindrome or not
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 8 TODO : segrregate odd and even nodes in a LL
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 9 TODO : remove Nth node from end/back of LL
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 10 TODO :  delete the middle node of a LL
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 11 TODO : sort LL
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 12 TODO : sort a LL of 0's, 1's and 2's by changing links
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 13 TODO : find the intersection points of Y LL
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 14 TODO : add 1 to a number represented by LL
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 15 TODO :add 2 numbers in LL
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# endregion




# region 6.4 LINKED LIST - DOUBLY MEDIUM
# --------------------------------------

# 1 TODO :  delete all occurences of a key in DLL
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : find pairs with given sum in DLL
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : remove duplicates from sorted DLL
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 




# endregion





# region 6.5 LINKED LIST - HARD
# -----------------------------

# 1 TODO :  reverse LL in group of given size K
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : rotate a LL
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : flattening of LL
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : clone a linked list with random and next pointer
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 



# endregion




# region 7.1 RECURSION - BASIC
# ----------------------------

# 1 TODO :  recursive implementation of atoi()
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : pow(x,n)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : count good numbers
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : sort a stack using recursion
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 5 TODO : reverse a stack using recursion
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 



# endregion




# region 7.2 RECURSION - PATTERN
# ------------------------------

# 1 TODO :  generate all binary strings
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : generate paranthesis
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : print all subsequences / power set
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : learn all patterns of subsequences (theory)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 5 TODO : count all subsequences with sum K
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 6 TODO : check if there exists a subsequences with sum K
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 7 TODO : combination sum - I
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 8 TODO : combination sum - II
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 9 TODO : subset sum - I
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 10 TODO :  subset sum - II
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 11 TODO : combination sum  - III
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 12 TODO : letter combination of phone number
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# endregion




# region 7.3 RECUSION - HARD
# --------------------------

# 1 TODO :  pallindrome partitioning
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : word search
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : N queen
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : rent a maze
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 5 TODO : word break
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 6 TODO : M coloring problem
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 7 TODO : sudoko solver
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 8 TODO : expression add operators
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# endregion





# region 8.1 BIT MANIPULATION - BASIC
# -----------------------------------

# 1 TODO :  introduction to bit manipulation
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : check if the i-th bit is set or not
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : check if a number is odd or not
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : check if a number is power of 2 or not
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 5 TODO : count the number of set bits
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 6 TODO : set/unset the right most unset bit
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 7 TODO : swap two numbers
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 8 TODO : divide two integers without using multiplication
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# endregion





# region 8.2 BIT MANIPULATION - MEDIUM
# ------------------------------------

# 1 TODO :  count number of bits to be flipped to convert A to B
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : find the number that appears odd number of times
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : power set 
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : find xor of numbers from left to right
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 5 TODO : find the two numbers appearing off number of times
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 



# endregion





# region 8.3 BIT MANIPULATION - HARD
# ----------------------------------

# 1 TODO :  print prime factors of a number
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : all divisors of a number
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : sieve of eratosthenes
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : find prime factorisation of a number using sieve
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 5 TODO : power(n,x)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 



# endregion






# region 9.1 STACK/QUEUE - LEARNING
# ---------------------------------

# 1 TODO :  implement stack using arrays
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : implement queue using arrays
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : implement stack using queue
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : implement queue using stack
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 5 TODO : implement stack using linked list
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 6 TODO : implement queue using linked list
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 7 TODO : check for balanced paranthesis
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 8 TODO : implement min stack
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 



# endregion






# region 9.2 STACK/QUEUE - PREFIX/POSTFIX
# ---------------------------------------

# 1 TODO :  infix to postfix conversion using stack
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : prefix to infix conversion
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : prefix to postfix conversion
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : postfix to prefix conversion
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 5 TODO : postfix to infix 
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 6 TODO : convert infix to prefix notation
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 




# endregion






# region 9.3 STACK/QUEUE - MONOTONIC
# ----------------------------------

# 1 TODO :  next greater element - I
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : next greater element - II
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : next smaller element
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : number of NGEs to the right
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 5 TODO : trapping rainwater
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 6 TODO : sum of subarray minimum
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 7 TODO : asteriod collision
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 8 TODO : sum of subarray ranges
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 9 TODO : remove k digits
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 10 TODO :  largest rectangle in a histogram
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 11 TODO : maximal rectangle
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 



# endregion






# region 9.4 STACK/QUEUE - IMPLEMENTATION
# ---------------------------------------

# 1 TODO :  sliding window maximum
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : stock span problem
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : the celebrity problem
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : LRU cache (important)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 5 TODO : LFU cache
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# endregion


# region 10.1 SLIDING WINDOW/TWO POINTER - MEDIUM
# -----------------------------------------------

# 1 TODO :  largest substring without repeating characters
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : max consecutive ones - III
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : fruit into baskets
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : longest repeating character replacement
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 5 TODO : binary subarray with sum
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 6 TODO : count number of nice subarrays
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 7 TODO : number of substring containg all three characters
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 8 TODO : maximun point you can obtain from cards


# endregion




# region 10.2 SLIDING WINDOW/TWO POINTER - HARD
# ---------------------------------------------

# 1 TODO : largest substring with at most K distincet characters 
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : subarray with k different integers
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : minimum window substring
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : minimum window subsequence
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 




# endregion




# region 11.1 HEAP/PRIORITY QUEUE - LEARNING
# ------------------------------------------

# 1 TODO :  introduction to parity queue using binary heaps
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : min heap and max heap replacement
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : check if an array represents a min-heap or not
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : convert min heap to max heap
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 



# endregion




# region 11.2 HEAP/PRIORITY QUEUE - MEDIUM
# ----------------------------------------

# 1 TODO :  Kth largest element in an array (use parity queue)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : Kth smallest element in an array  (use parity queue)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : sort K sorted array
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : merge M sorted lists
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 5 TODO : replace each array element by it's corresponding rank
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 6 TODO : task scheduler
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 7 TODO : hands of straights
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 




# endregion


# region 11.3 HEAP/PRIORITY QUEUE - HARD
# --------------------------------------

# 1 TODO :  design twitter
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : connect "n" ropes with minimal cost
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : Kth largest element in a stream of running integers
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : maximum sum combination
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 5 TODO : find median from data stream
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 6 TODO : K most frequent elements
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 



# endregion


# region 12.1 GREEDY ALGORITHM - EASY
# -----------------------------------

# 1 TODO :  assign cookies
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : fractional knapsack approch
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : greedy algorithm to find minimum number of coins
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : lemonade charge
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 5 TODO : valid paranthesis checker
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 



# endregion



# region 12.2 GREEDY ALGORITHM - MEDIUM/HARD
# ------------------------------------------

# 1 TODO :  N meetings in one room
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : jump game - I
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : jump game - II
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : minimum number of platforms required for a railway station
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 5 TODO : job sequenceing problem
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 6 TODO : candy
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 7 TODO : program for shortest job (one SNF) CPU scheduling
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 8 TODO : program for least recently used (LRU) page replacement algorithm
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 9 TODO : insert interval
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 10 TODO :  merge intervals
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 11 TODO : non-overlapping intervals
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 



# endregion


# region 13.1 BINARY TREES - TRAVERSALS
# -------------------------------------

# 1 TODO :  introduction to trees
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : binary tree representation in C++
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : binary tree representation in java
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : binary tree traversals in binary tree
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 5 TODO : preorder traversals of binary tree
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 6 TODO : inorder traversal of binary tree
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 7 TODO : post order traversal of binary tree
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 8 TODO : level order traversal / level order traversal in spiral form
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 9 TODO : iterative preorder traversal of binary tree
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 10 TODO :  iterative inorder traversal of binary tree
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 11 TODO : post order traversal of binary tree using 2-stack
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 12 TODO : post-order traversal of binary tree using 1 stack
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 13 TODO : preorder, inorder and post order traversal in one traversal
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# endregion



# region 13.2 BINARY TREES - MEDIUM
# ----------------------------------

# 1 TODO :  height of a binary tree
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : check if the binary tree is height-balanced or not
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : diameter of a binary tree
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : maximum path sum
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 5 TODO : check if two trees are identical or not
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 6 TODO : zig-zag traversal of binary tree
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 7 TODO : boundary traversal of binary tree
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 8 TODO : vertical order traversal of binary tree
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 9 TODO : top view binary tree
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 10 TODO :  bottom view binary tree
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 11 TODO : right/left view of a binary tree
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 12 TODO : symmetric binary tree
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# endregion



# region 13.3 BINARY TREES - HARD
# --------------------------------


# 1 TODO : root to node in a binary tree  
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : LCA in binary tree
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : maximum width of a binary tree
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : check for children sum property
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 5 TODO : print all the nodes at a distance of k in binary tree
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 6 TODO : minimum time taken to BURN the binary tree from a node
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 7 TODO : count total nodes in a complete binary tree
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 8 TODO : requirements needed to construct a unique binary tree (theory)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 9 TODO : construct binary tree from inorder and preorder traversal
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 10 TODO :  construct binary tree from postorder and inorder traversal
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 11 TODO : serialize and deserialize binary tree

# 12 TODO : morris preorder traversal of a binary tree
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 13 TODO : morris inorder traversal of a binary tree
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 14 TODO : flatten  binary tree to linked list
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 



# endregion



# region 14.1 BINARY SEARCH TREES - CONCEPTS
# ------------------------------------------

# 1 TODO :  introduction to binary search tree
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : search in a binary search tree
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : find min/max in BST
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 



# endregion




# region 14.2 BINARY SEARCH TREES - PRACTICE PROBLEMS
# ---------------------------------------------------

# 1 TODO :  ceil in a BST
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : floor in a BST
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : insert a given node in BST
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : delete a node in BST
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 5 TODO : find Kth smallest/largest element in BST
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 6 TODO : check if a tree is BST or BT
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 7 TODO : LCA in a BST
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 8 TODO : construct a BST from preorder traversal
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 9 TODO : inorder successor/predecessor in BST
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 10 TODO :  merge 2 BSTs
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 11 TODO : two sum in BST | check if there exists a pair with sum K
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 12 TODO : remove BST | connest BST with two nodes swapped
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 13 TODO : largest BST in binary tree
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 



# endregion



# region 15.1 GRAPHS - LEARNING
# -----------------------------

# 1 TODO :  graphs and types
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : graph implementation |c++
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : graph implementation | java
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : connected components | logic explanation
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 5 TODO : BFS
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 6 TODO : DFS
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 




# endregion



# region 15.2 GRAPHS - BFS/DFS
# ----------------------------
# 1 TODO :  number of provinces (leetcode)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : connected components problem in matrix
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : return oranges
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : flood fill
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 5 TODO : cycle detectio in undirected graph (BFS)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 6 TODO : cycle detectio in undirected graph (DFS)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 7 TODO : 0/1 matrix (BFS problem)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 8 TODO : surrounded regions (DFS)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 9 TODO : number of enclaves (flood fill implementation - multisource)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 10 TODO :  word index - 1
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 11 TODO : word index - 2
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 12 TODO : number of distinct islands (DFS multi source)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 13 TODO : bipartite Graphs (DFS)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 14 TODO : cucle detection in directed graph (DFS)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 




# endregion



# region 15.3 GRAPHS - TOPO SORT
# ------------------------------

# 1 TODO :  topo sort
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : kahn's algorithm
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : cycle detection in directed graph (BFS)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : course schedule - I
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 5 TODO : course schedule - 2
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 6 TODO : find eventual safe states
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 7 TODO : alien dictionary
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 




# endregion


# region 15.4 GRAPHS - SORTEST PATH
# ---------------------------------

# 1 TODO :  shortest path in UG with unit weights
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : shortest path in DAG
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : Dijkatra's algorithm
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : why parity queue is used in dijkatra's algorithm
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 5 TODO : shortest path in binary tree
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 6 TODO : path with minimum effort
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 7 TODO : cheapest flights with K stops
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 8 TODO : network delay time
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 9 TODO : number of ways to arive at destination
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 10 TODO :  minimum steps to reach end from start by performing multiplicationand mod with array elements
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 11 TODO : bellman ford algorithm
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 12 TODO : floyd warshall algorithm
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 13 TODO : find the city with the smallest number of neighbours at a threshold distance
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 




# endregion


# region 15.5 GRAPHS - MST/DISJOINT SET
# -------------------------------------

# 1 TODO :  minimu spanning tree
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : prism's algorithm
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : disjoint set (union by rank)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : disjoint set (union by size)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 5 TODO : kruskal's algorithm
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 6 TODO : number of operations to make network connected
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 7 TODO : most stones removed with the same rows or columns
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 8 TODO : accounts merge
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 9 TODO : number of islands - II
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 10 TODO :  making a large island
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 11 TODO : swim in rising water
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# endregion


# region 15.6 GRAPHS - OTHER ALGORITHMS
# -------------------------------------

# 1 TODO :  bridges in graph
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : articulation point
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : kosaraju's algorithm
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 




# endregion



# region 16.1 DP - INTRODUCTION
# -----------------------------

# 1 TODO :  dynamic programming introduction
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 



# endregion


# region 16.2 DP - 1D
# -------------------
# 1 TODO :  climbing stars
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : frog jump (DP -3)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : frog jump with k distances(DP - 4)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : maximum sum of non-adjacent elements (DP-5)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 5 TODO : house robber (DP-6)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 





# endregion

# region 16.3 DP - 2D/3D/GRIDS
# ----------------------------
# 1 TODO :  ninjas's training (Dp-7)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : grid unique paths : DP on grids (DP-8)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : grid unique paths 2 (DP - 9)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : minimum path sum in grid (DP-10)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 5 TODO : minimum path sum in triangular grid (DP-11)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 6 TODO : minimum/maximum falling path sum (DP-12)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 7 TODO : 3D DP : ninja and his friends (DP-13)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 



# endregion

# region 16.4 DP - SUBSEQUENCES
# -----------------------------

# 1 TODO :  subset sum equals to target (DP-14)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : partition equal subset sum (DP-15)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : partition set into 2 subsets with min absolute sum diff (DP-16)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : count subsets with sum K (DP-17)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 5 TODO : count partitions with given difference (DP-18)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 6 TODO : assign cookies
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 7 TODO : minimum coins (DP-20)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 8 TODO : target sum (DP-21)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 9 TODO : coin change 2 (DP-22)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 10 TODO :  unbounded knapsack (DP-23)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 11 TODO : red cutting problem (DP-24)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 



# endregion


# region 16.5 DP - STRINGS
# ------------------------

# 1 TODO :  longest common subsequence (DP-25)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : print longest common subsequence (DP-26)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : longest common substring (DP-27)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : longest pallindromic subsequence (DP-28)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 5 TODO : minimum insertions to make string pallindromic (DP-29)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 6 TODO : minimum insertions/deletions to convert string (DP-30)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 7 TODO : shortest common subsequence (DP-31)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 8 TODO : distinct subsequences (DP-32)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 9 TODO : edit distance (DP-33)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 10 TODO :  wildcard matching (DP-34)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 



# endregion


# region 16.6 DP - STOCKS
# -----------------------

# 1 TODO : best time to bus stocks - I (DP -35)  
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : buy and sell stock - II (DP - 36)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : buy and sell stock - III (DP-37)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : buy and sell stock - IV (DP-38)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 5 TODO : buy and sell stock with cooldown (DP-39)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 6 TODO : buy and sell stock with transaction fee (DP-40)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 




# endregion


# region 16.7 DP - LIS
# --------------------

# 1 TODO :  longest increasing subsequence (DP-41)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : printing longest increasing subsequence (DP-42)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : longest increasing subsequence (DP-43)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : largest divisible subset (DP-44)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 5 TODO : largest string chain (DP-45)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 6 TODO : longest bitonic subsequence (DP-46)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 7 TODO : number of longest increasing subsequence (DP-47)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 



# endregion



# region 16.8 DP - MCM/PARTITION
# ------------------------------

# 1 TODO :  bitonic chain multiplication (DP-48)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : matrix chain multiplication | Bottom up (DP-49)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : minimum cost to cut the stick (DP-50)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : burst balloons (DP-51)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 5 TODO : evaluate boolean expression to true (DP-52)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 6 TODO : pallindrome partioning - I (DP-53)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 7 TODO : partition array for maximumsum (DP-54)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# endregion



# region 16.9 DP - SQUARES
# ------------------------


# 1 TODO :  maximum rectangle area with all 1's (DP-55)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : count square submatrices with all ones (DP-56)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 




# endregion


# region 17.1 TRIES - THEORY
# --------------------------

# 1 TODO :  implement trie | insert |search | startswith
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 



# endregion


# region 17.2 TRIES - PRACTICE PROBLEMS
# -------------------------------------

# 1 TODO :  implement trie -2 (prefix tree)
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : longest string with all prefixes
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : number of distinct substrings in a string
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : bit preRequisites for trie problems
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 5 TODO : maximum xor of two numbers in an array
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 6 TODO : maximum xor with an element from array
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 




# endregion


# region 18.1 STRINGS - HARD
# --------------------------

# 1 TODO :  minimum number of brackets reversals neededto make an expression balanced
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 2 TODO : count and say
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 3 TODO : hashing in strings | theory
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 4 TODO : rabin karp
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 5 TODO : 2-function
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 6 TODO : KMP algo/LSP(pl) array
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 7 TODO : shortest pallindrome
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 8 TODO : longest happy prefix
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# 9 TODO : count pallindromic subsequence in given string
# method 1 : brute force approch, TC - , SC -


# method 2 : better approch, TC - , SC -


# method 3 : optimal solution, TC - , SC - 


# endregion

