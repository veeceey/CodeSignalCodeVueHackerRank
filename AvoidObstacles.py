"""
AvoidObstacles
https://app.codesignal.com/arcade/intro/level-5/XC9Q2DhRRKQrfLhb5/solutions
"""


def solution(inputArray):
    for jump in range(2, max(inputArray) + 2):
        flag = True
        for i in range(len(inputArray)):
            if inputArray[i] % jump == 0:
                flag = False
                break
        if flag == True:
            return jump


