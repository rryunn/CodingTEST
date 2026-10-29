from collections import deque

def bfs(sx,sy,visited,n,m,maps):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    q= deque()
    q.append((sx,sy))
    visited[sx][sy]=True
    total_food = int(maps[sx][sy])
    
    while q:
        x,y=q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny <m and not visited[nx][ny] and maps[nx][ny]!='X':
                visited[nx][ny] = True
                total_food += int(maps[nx][ny])
                q.append((nx,ny))
        
    return total_food

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False]*m for _ in range(n)]
    arr = []
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and maps[i][j]!='X':
                cnt = bfs(i,j,visited,n,m,maps)
                arr.append(cnt)
    
    if not arr:
        return [-1]
    
    arr.sort()
    return arr