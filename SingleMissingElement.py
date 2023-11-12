"""
An array A consisting of N different integers is given.
The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.
"""
arr=[1,2,3]
n=len(arr)
hs=set(arr)
for i in range(1, n+2):
    if i not in hs:
        print (i)