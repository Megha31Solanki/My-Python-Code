def find_non_repeating(arr):
    freq = {}
    result = []

    for i in arr:
        freq[i] = freq.get(i, 0) + 1

    for i in arr:
        if freq[i] == 1:
            result.append(i)

    return result

arr = [1, 2, 3, 2, 4, 5, 1]
print(find_non_repeating(arr))
