class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        maxlength = 0
        globalmax = 1
        for i in range(len(s)):
            hs = set()
            for j in range(i, len(s)):
                if s[j] in hs:
                    print(s[j], "sj ")
                    length = j - i
                    print(j, i, "j, i")
                    maxlength = max(maxlength, length)
                    break
                else:
                    length = j - i
                    hs.add(s[j])
                    maxlength = max(maxlength, length + 1)
            globalmax = max(globalmax, maxlength)
        return globalmax

s = "abcabcbb"
#3