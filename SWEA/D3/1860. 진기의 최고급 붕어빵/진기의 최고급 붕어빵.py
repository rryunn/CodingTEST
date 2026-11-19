T= int(input())

for test_case in range(1,T+1):
    n,m,k = map(int,input().split())
    time = list(map(int,input().split()))
    time.sort()

    is_p = True
    for i in range(len(time)):
        total = (time[i]//m)*k - i
        if total <=0:
            is_p = False
            break

    if is_p:
        print(f"#{test_case} Possible")
    else:
        print(f"#{test_case} Impossible")