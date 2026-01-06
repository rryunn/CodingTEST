while True:
    n = int(input())
    if n==0:
        break
    else:
        arr = list(str(n))
        length = len(str(n))
        end = length-1
        for i in range(0, int(length/2)+1):
            if arr[i] == arr[end]:
                end = end -1
                if(i==end+1 or i==end):
                    print("yes")
            else:
                print("no")
                break
            