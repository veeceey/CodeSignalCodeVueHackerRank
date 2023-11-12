"""
Define a word as a sequence of consecutive English letters. Find the longest word from the given string.
"""
def solution(text):
    temp = ""
    for c in text:
        if ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z'):
            temp += c
        else:
            temp += " "
    print(temp)
    array = temp.split(" ")
    print(array)
    maxlength = 0
    for a in array:
        if a is not None or a:
            if len(a) > maxlength:
                maxlength = len(a)
                maxlement = a
    return maxlement


