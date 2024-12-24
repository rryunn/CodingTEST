n = int(input())
arr = []
for _ in range(n):
    x = input()
    arr.append(x)
arr = list(set(arr))

arr2 = sorted(arr, key= lambda x : (len(x), x))

for i in arr2:
    print(i)