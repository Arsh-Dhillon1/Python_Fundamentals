import sys
sys.setrecursionlimit(3000)
def fibonnaci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonnaci(n-1) + fibonnaci(n-2)

n = int(input())
print(fibonnaci(n))