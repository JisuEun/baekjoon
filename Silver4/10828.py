import sys
input = sys.stdin.readline

stack = []

N = int(input())

for _ in range(N):
    cmd = input().strip()
    if "push" in cmd:
        X = list(cmd.split())[1]
        stack = [X] + stack
    elif cmd == "pop":
        if stack:
            print(stack[0])
            stack = stack[1:]
        else:
            print(-1)
    elif cmd == "size":
        print(len(stack))
    elif cmd == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif cmd == "top":
        if stack:
            print(stack[0])
        else:
            print(-1)
