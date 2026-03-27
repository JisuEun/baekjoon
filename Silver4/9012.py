import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    stack = []
    data = input().strip()
    try:
        for d in data:
            if d == '(':
                stack.append('(')
            else:
                stack.pop()
    except:
        print("NO")
        continue
    if stack:
        print("NO")
    else:
        print("YES")
