# this is how to actually use array
# import array
# arr = array.array('i',[1])
# arr.append(5)
# print(arr)


# dict1 = {'a':1,'b':2,'c':3}
# dict2 = {'b':2,'a':1,'c':3}
# if dict1 == dict2:
#     print("true shit")

# tup = (1,2,3)
# tup2 = (1,3,2)
# if tup == tup2:
#     print("Tuple equal")
# else:
#     print("nope")    
# print(list(tup))

# lis1 = [1,2,3]
# lis2 = [1,3,2]
# if lis1 == lis2:
#     print("yeah")
# else:
#     print("nope")    

set1 = {1,2,3}
set2 = {1,3,2,3,2,3}
if set1 ==set2:
    print("true")
else:
    print("naah")

# for lists,tuple and strings order is required but
# not for sets and dictionaries they see the no.

age = int(input("Enter your age : "))
is_student = True

if age >= 18 and is_student:
    print("Eligible")
else:
    print("nope")    