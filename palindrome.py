def isPalindrome(x: int) -> bool:
    if x < 0:
        return false
    
    stk = []
    n = []

    for i in str(x):
        stk.append(int(i)) 

    for i in stk[::-1]:
        n.append(i)    

    for i in stk:
        if n[i] != stk[i]:
            return False
    return True 
print(isPalindrome(121)) # type: ignore
# x = 124
# stk = []
# n = []
# ranj = len(str(x))
           