N = int(input())
data = list(map(int, input().split()))

data.sort()
ans = 0

for i in range(N):
    ans += sum(data[:i+1])

print(ans)