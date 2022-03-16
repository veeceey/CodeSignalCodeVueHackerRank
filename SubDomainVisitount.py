"""
https://leetcode.com/problems/subdomain-visit-count
Input: cpdomains = ["9001 discuss.leetcode.com"]
Output: ["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"]
Explanation: We only have one website domain: "discuss.leetcode.com".
As discussed above, the subdomain "leetcode.com" and "com" will also be visited. So they will all be visited 9001 times.
"""

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        output = []
        hm = {}
        for domains in cpdomains:
            s = domains.split(" ")
            stack = s[1].split(".")
            res = ""
            for i in range(len(stack) - 1, -1, -1):
                res = stack.pop() + "." + res if res else stack.pop() + res
                if res not in hm:
                    hm[res] = int(s[0])
                else:
                    newcount = hm[res] + int(s[0])
                    hm[res] = newcount
        for domain, freq in hm.items():
            output.append(str(freq) + " " + domain)
        return output

