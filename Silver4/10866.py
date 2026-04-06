import sys
input = sys.stdin.readline

N = int(input())

deque = []
for _ in range(N):
    cmd = list(input().rstrip().split())

    if cmd[0] == "push_front":
        deque = [cmd[1]] + deque
    elif cmd[0] == "push_back":
        deque.append(cmd[1])
    elif cmd[0] == "pop_front":
        print(deque.pop(0) if deque else -1)
    elif cmd[0] == "pop_back":
        print(deque.pop(-1) if deque else -1)
    elif cmd[0] == "size":
        print(len(deque))
    elif cmd[0] == "empty":
        print(1 if not deque else 0)
    elif cmd[0] == "front":
        print(deque[0] if deque else -1)
    elif cmd[0] == "back":
        print(deque[-1] if deque else -1)