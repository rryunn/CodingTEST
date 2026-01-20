from collections import deque
n = int(input())

arr = []
for i in range(1,n+1):
    arr.append(i)
queue = deque(arr)

count=0
while True:
    count+=1
    if(len(queue)==1):
        break
    if count%2==1:
        queue.popleft()
        
    else:
        new = queue.popleft()
        queue.append(new)
        
print(queue.popleft())