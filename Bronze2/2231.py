N = int(input())

for i in range(1, N):
    a = list(map(int, str(i)))
    if N == i + sum(a):
        print(i)
        break
else:
    print(0)