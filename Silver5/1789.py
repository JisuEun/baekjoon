S = int(input())

cnt = 0
while S > 0:
    if S > cnt:
        cnt += 1
        S -= cnt
    else:
        break

print(cnt)