import sys
input = sys.stdin.readline

N = int(input())
card = list(map(int, input().split()))

M = int(input())
temp = list(map(int, input().split()))

find = {}
for t in temp:
    find[t] = 0


for c in card:
    if c in find.keys():
        find[c] += 1

for t in temp:
    print(find[t], end=' ')