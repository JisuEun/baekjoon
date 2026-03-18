import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)

def bfs(v):
    queue = deque([v])
    visited[v] = True

    while queue:
        cur = queue.popleft()
        for nv in graph[cur]:
            if not visited[nv]:
                visited[nv] = True
                queue.append(nv)


cnt = 0
for i in range(1, N + 1):
    if not visited[i]:
        bfs(i)
        cnt += 1


print(cnt)


