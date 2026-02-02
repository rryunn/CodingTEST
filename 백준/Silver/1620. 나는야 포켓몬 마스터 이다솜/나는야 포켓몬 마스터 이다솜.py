import sys
input = sys.stdin.readline

n,m = map(int,input().split())
d = {}
for i in range(1,n+1):
    p = input().strip()
    # 문제가 알파벳으로 들어오면 번호를
    # 숫자로 들어오면 문자를
    d[i] = p
    d[p] = i
    
for _ in range(m):
    f = input().strip()
    #if type(f)==str:
    if f.isdigit():
        print(d[int(f)])
    else:
        print(d[f])