# region Global Variables
rows = 5



# region PATTERN 1
'''
*****
*****
*****
*****
*****
'''
for i in range(rows):
    for j in range(rows):
        print("*", end="")
    print("\n")

# region PATTERN 2
'''
*
**
***
****
*****
'''
for i in range(rows):
    for j in range(i+1):
        print("*", end="")
    print("\n")

# region PATTERN 3
'''
1
12
123
1234
12345
'''
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j, end="")
    print("\n")

# region PATTERN 4
'''
1
22
333
4444
55555
'''
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(i, end="")
    print("\n")

# region PATTERN 5
'''
*****
****
***
**
*
'''
for i in range(rows):
    for j in range(rows-i):
        print("*", end="")
    print("\n")

# region PATTERN 6
'''
12345
1234
123
12
1
'''
for i in range(1,rows+1):
    for j in range(1,rows+1-i+1):
        print(j, end="")
    print("\n")

# region PATTERN 7
'''
    *    

   ***   

  *****  

 ******* 

*********
'''
for i in range(1,rows):
    for j in range(1,rows-i):
      print("_", end="")
        
    for j in range(2*i-1):
      print("*", end="")
        
    for j in range(1,rows-i):
      print("_", end="")
    print("\n")

# region PATTERN 8
'''
*********
 ******* 
  ***** 
   ***   
    *    
'''
for i in range(1,rows):
    for j in range(1,i):
      print(" ", end="")
        
    for j in range(2*rows-2*i-1):
      print("*", end="")
        
    for j in range(1,i):
      print(" ", end="")
    print("\n")


# region PATTERN 9
'''
    *    
   ***   
  *****  
 ******* 
*********
*********
 ******* 
  ***** 
   ***   
    *  
'''
for i in range(1,rows):
    for j in range(1,rows-i):
      print(" ", end="")
        
    for j in range(2*i-1):
      print("*", end="")
        
    for j in range(1,rows-i):
      print(" ", end="")
    print("\n")
    
for i in range(1,rows):
    for j in range(1,i):
      print(" ", end="")
        
    for j in range(2*rows-2*i-1):
      print("*", end="")
        
    for j in range(1,i):
      print(" ", end="")
    print("\n")


# region PATTERN 10
'''
*
**
***
****
*****
****
***
**
*
'''
for i in range(1,2*rows):
    row_number = i
    if i>rows:
      row_number = 2*rows-i
    for j in range(row_number):
      print("*", end="")
    print("\n")
    
# region PATTERN 11
'''
1
01
101
0101
10101
'''
for i in range(1,rows+1):
    start = 0
    if i%2: start = 1
    for j in range(i):
      print(start, end="")
      start = 1 - start             # 1-0 = 1 and 1-1 = 0, flipping the number
    print("\n")
    
# region PATTERN 12
'''
1      1
12    21
123  321
12344321
'''
for i in range(1,rows+1):
    for j in range(1,i+1):
      print(j, end="")
      
    for j in range(2*rows-2*i):
      print("_", end="")
      
    for j in range(i,0,-1):             # 4,3,2,1, reversing the count
      print(j, end="")
      
    print("\n")

# region PATTERN 13
'''
1 
2 3
4 5 6
7 8 9 10
11 12 13 14 15
ABCDE
'''
num = 1
for i in range(1, rows+1, 1):
    for j in range(i):
      print(num, end=" ")
      num = num + 1
    print("\n")
    
# region PATTERN 14
'''
A
AB
ABC
ABCD
ABCDE
'''
for i in range(rows+1):
    for j in range(i):
      print(chr(65+j), end="")
    print("\n")
    
    
# region PATTERN 15
'''
ABCDE
ABCD
ABC
AB
A
'''
for i in range(rows+1):
    for j in range(rows-i):
      print(chr(65+j), end="")
    print("\n")
    
# region PATTERN 16
'''
A
BB
CCC
DDDD
EEEEE
'''
for i in range(rows):
    for j in range(i+1):
      print(chr(65+i), end="")
    print("\n")

# region PATTERN 17
'''
   A
  ABA
 ABCBA
ABCDCBA
'''
for i in range(1,num + 1):
  for j in range(num-i):
    print("_", end="")
  for k in range(i):
    print(chr(65 + k), end="")
  for k in range(i-1,0,-1):
    print(chr(64+k), end="")
  for j in range(num-i):
    print("_", end="")
  print("\n")
    
# region PATTERN 18
'''
E
DE
CDE
BCDE
ABCDE
'''
for i in range(1,num+1):
  for j in range(i):
    print(chr(65+ (num - j -1)), end="")
  print("\n")

# region PATTERN 19
'''
**********
****  ****
***    ***
**      **
*         *
*         *
**       **
***    ***
****  ****
**********
'''
for i in range(num):
  for j in range(num-i):
    print("*", end="")
  for j in range(2*i):
    print("_", end="")
  for j in range(num-i):
    print("*", end="")
  print("\n")
  
for i in range(num):
  for j in range(i+1):
    print("*", end="")
  for j in range(2*(num - i-1)):
    print("_", end="")
  for j in range(i+1):
    print("*", end="")
  print("\n")

# region PATTERN 20
'''
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
'''
for i in range(1, 2*num):
  if i> ((2*num-1)//2):
    for j in range(2*num-i):
      print("*", end="")
    for j in range(2*(i-num)):
      print("_", end="")
    for j in range(2*num-i):
      print("*", end="")
    print("\n")
  else:
    for j in range(i):
      print("*", end="")
    for j in range(2*(num - i)):
      print("_", end="")
    for j in range(i):
      print("*", end="")
    print("\n")

# region PATTERN 21
'''
****
*  *
*  *
****
'''
for i in range(num):
    for j in range(num):
        if i == 0 or i == num-1 or j == 0 or j == num-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# region PATTERN 22
# 👉👉👉 https://www.youtube.com/watch?v=tNm_NNSB3_w&list=PLgUwDviBIf0oF6QL8m22w1hIDC1vJ_BHz&index=5
'''
4444444
4333334
4322234
4321234
4322234
4333334
4444444
'''
for i in range(2*n-1):
  for j in range(2*n-1):
    top = i 
    bottom = (2*n-2) -i 
    left = j
    right = (2*n-2) -j
    print(n - min(min(top, bottom), min(left, right)), end="")
  print("\n")

