def power(n,p):
    if p == 1:
        return n
    if p == 0:
        return 1
    if p%2==0:
        return power(n,p//2) * power(n,p//2)
    else:
        return power(n,p//2) * power(n,(p//2)+1)


# Optimised Version
def power_optimized(n,p):
    if p == 1:
        return n
    if p == 0:
        return 1

    half = power_optimized(n,p//2)

    if p % 2 == 0:
        return half*half
    else:
        return half*half*n


n = int(input("Enter the number: "))
p = int(input("Enter it's power: "))
print(power(n,p))
print(power_optimized(n,p))