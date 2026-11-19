T =int(input())

dr = [0,1,0,-1]
dc = [1,0,-1,0]

for test_case in range(1,T+1):
    n = int(input())
    arr = [[0]*n for _ in range(n)]
    r,c = 0,0
    direction =0

    for number in range(1, n*n+1):
        arr[r][c] = number

        if number == n*n :
            break

        nr = r+dr[direction]
        nc = c + dc[direction]

        if not (0<=nr<n and 0<=nc<n) or arr[nr][nc]!=0:
            direction = (direction+1)%4
            nr = r+dr[direction]
            nc = c+dc[direction]
        r,c = nr,nc

    print(f"#{test_case}")
    for row in arr:
        print(*row)