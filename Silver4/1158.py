N, K = map(int, input().split())

arr = [i for i in range(1, N+1)]
ans = []

index = 0
while len(ans) < N:
    index = (index + K - 1) % len(arr)
    ans.append(str(arr.pop(index)))

print("<", end='')
print(', '.join(ans), end='')
print(">", end='')