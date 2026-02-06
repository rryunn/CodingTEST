def dfs(node):
    visited[node] = 1
    for neighbor in graph[node]:
        if visited[neighbor] == 0:
            dfs(neighbor)
    
V = int(input())
E = int(input())
visited = [0]*(V+1)
graph = [[] for _ in range(V+1)]
count = 0
for  _ in range(E):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
    
dfs(1)
print(sum(visited)-1)
    
    