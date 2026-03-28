L = int(input())
S = input()

r = 31
M = 1234567891

H = 0
for i in range(L):
    H += (ord(S[i])-96)*(r**i)

print(H%M)