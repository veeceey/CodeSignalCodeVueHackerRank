"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them,
We repeatedly make k duplicate removals on s until we no longer can.
Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.
Input: s = "abcd", k = 2
Output: "abcd"
"""

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[]
        for c in s:
            if stack and stack[-1][0]==c:
                stack[-1][1]+=1
                if stack[-1][1]==k:
                    stack.pop()
            else:
                stack.append([c, 1])
        return "".join(element*count for element, count in stack)