def solution(n, wires):
    graph=[[] for _ in range(n+1)]

    
    for u,v in wires:
        graph[u].append(v)
        graph[v].append(u)
        
    def dfs(start):
        visited[start]=True
        cnt=1
        
        for i in graph[start]:
            if not visited[i]:
                cnt+=dfs(i)
        return cnt        
    min_diff= float('inf')
    
    for start,ignore in wires:
        visited=[False]*(n+1)
        visited[ignore]=True
        group1 = dfs(start)
        group2 = n -group1
        
        diff = abs(group1-group2)
        
        min_diff = min(min_diff, diff)
    return min_diff