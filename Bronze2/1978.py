N = int(input())
num = list(map(int, input().split()))

ans = 0
for i in range(N):
    cnt = 0
    for j in range(1, num[i]+1):
        if num[i]%j==0:
            cnt += 1
    if cnt == 2:
        ans += 1

print(ans)