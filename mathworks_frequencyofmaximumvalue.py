"""
Frequency of Maximum Value HackerRank
Given an array ‘nums’ of length N containing positive integers and an array ‘query’ of length
‘Q’ containing indexes, print/store
 for each query the count of maximum value in the sub-array starting at index ‘i’ and ending at index ‘N-1’

"""
def solve(nums, query):
    n=len(query)
    result=[None]*len(query)
    for i in range(len(query)):
        currIndex=query[i]
        maxvalue=float('-inf')
        count=0
        for j in range(currIndex, n):
            if nums[j]>maxvalue:
                maxvalue=nums[j]
                count=1
            elif nums[j]==maxvalue:
                count+=1
        result[i]=count
    return result
nums = [ 5, 4, 5, 3, 2 ]
query = [ 1, 2, 3, 4, 5 ]
print(solve(nums, query))