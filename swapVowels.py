"""
Swap first position of vowel with next position of vowel
"""
def solve(string):
    temp=None
    hs=set(["a", "e", "i", "o", "u"])
    firstVowelIndex=None
    flag=False
    string=list(string)
    for i in range(len(string)):
        if temp is not None and string[i] in hs:
            var=string[i]
            string[i]=temp
            temp=var
        elif string[i] in hs:
            temp=string[i]
            if flag==False:
                firstVowelIndex=i
                flag=True
    string[firstVowelIndex]=temp
    return string
string="aeiou"
print(solve(string))
# output="vuran"