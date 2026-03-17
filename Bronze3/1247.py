import sys
input = sys.stdin.readline

for _ in range(3):
    N = int(input())
    sum = 0
    for i in range(N):
        sum += int(input())
    print("0" if sum == 0 else ("-" if sum < 0 else "+"))