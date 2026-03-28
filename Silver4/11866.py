N, K = map(int, input().split())

arr = [i for i in range(1, N+1)]
ans = []
tmp = K-1

while arr:
    ans.append(arr.pop(tmp))
    if not arr:
        break
    tmp = (tmp + K - 1) % len(arr)

print("<" + ", ".join(map(str, ans)) + ">")