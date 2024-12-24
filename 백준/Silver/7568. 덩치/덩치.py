n = int(input())
arr = []
for _ in range(n):
    x,y = map(int,input().split())
    arr.append((x,y))
    

ranks = [1]*n

for i in range(n):
    for j in range(n):
        if i != j :
            if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
                ranks[i] += 1
    

print(" ".join(map(str,ranks)))