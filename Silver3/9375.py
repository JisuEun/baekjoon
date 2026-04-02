import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    t = 0
    dict = {}
    for __ in range(n):
        name, category = input().rstrip().split()
        if not dict.get(category):
            t += 1
            dict[t] = category
        dict[category] = dict.get(category, 0) + 1

    ans = 1
    for i in range(1, t+1):
        ans *= dict[dict[i]] + 1

    print(ans-1)

