count = 0

def count_occurence(arr,target,index):
    global count
    if index == 0:
        if arr[index] == target:
            count+=1
        return 
    if arr[index] == target:
        count+=1

    count_occurence(arr,target,index-1)


def count_occurences(arr,target,index):
    if index<0:
        return 0
    match = 0
    if arr[index] == target: 
        match = 1


    return match+count_occurences(arr,target,index-1)

arr = [2, 5, 2, 7, 2, 9]
target = 2
print(count_occurences(arr,target,len(arr)-1))
count_occurence(arr,target,len(arr)-1)
print(count)


