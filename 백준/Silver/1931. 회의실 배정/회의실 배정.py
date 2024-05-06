n = int(input())
arrs = []
for i in range(n):
    start, end = map(int, input().split())
    arrs.append((start, end))
arrs.sort(key = lambda x : (x[1],x[0]))

time = 0
count = 0
for arr in arrs:
    if time <= arr[0]:
        time = arr[1]
        count += 1
        
print(count)
    