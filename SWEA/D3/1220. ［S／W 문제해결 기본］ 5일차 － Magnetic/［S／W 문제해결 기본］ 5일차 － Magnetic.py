T = 10
for test_case in range(1,T+1):
    count=0
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    for j in range(n):
        check = False
        for i in range(n):
            if arr[i][j] == 1:
                check = True
            if check and arr[i][j]==2:
                count+=1
                check = False

    print(f"#{test_case} {count}")