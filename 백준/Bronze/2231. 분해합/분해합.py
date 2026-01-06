n = int(input())
t_min =0
for i in range(1, n+1):
    arr = list(map(int,str(i)))
    t_sum = sum(arr)
    result = t_sum + i
    if result ==n:
        t_min = i
        break
print(t_min)
    
