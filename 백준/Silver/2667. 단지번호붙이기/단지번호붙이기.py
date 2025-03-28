def dfs(x,y):
    if x<0 or x>=N or y<0 or y>=N:
        return False
    
    if arr[x][y] == 1:
        global count
        count+=1 
        arr[x][y] = 0
        
        for i in range(4):
        
            ni = x + di[i]
            nj = y + dj[i]
            dfs(ni, nj)
        return True 
    return False
  
    

N =int(input())
arr =[list(map(int,input().strip())) for _ in range(N)]
num = []
di = (0,1,0,-1)
dj = (1,0,-1,0)
count = 0
result= 0

for i in range(N):
    for j in range(N):
        if dfs(i,j) :
            num.append(count)
            result += 1
            count =0
            
num.sort()
print(result)
for i in range(len(num)):
    print(num[i])
