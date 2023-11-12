# def helper(y):
#     ##y-$
#     z=y*2
#     if z==12:
#         print("Fail")
#     else:
#         print("Pass")
#     return 0
# print(helper(6))
#

"""
What if we have to test the posible values of a and b for which a*b = 12
a*b=12, lets get the possible values of and b 
Concrete non concrete values
"""
def helper(number):
    hs=set()
    for i in range(1, number//2):
        for j in range(number, 1, -1):
            if i*j==number:
                hs.add((i,j))
    return hs
print(helper(123123112321))


for i in range(len(arr)):

    

"""
All good untill now what if we deal with recursion 
"""



