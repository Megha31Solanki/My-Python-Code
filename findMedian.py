def getMedian(arr,n):
    arr.sort()

    if n%2==0:
        ind1=(n//2)-1
        ind2=(n//2)

        return(arr[ind1] + arr[ind2] )/2
    else:
        return(arr[n//2])
arr=[4,7,1,2,5,6]
n=6
print(getMedian(arr,n))            