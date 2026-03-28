S = [input() for _ in range(3)]

idx = 0
num = 0
for i in range(3):
    try:
        num = int(S[i])
        idx = i
    except:
        continue

ans = num+(3-idx)

if ans%3 == 0 and ans%5==0:
    print("FizzBuzz")
elif ans%3 == 0:
    print("Fizz")
elif ans%5 == 0:
    print("Buzz")
else:
    print(ans)