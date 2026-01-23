import sys 
input = sys.stdin.readline
n = int(input())
stack = []
for _ in range(n):
    cmd = input().strip()
    #if 'push' in cmd:
    if cmd.startswith('push'):
        c,v = cmd.split()
        stack.append(int(v))
    elif cmd == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
    elif cmd =='size':
        print(len(stack))
    elif cmd == 'empty':
        if len(stack)==0:
                print(1)
        else:
            print(0)
    elif cmd == 'pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
        

