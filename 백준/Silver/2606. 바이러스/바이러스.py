N = int(input())
V = int(input())

graph = [[] for _ in range(N + 1)]
for _ in range(V):
    line1, line2 = map(int,input().split())
    graph[line1].append(line2)
    graph[line2].append(line1)
    
def dfs(start):
    global count
    visited[start] = True
    count +=1
    for i in graph[start]:
            if not visited[i]:
                dfs(i)
count = 0
visited = [False for _ in range(N+1)]
dfs(1)
print(count-1)