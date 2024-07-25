#최단거리 bfs
#경로에 대한 정보 저장 dfs
from collections import deque
def solution(maps):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    n = len(maps)
    m = len(maps[0])
    
    start_x, start_y = 0 , 0
    end_x, end_y = n-1,m-1
    
    q = deque()
    #q의 원소는 x좌표, y좌표, 거리
    q.append((start_x, start_y,1))

    visited = set()
    visited.add((start_x, start_y))
    answer = -1
    while q:
        
        x,y,distance = q.popleft()
        
        if(x,y) == (end_x,end_y):
            answer = distance
            
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if 0<=nx<n and 0<=ny<m and maps[nx][ny] == 1 and (nx,ny) not in visited:
                q.append((nx,ny, distance+1))
                visited.add((nx,ny))
                 
                
                
    return answer
            