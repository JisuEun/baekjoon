T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    M_fact = 1
    for i in range(M, 0, -1):
        M_fact *= i
    N_fact = 1
    for i in range(N, 0, -1):
        N_fact *= i

    MN_fact = 1
    for i in range(M-N, 0, -1):
        MN_fact *= i

    print(M_fact//(N_fact*MN_fact))
