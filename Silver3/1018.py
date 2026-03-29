import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

ans = 64
for i in range(N - 7):
    for j in range(M - 7):
        cnt1 = 0
        cnt2 = 0

        for x in range(8):
            for y in range(8):
                if (x+y)%2 == 0:
                    if board[i+x][j+y] != 'W':
                        cnt1 += 1
                    if board[i + x][j + y] != 'B':
                        cnt2 += 1
                else:
                    if board[i+x][j+y] != 'B':
                        cnt1 += 1
                    if board[i + x][j + y] != 'W':
                        cnt2 += 1

        ans = min(ans, cnt1, cnt2)

print(ans)