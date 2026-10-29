def solution(n, computers):
    visited = [False]*n
    count=0
    
    def dfs(node):
        visited[node]=True
        for i in range(n):
            if not visited[i] and computers[node][i]==1:
                dfs(i)
                
    for i in range(n):
        if not visited[i]:
            dfs(i)
            count+=1
    return count
        