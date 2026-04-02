import sys
input = sys.stdin.readline

N, M = map(int, input().split())

hear = [input().rstrip() for _ in range(N)]
look = [input().rstrip() for _ in range(M)]

ans = list(set(hear) & set(look))
ans.sort()

print(len(ans))

for i in range(len(ans)):
    print(ans[i])