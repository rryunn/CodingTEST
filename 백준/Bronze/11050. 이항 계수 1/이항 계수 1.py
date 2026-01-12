n,k = map(int,input().split())
up= 1
down =1
for i in range(1,n+1):
    up*=i
for j in range(1,k+1):
    down*=j
for k in range(1,n-k+1):
    down*=k
print(int(up/down))