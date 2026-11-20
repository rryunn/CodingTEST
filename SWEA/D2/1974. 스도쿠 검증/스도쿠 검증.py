T = int(input())

for test_case in range(1,T+1):
    arr = [list(map(int,input().split())) for _ in range(9)]
    is_finish=False
    #행
    for i in range(9):
        visited = [False]*10
        for j in range(9):
            if visited[arr[i][j]]:
                is_finish = True
                break
            else:
                visited[arr[i][j]] = True

    # 열
    if not is_finish:
        for j in range(9):
            if sum(arr[r][j] for r in range(9))!=45:
                is_finish=True
                break

    #3x3
    if not is_finish:
        sm =0
        for j in range(0,9,3):
            for i in range(0,9):
                if i!=0 and i%3==0:
                    if sm !=45:
                        is_finish=True
                    else:
                        sm =0
                sm += sum(arr[i][j:j + 3])
            if sm != 45:
                is_finish=True
            else:
                sm=0
    if is_finish:
        result = 0
    else:
        result=1
    print(f"#{test_case} {result}")
