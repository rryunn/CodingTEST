from collections import deque
def dfs(start):
    visited[start] = True
    print(start, end=" ")
    for i in graph[start]:
            if not visited[i]:
                dfs(i)
    
def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

N,M,V = map(int,input().split())
graph = [[] for _ in range(N + 1)]

for j in range(M):
    line1, line2 = map(int,input().split())
    graph[line1].append(line2)
    graph[line2].append(line1)
    
for i in graph:
    i.sort()

visited = [False] * (N + 1)
dfs(V)
print()

visited = [False] * (N + 1)
bfs(V)