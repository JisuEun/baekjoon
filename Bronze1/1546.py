import sys
input = sys.stdin.readline

N = int(input())
scores = list(map(int, input().split()))
standard = max(scores)

for i in range(N):
    scores[i] = scores[i]/standard*100

print(sum(scores)/N)