from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    queue = deque([(0, 0, 1)])
    visited[0][0] = 1

    while queue:
        y, x, dist = queue.popleft()
        if y == N-1 and x == M-1:
            return dist
        for i in range(4):
            ni = y + di[i]
            nj = x + dj[i]
            if 0 <= ni < N and 0 <= nj < M:
                if not visited[ni][nj] and arr[ni][nj] == 1:
                    visited[ni][nj] = 1
                    queue.append((ni, nj, dist+1))
    return 0

N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

di = (0, 1, 0, -1)
dj = (1, 0, -1, 0)

print(bfs())
