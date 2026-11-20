T =10
for _ in range(1,T+1):
    test_case = int(input())
    count =0
    find = input()
    lst = input()
    for i in range(len(lst)-len(find)+1):
        if find == lst[i:i+len(find)]:
            count+=1

    print(f"#{test_case} {count}")