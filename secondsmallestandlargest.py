def secondSmallestLargest(arr):
    arr.sort()
    smallest=arr[1]
    largest=arr[-2]
    return smallest, largest

arr=[2,3,4,5,1,6,7]
small,large=secondSmallestLargest(arr)
print(small)
print(large)