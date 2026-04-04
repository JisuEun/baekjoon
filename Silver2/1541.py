S = input()
data = []
n = ''
for s in S:
    if s.isdigit():
        n += s
    else:
        data.append(n)
        n = ''
        data.append(s)
data.append(n)

# 스택 문제
# - 나옴: 다음 -까지 숫자들 더해두기 -> 한번에 빼기
# + 나옴: 더함

tmp = 0
ans = int(data[0])

i = 1
while i < len(data):
    if data[i] == "+":
        while i < len(data) and data[i] == "+":
            i += 1
            ans += int(data[i])
            i += 1
    elif data[i] == "-":
        i += 1
        tmp += int(data[i])
        i += 1
        while i < len(data) and data[i] == "+":
            i += 1
            tmp += int(data[i])
            i += 1
        ans -= tmp
        tmp = 0

print(ans)