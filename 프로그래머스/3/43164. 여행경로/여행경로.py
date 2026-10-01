def solution(tickets):
    tickets.sort()
    n = len(tickets)+1       
    visited = [False]*(n-1)    
    
    def dfs(start, path):
        if len(path)==n:
            return path
        
        for i, (a,b) in enumerate(tickets):
            
            if not visited[i] and a==start:
                visited[i] = True
                res = dfs(b,path+[b])
                if res:
                    return res
                visited[i] = False
    
    return dfs("ICN",["ICN"])