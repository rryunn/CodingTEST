import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().rstrip().split()))

arr2 = sorted(list(set(arr)))

#dict = {arr2[i] : i for i in range(len(arr2))}
dict = {}
for i in range(len(arr2)):
    dict[arr2[i]] = i
for i in arr:
    print(dict[i], end = ' ')