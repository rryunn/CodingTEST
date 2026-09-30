def solution(sizes):
    max_w = 0 # 긴 변들의 최댓값
    max_h = 0 # 짧은 변들의 최댓값
    
    for w, h in sizes:
        # 둘 중 큰 값을 w_side, 작은 값을 h_side로 정렬
        w_side = max(w, h)
        h_side = min(w, h)
        
        # 각각의 최댓값을 갱신
        max_w = max(max_w, w_side)
        max_h = max(max_h, h_side)
        
    return max_w * max_h