import sys
input = sys.stdin.readline

K, N = map(int, input().split())
length = [int(input()) for _ in range(K)]

start = 1
end = max(length)
answer = 0

while start <= end:
    mid = (start + end) // 2

    cnt = 0
    for l in length:
        cnt += l // mid

    if cnt >= N:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)