def generate(arr,current,used):
    if len(current) == len(arr):
        print(current[:])
        return

    for i in range(len(arr)):
        if not used[i]:
            current.append(arr[i])
            used[i] = True
            generate(arr,current,used)
            current.pop()
            used[i] = False

arr = [1,2,3]
generate(arr,[],[False]*len(arr))
