"""
https://app.codesignal.com/arcade/intro/level-12/ywMyCTspqGXPWRZx5/solutions
"""
def solution(time):
    newtime = time.split(":")
    if len(newtime) != 2:
        return False
    hour = newtime[0]
    minute = newtime[1]
    # print(hour, minute)
    if len(hour) != 2 or len(minute) != 2:
        return False
    if int(hour) > 23 or int(hour) < 0:
        return False
    if int(minute) > 59 or int(minute) < 0:
        return False
    return True


print(solution("23:59"))
