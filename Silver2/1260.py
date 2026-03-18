import sys
input = sys.stdin.readline

from collections import deque

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

visited = [False] * (N + 1)

def dfs(v):
    visited[v] = True
    print(v, end= " ")
    for nv in graph[v]:
        if not visited[nv]:
            dfs(nv)

dfs(V)

print()

visited = [False] * (N + 1)

def bfs(v):
    queue = deque([v])
    visited[v] = True

    while queue:
        cur = queue.popleft()
        print(cur, end=" ")

        for nv in graph[cur]:
            if not visited[nv]:
                visited[nv] = True
                queue.append(nv)

bfs(V)