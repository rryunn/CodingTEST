import sys

# deque 사용이 문제 의도 ! ! ! !
from collections import deque
input = sys.stdin.readline
deque = deque()
n = int(input())
for _ in range(n):
    cmd = input().strip()
    if cmd.startswith('push'):
        c,v = cmd.split(" ")
        deque.append(int(v))
    elif cmd == 'front':
        if len(deque)!=0:
            print(deque[0])
        else:
            print(-1)
    elif cmd == 'back':
        if len(deque)!=0:
            print(deque[-1])
        else:
            print(-1)
    elif cmd == 'size':
        print(len(deque))
    elif cmd =='empty':
        if len(deque)==0:
            print(1)
        else:
            print(0)
    elif cmd == 'pop':
        if len(deque)!=0:
            print(deque.popleft())
        else:
            print(-1)