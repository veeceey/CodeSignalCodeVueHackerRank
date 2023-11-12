"""
Call two arms equally strong if the heaviest weights they each are able to lift are equal.

For yourLeft = 10, yourRight = 15, friendsLeft = 15, and friendsRight = 10, the output should be
solution(yourLeft, yourRight, friendsLeft, friendsRight) = true;
For yourLeft = 15, yourRight = 10, friendsLeft = 15, and friendsRight = 10, the output should be
solution(yourLeft, yourRight, friendsLeft, friendsRight) = true;
For yourLeft = 15, yourRight = 10, friendsLeft = 15, and friendsRight = 9, the output should be
solution(yourLeft, yourRight, friendsLeft, friendsRight) = false.

"""

def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    you=[yourLeft, yourRight]
    friend=[friendsLeft, friendsRight]
    return min(you) == min(friend) and max(you)==max(friend)

