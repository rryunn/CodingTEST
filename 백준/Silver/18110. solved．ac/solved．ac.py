import sys
input = sys.stdin.readline
n = int(input())

# 의견없을시 난이도 0 
# 의견 하나 이상이면 30% 절대평균(가장큰거15%랑 작은거 15% 제거)
# 인원수는 반올림. 
# 결과도 반올림 

if n==0: print(0)
else:
        
    arr = []
    for _ in range(n):
        new = int(input())
        arr.append(new)

    percent = int(n * 0.15 + 0.5)

    sum=0
    arr.sort()
    for i in range(percent, len(arr)-percent):
        sum+=arr[i]

    print(int((sum/(n-2*percent))+0.5))

# 파이썬에서 round는 우리가 아는 반올림이 아님.
# 0.5일때는 가장 가까운 짝수로 감 ㅇㅈㄹ
# 2.5면 2, 3.5면 4, 4.5면 4 이런 식

