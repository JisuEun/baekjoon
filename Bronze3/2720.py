import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    cash = int(input())
    q = cash // 25
    d = cash%25 // 10
    n = (cash%25)%10 // 5
    p = ((cash%25)%10)%5 // 1
    print(q, d, n, p)