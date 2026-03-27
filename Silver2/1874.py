import sys
input = sys.stdin.readline

n = int(input())
stack = []
ans = []

cur = 1
possible = True
for _ in range(n):
    target = int(input())

    while cur <= target:
        stack.append(cur)
        ans.append('+')
        cur += 1

    if stack and stack[-1] == target:
        stack.pop()
        ans.append('-')
    else:
        possible = False
        break

if possible:
    for a in ans:
        print(a)
else:
    print("NO")