import sys
input = sys.stdin.readline

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
data.sort(key=lambda x:(x[1], x[0]))

end = -1
cnt = 0

for i in range(N):
    if end <= data[i][0]:
        end = data[i][1]
        cnt += 1
print(cnt)