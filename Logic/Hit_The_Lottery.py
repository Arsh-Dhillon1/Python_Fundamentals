n = int(input())
bill_count = 0
current_value = 0

while(current_value<n):
    if current_value+100 <= n:
        current_value+=100
    elif current_value+20 <= n:
        current_value+=20
    elif current_value+10 <= n:
        current_value+=10
    elif current_value+5 <= n:
        current_value+=5
    else:
        current_value+=1
    # print(current_value)
    bill_count+=1

print(bill_count)