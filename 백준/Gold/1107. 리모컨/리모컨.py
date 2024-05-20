import sys
input = sys.stdin.readline

n = int(input())
m = int(input()) 
brokes = list(map(int, input().split()))

count = abs(100 - n)

for nums in range(1000001):
    num = str(nums)

    for i in range(len(num)):  # 숫자 num의 각 자리수를 확인
        if int(num[i]) in brokes:  # 고장났으면 중단
            break
    else:  #고장난게 없으면
        count = min(count, abs(int(num) - n) + len(num))  # 최소 횟수 갱신

print(count)
