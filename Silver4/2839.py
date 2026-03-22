N = int(input())

cnt = 0

while N >= 0:
    if N%5:
        N -= 3
        cnt += 1
    else:
        cnt += N//5
        print(cnt)
        break
else:
    print(-1)