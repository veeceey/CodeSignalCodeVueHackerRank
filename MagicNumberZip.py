def sol(arr):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==mid:
            return mid
        elif arr[mid]<mid:
            low=mid+1
        else:
            high=mid-1


arr=[-10, -1, 0, 3, 10, 11, 30, 50, 100]
sol(arr)


