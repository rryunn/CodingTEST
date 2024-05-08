from collections import deque

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x ==k:
            print(way[x])
            break
            
        for i in (x+1, x-1 , 2*x):
            if 0<= i < 100001 and not way[i]:
                way[i] = way[x] +1
                q.append(i)
                
n,k = map(int, input().split())
way = [0] * 100001
bfs()