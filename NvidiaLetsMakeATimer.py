import time
print("input your time in number of seconds")
secondsInput=int(input())
seconds=secondsInput%60
minutes=secondsInput//60
print("Ok, you want you a timer for", minutes, " minutes and ", seconds, " seconds ")
print("starting now")
for i in range(minutes, -1, -1):
    if i==minutes:
        for j in range(seconds, -1, -1):
            print(i, " minutes and ", j, "seconds left")
            time.sleep(1)
    else:
        for j in range(60, -1, -1):
            print(i, " minutes and ", j, "seconds left")
            time.sleep(1)
print("timer ended, thank you")
    ##80seconds 1 minute 20 seconds

