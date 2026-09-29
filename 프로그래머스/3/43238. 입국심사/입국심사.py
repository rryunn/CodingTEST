def solution(n, times):
    start=0
    end = max(times)*n
    mn =end
    
    while start<=end:
        
        mid = (start+end)//2
        cnt =0
        for time in times:
            cnt+=mid//time
        
        if cnt>=n:
            mn = mid
            end = mid -1
        else:
            start = mid+1
    return mn