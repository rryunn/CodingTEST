T = int(input())

for test_case in range(1,T+1):

# NXN에는 파리의 개수
# MXM 파리채로 내려쳐서 파리 잡고자함
#  MAX 죽은 파리를 구하라

# 다소 의역 : MXM 칸 중 만들 수 있는 가장 큰 숫자의 합을 구하라
    arr = []
    n,m = map(int,input().split())
    for i in range(n):
        graph = list(map(int,input().split()))
        arr.append(graph)

    # 5 <= n <=15
    # 2<=m <=n

    mx =0

    #바보냐 m을 기준으로 해야지
    for i in range(0,n-m+1):
        for j in range(0,n-m+1):
            sm = 0
            for c in range(i,i+m):
                sm += sum(arr[c][j:j+m])
            mx = max(mx,sm)
    print(f"#{test_case} {mx}")