from collections import deque
T = 10
for _ in range(1,T+1):
    test_case = int(input())

    arr = list(map(int,input().split()))
    q = deque()
    for a in arr:
        q.append(a)
    count=1
    while True:
        stan = q.popleft()
        if stan-count<=0:
            q.append(0)
            break
        else:
            q.append(stan-count)
            count+=1
            if count ==6:
                count=1
    print(f"#{test_case}",*q)