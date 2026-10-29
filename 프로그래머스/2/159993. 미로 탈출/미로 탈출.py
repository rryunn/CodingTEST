from collections import deque

def bfs(sx,sy,visited,n,m,maps,fx,fy):
    q = deque()
    visited[sx][sy]=True
    q.append((sx,sy,0))
    
    dx = [0,-1,0,1]
    dy = [1,0,-1,0]
    
    while q:
        x,y,total= q.popleft()
        if x==fx and y==fy:
            return total
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if maps[nx][ny]=='O' or maps[nx][ny]=='L' or maps[nx][ny]=='E' or maps[nx][ny]=='S':
                    visited[nx][ny]=True

                    q.append((nx,ny,total+1))
    
    return -1
    
def solution(maps):
    # 아 레버까지 갔다가 방문처리 다시 다 리셋
    # 레버 들렷다가 exit
    n = len(maps)
    m = len(maps[0])
    count=0
    visited = [[False]*m for _ in range(n)]
    
    # 레버 위치 좌표랑 출구 좌표 저장하자
    lx=0
    ly=0
    ex=0
    ey=0
    for i in range(n):
        for j in range(m):
            if maps[i][j] =='L':
                lx = i
                ly = j
            elif maps[i][j] =='E':
                ex = i
                ey = j
            elif maps[i][j]=='S':
                sx,sy = i,j

    count+= bfs(sx,sy,visited,n,m,maps,lx,ly)

    if count ==-1:
        return -1
    visited = [[False]*m for _ in range(n)]
    count2=bfs(lx,ly,visited,n,m,maps,ex,ey)
    if count2 ==-1:
        return -1
    return count+count2