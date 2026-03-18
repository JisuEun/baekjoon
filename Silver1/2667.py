import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    graph[x][y] = 0
    cnt = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
            cnt += dfs(nx, ny)

    return cnt

result = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            result.append(dfs(i, j))

result.sort()

print(len(result))
for x in result:
    print(x)