def merge_sort(arr):
    if len(arr)<=1:
        return arr

    mid = len(arr)//2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge_arrays(left,right)


def merge_arrays(left,right):
    arr = []
    if not left and right:
        return right
    if not right and left:
        return left

    i = 0
    j = 0

    while(i<len(left) and j<len(right)):
        if left[i]<=right[j]:
            arr.append(left[i])
            i+=1
        else:
            arr.append(right[j])
            j+=1

    while(i<len(left)):
            arr.append(left[i])
            i+=1

    while(j<len(right)):
            arr.append(right[j])
            j+=1

    return arr





arr = [42, -7, 893, 0, 15, -99, 3.14, 10002, 55, -4, 19, 7856, -332, 1, 88]
print(merge_sort(arr))