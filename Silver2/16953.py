A, B = map(int, input().split())

def DFS(A, cnt=1):
    if A >= B:
        if A == B:
            stack.append(cnt)
        cnt -= 1
        return
    else:
        cnt += 1
        DFS(A*2, cnt)
        DFS(A*10+1, cnt)

stack = []
DFS(A)

if len(stack):
    print(min(stack))
else:
    print(-1)

# 종료 조건: A >= B
# A == B된 순간은 stack에 기록