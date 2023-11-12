"""
https://app.codesignal.com/arcade/intro/level-4/ZCD7NQnED724bJtjN/solutions
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

picture = ["abc",
           "ded"]
"""
def solution(picture):
    rows = len(picture)
    cols = len(picture[0])
    resRows = rows + 2
    resCols = cols + 2
    result = [None] * resRows
    for i in range(resRows):
        if i == 0 or i == resRows - 1:
            result[i] = "*" * resCols
        else:
            result[i] = "*" + picture[i - 1] + "*"
    return result

