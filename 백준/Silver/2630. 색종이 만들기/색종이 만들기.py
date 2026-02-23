def again(x,y,n): #(x,y) 기준 nxn 정사각형 한 색인지 확인.
    color = arr[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color != arr[i][j]: # 다른 색 하나라도 있으면 
                again(x,y,n//2) # 정사각형 4등분해서 쪼갠다잉.
                again(x,y+n//2,n//2)
                again(x+n//2,y,n//2)
                again(x+n//2,y+n//2,n//2)
                return
    if color ==0: # 다른색이 없으면 
        result.append(0) # 추가
    else:
        result.append(1)

n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

result =[]

again(0,0,n)
print(result.count(0))
print(result.count(1))