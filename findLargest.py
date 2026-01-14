def findLargest(arr,n):
    max=arr[0]
    for i in range(1,n):
        if arr[i]>max:
            max=arr[i]
    return max
arr=[9,5,6,2,5,5]
n=len(arr)
print(findLargest(arr,n))        