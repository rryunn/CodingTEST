T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    total =0
    max_price = arr[-1]

    for i in range(N-2, -1,-1):
        price = arr[i]

        if price > max_price:
            max_price = price
        else:
            total+=max_price - price
    print(f"#{test_case} {total}")