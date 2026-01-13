n = input()
total =0
check=1
for i in range(len(n)):
    if n[i]=='*':
        if i%2==0:
            check=1
        else:
            check=3
    else:   
        if i%2==0:
            total+=int(n[i])
        else:
            total+=int(n[i])*3

need = (10-total%10)%10
if check==1:
    print(need)
else:
    for x in range(10):
        if(3*x)%10==need:
            print(x)
            break