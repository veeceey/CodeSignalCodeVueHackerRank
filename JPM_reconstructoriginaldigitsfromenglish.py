"""
       Letter "z" is present only in "zero".
       Letter "w" is present only in "two".
       Letter "u" is present only in "four".
       Letter "x" is present only in "six".
       Letter "g" is present only in "eight"

"""

class Solution:
    def originalDigits(self, s: str) -> str:
        """
        Letter "z" is present only in "zero".
        Letter "w" is present only in "two".
        Letter "u" is present only in "four".
        Letter "x" is present only in "six".
        Letter "g" is present only in "eight".
        """
        freq = {}
        for c in s:
            freq[c] = 1 + freq.get(c, 0)
        print(freq)
        output = {}
        output["0"] = freq.get("z", 0)
        output["2"] = freq.get("w", 0)
        output["4"] = freq.get("u", 0)
        output["6"] = freq.get("x", 0)
        output["8"] = freq.get("g", 0)
        output["3"] = freq.get("h", 0) - output.get("8", 0)
        output["5"] = freq.get("f", 0) - output.get("4", 0)
        output["7"] = freq.get("s", 0) - output.get("6", 0)
        output["9"] = freq.get("i", 0) - output.get("5", 0) - output.get("6", 0) - output.get("8", 0)  ##i
        output["1"] = freq.get("n", 0) - output.get("7", 0) - 2 * output.get("9", 0)  ###n
        res = ""
        for digit in sorted(output.keys()):
            res += digit * output[digit]
        return res
s = "owoztneoer"
# Output: "012"









