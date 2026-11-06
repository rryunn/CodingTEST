from collections import Counter
def solution(want, number, discount):
    answer = 0
    
    target = {w:n for w,n in zip(want, number)}
    
    for i in range(len(discount)-9):
        curr = {}
        for item in discount[i:i+10]:
            curr[item] = curr.get(item,0)+1
        
        if curr==target:
            answer+=1
    return answer