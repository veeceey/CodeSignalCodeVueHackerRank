"""
https://app.codesignal.com/arcade/intro/level-5/veW5xJednTy4qcjso/solutions
All numbers should be present without leading zeros.
17.233.00.131 and 17.233.01.131 are not valid IPv4 addresses because they contain leading zeros
"""
def solution(inputString):
    array=inputString.split(".")
    if len(array)!=4:
        return False
    for c in array:
        if len(c)>3:
            return False
        if not c or c is None:
            return False
        elif not c.isnumeric():
            return False
        elif int(c)>255 or int(c)<0 :
            return False
        elif c[0]=="0" and len(c)>1:
            return False
    return True

