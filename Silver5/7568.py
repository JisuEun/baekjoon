import sys
input = sys.stdin.readline

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

ans = [1] * N

for i in range(N):
    for j in range(N):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            ans[i] += 1

print(*ans)