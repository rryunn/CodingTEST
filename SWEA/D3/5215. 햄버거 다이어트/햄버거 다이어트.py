T =int(input())
for test_case in range(1,T+1):
    n, cal = map(int,input().split())
    arr = []
    for _ in range(n):
        a,b = map(int,input().split())
        arr.append((a,b))

    #[(100,200), (300,500), (250,300), (500,1000), (400,400)]
    arr.sort(reverse=True)
    #[(500, 1000), (400, 400), (300, 500), (250, 300), (100, 200)]
    visited = [False]*n
    mx =0
    def dfs(start, total_favor, total_cal):
        global mx
        if total_cal > cal:
            return
        mx = max(mx, total_favor)
        for i in range(start, len(arr)):
            if visited[i]:
                continue
            visited[i] = True
            dfs(i+1, total_favor +arr[i][0], total_cal + arr[i][1])
            visited[i] = False

    dfs(0,0,0)
    print(f"#{test_case} {mx}")