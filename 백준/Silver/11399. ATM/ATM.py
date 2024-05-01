n = int(input())
counts = list(map(int,input().split()))
counts.sort()

total = []
total.append(counts[0])

for i in range(1,n):
    total.append(counts[i] + total[i-1])
print(sum(total))