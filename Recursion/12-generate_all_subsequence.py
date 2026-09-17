def subsequence(string, index, current):
    if index == len(string):
        print(current)
        return

    pick = subsequence(string,index+1,current+string[index])
    notpick = subsequence(string,index+1,current)


subsequence("abc",0,"")