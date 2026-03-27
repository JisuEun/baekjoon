import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A = set(A)
M = int(input())
m_data = list(map(int, input().split()))

for m in m_data:
    if m in A:
        print(1)
    else:
        print(0)