import sys
input = sys.stdin.readline

N = int(input())

data = [list(input().split()) for _ in range(N)]

data.sort(key=lambda x: int(x[0]))

for d in data:
    print(*d)