"""Largest Square in Histogram"""
def area(arr):
    maxArea=0
    for i in range(len(arr)):
        minHeight=arr[i]
        for j in range(i, len(arr)):
            minHeight=min(minHeight, arr[j])
            minEdge=min(minHeight, j-i+1)
            maxArea=max(maxArea, minEdge**2)
    return maxArea
arr=[4,3,4]
print(area(arr))




"""
Largest Rectangle in Histogram
"""
# def area(arr):
#     maxArea=0
#     for i in range(len(arr)):
#         minHeight=arr[i]
#         for j in range(i, len(arr)):
#             minHeight=min(minHeight, arr[j])
#             maxArea=max(maxArea, minHeight*(j-i+1))
#     return maxArea
# arr=[4,3,4]
# print(area(arr))