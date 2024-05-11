import sys
input = sys.stdin.readline
n, m = map(int, input().split())
num = list(map(int,input().split()))
result = 0
sum = [0]

for i in num:
    result = result + i
    sum.append(result)

for _ in range(m):
    a, b = map(int,input().split())
    print(sum[b]-sum[a-1])
