import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input()) # 층
    n = int(input()) # 호
    dp = [[0] * (n+1) for _ in range(k+1)] # 1층 -> 0, 1층
    dp[0] = [i for i in range(n+1)] # 1호 2호 ... n호
    for i in range(1, k+1):
        for j in range(1, n+1):
            dp[i][j] = sum(dp[i-1][:j+1])
    print(dp[k][n])
