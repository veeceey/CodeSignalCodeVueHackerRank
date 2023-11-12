"""
Q : Given 2 Strings s1 & s2, check if s1 can be derived from s2 by deleting one or more characers in s2 without changing the order of s2.
Eg: c s2 = "asdfgh" => true, by deleting 'h' from s2.
s1 = "qwer" c => false, as s2.length() < s1.length()
s1 = "qwer" s2 = "dfgvfev" => false
"""

def editDistance(s1, s2):
    if len(s1)> len(s2):
        return False
    i,j=0,0
    s=""
    while i<len(s1) and j<len(s2):
        if s1[i]!=s2[j]:
            j+=1
        else:
            s+=s1[i]
            i+=1
            j+=1
    if s==s1:
        return True
    return False


print(editDistance(s1 = "qwer", s2 = "xyaqwxer"))
