import sys
input = sys.stdin.readline

N, M = map(int, input().split())

matrix1 = [list(map(int, input().split())) for _ in range(N)]
matrix2 = [list(map(int, input().split())) for _ in range(N)]
ans = [[] for _ in range(N)]

for i in range(N):
    for j in range(M):
        ans[i].append(matrix1[i][j] + matrix2[i][j])

for i in range(N):
    print(*ans[i])