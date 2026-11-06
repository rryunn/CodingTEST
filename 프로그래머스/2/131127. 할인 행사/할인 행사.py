def solution(want, number, discount):
    d = {w:n for w,n in zip(want, number)}
    answer=0
    for i in range(len(discount)-9):
        
        curr = {}
        for j in discount[i:i+10]:
            curr[j] = curr.get(j,0)+1
        
        if curr==d:
            answer+=1
    return answer