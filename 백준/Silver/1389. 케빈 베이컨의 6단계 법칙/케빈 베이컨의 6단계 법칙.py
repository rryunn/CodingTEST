from collections import deque

def bfs(node):
    q= deque([node])
    visited[node] = 1
    
    while q:
        v = q.popleft()
        
        for i in graph[v]:
            if not visited[i]:
                visited[i] = visited[v]+1
                q.append(i)

n, m = map(int,input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
res = []

for i in range(1,n+1):
    visited = [0]*(n+1)
    bfs(i)
    res.append(sum(visited))
    
print(res.index(min(res)) + 1)
#가장 작은 값을 가진 사람을 출력하는데, 값이 같은경우 index(사람의 번호)가 적은걸로 출력
    
    