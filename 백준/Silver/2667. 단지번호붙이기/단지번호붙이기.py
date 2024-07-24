
from collections import deque
n = int(input())

lst = [list(map(int,input())) for _ in range(n)]   
def bfs( start_x, start_y):
    count = 1
    queue = deque()
    queue.append([start_x,start_y])
    lst[start_x][start_y] = 0
    dx = [-1,1,0,0]
    dy = [0,0, -1,1]

    while queue:
        x,y = queue.popleft()
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if (0<= nx < n) and (0<= ny < n) and lst[nx][ny] == 1:
                lst[nx][ny] = 0
                queue.append((nx,ny))
            
                count += 1
            
    return count
        


cnt = []

for i in range(n):
    for j in range(n):
        if lst[i][j] ==1:
            cnt.append(bfs(i,j))
            
cnt.sort()
print(len(cnt))
for coun in cnt:
    print(coun)
    
