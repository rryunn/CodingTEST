import sys, heapq #최소힙 만을 지원 함.
input = sys.stdin.readline
N = int(input())
heap = []
for i in range(N):
    num = int(input()) * (-1)
    if num != 0:
        heapq.heappush(heap, num)
    else:
        try:
            print(heapq.heappop(heap)*(-1))
            
        except:
            print(0)

        