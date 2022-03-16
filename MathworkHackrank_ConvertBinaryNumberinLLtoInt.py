class Solution:
    def getDecimalValue(self, head) -> int:
        number=head.val
        while head.next:
            number=number*2+head.next.val
            head=head.next
        return number

solve=Solution()