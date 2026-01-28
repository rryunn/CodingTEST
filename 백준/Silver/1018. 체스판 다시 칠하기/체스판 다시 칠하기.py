n,m=map(int,input().split())
chess = []
count = []

for _ in range(n):
    chess.append(input())

# 행가 열의 합이 짝수 , 홀수이면 각각 일정한 색을 가지게 된다.
for i in range(n-7):
    for j in range(m-7):
        w =0 
        b =0
        for k in range(i, i+8): # 행 인덱스
            for l in range(j,j+8): # 열 인덱스
                if (k+l)%2==0:
                    if chess[k][l] != 'W':
                        w+=1
                    else:
                        b+=1
                else:
                    if chess[k][l] != 'B':
                        w+=1
                    else:
                        b+=1
        count.append(w)
        count.append(b)

print(min(count))