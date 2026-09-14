def is_sorted(arr,index):
    if index == 0:
        return True
    if arr[index]<arr[index-1]:
        return False

    return is_sorted(arr,index-1)

arr = [1,2,3,4,5,4]
n = len(arr)-1
print(is_sorted(arr,n))