def cal(m,n,x,y):
    while x <= m*n: #카잉달력의 마지막해는 m과 n의 최소공배수
        if(x-y)%n == 0: 
            return x
        x += M
    return -1
        
T = int(input())

for _ in range(T):
    M,N,x,y = map(int,input().split())
    print(cal(M,N,x,y))
    
