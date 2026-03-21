import sys
input = sys.stdin.readline

N = int(input())

coordinate = []

for _ in range(N):
    x, y = map(int, input().split())
    coordinate.append([x, y])

coordinate.sort(key=lambda x: (x[0], x[1]))

for x in coordinate:
    print(*x)