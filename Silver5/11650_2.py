import sys
input = sys.stdin.readline

N = int(input())

coord = [list(map(int, input().split())) for _ in range(N)]

coord.sort(key=lambda x: (x[0], x[1]))

for c in coord:
    print(*c)