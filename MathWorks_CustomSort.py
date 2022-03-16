"""
In an array, elements at any two indices can be swapped in a single operation called a move.
For example, if the array is arr = [17, 4, 8], swap arr[0] = 17 and arr[2] = 8 to get arr' =
[8, 4, 17] in a single move. Determine the minimum number of moves required to sort an array such
that all of the even elements are at the beginning of the array and all of the odd elements are at the end of the array.
"""

evenPointer=0
swapCount=0
array=[5, 7, 4, 9, 2, 3, 1]
for i in range(len(array)):
    if array[i]%2==0:
        if array[evenPointer]%2==1:
            swapCount+=1
        evenPointer+=1
print(swapCount)

# def solution(array):
#     evenPointer=0
#     oddPointer=len(array)-1
#     swapCount=0
#     while evenPointer<oddPointer:
#         while evenPointer<=oddPointer and array[evenPointer]%2==0:
#             evenPointer+=1
#         while evenPointer<=oddPointer and array[evenPointer]%2==1:
#             oddPointer-=1
#         if evenPointer==oddPointer:
#             break
#         array[evenPointer], array[oddPointer]=array[oddPointer], array[evenPointer]
#         swapCount+=1
#         evenPointer+=1
#         oddPointer-=1
#     return swapCount
# array=[1, 0, 1, 2, 3, 0, 2]
# print(solution(array))