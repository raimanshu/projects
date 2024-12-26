


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


# method 3 : optimal solution
# TC     -      
# SC     -      



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


# method 2 : better approch
# TC     -      
# SC     -     


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


# method 2 : better approch
# TC     -      
# SC     -     


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
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


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
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      
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


# method 2 : better approch
# TC     -      
# SC     -     


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


# method 2 : better approch
# TC     -      
# SC     -     


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



# method 2 : better approch
# TC     -      
# SC     -     


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



# method 2 : better approch
# TC     -      
# SC     -     


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


# method 2 : better approch
# TC     -      
# SC     -     


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
# method 1 : brute force approch, TC - O(N), SC - O(1)
def singleNonDuplicate(arr):
    n = len(arr)  # Size of the array
    if n == 1:
        return arr[0]

    for i in range(n):
        # Check for first index
        if i == 0:
            if arr[i] != arr[i + 1]:
                return arr[i]
        # Check for last index
        elif i == n - 1:
            if arr[i] != arr[i - 1]:
                return arr[i]
        else:
            if arr[i] != arr[i - 1] and arr[i] != arr[i + 1]:
                return arr[i]

    # Dummy return statement
    return -1

arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
ans = singleNonDuplicate(arr)
print("The single element is:", ans)



# method 2 : better approch, TC - O(N), SC - O(1)
def singleNonDuplicate(arr):
    n = len(arr)  # Size of the array
    ans = 0
    # XOR all the elements
    for i in range(n):
        ans = ans ^ arr[i]
    return ans

arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
ans = singleNonDuplicate(arr)
print("The single element is:", ans)



# method 3 : optimal solution, TC - O(log(N)), SC - O(1) 

def singleNonDuplicate(arr):
    n = len(arr)  # Size of the array

    # Edge cases:
    if n == 1:
        return arr[0]
    if arr[0] != arr[1]:
        return arr[0]
    if arr[n - 1] != arr[n - 2]:
        return arr[n - 1]

    low = 1
    high = n - 2
    while low <= high:
        mid = (low + high) // 2

        # If arr[mid] is the single element:
        if arr[mid] != arr[mid + 1] and arr[mid] != arr[mid - 1]:
            return arr[mid]

        # We are in the left:
        if (mid % 2 == 1 and arr[mid] == arr[mid - 1]) or (mid % 2 == 0 and arr[mid] == arr[mid + 1]):
            # Eliminate the left half:
            low = mid + 1
        # We are in the right:
        else:
            # Eliminate the right half:
            high = mid - 1

    # Dummy return statement:
    return -1

arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
ans = singleNonDuplicate(arr)
print("The single element is:", ans)





# 13 TODO : find peak element
# method 1 : brute force approch, TC - O(N) , SC - O(1)



def findPeakElement(arr: [int]) -> int:
    n = len(arr) # Size of the array

    for i in range(n):
        # Checking for the peak:
        if (i == 0 or arr[i - 1] < arr[i]) and (i == n - 1 or arr[i] > arr[i + 1]):
            return i

    # Dummy return statement
    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1]
ans = findPeakElement(arr)
print("The peak is at index:", ans)


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution, TC - O(log(N)) , SC - O(1) 



def findPeakElement(arr: [int]) -> int:
    n = len(arr)  # Size of the array

    # Edge cases:
    if n == 1:
        return 0
    if arr[0] > arr[1]:
        return 0
    if arr[n - 1] > arr[n - 2]:
        return n - 1

    low = 1
    high = n - 2
    while low <= high:
        mid = (low + high) // 2

        # If arr[mid] is the peak:
        if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
            return mid

        # If we are in the left:
        if arr[mid] > arr[mid - 1]:
            low = mid + 1

        # If we are in the right:
        # Or, arr[mid] is a common point:
        else:
            high = mid - 1

    # Dummy return statement
    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1]
ans = findPeakElement(arr)
print("The peak is at index:", ans)





# endregion




# region 4.2 BINARY SEARCH on ANSWERS
# -----------------------------------


# 1 TODO :  find square root of a number in log(n) 
# method 1 : brute force approch, TC - O(N) , SC - O(1)



def floorSqrt(n):
    ans = 0
    # Linear search on the answer space:
    for i in range(1, n+1):
        val = i * i
        if val <= n:
            ans = i
        else:
            break
    return ans

n = 28
ans = floorSqrt(n)
print("The floor of square root of", n, "is:", ans)




# method 2 : better approch, TC - O(log(N)), SC - O(1)



import math

def floorSqrt(n):
    ans = int(math.sqrt(n))
    return ans

n = 28
ans = floorSqrt(n)
print("The floor of square root of", n, "is:", ans)




# method 3 : optimal solution, TC - O(log(N)), SC - O(1)



def floorSqrt(n):
    low = 1
    high = n
    # Binary search on the answers:
    while low <= high:
        mid = (low + high) // 2
        val = mid * mid
        if val <= n:
            # Eliminate the left half:
            low = mid + 1
        else:
            # Eliminate the right half:
            high = mid - 1
    return high

n = 28
ans = floorSqrt(n)
print("The floor of square root of", n, "is:", ans)





# 2 TODO : find the Nth root of a number using binary search
# method 1 : brute force approch, TC - O(M), SC - O(1)



def func(b, exp):
    ans = 1
    base = b
    while exp > 0:
        if exp % 2:
            exp -= 1
            ans = ans * base
        else:
            exp //= 2
            base = base * base
    return ans

def NthRoot(n: int, m: int) -> int:
    for i in range(1, m + 1):
        val = func(i, n)
        if val == m:
            return i
        elif val > m:
            break
    return -1

n = 3
m = 27
ans = NthRoot(n, m)
print("The answer is:", ans)






# method 2 : better approch
# TC     -      
# SC     -     



# method 3 : optimal solution, TC - O(log(N)), SC - O(1) 



def func(mid, n, m):
    ans = 1
    for i in range(1, n + 1):
        ans *= mid
        if ans > m:
            return 2
    if ans == m:
        return 1
    return 0

def NthRoot(n: int, m: int) -> int:
    low = 1
    high = m
    while low <= high:
        mid = (low + high) // 2
        midN = func(mid, n, m)
        if midN == 1:
            return mid
        elif midN == 0:
            low = mid + 1
        else:
            high = mid - 1
    return -1

n = 3
m = 27
ans = NthRoot(n, m)
print("The answer is:", ans)




# 3 TODO : koko eating bananas
# method 1 : brute force approch, TC - O(max(a[]) * N), SC - O(1)



import math

def findMax(v):
    maxi = float('-inf')
    n = len(v)
    # Find the maximum
    for i in range(n):
        maxi = max(maxi, v[i])
    return maxi

def calculateTotalHours(v, hourly):
    totalH = 0
    n = len(v)
    # Find total hours
    for i in range(n):
        totalH += math.ceil(v[i] / hourly)
    return totalH

def minimumRateToEatBananas(v, h):
    # Find the maximum number
    maxi = findMax(v)

    # Find the minimum value of k
    for i in range(1, maxi+1):
        reqTime = calculateTotalHours(v, i)
        if reqTime <= h:
            return i

    # Dummy return statement
    return maxi

v = [7, 15, 6, 3]
h = 8
ans = minimumRateToEatBananas(v, h)
print("Koko should eat at least", ans, "bananas/hr.")



# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution, TC - O(N * log(max(a[]))), SC - O(1)



import math

def findMax(v):
    maxi = float('-inf')
    n = len(v)
    # Find the maximum
    for i in range(n):
        maxi = max(maxi, v[i])
    return maxi

def calculateTotalHours(v, hourly):
    totalH = 0
    n = len(v)
    # Find total hours
    for i in range(n):
        totalH += math.ceil(v[i] / hourly)
    return totalH

def minimumRateToEatBananas(v, h):
    low = 1
    high = findMax(v)

    # Apply binary search
    while low <= high:
        mid = (low + high) // 2
        totalH = calculateTotalHours(v, mid)
        if totalH <= h:
            high = mid - 1
        else:
            low = mid + 1
    return low

v = [7, 15, 6, 3]
h = 8
ans = minimumRateToEatBananas(v, h)
print("Koko should eat at least", ans, "bananas/hr.")




# 4 TODO : minimum days to make M bouquets
# method 1 : brute force approch
# Time Complexity: O((max(arr[])-min(arr[])+1) * N), where {max(arr[]) -> maximum element of the array, min(arr[]) -> minimum element of the array, N = size of the array}.
# Reason: We are running a loop to check our answers that are in the range of [min(arr[]), max(arr[])]. For every possible answer, we will call the possible() function. Inside the possible() function, we are traversing the entire array, which results in O(N).

# Space Complexity: O(1) as we are not using any extra space to solve this problem.   



def possible(arr, day, m, k):
    n = len(arr)  # size of the array
    cnt = 0
    noOfB = 0
    # count the number of bouquets
    for i in range(n):
        if arr[i] <= day:
            cnt += 1
        else:
            noOfB += cnt // k
            cnt = 0
    noOfB += cnt // k
    return noOfB >= m

def roseGarden(arr, k, m):
    val = m * k
    n = len(arr)  # size of the array
    if val > n:
        return -1  # impossible case
    # find maximum and minimum
    mini = float('inf')
    maxi = float('-inf')
    for i in range(n):
        mini = min(mini, arr[i])
        maxi = max(maxi, arr[i])

    for i in range(mini, maxi+1):
        if possible(arr, i, m, k):
            return i
    return -1

arr = [7, 7, 7, 7, 13, 11, 12, 7]
k = 3
m = 2
ans = roseGarden(arr, k, m)
if ans == -1:
    print("We cannot make m bouquets.")
else:
    print("We can make bouquets on day", ans)





# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(log(max(arr[])-min(arr[])+1) * N), where {max(arr[]) -> maximum element of the array, min(arr[]) -> minimum element of the array, N = size of the array}.
Reason: We are applying binary search on our answers that are in the range of [min(arr[]), max(arr[])]. For every possible answer ‘mid’, we will call the possible() function. Inside the possible() function, we are traversing the entire array, which results in O(N).

Space Complexity: O(1) as we are not using any extra space to solve this problem.




def possible(arr, day, m, k):
    n = len(arr)  # size of the array
    cnt = 0
    noOfB = 0
    # count the number of bouquets
    for i in range(n):
        if arr[i] <= day:
            cnt += 1
        else:
            noOfB += cnt // k
            cnt = 0
    noOfB += cnt // k
    return noOfB >= m

def roseGarden(arr, k, m):
    val = m * k
    n = len(arr)  # size of the array
    if val > n:
        return -1  # impossible case
    # find maximum and minimum
    mini = float('inf')
    maxi = float('-inf')
    for i in range(n):
        mini = min(mini, arr[i])
        maxi = max(maxi, arr[i])

    # apply binary search
    low = mini
    high = maxi
    while low <= high:
        mid = (low + high) // 2
        if possible(arr, mid, m, k):
            high = mid - 1
        else:
            low = mid + 1
    return low

arr = [7, 7, 7, 7, 13, 11, 12, 7]
k = 3
m = 2
ans = roseGarden(arr, k, m)
if ans == -1:
    print("We cannot make m bouquets.")
else:
    print("We can make bouquets on day", ans)





# 5 TODO : find the smallest divisors
# method 1 : brute force approch
Time Complexity: O(max(arr[])*N), where max(arr[]) = maximum element in the array, N = size of the array.
Reason: We are using nested loops. The outer loop runs from 1 to max(arr[]) and the inner loop runs for N times.

Space Complexity: O(1) as we are not using any extra space to solve this problem. 



import math

def smallestDivisor(arr, limit):
    n = len(arr)  # size of array
    maxi = max(arr)
    # Find the smallest divisor
    for d in range(1, maxi+1):
        # Find the summation result
        sum = 0
        for i in range(n):
            sum += math.ceil(arr[i] / d)
        if sum <= limit:
            return d
    return -1

arr = [1, 2, 3, 4, 5]
limit = 8
ans = smallestDivisor(arr, limit)
print("The minimum divisor is:", ans)




# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(log(max(arr[]))*N), where max(arr[]) = maximum element in the array, N = size of the array.
Reason: We are applying binary search on our answers that are in the range of [1, max(arr[])]. For every possible divisor ‘mid’, we call the sumByD() function. Inside that function, we are traversing the entire array, which results in O(N).

Space Complexity: O(1) as we are not using any extra space to solve this problem.




import math

def sumByD(arr, div):
    n = len(arr)  # size of array
    # Find the summation of division values
    total_sum = 0
    for i in range(n):
        total_sum += math.ceil(arr[i] / div)
    return total_sum

def smallestDivisor(arr, limit):
    n = len(arr)
    if n > limit:
        return -1
    low = 1
    high = max(arr)

    # Apply binary search
    while low <= high:
        mid = (low + high) // 2
        if sumByD(arr, mid) <= limit:
            high = mid - 1
        else:
            low = mid + 1
    return low

arr = [1, 2, 3, 4, 5]
limit = 8
ans = smallestDivisor(arr, limit)
print("The minimum divisor is:", ans)





# 6 TODO : capacity to ship packages within D days
# method 1 : brute force approch
Time Complexity: O(N * (sum(weights[]) - max(weights[]) + 1)), where sum(weights[]) = summation of all the weights, max(weights[]) = maximum of all the weights, N = size of the weights array.
Reason: We are using a loop from max(weights[]) to sum(weights[]) to check all possible weights. Inside the loop, we are calling findDays() function for each weight. Now, inside the findDays() function, we are using a loop that runs for N times.

Space Complexity: O(1) as we are not using any extra space to solve this problem.




from typing import List

def findDays(weights: List[int], cap: int) -> int:
    days = 1  # First day
    load = 0
    n = len(weights)  # size of array

    for i in range(n):
        if load + weights[i] > cap:
            days += 1  # move to next day
            load = weights[i]  # load the weight
        else:
            # load the weight on the same day
            load += weights[i]
    
    return days

def leastWeightCapacity(weights: List[int], d: int) -> int:
    # Find the maximum and the summation
    maxi = max(weights)
    summation = sum(weights)

    for i in range(maxi, summation + 1):
        if findDays(weights, i) <= d:
            return i

    # dummy return statement
    return -1

weights = [5, 4, 5, 2, 3, 4, 5, 6]
d = 5
ans = leastWeightCapacity(weights, d)
print("The minimum capacity should be:", ans)





# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(N * log(sum(weights[]) - max(weights[]) + 1)), where sum(weights[]) = summation of all the weights, max(weights[]) = maximum of all the weights, N = size of the weights array.
Reason: We are applying binary search on the range [max(weights[]), sum(weights[])]. For every possible answer ‘mid’, we are calling findDays() function. Now, inside the findDays() function, we are using a loop that runs for N times.

Space Complexity: O(1) as we are not using any extra space to solve this problem.




def findDays(weights, cap):
    days = 1  # First day
    load = 0
    n = len(weights)  # Size of array
    for i in range(n):
        if load + weights[i] > cap:
            days += 1  # Move to next day
            load = weights[i]  # Load the weight
        else:
            # Load the weight on the same day
            load += weights[i]
    return days

def leastWeightCapacity(weights, d):
    # Find the maximum and the summation
    low = max(weights)
    high = sum(weights)
    while low <= high:
        mid = (low + high) // 2
        numberOfDays = findDays(weights, mid)
        if numberOfDays <= d:
            # Eliminate right half
            high = mid - 1
        else:
            # Eliminate left half
            low = mid + 1
    return low

weights = [5, 4, 5, 2, 3, 4, 5, 6]
d = 5
ans = leastWeightCapacity(weights, d)
print("The minimum capacity should be:", ans)





# 7 TODO : Kth missing positive number
# method 1 : brute force approch
Time Complexity: O(N), N = size of the given array.
Reason: We are using a loop that traverses the entire given array in the worst case.

Space Complexity: O(1) as we are not using any extra space to solve this problem.




def missingK(vec, n, k):
    for i in range(n):
        if vec[i] <= k:
            k += 1  # shifting k
        else:
            break
    return k


vec = [4, 7, 9, 10]
n = 4
k = 4
ans = missingK(vec, n, k)
print("The missing number is:", ans)






# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(logN), N = size of the given array.
Reason: We are using the simple binary search algorithm.

Space Complexity: O(1) as we are not using any extra space to solve this problem.




def missingK(vec, n, k):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        missing = vec[mid] - (mid + 1)
        if missing < k:
            low = mid + 1
        else:
            high = mid - 1
    return k + high + 1

vec = [4, 7, 9, 10]
n = 4
k = 4
ans = missingK(vec, n, k)
print("The missing number is:", ans)





# 8 TODO : aggressive cows
# method 1 : brute force approch
Time Complexity: O(NlogN) + O(N *(max(stalls[])-min(stalls[]))), where N = size of the array, max(stalls[]) = maximum element in stalls[] array, min(stalls[]) = minimum element in stalls[] array.
Reason: O(NlogN) for sorting the array. We are using a loop from 1 to max(stalls[])-min(stalls[]) to check all possible distances. Inside the loop, we are calling canWePlace() function for each distance. Now, inside the canWePlace() function, we are using a loop that runs for N times.

Space Complexity: O(1) as we are not using any extra space to solve this problem.




def canWePlace(stalls, dist, cows):
    n = len(stalls)  # size of array
    cntCows = 1  # no. of cows placed
    last = stalls[0]  # position of last placed cow
    for i in range(1, n):
        if stalls[i] - last >= dist:
            cntCows += 1  # place next cow
            last = stalls[i]  # update the last location
        if cntCows >= cows:
            return True
    return False

def aggressiveCows(stalls, k):
    n = len(stalls)  # size of array
    stalls.sort()  # sort the stalls[]
    limit = stalls[n - 1] - stalls[0]
    for i in range(1, limit + 1):
        if not canWePlace(stalls, i, k):
            return i - 1
    return limit

stalls = [0, 3, 4, 7, 10, 9]
k = 4
ans = aggressiveCows(stalls, k)
print("The maximum possible minimum distance is:", ans)






# method 2 : better approch
# TC     -      
# SC     -     


Time Complexity: O(NlogN) + O(N * log(max(stalls[])-min(stalls[]))), where N = size of the array, max(stalls[]) = maximum element in stalls[] array, min(stalls[]) = minimum element in stalls[] array.
Reason: O(NlogN) for sorting the array. We are applying binary search on [1, max(stalls[])-min(stalls[])]. Inside the loop, we are calling canWePlace() function for each distance, ‘mid’. Now, inside the canWePlace() function, we are using a loop that runs for N times.

Space Complexity: O(1) as we are not using any extra space to solve this problem.




def canWePlace(stalls, dist, cows):
    n = len(stalls)  # size of array
    cntCows = 1  # no. of cows placed
    last = stalls[0]  # position of last placed cow
    for i in range(1, n):
        if stalls[i] - last >= dist:
            cntCows += 1  # place next cow
            last = stalls[i]  # update the last location
        if cntCows >= cows:
            return True
    return False

def aggressiveCows(stalls, k):
    n = len(stalls)  # size of array
    stalls.sort()  # sort the stalls

    low = 1
    high = stalls[n - 1] - stalls[0]
    # apply binary search
    while low <= high:
        mid = (low + high) // 2
        if canWePlace(stalls, mid, k):
            low = mid + 1
        else:
            high = mid - 1
    return high

stalls = [0, 3, 4, 7, 10, 9]
k = 4
ans = aggressiveCows(stalls, k)
print("The maximum possible minimum distance is:", ans)





# 9 TODO : book allocation problem
# method 1 : brute force approch
Time Complexity: O(N * (sum(arr[])-max(arr[])+1)), where N = size of the array, sum(arr[]) = sum of all array elements, max(arr[]) = maximum of all array elements.
Reason: We are using a loop from max(arr[]) to sum(arr[]) to check all possible numbers of pages. Inside the loop, we are calling the countStudents() function for each number. Now, inside the countStudents() function, we are using a loop that runs for N times.

Space Complexity:  O(1) as we are not using any extra space to solve this problem.




def countStudents(arr, pages):
    n = len(arr)  # size of array
    students = 1
    pagesStudent = 0
    for i in range(n):
        if pagesStudent + arr[i] <= pages:
            # add pages to current student
            pagesStudent += arr[i]
        else:
            # add pages to next student
            students += 1
            pagesStudent = arr[i]
    return students

def findPages(arr, n, m):
    # book allocation impossible
    if m > n:
        return -1

    low = max(arr)
    high = sum(arr)

    for pages in range(low, high + 1):
        if countStudents(arr, pages) == m:
            return pages
    return low

arr = [25, 46, 28, 49, 24]
n = 5
m = 4
ans = findPages(arr, n, m)
print("The answer is:", ans)





# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(N * log(sum(arr[])-max(arr[])+1)), where N = size of the array, sum(arr[]) = sum of all array elements, max(arr[]) = maximum of all array elements.
Reason: We are applying binary search on [max(arr[]), sum(arr[])]. Inside the loop, we are calling the countStudents() function for the value of ‘mid’. Now, inside the countStudents() function, we are using a loop that runs for N times.

Space Complexity:  O(1) as we are not using any extra space to solve this problem. 



def countStudents(arr, pages):
    n = len(arr)  # size of array
    students = 1
    pagesStudent = 0
    for i in range(n):
        if pagesStudent + arr[i] <= pages:
            # add pages to current student
            pagesStudent += arr[i]
        else:
            # add pages to next student
            students += 1
            pagesStudent = arr[i]
    return students

def findPages(arr, n, m):
    # book allocation impossible
    if m > n:
        return -1

    low = max(arr)
    high = sum(arr)
    while low <= high:
        mid = (low + high) // 2
        students = countStudents(arr, mid)
        if students > m:
            low = mid + 1
        else:
            high = mid - 1
    return low

arr = [25, 46, 28, 49, 24]
n = 5
m = 4
ans = findPages(arr, n, m)
print("The answer is:", ans)






# 10 TODO :  split array - largest sum

Time Complexity: O(N * (sum(arr[])-max(arr[])+1)), where N = size of the array, sum(arr[]) = sum of all array elements, max(arr[]) = maximum of all array elements.
Reason: We are using a loop from max(arr[]) to sum(arr[]) to check all possible values of time. Inside the loop, we are calling the countPartitions() function for each number. Now, inside the countPartitions() function, we are using a loop that runs for N times.

Space Complexity:  O(1) as we are not using any extra space to solve this problem.




def countPartitions(a, maxSum):
    n = len(a)  # size of array
    partitions = 1
    subarraySum = 0
    for i in range(n):
        if subarraySum + a[i] <= maxSum:
            # insert element to current subarray
            subarraySum += a[i]
        else:
            # insert element to next subarray
            partitions += 1
            subarraySum = a[i]
    return partitions

def largestSubarraySumMinimized(a, k):
    low = max(a)
    high = sum(a)

    for maxSum in range(low, high+1):
        if countPartitions(a, maxSum) == k:
            return maxSum
    return low

a = [10, 20, 30, 40]
k = 2
ans = largestSubarraySumMinimized(a, k)
print("The answer is:", ans)




# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(N * log(sum(arr[])-max(arr[])+1)), where N = size of the array, sum(arr[]) = sum of all array elements, max(arr[]) = maximum of all array elements.
Reason: We are applying binary search on [max(arr[]), sum(arr[])]. Inside the loop, we are calling the countPartitions() function for the value of ‘mid’. Now, inside the countPartitions() function, we are using a loop that runs for N times.

Space Complexity:  O(1) as we are not using any extra space to solve this problem.




def countPartitions(a, maxSum):
    n = len(a)  # size of array
    partitions = 1
    subarraySum = 0
    for i in range(n):
        if subarraySum + a[i] <= maxSum:
            # insert element to current subarray
            subarraySum += a[i]
        else:
            # insert element to next subarray
            partitions += 1
            subarraySum = a[i]
    return partitions

def largestSubarraySumMinimized(a, k):
    low = max(a)
    high = sum(a)
    # Apply binary search
    while low <= high:
        mid = (low + high) // 2
        partitions = countPartitions(a, mid)
        if partitions > k:
            low = mid + 1
        else:
            high = mid - 1
    return low

a = [10, 20, 30, 40]
k = 2
ans = largestSubarraySumMinimized(a, k)
print("The answer is:", ans)




# 11 TODO : painter's partition
# method 1 : brute force approch
Time Complexity: O(N * (sum(arr[])-max(arr[])+1)), where N = size of the array, sum(arr[]) = sum of all array elements, max(arr[]) = maximum of all array elements.
Reason: We are using a loop from max(arr[]) to sum(arr[]) to check all possible values of time. Inside the loop, we are calling the countPainters() function for each number. Now, inside the countPainters() function, we are using a loop that runs for N times.

Space Complexity:  O(1) as we are not using any extra space to solve this problem.




def countPainters(boards, time):
    n = len(boards)  # size of array
    painters = 1
    boardsPainter = 0
    for i in range(n):
        if boardsPainter + boards[i] <= time:
            # allocate board to current painter
            boardsPainter += boards[i]
        else:
            # allocate board to next painter
            painters += 1
            boardsPainter = boards[i]
    return painters


def findLargestMinDistance(boards, k):
    low = max(boards)
    high = sum(boards)

    for time in range(low, high+1):
        if countPainters(boards, time) <= k:
            return time
    return low


boards = [10, 20, 30, 40]
k = 2
ans = findLargestMinDistance(boards, k)
print("The answer is:", ans)





# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(N * log(sum(arr[])-max(arr[])+1)), where N = size of the array, sum(arr[]) = sum of all array elements, max(arr[]) = maximum of all array elements.
Reason: We are applying binary search on [max(arr[]), sum(arr[])]. Inside the loop, we are calling the countPainters() function for the value of ‘mid’. Now, inside the countPainters() function, we are using a loop that runs for N times.

Space Complexity:  O(1) as we are not using any extra space to solve this problem.




def countPainters(boards, time):
    n = len(boards)  # size of array
    painters = 1
    boardsPainter = 0
    for i in range(n):
        if boardsPainter + boards[i] <= time:
            # allocate board to current painter
            boardsPainter += boards[i]
        else:
            # allocate board to next painter
            painters += 1
            boardsPainter = boards[i]
    return painters

def findLargestMinDistance(boards, k):
    low = max(boards)
    high = sum(boards)
    # Apply binary search
    while low <= high:
        mid = (low + high) // 2
        painters = countPainters(boards, mid)
        if painters > k:
            low = mid + 1
        else:
            high = mid - 1
    return low

boards = [10, 20, 30, 40]
k = 2
ans = findLargestMinDistance(boards, k)
print("The answer is:", ans)





# 12 TODO : minimize max distance in gas station
# method 1 : brute force approch
Time Complexity: O(k*n) + O(n), n = size of the given array, k = no. of gas stations to be placed.
Reason: O(k*n) to insert k gas stations between the existing stations with maximum distance. Another O(n) for finding the answer i.e. the maximum distance.

Space Complexity: O(n-1) as we are using an array to keep track of placed gas stations.




def minimiseMaxDistance(arr, k):
    n = len(arr)  # size of array
    howMany = [0] * (n - 1)

    # Pick and place k gas stations:
    for gasStations in range(1, k + 1):
        # Find the maximum section and insert the gas station:
        maxSection = -1
        maxInd = -1
        for i in range(n - 1):
            diff = arr[i + 1] - arr[i]
            sectionLength = diff / (howMany[i] + 1)
            if sectionLength > maxSection:
                maxSection = sectionLength
                maxInd = i
        # insert the current gas station:
        howMany[maxInd] += 1

    # Find the maximum distance i.e. the answer:
    maxAns = -1
    for i in range(n - 1):
        diff = arr[i + 1] - arr[i]
        sectionLength = diff / (howMany[i] + 1)
        maxAns = max(maxAns, sectionLength)
    return maxAns

arr = [1, 2, 3, 4, 5]
k = 4
ans = minimiseMaxDistance(arr, k)
print("The answer is:", ans)




# method 2 : better approch
Time Complexity: O(nlogn + klogn),  n = size of the given array, k = no. of gas stations to be placed.
Reason: Insert operation of priority queue takes logn time complexity. O(nlogn) for inserting all the indices with distance values and O(klogn) for placing the gas stations.

Space Complexity: O(n-1)+O(n-1)
Reason: The first O(n-1) is for the array to keep track of placed gas stations and the second one is for the priority queue.




import heapq

def minimiseMaxDistance(arr, k):
    n = len(arr)  # size of array.
    howMany = [0] * (n - 1)
    pq = []

    # insert the first n-1 elements into pq
    # with respective distance values:
    for i in range(n - 1):
        heapq.heappush(pq, ((-1)*(arr[i + 1] - arr[i]), i))

    # Pick and place k gas stations:
    for gasStations in range(1, k + 1):
        # Find the maximum section
        # and insert the gas station:
        tp = heapq.heappop(pq)
        secInd = tp[1]

        # insert the current gas station:
        howMany[secInd] += 1

        inidiff = arr[secInd + 1] - arr[secInd]
        newSecLen = inidiff / (howMany[secInd] + 1)
        heapq.heappush(pq, (newSecLen*(-1), secInd))

    return pq[0][0]*(-1)

arr = [1, 2, 3, 4, 5]
k = 4
ans = minimiseMaxDistance(arr, k)
print("The answer is:", ans)




# method 3 : optimal solution
Time Complexity: O(n*log(Len)) + O(n), n = size of the given array, Len = length of the answer space.
Reason: We are applying binary search on the answer space. For every possible answer, we are calling the function numberOfGasStationsRequired() that takes O(n) time complexity. And another O(n) for finding the maximum distance initially.

Space Complexity: O(1) as we are using no extra space to solve this problem.




def numberOfGasStationsRequired(dist, arr):
    n = len(arr)  # size of the array
    cnt = 0
    for i in range(1, n):
        numberInBetween = ((arr[i] - arr[i - 1]) / dist)
        if (arr[i] - arr[i - 1]) == (dist * numberInBetween):
            numberInBetween -= 1
        cnt += numberInBetween
    return cnt


def minimiseMaxDistance(arr, k):
    n = len(arr)  # size of the array
    low = 0
    high = 0

    # Find the maximum distance:
    for i in range(n - 1):
        high = max(high, arr[i + 1] - arr[i])

    # Apply Binary search:
    diff = 1e-6
    while high - low > diff:
        mid = (low + high) / 2.0
        cnt = numberOfGasStationsRequired(mid, arr)
        if cnt > k:
            low = mid
        else:
            high = mid

    return high


arr = [1, 2, 3, 4, 5]
k = 4
ans = minimiseMaxDistance(arr, k)
print("The answer is:", ans)





# 13 TODO : median of 2 sorted arrays
# method 1 : brute force approch
Time Complexity: O(n1+n2), where  n1 and n2 are the sizes of the given arrays.
Reason: We traverse through both arrays linearly.

Space Complexity: O(n1+n2), where  n1 and n2 are the sizes of the given arrays.
Reason: We are using an extra array of size (n1+n2) to solve this problem.



def median(a, b):
    # size of two given arrays:
    n1, n2 = len(a), len(b)

    arr3 = []
    # apply the merge step:
    i, j = 0, 0
    while i < n1 and j < n2:
        if a[i] < b[j]:
            arr3.append(a[i])
            i += 1
        else:
            arr3.append(b[j])
            j += 1

    # copy the left-out elements:
    arr3.extend(a[i:])
    arr3.extend(b[j:])

    # Find the median:
    n = n1 + n2
    if n % 2 == 1:
        return float(arr3[n // 2])

    median = (arr3[n // 2] + arr3[(n // 2) - 1]) / 2.0
    return median


if __name__ == "__main__":
    a = [1, 4, 7, 10, 12]
    b = [2, 3, 6, 15]
    print("The median of two sorted arrays is", "{:.1f}".format(median(a, b)))




# method 2 : better approch
Time Complexity: O(n1+n2), where  n1 and n2 are the sizes of the given arrays.
Reason: We traverse through both arrays linearly.

Space Complexity: O(1), as we are not using any extra space to solve this problem.




def median(a, b):
    # size of two given arrays:
    n1, n2 = len(a), len(b)
    n = n1 + n2  # total size
    # required indices:
    ind2 = n // 2
    ind1 = ind2 - 1
    cnt = 0
    ind1el, ind2el = -1, -1

    # apply the merge step:
    i, j = 0, 0
    while i < n1 and j < n2:
        if a[i] < b[j]:
            if cnt == ind1:
                ind1el = a[i]
            if cnt == ind2:
                ind2el = a[i]
            cnt += 1
            i += 1
        else:
            if cnt == ind1:
                ind1el = b[j]
            if cnt == ind2:
                ind2el = b[j]
            cnt += 1
            j += 1

    # copy the left-out elements:
    while i < n1:
        if cnt == ind1:
            ind1el = a[i]
        if cnt == ind2:
            ind2el = a[i]
        cnt += 1
        i += 1
    while j < n2:
        if cnt == ind1:
            ind1el = b[j]
        if cnt == ind2:
            ind2el = b[j]
        cnt += 1
        j += 1

    # Find the median:
    if n % 2 == 1:
        return float(ind2el)

    return float(ind1el + ind2el) / 2.0


if __name__ == "__main__":
    a = [1, 4, 7, 10, 12]
    b = [2, 3, 6, 15]
    print("The median of two sorted arrays is", "{:.1f}".format(median(a, b)))




# method 3 : optimal solution
Time Complexity: O(log(min(n1,n2))), where n1 and n2 are the sizes of two given arrays.
Reason: We are applying binary search on the range [0, min(n1, n2)].

Space Complexity: O(1) as no extra space is used.




def median(a, b):
    n1, n2 = len(a), len(b)
    # if n1 is bigger swap the arrays:
    if n1 > n2:
        return median(b, a)

    n = n1 + n2  # total length
    left = (n1 + n2 + 1) // 2  # length of left half
    # apply binary search:
    low, high = 0, n1
    while low <= high:
        mid1 = (low + high) // 2
        mid2 = left - mid1
        # calculate l1, l2, r1, and r2;
        l1, l2, r1, r2 = float('-inf'), float('-inf'), float('inf'), float('inf')
        if mid1 < n1:
            r1 = a[mid1]
        if mid2 < n2:
            r2 = b[mid2]
        if mid1 - 1 >= 0:
            l1 = a[mid1 - 1]
        if mid2 - 1 >= 0:
            l2 = b[mid2 - 1]

        if l1 <= r2 and l2 <= r1:
            if n % 2 == 1:
                return max(l1, l2)
            else:
                return (float(max(l1, l2)) + float(min(r1, r2))) / 2.0

        # eliminate the halves:
        elif l1 > r2:
            high = mid1 - 1
        else:
            low = mid1 + 1
    return 0  # dummy statement


a = [1, 4, 7, 10, 12]
b = [2, 3, 6, 15]
print("The median of two sorted arrays is {:.1f}".format(median(a, b)))





# 14 TODO : Kth element of 2 sorted arrays
Time Complexity: O(m+n), where m and n are the sizes of the given arrays.
Reason: We traverse through both arrays linearly.

Space Complexity: O(m+n), where m and n are the sizes of the given arrays.

Reason: We are using an extra array of size (m+n) to solve this problem.


            def kthElement(a, b, m, n, k):
                arr3 = []
            
                # Apply the merge step:
                i, j = 0, 0
                while i < m and j < n:
                    if a[i] < b[j]:
                        arr3.append(a[i])
                        i += 1
                    else:
                        arr3.append(b[j])
                        j += 1
            
                # Copy the left-out elements:
                arr3.extend(a[i:])
                arr3.extend(b[j:])
                return arr3[k - 1]
        
            if __name__ == "__main__":
                a = [2, 3, 6, 7, 9]
                b = [1, 4, 8, 10]
                print("The k-th element of two sorted arrays is:", kthElement(a, b, len(a), len(b), 5))
        
        


# method 2 : better approch
Time Complexity: O(m+n), where m and n are the sizes of the given arrays.
Reason: We traverse through both arrays linearly.

Space Complexity: O(1), as we are not using any extra space to solve this problem.


def kthElement(a, b, m, n, k):
    ele = -1
    cnt = 0  # counter
    # apply the merge step:
    i, j = 0, 0
    while i < m and j < n:
        if a[i] < b[j]:
            if cnt == k - 1:
                ele = a[i]
            cnt += 1
            i += 1
        else:
            if cnt == k - 1:
                ele = b[j]
            cnt += 1
            j += 1

    # copy the left-out elements:
    while i < m:
        if cnt == k - 1:
            ele = a[i]
        cnt += 1
        i += 1
    while j < n:
        if cnt == k - 1:
            ele = b[j]
        cnt += 1
        j += 1
    return ele
            
a = [2, 3, 6, 7, 9]
b = [1, 4, 8, 10]
print("The k-th element of two sorted arrays is:", kthElement(a, b, len(a), len(b), 5))
        
        


# method 3 : optimal solution
Time Complexity: O(log(min(m, n))), where m and n are the sizes of two given arrays.
Reason: We are applying binary search on the range [max(0, k-n2), min(k, n1)]. The range length <= min(m, n).

Space Complexity: O(1), as we are not using any extra space to solve this problem.



def kthElement(a, b, m, n, k):
    if m > n:
        return kthElement(b, a, n, m, k)

    left = k  # length of left half

    # apply binary search:
    low = max(0, k - n)
    high = min(k, m)
    while low <= high:
        mid1 = (low + high) // 2
        mid2 = left - mid1
        # calculate l1, l2, r1, and r2
        l1 = float('-inf')
        l2 = float('-inf')
        r1 = float('inf')
        r2 = float('inf')
        if mid1 < m:
            r1 = a[mid1]
        if mid2 < n:
            r2 = b[mid2]
        if mid1 - 1 >= 0:
            l1 = a[mid1 - 1]
        if mid2 - 1 >= 0:
            l2 = b[mid2 - 1]

        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)

        # eliminate the halves:
        elif l1 > r2:
            high = mid1 - 1
        else:
            low = mid1 + 1

    return 0  # dummy statement
            
            
a = [2, 3, 6, 7, 9]
b = [1, 4, 8, 10]
print("The k-th element of two sorted arrays is:", kthElement(a, b, len(a), len(b), 5))
        
        



# endregion






# region 4.3 BINARY SEARCH on 2D ARRAY
# ------------------------------------

# 1 TODO :  find the row with maximum number of 1's
# method 1 : brute force approch
Time Complexity: O(n X m), where n = given row number, m = given column number.
Reason: We are using nested loops running for n and m times respectively.

Space Complexity: O(1) as we are not using any extra space.




def rowWithMax1s(matrix, n, m):
    cnt_max = 0
    index = -1

    # traverse the matrix:
    for i in range(n):
        cnt_ones = sum(matrix[i])
        if cnt_ones > cnt_max:
            cnt_max = cnt_ones
            index = i
    return index

if __name__ == "__main__":
    matrix = [[1, 1, 1], [0, 0, 1], [0, 0, 0]]
    n = 3
    m = 3
    print("The row with maximum no. of 1's is:", rowWithMax1s(matrix, n, m))




# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(n X logm), where n = given row number, m = given column number.
Reason: We are using a loop running for n times to traverse the rows. Then we are applying binary search on each row with m columns.

Space Complexity: O(1) as we are not using any extra space.



def lowerBound(arr, n, x):
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] >= x:
            ans = mid
            # look for smaller index on the left
            high = mid - 1
        else:
            low = mid + 1  # look on the right
    return ans

def rowWithMax1s(matrix, n, m):
    cnt_max = 0
    index = -1

    # traverse the rows:
    for i in range(n):
        # get the number of 1's:
        cnt_ones = m - lowerBound(matrix[i], m, 1)
        if cnt_ones > cnt_max:
            cnt_max = cnt_ones
            index = i
    return index

matrix = [[1, 1, 1], [0, 0, 1], [0, 0, 0]]
n = 3
m = 3
print("The row with maximum no. of 1's is:", rowWithMax1s(matrix, n, m))




# 2 TODO : search in a 2 D matrix
# method 1 : brute force approch
Time Complexity: O(N X M), where N = given row number, M = given column number.
Reason: In order to traverse the matrix, we are using nested loops running for n and m times respectively.

Space Complexity: O(1) as we are not using any extra space.




def searchMatrix(matrix, target):
    n = len(matrix)
    m = len(matrix[0])

    # traverse the matrix:
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == target:
                return True
    return False

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
result = searchMatrix(matrix, 8)
print("true" if result else "false")




# method 2 : better approch
Time Complexity: O(N + logM), where N = given row number, M = given column number.
Reason: We are traversing all rows and it takes O(N) time complexity. But for all rows, we are not applying binary search rather we are only applying it once for a particular row. That is why the time complexity is O(N + logM) instead of O(N*logM).

Space Complexity: O(1) as we are not using any extra space.




def binarySearch(nums, target):
    n = len(nums) # size of the array
    low, high = 0, n - 1

    # Perform the steps:
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return True
        elif target > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return False

def searchMatrix(matrix, target):
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        if matrix[i][0] <= target <= matrix[i][m - 1]:
            return binarySearch(matrix[i], target)
    return False

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
result = searchMatrix(matrix, 8)
print("true" if result else "false")



# method 3 : optimal solution
Time Complexity: O(log(NxM)), where N = given row number, M = given column number.
Reason: We are applying binary search on the imaginary 1D array of size NxM.

Space Complexity: O(1) as we are not using any extra space.



def searchMatrix(matrix, target):
    n = len(matrix)
    m = len(matrix[0])

    # apply binary search:
    low = 0
    high = n * m - 1
    while low <= high:
        mid = (low + high) // 2
        row = mid // m
        col = mid % m
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
result = searchMatrix(matrix, 8)
print("true" if result else "false")





# 3 TODO : search in a row and column wise sorted matrix
# method 1 : brute force approch
Time Complexity: O(N X M), where N = given row number, M = given column number.
Reason: In order to traverse the matrix, we are using nested loops running for n and m times respectively.

Space Complexity: O(1) as we are not using any extra space.




def searchElement(matrix, target):
    n = len(matrix)
    m = len(matrix[0])

    # Traverse the matrix:
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == target:
                return True
    return False

matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]

result = searchElement(matrix, 8)
print("true" if result else "false")




# method 2 : better approch
Time Complexity: O(N*logM), where N = given row number, M = given column number.
Reason: We are traversing all rows and it takes O(N) time complexity. And for all rows, we are applying binary search. So, the total time complexity is O(N*logM).

Space Complexity: O(1) as we are not using any extra space.




def binarySearch(nums, target):
    n = len(nums) # size of the array
    low, high = 0, n - 1

    # Perform the steps:
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return True
        elif target > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return False

def searchElement(matrix, target):
    n = len(matrix)

    for i in range(n):
        flag = binarySearch(matrix[i], target)
        if flag:
            return True
    return False

matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]

result = searchElement(matrix, 8)
print("true" if result else "false")




# method 3 : optimal solution
Time Complexity: O(N+M), where N = given row number, M = given column number.
Reason: We are starting traversal from (0, M-1), and at most, we can end up being in the cell (M-1, 0). So, the total distance can be at most (N+M). So, the time complexity is O(N+M).

Space Complexity: O(1) as we are not using any extra space.




def searchElement(matrix, target):
    n = len(matrix)
    m = len(matrix[0])
    row = 0
    col = m - 1

    # Traverse the matrix from (0, m-1):
    while row < n and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1
    return False

matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]

result = searchElement(matrix, 8)
print("true" if result else "false")





# 4 TODO : find peak element in a 2D matrix
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 5 TODO : matrix median
# method 1 : brute force approch
Time Complexity: O(MXN) + O(MXN(log(MXN))), where M = number of row in the given matrix, N = number of columns in the given matrix

Reason: At first, we are traversing the matrix to copy the elements. This takes O(MXN) time complexity. Then we are sorting the linear array of size (MXN), that takes O(MXN(log(MXN))) time complexity

Space Complexity: O(MXN) as we are using a temporary list to store the elements of the matrix.
                                    
def median(matrix, m, n):
    lst = []

    # Traverse the matrix and copy the elements to the list:
    for i in range(m):
        for j in range(n):
            lst.append(matrix[i][j])

    # Sort the list:
    lst.sort()
    return lst[(m * n) // 2]

matrix = [
    [1, 2, 3, 4, 5],
    [8, 9, 11, 12, 13],
    [21, 23, 25, 27, 29]
]
m = len(matrix)
n = len(matrix[0])
ans = median(matrix, m, n)
print("The median element is:", ans)
                                    


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(log(109)) X O(M(logN)), where M = number of rows in the given matrix, N = number of columns in the given matrix

Reason: Our search space lies between [0, 109] as the min(matrix) can be 0 and the max(matrix) can be 109. We are applying binary search in this search space and it takes O(log(109)) time complexity. Then we call countSmallEqual() function for every ‘mid’ and this function takes O(M(logN)) time complexity.

Space Complexity : O(1) as we are not using any extra space

                                    
                         
def upperBound(arr, x, n):
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] > x:
            ans = mid
            # look for a smaller index on the left
            high = mid - 1
        else:
            low = mid + 1  # look on the right

    return ans

def countSmallEqual(matrix, m, n, x):
    cnt = 0
    for i in range(m):
        cnt += upperBound(matrix[i], x, n)
    return cnt

def median(matrix, m, n):
    low = float('inf')
    high = float('-inf')

    # point low and high to the right elements
    for i in range(m):
        low = min(low, matrix[i][0])
        high = max(high, matrix[i][n - 1])

    req = (n * m) // 2
    while low <= high:
        mid = (low + high) // 2
        smallEqual = countSmallEqual(matrix, m, n, mid)
        if smallEqual <= req:
            low = mid + 1
        else:
            high = mid - 1

    return low

if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4, 5],
        [8, 9, 11, 12, 13],
        [21, 23, 25, 27, 29]
    ]
    m = len(matrix)
    n = len(matrix[0])
    ans = median(matrix, m, n)
    print("The median element is:", ans)
                                    
                                




# endregion




# region 5.1 STRINGS - EASY
# -------------------------

# 1 TODO :  remove outermost pareanthesis
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 2 TODO : reverse words in a given string / palindrome check
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 3 TODO : largest odd number in a string
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 4 TODO : largest common prefix
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 5 TODO : isomorphic string
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 6 TODO : check whether one string is a rotation of another
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 7 TODO : check if two strings are anagram of each other
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      





# endregion





# region 5.2 STRINGS - MEDIUM
# ---------------------------

# 1 TODO : sort characters by frequency
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 2 TODO : maximum nesting depth of parenthesis
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      

# 3 TODO : roman number to integer and vice versa
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 4 TODO : implement atoi
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 5 TODO : count number of substrings
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 6 TODO : longest pallindromic substring (without using DP)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 7 TODO : sum of beauty of all substring
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 8 TODO : reverse every word in a substring
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      



# endregion




# region 6.1 LINKED LIST - 1D EASY
# --------------------------

# 1 TODO :  introduction to linked list, learn about struct and how is node represented
# # method 1 : brute force approch
# class Node:
#     def __init__(self, data1, next1=None):
#         self.data = data1
#         self.next = next1
# # Creating a new Node with the value from the array
# y = Node(2)
# # Printing the data stored in the Node
# print(y.data)

# class Node:
#     def __init__(self, data1, next1=None):
#         self.data = data1
#         self.next = next1
# # Creating a Node 'x' with the first element of the array
# x = Node(2)
# # Creating a reference 'y' pointing to the same Node 'x'
# y = x
# # Printing the reference 'y', which represents the memory address of the Node 'x'
# print(y)
   


# 2 TODO : inserting a node in a linked list
# Node class to represent a linked list node
Time Complexity: O(1) for inserting the new head of the linked list and O(N) for printing the linked list.

Space Complexity: O(1), as we have not used any extra space.
class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1

# Function to print the linked list
def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

# Function to insert a new node at the head of the linked list
def insertHead(head, val):
    temp = Node(val, head)
    return temp

if __name__ == "__main__":
    # Sample array and value for insertion
    arr = [12, 8, 5, 7]
    val = 100

    # Creating a linked list with initial elements from the array
    head = Node(arr[0])
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])
    head.next.next.next = Node(arr[3])

    # Inserting a new node at the head of the linked list
    head = insertHead(head, val)

    # Printing the linked list
    printLL(head) 


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 3 TODO : deleting a node in a linked list
Time Complexity: O(N) for traversing the linked list and updating the tail.

Space Complexity: O(1), as we have not used any extra space.
# method 1 : brute force approch
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

# Function to delete the tail of the linked list
def delete_tail(head):
    # Check if the linked list is empty or has only one node
    if head is None or head.next is None:
        return None

    # Create a temporary pointer for traversal
    temp = head

    # Traverse the list until the second-to-last node
    while temp.next.next is not None:
        temp = temp.next

    # Nullify the connection from the second-to-last node to delete the last node
    temp.next = None

    # Return the updated head of the linked list
    return head

# Function to print the linked list
def print_ll(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

# Main function
if __name__ == "__main__":
    # Initialize an array with integer values
    arr = [2, 5, 8, 7]

    # Create the linked list with nodes initialized with array values
    head = Node(arr[0])
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])
    head.next.next.next = Node(arr[3])

    # Delete the tail of the linked list
    head = delete_tail(head)

    # Print the modified linked list
    print_ll(head)

# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 4 TODO : find the length of the linked list (learn traversal)
Since we are iterating over the entire list,  time complexity is O(N).

Space Complexity:

We are not using any extra space, thus space complexity is O(1) or constant.
# method 1 : brute force approch
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node
# Function to calculate the length of a linked list
def length_of_linked_list(head):
    cnt = 0
    temp = head
    
    # Traverse the linked list and count nodes
    while temp is not None:
        temp = temp.next
        cnt += 1
  
    return cnt
# Main function
def main():
    arr = [2, 5, 8, 7]
    # Create a linked list
    head = Node(arr[0])
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])
    head.next.next.next = Node(arr[3])
    # Print the length of the linked list
    print("Length of the linked list:", length_of_linked_list(head))
main()


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 5 TODO : search an element in the linked list
Time Complexity: O(N) in the worst case if the element is not found. O(1) in the best case if the element is the first element. 

Space Complexity: O(1) as we did not use any extra space.
class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1

# Function to check if a given element is present in the linked list
def check_if_present(head, desired_element):
    temp = head

    # Traverse the linked list
    while temp is not None:
        # Check if the current node's data is equal to the desired element
        if temp.data == desired_element:
            return 1  # Return 1 if the element is found

        # Move to the next node
        temp = temp.next

    return 0  # Return 0 if the element is not found in the linked list

# Main function
if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3
    arr = [1, 2, 3]
    head = Node(arr[0])
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])

    val = 3  # Element to be checked for presence in the linked list

    # Call the check_if_present function and print the result
    print(check_if_present(head, val))

# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      



# endregion





# region 6.2 LINKED LIST - DOUBLY  EASY
# -------------------------------------
# 1 TODO :  introduction to linked list, learn about struct and how is node represented
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 2 TODO : insert a node in DLL
Doubly Linked List Initially:
12 5 8 7 4 
Doubly Linked List After Inserting at the tail with value 10: 
12 5 8 7 4 10

Time Complexity: O(N) The time complexity of this insertion operation is O(N) because we have to traverse the entire list to reach its tail. The complexity would be O(1) if we were given the tail node directly.

Space Complexity: O(1)  The space complexity is also O(1) because we are notusing any extradatastructures to do the operations apart from creating a single new node.
class Node:
    def __init__(self, data, next_node=None, back_node=None):
        """
        Constructor for a Node with data, a reference to the next node, and a reference to the previous node.
        """
        self.data = data
        self.next = next_node
        self.back = back_node

def convertArr2DLL(arr):
    """
    Function to convert an array to a doubly linked list.
    """
    # Create the head node with the first element of the array
    head = Node(arr[0])
    # Initialize 'prev' to the head node
    prev = head

    for i in range(1, len(arr)):
        # Create a new node with data from the array and set its 'back' pointer to the previous node
        temp = Node(arr[i], None, prev)
        # Update the 'next' pointer of the previous node to point to the new node
        prev.next = temp
        # Move 'prev' to the newly created node for the next iteration
        prev = temp

    # Return the head of the doubly linked list
    return head

def print_list(head):
    """
    Function to print the elements of the doubly linked list.
    """
    while head is not None:
        # Print the data in the current node
        print(head.data, end=" ")
        # Move to the next node
        head = head.next

def insert_at_tail(head, k):
    """
    Function to insert a new node with value 'k' at the end of the doubly linked list.
    """
    # Create a new node with data 'k'
    new_node = Node(k)

    # If the doubly linked list is empty, set 'head' to the new node
    if head is None:
        return new_node

    # Traverse to the end of the doubly linked list
    tail = head
    while tail.next is not None:
        tail = tail.next

    # Connect the new node to the last node in the list
    tail.next = new_node
    new_node.back = tail

    return head

# Main program
arr = [12, 5, 8, 7, 4]
head = convertArr2DLL(arr)
print(“\nDoubly Linked List Initially:”)
print_list(head)
print("\nDoubly Linked List After Inserting at the tail with value 10:")



# Insert a node with value 10 at the end
head = insert_at_tail(head, 10)
print_list(head) 


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 3 TODO : delete a node in DLL
Time Complexity: O(1) Removing the head of a doubly linked list is a quick operation, taking constant time because it only involves updating references.

Space Complexity: O(1) Deleting the head also has minimal memory usage, using a few extra pointers without regard to the list's size.
class Node:
    def __init__(self, data, next_node=None, back_node=None):
        self.data = data
        self.next = next_node
        self.back = back_node

def convert_arr_to_dll(arr):
    # Create the head node with the first element of the array
    head = Node(arr[0])
    # Initialize 'prev' to the head node
    prev = head

    for i in range(1, len(arr)):
        # Create a new node with data from the array and set its 'back' pointer to the previous node
        temp = Node(arr[i], None, prev)
        # Update the 'next' pointer of the previous node to point to the new node
        prev.next = temp
        # Move 'prev' to the newly created node for the next iteration
        prev = temp

    # Return the head of the doubly linked list
    return head

def print_dll(head):
    while head is not None:
        # Print the data in the current node
        print(head.data, end=" ")
        # Move to the next node
        head = head.next

def delete_tail(head):
    if head is None or head.next is None:
        return None  # If the list is empty or has only one node, return None

    tail = head
    while tail.next is not None:
        # Traverse to the last node (tail)
        tail = tail.next

    new_tail = tail.back
    new_tail.next = None
    tail.back = None

    # Free memory of the deleted node
    del tail

    return head

if __name__ == "__main__":
    arr = [12, 5, 8, 7]
    head = convert_arr_to_dll(arr)

    print("Original Doubly Linked List:", end=" ")
    print_dll(head)

    print("\n\nAfter deleting the tail node:", end=" ")
    head = delete_tail(head)
    print_dll(head)


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 4 TODO : reverse in DLL
Time Complexity : O(2N) During the first traversal, each node's value is pushed into the stack once, which requires O(N) time. Then, during the second iteration, the values are popped from the stack and used to update the nodes. Space Complexity : O(N) This is because we are using an external stack data structure. At the end of the first iteration, the stack will hold all N values of the doubly linked list therefore the space required for stack is directly proportional to the size of the input doubly linked list.
# method 1 : brute force approch

class Node:
    def __init__(self, data, next_node=None, back_node=None):
        # Data stored in the node
        self.data = data
        # Reference to the next node
        # in the list (forward direction)
        self.next = next_node
        # Reference to the previous node
        # in the list (backward direction)
        self.back = back_node

def convert_arr_to_dll(arr):
    # Create the head node with
    # the first element of the array
    head = Node(arr[0])
    # Initialize 'prev' to the head node
    prev = head

    for i in range(1, len(arr)):
        # Create a new node with data from the
        # array and set its 'back' pointer
        # to the previous node
        temp = Node(arr[i], None, prev)
        
        # Update the 'next' pointer of the
        # previous node to point to the new node
        prev.next = temp
        # Move 'prev' to the newly created 
        # node for the next iteration
        prev = temp

    # Return the head of the doubly linked list
    return head

def print_dll(head):
    while head is not None:
        # Print the data in the current node
        print(head.data, end=" ")
        # Move to the next node
        head = head.next
    print()


def reverse_dll(head):
    # If head is empty or there is only
    # one element, return the head directly
    if head is None or head.next is None:
        return head

    # Initialize a stack to store values
    st = []
    # Initialize the node pointer
    #'temp' at head
    temp = head

    # Traverse the doubly linked list
    # via the 'temp' pointer
    while temp is not None:
        # Insert the data of the current
        # node into the stack
        st.append(temp.data)
        # Traverse further
        temp = temp.next

    # Reinitialize 'temp' to head
    temp = head

    # Second iteration of the DLL
    # to replace the values
    while temp is not None:
        # Replace the value pointed to
        # by 'temp' with the value from
        # the top of the stack and pop it
        temp.data = st.pop()
        # Traverse further
        temp = temp.next

    # Return the updated doubly linked list
    # where the values of nodes from both
    # ends have been swapped
    return head


# Example usage:
arr = [12, 5, 6, 8, 4]
# Convert the array to a
# doubly linked list
head = convert_arr_to_dll(arr)
# Print the doubly linked list
print('Doubly Linked List Initially:  ')
print_dll(head)

print('Doubly Linked List After Reversing :')

# Reverse the doubly linked list
head = reverse_dll(head)
# Print the reversed doubly linked list
print_dll(head)




# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity : O(N) We only have to traverse the doubly linked list once, hence our time complexity is O(N).

Space Complexity : O(1), as the reversal is done in place.


class Node:
    def __init__(self, data, next_node=None, back_node=None):
        # Data stored in the node
        self.data = data
        # Reference to the next node
        # in the list (forward direction)
        self.next = next_node
        # Reference to the previous node
        # in the list (backward direction)
        self.back = back_node

def convert_arr_to_dll(arr):
    # Create the head node with
    # the first element of the array
    head = Node(arr[0])
    # Initialize 'prev' to the head node
    prev = head

    for i in range(1, len(arr)):
        # Create a new node with data from the
        # array and set its 'back' pointer
        # to the previous node
        temp = Node(arr[i], None, prev)
        
        # Update the 'next' pointer of the
        # previous node to point to the new node
        prev.next = temp
        # Move 'prev' to the newly created 
        # node for the next iteration
        prev = temp

    # Return the head of the doubly linked list
    return head

def print_dll(head):
    while head is not None:
        # Print the data in the current node
        print(head.data, end=" ")
        # Move to the next node
        head = head.next
    print()

def reverse_dll(head):
    # Check if the list is empty
    # or has only one node
    if head is None or head.next is None:
        # No change is needed;
        # return the current head
        return head
    
    # Initialize a pointer to
    # the previous node
    prev = None  
    
    # Initialize a pointer
    # to the current node
    current = head  

    # Traverse the linked list
    while current is not None:
        
        # Store a reference to
        # the previous node
        prev = current.back 

        # Swap the previous and next pointers
        current.back = current.next
        
         # This step reverses the links
        current.next = prev 
        
        # Move to the next node
        # in the original list
        current = current.back  

    # The final node in the original list
    # becomes the new head after reversal
    return prev.back

# Example usage:
arr = [12, 5, 6, 8, 4]
# Convert the array to a
# doubly linked list
head = convert_arr_to_dll(arr)
# Print the doubly linked list
print('Doubly Linked List Initially:  ')
print_dll(head)

print('Doubly Linked List After Reversing :')

# Reverse the doubly linked list
head = reverse_dll(head)
# Print the reversed doubly linked list
print_dll(head)





# endregion





# region 6.3 LINKED LIST - MEDIUM
# --------------------------------

# 1 TODO :  middle of a LL (Tortoise Hare method)
# method 1 : brute force approch
Time Complexity: O(N+N/2) The code traverses the entire linked list once and half times and then only half in the second iteration, first to count the number of nodes then then again to get to the middle node. Therefore, the time complexity is linear, O(N + N/2) ~ O(N).

Space Complexity : O(1) There is constant space complexity because it uses a constant amount of extra space regardless of the size of the linked list. We only use a few variables to keep track of the middle position and traverse the list, and the memory required for these variables does not depend on the size of the list.
                                
# Node class represents a node in 
# a linked list

class Node:
    def __init__(self, data, next_node=None):
        # Data stored in the node
        self.data = data       
        # Pointer to the next node in the list
        self.next = next_node  

# Function to find the middle 
# node of a linked list
def find_middle(head):
    # If the list is empty or has only 
    # one element, return the head
    # as it's the middle.
    if head is None or head.next is None:
        return head

    temp = head
    count = 0

    # Count the number of nodes
    # in the linked list.
    while temp is not None:
        count += 1
        temp = temp.next

    # Calculate the position of
    # the middle node.
    mid = count // 2 + 1
    temp = head

    # Traverse to the middle node by
    # moving temp to the middle position.
    while temp is not None:
        mid = mid -1

        # Check if the middle position is reached.
        if mid == 0:
           # break out of the loop
           # to return temp
            break
        
        # Move temp ahead
        temp = temp.next


    # Return the middle node.
    return temp

# Creating a sample linked list: 
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Find the middle node
middle_node = find_middle(head)

# Display the value of the middle node
print("The middle node value is:", middle_node.data)
                                
                            


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(N/2) The algorithm requires the 'fast' pointer to reach the end of the list which it does after approximately N/2 iterations (where N is the total number of nodes). Therefore, the maximum number of iterations needed to find the middle node is proportional to the number of nodes in the list, making the time complexity linear, or O(N/2) ~ O(N).

Space Complexity : O(1) There is constant space complexity because it uses a constant amount of extra space regardless of the size of the linked list. We only use a few variables to keep track of the middle position and traverse the list, and the memory required for these variables does not depend on the size of the list.
                                
                     
# Node class represents a node in 
# a linked list

class Node:
    def __init__(self, data, next_node=None):
        # Data stored in the node
        self.data = data       
        # Pointer to the next node in the list
        self.next = next_node  

# Function to find the middle 
# node of a linked list
def find_middle(head):
    # Initialize the slow pointer to the head.
    slow = head   
    
    # Initialize the fast pointer to the head.
    fast = head   

    # Traverse the linked list using
    # the Tortoise and Hare algorithm.
    while fast and fast.next and slow:
        # Move fast two steps.
        fast = fast.next.next 
        # Move slow one step.
        slow = slow.next       

    # Return the slow pointer,
    # which is now at the middle node.
    return slow  


# Creating a sample linked list: 
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Find the middle node
middle_node = find_middle(head)

# Display the value of the middle node
print("The middle node value is:", middle_node.data)
                                
                                


# 2 TODO : reverse a LL (itterative)
# method 1 : brute force approch
Time Complexity: O(2N) This is because we traverse the linked list twice: once to push the values onto the stack, and once to pop the values and update the linked list. Both traversals take O(N) time, hence time complexity  O(2N) ~ O(N).

Space Complexity: O(N) We use a stack to store the values of the linked list, and in the worst case, the stack will have all N values,  ie. storing the complete linked list. 


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

# Function to reverse the
# linked list using a stack
def reverse_linked_list(head):
    # Create a temporary pointer
    # to traverse the linked list
    temp = head  
    
    # Create a stack to temporarily
    # store the data values
    stack = []   

    # Step 1: Push the values of the
    # linked list onto the stack
    while temp is not None:
        # Push the current node's
        # data onto the stack
        stack.append(temp.data) 
        # Move to the next node
        # in the linked list
        temp = temp.next        

    # Reset the temporary pointer
    # to the head of the linked list
    temp = head  

    # Step 2: Pop values from the stack
    # and update the linked list
    while temp is not None:
        
        # Set the current node's data to
        # the value at the top of the stack
        temp.data = stack.pop()  
        
         # Move to the next node in
         # the linked list
        temp = temp.next        

    # Return the new head of
    # the reversed linked list
    return head  

# Function to print the linked list
def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()

# Create a linked list with
# values 1, 3, 2, and 4
head = Node(1)
head.next = Node(3)
head.next.next = Node(2)
head.next.next.next = Node(4)

# Print the original linked list
print("Original Linked List:", end=" ")
print_linked_list(head)

# Reverse the linked list
head = reverse_linked_list(head)

# Print the reversed linked list
print("Reversed Linked List:", end=" ")
print_linked_list(head)






# method 2 : better approch
Time Complexity: O(N) The code traverses the entire linked list once, where 'n' is the number of nodes in the list. This traversal has a linear time complexity, O(n).

Space Complexity: O(1) The code uses only a constant amount of additional space, regardless of the linked list's length. This is achieved by using three pointers (prev, temp and front) to reverse the list without any significant extra memory usage, resulting in constant space complexity, O(1).


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

# Function to reverse linked list
# using 3 pointer approach
def reverseLinkedList(head):
    
    # Initialize 'temp' at the
    # head of the linked list
    temp = head
    
    # Initialize 'prev' to None,
    # representing the previous node 
    prev = None
    
    while temp is not None:
        # Store the next node in 'front'
        # to preserve the reference
        front = temp.next
        # Reverse the direction of the current
        # node's 'next' pointer to point to 'prev'
        temp.next = prev
        # Move 'prev' to the current 
        # node, for the next iteration
        prev = temp
        # Move 'temp' to 'front' node
        # advancing traversal
        temp = front

    # Return the new head
    # of the reversed linked list
    return prev
    
# Function to print the linked list
def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()

# Create a linked list with
# values 1, 3, 2, and 4
head = Node(1)
head.next = Node(3)
head.next.next = Node(2)
head.next.next.next = Node(4)

# Print the original linked list
print("Original Linked List:", end=" ")
print_linked_list(head)

# Reverse the linked list
head = reverse_linked_list(head)

# Print the reversed linked list
print("Reversed Linked List:", end=" ")
print_linked_list(head)




# method 3 : optimal solution
Time Complexity: O(N) This is because we traverse the linked list twice: once to push the values onto the stack, and once to pop the values and update the linked list. Both traversals take O(N) time.

Space Complexity : O(1) No additional space is used explicitly for data structures or allocations during the linked list reversal process. However, it's important to note that there is an implicit use of stack space due to recursion. This recursive stack space stores function calls and associated variables during the recursive traversal and reversal of the linked list. Despite this, no extra memory beyond the program's existing execution space is allocated, hence maintaining a space complexity of O(1).


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

# Function to reverse a singly
# linked list using a recursion
def reverse_linked_list(head):
    # Base case:
    # If the linked list is empty or has only one node,
    # return the head as it is already reversed.
    if head is None or head.next is None:
        return head
    
    # Recursive step:
    # Reverse the linked list starting from the second node (head.next).
    new_head = reverse_linked_list(head.next)
    
    # Save a reference to the node following
    # the current 'head' node.
    front = head.next
    
    # Make the 'front' node point to the current
    # 'head' node in the reversed order.
    front.next = head
    
    # Break the link from the current 'head' node
    # to the 'front' node to avoid cycles.
    head.next = None
    
    # Return the 'new_head,' which is the new
    # head of the reversed linked list.
    return new_head


# Function to print the linked list
def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()

# Create a linked list with
# values 1, 3, 2, and 4
head = Node(1)
head.next = Node(3)
head.next.next = Node(2)
head.next.next.next = Node(4)

# Print the original linked list
print("Original Linked List:", end=" ")
print_linked_list(head)

# Reverse the linked list
head = reverse_linked_list(head)

# Print the reversed linked list
print("Reversed Linked List:", end=" ")
print_linked_list(head)





# 3 TODO : reverse a LL (recursive)
# method 1 : brute force approch
Time Complexity: O(2N) This is because we traverse the linked list twice: once to push the values onto the stack, and once to pop the values and update the linked list. Both traversals take O(N) time, hence time complexity  O(2N) ~ O(N).

Space Complexity: O(N) We use a stack to store the values of the linked list, and in the worst case, the stack will have all N values,  ie. storing the complete linked list. 


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

# Function to reverse the
# linked list using a stack
def reverse_linked_list(head):
    # Create a temporary pointer
    # to traverse the linked list
    temp = head  
    
    # Create a stack to temporarily
    # store the data values
    stack = []   

    # Step 1: Push the values of the
    # linked list onto the stack
    while temp is not None:
        # Push the current node's
        # data onto the stack
        stack.append(temp.data) 
        # Move to the next node
        # in the linked list
        temp = temp.next        

    # Reset the temporary pointer
    # to the head of the linked list
    temp = head  

    # Step 2: Pop values from the stack
    # and update the linked list
    while temp is not None:
        
        # Set the current node's data to
        # the value at the top of the stack
        temp.data = stack.pop()  
        
         # Move to the next node in
         # the linked list
        temp = temp.next        

    # Return the new head of
    # the reversed linked list
    return head  

# Function to print the linked list
def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()

# Create a linked list with
# values 1, 3, 2, and 4
head = Node(1)
head.next = Node(3)
head.next.next = Node(2)
head.next.next.next = Node(4)

# Print the original linked list
print("Original Linked List:", end=" ")
print_linked_list(head)

# Reverse the linked list
head = reverse_linked_list(head)

# Print the reversed linked list
print("Reversed Linked List:", end=" ")
print_linked_list(head)






# method 2 : better approch
Time Complexity: O(N) The code traverses the entire linked list once, where 'n' is the number of nodes in the list. This traversal has a linear time complexity, O(n).

Space Complexity: O(1) The code uses only a constant amount of additional space, regardless of the linked list's length. This is achieved by using three pointers (prev, temp and front) to reverse the list without any significant extra memory usage, resulting in constant space complexity, O(1).


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

# Function to reverse linked list
# using 3 pointer approach
def reverseLinkedList(head):
    
    # Initialize 'temp' at the
    # head of the linked list
    temp = head
    
    # Initialize 'prev' to None,
    # representing the previous node 
    prev = None
    
    while temp is not None:
        # Store the next node in 'front'
        # to preserve the reference
        front = temp.next
        # Reverse the direction of the current
        # node's 'next' pointer to point to 'prev'
        temp.next = prev
        # Move 'prev' to the current 
        # node, for the next iteration
        prev = temp
        # Move 'temp' to 'front' node
        # advancing traversal
        temp = front

    # Return the new head
    # of the reversed linked list
    return prev
    
# Function to print the linked list
def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()

# Create a linked list with
# values 1, 3, 2, and 4
head = Node(1)
head.next = Node(3)
head.next.next = Node(2)
head.next.next.next = Node(4)

# Print the original linked list
print("Original Linked List:", end=" ")
print_linked_list(head)

# Reverse the linked list
head = reverse_linked_list(head)

# Print the reversed linked list
print("Reversed Linked List:", end=" ")
print_linked_list(head)





# method 3 : optimal solution
Time Complexity: O(N) This is because we traverse the linked list twice: once to push the values onto the stack, and once to pop the values and update the linked list. Both traversals take O(N) time.

Space Complexity : O(1) No additional space is used explicitly for data structures or allocations during the linked list reversal process. However, it's important to note that there is an implicit use of stack space due to recursion. This recursive stack space stores function calls and associated variables during the recursive traversal and reversal of the linked list. Despite this, no extra memory beyond the program's existing execution space is allocated, hence maintaining a space complexity of O(1).


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

# Function to reverse a singly
# linked list using a recursion
def reverse_linked_list(head):
    # Base case:
    # If the linked list is empty or has only one node,
    # return the head as it is already reversed.
    if head is None or head.next is None:
        return head
    
    # Recursive step:
    # Reverse the linked list starting from the second node (head.next).
    new_head = reverse_linked_list(head.next)
    
    # Save a reference to the node following
    # the current 'head' node.
    front = head.next
    
    # Make the 'front' node point to the current
    # 'head' node in the reversed order.
    front.next = head
    
    # Break the link from the current 'head' node
    # to the 'front' node to avoid cycles.
    head.next = None
    
    # Return the 'new_head,' which is the new
    # head of the reversed linked list.
    return new_head


# Function to print the linked list
def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()

# Create a linked list with
# values 1, 3, 2, and 4
head = Node(1)
head.next = Node(3)
head.next.next = Node(2)
head.next.next.next = Node(4)

# Print the original linked list
print("Original Linked List:", end=" ")
print_linked_list(head)

# Reverse the linked list
head = reverse_linked_list(head)

# Print the reversed linked list
print("Reversed Linked List:", end=" ")
print_linked_list(head)





# 4 TODO : detect a loop in Ll
# method 1 : brute force approch
Time Complexity: O(N * 2 * log(N) )The algorithm traverses the linked list once, performing hashmap insertions and searches in the while loop for each node. The insertion and search operations in the unordered_map have a worst-case time complexity of O(log(N)). As the loop iterates through N nodes, the total time complexity is determined by the product of the traversal (O(N)) and the average-case complexity of the hashmap operations (insert and search), resulting in O(N * 2 * log(N)). 

Hashmaps and their time complexities are discussed in more detail here. 

Space Complexity: O(N) The code uses a hashmap/dictionary to store encountered nodes, which can take up to O(N) additional space, where 'n' is the number of nodes in the list. Hence, the spacecomplexity is O(N) due to the use of the map to track nodes.

# Node class represents
# a node in a linked list
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

# Function to detect a loop 
# n a linked list
def detect_loop(head):
    # Initialize a pointer 'temp' at 
    # the head of the linked list
    temp = head

    # Create a set to keep track
    # of encountered nodes
    node_set = set()

    # Step 2: Traverse the linked list
    while temp is not None:
        # If the node is already
        # in the set, there is a loop
        if temp in node_set:
            return True

        # Store the current node in the set
        node_set.add(temp)

        # Move to the next node
        temp = temp.next

    # Step 3: If the list is successfully
    # traversed without a loop, return False
    return False

if __name__ == "__main__":
    # Create a sample linked list with
    # a loop for testing
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    # Create a loop
    fifth.next = third

    # Check if there is a loop
    # in the linked list
    if detect_loop(head):
        print("Loop detected in the linked list.")
    else:
        print("No loop detected in the linked list.")

    # No need to explicitly free memory
    # in Python; memory management is automatic





# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(N), where N is the number of nodes in the linked list. This is because in the worst-case scenario, the fast pointer, which moves quicker, will either reach the end of the list (in case of no loop) or meet the slow pointer (in case of a loop) in a linear time relative to the length of the list.

The key insight into why this is O(N) and not something slower is that each step of the algorithm reduces the distance between the fast and slow pointers (when they are in the loop) by one. Therefore, the maximum number of steps needed for them to meet is proportional to the number of nodes in the list.


Space Complexity : O(1) The code uses only a constantamount of additionalspace, regardless of the linked list's length. This is achieved by using two pointers (slow and fast) to detect the loop without any significant extra memory usage, resulting in constantspace complexity, O(1).

# Node class represents
# a node in a linked list
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

# Function to detect a loop in a
# linked list using the Tortoise and Hare Algorithm
def detect_cycle(head):
    # Initialize two pointers, slow and fast,
    # to the head of the linked list
    slow = head
    fast = head

    # Step 2: Traverse the linked list
    # with the slow and fast pointers
    while fast is not None and fast.next is not None:
        # Move slow one step
        slow = slow.next
        # Move fast two steps
        fast = fast.next.next

        # Check if slow and fast pointers meet
        if slow == fast:
            return True  # Loop detected

    # If fast reaches the end of the
    # list, there is no loop
    return False


if __name__ == "__main__":
    # Create a sample linked list with
    # a loop for testing
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    # Create a loop
    fifth.next = third

    # Check if there is a loop
    # in the linked list
    if detect_cycle(head):
        print("Loop detected in the linked list.")
    else:
        print("No loop detected in the linked list.")

    # No need to explicitly free memory
    # in Python; memory management is automatic




# 5 TODO : find the starting point in LL
# method 1 : brute force approch
Time Complexity: O(N) The code traverses the entire linked list once, where 'N' is the number of nodes in the list. Therefore, the time complexity is linear, O(N).

Space Complexity : O(N) The code uses a hash map/dictionary to store encountered nodes, which can take up to O(N) additional space, where 'n' is the number of nodes in the list. Hence, the space complexity is O(N) due to the use of the map to track nodes.
                                
# Node class represents a node in a linked list
class Node:
    def __init__(self, data, next_node=None):
        # Data stored in the node
        self.data = data  
         # Pointer to the next node in the list
        self.next = next_node 

# Function to detect a loop in a linked list
# and return the starting node of the loop
def detect_loop(head):
    # Use temp to traverse the linked list
    temp = head
    
    # Dictionary to store all visited nodes
    node_map = {}
    
    # Traverse the list using temp
    while temp is not None:
        # Check if temp has been encountered again
        if temp in node_map:
            # A loop is detected, hence return temp
            return temp
        
        # Store temp as visited
        node_map[temp] = True
        
        # Iterate through the list
        temp = temp.next

    # If no loop is detected, return None
    return None

# Create a sample linked list with a loop
node1 = Node(1)
node2 = Node(2)
node1.next = node2
node3 = Node(3)
node2.next = node3
node4 = Node(4)
node3.next = node4
node5 = Node(5)
node4.next = node5

# Make a loop from node5 to node2
node5.next = node2

# Set the head of the linked list
head = node1

# Detect the loop in the linked list
loop_start_node = detect_loop(head)

if loop_start_node:
    print("Loop detected. Starting node of the loop is:", loop_start_node.data)
else:
    print("No loop detected in the linked list.")
                                
                              


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(N) The code traverses the entire linked list once, where 'n' is the number of nodes in the list. This traversal has a linear time complexity, O(n).

Space Complexity : O(1) The code uses only a constant amount of additional space, regardless of the linked list's length. This is achieved by using two pointers (slow and fast) to detect the loop without any significant extra memory usage, resulting in constant space complexity, O(1).
                                
                     
# Node class represents a
# node in a linked list
class Node:
    def __init__(self, data, next_node=None):
        # Data stored in the node
        self.data = data  
        # Pointer to the next node in the list
        self.next = next_node  

# Function to find the first
# node of the loop in a linked list
def first_node(head):
    # Initialize a slow and fast
    # pointers to the head of the list
    slow = head
    fast = head

    # Phase 1: Detect the loop
    while fast is not None and fast.next is not None:
        # Move slow one step
        slow = slow.next

        # Move fast two steps
        fast = fast.next.next

        # If slow and fast meet,
        # a loop is detected
        if slow == fast:
            # Reset the slow pointer
            # to the head of the list
            slow = head

            # Phase 2: Find the first
            # node of the loop
            while slow != fast:
                # Move slow and fast one
                # step at a time
                slow = slow.next
                fast = fast.next

                # When slow and fast meet again,
                # it's the first node of the loop
            return slow

    # If no loop is found, return None
    return None
    
# with a loop
node1 = Node(1)
node2 = Node(2)
node1.next = node2
node3 = Node(3)
node2.next = node3
node4 = Node(4)
node3.next = node4
node5 = Node(5)
node4.next = node5

# Make a loop from node5 to node2
node5.next = node2

# Set the head of the linked list
head = node1

# Detect the loop in the linked list
loop_start_node = first_node(head)

if loop_start_node:
    print("Loop detected. Starting node of the loop is:", loop_start_node.data)
else:
    print("No loop detected in the linked list.")
                                
                               


# 6 TODO : length of a loop in LL
# method 1 : brute force approch
Time Complexity: O(N) The code traverses the entire linked list at least once, where 'N' is the number of nodes in the list. Therefore, the time complexity is linear, O(N).

Space Complexity: O(N) The code uses a hashmap/dictionary to store encountered nodes, which can take up to O(N) additional space, where ‘N' is the number of nodes in the list. Hence, the space complexity is O(N) due to the use of the map to track nodes.


class Node:
    def __init__(self, data1, next1=None):
        # Data stored in the node
        self.data = data1
        # Pointer to the next node
        # in the list
        self.next = next1
        
# Function to return the lenght
# of loop when slow and fast are
# on the same node
def find_length(slow, fast):
    
    # count to keep track of 
    # nodes encountered in loop
    cnt = 1
    
    # move fast by one step
    fast = fast.next
    
    # traverse fast till it 
    # reaches back to slow
    while slow != fast:
        
        # at each node increase
        # count by 1 and move fast
        # forward by one step
        
        cnt += 1
        fast = fast.next
    
    # loop terminates when fast reaches
    # slow again and the count is returned
    return cnt
    
# Function to find the length
# of the loop in a linked list
def length_of_loop(head):
    slow = head
    fast = head
    
    # Step 1: Traverse the list to detect a loop
    while fast is not None and fast.next is not None:
        # Move slow one step
        slow = slow.next
        # Move fast two steps
        fast = fast.next.next
        
        # Step 2: If the slow and fast pointers
        # meet, there is a loop
        if slow == fast:
            
            # return the number of nodes
            # in the loop
            return find_length(slow, fast)
    
    return 0


# Create a linked list with a loop
head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)

# Create a loop from fifth to second
head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

# This creates a loop
fifth.next = second

loopLength = length_of_loop(head)

if loopLength > 0:
    print("Length of the loop:", loopLength)
else:
    print("No loop found in the linked list.")





# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(N) The code traverses the entire linked list once, where 'n' is the number of nodes in the list. This traversal has a linear time complexity, O(n).

Space Complexity: O(1) The code uses only a constant amount of additional space, regardless of the linked list's length. This is achieved by using two pointers (slow and fast) to detect the loop without any significant extra memory usage, resulting in constant space complexity, O(1).

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# Function to detect a loop in a
# linked list using the Tortoise and Hare Algorithm

def detect_loop(head):
    # Initialize the slow pointer at the head
    slow = head  
    
     # Initialize the fast pointer at the head
    fast = head 

    # Step 1: Traverse the list to detect a loop
    while fast is not None and fast.next is not None:
        # Move slow one step
        slow = slow.next  
        # Move fast two steps
        fast = fast.next.next  

        # Step 2: If the slow and fast
        # pointers meet, there is a loop
        if slow == fast:
            return True

    # Step 3: If the fast pointer
    # reaches the end, there is no loop
    return False

# Function to find the length
# of the loop in a linked list
def find_loop_length(head):
    slow = head
    fast = head

    # Step 1: Traverse the list to detect a loop
    while fast is not None and fast.next is not None:
        # Move slow one step
        slow = slow.next     
        # Move fast two steps
        fast = fast.next.next  

        # Step 2: If the slow and fast
        # pointers meet, there is a loop
        if slow == fast:
            # Initialize the loop length
            length = 1  
             # Move fast one step
            fast = fast.next 

            # Step 4: Initialize a counter
            # and traverse using the fast pointer
            while slow != fast:
                # Move fast one step
                fast = fast.next  
                # Increment the counter
                length += 1  

            # Step 6: Return the 
            # length of the loop
            return length

    # Step 3: If the fast pointer
    # reaches the end, there is no loop
    return 0  

# Create a linked list with a loop for testing
head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node3  # Creating a loop

# Check if there is a loop in the linked list
if detect_loop(head):
    # If there is a loop, find its length
    length = find_loop_length(head)
    print(f"The length of the loop is: {length}")
else:
    print("No loop found in the linked list.")



# 7 TODO : check if LL is pallindrome or not
# method 1 : brute force approch
Time Complexity: O(2 * N) This is because we traverse the linked list twice: once to push the values onto the stack, and once to pop the values and compare with the linked list. Both traversals take O(2*N) ~ O(N) time.

Space Complexity: O(N) We use a stack to store the values of the linked list, and in the worst case, the stack will have all N values,  ie. storing the complete linked list. 

from collections import deque

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


def isPalindrome(head):
    # Create an empty deque
    # to store values
    st = deque()

    # Initialize a temporary pointer
    # to the head of the linked list
    temp = head

    # Traverse the linked list and
    # push values onto the deque
    while temp is not None:
        # Push the data from the
        # current node onto the deque
        st.append(temp.data)

        # Move to the next node
        temp = temp.next

    # Reset the temporary pointer back
    # to the head of the linked list
    temp = head

    # Compare values by popping from the deque
    # and checking against linked list nodes
    while temp is not None:
        if temp.data != st.pop():
            # If values don't match,
            # it's not a palindrome
            return False

        # Move to the next node
        # in the linked list
        temp = temp.next

    # If all values match,
    # it's a palindrome
    return True

    
# Function to print the linked list
def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()

def main():
    # Create a linked list with
    # values 1, 5, 2, 5, and 1 (15251, a palindrome)
    head = Node(1)
    head.next = Node(5)
    head.next.next = Node(2)
    head.next.next.next = Node(5)
    head.next.next.next.next = Node(1)

    # Print the original linked list
    print("Original Linked List: ", end="")
    print_linked_list(head)

    # Check if the linked list is a palindrome
    if is_palindrome(head):
        print("The linked list is a palindrome.")
    else:
        print("The linked list is not a palindrome.")

if __name__ == "__main__":
    main()





# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O (2* N) The algorithm traverses the linked list twice, dividing it into halves. During the first traversal, it reverses one-half of the list, and during the second traversal, it compares the elements of both halves. As each traversal covers N/2 elements, the time complexity is calculated as O(N/2 + N/2 + N/2 + N/2), which simplifies to O(2N), ultimately representing O(N). 

Space Complexity: O(1) The approach uses a constant amount of additional space regardless of the size of the input linked list. It doesn't allocate any new data structures that depend on the input size, resulting in a space complexity of O(1).

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

# Function to reverse linked list
# using recursion approach
def reverse_linked_list(head):
    # Check if the list is empty
    # or has only one node
    if head is None or head.next is None:
        
        # No change is needed;
        # return the current head
        return head

    # Recursive step: Reverse the remaining part
    # of the list and obtain the new head
    new_head = reverse_linked_list(head.next)

    # Store the next node in 'front' to reverse the link
    front = head.next

    # Update the 'next' pointer of 'front' to 
    # point to the current head, effectively
    # reversing the link direction
    front.next = head

    # Set the 'next' pointer of the current
    # head to 'None' to break the original link
    head.next = None

    # Return the new head obtained
    # from the recursion
    return new_head
    
def is_palindrome(head):
    # Check if the linked list is empty
    # or has only one node
    if head is None or head.next is None:
        # It's a palindrome by definition
        return True

    # Initialize two pointers, slow and fast,
    # to find the middle of the linked list
    slow = head
    fast = head

    # Traverse the linked list to find the
    # middle using slow and fast pointers
    while fast.next is not None and fast.next.next is not None:
        # Move slow pointer one step at a time
        slow = slow.next

        # Move fast pointer two steps at a time
        fast = fast.next.next

    # Reverse the second half of the
    # linked list starting from the middle
    new_head = reverse_linked_list(slow.next)

    # Pointer to the first half
    first = head

    # Pointer to the reversed second half
    second = new_head
    while second is not None:
        # Compare data values of
        # nodes from both halves

        # If values do not match,
        # the list is not a palindrome
        if first.data != second.data:
            # Reverse the second half
            # back to its original state
            reverse_linked_list(new_head)
            # Not a palindrome
            return False

        # Move the first pointer
        first = first.next

        # Move the second pointer
        second = second.next

    # Reverse the second half
    # back to its original state
    reverse_linked_list(new_head)

    # The linked list is a palindrome
    return True
    
# Function to print the linked list
def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()

def main():
    # Create a linked list with
    # values 1, 5, 2, 5, and 1 (15251, a palindrome)
    head = Node(1)
    head.next = Node(5)
    head.next.next = Node(2)
    head.next.next.next = Node(5)
    head.next.next.next.next = Node(1)

    # Print the original linked list
    print("Original Linked List: ", end="")
    print_linked_list(head)

    # Check if the linked list is a palindrome
    if is_palindrome(head):
        print("The linked list is a palindrome.")
    else:
        print("The linked list is not a palindrome.")

if __name__ == "__main__":
    main()




# 8 TODO : segrregate odd and even nodes in a LL
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 9 TODO : remove Nth node from end/back of LL
# method 1 : brute force approch
Time Complexity: O(L)+O(L-N), We are calculating the length of the linked list and then iterating up to the (L-N)th node of the linked list, where L is the total length of the list.

Space Complexity:  O(1), as we have not used any extra space.


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

# Function to print the linked list
def printLL(head):
    while head is not None:
        print(head.data, end=' ')
        head = head.next

# Function to delete the Nth node from the end of the linked list
def DeleteNthNodefromEnd(head, N):
    if head is None:
        return None
    cnt = 0
    temp = head

    # Count the number of nodes in the linked list
    while temp is not None:
        cnt += 1
        temp = temp.next

    # If N equals the total number of nodes, delete the head
    if cnt == N:
        newhead = head.next
        head = None
        return newhead

    # Calculate the position of the node to delete (res)
    res = cnt - N
    temp = head

    # Traverse to the node just before the one to delete
    while temp is not None:
        res -= 1
        if res == 0:
            break
        temp = temp.next

    # Delete the Nth node from the end
    delNode = temp.next
    temp.next = temp.next.next
    delNode = None
    return head

arr = [1, 2, 3, 4, 5]
N = 3
head = Node(arr[0])
head.next = Node(arr[1])
head.next.next = Node(arr[2])
head.next.next.next = Node(arr[3])
head.next.next.next.next = Node(arr[4])

# Delete the Nth node from the end and print the modified linked list
head = DeleteNthNodefromEnd(head, N)
printLL(head)





# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(N) since the fast pointer will traverse the entire linked list, where N is the length of the linked list.

Space Complexity: O(1), as we have not used any extra space.

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

# Function to print the linked list
def printLL(head):
    while head is not None:
        print(head.data, end=' ')
        head = head.next

# Function to delete the Nth node from the end of the linked list
def DeleteNthNodefromEnd(head, N):
    # Create two pointers, fastp and slowp
    fastp = head
    slowp = head

    # Move the fastp pointer N nodes ahead
    for i in range(N):
        fastp = fastp.next

    # If fastp becomes None, the Nth node from the end is the head
    if fastp is None:
        return head.next

    # Move both pointers until fastp reaches the end
    while fastp.next is not None:
        fastp = fastp.next
        slowp = slowp.next

    # Delete the Nth node from the end
    delNode = slowp.next
    slowp.next = slowp.next.next
    delNode = None
    return head

arr = [1, 2, 3, 4, 5]
N = 3
head = Node(arr[0])
head.next = Node(arr[1])
head.next.next = Node(arr[2])
head.next.next.next = Node(arr[3])
head.next.next.next.next = Node(arr[4])

# Delete the Nth node from the end and print the modified linked list
head = DeleteNthNodefromEnd(head, N)
printLL(head)




# 10 TODO :  delete the middle node of a LL
# method 1 : brute force approch
Time Complexity: O(N + N/2) The loop traverses the entire linked list once to count the total number of nodes then the loop iterates halfway through the linked list to reach the middle node. Hence, the time complexity is O(N + N/2) ~ O(N).

Space Complexity : O(1) The algorithm uses a constant amount of extra space regardless of the size of the input (linked list). It doesn't use any additional data structures in proportion to the input size. Thus, the space complexity is O(1) (constant space). 

# Node class represents a node in 
# a linked list

class Node:
    def __init__(self, data, next_node=None):
        # Data stored in the node
        self.data = data       
        # Pointer to the next node in the list
        self.next = next_node  

# Function to delete the
# middle node of a linked list
def delete_middle(head):
    # Initialize a temporary node
    # to traverse the linked list
    temp = head
    
    # Variable to hold the number
    # of nodes in the linked list
    n = 0
    
    # Loop to count the number of
    # nodes in the linked list
    while temp is not None:
        n += 1
        temp = temp.next
    
    # Calculate the index of the middle node
    res = n // 2
    
    # Reset the temporary node to
    # the beginning of the linked list
    temp = head
    
    # Loop to find the
    # middle node to delete
    while temp is not None:
        res -= 1
        
        # If the middle node is found
        if res == 0:
            
            # Create a pointer
            # to the middle node
            middle = temp.next
            
            # Adjust pointers to
            # skip the middle node
            temp.next = temp.next.next
            
            # Delete the middle node
            # (Python handles memory management)
            # No explicit free() needed
            
            # Exit the loop after
            # deleting the middle node
            break
        
        # Move to the next node
        # in the linked list
        temp = temp.next
    
    # Return the head of the
    # modified linked list
    return head


def print_linked_list(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()

# Creating a sample linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Display the original linked list
print("Original Linked List: ", end="")
print_linked_list(head)

# Deleting the middle node
head = delete_middle(head)

# Displaying the updated linked list
print("Updated Linked List: ", end="")
print_linked_list(head)




# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(N/2) The algorithm traverses the linked list using the Tortoise and Hare approach. The code increments both 'slow' and 'fast' pointers at different rates, effectively covering about half the list before reaching the midpoint, hence the time complexity of the algorithm is O(N/2) ~ O(N).

Space Complexity: O(1) The algorithm uses a constant amount of extra space regardless of the size of the input (linked list). It doesn't use any additional data structures in proportion to the input size. Thus, the space complexity is O(1) (constant space). 

# Node class represents a node in 
# a linked list

class Node:
    def __init__(self, data, next_node=None):
        # Data stored in the node
        self.data = data       
        # Pointer to the next node in the list
        self.next = next_node  

# Function to delete the middle
# node of a linked list
def delete_middle(head):
    """
    If the list is empty or has only one node,
    return None as there is no middle node to delete
    """
    if head is None or head.next is None:
        return None

    # Initialize slow and fast pointers
    slow = head
    fast = head.next.next if head.next else None

    # Move 'fast' pointer twice as fast as 'slow'
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Delete the middle node by skipping it
    slow.next = slow.next.next
    return head

def print_linked_list(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()

# Creating a sample linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Display the original linked list
print("Original Linked List: ", end="")
print_linked_list(head)

# Deleting the middle node
head = delete_middle(head)

# Displaying the updated linked list
print("Updated Linked List: ", end="")
print_linked_list(head)




# 11 TODO : sort LL
# method 1 : brute force approch
Time Complexity: O(N) + O(N log N) + O(N)where N is the number of nodes in the linked list.

O(N) to traverse the linked list and store its data values in an additional array.
O(N log N) to sort the array containing the node values.
O(N) to traverse the sorted array and convert it into a new linked list.
Space Complexity : O(N)where N is the number of nodes in the linked list as we have to store the values of all nodes in the linked list in an additional array to sort them.
                                
# Node class represents a
# node in a linked list
class Node:
    def __init__(self, data, next_node=None):
        # Data stored in the node
        self.data = data
        # Pointer to the next node in the list
        self.next = next_node


# Function to sort a linked list
# using Brute Force approach
def sort_LL(head):
    # Create a list to
    # store node values
    arr = []
    
    # Temporary pointer to
    # traverse the linked list
    temp = head
    
    # Traverse the linked list and
    # store node values in the list
    while temp is not None:
        arr.append(temp.data)
        temp = temp.next
    
    # Sort the list
    # containing node values
    arr.sort()
    
    # Reassign sorted values to
    # the linked list nodes
    temp = head
    for i in range(len(arr)):
        # Update the node's data
        # with the sorted values
        temp.data = arr[i]
        # Move to the next node
        temp = temp.next
    
    # Return the head of the
    # sorted linked list
    return head


# Function to print the linked list
def print_linked_list(head):
    temp = head
    while temp is not None:
        # Print the data of the current node
        print(temp.data, end=" ")
        # Move to the next node
        temp = temp.next
    print()


# Linked List: 3 2 5 4 1
head = Node(3)
head.next = Node(2)
head.next.next = Node(5)
head.next.next.next = Node(4)
head.next.next.next.next = Node(1)

print("Original Linked List: ", end="")
print_linked_list(head)

# Sort the linked list
head = sort_LL(head)

print("Sorted Linked List: ", end="")
print_linked_list(head)
                                
                             


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(N log N)where N is the number of nodes in the linked list. Finding the middle node of the linked list requires traversing it linearly taking O(N) time complexity and to reach the individual nodes of the list, it has to be split log N times (continuously halve the list until we have individual elements).

Space Complexity : O(1) as no additional data structures or space is allocated for storage during the merging process. However, space proportional to O(log N) stack space is required for the recursive calls. THe maximum recursion depth of log N height is occupied on the call stack.

                                
                     
# Node class represents a
# node in a linked list
class Node:
    def __init__(self, data1, next1=None):
        # Data stored in the node
        self.data = data1
        
        # Pointer to the next node in the list
        self.next = next1

# Function to merge two sorted linked lists
def mergeTwoSortedLinkedLists(list1, list2):
    # Create a dummy node to serve
    # as the head of the merged list
    dummyNode = Node(-1)
    temp = dummyNode

    # Traverse both lists simultaneously
    while list1 is not None and list2 is not None:
        # Compare elements of both lists and
        # link the smaller node to the merged list
        if list1.data <= list2.data:
            temp.next = list1
            list1 = list1.next
        else:
            temp.next = list2
            list2 = list2.next
        # Move the temporary pointer
        # to the next node
        temp = temp.next 

    # If any list still has remaining
    # elements, append them to the merged list
    if list1 is not None:
        temp.next = list1
    else:
        temp.next = list2
    
    # Return the merged list starting 
    # from the next of the dummy node
    return dummyNode.next

# Function to find the middle of a linked list
def findMiddle(head):
    # If the list is empty or has only one node
    # the middle is the head itself
    if head is None or head.next is None:
        return head

    # Initializing slow and fast pointers
    slow = head
    fast = head.next

    # Move the fast pointer twice as
    # fast as the slow pointer

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        
    # When the fast pointer reaches the end,
    # the slow pointer will be at the middle

    return slow

# Function to perform merge sort on a linked list
def sortLL(head):
    # Base case: if the list is empty
    # or has only one node it is already 
    # sorted, so return the head
    if head is None or head.next is None:
        return head

    # Find the middle of the list
    # using the findMiddle function
    middle = findMiddle(head)

    # Divide the list into two halves
    right = middle.next
    middle.next = None
    left = head

    # Recursively sort the left and right halves
    left = sortLL(left)
    right = sortLL(right)

    # Merge the sorted halves using
    # the mergeTwoSortedLinkedLists function
    return mergeTwoSortedLinkedLists(left, right)

# Function to print the linked list
def printLinkedList(head):
    temp = head
    while temp is not None:
        # Print the data of the current node
        print(temp.data, end=" ")
        # Move to the next node
        temp = temp.next
    print()

# Linked List: 3 2 5 4 1
head = Node(3)
head.next = Node(2)
head.next.next = Node(5)
head.next.next.next = Node(4)
head.next.next.next.next = Node(1)

print("Original Linked List: ", end="")
printLinkedList(head)

# Sort the linked list
head = sortLL(head)

print("Sorted Linked List: ", end="")
printLinkedList(head)
    


# 12 TODO : sort a LL of 0's, 1's and 2's by changing links

                                
                            


# 13 TODO : find the intersection points of Y LL
# method 1 : brute force approch
Time Complexity: O(m*n)

Reason: For each node in list 2 entire list 1 is iterated. 

Space Complexity: O(1)

Reason: No extra space is used.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None




# utility function to insert node at the end of the linked list
def insertNode(head, val):
    newNode = Node(val)
    if head == None:
        head = newNode
        return head
    temp = head
    while temp.next != None:
        temp = temp.next
    temp.next = newNode
    return head




# utility function to check presence of intersection
def intersectionPresent(head1, head2):
    while head2 != None:
        temp = head1
        while temp != None:
            # if both nodes are same
            if temp == head2:
                return head2
            temp = temp.next
        head2 = head2.next
    # intersection is not present between the lists
    return None




# utility function to print linked list created
def printList(head):
    while head.next != None:
        print(head.val, end='->')
        head = head.next
    print(head.val)




if __name__ == '__main__':
    head = None
    head = insertNode(head, 1)
    head = insertNode(head, 3)
    head = insertNode(head, 1)
    head = insertNode(head, 2)
    head = insertNode(head, 4)
    head1 = head
    head = head.next.next.next
    headSec = None
    headSec = insertNode(headSec, 3)
    head2 = headSec
    headSec.next = head
    print('List1: ', end='')
    printList(head1)
    print('List2: ', end='')
    printList(head2)
    answerNode = intersectionPresent(head1, head2)
    if answerNode == None:
        print('No intersection')
    else:
        print('The intersection point is', answerNode.val) 


# method 2 : better approch
Time Complexity: O(n+m)

Reason: Iterating through list 1 first takes O(n), then iterating through list 2 takes O(m). 

Space Complexity: O(n)

Reason: Storing list 1 node addresses in unordered_set.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None




# utility function to insert node at the end of the linked list
def insertNode(head, val):
    newNode = Node(val)
    if head == None:
        head = newNode
        return head
    temp = head
    while temp.next != None:
        temp = temp.next
    temp.next = newNode
    return head




# utility function to check presence of intersection
def intersectionPresent(head1, head2):
    st = set()
    while head1 != None:
        st.add(head1)
        head1 = head1.next
    while head2 != None:
        if head2 in st:
            return head2
        head2 = head2.next
    return None




# utility function to print linked list created
def printList(head):
    while head.next != None:
        print(head.val, end='->')
        head = head.next
    print(head.val)




if __name__ == '__main__':
    head = None
    head = insertNode(head, 1)
    head = insertNode(head, 3)
    head = insertNode(head, 1)
    head = insertNode(head, 2)
    head = insertNode(head, 4)
    head1 = head
    head = head.next.next.next
    headSec = None
    headSec = insertNode(headSec, 3)
    head2 = headSec
    headSec.next = head
    print('List1: ', end='')
    printList(head1)
    print('List2: ', end='')
    printList(head2)
    answerNode = intersectionPresent(head1, head2)
    if answerNode == None:
        print('No intersection')
    else:
        print('The intersection point is', answerNode.val)


# method 3 : optimal solution
Time Complexity:

O(2max(length of list1,length of list2))+O(abs(length of list1-length of list2))+O(min(length of list1,length of list2))

Reason: Finding the length of both lists takes max(length of list1, length of list2) because it is found simultaneously for both of them. Moving the head pointer ahead by a difference of them. The next one is for searching.

Space Complexity: O(1)

Reason: No extra space is used.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None




# utility function to insert node at the end of the linked list
def insertNode(head, val):
    newNode = Node(val)
    if head == None:
        head = newNode
        return head
    temp = head
    while temp.next != None:
        temp = temp.next
    temp.next = newNode
    return head




def getDifference(head1, head2):
    len1 = 0
    len2 = 0
    while head1 != None or head2 != None:
        if head1 != None:
            len1 += 1
            head1 = head1.next
        if head2 != None:
            len2 += 1
            head2 = head2.next
    # if difference is neg-> length of list2 > length of list1 else vice-versa
    return len1 - len2




# utility function to check presence of intersection
def intersectionPresent(head1, head2):
    diff = getDifference(head1, head2)
    if diff < 0:
        while diff != 0:
            head2 = head2.next
            diff += 1
    else:
        while diff != 0:
            head1 = head1.next
            diff -= 1
    while head1 != None:
        if head1 == head2:
            return head1
        head2 = head2.next
        head1 = head1.next
    return head1




# utility function to print linked list created
def printList(head):
    while head.next != None:
        print(head.val, end='->')
        head = head.next
    print(head.val)




if __name__ == '__main__':
    head = None
    head = insertNode(head, 1)
    head = insertNode(head, 3)
    head = insertNode(head, 1)
    head = insertNode(head, 2)
    head = insertNode(head, 4)
    head1 = head
    head = head.next.next.next
    headSec = None
    headSec = insertNode(headSec, 3)
    head2 = headSec
    headSec.next = head
    print('List1: ', end='')
    printList(head1)
    print('List2: ', end='')
    printList(head2)
    answerNode = intersectionPresent(head1, head2)
    if answerNode == None:
        print('No intersection')
    else:
        print('The intersection point is', answerNode.val)

# method 4 optimized
Time Complexity: O(2*max(length of list1,length of list2))

Reason: Uses the same concept of difference of lengths of two lists.

Space Complexity: O(1)

Reason: No extra data structure is used
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None




# utility function to insert node at the end of the linked list
def insertNode(head, val):
    newNode = Node(val)
    if head == None:
        head = newNode
        return head
    temp = head
    while temp.next != None:
        temp = temp.next
    temp.next = newNode
    return head




# utility function to check presence of intersection
def intersectionPresent(head1, head2):
    d1 = head1
    d2 = head2
    while d1 != d2:
        d1 = head2 if d1 == None else d1.next
        d2 = head1 if d2 == None else d2.next
    return d1




# utility function to print linked list created
def printList(head):
    while head.next != None:
        print(head.val, end='->')
        head = head.next
    print(head.val)




if __name__ == '__main__':
    head = None
    head = insertNode(head, 1)
    head = insertNode(head, 3)
    head = insertNode(head, 1)
    head = insertNode(head, 2)
    head = insertNode(head, 4)
    head1 = head
    head = head.next.next.next
    headSec = None
    headSec = insertNode(headSec, 3)
    head2 = headSec
    headSec.next = head
    print('List1: ', end='')
    printList(head1)
    print('List2: ', end='')
    printList(head2)
    answerNode = intersectionPresent(head1, head2)
    if answerNode == None:
        print('No intersection')
    else:
        print('The intersection point is', answerNode.val)



# 14 TODO : add 1 to a number represented by LL
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 15 TODO :add 2 numbers in LL
# method 1 : brute force approch
Time Complexity: O(max(m,n)). Assume that m and n represent the length of l1 and l2 respectively, the algorithm above iterates at most max(m,n) times.

Space Complexity: O(max(m,n)). The length of the new list is at most max(m,n)+1.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        temp = dummy
        carry = 0
        while (l1 != None or l2 != None) or carry:
            sum = 0
            if l1 != None:
                sum += l1.val
                l1 = l1.next
            if l2 != None:
                sum += l2.val
                l2 = l2.next
            sum += carry
            carry = sum // 10
            node = ListNode(sum % 10)
            temp.next = node
            temp = temp.next
        return dummy.next 


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# endregion




# region 6.4 LINKED LIST - DOUBLY MEDIUM
# --------------------------------------

# 1 TODO :  delete all occurences of a key in DLL
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 2 TODO : find pairs with given sum in DLL
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 3 TODO : remove duplicates from sorted DLL
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      




# endregion





# region 6.5 LINKED LIST - HARD
# -----------------------------

# 1 TODO :  reverse LL in group of given size K
# method 1 : brute force approch
Time Complexity: O(2N) The time complexity consists of actions of reversing segments of K and finding the Kth node which operates in linear time. Thus, O(N) + O(N) = O(2N), which simplifies to O(N).

Space Complexity: O(1) The space complexity is O(1) as the algorithm operates in place without any additional space requirements.

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

# Function to reverse linked list
# using 3 pointer approach
def reverseLinkedList(head):
    
    # Initialize 'temp' at the
    # head of the linked list
    temp = head
    
    # Initialize 'prev' to None,
    # representing the previous node 
    prev = None
    
    while temp is not None:
        # Store the next node in 'front'
        # to preserve the reference
        front = temp.next
        # Reverse the direction of the current
        # node's 'next' pointer to point to 'prev'
        temp.next = prev
        # Move 'prev' to the current 
        # node, for the next iteration
        prev = temp
        # Move 'temp' to 'front' node
        # advancing traversal
        temp = front

    # Return the new head
    # of the reversed linked list
    return prev
    
# Function to get the Kth node from
# a given position in the linked list
def getKthNode(temp, k):
    # Decrement K as we already
    # start from the 1st node
    k -= 1

    # Decrement K until it reaches
    # the desired position
    while temp is not None and k > 0:
        # Decrement k as temp progresses
        k -= 1

        # Move to the next node
        temp = temp.next

    # Return the Kth node
    return temp


# Function to reverse nodes in groups of K
def kReverse(head, k):
    # Initialize a temporary
    # node to traverse the list
    temp = head

    # Initialize a pointer to track the
    # last node of the previous group
    prevLast = None

    # Traverse through the linked list
    while temp is not None:
        # Get the Kth node of the current group
        kThNode = getKthNode(temp, k)

        # If the Kth node is NULL
        # (not a complete group)
        if kThNode is None:
            # If there was a previous group,
            # link the last node to the current node
            if prevLast:
                prevLast.next = temp

            # Exit the loop
            break

        # Store the next node
        # after the Kth node
        nextNode = kThNode.next

        # Disconnect the Kth node
        # to prepare for reversal
        kThNode.next = None

        # Reverse the nodes from
        # temp to the Kth node
        reverseLinkedList(temp)

        # Adjust the head if the reversal
        # starts from the head
        if temp == head:
            head = kThNode
        else:
            # Link the last node of the previous
            # group to the reversed group
            prevLast.next = kThNode

        # Update the pointer to the
        # last node of the previous group
        prevLast = temp

        # Move to the next group
        temp = nextNode

    # Return the head of the
    # modified linked list
    return head


# Function to print the linked list
def printLinkedList(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create a linked list with
# values 5, 4, 3, 7, 9 and 2
head = Node(5)
head.next = Node(4)
head.next.next = Node(3)
head.next.next.next = Node(7)
head.next.next.next.next = Node(9)
head.next.next.next.next.next = Node(2)

# Print the original linked list
print("Original Linked List: ", end="")
printLinkedList(head)

# Reverse the linked list
head = kReverse(head, 4)

# Print the reversed linked list
print("Reversed Linked List: ", end="")
printLinkedList(head)  


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 2 TODO : rotate a LL
# method 1 : brute force approch
Time Complexity: O(Number of nodes present in the list*k)

Reason: For k times, we are iterating through the entire list to get the last element and move it to first.

Space Complexity: O(1)

Reason: No extra data structures is used for computations

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None




# utility function to insert node at the end of the linked list
def insertNode(head, val):
    newNode = Node(val)
    if head == None:
        head = newNode
        return head
    temp = head
    while temp.next != None:
        temp = temp.next
    temp.next = newNode
    return head




# utility function to rotate list by k times
def rotateRight(head, k):
    if head == None or head.next == None:
        return head
    for i in range(k):
        temp = head
        while temp.next.next != None:
            temp = temp.next
        end = temp.next
        temp.next = None
        end.next = head
        head = end
    return head




# utility function to print list
def printList(head):
    while head.next != None:
        print(head.val, end='->')
        head = head.next
    print(head.val)
    return




if __name__ == '__main__':
    head = None
    # inserting Node
    head = insertNode(head, 1)
    head = insertNode(head, 2)
    head = insertNode(head, 3)
    head = insertNode(head, 4)
    head = insertNode(head, 5)


    print("Original list: ", end='')
    printList(head)


    k = 2
    # calling function for rotating right of the nodes by k times
    newHead = rotateRight(head, k)


    print("After", k, "iterations: ", end='')
    printList(newHead)  # list after rotating nodes


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(length of list) + O(length of list - (length of list%k))

Reason: O(length of the list) for calculating the length of the list. O(length of the list - (length of list%k)) for breaking link.

Space Complexity: O(1)

Reason: No extra data structure is used for computation.
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None




# utility function to insert node at the end of the linked list
def insertNode(head, val):
    newNode = Node(val)
    if head == None:
        head = newNode
        return head
    temp = head
    while temp.next != None:
        temp = temp.next
    temp.next = newNode
    return head




# utility function to rotate list by k times
def rotateRight(head, k):
    if head == None or head.next == None or k == 0:
        return head
    # calculating length
    temp = head
    length = 1
    while temp.next != None:
        length += 1
        temp = temp.next
    # link last node to first node
    temp.next = head
    k = k % length  # when k is more than length of list
    end = length - k  # to get end of the list
    while end:
        temp = temp.next
        end -= 1
    # breaking last node link and pointing to NULL
    head = temp.next
    temp.next = None


    return head




# utility function to print list
def printList(head):
    while head.next != None:
        print(head.val, end='->')
        head = head.next
    print(head.val)
    return




if __name__ == '__main__':
    head = None
    # inserting Node
    head = insertNode(head, 1)
    head = insertNode(head, 2)
    head = insertNode(head, 3)
    head = insertNode(head, 4)
    head = insertNode(head, 5)


    print("Original list: ", end='')
    printList(head)


    k = 2
    # calling function for rotating right of the nodes by k times
    newHead = rotateRight(head, k)


    print("After", k, "iterations: ", end='')
    printList(newHead)  # list after rotating nodes


# 3 TODO : flattening of LL
# method 1 : brute force approch
Time Complexity: O(N*M) + O(N*M log(N*M)) + O(N*M)where N is the length of the linked list along the next pointer and M is the length of the linked list along the child pointer.

O(N*M) as we traverse through all the elements, iterating through ‘N’ nodes along the next pointer and ‘M’ nodes along the child pointer.
O(N*M log(N*M)) as we sort the array containing N*M (total) elements.
O(N*M) as we reconstruct the linked list from the sorted array by iterating over the N*M elements of the array.
Space Complexity : O(N*M) + O(N*M)where N is the length of the linked list along the next pointer and M is the length of the linked list along the child pointer.

O(N*M) for storing all the elements in an additional array for sorting.
O(N*M) to reconstruct the linked list from the array after sorting

                                
class Node:
    def __init__(self, x=None, nextNode=None, childNode=None):
        self.data = x
        self.next = nextNode
        self.child = childNode

# Function to convert a list to a linked list
def convertArrToLinkedList(arr):
    # Create a dummy node to serve as
    # the head of the linked list
    dummyNode = Node(-1)
    temp = dummyNode

    # Iterate through the list and
    # create nodes with list elements
    for val in arr:
        # Create a new node with the list element
        temp.child = Node(val)
        # Move the temporary pointer
        # to the newly created node
        temp = temp.child

    # Return the linked list starting
    # from the next of the dummy node
    return dummyNode.child

# Function to flatten a linked list with child pointers
def flattenLinkedList(head):
    arr = []

    # Traverse through the linked list
    while head:
        # Traverse through the child
        # nodes of each head node
        t2 = head
        while t2:
            # Store each node's data in the list
            arr.append(t2.data)
            # Move to the next child node
            t2 = t2.child
        # Move to the next head node
        head = head.next

    # Sort the list containing
    # node values in ascending order
    arr.sort()

    # Convert the sorted list
    # back to a linked list
    return convertArrToLinkedList(arr)

# Print the linked list by
# traversing through child pointers
def printLinkedList(head):
    while head:
        print(head.data, end=" ")
        head = head.child
    print()

# Print the linked list
# in a grid-like structure
def printOriginalLinkedList(head, depth=0):
    while head:
        print(head.data, end="")

        # If child exists, recursively
        # print it with indentation
        if head.child:
            print(" -> ", end="")
            printOriginalLinkedList(head.child, depth + 1)

        # Add vertical bars
        # for each level in the grid
        if head.next:
            print()
            print("| " * depth, end="")

        head = head.next

# Create a linked list with child pointers
head = Node(5)
head.child = Node(14)

head.next = Node(10)
head.next.child = Node(4)

head.next.next = Node(12)
head.next.next.child = Node(20)
head.next.next.child.child = Node(13)

head.next.next.next = Node(7)
head.next.next.next.child = Node(17)

# Print the original
# linked list structure
print("Original linked list:")
printOriginalLinkedList(head)

# Flatten the linked list
# and print the flattened list
flattened = flattenLinkedList(head)
print("\nFlattened linked list: ")
printLinkedList(flattened)
                                
                            



# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O( N*(2M) ) ~ O(2 N*M)where N is the length of the linked list along the next pointer and M is the length of the linked list along the child pointers.

The merge operation in each recursive call takes time complexity proportional to the length of the linked lists being merged as they have to iterate over the entire lists. Since the vertical depth of the linked lists is assume to be M, the time complexity for a single merge operation is proportional to O(2*M).
This operation operation is performed N number of times (to each and every node along the next pointer list) hence the resultant time complexity becomes: O(N* 2M).
Space Complexity : O(1) as this algorithm uses no external space or additional data structures to store values. But a recursive stack uses O(N) space to build the recursive calls for each node along the next pointer list.

                                
                     
class Node:
    def __init__(self, x=0, nextNode=None, childNode=None):
        self.data = x
        self.next = nextNode
        self.child = childNode

# Merges two linked lists in a particular
# order based on the data value
def merge(list1, list2):
    # Create a dummy node as a
    # placeholder for the result
    dummyNode = Node(-1)
    res = dummyNode

    # Merge the lists based on data values
    while list1 and list2:
        if list1.data < list2.data:
            res.child = list1
            res = list1
            list1 = list1.child
        else:
            res.child = list2
            res = list2
            list2 = list2.child
        res.next = None

    # Connect the remaining
    # elements if any
    if list1:
        res.child = list1
    else:
        res.child = list2

    # Break the last node's
    # link to prevent cycles
    if dummyNode.child:
        dummyNode.child.next = None

    return dummyNode.child

# Flattens a linked list with child pointers
def flattenLinkedList(head):
    # If head is null or there 
    # is no next node, return head
    if not head or not head.next:
        return head

    # Recursively flatten the
    # rest of the linked list
    mergedHead = flattenLinkedList(head.next)
    head = merge(head, mergedHead)
    return head

# Print the linked list by
# traversing through child pointers
def printLinkedList(head):
    while head:
        print(head.data, end=" ")
        head = head.child
    print()

# Print the linked list
# in a grid-like structure
def printOriginalLinkedList(head, depth):
    while head:
        print(head.data, end="")

        # If child exists, recursively
        # print it with indentation
        if head.child:
            print(" -> ", end="")
            printOriginalLinkedList(head.child, depth + 1)

        # Add vertical bars
        # for each level in the grid
        if head.next:
            print()
            print("| " * depth, end="")
        head = head.next

# Create a linked list with child pointers
head = Node(5)
head.child = Node(14)
head.next = Node(10)
head.next.child = Node(4)
head.next.next = Node(12)
head.next.next.child = Node(20)
head.next.next.child.child = Node(13)
head.next.next.next = Node(7)
head.next.next.next.child = Node(17)

# Print the original
# linked list structure
print("Original linked list:")
printOriginalLinkedList(head, 0)

# Flatten the linked list
# and print the flattened list
flattened = flattenLinkedList(head)
print("\nFlattened linked list: ", end="")
printLinkedList(flattened)

                                
                            


# 4 TODO : clone a linked list with random and next pointer
# method 1 : brute force approch
Time Complexity: O(2N) where N is the number of nodes in the linked list. The linked list is traversed twice, once for creating copies of each node and for the second time to set the next and random pointers for each copied node. The time to access the nodes in the map is O(1) due to hashing.

Space Complexity : O(N)+O(N)where N is the number of nodes in the linked list as all nodes are stored in the map to maintain mappings and the copied linked lists takes O(N) space as well.

                                
# Node class to represent
# elements in the linked list
class Node:
    def __init__(self, x, nextNode=None, randomNode=None):
        # Data stored in the node
        self.data = x
        # Pointer to the next node
        self.next = nextNode
        # Pointer to a random
        # node in the list
        self.random = randomNode


# Function to clone the linked list
def cloneLL(head):
    temp = head
    # Create a dictionary to map original
    # nodes to their corresponding copied nodes
    mpp = {}

    # Step 1: Create copies of each node
    # and store them in the map
    while temp is not None:
        # Create a new node with the
        # same data as the original node
        newNode = Node(temp.data)
        # Map the original node to its
        # corresponding copied node in the dictionary
        mpp[temp] = newNode
        # Move to the next node in the original list
        temp = temp.next

    temp = head
    # Step 2: Connect the next and random
    # pointers of the copied nodes using the dictionary
    while temp is not None:
        # Access the copied node corresponding
        # to the current original node
        copyNode = mpp[temp]
        # Set the next pointer of the copied node
        # to the copied node mapped to the
        # next node in the original list
        copyNode.next = mpp[temp.next]
        # Set the random pointer of the copied node
        # to the copied node mapped to the
        # random node in the original list
        copyNode.random = mpp[temp.random]
        # Move to the next node
        # in the original list
        temp = temp.next

    # Return the head of the
    # deep copied list from the dictionary
    return mpp[head]


# Function to print the cloned linked list
def printClonedLinkedList(head):
    while head is not None:
        print(f"Data: {head.data}", end="")
        if head.random is not None:
            print(f", Random: {head.random.data}")
        else:
            print(", Random: nullptr")
        head = head.next


# Main function
if __name__ == "__main__":
    # Example linked list: 7 -> 14 -> 21 -> 28
    head = Node(7)
    head.next = Node(14)
    head.next.next = Node(21)
    head.next.next.next = Node(28)

    # Assigning random pointers
    head.random = head.next.next
    head.next.random = head
    head.next.next.random = head.next.next.next
    head.next.next.next.random = head.next

    print("Original Linked List with Random Pointers:")
    printClonedLinkedList(head)

    # Clone the linked list
    clonedList = cloneLL(head)

    print("\nCloned Linked List with Random Pointers:")
    printClonedLinkedList(clonedList)
                                
                            


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(3N)where N is the number of nodes in the linked list. The algorithm makes three traversals of the linked list, once to create copies and insert them between original nodes, then to set the random pointers of the copied nodes to their appropriate copied nodes and then to separate the copied and original nodes.

Space Complexity : O(N) where N is the number of nodes in the linked list as the only extra additional space allocated it to create the copied list without creating any other additional data structures.

                                
                     
# Node class to represent
# elements in the linked list
class Node:
    # Data stored in the node
    def __init__(self, x):
        self.data = x
        # Pointer to the next node
        self.next = None
        # Pointer to a random
        # node in the list
        self.random = None

# Function to insert a copy of each
# node in between the original nodes
def insertCopyInBetween(head):
    temp = head
    while temp:
        nextElement = temp.next
        # Create a new node with the same data
        copy = Node(temp.data)

        # Point the copy's next to
        # the original node's next
        copy.next = nextElement

        # Point the original
        # node's next to the copy
        temp.next = copy

        # Move to the next original node
        temp = nextElement

# Function to connect random
# pointers of the copied nodes
def connectRandomPointers(head):
    temp = head
    while temp:
        # Access the copied node
        copyNode = temp.next

        # If the original node
        # has a random pointer
        if temp.random:
            # Point the copied node's random to the
            # corresponding copied random node
            copyNode.random = temp.random.next
        else:
            # Set the copied node's random to
            # null if the original random is null
            copyNode.random = None

        # Move to the next original node
        temp = temp.next.next

# Function to retrieve the
# deep copy of the linked list
def getDeepCopyList(head):
    temp = head
    # Create a dummy node
    dummyNode = Node(-1)
    # Initialize a result pointer
    res = dummyNode

    while temp:
        # Creating a new List by
        # pointing to copied nodes
        res.next = temp.next
        res = res.next

        # Disconnect and revert back to the
        # initial state of the original linked list
        temp.next = temp.next.next
        temp = temp.next

    # Return the deep copy of the
    # list starting from the dummy node
    return dummyNode.next

# Function to clone the linked list
def cloneLL(head):
    # If the original list
    # is empty, return null
    if not head:
        return None

    # Step 1: Insert copy of
    # nodes in between
    insertCopyInBetween(head)
    # Step 2: Connect random
    # pointers of copied nodes
    connectRandomPointers(head)
    # Step 3: Retrieve the deep
    # copy of the linked list
    return getDeepCopyList(head)

# Function to print the cloned linked list
def printClonedLinkedList(head):
    while head:
        print("Data:", head.data, end="")
        if head.random:
            print(", Random:", head.random.data, end="")
        else:
            print(", Random: None", end="")
        print()
        # Move to the next node
        head = head.next

# Main function
if __name__ == "__main__":
    # Example linked list: 7 -> 14 -> 21 -> 28
    head = Node(7)
    head.next = Node(14)
    head.next.next = Node(21)
    head.next.next.next = Node(28)

    # Assigning random pointers
    head.random = head.next.next
    head.next.random = head
    head.next.next.random = head.next.next.next
    head.next.next.next.random = head.next

    print("Original Linked List with Random Pointers:")
    printClonedLinkedList(head)

    # Clone the linked list
    clonedList = cloneLL(head)

    print("\nCloned Linked List with Random Pointers:")
    printClonedLinkedList(clonedList)

                                
                            



# endregion




# region 7.1 RECURSION - BASIC
# ----------------------------

# 1 TODO :  recursive implementation of atoi()
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 2 TODO : pow(x,n)
# method 1 : brute force approch
Time Complexity: O(N)

Space Complexity: O(1)

def myPow(x: float, n: int) -> float:
    ans = 1.0
    for i in range(n):
        ans = ans * x
    return ans

if __name__ == "__main__":
    print(myPow(2, 10))


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(log n)

Space Complexity: O(1)

def myPow(x: float, n: int) -> float:
    ans = 1.0
    nn = n
    if nn < 0:
        nn = -1 * nn
    while nn:
        if nn % 2:
            ans = ans * x
            nn = nn - 1
        else:
            x = x * x
            nn = nn // 2
    if n < 0:
        ans = 1.0 / ans
    return ans

if __name__ == "__main__":
    print(myPow(2, 10))


# 3 TODO : count good numbers
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 4 TODO : sort a stack using recursion
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 5 TODO : reverse a stack using recursion
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      



# endregion




# region 7.2 RECURSION - PATTERN
# ------------------------------

# 1 TODO :  generate all binary strings
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 2 TODO : generate paranthesis
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 3 TODO : print all subsequences / power set
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 4 TODO : learn all patterns of subsequences (theory)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 5 TODO : count all subsequences with sum K
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 6 TODO : check if there exists a subsequences with sum K
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 7 TODO : combination sum - I
# method 1 : brute force approch
Time Complexity: O(2^t * k) where t is the target, k is the average length

Reason: Assume if you were not allowed to pick a single element multiple times, every element will have a couple of options: pick or not pick which is 2^n different recursion calls, also assuming that the average length of every combination generated is k. (to put length k data structure into another data structure)

Why not (2^n) but (2^t) (where n is the size of an array)?

Assume that there is 1 and the target you want to reach is 10 so 10 times you can “pick or not pick” an element.

Space Complexity: O(k*x), k is the average length and x is the no. of combinations

from typing import List




class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        ds = []


        def findCombination(ind: int, target: int):
            if ind == len(candidates):
                if target == 0:
                    ans.append(ds[:])
                return
            if candidates[ind] <= target:
                ds.append(candidates[ind])
                findCombination(ind, target - candidates[ind])
                ds.pop()
            findCombination(ind + 1, target)
        findCombination(0, target)
        return ans




if __name__ == "__main__":
    obj = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    ans = obj.combinationSum(candidates, target)
    print("Combinations are: ")
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            print(ans[i][j], end=" ")
        print()


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 8 TODO : combination sum - II
# method 1 : brute force approch
Time Complexity:O(2^n*k)

Reason: Assume if all the elements in the array are unique then the no. of subsequence you will get will be O(2^n). we also add the ds to our ans when we reach the base case that will take “k”//average space for the ds.

Space Complexity:O(k*x)

Reason: if we have x combinations then space will be x*k where k is the average length of the combination.

from typing import List




def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    ans = []
    ds = []
    candidates.sort()


    def findCombination(ind: int, target: int):
        if target == 0:
            ans.append(ds[:])
            return
        for i in range(ind, len(candidates)):
            if i > ind and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            ds.append(candidates[i])
            findCombination(i + 1, target - candidates[i])
            ds.pop()


    findCombination(0, target)
    return ans




if __name__ == "__main__":
    v = [10, 1, 2, 7, 6, 1, 5]
    comb = combinationSum2(v, 8)
    print(*comb)


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 9 TODO : subset sum - I
# method 1 : brute force approch
Time Complexity: O(2^n)+O(2^n log(2^n)). Each index has two ways. You can either pick it up or not pick it. So for n index time complexity for O(2^n) and for sorting it will take (2^n log(2^n)).

Space Complexity: O(2^n) for storing subset sums, since 2^n subsets can be generated for an array of size n.

from typing import List




class Solution:
    def subsetSums(self, arr: List[int], n: int) -> List[int]:
        ans = []


        def subsetSumsHelper(ind: int, sum: int):
            if ind == n:
                ans.append(sum)
                return
            # element is picked
            subsetSumsHelper(ind + 1, sum + arr[ind])
            # element is not picked
            subsetSumsHelper(ind + 1, sum)
        subsetSumsHelper(0, 0)
        ans.sort()
        return ans




if __name__ == "__main__":
    arr = [3, 1, 2]
    ans = Solution().subsetSums(arr, len(arr))
    print("The sum of each subset is")
    for sum in ans:
        print(sum, end=" ")
    print()


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 10 TODO :  subset sum - II
# method 1 : brute force approch
Time Complexity: O( 2^n *(k log (x) )). 2^n  for generating every subset and k* log( x)  to insert every combination of average length k in a set of size x. After this, we have to convert the set of combinations back into a list of list /vector of vectors which takes more time.

Space Complexity:  O(2^n * k) to store every subset of average length k. Since we are initially using a set to store the answer another O(2^n *k) is also used.
from typing import List




class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        res = set()


        def fun(index: int, ds: List[int]):
            if index == len(nums):
                ds.sort()
                res.add(tuple(ds))
                return
            ds.append(nums[index])
            fun(index + 1, ds)
            ds.pop()
            fun(index + 1, ds)
        fun(0, [])
        for it in res:
            ans.append(list(it))
        return ans




if __name__ == "__main__":
    nums = [1, 2, 2]
    obj = Solution()
    ans = obj.subsetsWithDup(nums)
    print("The unique subsets are ")
    print("[ ", end="")
    for i in range(len(ans)):
        print("[ ", end="")
        for j in range(len(ans[i])):
            print(ans[i][j], end=" ")
        print("]", end="")  


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(2^n) for generating every subset and O(k)  to insert every subset in another data structure if the average length of every subset is k. Overall O(k * 2^n).

Space Complexity: O(2^n * k) to store every subset of average length k. Auxiliary space is O(n)  if n is the depth of the recursion tree.
from typing import List




class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        ds = []


        def findSubsets(ind: int):
            ans.append(ds[:])
            for i in range(ind, len(nums)):
                if i != ind and nums[i] == nums[i - 1]:
                    continue
                ds.append(nums[i])
                findSubsets(i + 1)
                ds.pop()
        nums.sort()
        findSubsets(0)
        return ans




if __name__ == "__main__":
    nums = [1, 2, 2]
    obj = Solution()
    ans = obj.subsetsWithDup(nums)
    print("The unique subsets are ")
    print(*ans)   


# 11 TODO : combination sum  - III
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 12 TODO : letter combination of phone number
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# endregion




# region 7.3 RECUSION - HARD
# --------------------------

# 1 TODO :  pallindrome partitioning
# method 1 : brute force approch
Time Complexity: O( (2^n) *k*(n/2) )

Reason: O(2^n) to generate every substring and O(n/2)  to check if the substring generated is a palindrome. O(k) is for inserting the palindromes in another data structure, where k  is the average length of the palindrome list.

Space Complexity: O(k * x)

Reason: The space complexity can vary depending on the length of the answer. k is the average length of the list of palindromes and if we have x such list of palindromes in our final answer. The depth of the recursion tree is n, so the auxiliary space required is equal to the O(n).

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []


        def partitionHelper(index: int):
            if index == len(s):
                res.append(path[:])
                return
            for i in range(index, len(s)):
                if isPalindrome(s, index, i):
                    path.append(s[index:i + 1])
                    partitionHelper(i + 1)
                    path.pop()


        def isPalindrome(s: str, start: int, end: int) -> bool:
            while start <= end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True


        partitionHelper(0)
        return res




if __name__ == "__main__":
    s = "aabb"
    obj = Solution()
    ans = obj.partition(s)
    print("The Palindromic partitions are :-")
    print(" [ ", end="")
    for i in ans:
        print("[ ", end="")
        for j in i:
            print(j, end=" ")
        print("] ", end="")
    print("]")

# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 2 TODO : word search
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 3 TODO : N queen
# method 1 : brute force approch
Time Complexity: Exponential in nature since we are trying out all ways, to be precise its O(N! * N).

Space Complexity: O( N2 )
class Solution:
    def isSafe1(self, row, col, board, n):
        # check upper element
        duprow = row
        dupcol = col


        while row >= 0 and col >= 0:
            if board[row][col] == 'Q':
                return False
            row -= 1
            col -= 1


        col = dupcol
        row = duprow
        while col >= 0:
            if board[row][col] == 'Q':
                return False
            col -= 1


        row = duprow
        col = dupcol
        while row < n and col >= 0:
            if board[row][col] == 'Q':
                return False
            row += 1
            col -= 1


        return True


    def solve(self, col, board, ans, n):
        if col == n:
            ans.append(list(board))
            return


        for row in range(n):
            if self.isSafe1(row, col, board, n):
                board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                self.solve(col+1, board, ans, n)
                board[row] = board[row][:col] + '.' + board[row][col+1:]


    def solveNQueens(self, n):
        ans = []
        board = ['.'*n for _ in range(n)]
        self.solve(0, board, ans, n)
        return ans


n = 4
obj = Solution()
ans = obj.solveNQueens(n)
for i in range(len(ans)):
    print(f"Arrangement {i+1}")
    for j in range(len(ans[0])):
        print(ans[i][j])
    print()


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: Exponential in nature since we are trying out all ways, to be precise it is O(N! * N).

Space Complexity: O(N)

from typing import List




class Solution:
    def solve(self, col, board, ans, leftrow, upperDiagonal, lowerDiagonal, n):
        if col == n:
            ans.append(board[:])
            return


        for row in range(n):
            if leftrow[row] == 0 and lowerDiagonal[row+col] == 0 and upperDiagonal[n-1+col-row] == 0:
                board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                leftrow[row] = 1
                lowerDiagonal[row+col] = 1
                upperDiagonal[n-1+col-row] = 1
                self.solve(col+1, board, ans, leftrow,
                           upperDiagonal, lowerDiagonal, n)
                board[row] = board[row][:col] + '.' + board[row][col+1:]
                leftrow[row] = 0
                lowerDiagonal[row+col] = 0
                upperDiagonal[n-1+col-row] = 0


    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = ['.'*n for _ in range(n)]
        leftrow = [0]*n
        upperDiagonal = [0]*(2*n-1)
        lowerDiagonal = [0]*(2*n-1)
        self.solve(0, board, ans, leftrow, upperDiagonal, lowerDiagonal, n)
        return ans




if __name__ == '__main__':
    n = 4
    obj = Solution()
    ans = obj.solveNQueens(n)
    for i in range(len(ans)):
        print("Arrangement", i+1)
        for j in range(len(ans[0])):
            print(ans[i][j])
            print()


# 4 TODO : rent a maze
# method 1 : brute force approch
Time Complexity: O(4^(m*n)), because on every cell we need to try 4 different directions.

Space Complexity:  O(m*n), Maximum Depth of the recursion tree(auxiliary space).
from typing import List




class Solution:


    def findPathHelper(self, i: int, j: int, a: List[List[int]], n: int, ans: List[str], move: str, vis: List[List[int]]):
        if i == n - 1 and j == n - 1:
            ans.append(move)
            return


        # downward
        if i + 1 < n and not vis[i + 1][j] and a[i + 1][j] == 1:
            vis[i][j] = 1
            self.findPathHelper(i + 1, j, a, n, ans, move + 'D', vis)
            vis[i][j] = 0


        # left
        if j - 1 >= 0 and not vis[i][j - 1] and a[i][j - 1] == 1:
            vis[i][j] = 1
            self.findPathHelper(i, j - 1, a, n, ans, move + 'L', vis)
            vis[i][j] = 0


        # right
        if j + 1 < n and not vis[i][j + 1] and a[i][j + 1] == 1:
            vis[i][j] = 1
            self.findPathHelper(i, j + 1, a, n, ans, move + 'R', vis)
            vis[i][j] = 0


        # upward
        if i - 1 >= 0 and not vis[i - 1][j] and a[i - 1][j] == 1:
            vis[i][j] = 1
            self.findPathHelper(i - 1, j, a, n, ans, move + 'U', vis)
            vis[i][j] = 0


    def findPath(self, m: List[List[int]], n: int) -> List[str]:
        ans = []
        vis = [[0 for _ in range(n)] for _ in range(n)]


        if m[0][0] == 1:
            self.findPathHelper(0, 0, m, n, ans, "", vis)
        return ans




if __name__ == '__main__':
    n = 4


    m = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]


    obj = Solution()
    result = obj.findPath(m, n)
    if len(result) == 0:
        print(-1)
    else:
        for i in range(len(result)):
            print(result[i], end=" ")
    print() 


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(4^(m*n)), because on every cell we need to try 4 different directions.

Space Complexity:  O(m*n), Maximum Depth of the recursion tree(auxiliary space).
from typing import List



class Solution:


    def solve(self, i: int, j: int, a: List[List[int]], n: int, ans: List[str], move: str, vis: List[List[int]], di: List[int], dj: List[int]):
        if i == n - 1 and j == n - 1:
            ans.append(move)
            return
        dir = "DLRU"
        for ind in range(4):
            nexti = i + di[ind]
            nextj = j + dj[ind]
            if nexti >= 0 and nextj >= 0 and nexti < n and nextj < n and not vis[nexti][nextj] and a[nexti][nextj] == 1:
                vis[i][j] = 1
                self.solve(nexti, nextj, a, n, ans,
                           move + dir[ind], vis, di, dj)
                vis[i][j] = 0


    def findPath(self, m: List[List[int]], n: int) -> List[str]:
        ans = []
        vis = [[0 for _ in range(n)] for _ in range(n)]
        di = [+1, 0, 0, -1]
        dj = [0, -1, 1, 0]
        if m[0][0] == 1:
            self.solve(0, 0, m, n, ans, "", vis, di, dj)
        return ans




if __name__ == "__main__":
    n = 4
    m = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
    obj = Solution()
    result = obj.findPath(m, n)
    if len(result) == 0:
        print(-1)
    else:
        for i in range(len(result)):
            print(result[i], end=" ")
    print()   


# 5 TODO : word break
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 6 TODO : M coloring problem
# method 1 : brute force approch
Time Complexity: O( N^M) (n raised to m)

Space Complexity: O(N)

def isSafe(node, color, graph, n, col):
    for k in range(n):
        if k != node and graph[k][node] == 1 and color[k] == col:
            return False
    return True




def solve(node, color, m, N, graph):
    if node == N:
        return True


    for i in range(1, m + 1):
        if isSafe(node, color, graph, N, i):
            color[node] = i
            if solve(node + 1, color, m, N, graph):
                return True
            color[node] = 0


    return False


# Function to determine if graph can be coloured with at most M colours such
# that no two adjacent vertices of graph are coloured with same colour.




def graphColoring(graph, m, N):
    color = [0] * N
    if solve(0, color, m, N, graph):
        return True
    return False




if __name__ == '__main__':
    N = 4
    m = 3


    graph = [[0 for i in range(101)] for j in range(101)]


    # Edges are (0, 1), (1, 2), (2, 3), (3, 0), (0, 2)
    graph[0][1] = 1
    graph[1][0] = 1
    graph[1][2] = 1
    graph[2][1] = 1
    graph[2][3] = 1
    graph[3][2] = 1
    graph[3][0] = 1
    graph[0][3] = 1
    graph[0][2] = 1
    graph[2][0] = 1


    print(1 if graphColoring(graph, m, N) else 0)


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 7 TODO : sudoko solver
# method 1 : brute force approch
Time Complexity: O(9(n ^ 2)), in the worst case, for each cell in the n2 board, we have 9 possible numbers.

Space Complexity: O(1), since we are refilling the given board itself, there is no extra space required, so constant space complexity.
from typing import List




def isValid(board: List[List[str]], row: int, col: int, c: str) -> bool:
    for i in range(9):
        if board[i][col] == c:
            return False
        if board[row][i] == c:
            return False
        if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == c:
            return False
    return True




def solveSudoku(board: List[List[str]]) -> bool:
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ".":
                for c in "123456789":
                    if isValid(board, i, j, c):
                        board[i][j] = c
                        if solveSudoku(board):
                            return True
                        else:
                            board[i][j] = "."
                return False
    return True




if __name__ == "__main__":
    board = [
        ["9", "5", "7", ".", "1", "3", ".", "8", "4"],
        ["4", "8", "3", ".", "5", "7", "1", ".", "6"],
        [".", "1", "2", ".", "4", "9", "5", "3", "7"],
        ["1", "7", ".", "3", ".", "4", "9", ".", "2"],
        ["5", ".", "4", "9", "7", ".", "3", "6", "."],
        ["3", ".", "9", "5", ".", "8", "7", ".", "1"],
        ["8", "4", "5", "7", "9", ".", "6", "1", "3"],
        [".", "9", "1", ".", "3", "6", ".", "7", "5"],
        ["7", ".", "6", "1", "8", "5", "4", ".", "9"],
    ]
    solveSudoku(board)
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()  


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 8 TODO : expression add operators
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# endregion





# region 8.1 BIT MANIPULATION - BASIC
# -----------------------------------

# 1 TODO :  introduction to bit manipulation
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 2 TODO : check if the i-th bit is set or not
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 3 TODO : check if a number is odd or not
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 4 TODO : check if a number is power of 2 or not
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 5 TODO : count the number of set bits
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 6 TODO : set/unset the right most unset bit
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 7 TODO : swap two numbers
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 8 TODO : divide two integers without using multiplication
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# endregion





# region 8.2 BIT MANIPULATION - MEDIUM
# ------------------------------------

# 1 TODO :  count number of bits to be flipped to convert A to B
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 2 TODO : find the number that appears odd number of times
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 3 TODO : power set 
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 4 TODO : find xor of numbers from left to right
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 5 TODO : find the two numbers appearing off number of times
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      



# endregion





# region 8.3 BIT MANIPULATION - HARD
# ----------------------------------

# 1 TODO :  print prime factors of a number
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 2 TODO : all divisors of a number
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 3 TODO : sieve of eratosthenes
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 4 TODO : find prime factorisation of a number using sieve
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 5 TODO : power(n,x)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      



# endregion






# region 9.1 STACK/QUEUE - LEARNING
# ---------------------------------

# 1 TODO :  implement stack using arrays
# method 1 : brute force approch
Time Complexity: O(N)

Space Complexity: O(N)
class Stack:
    def __init__(self):
        self.top = -1
        self.size = 1000
        self.arr = [0] * self.size


    def push(self, x: int) -> None:
        self.top += 1
        self.arr[self.top] = x


    def pop(self) -> int:
        x = self.arr[self.top]
        self.top -= 1
        return x


    def Top(self) -> int:
        return self.arr[self.top]


    def Size(self) -> int:
        return self.top + 1




if __name__ == "__main__":
    s = Stack()
    s.push(6)
    s.push(3)
    s.push(7)
    print("Top of stack is before deleting any element", s.Top())
    print("Size of stack before deleting any element", s.Size())
    print("The element deleted is", s.pop())
    print("Size of stack after deleting an element", s.Size())
    print("Top of stack after deleting an element", s.Top())

# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 2 TODO : implement queue using arrays
# method 1 : brute force approch
Time Complexity:

pop function: O(1)

push function: O(1)

top function: O(1)

size function: O(1)

Space Complexity:
Whole Queue: O(n)

class Queue:
    def __init__(self):
        self.start = -1
        self.end = -1
        self.currSize = 0
        self.maxSize = 16
        self.arr = [0] * self.maxSize


    def push(self, newElement: int) -> None:
        if self.currSize == self.maxSize:
            print("Queue is full\nExiting...")
            exit(1)
        if self.end == -1:
            self.start = 0
            self.end = 0
        else:
            self.end = (self.end + 1) % self.maxSize
        self.arr[self.end] = newElement
        print("The element pushed is", newElement)
        self.currSize += 1


    def pop(self) -> int:
        if self.start == -1:
            print("Queue Empty\nExiting...")
        popped = self.arr[self.start]
        if self.currSize == 1:
            self.start = -1
            self.end = -1
        else:
            self.start = (self.start + 1) % self.maxSize
        self.currSize -= 1
        return popped


    def top(self) -> int:
        if self.start == -1:
            print("Queue is Empty")
            exit(1)
        return self.arr[self.start]


    def size(self) -> int:
        return self.currSize




if __name__ == "__main__":
    q = Queue()
    q.push(4)
    q.push(14)
    q.push(24)
    q.push(34)
    print("The peek of the queue before deleting any element", q.top())
    print("The size of the queue before deletion", q.size())
    print("The first element to be deleted", q.pop())
    print("The peek of the queue after deleting an element", q.top())
    print("The size of the queue after deleting an element", q.size())


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 3 TODO : implement stack using queue
# method 1 : brute force approch
Time Complexity: O(N)

Space Complexity: O(N)
from queue import Queue




class Stack:
    def __init__(self):
        self.q = Queue()


    def push(self, x):
        s = self.q.qsize()
        self.q.put(x)
        for i in range(s):
            self.q.put(self.q.get())


    def pop(self):
        n = self.q.get()
        return n


    def top(self):
        return self.q.queue[0]


    def size(self):
        return self.q.qsize()




if __name__ == "__main__":
    s = Stack()
    s.push(3)
    s.push(2)
    s.push(4)
    s.push(1)
    print("Top of the stack: ", s.top())
    print("Size of the stack before removing element: ", s.size())
    print("The deleted element is: ", s.pop())
    print("Top of the stack after removing element: ", s.top())
    print("Size of the stack after removing element: ", s.size())  


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 4 TODO : implement queue using stack
# method 1 : brute force approch
Time Complexity: O(N )  

Space Complexity: O(2N)
from queue import LifoQueue
# using LifoQueue which is a stack in python




class Queue:
    def __init__(self):
        self.input = LifoQueue()
        self.output = LifoQueue()


    def push(self, data: int) -> None:
        # Pop out all elements from the stack input
        while not self.input.empty():
            self.output.put(self.input.get())
        # Insert the desired element in the stack input
        print("The element pushed is", data)
        self.input.put(data)
        # Pop out elements from the stack output and push them into the stack input
        while not self.output.empty():
            self.input.put(self.output.get())


    # Pop the element from the Queue
    def pop(self) -> int:
        if self.input.qsize() == 0:
            print("Stack is empty")
            exit(0)
        val = self.input.get()
        return val


    def Top(self) -> int:
        if self.input.qsize() == 0:
            print("Stack is empty")
            exit(0)
        return self.input.queue[-1]


    def size(self) -> int:
        return self.input.qsize()




if __name__ == "__main__":
    q = Queue()
    q.push(3)
    q.push(4)
    print("The element poped is", q.pop())
    q.push(5)
    print("The top of the queue is", q.Top())
    print("The size of the queue is", q.size())


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 5 TODO : implement stack using linked list
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 6 TODO : implement queue using linked list
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 7 TODO : check for balanced paranthesis
# method 1 : brute force approch
Time Complexity: O(N)

Space Complexity: O(N)
def isValid(s: str) -> bool:
    st = []
    for it in s:
        if it == '(' or it == '{' or it == '[':
            st.append(it)
        else:
            if len(st) == 0:
                return False
            ch = st[-1]
            st.pop()
            if (it == ')' and ch == '(') or (it == ']' and ch == '[') or (it == '}' and ch == '{'):
                continue
            else:
                return False
    return len(st) == 0




if __name__ == '__main__':
    s = "()[{}()]"
    if isValid(s):
        print("True")
    else:
        print("False") 


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 8 TODO : implement min stack
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      



# endregion






# region 9.2 STACK/QUEUE - PREFIX/POSTFIX
# ---------------------------------------

# 1 TODO :  infix to postfix conversion using stack
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 2 TODO : prefix to infix conversion
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 3 TODO : prefix to postfix conversion
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 4 TODO : postfix to prefix conversion
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 5 TODO : postfix to infix 
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 6 TODO : convert infix to prefix notation
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      




# endregion






# region 9.3 STACK/QUEUE - MONOTONIC
# ----------------------------------

# 1 TODO :  next greater element - I
# method 1 : brute force approch
Time Complexity: O(N)

Space Complexity: O(N)

from typing import List




class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nge = [-1] * n
        st = []


        for i in range(2 * n - 1, -1, -1):
            while st and st[-1] <= nums[i % n]:
                st.pop()


            if i < n:
                if st:
                    nge[i] = st[-1]
            st.append(nums[i % n])
        return nge




if __name__ == '__main__':
    obj = Solution()
    v = [5, 7, 1, 2, 6, 0]
    res = obj.nextGreaterElements(v)
    print("The next greater elements are")
    print(*res)


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 2 TODO : next greater element - II
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 3 TODO : next smaller element
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 4 TODO : number of NGEs to the right
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 5 TODO : trapping rainwater
# method 1 : brute force approch
Time Complexity: O(N*N) as for each index we are calculating leftMax and rightMax so it is a nested loop.

Space Complexity: O(1).

from typing import List




def trap(arr: List[int]) -> int:
    n = len(arr)
    waterTrapped = 0
    for i in range(n):
        j = i
        leftMax = 0
        rightMax = 0
        while j >= 0:
            leftMax = max(leftMax, arr[j])
            j -= 1
        j = i
        while j < n:
            rightMax = max(rightMax, arr[j])
            j += 1
        waterTrapped += min(leftMax, rightMax) - arr[i]
    return waterTrapped




if __name__ == "__main__":
    arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(f"The water that can be trapped is {trap(arr)}")


# method 2 : better approch
Time Complexity: O(3*N) as we are traversing through the array only once. And O(2*N) for computing prefix and suffix array.

Space Complexity: O(N)+O(N) for prefix and suffix arrays.
from typing import List




def trap(arr: List[int]) -> int:
    n = len(arr)
    prefix = [0] * n
    suffix = [0] * n
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = max(prefix[i - 1], arr[i])
    suffix[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        suffix[i] = max(suffix[i + 1], arr[i])
    waterTrapped = 0
    for i in range(n):
        waterTrapped += min(prefix[i], suffix[i]) - arr[i]
    return waterTrapped




if __name__ == "__main__":
    arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(f"The water that can be trapped is {trap(arr)}")
  


# method 3 : optimal solution
Time Complexity: O(N) because we are using 2 pointer approach.

Space Complexity: O(1) because we are not using anything extra.
from typing import List




def trap(height: List[int]) -> int:
    n = len(height)
    left = 0
    right = n-1
    res = 0
    maxLeft = 0
    maxRight = 0
    while left <= right:
        if height[left] <= height[right]:
            if height[left] >= maxLeft:
                maxLeft = height[left]
            else:
                res += maxLeft - height[left]
            left += 1
        else:
            if height[right] >= maxRight:
                maxRight = height[right]
            else:
                res += maxRight - height[right]
            right -= 1
    return res




if __name__ == "__main__":
    arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(f"The water that can be trapped is {trap(arr)}")    


# 6 TODO : sum of subarray minimum
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 7 TODO : asteriod collision
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 8 TODO : sum of subarray ranges
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 9 TODO : remove k digits
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 10 TODO :  largest rectangle in a histogram
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 11 TODO : maximal rectangle
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      



# endregion






# region 9.4 STACK/QUEUE - IMPLEMENTATION
# ---------------------------------------

# 1 TODO :  sliding window maximum
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 2 TODO : stock span problem
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 3 TODO : the celebrity problem
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 4 TODO : LRU cache (important)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 5 TODO : LFU cache
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# endregion


# region 10.1 SLIDING WINDOW/TWO POINTER - MEDIUM
# -----------------------------------------------

# 1 TODO :  largest substring without repeating characters
# method 1 : brute force approch
Time Complexity: O( N2 )

Space Complexity: O(N) where N is the size of HashSet taken for storing the elements 
def solve(str: str) -> int:
    if len(str) == 0:
        return 0
    maxans = -1
    for i in range(len(str)):  # outer loop for traversing the string
        set = {}
        # nested loop for getting different string starting with str[i]
        for j in range(i, len(str)):
            if str[j] in set:  # if element if found so mark it as ans and break from the loop
                maxans = max(maxans, j - i)
                break
            set[str[j]] = 1
    return maxans


if __name__ == "__main__":
    str = "takeUforward"
    print("The length of the longest substring without repeating characters is", solve(str))


# method 2 : better approch
Time Complexity: O( 2*N ) (sometimes left and right both have to travel a complete array)

Space Complexity: O(N) where N is the size of HashSet taken for storing the elements
def solve(str: str) -> int:
    if len(str) == 0:
        return 0
    maxans = float("-inf")
    setx = set()
    l = 0
    for r in range(len(str)):  # outer loop for traversing the string
        if str[r] in setx:  # if duplicate element is found
            while l < r and str[r] in setx:
                setx.remove(str[l])
                l += 1
        setx.add(str[r])
        maxans = max(maxans, r - l + 1)
    return maxans


if __name__ == "__main__":
    str = "takeUforward"
    print("The length of the longest substring without repeating characters is", solve(str))   


# method 3 : optimal solution
Time Complexity: O( N )

Space Complexity: O(N) where N represents the size of HashSet where we are storing our elements
class Solution:
    def lengthofLongestSubstring(self, s: str) -> int:
        mpp = [-1] * 256


        left = 0
        right = 0
        n = len(s)
        length = 0
        while right < n:
            if mpp[ord(s[right])] != -1:
                left = max(mpp[ord(s[right])] + 1, left)


            mpp[ord(s[right])] = right


            length = max(length, right - left + 1)
            right += 1
        return length


if __name__ == "__main__":
    str = "takeUforward"
    obj = Solution()
    print("The length of the longest substring without repeating characters is",
          obj.lengthofLongestSubstring(str))   


# 2 TODO : max consecutive ones - III
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 3 TODO : fruit into baskets
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 4 TODO : longest repeating character replacement
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 5 TODO : binary subarray with sum
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 6 TODO : count number of nice subarrays
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 7 TODO : number of substring containg all three characters
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 8 TODO : maximun point you can obtain from cards


# endregion




# region 10.2 SLIDING WINDOW/TWO POINTER - HARD
# ---------------------------------------------

# 1 TODO : largest substring with at most K distincet characters 
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 2 TODO : subarray with k different integers
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 3 TODO : minimum window substring
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 4 TODO : minimum window subsequence
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      




# endregion




# region 11.1 HEAP/PRIORITY QUEUE - LEARNING
# ------------------------------------------

# 1 TODO :  introduction to parity queue using binary heaps
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 2 TODO : min heap and max heap replacement
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 3 TODO : check if an array represents a min-heap or not
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 4 TODO : convert min heap to max heap
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      



# endregion




# region 11.2 HEAP/PRIORITY QUEUE - MEDIUM
# ----------------------------------------

# 1 TODO :  Kth largest element in an array (use parity queue)
# method 1 : brute force approch
Time complexity: O(nlogn)

Space complexity: O(1)
from typing import List




class Solution:
    def kth_Largest_And_Smallest_By_AscendingOrder(self, arr: List[int], k: int) -> None:
        arr.sort()
        n = len(arr)


        print(
            f"kth Largest element {arr[n - k]}, kth Smallest element {arr[k - 1]}")




if __name__ == "__main__":
    arr = [1, 2, 6, 4, 5, 3]
    Solution().kth_Largest_And_Smallest_By_AscendingOrder(arr, 3) 


# method 2 : better approch
Time complexity: O(k+(n-k)*log(k))  , n = size of array

Space complexity: O(k)

import heapq




class Solution:
    def kth_Largest_MaxHeap(self, arr, k):
        pq = []
        n = len(arr)
        for i in range(n):
            heapq.heappush(pq, -arr[i])


        f = k - 1


        while f > 0:
            heapq.heappop(pq)
            f -= 1


        print("Kth Largest element", -pq[0])


    def kth_Smallest_MinHeap(self, arr, k):
        pq = []
        n = len(arr)


        for i in range(n):
            heapq.heappush(pq, arr[i])


        f = k - 1


        while f > 0:
            heapq.heappop(pq)
            f -= 1


        print("Kth Smallest element", pq[0])




if __name__ == "__main__":
    arr = [1, 2, 6, 4, 5, 3]


    obj = Solution()
    obj.kth_Largest_MaxHeap(arr, 3)
    obj.kth_Smallest_MinHeap(arr, 3)

 


# method 3 : optimal solution
Time complexity: O(n) , where n = size of the array

Space complexity: O(1) 

from typing import List




def partition(arr: List[int], left: int, right: int) -> int:
    pivot = arr[left]
    l = left + 1
    r = right
    while l <= r:
        if arr[l] < pivot and arr[r] > pivot:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        if arr[l] >= pivot:
            l += 1
        if arr[r] <= pivot:
            r -= 1


    arr[left], arr[r] = arr[r], arr[left]
    return r




def kth_Largest_Element(arr: List[int], k: int) -> int:
    left = 0
    right = len(arr) - 1
    kth = 0
    while 1:
        idx = partition(arr, left, right)
        if idx == k - 1:
            kth = arr[idx]
            break
        if idx < k - 1:
            left = idx + 1
        else:
            right = idx - 1


    return kth


# method 4 : optimized
Time complexity: O(n) ,where n = size of the array

Space complexity: O(1)
from typing import List




def partition(arr: List[int], l: int, r: int) -> int:
    f = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= f:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i




def kth_Smallest_Element(arr: List[int], l: int, r: int, k: int) -> int:
    if k <= r - l + 1 and k > 0:
        ind = partition(arr, l, r)
        if ind - l == k - 1:
            return arr[ind]
        if ind - l > k - 1:
            return kth_Smallest_Element(arr, l, ind - 1, k)
        return kth_Smallest_Element(arr, ind + 1, r, k - ind + l - 1)
    return float("inf")




if __name__ == "__main__":
    arr = [12, 3, 5, 7, 4, 19, 26]
    n = len(arr)
    k = 1
    print(f"Kth smallest element is {kth_Smallest_Element(arr, 0, n - 1, k)}")





# 2 TODO : Kth smallest element in an array  (use parity queue)
# method 1 : brute force approch
Time complexity: O(nlogn)

Space complexity: O(1)
from typing import List




class Solution:
    def kth_Largest_And_Smallest_By_AscendingOrder(self, arr: List[int], k: int) -> None:
        arr.sort()
        n = len(arr)


        print(
            f"kth Largest element {arr[n - k]}, kth Smallest element {arr[k - 1]}")




if __name__ == "__main__":
    arr = [1, 2, 6, 4, 5, 3]
    Solution().kth_Largest_And_Smallest_By_AscendingOrder(arr, 3)


# method 2 : better approch
Time complexity: O(k+(n-k)*log(k))  , n = size of array

Space complexity: O(k)
import heapq




class Solution:
    def kth_Largest_MaxHeap(self, arr, k):
        pq = []
        n = len(arr)
        for i in range(n):
            heapq.heappush(pq, -arr[i])


        f = k - 1


        while f > 0:
            heapq.heappop(pq)
            f -= 1


        print("Kth Largest element", -pq[0])


    def kth_Smallest_MinHeap(self, arr, k):
        pq = []
        n = len(arr)


        for i in range(n):
            heapq.heappush(pq, arr[i])


        f = k - 1


        while f > 0:
            heapq.heappop(pq)
            f -= 1


        print("Kth Smallest element", pq[0])




if __name__ == "__main__":
    arr = [1, 2, 6, 4, 5, 3]


    obj = Solution()
    obj.kth_Largest_MaxHeap(arr, 3)
    obj.kth_Smallest_MinHeap(arr, 3)   


# method 3 : optimal solution
Time complexity: O(n) , where n = size of the array

Space complexity: O(1) 
from typing import List




def partition(arr: List[int], left: int, right: int) -> int:
    pivot = arr[left]
    l = left + 1
    r = right
    while l <= r:
        if arr[l] < pivot and arr[r] > pivot:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        if arr[l] >= pivot:
            l += 1
        if arr[r] <= pivot:
            r -= 1


    arr[left], arr[r] = arr[r], arr[left]
    return r




def kth_Largest_Element(arr: List[int], k: int) -> int:
    left = 0
    right = len(arr) - 1
    kth = 0
    while 1:
        idx = partition(arr, left, right)
        if idx == k - 1:
            kth = arr[idx]
            break
        if idx < k - 1:
            left = idx + 1
        else:
            right = idx - 1


    return kth




if __name__ == "__main__":
    arr = [12, 3, 5, 7, 4, 19, 26]
    n = len(arr)
    k = 1
    print(f"Kth Largest element is {kth_Largest_Element(arr, k)}")

# method 4/
Time complexity: O(n) ,where n = size of the array

Space complexity: O(1)
from typing import List




def partition(arr: List[int], l: int, r: int) -> int:
    f = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= f:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i




def kth_Smallest_Element(arr: List[int], l: int, r: int, k: int) -> int:
    if k <= r - l + 1 and k > 0:
        ind = partition(arr, l, r)
        if ind - l == k - 1:
            return arr[ind]
        if ind - l > k - 1:
            return kth_Smallest_Element(arr, l, ind - 1, k)
        return kth_Smallest_Element(arr, ind + 1, r, k - ind + l - 1)
    return float("inf")




if __name__ == "__main__":
    arr = [12, 3, 5, 7, 4, 19, 26]
    n = len(arr)
    k = 1
    print(f"Kth smallest element is {kth_Smallest_Element(arr, 0, n - 1, k)}")


# 3 TODO : sort K sorted array
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 4 TODO : merge M sorted lists
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 5 TODO : replace each array element by it's corresponding rank
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 6 TODO : task scheduler
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 7 TODO : hands of straights
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      




# endregion


# region 11.3 HEAP/PRIORITY QUEUE - HARD
# --------------------------------------

# 1 TODO :  design twitter
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 2 TODO : connect "n" ropes with minimal cost
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 3 TODO : Kth largest element in a stream of running integers
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 4 TODO : maximum sum combination
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 5 TODO : find median from data stream
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 6 TODO : K most frequent elements
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      



# endregion


# region 12.1 GREEDY ALGORITHM - EASY
# -----------------------------------

# 1 TODO :  assign cookies
Time Complexity: O(N logN + M logM + M) where N is the length of the greedy array, M is the length of the cookies array. To sort the greedy and cookies array, the complexity is O(N logN) and O(M logM).

After sorting, we iterate over the arrays at most M times as M is the total number of cookies.
Since each child and each cookie is considered at most once, the time complexity of this part is linear in terms of the size of the cookie array, which is O(M).
Space Complexity: O(1) as the algorithm uses only a constant amount of extra space regardless of the size of the input array. It does not require any additional data structures that scale with the input size.
                            
from typing import List

# Function to find the maximum
# number of content children
Time Complexity: O(N logN + M logM + M) where N is the length of the greedy array, M is the length of the cookies array. To sort the greedy and cookies array, the complexity is O(N logN) and O(M logM).

After sorting, we iterate over the arrays at most M times as M is the total number of cookies.
Since each child and each cookie is considered at most once, the time complexity of this part is linear in terms of the size of the cookie array, which is O(M).
Space Complexity: O(1) as the algorithm uses only a constant amount of extra space regardless of the size of the input array. It does not require any additional data structures that scale with the input size.
def findContentChildren(greed: List[int], cookieSize: List[int]) -> int:
    # Get the size of
    # the greed array
    n = len(greed)

    # Get the size of
    # the cookieSize array
    m = len(cookieSize)

    # Sort the greed factors in ascending
    # order to try and satisfy the
    # least greedy children first
    greed.sort()

    # Sort the cookie sizes in ascending
    # order to use the smallest cookies first
    cookieSize.sort()

    # Initialize a pointer for the
    # cookieSize array, starting
    # from the first cookie
    l = 0

    # Initialize a pointer for the
    # greed array, starting from
    # the first child
    r = 0

    # Iterate while there are
    # cookies and children
    # left to consider
    while l < m and r < n:
        # If the current cookie can
        # satisfy the current child's greed
        if greed[r] <= cookieSize[l]:
            # Move to the next child,
            # as the current child is satisfied
            r += 1
        # Always move to the next cookie
        # whether the current child
        # was satisfied or not
        l += 1

    # The value of r at the end of
    # the loop represents the number
    # of children that were satisfied
    return r

if __name__ == "__main__":
    greed = [1, 5, 3, 3, 4]
    cookieSize = [4, 2, 1, 2, 1, 3]
    
    print("Array Representing Greed: ", end="")
    for g in greed:
        print(g, end=" ")
    print()
    
    print("Array Representing Cookie Size: ", end="")
    for c in cookieSize:
        print(c, end=" ")
    print()
    
    ans = findContentChildren(greed, cookieSize)
    
    print(f"\nNo. of kids assigned cookies {ans}")
                           


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 2 TODO : fractional knapsack approch
# method 1 : brute force approch
Time Complexity: O(n log n + n). O(n log n) to sort the items and O(n) to iterate through all the items for calculating the answer.

Space Complexity: O(1), no additional data structure has been used.
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight




class Solution:
    def fractionalKnapsack(self, W, arr, n):
        arr.sort(key=lambda x: x.value / x.weight, reverse=True)
        curWeight = 0
        finalvalue = 0.0
        for i in range(n):
            if curWeight + arr[i].weight <= W:
                curWeight += arr[i].weight
                finalvalue += arr[i].value
            else:
                remain = W - curWeight
                finalvalue += arr[i].value / arr[i].weight * remain
                break
        return finalvalue




if __name__ == '__main__':
    n = 3
    W = 50
    arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
    obj = Solution()
    ans = obj.fractionalKnapsack(W, arr, n)
    print("The maximum value is", ans) 


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 3 TODO : greedy algorithm to find minimum number of coins
# method 1 : brute force approch
Time Complexity:O(V)

Space Complexity:O(1)

if __name__ == '__main__':
    V = 49
    ans = []
    coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    n = 9
    for i in range(n - 1, -1, -1):
        while V >= coins[i]:
            V -= coins[i]
            ans.append(coins[i])
    print("The minimum number of coins is", len(ans))
    print("The coins are")
    for i in range(len(ans)):
        print(ans[i], end=" ")  


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 4 TODO : lemonade charge
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(N) where N is the number of people in queue/ bills we will deal with. We iterate through each customer’s bills exactly once. The loop runs for N iterations and at each iteration the operations performed are constant time.

Space Complexity: O(1) as the algorithm uses only a constant amount of extra space regardless of the size of the input array. It does not require any additional data structures that scale with the input size.
                            
# Function to find whether each customer can 
# be provided with correct change
def lemonadeChange(bills):
    
    # Initialize a counter
    # for $5 bills
    five = 0 
    
    # Initialize a counter
    # for $10 bills
    ten = 0   
    
    # Iterate through each customer's bill
    for bill in bills:
        
        # If the customer's
        # bill is $5
        if bill == 5:
            
            # Increment the
            # count of $5 bills
            five += 1  
        
        # If the customer's
        # bill is $10
        elif bill == 10:
            
            # Check if there are $5
            # bills available to give change
            if five:
                 # Use one $5 bill
                 # to give change
                five -= 1 
                # Receive one $10 bill
                ten += 1   
            
            # If no $5 bill
            # available, return false
            else:
                return False  
        
        # If the customer's
        # bill is $20
        else:
            # Check if there are both
            # $5 and $10 bills
            # available to give change
            if five and ten:
                 # Use one $5 bill
                five -= 1 
                # Use one $10 bill
                ten -= 1   
            
            # If there are not enough $10 bills,
            # check if there are at least
            # three $5 bills available
            elif five >= 3:
                # Use three $5 bills
                # to give change
                five -= 3  
            
            # If unable to give
            # change, return false
            else:
                return False  
    
    # Return true if all customers
    # are served with correct change
    return True  

# Main function
def main():
    bills = [5, 5, 5, 10, 20]
    print("Queues of customers:", end=" ")
    for bill in bills:
        print(bill, end=" ")
    print()
    ans = lemonadeChange(bills)
    if ans:
        print("It is possible to provide change for all customers.")
    else:
        print("It is not possible to provide change for all customers.")

# Run the main function
if __name__ == "__main__":
    main()
                           
                          


# 5 TODO : valid paranthesis checker
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      



# endregion



# region 12.2 GREEDY ALGORITHM - MEDIUM/HARD
# ------------------------------------------

# 1 TODO :  N meetings in one room
# method 1 : brute force approch
Time Complexity: O(n) to iterate through every position and insert them in a data structure. O(n log n)  to sort the data structure in ascending order of end time. O(n)  to iterate through the positions and check which meeting can be performed.

Overall : O(n) +O(n log n) + O(n) ~O(n log n)

Space Complexity: O(n)  since we used an additional data structure for storing the start time, end time, and meeting no.
from typing import List




class meeting:
    def __init__(self, start, end, pos):
        self.start = start
        self.end = end
        self.pos = pos




class Solution:


    def maxMeetings(self, s: List[int], e: List[int], n: int) -> None:
        meet = [meeting(s[i], e[i], i + 1) for i in range(n)]
        sorted(meet, key=lambda x: (x.end, x.pos))
        answer = []
        limit = meet[0].end
        answer.append(meet[0].pos)
        for i in range(1, n):
            if meet[i].start > limit:
                limit = meet[i].end
                answer.append(meet[i].pos)
        print("The order in which the meetings will be performed is ")
        for i in answer:
            print(i, end=" ")




if __name__ == "__main__":
    obj = Solution()
    n = 6
    start = [1, 3, 0, 5, 8, 5]
    end = [2, 4, 5, 7, 9, 9]
    obj.maxMeetings(start, end, n)   


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 2 TODO : jump game - I
# method 1 : brute force approch
Time Complexity: O(N) where N is the length of the input array. We iterate through the input array exactly once and at each element perform constant time operations.

Space Complexity: O(1) as the algorithm uses only a constant amount of extra space regardless of the size of the input array. It does not require any additional data structures that scale with the input size.

                            
def can_jump(nums):
    # Initialize the maximum
    # index that can be reached
    max_index = 0

    # Iterate through each
    # index of the array
    for i in range(len(nums)):
        # If the current index is greater
        # than the maximum reachable index
        # it means we cannot move forward
        # and should return false
        if i > max_index:
            return False

        # Update the maximum index
        # that can be reached by comparing
        # the current max_index with the sum of
        # the current index and the
        # maximum jump from that index
        max_index = max(max_index, i + nums[i])

    # If we complete the loop,
    # it means we can reach the
    # last index
    return True


def main():
    nums = [4, 3, 7, 1, 2]

    print("Array representing maximum jump from each index: ", end="")
    for i in range(len(nums)):
        print(nums[i], end=" ")
    print()

    ans = can_jump(nums)

    if ans:
        print("It is possible to reach the last index.")
    else:
        print("It is not possible to reach the last index.")


if __name__ == "__main__":
    main()
                           
                        


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 3 TODO : jump game - II
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 4 TODO : minimum number of platforms required for a railway station
# method 1 : brute force approch
Time Complexity: O(n^2)  (due to two nested loops).

Space Complexity: O(1)  (no extra space used).
def countPlatforms(n, arr, dep):
    ans = 1  # final value
    for i in range(n):
        count = 1  # count of overlapping interval of only this iteration
        for j in range(i+1, n):
            if (arr[i] >= arr[j] and arr[i] <= dep[j]) or (arr[j] >= arr[i] and arr[j] <= dep[i]):
                count += 1
        ans = max(ans, count)  # updating the value
    return ans




if __name__ == "__main__":
    arr = [900, 945, 955, 1100, 1500, 1800]
    dep = [920, 1200, 1130, 1150, 1900, 2000]
    n = len(dep)
    print("Minimum number of Platforms required", countPlatforms(n, arr, dep))


# method 2 : better approch
Time Complexity: O(nlogn) Sorting takes O(nlogn) and traversal of arrays takes O(n) so overall time complexity is O(nlogn).

Space complexity: O(1)  (No extra space used).
def countPlatforms(arr, dep):
    arr.sort()
    dep.sort()


    ans = 1
    count = 1
    i = 1
    j = 0
    while i < len(arr) and j < len(dep):
        if arr[i] <= dep[j]:  # one more platform needed
            count += 1
            i += 1
        else:  # one platform can be reduced
            count -= 1
            j += 1
        ans = max(ans, count)  # updating the value with the current maximum
    return ans




if __name__ == "__main__":
    arr = [900, 945, 955, 1100, 1500, 1800]
    dep = [920, 1200, 1130, 1150, 1900, 2000]
    print("Minimum number of Platforms required ", countPlatforms(arr, dep))


# method 3 : optimal solution
# TC     -      
# SC     -      


# 5 TODO : job sequenceing problem
# method 1 : brute force approch
Time Complexity: O(N log N) + O(N*M).

O(N log N ) for sorting the jobs in decreasing order of profit. O(N*M) since we are iterating through all N jobs and for every job we are checking from the last deadline, say M deadlines in the worst case.

Space Complexity: O(M) for an array that keeps track of which day job is performed if M is the maximum deadline available.

class job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit




class Solution:
    def jobScheduling(self, jobs):
        jobs.sort(key=lambda x: x.profit, reverse=True)
        maxi = jobs[0].deadline
        for i in range(1, len(jobs)):
            maxi = max(maxi, jobs[i].deadline)


        slot = [-1] * (maxi + 1)
        countJobs = 0
        jobProfit = 0


        for i in range(len(jobs)):
            for j in range(jobs[i].deadline, 0, -1):
                if slot[j] == -1:
                    slot[j] = i
                    countJobs += 1
                    jobProfit += jobs[i].profit
                    break


        return countJobs, jobProfit




if __name__ == "__main__":
    jobs = [job(1, 4, 20), job(2, 1, 10), job(3, 2, 40), job(4, 2, 30)]
    count, profit = Solution().jobScheduling(jobs)
    print(count, profit)


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 6 TODO : candy
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 7 TODO : program for shortest job (one SNF) CPU scheduling
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(N logN + N) where N is the length of the jobs array. We sort the jobs array giving complexity O(N log N) and to calculate the waiting time we iterate through the sorted array taking O(N) complexity.

Space Complexity: O(1) as the algorithm uses only a constant amount of extra space regardless of the size of the input array. It does not require any additional data structures that scale with the input size.
                            
# Function to calculate average
# waiting time using Shortest
# Job First algorithm
def shortest_job_first(jobs):
    # Sort the jobs in ascending order
    jobs.sort()

    # Initialize total waiting time
    wait_time = 0
    # Initialize total time taken
    total_time = 0
    # Get the number of jobs
    n = len(jobs)

    # Iterate through each job
    # to calculate waiting time
    for i in range(n):

        # Add current total
        # time to waiting time
        wait_time += total_time

        # Add current job's
        # time to total time
        total_time += jobs[i]

    # Return the average waiting time
    return wait_time / n

if __name__ == "__main__":
    jobs = [4, 3, 7, 1, 2]

    print("Array Representing Job Durations:", end=" ")
    for job in jobs:
        print(job, end=" ")
    print()

    ans = shortest_job_first(jobs)
    print("Average waiting time:", ans)
                           
                            


# 8 TODO : program for least recently used (LRU) page replacement algorithm
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 9 TODO : insert interval
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 10 TODO :  merge intervals
# method 1 : brute force approch
Time Complexity: O(N*logN) + O(2*N), where N = the size of the given array.
Reason: Sorting the given array takes  O(N*logN) time complexity. Now, after that, we are using 2 loops i and j. But while using loop i, we skip all the intervals that are merged with loop j. So, we can conclude that every interval is roughly visited twice(roughly, once for checking or skipping and once for merging). So, the time complexity will be 2*N instead of N2.

Space Complexity: O(N), as we are using an answer list to store the merged intervals. Except for the answer array, we are not using any extra space.



from typing import List

def mergeOverlappingIntervals(arr: List[List[int]]) -> List[List[int]]:
    n = len(arr) # size of the array

    # sort the given intervals:
    arr.sort()

    ans = []

    for i in range(n): # select an interval:
        start, end = arr[i][0], arr[i][1]

        # Skip all the merged intervals:
        if ans and end <= ans[-1][1]:
            continue

        # check the rest of the intervals:
        for j in range(i + 1, n):
            if arr[j][0] <= end:
                end = max(end, arr[j][1])
            else:
                break
        ans.append([start, end])
    return ans

if __name__ == '__main__':
    arr = [[1, 3], [8, 10], [2, 6], [15, 18]]
    ans = mergeOverlappingIntervals(arr)
    print("The merged intervals are:")
    for it in ans:
        print(f"[{it[0]}, {it[1]}]", end=" ")
    print()



  


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(N*logN) + O(N), where N = the size of the given array.
Reason: Sorting the given array takes  O(N*logN) time complexity. Now, after that, we are just using a single loop that runs for N times. So, the time complexity will be O(N).

Space Complexity: O(N), as we are using an answer list to store the merged intervals. Except for the answer array, we are not using any extra space.




from typing import List

def mergeOverlappingIntervals(arr: List[List[int]]) -> List[List[int]]:
    n = len(arr) # size of the array

    # sort the given intervals:
    arr.sort()

    ans = []

    for i in range(n):
        # if the current interval does not
        # lie in the last interval:
        if not ans or arr[i][0] > ans[-1][1]:
            ans.append(arr[i])
        # if the current interval
        # lies in the last interval:
        else:
            ans[-1][1] = max(ans[-1][1], arr[i][1])
    return ans

if __name__ == '__main__':
    arr = [[1, 3], [8, 10], [2, 6], [15, 18]]
    ans = mergeOverlappingIntervals(arr)
    print("The merged intervals are:")
    for it in ans:
        print(f"[{it[0]}, {it[1]}]", end=" ")
    print()






# 11 TODO : non-overlapping intervals
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      



# endregion


# region 13.1 BINARY TREES - TRAVERSALS
# -------------------------------------

# 1 TODO :  introduction to trees
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 2 TODO : binary tree representation in C++
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 3 TODO : binary tree representation in java
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 4 TODO : binary tree traversals in binary tree
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 5 TODO : preorder traversals of binary tree
# method 1 : brute force approch
Time Complexity: O(N) where N is the number of nodes in the binary tree as each node of the binary tree is visited exactly once.

Space Complexity: O(N) where N is the number of nodes in the binary tree as an additional space for array is allocated to store the values of all ‘N’ nodes of the binary tree.
                            
# Node class for
# the binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Function to perform preorder traversal
# of the tree and store values in 'arr'
def preorder(root, arr):
    # If the current node is None
    # (base case for recursion), return
    if not root:
        return
    # Append the current node's
    # value into the list
    arr.append(root.data)
    # Recursively traverse
    # the left subtree
    preorder(root.left, arr)
    # Recursively traverse
    # the right subtree
    preorder(root.right, arr)

# Function to initiate preorder traversal
# and return the resulting list
def preOrder(root):
    # Create an empty list to
    # store preorder traversal values
    arr = []
    # Call the preorder traversal function
    preorder(root, arr)
    # Return the resulting list
    # containing preorder traversal values
    return arr

# Main function
if __name__ == "__main__":
    # Creating a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Getting preorder traversal
    result = preOrder(root)

    # Displaying the preorder traversal result
    print("Preorder Traversal:", end=" ")
    # Output each value in the
    # preorder traversal result
    for val in result:
        print(val, end=" ")
    print()
                            
                         


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 6 TODO : inorder traversal of binary tree
# method 1 : brute force approch
Time Complexity: O(N) where N is the number of nodes in the binary tree as each node of the binary tree is visited exactly once.

Space Complexity: O(N) where N is the number of nodes in the binary tree. This is because the recursive stack uses an auxiliary space which can potentially hold all nodes in the tree when dealing with a skewed tree (all nodes have only one child), consuming space proportional to the number of nodes.In the average case or for a balanced tree, the maximum number of nodes that could be in the stack at any given time would be roughly the height of the tree hence O(log2N).

                            
# Node class for the binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Function to perform inorder traversal
# of the tree and store values in 'arr'
def inorder(root, arr):
    # If the current node is None
    # (base case for recursion), return
    if root is None:
        return
    # Recursively traverse the left subtree
    inorder(root.left, arr)
    # Append the current node's
    # value into the list
    arr.append(root.data)
    # Recursively traverse 
    # the right subtree
    inorder(root.right, arr)

# Function to initiate inorder traversal
# and return the resulting list
def in_order(root):
    # Create an empty list to
    # store inorder traversal values
    arr = []
    # Call the inorder traversal function
    inorder(root, arr)
    # Return the resulting list
    # containing inorder traversal values
    return arr

# Main function
if __name__ == "__main__":
    # Creating a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Getting inorder traversal
    result = in_order(root)

    # Displaying the inorder traversal result
    print("Inorder Traversal:", end=" ")
    # Output each value in the
    # inorder traversal result
    for val in result:
        print(val, end=" ")
    print()
                           
                        


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 7 TODO : post order traversal of binary tree
# method 1 : brute force approch
Time Complexity: O(N) where N is the number of nodes in the binary tree as each node of the binary tree is visited exactly once.

Space Complexity: O(N) where N is the number of nodes in the binary tree as an additional space for array is allocated to store the values of all ‘N’ nodes of the binary tree.
                            
# Node class for the binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Function to perform postorder
# traversal recursively
def postorder(root, arr):
    # Base case: if root is None, return
    if root is None:
        return
    # Traverse left subtree
    postorder(root.left, arr)
    # Traverse right subtree
    postorder(root.right, arr)
    # Visit the node
    # (append node's data to the list)
    arr.append(root.data)

# Function to get the postorder
# traversal of a binary tree
def postOrder(root):
    # Create a list to
    # store the traversal result
    arr = []
    # Perform postorder traversal
    # starting from the root
    postorder(root, arr)
    # Return the postorder
    # traversal result
    return arr

# Function to print the
# elements of a list
def printList(lst):
    # Iterate through the list
    # and print each element
    for num in lst:
        print(num, end=" ")
    print()

# Main function
if __name__ == "__main__":
    # Creating a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Getting postorder traversal
    result = postOrder(root)

    # Printing the postorder
    # traversal result
    print("Postorder traversal: ", end="")
    printList(result)
                            
                        


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 8 TODO : level order traversal / level order traversal in spiral form
# method 1 : brute force approch
Time Complexity: O(N) where N is the number of nodes in the binary tree. Each node of the binary tree is enqueued and dequeued exactly once, hence all nodes need to be processed and visited. Processing each node takes constant time operations which contributes to the overall linear time complexity.

Space Complexity: O(N) where N is the number of nodes in the binary tree. In the worst case, the queue has to hold all the nodes of the last level of the binary tree, the last level could at most hold N/2 nodes hence the space complexity of the queue is proportional to O(N).The resultant vector answer also stores the values of the nodes level by level and hence contains all the nodes of the tree contributing to O(N) space as well.
                            
from collections import deque

# TreeNode class represents
# a node in a binary tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        # Create a list to store levels
        ans = []
        if not root:
            # If the tree is empty,
            # return an empty list
            return ans

        # Create a queue to store nodes
        # for level-order traversal
        q = deque()
        # Enqueue the root node
        q.append(root)

        while q:
            # Get the size of the current level
            size = len(q)
            # Create a list to store
            # nodes at the current level
            level = []

            for i in range(size):
                # Get the front node in the queue
                node = q.popleft()
                # Store the node value
                # in the current level list
                level.append(node.val)

                # Enqueue the child nodes if they exist
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # Store the current level
            # in the answer list
            ans.append(level)
        # Return the level-order
        # traversal of the tree
        return ans

# Function to print
# the elements of a list
def printList(lst):
    # Iterate through the
    # list and print each element
    for num in lst:
        print(num, end=" ")
    print()

# Main function
if __name__ == "__main__":
    # Creating a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Create an instance
    # of the Solution class
    solution = Solution()
    # Perform level-order traversal
    result = solution.levelOrder(root)

    print("Level Order Traversal of Tree:")

    # Printing the level order traversal result
    for level in result:
        printList(level)
                           
                         


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 9 TODO : iterative preorder traversal of binary tree
# method 1 : brute force approch
Time Complexity: O(N) where N is the number of nodes in the binary tree. Every node of the binary tree is visited exactly once, and for each node, , the operations performed (pushing and popping from the stack, accessing node values, etc.) are constant time operations.

Space Complexity: O(N) where N is the number of nodes in the binary tree. This is because the stack can potentially hold all nodes in the tree when dealing with a skewed tree (all nodes have only one child), consuming space proportional to the number of nodes.
                            
from typing import List

# Define the TreeNode structure
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Function to perform preorder traversal
    # of a binary tree iteratively
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # Initialize list to store
        # the preorder traversal result
        preorder = []
        
        # If the root is None, return
        # an empty traversal result
        if root is None:
            return preorder
        
        # Create a stack to store
        # nodes during traversal
        st = []
        # Push the root node
        # onto the stack
        st.append(root)
        
        # Perform iterative preorder traversal
        while st:
            # Get the current node
            # from the top of the stack
            root = st.pop()
            
            # Add the node's value to
            # the preorder traversal result
            preorder.append(root.val)
            
            # Push the right child
            # onto the stack if exists
            if root.right:
                st.append(root.right)
            
            # Push the left child onto
            # the stack if exists
            if root.left:
                st.append(root.left)
        
        # Return the preorder
        # traversal result
        return preorder

# Creating a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Initializing the Solution class
sol = Solution()

# Getting the preorder traversal
result = sol.preorderTraversal(root)

# Displaying the preorder traversal result
print("Preorder Traversal:", end=" ")
for val in result:
    print(val, end=" ")
print()
                           
                           


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 10 TODO :  iterative inorder traversal of binary tree
# method 1 : brute force approch
Time Complexity: O(N) where N is the number of nodes in the binary tree as each node of the binary tree is visited exactly once.

Space Complexity: O(N) where N is the number of nodes in the binary tree. This is because the recursive stack uses an auxiliary space which can potentially hold all nodes in the tree when dealing with a skewed tree (all nodes have only one child), consuming space proportional to the number of nodes.In the average case or for a balanced tree, the maximum number of nodes that could be in the stack at any given time would be roughly the height of the tree hence O(log2N).
                            
# Node class for the binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Function to perform inorder traversal
# of the tree and store values in 'arr'
def inorder(root, arr):
    # If the current node is None
    # (base case for recursion), return
    if root is None:
        return
    # Recursively traverse the left subtree
    inorder(root.left, arr)
    # Append the current node's
    # value into the list
    arr.append(root.data)
    # Recursively traverse 
    # the right subtree
    inorder(root.right, arr)

# Function to initiate inorder traversal
# and return the resulting list
def in_order(root):
    # Create an empty list to
    # store inorder traversal values
    arr = []
    # Call the inorder traversal function
    inorder(root, arr)
    # Return the resulting list
    # containing inorder traversal values
    return arr

# Main function
if __name__ == "__main__":
    # Creating a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Getting inorder traversal
    result = in_order(root)

    # Displaying the inorder traversal result
    print("Inorder Traversal:", end=" ")
    # Output each value in the
    # inorder traversal result
    for val in result:
        print(val, end=" ")
    print()
                           
                        

# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 11 TODO : post order traversal of binary tree using 2-stack
# method 1 : brute force approch
Time Complexity: O(2N) where N is the number of nodes in the Binary Tree. The traversal process visits each node in the Binary Tree exactly once to push into stack1 and stack2. Then after the tree is traversed and the nodes are popped from stack2 to push into the postorder array.

Space Complexity: O(2N) where N is the number of nodes in the Binary Tree. The space occupied by the two stacks depend on the height of the binary tree. In the worst-case scenario, if the tree is skewed, the space complexity would be O(N) as both stacks could potentially hold all nodes at different points during traversal.The postorder array also holds all nodes from the binary tree hence giving another O(N) + O(N) ~ O(2N).

                            
# Node class for the binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Function to return the postOrder
# traversal of a binary tree using
# two stacks
def postOrder(root):
    # Vector to store
    # postorder traversal
    postorder = []

    # If the tree is empty,
    # return an empty traversal
    if root is None:
        return postorder

    # Two stacks for
    # iterative traversal
    st1, st2 = [], []

    # Push the root node
    # onto the first stack
    st1.append(root)

    # Iterative traversal to populate
    # st2 with nodes in postorder
    while st1:
        # Get the top node from st1
        root = st1.pop()

        # Push the node onto st2
        st2.append(root)

        # Push left child onto st1 if exists
        if root.left is not None:
            st1.append(root.left)

        # Push right child onto st1 if exists
        if root.right is not None:
            st1.append(root.right)

    # Populate the postorder traversal
    # list by popping st2
    while st2:
        postorder.append(st2[-1].data)
        st2.pop()

    # Return the
    # postorder traversal
    return postorder


# Function to print the
# elements of a list
def printList(lst):
    # Iterate through the list
    # and print each element
    for num in lst:
        print(num, end=" ")
    print()

# Main function
if __name__ == "__main__":
    # Creating a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Getting postorder traversal
    result = postOrder(root)

    # Printing the postorder
    # traversal result
    print("Postorder traversal: ", end="")
    printList(result)
                           
                          


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 12 TODO : post-order traversal of binary tree using 1 stack
# method 1 : brute force approch
Time Complexity: O(N) where N is the number of nodes in the binary tree as each node of the binary tree is visited exactly once.

Space Complexity: O(N) where N is the number of nodes in the binary tree as an additional space for array is allocated to store the values of all ‘N’ nodes of the binary tree.
                            
# Node class for the binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Function to perform postorder
# traversal recursively
def postorder(root, arr):
    # Base case: if root is None, return
    if root is None:
        return
    # Traverse left subtree
    postorder(root.left, arr)
    # Traverse right subtree
    postorder(root.right, arr)
    # Visit the node
    # (append node's data to the list)
    arr.append(root.data)

# Function to get the postorder
# traversal of a binary tree
def postOrder(root):
    # Create a list to
    # store the traversal result
    arr = []
    # Perform postorder traversal
    # starting from the root
    postorder(root, arr)
    # Return the postorder
    # traversal result
    return arr

# Function to print the
# elements of a list
def printList(lst):
    # Iterate through the list
    # and print each element
    for num in lst:
        print(num, end=" ")
    print()

# Main function
if __name__ == "__main__":
    # Creating a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Getting postorder traversal
    result = postOrder(root)

    # Printing the postorder
    # traversal result
    print("Postorder traversal: ", end="")
    printList(result)
                            
                           


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 13 TODO : preorder, inorder and post order traversal in one traversal
# method 1 : brute force approch
Time Complexity: O(3N) where N is the number of nodes in the Binary Tree. Each node is processed once for each traversal type (pre-order, in-order, and post-order). Hence, the algorithm effectively visits each node three times in total across the three traversal types.

Space Complexity: O(4N) where N is the number of nodes in the Binary Tree. The following additional data structures are used:A stack to maintain traversal states, requiring additional space proportional to the maximum number of nodes in the stack at any point during traversal.Three vectors to store the preorder, inorder and postorder traversal. These arrays collectively occupy space proportional to the total number of nodes in the tree. Hence, 3N is added to the space complexity.

                            
# Node class for the binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Function to get the Preorder,
# Inorder and Postorder traversal
# Of Binary Tree in One traversal
def pre_in_post_traversal(root):
    # Lists to store traversals
    pre, in_order, post = [], [], []

    # If the tree is empty,
    # return empty traversals
    if root is None:
        return []

    # Stack to maintain nodes
    # and their traversal state
    stack = [(root, 1)]

    while stack:
        node, state = stack.pop()

        # this is part of pre
        if state == 1:
            # Store the node's data
            # in the preorder traversal
            pre.append(node.data)
            # Move to state 2
            # (inorder) for this node
            state = 2
            # Push the updated state
            # back onto the stack
            stack.append((node, state))

            # Push left child onto
            # the stack for processing
            if node.left:
                stack.append((node.left, 1))

        # this is a part of in
        elif state == 2:
            # Store the node's data
            # in the inorder traversal
            in_order.append(node.data)
            # Move to state 3
            # (postorder) for this node
            state = 3
            # Push the updated state
            # back onto the stack
            stack.append((node, state))

            # Push right child onto
            # the stack for processing
            if node.right:
                stack.append((node.right, 1))

        # this is part of post
        else:
            # Store the node's data
            # in the postorder traversal
            post.append(node.data)

    # Returning the traversals
    return [pre, in_order, post]

# Function to print the
# elements of a list
def print_list(lst):
    # Iterate through the list
    # and print each element
    for num in lst:
        print(num, end=" ")
    print()

# Main function
if __name__ == "__main__":
    # Creating a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Getting the pre-order, in-order,
    # and post-order traversals
    traversals = pre_in_post_traversal(root)

    # Extracting the traversals
    # from the result
    pre, in_order, post = traversals

    # Printing the traversals
    print("Preorder traversal: ", end="")
    print_list(pre)

    print("Inorder traversal: ", end="")
    print_list(in_order)

    print("Postorder traversal: ", end="")
    print_list(post)
                           
                        


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# endregion



# region 13.2 BINARY TREES - MEDIUM
# ----------------------------------

# 1 TODO :  height of a binary tree
# method 1 : brute force approch
Time Complexity: O(N) where N is the number of nodes in the Binary Tree. This complexity arises from visiting each node exactly once during the traversal to determine the maximum depth.

Space Complexity: O(N) where N is the number of nodes in the Binary Tree because in the worst case scenario the tree is balanced and has N/2 nodes in its last level which will have to be stored in the queue.
                            
from queue import Queue

# Node class for the binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    # Function to find the
    # maximum depth of a binary tree
    # using level order traversal
    def maxDepth(self, root):
        # If the root is NULL
        # (empty tree), depth is 0
        if root is None:
            return 0
        
        # Create a queue for
        # level order traversal
        q = Queue()
        level = 0
        
        # Push the root node into the queue
        q.put(root)
        
        # While there are nodes in the queue
        while not q.empty():
            # Get the number of nodes
            # at the current level
            size = q.qsize()
            
            # Process all nodes
            # at the current level
            for i in range(size):
                # Get the front node in the queue
                front = q.get()
                
                # Enqueue left child if exists
                if front.left is not None:
                    q.put(front.left)
                
                # Enqueue right child if exists
                if front.right is not None:
                    q.put(front.right)
            
            # Increment level to
            # move to the next level
            level += 1
        
        # Return the level, which represents
        # the maximum depth of the tree
        return level

# Creating a sample binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)
root.left.right.right.right = Node(7)

solution = Solution()
depth = solution.maxDepth(root)

print("Maximum depth of the binary tree:", depth)
                           
                            


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 2 TODO : check if the binary tree is height-balanced or not
# method 1 : brute force approch
Time Complexity: O(N2) where N is the number of nodes in the Binary Tree.This arises as we calculate the height of each node and to calculate the height for each node, we traverse the tree which is proportional to the number of nodes. Since this calculation is performed for each node in the tree, the complexity becomes: O(N x N) ~ O(N2).

Space Complexity : O(1) as no additional data structures or memory is allocated.O(H): Recursive Stack Space is used to calculate the height of the tree at each node which is proportional to the height of the tree.The recursive nature of the getHeight function, which incurs space on the call stack for each recursive call until it reaches the leaf nodes or the height of the tree.
                                
# Node structure for the binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    # Function to check if a binary tree is balanced
    def isBalanced(self, root):
        # If the tree is empty, it's balanced
        if not root:
            return True
        
        # Calculate the height of left and right subtrees
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)

        # Check if the absolute difference in heights
        # of left and right subtrees is <= 1
        if abs(leftHeight - rightHeight) <= 1 \
            and self.isBalanced(root.left) \
            and self.isBalanced(root.right):
            return True

        # If any condition fails, the tree is unbalanced
        return False

    # Function to calculate the height of a subtree
    def getHeight(self, root):
        # Base case: if the current node is NULL,
        # return 0 (height of an empty tree)
        if not root:
            return 0
        
        # Recursively calculate the height
        # of left and right subtrees
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        
        # Return the maximum height of left and right subtrees
        # plus 1 (to account for the current node)
        return max(leftHeight, rightHeight) + 1

# Creating a sample binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)
root.left.right.right.right = Node(7)

# Creating an instance of the Solution class
solution = Solution()

# Checking if the tree is balanced
if solution.isBalanced(root):
    print("The tree is balanced.")
else:
    print("The tree is not balanced.")
                                
                               


# method 2 : better approch
Time Complexity: O(N) where N is the number of nodes in the Binary Tree. This complexity arises from visiting each node exactly once during the postorder traversal.

Space Complexity : O(1) as no additional space or data structures is created that is proportional to the input size of the tree. O(H) Recursive Stack Auxiliary Space : The recursion stack space is determined by the maximum depth of the recursion, which is the height of the binary tree denoted as H. In the balanced case it is log2N and in the worst case its N.
                                
# Node class for the binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    # Function to check if a binary tree is balanced
    def isBalanced(self, root):
        # Check if the tree's height difference
        # between subtrees is less than 2
        # If not, return False; otherwise, return True
        return self.dfsHeight(root) != -1

    # Recursive function to calculate
    # the height of the tree
    def dfsHeight(self, root):
        # Base case: if the current node is None,
        # return 0 (height of an empty tree)
        if not root:
            return 0

        # Recursively calculate the
        # height of the left subtree
        left_height = self.dfsHeight(root.left)

        # If the left subtree is unbalanced,
        # propagate the unbalance status
        if left_height == -1:
            return -1

        # Recursively calculate the
        # height of the right subtree
        right_height = self.dfsHeight(root.right)

        # If the right subtree is unbalanced,
        # propagate the unbalance status
        if right_height == -1:
            return -1

        # Check if the difference in height between
        # left and right subtrees is greater than 1
        # If it's greater, the tree is unbalanced,
        # return -1 to propagate the unbalance status
        if abs(left_height - right_height) > 1:
            return -1

        # Return the maximum height of left and
        # right subtrees, adding 1 for the current node
        return max(left_height, right_height) + 1


# Creating a sample binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)
root.left.right.right.right = Node(7)

# Creating an instance of the Solution class
solution = Solution()

# Checking if the tree is balanced
if solution.isBalanced(root):
    print("The tree is balanced.")
else:
    print("The tree is not balanced.")                                   

                                
                            


# method 3 : optimal solution
# TC     -      
# SC     -      


# 3 TODO : diameter of a binary tree
# method 1 : brute force approch
Time Complexity: O(N*N) where N is the number of nodes in the Binary Tree.

This arises as we calculate the diameter of each node and to calculate the height of its left and right children, we traverse the tree which is proportional to the number of nodes.
Since this calculation is performed for each node in the tree, the complexity becomes: O(N x N) ~ O(N2).
Space Complexity : O(1) as no additional data structures or memory is allocated.O(H): Recursive Stack Space is used to calculate the height of the tree at each node which is proportional to the height of the tree.The recursive nature of the getHeight function, which incurs space on the call stack for each recursive call until it reaches the leaf nodes or the height of the tree.

                                
# Node structure for
# the binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        # Global variable to
        # store the diameter
        self.diameter = 0  

    # Function to calculate
    # the height of a subtree
    def calculateHeight(self, node):
        if node is None:
            return 0

        # Recursively calculate the
        # height of left and right subtrees
        left_height = self.calculateHeight(node.left)
        right_height = self.calculateHeight(node.right)

        # Calculate the diameter at the current
        # node and update the global variable
        self.diameter = max(self.diameter, left_height + right_height)

        # Return the height
        # of the current subtree
        return 1 + max(left_height, right_height)

    # Function to find the
    # diameter of a binary tree
    def diameterOfBinaryTree(self, root):
        # Start the recursive
        # traversal from the root
        self.calculateHeight(root)

        # Return the maximum diameter
        # found during traversal
        return self.diameter

# Main function
if __name__ == "__main__":
    # Creating a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.right = Node(6)
    root.left.right.right.right = Node(7)

    # Creating an instance of the Solution class
    solution = Solution()

    # Calculate the diameter of the binary tree
    diameter = solution.diameterOfBinaryTree(root)

    print("The diameter of the binary tree is:", diameter)

                                
                            


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(N) where N is the number of nodes in the Binary Tree. This complexity arises from visiting each node exactly once during the postorder traversal.

Space Complexity : O(1) as no additional space or data structures is created that is proportional to the input size of the tree. O(H) Recursive Stack Auxiliary Space : The recursion stack space is determined by the maximum depth of the recursion, which is the height of the binary tree denoted as H. In the balanced case it is log2N and in the worst case its N.

                                
                     
# Node class for the binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Solution class to find the diameter of the binary tree
class Solution:
    def diameterOfBinaryTree(self, root):
        # Initialize the variable to store the diameter of the tree
        diameter = [0]
        # Call the height function to traverse the tree and calculate diameter
        self.height(root, diameter)
        # Return the calculated diameter
        return diameter[0]

    # Function to calculate the height of the tree and update the diameter
    def height(self, node, diameter):
        # Base case: If the node is None, return 0 indicating the height of an empty tree
        if not node:
            return 0

        # Recursively calculate the height of left and right subtrees
        lh = self.height(node.left, diameter)
        rh = self.height(node.right, diameter)

        # Update the diameter with the maximum of current diameter or sum of left and right heights
        diameter[0] = max(diameter[0], lh + rh)

        # Return the height of the current node's subtree
        return 1 + max(lh, rh)


# Main function
if __name__ == "__main__":
    # Creating a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.right = Node(6)
    root.left.right.right.right = Node(7)

    # Creating an instance of the Solution class
    solution = Solution()

    # Calculate the diameter of the binary tree
    diameter = solution.diameterOfBinaryTree(root)

    print("The diameter of the binary tree is:", diameter)
                                
                            


# 4 TODO : maximum path sum
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(N) where N is the number of nodes in the Binary Tree. This complexity arises from visiting each node exactly once during the recursive traversal.

Space Complexity: O(1) as no additional space or data structures is created that is proportional to the input size of the tree. O(H) Recursive Stack Auxiliary Space : The recursion stack space is determined by the maximum depth of the recursion, which is the height of the binary tree denoted as H. In the balanced case it is log2N and in the worst case its N.
                            
class Node:
    def __init__(self, val):
        # Constructor to initialize
        # the node with a value
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def findMaxPathSum(self, root, maxi):
        # Recursive function to find the maximum path sum
        # for a given subtree rooted at 'root'
        # The variable 'maxi' is a reference parameter
        # updated to store the maximum path sum encountered

        # Base case: If the current node is None, return 0
        if root is None:
            return 0

        # Calculate the maximum path sum
        # for the left and right subtrees
        leftMaxPath = max(0, self.findMaxPathSum(root.left, maxi))
        rightMaxPath = max(0, self.findMaxPathSum(root.right, maxi))

        # Update the overall maximum
        # path sum including the current node
        maxi[0] = max(maxi[0], leftMaxPath + rightMaxPath + root.data)

        # Return the maximum sum considering
        # only one branch (either left or right)
        # along with the current node
        return max(leftMaxPath, rightMaxPath) + root.data

    def maxPathSum(self, root):
        # Function to find the maximum
        # path sum for the entire binary tree

        # Initialize maxi to the
        # minimum possible integer value
        maxi = [float('-inf')] 
        # Call the recursive function to
        # find the maximum path sum
        self.findMaxPathSum(root, maxi)
        # Return the final maximum path sum
        return maxi[0]

# Creating a sample binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)
root.left.right.right.right = Node(7)

# Creating an instance of the Solution class
solution = Solution()

# Finding and printing the maximum path sum
maxPathSum = solution.maxPathSum(root)
print("Maximum Path Sum:", maxPathSum)
                           
                          


# 5 TODO : check if two trees are identical or not
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


Time Complexity: O(N+M) where N is the number of nodes in the first Binary Tree and M is the number of nodes in the second Binary Tree. This complexity arises from visiting each node of the two binary nodes during their comparison.

Space Complexity: O(1) as no additional space or data structures is created that is proportional to the input size of the tree. O(H) Recursive Stack Auxiliary Space : The recursion stack space is determined by the maximum depth of the recursion, which is the height of the binary tree denoted as H. In the balanced case it is log2N and in the worst case (its N).
                            
# Node structure for the binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Solution class with a function to check if two binary trees are identical
class Solution:
    def isIdentical(self, node1, node2):
        # If both nodes are None, they are identical
        if node1 is None and node2 is None:
            return True
        # If only one of the nodes is None, they are not identical
        if node1 is None or node2 is None:
            return False
        # Check if the current nodes have the same data value
        # and recursively check their left and right subtrees
        return (node1.data == node2.data
                and self.isIdentical(node1.left, node2.left)
                and self.isIdentical(node1.right, node2.right))

# Creating nodes for binary trees in Python
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)

# Creating an instance of the Solution class
solution = Solution()

# Checking if the binary trees are identical
if solution.isIdentical(root1, root2):
    print("The binary trees are identical.")
else:
    print("The binary trees are not identical.")
                           
                          


# 6 TODO : zig-zag traversal of binary tree
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(N) where N is the number of nodes in the binary tree. Each node of the binary tree is enqueued and dequeued exactly once, hence all nodes need to be processed and visited. Processing each node takes constant time operations which contributes to the overall linear time complexity.

Space Complexity: O(N) where N is the number of nodes in the binary tree. In the worst case, the queue has to hold all the nodes of the last level of the binary tree, the last level could at most hold N/2 nodes hence the space complexity of the queue is proportional to O(N). The resultant vector answer also stores the values of the nodes level by level and hence contains all the nodes of the tree contributing to O(N) space as well.
                            
from collections import deque

# Node class for the binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    # Function to perform zigzag level order traversal of a binary tree
    def ZigZagLevelOrder(self, root):
        # List to store the result of zigzag traversal
        result = []
        
        # Check if the root is None, return an empty result
        if not root:
            return result
        
        # Queue to perform level order traversal
        nodesQueue = deque()
        nodesQueue.append(root)
        
        # Flag to determine the direction of traversal (left to right or right to left)
        leftToRight = True
        
        # Continue traversal until the queue is empty
        while nodesQueue:
            # Get the number of nodes at the current level
            size = len(nodesQueue)
            
            # List to store the values of nodes at the current level
            row = [0] * size
            
            # Traverse nodes at the current level
            for i in range(size):
                # Get the front node from the queue
                node = nodesQueue.popleft()
                
                # Determine the index to insert the node's value based on the traversal direction
                index = i if leftToRight else (size - 1 - i)
                
                # Insert the node's value at the determined index
                row[index] = node.data
                
                # Enqueue the left and right children if they exist
                if node.left:
                    nodesQueue.append(node.left)
                if node.right:
                    nodesQueue.append(node.right)
            
            # Switch the traversal direction for the next level
            leftToRight = not leftToRight
            
            # Add the current level's values to the result list
            result.append(row)
        
        # Return the final result of zigzag level order traversal
        return result

# Helper function to print the result
def printResult(result):
    for row in result:
        for val in row:
            print(val, end=" ")
        print()

# Creating a sample binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

solution = Solution()

# Get the zigzag level order traversal
result = solution.ZigZagLevelOrder(root)

# Print the result
printResult(result)
                           
                         


# 7 TODO : boundary traversal of binary tree
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(N) where N is the number of nodes in the Binary Tree.

Adding the left boundary of the Binary Tree results in the traversal of the left side of the tree which is proportional to the the height of the three hence O(H) ie. O(log2N). In the worst case that the tree is skewed the complexity would be O(N).
For the bottom traversal of the Binary Tree, traversing the leaves is proportional to O(N) as preorder traversal visits every node once.
Adding the right boundary of the Binary Tree results in the traversal of the right side of the tree which is proportional to the the height of the three hence O(H) ie. O(log2N). In the worst case that the tree is skewed the complexity would be O(N).
Since all these operations are performed sequentially, the overall time complexity is dominated by the most expensive operation, which is O(N).
Space Complexity: O(N) where N is the number of nodes in the Binary Tree to store the boundary nodes of the tree. O(H) or O(log2N) Recursive stack space while traversing the tree. In the worst case scenario the tree is skewed and the auxiliary recursion stack space would be stacked up to the maximum depth of the tree, resulting in an O(N) auxiliary space complexity.
                            
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def isLeaf(self, root):
        """
        Function to check if a node is a leaf
        """
        return not root.left and not root.right

    def addLeftBoundary(self, root, res):
        """
        Function to add the left boundary of the tree
        """
        curr = root.left
        while curr:
            if not self.isLeaf(curr):
                # If the current node is not a leaf,
                # add its value to the result
                res.append(curr.data)
            # Move to the left child if it exists,
            # otherwise move to the right child
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right

    def addRightBoundary(self, root, res):
        """
        Function to add the right boundary of the tree
        """
        curr = root.right
        temp = []
        while curr:
            if not self.isLeaf(curr):
                # If the current node is not a leaf,
                # add its value to a temporary vector
                temp.append(curr.data)
            # Move to the right child if it exists,
            # otherwise move to the left child
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
        # Reverse and add the values from
        # the temporary vector to the result
        for i in range(len(temp) - 1, -1, -1):
            res.append(temp[i])

    def addLeaves(self, root, res):
        """
        Function to add the leaves of the tree
        """
        if self.isLeaf(root):
            # If the current node is a leaf,
            # add its value to the result
            res.append(root.data)
            return
        # Recursively add leaves of
        # the left and right subtrees
        if root.left:
            self.addLeaves(root.left, res)
        if root.right:
            self.addLeaves(root.right, res)

    def printBoundary(self, root):
        """
        Main function to perform the
        boundary traversal of the binary tree
        """
        res = []
        if not root:
            return res
        # If the root is not a leaf,
        # add its value to the result
        if not self.isLeaf(root):
            res.append(root.data)

        # Add the left boundary, leaves,
        # and right boundary in order
        self.addLeftBoundary(root, res)
        self.addLeaves(root, res)
        self.addRightBoundary(root, res)

        return res

# Helper function to
# print the result
def printResult(result):
    for val in result:
        print(val, end=" ")
    print()

# Creating a sample binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

solution = Solution()

# Get the boundary traversal
result = solution.printBoundary(root)

# Print the result
print("Boundary Traversal:", end=" ")
printResult(result)
                           
                         


# 8 TODO : vertical order traversal of binary tree
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(N * log2N * log2N * log2N) where N represents the number of nodes in the Binary Tree.

Postorder Traversal performed using BFS as a time complexity of O(N) as we are visiting each and every node once.
Multiset Operations to insert overlapping nodes at a specific vertical and horizontal level also takes O(log2N) complexity.
Map operations involve insertion and retrieval of nodes with their vertical and level as their keys. Since there are two nested maps, the total time complexity becomes O(log2N)*O(log2N).
Space Complexity: O(N + N/2) where N represents the number of nodes in the Binary Tree.

The map for storing nodes based on their vertical and level information occupies an additional space complexity of O(N) as it stores all N nodes of the Binary Tree.
The queue for breadth first traversal occupies a space proportional to the maximum level of the tree which can be O(N/2) in the worst case of a balanced tree.
                            
from collections import deque, defaultdict

# Node structure for the binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    # Function to perform vertical order traversal
    # and return a 2D list of node values
    def findVertical(self, root):
        # Map to store nodes based on
        # vertical and level information
        nodes = defaultdict(lambda: defaultdict(lambda: set()))

        # Queue for BFS traversal, each
        # element is a pair containing node
        # and its vertical and level information
        todo = deque([(root, (0, 0))])

        # BFS traversal
        while todo:
            # Retrieve the node and its vertical
            # and level information from
            # the front of the queue
            temp, (x, y) = todo.popleft()

            # Insert the node value into the
            # corresponding vertical and level
            # in the map
            nodes[x][y].add(temp.data)

            # Process left child
            if temp.left:
                todo.append((temp.left, (x - 1, y + 1)))

            # Process right child
            if temp.right:
                todo.append((temp.right, (x + 1, y + 1)))

        # Prepare the final result list
        # by combining values from the map
        ans = []
        for x, y_vals in nodes.items():
            col = []
            for y, values in y_vals.items():
                # Insert node values
                # into the column list
                col.extend(sorted(values))
            # Add the column list
            # to the final result
            ans.append(col)

        return ans

# Helper function to
# print the result
def printResult(result):
    for level in result:
        for node in level:
            print(node, end=" ")
        print()
    print()

if __name__ == "__main__":
    # Creating a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(10)
    root.left.left.right = Node(5)
    root.left.left.right.right = Node(6)
    root.right = Node(3)
    root.right.right = Node(10)
    root.right.left = Node(9)

    solution = Solution()

    # Get the Vertical traversal
    verticalTraversal = solution.findVertical(root)

    # Print the result
    print("Vertical Traversal: ")
    printResult(verticalTraversal)
                           
                            


# 9 TODO : top view binary tree
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(N) where N is the number of nodes in the Binary Tree. This complexity arises from visiting each node exactly once during the BFS traversal.

Space Complexity: O(N/2 + N/2) where N represents the number of nodes in the Binary Tree.

The main space consuming data structure is the queue used for BFS traversal. It acquires space proportional to the number of nodes in the level it is exploring hence in the worst case of a balanced binary tree, the queue will have at most N/2 nodes which is the maximum width.
Additionally, the map is used to store the top view nodes based on their vertical positions hence its complexity will also be proportional to the greatest width level. In the worst case, it may have N/2 entries as well.
                            
from collections import deque

# Node class for the binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    # Function to return the top view of the binary tree
    def topView(self, root):
        # Vector to store the result
        ans = []
        
        # Check if the tree is empty
        if not root:
            return ans
        
        # Map to store the top view nodes
        # based on their vertical positions
        mpp = {}
        
        # Queue for BFS traversal, each element
        # is a pair containing node 
        # and its vertical position
        q = deque([(root, 0)])
        
        # Push the root node with its vertical
        # position (0) into the queue
        while q:
            # Retrieve the node and its vertical
            # position from the front of the queue
            node, line = q.popleft()
            
            # If the vertical position is not already
            # in the map, add the node's data to the map
            if line not in mpp:
                mpp[line] = node.data
            
            # Process left child
            if node.left:
                # Push the left child with a decreased
                # vertical position into the queue
                q.append((node.left, line - 1))
            
            # Process right child
            if node.right:
                # Push the right child with an increased
                # vertical position into the queue
                q.append((node.right, line + 1))
        
        # Transfer values from the
        # map to the result vector
        for value in sorted(mpp.items()):
            ans.append(value[1])
        
        return ans

# Creating a sample binary tree
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(10)
root.left.left.right = Node(5)
root.left.left.right.right = Node(6)
root.right = Node(3)
root.right.right = Node(10)
root.right.left = Node(9)

solution = Solution()

# Get the top view traversal
topView = solution.topView(root)

# Print the result
print("Vertical Traversal:")
for node in topView:
    print(node, end=" ")
                           
                            


# 10 TODO :  bottom view binary tree
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(N) where N is the number of nodes in the Binary Tree. This complexity arises from visiting each node exactly once during the BFS traversal.

Space Complexity: O(N/2 + N/2) where N represents the number of nodes in the Binary Tree.

The main space consuming data structure is the queue used for BFS traversal. It acquires space proportional to the number of nodes in the level it is exploring hence in the worst case of a balanced binary tree, the queue will have at most N/2 nodes which is the maximum width.
Additionally, the map is used to store the top view nodes based on their vertical positions hence its complexity will also be proportional to the greatest width level. In the worst case, it may have N/2 entries as well.
                            
from queue import Queue
from collections import deque, defaultdict

# Node class to represent the binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def bottomView(self, root):
        """
        Function to return the
        bottom view of the binary tree
        """
        # Vector to store the result
        ans = []

        # Check if the tree is empty
        if root is None:
            return ans

        # Map to store the bottom view nodes
        # based on their vertical positions
        mpp = defaultdict(int)

        # Queue for BFS traversal, each
        # element is a pair containing node
        # and its vertical position
        q = Queue()

        # Push the root node with its vertical
        # position (0) into the queue
        q.put((root, 0))

        # BFS traversal
        while not q.empty():
            # Retrieve the node and its vertical
            # position from the front of the queue
            it = q.get()
            node, line = it[0], it[1]

            # Update the map with the node's data
            # for the current vertical position
            mpp[line] = node.data

            # Process left child
            if node.left:
                # Push the left child with a decreased
                # vertical position into the queue
                q.put((node.left, line - 1))

            # Process right child
            if node.right:
                # Push the right child with an increased
                # vertical position into the queue
                q.put((node.right, line + 1))

        # Transfer values from the
        # map to the result vector
        for key, value in sorted(mpp.items()):
            ans.append(value)

        return ans

# Creating a sample binary tree
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(10)
root.left.left.right = Node(5)
root.left.left.right.right = Node(6)
root.right = Node(3)
root.right.right = Node(10)
root.right.left = Node(9)

# Creating a Solution object
solution = Solution()

# Get the Bottom View traversal
bottomView = solution.bottomView(root)

# Print the result
print("Bottom View Traversal:")
for node in bottomView:
    print(node, end=" ")
                           
                           


# 11 TODO : right/left view of a binary tree
# method 1 : brute force approch
Time Complexity: O(N) where N is the number of nodes in the binary tree. Each node of the binary tree is enqueued and dequeued exactly once, hence all nodes need to be processed and visited. Processing each node takes constant time operations which contributes to the overall linear time complexity.

Space Complexity : O(N) where N is the number of nodes in the binary tree. In the worst case, the queue has to hold all the nodes of the last level of the binary tree, the last level could at most hold N/2 nodes hence the space complexity of the queue is proportional to O(N). The resultant vector answer also stores the values of the nodes level by level and hence contains all the nodes of the tree contributing to O(N) space as well.
                                
 # Node class for the binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Solution class to get the left
# and right view of the binary tree
class Solution:
    def rightsideView(self, root):
        # Vector to store the result
        res = []
        
        # Call the recursive function
        # to populate the right-side view
        self.recursionRight(root, 0, res)
        
        return res

    def leftsideView(self, root):
        # Vector to store the result
        res = []
        
        # Call the recursive function
        # to populate the left-side view
        self.recursionLeft(root, 0, res)
        
        return res

    # Recursive function to traverse the
    # binary tree and populate the left-side view
    def recursionLeft(self, root, level, res):
        # Check if the current node is None
        if not root:
            return
        
        # Check if the size of the result list
        # is equal to the current level
        if len(res) == level:
            # If equal, add the value of the
            # current node to the result list
            res.append(root.data)
        
        # Recursively call the function for the
        # left child with an increased level
        self.recursionLeft(root.left, level + 1, res)
        
        # Recursively call the function for the
        # right child with an increased level
        self.recursionLeft(root.right, level + 1, res)

    # Recursive function to traverse the
    # binary tree and populate the right-side view
    def recursionRight(self, root, level, res):
        # Check if the current node is None
        if not root:
            return
        
        # Check if the size of the result list
        # is equal to the current level
        if len(res) == level:
            # If equal, add the value of the
            # current node to the result list
            res.append(root.data)
            
            # Recursively call the function for the
            # right child with an increased level
            self.recursionRight(root.right, level + 1, res)
            
            # Recursively call the function for the
            # left child with an increased level
            self.recursionRight(root.left, level + 1, res)

# Creating a sample binary tree
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(10)
root.left.left.right = Node(5)
root.left.left.right.right = Node(6)
root.right = Node(3)
root.right.right = Node(10)
root.right.left = Node(9)

solution = Solution()

# Get the Right View traversal
rightView = solution.rightsideView(root)

# Print the result for Right View
print("Right View Traversal:", end=" ")
for node in rightView:
    print(node, end=" ")
print()

# Get the Left View traversal
leftView = solution.leftsideView(root)

# Print the result for Left View
print("Left View Traversal:", end=" ")
for node in leftView:
    print(node, end=" ")
print()
                                
                            


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(log2N) where N is the number of nodes in the Binary Tree. This complexity arises as we travel along the height of the Binary Tree. For a balanced binary tree, the height is log2N but in the worst case when the tree is skewed, the complexity becomes O(N).

Space Complexity : O(log2N) where N is the number of nodes in the Binary Tree. This complexity arises because we store the leftmost and rightmost nodes in an additional vector. The size of this result vector is proportional to the height of the Binary Tree which will be log2N when the tree is balanced and O(N) in the worst case of a skewed tree.

O(H): Recursive Stack Space is used to calculate the height of the tree at each node which is proportional to the height of the tree.
The recursive nature of the getHeight function, which incurs space on the call stack for each recursive call until it reaches the leaf nodes or the height of the tree.
                                
                     
# Node class for the binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Solution class to get the left
# and right view of the binary tree
class Solution:
    def rightsideView(self, root):
        # Vector to store the result
        res = []
        
        # Call the recursive function
        # to populate the right-side view
        self.recursionRight(root, 0, res)
        
        return res

    def leftsideView(self, root):
        # Vector to store the result
        res = []
        
        # Call the recursive function
        # to populate the left-side view
        self.recursionLeft(root, 0, res)
        
        return res

    # Recursive function to traverse the
    # binary tree and populate the left-side view
    def recursionLeft(self, root, level, res):
        # Check if the current node is None
        if not root:
            return
        
        # Check if the size of the result list
        # is equal to the current level
        if len(res) == level:
            # If equal, add the value of the
            # current node to the result list
            res.append(root.data)
        
        # Recursively call the function for the
        # left child with an increased level
        self.recursionLeft(root.left, level + 1, res)
        
        # Recursively call the function for the
        # right child with an increased level
        self.recursionLeft(root.right, level + 1, res)

    # Recursive function to traverse the
    # binary tree and populate the right-side view
    def recursionRight(self, root, level, res):
        # Check if the current node is None
        if not root:
            return
        
        # Check if the size of the result list
        # is equal to the current level
        if len(res) == level:
            # If equal, add the value of the
            # current node to the result list
            res.append(root.data)
            
            # Recursively call the function for the
            # right child with an increased level
            self.recursionRight(root.right, level + 1, res)
            
            # Recursively call the function for the
            # left child with an increased level
            self.recursionRight(root.left, level + 1, res)

# Creating a sample binary tree
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(10)
root.left.left.right = Node(5)
root.left.left.right.right = Node(6)
root.right = Node(3)
root.right.right = Node(10)
root.right.left = Node(9)

solution = Solution()

# Get the Right View traversal
rightView = solution.rightsideView(root)

# Print the result for Right View
print("Right View Traversal:", end=" ")
for node in rightView:
    print(node, end=" ")
print()

# Get the Left View traversal
leftView = solution.leftsideView(root)

# Print the result for Left View
print("Left View Traversal:", end=" ")
for node in leftView:
    print(node, end=" ")
print()
                                
                            


# 12 TODO : symmetric binary tree
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(N) where N is the number of nodes in the Binary Tree. This complexity arises from visiting each node exactly once during the traversal and the function compares the nodes in a symmetric manner.

Space Complexity: O(1) as no additional data structures or memory is allocated.

O(H): Recursive Stack Space is used to calculate the height of the tree at each node which is proportional to the height of the tree.
The recursive nature of the getHeight function, which incurs space on the call stack for each recursive call until it reaches the leaf nodes or the height of the tree.

                            
# Node class for the binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Solution class to find the
# maximum depth of a binary tree
class Solution:
    # Function to find the
    # maximum depth of a binary tree
    def maxDepth(self, root):
        # If the root is None
        # (empty tree), depth is 0
        if root is None:
            return 0
        
        # Recursive call to find the
        # maximum depth of the left subtree
        lh = self.maxDepth(root.left)
        
        # Recursive call to find the
        # maximum depth of the right subtree
        rh = self.maxDepth(root.right)
        
        # Return the maximum depth of the
        # tree, adding 1 for the current node
        return 1 + max(lh, rh)

# Main function
if __name__ == "__main__":
    # Creating a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.right = Node(6)
    root.left.right.right.right = Node(7)
    
    solution = Solution()
    depth = solution.maxDepth(root)
    
    print("Maximum depth of the binary tree:", depth)
                           
                        


# endregion



# region 13.3 BINARY TREES - HARD
# --------------------------------


# 1 TODO : root to node in a binary tree  
# method 1 : brute force approch
Time Complexity: O(N) where N is the number of nodes in the binary tree as each node of the binary tree is visited exactly once in the inorder traversal.

Space Complexity: O(N) awhere N is the number of nodes in the binary tree. This is because the stack can potentially hold all nodes in the tree when dealing with a skewed tree (all nodes have only one child), consuming space proportional to the number of nodes.

O(H): In the average case or for a balanced tree, the maximum number of nodes that could be in the stack at any given time would be roughly the height of the tree hence O(log2N).
                            
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getPath(self, root, arr, x):
        """
        Function to find the path from the
        root to a given node with value 'x'
        """
        # Base case: If the current
        # node is None, return False
        if not root:
            return False

        # Add the current node's
        # value to the path list
        arr.append(root.val)

        # If the current node's value is equal
        # to the target value 'x', return True
        if root.val == x:
            return True

        # Recursively search for the target value
        # 'x' in the left and right subtrees
        if self.getPath(root.left, arr, x) or self.getPath(root.right, arr, x):
            return True

        # If the target value 'x' is not found
        # in the current path, backtrack
        arr.pop()
        return False

    def solve(self, A, B):
        """
        Function to find and return the path from
        the root to a given node with value 'B'
        """
        # Initialize an empty
        # list to store the path
        arr = []

        # If the root node is None,
        # return the empty path list
        if not A:
            return arr

        # Call the getPath function to find
        # the path to the node with value 'B'
        self.getPath(A, arr, B)

        # Return the path list
        return arr

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    sol = Solution()

    target_leaf_value = 7

    path = sol.solve(root, target_leaf_value)

    print(f"Path from root to leaf with value {target_leaf_value}: ", end="")
    for i in range(len(path)):
        print(path[i], end="")
        if i < len(path) - 1:
            print(" -> ", end="")
                           
                        


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 2 TODO : LCA in binary tree
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 3 TODO : maximum width of a binary tree
# method 1 : brute force approch
Time Complexity: O(N) where N is the number of nodes in the binary tree. Each node of the binary tree is enqueued and dequeued exactly once, hence all nodes need to be processed and visited. Processing each node takes constant time operations which contributes to the overall linear time complexity.

Space Complexity: O(N) where N is the number of nodes in the binary tree. In the worst case, the queue has to hold all the nodes of the last level of the binary tree, the last level could at most hold N/2 nodes hence the space complexity of the queue is proportional to O(N).
                            
from queue import Queue
from typing import Optional, Tuple


# TreeNode structure
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # If the root is null,
        # the width is zero
        if not root:
            return 0

        # Initialize a variable 'ans'
        # to store the maximum width
        ans = 0

        # Create a queue to perform level-order
        # traversal, where each element is a tuple
        # of TreeNode and its position in the level
        q = Queue()
        # Push the root node and its
        # position (0) into the queue
        q.put((root, 0))

        # Perform level-order traversal
        while not q.empty():
            # Get the number of
            # nodes at the current level
            size = q.qsize()
            # Get the position of the front
            # node in the current level
            mmin = q.queue[0][1]

            # Store the first and last positions
            # of nodes in the current level
            first, last = None, None

            # Process each node
            # in the current level
            for i in range(size):
                # Calculate current position relative
                # to the minimum position in the level
                cur_id = q.queue[i][1] - mmin
                # Get the current node
                node = q.queue[i][0]

                # If this is the first node in the level,
                # update the 'first' variable
                if i == 0:
                    first = cur_id

                # If this is the last node in the level,
                # update the 'last' variable
                if i == size - 1:
                    last = cur_id

                # Enqueue the left child of the
                # current node with its position
                if node.left:
                    q.put((node.left, cur_id * 2 + 1))

                # Enqueue the right child of the
                # current node with its position
                if node.right:
                    q.put((node.right, cur_id * 2 + 2))

            # Update the maximum width by calculating
            # the difference between the first and last
            # positions, and adding 1
            ans = max(ans, last - first + 1)

        # Return the maximum
        # width of the binary tree
        return ans


def main():
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    sol = Solution()

    maxWidth = sol.widthOfBinaryTree(root)

    print(f"Maximum width of the binary tree is: {maxWidth}")


if __name__ == "__main__":
    main()
                           
                          


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 4 TODO : check for children sum property
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(N) where N is the number of nodes in the binary tree. This is because the algorithm traverses each node exactly once, performing constant-time operations at each node.

Space Complexity: O(N) where N is the number of nodes in the Binary Tree.

In the worst case scenario the tree is skewed and the auxiliary recursion stack space would be stacked up to the maximum height of the tree, resulting in a space complexity of O(N).
In the optimal case of a balanced tree, the auxiliary space would take up space proportional to O(log2N).

                            
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def changeTree(self, root):
        # Base case: If the current node
        # is None, return and do nothing.
        if root is None:
            return

        # Calculate the sum of the values of
        # the left and right children, if they exist.
        child = 0
        if root.left:
            child += root.left.val
        if root.right:
            child += root.right.val

        # Compare the sum of children with
        # the current node's value and update
        if child >= root.val:
            root.val = child
        else:
            # If the sum is smaller, update the
            # child with the current node's value.
            if root.left:
                root.left.val = root.val
            elif root.right:
                root.right.val = root.val

        # Recursively call the function
        # on the left and right children.
        self.changeTree(root.left)
        self.changeTree(root.right)

        # Calculate the total sum of the
        # values of the left and right
        # children, if they exist.
        tot = 0
        if root.left:
            tot += root.left.val
        if root.right:
            tot += root.right.val

        # If either left or right child
        # exists, update the current node's
        # value with the total sum.
        if root.left or root.right:
            root.val = tot


# Function to print the inorder
# traversal of the tree
def inorderTraversal(root):
    if root is None:
        return
    inorderTraversal(root.left)
    print(root.val, end=" ")
    inorderTraversal(root.right)


# Create the binary tree
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

sol = Solution()

# Print the inorder traversal
# of tree before modification
print("Binary Tree before modification:", end=" ")
inorderTraversal(root)
print()

# Call the changeTree function
# to modify the binary tree
sol.changeTree(root)

# Print the inorder traversal
# after modification
print("Binary Tree after Children Sum Property:", end=" ")
inorderTraversal(root)
print()
                           
                        


# 5 TODO : print all the nodes at a distance of k in binary tree
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 6 TODO : minimum time taken to BURN the binary tree from a node
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 7 TODO : count total nodes in a complete binary tree
# method 1 : brute force approch
Time Complexity: O(N) where N is the number of nodes in the binary tree as each node of the binary tree is visited exactly once.

Space Complexity : O(N) where N is the number of nodes in the binary tree. This is because the recursive stack uses an auxiliary space which can potentially hold all nodes in the tree when dealing with a skewed tree (all nodes have only one child), consuming space proportional to the number of nodes. In the average case or for a balanced tree, the maximum number of nodes that could be in the stack at any given time would be roughly the height of the tree hence O(log2N).
                                
# TreeNode class definition
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorder(self, root, count):
        """
        Function to perform inorder traversal and count nodes
        """
        # Base case: If the current node is None, return
        if root is None:
            return

        # Increment count for the current node
        count[0] += 1

        # Recursively call inorder on the left subtree
        self.inorder(root.left, count)

        # Recursively call inorder on the right subtree
        self.inorder(root.right, count)

    def countNodes(self, root):
        """
        Function to count nodes in the binary tree
        """
        # Base case: If the root is None, the tree is empty, return 0
        if root is None:
            return 0

        # Initialize count variable to store the number of nodes
        count = [0]

        # Call the inorder traversal function to count nodes
        self.inorder(root, count)

        # Return the final count of nodes in the binary tree
        return count[0]


# Main function
if __name__ == "__main__":
    # Create the binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)

    sol = Solution()

    # Call the countNodes function
    totalNodes = sol.countNodes(root)

    # Print the result
    print("Total number of nodes in the Complete Binary Tree:", totalNodes)
                                
                               


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(log N * log N) where N is the number of nodes in the Binary Tree.

The calculation of leftHeight and rightHeight takes O(log N) time.
In the worst case, when encountering the second case (leftHeight != rightHeight), the recursive calls are made at most log N times (the height of the tree).
Therefore, the total time complexity is O(log N * log N).
Space Complexity : O(H) ~ O(N) where N is the number of nodes in the Binary Tree.

The space complexity is determined by the maximum depth of the recursion stack, which is equal to the height of the binary tree.
Since the given tree is a complete binary tree, the height will always be log N.
Therefore, the space complexity is O(log N).

                                
                     
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root):
        """
        Count the total number of nodes in the Complete Binary Tree.

        :param root: TreeNode, the root of the binary tree
        :return: int, total number of nodes in the binary tree
        """
        if not root:
            return 0

        lh = self.findHeightLeft(root)
        rh = self.findHeightRight(root)

        if lh == rh:
            return (1 << lh) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def findHeightLeft(self, node):
        """
        Find the height of the left subtree.

        :param node: TreeNode, the root of the subtree
        :return: int, height of the left subtree
        """
        hght = 0
        while node:
            hght += 1
            node = node.left
        return hght

    def findHeightRight(self, node):
        """
        Find the height of the right subtree.

        :param node: TreeNode, the root of the subtree
        :return: int, height of the right subtree
        """
        hght = 0
        while node:
            hght += 1
            node = node.right
        return hght


if __name__ == "__main__":
    # Create the binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)

    sol = Solution()

    # Call the countNodes function
    totalNodes = sol.countNodes(root)

    # Print the result
    print(f"Total number of nodes in the Complete Binary Tree: {totalNodes}")
                                
                            


# 8 TODO : requirements needed to construct a unique binary tree (theory)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 9 TODO : construct binary tree from inorder and preorder traversal
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(N) where N is the number of nodes in the Binary Tree. This is because each node of the Binary Tree is visited once.

Space Complexity: O(N) where N is the number of nodes in the Binary Tree. The inorder hashmap to store the inorder array for fast lookup takes up space proportional to the input nodes. An auxiliary stack space ~ O(H) where H is the height of the Binary Tree is used. This is the stack space used to build the tree recursively. In the case of a skewed tree, the height of the tree will be H ~ N hence the worst case auxiliary space is O(N).
                            
from typing import List

# TreeNode class definition
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # Create a map to store indices of elements in the inorder traversal
        inMap = {val: idx for idx, val in enumerate(inorder)}
        
        # Call the private helper function to recursively build the tree
        root = self._buildTree(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1, inMap)
        
        return root

    def _buildTree(self, preorder, preStart, preEnd, inorder, inStart, inEnd, inMap):
        # Base case: If the start indices exceed the end indices, return None
        if preStart > preEnd or inStart > inEnd:
            return None

        # Create a new TreeNode with value at the current preorder index
        root = TreeNode(preorder[preStart])

        # Find the index of the current root value in the inorder traversal
        inRoot = inMap[root.val]

        # Calculate the number of elements in the left subtree
        numsLeft = inRoot - inStart

        # Recursively build the left subtree
        root.left = self._buildTree(preorder, preStart + 1, preStart + numsLeft,
                                    inorder, inStart, inRoot - 1, inMap)

        # Recursively build the right subtree
        root.right = self._buildTree(preorder, preStart + numsLeft + 1, preEnd,
                                     inorder, inRoot + 1, inEnd, inMap)

        # Return the current root node
        return root

# Function to print the inorder traversal of a tree
def printInorder(root):
    if not root:
        return
    printInorder(root.left)
    print(root.val, end=" ")
    printInorder(root.right)

# Function to print the given list
def printList(lst):
    for val in lst:
        print(val, end=" ")
    print()

# Main function
if __name__ == "__main__":
    inorder = [9, 3, 15, 20, 7]
    preorder = [3, 9, 20, 15, 7]
    
    print("Inorder List: ", end="")
    printList(inorder)
    
    print("Preorder List: ", end="")
    printList(preorder)
    
    sol = Solution()

    root = sol.buildTree(preorder, inorder)
    
    print("Inorder of Unique Binary Tree Created:")
    printInorder(root)
    print()
                           
                           


# 10 TODO :  construct binary tree from postorder and inorder traversal
# method 1 : brute force approch
Time Complexity: O(N) where N is the number of nodes in the Binary Tree. This is because each node is processed and visited exactly once.

The algorithm processes each element in the inorder traversal and for each element it performs constant-time operations (lookup in the hashmap, recursive calls and variable operations).
Space Complexity: O(N + log2N) where N is the number of elements in the iwhere N is the number of nodes in the Binary Tree.

This complexity arises from the space used by the recursion stack during the recursive calls. In the worst case, the maximum depth of the recursion stack would be equal to the height of the Binary Tree and in the optimal case the recursion stack complexity would be O(log2N).

                            
from typing import List

# TreeNode class definition
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """
        Function to build a binary tree
        from inorder and postorder traversals
        """
        if len(inorder) != len(postorder):
            return None

        # Create a map to store the indices
        # of elements in the inorder traversal
        hm = {val: i for i, val in enumerate(inorder)}

        # Call the recursive function
        # to build the binary tree
        return self.buildTreePostIn(inorder, 0, len(inorder) - 1, postorder, 0,
                                     len(postorder) - 1, hm)

    def buildTreePostIn(self, inorder: List[int], is_, ie, postorder: List[int], ps, pe, hm):
        """
        Recursive function to build a binary
        tree from inorder and postorder traversals
        """
        # Base case: If the subtree
        # is empty, return None
        if ps > pe or is_ > ie:
            return None

        # Create a new TreeNode
        # with the root value from postorder
        root = TreeNode(postorder[pe])

        # Find the index of the root
        # value in inorder traversal
        inRoot = hm[postorder[pe]]

        # Number of nodes in the left subtree
        numsLeft = inRoot - is_

        # Recursively build the
        # left and right subtrees
        root.left = self.buildTreePostIn(inorder, is_, inRoot - 1, postorder,
                                         ps, ps + numsLeft - 1, hm)

        root.right = self.buildTreePostIn(inorder, inRoot + 1, ie, postorder,
                                          ps + numsLeft, pe - 1, hm)

        # Return the root of
        # the constructed subtree
        return root

# Function to print the
# inorder traversal of a tree
def printInorder(root):
    if not root:
        return
    printInorder(root.left)
    print(root.val, end=" ")
    printInorder(root.right)

# Function to print the given list
def printList(lst):
    for item in lst:
        print(item, end=" ")
    print()

# Example input lists
inorder = [40, 20, 50, 10, 60, 30]
postorder = [40, 50, 20, 60, 30, 10]

# Display the input lists
print("Inorder List: ", end="")
printList(inorder)

print("Postorder List: ", end="")
printList(postorder)

sol = Solution()

# Build the binary tree and
# print its inorder traversal
root = sol.buildTree(inorder, postorder)

print("Inorder of Unique Binary Tree Created:")
printInorder(root)
print()

                           
                        


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 11 TODO : serialize and deserialize binary tree
Time Complexity: O(N)

serialize function: O(N), where N is the number of nodes in the tree. This is because the function performs a level-order traversal of the tree, visiting each node once.
deserialize function: O(N), where N is the number of nodes in the tree. Similar to the serialize function, it processes each node once while reconstructing the tree.
Space Complexity: O(N)

serialize function: O(N), where N is the maximum number of nodes at any level in the tree. In the worst case, the queue can hold all nodes at the last level of the tree.
deserialize function: O(N), where N is the maximum number of nodes at any level in the tree. The queue is used to store nodes during the reconstruction process, and in the worst case, it may hold all nodes at the last level.
                            
from queue import Queue
from typing import Optional

# Definition for a
# binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def serialize(self, root: Optional[TreeNode]) -> str:
        # Check if the tree is empty
        if not root:
            return ""

        # Initialize an empty string
        # to store the serialized data
        s = ""
        # Use a queue for
        # level-order traversal
        q = Queue()
        # Start with the root node
        q.put(root)

        # Perform level-order traversal
        while not q.empty():
            # Get the front node in the queue
            cur_node = q.get()

            # Check if the current node is
            # null and append "#" to the string
            if not cur_node:
                s += "#,"
            else:
                # Append the value of the
                # current node to the string
                s += str(cur_node.val) + ","
                # Push the left and right children
                # to the queue for further traversal
                q.put(cur_node.left)
                q.put(cur_node.right)

        # Return the
        # serialized string
        return s

    def deserialize(self, data: str) -> Optional[TreeNode]:
        # Check if the
        # serialized data is empty
        if not data:
            return None

        # Use a queue for
        # level-order traversal
        q = Queue()
        # Use a list to store tokens
        tokens = data.split(',')
        # Read the root value
        # from the serialized data
        root_val = int(tokens.pop(0))
        root = TreeNode(root_val)
        q.put(root)

        # Perform level-order traversal
        # to reconstruct the tree
        while not q.empty():
            # Get the front node in the queue
            node = q.get()

            # Read the value of the left
            # child from the serialized data
            left_val = tokens.pop(0)
            # If the value is not "#", create a new
            # left child and push it to the queue
            if left_val != "#":
                left_node = TreeNode(int(left_val))
                node.left = left_node
                q.put(left_node)

            # Read the value of the right child
            # from the serialized data
            right_val = tokens.pop(0)
            # If the value is not "#", create a
            # new right child and push it to the queue
            if right_val != "#":
                right_node = TreeNode(int(right_val))
                node.right = right_node
                q.put(right_node)

        # Return the reconstructed
        # root of the tree
        return root

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    solution = Solution()
    print("Original Tree: ", end="")
    inorder(root)
    print()

    serialized = solution.serialize(root)
    print("Serialized: " + serialized)

    deserialized = solution.deserialize(serialized)
    print("Tree after deserialization: ", end="")
    inorder(deserialized)
    print()
                           
                        

# 12 TODO : morris preorder traversal of a binary tree
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(2N) where N is the number of nodes in the Binary Tree.

The time complexity is linear, as each node is visited at most twice (once for establishing the temporary link and once for reverting it).
In each step, we perform constant-time operations, such as moving to the left or right child and updating pointers.
Space Complexity: O(1) The space complexity is constant, as the algorithm uses only a constant amount of extra space irrespective of the input size.

Morris Traversal does not use any additional data structures like stacks or recursion, making it an in-place algorithm.
The only space utilised is for a few auxiliary variables, such as pointers to current and in-order predecessor nodes.
                            
# TreeNode class definition
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getPreorder(self, root):
        # List to store the preorder traversal result
        preorder = []

        # Pointer to the current node, starting with the root
        cur = root

        # Iterate until the current node becomes None
        while cur is not None:
            # If the current node has no left child
            if cur.left is None:
                # Add the value of the current node to the preorder list
                preorder.append(cur.val)

                # Move to the right child
                cur = cur.right
            else:
                # If the current node has a left child
                # Create a pointer to traverse to the rightmost node in the left subtree
                prev = cur.left

                # Traverse to the rightmost node in the left subtree
                # or until we find a node whose right child is not yet processed
                while prev.right and prev.right != cur:
                    prev = prev.right

                # If the right child of the rightmost node is None
                if prev.right is None:
                    # Set the right child of the rightmost node to the current node
                    prev.right = cur

                    # Move to the left child
                    cur = cur.left
                else:
                    # If the right child of the rightmost node is not None
                    # Reset the right child to None
                    prev.right = None

                    # Add the value of the current node to the preorder list
                    preorder.append(cur.val)

                    # Move to the right child
                    cur = cur.right

        # Return the resulting preorder traversal list
        return preorder


# Main function
if __name__ == "__main__":
    # Construct the binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.right = TreeNode(6)

    # Create an instance of the Solution class
    sol = Solution()

    # Perform Morris Preorder Traversal
    preorder = sol.getPreorder(root)

    # Print the result
    print("Binary Tree Morris Preorder Traversal:", end=" ")
    for val in preorder:
        print(val, end=" ")
    print()
                           
                             


# 13 TODO : morris inorder traversal of a binary tree
# method 1 : brute force approch
Time Complexity: O(2N) where N is the number of nodes in the Binary Tree.

The time complexity is linear, as each node is visited at most twice (once for establishing the temporary link and once for reverting it).
In each step, we perform constant-time operations, such as moving to the left or right child and updating pointers.
Space Complexity: O(1) The space complexity is constant, as the algorithm uses only a constant amount of extra space irrespective of the input size.

Morris Traversal does not use any additional data structures like stacks or recursion, making it an in-place algorithm.
The only space utilised is for a few auxiliary variables, such as pointers to current and in-order predecessor nodes.
                            
# TreeNode structure
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getInorder(self, root):
        # Vector to store the
        # inorder traversal result
        inorder = []
        # Pointer to the current node,
        # starting from the root
        cur = root

        # Loop until the current
        # node is not None
        while cur is not None:
            # If the current node's
            # left child is None
            if cur.left is None:
                # Add the value of the current
                # node to the inorder list
                inorder.append(cur.val)
                # Move to the right child
                cur = cur.right
            else:
                # If the left child is not None,
                # find the predecessor (rightmost node
                # in the left subtree)
                prev = cur.left
                while prev.right and prev.right != cur:
                    prev = prev.right

                # If the predecessor's right child
                # is None, establish a temporary link
                # and move to the left child
                if prev.right is None:
                    prev.right = cur
                    cur = cur.left
                else:
                    # If the predecessor's right child
                    # is already linked, remove the link,
                    # add the current node to inorder list,
                    # and move to the right child
                    prev.right = None
                    inorder.append(cur.val)
                    cur = cur.right

        # Return the inorder
        # traversal result
        return inorder


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.right = TreeNode(6)

    sol = Solution()

    inorder = sol.getInorder(root)

    print("Binary Tree Morris Inorder Traversal:", end=" ")
    for val in inorder:
        print(val, end=" ")
    print()
                           
                          


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 14 TODO : flatten  binary tree to linked list
# method 1 : brute force approch
Time Complexity: O(N) where N is the number of nodes in the Binary Tree. Each node of the binary node is visited exactly once. At each node, constant-time operations are performed. Hence the time complexity is O(N).

Space Complexity : O(log2N)where N is the number of nodes in the Binary Tree. There are no additional data structures or space used but the auxiliary stack space is used during recursion. Since the recursion depth can be at most equal to the height to the Binary Tree, the space complexity is O(H) where H is the height of the Binary Tree. In the ideal case, H = log2N and in the worst case H = N (skewed tree).
                                
# TreeNode structure
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        # Initialize a global variable
        # 'prev' to keep track of the
        # previously processed node.
        self.prev = None

    # Function to flatten a binary tree
    # to a right next Linked List structure
    def flatten(self, root):
        # Base case: If the current
        # node is None, return.
        if root is None:
            return

        # Recursive call to
        # flatten the right subtree
        self.flatten(root.right)

        # Recursive call to
        # flatten the left subtree
        self.flatten(root.left)

        # At this point, both left and right
        # subtrees are flattened, and 'prev'
        # is pointing to the rightmost node
        # in the flattened right subtree.

        # Set the right child of
        # the current node to 'prev'.
        root.right = self.prev

        # Set the left child of the
        # current node to None.
        root.left = None

        # Update 'prev' to the current
        # node for the next iteration.
        self.prev = root

# Print the preorder traversal of the
# Original Binary Tree
def print_preorder(root):
    if not root:
        return
    print(root.val, end=" ")
    print_preorder(root.left)
    print_preorder(root.right)

# Print the Binary Tree along the
# Right Pointers after Flattening
def print_flatten_tree(root):
    if not root:
        return
    print(root.val, end=" ")
    print_flatten_tree(root.right)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.right = TreeNode(6)
    root.right.right = TreeNode(7)
    root.right.left = TreeNode(8)

    sol = Solution()

    print("Binary Tree Preorder: ", end="")
    print_preorder(root)
    print()

    sol.flatten(root)

    print("Binary Tree After Flatten: ", end="")
    print_flatten_tree(root)
    print()
    
                                
                              


# method 2 : better approch
Time Complexity: O(N) where N is the number of nodes in the Binary Tree. Each node of the binary node is visited exactly once. At each node, constant-time operations are performed. Hence the time complexity is O(N).

Space Complexity : O(log2N) where N is the number of nodes in the Binary Tree. There are no additional data structures or space used but the auxiliary stack space is used during recursion. Since the recursion depth can be at most equal to the height to the Binary Tree, the space complexity is O(H) where H is the height of the Binary Tree. In the ideal case, H = log2N and in the worst case H = N (skewed tree).
                                
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        # Initialize a global variable
        # 'prev' to keep track of the
        # previously processed node.
        self.prev = None

    # Function to flatten a binary tree
    # to a right next Linked List structure
    def flatten(self, root):
        # Base case: If the current
        # node is None, return.
        if not root:
            return
        
        # Use a stack for
        # iterative traversal.
        stack = [root]

        # Continue the loop until
        # the stack is empty.
        while stack:
            # Get the top node from the stack.
            cur = stack.pop()

            if cur.right:
                # Push the right child
                # onto the stack.
                stack.append(cur.right)

            if cur.left:
                # Push the left child
                # onto the stack.
                stack.append(cur.left)

            if stack:
                # Connect the right child to
                # the next node in the stack.
                cur.right = stack[-1]

            # Set the left child to None to
            # form a right-oriented linked list.
            cur.left = None

# Print the preorder traversal of the
# Original Binary Tree
def print_preorder(root):
    if not root:
        return
    print(root.val, end=" ")
    print_preorder(root.left)
    print_preorder(root.right)

# Print the Binary Tree along the 
# Right Pointers after Flattening
def print_flatten_tree(root):
    if not root:
        return
    print(root.val, end=" ")
    print_flatten_tree(root.right)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.right = TreeNode(6)
    root.right.right = TreeNode(7)
    root.right.left = TreeNode(8)

    sol = Solution()

    print("Binary Tree Preorder: ", end="")
    print_preorder(root)
    print()

    sol.flatten(root)

    print("Binary Tree After Flatten: ", end="")
    print_flatten_tree(root)
    print()
                                
                             


# method 3 : optimal solution
Time Complexity: O(2N) where N is the number of nodes in the Binary Tree.

The time complexity is linear, as each node is visited at most twice (once for establishing the temporary link and once for reverting it).
In each step, we perform constant-time operations, such as moving to the left or right child and updating pointers.
Space Complexity: O(1) The space complexity is constant, as the algorithm uses only a constant amount of extra space irrespective of the input size.

Morris Traversal does not use any additional data structures like stacks or recursion, making it an in-place algorithm.
The only space utilised is for a few auxiliary variables, such as pointers to current and in-order predecessor nodes.

                                
# TreeNode structure
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Function to flatten a binary tree
    # to a right next Linked List structure
    def flatten(self, root):
        # Initialize a pointer
        # 'curr' to the root of the tree
        curr = root

        # Iterate until 'curr'
        # becomes None
        while curr:
            # Check if the current
            # node has a left child
            if curr.left:
                # If yes, find the rightmost
                # node in the left subtree
                pre = curr.left
                while pre.right:
                    pre = pre.right

                # Connect the rightmost node in
                # the left subtree to the current
                # node's right child
                pre.right = curr.right

                # Move the entire left subtree to the
                # right child of the current node
                curr.right = curr.left

                # Set the left child of
                # the current node to None
                curr.left = None

            # Move to the next node
            # on the right side
            curr = curr.right

# Print the preorder traversal of the
# Original Binary Tree
def print_preorder(root):
    if not root:
        return
    print(root.val, end=" ")
    print_preorder(root.left)
    print_preorder(root.right)

# Print the Binary Tree along the
# Right Pointers after Flattening
def print_flatten_tree(root):
    if not root:
        return
    print(root.val, end=" ")
    print_flatten_tree(root.right)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.right = TreeNode(6)
    root.right.right = TreeNode(7)
    root.right.left = TreeNode(8)

    sol = Solution()

    print("Binary Tree Preorder: ", end="")
    print_preorder(root)
    print()

    sol.flatten(root)

    print("Binary Tree After Flatten: ", end="")
    print_flatten_tree(root)
    print()


                                
                            



# endregion



# region 14.1 BINARY SEARCH TREES - CONCEPTS
# ------------------------------------------

# 1 TODO :  introduction to binary search tree
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 2 TODO : search in a binary search tree
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(log2N) where N is the number of nodes in the Binary Search Tree. In the best case scenario, where the tree is balanced, the time complexity is the height of the tree ie. log2N. In the worst-case scenario, where the tree is degenerate (linear), the time complexity becomes O(n), as it would require traversing all nodes along the path from the root to the leaf.

Space Complexity: O(1) since the algorithm does not use any additional space or data structures. The algorithm does use auxiliary stack space from recursion. In the average and worst-case scenarios, the space complexity for recursive stack space is O(h), where 'h' represents the height of the tree.
                            
# Definition of TreeNode structure
# for a binary tree node
class TreeNode:
    # Constructor to initialize the node with a
    # value and set left and right pointers to None
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # This function searches for a node with
    # a specified value in a Binary Search Tree (BST).
    def searchBST(self, root, val):
        # Loop until either the tree is
        # exhausted (None) or the value is found.
        while root is not None and root.val != val:
            # Check if the target value is
            # less than the current node's value.
            # If so, move to the left subtree
            # (values smaller than the current node).
            # Otherwise, move to the right subtree
            # (values larger than the current node).
            root = root.left if val < root.val else root.right
        # Return the node containing the target value,
        # if found; otherwise, return None.
        return root

# Function to perform an in-order traversal
# of a binary tree and print its nodes
def printInOrder(root):
    # Check if the current node
    # is None (base case for recursion)
    if root is None:
        # If None, return and
        # terminate the function
        return

    # Recursively call printInOrder
    # for the left subtree
    printInOrder(root.left)

    # Print the value of the current node
    print(root.val, end=" ")

    # Recursively call printInOrder
    # for the right subtree
    printInOrder(root.right)

# Creating a BST
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(10)

print("Binary Search Tree:")
printInOrder(root)
print()

solution = Solution()

# Searching for a value in the BST
target = 6
result = solution.searchBST(root, target)

# Displaying the search result
if result is not None:
    print(f"Value {target} found in the BST!")
else:
    print(f"Value {target} not found in the BST.")
                           




# 3 TODO : find min/max in BST
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      



# endregion




# region 14.2 BINARY SEARCH TREES - PRACTICE PROBLEMS
# ---------------------------------------------------

# 1 TODO :  ceil in a BST
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(log2N) where N is the number of nodes in the Binary Search Tree. In the best case scenario, where the tree is balanced, the time complexity is the height of the tree ie. log2N. In the worst-case scenario, where the tree is degenerate (linear), the time complexity becomes O(n), as it would require traversing all nodes along the path from the root to the leaf.

Space Complexity: O(1) since the algorithm does not use any additional space or data structures.
                            
# Definition of TreeNode structure
# for a binary tree node
class TreeNode:
    # Constructor to initialize the node with a
    # value and set left and right pointers to null
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Function to find the ceiling of
    # a key in a Binary Search Tree (BST)
    def findCeil(self, root, key):
        # Initialize the variable
        # to store the ceiling value
        ceil = -1
        
        # Traverse the BST until reaching
        # the end or finding the key
        while root:
            # If the key is found, assign it
            # as the ceiling and return
            if root.val == key:
                ceil = root.val
                return ceil
            
            # If the key is greater,
            # move to the right subtree
            if key > root.val:
                root = root.right
            else:
                # If the key is smaller, update ceil
                # and move to the left subtree
                ceil = root.val
                root = root.left
        
        # Return the computed ceiling value
        return ceil

# Function to perform an in-order traversal
# of a binary tree and print its nodes
def printInOrder(root):
    # Check if the current node
    # is null (base case for recursion)
    if not root:
        # If null, return and
        # terminate the function
        return
    
    # Recursively call printInOrder
    # for the left subtree
    printInOrder(root.left)
    
    # Print the value of the current node
    print(root.val, end=" ")
    
    # Recursively call printInOrder
    # for the right subtree
    printInOrder(root.right)

# Creating a BST
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(13)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(2)
root.left.left.right = TreeNode(4)
root.left.right = TreeNode(6)
root.left.right.right = TreeNode(9)
root.right.left = TreeNode(11)
root.right.right = TreeNode(14)

print("Binary Search Tree:")
printInOrder(root)
print()

solution = Solution()

# Searching for a value in the BST
target = 8
ciel = solution.findCeil(root, target)

if ciel != -1:
    print(f"Ceiling of {target} is: {ciel}")
else:
    print("No ceiling found!")
                           
                          


# 2 TODO : floor in a BST
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(log2N) where N is the number of nodes in the Binary Search Tree. In the best case scenario, where the tree is balanced, the time complexity is the height of the tree ie. log2N. In the worst-case scenario, where the tree is degenerate (linear), the time complexity becomes O(N), as it would require traversing all nodes along the path from the root to the leaf.

Space Complexity: O(1) since the algorithm does not use any additional space or data structures.
                            
# Definition of TreeNode structure
# for a binary tree node
class TreeNode:
    # Constructor to initialize the node with a
    # value and set left and right pointers to null
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Function to find the floor of a key
    # in a Binary Search Tree (BST)
    def floorInBST(self, root, key):
        # Initialize the floor variable
        # to store the floor value
        floor = -1
        
        # Traverse the BST until reaching
        # the end or finding the key
        while root:
            # If the key is found, assign it 
            # as the floor value and return
            if root.val == key:
                floor = root.val
                return floor
            
            # If the key is greater than the current
            # node's value, move to the right subtree
            if key > root.val:
                # Update the floor with the current node's
                # value and move to the right subtree
                floor = root.val
                root = root.right
            else:
                # If the key is smaller than the current
                # node's value, move to the left subtree
                root = root.left
        
        # Return the computed floor value
        return floor

# Function to perform an in-order traversal
# of a binary tree and print its nodes
def printInOrder(root):
    # Check if the current node
    # is null (base case for recursion)
    if root is None:
        # If null, return and
        # terminate the function
        return
    
    # Recursively call printInOrder
    # for the left subtree
    printInOrder(root.left)
    
    # Print the value of the current node
    print(root.val, end=" ")
    
    # Recursively call printInOrder
    # for the right subtree
    printInOrder(root.right)

# Creating a BST
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(13)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(2)
root.left.left.right = TreeNode(4)
root.left.right = TreeNode(6)
root.left.right.right = TreeNode(9)
root.right.left = TreeNode(11)
root.right.right = TreeNode(14)

print("Binary Search Tree:")
printInOrder(root)
print()

solution = Solution()

# Searching for a value in the BST
target = 8
ciel = solution.floorInBST(root, target)

if ciel != -1:
    print(f"Floor of {target} is: {ciel}")
else:
    print("No floor found!")
                           
                          


# 3 TODO : insert a given node in BST
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 4 TODO : delete a node in BST
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 5 TODO : find Kth smallest/largest element in BST
# method 1 : brute force approch
Time Complexity: O(N) where N is the number of nodes in the Binary Search Tree. because traversing the entire BST to perform an inorder traversal takes linear time. We visit each node once resulting in time complexity proportional to the number of nodes in the BST.

Space Complexity : O(N) where N is the number of nodes in the Binary Search Tree as additional space is required to store the elements of the BST in an array.
                                
# Definition of TreeNode structure
# for a binary tree node
class TreeNode:
    # Constructor to initialize the node with a
    # value and set left and right pointers to null
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Inorder traversal to populate
    # the list with BST elements
    def inorder(self, node, arr):
        if not node:
            return
        # Recursive call to the left subtree
        self.inorder(node.left, arr)
        
        # Append the value of current
        # node into the list
        arr.append(node.val)
        
        # Recursive call to the right subtree
        self.inorder(node.right, arr)
        return

    # Function to find the Kth
    # smallest and largest elements in BST
    def findKth(self, node, k):
        # List to store the
        # elements of the BST
        arr = []
        
        # Perform inorder traversal
        # to populate the list
        self.inorder(node, arr)
        
        # Calculate Kth largest
        # and smallest elements
        kLargest = arr[len(arr) - k]
        kSmallest = arr[k - 1]
        
        # Returning a tuple containing
        # Kth smallest and largest elements
        return (kSmallest, kLargest)


# Function to perform an in-order traversal
# of a binary tree and print its nodes
def printInOrder(root):
    # Check if the current node
    # is null (base case for recursion)
    if not root:
        # If null, return and
        # terminate the function
        return
    
    # Recursively call printInOrder
    # for the left subtree
    printInOrder(root.left)
    
    # Print the value of the current node
    print(root.val, end=" ")

    # Recursively call printInOrder
    # for the right subtree
    printInOrder(root.right)

# Creating a BST
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(13)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(2)
root.left.left.right = TreeNode(4)
root.left.right = TreeNode(6)
root.left.right.right = TreeNode(9)
root.right.left = TreeNode(11)
root.right.right = TreeNode(14)

print("Binary Search Tree:")
printInOrder(root)
print()

solution = Solution()

# Find the Kth smallest and largest elements
k = 3
print("k:", k)
kthElements = solution.findKth(root, k)

print("Kth smallest element:", kthElements[0])
print("Kth largest element:", kthElements[1])
                                
                              


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(N) where N is the number of nodes in the Binary Search Tree as we traverse in inorder and reverse inorder fashion to get to the required nodes. We visit each node once resulting in time complexity proportional to the number of nodes in the BST.

Space Complexity : as no additional space is allocated or data structures used to store any values.
                                
                     
# Definition of TreeNode class
# for a binary tree node
class TreeNode:
    def __init__(self, x):
        # Value of the node
        self.val = x
        
        # Pointer to the left child node
        self.left = None
        
        # Pointer to the right child node
        self.right = None

# Solution class to find Kth smallest and largest elements
class Solution:
    def __init__(self):
        pass

    # Helper function to perform reverse inorder
    # traversal to find Kth largest element
    def reverse_inorder(self, node, counter, k, k_largest):
        if not node or counter[0] >= k:
            return
        
        # Traverse right subtree
        self.reverse_inorder(node.right, counter, k, k_largest)

        # Increment counter after
        # visiting right subtree
        counter[0] += 1

        # Check if current node
        # is the Kth largest
        if counter[0] == k:
            k_largest[0] = node.val
            return

        # Traverse left subtree if
        # Kth largest is not found yet
        self.reverse_inorder(node.left, counter, k, k_largest)

    # Helper function to perform inorder
    # traversal to find Kth smallest element
    def inorder(self, node, counter, k, k_smallest):
        if not node or counter[0] >= k:
            return

        # Traverse left subtree
        self.inorder(node.left, counter, k, k_smallest)

        # Increment counter after visiting left subtree
        counter[0] += 1

        # Check if current node is the Kth smallest
        if counter[0] == k:
            k_smallest[0] = node.val
            return

        # Traverse right subtree if
        # Kth smallest is not found yet
        self.inorder(node.right, counter, k, k_smallest)

    def find_kth(self, root, k):
        k_smallest = [float('inf')]
        k_largest = [float('-inf')]
        # Counter to track visited nodes
        counter = [0]

        # Find Kth smallest element
        # (perform inorder traversal)
        self.inorder(root, counter, k, k_smallest)
        
        # Reset counter for Kth largest element
        counter[0] = 0
        # Find Kth largest element
        # (perform reverse inorder traversal)
        self.reverse_inorder(root, counter, k, k_largest)

        return k_smallest[0], k_largest[0]


# Function to perform an in-order traversal
# of a binary tree and print its nodes
def print_in_order(root):
    # Check if the current node
    # is null (base case for recursion)
    if not root:
        # If null, return and
        # terminate the function
        return
    
    # Recursively call printInOrder
    # for the left subtree
    print_in_order(root.left)

    # Print the value of the current node
    print(root.val, end=" ")

    # Recursively call printInOrder
    # for the right subtree
    print_in_order(root.right)

# Creating a BST
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(13)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(2)
root.left.left.right = TreeNode(4)
root.left.right = TreeNode(6)
root.left.right.right = TreeNode(9)
root.right.left = TreeNode(11)
root.right.right = TreeNode(14)

print("Binary Search Tree:")
print_in_order(root)
print()

solution = Solution()

# Find the Kth smallest and largest elements
k = 3
print("k:", k)
kth_elements = solution.find_kth(root, k)

print("Kth smallest element:", kth_elements[0])
print("Kth largest element:", kth_elements[1])
                                
                              


# 6 TODO : check if a tree is BST or BT
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 7 TODO : LCA in a BST
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 8 TODO : construct a BST from preorder traversal
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 9 TODO : inorder successor/predecessor in BST
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 10 TODO :  merge 2 BSTs
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 11 TODO : two sum in BST | check if there exists a pair with sum K
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 12 TODO : remove BST | connest BST with two nodes swapped
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 13 TODO : largest BST in binary tree
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      



# endregion



# region 15.1 GRAPHS - LEARNING
# -----------------------------

# 1 TODO :  graphs and types
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 2 TODO : graph implementation |c++
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 3 TODO : graph implementation | java
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 4 TODO : connected components | logic explanation
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 5 TODO : BFS
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 6 TODO : DFS
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      




# endregion



# region 15.2 GRAPHS - BFS/DFS
# ----------------------------
# 1 TODO :  number of provinces (leetcode)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 2 TODO : connected components problem in matrix
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 3 TODO : return oranges
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 4 TODO : flood fill
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 5 TODO : cycle detectio in undirected graph (BFS)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 6 TODO : cycle detectio in undirected graph (DFS)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 7 TODO : 0/1 matrix (BFS problem)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 8 TODO : surrounded regions (DFS)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 9 TODO : number of enclaves (flood fill implementation - multisource)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 10 TODO :  word index - 1
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 11 TODO : word index - 2
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 12 TODO : number of distinct islands (DFS multi source)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 13 TODO : bipartite Graphs (DFS)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 14 TODO : cucle detection in directed graph (DFS)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      




# endregion



# region 15.3 GRAPHS - TOPO SORT
# ------------------------------

# 1 TODO :  topo sort
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 2 TODO : kahn's algorithm
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 3 TODO : cycle detection in directed graph (BFS)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 4 TODO : course schedule - I
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 5 TODO : course schedule - 2
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 6 TODO : find eventual safe states
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 7 TODO : alien dictionary
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      




# endregion


# region 15.4 GRAPHS - SORTEST PATH
# ---------------------------------

# 1 TODO :  shortest path in UG with unit weights
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 2 TODO : shortest path in DAG
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 3 TODO : Dijkatra's algorithm
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 4 TODO : why parity queue is used in dijkatra's algorithm
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 5 TODO : shortest path in binary tree
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 6 TODO : path with minimum effort
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 7 TODO : cheapest flights with K stops
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 8 TODO : network delay time
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 9 TODO : number of ways to arive at destination
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 10 TODO :  minimum steps to reach end from start by performing multiplicationand mod with array elements
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 11 TODO : bellman ford algorithm
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 12 TODO : floyd warshall algorithm
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 13 TODO : find the city with the smallest number of neighbours at a threshold distance
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      




# endregion


# region 15.5 GRAPHS - MST/DISJOINT SET
# -------------------------------------

# 1 TODO :  minimu spanning tree
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 2 TODO : prism's algorithm
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 3 TODO : disjoint set (union by rank)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 4 TODO : disjoint set (union by size)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 5 TODO : kruskal's algorithm
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 6 TODO : number of operations to make network connected
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 7 TODO : most stones removed with the same rows or columns
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 8 TODO : accounts merge
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 9 TODO : number of islands - II
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 10 TODO :  making a large island
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 11 TODO : swim in rising water
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# endregion


# region 15.6 GRAPHS - OTHER ALGORITHMS
# -------------------------------------

# 1 TODO :  bridges in graph
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 2 TODO : articulation point
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 3 TODO : kosaraju's algorithm
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      




# endregion



# region 16.1 DP - INTRODUCTION
# -----------------------------

# 1 TODO :  dynamic programming introduction
# method 1 : memoization
Time Complexity: O(N)

Reason: The overlapping subproblems will return the answer in constant time O(1). Therefore the total number of new subproblems we solve is ‘n’. Hence total time complexity is O(N).

Space Complexity: O(N)

Reason: We are using a recursion stack space(O(N)) and an array (again O(N)). Therefore total space complexity will be O(N) + O(N) ≈ O(N)

def f(n, dp):
    if n <= 1:
        return n
    
    if dp[n] != -1:
        return dp[n]
    dp[n] = f(n-1, dp) + f(n-2, dp)
    return dp[n]

if __name__ == "__main__":
    n = 5
    dp = [-1] * (n+1)
    print(f(n, dp)) 


# method 2 tabulation
Time Complexity: O(N)

Reason: We are running a simple iterative loop

Space Complexity: O(N)

Reason: We are using an external array of size ‘n+1’.
from typing import List

def main():
    n = 5
    dp = [-1]*(n+1)

    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    print(dp[n])


# method 3 space optimization
Time Complexity: O(N)

Reason: We are running a simple iterative loop

Space Complexity: O(1)

Reason: We are not using any extra space
def main():
    n = 5

    prev2 = 0
    prev = 1

    for i in range(2, n+1):
        cur_i = prev2 + prev
        prev2 = prev
        prev = cur_i
    print(prev)

if __name__ == "__main__":
    main()
  



# endregion


# region 16.2 DP - 1D
# -------------------
# 1 TODO :  climbing stars
# method 1 : 
Time Complexity: O(N)

Reason: We are running a simple iterative loop

Space Complexity: O(N)

Reason: We are using an external array of size ‘n+1’.
def main():
    n = 3
    dp = [-1] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n+1):
      dp[i] = dp[i-1] + dp[i-2]
    print(dp[n])


if __name__ == "__main__":
    main()  


# method 2 : space optimization
Time Complexity: O(N)

Reason: We are running a simple iterative loop

Space Complexity: O(1)

Reason: We are not using any extra space.
def main():
    n = 3
    prev2 = 1
    prev = 1

    for i in range(2, n+1):
        cur_i = prev2 + prev
        prev2 = prev
        prev = cur_i

    print(prev)

if __name__ == "__main__":
    main()


# method 3 : optimal solution
# TC     -      
# SC     -      


# 2 TODO : frog jump (DP -3)
# method 1 : brute force approch
Time Complexity: O(N)

Reason: The overlapping subproblems will return the answer in constant time O(1). Therefore the total number of new subproblems we solve is ‘n’. Hence total time complexity is O(N).

Space Complexity: O(N)

Reason: We are using a recursion stack space(O(N)) and an array (again O(N)). Therefore total space complexity will be O(N) + O(N) ≈ O(N)

import sys
import math

def solve(ind, height, dp):
    if ind == 0:
        return 0
    if dp[ind] != -1:
        return dp[ind]
    jumpTwo = sys.maxsize
    jumpOne = solve(ind-1, height, dp) + abs(height[ind] - height[ind-1])
    if ind > 1:
        jumpTwo = solve(ind-2, height, dp) + abs(height[ind] - height[ind-2])
    dp[ind] = min(jumpOne, jumpTwo)
    return dp[ind]

if __name__ == "__main__":
    height = [30, 10, 60, 10, 60, 50]
    n = len(height)
    dp = [-1] * n
    print(solve(n-1, height, dp))

    


# method 2 : better approch
Time Complexity: O(N)

Reason: We are running a simple iterative loop

Space Complexity: O(N)

Reason: We are using an external array of size ‘n+1’.

def main():
    height = [30, 10, 60, 10, 60, 50]
    n = len(height)
    dp = [-1 for _ in range(n)]
    dp[0] = 0
    for ind in range(1, n):
        jumpTwo = float('inf')
        jumpOne = dp[ind-1] + abs(height[ind]-height[ind-1])
        if ind > 1:
            jumpTwo = dp[ind-2] + abs(height[ind]-height[ind-2])
        dp[ind] = min(jumpOne, jumpTwo)
    print(dp[n-1])

if __name__ == "__main__":
    main()

    


# method 3 : optimal solution
Time Complexity: O(N)

Reason: We are running a simple iterative loop

Space Complexity: O(1)

Reason: We are not using any extra space.

import sys
def main():
    height = [30, 10, 60, 10, 60, 50]
    n = len(height)
    prev = 0
    prev2 = 0
    for i in range(1, n):
        jumpTwo = sys.maxsize
        jumpOne = prev + abs(height[i] - height[i - 1])
        if i > 1:
            jumpTwo = prev2 + abs(height[i] - height[i - 2])

        cur_i = min(jumpOne, jumpTwo)
        prev2 = prev
        prev = cur_i

    print(prev)

if __name__ == "__main__":
    main()





# 3 TODO : frog jump with k distances(DP - 4)
# method 1 : brute force approch
Time Complexity: O(N *K)

Reason: The overlapping subproblems will return the answer in constant time. Therefore the total number of new subproblems we solve is ‘n’. At every new subproblem, we are running another loop for K times. Hence total time complexity is O(N * K).

Space Complexity: O(N)

Reason: We are using a recursion stack space(O(N)) and an array (again O(N)). Therefore total space complexity will be O(N) + O(N) ≈ O(N)

import sys

# Recursive function to calculate the minimum cost to reach the end
# from a given index with at most 'k' jumps.
def solveUtil(ind, height, dp, k):
    # Base case: If we are at the beginning (index 0), no cost is needed.
    if ind == 0:
        return 0
    # If the result for this index has been previously calculated, return it.
    if dp[ind] != -1:
        return dp[ind]

    mmSteps = sys.maxsize

    # Loop to try all possible jumps from '1' to 'k'
    for j in range(1, k + 1):
        # Ensure that we do not jump beyond the beginning of the array
        if ind - j >= 0:
            # Calculate the cost for this jump and update mmSteps with the minimum cost
            jump = solveUtil(ind - j, height, dp, k) + abs(height[ind] - height[ind - j])
            mmSteps = min(jump, mmSteps)

    # Store the minimum cost for this index in the dp array and return it.
    dp[ind] = mmSteps
    return dp[ind]

# Function to find the minimum cost to reach the end of the array
def solve(n, height, k):
    dp = [-1] * n  # Initialize a memoization array to store calculated results
    return solveUtil(n - 1, height, dp, k)  # Start the recursion from the last index

def main():
    height = [30, 10, 60, 10, 60, 50]
    n = len(height)
    k = 2
    print(solve(n, height, k))  # Print the result of the solve function

if __name__ == "__main__":
    main()




# method 2 : better approch
Time Complexity: O(N*K)

Reason: We are running two nested loops, where outer loops run from 1 to n-1 and the inner loop runs from 1 to K

Space Complexity: O(N)

Reason: We are using an external array of size ‘n’’.

import sys

# Helper function to solve the problem using dynamic programming
def solve_util(n, height, dp, k):
    # Initialize the first element of the dp array as 0 since no steps are needed to reach the first position
    dp[0] = 0

    # Loop through the elements of the height array
    for i in range(1, n):
        mmSteps = sys.maxsize  # Initialize the minimum steps to a large value
        for j in range(1, k+1):
            if i - j >= 0:
                # Calculate the number of steps required to reach the current position from the previous positions
                jump = dp[i - j] + abs(height[i] - height[i - j])
                mmSteps = min(jump, mmSteps)  # Update the minimum steps
        dp[i] = mmSteps  # Store the minimum steps needed to reach the current position

    return dp[n-1]  # Return the minimum steps needed to reach the last position

# Main function to solve the problem
def solve(n, height, k):
    dp = [-sys.maxsize] * n  # Initialize a dp array with large negative values
    return solve_util(n, height, dp, k)  # Call the helper function

# Entry point of the program
def main():
    height = [30, 10, 60, 10, 60, 50]
    n = len(height)
    k = 2
    dp = [-sys.maxsize] * n  # Initialize dp array
    result = solve(n, height, k)  # Call the solve function
    print(result)  # Print the result

if __name__ == "__main__":
    main()

 


# method 3 : optimal solution
# TC     -      
# SC     -      


# 4 TODO : maximum sum of non-adjacent elements (DP-5)
# method 1 : brute force approch
Time Complexity: O(N)

Reason: The overlapping subproblems will return the answer in constant time O(1). Therefore the total number of new subproblems we solve is ‘n’. Hence total time complexity is O(N).

Space Complexity: O(N)

Reason: We are using a recursion stack space(O(N)) and an array (again O(N)). Therefore total space complexity will be O(N) + O(N) ≈ O(N)

# Function to solve the problem using dynamic programming
def solveUtil(ind, arr, dp):
    # Check if the solution for this index has already been calculated
    if dp[ind] != -1:
        return dp[ind]
    
    # Base case: when the index is 0, return the value at that index
    if ind == 0:
        return arr[ind]
    
    # Base case: when the index is negative, return 0 (out of bounds)
    if ind < 0:
        return 0
    
    # Calculate the maximum value when picking the current element
    pick = arr[ind] + solveUtil(ind - 2, arr, dp)
    
    # Calculate the maximum value when not picking the current element
    nonPick = 0 + solveUtil(ind - 1, arr, dp)
    
    # Store the maximum of the two choices in the DP table
    dp[ind] = max(pick, nonPick)
    
    # Return the maximum value for the current index
    return dp[ind]

# Function to solve the problem for the given array
def solve(n, arr):
    # Initialize a DP table with -1 values to store intermediate results
    dp = [-1 for i in range(n)]
    
    # Call the recursive utility function to find the maximum value
    return solveUtil(n - 1, arr, dp)

# Main function to test the code
def main():
    arr = [2, 1, 4, 9]
    n = len(arr)
    
    # Call the solve function and print the result
    print(solve(n, arr))

if __name__ == '__main__':
    main()

 


# method 2 : better approch
Time Complexity: O(N)

Reason: We are running a simple iterative loop

Space Complexity: O(N)

Reason: We are using an external array of size ‘n+1’.

# Function to solve the problem using dynamic programming
def solveUtil(n, arr, dp):
    # Initialize the first element of the DP table with the first element of the array
    dp[0] = arr[0]
    
    # Loop through the array starting from the second element
    for i in range(1, n):
        # Calculate the maximum value when picking the current element
        pick = arr[i]
        
        # Check if there are at least two elements before the current element
        if i > 1:
            pick += dp[i - 2]
        
        # Calculate the maximum value when not picking the current element
        non_pick = 0 + dp[i - 1]
        
        # Store the maximum of the two choices in the DP table
        dp[i] = max(pick, non_pick)
    
    # Return the maximum value for the last index
    return dp[n - 1]

# Function to solve the problem for the given array
def solve(n, arr):
    # Initialize a DP table with -1 values to store intermediate results
    dp = [-1 for _ in range(n)]
    
    # Call the solveUtil function to find the maximum value
    return solveUtil(n, arr, dp)

# Main function to test the code
def main():
    arr = [2, 1, 4, 9]
    n = len(arr)
    
    # Call the solve function and print the result
    print(solve(n, arr))

if __name__ == '__main__':
    main()




# method 3 : optimal solution
Time Complexity: O(N)

Reason: We are running a simple iterative loop

Space Complexity: O(1)

Reason: We are not using any extra space.

# Function to solve the problem of finding the maximum sum of non-adjacent elements in an array
def solve(n, arr):
    # Initialize variables to keep track of the previous maximum and the one before that
    prev = arr[0]  # Initialize with the first element of the array
    prev2 = 0      # Initialize with 0 because there is no element before the first
    
    # Loop through the array starting from the second element
    for i in range(1, n):
        # Calculate the maximum value when picking the current element
        pick = arr[i]
        
        # Check if there are at least two elements before the current element
        if i > 1:
            pick += prev2
        
        # Calculate the maximum value when not picking the current element
        non_pick = 0 + prev
        
        # Calculate the maximum value for the current index
        cur_i = max(pick, non_pick)
        
        # Update the 'prev' and 'prev2' variables for the next iteration
        prev2 = prev
        prev = cur_i
    
    # Return the maximum value for the last index, which represents the solution
    return prev

# Main function to test the code
def main():
    arr = [2, 1, 4, 9]
    n = len(arr)
    
    # Call the solve function and print the result
    print(solve(n, arr))

if __name__ == "__main__":
    main()

    


# 5 TODO : house robber (DP-6)
# method 1 : brute force approch
Time Complexity: O(N )

Reason: We are running a simple iterative loop, two times. Therefore total time complexity will be O(N) + O(N) ≈ O(N)

Space Complexity: O(1)

Reason: We are not using extra space.
def solve(arr):
    n = len(arr)
    prev = arr[0]
    prev2 = 0

    for i in range(1, n):
        pick = arr[i]
        if i > 1:
            pick += prev2
        nonPick = 0 + prev

        cur_i = max(pick, nonPick)
        prev2 = prev
        prev = cur_i

    return prev

def robStreet(n, arr):
    arr1 = []
    arr2 = []

    if n == 1:
        return arr[0]

    for i in range(n):
        if i != 0:
            arr1.append(arr[i])
        if i != n - 1:
            arr2.append(arr[i])

    ans1 = solve(arr1)
    ans2 = solve(arr2)

    return max(ans1, ans2)

def main():
    arr = [1, 5, 1, 2, 6]
    n = len(arr)
    print(robStreet(n, arr))

if __name__ == '__main__':
    main()   


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      





# endregion

# region 16.3 DP - 2D/3D/GRIDS
# ----------------------------
# 1 TODO :  ninjas's training (Dp-7)
# method 1 : brute force approch
Time Complexity: O(N*4*3)

Reason: There are N*4 states and for every state, we are running a for loop iterating three times.

Space Complexity: O(N) + O(N*4)

Reason: We are using a recursion stack space(O(N)) and a 2D array (again O(N*4)). Therefore total space complexity will be O(N) + O(N) ≈ O(N)

def f(day, last, points, dp):
    # Check if the result for this day and last activity is already computed.
    if dp[day][last] != -1:
        return dp[day][last]

    # Base case: When we reach day 0, return the maximum point for the last day.
    if day == 0:
        maxi = 0
        for i in range(3):
            if i != last:
                maxi = max(maxi, points[0][i])
        dp[day][last] = maxi
        return dp[day][last]

    maxi = 0
    # Iterate through all activities for the current day.
    for i in range(3):
        if i != last:
            # Calculate the total points for the current day's activity and recursively call for the previous day.
            activity = points[day][i] + f(day - 1, i, points, dp)
            maxi = max(maxi, activity)

    # Store the maximum points in the DP table and return it.
    dp[day][last] = maxi
    return dp[day][last]

def ninjaTraining(n, points):
    # Initialize a DP table to store the computed results.
    dp = [[-1 for j in range(4)] for i in range(n)]
    # Start the recursive function from the last day with no previous activity.
    return f(n - 1, 3, points, dp)

def main():
    # Define the points matrix for each day.
    points = [[10, 40, 70],
              [20, 50, 80],
              [30, 60, 90]]

    n = len(points)  # Get the number of days.
    # Call the ninjaTraining function to find the maximum points.
    print(ninjaTraining(n, points))

if __name__ == '__main__':
    main()

   


# method 2 : better approch
Time Complexity: O(N*4*3)

Reason: There are three nested loops

Space Complexity: O(N*4)

Reason: We are using an external array of size ‘N*4’’.

def ninjaTraining(n, points):
    # Initialize a DP table with dimensions (n x 4) to store the maximum points.
    dp = [[0 for j in range(4)] for i in range(n)]

    # Initialize the DP table for day 0 with base cases.
    dp[0][0] = max(points[0][1], points[0][2])
    dp[0][1] = max(points[0][0], points[0][2])
    dp[0][2] = max(points[0][0], points[0][1])
    dp[0][3] = max(points[0][0], max(points[0][1], points[0][2]))

    # Loop through the days starting from the second day.
    for day in range(1, n):
        for last in range(4):
            dp[day][last] = 0  # Initialize the maximum points for the current day and last activity.
            for task in range(3):
                if task != last:
                    # Calculate the total points for the current day's activity and the previous day's maximum points.
                    activity = points[day][task] + dp[day - 1][task]
                    dp[day][last] = max(dp[day][last], activity)

    # Return the maximum points achievable after the last day with any activity.
    return dp[n - 1][3]

def main():
    # Define the points matrix for each day.
    points = [[10, 40, 70],
              [20, 50, 80],
              [30, 60, 90]]
    n = len(points)  # Get the number of days.
    # Call the ninjaTraining function to find the maximum points.
    print(ninjaTraining(n, points))

if __name__ == '__main__':
    main()

 


# method 3 : optimal solution
Time Complexity: O(N*4*3)

Reason: There are three nested loops

Space Complexity: O(4)

Reason: We are using an external array of size ‘4’ to store only one row.

def ninjaTraining(n, points):
    # Initialize a list 'prev' to store the maximum points for each possible last activity on the previous day.
    prev = [0] * 4

    # Initialize 'prev' with the maximum points for the first day's activities.
    prev[0] = max(points[0][1], points[0][2])
    prev[1] = max(points[0][0], points[0][2])
    prev[2] = max(points[0][0], points[0][1])
    prev[3] = max(points[0][0], max(points[0][1], points[0][2]))

    # Loop through the days starting from the second day.
    for day in range(1, n):
        # Initialize a temporary list 'temp' to store the maximum points for each possible last activity on the current day.
        temp = [0] * 4

        for last in range(4):
            # Initialize 'temp' for the current last activity.
            temp[last] = 0

            for task in range(3):
                if task != last:
                    # Calculate the total points for the current day's activity and the previous day's maximum points.
                    activity = points[day][task] + prev[task]
                    # Update 'temp' with the maximum points for the current last activity.
                    temp[last] = max(temp[last], activity)

        # Update 'prev' with 'temp' for the next iteration.
        prev = temp

    # Return the maximum points achievable after the last day with any activity.
    return prev[3]

def main():
    # Define the points matrix for each day.
    points = [[10, 40, 70],
              [20, 50, 80],
              [30, 60, 90]]
    n = len(points)  # Get the number of days.
    # Call the ninjaTraining function to find and print the maximum points.
    print(ninjaTraining(n, points))

if __name__ == '__main__':
    main()

 


# 2 TODO : grid unique paths : DP on grids (DP-8)
# method 1 : brute force approch
Time Complexity: O(M*N)

Reason: At max, there will be M*N calls of recursion.

Space Complexity: O((N-1)+(M-1)) + O(M*N)

Reason: We are using a recursion stack space: O((N-1)+(M-1)), here (N-1)+(M-1) is the path length and an external DP Array of size ‘M*N’.

def countWaysUtil(i, j, dp):
    # Base case: If we reach the top-left corner (i=0, j=0), there is one way to reach there.
    if i == 0 and j == 0:
        return 1
    # If either i or j goes out of bounds (negative), there is no way to reach that cell.
    if i < 0 or j < 0:
        return 0
    # If we have already calculated the number of ways for this cell, return it from the dp array.
    if dp[i][j] != -1:
        return dp[i][j]
    
    # Recursive calls to count the number of ways to reach the current cell.
    up = countWaysUtil(i - 1, j, dp)    # Moving up one row.
    left = countWaysUtil(i, j - 1, dp)  # Moving left one column.
    
    # Store the result in the dp array and return it.
    dp[i][j] = up + left
    return dp[i][j]

def countWays(m, n):
    # Initialize a memoization (dp) array to store intermediate results.
    dp = [[-1 for j in range(n)] for i in range(m)]
    
    # Call the utility function to compute the number of ways to reach the bottom-right cell (m-1, n-1).
    return countWaysUtil(m - 1, n - 1, dp)

def main():
    m = 3
    n = 2
    # Call the countWays function to calculate and print the number of ways to reach the destination.
    print(countWays(m, n))

if __name__ == '__main__':
    main()




# method 2 : better approch
Time Complexity: O(M*N)

Reason: There are two nested loops

Space Complexity: O(M*N)

Reason: We are using an external array of size ‘M*N’’.

def countWaysUtil(m, n, dp):
    # Loop through each cell in the grid
    for i in range(m):
        for j in range(n):
            # Base condition: If we are at the top-left corner, there is one way to reach it.
            if i == 0 and j == 0:
                dp[i][j] = 1
                continue
            
            # Initialize variables to store the number of ways from above and from the left.
            up = 0
            left = 0
            
            # Check if moving up is a valid option (not out of bounds).
            if i > 0:
                up = dp[i - 1][j]
            
            # Check if moving left is a valid option (not out of bounds).
            if j > 0:
                left = dp[i][j - 1]
            
            # Calculate and store the number of ways to reach the current cell.
            dp[i][j] = up + left
    
    # The bottom-right cell (m-1, n-1) now contains the total number of ways to reach there.
    return dp[m - 1][n - 1]

def countWays(m, n):
    # Initialize a memoization (dp) array to store intermediate results.
    dp = [[-1 for j in range(n)] for i in range(m)]
    
    # Call the utility function to compute the number of ways to reach the destination.
    return countWaysUtil(m, n, dp)

def main():
    m = 3
    n = 2
    # Call the countWays function to calculate and print the number of ways to reach the destination.
    print(countWays(m, n))

if __name__ == '__main__':
    main()





# method 3 : optimal solution
Time Complexity: O(M*N)

Reason: There are two nested loops

Space Complexity: O(N)

Reason: We are using an external array of size ‘N’ to store only one row.

def countWays(m, n):
    # Initialize a previous row to store intermediate results.
    prev = [0] * n

    # Loop through each row of the grid.
    for i in range(m):
        # Initialize a temporary row to store current row results.
        temp = [0] * n
        
        # Loop through each column of the grid.
        for j in range(n):
            # Base case: If we are at the top-left corner, there is one way to reach it.
            if i == 0 and j == 0:
                temp[j] = 1
                continue
            
            # Initialize variables to store the number of ways from above and from the left.
            up = 0
            left = 0
            
            # Check if moving up is a valid option (not out of bounds).
            if i > 0:
                up = prev[j]
            
            # Check if moving left is a valid option (not out of bounds).
            if j > 0:
                left = temp[j - 1]
                
            # Calculate and store the number of ways to reach the current cell.
            temp[j] = up + left
        
        # Update the previous row with the current row results.
        prev = temp
    
    # The last element in the previous row (prev) now contains the total number of ways to reach the destination.
    return prev[n - 1]

def main():
    m = 3
    n = 2
    # Call the countWays function to calculate and print the number of ways to reach the destination.
    print(countWays(m, n))

if __name__ == '__main__':
    main()




# 3 TODO : grid unique paths 2 (DP - 9)
# method 1 : brute force approch
Time Complexity: O(N*M)

Reason: At max, there will be N*M calls of recursion.

Space Complexity: O((M-1)+(N-1)) + O(N*M)

Reason: We are using a recursion stack space:O((M-1)+(N-1)), here (M-1)+(N-1) is the path length and an external DP Array of size ‘N*M’.

def mazeObstaclesUtil(i, j, maze, dp):
    # Base case: If we are out of bounds or at an obstacle, return 0.
    if i < 0 or j < 0 or maze[i][j] == -1:
        return 0

    # Base case: If we reach the starting point, return 1 (we found a path).
    if i == 0 and j == 0:
        return 1

    # If we've already computed the number of paths for this position, return it.
    if dp[i][j] != -1:
        return dp[i][j]

    # Move up and left in the maze, and recursively calculate the number of paths.
    up = mazeObstaclesUtil(i - 1, j, maze, dp)
    left = mazeObstaclesUtil(i, j - 1, maze, dp)

    # Store the result in the DP table and return it.
    dp[i][j] = up + left
    return dp[i][j]

def mazeObstacles(n, m, maze):
    # Create a DP table initialized with -1 values.
    dp = [[-1 for j in range(m)] for i in range(n)]
    
    # Call the utility function to find the number of paths.
    return mazeObstaclesUtil(n - 1, m - 1, maze, dp)

def main():
    # Example maze with 0s representing open paths and -1 representing obstacles.
    maze = [[0, 0, 0], [0, -1, 0], [0, 0, 0]]
    n = len(maze)
    m = len(maze[0])

    # Call the mazeObstacles function and print the result.
    print(mazeObstacles(n, m, maze))

if __name__ == '__main__':
    main()




# method 2 : better approch
Time Complexity: O(N*M)

Reason: There are two nested loops

Space Complexity: O(N*M)

Reason: We are using an external array of size ‘N*M’’.

def mazeObstaclesUtil(n, m, maze, dp):
    # Loop through each cell in the maze
    for i in range(n):
        for j in range(m):
            # Base conditions:
            # If we encounter an obstacle or we are out of bounds, set dp[i][j] to 0.
            if i > 0 and j > 0 and maze[i][j] == -1:
                dp[i][j] = 0
                continue
            # If we are at the starting point, set dp[i][j] to 1.
            if i == 0 and j == 0:
                dp[i][j] = 1
                continue
            
            # Initialize variables to store the number of paths coming from up and left.
            up = 0
            left = 0
            
            # If we can move up (i > 0), update 'up' with the value from the cell above.
            if i > 0:
                up = dp[i - 1][j]
            
            # If we can move left (j > 0), update 'left' with the value from the cell to the left.
            if j > 0:
                left = dp[i][j - 1]
            
            # Calculate the total number of paths to reach this cell and store it in dp[i][j].
            dp[i][j] = up + left
    
    # The result is stored in the bottom-right corner of the DP table.
    return dp[n - 1][m - 1]

def mazeObstacles(n, m, maze):
    # Create a DP table initialized with -1 values.
    dp = [[-1 for j in range(m)] for i in range(n)]
    
    # Call the utility function to find the number of paths.
    return mazeObstaclesUtil(n, m, maze, dp)

def main():
    # Example maze with 0s representing open paths and -1 representing obstacles.
    maze = [[0, 0, 0],
            [0, -1, 0],
            [0, 0, 0]]
    n = len(maze)
    m = len(maze[0])
    
    # Call the mazeObstacles function and print the result.
    print(mazeObstacles(n, m, maze))

if __name__ == "__main__":
    main()

 


# method 3 : optimal solution
Time Complexity: O(M*N)

Reason: There are two nested loops

Space Complexity: O(N)

Reason: We are using an external array of size ‘N’ to store only one row.

def mazeObstacles(n, m, maze):
    # Initialize the 'prev' list to keep track of the number of paths in the previous row.
    prev = [0] * m
    
    # Loop through each row of the maze.
    for i in range(n):
        # Initialize a temporary list to store the number of paths for the current row.
        temp = [0] * m
        
        # Loop through each cell in the current row.
        for j in range(m):
            # Base conditions:
            # If we encounter an obstacle or we are out of bounds, set 'temp[j]' to 0.
            if i > 0 and j > 0 and maze[i][j] == -1:
                temp[j] = 0
                continue
            # If we are at the starting point, set 'temp[j]' to 1.
            if i == 0 and j == 0:
                temp[j] = 1
                continue
            
            # Initialize variables to store the number of paths coming from up and left.
            up = 0
            left = 0
            
            # If we can move up (i > 0), update 'up' with the value from the previous row.
            if i > 0:
                up = prev[j]
            
            # If we can move left (j > 0), update 'left' with the value from the current row.
            if j > 0:
                left = temp[j - 1]
            
            # Calculate the total number of paths to reach this cell and store it in 'temp[j]'.
            temp[j] = up + left
        
        # Update 'prev' with the 'temp' list for the next iteration.
        prev = temp
    
    # The result is stored in the last element of the 'prev' list (bottom-right corner).
    return prev[m - 1]

def main():
    # Example maze with 0s representing open paths and -1 representing obstacles.
    maze = [[0, 0, 0],
            [0, -1, 0],
            [0, 0, 0]]
    n = len(maze)
    m = len(maze[0])
    
    # Call the mazeObstacles function and print the result.
    print(mazeObstacles(n, m, maze))

if __name__ == "__main__":
    main()

 


# 4 TODO : minimum path sum in grid (DP-10)
# method 1 : brute force approch
Time Complexity: O(N*M)

Reason: At max, there will be N*M calls of recursion.

Space Complexity: O((M-1)+(N-1)) + O(N*M)

Reason: We are using a recursion stack space: O((M-1)+(N-1)), here (M-1)+(N-1) is the path length and an external DP Array of size ‘N*M’.

def minSumPathUtil(i, j, matrix, dp):
    # Base case: If we are at the top-left corner, return the value of that cell.
    if i == 0 and j == 0:
        return matrix[0][0]
    
    # Base case: If we are out of bounds (negative indices), return a very large value.
    if i < 0 or j < 0:
        return int(1e9)
    
    # If we have already calculated the minimum sum for this cell, return it.
    if dp[i][j] != -1:
        return dp[i][j]

    # Calculate the minimum sum path recursively by considering both up and left moves.
    up = matrix[i][j] + minSumPathUtil(i-1, j, matrix, dp)
    left = matrix[i][j] + minSumPathUtil(i, j-1, matrix, dp)

    # Store the minimum of the two possible paths in the DP table.
    dp[i][j] = min(up, left)
    return dp[i][j]


def minSumPath(n, m, matrix):
    # Create a DP table initialized with -1 values.
    dp = [[-1 for j in range(m)] for i in range(n)]
    
    # Call the utility function to find the minimum sum path.
    return minSumPathUtil(n-1, m-1, matrix, dp)


def main():
    # Example matrix with values representing cell costs.
    matrix = [[5, 9, 6],
              [11, 5, 2]]

    n = len(matrix)
    m = len(matrix[0])

    # Call the minSumPath function and print the result.
    print(minSumPath(n, m, matrix))


if __name__ == '__main__':
    main()




# method 2 : better approch
Time Complexity: O(N*M)

Reason: There are two nested loops

Space Complexity: O(N*M)

Reason: We are using an external array of size ‘N*M’’.

def minSumPath(n, m, matrix):
    # Create a DP table initialized with zeros.
    dp = [[0 for j in range(m)] for i in range(n)]
    
    # Loop through each cell in the matrix.
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                # Base case: If we are at the top-left corner, set dp[i][j] to the value of that cell.
                dp[i][j] = matrix[i][j]
            else:
                # Calculate the cost of moving up from the cell (i, j).
                up = matrix[i][j]
                if i > 0:
                    up += dp[i-1][j]
                else:
                    # If we are at the top row and can't move up, set 'up' to a large value.
                    up += int(1e9)
                
                # Calculate the cost of moving left from the cell (i, j).
                left = matrix[i][j]
                if j > 0:
                    left += dp[i][j-1]
                else:
                    # If we are at the leftmost column and can't move left, set 'left' to a large value.
                    left += int(1e9)
                
                # Store the minimum cost of reaching the current cell in dp[i][j].
                dp[i][j] = min(up, left)
    
    # The result is stored in the bottom-right corner of the DP table.
    return dp[n-1][m-1]

def main():
    # Example matrix with values representing cell costs.
    matrix = [[5, 9, 6], [11, 5, 2]]
    n = len(matrix)
    m = len(matrix[0])
    
    # Call the minSumPath function and print the result.
    print(minSumPath(n, m, matrix))

if __name__ == "__main__":
    main()




# method 3 : optimal solution
Time Complexity: O(M*N)

Reason: There are two nested loops

Space Complexity: O(N)

Reason: We are using an external array of size ‘N’ to store only one row.

def minSumPath(n, m, matrix):
    # Initialize the 'prev' list to keep track of the minimum cost in the previous row.
    prev = [0] * m
    
    # Loop through each row of the matrix.
    for i in range(n):
        # Initialize a temporary list to store the minimum cost for the current row.
        temp = [0] * m
        
        # Loop through each cell in the current row.
        for j in range(m):
            if i == 0 and j == 0:
                # Base case: If we are at the top-left corner, set 'temp[j]' to the value of that cell.
                temp[j] = matrix[i][j]
            else:
                # Calculate the cost of moving up from the cell (i, j).
                up = matrix[i][j]
                if i > 0:
                    up += prev[j]
                else:
                    # If we are at the top row and can't move up, set 'up' to a large value.
                    up = int(1e9)
                
                # Calculate the cost of moving left from the cell (i, j).
                left = matrix[i][j]
                if j > 0:
                    left += temp[j-1]
                else:
                    # If we are at the leftmost column and can't move left, set 'left' to a large value.
                    left = int(1e9)
                
                # Store the minimum cost of reaching the current cell in 'temp[j]'.
                temp[j] = min(up, left)
        
        # Update 'prev' with the 'temp' list for the next iteration.
        prev = temp
    
    # The result is stored in the last element of the 'prev' list (bottom-right corner).
    return prev[m - 1]

def main():
    # Example matrix with values representing cell costs.
    matrix = [[5, 9, 6], [11, 5, 2]]
    n = len(matrix)
    m = len(matrix[0])
    
    # Call the minSumPath function and print the result.
    print(minSumPath(n, m, matrix))

if __name__ == '__main__':
    main()

    


# 5 TODO : minimum path sum in triangular grid (DP-11)
Time Complexity: O(N*N)

Reason: There are two nested loops

Space Complexity: O(N*N)

Reason: We are using an external array of size ‘N*N’. The stack space will be eliminated.

def minimumPathSumUtil(i, j, triangle, n, dp):
    # Check if we have already computed the minimum path sum for this cell
    if dp[i][j] != -1:
        return dp[i][j]

    # If we are at the bottom of the triangle, return the value in the current cell
    if i == n - 1:
        return triangle[i][j]

    # Calculate the minimum path sum by considering two possible moves: down and diagonal
    down = triangle[i][j] + minimumPathSumUtil(i + 1, j, triangle, n, dp)
    diagonal = triangle[i][j] + minimumPathSumUtil(i + 1, j + 1, triangle, n, dp)

    # Store the computed minimum path sum in the memoization table
    dp[i][j] = min(down, diagonal)
    return dp[i][j]

# Define a wrapper function to initialize memoization table and start the computation
def minimumPathSum(triangle, n):
    dp = [[-1 for j in range(n)] for i in range(n)]  # Initialize a memoization table with -1
    return minimumPathSumUtil(0, 0, triangle, n, dp)  # Start the recursive computation

# Define the main function where you set up the triangle and call the minimumPathSum function
def main():
    triangle = [[1], [2, 3], [3, 6, 7], [8, 9, 6, 10]]
    n = len(triangle)

    # Call the minimumPathSum function and print the result
    print(minimumPathSum(triangle, n))

# Check if this script is the main program entry point
if __name__ == "__main__":
    main()  # Call the main function to start the program

 


# method 2 : better approch
Time Complexity: O(N*N)

Reason: There are two nested loops

Space Complexity: O(N*N)

Reason: We are using an external array of size ‘N*N’. The stack space will be eliminated.

def minimum_path_sum(triangle, n):
    # Create a 2D array dp to store minimum path sums
    dp = [[0 for j in range(n)] for i in range(n)]
    
    # Initialize the bottom row of dp with the values from the last row of the triangle
    for j in range(n):
        dp[n - 1][j] = triangle[n - 1][j]
    
    # Start from the second-to-last row and work upwards
    for i in range(n - 2, -1, -1):
        for j in range(i, -1, -1):
            # Calculate the minimum path sum for the current cell by considering two possible moves: down and diagonal
            down = triangle[i][j] + dp[i + 1][j]
            diagonal = triangle[i][j] + dp[i + 1][j + 1]
            
            # Store the minimum of the two possible moves in dp
            dp[i][j] = min(down, diagonal)
    
    # The minimum path sum will be stored in dp[0][0] after the loops
    return dp[0][0]

def main():
    # Define the input triangle and its size
    triangle = [[1], [2, 3], [3, 6, 7], [8, 9, 6, 10]]
    n = len(triangle)
    
    # Call the minimum_path_sum function and print the result
    print(minimum_path_sum(triangle, n))

if __name__ == '__main__':
    main()



# method 3 : optimal solution
Time Complexity: O(N*N)

Reason: There are two nested loops

Space Complexity: O(N)

Reason: We are using an external array of size ‘N’ to store only one row.

def minimumPathSum(triangle, n):
    # Initialize two lists: front and cur to represent the current and previous rows in dp
    front = [0] * n  # This represents the previous row
    cur = [0] * n    # This represents the current row
    
    # Initialize the bottom row of dp (front) with the values from the last row of the triangle
    for j in range(n):
        front[j] = triangle[n - 1][j]
    
    # Start from the second-to-last row and work upwards
    for i in range(n - 2, -1, -1):
        for j in range(i, -1, -1):
            # Calculate the minimum path sum for the current cell by considering two possible moves: down and diagonal
            down = triangle[i][j] + front[j]
            diagonal = triangle[i][j] + front[j + 1]
            
            # Store the minimum of the two possible moves in the current row (cur)
            cur[j] = min(down, diagonal)
        
        # Update the previous row (front) with the current row (cur) for the next iteration
        front = cur
        
    # The minimum path sum will be stored in the first element of the front list after the loops
    return front[0]

def main():
    # Define the input triangle and its size
    triangle = [[1], [2, 3], [3, 6, 7], [8, 9, 6, 10]]
    n = len(triangle)
    
    # Call the minimumPathSum function and print the result
    print(minimumPathSum(triangle, n))

if __name__ == '__main__':
    main()

  


# 6 TODO : minimum/maximum falling path sum (DP-12)
# method 1 : brute force approch
Time Complexity: O(N*N)

Reason: At max, there will be M*N calls of recursion to solve a new problem,

Space Complexity: O(N) + O(N*M)

Reason: We are using a recursion stack space: O(N), where N is the path length and an external DP Array of size ‘N*M’.

import sys

# Recursive function to find the maximum path sum starting from cell (i, j)
def getMaxUtil(i, j, m, matrix, dp):
    # Base case: If j is out of bounds, return a large negative value
    if j < 0 or j >= m:
        return -int(1e9)
    
    # Base case: If we are at the top row (i == 0), return the value in the current cell
    if i == 0:
        return matrix[0][j]
    
    # Check if the maximum path sum for this cell has already been computed
    if dp[i][j] != -1:
        return dp[i][j]
    
    # Calculate three possible moves: going up, going up-left, and going up-right
    up = matrix[i][j] + getMaxUtil(i - 1, j, m, matrix, dp)
    leftDiagonal = matrix[i][j] + getMaxUtil(i - 1, j - 1, m, matrix, dp)
    rightDiagonal = matrix[i][j] + getMaxUtil(i - 1, j + 1, m, matrix, dp)
    
    # Store the maximum of the three moves in the memoization table
    dp[i][j] = max(up, max(leftDiagonal, rightDiagonal))
    return dp[i][j]

# Function to find the maximum path sum in the matrix
def getMaxPathSum(matrix):
    n = len(matrix)  # Number of rows
    m = len(matrix[0])  # Number of columns
    dp = [[-1 for j in range(m)] for i in range(n)]  # Initialize a memoization table
    maxi = -sys.maxsize  # Initialize the maximum sum to a large negative value
    
    # Iterate through the first row and find the maximum path sum starting from each cell
    for j in range(m):
        ans = getMaxUtil(n - 1, j, m, matrix, dp)
        maxi = max(maxi, ans)
    
    return maxi  # Return the maximum path sum

def main():
    # Define the input matrix
    matrix = [[1, 2, 10, 4], [100, 3, 2, 1], [1, 1, 20, 2], [1, 2, 2, 1]]
    
    # Call the getMaxPathSum function and print the result
    print(getMaxPathSum(matrix))

if __name__ == "__main__":
    main()




# method 2 : better approch
Time Complexity: O(N*M)

Reason: There are two nested loops

Space Complexity: O(N*M)

Reason: We are using an external array of size ‘N*M’. The stack space will be eliminated.

import sys

# Function to find the maximum path sum in the matrix
def getMaxPathSum(matrix):
    n = len(matrix)  # Number of rows
    m = len(matrix[0])  # Number of columns
    
    # Initialize a dynamic programming table (dp) with zeros
    dp = [[0 for j in range(m)] for i in range(n)]
    
    # Initializing the first row of dp as the base condition
    for j in range(m):
        dp[0][j] = matrix[0][j]
    
    # Iterate through the matrix to compute the maximum path sum
    for i in range(1, n):
        for j in range(m):
            # Calculate the three possible moves: up, left diagonal, and right diagonal
            up = matrix[i][j] + dp[i - 1][j]
            
            # Handle left diagonal
            left_diagonal = matrix[i][j]
            if j - 1 >= 0:
                left_diagonal += dp[i - 1][j - 1]
            else:
                left_diagonal += -int(1e9)  # A large negative value if out of bounds
            
            # Handle right diagonal
            right_diagonal = matrix[i][j]
            if j + 1 < m:
                right_diagonal += dp[i - 1][j + 1]
            else:
                right_diagonal += -int(1e9)  # A large negative value if out of bounds
            
            # Store the maximum of the three moves in dp
            dp[i][j] = max(up, left_diagonal, right_diagonal)
    
    # Find the maximum path sum in the last row of dp
    maxi = -sys.maxsize
    for j in range(m):
        maxi = max(maxi, dp[n - 1][j])
    
    return maxi  # Return the maximum path sum

def main():
    # Define the input matrix
    matrix = [[1, 2, 10, 4], [100, 3, 2, 1], [1, 1, 20, 2], [1, 2, 2, 1]]
    
    # Call the getMaxPathSum function and print the result
    print(getMaxPathSum(matrix))

if __name__ == "__main__":
    main()

  


# method 3 : optimal solution
Time Complexity: O(N*M)

Reason: There are two nested loops

Space Complexity: O(M)

Reason: We are using an external array of size ‘M’ to store only one row.

import sys

# Function to find the maximum path sum in the matrix
def getMaxPathSum(matrix):
    n = len(matrix)  # Number of rows
    m = len(matrix[0])  # Number of columns

    # Initialize two lists: prev (previous row) and cur (current row)
    prev = [0] * m
    cur = [0] * m

    # Initializing the first row of prev as the base condition
    for j in range(m):
        prev[j] = matrix[0][j]

    # Iterate through the matrix to compute the maximum path sum
    for i in range(1, n):
        for j in range(m):
            # Calculate the three possible moves: up, left diagonal, and right diagonal
            up = matrix[i][j] + prev[j]

            leftDiagonal = matrix[i][j]
            if j - 1 >= 0:
                leftDiagonal += prev[j - 1]
            else:
                leftDiagonal += -int(1e9)  # A large negative value if out of bounds

            rightDiagonal = matrix[i][j]
            if j + 1 < m:
                rightDiagonal += prev[j + 1]
            else:
                rightDiagonal += -int(1e9)  # A large negative value if out of bounds

            # Store the maximum of the three moves in the current row (cur)
            cur[j] = max(up, max(leftDiagonal, rightDiagonal))

        # Update prev with the values of cur for the next iteration
        prev = cur[:]

    # Find the maximum path sum in the last row of prev
    maxi = -sys.maxsize
    for j in range(m):
        maxi = max(maxi, prev[j])

    return maxi  # Return the maximum path sum

def main():
    # Define the input matrix
    matrix = [[1, 2, 10, 4], [100, 3, 2, 1], [1, 1, 20, 2], [1, 2, 2, 1]]

    # Call the getMaxPathSum function and print the result
    print(getMaxPathSum(matrix))

if __name__ == '__main__':
    main()




# 7 TODO : 3D DP : ninja and his friends (DP-13)
# method 1 : brute force approch
Time Complexity: O(N*M*M) * 9

Reason: At max, there will be N*M*M calls of recursion to solve a new problem and in every call, two nested loops together run for 9 times.

Space Complexity: O(N) + O(N*M*M)

Reason: We are using a recursion stack space: O(N), where N is the path length and an external DP Array of size ‘N*M*M’.

import sys

# Recursive function to find the maximum chocolates collected
def maxChocoUtil(i, j1, j2, n, m, grid, dp):
    # Base cases:
    # - If either of the indices is out of bounds, return a large negative value
    # - If we're at the last row, return the sum of chocolates in the two selected columns
    if j1 < 0 or j1 >= m or j2 < 0 or j2 >= m:
        return int(-1e9)
    if i == n - 1:
        if j1 == j2:
            return grid[i][j1]
        else:
            return grid[i][j1] + grid[i][j2]
    
    # If the result for these indices has already been computed, return it
    if dp[i][j1][j2] != -1:
        return dp[i][j1][j2]
    
    # Initialize the maximum chocolates collected to a large negative value
    maxi = -sys.maxsize
    
    # Iterate through the adjacent cells in the next row
    for di in range(-1, 2):
        for dj in range(-1, 2):
            ans = 0
            if j1 == j2:
                ans = grid[i][j1] + maxChocoUtil(i + 1, j1 + di, j2 + dj, n, m, grid, dp)
            else:
                ans = grid[i][j1] + grid[i][j2] + maxChocoUtil(i + 1, j1 + di, j2 + dj, n, m, grid, dp)
            maxi = max(maxi, ans)
    
    # Store the maximum chocolates collected in the memoization table
    dp[i][j1][j2] = maxi
    return maxi

# Function to find the maximum chocolates collected
def maximumChocolates(n, m, grid):
    # Initialize a memoization table with -1 values
    dp = [[[-1 for j in range(m)] for i in range(m)] for k in range(n)]
    
    # Start the recursion from the first row, columns 0 and m-1
    return maxChocoUtil(0, 0, m - 1, n, m, grid, dp)

def main():
    # Define the input matrix and its dimensions
    matrix = [[2, 3, 1, 2], [3, 4, 2, 2], [5, 6, 3, 5]]
    n = len(matrix)
    m = len(matrix[0])
    
    # Call the maximumChocolates function and print the result
    print(maximumChocolates(n, m, matrix))

if __name__ == "__main__":
    main()

   


# method 2 : better approch
Time Complexity: O(N*M*M)*9

Reason: The outer nested loops run for (N*M*M) times and the inner two nested loops run for 9 times.

Space Complexity: O(N*M*M)

Reason: We are using an external array of size ‘N*M*M’. The stack space will be eliminated.

import sys

# Function to find the maximum chocolates collected
def maximumChocolates(n, m, grid):
    # Initialize a 3D memoization table dp with zeros
    dp = [[[0 for _ in range(m)] for _ in range(m)] for _ in range(n)]

    # Initialize the values for the last row of dp based on grid values
    for j1 in range(m):
        for j2 in range(m):
            if j1 == j2:
                dp[n - 1][j1][j2] = grid[n - 1][j1]
            else:
                dp[n - 1][j1][j2] = grid[n - 1][j1] + grid[n - 1][j2]

    # Iterate through rows from the second-to-last row to the first row
    for i in range(n - 2, -1, -1):
        for j1 in range(m):
            for j2 in range(m):
                maxi = -sys.maxsize

                # Try out 9 possible options by changing the indices
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        ans = 0
                        if j1 == j2:
                            ans = grid[i][j1]
                        else:
                            ans = grid[i][j1] + grid[i][j2]

                        if ((j1 + di < 0 or j1 + di >= m) or (j2 + dj < 0 or j2 + dj >= m)):
                            ans += int(-1e9)  # A large negative value if out of bounds
                        else:
                            ans += dp[i + 1][j1 + di][j2 + dj]  # Add the value from the next row

                        maxi = max(ans, maxi)

                # Store the maximum chocolates collected in the memoization table
                dp[i][j1][j2] = maxi

    # Return the maximum chocolates collected in the top row and the last column
    return dp[0][0][m - 1]

def main():
    # Define the input matrix and its dimensions
    matrix = [[2, 3, 1, 2], [3, 4, 2, 2], [5, 6, 3, 5]]
    n = len(matrix)
    m = len(matrix[0])

    # Call the maximumChocolates function and print the result
    print(maximumChocolates(n, m, matrix))

if __name__ == '__main__':
    main()




# method 3 : optimal solution
Time Complexity: O(N*M*M)*9

Reason: The outer nested loops run for (N*M*M) times and the inner two nested loops run for 9 times.

Space Complexity: O(M*M)

Reason: We are using an external array of size ‘M*M’.

import sys

# Function to find the maximum chocolates collected
def maximumChocolates(n, m, grid):
    # Initialize two matrices: front (for the current row) and cur (for the next row)
    front = [[0] * m for _ in range(m)]
    cur = [[0] * m for _ in range(m)]

    # Initialize the values for the last row of front based on grid values
    for j1 in range(m):
        for j2 in range(m):
            if j1 == j2:
                front[j1][j2] = grid[n - 1][j1]
            else:
                front[j1][j2] = grid[n - 1][j1] + grid[n - 1][j2]

    # Iterate through rows from the second-to-last row to the first row
    for i in range(n - 2, -1, -1):
        for j1 in range(m):
            for j2 in range(m):
                maxi = -sys.maxsize

                # Try out 9 possible options by changing the indices
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        ans = 0
                        if j1 == j2:
                            ans = grid[i][j1]
                        else:
                            ans = grid[i][j1] + grid[i][j2]

                        if ((j1 + di < 0 or j1 + di >= m) or (j2 + dj < 0 or j2 + dj >= m)):
                            ans += int(-1e9)  # A large negative value if out of bounds
                        else:
                            ans += front[j1 + di][j2 + dj]  # Add the value from the current front row

                        maxi = max(ans, maxi)
                cur[j1][j2] = maxi

        # Update front with the values of cur for the next iteration
        front = [row[:] for row in cur]

    # Return the maximum chocolates collected in the top-left corner of front
    return front[0][m - 1]

def main():
    # Define the input matrix and its dimensions
    matrix = [[2, 3, 1, 2], [3, 4, 2, 2], [5, 6, 3, 5]]
    n = len(matrix)
    m = len(matrix[0])

    # Call the maximumChocolates function and print the result
    print(maximumChocolates(n, m, matrix))

if __name__ == '__main__':
    main()

   



# endregion

# region 16.4 DP - SUBSEQUENCES
# -----------------------------

# 1 TODO :  subset sum equals to target (DP-14)
# method 1 : brute force approch
Time Complexity: O(N*K)

Reason: There are N*K states therefore at max ‘N*K’ new problems will be solved.

Space Complexity: O(N*K) + O(N)

Reason: We are using a recursion stack space(O(N)) and a 2D array ( O(N*K)).

def subsetSumUtil(ind, target, arr, dp):
    # Check if the target sum has been achieved.
    if target == 0:
        return True

    # If we have reached the first element in the array.
    if ind == 0:
        return arr[0] == target

    # Check if the result for this combination of 'ind' and 'target' has already been computed.
    if dp[ind][target] != -1:
        return dp[ind][target]

    # Recursively try not taking the current element.
    notTaken = subsetSumUtil(ind - 1, target, arr, dp)

    taken = False
    # Check if the current element can be taken without exceeding the target.
    if arr[ind] <= target:
        taken = subsetSumUtil(ind - 1, target - arr[ind], arr, dp)

    # Store the result in the dp array to avoid recomputation.
    dp[ind][target] = notTaken or taken
    return dp[ind][target]

def subsetSumToK(n, k, arr):
    # Initialize a memoization table with -1.
    dp = [[-1 for j in range(k + 1)] for i in range(n)]

    # Call the utility function to find if a subset with the given target sum exists.
    return subsetSumUtil(n - 1, k, arr, dp)

def main():
    arr = [1, 2, 3, 4]
    k = 4
    n = len(arr)

    if subsetSumToK(n, k, arr):
        print("Subset with the given target found")
    else:
        print("Subset with the given target not found")

if __name__ == "__main__":
    main()




# method 2 : better approch
Time Complexity: O(N*K)

Reason: There are two nested loops

Space Complexity: O(N*K)

Reason: We are using an external array of size ‘N*K’. Stack Space is eliminated.

def subsetSumToK(n, k, arr):
    # Initialize a 2D DP table with False values.
    dp = [[False for j in range(k + 1)] for i in range(n)]
    
    # Set the first column to True since a sum of 0 is always possible with an empty subset.
    for i in range(n):
        dp[i][0] = True
    
    # Check if the first element of the array can be used to make the target sum.
    if arr[0] <= k:
        dp[0][arr[0]] = True
    
    # Fill in the DP table iteratively.
    for ind in range(1, n):
        for target in range(1, k + 1):
            notTaken = dp[ind - 1][target]  # Not taking the current element.
            taken = False
            # Check if taking the current element is possible without exceeding the target.
            if arr[ind] <= target:
                taken = dp[ind - 1][target - arr[ind]]
            dp[ind][target] = notTaken or taken  # Update the DP table with the result.
    
    # The final result is stored in the bottom-right cell of the DP table.
    return dp[n - 1][k]

def main():
    arr = [1, 2, 3, 4]
    k = 4
    n = len(arr)

    if subsetSumToK(n, k, arr):
        print("Subset with the given target found")
    else:
        print("Subset with the given target not found")

if __name__ == '__main__':
    main()




# method 3 : optimal solution
Time Complexity: O(N*K)

Reason: There are three nested loops

Space Complexity: O(K)

Reason: We are using an external array of size ‘K+1’ to store only one row.

def subset_sum_to_k(n, k, arr):
    # Initialize a boolean array 'prev' with size (k + 1).
    prev = [False] * (k + 1)
    
    # Set the first element of 'prev' to True since an empty subset can sum up to 0.
    prev[0] = True
    
    # Check if the first element of 'arr' can directly contribute to the target sum 'k'.
    if arr[0] <= k:
        prev[arr[0]] = True

    # Loop through the elements of 'arr' and update 'prev' using dynamic programming.
    for ind in range(1, n):
        # Initialize a new boolean array 'cur' for the current element.
        cur = [False] * (k + 1)
        
        # An empty subset can always sum up to 0.
        cur[0] = True
        
        for target in range(1, k + 1):
            not_taken = prev[target]  # Previous result without including the current element.
            taken = False
            
            # Check if including the current element is possible without exceeding the target.
            if arr[ind] <= target:
                taken = prev[target - arr[ind]]
            
            # Update 'cur' with the result for the current 'target'.
            cur[target] = not_taken or taken
        
        # Update 'prev' with the results for the current element 'ind'.
        prev = cur

    # The final result is stored in 'prev[k]'.
    return prev[k]

def main():
    arr = [1, 2, 3, 4]
    k = 4
    n = len(arr)

    if subset_sum_to_k(n, k, arr):
        print("Subset with the given target found")
    else:
        print("Subset with the given target not found")

if __name__ == "__main__":
    main()




# 2 TODO : partition equal subset sum (DP-15)
# method 1 : brute force approch
Time Complexity: O(N*K) + O(N)

Reason: There are N*K states therefore at max ‘N*K’ new problems will be solved and we are running a for loop for ‘N’ times to calculate the total sum

Space Complexity: O(N*K) + O(N)

Reason: We are using a recursion stack space(O(N)) and a 2D array ( O(N*K)).

def subsetSumUtil(ind, target, arr, dp):
    # Base case: If the target sum is 0, we have found a subset that sums to the target.
    if target == 0:
        return True
    
    # Base case: If we have reached the first element of the array, check if it equals the target.
    if ind == 0:
        return arr[0] == target
    
    # Check if the result for this combination of 'ind' and 'target' has already been computed.
    if dp[ind][target] != -1:
        return dp[ind][target]
    
    # Recursive cases:
    # 1. Try not taking the current element.
    notTaken = subsetSumUtil(ind - 1, target, arr, dp)
    
    # 2. Try taking the current element if it is less than or equal to the target.
    taken = False
    if arr[ind] <= target:
        taken = subsetSumUtil(ind - 1, target - arr[ind], arr, dp)
        
    # Update the DP table and return the result.
    dp[ind][target] = notTaken or taken
    return dp[ind][target]

def canPartition(n, arr):
    # Calculate the total sum of the array elements.
    totSum = sum(arr)
    
    # If the total sum is odd, it cannot be partitioned into two equal subsets.
    if totSum % 2 == 1:
        return False
    else:
        # Calculate the target sum for each subset.
        k = totSum // 2
        
        # Initialize a memoization table for dynamic programming.
        dp = [[-1 for i in range(k + 1)] for j in range(n)]
        
        # Call the subsetSumUtil function to check if a subset with sum 'k' exists.
        return subsetSumUtil(n - 1, k, arr, dp)

def main():
    arr = [2, 3, 3, 3, 4, 5]
    n = len(arr)
    
    # Check if the array can be partitioned into two equal subsets and print the result.
    if canPartition(n, arr):
        print("The Array can be partitioned into two equal subsets")
    else:
        print("The Array cannot be partitioned into two equal subsets")

if __name__ == "__main__":
    main()




# method 2 : better approch
Time Complexity: O(N*K) +O(N)

Reason: There are two nested loops that account for O(N*K) and at starting we are running a for loop to calculate totSum.

Space Complexity: O(N*K)

Reason: We are using an external array of size ‘N*K’. Stack Space is eliminated.

def canPartition(n, arr):
    # Calculate the total sum of the array elements.
    totSum = sum(arr)
    
    # If the total sum is odd, it cannot be partitioned into two equal subsets.
    if totSum % 2 == 1:
        return False
    else:
        # Calculate the target sum for each subset.
        k = totSum // 2
        
        # Initialize a dynamic programming table (dp) to store subproblem results.
        dp = [[False for j in range(k + 1)] for i in range(n)]

        # Initialize the base case: An empty subset can always achieve a sum of 0.
        for i in range(n):
            dp[i][0] = True

        # Initialize the base case for the first element in the array.
        if arr[0] <= k:
            dp[0][arr[0]] = True

        # Fill in the DP table using a bottom-up approach.
        for ind in range(1, n):
            for target in range(1, k + 1):
                # If the current element is not taken, the result is the same as the previous row.
                notTaken = dp[ind - 1][target]
                
                # If the current element is taken, subtract its value from the target and check the previous row.
                taken = False
                if arr[ind] <= target:
                    taken = dp[ind - 1][target - arr[ind]]
                
                # Update the DP table with the result of taking or not taking the current element.
                dp[ind][target] = notTaken or taken
        
        # The final result is stored in the bottom-right cell of the DP table.
        return dp[n - 1][k]

def main():
    arr = [2, 3, 3, 3, 4, 5]
    n = len(arr)
    
    # Check if the array can be partitioned into two equal subsets and print the result.
    if canPartition(n, arr):
        print("The Array can be partitioned into two equal subsets")
    else:
        print("The Array cannot be partitioned into two equal subsets")

if __name__ == '__main__':
    main()




# method 3 : optimal solution
Time Complexity: O(N*K) +O(N)

Reason: There are two nested loops that account for O(N*K) and at starting we are running a for loop to calculate totSum.

Space Complexity: O(K)

Reason: We are using an external array of size ‘K+1’ to store only one row.

def canPartition(n, arr):
    # Calculate the total sum of the array elements.
    totSum = sum(arr)
    
    # If the total sum is odd, it cannot be partitioned into two equal subsets.
    if totSum % 2 == 1:
        return False
    else:
        # Calculate the target sum for each subset.
        k = totSum // 2
        
        # Initialize a boolean array 'prev' to store the results for the previous row.
        prev = [False] * (k + 1)
        prev[0] = True  # Base case: An empty subset can always achieve a sum of 0.
        
        # Handle the base case for the first element in the array.
        if arr[0] <= k:
            prev[arr[0]] = True

        # Iterate through the elements in the array.
        for ind in range(1, n):
            # Initialize a new boolean array 'cur' for the current row.
            cur = [False] * (k + 1)
            cur[0] = True  # An empty subset can always achieve a sum of 0.

            # Fill in the 'cur' array using dynamic programming.
            for target in range(1, k + 1):
                # If the current element is not taken, the result is the same as the previous row.
                notTaken = prev[target]
                
                # If the current element is taken, subtract its value from the target and check the previous row.
                taken = False
                if arr[ind] <= target:
                    taken = prev[target - arr[ind]]
                
                # Update the 'cur' array with the result of taking or not taking the current element.
                cur[target] = notTaken or taken
            
            # Update 'prev' to 'cur' for the next iteration.
            prev = cur
        
        # The final result is stored in 'prev[k]', indicating whether a subset with sum 'k' is possible.
        return prev[k]

def main():
    arr = [2, 3, 3, 3, 4, 5]
    n = len(arr)
    
    # Check if the array can be partitioned into two equal subsets and print the result.
    if canPartition(n, arr):
        print("The Array can be partitioned into two equal subsets")
    else:
        print("The Array cannot be partitioned into two equal subsets")

if __name__ == "__main__":
    main()

    


# 3 TODO : partition set into 2 subsets with min absolute sum diff (DP-16)
# method 1 : brute force approch
Time Complexity: O(N*totSum) +O(N) +O(N)

Reason: There are two nested loops that account for O(N*totSum), at starting we are running a for loop to calculate totSum and at last a for loop to traverse the last row.

Space Complexity: O(N*totSum) + O(N)

Reason: We are using an external array of size ‘N * totSum’ and a stack space of O(N).

def subsetSumUtil(ind, target, arr, dp):
    # Base case: If the target sum is 0, we have found a subset that sums to the target.
    if target == 0:
        return True

    # Base case: If we have reached the first element of the array, check if it equals the target.
    if ind == 0:
        return arr[0] == target

    # Check if the result for this combination of 'ind' and 'target' has already been computed.
    if dp[ind][target] != -1:
        return dp[ind][target]

    # Recursive cases:
    # 1. Try not taking the current element.
    notTaken = subsetSumUtil(ind - 1, target, arr, dp)

    # 2. Try taking the current element if it is less than or equal to the target.
    taken = False
    if arr[ind] <= target:
        taken = subsetSumUtil(ind - 1, target - arr[ind], arr, dp)

    # Update the DP table and return the result.
    dp[ind][target] = notTaken or taken
    return dp[ind][target]

def minSubsetSumDifference(arr):
    n = len(arr)
    totSum = sum(arr)

    # Initialize a DP table to store the subset sum information.
    dp = [[-1 for i in range(totSum + 1)] for j in range(n)]

    # Calculate dummy values for all possible sums using subsetSumUtil.
    for i in range(totSum + 1):
        dummy = subsetSumUtil(n - 1, i, arr, dp)

    # Initialize a variable to track the minimum absolute difference.
    mini = int(1e9)

    # Iterate through all possible sums.
    for i in range(totSum + 1):
        if dp[n - 1][i] == True:
            # Calculate the difference between the current sum and the complement sum.
            diff = abs(i - (totSum - i))
            mini = min(mini, diff)

    return mini

def main():
    arr = [1, 2, 3, 4]
    print("The minimum absolute difference is:", minSubsetSumDifference(arr))

if __name__ == "__main__":
    main()




# method 2 : better approch
Time Complexity: O(N*totSum) +O(N) +O(N)

Reason: There are two nested loops that account for O(N*totSum), at starting we are running a for loop to calculate totSum, and at last a for loop to traverse the last row.

Space Complexity: O(N*totSum)

Reason: We are using an external array of size ‘N * totSum’. Stack Space is eliminated.

def minSubsetSumDifference(arr, n):
    # Calculate the total sum of the array elements.
    totSum = sum(arr)

    # Initialize a DP table to store subset sum information.
    dp = [[False for i in range(totSum + 1)] for j in range(n)]

    # Initialize the base cases for the DP table.
    for i in range(n):
        dp[i][0] = True

    # Handle the base case for the first element in the array.
    if arr[0] <= totSum:
        dp[0][arr[0]] = True

    # Fill in the DP table using dynamic programming.
    for ind in range(1, n):
        for target in range(1, totSum + 1):
            # If the current element is not taken, the result is the same as the previous row.
            notTaken = dp[ind - 1][target]

            # If the current element is taken, subtract its value from the target and check the previous row.
            taken = False
            if arr[ind] <= target:
                taken = dp[ind - 1][target - arr[ind]]

            # Update the DP table with the result of taking or not taking the current element.
            dp[ind][target] = notTaken or taken

    # Initialize a variable to track the minimum absolute difference.
    mini = int(1e9)

    # Iterate through all possible sums.
    for i in range(totSum + 1):
        if dp[n - 1][i] == True:
            # Calculate the difference between the current sum and the complement sum.
            diff = abs(i - (totSum - i))
            mini = min(mini, diff)

    return mini

def main():
    arr = [1, 2, 3, 4]
    n = len(arr)

    # Find and print the minimum absolute difference between two subsets.
    print("The minimum absolute difference is:", minSubsetSumDifference(arr, n))

if __name__ == '__main__':
    main()

  


# method 3 : optimal solution
Time Complexity: O(N*totSum) +O(N) +O(N)

Reason: There are two nested loops that account for O(N*totSum), at starting we are running a for loop to calculate totSum and at last a for loop to traverse the last row.

Space Complexity: O(totSum)

Reason: We are using an external array of size ‘totSum+1’ to store only one row.

def minSubsetSumDifference(arr, n):
    # Calculate the total sum of the array elements.
    totSum = sum(arr)
    
    # Initialize a boolean array 'prev' to store the results for the previous row.
    prev = [False] * (totSum + 1)
    prev[0] = True  # Base case: An empty subset can always achieve a sum of 0.

    # Handle the base case for the first element in the array.
    if arr[0] <= totSum:
        prev[arr[0]] = True

    # Iterate through the elements in the array.
    for ind in range(1, n):
        # Initialize a new boolean array 'cur' for the current row.
        cur = [False] * (totSum + 1)
        cur[0] = True  # An empty subset can always achieve a sum of 0.

        # Fill in the 'cur' array using dynamic programming.
        for target in range(1, totSum + 1):
            # If the current element is not taken, the result is the same as the previous row.
            notTaken = prev[target]

            # If the current element is taken, subtract its value from the target and check the previous row.
            taken = prev[target - arr[ind]] if arr[ind] <= target else False

            # Update the 'cur' array with the result of taking or not taking the current element.
            cur[target] = notTaken or taken

        # Update 'prev' to 'cur' for the next iteration.
        prev = cur

    # Initialize a variable to track the minimum absolute difference.
    mini = int(1e9)

    # Iterate through all possible sums.
    for i in range(totSum + 1):
        if prev[i]:
            # Calculate the difference between the current sum and the complement sum.
            diff = abs(i - (totSum - i))
            mini = min(mini, diff)

    return mini

def main():
    arr = [1, 2, 3, 4]
    n = len(arr)
    
    # Find and print the minimum absolute difference between two subsets.
    print("The minimum absolute difference is:", minSubsetSumDifference(arr, n))

if __name__ == "__main__":
    main()



# 4 TODO : count subsets with sum K (DP-17)
# method 1 : brute force approch
Time Complexity: O(N*K)

Reason: There are N*K states therefore at max ‘N*K’ new problems will be solved.

Space Complexity: O(N*K) + O(N)

Reason: We are using a recursion stack space(O(N)) and a 2D array ( O(N*K)).

def findWays(num, k):
    n = len(num)
    
    # Initialize a 2D DP array to store the count of subsets for different targets.
    dp = [[0] * (k + 1) for _ in range(n)]
    
    # Base case: There is always one way to make a subset with a target sum of 0 (empty subset).
    for i in range(n):
        dp[i][0] = 1
    
    # Handle the base case for the first element in the array.
    if num[0] <= k:
        dp[0][num[0]] = 1

    # Iterate through the elements in the array.
    for ind in range(1, n):
        for target in range(1, k + 1):
            # If the current element is not taken, the count is the same as the previous row.
            notTaken = dp[ind - 1][target]
            
            # If the current element is taken, subtract its value from the target and check the previous row.
            taken = 0
            if num[ind] <= target:
                taken = dp[ind - 1][target - num[ind]]
            
            # Update the DP array with the total count of ways (taken + notTaken).
            dp[ind][target] = notTaken + taken

    # The result is stored in the bottom-right cell of the DP array.
    return dp[n - 1][k]

def main():
    arr = [1, 2, 2, 3]
    k = 3
    
    # Find and print the number of subsets that can be formed with a sum of 'k'.
    print("The number of subsets found are", findWays(arr, k))

if __name__ == "__main__":
    main()




# method 2 : better approch
Time Complexity: O(N*K)

Reason: There are two nested loops

Space Complexity: O(N*K)

Reason: We are using an external array of size ‘N*K’. Stack Space is eliminated.

def findWays(num, k):
    n = len(num)
    
    # Initialize a 2D DP array to store the count of subsets for different targets.
    dp = [[0] * (k + 1) for _ in range(n)]
    
    # Base case: There is always one way to make a subset with a target sum of 0 (empty subset).
    for i in range(n):
        dp[i][0] = 1
    
    # Handle the base case for the first element in the array.
    if num[0] <= k:
        dp[0][num[0]] = 1

    # Iterate through the elements in the array.
    for ind in range(1, n):
        for target in range(1, k + 1):
            # If the current element is not taken, the count is the same as the previous row.
            notTaken = dp[ind - 1][target]
            
            # If the current element is taken, subtract its value from the target and check the previous row.
            taken = 0
            if num[ind] <= target:
                taken = dp[ind - 1][target - num[ind]]
            
            # Update the DP array with the total count of ways (taken + notTaken).
            dp[ind][target] = notTaken + taken

    # The result is stored in the bottom-right cell of the DP array.
    return dp[n - 1][k]

def main():
    arr = [1, 2, 2, 3]
    k = 3
    
    # Find and print the number of subsets that can be formed with a sum of 'k'.
    print("The number of subsets found are", findWays(arr, k))

if __name__ == "__main__":
    main()




# method 3 : optimal solution
Time Complexity: O(N*K)

Reason: There are two nested loops

Space Complexity: O(K)

Reason: We are using an external array of size ‘K+1’ to store only one row.

def findWays(num, k):
    n = len(num)

    # Initialize a list 'prev' to store the count of subsets for different targets.
    prev = [0 for i in range(k + 1)]
    
    # Base case: There is always one way to make a subset with a target sum of 0 (empty subset).
    prev[0] = 1
    
    # Handle the base case for the first element in the array.
    if num[0] <= k:
        prev[num[0]] = 1
    
    # Iterate through the elements in the array.
    for ind in range(1, n):
        # Initialize a new list 'cur' to store the count for the current row.
        cur = [0 for i in range(k + 1)]
        cur[0] = 1
        
        for target in range(1, k + 1):
            # If the current element is not taken, the count is the same as the previous row.
            notTaken = prev[target]
    
            # If the current element is taken, subtract its value from the target and check the previous row.
            taken = 0
            if num[ind] <= target:
                taken = prev[target - num[ind]]
        
            # Update the 'cur' list with the total count of ways (taken + notTaken).
            cur[target] = notTaken + taken
        
        # Update 'prev' to 'cur' for the next iteration.
        prev = cur
    
    # The result is stored in 'prev[k]', indicating the count of subsets that can be formed with a sum of 'k'.
    return prev[k]

def main():
    arr = [1, 2, 2, 3]
    k = 3
    
    # Find and print the number of subsets that can be formed with a sum of 'k'.
    print("The number of subsets found are", findWays(arr, k))

if __name__ == "__main__":
    main()

  


# 5 TODO : count partitions with given difference (DP-18)
# method 1 : brute force approch
Time Complexity: O(N*K)

Reason: There are N*K states therefore at max ‘N*K’ new problems will be solved.

Space Complexity: O(N*K) + O(N)

Reason: We are using a recursion stack space(O(N)) and a 2D array ( O(N*K)).
mod = int(1e9 + 7)

def countPartitionsUtil(ind, target, arr, dp):
    if ind == 0:
        if target == 0 and arr[0] == 0:
            return 2
        if target == 0 or target == arr[0]:
            return 1
        return 0
    
    if dp[ind][target] != -1:
        return dp[ind][target]
        
    notTaken = countPartitionsUtil(ind-1, target, arr, dp)
    
    taken = 0
    if arr[ind] <= target:
        taken = countPartitionsUtil(ind-1, target-arr[ind], arr, dp)
        
    dp[ind][target] = (notTaken + taken) % mod
    return dp[ind][target]

def countPartitions(d, arr):
    n = len(arr)
    totSum = sum(arr)
    
    # Checking for edge cases
    if totSum - d < 0:
        return 0
    if (totSum - d) % 2 == 1:
        return 0
    
    s2 = (totSum - d) // 2
    
    dp = [[-1 for j in range(s2 + 1)] for i in range(n)]
    return countPartitionsUtil(n-1, s2, arr, dp)

def main():
    arr = [5, 2, 6, 4]
    d = 3

    print("The number of subsets found are", countPartitions(d, arr))

if __name__ == "__main__":
    main() 


# method 2 : better approch
mod=int(1e9+7)
def findWays(num, tar):
    n = len(num)
    dp = [[0] * (tar + 1) for _ in range(n)]
    
    if num[0] == 0:
        dp[0][0] = 2 # 2 cases - pick and not pick
    else:
        dp[0][0] = 1 # 1 case - not pick
    
    if num[0] != 0 and num[0] <= tar:
        dp[0][num[0]] = 1 # 1 case - pick
    
    for ind in range(1, n):
        for target in range(tar + 1):
            notTaken = dp[ind - 1][target]
            taken = 0
            if num[ind] <= target:
                taken = dp[ind - 1][target - num[ind]]
        
            dp[ind][target] = (notTaken + taken) % mod
    return dp[n - 1][tar]

def countPartitions(n, d, arr):
    totSum = sum(arr)
    
    # Checking for edge cases
    if (totSum - d) < 0 or (totSum - d) % 2:
        return 0
    
    return findWays(arr, (totSum - d) // 2)

def main():
  arr = [5, 2, 6, 4]
  n = len(arr)
  d = 3
  print("The number of subsets found are", countPartitions(n, d, arr))
if __name__ == "__main__":
  main()  


# method 3 : optimal solution
Time Complexity: O(N*K)

Reason: There are three nested loops

Space Complexity: O(K)

Reason: We are using an external array of size ‘K+1’ to store only one row.
mod =int(1e9+7)

def findWays(num, tar):
    n = len(num)

    prev = [0] * (tar + 1)
    
    if num[0] == 0:
        prev[0] = 2  # 2 cases - pick and not pick
    else:
        prev[0] = 1  # 1 case - not pick
    
    if num[0] != 0 and num[0] <= tar:
        prev[num[0]] = 1  # 1 case - pick
    
    for ind in range(1, n):
        cur = [0] * (tar + 1)
        for target in range(tar + 1):
            notTaken = prev[target]
    
            taken = 0
            if num[ind] <= target:
                taken = prev[target - num[ind]]
        
            cur[target] = (notTaken + taken) % mod
        prev = cur
    return prev[tar]

def countPartitions(n, d, arr):
    totSum = 0
    for i in range(n):
        totSum += arr[i]
    
    # Checking for edge cases
    if totSum - d < 0 or (totSum - d) % 2:
        return 0
    
    return findWays(arr, (totSum - d) // 2)
  

def main():
    arr = [5, 2, 6, 4]
    n = len(arr)
    d = 3

    print("The number of subsets found are", countPartitions(n, d, arr))
if __name__ == '__main__':
  main()    


# 6 TODO : assign cookies
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 7 TODO : minimum coins (DP-20)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 8 TODO : target sum (DP-21)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 9 TODO : coin change 2 (DP-22)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 10 TODO :  unbounded knapsack (DP-23)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 11 TODO : red cutting problem (DP-24)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      



# endregion


# region 16.5 DP - STRINGS
# ------------------------

# 1 TODO :  longest common subsequence (DP-25)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 2 TODO : print longest common subsequence (DP-26)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 3 TODO : longest common substring (DP-27)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 4 TODO : longest pallindromic subsequence (DP-28)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 5 TODO : minimum insertions to make string pallindromic (DP-29)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 6 TODO : minimum insertions/deletions to convert string (DP-30)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 7 TODO : shortest common subsequence (DP-31)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 8 TODO : distinct subsequences (DP-32)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 9 TODO : edit distance (DP-33)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 10 TODO :  wildcard matching (DP-34)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      



# endregion


# region 16.6 DP - STOCKS
# -----------------------

# 1 TODO : best time to bus stocks - I (DP -35)  
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 2 TODO : buy and sell stock - II (DP - 36)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 3 TODO : buy and sell stock - III (DP-37)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 4 TODO : buy and sell stock - IV (DP-38)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 5 TODO : buy and sell stock with cooldown (DP-39)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 6 TODO : buy and sell stock with transaction fee (DP-40)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      




# endregion


# region 16.7 DP - LIS
# --------------------

# 1 TODO :  longest increasing subsequence (DP-41)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 2 TODO : printing longest increasing subsequence (DP-42)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 3 TODO : longest increasing subsequence (DP-43)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 4 TODO : largest divisible subset (DP-44)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 5 TODO : largest string chain (DP-45)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 6 TODO : longest bitonic subsequence (DP-46)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 7 TODO : number of longest increasing subsequence (DP-47)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      



# endregion



# region 16.8 DP - MCM/PARTITION
# ------------------------------

# 1 TODO :  bitonic chain multiplication (DP-48)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 2 TODO : matrix chain multiplication | Bottom up (DP-49)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 3 TODO : minimum cost to cut the stick (DP-50)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 4 TODO : burst balloons (DP-51)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 5 TODO : evaluate boolean expression to true (DP-52)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 6 TODO : pallindrome partioning - I (DP-53)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 7 TODO : partition array for maximumsum (DP-54)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# endregion



# region 16.9 DP - SQUARES
# ------------------------


# 1 TODO :  maximum rectangle area with all 1's (DP-55)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 2 TODO : count square submatrices with all ones (DP-56)
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      




# endregion


# region 17.1 TRIES - THEORY
# --------------------------

# 1 TODO :  implement trie | insert |search | startswith
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity:

Insertion: O(N) where N is the length of the word being inserted. This is because we have to iterate over each letter of the word to find its corresponding node or create a node accordingly.
Search: O(N) where N is the length of the word being searched for. This is because in Trie search we traverse over each letter for the word from the root, checking if the current node contains a node at the index of the next letter. This process repeats until we reach the end of the word or encounter a node without the next letter.
Prefix Search: O(N) where N is the length of the prefix being searched for. Similar to searching for words, in prefix search we also iterate over each letter of the word to find its corresponding node.
Space Complexity: O(N) where N is the total number of characters across all unique words inserted into the Trie. For each character in a word, a new node may need to be created leading to space proportional to the number of characters.
                            
class Node:
    def __init__(self):
        # Array to store links to child nodes,
        # each index represents a letter
        self.links = [None] * 26
        # Flag indicating if the node
        # marks the end of a word
        self.flag = False

    # Check if the node contains
    # a specific key (letter)
    def containsKey(self, ch):
        return self.links[ord(ch) - ord('a')] is not None

    # Insert a new node with a specific
    # key (letter) into the Trie
    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node

    # Get the node with a specific
    # key (letter) from the Trie
    def get(self, ch):
        return self.links[ord(ch) - ord('a')]

    # Set the current node
    # as the end of a word
    def setEnd(self):
        self.flag = True

    # Check if the current node
    # marks the end of a word
    def isEnd(self):
        return self.flag


class Trie:
    def __init__(self):
        # Constructor to initialize the
        # Trie with an empty root node
        self.root = Node()

    # Inserts a word into the Trie
    # Time Complexity O(len), where len
    # is the length of the word
    def insert(self, word):
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                # Create a new node for
                # the letter if not present
                node.put(ch, Node())
            # Move to the next node
            node = node.get(ch)
        # Mark the end of the word
        node.setEnd()

    # Returns if the word
    # is in the trie
    def search(self, word):
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                # If a letter is not found,
                # the word is not in the Trie
                return False
            # Move to the next node
            node = node.get(ch)
        # Check if the last node
        # marks the end of a word
        return node.isEnd()

    # Returns if there is any word in the
    # trie that starts with the given prefix
    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if not node.containsKey(ch):
                # If a letter is not found, there is
                # no word with the given prefix
                return False
            # Move to the next node
            node = node.get(ch)
        # The prefix is found in the Trie
        return True


if __name__ == "__main__":
    trie = Trie()
    print("Inserting words: Striver, Striving, String, Strike")
    trie.insert("striver")
    trie.insert("striving")
    trie.insert("string")
    trie.insert("strike")

    print("Search if Strawberry exists in trie: " +
          ("True" if trie.search("strawberry") else "False"))

    print("Search if Strike exists in trie: " +
          ("True" if trie.search("strike") else "False"))

    print("If words in Trie start with Stri: " +
          ("True" if trie.startsWith("stri") else "False"))
                           
                        



# endregion


# region 17.2 TRIES - PRACTICE PROBLEMS
# -------------------------------------

# 1 TODO :  implement trie -2 (prefix tree)
# method 1 : brute force approch
Time Complexity: O(N) where N is the length of the word or prefix being processed.

Each method (insertion, counting words equal to a given word, counting words starting with a prefix, and erasing a word) requires traversing the Trie for each character of the input word or prefix.
Therefore, the time complexity is linear with respect to the length of the word or prefix being processed.
Space Complexity: O(N) where N is the total characters across all words inserted into the Trie. The space complexity is proportional to the number of unique words inserted into the Trie and the average length of those words.
                            
class Node:
    """
    Define a class for each node in the trie.
    """

    def __init__(self):
        # Array to store links
        # to child nodes
        self.links = [None] * 26
        # Counter for number of words
        # that end at this node
        self.cntEndWith = 0
        # Counter for number of words that
        # have this node as a prefix
        self.cntPrefix = 0

    def contains_key(self, ch):
        """
        Function to check if the
        node contains a specific key.
        """
        # Check if the link corresponding
        # to the character exists
        return self.links[ord(ch) - ord('a')] is not None

    def get(self, ch):
        """
        Function to get the child node
        corresponding to a key.
        """
        # Return the link corresponding
        # to the character
        return self.links[ord(ch) - ord('a')]

    def put(self, ch, node):
        """
        Function to insert a child node
        with a specific key.
        """
        # Set the link corresponding to
        # the character to the provided node
        self.links[ord(ch) - ord('a')] = node

    def increase_end(self):
        """
        Function to increment the count
        of words that end at this node.
        """
        # Increment the counter
        self.cntEndWith += 1

    def increase_prefix(self):
        """
        Function to increment the count of
        words that have this node as a prefix.
        """
        # Increment the counter
        self.cntPrefix += 1

    def delete_end(self):
        """
        Function to decrement the count of
        words that end at this node.
        """
        # Decrement the counter
        self.cntEndWith -= 1

    def reduce_prefix(self):
        """
        Function to decrement the count of 
        words that have this node as a prefix.
        """
        # Decrement the counter
        self.cntPrefix -= 1


class Trie:
    """
    Define a class for the
    trie data structure.
    """

    def __init__(self):
        """
        Constructor to initialize the
        trie with an empty root node.
        """
        # Create a new root node
        self.root = Node()

    def insert(self, word):
        """
        Function to insert a
        word into the trie.
        """
        # Start from the root node
        node = self.root
        
        # Iterate over each
        # character in the word
        for ch in word:
            # If the character is not
            # already in the trie
            
            if not node.contains_key(ch):
            
                # Create a new node
                # for the character
                node.put(ch, Node())
           
            # Move to the child node
            # corresponding to the character
            
            node = node.get(ch)
            # Increment the prefix
            # count for the node
            node.increase_prefix()
        # Increment the end count
        # for the last node of the word
        node.increase_end()

    def count_words_equal_to(self, word):
        """
        Function to count the number
        of words equal to a given word.
        """
        # Start from the
        # root node
        node = self.root
        # Iterate over each
        # character in the word
        for ch in word:
            # If the character is
            # found in the trie
            if node.contains_key(ch):
                # Move to the child node
                # corresponding to the character
                node = node.get(ch)
            else:
                # Return 0 if the
                # character is not found
                return 0
        # Return the count of
        # words ending at the node
        return node.cntEndWith

    def count_words_starting_with(self, word):
        """
        Function to count the number of
        words starting with a given prefix.
        """
        # Start from the root node
        node = self.root
        # Iterate over each
        # character in the prefix
        for ch in word:
            # If the character is
            # found in the trie
            if node.contains_key(ch):
                # Move to the child node
                # corresponding to the character
                node = node.get(ch)
            else:
                # Return 0 if the
                # character is not found
                return 0
        # Return the count of
        # words with the prefix
        return node.cntPrefix

    def erase(self, word):
        """
        Function to erase
        a word from the trie.
        """
        # Start from the root node
        node = self.root
        # Iterate over each
        # character in the word
        for ch in word:
            # If the character is
            # found in the trie
            if node.contains_key(ch):
                # Move to the child node
                # corresponding to the character
                node = node.get(ch)
                # Decrement the prefix
                # count for the node
                node.reduce_prefix()
            else:
                # Return if the
                # character is not found
                return
        # Decrement the end count
        # for the last node of the word
        node.delete_end()


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    trie.insert("app")
    print("Inserting strings 'apple', 'app' into Trie")
    print("Count Words Equal to 'apple':", trie.count_words_equal_to("apple"))
    print("Count Words Starting With 'app':", trie.count_words_starting_with("app"))
    print("Erasing word 'app' from trie")
    trie.erase("app")
    print("Count Words Equal to 'apple':", trie.count_words_equal_to("apple"))
    print("Count Words Starting With 'apple':", trie.count_words_starting_with("app"))
                           
                         


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 2 TODO : longest string with all prefixes
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 3 TODO : number of distinct substrings in a string
# method 1 : brute force approch
Time Complexity: O(N*N) where N is the number of characters in the given word. The implementation has two nested loops:

The outer loop iterates over each character of the string, leading to O(N) iterations.
The inner loop iterates over the remaining characters in the string for each character, also leading to O(N) iterations in the worst case.
Space Complexity : O(N*N)where N is the number of characters in the given word. The size of the set to store distinct substrings can grow up to O(N*N) in the worst case where all substrings are distinct. Each substring stored in the set occupies space proportional to its length, but the total space occupied by all substrings will limit to O(N*N).
                                
# Function to count all distinct
# substrings of a given string
def count_distinct_substrings(s):
    # Set to store
    # distinct substrings
    st = set()

    # Length of the
    # input string
    n = len(s)

    # Iterate over each
    # character in the string
    for i in range(n):
        # Initialize an empty string
        # to store the current substring
        substr = ""

        # Iterate over the remaining characters 
        # in the string starting from index i
        for j in range(i, n):
            # Append the current
            # character to the substring
            substr += s[j]

            # Insert the current
            # substring into the set
            st.add(substr)

    # Return the set containing
    # all distinct substrings
    return st

if __name__ == "__main__":
    s = "striver"
    print("Given String:", s)

    # Call the function to
    # count distinct substrings
    substrings = count_distinct_substrings(s)
    count = 0

    # Print the distinct substrings
    print("Distinct Substrings:")
    for substr in substrings:
        print(substr)
        count += 1

    # Count + 1 as we have to count
    # the empty string as well
    print("Number of distinct substrings:", count + 1)
                                




# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(N*N)where N is the length of the input string. This is because for each starting position of the substring, we traverse the entire substring once. However, due to the Trie structure, the actual number of comparisons is reduced as we progress.

Space Complexity : O(N*N) where N is the length of the input string. In the worst-case scenario, where there are no common prefixes among substrings the number of nodes could be as high as the total number of substrings which is bounded by O(N*N).
                                
                     
class Node:
    """
    Node structure representing
    each node in the trie
    """

    def __init__(self):
        self.links = [None] * 26  
        # Array of pointers to child nodes,
        # each corresponding to a letter
        # of the alphabet
        self.flag = False  
        # Flag indicating if the current
        # node represents the end of a substring

    def containsKey(self, ch):
        """
        Method to check if a specific character key
        exists in the children of the current node
        """
        # Check if the current node has a child node
        # corresponding to character 'ch'
        return self.links[ord(ch) - ord('a')] is not None

    def get(self, ch):
        """
        Method to get the child node corresponding
        to a specific character key
        """
        # Get the child node
        # corresponding to character 'ch'
        return self.links[ord(ch) - ord('a')]

    def put(self, ch, node):
        """
        Method to insert a new child
        node with a specific character key
        """
        # Insert a new child
        # node for character 'ch'
        self.links[ord(ch) - ord('a')] = node

    def setEnd(self):
        """
        Method to mark the current
        node as the end of a substring
        """
        # Mark the current node
        # as the end of a substring
        self.flag = True

    def isEnd(self):
        """
        Method to check if the current
        node marks the end of a substring
        """
        # Check if the current node
        # marks the end of a substring
        return self.flag


def countDistinctSubstrings(s):
    """
    Function to count the number of
    distinct substrings in the given string
    """
    root = Node()  
    # Creating the root
    # node of the trie
    cnt = 0  
    # Counter to keep track
    # of distinct substrings
    n = len(s)  
    # Length of the input string

    # Nested loops to iterate through all
    # possible substrings of the input string
    for i in range(n):  
        # Iterate through each
        # starting position of the substring
        node = root  
        # Start from the root for each substring
        for j in range(i, n):  
            # Iterate through each character of the substring
            # If the current character is not a child
            # of the current node, insert it as a new child node
            if not node.containsKey(s[j]):
                node.put(s[j], Node())  
                # Insert a new child
                # node for character s[j]
                cnt += 1  
                # Increment the counter
                # since a new substring is found
            node = node.get(s[j])  
            # Move to the child node
            # corresponding to character s[j]

    return cnt + 1  
    # Return the total count of distinct substrings
    # (+1 to account for the input string itself)


if __name__ == "__main__":
    s = "striver"  
    # Input string
    print("Current String:", s)
    print("Number of distinct substrings:", countDistinctSubstrings(s))  
    # Output the result
                                
                              


# 4 TODO : bit preRequisites for trie problems
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 5 TODO : maximum xor of two numbers in an array
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(32*N + 32*M) where N is the length of the input array.

Insertion: The time complexity of inserting each number into the Trie is O(32) as each number is composed of 32 bits in the Binary Representation. This operation is performed for each of the N numbers in the first array.
Finding Maximum XOR Operation: To find the maximum XOR value for each number, we iterate through its 32 bits performing constant-time operations for each bit. This is performed for all M numbers in the second array hence this operation accounts for the second time complexity of O(32*N).
Space Complexity: O(32N) where N is the length of the input array. This algorithm has a linear space complexity with respect to the size of the input array and each number takes up space proportional to 32 which is the size in Binary Representation.
                            
class Node:
    """Node structure for the Trie"""

    def __init__(self):
        # Array to store links
        # to child nodes (0 and 1)
        self.links = [None, None]

    def contains_key(self, bit):
        # Method to check if a specific
        # bit key is present in the child nodes
        # Returns True if the link at
        # index 'bit' is not None
        return self.links[bit] is not None

    def get(self, bit):
        # Method to get the child node
        # corresponding to a specific bit
        # Returns the child
        # node at index 'bit'
        return self.links[bit]

    def put(self, bit, node):
        # Method to set a child node at a
        # specific index in the links array
        # Sets the child node at index
        # 'bit' to the provided node
        self.links[bit] = node


class Trie:
    """Trie class"""

    def __init__(self):
        # Constructor to initialize
        # the Trie with a root node
        # Creates a new root
        # node for the Trie
        self.root = Node()

    def insert(self, num):
        # Method to insert a number into the Trie
        # Start from the root node
        node = self.root
        # Iterate through each bit of the
        # number (from left to right)
        for i in range(31, -1, -1):
            # Extract the i-th bit of the number
            bit = (num >> i) & 1

            # If the current node doesn't have a
            # child node with the current bit
            if not node.contains_key(bit):
                # Create a new child node
                # with the current bit
                node.put(bit, Node())

            # Move to the child node
            # corresponding to the current bit
            node = node.get(bit)

    def get_max(self, num):
        # Method to find the maximum
        # XOR value for a given number
        # Start from the root node
        node = self.root

        # Initialize the maximum XOR value
        max_num = 0

        # Iterate through each bit of
        # the number (from left to right)
        for i in range(31, -1, -1):
            # Extract the i-th
            # bit of the number
            bit = (num >> i) & 1

            # If the complement of the current
            # bit exists in the Trie
            if node.contains_key(1 - bit):
                # Update the maximum XOR
                # value with the current bit
                max_num |= (1 << i)

                # Move to the child node corresponding
                # to the complement of the current bit
                node = node.get(1 - bit)
            else:
                # Move to the child node
                # corresponding to the current bit
                node = node.get(bit)

        # Return the maximum XOR value
        return max_num


def max_xor(n, m, arr1, arr2):
    # Function to find the maximum XOR
    # value between two sets of numbers
    # Create a Trie object
    trie = Trie()
    # Insert each number from
    # the first set into the Trie
    for num in arr1:
        trie.insert(num)

    # Initialize the maximum XOR value
    maxi = 0

    # Iterate through each
    # number in the second set
    for num in arr2:
        # Update the maximum XOR value
        # with the result from the Trie
        maxi = max(maxi, trie.get_max(num))

    # Return the
    # maximum XOR value
    return maxi


def print_arr(arr):
    # Function to print the
    # Input Arrays
    for item in arr:
        print(item, end=" ")
    print()


if __name__ == "__main__":
    arr1 = [3, 10, 5, 25, 2]
    arr2 = [8, 1, 2, 12, 7]
    n = len(arr1)
    m = len(arr2)

    print("Arr1: ", end="")
    print_arr(arr1)
    print("Arr2: ", end="")
    print_arr(arr2)

    result = max_xor(n, m, arr1, arr2)
    print("Maximum XOR value:", result)
                           
                          


# 6 TODO : maximum xor with an element from array
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
Time Complexity: O(32*N + Q(logQ) + 32*Q) where N is the size of the input array and Q is the number of queries.

For each number in the input array, we traverse its bits from left to right (total of 32 bits). Since there are ‘N’ numbers in the array, the total time complexity is O(32*N).
Sorting the offline queries based on their endpoints requires O(Q log(Q) time using the inbuilt library for sorting.
For each query, we traverse the bits of the numbers in the Trie to find the maximum XOR value. Since each number has 32 bits and there are Q Queries, the total time complexity for processing is O(32*Q).
Space Complexity: O(32*N + Q) where N is the size of the input array and Q is the number of queries.

The space complexity of the Trie depends on the number of bits required to represent the numbers in the input array. Each number is represented as a sequence of 32 bits hence the space required by the Trie is O(32*N).
We store the queries and sort them based on the endpoint of each query. This requires an additional space complexity of O(Q).
                            
class Node:
    def __init__(self):
        # Array to hold links
        # to child nodes (0 and 1)
        self.links = [None, None]

    # Function to check if a child node
    # exists at a given index (0 or 1)
    def containsKey(self, ind):
        return self.links[ind] is not None

    # Function to get the child
    # node at a given index (0 or 1)
    def get(self, ind):
        return self.links[ind]

    # Function to set the child
    # node at a given index (0 or 1)
    def put(self, ind, node):
        self.links[ind] = node


class Trie:
    def __init__(self):
        # Pointer to the root
        # node of the trie
        self.root = Node()

    # Function to insert a
    # number into the trie
    def insert(self, num):
        # Start traversal
        # from the root node
        node = self.root

        # Traverse each bit of the number
        # from the most significant bit
        # to the least significant bit
        for i in range(31, -1, -1):
            # Extract the i-th
            # bit of the number
            bit = (num >> i) & 1

            # If the current node doesn't
            # have a child node at the
            # current bit, create one
            if not node.containsKey(bit):
                node.put(bit, Node())

            # Move to the child node
            # corresponding to the current bit
            node = node.get(bit)

    # Function to find the maximum XOR
    # value achievable with a given number
    def findMax(self, num):
        # Start traversal from the root node
        node = self.root

        # Initialize the maximum XOR value
        maxNum = 0

        # Traverse each bit of the number
        # from the most significant bit to
        # the least significant bit
        for i in range(31, -1, -1):
            # Extract the i-th
            # bit of the number
            bit = (num >> i) & 1

            # If there exists a different bit
            # in the trie at the current position,
            # choose it to maximize XOR
            if node.containsKey(not bit):
                # Set the corresponding
                # bit in the result
                maxNum |= (1 << i)
                # Move to the child node
                # with the different bit
                node = node.get(not bit)
            else:
                # Move to the child node
                # with the same bit
                node = node.get(bit)

        # Return the maximum XOR value
        return maxNum


# Function to perform offline
# maximum XOR queries
def maxXorQueries(arr, queries):
    # Initialize list to
    # store results of queries
    ans = [0] * len(queries)

    # Vector to store offline queries
    offlineQueries = []

    # Sort the array of numbers
    arr.sort()

    # Convert queries to offline
    # queries and store them in a list
    index = 0
    for query in queries:
        offlineQueries.append((query[1], (query[0], index)))
        index += 1

    # Sort offline queries
    # based on their end points
    offlineQueries.sort()

    # Pointer to iterate through
    # the array of numbers
    i = 0

    # Number of elements in the array
    n = len(arr)

    # Create an instance of
    # the Trie data structure
    trie = Trie()

    # Process each offline query
    for end, (start, queryIndex) in offlineQueries:
        # Insert numbers into the trie
        # until the current query's end point
        while i < n and arr[i] <= end:
            trie.insert(arr[i])
            i += 1

        # If there are numbers inserted
        # into the trie, find the maximum
        # XOR value for the query range
        if i != 0:
            ans[queryIndex] = trie.findMax(start)
        else:
            # If no numbers inserted,
            # set result to -1
            ans[queryIndex] = -1

    # Return the results
    # of all queries
    return ans


if __name__ == "__main__":
    arr = [3, 10, 5, 25, 2, 8]
    print("Given Array:", arr)
    queries = [[0, 1], [1, 2], [0, 3], [3, 3]]
    print("Queries:", queries)

    result = maxXorQueries(arr, queries)

    print("Result of Max XOR Queries:")
    for i, res in enumerate(result):
        print(f"Query {i+1}: {res}")

                           
                              




# endregion


# region 18.1 STRINGS - HARD
# --------------------------

# 1 TODO :  minimum number of brackets reversals neededto make an expression balanced
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 2 TODO : count and say
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 3 TODO : hashing in strings | theory
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 4 TODO : rabin karp
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 5 TODO : 2-function
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 6 TODO : KMP algo/LSP(pl) array
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 7 TODO : shortest pallindrome
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 8 TODO : longest happy prefix
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# 9 TODO : count pallindromic subsequence in given string
# method 1 : brute force approch
# TC     -      
# SC     -     


# method 2 : better approch
# TC     -      
# SC     -     


# method 3 : optimal solution
# TC     -      
# SC     -      


# endregion

