T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    arr = []
    for _ in range(n):
        graph = list(map(int,input()))
        arr.append(graph)

    mid = n//2
    sm =0
    count =0
    for i in range(0,mid+1):
        if count ==0:
            sm +=arr[i][mid]
        else:
            sm+= sum(arr[i][mid-count:mid+count+1])
        count+=1
    count-=1
    for i in range(mid+1, n):
        count-=1
        if count == 0:
            sm += arr[i][mid]
        else:
            sm += sum(arr[i][mid-count:mid+count+1])

    print(f"#{test_case} {sm}")
