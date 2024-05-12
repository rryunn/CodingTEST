from collections import deque
m,n = map(int,input().split())
tomato = []

for i in range(n):
    tomato.append(list(map(int,input().split())))
        
q = deque()

    
dx=  [-1,1,0,0]
dy = [0,0,-1,1]
day= 0

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append([i, j])
            
def bfs():
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x +dx[i]
            ny = y + dy[i]
            
            if nx<0 or nx>=n or ny<0 or ny>=m:
                    continue

            if tomato[nx][ny]==0:
                tomato[nx][ny] = tomato[x][y]+1
                q.append((nx,ny))

        
bfs()

for i in tomato:
    for j in i:
        if j ==0 :
            print(-1)
            exit(0)
    else:
        day = max(day,max(i))

print(day-1)       
