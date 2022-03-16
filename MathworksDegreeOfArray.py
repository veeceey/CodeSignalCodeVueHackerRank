"""
https://leetcode.com/problems/degree-of-an-array/
Given a non-empty array of non-negative integers nums, the degree of this array is defined as
the maximum frequency of any one of its elements.
Your task is to find the smallest possible length of a (contiguous) subarray of nums,
that has the same degree as nums.
Input: nums = [1,2,2,3,1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
"""
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = {}
        maxfreq = 0
        indexeshm = {}
        for i, num in enumerate(nums):
            freq[num] = 1 + freq.get(num, 0)
            if freq[num] > maxfreq:
                maxfreq = freq[num]
            if nums[i] not in indexeshm:
                indexeshm[nums[i]] = [i]
            else:
                indexeshm[nums[i]].append(i)
        minlength = len(nums)
        for i, n in enumerate(nums):
            if freq[n] == maxfreq:
                length = indexeshm[n][-1] - indexeshm[n][0] + 1
                ##last index entered for nmber 0 first index entered
                if length < minlength:
                    minlength = length
                    # minlength=min(length, minlength)
                    # maxfreq=freq[n]
        return (minlength)




