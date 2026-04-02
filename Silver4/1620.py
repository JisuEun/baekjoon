import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pokemon = {}

for i in range(1, N+1):
    S = input().rstrip()
    pokemon[i] = S
    pokemon[S] = i

for _ in range(M):
    S = input().rstrip()
    if S.isdigit():
        print(pokemon[int(S)])
    else:
        print(pokemon[S])