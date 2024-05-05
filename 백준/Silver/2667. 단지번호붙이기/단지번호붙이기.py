#2178 미로탐색 문제랑 거의 유사
from collections import deque

def bfs(graph,x,y):
    N= len(graph)
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    queue = deque()
    queue.append((x,y))
    graph[x][y]=0
    count =1
    
    while queue:
        x,y = queue.popleft()

        for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx<0 or nx>=N or ny<0 or ny>=N:
                    continue
                    
                if graph[nx][ny]==0:
                    continue

                if graph[nx][ny]==1:
                    graph[nx][ny] = 0
                    queue.append((nx,ny))
                    count += 1
    return count

N = int(input())
graph = []
counts =[] #단지 개수들을 담을 list
for i in range(N):
    graph.append(list(map(int,input())))
    
for i in range(N):
    for j in range(N):
        if graph[i][j]==1:
            counts.append(bfs(graph,i,j))
            
counts.sort()
print(len(counts))
for count in counts:
    print(count)
    