def solution(my_string, m, c):
    n=len(my_string)
    s =""
    for i in range(0,n,m):
        arr= my_string[i:i+m]
        s+=arr[c-1]
    return s