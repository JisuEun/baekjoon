import sys
input = sys.stdin.readline

N = int(input())

data = [list(input().split()) for _ in range(N)]

for i in range(N):
    data[i][0] = int(data[i][0])

data.sort(key=lambda x: x[0])

for d in data:
    print(*d)