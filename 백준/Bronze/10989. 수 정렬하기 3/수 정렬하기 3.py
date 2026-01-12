import sys
input = sys.stdin.readline
n = int(input())
count = [0]* 10001
#arr.sort()
# 카운팅 정렬? 첨들어봤는디 값을 저장하지말고 개수를 저장하래요
# index를 입력값으로 생각하고 하라는 거 같음
for i in range(n):
    num = int(input())
    count[num]+=1

for i in range(1,10001):
    if count[i] !=0:
        for _ in range(count[i]):
            print(i)    