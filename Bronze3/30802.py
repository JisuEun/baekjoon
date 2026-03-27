import sys
input = sys.stdin.readline

N = int(input())

shirt = list(map(int, input().split()))
T, P = map(int, input().split())

print(sum([shirt[i]//T if shirt[i]%T==0 else shirt[i]//T+1 for i in range(6)]))
print(N//P, N%P)