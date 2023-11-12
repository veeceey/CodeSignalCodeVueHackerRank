"""
You are given an array of integers. On each move you are allowed to increase exactly one of its element by one.
Find the minimal number of moves required to obtain a strictly increasing sequence from the input.
"""


def solution(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    if count > 2:
        return False
    ##not allowed to swap more than once
    a.sort()
    b.sort()
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True




