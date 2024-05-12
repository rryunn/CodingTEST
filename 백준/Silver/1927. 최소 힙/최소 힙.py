import heapq
import sys
n = int(input())
heap = []
for i in range(n):
    num = int(sys.stdin.readline())

    if num != 0:
        heapq.heappush(heap,num)
    else:
        try:
            print(heapq.heappop(heap))
            #pop시 가장 우선순위가 높은, 즉 원소가 가장 작은 수가 먼저 튀어나오고 사라짐
        except:
            print(0)
        