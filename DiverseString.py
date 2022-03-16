def solution(heights):
    maxArea = 0
    stack = []  ## index, height
    for i, currheight in enumerate(heights):
        start = i  ##we don't know if we can extend it backwards just yet.
        while stack and stack[-1][1] > currheight:
            index, greaterHeight = stack.pop()
            if not stack:
                width=index
            else:
                width=i-index-1
            squarEdge=min(width, heights[index])
            maxArea=max(maxArea,squarEdge*squarEdge)
            start = index
        stack.append((start, currheight))

    for index, height in stack:
        ##they were extended all the way to the end
        maxArea = max(maxArea, height * (len(heights) - index))
    return maxArea

heights = [100]
print(solution(heights))
#     maxArea = 0;
#     for i in range(len(heights)):
#         minH = heights[i];
#         for j in range(i+1, len(heights)):
#             minH=min(minH, heights[j])
#             maxArea=max(maxArea, minH*(j-i))
#     return maxArea



# def solution(n, d, p, ids, positions, queries):
#     hm = {}
#     for identity, position in zip(ids, positions):
#         hm[identity] = position
#     # print(hm)
#     for query in queries:
#         e1 = query[0]
#         e2 = query[1]
#         position1 = hm[e1]
#         position2 = hm[e2]
#         if abs(position2 - position1) <= d:
#             print("Yes")
#     print("No")
#
#
#
# n= 10
# d= 3
# p= 50
# ids= [9, 10, 8, 6, 3, 5, 4, 7, 1, 2]
# positions= [19, 1, 4, 13, 9, 11, 1, 10, 35, 22]
# queries=[[10,9],
#  [2,9],
#  [9,4],
#  [4,9],
#  [5,3],
#  [1,4],
#  [1,6],
#  [5,7],
#  [8,1],
#  [9,8],
#  [4,5],
#  [2,7],
#  [2,10],
#  [4,9],
#  [8,6],
#  [4,2],
#  [8,7],
#  [10,8],
#  [8,5],
#  [8,4],
#  [2,1],
#  [7,2],
#  [3,1],
#  [6,5],
#  [10,7],
#  [9,10],
#  [8,7],
#  [3,7],
#  [3,1],
#  [2,1],
#  [8,2],
#  [2,4],
#  [7,3],
#  [5,1],
#  [9,5],
#  [6,7],
#  [1,3],
#  [2,9],
#  [9,10],
#  [6,3],
#  [4,8],
#  [3,5],
#  [9,8],
#  [4,1],
#  [3,4],
#  [5,10],
#  [3,6],
#  [4,2],
#  [1,8],
#  [3,2]]
# solution(n, d, p, ids, positions, queries)