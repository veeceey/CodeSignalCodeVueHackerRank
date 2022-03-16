"""
https://www.geeksforgeeks.org/minimum-number-of-swaps-required-to-sort-an-array-of-first-n-number/
For each index in arr[].
Check if the current element is in it’s right position or not.
Since the array contains distinct elements from 1 to N, we can simply compare the element with it’s index
in array to check if it is at its right position.
If current element is not at it’s right position then swap the element with the element which has occupied its place.
Else check for next index.
"""
def solve(arr):
    swaps=0
    for i in range(len(arr)):
        while arr[i]!=i+1:
            swaps+=1
            arr[arr[i]-1], arr[i] =  arr[i], arr[arr[i]-1]
        print(arr, "iteration", i)
    print("result below")
    print("swap count", swaps)
    return arr
arr = [2, 3, 4, 1, 5]
print(arr, "input")
print(solve(arr))
