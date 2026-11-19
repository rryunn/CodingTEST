T = int(input())

for test_case in range(1,T+1):

    n, k = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]

    # 가로 세로 보면서 1이 연속하는 길이가 k와 같을 경우 +1
    count =0
    for i in range(n):
        check =0
        for j in range(n):
            if arr[i][j]==1:
                check+=1
            elif check ==k and arr[i][j]==0:
                count+=1
                check=0
            else:
                check=0
        if check == k:
            count+=1

    for j in range(n):
        check=0
        for i in range(n):
            if arr[i][j] == 1:
                check += 1
            elif check == k and arr[i][j] == 0:
                count += 1
                check = 0
            else:
                check=0
        if check == k:
            count += 1

    print(f"#{test_case} {count}")