import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

visited = [0] * (N + 1)

cnt = 1
def dfs(v):
    global cnt
    visited[v] = cnt

    for nv in graph[v]:
        if not visited[nv]:
            visited[nv] = cnt
            cnt += 1
            dfs(nv)

dfs(R)

for i in range(1, N+1):
    print(visited[i])