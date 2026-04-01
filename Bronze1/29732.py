N, M, K = map(int, input().split())

today = ["."] + list(input().strip())
tomorrow = ["."] * (N+1)
cnt = 0

for i in range(1, N+1):
    if today[i] == "R":
        tomorrow[i] = "R"

        if K+1 <= i <= N-K:
            for j in range(i-K, i+K+1):
                tomorrow[j] = "R"
        elif i < K+1:
            for j in range(0, i+K+1):
                tomorrow[j] = "R"
        elif i > N-K:
            for j in range(i-K, N+1):
                tomorrow[j] = "R"

for t in tomorrow:
    if t == "R":
        cnt += 1

print("Yes" if M >= cnt else "No")

