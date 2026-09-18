def permutations(string, current, used):
    if len(current) == len(string):
        new_string = "".join(current)
        print(new_string)
        return

    for i in range(len(string)):
        if not used[i]:
            current.append(string[i])
            used[i] = True
            permutations(string,current,used)
            current.pop()
            used[i] = False

s = "ABC"
permutations(s,[],[False]*len(s))