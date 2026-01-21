n = int(input())
for _ in range(n):
    T = input()
    stack = []
    check = True
    for i in T:
        if i =='(' or i=='[':
            stack.append(i)
        elif i==')' :
            if len(stack)!=0 and stack[-1]=='(':
                stack.pop()
            else:
                check = False
        elif i==']' and len(stack)!=0:
            if stack[-1]=='[':
                stack.pop()
            else:
                check = False
    if len(stack)!=0:
        check = False
    if check == False:
        print("NO")
    else:
        print("YES")
        
