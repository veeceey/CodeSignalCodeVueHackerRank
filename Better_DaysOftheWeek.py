def returnDay(day, k):
    days=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for i in range(len(days)):
        if days[i]==day:
            newDay=(i+k)%7
            return days[newDay]

    

day="Sat"
k=23
print(returnDay(day, k))




