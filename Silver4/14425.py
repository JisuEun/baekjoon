import sys
input = sys.stdin.readline

N, M = map(int, input().split())

validation = set([input().rstrip() for _ in range(N)])

cnt = 0
for _ in range(M):
    S = input().rstrip()
    if S in validation:
        cnt += 1
print(cnt)