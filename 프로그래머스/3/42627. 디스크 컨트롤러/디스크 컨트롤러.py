import heapq

def solution(jobs):
    answer = 0
    now = 0          # 현재 시간
    i = 0            # jobs 배열의 인덱스
    count = 0        # 처리된 작업 개수
    start = -1       # 바로 전 작업이 시작했던 시간
    heap = []
    
    # 요청 시각 기준으로 정렬
    jobs.sort()
    
    # 모든 작업을 처리할 때까지 반복
    while count < len(jobs):
        # 현재 시점(now) 이전에 들어온 작업들을 힙에 넣음
        while i < len(jobs) and jobs[i][0] <= now:
            # 힙 정렬 우선순위: (소요시간, 요청시각)
            heapq.heappush(heap, (jobs[i][1], jobs[i][0]))
            i += 1
            
        if heap:
            # 대기 큐에서 소요시간이 가장 짧은 작업 꺼내기
            duration, request_time = heapq.heappop(heap)
            start = now
            now += duration
            answer += (now - request_time)  # 반환 시간 = 종료시간 - 요청시간
            count += 1
        else:
            # 대기 큐가 비어있다면 다음 작업의 요청 시각으로 시간을 이동
            now = jobs[i][0]
            
    return answer // len(jobs)