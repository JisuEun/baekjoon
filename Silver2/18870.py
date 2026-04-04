import sys
input = sys.stdin.readline

N = int(input())
coord = list(map(int, input().split()))
coord2 = sorted(list(set(coord)))

dic = {}
for i in range(len(coord2)):
    dic[coord2[i]] = i

for i in coord:
    print(dic[i], end=" ")
