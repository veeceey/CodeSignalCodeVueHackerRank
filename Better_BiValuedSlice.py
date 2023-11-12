class Solution:
    def helper(self, A):
        prev1=None
        prev2=None
        maxlength=float('-inf')
        length=0
        repcountSeen=0
        for current in A:
            if current==prev1 or current==prev2:
                length+=1
            else:
                ##we got a new number so we will have to shed the older number
                length=1 + repcountSeen
            if current==prev1:
                repcountSeen+=1
            else:
                repcountSeen=1
                prev2=prev1
                prev1=current
            maxlength=max(maxlength, length)
        return maxlength

A= [1, 2, 1, 2, 2, 3, 3, 2, 3]
solve=Solution()
print(solve.helper(A))
i
