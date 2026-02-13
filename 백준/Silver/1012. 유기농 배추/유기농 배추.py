from collections import deque

T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    arr[x][y] = 0

    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if arr[nx][ny] == 1:
                q.append((nx, ny))
                arr[nx][ny] = 0

for _ in range(T):
    m, n, k = map(int, input().split())
    arr = [[0] * n for _ in range(m)]
    count = 0

    for _ in range(k):
        x, y = map(int, input().split())
        arr[x][y] = 1

    for z in range(m):
        for q in range(n):
            if arr[z][q] == 1:
                bfs(z, q)
                count += 1

    print(count)
