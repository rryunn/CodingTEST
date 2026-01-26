n,k = map(int,input().split())

list = []
check =[]
target=k
index = target-1
for i in range(1,n+1):
    check.append(i)

while len(check)!=0:
    if(index<=len(check)-1):
        a = check.pop(index) #index값으로 pop하니까
        list.append(a)
        index+=target
        index-=1
    else:
        index-=len(check)

# print(list)

print("<",end="")
for i in range(len(list)):
    if i!=len(list)-1:
        print(list[i] , end=", ")
    else:
        print(list[i], end="")
print(">",end="")

