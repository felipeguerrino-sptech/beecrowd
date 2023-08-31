cases = int(input())

for i in range(0, cases):
    food = float(input())
    dias = 0
    while(food > 1):
        food = food / 2
        dias += 1
        
    print(f"{dias} dias")
    