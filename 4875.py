def mico():
    while stack:
        y,x = stack.pop() # y가 행 x가 열 
        arr[y][x] = -1 #지나간 길 표시
        for i in range(4): # 4방향 검색:
            ni = y + di[i]
            nj = x + dj[i]
            
            if 0<= ni <N and 0<=nj<N:
                if arr[ni][nj] ==3 :
                    return 1
                elif arr[ni][nj] == 0 :
                    stack.append((ni,nj))
    return 0

T = int(input())
for test_case in range(1,T+1):
    N= int(input())
    arr= [list(map(int,input().strip())) for _ in range(N)]

    di = (0,1,0,-1) #행
    dj = (1,0,-1,0) # 열 

    for i in range(N): #행
        for j in range(N): # 열
            if arr[i][j] == 2:
                stack =[(i,j)]
                break
    print(f'#{test_case} {mico()}')

