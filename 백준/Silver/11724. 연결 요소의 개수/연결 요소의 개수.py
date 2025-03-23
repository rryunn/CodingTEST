def dfs(node):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor)
            
V,E = map(int,input().split())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = set()
count = 0

for node in range(1,V+1):
    if node not in visited:
        dfs(node)
        count+=1
        
print(count)