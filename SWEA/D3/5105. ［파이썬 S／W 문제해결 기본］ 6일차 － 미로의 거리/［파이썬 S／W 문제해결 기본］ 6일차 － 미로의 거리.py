from collections import deque

def bfs():
    while queue:
        y, x, dist = queue.popleft()  # 현재 위치와 거리 꺼내기
        arr[y][x] = -1  # 방문한 곳 표시
        
        for i in range(4):  # 4방향 탐색
            ni, nj = y + di[i], x + dj[i]

            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == 3:  # 도착지 발견
                    return dist
                elif arr[ni][nj] == 0:  # 이동 가능하면 큐에 추가
                    queue.append((ni, nj, dist + 1))
                    arr[ni][nj] = -1  # 방문 처리

    return 0  # 도착 불가능

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]

    di = (0, 1, 0, -1)  # 행 이동 (상하좌우)
    dj = (1, 0, -1, 0)  # 열 이동 (상하좌우)

    # 출발지(2) 찾기
    queue = deque()
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                queue.append((i, j, 0))  # (행, 열, 이동 거리)
                break

    print(f'#{test_case} {bfs()}')
