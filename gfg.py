# def checkOddEven(x):
#     # code here
#     if x % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# ch = checkOddEven(5)
# print(ch)

# def pos(n):
#     ## Write the code
#     if n < 0:
#         return neg(n)
#     if n == 0:
#         return "already zero"
#     s = ""    
#     for i in range(1,n+1):
#         s += str(n - i) + " "
#     print(s.strip())
    
# def neg(n):
#     ##Write the code
#     s = ""
#     for i in range(0,abs(n)+1):
#         s += str(n + i) + " "
#     print(s.strip()) 

# n = pos(-3)
# print(n)

# def fizzBuzz(number):
#     # Write your code here.
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#         return
#     elif number % 3 == 0:
#         print("Fizz")
#         return
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)
#         return

# f = fizzBuzz(7)
# print(f)    

# def printIncreasingPower(x):
#     #code here
#     # Loop to jump in powers of 2
#     if x == 1:
#         return 1
#     sq = 1
#     i = 1
#     while(sq < x):
#         #code here
#         print (i**2, end = " ")
#         i = i+1
#         sq = i*i
#     return
#         #code here  

# square = printIncreasingPower(10)
# print(square)



          

# class Solution:
#     def countTriangles(self, arr):
#         n = len(arr)
#         arr.sort()   # sort array first
#         count = 0

#         # Fix the third side one by one
#         for k in range(n-1, 1, -1):  # k = largest side index
#             i, j = 0, k-1
#             while i < j:
#                 if arr[i] + arr[j] > arr[k]:
#                     # all pairs from i..j-1 with j work
#                     count += (j - i)
#                     j -= 1
#                 else:
#                     i += 1
#         return count
# arr = [3,4,6,7]    
# sol = Solution()
# print(sol.countTriangles(arr) )
