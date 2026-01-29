# 중요도가 높은애들 먼저 출력하겠다
# 어떤 문서가 몇번째로 인쇄되는가

t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    rank = list(map(int,input().split()))
    count=1
    while rank:
        if rank[0] < max(rank):
            rank.append(rank.pop(0))
            
        else:
            if m ==0:
                break
            rank.pop(0)
            count+=1
        m = m-1 if m>0 else len(rank)-1
        
    print(count)