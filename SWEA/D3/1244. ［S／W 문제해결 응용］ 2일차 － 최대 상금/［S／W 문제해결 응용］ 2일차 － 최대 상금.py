T = int(input())

for test_case in range(1,T+1):

    num, change = map(int,input().split())
    arr = list(str(num))
    visited = set()
    ans = 0

    def dfs(count):
        global ans
        current_num = "".join(arr)

        if count ==change:
            ans = max(ans,int(current_num))
            return

        if (current_num, count) in visited:
            return
        visited.add((current_num, count))

        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                arr[i], arr[j] = arr[j], arr[i]
                dfs(count+1)
                arr[i], arr[j] = arr[j], arr[i]
    dfs(0)
    print(f"#{test_case} {ans}")