import sys
input = sys.stdin.readline 

n,k = map(int,input().split())
kind =[]
for _ in range(n):
    kind.append(int(input()))

count=0    
for i in reversed(kind):
    if k==0: break
    count+= k//i
    k %= i
print(count)