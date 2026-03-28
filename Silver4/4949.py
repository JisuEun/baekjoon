import sys
input = sys.stdin.readline

while True:
    S = input().rstrip("\n")

    if S == ".":
        break

    stack = []
    isValid = True
    for s in S:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if len(stack) == 0 or stack[-1] != '(':
                isValid = False
                break
            else:
                stack.pop()
        elif s == ']':
            if len(stack) == 0 or stack[-1] != '[':
                isValid = False
                break
            else:
                stack.pop()

    if stack:
        isValid = False
    print("yes" if isValid else "no")