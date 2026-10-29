def solution(s):
    n = len(s)
    count=0
    for i in range(n):
        arr = ""
        arr = s[i:] + s[:i]        
        stack = []
        
        for i in arr:
            if stack:
                if i==')' and stack[-1]=='(':
                    stack.pop()
                elif i=='}' and stack[-1]=='{':
                    stack.pop()
                elif i==']' and stack[-1]=='[':
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)

        if not stack:
            count+=1
    return count