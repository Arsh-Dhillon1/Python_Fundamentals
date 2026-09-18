def permutations(arr,current,used,target):
    if len(current) == len(arr):
        ans = sum(current)
        if ans == target:
            print(current[:])
        return

    for i in range(len(arr)):
        if not used[i]:
            current.append(arr[i])
            used[i] = True
            permutations(arr,current,used,target)
            current.pop()
            used[i] = False

arr = [1,2,3]
target = int(input())
permutations(arr,[],[False]*len(arr),target)