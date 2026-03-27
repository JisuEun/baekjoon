import sys
input = sys.stdin.readline

N = int(input())
stack = []
cnt = 0

for _ in range(N):
    h = int(input())

    while stack and stack[-1] <= h:
        stack.pop()

    cnt += len(stack)
    stack.append(h)

print(cnt)