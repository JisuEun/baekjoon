N = int(input())
num = list(map(int, input().split()))
v = int(input())

cnt = 0
for n in num:
    if n == v:
        cnt += 1
print(cnt)