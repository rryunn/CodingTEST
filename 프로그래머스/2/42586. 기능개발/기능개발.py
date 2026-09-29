def solution(progresses, speeds):
    ans = []
    for i in range(len(speeds)):
        if (100-progresses[i])%speeds[i]==0:
            ans.append((100-progresses[i])//speeds[i])
        else:
            ans.append((100-progresses[i])//speeds[i] +1)
    
    stack = []
    answer = []
    cnt = 1
    for a in ans:
        if not stack:
            stack.append(a)
        elif stack[-1]<a:
            answer.append(cnt)
            stack.append(a)
            cnt =1
        else:
            cnt+=1
            
    answer.append(cnt)
    return answer
        