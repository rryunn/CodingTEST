from collections import deque

def solution(n, wires):
    graph =[[] for _ in range(n+1)]

    for u,v in wires:
        graph[u].append(v)
        graph[v].append(u)
    
    def count_node(start,ignore):
        
        visited= [False]*(n+1)
        visited[start]=True
        visited[ignore]=True
        q = deque()
        cnt=1
        q.append(start)
        while q:
            node = q.popleft()
            for g in graph[node]:
                if not visited[g]:
                    visited[g]=True
                    q.append(g)
                    cnt+=1
        return cnt
      
    min_dff=float('inf')
    for u,v in wires:
        cnt1= count_node(u,v)
        cnt2 = n-cnt1
        
        diff= abs(cnt1-cnt2)
        min_dff = min(min_dff,diff)
    return min_dff