#길이가 n인 회문의 개수 구하기

#행 먼저 보기
    # 한 줄씩 볼건데, 잘라서 n개씩 볼거임
    # [i][j:j+n]이렇게 배열을 만들고,
    # n//2만큼의 for문을 돌릴건데
        # arr[0] = arr[n]
        # arr[1] = arr[
        #같으면 count +1
#열 먼저 보기

T=10

for test_case in range(1,T+1):
    n = int(input())
    arr = [list(str(input())) for _ in range(8)]
    count =0

    mid = n//2
    for i in range(8):
        for j in range(8-n+1):
            arr2 = arr[i][j:j+n]
            is_pal =True
            for c in range(mid):
                if arr2[c]!=arr2[n-c-1]:
                    is_pal=False
            if is_pal:
                count+=1


    for j in range(8):
        for i in range(8-n+1):
            arr3 = [arr[r][j] for r in range(i,i+n)]
            if arr3 == arr3[::-1]:
                count+=1
    print(f"#{test_case} {count}")
