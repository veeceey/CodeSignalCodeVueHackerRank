"""
https://leetcode.com/problems/lonely-pixel-i/
Given an m x n picture consisting of black 'B' and white 'W' pixels, return the number of black lonely pixels.

A black lonely pixel is a character 'B' that located at a specific position where the same row and same column don't have any other black pixels.
Input: picture = [["W","W","B"],["W","B","W"],["B","W","W"]]
Output: 3
Explanation: All the three 'B's are black lonely pixels.
"""


class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        ##if found i will go on diagonal
        ##if not found i will go both on right and down
        hmrows = {}
        hmcols = {}
        rows = len(picture)
        cols = len(picture[0])
        visitedIndices = []
        count = 0
        for i in range(rows):
            for j in range(cols):
                if picture[i][j] == 'B':
                    hmrows[i] = 1 + hmrows.get(i, 0)
                    hmcols[j] = 1 + hmcols.get(j, 0)
                    visitedIndices.append((i, j))
        for row, col in visitedIndices:
            if hmrows[row] == 1 and hmcols[col] == 1:
                count += 1
        return count





