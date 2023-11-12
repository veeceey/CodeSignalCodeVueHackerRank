def solution(inputString):
    stack = []
    inputString = list(inputString)
    for index, character in enumerate(inputString):
        if character == "(":
            stack.append(index)
        elif character == ")":
            startIndex = stack.pop()
            endIndex = index
            temp = inputString[startIndex + 1:endIndex]
            inputString[startIndex + 1:endIndex] = temp[::-1]
    res = ""
    for c in inputString:
        if c != "(" and c != ")":
            res += c
    return res
    # return result













