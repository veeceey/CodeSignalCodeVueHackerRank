"""
count the number of elements in an array a which are absolute distinct, what it means is if an array had
 -3 and 3 in it these numbers are not distinct because|-3|=|3|. i think an example would clear it up better
a={-5,-3,0,1,3}
"""

def solve(a):
    seta=set(a)
    return len(seta)
a=[-5,-3,0,1,-3]
print(solve(a))

def solution(N):

  list_of_absolute_values = list(map(lambda x:abs(x), N))

  return len(set(list_of_absolute_values))