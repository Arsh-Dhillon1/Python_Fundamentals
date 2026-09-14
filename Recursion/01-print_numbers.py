# Here, I'll print the numbers from m till n
def print_numbers(n,m):
    if n == (m-1):
        return

    print(n)
    print_numbers(n-1,m)

print_numbers(5,1)