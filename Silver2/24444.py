import sys
input = sys.stdin.readline
from collections import deque

N, M, R = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

visited = [0] * (N + 1)
def bfs(v):
    cnt = 1
    visited[v] = cnt
    queue = deque([v])

    while queue:
        cur = queue.popleft()

        for nv in graph[cur]:
            if not visited[nv]:
                cnt += 1
                visited[nv] = cnt
                queue.append(nv)

bfs(R)

for i in range(1, N+1):
    print(visited[i])