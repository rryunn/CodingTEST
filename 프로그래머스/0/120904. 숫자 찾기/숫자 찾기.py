def solution(num, k):
    arr =list(str(num))
    for i in range(len(arr)):
        if int(arr[i]) == k:
            return i+1
    return -1