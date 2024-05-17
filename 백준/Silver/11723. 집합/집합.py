import sys
M = int(sys.stdin.readline())
arr = set() #파이썬에서 집합을 이용할 땐 set

for _ in range(M):
    str = sys.stdin.readline().strip().split()
    
    if len(str)==1:
        if str[0] == 'all':
            arr = set([i for i in range(1,21)])
        elif str[0] == 'empty':
            arr = set()
            
    else:
        s,num = str[0], str[1]
        num = int(num)
        if s == 'add':
            arr.add(num)
        elif s == 'remove':
            arr.discard(num) #remove와 discard와의 차이 확인하기
        
        elif s == 'check':
            if num in arr:
                print(1)
            else:  
                print(0)
        elif s == 'toggle':
            if num in arr:
                arr.discard(num)        
            else:
                arr.add(num)
   