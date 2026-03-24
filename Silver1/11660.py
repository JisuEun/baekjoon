import sys
input = sys.stdin.readline

N, M = map(int, input().split())

table = [list(map(int, input().split())) for _ in range(N)]
coord = [list(map(int, input().split())) for _ in range(M)]

dp = [[0]*N for _ in range(1025)]

for i in range(N):
    for j in range(N):
        if i == 0 and j == 0:
            dp[0][0] = table[0][0]
        elif i == 0:
            dp[i][j] = dp[i][j-1] + table[i][j]
        elif j == 0:
            dp[i][j] = dp[i-1][j] + table[i][j]
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + table[i][j]

for i in range(M):
    if coord[i][0] == 1 and coord[i][1] == 1:
        print(dp[coord[i][2]-1][coord[i][3]-1])
    elif coord[i][0] == 1:
        print(dp[coord[i][2]-1][coord[i][3]-1] - dp[coord[i][2]-1][coord[i][1]-2])
    elif coord[i][1] == 1:
        print(dp[coord[i][2]-1][coord[i][3]-1] - dp[coord[i][0]-2][coord[i][3]-1])
    else:
        print(dp[coord[i][2]-1][coord[i][3]-1] - dp[coord[i][2]-1][coord[i][1]-2] - dp[coord[i][0]-2][coord[i][3]-1] + dp[coord[i][0]-2][coord[i][1]-2])