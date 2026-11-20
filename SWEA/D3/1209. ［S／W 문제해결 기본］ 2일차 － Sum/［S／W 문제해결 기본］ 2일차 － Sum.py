T= 10
for _ in range(1,T+1):
    test_case = int(input())
    sm =0
    arr = [list(map(int,input().split())) for _ in range(100)]

    # 행
    for i in range(100):
        sm = max(sm, sum(arr[i]))

    # 열
    for j in range(100):
        c = sum(arr[r][j] for r in range(100))
        sm = max(c,sm)

    # 대각선
    diag1=0
    diag2=0
    for i in range(100):
        for j in range(100):
            if i==j:
                diag1+=arr[i][j]
            elif i == 100-1-j:
                diag2+=arr[i][j]
    sm = max(diag1, diag2, sm)

    print(f"#{test_case} {sm}")