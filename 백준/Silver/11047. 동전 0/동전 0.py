n, goal = map(int, input().split())

coins = []
for i in range(n):
    coins.append(int(input()))

coins.sort(reverse=True) 

count = 0
for coin in coins:
    if goal >= coin:  
        count += goal // coin 
        goal %= coin 

print(count)  
