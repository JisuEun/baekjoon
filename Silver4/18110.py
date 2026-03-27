import sys
input = sys.stdin.readline

n = int(input())

if n == 0:
    print(0)
else:
    rate = [int(input()) for _ in range(n)]

    rate.sort()

    cut = int(0.15*n+0.5)

    rate = rate[cut:n-cut]

    print(int(sum(rate)/len(rate)+0.5))