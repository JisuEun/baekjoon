import sys
input = sys.stdin.readline

N = int(input())
data = [int(input()) for _ in range(N)]

dp = [[0]*2 for _ in range(N)]

dp[0][0] = 0
dp[0][1] = data[0]


for i in range(1, N):
    # 이번에 안 밟기: i-1에는 밟았어야 함
    dp[i][0] = dp[i-1][1]
    # 이번에 밟기: i-1에 안 밟기 vs. i-1에 밟고 i-2에 안 밟기
    if i == 1:
        dp[i][1] = dp[i-1][1] + data[i]
    else:
        dp[i][1] = max(dp[i-1][0], dp[i-2][0]+data[i-1]) + data[i]

print(dp[N-1][1])