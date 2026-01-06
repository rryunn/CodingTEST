n = int(input())
t_min =n
check = False
for i in range(1, n+1):
    arr = list(map(int,str(i)))
    t_sum = sum(arr)
    result = t_sum + i
    if result ==n:
        check = True
        if i < t_min:
            t_min = i
if check == False:
    t_min = 0
print(t_min)
    