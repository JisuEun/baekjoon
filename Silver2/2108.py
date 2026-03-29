import sys
input = sys.stdin.readline

N = int(input())
num = [int(input()) for _ in range(N)]
num.sort()

avg = sum(num) / N

if avg >= 0:
    print(int(avg + 0.5))
else:
    print(int(avg - 0.5))

print(num[N//2])

###

cnt = [0] * 8001

for n in num:
    cnt[n+4000] += 1

max_cnt = max(cnt)
candidate = []

for i in range(8001):
    if cnt[i] == max_cnt:
        candidate.append(i - 4000)

if len(candidate) == 1:
    print(candidate[0])
else:
    candidate.sort()
    print(candidate[1])

###



print(num[-1] - num[0])