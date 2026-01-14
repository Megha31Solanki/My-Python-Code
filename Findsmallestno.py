def findSmallest(arr,n):
    min =arr[0]
    for i in range(1,n):
        if arr[i]<min:
            min=arr[i]
    return min
arr=[2,5,1,3,0]
n=len(arr)
print(findSmallest(arr,n))
        