from collections import deque
def solution(begin, target, words):
    
    q = deque()
    visited = set([begin])
    q.append((begin, 0))
    
    if target not in words:
        return 0
    
    while q:
        word, count = q.popleft()
        
        if word == target:
            return count
        
        for w in words:
            diff=0
            for a,b in zip(w, word):
                if a!=b:
                    diff+=1
            if diff==1:
                q.append((w,count+1))
                visited.add(w)
    