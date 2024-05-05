T = int(input())
for i in range(T):
    n = int(input())
    x, y = 1, 0
    for i in range(n):
        x, y = y , x+y
    print(x,y)