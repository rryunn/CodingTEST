import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    num = int(input())
    arr.append(num)

# 산술평균
sum = 0
for i in arr:
    sum += i
if sum >= 0:
    print(int(sum/n + 0.5))
else:
    sum = -sum
    rev = int(sum/n + 0.5)
    print(-rev)

# 중앙값
arr.sort()
find = int(len(arr)/2)
print(arr[find])

# 최빈값
same = []
count = 1
for i in range(1, n):
    if arr[i] == arr[i-1]:
        count += 1
    else:
        same.append((arr[i-1], count))  # ⭐ 여기만 수정
        count = 1

same.append((arr[-1], count))  # ⭐ 필수

a_max = 0
for v, c in same:
    if c > a_max:
        a_max = c

mode = []
for v, c in same:
    if c == a_max:
        mode.append(v)

mode.sort()
if len(mode) > 1:
    print(mode[1])
else:
    print(mode[0])

# 범위
print(arr[-1] - arr[0])