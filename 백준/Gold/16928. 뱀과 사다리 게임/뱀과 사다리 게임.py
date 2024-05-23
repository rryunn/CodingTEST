from collections import deque
def bfs():
    queue = deque()
    queue.append((1,0))
    visit = [0 for _ in range(101)]
    visit[1] = 1
    
    while queue:
        x, count = queue.popleft()
        if x == 100:
            return count
        for i in range(1, 7, 1):
            nx = x+i
            
            if 0< nx <= 100 and visit[nx] == 0 :
                if nx in dict:
                    nx = dict[nx]
                if nx in careful:
                    nx = careful[nx]
                if visit[nx] == 0:
                    queue.append((nx, count +1 ))
                    visit[nx] =1

N,M = map(int,input().split())
dict ={}
careful = {}
#사다리의 정보 x에 도착 시 y로 이동
for _ in range(N):
    x,y = map(int,input().split())
    dict[x]=y
    
for _ in range(M):
    x,y = map(int,input().split())
    careful[x]=y


print(bfs())