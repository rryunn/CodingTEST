from collections import deque
def bfs(x,y):
    q.append((x,y))
    visited[x][y]=1
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x +dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            
            if pic[nx][ny] == pic[x][y] and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx,ny))
                

# pic = []
# for i in range(n):
#   row = list(input())
#   pic.append(row)

n = int(input())
pic = [list(input()) for i in range(n)]
q = deque()
dx = [-1,1,0,0]
dy = [0,0,-1,1]
#적록색맹 x
visited = [[0]*n for _ in range(n)]
count1 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            count1+=1
            
#적록색맹 o
for i in range(n):
    for j in range(n):
        if pic[i][j] == 'R':
            pic[i][j] = 'G'
            
visited = [[0] * n for _ in range(n)]
count2 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            count2+=1
            
print(count1)
print(count2)