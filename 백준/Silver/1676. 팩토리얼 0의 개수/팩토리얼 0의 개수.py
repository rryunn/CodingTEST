n = int(input())
total=1
for i in range(n,0,-1):
    total*=i

total = str(total)
count =0
for i in range(len(total)-1,-1,-1):
    if total[i]=='0':
        count+=1    
    else:
        break
print(count)