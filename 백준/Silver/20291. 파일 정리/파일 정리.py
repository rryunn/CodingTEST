n = int(input())
d ={}
for i in range(n):
    a,b = input().split(".")
    if b not in d:
        d[b]=1
    else:
        d[b]+=1

sort_file = sorted(d.items())
for key,value in sort_file:
    print(key, value)