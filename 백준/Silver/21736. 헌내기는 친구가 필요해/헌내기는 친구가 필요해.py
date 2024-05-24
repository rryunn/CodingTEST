from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
campus = [] 
x, y = 0, 0 
count = 0 

N, M = map(int, input().split())

for i in range(N):
    campus.append(list(input()))
    
    for j in range(M):
        if campus[i][j] == 'I': 
            x= i
            y = j

visited = [[0] * M for _ in range(N)] 

queue = deque()
queue.append([x, y])

while queue: 
    x, y = queue.popleft()
    for i in range(4):  # 상하좌우 탐색
        nx, ny = x + dx[i], y + dy[i]
        
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0: # 방문 안했으면 
            visited[nx][ny] = 1
            if campus[nx][ny] == 'O':  
                queue.append([nx, ny])
                
            elif campus[nx][ny] == 'P': 
                queue.append([nx, ny])
                count += 1 

print('TT' if count == 0 else count) 