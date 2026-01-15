def removeDuplicate(arr):
    arr.sort()

    seen=set()
    result=[]

    for i in arr:
        if i not in seen:
            seen.add(i)
            result.append(i)
    return result
arr=[3,1,2,1,3,4,2]
print(removeDuplicate(arr))
