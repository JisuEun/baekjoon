import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (N+1)

def BFS(v):
    queue = deque([v])
    while queue:
        curr = queue.popleft()
        for x in graph[curr]:
            if not parent[x]:
                parent[x] = curr
                queue.append(x)

BFS(1)

for i in range(2, N+1):
    print(parent[i])