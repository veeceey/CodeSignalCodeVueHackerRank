"""
The 2nd question is similar to leetcode problem below except they ask you to remove the peak element in the array
and return an array that contains the peak elements in the order they are removed.
It was the second question of the test so it should be an easy level question not medium.
"""
class Solution:
    def findPeakElement(self, nums) -> int:
        low=0
        size=len(nums)
        high=size-1
        stack=[]
        while low<high:
            mid=(low+high)//2
            if nums[mid]>nums[mid+1]:
                high=mid
                stack.append(high)
            else:
                low=mid+1
        if stack[-1]!=size-1:
            stack.append(size-1)
        return stack

        # size=len(nums)
        # stack=[]
        # for i in range(size):
        #     if i==size-1 or nums[i]>nums[i+1]:
        #         stack.append(i)
        #         # return i
        # return stack

solve=Solution()
nums=[1,2,3,1]
print("input", nums)
print(solve.findPeakElement((nums)))