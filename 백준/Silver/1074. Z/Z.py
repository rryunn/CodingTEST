N, r, c = map(int, input().split())


def sol(n, row, col):
    if n == 0:
        return 0
    cnt = 2 * (row % 2) + (col % 2)
    return 4 * sol(n-1, row // 2, col // 2) + cnt


print(sol(N, r, c))