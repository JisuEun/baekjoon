import sys
input = sys.stdin.readline

N = int(input())
card = set(list(map(int, input().split())))
M = int(input())
ox = list(map(int, input().split()))

for i in range(M):
    if ox[i] in card:
        print(1, end=" ")
    else:
        print(0, end=" ")