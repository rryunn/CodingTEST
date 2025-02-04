arr = []
for _ in range(9):
    hei = int(input())
    arr.append(hei)
arr.sort()
sum = sum(arr)
 
found = False   
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if(sum-arr[i]-arr[j] == 100):
            num1 = i
            num2 = j
            found = True
            break
        if found:
            break
arr2 = []
for i in range(len(arr)):
    if i != num1 and i != num2:
        print(arr[i])
