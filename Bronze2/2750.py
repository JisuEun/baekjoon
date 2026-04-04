import sys
input = sys.stdin.readline

N = int(input())
num = [int(input()) for _ in range(N)]

num.sort()

for n in num:
    print(n)