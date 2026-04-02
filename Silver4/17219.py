import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dict = {}

for _ in range(N):
    url, pw = input().rstrip().split()
    dict[url] = pw

for _ in range(M):
    print(dict[input().rstrip()])