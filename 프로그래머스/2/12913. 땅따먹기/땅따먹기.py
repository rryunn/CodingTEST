def solution(land):
    # 1번째 행부터 마지막 행까지 내려가며 DP 값 갱신
    for i in range(1, len(land)):
        land[i][0] = land[i-1][0] + max(land[i][1],land[i][2],land[i][3])
        land[i][1] = land[i-1][1]+max(land[i][0],land[i][2],land[i][3])
        land[i][2]=land[i-1][2]+max(land[i][1],land[i][3],land[i][0])
        land[i][3]=land[i-1][3] +max(land[i][0],land[i][1],land[i][2])
        
        
    
    # 마지막 행의 4개 값 중 최댓값 반환
    return max(land[-1])