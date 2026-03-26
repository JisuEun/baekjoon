N = int(input())

num = 1
def factorial(N):
    global num
    if N == 0:
        return
    num *= N
    factorial(N-1)

factorial(N)

cnt = 0
num = str(num)[::-1]

for x in num:
    if x == '0':
        cnt += 1
    elif cnt != 0:
        break

print(cnt)