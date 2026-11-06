from collections import Counter
def solution(want, number, discount):
    answer = 0
    
    target = {w:n for w,n in zip(want, number)}
    
    for i in range(len(discount)-9):
        if Counter(discount[i:i+10])==target:
            answer+=1
    return answer