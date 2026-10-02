import heapq

def solution(scoville, K):
    count=0
    heapq.heapify(scoville)
    while scoville[0]<K:
        if len(scoville)<2:
            return -1
        
        first = heapq.heappop(scoville) #제일 작은거

        second = heapq.heappop(scoville)

        #계산한 값을 다시 넣어줍니다
        heapq.heappush(scoville, first+(second)*2)
        count+=1
    return count