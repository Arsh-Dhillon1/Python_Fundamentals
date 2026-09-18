def generate(n,current):
    if len(current) == n:
        print(current)
        return

    generate(n,current+'0')
    generate(n,current+"1")

n = int(input())
generate(n,"")