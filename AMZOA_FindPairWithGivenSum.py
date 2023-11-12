"""You are on a flight and wanna watch two movies during this flight.
You are given List<Integer> movieDurations which includes all the movie durations.
You are also given the duration of the flight which is d in minutes.
Now, you need to pick two movies and the total duration of the two movies is exactly 30 minutes before filght ends (d - 30min).


You will pick exactly 2 songs. you cannot pick the same song twice. if you have multiple pais with the same total time,
select the pair with the longest song. there are atleast 2 songs available. write an alorithm to return ID's of the 2 songs whose combined runtime will finish
exactly 30 seconds before the bus arrives, keeping the original order. If no such pair is possible, return a pair with <-1,-1>.
input: rideDuration = 90 songDuration = {1,10,25,35,60}
output: [2,3]


"""

##if they say song combination exactly should end exactly 30 minutes before the ride duration then do this
def findsongspair(array, d):
    hm={}
    d-=30
    maximum=float('-inf')
    answer=[-1, -1]
    for i in range(len(array)):
        if d-array[i] in hm:
            if d-array[i]> maximum or array[i]>maximum:
                answer[0]=hm[d-array[i]]
                answer[1]=i
                maximum=max(d-array[i], array[i])
        else:
            hm[array[i]]=i
    return answer
movieDurations =[50, 20, 10, 40, 25, 30]
d = 90
print(findsongspair(movieDurations, d))


### if they say song combination should end <=30 minutes before the rideDuraction
def findsongspair(array, d):
    target=d-30
    ans = []
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] < target:
                ans = [array[i], array[j]]
    return ans

movieDurations =[50, 20, 10, 40, 25, 30]
d = 90
print(findsongspair(movieDurations, d))
