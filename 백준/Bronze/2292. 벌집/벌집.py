n = int(input())
count=1
while n>1:
    cal = count*6 
    count+=1
    if(n>=cal):     
        n = n - cal 
    else:
        break
print(count)