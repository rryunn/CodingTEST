def solution(clothes):
    arr = {}
    for cloth in clothes:
        c, kind = cloth[0], cloth[1]
        if kind in arr:
            arr[kind].append(c)
        else:
            arr[kind] = [c]
    print(arr)
    
    # kind가 하나면 그냥 그 len 자체 제출
    #
    for key in arr:
        if len(arr)==1:
            return len(arr[key])
    cnt = 1
    for key in arr:
        cnt*=(len(arr[key])+1)

    print(arr)
    return cnt-1