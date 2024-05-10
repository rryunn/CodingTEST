def dfs(start):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            dfs(i)
    
    
N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    line1, line2 = map(int,input().split())
    graph[line1].append(line2)
    graph[line2].append(line1)
    
count = 0 
visited = [False]*(N+1)

for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        count+=1
        
print(count)