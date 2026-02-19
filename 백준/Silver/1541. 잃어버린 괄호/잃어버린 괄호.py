n = input()

arr = n.split('-')

for i in range(len(arr)):
    if '+' in arr[i]:
        plus = list(map(int,arr[i].split('+')))
        total = sum(plus)
        arr[i]=total
    else:
        arr[i] = int(arr[i])
        
result=arr[0]
for i in range(1,len(arr)):
    result-=arr[i]
print(result)