T = int(input())
for test_case in range(1,T+1):
    st = input()
    arr = []
    S = set()
    D = set()
    H = set()
    C = set()
    is_Error = False
    for i in range(0,len(st),3):
        if st[i] == 'S':
            value = int(st[i+1:i+3])
            if value in S:
                is_Error=True
            S.add(value)
        elif st[i] == 'D':
            value = int(st[i+1:i+3])
            if value in D:
                is_Error=True
            D.add(value)
        elif st[i] == 'H':
            value = int(st[i + 1:i + 3])
            if value in H:
                is_Error = True
            H.add(value)
        elif st[i] == 'C':
            value = int(st[i + 1:i + 3])
            if value in C:
                is_Error = True
            C.add(value)

    if is_Error:
        print(f"#{test_case} ERROR")
    else:
        print(f"#{test_case} {13-len(S)} {13-len(D)} {13-len(H)} {13-len(C)}")