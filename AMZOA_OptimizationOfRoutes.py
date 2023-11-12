"""
There are 3 things to be known before attempting this problem:
maxTravelDist, it is an integer which represents the maximum operating travel distance of the given aircraft;
forwardRouteList, it is a list of pairs of integers where the first integer represents the unique identifier of a forward shipping route
and the second integer represents the amount of travel distance required by this shipping route;
returnRouteList, a list of pairs of integers where the first integer represents the unique identifer of a return shipping route
and the second integer represents the amount of travel distance required by this shipping route.
These three things will be given as an input to you. you need to return a list of pairs of integers representing the pairs of IDs of forward and also return the shipping routes
that optimally utilize the given aircraft. If no route is possible, return a list with empty pair.
Example 1:
Input:
maxTravelDist = 7000
forwardRouteList = [[1,2000],[2,4000],[3,6000]]
returnRouteList = [[1,2000]]
Output:[[2,1]]
Explanation:There are only three combinations [1,1],[2,1],and [3,1], which have a total of 4000, 6000, and 8000 miles, respectively. Since 6000 is the largest use that does not exceed 7000, [2,1] is the optimal pair.
"""
# def solution(maxTravelDist, forwardRouteList, returnRouteList):
#     maxdistance=0
#     result=[None,None]
#     for routeIDfwd, forwardRouteDistance in forwardRouteList:
#         for routIDbckwd, backwardRouteDistance in returnRouteList:
#             if forwardRouteDistance + backwardRouteDistance > maxdistance and forwardRouteDistance+backwardRouteDistance <=maxTravelDist:
#                 maxdistance=forwardRouteDistance+backwardRouteDistance
#                 # result.append([routeIDfwd, routIDbckwd])
#
#
# maxTravelDist = 7000
# forwardRouteList = [[1, 2000], [2, 4000], [3, 6000]]
# returnRouteList = [[1, 2000]]
# print(solution(maxTravelDist, forwardRouteList, returnRouteList))


class Solution:
    def optimalUtilization(self, a, b, target):
        maximum=float('-inf')
        result=[]
        for i in range(len(a)):
            for j in range(len(b)):
                temp=a[i][1]+b[j][1]
                if temp <= target and temp > maximum:
                    maximum = max(maximum, temp)
                    result=[]
                    result.append([a[i][0], b[j][0]])
                elif temp<=target and temp>=maximum:
                    maximum=max(maximum, temp)
                    result.append([a[i][0], b[j][0]])

        return result

target=7000
forwardRouteList=[[1, 2000], [2, 4000], [3, 6000]]
returnRouteList= [[1, 2000]]
solve=Solution()
print(solve.optimalUtilization(forwardRouteList, returnRouteList, target))