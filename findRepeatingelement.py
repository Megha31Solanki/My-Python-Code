def find_repeating(arr):
    freq={}
    repeating=[]

    for i in arr:
        freq[i]=freq.get(i,0)+1

    for key in freq:
        if freq[key]>1:
            repeating.append(key)
    return repeating
arr=[1,2,3,2,4,5,1,3]
print(find_repeating(arr))            