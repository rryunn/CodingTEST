from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    
    distance = [-1]*(n+1)
    for u,v in edge:
        graph[u].append(v)
        graph[v].append(u)
    
    q = deque()
    q.append(1)
    distance[1] =1
    
    while q:
        node = q.popleft()
        
        for i in graph[node]:
            if distance[i]==-1:
                distance[i] = distance[node]+1
                q.append(i)
    print(distance)
    
    dist = max(distance)
    return distance.count(dist)