from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    q = deque()
    q.append((begin, 0))
    
    visited=set([begin])
    
    while q:
        word, cnt = q.popleft()
        
        if word == target:
            return cnt
        
        for w in words:
            #words중에서 word랑 1글자만 다른거 찾을거예요
            
            if w not in visited:
                diff =   sum(1 for a,b in zip(word,w) if a!=b)
                if diff==1:
                    visited.add(w)
                    q.append((w,cnt+1))
                    
    return 0