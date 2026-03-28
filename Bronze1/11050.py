N, K = map(int, input().split())

n_fact = 1
for i in range(1, N+1):
    n_fact *= i

k_fact = 1
for i in range(1, K+1):
    k_fact *= i

nk_fact = 1
for i in range(1, N-K+1):
    nk_fact *= i

print(n_fact//(k_fact * nk_fact))
