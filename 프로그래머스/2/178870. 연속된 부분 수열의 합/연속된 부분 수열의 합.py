def solution(sequence, k):
    answer = []
    left =0
    right =0
    total = sequence[0]
    min_len = float('inf')
    
    while right<len(sequence):
        if total==k:
            current_len = right-left
            
            if current_len < min_len:
                min_len = current_len
                answer =[left,right]
            total-=sequence[left]
            left+=1
        elif total<k:
            right+=1
            if right < len(sequence):
                total+=sequence[right]
        else:
            total-=sequence[left]
            left+=1
    return answer