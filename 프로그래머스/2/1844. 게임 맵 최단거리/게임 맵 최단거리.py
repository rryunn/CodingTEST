from collections import deque
def solution(maps):
    n= len(maps)
    m = len(maps[0])
    
    visited = [[False]*m for _ in range(n)]
    q = deque()
    q.append((0,0,1))
    visited[0][0]=True
    
    while q:
        x,y,cnt = q.popleft()
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        
        if x == n-1 and y ==m-1:
            return cnt
        
        for i in range(4):
            nx = dx[i]+x
            ny= dy[i]+y
            
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and maps[nx][ny]==1:
                visited[nx][ny]= True
                q.append((nx,ny,cnt+1))
    return -1
            
            
            
            