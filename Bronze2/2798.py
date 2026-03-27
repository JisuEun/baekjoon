import sys
input = sys.stdin.readline

N, M = map(int, input().split())
card = list(map(int, input().split()))

card.sort()

ans = 0
diff = 1000000
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            temp = card[i] + card[j] + card[k]
            if M >= temp and M-temp < diff:
                ans = temp
                diff = M-temp

print(ans)

