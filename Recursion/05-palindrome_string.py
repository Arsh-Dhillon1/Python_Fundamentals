def check_palindrome(s,left,right):
    if left>right:
        return True

    if s[left] == s[right] and check_palindrome(s,left+1,right-1):
        return True

    return False


s = "nitinn"
print(check_palindrome(s,0,len(s)-1))