import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

for _ in range(T):
    cmd = input().rstrip()
    n = int(input())
    arr = list(input().rstrip()[1:-1].split(","))
    if n == 0:
        queue = deque()
    else:
        queue = deque(arr)

    rev = False
    err = False
    for c in cmd:
        if c == "R":
            rev = not rev
        elif c == "D":
            if not queue:
                print("error")
                err = True
                break
            if rev:
                queue.pop()
            else:
                queue.popleft()
    if not err:
        print('[', ','.join(queue) if not rev else ','.join(reversed(queue)), ']', sep='')

