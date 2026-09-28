def solution(n, times):
    #몇분까지 가능한가 20분 ? 30분? 하면서 좁혀나가는 이분탐색임.
    
    start = 1
    end = max(times)*n
    mn = end
    while start<=end:
        
        mid = (start+end)//2
        count =0
        for t in times:
            count +=mid//t
        
        if count >=n:
            mn = mid
            end = mid -1
        else:
            start = mid + 1
            
    return mn
