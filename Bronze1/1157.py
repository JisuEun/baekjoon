S = input().lower()

dic = {}

for s in S:
    dic[s] = dic.get(s, 0) + 1

ans = []
max = -1
for d in dic:
    if dic[d] > max:
        ans = [d]
        max = dic[d]
    elif dic[d] == max:
        ans.append(d)

if len(ans) == 1:
    print(ans[0].upper())
else:
    print("?")