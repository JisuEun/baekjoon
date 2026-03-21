import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    case = input().strip()
    case = case.lower()
    if case == case[::-1]:
        print("Yes")
    else:
        print("No")