"""
Longest consecutive 0's

A binary gap within a positive integer N is any maximal
 sequence of consecutive zeros that is surrounded
  by ones at both ends in the binary representation of N
  For example, number 9 has binary representation 1001 and contains a binary gap of length 2.
  The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3.
"""
def solution(N):
    # write your code in Python 3.6
    number=bin(N)[2:]
    arr=str(number)
    # print(arr, "hello")
    maxcount=0
    for i in range(len(arr)):
        if arr[i]=="1":
            count=0
            for j in range(i+1, len(arr)):
                if arr[j]=="0":
                    count+=1
                    # print(count)
                else:
                    maxcount=max(count, maxcount)
                    break
                # print(maxcount)
    return maxcount