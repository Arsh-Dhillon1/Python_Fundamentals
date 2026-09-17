def last_occurence(arr,target,index):
    if index == len(arr):
        return -1

    ans = last_occurence(arr,target,index+1)

    if ans!=-1:
        return ans

    if arr[index] == target:
        return index

    return -1

arr = [5, 7, 2, 9, 2]
target = 2

print(last_occurence(arr,target,0))