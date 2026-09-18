def generate(arr,current,used):
    if current == 2:
        print(current[:])
        return
    for i in range(len(arr)):
        current.append(arr[i])
        generate(arr,current,arr[i])
        current.pop()

arr = [1,2,3]
generate(arr,[],0)