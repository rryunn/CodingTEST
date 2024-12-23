n = int(input())
arr = list(map(int,input().split()))
    
sum = 0
max = max(arr)

for i in arr:
    i = i*100/max
    sum = sum + i

print(sum/len(arr))