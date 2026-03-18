import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)

def dfs(v):
    visited[v] = True

    for next in graph[v]:
        if not visited[next]:
            dfs(next)

dfs(1)

cnt = 0
for a in visited:
    if a:
        cnt += 1

print(cnt - 1)