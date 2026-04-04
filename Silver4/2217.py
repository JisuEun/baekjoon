import sys
input = sys.stdin.readline

N = int(input())

rope = sorted([int(input()) for _ in range(N)])

_max = rope[0] * N

for i in range(N):
    if rope[i]*(N-i) > _max:
        _max = rope[i]*(N-i)

print(_max)
