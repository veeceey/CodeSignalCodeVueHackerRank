class Solution:
    ##consider this as a custom sort just like
    def helper(self, array):
        n=len(array)
        low=0
        high=n-1
        ###pallindrome check ##varun chawla
        while low<high:
            while low<high and array[low]%2==0:
                low+=1
            while low<high and array[high]%2!=0:
                high-=1
            if low<high:
                array[low], array[high]=array[high], array[low]
                low+=1
                high-=1
        return array

array=[1,4,2,5,6,8,7,9,11, 12]
##pehle even phir odd order doesnt matter
solve=Solution()
print(solve.helper(array))