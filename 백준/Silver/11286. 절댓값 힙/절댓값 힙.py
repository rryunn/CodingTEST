import sys
import heapq

input_str = sys.stdin.readline()
n = int(input_str)

heap = []

for i in range(n):
    input2 = sys.stdin.readline()
    num = int(input2)
    if num != 0:
        heapq.heappush(heap, (abs(num), num))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except IndexError:
            print(0)
