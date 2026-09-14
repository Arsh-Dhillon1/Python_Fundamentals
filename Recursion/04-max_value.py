def max_value(arr,index):
    if index == 0:
        return arr[0]
    
    if arr[index]>max_value(arr,index-1):
        return arr[index]

    return max_value(arr,index-1)
    
# maxi = float('-inf')
arr = [2,1,3,15,0,1,2,10,-8]
print(max_value(arr,len(arr)-1))