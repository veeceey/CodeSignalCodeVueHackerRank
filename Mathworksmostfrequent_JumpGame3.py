from collections import deque
class Solution:
    ##Time On Space Ok
    def maxResult(self, nums:, k: int) -> int:
        n = len(nums)
        score = nums[0]
        q = deque()
        q.append((0, score))
        for i in range(1, n):
            while q and q[0][0] < i - k:
                q.popleft()
            ### 1 2 3 4 5 index 4 with element 5 and k =2 we dont need 1 and 2
            ##not needed elements popped
            score = q[0][1] + nums[i]
            while q and q[-1][1] < score:
                q.pop()
            q.append((i, score))
        return score

nums=[1,-1,-2,4,-7,3]
k=2