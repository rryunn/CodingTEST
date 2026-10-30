def solution(clothes):
    d={}
    for cloth, kind in clothes:
        d[kind]=d.get(kind,0)+1
    
    ans = 1
    for count in d.values():
        ans*= (count+1)
    
    return ans-1