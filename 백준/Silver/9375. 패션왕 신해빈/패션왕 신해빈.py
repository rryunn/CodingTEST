
T = int(input())

for _ in range(T):
    n = int(input())
    d = {}
    for _ in range(n):
        clothes, kind= input().split()
        if kind in d:
            d[kind].append(clothes)
        else:
            d[kind] = [clothes]

    # [1,2] [1]
    count=1
    for x in d:
        count*=(len(d[x])+1)
    print(count-1)