n,m = map(int,input().split())
lens = list(map(int,input().split()))
lens.sort()
start, end = 1, lens[-1] #max(lens)

while start <= end:
    mid = (start+end)//2
    
    tot = 0
    for len in lens:
        if len >= mid:
            tot = tot + ( len - mid )
    
    if tot >= m:
        start = mid +1
    else:
        end = mid -1
        
print(end)