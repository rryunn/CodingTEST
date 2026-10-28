from collections import deque

def solution(n, edge):
    graph =[[] for _ in range(n+1)]
    
    for u,v in edge:
        graph[u].append(v)
        graph[v].append(u)
        
    distance = [-1]*(n+1)
    
    q=deque()
    q.append(1)
    distance[1]=0
    
    while q:
        curr = q.popleft()
        
        for nxt in graph[curr]:
            if distance[nxt]==-1:
                distance[nxt]=distance[curr]+1
                q.append(nxt)
    dist = max(distance)
    return distance.count(dist)