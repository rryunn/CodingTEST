# # '('가 들어오면 stack에 저장했다가 
# # ')'가 들어오면 pop을 해! 그때 에러나면 no
# # 마찬가지로 []도 같이 진행.


while True:
    arr = input()
    check = True
    if arr =='.':
        break
    stack = []
    for i in arr:
        if i not in '()[]':
            continue
        if i == '(' or i== '[':
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1]!='(':
                check=False
                break
            stack.pop()
        elif i==']':
            if not stack or stack[-1]!='[':
                check=False
                break
            stack.pop()
        
    if check and not stack:
        print("yes")
    else:
        print("no")
    
