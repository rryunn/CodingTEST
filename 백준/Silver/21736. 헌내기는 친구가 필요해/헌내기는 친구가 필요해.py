from collections import deque
n,m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(list(input()))

q = deque()
v = set()

for i in range(n):
    for j in range(m):
        if arr[i][j] =='I':
            q.append((i,j))
            v.add((i,j))

count=0
while q:
    ci,cj = q.popleft()
    for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
        ni = di+ci
        nj = dj+cj

        if 0<=ni<n and 0<=nj<m and (ni,nj) not in v and arr[ni][nj]!='X':
            if arr[ni][nj] =='P':
                count+=1
                q.append((ni,nj))
                v.add((ni,nj))
            else:
                q.append((ni,nj))
                v.add((ni,nj))

if count ==0:
    print('TT')
else:
    print(count)