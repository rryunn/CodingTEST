import sys
input = sys.stdin.readline
m = int(input())
arr= set()
for _ in range(m):
    cmd = input().strip()
    if cmd == 'all':
        arr = set(range(1,21))
    elif cmd == 'empty':
        arr.clear()
    else:
        cmd, v = cmd.split(" ")
        v = int(v)
        if cmd ==  "add":
            arr.add(v)
        elif cmd == "remove":
            if v in arr:
                arr.remove(v)
            else:
                continue
        elif cmd =="check":
            if v in arr:
                print(1)
            else:
                print(0)
        elif cmd == "toggle":
            if v in arr:
                arr.remove(v)
            else:
                arr.add(v)

    