# s = "abc"
# for i in s:
#     print(s)

# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         # base case
#         if not p:
#             return not s

#         # check first character match (either same char or '.')
#         firstcase = bool(s) and (p[0] == s[0] or p[0] == '.')

#         # if next char is '*'
#         if len(p) >= 2 and p[1] == '*':
#             # 1. skip the "x*" (move p forward by 2)
#             # 2. OR if firstcase, consume one from s and try again
#             return (self.isMatch(s, p[2:])) or (firstcase and self.isMatch(s[1:], p))
#         else:
#             # otherwise, move forward one character in both
#             return firstcase and self.isMatch(s[1:], p[1:])

# from typing import List


# class Solution:
#     def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
#         new = []
#         lf = len(friends)
#         lo = len(order)
#         for i in range(lo):
#             for j in range(lf): 
#                 if order[i] == friends[j]:
#                     new.append(order[i])
#         return new           

# solve = Solution()
# print(solve.recoverOrder([3,1,2,5,4],[1,3,4]))

# class Solution:
#     def minDifference(self, n: int, k: int) -> list[int]:
#         result = set()
#         for i in range(1,int(n**0.5) + 1):
#             if n % i == 0:
#                 result.add(i)
#                 result.add(n // i)

# class soum:
#     def suom (self, n: int)->int:
#         sum = n + n + n
#         return sum
# s = soum()
# print(s.suom(0))
                
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        if num1 == 0:
            return 0
        for i in range(1,61):
            num1 = num1 - (2**i + num2)  
            if num1 <= 0:
                