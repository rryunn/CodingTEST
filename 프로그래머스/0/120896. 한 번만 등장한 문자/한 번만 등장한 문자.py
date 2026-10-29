def solution(s):
    arr ={}
    for i in s:
        if i not in arr:
            arr[i]=1
        else:
            arr[i]+=1

    ans =[]
    print(arr)
    for key,value in arr.items():
        if value ==1:
            ans.append(key)
    
    print(ans)
    ans.sort()
    return "".join(ans)