"""
Maximum Value by deleting only one digit(5)
"""
def solve(n):
    maxvalue=float('-inf')
    string=str(n)
    for i in range(len(string)):
        if string[i]=="5":
           newstring=string[:i]+string[i+1:]
           integerNewString=int(newstring)
           print(integerNewString, "newdeletedString")
           maxvalue=max(integerNewString, maxvalue)
    return maxvalue
n=-50
print(solve(n))
