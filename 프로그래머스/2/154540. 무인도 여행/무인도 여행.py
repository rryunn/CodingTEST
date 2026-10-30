from collections import deque

def bfs(visited,maps,sx,sy,n,m):
    dx = [0,-1,0,1]
    dy = [1,0,-1,0]    
    q= deque()
    q.append((sx,sy))
    visited[sx][sy]=True
    total_food = int(maps[sx][sy])

    while q:
        x,y= q.popleft()
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and maps[nx][ny]!='X':
                total_food+=int(maps[nx][ny])
                q.append((nx,ny))
                visited[nx][ny]= True
        
    return total_food
                
def solution(maps):
    ans =[]
    n = len(maps)
    m = len(maps[0])
    visited = [[False]*m for _ in range(n)]
    count =0
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and maps[i][j]!='X':
                count = bfs(visited,maps,i,j,n,m)
                ans.append(count)
    ans.sort()
    if not ans:
        return [-1]
    return ans