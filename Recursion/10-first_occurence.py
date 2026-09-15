def first_occurence(arr,target,index):
    if index == len(arr)-1:
        return -1

    if target == arr[index]:
        return index

    return first_occurence(arr,target,index+1)

def first_occurences(arr,target,index):
    if index == 0:
        if arr[index] == target:
            return index
        return -1

    ans = first_occurences(arr,target,index-1)
    if ans != -1:
        return ans

    if arr[index] == target:
        return index

    return -1

arr = [5, 7, 2, 9, 2]
target = 2
print(first_occurence(arr,target,0))
print(first_occurences(arr,target,len(arr)-1))

