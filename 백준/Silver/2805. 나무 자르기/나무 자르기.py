import sys
input = sys.stdin.readline
n,m = map(int,input().split())
trees = list(map(int,input().split()))
trees.sort()
start =1
end = trees[-1]

while start<=end:
    mid = (start+end)//2 # 절단기의 높이
    
    total = 0
    for tree in trees:
        if tree>=mid:
            total += tree-mid # 자른만큼 가져감
    if total>=m: # 원하는 만큼 얻었다면
        start = mid +1 # 절단기를 하나 더 높여도 됨
    else: # 너무 높였으면
        end = mid -1 # 내림
        
print(end)